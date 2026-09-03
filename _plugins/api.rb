module Api
  # Builds data-search-keywords for {% api %} blocks from _data/api_metadata.yml.
  class Metadata
    def self.for_site(site)
      data = site.respond_to?(:data) ? site.data : nil
      config = data && data['api_metadata']
      @instances ||= {}
      cache_key = config.object_id
      @instances[cache_key] ||= new(config)
    end

    def self.reset_cache!
      @instances = {}
    end

    def initialize(config)
      if config.nil? || config.empty?
        raise ArgumentError, 'API metadata config is missing. Add extraction patterns to _data/api_metadata.yml.'
      end

      @keyword_fields = Array(config.fetch('keyword_fields'))
      @pattern_specs = stringify_keys(config.fetch('patterns'))
      @transform_specs = stringify_keys(config.fetch('transforms', {}))
      @escapes = config.fetch('keyword_escaping')
      @compiled_patterns = compile_all(@pattern_specs)
      @compiled_transforms = compile_all(@transform_specs)
    end

    def wrap(apiid, content)
      "<div id='#{apiid}' class='api_div' data-search-keywords='#{keywords_for(content)}'>#{content}</div>"
    end

    def keywords_for(content)
      parts = @keyword_fields.map { |field| extract_field(content, field.to_s) }
      escape_keywords(parts.reject(&:empty?).join(' ').downcase)
    end

    private

    def extract_field(content, field)
      spec = @pattern_specs[field]
      raise ArgumentError, "api_metadata.yml keyword_fields includes unknown pattern '#{field}'." unless spec

      regex = @compiled_patterns.fetch(field)
      mode = spec.fetch('mode', 'match').to_s

      if mode == 'scan'
        values = content.scan(regex).flatten
        values = values.map { |value| apply_transforms(value.to_s, spec) }.reject(&:empty?)
        values = values.uniq if spec['unique']
        return values.join(spec.fetch('join', ' '))
      end

      match = content.match(regex)
      return '' unless match

      apply_transforms(match[Integer(spec.fetch('capture', 1))].to_s, spec)
    end

    def apply_transforms(value, spec)
      Array(spec['transforms']).reduce(value) do |result, name|
        apply_transform(result, name.to_s)
      end
    end

    def apply_transform(value, name)
      return value.strip if name == 'strip'

      spec = @transform_specs[name]
      raise ArgumentError, "api_metadata.yml references unknown transform '#{name}'." unless spec

      regex = @compiled_transforms.fetch(name)
      value.gsub(regex, spec.fetch('replacement', '').to_s)
    end

    def escape_keywords(keywords)
      escaped = keywords.dup
      @escapes.each { |from, to| escaped = escaped.gsub(from.to_s, to.to_s) }
      escaped
    end

    def compile_all(specs)
      specs.each_with_object({}) do |(name, spec), compiled|
        next unless spec.is_a?(Hash) && spec['regex']

        compiled[name.to_s] = compile_regex(spec)
      end
    end

    def compile_regex(spec)
      flags = 0
      options = spec.fetch('options', '').to_s
      flags |= Regexp::IGNORECASE if options.include?('i')
      flags |= Regexp::MULTILINE if options.include?('m')
      flags |= Regexp::EXTENDED if options.include?('x')
      Regexp.new(spec.fetch('regex').to_s, flags)
    end

    def stringify_keys(hash)
      hash.each_with_object({}) { |(key, value), out| out[key.to_s] = value }
    end
  end

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

      # Build a search index so JS can search without touching lazy tab content.
      # At this point `content` still has the full rendered tab HTML (before the
      # lazy-loading plugin offloads panes).
      Metadata.for_site(site).wrap(@apiid, content)
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
