---
nav_title: Shopify概要
article_title: Shopify概要
description: "このリファレンス記事では、BrazeとShopifyのパートナーシップについて説明します。Shopifyはグローバルなコマース企業であり、ShopifyストアをBrazeとシームレスに接続して、選択したShopify webhookをBrazeに渡すことができます。Brazeのクロスチャネル戦略とキャンバスを活用して、顧客が購入を完了するように促し、購入履歴に基づいてユーザーをリターゲティングできます。"
page_type: partner
search_tag: Partner
alias: /shopify_overview/
page_order: 0
---

# Shopify概要 {#shopify-overview}

> [Shopify](https://www.shopify.com/) は、規模を問わずビジネスの開始、成長、マーケティング、管理のための信頼できるツールを提供する世界的なコマースのリーディングカンパニーです。Shopifyは、信頼性の高いプラットフォームとサービスを提供し、世界中の消費者により良いショッピング体験を提供することで、すべての人にとって商取引をより良くします。

ShopifyとのBraze統合は、カスタマーエンゲージメントを高め、パーソナライズされたマーケティング活動を推進しようとするeコマース事業者にとって、強力なソリューションを提供します。この統合は、Shopifyの堅牢なeコマース機能を高度なカスタマーエンゲージメントプラットフォームにシームレスに接続し、リアルタイムの買い物行動やトランザクションデータに基づいて、ターゲットを絞った、関連性のある、タイムリーなメッセージをユーザーに配信することを可能にします。

## 要件 {#requirements}

| 要件 | 説明 |
| --- | --- |
| Shopifyストア | アクティブなShopifyストアがあること。 |
| Shopifyストアオーナーまたはスタッフメンバーの権限 | {::nomarkdown}<ul><li>すべての一般設定とオンラインストア設定にアクセスできること。</li><li> 追加の管理者権限:<ul><li>Orders: View</li><li>Customer: ReadWrite</li><li>View Customer Events (Web Pixels)</li><li>Manage Settings</li><li>View Apps Developed by Staff/Collaborators</li><li>Manage/Install Apps and Channels</li><li>Manage/Add Custom Pixels</li></ul></li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requirements" }

## 統合方法 {#how-to-integrate}

Brazeは、Shopify加盟店向けに、eコマースビジネスの多様なニーズを満たすように設計された2つの統合オプションである**標準統合**と**カスタム統合**を提供しています。

{% multi_lang_include partners/shopify.md section='Integration Tabs' %}

## 統合の仕組み {#how-the-integration-works}

設定で[履歴バックフィル]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features/#historical-backfill)をすでに設定してオンにしている場合は、最初のデータ同期がすぐに開始されます。

{% multi_lang_include partners/shopify.md section='Custom external ID historical backfill' %}

最初のデータ同期後、BrazeはShopifyとBraze SDKから直接、新しいデータと更新を継続的に追跡します。

{% alert note %}
既存のBrazeユーザーで、アクティブなキャンペーンやキャンバスをご利用の場合は、[Shopifyの履歴バックフィル]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features/#historical-backfill)で重要な情報を確認してください。具体的にどのような顧客データがバックフィルされているかについては、[Shopifyの機能]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features/)を参照してください。
{% endalert %}

### ユーザーとデータの同期 {#user-and-data-syncing}

統合が開始された後、BrazeはShopify統合を通じて、2つの主要なソースからユーザーデータを収集します。
- **Shopify Web Pixel APIとアプリ埋め込み:** これにより、Braze Web SDKとJavascript SDKの機能が強化され、オンサイトトラッキング、ID管理、eコマース行動データ、アプリ内メッセージなどのメッセージングチャネルがサポートされます。
- **Shopify webhook:** eコマースの行動データ、商品同期、サブスクライバー収集

統合のオンボーディングの際に、Braze SDKが初期化され、Shopifyサイトを読み込むタイミングを選択する必要があります。
- サイト訪問時（セッション開始時など）
    - **実行内容:** ゲスト買い物客などの匿名ユーザーを追跡し、より詳細なパーソナライゼーションのためのデータにアクセスします。
- アカウント登録時（アカウントログインなど）
    - **実行内容:** より保守的なプライバシー指向のアプローチで匿名ユーザーの追跡を防止します。そのため、ユーザーのアクティビティはアカウントにサインインした*後に*追跡されます。

{% alert note %}
- Webサイトへの訪問（セッション）は、月間アクティブユーザー数（MAU）の割り当てにカウントされます。
- Braze Web SDKとJavaScript SDKのバージョンは自動的にv5.4.0に設定されます。
{% endalert %}

Brazeは、Shopify統合を使用して、ユーザーがゲストとしてショッピングを体験してから識別済みのユーザーになるまでを追跡する複数の識別子をサポートしています。

| Braze識別子 | 説明 |
| --- | --- |
| Braze `device_id` | Braze SDKを通じて匿名ユーザーのアクティビティを追跡するために、ブラウザーに保存されるランダムに生成されるIDです。 |
| カートトークンユーザーエイリアス | Brazeがカート更新イベントを追跡するために作成するエイリアスです。このトークンは、Shopifyカートトークンを使用して作成されます。 |
| チェックアウトトークンユーザーエイリアス | ユーザーがチェックアウトプロセスを開始する際にBrazeが作成するエイリアスです。このトークンは、Shopifyのチェックアウトトークンを使用して作成されます。<br><br> 顧客がShop Payを高速チェックアウトオプションとして使用した場合、Shopifyは特定の標準チェックアウトイベントをバイパスし、Brazeがチェックアウトトークンエイリアスを追加するために必要なデータを受信できなくなる場合があります。 |
| Shopify顧客IDエイリアス | Shopify顧客IDは、アカウントログイン時または注文時にexternal IDが割り当てられる際にエイリアスとして割り当てられます。 |
| Braze `external_id` | デバイスやプラットフォームを横断して顧客を追跡するための一意の識別子です。ユーザーがデバイスを切り替えたり、アプリを再インストールしたりしても、複数のプロファイルが作成されることを防ぎ、一貫したユーザーエクスペリエンスを維持し、分析を向上させます。<br><br>Shopify統合では、以下の`external_id`タイプがサポートされます。<br><br>{::nomarkdown}<ul><li>Shopify顧客ID（デフォルト）</li><li>カスタムexternal ID</li><li>ハッシュされたメール（SHA-256）</li><li>ハッシュされたメール（SHA-1）</li><li>ハッシュされたメール（MD5）</li><li>メール</li></ul>{:/}Brazeは以下のタイミングでSDK内のchangeUserメソッドを呼び出すことで、ユーザーに`external_id`を割り当てます。<br><br>{::nomarkdown}<ul><li>ユーザーがログインするか、アカウントを作成する</li><li>注文が行われる</li></ul>{:/}<br> 匿名プロファイルに`external_id`を割り当てた場合の詳細については、[ユーザープロファイルのライフサイクル]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/#what-happens-when-you-identify-anonymous-users)を参照してください。<br><br>Brazeはまた、`external_id`を活用して、Shopify webhookからの下流のeコマース行動データを紐付けます。|
{: .reset-td-br-1 .reset-td-br-2 aria-label="User and data syncing" }

この統合では、Braze SDKとShopifyサービスが連携して、Shopifyデータをほぼリアルタイムで適切に追跡し、適切なユーザーに紐付ける必要があります。統合によって追跡されるデータの詳細については、[Shopifyデータ]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features/)を参照してください。

