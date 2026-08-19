---
nav_title: Shopify for Currents
article_title: Shopify for Currents
description: "이 참조 문서에서는 Braze Currents와 Shopify 간의 파트너십에 대해 설명합니다. Shopify는 글로벌 커머스 기업으로, Braze와 Shopify 스토어를 원활하게 연결하여 내부 보고를 강화하고 구매에 대한 라스트 터치 기여도를 더 잘 추적할 수 있도록 합니다."
page_type: partner
tool: Currents
search_tag: Partner
alias: /shopify_for_currents/
hidden: true
noindex: true

---

# Shopify for Currents

> [Shopify](https://www.shopify.com/)는 모든 규모의 비즈니스를 시작, 성장, 마케팅 및 관리할 수 있는 신뢰할 수 있는 도구를 제공하는 선도적인 글로벌 커머스 기업입니다. Shopify의 플랫폼과 서비스는 안정성을 위해 설계되었으며, 전 세계 소비자에게 더 나은 쇼핑 경험을 제공합니다.

{% alert important %}
이 통합은 현재 베타 버전입니다. 자세한 내용은 Braze 고객 성공 매니저에게 문의하세요.
{% endalert %}

Braze와 Shopify의 통합은 고객 참여를 강화하고 개인화된 마케팅 활동을 추진하려는 이커머스 비즈니스에 강력한 솔루션을 제공합니다. [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents)를 사용하면 데이터를 Shopify에 연결하여 내부 보고를 강화하고 구매에 대한 라스트 터치 기여도를 더 잘 추적할 수 있습니다.

## 전제 조건 {#prerequisites}

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Currents | Shopify로 데이터를 내보내려면 계정에 [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents#access-currents)가 설정되어 있어야 합니다. |
| Shopify 스토어 | 이미 [Braze와 하나 이상의 Shopify 스토어를 설정]({{site.baseurl}}/shopify_standard_integration)했는지 확인하세요. |
| Shopify 스토어 소유자 또는 직원 권한 | {::nomarkdown}<ul><li>모든 <b>General</b> 및 <b>Online Store</b> 설정에 대한 액세스 권한.</li><li> 추가 관리자 권한:</li><ul><li>Orders: View</li><li>Customer: ReadWrite</li><li>View Customer Events (Web Pixels)</li><li>설정 관리</li><li>View Apps Developed by Staff/Collaborators</li><li>Manage/Install Apps and Channels</li><li>Manage/Add Custom Pixels</li></ul></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 통합 {#integration}

### 1단계: Shopify 스토어 설정 {#step-1-set-up-your-shopify-store}

아직 설정하지 않았다면, [Shopify 표준 통합 설정]({{site.baseurl}}/shopify_standard_integration) 단계를 따라 Braze에 최소 하나의 Shopify 스토어를 설정합니다.

### 2단계: Braze Currents 생성 {#step-2-create-braze-current}

1. Braze에서 **파트너 통합** > **Currents** > **+ Create New Current** > **Shopify Export**로 이동합니다.
2. 통합 이름과 연락처 이메일을 입력합니다.
3. **자격 증명** 섹션에서 [1단계](#step-1-set-up-your-shopify-store)에서 설정한 Shopify 스토어를 선택합니다.
4. 추적할 이벤트를 선택합니다. 사용 가능한 이벤트 목록이 제공됩니다.
5. **Launch Current**을 선택합니다.

![Braze Shopify Currents 페이지. 이 페이지에는 통합 이름, 연락처 이메일, Shopify 스토어 필드가 포함되어 있습니다.]({% image_buster /assets/img/shopify/shopify_currents.png %})

## 고객 프로필 동기화 {#user-profile-sync}

이벤트 데이터 외에도 Shopify 통합은 Braze에서 Shopify 스토어로 고객 프로필 업데이트를 동기화할 수 있습니다. Braze에서 사용자의 프로필이 업데이트되면 Currents가 스토어에서 일치하는 고객을 생성하거나 업데이트합니다.

{% alert note %}
고객 프로필 동기화는 [테스트 Currents 커넥터]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents#testing-currents-connectors)에서는 지원되지 않습니다. 다른 이벤트 내보내기에는 영향이 없습니다. 고객 프로필을 동기화하려면 [표준 Shopify Currents 커넥터](#step-2-create-braze-current)를 사용하세요.
{% endalert %}

### 사용자 매칭 {#user-matching}

Braze는 Braze `user_id`를 Shopify [커스텀 식별자](https://shopify.dev/docs/api/admin-graphql/latest/mutations/customerSet)(`customId`)로 사용하여 Shopify 고객을 매칭합니다. 이때 네임스페이스는 `braze`이고 키는 `user_id`입니다. 해당 식별자를 가진 고객이 스토어에 존재하지 않으면 새 고객이 생성됩니다. 익명 사용자는 동기화되지 않습니다.

### 필드 매핑 {#field-mapping}

다음 Braze 프로필 필드가 Shopify로 동기화됩니다.

| Braze 필드 | Shopify 고객 필드 | 참고 |
| ----------- | ---------------------- | ----- |
| `first_name` | `firstName` | 있는 그대로 매핑됩니다. 프로필 업데이트에 존재하는 경우에만 전송됩니다. |
| `last_name` | `lastName` | 있는 그대로 매핑됩니다. 프로필 업데이트에 존재하는 경우에만 전송됩니다. |
| `email_address` | `email` | 전송 전에 공백이 제거되고 소문자로 변환됩니다. |
| `phone_number` | `phone` | [E.164](https://en.wikipedia.org/wiki/E.164) 형식으로 전송됩니다. |
| `language` | `locale` | Shopify에서 지원하는 로케일로 변환됩니다. 포르투갈어와 중국어는 사용자의 국가를 기반으로 지역 변형(예: `pt-BR`)이 할당됩니다. 사용자의 언어가 Shopify에서 지원되지 않는 경우 이 필드는 생략됩니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

프로필 업데이트에 포함된 필드만 전송됩니다. 업데이트에서 생략된 필드는 Shopify에서 변경되지 않으며, 동기화 시 Shopify 고객의 필드가 삭제되거나 초기화되는 일은 없습니다.

### 동기화되지 않는 필드 {#fields-that-are-not-synced}

현재 이 통합은 Shopify 메타필드를 기록하지 않으므로, 메타필드가 필요한 프로필 필드는 동기화되지 않습니다. 특히 커스텀 속성은 Shopify로 전송되지 않습니다. 전송되지 않는 다른 필드로는 `external_user_id`, `gender`, `dob`(생년월일), `timezone`, `home_city`, `country`, `archived`가 있습니다.

Braze는 스토어에 `braze` 네임스페이스 아래에 메타필드 정의를 생성할 수 있습니다(예: `braze.gender`). 이러한 정의는 향후 사용을 위해 예약되어 있으며, 현재 Braze는 해당 정의에 값을 기록하지 않습니다. 예외는 `braze.user_id`로, 고객을 매칭하는 데 사용되는 식별자를 저장합니다.