# frozen_string_literal: true

require 'fileutils'
require 'nokogiri'
require_relative 'tab_components_config'

module Tags
  module TabRendering
    def tab_type
      self.class::TAB_TYPE
    end

    def render_tabs_block(context, tabonly, inner)
      site = context.registers[:site]
      config = TabComponentsConfig.for(site, tab_type)['tabs']
      tabclass = TabComponentsConfig.toggle_class(config['toggle'], tabonly, :local)
      tabid = config['id_prefix'] + TabComponentsConfig.random_id

      tabs = inner.scan(Regexp.new(config['tab_scan_regex']))
      nav = config['nav']
      list_item = config['list_item']
      link = config['link']
      content = config['content']

      tabslist = '<ul role="' + nav['role'] + '" class="' + nav['classes'] + ' ' + tabclass + nav['ul_suffix'] + '" id="' + tabid + nav['id_suffix'] + '">' + "\n"
      if tabs.length > 0
        tabs.each_with_index do |tab, ind|
          itemid = TabComponentsConfig.random_id
          tabslug = TabComponentsConfig.slugify(tab[0])

          tab_aria_selected = ind == 0 ? 'true' : 'false'
          tab_tabindex      = ind == 0 ? '0'    : '-1'

          tabslist += '    <li role="' + list_item['role'] + '" id="' + list_item['id_prefix'] + itemid + '" class="' + list_item['row_class'] + ' ' + tabslug
          if ind == 0
            tabslist += ' ' + list_item['active_class']
          end
          tabslist += '"><a role="' + link['role'] + '" tabindex="' + tab_tabindex + '" aria-selected="' + tab_aria_selected + '" class="' + tabclass + '" ' + link['target_attr'] + '="' + tabid + '" ' + link['tab_attr'] + '="' + tabslug + '">' + tab[0] + '</a></li>' + "\n"
        end
      end
      tabslist += '</ul>'  + "\n"
      tabslist + '<div id="' + tabid + '" class="' + content['classes'] + ' ' + tabclass + content['div_suffix'] + '">' + "\n" + inner + "\n</div>\n"
    end

    def render_tab_block(context, raw_content)
      return "" if @tab.empty?

      site      = context.registers[:site]
      config    = TabComponentsConfig.for(site, tab_type)['tab']
      converter = site.find_converter_instance(Jekyll::Converters::Markdown)

      lines = raw_content.rstrip.split(/\r\n|\r|\n/).select { |line| line.size > 0 }
      indentation = lines.map do |line|
        match = line.match(/^(\s+)[^\s]+/)
        match ? match[1].size : 0
      end
      indentation = indentation.min
      contentid = TabComponentsConfig.random_id

      content = indentation ? raw_content.gsub(/^#{' |\t' * indentation}/, '') : raw_content
      content = converter.convert(content)
      content = content.strip # Strip again to avoid "\n"
      tabslug = TabComponentsConfig.slugify(@tab)

      if config['heading_id_prefix_suffix']
        content = content.gsub(/<(h[1-6]) id=\"/, '<\1 id="' + tabslug + config['heading_id_prefix_suffix'])
      end

      data_value = (config['data_value_prefix'] || '') + @tab
      '<div id="' + config['id_prefix'] + contentid + '" role="' + config['role'] + '" tabindex="' + config['tabindex'] + '" class="' + config['pane_class'] + ' ' + tabslug + config['pane_slug_suffix'] + '" ' + config['tab_attr'] + '="' + data_value + '">' + content + "</div>"
    end

    def render_subtabs_block(context, tabonly, inner)
      site = context.registers[:site]
      config = TabComponentsConfig.for(site, tab_type)['subtabs']
      tabclass = TabComponentsConfig.toggle_class(config['toggle'], tabonly, :global)
      tabid = config['id_prefix'] + TabComponentsConfig.random_id

      tabs = inner.scan(Regexp.new(config['tab_scan_regex']))
      nav = config['nav']
      list_item = config['list_item']
      link = config['link']
      content = config['content']

      tabslist = '<ul role="' + nav['role'] + '" class="' + nav['classes'] + ' ' + tabclass + nav['ul_suffix'] + '" id="' + tabid + nav['id_suffix'] + '">' + "\n"
      if tabs.length > 0
        tabs.each_with_index do |tab, ind|
          itemid = TabComponentsConfig.random_id
          tabslug = TabComponentsConfig.slugify(tab[0])

          tab_aria_selected = ind == 0 ? 'true' : 'false'
          tab_tabindex      = ind == 0 ? '0'    : '-1'

          tabslist += '    <li role="' + list_item['role'] + '" id="' + list_item['id_prefix'] + itemid + '" class="' + list_item['row_class'] + ' ' + tabslug + list_item['slug_suffix']
          if ind == 0
            tabslist += ' ' + list_item['active_class']
          end
          tabslist += '"><a role="' + link['role'] + '" tabindex="' + tab_tabindex + '" aria-selected="' + tab_aria_selected + '" class="' + tabclass + '" ' + link['target_attr'] + '="' + tabid + '" ' + link['tab_attr'] + '="' + tabslug + link['slug_suffix'] + '">' + tab[0] + '</a></li>' + "\n"
        end
      end
      tabslist += '</ul>'  + "\n"
      tabslist + '<div id="' + tabid + '" class="' + content['classes'] + ' ' + tabclass + content['div_suffix'] + '">' + "\n" + inner + "\n</div>\n"
    end

    def render_subtab_block(context, raw_content)
      return "" if @tab.empty?

      site      = context.registers[:site]
      config    = TabComponentsConfig.for(site, tab_type)['subtab']
      converter = site.find_converter_instance(Jekyll::Converters::Markdown)

      lines = raw_content.rstrip.split(/\r\n|\r|\n/).select { |line| line.size > 0 }
      indentation = lines.map do |line|
        match = line.match(/^(\s+)[^\s]+/)
        match ? match[1].size : 0
      end
      indentation = indentation.min
      contentid = TabComponentsConfig.random_id

      content = indentation ? raw_content.gsub(/^#{' |\t' * indentation}/, '') : raw_content
      content = converter.convert(content)
      content = content.strip # Strip again to avoid "\n"
      tabslug = TabComponentsConfig.slugify(@tab)

      '<div id="' + config['id_prefix'] + contentid + '" role="' + config['role'] + '" tabindex="' + config['tabindex'] + '" class="' + config['pane_class'] + ' ' + tabslug + config['pane_slug_suffix'] + '" ' + config['tab_attr'] + '="' + @tab + '">' + content + "</div>"
    end
  end

  class TabsBlock < Liquid::Block
    include TabRendering
    TAB_TYPE = 'generic'

    def initialize(tag_name, tabonly = 'false', tokens)
      super
      @tabonly = tabonly
    end

    def render(context)
      render_tabs_block(context, @tabonly, super)
    end
  end

  class TabBlock < Liquid::Block
    include TabRendering
    TAB_TYPE = 'generic'

    def initialize(tag_name, tab, tokens)
      super
      @tab = tab.strip.downcase
    end

    def render(context)
      render_tab_block(context, super)
    end
  end

  class SubTabsBlock < Liquid::Block
    include TabRendering
    TAB_TYPE = 'generic'

    def initialize(tag_name, tabonly = 'false', tokens)
      super
      @tabonly = tabonly
    end

    def render(context)
      render_subtabs_block(context, @tabonly, super)
    end
  end

  class SubTabBlock < Liquid::Block
    include TabRendering
    TAB_TYPE = 'generic'

    def initialize(tag_name, tab, tokens)
      super
      @tab = tab.strip.downcase
    end

    def render(context)
      render_subtab_block(context, super)
    end
  end

  class SdkTabsBlock < TabsBlock
    TAB_TYPE = 'sdk'
  end

  class SdkTabBlock < TabBlock
    TAB_TYPE = 'sdk'
  end

  class SdkSubTabsBlock < SubTabsBlock
    TAB_TYPE = 'sdk'
  end

  class SdkSubTabBlock < SubTabBlock
    TAB_TYPE = 'sdk'
  end
end

Liquid::Template.register_tag("tabs", Tags::TabsBlock)
Liquid::Template.register_tag("tab",  Tags::TabBlock)
Liquid::Template.register_tag("subtabs", Tags::SubTabsBlock)
Liquid::Template.register_tag("subtab",  Tags::SubTabBlock)
Liquid::Template.register_tag("sdktabs", Tags::SdkTabsBlock)
Liquid::Template.register_tag("sdktab",  Tags::SdkTabBlock)
Liquid::Template.register_tag("sdksubtabs", Tags::SdkSubTabsBlock)
Liquid::Template.register_tag("sdksubtab",  Tags::SdkSubTabBlock)

module CurrentsGlossaryLazyTabs
  SCRIPT_PLACEHOLDER_PREFIX = '@@@CURRENTS_GLOSSARY_SCRIPT'

  def self.config(site)
    TabComponentsConfig.for(site, 'glossary')['lazy'] || {}
  end

  def self.lazy_tab_pages(site)
    key = config(site)['page_front_matter_key'] || 'lazy_partner_tabs'
    site.collections.values.flat_map(&:docs).select { |doc| doc.data[key] }
  end

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
    lazy_config = config(site)
    i18n = site.data['i18n'] || {}
    locale = i18n[lang] || {}
    en = i18n['en'] || {}
    key = lazy_config['loading_text_i18n_key'] || 'glossary_currents_events_loading'
    locale[key] ||
      en[key] ||
      lazy_config['loading_text_default'] ||
      'Loading schema…'
  end

  def self.process_html!(html, site, dest, page_slug, baseurl, loading_label)
    lazy_config = config(site)
    pane_class = lazy_config['pane_class'] || 'ab-tab-pane'
    lazy_attr = lazy_config['lazy_attribute'] || 'data-currents-lazy'
    fragment_attr = lazy_config['fragment_attribute'] || 'data-currents-fragment'
    placeholder_class = lazy_config['placeholder_class'] || 'currents-lazy-tab-placeholder'
    fragments_dir = lazy_config['fragments_dir'] || 'currents_glossary_tab_fragments'

    return html unless html.include?(pane_class)
    return html if html.include?("#{lazy_attr}=\"true\"")

    masked_html, scripts = mask_scripts(html)
    doc = Nokogiri::HTML.parse(masked_html)
    fragment_dir = File.join(dest, fragments_dir, page_slug)
    FileUtils.mkdir_p(fragment_dir)

    baseurl = '' if baseurl == '/'

    doc.css(".#{pane_class.gsub(' ', '.')}").each do |pane|
      next if pane[lazy_attr] == 'true'

      pane_id = pane['id']
      next if pane_id.nil? || pane_id.empty?

      fragment_rel = File.join(fragments_dir, page_slug, "#{pane_id}.html")
      fragment_path = File.join(dest, fragment_rel)
      File.write(fragment_path, pane.inner_html, encoding: 'utf-8')

      fragment_url = "#{baseurl}/#{fragment_rel.tr('\\', '/')}"
      fragment_url = fragment_url.gsub(%r{//+}, '/')

      pane.inner_html = "<p class=\"#{placeholder_class}\">#{loading_label}</p>"
      pane[fragment_attr] = fragment_url
      pane[lazy_attr] = 'true'
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
      processed = process_html!(html, site, site.dest, page_slug, baseurl, loading_label)
      next if processed == html

      File.write(output_path, processed, encoding: 'utf-8')
    end
  end
end
