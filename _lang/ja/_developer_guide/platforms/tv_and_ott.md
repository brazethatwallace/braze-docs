---
nav_title: テレビとOTT
article_title: Braze用TVとOTTの統合
page_order: 15

description: "この記事では、BrazeのTVおよびOTT機能、統合、利用可能なプラットフォーム、その他の機能について詳しく説明します。"
platform:
  - tvOS
  - Roku
  - Web
  - Android
  - FireOS
---

# TVとOTTの統合 {#tv-and-ott-integrations}

> テクノロジーが新しいプラットフォームやデバイスへと進化するにつれて、Brazeを使ったメッセージングも進化します！Brazeは、さまざまなTVオペレーティングシステムおよびOver-the-Top（OTT）コンテンツ配信方法に対応した、さまざまなエンゲージメントチャネルを提供しています。

## プラットフォームと機能 {#platforms-and-features}

以下は、現在サポートされている機能とメッセージングチャネルの一覧です。

<style>
#tv-feature-table td,
#tv-feature-table th {
    text-align: center !important;
    vertical-align: center;
}

</style>
<table aria-label="プラットフォームと機能" id="tv-feature-table">
  <caption>プラットフォームと機能</caption>
    <thead>
        <tr>
            <th>デバイスタイプ</th>
            <th>データと分析</th>
            <th>アプリ内メッセージ</th>
            <th>Content Cards</th>
            <th>プッシュ通知</th>
            <th>Canvas</th>
            <th>フィーチャーフラグ</th>
            <th>バナー</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Amazon Fire TV</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
            <td for="iam"><i class="fas fa-check text-success"></i></td>
            <td for="content-cards"><i class="fas fa-check text-success"></i></td>
            <td for="push"><i class="fas fa-check text-success"></i></td>
            <td for="canvas"><i class="fas fa-check text-success"></i></td>
            <td for="feature-flags"><i class="fas fa-check text-success"></i></td>
            <td for="banners"><i class="fas fa-check text-success"></i></td>
        </tr>
        <tr>
            <td>Kindle Fire</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
            <td for="iam"><i class="fas fa-check text-success"></i></td>
            <td for="content-cards"><i class="fas fa-check text-success"></i></td>
            <td for="push"><i class="fas fa-check text-success"></i></td>
            <td for="canvas"><i class="fas fa-check text-success"></i></td>
            <td for="feature-flags"><i class="fas fa-check text-success"></i></td>
            <td for="banners"><i class="fas fa-check text-success"></i></td>
        </tr>
        <tr>
            <td>Android TV</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
            <td for="iam"><i class="fas fa-check text-success"></i></td>
            <td for="content-cards"><i class="fas fa-check text-success"></i></td>
            <td for="push"><i class="fas fa-check text-success"></i></td>
            <td for="canvas"><i class="fas fa-check text-success"></i></td>
            <td for="feature-flags"><i class="fas fa-check text-success"></i></td>
            <td for="banners"><i class="fas fa-check text-success"></i></td>
        </tr>
        <tr>
            <td>LGテレビ（webOS）</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
            <td for="iam"><i class="fas fa-check text-success"></i></td>
            <td for="content-cards"><i class="fas fa-check text-success"></i></td>
            <td for="push">該当なし</td>
            <td for="canvas"><i class="fas fa-check text-success"></i></td>
            <td for="feature-flags"><i class="fas fa-check text-success"></i></td>
            <td for="banners"><i class="fas fa-check text-success"></i></td>
        </tr>
        <tr>
            <td>Samsung Tizen TV</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
            <td for="iam"><i class="fas fa-check text-success"></i></td>
            <td for="content-cards"><i class="fas fa-check text-success"></i></td>
            <td for="push">該当なし</td>
            <td for="canvas"><i class="fas fa-check text-success"></i></td>
            <td for="feature-flags"><i class="fas fa-check text-success"></i></td>
            <td for="banners"><i class="fas fa-check text-success"></i></td>
        </tr>
        <tr>
            <td>Roku</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
            <td for="iam"><i class="fas fa-check text-success"></i></td>
            <td for="content-cards"><i class="fas fa-times text-warning"></i></td>
            <td for="push">該当なし</td>
            <td for="canvas"><i class="fas fa-check text-success"></i></td>
            <td for="feature-flags"><i class="fas fa-check text-success"></i></td>
            <td for="banners"><i class="fas fa-times text-warning"></i></td>
        </tr>
        <tr>
            <td>Apple TV OS</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
             <td for="iam"><i class="fas fa-check text-success"></i></td>
            <td for="content-cards"><i class="fas fa-check text-success"></i></td>
            <td for="push"><i class="fa-solid fa-minus"></i></td>
            <td for="canvas"><i class="fas fa-check text-success"></i></td>
            <td for="feature-flags"><i class="fas fa-check text-success"></i></td>
            <td for="banners"><i class="fas fa-check text-success"></i></td>
        </tr>
       <tr>
          <td>Apple Vision Pro</td>
          <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
           <td for="iam"><i class="fas fa-check text-success"></i></td>
          <td for="content-cards"><i class="fas fa-check text-success"></i></td>
          <td for="push"><i class="fa-solid fa-minus"></i></td>
          <td for="canvas"><i class="fas fa-check text-success"></i></td>
          <td for="feature-flags"><i class="fas fa-check text-success"></i></td>
          <td for="banners"><i class="fas fa-check text-success"></i></td>
      </tr>
    </tbody>
