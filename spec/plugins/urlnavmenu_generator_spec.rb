require 'cgi'

# Stub Jekyll and Liquid so the plugin loads without a full Jekyll environment
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

module Liquid
  class Tag
    def initialize(tag_name, markup, tokens); end
  end

  module Template
    def self.register_tag(name, klass); end
    def self.parse(str) = self
    def self.render(ctx) = str
  end
end

require_relative '../../_plugins/urlnavmenu_generator'

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

def build_menu_instance(current_page_url, current_page_id)
  instance = Jekyll::UrlNavMenu.allocate

  # Constants from initialize
  instance.instance_variable_set(:@menu_nav_list,    :menu_nav_list)
  instance.instance_variable_set(:@menu_nav_pages,   :menu_nav_pages)
  instance.instance_variable_set(:@menu_sorted_list, :menu_sorted_list)

  instance.instance_variable_set(:@nav_toggle_class,       'nav_toggle')
  instance.instance_variable_set(:@nav_item_class,         'nav-item')
  instance.instance_variable_set(:@nav_item_link_class,    'nav_link')
  instance.instance_variable_set(:@nav_prefix,             'nav')
  instance.instance_variable_set(:@nav_active_page_class,  'nav_url')
  instance.instance_variable_set(:@nav_active_basic_class, 'nav_reg')
  instance.instance_variable_set(:@nav_title_class,        'nav_title')
  instance.instance_variable_set(:@nav_title_block,        'nav_block')
  instance.instance_variable_set(:@page_weight,            'page_order')
  instance.instance_variable_set(:@page_hidden,            'hidden')
  instance.instance_variable_set(:@page_nav_title,         'nav_title')
  instance.instance_variable_set(:@page_config_only,       'config_only')

  instance.instance_variable_set(:@page_key_index,    0)
  instance.instance_variable_set(:@page_pg_index,     1)
  instance.instance_variable_set(:@page_title_index,  2)
  instance.instance_variable_set(:@page_weight_index, 3)
  instance.instance_variable_set(:@page_id_index,     4)
  instance.instance_variable_set(:@page_url_index,    5)

  instance.instance_variable_set(:@fa_class,          'fas')
  instance.instance_variable_set(:@activeclass,       ' active')
  instance.instance_variable_set(:@activeparentclass, ' active_parent')
  instance.instance_variable_set(:@unique_postfix,    '_nav_page')

  instance.instance_variable_set(:@expand_section_label,   'Expand section')
  instance.instance_variable_set(:@collapse_section_label, 'Collapse section')

  # Runtime state
  instance.instance_variable_set(:@baseurl,          '')
  instance.instance_variable_set(:@nav_expand_list,  [])
  instance.instance_variable_set(:@minlevel,         2)

  current_page = Struct.new(:url, :id).new(current_page_url, current_page_id)
  instance.instance_variable_set(:@currentpage,      current_page)
  instance.instance_variable_set(:@currentpage_id,   current_page_id)

  instance
end

RSpec.describe Jekyll::UrlNavMenu, '#build_menu_html' do
  describe 'active leaf page (no children)' do
    it "renders aria-current='page' on the active span" do
      menu     = build_test_menu('/docs/guide/intro')
      instance = build_menu_instance('/docs/guide/intro/', '/docs/guide/intro')
      html     = instance.send(:build_menu_html, menu, '', 0)

      expect(html).to include("aria-current='page'")
    end

    it 'wraps the first root item in nav-item--rail for the sidebar toggle host' do
      menu     = build_test_menu('/docs/guide/intro')
      instance = build_menu_instance('/docs/guide/intro/', '/docs/guide/intro')
      html     = instance.send(:build_menu_html, menu, '', 0)

      expect(html).to include('nav-item--rail')
      expect(html).to include("id='sidebar_toggle_host'")
    end
  end

  describe 'active section page (has children, is current page)' do
    it "renders aria-current='page' on the active span inside the nav_item_row" do
      menu     = build_test_menu('/docs/guide/setup')
      instance = build_menu_instance('/docs/guide/setup/', '/docs/guide/setup')
      html     = instance.send(:build_menu_html, menu, '', 0)

      expect(html).to include("aria-current='page'")
    end
  end

  describe 'non-active page' do
    it 'does not render aria-current on a regular link' do
      menu     = build_test_menu('/docs/guide/intro')
      instance = build_menu_instance('/docs/guide/setup/', '/docs/guide/setup')
      html     = instance.send(:build_menu_html, menu, '', 0)

      # intro is not the current page — its link should have no aria-current
      expect(html).not_to match(/href='[^']*intro[^']*'[^>]*aria-current/)
    end
  end

  describe 'leaf item HTML structure' do
    it 'renders a flat nav_reg with nav_link directly inside, no nav_block wrapper' do
      menu     = build_test_menu('/docs/guide/setup')
      instance = build_menu_instance('/docs/guide/setup/', '/docs/guide/setup')
      html     = instance.send(:build_menu_html, menu, '', 0)

      # Non-active leaf (install) should be nav_reg > a.nav_link, no nav_block in between
      expect(html).to include("<div class='nav_reg'")
      expect(html).not_to match(/<div class='nav_reg'[^>]*>\s*<div class='nav_block'/)
    end
  end
end
