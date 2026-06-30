---
nav_title: SDKの概要
article_title: 開発者向けのSDK概要
description: "このオンボーディングリファレンス記事には、Braze SDKの開発者向けの技術概要が記載されています。ここでは、SDKでトラッキングされるデフォルトの分析、自動データ収集のブロック、アプリのライブSDKバージョンについて説明します。"
page_order: 0
---

# [![Brazeラーニングコース]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/path/developer/sdk-integration-basics){: style="float:right;width:120px;border:0;" class="noimgborder"}開発者向けSDKの概要 {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecompathdevelopersdk-integration-basics-stylefloatrightwidth120pxborder0-classnoimgbordersdk-overview-for-developers}

> Braze SDKの統合を開始する前に、正確に何を構築および統合するのかを疑問に思うかもしれません。また、ニーズに応じてSDKをより詳細にカスタマイズする方法に興味があるかもしれません。この記事は、SDKに関するすべての疑問を解決するのに役立ちます。

SDKの基本的な概要を探しているマーケターは、代わりに[マーケター向けの概要]({{site.baseurl}}/user_guide/get_started/sdk_overview)をご覧ください。

Braze SDKを簡単に説明すると、次のとおりです。
* ユーザーデータを収集し、統合ユーザープロファイルに同期します
* セッションデータ、デバイス情報、プッシュトークンを自動的に収集します
* マーケティングエンゲージメントデータとビジネスに固有のカスタムデータを取得します
* プッシュ通知、**In-App Messages**、コンテンツカードメッセージングチャネルを強化します

以下の動画で、Braze SDKの統合の基本とコア機能について簡単に紹介しています。

{% multi_lang_include video.html id="il152jayp0" source="wistia" %}

## アプリのパフォーマンス {#app-performance}

Brazeがアプリのパフォーマンスに悪影響を及ぼすことはありません。

Braze SDKのフットプリントは非常に小さいです。手動のネットワーク制御が許可されるのに加え、ネットワークの品質に応じ、ユーザーデータをフラッシュするレートの自動変更が実行されます。SDKからのAPIリクエストを自動的にバッチ処理して、ネットワーク効率を常に最大化しながらデータが迅速にロギングされるようにします。最後に、各API呼び出し内でクライアントからBrazeに送信されるデータは非常に少量です。

## SDKの互換性 {#sdk-compatibility}

Braze SDKは非常に円滑に動作し、アプリ内に存在する他のSDKに干渉しないよう設計されています。他のSDKとの互換性不足が原因と思われる問題が発生している場合は、Brazeサポートにお問い合わせください。

## デフォルトの分析とセッション処理 {#default-analytics-and-session-handling}

最初に使用したアプリ、最後に使用したアプリ、合計セッション数、デバイスOSなど、特定のユーザーデータはSDKで自動的に収集されます。統合ガイドに従ってSDKを実装すると、この[デフォルトデータ収集]({{site.baseurl}}/user_guide/data/unification/user_data/sdk_data_collection)を利用できるようになります。このリストを確認することで、ユーザーに関する同じ情報を複数回保存しなくて済みます。セッション開始とセッション終了を除き、その他の自動的にトラッキングされるデータは、データポイント使用量にはカウントされません。

{% alert note %}
すべての機能が構成可能ですが、デフォルトのデータ収集モデルを完全に実装することをお勧めします。

<br>ユースケースで必要な場合は、統合の完了後に[特定のデータの収集を制限](#blocking-data-collection)できます。
{% endalert %}

## データのアップロードとダウンロード {#data-upload-and-download}

Braze SDKでは、データ（セッション、カスタムイベントなど）がキャッシュされ、定期的にアップロードされます。データがアップロードされた後でのみ、ダッシュボード上で値が更新されます。アップロード間隔は、デバイスの状態を考慮し、ネットワーク接続の品質に基づいて決定されます。

| ネットワーク接続品質 | データフラッシュ間隔 |
|---|---|
| 素晴らしい | 10秒 |
| 良好 | 30秒 |
| 不良 | 60秒 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="データのアップロードとダウンロード" }

ネットワーク接続がない場合、ネットワーク接続が再確立されるまで、データはデバイスのローカルにキャッシュされます。接続が再確立されると、データがBrazeにアップロードされます。

