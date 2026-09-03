---
nav_title: Sendbird
article_title: Sendbird
description: "이 참조 문서에서는 사용자가 Sendbird 플랫폼에서 인앱 알림을 받을 수 있도록 하는 선도적인 인앱 메시징 솔루션인 Braze와 Sendbird 간의 파트너십에 대해 설명합니다."
alias: /partners/sendbird/
page_type: partner
search_tag: Partner

---

# Sendbird

> [Sendbird](https://sendbird.com/) Notifications는 마케터와 제품 매니저에게 지속적이고 인터랙티브한 단방향 메시지를 통해 인앱에서 고객과 소통할 수 있는 강력한 새 채널을 제공합니다. 이러한 메시지는 모든 커뮤니케이션에 사용할 수 있으며, 가장 일반적으로 프로모션 및 트랜잭션 목적으로 사용됩니다.

_이 통합은 Sendbird에서 유지 관리합니다._

## 통합 정보 {#about-the-integration}

Braze와 Sendbird 통합을 통해 회사 사용자는 다음을 수행할 수 있습니다:
{% multi_lang_include partners/instant_chat/sendbird_integration_bullets.md %}

Braze와 Sendbird Notifications의 결합된 기능을 활용하면, 기업은 효과적인 인앱 알림 전략을 통해 고객 참여를 높이고 더 높은 전환율을 달성할 수 있습니다.

## 사전 요구 사항 {#prerequisites}

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Sendbird 계정 | 이 파트너십을 활용하려면 Sendbird 계정이 필요합니다. |
| Sendbird UIKit | [iOS](https://sendbird.com/docs/notifications/v1/uikit/ios/install-uikit) 또는 [Android](https://sendbird.com/docs/notifications/v1/uikit/android/install-uikit) 앱에 Sendbird UIKit이 설치되어 있어야 합니다. |
| Braze REST API 키 | `users.track` 권한이 있는 Braze REST API 키. <br><br> 이 키는 Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
| Braze REST 엔드포인트 | [REST 엔드포인트 URL]({{site.baseurl}}/developer_guide/rest_api/basics#endpoints). 엔드포인트는 인스턴스의 Braze URL에 따라 달라집니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="사전 요구 사항" }

## 사용 사례 {#use-cases}

![마케팅 및 트랜잭션 메시징을 위한 Braze와 Sendbird Notifications 통합 사용 사례를 요약한 다이어그램.]({% image_buster /assets/img/sendbird/use-cases.png %})

Braze와 Sendbird Notifications 통합은 고객 참여를 높이고 뛰어난 사용자 경험을 제공하기 위한 다양한 사용 사례를 지원합니다:

- **마케팅**: 검색 기록이나 과거 구매 내역을 기반으로 한 독점 할인 등 사용자의 선호도에 맞춘 개인화된 프로모션과 추천을 통해 타겟 캠페인을 강화할 수 있습니다.
- **트랜잭션**: 주문, 배송, 청구 및 결제에 대한 실시간 업데이트를 통해 고객 커뮤니케이션을 향상시킬 수 있으며, 주문 상태, 배송 세부 정보, 예상 배송 시간에 대한 알림을 포함합니다.

## 통합 {#integration}

### 1단계: 알림 템플릿 만들기 {#step-1-create-a-notification-template}

[Sendbird 템플릿](https://sendbird.com/docs/notifications/v1/templates)을 사용하면 각 채널에 대해 여러 템플릿을 만들고 활용하여 개인화된 인앱 알림을 보낼 수 있습니다. 템플릿은 코드를 작성하지 않고도 Sendbird 대시보드에서 생성하고 커스터마이즈할 수 있습니다.

![알림 템플릿을 만들기 위한 Sendbird 대시보드 템플릿 편집기.]({% image_buster /assets/img/sendbird/sendbird-dashboard-template.png %})

### 2단계: Sendbird 대시보드에서 Braze 통합 설정하기 {#step-2-set-up-the-braze-integration-on-sendbird-dashboard}

**Sendbird 대시보드**에서 애플리케이션을 선택하고 **Notifications > Integrations**로 이동한 다음, **Braze** 섹션 아래의 **Add**를 클릭합니다. 여기에서 Braze REST API 키와 Braze REST 엔드포인트가 필요합니다.

모든 필드를 입력한 후 **Save**를 클릭하여 통합을 완료하고 통합 엔드포인트 및 API 토큰에 액세스합니다.

### 3단계: Sendbird Notification Builder 설치하기 {#step-3-install-sendbird-notification-builder}

다음으로 [Sendbird Notification Builder](https://chrome.google.com/webstore/detail/apbhgfffamdcdogeijjcnjbmghahoaji)를 설치해야 합니다. 이 Google Chrome 확장 프로그램을 사용하면 Braze 대시보드에서 Sendbird를 통해 커스터마이즈된 알림을 보낼 수 있습니다.

![Braze 대시보드의 Sendbird Notification Builder Chrome 확장 프로그램 패널.]({% image_buster /assets/img/sendbird/sendbird-notification-builder.png %})

#### 확장 프로그램에 Sendbird 자격 증명 추가하기 {#add-sendbird-credentials-to-the-extension}

확장 프로그램이 설치되면 브라우저 툴바에서 Sendbird 아이콘을 클릭하고 **Settings**를 선택합니다. 여기에서 **Sendbird Notification Builder**에 있는 앱 ID와 API 토큰을 입력합니다.

### 4단계: Sendbird 사용자 ID를 Braze 사용자 ID에 매핑하기 {#step-4-map-sendbird-user-id-to-braze-user-id}

통합을 사용하려면 Sendbird 사용자 ID를 Braze 고객 프로필에 [커스텀 속성]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes)으로 추가해야 합니다. [사용자 가져오기]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import#csv) 페이지에서 CSV 파일을 통해 고객 프로필을 업로드하고 업데이트할 수 있습니다. 또는 Braze 사용자 ID를 Sendbird 사용자 ID로 사용할 수도 있습니다.

### 5단계: 웹훅 템플릿 설정하기 {#step-5-set-up-your-webhook-template}

Braze에서 **템플릿 및 미디어**로 이동한 다음 **웹훅 템플릿**에서 **Sendbird Webhook Template**을 선택합니다. 이 템플릿은 Sendbird Notification Builder 확장 프로그램을 설치한 경우에만 사용할 수 있습니다.

{% raw %}
1. 템플릿 이름을 입력하고 필요에 따라 팀과 태그를 추가합니다.
2. Sendbird 대시보드에서 실시간 또는 배치 엔드포인트를 복사하여 **Webhook URL**에 붙여넣습니다.
3. **Receiver** 필드에서 <i class="fas fa-plus" aria-label="추가"></i> 아이콘을 클릭하고 Sendbird 사용자 ID에 매핑된 사용자 속성을 삽입합니다.
    - Sendbird 사용자 ID로 커스텀 속성 `sendbird_id`를 사용하는 경우 `{{ '{{' }}custom_attribute.${sendbird_id}}}`를 입력합니다.
    - Braze 사용자 ID를 Sendbird 사용자 ID로 사용하는 경우 `{{ '{{' }}${user_id}}}`를 입력합니다.
4. **Settings** 탭에서 `SENDBIRD_API_TOKEN`을 Sendbird 대시보드의 알림 API 토큰으로 교체합니다.
5. 템플릿을 저장합니다.
{% endraw %}

## 이 통합 사용하기 {#using-this-integration}

### Campaigns

1. Braze 대시보드의 **Campaigns** 페이지에서 **Create Campaign** > **Webhook**을 클릭합니다.
2. 이 섹션에서 생성한 웹훅 템플릿을 선택합니다. Campaigns에는 배치 엔드포인트를 사용하는 것을 강력히 권장합니다.
3. **Compose** 탭에서 변수를 편집하여 템플릿을 커스터마이즈합니다.

### Canvas

1. 새 Canvas 또는 기존 Canvas에서 **메시지** 컴포넌트를 추가합니다.
2. 컴포넌트를 열고 **메시징 채널**에서 **Webhook**을 선택합니다.
3. 이 섹션에서 생성한 웹훅 템플릿을 선택합니다. Canvases에는 실시간 엔드포인트를 사용하는 것을 강력히 권장합니다.
4. **Compose** 탭에서 변수를 편집하여 템플릿을 커스터마이즈합니다.

## 커스터마이제이션 {#customization}

### 전달 및 열람 상태 추적 {#track-delivery-and-open-status}

알림의 전달 및 열람 상태 이벤트를 Campaign의 전환 지표와 통합하려면 Braze 대시보드에서 커스텀 이벤트를 추가하세요.

1. Braze 대시보드에서 **설정 > 설정 관리 > 커스텀 이벤트**로 이동한 다음 **+ 커스텀 이벤트 추가**를 클릭합니다.
2. 커스텀 이벤트를 생성한 후 **속성정보 관리**를 클릭하고, "status"라는 이름의 속성정보를 추가한 다음 속성정보 유형으로 "String"을 선택합니다.
3. Campaigns 또는 Canvases에서 알림을 작성할 때 **Event Name** 필드에 커스텀 이벤트의 이름을 입력합니다.

이 커스텀 이벤트는 각 알림에 대해 두 번 트리거됩니다. 메시지가 전송될 때와 사용자가 메시지를 열람할 때 각각 트리거됩니다.
- 메시지가 전송되면 `SENT` 상태로 커스텀 이벤트가 트리거됩니다.
- 메시지가 읽히면 `READ` 상태로 커스텀 이벤트가 트리거됩니다.