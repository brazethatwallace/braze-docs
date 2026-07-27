{% comment %}
  Shared drag-and-drop editor guidance for hiding rows and blocks by device.
  Parameters:
  - channel (required): "banner", "in_app_message", or "landing_page"
{% endcomment %}

{% if include.channel == 'banner' %}
{% assign heading_level = '#####' %}
{% assign preview_subject = '배너' %}
{% assign live_phrase = '실시간 배너에서' %}
{% elsif include.channel == 'in_app_message' %}
{% assign heading_level = '###' %}
{% assign preview_subject = '메시지' %}
{% assign live_phrase = '실시간 인앱 메시지에서' %}
{% elsif include.channel == 'landing_page' %}
{% assign heading_level = '####' %}
{% assign preview_subject = '페이지' %}
{% assign live_phrase = '실시간 랜딩 페이지에서' %}
{% endif %}

{{ heading_level }} 기기별 행 및 블록 숨기기

데스크톱과 태블릿 및 모바일에 맞게 레이아웃을 조정하려면 캔버스에서 행 또는 블록을 선택한 다음, 속성 패널의 **Hide on** 토글을 사용하여 **Desktop** 또는 **Tablet and smaller devices**에서 숨길 수 있습니다. 숨겨진 행 또는 블록은 드래그 앤 드롭 편집기에서 {{ preview_subject }}을(를) 미리 볼 때나 {{ live_phrase }} 해당 기기 유형에 표시되지 않습니다.