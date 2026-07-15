# frozen_string_literal: true

require_relative "../../scripts/validate_doc_redirects"
require_relative "../../scripts/doc_anchor_links"

RSpec.describe "anchor drift detection in validate_doc_redirects.rb" do
  let(:link) do
    ->(source, target, anchor, kind: :md) do
      DocAnchorLinks::Link.new(source_file: source, kind: kind, raw_url: "n/a",
                                target_path: target, anchor: anchor)
    end
  end

  describe "#anchor_resolves?" do
    it "is true when the anchor is a real id on the target page" do
      heading_map = { "_docs/a.md" => { "all_ids" => ["foo"], "heading_ids" => ["foo"], "local_redirect_keys" => [] } }
      l = link.call("_docs/b.md", "_docs/a.md", "foo")

      expect(anchor_resolves?(heading_map, l)).to eq(true)
    end

    it "is true when the anchor is a local_redirect key, even with no matching id" do
      heading_map = { "_docs/a.md" => { "all_ids" => [], "heading_ids" => [], "local_redirect_keys" => ["rest-api-key"] } }
      l = link.call("_docs/b.md", "_docs/a.md", "rest-api-key")

      expect(anchor_resolves?(heading_map, l)).to eq(true)
    end

    it "is false when the target page has no matching id" do
      heading_map = { "_docs/a.md" => { "all_ids" => ["bar"], "heading_ids" => ["bar"], "local_redirect_keys" => [] } }
      l = link.call("_docs/b.md", "_docs/a.md", "foo")

      expect(anchor_resolves?(heading_map, l)).to eq(false)
    end

    it "is false when the target page does not exist in the heading map" do
      l = link.call("_docs/b.md", "_docs/missing.md", "foo")

      expect(anchor_resolves?({}, l)).to eq(false)
    end
  end

  describe "#required_anchor_fixes" do
    it "flags a heading-renamed link: resolved on base, broken on head" do
      heading_map_base = { "_docs/a.md" => { "all_ids" => ["old-name"], "heading_ids" => ["old-name"], "local_redirect_keys" => [] } }
      heading_map_head = { "_docs/a.md" => { "all_ids" => ["new-name"], "heading_ids" => ["new-name"], "local_redirect_keys" => [] } }
      l = link.call("_docs/b.md", "_docs/a.md", "old-name")

      newly_broken, = required_anchor_fixes(heading_map_base, heading_map_head, [l], [l])

      expect(newly_broken.length).to eq(1)
      expect(newly_broken.first[:category]).to eq(:heading_renamed)
    end

    it "flags a new-link-wrong-anchor: link did not exist on base at all" do
      heading_map_base = { "_docs/a.md" => { "all_ids" => ["foo"], "heading_ids" => ["foo"], "local_redirect_keys" => [] } }
      heading_map_head = { "_docs/a.md" => { "all_ids" => ["foo"], "heading_ids" => ["foo"], "local_redirect_keys" => [] } }
      l = link.call("_docs/b.md", "_docs/a.md", "typo-anchor")

      newly_broken, = required_anchor_fixes(heading_map_base, heading_map_head, [], [l])

      expect(newly_broken.length).to eq(1)
      expect(newly_broken.first[:category]).to eq(:new_link_wrong_anchor)
    end

    it "does not flag a link that was already broken on base (pre-existing debt)" do
      heading_map_base = { "_docs/a.md" => { "all_ids" => ["foo"], "heading_ids" => ["foo"], "local_redirect_keys" => [] } }
      heading_map_head = { "_docs/a.md" => { "all_ids" => ["foo"], "heading_ids" => ["foo"], "local_redirect_keys" => [] } }
      l = link.call("_docs/b.md", "_docs/a.md", "already-broken")

      newly_broken, = required_anchor_fixes(heading_map_base, heading_map_head, [l], [l])

      expect(newly_broken).to be_empty
    end

    it "does not flag a link that still resolves on head" do
      heading_map = { "_docs/a.md" => { "all_ids" => ["foo"], "heading_ids" => ["foo"], "local_redirect_keys" => [] } }
      l = link.call("_docs/b.md", "_docs/a.md", "foo")

      newly_broken, = required_anchor_fixes(heading_map, heading_map, [l], [l])

      expect(newly_broken).to be_empty
    end

    it "warns (non-blocking) when a resolving link's anchor matches the target's first heading" do
      heading_map = { "_docs/a.md" => { "all_ids" => ["page-title"], "heading_ids" => ["page-title", "second"], "local_redirect_keys" => [] } }
      l = link.call("_docs/b.md", "_docs/a.md", "page-title")

      newly_broken, warnings = required_anchor_fixes(heading_map, heading_map, [l], [l])

      expect(newly_broken).to be_empty
      expect(warnings.length).to eq(1)
      expect(warnings.first.anchor).to eq("page-title")
    end

    it "does not warn when a resolving link's anchor matches a non-first heading" do
      heading_map = { "_docs/a.md" => { "all_ids" => ["second"], "heading_ids" => ["page-title", "second"], "local_redirect_keys" => [] } }
      l = link.call("_docs/b.md", "_docs/a.md", "second")

      _, warnings = required_anchor_fixes(heading_map, heading_map, [l], [l])

      expect(warnings).to be_empty
    end
  end
end
