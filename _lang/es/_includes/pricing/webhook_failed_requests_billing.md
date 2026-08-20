{% comment %}
  Shared webhook billing note for Message Credits / Action Credits pages.
  Optional parameter:
  - credit_name: Product name shown in the sentence (default: "Message Credits")
{% endcomment %}
{% assign credit_name = include.credit_name | default: "Message Credits" %}
A partir del 19 de agosto de 2026, las solicitudes de webhook fallidas se excluyen de la facturación de uso; solo las solicitudes exitosas utilizan {{ credit_name }}. Este cambio se aplica de forma prospectiva y no afecta al uso facturado antes de la fecha de entrada en vigor.