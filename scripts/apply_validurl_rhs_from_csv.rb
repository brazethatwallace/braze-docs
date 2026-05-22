#!/usr/bin/env ruby
# frozen_string_literal: true

# Applies redirect *destination* (RHS) updates from an audit CSV to
# assets/js/broken_redirect_list.js. Only edits lines that match validurls[...] = '...';
# the RHS must match the CSV `stale_target` string exactly.
#
# Prerequisite: triage the CSV (remove bad suggestions) before --apply.
#
# Usage:
#   bundle exec ruby scripts/apply_validurl_rhs_from_csv.rb --csv PATH [--dry-run | --apply]
#
# Options:
#   --csv PATH                 Required. Columns: stale_target, suggested_jekyll_url (and optional others).
#   --dry-run                  Print planned changes (default).
#   --apply                    Write broken_redirect_list.js.
#   --redirect-file PATH       Default: assets/js/broken_redirect_list.js
#   --merge-fragments          If stale_target has #fragment and suggested does not, append that fragment
#                              to the new RHS (default: on).
#   --no-merge-fragments       Use suggested_jekyll_url verbatim.

require "csv"
require_relative "redirect_file_io"
require_relative "redirect_target_verify_helpers"

dry_run = true
merge_fragments = true
csv_path = nil
redirect_file = File.join(__dir__, "..", "assets", "js", "broken_redirect_list.js")

args = ARGV.dup
while args.any?
  a = args.shift
  case a
  when "--dry-run"
    dry_run = true
  when "--apply"
    dry_run = false
  when "--merge-fragments"
    merge_fragments = true
  when "--no-merge-fragments"
    merge_fragments = false
  when "--csv"
    csv_path = args.shift
  when "--redirect-file"
    redirect_file = args.shift
  else
    abort "Unknown option #{a}\nusage: bundle exec ruby scripts/apply_validurl_rhs_from_csv.rb --csv PATH [--dry-run|--apply] [--no-merge-fragments]"
  end
end

unless csv_path
  abort "Missing --csv PATH"
end

repo_root = File.expand_path("..", __dir__)
resolved = [File.expand_path(csv_path, Dir.pwd), File.expand_path(csv_path, repo_root)].uniq.find { |p| File.file?(p) }
abort "CSV not found: #{csv_path}" unless resolved

csv_path = resolved

unless File.file?(redirect_file)
  abort "Missing redirect file: #{redirect_file}"
end

pairs = {}
CSV.foreach(csv_path, headers: true) do |row|
  stale = row["stale_target"]&.strip
  sug = row["suggested_jekyll_url"]&.strip
  next if stale.nil? || sug.nil? || stale.empty? || sug.empty?

  pairs[stale] = sug
end

abort "No rows in #{csv_path}" if pairs.empty?

def compute_rhs(stale, suggested, merge_fragments)
  return suggested unless merge_fragments
  return suggested if suggested.include?("#")

  parts = stale.split("#", 2)
  frag = parts[1]
  return suggested if frag.nil? || frag.empty?

  sug_base, sug_frag = suggested.split("#", 2)
  # Keep suggested fragment if present
  return suggested if sug_frag

  # Insert fragment after path and query
  if sug_base.include?("?")
    path, q = sug_base.split("?", 2)
    "#{path}?#{q}##{frag}"
  else
    "#{sug_base}##{frag}"
  end
end

lines = File.readlines(redirect_file, chomp: true)

changes = []
lines.each_with_index do |line, idx|
  next if line.strip.start_with?("//")

  p = RedirectTargetVerify.parse_validurls_line(line)
  next unless p

  from_key = p[:lhs]
  old_to = p[:rhs]
  next unless pairs.key?(old_to)

  new_to = compute_rhs(old_to, pairs[old_to], merge_fragments)
  next if old_to == new_to
  next if RedirectTargetVerify.normalize_url_for_compare(old_to) == RedirectTargetVerify.normalize_url_for_compare(new_to)

  new_line = "#{p[:indent]}validurls['#{RedirectTargetVerify.escape_js_single_quoted(from_key)}'] = '#{RedirectTargetVerify.escape_js_single_quoted(new_to)}';"
  next if new_line == line

  changes << { idx: idx, old_line: line, new_line: new_line, old_to: old_to, new_to: new_to }
end

mode = dry_run ? "DRY-RUN" : "APPLY"
puts "#{mode}: #{pairs.size} stale_target key(s) in CSV, #{changes.size} validurls line(s) to change"
changes.first(30).each do |c|
  puts "  #{c[:old_to][0, 90]}#{c[:old_to].size > 90 ? '...' : ''}"
  puts "    -> #{c[:new_to][0, 90]}#{c[:new_to].size > 90 ? '...' : ''}"
end
puts "  ... (#{changes.size - 30} more)" if changes.size > 30

if dry_run
  puts "Run with --apply after triaging the CSV to write #{redirect_file}"
  exit 0
end

changes.each { |c| lines[c[:idx]] = c[:new_line] }
RedirectFileIO.atomic_write!(redirect_file, "#{lines.join("\n")}\n")
puts "Wrote #{redirect_file}"
exit 0