{% alert note %}
- 統合をテストしている場合は、シークレットモードを使用するか、Cookieをクリアしてbraze `device_id`をリセットし、匿名ユーザーの行動を模倣することをお勧めします。
- Shopifyの顧客IDは、Shopifyのニュースレターフッターにメールが入力されたときや、注文前のチェックアウトプロセス中に生成されますが、その顧客IDにはShopify Web Pixelsからアクセスできません。このため、Brazeはこの2つの状況では`changeUser`メソッドを使用できません。
{% endalert %}

### ShopifyのメールおよびSMSマーケティングオプトインの同期 {#syncing-shopify-email-and-sms-marketing-opt-ins}

設定でサブスクライバー収集を有効にした場合は、Brazeに接続する各ストアにサブスクリプショングループを割り当てる必要があります。これにより、顧客はストアのサブスクリプショングループで「購読中」または「配信停止」のいずれかに分類されます。

メールとSMSマーケティングのShopifyマーケティングオプトインステータスは、以下の方法で更新できます。
- **手動更新:** ユーザーのメールやSMSマーケティングのオプトインステータスは、Shopify管理画面で手動で変更できます。
- **Shopifyニュースレターフッター:** ユーザーがShopifyデフォルトのニュースレターフッターにメールを入力すると、オプトインステータスが更新されます。
- **チェックアウトプロセス:** ユーザーがチェックアウト中にオプトインステータスを更新した場合。

{% alert note %}
Shopifyからのメールマーケティングオプトインステータスによって、Brazeのユーザーの[グローバルメールサブスクリプションステータス]({{site.baseurl}}/user_guide/channels/email/subscriptions/)が変更されることはありません。ユーザープロファイルが作成されたときのデフォルトのサブスクリプションステータスは「購読中」です。キャンペーンまたはキャンバスのエントリ基準の一部として、サブスクリプショングループを必ず使用してください。
{% endalert %}

この表は、Shopifyマーケティングのオプトインステータスと、Brazeサブスクリプショングループ内のステータスとの対応関係を示しています。

