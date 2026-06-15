#!/usr/bin/env ruby
# frozen_string_literal: true

# Verifies a Jekyll docs build: every <loc> in sitemap.xml resolves to HTML under the site
# directory, optionally <link rel="canonical"> matches <loc>, and optionally completeness
# (sitemap URL set equals URLs derived from eligible Markdown under the content root).
#
# Despite the filename, this script is **locale-agnostic**; the `en` name is historical.
# Use `--locale <code>` (see LOCALE_REGISTRY) or explicit `--site-dir`, `--config`, `--source-dir`.
#
# English (default): `bundle exec rake docs_en:build` → sitemap at _site/sitemap.xml, content _docs/.
#
# Localized docs: `bundle exec rake 'lang:build[<code>]'` merges _config.yml + _lang/_config_<...>.yml
# for homeurl/baseurl/destination; sitemap under that destination (e.g. _site/docs/de/sitemap.xml).
#
# LOCALE_REGISTRY (rake arg == --locale after downcase):
#   de     → _lang/_config_de.yml,    source _lang/de,     site _site/docs/de,     JSON sitemap_de.json
#   es     → _lang/_config_es.yml,    source _lang/es,     site _site/docs/es,     JSON sitemap_es.json
#   fr     → _lang/_config_fr.yml,    source _lang/fr_fr,  site _site/docs/fr,     JSON sitemap_fr_fr.json
#   ja     → _lang/_config_ja.yml,    source _lang/ja,     site _site/docs/ja,     JSON sitemap_ja.json
#   ko     → _lang/_config_ko.yml,    source _lang/ko,     site _site/docs/ko,     JSON sitemap_ko.json
#   pt-br  → _lang/_config_pt-br.yml, source _lang/pt_br,   site _site/docs/pt-br,  JSON sitemap_pt_br.json
#
# --completeness uses source Markdown (not a blind _site walk) so redirect/config-only pages
# that still emit HTML do not inflate **P**, the Markdown-derived URL set (see completeness diagnostics).
# Custom permalink in frontmatter can break path-based **P** (same caveat as English).
#
# Usage (repo root):
#   bundle exec ruby scripts/verify_sitemap_en_build.rb
#   bundle exec ruby scripts/verify_sitemap_en_build.rb --canonical --completeness
#   bundle exec ruby scripts/verify_sitemap_en_build.rb --locale de --canonical --completeness
#   bundle exec ruby scripts/verify_sitemap_en_build.rb --site-dir _site --config _config.yml --source-dir _docs

require "date"
require "optparse"
require "pathname"
require "rexml/document"
require "set"
require "time"
require "uri"
require "yaml"

# Rake lang:build key => lang overlay config (merged on top of _config.yml), Markdown root for completeness.
LOCALE_REGISTRY = {
  "de" => {
    lang_config: "_lang/_config_de.yml",
    source_dir: "_lang/de"
  },
  "es" => {
    lang_config: "_lang/_config_es.yml",
    source_dir: "_lang/es"
  },
  "fr" => {
    lang_config: "_lang/_config_fr.yml",
    source_dir: "_lang/fr_fr"
  },
  "ja" => {
    lang_config: "_lang/_config_ja.yml",
    source_dir: "_lang/ja"
  },
  "ko" => {
    lang_config: "_lang/_config_ko.yml",
    source_dir: "_lang/ko"
  },
  "pt-br" => {
    lang_config: "_lang/_config_pt-br.yml",
    source_dir: "_lang/pt_br"
  }
}.freeze

# _docs/_<segment>/ (or _lang/<locale>/_<segment>/) for public collections. Omit hidden, docs_pages.
COMPLETENESS_COLLECTION_SEGMENTS = %w[
  api contributing developer_guide help home partners releases user_guide
].freeze

def load_jekyll_config(path)
  YAML.safe_load(File.read(path), permitted_classes: [Date, Time], aliases: true)
end

