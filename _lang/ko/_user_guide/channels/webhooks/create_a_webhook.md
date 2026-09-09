---
nav_title: 웹훅 생성
article_title: 웹훅 생성
page_order: 1
channel:
  - webhooks
description: "이 참조 문서에서는 웹훅 캠페인을 생성하고 구성하는 방법을 다룹니다."
search_rank: 2
---

# 웹훅 캠페인 생성 {#create-a-webhook-campaign}

> 웹훅 캠페인을 생성하거나 멀티채널 캠페인에 웹훅을 포함하면 다른 시스템 및 애플리케이션에 실시간 정보를 제공하여 앱 외부 동작을 트리거할 수 있습니다.

웹훅을 사용하여 Salesforce나 Marketo와 같은 시스템 또는 백엔드 시스템에 정보를 전송할 수 있습니다. 예를 들어, 고객이 커스텀 이벤트를 특정 횟수만큼 수행한 후 프로모션으로 고객 계정에 크레딧을 적립할 수 있습니다.

{% alert tip %}
웹훅이 무엇이며 Braze에서 어떻게 사용할 수 있는지 자세히 알아보려면 계속하기 전에 [웹훅]({{site.baseurl}}/user_guide/channels/webhooks)을 확인하세요.
{% endalert %}

## 1단계: 메시지를 작성할 위치 선택하기 {#step-1-choose-where-to-build-your-message}

메시지를 Campaign으로 보낼지 Canvas로 보낼지 잘 모르시겠나요? Campaigns는 단일하고 타겟팅된 메시징 캠페인에 적합하고, Canvases는 여러 단계로 이루어진 사용자 여정에 더 적합합니다.

{% tabs %}
{% tab Campaign %}

**단계:**

1. **메시징** > **Campaigns**로 이동하여 **Campaign 생성**을 선택합니다.
2. **웹훅**을 선택하거나, 여러 채널을 타겟팅하는 Campaigns의 경우 **멀티채널**을 선택합니다.
3. Campaign 이름을 명확하고 의미 있게 지정합니다.
4. (선택 사항) 이 Campaign의 사용 목적을 설명하는 설명을 추가합니다.
4. 필요에 따라 [팀]({{site.baseurl}}/user_guide/administer/global/user_management/teams) 및 [태그]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags)를 추가합니다.
   * 태그를 사용하면 Campaigns를 더 쉽게 찾고 보고서를 작성할 수 있습니다. 예를 들어, [보고서 빌더]({{site.baseurl}}/user_guide/analytics/reports/report_builder)를 사용할 때 특정 태그로 필터링할 수 있습니다.
5. Campaign에 필요한 만큼 배리언트를 추가하고 이름을 지정합니다. 추가된 각 배리언트에 대해 서로 다른 웹훅 템플릿을 선택할 수 있습니다. 이 주제에 대한 자세한 내용은 [다변량 및 A/B 테스트]({{site.baseurl}}/user_guide/messaging/ab_testing)를 참조하세요.

{% alert tip %}
Campaign의 모든 메시지가 유사하거나 동일한 콘텐츠를 포함할 경우, 추가 배리언트를 추가하기 전에 먼저 메시지를 작성하세요. 그런 다음 **배리언트 추가** 드롭다운에서 **배리언트에서 복사**를 선택할 수 있습니다.
{% endalert %}

{% endtab %}
{% tab Canvas %}

**단계:**

{% multi_lang_include messaging/canvas_message_step_setup.md %}

{% endtab %}
{% endtabs %}

## 2단계: 웹훅 작성하기 {#step-2-build-your-webhook}

웹훅을 처음부터 새로 만들거나, 기존 템플릿을 사용하거나, Braze에서 제공하는 기존 템플릿 중 하나를 사용할 수 있습니다. 그런 다음, 편집기의 **작성** 탭에서 웹훅을 작성합니다.

**작성** 탭은 다음 필드로 구성됩니다:

- 언어
- 웹훅 URL
- HTTP 메서드
- 요청 본문

