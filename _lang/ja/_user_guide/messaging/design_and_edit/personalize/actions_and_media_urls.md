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
**開発者向け:** カスタムスキーム、ユニバーサルリンク、その他のオプションの選択ガイド（AASA ファイルが必要な場合、実装すべきアプリデリゲートメソッド、デバッグ方法など）については、[iOS ディープリンクガイド]({{site.baseurl}}/developer_guide/push_notifications/ios_deep_linking_guide)および[ディープリンクのトラブルシューティング]({{site.baseurl}}/developer_guide/push_notifications/deep_linking_troubleshooting)を参照してください。
{% endalert %}

### ディープリンクとは {#what-is-deep-linking}

ディープリンクとは、ネイティブアプリを起動し、特定のアクションを実行したり特定のコンテンツを表示したりするための追加情報を提供する方法です。

これには3つの要素があります。

1. 起動するアプリを特定する。
2. 実行するアクションをアプリに指示する。
3. アクションに必要な追加データを提供する。

ディープリンクは、アプリの特定の部分にリンクするカスタム URI であり、これら3つの要素をすべて含みます。重要なのはカスタムスキームを定義することです。`http:` はほぼすべての人が知っているスキームですが、スキームは任意の単語で始めることができます。スキームは文字で始まる必要がありますが、その後は文字、数字、プラス記号、マイナス記号、ドットを含めることができます。実際には、競合を防ぐための中央レジストリは存在しないため、スキームにドメイン名を含めることがベストプラクティスです。例えば、`twitter://` はX（旧 Twitter）のモバイルアプリを起動するための iOS URI です。

ディープリンク内のコロン以降はすべて自由形式のテキストです。その構造と解釈は自由に定義できます。ただし、一般的な慣例として、先頭の `//` やクエリパラメーター（例: `?foo=1&bar=2`）を含む `http:` URL をモデルにすることが多いです。前述の例では、`twitter://user?screen_name=[id]` を使用してアプリ内の特定のプロフィールを起動します。

{% alert important %}
ラッパーフレームワーク（Flutter や Cordova など）で構築されたアプリの場合、Brazeはラッパー固有のディープリンクサポートを提供していません。ネイティブの iOS および Android レイヤーでディープリンクを設定する必要があります。Cordova については、[プッシュ通知でのディープリンク]({{site.baseurl}}/developer_guide/push_notifications/deep_linking?sdktab=cordova)を参照してください。
{% endalert %}

### UTM タグとキャンペーンアトリビューション {#utm-tags-and-campaign-attribution}

#### UTM タグとは {#what-is-a-utm-tag}

