---
nav_title: "간단한 설문조사"
article_title: 간단한 설문조사 인앱 메시지
page_order: 6
page_type: reference
description: "이 참조 문서에서는 인앱 메시지 설문조사를 사용하여 사용자 속성, 인사이트 및 선호도를 수집하고 Campaign 전략을 강화하는 방법을 다룹니다."
channel:
  - in-app messages
tool:
  - Templates
---

# 간단한 설문조사 {#simple-survey}

> **간단한 설문조사** 인앱 메시지 템플릿을 사용하여 사용자 속성, 인사이트 및 선호도를 수집하고 Campaign 전략을 강화하세요.

이 메시지 유형은 [기존 에디터]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional)에서 사용할 수 있습니다.

일반적인 설문조사 사용 사례로는 사용자에게 앱을 어떻게 사용하고 싶은지 묻기, 개인 선호도에 대해 자세히 알아보기, 특정 기능에 대한 만족도를 묻기 등이 있습니다.

![세 가지 간단한 설문조사 메시지: 알림 환경설정, 식단 선호도, 고객 만족도 설문조사. 설문조사에서 선택한 옵션은 해당 사용자에 대해 기록될 커스텀 속성에 해당합니다.]({% image_buster /assets/img/iam/iam-survey.png %})

## SDK 요구 사항 {#supported-sdk-versions}

이 인앱 메시지는 [Flex CSS](https://caniuse.com/flexbox)를 지원하는 기기에만 전달되며, 최소 다음 [SDK 버전]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/new_features#filtering-by-most-recent-app-versions) 이상이어야 합니다.

{% sdk_min_versions ios:3.23.0 android:8.0.0 web:2.5.0 %}

{% alert note %}
웹 SDK를 통해 HTML 인앱 메시지를 활성화하려면 Braze에 `allowUserSuppliedJavascript` 초기화 옵션을 제공해야 합니다.
{% endalert %}

## 설문조사 만들기 {#create}

[인앱 메시지]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional)를 만들 때 **메시지 유형**으로 **간단한 설문조사**를 선택합니다.

