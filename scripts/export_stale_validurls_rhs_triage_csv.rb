#!/usr/bin/env ruby
# frozen_string_literal: true

# Writes one CSV row per *unique* stale validurls RHS (not in Jekyll map), with triage context.
#
# Usage:
#   bundle exec ruby scripts/export_stale_validurls_rhs_triage_csv.rb MAP.json OUT.csv
#   bundle exec ruby scripts/export_stale_validurls_rhs_triage_csv.rb MAP.json OUT.csv --min-prefix-segments 4
#
# Columns: stale_target_raw, normalized_rhs, example_lhs, lhs_count, has_query, has_fragment,
#          suggested_jekyll_url, triage_notes

require "csv"
require "fileutils"
require_relative "redirect_target_verify_helpers"

args = ARGV.dup
min_prefix_segments = 4
positional = []
while args.any?
  a = args.shift
  case a
  when "--min-prefix-segments"
    min_prefix_segments = Integer(args.shift || abort("usage: --min-prefix-segments N"))
  else
    positional << a
  end
end

map_path = positional[0] || abort("usage: export_stale_validurls_rhs_triage_csv.rb MAP.json OUT.csv [--min-prefix-segments N]")
out_path = positional[1] || abort("usage: export_stale_validurls_rhs_triage_csv.rb MAP.json OUT.csv [--min-prefix-segments N]")

abort "Missing #{map_path}" unless File.file?(map_path)

redirect_file = File.join(__dir__, "..", "assets", "js", "broken_redirect_list.js")
abort "Missing #{redirect_file}" unless File.file?(redirect_file)

published = RedirectTargetVerify.load_published_urls(map_path)

basename_index = Hash.new { |h, k| h[k] = [] }
published.each do |u|
  seg = RedirectTargetVerify.path_last_segment(u)
  next if seg.nil? || seg.empty?

  basename_index[seg] << u
end
basename_index.each_value(&:uniq!)

# norm_to => { raw_to:, example_from:, lhs_list: [] }
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
  entry = (stale[n] ||= { raw_to: to, example_from: from, lhs_list: [] })
  entry[:lhs_list] << from
end

def triage_row(norm_to, info, basename_index, min_prefix_segments)
  raw_to = info[:raw_to]
  example_from = info[:example_from]
  lhs_count = info[:lhs_list].size
  base_part = raw_to.split("#", 2).first
  has_query = base_part.include?("?")
  has_fragment = raw_to.include?("#")

  seg = RedirectTargetVerify.path_last_segment(norm_to)
  suggested = ""
  notes = ""

  if seg.nil? || seg.empty?
    notes = "no_last_path_segment"
  else
    cands = basename_index[seg] || []
    case cands.size
    when 0
      notes = "no_basename_match_in_jekyll_map"
    when 1
      sug = cands.first
      stale_segs = RedirectTargetVerify.path_segments_for_prefix_compare(norm_to)
      sugg_segs = RedirectTargetVerify.path_segments_for_prefix_compare(sug)
      shared = RedirectTargetVerify.common_prefix_segment_count(stale_segs, sugg_segs)
      if min_prefix_segments <= 0 || shared >= min_prefix_segments
        suggested = sug
        notes = "unique_basename_prefix_segments_shared_#{shared}"
      else
        notes = "unique_basename_insufficient_prefix_shared_#{shared}_need_#{min_prefix_segments}"
      end
    else
      notes = "ambiguous_#{cands.size}_candidates_last_segment_#{seg}"
    end
  end

  external = raw_to.match?(/\Ahttps?:\/\//i)
  notes = "#{notes};external_url" if external

  [raw_to, norm_to, example_from, lhs_count, has_query ? "yes" : "no", has_fragment ? "yes" : "no", suggested, notes]
end

rows = stale.keys.sort.map { |n| triage_row(n, stale[n], basename_index, min_prefix_segments) }

FileUtils.mkdir_p(File.dirname(File.expand_path(out_path))) if File.dirname(out_path) != "."

CSV.open(File.expand_path(out_path), "w") do |csv|
  csv << %w[stale_target_raw normalized_rhs example_lhs lhs_count has_query_string has_fragment suggested_jekyll_url triage_notes]
  rows.each { |r| csv << r }
end

puts "Wrote #{File.expand_path(out_path)} (#{rows.size} unique stale RHS)"