![예제 웹훅 템플릿이 포함된 '작성' 탭.]({% image_buster /assets/img_archive/webhook_compose.png %})

### 언어 {#internationalization}

URL과 요청 본문에서 [국제화]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization)가 지원됩니다. 메시지를 국제화하려면 **언어 추가**를 선택하고 필수 필드를 입력합니다.

콘텐츠를 작성하기 전에 언어를 먼저 선택하여 Liquid에서 적절한 위치에 텍스트를 입력할 수 있도록 하는 것이 좋습니다. 사용 가능한 전체 언어 목록은 [지원 언어]({{site.baseurl}}/developer_guide/localization?tab=android)를 참조하세요.

오른쪽에서 왼쪽으로 쓰는 언어로 텍스트를 추가하는 경우, 오른쪽에서 왼쪽 방향 메시지의 최종 표시 형태는 서비스 제공업체의 렌더링 방식에 크게 좌우됩니다. 최대한 정확하게 표시되는 오른쪽에서 왼쪽 방향 메시지를 작성하기 위한 모범 사례는 [오른쪽에서 왼쪽 방향 메시지 작성하기]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages)를 참조하세요.

### 웹훅 URL {#webhook-url}

웹훅 URL 또는 HTTP URL은 엔드포인트를 지정합니다. 엔드포인트는 웹훅에서 캡처한 정보를 전송할 위치입니다.

벤더에게 정보를 전송하려는 경우, 벤더가 API 설명서에 이 URL을 제공해야 합니다. 자체 시스템으로 정보를 전송하는 경우, 개발 또는 엔지니어링 팀에 올바른 URL을 사용하고 있는지 확인하세요.

Braze에서는 표준 포트 `80`(HTTP) 및 `443`(HTTPS)을 통해 통신하는 URL만 허용합니다.

#### Liquid 사용하기 {#using-liquid}

[Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid)를 사용하여 웹훅 URL을 개인화할 수 있습니다. 경우에 따라 특정 엔드포인트에서 사용자를 식별하거나 URL의 일부로 사용자별 정보를 제공해야 할 수 있습니다. Liquid를 사용할 때는 URL에 사용하는 각 사용자별 정보에 대해 [기본값]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=web)을 포함해야 합니다.

### HTTP 메서드 {#http-method}

사용해야 하는 HTTP 메서드는 정보를 전송하는 엔드포인트에 따라 다릅니다. 대부분의 경우 POST를 사용합니다.

| HTTP 메서드 | 설명 |
| ----------- | ----------- |
| POST | 수신 서버에 새 정보를 기록합니다. 데이터를 전송할 때 가장 많이 사용되는 메서드입니다. |
| GET | 새 정보를 기록하는 것이 아니라 기존 정보를 검색합니다. 정의에 따라 GET 요청은 요청 본문을 지원하지 않습니다. |
| PUT | 엔드포인트의 정보를 업데이트하여 기존 정보를 요청 본문의 내용으로 교체합니다. |
| DELETE | HTTP URL의 리소스를 삭제합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="HTTP 메서드" }

### 요청 본문 {#request-body}

요청 본문은 지정한 URL로 전송될 정보입니다. JSON 키-값 페어 또는 원시 텍스트를 사용하여 웹훅 요청의 본문을 만들 수 있습니다.

#### JSON 키-값 페어 {#json-key-value-pairs}

JSON 키-값 페어를 사용하면 JSON 형식을 기대하는 엔드포인트에 대한 요청을 쉽게 작성할 수 있습니다. JSON 요청을 기대하는 엔드포인트에서만 사용할 수 있습니다. 예를 들어, 키가 `message_body`인 경우 해당 값은 `Your order just arrived!`일 수 있습니다. 키-값 페어를 입력하면 작성기가 JSON 구문으로 요청을 구성하며, JSON 요청의 미리보기가 자동으로 표시됩니다.

![JSON 키-값 페어로 설정된 요청 본문.]({% image_buster /assets/img/webhook_json_1.png %})

