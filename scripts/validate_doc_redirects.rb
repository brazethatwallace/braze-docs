#!/usr/bin/env ruby
# frozen_string_literal: true

# Compares Jekyll-computed doc URLs between a base ref (default: origin/develop) and HEAD,
# then checks assets/js/broken_redirect_list.js for matching old -> new mappings.
#
# With --json PATH, the report includes "required_mappings" (from → to) for every URL the
# diff requires; use scripts/verify_redirect_targets_in_jekyll.rb to confirm destinations exist
# in a Jekyll URL map (see jekyll_url_map_dump.rb).
#
# Usage (from repo root):
#   bundle exec ruby scripts/validate_doc_redirects.rb
#   bundle exec ruby scripts/validate_doc_redirects.rb --base origin/develop
#   bundle exec ruby scripts/validate_doc_redirects.rb --skip-fetch
#
# Requires: git, bundler, gems from Gemfile (Jekyll). Uses a temporary git worktree for the base ref.

require "fileutils"
require "json"
require "open3"
require "optparse"
require "set"
require "tempfile"
require "tmpdir"
require_relative "doc_anchor_links"

REPO_ROOT = begin
  out, err, st = Open3.capture3("git", "rev-parse", "--show-toplevel")
  raise "Failed to determine repository root. Is this a git checkout?\n#{err}" unless st.success?

  out.strip
