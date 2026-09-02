---
nav_title: Shopify 표준 통합 설정
article_title: Shopify 표준 통합 설정
description: "이 참조 문서에서는 표준 Shopify 통합을 설정하는 방법을 설명합니다."
page_type: partner
search_tag: Partner
alias: /shopify_standard_integration/
page_order: 1
---

# Shopify 표준 통합 설정 {#shopify-standard-integration-setup}

> 이 페이지에서는 Shopify 온라인 스토어를 사용하는 사용자를 위한 표준 통합을 사용하여 Braze와 Shopify를 통합하는 방법을 안내합니다. Shopify 헤드리스 사이트를 사용하거나 더 맞춤화된 솔루션을 구현하려는 경우 [Shopify 커스텀 통합 설정]({{site.baseurl}}/shopify_custom_integration)을 참조하세요.

## 1단계: Shopify 스토어 연결 {#step-1-connect-your-shopify-store}

1. Braze에서 **파트너 통합** > **기술 파트너**로 이동한 다음 "Shopify"를 검색합니다.
2. Shopify 파트너 페이지에서 **설정 시작**을 선택하여 통합 프로세스를 시작합니다.<br><br>![설정 시작 버튼이 있는 Shopify 통합 페이지.]({% image_buster /assets/img/shopify/begin_setup.png %})<br><br>
3. Shopify 앱 스토어에서 Braze 애플리케이션을 설치합니다.<br><br>![애플리케이션 설치 버튼이 있는 Braze 앱 스토어 페이지.]({% image_buster /assets/img/shopify/shopify_log_in.png %}){: style="max-width:70%;"}

{% alert note %}
Shopify 계정이 둘 이상의 스토어와 연결되어 있는 경우 헤더의 스토어 아이콘을 선택하고 **스토어 전환**을 선택하여 로그인한 스토어를 변경할 수 있습니다.
{% endalert %}

{: start="4"}
4. Braze 앱을 설치한 후 Shopify에 연결할 워크스페이스를 확인하기 위해 Braze로 리디렉션됩니다. Shopify 스토어는 하나의 워크스페이스에만 연결할 수 있습니다. 전환이 필요한 경우 올바른 워크스페이스를 선택하세요.<br><br>![올바른 워크스페이스에 있는지 확인하는 창.]({% image_buster /assets/img/shopify/confirm_workspace1.png %}){: style="max-width:70%;"}

{: start="5"}
5. **설정 시작**을 선택합니다.<br><br>![도메인 입력 필드와 설정 시작 버튼이 있는 "통합 설정".]({% image_buster /assets/img/shopify/choose_account.png %})

## 2단계: Braze Web SDK 활성화 {#step-2-enable-braze-web-sdks}

Shopify 온라인 스토어의 경우 표준 설정을 선택하여 Braze Web SDK와 JavaScript SDK를 자동으로 구현할 수 있습니다.

![표준 설정 또는 커스텀 설정을 통해 구현하는 옵션이 있는 "Web SDK 활성화" 단계.]({% image_buster /assets/img/shopify/sdk_setup.png %})

표준 설정 온보딩 경로를 선택한 후 Braze가 SDK를 초기화하고 로드할 시점을 다음 옵션 중에서 선택해야 합니다:
- 사이트 방문 시(예: 세션 시작)
    - 식별된 사용자와 익명 사용자 모두 추적
- 계정 가입 시(예: 계정 로그인)
    - 식별된 사용자만 추적
    - 사이트 방문자가 계정에 가입하거나 로그인할 때 데이터 추적 시작

{% alert note %}
신규 고객은 설정 중에 최신 Braze Web SDK 및 JavaScript SDK 버전으로 프로비저닝됩니다. 기존 고객은 통합 설정에서 현재 SDK 버전을 확인하고, 새 버전이 출시되면 알림을 받으며, 통합 설정에서 직접 업그레이드할 수 있습니다.
{% endalert %}

## 3단계: Shopify 데이터 구성 {#step-3-configure-your-shopify-data}

