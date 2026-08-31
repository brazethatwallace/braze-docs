# frozen_string_literal: true

require 'jekyll'
require_relative 'llms_collector'
require_relative 'llms_writer'

module Jekyll
  class LlmsTxtGenerator
    def self.init
      # Use :post_render (after pages are rendered, before :site, :post_write).
      # At this point markdown_copy_llm's :pre_render hook has populated
      # __export_merged_md / llm_markdown_content on each doc, so we have the
      # high-quality rendered markdown available.
      Jekyll::Hooks.register :site, :post_render do |site|
        next if site.config['__llms_txt_static_files_added']
        register_llms_txt_static_files(site)
        site.config['__llms_txt_static_files_added'] = true
      rescue StandardError => e
        Jekyll.logger.error(
          "LlmsTxtGenerator:",
          "Failed to register llms.txt static files: #{e.class}: #{e.message}"
        )
      end

      # Safety net: if for any reason the static file registration didn't run
      # (load order, hook skipped), regenerate via direct file write after the
      # build completes. Skipped when StaticFiles already emitted the outputs.
      Jekyll::Hooks.register :site, :post_write do |site|
        next if site.config['__llms_txt_static_files_added']
        next if site.config['__llms_txt_generated_for_this_build']
        generate_llms_txt(site)
        site.config['__llms_txt_generated_for_this_build'] = true
      rescue StandardError => e
        Jekyll.logger.error(
          "LlmsTxtGenerator:",
          "Failed to generate llms.txt files via post_write fallback: #{e.class}: #{e.message}"
        )
      end
    end

    def self.register_llms_txt_static_files(site)
      artifacts = LlmsCollector.collect(site)
      LlmsWriter.register_static_files(site, artifacts)
    end

    def self.generate_llms_txt(site)
      artifacts = LlmsCollector.collect(site)
      LlmsWriter.write_fallback(site, artifacts)
    end
  end
end

# Initialize the plugin
Jekyll::LlmsTxtGenerator.init
