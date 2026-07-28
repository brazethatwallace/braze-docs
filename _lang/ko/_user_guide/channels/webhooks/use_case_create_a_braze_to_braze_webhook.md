---
nav_title: "사용 사례: Braze-to-Braze 웹훅 생성"
article_title: "사용 사례: Braze-to-Braze 웹훅 생성"
page_order: 2
channel:
  - webhooks
description: "이 참조 문서에서는 사용자 업데이트와 Braze-to-Braze 웹훅을 각각 언제 사용해야 하는지, 그리고 Braze-to-Braze 웹훅을 생성하는 방법을 다룹니다."

---

# Braze-to-Braze 웹훅 생성 {#create-a-braze-to-braze-webhook}

> Braze-to-Braze 웹훅을 사용하면 [Campaign]({{site.baseurl}}/user_guide/messaging/canvas) 또는 [Canvas]({{site.baseurl}}/user_guide/messaging/campaigns)의 [웹훅]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook)을 통해 Braze 내에서 [Braze REST API]({{site.baseurl}}/api/basics)를 호출할 수 있습니다. [API 트리거 Canvas]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases)를 트리거하는 등의 오케스트레이션 작업에 활용할 수 있습니다. Canvas에서 [사용자 속성]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes), [커스텀 이벤트]({{site.baseurl}}/user_guide/data/activation/events/custom_events) 또는 [구매]({{site.baseurl}}/user_guide/data/activation/events/purchase_events)를 업데이트하려면 대신 [사용자 업데이트]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update)를 사용하세요. 사용자 업데이트는 고객 프로필 변경에 최적화되어 있으며 업데이트를 더 효율적으로 처리합니다.

이 문서를 최대한 활용하려면 [웹훅의 작동 방식]({{site.baseurl}}/user_guide/channels/webhooks)과 Braze에서 [웹훅을 생성하는 방법]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook)에 익숙해야 합니다.

## 다른 Canvas를 트리거하려면 Send to Destination 사용 {#use-send-to-destination-for-triggering-another-canvas}

Canvas 내에서 두 번째 Canvas를 트리거하려면 Braze-to-Braze 웹훅 대신 [Send to Destination]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/send_to_destination)을 사용하세요. 이 캔버스 구성요소는 Canvas 여정을 연결하기 위해 특별히 설계되었으며, 한 Canvas에서 다른 Canvas로 사용자를 보내는 더 간단하고 효율적인 방법을 제공합니다.

Send to Destination은 사용자가 해당 단계에 도달할 때 대상 Canvas의 진입 및 오디언스 기준에 따라 사용자를 평가하며, 웹훅 구성이나 API 키가 필요하지 않습니다. 기준을 충족하는 사용자는 대상 Canvas에 진입하며, 이후 추가 단계가 있는 경우 소스 Canvas에서 여정을 계속할 수 있습니다.

{% alert tip %}
Canvas에 [Send to Destination]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/send_to_destination)을 추가하여 웹훅이나 API 호출을 구성하지 않고도 사용자를 다른 Canvas 여정으로 보낼 수 있습니다.
{% endalert %}

## 사용자 데이터 변경에는 사용자 업데이트 사용 {#use-user-update-for-user-data-changes}

Canvas 내에서 고객 프로필을 업데이트하려면([커스텀 속성]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes) 수정, [커스텀 이벤트]({{site.baseurl}}/user_guide/data/activation/events/custom_events) 기록, [구매]({{site.baseurl}}/user_guide/data/activation/events/purchase_events) 기록 포함) Braze-to-Braze 웹훅 대신 [사용자 업데이트]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update)를 사용하세요.

사용자 업데이트는 여러 변경 사항을 그룹화하여 일괄 전송하므로 웹훅보다 빠릅니다. 웹훅보다 설정이 간편하며 [고급 JSON 작성기]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update#advanced-json-editor)를 통해 복잡한 업데이트도 지원합니다. 예를 들어, 사용자가 메시지를 본 횟수를 카운트하려면 Braze-to-Braze 웹훅 대신 사용자 업데이트의 [증가 및 감소 기능]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update#increasing-and-decreasing-values)을 사용하세요.

