{% comment %}
  Shared drag-and-drop editor guidance for hiding rows and blocks by device.
  Parameters:
  - channel (required): "banner", "in_app_message", or "landing_page"
{% endcomment %}

{% if include.channel == 'banner' %}
{% assign heading_level = '#####' %}
{% assign preview_subject = 'tu Banner' %}
{% assign live_phrase = 'en el Banner en vivo' %}
{% elsif include.channel == 'in_app_message' %}
{% assign heading_level = '###' %}
{% assign preview_subject = 'tu mensaje' %}
{% assign live_phrase = 'en el mensaje dentro de la aplicación en vivo' %}
{% elsif include.channel == 'landing_page' %}
{% assign heading_level = '####' %}
{% assign preview_subject = 'tu página' %}
{% assign live_phrase = 'en la página de destino en vivo' %}
{% endif %}

{{ heading_level }} Ocultar filas y bloques por dispositivo

Para adaptar tu diseño a escritorio frente a tableta y móvil, selecciona una fila o un bloque en el lienzo y luego usa el alternador **Ocultar en** en el panel de propiedades para ocultarlo en **Escritorio** o **Tableta y dispositivos más pequeños**. Una fila o bloque oculto no aparecerá para ese tipo de dispositivo, ya sea al previsualizar {{ preview_subject }} en el editor de arrastrar y soltar o {{ live_phrase }}.