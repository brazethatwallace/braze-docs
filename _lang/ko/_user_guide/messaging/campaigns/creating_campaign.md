---
nav_title: 캠페인 생성
article_title: 캠페인 생성
page_order: 1
page_type: tutorial
description: "작성부터 시작까지 Braze 메시징 캠페인을 생성하는 방법(멀티채널 발송 포함)과 전달 스케줄, 타겟 오디언스, 전환 이벤트 할당, 테스트 발송 및 시작 방법을 알아보세요."
tool: Campaigns
---

# 캠페인 생성 {#create-a-campaign}

> 하나 이상의 지원 채널을 통해 단일 메시징 단계로 소비자에게 도달하려면 캠페인을 사용하세요. 다단계 여정의 경우 [Canvas]({{site.baseurl}}/user_guide/messaging/canvas)를 사용하세요.

## 사전 요구 사항 {#prerequisites}

Campaign을 생성하고 실행하려면 "Campaign 편집" 및 "캠페인 실행" 권한이 필요합니다. 워크스페이스 권한의 전체 목록과 대시보드에서 표시되는 방식에 대해서는 [권한]({{site.baseurl}}/user_guide/administer/global/user_management/permissions)을 참조하세요.

### 시작하기 전에 {#before-you-begin}

- 메시지를 수신할 대상을 정의하는 [Segments]({{site.baseurl}}/user_guide/audience/segments)를 구축하거나 선택하세요.
- 메시징 채널, 전달 유형 및 전환 목표가 사용 사례에 맞는지 [Campaign 기본 사항]({{site.baseurl}}/user_guide/messaging/campaigns/campaign_basics)을 검토하세요.
- 전달, 타겟팅 및 전환에 대한 안내 워크스루는 [Campaign 설정](https://learning.braze.com/campaign-setup-delivery-targeting-conversions) Braze 학습 과정을 수강하세요.
- Operator에게 브리프를 기반으로 Campaign 초안을 작성하도록 요청하거나, 타겟팅 및 전달 선택을 개선하세요. 자세한 내용은 [Operator로 할 수 있는 것]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#campaigns-and-audiences)을 참조하세요.

## Campaign 작성기 {#campaign-composer}

Campaign 작성기는 전달, 오디언스, 전환 및 실행 설정을 정의하는 곳입니다. 계속하기 전에 단일 채널 또는 멀티채널 Campaign을 만들지 결정하세요.

{% tabs %}
{% tab 단일 채널 %}

단일 채널 Campaign은 한 번 실행할 때 하나의 메시징 채널을 통해 사용자에게 도달합니다.

### 차이점 {#whats-different}

#### 전환 및 보고 {#single-channel-conversions}

단일 채널 Campaign의 경우, Braze는 해당 채널의 발송에 대해 Campaign에 할당한 [전환 이벤트]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events)를 추적합니다. 기여 기간 및 집계 규칙에 대해서는 [전환 추적 규칙]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events#conversion-tracking-rules)을 참조하세요.

워크스페이스 [최대 게재빈도 설정]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping) 및 발송 제한은 여전히 적용됩니다.

### 단일 채널 Campaign 만들기 {#create-a-single-channel-campaign}

Campaign을 만들려면:

