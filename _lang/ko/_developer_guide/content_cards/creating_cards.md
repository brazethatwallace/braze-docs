---
nav_title: 카드 만들기
article_title: Content Cards 만들기
page_order: 0
description: "이 문서에서는 커스텀 Content Cards UI를 만드는 구성요소에 대해 설명합니다."
channel:
  - content cards
platform:
  - Android
  - FireOS
  - Swift
  - Web
---

# Content Cards 만들기 {#create-content-cards}

> 이 문서에서는 커스텀 Content Cards를 구현할 때 사용할 기본 접근 방식과 세 가지 일반적인 사용 사례에 대해 설명합니다. 기본적으로 수행할 수 있는 작업과 커스텀 코드가 필요한 작업을 이해하기 위해 Content Cards 커스터마이징 가이드의 다른 문서를 이미 읽었다고 가정합니다. 커스텀 Content Cards에 대한 [분석을 기록하는]({{site.baseurl}}/developer_guide/content_cards/logging_analytics) 방법을 이해하면 특히 유용합니다.

{% multi_lang_include banners/content_card_alert.md %}

## 카드 만들기 {#creating-a-card}

### 1단계: 커스텀 UI 만들기 {#step-1-create-a-custom-ui}

{% tabs local %}
{% tab web %}

먼저, 카드를 렌더링하는 데 사용할 커스텀 HTML 컴포넌트를 만듭니다.

{% endtab %}
{% tab android %}

먼저, 커스텀 프래그먼트를 직접 만듭니다. 기본 [`ContentCardsFragment`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html)는 기본 Content Cards 유형만 처리하도록 설계되어 있지만, 좋은 출발점이 될 수 있습니다.

{% endtab %}
{% tab swift %}

먼저, 커스텀 뷰 컨트롤러 컴포넌트를 직접 만듭니다. 기본 [`BrazeContentCardUI.ViewController`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller)는 기본 Content Cards 유형만 처리하도록 설계되어 있지만, 좋은 출발점이 될 수 있습니다.

{% endtab %}
{% endtabs %}

### 2단계: 카드 업데이트 구독하기 {#step-2-subscribe-to-card-updates}

카드가 새로고침될 때 데이터 업데이트를 구독하기 위해 콜백 함수를 등록합니다. Content Cards 객체를 파싱하여 `title`, `cardDescription`, `imageUrl` 등의 페이로드 데이터를 추출한 다음, 결과 모델 데이터를 사용하여 커스텀 UI를 채울 수 있습니다.

Content Cards 데이터 모델을 얻으려면 Content Cards 업데이트를 구독합니다. 다음 속성정보에 특히 주의하세요:

* **`id`:** Content Cards ID 문자열을 나타냅니다. 커스텀 Content Cards에서 분석을 기록하는 데 사용되는 고유 식별자입니다.
* **`extras`:** Braze 대시보드의 모든 키-값 페어를 포함합니다.

`id`와 `extras` 이외의 모든 속성정보는 커스텀 Content Cards에서 선택적으로 파싱할 수 있습니다. 데이터 모델에 대한 자세한 내용은 각 플랫폼의 통합 문서를 참조하세요: [Android]({{site.baseurl}}/developer_guide/content_cards?sdktab=android), [iOS]({{site.baseurl}}/developer_guide/content_cards?sdktab=swift), [웹]({{site.baseurl}}/developer_guide/content_cards?sdktab=web).

{% tabs local %}
{% tab web %}

```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToContentCardsUpdates((updates) => {
  const cards = updates.cards;
// For example:
  cards.forEach(card => {
    if (card.isControl) {
      // Do not display the control card, but remember to call `logContentCardImpressions([card])`
    }
    else if (card instanceof braze.ClassicCard || card instanceof braze.CaptionedImage) {
      // Use `card.title`, `card.imageUrl`, etc.
    }
    else if (card instanceof braze.ImageOnly) {
      // Use `card.imageUrl`, etc.
    }
  })
});

braze.openSession();
```

{% alert note %}
Content Cards는 `subscribeToContentCardsUpdates()`가 `openSession()` 전에 호출된 경우에만 세션 시작 시 새로고침됩니다. 언제든지 [수동으로 피드를 새로고침]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/feed)할 수도 있습니다.
{% endalert %}

