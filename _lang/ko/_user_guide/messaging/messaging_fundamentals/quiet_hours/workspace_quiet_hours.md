---
nav_title: 워크스페이스 방해금지 시간
article_title: 워크스페이스 방해금지 시간
page_order: 4
page_type: reference
description: "이 참고 문서에서는 워크스페이스 방해금지 시간, Braze가 방해금지 기간 동안 메시지를 처리하는 방법, 그리고 방해금지 시간과 Intelligent Timing의 상호작용에 대해 다룹니다."
---

# 워크스페이스 방해금지 시간 {#workspace-quiet-hours}

> 워크스페이스 방해금지 시간을 사용하면 워크스페이스 전체에서 메시징 채널에 대한 기본 방해금지 시간 창을 설정할 수 있습니다. 해당 채널로 발송하는 모든 Campaign과 Canvas가 자동으로 이 창을 준수하므로, 각 Campaign이나 Canvas에서 개별적으로 방해금지 시간을 구성할 필요가 없습니다.

워크스페이스 방해금지 시간은 Campaign 및 Canvas 수준의 방해금지 시간과 별개이며, 구성 시 해당 설정이 계속 적용됩니다. 워크스페이스 방해금지 시간은 기본 사례(예: 모든 SMS 발송에 대한 규정 준수 요구사항)에 사용하세요. Campaign 및 Canvas 수준의 방해금지 시간은 예외 상황에 사용하세요.

{% alert important %}
워크스페이스 방해금지 시간은 현재 얼리 액세스로 제공됩니다. 정식 출시 전에 구성 옵션이 변경될 수 있습니다. 액세스를 요청하려면 Braze 계정 팀에 문의하세요.
{% endalert %}

## 작동 방식 {#how-it-works}

- **채널당 하나의 시간대:** 각 채널은 시작 시간과 종료 시간으로 정의되는 단일 워크스페이스 방해금지 시간 시간대를 지원합니다.
- **현지 시간대:** Campaign 및 Canvas 수준의 방해금지 시간과 마찬가지로, 워크스페이스 방해금지 시간은 회사의 시간대가 아닌 각 수신자의 현지 시간대에 적용됩니다.
- **나중에 전달하기 위해 보류:** 방해금지 시간 시간대 중에 전송될 메시지는 보류되어 나중에 전달되거나, Campaign 유형에 따라 중단됩니다. [보류된 메시지는 어떻게 되나요](#what-happens-to-a-held-message)를 참조하세요. 방해금지 시간은 메시지 내용을 수정하지 않으며, 전송 타이밍에만 영향을 줍니다.
- **최대 시간대 길이:** 방해금지 시간 시간대는 20시간을 초과할 수 없습니다. 이 제한은 채널의 모든 전송이 실수로 일시 중지되는 것을 방지하기 위해 존재합니다(예: 시작 시간과 종료 시간을 동일한 값으로 설정하는 경우).

### 지원되는 채널 {#supported-channels}

다음 채널에 대해 워크스페이스 방해금지 시간 시간대를 설정할 수 있습니다:

- Content Cards
- 이메일
- KakaoTalk
- LINE
- 푸시
   - 워크스페이스의 모든 푸시 플랫폼에 적용됩니다. 개별 플랫폼(예: iOS와 Android)에 대해 서로 다른 방해금지 시간을 설정하는 옵션은 없습니다.
- SMS/MMS/RCS
- 웹훅
- WhatsApp

## 사전 요구 사항 {#prerequisites}

워크스페이스 방해금지 시간을 생성하거나 업데이트하려면 "방해금지 시간 편집" 권한이 필요합니다.

| 권한 | 접근 |
|---|---|
| 방해금지 시간 편집 | 워크스페이스 방해금지 시간을 생성하고 업데이트합니다. |
| 방해금지 시간 보기 | 워크스페이스 방해금지 시간 구성을 편집 없이 확인합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="방해금지 시간 권한" }

기존 Campaign 및 Canvas 편집 권한은 영향을 받지 않습니다. 해당 권한을 가진 사용자는 Campaign 또는 Canvas 수준에서 방해금지 시간을 계속 편집할 수 있습니다.

## 워크스페이스 방해금지 시간 설정 {#set-up-workspace-quiet-hours}

### 워크스페이스 시간대 구성 {#configure-the-workspace-window}

1. **설정** > **방해금지 시간**으로 이동합니다.
2. **방해금지 시간 추가**를 선택합니다.
3. 채널을 선택한 다음 시작 시간과 종료 시간을 입력합니다. 채널당 한 번에 하나의 워크스페이스 방해금지 시간대만 설정할 수 있습니다.
4. (선택 사항) 다른 채널을 추가하려면 **방해금지 시간 추가**를 다시 선택합니다.
5. 변경 사항을 저장합니다.