# Shallow merge matches Jekyll multi-config overlay for top-level keys we read (homeurl, baseurl, destination).
def merge_jekyll_configs(base_path, overlay_path)
  base = load_jekyll_config(base_path)
  over = load_jekyll_config(overlay_path)
  base.merge(over)
end

options = {
  site_dir: nil,
  config_path: "_config.yml",
  sitemap_path: nil,
  source_dir: nil,
  canonical: false,
  completeness: false,
  locale: nil,
  site_dir_explicit: false
}

OptionParser.new do |opts|
  opts.banner = "Usage: #{$PROGRAM_NAME} [options]"

  opts.on("--site-dir=PATH", "Jekyll output directory (default: _site or config destination)") do |v|
    options[:site_dir] = v
    options[:site_dir_explicit] = true
  end
  opts.on("--config=PATH", "Jekyll config when not using --locale (default: _config.yml)") { |v| options[:config_path] = v }
  opts.on("--source-dir=PATH", "Markdown root for --completeness (default: _docs or locale registry)") do |v|
    options[:source_dir] = v
  end
  opts.on("--sitemap=PATH", "Path to sitemap.xml (default: <site-dir>/sitemap.xml)") { |v| options[:sitemap_path] = v }
  opts.on("--locale=CODE", "Pilot: #{LOCALE_REGISTRY.keys.join(', ')} — merges _config.yml + lang overlay") do |v|
    options[:locale] = v
  end
  opts.on("--canonical", "Assert canonical link matches each <loc>") { options[:canonical] = true }
  opts.on("--completeness", "Assert sitemap <loc> set equals eligible Markdown URL set") { options[:completeness] = true }
end.parse!

repo_root = Dir.pwd
base_config_path = File.expand_path("_config.yml", repo_root)

if options[:locale]
  code = options[:locale].downcase
  reg = LOCALE_REGISTRY[code]
  unless reg
    warn "Unknown --locale #{options[:locale].inspect}. Known: #{LOCALE_REGISTRY.keys.join(', ')}"
    exit 2
  end
  overlay_path = File.expand_path(reg[:lang_config], repo_root)
  unless File.file?(base_config_path)
    warn "Missing base config: #{base_config_path}"
    exit 2
  end
  unless File.file?(overlay_path)
    warn "Missing lang config: #{overlay_path}"
    exit 2
  end
  cfg = merge_jekyll_configs(base_config_path, overlay_path)
  config_label = "#{base_config_path} + #{overlay_path}"
  site_dir_rel = options[:site_dir_explicit] ? options[:site_dir] : (cfg["destination"] || "_site")
  site_dir = File.expand_path(site_dir_rel, repo_root)
  source_dir = options[:source_dir] || reg[:source_dir]
else
  config_path = File.expand_path(options[:config_path], repo_root)
  unless File.file?(config_path)
    warn "Missing config: #{config_path}"
    exit 2
  end
  cfg = load_jekyll_config(config_path)
  config_label = config_path
  site_dir_rel = options[:site_dir] || cfg["destination"] || "_site"
  site_dir = File.expand_path(site_dir_rel, repo_root)
  source_dir = options[:source_dir] || "_docs"
end

sitemap_path = options[:sitemap_path] ? File.expand_path(options[:sitemap_path], repo_root) : File.join(site_dir, "sitemap.xml")

unless File.file?(sitemap_path)
  warn "Missing sitemap: #{sitemap_path} (run the appropriate Jekyll build first)"
  exit 2
end
unless File.directory?(site_dir)
  warn "Missing site dir: #{site_dir}"
  exit 2
end

homeurl = cfg.fetch("homeurl", "https://www.braze.com").to_s.chomp("/")
baseurl = cfg.fetch("baseurl", "/docs").to_s
baseurl = "/#{baseurl.delete_prefix("/")}" unless baseurl.start_with?("/")
url_prefix = "#{homeurl}#{baseurl}"

