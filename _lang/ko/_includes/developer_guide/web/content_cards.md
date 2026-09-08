{% multi_lang_include archive/web-v4-rename.md %}

## 전제 조건 {#prerequisites}

Content Cards를 사용하려면 먼저 앱에 [Braze 웹 SDK를 연동]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web)해야 합니다. 추가 설정은 필요하지 않습니다. 자체 UI를 구축하려면 [Content Cards 커스터마이징 가이드]({{site.baseurl}}/developer_guide/content_cards)를 참조하세요.

{% alert note %}
일부 광고 차단기 및 브라우저 개인정보 보호 확장 프로그램은 Braze 웹 SDK 스크립트 또는 관련 네트워크 요청을 차단하여 Content Cards가 로드되지 않을 수 있습니다. CDN 연동 방식을 사용하고 있다면, SDK 라이브러리를 웹사이트에 로컬로 저장하여 광고 차단기 관련 문제를 방지할 수 있는 [NPM 연동 방식]({{site.baseurl}}/developer_guide/sdk_integration/?subtab=package%20manager&sdktab=web)으로 전환하는 것을 고려해 보세요.
{% endalert %}

## 표준 피드 UI {#standard-feed-ui}

포함된 Content Cards UI를 사용하려면 웹사이트에서 피드를 표시할 위치를 지정해야 합니다.

이 예시에서는 Content Cards 피드를 배치할 `<div id="feed"></div>`가 있습니다. 세 개의 버튼을 사용하여 피드를 숨기거나, 표시하거나, 토글(현재 상태에 따라 숨기기 또는 표시)할 수 있습니다.

```html

<button id="toggle" type="button">Toggle Cards Feed</button>
<button id="hide" type="button">Hide Cards Feed</button>
<button id="show" type="button">Show Cards Feed</button>

<nav>
    <h1>Your Personalized Feed</h1>
    <div id="feed"></div>
</nav>

<script>
   const toggle = document.getElementById("toggle");
   const hide = document.getElementById("hide");
   const show = document.getElementById("show");
   const feed = document.getElementById("feed");

   toggle.onclick = function(){
      braze.toggleContentCards(feed);
   }

   hide.onclick = function(){
      braze.hideContentCards();
   }

   show.onclick = function(){
      braze.showContentCards(feed);
   }
</script>
```

`toggleContentCards(parentNode, filterFunction)` 및 `showContentCards(parentNode, filterFunction)` 메서드를 사용할 때 인수가 제공되지 않으면 모든 Content Cards가 페이지의 고정 위치 사이드바에 표시됩니다. 그렇지 않으면 피드가 지정된 `parentNode` 옵션에 배치됩니다.

|매개변수 | 설명 |
|---|---|
| `parentNode` | Content Cards를 렌더링할 HTML 노드입니다. 부모 노드에 이미 Braze Content Cards 뷰가 직접 하위 요소로 존재하는 경우, 기존 Content Cards가 대체됩니다. 예를 들어 `document.querySelector(".my-container")`를 전달해야 합니다.|
| `filterFunction` | 이 뷰에 표시되는 카드의 필터 또는 정렬 함수입니다. `{pinned, date}` 기준으로 정렬된 `Card` 객체의 배열과 함께 호출됩니다. 이 사용자에게 렌더링할 정렬된 `Card` 객체의 배열을 반환해야 합니다. 생략하면 모든 카드가 표시됩니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="표준 피드 UI" }