{% alert tip %}
Canvas에 [사용자 업데이트]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update)를 추가하여 JSON 작성기를 사용해 사용자의 속성, 이벤트, 구매를 업데이트할 수 있습니다.
{% endalert %}

## Braze-to-Braze 웹훅을 사용해야 하는 경우 {#when-to-use-a-braze-to-braze-webhook}

사용자 업데이트는 고객 프로필 업데이트를 위해 Braze-to-Braze 웹훅이 수행하는 거의 모든 작업을 처리할 수 있습니다. 단순한 커스텀 속성을 넘어서는 복잡한 업데이트의 경우 [고급 JSON 작성기]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update#advanced-json-editor)를 사용할 수 있습니다.

Send to Destination은 웹훅 구성 없이 Canvas 내에서 두 번째 Canvas를 트리거하는 더 간단한 방법을 제공합니다.

전용 캔버스 구성요소가 없는 시나리오에서 Braze 내에서 Braze의 [REST API]({{site.baseurl}}/api/basics)를 호출해야 하는 경우 Braze-to-Braze 웹훅을 사용할 수 있습니다. 일반적인 예시는 다음과 같습니다:

- Canvas에서 [API 트리거 Campaign]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns)을 트리거하는 경우
- Braze의 한 워크플로가 전용 캔버스 구성요소가 없는 API를 호출해야 하는 오케스트레이션 패턴을 위해 다른 [메시징 엔드포인트]({{site.baseurl}}/api/endpoints/messaging)를 호출하는 경우

Canvas 내에서 사용자를 업데이트하려면 [사용자 업데이트]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update)를 사용하세요. 다른 Canvas를 트리거하려면 [Send to Destination]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/send_to_destination)을 사용하세요.

## 필수 조건 {#prerequisites}

Braze-to-Braze 웹훅을 생성하려면 호출하려는 엔드포인트에 대한 권한이 있는 [API 키]({{site.baseurl}}/api/api_key)가 필요합니다. 예를 들어, API 트리거 Canvas를 트리거하려면 `canvas.trigger.send` 권한이 있는 API 키가 필요합니다.

## Braze-to-Braze 웹훅 설정 {#setting-up-your-braze-to-braze-webhook}

Braze-to-Braze 웹훅을 생성하는 일반적인 워크플로는 다음 단계를 따릅니다:

1. Campaign 또는 캔버스 구성요소로 [웹훅을 생성]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook)합니다.
2. **빈 템플릿**을 선택합니다.
3. **작성** 탭에서 API 사용 사례에 맞는 **웹훅 URL**과 **요청 본문**을 지정합니다.
4. **설정** 탭에서 엔드포인트에서 요구하는 **HTTP 메서드**와 **요청 헤더**를 지정합니다.
5. 추가 전달 설정(예: 커스텀 이벤트에서 트리거)을 구성하고 나머지 Campaign 또는 Canvas를 구축합니다.

## 초기 Canvas에서 두 번째 Canvas 트리거 {#trigger-a-second-canvas-from-an-initial-canvas}

이 사용 사례에서는 두 개의 Canvas를 생성하고 Braze-to-Braze 웹훅을 사용하여 첫 번째 Canvas에서 두 번째 Canvas를 트리거합니다. 이는 사용자가 다른 Canvas의 특정 지점에 도달했을 때의 진입 트리거 역할을 합니다.

{% alert note %}
**캔버스 단계와 상호작용** 트리거는 Campaign에서만 사용할 수 있으며, 액션 기반 Canvas 진입에는 사용할 수 없습니다. 사용자가 다른 Canvas의 특정 단계에 도달하는 것을 기반으로 Canvas를 트리거해야 하는 경우, 이 Braze-to-Braze 웹훅 방식 또는 [Send to Destination]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/send_to_destination) 캔버스 구성요소를 사용하세요.
{% endalert %}

