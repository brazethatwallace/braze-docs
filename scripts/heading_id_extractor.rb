# scripts/heading_id_extractor.rb
# frozen_string_literal: true

# Pure string/data extraction used by jekyll_heading_id_dump.rb. No Jekyll
# dependency, so this is unit-testable without booting a Jekyll site.
module HeadingIdExtractor
  ID_ATTR_RE = /\sid=["']([^"']+)["']/.freeze
  HEADING_ID_RE = /<h[1-6][^>]*\sid=["']([^"']+)["']/.freeze

  # Every element id present anywhere in a fully-rendered page (Liquid +
  # kramdown + layouts already applied). Used to validate that an anchor
  # link resolves to something real on the target page — not restricted to
  # headings, since kramdown IALs can attach an id to non-heading blocks too.
  # Known narrow false-negative: this also picks up ids from shared layout
  # chrome (nav, sidebar, etc.), so a broken anchor that happens to collide
  # with a sitewide element id (e.g. a search box id present on every page)
  # would be incorrectly treated as resolved. Accepted for now; revisit if
  # it causes a real false negative in practice.
  def self.all_ids(html)
    html.to_s.scan(ID_ATTR_RE).flatten.uniq
  end

  # Ordered list of <h1>-<h6> element ids, in document order. Used to detect
  # links whose anchor points at a page's first heading (see the
  # first-heading warning in validate_doc_redirects.rb) — that anchor
  # behaves identically to no anchor at all when a browser navigates there.
  def self.heading_ids(html)
    html.to_s.scan(HEADING_ID_RE).flatten
  end

  # `local_redirect:` frontmatter is a client-side JS redirect with no real
  # DOM id (see hash_redirect.js / _layouts/default.html). It parses as one
  # of two shapes depending on how the author wrote it in YAML:
  #   - a Hash, e.g. _docs/_api/endpoints/messaging.md
  #   - an Array of single-key Hashes, e.g.
  #     _docs/_user_guide/channels/in_app_messages/customize.md
  # Both are treated as valid anchors regardless of whether a matching
  # heading exists in the rendered HTML.
  def self.local_redirect_keys(value)
    case value
    when Hash
      value.keys.map(&:to_s)
    when Array
      value.flat_map { |item| item.is_a?(Hash) ? item.keys.map(&:to_s) : [] }
    else
      []
    end
  end
end
