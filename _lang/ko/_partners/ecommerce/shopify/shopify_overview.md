---
nav_title: Shopify 개요
article_title: Shopify 개요
description: "이 참조 문서에서는 Braze와 글로벌 커머스 기업인 Shopify 간의 파트너십에 대해 설명합니다. Shopify 스토어를 Braze에 원활하게 연결하여 선택한 Shopify 웹훅을 Braze로 전달할 수 있습니다. Braze의 크로스채널 전략과 Canvas를 활용하여 고객이 구매를 완료하도록 유도하거나 이전 구매를 기반으로 사용자를 리타겟할 수 있습니다."
page_type: partner
search_tag: Partner
alias: /shopify_overview/
page_order: 0
---

# Shopify 개요 {#shopify-overview}

> [Shopify](https://www.shopify.com/)는 모든 규모의 비즈니스를 시작, 성장, 마케팅 및 관리할 수 있는 신뢰할 수 있는 도구를 제공하는 선도적인 글로벌 커머스 기업입니다. Shopify는 안정성을 위해 설계된 플랫폼과 서비스를 통해 모든 곳의 소비자에게 더 나은 쇼핑 경험을 제공하며 커머스를 더 나은 방향으로 발전시킵니다.

Braze와 Shopify의 통합은 고객 참여를 강화하고 개인화된 마케팅 활동을 추진하고자 하는 이커머스 비즈니스에 강력한 솔루션을 제공합니다. 이 통합은 Shopify의 강력한 이커머스 기능과 고도화된 고객 인게이지먼트 플랫폼을 원활하게 연결하여 실시간 쇼핑 행동 및 트랜잭션 데이터를 기반으로 사용자에게 타겟팅된 관련성 있고 시의적절한 메시지를 전달할 수 있도록 지원합니다.

## 요구 사항 {#requirements}

| 요구 사항 | 설명 |
| --- | --- |
| Shopify 스토어 | 활성 Shopify 스토어가 있어야 합니다. |
| Shopify 스토어 소유자 또는 스태프 멤버 권한 | {::nomarkdown}<ul><li>모든 일반 및 온라인 스토어 설정에 대한 액세스.</li><li> 추가 관리자 권한:<ul><li>Orders: View</li><li>Customer: ReadWrite</li><li>View Customer Events (Web Pixels)</li><li>Manage Settings</li><li>View Apps Developed by Staff/Collaborators</li><li>Manage/Install Apps and Channels</li><li>Manage/Add Custom Pixels</li></ul></li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="요구 사항" }

## 통합 방법 {#how-to-integrate}

Braze는 이커머스 비즈니스의 다양한 요구를 충족할 수 있도록 Shopify 판매자를 위한 두 가지 통합 옵션을 제공합니다: **표준 통합**과 **커스텀 통합**입니다.

{% multi_lang_include partners/shopify.md section='Integration Tabs' %}

## 통합 작동 방식 {#how-the-integration-works}

구성 설정에서 [과거 데이터 백필]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features#historical-backfill)을 이미 설정하고 활성화한 경우, 초기 데이터 동기화가 즉시 시작됩니다.

{% multi_lang_include partners/shopify.md section='Custom external ID historical backfill' %}

초기 데이터 동기화 이후, Braze는 Shopify와 Braze SDK에서 직접 새로운 데이터와 업데이트를 지속적으로 추적합니다.

{% alert note %}
기존 Braze 고객으로서 활성 Campaigns 또는 Canvases가 있는 경우, 중요한 정보를 위해 [Shopify 과거 데이터 백필]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features#historical-backfill)을 검토하세요. 백필되는 구체적인 고객 데이터를 확인하려면 [Shopify 기능]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features)을 참조하세요.
{% endalert %}

### 사용자 및 데이터 동기화 {#user-and-data-syncing}

통합이 실시간으로 가동되면, Braze는 Shopify 통합을 통해 두 가지 주요 소스에서 사용자 데이터를 수집합니다:
- **Shopify 웹 픽셀 API 및 앱 임베드:** Braze 웹 SDK와 Javascript SDK를 구동하여 사이트 내 추적, ID 관리, 이커머스 행동 데이터 및 인앱 메시지와 같은 메시징 채널을 지원합니다.
- **Shopify 웹훅:** 이커머스 행동 데이터, 제품 동기화, 가입자 수집

