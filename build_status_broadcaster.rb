# frozen_string_literal: true

require 'filewatcher'
require 'json'
require 'singleton'

# Watches the Jekyll build-status file and broadcasts SSE events to connected clients.
class BuildStatusBroadcaster
  include Singleton

  HEARTBEAT_INTERVAL = 15
  BUILD_STATUS_FILE = File.expand_path('.dev/build-complete', __dir__)

  def initialize
    @mutex = Mutex.new
    @clients = []
    @watcher_thread = nil
  end

  def start!
    return if @watcher_thread&.alive?

    @watcher_thread = Thread.new do
      FileUtils.mkdir_p(File.dirname(BUILD_STATUS_FILE))
      FileUtils.touch(BUILD_STATUS_FILE) unless File.exist?(BUILD_STATUS_FILE)

      filewatcher = Filewatcher.new([BUILD_STATUS_FILE])
      filewatcher.watch do |_changes|
        broadcast_latest
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

  def broadcast_latest
    completed_at = read_completed_at
    payload = "event: build-complete\ndata: #{JSON.generate(completed_at: completed_at)}\n\n"

    @mutex.synchronize do
      @clients.each do |client|
        client << payload
        client.flush if client.respond_to?(:flush)
      rescue StandardError
        @clients.delete(client)
      end
    end
  end

  def read_completed_at
    return Time.now.to_f unless File.exist?(BUILD_STATUS_FILE)

    content = File.read(BUILD_STATUS_FILE).strip
    return Time.now.to_f if content.empty?

    Float(content)
  rescue ArgumentError
    Time.now.to_f
  end

  private

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
