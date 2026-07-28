{% comment %}
  Shared drag-and-drop editor guidance for hiding rows and blocks by device.
  Parameters:
  - channel (required): "banner", "in_app_message", or "landing_page"
{% endcomment %}

{% if include.channel == 'banner' %}
{% assign heading_level = '#####' %}
{% assign preview_subject = 'seu Banner' %}
{% assign live_phrase = 'no Banner ao vivo' %}
{% elsif include.channel == 'in_app_message' %}
{% assign heading_level = '###' %}
{% assign preview_subject = 'sua mensagem' %}
{% assign live_phrase = 'na mensagem no app ao vivo' %}
{% elsif include.channel == 'landing_page' %}
{% assign heading_level = '####' %}
{% assign preview_subject = 'sua página' %}
{% assign live_phrase = 'na landing page ao vivo' %}
{% endif %}

{{ heading_level }} Ocultar linhas e blocos por dispositivo

Para adaptar o layout para desktop em comparação com tablet e dispositivos móveis, selecione uma linha ou bloco no canvas e use o botão **Hide on** no painel de propriedades para ocultá-lo em **Desktop** ou **Tablet and smaller devices**. Uma linha ou bloco oculto não será exibido para esse tipo de dispositivo, seja ao visualizar a prévia de {{ preview_subject }} no editor de arrastar e soltar ou {{ live_phrase }}.