{% endtab %}
{% tab android %}
{% subtabs local %}
{% subtab Java %}

#### 2a단계: 비공개 구독자 변수 만들기 {#step-2a-create-a-private-subscriber-variable}

카드 업데이트를 구독하려면 먼저 커스텀 클래스에 구독자를 보관할 비공개 변수를 선언합니다:

```java
// subscriber variable
private IEventSubscriber<ContentCardsUpdatedEvent> mContentCardsUpdatedSubscriber;
```

#### 2b단계: 업데이트 구독하기 {#step-2b-subscribe-to-updates}

다음 코드를 추가하여 Braze에서 Content Cards 업데이트를 구독합니다. 일반적으로 커스텀 Content Cards 액티비티의 `Activity.onCreate()` 내부에 추가합니다:

```java
// Remove the previous subscriber before rebuilding a new one with our new activity.
Braze.getInstance(context).removeSingleSubscription(mContentCardsUpdatedSubscriber, ContentCardsUpdatedEvent.class);
mContentCardsUpdatedSubscriber = new IEventSubscriber<ContentCardsUpdatedEvent>() {
    @Override
    public void trigger(ContentCardsUpdatedEvent event) {
        // List of all Content Cards
        List<Card> allCards = event.getAllCards();

        // Your logic below
    }
};
Braze.getInstance(context).subscribeToContentCardsUpdates(mContentCardsUpdatedSubscriber);
Braze.getInstance(context).requestContentCardsRefresh();
```

#### 2c단계: 구독 해제하기 {#step-2c-unsubscribe}

커스텀 액티비티가 화면에서 벗어날 때 구독을 해제합니다. 액티비티의 `onDestroy()` 수명 주기 메서드에 다음 코드를 추가합니다:

```java
Braze.getInstance(context).removeSingleSubscription(mContentCardsUpdatedSubscriber, ContentCardsUpdatedEvent.class);
```

{% endsubtab %}
{% subtab Kotlin %}

#### 2a단계: 비공개 구독자 변수 만들기

카드 업데이트를 구독하려면 먼저 커스텀 클래스에 구독자를 보관할 비공개 변수를 선언합니다:

```kotlin
private var contentCardsUpdatedSubscriber: IEventSubscriber<ContentCardsUpdatedEvent>? = null
```

#### 2b단계: 업데이트 구독하기

다음 코드를 추가하여 Braze에서 Content Cards 업데이트를 구독합니다. 일반적으로 커스텀 Content Cards 액티비티의 `Activity.onCreate()` 내부에 추가합니다:

```kotlin
// Remove the previous subscriber before rebuilding a new one with our new activity.
Braze.getInstance(context).subscribeToContentCardsUpdates(contentCardsUpdatedSubscriber)
Braze.getInstance(context).requestContentCardsRefresh()
  // List of all Content Cards
  val allCards = event.allCards

  // Your logic below
}
Braze.getInstance(context).subscribeToContentCardsUpdates(mContentCardsUpdatedSubscriber)
Braze.getInstance(context).requestContentCardsRefresh(true)
```

#### 2c단계: 구독 해제하기

커스텀 액티비티가 화면에서 벗어날 때 구독을 해제합니다. 액티비티의 `onDestroy()` 수명 주기 메서드에 다음 코드를 추가합니다:

