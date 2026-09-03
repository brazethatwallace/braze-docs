---
nav_title: 연결된 콘텐츠 디버거
article_title: 연결된 콘텐츠 디버거
page_order: 3.5
description: "이 참고 문서에서는 메시지를 발송하기 전에 연결된 콘텐츠 디버거를 사용하여 문제를 해결하는 방법을 다룹니다."
---

# 연결된 콘텐츠 디버거 {#connected-content-debugger}

> 연결된 콘텐츠 디버거를 사용하면 각 연결된 콘텐츠 호출에 대한 실시간 요청 및 응답을 확인할 수 있으므로, Campaign 또는 Canvas를 시작하기 전에 엔드포인트, 헤더, Liquid 태그를 검증할 수 있습니다.

## 디버거 소개 {#about-the-debugger}

연결된 콘텐츠를 사용하면 렌더링 시점에 외부 API로 HTTP 호출을 수행하여 실시간 데이터로 메시지를 보강한 다음, Liquid를 사용해 응답을 메시지에 삽입할 수 있습니다. 이 호출은 Braze 외부에서 이루어지기 때문에, Campaign 또는 Canvas가 라이브 상태가 되기 전에 Braze가 보낸 요청, 엔드포인트가 반환한 결과, 또는 호출이 실패한 이유를 정확히 확인하기 어려울 수 있습니다.

연결된 콘텐츠 디버거는 이러한 문제를 출시 전에 해결할 수 있도록 도와줍니다. **미리보기 및 테스트** 섹션에서 메시지의 모든 연결된 콘텐츠 호출에 대한 실시간 요청 및 응답을 표시합니다. 이를 통해 엔드포인트, 헤더, Liquid 태그가 모두 Braze 대시보드 내에서 올바르게 구성되었는지 확인할 수 있습니다.

### 지원 영역 {#supported-areas}

연결된 콘텐츠 디버거는 다음 영역에서 사용할 수 있습니다.

- Canvas Context 단계
- Content Cards
- 이메일
    - 템플릿 포함
    - 푸터 및 구독 페이지 제외
- In-App Messages
- 푸시 알림
- SMS/MMS/RCS
- 웹훅
    - 템플릿 포함
- WhatsApp

{% alert note %}
디버거는 대부분의 채널에서 사용할 수 있지만, KakaoTalk, LINE, 배너 또는 채널에 한정되지 않는 작성 영역(예: Content Blocks 및 Canvas 사용자 업데이트 단계)에서는 아직 지원되지 않습니다. 디버거가 보이지 않는다면, 해당 기능에서 연결된 콘텐츠 디버깅이 아직 지원되지 않을 수 있습니다.
{% endalert %}

## 디버거 사용하기 {#use-the-debugger}

미리보기를 실행할 때마다 Braze는 **미리보기** 탭에 연결된 콘텐츠 호출 결과를 자동으로 렌더링합니다. 디버거를 사용하려면:

1. {% raw %}`{% connected_content %}`{% endraw %} 태그로 메시지를 구성합니다.
2. **미리보기 및 테스트** 섹션으로 이동합니다. 메시지에 연결된 콘텐츠 태그가 포함되어 있으면 연결된 콘텐츠 호출 수와 성공 및 오류 상태를 요약 보기로 확인할 수 있습니다.

![테스트 섹션의 연결된 콘텐츠 영역.]({% image_buster /assets/img/connected_content/debugger1.png %})

{:start="3"}
3. **세부 정보 보기**를 선택하여 미리보기 옆에 디버거를 엽니다. 드로어에는 각 연결된 콘텐츠 호출의 URL과 결과가 테이블로 표시됩니다.

![검토할 세 개의 URL이 있는 연결된 콘텐츠 호출.]({% image_buster /assets/img/connected_content/debugger3.png %})

{:start="4"}
4. 각 URL 및 결과 옆에서 **보기**를 선택하여 요청 및 응답 헤더, 페이로드, 메서드, 소요 시간, 캐싱 정보를 확인합니다.

![요청 및 응답 세부 정보가 포함된 연결된 콘텐츠 호출.]({% image_buster /assets/img/connected_content/debugger4.png %})

{:start="5"}
5. 결과를 검토하고 필요에 따라 태그, 헤더 또는 엔드포인트를 조정합니다. 그런 다음 새 미리보기를 생성하여 수정 사항을 확인합니다.

템플릿에 {% raw %}`{% connected_content %}`{% endraw %} 태그가 두 개 이상 포함된 경우, 디버거는 수행된 모든 호출을 목록으로 표시합니다. 하나의 템플릿에서 여러 메시지 본문을 렌더링하는 채널(예: HTML, 일반 텍스트, AMP 본문을 각각 렌더링하는 이메일, 또는 기기별 본문을 각각 렌더링하는 Quick Push)의 경우, 디버거는 현재 미리보고 있는 본문뿐만 아니라 모든 본문에서 이루어진 연결된 콘텐츠 호출을 전부 표시합니다.

## 디버그 출력 이해하기 {#understand-the-debug-output}

각 연결된 콘텐츠 호출은 자체 **Response** 탭과 **Request** 탭으로 표시됩니다. **Response** 탭은 호출 성공 여부를 확인하는 첫 번째 지표이므로 기본적으로 표시됩니다.

### URL 세부 정보 {#url-details}

