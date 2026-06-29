{% multi_lang_include developer_guide/prerequisites/android.md %} [プッシュ通知の設定]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android)も必要です。

## プッシュイベント用のコールバックを使用する {#push-callback}

Brazeには、プッシュ通知が受信されたとき、開かれたとき、または却下されたときのための[`subscribeToPushNotificationEvents()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/subscribe-to-push-notification-events.html)コールバックが用意されています。アプリケーションが実行されていないときに発生するイベントを見逃さないように、このコールバックを`Application.onCreate()`に配置することをお勧めします。

{% alert note %}
以前にアプリケーションでこの機能にカスタムブロードキャストレシーバーを使用していた場合は、この統合オプションを優先して、レシーバーを安全に削除できます。
{% endalert %}

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).subscribeToPushNotificationEvents(event -> {
  final BrazeNotificationPayload parsedData = event.getNotificationPayload();

  //
  // The type of notification itself
  //
  final boolean isPushOpenEvent = event.getEventType() == BrazePushEventType.NOTIFICATION_OPENED;
  final boolean isPushReceivedEvent = event.getEventType() == BrazePushEventType.NOTIFICATION_RECEIVED;
  // Sent when a user has dismissed a notification
  final boolean isPushDeletedEvent = event.getEventType() == BrazePushEventType.NOTIFICATION_DELETED;

  //
  // Notification data
  //
  final String pushTitle = parsedData.getTitleText();
  final Long pushArrivalTimeMs = parsedData.getNotificationReceivedTimestampMillis();
  final String deeplink = parsedData.getDeeplink();

  //
  // Custom KVP data
  //
  final String myCustomKvp1 = parsedData.getBrazeExtras().getString("my first kvp");
  final String myCustomKvp2 = parsedData.getBrazeExtras().getString("my second kvp");
});
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).subscribeToPushNotificationEvents { event ->
    val parsedData = event.notificationPayload

    //
    // The type of notification itself
    //
    val isPushOpenEvent = event.eventType == BrazePushEventType.NOTIFICATION_OPENED
    val isPushReceivedEvent = event.eventType == BrazePushEventType.NOTIFICATION_RECEIVED
    // Sent when a user has dismissed a notification
    val isPushDeletedEvent = event.eventType == BrazePushEventType.NOTIFICATION_DELETED

    //
    // Notification data
    //
    val pushTitle = parsedData.titleText
    val pushArrivalTimeMs = parsedData.notificationReceivedTimestampMillis
    val deeplink = parsedData.deeplink

    //
    // Custom KVP data
    //
    val myCustomKvp1 = parsedData.brazeExtras.getString("my first kvp")
    val myCustomKvp2 = parsedData.brazeExtras.getString("my second kvp")
}
```

{% endtab %}
{% endtabs %}

{% alert tip %}
通知アクションボタンを使用すると、`opens app`または`deep link`アクションを持つボタンがクリックされたときに`BRAZE_PUSH_INTENT_NOTIFICATION_OPENED`インテントが起動します。ディープリンクとエクストラの処理は変わりません。`close`アクション付きのボタンは`BRAZE_PUSH_INTENT_NOTIFICATION_OPENED`インテントを起動せず、通知を自動的に閉じます。
{% endalert %}

{% alert important %}
`Application.onCreate`でプッシュ通知リスナーを作成し、アプリが終了状態にある間にエンドユーザーが通知をタップした場合でもリスナーがトリガーされるようにしてください。
{% endalert %}

## 通知表示のカスタマイズ {#customization-display}

### ステップ 1:カスタム通知ファクトリーを作成する {#step-1-create-your-custom-notification-factory}

サーバー側では面倒な方法や利用できない方法でプッシュ通知をカスタマイズしたい場合があります。通知表示を完全に制御できるように、独自の[`IBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html)を定義してBrazeで表示する通知オブジェクトを作成する機能が追加されました。

カスタムの`IBrazeNotificationFactory`が設定されている場合、ユーザーに通知が表示される前に、プッシュ受信時にBrazeがファクトリーの`createNotification()`メソッドを呼び出します。Brazeは、Brazeプッシュデータを含む`Bundle`と、ダッシュボードまたはメッセージングAPI経由で送信されたカスタムのキーと値のペアを含む別の`Bundle`を渡します。

Brazeは、Brazeプッシュ通知からのデータを含む[`BrazeNotificationPayload`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.push/-braze-notification-payload/index.html)を渡します。

{% tabs %}
{% tab JAVA %}

```java
// Factory method implemented in your custom IBrazeNotificationFactory
@Override
public Notification createNotification(BrazeNotificationPayload brazeNotificationPayload) {
  // Example of getting notification title
  String title = brazeNotificationPayload.getTitleText();

  // Example of retrieving a custom KVP ("my_key" -> "my_value")
  String customKvp = brazeNotificationPayload.getBrazeExtras().getString("my_key");
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
// Factory method implemented in your custom IBrazeNotificationFactory
override fun createNotification(brazeNotificationPayload: BrazeNotificationPayload): Notification {
  // Example of getting notification title
  val title = brazeNotificationPayload.getTitleText()

  // Example of retrieving a custom KVP ("my_key" -> "my_value")
  val customKvp = brazeNotificationPayload.getBrazeExtras().getString("my_key")
}
```

{% endtab %}
{% endtabs %}

カスタムの`createNotification()`メソッドから`null`を返して通知をまったく表示しないことも、`BrazeNotificationFactory.getInstance().createNotification()`を使用してそのデータのデフォルトの`notification`オブジェクトを取得し、表示前に変更することも、完全に別個の`notification`オブジェクトを生成して表示することもできます。

{% alert note %}
Brazeのプッシュデータキーに関するドキュメントは、[Android SDK](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-constants/index.html)を参照してください。
{% endalert %}

### ステップ 2:カスタム通知ファクトリーを設定する {#step-2-set-your-custom-notification-factory}

Brazeにカスタム通知ファクトリーを使用するように指示するには、`setCustomBrazeNotificationFactory`メソッドを使用して[`IBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html)を設定します。

{% tabs %}
{% tab JAVA %}


```java
setCustomBrazeNotificationFactory(IBrazeNotificationFactory brazeNotificationFactory);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
setCustomBrazeNotificationFactory(brazeNotificationFactory: IBrazeNotificationFactory)
```

{% endtab %}
{% endtabs %}

カスタム`IBrazeNotificationFactory`を設定する場所として推奨されるのは、`Application.onCreate()`アプリケーションライフサイクルメソッド（アクティビティではない）です。これにより、アプリプロセスがアクティブなときはいつでも通知ファクトリーが正しく設定されます。

{% alert important %}
ゼロから独自の通知を作成するのは高度なユースケースであり、十分なテストとBrazeのプッシュ機能に対する深い理解がある場合にのみ行うべきです。たとえば、通知がプッシュ開封を正しくログに記録することを確認する必要があります。
{% endalert %}

カスタム[`IBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html)の設定を解除し、プッシュのデフォルトのBraze処理に戻すには、カスタム通知ファクトリーセッターに`null`を渡します。

{% tabs %}
{% tab JAVA %}


```java
setCustomBrazeNotificationFactory(null);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
setCustomBrazeNotificationFactory(null)
```

{% endtab %}
{% endtabs %}

## 多色テキストのレンダリング {#rendering-multicolor-text}

Braze SDKバージョン3.1.1では、HTMLをデバイスに送信することで、プッシュ通知内で多色テキストを表示できます。

![文字に複数の異なる色、斜体、背景色が指定されたAndroidプッシュメッセージ「Multicolor Push test message」。]({% image_buster /assets/img/multicolor_android_push.png %}){: style="max-width:40%;"}

この例は、以下のHTMLでレンダリングされます。

```html
<p><span style="color: #99cc00;">M</span>u<span style="color: #008080;">lti</span>Colo<span style="color: #ff6600;">r</span> <span style="color: #000080;">P</span><span style="color: #00ccff;">u</span><span style="color: #ff0000;">s</span><span style="color: #808080;">h</span></p>

<p><em>test</em> <span style="text-decoration: underline; background-color: #ff6600;"><strong>message</strong></span></p>
```

Androidでは、プッシュ通知内で有効なHTML要素やタグが制限されていることに注意してください。たとえば、`marquee`は使用できません。

{% alert important %}
多色テキストの表示はデバイス固有であり、Androidデバイスやバージョンによっては表示されない場合があります。
{% endalert %}

プッシュ通知で多色テキストを表示するには、`braze.xml`または`BrazeConfig`を更新します。

{% tabs local %}
{% tab braze.xml %}
`braze.xml`に以下を追加します。

```xml
<bool translatable="false" name="com_braze_push_notification_html_rendering_enabled">true</bool>
```
{% endtab %}

{% tab BrazeConfig %}
[`BrazeConfig`]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/runtime_configuration/#runtime-configuration)に以下を追加します。

{% subtabs local %}
{% subtab JAVA %}

```java
BrazeConfig brazeConfig = new BrazeConfig.Builder()
  .setPushHtmlRenderingEnabled(true)
  .build();
Braze.configure(this, brazeConfig);
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
val brazeConfig = BrazeConfig.Builder()
    .setPushHtmlRenderingEnabled(true)
    .build()
Braze.configure(this, brazeConfig)
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### サポートされているHTMLタグ {#supported-html-tags}

現在、GoogleはAndroid向けのサポート対象HTMLタグを公式ドキュメントに直接記載していません。この情報は[GitリポジトリのHtml.javaファイル](https://android.googlesource.com/platform/frameworks/base/+/master/core/java/android/text/Html.java)でのみ確認できます。以下の表を参照する際は、この情報がこのファイルから抽出されたものであり、サポートされているHTMLタグは変更される可能性があることに留意してください。

<table aria-label="サポートされているHTMLタグ">
  <thead>
    <tr>
      <th>カテゴリー</th>
      <th>HTMLタグ</th>
      <th>説明</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="7">基本的なテキストの書式設定</td>
      <td><code>&lt;b&gt;</code>、<code>&lt;strong&gt;</code></td>
      <td>太字テキスト</td>
    </tr>
    <tr>
      <td><code>&lt;i&gt;</code>、<code>&lt;em&gt;</code></td>
      <td>斜体テキスト</td>
    </tr>
    <tr>
      <td><code>&lt;u&gt;</code></td>
      <td>下線テキスト</td>
    </tr>
    <tr>
      <td><code>&lt;s&gt;</code>、<code>&lt;strike&gt;</code>、<code>&lt;del&gt;</code></td>
      <td>取り消し線テキスト</td>
    </tr>
    <tr>
      <td><code>&lt;sup&gt;</code></td>
      <td>上付きテキスト</td>
    </tr>
    <tr>
      <td><code>&lt;sub&gt;</code></td>
      <td>下付きテキスト</td>
    </tr>
    <tr>
      <td><code>&lt;tt&gt;</code></td>
      <td>等幅テキスト</td>
    </tr>
    <tr>
      <td rowspan="3">サイズ／フォント</td>
      <td><code>&lt;big&gt;</code>、<code>&lt;small&gt;</code></td>
      <td>相対的なテキストサイズの変更</td>
    </tr>
    <tr>
      <td><code>&lt;font color="..."&gt;</code></td>
      <td>前景色を設定</td>
    </tr>
    <tr>
      <td><code>&lt;span&gt;</code>（インラインCSS付き）</td>
      <td>インラインスタイル（色、背景など）</td>
    </tr>
    <tr>
      <td rowspan="4">段落とブロック</td>
      <td><code>&lt;p&gt;</code>、<code>&lt;div&gt;</code></td>
      <td>ブロックレベルのセクション</td>
    </tr>
    <tr>
      <td><code>&lt;br&gt;</code></td>
      <td>改行</td>
    </tr>
    <tr>
      <td><code>&lt;blockquote&gt;</code></td>
      <td>引用ブロック</td>
    </tr>
    <tr>
      <td><code>&lt;ul&gt;</code> + <code>&lt;li&gt;</code></td>
      <td>箇条書きリスト</td>
    </tr>
    <tr>
      <td>見出し</td>
      <td><code>&lt;h1&gt;</code> ～ <code>&lt;h6&gt;</code></td>
      <td>見出し（さまざまなサイズ）</td>
    </tr>
    <tr>
      <td rowspan="2">リンクと画像</td>
      <td><code>&lt;a href="..."&gt;</code></td>
      <td>クリック可能なリンク</td>
    </tr>
    <tr>
      <td><code>&lt;img src="..."&gt;</code></td>
      <td>インライン画像</td>
    </tr>
    <tr>
      <td>その他のインライン</td>
      <td><code>&lt;em&gt;</code>、<code>&lt;strong&gt;</code>、<code>&lt;dfn&gt;</code>、<code>&lt;cite&gt;</code></td>
      <td>斜体や太字の同義語</td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="サポートされているHTMLタグ" }

## インライン画像のレンダリング {#rendering-inline-images}

### 仕組み {#how-it-works}

Androidのプッシュ通知では、インライン画像プッシュを使用して大きな画像を表示できます。このデザインにより、ユーザーは画像を拡大するために手動でプッシュを展開する必要がなくなります。通常のAndroidプッシュ通知とは異なり、インライン画像プッシュの画像は3:2のアスペクト比です。

![]({% image_buster /assets/img/android/push/inline_image_push_android_1.png %}){: style="max-width:50%;"}

### 互換性 {#compatibility}

インライン画像はどのデバイスにも送信できますが、最低バージョンを満たさないデバイスやSDKでは代わりに標準画像が表示されます。インライン画像が正しく表示されるには、Android Braze SDK v10.0.0以上と、Android M以降を搭載したデバイスの両方が必要です。画像をレンダリングするには、SDKも有効にする必要があります。

{% alert note %}
Android 12を実行しているデバイスでは、カスタムプッシュ通知スタイルの変更によりレンダリングが異なります。
{% endalert %}

### インライン画像プッシュの送信 {#sending-an-inline-image-push}

Androidプッシュメッセージを作成する場合、この機能は**通知タイプ**ドロップダウンで使用できます。

![プッシュCampaignエディターで、標準のプッシュプレビューの上部に位置する「通知タイプ」ドロップダウンの場所を示している。]({% image_buster /assets/img/android/push/android_inline_image_notification_type.png %})

## 設定 {#settings}

Brazeダッシュボードから送信されるAndroidプッシュ通知には、多くの高度な設定が利用可能です。この記事では、これらの機能とそれらを効果的に使用する方法について説明します。

![]({% image_buster /assets/img_archive/android_advanced_settings.png %})

### 通知ID {#notification-id}

**通知ID**は、選択したメッセージカテゴリの一意の識別子です。そのIDからの最新のメッセージのみを尊重するようメッセージングサービスに通知する役割を果たします。通知IDを設定すると、古くて無関係なメッセージのスタックではなく、最新で関連性の高いメッセージだけを送信できます。

### Firebase メッセージング配信の優先度 {#fcm-priority}

[Firebase Messaging Delivery Priority](https://firebase.google.com/docs/cloud-messaging/android/message-priority#setting-priority-for-messages)フィールドでは、「通常」または「高」のどちらの優先度でプッシュをFirebase Cloud Messagingに送信するかを制御できます。

### 有効時間（TTL） {#ttl}

**有効時間**（TTL）フィールドを使用すると、プッシュメッセージングサービスでメッセージを保存する期間をカスタム設定できます。有効時間のデフォルト値は、FCMの場合は4週間、ADMの場合は31日です。

### 要約テキスト {#summary-text}

要約テキストを使用すると、拡張通知ビューに追加のテキストを設定できます。画像付きの通知のキャプションとしても機能します。

![Androidの通知で、タイトルが「This is the title for the notification.」、要約テキストが「This is the summary text for the notification.」のもの。]({% image_buster /assets/img/android/push/collapsed-android-notification.png %}){: style="max-width:65%;"}

要約テキストは、展開されたビューのメッセージ本文の下に表示されます。

![Androidの通知で、タイトルが「This is the title for the notification.」、要約テキストが「This is the summary text for the notification.」のもの。]({% image_buster /assets/img/android/push/expanded-android-notification.png %}){: style="max-width:65%;"}

画像を含むプッシュ通知の場合、折りたたまれたビューにはメッセージテキストが表示され、通知が展開されると、要約テキストが画像のキャプションとして表示されます。

### カスタムURI {#custom-uri}

**カスタムURI**機能を使用すると、通知がクリックされたときの誘導先Web URLまたはAndroidリソースを指定できます。カスタムURIが指定されていない場合、通知をクリックするとユーザーはアプリに誘導されます。カスタムURIを使用してアプリ内でディープリンクし、アプリ外部のリソースにユーザーを誘導することができます。この設定は、[メッセージングAPI]({{site.baseurl}}/api/endpoints/messaging/)またはダッシュボードのプッシュコンポーザーの**詳細設定**から行うことができます。

![Brazeプッシュコンポーザーのディープリンクの高度な設定。]({% image_buster /assets/img_archive/deep_link.png %})

### 通知の表示優先度 {#notification-priority}

{% alert important %}
通知の表示優先度設定は、Android O以降を実行しているデバイスでは使用されなくなりました。新しいデバイスの場合は、[通知チャネル設定](https://developer.android.com/training/notify-user/channels#importance)を使用して優先度を設定します。
{% endalert %}

プッシュ通知の優先度レベルは、通知トレイ内で他の通知と比較して通知がどのように表示されるかに影響します。また、通常のメッセージや優先度の低いメッセージは、バッテリー寿命を延ばすためにわずかに遅延が長くなったりバッチ処理で送信されたりするのに対し、優先度の高いメッセージは常に即座に送信されるため、配信の速度と方法にも影響する可能性があります。

Android Oでは、通知の優先度が通知チャネルのプロパティになりました。開発者と協力して設定中にチャネルの優先度を定義し、ダッシュボードを使用して通知音を送信するときに適切なチャネルを選択する必要があります。Android O以前のバージョンを実行するデバイスでは、BrazeダッシュボードとメッセージングAPIを通じてAndroid通知の優先度レベルを指定することが可能です。

特定の優先度でユーザー群全体にメッセージを送信する場合、[通知チャネルの設定](https://developer.android.com/training/notify-user/channels#importance)を通じて優先度を間接的に指定し（O+デバイスを対象とする場合）、*さらに*ダッシュボードから個別の優先度を送信する（&#60;Oデバイスを対象とする場合）ことをお勧めします。

AndroidまたはFire OSプッシュ通知で設定できる優先度レベルは次のとおりです。

| 優先度 | 説明／使用目的 | `priority`値（APIメッセージ用） |
|----------|--------------------------|-------------------------------------|
| 最大      | 緊急または一刻を争うメッセージ | `2` |
| 高     | 友人からの新着メッセージなど、重要なコミュニケーション | `1` |
| デフォルト  | ほとんどの通知 - メッセージが他の優先度タイプのいずれにも明示的に該当しない場合に使用します | `0` |
| 低      | ユーザーに知ってもらいたいが、すぐに行動を起こす必要のない情報 | `-1` |
| 最小      | 文脈に応じた情報またはバックグラウンド情報 | `-2` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="通知の表示優先度" }

詳細については、Googleの[Android通知](http://developer.android.com/design/patterns/notifications.html)に関するドキュメントを参照してください。

### サウンド {#sounds}

Android Oでは、通知音は通知チャネルのプロパティになりました。開発者と協力して設定時にチャネルのサウンドを定義し、通知を送信するときにダッシュボードを使用して適切なチャネルを選択する必要があります。

Android Oより前のバージョンを実行しているデバイスの場合、Brazeを使用するとダッシュボードコンポーザーを通じて個々のプッシュメッセージのサウンドを設定できます。これを行うには、デバイスのローカルサウンドリソースを指定します（例：`android.resource://com.mycompany.myapp/raw/mysound`）。このフィールドに「default」を指定すると、デフォルトの通知音がデバイスで再生されます。これは、[メッセージングAPI]({{site.baseurl}}/api/endpoints/messaging/)またはダッシュボードのプッシュコンポーザーの**詳細設定**で指定できます。

![Brazeプッシュコンポーザーのサウンドの高度な設定。]({% image_buster /assets/img_archive/sound_android.png %})

完全なサウンドリソースURI（例：`android.resource://com.mycompany.myapp/raw/mysound`）をダッシュボードプロンプトに入力します。

ユーザー群全体に特定のサウンドでメッセージを送信する場合、[通知チャネルの設定](https://developer.android.com/training/notify-user/channels)を通じてサウンドを間接的に指定し（O+デバイス向け）、*さらに*ダッシュボードから個別のサウンドを送信する（&#60;Oデバイス向け）ことをお勧めします。