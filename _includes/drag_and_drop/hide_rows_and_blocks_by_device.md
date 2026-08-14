{% comment %}
  Shared drag-and-drop editor guidance for hiding rows and blocks by device.
  Parameters:
  - channel (required): "banner", "in_app_message", or "landing_page"
{% endcomment %}

{% if include.channel == 'banner' %}
{% assign heading_level = '#####' %}
{% assign preview_subject = 'your Banner' %}
{% assign live_phrase = 'in the live Banner' %}
{% elsif include.channel == 'in_app_message' %}
{% assign heading_level = '###' %}
{% assign preview_subject = 'your message' %}
{% assign live_phrase = 'in the live in-app message' %}
{% elsif include.channel == 'landing_page' %}
{% assign heading_level = '####' %}
{% assign preview_subject = 'your page' %}
{% assign live_phrase = 'on the live landing page' %}
{% endif %}

{{ heading_level }} Hide rows and blocks by device

To tailor your layout for desktop versus tablet and mobile, select a row or block on the canvas, then use the **Hide on** toggle in the properties panel to hide it on **Desktop** or **Tablet and smaller devices**. A hidden row or block won't appear for that device type, either when previewing {{ preview_subject }} in the drag-and-drop editor or {{ live_phrase }}.
