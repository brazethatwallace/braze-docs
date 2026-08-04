require 'fileutils'
require 'find'
require 'thread'
require 'yaml'

def resolve_utf8_locale(existing_locale)
  return existing_locale if existing_locale.to_s.match?(/UTF-8/i)

  return 'C.UTF-8'
end

def default_utf8_build_env
  {
    'LANG' => resolve_utf8_locale(ENV['LANG']),
    'LC_ALL' => resolve_utf8_locale(ENV['LC_ALL'])
  }
end

# File watching functionality
def watch_includes_folder
  puts "Starting file watcher for _includes folder..."
  load 'includes_watcher.rb'
  watcher = IncludesWatcher.new
  watcher.start
rescue Interrupt
  puts "File watcher interrupted, shutting down..."
rescue => e
  puts "File watcher error: #{e.message}"
end

def pipe(command, env = {})
  output = ''
  runtime_env = default_utf8_build_env.merge(env)
  IO.popen(runtime_env, command) do |io|
    until io.eof?
      buffer = io.gets
      output << buffer
      puts buffer
    end
  end

  output
end

task default: :serve

def load_locales_config(path = './_data/locales.yml')
  unless File.exist?(path)
    abort "Missing locale configuration file: #{path}"
  end

  config = YAML.safe_load(File.read(path), aliases: true)
  config = {} unless config.is_a?(Hash)

  supported = Array(config['supported']).map { |code| code.to_s.downcase }.uniq
  if supported.empty?
    abort "Locale configuration must include at least one entry under 'supported'."
  end

  task_aliases = config['task_aliases']
  task_aliases = task_aliases.is_a?(Hash) ? task_aliases.transform_keys(&:to_s).transform_values(&:to_s) : {}

  {
    'supported' => supported,
    'task_aliases' => task_aliases
  }
rescue Psych::SyntaxError => e
  abort "Failed to parse locale configuration in #{path}: #{e.message}"
end

LOCALES_CONFIG = load_locales_config
SUPPORTED_LOCALES = LOCALES_CONFIG['supported'].freeze
NON_EN_LOCALES = SUPPORTED_LOCALES.reject { |locale| locale == 'en' }.freeze
LOCALE_TASK_ALIASES = LOCALES_CONFIG['task_aliases'].freeze

def locale_task_name(locale)
  alias_name = LOCALE_TASK_ALIASES[locale]
  return alias_name unless alias_name.nil? || alias_name.empty?

  locale.tr('-', '_')
end

def fast_jekyll_build?
  %w[1 true yes].include?(ENV.fetch('JEKYLL_FAST', '').downcase) ||
    %w[1 true yes].include?(ENV.fetch('BRAZE_DOCS_FAST_BUILD', '').downcase)
end

def jekyll_build_configs(config_file, incremental: false)
  incremental ||= fast_jekyll_build?
  return config_file unless incremental
  return config_file if config_file.include?('_incremental_config')

  "#{config_file},_incremental_config.yml"
end

def jekyll_build(config_file = '_config.yml', lang = 'en', incremental: false)
  public_folder = './public'
  configs = jekyll_build_configs(config_file, incremental: incremental)
  command = ['bundle', 'exec', 'jekyll', 'build', '--config', configs]
  command << '--incremental' if incremental || fast_jekyll_build?
  pipe(command)
  if (lang != 'en')
    index_file = File.join(public_folder, "index_#{lang}.html")
    FileUtils.copy_file(index_file, File.join('_site', "index.html"))
    FileUtils.copy_file(File.join("_site/docs/#{lang}", "404.html"), File.join('_site', "404.html"))
  end
  verify_llms_txt_artifacts(lang)
end

