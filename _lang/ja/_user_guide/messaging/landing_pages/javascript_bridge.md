---
nav_title: JavaScriptブリッジ
article_title: ランディングページ用JavaScriptブリッジ
page_order: 5
page_type: reference
description: "ランディングページのカスタムコードブロックからイベントのログ記録、カスタム属性の設定、Brazeアクションのトリガーを行うために、brazeBridge JavaScriptブリッジを使用する方法を説明します。"
---

# ランディングページ用JavaScriptブリッジ {#javascript-bridge-for-landing-pages}

> ランディングページは、カスタムコード（HTML、CSS、JavaScript）をBraze SDKと連携するためのJavaScript「ブリッジ」をサポートしています。

カスタムコードブロックで`brazeBridge`を使用してブリッジにアクセスし、訪問者がランディングページとインタラクションした際にイベントのログ記録、カスタム属性の設定、ユーザーの識別などを行えます。

## 仕組み {#how-it-works}

ランディングページでは、**カスタムコード**ブロックにカスタムHTML、CSS、JavaScriptを追加して、ページの外観、操作感、動作をより細かくコントロールできます。カスタムコードブロックでは、[JavaScriptブリッジ](#supported-methods)を使用してイベントのログ記録、カスタム属性の設定、ユーザーの識別などを行えます：
- カスタムイベントと購入のログ記録
- 標準およびカスタムユーザー属性の設定
- クリックとフォーム送信のトラッキング
- ユーザーの識別

アプリ内メッセージやバナーの`brazeBridge`コードを再利用する場合、ランディングページでもそのまま動作します。ランディングページに適用されないメソッドは無視され、エラーを発生させる代わりにブラウザコンソールに警告がログ記録されます。詳細については、[ランディングページでサポートされていないメソッド](#methods-not-supported-on-landing-pages)を参照してください。

{% alert important %}
ランディングページのブリッジは非同期であり、各メソッドはPromiseを返します。これは、メソッドが即座に返される[カスタムHTMLアプリ内メッセージブリッジ]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html#javascript-bridge)とは異なります。スクリプトの次のステップがブリッジ呼び出しの完了に依存する場合（ページのリダイレクト、フォームの送信、Brazeへのデータ送信など）、`await`または`.then()`を使用し、呼び出しが同期的に完了したと想定しないでください。
{% endalert %}

## ブリッジの利用可能性 {#bridge-availability}

訪問者がランディングページを開くと、`brazeBridge`は**カスタムコード**のJavaScript内ですでに利用可能です。ランディングページではブリッジメソッドを直接呼び出せます。アプリ内メッセージで`ab.BridgeReady`を使用するような別のreadyイベントを待つ必要はありません。

ブリッジオブジェクトが利用可能であっても、その訪問者に対してBraze SDKが初期化されているとは限りません。SDKは以下のいずれかの場合にランディングページ訪問時に初期化されます：

- 訪問者がBrazeチャネル（メール、SMS、プッシュなど）を通じて送信された[ランディングページLiquidタグ]({{site.baseurl}}/user_guide/messaging/landing_pages/tracking_users)経由でページを開いた場合。SDKはページの読み込み時に自動的に初期化されます。
- 訪問者がページのフォームを送信した場合（例えば、フォームデータを送信する**送信**ボタンをクリックした場合）。これには、[カスタムフォームブロック]({{site.baseurl}}/user_guide/messaging/landing_pages/custom_form_blocks)の`registerFormInput`コールバック内で行われた`brazeBridge`呼び出しも含まれます。これらはフォーム送信の一部として実行されるためです。

訪問者がランディングページLiquidタグなしでランディングページを直接開き、フォームを送信しなかった場合、そのページはBrazeにとって匿名であり、ブリッジメソッドの呼び出しは効果がありません。

{% alert note %}
`window.lpBridge`と`window.appboyBridge`は同じブリッジオブジェクトを参照しますが、どちらも非推奨です。`window.brazeBridge`を使用してください。
{% endalert %}

## 例 {#example}

メソッドは非同期であるため、順序や完了が重要な場合はasyncハンドラーを使用し、呼び出しを`await`してください：

```html
<button id="button">Set Favorite Color</button>
<script>
  document.querySelector("#button").onclick = async function () {
    // Track a click for analytics
    await brazeBridge.logClick("set-favorite-color");
    // Set the user's custom attribute
    await brazeBridge.getUser().setCustomUserAttribute("favorite color", "blue");
    // Track a custom event
    await brazeBridge.logCustomEvent("completed survey");
    // Send the enqueued data to Braze
    await brazeBridge.requestImmediateDataFlush();
  };
</script>
```

## サポートされているメソッド {#supported-methods}

以下の`brazeBridge`メソッドはPromiseを返し、ランディングページの**カスタムコード**ブロックでサポートされています。作業の順序付けや完了の保証が必要な場合は、`await`するか`.then()`を使用してください。

### トップレベルメソッド {#top-level-methods}

| メソッド | 説明 |
| --- | --- |
| `brazeBridge.changeUser(userId, signature?)` | 一意のIDでユーザーを識別します。 |
| `brazeBridge.logCustomEvent(eventName, eventProperties?)` | カスタムイベントをログに記録します。 |
| `brazeBridge.logPurchase(productId, price, currencyCode?, quantity?, purchaseProperties?)` | 購入をログに記録します。 |
| `brazeBridge.requestImmediateDataFlush(callback?)` | キューに入れられたデータをBrazeサーバーにフラッシュします。 |
| `brazeBridge.logClick(trackingId)` | 指定されたトラッキングIDでランディングページクリック（`lp_c`）をログに記録します。[クリックトラッキング](#click-tracking)を参照してください。 |
| `brazeBridge.logSubmit()` | ランディングページのフォーム送信（`lp_fs`）をログに記録します。ランディングページ固有のメソッドです。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="トップレベルメソッド" }

### `getUser()`メソッド {#getuser-methods}

{% alert note %}
`brazeBridge.getUser()`は同期的にプレーンオブジェクトを返すため、`getUser()`を`await`する必要はありません。返されたオブジェクトのメソッド（`getUser().setEmail(email)`など）がPromiseを返します。
{% endalert %}

`getUser()`は以下のユーザーメソッドを公開するオブジェクトを返します。各メソッドはPromiseを返します。

| メソッド | 説明 |
| --- | --- |
| `getUser().setFirstName(firstName)` | ユーザーの名を設定します。 |
| `getUser().setLastName(lastName)` | ユーザーの姓を設定します。 |
| `getUser().setEmail(email)` | ユーザーのメールアドレスを設定します。 |
| `getUser().setPhoneNumber(phoneNumber)` | ユーザーの電話番号を設定します。 |
| `getUser().setGender(gender: "m" \| "f" \| "o" \| "u" \| "n" \| "p")` | ユーザーの性別を設定します。それぞれ男性、女性、その他、不明、該当なし、回答しないを表します。 |
| `getUser().setDateOfBirth(year, month, day)` | ユーザーの生年月日を設定します。 |
| `getUser().setCountry(country)` | ユーザーの国を設定します。 |
| `getUser().setHomeCity(city)` | ユーザーの居住市区町村を設定します。 |
| `getUser().setLanguage(language)` | ユーザーの言語を設定します。 |
| `getUser().setCustomUserAttribute(key, value, merge?)` | カスタムユーザー属性を設定します。 |
| `getUser().addToCustomAttributeArray(key, value)` | カスタム属性配列に値を追加します。 |
| `getUser().removeFromCustomAttributeArray(key, value)` | カスタム属性配列から値を削除します。 |
| `getUser().incrementCustomUserAttribute(key, incrementValue?)` | 数値カスタム属性をインクリメントします。 |
| `getUser().setCustomLocationAttribute(key, latitude, longitude)` | カスタムロケーション属性を設定します。 |
| `getUser().addToSubscriptionGroup(subscriptionGroupId)` | メールまたはSMS購読グループにユーザーを追加します。 |
| `getUser().removeFromSubscriptionGroup(subscriptionGroupId)` | メールまたはSMS購読グループからユーザーを削除します。 |
| `getUser().setEmailNotificationSubscriptionType(type: "opted_in" \| "subscribed" \| "unsubscribed")` | メール通知の購読ステータスを設定します。 |
| `getUser().setPushNotificationSubscriptionType(type: "opted_in" \| "subscribed" \| "unsubscribed")` | プッシュ通知の購読ステータスを設定します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="getUser()メソッド" }

## クリックトラッキング {#click-tracking}

`brazeBridge.logClick(trackingId)`を使用して、ランディングページ上のクリックをトラッキングします。各呼び出しは、渡されたトラッキングIDでタグ付けされたランディングページクリックイベント（`lp_c`）をログに記録します：

```html
<a href="#" onclick="brazeBridge.logClick('cta-hero')">Get started</a>
```

{% alert note %}
ランディングページのクリックトラッキングは、「ボタン1」と「ボタン2」の慣例的なIDとして`logClick('0')`と`logClick('1')`を使用するアプリ内メッセージとは異なります。ランディングページには同等の特別なボタンIDはありません。すべての`logClick(trackingId)`呼び出しは、指定されたトラッキングIDをキーとする`lp_c`イベントをログに記録します。
{% endalert %}

## ランディングページでサポートされていないメソッド {#methods-not-supported-on-landing-pages}

以下のメソッドはアプリ内メッセージとバナーでは動作しますが、ランディングページではサポートされていません。ランディングページでこれらのメソッドを呼び出した場合、Brazeはその呼び出しを無視します。ページは引き続き動作しますが、ブラウザの開発者コンソールに警告が表示される場合があります。

| メソッド | 備考 |
| --- | --- |
| `brazeBridge.closeMessage()` | ランディングページには閉じるメッセージUIがありません。 |
| `brazeBridge.requestPushPermission(successCallback?, deniedCallback?)` | ランディングページからプッシュ許可はリクエストされません。 |
| `brazeBridge.web.registerAppboyPushMessages(successCallback?, deniedCallback?)` | ランディングページではWebプッシュ登録は利用できません。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ランディングページでサポートされていないメソッド" }

## 関連コンテンツ {#related-content}

- [カスタムフォームブロックの作成]({{site.baseurl}}/user_guide/messaging/landing_pages/custom_form_blocks)では、このブリッジのより高度な使用方法として、完全にカスタムなUIをランディングページフォームに接続する方法を説明しています。
- [ランディングページの作成]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages)