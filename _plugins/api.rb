module Api
  class ApiInfoBlock < Liquid::Block
    def initialize(tag_name, tabonly = 'false', tokens)
        super
        # @tabclass = 'tab_toggle'
        @apiid = 'api_' + (0...12).map { (97 + rand(26)).chr }.join
    end
    def render(context)
      site = context.registers[:site]
      converter = site.find_converter_instance(Jekyll::Converters::Markdown)
      content = converter.convert(super)

      # Build a search index from the event name (h2), tags, and description
      # so JS can search field-level terms without reading lazy tab pane content.
      h2_match    = content.match(/<h2[^>]*>(.*?)<\/h2>/i)
      tags_match  = content.match(/data-tags=['"]([^'"]*)['"]/i)
      desc_match  = content.match(/class='api_tags'[^>]*><\/div>\s*<p>(.*?)<\/p>/m)
      keywords = [
        h2_match   ? h2_match[1].gsub(/<[^>]+>/, '').strip   : '',
        tags_match ? tags_match[1].strip                      : '',
        desc_match ? desc_match[1].gsub(/<[^>]+>/, '').strip  : ''
      ].reject(&:empty?).join(' ').downcase

      return "<div id='#{@apiid}' class='api_div' data-search-keywords='#{keywords}'>#{content}</div>"
    end
  end

  class ApiMethodBlock < Liquid::Block
      def initialize(tag_name, params, tokens)
          super
          @methodtype, @coreparam = params.split(' ').map(&:strip)
      end

      def render(context)
          site = context.registers[:site]
          converter = site.find_converter_instance(Jekyll::Converters::Markdown)
          content = converter.convert(super)
          apicontent = "<div class='api_type'><div class='method #{@methodtype.downcase} '>#{ @methodtype }</div>#{content}"
          unless @coreparam.nil?
            coretype, coreurl = @coreparam.split('|')
            if coreurl.nil?
              apicontent += "<div class='coreclass #{coretype.downcase} '>#{ coretype.gsub(/\_/,' ') }</div>"
            else
              apicontent += "<div class='coreclass #{coretype.downcase} '><a href=\"#{coreurl}\">#{ coretype.gsub(/\_/,' ') }</a></div>"
            end
          end
          apicontent += "</div>"
          return apicontent
      end
  end
  class ApiTagsBlock < Liquid::Block
      def initialize(tag_name, param, tokens)
          super
      end

      def render(context)
        content = super.strip
        return "<div class='api_tags' data-tags='#{content}' data-tags-lower='#{content.downcase}'></div>"
      end
  end
  class ApiReferenceBlock < Liquid::Block
      def initialize(tag_name, param, tokens)
          super
          @reftype = param.downcase.strip
      end

      def render(context)
        content = super.strip
        reftext = ''
        case @reftype
        when "swagger"
          reftext = 'Test me with Swagger'
        when "postman"
          reftext = 'See me in Postman'
        end
        return "<div class='api_reference #{@reftype}'><a href='#{content}' class='seeme'>#{reftext}</a></div>"
      end
  end
end

Liquid::Template.register_tag("api", Api::ApiInfoBlock)
Liquid::Template.register_tag("apimethod",  Api::ApiMethodBlock)
Liquid::Template.register_tag("apitags",  Api::ApiTagsBlock)
Liquid::Template.register_tag("apiref",  Api::ApiReferenceBlock)
