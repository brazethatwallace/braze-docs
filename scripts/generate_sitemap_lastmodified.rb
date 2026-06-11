#!/usr/bin/env ruby
# frozen_string_literal: true

# Generates _data/sitemap_<locale>.json last-modified timestamps from git history.
# Article lastmod is the max of the article file date and all transitive includes
# (see _plugins/multi_lang_include.rb for include resolution rules).

require 'find'
require 'time'
require 'json'
require 'set'
require 'pathname'

LANGUAGES = %w[en de es fr_fr ja ko pt_br].freeze
ALLOWED_FOLDERS = %w[_home _user_guide _developer_guide _api _partners _help _contributing].freeze
INCREMENTAL_SINCE = '2 weeks ago'
INCLUDE_TAG =
  /\{%-?\s*(?:multi_lang_include|include)\s+(?:'([^']+)'|"([^"]+)"|([\w\/.\-()+~\#@]+))/m.freeze

def check_git!
  return if system('git rev-parse --git-dir > /dev/null 2>&1')

  puts 'Error: Not in a git repository or git not available'
  exit 1
end

def locale_for_directory(directory)
  directory == '_docs' ? 'en' : directory.sub(%r{\A_lang/}, '')
end

def folder_patterns(directory)
  ALLOWED_FOLDERS.map { |f| "#{directory}/#{f}/**/*.md" }
end

def include_patterns(locale)
  if locale == 'en'
    ['_includes/**/*.md']
  else
    ["_lang/#{locale}/_includes/**/*.md", '_includes/**/*.md']
  end
end

def all_tracked_patterns(directory, locale)
  folder_patterns(directory) + include_patterns(locale)
end

def format_git_date(raw)
  Time.parse(raw).utc.strftime('%Y-%m-%dT%H:%M:%S+00:00')
end

def today_timestamp
  Time.now.utc.strftime('%Y-%m-%dT%H:%M:%S+00:00')
end

# ── Include parsing and resolution (keep in sync with multi_lang_include.rb) ──

module IncludeReferenceParser
  module_function

  def extract_paths(content)
    return [] if content.nil? || content.empty?

    content.scan(INCLUDE_TAG).filter_map do |quoted_single, quoted_double, bare|
      (quoted_single || quoted_double || bare)&.strip
    end.uniq
  end
end

module IncludePathResolver
  module_function

  def normalize_include_ref(ref)
    ref = ref.strip
    ref.end_with?('.md') ? ref : "#{ref}.md"
  end

  def resolve(include_ref, locale, repo_root = '.')
    path = normalize_include_ref(include_ref)
    candidates = if locale == 'en'
                   [File.join(repo_root, '_includes', path)]
                 else
                   [
                     File.join(repo_root, '_lang', locale, '_includes', path),
                     File.join(repo_root, '_includes', path)
                   ]
                 end

    found = candidates.find { |candidate| File.file?(candidate) }
    return nil unless found

    Pathname.new(File.expand_path(found)).relative_path_from(Pathname.new(File.expand_path(repo_root))).to_s
  end

  def locale_for_file(repo_relative_path)
    if repo_relative_path.start_with?('_lang/')
      repo_relative_path.split('/')[1]
    else
      'en'
    end
  end
end

class IncludeDependencyGraph
  def initialize(content_root:, locale:, repo_root: '.')
    @repo_root = repo_root
    @content_root = content_root
    @locale = locale
    @direct_deps = Hash.new { |h, k| h[k] = [] }
    @reverse_index = Hash.new { |h, k| h[k] = Set.new }
    @parsed = Set.new
  end

  attr_reader :direct_deps, :reverse_index

  def include_file?(repo_relative_path)
    repo_relative_path.start_with?('_includes/') || repo_relative_path.include?('/_includes/')
  end

  def filesystem_path(repo_relative_path)
    if include_file?(repo_relative_path)
      File.join(@repo_root, repo_relative_path)
    else
      File.join(@repo_root, @content_root, repo_relative_path)
    end
  end

  def register_file(repo_relative_path)
    return @direct_deps[repo_relative_path] if @parsed.include?(repo_relative_path)

    @parsed.add(repo_relative_path)
    full_path = filesystem_path(repo_relative_path)
    unless File.file?(full_path)
      @direct_deps[repo_relative_path] = []
      return []
    end

    locale = include_file?(repo_relative_path) ? IncludePathResolver.locale_for_file(repo_relative_path) : @locale
    content = File.read(full_path)
    refs = IncludeReferenceParser.extract_paths(content)

    resolved = refs.filter_map do |ref|
      IncludePathResolver.resolve(ref, locale, @repo_root)
    end.uniq

    @direct_deps[repo_relative_path] = resolved
    resolved.each { |inc| @reverse_index[inc] << repo_relative_path }
    resolved
  end

  def register_article(repo_relative_path)
    register_file(repo_relative_path)
    transitive_includes(repo_relative_path).each { |inc| register_file(inc) }
  end

  def transitive_includes(repo_relative_path, visited = nil)
    visited ||= Set.new
    return [] if visited.include?(repo_relative_path)

    visited.add(repo_relative_path)
    register_file(repo_relative_path)

    @direct_deps[repo_relative_path].flat_map do |include_path|
      [include_path] + transitive_includes(include_path, visited)
    end.uniq
  end

  def articles_affected_by_includes(changed_include_paths, article_paths)
    article_set = article_paths.to_set
    affected = Set.new

    changed_include_paths.each do |include_path|
      queue = [include_path]
      visited = Set.new

      until queue.empty?
        current = queue.pop
        next if visited.include?(current)

        visited.add(current)

        @reverse_index[current]&.each do |dependent|
          if article_set.include?(dependent)
            affected << dependent
          elsif dependent.include?('_includes/')
            queue << dependent
          end
        end
      end
    end

    affected.to_a
  end
