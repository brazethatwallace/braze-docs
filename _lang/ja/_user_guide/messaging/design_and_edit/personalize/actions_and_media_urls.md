---
nav_title: アクションとメディアの URL
article_title: Liquid でアクションとメディアの URL をパーソナライズする
page_order: 2
description: "このリファレンス記事では、Liquid を使用してアクションとメディアの URL をパーソナライズする方法について説明します。"
---

# Liquid でアクションとメディアの URL をパーソナライズする {#personalize-action-and-media-urls-with-liquid}

> ボタン、リンク、画像、動画の URL に Liquid 変数を追加することで、メッセージを受信する各ユーザーに合わせてリンク先やコンテンツをパーソナライズできます。

## アプリ内コンテンツへのディープリンク {#deep-link-to-in-app-content}

{% alert tip %}
**開発者向け:** 統合手順については、[Android ディープリンク]({{site.baseurl}}/developer_guide/push_notifications/deep_linking?sdktab=android)または[Swift ディープリンク]({{site.baseurl}}/developer_guide/push_notifications/deep_linking?sdktab=swift)を参照してください。iOSリンクタイプの選択については、[iOS ディープリンクガイド]({{site.baseurl}}/developer_guide/push_notifications/ios_deep_linking_guide)を参照してください。問題の診断については、[ディープリンクのトラブルシューティング]({{site.baseurl}}/developer_guide/push_notifications/deep_linking_troubleshooting)を参照してください。
{% endalert %}

### ディープリンクとは {#what-is-deep-linking}

ディープリンクとは、ネイティブアプリを起動し、特定のアクションを実行したり特定のコンテンツを表示したりするための追加情報を提供する方法です。

これには3つの要素があります。

1. 起動するアプリを特定する。
2. 実行するアクションをアプリに指示する。
3. アクションに必要な追加データを提供する。

ディープリンクは、アプリの特定の部分にリンクするカスタムURIであり、これら3つの要素をすべて含んでいます。重要なのはカスタムスキームを定義することです。`http:` はほぼすべての人が馴染みのあるスキームですが、スキームは任意の単語で始めることができます。スキームは文字で始まる必要がありますが、その後は文字、数字、プラス記号、マイナス記号、またはドットを含めることができます。実際には、競合を防ぐための中央レジストリは存在しないため、スキームにドメイン名を含めることがベストプラクティスです。例えば、`twitter://` は旧Twitter（現X）のモバイルアプリを起動するためのiOS URIです。

ディープリンク内のコロン以降はすべて自由形式のテキストです。その構造と解釈はユーザーが定義します。ただし、一般的な慣例として `http:` URLをモデルにし、先頭の `//` やクエリパラメータ（例: `?foo=1&bar=2`）を含めます。前述の例では、`twitter://user?screen_name=[id]` を使用してアプリ内の特定のプロファイルを起動します。

{% alert important %}
ラッパーフレームワーク（FlutterやCordovaなど）で構築されたアプリの場合、Brazeはラッパー固有のディープリンクサポートを提供していません。ネイティブのiOSおよびAndroidレイヤーでディープリンクを設定する必要があります。Cordovaについては、[プッシュ通知でのディープリンク]({{site.baseurl}}/developer_guide/push_notifications/deep_linking?sdktab=cordova)を参照してください。
{% endalert %}

### システムURIスキーム {#system-uri-schemes}

iOSおよびAndroidでネイティブに処理される標準URIスキーム（`tel:`、`mailto:`、`sms:` など）は、アプリにカスタムディープリンク統合を必要とせず、ディープリンクURLフィールドに直接入力できます。

| スキーム | 例 | アクション |
| ------ | ------- | ------ |
| `tel:` | `tel:+18005555555` | 電話ダイヤラーを開く |
| `mailto:` | `mailto:support@example.com` | メール作成画面を開く |
| `sms:` | `sms:+18005555555` | SMS作成画面を開く |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="システムURIスキーム"}

これらはプッシュ通知のクリック時動作やアプリ内メッセージのボタンアクションで機能します。追加のSDK設定やアプリコードの変更は不要です。