[UTM（Urchin Traffic Manager）タグ](https://support.google.com/analytics/answer/10917952?sjid=14344007686729081565-NC#zippy=%2Cin-this-article)を使用すると、キャンペーンアトリビューションの詳細をリンクに直接含めることができます。UTM タグは Google Analytics でキャンペーンアトリビューションデータを収集するために使用され、以下のプロパティを追跡できます。

- `utm_source`: トラフィックのソースの識別子（例: `my_app`）
- `utm_medium`: キャンペーンの媒体（例: `newsfeed`）
- `utm_campaign`: キャンペーンの識別子（例: `spring_2016_campaign`）
- `utm_term`: ユーザーをアプリまたはWebサイトに誘導した有料検索キーワードの識別子（例: `pizza`）
- `utm_content`: ユーザーがクリックした特定のリンクまたはコンテンツの識別子（例: `toplink` または `android_iam_button2`）

UTM タグは、通常の HTTP（Web）リンクとディープリンクの両方に埋め込むことができ、Google Analytics で追跡できます。

##### UTM タグの計算 {#utm-tag-calculations}

Brazeはキャンペーンまたはキャンバスステップ内のすべてのリンクの*合計クリック数*をレポートしますが、これには UTM タグが付いていないリンクも含まれる場合があります。そのため、Google Analytics のキャンペーントラッキングリンクでは、キャンペーンパフォーマンスやレポートビルダーに表示される*合計クリック数*と比較して、異なる（多くの場合低い）結果が表示されることがあります。

#### Brazeでの UTM タグの使用 {#using-utm-tags-with-braze}

通常の HTTP（Web）リンクで UTM タグを使用する場合（例えば、メールキャンペーンのキャンペーンアトリビューションを行う場合）、組織がすでに Google Analytics を使用しているなら、[Google の URL ビルダー](https://ga-dev-tools.google/ga4/campaign-url-builder/)を使用して UTM リンクを生成できます。これらのリンクは、他のリンクと同様にBrazeキャンペーンのコピーに簡単に埋め込むことができます。

アプリへのディープリンクで UTM タグを使用するには、アプリに関連する [Google Analytics SDK](https://developers.google.com/analytics/devguides/collection/) が統合され、ディープリンクを処理するように正しく設定されている必要があります。不明な場合は開発者に確認してください。

Analytics SDKが統合・設定された後、Brazeキャンペーンのディープリンクで UTM タグを使用できます。キャンペーンの UTM タグを設定するには、送信先 URL またはディープリンクに必要な UTM タグを含めます。以下の例では、プッシュ通知とアプリ内メッセージで UTM タグを使用する方法を示します。

##### UTM タグによるプッシュ開封とアプリ内メッセージクリックのアトリビューション {#attribute-push-opens-and-in-app-message-clicks-with-utm-tags}

{% tabs %}
{% tab プッシュ開封 %}

プッシュ通知のディープリンクに UTM タグを含めるには、プッシュメッセージのクリック時の動作をディープリンクに設定し、ディープリンクアドレスを記述して、以下のように必要な UTM タグを含めます。

```
myapp://products/20-gift-card?utm_source=my_app&utm_medium=push&utm_campaign=spring2016giftcards&utm_content=ios_deeplink
```

![UTM タグを使用したプッシュ開封とアプリ内メッセージクリックのアトリビューションに関するスクリーンショット。]({% image_buster /assets/img_archive/push_utm_tags.png %})

{% endtab %}
{% tab アプリ内メッセージクリック %}

アプリ内メッセージのディープリンクに UTM タグを含めるには、以下を使用します。

```
myapp://products/20-gift-card?utm_source=my_app&utm_medium=iam&utm_campaign=spring2021giftcards&utm_content=web_link
```

![UTM タグを使用したプッシュ開封とアプリ内メッセージクリックのアトリビューションに関するスクリーンショット。]({% image_buster /assets/img_archive/iam_utm_tags.png %})

{% endtab %}
{% endtabs %}

## URLでの Liquid パーソナライゼーションの使用 {#use-liquid-personalization-in-urls}

Brazeコンポーザー内で URL を動的に構築できるため、URL にダイナミックな UTM パラメーターを追加したり、ユーザーにユニークなリンクを送信したりできます（例えば、放棄カートや再入荷した特定の製品にユーザーを誘導するなど）。

### サポートされている Liquid パーソナライゼーションタグで URL を作成する {#create-a-url-with-supported-liquid-personalization-tags}

[サポートされている Liquid パーソナライゼーションタグ]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags)を使用して、URL を動的に生成できます。

{% raw %}
```liquid
https://example.com/?campaign_utm={{campaign.${api_id}}}&user_attribute={{custom_attribute.${attribute1}}}
```
{% endraw %}

カスタム定義の Liquid 変数の短縮もサポートしています。以下のセクションにいくつかの例を示します。

### Liquid 変数を使用して URL を作成する {#create-a-url-using-liquid-variables}

{% raw %}
```liquid
{% assign url_var = {{event_properties.${url_slug}}} %}
https://example.com/{{url_var}}
```
{% endraw %}

### Liquid 変数でレンダリングされた URL を短縮する {#shorten-urls-rendered-by-liquid-variables}

**サポートされているチャネル:** KakaoTalk、LINE、SMS、RCS、WhatsApp

Liquid でレンダリングされた URL は、API トリガープロパティに含まれるものも含めて短縮されます。例えば、{% raw %}`{{api_trigger_properties.${url_value}}}`{% endraw %} が有効な URL を表す場合、メッセージを送信する前にその URL を短縮してトラッキングします。

### `/messages/send` エンドポイントでの URL 短縮 {#shorten-urls-in-messagessend-endpoint}

リンク短縮は、[`/messages/send` エンドポイント]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages)を通じた API のみのメッセージでも有効になっています。リクエストパラメーターの完全なリストについては、[リクエストパラメーター]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages#request-parameters)を参照してください。

| パラメーター | 必須 | データタイプ | 説明 |
| --------- | ---------| --------- | ----------- |
| `link_shortening_enabled` | はい | ブール値 | リンク短縮を有効にするには、`link_shortening_enabled` を `true` に設定します。トラッキングを使用するには、`campaign_id` と `message_variation_id` が必要です。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="/messages/send エンドポイントでの URL 短縮" }