end

# ── Git dates ────────────────────────────────────────────────────────────────

def git_ls_files_dates(patterns)
  return {} if patterns.empty?

  quoted = patterns.map { |p| "'#{p}'" }.join(' ')
  files = `git ls-files #{quoted}`.split("\n").map(&:strip).reject(&:empty?)

  git_dates = {}
  files.each do |path|
    date_str = `git log -1 --format='%cI' -- '#{path}'`.strip
    next if date_str.empty?

    git_dates[path] = format_git_date(date_str)
  rescue StandardError => e
    puts "Warning: Could not parse date for #{path}: #{e.message}"
  end

  git_dates
end

def get_all_git_dates(directory, locale)
  puts 'Getting git history for articles and includes...'
  patterns = all_tracked_patterns(directory, locale)
  git_dates = git_ls_files_dates(patterns)
  puts "Found git history for #{git_dates.length} tracked files"
  git_dates
end

def parse_git_log_output(result)
  git_dates = {}
  current_date = nil

  result.split("\n").each do |line|
    line = line.strip.delete("'")
    next if line.empty?

    if line.match?(/^\d{4}-\d{2}-\d{2}T/)
      current_date = line
    elsif current_date && line.end_with?('.md')
      git_dates[line] ||= format_git_date(current_date)
    end
  end

  git_dates
end

def get_recent_git_dates(directory, locale)
  puts "Getting files changed since #{INCREMENTAL_SINCE}..."
  patterns = all_tracked_patterns(directory, locale)
  quoted = patterns.map { |p| "'#{p}'" }.join(' ')
  cmd = "git log --since='#{INCREMENTAL_SINCE}' --name-only --pretty=format:'%cI' -- #{quoted}"
  result = `#{cmd}`.strip
  git_dates = parse_git_log_output(result)
  puts "Found #{git_dates.length} files modified since #{INCREMENTAL_SINCE}"
  git_dates
end

def get_single_file_date(path)
  date_str = `git log -1 --format='%cI' -- '#{path}'`.strip
  return today_timestamp if date_str.empty?

  format_git_date(date_str)
rescue StandardError => e
  puts "Warning: Could not parse date for #{path}: #{e.message}"
  today_timestamp
end

def max_timestamp(*timestamps)
  timestamps.compact.max_by { |ts| Time.parse(ts) }
end

def monotonic_lastmod(computed, existing)
  return computed if existing.nil? || existing.empty?

  max_timestamp(computed, existing)
end

def effective_lastmod(article_relative, graph, git_dates, directory)
  article_repo_path = File.join(directory, article_relative)

  dates = [git_dates[article_repo_path] || get_single_file_date(article_repo_path)]
  graph.transitive_includes(article_relative).each do |include_path|
    dates << (git_dates[include_path] || get_single_file_date(include_path))
  end

  max_timestamp(*dates)
end

# ── Sitemap generation ───────────────────────────────────────────────────────

def load_existing_data(output_file)
  return {} unless File.exist?(output_file)

  data = JSON.parse(File.read(output_file))
  data.transform_values! { |v| v.length <= 10 ? "#{v}T00:00:00+00:00" : v }
  puts "Loaded #{data.length} existing entries from #{output_file}"
  data
rescue JSON::ParserError => e
  puts "Warning: Could not parse existing data file (#{e.message}), running full scan"
  {}
end

def collect_article_paths(directory)
  paths = []
  ALLOWED_FOLDERS.each do |folder|
    folder_path = File.join(directory, folder)
    next unless Dir.exist?(folder_path)

    Find.find(folder_path) do |path|
      next if File.directory?(path)
      next unless path.end_with?('.md')

      paths << path
    end
  end
  paths
end