```kotlin
Braze.getInstance(context).removeSingleSubscription(contentCardsUpdatedSubscriber, ContentCardsUpdatedEvent::class.java)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab swift %}

Content Cards 데이터 모델에 접근하려면 `braze` 인스턴스에서 [`contentCards.cards`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/cards)를 호출합니다.

{% subtabs local %}
{% subtab Swift %}

```swift
let cards: [Braze.ContentCard] = AppDelegate.braze?.contentCards.cards
```

또한 Content Cards의 변경 사항을 관찰하기 위한 구독을 유지할 수 있습니다. 다음 두 가지 방법 중 하나로 수행할 수 있습니다:
1. 취소 가능한 객체를 유지하거나,
2. `AsyncStream`을 유지합니다.

##### 취소 가능한 객체 {#cancellable}

```swift
// This subscription is maintained through a Braze cancellable, which will observe for changes until the subscription is cancelled.
// You must keep a strong reference to the cancellable to keep the subscription active.
// The subscription is canceled either when the cancellable is deinitialized or when you call its `.cancel()` method.
let cancellable = AppDelegate.braze?.contentCards.subscribeToUpdates { [weak self] contentCards in
  // Implement your completion handler to respond to updates in `contentCards`.
}
```

##### AsyncStream

```swift
let stream: AsyncStream<[Braze.ContentCard]> = AppDelegate.braze?.contentCards.cardsStream
```

{% endsubtab %}
{% subtab Objective-C %}

```objc
NSArray<BRZContentCardRaw *> *contentCards = AppDelegate.braze.contentCards.cards;
```

또한 콘텐츠 카드에 대한 구독을 유지하려면 [`subscribeToUpdates`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/subscribetoupdates(_:))를 호출할 수 있습니다:

```objc
// This subscription is maintained through Braze cancellable, which will continue to observe for changes until the subscription is cancelled.
BRZCancellable *cancellable = [self.braze.contentCards subscribeToUpdates:^(NSArray<BRZContentCardRaw *> *contentCards) {
  // Implement your completion handler to respond to updates in `contentCards`.
}];
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}


### 3단계: 분석 구현하기 {#step-3-implement-analytics}

Content Cards의 노출 횟수, 클릭, 해제는 커스텀 뷰에서 자동으로 기록되지 않습니다. 모든 측정기준을 Braze 대시보드 분석에 올바르게 기록하려면 [각각의 메서드를 구현]({{site.baseurl}}/developer_guide/content_cards/logging_analytics)해야 합니다.

### 4단계: 카드 테스트하기 (선택 사항) {#step-4-test-your-card-optional}

Content Cards를 테스트하려면:

