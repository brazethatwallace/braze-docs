# frozen_string_literal: true

require_relative "../../scripts/doc_anchor_links"

RSpec.describe DocAnchorLinks do
  describe ".extract" do
    it "extracts a cross-file markdown link with an anchor" do
      content = "See [rate limits]({{site.baseurl}}/api/basics#rest-api-key-permissions)."
      links = described_class.extract("_docs/_api/api_limits.md", content)

      expect(links.length).to eq(1)
      expect(links.first.target_path).to eq("_docs/_api/basics.md")
      expect(links.first.anchor).to eq("rest-api-key-permissions")
      expect(links.first.kind).to eq(:md)
    end

    it "extracts a same-page markdown anchor link" do
      content = "See [the section above](#about-rate-limiting) for details."
      links = described_class.extract("_docs/_api/basics.md", content)

      expect(links.length).to eq(1)
      expect(links.first.target_path).to eq("_docs/_api/basics.md")
      expect(links.first.anchor).to eq("about-rate-limiting")
    end

    it "extracts an HTML <a href> link with an absolute /docs/ prefix" do
      content = %(<a href='/docs/api/basics#rest-api-key-permissions'>API key</a>)
      links = described_class.extract("_docs/_api/api_limits.md", content)

      expect(links.length).to eq(1)
      expect(links.first.target_path).to eq("_docs/_api/basics.md")
      expect(links.first.anchor).to eq("rest-api-key-permissions")
      expect(links.first.kind).to eq(:html)
    end

    it "resolves a single-segment path to a top-level doc" do
      content = "[archival]({{site.baseurl}}/user_archival#active-users)"
      links = described_class.extract("_docs/_api/data_retention.md", content)

      expect(links.first.target_path).to eq("_docs/user_archival.md")
    end

    it "ignores links with no anchor" do
      content = "[basics]({{site.baseurl}}/api/basics)"
      expect(described_class.extract("_docs/_api/x.md", content)).to eq([])
    end

    it "ignores links whose last path segment looks like a file (has an extension)" do
      content = "[manual link](/assets/manual.pdf#page=2)"
      expect(described_class.extract("_docs/_api/x.md", content)).to eq([])
    end

    it "ignores image links" do
      content = "![alt]({{site.baseurl}}/api/basics#rest-api-key-permissions)"
      expect(described_class.extract("_docs/_api/x.md", content)).to eq([])
    end

    it "ignores image reference-style links" do
      content = <<~MD
        ![alt][img-ref]

        [img-ref]: {{site.baseurl}}/api/basics#rest-api-key-permissions
      MD
      expect(described_class.extract("_docs/_api/x.md", content)).to eq([])
    end

    it "ignores external links" do
      content = "[external](https://example.com/page#section)"
      expect(described_class.extract("_docs/_api/x.md", content)).to eq([])
    end

    it "extracts reference-style links" do
      content = <<~MD
        See [rate limits][limits-ref].

        [limits-ref]: {{site.baseurl}}/api/basics#rest-api-key-permissions
      MD
      links = described_class.extract("_docs/_api/x.md", content)

      expect(links.length).to eq(1)
      expect(links.first.target_path).to eq("_docs/_api/basics.md")
      expect(links.first.anchor).to eq("rest-api-key-permissions")
    end

    it "strips query strings before extracting the anchor" do
      content = "[link]({{site.baseurl}}/api/basics?tab=x#rest-api-key-permissions)"
      links = described_class.extract("_docs/_api/x.md", content)

      expect(links.first.anchor).to eq("rest-api-key-permissions")
    end

    it "does not scan inside fenced code blocks" do
      content = <<~MD
        ```
        [not a real link]({{site.baseurl}}/api/basics#rest-api-key-permissions)
        ```
      MD
      expect(described_class.extract("_docs/_api/x.md", content)).to eq([])
    end

    it "does not extract a link shown as a literal example inside inline code" do
      content = "Use the syntax `[text](url#anchor)` to link to a section."
      expect(described_class.extract("_docs/_api/x.md", content)).to eq([])
    end

    it "ignores a bare-# anchor link that resolves to the site root, rather than treating it as same-page" do
      content = "[home](/docs/#some-anchor)"
      expect(described_class.extract("_docs/_api/x.md", content)).to eq([])
    end

    it "still treats a truly bare #anchor (no path at all) as same-page" do
      content = "See [the section above](#about-rate-limiting)."
      links = described_class.extract("_docs/_api/basics.md", content)

      expect(links.length).to eq(1)
      expect(links.first.target_path).to eq("_docs/_api/basics.md")
    end
  end
end
