# frozen_string_literal: true

require 'jekyll'

module Jekyll
  module ImageDimensions
    IMG_TAG_RE = /<img\b([^>]*?)>/i
    PNG_SIGNATURE = "\x89PNG\r\n\x1a\n".b.freeze
    JPEG_SIGNATURE = "\xFF\xD8".b.freeze
    SUPPORTED_EXTENSIONS = %w[.png .jpg .jpeg .gif .webp].freeze
    JPEG_SOF_MARKERS = [0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7, 0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF].freeze

    module_function

    def enabled?(site)
      config = site.config['image_dimensions'] || {}
      config.fetch('enabled', true)
    end

    def inject(html, site)
      return html if html.nil? || html.empty?

      html.gsub(IMG_TAG_RE) do |tag|
        attrs = Regexp.last_match(1)
        inject_tag(tag, attrs, site)
      end
    end

    def inject_tag(tag, attrs, site)
      return tag if attrs.match?(/\bwidth\s*=/i)

      src = extract_attr(attrs, 'src')
      return tag unless src

      local_path = local_asset_path(src, site)
      return tag unless local_path

      dimensions = dimensions_for(local_path)
      return tag unless dimensions

      attrs_with_dims = "#{attrs} width=\"#{dimensions[:width]}\" height=\"#{dimensions[:height]}\""
      "<img#{attrs_with_dims}>"
    end

    def extract_attr(attrs, name)
      match = attrs.match(/\b#{name}\s*=\s*(["'])(.*?)\1/i)
      match&.[](2)
    end

    def local_asset_path(src, site)
      path = src.split('?', 2).first
      baseurl = site.config.fetch('baseurl', '').to_s
      path = path.sub(%r{\A#{Regexp.escape(baseurl)}/?}, '') if baseurl && !baseurl.empty?
      path = path.sub(%r{\A/}, '')

      return nil unless path.start_with?('assets/')
      return nil unless SUPPORTED_EXTENSIONS.include?(File.extname(path).downcase)
      return nil unless File.file?(path)

      path
    end

    def dimensions_for(path)
      @dimensions_cache ||= {}
      return @dimensions_cache[path] if @dimensions_cache.key?(path)

      @dimensions_cache[path] = read_dimensions(path)
    end

    def clear_cache!
      @dimensions_cache = {}
    end

    def read_dimensions(path)
      case File.extname(path).downcase
      when '.png' then read_png(path)
      when '.jpg', '.jpeg' then read_jpeg(path)
      when '.gif' then read_gif(path)
      when '.webp' then read_webp(path)
      end
    rescue StandardError => e
      Jekyll.logger.warn 'ImageDimensions:', "Could not read #{path}: #{e.message}"
      nil
    end

    def read_png(path)
      File.open(path, 'rb') do |file|
        return nil unless file.read(8) == PNG_SIGNATURE

        file.read(4)
        return nil unless file.read(4) == 'IHDR'

        width, height = file.read(8).unpack('NN')
        return nil unless width.positive? && height.positive?

        { width: width, height: height }
      end
    end

    def read_gif(path)
      File.open(path, 'rb') do |file|
        return nil unless file.read(6)&.match?(/\AGIF8[79]a\z/)

        width, height = file.read(4).unpack('v2')
        return nil unless width.positive? && height.positive?

        { width: width, height: height }
      end
    end

    def read_jpeg(path)
      File.open(path, 'rb') do |file|
        return nil unless file.read(2) == JPEG_SIGNATURE

        loop do
          marker = file.read(1)
          return nil if marker.nil? || marker.empty?

          break unless marker.ord == 0xFF

          code = file.read(1)
          return nil if code.nil? || code.empty?

          code = code.ord
          length_bytes = file.read(2)
          return nil if length_bytes.nil? || length_bytes.bytesize < 2

          length = length_bytes.unpack1('n')
          if JPEG_SOF_MARKERS.include?(code)
            file.read(1)
            height, width = file.read(4).unpack('nn')
            return nil unless width.positive? && height.positive?

            return { width: width, height: height }
          end

          file.seek(length - 2, IO::SEEK_CUR)
        end
      end

      nil
    end

    VP8_KEYFRAME_START = "\x9D\x01\x2A".b.freeze

    def uint24_le(data)
      bytes = data.bytes
      bytes[0] | (bytes[1] << 8) | (bytes[2] << 16)
    end

    def vp8_lossy_dimensions(frame)
      return nil if frame.nil? || frame.bytesize < 10

      dim_offset =
        if frame[3, 3].b == VP8_KEYFRAME_START
          6
        elsif frame[0, 3].b == VP8_KEYFRAME_START
          3
        end
      return nil unless dim_offset

      width, height = frame[dim_offset, 4].unpack('v2')
      { width: width & 0x3FFF, height: height & 0x3FFF }
    end

    def read_webp(path)
      File.open(path, 'rb') do |file|
        return nil unless file.read(4) == 'RIFF'

        file.read(4)
        return nil unless file.read(4) == 'WEBP'

        chunk_header = file.read(8)
        return nil if chunk_header.nil? || chunk_header.bytesize < 8

        fourcc = chunk_header[0, 4]
        chunk_size = chunk_header[4, 4].unpack1('V')

        case fourcc
        when 'VP8 '
          frame = file.read(chunk_size)
          vp8_lossy_dimensions(frame)
        when 'VP8L'
          frame = file.read(chunk_size)
          return nil if frame.nil? || frame.bytesize < 5
          return nil unless frame[0].ord == 0x2F

          bits = frame[1, 4].unpack1('V')
          width = (bits & 0x3FFF) + 1
          height = ((bits >> 14) & 0x3FFF) + 1
          { width: width, height: height }
        when 'VP8X'
          frame = file.read(chunk_size)
          return nil if frame.nil? || frame.bytesize < 10

          width = 1 + uint24_le(frame[4, 3])
          height = 1 + uint24_le(frame[7, 3])
          { width: width, height: height }
        end
      end
    end
  end
end

Jekyll::Hooks.register :documents, :post_render do |document|
  next unless Jekyll::ImageDimensions.enabled?(document.site)

  document.output = Jekyll::ImageDimensions.inject(document.output, document.site)
end

Jekyll::Hooks.register :pages, :post_render do |page|
  next unless Jekyll::ImageDimensions.enabled?(page.site)

  page.output = Jekyll::ImageDimensions.inject(page.output, page.site)
end