Liquid를 사용하여 키-값 페어를 개인화할 수 있으며, 사용자 속성, [커스텀 속성]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes?sdktab=swift) 또는 [이벤트 속성정보]({{site.baseurl}}/user_guide/data/activation/events/custom_events)를 요청에 포함할 수 있습니다. 예를 들어, 고객의 이름과 이메일을 요청에 포함할 수 있습니다. 각 속성에 대해 [기본값]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=web)을 포함해야 합니다.

#### 원시 텍스트 {#raw-text}

원시 텍스트 옵션은 모든 형식의 본문을 기대하는 엔드포인트에 대한 요청을 작성할 수 있는 유연성을 제공합니다. 예를 들어, XML 형식의 요청을 기대하는 엔드포인트에 대한 요청을 작성하는 데 사용할 수 있습니다.

원시 텍스트에서는 Liquid를 사용한 [개인화]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid)와 [국제화]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization)가 모두 지원됩니다.

![Liquid를 사용한 원시 텍스트 요청 본문의 예시.]({% image_buster /assets/img_archive/webhook_rawtext.png %})

`Content-Type` [요청 헤더](#request-headers-optional)를 `application/x-www-form-url-encoded`로 설정하는 경우, 요청 본문은 URL 인코딩된 문자열로 포맷되어야 합니다. 예를 들어:

{% raw %}
```
to={{custom_attribute.${example}}}&text=Your+order+just+arrived
```
{% endraw %}

![URL 인코딩된 문자열이 포함된 요청 본문.]({% image_buster /assets/img_archive/webhook_rawtext_URL-encoded.png %})

## 3단계: 추가 설정 구성 {#step-3-configure-additional-settings}

### 요청 헤더 (선택 사항) {#request-headers-optional}

일부 엔드포인트는 요청에 헤더를 포함해야 할 수 있습니다. 작성기의 **작성** 섹션에서 필요한 만큼 헤더를 추가할 수 있습니다.

!["Authorization" 키와 "Content-type" 키에 대한 요청 헤더 예시.]({% image_buster /assets/img_archive/webhook_request_headers_example.png %})

일반적인 요청 헤더에는 [`Content-Type`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Type) 사양(본문에서 예상할 데이터 유형(예: XML 또는 JSON)을 설명)과 공급업체 또는 시스템에 대한 자격 증명을 포함하는 [`Authorization`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization) 헤더가 있습니다.

{% alert note %}
HTTP 헤더 이름은 [RFC 7230, 섹션 3.2("각 헤더 필드는 대소문자를 구분하지 않는 필드 이름으로 구성된다")](https://datatracker.ietf.org/doc/html/rfc7230#section-3.2)에 따라 대소문자를 구분하지 않습니다. 수신 엔드포인트나 중간 서비스(예: CDN)가 헤더 대소문자를 변환하더라도 헤더 처리에 영향을 주지 않습니다. `Content-Type`, `content-type`, `CONTENT-TYPE`은 모두 동일하게 처리됩니다.
{% endalert %}

콘텐츠 유형 사양은 `Content-Type` 키를 사용해야 합니다. 일반적인 값은 `application/json` 또는 `application/x-www-form-urlencoded`입니다.

인증 헤더는 `Authorization` 키를 사용해야 합니다. 일반적인 값은 {% raw %} `Bearer {{YOUR_TOKEN}}` 또는 `Basic {{YOUR_TOKEN}}` {% endraw %}이며, 여기서 `YOUR_TOKEN`은 공급업체 또는 시스템에서 제공하는 자격 증명입니다.

## 4단계: 메시지 테스트 전송 {#step-4-test-send-your-message}

Campaign을 라이브로 전환하기 전에 Braze에서는 웹훅을 테스트하여 요청이 올바르게 포맷되었는지 확인할 것을 권장합니다.

이렇게 하려면 **테스트** 탭으로 전환하여 테스트 웹훅을 보내세요. 무작위 사용자, 특정 사용자(이메일 주소 또는 외부 사용자 ID 입력), 또는 원하는 속성을 가진 커스텀 사용자로 웹훅을 테스트할 수 있습니다.

테스트 웹훅을 보낸 후 응답 메시지가 포함된 대화 상자가 나타납니다. 웹훅 요청이 실패한 경우 오류 메시지를 참조하여 웹훅 문제를 해결하세요. 다음 예시는 잘못된 웹훅 URL이 포함된 웹훅의 응답을 보여줍니다.

```http
404 Not Found

{
  "error": {
    "message": "Unrecognized request URL. Please see https://lob.com/docs or email us at support@lob.com.",
    "status_code": 404
  }
}

```

자세한 내용은 [테스트 메시지 보내기]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=webhook)를 참조하세요.

## 5단계: Campaign 또는 Canvas의 나머지 부분 구성 {#step-5-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab Campaign %}

다음으로 Campaign의 나머지 부분을 구성합니다. 웹훅을 구성하기 위해 도구를 가장 잘 활용하는 방법에 대한 자세한 내용은 다음 섹션을 참조하세요.

### 전달 스케줄 또는 트리거 선택 {#choose-delivery-schedule-or-trigger}

웹훅은 예약된 시간, 실행 또는 API 트리거를 기반으로 전달할 수 있습니다. 자세한 내용은 [Campaign 스케줄링]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign)을 참조하세요.

