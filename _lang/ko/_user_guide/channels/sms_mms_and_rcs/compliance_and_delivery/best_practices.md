---
nav_title: "모범 사례"
article_title: SMS, MMS, RCS 모범 사례
page_order: 2
description: "이 참조 문서에서는 SMS/MMS 모범 사례를 다룹니다."
alias: /sms_mms_rcs_best_practices/
page_type: reference
channel:
  - SMS
  - MMS
  - RCS


---

# SMS, MMS, RCS 모범 사례 {#best-practices-for-sms-mms-and-rcs}

> 옵트아웃 모니터링 및 트래픽 펌핑에 대한 권장 사항을 포함하여 Braze에서의 SMS, MMS, RCS 모범 사례에 대해 자세히 알아보세요.

## 수신 거부 모니터링 권장 사항 {#opt-out-monitoring-recommendations}

커뮤니케이션 수신 거부 요청을 준수하는 것은 법적 의무입니다. SMS 수신자의 채널 수신 거부 요청을 준수하지 않으면 벌금 등의 처벌을 받을 수 있으며 소송으로 이어질 수 있습니다. Braze는 SMS 및 MMS 옵트인/수신 거부 관리를 효과적으로 지원하는 기능을 갖추고 있으며, 요청이 올바르게 처리되도록 돕는 메커니즘도 제공합니다.

당사와의 구독 계약에 따라, 고객은 당사 서비스 이용 시 관련 법률 준수에 대해 전적으로 책임을 집니다. 이에 따라 고객이 SMS 설정을 올바르게 구성하는 데 각별히 주의를 기울이고, 해당 설정을 철저히 테스트하며, 수신 거부 준수 여부를 모니터링하기 위한 조치를 취하고, 수신 거부 요청 미준수 사례가 확인될 경우 신속하게 대응할 것을 강력히 권장합니다.

Braze에서 옵트인 및 수신 거부를 관리하기 위해 SMS 및 MMS를 설정할 때, 다음 리소스 목록을 참고하세요:
* [SMS 구독 그룹]({{site.baseurl}}/sms_rcs_subscription_groups): 구독 그룹과 옵트인/수신 거부 방법 및 상태에 대한 안내입니다.
* [구독 그룹 REST API]({{site.baseurl}}/api/endpoints/subscription_groups): 메시지에 대한 직접 응답이 아닌 다른 소스에서 수신한 옵트인 및 수신 거부를 처리하는 방법입니다.
* [키워드 처리]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing): Braze가 키워드 처리 및 관리에 접근하는 방식에 대한 설명입니다.
* [SMS 이중 옵트인]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/double_opt_in): 사용자가 SMS 메시지를 수신하기 전에 옵트인 의사를 명시적으로 확인해야 합니다. SMS 이중 옵트인은 일부 국가에서 필수 요건이므로, Braze는 이를 구성할 것을 권장합니다.
* [SMS 메시지 발송]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sms_sending): Braze의 SMS 발송 기본 사항으로, 구독 그룹의 중요성, SMS 세그먼트 및 메시지 본문 요구 사항 등을 다룹니다.

### 고려 사항 {#considerations}

SMS 및 MMS가 여러 인스턴스에 걸쳐 설정된 경우, 잘못된 구성으로 인해 Campaign 또는 Canvas 수신 거부가 잘못된 워크스페이스로 전송될 수 있습니다.

* Braze는 이러한 사례를 식별하기 위한 모니터링 체계를 갖추고 있습니다. 이 동작이 감지되면 Braze는 해당 수신 거부를 올바른 인스턴스에 적용하고, 해당 기간 동안 발생한 모든 건을 소급 처리합니다.
* 고객이 Braze에 설정한 각 구독 그룹에 대해 수신 거부를 테스트할 것을 강력히 권장합니다. 메시지 발송 전에 이 문제를 파악하는 것이 문제가 발견된 후 대응하는 것보다 훨씬 효과적입니다.

