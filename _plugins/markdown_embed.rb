# https://github.com/dimitri-koenig/jekyll-plugins
# modified to allow variable url
require_relative 'braze_docs_http'
require 'uri'

module Jekyll

  class EmbedMarkdown < Liquid::Tag

    def initialize(tag_name, markup, tokens)
      @url = markup.strip
      super
    end

    def render(context)
      site = context.registers[:site]
      embedmarkdown = site.config['markdown_api']
      if @url.empty?
        embedmarkdown = false
      end
      if ENV["MARKDOWN_API"].to_s.downcase != 'true'
        embedmarkdown = false
      end
      if embedmarkdown
        url = @url.strip

        if url.downcase.end_with?('.md')
          cache = context['site']['data']
          hit, cached = BrazeDocsHttp.cache_read(cache, url)
          if hit
            puts 'Using cache for markdown: ' + url
            return cached
          end

          puts 'Fetching content of markdown url: ' + url
          unless url =~ URI::regexp
            puts 'Error fetching markdown: ' + url
            return ''
          end

          @results = fetchContent(url)

          if @results.code != '200'
            puts 'Error returning results: ' + url
            return ''
          elsif @results.body
            converter = site.find_converter_instance(Jekyll::Converters::Markdown)
            rendered_markdown = converter.convert(@results.body.force_encoding('UTF-8'))
            BrazeDocsHttp.cache_write(cache, url, rendered_markdown)
            return cache[url]
          else
            puts 'Empty content from : ' + url
            return ''
          end
        else
          return ''
        end
      else
        return ''
      end
    end

    def fetchContent(url)
      BrazeDocsHttp.get(url)
    end
  end
end

Liquid::Template.register_tag('markdown_embed', Jekyll::EmbedMarkdown)
