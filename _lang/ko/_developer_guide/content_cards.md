---
page_order: 2.2
nav_title: 콘텐츠 카드
article_title: 콘텐츠 카드
description: "데이터 모델, 카드 유형, 모바일 및 웹 앱을 위한 커스터마이징 옵션을 포함하여 Braze SDK로 Content Cards를 구현하는 방법을 알아보세요."
channel:
  - content cards
platform:
  - Android
  - FireOS
  - Swift
  - Web
---

# 콘텐츠 카드 {#content-cards}

> 애플리케이션에서 사용할 수 있는 다양한 데이터 모델과 카드별 속성정보를 포함하여 Braze SDK의 Content Cards에 대해 알아보세요.

{% multi_lang_include banners/content_card_alert.md %}

{% sdktabs %}
{% sdktab web %}
{% multi_lang_include developer_guide/web/content_cards.md %}
{% endsdktab %}

{% sdktab android %}
## 필수 조건 {#prerequisites}

Braze Content Cards를 사용하려면 먼저 앱에 [Braze Android SDK]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android)를 통합해야 합니다. 그러나 추가 설정은 필요하지 않습니다.

## Google 프래그먼트 {#google-fragments}

Android에서 Content Cards 피드는 Braze Android UI 프로젝트에서 사용할 수 있는 [프래그먼트](https://developer.android.com/guide/components/fragments.html)로 구현됩니다. [`ContentCardsFragment`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html) 클래스는 Content Cards의 콘텐츠를 자동으로 새로고침하고 표시하며 사용 분석을 기록합니다. 사용자의 `ContentCards`에 표시될 수 있는 카드는 Braze 대시보드에서 생성됩니다.

액티비티에 프래그먼트를 추가하는 방법은 [Google의 프래그먼트 설명서](https://developer.android.com/guide/fragments#Adding)를 참조하세요.

## 카드 유형 및 속성정보 {#card-types-and-properties}

Content Cards 데이터 모델은 Android SDK에서 사용할 수 있으며 다음과 같은 고유한 Content Cards 유형을 제공합니다. 각 유형은 기본 모델을 공유하므로 기본 모델에서 공통 속성정보를 상속받을 수 있으며, 각 유형만의 고유한 속성정보도 가지고 있습니다. 전체 참조 설명서는 [`com.braze.models.cards`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/index.html)를 참조하세요.

### 기본 카드 모델 {#base-card-for-android}

[기본 카드](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html) 모델은 모든 카드에 대한 기본 동작을 제공합니다.

| 속성정보 | 설명 |
|---|---|
|`getId()` | Braze에서 설정한 카드 ID를 반환합니다.|
|`getViewed()` | 사용자가 카드를 읽었는지 읽지 않았는지를 나타내는 불리언을 반환합니다.|
|`getExtras()` | 이 카드의 키-값 추가 항목 맵을 반환합니다.|
|`getCreated()` | Braze에서 카드가 생성된 시간의 unix 타임스탬프를 반환합니다.|
|`isPinned` | 카드가 고정되어 있는지를 나타내는 불리언을 반환합니다.|
|`getOpenUriInWebView()` | 이 카드의 URI를 Braze WebView에서 열어야 하는지 <br> 여부를 나타내는 불리언을 반환합니다.|
|`getExpiredAt()` | 카드의 만료 날짜를 가져옵니다.|
|`isRemoved()` | 최종사용자가 이 카드를 해제했는지를 나타내는 불리언을 반환합니다.|
|`isDismissibleByUser()` | 사용자가 카드를 해제할 수 있는지를 나타내는 불리언을 반환합니다.|
|`isClicked()` | 이 카드의 클릭 상태를 나타내는 불리언을 반환합니다.|
|`isDismissed` | 카드가 해제되었는지를 나타내는 불리언을 반환합니다. 카드를 해제됨으로 표시하려면 `true`로 설정합니다. 이미 해제됨으로 표시된 카드는 다시 해제됨으로 표시할 수 없습니다.|
|`isControl()` | 이 카드가 컨트롤 카드이며 렌더링되지 않아야 하는지를 나타내는 불리언을 반환합니다.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="기본 카드 모델 #base-card-for-android" }

### 이미지 전용 {#banner-image-card-for-android}

[이미지 전용 카드](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-image-only-card/index.html)는 클릭 가능한 전체 크기 이미지입니다.

| 속성정보 | 설명 |
|---|---|
|`getImageUrl()` | 카드 이미지의 URL을 반환합니다.|
|`getUrl()` | 카드를 클릭한 후 열리는 URL을 반환합니다. HTTP(s) URL 또는 프로토콜 URL일 수 있습니다.|
|`getDomain()` | 속성정보 URL의 링크 텍스트를 반환합니다.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="이미지 전용 #banner-image-card-for-android" }

### 캡션 이미지 {#captioned-image-card-for-android}

[캡션 이미지 카드](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-captioned-image-card/index.html)는 설명 텍스트가 함께 제공되는 클릭 가능한 전체 크기 이미지입니다.

| 속성정보 | 설명 |
|---|---|
|`getImageUrl()` | 카드 이미지의 URL을 반환합니다.|
|`getTitle()` | 카드의 제목 텍스트를 반환합니다.|
|`getDescription()` | 카드의 본문 텍스트를 반환합니다.|
|`getUrl()` | 카드를 클릭한 후 열리는 URL을 반환합니다. HTTP(s) URL 또는 프로토콜 URL일 수 있습니다.|
|`getDomain()` | 속성정보 URL의 링크 텍스트를 반환합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="캡션 이미지 #captioned-image-card-for-android" }

