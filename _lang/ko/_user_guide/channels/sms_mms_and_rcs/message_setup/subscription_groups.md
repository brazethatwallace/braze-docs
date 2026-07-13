---
nav_title: "구독 그룹"
article_title: SMS 및 RCS 구독 그룹
page_order: 4
description: "이 참조 문서에서는 SMS, MMS, RCS 채널의 구독 그룹, 구독 상태, 구독 그룹 설정 프로세스에 대해 설명합니다."
page_type: reference
alias: /sms_rcs_subscription_groups/
channel:
  - SMS
  - MMS
  - RCS

---

# SMS, MMS, RCS 구독 그룹 {#sms-mms-and-rcs-subscription-groups}

> 구독 그룹은 Braze를 통해 SMS, MMS, RCS 메시지를 발송하기 위한 기반입니다. 구독 그룹은 특정 유형의 메시징 목적에 사용되는 [발송 엔티티]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup)(RCS 인증 발신자, SMS 짧은 코드, SMS 긴 코드, SMS 영숫자 발신자 ID 등)의 모음입니다. 예를 들어, 브랜드가 트랜잭션 SMS 메시징과 프로모션 SMS 메시징을 모두 발송할 계획이라면, Braze 대시보드 내에서 별도의 발송 전화번호 풀을 가진 두 개의 구독 그룹을 설정해야 합니다.

{% multi_lang_include alerts/note_alerts.md alert='subscription group limit' %}

## 구독 그룹 상태 {#subscription-group-states}

SMS 및 RCS 사용자에게는 `subscribed`와 `unsubscribed` 두 가지 구독 상태가 있습니다. 사용자의 구독 상태는 구독 그룹 수준에 존재하며 구독 그룹 간에 공유되지 않습니다. 즉, 사용자가 트랜잭션 구독 그룹에는 `subscribed`이지만 프로모션 구독 그룹에는 `unsubscribed`일 수 있습니다. 브랜드에게 이러한 상태 분리는 사용자에게 관련성 있는 SMS 및 RCS 메시지를 계속 발송할 수 있도록 보장합니다.

| 상태 | 정의 |
| --------- | ---------- |
| 가입됨 | 사용자가 특정 구독 그룹에서 SMS 및 RCS를 수신하도록 가입되어 있습니다. 사용자는 Braze 구독 API를 통해 구독 상태를 업데이트하거나 옵트인 키워드 응답을 문자로 보내 가입할 수 있습니다. SMS 또는 RCS, 혹은 둘 다를 수신하려면 사용자가 SMS 또는 RCS 구독 그룹에 가입되어 있어야 합니다. [이중 옵트인]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/double_opt_in)이 활성화된 경우, 사용자는 구독 상태가 `Subscribed`로 업데이트되기 전에 옵트인 의사를 확인해야 합니다. |
| 가입 취소됨 | 사용자가 SMS 및 RCS 구독 그룹과 해당 구독 그룹 내 발송 전화번호로부터의 메시징을 명시적으로 옵트아웃했습니다. 옵트아웃 키워드 응답을 문자로 보내 가입을 취소하거나, [Braze 구독 API]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status)를 통해 사용자의 가입을 취소할 수 있습니다. SMS 및 RCS 구독 그룹에서 가입 취소된 사용자는 해당 구독 그룹에 속한 발송 전화번호로부터 더 이상 SMS 또는 RCS를 수신하지 않습니다.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="구독 그룹 상태" }

### 사용자 상태 설정 {#set-a-users-state}

사용자 프로필에서 전화번호가 업데이트되면, 새 전화번호는 해당 사용자의 구독 그룹 상태를 상속합니다. 전화번호가 Braze에 이미 존재하는 번호로 업데이트되면, 해당 기존 전화번호의 구독 상태가 상속됩니다.

예를 들어, 사용자 A가 여러 구독 그룹에 가입된 전화번호를 가지고 있고 해당 전화번호가 사용자 B에게 추가되면, 사용자 B는 동일한 구독 그룹에 가입됩니다. 사용자가 기존 구독을 상속하는 것을 방지하려면, 사용자가 번호를 변경할 때마다 Braze REST API를 통해 이전 번호의 구독 그룹을 초기화할 수 있습니다. 여러 사용자가 이 전화번호를 공유하는 경우, 모두 가입 취소됩니다.

사용자의 구독 그룹 상태를 설정하려면 다음 방법 중 하나를 사용하세요:

- **REST API:** [`/subscription/status/set` 엔드포인트]({{ site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/)를 사용하여 Braze REST API로 사용자 프로필을 프로그래밍 방식으로 설정할 수 있습니다.
- **SDK 통합:** [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/add-to-subscription-group.html), [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)), 또는 [Web](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addtosubscriptiongroup)용 `addToSubscriptionGroup` 메서드를 사용하여 이메일 또는 SMS 및 RCS 구독 그룹에 사용자를 추가할 수 있습니다.
- **전화번호 수집 인앱 메시지 양식:** 인앱 메시지 드래그 앤 드롭 에디터의 전화번호 수집 템플릿을 통해 사용자 전화번호를 수집할 수 있습니다.
- **사용자 옵트인/옵트아웃 시 자동 처리:** 사용자가 기본 옵트인 또는 옵트아웃 [키워드]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/optin_optout)를 문자로 보내면, Braze가 자동으로 사용자의 구독 상태를 설정하고 업데이트합니다.
- **사용자 가져오기:** **사용자 가져오기**를 통해 이메일 또는 SMS 및 RCS 구독 그룹에 사용자를 추가할 수 있습니다. 구독 그룹 상태를 업데이트할 때 CSV에 `subscription_group_id`와 `subscription_state` 두 열이 있어야 합니다. 자세한 내용은 [사용자 가져오기]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#updating-subscription-group-status)를 참조하세요.

#### Canvas에서 사용자 상태 업데이트 {#update-a-users-state-in-a-canvas}

Canvas 플로우의 일부로 사용자의 구독 그룹 상태를 업데이트할 때는 웹훅 대신 [사용자 업데이트]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update) 단계를 사용하세요. 사용자 업데이트 단계는 처리가 완료될 때까지 기다린 후 사용자를 다음 단계로 진행시키므로, 후속 메시징 단계에서 업데이트된 구독 상태를 사용합니다.

웹훅을 사용하여 구독 그룹을 업데이트하면, 구독 변경 처리가 완료되기 전에 웹훅이 발송되는 즉시 사용자가 진행됩니다. 이로 인해 후속 SMS 단계가 사용자가 가입되기 전에 실행되어 일부 사용자에게 메시지 발송이 실패하는 경합 조건이 발생할 수 있습니다. 웹훅을 사용해야 하는 경우, 다음 메시징 단계 전에 최소 1분의 지연 단계를 추가하세요.

#{% multi_lang_include api/orphaned_subscription_states.md %}

### 사용자 그룹 확인 {#check-a-users-group}

사용자의 구독 그룹을 확인하려면 다음 방법 중 하나를 사용하세요:

- **사용자 프로필:** Braze 대시보드에서 사이드바의 **사용자 검색**을 선택하여 개별 사용자 프로필에 접근할 수 있습니다. 여기에서 이메일 주소, 전화번호 또는 외부 사용자 ID로 사용자 프로필을 검색할 수 있습니다. 사용자 프로필 내 참여 탭에서 사용자의 SMS 및 RCS 구독 그룹을 확인할 수 있습니다.
- **REST API:** [사용자의 구독 그룹 나열 엔드포인트]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups) 또는 [사용자의 구독 그룹 상태 나열 엔드포인트]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status)를 사용하여 Braze REST API로 개별 사용자 프로필의 구독 그룹을 확인할 수 있습니다.

## 구독 그룹으로 메시지 발송 {#send-messages-with-a-subscription-group}

Braze를 통해 SMS 또는 RCS Campaign을 시작하려면 **SMS/MMS/RCS Variants** 드롭다운에서 구독 그룹을 선택하세요. 선택하면 오디언스 필터가 Campaign 또는 Canvas에 자동으로 추가되어, 선택한 구독 그룹에 `subscribed`된 사용자만 타겟 오디언스에 포함됩니다.

{% alert important %}
국제 [통신 규정 준수 및 가이드라인]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations)을 준수하여, Braze는 선택한 구독 그룹에 가입하지 않은 사용자에게 SMS 또는 RCS를 발송하지 않습니다.
{% endalert %}

![구독 그룹 드롭다운이 열려 있고 사용자가 "Messaging Service A for SMS"를 강조 표시한 SMS 작성기.]({% image_buster /assets/img/sms/sms_subgroup_select.png %})

## SMS 구독 그룹 모범 사례 {#sms-subscription-group-best-practices}

각 메시징 목적(예: 트랜잭션 대 마케팅)과 각 워크스페이스에 대해 별도의 SMS 구독 그룹을 설계하세요. 여러 국가에서 운영하는 경우, 현지 규정 준수 규칙을 지원하기 위해 지역별로 별도의 그룹을 고려하세요. 예를 들어, 브라질의 프로모션 발송 시간 제한이 이에 해당합니다.

## 구독 그룹 활성화 {#enable-subscription-groups}

SMS, MMS 또는 RCS의 구독 그룹을 활성화하려면 다음을 참조하세요:

{% tabs local %}
{% tab SMS %}
SMS 온보딩 과정에서 Braze 온보딩 매니저가 대시보드 계정에 대한 구독 그룹을 설정합니다. 필요한 구독 그룹 수를 결정하고 적절한 발송 전화번호를 구독 그룹에 추가하는 작업을 함께 진행합니다. 구독 그룹 설정 일정은 추가하는 전화번호 유형에 따라 달라집니다. 예를 들어, 짧은 코드 신청은 8~12주가 소요될 수 있으며, 긴 코드는 하루 만에 설정할 수 있습니다. Braze 대시보드 설정에 대한 질문이 있으면 Braze 담당자에게 문의하세요.
{% endtab %}

{% tab MMS %}
MMS 메시지를 발송하려면 구독 그룹 내 최소 하나의 번호가 MMS 발송이 가능하도록 활성화되어 있어야 합니다. 이는 구독 그룹 옆에 위치한 태그로 표시됩니다.

!["Messaging Service A for SMS"가 강조 표시된 구독 그룹 드롭다운. 항목 앞에 "MMS" 태그가 붙어 있습니다.]({% image_buster /assets/img/sms/mms_sub_group_tag.png %}){: style="max-width:40%"}
{% endtab %}

{% tab RCS %}
RCS 메시지를 발송하려면 구독 그룹 내에 RCS 인증 발신자가 있어야 합니다.

RCS 인증 발신자를 추가하는 방법은 두 가지입니다:
- 기존 구독 그룹에 추가
- 새 RCS 구독 그룹 생성
선택은 주로 관심 있는 RCS 사용 사례에 따라 달라집니다.

통합 방식에 따라 Braze는 기존 SMS 구독 그룹에 RCS 인증 발신자를 추가하거나 새 구독 그룹을 설정할 수 있습니다. 어느 경우든 고객 성공 매니저가 원활하고 효율적인 SMS 트래픽 업그레이드를 안내해 드립니다.
{% endtab %}
{% endtabs %}

## 에이전트 콘솔에서 자연어 옵트아웃 처리 {#handle-natural-language-opt-outs-in-the-agent-console}

포괄적인 구독 관리를 위해, 표준 또는 커스텀 키워드 범위를 벗어나는 옵트아웃 의도(예: "문자 보내지 마세요")를 캡처할 수 있습니다. AI 에이전트를 생성하면 감성 분석을 사용하여 이러한 요청을 자동으로 식별하고 처리할 수 있습니다.

### 설정 {#setup}

1. [에이전트 콘솔]({{site.baseurl}}/user_guide/brazeai/agents)에서 "SMS 감성 분석 에이전트"를 생성합니다.

{% alert tip %}
초기 에이전트 구성을 지원하려면 [Operator]({{site.baseurl}}/user_guide/brazeai/agents/reference#canvas-agent-examples)를 사용하세요.
{% endalert %}

{: start="2"}
2. **기타** 키워드 카테고리 내에서 **SMS 인바운드 메시지 발송**에 의해 트리거되는 액션 기반 Canvas를 생성합니다.
3. Canvas에 [에이전트 단계]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step)를 추가하여 옵트아웃 의도를 식별합니다.
4. 요청을 확인하는 후속 SMS [메시지 단계]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step)를 추가합니다: "SMS 수신 거부를 원하시는 것 같아 수신 거부 처리를 진행합니다. 실수인 경우 START를 문자로 보내 다시 옵트인하세요."
5. [사용자 업데이트 단계]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update#user-update)를 추가하여 특정 SMS 구독 그룹에서 사용자의 상태를 "가입 취소됨"으로 변경합니다.

{% alert note %}
에이전트 콘솔을 사용하면 메시지 또는 액션 크레딧이 소모됩니다.
{% endalert %}

## SMS 트래픽을 RCS로 마이그레이션 {#migrate-sms-traffic-to-rcs}

별도의 SMS 및 RCS 구독 그룹이 있는 경우, 한 단계 Canvas를 사용하여 사용자를 SMS에서 RCS로 마이그레이션할 수 있습니다.

Braze는 처음에 소규모 사용자에게 RCS 발송을 테스트하고, 시간이 지남에 따라 더 많은 사용자를 RCS 구독 그룹으로 마이그레이션할 것을 권장합니다. 예를 들어, SMS 구독 그룹에 1,000,000명의 사용자가 가입되어 있다면, 먼저 모든 사용자를 새 구독 그룹으로 마이그레이션한 다음 50,000~100,000명(5~10%)의 소규모 오디언스로 세분화하여 RCS 메시지를 테스트하는 방식이 될 수 있습니다.

### 1단계: Canvas 생성 및 진입 스케줄 작성 {#step-1-create-a-canvas-and-fill-out-the-entry-schedule}

Canvas를 생성하고 쉽게 식별할 수 있는 이름(예: "SMS-RCS 구독 그룹 사용자 이전")을 지정하세요. 그런 다음 편리한 시간에 스케줄을 설정하세요.

