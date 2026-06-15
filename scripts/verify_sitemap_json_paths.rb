#!/usr/bin/env ruby
# frozen_string_literal: true

# Verifies every path key in _data/sitemap_<locale>.json maps to an existing file under a content root.
# Default root is _docs (English). Localized docs use --content-root (e.g. _lang/ja for sitemap_ja.json).
#
# Pair with scripts/verify_sitemap_en_build.rb after the matching Jekyll build.
#
# Usage (repo root):
#   bundle exec ruby scripts/verify_sitemap_json_paths.rb
#   bundle exec ruby scripts/verify_sitemap_json_paths.rb _data/sitemap_en.json
#   bundle exec ruby scripts/verify_sitemap_json_paths.rb --content-root _lang/ja _data/sitemap_ja.json

require "json"
require "optparse"

content_root = "_docs"
parser = OptionParser.new do |opts|
  opts.banner = "Usage: #{$PROGRAM_NAME} [options] [sitemap_json_path]"

  opts.on("--content-root PATH", "Directory with _api, _user_guide, … (default: _docs)") do |v|
    content_root = v
  end
end
args = parser.order!(ARGV)

unless File.directory?(content_root)
  warn "Content root not found: #{content_root}"
  exit 2
end

sitemap_path = args[0] || "_data/sitemap_en.json"
unless File.file?(sitemap_path)
  warn "Missing #{sitemap_path}"
  exit 2
end

map = JSON.parse(File.read(sitemap_path))
missing = []
map.each_key do |key|
  rel = key.start_with?("_") ? key : "_#{key}"
  path = File.join(content_root, rel)
  missing << key unless File.file?(path)
end

puts "Sitemap path check: #{sitemap_path}"
puts "  Content root: #{content_root}"
puts "  Entries: #{map.size}, missing files: #{missing.size}"
if missing.any?
  missing.first(30).each { |k| puts "  #{k}" }
  puts "  …" if missing.size > 30
  exit 1
end

puts "OK — every sitemap key resolves to a file under #{content_root}/."
exit 0
