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

Braze와 Shopify의 통합은 고객 참여를 강화하고 개인화된 마케팅 활동을 추진하려는 이커머스 비즈니스에 강력한 솔루션을 제공합니다. [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/)를 사용하면 데이터를 Shopify에 연결하여 내부 보고를 강화하고 구매에 대한 라스트 터치 기여도를 더 잘 추적할 수 있습니다.

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Currents | 데이터를 Shopify로 내보내려면 계정에 [Braze 커런츠]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents)가 설정되어 있어야 합니다. |
| Shopify 스토어 | [Braze와 최소 하나의 Shopify 스토어를 설정]({{site.baseurl}}/shopify_standard_integration/)했는지 확인하세요. |
| Shopify 스토어 소유자 또는 직원 권한 | {::nomarkdown}<ul><li>모든 <b>General</b> 및 <b>Online Store</b> 설정에 대한 접근 권한.</li><li> 추가 관리자 권한:</li><ul><li>Orders: View</li><li>Customer: ReadWrite</li><li>View Customer Events (Web Pixels)</li><li>Manage Settings</li><li>View Apps Developed by Staff/Collaborators</li><li>Manage/Install Apps and Channels</li><li>Manage/Add Custom Pixels</li></ul></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 통합 {#integration}

### 1단계: Shopify 스토어 설정 {#step-1-set-up-your-shopify-store}

아직 설정하지 않았다면 [Shopify 표준 통합 설정]({{site.baseurl}}/shopify_standard_integration/) 단계를 따라 Braze와 최소 하나의 Shopify 스토어를 설정하세요.

### 2단계: Braze Current 생성 {#step-2-create-braze-current}

1. Braze에서 **Partner Integrations** > **Currents** > **+ Create New Current** > **Shopify Export**로 이동합니다.
2. 통합 이름과 연락처 이메일을 입력합니다.
3. **Credentials** 섹션에서 [1단계](#step-1-set-up-your-shopify-store)에서 설정한 Shopify 스토어를 선택합니다.
4. 추적하려는 이벤트를 선택합니다. 사용 가능한 이벤트 목록이 제공됩니다.
5. **Launch Current**을 선택합니다.

![Braze Shopify Currents 페이지. 이 페이지에는 통합 이름, 연락처 이메일 및 Shopify 스토어 필드가 포함되어 있습니다.]({% image_buster /assets/img/shopify/shopify_currents.png %})