### 2단계: 오디언스 정의 {#step-2-define-your-audience}
{: #step-2-define-your-audience}

다음 방법 중 하나를 사용하여 오디언스를 정의하세요. 그런 다음 **발송 설정** 단계로 이동하여 **가입했거나 옵트인한 사용자**를 선택하세요.

| 방법 | 설명 |
|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Segment 생성** | 구독 그룹의 모든 사용자 또는 세분화 필터를 사용한 하위 집합(예: 무작위 5~10%)을 포함하는 Segment를 구축합니다. Segment는 각 발송 전에 업데이트되어 현재 사용자 기반을 반영합니다. |
| **Campaign 또는 Canvas 필터 적용** | Campaign 또는 Canvas의 **타겟 오디언스** 단계에서 오디언스를 세분화합니다. 페이지를 벗어나지 않고 타겟팅 옵션을 조정하여 유연성을 높일 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="2단계: 오디언스 정의" }

### 3단계: 사용자 업데이트 단계 구성 {#step-3-configure-a-user-update-step}

Canvas에 사용자 업데이트 단계를 추가하세요. 단계에서 **Advanced JSON Editor**를 열고 다음을 입력하세요(고유 사용자 식별자 필드에는 `braze_id` 필드를 사용하는 것을 권장합니다):

{% raw %}
```json
{
  "attributes": [
    {
      "braze_id": "{{${braze_id}}}",
      "subscription_groups": [
        {
          "subscription_group_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx",
          "subscription_state": "subscribed",
          "use_double_opt_in_logic": true
        }
      ]
    }
  ]
}
```
{% endraw %}

![앞서 언급한 JSON 코드가 포함된 "사용자 업데이트 오브젝트".]({% image_buster /assets/img/sms/user_update_object.png %})

### 4단계: Canvas 테스트 {#step-4-test-the-canvas}

더 넓은 오디언스에게 발송하기 전에 [Canvas를 테스트]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/sending_test_canvases)하여 예상대로 작동하는지 확인하는 것을 강력히 권장합니다.

### 5단계: Canvas 시작 {#step-5-launch-your-canvas}

Canvas를 성공적으로 테스트한 후, 사용자 하위 집합에 대해 시작하세요!

사용자가 성공적으로 마이그레이션되었는지 확인하려면, 업데이트된 개별 사용자 프로필 몇 개를 확인하는 것을 권장합니다. **Engagement** 탭에서 **Contact Settings**를 찾아 스크롤하여 사용자가 가입한 구독 그룹을 확인하세요. RCS 구독 그룹 토글이 켜져 있어야 합니다.

RCS 발신자 및 구독 그룹 설정에 대해서는 [RCS 설정]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/rcs_setup)도 참조하세요.

## 모범 사례 {#best-practices}

### 별도의 구독 그룹 지정 {#designate-separate-subscription-groups}

- **메시징 유형:** 트랜잭션 및 마케팅과 같은 각 메시징 유형에 대해 별도의 구독 그룹을 생성하세요.
- **워크스페이스:** 명확성과 조직을 유지하기 위해 각 워크스페이스에 대해 별도의 구독 그룹을 생성하세요.

두 개의 워크스페이스에 걸쳐 네 개의 구독 그룹이 있는 다음 예시를 참고하세요:

- **프로덕션 워크스페이스**
  - Marketing - PROD for SMS
  - Transactional - PROD for SMS
- **개발 워크스페이스(테스트용)**
  - Marketing - DEV for SMS
  - Transactional - DEV for SMS

### 명확한 명명 규칙 사용 {#use-clear-naming-conventions}

SMS Campaign을 생성할 때 올바른 그룹이 선택되도록 설명적이고 명확한 구독 그룹 이름을 선택하세요.

### 국가별 그룹 분리 {#separate-groups-by-country}

SMS 규정은 국가마다 다릅니다. SMS 구독 그룹을 국가별로 분리하는 것을 권장합니다. 이렇게 하면 메시지를 발송하는 모든 지역에서 규정 준수 기준을 충족하는 데 도움이 됩니다.

각 구독 그룹에 대해 **Geographic Permissions** 아래에서 국가 허용 목록을 구성하여 SMS, MMS, RCS가 승인된 지역으로만 발송되도록 할 수도 있습니다. 자세한 내용은 [지리적 권한]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups/geographic_permissions)을 참조하세요.

예를 들어, 브라질에서는 현지 시간 오전 9시에서 오후 9시 이외의 시간에 마케팅 메시지를 발송하는 것이 금지되어 있으며, 이 나라는 세 개의 시간대에 걸쳐 있습니다. 이러한 규정을 준수하기 위해 브라질과 미국에 메시지를 발송하기 위한 별도의 그룹을 설정할 수 있습니다. 이렇게 하면 브라질 사용자가 금지된 시간에 마케팅 메시지를 수신하는 것을 방지할 수 있습니다.