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

![Campaign이 시작되는 즉시 발송하는 시간 기반 스케줄 옵션과 함께 "예약됨"이 선택된 "전달" 섹션.]({% image_buster /assets/img_archive/schedule_immediately.png %})

이 유형의 스케줄은 현재 진행 중인 이벤트에 대한 메시지처럼 즉시 발송하려는 일회성 Campaign을 위해 설계되었습니다. 예를 들어, 스포츠 앱에서는 이 옵션을 사용하여 점수 업데이트에 대한 푸시 알림을 스케줄할 수 있습니다. 또한, 본인이나 팀에게만 보내는 테스트 메시지를 발송할 때 이 옵션을 사용하면 즉시 전달할 수 있습니다.

Campaign을 수정하고 테스트를 확인한 후 다시 발송할 계획이라면, 사용자가 Campaign을 다시 받을 수 있도록 [재자격]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility) 체크박스를 선택해야 합니다. 기본적으로 Braze는 해당 체크박스가 선택되지 않는 한 사용자에게 Campaign을 한 번만 발송합니다.

## 옵션 2: 지정된 시간에 발송 {#option-2-send-at-a-designated-time}

Campaign을 지정된 시간에 발송하도록 스케줄하면 Campaign이 발송되는 요일과 시간을 지정할 수 있습니다. 특정 시간에 한 번, 매일, 매주 또는 매월 메시지를 발송할 수 있으며, Campaign의 시작일과 종료일도 지정할 수 있습니다. 이 종료일은 포함 기준이므로 마지막 발송은 종료일에 이루어집니다.

월간 반복 스케줄을 선택하는 경우, 일부 월에는 선택한 날짜가 없을 수 있다는 점에 유의하세요. 예를 들어, Campaign을 매월 31일에 발송하도록 설정했다고 가정해 보겠습니다. 이 경우 Braze는 해당 월의 마지막 날에 발송합니다. 예를 들어 4월 31일은 존재하지 않으므로 4월 30일에 발송됩니다.

**Scheduled Delivery**를 선택하고 사용자 현지 시간으로 발송하도록 선택하지 않으면, Campaign은 **Company Settings** 페이지에 지정된 시간대에 따라 발송됩니다.

![지정된 시간에 Campaign을 발송하기 위한 시간 기반 스케줄 옵션.]({% image_buster /assets/img_archive/schedule_designated.png %})

### 현지 시간대 Campaign {#local-time-zone-campaigns}

