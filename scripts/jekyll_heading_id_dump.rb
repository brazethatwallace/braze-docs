#!/usr/bin/env ruby
# frozen_string_literal: true

# Dumps a JSON object: "_docs-relative-path" => {
#   "all_ids" => [...],            every element id on the rendered page
#   "heading_ids" => [...],        ordered <h1>-<h6> ids only
#   "local_redirect_keys" => [...] anchors valid via client-side JS redirect
#   "title" => "..."               human-readable article name, for reporting
# }
#
# Used by validate_doc_redirects.rb. Run from repo root with:
#   bundle exec ruby scripts/jekyll_heading_id_dump.rb OUT.json [SOURCE_DIR]
#
# Unlike jekyll_url_map_dump.rb (which only calls site.read + site.generate),
# this script calls site.render so Liquid tags and layouts actually execute.
# That is required for two known ID sources that only exist after rendering:
#   - the glossary_page layout, which generates ids from YAML `glossaries:`
#     frontmatter (_layouts/glossary_page.html), not from markdown headings
#   - the sdktabs plugin, which prefixes heading ids inside {% sdktab %}
#     blocks (e.g. "swift_...") (_plugins/sdktabs.rb)
# site.render does not call site.write, so no per-file HTML is written to
# disk for the whole site (Jekyll::Site#render measured at ~37s for the
# ~1,828 docs in this repo as of July 2026 -- see the plan's "Before you
# start" section for how that was measured).

require "jekyll"
require "json"
require "tmpdir"
require_relative "heading_id_extractor"

module JekyllHeadingIdDump
  # Human-readable label for a page, used by validate_doc_redirects.rb to build
  # PR-comment text that names articles instead of file paths. Prefers the
  # frontmatter fields authors already maintain for navigation/SEO (nav_title
  # is short and scannable; article_title is the descriptive H1) over the raw
  # file path, since a path like "_docs/_api/endpoints/apps/..." tells a
  # reader far less than "Update Push Credential".
  def self.readable_title(path, nav_title: nil, article_title: nil)
    [nav_title, article_title].each do |candidate|
      trimmed = candidate.to_s.strip
      return trimmed unless trimmed.empty?
    end

    File.basename(path, ".md").tr("_", " ").split.map(&:capitalize).join(" ")
  end

  def self.build(source_dir)
    Dir.mktmpdir("jekyll-heading-id-map") do |dest|
      site = Jekyll::Site.new(
        Jekyll.configuration(
          "source" => source_dir,
          "quiet" => true,
          "safe" => false,
          "destination" => dest
        )
      )

      site.read
      site.generate
      site.render

      map = {}
      site.collections.each_value do |coll|
        coll.docs.each do |doc|
          key = doc.path.delete_prefix("#{site.source}/")
          output = doc.output.to_s

          map[key] = {
            "all_ids" => HeadingIdExtractor.all_ids(output),
            "heading_ids" => HeadingIdExtractor.heading_ids(output),
            "local_redirect_keys" => HeadingIdExtractor.local_redirect_keys(doc.data["local_redirect"]),
            "title" => readable_title(key, nav_title: doc.data["nav_title"], article_title: doc.data["article_title"])
          }
        end
      end

      # Root _includes/*.md files aren't Jekyll documents (they're pulled into
      # _docs/ pages via {% multi_lang_include %}), so they have no doc.output
      # from site.render above. They still need heading-id entries so a
      # same-page anchor link written *inside* an include (target_path ==
      # source_file) can resolve. Convert each include's raw markdown
      # directly through the site's markdown converter (kramdown) rather
      # than the full per-document Liquid+layout pipeline -- this correctly
      # produces standard kramdown auto-ids and explicit {#id} overrides,
      # but will NOT resolve nested {% multi_lang_include %} or {% sdktabs %}
      # content that only exists once the include is pulled into a real
      # page. Accepted limitation: same-page anchors inside includes are
      # rare (none exist in this repo as of this check's introduction), and
      # cross-file links *into* an include's headings are already covered by
      # the full per-page render above, since the include's content is
      # inlined into whatever _docs/ page pulls it in.
      converter = site.find_converter_instance(Jekyll::Converters::Markdown)
      Dir.glob(File.join(source_dir, "_includes", "**", "*.md")).each do |path|
        key = path.delete_prefix("#{source_dir}/")
        raw = File.read(path)
        # Strip a leading YAML frontmatter block, if present (uncommon for
        # includes, but some exist -- e.g. currents_changelogs_template.md).
        # Reuses Jekyll's own canonical front-matter regex
        # (Jekyll::Document::YAML_FRONT_MATTER_REGEXP) rather than a custom
        # one, so this behaves identically to how Jekyll itself would parse
        # the same file if it were ever promoted to a real document --
        # including tolerating CRLF line endings and correctly leaving a
        # file with no closing "---"/"..." delimiter untouched. The one
        # inherent ambiguity (two unrelated "---" lines with ordinary prose
        # between them, misread as frontmatter) is shared with Jekyll's own
        # parsing everywhere else in the site, not a risk unique to this
        # script.
        body = raw.sub(Jekyll::Document::YAML_FRONT_MATTER_REGEXP, "")
        output = converter.convert(body)

        map[key] = {
          "all_ids" => HeadingIdExtractor.all_ids(output),
          "heading_ids" => HeadingIdExtractor.heading_ids(output),
          "local_redirect_keys" => [],
          "title" => readable_title(key)
        }
      end

      map
    end
  end
end

if $PROGRAM_NAME == __FILE__
  out_path = ARGV[0] or abort "usage: jekyll_heading_id_dump.rb OUT.json [SOURCE_DIR]"
  source_dir = ARGV[1] || "."
  File.write(out_path, JSON.generate(JekyllHeadingIdDump.build(source_dir)))
end
