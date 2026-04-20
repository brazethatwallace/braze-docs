#!/usr/bin/env ruby
# frozen_string_literal: true

# Regenerate PR 13182 triage CSVs. Run from repo root:
#   ruby scripts/reference/pr13182_redirect_qa/regenerate_report.rb BASE_SHA HEAD_SHA [OUT_DIR]

require "csv"
require "fileutils"

BASE = ARGV[0] || abort("usage: ruby #{$PROGRAM_NAME} BASE_SHA HEAD_SHA [OUT_DIR]")
HEAD = ARGV[1] || abort("usage: ruby #{$PROGRAM_NAME} BASE_SHA HEAD_SHA [OUT_DIR]")
REPO_ROOT = File.expand_path("../../..", __dir__)
OUT_DIR = ARGV[2] ? File.expand_path(ARGV[2], REPO_ROOT) : File.join(REPO_ROOT, "scripts", "temp")

RX = /\A(\s*)validurls\['([^']+)'\]\s*=\s*'([^']*)'\s*;?\s*\z/

def norm_lhs_key(lhs)
  lhs.to_s.strip.downcase.gsub(%r{/+\z}, "")
end

def validurls_rows(git_ref)
  raw = IO.popen(["git", "show", "#{git_ref}:assets/js/broken_redirect_list.js"], &:read)
  rows = []
  raw.each_line.with_index(1) do |line, lineno|
    ch = line.chomp
    next if ch.strip.start_with?("//")
    m = ch.match(RX)
    next unless m

    rows << {
      line: lineno,
      lhs: m[2],
      rhs: m[3],
      had_semi: ch.rstrip.end_with?(";"),
      norm: norm_lhs_key(m[2])
    }
  end
  rows
end

def group_by_norm(rows)
  h = Hash.new { |hash, key| hash[key] = [] }
  rows.each { |r| h[r[:norm]] << r }
  h
end

base_rows = validurls_rows(BASE)
head_rows = validurls_rows(HEAD)
base_g = group_by_norm(base_rows)
head_g = group_by_norm(head_rows)

all_keys = (base_g.keys + head_g.keys).uniq.sort

FileUtils.mkdir_p(OUT_DIR)

CSV.open(File.join(OUT_DIR, "redirect_pr_develop_duplicate_norm_lhs.csv"), "w") do |csv|
  csv << %w[normalized_lhs_key occurrences develop_line_lhs_rhs_pairs]
  base_g.each do |k, list|
    next if list.size < 2

    pairs = list.map { |r| "L#{r[:line]}:#{r[:lhs]}=>#{r[:rhs]}" }.join(" | ")
    csv << [k, list.size, pairs]
  end
end

summary_path = File.join(OUT_DIR, "redirect_pr_lhs_summary.csv")
CSV.open(summary_path, "w") do |csv|
  csv << %w[
    normalized_lhs_key
    change_bucket
    develop_count pr_count
    develop_last_lhs develop_last_rhs develop_last_line
    pr_last_lhs pr_last_rhs pr_last_line
    notes
  ]

  all_keys.each do |k|
    bl = base_g.fetch(k, [])
    hl = head_g.fetch(k, [])
    b = bl.last
    h = hl.last

    bucket = if bl.any? && hl.any?
               if bl.size > 1
                 "develop_had_duplicate_norm_lhs"
               elsif b[:lhs] == h[:lhs] && b[:rhs] == h[:rhs]
                 b[:had_semi] == h[:had_semi] ? "unchanged" : "semicolon_only"
               else
                 "modified"
               end
             elsif bl.any? && hl.empty?
               "removed_from_pr"
             elsif bl.empty? && hl.any?
               "added_in_pr"
             else
               "unknown"
             end

    notes = []
    notes << "develop #{bl.size} row(s), PR #{hl.size} row(s)" if bl.size != hl.size
    notes << "develop duplicate norm keys collapsed on PR" if bl.size > 1 && hl.size <= 1
    notes << "semicolon fix" if b && h && b[:had_semi] != h[:had_semi]
    notes << "lhs string canonicalized" if b && h && b[:lhs] != h[:lhs]

    csv << [
      k,
      bucket,
      bl.size,
      hl.size,
      b ? b[:lhs] : "",
      b ? b[:rhs] : "",
      b ? b[:line] : "",
      h ? h[:lhs] : "",
      h ? h[:rhs] : "",
      h ? h[:line] : "",
      notes.join(" | ")
    ]
  end
end

CSV.open(File.join(OUT_DIR, "redirect_pr_lhs_modified_or_semicolon.csv"), "w") do |csv|
  csv << %w[normalized_lhs_key bucket develop_lhs develop_rhs pr_lhs pr_rhs develop_count pr_count notes]

  all_keys.each do |k|
    bl = base_g.fetch(k, [])
    hl = head_g.fetch(k, [])
    next unless bl.any? && hl.any?

    b = bl.last
    h = hl.last
    next if bl.size == 1 && b[:lhs] == h[:lhs] && b[:rhs] == h[:rhs] && b[:had_semi] == h[:had_semi]

    bucket = if bl.size > 1
               "develop_duplicate_collapsed"
             elsif b[:rhs] != h[:rhs] || b[:lhs] != h[:lhs]
               "content_or_lhs_change"
             else
               "semicolon_only"
             end
    notes = []
    notes << "semicolon" if b[:had_semi] != h[:had_semi]
    notes << "lhs" if b[:lhs] != h[:lhs]
    notes << "rhs" if b[:rhs] != h[:rhs]
    csv << [k, bucket, b[:lhs], b[:rhs], h[:lhs], h[:rhs], bl.size, hl.size, notes.join("+")]
  end
end

CSV.open(File.join(OUT_DIR, "redirect_pr_lhs_removed.csv"), "w") do |csv|
  csv << %w[normalized_lhs_key develop_row_count sample_lhs sample_rhs sample_line]
  all_keys.each do |k|
    bl = base_g.fetch(k, [])
    hl = head_g.fetch(k, [])
    next unless bl.any? && hl.empty?

    s = bl.last
    csv << [k, bl.size, s[:lhs], s[:rhs], s[:line]]
  end
end

CSV.open(File.join(OUT_DIR, "redirect_pr_lhs_added.csv"), "w") do |csv|
  csv << %w[normalized_lhs_key pr_row_count sample_lhs sample_rhs sample_line]
  all_keys.each do |k|
    bl = base_g.fetch(k, [])
    hl = head_g.fetch(k, [])
    next unless bl.empty? && hl.any?

    s = hl.last
    csv << [k, hl.size, s[:lhs], s[:rhs], s[:line]]
  end
end

review = File.join(REPO_ROOT, "scripts", "reference", "pr13182_redirect_qa", "redirect_pr_lhs_summary_review.csv")
review_rows = []
CSV.foreach(summary_path, headers: true) do |row|
  review_rows << row if row["change_bucket"] != "unchanged"
end
CSV.open(review, "w") do |w|
  if review_rows.any?
    w << review_rows.first.headers
    review_rows.each { |r| w << r.fields }
  end
end
non_unchanged = review_rows.size

puts "Wrote under #{OUT_DIR}:"
puts "  redirect_pr_develop_duplicate_norm_lhs.csv"
puts "  redirect_pr_lhs_summary.csv (large)"
puts "  redirect_pr_lhs_modified_or_semicolon.csv"
puts "  redirect_pr_lhs_removed.csv"
puts "  redirect_pr_lhs_added.csv"
puts "Updated #{review} (#{non_unchanged} non-unchanged rows)"
puts "Base validurls rows: #{base_rows.size} (#{base_g.size} unique norm lhs)"
puts "Head validurls rows: #{head_rows.size} (#{head_g.keys.size} unique norm lhs)"