### 클래식 {#text-Announcement-card-for-android}

이미지가 포함되지 않은 클래식 카드는 [텍스트 공지 카드](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-text-announcement-card/index.html)가 됩니다. 이미지가 포함된 경우 [짧은 뉴스 카드](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-short-news-card/index.html)를 받게 됩니다.

| 속성정보 | 설명 |
|---|---|
|`getTitle()` | 카드의 제목 텍스트를 반환합니다. |
|`getDescription()` | 카드의 본문 텍스트를 반환합니다. |
|`getUrl()` | 카드를 클릭한 후 열리는 URL을 반환합니다. HTTP(s) URL 또는 프로토콜 URL일 수 있습니다. |
|`getDomain()` | 속성정보 URL의 링크 텍스트를 반환합니다. |
|`getImageUrl()` | 카드 이미지의 URL을 반환합니다. 클래식 짧은 뉴스 카드에만 적용됩니다. |
|`isDismissed` | 카드가 해제되었는지를 나타내는 불리언을 반환합니다. 카드를 해제됨으로 표시하려면 `true`로 설정합니다. 이미 해제됨으로 표시된 카드는 다시 해제됨으로 표시할 수 없습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="클래식 #text-Announcement-card-for-android" }

## 카드 메서드 {#card-methods}

모든 [`Card`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/index.html) 데이터 모델 객체는 Braze 서버에 사용자 이벤트를 기록하기 위한 다음 분석 메서드를 제공합니다.

| 메서드 | 설명 |
|---|---|
|`logImpression()` | 특정 카드에 대한 노출을 Braze에 수동으로 기록합니다. |
|`logClick()` | 특정 카드에 대한 클릭을 Braze에 수동으로 기록합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="카드 메서드" }

{% endsdktab %}

{% sdktab swift %}
{% multi_lang_include developer_guide/swift/content_cards.md %}
{% endsdktab %}

{% sdktab cordova %}
{% multi_lang_include developer_guide/cordova/content_cards.md %}
{% endsdktab %}

{% sdktab flutter %}
{% multi_lang_include developer_guide/flutter/content_cards.md %}
{% endsdktab %}

{% sdktab react native %}
{% multi_lang_include developer_guide/react_native/content_cards.md %}
{% endsdktab %}

{% sdktab tvos %}
## 필수 조건

Content Cards를 사용하려면 먼저 앱에 [Braze Swift SDK]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=swift)를 통합하세요. 그런 다음 tvOS 앱 설정 단계를 완료합니다.

{% alert important %}
Content Cards는 Swift SDK를 사용한 헤드리스 UI를 통해 지원되며, tvOS용 기본 UI나 뷰가 포함되어 있지 않으므로 커스텀 UI를 직접 구현하세요.
{% endalert %}

## tvOS 앱 설정 {#setting-up-your-tvos-app}

### 1단계: 새 iOS 앱 만들기 {#step-1-create-a-new-ios-app}

Braze에서 **설정** > **앱 설정**을 선택한 다음 **앱 추가**를 선택합니다. tvOS 앱의 이름을 입력하고 **iOS**&#8212;_tvOS가 아님_&#8212;를 선택한 다음 **앱 추가**를 선택합니다.

![tvOS 앱을 등록하기 위해 iOS 플랫폼이 선택된 Braze의 앱 추가 대화 상자]({% image_buster /assets/img/tvos.png %}){: style="width:70%"}

{% alert warning %}
**tvOS** 체크박스를 선택하면 tvOS용 Content Cards를 커스터마이징할 수 없습니다.
{% endalert %}

### 2단계: 앱의 API 키 가져오기 {#step-2-get-your-apps-api-key}

앱 설정에서 새 tvOS 앱을 선택한 다음 앱의 API 키를 확인합니다. 이 키를 사용하여 Xcode에서 앱을 구성합니다.

![SDK 통합에 사용되는 API 키를 보여주는 tvOS 앱의 앱 설정]({% image_buster /assets/img/tvos1.png %}){: style="width:70%"}

### 3단계: BrazeKit 통합 {#step-3-integrate-brazekit}

앱의 API 키를 사용하여 Xcode의 tvOS 프로젝트에 [Braze Swift SDK](https://github.com/braze-inc/braze-swift-sdk)를 통합합니다. Braze Swift SDK에서 BrazeKit만 통합하면 됩니다.

### 4단계: 커스텀 UI 만들기 {#step-4-create-your-custom-ui}

Braze는 tvOS에서 콘텐츠 카드에 대한 기본 UI를 제공하지 않으므로 직접 커스터마이징해야 합니다. 전체 안내는 단계별 튜토리얼을 참조하세요: [tvOS용 콘텐츠 카드 커스터마이징](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/content-cards-customization/). 샘플 프로젝트는 [Braze Swift SDK 샘플](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples#contentcards-custom-ui)을 참조하세요.

{% endsdktab %}

{% sdktab unity %}
{% multi_lang_include developer_guide/unity/content_cards.md %}
{% endsdktab %}

{% sdktab .NET MAUI (Xamarin) %}
{% multi_lang_include developer_guide/xamarin/content_cards.md %}
{% endsdktab %}
{% endsdktabs %}