통합 온보딩 중에 Braze SDK가 Shopify 사이트를 초기화하고 로드하는 시점을 선택해야 합니다:
- 사이트 방문 시(예: 세션 시작)
    - **동작 내용:** 게스트 쇼핑객과 같은 익명 사용자를 추적하여 더 깊은 개인화를 위한 더 많은 데이터에 접근합니다
- 계정 가입 시(예: 계정 로그인)
    - **동작 내용:** 보다 보수적이고 프라이버시 중심의 접근 방식으로 익명 사용자 추적을 방지하여, 사용자가 계정에 로그인한 *이후*에만 사용자 활동을 추적합니다

{% alert note %}
- 웹사이트 방문(세션)은 월간 활성 사용자(MAU) 할당량에 포함됩니다.
- Braze 웹 SDK 및 JavaScript SDK 버전은 자동으로 v6.8.0으로 설정됩니다. 통합 설정에서 언제든지 SDK 버전을 업그레이드할 수 있습니다.
{% endalert %}

Braze는 Shopify 통합을 사용하여 게스트 쇼핑 경험부터 식별된 사용자가 될 때까지 사용자를 추적하는 여러 식별자를 지원합니다:

| Braze 식별자 | 설명 |
| --- | --- |
| Braze `device_id` | 브라우저에 저장되는 무작위로 생성된 ID로, Braze SDK를 통해 익명 사용자 활동을 추적합니다. |
| 장바구니 토큰 사용자 별칭 | Braze가 장바구니 업데이트 이벤트를 추적하기 위해 생성하는 별칭입니다. 이 토큰은 Shopify 장바구니 토큰을 사용하여 생성됩니다. |
| 결제 토큰 사용자 별칭 | 사용자가 결제 프로세스를 시작할 때 Braze가 생성하는 별칭입니다. 이 토큰은 Shopify 결제 토큰을 사용하여 생성됩니다.<br><br> 고객이 Shop Pay를 빠른 결제 옵션으로 사용하는 경우, Shopify가 특정 표준 결제 이벤트를 건너뛰어 Braze가 결제 토큰 별칭을 추가하는 데 필요한 데이터를 수신하지 못할 수 있습니다. |
| Shopify 고객 ID 별칭 | Shopify 고객 ID는 계정 로그인 시 또는 주문이 발생할 때 외부 ID가 할당되면서 별칭으로 지정됩니다. |
| Braze `external_id` | 기기와 플랫폼에 걸쳐 고객을 추적하는 데 도움이 되는 고유 식별자입니다. 이를 통해 사용자가 기기를 전환하거나 앱을 재설치할 때 다중 프로필을 방지하여 일관된 사용자 경험을 유지하고 분석을 개선합니다.<br><br>Shopify 통합은 다음과 같은 `external_id` 유형을 지원합니다: <br><br>{::nomarkdown}<ul><li>Shopify 고객 ID(기본값)</li><li>커스텀 외부 ID</li><li>해시된 이메일(SHA-256)</li><li>해시된 이메일(SHA-1)</li><li>해시된 이메일(MD5)</li><li>이메일</li></ul>{:/}Braze는 다음과 같은 경우 SDK 내에서 changeUser 메서드를 호출하여 사용자에게 `external_id`를 할당합니다: <br><br>{::nomarkdown}<ul><li>사용자가 로그인하거나 계정을 생성할 때</li><li>주문이 발생할 때</li></ul>{:/}<br> 익명 프로필에 `external_id`를 할당할 때 발생하는 상황에 대한 자세한 내용은 [사용자 프로필 수명주기]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#what-happens-when-you-identify-anonymous-users)를 참조하세요.<br><br>Braze는 또한 `external_id`를 활용하여 Shopify 웹훅에서 오는 다운스트림 이커머스 행동 데이터를 귀속시킵니다.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="사용자 및 데이터 동기화" }

