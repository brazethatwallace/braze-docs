#!/usr/bin/env ruby
# frozen_string_literal: true

# Rewrites validurls lines keyed by exact LHS string. Safer than apply_validurl_rhs_from_csv
# when multiple LHS share the same RHS and need different destinations.
#
# CSV columns: lhs, suggested_jekyll_url (required). Optional: notes (ignored).
# Skips rows with blank suggested_jekyll_url.
#
# Usage:
#   bundle exec ruby scripts/apply_validurl_by_lhs_csv.rb --csv PATH [--dry-run | --apply]

require "csv"
require_relative "redirect_file_io"
require_relative "redirect_target_verify_helpers"

dry_run = true
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
  when "--csv"
    csv_path = args.shift
  when "--redirect-file"
    redirect_file = args.shift
  else
    abort "Unknown option #{a}\nusage: apply_validurl_by_lhs_csv.rb --csv PATH [--dry-run|--apply] [--redirect-file PATH]"
  end
end

abort "Missing --csv PATH" unless csv_path

repo_root = File.expand_path("..", __dir__)
resolved = [File.expand_path(csv_path, Dir.pwd), File.expand_path(csv_path, repo_root)].uniq.find { |p| File.file?(p) }
abort "CSV not found: #{csv_path}" unless resolved

csv_path = resolved
abort "Missing #{redirect_file}" unless File.file?(redirect_file)

pairs = {}
CSV.foreach(csv_path, headers: true) do |row|
  lhs = row["lhs"]&.strip
  sug = row["suggested_jekyll_url"]&.strip
  next if lhs.nil? || sug.nil? || lhs.empty? || sug.empty?

  pairs[lhs] = sug
end

abort "No lhs/suggested_jekyll_url rows in #{csv_path}" if pairs.empty?

lines = File.readlines(redirect_file, chomp: true)
changes = []

lines.each_with_index do |line, idx|
  next if line.strip.start_with?("//")

  p = RedirectTargetVerify.parse_validurls_line(line)
  next unless p

  from_key = p[:lhs]
  next unless pairs.key?(from_key)

  new_rhs = pairs[from_key]
  new_line = "#{p[:indent]}validurls['#{RedirectTargetVerify.escape_js_single_quoted(from_key)}'] = '#{RedirectTargetVerify.escape_js_single_quoted(new_rhs)}';"
  next if new_line == line

  changes << { idx: idx, old_line: line, new_line: new_line, lhs: from_key, new_rhs: new_rhs }
end

mode = dry_run ? "DRY-RUN" : "APPLY"
puts "#{mode}: #{pairs.size} lhs key(s) in CSV, #{changes.size} line(s) to update"
changes.first(40).each do |c|
  puts "  #{c[:lhs][0, 100]}#{c[:lhs].size > 100 ? '...' : ''}"
  puts "    -> #{c[:new_rhs][0, 100]}#{c[:new_rhs].size > 100 ? '...' : ''}"
end
puts "  ... (#{changes.size - 40} more)" if changes.size > 40

missing_lhs = pairs.keys - changes.map { |c| c[:lhs] }
unless missing_lhs.empty?
  puts "WARN: #{missing_lhs.size} CSV lhs key(s) not found as validurls LHS in file (first 10):"
  missing_lhs.first(10).each { |k| puts "  #{k[0, 120]}" }
end

if dry_run
  puts "Run with --apply to write #{redirect_file}"
  exit 0
end

changes.each { |c| lines[c[:idx]] = c[:new_line] }
RedirectFileIO.atomic_write!(redirect_file, "#{lines.join("\n")}\n")
puts "Wrote #{redirect_file}"
exit 0
