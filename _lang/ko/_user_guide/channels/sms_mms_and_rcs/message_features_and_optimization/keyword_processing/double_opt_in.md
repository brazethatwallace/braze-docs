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

> 이중 옵트인 기능은 사용자가 단문 메시지 서비스, MMS 또는 RCS 메시지를 수신하기 전에 옵트인 의도를 명시적으로 확인하도록 요구합니다. 이를 통해 참여도가 높은 사용자에게 메시지를 집중하고 규정 준수 모범 사례를 지원합니다.

이중 옵트인이 활성화되면, 사용자는 Campaign(캠페인) 또는 Canvas를 통해 메시지를 받기 전에 명시적 동의를 요청하는 메시지를 수신합니다.

1991년 전화 소비자 보호법(TCPA)의 명시적 요구 사항은 아니지만, Braze는 사용자가 단문 메시지 서비스, MMS 또는 RCS 프로그램에 참여하는 것을 인지하고 동의하는지 확인하기 위해 이중 옵트인을 구성할 것을 권장합니다. 규정 준수에 대한 자세한 내용은 [단문 메시지 서비스, MMS 및 RCS에 대한 법률, 규정 및 남용 방지]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations)를 참조하세요.

## 이중 옵트인 워크플로 {#double-opt-in-workflows}

이중 옵트인을 통해 인바운드 및 아웃바운드 옵트인 캠페인을 통해 명시적 동의를 확보할 수 있습니다.

### 아웃바운드 {#outbound}

사용자가 전화번호를 제공하면 동의를 요청하는 메시지가 전송됩니다.

![아웃바운드 SMS 메시지 스크린샷으로, 브랜드가 "Welcome to BRAND text updates! 1 msg a week for the latest offers. Reply Y to opt-in."이라고 보내고, 사용자가 "Y"로 답장하면 브랜드가 "Thanks! You're now opted-in to BRAND alerts. Here is a promo code SMS10 for 10% off your first purchase!"라고 응답합니다.]({% image_buster /assets/img/double_opt_in_outbound.png %}){:style="max-width:40%;"}

### 인바운드 {#inbound}

사용자가 옵트인 키워드가 포함된 메시지를 보내면 동의를 요청하는 메시지가 전송됩니다.

![인바운드 SMS 메시지 스크린샷으로, 사용자가 "JOIN"을 보내면 "Reply Y to confirm you want to JOIN our SMS program. 3msg/week, text STOP at any time to STOP"이라는 응답을 받고 "Y"를 답장합니다.]({% image_buster /assets/img/double_opt_in_inbound.png %}){:style="max-width:40%;"}

## 더블 옵트인 활성화 {#enabling-double-opt-in}

더블 옵트인을 켜려면 해당 구독 그룹의 **Global Keywords** 테이블로 이동하여 **Opt-In Keyword Category**에서 **Edit**를 선택합니다. 다음으로 옵트인 방법(**Opt-In** 또는 **Double Opt-In**)을 선택합니다. **Double Opt-In**을 선택하면 페이지가 확장되어 추가 [설정 가능한 필드](#configurable-fields)가 표시됩니다.

![옵트인 방법 섹션에서 Opt-In과 Double Opt-In 두 가지 옵트인 방법을 선택할 수 있습니다.]({% image_buster /assets/img/double_opt_in_method.png %}){:style="max-width:50%;"}

### 설정 가능한 필드 {#configurable-fields}

| 카테고리   |    필드    | 설명
| ----------- |----------- |----------------
| 옵트인 안내 | 키워드 | 사용자가 옵트인 의도를 나타내기 위해 문자로 보낼 수 있는 키워드입니다. `START`는 필수 키워드입니다. 이 옵트인 안내는 [구독 소스](#subscription-sources) 섹션에 나열된 소스에 의해 사용자의 구독 상태가 업데이트될 때에도 전송됩니다.
| | 응답 메시지 | 사용자가 옵트인 키워드를 보낸 후 받는 초기 응답입니다. (예: "이 번호에서 메시지를 수신하려면 Y를 답장하세요. 메시지 및 데이터 요금이 부과될 수 있습니다.")
| 더블 옵트인 확인 | 키워드 | 사용자가 옵트인 의도를 확인하기 위해 답장할 수 있는 키워드입니다. 최소 하나의 키워드가 필요합니다. 이러한 키워드는 **옵트인 안내 응답 메시지** 필드에 지정해야 합니다.
| | 응답 메시지 | 사용자가 옵트인을 명시적으로 확인하고 메시지 수신이 가능해진 후 받는 확인 응답입니다. 사용자의 구독 그룹 상태가 `Subscribed`로 설정됩니다.
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="설정 가능한 필드 #configurable-fields" }

사용자가 옵트인 안내를 받으면 옵트인 의도를 확인할 수 있는 기간이 30일 주어집니다. 30일이 지난 후 구독하려면 옵트인 키워드를 다시 보내 더블 옵트인 워크플로를 새로 시작해야 합니다.

![설정 가능한 필드에는 옵트인 안내와 더블 옵트인 확인 두 섹션이 있으며, 각각 키워드와 응답 메시지 필드가 포함되어 있습니다.]({% image_buster /assets/img/double_opt_in_fields.png %})

## 구독 그룹 상태 {#subscription-group-status}

사용자가 이중 옵트인 워크플로우를 완료한 후에만 [구독 그룹 상태]({{site.baseurl}}/sms_rcs_subscription_groups)가 `Subscribed`로 업데이트됩니다. 사용자가 워크플로우를 시작했지만 완료하지 않은 경우, `Unsubscribed` 상태로 유지되며 해당 구독 그룹에서 메시지를 받을 수 없습니다.

사용자는 [다른 소스에서 구독]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups)한 경우(예: REST API, SDK)에도 이중 옵트인 워크플로우에 진입할 수 있습니다.

