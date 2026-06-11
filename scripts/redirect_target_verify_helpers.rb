# frozen_string_literal: true

# Shared URL normalization and Jekyll published-URL checks for:
#   scripts/verify_redirect_targets_in_jekyll.rb
#   scripts/audit_validurls_targets_vs_jekyll.rb
#
# Keep behavior identical across both tools.
#
# All writers of validurls[...] lines must use escape_js_single_quoted for LHS/RHS payloads.

require "json"
require "set"

module RedirectTargetVerify
  # Full validurls assignment line: leading indent, trailing semicolon required.
  VALIDURLS_LINE_RX = /\A(\s*)validurls\['([^']+)'\]\s*=\s*'([^']*)'\s*;\s*\z/

  module_function

  def parse_validurls_line(line)
    m = VALIDURLS_LINE_RX.match(line.chomp)
    return nil unless m

    { indent: m[1], lhs: m[2], rhs: m[3] }
  end

  # Escape for use inside JavaScript single-quoted string literals. Backslashes first, then quotes.
  # Raises if the value contains characters that cannot appear in a single-line redirect URL cell.
  def escape_js_single_quoted(str)
    s = str.to_s
    if /[\r\n\0]/.match?(s)
      raise ArgumentError, "validurls URL must not contain null or newline: #{s.inspect.byteslice(0, 120)}"
    end

    # Block form avoids gsub replacement specials (e.g. \\' = string after match).
    s.gsub("\\") { "\\\\" }.gsub("'") { "\\'" }
  end

  # Path only (no ?query or #fragment). True if last segment looks like a file with extension.
  def path_looks_like_file?(path)
    seg = File.basename(path.to_s.chomp("/"))
    !seg.empty? && seg.match?(/\.[A-Za-z0-9]{2,}\z/)
  end

  def normalize_url_for_compare(url)
    u = url.to_s.strip.gsub(%r{(?<!:)//+}, "/")
    parts = u.split("#", 2)
    path = parts[0] || ""
    frag = parts[1] ? "##{parts[1]}" : nil
    q = nil
    if path.include?("?")
      pq = path.split("?", 2)
      path = pq[0] || ""
      q = pq[1] ? "?#{pq[1]}" : nil
    end
    path = path.chomp("/")
    has_extension = path_looks_like_file?(path)
    path += "/" unless path.empty? || has_extension
    "#{path}#{q}#{frag}"
  end

  def load_published_urls(map_path)
    JSON.parse(File.read(map_path)).values.map { |u| normalize_url_for_compare(u) }.to_set
  end

  def published_include?(published, raw_target)
    n = normalize_url_for_compare(raw_target)
    base = n.split("#", 2).first
    return true if published.include?(n)
    return true if published.include?(base)

    # Path only: Jekyll map has no ?tab= / ?sdktab= (client-side on the same doc URL)
    path_only = base.split("?", 2).first
    path_norm = normalize_url_for_compare(path_only)
    published.include?(path_norm)
  end

  # Last path segment (no query/fragment), without trailing slash, for basename indexing.
  def path_last_segment(normalized_url)
    base = normalized_url.split("#", 2).first.split("?", 2).first
    base = base.chomp("/")
    seg = File.basename(base)
    seg.empty? ? nil : seg
  end

  # Path segments for prefix comparison (query and fragment stripped). Leading/trailing slashes ignored.
  def path_segments_for_prefix_compare(normalized_url)
    path_part = normalized_url.split("#", 2).first.split("?", 2).first
    path_part.to_s.chomp("/").split("/").reject(&:empty?)
  end

  # Count how many leading segments match (case-sensitive, after normalization).
  def common_prefix_segment_count(segments_a, segments_b)
    len = [segments_a.size, segments_b.size].min
    count = 0
    while count < len && segments_a[count] == segments_b[count]
      count += 1
    end
    count
  end
end
