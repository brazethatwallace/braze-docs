---
nav_title: 이중 옵트인
article_title: 이중 옵트인
description: "이 참조 문서에서는 이중 옵트인 기능을 다루며, 기능 활성화 방법, 옵트인 키워드 및 응답 메시지 선택 방법, REST API, SDK, 환경설정 센터 업데이트를 통한 구독 업데이트로 사용자를 이중 옵트인 워크플로에 진입시키는 방법을 설명합니다."
page_type: reference
page_order: 1
channel:
  - SMS
  - MMS
  - RCS
---

# 이중 옵트인 {#double-opt-in}

> 이중 옵트인 기능은 사용자가 SMS, MMS 또는 RCS 메시지를 수신하기 전에 옵트인 의도를 명시적으로 확인하도록 요구합니다. 이를 통해 참여도가 높은 사용자에게 메시지를 집중하고 규정 준수 모범 사례를 지원합니다.

이중 옵트인이 활성화되면, 사용자는 Campaign(캠페인) 또는 Canvas를 통해 메시지를 받기 전에 명시적 동의를 요청하는 메시지를 수신합니다.

1991년 전화 소비자 보호법(TCPA)의 명시적 요구 사항은 아니지만, Braze는 사용자가 SMS, MMS 또는 RCS 프로그램에 참여하는 것을 인지하고 동의하는지 확인하기 위해 이중 옵트인을 구성할 것을 권장합니다. 규정 준수에 대한 자세한 내용은 [SMS, MMS 및 RCS에 대한 법률, 규정 및 남용 방지]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations/)를 참조하세요.

## 이중 옵트인 워크플로 {#double-opt-in-workflows}

이중 옵트인을 통해 인바운드 및 아웃바운드 옵트인 캠페인으로 명시적 동의를 얻을 수 있습니다.

### 아웃바운드 {#outbound}

사용자가 전화번호를 제공하면 동의를 요청하는 메시지가 전송됩니다.

![브랜드가 "BRAND 문자 업데이트에 오신 것을 환영합니다! 최신 혜택을 위해 주 1회 메시지를 보내드립니다. 옵트인하려면 Y로 답장하세요."라고 문자를 보내고, 사용자가 "Y"로 답장하고, 브랜드가 "감사합니다! 이제 BRAND 알림에 옵트인되었습니다. 첫 구매 시 10% 할인 프로모션 코드 SMS10을 드립니다!"라고 응답하는 아웃바운드 SMS 메시지 스크린샷]({% image_buster /assets/img/double_opt_in_outbound.png %}){:style="max-width:40%;"}

### 인바운드 {#inbound}

사용자가 옵트인 키워드가 포함된 메시지를 보내면 동의를 요청하는 메시지가 전송됩니다.

![사용자가 "JOIN"을 보내고 "SMS 프로그램에 JOIN하려면 Y로 답장하여 확인하세요. 주 3회 메시지, 중단하려면 언제든지 STOP을 문자하세요"라는 응답을 받은 후 "Y"로 답장하는 인바운드 SMS 메시지 스크린샷]({% image_buster /assets/img/double_opt_in_inbound.png %}){:style="max-width:40%;"}

## 이중 옵트인 활성화 {#enabling-double-opt-in}

