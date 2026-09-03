# frozen_string_literal: true

require_relative 'urlnavmenu_tree_builder'
require_relative 'urlnavmenu_html_renderer'

# Custom Navigation Plugin based on initial code structure from https://github.com/govdelivery/jekyll-nested-menu-generator
# Updated to allow for dynamic navigation via the URL string
# ie from /documents/documentation/iOS/Integration/SDK
# and /documents/documentation/iOS/Analytics/Report
# Generates collapsible navigation using bootstrap 4.1
# documents -
#   documentation -
#     iOS +
#       Integration +
#         SDK
#       Analytics +
#         Report
# Usage {% UrlNavMenu {{page.collection}} %}
#

module Jekyll
  class UrlNavMenu < Liquid::Tag
    UNIQUE_POSTFIX = '_nav_page'

    def initialize(tag_name, menu_root, tokens)
      @menu_root = menu_root.strip
      super
    end

    def render(context)
      site = context.registers[:site]
      baseurl = site.baseurl
      nav_expand_list = site.config['nav_expand_list']

      language = site.config['language'] || 'en'
      i18n = site.data['i18n'] || {}
      locale = i18n[language] || {}
      expand_section_label = locale['expand_section'] || 'Expand section'
      collapse_section_label = locale['collapse_section'] || 'Collapse section'

      params = Liquid::Template.parse(@menu_root).render(context).split('|')
      minlevel = params[0].to_i
      collection = params[1]
      currentpage = context.registers[:page]
      currentpage_id = currentpage.respond_to?(:id) ? currentpage.id : nil
      Jekyll.logger.debug("Current Page: #{currentpage_id}") if currentpage_id

      site_data_key = collection + UNIQUE_POSTFIX

      unless context['site']['data'].include?(site_data_key)
        menu_hash = UrlNavMenuTreeBuilder.build(context['site']['documents'], collection)
        context['site']['data'][site_data_key] = menu_hash
      end

      renderer = UrlNavMenuHtmlRenderer.new(
        baseurl: baseurl,
        nav_expand_list: nav_expand_list,
        minlevel: minlevel,
        currentpage: currentpage,
        currentpage_id: currentpage_id,
        expand_section_label: expand_section_label,
        collapse_section_label: collapse_section_label
      )

      renderer.render(context['site']['data'][site_data_key], '', 0, true)
    end
  end
end

Liquid::Template.register_tag('UrlNavMenu', Jekyll::UrlNavMenu)
