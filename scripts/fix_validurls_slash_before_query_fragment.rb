#!/usr/bin/env ruby
# frozen_string_literal: true

# Ensures /docs/ paths end with / immediately before ?query or #fragment (Jekyll pretty URLs).
#
# Usage:
#   bundle exec ruby scripts/fix_validurls_slash_before_query_fragment.rb [--dry-run | --apply]
# Default: --dry-run. Use --apply to write via atomic replace.

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

apply = ARGV.include?("--apply")
apply = false if ARGV.include?("--dry-run")

lines = File.readlines(REDIRECT)
changed = 0
out = lines.map do |line|
  m = VALIDURLS.match(line.chomp)
  unless m
    line
  else
    indent, lhs, rhs = m[1], m[2], m[3]
    nl = ensure_slash_before_query_or_fragment(lhs)
    nr = ensure_slash_before_query_or_fragment(rhs)
    new_inner = "#{indent}validurls['#{RedirectTargetVerify.escape_js_single_quoted(nl)}'] = '#{RedirectTargetVerify.escape_js_single_quoted(nr)}';\n"
    changed += 1 if new_inner != line
    new_inner
  end
end

row_count = lines.count { |l| VALIDURLS.match?(l.chomp) }

if apply
  RedirectFileIO.atomic_write!(REDIRECT, out.join)
  puts "APPLY: updated #{row_count} validurls row(s) in #{REDIRECT} (#{changed} line(s) changed)."
else
  new_content = out.join
  old_content = File.read(REDIRECT)
  if new_content == old_content
    puts "DRY-RUN: no changes (#{row_count} validurls row(s))"
  else
    puts "DRY-RUN: would update #{row_count} validurls row(s), #{changed} line(s) would change. Run with --apply to write."
  end
end
