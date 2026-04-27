---
nav_title: 연결된 콘텐츠 재시도
article_title: 연결된 콘텐츠 재시도
page_order: 5
description: "이 참조 문서에서는 연결된 콘텐츠 재시도를 처리하는 방법을 다룹니다."

---

# 연결된 콘텐츠에 재시도 로직 사용하기

> 이 페이지에서는 연결된 콘텐츠 호출에 재시도를 추가하는 방법을 다룹니다.

## 재시도 작동 방식

연결된 콘텐츠는 API에서 데이터를 수신하는 것에 의존하기 때문에, Braze가 호출을 수행하는 동안 API가 간헐적으로 사용 불가능할 수 있습니다. 이 경우 Braze는 지수 백오프를 사용하여 요청을 재시도하는 재시도 로직을 지원합니다.

{% alert note %}
연결된 콘텐츠 `:retry`는 인앱 메시지에서 사용할 수 없습니다.
{% endalert %}

## 재시도 로직 사용하기

재시도 로직을 사용하려면 다음 코드 스니펫에 표시된 것처럼 연결된 콘텐츠 호출에 `:retry` 태그를 추가합니다:

{% raw %}
```
{% connected_content https://yourwebsite.com/api/endpoint :retry %}
{% connected_content https://www.braze.com :save my_content :basic_auth auth_name :retry %}
```
{% endraw %}

연결된 콘텐츠 호출에 `:retry` 태그가 포함되면, Braze는 최대 5회까지 호출을 재시도합니다.

### 재시도 결과

#### 재시도가 성공한 경우

재시도가 성공하면 메시지가 전송되며, 해당 메시지에 대해 더 이상 재시도가 시도되지 않습니다.

#### API 호출이 실패하고 재시도가 활성화된 경우

API 호출이 실패하고 이 기능이 활성화된 경우, Braze는 각 재전송에 대해 설정한 [사용량 제한]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/#delivery-speed-rate-limiting)을 준수하면서 호출을 재시도합니다. Braze는 실패한 메시지를 대기줄의 뒤로 이동시키고, 필요한 경우 귀하의 메시지를 전송하는 데 걸리는 총 시간에 추가 시간을 더합니다.

연결된 콘텐츠 호출이 5회 이상 오류가 발생하면, [메시지 중단 태그]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/aborting_connected_content/)가 트리거되는 것과 유사하게 메시지가 중단됩니다.

{% multi_lang_include connected_content/abort_and_retry_logic.md %}