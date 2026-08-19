{% comment %}
  Shared webhook billing note for Message Credits / Action Credits pages.
  Optional parameter:
  - credit_name: Product name shown in the sentence (default: "Message Credits")
{% endcomment %}
{% assign credit_name = include.credit_name | default: "Message Credits" %}
2026年8月19日より、失敗したWebhookリクエストは使用量の請求から除外され、成功したリクエストのみが{{ credit_name }}を消費します。この変更は将来に向けて適用され、発効日以前に請求された使用量には影響しません。