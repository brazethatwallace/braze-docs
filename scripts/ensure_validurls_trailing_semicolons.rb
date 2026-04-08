#!/usr/bin/env ruby
# frozen_string_literal: true

# One-off / maintenance: append ';' to validurls assignment lines that omit it (ASI-only).
# After migration, audit/normalize tools require a trailing semicolon per VALIDURLS_LINE_RX.

require_relative "redirect_file_io"

redirect = File.join(__dir__, "..", "assets", "js", "broken_redirect_list.js")
abort "Missing #{redirect}" unless File.file?(redirect)

dry_run = !ARGV.include?("--apply")

lines = File.readlines(redirect)
fixed = 0
out = lines.map do |line|
  ch = line.chomp
  if !ch.strip.start_with?("//") && ch.match?(/\A(\s*)validurls\['([^']+)'\]\s*=\s*'([^']*)'\s*\z/)
    fixed += 1
    "#{ch};\n"
  else
    line
  end
end

if dry_run
  puts "DRY-RUN: would add semicolon to #{fixed} line(s). Run with --apply to write."
  exit 0
end

RedirectFileIO.atomic_write!(redirect, out.join)
puts "Wrote #{redirect} (#{fixed} line(s) fixed)"
exit 0
