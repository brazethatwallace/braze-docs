---
nav_title: 예약 전달
article_title: 예약 전달
page_order: 0
page_type: reference
description: "이 참조 문서에서는 캠페인 전달을 위한 시간 기반 예약 옵션 간의 차이점을 설명합니다."
tool: Campaigns

---

# 예약 전달 {#scheduled-delivery}

> 시간 기반 예약 전달을 사용하여 발송되는 Campaign(캠페인)은 지정된 날짜에 전달됩니다.

## 옵션 1: Campaign이 시작되는 즉시 발송 {#option-1-send-as-soon-as-the-campaign-is-launched}

메시지를 시작되는 즉시 발송하도록 선택하면, Campaign 생성을 완료하는 즉시 메시지 발송이 시작됩니다.

!["스케줄"이 선택되고 Campaign이 시작되는 즉시 발송하는 시간 기반 예약 옵션이 표시된 "전달" 섹션.]({% image_buster /assets/img_archive/schedule_immediately.png %})

이 유형의 스케줄은 현재 이벤트에 대한 메시지와 같이 즉시 발송하려는 일회성 Campaigns를 위해 설계되었습니다. 예를 들어, 스포츠 앱은 이 옵션을 사용하여 점수 업데이트에 대한 푸시 알림을 예약할 수 있습니다. 또한, 본인이나 팀만을 대상으로 테스트 메시지를 발송할 때 이 옵션을 사용하면 즉시 전달할 수 있습니다.

테스트를 확인한 후 Campaign을 편집하고 다시 발송할 계획이라면, 사용자가 Campaign을 [재수신할 수 있도록]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility/) 하는 체크박스를 선택해야 합니다. 기본적으로 Braze는 해당 체크박스가 선택되지 않는 한 사용자에게 Campaign을 한 번만 발송합니다.

## 옵션 2: 지정된 시간에 발송 {#option-2-send-at-a-designated-time}

Campaign을 지정된 시간에 발송하도록 예약하면 Campaign이 발송되는 날짜와 시간을 지정할 수 있습니다. 메시지를 특정 시간에 한 번, 매일, 매주 또는 매월 발송할 수 있으며, Campaign의 시작 및 종료 시점도 지정할 수 있습니다. 이 종료 날짜는 포함되므로, 마지막 발송은 종료 날짜에 이루어집니다.

월간 반복 스케줄을 선택하면, 일부 달에는 선택한 날짜가 없을 수 있습니다. 예를 들어, Campaign을 매월 31일에 발송하도록 설정했다고 가정해 보겠습니다. 이 경우 Braze는 4월 31일이 존재하지 않으므로 4월 30일과 같이 해당 월의 마지막 날에 발송합니다.

**예약 전달**을 선택하고 사용자 현지 시간으로 발송하도록 선택하지 않으면, Campaign은 **회사 설정** 페이지에 지정된 시간대에 따라 발송됩니다.

![지정된 시간에 Campaign을 발송하기 위한 시간 기반 예약 옵션.]({% image_buster /assets/img_archive/schedule_designated.png %})

### 현지 시간대 Campaigns {#local-time-zone-campaigns}

