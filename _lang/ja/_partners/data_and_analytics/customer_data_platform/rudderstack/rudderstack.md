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
| 設定済みのソース | [ソース](https://www.rudderstack.com/docs/dashboard-guides/sources/)は基本的に、Webサイト、モバイルアプリ、バックエンドサーバーなど、RudderStackに送信されるあらゆるデータの提供元です。RudderStackでBrazeを送信先として設定する前に、ソースを設定する必要があります。 |
| Braze REST APIキー | `users.track`、`users.identify`、`users.delete`、`users.alias.new`の権限を持つBraze REST APIキー。<br><br>これは、Brazeダッシュボードの**設定** > **APIキー**で作成できます。 |
| Brazeアプリキー | Brazeダッシュボードでアプリキーを取得するには、**設定** > **アプリ設定** > **Identification**に移動し、アプリ名を見つけます。関連する識別子文字列を保存してください。
| データセンター | データセンターは、Brazeダッシュボードの[インスタンス]({{site.baseurl}}/api/basics#endpoints)に対応しています。  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## 統合 {#integration}

### ステップ1:ソースを追加する {#step-1-add-a-source}

Brazeへのデータ送信を開始するには、まずRudderStackアプリにソースが設定されていることを確認する必要があります。データソースの設定方法については、[RudderStack](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#getting-started)を参照してください。

### ステップ2:送信先を設定する {#step-2-configure-destination}

データソースが設定されたら、RudderStackダッシュボードで、**Destinations**の下にある**ADD DESTINATION**を選択します。使用可能な送信先のリストから**Braze**を選択し、**Next**をクリックします。

Brazeの送信先で、アプリキー、Braze REST APIキー、データクラスタ、およびネイティブSDKオプション（デバイスモードのみ）を指定します。ネイティブSDKオプションをオンにすると、BrazeネイティブSDKを使用してイベントが送信されます。

### ステップ3:統合のタイプを選ぶ {#step-3-choose-the-type-of-integration}

次のいずれかの方法を使用して、RudderStackのWebライブラリとネイティブクライアント側ライブラリをBrazeと統合できます。

- [サイドバイサイド/デバイスモード](#device-mode)**:** RudderStackは、クライアント（ブラウザまたはモバイルアプリケーション）から直接Brazeにイベントデータを送信します。
- [サーバー間/クラウドモード](#cloud-mode)**:** Braze SDKはイベントデータをRudderStackに直接送信し、そこで変換されてBrazeにルーティングされます。
- [ハイブリッドモード](#hybrid-mode)**:** ハイブリッドモードを使用して、iOSとAndroidの自動生成イベントとユーザー生成イベントを、単一の接続を使用してBrazeに送信します。

{% alert note %}
RudderStackの[接続モード](https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/)と、それぞれの利点について詳しくはこちらをご覧ください。
{% endalert %}

#### サイドバイサイド統合（デバイスモード） {#device-mode}

このモードでは、Webサイトまたはモバイルアプリで設定したBraze SDKを使用して、イベントをBrazeに送信できます。

[サポートされているメソッド](#supported-methods)で説明されているように、BrazeのGitHubリポジトリでご使用のプラットフォームに対応したRudderStack SDKへのマッピングを設定します。

- [Android](https://github.com/rudderlabs/rudder-integration-braze-android)
- [iOS](https://github.com/rudderlabs/rudder-integration-braze-ios/tree/master)
- [Swift](https://github.com/rudderlabs/rudder-integration-braze-swift)
- [Web](https://github.com/rudderlabs/rudder-sdk-js/tree/develop/packages/analytics-js-integrations/src/integrations/Braze)
- [React Native](https://github.com/rudderlabs/rudder-sdk-react-native/tree/develop/libs/rudder-integration-braze-react-native)
- [Flutter](https://github.com/rudderlabs/rudder-sdk-flutter/tree/develop/packages/integrations/rudder_integration_braze_flutter)

デバイスモードの統合を完了するには、RudderStackの[プロジェクトにBrazeを追加する](https://rudderstack.com/docs/destinations/marketing/braze/#adding-device-mode-integration)詳しい手順を参照してください。

#### サーバー間統合（クラウドモード） {#cloud-mode}

このモードでは、SDKはイベントデータを直接RudderStackサーバーに送信します。その後、RudderStackはこのデータを変換し、目的の送信先にルーティングします。この変換は、RudderStackのトランスフォーマーモジュールを使用してRudderStackバックエンドで実行されます。

統合を有効にするには、[サポートされているメソッド](#supported-methods)で説明されているように、RudderStackメソッドをBrazeにマッピングする必要があります。

{% alert note %}
RudderStackのサーバーサイドSDK（Java、Python、Node.js、Go、Ruby）は、クラウドモードのみをサポートしています。これは、サーバー側のSDKがRudderStackバックエンドで動作し、Braze固有のSDKを読み込むことができないためです。
{% endalert %}

{% alert important %}
サーバー間の統合は、プッシュ通知やアプリ内メッセージングなどのBraze UI機能をサポートしていません。ただし、これらの機能はデバイスモード統合によってサポートされます。
{% endalert %}

#### ハイブリッドモード {#hybrid-mode}

ハイブリッドモードを使用して、iOSとAndroidのソースからすべてのイベントをBrazeに送信します。

ハイブリッドモードでBrazeにイベントを送信することを選択した場合、RudderStackにより次の操作が行われます。
1. Braze SDKを初期化します。
2. ユーザーが生成したすべてのイベント（identify、track、page、screen、group）をクラウドモードからのみBrazeに送信し、デバイスモードからの送信をブロックします。
3. 自動生成イベント（アプリ内メッセージ、Braze SDKを必要とするプッシュ通知）をデバイスモード経由で送信します。

[ハイブリッドモードでイベントを送信する](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#send-events-in-hybrid-mode)には、ソースをBrazeの送信先に接続する際にハイブリッドモードオプションを使用します。次に、Braze統合をプロジェクトに追加します。

## ステップ4:追加設定を行う {#step-4-configure-additional-settings}

初期設定完了後、Brazeでデータを正しく受信するために以下の設定を行います。

- **Enable subscription groups in group call**：グループイベントでサブスクリプショングループのステータスを送信するには、この設定を有効にします。詳細については、[Group](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#group)を参照してください。
- **Use Custom Attributes Operation**：Brazeの[階層化カスタム属性]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects)機能を使用してセグメントを作成し、カスタム属性オブジェクトを使用してメッセージをパーソナライズする場合は、この設定を有効にします。詳細については、[ネストされたカスタム属性としてユーザー特性を送信する](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#send-user-traits-as-nested-custom-attributes)を参照してください。
- **Track events for anonymous users**：この設定を有効にすると、匿名ユーザーの活動が追跡され、その情報がBrazeに送信されます。

### デバイスモード設定 {#device-mode-settings}

以下の設定は、[デバイスモード](https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode)経由でBrazeにイベントを送信する場合にのみ適用されます。

- **Client-side Events Filtering**：この設定により、Brazeに流れるイベントをブロックするか、許可するかを指定できます。この設定の詳細については、[Client-side Events Filtering](https://www.rudderstack.com/docs/sources/event-streams/sdks/event-filtering/)を参照してください。
- **Deduplicate Traits**：この設定を有効にすると、[`identify`](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#identify)呼び出しでユーザー特性の重複が排除されます。
- **Show Braze logs**：この設定は、[JavaScript SDK](https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/)をソースとして使用する場合にのみ適用されます。Brazeのログをユーザーに表示するには、これを有効にします。
- **OneTrust Cookieカテゴリー**：この設定により、[OneTrust](https://www.rudderstack.com/docs/sources/event-streams/sdks/onetrust/javascript/) Cookieの同意グループをBrazeに関連付けることができます。

## サポートされているメソッド {#supported-methods}

Brazeは、RudderStackメソッドのidentify、track、screen、page、group、aliasをサポートしています。

{% tabs %}
{% tab Identify %}

RudderStackの[`identify`メソッド](https://rudderstack.com/docs/destinations/marketing/braze/#identify)は、ユーザーとそのアクションを関連付けます。RudderStackは、一意のユーザーIDと、名前、メール、IPアドレスなど、そのユーザーに関連するオプションの特性をキャプチャします。

**identify呼び出しの差分管理**<br>
デバイスモードでBrazeにイベントを送信する場合、`identify`呼び出しを重複排除することでコストを節減できます。そのためには、Deduplicate Traitsダッシュボード設定を有効にします。その後、RudderStackは変更された属性（特性）のみをBrazeに送信します。

**ユーザーの削除**<br>
RudderStack [Data Regulation API](https://www.rudderstack.com/docs/api/data-regulation-api/)の[抑制と削除の規則（Suppression with Delete regulation）](https://www.rudderstack.com/docs/api/data-regulation-api/#adding-a-suppression-with-delete-regulation)を使用して、Brazeのユーザーを削除できます。

{% endtab %}
{% tab Track %}

RudderStackの[`track`メソッド](https://rudderstack.com/docs/destinations/marketing/braze/#track)は、すべてのユーザーアクティビティと、それらのアクティビティに関連するプロパティをキャプチャします。

**Order completed**<br>
[RudderStack eCommerce API](https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/)を使用して`Order Completed`という名前のイベントに対してtrackメソッドを呼び出すと、RudderStackはそのイベントにリストされている製品を[`purchases`]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data#revenue-data)としてBrazeに送信します。

{% endtab %}
{% tab Screen %}

RudderStackの[`screen`メソッド](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#screen)を使用して、ユーザーのモバイル画面ビューを、表示されている画面に関する追加情報とともに記録できます。

{% endtab %}
{% tab Page %}

RudderStackの[`page`メソッド](https://rudderstack.com/docs/destinations/marketing/braze/#page)を使用して、Webサイトのページビューを記録できます。また、そのページに関するその他の関連情報もキャプチャされます。

{% endtab %}
{% tab Group %}

RudderStackの[`group`メソッド](https://rudderstack.com/docs/destinations/marketing/braze/#group)を使用して、ユーザーをグループに関連付けることができます。

**サブスクリプショングループのステータス**<br>
サブスクリプショングループのステータスを更新するには、RudderStackダッシュボードの「Enable subscription groups in group call」設定を有効にし、グループ呼び出しでサブスクリプショングループのステータスを送信します。

{% endtab %}
{% tab Alias %}

RudderStackの[`alias`メソッド](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#alias)を使用して、既知のユーザーの複数のIDをマージできます。RudderStackは、クラウドモードでのみBrazeのエイリアス呼び出しをサポートしていることに注意してください。

{% endtab %}
{% endtabs %}

## ユーザー特性を階層化カスタム属性として送信する {#send-user-traits-as-nested-custom-attributes}

ユーザー特性を階層化カスタム属性としてBrazeに送信し、それに対して追加、更新、削除操作を実行できます。これを行うには、Brazeの送信先を設定するときにRudderStackで「Use Custom Attributes Operation dashboard」設定を有効にします。この機能はクラウドモードでのみ利用できます。

次の形式で`identify`イベントでユーザー特性を階層化カスタム属性として送信できます。
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

`track`、`page`、または`screen`呼び出しでユーザー特性をカスタムユーザー属性として送信するには、イベントのコンテキストフィールドとして`traits`を渡します。
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
更新と削除の操作では、`identifier`が必須キーとなります。add、update、remove操作がネスト配列に存在しない場合、RudderStackはデフォルトでcreate操作を使用してプロパティを作成します。階層化カスタム属性の送信の詳細については、[オブジェクト配列]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects)を参照してください。
{% endalert %}