require 'cgi'
require_relative 'urlnavmenu_tree_builder'

module Jekyll
  # Renders a UrlNavMenuTreeBuilder menu hash as Bootstrap navigation HTML.
  class UrlNavMenuHtmlRenderer
    NAV_ITEM_CLASS = 'nav-item'
    NAV_ITEM_LINK_CLASS = 'nav_link'
    NAV_PREFIX = 'nav'
    NAV_ACTIVE_PAGE_CLASS = 'nav_url'
    NAV_ACTIVE_BASIC_CLASS = 'nav_reg'
    NAV_TITLE_CLASS = 'nav_title'
    NAV_TITLE_BLOCK = 'nav_block'
    FA_CLASS = 'fas'
    ACTIVE_CLASS = ' active'
    ACTIVE_PARENT_CLASS = ' active_parent'

    MENU_SORTED_LIST = :menu_sorted_list

    NAV_TOGGLE_CLASS = 'nav_toggle'

    MENU_NAV_LIST = UrlNavMenuTreeBuilder::MENU_NAV_LIST
    MENU_NAV_PAGES = UrlNavMenuTreeBuilder::MENU_NAV_PAGES
    PAGE_KEY_INDEX = UrlNavMenuTreeBuilder::PAGE_KEY_INDEX
    PAGE_TITLE_INDEX = UrlNavMenuTreeBuilder::PAGE_TITLE_INDEX
    PAGE_WEIGHT_INDEX = UrlNavMenuTreeBuilder::PAGE_WEIGHT_INDEX
    PAGE_ID_INDEX = UrlNavMenuTreeBuilder::PAGE_ID_INDEX
    PAGE_URL_INDEX = UrlNavMenuTreeBuilder::PAGE_URL_INDEX

    def initialize(baseurl:, nav_expand_list:, minlevel:, currentpage:, currentpage_id:,
                   expand_section_label:, collapse_section_label:)
      @baseurl = baseurl
      @nav_expand_list = nav_expand_list
      @minlevel = minlevel
      @currentpage = currentpage
      @currentpage_id = currentpage_id
      @expand_section_label = expand_section_label
      @collapse_section_label = collapse_section_label
      @rail_slot_used = false
    end

    def render(menu_hash, parent_key = '', level = 0, root_nav = false)
      @rail_slot_used = false if root_nav && level.zero?
      build_menu_html(menu_hash, parent_key, level, root_nav)
    end

    private

    def build_menu_html(menu_hash, parent_key, level, root_nav = false)
      resultstr = ''
      unless menu_hash.nil?
        unless menu_hash[MENU_NAV_LIST].nil?
          if menu_hash[MENU_SORTED_LIST].nil?
            menu_hash[MENU_SORTED_LIST] = []

            menu_hash[MENU_NAV_LIST].each do |_k, v|
              menu_hash[MENU_SORTED_LIST].push(v)
            end

            menu_hash[MENU_SORTED_LIST].sort_by! do |e|
              weight = e[PAGE_WEIGHT_INDEX]
              [
                weight.nil? ? 1 : 0,
                weight.nil? ? 0 : weight,
                e[PAGE_TITLE_INDEX].to_s.downcase
              ]
            end
          end

          items = ''
          results = ''
          navclass = ''
          ariaexpanded = false
          navclass = ' show' if level < @minlevel

          nextlevel = level + 1

          menu_hash[MENU_SORTED_LIST].each do |ma|
            page_key = ''
            curclass = ''
            curinfo = nil
            item = nil
            is_currentpage = false
            is_active = false

            unless menu_hash[MENU_NAV_LIST].nil?
              page_title = ma[PAGE_TITLE_INDEX]
              page_title_escaped = CGI.escapeHTML(page_title.to_s)

              unless ma[PAGE_KEY_INDEX].nil?
                page_key = ma[PAGE_KEY_INDEX].to_s.gsub(/[^0-9a-z]/i, '')
              end

              unless menu_hash[MENU_NAV_PAGES].nil?
                if menu_hash[MENU_NAV_PAGES][ma[PAGE_KEY_INDEX]].is_a?(Jekyll::Document)
                  curinfo = menu_hash[MENU_NAV_PAGES][ma[PAGE_KEY_INDEX]]
                  is_currentpage = true if @currentpage_id && @currentpage_id == ma[PAGE_ID_INDEX]
                end
              end

              parent_page_key = page_key
              unless parent_key.empty?
                parent_page_key = parent_key + '_' + page_key
              else
                parent_key = 'top'
              end

              item = if @nav_expand_list.include?(ma[PAGE_ID_INDEX]) || is_currentpage
                       build_menu_html(menu_hash[ma[PAGE_KEY_INDEX]], parent_page_key, (@minlevel - 1), false)
                     else
                       build_menu_html(menu_hash[ma[PAGE_KEY_INDEX]], parent_page_key, nextlevel, false)
                     end

              ariaexpanded = false
              ariaexpanded = true if level < (@minlevel - 1)

              unless ma[PAGE_URL_INDEX].nil?
                if @currentpage.url.start_with?(ma[PAGE_URL_INDEX])
                  navclass = ' show'
                  ariaexpanded = true
                  curclass << " #{ACTIVE_PARENT_CLASS} "
                end
                if level >= (@minlevel - 1) && @currentpage.url == ma[PAGE_URL_INDEX]
                  ariaexpanded = false
                end
              end

              ariaexpanded = true if @nav_expand_list.include?(ma[PAGE_ID_INDEX]) || is_currentpage

              unless curinfo.nil?
                if is_currentpage
                  curclass << " #{ACTIVE_CLASS} "
                  is_active = true
                end

                cur_url = @baseurl + curinfo.url
                if curinfo['redirect_to'] && level.zero?
                  cur_url = curinfo['redirect_to'].gsub!(%r{^/docs/}, "#{@baseurl}/")
                end

                apply_rail_layout = (root_nav && level.zero? && !@rail_slot_used)
                nav_item_classes = [NAV_ITEM_CLASS, curclass.strip]
                nav_item_classes << 'nav-item--rail' if apply_rail_layout
                items << "<div class='#{nav_item_classes.reject(&:empty?).join(' ')}' id='parent_#{NAV_PREFIX}_#{parent_page_key}' data-parent='parent_#{NAV_PREFIX}_#{parent_key}'>"
                items << "<div class='nav-item--rail__main'>" if apply_rail_layout

                if item.empty?
                  items << "<div class='#{NAV_ACTIVE_BASIC_CLASS}' data-parent='parent_#{NAV_PREFIX}_#{parent_key}'>"
                  if is_active
                    items << "<span class='#{NAV_TITLE_CLASS}' aria-current='page'>#{page_title_escaped}</span>"
                  else
                    items << "<a href='#{cur_url}' class='#{NAV_ITEM_LINK_CLASS}' data-parent='parent_#{NAV_PREFIX}_#{parent_key}' aria-label='#{page_title_escaped}'>#{page_title_escaped}</a>"
                  end
                  items << "</div>\n"
                else
                  items << "<div class='#{NAV_ACTIVE_PAGE_CLASS} nav_item_row'  data-parent='parent_#{NAV_PREFIX}_#{parent_key}'>"
                  if is_active
                    items << "<span class='#{NAV_TITLE_CLASS}' aria-current='page'>#{page_title_escaped}</span>"
                  else
                    items << "<a href='#{cur_url}' class='#{NAV_ITEM_LINK_CLASS}' data-parent='parent_#{NAV_PREFIX}_#{parent_key}' aria-label='#{page_title_escaped}'>#{page_title_escaped}</a>"
                  end
                  expand_label = CGI.escapeHTML("#{@expand_section_label}: #{page_title}")
                  collapse_label = CGI.escapeHTML("#{@collapse_section_label}: #{page_title}")
                  items << "<button type='button' class='#{NAV_TOGGLE_CLASS}' data-toggle='collapse' data-target='##{NAV_PREFIX}_#{parent_page_key}' aria-expanded='#{ariaexpanded}' data-parent='parent_#{NAV_PREFIX}_#{parent_key}' aria-label='#{ariaexpanded ? collapse_label : expand_label}' data-expand-label='#{expand_label}' data-collapse-label='#{collapse_label}'><i class='#{FA_CLASS} fa-chevron-#{ariaexpanded ? 'down' : 'right'}' aria-hidden='true'></i></button>"
                  items << "</div>\n"
                end

                if apply_rail_layout
                  items << "</div>\n"
                  items << "<div class='nav-item--rail__toggle' id='sidebar_toggle_host'></div>\n"
                  @rail_slot_used = true
                end
                items << "</div>\n"
              else
                items << "<div class='#{NAV_ITEM_CLASS}  #{curclass}' id='parent_#{NAV_PREFIX}_#{parent_page_key}' data-parent='parent_#{NAV_PREFIX}_#{parent_key}'> "

                if item.empty?
                  items << " <div class='#{NAV_TITLE_BLOCK}'  data-parent='parent_#{NAV_PREFIX}_#{parent_key}'><div class='#{NAV_ACTIVE_BASIC_CLASS} #{NAV_TITLE_CLASS}'>"
                  items << page_title_escaped.to_s
                  items << "</div></div></div>\n"
                else
                  expand_label = CGI.escapeHTML("#{@expand_section_label}: #{page_title}")
                  collapse_label = CGI.escapeHTML("#{@collapse_section_label}: #{page_title}")
                  items << "<div class='#{NAV_ACTIVE_PAGE_CLASS} nav_item_row'  data-parent='parent_#{NAV_PREFIX}_#{parent_key}'><button type='button' class='#{NAV_TITLE_CLASS}' data-toggle='collapse' data-target='##{NAV_PREFIX}_#{parent_page_key}' aria-expanded='#{ariaexpanded}' aria-label='#{ariaexpanded ? collapse_label : expand_label}' data-expand-label='#{expand_label}' data-collapse-label='#{collapse_label}'>#{page_title_escaped}</button><button type='button' class='#{NAV_TOGGLE_CLASS}' data-toggle='collapse' data-target='##{NAV_PREFIX}_#{parent_page_key}' aria-expanded='#{ariaexpanded}' data-parent='parent_#{NAV_PREFIX}_#{parent_key}' aria-label='#{ariaexpanded ? collapse_label : expand_label}' data-expand-label='#{expand_label}' data-collapse-label='#{collapse_label}'><i class='#{FA_CLASS} fa-chevron-#{ariaexpanded ? 'down' : 'right'}' aria-hidden='true'></i></button></div>"
                  items << "</div>\n"
                end
              end

              items << item unless item.empty?
            end
          end

          unless items.empty?
            results = "<div class='nav flex-column flex-nowrap "
            results << 'collapse ' unless ariaexpanded
            results << "#{navclass}' id='#{NAV_PREFIX}_#{parent_key}'  >\n"
            results << items
            results << '</div>'
          end
          resultstr << results
        end
      end
      resultstr
    end
  end
end
