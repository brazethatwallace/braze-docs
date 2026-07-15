# spec/scripts/heading_id_extractor_spec.rb
# frozen_string_literal: true

require_relative "../../scripts/heading_id_extractor"

RSpec.describe HeadingIdExtractor do
  describe ".all_ids" do
    it "extracts every element id in the rendered HTML" do
      html = <<~HTML
        <h2 id="about-rate-limiting">About rate limiting</h2>
        <div class="reset-td-br-1" id="filter_soft-bounced"></div>
        <p>no id here</p>
      HTML

      expect(described_class.all_ids(html)).to contain_exactly(
        "about-rate-limiting", "filter_soft-bounced"
      )
    end

    it "dedupes repeated ids" do
      html = %(<h2 id="dup">A</h2><span id="dup"></span>)
      expect(described_class.all_ids(html)).to eq(["dup"])
    end

    it "returns an empty array for html with no ids" do
      expect(described_class.all_ids("<p>hello</p>")).to eq([])
    end

    it "does not match id-looking text that isn't inside a real tag (e.g. an escaped code sample)" do
      html = %(<p>Example: &lt;div id="my-example"&gt;&lt;/div&gt;</p>)
      expect(described_class.all_ids(html)).to eq([])
    end

    it "matches ids on any real element, not just headings" do
      html = %(<a id="jump-target" href="#">Link</a>)
      expect(described_class.all_ids(html)).to eq(["jump-target"])
    end
  end

  describe ".heading_ids" do
    it "extracts only h1-h6 ids, in document order" do
      html = <<~HTML
        <h1 id="page-title">Page title</h1>
        <div id="not-a-heading"></div>
        <h2 id="second-section">Second section</h2>
      HTML

      expect(described_class.heading_ids(html)).to eq(["page-title", "second-section"])
    end

    it "returns an empty array when there are no headings" do
      expect(described_class.heading_ids("<p>no headings</p>")).to eq([])
    end
  end

  describe ".local_redirect_keys" do
    it "extracts keys from a Hash-shaped local_redirect (messaging.md style)" do
      value = {
        "app-group-rest-api-key" => "/docs/api/basics/#rest-api-key",
        "app-identifier" => "/docs/api/identifier_types/"
      }
      expect(described_class.local_redirect_keys(value)).to contain_exactly(
        "app-group-rest-api-key", "app-identifier"
      )
    end

    it "extracts keys from an Array-of-single-key-Hashes local_redirect (customize.md style)" do
      value = [
        { "style-settings" => "/docs/user_guide/.../customize/#style-settings" },
        { "style_settings" => "/docs/user_guide/.../customize/style_settings" }
      ]
      expect(described_class.local_redirect_keys(value)).to contain_exactly(
        "style-settings", "style_settings"
      )
    end

    it "returns an empty array when there is no local_redirect" do
      expect(described_class.local_redirect_keys(nil)).to eq([])
    end

    it "ignores non-Hash entries in an Array-shaped local_redirect" do
      value = ["not-a-hash", { "key" => "value" }]
      expect(described_class.local_redirect_keys(value)).to eq(["key"])
    end
  end
end
