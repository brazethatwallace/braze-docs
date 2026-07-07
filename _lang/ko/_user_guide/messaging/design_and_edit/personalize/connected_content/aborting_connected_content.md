---
nav_title: 연결된 콘텐츠 중단
article_title: 연결된 콘텐츠 중단
page_order: 2
description: "이 참조 문서에서는 연결된 콘텐츠에 대한 메시지 중단 모범 사례를 다룹니다."
---

# 연결된 콘텐츠 중단 {#aborting-connected-content}

> Liquid 템플릿을 사용할 때 조건 로직으로 메시지를 중단할 수 있습니다. 이 페이지에서는 이를 수행할 때의 모범 사례를 다룹니다.

다음 예시에서 조건 `connected.recommendations.size < 5`와 `connected.foo.bar == nil`은 메시지가 중단되는 상황을 지정합니다.

{% raw %}
```
{% connected_content https://example.com/webservice.json :save connected %}
   {% if connected.recommendations.size < 5 or connected.foo.bar == nil %}
     {% abort_message() %}
   {% endif %}
```
{% endraw %}

## 중단 사유 지정 {#specify-an-abort-reason}

중단 사유를 지정할 수도 있으며, 이는 [메시지 활동 로그]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log)에 저장됩니다. 이 중단 사유는 문자열이어야 하며 Liquid를 포함할 수 없습니다.

{% raw %}
`{% abort_message('Could not get enough recommendations') %}`
{% endraw %}

{% alert important %}
Braze는 중단된 메시지를 Braze 계정 또는 Currents의 발송 수에 포함하지 않습니다.
{% endalert %}

{% multi_lang_include connected_content/abort_and_retry_logic.md %}