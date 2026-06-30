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

## 옵트아웃 모니터링 권장 사항 {#opt-out-monitoring-recommendations}

수신 거부 요청을 준수하는 것은 법적으로 필수입니다. SMS 수신자의 채널 옵트아웃 요청을 준수하지 않으면 벌금을 포함한 제재를 받을 수 있으며 소송으로 이어질 수 있습니다. Braze는 강력한 SMS 및 MMS 옵트인/옵트아웃 관리를 지원하는 기능과 요청이 올바르게 처리되도록 돕는 메커니즘을 갖추고 있습니다.

당사와의 구독 계약에 따라 고객은 당사 서비스 이용 시 관련 법률 준수에 대한 전적인 책임을 집니다. 따라서 고객이 SMS 설정을 올바르게 구성하는 데 세심한 주의를 기울이고, 해당 설정을 철저히 테스트하며, 옵트아웃 준수를 모니터링하기 위한 조치를 취하고, 옵트아웃 요청 미준수 사례를 발견할 경우 신속하게 조치할 것을 강력히 권장합니다.

Braze에서 SMS 및 MMS의 옵트인/옵트아웃을 관리하도록 설정할 때 다음 리소스 목록을 참조하세요:
* [SMS 구독 그룹]({{site.baseurl}}/sms_rcs_subscription_groups): 구독 그룹 및 옵트인/옵트아웃 방법과 상태.
* [구독 그룹 REST API]({{site.baseurl}}/api/endpoints/subscription_groups): 메시지에 대한 직접 응답이 아닌 다른 소스에서 수신한 옵트인 및 옵트아웃을 처리하는 방법.
* [키워드 처리]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing): Braze가 키워드 처리 및 관리에 접근하는 방식에 대한 설명.
* [SMS 이중 옵트인]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/double_opt_in): 사용자가 SMS 메시지를 수신하기 전에 옵트인 의사를 명시적으로 확인하도록 요구합니다. SMS 이중 옵트인은 일부 국가에서 필수이므로 Braze는 이를 구성할 것을 권장합니다.
* [SMS 메시지 발송]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sms_sending): 구독 그룹의 중요성, SMS 세그먼트 및 메시지 본문 요구 사항 등 Braze에서의 SMS 발송 기본 사항.

### 고려 사항 {#considerations}

SMS 및 MMS가 여러 인스턴스에 걸쳐 설정되어 있고 잘못된 구성으로 인해 Campaign 또는 Canvas 옵트아웃이 잘못된 워크스페이스로 전송되는 경우가 있습니다.

* Braze는 이러한 사례를 식별하기 위한 모니터링을 갖추고 있습니다. 이 동작이 감지되면 Braze는 옵트아웃을 올바른 인스턴스로 재지정하고 해당 기간 동안 발생한 옵트아웃을 소급 적용합니다.
* 고객이 Braze에 있는 각 구독 그룹에 대해 옵트아웃을 테스트할 것을 강력히 권장합니다. 메시지를 발송하기 전에 이 문제를 식별하는 것이 문제가 발견된 후 완화하는 것보다 낫습니다.

Braze는 고객 프로필(`user_id`) 수준과 전화번호(`channel_id`) 수준 모두에서 SMS/MMS 구독을 관리합니다. 전화번호가 옵트인 또는 옵트아웃되면 해당 번호를 공유하는 모든 프로필에 업데이트가 적용됩니다. 최종 사용자가 특정 전화번호로 옵트인한 후 전화번호를 변경하는 경우, 새 전화번호는 해당 사용자의 구독 그룹 상태를 상속합니다. 따라서 최종 사용자가 옵트아웃한 후 새 전화번호로 앱이나 웹사이트에 다시 접속하더라도 원치 않는 메시지를 수신하지 않습니다.

## 전화번호 목록 위생 권장 사항 {#phone-number-list-hygiene-recommendations}

전화번호 목록 위생을 유지하면 시간이 지나도 유효한 동의 및 도달 가능성 데이터를 보존할 수 있습니다. Braze는 규정 준수 위험을 줄이고, 동의 기반 메시징 관행을 지원하며, 원래 사용자에게 더 이상 속하지 않을 수 있는 번호로의 발송을 방지하기 위해 일부 전화번호를 유효하지 않음으로 표시합니다.

전화번호가 유효하지 않음으로 표시되는 일반적인 이유는 [유효하지 않은 전화번호 처리]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/user_phone_numbers#handling-invalid-phone-numbers)를 참조하세요.

유효하지 않은 전화번호를 제거하기 위해 다음 워크플로를 권장합니다:

1. [`/sms/invalid_phone_numbers` 엔드포인트]({{site.baseurl}}/api/endpoints/sms/get_query_invalid_numbers)를 통해 영향을 받는 전화번호를 식별합니다.
2. 비활성화된 전화번호와 통신사 오류를 수신한 전화번호를 구분합니다.
3. 비활성화된 전화번호의 경우 사용자에게 전화번호를 재확인합니다. 사용자가 전화번호를 확인한 후 [`/sms/invalid_phone_numbers/remove` 엔드포인트]({{site.baseurl}}/api/endpoints/sms/post_remove_invalid_numbers)를 통해 유효하지 않은 목록에서 전화번호를 제거합니다.

## 트래픽 펌핑 권장 사항 {#traffic-pumping-recommendations}

### 트래픽 펌핑이란? {#what-is-traffic-pumping}

트래픽 펌핑은 악의적인 행위자가 온라인 양식을 사용하여 대량의 SMS 메시지(예: 옵트인 메시지 또는 일회용 비밀번호)를 발송하도록 유도하는 사기 형태입니다. 악의적인 행위자는 이러한 메시지가 전송될 프리미엄 요금 전화번호를 설정하고, 프리미엄 요금 번호가 설정된 이동통신사와의 수익 분배를 청구하여 불법 수익을 창출합니다.

### 트래픽 펌핑을 식별하는 방법 {#how-to-spot-traffic-pumping}

* 이러한 종류의 사기를 지원하는 프리미엄 요금 번호는 항상 그런 것은 아니지만, 일반적인 발송 지역 외의 국가에 설정되는 경우가 많습니다.
* 온라인 양식에서의 비정상적인 메시지 발송 급증은 트래픽 펌핑을 나타낼 수 있습니다.
    * 비현실적으로 많은 수의 메시지가 발송될 경우 상한을 설정하고 알림을 받을 수 있도록 [Campaign 알림]({{site.baseurl}}/user_guide/messaging/campaigns/manage_campaigns/campaign_alerts)을 설정하는 것을 권장합니다.
* 불완전한 온라인 양식은 프로그래밍 방식의 양식 작성을 나타낼 수 있습니다.
* 온라인 양식을 구축할 때 양식이 완전히 작성되도록 규칙을 설정하고 CAPTCHA와 같은 도구를 사용하여 위험을 최소화하는 것을 권장합니다.

### 트래픽 펌핑의 영향 {#impact-of-traffic-pumping}

고객은 발송하는 트래픽을 모니터링할 책임이 있으며, 계정을 통해 발송된 모든 SMS에 대해 청구됩니다. Braze와 고객 사이에서 고객이 트래픽 펌핑을 감지하고 방지하기에 더 유리한 위치에 있습니다.

## 다국가 SMS 발송 {#multi-country-sms-sending}

일부 브랜드는 서로 다른 국가의 전화번호를 가진 사용자 그룹에 발송하기를 원할 수 있습니다. 특정 국가의 전화번호로 SMS 메시지를 보내려면 동일한 국가의 긴 코드 또는 짧은 코드를 사용하는 것이 모범 사례입니다. 실제로 짧은 코드는 해당 짧은 코드가 생성된 동일한 국가의 전화번호로만 SMS를 보낼 수 있습니다.

이 제한을 극복하기 위해 구독 그룹 [설정 프로세스]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups) 중에 여러 국가의 긴 코드와 짧은 코드를 포함하도록 그룹을 설정할 수 있습니다. 완료되면 Campaign을 시작할 때 타겟 사용자의 전화번호와 동일한 국가 코드를 가진 발송 전화번호가 자동으로 사용됩니다. 서로 다른 국가 코드의 전화번호를 가진 사용자를 위해 별도의 Campaign을 만들 필요 없이 하나의 Campaign을 시작하거나 하나의 Canvas 구성요소를 사용하여 관련 사용자를 타겟팅할 수 있습니다.

![SMS 페이로드는 타겟 사용자의 전화번호와 동일한 국가 코드를 사용하여 발송됩니다.]({% image_buster /assets/img/sms/multi_country_subgroups.png %})

### 일반 발송 모범 사례 {#general-sending-best-practices}

1. **허가를 받으세요.** 비즈니스에서 SMS를 사용할 때 가장 중요한 규칙 중 하나는 먼저 고객에게 연락할 수 있는 허가를 받아야 한다는 것입니다. 이를 지키지 않으면 브랜드에 손상을 줄 수 있으며 막대한 법적 비용이 발생할 수 있습니다.
2. **사용 사례에 적합한 번호를 선택하세요.** SMS 메시지를 보내고 받을 수 있는 세 가지 주요 유형의 전화번호는 긴 코드, 짧은 코드, 영숫자 발신자 ID이며, 각각의 기능과 지역별 가용성이 다릅니다. 비즈니스에 맞춤형 코드가 더 적합한지 미리 생각해 보세요.
3. **타이밍에 주의하세요.** 고객은 자신에게 직접 전달되는 자료에 더 잘 반응한다는 점을 기억하세요. 수신자의 이름을 사용하거나 고객의 관심사를 반영하는 대화체 터치를 추가하는 등 약간의 개인화가 큰 효과를 발휘합니다.
4. **양방향 대화에 참여하세요.** SMS는 고객과 소통하는 데 매우 효과적인 채널이므로 메시지에 대한 응답을 예상하고 효과적으로 처리하는 것이 중요합니다. 소비자의 85%는 정보를 수신하는 것뿐만 아니라 비즈니스에 답장하거나 대화에 참여하기를 원합니다.
5. **효과를 측정하세요.** 적절한 시간에, 최적의 빈도로, 가장 효과적인 행동 유도 문구를 사용하여 고객에게 도달하고 있나요? 적절한 추적 도구를 사용하면 ROI를 입증하는 직접적이고 측정 가능한 측정기준을 제공할 수 있습니다.

## 대량 발송 {#high-volume-sending}

대량 발송을 계획하고 계신가요? 원활하게 진행되도록 몇 가지 모범 사례를 안내해 드립니다.

- 타겟 오디언스 규모에 따라 Campaign 또는 Canvases의 전달 속도 사용량 제한을 필요에 맞게 조정하세요. 이를 통해 필요한 발송량에 도달하고 Braze가 Twilio가 예상하고 처리할 수 있는 속도로 메시지를 발송할 수 있습니다.
- 160자 제한을 준수하고, 특수 문자가 두 배로 계산된다는 점에 유의하세요(예: 슬래시 `\`, 캐럿 `^`, 물결표 `~`).

## 방해금지 시간 권장 사항 {#quiet-hours-recommendations}

{% alert warning %}
**Braze 기본 방해금지 시간은 기기 수준의 전달 시간을 보장하지 않습니다.** 메시지가 발송되면 통신사에 전달됩니다. 통신사가 메시지를 수락하면 Braze는 사용자의 기기에 정확히 언제 전달되는지 더 이상 제어할 수 없습니다.<br><br> 예를 들어, 메시지가 오후 8시 59분에 통신사에 전달되었더라도 기기에는 오후 9시 2분에 도착할 수 있습니다. 위험을 줄이기 위해 다음의 Liquid 기반 방해금지 시간 방법을 사용하는 것을 권장합니다. 이 방법은 통신사에 전달되기 전에 Braze 엔진 수준에서 메시지를 억제합니다.
{% endalert %}

### Braze 기본 방해금지 시간 {#braze-native-quiet-hours}

모든 SMS Campaign 및 Canvases에서 [방해금지 시간]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing#quiet-hours)을 활성화하여 지역 규정 및 모범 사례를 준수할 것을 강력히 권장합니다.

### Content Blocks를 통한 추가 보호 {#additional-safeguard-through-content-blocks}

콘텐츠 블록 내에 Liquid 기반 검사를 추가할 수 있습니다. 이는 기본 설정과 함께 작동하는 안정적이고 확장 가능한 보호 장치를 제공합니다.

#### 설정 {#setup}

SMS 메시지 본문 상단에 다음 스니펫을 포함하세요. 이 예시는 사용자의 [현지 시간대]({{site.baseurl}}/user_guide/messaging/campaigns/faq#what-does-local-time-zone-delivery-offer)를 기준으로 오전 9시~오후 9시 범위를 벗어나는 경우 발송을 중단합니다.

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

- {% raw %}`time_zone: ${time_zone}`{% endraw %}를 사용하면 고정된 글로벌 시간이 아닌 각 사용자의 현지 시간을 기준으로 시간 범위를 평가할 수 있습니다. 자세한 내용은 [이 FAQ]({{site.baseurl}}/user_guide/messaging/campaigns/faq#what-does-local-time-zone-delivery-offer)를 참조하세요.
- {% raw %}`abort_message()`{% endraw %}에 의해 억제된 메시지는 다음 날로 재스케줄되지 않으며 취소됩니다.
- {% raw %}기본적으로 중단된 메시지는 표준 Campaign 보고서에 표시되지 않습니다. 그러나 Liquid가 `{% abort_message %}`로 발송을 중단하면 Braze는 이를 메시지 활동 로그에 메시지 오류로 기록합니다(기본적으로 `{% abort_message %}`가 호출된 것으로 표시됩니다). 문자열을 전달하면 해당 사유가 로그에 표시됩니다(예: `{% abort_message('language was nil') %}`){% endraw %}. 대시보드에서 이러한 억제 내역을 확인하려면 고객 성공 매니저에게 연락하여 [메시징 진단 대시보드]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/diagnostics_dashboard)에 대한 액세스를 요청하세요.