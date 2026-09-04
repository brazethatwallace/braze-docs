# frozen_string_literal: true

# Detects page-level needs for heavy optional assets (Mermaid, Swiper, MathJax)
# so html_include.html can load them only when required.
module Jekyll
  module ConditionalAssets
    MERMAID_PATTERN = /```mermaid\b|language-mermaid/i
    SWIPER_PATTERN = /\{%\s*-?\s*gallery\b|swiper-container|swiper-wrapper|new\s+Swiper/i
    MATHJAX_PATTERN = /\$\$\\(?:text|frac|sum|int|dfrac)\{/
    INCLUDE_PATTERN = /\{%\s*-?\s*(?:multi_lang_include|include)\s+([^%\s"']+|"[^"]+"|'[^']+')/m

    module_function

    def asset_flags_for(content)
      text = content.to_s
      {
        mermaid: text.match?(MERMAID_PATTERN),
        swiper: text.match?(SWIPER_PATTERN),
        mathjax: text.match?(MATHJAX_PATTERN)
      }
    end

    def merge_flags(*flag_sets)
      flag_sets.reduce({ mermaid: false, swiper: false, mathjax: false }) do |merged, flags|
        merged.merge(flags) { |_, left, right| left || right }
      end
    end

    def scan_item(item)
      visited = Set.new
      flags = asset_flags_for(item.content)
      include_flags = referenced_include_paths(item).map do |path|
        scan_include_file(item.site, path, visited)
      end
      merge_flags(flags, *include_flags)
    end

    def referenced_include_paths(item)
      item.content.to_s.scan(INCLUDE_PATTERN).filter_map do |match|
        match[0].to_s.delete_prefix('"').delete_suffix('"').delete_prefix("'").delete_suffix("'")
      end
    end

    def scan_include_file(site, file, visited)
      path = resolve_include_path(site, file)
      return { mermaid: false, swiper: false, mathjax: false } unless path
      return { mermaid: false, swiper: false, mathjax: false } if visited.include?(path)

      visited.add(path)
      content = File.read(path, **site.file_read_opts)
      flags = asset_flags_for(content)
      nested = content.scan(INCLUDE_PATTERN).filter_map do |match|
        nested_file = match[0].to_s.delete_prefix('"').delete_suffix('"').delete_prefix("'").delete_suffix("'")
        scan_include_file(site, nested_file, visited)
      end
      merge_flags(flags, *nested)
    end

    def resolve_include_path(site, file)
      candidates = [
        File.join('_includes', file),
        File.join('_includes', "#{file}.md"),
        File.join('_includes', "#{file}.html")
      ]

      candidates
        .map { |candidate| File.join(site.source, candidate) }
        .find { |path| File.file?(path) }
    end

    def apply_flags!(item)
      flags = scan_item(item)
      item.data['needs_mermaid'] = item.data['needs_mermaid'] == true || flags[:mermaid]
      item.data['needs_swiper'] = item.data['needs_swiper'] == true || flags[:swiper]
      item.data['needs_mathjax'] = item.data['needs_mathjax'] == true || flags[:mathjax]
    end
  end

  Jekyll::Hooks.register [:pages, :documents], :pre_render do |item, _payload|
    Jekyll::ConditionalAssets.apply_flags!(item)
  end
end
