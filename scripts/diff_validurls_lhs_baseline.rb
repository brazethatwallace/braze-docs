#!/usr/bin/env ruby
# frozen_string_literal: true

# Compare baseline vs current broken_redirect_list.js by normalized LHS (with optional
# /docs/<locale>/ stripping). Redirect links must use /docs/... only (no locale prefix).
#
# Usage:
#   bundle exec ruby scripts/diff_validurls_lhs_baseline.rb --baseline PATH [--current PATH] [--csv-out PATH]
#   bundle exec ruby scripts/diff_validurls_lhs_baseline.rb --baseline PATH --apply-restores
#
# Options:
#   --baseline PATH            Required. Pre-IA snapshot (e.g. ~/Downloads/baseline_broken_redirect_list.js).
#   --current PATH             Default: assets/js/broken_redirect_list.js
#   --csv-out PATH             Write missing_lhs report (default: scripts/temp/missing_validurls_lhs.csv)
#   --apply-restores           Append missing rows to current file (baseline RHS; no chain collapse).
#   --no-strip-locale          Compare without stripping /docs/<locale>/ (not recommended).

require "csv"
require "fileutils"
require_relative "redirect_file_io"
require_relative "redirect_target_verify_helpers"

LOCALE_CODES = %w[ja ko de es fr_fr pt_br].freeze
LOCALE_RE = /\A\/docs\/(#{LOCALE_CODES.join('|')})(\/|\z)/.freeze

module DocsLocaleStrip
  module_function

  def strip_leading_docs_locale(url)
    s = url.to_s
    m = LOCALE_RE.match(s) or return s

    tail = s[m.end(0)..].to_s.delete_prefix("/")
    tail.empty? ? "/docs/" : "/docs/#{tail}"
  end
end

def parse_validurls(path)
  pairs = []
  File.foreach(path, chomp: true) do |line|
    next if line.strip.start_with?("//")

    p = RedirectTargetVerify.parse_validurls_line(line)
    pairs << { lhs: p[:lhs], rhs: p[:rhs] } if p
  end
  pairs
end

def norm_lhs(url, strip_locale:)
  u = strip_locale ? DocsLocaleStrip.strip_leading_docs_locale(url) : url.to_s
  RedirectTargetVerify.normalize_url_for_compare(u)
end

repo_root = File.expand_path("..", __dir__)
baseline_path = nil
current_path = File.join(repo_root, "assets", "js", "broken_redirect_list.js")
csv_out = File.join(repo_root, "scripts", "temp", "missing_validurls_lhs.csv")
apply_restores = false
strip_locale = true

args = ARGV.dup
while args.any?
  a = args.shift
  case a
  when "--baseline"
    baseline_path = args.shift
  when "--current"
    current_path = args.shift
  when "--csv-out"
    csv_out = args.shift
  when "--apply-restores"
    apply_restores = true
  when "--no-strip-locale"
    strip_locale = false
  else
    abort "Unknown option #{a}\nusage: diff_validurls_lhs_baseline.rb --baseline PATH [--current PATH] [--csv-out PATH] [--apply-restores] [--no-strip-locale]"
  end
end

abort "Missing --baseline PATH" unless baseline_path
baseline_path = [File.expand_path(baseline_path), File.expand_path(baseline_path, repo_root)].find { |p| File.file?(p) }
abort "Baseline not found" unless baseline_path && File.file?(baseline_path)

current_path = [File.expand_path(current_path), File.expand_path(current_path, repo_root)].find { |p| File.file?(p) }
abort "Current redirect file not found: #{current_path}" unless current_path && File.file?(current_path)

baseline_pairs = parse_validurls(baseline_path)
current_pairs = parse_validurls(current_path)

current_norms = current_pairs.map { |p| norm_lhs(p[:lhs], strip_locale: strip_locale) }.to_set

# First baseline occurrence wins representative lhs/rhs per normalized key
seen_norm = {}
baseline_pairs.each do |p|
  n = norm_lhs(p[:lhs], strip_locale: strip_locale)
  next if seen_norm.key?(n)

  seen_norm[n] = { lhs: p[:lhs], rhs: p[:rhs] }
end

missing = seen_norm.reject { |n, _| current_norms.include?(n) }

puts "Baseline: #{baseline_path} (#{baseline_pairs.size} lines)"
puts "Current:  #{current_path} (#{current_pairs.size} lines)"
puts "Unique baseline LHS (norm): #{seen_norm.size}"
puts "Missing in current (norm): #{missing.size}"

FileUtils.mkdir_p(File.dirname(csv_out))
CSV.open(csv_out, "w", write_headers: true, headers: %w[normalized_lhs baseline_lhs baseline_rhs]) do |csv|
  missing.each do |norm, h|
    csv << [norm, h[:lhs], h[:rhs]]
  end
end
puts "Wrote #{csv_out}"

if apply_restores
  lines = File.readlines(current_path, chomp: true)
  block = []
  block << ""
  block << "// Restored LHS from baseline (diff_validurls_lhs_baseline.rb --apply-restores)"
  missing.each_value do |h|
    lhs = RedirectTargetVerify.escape_js_single_quoted(h[:lhs])
    rhs = RedirectTargetVerify.escape_js_single_quoted(h[:rhs])
    block << "validurls['#{lhs}'] = '#{rhs}';"
  end
  RedirectFileIO.atomic_write!(current_path, "#{lines.join("\n")}\n#{block.join("\n")}\n")
  puts "Appended #{missing.size} validurls line(s) to #{current_path}"
  exit 0
end

exit missing.empty? ? 0 : 1
