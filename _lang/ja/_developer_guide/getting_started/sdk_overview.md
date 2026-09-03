---
nav_title: SDKの概要
article_title: 開発者向けのSDK概要
description: "このオンボーディングリファレンス記事には、Braze SDKの開発者向けの技術概要が記載されています。ここでは、SDKでトラッキングされるデフォルトの分析について説明します。"
page_order: 0
---

# [![Braze Learningコース]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/path/developer/sdk-integration-basics){: style="float:right;width:120px;border:0;" class="noimgborder"}開発者向けSDKの概要 {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecompathdevelopersdk-integration-basics-stylefloatrightwidth120pxborder0-classnoimgbordersdk-overview-for-developers}

> Braze SDKの統合を開始する前に、正確に何を構築および統合するのかを疑問に思うかもしれません。また、ニーズに応じてSDKをより詳細にカスタマイズする方法に興味があるかもしれません。この記事は、SDKに関するすべての疑問を解決するのに役立ちます。

SDKの基本的な概要を探しているマーケターは、代わりに[マーケター向けの概要]({{site.baseurl}}/user_guide/get_started/sdk_overview)をご覧ください。

Braze SDKを簡単に説明すると、次のとおりです。
* ユーザーデータを収集し、統合ユーザープロファイルに同期します
* セッションデータ、デバイス情報、プッシュトークンを自動的に収集します
* マーケティングエンゲージメントデータとビジネスに固有のカスタムデータを取得します
* プッシュ通知、アプリ内メッセージ、コンテンツカードメッセージングチャネルを強化します

以下の動画で、Braze SDKの統合の基本とコア機能について簡単に紹介しています。

{% multi_lang_include video.html id="il152jayp0" source="wistia" %}

## アプリのパフォーマンス {#app-performance}

Brazeがアプリのパフォーマンスに悪影響を及ぼすことはありません。

Braze SDKは非常に軽量に設計されています。ネットワークの品質に応じてユーザーデータのフラッシュレートを自動的に変更するほか、手動によるネットワーク制御も可能です。SDKからのAPIリクエストを自動的にバッチ処理することで、最大限のネットワーク効率を維持しながら迅速にデータを記録します。さらに、各API呼び出しでクライアントからBrazeに送信されるデータ量は非常に小さくなっています。

## SDKの互換性 {#sdk-compatibility}

Braze SDKは、非常に行儀よく動作し、アプリ内の他のSDKに干渉しないように設計されています。他のSDKとの非互換性が原因と思われる問題が発生した場合は、Brazeサポートにお問い合わせください。

## デフォルトの分析とセッション処理 {#default-analytics-and-session-handling}

特定のユーザーデータはSDKによって自動的に収集されます。例えば、アプリの初回使用日、アプリの最終使用日、合計セッション数、デバイスOSなどです。統合ガイドに従ってSDKを実装すると、この[デフォルトのデータ収集]({{site.baseurl}}/user_guide/data/unification/user_data/sdk_data_collection)を活用できます。このリストを確認することで、ユーザーに関する同じ情報を重複して保存することを避けられます。セッション開始とセッション終了を除き、自動的にトラッキングされるその他すべてのデータはデータポイント使用量にカウントされません。

{% alert note %}
すべての機能は設定可能ですが、デフォルトのデータ収集モデルを完全に実装することをお勧めします。

