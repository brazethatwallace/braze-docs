require 'jekyll_asset_pipeline'

module JekyllAssetPipeline
  def self.normalize_utf8(content)
    normalized_content = content.dup.force_encoding(Encoding::UTF_8)
    return normalized_content if normalized_content.valid_encoding?

    raise Encoding::InvalidByteSequenceError,
          "Asset content is not valid UTF-8 after normalization"
  end

  class SassConverter < JekyllAssetPipeline::Converter
    require 'sassc'

    def self.filetype
      '.scss'
    end

    def convert
      return SassC::Engine.new(@content, syntax: :scss, load_paths: [@dirname]).render
    end

  end

  class CssCompressor < JekyllAssetPipeline::Compressor
    require 'sassc'

    def self.filetype
      '.css'
    end

    def compress
      normalized_content = JekyllAssetPipeline.normalize_utf8(@content)
      return SassC::Engine.new(
        normalized_content,
        syntax: :css,
        load_paths: [@dirname],
        style: :compressed
      ).render
    end

  end

  class JavaScriptCompressor < JekyllAssetPipeline::Compressor
    require 'uglifier'

    def self.filetype
      '.js'
    end

    def compress
      # YUI::JavaScriptCompressor.new(:munge => true).compress(@content)
      normalized_content = JekyllAssetPipeline.normalize_utf8(@content)
      Uglifier.new(:harmony => true).compile(normalized_content)
    end
  end

  # Override Jekyll Asset Pipeline method so it uses file content instead of
  # timestamp to determined MD5 hash value
  class Pipeline
    @@cached_manifest = {}
    require 'sassc'

    # rubocop:enable Metrics/ClassLength
    def self.hash(source, manifest, options = {})
      options = DEFAULTS.merge(options)
      # use cache manifest if exist
      if @@cached_manifest[manifest]
        return @@cached_manifest[manifest]
      else
        begin
          # read file to determine cache md5 manifest. This will prevent webhost from
          # generating new hash names when files are not changed
          cached_md5 = YAML.safe_load(manifest).map! do |path|
            # Fix issue with scsss import changes not updating MD5 hash
            if (path.end_with?('.scss'))
              file_path = File.join(source, path)
              Digest::MD5.hexdigest(SassC::Engine.new(IO.read(file_path), syntax: :scss, load_paths: [File.dirname(file_path)]).render).to_sym
            else
              Digest::MD5.hexdigest(IO.read(File.join(source, path))).to_sym
            end
          end
          # use options as another hash identifier in case it changes
          cached_md5.push(options.to_s)
          @@cached_manifest[manifest] = Digest::MD5.hexdigest(cached_md5.join('|'))
          return @@cached_manifest[manifest]
        rescue StandardError => e
          puts "Failed to generate hash from provided manifest: #{e.message}"
          raise e
        end
      end
    end

  end

  # Emit deferred script tags for bundled JavaScript assets.
  class DeferredJavaScriptTagTemplate < JekyllAssetPipeline::Template
    def self.filetype
      '.js'
    end

    def self.priority
      1
    end

    def html
      "<script src='#{output_path}/#{@filename}' " \
        "type='text/javascript' defer></script>"
    end
  end
end
