# frozen_string_literal: true

require 'fileutils'
require 'json'
require 'stringio'
require 'tmpdir'
require_relative '../build_status_broadcaster'

RSpec.describe BuildStatusBroadcaster do
  let(:status_dir) { File.join(Dir.tmpdir, "build-status-#{Process.pid}") }
  let(:started_file) { File.join(status_dir, 'build-started') }
  let(:complete_file) { File.join(status_dir, 'build-complete') }

  before do
    stub_const('BuildStatusBroadcaster::BUILD_STATUS_DIR', status_dir)
    stub_const('BuildStatusBroadcaster::BUILD_STARTED_FILE', started_file)
    stub_const('BuildStatusBroadcaster::BUILD_COMPLETE_FILE', complete_file)
    stub_const('BuildStatusBroadcaster::BUILD_STATUS_FILE', complete_file)
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
      File.write(complete_file, '1734567890.5')
      expect(described_class.instance.read_completed_at).to eq(1734567890.5)
    end
  end

  describe '#broadcast_started' do
    it 'writes a build-started SSE payload to connected clients' do
      File.write(started_file, '1734567890.25')
      client = StringIO.new
      broadcaster = described_class.instance
      broadcaster.add_client(client)

      broadcaster.broadcast_started

      output = client.string
      expect(output).to include('event: build-started')
      expect(output).to include('"started_at":1734567890.25')
    end
  end

  describe '#broadcast_complete' do
    it 'writes a build-complete SSE payload to connected clients' do
      File.write(complete_file, '1734567890.5')
      client = StringIO.new
      broadcaster = described_class.instance
      broadcaster.add_client(client)

      broadcaster.broadcast_complete

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
      broadcaster.broadcast_complete

      expect(broadcaster.instance_variable_get(:@clients)).to be_empty
    end
  end
end
