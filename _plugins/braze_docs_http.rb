# Shared HTTP fetch for Jekyll plugins that call external APIs at build time
# (currently markdown_embed). Centralizes SSL, timeouts, and site.data caching.
require 'jekyll'
require 'net/http'
require 'uri'
require 'openssl'
require 'ostruct'

module BrazeDocsHttp
  OPEN_TIMEOUT = 60
  READ_TIMEOUT = 120

  module_function

  # Local-only SSL verify skip. Never applied when RACK_ENV=production.
  def skip_ssl_verify?(env_key = 'SKIP_HTTP_SSL_VERIFY')
    ENV[env_key].to_s.downcase == 'true' &&
      ENV['RACK_ENV'].to_s.downcase != 'production'
  end

  # GET + return the Net::HTTPResponse. Raises on network/SSL errors unless
  # rescue_errors is true, in which case returns OpenStruct(code: '500', body: nil).
  def get(url, skip_ssl_verify: false, rescue_errors: false, logger_prefix: 'BrazeDocsHttp',
          ssl_error_message: nil, error_message: nil)
    link = URI.parse(url.to_s.strip)
    http = Net::HTTP.new(link.host, link.port)
    http.use_ssl = (link.scheme == 'https')
    http.open_timeout = OPEN_TIMEOUT
    http.read_timeout = READ_TIMEOUT
    http.verify_mode = OpenSSL::SSL::VERIFY_NONE if skip_ssl_verify
    http.get(link.request_uri)
  rescue OpenSSL::SSL::SSLError => e
    raise unless rescue_errors

    # ssl_error_message may include a single "%s" for e.message
    message = if ssl_error_message
                ssl_error_message.to_s.sub('%s', e.message)
              else
                "SSL verification failed (#{e.message})."
              end
    ::Jekyll.logger.warn "#{logger_prefix}:", message
    OpenStruct.new(code: '500', body: nil)
  rescue StandardError => e
    raise unless rescue_errors

    message = if error_message
                error_message.to_s.sub('%s', e.message)
              else
                "Request failed (#{e.message})."
              end
    ::Jekyll.logger.warn "#{logger_prefix}:", message
    OpenStruct.new(code: '500', body: nil)
  end

  # Read a build-time cache entry from site.data (or any Hash-like cache).
  # Returns [hit, value] so callers can log cache hits without a second lookup.
  def cache_read(cache, key)
    return [true, cache[key]] if cache.include?(key)

    [false, nil]
  end

  def cache_write(cache, key, value)
    cache[key] = value
  end
end