![SMS 및 이메일 방해금지 시간대가 각각 시작 시간과 종료 시간과 함께 표시되어 있고, 방해금지 시간 추가 옵션이 있는 방해금지 시간 워크스페이스 설정 페이지.]({% image_buster /assets/img/quiet_hours/workspace_quiet_hours_settings.png %}){: style="max-width:90%;"}

워크스페이스 방해금지 시간에 대한 업데이트는 체인지로그에 기록되며, 이 설정이 해당 채널의 모든 Campaign과 Canvas에 영향을 미치므로 누가 언제 변경했는지도 함께 기록됩니다.

### Campaign 또는 Canvas에서 적용 또는 재정의 {#apply-or-override-in-a-campaign-or-canvas}

저장 후, 워크스페이스 방해금지 시간대는 해당 시간대가 설정된 각 채널의 Campaign 및 Canvas 편집기에 표시됩니다. 워크스페이스 기본값을 유지하거나, 워크스페이스 수준의 최대 게재빈도 설정을 해제하는 것과 같은 방식으로 해제하고 Campaign 또는 Canvas 전용 시간대를 대신 적용할 수 있습니다.

1. **이 Campaign에 방해금지 시간 적용**(또는 Canvas에 해당하는 옵션)을 선택합니다.
2. 워크스페이스 기본값을 적용하려면 **워크스페이스 방해금지 시간 사용**을 선택하고, Campaign 또는 Canvas 전용 시간대를 설정하려면 **커스텀 방해금지 시간 사용**을 선택합니다.
3. 사용 중인 채널의 워크스페이스 시간대를 확인하려면 **방해금지 시간 보기**를 선택합니다.

![이 Campaign에 방해금지 시간 적용이 선택되고, 워크스페이스 방해금지 시간 사용이 선택되어 있으며, 이메일 워크스페이스 시간대가 오후 8:00부터 오전 8:00까지로 확장 표시된 Campaign의 방해금지 시간 섹션.]({% image_buster /assets/img/quiet_hours/campaign_workspace_quiet_hours.png %}){: style="max-width:70%;"}

## 우선순위: 워크스페이스 방해금지 시간 대 Campaign 또는 Canvas 방해금지 시간 {#precedence-workspace-versus-campaign-or-canvas-quiet-hours}

특정 Campaign 또는 Canvas에 대해 한 번에 하나의 방해금지 시간 설정만 적용됩니다(워크스페이스 방해금지 시간, Campaign 또는 Canvas별 설정, 또는 없음). Campaign 또는 Canvas 수준의 방해금지 시간 설정은 항상 워크스페이스 기본값보다 우선합니다.

방해금지 시간이 적용되는 방식은 Campaign 또는 Canvas가 생성된 시점에 따라 달라집니다:

- **기존 Campaigns 및 Canvases**(워크스페이스 방해금지 시간을 활성화하기 전에 생성된 경우): Campaign 또는 Canvas에 자체 방해금지 시간 설정이 없으면 해당 채널의 워크스페이스 방해금지 시간이 자동으로 적용됩니다. 이미 Campaign 또는 Canvas 수준의 설정이 있는 경우 해당 설정이 계속 적용됩니다.
- **새 Campaigns 및 Canvases:** Campaign 또는 Canvas를 생성할 때 워크스페이스 방해금지 시간 기본값을 사용하거나, 커스텀 Campaign 또는 Canvas 수준의 설정을 지정하거나, 방해금지 시간을 완전히 해제할 수 있습니다.

| 설정 상태 | 적용되는 방해금지 시간 |
|---|---|
| Campaign 또는 Canvas에 자체 방해금지 시간 설정이 있는 경우 | Campaign 또는 Canvas 수준의 설정이 적용됩니다. 해당 Campaign 또는 Canvas에 대해 워크스페이스 방해금지 시간은 무시됩니다. |
| Campaign 또는 Canvas에 자체 방해금지 시간 설정이 없고, 사용하는 채널에 대한 워크스페이스 방해금지 시간이 존재하는 경우 | 워크스페이스 방해금지 시간이 자동으로 적용됩니다. 방해금지 시간을 설정한 적이 없는 기존 Campaigns 및 Canvases도 포함됩니다. |
| Campaign 또는 Canvas가 방해금지 시간을 해제한 경우 | 방해금지 시간이 적용되지 않습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="방해금지 시간 우선순위" }

### 보류된 메시지의 처리 방식 {#what-happens-to-a-held-message}

방해금지 시간 내에 해당하는 메시지의 처리 방식은 Campaign 또는 Canvas 전달 유형에 따라 달라집니다:

- **액션 기반 Campaigns 및 Canvases:** 대체 동작은 **메시지 중단** 또는 **다음 가능한 시간에 전송** 중 선택할 수 있으며, Campaign 및 Canvas 수준의 방해금지 시간과 동일한 옵션입니다.
- **고정 전송 시간이 있는 스케줄 Campaigns:** 대체 동작은 **메시지 중단**입니다. Braze는 고정 시간 전송을 다음 가능한 시간대로 지연하지 않습니다. 방해금지 시간이 종료된 후 압축된 전송 시간대에 대량의 메시지가 몰릴 수 있기 때문입니다.
- **Intelligent Timing을 사용하는 Campaigns:** 별도의 대체 동작이 필요하지 않습니다. Braze는 각 사용자에 대해 최적의 전송 시간을 계산할 때 워크스페이스 방해금지 시간을 이미 반영하므로, 메시지가 해당 시간대에 스케줄되지 않습니다.
- **API 트리거 Campaigns 및 API Campaigns:** 대체 동작은 기본적으로 **메시지 중단**입니다.

### API 트리거 및 API Campaigns {#api-triggered-and-api-campaigns}

API 트리거 Campaigns와 API Campaigns에서는 방해금지 시간이 다르게 작동합니다.

#### API 트리거 Campaigns {#api-triggered-campaigns}

API 트리거 Campaigns는 대시보드의 다른 Campaigns와 동일한 방해금지 시간 옵션을 따릅니다. 워크스페이스 방해금지 시간 기본값을 사용하거나, 커스텀 Campaign 수준의 설정을 지정하거나, Campaign 설정에서 방해금지 시간을 해제할 수 있습니다. API 트리거 전송에는 `ignore_workspace_quiet_hours` API 파라미터가 없습니다.

`at_optimal_time`을 사용하는 스케줄 API 트리거 전송의 경우, [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing)과 유사하게 워크스페이스 방해금지 시간이 최적 전송 시간에 이미 반영됩니다.

#### API Campaigns {#api-campaigns}

API Campaigns는 Campaign 수준의 방해금지 시간을 사용할 수 없습니다. 워크스페이스 방해금지 시간만 적용됩니다. 해당 시간대에 전송하려면 API 요청에 선택적 `ignore_workspace_quiet_hours` 파라미터를 포함하세요.

### 제외 항목 {#exclusions}

다음 항목은 채널에 관계없이 워크스페이스 방해금지 시간에 의해 보류되지 않습니다:

- 트랜잭션 이메일 메시지
- SMS 자동 응답(예: `STOP` 또는 `HELP` 키워드 응답)
- 테스트 전송 및 시드 그룹 전송

## 기타 고려 사항 {#other-considerations}

- **회사 시간대 기준 예약 발송:** 워크스페이스 방해금지 시간은 각 수신자의 현지 시간대를 기준으로 하지만, 예약된 Campaign의 발송 시간은 회사의 시간대로 설정될 수 있습니다. 이러한 불일치로 인해 회사 시간대에서는 문제없어 보이는 발송 시간이 일부 수신자에게는 방해금지 시간에 해당할 수 있습니다. 발송 전에 Campaign 편집기에 표시된 워크스페이스 방해금지 시간 세부 정보를 확인하세요.
- **방해금지 시간 종료 후 전달:** 방해금지 시간 동안 대규모 오디언스의 메시지가 보류된 경우, 해당 시간이 종료되면 모든 메시지가 한꺼번에 발송 대상이 될 수 있습니다. 채널의 오디언스가 넓고 방해금지 시간이 긴 경우 이를 고려하여 계획하세요.
- **최대 게재빈도 설정 및 사용량 제한조치와 독립적으로 적용:** 워크스페이스 방해금지 시간은 최대 게재빈도 설정 및 사용량 제한조치와 독립적으로 적용됩니다. 해당 제어를 통과한 메시지도 방해금지 시간에 의해 보류될 수 있으며, 방해금지 시간에 의해 보류된 메시지는 발송 준비가 되면 사용량 제한에 대해 다시 평가됩니다.
- **Intelligent Timing은 멀티채널 액션 기반 Campaign에서 워크스페이스 방해금지 시간을 재정의합니다. 발송 시간을 제한하려면 커스텀 방해금지 시간을 대신 설정하세요.

## 관련 설정 {#related-settings}

- [방해금지 시간]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours): 기존의 Campaign 및 Canvas별 버전의 기능입니다. 워크스페이스 방해금지 시간은 이를 대체하지 않으며, Campaign 또는 Canvas에서 자체 시간대를 설정하지 않은 경우 적용되는 기본값을 지정합니다.
- [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing): 사용자별 최적의 발송 시간을 계산합니다. 워크스페이스 방해금지 시간과 함께 활성화하면, 방해금지 시간이 해당 계산에 반영됩니다.
- [사용량 제한조치 및 최대 게재빈도 설정]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping): 방해금지 시간과 독립적으로 적용되는 별도의 전송 제어 기능입니다.