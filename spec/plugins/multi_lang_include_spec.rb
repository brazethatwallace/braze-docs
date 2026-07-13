require 'fileutils'
require 'liquid'
require 'tmpdir'

require_relative '../../_plugins/multi_lang_include'

class FakeIncludeSite
  attr_reader :config, :data

  def initialize(source:, language:, locales_data:)
    @config = { 'source' => source, 'language' => language }
    @data = { 'locales' => locales_data }
  end

  def file_read_opts
    {}
  end
end

RSpec.describe Jekyll::Tags::IncludeAbsoluteTag do
  let(:locales_data) do
    {
      'supported' => ['en', 'fr', 'pt-br'],
      'include_dir_overrides' => {
        'fr' => 'fr_fr',
        'pt-br' => 'pt_br'
      }
    }
  end

  def render_include(source:, language:, body: '{% multi_lang_include sample.md %}')
    template = Liquid::Template.parse(body)
    site = FakeIncludeSite.new(source: source, language: language, locales_data: locales_data)
    template.render({}, registers: { site: site })
  end

  it 'loads localized include content using locale override mapping' do
    Dir.mktmpdir do |dir|
      FileUtils.mkdir_p(File.join(dir, '_lang', 'fr_fr', '_includes'))
      FileUtils.mkdir_p(File.join(dir, '_includes'))
      File.write(File.join(dir, '_lang', 'fr_fr', '_includes', 'sample.md'), 'FR include')
      File.write(File.join(dir, '_includes', 'sample.md'), 'EN include')

      output = render_include(source: dir, language: 'fr')
      expect(output).to include('FR include')
    end
  end

  it 'falls back to english include when localized file is missing' do
    Dir.mktmpdir do |dir|
      FileUtils.mkdir_p(File.join(dir, '_lang', 'fr_fr', '_includes'))
      FileUtils.mkdir_p(File.join(dir, '_includes'))
      File.write(File.join(dir, '_includes', 'sample.md'), 'EN include')

      output = render_include(source: dir, language: 'fr')
      expect(output).to include('EN include')
    end
  end

  it 'falls back to english include path for unsupported locales' do
    Dir.mktmpdir do |dir|
      FileUtils.mkdir_p(File.join(dir, '_includes'))
      File.write(File.join(dir, '_includes', 'sample.md'), 'EN include')

      output = render_include(source: dir, language: 'it')
      expect(output).to include('EN include')
    end
  end
end