통합에는 Braze SDK와 Shopify 서비스가 함께 작동하여 Shopify 데이터를 거의 실시간으로 적절한 사용자에게 추적 및 귀속시켜야 합니다. 통합을 통해 추적되는 데이터에 대한 자세한 내용은 [Shopify 데이터]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features)를 참조하세요.

{% alert note %}
- 통합을 테스트하는 경우, Braze `device_id`를 재설정하고 익명 사용자의 행동을 모방하기 위해 시크릿 모드를 사용하거나 쿠키를 삭제하는 것을 권장합니다.
- Shopify 뉴스레터 푸터에 이메일을 입력하거나 주문이 발생하기 전 결제 과정에서 Shopify 고객 ID가 생성되더라도, 해당 고객 ID는 Shopify 웹 픽셀을 통해 접근할 수 없습니다. 이로 인해 Braze는 이 두 가지 상황에서 `changeUser` 메서드를 사용할 수 없습니다.
{% endalert %}

### Shopify 이메일 및 SMS 마케팅 옵트인 동기화 {#syncing-shopify-email-and-sms-marketing-opt-ins}

구성 설정에서 가입자 수집을 활성화하는 경우, Braze에 연결하는 각 스토어에 구독 그룹을 할당해야 합니다. 이렇게 하면 고객이 스토어의 구독 그룹에 대해 "subscribed" 또는 "unsubscribed"로 분류됩니다.

이메일 및 SMS 마케팅에 대한 Shopify 마케팅 옵트인 상태는 다음과 같은 방식으로 업데이트될 수 있습니다:
- **수동 업데이트:** Shopify 관리자에서 사용자의 이메일 또는 SMS 마케팅 옵트인 상태를 수동으로 변경할 수 있습니다.
- **Shopify 뉴스레터 푸터:** 사용자가 Shopify 기본 뉴스레터 푸터에 이메일을 입력하면 옵트인 상태가 업데이트됩니다.
- **결제:** 사용자가 마케팅 체크박스를 선택하고 단일 페이지 결제에서 **Pay now**를 선택하거나 3페이지 결제에서 **Continue to shipping**을 선택하여 결제를 진행할 때 사용자 동의가 수집됩니다.

{% alert note %}
Shopify의 이메일 마케팅 옵트인 상태는 Braze에서 사용자의 [글로벌 이메일 구독 상태]({{site.baseurl}}/user_guide/channels/email/subscriptions)를 변경하지 않습니다. 사용자 프로필이 생성될 때 기본 구독 상태는 "subscribed"입니다. Campaign 또는 Canvas 진입 기준의 일부로 구독 그룹을 사용하는 것을 잊지 마세요.
{% endalert %}

이 표는 Shopify 마케팅 옵트인 상태가 Braze 구독 그룹 내의 상태와 어떻게 대응하는지 보여줍니다.

| Shopify 마케팅 옵트인 상태 | Braze 구독 그룹 상태 |
| --- | --- |
| 이메일 구독됨 | Subscribed |
| 이메일 구독 해지됨 | Unsubscribed |
| 이메일 확인 대기 중 | Unsubscribed |
| 이메일 유효하지 않음 | Unsubscribed |
| SMS 구독됨 | Subscribed |
| SMS 구독 해지됨 | Unsubscribed |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Shopify 이메일 및 SMS 마케팅 옵트인 동기화" }

### 가입 양식 {#sign-up-forms}

#### Shopify 뉴스레터 푸터 {#shopify-newsletter-footer}

Shopify 뉴스레터 푸터에 이메일 주소를 입력하는 사용자는 다음 워크플로우 중 하나를 경험하게 됩니다:

##### 계정에 로그인하지 않은 사용자 {#users-who-havent-logged-into-their-account}

1. Braze는 고객이 생성되거나 업데이트될 때마다 인바운드 Shopify 웹훅을 수신합니다.
2. Braze는 해당 사용자와 연결된 이메일 주소 및 Shopify 고객 ID 별칭을 포함하는 사용자 프로필을 생성합니다.
3. Braze SDK가 익명 프로필을 이메일 주소로 업데이트합니다.

{% alert note %}
이로 인해 사용자가 계정 생성, 계정 로그인 또는 주문을 통해 자신을 식별할 때까지 중복 프로필이 발생할 수 있습니다. Braze는 중복 프로필의 조정을 자동화하는 데 도움이 되는 대량 병합 도구를 제공합니다. 자세한 내용은 [중복 사용자]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users)를 참조하세요.
{% endalert %}

##### 이미 계정에 로그인한 사용자 {#users-who-have-already-logged-into-their-account}

Braze는 해당 사용자와 연결된 이메일 주소 및 Shopify 고객 ID 별칭을 포함하는 사용자 프로필을 생성합니다. Braze는 Shopify가 이미 이 정보를 제공했다고 가정하므로 로그인한 사용자의 이메일 주소를 업데이트하지 않습니다.

#### Braze 가입 양식 {#braze-sign-up-forms}

Braze는 두 가지 유형의 가입 양식 템플릿을 제공합니다:
- **[이메일 가입 양식]({{site.baseurl}}/user_guide/messaging/templates/in_app_message_templates/email_capture):** 드래그 앤 드롭 편집기를 사용하여 생성합니다.
- **[기존 편집기 이메일 캡처 양식]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/email_capture_form):** 이메일 주소를 캡처하기 위한 보다 간단한 양식입니다.

이러한 가입 양식 템플릿을 사용하면, Braze가 사용자 프로필의 글로벌 이메일 구독 상태를 자동으로 업데이트합니다. 이메일 유효성 검사를 포함하여 글로벌 이메일 구독 상태가 처리되는 방식에 대한 자세한 내용은 각 양식 템플릿 유형의 설명서를 참조하세요.

{% alert note %}
- Shopify 스토어에 연결된 글로벌 이메일 구독 상태와 구독 그룹을 모두 포함하는 진입 기준을 Campaign 또는 Canvas에 포함해야 합니다. 이를 통해 올바른 오디언스를 타겟팅할 수 있습니다.
- Braze는 인브라우저 메시지를 통해 이메일 주소 및 전화번호와 같은 방문자 정보를 수집합니다. 이 정보는 Shopify Visitor API로 전송되지만 Shopify에서 고객 프로필을 생성하지는 않습니다. 자세한 내용은 [Visitor API](https://shopify.dev/docs/api/web-pixels-api/emitting-data#visitor-api)를 참조하세요.
{% endalert %}

#### 서드파티 가입 양식 {#third-party-sign-up-forms}

가입 양식에 서드파티 플랫폼이나 Shopify 플러그인을 사용하는 경우, 양식 제출에서 이메일 주소와 글로벌 이메일 구독 상태를 캡처하기 위해 개발자와 협력하여 Braze SDK 코드를 통합해야 합니다. 자세한 내용은 [Shopify 표준 통합 설정]({{site.baseurl}}/shopify_standard_integration) 및 [Shopify 커스텀 통합 설정]({{site.baseurl}}/shopify_custom_integration)을 참조하세요.

### 제품 동기화 {#product-syncing}

Braze는 Shopify 스토어의 제품을 Braze 카탈로그에 동기화하는 기능을 지원합니다. 자세한 내용은 [Shopify 제품 동기화]({{site.baseurl}}/shopify_catalogs)를 참조하세요.

## 데이터 주체 요청 {#data-subject-requests}

Braze 플랫폼의 Shopify 통합의 일환으로, Braze는 자동으로 [Shopify의 컴플라이언스 웹훅](https://shopify.dev/docs/apps/build/privacy-law-compliance/)을 수신합니다. 그러나 고객이 최종사용자 데이터의 데이터 관리자이므로, 고객은 Braze에 있는 최종사용자 데이터(Shopify 통합을 통해 수신된 최종사용자 데이터 포함)와 관련하여 수신된 데이터 주체 요청을 처리하는 데 필요한 모든 조치를 직접 수행해야 합니다. 자세한 내용은 [데이터 보호 기술 지원]({{site.baseurl}}/dp-technical-assistance) 설명서를 참조하세요.