Braze는 사용자 프로필(`user_id`) 수준과 전화번호(`channel_id`) 수준 모두에서 SMS/MMS 구독을 관리합니다. 전화번호가 옵트인 또는 수신 거부되면 해당 번호를 공유하는 모든 프로필에 업데이트가 적용됩니다. 사용자가 특정 전화번호로 옵트인한 후 전화번호를 변경한 경우, 새 전화번호는 해당 사용자의 구독 그룹 상태를 상속받습니다. 따라서 사용자가 수신 거부한 후 새 전화번호로 앱이나 웹사이트에 다시 접속하더라도 원치 않는 메시지를 수신하지 않습니다.

## 전화번호 목록 위생 관리 권장 사항 {#phone-number-list-hygiene-recommendations}

전화번호 목록 위생을 유지하면 시간이 지나도 유효한 동의 및 도달 가능성 데이터를 보존할 수 있습니다. Braze는 규정 준수 위험을 줄이고, 동의 기반 메시징 관행을 지원하며, 원래 사용자에게 더 이상 속하지 않을 수 있는 번호로의 발송을 방지하기 위해 일부 전화번호를 유효하지 않음으로 표시합니다.

전화번호가 유효하지 않음으로 표시되는 일반적인 이유에 대해서는 [유효하지 않은 전화번호 처리]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/user_phone_numbers#handling-invalid-phone-numbers)를 참조하세요.

유효하지 않은 전화번호를 제거하기 위해 다음 워크플로를 권장합니다.

1. [`/sms/invalid_phone_numbers` 엔드포인트]({{site.baseurl}}/api/endpoints/sms/get_query_invalid_numbers)를 통해 영향을 받는 전화번호를 식별합니다.
2. 비활성화된 전화번호와 통신사 오류가 발생한 전화번호를 구분합니다.
3. 비활성화된 전화번호의 경우, 사용자에게 전화번호를 다시 확인합니다. 사용자가 전화번호를 확인한 후 [`/sms/invalid_phone_numbers/remove` 엔드포인트]({{site.baseurl}}/api/endpoints/sms/post_remove_invalid_numbers)를 통해 유효하지 않은 목록에서 전화번호를 제거합니다.

## 트래픽 펌핑 권장 사항 {#traffic-pumping-recommendations}

### 트래픽 펌핑이란? {#what-is-traffic-pumping}

트래픽 펌핑은 악의적인 행위자가 온라인 양식을 사용하여 대량의 SMS 메시지(예: 옵트인 메시지 또는 일회용 비밀번호)가 발송되도록 트리거하는 사기 행위입니다. 악의적인 행위자는 이러한 메시지가 발송될 프리미엄 요금 전화번호를 설정하고, 해당 프리미엄 요금 번호가 설정된 이동통신사로부터 수익을 분배받아 불법 수익을 창출합니다.

### 트래픽 펌핑을 식별하는 방법 {#how-to-spot-traffic-pumping}

* 이런 종류의 사기를 지원하는 프리미엄 요금 번호는 항상 그런 것은 아니지만, 일반적인 발송 지역 이외의 국가에 설정되는 경우가 많습니다.
* 온라인 양식에서 비정상적으로 메시지 발송이 급증하는 것은 트래픽 펌핑을 나타낼 수 있습니다.
    * 비합리적으로 많은 수의 메시지가 발송될 경우 한도를 설정하고 알림을 받을 수 있도록 [Campaign 알림]({{site.baseurl}}/user_guide/messaging/campaigns/manage_campaigns/campaign_alerts)을 설정하는 것을 권장합니다.
* 불완전한 온라인 양식은 프로그래밍 방식의 양식 자동 입력을 나타낼 수 있습니다.
* 온라인 양식을 구축할 때, 양식이 완전히 작성되었는지 확인하는 규칙을 설정하고 CAPTCHA와 같은 도구를 사용하여 위험을 최소화하는 것을 권장합니다.

### 트래픽 펌핑의 영향 {#impact-of-traffic-pumping}

고객은 발송하는 트래픽을 모니터링할 책임이 있으며, 계정을 통해 발송된 모든 SMS에 대해 비용이 청구됩니다. Braze와 고객 사이에서 고객이 트래픽 펌핑을 감지하고 방지하기에 더 적합한 위치에 있는 당사자입니다.

## 다국가 SMS 발송 {#multi-country-sms-sending}

일부 브랜드는 서로 다른 국가의 전화번호를 보유한 사용자 그룹에 메시지를 발송하고자 할 수 있습니다. 특정 국가의 전화번호로 SMS 메시지를 발송하려면, 해당 국가에서 발급된 긴 코드 또는 짧은 코드를 사용하는 것이 모범 사례입니다. 실제로 짧은 코드는 해당 짧은 코드가 생성된 국가의 전화번호로만 SMS를 발송할 수 있습니다.

이러한 제한을 극복하기 위해, 구독 그룹 [설정 프로세스]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups) 중에 여러 국가의 긴 코드와 짧은 코드를 포함하는 그룹을 설정할 수 있습니다. 설정이 완료되면 Campaign을 시작할 때 대상 사용자의 전화번호와 동일한 국가 코드를 가진 발신 전화번호가 자동으로 사용됩니다. 서로 다른 국가 코드의 전화번호를 가진 사용자를 위해 별도의 Campaign을 만들 필요 없이, 하나의 Campaign 또는 하나의 Canvas 구성 요소를 사용하여 관련 사용자를 타겟팅할 수 있습니다.

![대상 사용자의 전화번호와 동일한 국가 코드를 사용하여 SMS 페이로드가 발송됩니다.]({% image_buster /assets/img/sms/multi_country_subgroups.png %})

### 일반 발송 모범 사례 {#general-sending-best-practices}

1. **허가를 받으세요.** 비즈니스에서 SMS를 사용할 때 가장 중요한 규칙 중 하나는 고객에게 연락하기 전에 먼저 허가를 받아야 한다는 것입니다. 이를 지키지 않으면 브랜드 이미지가 손상되고 막대한 법적 비용이 발생할 수 있습니다.
2. **사용 사례에 맞는 번호를 선택하세요.** SMS 메시지를 발송하고 수신할 수 있는 전화번호에는 긴 코드, 짧은 코드, 영숫자 발신자 ID의 세 가지 주요 유형이 있으며, 지역에 따라 기능과 가용성이 다릅니다. 비즈니스에 배니티 코드가 더 적합한지 미리 검토하세요.
3. **타이밍에 주의하세요.** 고객은 자신에게 직접 전달되는 콘텐츠에 더 잘 반응한다는 점을 기억하세요. 수신자의 이름을 사용하거나 고객의 관심사를 반영하는 대화식 톤을 추가하는 등 약간의 개인화만으로도 큰 효과를 얻을 수 있습니다.
4. **양방향 대화에 참여하세요.** SMS는 고객과 소통하는 데 매우 효과적인 채널이므로, 메시지에 대한 응답을 예상하고 효과적으로 처리하는 것이 중요합니다. 소비자의 85%는 정보를 수신하는 것뿐만 아니라 비즈니스에 답장하거나 대화에 참여할 수 있기를 원합니다.
5. **효과가 있는 것을 측정하세요.** 적절한 시간에, 최적의 빈도로, 가장 효과적인 행동 유도 문구를 사용하여 고객에게 도달하고 있나요? 올바른 추적 도구를 사용하면 ROI를 입증하는 직접적이고 측정 가능한 측정기준을 제공받을 수 있습니다.

## 대량 발송 {#high-volume-sending}

대량 발송을 계획하고 계신가요? 원활하게 진행할 수 있도록 몇 가지 모범 사례를 안내해 드립니다.