セッションの時点でユーザーが属するSegmentに基づいて、セッションの開始時にBrazeからSDKにデータが送信されます。新しいアプリ内メッセージはセッション中に更新されません。ただし、セッション中のユーザーデータは、クライアントから送信されると継続的に処理されます。たとえば、離脱ユーザー（アプリを最後に使用してから7日以上経過）には、アプリに戻ってから最初のセッションで、離脱ユーザーをターゲットにしたコンテンツが提供されます。

## データ収集のブロック {#blocking-data-collection}

SDK統合からの特定のデータの自動収集をブロックしたり、そのプロセスを許可リストに登録したりすることは（推奨はされませんが）可能です。

分析データを削除すると、プラットフォームのパーソナライゼーションとターゲット設定の能力が低下するため、データ収集をブロックすることは推奨されません。以下はその例です。

- いずれかのSDKで位置情報を完全に統合しないことを選択した場合、言語や位置情報に基づいてメッセージングをパーソナライズできません。
- タイムゾーンを統合しないことを選択した場合、ユーザーのタイムゾーン内でメッセージを送信できない可能性があります。
- 特定のデバイスビジュアル情報を統合しないことを選択した場合、メッセージのコンテンツがそのデバイス向けに最適化されない可能性があります。

製品の機能を最大限に活用するには、SDKを完全に統合することを強くお勧めします。

{% tabs %}
{% tab Web SDK %}

SDKの特定の部分を統合しないことも、ユーザーに対して[`disableSDK`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#disablesdk)を使用することもできます。このメソッドにより、`disableSDK()`の呼び出し前にロギングされたデータが同期され、このページと将来のページの読み込みに対するその後のBraze Web SDKの呼び出しはすべて無視されます。後の時点でデータ収集を再開するには、[`enableSDK()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#enablesdk)メソッドを使用できます。この詳細については、[Webトラッキングの無効化]({{site.baseurl}}/developer_guide/analytics/managing_data_collection?sdktab=web)に関する記事をご覧ください。

{% endtab %}
{% tab Android SDK %}

[`setDeviceObjectAllowlist`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-device-object-allowlist.html?query=fun%20setDeviceObjectAllowlist(deviceObjectAllowlist:%20EnumSet%3CDeviceKey%3E):%20BrazeConfig.Builder)を使用し、設定された許可リストに従ってデバイスオブジェクトのキーまたは値のサブセットのみを送信するようSDKを構成できます。これは[`setDeviceObjectAllowlistEnabled`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-device-object-allowlist-enabled.html?query=fun%20setDeviceObjectAllowlistEnabled(enabled:%20Boolean):%20BrazeConfig.Builder)を介して有効にする必要があります。

{% alert important %}
許可リストが空の場合、デバイスデータはBrazeに送信**されません**。
{% endalert %}

{% endtab %}
{% tab Swift SDK %}

`Braze.Configuration`で対象となるフィールドのセットを[`configuration.devicePropertyAllowList`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/devicepropertyallowlist)に割り当て、SDKで収集されるデバイスフィールドの許可リストを指定することができます。フィールドの完全なリストは[`Braze.Configuration.DeviceProperty`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/deviceproperty)で定義されます。すべてのデバイスフィールドの収集をオフにするには、このプロパティの値を空のセット (`[]`) に設定します。

{% alert important %}
デフォルトでは、Braze Swift SDKですべてのフィールドが収集されます。一部のデバイスプロパティを削除すると、SDK機能が無効になる場合があります。
{% endalert %}

使用の詳細については、Swift SDKドキュメントの[ストレージ]({{site.baseurl}}/developer_guide/storage?tab=swift)を参照してください。

{% endtab %}
{% endtabs %}

## 使用しているSDKバージョンの確認 {#what-version-of-the-sdk-am-i-on}

ダッシュボードを使用して、**設定** > **アプリ設定**から特定のアプリのSDKバージョンを確認できます。**ライブSDKバージョン**には、ユーザーの5%以上を対象とする最新のライブアプリケーションで使用されている最上位のBraze SDKバージョンが表示されます。

![ワークスペースのSwiftyという名前のアプリ。ライブSDKバージョンは6.6.0です。]({% image_buster /assets/img/live-sdk-version.png %}){: style="max-width:80%"}

{% alert tip %}
iOSアプリをお持ちの場合、**ライブSDKバージョン**が5.0.0（最初にリリースされたSwift SDKのバージョン）以降であれば、従来の[Objective-C iOS SDK]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/overview)の代わりに[Swift SDK]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=swift)を使用していることを確認できます。
{% endalert %}