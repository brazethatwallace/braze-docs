#!/usr/bin/env ruby
# frozen_string_literal: true

# Normalize validurls in assets/js/broken_redirect_list.js.
#
# Passes (run in this order when using --all, the default):
#   1. Semicolons  – append trailing ';' to validurls assignments that omit it.
#   2. Slash fix   – ensure /docs/ paths end with '/' before ?query or #fragment.
#   3. Full norm   – lowercase internal paths & fragments, deduplicate by LHS,
#                    restore Jekyll canonical casing on RHS, trim trailing slashes.
#
# Usage:
#   bundle exec ruby scripts/normalize_broken_redirect_list.rb [--dry-run | --apply] [MODE]
#
# Modes (pick one, default --all):
#   --all              Full normalization (semicolons + slash fix + full norm)
#   --semicolons-only  Only fix missing trailing semicolons
#   --slash-fix-only   Only fix missing slash before ?query / #fragment
#
# Default: --dry-run (no write). Use --apply to write via atomic replace.

REPO_ROOT = File.expand_path("..", __dir__)
REDIRECT = File.join(REPO_ROOT, "assets", "js", "broken_redirect_list.js")

require_relative "redirect_file_io"
require_relative "redirect_target_verify_helpers"

VALIDURLS = RedirectTargetVerify::VALIDURLS_LINE_RX

# Regex for lines that look like validurls assignments but lack a trailing semicolon.
VALIDURLS_NO_SEMI = /\A(\s*)validurls\['([^']+)'\]\s*=\s*'([^']*)'\s*\z/

# ---------- Semicolon pass --------------------------------------------------

def fix_semicolons(content)
  fixed = 0
  out = content.each_line.map do |line|
    ch = line.chomp
    if !ch.strip.start_with?("//") && ch.match?(VALIDURLS_NO_SEMI)
      fixed += 1
      "#{ch};\n"
    else
      line
    end
  end
  [out.join, fixed]
end

# ---------- URL helpers ------------------------------------------------------

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

# ---------- Slash-fix-only pass ----------------------------------------------

def slash_fix_only(content)
  changed = 0
  out = content.each_line.map do |line|
    m = VALIDURLS.match(line.chomp)
    unless m
      line
    else
      indent, lhs, rhs = m[1], m[2], m[3]
      nl = ensure_slash_before_query_or_fragment(lhs)
      nr = ensure_slash_before_query_or_fragment(rhs)
      new_line = "#{indent}validurls['#{RedirectTargetVerify.escape_js_single_quoted(nl)}'] = '#{RedirectTargetVerify.escape_js_single_quoted(nr)}';\n"
      changed += 1 if new_line != line
      new_line
    end
  end
  [out.join, changed]
end

# ---------- Full normalization pass ------------------------------------------

def full_normalize(content)
  lines = content.each_line.to_a

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

  [out.join, vu_rows.size]
end

# ---------- Main -------------------------------------------------------------

def main
  apply = ARGV.include?("--apply")
  apply = false if ARGV.include?("--dry-run")

  mode = if ARGV.include?("--semicolons-only")
           :semicolons
         elsif ARGV.include?("--slash-fix-only")
           :slash_fix
         else
           :all
         end

  old_content = File.read(REDIRECT)
  new_content = old_content
  summary_parts = []

  # Pass 1: Semicolons (always runs in :all and :semicolons modes)
  if mode == :all || mode == :semicolons
    new_content, semi_fixed = fix_semicolons(new_content)
    summary_parts << "#{semi_fixed} semicolon(s) added" if semi_fixed.positive?
  end

  # Pass 2: Slash fix (always runs in :all and :slash_fix modes)
  if mode == :all || mode == :slash_fix
    new_content, slash_changed = slash_fix_only(new_content)
    summary_parts << "#{slash_changed} slash fix(es)" if slash_changed.positive?
  end

  # Pass 3: Full normalization (only in :all mode)
  if mode == :all
    new_content, vu_count = full_normalize(new_content)
    summary_parts << "#{vu_count} validurls row(s) normalized"
  end

  summary = summary_parts.empty? ? "no changes" : summary_parts.join(", ")

  if new_content == old_content
    puts "#{apply ? 'APPLY' : 'DRY-RUN'}: no changes needed (#{summary})"
  elsif apply
    RedirectFileIO.atomic_write!(REDIRECT, new_content)
    puts "APPLY: wrote #{REDIRECT} (#{summary}; #{old_content.bytesize} -> #{new_content.bytesize} bytes)"
  else
    puts "DRY-RUN: would rewrite #{REDIRECT} (#{summary}; #{old_content.bytesize} -> #{new_content.bytesize} bytes). Run with --apply to write."
  end
end

main
