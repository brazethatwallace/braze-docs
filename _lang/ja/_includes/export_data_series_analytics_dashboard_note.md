{% comment %}
  Note for GET export campaign/canvas data_series analytics endpoints.
  Use with multi_lang_include.

  Parameters:
  - type (required): "canvas" or "campaign" — selects the dashboard analytics label in the sentence.
{% endcomment %}
{% if include.type == 'canvas' %}
{% capture dashboard_match %}ダッシュボードのCanvas分析{% endcapture %}
{% elsif include.type == 'campaign' %}
{% capture dashboard_match %}ダッシュボードのエンゲージメント分析{% endcapture %}
{% endif %}
{% alert note %}
このエンドポイントから返されるカウントは、{{ dashboard_match }}や[Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/)から構築した集計値と必ずしも正確に一致するとは限りません。ダッシュボードの指標やAPIの時系列データは、未加工のCurrentsイベントとは異なる集計時間枠や定義を使用しています。
{% endalert %}