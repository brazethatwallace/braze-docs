require 'jekyll'
require 'fileutils'

module Jekyll
  class LlmsTxtGenerator
    RAW_MARKDOWN_KEY = "__export_merged_md"
    PUBLIC_MARKDOWN_KEY = "llm_markdown_content"

    SUPPORTED_COLLECTIONS = %w[user_guide developer_guide api partners releases].freeze

    COLLECTION_LABELS = {
      'user_guide' => 'User Guide',
      'developer_guide' => 'Developer Guide',
      'api' => 'API',
      'partners' => 'Technology Partners',
      'releases' => "What's New"
    }.freeze

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

    def self.init
      # Use :post_render (after pages are rendered, before :site, :post_write).
      # At this point markdown_copy_llm's :pre_render hook has populated
      # __export_merged_md / llm_markdown_content on each doc, so we have the
      # high-quality rendered markdown available.
      Jekyll::Hooks.register :site, :post_render do |site|
        next if site.config['__llms_txt_static_files_added']
        register_llms_txt_static_files(site)
        site.config['__llms_txt_static_files_added'] = true
      rescue => e
        Jekyll.logger.error(
          "LlmsTxtGenerator:",
          "Failed to register llms.txt static files: #{e.class}: #{e.message}"
        )
      end

      # Safety net: if for any reason the static file registration didn't run
      # (load order, hook skipped), regenerate via direct file write after the
      # build completes. Skipped when StaticFiles already emitted the outputs.
      Jekyll::Hooks.register :site, :post_write do |site|
        next if site.config['__llms_txt_static_files_added']
        next if site.config['__llms_txt_generated_for_this_build']
        generate_llms_txt(site)
        site.config['__llms_txt_generated_for_this_build'] = true
      rescue => e
        Jekyll.logger.error(
          "LlmsTxtGenerator:",
          "Failed to generate llms.txt files via post_write fallback: #{e.class}: #{e.message}"
        )
      end
    end

    def self.register_llms_txt_static_files(site)
      return unless should_generate_llms_txt?(site)

      SUPPORTED_COLLECTIONS.each do |collection_name|
        documents = collection_documents(site, collection_name)
        next if documents.empty?

        label = COLLECTION_LABELS.fetch(collection_name, collection_name.tr('_', ' ').capitalize)
        llms_content = generate_llms_content(site, documents, label)
        llms_full_content = generate_llms_full_content(site, documents, label)

        site.static_files << InMemoryStaticFile.new(site, "#{collection_name}/llms.txt", llms_content)
        site.static_files << InMemoryStaticFile.new(site, "#{collection_name}/llms-full.txt", llms_full_content)

        Jekyll.logger.info(
          "LlmsTxtGenerator:",
          "Registered llms.txt and llms-full.txt static files for #{documents.length} #{label} pages"
        )
      end
    end

    def self.generate_llms_txt(site)
      return unless should_generate_llms_txt?(site)

      SUPPORTED_COLLECTIONS.each do |collection_name|
        generate_llms_txt_for_collection(site, collection_name)
      end
    end

    def self.generate_llms_txt_for_collection(site, collection_name)
      documents = collection_documents(site, collection_name)
      return if documents.empty?

      label = COLLECTION_LABELS.fetch(collection_name, collection_name.tr('_', ' ').capitalize)
      llms_content = generate_llms_content(site, documents, label)
      llms_full_content = generate_llms_full_content(site, documents, label)

      site_dir = site.dest || File.join(site.source, '_site')
      collection_dir = File.join(site_dir, collection_name)
      FileUtils.mkdir_p(collection_dir)

      File.write(File.join(collection_dir, 'llms.txt'), llms_content)
      File.write(File.join(collection_dir, 'llms-full.txt'), llms_full_content)

      Jekyll.logger.info(
        "LlmsTxtGenerator:",
        "Generated llms.txt and llms-full.txt (fallback path) with #{documents.length} #{label} pages"
      )
    end

    def self.should_generate_llms_txt?(site)
      site.config['llms_txt'] != false &&
      (ENV['JEKYLL_ENV'] == 'production' || site.config['llms_txt'] == true)
    end

    def self.collection_documents(site, collection_name)
      collection = site.collections[collection_name]
      return [] unless collection

      docs = collection.docs.select { |doc| doc.output != false }
      ordered = sort_documents_like_nav_tree(docs)

      seen = {}
      ordered.each { |doc| seen[doc.url.to_s] = true }
      docs.each do |doc|
        ordered << doc unless seen[doc.url.to_s]
      end

      ordered
    end

    def self.sort_documents_like_nav_tree(documents)
      tree = build_nav_tree(documents)
      ordered = []
      flatten_nav_tree(tree, ordered)
      ordered
    end

    def self.build_nav_tree(documents)
      root = {}

      documents.each do |doc|
        path_parts = doc.url.to_s.split('/')
        path_parts.shift # leading empty value
        path_parts.shift # collection segment (e.g. developer_guide, user_guide)

        current = root
        max_index = path_parts.length - 1

        path_parts.each_with_index do |segment, idx|
          next if segment.to_s.empty?

          key = segment.downcase
          current[:nav_list] ||= {}
          current[:children] ||= {}

          if idx < max_index
            unless current[:nav_list].key?(key)
              current[:nav_list][key] = {
                key: key,
                title: decode_slug_title(segment),
                weight: nil
              }
            end
            current[:children][key] ||= {}
            current = current[:children][key]
            next
          end

          current[:nav_list][key] = {
            key: key,
            title: page_title_for(doc, ""),
            weight: parse_weight(doc.data['page_order'])
          }
          current[:nav_pages] ||= {}
          current[:nav_pages][key] = doc unless doc.data['config_only']
        end
      end

      root
    end

    def self.flatten_nav_tree(node, output)
      nav_list = node[:nav_list] || {}
      return if nav_list.empty?

      sorted_entries = nav_list.values.sort_by do |entry|
        [entry[:weight].nil? ? 1 : 0, entry[:weight]]
      end

      sorted_entries.each do |entry|
        key = entry[:key]
        page = (node[:nav_pages] || {})[key]
        output << page if page

        child = (node[:children] || {})[key]
        flatten_nav_tree(child, output) if child
      end
    end

    def self.parse_weight(value)
      return nil if value.nil?

      Float(value)
    rescue
      nil
    end

    def self.decode_slug_title(text)
      text.to_s
          .gsub("%20", ' ')
          .gsub("+", ' ')
          .gsub('_', ' ')
          .gsub("%26", '&')
          .gsub("%2F", '/')
          .gsub("%3A", ':')
          .gsub("%3F", '?')
          .gsub("%2C", ',')
          .gsub("%2B", '+')
    end

    def self.page_title_for(doc, markdown)
      explicit_title = doc.data['article_title'] || doc.data['nav_title'] || doc.data['title']
      explicit = decode_slug_title(explicit_title.to_s).strip
      return explicit unless explicit.empty?

      extract_markdown_headings(markdown).each do |heading|
        return heading[:text] if heading[:level] == 1
      end

      "Untitled"
    end

    def self.page_markdown_for(doc)
      merged = doc.data[RAW_MARKDOWN_KEY] || doc.data[PUBLIC_MARKDOWN_KEY]
      content = merged.to_s.strip
      content = doc.content.to_s if content.empty?
      content.to_s
    end

    def self.path_for_llms(doc, site)
      base_path = site.config['baseurl'].to_s
      doc_path = doc.url.to_s
      suffix = doc_path.end_with?('/') ? 'index.md' : '/index.md'
      "#{base_path}#{doc_path}#{suffix}"
    end

    def self.extract_markdown_headings(markdown)
      headings = []
      in_code_block = false

      markdown.to_s.each_line do |line|
        stripped = line.strip

        if stripped.start_with?("```")
          in_code_block = !in_code_block
          next
        end
        next if in_code_block

        match = line.match(/^(#+)\s+(.+?)\s*#*\s*$/)
        next unless match

        heading_text = cleanup_inline_markdown(match[2])
        next if heading_text.empty?

        headings << {
          level: match[1].length,
          text: heading_text
        }
      end

      headings
    end

    def self.cleanup_inline_markdown(text)
      clean = text.to_s.dup
      clean.gsub!(/`([^`]+)`/, '\1')
      clean.gsub!(/\[([^\]]+)\]\([^)]+\)/, '\1')
      clean.gsub!(/\*\*([^*]+)\*\*/, '\1')
      clean.gsub!(/\*([^*]+)\*/, '\1')
      clean.gsub!(/_{1,2}([^_]+)_{1,2}/, '\1')
      clean.gsub!(/\{%\s*.*?\s*%\}/, '')
      clean.gsub!(/\{\{\s*.*?\s*\}\}/, '')
      clean.gsub!(/\s+/, ' ')
      clean.strip
    end

    def self.extract_summary(markdown)
      in_code_block = false
      markdown.to_s.each_line do |line|
        stripped = line.strip
        if stripped.start_with?("```")
          in_code_block = !in_code_block
          next
        end
        next if in_code_block
        next if stripped.empty?
        next if stripped.match?(/\A<\/?[\w:-]+[^>]*>\z/)
        next if stripped.start_with?('#', '>', '-', '*', '|', '{%', '{{')

        summary = cleanup_inline_markdown(stripped)
        return summary unless summary.empty?
      end

      ""
    end

    def self.strip_frontmatter(markdown)
      text = markdown.to_s
      return text unless text.start_with?("---\n")

      parts = text.split(/^---\s*$\n?/, 3)
      return text if parts.length < 3

      parts[2].to_s
    end

    def self.normalize_full_text(markdown)
      clean = strip_frontmatter(markdown)
      clean = clean.gsub(/\r\n?/, "\n")
      clean = clean.gsub(/\t/, "  ")
      clean = clean.gsub(/\{%\s*.*?\s*%\}/m, '')
      clean = clean.gsub(/\{\{\s*.*?\s*\}\}/m, '')
      clean = clean.gsub(/\n{3,}/, "\n\n")
      clean.strip
    end

    def self.strip_html(text)
      text.to_s.gsub(/<[^>]*>/, ' ').gsub(/\s+/, ' ').strip
    end

    def self.full_text_fallback_from_frontmatter(doc)
      lines = []
      top = strip_html(doc.data['guide_top_text'])
      desc = strip_html(doc.data['description'])

      guide_header = strip_html(doc.data['guide_top_header'])
      lines << guide_header unless guide_header.empty?
      lines << top unless top.empty?
      lines << desc unless desc.empty?

      featured = doc.data['guide_featured_list']
      if featured.is_a?(Array) && !featured.empty?
        lines << "Featured:"
        featured.each do |item|
          next unless item.is_a?(Hash)
          name = strip_html(item['name'])
          lines << "- #{name}" unless name.empty?
        end
      end

      lines.join("\n").strip
    end

    def self.full_text_for_doc(doc, markdown)
      normalized = normalize_full_text(markdown)
      return normalized unless normalized.empty?

      full_text_fallback_from_frontmatter(doc)
    end

    def self.generate_llms_content(site, documents, label)
      content = <<~LLMS
        # Braze Documentation

        Index of all #{label} pages and their headings.

        ## #{label}

      LLMS

      documents.each do |doc|
        markdown = page_markdown_for(doc)
        title = page_title_for(doc, markdown)
        path = path_for_llms(doc, site)
        summary = extract_summary(markdown)
        headings = extract_markdown_headings(markdown)

        if summary.empty?
          content << "- [#{title}](#{path})\n"
        else
          content << "- [#{title}](#{path}): #{summary}\n"
        end

        headings.each do |heading|
          indent = '  ' * heading[:level]
          content << "#{indent}- #{'#' * heading[:level]} #{heading[:text]}\n"
        end

        content << "\n"
      end

      content
    end

    def self.generate_llms_full_content(site, documents, label)
      content = <<~LLMS
        # Braze #{label} Full Text

        Consolidated full markdown text for all pages in the #{label} collection.

      LLMS

      documents.each do |doc|
        markdown = page_markdown_for(doc)
        title = page_title_for(doc, markdown)
        path = path_for_llms(doc, site)
        normalized = full_text_for_doc(doc, markdown)
        next if normalized.empty?

        content << "# #{title}\n\n"
        content << "Source: #{path}\n\n"
        content << "#{normalized}\n\n"
      end

      content
    end
  end

end

# Initialize the plugin
Jekyll::LlmsTxtGenerator.init
