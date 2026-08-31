# frozen_string_literal: true

require 'fileutils'
require 'tmpdir'

module Jekyll
  module Hooks
    def self.register(*); end
  end

  def self.env
    'development'
  end
end

require_relative '../_plugins/dev_build_status'

RSpec.describe Jekyll::DevBuildStatus do
  let(:tmpdir) { File.join(Dir.tmpdir, "dev-build-status-#{Process.pid}") }
  let(:site) { Struct.new(:source).new(tmpdir) }

  after do
    FileUtils.rm_rf(tmpdir)
  end

  it 'writes a timestamp to .dev/build-complete under the site source' do
    described_class.write_build_complete(site)

    path = described_class.build_status_path(site)
    expect(File).to exist(path)
    expect(Float(File.read(path))).to be_a(Float)
  end
end