실행 기반 전달의 경우 Campaign 기간 및 [방해금지 시간]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours)을 설정할 수도 있습니다.

이 단계에서는 사용자가 Campaign을 [다시 수신할 수 있도록]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility#turning-on-re-eligibility) 허용하거나 [최대 게재빈도 설정]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#about-frequency-capping) 규칙을 활성화하는 등 전달 제어를 지정할 수도 있습니다.

### 타겟 사용자 선택 {#choose-users-to-target}

다음으로 Segment 또는 필터를 선택하여 오디언스 범위를 좁혀 [사용자를 타겟팅]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users)해야 합니다. 이 단계에서는 Segment에서 더 넓은 오디언스를 선택한 다음 필요에 따라 필터를 사용하여 해당 Segment를 더 좁힐 수 있습니다. 대략적인 Segment 인구의 미리보기가 자동으로 표시됩니다. 정확한 Segment 멤버십은 항상 메시지가 전송되기 전에 계산된다는 점을 유의하세요.

{% multi_lang_include audience/target_audiences.md %}

### 전환 이벤트 선택 {#choose-conversion-events}

Braze에서는 사용자가 Campaign을 수신한 후 특정 행동인 [전환 이벤트]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events)를 얼마나 자주 수행하는지 추적할 수 있습니다. 사용자가 지정된 행동을 취할 경우 전환이 집계되는 최대 30일의 기간을 설정할 수 있습니다.

{% endtab %}

{% tab Canvas %}

아직 완료하지 않았다면 Canvas 단계의 나머지 섹션을 완료하세요. 다변량 테스트 및 [BrazeAI<sup>TM</sup>로 최적화]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#optimize-canvas-variants-with-brazeai)를 포함하여 Canvas의 나머지 부분을 구성하는 방법에 대한 자세한 내용은 [Canvas 구성]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-2-build-your-canvas)을 참조하세요.

{% endtab %}
{% endtabs %}

## 6단계: 검토 및 배포 {#step-6-review-and-deploy}

Campaign 또는 Canvas의 마지막 구성을 완료한 후 세부 사항을 검토하고, 테스트한 다음, 전송하세요!

## 알아야 할 사항 {#things-to-know}

### 오류, 재시도 로직 및 시간 초과 {#errors-retry-logic-and-timeouts}

웹훅은 Braze 서버가 외부 엔드포인트에 요청을 보내는 방식에 의존하며, 간혹 오류가 발생할 수 있습니다. 가장 흔한 오류로는 구문 오류, 만료된 API 키, 사용량 제한, 예기치 않은 서버 측 문제 등이 있습니다. 웹훅 Campaign을 보내기 전에:

