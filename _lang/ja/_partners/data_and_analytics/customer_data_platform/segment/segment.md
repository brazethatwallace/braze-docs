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

> [セグメント](https://segment.com) は、顧客データの収集、クリーンアップ、およびアクティブ化を支援する顧客データプラットフォームです。

Brazeとセグメントの統合により、ユーザーを追跡し、さまざまなユーザー分析プロバイダーにデータを転送できます。セグメントでは次の操作を行うことができます。

- Brazeのキャンペーンとキャンバスセグメンテーションで使用するために、[セグメント Engage]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/segment/segment_engage/)をBrazeに同期する。
- [2つのプラットフォーム間でデータをインポートする](#integration-options)。Android、iOS、およびWebアプリケーション用のサイドバイサイドSDK統合と、BrazeのREST APIにデータを同期するサーバー間統合を提供しています。
- [Currentsを介してデータをセグメントに接続する]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/segment/segment_for_currents/)。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| ----------- | ----------- |
| セグメントアカウント | このパートナーシップを活用するには、[セグメントアカウント](https://app.segment.com/login)が必要です。 |
| インストールされたソースとセグメントソースの[ライブラリ](https://segment.com/docs/sources/) | モバイルアプリ、Webサイト、バックエンドサーバーなど、セグメントに送信されるデータの提供元。<br><br>適切な `Source > Destination` フローを設定できるようにするには、ライブラリをアプリ、サイト、サーバーにインストールしておく必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 統合 {#integration}

Brazeとセグメントを統合するには、[選択した統合タイプ](#integration-options)（接続モード）に従って、[Brazeを送信先に](#connection-settings)設定する必要があります。Brazeの新規顧客であれば、[セグメントリプレイ](#segment-replays)を使って過去のデータをBrazeにリレーすることができます。次に、Brazeとセグメント間のスムーズなデータフローを確保するために、[マッピング](#methods)を設定し、[統合をテスト](#step-4-test-your-integration)する必要があります。

### ステップ1:Braze送信先を作成する {#connection-settings}

ソースの設定が完了したら、各ソース（iOS、Android、Webなど）の[送信先](https://segment.com/docs/destinations/)としてBrazeを設定する必要があります。接続設定を使用して、Brazeとセグメント間のデータフローをカスタマイズする多くのオプションがあります。

### ステップ2:送信先フレームワークと接続タイプを選択する {#integration-options}

セグメントで、**Destinations** > **Braze** > **Configure Braze** > **Select your Source** > **Setup** と移動します。

![ソースの設定ページ。このページでは、送信先フレームワークを「Actions」または「Classic」のいずれかに設定し、接続モードを「Cloud mode」または「Device mode」のいずれかに設定します。]({% image_buster /assets/img/segment/setup.png %})

セグメントのWebソース（Analytics.js）およびネイティブクライアントサイドライブラリは、サイドバイサイド（デバイスモード）統合またはサーバー間（クラウドモード）統合のいずれかを使用して、Brazeと統合できます。

選択する接続モードは、送信先が設定されているソースのタイプによって決まります。

| 統合 | 詳細 |
| ----------- | ------- |
| [サイドバイサイド<br>（デバイスモード）](#side-by-side-sdk-integration) |セグメントのSDKを使用して、イベントをBrazeのネイティブ呼び出しに変換します。これにより、サーバー間統合よりも高度な機能を利用できるため、Brazeをより包括的に使用できるようになります。<br><br>セグメントは、すべてのBrazeメソッド（Content Cardsなど）に対応しているわけではありません。対応するマッピングを通してマッピングされていないBrazeメソッドを使用するには、コードベースにネイティブのBrazeコードを追加してメソッドを呼び出す必要があります。 |
| [サーバー間<br>（クラウドモード）](#server-to-server-integration) | セグメントからBraze REST APIエンドポイントにデータを転送します。<br><br>アプリ内メッセージ、Content Cards、プッシュ通知などのBraze UI機能には対応していません。また、この方法では利用できないデバイスレベルのフィールドなど、自動的に取得されるデータも存在します。<br><br>これらの機能を使いたい場合は、サイドバイサイドの統合を検討してください。|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 2: Choose destination framework and connection type #integration-options" }

{% alert note %}
2つの統合オプション（接続モード）について、それぞれの利点を含め、詳しくは[セグメント](https://segment.com/docs/destinations/#connection-modes)をご覧ください。
{% endalert %}

#### サイドバイサイドのSDK統合 {#side-by-side-sdk-integration}

デバイスモードとも呼ばれるこの統合では、セグメントのSDKと[メソッド](#methods)がBraze SDKにマッピングされます。これにより、Braze SDKが提供するすべての機能（プッシュ、アプリ内メッセージング、その他のBrazeネイティブのメソッドなど）にアクセスできるようになります。

{% alert note %}
セグメントのデバイスモードを使用する場合、Braze SDKを直接統合する必要はありません。セグメントのデバイスモードの送信先としてBrazeを追加する場合、セグメント SDKはBraze SDKを初期化し、関連するマッピングされたBrazeメソッドを呼び出します。
{% endalert %}

{% alert important %}
モバイルでのデバイスモード統合では、セグメントダッシュボードで送信先を設定するだけでなく、アプリにBraze送信先プラグインを追加する必要があります。セグメント SDKにはデフォルトでBrazeプラグインが含まれていないため、プラグインがないとセグメント SDKはBrazeにデータやマッピングされたメソッド呼び出しを転送できず、プッシュ、アプリ内メッセージ、Content Cardsなどの機能が動作しません。インストール手順については、以下のプラットフォーム別タブを参照してください。
{% endalert %}

デバイスモード接続を使用する場合、Braze SDKをネイティブに統合する場合と同様に、Braze SDKはすべてのユーザーに`device_id`とバックエンド識別子`braze_id`を割り当てます。これによりBrazeは、`userId`の代わりにこれらの識別子を照合することで、デバイスからの匿名アクティビティを取得できます。

{% alert note %}
[送信先フィルター](https://segment.com/docs/connections/destinations/destination-filters/)をデバイスモード（KotlinまたはSwift）の送信先で使用する場合、フィルターサポートを有効にして送信先プラグインを設定する必要があります。サポートされているプラグインバージョンの詳細については、セグメントの[送信先フィルターのドキュメント](https://segment.com/docs/connections/destinations/destination-filters/)を参照してください。
{% endalert %}

{% tabs local %}
{% tab Android %}

{% alert important %}
Androidデバイスモード統合のソースコードはBrazeによって保守されており、新しいBraze SDKのリリースを反映して定期的に更新されます。

<br>
使用するBraze SDKは、使用するセグメント SDKによって異なります。

| | セグメント SDK | Braze SDK |
| - | ----------- | --------- |
| 推奨 | [Analytics-Kotlin](https://github.com/segmentio/analytics-kotlin) | [Braze セグメント Kotlin](https://github.com/braze-inc/braze-segment-kotlin) |
| レガシー | [Analytics-Android](https://github.com/segmentio/analytics-android) | [Braze セグメント Android](https://github.com/braze-inc/braze-segment-android) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Side-by-side SDK integration" }


{% endalert %}

BrazeをAndroidソースのデバイスモード送信先として設定するには、**Destination framework**として**Actions**を選択してから、**Save**を選択します。

サイドバイサイドの統合を完了するには、Androidアプリに[Braze Kotlin送信先プラグイン](https://segment.com/docs/connections/sources/catalog/libraries/mobile/kotlin-android/destination-plugins/braze-kotlin-android/)を追加する必要があります。このプラグインはセグメント SDKとBraze SDKを橋渡しし、デバイスモードのデータをBrazeに流すことができます。セグメントのインストール手順に従って、プラグインの依存関係を追加し、セグメント Analyticsインスタンスで初期化してください。

[Androidデバイスモード](https://github.com/braze-inc/braze-segment-kotlin)統合のソースコードはBrazeによって保守されており、新しいBraze SDKのリリースを反映して定期的に更新されます。

{% endtab %}
{% tab iOS %}

{% alert important %}
iOSデバイスモード統合のソースコードはBrazeによって保守されており、新しいBraze SDKのリリースを反映して定期的に更新されます。

<br>
使用するBraze SDKは、使用するセグメント SDKによって異なります。

| | セグメント SDK | Braze SDK |
| - | ----------- | --------- |
| 推奨 | [Analytics-Swift](https://github.com/segmentio/analytics-swift) | [Braze セグメント Swift](https://github.com/braze-inc/braze-segment-swift) |
| レガシー | [Analytics-iOS](https://github.com/segmentio/analytics-ios) | [Braze セグメント iOS](https://github.com/Appboy/appboy-segment-ios) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Side-by-side SDK integration" }
{% endalert %}

BrazeをiOSソースのデバイスモード送信先として設定するには、**Destination framework**として**Actions**を選択してから、**Save**を選択します。

サイドバイサイドの統合を完了するには、iOSアプリに[Braze Swift送信先プラグイン](https://segment.com/docs/connections/sources/catalog/libraries/mobile/apple/destination-plugins/braze-swift/)を追加する必要があります。このプラグインはセグメント SDKとBraze SDKを橋渡しし、デバイスモードのデータをBrazeに流すことができます。セグメントのインストール手順に従って、プラグインの依存関係（Swift Package ManagerまたはCocoaPods経由）を追加し、セグメント Analyticsインスタンスで初期化してください。

[iOSデバイスモード](https://github.com/braze-inc/braze-segment-swift)統合のソースコードはBrazeによって保守されており、新しいBraze SDKのリリースを反映して定期的に更新されます。

{% endtab %}
{% tab Web or JavaScript %}

Webソースのデバイスモード送信先としてBrazeを設定する場合は、セグメントのBraze Webモード（Actions）フレームワークが推奨されます。

セグメントで、送信先フレームワークとして**Actions**を選択し、接続モードとして**Device Mode**を選択します。

![]({% image_buster /assets/img/segment/website.png %})

{% endtab %}
{% tab React Native %}
[React Native Brazeプラグイン](https://github.com/segmentio/analytics-react-native/tree/master/packages/plugins/plugin-braze)のソースコードはセグメントによって管理されており、新しいBraze SDKリリースを反映するために定期的に更新されます。

React Native セグメントソースをBrazeに接続する場合は、オペレーティングシステムごとにソースと送信先を設定する必要があります。たとえば、iOSの送信先とAndroidの送信先を設定します。

アプリのコードベース内で、各アプリに関連付けられたそれぞれのソース書き込みキーを使用して、デバイスタイプ別にセグメント SDKを条件付きで初期化します。

デバイスからプッシュトークンが登録されBrazeに送信されると、SDKの初期化時に使用されたアプリ識別子に関連付けられます。デバイスタイプの条件付き初期化は、Brazeに送信されるプッシュトークンが関連アプリに関連付けられていることを確認するのに役立ちます。

{% alert important %}
React NativeアプリがすべてのデバイスでBrazeの同じアプリ識別子を使用してBrazeを初期化する場合、すべてのReact NativeユーザーはBrazeでAndroidユーザーまたはiOSユーザーとみなされ、すべてのプッシュトークンはそのオペレーティングシステムに関連付けられます。
{% endalert %}

Brazeを各ソースのデバイスモード送信先として設定するには、**Destination framework**として**Actions**を選択してから、**Save**を選択します。

{% endtab %}
{% endtabs %}

#### サーバー間統合 {#server-to-server-integration}

クラウドモードとも呼ばれるこの統合は、セグメントからBrazeのREST APIにデータを転送します。セグメントの[Brazeクラウドモード（Actions）](https://segment.com/docs/connections/destinations/catalog/braze-cloud-mode-actions/)フレームワークを使用して、任意のソースにクラウドモードの送信先を設定します。

サイドバイサイドの統合とは異なり、サーバー間の統合では、アプリ内メッセージング、Content Cards、自動プッシュトークン登録などのBraze UI機能はサポートされません。また、クラウドモードでは利用できない[自動取得]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/#user-data-collection)データ（匿名ユーザーやデバイスレベルのフィールドなど）も存在します。

このデータとこれらの機能を使用したい場合は、サイドバイサイド（デバイスモード）SDK統合の使用を検討してください。

[Brazeクラウドモード（Actions）送信先](https://github.com/segmentio/action-destinations/tree/main/packages/destination-actions/src/destinations/braze)のソースコードはセグメントによって管理されています。

### ステップ3:設定 {#step-3-settings}

送信先の設定を定義します。すべての設定がすべての送信先タイプに適用されるわけではありません。

{% tabs local %}
{% tab Mobile Device-Mode %}

| 設定 | 説明 |
| ------- | ----------- |
| アプリ識別子 | 特定のアプリを参照するためのアプリ識別子。これは、Brazeダッシュボードの**設定の管理**で確認できます。 |
| カスタムAPIエンドポイント<br>（SDKエンドポイント） | インスタンスに対応するBraze SDKエンドポイント（`sdk.iad-01.braze.com`など） |
| エンドポイントリージョン | Brazeインスタンス（US 01、US 02、EU 01など） |
| アプリ内メッセージの自動登録を有効にする | アプリ内メッセージを手動で登録したい場合は、これを無効にしてください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 3: Settings" }

{% endtab %}
{% tab Web Device-Mode %}

| 設定 | 説明 |
| ------- | ----------- |
| アプリ識別子 | 特定のアプリを参照するためのアプリ識別子。これは、Brazeダッシュボードの**設定の管理**で確認できます。 |
| カスタムAPIエンドポイント<br>（SDKエンドポイント） | インスタンスに対応するBraze SDKエンドポイント（`sdk.iad-01.braze.com`など） |
| Safari WebサイトプッシュID | Safariプッシュをサポートしている場合、Safariプッシュ証明書を作成する際にAppleに提供したWebサイトプッシュID（`web`で始まる、たとえば`web.com.example.domain`）をこのオプションに指定する必要があります。 |
| Braze Web SDKバージョン | 使用したいBraze Web SDKのバージョン |
| アプリ内メッセージを自動送信する | デフォルトでは、ユーザーが受信できるすべてのアプリ内メッセージは、自動的にユーザーに配信されます。アプリ内メッセージを手動で表示したい場合は、これを無効にしてください。 |
| Font Awesomeを読み込まない | Brazeはアプリ内メッセージアイコンにFont Awesomeを使用しています。デフォルトでは、BrazeはFontAwesome CDNからFontAwesomeを自動的に読み込みます。この動作を無効にするには（例えば、サイトがFontAwesomeのカスタマイズ版を使用しているため）、このオプションを`TRUE`に設定します。これを行う場合、FontAwesomeがサイトに読み込まれていることを確認する責任があることに注意してください。そうでない場合、アプリ内メッセージが正しくレンダリングされない可能性があります。 |
| HTMLアプリ内メッセージを有効にする | このオプションを有効にすると、BrazeダッシュボードのユーザーがHTMLアプリ内メッセージを使用できるようになります。 |
| アプリ内メッセージを新しいタブで開く | デフォルトでは、アプリ内メッセージでクリックしたリンクは、現在のタブまたは新しいタブに読み込まれます。どちらのタブになるかは、ダッシュボードでメッセージごとに指定されています。このオプションを`TRUE`に設定すると、アプリ内メッセージのクリックによるすべてのリンクが新しいタブまたはウィンドウで強制的に開かれます。 |
| アプリ内メッセージのzインデックス | このオプションに値を指定してBrazeのデフォルトのz-indexをオーバーライドします。 |
| アプリ内メッセージの明示的な閉じ操作を必須にする | デフォルトでは、アプリ内メッセージが表示されている場合、エスケープボタンを押すか、ページのグレーアウトした背景をクリックすると、メッセージが閉じられます。このオプションをtrueに設定すると、この動作を防ぎ、メッセージを閉じるために明示的なボタンクリックを要求します。 |
| トリガーアクションの最小間隔（秒） | デフォルトは30です。<br>デフォルトでは、トリガーアクションは、前回のトリガーアクションから30秒以上が経過した場合にのみ実行されます。デフォルトを各自の値でオーバーライドするには、この設定オプションに値を指定します。ユーザーへのスパム通知を避けるため、この値を10より小さくすることは推奨しません。|
| サービスワーカーの場所 | デフォルトでは、Webプッシュ通知のためにユーザーを登録するとき、BrazeはWebサーバーのルートディレクトリの`/service-worker.js`にある必要なサービスワーカーファイルを探します。サーバー上の別のパスでサービスワーカーをホストする場合は、このオプションにファイルの絶対パスを指定します（例：`/mycustompath/my-worker.js`）。ここで値を設定すると、サイトでのプッシュ通知の範囲が制限されることに注意してください。たとえば上記の例では、サービスワーカーファイルは`/mycustompath/`ディレクトリ内にあるため、`requestPushPermission`は`http://yoursite.com/mycustompath/`で始まるWebページからのみ呼び出すことができます。 |
| プッシュトークンのメンテナンスを無効にする | デフォルトでは、確実に配信されるようにするため、すでにWebプッシュ通知の権限が付与されているユーザーが、新しいセッションでプッシュトークンをBrazeバックエンドと自動的に同期します。この動作を無効にするには、このオプションを`FALSE`に設定します。 |
| サービスワーカーを外部で管理する | 登録し、ライフサイクルを制御する独自のサービスワーカーがある場合、このオプションを`TRUE`に設定すると、Braze SDKはサービスワーカーを登録または登録解除しません。このオプションを`TRUE`に設定した場合にプッシュを正しく機能させるには、`requestPushPermission`を呼び出す前にサービスワーカーを自身で登録し、`self.importScripts('https://js.appboycdn.com/web-sdk-develop/4.1/service-worker.js');`を使うか、そのファイルの内容を直接含めることで、Brazeサービスワーカーのコードが確実に含まれるようにする必要があります。このオプションが`TRUE`の場合、`serviceWorkerLocation`オプションは無関係であり、無視されます。 |
| コンテンツセキュリティnonce | このオプションに値を指定すると、Braze SDKによって作成されたすべての`<script>`要素と`<style>`要素にnonceが追加されます。これによりBraze SDKは、Webサイトのコンテンツセキュリティポリシーを処理できるようになります。このnonceの設定に加えて、FontAwesomeの読み込みを許可する必要があります。このためには、コンテンツセキュリティポリシー許可リストに`use.fontawesome.com`を追加するか、または`doNotLoadFontAwesome`オプションを使用して手動で読み込みます。 |
| クローラーのアクティビティを許可する | デフォルトでは、Braze Web SDKはユーザーエージェント文字列に基づいて、Googleなどの既知のスパイダーやWebクローラーからのアクティビティを無視します。これによりデータポイントを節約でき、分析がより正確になり、またページランクが向上する可能性があります。ただし、Brazeにこれらのクローラーからのアクティビティを記録させる場合には、このオプションを`TRUE`に設定します。 |
| ロギングを有効にする | デフォルトでロギングを有効にするには、`TRUE`に設定します。これによりBrazeは、すべてのユーザーに対して表示されるJavaScriptコンソールにログを記録することに注意してください。ページを本番環境にリリースする前にこれを削除するか、`setLogger`で代替ロガーを指定する必要があります。 |
| ユーザー提供のJavaScriptを許可する | デフォルトでは、Braze Web SDKは、ユーザー提供のJavaScriptクリックアクションを許可しません。これは、このアクションにより、BrazeダッシュボードのユーザーがサイトでJavaScriptを実行できるようになるためです。Brazeダッシュボードのユーザーが悪意のないJavaScriptクリックアクションを記述することを信頼することを示すには、このプロパティを`TRUE`に設定します。`enableHtmlInAppMessages`が`TRUE`の場合、このオプションも`TRUE`に設定されます。 |
| アプリバージョン | このオプションに値を指定すると、Brazeに送信されたユーザーイベントは、指定したバージョンに関連付けられ、ユーザーセグメンテーションに使用できます。 |
| セッションタイムアウト（秒） | デフォルトは30です。<br>デフォルトでは、セッションは30分間操作がないとタイムアウトします。デフォルトを各自の値でオーバーライドするには、この設定オプションに値を指定します。 |
| デバイスプロパティの許可リスト | デフォルトでは、Braze SDKは`DeviceProperties`のすべてのデバイスプロパティを自動的に検出して収集します。この動作をオーバーライドするには、`DeviceProperties`の配列を指定します。いくつかのプロパティがないと一部の機能が正しく機能しないことがあるので注意してください。たとえば、ローカルタイムゾーンの配信はタイムゾーンなしでは機能しません。 |
| ローカライゼーション | デフォルトでは、SDKにより生成されたユーザーに対して表示されるメッセージはすべて、ユーザーのブラウザーで設定されている言語で表示されます。その動作をオーバーライドして特定の言語を強制するには、このオプションに値を指定します。このオプションの値はISO 639-1言語コードでなければなりません。 |
| Cookieなし | デフォルトでは、Braze SDKは少量のデータ（ユーザーID、セッションID）をCookieに保存します。これは、Brazeがサイトの異なるサブドメイン間でユーザーとセッションを認識できるようにするためです。これで問題が発生する場合は、このオプションに`TRUE`を渡してCookieの保存を無効にし、HTML 5 localStorageのみを使用してユーザーとセッションを識別します。 |
| すべてのページを追跡する | **Classic Destination Web Device-Mode（メンテナンス）のみ**<br><br>セグメントは、この設定をWeb Actionsフレームワーク送信先に移行することを推奨しています。Web Actionsフレームワーク送信先では、この設定を[マッピングによって有効にできます](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#braze-web-settings-mapping)。<br><br>これにより、すべての[ページ呼び出し](https://segment.com/docs/spec/page/)が「Loaded/Viewed a Page」イベントとしてBrazeに送信されます。 |
| 指定されたページのみを追跡する | **Classic Destination Web Device-Mode（メンテナンス）のみ**<br><br>セグメントは、この設定をWeb Actionsフレームワーク送信先に移行することを推奨しています。Web Actionsフレームワーク送信先では、この設定を[マッピングによって有効にできます](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#braze-web-settings-mapping)。<br><br>これにより、名前が関連付けられているページ呼び出しのみがBrazeに送信されます。 |
| 収益がある場合に購入を記録する | **Classic Destination Web Device-Mode（メンテナンス）のみ**<br><br>セグメントは、この設定をWeb Actionsフレームワーク送信先に移行することを推奨しています。Web Actionsフレームワーク送信先では、この設定を[マッピングによって有効にできます](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#braze-web-settings-mapping)。<br><br>このオプションを有効にすると、収益プロパティを持つすべてのTrack呼び出しが購入イベントをトリガーします。 |
| 既知のユーザーのみを追跡する | **Classic Destination Web Device-Mode（メンテナンス）のみ**<br><br>セグメントは、この設定をWeb Actionsフレームワーク送信先に移行することを推奨しています。Web Actionsフレームワーク送信先では、この設定をマッピングによって有効にできます。<br><br>有効にすると、この新しい設定により、有効な`userId`が存在するまで`window.braze.initialize`の呼び出しが遅延します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 3: Settings" }

{% endtab %}
{% tab Cloud-Mode %}

| 設定 | 説明 |
| ------- | ----------- |
| アプリ識別子 | 特定のアプリを参照するためのアプリ識別子。これは、Brazeダッシュボードの**設定の管理**で確認できます。 |
| REST APIキー | これは、Brazeダッシュボードの**設定** > **APIキー**で確認できます。 |
| カスタムREST APIエンドポイント | インスタンスに対応するBraze RESTエンドポイント（rest.iad-01.braze.comなど）。 |
| 既存ユーザーのみを更新する | **Classic Destination Cloud-Mode（メンテナンス）のみ**<br><br>セグメントは、この設定をCloud Actionsフレームワーク送信先に移行することを推奨しています。Cloud Actionsフレームワーク送信先では、この設定を[マッピングによって有効にできます](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#braze-web-settings-mapping)。<br><br>既存のユーザーのみを更新するかどうかを決定します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 3: Settings" }

{% endtab %}
{% endtabs %}

### ステップ4:メソッドをマッピングする {#methods}

Brazeは、[Page](https://segment.com/docs/connections/sources/catalog/libraries/website/javascript/#page)、[Identify](https://segment.com/docs/spec/identify/)、[Track](https://segment.com/docs/spec/track/)のセグメントメソッドをサポートしています。これらのメソッドで使用される識別子の種類は、データがサーバー間統合（クラウドモード）で送信されるのか、サイドバイサイド（デバイスモード）で送信されるのかによって異なります。Braze Web Mode Actions送信先とCloud Mode Actions送信先では、[セグメントエイリアス呼び出し](https://segment.com/docs/connections/spec/alias/)のマッピングを設定することもできます。

{% alert note %}
ユーザーエイリアスは、Braze Cloud Mode（Actions）送信先の識別子としてサポートされていますが、セグメントのエイリアス呼び出しは、Brazeユーザーエイリアスとは直接関係ないことに注意してください。
{% endalert %}

| 識別子タイプ | サポートされている送信先 |
| --------------- | --------------------- |
| `userId`（`external_id`） | すべて |
| 匿名ユーザー | デバイスモードの送信先 |
| ユーザーエイリアス | クラウドモードの送信先 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 4: Map methods #methods" }

Cloud Mode（Actions）送信先にある[Create Aliasアクション](https://segment.com/docs/connections/destinations/catalog/actions-braze-cloud/#create-alias)を使用して、エイリアスのみのユーザーを作成したり、既存の`external_id`プロファイルにエイリアスを追加したりできます。[Identify Userアクション](https://segment.com/docs/connections/destinations/catalog/actions-braze-cloud/#identify-user)は、Create Aliasアクションと並行して使用することができ、そのユーザーに`external_id`が利用可能になった後、エイリアスのみのユーザーを`external_id`とマージできます。

回避策を考案し、`braze_id`を使用してクラウドモードで匿名ユーザーのデータを送信することもできます。そのため、すべてのセグメント APIコールにユーザーの`braze_id`を手動で含める必要があります。この回避策の設定方法については、[セグメントのドキュメント](https://segment.com/docs/connections/destinations/catalog/braze/#capture-the-braze_id-of-anonymous-users)を参照してください。

Brazeに送信される送信先データは、Cloud Mode Actions内でバッチ処理できます。バッチサイズの上限は75イベントであり、これらのバッチはフラッシュされる前に30秒間蓄積されます。リクエストのバッチ処理はアクションごとに実行されます。たとえば、Identify Calls（属性）が1つのリクエストでバッチ処理され、Track Calls（カスタムイベント）が2番目のリクエストでバッチ処理されます。セグメントからBrazeに送信されるリクエストの数を減らすことができるため、Brazeはこの機能を有効にすることを推奨しています。その結果、送信先がBrazeのレート制限に達してリクエストを再試行するリスクが減少します。

Braze送信先 > **Mappings**に移動して、アクションのバッチ処理をオンにできます。そこから、マッピングの右側にある3つのドットのアイコンをクリックし、**Edit Mapping**を選択します。**Select mappings**セクションの一番下までスクロールし、**Batch Data to Braze**が**Yes**に設定されていることを確認します。


{% tabs local %}
{% tab Identify %}
#### Identify

[Identify](https://segment.com/docs/spec/identify/)呼び出しは、ユーザーをその行動に結びつけ、そのユーザーに関する属性を記録することができます。

特定のセグメント特殊特性は、Brazeの標準属性プロファイルフィールドにマッピングされます。

| セグメントの特別な特性 | Brazeの標準属性項目 |
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

`email_subscribe`や`push_subscribe`などのその他の予約済みBrazeプロファイルフィールドを送信するには、これらのフィールドにBraze命名規則を使用して、identify呼び出しでこれらを特性として渡します。

##### サブスクリプショングループにユーザーを追加する {#adding-a-user-to-a-subscription-group}

traitsパラメータの以下のフィールドを使用して、指定されたサブスクリプショングループからユーザーをサブスクライブまたはアンサブスクライブすることもできます。

`braze_subscription_groups`という予約済みのBrazeプロファイルフィールドを使用します。このフィールドは、オブジェクト配列に関連付けることができます。配列の各オブジェクトに2つの予約キーが含まれている必要があります。

1. `subscription_group_state`：特定のサブスクリプショングループに対してユーザーが`"subscribed"`または`"unsubscribed"`のいずれであるかを示します。
2. `subscription_group_id`：サブスクリプショングループの一意のIDを表します。このIDは、Brazeダッシュボードの**購読グループ管理**で確認できます。

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
`````````kotlin
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
`````````typescript
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

その他の特性はすべて[カスタム属性]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/)として記録されます。

| セグメントでの方法 | Brazeでの方法 | 例 |
|---|---|---|
| ユーザーIDで識別する | 外部IDを設定する | セグメント:  `analytics.identify("dawei");`<br>Braze: `Braze.changeUser("dawei")` |
| 予約済み特性で識別する | ユーザー属性を設定する | セグメント: `analytics.identify({email: "dawei@braze.com"});`<br> Braze: `Braze.getUser().setEmail("dawei@braze.com");`
| カスタム特性で識別する | カスタム属性を設定する | セグメント: `analytics.identify({fav_cartoon: "Naruto"});`<br>Braze: `Braze.getUser().setCustomAttribute("fav_cartoon": "Naruto")`;
| ユーザーIDと特性で識別する | セグメント:外部IDと属性を設定する | 先の方法を組み合わせます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Custom attributes" }

[Web Mode Actions](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#update-user-profile)送信先と[Cloud Mode Actions](https://segment.com/docs/connections/destinations/catalog/braze-cloud-mode-actions/#update-user-profile)送信先では、Update User Profile Actionを使用して前述のマッピングを設定できます。

{% alert important %}
ユーザー属性データを渡すときは、前回の更新以降に変更された属性の値のみを渡すようにしてください。これにより、不必要にデータポイントを記録することがなくなります。クライアントサイドのソースについては、セグメントのオープンソース[Middleware](https://github.com/segmentio/segment-braze-mobile-middleware)ツールを使用して統合を最適化し、セグメントからの重複した`identify()`呼び出しをデバウンスすることで、データポイント使用量を制限します。

{% endalert %}
{% endtab %}

{% tab Track %}
#### Track

イベントを追跡すると、提供された名前を使用して[カスタムイベント]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-events)としてそのイベントが記録されます。

Track呼び出しのプロパティオブジェクト内で送信されたメタデータは、関連イベントのカスタムイベントプロパティとしてBrazeに記録されます。すべての[カスタムイベントプロパティデータタイプ]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties/)がサポートされています。

[Web Mode Actions](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#track-event)送信先と[Cloud Mode Actions](https://segment.com/docs/connections/destinations/catalog/braze-cloud-mode-actions/#track-event)送信先では、Track Event Actionを使用して前述のマッピングを設定できます。

| セグメントでの方法 | Brazeでの方法 | 例 |
|---|---|---|
| [Track](https://segment.com/docs/spec/track/) | [カスタムイベント]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-events)として記録される | セグメント: `analytics.track("played_game");` <br>Braze: `Braze.logCustomEvent("played_game");`|
| [プロパティを使用したTrack](https://segment.com/docs/spec/track/) | [イベントプロパティ]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties/)として記録される | セグメント: `analytics.track("played_game", {name: "BotW", weapon: "boomerang"});` <br>Braze: `Braze.logCustomEvent("played_game", { "name": "BotW", "weapon": "boomerang"});` |
| [製品を使用したTrack](https://segment.com/docs/spec/track/) | [購入イベント]({{site.baseurl}}/developer_guide/analytics/logging_purchases/?tab=web)として記録される | セグメント: `analytics.track("Order Completed", {products: [product_id: "ab12", price: 19]});` <br>Braze: `Braze.logPurchase("ab12", 19);` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Track" }

##### 注文完了 {#order-completed}

セグメントの[eCommerce API](https://segment.com/docs/spec/ecommerce/v2/)で記述されているフォーマットを使用して、`Order Completed`という名前のイベントを追跡すると、[購入]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data/#revenue-data)としてリストアップされた商品が記録されます。

[Web Mode Actions](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#track-purchase)送信先と[Cloud Mode Actions](https://segment.com/docs/connections/destinations/catalog/braze-cloud-mode-actions/#track-purchase)送信先では、Track Purchase Actionでデフォルトのマッピングをカスタマイズできます。

{% endtab %}

{% tab Page %}
#### Page {#page}

[Page](https://segment.com/docs/spec/page/)呼び出しは、ユーザーがWebサイトのページを見るたびに、ページに関するオプションのプロパティとともに記録することができます。

このイベントタイプを、Web Mode Actions送信先とCloud Actions送信先でトリガーとして使用して、カスタムイベントをBrazeに記録することができます。
{% endtab %}

{% endtabs %}

### ステップ5:統合のテスト {#step-5-test-your-integration}

サイドバイサイド（デバイスモード）統合を使用する場合、[概要]({{site.baseurl}}/user_guide/analytics/dashboards/home/)指標（ライフタイムセッション、MAU、DAU、スティッキネス、デイリーセッション、MAUあたりのデイリーセッション）を使用して、Brazeがセグメントからデータを受信していることを確認できます。

[カスタムイベント]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_custom_event_data/#custom-event-data)ページまたは[収益]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data/#revenue-data)ページでデータを確認するか、または[セグメントを作成する]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#creating-a-segment)ことでデータを確認できます。ダッシュボードの**カスタムイベント**ページでは、カスタムイベントのカウントを時系列で見ることができます。サーバー間（クラウドモード）統合を使用している場合、MAUとDAU統計を含む[計算式]({{site.baseurl}}/user_guide/data_and_analytics/creating_a_formula/#creating-a-formula)を使用することはできないことに注意してください。

Brazeに購入データを送信する場合（[ステップ3](#methods)の「**Track**」タブの「注文完了」を参照）、[収益]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data/#revenue-data)ページで特定の期間の収益や購入に関するデータ、またはアプリの総収益を確認できます。

[セグメントを作成すること]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#creating-a-segment)で、カスタムイベントと属性データに基づいてユーザーをフィルタリングすることができます。

{% alert important %}
サーバー間統合（クラウドモード）を使用する場合、自動的に収集されたセッションデータに関連するフィルター（「最初に使用したアプリ」や「最後に使用したアプリ」など）は機能しません。セグメントとBrazeの統合でこれらを使用する場合は、サイドバイサイド統合（デバイスモード）を使用してください。
{% endalert %}

## ユーザーの削除と抑制 {#user-deletion-and-suppression}

ユーザーを削除または抑制する必要がある場合は、[セグメントのユーザー削除機能](https://segment.com/docs/privacy/user-deletion-and-suppression/#which-destinations-can-i-send-deletion-requests-to)**が**Brazeの[`/users/delete`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/)にマッピングされていることに注意してください。これらの削除の検証には最大30日かかる可能性があることに注意してください。

Brazeとセグメントの間で共通のユーザー識別子（`external_id`など）を選択する必要があります。セグメントで削除リクエストを開始した後は、セグメントダッシュボードの削除リクエストのタブでステータスを確認できます。

## セグメントのリプレイ機能 {#segment-replays}

セグメントは、新しいテクノロジーパートナーに対してすべての履歴データを「再生」するサービスをクライアントに提供しています。関連するすべての履歴データをインポートすることを望むBrazeの新しいお客様は、セグメントを介してインポートできます。この機能に興味がある場合はセグメントの担当者にお問い合わせください。

セグメントが[`/users/track`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)に接続し、ユーザーに代わってBrazeにユーザーデータをインポートします。

{% alert important %}
Cloud Mode Actions送信先でサポートされているすべての識別子は、セグメントのリプレイの一部としてサポートされています。
{% endalert %}

## ベストプラクティス {#best-practices}

{% details データ超過を避けるためにユースケースを確認する。 %}

セグメントでは、クライアントが送信できるデータエレメントの数は制限**されていません**。セグメントを使えば、すべてのイベントをBrazeに送ることも、どのイベントを送るかを決めることもできます。セグメントを使ってすべてのイベントを送信するのではなく、マーケティングチームや編集チームとユースケースを検討し、データ超過を避けるためにBrazeに送信するイベントを決定することをお勧めします。

{% enddetails %}

{% details モバイルデバイスモード送信先設定におけるカスタムAPIエンドポイントとカスタムREST APIエンドポイントの違いを理解する。 %}

| Braze用語 | セグメントで対応する用語 |
| ----------------- | ------------------ |
| Braze SDKエンドポイント | カスタムAPIエンドポイント |
| Braze RESTエンドポイント | カスタムREST APIエンドポイント |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Best practices" }

Braze APIエンドポイント（セグメントでは「Custom API Endpoint」と呼ばれます）は、SDKのためにBrazeにより設定されるSDKエンドポイントです（例：`sdk.iad-03.braze.com`）。Braze REST APIエンドポイント（セグメントでは「Custom REST API Endpoint」と呼ばれます）は、REST APIエンドポイントです（例：`https://rest.iad-03.braze.com`）。
{% enddetails %}

{% details カスタムAPIエンドポイントがモバイルデバイスモード送信先設定に正しく入力されていることを確認する。 %}

| Braze用語 | セグメントで対応する用語 |
| ----------------- | ------------------ |
| Braze SDKエンドポイント | カスタムAPIエンドポイント |
| Braze RESTエンドポイント | カスタムREST APIエンドポイント |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Best practices" }

Braze SDKのエンドポイントを正しく入力するには、適切な形式に従う必要があります。Braze SDKエンドポイントには`https://`を含めないでください（例：`sdk.iad-03.braze.com`）。このようにしないと、Braze統合が機能しなくなります。これは、セグメントによりエンドポイントの先頭に`https://`が自動的に付加され、その結果、Brazeは無効なエンドポイント`https://https://sdk.iad-03.braze.com`で初期化されることになるためです。

{% enddetails %}

{% details データマッピングの注意点。 %}

データが期待通りに通過しないシナリオ：

1. 階層化カスタム属性
  - [階層化カスタム属性]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support/)は、技術的にはセグメントを通してBrazeに送信できますが、**ペイロード全体**が毎回送信されます。これにより、ペイロードが送信されるたびに、ネストされたオブジェクトに渡されたキーごとに[データポイント]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support/#data-points)が発生します。<br><br> ペイロードの送信時にデータポイントのサブセットのみを使用するには、セグメントのカスタム[送信先関数](https://segment.com/docs/connections/functions/destination-functions/)機能を使用できます。セグメントプラットフォームのこの機能により、ダウンストリームの送信先へのデータの送信方法をカスタマイズできます。

  {% alert note %}
  カスタム送信先関数はセグメント内で管理されるため、Brazeでは外部で設定されているこの関数に関する情報は限られています。
  {% endalert %}

{: start="2"}
2. サーバー間で匿名データを受け渡す。
  - 顧客は、セグメントのサーバー間ライブラリを使用して、匿名データを他のシステムに渡すことができます。サーバー間（クラウドモード）統合を介して`external_id`を持たないユーザーをBrazeに送信する方法については、「メソッドをマッピングする」セクションを参照してください。

{% enddetails %}

{% details Brazeの初期化のカスタマイズ。 %}

Brazeのカスタマイズには、プッシュ、アプリ内メッセージ、Content Cards、初期化など、いくつかの方法があります。サイドバイサイド統合では、Brazeの直接統合と同様に、プッシュ、アプリ内メッセージ、Content Cardsをカスタマイズできます。

ただしBraze SDKの統合時にカスタマイズを行うこと、または初期化設定を指定することは難しく、場合によっては不可能なことがあります。これは、セグメントの初期化時にセグメントによりBraze SDKが初期化されるためです。

{% enddetails %}

{% details Brazeへの差分送信。 %}

ユーザー属性データを渡すときは、前回の更新以降に変更された属性の値のみを渡すようにしてください。これにより、不要なデータポイントのロギングを防ぐことができます。クライアントサイドのソースについては、セグメントのオープンソース[Middleware](https://github.com/segmentio/segment-braze-mobile-middleware)ツールを使用して統合を最適化し、セグメントからの重複した`identify()`呼び出しをデバウンスすることで、データポイント使用量を制限します。

{% enddetails %}

{% details 正しいBrazeデータセンターを使用する。 %}

セグメントは、Brazeデータセンターを使用して適切なBraze RESTエンドポイント（`https://rest.iad-01.braze.com`など）を取得し、サーバー間呼び出しを行います。

{% enddetails %}

{% details セグメントのEvent Testerを使用する場合はカスタムREST APIエンドポイントを削除する。 %}

セグメントのEvent Testerは、Brazeの`/users/track` REST APIエンドポイントにイベントを送信し、Braze送信先設定にカスタムREST APIエンドポイントが設定されている場合、そのエンドポイントが正しくても`401 Invalid API Key`エラーをスローします。Event Testerが正しく機能するように、セグメントのカスタムREST APIエンドポイントの値を削除してください。

{% enddetails %}

{% details 新しいソースを設定した後は更新に時間がかかることに注意する。 %}

セグメントは設定をキャッシュに長時間保持するため、新しいソースを設定する場合（例えば、クラウドモードからデバイスモードへの切り替え）、キャッシュが更新されるまでアプリに新しい動作やデータが表示されない場合があります。ソースを追加する計画を立てる際は、この遅延に注意してください。

{% enddetails %}