---
page_order: 2.2
nav_title: Content Cards
article_title: Content Cards
description: "データモデル、カードタイプ、カスタマイズオプションなど、Braze SDKでContent Cardsを実装する方法について説明します。"
channel:
  - content cards
platform:
  - Android
  - FireOS
  - Swift
  - Web
---

# Content Cards {#content-cards}

> アプリケーションで使用できるさまざまなデータモデルやカード固有のプロパティなど、Braze SDKのContent Cardsについて説明します。

{% multi_lang_include banners/content_card_alert.md %}

{% sdktabs %}
{% sdktab web %}
{% multi_lang_include developer_guide/web/content_cards.md %}
{% endsdktab %}

{% sdktab android %}
## 前提条件 {#prerequisites}

BrazeのContent Cardsを使用するには、[Braze Android SDK]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android)をアプリに統合する必要があります。ただし、追加のセットアップは不要です。

## Googleフラグメント {#google-fragments}

Androidでは、Content Cardsフィードは、Braze Android UIプロジェクトで利用可能な[フラグメント](https://developer.android.com/guide/components/fragments.html)として実装されています。[`ContentCardsFragment`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html)クラスは、Content Cardsのコンテンツを自動的に更新・表示し、使用状況の分析をログに記録します。ユーザーの`ContentCards`に表示されるカードは、Brazeダッシュボードで作成されます。

アクティビティにフラグメントを追加する方法については、[Googleのフラグメントドキュメント](https://developer.android.com/guide/fragments#Adding)を参照してください。

## カードのタイプとプロパティ {#card-types-and-properties}

Content CardsのデータモデルはAndroid SDKで利用可能で、以下の固有のContent Cardsタイプを提供します。各タイプはベースモデルを共有しており、ベースモデルから共通のプロパティを継承するとともに、独自のプロパティも持っています。完全なリファレンスドキュメントについては、[`com.braze.models.cards`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/index.html)を参照してください。

### ベースカードモデル {#base-card-for-android}

[ベースカード](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html)モデルは、すべてのカードの基本的な動作を提供します。

| プロパティ | 説明 |
|---|---|
| `getId()` | Brazeによって設定されたカードのIDを返します。|
| `getViewed()` | カードがユーザーによって既読か未読かを示すブール値を返します。|
| `getExtras()` | このカードのキーと値のエクストラのマップを返します。|
| `getCreated()` | Brazeからのカード作成時刻のUNIXタイムスタンプを返します。|
| `isPinned` | カードがピン留めされているかどうかを示すブール値を返します。|
| `getOpenUriInWebView()` | このカードのURIをBraze WebViewで開くかどうかを示す<br>ブール値を返します。|
| `getExpiredAt()` | カードの有効期限を取得します。|
| `isRemoved()` | エンドユーザーがこのカードを非表示にしたかどうかを示すブール値を返します。|
| `isDismissibleByUser()` | ユーザーがカードを非表示にできるかどうかを示すブール値を返します。|
| `isClicked()` | このカードのクリック状態を示すブール値を返します。|
| `isDismissed` | カードが非表示にされたかどうかを示すブール値を返します。カードを非表示としてマークするには`true`に設定します。すでに非表示としてマークされているカードは、再度非表示としてマークすることはできません。|
| `isControl()` | このカードがコントロールカードであり、レンダリングすべきでない場合にブール値を返します。|
{: .reset-td-br-1 .reset-td-br-2 aria-label="ベースカードモデル #base-card-for-android" }

### 画像のみ {#banner-image-card-for-android}

[画像のみカード](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-image-only-card/index.html)は、クリック可能なフルサイズの画像です。

| プロパティ | 説明 |
|---|---|
| `getImageUrl()` | カードの画像のURLを返します。|
| `getUrl()` | カードがクリックされた後に開かれるURLを返します。HTTP(s) URLまたはプロトコルURLの場合があります。|
| `getDomain()` | プロパティURLのリンクテキストを返します。|
{: .reset-td-br-1 .reset-td-br-2 aria-label="画像のみ #banner-image-card-for-android" }

### キャプション付き画像 {#captioned-image-card-for-android}

[キャプション付き画像カード](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-captioned-image-card/index.html)は、説明テキストが付いたクリック可能なフルサイズの画像です。

| プロパティ | 説明 |
|---|---|
| `getImageUrl()` | カードの画像のURLを返します。|
| `getTitle()` | カードのタイトルテキストを返します。|
| `getDescription()` | カードの本文テキストを返します。|
| `getUrl()` | カードがクリックされた後に開かれるURLを返します。HTTP(s) URLまたはプロトコルURLの場合があります。|
| `getDomain()` | プロパティURLのリンクテキストを返します。|
{: .reset-td-br-1 .reset-td-br-2 aria-label="キャプション付き画像 #captioned-image-card-for-android" }

### クラシック {#text-Announcement-card-for-android}

画像が含まれていないクラシックカードは、[テキストアナウンスメントカード](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-text-announcement-card/index.html)になります。画像が含まれている場合は、[ショートニュースカード](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-short-news-card/index.html)になります。

| プロパティ | 説明 |
|---|---|
| `getTitle()` | カードのタイトルテキストを返します。|
| `getDescription()` | カードの本文テキストを返します。|
| `getUrl()` | カードがクリックされた後に開かれるURLを返します。HTTP(s) URLまたはプロトコルURLの場合があります。|
| `getDomain()` | プロパティURLのリンクテキストを返します。|
| `getImageUrl()` | カードの画像のURLを返します。クラシックショートニュースカードにのみ適用されます。|
| `isDismissed` | カードが非表示にされたかどうかを示すブール値を返します。カードを非表示としてマークするには`true`に設定します。すでに非表示としてマークされているカードは、再度非表示としてマークすることはできません。|
{: .reset-td-br-1 .reset-td-br-2 aria-label="クラシック #text-Announcement-card-for-android" }

## カードメソッド {#card-methods}

すべての[`Card`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/index.html)データモデルオブジェクトは、ユーザーイベントをBrazeサーバーにログ記録するための以下の分析メソッドを提供します。

| メソッド | 説明 |
|---|---|
| `logImpression()` | 特定のカードのインプレッションをBrazeに手動でログ記録します。|
| `logClick()` | 特定のカードのクリックをBrazeに手動でログ記録します。|
{: .reset-td-br-1 .reset-td-br-2 aria-label="カードメソッド" }

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
## 前提条件

Content Cardsを使用するには、[Braze Swift SDK]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=swift)をアプリに統合してください。その後、tvOSアプリのセットアップ手順を完了します。

{% alert important %}
Content CardsはSwift SDKを使用したヘッドレスUIでサポートされており、tvOS用のデフォルトUIやビューは含まれていないため、独自のカスタムUIを実装してください。
{% endalert %}

## tvOSアプリのセットアップ {#setting-up-your-tvos-app}

### ステップ1:新しいiOSアプリを作成する {#step-1-create-a-new-ios-app}

Brazeで、**設定** > **アプリ設定**を選択し、**アプリを追加**を選択します。tvOSアプリの名前を入力し、**iOS**（_tvOSではありません_）を選択してから、**アプリを追加**を選択します。

![tvOSアプリを登録するためにiOSプラットフォームが選択されたBrazeのアプリ追加ダイアログ]({% image_buster /assets/img/tvos.png %}){: style="width:70%"}

{% alert warning %}
**tvOS**チェックボックスを選択すると、tvOS用のContent Cardsをカスタマイズできなくなります。
{% endalert %}

### ステップ2:アプリのAPIキーを取得する {#step-2-get-your-apps-api-key}

アプリ設定で、新しいtvOSアプリを選択し、アプリのAPIキーをメモします。このキーを使用して、Xcodeでアプリを設定します。

![SDK統合に使用されるAPIキーが表示されたtvOSアプリのアプリ設定]({% image_buster /assets/img/tvos1.png %}){: style="width:70%"}

### ステップ3:BrazeKitを統合する {#step-3-integrate-brazekit}

アプリのAPIキーを使用して、[Braze Swift SDK](https://github.com/braze-inc/braze-swift-sdk)をXcodeのtvOSプロジェクトに統合します。Braze Swift SDKからBrazeKitのみを統合する必要があります。

### ステップ4:カスタムUIを作成する {#step-4-create-your-custom-ui}

BrazeはtvOS上のContent Cards用のデフォルトUIを提供していないため、自分でカスタマイズしてください。詳細なウォークスルーについては、ステップバイステップのチュートリアル「[tvOS用Content Cardsのカスタマイズ](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/content-cards-customization/)」を参照してください。サンプルプロジェクトについては、[Braze Swift SDKサンプル](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples#contentcards-custom-ui)を参照してください。

{% endsdktab %}

{% sdktab unity %}
{% multi_lang_include developer_guide/unity/content_cards.md %}
{% endsdktab %}

{% sdktab .NET MAUI (Xamarin) %}
{% multi_lang_include developer_guide/xamarin/content_cards.md %}
{% endsdktab %}
{% endsdktabs %}