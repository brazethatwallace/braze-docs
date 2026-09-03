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

> [Shopify](https://www.shopify.com/)は、規模を問わずビジネスの開始、成長、マーケティング、管理のための信頼できるツールを提供する世界的なコマースのリーディングカンパニーです。Shopifyは、信頼性の高いプラットフォームとサービスを提供し、世界中の消費者により良いショッピング体験を提供することで、すべての人にとって商取引をより良くします。

ShopifyとのBraze統合は、カスタマーエンゲージメントを高め、パーソナライズされたマーケティング活動を推進しようとするeコマース事業者にとって、強力なソリューションを提供します。この統合は、Shopifyの堅牢なeコマース機能を高度なカスタマーエンゲージメントプラットフォームにシームレスに接続し、リアルタイムの買い物行動やトランザクションデータに基づいて、ターゲットを絞った、関連性のある、タイムリーなメッセージをユーザーに配信することを可能にします。

## 要件 {#requirements}

| 要件 | 説明 |
| --- | --- |
| Shopify ストア | アクティブな Shopify ストアがあること。 |
| Shopify ストアオーナーまたはスタッフメンバーの権限 | {::nomarkdown}<ul><li>すべての一般設定およびオンラインストア設定へのアクセス。</li><li> 追加の管理者権限:<ul><li>注文:表示</li><li>顧客:読み取り/書き込み</li><li>顧客イベントの表示 (Web Pixels)</li><li>設定の管理</li><li>スタッフ/コラボレーターが開発したアプリの表示</li><li>アプリとチャネルの管理/インストール</li><li>カスタムピクセルの管理/追加</li></ul></li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="要件" }

## 統合方法 {#how-to-integrate}

Brazeは、eコマースビジネスの多様なニーズに対応するために設計された、Shopifyマーチャント向けの2つの統合オプションを提供しています：**標準統合**と**カスタム統合**です。

{% multi_lang_include partners/shopify.md section='Integration Tabs' %}

## 連携の仕組み {#how-the-integration-works}

設定で[履歴バックフィル]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features#historical-backfill)をすでにセットアップして有効にしている場合、初期データ同期がすぐに開始されます。

{% multi_lang_include partners/shopify.md section='Custom external ID historical backfill' %}

初期データ同期の後、Brazeは Shopify と Braze SDKから直接、新しいデータと更新を継続的にトラッキングします。

{% alert note %}
アクティブなキャンペーンやキャンバスを運用中の既存のBraze顧客の場合は、重要な情報について[Shopify 履歴バックフィル]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features#historical-backfill)を確認してください。バックフィルされる具体的な顧客データについては、[Shopify の機能]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features)を参照してください。
{% endalert %}

### ユーザーとデータの同期 {#user-and-data-syncing}

連携が稼働すると、BrazeはShopify連携を通じて2つの主要なソースからユーザーデータを収集します。
- **Shopify Web Pixel API とアプリ埋め込み:** Braze Web SDKとJavascript SDKを活用し、オンサイトトラッキング、ID管理、eコマース行動データ、およびアプリ内メッセージなどのメッセージングチャネルをサポートします。
- **Shopify Webhook:** eコマース行動データ、商品同期、購読者収集

連携のオンボーディング中に、Braze SDKがShopifyサイトを初期化して読み込むタイミングを選択する必要があります。
- サイト訪問時（セッション開始など）
    - **動作:** ゲストショッパーなどの匿名ユーザーをトラッキングし、より深いパーソナライゼーションのためのデータにアクセスします
- アカウント登録時（アカウントログインなど）
    - **動作:** 匿名ユーザーのトラッキングを防止し、よりプライバシー重視の保守的なアプローチを取ります。ユーザーのアクティビティは、ユーザーがアカウントにサインインした*後*にトラッキングされます

{% alert note %}
- Webサイトの訪問（セッション）は、月間アクティブユーザー（MAU）の割り当てにカウントされます。
- Braze Web SDKとJavaScript SDKのバージョンは自動的にv6.8.0に設定されます。連携設定からいつでもSDKバージョンをアップグレードできます。
{% endalert %}

Brazeは、Shopify連携を使用して、ゲストショッピング体験から識別済みユーザーになるまでのユーザーをトラッキングする複数の識別子をサポートしています。

