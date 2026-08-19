> 콘텐츠 카드에 대한 커스텀 UI를 구축할 때, 노출 횟수, 클릭 및 해제와 같은 분석을 수동으로 기록해야 합니다. 이는 기본 카드 모델에 대해서만 자동으로 처리됩니다. 이러한 이벤트를 기록하는 것은 Content Cards 통합의 표준 부분이며, 정확한 Campaign 보고 및 청구에 필수적입니다. 이를 위해 Braze 데이터 모델의 데이터로 커스텀 UI를 채운 다음 이벤트를 수동으로 기록합니다. 분석을 기록하는 방법을 이해하면 Braze 고객이 [커스텀 Content Cards를 생성]({{site.baseurl}}/developer_guide/content_cards/creating_cards)하는 일반적인 방법을 확인할 수 있습니다.

## 분석 로깅 {#logging-analytics}

커스텀 Content Cards를 구현할 때, Content Card 오브젝트를 파싱하여 `title`, `cardDescription`, `imageUrl` 등의 페이로드 데이터를 추출할 수 있습니다. 그런 다음 결과 모델 데이터를 사용하여 커스텀 UI를 채울 수 있습니다.

Content Card 데이터 모델을 가져오려면 Content Card 업데이트를 구독하세요. 특히 주의해야 할 두 가지 속성정보가 있습니다:

* **`id`**: Content Card ID 문자열을 나타냅니다. 커스텀 Content Cards에서 분석을 로깅하는 데 사용되는 고유 식별자입니다.
* **`extras`**: Braze 대시보드의 모든 키-값 페어를 포함합니다.

`id`와 `extras` 이외의 모든 속성정보는 커스텀 Content Cards에서 파싱이 선택 사항입니다. 데이터 모델에 대한 자세한 내용은 각 플랫폼의 통합 문서를 참조하세요: [Android]({{site.baseurl}}/developer_guide/content_cards/?sdktab=android), [iOS]({{site.baseurl}}/developer_guide/content_cards/?sdktab=swift), [웹]({{site.baseurl}}/developer_guide/content_cards/?sdktab=web).


{% tabs %}
{% tab 웹 %}

카드가 새로고침될 때 업데이트를 구독하려면 콜백 함수를 등록하세요.

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
Content Cards는 `openSession()` 전에 구독 요청이 호출된 경우에만 세션 시작 시 새로고침됩니다. 언제든지 [수동으로 피드를 새로고침]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/feed)할 수도 있습니다.
{% endalert %}

{% endtab %}
{% tab Android %}
{% subtabs local %}
{% subtab Java %}

### 1단계: 비공개 구독자 변수 생성 {#step-1-create-a-private-subscriber-variable}

카드 업데이트를 구독하려면 먼저 커스텀 클래스에서 구독자를 보관할 비공개 변수를 선언합니다:

```java
// subscriber variable
private IEventSubscriber<ContentCardsUpdatedEvent> mContentCardsUpdatedSubscriber;
```

### 2단계: 업데이트 구독 {#step-2-subscribe-to-updates}

다음으로, Braze에서 Content Card 업데이트를 구독하기 위해 아래 코드를 추가합니다. 일반적으로 커스텀 Content Cards 액티비티의 `Activity.onCreate()` 내부에 배치합니다:

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

### 3단계: 구독 해제 {#step-3-unsubscribe}

커스텀 액티비티가 화면에서 벗어날 때 구독을 해제하는 것도 권장합니다. 액티비티의 `onDestroy()` 라이프사이클 메서드에 다음 코드를 추가하세요:

```java
Braze.getInstance(context).removeSingleSubscription(mContentCardsUpdatedSubscriber, ContentCardsUpdatedEvent.class);
```

{% endsubtab %}
{% subtab Kotlin %}

### 1단계: 비공개 구독자 변수 생성

카드 업데이트를 구독하려면 먼저 커스텀 클래스에서 구독자를 보관할 비공개 변수를 선언합니다:

