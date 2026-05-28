{% comment %}
  Moved into the includes/api subfolder; previously, this wasn't in a subfolder.
  Note for GET export campaign/canvas/send data_series analytics endpoints.
  Use with multi_lang_include.

  Parameters:
  - type (required): "campaign", "canvas", or "send" — selects the opening phrase and dashboard analytics label.
{% endcomment %}

{% if include.type == 'send' %}
{% capture counts_subject %}전송 수준 `data_series` 수치{% endcapture %}
{% capture dashboard_match %}대시보드 참여 분석{% endcapture %}
{% elsif include.type == 'canvas' %}
{% capture counts_subject %}이 엔드포인트의 수치{% endcapture %}
{% capture dashboard_match %}대시보드 Canvas 분석{% endcapture %}
{% elsif include.type == 'campaign' %}
{% capture counts_subject %}이 엔드포인트의 수치{% endcapture %}
{% capture dashboard_match %}대시보드 참여 분석{% endcapture %}
{% endif %}
{% alert note %}
{{ counts_subject }}는 {{ dashboard_match }} 또는 [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/)에서 구축한 집계와 항상 정확히 일치하지 않을 수 있습니다. 대시보드 측정기준과 API 시계열은 원시 Currents 이벤트와 다른 집계 기간 및 정의를 사용합니다. 일반적인 데이터 조정 관련 참고 사항은 [Currents FAQ]({{site.baseurl}}/user_guide/data/distribution/braze_currents/faq/)를 참조하세요.
{% endalert %}