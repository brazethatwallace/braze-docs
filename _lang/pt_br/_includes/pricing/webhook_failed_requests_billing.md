{% comment %}
  Shared webhook billing note for Message Credits / Action Credits pages.
  Optional parameter:
  - credit_name: Product name shown in the sentence (default: "Message Credits")
{% endcomment %}
{% assign credit_name = include.credit_name | default: "Message Credits" %}
A partir de 19 de agosto de 2026, as solicitações de webhook com falha serão excluídas do faturamento de uso; apenas as solicitações bem-sucedidas utilizam {{ credit_name }}. Essa alteração se aplica de forma prospectiva e não afeta o uso faturado antes da data de vigência.