1. [`changeUser()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser) 메서드를 호출하여 애플리케이션에 활성 사용자를 설정합니다.
2. Braze에서 **Campaigns**로 이동한 다음 [새 콘텐츠 카드 캠페인을 만듭니다]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card).
3. Campaign에서 **테스트**를 선택한 다음 테스트 사용자의 `user-id`를 입력합니다. 준비가 되면 **테스트 보내기**를 선택합니다. 곧 기기에서 Content Cards를 실행할 수 있습니다.

![자신의 사용자 ID를 테스트 수신자로 추가하여 Content Cards를 테스트할 수 있음을 보여주는 Braze 콘텐츠 카드 캠페인]({% image_buster /assets/img/react-native/content-card-test.png %} "Content Card Campaign Test")

## Content Cards 배치 {#content-card-placements}

Content Cards는 다양한 방식으로 사용할 수 있습니다. 일반적인 세 가지 구현 방법은 메시지 센터, 동적 이미지 광고 또는 이미지 캐러셀로 사용하는 것입니다. 이러한 각 배치에서 Content Cards에 [키-값 페어]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/behavior)(데이터 모델의 `extras` 속성정보)를 할당하고, 해당 값을 기반으로 런타임 중에 카드의 동작, 외관 또는 기능을 동적으로 조정합니다.

![메시지 받은편지함, 동적 이미지 광고, 이미지 캐러셀 등 세 가지 Content Cards 배치 예시를 보여주는 다이어그램.]({% image_buster /assets/img_archive/cc_placements.png %}){: style="border:0px;"}

### 메시지 받은편지함 {#message-inbox}

Content Cards를 메시지 센터처럼 사용할 수 있습니다. 이 형식에서는 각 메시지가 개별 카드이며, 클릭 이벤트를 구동하는 [키-값 페어]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/behavior)를 포함합니다. 이 키-값 페어는 사용자가 받은편지함 메시지를 클릭할 때 어디로 이동할지 결정하기 위해 애플리케이션이 참조하는 핵심 식별자입니다. 키-값 페어의 값은 임의로 설정할 수 있습니다.

#### 예시 {#example}

예를 들어, 두 개의 메시지 카드를 만들고 싶을 수 있습니다: 사용자에게 독서 추천을 활성화하도록 유도하는 행동 유도 카드와 신규 구독자 Segment에 제공하는 쿠폰 코드 카드입니다.

`body`, `title`, `buttonText`와 같은 키에는 마케터가 설정할 수 있는 간단한 문자열 값이 들어갈 수 있습니다. `terms`와 같은 키에는 법무 부서가 승인한 소규모 문구 모음을 제공하는 값이 들어갈 수 있습니다. `style` 및 `class_type`과 같은 키에는 앱이나 사이트에서 카드가 어떻게 렌더링될지 결정하기 위해 설정할 수 있는 문자열 값이 들어갑니다.

{% tabs local %}
{% tab 독서 추천 %}
독서 추천 카드의 키-값 페어:

| 키 | 값 |
|------------|----------------------------------------------------------------------|
| `body`       | Add your interests to your Politer Weekly profile for personal reading recommendations. |
| `style`      | info                                                                 |
| `class_type` | notification_center                                                 |
| `card_priority` | 1                                                                 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="예시" }
{% endtab %}

{% tab 신규 구독자 쿠폰 %}
신규 구독자 쿠폰의 키-값 페어:

| 키 | 값 |
|------------|------------------------------------------------------------------|
| `title`      | Subscribe for unlimited games                                    |
| `body`       | End of Summer Special - Enjoy 10% off Politer games              |
| `buttonText` | Subscribe Now                                                    |
| `style`      | promo                                                            |
| `class_type` | notification_center                                              |
| `card_priority` | 2                                                              |
| `terms`      | new_subscribers_only                                             |
{: .reset-td-br-1 .reset-td-br-2 aria-label="예시" }
{% endtab %}
{% endtabs %}

{% details Android 추가 정보 %}

Android 및 FireOS SDK에서는 메시지 센터 로직이 Braze의 키-값 페어에서 제공하는 `class_type` 값에 의해 구동됩니다. [`createContentCardable`]({{site.baseurl}}/developer_guide/content_cards) 메서드를 사용하면 이러한 클래스 유형을 필터링하고 식별할 수 있습니다.

{% tabs local %}
{% tab Kotlin %}
**클릭 동작을 위한 `class_type` 사용**<br>
Content Cards 데이터를 커스텀 클래스로 변환할 때, 데이터의 `ContentCardClass` 속성정보를 사용하여 데이터를 저장하는 데 사용할 구체적인 하위 클래스를 결정합니다.

```kotlin
 private fun createContentCardable(metadata: Map<String, Any>, type: ContentCardClass?): ContentCardable?{
        return when(type){
            ContentCardClass.AD -> Ad(metadata)
            ContentCardClass.MESSAGE_WEB_VIEW -> WebViewMessage(metadata)
            ContentCardClass.NOTIFICATION_CENTER -> FullPageMessage(metadata)
            ContentCardClass.ITEM_GROUP -> Group(metadata)
            ContentCardClass.ITEM_TILE -> Tile(metadata)
            ContentCardClass.COUPON -> Coupon(metadata)
            else -> null
        }
    }
```

그런 다음, 메시지 목록에서 사용자 상호작용을 처리할 때 메시지 유형을 사용하여 사용자에게 표시할 뷰를 결정할 수 있습니다.

```kotlin
override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        //...
        listView.onItemClickListener = AdapterView.OnItemClickListener { parent, view, position, id ->
           when (val card = dataProvider[position]){
                is WebViewMessage -> {
                    val intent = Intent(this, WebViewActivity::class.java)
                    val bundle = Bundle()
                    bundle.putString(WebViewActivity.INTENT_PAYLOAD, card.contentString)
                    intent.putExtras(bundle)
                    startActivity(intent)
                }
                is FullPageMessage -> {
                    val intent = Intent(this, FullPageContentCard::class.java)
                    val bundle = Bundle()
                    bundle.putString(FullPageContentCard.CONTENT_CARD_IMAGE, card.icon)
                    bundle.putString(FullPageContentCard.CONTENT_CARD_TITLE, card.messageTitle)
                    bundle.putString(FullPageContentCard.CONTENT_CARD_DESCRIPTION, card.cardDescription)
                    intent.putExtras(bundle)
                    startActivity(intent)
                }
            }

        }
    }