def build_dependency_graph(directory, locale, article_paths)
  graph = IncludeDependencyGraph.new(content_root: directory, locale: locale)
  article_paths.each do |full_path|
    repo_relative = full_path.sub(%r{\A#{Regexp.escape(directory)}/}, '')
    graph.register_article(repo_relative)
  end
  graph
end

def generate_file_listing(directory, output_file, full: false)
  unless Dir.exist?(directory)
    puts "Error: Directory '#{directory}' does not exist"
    exit 1
  end

  locale = locale_for_directory(directory)
  prior_sitemap_data = load_existing_data(output_file)
  existing_data = full ? {} : prior_sitemap_data
  incremental = !existing_data.empty?

  git_dates = if incremental
                get_recent_git_dates(directory, locale)
              else
                get_all_git_dates(directory, locale)
              end

  article_paths = collect_article_paths(directory)
  article_relative_paths = article_paths.map { |p| p.sub(%r{\A#{Regexp.escape(directory)}/}, '') }
  graph = build_dependency_graph(directory, locale, article_paths)

  file_data = existing_data.dup
  missing_files = []
  recomputed = 0

  changed_includes = git_dates.keys.select do |path|
    path.start_with?('_includes/') || path.include?('/_includes/')
  end
  affected_by_includes = if incremental && !changed_includes.empty?
                           graph.articles_affected_by_includes(changed_includes, article_relative_paths)
                         else
                           Set.new
                         end

  if incremental && !changed_includes.empty?
    puts "Includes changed: #{changed_includes.length} → recomputing #{affected_by_includes.size} articles"
  end

  article_paths.each do |path|
    relative_path = path.sub(%r{\A#{Regexp.escape(directory)}/}, '')
    repo_article_path = File.join(directory, relative_path)

    should_recompute = !incremental ||
                       git_dates.key?(repo_article_path) ||
                       affected_by_includes.include?(relative_path) ||
                       !existing_data.key?(relative_path)

    next unless should_recompute

    computed = effective_lastmod(relative_path, graph, git_dates, directory)
    file_data[relative_path] = monotonic_lastmod(computed, prior_sitemap_data[relative_path])
    recomputed += 1
  end

  unless missing_files.empty?
    puts "Backfilling #{missing_files.length} new files not in existing data..."
    missing_files.each do |path|
      relative_path = path.sub(%r{\A#{Regexp.escape(directory)}/}, '')
      computed = effective_lastmod(relative_path, graph, git_dates, directory)
      file_data[relative_path] = monotonic_lastmod(computed, prior_sitemap_data[relative_path])
    end
  end

  if incremental
    before = file_data.length
    file_data.reject! do |key, _|
      full_path = File.join(directory, key)
      missing = !File.exist?(full_path)
      puts "Pruning deleted file: #{key}" if missing
      missing
    end
    pruned = before - file_data.length
    puts "Pruned #{pruned} deleted entries" if pruned.positive?
  end

  File.write(output_file, JSON.pretty_generate(file_data))

  mode_label = incremental ? 'incremental' : 'full'
  puts "File listing generated (#{mode_label}): #{output_file} (#{file_data.length} files, #{recomputed} recomputed)"
end

# ── CLI ──────────────────────────────────────────────────────────────────────

if __FILE__ == $PROGRAM_NAME
full_mode = ARGV.delete('--full')

if ARGV.length > 2
  puts "Usage: ruby #{$PROGRAM_NAME} [locale] [output_file] [--full]"
  puts ''
  puts 'Options:'
  puts "  locale       Language code (#{LANGUAGES.join(', ')}) or 'all'. Default: en"
  puts '  output_file  Custom output path (ignored with \'all\'). Default: _data/sitemap_<locale>.json'
  puts '  --full       Force a full git scan even when existing data is available'
  puts ''
  puts 'Examples:'
  puts "  ruby #{$PROGRAM_NAME}                  # incremental update for en"
  puts "  ruby #{$PROGRAM_NAME} all              # incremental update for all languages"
  puts "  ruby #{$PROGRAM_NAME} all --full       # full scan for all languages"
  puts "  ruby #{$PROGRAM_NAME} ja               # incremental update for ja"
  puts "  ruby #{$PROGRAM_NAME} en --full        # full scan for en"
  puts "  ruby #{$PROGRAM_NAME} en custom.json   # custom output path"
  exit 1
end

check_git!

locale = ARGV[0] || 'en'
output_file = ARGV[1]

if locale == 'all'
  LANGUAGES.each do |lang|
    directory = lang == 'en' ? '_docs' : "_lang/#{lang}"
    out = "_data/sitemap_#{lang}.json"
    puts "\n=== Processing #{lang} ==="
    generate_file_listing(directory, out, full: full_mode)
  end
else
  unless LANGUAGES.include?(locale)
    puts "Error: Unknown locale '#{locale}'. Supported: #{LANGUAGES.join(', ')}, all"
    exit 1
  end
  directory = locale == 'en' ? '_docs' : "_lang/#{locale}"
  out = output_file || "_data/sitemap_#{locale}.json"
  generate_file_listing(directory, out, full: full_mode)
end
end
