---
nav_title: "チュートリアル: Content Cards受信トレイ"
article_title: "チュートリアル: Content Cardsを使った受信トレイの作成"
description: ""
page_order: 6
layout: scrolly
---

# チュートリアル: Content Cardsを使った受信トレイの作成 {#tutorial-making-an-inbox-with-content-cards}

> このチュートリアルのサンプルコードに沿って、BrazeのContent Cardsで受信トレイを構築しましょう。

{% sdktabs %}
{% sdktab android %}
{% multi_lang_include developer_guide/prerequisites/android.md %}

## Android（Compose）向けContent Cardsを使った受信トレイの作成 {#making-an-inbox-with-content-cards-for-android-compose}

{% multi_lang_include developer_guide/_shared/tutorial_feedback.md %}

{% scrolly %}

```kotlin file=MainApplication.kt
import android.app.Application
import com.braze.Braze
import com.braze.support.BrazeLogger
import com.braze.configuration.BrazeConfig
import android.util.Log

class ContentCardsApplication : Application() {
    override fun onCreate() {
        super.onCreate()

        // Turn on verbose Braze logging
        BrazeLogger.enableVerboseLogging()

        // Configure Braze with your SDK key & endpoint
        val config = BrazeConfig.Builder()
            .setApiKey("YOUR_API_KEY")
            .setCustomEndpoint("YOUR_API_ENDPOINT")
            .build()
        Braze.configure(this, config)
    }
}
```

```kotlin file=ContentCardsInboxScreen.kt
import android.content.Intent
import android.net.Uri
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.braze.Braze
import com.braze.events.ContentCardsUpdatedEvent
import com.braze.events.IEventSubscriber
import com.braze.models.cards.*

@Composable
fun ContentCardInboxScreen() {
    val context = LocalContext.current
    var cards by remember { mutableStateOf<List<Card>>(emptyList()) }
    val loggedImpressions = remember { mutableSetOf<String>() }

    DisposableEffect(Unit) {
        val subscriber = IEventSubscriber<ContentCardsUpdatedEvent> { event ->
            cards = event.allCards.filter { !it.isControl }
        }

        Braze.getInstance(context).subscribeToContentCardsUpdates(subscriber)
        Braze.getInstance(context).requestContentCardsRefresh(false)

        onDispose {
            Braze.getInstance(context)
                .removeSingleSubscription(subscriber, ContentCardsUpdatedEvent::class.java)
        }
    }

    Column(modifier = Modifier.fillMaxSize()) {
        Text(
            text = "Message Inbox",
            fontSize = 20.sp,
            fontWeight = FontWeight.Bold,
            modifier = Modifier.padding(start = 16.dp, end = 16.dp, top = 12.dp, bottom = 8.dp)
        )

        LazyColumn(
            modifier = Modifier
                .fillMaxSize()
                .padding(horizontal = 16.dp)
        ) {
            items(cards, key = { it.id }) { card ->
                ContentCardItem(
                    card = card,
                    onImpression = {
                        if (!loggedImpressions.contains(card.id)) {
                            card.logImpression()
                            loggedImpressions.add(card.id)
                        }
                    },
                    onClick = {
                        card.logClick()
                        card.url?.let {
                            context.startActivity(Intent(Intent.ACTION_VIEW, Uri.parse(it)))
                        }
                    }
                )
            }
        }
    }
}

@Composable
fun ContentCardItem(
    card: Card,
    onImpression: () -> Unit,
    onClick: () -> Unit
) {
    // Log impression when the card becomes visible
    LaunchedEffect(card.id) {
        onImpression()
    }

    val title = when (card) {
        is CaptionedImageCard -> card.title
        is ShortNewsCard -> card.title
        is TextAnnouncementCard -> card.title
        else -> null
    }
    val description = when (card) {
        is CaptionedImageCard -> card.description
        is ShortNewsCard -> card.description
        is TextAnnouncementCard -> card.description
        else -> null
    }

    Card(
        modifier = Modifier
            .fillMaxWidth()
            .padding(vertical = 4.dp)
            .clickable { onClick() }
    ) {
        Column(modifier = Modifier.padding(16.dp)) {
            title?.let {
                Text(
                    text = it,
                    fontWeight = FontWeight.Bold,
                    fontSize = 16.sp
                )
            }
            description?.let {
                Spacer(modifier = Modifier.height(4.dp))
                Text(
                    text = it,
                    fontSize = 14.sp
                )
            }
        }
    }
}
```