| 필드 | 설명 |
| --- | --- |
| URL | Braze가 호출한 완전히 렌더링된 URL로, 모든 Liquid 태그가 해석된 상태입니다. |
| Method | 사용된 HTTP 메서드(GET 또는 POST)입니다. |
| Status code | 엔드포인트가 반환한 HTTP 상태 코드입니다(예: `200`, `404`, `500`). Braze 전용 코드에 대해서는 [응답 코드 문제 해결](#troubleshooting-response-codes)을 참고하세요. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="URL 세부 정보" }

### Response 탭 {#response-tab}

| 필드 | 설명 |
| --- | --- |
| Duration | 요청이 완료되기까지 걸린 시간(초)입니다. Duration은 실시간(캐시되지 않은) 호출에 대해서만 표시됩니다. |
| Served from cache | 이 응답이 엔드포인트에 대한 실시간 호출이 아닌 Braze의 연결된 콘텐츠 캐시에서 제공되었는지 여부를 나타냅니다(`Yes` 또는 `No`). 캐시된 결과는 이전 응답을 반영하며, 반드시 엔드포인트의 현재 상태를 나타내지는 않습니다. |
| Response body | 엔드포인트가 반환한 응답 본문입니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Response 탭" }

### Request 탭 {#request-tab}

| 필드 | 설명 |
| --- | --- |
| Headers | 연결된 콘텐츠 태그의 헤더입니다(`:headers`, 자격 증명, `:content_type` 등의 옵션). |
| Body | 전송된 요청 본문입니다(POST 요청인 경우). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Request 탭" }

## 디버거에 표시되는 요청 헤더 {#which-request-headers-appear-in-the-debugger}

**Request** 탭에는 연결된 콘텐츠 태그의 헤더가 나열됩니다: 커스텀 `:headers`, 저장된 자격 증명, 그리고 `:content_type` 및 `:basic_auth`와 같은 태그 옵션으로 설정된 헤더가 포함됩니다. Braze는 엔드포인트로 보내는 발신 요청에 표준 헤더(예: `User-Agent` 및 `Host`)도 추가합니다. 이러한 Braze가 추가한 헤더는 `:headers`에서 설정한 경우 디버거에 표시됩니다.

{% alert note %}
일관된 `User-Agent`를 보내려면 `:headers`에서 설정하세요. Braze는 사용자가 설정한 값을 사용하며, 디버거에 해당 헤더가 표시됩니다.
{% endalert %}

{% multi_lang_include connected_content/outgoing_request_headers.md %}

## 자격 증명 수정 {#credential-redaction}

연결된 콘텐츠 태그에서 `:basic_auth`, 일반적인 시크릿 헤더, 키 또는 기타 [인증 자격 증명 옵션]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call#authentication-types)을 사용하는 경우, 디버거는 **Request** 탭에서 해당 값을 수정하고 일련의 별표(*)로 대체합니다. 이를 통해 **미리보기 및 테스트**에서 값을 노출하지 않으면서도 요청에 자격 증명이 포함되었는지 확인할 수 있습니다.

자격 증명이 수정된 경우에도 인증 실패는 여전히 표시됩니다. 엔드포인트가 `401` 또는 `403`을 반환하면, 해당 상태 코드가 **Response** 탭에 정상적으로 표시되므로 자격 증명 자체는 숨겨져 있더라도 인증 문제로 인해 요청이 거부되었음을 확인할 수 있습니다.

## 응답 코드 문제 해결 {#troubleshooting-response-codes}

### 엔드포인트 오류와 Braze가 부과하는 제한 {#endpoint-errors-versus-braze-imposed-limits}

**Response** 탭에 표시되는 `2XX`가 아닌 상태 코드가 모두 엔드포인트에서 발생하는 것은 아닙니다. Braze는 연결된 콘텐츠 호출에 자체 제한을 적용하며, 이러한 제한으로 인해 엔드포인트 오류와 유사하게 보이는 응답이 생성될 수 있습니다.

`408`, `429`, `502`, `503`, `504`, `599`와 같은 [응답 코드]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/troubleshooting_webhooks_and_connected_content#start-here-match-your-symptom)가 표시되면, 일반적으로 호스트 상태, 타임아웃 또는 페이로드 크기와 관련된 Braze 측 호출 문제입니다. 엔드포인트가 지속적으로 큰 응답을 반환하는 경우, 메시지에 필요한 필드만 포함하도록 응답 페이로드를 축소하는 것을 고려하세요.

### 엔드포인트가 예상치 못한 상태 코드를 반환한 경우 {#endpoint-returned-an-unexpected-status-code}

**Request** 탭을 사용하여 URL, 태그의 헤더, 본문을 확인하세요. 예상치 못한 `4XX` 응답의 일반적인 원인은 URL, 헤더 또는 본문 내의 Liquid 태그가 예상대로 해석되지 않는 것입니다. {% raw %}`{{ }}`{% endraw %} 참조가 미리보기 중인 사용자 또는 컨텍스트에 존재하는 필드를 가리키고 있는지 확인하세요.

### 응답이 오래된 것으로 보이는 경우 {#response-looks-stale}

**Response** 탭에서 **Served from cache**를 확인하세요. `Yes`로 표시되면, 디버거가 새로운 호출이 아닌 이전에 캐시된 응답을 보여주고 있는 것입니다. 현재 엔드포인트 동작을 확인하려면 태그에 임시로 `:no_cache`를 추가하거나, 캐시가 만료될 때까지(`:cache_max_age` 기준) 기다리세요.

## 관련 문서 {#related-articles}

- [연결된 콘텐츠 참조]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content)
- [연결된 콘텐츠 API 호출하기]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call)
- [발신 요청 헤더]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call#outgoing-request-headers)
- [웹훅 및 연결된 콘텐츠 요청 문제 해결]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/troubleshooting_webhooks_and_connected_content)