## 구독 소스 {#subscription-sources}

사용자는 인바운드 메시지 외부에서 발생하는 구독 업데이트를 통해서도 이중 옵트인 워크플로에 진입할 수 있습니다. 이러한 소스에는 REST API, SDK 및 환경설정 센터의 업데이트가 포함됩니다. 사용자가 이러한 소스를 통해 이중 옵트인 워크플로에 진입하면 **옵트인 안내 응답 메시지**를 수신합니다.

{% alert important %}
인바운드 메시지 이외의 소스를 통해 이중 옵트인 워크플로에 진입한 사용자는 이 워크플로에 진입한 횟수에 관계없이 24시간 롤링 기간 동안 최대 하나의 옵트인 안내 응답 메시지를 수신합니다.
{% endalert %}

각 구독 소스는 다음 표에 설명된 대로 서로 다른 등록 동작을 가집니다.

| 소스 | 이중 옵트인 등록 동작 |
| ----------- | ----------- |
| SDK | 사용자가 Braze SDK를 통해 구독하면 자동으로 이중 옵트인 워크플로에 진입합니다. |
| REST API | `/subscription/status/set`, `/v2/subscription/status/set` 또는 `/users/track`를 통해 구독 상태가 설정되고 선택적 매개변수 `use_double_opt_in_logic`이 `true`로 전달되면 사용자가 워크플로에 진입할 수 있습니다(예: [{"subscription_group_id" : "subscription_group_identifier", "subscription_state" : "subscribed", "use_double_opt_in_logic": true}]). 이 매개변수가 생략되면 사용자는 이중 옵트인 워크플로에 진입하지 않습니다. <br><br>`use_double_opt_in_logic`을 REST API와 함께 사용할 때, 제공된 전화번호와 연결된 고객 프로필이 없으면 구독 상태가 업데이트되지 않으며 사용자는 이중 옵트인 워크플로에 진입할 수 없습니다. |
| Shopify | Shopify 통합에 의해 구독 상태가 설정된 경우 사용자는 이중 옵트인 워크플로에 진입하지 않습니다. |
| 사용자 가져오기 | 사용자 가져오기에 의해 구독 상태가 설정된 경우 사용자는 이중 옵트인 워크플로에 진입하지 않습니다. |
| [환경설정 센터]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center) | 사용자가 환경설정 센터를 통해 구독하면 자동으로 이중 옵트인 워크플로에 진입합니다. |
| 사용자 업데이트 단계 | 사용자 업데이트 단계를 통해 구독 상태가 설정되고 선택적 매개변수 `use_double_opt_in_logic`이 `true`로 전달되면 사용자가 이중 옵트인 워크플로에 진입할 수 있습니다. 이 매개변수가 생략되면 사용자는 이중 옵트인 워크플로에 진입하지 않습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="구독 소스" }

## 다국어 지원 {#multi-language-support}
인바운드 메시지의 경우, 이중 옵트인은 구독 그룹에 정의된 모든 언어를 지원합니다. 즉, 자동 응답을 다양한 언어로 정의할 수 있으며, 일치하는 키워드가 수신되면 Braze가 해당 언어에 연결된 자동 응답을 전송합니다.

인바운드 메시지 외부에서 발생하는 구독 업데이트(예: SDK, REST API, Shopify)를 통해 이중 옵트인 워크플로에 진입하는 사용자에게는 영어 키워드만 전송됩니다.