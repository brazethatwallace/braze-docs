# frozen_string_literal: true

require 'fileutils'
require 'nokogiri'

# Offloads all Currents glossary tab panes (including Cloud Storage) to static
# fragment files so the main glossary HTML stays small and loads fast.
# Enable per page with front matter: lazy_partner_tabs: true
module CurrentsGlossaryLazyTabs
  FRAGMENTS_DIR = 'currents_glossary_tab_fragments'
  SCRIPT_PLACEHOLDER_PREFIX = '@@@CURRENTS_GLOSSARY_SCRIPT'

  def self.lazy_tab_pages(site)
    site.collections.values.flat_map(&:docs).select { |doc| doc.data['lazy_partner_tabs'] }
  end

  # Replace inline <script> blocks with placeholders so Nokogiri does not treat
  # literal "</script>" sequences inside JavaScript as closing the element.
  def self.mask_scripts(html)
    placeholders = []
    out = html.dup
    i = 0
    while (start = out.index(/<script\b/i, i))
      tag_end = out.index('>', start)
      break unless tag_end

      body_start = tag_end + 1
      close = out.index(/<\/script>/i, body_start)
      break unless close

      placeholders << out[start...(close + 9)]
      placeholder = "#{SCRIPT_PLACEHOLDER_PREFIX}#{placeholders.length - 1}@@@"
      out[start...(close + 9)] = placeholder
      i = start + placeholder.length
    end
    [out, placeholders]
  end

  def self.unmask_scripts(html, placeholders)
    placeholders.each_with_index do |script, index|
      html.sub!("#{SCRIPT_PLACEHOLDER_PREFIX}#{index}@@@", script)
    end
    html
  end

  def self.loading_text(site, lang)
    i18n = site.data['i18n'] || {}
    locale = i18n[lang] || {}
    en = i18n['en'] || {}
    locale['glossary_currents_events_loading'] ||
      en['glossary_currents_events_loading'] ||
      'Loading schema\u2026'
  end

  def self.process_html!(html, dest, page_slug, baseurl, loading_label)
    return html unless html.include?('ab-tab-pane')
    return html if html.include?('data-currents-lazy="true"')

    masked_html, scripts = mask_scripts(html)
    doc = Nokogiri::HTML.parse(masked_html)
    fragment_dir = File.join(dest, FRAGMENTS_DIR, page_slug)
    FileUtils.mkdir_p(fragment_dir)

    baseurl = '' if baseurl == '/'

    doc.css('.ab-tab-pane').each do |pane|
      next if pane['data-currents-lazy'] == 'true'

      pane_id = pane['id']
      next if pane_id.nil? || pane_id.empty?

      fragment_rel = File.join(FRAGMENTS_DIR, page_slug, "#{pane_id}.html")
      fragment_path = File.join(dest, fragment_rel)
      File.write(fragment_path, pane.inner_html, encoding: 'utf-8')

      fragment_url = "#{baseurl}/#{fragment_rel.tr('\\', '/')}"
      fragment_url = fragment_url.gsub(%r{//+}, '/')

      pane.inner_html = "<p class=\"currents-lazy-tab-placeholder\">#{loading_label}</p>"
      pane['data-currents-fragment'] = fragment_url
      pane['data-currents-lazy'] = 'true'
    end

    unmask_scripts(doc.to_html, scripts)
  end

  Jekyll::Hooks.register :site, :post_write do |site|
    baseurl = site.baseurl.to_s

    lazy_tab_pages(site).each do |item|
      output_path = item.destination(site.dest)
      next unless File.exist?(output_path)

      lang = item.data['lang'] || site.config['language'] || 'en'
      loading_label = loading_text(site, lang)
      page_slug = item.data['slug'] || File.basename(item.url.to_s.chomp('/'))
      html = File.read(output_path, encoding: 'utf-8')
      processed = process_html!(html, site.dest, page_slug, baseurl, loading_label)
      next if processed == html

      File.write(output_path, processed, encoding: 'utf-8')
    end
  end
end
