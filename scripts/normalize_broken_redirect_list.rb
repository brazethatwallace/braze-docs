#!/usr/bin/env ruby
# frozen_string_literal: true

# Normalize validurls in assets/js/broken_redirect_list.js (full pass).
# - /docs/ paths: no trailing slash when the URL ends at the path (no ? or #)
# - /docs/ paths: trailing slash required immediately before ?query or #fragment
# - Internal paths (starting with /): lowercase; https URLs: trim terminal / only
# - Fragments: lowercase (path segment casing preserved via restore_jekyll_canonical_segments on RHS)
# - Duplicate LHS after normalize: keep last assignment (JavaScript semantics)
#
# Usage:
#   bundle exec ruby scripts/normalize_broken_redirect_list.rb [--dry-run | --apply]
# Default: --dry-run (no write). Use --apply to write via atomic replace.

REPO_ROOT = File.expand_path("..", __dir__)
REDIRECT = File.join(REPO_ROOT, "assets", "js", "broken_redirect_list.js")

require_relative "redirect_file_io"
require_relative "redirect_target_verify_helpers"

VALIDURLS = RedirectTargetVerify::VALIDURLS_LINE_RX

def split_hash_query(url)
  frag = nil
  body = url
  if body.include?("#")
    body, rest = body.split("#", 2)
    frag = "##{rest}"
  end
  query = nil
  if body.include?("?")
    body, q = body.split("?", 2)
    query = "?#{q}"
  end
  [body, query, frag]
end

def join_path_query_frag(path, query, frag)
  "#{path}#{query}#{frag}"
end

def ensure_slash_before_query_or_fragment(url)
  return url if url.match?(%r{\Ahttps?://}i)

  path, query, frag = split_hash_query(url)
  return url if path.empty? || !(query || frag)
  return url unless path.start_with?("/docs/")
  return url if RedirectTargetVerify.path_looks_like_file?(path)

  path += "/" unless path.end_with?("/")
  join_path_query_frag(path, query, frag)
end

def restore_jekyll_canonical_segments(rhs)
  rhs.gsub("legacy_sdks/macos", "legacy_sdks/macOS").gsub(
    "apple_mail/email_private_relay_apple_sso",
    "apple_mail/email_private_relay_apple_SSO"
  )
end

def normalize_touched_url(url)
  path, query, frag = split_hash_query(url)
  has_suffix = !!(query || frag)

  if path.match?(%r{\Ahttps?://}i)
    path = path.sub(%r{/\z}, "")
  elsif path.start_with?("/")
    path = path.gsub(%r{/+\z}, "").downcase
    if has_suffix && path.start_with?("/docs/") && !RedirectTargetVerify.path_looks_like_file?(path)
      path += "/" unless path.end_with?("/")
    end
  end

  if frag && frag.length > 1
    frag = "##{frag[1..].downcase}"
  end

  out = join_path_query_frag(path, query, frag)
  ensure_slash_before_query_or_fragment(out)
end

def main
  apply = ARGV.include?("--apply")
  if ARGV.any? { |a| a == "--dry-run" }
    apply = false
  end

  lines = File.readlines(REDIRECT)

  parsed = lines.each_with_index.map do |line, idx|
    raw = line.chomp
    m = VALIDURLS.match(raw)
    if m
      { idx: idx, kind: :vu, indent: m[1], lhs: m[2], rhs: m[3], raw: raw }
    else
      { idx: idx, kind: :raw, line: line }
    end
  end

  vu_rows = parsed.select { |r| r[:kind] == :vu }
  vu_rows.each do |r|
    r[:new_lhs] = normalize_touched_url(r[:lhs])
    r[:new_rhs] = restore_jekyll_canonical_segments(normalize_touched_url(r[:rhs]))
  end

  winner_idx = {}
  vu_rows.each do |r|
    winner_idx[r[:new_lhs]] = r[:idx]
  end

  out = []
  parsed.each do |r|
    if r[:kind] == :raw
      out << r[:line]
      next
    end

    next unless winner_idx[r[:new_lhs]] == r[:idx]

    lhs_e = RedirectTargetVerify.escape_js_single_quoted(r[:new_lhs])
    rhs_e = RedirectTargetVerify.escape_js_single_quoted(r[:new_rhs])
    out << "#{r[:indent]}validurls['#{lhs_e}'] = '#{rhs_e}';\n"
  end

  removed = vu_rows.size - winner_idx.size
  warn "Deduped #{removed} duplicate validurls rows (last assignment kept per LHS)." if removed.positive?

  new_content = out.join
  old_content = File.read(REDIRECT)

  if apply
    RedirectFileIO.atomic_write!(REDIRECT, new_content)
    puts "APPLY: wrote #{REDIRECT}"
  elsif new_content == old_content
    puts "DRY-RUN: no changes (#{vu_rows.size} validurls row(s) considered)"
  else
    puts "DRY-RUN: would rewrite #{REDIRECT} (#{vu_rows.size} validurls row(s); output size #{old_content.bytesize} -> #{new_content.bytesize} bytes). Run with --apply to write."
  end
end

main
