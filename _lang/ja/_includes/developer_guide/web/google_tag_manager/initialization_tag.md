### 前提条件 {#prerequisites}

この連携方法を使用する前に、[Google Tag Managerのアカウントとコンテナを作成](https://support.google.com/tagmanager/answer/14842164)する必要があります。

### ステップ 1: タグテンプレートギャラリーを開く {#step-1-open-the-tag-template-gallery}

[Google Tag Manager](https://tagmanager.google.com/)でワークスペースを選択し、**Templates**を選びます。**Tag Template**ペインで、**Search Gallery**を選択します。

![Google Tag Managerのサンプルワークスペースのテンプレートページ。]({% image_buster /assets/img/web-gtm/search_tag_template_gallery.png %}){: style="max-width:95%;"}

### ステップ 2: 初期化タグのテンプレートを追加する {#step-2-add-the-initialization-tag-template}

テンプレートギャラリーで `braze-inc` を検索し、**Braze Initialization Tag**を選択します。

![様々な「braze-inc」テンプレートを表示するテンプレートギャラリー。]({% image_buster /assets/img/web-gtm/template_gallery_results.png %}){: style="max-width:80%;"}

**Add to workspace** > **Add**を選択します。

![Google Tag Managerの「Braze Initialization Tag」ページ。]({% image_buster /assets/img/web-gtm/add_to_workspace.png %}){: style="max-width:70%;"}

### ステップ 3: タグを設定する {#step-3-configure-the-tag}

**Templates**セクションから、新しく追加したテンプレートを選択します。

![Google Tag Managerの「Templates」ページに、Braze Initialization Tagテンプレートが表示されている。]({% image_buster /assets/img/web-gtm/select_tag_template.png %}){: style="max-width:95%;"}

鉛筆アイコンを選択して、**Tag Configuration**のドロップダウンを開きます。

![鉛筆アイコンが表示されたTag Configurationタイル。]({% image_buster /assets/img/web-gtm/gtm-initialization-tag.png %})

必要な最低限の情報を入力します。

| フィールド         | 説明 |
| ------------- | ----------- |
| **API Key**   | [Braze APIキー]({{site.baseurl}}/api/basics#about-rest-api-keys)。Brazeダッシュボードの**Settings** > **App Settings**にあります。 |
| **API Endpoint** | RESTエンドポイントのURLです。エンドポイントは、[インスタンス]({{site.baseurl}}/api/basics#endpoints)のBraze URLによって異なります。 |
| **SDK Version**  | [変更ログ]({{site.baseurl}}/developer_guide/changelogs/?sdktab=web)に記載されている最新のWeb Braze SDKの `MAJOR.MINOR` バージョンです。たとえば、最新バージョンが `4.1.2` の場合、`4.1` と入力します。詳細については、[SDKのバージョン管理について]({{site.baseurl}}/developer_guide/sdk_integration/version_management)を参照してください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ステップ 3: タグを設定する" }

追加の初期化設定を行うには、**Braze Initialization Options**を選択し、必要なオプションを選びます。

![「Tag Configuration」の下にあるBraze Initialization Optionsの一覧。]({% image_buster /assets/img/web-gtm/braze_initialization_options.png %}){: style="max-width:65%;"}

### ステップ 4: 初期化オプションを選択する {#step-4-choose-initialization-options}

Braze Initialization Tagは以下のオプションを公開しています。これらのほとんどは[Web SDKの `InitializationOptions`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions)に直接対応しており、一部はタグが初期化時に呼び出すWeb SDKメソッドに対応しています。連携のニーズに合うオプションを選択してください。

| GTMオプション | Web SDKの設定またはメソッド | 説明 |
| --- | --- | --- |
| **Allow HTML In-App Messages** | `allowUserSuppliedJavascript` | HTMLアプリ内メッセージ、バナー、およびユーザー提供のJavaScriptクリックアクションを有効にします。カスタムHTMLを使用する[HTMLアプリ内メッセージ]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html)や[バナー]({{site.baseurl}}/developer_guide/banners/placements/?sdktab=web)に必須です。HTMLとJavaScriptのコンテンツを信頼できる場合にのみ有効にしてください。ユーザー提供のJavaScript実行を許可するためです。 |
| **App Version Number** | `appVersion`, `appVersionNumber` | セグメンテーション用のアプリバージョン（例: `1.2.3.4`）。 |
| **Automatically Open New Session** | `braze.openSession()` | このメソッドを呼び出すことで、SDKの初期化後に新しいセッションを自動的に開きます。 |
| **Automatically show new in app messages** | `braze.automaticallyShowInAppMessages()` | 初期化後にこのメソッドを呼び出すことで、サーバーから新しいアプリ内メッセージが届いた際に自動的に表示します。 |
| **Disable Automatic Push Token Maintenance** | `disablePushTokenMaintenance` | 新しいセッションでSDKがプッシュトークンをBrazeバックエンドと同期するのを停止します。 |
| **Disable Automatic Service Worker Registration** | `manageServiceWorkerExternally` | サービスワーカーを自分で登録・制御する場合に使用します。 |
| **Disable Cookies** | `noCookies` | ユーザー/セッションデータにCookieではなくlocalStorageを使用します。クロスサブドメイン認識を防ぎます。 |
| **Disable Font Awesome** | `doNotLoadFontAwesome` | SDKがCDNからFont Awesomeを読み込むのを防ぎます。サイトに独自のFont Awesomeがある場合に使用します。 |
| **Enable SDK Authentication** | `enableSdkAuthentication` | [SDK認証]({{site.baseurl}}/developer_guide/sdk_integration/authentication)を有効にします。 |
| **Enable Web SDK Logging** | `enableLogging` | デバッグ用のコンソールログを有効にします。本番環境では削除してください。 |
| **Minimum Interval Between Triggered Messages** | `minimumIntervalBetweenTriggerActionsInSeconds` | トリガーアクション間の最小秒数（デフォルト: 30）。 |
| **Open Cards in New Tab** | `openCardsInNewTab` | デフォルトのフィードUIを使用している場合、Content Cardsのリンクを新しいタブで開きます。 |
| **Service Worker Location** | `serviceWorkerLocation` | サービスワーカーファイルのカスタムパス（デフォルト: `/service-worker.js`）。 |
| **Session Timeout (seconds)** | `sessionTimeoutInSeconds` | セッションタイムアウト（秒単位）（デフォルト: 1800）。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="ステップ 4: 初期化オプションを選択する" }

{% alert note %}
Google Tag ManagerのBraze Initialization Tagを使用する際に[カスタムHTMLアプリ内メッセージ]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html)を有効にするには、**Braze Initialization Options**で**Allow HTML In-App Messages**を選択します。このチェックボックスは `braze.initialize()` の `allowUserSuppliedJavascript` 初期化オプションに対応し、`true` に設定します。Google Tag ManagerのBraze Initialization Tagは、オプション名ではなくこのラベルを使用します。
{% endalert %}

GTMテンプレートで公開されていないオプション（`contentSecurityNonce`、`localization`、`devicePropertyAllowlist` など）については、代わりに[ランタイム初期化]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web)を使用してください。