이 설문조사 템플릿은 모바일 앱과 웹 브라우저 모두에서 지원됩니다. SDK가 이 기능에 필요한 [최소 SDK 버전](#supported-sdk-versions)인지 확인하세요.

### 1단계: 설문조사 질문 추가 {#step-1-add-your-survey-question}

설문조사 작성을 시작하려면 설문조사 **헤더** 필드에 질문을 추가합니다. 원하는 경우 설문조사 질문 아래에 표시될 선택적 **본문** 메시지를 추가할 수 있습니다.

![간단한 설문조사 에디터의 작성 탭으로, 헤더, 선택적 본문 및 선택적 도움말 텍스트 필드가 있습니다.]({% image_buster /assets/img/iam/iam-survey2.png %}){: style="max-width:90%"}

{% alert tip %}
이 필드에는 Liquid과 이모지를 모두 사용할 수 있으니 마음껏 활용하세요!
{% endalert %}

### 2단계: 선택지 구성 {#single-multiple-choice}

설문조사에 최대 12개의 선택지를 추가할 수 있습니다.

**단일 선택** 또는 **다중 선택**을 선택합니다. 두 옵션 사이를 전환하면 사용자가 몇 개의 선택지를 선택할 수 있는지 알려주는 **도움말 텍스트**가 자동으로 업데이트됩니다.

그런 다음 [커스텀 속성을 수집](#custom-attributes)할지 또는 [응답만 기록](#no-attributes)할지 결정합니다.

![제출 시 속성 기록이 선택된 선택지 드롭다운.]({% image_buster /assets/img/iam/collect-attributes.png %}){: style="max-width:60%"}

#### 커스텀 속성 수집 {#custom-attributes}

**제출 시 속성 기록**을 선택하여 사용자의 제출 내용을 기반으로 속성을 수집합니다. 이 옵션을 사용하여 새로운 Segment와 리타겟팅 Campaign을 만들 수 있습니다. 예를 들어, [만족도 설문조사](#user-satisfaction)에서 만족하지 않은 모든 사용자에게 후속 이메일을 보낼 수 있습니다.

각 선택지에 커스텀 속성을 추가하려면 드롭다운 메뉴에서 커스텀 속성 이름을 선택하거나 새로 만든 다음, 이 선택지가 제출될 때 설정할 값을 입력합니다. [설정 페이지]({{site.baseurl}}/user_guide/data/activation/custom_data/managing_custom_data)에서 새 커스텀 속성을 만들 수도 있습니다.

커스텀 속성의 데이터 유형은 설문조사 설정 방식에 따라 중요합니다.

- **다중 선택:** 커스텀 속성의 데이터 유형은 배열이어야 합니다. 커스텀 속성이 다른 데이터 유형으로 설정된 경우 응답이 기록되지 않습니다.
- **단일 선택:** 커스텀 속성의 데이터 유형은 문자열이어야 합니다. 문자열 유형이 아닌 커스텀 속성은 드롭다운에 표시되지 않으며 응답이 기록되지 않습니다.

{% alert important %}
커스텀 속성 수집이 활성화되면 동일한 커스텀 속성 이름을 공유하는 선택지가 배열로 결합됩니다.
{% endalert %}

##### 예시 {#example}

예를 들어, [알림 환경설정 설문조사](#notification-preferences)에서 각 선택지를 부울(true/false) 속성으로 만들어 사용자가 관심 있는 주제를 선택할 수 있도록 할 수 있습니다. 사용자가 "프로모션" 선택지를 체크하면 해당 [고객 프로필]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle)에 커스텀 속성 `Promotions Topic`이 `true`로 업데이트됩니다. 선택지를 체크하지 않으면 해당 속성은 변경되지 않습니다.

그런 다음 `Custom Attribute` 필터를 사용하여 커스텀 속성 `Promotions Topic`이 `true`인 사용자의 Segment를 만들어 프로모션에 관심 있는 사용자만 관련 Campaign을 받도록 할 수 있습니다.

#### 응답만 기록 {#no-attributes}

또는 **응답만 기록(속성 없음)**을 선택할 수 있습니다. 이 옵션을 선택하면 설문조사 응답이 버튼 클릭으로 기록되지만 커스텀 속성은 사용자 프로필에 기록되지 않습니다. 즉, 각 설문조사 옵션의 클릭 측정기준은 여전히 볼 수 있지만([분석](#analytics) 참조), 해당 선택이 고객 프로필에 반영되지는 않습니다.

이러한 클릭 측정기준은 리타겟팅에 사용할 수 없습니다.

### 4단계: 제출 동작 선택 {#step-4-choose-submission-behavior}

사용자가 응답을 제출하면 선택적으로 확인 페이지를 표시하거나 단순히 메시지를 닫을 수 있습니다.

확인 페이지는 사용자에게 시간을 내주셔서 감사하다는 메시지를 전하거나 추가 정보를 제공하기에 좋은 곳입니다. 이 페이지의 행동 유도 문구를 커스터마이즈하여 사용자를 앱이나 웹사이트의 다른 페이지로 안내할 수 있습니다.

**설문조사** 탭 하단의 **제출 버튼** 섹션에서 버튼 텍스트와 클릭 시 동작을 편집합니다:

![클릭 시 동작이 '응답 제출 및 확인 페이지 표시'로 설정됨.]({% image_buster /assets/img/iam/confirmation-option.png %}){: style="max-width:60%"}

확인 페이지를 추가하려면 **확인 페이지** 탭으로 전환하여 메시지를 커스터마이즈합니다:

![간단한 설문조사 에디터의 확인 페이지 탭. 사용 가능한 필드는 헤더, 선택적 본문, 버튼 텍스트 및 버튼 클릭 시 동작입니다.]({% image_buster /assets/img/iam/confirmation-page.png %}){: style="max-width:90%"}

사용자를 앱이나 웹사이트의 다른 페이지로 안내하려면 버튼의 **클릭 시 동작**을 변경합니다.

### 5단계: 메시지 스타일 지정(선택 사항) {#styling}

**색상 테마** 선택기를 사용하여 메시지의 글꼴 색상과 강조 색상을 커스터마이즈할 수 있습니다.

![사용자가 색상 팔레트를 클릭한 후 색상 테마 선택기가 확장된 간단한 설문조사 에디터의 작성 탭.]({% image_buster /assets/img/iam/color-theme-picker.png %}){: style="max-width:80%"}

## 결과 분석 {#analytics}

Campaign이 시작되면 실시간으로 결과를 분석하여 각 선택지의 분포를 확인할 수 있습니다. [커스텀 속성 수집](#custom-attributes)을 활성화한 경우 설문조사를 제출한 사용자를 위한 새로운 Segment나 후속 Campaign을 만들 수도 있습니다.

{% alert note %}
삭제된 설문조사 선택지는 분석에 계속 표시되지만 새 사용자에게는 선택지로 표시되지 않습니다.
{% endalert %}

분석의 **인앱 메시지 성과** 섹션에서 특정 배리언트의 **결과** 드롭다운을 확장하여 설문조사 성과 측정기준을 확인할 수 있습니다. 다음은 확인할 수 있는 항목입니다:

- **설문조사 참여**는 사용자가 설문조사와 전반적으로 어떻게 상호작용했는지를 보여주며, 총 제출 수, 해제 수, 메시지 본문 내 클릭 수를 포함합니다.
- **설문조사 결과**는 각 응답 옵션을 선택한 사용자 수와 각 선택지가 전체 제출에서 차지하는 비율을 보여줍니다.
- **확인 페이지 측정기준**(활성화된 경우)에는 확인 화면을 본 사용자 수, 버튼을 클릭한 사용자 수, 상호작용 없이 해제한 사용자 수가 포함됩니다.

설문조사 측정기준의 정의는 [보고서 측정기준 용어집]({{site.baseurl}}/user_guide/analytics/metrics_glossary)을 참조하고 "In-App Message"로 필터링하세요.

Campaign 측정기준의 분석은 [인앱 메시지 보고]({{site.baseurl}}/user_guide/channels/in_app_messages/reporting)를 확인하세요.

### Currents {#currents}

선택한 선택지는 [**인앱 메시지 클릭 이벤트**]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#api_fzzdoylmrtwe) `button_id` 필드 아래에서 Currents로 자동 전달됩니다. 각 선택지는 고유 식별자(UUID)와 함께 전송됩니다.

## 사용 사례 {#use-cases}

{% tabs %}
{% tab 사용자 만족도 %}

### 사용자 만족도 {#user-satisfaction}

**목표:** 고객 만족도를 측정하고 낮은 점수를 남긴 사용자에게 윈백 Campaign을 보냅니다.

이를 설정하려면 "😡 매우 불만족"부터 "😍 매우 만족"까지 5개의 옵션이 있는 단일 선택 설문조사를 사용합니다. 각 선택지는 커스텀 속성 `customer_satisfaction`에 매핑되며, 1부터 5까지의 숫자 값을 가집니다. 여기서 1은 가장 불만족, 5는 가장 만족을 나타냅니다. 단일 선택에는 문자열 커스텀 속성이 필요하므로 이러한 숫자 값은 문자열로 저장됩니다.

| 선택지 | 속성 | 값 |
|---------------------------------------|------------------------|-------|
| 😡 매우 불만족 | `customer_satisfaction` | 1     |
| 😟 불만족 | `customer_satisfaction` | 2     |
| 🙂 보통 | `customer_satisfaction` | 3     |
| 😊 만족 | `customer_satisfaction` | 4     |
| 😍 매우 만족 | `customer_satisfaction` | 5     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="사용자 만족도" }

사용자가 설문조사를 제출하면 선택한 값이 커스텀 속성으로 기록됩니다. 그런 다음 오디언스 필터를 사용하여 후속 Campaign을 구축할 수 있습니다. 예를 들어, `customer_satisfaction` 속성이 "1" 또는 "2"인 사용자에게 윈백 메시지를 타겟팅할 수 있습니다.

{% endtab %}
{% tab 알림 환경설정 %}

### 알림 환경설정 {#notification-preferences}

**목표:** 사용자가 특정 유형의 알림을 수신하도록 선택할 수 있게 합니다.

이를 설정하려면 각 선택지가 알림 주제를 나타내는 다중 선택 설문조사를 사용합니다. 동일한 속성에 다른 값을 할당하는 대신, 각 선택지는 해당 주제에 대한 사용자의 관심을 반영하는 고유한 부울 속성에 매핑됩니다. 사용자가 선택지를 선택하면 해당 속성이 `true`로 설정됩니다. 선택하지 않으면 속성은 변경되지 않습니다.

| 선택지 | 속성 | 값 |
|--------------------|------------------------|--------|
| 제품 업데이트 | `wants_product_updates`| `true` |
| 프로모션 | `wants_promotions`     | `true` |
| 이벤트 초대 | `wants_event_invites`  | `true` |
| 설문조사 및 피드백 | `wants_surveys`        | `true` |
| 팁 및 튜토리얼 | `wants_tips`           | `true` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="알림 환경설정" }

{% endtab %}
{% tab 고객 목표 파악 %}

### 고객 목표 파악 {#identify-customer-goals}

**목표:** 사용자가 앱을 방문하는 주요 이유를 파악합니다.

이를 설정하려면 각 옵션이 일반적인 목표 또는 의도를 나타내는 단일 선택 설문조사를 사용합니다. 각 선택지는 선택한 사용자 의도에 해당하는 값으로 커스텀 속성 `product_goal`에 매핑됩니다.

| 선택지 | 속성 | 값 |
|----------------------------|------------------|-----------|
| 상태 확인 | `product_goal`   | `status`  |
| 계정 업그레이드 | `product_goal`   | `upgrade` |
| 예약 잡기 | `product_goal`   | `schedule`|
| 고객지원 | `product_goal`   | `support` |
| 둘러보기 | `product_goal`   | `browse`  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="고객 목표 파악" }

사용자가 설문조사를 제출하면 선택한 값이 프로필에 커스텀 속성으로 기록됩니다. 그런 다음 이 데이터를 사용하여 향후 경험을 개인화하거나 주요 목표에 따라 사용자를 세분화할 수 있습니다.

{% endtab %}
{% tab 전환율 개선 %}

### 전환율 개선 {#improve-conversion-rates}

**목표:** 고객이 업그레이드하거나 구매하지 않는 이유를 파악합니다.

이를 설정하려면 각 옵션이 업그레이드의 일반적인 장벽을 나타내는 단일 선택 설문조사를 사용합니다. 각 선택지는 사용자의 선택을 반영하는 해당 값으로 커스텀 속성 `upgrade_reason`에 매핑됩니다.

| 선택지 | 속성 | 값 |
|---------------------|------------------|-------------|
| 너무 비쌈 | `upgrade_reason` | `expensive` |
| 가치가 없음 | `upgrade_reason` | `value`     |
| 사용하기 어려움 | `upgrade_reason` | `difficult` |
| 경쟁사 사용 중 | `upgrade_reason` | `competitor`|
| 기타 이유 | `upgrade_reason` | `other`     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="전환율 개선" }

사용자가 설문조사를 제출하면 선택한 값이 프로필에 저장됩니다. 그런 다음 할인 혜택이나 사용성 개선 등 특정 이의에 맞춘 Campaign으로 이러한 사용자를 타겟팅할 수 있습니다.

{% endtab %}
{% tab 선호 기능 %}

### 선호 기능 {#favorite-features}

**목표:** 고객이 즐겨 사용하는 기능을 파악합니다.

이를 설정하려면 각 옵션이 앱의 기능을 나타내는 다중 선택 설문조사를 사용합니다. 각 선택지는 커스텀 속성 `favorite_features`에 매핑되며, 사용자가 설문조사를 제출하면 속성이 선택한 값의 배열로 설정됩니다.

| 선택지 | 속성 | 값 |
|-------------------|--------------------|--------------|
| 북마크 | `favorite_features`| `bookmarks`  |
| 모바일 앱 | `favorite_features`| `mobile`     |
| 게시물 공유 | `favorite_features`| `sharing`    |
| 고객지원 | `favorite_features`| `support`    |
| 커스터마이즈 | `favorite_features`| `custom`     |
| 가격/가치 | `favorite_features`| `value`      |
| 커뮤니티 | `favorite_features`| `community`  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="선호 기능" }

이 설문조사는 다중 선택을 사용하므로 사용자의 프로필은 선택한 모든 기능 값의 목록으로 업데이트됩니다.

{% endtab %}
{% endtabs %}