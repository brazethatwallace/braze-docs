---
nav_title: 사용자 이름 및 BSUID
article_title: WhatsApp 사용자 이름 및 비즈니스 범위 사용자 ID
page_order: 7
description: "WhatsApp 사용자 이름과 비즈니스 범위 사용자 ID(BSUID)가 Braze에서 사용자 식별, 메시징 및 데이터 처리에 미치는 영향을 알아보세요."
page_type: reference
alias: "/whatsapp_usernames/"
channel:
  - WhatsApp
hidden: true
noindex: true
---

# WhatsApp 사용자 이름 및 비즈니스 범위 사용자 ID {#whatsapp-usernames-and-business-scoped-user-ids}

> 2026년 6월, WhatsApp은 사용자 이름 기능을 도입할 예정입니다. 이 기능은 비즈니스와 메시지를 주고받을 때 사용자의 전화번호를 숨기는 선택적 개인정보 보호 기능입니다. Braze는 이 변경 사항을 완벽하게 처리할 준비가 되어 있으며, 대부분의 고객은 Campaign이나 Canvas에서 아무것도 변경할 필요가 없습니다.

{% alert important %}
WhatsApp 사용자 이름 및 비즈니스 범위 사용자 ID(BSUID)는 2026년 6월에 출시될 예정이며, Braze 업데이트도 이 출시에 맞춰 제공됩니다. 이 문서에 설명된 Braze 업데이트는 아직 **출시되지 않았습니다**.
{% endalert %}

WhatsApp 사용자가 사용자 이름을 채택하면, 해당 사용자의 전화번호는 더 이상 메시지를 보내는 비즈니스에 자동으로 공유되지 않습니다. 대신 WhatsApp은 비즈니스에 비즈니스 범위 사용자 ID(BSUID)를 제공합니다. 이는 각 비즈니스 포트폴리오와 사용자 쌍에 고유한 식별자입니다.