</table>

- <i class="fas fa-check text-success"></i> = サポート対象
- <i class="fa-solid fa-minus"></i> = 部分的にサポート
- <i class="fas fa-times text-warning"></i> = Brazeではサポートされていません
- 該当なし = OTTプラットフォームではサポートされていません

## 統合ガイド {#integration-guides}

### Amazon Fire TV {#fire-tv}

Amazon Fire TVデバイスと統合するには、Braze Fire OS SDKを使用します。

以下の機能があります。

- クロスチャネルエンゲージメントのためのデータと分析の収集
- プッシュ通知（[「ヘッドアップ通知」](https://developer.amazon.com/docs/fire-tv/notifications.html#headsup)とも呼ばれます）
  - これらを表示するには、優先度を「HIGH」に設定する必要があります。すべての通知はFire TVの設定メニューに表示されます。
- Content Cards
- フィーチャーフラグ
- アプリ内メッセージ
  - TVなどの非タッチ環境でHTMLメッセージを表示するには、`com.braze.configuration.BrazeConfig.Builder.setIsTouchModeRequiredForHtmlInAppMessages`を`false`に設定します（[Android SDK v23.1.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2310)から利用可能）。
- バナー
  - [バナープレースメント]({{site.baseurl}}/developer_guide/banners/placements/)を使用して、Fire TVアプリにメッセージを直接埋め込みます。

詳細については、[Fire OS統合ガイド]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android)を参照してください。

### Kindle Fire {#kindle-fire}

Amazon Kindle Fireデバイスと統合するには、Braze Fire OS SDKを使用します。

以下の機能があります。

- クロスチャネルエンゲージメントのためのデータと分析の収集
- プッシュ通知
- Content Cards
- フィーチャーフラグ
- アプリ内メッセージ
- バナー
  - [バナープレースメント]({{site.baseurl}}/developer_guide/banners/placements/)を使用して、Kindle Fireにメッセージを直接埋め込みます。

詳細については、[Fire OS統合ガイド]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android)を参照してください。

### Android TV {#android-tv}

Braze Android SDKを使用して、Android TVデバイスと統合します。

以下の機能があります。

- クロスチャネルエンゲージメントのためのデータと分析の収集
- Content Cards
- フィーチャーフラグ
- アプリ内メッセージ
  - TVなどの非タッチ環境でHTMLメッセージを表示するには、`com.braze.configuration.BrazeConfig.Builder.setIsTouchModeRequiredForHtmlInAppMessages`を`false`に設定します（[Android SDK v23.1.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2310)から利用可能）。
- &#42; プッシュ通知（手動統合が必要）
  - プッシュ通知はAndroid TVでネイティブにサポートされていません。理由については、Googleの[デザインガイドライン](https://designguidelines.withgoogle.com/android-tv/patterns/notifications.html)を参照してください。ただし、**プッシュ通知UIの手動統合を行うことでこれを実現できます**。設定方法については、[ドキュメント]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android%20tv)を参照してください。
- バナー
  - [バナープレースメント]({{site.baseurl}}/developer_guide/banners/placements/)を使用して、Android TVアプリにメッセージを直接埋め込みます。

詳細については、[Android SDK統合ガイド]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android)を参照してください。

{% alert note %}
Android OTT統合用に、ダッシュボードで新しいAndroidアプリを作成してください。
{% endalert %}

### LG webOS {#lg-webos}