1. **메시징** > **Campaigns**로 이동합니다.
2. **Campaign 만들기**를 선택합니다.
3. 사용 사례에 맞는 [채널]({{site.baseurl}}/user_guide/channels)을 선택합니다.
4. [작성 단계](#step-1-compose-messages)에서 해당 채널의 문구를 작성하고 미리 봅니다.

각 Campaign은 한 번에 하나의 채널 유형을 사용합니다. 크리에이티브 분할을 비교하거나 [A/B 테스트]({{site.baseurl}}/user_guide/messaging/ab_testing)를 실행하려면 배리언트를 추가하세요.

{% endtab %}
{% tab 멀티채널 %}

멀티채널 Campaign은 한 번 실행할 때 두 개 이상의 메시징 채널을 통해 사용자에게 도달합니다. 예를 들어, 이메일과 푸시 알림을 함께 보낼 수 있습니다.

{% alert note %}
[In-App Messages]({{site.baseurl}}/user_guide/channels/in_app_messages)는 멀티채널 Campaign에서 사용할 수 없습니다. 대신 단일 채널 Campaign 또는 Canvas를 만드세요.
{% endalert %}

### 차이점

#### 대조군 {#multichannel-control-groups}

Campaign 대조군은 하나의 채널 내에서 배리언트를 비교합니다(예: 이메일 A와 이메일 B). 하나의 멀티채널 Campaign 내에서 전체 채널을 비교하는 데는 사용되지 않습니다. 여정 전반에 걸쳐 채널, 크리에이티브 또는 타이밍을 함께 테스트하려면 [Canvas]({{site.baseurl}}/user_guide/messaging/canvas)를 사용하세요.

#### 전환 및 보고 {#multichannel-conversions}

멀티채널 Campaign의 경우, Braze는 채널별로 [전환 이벤트]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events)를 추적합니다. 사용자가 두 개 이상의 채널에서 메시지를 수신한 후 전환하면, Braze는 해당 전환을 여러 채널에 기여할 수 있습니다. 전환 수가 *고유 사용자 수*를 초과할 수 있으며, 전환율이 100%를 초과할 수 있습니다. 전체 규칙은 [전환 추적 규칙]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events#conversion-tracking-rules)을 참조하세요.

여러 채널에 걸친 발송의 사용량 제한에 대해서는 [멀티채널 Campaigns 및 Canvases]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#multichannel-campaigns-and-canvases)에 설명되어 있습니다. 워크스페이스 전체 규칙(멀티채널 발송이 상한에 포함되는 방식 포함)은 [최대 게재빈도 설정]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping)을 참조하세요.

### 멀티채널 Campaign 만들기 {#create-a-multichannel-campaign}

1. **메시징** > **Campaigns**로 이동합니다.
2. **Campaign 만들기**를 선택합니다.
3. **멀티채널**을 선택합니다.
4. [작성 단계](#step-1-compose-messages)에서 **채널 추가**를 선택하고 필요한 각 채널을 선택합니다. 각 채널의 문구를 작성하면서 채널 아이콘을 선택하여 작성기 간에 전환할 수 있습니다.

{% endtab %}
{% endtabs %}

## 1단계: 메시지 작성 {#step-1-compose-messages}

### 캠페인 세부 정보 {#campaign-details}

다음 필드를 사용하여 팀이 캠페인을 찾고 관리하는 데 도움이 되는 메타데이터를 기록하세요.

| 필드 | 용도 |
| --- | --- |
| 이름 | 캠페인 목표를 반영하는 명확한 이름을 사용하세요. |
| 설명 | 선택 사항. 협업자를 위한 의도 또는 브리프 링크를 설명하세요. |
| 팀 | 선택 사항. 적절한 그룹이 이 발송을 편집하거나 보고할 수 있도록 [Teams]({{site.baseurl}}/user_guide/administer/global/user_management/teams)를 할당하세요. |
| 태그 | 선택 사항. [보고서 빌더]({{site.baseurl}}/user_guide/analytics/reports/report_builder) 등의 목록 및 도구에서 필터링할 수 있도록 [태그]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags)를 추가하세요. |
| Campaign ID | 작성기 또는 요약에 표시되는 경우, 특정 캠페인을 참조하는 API 호출, 보고 및 통합을 위해 이 식별자를 복사하세요. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="캠페인 세부 정보" }

### 채널 및 편집기 {#channels-and-editors}

이 단계에서 채널별 콘텐츠를 작성합니다. 자세한 안내는 [채널]({{site.baseurl}}/user_guide/channels)을 참조하고 선택한 채널의 문서를 열어보세요.

### 배리언트 {#variants}

크리에이티브 또는 전달 분할을 비교하려면 배리언트를 추가하세요. 실험 및 대조군에 대한 배경 정보는 [다변량 및 A/B 테스트]({{site.baseurl}}/user_guide/messaging/ab_testing)를 참조하세요.

{% alert tip %}
각 배리언트가 유사한 본문 콘텐츠를 사용하는 경우, 추가 배리언트를 추가하기 **전에** 메시지를 작성하세요. 그런 다음 **배리언트 추가** 메뉴에서 **배리언트에서 복사**를 사용하여 배리언트 또는 채널 간에 작업을 재사용하세요.
{% endalert %}