사용자의 현지 시간대로 메시지를 전달하면 해외 오디언스가 불편한 시간에 알림을 받지 않도록 할 수 있습니다. 현지 시간대 Campaigns는 모든 시간대의 적격 사용자가 수신할 수 있도록 24시간 전에 예약해야 합니다. 현지 시간대 Campaigns의 작동 방식과 관련 전달 규칙을 이해하려면 [Campaign FAQ]({{site.baseurl}}/user_guide/messaging/campaigns/faq#how-do-i-schedule-a-local-time-zone-campaign/)를 확인하세요.

현지 시간대 Campaigns로 타겟팅되는 Segments는 모든 시간대의 사용자를 포함하기 위해 최소 2일의 기간을 포함해야 합니다. 예를 들어, Campaign이 저녁에 발송되도록 예약되어 있지만 1일 기간만 설정되어 있다면, 일부 사용자의 시간대에 도달했을 때 해당 사용자가 이미 Segment에서 벗어났을 수 있습니다. 2일 기간을 만드는 필터의 예로는 "1일 전 이후에 마지막으로 사용"과 "3일 전 이전에 마지막으로 사용", 또는 "7일 전 이후에 처음 구매"와 "9일 전 이전에 처음 구매"가 있습니다.

### 활용 사례 {#use-cases}

지정된 시간 스케줄은 사전에 예약된 메시지와 온보딩 및 리텐션과 같이 모든 적격 사용자를 대상으로 정기적으로 실행되는 반복 Campaigns에 가장 적합합니다.

## 옵션 3: Intelligent Timing {#option-3-intelligent-timing}

[Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing/)을 사용하면 각 사용자에게 서로 다른 시간에 Campaign을 전달할 수 있습니다. Braze는 사용자가 일반적으로 앱과 알림에 참여하는 시간을 기반으로 각 개인의 최적 시간을 계산합니다. 선택적으로 Intelligent Timing Campaigns가 하루 중 특정 시간대에만 발송되도록 지정할 수 있습니다. 예를 들어, 자정에 종료되는 프로모션을 사용자에게 알리는 경우, 메시지가 늦어도 오후 10시까지는 발송되도록 할 수 있습니다.

![모든 사용자 중 앱을 가장 많이 사용하는 시간에 Campaign을 발송하기 위해 Intelligent Timing을 사용하는 시간 기반 예약 옵션.]({% image_buster /assets/img_archive/schedule_intelligent.png %})

### 전달 규칙 {#delivery-rules}

사용자의 최적 시간은 24시간 중 언제든지 될 수 있으므로, 모든 Intelligent Timing Campaigns는 24시간 전에 예약해야 합니다. 또한, 지정된 시간 Campaigns와 마찬가지로 1일 기간의 메시지는 해당 시간대에서 최적 시간에 도달하기 전에 Segment에서 벗어난 사용자를 놓칠 수 있습니다. Intelligent Timing Campaigns의 Segments는 이를 고려하여 최소 3일의 기간을 포함해야 합니다.

사용자의 프로필에 최적 시간을 계산하기에 충분한 데이터가 없는 경우, 모든 사용자 중 앱을 가장 많이 사용하는 시간에 발송하거나 설정된 커스텀 대체 시간에 발송하는 백업 방법을 선택할 수 있습니다.

### 활용 사례

Intelligent Timing Campaigns는 속보나 시간이 정해진 공지에는 적합하지 않지만, 전달 시간에 어느 정도 유연성이 있는 일회성 및 반복 메시지에 가장 효과적입니다.

## 지연이 있는 오디언스 기준 평가 {#audience-criteria-evaluation-with-delays}

예약 전달을 사용하는 Campaigns의 경우, 오디언스 기준은 Campaign이 시작될 때가 아니라 항상 예약된 발송 시점에 평가됩니다. 이는 예약과 발송 사이의 모든 지연에 적용됩니다. 예를 들어, 사용량 제한, 현지 시간대, Intelligent Timing 또는 트리거 스케줄이 이에 해당합니다.

## 문제 해결 {#troubleshooting}

### 예약된 이메일 Campaign이 예상 오디언스 전체에 도달하지 못한 이유는 무엇인가요? {#why-didnt-my-scheduled-email-campaign-reach-the-entire-estimated-audience}

발송 수가 예상 오디언스보다 적을 수 있는 이유는 사용자에게 이메일 주소가 없거나, 이메일을 구독하지 않았거나, 발송 시점에 전달 가능성 필터에 의해 제외되었기 때문입니다. 사용자의 이메일 주소가 최근에 변경된 경우에도 발송 시점에 오디언스 기준이 재평가될 때 적격성에 영향을 줄 수 있습니다. 더 많은 요인에 대해서는 [발송 수가 예상 오디언스 규모보다 적은 이유는 무엇인가요?]({{site.baseurl}}/user_guide/messaging/campaigns/faq/#why-are-sends-lower-than-the-estimated-audience-size)를 참조하세요.

### Campaign이 예약된 시간보다 하루 일찍 발송된 이유는 무엇인가요? {#why-did-my-campaign-send-a-day-before-the-scheduled-time}

Campaign이 **회사 설정**에서 설정한 스케줄보다 일찍 발송된 경우, **현지 시간대로 발송**을 활성화하거나 Intelligent Timing Campaigns에 전달 시간 기간을 추가하세요. 이러한 설정이 없으면 시간대 평가로 인해 의도한 스케줄 시간보다 이른 시간대의 사용자에게 발송이 대기열에 추가될 수 있습니다. 자세한 내용은 [현지 시간대 Campaigns](#local-time-zone-campaigns) 및 [Braze는 현지 시간대 전달을 위해 사용자를 언제 평가하나요?]({{site.baseurl}}/user_guide/messaging/campaigns/faq/#when-does-braze-evaluate-users-for-local-time-zone-delivery)를 참조하세요.