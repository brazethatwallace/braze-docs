require 'cgi'
require 'liquid'

# Stub Jekyll Document so plugin code can type-check menu pages
unless defined?(Jekyll::Document)
  module Jekyll
    class Document
      attr_reader :url, :id, :data
      def initialize(url, id, data = {})
        @url  = url
        @id   = id
        @data = data
      end
      def [](key) = @data[key]
      def respond_to?(method, *) = method == :id ? true : super
    end
  end
end

require_relative '../../_plugins/urlnavmenu_html_renderer'

# Build a minimal menu_hash for a two-level nav:
#   /docs/guide/intro  (leaf, no children)
#   /docs/guide/setup  (has a child: /docs/guide/setup/install)
def build_test_menu(current_page_id)
  intro_doc   = Jekyll::Document.new('/docs/guide/intro',           '/docs/guide/intro')
  setup_doc   = Jekyll::Document.new('/docs/guide/setup',           '/docs/guide/setup')
  install_doc = Jekyll::Document.new('/docs/guide/setup/install',   '/docs/guide/setup/install')

  intro_entry   = ['intro',   'intro',   'Introduction',  1, '/docs/guide/intro',         '/docs/guide/intro/']
  setup_entry   = ['setup',   'setup',   'Setup',         2, '/docs/guide/setup',         '/docs/guide/setup/']
  install_entry = ['install', 'install', 'Install',       1, '/docs/guide/setup/install', '/docs/guide/setup/install/']

  {
    :menu_nav_list   => { 'intro' => intro_entry, 'setup' => setup_entry },
    :menu_nav_pages  => { 'intro' => intro_doc,   'setup' => setup_doc   },
    'intro'          => nil,
    'setup'          => {
      :menu_nav_list  => { 'install' => install_entry },
      :menu_nav_pages => { 'install' => install_doc },
      'install'       => nil
    }
  }
end

# Same tree with setup as the first root item (lower page_order).
def build_test_menu_setup_first
  intro_doc   = Jekyll::Document.new('/docs/guide/intro',           '/docs/guide/intro')
  setup_doc   = Jekyll::Document.new('/docs/guide/setup',           '/docs/guide/setup')
  install_doc = Jekyll::Document.new('/docs/guide/setup/install',   '/docs/guide/setup/install')

  intro_entry   = ['intro',   'intro',   'Introduction',  2, '/docs/guide/intro',         '/docs/guide/intro/']
  setup_entry   = ['setup',   'setup',   'Setup',         1, '/docs/guide/setup',         '/docs/guide/setup/']
  install_entry = ['install', 'install', 'Install',       1, '/docs/guide/setup/install', '/docs/guide/setup/install/']

  {
    :menu_nav_list   => { 'setup' => setup_entry, 'intro' => intro_entry },
    :menu_nav_pages  => { 'setup' => setup_doc,   'intro' => intro_doc   },
    'setup'          => {
      :menu_nav_list  => { 'install' => install_entry },
      :menu_nav_pages => { 'install' => install_doc },
      'install'       => nil
    },
    'intro'          => nil
  }
end

def build_renderer(current_page_url, current_page_id, minlevel: 2)
  current_page = Struct.new(:url, :id).new(current_page_url, current_page_id)

  Jekyll::UrlNavMenuHtmlRenderer.new(
    baseurl: '',
    nav_expand_list: [],
    minlevel: minlevel,
    currentpage: current_page,
    currentpage_id: current_page_id,
    expand_section_label: 'Expand section',
    collapse_section_label: 'Collapse section'
  )
end

RSpec.describe Jekyll::UrlNavMenuHtmlRenderer, '#render' do
  describe 'active leaf page (no children)' do
    it "renders aria-current='page' on the active span" do
      menu     = build_test_menu('/docs/guide/intro')
      renderer = build_renderer('/docs/guide/intro/', '/docs/guide/intro')
      html     = renderer.render(menu, '', 0, true)

      expect(html).to include("aria-current='page'")
    end

    it 'wraps the first root item in nav-item--rail for the sidebar toggle host' do
      menu     = build_test_menu('/docs/guide/intro')
      renderer = build_renderer('/docs/guide/intro/', '/docs/guide/intro')
      html     = renderer.render(menu, '', 0, true)

      expect(html).to include('nav-item--rail')
      expect(html).to include("id='sidebar_toggle_host'")
    end

    it 'emits only one sidebar_toggle_host when nav_level is 1 and a nested section is current' do
      menu     = build_test_menu('/docs/guide/setup/install')
      renderer = build_renderer('/docs/guide/setup/install/', '/docs/guide/setup/install', minlevel: 1)
      html     = renderer.render(menu, '', 0, true)

      expect(html.scan(/id='sidebar_toggle_host'/).length).to eq(1)
    end

    it 'keeps nav-item--rail on the first root item when it is current and has children' do
      menu     = build_test_menu_setup_first
      renderer = build_renderer('/docs/guide/setup/', '/docs/guide/setup', minlevel: 1)
      html     = renderer.render(menu, '', 0, true)

      expect(html.scan(/id='sidebar_toggle_host'/).length).to eq(1)
      expect(html).to match(/class='[^']*nav-item--rail[^']*' id='parent_nav_setup'/)
      expect(html).not_to match(/class='[^']*nav-item--rail[^']*' id='parent_nav_setup_install'/)
    end
  end

  describe 'active section page (has children, is current page)' do
    it "renders aria-current='page' on the active span inside the nav_item_row" do
      menu     = build_test_menu('/docs/guide/setup')
      renderer = build_renderer('/docs/guide/setup/', '/docs/guide/setup')
      html     = renderer.render(menu, '', 0, true)

      expect(html).to include("aria-current='page'")
    end
  end

  describe 'non-active page' do
    it 'does not render aria-current on a regular link' do
      menu     = build_test_menu('/docs/guide/intro')
      renderer = build_renderer('/docs/guide/setup/', '/docs/guide/setup')
      html     = renderer.render(menu, '', 0, true)

      # intro is not the current page — its link should have no aria-current
      expect(html).not_to match(/href='[^']*intro[^']*'[^>]*aria-current/)
    end
  end

  describe 'leaf item HTML structure' do
    it 'renders a flat nav_reg with nav_link directly inside, no nav_block wrapper' do
      menu     = build_test_menu('/docs/guide/setup')
      renderer = build_renderer('/docs/guide/setup/', '/docs/guide/setup')
      html     = renderer.render(menu, '', 0, true)

      # Non-active leaf (install) should be nav_reg > a.nav_link, no nav_block in between
      expect(html).to include("<div class='nav_reg'")
      expect(html).not_to match(/<div class='nav_reg'[^>]*>\s*<div class='nav_block'/)
    end
  end
end
