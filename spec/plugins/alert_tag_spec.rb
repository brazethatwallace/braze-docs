require 'liquid'

module Jekyll
  module Converters
    class Markdown; end
  end
end

require_relative '../../_plugins/alert_tag'

class FakeMarkdownConverter
  def convert(input)
    "<p>#{input}</p>\n"
  end
end

class FakeAlertSite
  attr_reader :config, :data

  def initialize(language:, data:, baseurl: '/docs')
    @config = { 'language' => language, 'baseurl' => baseurl }
    @data = data
    @converter = FakeMarkdownConverter.new
  end

  def find_converter_instance(_klass)
    @converter
  end
end

RSpec.describe Jekyll::Alerts::AlertTag do
  let(:data) do
    {
      'locales' => {
        'supported' => ['en', 'fr', 'es']
      },
      'alert_labels' => {
        'fr' => { 'note' => 'Remarque' },
        'es' => { 'note' => 'Nota' }
      }
    }
  end

  def render_alert(caption:, body:, language:, site_data: data)
    template = Liquid::Template.parse("{% alert #{caption} %}#{body}{% endalert %}")
    site = FakeAlertSite.new(language: language, data: site_data)
    template.render({}, registers: { site: site })
  end

  it 'renders localized labels from _data/alert_labels.yml' do
    html = render_alert(caption: 'note', body: 'Body', language: 'fr')

    expect(html).to include("class='alert alert-note'")
    expect(html).to include(">Remarque<")
  end

  it 'falls back to alert type text for unsupported locales' do
    html = render_alert(caption: 'note', body: 'Body', language: 'it')

    expect(html).to include(">note<")
  end

  it 'falls back to dashed caption text when locale label key is missing' do
    html = render_alert(caption: 'service-notice', body: 'Body', language: 'fr')

    expect(html).to include(">service notice<")
  end

  it 'preserves icon aliases for checkpoint alerts' do
    html = render_alert(caption: 'checkpoint', body: 'Body', language: 'fr')

    expect(html).to include("/assets/img/message-stop.png")
  end
end