| Braze識別子 | 説明 |
| --- | --- |
| Braze `device_id` | ブラウザに保存されるランダム生成IDで、Braze SDKを通じて匿名ユーザーのアクティビティをトラッキングします。 |
| カートトークンユーザーエイリアス | Brazeがカート更新イベントをトラッキングするために作成するエイリアスです。このトークンはShopifyカートトークンを使用して作成されます。 |
| チェックアウトトークンユーザーエイリアス | ユーザーがチェックアウトプロセスを開始したときにBrazeが作成するエイリアスです。このトークンはShopifyチェックアウトトークンを使用して作成されます。<br><br>顧客がShop Payを高速チェックアウトオプションとして使用した場合、Shopifyは特定の標準チェックアウトイベントをバイパスし、Brazeがチェックアウトトークンエイリアスを追加するために必要なデータを受信できなくなる場合があります。 |
| Shopify顧客IDエイリアス | Shopify顧客IDは、アカウントログイン時または注文時にexternal IDが割り当てられる際にエイリアスとして割り当てられます。 |
| Braze `external_id` | デバイスやプラットフォーム間で顧客をトラッキングするための一意の識別子です。ユーザーがデバイスを切り替えたりアプリを再インストールしたりした際に複数のプロファイルが作成されるのを防ぎ、一貫したユーザー体験を維持し、分析を改善します。<br><br>Shopify連携は以下の`external_id`タイプをサポートしています。<br><br>{::nomarkdown}<ul><li>Shopify顧客ID（デフォルト）</li><li>カスタムexternal ID</li><li>ハッシュ化メール（SHA-256）</li><li>ハッシュ化メール（SHA-1）</li><li>ハッシュ化メール（MD5）</li><li>メール</li></ul>{:/}Brazeは、以下の場合にSDK内のchangeUserメソッドを呼び出すことで、ユーザーに`external_id`を割り当てます。<br><br>{::nomarkdown}<ul><li>ユーザーがログインまたはアカウントを作成した場合</li><li>注文が行われた場合</li></ul>{:/}<br>匿名プロファイルに`external_id`を割り当てた場合の動作の詳細については、[ユーザープロファイルのライフサイクル]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle#what-happens-when-you-identify-anonymous-users)を参照してください。<br><br>Brazeは、Shopify Webhookからの下流のeコマース行動データを帰属させるためにも`external_id`を活用します。|
{: .reset-td-br-1 .reset-td-br-2 aria-label="ユーザーとデータの同期" }

この連携では、Braze SDKとShopifyサービスが連携して、Shopifyデータをほぼリアルタイムで適切なユーザーにトラッキングおよび帰属させる必要があります。連携を通じてトラッキングされるデータの詳細については、[Shopifyデータ]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features)を参照してください。

{% alert note %}
- 連携をテストする場合は、シークレットモードを使用するか、CookieをクリアしてBraze `device_id`をリセットし、匿名ユーザーの動作を模倣することをお勧めします。
- Shopifyニュースレターフッターでメールが入力された場合や、注文が行われる前のチェックアウトプロセス中にShopify顧客IDが生成されますが、その顧客IDはShopify Web Pixelsを通じてアクセスできません。このため、Brazeはこれら2つの状況で`changeUser`メソッドを使用できません。
{% endalert %}

### Shopifyメールおよび SMS マーケティングオプトインの同期 {#syncing-shopify-email-and-sms-marketing-opt-ins}

設定で購読者収集を有効にした場合、Brazeに接続する各ストアに購読グループを割り当てる必要があります。これにより、顧客はストアの購読グループに対して「購読済み」または「購読解除」のいずれかに分類されます。

メールおよび SMS マーケティングのShopifyマーケティングオプトインステータスは、以下の方法で更新できます。
- **手動更新:** Shopify管理画面でユーザーのメールまたは SMS マーケティングオプトインステータスを手動で変更できます。
- **Shopifyニュースレターフッター:** ユーザーがShopifyのデフォルトニュースレターフッターにメールを入力すると、オプトインステータスが更新されます。
- **チェックアウト:** ユーザーがマーケティングチェックボックスを選択し、1ページチェックアウトで**Pay now**を選択するか、3ページチェックアウトで**Continue to shipping**を選択してチェックアウトを進めると、ユーザーの同意がチェックアウト時にキャプチャされます。

{% alert note %}
Shopifyからのメールマーケティングオプトインステータスは、Brazeのユーザーの[グローバルメール購読状態]({{site.baseurl}}/user_guide/channels/email/subscriptions)を変更しません。ユーザープロファイルが作成された際のデフォルトの購読状態は「subscribed」です。キャンペーンやキャンバスのエントリ条件の一部として購読グループを使用することを忘れないでください。
{% endalert %}

この表は、Shopifyマーケティングオプトイン状態がBraze購読グループ内のステータスとどのように対応するかを示しています。

