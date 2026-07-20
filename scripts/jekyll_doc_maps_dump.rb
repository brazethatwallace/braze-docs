#!/usr/bin/env ruby
# frozen_string_literal: true

# Single Jekyll boot that dumps both maps validate_doc_redirects.rb needs:
#   { "urls" => { path => public URL }, "headings" => { path => heading entry } }
#
# Replaces the previous two-boot sequence (jekyll_url_map_dump.rb +
# jekyll_heading_id_dump.rb) per ref. Standalone scripts remain for lighter
# one-map use cases (e.g. verify_redirect_targets_in_jekyll.rb).
#
# Usage (from repo root):
#   bundle exec ruby scripts/jekyll_doc_maps_dump.rb OUT.json [SOURCE_DIR]

require "json"
require_relative "jekyll_heading_id_dump"

out_path = ARGV[0] or abort "usage: jekyll_doc_maps_dump.rb OUT.json [SOURCE_DIR]"
source_dir = ARGV[1] || "."
File.write(out_path, JSON.generate(JekyllHeadingIdDump.build_maps(source_dir)))
