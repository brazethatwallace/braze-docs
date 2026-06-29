#!/usr/bin/env ruby
# frozen_string_literal: true

require 'fileutils'
require 'json'
require 'tmpdir'
require 'minitest/autorun'

repo_root = File.expand_path('../..', __dir__)
load File.join(repo_root, 'scripts/generate_sitemap_lastmodified.rb')

class GenerateSitemapLastmodifiedTest < Minitest::Test
  def repo_root
    @repo_root ||= File.expand_path('../..', __dir__)
  end

  def test_extract_paths_from_multi_lang_include_with_params
    content = <<~MD
      {% multi_lang_include analytics/metrics.md metric='Variation' %}
      {% multi_lang_include 'contributing/templates/basic.md' %}
    MD

    paths = IncludeReferenceParser.extract_paths(content)
    assert_includes paths, 'analytics/metrics.md'
    assert_includes paths, 'contributing/templates/basic.md'
  end

  def test_extract_paths_from_standard_include
    content = "{% include early_access_beta_alert.md feature='This endpoint' %}"
    paths = IncludeReferenceParser.extract_paths(content)
    assert_equal ['early_access_beta_alert.md'], paths
  end

  def test_resolve_en_include
    resolved = IncludePathResolver.resolve('alerts/note_alerts.md', 'en', self.repo_root)
    assert_equal '_includes/alerts/note_alerts.md', resolved
    assert File.file?(File.join(repo_root, resolved))
  end

  def test_resolve_de_prefers_locale_include
    skip 'No German overlay include in repo' unless Dir.exist?(File.join(self.repo_root, '_lang/de/_includes'))

    resolved = IncludePathResolver.resolve('developer_guide/android/in_app_messages/customization.md', 'de', self.repo_root)
    if File.file?(File.join(self.repo_root, '_lang/de/_includes/developer_guide/android/in_app_messages/customization.md'))
      assert resolved.start_with?('_lang/de/_includes/')
    end
  end

  def test_transitive_includes_and_reverse_index
    Dir.mktmpdir do |tmpdir|
      FileUtils.mkdir_p(File.join(tmpdir, '_docs/_user_guide'))
      FileUtils.mkdir_p(File.join(tmpdir, '_includes/nested'))
      File.write(File.join(tmpdir, '_includes/leaf.md'), 'Leaf content.')
      File.write(File.join(tmpdir, '_includes/nested/mid.md'), "{% multi_lang_include leaf.md %}")
      File.write(
        File.join(tmpdir, '_docs/_user_guide/article.md'),
        "{% multi_lang_include nested/mid.md %}"
      )

      graph = IncludeDependencyGraph.new(content_root: '_docs', locale: 'en', repo_root: tmpdir)
      graph.register_article('_user_guide/article.md')

      includes = graph.transitive_includes('_user_guide/article.md')
      assert_includes includes, '_includes/nested/mid.md'
      assert_includes includes, '_includes/leaf.md'

      affected = graph.articles_affected_by_includes(['_includes/leaf.md'], ['_user_guide/article.md'])
      assert_equal ['_user_guide/article.md'], affected.sort
    end
  end

  def test_max_timestamp_picks_latest
    older = '2024-01-01T00:00:00+00:00'
    newer = '2025-06-01T12:00:00+00:00'
    assert_equal newer, max_timestamp(older, newer)
  end

  def test_monotonic_lastmod_keeps_existing_when_computed_is_older
    computed = '2025-08-22T20:07:24+00:00'
    existing = '2026-04-07T16:30:38+00:00'
    assert_equal existing, monotonic_lastmod(computed, existing)
  end

  def test_monotonic_lastmod_uses_computed_when_newer
    computed = '2026-05-01T10:00:00+00:00'
    existing = '2026-04-07T16:30:38+00:00'
    assert_equal computed, monotonic_lastmod(computed, existing)
  end

  def test_monotonic_lastmod_without_existing_returns_computed
    computed = '2025-08-22T20:07:24+00:00'
    assert_equal computed, monotonic_lastmod(computed, nil)
    assert_equal computed, monotonic_lastmod(computed, '')
  end
end
