{% comment %}
  Shared drag-and-drop editor guidance for hiding rows and blocks by device.
  Parameters:
  - channel (required): "banner", "in_app_message", or "landing_page"
{% endcomment %}

{% if include.channel == 'banner' %}
{% assign heading_level = '#####' %}
{% assign preview_subject = 'votre bannière' %}
{% assign live_phrase = 'dans la bannière en direct' %}
{% elsif include.channel == 'in_app_message' %}
{% assign heading_level = '###' %}
{% assign preview_subject = 'votre message' %}
{% assign live_phrase = 'dans le message in-app en direct' %}
{% elsif include.channel == 'landing_page' %}
{% assign heading_level = '####' %}
{% assign preview_subject = 'votre page' %}
{% assign live_phrase = 'sur la page de destination en direct' %}
{% endif %}

{{ heading_level }} Masquer des lignes et des blocs par appareil

Pour adapter votre mise en page aux ordinateurs de bureau par rapport aux tablettes et aux appareils mobiles, sélectionnez une ligne ou un bloc sur le canevas, puis utilisez le bouton **Hide on** dans le panneau de propriétés pour le masquer sur **Desktop** ou **Tablet and smaller devices**. Une ligne ou un bloc masqué n'apparaîtra pas pour ce type d'appareil, que ce soit lors de la prévisualisation de {{ preview_subject }} dans l'éditeur par glisser-déposer ou {{ live_phrase }}.