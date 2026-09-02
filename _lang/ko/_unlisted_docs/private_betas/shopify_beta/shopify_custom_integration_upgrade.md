---
nav_title: Shopify 업그레이드 (커스텀)
article_title: "커스텀 Shopify 통합 업그레이드"
description: "Braze를 위한 커스텀 Shopify 통합을 업그레이드하는 방법을 알아보세요."
page_type: partner
search_tag: Partner
permalink: "/shopify_custom_upgrade/"
hidden: true
---

# Shopify 통합 업그레이드 (커스텀) {#upgrading-your-shopify-integration-custom}

> Braze의 커스텀 경로를 사용하여 Shopify 통합을 업그레이드하는 방법을 알아보세요. 최상의 경험을 제공하기 위한 노력의 일환으로, 모든 Shopify 통합은 2025년 8월 28일까지 최신 버전으로 [업그레이드]({{site.baseurl}}/shopify)해야 합니다. 이 업그레이드는 Shopify 기술의 중요한 변경 사항이 통합 기능에 영향을 미치기 때문에 필수적입니다.

## 대상은 누구인가요? {#whos-eligible}

이 업그레이드 경로는 Shopify 헤드리스 또는 Shopify Hydrogen 스토어를 운영하는 브랜드를 위한 것입니다.

{% multi_lang_include partners/shopify_alerts.md alert='breaking' %}

## 업그레이드 요구 사항 {#upgrade-requirements}

시작하기 전에 다음 사항을 확인하세요:

