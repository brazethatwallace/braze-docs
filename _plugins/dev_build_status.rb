# frozen_string_literal: true

# Records Jekyll build completion during local development so proxy.rb can notify
# browsers over SSE (BD-6623).
module Jekyll
  module DevBuildStatus
    module_function

    def build_status_path(site)
      File.join(site.source, '.dev', 'build-complete')
    end

    def write_build_complete(site)
      path = build_status_path(site)
      FileUtils.mkdir_p(File.dirname(path))
      File.write(path, Time.now.to_f.to_s)
    end
  end

  Jekyll::Hooks.register :site, :post_write do |site|
    next unless Jekyll.env == 'development'

    Jekyll::DevBuildStatus.write_build_complete(site)
  end
end
