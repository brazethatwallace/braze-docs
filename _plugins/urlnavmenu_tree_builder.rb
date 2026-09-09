# frozen_string_literal: true

module Jekyll
  # Builds the nested navigation tree from Jekyll documents. Pure data transform — no HTML.
  class UrlNavMenuTreeBuilder
    MENU_NAV_LIST = :menu_nav_list
    MENU_NAV_PAGES = :menu_nav_pages

    PAGE_WEIGHT = 'page_order'
    PAGE_HIDDEN = 'hidden'
    PAGE_NAV_TITLE = 'nav_title'
    PAGE_CONFIG_ONLY = 'config_only'

    PAGE_KEY_INDEX = 0
    PAGE_PG_INDEX = 1
    PAGE_TITLE_INDEX = 2
    PAGE_WEIGHT_INDEX = 3
    PAGE_ID_INDEX = 4
    PAGE_URL_INDEX = 5

    def self.build(documents, collection)
      menu_hash = {}
      root_string = "/#{collection}"

      documents.find_all { |page| page.url.start_with?(root_string) }.each do |page|
        next if page.data[PAGE_HIDDEN] == true

        path_parts = page.url.split('/')
        next unless path_parts.shift

        path_url = '/'
        next unless path_url += path_parts.shift

        path_url += '/'

        cnt = 0
        max_len = path_parts.length
        cur_hash = menu_hash
        page_weight = page.data[PAGE_WEIGHT] || nil

        while cnt <= max_len
          path_part = path_parts.shift
          if path_part
            path_key = path_part.downcase
            path_url += path_part + '/'

            if path_parts.length > 0
              cur_hash[path_key] ||= {}
              cur_hash[MENU_NAV_LIST] ||= {}

              if cur_hash[MENU_NAV_LIST][path_key].nil?
                page_title = decode_title(path_part.to_s)
                cur_hash[MENU_NAV_LIST][path_key] = [path_key, path_part, page_title, nil, path_url, path_url]
              end
              cur_hash = cur_hash[path_key]
            else
              page_title = page.data[PAGE_NAV_TITLE] || page.data['title']
              page_title = decode_title(page_title.to_s)

              cur_hash[MENU_NAV_LIST] ||= {}
              nav_page_url = page.url
              nav_page_url = page.data['custom_url'] unless page.data['custom_url'].nil?

              page_id = ''
              page_id = page.id if page.respond_to?(:id) && !page.id.nil?

              cur_hash[MENU_NAV_LIST][path_key] = [path_key, path_part, page_title, page_weight, page_id, nav_page_url]

              cur_hash[MENU_NAV_PAGES] ||= {}
              cur_hash[MENU_NAV_PAGES][path_key] = page unless page.data[PAGE_CONFIG_ONLY]

              cnt = max_len
            end
          end
          cnt += 1
        end
      end

      menu_hash
    end

    def self.decode_title(text)
      text.to_s
          .gsub('%20', ' ')
          .gsub('+', ' ')
          .gsub('_', ' ')
          .gsub('%26', '&')
          .gsub('%2F', '/')
          .gsub('%3A', ':')
          .gsub('%3F', '?')
          .gsub('%2C', ',')
          .gsub('%2B', '+')
    end

    private_class_method :decode_title
  end
end
