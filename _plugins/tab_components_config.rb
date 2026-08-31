require 'digest/md5'

module TabComponentsConfig
  module_function

  def for(site, section)
    (site.data['tab_components'] || {})[section] || {}
  end

  def random_id(length = 12)
    (0...length).map { (97 + rand(26)).chr }.join
  end

  def slugify(tab_name)
    slug = tab_name.gsub(/[^0-9a-z]/i, '')
    slug = Digest::MD5.hexdigest(tab_name) if slug.empty?
    slug
  end

  def toggle_class(toggle_config, tabonly, mode)
    case mode
    when :local
      tabonly.to_s.downcase.strip == 'local' ? toggle_config['local'] : toggle_config['default']
    when :global
      tabonly.to_s.downcase.strip == 'global' ? toggle_config['default'] : toggle_config['non_global']
    end
  end
end