!!step
lines-MainApplication.kt=12

### 1. デバッグを有効にする（オプション） {#1-enable-debugging-optional}

開発中のトラブルシューティングを容易にするために、デバッグを有効にすることを検討してください。

!!step
lines-ContentCardsInboxScreen.kt=47-69

#### 2. UIビューを構築する {#2-build-a-ui-view}

Jetpack Composeでは、[`LazyColumn`](<https://developer.android.com/develop/ui/compose/lists#lazy>)を使用して、スクロール可能なリストにContent Cardsを表示します。

!!step
lines-ContentCardsInboxScreen.kt=25-37

#### 3. Content Cardsの更新をサブスクライブする {#3-subscribe-to-content-card-updates}

[`DisposableEffect`](<https://developer.android.com/develop/ui/compose/side-effects#disposableeffect>)を使用してサブスクリプションのライフサイクルを管理し、コンポーザブルがコンポジションから離脱する際に適切なクリーンアップを行います。

!!step
lines-ContentCardsInboxScreen.kt=84-95

#### 4. カスタム受信トレイUIを構築する {#4-build-a-custom-inbox-ui}

Content Cardsの[属性](<https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html>)（`title`、`description`、`url`など）を使用することで、特定のUI要件に合ったContent Cardsを作成できます。ここでは、Jetpack Composeの`Card`コンポーザブルと`Column`コンポーザブルを使って受信トレイを構築しています。

!!step
lines-ContentCardsInboxScreen.kt=57,62

#### 5. インプレッションとクリックをトラッキングする {#5-track-impressions-and-clicks}

Content Cards向けに用意されている[`logImpressions`](<https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/log-impression.html>)メソッドと[`logClick`](<https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/log-click.html>)メソッドを使って、インプレッションとクリックを記録できます。

インプレッションは、ユーザーがカードを閲覧した際に一度だけ記録する必要があります。`LaunchedEffect`を使用して、カードが表示されたときにインプレッションを記録します。アプリのビューライフサイクルやユースケースを考慮して、インプレッションが正しく記録されるようにする必要がある点にご注意ください。

{% endscrolly %}

## Android向けContent Cardsを使った受信トレイの作成（RecyclerView） {#making-an-inbox-with-content-cards-for-android-recyclerview}

{% scrolly %}

```kotlin file=MainApplication.kt
import android.app.Application
import com.braze.Braze
import com.braze.support.BrazeLogger
import com.braze.configuration.BrazeConfig
import android.util.Log

class ContentCardsApplication : Application() {
    override fun onCreate() {
        super.onCreate()

        // Turn on verbose Braze logging
        BrazeLogger.enableVerboseLogging()

        // Configure Braze with your SDK key & endpoint
        val config = BrazeConfig.Builder()
            .setApiKey("YOUR_API_KEY")
            .setCustomEndpoint("YOUR_API_ENDPOINT")
            .build()
        Braze.configure(this, config)
    }
}
```

```kotlin file=ContentCardInboxActivity.kt
import android.content.Intent
import android.net.Uri
import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import android.view.*
import android.widget.TextView
import com.braze.Braze
import com.braze.events.ContentCardsUpdatedEvent
import com.braze.events.IEventSubscriber
import com.braze.models.cards.*

class ContentCardsActivity : ComponentActivity() {
    private val cards = mutableListOf<Card>()
    private var subscriber: IEventSubscriber<ContentCardsUpdatedEvent>? = null
    private lateinit var recyclerView: RecyclerView
    private val adapter = ContentCardAdapter()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.content_card_inbox)

        recyclerView = findViewById(R.id.contentCardsRecyclerView)
        recyclerView.layoutManager = LinearLayoutManager(this)
        recyclerView.adapter = adapter

        // Prepare the subscriber (attach/detach in onStart/onStop)
        subscriber = IEventSubscriber { event ->
            runOnUiThread {
                cards.clear()
                cards.addAll(event.allCards.filter { !it.isControl })
                adapter.notifyDataSetChanged()
            }
        }
    }

    override fun onStart() {
        super.onStart()
        subscriber?.let {
            Braze.getInstance(this).subscribeToContentCardsUpdates(it)
        }
        // Fetch fresh cards
        Braze.getInstance(this).requestContentCardsRefresh(false)
    }

    override fun onStop() {
        // Avoid leaks by removing the subscription when not visible
        Braze.getInstance(this)
            .removeSingleSubscription(subscriber, ContentCardsUpdatedEvent::class.java)
        super.onStop()
    }

    inner class ContentCardAdapter :
        RecyclerView.Adapter<ContentCardAdapter.CardViewHolder>() {

        inner class CardViewHolder(v: View) : RecyclerView.ViewHolder(v) {
            val title: TextView = v.findViewById(android.R.id.text1)
            val description: TextView = v.findViewById(android.R.id.text2)
        }

        override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): CardViewHolder {
            val view = LayoutInflater.from(parent.context)
                .inflate(android.R.layout.simple_list_item_2, parent, false)
            return CardViewHolder(view)
        }

        override fun getItemCount() = cards.size

        override fun onBindViewHolder(holder: CardViewHolder, position: Int) {
            val card = cards[position]

            val title = when (card) {
                is CaptionedImageCard -> card.title
                is ShortNewsCard -> card.title
                is TextAnnouncementCard -> card.title
                else -> null
            }
            val description = when (card) {
                is CaptionedImageCard -> card.description
                is ShortNewsCard -> card.description
                is TextAnnouncementCard -> card.description
                else -> null
            }

            holder.title.text = title.orEmpty()
            holder.description.text = description.orEmpty()

            // Naive impression guard: only log the first time we bind a not-yet-viewed card.
            if (!card.viewed) card.logImpression()

            holder.itemView.setOnClickListener {
                card.logClick()
                card.url?.let { startActivity(Intent(Intent.ACTION_VIEW, Uri.parse(it))) }
            }
        }
    }
}
```

```xml file=content_card_inbox.xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
        android:orientation="vertical"
        android:layout_width="match_parent"
        android:layout_height="match_parent">

        <TextView
            android:id="@+id/inboxHeader"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:text="Message Inbox"
            android:textStyle="bold"
            android:textSize="20sp"
            android:paddingStart="16dp"
            android:paddingEnd="16dp"
            android:paddingTop="12dp"
            android:paddingBottom="8dp" />

        <androidx.recyclerview.widget.RecyclerView
            android:id="@+id/contentCardsRecyclerView"
            android:layout_width="match_parent"
            android:layout_height="0dp"
            android:layout_weight="1" />
    </LinearLayout>

```

!!step
lines-MainApplication.kt=12

### 1. デバッグを有効にする（オプション）

開発中のトラブルシューティングを容易にするために、デバッグを有効にすることを検討してください。

!!step
lines-content_card_inbox.xml=1-24

#### 2. UIビューを構築する

このチュートリアルでは、Androidの[`RecyclerView`](<https://developer.android.com/develop/ui/views/layout/recyclerview>)を使用してContent Cardsを表示しますが、ユースケースに合ったクラスやコンポーネントでUIを構築することをお勧めします。BrazeはデフォルトでUIを提供しますが、このチュートリアルでは外観と動作をカスタマイズするためのカスタムビューの作成方法を説明します。

!!step
lines-ContentCardInboxActivity.kt=29-35,40-42,44

#### 3. Content Cardsの更新をサブスクライブする

[`subscribeToContentCardsUpdates`](<https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/subscribe-to-content-cards-updates.html?query=abstract%20fun%20subscribeToContentCardsUpdates(subscriber:%20IEventSubscriber%3CContentCardsUpdatedEvent%3E)>)を使用して、新しいContent Cardsが利用可能になった際にUIが応答できるようにします。ここでは、サブスクライバーはアクティビティのライフサイクルフック内で登録および削除されます。

!!step
lines-ContentCardInboxActivity.kt=73-84

#### 4. カスタム受信トレイUIを構築する

Content Cardsの[属性](<https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html>)（`title`、`description`、`url`など）を使用することで、特定のUI要件に合ったContent Cardsを作成できます。ここでは、Androidのネイティブ`RecyclerView`を使って受信トレイを構築しています。

!!step
lines-ContentCardInboxActivity.kt=90,93

#### 5. インプレッションとクリックをトラッキングする

Content Cards向けに用意されている[`logImpressions`](<https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/log-impression.html>)メソッドと[`logClick`](<https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/log-click.html>)メソッドを使って、インプレッションとクリックを記録できます。

インプレッションは、ユーザーがカードを閲覧した際に一度だけ記録する必要があります。ここでは、カードごとのフラグを用いて重複ログを防ぐシンプルな仕組みを採用しています。アプリのビューライフサイクルやユースケースを考慮して、インプレッションが正しく記録されるようにする必要がある点にご注意ください。

{% endscrolly %}
{% endsdktab %}
{% sdktab swift %}
{% multi_lang_include developer_guide/prerequisites/swift.md %} また、[Swiftのアプリ内メッセージを有効にする]({{site.baseurl}}/developer_guide/in_app_messages?sdktab=swift#swift_enabling-in-app-messages)必要もあります。

## Swift向けContent Cardsを使った受信トレイの作成 {#making-an-inbox-with-content-cards-for-swift}

{% multi_lang_include developer_guide/_shared/tutorial_feedback.md %}

{% scrolly %}

```swift file=AppDelegate.swift
import SwiftUI
import BrazeKit
import BrazeUI

class AppDelegate: UIResponder, UIApplicationDelegate {
    static var braze: Braze!

    func application(
      _ application: UIApplication,
      didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
    ) -> Bool {

        // Braze configuration with your SDK API key and endpoint
        let configuration = Braze.Configuration(apiKey: "YOUR_API_ENDPOINT", endpoint: "YOUR_API_KEY")
        configuration.logger.level = .debug

        // Initialize Braze SDK instance
        AppDelegate.braze = Braze(configuration: configuration)

        return true
    }
}

struct InboxViewControllerRepresentable: UIViewControllerRepresentable {
    func makeUIViewController(context: Context) -> UINavigationController {
        let vc = BrazeInboxViewController(style: .plain)
        return UINavigationController(rootViewController: vc)
    }
    func updateUIViewController(_ uiViewController: UINavigationController, context: Context) {}
}

struct ContentView: View {
    var body: some View {
        NavigationView {
                InboxViewControllerRepresentable()
            .navigationTitle("Message Inbox")
        }
    }
}

```

```swift file=SampleApp.swift
import SwiftUI

@main
struct SampleApp: App {
    @UIApplicationDelegateAdaptor(AppDelegate.self) var delegate

    var body: some Scene {
        WindowGroup {
            ContentView()
        }
    }
}
```

```swift file=BrazeInboxView.swift
import SwiftUI
import UIKit
import BrazeKit

class BrazeInboxViewController: UITableViewController {
    private var cards: [Braze.ContentCard] = []
    private var subscription: Any?
    private var loggedImpressions = Set<String>()

    override func viewDidLoad() {
        super.viewDidLoad()
        tableView.register(UITableViewCell.self, forCellReuseIdentifier: "CardCell")
        tableView.rowHeight = 100

        subscription = AppDelegate.braze.contentCards.subscribeToUpdates { [weak self] updatedCards in
            self?.cards = updatedCards
            self?.tableView.reloadData()
        }

        AppDelegate.braze.contentCards.requestRefresh()
    }

    override func numberOfSections(in tableView: UITableView) -> Int { 1 }

    override func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        cards.count
    }

    override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let card = cards[indexPath.row]
        let cell = tableView.dequeueReusableCell(withIdentifier: "CardCell", for: indexPath)

        // Work with the content card's title and description
        cell.textLabel?.numberOfLines = 2
        cell.textLabel?.text = [card.title, card.description].compactMap { $0 }.joined(separator: "\n")

        return cell
    }

    override func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        let card = cards[indexPath.row]
        card.logClick(using: AppDelegate.braze)
        if let url = card.clickAction?.url {
            UIApplication.shared.open(url, options: [:], completionHandler: nil)
        }
        tableView.deselectRow(at: indexPath, animated: true)
    }

    override func tableView(_ tableView: UITableView,
                            willDisplay cell: UITableViewCell,
                            forRowAt indexPath: IndexPath) {
        let card = cards[indexPath.row]
        if !loggedImpressions.contains(card.id) {
            card.logImpression(using: AppDelegate.braze)
        }
    }
}
```

!!step
lines-AppDelegate.swift=15

### 1. デバッグを有効にする（オプション）

開発中のトラブルシューティングを容易にするために、デバッグを有効にすることを検討してください。

!!step
lines-BrazeInboxView.swift=5

#### 2. UIビューを構築する

このチュートリアルではSwiftの[`UITableViewController`](https://developer.apple.com/documentation/uikit/uitableviewcontroller)を使用しますが、ユースケースに合ったクラスやコンポーネントでUIを構築することをお勧めします。

!!step
lines-BrazeInboxView.swift=15-20

#### 3. Content Cardsの更新をサブスクライブする

Content Cardsリスナーをサブスクライブして最新の更新を受け取り、`requestRefresh()`を呼び出してそのユーザー向けの最新のContent Cardsをリクエストします。

!!step
lines-BrazeInboxView.swift=34-35

#### 4. カスタム受信トレイUIを構築する

Content Cardsの[`attributes`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard)（`title`、`description`、`imageUrl`など）を使用することで、特定のUI要件に合ったContent Cardsを作成できます。ここでは、SwiftのネイティブテーブルAPIを使って受信トレイを構築しています。

!!step
lines-BrazeInboxView.swift=8,43,49-56

#### 5. インプレッションとクリックをトラッキングする

コンテンツカード向けに用意されている[`logClick(using:)`](<https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/logclick(using:)/>)メソッドと[`logImpression(using:)`](<https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/logimpression(using:)/>)メソッドを使って、インプレッションとクリックを記録できます。

さらに、却下の記録には[`logDismissed(using:)`](<https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/logdismissed(using:)/>)も使用できます。

インプレッションは、ユーザーが閲覧した際に一度だけ記録する必要があります。ここでは、`Set`と`willDisplay`を使用したシンプルな仕組みでこれを実現しています。アプリのUIライフサイクルやユースケースを考慮して、インプレッションが正しく記録されるようにする必要がある点にご注意ください。

{% endscrolly %}
{% endsdktab %}
{% sdktab web %}
{% multi_lang_include developer_guide/prerequisites/web.md %} ただし、追加のセットアップは不要です。

## Web向けContent Cardsを使った受信トレイの作成 {#making-an-inbox-with-content-cards-for-web}

{% multi_lang_include developer_guide/_shared/tutorial_feedback.md %}

{% scrolly %}

```js file=main.js
import * as braze from "@braze/web-sdk";

// Uncomment this if you'd like to run braze web SDK methods in the console
// window.braze = braze;

// initialize the Braze SDK
braze.initialize("YOUR_API_KEY", {
  baseUrl: "YOUR_API_ENDPOINT",
  enableLogging: true,
});
braze.openSession();

// --- DOM refs ---
const listEl = document.getElementById("cards-list");

// --- State for impression de-duping & lookup ---
const loggedImpressions = new Set();
const idToCard = new Map();
let observer = null;

// Utility: clean observer between renders
function resetObserver() {
  if (observer) observer.disconnect();
  observer = new IntersectionObserver(onIntersect, { threshold: 0.6 });
}

// Intersection callback: logs impression once when ≥60% visible
function onIntersect(entries) {
  entries.forEach((entry) => {
    if (!entry.isIntersecting) return;

    const id = entry.target.dataset.cardId;
    if (!id || loggedImpressions.has(id)) return;

    const card = idToCard.get(id);
    if (!card) return;

    // Log a single-card impression and stop observing this element
    braze.logContentCardImpressions([card]);
    loggedImpressions.add(id);
    observer.unobserve(entry.target);
  });
}

// Renders cards into the DOM, sets up click + visibility tracking
function renderCards(cards) {
  // Rebuild lookup and observer each render
  idToCard.clear();
  resetObserver();

  listEl.textContent = ""; // clear list

  cards.forEach((card) => {
    // Skip control-group cards in UI; (optional) you could log impressions for them elsewhere
    if (card.isControl) return;

    idToCard.set(card.id, card);

    const item = document.createElement("article");
    item.className = "card-item";
    item.dataset.cardId = card.id;

    const h3 = document.createElement("h3");
    h3.textContent = card.title || "";

    const p = document.createElement("p");
    p.textContent = card.description || "";

    let img = undefined;
    if (card.imageUrl) {
      img = document.createElement("img");
      img.src = card.imageUrl;
      item.append(img);
    }

    const children = [h3, p];
    if (img) {
      children.push(img);
    }
    item.append(...children);

    // Click tracking + action
    item.addEventListener("click", (e) => {
      braze.logContentCardClick(card);
      if (card.url) {
        // any url-handling logic for your use case
      }
    });

    listEl.appendChild(item);
    observer.observe(item);
  });
}

// Subscribe to updates *then* ask for a refresh
braze.subscribeToContentCardsUpdates((updates) => {
  const cards = updates.cards || [];
  renderCards(cards);
});

braze.requestContentCardsRefresh();
```

```html file=index.html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <style>
      body {
        font-family: system-ui, -apple-system, Segoe UI, Roboto, Arial,
          sans-serif;
        margin: 0;
      }
      main {
        max-width: 720px;
        margin: 0 auto;
        padding: 16px;
      }
      h1 {
        margin: 0 0 12px;
        font-size: 24px;
      }
      .card-item {
        border-bottom: 1px solid #eee;
        padding: 12px 0;
        cursor: pointer;
      }
      .card-item h3 {
        margin: 0 0 6px;
        font-size: 16px;
      }
      .card-item p {
        margin: 0;
        color: #444;
      }
      .card-item img {
        max-width: 100%;
        height: auto;
      }
    </style>
  </head>
  <body>
    <main id="app">
      <h1>Message Inbox</h1>
      <div id="cards-list" aria-live="polite"></div>
    </main>

    <script type="module" src="/src/main.js"></script>
  </body>
</html>
```

!!step
lines-main.js=3-4,9

### 1. デバッグを有効にする（オプション）

開発中のトラブルシューティングを容易にするために、デバッグを有効にすることを検討してください。オプションとして、コンソールでBraze Web SDKのメソッドを実行することもできます。

!!step
lines-index.html=1-44

#### 2. UIを構築する {#2-build-the-ui}

受信トレイページのUIを作成します。ここでは、基本的なHTMLページを作成しています。このページには、`cards-list`というIDを持つ`div`が含まれています。これはContent Cardsをレンダリングするためのターゲットコンテナとして使用されます。

!!step
lines-main.js=96-99,101

#### 3. Content Cardsの更新をサブスクライブする

Content Cardsリスナーをサブスクライブして最新の更新を受け取り、[`requestContentCardsRefresh()`](<https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestcontentcardsrefresh>)を呼び出してそのユーザー向けの最新のContent Cardsをリクエストします。または、セッション開始時に自動更新を行うために、`openSession()`の前にサブスクライバーを呼び出すこともできます。

!!step
lines-main.js=64,67,70-74

#### 4. 受信トレイの要素を作成する {#4-build-the-inbox-elements}

Content Cardsの[属性](<https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.classiccard.html>)（`title`、`description`、`url`など）を使用することで、特定のUI要件に合わせてContent Cardsを表示できます。

!!step
lines-main.js=22-25,28-43,84,91

#### 5. インプレッションとクリックをトラッキングする

Content Cards向けに用意されている[`logContentCardImpressions`](<https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcontentcardimpressions>)メソッドと[`logContentCardClick`](<https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcontentcardclick>)メソッドを使って、インプレッションとクリックを記録できます。

さらに、却下の記録には[`logCardDismissal`](<https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcarddismissal>)も使用できます。

インプレッションは、ユーザーが閲覧した際に一度だけ記録する必要があります。ここでは、`IntersectionObserver`と`card.id`をキーとした`Set`を使用して重複ログを防止しています。アプリのUIライフサイクルやユースケースを考慮して、インプレッションが正しく記録されるようにする必要がある点にご注意ください。

{% endscrolly %}
{% endsdktab %}
{% endsdktabs %}