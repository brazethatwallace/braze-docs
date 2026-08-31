# frozen_string_literal: true

require 'fileutils'
require 'json'
require 'stringio'
require 'tmpdir'
require_relative '../build_status_broadcaster'

RSpec.describe BuildStatusBroadcaster do
  let(:status_dir) { File.join(Dir.tmpdir, "build-status-#{Process.pid}") }
  let(:status_file) { File.join(status_dir, 'build-complete') }

  before do
    stub_const('BuildStatusBroadcaster::BUILD_STATUS_FILE', status_file)
    FileUtils.mkdir_p(status_dir)
    broadcaster = described_class.instance
    broadcaster.instance_variable_set(:@clients, [])
    broadcaster.instance_variable_set(:@watcher_thread, nil)
  end

  after do
    FileUtils.rm_rf(status_dir)
  end

  describe '#read_completed_at' do
    it 'returns the timestamp written to the status file' do
      File.write(status_file, '1734567890.5')
      expect(described_class.instance.read_completed_at).to eq(1734567890.5)
    end

    it 'falls back when the file contains invalid data' do
      File.write(status_file, 'not-a-number')
      expect(described_class.instance.read_completed_at).to be_a(Float)
    end
  end

  describe '#broadcast_latest' do
    it 'writes a build-complete SSE payload to connected clients' do
      File.write(status_file, '1734567890.5')
      client = StringIO.new
      broadcaster = described_class.instance
      broadcaster.add_client(client)

      broadcaster.broadcast_latest

      output = client.string
      expect(output).to include('event: build-complete')
      expect(output).to include('"completed_at":1734567890.5')
    end

    it 'removes clients that raise on write' do
      client = Object.new
      def client.<<(_payload)
        raise IOError, 'broken pipe'
      end

      broadcaster = described_class.instance
      broadcaster.add_client(client)
      broadcaster.broadcast_latest

      expect(broadcaster.instance_variable_get(:@clients)).to be_empty
    end
  end
end