| Shopifyマーケティングオプトイン状態 | Braze購読グループの状態 |
| --- | --- |
| メール購読済み | Subscribed |
| メール購読解除 | Unsubscribed |
| メール確認待ち | Unsubscribed |
| メール無効 | Unsubscribed |
| SMS 購読済み | Subscribed |
| SMS 購読解除 | Unsubscribed |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Shopifyメールおよび SMS マーケティングオプトインの同期" }

### サインアップフォーム {#sign-up-forms}

#### Shopifyニュースレターフッター {#shopify-newsletter-footer}

Shopifyニュースレターフッターにメールアドレスを入力したユーザーは、以下のいずれかのワークフローを経験します。

##### アカウントにログインしていないユーザー {#users-who-havent-logged-into-their-account}

1. Brazeは、顧客が作成または更新されるたびに、受信Shopify Webhookを受け取ります。
2. Brazeは、そのユーザーに関連付けられたメールアドレスとShopify顧客IDエイリアスを含むユーザープロファイルを作成します。
3. Braze SDKは、匿名プロファイルをメールアドレスで更新します。

{% alert note %}
これにより、ユーザーがアカウントを作成するか、アカウントにログインするか、注文を行うことで自身を識別するまで、重複プロファイルが発生する可能性があります。Brazeは、重複プロファイルの照合を自動化するための一括マージツールを提供しています。詳細については、[重複ユーザー]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users)を参照してください。
{% endalert %}

##### すでにアカウントにログインしているユーザー {#users-who-have-already-logged-into-their-account}

Brazeは、そのユーザーに関連付けられたメールアドレスとShopify顧客IDエイリアスを含むユーザープロファイルを作成します。Shopifyがすでにこの情報を提供していると想定されるため、Brazeはログイン済みユーザーのメールアドレスを更新しません。

#### Brazeサインアップフォーム {#braze-sign-up-forms}

Brazeは2種類のサインアップフォームテンプレートを提供しています。
- **[メールサインアップフォーム]({{site.baseurl}}/user_guide/messaging/templates/in_app_message_templates/email_capture):** ドラッグ＆ドロップエディターを使用して作成します。
- **[従来のエディターのメールキャプチャフォーム]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/email_capture_form):** メールアドレスをキャプチャするためのよりシンプルなフォームです。

これらのサインアップフォームテンプレートを使用すると、Brazeはユーザープロファイルのグローバルメール購読ステータスを自動的に更新します。グローバルメール購読状態の処理方法（メールバリデーションに関する情報を含む）の詳細については、各フォームテンプレートタイプのドキュメントを参照してください。

{% alert note %}
- キャンペーンやキャンバスに、グローバルメール購読ステータスとShopifyストアに接続された購読グループの両方を含むエントリ条件を必ず含めてください。これにより、適切なオーディエンスをターゲティングできます。
- Brazeは、ブラウザ内メッセージを通じてメールアドレスや電話番号などの訪問者情報を収集します。この情報はShopify Visitor APIに送信されますが、Shopifyに顧客プロファイルは作成されません。詳細については、[Visitor API](https://shopify.dev/docs/api/web-pixels-api/emitting-data#visitor-api)を参照してください。
{% endalert %}

#### サードパーティのサインアップフォーム {#third-party-sign-up-forms}

サインアップフォームにサードパーティのプラットフォームやShopifyプラグインを使用している場合は、フォーム送信からメールアドレスとグローバルメール購読ステータスをキャプチャするために、開発者と協力してBraze SDKコードを統合する必要があります。詳細については、[Shopify標準連携セットアップ]({{site.baseurl}}/shopify_standard_integration)および[Shopifyカスタム連携セットアップ]({{site.baseurl}}/shopify_custom_integration)を確認してください。

### 商品同期 {#product-syncing}

Brazeは、Shopifyストアの商品をBrazeカタログに同期する機能をサポートしています。詳細については、[Shopify商品同期]({{site.baseurl}}/shopify_catalogs)を参照してください。

## データ主体のリクエスト {#data-subject-requests}

Braze プラットフォームの Shopify 統合の一環として、Braze は [Shopify のコンプライアンス Webhook](https://shopify.dev/docs/apps/build/privacy-law-compliance/) を自動的に受信します。ただし、顧客はエンドユーザーのデータのデータ管理者であるため、Braze 内のエンドユーザーデータ（Shopify 統合を通じて受信したエンドユーザーデータを含む）に関して受け取ったデータ主体のリクエストに対応するために必要なアクションは、顧客自身が実行する必要があります。詳細については、[データ保護に関する技術支援]({{site.baseurl}}/dp-technical-assistance)のドキュメントを参照してください。