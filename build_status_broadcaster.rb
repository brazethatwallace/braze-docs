# frozen_string_literal: true

require 'filewatcher'
require 'json'
require 'singleton'

# Watches the Jekyll build-status files and broadcasts SSE events to connected clients.
class BuildStatusBroadcaster
  include Singleton

  HEARTBEAT_INTERVAL = 15
  BUILD_STATUS_DIR = File.expand_path('.dev', __dir__)
  BUILD_STARTED_FILE = File.join(BUILD_STATUS_DIR, 'build-started')
  BUILD_COMPLETE_FILE = File.join(BUILD_STATUS_DIR, 'build-complete')
  BUILD_STATUS_FILE = BUILD_COMPLETE_FILE

  def initialize
    @mutex = Mutex.new
    @clients = []
    @watcher_thread = nil
  end

  def start!
    return if @watcher_thread&.alive?

    @watcher_thread = Thread.new do
      FileUtils.mkdir_p(BUILD_STATUS_DIR)
      [BUILD_STARTED_FILE, BUILD_COMPLETE_FILE].each do |path|
        FileUtils.touch(path) unless File.exist?(path)
      end

      filewatcher = Filewatcher.new([BUILD_STARTED_FILE, BUILD_COMPLETE_FILE])
      filewatcher.watch do |changes|
        changes.each do |filename, _event|
          if filename.end_with?('build-started')
            broadcast_started
          elsif filename.end_with?('build-complete')
            broadcast_complete
          end
        end
      end
    rescue StandardError => e
      warn "Build status watcher error: #{e.message}"
    end
  end

  def serve_client(io)
    add_client(io)
    io.write("retry: 3000\n\n")
    io.flush
    wait_with_heartbeats(io)
  rescue IOError, Errno::EPIPE, Errno::ECONNRESET
    # Client disconnected.
  ensure
    remove_client(io)
  end

  def add_client(out)
    @mutex.synchronize { @clients << out }
  end

  def remove_client(out)
    @mutex.synchronize { @clients.delete(out) }
  end

  def broadcast_started
    started_at = read_timestamp(BUILD_STARTED_FILE)
    broadcast_event('build-started', started_at: started_at)
  end

  def broadcast_complete
    completed_at = read_timestamp(BUILD_COMPLETE_FILE)
    broadcast_event('build-complete', completed_at: completed_at)
  end

  def broadcast_latest
    broadcast_complete
  end

  def read_completed_at
    read_timestamp(BUILD_COMPLETE_FILE)
  end

  private

  def broadcast_event(event_name, payload)
    data = "event: #{event_name}\ndata: #{JSON.generate(payload)}\n\n"

    @mutex.synchronize do
      @clients.each do |client|
        client << data
        client.flush if client.respond_to?(:flush)
      rescue StandardError
        @clients.delete(client)
      end
    end
  end

  def read_timestamp(path)
    return Time.now.to_f unless File.exist?(path)

    content = File.read(path).strip
    return Time.now.to_f if content.empty?

    Float(content)
  rescue ArgumentError
    Time.now.to_f
  end

  def wait_with_heartbeats(io)
    loop do
      readable, = IO.select([io], nil, nil, HEARTBEAT_INTERVAL)
      if readable
        begin
          io.read_nonblock(1024)
        rescue IO::WaitReadable
          next
        rescue EOFError, IOError, Errno::EPIPE, Errno::ECONNRESET
          break
        end
      else
        io.write(": heartbeat\n\n")
        io.flush
      end
    end
  end
end