- 타겟 오디언스 규모에 따라 Campaign 또는 Canvases의 전송 속도 사용량 제한을 필요에 맞게 조정하세요. 이렇게 하면 필요한 발송량에 도달할 수 있으며, Braze가 Twilio에서 예상하고 처리할 수 있는 속도로 메시지를 발송할 수 있습니다.
- 160자 제한을 준수하고, 특수 문자가 두 배로 카운트될 수 있다는 점에 유의하세요(예: 슬래시 `\`, 캐럿 `^`, 물결표 `~`).

## 방해금지 시간 권장 사항 {#quiet-hours-recommendations}

{% alert warning %}
**Braze 기본 방해금지 시간은 기기 수준의 전달 시간을 보장하지 않습니다.** 메시지가 발송되면 통신사에 전달됩니다. 통신사가 메시지를 수락하면, Braze는 사용자의 기기에 메시지가 전달되는 정확한 시점을 더 이상 제어할 수 없습니다.<br><br> 예를 들어, 메시지가 오후 8시 59분에 통신사에 전달되었더라도 기기에는 오후 9시 2분에 도착할 수 있습니다. 이러한 위험을 줄이기 위해 다음의 Liquid 기반 방해금지 시간 방법을 사용하는 것을 권장합니다. 이 방법은 전달 전에 Braze 엔진 수준에서 메시지를 억제합니다.
{% endalert %}

### Braze 기본 방해금지 시간 {#braze-native-quiet-hours}

모든 SMS Campaign 및 Canvases에서 지역 규정과 모범 사례를 준수할 수 있도록 [방해금지 시간]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing#quiet-hours)을 활성화할 것을 적극 권장합니다.

### Content Blocks를 통한 추가 보호 조치 {#additional-safeguard-through-content-blocks}

Liquid 기반 확인 로직을 Content Blocks에 추가할 수 있습니다. 이 방법은 기본 설정과 함께 작동하는 안정적이고 확장 가능한 보호 조치를 제공합니다.

#### 설정 {#setup}

SMS 메시지 본문 상단에 다음 스니펫을 포함하세요. 이 예시는 사용자의 [현지 시간대]({{site.baseurl}}/user_guide/messaging/campaigns/faq#what-does-local-time-zone-delivery-offer) 기준으로 오전 9시~오후 9시 범위를 벗어날 경우 발송을 중단합니다.

{% raw %}
```liquid
{% assign time = 'now' | time_zone: ${time_zone} %}
{% assign hour = time | date: '%H' | plus: 0 %}
{% if hour >= 21 or hour < 9 %}
  {% abort_message("Outside allowed time window") %}
{% endif %}
```
{% endraw %}

#### 고려 사항

- {% raw %}`time_zone: ${time_zone}`{% endraw %}을 사용하면 고정된 글로벌 시간이 아닌 각 사용자의 현지 시간을 기준으로 시간 범위를 평가할 수 있습니다. 자세한 내용은 [Campaigns FAQ]({{site.baseurl}}/user_guide/messaging/campaigns/faq#what-does-local-time-zone-delivery-offer)를 참조하세요.
- {% raw %}`abort_message()`{% endraw %}에 의해 억제된 메시지는 다음 날로 재스케줄되지 않으며, 취소됩니다.
- {% raw %} 기본적으로 중단된 메시지는 표준 Campaign 리포트에 표시되지 않습니다. 그러나 Liquid가 `{% abort_message %}`로 발송을 중단하면, Braze는 이를 메시지 활동 로그에 메시지 오류로 기록합니다(기본적으로 `{% abort_message %}`가 호출된 것으로 표시됩니다). 문자열을 전달하면 해당 이유가 로그에 표시됩니다. 예: `{% abort_message('language was nil') %}`{% endraw %}. 대시보드에서 이러한 억제 내역을 확인하려면 고객 성공 매니저에게 연락하여 [메시징 진단 대시보드]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/diagnostics_dashboard)에 대한 접근 권한을 요청하세요.