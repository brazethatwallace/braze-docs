# frozen_string_literal: true

module Jekyll
  # Assembles llms.txt / llms-full.txt content from Jekyll collections.
  # No file I/O — returns structured artifacts for LlmsWriter.
  class LlmsCollector
    RAW_MARKDOWN_KEY = "__export_merged_md"
    PUBLIC_MARKDOWN_KEY = "llm_markdown_content"

    DEFAULT_OUTPUT_INDEX = "llms.txt"
    DEFAULT_OUTPUT_FULL = "llms-full.txt"
    CONFIG_DATA_KEY = "llms_config"

    CollectionArtifacts = Struct.new(
      :collection_name,
      :label,
      :document_count,
      :index_relative_path,
      :full_relative_path,
      :index_content,
      :full_content,
      keyword_init: true
    )

    def self.collect(site)
      return [] unless should_generate_llms_txt?(site)

      config = llms_config(site)
      index_name = output_filename(config, :index)
      full_name = output_filename(config, :full)

      configured_collections(config).filter_map do |collection_name, label|
        documents = collection_documents(site, collection_name)
        next if documents.empty?

        CollectionArtifacts.new(
          collection_name: collection_name,
          label: label,
          document_count: documents.length,
          index_relative_path: "#{collection_name}/#{index_name}",
          full_relative_path: "#{collection_name}/#{full_name}",
          index_content: generate_llms_content(site, documents, label),
          full_content: generate_llms_full_content(site, documents, label)
        )
      end
    end

    def self.should_generate_llms_txt?(site)
      site.config['llms_txt'] != false &&
        (ENV['JEKYLL_ENV'] == 'production' || site.config['llms_txt'] == true)
    end

    def self.llms_config(site)
      raw = site.data[CONFIG_DATA_KEY]
      return raw if raw.is_a?(Hash)

      Jekyll.logger.warn(
        "LlmsTxtGenerator:",
        "Missing or invalid _data/#{CONFIG_DATA_KEY}.yml; no collections will be generated."
      )
      {}
    end

    def self.configured_collections(config)
      entries = config['collections']
      unless entries.is_a?(Array) && !entries.empty?
        Jekyll.logger.warn(
          "LlmsTxtGenerator:",
          "No collections listed in _data/#{CONFIG_DATA_KEY}.yml."
        )
        return []
      end

      entries.filter_map do |entry|
        next unless entry.is_a?(Hash)

        name = entry['name'].to_s.strip
        next if name.empty?

        label = entry['label'].to_s.strip
        label = default_collection_label(name) if label.empty?
        [name, label]
      end
    end

    def self.output_filename(config, kind)
      files = config['output_files']
      files = {} unless files.is_a?(Hash)

      case kind
      when :index
        name = files['index'].to_s.strip
        name.empty? ? DEFAULT_OUTPUT_INDEX : name
      when :full
        name = files['full'].to_s.strip
        name.empty? ? DEFAULT_OUTPUT_FULL : name
      else
        raise ArgumentError, "Unknown output kind: #{kind}"
      end
    end

    def self.default_collection_label(collection_name)
      collection_name.to_s.tr('_', ' ').capitalize
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
    rescue StandardError
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

    private_class_method :configured_collections,
                         :output_filename,
                         :default_collection_label,
                         :collection_documents,
                         :sort_documents_like_nav_tree,
                         :build_nav_tree,
                         :flatten_nav_tree,
                         :parse_weight,
                         :decode_slug_title,
                         :page_title_for,
                         :page_markdown_for,
                         :path_for_llms,
                         :extract_markdown_headings,
                         :cleanup_inline_markdown,
                         :extract_summary,
                         :strip_frontmatter,
                         :normalize_full_text,
                         :strip_html,
                         :full_text_fallback_from_frontmatter,
                         :full_text_for_doc,
                         :generate_llms_content,
                         :generate_llms_full_content
  end
end