```kotlin
private var contentCardsUpdatedSubscriber: IEventSubscriber<ContentCardsUpdatedEvent>? = null
```

### 2단계: 업데이트 구독

다음으로, Braze에서 Content Card 업데이트를 구독하기 위해 아래 코드를 추가합니다. 일반적으로 커스텀 Content Cards 액티비티의 `Activity.onCreate()` 내부에 배치합니다:

```kotlin
// Remove the previous subscriber before rebuilding a new one with our new activity.
Braze.getInstance(context).removeSingleSubscription(contentCardsUpdatedSubscriber, ContentCardsUpdatedEvent::class.java)
contentCardsUpdatedSubscriber = IEventSubscriber { event ->
  // List of all Content Cards
  val allCards = event.allCards

  // Your logic below
}
Braze.getInstance(context).subscribeToContentCardsUpdates(contentCardsUpdatedSubscriber)
Braze.getInstance(context).requestContentCardsRefresh(true)
```

### 3단계: 구독 해제

커스텀 액티비티가 화면에서 벗어날 때 구독을 해제하는 것도 권장합니다. 액티비티의 `onDestroy()` 라이프사이클 메서드에 다음 코드를 추가하세요:

```kotlin
Braze.getInstance(context).removeSingleSubscription(contentCardsUpdatedSubscriber, ContentCardsUpdatedEvent::class.java)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Swift %}

Content Cards 데이터 모델에 접근하려면 `braze` 인스턴스에서 [`contentCards.cards`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/cards)를 호출하세요.

{% subtabs local %}
{% subtab Swift %}

```swift
let cards: [Braze.ContentCard] = AppDelegate.braze?.contentCards.cards
```

{% alert note %}
`contentCards.cards`, `contentCards.unviewedCards` 또는 `contentCards.lastUpdate`를 읽으면 SDK가 초기화 후 작업을 완료할 때까지 호출 스레드가 차단됩니다. 메인 스레드 또는 지연에 민감한 컨텍스트에서는 [논블로킹 스냅샷 접근자](#non-blocking-snapshot-accessors)를 사용하세요.
{% endalert %}

또한 Content Cards의 변경 사항을 관찰하기 위한 구독을 유지할 수도 있습니다. 다음 두 가지 방법 중 하나로 수행할 수 있습니다:
1. 취소 가능 객체 유지; 또는
2. `AsyncStream` 유지.

### 취소 가능 객체 {#cancellable}

```swift
// This subscription is maintained through a Braze cancellable, which will observe for changes until the subscription is cancelled.
// You must keep a strong reference to the cancellable to keep the subscription active.
// The subscription is canceled either when the cancellable is deinitialized or when you call its `.cancel()` method.
let cancellable = AppDelegate.braze?.contentCards.subscribeToUpdates { [weak self] contentCards in
  // Implement your completion handler to respond to updates in `contentCards`.
}
```

### AsyncStream

```swift
let stream: AsyncStream<[Braze.ContentCard]> = AppDelegate.braze?.contentCards.cardsStream
```

### 논블로킹 스냅샷 접근자 {#non-blocking-snapshot-accessors}

호출 스레드를 차단하지 않고 현재 캐시된 상태를 읽으려면 다음 메서드를 사용하세요. 각 완료 핸들러는 항상 메인 스레드에서 전달됩니다.

```swift
// All cached cards.
AppDelegate.braze?.contentCards.getCachedContentCards { cards in
  // Use `cards` here.
}

// Unviewed cards only (excludes control cards).
AppDelegate.braze?.contentCards.getUnviewedCards { cards in
  // Use `cards` here.
}

