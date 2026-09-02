---
nav_title: Dynamics 365 Customer Insights
article_title: Dynamics 365 Customer Insights
description: "이 참조 문서에서는 선도적인 엔터프라이즈 고객 데이터 플랫폼인 Dynamics 365 Customer Insights와 Braze 간의 파트너십을 설명합니다. 이 통합을 통해 고객 세그먼트를 Braze로 내보내 Campaigns 또는 Canvases에서 활용할 수 있습니다."
alias: /partners/dynamics_365_customer_insights/
page_type: partner
search_tag: Partner
---

# Dynamics 365 Customer Insights

> [Dynamics 365 Customer Insights](https://dynamics.microsoft.com/en-gb/ai/customer-insights/)는 고객에 대한 360도 뷰를 통해 개인화된 고객 경험을 제공하는 선도적인 엔터프라이즈 고객 데이터 플랫폼입니다.

_이 통합은 Dynamics 365 Customer Insights에서 유지 관리합니다._

## 통합 정보 {#about-the-integration}

Braze와 Dynamics 365 Customer Insights 통합을 사용하면 고객 세그먼트를 Braze로 내보내 Campaigns 또는 Canvases에서 활용할 수 있습니다.

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Dynamics 365 Customer Insights 계정 | 이 파트너십을 활용하려면 [Dynamics 365 Customer Insights](https://dynamics.microsoft.com/en-gb/ai/customer-insights/) 계정이 필요합니다. Dynamics 365 Customer Insights 계정 내에서 연결을 보고 편집하려면 관리자 권한이 필요하며, 이를 통해 필요한 플러그인에 접근할 수 있습니다. |
| Braze REST API 키 | `users.track` 및 `users.export.segment` 권한이 있는 Braze REST API 키가 필요합니다. <br><br> Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
| 일치하는 프로필 식별자 | 내보낸 세그먼트의 통합 고객 프로필에는 이메일 주소를 나타내는 필드와 Braze `external_id`가 포함되어야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 통합 {#integration}

### 1단계: Braze 연결 설정 {#step-1-set-up-braze-connection}

Customer Insights에서 **Admin > Connections**로 이동합니다. 그런 다음 **Add connections**를 선택하고 **Braze**를 선택하여 연결을 구성합니다.

1. **Display name** 필드에 알아보기 쉬운 연결 이름을 입력합니다.
2. 이 연결을 사용할 수 있는 사용자를 선택합니다. 이 필드를 비워 두면 기본값은 관리자입니다. 자세한 내용은 [기여자가 내보내기에 연결을 사용할 수 있도록 허용](https://docs.microsoft.com/en-us/dynamics365/customer-insights/connections#allow-contributors-to-use-a-connection-for-exports)을 참조하세요.
3. Braze API 키와 REST 엔드포인트를 `rest.iad-03.braze.com` 형식으로 입력합니다.
4. **I agree**를 선택하여 데이터 및 개인정보 보호 규정 준수를 확인합니다.
5. **Connect**를 선택하여 Braze에 대한 연결을 초기화합니다.
6. **Add yourself as export user**를 선택하고 Customer Insights 자격 증명을 입력합니다.
7. **Save**를 선택하여 연결을 완료합니다.

### 2단계: Braze 세그먼트 생성 {#step-2-create-a-braze-segment}

1. Braze에서 **Audience** > **Segments**로 이동합니다.
2. Dynamics 365 Customer Insights를 통해 Microsoft가 업데이트할 사용자의 세그먼트를 생성합니다.
3. 해당 세그먼트의 **API 식별자**를 기록합니다.

### 3단계: 내보내기 구성 {#step-3-configure-an-export}

이 유형의 연결에 대한 접근 권한이 있는 경우 이 내보내기를 구성할 수 있습니다. 자세한 내용은 [내보내기 개요](https://docs.microsoft.com/en-us/dynamics365/customer-insights/export-destinations#set-up-a-new-export)를 참조하세요.

1. Customer Insights에서 **Data > Exports**로 이동합니다. 새 내보내기를 생성하려면 **Add destination**을 선택합니다.
2. **Connection for export** 필드에서 Braze 섹션에 대한 연결을 선택합니다. 이 섹션 이름이 보이지 않으면 사용 가능한 이 유형의 연결이 없는 것입니다.
3. Braze에서 해당 세그먼트의 세그먼트 API 식별자를 입력합니다.
4. **Data matching** 섹션의 **Email** 필드에서 고객의 이메일 주소를 나타내는 필드를 선택합니다. 그런 다음 **Braze Customer ID** 필드에서 고객의 Braze ID를 나타내는 필드를 선택합니다. 데이터 매칭을 위한 추가 선택 사항 필드를 선택할 수도 있습니다.
  a. Braze의 `external_id`를 Customer Insights의 Braze 고객 ID 필드에 매핑하면 내보내기 시 Braze의 기존 레코드가 업데이트됩니다.
  b. Braze 레코드의 `external_id`를 나타내지 않는 다른 ID 필드 또는 비어 있는 필드를 매핑하면 내보내기 시 Braze에 새 레코드가 생성됩니다.
5. 마지막으로 내보낼 세그먼트를 선택하고 **Save**를 선택합니다.

내보내기를 저장해도 즉시 내보내기가 실행되지는 않습니다. 이 내보내기는 [스케줄된 새로고침](https://docs.microsoft.com/en-us/dynamics365/customer-insights/system#schedule-tab)마다 실행됩니다. [온디맨드로 데이터를 내보내기](https://docs.microsoft.com/en-us/dynamics365/customer-insights/export-destinations#run-exports-on-demand)할 수도 있습니다.


### 이 통합 사용하기 {#using-this-integration}

세그먼트가 Braze로 성공적으로 내보내지면 고객 프로필에서 커스텀 속성으로 확인할 수 있습니다. 커스텀 속성은 내보내기 연결을 구성할 때 입력한 Braze 세그먼트 API 식별자로 이름이 지정됩니다. 예: `"Segment_API_Identifier": "0000-0000-0000"`

Braze에서 이러한 사용자의 세그먼트를 생성하려면 **Segments**로 이동하여 새 세그먼트를 생성하고 필터로 **커스텀 속성**를 선택합니다. 여기에서 Dynamics 365와 동기화된 커스텀 속성을 선택할 수 있습니다. 세그먼트가 생성되면 Campaign 또는 Canvas를 생성할 때 오디언스 필터로 선택할 수 있습니다.

{% alert note %}
이 통합에 대한 자세한 내용은 Microsoft의 Braze [통합 문서](https://docs.microsoft.com/en-us/dynamics365/customer-insights/export-braze)를 참조하세요.
{% endalert %}