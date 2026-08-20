{% comment %}
  Shared webhook billing note for Message Credits / Action Credits pages.
  Optional parameter:
  - credit_name: Product name shown in the sentence (default: "Message Credits")
{% endcomment %}
{% assign credit_name = include.credit_name | default: "Message Credits" %}
Effective August 19, 2026, failed webhook requests are excluded from usage billing; only successful requests use {{ credit_name }}. This change applies prospectively and does not affect usage billed before the effective date.
