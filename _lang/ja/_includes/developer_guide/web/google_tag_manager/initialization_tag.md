### 前提条件

この連携方法を使用する前に、[Google Tag Manager のアカウントとコンテナを作成](https://support.google.com/tagmanager/answer/14842164)する必要があります。

### ステップ 1: タグテンプレートギャラリーを開く

[Google Tag Manager](https://tagmanager.google.com/) でワークスペースを選択し、**テンプレート**を選びます。**タグテンプレート**ペインで、**検索ギャラリー**を選択します。

![Google Tag Manager のサンプルワークスペースのテンプレートページ。]({% image_buster /assets/img/web-gtm/search_tag_template_gallery.png %}){: style="max-width:95%;"}

### ステップ 2: 初期化タグのテンプレートを追加する

テンプレートギャラリーで `braze-inc` を検索し、**Braze Initialization Tag** を選択します。

![様々な「braze-inc」テンプレートを表示するテンプレートギャラリー。]({% image_buster /assets/img/web-gtm/template_gallery_results.png %}){: style="max-width:80%;"}

**ワークスペースに追加** > **追加**を選択します。

![Google Tag Manager の「Braze Initialization Tag」ページ。]({% image_buster /assets/img/web-gtm/add_to_workspace.png %}){: style="max-width:70%;"}

### ステップ 3: タグを設定する

**テンプレート**セクションから、新しく追加したテンプレートを選択します。

![Google Tag Manager の「テンプレート」ページに、Braze Initialization Tag テンプレートが表示されている。]({% image_buster /assets/img/web-gtm/select_tag_template.png %}){: style="max-width:95%;"}

鉛筆アイコンを選択して、**タグ設定**のドロップダウンを開きます。

![鉛筆アイコンが表示されたタグ設定タイル。]({% image_buster /assets/img/web-gtm/gtm-initialization-tag.png %})

必要な最低限の情報を入力します。

| フィールド         | 説明 |
| ------------- | ----------- |
| **API キー**   | [Braze API キー]({{site.baseurl}}/api/basics/#about-rest-api-keys)。Braze ダッシュボードの**設定** > **アプリ設定**にあります。 |
| **API エンドポイント** | REST エンドポイントの URL。エンドポイントは、[インスタンス]({{site.baseurl}}/api/basics/#endpoints)の Braze URL によって異なります。 |
| **SDK バージョン**  | [変更ログ]({{site.baseurl}}/developer_guide/changelogs/?sdktab=web)に記載されている最新の Web Braze SDK の `MAJOR.MINOR` バージョンです。たとえば、最新バージョンが `4.1.2` の場合、`4.1` と入力します。詳細については、[SDK のバージョン管理について]({{site.baseurl}}/developer_guide/sdk_integration/version_management/)を参照してください。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

追加の初期化設定を行うには、**Braze Initialization Options** を選択し、必要なオプションを選びます。

![「タグ設定」の下にある Braze Initialization Options の一覧。]({% image_buster /assets/img/web-gtm/braze_initialization_options.png %}){: style="max-width:65%;"}

### ステップ 4: 初期化オプションを選択する

Braze Initialization Tag は以下のオプションを公開しています。これらのほとんどは [Web SDK の `InitializationOptions`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions) に直接対応しており、一部はタグが初期化時に呼び出す Web SDK メソッドに対応しています。連携のニーズに合うオプションを選択してください。

| GTM オプション | Web SDK の設定またはメソッド | 説明 |
| --- | --- | --- |
| **Allow HTML In-App Messages** | `allowUserSuppliedJavascript` | HTML アプリ内メッセージ、バナー、およびユーザー提供の JavaScript クリックアクションを有効にします。カスタム HTML を使用する [HTML アプリ内メッセージ]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html/)や[バナー]({{site.baseurl}}/developer_guide/banners/placements/?sdktab=web)に必須です。HTML と JavaScript のコンテンツを信頼できる場合にのみ有効にしてください。ユーザー提供の JavaScript の実行を許可するためです。 |
| **App Version Number** | `appVersion`, `appVersionNumber` | セグメンテーション用のアプリバージョン（例: `1.2.3.4`）。 |
| **Automatically Open New Session** | `braze.openSession()` | このメソッドを呼び出すことで、SDK の初期化後に新しいセッションを自動的に開きます。 |
| **Automatically show new in app messages** | `braze.automaticallyShowInAppMessages()` | 初期化後にこのメソッドを呼び出すことで、サーバーから新しいアプリ内メッセージが届いた際に自動的に表示します。 |
| **Disable Automatic Push Token Maintenance** | `disablePushTokenMaintenance` | 新しいセッションで SDK がプッシュトークンを Braze バックエンドと同期するのを停止します。 |
| **Disable Automatic Service Worker Registration** | `manageServiceWorkerExternally` | サービスワーカーを自分で登録・制御する場合に使用します。 |
| **Disable Cookies** | `noCookies` | ユーザー/セッションデータに Cookie ではなく localStorage を使用します。クロスサブドメイン認識を防ぎます。 |
| **Disable Font Awesome** | `doNotLoadFontAwesome` | SDK が CDN から Font Awesome を読み込むのを防ぎます。サイトに独自の Font Awesome がある場合に使用します。 |
| **Enable SDK Authentication** | `enableSdkAuthentication` | [SDK認証]({{site.baseurl}}/developer_guide/sdk_integration/authentication/)を有効にします。 |
| **Enable Web SDK Logging** | `enableLogging` | デバッグ用のコンソールログを有効にします。本番環境では削除してください。 |
| **Minimum Interval Between Triggered Messages** | `minimumIntervalBetweenTriggerActionsInSeconds` | トリガーアクション間の最小秒数（デフォルト: 30）。 |
| **Open Cards in New Tab** | `openCardsInNewTab` | デフォルトのフィード UI を使用している場合、コンテンツカードのリンクを新しいタブで開きます。 |
| **Service Worker Location** | `serviceWorkerLocation` | サービスワーカーファイルのカスタムパス（デフォルト: `/service-worker.js`）。 |
| **Session Timeout (seconds)** | `sessionTimeoutInSeconds` | セッションタイムアウト（秒単位）（デフォルト: 1800）。 |

{% alert note %}
Google Tag Manager の Braze Initialization Tag を使用する際に[カスタム HTML アプリ内メッセージ]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html/)を有効にするには、**Braze Initialization Options** で **Allow HTML In-App Messages** を選択します。このチェックボックスは `braze.initialize()` の `allowUserSuppliedJavascript` 初期化オプションに対応し、`true` に設定します。Google Tag Manager の Braze Initialization Tag は、オプション名ではなくこのラベルを使用します。
{% endalert %}

GTM テンプレートで公開されていないオプション（`contentSecurityNonce`、`localization`、`devicePropertyAllowlist` など）については、代わりに[ランタイム初期化]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web)を使用してください。

### ステップ 5: *すべてのページ*でトリガーされるように設定する

初期化タグはサイトのすべてのページで実行する必要があります。これにより、Braze SDK メソッドを使用し、Web プッシュの分析を記録できるようになります。

### ステップ 6: 連携を確認する

以下のいずれかの方法で連携を確認できます。

- **オプション 1:** Google Tag Manager の[デバッグツール](https://support.google.com/tagmanager/answer/6107056?hl=en)を使用して、設定したページやイベントで Braze Initialization Tag が正しくトリガーされているか確認できます。
- **オプション 2:** Web ページから Braze へのネットワークリクエストが行われているか確認します。さらに、グローバルの `window.braze` ライブラリーが定義されていることを確認してください。