{%- assign portal_url = site.baseurl | append: '/user_guide/administer/personal/product_portal' -%}
{%- assign feature_label = include.feature | default: 'this capability' -%}
{%- assign pain_point_channel = include.channel | default: '' | downcase -%}
{%- if include.context == 'gap' -%}
{{ feature_label }}にご興味がある場合は、[製品フィードバック]({{ portal_url }})を送信してください。
{%- elsif include.context == 'new_feature' -%}
{%- assign feature_label = include.feature | default: 'This capability' -%}
{{ feature_label }}は一般提供されています。[製品フィードバック]({{ portal_url }})を通じて、チームでの活用状況をお聞かせください。
{%- elsif include.context == 'pain_point' -%}
{%- if pain_point_channel == 'feature' -%}
{{ feature_label }}をご希望ですか？[製品フィードバック]({{ portal_url }})の送信をご検討ください。
{%- elsif pain_point_channel == 'ux' -%}
{{ feature_label }}についてフィードバックがある場合は、グローバルヘッダーの**サポート**メニューを開き、**フィードバックを共有**を選択してご意見をお寄せください。
{%- else -%}
<!-- product_feedback_cta fallback: missing or invalid pain_point channel; expected feature or ux -->
{{ feature_label }}をご希望ですか？[製品フィードバック]({{ portal_url }})の送信をご検討ください。
{%- endif -%}
{%- endif -%}