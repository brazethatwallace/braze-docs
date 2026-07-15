---
nav_title: Zeotap Symphony
description: "이 참조 문서에서는 ID 확인, 인사이트 및 데이터 보강을 제공하는 차세대 고객 데이터 플랫폼인 Zeotap과 Braze 간의 파트너십에 대해 설명합니다."
page_type: partner
search_tag: Partner
page_order: 2
---

# Zeotap Symphony

Braze와 Zeotap Symphony 통합을 사용하면 실시간 오케스트레이션을 생성하고 이메일 및 푸시 알림 캠페인을 실행할 수 있습니다.

- Zeotap을 통해 이름과 성을 전송하면, 이를 기반으로 사용자가 Braze를 통해 개인화된 이메일을 보낼 수 있습니다.
- Zeotap을 통해 커스텀 이벤트 또는 구매 이벤트를 실시간으로 전송하면, 이를 기반으로 사용자가 Braze 내에서 캠페인 트리거를 생성하여 고객을 타겟팅할 수 있습니다.

{% alert note %}
이메일 마케팅 캠페인을 생성하려면 Zeotap Catalogue에서 `Email Raw`에 매핑하여 원시 이메일을 Zeotap에 온보딩하세요.
{% endalert %}

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
| ----------- | ----------- |
| 클라이언트 이름 | Braze 계정의 클라이언트 이름입니다. Braze 콘솔로 이동하여 확인할 수 있습니다. |
| Braze REST API 키 | `users.track` 권한이 있는 Braze REST API 키입니다. <br><br> Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
| 인스턴스 | Braze 인스턴스는 Braze 온보딩 매니저에게 문의하거나 [API 개요 페이지]({{site.baseurl}}/api/basics#endpoints)에서 확인할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="필수 조건" }

## 통합 {#integration}

이 섹션에서는 Braze와 통합할 수 있는 두 가지 방법에 대한 정보를 제공합니다.

### 방법 1 {#method-1}
이 방법에서는 다음 작업을 수행해야 합니다.
1. 웹사이트 또는 앱에 Braze SDK를 통합합니다.
2. Symphony를 통해 Braze와 Zeotap을 통합합니다.

- `User traits`는 **Data To Send** 탭에서 해당 Braze 필드에 매핑해야 합니다. `Event` 및 `Purchase` 속성을 매핑하면 Braze 내에서 이벤트가 중복됩니다.
- `External ID`를 Braze SDK 설정 시 구성한 `User ID`에 매핑합니다.

통합이 성공적으로 설정되면 Symphony를 통해 Braze로 전송된 커스텀 속성을 기반으로 이메일 및 푸시 알림 캠페인을 생성할 수 있습니다.

### 방법 2 {#method-2}
이 방법에서는 Symphony를 통해 Braze와 Zeotap을 통합할 수 있습니다.

- 이 방법은 인앱 메시징, Content Cards 또는 푸시 알림과 같은 Braze UI 기능을 지원하지 않습니다.
- Zeotap은 Zeotap Catalogue에서 사용 가능한 `hashed email`을 `External ID`에 매핑할 것을 권장합니다.

통합이 성공적으로 설정되면 Symphony를 통해 Braze로 전송된 커스텀 속성을 기반으로 이메일 캠페인만 생성할 수 있습니다.

## Braze로의 데이터 흐름 및 지원되는 식별자 {#data-flow-to-braze-and-supported-identifiers}

데이터는 [`/users/track` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track)를 사용하여 Zeotap에서 Braze로 전달됩니다. 다음은 데이터 흐름을 요약한 것입니다.

1. Zeotap이 사용자 프로필 속성, 커스텀 속성, 커스텀 이벤트 및 구매 필드를 전송합니다.
2. **Data To Send** 탭에서 관련 Zeotap Catalogue 필드를 모두 Braze 필드에 매핑합니다.
3. 그런 다음 데이터가 Braze에 업로드됩니다.

다양한 속성에 대한 자세한 내용은 [Data To Send](#data-to-send-tab) 섹션에서 확인할 수 있습니다.

## 대상 설정 {#destination-setup}

Symphony에서 사용자에 대한 필터를 적용하거나 조건을 추가한 후 **Send to Destinations**에서 Braze로 활성화할 수 있습니다. 새 창이 열리며 대상을 설정할 수 있습니다. **Available Destinations** 목록에서 기존 대상을 사용하거나 새 대상을 생성할 수 있습니다.

### 새 대상 추가 {#add-new-destination}
새 대상을 추가하려면 다음 단계를 수행합니다.
1. **Add New Destination**을 선택합니다.
2. **Braze**를 검색합니다.
3. **Client Name**, **API Key** 및 **Instance**를 추가하고 대상을 저장합니다.

대상이 생성되어 **Available Destinations**에서 사용할 수 있게 됩니다.

### 워크플로 수준 입력 추가 {#add-workflow-level-inputs}
대상을 생성한 후 아래에 설명된 대로 워크플로 수준 입력을 추가해야 합니다.
1. 검색 기능을 사용하여 사용 가능한 대상 목록에서 대상을 선택합니다.
2. **Client Name**, **API Key** 및 **Instance** 필드는 대상 생성 시 입력한 값을 기반으로 자동으로 채워집니다.
3. 이 워크플로 노드에 대해 생성할 **Audience Name**을 입력합니다. 이는 **커스텀 속성**으로 Braze에 전송됩니다.
4. **Data To Send** 탭에서 카탈로그-대상 매핑을 완료합니다. 매핑 수행 방법에 대한 자세한 내용은 아래에서 확인할 수 있습니다.

### Data to send 탭 {#data-to-send-tab}
**Data To Send** 탭에서는 Zeotap Catalogue 필드를 Braze로 전송할 수 있는 Braze 필드에 매핑할 수 있습니다. 매핑은 다음 방법 중 하나로 수행할 수 있습니다.
- **정적 매핑** - Zeotap이 이메일, 전화번호, 이름, 성 등과 같은 관련 Braze 필드에 자동으로 매핑하는 특정 필드가 있습니다.<br>
- **드롭다운 선택** - 드롭다운 메뉴에 제공된 Braze 필드에 Zeotap에서 수집된 관련 필드를 매핑합니다.<br>![Zeotap에서 설정한 다양한 사용자 특성(예: 언어, 구/군/시, 생일 등).]({% image_buster /assets/img/zeotap/zeotap7.png %}){: style="max-width:70%;"}<br>
- **커스텀 데이터 입력** - 관련 Zeotap 필드에 매핑된 커스텀 데이터를 추가하고 Braze로 전송합니다.<br>![Zeotap에서 "loyalty_points"를 사용자 특성으로 선택하는 화면.]({% image_buster /assets/img/zeotap/zeotap8.png %}){: style="max-width:70%;"}

## 지원되는 속성 {#supported-attributes}
이 섹션에서 모든 Braze 필드에 대한 자세한 내용을 확인할 수 있습니다.

| Braze 필드 | 매핑 유형 | 설명 |
| --- | --- | --- |
| External ID | 드롭다운 선택 | Braze에서 기기 및 플랫폼 전반에 걸쳐 사용자를 추적하기 위해 정의한 영구적인 `User ID`입니다. `User ID`를 `External ID`에 매핑하는 것을 권장합니다. 그렇지 않으면 Zeotap이 이메일을 사용자 별칭으로 전송할 수 있습니다.<br><br>Zeotap은 Zeotap Catalogue에서 사용 가능한 `hashed email`을 `External ID`에 매핑할 것을 권장합니다. |
| Email | 정적 매핑 | Zeotap Catalogue의 `Email Raw`에 매핑됩니다. |
| Phone | 정적 매핑 | Zeotap Catalogue의 `Mobile Raw`에 매핑됩니다.<br><br>• Braze는 `E.164` 형식의 전화번호를 허용합니다. Zeotap은 변환을 수행하지 않습니다. 따라서 규정된 형식으로 전화번호를 수집해야 합니다. 자세한 내용은 [사용자 전화번호]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/user_phone_numbers)를 참조하세요. |
| First Name | 정적 매핑 | Zeotap Catalogue의 `First Name`에 매핑됩니다. |
| Last Name | 정적 매핑 | Zeotap Catalogue의 `Last Name`에 매핑됩니다. |
| Gender | 정적 매핑 | Zeotap Catalogue의 `Gender`에 매핑됩니다. |
| Custom Event Name | 정적 매핑 | Zeotap Catalogue의 `Event Name`에 매핑됩니다.<br><br>Braze에서 커스텀 이벤트를 캡처하려면 Custom Event Name과 Custom Event Timestamp를 모두 매핑해야 합니다. 둘 중 하나라도 매핑되지 않으면 커스텀 이벤트를 처리할 수 없습니다. 자세한 내용은 [이벤트 오브젝트]({{site.baseurl}}/api/objects_filters/event_object#what-is-the-event-object)를 참조하세요. |
| Custom Event Timestamp | 정적 매핑 | Zeotap Catalogue의 `Event Timestamp`에 매핑됩니다.<br><br>Braze에서 커스텀 이벤트를 캡처하려면 Custom Event Name과 Custom Event Timestamp를 모두 매핑해야 합니다. 둘 중 하나라도 매핑되지 않으면 커스텀 이벤트를 처리할 수 없습니다. 자세한 내용은 [이벤트 오브젝트]({{site.baseurl}}/api/objects_filters/event_object#what-is-the-event-object)를 참조하세요. |
| Email Subscribe | 드롭다운 선택 | `Email Marketing Preference` 필드를 온보딩하고 매핑합니다.<br><br>Zeotap은 다음 세 가지 값을 전송합니다.<br>• `opted_in` - 사용자가 이메일 마케팅 수신에 명시적으로 등록했음을 나타냅니다.<br>• `unsubscribed` - 사용자가 이메일 메시지 수신을 명시적으로 거부했음을 나타냅니다.<br>• `subscribed` - 사용자가 수신 동의도 거부도 하지 않았음을 나타냅니다. |
| Push Subscribe | 드롭다운 선택 | `Push Marketing Preference` 필드를 온보딩하고 매핑합니다.<br><br>Zeotap은 다음 세 가지 값을 전송합니다.<br>• `opted_in` - 사용자가 푸시 마케팅 수신에 명시적으로 등록했음을 나타냅니다.<br>• `unsubscribed` - 사용자가 푸시 메시지 수신을 명시적으로 거부했음을 나타냅니다.<br>• `subscribed` - 사용자가 수신 동의도 거부도 하지 않았음을 나타냅니다. |
| Email Open Tracking Enable | 드롭다운 선택 | 관련 `Marketing Preference` 필드를 매핑합니다.<br><br>true로 설정하면 이 사용자에게 향후 전송되는 모든 이메일에 열람 추적 픽셀이 추가됩니다. |
| Email Click Tracking Enable | 드롭다운 선택 | 관련 `Marketing Preference` 필드를 매핑합니다.<br><br>true로 설정하면 이 사용자에게 향후 전송되는 모든 이메일의 모든 링크에 대해 클릭 추적이 활성화됩니다. |
| Product ID | 드롭다운 선택 | • 구매 동작의 식별자 `(Product Name/Product Category)`입니다. 자세한 내용은 [구매 오브젝트]({{site.baseurl}}/api/objects_filters/purchase_object)를 참조하세요.<br>• 관련 속성을 Zeotap Catalogue에 온보딩하고 매핑합니다.<br><br>Braze에서 구매 이벤트를 캡처하려면 `Product ID`, `Currency`, `Price`를 반드시 매핑해야 합니다. 세 가지 중 하나라도 누락되면 구매 이벤트가 처리되지 않습니다. 자세한 내용은 [구매 오브젝트]({{site.baseurl}}/api/objects_filters/purchase_object#purchase-object)를 참조하세요. |
| Currency | 드롭다운 선택 | • 구매 동작의 통화 속성입니다.<br>• 지원되는 형식은 `ISO 4217 Alphabetic Currency Code`입니다.<br>• 올바른 형식의 통화 데이터를 Zeotap Catalogue에 온보딩하고 매핑합니다.<br><br>Braze에서 구매 이벤트를 캡처하려면 `Product ID`, `Currency`, `Price`를 반드시 매핑해야 합니다. 세 가지 중 하나라도 누락되면 구매 이벤트가 처리되지 않습니다. |
| Price | 드롭다운 선택 | • 구매 동작의 가격 속성입니다.<br>• 관련 속성을 Zeotap Catalogue에 온보딩하고 매핑합니다.<br><br>Braze에서 구매 이벤트를 캡처하려면 `Product ID`, `Currency`, `Price`를 반드시 매핑해야 합니다. 세 가지 중 하나라도 누락되면 구매 이벤트가 처리되지 않습니다. |
| Quantity | 드롭다운 선택 | • 구매 동작의 수량 속성입니다.<br>• 관련 속성을 Zeotap Catalogue에 온보딩하고 매핑합니다. |
| Country | 드롭다운 선택 | 온보딩 중인 `Country` Catalogue 필드에 매핑합니다. |
| City | 드롭다운 선택 | 온보딩 중인 `City` Catalogue 필드에 매핑합니다. |
| Language | 드롭다운 선택 | • 허용되는 형식은 `ISO-639-1` 표준입니다(예: en).<br>• 올바른 형식의 언어를 온보딩하고 매핑합니다. |
| Date of Birth | 드롭다운 선택 | 온보딩 중인 `Date of Birth` 필드에 매핑합니다. |
| Custom Attribute | 커스텀 데이터 입력 | 사용자 속성을 커스텀 데이터 입력에 매핑하면 Braze로 전송됩니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="지원되는 속성" }

## Braze 콘솔에서 데이터 보기 {#viewing-data-on-braze-console}

관련 속성을 매핑하여 워크플로에서 전송 및 게시한 후, 정의된 기준에 따라 이벤트가 Braze로 흐르기 시작합니다. Braze 콘솔에서 이메일 ID 또는 외부 ID로 검색할 수 있습니다.

![수신된 Zeotap 속성 및 이벤트를 보여주는 Braze 사용자 프로필 화면.]({% image_buster /assets/img/zeotap/zeotap6.jpg %})

Braze 내 사용자 대시보드의 다양한 섹션에 여러 속성이 표시됩니다.
- **Profile** 탭에는 사용자 속성이 포함되어 있습니다.
- **Custom Attributes** 탭에는 사용자가 정의한 커스텀 속성이 포함되어 있습니다.
- **Custom Events** 탭에는 사용자가 정의한 커스텀 이벤트가 포함되어 있습니다.
- **Purchases** 탭에는 일정 기간 동안 사용자가 수행한 구매가 포함되어 있습니다.

## 캠페인 생성 {#campaign-creation}

사용자는 Braze 내에서 캠페인을 생성하고 실시간으로 또는 예약된 시간에 따라 사용자를 활성화할 수 있습니다. 사용자가 수행한 동작(커스텀 이벤트, 구매) 또는 사용자 속성을 기반으로 캠페인을 트리거할 수 있습니다.