Braze는 BSUID를 자동으로 처리합니다. 사용자 이름을 채택한 사용자는 계속해서 Braze 워크스페이스에 표시되고, 메시지를 수신하고, Canvases를 트리거하고, 이벤트를 생성합니다. 일부 고객은 [변경 사항에 대비](#how-to-prepare-for-the-change)해야 할 수 있습니다.

## 비즈니스 범위 사용자 ID(BSUID) {#business-scoped-user-id-bsuid}

BSUID는 WhatsApp이 특정 비즈니스 포트폴리오 내에서 사용자를 나타내기 위해 할당하는 고유하고 영구적인 식별자입니다. 전화번호를 비공개로 유지하려는 사용자를 위한 대체 전화번호라고 생각하면 됩니다.

BSUID에는 세 가지 주요 특성이 있습니다:

| 특성 | 설명 |
| ----- | ----- |
| 고유성 | 비즈니스 포트폴리오 내에서 두 사용자가 동일한 BSUID를 공유하지 않습니다. |
| 비즈니스 범위 | 동일한 사용자가 메시지를 보내는 각 비즈니스마다 다른 BSUID를 갖게 됩니다. BSUID는 서로 다른 비즈니스 포트폴리오 간에 공유하거나 비교할 수 없습니다. |
| 웹훅에서 사용 가능 | BSUID는 현재 사용자의 전화번호를 포함하는 모든 동일한 웹훅 페이로드에 포함됩니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Business-scoped user ID (BSUID)" }

## WhatsApp 사용자 유형 변경 사항 {#changes-to-whatsapp-user-types}

WhatsApp 사용자 이름이 출시된 후에는 두 가지 유형의 WhatsApp 사용자가 있게 됩니다:

| 사용자 유형 | WhatsApp 식별 | Braze가 수신하는 정보 |
| ----- | ----- | ----- |
| 사용자 이름이 없는 사용자 | 전화번호(변경 없음) | 전화번호(변경 없음) |
| 사용자 이름이 있는 사용자 | 사용자 이름(표시됨), BSUID(백엔드) | BSUID, 비즈니스와 기존 대화가 있는 사용자의 전화번호 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Changes to WhatsApp user types" }

핵심적인 차이점은 사용자 이름을 채택한 사용자가 이전에 대화한 적이 있거나 WhatsApp 연락처 목록에 있는 경우에만 비즈니스에 전화번호를 공유한다는 것입니다.

## Braze의 BSUID 처리 방식 {#how-braze-will-handle-bsuids}

Braze는 BSUID를 고객 프로필에 `whats_app_bsuid` 레이블이 있는 [사용자 별칭]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/#user-aliases)으로 저장합니다. 이는 BSUID만 있는 사용자도 완전한 Braze 고객 프로필을 가지며 Canvases에 진입하고, 메시지를 수신하고, 이벤트를 생성하고, API를 통해 업데이트될 수 있음을 의미합니다.

### 메시지 전송 {#send-messages}

Braze가 WhatsApp 메시지를 전송할 때, 전화번호가 있으면 전화번호를 사용합니다. 사용자에게 BSUID만 있는 경우(예: 사용자 이름을 채택한 후 처음으로 메시지를 보낸 사용자), Braze는 대신 BSUID를 사용하여 전송합니다. 메시지 템플릿, Campaigns 또는 캔버스 단계를 변경할 필요가 없습니다.

### 인바운드 메시지 및 Canvas 트리거 {#inbound-messages-and-canvas-triggers}

사용자 이름이 있는 사용자가 인바운드 WhatsApp 메시지를 보내면, Braze는 다음을 수행합니다:

1. BSUID 또는 전화번호(웹훅에서 사용 가능한 것)로 사용자를 조회합니다.
2. 일치하는 사용자가 없으면, BSUID를 사용자 별칭으로 저장한 새 익명 사용자 프로필을 생성합니다.
3. 인바운드 WhatsApp 메시지에서 시작하도록 구성된 Canvas 또는 Campaign을 트리거합니다.

### 고객 프로필 {#user-profile}

사용자의 BSUID는 Braze 고객 프로필의 WhatsApp 섹션에서 확인할 수 있습니다.

![비즈니스 범위 사용자 ID가 포함된 WhatsApp 섹션이 있는 고객 프로필.]({% image_buster /assets/img/whatsapp/bsuid_profile.png %}){: style="max-width:60%;"}

### 구독 그룹 {#subscription-groups}

구독 그룹 관리는 사용자 별칭으로 식별된 모든 사용자와 동일한 방식으로 BSUID 사용자에게도 작동합니다. 다음을 통해 BSUID 사용자의 구독 상태를 업데이트할 수 있습니다:

- `user_alias`를 사용하는 [users/track 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)
- [사용자 업데이트]({{site.baseurl}}/user_update/) 캔버스 단계(자동으로 작동)
- CSV 업로드

{% alert note %}
[subscription/status/set 엔드포인트]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/)는 [`user_alias`]({{site.baseurl}}/api/objects_filters/user_alias_object/)를 지원하지 않습니다. BSUID만 있는 사용자의 구독 상태를 업데이트하려면 [users/track 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)를 사용하세요.
{% endalert %}

### Currents 및 이벤트 데이터 {#currents-and-event-data}

모든 WhatsApp Currents 이벤트(전송, 전달, 읽음, 실패, 인바운드 수신, 중단, 재시도)에는 BSUID 필드가 포함됩니다. 전화번호와 BSUID가 모두 있는 사용자의 경우 두 필드가 모두 포함됩니다. BSUID만 있는 사용자의 경우 BSUID 필드만 포함됩니다(전화번호 필드는 비어 있음).

## 변경 사항에 대비하는 방법 {#how-to-prepare-for-the-change}