사용자의 현지 시간대에 맞춰 메시지를 전달하면 해외 오디언스가 불편한 시간에 알림을 받지 않도록 할 수 있습니다. 현지 시간대 Campaign은 모든 시간대의 적격 사용자가 수신할 수 있도록 최소 24시간 전에 스케줄해야 합니다. 현지 시간대 Campaign의 작동 방식과 관련 전달 규칙에 대해 자세히 알아보려면 [Campaign FAQ]({{site.baseurl}}/user_guide/messaging/campaigns/faq#how-do-i-schedule-a-local-time-zone-campaign)를 확인하세요.

현지 시간대 Campaign의 대상 Segment에는 모든 시간대의 사용자를 포함할 수 있도록 최소 2일의 기간을 설정해야 합니다. 예를 들어, Campaign이 저녁에 발송되도록 스케줄되어 있지만 기간이 1일뿐이라면, 해당 시간대에 도달했을 때 일부 사용자가 이미 Segment에서 벗어났을 수 있습니다. 2일 기간을 만드는 필터의 예로는 "1일 전보다 이전에 마지막 사용"과 "3일 전보다 이내에 마지막 사용", 또는 "7일 전보다 이전에 첫 구매"와 "9일 전보다 이내에 첫 구매"가 있습니다.

### 사용 사례 {#use-cases}

지정된 시간 스케줄은 사전에 예약된 메시지와 온보딩 및 유지 등 모든 적격 사용자를 대상으로 정기적으로 실행되는 반복 Campaign에 가장 적합합니다.

## 옵션 3: Intelligent Timing {#option-3-intelligent-timing}

[Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing)을 사용하면 각 사용자에게 서로 다른 시간에 Campaign을 전달할 수 있습니다. Braze는 해당 사용자가 일반적으로 앱 및 알림에 참여하는 시간을 기반으로 각 개인의 최적 시간을 계산합니다. 선택적으로 Intelligent Timing Campaign이 하루 중 특정 시간대에만 발송되도록 지정할 수 있습니다. 예를 들어, 자정에 종료되는 프로모션을 사용자에게 알리는 경우 메시지가 늦어도 오후 10시까지는 발송되도록 설정할 수 있습니다.

![Intelligent Timing을 사용하여 모든 사용자 중 앱을 가장 많이 사용하는 시간에 Campaign을 발송하는 시간 기반 스케줄 옵션입니다.]({% image_buster /assets/img_archive/schedule_intelligent.png %})

### 전달 규칙 {#delivery-rules}

사용자의 최적 시간은 모든 글로벌 시간대에 걸쳐 24시간 중 어느 때든 될 수 있으므로, 모든 Intelligent Timing Campaign은 48시간 전에 스케줄해야 합니다. 48시간 전에 스케줄하면 하루가 모든 시간대에 걸쳐 약 48시간에 해당하므로 전 세계 모든 사용자에게 전달할 수 있습니다. 또한 지정 시간 Campaign과 마찬가지로, 1일 기간의 메시지는 해당 시간대에서 최적 시간이 도달하기 전에 Segment에서 이탈한 사용자에게는 전달되지 않습니다. Intelligent Timing Campaign의 Segments는 이를 고려하여 최소 3일의 기간을 포함해야 합니다.

사용자의 프로필에 최적 시간을 계산할 충분한 데이터가 없는 경우, 모든 사용자 중 앱을 가장 많이 사용하는 시간에 발송하거나 설정된 커스텀 대체 시간에 발송하는 백업 방법을 선택할 수 있습니다.

### 사용 사례

Intelligent Timing Campaign은 속보나 시간이 정해진 공지에는 적합하지 않지만, 전달 시간에 어느 정도 유연성이 있는 일회성 및 반복 메시지에 가장 적합합니다.

## 지연이 있는 오디언스 기준 평가 {#audience-criteria-evaluation-with-delays}

스케줄 전달을 사용하는 Campaigns의 경우, 오디언스 기준은 Campaign이 시작될 때가 아니라 항상 스케줄된 전송 시점에 평가됩니다. 이는 스케줄과 전송 사이의 모든 지연에 적용됩니다. 예를 들어 사용량 제한조치, 현지 시간대, Intelligent Timing 또는 트리거 스케줄 등이 해당됩니다.

### Segment 변경 시점 {#timing-of-segment-changes}

스케줄된 Campaign의 오디언스로 사용 중인 Segment를 수정하면, 스케줄된 전송 시간에 가까운 시점에 이루어진 변경 사항도 오디언스 평가 시 일반적으로 포함됩니다. 정확한 마감 시점은 다를 수 있지만, Braze가 해당 전송을 위한 오디언스를 구성하기 전에 처리가 완료되면 변경 사항이 대체로 반영됩니다.

예를 들어, 오후 4시에 전송하도록 스케줄된 Campaign에 대해 오후 3시 50분에 Segment를 업데이트하면, Campaign 실행이 시작되기 전에 변경 처리가 완료된다는 전제 하에 Braze는 업데이트된 Segment 기준을 사용하여 오디언스를 평가합니다.

#### 모범 사례 {#best-practices}

스케줄된 Campaigns가 전송되기 전에 Segment 변경 사항이 처리를 완료할 수 있도록 다음을 권장합니다.

- **미리 계획하세요:** 스케줄된 전송 시간보다 충분히 앞서 Segment를 변경하여 처리가 완료될 시간을 확보하세요.
- **먼저 테스트하세요:** 가능하다면, 더 크고 중요한 Campaigns에 적용하기 전에 소규모 Campaign에서 변경 사항을 먼저 테스트하세요.

스케줄 전달 옵션에 대한 자세한 내용은 [전달 및 진입 유형]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/delivery_and_entry_types#time-based-options)을 참조하세요.

## 문제 해결 {#troubleshooting}

### 스케줄된 이메일 Campaign이 예상 오디언스 전체에 도달하지 못한 이유는 무엇인가요? {#why-didnt-my-scheduled-email-campaign-reach-the-entire-estimated-audience}

발송 수가 예상 오디언스보다 적을 수 있는 이유는 사용자에게 이메일 주소가 없거나, 이메일 수신에 동의하지 않았거나, 발송 시점에 전달 가능성 필터에 의해 제외되었기 때문입니다. 최근 사용자의 이메일 주소가 변경된 경우에도 오디언스 기준이 발송 시 재평가될 때 자격에 영향을 줄 수 있습니다. 더 많은 요인에 대해서는 [발송 수가 예상 오디언스 규모보다 적은 이유는 무엇인가요?]({{site.baseurl}}/user_guide/messaging/campaigns/faq#why-are-sends-lower-than-the-estimated-audience-size)를 참조하세요.

### Campaign이 스케줄된 시간보다 하루 일찍 발송된 이유는 무엇인가요? {#why-did-my-campaign-send-a-day-before-the-scheduled-time}

**회사 설정**에서 지정한 스케줄보다 Campaign이 일찍 발송되는 경우, **현지 시간대로 발송**을 활성화하거나 Intelligent Timing Campaign에 전달 시간 창을 추가하세요. 이러한 설정이 없으면 시간대 평가로 인해 더 이른 시간대에 있는 사용자에게 의도한 스케줄 시간보다 먼저 발송이 대기줄에 추가될 수 있습니다. 자세한 내용은 [현지 시간대 Campaign](#local-time-zone-campaigns) 및 [Braze는 현지 시간대 전달을 위해 사용자를 언제 평가하나요?]({{site.baseurl}}/user_guide/messaging/campaigns/faq#when-does-braze-evaluate-users-for-local-time-zone-delivery)를 참조하세요.