| Shopifyマーケティングのオプトインステータス | Brazeサブスクリプショングループのステータス |
| --- | --- |
| メール購読済み | 購読中 |
| メール配信停止 | 配信停止済み |
| メール確認待ち | 配信停止済み |
| メールが無効 | 配信停止済み |
| SMS購読済み | 購読中 |
| SMS配信停止済み | 配信停止済み |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Syncing Shopify email and SMS marketing opt-ins" }

### 登録フォーム {#sign-up-forms}

#### Shopifyニュースレターフッター {#shopify-newsletter-footer}

Shopifyのニュースレターフッターにメールアドレスを入力したユーザーには、次のいずれかのワークフローが適用されます。

##### アカウントにログインしていないユーザー {#users-who-havent-logged-into-their-account}

1. 顧客が作成または更新されるたびに、BrazeはShopifyのインバウンドwebhookを受信します。
2. Brazeは、そのユーザーに関連付けられたメールアドレスとShopify顧客IDエイリアスを含むユーザープロファイルを作成します。
3. Braze SDKは、メールアドレスで匿名プロファイルを更新します。

{% alert note %}
その結果、ユーザーがアカウントの作成、アカウントへのログイン、または注文を行うことで自身を識別するまで、プロファイルの重複が生じる場合があります。Brazeは、重複プロファイルの照合を自動化するための一括マージツールを提供しています。詳細は[重複ユーザー]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users/)を参照してください。
{% endalert %}

##### アカウントにログイン済みのユーザー {#users-who-have-already-logged-into-their-account}

Brazeは、そのユーザーに関連付けられたメールアドレスとShopify顧客IDエイリアスを含むユーザープロファイルを作成します。Shopifyがすでにこの情報を提供していると想定されるため、Brazeはログイン済みユーザーのメールアドレスを更新しません。

#### Braze登録フォーム {#braze-sign-up-forms}

Brazeは2種類の登録フォームテンプレートを提供しています。
- **[メール登録フォーム]({{site.baseurl}}/user_guide/messaging/templates/in_app_message_templates/email_capture/):** ドラッグ＆ドロップエディターを使用して作成します。
- **[従来のエディターのメールキャプチャフォーム]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/email_capture_form/):** メールアドレスを取得するための、よりシンプルなフォームです。

これらの登録フォームテンプレートを使用すると、Brazeは自動的にユーザープロファイルのグローバルメールサブスクリプションステータスを更新します。グローバルメールサブスクリプションステータスの処理方法についての詳細（メールの検証に関する情報を含む）については、各フォームテンプレートタイプのドキュメントを参照してください。

{% alert note %}
- キャンペーンまたはキャンバスに、グローバルメールサブスクリプションステータスと、Shopifyストアに接続されているサブスクリプショングループの両方を含むエントリ基準を必ず含めてください。これにより、適切なオーディエンスをターゲットにしていることを確認できます。
- Brazeは、ブラウザー内メッセージを通じて、メールアドレスや電話番号などの訪問者情報を収集します。この情報はShopify Visitor APIに送信されますが、Shopifyでは顧客プロファイルは作成されません。詳細については、[Visitor API](https://shopify.dev/docs/api/web-pixels-api/emitting-data#visitor-api)を参照してください。
{% endalert %}

#### サードパーティの登録フォーム {#third-party-sign-up-forms}

サードパーティのプラットフォームやShopifyプラグインを登録フォームに使用している場合は、フォーム送信からメールアドレスとグローバルメールサブスクリプションステータスを取得するために、開発者と協力してBraze SDKコードを統合する必要があります。詳細については、[Shopify標準統合セットアップ]({{site.baseurl}}/shopify_standard_integration/)と[Shopifyカスタム統合セットアップ]({{site.baseurl}}/shopify_custom_integration/)を確認してください。

### 商品の同期 {#product-syncing}

Brazeは、Shopifyストアの商品をBrazeカタログに同期する機能をサポートしています。詳細は、[Shopify商品同期]({{site.baseurl}}/shopify_catalogs/)を参照してください。

## データ主体リクエスト {#data-subject-requests}

BrazeプラットフォームのShopify統合の一環として、Brazeは自動的に[Shopifyのコンプライアンスwebhook](https://shopify.dev/docs/apps/build/privacy-law-compliance/)を受信します。ただし、顧客はそのエンドユーザーデータのデータ管理者であるため、Brazeのエンドユーザーデータ（Shopify統合を通じて受信したエンドユーザーデータを含む）に関して受領したデータ主体リクエストへの対応に必要なアクションを実行する必要があります。詳細は、[データ保護技術支援]({{site.baseurl}}/dp-technical-assistance/)ドキュメントを参照してください。