// Date of the last server sync for the current user (nil until the first sync completes).
AppDelegate.braze?.contentCards.getLastUpdate { date in
  // Use `date` here.
}
```

{% endsubtab %}
{% subtab Objective-C %}

```objc
NSArray<BRZContentCardRaw *> *contentCards = AppDelegate.braze.contentCards.cards;
```

또한 Content Cards에 대한 구독을 유지하려면 [`subscribeToUpdates`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/subscribetoupdates(_:))를 호출할 수 있습니다:

```objc
// This subscription is maintained through Braze cancellable, which will continue to observe for changes until the subscription is cancelled.
BRZCancellable *cancellable = [self.braze.contentCards subscribeToUpdates:^(NSArray<BRZContentCardRaw *> *contentCards) {
  // Implement your completion handler to respond to updates in `contentCards`.
}];
```

호출 스레드를 차단하지 않고 현재 캐시된 상태를 읽으려면 다음 메서드를 사용하세요. 각 완료 핸들러는 메인 스레드에서 전달됩니다.

```objc
// All cached cards.
[AppDelegate.braze.contentCards getCachedContentCardsWithCompletion:^(NSArray<BRZContentCardRaw *> *cards) {
  // Use `cards` here.
}];

// Unviewed cards only (excludes control cards).
[AppDelegate.braze.contentCards getUnviewedCardsWithCompletion:^(NSArray<BRZContentCardRaw *> *cards) {
  // Use `cards` here.
}];

// Date of the last server sync for the current user (nil until the first sync completes).
[AppDelegate.braze.contentCards getLastUpdateWithCompletion:^(NSDate * _Nullable date) {
  // Use `date` here.
}];
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab React Native %}

업데이트를 수신하려면 Content Card 업데이트 이벤트를 구독하세요:

```javascript
const subscription = Braze.addListener(Braze.Events.CONTENT_CARDS_UPDATED, (update) => {
  const cards = update.cards;
  cards.forEach(card => {
    if (card.isControl) {
      // Do not display the control card, but remember to log an impression
    } else {
      // Use card.title, card.cardDescription, card.image, etc.
    }
  });
});
```

가장 최근에 캐시된 Content Card 데이터를 가져오려면:

```javascript
import Braze from "@braze/react-native-sdk";

const cachedCards = await Braze.getCachedContentCards();
```

Braze 서버에서 Content Cards를 수동으로 새로고침하려면:

```javascript
Braze.requestContentCardsRefresh();
```

{% endtab %}
{% endtabs %}

## 이벤트 로깅 {#logging-events}

노출 횟수, 클릭, 해제와 같은 유용한 측정기준을 로깅하는 것은 빠르고 간단합니다. 커스텀 클릭 리스너를 설정하여 이러한 분석을 수동으로 처리할 수 있습니다.

{% tabs %}
{% tab 웹 %}

사용자가 카드를 확인할 때 [`logContentCardImpressions`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcontentcardimpressions)를 사용하여 노출 이벤트를 로깅합니다:

```javascript
import * as braze from "@braze/web-sdk";

braze.logContentCardImpressions([card1, card2, card3]);
```

사용자가 카드와 상호작용할 때 [`logContentCardClick`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcontentcardclick)을 사용하여 카드 클릭 이벤트를 로깅합니다:

```javascript
import * as braze from "@braze/web-sdk";

braze.logContentCardClick(card);
```

{% endtab %}
{% tab Android %}

