# frozen_string_literal: true

require 'fileutils'

module Jekyll
  # Writes LlmsCollector output to disk via Jekyll static files or a fallback path.
  class LlmsWriter
    # Backed-by-memory static file written through Jekyll's normal write phase.
    # Using a real StaticFile instead of an out-of-band File.write() ensures the
    # LLM index files are emitted by the same pipeline as every other asset,
    # which is required for them to land in the deployed _site artifact in
    # environments where post_write hooks behave unexpectedly.
    class InMemoryStaticFile < Jekyll::StaticFile
      def initialize(site, dest_subpath, content)
        @site = site
        @base = site.source
        @dir = File.dirname(dest_subpath)
        @name = File.basename(dest_subpath)
        @relative_path = dest_subpath.start_with?('/') ? dest_subpath : "/#{dest_subpath}"
        @extname = File.extname(@name)
        @collection = nil
        @content = content.to_s
        @modified_time = Time.now
        @data = {}
      end

      def path
        nil
      end

      def url
        @relative_path
      end

      def destination(dest)
        File.join(dest, @relative_path)
      end

      def modified?
        true
      end

      def write(dest)
        dest_path = destination(dest)
        FileUtils.mkdir_p(File.dirname(dest_path))
        File.open(dest_path, 'wb') { |f| f.write(@content) }
        Jekyll.logger.debug("LlmsTxtGenerator:", "Wrote #{@relative_path} (#{@content.bytesize} bytes)")
        true
      end
    end

    def self.register_static_files(site, artifacts)
      artifacts.each do |artifact|
        site.static_files << InMemoryStaticFile.new(site, artifact.index_relative_path, artifact.index_content)
        site.static_files << InMemoryStaticFile.new(site, artifact.full_relative_path, artifact.full_content)

        index_name = File.basename(artifact.index_relative_path)
        full_name = File.basename(artifact.full_relative_path)
        Jekyll.logger.info(
          "LlmsTxtGenerator:",
          "Registered #{index_name} and #{full_name} static files for #{artifact.document_count} #{artifact.label} pages"
        )
      end
    end

    def self.write_fallback(site, artifacts)
      site_dir = site.dest || File.join(site.source, '_site')

      artifacts.each do |artifact|
        collection_dir = File.join(site_dir, artifact.collection_name)
        FileUtils.mkdir_p(collection_dir)

        index_name = File.basename(artifact.index_relative_path)
        full_name = File.basename(artifact.full_relative_path)
        File.write(File.join(collection_dir, index_name), artifact.index_content)
        File.write(File.join(collection_dir, full_name), artifact.full_content)

        Jekyll.logger.info(
          "LlmsTxtGenerator:",
          "Generated #{index_name} and #{full_name} (fallback path) with #{artifact.document_count} #{artifact.label} pages"
        )
      end
    end
  end
end
