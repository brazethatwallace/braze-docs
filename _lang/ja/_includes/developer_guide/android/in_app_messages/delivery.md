{% multi_lang_include developer_guide/prerequisites/android.md %}

## メッセージトリガー {#message-triggers}

### トリガーの種類 {#trigger-types}

アプリ内メッセージは、SDKが以下のカスタムイベントタイプのいずれかを記録した際に自動的にトリガーされます：`Any Purchase`、`Specific Purchase`、`Session Start`、`Custom Event`、および `Push Click`。なお、`Specific Purchase` および `Custom Event` トリガーには堅牢なプロパティフィルターも含まれています。

{% alert note %}
アプリ内メッセージは、APIまたはAPIイベントによってトリガーすることはできません。SDKによって記録されるカスタムイベントによってのみトリガーされます。ロギングの詳細については、[カスタムイベントのログ記録]({{site.baseurl}}/developer_guide/analytics/logging_events/)を参照してください。
{% endalert %}

### 配信セマンティクス {#delivery-semantics}

すべての適格なアプリ内メッセージは、ユーザーのセッション開始時にデバイスに配信されます。配信されると、SDKはアセットをプリフェッチするため、トリガー時にアセットが利用可能となり、表示の遅延を最小限に抑えます。トリガーイベントに複数の適格なアプリ内メッセージがある場合、最も優先度の高いメッセージのみが配信されます。

SDKのセッション開始セマンティクスについて詳しくは、[セッションのライフサイクル]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=android)を参照してください。

### レート制限 {#rate-limit}

デフォルトでは、SDKはトリガーされたアプリ内メッセージを30秒に1回にレート制限しています。

本番アプリでは、この値を10秒未満に設定しないでください。連続するアプリ内メッセージでユーザーが圧倒されるのを防ぐためです。テストやサンプルアプリのフローでは、5秒が一般的な設定です。

テスト用にこの間隔を `0` に設定することもできます。ただし、`0` 秒の間隔は複数のアプリ内メッセージを同時に表示させるものではありません。1つのメッセージがまだ表示されている場合、現在のメッセージが閉じられるまで次のメッセージは表示されません。

この値をオーバーライドするには、`braze.xml` で `com_braze_trigger_action_minimum_time_interval_seconds` を次のように設定します。

```xml
  <integer name="com_braze_trigger_action_minimum_time_interval_seconds">5</integer>
```

## キーと値のペア {#key-value-pairs}

Brazeでキャンペーンを作成する際、キーと値のペアを `extras` として設定できます。これは、アプリ内メッセージングオブジェクトがアプリにデータを送信する際に使用できます。以下に例を示します。

{% tabs %}
{% tab JAVA %}
`````````java
Map<String, String> getExtras()
```
{% endtab %}
{% tab KOTLIN %}
`````````kotlin
extras: Map<String, String>
```
{% endtab %}
{% endtabs %}

{% alert note %}
詳細については、[KDoc](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message/index.html#1498425856%2FProperties%2F-1725759721)を参照してください。
{% endalert %}

## 自動トリガーを無効にする {#disabling-automatic-triggers}

アプリ内メッセージが自動的にトリガーされるのを防ぐには、以下の手順に従います。

1. 自動統合初期化機能を使用していることを確認してください。この機能は、バージョン `2.2.0` 以降でデフォルトで有効になっています。
2. 次の行を `braze.xml` ファイルに追加することで、アプリ内メッセージ操作のデフォルトを `DISCARD` に設定します。

`````````xml
<string name="com_braze_flutter_automatic_integration_iam_operation">DISCARD</string>
```

## 手動でメッセージをトリガーする {#manually-triggering-messages}

デフォルトでは、アプリ内メッセージはSDKがカスタムイベントを記録したときに自動的にトリガーされます。ただし、以下の方法で手動でメッセージをトリガーすることもできます。

### サーバー側のイベントを使用する {#using-a-server-side-event}

サーバー送信イベントを使用してアプリ内メッセージをトリガーするには、サイレントプッシュ通知をデバイスに送信し、カスタムプッシュコールバックがSDKベースのイベントを記録できるようにします。このイベントが、その後ユーザー向けのアプリ内メッセージをトリガーします。

#### ステップ 1: サイレントプッシュを受信するプッシュコールバックを作成する {#step-1-create-a-push-callback-to-receive-the-silent-push}

特定のサイレントプッシュ通知をリッスンするために、[カスタムプッシュイベントコールバック]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=android#push-callback)を登録します。

以下の例では、アプリ内メッセージを配信するために2つのイベントが記録されます。1つはサーバーから、もう1つはカスタムプッシュコールバック内から記録されます。同じイベントが重複しないようにするため、プッシュコールバック内から記録されるイベントは、サーバー送信イベントと同じ名前ではなく、「アプリ内メッセージトリガーイベント」などの一般的な命名規則に従う必要があります。そうしないと、単一のユーザーアクションに対して重複イベントが記録され、セグメンテーションとユーザーデータに影響を与える可能性があります。

{% tabs %}
{% tab JAVA %}

`````````java
Braze.getInstance(context).subscribeToPushNotificationEvents(event -> {
  final Bundle kvps = event.getNotificationPayload().getBrazeExtras();
  if (kvps.containsKey("IS_SERVER_EVENT")) {
    BrazeProperties eventProperties = new BrazeProperties();

    // The campaign name is a string extra that clients can include in the push
    String campaignName = kvps.getString("CAMPAIGN_NAME");
    eventProperties.addProperty("campaign_name", campaignName);
    Braze.getInstance(context).logCustomEvent("IAM Trigger", eventProperties);
  }
});
```

{% endtab %}
{% tab KOTLIN %}

`````````kotlin
Braze.getInstance(applicationContext).subscribeToPushNotificationEvents { event ->
    val kvps = event.notificationPayload.brazeExtras
    if (kvps.containsKey("IS_SERVER_EVENT")) {
        val eventProperties = BrazeProperties()

        // The campaign name is a string extra that clients can include in the push
        val campaignName = kvps.getString("CAMPAIGN_NAME")
        eventProperties.addProperty("campaign_name", campaignName)
        Braze.getInstance(applicationContext).logCustomEvent("IAM Trigger", eventProperties)
    }
}
```

{% endtab %}
{% endtabs %}

#### ステップ 2: プッシュキャンペーンを作成する {#step-2-create-a-push-campaign}

サーバー送信イベントを介してトリガーされる[サイレントプッシュキャンペーン]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=android)を作成します。