이중 옵트인을 활성화하려면 해당 구독 그룹의 **Global Keywords** 테이블로 이동하여 **Opt-In Keyword Category**에서 **Edit**를 클릭합니다. 그런 다음 옵트인 방법(**Opt-In** 또는 **Double Opt-In**)을 선택합니다. **Double Opt-In**을 선택하면 추가 [구성 가능한 필드](#configurable-fields)가 표시되도록 페이지가 확장됩니다.

![옵트인 방법 섹션에는 Opt-In과 Double Opt-In 두 가지 옵트인 방법이 있습니다.]({% image_buster /assets/img/double_opt_in_method.png %}){:style="max-width:50%;"}

### 구성 가능한 필드 {#configurable-fields}

| 카테고리 | 필드 | 설명
| ----------- |----------- |----------------
| 옵트인 안내 | 키워드 | 사용자가 옵트인 의도를 나타내기 위해 문자로 보낼 수 있는 키워드입니다. `START`는 필수 키워드입니다. 이 옵트인 안내는 [구독 소스](#subscription-sources) 섹션에 나열된 소스에 의해 구독 상태가 업데이트될 때도 사용자에게 전송됩니다.
| | 응답 메시지 | 사용자가 옵트인 키워드를 문자로 보낸 후 받게 되는 초기 응답입니다(예: "이 번호에서 메시지를 수신하려면 Y로 답장하여 확인하세요. 메시지 및 데이터 요금이 적용될 수 있습니다.")
| 이중 옵트인 확인 | 키워드 | 사용자가 옵트인 의도를 확인하기 위해 답장할 수 있는 키워드입니다. 최소 하나의 키워드가 필요합니다. 이 키워드는 **옵트인 안내 응답 메시지** 필드에 지정해야 합니다.
| | 응답 메시지 | 사용자가 옵트인을 명시적으로 확인하고 메시지 수신이 가능해진 후 받게 되는 확인 응답입니다. 사용자의 구독 그룹 상태가 `Subscribed`로 설정됩니다.
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

사용자가 옵트인 안내를 받으면 옵트인 의도를 확인할 수 있는 기간은 30일입니다. 30일 기간이 지난 후 구독하려면 옵트인 키워드를 문자로 보내 이중 옵트인 워크플로를 다시 시작해야 합니다.

![구성 가능한 필드에는 옵트인 안내와 이중 옵트인 확인 두 섹션이 있으며, 각각 키워드와 응답 메시지 필드가 있습니다.]({% image_buster /assets/img/double_opt_in_fields.png %})

## 구독 그룹 상태 {#subscription-group-status}

사용자가 이중 옵트인 워크플로를 완료한 후에만 [구독 그룹 상태]({{site.baseurl}}/sms_rcs_subscription_groups/)가 `Subscribed`로 업데이트됩니다. 사용자가 워크플로를 시작했지만 완료하지 않으면 `Unsubscribed` 상태로 유지되며 해당 구독 그룹에서 메시지를 받을 수 없습니다.

사용자는 [다른 소스에서 구독]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups/)한 경우(예: REST API, SDK)에도 이중 옵트인 워크플로에 진입할 수 있습니다.

## 구독 소스 {#subscription-sources}

사용자는 인바운드 메시지 외부에서 발생하는 구독 업데이트를 통해서도 이중 옵트인 워크플로에 진입할 수 있습니다. 이러한 소스에는 REST API, SDK 및 환경설정 센터의 업데이트가 포함됩니다. 사용자가 이러한 소스를 통해 이중 옵트인 워크플로에 진입하면 **옵트인 안내 응답 메시지**를 수신합니다.

{% alert important %}
인바운드 메시지 이외의 소스를 통해 이중 옵트인 워크플로에 진입한 사용자는 이 워크플로에 진입한 횟수에 관계없이 24시간 롤링 기간 동안 최대 하나의 옵트인 안내 응답 메시지를 수신합니다.
{% endalert %}

각 구독 소스는 다음 표에 설명된 대로 서로 다른 등록 동작을 가집니다.

| 소스 | 이중 옵트인 등록 동작 |
| ----------- | ----------- |
| SDK | 사용자가 Braze SDK를 통해 구독하면 자동으로 이중 옵트인 워크플로에 진입합니다. |
| REST API | `/subscription/status/set`, `/v2/subscription/status/set` 또는 `/users/track`를 통해 구독 상태가 설정되고 선택적 매개변수 `use_double_opt_in_logic`이 `true`로 전달되면 사용자가 워크플로에 진입할 수 있습니다(예: [{"subscription_group_id" : "subscription_group_identifier", "subscription_state" : "subscribed", "use_double_opt_in_logic": true}]). 이 매개변수가 생략되면 사용자는 이중 옵트인 워크플로에 진입하지 않습니다. |
| Shopify | Shopify 통합에 의해 구독 상태가 설정된 경우 사용자는 이중 옵트인 워크플로에 진입하지 않습니다. |
| 사용자 가져오기 | 사용자 가져오기에 의해 구독 상태가 설정된 경우 사용자는 이중 옵트인 워크플로에 진입하지 않습니다. |
| [환경설정 센터]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center/) | 사용자가 환경설정 센터를 통해 구독하면 자동으로 이중 옵트인 워크플로에 진입합니다. |
| 사용자 업데이트 단계 | 사용자 업데이트 단계를 통해 구독 상태가 설정되고 선택적 매개변수 `use_double_opt_in_logic`이 `true`로 전달되면 사용자가 이중 옵트인 워크플로에 진입할 수 있습니다. 이 매개변수가 생략되면 사용자는 이중 옵트인 워크플로에 진입하지 않습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 다중 언어 지원 {#multi-language-support}
인바운드 메시지의 경우, 이중 옵트인은 구독 그룹에 정의된 모든 언어를 지원합니다. 즉, 다양한 언어로 자동 응답을 정의할 수 있으며, 일치하는 키워드가 수신되면 Braze가 특정 언어와 연결된 자동 응답을 전송합니다.

인바운드 메시지 외부에서 발생하는 구독 업데이트(예: SDK, REST API, Shopify)를 통해 이중 옵트인 워크플로에 진입한 사용자에게는 영어 키워드만 전송됩니다.