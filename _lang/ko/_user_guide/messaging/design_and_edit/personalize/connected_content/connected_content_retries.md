---
nav_title: 연결된 콘텐츠 재시도
article_title: 연결된 콘텐츠 재시도
page_order: 5
description: "이 참조 문서에서는 연결된 콘텐츠 재시도를 처리하는 방법을 다룹니다."

---

# 연결된 콘텐츠에 재시도 로직 사용하기 {#use-retry-logic-for-connected-content}

> 이 페이지에서는 연결된 콘텐츠 호출에 재시도를 추가하는 방법을 다룹니다.

## 재시도 작동 방식 {#how-retries-work}

연결된 콘텐츠는 API에서 데이터를 수신하는 것에 의존하기 때문에, Braze가 호출을 수행하는 동안 API를 일시적으로 사용할 수 없는 경우가 있습니다. 이 경우 Braze는 지수 백오프를 사용하여 요청을 다시 시도하는 재시도 로직을 지원합니다.

{% alert note %}
연결된 콘텐츠 `:retry`는 인앱 메시지에서 사용할 수 없습니다.
{% endalert %}

## 재시도 로직 사용하기 {#using-retry-logic}

재시도 로직을 사용하려면 다음 코드 스니펫과 같이 연결된 콘텐츠 호출에 `:retry` 태그를 추가합니다:

{% raw %}
```
{% connected_content https://yourwebsite.com/api/endpoint :retry %}
{% connected_content https://www.braze.com :save my_content :basic_auth auth_name :retry %}
```
{% endraw %}

연결된 콘텐츠 호출에 `:retry` 태그가 포함되면, Braze는 최대 5회까지 호출을 재시도합니다.

### 미리보기 동작 {#preview-behavior}

재시도 로직은 실시간 발송(테스트 발송 포함)에만 적용되며, 미리보기에는 적용되지 않습니다. `:retry`가 포함된 연결된 콘텐츠 호출이 미리보기 중에 실패하면, 콘텐츠를 렌더링하는 대신 "재시도 기능이 트리거되어 이 메시지가 표시되지 않았을 것입니다"라는 메시지가 미리보기에 표시될 수 있습니다. 이는 예상된 동작이며 Braze 내의 문제를 나타내는 것이 아닙니다.

### 재시도 성과 {#retry-outcomes}

#### 재시도가 성공한 경우 {#when-a-retry-succeeds}

재시도가 성공하면 메시지가 발송되며, 해당 메시지에 대해 더 이상 재시도가 시도되지 않습니다.

#### API 호출이 실패하고 재시도가 활성화된 경우 {#when-the-api-call-fails-and-retries-are-enabled}

API 호출이 실패하고 이 기능이 활성화된 경우, Braze는 각 재발송에 대해 설정한 [사용량 제한]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting)을 준수하면서 호출을 재시도합니다. Braze는 실패한 메시지를 대기줄 뒤로 이동시키고, 필요한 경우 메시지 발송에 소요되는 총 시간에 추가 시간을 더합니다.

연결된 콘텐츠 호출이 5회 이상 오류가 발생하면, [메시지 중단 태그]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/aborting_connected_content)가 트리거되는 것과 유사하게 메시지가 중단됩니다.

{% multi_lang_include connected_content/abort_and_retry_logic.md %}