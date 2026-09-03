---
nav_title: セグメント
article_title: セグメント
page_order: 1
alias: /partners/segment/
description: "このリファレンス記事では、Brazeとセグメントのパートナーシップについて概説します。セグメントは、マーケティングスタックのソース間で情報を収集し、ルーティングする顧客データプラットフォームです。"
page_type: partner
search_tag: Partner

---

# セグメント {#segment}

{% multi_lang_include video.html id="RfOHfZ34hYM" align="right" %}

> [セグメント](https://segment.com)は、顧客データの収集、クリーンアップ、およびアクティブ化を支援する顧客データプラットフォームです。

Brazeとセグメントの統合により、ユーザーを追跡し、さまざまなユーザー分析プロバイダーにデータを転送できます。セグメントでは次の操作を行うことができます。

- Brazeのキャンペーンとキャンバスのセグメンテーションで使用するために、[セグメント Engage]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/segment/segment_engage)をBrazeに同期する。
- [2つのプラットフォーム間でデータをインポートする](#integration-options)。Android、iOS、およびWebアプリケーション用のサイドバイサイドSDK統合と、Braze REST APIにデータを同期するサーバー間統合を提供しています。
- [Currentsを介してデータをセグメントに接続する]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/segment/segment_for_currents)。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| ----------- | ----------- |
| セグメントアカウント | このパートナーシップを活用するには、[セグメントアカウント](https://app.segment.com/login)が必要です。 |
| インストール済みのソースとセグメントソース[ライブラリ](https://segment.com/docs/sources/) | モバイルアプリ、Webサイト、バックエンドサーバーなど、セグメントに送信されるすべてのデータの発生元です。<br><br>`Source > Destination`フローを正しく設定するには、事前にアプリ、サイト、またはサーバーにライブラリをインストールする必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## 統合 {#integration}

Brazeとセグメントを統合するには、[選択した統合タイプ](#integration-options)（接続モード）に従って、[Brazeを送信先として設定](#connection-settings)する必要があります。Brazeを初めてご利用のお客様は、[セグメント replays](#segment-replays)を使用して履歴データをBrazeに転送できます。次に、[マッピング](#methods)を設定し、[統合をテスト](#step-4-test-your-integration)して、Brazeとセグメント間のスムーズなデータフローを確認する必要があります。

### ステップ 1:Braze送信先を作成する {#connection-settings}

ソースの設定が正常に完了したら、各ソース（iOS、Android、Webなど）に対してBrazeを[送信先](https://segment.com/docs/destinations/)として設定する必要があります。接続設定を使用して、Brazeとセグメント間のデータフローをカスタマイズするための多くのオプションがあります。

### ステップ 2:送信先フレームワークと接続タイプを選択する {#integration-options}

セグメントで、**Destinations** > **Braze** > **Configure Braze** > **Select your Source** > **Setup**に移動します。

![ソース設定ページ。このページには、送信先フレームワークを「actions」または「classic」に設定し、接続モードを「cloud mode」または「device mode」に設定するための設定が含まれています。]({% image_buster /assets/img/segment/setup.png %})

セグメントのウェブソース（Analytics.js）およびネイティブのクライアントサイドライブラリは、サイドバイサイド（デバイスモード）統合またはサーバー間（クラウドモード）統合のいずれかを使用してBrazeと統合できます。

接続モードの選択は、送信先が設定されているソースのタイプによって決まります。

| 統合 | 詳細 |
| ----------- | ------- |
| [サイドバイサイド<br>（デバイスモード）](#side-by-side-sdk-integration) | セグメントのSDKを使用してイベントをBrazeのネイティブ呼び出しに変換し、サーバー間統合よりも深い機能へのアクセスとBrazeのより包括的な使用を可能にします。<br><br>セグメントはすべてのメソッド（たとえばContent Cards）をサポートしているわけではないことに注意してください。対応するマッピングを通じてマッピングされていないBrazeメソッドを使用するには、コードベースにネイティブのBrazeコードを追加してメソッドを呼び出す必要があります。 |
| [サーバー間<br>（クラウドモード）](#server-to-server-integration) | セグメントからBraze REST APIエンドポイントにデータを転送します。<br><br>アプリ内メッセージ、Content Cards、プッシュ通知などのBraze UI機能はサポートされていません。また、デバイスレベルのフィールドなど、この方法では利用できない自動キャプチャデータも存在します。<br><br>これらの機能を使用したい場合は、サイドバイサイド統合を検討してください。|
{: .reset-td-br-1 .reset-td-br-2 aria-label="ステップ 2：送信先フレームワークと接続タイプを選択する" }

{% alert note %}
2つの統合オプション（接続モード）の詳細とそれぞれのメリットについては、[セグメント](https://segment.com/docs/destinations/#connection-modes)を参照してください。
{% endalert %}

#### サイドバイサイドSDK統合 {#side-by-side-sdk-integration}

デバイスモードとも呼ばれるこの統合は、セグメントのSDKと[メソッド](#methods)をBraze SDKにマッピングし、プッシュ、アプリ内メッセージ、その他のBrazeネイティブメソッドなど、SDKが提供するすべての機能にアクセスできるようにします。

{% alert note %}
セグメントのデバイスモードを使用する場合は、セグメントにBrazeを初期化させてください。アプリ内でBraze SDKを別途初期化しないでください。送信先プラグインがBrazeを設定し、セッションを開始します。2回目のネイティブ初期化を行うとセッションが重複して記録される可能性があります。セグメントの`identify`を使用してユーザーIDを設定してください。プラグインはその呼び出しを`changeUser()`にマッピングします。
{% endalert %}

{% alert important %}
モバイルでのデバイスモード統合の場合、セグメントダッシュボードで送信先を設定するだけでなく、Braze送信先プラグインをアプリに追加する必要があります。セグメント SDKにはデフォルトでBrazeプラグインが含まれていません。プラグインがない場合、セグメント SDKはデータやマッピングされたメソッド呼び出しをBrazeに転送できず、プッシュ、アプリ内メッセージ、Content Cardsなどの機能が動作しません。インストール手順については、このセクションのプラットフォーム固有のタブを参照してください。
{% endalert %}

デバイスモード接続を使用する場合、Braze SDKをネイティブに統合する場合と同様に、Braze SDKはすべてのユーザーに`device_id`とバックエンド識別子である`braze_id`を割り当てます。これにより、Brazeは`userId`の代わりにこれらの識別子を照合してデバイスからの匿名アクティビティをキャプチャできます。

{% alert note %}
デバイスモード（KotlinまたはSwift）の送信先で[送信先フィルター](https://segment.com/docs/connections/destinations/destination-filters/)を使用する場合、フィルターサポートを有効にして送信先プラグインを設定する必要があります。サポートされているプラグインバージョンの詳細については、セグメントの[送信先フィルターのドキュメント](https://segment.com/docs/connections/destinations/destination-filters/)を参照してください。
{% endalert %}

{% tabs local %}
{% tab Android %}

{% alert important %}
Android デバイスモード統合のソースコードはBrazeが管理しており、新しいBraze SDKリリースを反映して定期的に更新されます。

<br>
使用するBraze SDKは、使用するセグメント SDKによって異なります：

| | セグメント SDK | Braze SDK |
| - | ----------- | --------- |
| 推奨 | [Analytics-Kotlin](https://github.com/segmentio/analytics-kotlin) | [Braze セグメント Kotlin](https://github.com/braze-inc/braze-segment-kotlin) |
| レガシー | [Analytics-Android](https://github.com/segmentio/analytics-android) | [Braze セグメント Android](https://github.com/braze-inc/braze-segment-android) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="サイドバイサイドSDK統合" }


{% endalert %}

Androidソースのデバイスモード送信先としてBrazeを設定するには、**送信先フレームワーク**として**Actions**を選択し、**Save**を選択します。

サイドバイサイド統合を完了するには、[Braze Kotlin送信先プラグイン](https://segment.com/docs/connections/sources/catalog/libraries/mobile/kotlin-android/destination-plugins/braze-kotlin-android/)をAndroidアプリに追加する必要があります。このプラグインはセグメント SDKとBraze SDKをブリッジし、デバイスモードのデータをBrazeにフローさせます。セグメントのインストール手順に従って、プラグインの依存関係を追加し、セグメント analyticsインスタンスで初期化してください。

[Androidデバイスモード](https://github.com/braze-inc/braze-segment-kotlin)統合のソースコードはBrazeが管理しており、新しいBraze SDKリリースを反映して定期的に更新されます。

{% endtab %}
{% tab iOS %}

{% alert important %}
iOSデバイスモード統合のソースコードはBrazeが管理しており、新しいBraze SDKリリースを反映して定期的に更新されます。

<br>
使用するBraze SDKは、使用するセグメント SDKによって異なります：

| | セグメント SDK | Braze SDK |
| - | ----------- | --------- |
| 推奨 | [Analytics-Swift](https://github.com/segmentio/analytics-swift) | [Braze セグメント Swift](https://github.com/braze-inc/braze-segment-swift) |
| レガシー | [Analytics-iOS](https://github.com/segmentio/analytics-ios) | [Braze セグメント iOS](https://github.com/Appboy/appboy-segment-ios) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="サイドバイサイドSDK統合" }
{% endalert %}

iOSソースのデバイスモード送信先としてBrazeを設定するには、**送信先フレームワーク**として**Actions**を選択し、**Save**を選択します。

サイドバイサイド統合を完了するには、[Braze Swift送信先プラグイン](https://segment.com/docs/connections/sources/catalog/libraries/mobile/apple/destination-plugins/braze-swift/)をiOSアプリに追加する必要があります。このプラグインはセグメント SDKとBraze SDKをブリッジし、デバイスモードのデータをBrazeにフローさせます。セグメントのインストール手順に従って、プラグインの依存関係（Swift Package ManagerまたはCocoaPods経由）を追加し、セグメント analyticsインスタンスで初期化してください。

[iOSデバイスモード](https://github.com/braze-inc/braze-segment-swift)統合のソースコードはBrazeが管理しており、新しいBraze SDKリリースを反映して定期的に更新されます。

{% endtab %}
{% tab Web or JavaScript %}

セグメントのBraze Web Mode (Actions) フレームワークは、ウェブソースのデバイスモード送信先としてBrazeを設定する際に推奨されます。

セグメントで、送信先フレームワークとして**Actions**を、接続モードとして**Device Mode**を選択します。

![Actionsフレームワークとデバイスモードが選択されたセグメント送信先設定。]({% image_buster /assets/img/segment/website.png %})

{% endtab %}
{% tab React Native %}
[React Native Brazeプラグイン](https://github.com/segmentio/analytics-react-native/tree/master/packages/plugins/plugin-braze)のソースコードはセグメントが管理しており、新しいBraze SDKリリースを反映して定期的に更新されます。

React Native セグメントソースをBrazeに接続する場合、オペレーティングシステムごとにソースと送信先を設定する必要があります。たとえば、iOS送信先とAndroid送信先をそれぞれ設定します。

アプリのコードベース内で、デバイスタイプに応じて条件分岐でセグメント SDKを初期化し、各アプリに関連付けられたそれぞれのソースライトキーを使用します。

プッシュトークンがデバイスから登録されBrazeに送信されると、SDKの初期化時に使用されたアプリ識別子に関連付けられます。デバイスタイプの条件分岐による初期化は、Brazeに送信されるプッシュトークンが適切なアプリに関連付けられることを確認するのに役立ちます。

{% alert important %}
React Nativeアプリがすべてのデバイスで同じBrazeアプリ識別子を使用してBrazeを初期化する場合、すべてのReact NativeユーザーはBrazeでAndroidまたはiOSユーザーとみなされ、すべてのプッシュトークンがそのオペレーティングシステムに関連付けられます。
{% endalert %}

各ソースのデバイスモード送信先としてBrazeを設定するには、**送信先フレームワーク**として**Actions**を選択し、**Save**を選択します。

{% endtab %}
{% endtabs %}

#### サーバー間統合 {#server-to-server-integration}

クラウドモードとも呼ばれるこの統合は、セグメントからBraze REST APIにデータを転送します。セグメントの[Braze Cloud Mode (Actions)](https://segment.com/docs/connections/destinations/catalog/braze-cloud-mode-actions/)フレームワークを使用して、任意のソースに対してクラウドモード送信先を設定します。

サイドバイサイド統合とは異なり、サーバー間統合ではアプリ内メッセージ、Content Cards、自動プッシュトークン登録などのBraze UI機能はサポートされていません。また、クラウドモードでは利用できない[自動キャプチャ]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection#user-data-collection)データ（匿名ユーザーやデバイスレベルのフィールドなど）も存在します。

このデータやこれらの機能を使用したい場合は、サイドバイサイド（デバイスモード）SDK統合の使用を検討してください。

[Braze Cloud Mode (Actions) 送信先](https://github.com/segmentio/action-destinations/tree/main/packages/destination-actions/src/destinations/braze)のソースコードはセグメントが管理しています。

### ステップ 3:設定 {#step-3-settings}

送信先の設定を定義します。すべての設定がすべての送信先タイプに適用されるわけではありません。

{% tabs local %}
{% tab モバイルデバイスモード %}

| 設定 | 説明 |
| ------- | ----------- |
| アプリ識別子 | 特定のアプリを参照するために使用されるアプリ識別子。Brazeダッシュボードの**設定の管理**で確認できます。 |
| カスタムAPIエンドポイント<br>（SDKエンドポイント） | インスタンスに対応するBraze SDKエンドポイント（例：`sdk.iad-01.braze.com`） |
| エンドポイントリージョン | Brazeインスタンス（例：US 01、US 02、EU 01など） |
| 自動アプリ内メッセージ登録を有効にする | アプリ内メッセージを手動で登録したい場合はこれを無効にしてください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ステップ 3：設定" }

{% endtab %}
{% tab Webデバイスモード %}

| 設定 | 説明 |
| ------- | ----------- |
| アプリ識別子 | 特定のアプリを参照するために使用されるアプリ識別子。Brazeダッシュボードの**設定の管理**で確認できます。 |
| カスタムAPIエンドポイント<br>（SDKエンドポイント） | インスタンスに対応するBraze SDKエンドポイント（例：`sdk.iad-01.braze.com`） |
| Safari Webサイトプッシュ ID | Safariプッシュをサポートする場合、Safariプッシュ証明書を作成する際にAppleに提供したWebサイトプッシュIDでこのオプションを指定する必要があります（`web`で始まります。例：`web.com.example.domain`）。 |
| Braze Web SDKバージョン | 使用したいBraze Web SDKのバージョン |
| アプリ内メッセージを自動送信 | デフォルトでは、ユーザーが対象となるすべてのアプリ内メッセージが自動的に配信されます。アプリ内メッセージを手動で表示したい場合はこれを無効にしてください。 |
| Font Awesomeを読み込まない | Brazeはアプリ内メッセージのアイコンにFont Awesomeを使用します。デフォルトでは、BrazeはFontAwesome CDNからFontAwesomeを自動的に読み込みます。この動作を無効にするには（たとえば、サイトがFontAwesomeのカスタマイズ版を使用している場合）、このオプションを`TRUE`に設定します。この場合、サイトにFontAwesomeが読み込まれていることを確認する責任があります。そうしないと、アプリ内メッセージが正しくレンダリングされない場合があります。 |
| HTMLアプリ内メッセージを有効にする | このオプションを有効にすると、Brazeダッシュボードユーザーがアプリ内メッセージでHTMLを使用できるようになります。 |
| アプリ内メッセージを新しいタブで開く | デフォルトでは、アプリ内メッセージのクリックからのリンクは、ダッシュボードでメッセージごとに指定されたとおりに、現在のタブまたは新しいタブで読み込まれます。すべてのアプリ内メッセージクリックからのリンクを新しいタブまたはウィンドウで強制的に開くには、このオプションを`TRUE`に設定します。 |
| アプリ内メッセージのzインデックス | このオプションの値を指定して、Brazeのデフォルトのzインデックスをオーバーライドします。 |
| アプリ内メッセージの明示的な閉じを必要とする | デフォルトでは、アプリ内メッセージが表示されているときに、Escapeキーを押すかページのグレーアウトされた背景をクリックするとメッセージが閉じられます。この動作を防止し、メッセージを閉じるために明示的なボタンクリックを必要とするには、このオプションをtrueに設定します。 |
| トリガーアクション間の最小間隔（秒） | デフォルトは30です。<br>デフォルトでは、トリガーアクションは前回のトリガーアクションから少なくとも30秒経過した場合にのみ発火します。この設定オプションの値を指定してデフォルトをオーバーライドできます。通知でユーザーにスパムを送信しないように、この値を10より小さくしないことをお勧めします。 |
| Service Workerの場所 | デフォルトでは、Webプッシュ通知のユーザー登録時に、BrazeはWebサーバーのルートディレクトリ`/service-worker.js`で必要なService Workerファイルを探します。Service Workerをそのサーバーの別のパスでホストしたい場合、ファイルへの絶対パスの値をこのオプションに指定します（例：`/mycustompath/my-worker.js`）。ここで値を設定すると、サイトのプッシュ通知のスコープが制限されることに注意してください。たとえば、この例では、Service Workerファイルが`/mycustompath/`ディレクトリ内にあるため、`requestPushPermission`は`http://yoursite.com/mycustompath/`で始まるWebページからのみ呼び出すことができます。 |
| プッシュトークンメンテナンスを無効にする | デフォルトでは、すでにWebプッシュ許可を付与したユーザーは、新しいセッション時にBrazeバックエンドとプッシュトークンを自動的に同期して配信性を確保します。この動作を無効にするには、このオプションを`FALSE`に設定します。 |
| Service Workerを外部管理する | 独自のService Workerを登録してそのライフサイクルを制御している場合、このオプションを`TRUE`に設定すると、Braze SDKはService Workerの登録や登録解除を行いません。このオプションを`TRUE`に設定した場合、プッシュが正しく機能するためには、`requestPushPermission`を呼び出す前にService Workerを自分で登録し、`self.importScripts('https://js.appboycdn.com/web-sdk-develop/4.1/service-worker.js');`でBraze Service Workerコードを含めるか、そのファイルの内容を直接含める必要があります。このオプションが`TRUE`の場合、`serviceWorkerLocation`オプションは無関係で無視されます。 |
| Content Securityノンス | このオプションに値を指定すると、Braze SDKはSDKによって作成されたすべての`<script>`要素と`<style>`要素にノンスを追加します。これにより、Braze SDKがWebサイトのContent Securityポリシーと連携できるようになります。このノンスの設定に加えて、FontAwesomeの読み込みを許可する必要がある場合があります。これは、Content SecurityポリシーのAllowlistに`use.fontawesome.com`を追加するか、`doNotLoadFontAwesome`オプションを使用して手動で読み込むことで行えます。 |
| クローラーアクティビティを許可する | デフォルトでは、Braze Web SDKはユーザーエージェント文字列に基づいて、Googleなどの既知のスパイダーやWebクローラーからのアクティビティを無視します。これにより、データポイントが節約され、分析がより正確になり、ページランクが向上する可能性があります。ただし、これらのクローラーからのアクティビティをBrazeで記録したい場合は、このオプションを`TRUE`に設定できます。 |
| ログを有効にする | `TRUE`に設定すると、デフォルトでログが有効になります。これにより、Brazeはすべてのユーザーに表示されるJavaScriptコンソールにログを記録します。ページを本番環境にリリースする前に、これを削除するか、`setLogger`で代替ロガーを提供する必要があります。 |
| ユーザー提供のJavaScriptを許可する | デフォルトでは、Braze Web SDKはユーザー提供のJavaScriptクリックアクションを許可しません。これは、Brazeダッシュボードユーザーがサイト上でJavaScriptを実行できるようになるためです。Brazeダッシュボードユーザーが悪意のないJavaScriptクリックアクションを記述することを信頼していることを示すには、このプロパティを`TRUE`に設定します。`enableHtmlInAppMessages`が`TRUE`の場合、このオプションも`TRUE`に設定されます。 |
| アプリバージョン | このオプションに値を指定すると、Brazeに送信されるユーザーイベントが指定されたバージョンに関連付けられ、ユーザーセグメンテーションに使用できます。 |
| セッションタイムアウト（秒） | デフォルトは30です。<br>デフォルトでは、セッションは30分の非アクティブ後にタイムアウトします。この設定オプションの値を指定してデフォルトをオーバーライドできます。 |
| デバイスプロパティAllowlist | デフォルトでは、Braze SDKは`DeviceProperties`のすべてのデバイスプロパティを自動的に検出して収集します。この動作をオーバーライドするには、`DeviceProperties`の配列を指定します。一部のプロパティがないと、すべての機能が正しく機能しない場合があることに注意してください。たとえば、ローカルタイムゾーン配信はタイムゾーンなしでは機能しません。 |
| ローカライゼーション | デフォルトでは、SDKが生成するユーザー向けメッセージはユーザーのブラウザ言語で表示されます。この動作をオーバーライドして特定の言語を強制するには、このオプションの値を指定します。このオプションの値はISO 639-1言語コードである必要があります。 |
| Cookieなし | デフォルトでは、Braze SDKは少量のデータ（ユーザーID、セッションID）をCookieに保存します。これにより、Brazeがサイトの異なるサブドメイン間でユーザーとセッションを認識できるようになります。これが問題となる場合、このオプションに`TRUE`を渡してCookieストレージを無効にし、HTML 5 localStorageのみに依存してユーザーとセッションを識別します。 |
| すべてのページをトラック | **Classic Destination Webデバイスモード（メンテナンス）のみ**<br><br>セグメントでは、この設定を[マッピングを通じて有効にできる](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#braze-web-settings-mapping)Web Actionsフレームワーク送信先への移行を推奨しています。<br><br>すべての[Pageコール](https://segment.com/docs/spec/page/)を「Loaded/Viewed a Page」イベントとしてBrazeに送信します。 |
| 名前付きページのみをトラック | **Classic Destination Webデバイスモード（メンテナンス）のみ**<br><br>セグメントでは、この設定を[マッピングを通じて有効にできる](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#braze-web-settings-mapping)Web Actionsフレームワーク送信先への移行を推奨しています。<br><br>名前が関連付けられたPageコールのみをBrazeに送信します。 |
| 収益がある場合に購入を記録 | **Classic Destination Webデバイスモード（メンテナンス）のみ**<br><br>セグメントでは、この設定を[マッピングを通じて有効にできる](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#braze-web-settings-mapping)Web Actionsフレームワーク送信先への移行を推奨しています。<br><br>このオプションを有効にすると、revenueプロパティを含むすべてのTrackコールが購入イベントをトリガーします。 |
| 既知のユーザーのみをトラック | **Classic Destination Webデバイスモード（メンテナンス）のみ**<br><br>セグメントでは、この設定をマッピングを通じて有効にできるWeb Actionsフレームワーク送信先への移行を推奨しています。<br><br>有効にすると、この新しい設定は有効な`userId`が存在するまで`window.braze.initialize`の呼び出しを遅延させます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ステップ 3：設定" }

{% endtab %}
{% tab クラウドモード %}

| 設定 | 説明 |
| ------- | ----------- |
| アプリ識別子 | 特定のアプリを参照するために使用されるアプリ識別子。Brazeダッシュボードの**設定の管理**で確認できます。 |
| REST APIキー | Brazeダッシュボードの**設定** > **APIキー**で確認できます。 |
| カスタムREST APIエンドポイント | インスタンスに対応するBraze RESTエンドポイント（例：rest.iad-01.braze.com）。 |
| 既存ユーザーのみを更新 | **Classic Destination クラウドモード（メンテナンス）のみ**<br><br>セグメントでは、この設定を[マッピングを通じて有効にできる](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#braze-web-settings-mapping)Cloud Actionsフレームワーク送信先への移行を推奨しています。<br><br>既存ユーザーのみを更新するかどうかを決定します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ステップ 3：設定" }

{% endtab %}
{% endtabs %}

### ステップ 4:メソッドをマッピングする {#methods}

Brazeは、セグメントの[Page](https://segment.com/docs/connections/sources/catalog/libraries/website/javascript/#page)、[Identify](https://segment.com/docs/spec/identify/)、および[Track](https://segment.com/docs/spec/track/)メソッドをサポートしています。これらのメソッド内で使用される識別子のタイプは、データがサーバー間（クラウドモード）統合で送信されるか、サイドバイサイド（デバイスモード）統合で送信されるかによって異なります。Braze Web Mode ActionsおよびCloud Mode Actions送信先では、[セグメント aliasコール](https://segment.com/docs/connections/spec/alias/)のマッピングを設定することもできます。

{% alert note %}
Braze Cloud Mode (Actions) 送信先では識別子としてユーザーエイリアスがサポートされていますが、セグメントのaliasコールは直接Brazeのユーザーエイリアスとは関連していないことに注意してください。
{% endalert %}

| 識別子タイプ | サポートされる送信先 |
| --------------- | --------------------- |
| `userId` (`external_id`) | すべて |
| 匿名ユーザー | デバイスモード送信先 |
| ユーザーエイリアス | クラウドモード送信先 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ステップ 4：メソッドをマッピングする" }

Cloud Mode (Actions) 送信先には、エイリアスのみのユーザーを作成するか、既存の`external_id`プロファイルにエイリアスを追加するために使用できる[Create Aliasアクション](https://segment.com/docs/connections/destinations/catalog/actions-braze-cloud/#create-alias)が用意されています。[Identify Userアクション](https://segment.com/docs/connections/destinations/catalog/actions-braze-cloud/#identify-user)をCreate Aliasアクションと併用して、ユーザーに`external_id`が利用可能になった後にエイリアスのみのユーザーを`external_id`とマージできます。

`braze_id`を使用してクラウドモードで匿名ユーザーデータを送信する回避策を構築することも可能です。これには、すべてのセグメント API呼び出しにユーザーの`braze_id`を手動で含める必要があります。この回避策の設定方法の詳細については、[セグメントのドキュメント](https://segment.com/docs/connections/destinations/catalog/braze/#capture-the-braze_id-of-anonymous-users)を参照してください。

Cloud Mode Actions内でBrazeに送信される送信先データはバッチ処理が可能です。バッチサイズは75イベントを上限とし、これらのバッチは30秒間蓄積された後にフラッシュされます。リクエストのバッチ処理はアクションごとに行われます。たとえば、Identifyコール（属性）は1つのリクエストにバッチされ、Trackコール（カスタムイベント）は2番目のリクエストにバッチされます。セグメントからBrazeへのリクエスト数が削減されるため、この機能を有効にすることをBrazeは推奨しています。これにより、送信先がBrazeのレート制限に達してリクエストをリトライするリスクも軽減されます。

アクションのバッチ処理を有効にするには、Braze送信先 > **Mappings**に移動します。そこから、マッピングの横にある3点アイコンをクリックし、**Edit Mapping**を選択します。**Select mappings**セクションの一番下までスクロールし、**Batch Data to Braze**が**Yes**に設定されていることを確認します。


{% tabs local %}
{% tab Identify %}
#### Identify

[Identify](https://segment.com/docs/spec/identify/)コールを使用すると、ユーザーをアクションに結び付け、属性を記録できます。

特定のセグメント特別トレイトは、Brazeの標準属性プロファイルフィールドにマッピングされます：

| セグメント特別トレイト | Braze標準属性 |
| ------------- | ----------- |
| `userId` | `external_id` |
| `firstName` | `first_name` |
| `lastName` | `last_name` |
| `email` | `email` |
| `birthday` | `dob` |
| `address.country` | `country` |
| `address.city` | `home_city` |
| `gender` | `gender` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Identify" }

`email_subscribe`や`push_subscribe`などの他の予約済みBrazeプロファイルフィールドは、これらのフィールドのBraze命名規則を使用し、Identifyコール内のトレイトとして渡すことで送信できます。

##### 購読グループへのユーザーの追加 {#adding-a-user-to-a-subscription-group}

トレイトパラメーター内の以下のフィールドを使用して、特定の購読グループにユーザーを購読または購読解除することもできます。

`braze_subscription_groups`と呼ばれる予約済みBrazeプロファイルフィールドを使用します。これはオブジェクトの配列に関連付けることができます。配列内の各オブジェクトには2つの予約キーが必要です：

1. `subscription_group_state`：ユーザーが特定の購読グループに`"subscribed"`（購読済み）か`"unsubscribed"`（購読解除済み）かを示します。
2. `subscription_group_id`：購読グループの一意のIDを表します。このIDはBrazeダッシュボードの**Subscription Group Management**で確認できます。

{% subtabs %}
{% subtab Swift %}
```swift
analytics.identify(
  userId: "{your-user}",
  traits: [
    "braze_subscription_groups": [
      [
        "subscription_group_id": "{your-group-id}",
        "subscription_group_state": "subscribed"
      ],
      [
        "subscription_group_id", "{your-group-id}",
        "subscription_group_state": "unsubscribed"
      ]
    ]
  ]
)
```
{% endsubtab %}
{% subtab Kotlin %}
```kotlin
analytics.identify(
  "{your-user}",
  buildJsonObject {
    put("braze_subscription_groups", buildJsonArray {
        add(
          buildJsonObject {
            put("subscription_group_id", "{your-group-id}")
            put("subscription_group_state", "subscribed")
          }
        )
        add(
          buildJsonObject {
            put("subscription_group_id", "{your-group-id}")
            put("subscription_group_state", "unsubscribed")
          }
        )
      }
    )
  }
)
```
{% endsubtab %}
{% subtab TypeScript %}
```typescript
analytics.identify(
  "{your-user}",
  {
    braze_subscription_groups: [
      {
        subscription_group_id: "{your-group-id}",
        subscription_group_state: "subscribed"
      },
      {
        subscription_group_id: "{your-group-id}",
        subscription_group_state: "unsubscribed"
      }
    ]
  }
)
```
{% endsubtab %}
{% endsubtabs %}

##### カスタム属性 {#custom-attributes}

その他のすべてのトレイトは[カスタム属性]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes)として記録されます。

| セグメントメソッド | Brazeメソッド | 例 |
|---|---|---|
| ユーザーIDでIdentify | External IDを設定 | セグメント: `analytics.identify("dawei");`<br>Braze: `Braze.changeUser("dawei")` |
| 予約済みトレイトでIdentify | ユーザー属性を設定 | セグメント: `analytics.identify({email: "dawei@braze.com"});`<br> Braze: `Braze.getUser().setEmail("dawei@braze.com");`
| カスタムトレイトでIdentify | カスタム属性を設定 | セグメント: `analytics.identify({fav_cartoon: "Naruto"});`<br>Braze: `Braze.getUser().setCustomAttribute("fav_cartoon": "Naruto")`;
| ユーザーIDとトレイトでIdentify | セグメント: External IDと属性を設定 | 上記のメソッドを組み合わせます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="カスタム属性" }

[Web Mode Actions](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#update-user-profile)および[Cloud Mode Actions](https://segment.com/docs/connections/destinations/catalog/braze-cloud-mode-actions/#update-user-profile)送信先では、Update User Profileアクションを使用してこれらのマッピングを設定できます。

{% alert important %}
ユーザー属性データを渡す際は、前回の更新以降に変更された属性の値のみを渡していることを確認してください。これにより、データポイントの不必要な消費を避けることができます。クライアントサイドソースの場合、セグメントのオープンソース[Middleware](https://github.com/segmentio/segment-braze-mobile-middleware)ツールを使用して統合を最適化し、セグメントからの重複する`identify()`コールのデバウンスによりデータポイント使用量を制限できます。

{% endalert %}
{% endtab %}

{% tab Track %}
#### Track

イベントをトラックすると、指定された名前を使用して[カスタムイベント]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events#custom-events)として記録されます。

Trackコールのpropertiesオブジェクト内で送信されたメタデータは、関連するイベントのカスタムイベントプロパティとしてBrazeに記録されます。すべての[カスタムイベントプロパティのデータ型]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties)がサポートされています。

[Web Mode Actions](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#track-event)および[Cloud Mode Actions](https://segment.com/docs/connections/destinations/catalog/braze-cloud-mode-actions/#track-event)送信先では、Track Eventアクションを使用してこれらのマッピングを設定できます。

| セグメントメソッド | Brazeメソッド | 例 |
|---|---|---|
| [Track](https://segment.com/docs/spec/track/) | [カスタムイベント]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events#custom-events)として記録されます。 | セグメント: `analytics.track("played_game");` <br>Braze: `Braze.logCustomEvent("played_game");`|
| [プロパティ付きTrack](https://segment.com/docs/spec/track/) | [イベントプロパティ]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties)として記録されます。 | セグメント: `analytics.track("played_game", {name: "BotW", weapon: "boomerang"});` <br>Braze: `Braze.logCustomEvent("played_game", { "name": "BotW", "weapon": "boomerang"});` |
| [製品付きTrack](https://segment.com/docs/spec/track/) | [購入イベント]({{site.baseurl}}/developer_guide/analytics/logging_purchases/?tab=web)として記録されます。 | セグメント: `analytics.track("Order Completed", {products: [product_id: "ab12", price: 19]});` <br>Braze: `Braze.logPurchase("ab12", 19);` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Track" }

##### 注文完了 {#order-completed}

セグメントの[eCommerce API](https://segment.com/docs/spec/ecommerce/v2/)で説明されている形式を使用して`Order Completed`という名前のイベントをトラックすると、リストされた製品が[購入]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data#revenue-data)として記録されます。

[Web Mode Actions](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#track-purchase)および[Cloud Mode Actions](https://segment.com/docs/connections/destinations/catalog/braze-cloud-mode-actions/#track-purchase)送信先では、Track Purchaseアクションを通じてデフォルトのマッピングをカスタマイズできます。

{% endtab %}

{% tab Page %}
#### Page {#page}

[Page](https://segment.com/docs/spec/page/)コールを使用すると、ユーザーがWebサイトのページを表示するたびに、ページに関するオプションのプロパティとともに記録できます。

このイベントタイプは、Web Mode ActionsおよびCloud Actions送信先でトリガーとして使用し、Brazeにカスタムイベントを記録できます。
{% endtab %}

{% endtabs %}

### ステップ 5:統合をテストする {#step-5-test-your-integration}

サイドバイサイド（デバイスモード）統合を使用する場合、[概要]({{site.baseurl}}/user_guide/analytics/dashboards/home)メトリクス（ライフタイムセッション、MAU、DAU、スティッキネス、デイリーセッション、MAUごとのデイリーセッション）を使用して、Brazeがセグメントからデータを受信していることを確認できます。

データは[カスタムイベント]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_custom_event_data#custom-event-data)ページまたは[収益]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data#revenue-data)ページで表示するか、[セグメントを作成]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment#creating-a-segment)して確認できます。ダッシュボードの**カスタムイベント**ページでは、カスタムイベント数を時系列で表示できます。サーバー間（クラウドモード）統合を使用している場合、MAUおよびDAU統計を含む[数式]({{site.baseurl}}/user_guide/data_and_analytics/creating_a_formula#creating-a-formula)は使用できないことに注意してください。

購入データをBrazeに送信している場合（[ステップ 3](#methods)の**Track**タブの「注文完了」を参照）、[収益]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data#revenue-data)ページで特定の期間の収益や購入に関するデータ、またはアプリの総収益を表示できます。

[セグメントを作成]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment#creating-a-segment)すると、カスタムイベントや属性データに基づいてユーザーをフィルタリングできます。

{% alert important %}
サーバー間統合（クラウドモード）を使用する場合、自動キャプチャされるセッションデータに関連するフィルター（「最初にアプリを使用した日」や「最後にアプリを使用した日」など）は機能しません。セグメントとBrazeの統合でこれらを使用したい場合は、サイドバイサイド統合（デバイスモード）を使用してください。
{% endalert %}

## ユーザーの削除と抑制 {#user-deletion-and-suppression}

ユーザーを削除または抑制する必要がある場合、[セグメントのユーザー削除機能](https://segment.com/docs/privacy/user-deletion-and-suppression/#which-destinations-can-i-send-deletion-requests-to)はBrazeの[`/users/delete`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_delete)に**マッピングされています**。これらの削除の確認には最大30日かかる場合があることに注意してください。

Brazeとセグメント間で共通のユーザー識別子（`external_id`など）を選択する必要があります。セグメントで削除リクエストを開始した後、セグメントダッシュボードの削除リクエストタブでステータスを確認できます。

## セグメントリプレイ {#segment-replays}

セグメントは、すべての過去データを新しいテクノロジーパートナーに「リプレイ」するサービスをクライアントに提供しています。関連する過去のデータをすべてインポートしたい新規Braze顧客は、セグメントを通じてインポートできます。この機能に興味がある場合は、セグメントの担当者にお問い合わせください。

セグメントは[`/users/track`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track)に接続して、お客様に代わってユーザーデータをBrazeにインポートします。

{% alert important %}
Cloud Modeアクション送信先でサポートされているすべての識別子は、セグメントリプレイの一部としてサポートされています。
{% endalert %}

## ベストプラクティス {#best-practices}

{% details データ超過料金を避けるためにユースケースを確認してください。 %}

セグメントでは、クライアントが送信するデータ要素の数に制限は**ありません**。セグメントでは、すべてのイベントを送信するか、Brazeに送信するイベントを選択することができます。セグメントを使用してすべてのイベントを送信するのではなく、マーケティングチームや編集チームとユースケースを確認し、データ超過料金を避けるためにBrazeに送信するイベントを決定することをお勧めします。

{% enddetails %}

{% details モバイルデバイスモードの送信先設定における、カスタムAPIエンドポイントとカスタムREST APIエンドポイントの違いを理解してください。 %}

| Braze用語 | セグメントでの対応 |
| ----------------- | ------------------ |
| Braze SDKエンドポイント | カスタムAPIエンドポイント |
| Braze RESTエンドポイント | カスタムREST APIエンドポイント |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ベストプラクティス" }

Braze APIエンドポイント（セグメントでは「Custom API Endpoint」と呼ばれます）は、BrazeがSDK用にセットアップするSDKエンドポイントです（例：`sdk.iad-03.braze.com`）。Braze REST APIエンドポイント（セグメントでは「Custom REST API Endpoint」と呼ばれます）は、REST APIエンドポイントです（例：`https://rest.iad-03.braze.com`）。
{% enddetails %}

{% details カスタムAPIエンドポイントがモバイルデバイスモードの送信先設定に正しく入力されていることを確認してください。 %}

| Braze用語 | セグメントでの対応 |
| ----------------- | ------------------ |
| Braze SDKエンドポイント | カスタムAPIエンドポイント |
| Braze RESTエンドポイント | カスタムREST APIエンドポイント |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ベストプラクティス" }

Braze SDKエンドポイントを正しく入力するためには、適切なフォーマットに従う必要があります。Braze SDKエンドポイントには `https://` を含めないでください（例：`sdk.iad-03.braze.com`）。含めると、Brazeの統合が機能しなくなります。これは、セグメントがエンドポイントに自動的に `https://` を付加するため、Brazeが無効なエンドポイント `https://https://sdk.iad-03.braze.com` で初期化されてしまうことが原因です。

{% enddetails %}

{% details データマッピングのニュアンス。 %}

データが想定通りに渡されないシナリオ：

1. 階層化カスタム属性
  - [階層化カスタム属性]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support)は技術的にセグメント経由でBrazeに送信できますが、送信のたびに**ペイロード全体**が送信されます。これにより、ペイロードが送信されるたびにネストされたオブジェクトで渡されたキーごとに[データポイント]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support#data-points)が発生します。<br><br> ペイロード送信時にデータポイントのサブセットのみを消費するには、セグメントが提供するカスタム[destination functions](https://segment.com/docs/connections/functions/destination-functions/)機能を使用できます。セグメントプラットフォームのこの機能により、ダウンストリームの送信先へのデータ送信方法をカスタマイズできます。

  {% alert note %}
  カスタムdestination functionsはセグメント内で管理されており、Brazeには外部で設定された機能に関する情報は限られています。
  {% endalert %}

{: start="2"}
2. サーバー間での匿名データの受け渡し。
  - セグメントのサーバー間ライブラリを使用して、匿名データを他のシステムに送信できます。サーバー間（クラウドモード）統合を通じて `external_id` なしでBrazeにユーザーを送信する方法の詳細については、マップメソッドのセクションを参照してください。

{% enddetails %}

{% details Braze初期化のカスタマイズ。 %}

Brazeのカスタマイズには、プッシュ、アプリ内メッセージ、Content Cards、初期化などさまざまな方法があります。サイドバイサイド統合では、直接的なBraze統合と同様に、プッシュ、アプリ内メッセージ、Content Cardsをカスタマイズできます。

ただし、Braze SDKが統合されるタイミングのカスタマイズや初期化設定の指定は、困難な場合や不可能な場合があります。これは、セグメントの初期化が行われる際に、セグメントがBraze SDKを初期化するためです。

{% enddetails %}

{% details Brazeへの差分データの送信。 %}

ユーザー属性データを渡す際には、最後の更新以降に変更された属性の値のみを渡していることを確認してください。これにより、不要なデータポイントの記録を防ぐことができます。クライアント側のソースの場合は、セグメントのオープンソースの[Middleware](https://github.com/segmentio/segment-braze-mobile-middleware)ツールを使用して統合を最適化し、セグメントからの重複する `identify()` コールをデバウンスしてデータポイント使用量を制限できます。

{% enddetails %}

{% details 正しいBrazeデータセンターを使用してください。 %}

セグメントは、サーバー間コールを行うために、Brazeデータセンターを使用して適切なBraze RESTエンドポイント（`https://rest.iad-01.braze.com` など）を取得します。

{% enddetails %}

{% details セグメントのEvent Tester使用時にカスタムREST APIエンドポイントを削除してください。 %}

セグメントのEvent Testerは、Brazeの `/users/track` REST APIエンドポイントにイベントを送信しますが、カスタムREST APIエンドポイントが正しく設定されていても、Brazeの送信先設定にカスタムREST APIエンドポイントが設定されていると `401 Invalid API Key` エラーをスローします。Event Testerを正しく機能させるには、セグメントでカスタムREST APIエンドポイントの値を削除してください。

{% enddetails %}

{% details 新しいソースの設定後は更新に時間をかけてください。 %}

セグメントは設定をキャッシュに長期間保持するため、新しいソースを設定した場合（クラウドモードからデバイスモードへの切り替えなど）、キャッシュが更新されるまでアプリに新しい動作やデータが表示されないことがあります。ソースの追加を計画する際には、この遅延に注意してください。

{% enddetails %}