- 웹훅에 구문 오류가 없는지 테스트하세요
- 개인화된 변수에 기본값이 있는지 확인하세요

웹훅 전송에 실패하면 [메시지 활동 로그]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log)에 오류 메시지가 기록되며, 오류 타임스탬프, 앱 이름, 오류에 대한 세부 정보가 포함됩니다.

![현재 사용자에 대한 정보를 쿼리하려면 활성 액세스 토큰을 사용해야 한다는 메시지가 표시된 웹훅 오류.]({% image_buster /assets/img_archive/webhook-error.png %})

오류 메시지가 오류의 원인에 대해 충분히 명확하지 않은 경우, 사용 중인 API 엔드포인트의 설명서를 확인해야 합니다. 이러한 설명서에는 일반적으로 엔드포인트가 사용하는 오류 코드에 대한 설명과 그 원인이 포함되어 있습니다.

#### 응답 코드 및 재시도 로직 {#response-codes-and-retry-logic}

웹훅 요청이 전송되면 수신 서버는 요청에 대해 어떤 일이 발생했는지를 나타내는 응답 코드를 반환합니다. 다음 표에는 서버가 보낼 수 있는 다양한 응답, Campaign 분석에 미치는 영향, 오류가 발생한 경우 Braze가 Campaign 재전달을 시도하는지 여부가 요약되어 있습니다.

| 응답 코드 | 수신으로 표시? | 재시도? |
|---------------|-----------|----------|
| `20x` (성공)  | 예 |   해당 없음  |
| `30x` (리디렉션)  | 아니요 | 아니요 |
| `408` (요청 시간 초과)  | 아니요 | 예 |
| `429` (사용량 제한 초과)  | 아니요 | 예 |
| `기타 4XX` (클라이언트 오류)  | 아니요 | 아니요 |
| `5XX` (서버 오류)   | 아니요 | 예 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="응답 코드 및 재시도 로직" }

{% alert note %}
Braze는 이 섹션의 재시도 가능한 상태 코드에 대해 최대 5회(초기 요청 1회와 재시도 4회)까지 시도하며, 시도 간 대기 시간이 점차 늘어납니다. Braze가 엔드포인트에 도달할 수 없는 경우, 재시도는 최대 24시간 동안 계속될 수 있습니다.<br><br>각 웹훅 요청은 시간 초과되기 전까지 120초가 허용됩니다.
{% endalert %}

`Retry-After` 및 사용량 제한 응답 헤더는 Braze가 **재시도 가능한** 시도 전에 대기하는 시간에 영향을 줄 수 있습니다(예: `408`, `429`, 또는 `5XX` 이후). 이 헤더는 `401`과 같은 재시도 불가능한 응답을 재시도 대상으로 만들지는 않습니다.