### 표준 데이터 설정 {#standard-data-setup}

{% multi_lang_include alerts/important_alerts.md alert='Shopify cart token alias' %}

이제 추적할 Shopify 데이터를 선택합니다.

![행동 이벤트 및 사용자 속성을 추적하는 체크박스가 있는 "Shopify 데이터 추적" 섹션.]({% image_buster /assets/img/shopify/tracking_shopify_data.png %})

다음 이벤트는 표준 통합에서 기본적으로 활성화됩니다.

| Braze 권장 이벤트 | Shopify 커스텀 이벤트 | Shopify 커스텀 속성 |
| --- | --- | --- |
| {::nomarkdown}<ul><li>Product viewed</li><li>Cart updated</li><li>Checkout started</li><li>Order placed</li></ul>{:/}  | {::nomarkdown}<ul><li>shopify_account_login</li><li>shopify_paid_order</li><li>shopify_order_canceled</li><li>shopify_order_refunded</li><li>shopify_order_fulfilled</li><li>shopify_order_partially_fulfilled</li></ul>{:/} | {::nomarkdown}<ul><li>shopify_tags</li><li>shopify_total_spent</li><li>shopify_order_count</li><li>shopify_last_order_id</li><li>shopify_last_order_name</li><li>shopify_zipcode</li><li>shopify_province</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2  .reset-td-br-3 aria-label="표준 데이터 설정" }

통합을 통해 추적되는 데이터에 대한 자세한 내용은 [Shopify 데이터 기능]({{site.baseurl}}/shopify_data_features)을 참조하세요.

{% multi_lang_include alerts/important_alerts.md alert='Shopify customer create' %}

### 과거 데이터 백필 설정 {#historical-backfill-setup}

**Shopify 데이터 추적** 단계에서 통합의 일부로 초기 과거 데이터 로드를 포함하려면 체크박스를 선택합니다.

가져오는 항목, 매출 보고 동작, 설정 스크린샷, 그리고 활성 Campaign(캠페인) 또는 Canvas와 함께 이미 Braze를 사용하고 있는 경우의 안내는 [과거 데이터 백필]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features#historical-backfill)을 참조하세요.

### (고급) 커스텀 데이터 추적 설정 {#advanced-custom-data-tracking-setup}

Braze SDK를 사용하면 이 통합의 표준 이벤트를 넘어서는 커스텀 이벤트 또는 커스텀 속성을 추적할 수 있습니다. 커스텀 이벤트는 스토어에서의 고유한 상호작용을 캡처합니다. 예를 들면 다음과 같습니다:

<style>
#custom-data td {
    word-break: break-word;
    width: 50%;
}
</style>

<table aria-label="(고급) 커스텀 데이터 추적 설정" style="width: 100%;">
  <caption>(고급) 커스텀 데이터 추적 설정</caption>
  <thead>
    <tr>
      <th style="width: 50%;">커스텀 이벤트</th>
      <th style="width: 50%;">커스텀 속성</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <ul>
          <li>커스텀 할인 코드 사용</li>
          <li>개인화된 제품 추천과의 상호작용</li>
          <li>주문에 선물 메시지 추가</li>
        </ul>
      </td>
      <td>
        <ul>
          <li>선호 브랜드 또는 제품</li>
          <li>선호 쇼핑 카테고리</li>
          <li>멤버십 또는 로열티 상태</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