대부분의 고객은 별도의 조치가 필요하지 않습니다. Braze가 BSUID 라우팅, 사용자 생성 및 이벤트 추적을 자동으로 처리합니다. 그러나 [WhatsApp 연락처 목록 활성화](#enable-whatsapp-contact-book)와 여러 WhatsApp Business 계정(WABA)을 사용하는 경우 [비즈니스 포트폴리오 연결](#link-business-portfolios-if-you-use-multiple-wabas)을 권장합니다.

### WhatsApp 연락처 목록 활성화 {#enable-whatsapp-contact-book}

연락처 목록은 이미 대화한 사용자의 전화번호를 기록하는 Meta 기능입니다. 사용자가 사용자 이름을 채택하면, 연락처 목록에 있는 경우 해당 사용자의 전화번호가 비즈니스에 계속 표시됩니다. 이는 사용자가 사용자 이름을 활성화한 후에도 Braze가 전화번호로 사용자를 계속 식별할 수 있음을 의미합니다.

연락처 목록을 활성화하려면:

1. **Meta Business Suite** > **비즈니스 설정** > **비즈니스 정보**로 이동합니다.
2. 연락처 목록 기능이 활성화되어 있는지 확인합니다.

{% alert tip %}
연락처 목록 기능은 기본적으로 활성화되어 있지만, Meta 비즈니스 설정에서 확인하는 것을 권장합니다. 연락처 목록이 비활성화된 경우, 사용자 이름을 채택한 사용자는 이전에 메시지를 보낸 적이 있더라도 새로운 BSUID 전용 사용자로 표시됩니다.
{% endalert %}

### 여러 WABA를 사용하는 경우 비즈니스 포트폴리오 연결 {#link-business-portfolios-if-you-use-multiple-wabas}

BSUID는 단일 비즈니스 포트폴리오에 범위가 지정됩니다. 조직이 동일한 Braze 워크스페이스 내에서 여러 비즈니스 포트폴리오의 WABA를 관리하는 경우, 동일한 사용자가 각 포트폴리오마다 다른 BSUID를 갖게 됩니다. 이로 인해 Braze 고객 프로필이 중복될 수 있습니다.

이를 방지하려면 Meta 담당자에게 연락하여 비즈니스가 포트폴리오 연결 자격이 있는지 확인하세요. 자세한 내용은 [비즈니스 포트폴리오 연결 및 상위 BSUID](#link-business-portfolios-and-parent-bsuids)를 참조하세요.

모든 WABA가 동일한 비즈니스 포트폴리오 내에 있는 경우 별도의 조치가 필요하지 않습니다.

## 비즈니스 포트폴리오 연결 및 상위 BSUID {#link-business-portfolios-and-parent-bsuids}

조직이 서로 다른 비즈니스 포트폴리오에 걸쳐 여러 WhatsApp Business 계정(WABA)을 운영하는 경우, Meta 담당자에게 연락하여 해당 포트폴리오를 함께 연결할 자격이 있는지 확인할 수 있습니다. 자격은 Meta에서 결정하며 관리형 비즈니스에 제공됩니다.

### 연결된 포트폴리오 동작 {#linked-portfolio-behavior}

비즈니스 포트폴리오가 연결되면, WhatsApp은 모든 메시지 웹훅에 일반 BSUID와 함께 상위 BSUID를 포함합니다. 상위 BSUID는 웹훅 페이로드의 새로운 `parent_user_id` 등록정보에 할당됩니다.

상위 BSUID는 일반 BSUID와 동일한 속성을 가지지만, 연결된 포트폴리오 세트 내의 모든 비즈니스 전화번호에서 공유됩니다. 이는 동일한 사용자가 어떤 WABA에 메시지를 보내든 단일 일관된 식별자를 가지게 되어 중복 고객 프로필의 위험을 방지합니다.

상위 BSUID는 국가 코드와 영숫자 식별자 사이에 `ENT`를 포함합니다. 예를 들어:

```
US.ENT.11815799212886844830
```

일반 BSUID에는 `ENT`가 포함되지 않습니다.

### Braze의 상위 BSUID 사용 방식 {#how-braze-uses-parent-bsuids}

웹훅에 일반 BSUID와 상위 BSUID가 모두 포함된 경우, Braze는 상위 BSUID를 기본 식별자로 사용합니다. 이를 통해 연결된 포트폴리오의 여러 WABA에 메시지를 보내는 사용자가 동일한 Braze 고객 프로필에 일관되게 매칭됩니다.

상위 BSUID가 없는 경우(예: 포트폴리오가 연결되지 않았거나 사용자가 연결되지 않은 WABA에 메시지를 보내는 경우), Braze는 일반 BSUID를 사용합니다. 일반 BSUID는 모든 경우에 정상적으로 계속 작동합니다.

{% alert note %}
Meta가 비즈니스 포트폴리오 연결 프로세스를 관리합니다. 시작하려면 Meta 담당자에게 연락하세요. 포트폴리오가 연결되어 있더라도 일반 BSUID를 사용하여 사용자에게 메시지를 보낼 수 있습니다. 상위 BSUID는 대체가 아닌 추가 기능입니다.
{% endalert %}

| 시나리오 | Braze가 사용하는 식별자 |
| ----- | ----- |
| 단일 비즈니스 포트폴리오 | 일반 BSUID |
| 여러 연결된 포트폴리오 | 상위 BSUID(우선). 상위 BSUID가 없으면 일반 BSUID 사용 |
| 여러 연결되지 않은 포트폴리오 | 일반 BSUID(포트폴리오별로 중복 고객 프로필이 생성될 수 있음) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="How Braze uses parent BSUIDs" }

## 자주 묻는 질문 {#frequently-asked-questions}

### WhatsApp 사용자 이름이 출시되면 기존 Campaigns와 Canvases가 중단되나요? {#will-my-existing-campaigns-and-canvases-break-when-whatsapp-usernames-launch}

아닙니다. 기존 Campaigns와 Canvases는 계속 작동합니다. 사용자 이름을 채택하지 않은 사용자는 전혀 영향을 받지 않습니다. 사용자 이름을 채택하고 비즈니스와 기존 대화 기록이 있는 사용자의 경우, Braze는 계속해서 전화번호를 기본 식별자로 사용합니다.

### 사용자가 사용자 이름을 채택했지만 이미 비즈니스에 메시지를 보낸 적이 있는 경우 어떻게 되나요? {#what-happens-to-a-user-who-adopts-a-username-but-has-already-messaged-my-business}

WhatsApp 연락처 목록이 활성화되어 있고 최근 30일 이내에 해당 사용자와 대화한 적이 있는 경우(또는 메시지를 보낸 경우), 해당 사용자의 전화번호가 BSUID와 함께 웹훅 페이로드에 계속 표시됩니다. Braze는 기존 고객 프로필에 매칭합니다. 중복 프로필은 생성되지 않습니다.

### 사용자가 사용자 이름을 채택했지만 비즈니스와 이전 대화가 없는 경우 어떻게 되나요? {#what-if-a-user-adopts-a-username-and-has-no-prior-conversation-with-my-business}

Braze는 인바운드 웹훅에서 사용자의 BSUID를 수신하고, 기존 고객 프로필에 매칭하거나(이전에 BSUID를 저장한 경우) BSUID를 사용자 별칭으로 저장한 새 익명 사용자 프로필을 생성합니다. 해당 사용자는 Canvases에 진입하고, 아웃바운드 메시지를 수신하고, Braze 표준 ID 확인 도구를 사용하여 다른 프로필과 식별 또는 병합될 수 있습니다.

### BSUID 사용자를 Segments에서 타겟팅할 수 있나요? {#can-i-target-bsuid-users-in-segments}

BSUID 사용자는 완전한 Braze 고객 프로필이므로 표준 오디언스 필터(예: "WhatsApp 메시지를 수신한 적이 있음" 또는 구독 그룹 멤버십)를 통해 타겟팅할 수 있습니다. 그러나 BSUID 값을 기준으로 구체적으로 세분화하는 것(예: "BSUID가 존재함" 또는 "BSUID가 X와 같음")은 지원되지 않습니다.

### BSUID 사용자에 대한 WhatsApp 요금은 어떻게 적용되나요? {#how-does-whatsapp-pricing-work-for-bsuid-users}

WhatsApp 대화 요금은 사용자의 국가에 따라 결정됩니다. 전화번호로 식별된 사용자의 경우, Meta는 전화번호의 국가 코드에서 국가를 파악합니다. BSUID로 식별된 사용자의 경우, 국가가 BSUID 자체에 직접 인코딩되어 있습니다. 예를 들어, `US`로 시작하는 BSUID는 미국의 사용자를 나타냅니다.

이는 사용자가 전화번호로 식별되든 BSUID로 식별되든 요금 적용 방식이 일관됨을 의미합니다. 대화 요금을 계산하는 데 사용되는 국가는 Meta가 제공하는 식별자에 의해 결정되며, Braze는 이를 수정 없이 전달합니다. 별도로 다르게 할 필요는 없지만, BSUID 전용 사용자에게 메시지를 보낼 때 Meta의 국가 기반 요금이 전화번호가 아닌 사용자의 BSUID에 인코딩된 국가를 기반으로 한다는 점을 알아두세요.

### API 호출에서 BSUID 사용자를 어떻게 참조하나요? {#how-do-i-reference-a-bsuid-user-in-api-calls}

`user_alias` 파라미터에 `alias_label: "whats_app_bsuid"`와 `alias_name`을 사용자의 BSUID 값으로 설정하여 사용합니다. 예를 들어:

```json
{
  "user_alias": {
    "alias_label": "whats_app_bsuid",
    "alias_name": "DDC91135R"
  }
}
```

이는 `users/track`, `users/identify`, CSV 업로드 및 사용자 업데이트 캔버스 단계에서 작동합니다.

### Currents 데이터 파이프라인이 중단되나요? {#will-my-currents-data-pipelines-break}

WhatsApp용 Currents 이벤트에는 기존 전화번호 필드와 함께 `bsuid` 필드가 포함됩니다. BSUID만 있는 사용자의 경우 전화번호 필드는 비어 있습니다. 다운스트림 파이프라인에 전화번호 필드에 대한 엄격한 요구 사항이 있는 경우, null 또는 빈 값을 처리할 수 있는지 확인하세요.

### 서로 다른 비즈니스 포트폴리오에 걸쳐 여러 WABA가 있습니다. 동일한 사용자가 Braze에서 두 개의 다른 프로필로 표시되나요? {#i-have-multiple-wabas-across-different-business-portfolios-will-the-same-user-appear-as-two-different-profiles-in-braze}

연결된 포트폴리오가 없으면 그렇습니다. 동일한 WhatsApp 사용자가 비즈니스 포트폴리오별로 다른 BSUID를 가지게 되며, Braze는 각각에 대해 별도의 프로필을 생성합니다.

이를 해결하려면 Meta 담당자에게 연락하여 포트폴리오 연결 자격을 확인하세요. 연결되면 Meta가 모든 포트폴리오에서 공유되는 상위 BSUID를 제공하며, Braze는 이를 사용하여 WABA 전체에서 사용자를 일관되게 식별합니다. 자세한 내용은 [비즈니스 포트폴리오 연결 및 상위 BSUID](#link-business-portfolios-and-parent-bsuids)를 참조하세요.

### 연락처 목록을 비활성화할 수 있나요? {#can-i-disable-the-contact-book}

연락처 목록을 활성화된 상태로 유지하는 것을 강력히 권장합니다. 연락처 목록이 비활성화되면 사용자의 모든 기존 전화번호 기록이 손실됩니다. 사용자 이름을 채택한 사용자는 이전에 메시지를 보낸 적이 있더라도 새로운 BSUID 전용 사용자로 표시됩니다.

## 추가 리소스 {#additional-resources}

* [WhatsApp 설정]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/)
* [사용자 별칭]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/#user-aliases)
* [WhatsApp 구독 그룹]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups/)
* [WhatsApp Currents 이벤트]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/#whatsapp)
* [Meta: 비즈니스 범위 사용자 ID](https://developers.facebook.com/documentation/business-messaging/whatsapp/business-scoped-user-ids)