# Normalize Jekyll page paths for production URLs (Vercel trailingSlash: false).
module Jekyll
  module PublicDocPathFilter
    def public_doc_path(input)
      path = input.to_s.gsub("index.html", "")
      return path if path.empty? || path == "/"

      path.chomp("/")
    end
  end
end

Liquid::Template.register_filter(Jekyll::PublicDocPathFilter)