Braze Web SDKを使用して[LG webOSテレビ](https://webostv.developer.lge.com/discover)と統合します。

以下の機能があります。

- クロスチャネルエンゲージメントのためのデータと分析の収集
- Content Cards（[ヘッドレスUI](#custom-ui)経由）
- フィーチャーフラグ
- アプリ内メッセージ（[ヘッドレスUI](#custom-ui)経由）
- バナー
  - [バナープレースメント]({{site.baseurl}}/developer_guide/banners/placements/)を使用して、webOSアプリにメッセージを直接埋め込みます。

詳細については、[Web Smart TV統合ガイド]({{site.baseurl}}/developer_guide/platforms/web/smart_tvs/)を参照してください。

### Samsung Tizen {#tizen}

Braze Web SDKを使用して[Samsung Tizenテレビ](https://developer.samsung.com/smarttv/develop/specifications/tv-model-groups.html)と統合します。

以下の機能があります。

- クロスチャネルエンゲージメントのためのデータと分析の収集
- Content Cards（[ヘッドレスUI](#custom-ui)経由）
- フィーチャーフラグ
- アプリ内メッセージ（[ヘッドレスUI](#custom-ui)経由）
- バナー
  - [バナープレースメント]({{site.baseurl}}/developer_guide/banners/placements/)を使用して、Tizenアプリにメッセージを直接埋め込みます。

詳細については、[Web Smart TV統合ガイド]({{site.baseurl}}/developer_guide/platforms/web/smart_tvs/)を参照してください。

### Roku {#roku}

Braze Roku SDKを使用して[Rokuテレビ](https://developer.roku.com/docs/developer-program/getting-started/roku-dev-prog.md)と統合します。

以下の機能があります。

- クロスチャネルエンゲージメントのためのデータと分析の収集
- アプリ内メッセージ（[ヘッドレスUI](#custom-ui)経由）
  - RokuプラットフォームではWebviewがサポートされていないため、HTMLアプリ内メッセージもサポートされていません。
- フィーチャーフラグ

詳細については、[Roku統合ガイド]({{site.baseurl}}/developer_guide/in_app_messages/?sdktab=roku)を参照してください。

### Apple TV OS {#tvos}

tvOSと統合するにはBraze Swift SDKを使用します。Swift SDKにはtvOS用のデフォルトUIやビューが含まれていないため、独自に実装する必要があります。

以下の機能があります。

- クロスチャネルエンゲージメントのためのデータと分析の収集
- Content Cards（[ヘッドレスUI](#custom-ui)経由）
- フィーチャーフラグ
- アプリ内メッセージ（[ヘッドレスUI](#custom-ui)経由）
  - tvOSプラットフォームではWebビューがサポートされていないため、HTMLアプリ内メッセージもサポートされていません。
  - tvOSでカスタマイズされたメッセージングにヘッドレスUIを使用する方法の詳細については、[サンプルアプリ](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples#inappmessages-custom-ui)を参照してください。
- サイレントプッシュ通知とバッジの更新
- バナー
  - [バナープレースメント]({{site.baseurl}}/developer_guide/banners/placements/)を使用して、tvOSアプリにメッセージを直接埋め込みます。

詳細については、[iOS Swift SDK統合ガイド](https://github.com/braze-inc/braze-swift-sdk)を参照してください。

{% alert note %}
TVユーザーにモバイルのアプリ内メッセージが表示されないようにするには、[アプリターゲティング](#app-targeting)を設定するか、キーと値のペアを使用してメッセージをフィルタリングしてください。例えば、特別な`tv = true`キーと値のペアが含まれている場合にのみtvOSメッセージを表示するようにします。
{% endalert %}

### Apple Vision Pro {#vision-pro}

Braze Swift SDKを使用してvisionOSと統合します。iOSで利用可能なほとんどの機能はvisionOSでも利用でき、以下が含まれます。

- 分析（セッション、カスタムイベント、購入など）
- アプリ内メッセージング（データモデルとUI）
- Content Cards（データモデルとUI）
- プッシュ通知（アクションボタン付きのユーザー可視通知とサイレント通知）
- フィーチャーフラグ
- ロケーション分析
- バナー
  - [バナープレースメント]({{site.baseurl}}/developer_guide/banners/placements/)を使用して、visionOSアプリにメッセージを直接埋め込みます。

詳細については、[iOS Swift SDK統合ガイド](https://github.com/braze-inc/braze-swift-sdk)を参照してください。

{% alert important %}
一部のiOS機能は部分的にサポートされているか、サポートされていません。完全なリストについては、[visionOSサポート](https://www.braze.com/docs/developer_guide/platform_integration_guides/swift/visionos)を参照してください。
{% endalert %}

## アプリターゲティング {#app-targeting}

メッセージングでOTTアプリをターゲットにするには、OTTアプリ専用のセグメントを作成することをお勧めします。

![Android OTTアプリを使用して作成されたセグメント。]({% image_buster /assets/img/android_ott.png %})

## ヘッドレスUI {#custom-ui}

{% alert important %}
ヘッドレスUIを通じてアプリ内メッセージやContent Cardsをサポートするプラットフォームには、デフォルトのUIやビューは含まれて**いません**。独自のカスタムUI（アプリ内メッセージ用など）を構築し、SDKが提供するデータモデルを使用してそれらのUIにデータを表示してください。
{% endalert %}

ヘッドレスUIでは、BrazeがJSONなどのデータモデルを配信し、アプリが制御するUI内でアプリがそのデータを読み取って使用できます。このデータには、ダッシュボードで設定されたフィールド（タイトル、本文、ボタンテキスト、色など）が含まれており、アプリはその設定に従ってそれらを読み取り、表示できます。メッセージングのカスタム処理の詳細については、以下を参照してください。

**Android SDK**
- [アプリ内メッセージのカスタマイズ]({{site.baseurl}}/developer_guide/in_app_messages/customization/?sdktab=android#android_setting-custom-manager-listeners)
- [Content Cardsのカスタマイズ]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/style/)

**Swift SDK**
- [アプリ内メッセージのカスタマイズ](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazeinappmessagepresenter/)
- [ヘッドレスUIサンプルアプリ](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples#inappmessages-custom-ui)
- [Content Cardsのカスタマイズ](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/)

**Web SDK**
- [アプリ内メッセージのカスタマイズ]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages/?tab=web)
- [Content Cardsのカスタマイズ]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/style/)