[`BrazeManager`](https://github.com/braze-inc/braze-growth-shares-android-demo-app/blob/main/app/src/main/java/com/braze/advancedsamples/BrazeManager.kt)는 Content Cards 오브젝트 배열 목록과 같은 Braze SDK 종속성을 참조하여 [`Card`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html)를 가져와 Braze 로깅 메서드를 호출할 수 있습니다. `ContentCardable` 기본 클래스를 사용하면 `BrazeManager`에 데이터를 쉽게 참조하고 제공할 수 있습니다.

카드에 대한 노출 또는 클릭을 로깅하려면 각각 [`Card.logClick()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/log-click.html) 또는 [`Card.logImpression()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/log-impression.html)을 호출합니다.

특정 카드에 대해 Content Cards를 수동으로 로깅하거나 Braze에 "해제됨"으로 설정하려면 [`isDismissed`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/is-dismissed.html)를 사용합니다. 카드가 이미 해제됨으로 표시된 경우 다시 해제됨으로 표시할 수 없습니다.

커스텀 클릭 리스너를 만들려면 [`IContentCardsActionListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.listeners/-i-content-cards-action-listener/index.html)를 구현하는 클래스를 만들고 [`BrazeContentCardsManager`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.managers/-braze-content-cards-manager/index.html)에 등록합니다. 사용자가 Content Cards를 클릭할 때 호출되는 [`onContentCardClicked()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.listeners/-i-content-cards-action-listener/on-content-card-clicked.html) 메서드를 구현합니다. 그런 다음 Braze에 Content Cards 클릭 리스너를 사용하도록 지시합니다.

{% subtabs local %}
{% subtab Java %}

예시:

```java
BrazeContentCardsManager.getInstance().setContentCardsActionListener(new IContentCardsActionListener() {
  @Override
  public boolean onContentCardClicked(Context context, Card card, IAction cardAction) {
    return false;
  }

  @Override
  public void onContentCardDismissed(Context context, Card card) {

  }
});
```

{% endsubtab %}
{% subtab Kotlin %}

예시:

```kotlin
BrazeContentCardsManager.getInstance().contentCardsActionListener = object : IContentCardsActionListener {
  override fun onContentCardClicked(context: Context, card: Card, cardAction: IAction): Boolean {
    return false
  }

  override fun onContentCardDismissed(context: Context, card: Card) {

  }
}
```

{% endsubtab %}
{% endsubtabs %}

{% alert important %}
커스텀 UI에서 컨트롤 배리언트 Content Cards를 처리하려면 [`com.braze.models.cards.Card`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html) 오브젝트를 전달한 다음 다른 Content Cards 유형과 마찬가지로 `logImpression` 메서드를 호출합니다. 이 오브젝트는 사용자가 컨트롤 카드를 확인했을 시점을 분석에 알리기 위해 암묵적으로 컨트롤 노출을 로깅합니다.{% endalert %}

{% endtab %}

{% tab Swift %}

[`BrazeContentCardUIViewControllerDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcarduiviewcontrollerdelegate) 프로토콜을 구현하고 델리게이트 오브젝트를 `BrazeContentCardUI.ViewController`의 `delegate` 속성으로 설정합니다. 이 델리게이트는 커스텀 오브젝트의 데이터를 Braze에 전달하여 로깅되도록 처리합니다. 예시는 [Content Cards UI 튜토리얼](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c2-contentcardsui/)을 참조하세요.

{% subtabs local %}
{% subtab Swift %}

```swift
// Set the delegate when creating the Content Cards controller
contentCardsController.delegate = delegate

// Method to implement in delegate
func contentCard(
    _ controller: BrazeContentCardUI.ViewController,
    shouldProcess clickAction: Braze.ContentCard.ClickAction,
    card: Braze.ContentCard
  ) -> Bool {
  // Intercept the content card click action here.
  return true
}
```

{% endsubtab %}
{% subtab Objective-C %}

```objc
// Set the delegate when creating the Content Cards controller
contentCardsController.delegate = delegate;

// Method to implement in delegate
- (BOOL)contentCardController:(BRZContentCardUIViewController *)controller
                shouldProcess:(NSURL *)url
                         card:(BRZContentCardRaw *)card {
  // Intercept the content card click action here.
  return YES;
}
```
{% endsubtab %}
{% endsubtabs %}

{% alert important %}
커스텀 UI에서 컨트롤 배리언트 Content Cards를 처리하려면 [`Braze.ContentCard.Control`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/control(_:)) 오브젝트를 전달한 다음 다른 Content Cards 유형과 마찬가지로 `logImpression` 메서드를 호출합니다. 이 오브젝트는 사용자가 컨트롤 카드를 확인했을 시점을 분석에 알리기 위해 암묵적으로 컨트롤 노출을 로깅합니다.
{% endalert %}
{% endtab %}

{% tab React Native %}

사용자가 카드를 확인할 때 노출 이벤트를 로깅합니다:

```javascript
Braze.logContentCardImpression(card.id);
```

사용자가 카드와 상호작용할 때 카드 클릭 이벤트를 로깅합니다:

```javascript
Braze.logContentCardClicked(card.id);
```

사용자가 카드를 해제할 때 해제 이벤트를 로깅합니다:

```javascript
Braze.logContentCardDismissed(card.id);
```

{% endtab %}
{% endtabs %}

## 클릭 시 동작 처리 {#handling-on-click-behavior}

{% tabs %}
{% tab 웹 %}

사용자가 커스텀 피드에서 콘텐츠 카드를 클릭하면, 클릭 시 동작(URL 이동, 딥링킹, 커스텀 이벤트 로깅 등)이 자동으로 처리되지 않습니다. [`handleBrazeAction`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#handlebrazeaction)을 사용하여 카드의 URL을 처리하고 Braze 액션(`brazeActions://` URL)을 포함한 구성된 클릭 시 동작을 실행합니다.

```javascript
import * as braze from "@braze/web-sdk";

// In your card click handler
function onCardClick(card) {
  // Log the click
  braze.logContentCardClick(card);

  // Handle the on-click behavior
  if (card.url) {
    braze.handleBrazeAction(card.url);
  }
}
```

| 매개변수 | 설명 |
|---|---|
| `url` | 유효한 URL 또는 `brazeActions://` 스킴을 사용하는 유효한 Braze 액션 URL입니다. |
| `openLinkInNewTab` | (선택 사항) URL을 새 탭에서 열지 여부입니다. 기본값은 `false`입니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="클릭 시 동작 처리" }

{% alert important %}
`handleBrazeAction()`을 호출하지 않으면, Braze 대시보드에서 구성한 클릭 시 동작(예: "커스텀 이벤트 로깅" 또는 "URL로 이동")이 커스텀 피드에 표시된 카드에서 실행되지 않습니다.
{% endalert %}

{% endtab %}
{% tab Android %}

클릭 시 동작은 기본 Content Cards UI에서 자동으로 처리됩니다. 커스텀 구현의 경우 **분석 로깅**에 설명된 [`IContentCardsActionListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.listeners/-i-content-cards-action-listener/index.html) 인터페이스를 사용합니다.

{% endtab %}
{% tab Swift %}

클릭 시 동작은 기본 Content Cards UI에서 자동으로 처리됩니다. 커스텀 구현의 경우 **분석 로깅**에 설명된 [`BrazeContentCardUIViewControllerDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcarduiviewcontrollerdelegate) 프로토콜을 사용합니다.

{% endtab %}
{% tab React Native %}

사용자가 커스텀 피드에서 콘텐츠 카드를 클릭하면, 클릭 시 동작이 자동으로 처리되지 않습니다. `Braze.logContentCardClicked(cardId)`로 클릭을 로깅한 후, `Braze.processContentCardClickAction(cardId)`를 호출하여 딥링크, URL 및 `brazeActions://` 액션을 처리합니다. 메서드 참조는 [React Native Content Cards]({{site.baseurl}}/developer_guide/content_cards/?sdktab=react%20native)를 확인하세요.

```javascript
import Braze from "@braze/react-native-sdk";

function onCardPress(card) {
  Braze.logContentCardClicked(card.id);

  if (card.url) {
    Braze.processContentCardClickAction(card.id);
  }
}
```

{% alert important %}
`processContentCardClickAction()`을 호출하지 않으면, Braze 대시보드에서 구성한 클릭 시 동작이 커스텀 피드의 카드에서 실행되지 않습니다.
{% endalert %}

{% endtab %}
{% endtabs %}