require 'liquid'
require 'yaml'

module Jekyll
  module Converters
    class Markdown; end
  end
end

require_relative '../../_plugins/api'

class FakeMarkdownConverter
  def convert(input)
    input
  end
end

class FakeApiSite
  attr_reader :config, :data

  def initialize(data:)
    @config = {}
    @data = data
    @converter = FakeMarkdownConverter.new
  end

  def find_converter_instance(_klass)
    @converter
  end
end

RSpec.describe Api::Metadata do
  let(:config) do
    YAML.safe_load(
      File.read(File.expand_path('../../_data/api_metadata.yml', __dir__)),
      permitted_classes: [],
      permitted_symbols: [],
      aliases: false
    )
  end

  let(:fixture_html) do
    <<~HTML
      <h2 id="delete-users"><a href="#delete-users">Delete users</a></h2>
      <div class='api_tags' data-tags='User Data,Delete' data-tags-lower='user data,delete'></div>
      <p>Delete any user profile by specifying a known identifier. <span class="sr-only">Screen reader only</span></p>
      <pre class="highlight json"><code>
      <span class="p">{</span>
        <span class="nl">"external_ids"</span><span class="p">:</span>
        <span class="nl">"braze_ids"</span><span class="p">:</span>
        <span class="nl">"external_ids"</span><span class="p">:</span>
        <span class="nl">"Not_a_field"</span><span class="p">:</span>
      <span class="p">}</span>
      </code></pre>
    HTML
  end

  after { described_class.reset_cache! }

  it 'indexes the glossary h2 title, tags, description, and unique JSON keys' do
    expect(described_class.new(config).keywords_for(fixture_html)).to eq(
      'delete users user data,delete delete any user profile by specifying a known identifier. ' \
      'external_ids braze_ids'
    )
  end

  it 'indexes the h1 endpoint name instead of the first h2 on endpoint pages' do
    html = <<~HTML
      <h1 id="delete-catalog-selection">Delete catalog selection</h1>
      <h2 id="prerequisites">Prerequisites</h2>
      <h2 id="rate-limit">Rate limit</h2>
      <pre class="highlight json"><code>
        <span class="nl">"message"</span>
        <span class="nl">"errors"</span>
      </code></pre>
      <h2 id="troubleshooting">Troubleshooting</h2>
    HTML

    keywords = described_class.new(config).keywords_for(html)

    expect(keywords).to start_with('delete catalog selection')
    expect(keywords).to include('message')
    expect(keywords).to include('errors')
    expect(keywords).not_to include('prerequisites')
    expect(keywords).not_to include('rate limit')
    expect(keywords).not_to include('troubleshooting')
  end

  it 'includes heading text, tags, description, and unique JSON keys' do
    keywords = described_class.new(config).keywords_for(fixture_html)

    expect(keywords).to include('delete users')
    expect(keywords).to include('user data,delete')
    expect(keywords).to include('delete any user profile')
    expect(keywords).to include('external_ids')
    expect(keywords).to include('braze_ids')
    expect(keywords).not_to include('screen reader only')
    expect(keywords).not_to include('not_a_field')
  end

  it 'escapes quotes in assembled keywords' do
    html = %(<h2>Users "beta" and 'alpha'</h2>)

    expect(described_class.new(config).keywords_for(html))
      .to eq('users &quot;beta&quot; and &#39;alpha&#39;')
  end

  it 'wraps content with data-search-keywords from YAML-driven extraction' do
    html = described_class.new(config).wrap('api_testdividxx', '<p>body</p>')
    expect(html).to start_with("<div id='api_testdividxx' class='api_div' data-search-keywords='")
    expect(html).to end_with("'><p>body</p></div>")
  end

  it 'raises when _data/api_metadata.yml is missing' do
    expect { described_class.new(nil) }.to raise_error(ArgumentError, /api_metadata.yml/)
  end
end

RSpec.describe Api::ApiInfoBlock do
  let(:config) do
    YAML.safe_load(
      File.read(File.expand_path('../../_data/api_metadata.yml', __dir__)),
      permitted_classes: [],
      permitted_symbols: [],
      aliases: false
    )
  end

  after { Api::Metadata.reset_cache! }

  it 'reads extraction patterns from site.data api_metadata' do
    template = Liquid::Template.parse("{% api %}<h2>Rate limit</h2>{% endapi %}")
    site = FakeApiSite.new(data: { 'api_metadata' => config })
    html = template.render({}, registers: { site: site })

    expect(html).to include("class='api_div'")
    expect(html).to include("data-search-keywords='rate limit'")
    expect(html).to include('<h2>Rate limit</h2>')
  end
end
