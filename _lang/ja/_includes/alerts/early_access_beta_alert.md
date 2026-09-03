{% comment %}
  早期アクセスまたはベータ版のアラートです。早期アクセスまたはベータ版の機能やエンドポイントに使用します。
  パラメーター:
  - feature（必須）：機能や対象。例：「This endpoint」、「SCIM provisioning」、「The Okta integration」
  - type（オプション）："early_access"（デフォルト）または "beta"
  - contact（オプション）：連絡先。例："Braze account manager"（デフォルト）または "customer success manager"
{% endcomment %}
{% assign contact_role = include.contact | default: "Braze account manager" %}
{% if include.type == "beta" %}
{% alert important %}
{{ include.feature }}は現在ベータ版です。ベータ版への参加にご興味がある場合は、{{ contact_role }}までお問い合わせください。
{% endalert %}
{% else %}
{% alert important %}
{{ include.feature }}は現在早期アクセス中です。早期アクセスへの参加にご興味がある場合は、{{ contact_role }}までお問い合わせください。
{% endalert %}
{% endif %}