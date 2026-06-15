#!/usr/bin/env ruby
# frozen_string_literal: true

# Verifies redirect destinations for mappings required by validate_doc_redirects.rb
# exist in the Jekyll URL map for HEAD (proves targets resolve after build).
#
# Usage (after ./bdocs check_redirects --json scripts/temp/redirect-report.json):
#   bundle exec ruby scripts/jekyll_url_map_dump.rb /tmp/jekyll-url-map-head.json
#   bundle exec ruby scripts/verify_redirect_targets_in_jekyll.rb scripts/temp/redirect-report.json /tmp/jekyll-url-map-head.json
#
# Optional: audit legacy validurls rows whose RHS is not a published Jekyll URL:
#   bundle exec ruby scripts/verify_redirect_targets_in_jekyll.rb --audit-stale /tmp/jekyll-url-map-head.json
#
# Full categorized CSV audit (known suggestions vs unsure):
#   bundle exec ruby scripts/audit_validurls_targets_vs_jekyll.rb /tmp/jekyll-url-map-head.json

require "json"
require_relative "redirect_target_verify_helpers"

def audit_stale_redirect_targets(map_path)
  published = RedirectTargetVerify.load_published_urls(map_path)
  redirect_file = File.join(__dir__, "..", "assets", "js", "broken_redirect_list.js")
  stale = []
  File.foreach(redirect_file, chomp: true) do |line|
    next if line.strip.start_with?("//")
    p = RedirectTargetVerify.parse_validurls_line(line)
    next unless p

    _from, to = p[:lhs], p[:rhs]
    next if to.strip.empty?

    stale << to unless RedirectTargetVerify.published_include?(published, to)
  end
  puts "Stale redirect target audit (RHS not matching any Jekyll doc URL on HEAD)"
  puts "  Jekyll map: #{map_path}"
  puts "  Stale count: #{stale.size}"
  stale.first(25).each { |u| puts "  #{u}" }
  puts "  …" if stale.size > 25
  puts "  Note: Legacy rows often predate IA; fix high-traffic keys as time allows."
end

if ARGV[0] == "--audit-stale"
  map_path = ARGV[1] || "/tmp/jekyll-url-map-head.json"
  unless File.file?(map_path)
    warn "Missing #{map_path}"
    exit 2
  end

  audit_stale_redirect_targets(map_path)
  exit 0
end

report_path = ARGV[0] || "scripts/temp/redirect-report.json"
map_path = ARGV[1] || "/tmp/jekyll-url-map-head.json"

unless File.file?(report_path)
  warn "Missing #{report_path} — run: ./bdocs check_redirects --base origin/develop --json #{report_path}"
  exit 2
end
unless File.file?(map_path)
  warn "Missing #{map_path} — run: bundle exec ruby scripts/jekyll_url_map_dump.rb #{map_path}"
  exit 2
end

report = JSON.parse(File.read(report_path))
pairs = report["required_mappings"] || []
if pairs.empty?
  warn "No required_mappings in #{report_path} — re-run check_redirects with an updated validate_doc_redirects.rb"
  exit 2
end

published = RedirectTargetVerify.load_published_urls(map_path)
missing = []
pairs.each do |row|
  to = row["to"]
  next if to.nil? || to.to_s.strip.empty?

  missing << row unless RedirectTargetVerify.published_include?(published, to)
end

puts "Required redirect target check (#{pairs.size} mappings from #{report_path})"
puts "  Jekyll map: #{map_path}"
if missing.empty?
  puts "OK — every required redirect destination matches a Jekyll doc URL on HEAD."
  exit 0
end

puts "FAILED — #{missing.size} required destination(s) missing from Jekyll map:"
missing.first(20).each { |row| puts "  #{row['from']} → #{row['to']}" }
puts "  …" if missing.size > 20
exit 1
