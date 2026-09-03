# frozen_string_literal: true

# Pure extraction of internal anchor-bearing links from a document's raw
# source text. No Jekyll dependency -- used to build a link index for both
# the base ref and HEAD in validate_doc_redirects.rb.
#
# Deliberately narrower in scope than scripts/find_broken_links.ts: this
# module only returns links that carry a "#anchor" fragment, since page
# existence (no anchor) is already validated by the "Broken internal links"
# CI check. Path-resolution logic mirrors convertLinkToMarkdownPath in
# find_broken_links.ts.
module DocAnchorLinks
  # target_path is a best guess from the URL's shape; target_url is the URL the
  # link actually points at, so a caller holding Jekyll's URL map can correct
  # target_path for pages whose `permalink` frontmatter breaks the convention
  # (see resolve_doc_path). Same-page links leave target_url nil.
  Link = Struct.new(:source_file, :kind, :raw_url, :target_path, :target_url, :anchor, keyword_init: true)

  INLINE_MD_RE = /(!?)\[.*?\]\((.*?)\)/m.freeze
  REF_DEF_RE = /^\s*\[([^\]]+)\]:\s*(.+)$/.freeze
  REF_LINK_RE = /(!?)\[.*?\]\[([^\]]+)\]/.freeze
  HTML_A_RE = /<a\s+[^>]*href=["']([^"']+)["']/i.freeze

  def self.extract(source_file, raw_content)
    content = strip_non_prose(raw_content)
    links = []

    ref_map = {}
    content.scan(REF_DEF_RE) { |ref_id, url| ref_map[ref_id.strip] = url.strip }

    content.scan(INLINE_MD_RE) do |bang, url|
      next if bang == "!"

      add_link(links, source_file, :md, url)
    end

    content.scan(REF_LINK_RE) do |bang, ref_id|
      next if bang == "!"

      url = ref_map[ref_id.strip]
      add_link(links, source_file, :md, url) if url
    end

    content.scan(HTML_A_RE) do |url,|
      add_link(links, source_file, :html, url)
    end

    links
  end

  def self.strip_non_prose(content)
    content
      .gsub(/```.*?```/m, "")
      .gsub(/`[^`\n]+`/, "")
      .gsub(%r{<script.*?</script>}mi, "")
      .gsub(%r{<style.*?</style>}mi, "")
  end
  private_class_method :strip_non_prose

  def self.add_link(links, source_file, kind, raw_url)
    clean = raw_url.to_s.gsub(/\{\{\s*site\.baseurl\s*\}\}/, "").strip.split(" ").first.to_s

    # HTML anchors use an absolute /docs/-prefixed path per site convention
    # (docs/contributing/style_guide.md); normalize to the same no-/docs/
    # form markdown links use once {{site.baseurl}} is stripped.
    clean = clean.sub(%r{\A/docs/}, "/") if clean.start_with?("/docs/")
    clean = "/" if clean == "/docs"

    return unless clean.start_with?("/") || clean.start_with?("#")
    return if clean.start_with?("//") # protocol-relative external URL

    path_part, _, anchor = clean.partition("#")
    path_part = path_part.split("?").first.to_s
    return if anchor.empty?

    if path_part.empty?
      links << Link.new(source_file: source_file, kind: kind, raw_url: raw_url,
                         target_path: source_file, anchor: anchor)
      return
    end

    # A bare "/" (e.g. "/docs/#anchor" normalized above) points at the site
    # root, not the current document -- treating it as same-page (as an
    # earlier version of this code did) is wrong whenever source_file isn't
    # itself the homepage. There's no real _docs/ file behind the bare root
    # in this Jekyll site (the homepage is served separately, outside the
    # _docs/ collection this checker scans), so there's nothing correct to
    # resolve it to; skip it rather than guess.
    return if path_part == "/"

    last_segment = path_part.split("/").last.to_s
    return if last_segment.include?(".") # points at a real file (image, pdf, etc.), not a page

    links << Link.new(source_file: source_file, kind: kind, raw_url: raw_url,
                       target_path: resolve_doc_path(path_part), target_url: path_part,
                       anchor: anchor)
  end
  private_class_method :add_link

  # Mirrors convertLinkToMarkdownPath in scripts/find_broken_links.ts. Pages
  # that set a custom `permalink` do not follow this convention; callers with a
  # Jekyll URL map should prefer it over this guess (find_broken_links.ts makes
  # the same allowance by matching links against declared permalinks).
  def self.resolve_doc_path(path_part)
    trimmed = path_part.sub(%r{\A/}, "").sub(%r{/\z}, "")
    segments = trimmed.split("/")
    return "_docs/#{segments[0]}.md" if segments.length == 1

    "_docs/_#{segments[0]}/#{segments[1..].join('/')}.md"
  end
  private_class_method :resolve_doc_path
end
