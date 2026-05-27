{% comment %}
  Moved into the includes/api subfolder; previously, this wasn't in a subfolder.
  Note for GET export campaign/canvas/send data_series analytics endpoints.
  Use with multi_lang_include.

  Parameters:
  - type (required): "campaign", "canvas", or "send" — selects the opening phrase and dashboard analytics label.
{% endcomment %}

{% if include.type == 'send' %}
{% capture counts_subject %}送信レベルの`data_series`カウント{% endcapture %}
{% capture dashboard_match %}ダッシュボードのエンゲージメント分析{% endcapture %}
{% elsif include.type == 'canvas' %}
{% capture counts_subject %}このエンドポイントから返されるカウント{% endcapture %}
{% capture dashboard_match %}ダッシュボードのキャンバス分析{% endcapture %}
{% elsif include.type == 'campaign' %}
{% capture counts_subject %}このエンドポイントから返されるカウント{% endcapture %}
{% capture dashboard_match %}ダッシュボードのエンゲージメント分析{% endcapture %}
{% endif %}
{% alert note %}
{{ counts_subject }}は、{{ dashboard_match }}や[Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/)から構築した集計値と必ずしも正確に一致するとは限りません。ダッシュボードの指標やAPIの時系列データは、未加工のCurrentsイベントとは異なる集計時間枠や定義を使用しています。一般的な照合に関する注意事項については、[Currents FAQ]({{site.baseurl}}/user_guide/data/distribution/braze_currents/faq/)を参照してください。
{% endalert %}