### アプリケーションへのディープリンク {#deep-link-into-application}

プッシュ通知、アプリ内メッセージ、バナー、またはContent Cardsを作成する際に、**アプリケーションへのディープリンク**を選択して、アプリ内の特定の画面やアクションを開くことができます。一部のコンポーザーでは、このオプションは**Deep Link Into App**と表示されます。

このオプションを使用する前に、開発者と協力してURI形式を定義し、アプリがそれを開けるように設定してください。`myapp://` などのカスタムスキームは、インストール済みのアプリを直接開きます。ユニバーサルリンク（iOS）およびApp Links（Android）は `https://` URLを使用し、アプリがインストールされている場合はアプリを開き、インストールされていない場合はWebページにフォールバックします。

このクリック時動作を設定するには:

1. キャンペーンまたはキャンバスコンポーザーで、**クリック時動作**を見つけます。
   - プッシュ通知とContent Cardsの場合は、**作成**タブに移動します。
   - アプリ内メッセージの場合は、**作成**タブに移動します。ドラッグ＆ドロップエディターでは、ボタンまたは画像ブロックを選択し、そのプロパティパネルを開きます。
2. **アプリケーションへのディープリンク**または**Deep Link Into App**を選択します。
3. URLフィールドにリンクを入力します。例えば、カスタムスキームの場合は `myapp://products/12345`、ユニバーサルリンクまたはApp Linkの場合は `https://example.com/products/12345` です。
4. 物理デバイスにテストメッセージを送信します。テストが成功すると、アプリが開き、目的の画面またはアクションにルーティングされます。ユニバーサルリンクまたはApp Linkの場合は、アプリがインストールされていないデバイスでもテストして、期待されるWebフォールバックを確認してください。

### UTMタグとキャンペーンアトリビューション {#utm-tags-and-campaign-attribution}

#### UTMタグとは {#what-is-a-utm-tag}