<br>ユースケースに応じて必要であれば、統合完了後に[特定のデータの収集を制限する](#blocking-data-collection)ことができます。
{% endalert %}

## データのアップロードとダウンロード {#data-upload-and-download}

Braze SDKはデータ（セッション、カスタムイベントなど）をキャッシュし、定期的にアップロードします。データがアップロードされて初めて、ダッシュボード上の値が更新されます。アップロード間隔はデバイスの状態を考慮し、ネットワーク接続の品質によって制御されます。

|ネットワーク接続品質 |    データフラッシュ間隔|
|---|---|
|良好    |10秒|
|普通    |30秒|
|不良    |60秒|
{: .reset-td-br-1 .reset-td-br-2 aria-label="データのアップロードとダウンロード" }

ネットワーク接続がない場合、データはネットワーク接続が再確立されるまでデバイス上にローカルにキャッシュされます。接続が再確立されると、データはBrazeにアップロードされます。

Brazeは、セッションの開始時に、そのセッション時点でユーザーが該当するセグメントに基づいてSDKにデータを送信します。新しいアプリ内メッセージはセッション中に更新されません。ただし、セッション中のユーザーデータは、クライアントから送信されるたびに継続的に処理されます。たとえば、休眠ユーザー（7日以上アプリを使用していないユーザー）は、アプリに戻った最初のセッションで休眠ユーザー向けのコンテンツを受け取ります。

## データ収集のブロック {#blocking-data-collection}

SDK統合から特定のデータの自動収集をブロックしたり、収集を行うプロセスを許可リストに登録したりすることは可能ですが、推奨されません。

データ収集のブロックは推奨されません。分析データを除去すると、プラットフォームのパーソナライゼーションやターゲティングの能力が低下するためです。例:

- いずれかのSDKでロケーションを完全に統合しない場合、言語やロケーションに基づいたメッセージングのパーソナライゼーションができなくなります。
- タイムゾーンを統合しない場合、ユーザーのタイムゾーンに合わせたメッセージ送信ができなくなる可能性があります。
- 特定のデバイスのビジュアル情報を統合しない場合、メッセージコンテンツがそのデバイスに最適化されない可能性があります。

製品の機能を最大限に活用するために、SDKを完全に統合することを強くお勧めします。

{% tabs %}
{% tab Web SDK %}

SDKの特定の部分を統合しないか、ユーザーに対して[`disableSDK`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#disablesdk)を使用できます。このメソッドは`disableSDK()`が呼び出される前にログに記録されたデータを同期し、このページおよび将来のページ読み込みに対するBraze Web SDKへの後続のすべての呼び出しを無視します。後からデータ収集を再開する場合は、[`enableSDK()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#enablesdk)メソッドを使用してデータ収集を再開できます。詳細については、[Webトラッキングの無効化]({{site.baseurl}}/developer_guide/analytics/managing_data_collection?sdktab=web)の記事をご覧ください。

{% endtab %}
{% tab Android SDK %}

[`setDeviceObjectAllowlist`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-device-object-allowlist.html?query=fun%20setDeviceObjectAllowlist(deviceObjectAllowlist:%20EnumSet%3CDeviceKey%3E):%20BrazeConfig.Builder)を使用して、設定した許可リストに従ってデバイスオブジェクトのキーまたは値のサブセットのみを送信するようにSDKを構成できます。これは[`setDeviceObjectAllowlistEnabled`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-device-object-allowlist-enabled.html?query=fun%20setDeviceObjectAllowlistEnabled(enabled:%20Boolean):%20BrazeConfig.Builder)で有効にする必要があります。

{% alert important %}
空の許可リストを設定すると、デバイスデータはBrazeに**一切**送信されなくなります。
{% endalert %}

{% endtab %}
{% tab Swift SDK %}

`Braze.Configuration`の[`configuration.devicePropertyAllowList`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/devicepropertyallowlist)に対象フィールドのセットを割り当てることで、SDKが収集するデバイスフィールドの許可リストを指定できます。フィールドの完全なリストは[`Braze.Configuration.DeviceProperty`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/deviceproperty)で定義されています。すべてのデバイスフィールドの収集を無効にするには、このプロパティの値を空のセット（`[]`）に設定します。

{% alert important %}
デフォルトでは、すべてのフィールドがBraze Swift SDKによって収集されます。一部のデバイスプロパティを削除すると、SDK機能が無効になる場合があります。
{% endalert %}

使用方法の詳細については、Swift SDKドキュメントの[Speicher]({{site.baseurl}}/developer_guide/storage?tab=swift)を参照してください。

{% endtab %}
{% endtabs %}

## 使用しているSDKのバージョンは？ {#what-version-of-the-sdk-am-i-on}

ダッシュボードで特定のアプリのSDKバージョンを確認するには、**設定 > アプリ設定**にアクセスします。**ライブSDKバージョン**には、ユーザーの少なくとも5%が使用している最新のライブアプリケーションで使用されている最も高いBraze SDKバージョンが表示されます。

![ワークスペース内のSwiftyという名前のアプリ。ライブSDKバージョンは6.6.0です。]({% image_buster /assets/img/live-sdk-version.png %}){: style="max-width:80%"}

{% alert tip %}
iOSアプリをお持ちの場合、**ライブSDKバージョン**が5.0.0以上であれば、レガシーの[Objective-C iOS SDK]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/overview)ではなく[Swift SDK]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=swift)を使用していることを確認できます。5.0.0はSwift SDKの最初のリリースバージョンです。
{% endalert %}