## 2단계: 전달 스케줄 {#step-2-schedule-delivery}

사용자가 캠페인을 수신할 자격을 얻는 시점을 선택합니다:

| 전달 유형 | 요약 |
| --- | --- |
| [스케줄 전달]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/scheduled_delivery) | 지정된 시간 또는 주기에 발송합니다. |
| [실행 기반 전달]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery) | 사용자가 정의한 동작을 수행하거나 조건을 충족할 때 발송합니다. |
| [API 트리거 전달]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery) | 시스템이 Braze를 호출하여 자격이 있는 사용자에게 캠페인을 트리거할 때 발송합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="2단계: 전달 스케줄" }

Braze 전반의 스케줄링 개념은 [캠페인 스케줄]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign)을 참조하세요.

### 전달 제어 {#delivery-controls}

전달 유형에 따라 [재자격]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility)(사용자가 캠페인에 다시 진입할 수 있는지 여부)을 조정하고 워크스페이스 [최대 게재빈도 설정]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping) 규칙을 준수할 수 있습니다. 또한 제한된 기간 동안 메시지가 발송되지 않도록 [방해금지 시간]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours)을 구성할 수도 있습니다.

## 3단계: 타겟 오디언스 {#step-3-target-audiences}

**타겟 오디언스**에서 캠페인을 수신할 자격이 있는 대상을 정의합니다. 전체 타겟팅 옵션, UI 워크스루 및 스크린샷은 [사용자 타겟팅]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users)을 참조하세요.

### 타겟팅 옵션 {#targeting-options}

이 섹션에서는 Segment 또는 필터를 선택하여 오디언스를 좁혀 사용자를 타겟팅할 수 있습니다. 자격이 있는 사용자는 여전히 **전달 스케줄** 단계에서 정의한 트리거 또는 기준을 충족해야 합니다. 타겟 오디언스는 대기실과 같습니다. 이미 안에 있는 사람만 다음 동작이 발생할 때 앞으로 나아갈 수 있습니다.

워크스페이스 [억제 목록]({{site.baseurl}}/user_guide/audience/suppression_lists)은 이 캠페인에 대한 예외를 허용하지 않는 한 목록에 있는 사용자를 자동으로 제외합니다.

### 오디언스 요약 {#audience-summary}

Segment 또는 필터를 추가한 후, **오디언스 요약**은 해당 Segment 모집단의 모습을 미리 보여주며, 해당 Segment 내에서 선택한 채널을 통해 도달 가능한 사용자 수를 포함합니다. 도달 가능 수는 워크스페이스 데이터, 채널 설정 및 필터를 반영합니다. 정확한 Segment 멤버십은 항상 메시지가 발송되기 전에 계산된다는 점을 유의하세요. 매우 큰 오디언스의 경우, Braze는 정확한 통계를 계산할 때까지 추정치를 표시할 수 있습니다.

{% alert note %}
[글로벌 컨트롤 그룹]({{site.baseurl}}/user_guide/audience/global_control_group)이 설정되어 있는 경우, 캠페인 타겟 오디언스에 표시되는 도달 가능 사용자 수는 동일한 Segment에 대해 표시되는 도달 가능 사용자 수보다 적습니다. 이는 캠페인이 글로벌 컨트롤 그룹에 속한 사용자를 제외하는 반면, Segment 수에는 해당 사용자가 포함되기 때문입니다.
{% endalert %}

### 사용자 조회 {#user-lookup}

Segment 또는 필터를 추가한 후, 사용자를 조회하여 Segment 기준에 일치하는지 확인함으로써 오디언스가 예상대로 설정되었는지 테스트할 수 있습니다. 이를 위해 **사용자 조회** 섹션에서 사용자의 `external_id` 또는 `braze_id`를 검색하세요. 여기서는 이메일 주소로 검색할 수 없습니다. 자세한 내용은 [Segment 테스트]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment#testing-segments)를 참조하세요.

사용자가 Segment, 필터 및 앱 기준에 일치하면 알림이 표시됩니다. 사용자가 Segment, 필터 또는 앱 기준의 일부 또는 전부에 일치하지 않으면, 문제 해결을 위해 누락된 기준이 나열됩니다.

### 이 사용자에게 발송 {#send-to-these-users}

