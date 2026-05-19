# frozen_string_literal: true

require 'fileutils'
require 'nokogiri'

# Offloads non–Cloud Storage Currents glossary tab panes to static fragment
# files so the main glossary HTML stays under agent/crawler size limits.
# Enable per page with front matter: lazy_partner_tabs: true
module CurrentsGlossaryLazyTabs
  KEEP_TAB_CLASS = 'cloudstorage_tab'
  FRAGMENTS_DIR = 'currents_glossary_tab_fragments'

  def self.lazy_tab_pages(site)
    site.collections.values.flat_map(&:docs).select { |doc| doc.data['lazy_partner_tabs'] }
  end

  def self.process_html!(html, dest, page_slug, baseurl)
    return html unless html.include?('ab-tab-pane')
    return html if html.include?('data-currents-lazy="true"')

    doc = Nokogiri::HTML.parse(html)
    fragment_dir = File.join(dest, FRAGMENTS_DIR, page_slug)
    FileUtils.mkdir_p(fragment_dir)

    baseurl = '' if baseurl == '/'

    doc.css('.ab-tab-pane').each do |pane|
      next if pane['class'].to_s.include?(KEEP_TAB_CLASS)
      next if pane['data-currents-lazy'] == 'true'

      pane_id = pane['id']
      next if pane_id.nil? || pane_id.empty?

      fragment_rel = File.join(FRAGMENTS_DIR, page_slug, "#{pane_id}.html")
      fragment_path = File.join(dest, fragment_rel)
      File.write(fragment_path, pane.inner_html)

      fragment_url = "#{baseurl}/#{fragment_rel.tr('\\', '/')}"
      fragment_url = fragment_url.gsub(%r{//+}, '/')

      pane.inner_html = '<p class="currents-lazy-tab-placeholder">Loading schema…</p>'
      pane['data-currents-fragment'] = fragment_url
      pane['data-currents-lazy'] = 'true'
    end

    doc.to_html
  end

  Jekyll::Hooks.register :site, :post_write do |site|
    baseurl = site.baseurl.to_s

    lazy_tab_pages(site).each do |item|
      output_path = item.destination(site.dest)
      next unless File.exist?(output_path)

      page_slug = item.data['slug'] || File.basename(item.url.to_s.chomp('/'))
      html = File.read(output_path)
      processed = process_html!(html, site.dest, page_slug, baseurl)
      next if processed == html

      File.write(output_path, processed)
    end
  end
end
