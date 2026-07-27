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

{{ heading_level }} Ocultar linhas e blocos por dispositivo

Para adaptar o layout para desktop em comparação com tablet e dispositivos móveis, selecione uma linha ou bloco no canvas e use o botão **Hide on** no painel de propriedades para ocultá-lo em **Desktop** ou **Tablet and smaller devices**. Uma linha ou bloco oculto não será exibido para esse tipo de dispositivo, seja ao visualizar a prévia {{ preview_subject }} no editor de arrastar e soltar ou {{ live_phrase }}.