## React Native Content Cards 정보 {#about-react-native-content-cards}

Braze SDK에는 Content Cards를 시작할 수 있는 기본 카드 피드가 포함되어 있습니다. 카드 피드를 표시하려면 `Braze.launchContentCards()` 메서드를 사용할 수 있습니다. Braze SDK에 포함된 기본 카드 피드는 사용자의 Content Cards에 대한 모든 분석 추적, 해제 및 렌더링을 처리합니다.

{% multi_lang_include developer_guide/prerequisites/react_native.md %}

## 카드 메서드 {#cards-methods}

자체 UI를 구축하려면 사용 가능한 카드 목록을 가져오고 카드 업데이트를 수신 대기할 수 있습니다.

```javascript
// Set initial cards
const [cards, setCards] = useState([]);

// Listen for updates as a result of card refreshes, such as:
// a new session, a manual refresh with `requestContentCardsRefresh()`, or after the timeout period
Braze.addListener(Braze.Events.CONTENT_CARDS_UPDATED, async (update) => {
    setCards(update.cards);
});

// Manually trigger a refresh of cards
Braze.requestContentCardsRefresh();
```

{% alert important %}
카드를 표시할 자체 UI를 구축하려는 경우 해당 카드에 대한 분석을 수신하려면 `logContentCardImpression`을 호출해야 합니다. 여기에는 `control` 카드도 포함되며, 사용자에게 표시되지 않더라도 추적해야 합니다.
{% endalert %}

이러한 추가 메서드를 사용하여 앱 내에서 커스텀 Content Cards 피드를 구축할 수 있습니다.

| 메서드                                   | 설명                                                                                            |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| `launchContentCards()`                   | Content Cards UI 요소를 실행합니다.                                                                 |
| `requestContentCardsRefresh()`           | Braze SDK 서버에서 최신 Content Cards를 요청합니다. 결과 카드 목록은 이전에 등록된 각 [콘텐츠 카드 이벤트 리스너](#reactnative_cards-methods)로 전달됩니다. |
| `getCachedContentCards()`                | 캐시에서 가장 최근의 Content Cards 배열을 반환합니다.                                            |
| `logContentCardClicked(cardId)`          | 지정된 Content Card ID에 대한 클릭을 기록합니다. 이 메서드는 분석에만 사용됩니다. 클릭 동작을 실행하려면 `processContentCardClickAction(cardId)`도 추가로 호출하세요.                                                        |
| `logContentCardImpression(cardId)`       | 지정된 Content Card ID에 대한 노출을 기록합니다.                                                      |
| `logContentCardDismissed(cardId)`        | 지정된 Content Card ID에 대한 해제를 기록합니다.                                                        |
| `processContentCardClickAction(cardId)`  | 특정 카드의 동작을 수행합니다.                                                               |
{: .reset-td-br-1 .reset-td-br-2 aria-label="카드 메서드" }

## 카드 유형 및 속성정보 {#card-types-and-properties}

Content Cards 데이터 모델은 React Native SDK에서 사용할 수 있으며 다음과 같은 Content Cards 카드 유형을 제공합니다: [이미지 전용](#image-only), [캡션 이미지](#captioned-image), [클래식](#classic). 특정 카드의 대조군에 속하는 사용자에게 반환되는 특별한 [대조](#control) 카드 유형도 있습니다. 각 유형은 고유한 속성정보 외에도 기본 모델에서 공통 속성정보를 상속받습니다.

{% alert tip %}
Content Cards 데이터 모델에 대한 전체 참조는 [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/index.html) 및 [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard) 설명서를 참조하세요.
{% endalert %}

### 기본 카드 모델 {#base-card-model}

기본 카드 모델은 모든 카드에 대한 기초적인 동작을 제공합니다.

| 속성정보      | 설명                                                                                                            |
|--------------|------------------------------------------------------------------------------------------------------------------------|
| `id`          | Braze에서 설정한 카드의 ID입니다.                                                                                            |
| `created`     | Braze에서 카드가 생성된 시간의 unix 타임스탬프입니다.                                                             |
| `expiresAt`   | 카드 만료 시간의 unix 타임스탬프입니다. 값이 0보다 작으면 카드가 만료되지 않는다는 의미입니다.      |
| `viewed`      | 사용자가 카드를 읽었는지 또는 읽지 않았는지 여부입니다. 이는 분석을 기록하지 않습니다.                                           |
| `clicked`     | 사용자가 카드를 클릭했는지 여부입니다.                                                                         |
| `pinned`      | 카드가 고정되어 있는지 여부입니다.                                                                                            |
| `dismissed`   | 사용자가 이 카드를 해제했는지 여부입니다. 이미 해제된 카드를 해제된 것으로 표시하면 아무 작업도 수행되지 않습니다. |
| `dismissible` | 사용자가 카드를 해제할 수 있는지 여부입니다.                                                                           |
| `url`         | (선택 사항) 카드 클릭 동작과 연결된 URL 문자열입니다.                                                       |
| `openURLInWebView` | 이 카드의 URL을 Braze WebView에서 열어야 하는지 여부입니다.                                            |
| `isControl`   | 이 카드가 대조 카드인지 여부입니다. 대조 카드는 사용자에게 표시되지 않아야 합니다.                                |
| `extras`      | 이 카드의 키-값 추가 항목 맵입니다.                                                                             |
{: .reset-td-br-1 .reset-td-br-2 aria-label="기본 카드 모델" }

기본 카드에 대한 전체 참조는 [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html) 및 [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/data-swift.struct) 설명서를 참조하세요.

### 이미지 전용 {#image-only}

이미지 전용 카드는 클릭 가능한 전체 크기 이미지입니다.

| 속성정보           | 설명                                                                                                       |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
| `type`             | Content Card 유형, `IMAGE_ONLY`.                                                                              |
| `image`            | 카드 이미지의 URL입니다.                                                                                      |
| `imageAspectRatio` | 카드 이미지의 종횡비입니다. 이미지 로드가 완료되기 전에 힌트 역할을 합니다. 특정 상황에서는 속성정보가 제공되지 않을 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="이미지 전용" }

이미지 전용 카드에 대한 전체 참조는 [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-image-only-card/index.html) 및 [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/imageonly-swift.struct) 설명서를 참조하세요.

### 캡션 이미지 {#captioned-image}

캡션 이미지 카드는 클릭 가능한 전체 크기 이미지로, 설명 텍스트가 함께 제공됩니다.

| 속성정보           | 설명                                                                                                       |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
| `type`             | Content Card 유형, `CAPTIONED`.                                                                               |
| `image`            | 카드 이미지의 URL입니다.                                                                                      |
| `imageAspectRatio` | 카드 이미지의 종횡비입니다. 이미지 로드가 완료되기 전에 힌트 역할을 합니다. 특정 상황에서는 속성정보가 제공되지 않을 수 있습니다. |
| `title`            | 카드의 제목 텍스트입니다.                                                                                      |
| `cardDescription`  | 카드의 설명 텍스트입니다.                                                                                |
| `domain`           | (선택 사항) 속성정보 URL의 링크 텍스트(예: `"braze.com/resources/"`). 카드의 UI에 표시되어 카드를 클릭할 때의 동작과 방향을 나타낼 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="캡션 이미지" }