![]({% image_buster /assets/img_archive/serverSentPush.png %})

プッシュキャンペーンには、このプッシュキャンペーンがSDKカスタムイベントを記録するために送信されることを示すキーと値のペアのエクストラを含める必要があります。このイベントはアプリ内メッセージをトリガーするために使用されます。

![2組のキーと値のペア：IS_SERVER_EVENTが「true」に設定され、CAMPAIGN_NAMEが「example campaign name」に設定されている。]({% image_buster /assets/img_archive/kvpConfiguration.png %}){: style="max-width:70%;" }

前出のプッシュコールバックサンプルコードは、キーと値のペアを認識して、適切なSDKカスタムイベントを記録します。

「アプリ内メッセージトリガー」イベントに添付するイベントプロパティを含めたい場合は、プッシュペイロードのキーと値のペアでプロパティを渡すことで実現できます。この例では、後続のアプリ内メッセージのキャンペーン名が含められています。カスタムプッシュコールバックは、カスタムイベントを記録する際に、イベントプロパティのパラメーターとして値を渡すことができます。

#### ステップ 3: アプリ内メッセージキャンペーンを作成する {#step-3-create-an-in-app-message-campaign}

Brazeダッシュボードで、ユーザーに表示されるアプリ内メッセージキャンペーンを作成します。このキャンペーンにはアクションベースの配信を設定し、カスタムプッシュコールバック内から記録されたカスタムイベントからトリガーされるようにする必要があります。

以下の例では、イベントプロパティを最初のサイレントプッシュの一部として送信することで、トリガーされる特定のアプリ内メッセージが設定されています。

![アクションベースの配信キャンペーンで、「campaign_name」が「IAM campaign name example」と等しい場合にアプリ内メッセージがトリガーされる。]({% image_buster /assets/img_archive/iam_event_trigger.png %})

アプリがフォアグラウンドにないときにサーバー送信イベントが記録されると、イベントは記録されますが、アプリ内メッセージは表示されません。アプリケーションがフォアグラウンドになるまでイベントを遅延させたい場合は、カスタムプッシュレシーバーにチェックを含めて、アプリがフォアグラウンドに入るまでイベントを無視または遅延させる必要があります。

### 事前定義されたメッセージを表示する {#displaying-a-pre-defined-message}

事前定義したアプリ内メッセージを手動で表示するには、以下の方法を使用します。

{% tabs %}
{% tab JAVA %}

`````````java
BrazeInAppMessageManager.getInstance().addInAppMessage(inAppMessage);
```

{% endtab %}
{% tab KOTLIN %}

`````````kotlin
BrazeInAppMessageManager.getInstance().addInAppMessage(inAppMessage)
```

{% endtab %}
{% endtabs %}

### リアルタイムでメッセージを表示する {#displaying-a-message-in-real-time}

ダッシュボードで利用できるのと同じカスタマイズオプションを使って、ローカルのアプリ内メッセージをリアルタイムで作成・表示することもできます。そのためには、以下のようにします。

{% tabs %}
{% tab JAVA %}

`````````java
// Initializes a new slideup type in-app message and specifies its message.
InAppMessageSlideup inAppMessage = new InAppMessageSlideup();
inAppMessage.setMessage("Welcome to Braze! This is a slideup in-app message.");
```

{% endtab %}
{% tab KOTLIN %}

`````````kotlin
// Initializes a new slideup type in-app message and specifies its message.
val inAppMessage = InAppMessageSlideup()
inAppMessage.message = "Welcome to Braze! This is a slideup in-app message."
```

{% endtab %}
{% endtabs %}

{% alert important %}
ソフトキーボードが画面に表示されているときは、レンダリングが未定義となるため、アプリ内メッセージを表示しないでください。
{% endalert %}