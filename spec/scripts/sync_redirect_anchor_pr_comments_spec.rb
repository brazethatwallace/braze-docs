# frozen_string_literal: true

# Lightweight checks for the escape helpers used in PR comment bodies.
# Full sync path needs github-script; these cover the hardening surface.

require "json"
require "open3"

RSpec.describe "sync_redirect_anchor_pr_comments escape helpers" do
  let(:helpers) do
    script = <<~JS
      const { htmlEscape, mdEscape, code, text } = require('./scripts/sync_redirect_anchor_pr_comments.js')._test;
      const cases = {
        html: htmlEscape('a<b>&"c'),
        md: mdEscape('[x](evil)'),
        code: code('rest-api-key<script>'),
        text: text('Foo_Bar'),
        newline: code("line1\\nline2")
      };
      process.stdout.write(JSON.stringify(cases));
    JS
    out, err, st = Open3.capture3("node", "-e", script, chdir: File.expand_path("../..", __dir__))
    raise "node helper probe failed: #{err}" unless st.success?

    JSON.parse(out)
  end

  it "HTML-escapes angle brackets, ampersands, and quotes" do
    expect(helpers["html"]).to eq("a&lt;b&gt;&amp;&quot;c")
  end

  it "backslash-escapes markdown-significant punctuation" do
    expect(helpers["md"]).to eq('\\[x\\]\\(evil\\)')
  end

  it "wraps identifiers in <code> with both HTML and markdown escaping" do
    expect(helpers["code"]).to include("<code>")
    expect(helpers["code"]).to include("&lt;")
    expect(helpers["code"]).not_to include("<script>")
  end

  it "flattens embedded newlines before wrapping" do
    expect(helpers["newline"]).not_to include("\n")
    expect(helpers["newline"]).to include("line1 line2")
  end

  it "escapes prose for markdown emphasis characters" do
    expect(helpers["text"]).to eq("Foo\\_Bar")
  end
end