| 요구 사항           | 설명 |
|-----------------------|-------------|
| **중요 변경 사항**  | [Shopify 업그레이드 개요]({{site.baseurl}}/shopify_upgrade_overview#subscriber-collection)에서 기존 커넥터에서 새 커넥터로의 모든 중요 변경 사항을 확인했는지 확인하세요. |
| **업그레이드 사전 요구 사항** | 엔지니어링 및 마케팅 팀과 함께 필요한 모든 [업그레이드 사전 요구 사항]({{site.baseurl}}/shopify_upgrade_overview#upgrade-prerequisites)을 완료했는지 확인하세요. 헤드리스 Shopify 스토어를 Braze로 업그레이드하려면 두 가지 중요한 단계를 완료해야 합니다:<br><br>- 온사이트 추적 기술을 활성화하기 위해 Braze 웹 SDK를 초기화하고 로드합니다<br>- 제품 내 업그레이드 경험을 통해 기존 스토어를 업그레이드합니다 |
| **호환성 문제 변경 사항**  | Braze에서 표시된 모든 호환성 문제 변경 사항을 검토하고 수정하세요. 전체 안내는 [호환성 문제 변경 사항 수정](#fixing-breaking-changes-fixing-breaking-changes)을 참조하세요. |
{: .reset-td-br-1 .reset-td-br-2  role="presentation"}

## 호환성 문제 변경 사항 수정 {#fixing-breaking-changes}

Braze에서 **파트너 통합** > **Shopify**로 이동한 다음 **Start upgrade**를 선택합니다.

![업그레이드를 시작하는 옵션이 있는 패널.]({% image_buster /assets/unlisted_docs/img/shopify/start_shopify_custom_upgrade.png %}){: style="max-width:35%;"}

Shopify 데이터를 사용하는 영향을 받는 Canvases, Campaigns, Segments가 플래그됩니다.

![호환성 문제 변경 사항의 영향을 검토하는 모달.]({% image_buster /assets/unlisted_docs/img/shopify/review_breaking_changes.png %})

대부분의 이벤트에 대해, 활성 메시지의 원활한 업그레이드를 위해 "OR" 연산자를 사용하여 새로운 필수 Shopify 이벤트 및 속성을 포함하는 것을 권장합니다. 보다 구체적인 경우에는 다음을 참조하세요:

{% tabs local %}
{% tab 유기한 장바구니 %}
유기한 장바구니 메시징의 경우, 다음을 포함하는 새로운 유기한 장바구니 Canvas 템플릿을 사용해야 합니다:

{% multi_lang_include partners/shopify/abandoned_cart_template_features.md %}
{% endtab %}

{% tab 유기한 결제 %}
유기한 결제 메시징의 경우, 다음을 포함하는 새로운 유기한 결제 Canvas 템플릿을 사용해야 합니다:

{% multi_lang_include partners/shopify/abandoned_checkout_template_features.md %}

통합을 통해 사용할 수 있는 새로운 이커머스 Canvas 템플릿 및 제품 개인화를 위한 사전 정의된 HTML 블록의 전체 목록은 [Canvas 사용자 여정 만들기]({{site.baseurl}}using_shopify_with_braze#create-your-canvas-user-journeys)를 참조하세요.

{% alert important %}
Shopify 통합에서 중단된 이벤트를 사용하는 활성 메시지를 처리하지 않으면, 영향을 받는 메시지가 더 이상 고객에게 전송되지 않습니다.
{% endalert %}

자세한 내용은 [지원되는 Shopify 이벤트]({{site.baseurl}}/shopify_upgrade_overview#supported-shopify-events)를 참조하세요.
{% endtab %}

{% tab 구독자 목록 %}
통합을 통해 Shopify에서 이메일 또는 단문 메시지 서비스 구독자를 수집하는 경우, 활성 메시지에 Shopify 스토어에 해당하는 구독자 목록이 포함되어 있는지 확인하세요.

업그레이드가 완료되면 통합을 위한 새로운 기본 구독 그룹이 생성되며, 이를 활성 메시징의 일부로 활용해야 합니다. 변경 사항에 대한 자세한 내용은 [구독자 수집]({{site.baseurl}}/shopify_upgrade_overview#subscriber-collection)을 참조하세요.
{% endtab %}
{% endtabs %}

## Shopify 업그레이드 {#upgrading-shopify}

{% alert important %}
업그레이드를 시작하기 전에 반드시 [모든 호환성 변경 사항을 수정](#fixing-breaking-changes)해야 합니다.
{% endalert %}

### 1단계: Braze 웹 SDK를 초기화하고 로드하여 온사이트 추적 활성화 {#step-1}

아직 하지 않았다면, Braze 웹 SDK를 초기화하고 로드하여 온사이트 추적을 활성화합니다. 전체 안내는 [Shopify 커스텀 통합 설정]({{site.baseurl}}/partners/ecommerce/shopify/shopify_custom_integration#step-1)을 참조하세요:
- Braze 웹 앱 생성
- 하위 도메인 및 환경 변수 추가
- 온사이트 추적 활성화
- Shopify 계정 로그인 이벤트 추가
- Product Viewed 및 Cart Update 이벤트에 대한 추적 추가

### 2단계: 업그레이드 시작 {#step-2-start-the-upgrade}

Braze에서 **파트너 통합** > **Shopify**로 이동한 다음 **Start upgrade**를 선택합니다.

![업그레이드를 시작하는 옵션이 있는 패널.]({% image_buster /assets/unlisted_docs/img/shopify/start_shopify_custom_upgrade.png %}){: style="max-width:35%;"}

체크박스를 선택하여 업그레이드 가이드라인에 동의한 다음 **Start the upgrade**를 선택합니다.

![업그레이드 시 호환성 변경이 발생할 수 있음을 이해했는지 확인하는 모달.]({% image_buster /assets/unlisted_docs/img/shopify/confirm_upgrade.png %}){: style="max-width:50%;"}

개발자와 함께 커스텀 경로 업그레이드의 1단계를 완료했는지 체크박스를 선택하여 확인한 다음 **Confirm**을 선택합니다.

![1~5단계를 완료했는지 확인하는 체크박스가 있는 모달.]({% image_buster /assets/unlisted_docs/img/shopify/confirm_completed_steps.png %}){: style="max-width:50%;"}

{% alert important %}
통합이 올바르게 작동하려면 커스텀 업그레이드의 [1단계](#step-1)를 완료해야 합니다. 이 단계를 건너뛰면 통합이 제대로 작동하지 않을 수 있습니다.
{% endalert %}

### 3단계: Braze 앱 재인증 {#step-3-reauthorize-the-braze-app}

Braze 앱을 재인증하려면 **Go to Shopify**를 선택합니다.

![Shopify로 이동하는 옵션이 있는 패널.]({% image_buster /assets/unlisted_docs/img/shopify/custom_go_to_shopify.png %}){: style="max-width:35%"}

Shopify 사이트에서 프롬프트에 따라 Braze 앱을 재인증합니다. 이를 통해 Braze가 Shopify 데이터에 접근할 수 있습니다.

{% alert important %}
재인증 프로세스는 몇 분이 걸릴 수 있지만, 완료되면 Shopify 페이지에서 자동으로 업데이트됩니다.
{% endalert %}

![Braze 앱 재인증 옆에 로딩 아이콘이 있는 Shopify 업그레이드 패널.]({% image_buster /assets/unlisted_docs/img/shopify/reauthorize_app_loading.png %}){: style="max-width:35%;"}

### 4단계: 외부 ID 유형 선택 {#step-4-choose-an-external-id-type}

선택한 외부 ID 유형은 Shopify 계정이 생성되거나 주문이 이루어질 때 새로운 Shopify 고객 프로필에 할당됩니다. 또한 Shopify 고객 ID 별칭이 있지만 Braze에서 외부 ID가 할당되지 않은 기존 사용자 프로필을 업데이트하는 데에도 사용됩니다.

외부 ID 유형을 선택하려면 Braze로 돌아가서 **Confirm external ID**를 선택합니다.

![외부 ID를 확인하는 버튼이 있는 Shopify 업그레이드 패널.]({% image_buster /assets/unlisted_docs/img/shopify/custom_confirm_external_id.png %}){: style="max-width:35%;"}

워크스페이스의 Shopify 통합에 사용할 외부 ID를 선택합니다. 완료되면 **Set external ID**를 선택합니다.

![외부 ID를 선택하는 드롭다운이 있는 모달.]({% image_buster /assets/unlisted_docs/img/shopify/external_id_custom.png %}){: style="max-width:50%;"}

{% alert important %}
기본적으로 Braze는 Shopify의 이메일을 외부 ID로 사용하기 전에 자동으로 소문자로 변환합니다. 이메일 또는 해시된 이메일을 외부 ID로 사용하는 경우, 이메일 주소를 외부 ID로 할당하거나 다른 데이터 소스에서 해시하기 전에 소문자로 변환했는지 확인하세요. 이렇게 하면 외부 ID의 불일치를 방지하고 Braze에서 중복 사용자 프로필이 생성되는 것을 방지할 수 있습니다.
{% endalert %}

커스텀 외부 ID 유형을 선택한 경우 4.1~4.3단계로 진행합니다. 그렇지 않으면 5단계로 계속 진행합니다.

#### 4.1단계: `braze.external_id` 메타필드 생성 {#step-41-create-the-brazeexternal_id-metafield}

{% multi_lang_include partners/shopify/customer_metafield_definition_steps.md %}

메타필드가 생성된 후 고객에 대해 이를 채워야 합니다. 다음 접근 방식을 권장합니다:

- **고객 생성 웹훅 수신:** [`customer/create` 이벤트](https://help.shopify.com/en/manual/fulfillment/setup/notifications/webhooks)를 수신하는 웹훅을 설정합니다. 이를 통해 새 고객이 생성될 때 메타필드를 작성할 수 있습니다.
- **기존 고객 백필:** [Admin API](https://shopify.dev/docs/api/admin-graphql) 또는 [Customer API](https://shopify.dev/docs/api/admin-rest/2025-04/resources/customer)를 사용하여 이전에 생성된 고객의 메타필드를 백필합니다.

#### 4.2단계: 외부 ID를 조회하는 엔드포인트 생성 {#step-42-create-an-endpoint-to-retrieve-your-external-id}

Braze가 외부 ID를 조회하기 위해 호출할 수 있는 공개 엔드포인트를 생성해야 합니다. 이는 Shopify가 `braze.external_id` 메타필드를 제공할 수 없는 시나리오에 필요합니다.

##### 엔드포인트 사양 {#endpoint-specifications}

**메서드:** `GET`

| 파라미터 | 설명 |
| --- | --- |
| `shopify_customer_id` | Shopify 고객 ID. |
| `email_address` | 로그인한 사용자의 이메일 주소. |
| `shopify_storefront` | 요청에 대한 스토어프론트. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

##### 엔드포인트 예시 {#example-endpoint}

```
GET
https://mystore.com/custom_id?shopify_customer_id=1234&email_address=bob@example.com&shopify_storefront=dev-store.myshopify.com
```

##### 예상 응답 {#expected-response}

Braze는 `200` 상태 코드를 기대합니다. 다른 코드는 실패로 간주됩니다.

{% raw %}
```json
{ "external_id": "my_external_id" }
```
{% endraw %}

{% alert important %}
`shopify_customer_id`와 `email_address`가 Shopify의 고객 값과 일치하는지 검증하는 것이 중요합니다. [Admin API](https://shopify.dev/docs/api/admin-graphql) 또는 [Customer API](https://shopify.dev/docs/api/admin-rest/2025-04/resources/customer)를 사용하여 이러한 파라미터를 검증하고 `braze.external_id` 메타필드를 조회할 수 있습니다.
{% endalert %}

#### 4.3단계: 외부 ID 입력 {#step-43-input-your-external-id}

[4단계](#step-4-choose-an-external-id-type)를 반복하고, Braze 외부 ID 유형으로 커스텀 외부 ID를 선택한 후 엔드포인트 URL을 입력합니다.

##### 고려 사항 {#considerations}

{% multi_lang_include partners/shopify/external_id_generation_notes.md %}

### 5단계: Braze 앱 임베드 활성화 {#step-5-enable-the-braze-app-embed}

스토어 테마 내에서 Braze 앱 임베드를 활성화하려면 Braze로 돌아가서 Go to Shopify를 선택합니다.

![Braze 앱 임베드를 활성화하는 버튼이 있는 Shopify 업그레이드 패널.]({% image_buster /assets/unlisted_docs/img/shopify/custom_enable_app_embed.png %}){: style="max-width:35%;"}

Shopify 사이트에서 Braze 앱 임베드를 활성화한 다음 변경 사항을 저장합니다.

![앱 임베드 예시.]({% image_buster /assets/unlisted_docs/img/shopify/app_embed.png %})

### 6단계: 업그레이드 확인 {#step-6-verify-the-upgrade}

Braze로 돌아가면 Shopify 통합 설치가 완료되었을 때 알림을 받게 됩니다.

![성공 배너가 있는 Shopify 통합 페이지.]({% image_buster /assets/unlisted_docs/img/shopify/success_integration.png %})

새 Shopify 커넥터가 실시간으로 작동하는지 확인하려면 다음을 테스트합니다:

{% multi_lang_include partners/shopify/upgrade_validation_checklist.md %}

질문이 있는 경우 [고객 지원에 문의]({{site.baseurl}}/user_guide/administer/personal/braze_support)하세요.