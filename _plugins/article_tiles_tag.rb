require 'cgi'
require 'yaml'

module Jekyll
  module Tags
    # Renders link tiles from a YAML list in the tag body, so tile data lives next
    # to the heading instead of in page front matter.
    #
    # {% article_tiles %}
    # - name: Email setup
    #   link: /docs/user_guide/channels/email/email_setup
    # {% endarticle_tiles %}
    class ArticleTilesTag < Liquid::Block
      def render(context)
        site = context.registers[:site]
        baseurl = site.config['baseurl'] || '/docs'
        yaml_text = super(context).to_s.strip
        return '' if yaml_text.empty?

        tiles = YAML.safe_load(yaml_text)
        unless tiles.is_a?(Array)
          raise ArgumentError, "article_tiles: expected a YAML list of tiles, got #{tiles.class}"
        end

        items = tiles.filter_map { |tile| render_tile(tile, site, baseurl) }
        return '' if items.empty?

        "<ul class=\"guide_tiles\">#{items.join}</ul>"
      end

      private

      def render_tile(tile, site, baseurl)
        return if tile.nil?
        tile = stringify_keys(tile)
        name = tile['name'].to_s.strip
        href = resolve_href(tile['link'].to_s.strip, site, baseurl)
        return if name.empty? || href.empty?

        description = tile['description'].to_s.strip
        description_html = description.empty? ? '' : "<span class=\"guide_tile_description\">#{CGI.escapeHTML(description)}</span>"
        tile_class = description.empty? ? 'guide_tile' : 'guide_tile guide_tile_has_description'

        "<li><a href=\"#{CGI.escapeHTML(href)}\"><div class=\"#{tile_class}\"><span class=\"guide_tile_text\"><span class=\"guide_tile_title\">#{CGI.escapeHTML(name)}</span>#{description_html}</span></div></a></li>"
      end

      def stringify_keys(hash)
        return {} unless hash.is_a?(Hash)

        hash.each_with_object({}) { |(key, value), out| out[key.to_s] = value }
      end

      def resolve_href(link, site, baseurl)
        href = link.gsub('{{site.baseurl}}', baseurl).gsub('{{ site.baseurl }}', baseurl)
        return href if href.include?('://')

        href = "#{baseurl}#{href}" unless href.start_with?('/docs')
        apply_multi_lang(href, site)
      end

      def apply_multi_lang(url, site)
        lang = site.config['language'] || 'en'
        return url if lang == 'en' || localized_docs_url?(url, site)

        url.sub(%r{\A/docs/}, "/docs/#{lang}/")
      end

      def localized_docs_url?(url, site)
        locales = Array(site.data.dig('locales', 'supported')).map(&:to_s).reject { |code| code == 'en' }
        return false if locales.empty?

        pattern = %r{\A/docs/(?:#{locales.sort_by { |code| -code.length }.map { |code| Regexp.escape(code) }.join('|')})/}
        url.match?(pattern)
      end
    end
  end
end

Liquid::Template.register_tag('article_tiles', Jekyll::Tags::ArticleTilesTag)
