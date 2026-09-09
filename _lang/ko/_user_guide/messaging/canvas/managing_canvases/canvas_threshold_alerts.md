---
nav_title: Canvas 알림
article_title: Canvas 임계값 알림
page_order: 4
page_type: reference
description: "이 참조 문서에서는 Canvas에 대한 임계값 알림을 설정하여 사용자 항목 또는 발송된 메시지가 예상 범위를 벗어날 때 사전에 알림을 받는 방법을 다룹니다."
tool: Canvas
channel:
- email
- webhooks
---

# Canvas 임계값 알림 {#canvas-threshold-alerts}

> Canvas 임계값 알림은 Canvas에서 계획대로 진행되지 않는 상황을 알려주어, 고객에게 영향을 미치기 전에 중단된 여정이나 예상치 못한 이탈을 포착할 수 있도록 합니다.

{% multi_lang_include alerts/early_access_beta_alert.md feature='Canvas threshold alerts' %}

사용자 항목 또는 발송된 메시지에 대한 볼륨 또는 비율 임계값을 설정하면, 해당 임계값이 초과될 경우 Braze가 이메일 또는 웹훅으로 알림을 보냅니다. 동일한 Canvas에 대해 여러 알림을 생성할 수도 있습니다. 예를 들어, 사용자 항목에 대한 알림 하나와 발송된 메시지에 대한 알림 하나를 설정할 수 있습니다.

어디서부터 시작해야 할지 모르겠다면, [Operator]({{site.baseurl}}/user_guide/brazeai/operator/capabilities)가 Canvas 임계값 알림 설정 방법을 안내해 드릴 수 있습니다.

## 1단계: 알림 만들기 {#step-1-create-an-alert}

알림은 Canvas 수준에서 설정되며, 활성 상태와 초안 상태의 Canvases 모두에 대해 구성할 수 있습니다. Canvas의 **알림 관리** 페이지를 열려면 다음 중 하나를 수행합니다:

- **메시징** > **Canvas**로 이동하여 개별 Canvas의 컨텍스트 메뉴에서 **알림 관리**를 선택합니다.
- 활성 Canvases의 경우, **Canvas 분석**을 열고 **알림 관리**를 선택합니다.

**알림 관리** 페이지에서 **알림 구성**을 선택하여 새 알림을 만듭니다.

## 2단계: 알림 이름 지정 및 Canvas 선택 {#step-2-name-your-alert-and-select-a-canvas}

알림에 이름을 지정하고 적용할 Canvas를 확인합니다.

![알림 이름과 Canvas 이름 필드, 빈 규칙 그룹, 알림 규칙, 스케줄 및 알림에 대한 요약 사이드바를 보여주는 알림 구성 패널.]({% image_buster /assets/img/canvas_threshold_alerts/configure_alert.png %})

## 3단계: 알림 규칙 설정 {#step-3-set-alert-rules}

알림 규칙은 알림을 트리거하는 임계값을 정의합니다. 두 가지 측정기준을 사용하여 규칙을 작성할 수 있습니다.

- **사용자 항목:** Canvas에 진입한 사용자 수
- **메시지 전송:** Canvas에서 전송된 메시지 수

각 규칙에 대해 비교 조건(미만, 초과, 이하, 이상 또는 같음), 단위, 임계값을 선택합니다.

- **볼륨:** 현재 확인 기간의 절대 수를 비교합니다. 예를 들어, "사용자 항목이 3,000 미만"은 평소에 수천 명의 사용자에게 도달하던 Canvas가 갑자기 중단된 경우를 감지합니다. 이는 상위 오디언스 또는 진입 문제를 조사할 필요가 있다는 신호입니다.
- **퍼센트:** 현재 수를 해당 Canvas의 기준값과 비교합니다. 기준값은 이전 7일 동안 동일한 시간 구간의 평균입니다. 예를 들어, 알림이 3시간마다 확인하는 경우 오후 2시~5시 확인은 이전 7일간의 오후 2시~5시 구간 평균과 비교합니다. "메시지 전송이 50% 미만" 규칙은 평소 볼륨의 절반 이하로 감소한 경우를 감지합니다.

임계값은 정수입니다. **미만** 또는 **이하** 퍼센트 규칙의 경우 1에서 100 사이의 값을 입력합니다. **초과**, **이상** 또는 **같음**의 경우 퍼센트 값은 0 이상이며 100을 초과하는 값도 입력할 수 있으므로, 기준값 대비 급증을 감지하는 알림을 설정할 수 있습니다.

여러 규칙을 함께 그룹화할 수 있으며, 볼륨 규칙과 퍼센트 규칙을 혼합하는 것도 가능합니다. 규칙 그룹을 AND 또는 OR 논리로 결합하여 더 구체적인 알림 조건을 구성할 수 있습니다.

