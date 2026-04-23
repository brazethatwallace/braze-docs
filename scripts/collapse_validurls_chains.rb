#!/usr/bin/env ruby
# frozen_string_literal: true

# Collapse internal redirect chains in assets/js/broken_redirect_list.js: if RHS (normalized)
# equals some other row's LHS (normalized), replace with the transitive target until fixed point.
# Run after apply_validurl_rhs_from_csv so intermediates already point at Jekyll URLs where possible.
#
# Usage:
#   bundle exec ruby scripts/collapse_validurls_chains.rb --jekyll-map PATH.json [--dry-run | --apply] [--max-hops N] [--redirect-file PATH]
#
# Required:
#   --jekyll-map PATH.json  Load published URLs; only apply a collapse when the final RHS passes published_include?
#                           (matches Jekyll map semantics). Rows that would end on a non-published URL are skipped.
#
# Optional:
#   --warn-unpublished      With --jekyll-map, only warn instead of skipping (default is skip when map given).
#   --export-skipped PATH   Write skipped rows to CSV (lhs, immediate_rhs, collapsed_final, category, suggested_jekyll_url).

require "csv"
require "fileutils"
require_relative "redirect_file_io"
require_relative "redirect_target_verify_helpers"
DEFAULT_MAX_HOPS = 32

dry_run = true
max_hops = DEFAULT_MAX_HOPS
redirect_file = File.join(__dir__, "..", "assets", "js", "broken_redirect_list.js")
jekyll_map_path = nil
skip_unpublished = true
export_skipped_path = nil

args = ARGV.dup
while args.any?
  a = args.shift
  case a
  when "--dry-run"
    dry_run = true
  when "--apply"
    dry_run = false
  when "--max-hops"
    max_hops = Integer(args.shift || abort("usage: --max-hops N"))
  when "--redirect-file"
    redirect_file = args.shift
  when "--jekyll-map"
    jekyll_map_path = args.shift
  when "--warn-unpublished"
    skip_unpublished = false
  when "--export-skipped"
    export_skipped_path = args.shift
  else
    abort "Unknown option #{a}\nusage: collapse_validurls_chains.rb [--dry-run|--apply] [--max-hops N] [--redirect-file PATH] [--jekyll-map PATH.json] [--warn-unpublished] [--export-skipped PATH.csv]"
  end
end

def skipped_collapse_category(collapsed_final)
  f = collapsed_final.to_s
  return "external" if f.match?(/\Ahttps?:\/\//i)

  path_only = f.split("#", 2).first.split("?", 2).first
  bare = path_only.to_s.sub(%r{/+\z}, "")
  return "root_docs" if bare == "/docs"

  return "query_tab" if f.include?("?tab=") || f.include?("?sdktab=")

  segs = path_only.to_s.chomp("/").split("/").reject(&:empty?)
  # /docs/partners/<one_segment> — short alias, often not in map
  return "partner_short" if segs.size == 3 && segs[0] == "docs" && segs[1] == "partners"

  "other"
end

abort "Missing #{redirect_file}" unless File.file?(redirect_file)
abort "Pass --jekyll-map when collapsing so finals are constrained to the Jekyll URL map." unless jekyll_map_path

lines = File.readlines(redirect_file, chomp: true)
# norm(lhs) -> rhs (last occurrence in file wins, matching JS object semantics)
norm_lhs_to_rhs = {}
line_matches = []
lines.each_with_index do |line, idx|
  next if line.strip.start_with?("//")

  p = RedirectTargetVerify.parse_validurls_line(line)
  next unless p

  lhs, rhs = p[:lhs], p[:rhs]
  nk = RedirectTargetVerify.normalize_url_for_compare(lhs)
  norm_lhs_to_rhs[nk] = rhs
  line_matches << { idx: idx, indent: p[:indent], lhs: lhs, rhs: rhs }
end

def resolve_rhs(start_rhs, norm_lhs_to_rhs, max_hops)
  current = start_rhs
  hops = 0
  visited = {}
  while hops < max_hops
    nk = RedirectTargetVerify.normalize_url_for_compare(current)
    break if visited[nk]
    visited[nk] = true

    nxt = norm_lhs_to_rhs[nk]
    break if nxt.nil? || nxt.empty?

    current = nxt
    hops += 1
  end
  current
end

published = RedirectTargetVerify.load_published_urls(jekyll_map_path)

changes = []
skipped_unpublished = []

line_matches.each do |row|
  final = resolve_rhs(row[:rhs], norm_lhs_to_rhs, max_hops)
  next if final == row[:rhs]
  next if RedirectTargetVerify.normalize_url_for_compare(final) == RedirectTargetVerify.normalize_url_for_compare(row[:rhs])

  unless RedirectTargetVerify.published_include?(published, final)
    skipped_unpublished << { lhs: row[:lhs], from: row[:rhs], to: final }
    next if skip_unpublished
  end

  new_line = "#{row[:indent]}validurls['#{RedirectTargetVerify.escape_js_single_quoted(row[:lhs])}'] = '#{RedirectTargetVerify.escape_js_single_quoted(final)}';"
  changes << { idx: row[:idx], old_line: lines[row[:idx]], new_line: new_line, from: row[:rhs], to: final }
end

mode = dry_run ? "DRY-RUN" : "APPLY"
puts "#{mode}: #{changes.size} validurls line(s) to collapse (max_hops=#{max_hops})"
changes.first(25).each do |c|
  puts "  #{c[:from][0, 100]}#{c[:from].size > 100 ? '...' : ''}"
  puts "    => #{c[:to][0, 100]}#{c[:to].size > 100 ? '...' : ''}"
end
puts "  ... (#{changes.size - 25} more)" if changes.size > 25

unless skipped_unpublished.empty?
  puts "Skipped #{skipped_unpublished.size} collapse(s) whose final RHS is not in Jekyll map (use --warn-unpublished to apply anyway):"
  skipped_unpublished.first(12).each do |s|
    puts "  LHS #{s[:lhs][0, 70]}... -> #{s[:to][0, 80]}..."
  end
  puts "  ... (#{skipped_unpublished.size - 12} more)" if skipped_unpublished.size > 12
end

if export_skipped_path
  repo_root = File.expand_path("..", __dir__)
  out = export_skipped_path.start_with?("/") ? export_skipped_path : File.expand_path(export_skipped_path, repo_root)
  FileUtils.mkdir_p(File.dirname(out))
  CSV.open(out, "w", write_headers: true, headers: %w[lhs immediate_rhs collapsed_final category suggested_jekyll_url]) do |csv|
    skipped_unpublished.each do |s|
      csv << [s[:lhs], s[:from], s[:to], skipped_collapse_category(s[:to]), ""]
    end
  end
  puts "Wrote #{out} (#{skipped_unpublished.size} row(s))"
end

if dry_run
  puts "Run with --apply to write #{redirect_file}"
  exit 0
end

changes.each { |c| lines[c[:idx]] = c[:new_line] }
RedirectFileIO.atomic_write!(redirect_file, "#{lines.join("\n")}\n")
puts "Wrote #{redirect_file}"
exit 0