1. 먼저 두 번째 Canvas, 즉 초기 Canvas에 의해 트리거될 Canvas를 생성합니다.
2. Canvas **진입 스케줄**에서 **API-Triggered**를 선택합니다.
3. **Canvas ID**를 메모해 두세요. 이후 단계에서 필요합니다.
4. 두 번째 Canvas의 단계를 계속 구축한 다음 Canvas를 저장합니다.
5. 마지막으로 첫 번째 Canvas를 생성합니다. 두 번째 Canvas를 트리거하려는 단계를 찾아 웹훅이 포함된 새 단계를 생성합니다.

웹훅을 구성할 때 다음을 참조하세요:

- **웹훅 URL:** [REST 엔드포인트 URL]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints) 뒤에 `/canvas/trigger/send`를 추가합니다. 예를 들어, `US-06` 인스턴스의 경우 URL은 `https://rest.iad-06.braze.com/canvas/trigger/send`입니다.
- **요청 본문:** Raw Text

### 요청 헤더 및 메서드 {#request-headers-and-method}

Braze는 API 키를 포함하는 승인용 HTTP 헤더와 콘텐츠-유형을 선언하는 헤더가 필요합니다.

- **요청 헤더:**
  - **Authorization:** `Bearer YOUR_API_KEY`
  - **Content-Type:** `application/json`
- **HTTP 메서드:** `POST`

`YOUR_API_KEY`를 `canvas.trigger.send` 권한이 있는 Braze API 키로 교체하세요. Braze 대시보드에서 **설정** > **API 키**로 이동하여 API 키를 생성할 수 있습니다.

![Braze 대시보드에서 Authorization 및 Content-Type 필드를 보여주는 웹훅 요청 헤더.]({% image_buster /assets/img_archive/webhook_settings.png %}){: style="max-width:70%;"}

#### 요청 본문 {#request-body}

텍스트 필드에 `/canvas/trigger/send` 요청을 추가합니다. 자세한 내용은 [API 트리거 전달을 통한 Canvas 메시지 전송]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases)을 참조하세요. 다음은 이 엔드포인트의 요청 본문 예시이며, `your_canvas_id`는 두 번째 Canvas의 Canvas ID입니다:

{% raw %}
```json
{
  "canvas_id": "your_canvas_id",
  "recipients": [
    {
      "external_user_id": "{{${user_id}}}"
    }
  ]
}
```
{% endraw %}

사용자가 첫 번째 Canvas에서 이 웹훅 단계에 도달하면 Braze는 API를 통해 해당 사용자에 대해 두 번째 Canvas를 트리거합니다.

## 고려 사항 {#considerations}

- **사용자 업데이트:** Canvas에서 고객 프로필을 업데이트(속성, 이벤트, 구매)하려면 효율성과 비용 효과를 위해 Braze-to-Braze 웹훅 대신 [사용자 업데이트]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update)를 사용하세요.
- Braze-to-Braze 웹훅은 엔드포인트 [사용량 제한]({{site.baseurl}}/api/api_limits)의 적용을 받습니다.
- 고객 프로필 업데이트는 전체 소비량에 포함되는 [데이터 포인트]({{site.baseurl}}/user_guide/data/infrastructure/data_points)가 발생하지만, 메시징 엔드포인트를 통해 다른 메시지를 트리거하는 것은 데이터 포인트가 발생하지 않습니다.
- [익명 사용자]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#anonymous-user-profiles)를 타겟팅하려면 웹훅의 요청 본문에서 `external_id` 대신 `braze_id`를 사용하세요.
- Braze-to-Braze 웹훅을 재사용을 위해 [웹훅 템플릿]({{site.baseurl}}/user_guide/messaging/templates/webhook_templates)으로 저장할 수 있습니다.
- [메시지 활동 로그]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log)에서 웹훅 실패를 확인하고 문제를 해결할 수 있습니다.