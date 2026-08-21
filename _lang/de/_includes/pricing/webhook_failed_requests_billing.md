{% comment %}
  Shared webhook billing note for Message Credits / Action Credits pages.
  Optional parameter:
  - credit_name: Product name shown in the sentence (default: "Message Credits")
{% endcomment %}
{% assign credit_name = include.credit_name | default: "Message Credits" %}
Ab dem 19. August 2026 werden fehlgeschlagene Webhook-Anfragen von der Nutzungsabrechnung ausgeschlossen; nur erfolgreiche Anfragen verbrauchen {{ credit_name }}. Diese Änderung gilt prospektiv und hat keine Auswirkungen auf die vor dem Stichtag abgerechnete Nutzung.