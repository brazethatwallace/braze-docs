---
nav_title: RudderStack
article_title: RudderStack
description: "この記事では、Brazeと、Android、iOS、WebアプリケーションにシームレスなBraze統合を提供するオープンソースの顧客データインフラであるRudderStackとのパートナーシップについて説明します。RudderStackを使用すると、アプリ内の顧客イベントデータをBrazeに直接送信し、文脈に応じた分析を行うことができます。"
page_type: partner
search_tag: Partner

---

# RudderStack

> [RudderStack](https://rudderstack.com/) は、顧客イベントデータを収集し、希望するデータウェアハウスやBrazeなどの他の多数の分析プロバイダーにルーティングするための、オープンソースの顧客データインフラです。エンタープライズ対応で、イベントデータを即座に処理するための強力な変換フレームワークを提供します。

BrazeとRudderStackの統合により、Android、iOS、およびWebアプリケーションのネイティブSDK統合と、バックエンドサービスからのサーバー間統合が提供されます。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| --- | --- |
| RudderStackアカウント | このパートナーシップを活用するには、[RudderStackアカウント](https://app.rudderstack.com/)が必要です。 |
| 設定済みのソース | [ソース](https://www.rudderstack.com/docs/dashboard-guides/sources/)とは、Webサイト、モバイルアプリ、バックエンドサーバーなど、RudderStackに送信されるあらゆるデータの発生元です。RudderStackでBrazeを送信先として設定する前に、ソースを設定する必要があります。 |
| Braze REST APIキー | `users.track`、`users.identify`、`users.delete`、`users.alias.new` の権限を持つBraze REST APIキー。<br><br>これはBrazeダッシュボードの**設定** > **APIキー**から作成できます。 |
| Brazeアプリキー | アプリキーを取得するには、Brazeダッシュボードで**設定** > **アプリ設定** > **識別情報**に移動し、アプリ名を見つけます。関連する識別子文字列を保存してください。 |
| データセンター | データセンターはBrazeダッシュボードの[インスタンス]({{site.baseurl}}/api/basics#endpoints)と対応しています。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## 統合 {#integration}

### ステップ 1:ソースを追加する {#step-1-add-a-source}

Brazeへのデータ送信を開始するには、まずRudderStackアプリでソースが設定されていることを確認する必要があります。データソースの設定方法については、[RudderStack](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#getting-started) を参照してください。

### ステップ 2:送信先を設定する {#step-2-configure-destination}

データソースの設定が完了したら、RudderStackダッシュボードで**Destinations**の下にある**ADD DESTINATION**を選択します。利用可能な送信先のリストから**Braze**を選択し、**Next**をクリックします。

Brazeの送信先で、アプリキー、Braze REST APIキー、データクラスター、ネイティブSDKオプション（デバイスモードのみ）を指定します。ネイティブSDKオプションをオンにすると、BrazeネイティブSDKを使用してイベントを送信します。

### ステップ 3:統合タイプを選択する {#step-3-choose-the-type-of-integration}

RudderStackのWebおよびネイティブクライアントサイドライブラリとBrazeの統合には、以下のいずれかのアプローチを選択できます。

- [サイドバイサイド / デバイスモード](#device-mode)**:** RudderStackがクライアント（ブラウザーまたはモバイルアプリケーション）からBrazeに直接イベントデータを送信します。
- [サーバー間 / クラウドモード](#cloud-mode)**:** Braze SDKがイベントデータをRudderStackに直接送信し、そのデータが変換されてBrazeにルーティングされます。
- [ハイブリッドモード](#hybrid-mode)**:** ハイブリッドモードを使用すると、iOSとAndroidの自動生成イベントおよびユーザー生成イベントを単一の接続でBrazeに送信できます。

{% alert note %}
RudderStackの[接続モード](https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/)と各モードの利点について、詳しくはこちらをご覧ください。
{% endalert %}

#### サイドバイサイド統合（デバイスモード） {#device-mode}

このモードでは、Webサイトまたはモバイルアプリに設定されたBraze SDKを使用してイベントを Brazeに送信できます。

[サポートされているメソッド](#supported-methods)の説明に従い、Braze GitHubリポジトリでプラットフォーム用のRudderStack SDKへのマッピングを設定します。

- [Android](https://github.com/rudderlabs/rudder-integration-braze-android)
- [iOS](https://github.com/rudderlabs/rudder-integration-braze-ios/tree/master)
- [Swift](https://github.com/rudderlabs/rudder-integration-braze-swift)
- [Web](https://github.com/rudderlabs/rudder-sdk-js/tree/develop/packages/analytics-js-integrations/src/integrations/Braze)
- [React Native](https://github.com/rudderlabs/rudder-sdk-react-native/tree/develop/libs/rudder-integration-braze-react-native)
- [Flutter](https://github.com/rudderlabs/rudder-sdk-flutter/tree/develop/packages/integrations/rudder_integration_braze_flutter)

デバイスモード統合を完了するには、[プロジェクトへのBrazeの追加](https://rudderstack.com/docs/destinations/marketing/braze/#adding-device-mode-integration)に関するRudderStackの詳細な手順を参照してください。

#### サーバー間統合（クラウドモード） {#cloud-mode}

このモードでは、SDKがイベントデータをRudderStackサーバーに直接送信します。RudderStackはこのデータを変換し、目的の送信先にルーティングします。この変換は、RudderStackのtransformerモジュールを使用してRudderStackバックエンドで実行されます。

統合を有効にするには、[サポートされているメソッド](#supported-methods)の説明に従って、RudderStackのメソッドをBrazeにマッピングする必要があります。

{% alert note %}
RudderStackのサーバーサイドSDK（Java、Python、Node.js、Go、Ruby）はクラウドモードのみをサポートしています。これは、サーバーサイドSDKがRudderStackバックエンドで動作し、Braze固有のSDKを読み込むことができないためです。
{% endalert %}

{% alert important %}
サーバー間統合は、プッシュ通知やアプリ内メッセージングなどのBraze UI機能をサポートしていません。ただし、これらの機能はデバイスモード統合ではサポートされています。
{% endalert %}

#### ハイブリッドモード {#hybrid-mode}

ハイブリッドモードを使用すると、iOSおよびAndroidソースからすべてのイベントをBrazeに送信できます。

ハイブリッドモードを選択してBrazeにイベントを送信すると、RudderStackは次のように動作します。
1. Braze SDKを初期化します。
2. すべてのユーザー生成イベント（identify、track、page、screen、group）をクラウドモードのみでBrazeに送信し、デバイスモードでの送信をブロックします。
3. 自動生成イベント（Braze SDKが必要なアプリ内メッセージ、プッシュ通知）をデバイスモードで送信します。

[ハイブリッドモードでイベントを送信する](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#send-events-in-hybrid-mode)には、ソースをBrazeの送信先に接続する際にハイブリッドモードオプションを使用します。その後、プロジェクトにBraze統合を追加します。

## ステップ4:追加設定を行う {#step-4-configure-additional-settings}

初期設定が完了したら、Brazeでデータを正しく受信するために以下の設定を行います。

- **Enable subscription groups in group call**:この設定を有効にすると、グループイベントで購読グループのステータスを送信できます。詳細については、[Group](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#group)を参照してください。
- **Use Custom Attributes Operation**:Brazeの[階層化カスタム属性]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects)機能を使用して、カスタム属性オブジェクトによるセグメントの作成やメッセージのパーソナライズを行いたい場合は、この設定を有効にします。詳細については、[Send user traits as nested custom attributes](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#send-user-traits-as-nested-custom-attributes)を参照してください。
- **Track events for anonymous users**:この設定を有効にすると、匿名ユーザーのアクティビティをトラッキングし、その情報をBrazeに送信できます。

### デバイスモード設定 {#device-mode-settings}

以下の設定は、[デバイスモード](https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode)でBrazeにイベントを送信する場合にのみ適用されます。

- **Client-side Events Filtering**:この設定では、Brazeに送信するイベントをブロックまたは許可するかを指定できます。この設定の詳細については、[Client-side Events Filtering](https://www.rudderstack.com/docs/sources/event-streams/sdks/event-filtering/)を参照してください。
- **Deduplicate Traits**:この設定を有効にすると、[`identify`](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#identify)コールでユーザー特性の重複が排除されます。
- **Show Braze logs**:この設定は、ソースとして[JavaScript SDK](https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/)を使用している場合にのみ適用されます。有効にすると、ユーザーにBrazeのログを表示します。
- **OneTrust Cookie Categories**:この設定では、[OneTrust](https://www.rudderstack.com/docs/sources/event-streams/sdks/onetrust/javascript/)のCookie同意グループをBrazeに関連付けることができます。

## サポートされるメソッド {#supported-methods}

Brazeは、RudderStackのメソッドであるidentify、track、screen、page、group、aliasをサポートしています。

{% tabs %}
{% tab Identify %}

RudderStackの[`identify`メソッド](https://rudderstack.com/docs/destinations/marketing/braze/#identify)は、ユーザーをそのアクションに関連付けます。RudderStackは、一意のユーザーIDと、名前、メール、IPアドレスなど、そのユーザーに関連付けられたオプションの特性をキャプチャします。

**identifyコールのデルタ管理**<br>
デバイスモードでBrazeにイベントを送信する場合、`identify`コールを重複排除することでコストを削減できます。これを行うには、ダッシュボードの「Deduplicate Traits」設定を有効にします。RudderStackは、変更または修正された属性（特性）のみをBrazeに送信します。

**ユーザーの削除**<br>
RudderStackの[Data Regulation API](https://www.rudderstack.com/docs/api/data-regulation-api/)の[Suppression with Delete regulation](https://www.rudderstack.com/docs/api/data-regulation-api/#adding-a-suppression-with-delete-regulation)を使用して、Brazeのユーザーを削除できます。

{% endtab %}
{% tab Track %}

RudderStackの[`track`メソッド](https://rudderstack.com/docs/destinations/marketing/braze/#track)は、すべてのユーザーアクティビティとそれらのアクティビティに関連付けられたプロパティをキャプチャします。

**注文完了**<br>
[RudderStack eコマースAPI](https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/)を使用して、`Order Completed`というイベント名でtrackメソッドを呼び出すと、RudderStackはそのイベントに含まれる商品を[`purchases`]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data#revenue-data)としてBrazeに送信します。

{% endtab %}
{% tab Screen %}

RudderStackの[`screen`メソッド](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#screen)を使用すると、閲覧した画面に関する追加情報とともに、ユーザーのモバイル画面ビューを記録できます。

{% endtab %}
{% tab Page %}

RudderStackの[`page`メソッド](https://rudderstack.com/docs/destinations/marketing/braze/#page)を使用すると、Webサイトのページビューを記録できます。また、そのページに関するその他の関連情報もキャプチャします。

{% endtab %}
{% tab Group %}

RudderStackの[`group`メソッド](https://rudderstack.com/docs/destinations/marketing/braze/#group)を使用すると、ユーザーをグループに関連付けることができます。

**購読グループのステータス**<br>
購読グループのステータスを更新するには、RudderStackダッシュボードで「Enable subscription groups in group call」設定を有効にし、groupコールで購読グループのステータスを送信します。

{% endtab %}
{% tab Alias %}

RudderStackの[`alias`メソッド](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#alias)を使用すると、既知のユーザーの異なるIDを統合できます。RudderStackは、Brazeに対するaliasコールをクラウドモードでのみサポートしています。

{% endtab %}
{% endtabs %}

## ユーザー特性を階層化カスタム属性として送信する {#send-user-traits-as-nested-custom-attributes}

ユーザー特性を階層化カスタム属性としてBrazeに送信し、追加、更新、削除の操作を実行できます。これを行うには、Brazeの送信先を設定する際に、RudderStackで「Use Custom Attributes Operation dashboard」設定を有効にします。この機能はクラウドモードでのみ利用可能です。

ユーザー特性を階層化カスタム属性として`identify`イベントで以下の形式で送信できます。
```javascript
rudderanalytics.identify("1hKOmRA4GRlm", {
  "cars": {
    "add": [{
      "age": 27,
      "id": 1,
      "name": "Alex Keener"
    }],
    "update": [{
        "age": 30,
        "id": 2,
        "identifier": "id",
        "name": "Rowan"
      },
      {
        "age": 27,
        "id": 1,
        "identifier": "id",
        "name": "Alex"
      }
    ]
  },
  "country": "USA",
  "email": "alex@example.com",
  "firstName": "Alex",
  "gender": "M",
  "pets": [{
      "breed": "beagle",
      "id": 1,
      "name": "Scooby",
      "type": "dog"
    },
    {
      "breed": "calico",
      "id": 2,
      "name": "Garfield",
      "type": "cat"
    }
  ]
})
```

ユーザー特性をカスタムユーザー属性として`track`、`page`、または`screen`呼び出しで送信するには、イベントのコンテキストフィールドとして`traits`を渡します。
```javascript
rudderanalytics.track("Product Viewed", {
    revenue: 8.99,
    currency: "USD",
 },{
  "traits": {
    "cars": {
      "add": [{
        "age": 27,
        "id": 1,
        "name": "Alex Keener"
      }],
      "update": [{
          "age": 30,
          "id": 2,
          "identifier": "id",
          "name": "Alex"
        },
        {
          "age": 27,
          "id": 1,
          "identifier": "id",
          "name": "Rowan"
        }
      ]
    },
    "city": "Disney",
    "country": "USA",
    "email": "alexa@example.com",
    "firstName": "Alexa",
    "gender": "woman",
    "pets": [{
        "breed": "beagle",
        "id": 1,
        "name": "Scooby",
        "type": "dog"
      },
      {
        "breed": "calico",
        "id": 2,
        "name": "Garfield",
        "type": "cat"
      }
    ]
  }
});
```

{% alert note %}
更新および削除の操作では、`identifier`が必須キーです。ネストされた配列に追加、更新、または削除の操作が含まれていない場合、RudderStackはデフォルトで作成操作を使用してプロパティを作成します。階層化カスタム属性の送信に関する詳細は、[オブジェクトの配列]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects)を参照してください。
{% endalert %}

## トラブルシューティング {#troubleshooting}

### RudderStack のログに「[Braze Deduplication]: Duplicate user detected, the user is dropped」と表示される {#i-see-braze-deduplication-duplicate-user-detected-the-user-is-dropped-in-rudderstack-logs}

このメッセージは、**Deduplicate Traits** が有効になっている場合に RudderStack から表示されるもので、RudderStack が変更のないユーザー特性を Braze に転送する前に除外したことを示しています。これは Braze のエラーではありません。

RudderStack は受信した `identify` および `track` の特性をユーザープロファイルと比較し、差分のない属性をスキップすることで Braze のデータポイント使用量を削減します。詳細については、RudderStack の [User Trait Deduplication in Braze](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/trait-deduplication/) ガイドを参照してください。

すべての呼び出しで毎回すべての特性を送信する必要がある場合は、RudderStack の Braze 送信先設定で **Deduplicate Traits** をオフにしてください。ただし、この設定により Braze のデータポイント消費量が増加する可能性があることに注意してください。