# Post-build sanity check: confirms the llms.txt / llms-full.txt files the
# llms_txt_generator plugin is supposed to emit are actually present on disk.
# Only enforced for the English build (other locales don't generate them).
def verify_llms_txt_artifacts(lang)
  return unless lang == 'en'
  return if %w[1 true yes].include?(ENV.fetch('SKIP_LLMS_TXT_VERIFY', '').downcase)

  expected = %w[user_guide developer_guide api partners releases].flat_map do |collection|
    %W[_site/#{collection}/llms.txt _site/#{collection}/llms-full.txt]
  end

  missing = expected.reject { |path| File.exist?(path) && File.size(path) > 0 }
  if missing.empty?
    puts "LLMS verify: all #{expected.length} llms.txt artifacts present in _site."
    return
  end

  warn "LLMS verify: missing or empty artifacts after Jekyll build:"
  missing.each { |path| warn "  - #{path}" }
  warn "LLMS verify: this means the llms_txt_generator plugin did not run."
  warn "LLMS verify: set SKIP_LLMS_TXT_VERIFY=1 to bypass this check."
  abort "LLMS verify: failing the build so the deploy doesn't ship without llms.txt files."
end
def jekyll_serve(config_file = '_config.yml')
  if ENV["RACK_ENV"] == 'staging'
    pipe "bundle exec jekyll s --port 5006 --config #{config_file}"
  else
    # Dropping .jekyll-metadata forces a full rebuild (slow). Omit unless you need
    # a clean slate (asset pipeline oddities, stale incremental cache): JEKYLL_CLEAN=1 rake
    if %w[1 true yes].include?(ENV.fetch('JEKYLL_CLEAN', '').downcase)
      puts `rm -f .jekyll-metadata`
    end

    # Start file watcher in a separate thread
    watcher_thread = Thread.new do
      watch_includes_folder
    end
    
    # Set up signal handlers to stop the watcher thread
    Signal.trap('INT') do
      puts "\nStopping Jekyll serve and file watcher..."
      watcher_thread.raise Interrupt
      exit 0
    end
    
    Signal.trap('TERM') do
      puts "\nStopping Jekyll serve and file watcher..."
      watcher_thread.raise Interrupt
      exit 0
    end
    
    begin
      pipe "bundle exec jekyll s --port 5006 --incremental --config #{config_file},_incremental_config.yml"
    ensure
      # Ensure the watcher thread is stopped when Jekyll exits
      watcher_thread.raise Interrupt if watcher_thread.alive?
      watcher_thread.join(2) # Wait up to 2 seconds for clean shutdown
    end
  end
end

namespace :docs_en do
  config_file = './_config.yml'
  task :index do
    if ENV["SITE_URL"] == 'https://www.braze.com' && ENV["RACK_ENV"] == 'production'
      puts `bundle exec jekyll algolia --config #{config_file}`
    end
  end
  task build: [:index] do
      jekyll_build(config_file, 'en')
  end
  task build_fast: [:index] do
    jekyll_build(config_file, 'en', incremental: true)
  end
  task :serve do
    jekyll_serve(config_file)
  end
  task :serve_with_watch do
    jekyll_serve(config_file)
  end
  task :proxy_serve do
    pipe 'bundle exec ruby proxy.rb'
  end
end

namespace :lang do
  task :index, [:lang] do |t, args|
    config_file = "./_config.yml,./_lang/_config_#{args[:lang]}.yml"
    if ENV["SITE_URL"] == 'https://www.braze.com' && ENV["RACK_ENV"] == 'production'
      puts `bundle exec jekyll algolia --config #{config_file}`
    end
  end
  task :build, [:lang] => [:index] do |t, args|
    jekyll_build("./_config.yml,./_lang/_config_#{args[:lang]}.yml", args[:lang])
  end
  task :build_fast, [:lang] => [:index] do |t, args|
    jekyll_build("./_config.yml,./_lang/_config_#{args[:lang]}.yml", args[:lang], incremental: true)
  end
  task :serve, [:lang] do |t, args|
    jekyll_serve("./_config.yml,./_lang/_config_#{args[:lang]}.yml")
  end
  task :serve_with_watch, [:lang] do |t, args|
    jekyll_serve("./_config.yml,./_lang/_config_#{args[:lang]}.yml")
  end
  task :proxy_serve, [:lang] do |t, args|
    pipe "bundle exec ruby proxy.rb #{args[:lang]}"
  end
end

namespace :assets do
  task :precompile do
    print 'no-op'
  end
end


# Usage: rake "lang[:lang]" ie
# rake "lang[:fr]"
# rake "lang[:ja]"
multitask :lang, [:lang] => [
  'lang:serve',
  'lang:proxy_serve'
]

multitask serve: [
  'docs_en:serve', 'docs_en:proxy_serve'
]

multitask en: [
  'docs_en:serve', 'docs_en:proxy_serve'
]

NON_EN_LOCALES.each do |locale|
  task_name = locale_task_name(locale)

  task task_name.to_sym do
    Rake::Task['lang'].invoke(locale)
  end

  task "#{task_name}_build".to_sym do
    Rake::Task['lang:build'].invoke(locale)
  end
end

# Convenience tasks for file watching
task :serve_with_test_watch do
  Rake::Task["docs_en:serve_with_watch"].invoke
end

task :serve_with_lint_watch do
  Rake::Task["docs_en:serve_with_watch"].invoke
end

task :serve_with_build_watch do
  Rake::Task["docs_en:serve_with_watch"].invoke
end

# Usage examples:
# rake serve_with_test_watch          # Serve with file watching (same as serve_with_watch)
# rake serve_with_lint_watch          # Serve with file watching (same as serve_with_watch)
# rake serve_with_build_watch         # Serve with file watching (same as serve_with_watch)
# rake docs_en:serve_with_watch       # Serve English docs with file watching
# rake "lang:serve_with_watch[fr]"    # Serve French docs with file watching