def normalize_comparison_url(url)
  url.to_s.strip.chomp("/")
end

def loc_to_site_paths(site_dir, url_path_under_docs)
  rel = url_path_under_docs.delete_prefix("/")
  if rel.empty? || rel.end_with?("/")
    dir = File.join(site_dir, rel)
    [File.join(dir, "index.html")]
  else
    base = File.join(site_dir, rel)
    ["#{base}.html", File.join(base, "index.html"), base]
  end
end

def extract_canonical(html)
  return nil unless html

  if (m = html.match(%r{<link\s[^>]*\brel\s*=\s*["']canonical["'][^>]*>}i))
    tag = m[0]
    if (h = tag.match(/\bhref\s*=\s*["']([^"']+)["']/i))
      return h[1]
    end
  end
  if (m = html.match(%r{<link\s[^>]*\bhref\s*=\s*["']([^"']+)["'][^>]*\brel\s*=\s*["']canonical["'][^>]*>}i))
    return m[1]
  end
  nil
end

def read_yaml_frontmatter(path)
  content = File.read(path, encoding: "UTF-8")
  return nil unless content.match?(/\A---\s*(\r?\n)/)

  m = content.match(/\A---\s*?\r?\n(.*?)^---\s*?(?:\r?\n|\z)/m)
  return nil unless m

  YAML.safe_load(m[1], permitted_classes: [Date, Time], aliases: true) || {}
rescue Psych::SyntaxError, ArgumentError
  nil
end

def sitemap_eligible_frontmatter?(fm)
  return false if fm.nil?
  return false unless fm.is_a?(Hash)

  return false if fm["published"] == false
  return false if fm["hidden"] == true
  return false if fm["noindex"] == true
  return false if fm["config_only"] == true

  layout = fm["layout"].to_s
  return false if layout == "redirect"
  return false if layout == "blank_config"

  true
end

def md_path_to_normalized_url(md_path, segment, docs_dir, url_prefix)
  coll_dir = File.join(docs_dir, "_#{segment}")
  rel = Pathname.new(md_path).relative_path_from(Pathname.new(coll_dir)).to_s
  return nil if rel.start_with?("..")

  body = rel.sub(/\.md\z/, "")
  path_part =
    if body.empty?
      "#{segment}/"
    else
      "#{segment}/#{body}/"
    end
  web_path = "/#{path_part.tr('\\', '/')}".gsub(%r{/+}, "/")
  normalize_comparison_url("#{url_prefix}#{web_path}")
end

def completeness_p_set(docs_dir, site_dir, url_prefix, sitemap_loc_set)
  p_set = Set.new

  COMPLETENESS_COLLECTION_SEGMENTS.each do |segment|
    coll_dir = File.join(docs_dir, "_#{segment}")
    next unless File.directory?(coll_dir)

    Dir.glob(File.join(coll_dir, "**", "*.md"), File::FNM_DOTMATCH).each do |md_path|
      next if File.basename(md_path).start_with?(".")

      fm = read_yaml_frontmatter(md_path)
      next if fm.nil?
      next unless sitemap_eligible_frontmatter?(fm)

      url = md_path_to_normalized_url(md_path, segment, docs_dir, url_prefix)
      p_set.add(url) if url
    end
  end

  root_norm = normalize_comparison_url("#{url_prefix}/")
  if sitemap_loc_set.include?(root_norm) && File.file?(File.join(site_dir, "index.html"))
    p_set.add(root_norm)
  end

  p_set
end

xml = File.read(sitemap_path)
doc = REXML::Document.new(xml)
missing_fs = []
wrong_scheme = []
canonical_mismatches = []

sitemap_loc_set = Set.new
doc.elements.each("//urlset/url/loc") do |el|
  loc = el.text.to_s.strip
  next if loc.empty?

  sitemap_loc_set.add(normalize_comparison_url(loc))
end

doc.elements.each("//urlset/url/loc") do |el|
  loc = el.text.to_s.strip
  next if loc.empty?

  begin
    uri = URI.parse(loc)
  rescue URI::InvalidURIError
    wrong_scheme << "#{loc} (invalid URI)"
    next
  end
  unless %w[http https].include?(uri.scheme)
    wrong_scheme << loc
    next
  end

  path = uri.path.to_s
  path = "/#{path.delete_prefix("/")}"

  unless path == baseurl || path.start_with?("#{baseurl}/")
    wrong_scheme << "#{loc} (path not under #{baseurl})"
    next
  end

  under = path.delete_prefix(baseurl)
  under = under.delete_prefix("/")

  candidates = loc_to_site_paths(site_dir, under)
  html_path = candidates.find { |p| File.file?(p) }
  unless html_path
    missing_fs << loc
    next
  end

  next unless options[:canonical]

  html = File.read(html_path, encoding: "UTF-8")
  canon = extract_canonical(html)
  unless canon
    canonical_mismatches << "#{loc} (no canonical in #{html_path})"
    next
  end

  if normalize_comparison_url(canon) != normalize_comparison_url(loc)
    canonical_mismatches << "#{loc} (canonical: #{canon})"
  end
end

puts "Sitemap build check"
puts "  Config: #{config_label}"
puts "  Locale: #{options[:locale] || 'en (default)'}"
puts "  Sitemap: #{sitemap_path}"
puts "  Site dir: #{site_dir}"
puts "  Content root (completeness): #{source_dir}"
puts "  URL prefix: #{url_prefix}"
puts "  Canonical check: #{options[:canonical]}"
puts "  Completeness check: #{options[:completeness]}"

exit_code = 0

if wrong_scheme.any?
  puts "  Invalid or out-of-scope URLs: #{wrong_scheme.size}"
  wrong_scheme.first(20).each { |x| puts "    #{x}" }
  puts "    …" if wrong_scheme.size > 20
  exit_code = 1
end

if missing_fs.any?
  puts "  Missing built files for <loc>: #{missing_fs.size}"
  missing_fs.first(30).each { |x| puts "    #{x}" }
  puts "    …" if missing_fs.size > 30
  exit_code = 1
end

if canonical_mismatches.any?
  puts "  Canonical mismatches: #{canonical_mismatches.size}"
  canonical_mismatches.first(30).each { |x| puts "    #{x}" }
  puts "    …" if canonical_mismatches.size > 30
  exit_code = 1
end

if options[:completeness]
  docs_dir = File.expand_path(source_dir, repo_root)
  unless File.directory?(docs_dir)
    warn "Missing content directory for completeness: #{docs_dir}"
    exit 2
  end

  p_set = completeness_p_set(docs_dir, site_dir, url_prefix, sitemap_loc_set)
  s_minus_p = sitemap_loc_set - p_set
  p_minus_s = p_set - sitemap_loc_set

  if s_minus_p.any? || p_minus_s.any?
    puts "  Completeness: S (sitemap) has #{sitemap_loc_set.size} URLs, P (Markdown-derived) has #{p_set.size} URLs"
    if s_minus_p.any?
      puts "  In sitemap but not in Markdown set (S − P): #{s_minus_p.size}"
      s_minus_p.sort.first(30).each { |u| puts "    #{u}" }
      puts "    …" if s_minus_p.size > 30
    end
    if p_minus_s.any?
      puts "  Markdown set but not in sitemap (P − S): #{p_minus_s.size}"
      p_minus_s.sort.first(30).each { |u| puts "    #{u}" }
      puts "    …" if p_minus_s.size > 30
    end
    exit_code = 1
  else
    puts "  OK — completeness: S and P both have #{sitemap_loc_set.size} URLs."
  end
end

if exit_code.zero?
  n = doc.get_elements("//urlset/url/loc").size
  puts "  OK — #{n} <loc> entries verified."
end

exit exit_code
