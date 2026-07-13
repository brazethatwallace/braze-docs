module Jekyll
  module Alerts
    class AlertTag < Liquid::Block

      def initialize(tag_name, markup, tokens)
        super
        @caption = markup
      end

      def render(context)
        site = context.registers[:site]
        converter = site.find_converter_instance(::Jekyll::Converters::Markdown)
        type = converter.convert(@caption).gsub(/<\/?p[^>]*>/, '').chomp.strip
        lang = (site.config['language'] || 'en').downcase
        labels = alert_labels_for(site, lang)
        label = (labels[type.downcase] || type).gsub('-', ' ')
        body = converter.convert(super(context))
        base_url = site.config['baseurl'] || '/docs'
        icon_file = { 'checkpoint' => 'stop', 'service-notice' => 'note' }.fetch(type, type)
        icon = "<img src='#{base_url}/assets/img/message-#{icon_file}.png' alt='' class='alert-icon'>"
        "<div class='alert alert-#{type}' role='alert'>#{icon}<div class='alert-msg'><span class='alert-label' role='heading' aria-level='6'>#{label}</span><br />#{body}</div></div>"
      end

      private

      def alert_labels_for(site, lang)
        supported_locales = Array(site.data.dig('locales', 'supported')).map { |code| code.to_s.downcase }
        return {} unless supported_locales.include?(lang)

        labels = site.data['alert_labels']
        labels.is_a?(Hash) ? (labels[lang] || {}) : {}
      end

    end
  end
end

Liquid::Template.register_tag('alert', Jekyll::Alerts::AlertTag)