<!-- support-analyzer-phase2:webhook_delivery_failures -->
{% alert note %}
분석에서 웹훅 전송이 누락된 것으로 보이는 경우, 해당 Campaign 또는 Canvas 단계의 [메시지 활동 로그]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log)를 확인하세요. Braze는 특정 응답(`408`, `429`, `5XX` 등)만 재시도하며, `401 Unauthorized`를 포함한 대부분의 다른 `4XX` 클라이언트 오류는 재시도되지 **않습니다**. 전체 응답 표는 [응답 코드 및 재시도 로직](#response-codes-and-retry-logic)을 참조하세요.
{% endalert %}


#### 403 Forbidden 및 IP 허용 목록 {#403-forbidden-and-ip-allowlisting}

`403 Forbidden` 응답은 엔드포인트가 요청을 수신했지만 거부했음을 의미합니다. 일반적인 원인에는 잘못되었거나 누락된 인증, 불충분한 API 권한, Braze의 아웃바운드 IP 주소를 차단하는 네트워크 규칙(예: 방화벽 또는 웹 애플리케이션 방화벽) 등이 있습니다.

웹훅 요청이 지속적으로 `403`을 반환하고 인증 헤더가 올바른 경우, 웹훅을 수신하는 서버에서 해당 클러스터의 Braze IP를 허용 목록에 추가하세요. [IP 허용 목록](#ip-allowlisting)을 참조하세요. 연결된 콘텐츠 요청은 동일한 아웃바운드 IP를 사용합니다. [연결된 콘텐츠 IP 허용 목록]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call#connected-content-ip-allowlisting)을 참조하세요.

기타 `4XX` 문제 해결 단계는 [웹훅 및 연결된 콘텐츠 요청 문제 해결]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/troubleshooting_webhooks_and_connected_content#4xx-errors)을 참조하세요.

#### 인증 및 연결된 콘텐츠 자격 증명 {#authentication-and-connected-content-credentials}

아웃바운드 웹훅 HTTP 요청은 엔드포인트에 대해 인증하기 위한 [연결된 콘텐츠 자격 증명]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call#authentication-types)(`:basic_auth` 또는 `:auth_credentials`)의 첨부를 지원하지 않습니다. 대신 웹훅의 **요청 헤더**를 사용하여 인증을 설정하세요. 전송 시점에 토큰이나 시크릿을 가져오려면 헤더 또는 본문 필드에 {% raw %}`{% connected_content %}`{% endraw %} 태그를 배치하여 웹훅이 전송되기 전에 Liquid가 이를 처리하도록 할 수 있습니다.

#### 저장된 웹훅 템플릿 및 Campaign 사용 {#saved-webhook-templates-and-campaign-usage}

Braze는 지정된 **저장된 웹훅 템플릿**을 참조하는 모든 Campaign 또는 Canvas 단계를 나열하는 기본 보고서를 제공하지 않습니다. 사용 현황을 감사하려면 동일한 URL과 HTTP 메서드를 사용하는 웹훅 단계를 검토하거나 [Braze 지원팀]({{site.baseurl}}/support_contact)에 문의하세요.

#### 문제 해결 및 추가 오류 세부 정보 {#troubleshooting-and-additional-error-details}

자세한 설명, 문제 해결 단계, 특정 웹훅 오류 해결에 대한 안내는 [웹훅 및 연결된 콘텐츠 요청 문제 해결]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/troubleshooting_webhooks_and_connected_content)을 참조하세요. 비정상 호스트 감지 시스템의 작동 방식과 Braze가 자동 이메일 및 Braze Currents의 추가 로깅을 통해 오류 알림을 제공하는 방법에 대한 자세한 설명도 확인할 수 있습니다.

### IP 허용 목록 {#ip-allowlisting}

Braze에서 웹훅이 전송되면 Braze 서버는 고객 또는 서드파티 서버에 네트워크 요청을 보냅니다. IP 허용 목록을 사용하면 웹훅 요청이 Braze에서 오는 것인지 확인할 수 있어 보안 계층이 추가됩니다.

Braze는 다음 IP에서 웹훅을 전송합니다. 나열된 IP는 허용 목록에 옵트인된 모든 API 키에 자동으로 동적 추가됩니다.

{% alert important %}
Braze 간 웹훅을 만들고 허용 목록을 사용하는 경우, `127.0.0.1`을 포함한 다음 모든 IP를 허용 목록에 추가해야 합니다.
{% endalert %}

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

### 사용자 삭제 {#delete-users}

개별 사용자 또는 사용자 Segment를 삭제하려면 **오디언스** > **오디언스 관리** > **사용자 삭제**로 이동하세요. 대시보드는 대량 Segment 삭제(최대 1,000만 프로필)를 지원하며, 7일 취소 기간이 포함되어 있고, 공유 REST API 사용량 제한을 소모하지 않습니다. 단계, 제한 및 권한에 대해서는 [사용자 삭제]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles/delete_users)를 참조하세요.

더 작은 배치로 프로그래밍 방식의 삭제를 수행하려면 웹훅 Campaign 대신 [`/users/delete` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_delete)를 사용하세요.