Content Cards 토글에 대한 자세한 내용은 [SDK 참조 문서](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#togglecontentcards)를 참조하세요.

## 웹에서 Content Cards 테스트하기 {#testing-content-cards-on-the-web}

브라우저의 개발자 도구를 사용하여 Content Cards 통합을 테스트할 수 있습니다.

1. 콘텐츠 카드 Campaign을 생성하고 테스트 사용자를 타겟팅합니다.
2. 웹 SDK가 통합된 웹사이트에 로그인합니다.
3. 브라우저 콘솔을 엽니다. Chrome의 경우 페이지를 마우스 오른쪽 버튼으로 클릭하고 **검사**를 선택한 다음 **콘솔** 탭을 선택합니다.
4. 콘솔에서 다음 명령을 실행합니다:
   - `window.braze.getCachedContentCards()`
   - `window.braze.toggleContentCards()`

## 카드 유형 및 속성정보 {#card-types-and-properties}

Content Cards 데이터 모델은 웹 SDK에서 사용할 수 있으며 다음과 같은 Content Cards 유형을 제공합니다: [ImageOnly](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.imageonly.html), [CaptionedImage](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.captionedimage.html), [ClassicCard](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.classiccard.html). 각 유형은 기본 모델 [Card](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html)에서 공통 속성정보를 상속받으며 다음과 같은 추가 속성정보를 갖습니다.

{% alert tip %}
Content Cards 데이터를 기록하려면 [분석 로깅]({{site.baseurl}}/developer_guide/content_cards/logging_analytics)을 참조하세요.
{% endalert %}

### 기본 카드 모델 {#base-card-model}

모든 Content Cards에는 다음과 같은 공유 속성정보가 있습니다:

| 속성정보 | 설명 |
|---|---|
| `expiresAt` | 카드 만료 시간의 UNIX 타임스탬프입니다. |
| `extras` | (선택 사항) 값 문자열을 가진 문자열 객체 형식의 키-값 페어 데이터입니다. |
| `id` | (선택 사항) 카드의 ID입니다. 분석 목적으로 이벤트와 함께 Braze에 다시 보고됩니다. |
| `pinned` | 이 속성정보는 카드가 대시보드에서 "고정"으로 설정되었는지를 나타냅니다. |
| `updated` | 이 카드가 마지막으로 수정된 UNIX 타임스탬프입니다. |
| `viewed` | 이 속성정보는 사용자가 카드를 확인했는지 여부를 나타냅니다. |
| `isControl` | 이 속성정보는 카드가 A/B 테스트 내 "대조군" 그룹일 때 `true`입니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="기본 카드 모델" }

### 이미지 전용 {#image-only}

[ImageOnly](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.imageonly.html) 카드는 클릭 가능한 전체 크기 이미지입니다.

| 속성정보 | 설명 |
|---|---|
| `aspectRatio` | 카드 이미지의 종횡비이며 이미지 로딩이 완료되기 전의 힌트 역할을 합니다. 특정 상황에서는 이 속성정보가 제공되지 않을 수 있습니다. |
| `categories` | 이 속성정보는 커스텀 구현에서의 정리 용도로만 사용됩니다. 이러한 카테고리는 대시보드 작성기에서 설정할 수 있습니다. |
| `clicked` | 이 속성정보는 이 기기에서 카드가 클릭된 적이 있는지를 나타냅니다. |
| `created` | Braze에서 카드가 생성된 시간의 UNIX 타임스탬프입니다. |
| `dismissed` | 이 속성정보는 카드가 해제되었는지를 나타냅니다. |
| `dismissible` | 이 속성정보는 사용자가 카드를 해제하여 보기에서 제거할 수 있는지를 나타냅니다. |
| `imageUrl` | 카드 이미지의 URL입니다. |
| `linkText` | URL의 표시 텍스트입니다. |
| `url` | 카드를 클릭하면 열리는 URL입니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="이미지 전용" }

### 캡션 이미지 {#captioned-image}

[CaptionedImage](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.captionedimage.html) 카드는 설명 텍스트가 포함된 클릭 가능한 전체 크기 이미지입니다.

| 속성정보 | 설명 |
|---|---|
| `aspectRatio` | 카드 이미지의 종횡비이며 이미지 로딩이 완료되기 전의 힌트 역할을 합니다. 특정 상황에서는 이 속성정보가 제공되지 않을 수 있습니다. |
| `categories` | 이 속성정보는 커스텀 구현에서의 정리 용도로만 사용됩니다. 이러한 카테고리는 대시보드 작성기에서 설정할 수 있습니다. |
| `clicked` | 이 속성정보는 이 기기에서 카드가 클릭된 적이 있는지를 나타냅니다. |
| `created` | Braze에서 카드가 생성된 시간의 UNIX 타임스탬프입니다. |
| `dismissed` | 이 속성정보는 카드가 해제되었는지를 나타냅니다. |
| `dismissible` | 이 속성정보는 사용자가 카드를 해제하여 보기에서 제거할 수 있는지를 나타냅니다. |
| `imageUrl` | 카드 이미지의 URL입니다. |
| `linkText` | URL의 표시 텍스트입니다. |
| `title` | 이 카드의 제목 텍스트입니다. |
| `url` | 카드를 클릭하면 열리는 URL입니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="캡션 이미지" }

### 클래식 {#classic}