캡션 이미지 카드에 대한 전체 참조는 [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-captioned-image-card/index.html) 및 [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/captionedimage-swift.struct) 설명서를 참조하세요.

### 클래식 {#classic}

클래식 카드에는 텍스트 앞에 제목, 설명, 이미지(선택 사항)가 있습니다.

| 속성정보           | 설명                                                                                                       |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
| `type`             | Content Card 유형, `CLASSIC`.                                                                                 |
| `image`            | (선택 사항) 카드 이미지의 URL입니다.                                                                           |
| `title`            | 카드의 제목 텍스트입니다.                                                                                      |
| `cardDescription`  | 카드의 설명 텍스트입니다.                                                                                |
| `domain`           | (선택 사항) 속성정보 URL의 링크 텍스트(예: `"braze.com/resources/"`). 카드의 UI에 표시되어 카드를 클릭할 때의 동작과 방향을 나타낼 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="클래식" }

클래식(텍스트 알림) Content Card에 대한 전체 참조는 [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-text-announcement-card/index.html) 및 [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/classic-swift.struct) 설명서를 참조하세요. 클래식 이미지(짧은 뉴스) 카드에 대해서는 [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-short-news-card/index.html) 및 [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/classicimage-swift.struct) 설명서를 참조하세요.

### 대조 {#control}

대조 카드에는 몇 가지 중요한 차이점이 있는 모든 기본 속성정보가 포함됩니다. 특히 다음 사항이 중요합니다.

- `isControl` 속성정보는 `true`로 보장됩니다.
- `extras` 속성정보는 비어 있음이 보장됩니다.

대조 카드에 대한 전체 참조는 [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-control-card/index.html) 및 [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/control-swift.struct) 설명서를 참조하세요.