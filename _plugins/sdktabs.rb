require 'digest/md5'

module Tags
    class SdkTabsBlock < Liquid::Block
      def initialize(tag_name, tabonly = 'false', tokens)
          super
          @tabclass = 'sdk-tab_toggle'
          @tabid = 'sdk-tab_' + (0...12).map { (97 + rand(26)).chr }.join
          params = tabonly.downcase.strip.split(/\s+/)
          if params.include?('local')
            @tabclass = 'sdk-tab_toggle_only'
          end
          @all_mode = params.include?('all')
      end
      def render(context)
          tabs = super.scan(/data\-sdk\-tab=\"sdk\-(.*?)\"/)
          tabslist = '<ul role="tablist" class="sdk-ab-nav sdk-ab-nav-tabs ' + @tabclass + '_ul" id="' + @tabid + '_nav">' + "\n"

          if @all_mode
            tabslist += '    <li role="presentation" class="sdkrow sdktabs-all-tab active"><a role="tab" tabindex="0" aria-selected="true" class="sdktabs-all-btn">All</a></li>' + "\n"
          end

          if tabs.length > 0
            tabs.each_with_index do |tab, ind|
              itemid = (0...12).map { (97 + rand(26)).chr }.join

              tabslug = tab[0].gsub(/[^0-9a-z]/i, '')
              tabslug = Digest::MD5.hexdigest(tab[0]) if tabslug.empty?

              tab_aria_selected = (@all_mode || ind > 0) ? 'false' : 'true'
              tab_tabindex      = (@all_mode || ind > 0) ? '-1'    : '0'

              # scan returns array of results, only care about first match
              tabslist += '    <li role="presentation" id="sdkt_' + itemid + '" class="sdkrow ' + tabslug
              if ind == 0 && !@all_mode
                tabslist += ' active'
              end
              tabslist += '"><a role="tab" tabindex="' + tab_tabindex + '" aria-selected="' + tab_aria_selected + '" class="' + @tabclass + '" data-sdk-tab-target="' + @tabid + '" data-sdk-tab="' + tabslug + '">' + tab[0] + '</a></li>' + "\n"
            end
          end
          tabslist += '</ul>'  + "\n"

          content_html = super
          if @all_mode
            content_html = content_html.gsub('class="sdk-ab-tab-pane ', 'class="sdk-ab-tab-pane active ')
          end

          result = tabslist + '<div id="' + @tabid + '" class="sdk-tab-content ' + @tabclass + '_div">' + "\n" + content_html + "\n</div>\n"

          if @all_mode
            result += <<~JS
              <script>
              (function() {
                var nav = document.getElementById('#{@tabid}_nav');
                var content = document.getElementById('#{@tabid}');
                if (!nav || !content) return;
                nav.querySelector('.sdktabs-all-btn').addEventListener('click', function(e) {
                  e.preventDefault();
                  content.querySelectorAll('.sdk-ab-tab-pane').forEach(function(p) { p.classList.add('active'); });
                  nav.querySelectorAll('li').forEach(function(li) { li.classList.remove('active'); });
                  nav.querySelector('.sdktabs-all-tab').classList.add('active');
                  nav.querySelectorAll('[role="tab"]').forEach(function(a) {
                    a.setAttribute('aria-selected', 'false');
                    a.setAttribute('tabindex', '-1');
                  });
                  this.setAttribute('aria-selected', 'true');
                  this.setAttribute('tabindex', '0');
                });
              })();
              </script>
            JS
          end

          result
      end
    end

    class SdkTabBlock < Liquid::Block
      def initialize(tag_name, tab, tokens)
          super
          @tab = tab.strip.downcase
      end

      def render(context)
          return "" if @tab.empty?

          site      = context.registers[:site]
          converter = site.find_converter_instance(Jekyll::Converters::Markdown)

          lines = super.rstrip.split(/\r\n|\r|\n/).select { |line| line.size > 0 }
          indentation = lines.map do |line|
              match = line.match(/^(\s+)[^\s]+/)
          match ? match[1].size : 0
          end
          indentation = indentation.min
          contentid = (0...12).map { (97 + rand(26)).chr }.join

          content = indentation ? super.gsub(/^#{' |\t' * indentation}/, '') : super
          content = converter.convert(content)
          content = content.strip # Strip again to avoid "\n"
          tabslug = @tab.gsub(/[^0-9a-z]/i, '')
          tabslug = Digest::MD5.hexdigest(@tab) if tabslug.empty?
          content = content.gsub(/<(h[1-6]) id=\"/, '<\1 id="' + tabslug + '_')

          return '<div id="sdkc_' + contentid + '" role="tabpanel" tabindex="0" class="sdk-ab-tab-pane ' + tabslug + '_tab " data-sdk-tab="sdk-' + @tab + '">' + content + "</div>"
      end
    end

    class SdkSubTabsBlock < Liquid::Block
      def initialize(tag_name, tabonly = 'false', tokens)
          super
          @tabclass = 'sub_sdk-tab_toggle'
          @tabid = 'sub_sdk-tab_' + (0...12).map { (97 + rand(26)).chr }.join
          if tabonly.downcase.strip != 'global'
            @tabclass = 'sub_sdk-tab_toggle_only'
          end
      end
      def render(context)
          tabs = super.scan(/data\-sdk\-sub\_tab=\"(.*?)\"/)
          tabslist = '<ul role="tablist" class="sdk-ab-sub_nav sdk-ab-sub_nav-sub_tabs ' + @tabclass + '_ul" id="' + @tabid + '_nav">' + "\n"

          if tabs.length > 0
            tabs.each_with_index do |tab, ind|

              itemid = (0...12).map { (97 + rand(26)).chr }.join
              tabslug = tab[0].gsub(/[^0-9a-z]/i, '')
              tabslug = Digest::MD5.hexdigest(tab[0]) if tabslug.empty?

              tab_aria_selected = ind == 0 ? 'true' : 'false'
              tab_tabindex      = ind == 0 ? '0'    : '-1'

              # scan returns array of results, only care about first match
              tabslist += '    <li role="presentation" id="sdkst_' + itemid + '" class="coderow ' + tabslug + '_sub_sdk_tab'
              if ind == 0
                tabslist += ' sub_active'
              end
              tabslist += '"><a role="tab" tabindex="' + tab_tabindex + '" aria-selected="' + tab_aria_selected + '" class="' + @tabclass + '" data-sdk-sub_tab-target="' + @tabid + '" data-sdk-sub_tab="' + tabslug + '_sub_sdk_tab">' + tab[0] + '</a></li>' + "\n"
            end
          end
          tabslist += '</ul>'  + "\n"
          tabslist + '<div id="' + @tabid + '" class="sdk-ab-sub_tab-content ' + @tabclass + '_sdk_div">' + "\n" + super + "\n</div>\n"
      end
    end

    class SdkSubTabBlock < Liquid::Block
      def initialize(tag_name, tab, tokens)
          super
          @tab = tab.strip.downcase
      end

      def render(context)
          return "" if @tab.empty?

          site      = context.registers[:site]
          converter = site.find_converter_instance(Jekyll::Converters::Markdown)

          lines = super.rstrip.split(/\r\n|\r|\n/).select { |line| line.size > 0 }
          indentation = lines.map do |line|
              match = line.match(/^(\s+)[^\s]+/)
          match ? match[1].size : 0
          end
          indentation = indentation.min
          contentid = (0...12).map { (97 + rand(26)).chr }.join

          content = indentation ? super.gsub(/^#{' |\t' * indentation}/, '') : super
          content = converter.convert(content)
          content = content.strip # Strip again to avoid "\n"
          tabslug = @tab.gsub(/[^0-9a-z]/i, '')
          tabslug = Digest::MD5.hexdigest(@tab) if tabslug.empty?

          return '<div id="sdksc_' + contentid + '" role="tabpanel" tabindex="0" class="sdk-ab-sub_tab-pane ' + tabslug + '_sub_sdk_tab " data-sdk-sub_tab="' + @tab + '">' + content + "</div>"
      end
    end
end

Liquid::Template.register_tag("sdktabs", Tags::SdkTabsBlock)
Liquid::Template.register_tag("sdktab",  Tags::SdkTabBlock)
Liquid::Template.register_tag("sdksubtabs", Tags::SdkSubTabsBlock)
Liquid::Template.register_tag("sdksubtab",  Tags::SdkSubTabBlock)