### ステップ 5: *すべてのページ*でトリガーされるように設定する {#step-5-set-to-trigger-on-all-pages}

初期化タグはサイトのすべてのページで実行する必要があります。これにより、Braze SDKメソッドを使用し、Webプッシュの分析を記録できるようになります。

{% alert important %}
**タグの順序付け:** Braze Initialization Tagは、Braze SDKメソッドを呼び出す他のすべてのタグ（`braze.getUser()` や `braze.logCustomEvent()` など）よりも先に発火する必要があります。SDKが初期化される前にカスタムイベント、ユーザー属性、またはその他のBrazeメソッド呼び出しが発火すると、`Uncaught TypeError: Cannot read properties of undefined (reading 'getUser')` のようなエラーが発生する可能性があります。適切な順序を確保するには、Braze Initialization Tagをセットアップタグとして設定するか、GTMのタグ順序付け機能を使用して最初に発火するようにしてください。詳細については、[Brazeアクションタグのタグ順序付け]({{site.baseurl}}/developer_guide/sdk_integration/google_tag_manager/?sdktab=web#web_tag-sequencing-for-braze-action-tags)を参照してください。
{% endalert %}

### ステップ 6: 連携を確認する {#step-6-verify-your-integration}

以下のいずれかの方法で連携を確認できます。

- **オプション 1:** Google Tag Managerの[デバッグツール](https://support.google.com/tagmanager/answer/6107056?hl=en)を使用して、設定したページやイベントでBraze Initialization Tagが正しくトリガーされているか確認できます。
- **オプション 2:** Webページからのネットワークリクエストを確認し、Brazeへのリクエストが行われているか確認します。さらに、グローバルの `window.braze` ライブラリが定義されていることを確認してください。