{% comment %}
  Shared drag-and-drop editor guidance for hiding rows and blocks by device.
  Parameters:
  - channel (required): "banner", "in_app_message", or "landing_page"
{% endcomment %}

{% if include.channel == 'banner' %}
{% assign heading_level = '#####' %}
{% assign preview_subject = 'Ihr Banner' %}
{% assign live_phrase = 'im Live-Banner' %}
{% elsif include.channel == 'in_app_message' %}
{% assign heading_level = '###' %}
{% assign preview_subject = 'Ihre Nachricht' %}
{% assign live_phrase = 'in der Live-In-App-Nachricht' %}
{% elsif include.channel == 'landing_page' %}
{% assign heading_level = '####' %}
{% assign preview_subject = 'Ihre Seite' %}
{% assign live_phrase = 'auf der Live-Landing-Page' %}
{% endif %}

{{ heading_level }} Zeilen und Blöcke nach Gerät ausblenden

Um Ihr Layout für Desktop im Vergleich zu Tablet und Mobilgerät anzupassen, wählen Sie eine Zeile oder einen Block auf der Arbeitsfläche aus und verwenden Sie dann den Umschalter **Ausblenden auf** im Eigenschaften-Panel, um die Zeile oder den Block auf **Desktop** oder **Tablet und kleinere Geräte** auszublenden. Eine ausgeblendete Zeile oder ein ausgeblendeter Block wird für diesen Gerätetyp nicht angezeigt – weder bei der Vorschau von {{ preview_subject }} im Drag-and-Drop-Editor noch {{ live_phrase }}.