#!/usr/bin/env ruby
# frozen_string_literal: true

# Audits redirect *destinations* (RHS) in assets/js/broken_redirect_list.js against the
# Jekyll URL map. Redirect *sources* (LHS) are often legacy URLs that are intentionally
# not published; this script does not flag missing LHS pages.
#
# Skips: empty RHS, identity mappings (FROM and TO equal after normalization).
#
# Usage:
#   bundle exec ruby scripts/jekyll_url_map_dump.rb /tmp/jekyll-url-map-head.json
#   bundle exec ruby scripts/audit_validurls_targets_vs_jekyll.rb /tmp/jekyll-url-map-head.json
#
# Options:
#   --warn-only                  Exit 0 even when stale targets exist (still writes CSVs).
#   --out-dir PATH               Output directory (default: scripts/temp)
#   --min-prefix-segments N      For the "known" bucket, require stale and suggested paths to share
#                                N leading path segments (query/fragment stripped; default: 4).
#                                Use 0 to disable (every unique basename match stays "known").
#
# Outputs:
#   validurls-stale-targets-known-suggestions.csv  — unique basename + prefix rule (or basename only if N=0)
#   validurls-stale-targets-unsure.csv           — no match, ambiguous basename, or insufficient prefix

require "csv"
require "fileutils"
require_relative "redirect_target_verify_helpers"

warn_only = false
out_dir = "scripts/temp"
min_prefix_segments = 4
positional = []

i = 0
while i < ARGV.length
  case ARGV[i]
  when "--warn-only"
    warn_only = true
    i += 1
  when "--out-dir"
    out_dir = ARGV[i + 1] || abort("usage: bundle exec ruby scripts/audit_validurls_targets_vs_jekyll.rb [MAP.json] [--out-dir PATH] [--warn-only] [--min-prefix-segments N]")
    i += 2
  when "--min-prefix-segments"
    min_prefix_segments = Integer(ARGV[i + 1] || abort("usage: ... --min-prefix-segments N (use 0 to disable)"))
    i += 2
  when /^--/
    abort "Unknown option #{ARGV[i]}"
  else
    positional << ARGV[i]
    i += 1
  end
end

map_path = positional.first || "/tmp/jekyll-url-map-head.json"

unless File.file?(map_path)
  warn "Missing #{map_path} — run: bundle exec ruby scripts/jekyll_url_map_dump.rb #{map_path}"
  exit 2
end

redirect_file = File.join(__dir__, "..", "assets", "js", "broken_redirect_list.js")
published = RedirectTargetVerify.load_published_urls(map_path)

basename_index = Hash.new { |h, k| h[k] = [] }
published.each do |u|
  seg = RedirectTargetVerify.path_last_segment(u)
  next if seg.nil? || seg.empty?

  basename_index[seg] << u
end
basename_index.each_value(&:uniq!)

# norm_to => { raw_to:, example_from: }
stale = {}
File.foreach(redirect_file, chomp: true) do |line|
  next if line.strip.start_with?("//")
  p = RedirectTargetVerify.parse_validurls_line(line)
  next unless p

  from, to = p[:lhs], p[:rhs]
  next if to.strip.empty?
  next if RedirectTargetVerify.normalize_url_for_compare(from) == RedirectTargetVerify.normalize_url_for_compare(to)
  next if RedirectTargetVerify.published_include?(published, to)

  n = RedirectTargetVerify.normalize_url_for_compare(to)
  stale[n] ||= { raw_to: to, example_from: from }
end

known_rows = []
unsure_rows = []

stale.keys.sort.each do |norm_to|
  info = stale[norm_to]
  raw_to = info[:raw_to]
  example_from = info[:example_from]

  seg = RedirectTargetVerify.path_last_segment(norm_to)
  if seg.nil? || seg.empty?
    unsure_rows << [raw_to, example_from, "no_last_path_segment"]
    next
  end

  cands = basename_index[seg] || []
  case cands.size
  when 0
    unsure_rows << [raw_to, example_from, "no_match"]
  when 1
    suggested = cands.first
    if min_prefix_segments <= 0
      known_rows << [raw_to, suggested, "unique_basename", example_from]
    else
      stale_segs = RedirectTargetVerify.path_segments_for_prefix_compare(norm_to)
      sugg_segs = RedirectTargetVerify.path_segments_for_prefix_compare(suggested)
      shared = RedirectTargetVerify.common_prefix_segment_count(stale_segs, sugg_segs)
      if shared >= min_prefix_segments
        known_rows << [raw_to, suggested, "unique_basename_prefix_#{shared}", example_from]
      else
        unsure_rows << [raw_to, example_from, "unique_basename_insufficient_prefix_shared_#{shared}_need_#{min_prefix_segments}"]
      end
    end
  else
    unsure_rows << [raw_to, example_from, "ambiguous_#{cands.size}_candidates_last_segment=#{seg}"]
  end
end

FileUtils.mkdir_p(out_dir)
known_path = File.join(out_dir, "validurls-stale-targets-known-suggestions.csv")
unsure_path = File.join(out_dir, "validurls-stale-targets-unsure.csv")

CSV.open(known_path, "w") do |csv|
  csv << %w[stale_target suggested_jekyll_url reason example_from]
  known_rows.each { |r| csv << r }
end

CSV.open(unsure_path, "w") do |csv|
  csv << %w[stale_target example_from notes]
  unsure_rows.each { |r| csv << r }
end

considered = 0
good_lines = 0
File.foreach(redirect_file, chomp: true) do |line|
  next if line.strip.start_with?("//")
  p = RedirectTargetVerify.parse_validurls_line(line)
  next unless p

  from, to = p[:lhs], p[:rhs]
  next if to.strip.empty?
  next if RedirectTargetVerify.normalize_url_for_compare(from) == RedirectTargetVerify.normalize_url_for_compare(to)

  considered += 1
  good_lines += 1 if RedirectTargetVerify.published_include?(published, to)
end

puts "validurls RHS audit (Jekyll map: #{map_path})"
puts "  Mapping lines (non-empty RHS, non-identity): #{considered}"
puts "  Those lines with RHS in Jekyll map: #{good_lines}"
puts "  Unique stale RHS (not in published map): #{stale.size}"
prefix_note = min_prefix_segments <= 0 ? "disabled (--min-prefix-segments 0)" : min_prefix_segments.to_s
puts "  Min leading path segments for \"known\" bucket: #{prefix_note}"
puts "  Known suggestions: #{known_rows.size}"
puts "  Unsure: #{unsure_rows.size}"
puts "  Wrote #{known_path}"
puts "  Wrote #{unsure_path}"
puts "  Note: Review suggested URLs before editing broken_redirect_list.js; prefix + basename can still be wrong for edge cases."

exit(((known_rows.empty? && unsure_rows.empty?) || warn_only) ? 0 : 1)
