require 'rack/reverse_proxy'
require 'sinatra'
require_relative 'build_status_broadcaster'

lang = ARGV.length > 0 ? ARGV[0].downcase : nil

def dev_build_status_enabled?
  return false if ENV.fetch('RACK_ENV', 'development') == 'production'
  return false if ENV.fetch('BRAZE_DOCS_BUILD_STATUS_SSE', '1') == '0'

  true
end

if dev_build_status_enabled?
  BuildStatusBroadcaster.instance.start!
end

use Rack::ReverseProxy do
  # Set :preserve_host to true globally (default is true already)
  reverse_proxy_options preserve_host: true
  reverse_proxy /^\/docs(\/.*)$/, 'http://localhost:5006/docs/$1'
end

set :port, 4000

get '/sse/build-status' do
  halt 404 unless dev_build_status_enabled?
  halt 501, 'Streaming not supported' unless env['rack.hijack']

  io = env['rack.hijack'].call
  Thread.new do
    begin
      io.write "HTTP/1.1 200 OK\r\n"
      io.write "Content-Type: text/event-stream; charset=utf-8\r\n"
      io.write "Cache-Control: no-cache\r\n"
      io.write "Connection: keep-alive\r\n"
      io.write "X-Accel-Buffering: no\r\n"
      io.write "\r\n"
      io.flush
      BuildStatusBroadcaster.instance.serve_client(io)
    ensure
      io.close rescue nil
    end
  end

  # Release the Puma request thread; the hijacked IO is served in the background.
  status -1
  body []
end

get '/' do
  if !(lang.nil?) && (lang != 'en')
    send_file File.join(settings.public_folder, "index_#{lang}.html")
  else
    send_file File.join(settings.public_folder, 'index.html')
  end
end
