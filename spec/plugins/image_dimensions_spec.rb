require 'fileutils'
require 'tmpdir'

require_relative '../../_plugins/image_dimensions'

class FakeDimensionSite
  attr_reader :config

  def initialize(baseurl: '/docs', image_dimensions: { 'enabled' => true })
    @config = {
      'baseurl' => baseurl,
      'image_dimensions' => image_dimensions
    }
  end
end

RSpec.describe Jekyll::ImageDimensions do
  let(:site) { FakeDimensionSite.new }

  def build_webp_chunk(fourcc, payload)
    payload = payload.b
    chunk = fourcc.b + [payload.bytesize].pack('V') + payload
    body = 'WEBP'.b + chunk
    'RIFF'.b + [body.bytesize].pack('V') + body
  end

  before { described_class.clear_cache! }

  describe '.read_dimensions' do
    it 'reads PNG dimensions from a real asset' do
      path = 'assets/img/empty-cc.png'
      skip "fixture #{path} missing" unless File.file?(path)

      dims = described_class.read_dimensions(path)
      expect(dims).to eq({ width: 832, height: 1478 })
    end

    it 'reads VP8X WebP canvas dimensions as little-endian 24-bit values' do
      payload = [
        0,
        0, 0, 0,
        99, 0, 0,
        49, 0, 0
      ].pack('C*')
      webp = build_webp_chunk('VP8X', payload)

      Dir.mktmpdir do |dir|
        path = File.join(dir, 'vp8x.webp')
        File.binwrite(path, webp)
        expect(described_class.read_dimensions(path)).to eq({ width: 100, height: 50 })
      end
    end

    it 'reads lossy VP8 WebP dimensions after the frame tag' do
      frame = [
        0, 0, 0,
        0x9D, 0x01, 0x2A,
        200, 0,
        100, 0
      ].pack('C*')
      webp = build_webp_chunk('VP8 ', frame)

      Dir.mktmpdir do |dir|
        path = File.join(dir, 'vp8.webp')
        File.binwrite(path, webp)
        expect(described_class.read_dimensions(path)).to eq({ width: 200, height: 100 })
      end
    end
  end

  describe '.inject' do
    it 'adds width and height to local asset images without dimensions' do
      html = '<p><img src="/docs/assets/img/empty-cc.png?abc123" alt="Example"></p>'
      output = described_class.inject(html, site)

      expect(output).to include('width="832"')
      expect(output).to include('height="1478"')
    end

    it 'leaves images that already define width untouched' do
      html = '<img src="/docs/assets/img/empty-cc.png" width="100" height="200" alt="Example">'
      output = described_class.inject(html, site)

      expect(output).not_to include('width="832"')
      expect(output).to include('width="100"')
    end

    it 'skips external images' do
      html = '<img src="https://example.com/assets/img/foo.png" alt="Example">'
      expect(described_class.inject(html, site)).to eq(html)
    end

    it 'skips SVG assets' do
      html = '<img src="/docs/assets/img/logo-braze-fa.svg" alt="Example">'
      expect(described_class.inject(html, site)).to eq(html)
    end
  end

  describe '.local_asset_path' do
    it 'strips baseurl and cache-busting query params' do
      path = described_class.local_asset_path('/docs/assets/img/empty-cc.png?deadbeef', site)
      expect(path).to eq('assets/img/empty-cc.png')
    end
  end
end