## 4단계: 알림 스케줄 설정 {#step-4-set-the-alert-schedule}

알림 규칙이 확인되는 빈도를 정의합니다. 확인 빈도는 3시간에서 12시간까지(1시간 단위) 또는 24시간마다로 설정할 수 있습니다. 활성화된 알림은 해당 알림과 연결된 Canvas가 활성 상태인 동안 이 스케줄에 따라 계속 확인됩니다.

## 5단계: 알림 설정 {#step-5-set-up-notifications}

알림 규칙이 충족되었을 때 누구에게 어떤 방식으로 알림을 보낼지 선택합니다:

- **이메일:** 하나 이상의 수신자 이메일 주소를 추가합니다
- **웹훅:** 알림을 보낼 웹훅 URL을 입력하고, 웹훅 대상에서 요구하는 커스텀 요청 헤더를 선택적으로 추가합니다

단일 알림에 대해 하나 또는 두 가지 알림 방식을 모두 활성화할 수 있습니다.

웹훅 알림은 Slack 채널과 같은 외부 플랫폼으로 알림을 라우팅하는 데 유용합니다. 자세한 내용은 Slack의 [수신 웹훅을 사용한 메시지 전송](https://docs.slack.dev/messaging/sending-messages-using-incoming-webhooks/) 설명서를 참조하세요. 각 웹훅 알림은 알림 이름, 평가 기간, 알림을 트리거한 조건이 포함된 JSON 페이로드를 전송합니다. 각 조건에는 `volume` 또는 `percentage`의 `threshold_unit`이 포함됩니다. 백분율 조건에는 `percentage_metric_value`(관측된 수를 기준선의 정수 백분율로 나타낸 값)도 포함됩니다. `metric_value`는 항상 절대 수입니다.

### 웹훅 페이로드 예시 {#example-webhook-payload}

다음은 알림이 트리거되었을 때 웹훅 엔드포인트로 전송되는 POST 요청의 JSON 페이로드 예시입니다. 첫 번째 조건은 볼륨 규칙입니다. 두 번째는 백분율 규칙으로, 51,235개의 메시지가 전송되었으며 이는 7일 동일 기간 기준선의 57%로, 55% 초과 임곗값에 대한 조건입니다.

```json
{
  "alert": {
    "name": "Canvas Alert - August 6, 2026",
    "target_type": "CANVAS"
  },
  "evaluation_window_start": "2026-08-06T10:28:01Z",
  "evaluation_window_end": "2026-08-06T13:28:01Z",
  "conditions": [
    {
      "subject": "user_entries",
      "operator": "lt",
      "threshold_value": 500,
      "metric_value": 0.0,
      "group_index": 0,
      "threshold_unit": "volume"
    },
    {
      "subject": "messages_sent",
      "operator": "gt",
      "threshold_value": 55,
      "metric_value": 51235.0,
      "group_index": 0,
      "threshold_unit": "percentage",
      "percentage_metric_value": 57
    }
  ]
}
```

## 6단계: 알림 저장 {#step-6-save-your-alert}

요약 패널에서 알림 규칙, 스케줄 및 알림 설정을 검토한 다음 **Save alert**를 선택합니다.

## 7단계: 알림 활성화하기 {#step-7-activate-the-alert}

알림을 저장해도 자동으로 활성화되지는 않습니다. 알림을 켜려면 **알림 관리** 페이지로 이동하여 해당 알림의 **상태** 토글을 사용하세요. 알림은 비활성화하거나 연결된 Canvas가 더 이상 활성 상태가 아닐 때까지 활성 상태로 유지됩니다. **Canvas** 페이지의 **구성된 알림** 열에는 저장된 알림이 하나 이상 있는 Canvas에 종 모양 아이콘이 표시됩니다.

## 고려 사항 {#considerations}

- **초안 Canvases:** 아직 초안 상태인 Canvas에 대해 임계값 알림을 설정할 수 있지만, Canvas가 시작될 때까지 알림이 규칙에 대해 확인을 시작하지 않습니다.
- **백분율 기준:** 백분율 규칙은 Canvas 시작 후 동일한 기간의 이전 7일이 완전히 경과해야 합니다. 해당 기간이 아직 존재하지 않거나 기준 평균이 0인 경우(이전 기간에 활동이 없는 경우), 백분율 규칙은 알림을 트리거하지 않습니다.

## 자주 묻는 질문 {#frequently-asked-questions}

### Canvas 임계값 알림은 웹훅 사용량에 포함되나요? {#do-canvas-threshold-alerts-count-toward-webhook-usage}

아니요. Canvas 임계값 알림은 웹훅 사용량 제한이나 사용량 측정기준에 포함되지 않습니다.