end
DOC_MAPS_SCRIPT = File.expand_path("jekyll_doc_maps_dump.rb", __dir__)
REDIRECT_REL = "assets/js/broken_redirect_list.js"
RX_VALIDURL = /validurls\['([^']+)'\]\s*=\s*'([^']*)'(?:;)?/

def run!(argv)
  options = { base: "origin/develop", fetch: true, json_out: nil }
  OptionParser.new do |o|
    o.banner = "usage: validate_doc_redirects.rb [options]"
    o.on("--base REF", "Git ref to compare against (default: origin/develop)") { |v| options[:base] = v }
    o.on("--skip-fetch", "Do not run git fetch for the base ref") { options[:fetch] = false }
    o.on("--json PATH", "Write machine-readable report to PATH") { |v| options[:json_out] = v }
    o.on("-h", "--help", "Show help") do
      puts o
      exit 0
    end
  end.parse!(argv)

  Dir.chdir(REPO_ROOT) do
    validate!(options)
  end
end

def sh_capture(*cmd)
  out, err, st = Open3.capture3(*cmd)
  raise "command failed: #{cmd.join(' ')}\n#{err}#{out}" unless st.success?

  out
end

def sh!(*cmd)
  system(*cmd, exception: true)
end

def normalize_url_for_compare(url)
  # Use a negative lookbehind so the repeated-slash collapse does not destroy
  # the "//" in an absolute URL scheme (e.g. "https://…" stays "https://…").
  # Lowercasing is intentionally omitted: case-only URL changes are real and
  # should be caught as mismatches rather than silently normalised away.
  u = url.to_s.strip.gsub(%r{(?<!:)//+}, "/")
  # Ruby: "".split("#", 2) => [] — always use indexed parts
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
  file_segment = File.basename(path)
  has_extension = !file_segment.empty? && file_segment.match?(/\.[A-Za-z0-9]{2,}$/)
  path += "/" unless path.empty? || has_extension
  "#{path}#{q}#{frag}"
end

def parse_redirect_file(path)
  map = {}
  File.foreach(path, chomp: true) do |line|
    next if line.strip.start_with?("//")
    next unless line.include?("validurls[")

    m = RX_VALIDURL.match(line)
    next unless m

    from = normalize_url_for_compare(m[1])
    to_raw = m[2].to_s.strip
    next if to_raw.empty?

    to = normalize_url_for_compare(to_raw)
    map[from] = to
  end
  map
end

# One Jekyll boot per site root: URL map + heading-id map together.
# Returns [url_map, heading_map].
def jekyll_doc_maps(site_root)
  tmp = Tempfile.new(["jekyll-doc-maps", ".json"])
  tmp.close
  Dir.chdir(site_root) do
    sh!("bundle", "exec", "ruby", DOC_MAPS_SCRIPT, tmp.path)
  end
  data = JSON.parse(File.read(tmp.path))
  [data.fetch("urls"), data.fetch("headings")]
ensure
  tmp&.unlink
end

# Every markdown file this check scans for anchor-bearing links: all of
# _docs/ and root _includes/. (find_broken_links.ts excludes a "_docs/
# _contributing/" directory for example/tooling docs with intentionally
# non-resolving links, but that directory does not exist in this repo --
# the real contributing docs live at docs/contributing/ and
# _includes/contributing/, outside the _docs/ collection entirely -- so no
# equivalent exclusion is needed here. If a future _docs/_contributing/-
# style directory is added with deliberately-broken example links, add an
# exclusion here matching its real path at that time.)
def anchor_scan_files(root)
  docs = Dir.glob(File.join(root, "_docs", "**", "*.md"))
  includes = Dir.glob(File.join(root, "_includes", "**", "*.md"))
  (docs + includes).map { |p| p.delete_prefix("#{root}/") }
end

def build_anchor_link_index(root)
  anchor_scan_files(root).flat_map do |rel_path|
    content = File.read(File.join(root, rel_path))
    DocAnchorLinks.extract(rel_path, content)
  end
end

def anchor_resolves?(heading_map, link)
  entry = heading_map[link.target_path]
  return false if entry.nil?

  (entry["all_ids"] || []).include?(link.anchor) ||
    (entry["local_redirect_keys"] || []).include?(link.anchor)
end

def anchor_link_key(link)
  [link.source_file, link.target_path, link.anchor]
end

# Human-readable article name for a report entry (falls back to the raw path
# if HEAD's heading map has no entry, e.g. a since-deleted source file).
def doc_title(heading_map, path)
  heading_map.dig(path, "title") || path
end

# Returns newly_broken: links whose anchor does not resolve on HEAD and were
# not already broken on base (mirrors required_redirects' "only fail on new
# breakage" rule). Each entry is tagged with a :category so the report can
# tell an author what kind of fix is needed:
#   :heading_renamed        -- this exact link resolved fine on base; some
#                               heading it points at changed or disappeared
#   :new_link_wrong_anchor  -- this link (by source file + target path +
#                               anchor) did not exist on base at all; likely
#                               a typo or wrong target in newly-added content
#
# Known limitations of the (source_file, target_path, anchor) identity key:
# - If the *source* file itself was renamed in this PR (already tracked
#   separately via git rename detection in required_redirects), the same
#   link reports under a different key and gets labeled
#   :new_link_wrong_anchor even though it's really a renamed-heading case.
#   Cosmetic only -- it doesn't change whether the check passes or fails,
#   just which fix-suggestion message an author sees.
# - Two distinct links in the same source file that happen to resolve to the
#   same (target_path, anchor) are indistinguishable by this key. If one was
#   already broken on base, a newly-added second link to that same already-
#   broken destination is classified as pre-existing debt rather than new
#   breakage. Accepted: both links point at the literal same nonexistent
#   destination, so a single heading fix resolves both.
def required_anchor_fixes(heading_map_base, heading_map_head, links_base, links_head)
  base_keys = links_base.map { |l| anchor_link_key(l) }.to_set
  broken_before_keys = links_base.reject { |l| anchor_resolves?(heading_map_base, l) }
                                  .map { |l| anchor_link_key(l) }.to_set

  newly_broken = []
  links_head.each do |l|
    next if anchor_resolves?(heading_map_head, l)

    key = anchor_link_key(l)
    next if broken_before_keys.include?(key)

    category = base_keys.include?(key) ? :heading_renamed : :new_link_wrong_anchor
    newly_broken << { link: l, category: category }
  end

  newly_broken
end

def first_heading_link?(heading_map_head, link)
  return false unless anchor_resolves?(heading_map_head, link)

  entry = heading_map_head[link.target_path]
  entry && !entry["heading_ids"].to_a.empty? && entry["heading_ids"].first == link.anchor
end

# Every path this PR added, modified, or renamed-to, under _docs/ or root
# _includes/ (the same scan domain as anchor_scan_files). Used to scope the
# first-heading warning to links living in files this PR actually touched --
# scanning every resolving link sitewide produced hundreds of warnings on
# pre-existing, unrelated content and wasn't useful signal for a reviewer.
def changed_or_added_files(diff_rows)
  diff_rows.each_with_object(Set.new) do |row, set|
    case row[0]
    when :rename
      set << row[2] # only the new path can appear as a link source in HEAD
    when :a, :m, :t
      set << row[1]
    end
  end
end

# links that DO resolve on HEAD, live in a file this PR touched, and whose
# anchor matches the target page's first heading id. Non-blocking -- this is
# advisory since a link to a page's first heading behaves identically to
# linking the page directly, and a reviewer would reasonably want to
# double-check whether that was intentional -- but only for content this PR
# is actually responsible for, not the whole site's pre-existing links.
#
# Same-page anchors are exempt: on the page that owns the heading, the anchor
# scrolls the reader to that section, so it is not equivalent to a bare link
# and the suggested fix (drop the anchor) would leave an empty href. The
# writing style guide endorses this pattern ("On this page, see [heading]").
def first_heading_warnings_for(heading_map_head, links_head, changed_files)
  links_head.select do |l|
    next false if l.target_path == l.source_file

    changed_files.include?(l.source_file) && first_heading_link?(heading_map_head, l)
  end
end

def git_diff_name_status(base_ref, paths: ["_docs/"])
  range = "#{base_ref}...HEAD"
  out = sh_capture("git", "diff", "--name-status", "-M20%", range, "--", *paths)
  rows = []
  out.each_line do |line|
    line = line.chomp
    next if line.empty?

    parts = line.split("\t", -1)
    status = parts[0]
    case status
    when /^R\d*/
      rows << [:rename, parts[1], parts[2]]
    when "M", "A", "D", "T"
      rows << [status.downcase.to_sym, parts[1]]
    else
      rows << [:unknown, line]
    end
  end
  rows
end

def required_redirects(url_map_base, url_map_head, diff_rows)
  needed = {} # old_url_norm => new_url_norm
  md_paths = lambda { |p| p.end_with?(".md") }

  renames = diff_rows.select { |r| r[0] == :rename }
  deleted = diff_rows.select { |r| r[0] == :d }.map { |r| r[1] }.select(&md_paths)
  added = diff_rows.select { |r| r[0] == :a }.map { |r| r[1] }.select(&md_paths)
  modified = diff_rows.select { |r| r[0] == :m }.map { |r| r[1] }.select(&md_paths)

  renamed_sources = renames.map { |(_, old_p, _)| old_p }.to_set

  # Process renames: use git's rename detection to pair old→new paths.
  renames.each do |(_, old_p, new_p)|
    next unless md_paths.call(old_p) && md_paths.call(new_p)

    old_u = url_map_base[old_p]
    new_u = url_map_head[new_p]
    next if old_u.nil? || new_u.nil?
    next if normalize_url_for_compare(old_u) == normalize_url_for_compare(new_u)

    needed[normalize_url_for_compare(old_u)] = normalize_url_for_compare(new_u)
  end

  # Detect URL changes for all paths shared between base and HEAD. Comparing
  # URL maps directly (rather than relying solely on the _docs/ git diff) catches
  # permalink re-URLs driven by _config.yml or _plugins/ changes, where doc files
  # themselves are not modified.
  head_keys = url_map_head.keys.to_set
  url_map_base.each_key do |p|
    next unless md_paths.call(p)
    next unless head_keys.include?(p)
    next if renamed_sources.include?(p)

    old_u = normalize_url_for_compare(url_map_base[p])
    new_u = normalize_url_for_compare(url_map_head[p])
    next if old_u == new_u

    needed[old_u] = new_u
  end

  # Deleted pages: paths present in the base URL map but absent from HEAD's map
  # (and not the source of a rename) need a manual redirect to a replacement URL.
  url_map_base.each_key do |p|
    next unless md_paths.call(p)
    next if head_keys.include?(p)
    next if renamed_sources.include?(p)

    old_u = url_map_base[p]
    next if old_u.nil?

    needed[normalize_url_for_compare(old_u)] = :deleted_no_target
  end

  [needed, { renames: renames.size, modified: modified.size, deleted: deleted.size, added: added.size }]
end

def validate!(options)
  base_ref = options[:base]

  if options[:fetch] && base_ref.match?(/\Aorigin\/[\w\-\.\/]+\z/)
    sh!("git", "fetch", "--quiet", "origin", base_ref.delete_prefix("origin/"))
  end

  resolve_ref = sh_capture("git", "rev-parse", "--verify", base_ref).strip

  tmp_parent = Dir.mktmpdir("braze-redirect-validate")
  worktree = File.join(tmp_parent, "base-tree")
  begin
    sh!("git", "-C", REPO_ROOT, "worktree", "add", "--detach", worktree, resolve_ref)

    puts "Building URL + heading-id maps for #{base_ref} (#{resolve_ref[0..12]})…"
    map_base, heading_map_base = jekyll_doc_maps(worktree)
    puts "Building URL + heading-id maps for HEAD…"
    map_head, heading_map_head = jekyll_doc_maps(REPO_ROOT)

    links_base = build_anchor_link_index(worktree)
    links_head = build_anchor_link_index(REPO_ROOT)
  ensure
    success = system("git", "-C", REPO_ROOT, "worktree", "remove", "-f", worktree, out: File::NULL, err: File::NULL)
    FileUtils.remove_entry(tmp_parent, true)
    unless success
      system("git", "-C", REPO_ROOT, "worktree", "prune", out: File::NULL, err: File::NULL)
      raise "Failed to remove git worktree at #{worktree}"
    end
  end

  # Use resolve_ref (the exact SHA) so the diff is guaranteed to be based on
  # the same commit that was checked out for the base URL map, even if base_ref
  # is a mutable ref (branch or remote-tracking branch) that could advance.
  diff_rows = git_diff_name_status(resolve_ref)
  needed, stats = required_redirects(map_base, map_head, diff_rows)
  newly_broken_anchors = required_anchor_fixes(heading_map_base, heading_map_head, links_base, links_head)

  anchor_diff_rows = git_diff_name_status(resolve_ref, paths: ["_docs/", "_includes/"])
  changed_files = changed_or_added_files(anchor_diff_rows)
  heading_warnings = first_heading_warnings_for(heading_map_head, links_head, changed_files)

  redirect_path = File.join(REPO_ROOT, REDIRECT_REL)
  redirects = parse_redirect_file(redirect_path)

  missing = []
  wrong = []
  deleted_warn = []

  needed.each do |from_norm, to_norm|
    if to_norm == :deleted_no_target
      # Manual redirect in broken_redirect_list.js is sufficient when the doc file
      # is gone from HEAD (no Jekyll URL to diff against).
      if redirects[from_norm].nil?
        deleted_warn << { old_url: from_norm, note: "Page removed; add redirect manually to a replacement URL." }
      end
      next
    end

    actual_to = redirects[from_norm]
    if actual_to.nil?
      missing << { old_url: from_norm, expected_new: to_norm }
      next
    end

    next if actual_to == to_norm

    wrong << { old_url: from_norm, expected_new: to_norm, mapped_new: actual_to }
  end

  required_mappings = needed.filter_map do |from_norm, to_norm|
    if to_norm == :deleted_no_target
      dest = redirects[from_norm]
      next if dest.nil?

      { "from" => from_norm, "to" => dest }
    else
      { "from" => from_norm, "to" => to_norm }
    end
  end

  report = {
    base_ref: base_ref,
    base_sha: resolve_ref,
    diff_stats: stats,
    counts: {
      required_redirects: needed.count { |_, t| t != :deleted_no_target },
      missing: missing.size,
      wrong_target: wrong.size,
      deleted_pages: deleted_warn.size
    },
    missing: missing,
    wrong_target: wrong,
    deleted_pages: deleted_warn,
    required_mappings: required_mappings,
    anchor_issues: newly_broken_anchors.map { |row|
      link = row[:link]
      {
        "source_file" => link.source_file,
        "source_title" => doc_title(heading_map_head, link.source_file),
        "target_path" => link.target_path,
        "target_title" => doc_title(heading_map_head, link.target_path),
        "anchor" => link.anchor,
        "link" => link.raw_url,
        "category" => row[:category].to_s
      }
    },
    anchor_warnings: heading_warnings.map { |l|
      {
        "source_file" => l.source_file,
        "source_title" => doc_title(heading_map_head, l.source_file),
        "target_path" => l.target_path,
        "target_title" => doc_title(heading_map_head, l.target_path),
        "anchor" => l.anchor,
        "link" => l.raw_url
      }
    }
  }

  if options[:json_out]
    File.write(options[:json_out], JSON.pretty_generate(report))
    puts "Wrote #{options[:json_out]}"
  end

  puts ""
  puts "Doc redirect validation (Jekyll URL maps vs #{REDIRECT_REL})"
  puts "  Base: #{base_ref} @ #{resolve_ref[0..11]}"
  puts "  Git diff (#{base_ref}...HEAD under _docs/): #{stats[:renames]} renames, #{stats[:modified]} modified, #{stats[:deleted]} deleted, #{stats[:added]} added"
  puts "  Required old→new mappings (URL changed or page deleted): #{report[:counts][:required_redirects] + report[:counts][:deleted_pages]}"
  puts ""

  if deleted_warn.any?
    puts "Deleted pages (need a manual redirect target in #{REDIRECT_REL}):"
    deleted_warn.each { |row| puts "  - #{row[:old_url]}" }
    puts ""
  end

  if missing.any?
    puts "Missing redirects (add validurls['OLD'] = 'NEW';):"
    missing.each { |row| puts "  - #{row[:old_url]}  →  #{row[:expected_new]}" }
    puts ""
  end

  if wrong.any?
    puts "Wrong redirect target:"
    wrong.each do |row|
      puts "  - #{row[:old_url]}"
      puts "      expected: #{row[:expected_new]}"
      puts "      mapped:   #{row[:mapped_new]}"
    end
    puts ""
  end

  if newly_broken_anchors.any?
    renamed = newly_broken_anchors.select { |r| r[:category] == :heading_renamed }
    new_wrong = newly_broken_anchors.select { |r| r[:category] == :new_link_wrong_anchor }

    if renamed.any?
      puts "Broken anchors (heading was renamed or removed -- update the link's anchor):"
      renamed.each { |r| puts "  - #{r[:link].source_file}: #{r[:link].raw_url}" }
      puts ""
    end

    if new_wrong.any?
      puts "Broken anchors (new link points at a nonexistent anchor -- check for a typo or wrong target):"
      new_wrong.each { |r| puts "  - #{r[:link].source_file}: #{r[:link].raw_url}" }
      puts ""
    end
  end

  if heading_warnings.any?
    puts "Warning (non-blocking): links pointing at a target page's first heading behave"
    puts "identically to linking the page directly. Please confirm these are intentional:"
    heading_warnings.each { |l| puts "  - #{l.source_file}: #{l.raw_url}" }
    puts ""
  end

  if missing.empty? && wrong.empty? && deleted_warn.empty? && newly_broken_anchors.empty?
    puts "OK — all required redirects are present, targets match, and no new anchor drift found."
    exit 0
  end

  if missing.any? || wrong.any? || deleted_warn.any?
    puts "FAILED — fix #{REDIRECT_REL} before merging."
  else
    puts "FAILED — fix the broken anchor link(s) above before merging."
  end
  exit 1
end

run!(ARGV) if $PROGRAM_NAME == __FILE__