[ClassicCard](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.classiccard.html) 모델은 텍스트 없이 이미지만 포함하거나 이미지와 텍스트를 함께 포함할 수 있습니다.

| 속성정보 | 설명 |
|---|---|
| `aspectRatio` | 카드 이미지의 종횡비이며 이미지 로딩이 완료되기 전의 힌트 역할을 합니다. 특정 상황에서는 이 속성정보가 제공되지 않을 수 있습니다. |
| `categories` | 이 속성정보는 커스텀 구현에서의 정리 용도로만 사용됩니다. 이러한 카테고리는 대시보드 작성기에서 설정할 수 있습니다. |
| `clicked` | 이 속성정보는 이 기기에서 카드가 클릭된 적이 있는지를 나타냅니다. |
| `created` | Braze에서 카드가 생성된 시간의 UNIX 타임스탬프입니다. |
| `description` | 이 카드의 본문 텍스트입니다. |
| `dismissed` | 이 속성정보는 카드가 해제되었는지를 나타냅니다. |
| `dismissible` | 이 속성정보는 사용자가 카드를 해제하여 보기에서 제거할 수 있는지를 나타냅니다. |
| `imageUrl` | 카드 이미지의 URL입니다. |
| `linkText` | URL의 표시 텍스트입니다. |
| `title` | 이 카드의 제목 텍스트입니다. |
| `url` | 카드를 클릭하면 열리는 URL입니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="클래식" }

### 이미지 형식 {#image-formats}

Content Cards 이미지(GIF 포함)는 표준 HTML `<img>` 태그를 사용하여 렌더링됩니다. GIF 지원 여부는 사용자의 브라우저 기능에 따라 달라지며 최소 웹 SDK 버전을 요구하지 않습니다. 모든 최신 브라우저는 기본적으로 GIF 재생을 지원합니다.

## 대조군 {#control-group}

기본 Content Cards 피드를 사용하는 경우, 노출 횟수와 클릭은 자동으로 추적됩니다.

Content Cards에 커스텀 통합을 사용하는 경우, 대조군 카드가 표시되었을 때 [노출 횟수를 기록]({{site.baseurl}}/developer_guide/content_cards/logging_analytics)해야 합니다. 이 과정에서 A/B 테스트의 노출 횟수를 기록할 때 대조군 카드를 반드시 처리해야 합니다. 이 카드는 비어 있으며 사용자에게 표시되지 않지만, 비대조군 카드와의 성과를 비교하려면 노출 횟수를 기록해야 합니다.

콘텐츠 카드가 A/B 테스트의 대조군에 속하는지 확인하려면 `card.isControl` 속성정보(Web SDK v4.5.0+)를 확인하거나, 해당 카드가 `ControlCard` 인스턴스인지 확인합니다(`card instanceof braze.ControlCard`).

## 카드 메서드 {#card-methods}

### 기본 피드 메서드 {#default-feed-methods}

Braze 기본 피드 UI를 사용하여 Content Cards를 표시할 때 다음 메서드를 사용하세요:

|메서드 | 설명 |
|---|---|
|[`showContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showcontentcards)| 기본 Content Cards 피드를 표시합니다. 제공된 `parentNode` HTML 요소에 카드를 렌더링하거나, 요소가 지정되지 않은 경우 고정 위치 사이드바로 표시합니다. 표시 전에 카드를 정렬하거나 필터링하기 위한 선택적 `filterFunction`을 허용합니다. |
|[`hideContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#hidecontentcards)| 현재 표시 중인 기본 Content Cards 피드를 숨깁니다. |
|[`toggleContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#togglecontentcards)| 기본 Content Cards 피드가 숨겨져 있으면 표시하고, 표시되어 있으면 숨깁니다. 여러 Content Cards 피드를 동시에 표시해야 하는 경우 `showContentCards`와 `hideContentCards`를 대신 사용하세요. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="기본 피드 메서드" }

### 커스텀 피드 메서드 {#custom-feed-methods}

자체 Content Cards UI를 구축할 때 다음 메서드를 사용하세요:

|메서드 | 설명 |
|---|---|
|[`subscribeToContentCardsUpdates`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetocontentcardsupdates)| 현재 사용자의 Content Cards가 업데이트될 때마다(예: 세션 시작 시) 호출되는 콜백 함수를 등록합니다. 커스텀 피드에서 카드 데이터를 수신하는 기본 방법으로 사용하세요. 초기 세션에서 업데이트를 받으려면 `openSession()` 전에 호출해야 합니다. |
|[`getCachedContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#getcachedcontentcards)| 가장 최근 Content Cards 새로고침에서 현재 사용 가능한 모든 카드를 반환합니다. 새 서버 요청을 기다리지 않고 페이지 로드 시 즉시 카드를 표시하려면 이 메서드를 사용하세요. 예를 들어 활성 세션 중에 사용자가 페이지로 돌아오는 경우에 유용합니다. |
|[`requestContentCardsRefresh`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestcontentcardsrefresh)| Braze 서버에서 Content Cards의 즉시 새로고침을 요청합니다. 기본적으로 카드는 세션 시작 시와 기본 피드가 다시 열릴 때 새로고침됩니다. 특정 사용자 행동 후와 같이 다른 시점에 강제로 새로고침하려면 이 메서드를 사용하세요. [사용량 제한]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/feed#rate-limit)에 유의하세요. |
|[`logContentCardImpressions`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcontentcardimpressions)| 카드 배열에 대한 노출 이벤트를 기록합니다. 카드가 렌더링되어 사용자에게 표시될 때 호출하세요. 커스텀 UI를 사용할 때 정확한 캠페인 보고를 위해 필수이며, 기본 피드 외부에서는 노출이 자동으로 추적되지 않습니다. |
|[`logContentCardClick`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcontentcardclick)| 단일 카드에 대한 클릭 이벤트를 기록합니다. 커스텀 UI에서 사용자가 카드와 상호작용할 때 호출하세요. 정확한 캠페인 보고를 위해 필수이며, 기본 피드 외부에서는 클릭이 자동으로 추적되지 않습니다. |
|[`handleBrazeAction`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#handlebrazeaction)| 카드의 URL을 처리하고 Braze 액션(`brazeActions://` URL) 및 표준 URL 내비게이션을 포함한 구성된 클릭 시 동작을 실행합니다. Braze 대시보드에서 구성된 클릭 시 동작이 실행되도록 하려면 카드 클릭 핸들러에서 이 메서드를 호출하세요. |
|[`dismissCard`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html#dismisscard)| 프로그래밍 방식으로 카드를 해제하여 사용자 피드에서 제거합니다. 커스텀 UI에서 사용자가 카드를 해제할 수 있도록 하려면 이 메서드를 사용하세요. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="커스텀 피드 메서드" }

자세한 내용은 [SDK 참조 설명서](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html)를 참조하세요.

## 모범 사례 {#best-practices}

### 올바른 순서로 메서드 호출하기 {#call-methods-in-the-correct-order}

커스텀 피드의 경우, Content Cards는 `subscribeToContentCardsUpdates()`가 `openSession()` 전에 호출된 경우에만 세션 시작 시 새로고침됩니다. Braze 메서드를 다음 순서로 호출하세요:

```javascript
import * as braze from "@braze/web-sdk";

// Step 1: Initialize the SDK
braze.initialize("YOUR-API-KEY", { baseUrl: "YOUR-SDK-ENDPOINT" });

// Step 2: Subscribe to card updates
braze.subscribeToContentCardsUpdates((updates) => {
  const cards = updates.cards;
  renderCards(cards);
});

// Step 3: Identify the user
braze.changeUser("USER_ID");

// Step 4: Start the session
braze.openSession();
```

### 캐시된 카드를 사용하여 페이지 로드 간 콘텐츠 유지하기 {#use-cached-cards-to-persist-content-across-page-loads}

`subscribeToContentCardsUpdates()`는 새로운 업데이트(예: 세션 시작 시)가 있을 때만 콜백을 호출하므로, 사용자가 세션 중간에 페이지를 새로고침하면 커스텀 피드에서 카드가 사라질 수 있습니다. 이를 방지하려면 `getCachedContentCards()`를 사용하여 로컬 캐시에서 즉시 카드를 렌더링하고, 동시에 새로운 업데이트를 구독하세요:

```javascript
import * as braze from "@braze/web-sdk";

function renderCards(cards) {
  const container = document.getElementById("content-cards");
  container.textContent = "";
  const displayedCards = [];

  cards.forEach(card => {
    if (card instanceof braze.ClassicCard || card instanceof braze.CaptionedImage) {
      const cardElement = document.createElement("div");

      const h3 = document.createElement("h3");
      h3.textContent = card.title || "";
      cardElement.appendChild(h3);

      const p = document.createElement("p");
      p.textContent = card.description || "";
      cardElement.appendChild(p);

      if (card.imageUrl) {
        const img = document.createElement("img");
        img.src = card.imageUrl;
        img.alt = card.title || "";
        cardElement.appendChild(img);
      }

      if (card.url) {
        cardElement.addEventListener("click", () => {
          braze.logContentCardClick(card);
          braze.handleBrazeAction(card.url);
        });
      }

      container.appendChild(cardElement);
      displayedCards.push(card);
    }
  });

  if (displayedCards.length > 0) {
    braze.logContentCardImpressions(displayedCards);
  }
}

// Display cached cards immediately
const cached = braze.getCachedContentCards();
if (cached && cached.cards.length > 0) {
  renderCards(cached.cards);
}

// Subscribe to future updates
braze.subscribeToContentCardsUpdates((updates) => {
  renderCards(updates.cards);
});
```

### 커스텀 피드에 대한 분석 로깅 {#log-analytics-for-custom-feeds}

커스텀 UI를 사용하는 경우 노출 횟수, 클릭, 해제가 자동으로 추적되지 않습니다. 각 이벤트를 수동으로 로깅해야 합니다:

- **노출 횟수:** 카드가 사용자에게 표시될 때 카드 객체 배열을 사용하여 `logContentCardImpressions([card1, card2, ...])`를 호출합니다.
- **클릭:** 사용자가 카드와 상호작용할 때 `logContentCardClick(card)`를 호출합니다.
- **클릭 시 동작:** 카드에 설정된 클릭 시 동작(예: URL로 이동하거나 커스텀 이벤트 로깅)을 실행하려면 `handleBrazeAction(card.url)`을 호출합니다.

{% alert warning %}
`logContentCardClick()`에 전달되는 인수는 원본 Braze `Card` 객체여야 합니다. 카드 데이터를 변환하거나 재구성(예: 직렬화 및 역직렬화)한 경우, 클릭이 로깅되지 않으며 "card must be a Card object."라는 오류가 표시됩니다.
{% endalert %}

## Google Tag Manager 사용하기 {#using-google-tag-manager}

Google Tag Manager는 [Braze CDN]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup#install-cdn)(웹 SDK의 한 버전)을 웹사이트 코드에 직접 삽입하는 방식으로 작동합니다. 이는 Content Cards를 구현하는 경우를 제외하면, Google Tag Manager 없이 SDK를 직접 통합한 것과 동일하게 모든 SDK 메서드를 사용할 수 있다는 것을 의미합니다.

### Content Cards 설정하기 {#setting-up-content-cards}

{% tabs local %}
{% tab Google Tag Manager %}
Content Cards 피드의 표준 통합을 위해 Google Tag Manager에서 **커스텀 HTML** 태그를 사용할 수 있습니다. 다음 코드를 커스텀 HTML 태그에 추가하면 표준 Content Cards 피드가 활성화됩니다:

```html
<script>
   window.braze.showContentCards();
</script>
```

![Content Cards 피드를 표시하는 커스텀 HTML 태그의 Google Tag Manager 태그 구성.]({% image_buster /assets/img/web-gtm/gtm_content_cards.png %})
{% endtab %}

{% tab 수동 %}
Content Cards 및 피드의 외관을 자유롭게 커스터마이징하려면, Content Cards를 네이티브 웹사이트에 직접 통합할 수 있습니다. 이를 위해 표준 피드 UI를 사용하거나 커스텀 피드 UI를 만드는 두 가지 방법이 있습니다.

{% subtabs local %}
{% subtab 표준 피드 %}
[표준 피드 UI]({{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/integration#standard-feed-ui)를 구현할 때, Braze 메서드 앞에 `window.`를 추가해야 합니다. 예를 들어, `braze.showContentCards`는 `window.braze.showContentCards`로 작성해야 합니다.
{% endsubtab %}

{% subtab 커스텀 피드 %}
[커스텀 피드]({{site.baseurl}}/developer_guide/content_cards/creating_cards) 스타일링의 경우, GTM 없이 SDK를 통합한 것과 동일한 단계를 따릅니다. 예를 들어, Content Cards 피드의 너비를 커스터마이징하려면 CSS 파일에 다음 코드를 붙여넣으면 됩니다:

{% raw %}
```css
body .ab-feed {
    width: 800px;
}
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### 템플릿 업그레이드 {#upgrading}

Braze 웹 SDK의 최신 버전으로 업그레이드하려면, Google Tag Manager 대시보드에서 다음 세 단계를 수행합니다:

1. **태그 템플릿 업데이트**<br>워크스페이스의 **Templates** 페이지로 이동합니다. 업데이트가 가능한 경우 아이콘이 표시됩니다.<br><br>![업데이트가 가능함을 나타내는 Templates 페이지]({% image_buster /assets/img/web-gtm/gtm-update-available.png %})<br><br>해당 아이콘을 클릭하고 변경 사항을 검토한 후 **Accept Update**를 클릭합니다.<br><br>![이전 태그 템플릿과 새 태그 템플릿을 비교하는 화면에 "Accept Update" 버튼이 표시되어 있습니다.]({% image_buster /assets/img/web-gtm/gtm-accept-update.png %})<br><br>
2. **버전 번호 업데이트**<br>태그 템플릿이 업데이트되면, Braze 초기화 태그를 편집하고 SDK 버전을 최신 `major.minor` 버전으로 업데이트합니다. 예를 들어, 최신 버전이 `4.1.2`인 경우 `4.1`을 입력합니다. [체인지로그](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)에서 SDK 버전 목록을 확인할 수 있습니다.<br><br>![SDK 버전을 변경하는 입력 필드가 있는 Braze 초기화 템플릿]({% image_buster /assets/img/web-gtm/gtm-version-number.png %})<br><br>
3. **QA 및 배포**<br>태그 컨테이너에 업데이트를 게시하기 전에 Google Tag Manager의 [디버깅 툴](https://support.google.com/tagmanager/answer/6107056?hl=en)을 사용하여 새 SDK 버전이 제대로 작동하는지 확인합니다.

### 문제 해결 {#troubleshooting}

#### 태그 디버깅 활성화 {#debugging}

각 Braze 태그 템플릿에는 선택적인 **GTM Tag Debugging** 체크박스가 있으며, 이를 사용하여 웹 페이지의 JavaScript 콘솔에 디버그 메시지를 기록할 수 있습니다.

![Google Tag Manager의 디버그 도구]({% image_buster /assets/img/web-gtm/gtm-tag-debugging.png %})

#### 디버그 모드 진입 {#enter-debug-mode}

Google Tag Manager 통합을 디버그하는 또 다른 방법은 Google의 [미리보기 모드](https://support.google.com/tagmanager/answer/6107056) 기능을 사용하는 것입니다.

이 기능을 통해 웹 페이지의 데이터 레이어에서 트리거된 각 Braze 태그로 어떤 값이 전달되는지 확인할 수 있으며, 어떤 태그가 트리거되었는지 또는 트리거되지 않았는지도 파악할 수 있습니다.

![Braze 초기화 태그 요약 페이지에서 트리거된 태그 정보를 포함한 태그 개요를 제공합니다.]({% image_buster /assets/img/web-gtm/gtm-debug-mode.png %})

#### 커스텀 이벤트의 태그 순서 확인 {#tag-sequencing}

커스텀 이벤트나 기타 액션이 Braze에 기록되지 않는 경우, 일반적인 원인은 액션 태그(예: **Custom Event** 또는 **Purchase**)가 **Braze Initialization** 태그가 완료되기 전에 실행되는 경합 조건입니다. 이를 해결하려면 GTM에서 [태그 순서](https://support.google.com/tagmanager/answer/6238868)를 구성합니다:

1. 올바르게 기록되지 않는 액션 태그를 엽니다.
2. **Advanced Settings** > **Tag Sequencing**에서 **A tag that fires before \[this tag\]**를 선택합니다.
3. **Braze Initialization** 태그를 설정 태그로 선택합니다.

이렇게 하면 액션 태그가 Braze에 데이터를 전송하기 전에 SDK가 완전히 초기화됩니다.

#### 상세 로깅 활성화 {#enable-verbose-logging}

문제 해결을 위한 상세 로그를 캡처하려면, Google Tag Manager 통합에서 상세 로깅을 활성화할 수 있습니다. 이러한 로그는 브라우저의 [개발자 도구](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_are_browser_developer_tools) **Console** 탭에 표시됩니다.

Google Tag Manager 통합에서 Braze 초기화 태그로 이동하여 **Enable Web SDK Logging**을 선택합니다.

![웹 SDK 로깅 활성화 옵션이 켜져 있는 Braze 초기화 태그 요약 페이지.]({% image_buster /assets/img/web-gtm/gtm_verbose_logging.png %})

[changelog]: https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md