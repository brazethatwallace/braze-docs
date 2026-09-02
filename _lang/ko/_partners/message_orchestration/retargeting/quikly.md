---
nav_title: Quikly
article_title: Quikly
description: "이 참조 문서에서는 긴급성 마케팅 플랫폼인 Quikly와 Braze 간의 파트너십을 설명합니다. 이 파트너십을 통해 Braze 고객 여정 내 이벤트에 대한 전환을 가속화할 수 있습니다."
alias: /partners/quikly/
page_type: partner
search_tag: Partner

---

# Quikly

> 긴급성 마케팅 플랫폼인 [Quikly](https://www.quikly.com)는 심리학을 활용하여 소비자의 동기를 부여하므로, 브랜드는 주요 마케팅 이니셔티브에 대한 반응을 즉각적으로 높일 수 있습니다.

_이 통합은 Quikly에서 유지 관리합니다._

## 통합 정보 {#about-the-integration}

Braze와 Quikly 파트너십을 통해 Braze 고객 여정 내 이벤트에 대한 전환을 가속화할 수 있습니다. Quikly는 긴급성 심리학을 활용하여 소비자에게 재미있고 즉각적인 방식으로 동기를 부여합니다. 예를 들어, 브랜드는 Quikly를 사용하여 새로운 이메일 및 단문 메시지 서비스 구독자를 Braze에 직접 확보하거나, 모바일 앱 다운로드와 같은 기타 주요 마케팅 목표를 달성하도록 동기를 부여할 수 있습니다.

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Quikly 계정 | 이 파트너십을 활용하려면 [Quikly](https://www.quikly.com) 브랜드 파트너 계정이 필요합니다. |
| Braze REST API 키 | `users.track`, `subscription.status.set`, `users.export.ids`, `subscription.status.get` 권한이 있는 Braze REST API 키가 필요합니다. <br><br> Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
| Braze REST 엔드포인트 | [REST 엔드포인트 URL]({{site.baseurl}}/developer_guide/rest_api/basics#endpoints). 엔드포인트는 인스턴스의 Braze URL에 따라 달라집니다. |
| Quikly API 키(선택 사항) | 클라이언트 성공 매니저가 제공하는 Quikly API 키입니다(웹훅 전용). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="필수 조건" }

## 사용 사례 {#use-cases}

Quikly를 사용하면 브랜드가 이메일 또는 단문 메시지 서비스 확보를 가속화하고, 구독자가 Braze 내에서 직접 퍼스트파티 데이터를 제공하도록 동기를 부여할 수 있습니다. 또한 Braze를 사용하여 이탈한 고객을 Quikly 활성화로 타겟팅하여 해당 오디언스를 재활성화하고 유지할 수 있습니다. 마케터는 이 통합을 사용하여 고유한 리워드 구조로 특정 고객 여정 이벤트에 인센티브를 제공할 수도 있습니다.

예를 들어:
 - [Quikly Hype](https://www.quikly.com/urgency-marketing/platform/product-overview/hype)를 통해 소비자가 흥미로운 리워드를 받을 기회에 옵트인하면서 며칠에 걸쳐 기대감과 참여를 구축합니다. 퍼스트파티 데이터는 자동으로 Braze에 푸시됩니다.
 - [Quikly Swap](https://www.quikly.com/urgency-marketing/platform/product-overview/swap)을 사용하여 소비자의 응답 속도, 다른 사람과의 순위, 무작위, 또는 시간이나 수량이 소진되기 전에 기반한 고유한 실시간 오퍼로 새로운 이메일 및 단문 메시지 서비스 구독자 확보를 가속화합니다.
 - 웹훅을 사용하여 고유한 리워드 구조로 고객 여정의 특정 단계에 동기를 부여합니다.
 - Quikly 활성화에 참여할 때 사용자 프로필에 커스텀 속성 또는 이벤트를 적용합니다.

## 통합 {#integration}

이 섹션에서는 이메일 확보, 단문 메시지 서비스 확보, 커스텀 속성, 웹훅의 네 가지 통합을 설명합니다. 선택하는 통합은 Quikly 활성화 및 사용 사례에 따라 달라집니다.

{% tabs %}
{% tab 이메일 확보 %}

### 이메일 확보 {#email-acquisition}

Quikly 활성화에서 고객 이메일 주소 또는 프로필 데이터를 수집하는 경우, 유일한 필수 단계는 Quikly에 REST API 키와 엔드포인트를 제공하는 것입니다. Quikly가 이 데이터를 Braze에 전달하도록 브랜드 계정을 구성합니다. 포함하고 싶은 추가 사용자 속성이 있는 경우, Quikly에 API 자격 증명을 제공할 때 이를 언급하세요.

다음은 Quikly가 이 워크플로를 실행하는 방법에 대한 개요입니다.
1. Quikly 활성화에 참여하면, Quikly는 [내보내기 API]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier)를 사용하여 사용자 조회를 스케줄하고 지정된 `email_address`를 가진 사용자가 존재하는지 확인합니다.
2. 사용자를 기록하거나 업데이트합니다.
  - 사용자가 존재하는 경우:
    - 새 프로필을 생성하지 않습니다.
    - 필요한 경우, Quikly는 사용자가 활성화에 참여했음을 나타내기 위해 사용자 프로필에 커스텀 속성을 기록할 수 있습니다.
  - 사용자가 존재하지 않는 경우:
    - Quikly는 Braze [`/users/track` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track)를 통해 별칭 전용 프로필을 생성하고, 향후 해당 사용자를 참조할 수 있도록 사용자의 이메일을 사용자 별칭으로 설정합니다(사용자에게 외부 ID가 없으므로).
    - 필요한 경우, Quikly는 이 프로필이 Quikly 활성화에 참여했음을 나타내기 위해 커스텀 이벤트를 기록할 수 있습니다.

{% details /users/track 요청 %}

#### 요청 헤더 {#request-headers}
```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

#### 요청 본문 {#request-body}
```
{
  "attributes": [{
    "_update_existing_only": false,
    "user_alias:": {
      "alias_name": "email@example.com",
      "alias_label: "email"
    },
    "email": "email@example.com"
  }]
}
```

{% enddetails %}

{% endtab %}
{% tab 단문 메시지 서비스 확보 %}

### 단문 메시지 서비스 구독 {#sms-subscriptions}

Quikly 활성화는 고객으로부터 직접 휴대폰 번호를 수집하고 새로운 단문 메시지 서비스 구독을 시작할 수 있습니다. 이 통합을 활성화하려면 Quikly 클라이언트 성공 매니저에게 `subscription_group_id`를 제공하세요. **구독 그룹** 페이지로 이동하여 구독 그룹의 `subscription_group_id`에 접근할 수 있습니다.

Quikly는 고객의 전화번호를 사용하여 구독 조회를 수행하고, 단문 메시지 서비스 구독이 이미 존재하는 경우 활성화에서 자동으로 크레딧을 부여합니다. 그렇지 않으면 새 구독이 시작되고, 구독 상태가 확인된 후 고객에게 크레딧이 부여됩니다.

다음은 고객이 Quikly를 통해 휴대폰 번호와 동의를 제공할 때의 전체 워크플로입니다:
1. Quikly는 [구독 그룹 상태]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status)를 사용하여 구독 조회를 수행하고, 지정된 `phone`이 `subscription_group_id`에 구독되어 있는지 확인합니다. 구독이 존재하면 Quikly 활성화에서 사용자에게 크레딧을 부여합니다. 추가 조치는 필요하지 않습니다.
2. Quikly는 [식별자별 사용자 프로필 내보내기 엔드포인트]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier)를 사용하여 사용자 조회를 수행하고, 지정된 `email_address`를 가진 사용자 프로필이 존재하는지 확인합니다. 사용자가 존재하지 않으면 Braze [`/users/track` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track)를 통해 별칭 전용 프로필을 생성하고, 향후 해당 사용자를 참조할 수 있도록 사용자의 이메일을 사용자 별칭으로 설정합니다(사용자에게 외부 ID가 없으므로).
3. [사용자의 구독 그룹 상태 업데이트 엔드포인트]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status)를 사용하여 구독 상태를 업데이트합니다.

기존 이중 옵트인 단문 메시지 서비스 구독 워크플로를 지원하기 위해, Quikly는 이 섹션의 표준 워크플로 대신 Braze에 커스텀 이벤트를 전송할 수 있습니다. 이 경우 구독 상태를 직접 업데이트하는 대신, [커스텀 이벤트가 이중 옵트인 프로세스를 트리거]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/double_opt_in)하고, 사용자가 완전히 옵트인했는지 확인하기 위해 구독 상태를 주기적으로 모니터링한 후 Quikly 활성화에서 크레딧을 부여합니다.

{% alert important %}
Braze는 `/users/track` 엔드포인트를 통해 새 사용자를 생성할 때, Braze가 사용자 프로필을 완전히 생성할 시간을 확보할 수 있도록 관련 구독 그룹에 사용자를 추가하기 전에 약 2분의 지연을 두는 것을 권장합니다.
{% endalert %}

{% details 상세 /subscription/status/set 요청 %}
#### 요청 헤더
```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

#### 요청 본문
```
{
  "subscription_group_id": "the-id-of-the-subscription-group",
    "subscription_status": "subscribed",
    "phone": "+13135551212"
  }]
}
```

{% enddetails %}

{% endtab %}
{% tab 커스텀 속성 %}
### 커스텀 속성 {#custom-attributes}

Braze 구현에 따라 Quikly 활성화 내 이벤트가 추가 처리를 위해 Braze를 통해 전파되기를 원할 수 있습니다. 예를 들어, Quikly 활성화에서 달성한 레벨이나 인센티브에 따라 커스텀 사용자 속성을 적용하여, 사용자가 앱을 열거나 웹사이트에 로그인할 때 관련 콘텐츠 카드를 표시할 수 있습니다. Quikly가 직접 협력하여 이러한 통합을 구현합니다.

{% endtab %}
{% tab 웹훅 %}
### 웹훅 {#webhooks}
웹훅을 사용하여 고객 여정의 특정 이벤트에 대한 인센티브를 트리거합니다. 예를 들어, 사용자가 앱에 로그인하거나, 푸시 알림을 켜거나, 매장 찾기를 사용할 때의 Braze 이벤트가 있는 경우, 웹훅을 사용하여 특정 Quikly 활성화의 구성에 따라 해당 사용자에게 맞춤 오퍼를 트리거할 수 있습니다. 예시 전략으로는 특정 동작(예: 앱에 로그인)을 수행한 처음 X명의 사용자에게 맞춤 오퍼를 리워드로 제공하거나, 시간이 경과할수록 가치가 감소하는 오퍼를 제공하여 즉각적인 반응을 유도하는 것이 있습니다.

### Braze에서 Quikly 웹훅 생성 {#create-a-quikly-webhook-in-braze}

향후 Campaigns 또는 Canvases를 위한 Quikly 웹훅 템플릿을 생성하려면 Braze 플랫폼에서 **콘텐츠** > **웹훅**으로 이동한 다음 **웹훅 템플릿 생성**을 선택합니다.

일회성 Quikly 웹훅 Campaign을 생성하거나 기존 템플릿을 사용하려면, 새 Campaign을 생성할 때 Braze에서 **웹훅**을 선택합니다.

**빈 템플릿**을 선택하고 웹훅 URL과 요청 본문에 다음을 입력합니다:
- **웹훅 URL**: https://api.quikly.com/webhook/braze
- **요청 본문**: JSON 키/값 쌍

#### 요청 헤더 및 메서드 {#request-headers-and-method}

Quikly는 인증을 위해 `HTTP Header`가 필요합니다.

- **HTTP Method**: POST
- **요청 헤더**:
  - **Authorization**: Bearer [PARTNER_AUTHORIZATION_HEADER]
  - **Content-Type**: application/json

#### 요청 본문

***JSON 키/값 쌍***을 선택하고 다음 쌍을 추가합니다:
{% raw %}
```
"q_scope": "your-activations-scope-id"
"event": "your-event-identifier"
"email": {{${email_address}}
```
{% endraw %}

### 요청 미리보기 {#preview-your-request}

**미리보기** 패널에서 요청을 미리 보거나 `Test` 탭으로 이동하여 무작위 사용자, 기존 사용자를 선택하거나 직접 커스터마이즈하여 웹훅을 테스트할 수 있습니다.

{% alert important %}
페이지를 떠나기 전에 템플릿을 저장하세요! <br>업데이트된 웹훅 템플릿은 새 [웹훅 Campaign]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook)을 생성할 때 **저장된 웹훅 템플릿** 목록에서 찾을 수 있습니다.
{% endalert %}

{% endtab %}
{% endtabs %}

## 고객지원 {#support}
궁금한 점이 있으면 Quikly의 클라이언트 성공 매니저에게 문의하세요.