가입 기반 채널(이메일, SMS 등)의 경우, **이 사용자에게 발송**을 사용하여 특정 가입 상태를 가진 사용자(예: 이메일에 가입되고 옵트인한 사용자)에게만 캠페인을 발송하세요.

### 발송량 제한 {#limit-send-volume}

메시지를 수신하는 총 사용자 수를 제한할 수 있습니다. 이는 캠페인 필터와 독립적인 확인 역할을 합니다. 자세한 내용은 [최대 사용자 한도 설정]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#setting-a-maximum-user-cap)을 참조하세요.

### 이 캠페인의 발송 속도 제한 {#limit-the-rate-at-which-this-campaign-sends}

대규모 캠페인이 사용자 활동 급증을 유발하여 서버에 과부하를 줄 것으로 예상되는 경우, 메시지 발송에 대한 분당 사용량 제한을 지정할 수 있습니다. 이는 Braze가 1분 내에 사용량 제한 설정 이상으로 발송하지 않음을 의미합니다. 자세한 내용은 [전달 속도 사용량 제한조치]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting)를 참조하세요.

### A/B 테스트 {#ab-testing}

단일 채널을 타겟팅하는 모든 캠페인에 대해 [다변량 또는 A/B 테스트]({{site.baseurl}}/user_guide/messaging/ab_testing)를 생성할 수 있으며, 단일 채널에 여러 기기가 포함되어 있어도 가능합니다. 예를 들어, 푸시 캠페인에 다변량 또는 A/B 테스트를 사용하려면 iOS 기기만 또는 Android 기기만 타겟팅할 수 있으며, 동일한 캠페인에서 두 기기 유형을 모두 타겟팅할 수는 없습니다.

지원되는 1회 발송 및 다회 발송 캠페인의 경우, [BrazeAI<sup>TM</sup>로 최적화]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/variant_selection)를 켜서 배리언트 배분을 자동으로 최적화할 수 있습니다.

## 4단계: 전환 이벤트 할당 {#step-4-assign-conversion-events}

[전환 이벤트]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events)는 사용자가 캠페인을 수신한 후(또는 대조군에 진입한 후) 성과를 측정합니다. Braze는 기본적으로 짧은 기간(3일) 내의 **세션 시작**을 사용합니다. 캠페인당 최대 4개의 이벤트까지 핵심 성과 지표(KPI)에 맞는 전환 이벤트를 정의할 수 있습니다.

시작 후, [전환 대시보드]({{site.baseurl}}/user_guide/analytics/dashboards/conversions)를 사용하여 여러 Campaigns 또는 Canvases에 걸친 전환 추세를 분석하고, 채널을 비교하며, 날짜 범위, 기여도 방법 및 분석 항목을 한 곳에서 조정하세요.

{% alert important %}
캠페인 시작 후에는 전환 이벤트를 추가하거나 제거할 수 없습니다. 시작 전에 이벤트를 확인하세요.
{% endalert %}

## 5단계: 요약 검토 및 시작 {#step-5-review-summary-and-launch}

**요약 검토** 단계에서는 스케줄, 오디언스, 배리언트 및 메시징 선택 사항을 보여줍니다. 캠페인을 시작하기 전에:

1. Segment, 배리언트 및 전달 설정이 의도와 일치하는지 확인합니다.
2. 테스트 기기 또는 내부 수신자에서 렌더링 및 동작을 검증하기 위해 [테스트 메시지를 발송]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages)합니다.

준비가 되면 **캠페인 시작**을 선택합니다.

### 승인 {#approvals}

워크스페이스에서 승인을 사용하는 경우, 캠페인 승인 권한이 있는 팀원이 시작 전에 승인해야 합니다. 자세한 내용은 [Campaigns 및 Canvases 승인]({{site.baseurl}}/user_guide/messaging/governance/approvals)을 참조하세요.

## 관련 문서 {#related-articles}

- [디자인 및 편집]({{site.baseurl}}/user_guide/messaging/design_and_edit)
- [A/B 테스트]({{site.baseurl}}/user_guide/messaging/ab_testing)
- [발송 전 확인 사항]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/know_before_you_send)
- [Campaign 분석]({{site.baseurl}}/user_guide/analytics/reports/campaign_analytics)