```
{% endtab %}
{% tab Java %}
**클릭 동작을 위한 `class_type` 사용**<br>
Content Cards 데이터를 커스텀 클래스로 변환할 때, 데이터의 `ContentCardClass` 속성정보를 사용하여 데이터를 저장하는 데 사용할 구체적인 하위 클래스를 결정합니다.

```java
private ContentCardable createContentCardable(Map<String, ?> metadata,  ContentCardClass type){
    switch(type){
        case ContentCardClass.AD:{
            return new Ad(metadata);
        }
        case ContentCardClass.MESSAGE_WEB_VIEW:{
            return new WebViewMessage(metadata);
        }
        case ContentCardClass.NOTIFICATION_CENTER:{
            return new FullPageMessage(metadata);
        }
        case ContentCardClass.ITEM_GROUP:{
            return new Group(metadata);
        }
        case ContentCardClass.ITEM_TILE:{
            return new Tile(metadata);
        }
        case ContentCardClass.COUPON:{
            return new Coupon(metadata);
        }
        default:{
            return null;
        }
    }
}

```

그런 다음, 메시지 목록에서 사용자 상호작용을 처리할 때 메시지 유형을 사용하여 사용자에게 표시할 뷰를 결정할 수 있습니다.

```java
@Override
protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState)
        //...
        listView.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> parent, View view, int position, long id){
               ContentCardable card = dataProvider.get(position);
               if (card instanceof WebViewMessage){
                    Bundle intent = new Intent(this, WebViewActivity.class);
                    Bundle bundle = new Bundle();
                    bundle.putString(WebViewActivity.INTENT_PAYLOAD, card.getContentString());
                    intent.putExtras(bundle);
                    startActivity(intent);
                }
                else if (card instanceof FullPageMessage){
                    Intent intent = new Intent(this, FullPageContentCard.class);
                    Bundle bundle = Bundle();
                    bundle.putString(FullPageContentCard.CONTENT_CARD_IMAGE, card.getIcon());
                    bundle.putString(FullPageContentCard.CONTENT_CARD_TITLE, card.getMessageTitle());
                    bundle.putString(FullPageContentCard.CONTENT_CARD_DESCRIPTION, card.getCardDescription());
                    intent.putExtras(bundle)
                    startActivity(intent)
                }
            }

        });
    }
```

{% endtab %}
{% endtabs %}
{% enddetails %}

### 캐러셀 {#carousel}

완전히 커스텀된 캐러셀 피드에 Content Cards를 설정하여 사용자가 스와이프하면서 추가 추천 카드를 볼 수 있도록 할 수 있습니다. 기본적으로 Content Cards는 생성 날짜순(최신순)으로 정렬되며, 사용자는 자격이 있는 모든 카드를 볼 수 있습니다.

Content Cards 캐러셀을 구현하려면:

1. [Content Cards 변경 사항]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/feed)을 감지하고 Content Cards 도착을 처리하는 커스텀 로직을 생성합니다.
2. 캐러셀에 특정 수의 카드를 한 번에 표시하기 위한 커스텀 클라이언트 측 로직을 생성합니다. 예를 들어, 배열에서 처음 다섯 개의 Content Cards 객체를 선택하거나 키-값 페어를 도입하여 조건 로직을 구성할 수 있습니다.

{% alert tip %}
캐러셀을 보조 Content Cards 피드로 구현하는 경우, [키-값 페어를 사용하여 카드를 올바른 피드로 정렬]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/feed)해야 합니다.
{% endalert %}

### 이미지 전용 {#image-only}

Content Cards가 반드시 "카드"처럼 보일 필요는 없습니다. 예를 들어, Content Cards는 홈페이지나 지정된 페이지 상단에 지속적으로 표시되는 동적 이미지로 나타날 수 있습니다.

이를 구현하려면 마케터가 **Image Only** 유형의 Content Cards로 Campaign 또는 캔버스 단계를 생성합니다. 그런 다음, [Content Cards를 보충 콘텐츠로 사용]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/behavior)하는 데 적합한 키-값 페어를 설정합니다.