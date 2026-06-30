{% comment %}
  早期アクセスまたはベータ版のアラートです。早期アクセスまたはベータ版の機能やエンドポイントに使用します。
  パラメーター:
  - feature（必須）：機能や対象。例：「This endpoint」、「SCIM provisioning」、「The Okta integration」
  - type（オプション）："early_access"（デフォルト）または "beta"
{% endcomment %}
{% if include.type == "beta" %}
{% alert important %}
{{ include.feature }}は現在ベータ版です。ベータ版への参加にご興味がある場合は、Brazeアカウントマネージャーまでお問い合わせください。
{% endalert %}
{% else %}
{% alert important %}
{{ include.feature }}は現在早期アクセス中です。早期アクセスへの参加にご興味がある場合は、Brazeアカウントマネージャーまでお問い合わせください。
{% endalert %}
{% endif %}