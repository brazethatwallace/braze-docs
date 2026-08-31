# frozen_string_literal: true

# Records Jekyll build lifecycle during local development so proxy.rb can notify
# browsers over SSE (BD-6623, BD-6624).
module Jekyll
  module DevBuildStatus
    module_function

    def build_status_dir(site)
      File.join(site.source, '.dev')
    end

    def build_started_path(site)
      File.join(build_status_dir(site), 'build-started')
    end

    def build_complete_path(site)
      File.join(build_status_dir(site), 'build-complete')
    end

    def write_build_started(site)
      write_timestamp(build_started_path(site))
    end

    def write_build_complete(site)
      write_timestamp(build_complete_path(site))
    end

    def write_timestamp(path)
      FileUtils.mkdir_p(File.dirname(path))
      File.write(path, Time.now.to_f.to_s)
    end
  end

  Jekyll::Hooks.register :site, :pre_render do |site|
    next unless Jekyll.env == 'development'

    Jekyll::DevBuildStatus.write_build_started(site)
  end

  Jekyll::Hooks.register :site, :post_write do |site|
    next unless Jekyll.env == 'development'

    Jekyll::DevBuildStatus.write_build_complete(site)
  end
end
