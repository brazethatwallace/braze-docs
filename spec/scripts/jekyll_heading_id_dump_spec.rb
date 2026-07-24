# frozen_string_literal: true

require_relative "../../scripts/jekyll_heading_id_dump"

RSpec.describe "JekyllHeadingIdDump.readable_title" do
  it "prefers nav_title when present" do
    title = JekyllHeadingIdDump.readable_title(
      "_docs/_api/endpoints/apps/post_update_push_credential.md",
      nav_title: "Update push credential",
      article_title: "Update Push Credential Endpoint"
    )
    expect(title).to eq("Update push credential")
  end

  it "falls back to article_title when nav_title is missing" do
    title = JekyllHeadingIdDump.readable_title(
      "_docs/_api/basics.md",
      nav_title: nil,
      article_title: "API Basics"
    )
    expect(title).to eq("API Basics")
  end

  it "falls back to article_title when nav_title is blank" do
    title = JekyllHeadingIdDump.readable_title(
      "_docs/_api/basics.md",
      nav_title: "  ",
      article_title: "API Basics"
    )
    expect(title).to eq("API Basics")
  end

  it "derives a title from the file path when neither frontmatter field is present" do
    title = JekyllHeadingIdDump.readable_title("_includes/rate_limits.md")
    expect(title).to eq("Rate Limits")
  end
end