[UTM（Urchin Traffic マネージャー）タグ](https://support.google.com/analytics/answer/10917952?sjid=14344007686729081565-NC#zippy=%2Cin-this-article)を使用すると、キャンペーンアトリビューションの詳細をリンクに直接含めることができます。UTMタグはGoogle Analyticsでキャンペーンアトリビューションデータを収集するために使用され、以下のプロパティを追跡できます。

- `utm_source`: トラフィックのソースの識別子（例: `my_app`）
- `utm_medium`: キャンペーンメディア（例: `newsfeed`）
- `utm_campaign`: キャンペーンの識別子（例: `spring_2016_campaign`）
- `utm_term`: ユーザーをアプリまたはWebサイトに誘導した有料検索キーワードの識別子（例: `pizza`）
- `utm_content`: ユーザーがクリックした特定のリンクまたはコンテンツの識別子（例: `toplink` または `android_iam_button2`）

UTMタグは、通常のHTTP（Web）リンクとディープリンクの両方に埋め込み、Google Analyticsで追跡できます。

##### UTMタグの計算 {#utm-tag-calculations}

Brazeはキャンペーンまたはキャンバスステップ内のすべてのリンクについて_合計クリック数_をレポートしますが、これにはUTMタグのないリンクも含まれる場合があります。そのため、Google Analyticsのキャンペーントラッキングリンクでは、キャンペーンパフォーマンスまたはレポートビルダーに表示される_合計クリック数_と比較して、異なる（多くの場合低い）結果が表示されることがあります。

#### BrazeでのUTMタグの使用 {#using-utm-tags-with-braze}

通常のHTTP（Web）リンクでUTMタグを使用する場合（例えば、メールキャンペーンのキャンペーンアトリビューションを行う場合）、組織がすでにGoogle Analyticsを使用しているなら、[GoogleのURLビルダー](https://ga-dev-tools.google/ga4/campaign-url-builder/)を使用してUTMリンクを生成できます。これらのリンクは、他のリンクと同様にBrazeキャンペーンのコピーに簡単に埋め込むことができます。

アプリへのディープリンクでUTMタグを使用するには、アプリに関連する[Google Analytics SDK](https://developers.google.com/analytics/devguides/collection/)が統合され、ディープリンクを処理するように正しく設定されている必要があります。不明な場合は開発者に確認してください。

Analytics SDKが統合および設定された後、BrazeキャンペーンのディープリンクでUTMタグを使用できます。キャンペーンのUTMタグを設定するには、送信先URLまたはディープリンクに必要なUTMタグを含めます。以下の例は、プッシュ通知とアプリ内メッセージでUTMタグを使用する方法を示しています。

##### UTMタグによるプッシュ開封とアプリ内メッセージクリックのアトリビューション {#attribute-push-opens-and-in-app-message-clicks-with-utm-tags}

{% tabs %}
{% tab プッシュ開封 %}

プッシュ通知のディープリンクにUTMタグを含めるには、プッシュメッセージのクリック時動作をディープリンクに設定し、ディープリンクアドレスを記述して、以下のように目的のUTMタグを含めます。

```
myapp://products/20-gift-card?utm_source=my_app&utm_medium=push&utm_campaign=spring2016giftcards&utm_content=ios_deeplink
```

![UTMタグによるプッシュ開封とアプリ内メッセージクリックのアトリビューションに関するスクリーンショット。]({% image_buster /assets/img_archive/push_utm_tags.png %})

{% endtab %}
{% tab アプリ内メッセージクリック %}

アプリ内メッセージのディープリンクにUTMタグを含めるには、以下を使用します。

```
myapp://products/20-gift-card?utm_source=my_app&utm_medium=iam&utm_campaign=spring2021giftcards&utm_content=web_link
```

![UTMタグによるプッシュ開封とアプリ内メッセージクリックのアトリビューションに関するスクリーンショット。]({% image_buster /assets/img_archive/iam_utm_tags.png %})

{% endtab %}
{% endtabs %}

## URLでLiquidパーソナライゼーションを使用する {#use-liquid-personalization-in-urls}

Brazeコンポーザー内でURLを動的に構築できるため、URLにダイナミックなUTMパラメーターを追加したり、ユーザーにユニークなリンクを送信したりできます（放棄カートや再入荷した特定の商品にユーザーを誘導するなど）。

### サポートされているLiquidパーソナライゼーションタグを使用してURLを作成する {#create-a-url-with-supported-liquid-personalization-tags}

[サポートされているLiquidパーソナライゼーションタグ]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags)を使用して、URLを動的に生成できます。

{% raw %}
```liquid
https://example.com/?campaign_utm={{campaign.${api_id}}}&user_attribute={{custom_attribute.${attribute1}}}
```
{% endraw %}

また、以下の例のように、カスタム定義されたLiquid変数の短縮もサポートしています。

### Liquid変数を使用してURLを作成する {#create-a-url-using-liquid-variables}

{% raw %}
```liquid
{% assign url_var = {{event_properties.${url_slug}}} %}
https://example.com/{{url_var}}
```
{% endraw %}

### Liquid変数によってレンダリングされたURLを短縮する {#shorten-urls-rendered-by-liquid-variables}

**サポートされているチャネル:** KakaoTalk、LINE、SMS、RCS、WhatsApp

LiquidによってレンダリングされたURLは、APIトリガープロパティに含まれるものも含めて短縮されます。たとえば、{% raw %}`{{api_trigger_properties.${url_value}}}`{% endraw %}が有効なURLを表す場合、メッセージを送信する前にそのURLを短縮してトラッキングします。

### `/messages/send`エンドポイントでURLを短縮する {#shorten-urls-in-messagessend-endpoint}

リンク短縮は、[`/messages/send`エンドポイント]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages)を介したAPI専用メッセージでも有効になります。リクエストパラメーターの完全なリストについては、[リクエストパラメーター]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages#request-parameters)を参照してください。

| パラメーター | 必須 | データ型 | 説明 |
| --------- | ---------| --------- | ----------- |
| `link_shortening_enabled` | はい | Boolean | リンク短縮を有効にするには、`link_shortening_enabled`を`true`に設定します。トラッキングを使用するには、`campaign_id`と`message_variation_id`が存在する必要があります。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="/messages/sendエンドポイントでURLを短縮する" }