커스텀 데이터를 추적하면 사용자 행동에 대한 심층적인 인사이트를 확보하고 추가적인 개인화를 지원할 수 있습니다. 커스텀 이벤트를 구현하려면 `theme.liquid` 파일에서 [스토어프론트의 테마 코드](https://help.shopify.com/en/manual/online-store/themes/theme-structure/extend/edit-theme-code)를 편집해야 합니다. 개발자의 도움이 필요할 수 있습니다.

예를 들어, 다음 JavaScript 스니펫은 현재 사용자가 뉴스레터를 구독하는지 추적하고 이를 Braze의 프로필에 커스텀 이벤트로 기록합니다:

```javascript
braze.logCustomEvent(
  “subscribed_to_newsletter”,
  {
    newsletterName: ‘News and Offers’,
    customerEmail: ‘customer_1@example.com’,
    sendOffers: true
  }
);

```

이벤트 또는 커스텀 속성을 기록하려면 사용자의 기기에서 SDK가 초기화(활동 수신 대기)되어 있어야 합니다. 커스텀 데이터 기록에 대해 자세히 알아보려면 [User object](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html) 및 [logCustomEvent object](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcustomevent)를 참조하세요.

## 4단계: 사용자 관리 방법 구성 {#step-4}

드롭다운에서 `external_id` 유형을 선택합니다.

!["구독자 수집" 섹션.]({% image_buster /assets/img/shopify/external_id_standard.png %})

{% alert important %}
이메일 주소 또는 해시된 이메일 주소를 Braze 외부 ID로 사용하면 데이터 소스 전반에서 ID 관리를 간소화할 수 있습니다. 그러나 사용자 개인정보 보호 및 데이터 보안에 대한 잠재적 위험을 고려하는 것이 중요합니다.<br><br>

- **추측 가능한 정보:** 이메일 주소는 쉽게 추측할 수 있어 공격에 취약합니다.
- **악용 위험:** 악의적인 사용자가 웹 브라우저를 변조하여 다른 사람의 이메일 주소를 외부 ID로 전송하면 민감한 메시지나 계정 정보에 접근할 수 있습니다.
{% endalert %}

기본적으로 Braze는 Shopify의 이메일을 외부 ID로 사용하기 전에 소문자로 자동 변환합니다. 이메일 또는 해시된 이메일을 외부 ID로 사용하는 경우, 외부 ID로 할당하기 전이나 다른 데이터 소스에서 해시하기 전에 이메일 주소도 소문자로 변환되었는지 확인하세요. 이렇게 하면 외부 ID의 불일치를 방지하고 Braze에서 중복 고객 프로필이 생성되는 것을 막을 수 있습니다.

{% alert note %}
다음 단계는 외부 ID 선택에 따라 달라집니다:<br><br>
- **커스텀 외부 ID 유형을 선택한 경우:** 4.1~4.3단계를 완료하여 커스텀 외부 ID 구성을 설정합니다.
- **Shopify 고객 ID, 이메일 또는 해시된 이메일을 선택한 경우:** 4.1~4.3단계를 건너뛰고 바로 4.4단계로 진행합니다.
{% endalert %}

### 4.1단계: `braze.external_id` 메타필드 만들기 {#step-41-create-the-brazeexternal_id-metafield}

1. Shopify 관리자 패널에서 **Settings** > **Metafields and metaobjects**로 이동합니다.
2. **Customers** > **Add definition**을 선택합니다.
3. **Name**에 `braze.external_id`를 입력합니다.
4. 자동 생성된 네임스페이스와 키(`custom.braze_external_id`)를 선택하여 편집하고 `braze.external_id`로 변경합니다.
5. **Type**에서 **ID Type**을 선택합니다.

메타필드가 생성되면 고객에 대해 메타필드를 채웁니다. 다음과 같은 방법을 권장합니다:

- **고객 생성 웹훅 수신:** [`customer/create` 이벤트](https://help.shopify.com/en/manual/fulfillment/setup/notifications/webhooks)를 수신하도록 웹훅을 설정합니다. 이를 통해 새 고객이 생성될 때 메타필드를 작성할 수 있습니다.
- **기존 고객 백필:** [Admin API](https://shopify.dev/docs/api/admin-graphql) 또는 [Customer API](https://shopify.dev/docs/api/admin-rest/2025-04/resources/customer)를 사용하여 이전에 생성된 고객의 메타필드를 백필합니다.

#### 잠재적 경합 조건 {#potential-race-condition}

Shopify `customers/create` 웹훅은 `braze.external_id` 메타필드가 고객 프로필에 기록되기 전에 실행될 수 있습니다. 이 경우:

1. 메타필드가 누락되면 Braze는 구성된 엔드포인트(4.2단계)를 호출하여 외부 ID를 가져옵니다.
2. 해당 호출도 실패하거나 시간 초과되면 Braze는 Shopify 고객 ID를 외부 ID로 사용하여 임시 고객 프로필을 생성합니다.
3. 메타필드가 존재하는 후속 이벤트(예: `customers/update` 또는 `ecommerce.order_placed` 이벤트에 대한 `orders/create`)에서 Braze는 자동으로 불일치를 감지하고 임시 프로필을 올바른 외부 ID와 병합합니다.

이는 임시 중복 프로필이 발생할 수 있지만 자동으로 수정된다는 것을 의미합니다. 이러한 프로필을 수동으로 병합할 필요는 없습니다.

### 4.2단계: 외부 ID를 검색할 엔드포인트 만들기 {#step-42-create-an-endpoint-to-retrieve-your-external-id}

외부 ID를 검색하기 위해 Braze가 호출할 수 있는 공용 엔드포인트를 만들어야 합니다. 이를 통해 Shopify에서 `braze.external_id` 메타필드를 직접 제공할 수 없는 시나리오에서 Braze가 ID를 가져올 수 있습니다.

#### 엔드포인트 사양 {#endpoint-specifications}

**메서드:** GET

Braze는 다음 매개변수를 엔드포인트로 전송합니다:

| 매개변수 | 필수 | 데이터 유형 | 설명 |
|----------------------|----------|-----------|------------------------------------------------------------------|
| shopify_customer_id  | 예      | 문자열    | Shopify 고객 ID입니다.                                         |
| shopify_storefront   | 예      | 문자열    | 요청에 대한 스토어프론트 이름입니다. 예: `<storefront_name>.myshopify.com` |
| email_address        | 아니요       | 문자열    | 로그인한 사용자의 이메일 주소입니다. <br><br>특정 웹훅 시나리오에서는 이 필드가 누락될 수 있습니다. 엔드포인트 로직에서 null 값을 처리할 수 있어야 합니다(예: 내부 로직에 필요한 경우 shopify_customer_id를 사용하여 이메일을 가져옵니다). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="엔드포인트 사양" }

#### 엔드포인트 예시 {#example-endpoint}

```http
GET https://mystore.com/custom_id?shopify_customer_id=1234&email_address=bob@example.com&shopify_storefront=dev-store.myshopify.com
```

#### 예상 응답 {#expected-response}
Braze는 외부 ID JSON을 반환하는 `200` 상태 코드를 기대합니다:
```json
{
  "external_id": "my_external_id"
}
```

#### 유효성 검사 {#validation}
`shopify_customer_id` 및 `email_address`(있는 경우)가 Shopify의 고객 값과 일치하는지 검증하는 것이 중요합니다. [Shopify Admin API](https://shopify.dev/docs/api/admin-graphql) 또는 [Customer API](https://shopify.dev/docs/api/admin-rest/2025-04/resources/customer)를 사용하여 이러한 매개변수의 유효성을 검사하고 올바른 `braze.external_id` 메타필드를 검색할 수 있습니다.

#### 실패 동작 및 병합 {#failure-behavior-and-merging}
`200` 이외의 상태 코드는 모두 실패로 간주됩니다.

{% multi_lang_include partners/shopify/external_id_merge_implications.md %}

### 4.3단계: 외부 ID 입력 {#step-43-input-your-external-id}

[4단계](#step-4)를 반복하고 Braze 외부 ID 유형으로 커스텀 외부 ID를 선택한 후 엔드포인트 URL을 입력합니다.

#### 고려 사항 {#considerations}

{% multi_lang_include partners/shopify/external_id_generation_notes.md %}

### 4.4단계: Shopify에서 이메일 또는 SMS 옵트인 수집(선택 사항) {#step-44-collect-your-email-or-sms-opt-ins-from-shopify-optional}

Shopify에서 이메일 또는 SMS 마케팅 옵트인을 수집하는 옵션이 있습니다.

이메일 또는 SMS 채널을 사용하는 경우 이메일 및 SMS 마케팅 옵트인 상태를 Braze에 동기화할 수 있습니다. Shopify에서 이메일 마케팅 옵트인을 동기화하면 Braze는 해당 특정 스토어와 연결된 모든 사용자에 대해 이메일 구독 그룹을 자동으로 생성합니다. 이 구독 그룹에 고유한 이름을 지정해야 합니다.

![이메일 또는 SMS 마케팅 옵트인을 수집하는 옵션이 있는 "구독자 수집" 섹션.]({% image_buster /assets/img/shopify/collect_email_subscribers.png %})

{% multi_lang_include partners/shopify/third_party_capture_form_note.md %}

## 5단계: 제품 동기화(선택 사항) {#step-5-sync-products-optional}

Shopify 스토어의 모든 제품을 Braze 카탈로그에 동기화하여 더 깊은 메시징 개인화를 구현할 수 있습니다. 자동 업데이트가 거의 실시간으로 이루어지므로 카탈로그에 최신 제품 세부 정보가 반영됩니다. 자세한 내용은 [Shopify 제품 동기화]({{site.baseurl}}/partners/ecommerce/shopify/shopify_catalogs)를 확인하세요.

![카탈로그 제품 식별자로 "Shopify Variant ID"가 설정된 설정 프로세스의 4단계.]({% image_buster /assets/img/shopify/sync_products_step1.png %}){: style="max-width:80%;"}

## 6단계: 채널 활성화(선택 사항) {#step-6-activate-channels-optional}

설정에서 구성하여 개발자 없이 인앱 메시지를 활성화할 수 있습니다.

![인브라우저 메시징 옵션이 있는 채널 활성화 설정 단계.]({% image_buster /assets/img/shopify/activate_channels_standard.png %})

{% alert note %}
Braze는 인브라우저 메시지를 통해 이메일 주소 및 전화번호와 같은 방문자 정보를 수집합니다. 이 정보는 Shopify로 전송됩니다. 판매자는 이 데이터를 통해 매장 방문자를 인식하고 보다 개인화된 쇼핑 경험을 제공할 수 있습니다. 자세한 내용은 [Visitor API](https://shopify.dev/docs/api/web-pixels-api/emitting-data#visitor-api)를 참조하세요.
{% endalert %}

### 추가 SDK 채널 지원 {#supporting-additional-sdk-channels}

Braze SDK는 Content Cards를 포함한 다양한 메시징 채널을 지원합니다.

#### Content Cards 및 피처 플래그 {#content-cards-and-feature-flags}

Content Cards 또는 피처 플래그를 추가하려면 개발자와 협력하여 필요한 SDK 코드를 `theme.liquid` 파일에 직접 삽입해야 합니다. 자세한 지침은 [Braze SDK 통합]({{site.baseurl}}/developer_guide/sdk_integration)을 참조하세요.

#### 웹 푸시 알림 {#web-push-notifications}

현재 웹 푸시는 Shopify 통합에서 지원되지 않습니다. {% multi_lang_include product_feedback_cta.md context="gap" feature="web push for the Shopify integration" %}

## 7단계: 설정 완료 {#step-7-finish-setup}

1. 설정을 구성한 후 **설정 완료**를 선택합니다.
2. Shopify 테마 설정에서 Braze 앱 임베드를 활성화합니다. **Shopify 열기**를 선택하면 Shopify 계정으로 리디렉션되어 스토어의 테마 설정에서 앱 임베드를 활성화할 수 있습니다.

![Shopify에서 Braze 앱 임베드를 활성화해야 한다는 배너와 Shopify 열기 버튼.]({% image_buster /assets/img/shopify/open_shopify.png %})

{: start="3"}
3. 앱 임베드를 활성화하면 설정이 완료됩니다!
통합 설정, 초기 데이터 동기화 상태 및 활성 Shopify 이벤트를 확인할 수 있는지 확인하세요. <br><br>![통합 설정을 표시하는 Shopify 파트너 페이지.]({% image_buster /assets/img/shopify/install_complete.png %})