---
nav_title: ホーム
article_title: Brazeの新機能
description: "Brazeリリースノートは毎月発行されるため、主要な製品リリース、継続的な製品改良、Brazeパートナーシップ、SDKの破壊的変更、および機能の非推奨について最新の状態を維持できます。"
page_order: 0
search_rank: 1
page_type: reference

---

# Brazeの新機能 {#whats-new-in-braze}

{% alert tip %}
このページに記載されている更新の詳細については、アカウントマネージャーにお問い合わせいただくか、[サポートチケットを開いて]({{site.baseurl}}/user_guide/administer/personal/braze_support)ください。また、[SDK変更ログ]({{site.baseurl}}/developer_guide/changelogs)では、毎月のSDKリリース、改良、および破壊的変更に関する詳細を確認することもできます。
{% endalert %}

{% details 2026年7月23日 %}

## 2026年7月23日リリース {#july-23-2026-release}

### データ＆レポート {#data-reporting}

#### メッセージング診断ダッシュボード {#messaging-diagnostics-dashboard}

{% multi_lang_include release_type.md release="General availability" %}

[メッセージング診断ダッシュボード]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/diagnostics_dashboard)は、メッセージ送信結果の概要を提供し、トレンドを把握してメッセージング設定の潜在的な問題を診断できます。このダッシュボードは、キャンペーンやキャンバスからのメッセージが期待どおりに送信されなかった理由を理解するのに役立ちます。この機能へのアクセスについては、カスタマーサクセスマネージャーにお問い合わせください。

#### CSVカスタムイベントマッパー {#csv-custom-events-mapper}

{% multi_lang_include release_type.md release="General availability" %}

カスタムイベントの[CSVインポートフロー]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import#about-csv-import)に、インポート前にイベント名とイベントプロパティヘッダーをBrazeフィールドにマッピングできるマッパーが追加されました。この更新により、カスタムイベントのエクスペリエンスがカスタム属性フローと統一され、アップロード前のファイル再フォーマットの必要性が軽減されます。フローには、CSVのアップロード、必須フィールドとイベントのマッピング、イベントプロパティのマッピング、インポート前のターゲティング設定の選択が含まれます。ファイルが既に期待されるフォーマットに一致している場合は、マッピングの変更なしでフローを続行できます。

#### カタログの無料ストレージが最大500 MBに対応 {#catalogs-free-storage-now-supports-up-to-500-mb}

{% multi_lang_include release_type.md release="General availability" %}

[カタログ]({{site.baseurl}}/user_guide/data/activation/catalogs/create#tiers)の無料版が、すべてのCSVファイルで最大500 MBのストレージをサポートするようになりました。

### BrazeAI<sup>TM</sup>

#### Operatorが設定ページを更新可能に {#operator-can-now-update-settings-pages-for-you}

{% multi_lang_include release_type.md release="General availability" %}

[Operator]({{site.baseurl}}/user_guide/brazeai/operator/capabilities)が、より多くの設定ページで直接変更を行えるようになりました。設定画面をクリックして操作する代わりに、自然言語で変更内容を記述できます。サポートされるページは以下のとおりです。

- クワイエットアワー
- プッシュ設定
- メッセージングレート制限
- メッセージングルールと常時承認ワークフロー
- その他の識別子とAPI制限
- 連絡先情報

たとえば、クワイエットアワーページで、OperatorにSMSのクワイエットアワーを午後9時から午前8時に設定するよう依頼できます。

#### リモートBraze MCPサーバー {#remote-braze-mcp-server}

{% multi_lang_include release_type.md release="Early access" %}

[Braze MCPサーバー]({{site.baseurl}}/user_guide/brazeai/mcp_server)は、Claude、ChatGPT、Cursor、VSCode、Codex、Google Antigravity、Claude CodeなどのAIエージェントをBrazeに直接接続できるリモートホスト型の接続です。自然言語を通じて、エージェントはキャンペーン、キャンバス、セグメントの分析、カスタム属性、イベント、KPI、カタログを読み取り、メールテンプレート、Content Blocks、メディアライブラリアセットを作成または更新できます。ユーザープロファイルのPIIは公開されません。

接続するには、MCPクライアントに1つのエンドポイントURLを貼り付けます。USの場合は`https://mcp.braze.com/mcp`、EUの場合は`https://mcp.braze.eu/mcp`です。その後、SSOを含むOAuthでサインインします。サーバーは利用可能なツールとともに起動します。

### オーケストレーション {#orchestration}

#### チームのオーディエンススコーピング {#teams-audience-scoping}

{% multi_lang_include release_type.md release="General availability" %}

[チーム]({{site.baseurl}}/user_guide/administer/global/user_management/teams)のオーディエンス設定が複数のフィルターをサポートするようになりました。

### チャネルとタッチポイント {#channels-touchpoints}

#### アプリ内メッセージとランディングページのアンケート評価スケール {#survey-rating-scale-for-in-app-messages-and-landing-pages}

{% multi_lang_include release_type.md release="Early access" %}

[ランディングページアンケート]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/surveys#rating-scale)と[アプリ内メッセージアンケート]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/surveys#rating-scale)の両方のフォームブロックに数値評価スケールを追加して、カスタムコードなしでセンチメント、満足度、推奨度を収集できます。1〜10、1〜5、0〜10（標準NPSレンジ）の3つのレンジがサポートされています。

#### WhatsApp期間限定オファーテンプレート {#whatsapp-limited-time-offer-templates}

{% multi_lang_include release_type.md release="General availability" %}

[WhatsApp期間限定オファーテンプレート]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message/message_and_image_formats#limited-time-offer-templates)は、オファーの有効期限が近づくとオプションのカウントダウン付きで期間限定のプロモーションオファーを表示します。季節セールやユーザー属性にパーソナライズされたオファーなど、期間限定のプロモーションにこのレイアウトを使用します。

#### Shopifyセルフサーブ SDKバージョンアップグレード {#shopify-self-serve-sdk-version-upgrade}

{% multi_lang_include release_type.md release="General availability" %}

新しい[Shopify]({{site.baseurl}}/partners/ecommerce/shopify)顧客は、セットアップ時に最新のBraze Web SDKおよびJavaScript SDKバージョンでプロビジョニングされます。既存の顧客は、インテグレーション設定で現在のSDKバージョンを確認し、新しいバージョンが利用可能になったときに通知を受け取り、インテグレーション設定からセルフサーブでアップグレードできます。

#### バナー用HTMLエディタ {#html-editor-for-banners}

{% multi_lang_include release_type.md release="General availability" %}

バナーを作成する際に、[HTMLエディタを使用して]({{site.baseurl}}/user_guide/channels/banners/create_a_banner#compose-a-banner)構築できるようになりました。HTMLエディタは、独自のHTMLテンプレートを既に管理しているチームや、バナーのマークアップとスタイリングを完全にコントロールしたいチームに最適です。カスタムHTMLをエディタに直接記述または貼り付けできます。

#### メディアライブラリのファイル置換 {#replace-a-file-in-the-media-library}

{% multi_lang_include release_type.md release="General availability" %}

URLとアセットIDを安定させたまま、[既存のメディアライブラリアセットのファイルを置換]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library#replace-a-file)できるようになりました。URLが変わらないため、そのアセットを参照するキャンペーン、キャンバス、Content Block、テンプレートは自動的に更新されたファイルを反映するため、使用されているすべての場所で手動で再アップロードや再リンクする必要がありません。

#### メディアライブラリのグリッドビュー {#grid-view-for-the-media-library}

{% multi_lang_include release_type.md release="General availability" %}

メディアライブラリと一部のテンプレートライブラリで、既存のリストビューに加えてグリッドビューが提供されるようになりました。グリッドビューは、アセットをサムネイルと主要なメタデータ（名前、タイプ、最終更新日）とともに表示し、ファイル名ではなく見た目で画像やクリエイティブを素早く見つけることができます。フィルタリングと検索は両方のビューで同じように機能します。

#### 共有可能プレビューが追加チャネルに対応 {#shareable-preview-support-for-more-channels}

{% multi_lang_include release_type.md release="General availability" %}

[共有可能プレビュー]({{site.baseurl}}/user_guide/channels/email/html_editor#step-3b-preview-and-test-your-message)が以下の追加チャネルをサポートするようになりました。

- SMS、MMS、RCS
- WhatsApp
- プッシュ
- Content Cards
- LINE

キャンペーンまたはメッセージからリンクを生成し、Brazeダッシュボードにアクセスできないレビュアー（ブランド、法務、外部エージェンシーなど）と共有できます。受信者は任意のブラウザでリンクを開き、テストパーソナライゼーションを含め、顧客が見るようにレンダリングされたメッセージを確認できます。

#### プッシュ認証情報更新API {#push-credentials-update-api}

{% multi_lang_include release_type.md release="General availability" %}

[プッシュ認証情報更新エンドポイント]({{site.baseurl}}/api/endpoints/apps/post_update_push_credential)を使用して、プッシュ認証情報をプログラムで更新できるようになりました。各リクエストは1つのアプリと1つのプラットフォーム（`apple`、`firebase`、`huawei`、または`kindle`）を更新し、認証情報ペイロードをBase64エンコード値として受け入れます。これにより、手動のダッシュボードアップロードに依存せずに、大規模なアプリポートフォリオと認証情報ローテーションポリシーを管理できます。

### パートナーシップ {#partnerships}

#### Refiner - アンケート {#refiner-surveys}

[Refiner](https://refiner.io)は、SaaSおよびモバイルアプリ向けのアプリ内アンケートプラットフォームです。プロダクトチームやVoC（顧客の声）チームが、ターゲットを絞ったアプリ内アンケートを起動し、NPS、CSAT、CES、製品フィードバック、ゼロパーティユーザーデータを継続的に収集できます。

#### Stayfilm - ビジュアルとインタラクティブコンテンツ {#stayfilm-visual-and-interactive-content}

[Stayfilm](https://www.stayfilm.com/)は、大規模な自動パーソナライズ動画制作のためのREST APIです。データ、画像、テキスト、サウンドトラック、ナレーション、ビジュアルエフェクトを統合して、eコマース、マーケットプレイス、CRMワークフロー、マーケティングキャンペーン向けのカスタマイズされた動画コンテンツを生成します。

#### Validity - データと分析 {#validity-data-and-analytics}

[Validity Everest](https://www.validity.com/everest/)は、受信トレイ配置の測定と送信レピュテーションの保護に役立つメールデリバラビリティプラットフォームです。BrazeとValidityのインテグレーションは、EverestシードリストをBrazeに同期し、対象のキャンペーンやキャンバスに自動的にシードを配置し、エンゲージメント指標をValidity Inboxに取り込むことで、シードベースの配置と実際のサブスクライバーエンゲージメントを比較できます。

### SDK

以下のSDK更新がリリースされました。詳細については、[SDK変更ログ]({{site.baseurl}}/developer_guide/changelogs)を参照してください。

#### SDKの破壊的更新 {#sdk-breaking-updates}

最新のSDK更新がリリースされました。破壊的更新はSDK更新セクションに記載されています。その他すべての更新は、対応するSDK変更ログをご確認ください。

- [Android SDK 43.0.0](https://github.com/braze-inc/braze-android-sdk/releases/tag/v43.0.0)
    - `unregisterPush`およびログアウトメソッドを追加しました。
    - eコマースイベントに追加フィールドを追加しました。
    - プッシュ通知画像読み込みの指数バックオフを追加しました。
- [Swift SDK 17.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
    - eコマースイベントに追加フィールドを追加しました。
    - 初期化後のデータ状態を予測可能にしました。
    - デバイスおよびユーザー識別子のノンブロッキングアクセサーを追加しました。
    - `Braze.LiveActivities`の非推奨のpush-to-start更新APIを削除しました。
- [Web SDK 6.10.1](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
    - `unregisterPush`およびログアウトメソッドを追加しました。
    - eコマースイベントに追加フィールドを追加しました。
    - 起動時の冗長なリフレッシュに関連するバナーおよびContent Cardsの問題を修正しました。
    - バナー却下のパブリックメソッドを追加しました。
- [Flutter SDK 21.0.0](https://github.com/braze-inc/braze-flutter-sdk/releases/tag/v21.0.0)
    - ネイティブiOSブリッジを更新しました。
    - 非推奨メソッドを削除しました。
    - `changeUser`、`enableSDK`、`disableSDK`ハンドラーを完了結果を返すように更新しました。
- [Expo SDK 5.2.0](https://github.com/braze-inc/braze-expo-plugin/releases/tag/v5.2.0)
    - サンプルアプリをExpo SDK 56に更新しました。
- [React Native SDK 22.0.0](https://www.npmjs.com/package/@braze/react-native-sdk/v/22.0.0)
    - バナー却下のサポートを追加しました。
    - バインディングの更新を含みます。

{% enddetails %}
{% details 2026年6月25日 %}

## 2026年6月25日リリース {#june-25-2026-release}

### データ＆レポート

#### Content Cardsおよびバナーの指標名の更新 {#metric-name-update-for-content-cards-and-banners}

Content Cardsおよびバナーの_ユニーク受信者_指標が_ユニークデイリーインプレッション_に名前変更されました。_ユニークデイリーインプレッション_は、Brazeから受信した数値を指し、`user_id`に基づいています。ユニークデイリーインプレッションは、キャンペーンまたはキャンバスステップレベルでカウントされます。詳細については、[指標用語集]({{site.baseurl}}/user_guide/analytics/metrics_glossary)を参照してください。

#### ユーザー削除 {#user-deletion}

{% multi_lang_include release_type.md release="General availability" %}

[ユーザー削除]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles/delete_users)を使用すると、不要になったプロファイル、誤って作成されたプロファイル、またはコンプライアンス（GDPRやCCPAなど）のために削除が必要なプロファイルを削除してデータベースを管理できます。

#### データポイント除外 {#data-point-exclusions}

{% multi_lang_include release_type.md release="General availability" %}

[eコマース推奨イベント]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events)は、課金対象のデータポイントにカウントされなくなりました。Braze eコマースイベント（`ecommerce.product_viewed`、`ecommerce.cart_updated`、`ecommerce.checkout_started`、`ecommerce.order_placed`、`ecommerce.order_cancelled`、`ecommerce.order_refunded`）をデータポイント消費なしで採用できます。

#### イベント履歴タブ {#event-history-tab}

{% multi_lang_include release_type.md release="General availability" %}

[ユーザープロファイル]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles)の**イベント履歴**タブには、過去30日間のユーザーのカスタムイベントと購入が一覧表示されます（最新100件まで）。SDKまたはAPIインテグレーションが期待どおりにイベントを送信しているかの確認、ユーザーがイベントトリガーのキャンペーンやキャンバスに入った（または入らなかった）理由のデバッグ、特定のユーザーに関するサポートエスカレーションの調査に使用できます。

#### Amazon SES顧客向けのデリバラビリティセンターでのMicrosoft SNDSデータ表示 {#deliverability-center-surfaces-microsoft-snds-data-for-amazon-ses-customers}

Amazon SES経由でメールを送信するワークスペースでは、[デリバラビリティセンター]({{site.baseurl}}/deliverability_center)が専用送信IPのMicrosoft SNDS指標を表示します。この機能がワークスペースで有効になると、Brazeは最大90日間の過去のSNDSデータをバックフィルします。

### BrazeAI<sup>TM</sup>

#### Operatorに統合されたBrazeAIアシスタント {#unified-brazeai-assistants-in-operator}

ダッシュボード全体に散在していたスタンドアロンのBrazeAIアシスタントが[BrazeAI Operator]({{site.baseurl}}/user_guide/brazeai/operator)に統合され、Operatorがダッシュボード全体のマーケター向け生成AI支援のための単一のAIアシスタントとして確立されました。以下のアシスタントがOperator経由でルーティングされるようになりました。

{% multi_lang_include releases/brazeai_operator_legacy_assistants.md %}

既存のエントリポイントは、以前の各レガシーアシスタントボタンがあった場所にそのまま残ります。スタンドアロンアシスタントを開く代わりに、これらのエントリポイントはタスクに事前スコープされたダイナミックプロンプトを持つOperatorペインを開くようになりました。これらのエントリポイントは、既存のワークフローを調整することなくこれらの機能を使用できるように、Operatorへの直接ルートを提供します。

#### キャンペーン作成と編集のOperatorサポート {#operator-support-for-campaign-creation-and-editing}

[Operator]({{site.baseurl}}/user_guide/brazeai/operator)が、メッセージの作成だけでなく、キャンペーン全体の作成と編集ができるようになりました。1つの自然言語プロンプトまたはキャンペーンブリーフから、Operatorはレビュー可能なキャンペーンをエンドツーエンドで構築します。メッセージの作成、配信のスケジュール、オーディエンスのターゲティング、コンバージョンイベントの割り当てを行い、レビューステップで構築内容を要約します。以前は、Operatorはメッセージの作成（キャンペーン作成の5つのステップのうちの1つ）のみが可能でしたが、残りのスケジュール、ターゲット、割り当て、レビューのステップも可視化・制御できるようになりました。

この機能は、**キャンペーン**ページまたは既存のキャンペーン内から利用できます。その結果、Operatorは以下が可能です。

{% multi_lang_include releases/brazeai_operator_campaign_creation_prompts.md %}

#### Content BlocksのOperatorサポート {#operator-support-for-content-blocks}

[Operator]({{site.baseurl}}/user_guide/brazeai/operator)が、[Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks)（一度構築して複数のメッセージで参照する再利用可能なスニペット）を自然言語プロンプトから直接作成・編集できるようになりました。**Content Blocks**ページから、Operatorに新しいContent Blockをゼロから作成するか、既存のものを編集するよう依頼すると、Operatorがレビュー用のコンテンツを生成または更新します。

#### Operatorで構築されたエージェントコンソールテンプレート {#agent-console-templates-built-with-operator}

**エージェントコンソール**でエージェントを構築する際に、カスタムエージェントを作成するか、**Operatorでエージェントを作成**のオプションを選択してBrazeAI Operatorで開始テンプレートを適用できます。Operatorは、以下のエージェントコンソール開始テンプレートの指示、出力フィールド、コンテキストを事前設定できます。

詳細については、[カスタムエージェントの作成]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#agent-templates-built-with-operator)を参照してください。

#### エージェントコンソールの機能強化 {#agent-console-enhancements}

[エージェントコンソール]({{site.baseurl}}/user_guide/brazeai/agents)で以下が可能になりました。

{% multi_lang_include releases/brazeai_agent_console_enhancements.md %}

#### 起動済みコンテンツオプティマイザーステップの編集 {#edit-a-launched-content-optimizer-step}

{% multi_lang_include release_type.md release="Beta" %}

キャンバスの起動後、[コンテンツオプティマイザーステップを更新]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/content_optimizer_step#edit-a-launched-step)して以下が可能になりました。

{% multi_lang_include messaging/canvas/content_optimizer_launched_step_actions.md %}

### チャネルとタッチポイント

#### バナーのユーザー却下 {#user-dismissals-for-banners}

{% multi_lang_include release_type.md release="General availability" %}

却下動作を設定する際に**バナーを却下可能**を選択することで、ユーザーがバナーを手動で却下できるようにすることができます。このオプションは、すべてのアプリユーザーに期間限定セールを宣伝したいが、興味がない場合にメッセージを却下できるようにしたいシナリオで有益です。

却下の有効化と却下ボタンのカスタマイズの詳細については、[却下動作の設定]({{site.baseurl}}/user_guide/channels/banners/create_a_banner#dismiss-behavior)を参照してください。

#### バナーのカスタムクリックトラッキング {#custom-click-tracking-for-banners}

{% multi_lang_include release_type.md release="General availability" %}

バナーのより詳細なクリックトラッキングのために、プロパティパネルの**レポート用識別子**フィールドを使用して、各インタラクティブ要素に[カスタム識別子を割り当て]({{site.baseurl}}/user_guide/channels/banners/create_a_banner#step-32-define-on-click-behavior-optional)できます。

#### バナーの再適格性 {#re-eligibility-for-banners}

バナーキャンペーンで再適格性が有効になっている場合、バナーを却下したユーザーは、却下時に開始される設定可能なクールダウンウィンドウの後に再び適格になることができます。再適格性がオンになっていない場合、却下したユーザーは不適格のままです。再適格性を設定するには、[再適格性の設定]({{site.baseurl}}/user_guide/channels/banners/create_a_banner#re-eligibility)を参照してください。キャンバスのバナーステップは、キャンバスの再エントリ設定を使用することに注意してください。

#### クイックプッシュABテスト {#quick-push-ab-testing}

{% multi_lang_include release_type.md release="General availability" %}

クイックプッシュABテストが、バリアントグループを通じてマルチプラットフォームのプッシュキャンペーンおよびキャンバスステップをサポートするようになりました。これにより、1つのワークフローで整合されたiOSとAndroidのメッセージバリエーションをテストできます。詳細については、[マルチプラットフォームプッシュメッセージ]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/multiple_platform_push#use-cases)を参照してください。

#### BrazeAI<sup>TM</sup>バリアントセレクション {#brazeai-variant-selection}

{% multi_lang_include release_type.md release="Early access" %}

BrazeAI<sup>TM</sup>バリアントセレクションは、複数のプッシュバリアントを追加すると自動的にオンになり、推奨される実験デフォルトを適用し、エンゲージメントを向上させるために最もパフォーマンスの高いバリアントに最適化します。即時送信が必要な場合はオフにできます。詳細については、[BrazeAI<sup>TM</sup>バリアントセレクション]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/variant_selection)を参照してください。

#### WhatsAppテスト送信結果 {#whatsapp-test-send-results}

テストWhatsAppメッセージを送信した後、メッセージ作成画面で直接[詳細な配信レポート]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message#step-4-view-test-send-results)を確認できます。これにより、メッセージが意図した受信者に届いたことを確認し、起動前に失敗をトラブルシューティングするのに役立ちます。

### パートナーシップ

#### Convercus - データと分析 - ロイヤルティ {#convercus-data-and-analytics-loyalty}

[Convercus]({{site.baseurl}}/partners/data_and_analytics/loyalty/convercus)は、ブランドや小売業者がオムニチャネルロイヤルティプログラムとパーソナライズされたクーポンキャンペーンを通じて、顧客の来店頻度、バスケット価値、再購入率を向上させるのに役立つSaaSロイヤルティおよびクーポンプラットフォームです。

#### Copy Pastd - メッセージオーケストレーション - テンプレート {#copy-pastd-message-orchestration-templates}

[Copy Pastd]({{site.baseurl}}/partners/copy_pastd) Building Blocksは、Liquid対応のContent Blocksと完全なテンプレートをBrazeワークスペースに直接プッシュするドラッグ＆ドロップメールビルダーです。一度デザインし、Brazeに同期して、毎回HTMLを再構築することなく、キャンペーン、キャンバス、トリガーフロー全体で同じコンポーネントを再利用できます。

#### Databricks Mosaic - AIモデルプロバイダー {#databricks-mosaic-ai-model-providers}

[Databricks Mosaic]({{site.baseurl}}/partners/databricks_mosaic)は、Databricks Data Intelligence Platform上でAIおよび機械学習モデルを大規模に構築、デプロイ、管理するためのDatabricksの統合プラットフォームです。

#### DinMo - データと分析 - リバースETL {#dinmo-data-and-analytics-reverse-etl}

[DinMo]({{site.baseurl}}/partners/dinmo)は、リバースExtract、Transform、Load（ETL）を通じてクラウドデータウェアハウスをBrazeに接続するコンポーザブル顧客データプラットフォーム（CDP）です。マーケティングチームは、ウェアハウスデータからオーディエンスセグメントを構築し、ユーザー属性とイベントをBrazeに同期し、CSVアップロードやエンジニアリングサポートなしでサブスクリプションステータスを最新の状態に保つことができます。

#### EmailShepherd - メッセージオーケストレーション - テンプレート {#emailshepherd-message-orchestration-templates}

[EmailShepherd]({{site.baseurl}}/partners/emailshepherd)は、メールデザインシステム上に構築されたエージェント型メール作成プラットフォームで、マーケティングチーム全体（およびAIエージェント）がボトルネックなしにオンブランドで本番対応のメールを作成できます。Brazeインテグレーションは、承認されたメールをBrazeワークスペースに直接公開するため、マーケターはブランドの一貫性を犠牲にすることなくBrazeでのメール制作をスケールできます。

#### Talkable - メッセージパーソナライゼーション - リファラル {#talkable-message-personalization-referrals}

[Talkable]({{site.baseurl}}/partners/talkable)は、消費者ブランドが満足した顧客をスケーラブルなリファラルチャネルに変えるのに役立ちます。Brazeインテグレーションにより、TalkableリファラルキャンペーンでキャプチャされたマーケティングメールのオプトインがリアルタイムでBrazeに流れ込み、すべての新しいアドボケートとフレンドを歓迎、セグメント化、エンゲージするために必要な同意、コンテキスト、キャンペーンデータをチームに提供します。

### SDK

#### SDKの破壊的更新

最新のSDK更新がリリースされました。破壊的更新はSDK更新セクションに記載されています。その他すべての更新は、対応するSDK変更ログをご確認ください。

{% multi_lang_include releases/sdk/2026_6_25_26_updates.md %}

{% enddetails %}

{% details 2026年5月28日 %}

## 2026年5月28日リリース {#may-28-2026-release}

### データ＆レポート

#### プッシュパフォーマンスダッシュボード {#push-performance-dashboard}

[プッシュパフォーマンスダッシュボード]({{site.baseurl}}/user_guide/analytics/dashboards/channel_performance?tab=push%20performance#push-performance-dashboard)は、プッシュエンゲージメントのチャネルレベルの単一ビューを提供します。送信、バウンス、配信、直接・影響・合計の開封率を設定可能な時間ウィンドウで確認できます。個々のキャンペーンやキャンバスからデータを集計することなく、プッシュチャネル全体の健全性を把握するために使用します。

#### カタログセレクションのジオロケーションフィールド {#geolocation-fields-in-catalog-selections}

{% multi_lang_include release_type.md release="General availability" %}

カタログが、新しいジオロケーションフィールドタイプとカタログセレクション演算子による距離ベースのフィルタリングをサポートするようになりました。これにより、各ユーザーに最寄りのレストランを表示したり、不動産キャンペーンで50km以内の物件をフィルタリングしたり、特定のイベント近くの店舗をターゲットにしたりするなど、よりロケーションに関連したエクスペリエンスを作成できます。都市やリージョンコードで地理的ターゲティングを近似する代わりに、ユーザーの最新のロケーションなどのLiquidユーザー属性を含む中心点への近接度でカタログアイテムをフィルタリングできます。詳細については、[セレクション]({{site.baseurl}}/user_guide/data/activation/catalogs/selections)を参照してください。

#### レポートビルダーのバナーとRCS {#banner-and-rcs-for-report-builder}

[レポートビルダー]({{site.baseurl}}/report_builder)がバナーをチャネルとして、RCSをSMSのサブカテゴリーとしてサポートするようになりました。これにより、他のすべてのBrazeチャネルと並べて、カスタムレポートで両方のパフォーマンスを直接測定できます。

#### `ecommerce.cart_updated`イベントアクション {#ecommercecart_updated-event-actions}

[`ecommerce.cart_updated`イベント]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/?tab=ecommerce.cart_updated#code-examples)が`replace`に加えて`add`および`remove`アクションをサポートするようになり、更新のたびにカート全体のスナップショットを送信する代わりに、増分的なカート変更を送信できます。

### BrazeAI<sup>TM</sup>

#### SMS、MMS、RCSメッセージ向けコンテンツオプティマイザー {#content-optimizer-for-sms-mms-and-rcs-messages}

{% multi_lang_include release_type.md release="Beta" %}

[コンテンツオプティマイザー]({{site.baseurl}}/user_guide/brazeai/content_optimizer)を使用して、SMS、MMS、RCSメッセージのフック、本文、CTAを最適化できます。コンテンツオプティマイザーは、AIを使用して大量のコンテンツバリアントを自動的に生成・評価し、メッセージコンテンツを大規模にテスト・最適化するのに役立ちます。

### オーケストレーション

#### ワークスペースのタイムゾーン {#workspace-time-zones}

{% multi_lang_include release_type.md release="General availability" %}

[ワークスペースのタイムゾーン]({{site.baseurl}}/user_guide/administer/global/admin_settings/workspace_time_zone)を使用して、個々のワークスペースに特定のタイムゾーンを定義できます。これにより、スケジュールされたキャンペーンやキャンバス（ローカルタイムやインテリジェントタイミングを使用しないもの）が、全体的な会社のタイムゾーンではなく、ワークスペースの指定されたタイムゾーンに従って送信されます。

メッセージ送信のワークスペースタイムゾーンは段階的に展開されているため、ダッシュボードにこれらの設定がまだ表示されない場合があります。

### チャネルとタッチポイント

#### WhatsApp `inbound_profile_name`

Metaの受信メッセージングwebhookからユーザーのWhatsApp表示名を自動的にキャプチャし、ユーザーのBrazeプロファイルに書き込むことができます。受信WhatsAppメッセージを受信すると、Brazeはプロファイル名を新しいWhatsApp Liquid属性[{% raw %}`{{whats_app.${inbound_profile_name}}}`{% endraw %}]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags)として公開します。これをキャンバスのユーザー更新ステップで参照して、プロファイルフィールドに保存できます。

#### 孤立したSMSサブスクリプション状態 {#orphaned-sms-subscription-states}

Brazeは[孤立したサブスクリプション状態レコードを自動的に管理]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups#how-braze-handles-orphaned-subscription-states)します（ユーザープロファイルに紐付けられていない電話番号やメールアドレスに保存されたサブスクリプションデータ）。これにより、意図しないサブスクリプション状態の継承を防止します。新しく作成されたユーザープロファイルが、以前に削除された、または無関係なユーザーからサブスクリプション状態を誤って継承するシナリオからユーザーを保護します。

### パートナーシップ

#### Chord - 顧客データプラットフォーム {#chord-customer-data-platform}

[Chord](https://www.chord.co/)は、eコマースストアフロントからイベントをキャプチャし標準化する顧客データプラットフォームを提供します。ChordをBrazeに接続すると、購入アクティビティ、行動イベント、アイデンティティの更新がBrazeに流れ込み、パイプラインを自分で構築することなく、キャンペーンをトリガーしてプロファイルを最新の状態に保つことができます。

詳細については、[Chord]({{site.baseurl}}/partners/chord)を参照してください。

#### Better Email - テンプレート {#better-email-templates}

[Better Email](https://www.betteremail.dev)は、メールデザインシステムを中心に構築されたコラボレーティブなメール作成プラットフォームです。チームは、ブロックとスタイルの共有システムから本番対応のメールをデザイン、管理、エクスポートでき、開発者やエージェンシーに依存することなく、大規模にブランドの一貫性を確保できます。

詳細については、[Better Email]({{site.baseurl}}/partners/better_email)を参照してください。

#### DailyPlay - ダイナミックコンテンツ {#dailyplay-dynamic-content}

[DailyPlay](https://dailyplay.ai/)はゲーミフィケーションプラットフォームです。パーソナライズされたブランドゲームと組み込みのリワードシステムを起動して、エンゲージメントを深め、リテンションを向上させるために使用します。

詳細については、[DailyPlay]({{site.baseurl}}/partners/dailyplay)を参照してください。

### SDK

#### SDKの破壊的更新

最新のSDK更新がリリースされました。破壊的更新はSDK更新セクションに記載されています。その他すべての更新は、対応するSDK変更ログをご確認ください。

{% multi_lang_include releases/sdk/2026_5_28_26_updates.md %}

{% enddetails %}
{% details 2026年4月30日 %}

## 2026年4月30日リリース {#april-30-2026-release}

### データ＆レポート

#### 個別プロファイル作成のためのクイックユーザー追加 {#quick-user-add-for-individual-profile-creation}

{% multi_lang_include release_type.md release="General availability" %}

**ユーザーをインポート**から**クイックユーザー追加**を選択し、メールアドレスまたはexternal IDを入力することで、個別のユーザープロファイルを作成できるようになりました。

以前は、このワークフローからユーザーを作成するにはCSVアップロードまたは自動取り込み方法が必要でした。

詳細については、[CSVインポート]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import)を参照してください。

#### ゼロコピーCDI同期によるキャンバストリガー {#zero-copy-cdi-syncs-for-canvas-triggers}

{% multi_lang_include release_type.md release="General availability" %}

CDIがゼロコピーパーソナライゼーション用の`キャンバス triggers`データタイプをサポートするようになりました。ウェアハウスまたはS3データからキャンバスをトリガーし、Brazeユーザープロファイルにフィールドを保持せずにコンテキストフィールドを渡すことができます。

以前は、CDI同期ではこのタイプのパーソナライゼーションワークフローのためにデータをBrazeプロファイルに書き込む必要がありました。

詳細については、[CDIを使用したゼロコピーパーソナライゼーション]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/zero_copy_sync)を参照してください。

#### eコマース推奨イベント {#ecommerce-recommended-events}

{% multi_lang_include release_type.md release="General availability" %}

[eコマース推奨イベント]({{site.baseurl}}/user_guide/data/activation/events/recommended_events)は、購入ジャーニーの6つのステップをカバーします：`product_viewed`、`cart_updated`、`checkout_started`、`order_placed`、`order_cancelled`、`order_refunded`。これらのイベントを正常に送信すると、Brazeはデータを検証し、拡大するプラットフォーム機能のセットで利用可能にします。

### Currentsとデータ共有 {#currents-and-datashare}

#### 新しいバナーおよびWhatsApp Currents更新 {#new-banner-and-whatsapp-currents-updates}

{% multi_lang_include release_type.md release="General availability" %}

Currentsとデータ共有に、新しい`Banner.Dismiss`イベントと既存のWhatsAppイベントの追加フィールドが含まれるようになりました。

以前は、これらのバナー却下イベントとWhatsAppフィールドはエクスポートデータで利用できませんでした。

詳細については、[Currents変更ログ]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs)を参照してください。

### オーケストレーション

#### 多言語翻訳 {#multi-language-translations}

{% multi_lang_include release_type.md release="General availability" %}

複雑なコードを必要としないワンタイムのロケール設定で[多言語メッセージ]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages)を作成し、すべての市場に自信を持って送信できます。

#### きめ細かな権限の移行 {#granular-permissions-migration}

{% multi_lang_include release_type.md release="General availability" %}

アカウントにアクセスし特定のアクションを実行できるユーザーを管理することは、セキュリティと運用効率の両方にとって重要です。より多くのコントロールを提供するために、Brazeはアカウント全体でユーザーアクセスを管理するためのより柔軟で正確な方法である[きめ細かな権限]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/granular_permissions_migration)を導入しています。

#### 送信先キャンバスコンポーネント {#send-to-destination-canvas-component}

{% multi_lang_include release_type.md release="General availability" %}

[送信先ステップ]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/send_to_destination)を使用すると、あるキャンバスから別のキャンバスにユーザーを送信できます。たとえば、プロモーションオファーのメッセージングを共有する2つのキャンバスがある場合、送信先を使用してこれらのキャンバスを接続できます。

#### キャンバスコンテキストの機能強化 {#canvas-context-enhancements}

{% multi_lang_include release_type.md release="General availability" %}

キャンバスで、コンテキスト変数を参照して以下を設定できるようになりました。

- Content Cardsの削除イベント
- Content Cardsの有効期限

詳細については、[カード作成]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card/card_creation/?tab=canvas)を参照してください。

#### メッセージステップの配信バリデーション進行動作 {#delivery-validation-advancement-behavior-for-message-steps}

{% multi_lang_include release_type.md release="General availability" %}

[配信バリデーション]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#delivery-validations)は、メッセージ送信時にオーディエンスが配信基準を満たしていることを確認するための追加チェックを提供します。ユーザーがメッセージステップの設定された配信バリデーションを満たさない場合、**配信バリデーション進行動作**設定を使用して、ユーザーが次のステップに進むかキャンバスを退出するかを決定できます。

#### ワークスペースメッセージングレート制限 {#workspace-messaging-rate-limits}

{% multi_lang_include release_type.md release="General availability" %}

[ワークスペースメッセージングレート制限]({{site.baseurl}}/user_guide/administer/global/workspace_settings/messaging_rate_limits)を使用して、プラットフォームからの送信メッセージの配信レートを調整し、ユーザーが必要なメッセージを確実に受信できるようにします。ワークスペースメッセージングレート制限は段階的に展開されているため、ダッシュボードにこれらの設定がまだ表示されない場合があります。

### チャネルとタッチポイント

#### WhatsAppテンプレートビルダー {#whatsapp-template-builder}

{% multi_lang_include release_type.md release="Early access" %}

[WhatsAppテンプレートビルダー]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization)を使用すると、BrazeとMeta Business Managerを切り替えることなく、Braze内で直接WhatsAppメッセージテンプレートを作成・送信できます。Metaがテンプレートを承認した後、必要な数のキャンペーンやキャンバスで使用できます。

#### Shopify製品タグ、メタフィールド、コレクション {#shopify-product-tags-metafields-and-collections}

{% multi_lang_include release_type.md release="General availability" %}

Shopifyストアから[Shopify製品タグ、コレクション、メタフィールドをBrazeカタログに同期]({{site.baseurl}}/partners/ecommerce/shopify/shopify_catalogs)できるようになりました。これにより、カスタムの回避策なしで、パーソナライゼーション、セグメンテーション、カタログベースのメッセージングのためのより豊富な製品データが提供されます。

### パートナーシップ

#### GRAVITY - データと分析 - ロイヤルティ {#gravity-data-and-analytics-loyalty}

{% multi_lang_include release_type.md release="General availability" %}

[GRAVTY®](https://www.lji.io/)は、Loyalty Juggernaut Inc.（LJI）のエンタープライズグレードのロイヤルティプラットフォームで、小売、旅行、レストラン（クイックサービスレストランを含む）、金融サービスのブランドが次世代プログラムを設計、管理、スケールできるようにし、パーソナライズされたデータ主導のエクスペリエンスを通じて、エンゲージメント、リテンション、顧客生涯価値の測定可能な成長を促進します。

<!-- Use this section to list any new SDKs or SDK updates that are already released. -->
### SDK

以下のSDK更新がリリースされました。詳細については、[SDK変更ログ]({{site.baseurl}}/releases/sdk_changelogs)を参照してください。

#### SDKの破壊的更新

{% multi_lang_include release_type.md release="General availability" %}

最新のSDK更新がリリースされました。破壊的更新はSDK更新セクションに記載されています。その他すべての更新は、対応するSDK変更ログをご確認ください。

{% multi_lang_include releases/sdk/2026_4_30_26_updates.md %}

{% enddetails %}
{% details 2026年4月2日 %}

## 2026年4月2日リリース {#april-2-2026-release}

### データ＆レポート

#### Currentsおよびデータ共有イベントの新しいバナーチャネルフィールド {#new-banner-channel-fields-in-currents-and-datashare-events}

Brazeは、Currentsおよびデータ共有エクスポートの既存のバナーチャネルイベントにフィールドを追加しました。これらのイベントおよびフィールドの更新一覧については、[バージョン7の変更点]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs#changes-for-storage)を参照してください。

#### CurrentsのMixpanel EUおよびインドデータセンターサポート {#mixpanel-eu-and-india-data-center-support-for-currents}

Currents Mixpanelインテグレーションが、MixpanelのEUおよびインドデータセンターをサポートするようになりました。Mixpanelインテグレーションを設定する際に、BrazeがデータをどのMixpanelリージョンに送信するかを選択できます。この更新は、相互顧客向けのMixpanelの国際的な拡大をサポートします。詳細については、[Mixpanel]({{site.baseurl}}/partners/data_and_analytics/analytics/mixpanel)を参照してください。

#### 再利用可能なクラウドデータ取り込み（CDI）ソースと同期 {#reusable-cloud-data-ingestion-cdi-sources-and-syncs}

{% multi_lang_include release_type.md release="Early access" %}

クラウドデータ取り込み（CDI）に、ソースと同期を分離する新しいデザインが導入され、1つのソースを複数の同期で再利用できるようになりました。既存の同期は、ダウンタイムなしで新しいソースと同期モデルに自動的に移行されます。**クラウドデータ取り込み** > **ソース**に移動して、ソースの表示、編集、作成を行い、同期を作成する際にドロップダウンからソースを選択します。この変更により、繰り返しのセットアップが削減され、将来の機能強化の基盤が構築されます。詳細については、[データウェアハウスインテグレーションの設定]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations#setting-up-data-warehouse-integrations)を参照してください。

### BrazeAI<sup>TM</sup>

#### BrazeAI Operator<sup>TM</sup>からサポートチケットを提出 {#file-support-tickets-from-brazeai-operatortm}

{% multi_lang_include release_type.md release="General availability" %}

[BrazeAI Operator]({{site.baseurl}}/user_guide/brazeai/operator)に、ダッシュボードを離れずにBrazeサポートチケットを提出するフローが追加されました。手順、自動的に含まれるコンテキスト、および迅速な解決のためのヒントについては、[BrazeAI Operatorでサポートチケットを提出]({{site.baseurl}}/user_guide/brazeai/operator/support_tickets)を参照してください。

### オーケストレーション

#### 多言語翻訳

{% multi_lang_include release_type.md release="General availability" %}

ワークスペースにロケールを追加した後、[多言語翻訳]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales)を使用して、1つのプッシュ、メール、バナー、アプリ内メッセージ、またはContent Block内で異なる言語のユーザーをターゲットにできます。

![ロケールプレビュー]({% image_buster /assets/img/multi-language_support/multi_language_user_preview.png %}){: style="max-width:70%;"}

#### キャンバスコンテキストの機能強化

{% multi_lang_include release_type.md release="General availability" %}

キャンバスで、コンテキスト変数を参照して以下を設定できるようになりました。

- メッセージステップのバナーおよびアプリ内メッセージの[有効期限]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables#set-an-expiration)
- アクションパスステップの[パーソナライズされた遅延]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables#action-path-delays)

コンテキスト変数名フィールドでは、コンテキスト変数名を入力するか、ステップエディタのドロップダウンから選択することもできます。詳細については、[コンテキスト]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context)および[コンテキスト変数]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables)を参照してください。

### チャネルとタッチポイント

#### KakaoTalk

{% multi_lang_include release_type.md release="General availability" %}

[KakaoTalk]({{site.baseurl}}/kakaotalk)は、ブロードキャストメッセージングおよびユーザーとの1:1チャットを可能にするメッセージングチャネルです。Liquidやその他のダイナミックコンテンツを使用してパーソナライズされたユーザーエクスペリエンスを作成し、ブランドとの豊かなユーザーエクスペリエンスを育成・強化する環境を構築します。

![KakaoTalkリストアイテムメッセージ。]({% image_buster /assets/img/kakaotalk/wide_image.png %}){: style="max-width:70%;"}

#### キャンバスのバナー {#banners-in-canvas}

{% multi_lang_include release_type.md release="General availability" %}

キャンバスの[メッセージステップ]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step)のメッセージングチャネルとして[バナー]({{site.baseurl}}/user_guide/message_building_by_channel/banners)を使用できます。バナーを使用すると、リアルタイムのユーザー適格性と動作を反映して、アプリやWebサイトのコンテンツを動的にパーソナライズできます。

### パートナーシップ

#### CataBoom - メッセージパーソナライゼーション - ビジュアルとインタラクティブコンテンツ {#cataboom-message-personalization-visual-and-interactive-content}

[CataBoom]({{site.baseurl}}/partners/cataboom)はゲーミフィケーションプラットフォームです。ブランドはこれを使用して、スピン・トゥ・ウィンゲーム、クイズ、インスタントウィンゲームなどのインタラクティブなデジタルエクスペリエンスを構築・起動します。これらのエクスペリエンスはエンゲージメントを深め、ファーストパーティデータを収集します。

#### Denada - メッセージオーケストレーション - テンプレート {#denada-message-orchestration-templates}

[Denada]({{site.baseurl}}/partners/denada)は、AIを活用したマーケティングクリエイティブプラットフォームで、専門家が自然な会話を通じてオンブランドのマーケティング素材を作成できます。Denadaを使用すると、チームはデザインの専門知識がなくても、アイデアから完成したメールコンテンツまで進めることができます。

#### Poq - eコマース - モバイルアプリプラットフォーム {#poq-ecommerce-mobile-app-platform}

[Poq]({{site.baseurl}}/partners/poq)は、エンタープライズビジネスがフルネイティブのiOSおよびAndroidアプリを迅速に起動、管理、スケールできるようにし、コマースを推進しブランドの約束を実現する高パフォーマンスのモバイルエクスペリエンスを提供します。

#### The Trade Desk – キャンバス Audience Sync {#the-trade-desk-canvas-audience-sync}

[Braze Audience Sync to The Trade Desk]({{site.baseurl}}/partners/canvas_audience_sync/trade_desk_audience_sync)を使用すると、ファーストパーティのユーザーデータをBrazeからThe Trade Deskに動的に同期して、広告リターゲティング、類似モデリング、抑制に活用できます。

### SDK

#### 統合開発環境（IDE）をDocs MCPに接続 {#connect-your-integrated-development-environment-ide-to-the-docs-mcp}

AIコーディングアシスタントを使用して、統合開発環境（IDE）をContext7経由でBraze Docs MCPに接続することで、Brazeインテグレーションワークフローを加速できます。これにより、アシスタントが最新のBrazeドキュメントに直接アクセスでき、開発環境でより正確なSDKガイダンス、コード例、トラブルシューティングヘルプを生成できます。Cursor、Claude Desktop、VS Codeでのセットアップ手順については、[LLMを使用した構築]({{site.baseurl}}/developer_guide/getting_started/build_with_llm#connecting-to-the-braze-docs-mcp)を参照してください。

#### SDKの破壊的更新

最新のSDK更新がリリースされました。破壊的更新はSDK更新セクションに記載されています。その他すべての更新は、対応するSDK変更ログをご確認ください。

{% multi_lang_include releases/sdk/2026_4_2_26_updates.md %}

{% enddetails %}

{% details 2026年3月5日 %}

## 2026年3月5日リリース {#march-5-2026-release}

### データ＆レポート

#### 新しいデータセンター {#new-data-center}

{% multi_lang_include release_type.md release="General availability" %}

Brazeは新しい[データセンター]({{site.baseurl}}/user_guide/data/infrastructure/data_centers)を開設しました：JP-01。Brazeアカウントの設定時にリージョン固有のデータセンターにサインアップできます。

#### コンテキスト変数 {#context-variables}

{% multi_lang_include release_type.md release="General availability" %}

[コンテキスト変数]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context)は、特定のキャンバス内でのユーザーのジャーニー中に作成・使用できる一時的なデータです。ユーザーがキャンバスに入るたびに（以前に入ったことがある場合でも）、コンテキスト変数は最新のエントリデータとキャンバス設定に基づいて再定義されます。このアプローチにより、各キャンバスエントリが独自の独立したコンテキストを維持でき、ユーザーは各状態の特定のコンテキストを保持しながら、同じジャーニー内で複数のアクティブな状態を持つことができます。

#### クラウドデータ取り込みソース {#cloud-data-ingestion-sources}

{% multi_lang_include release_type.md release="Early access" %}

[クラウドデータ取り込み]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/file_storage_integrations#setting-up-cloud-data-ingestion-in-braze)に、ソースと同期を分離する新しいUIが導入され、1つのソースを任意の数の同期で再利用できるようになりました。これにより、重複する設定が削減され、複数の同期がある場合のセットアップが簡素化されます。既存の同期がある場合、ダウンタイムなしで新しいソースと同期の構造に自動的に移行されます。開始するには、**クラウドデータ取り込み** > **ソース**に移動して、ソースの表示、編集、作成を行い、同期を作成する際にドロップダウンからソースを選択します。

#### Currentsおよびデータ共有イベントの追加フィールド {#additional-fields-for-currents-and-data-share-events}

{% multi_lang_include release_type.md release="General availability" %}

[Currentsおよびデータ共有イベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs#changes-in-version-5-release-date-2026-02-04)に、分析およびダウンストリームシステムで利用可能なデータを深めるための以下の新しいフィールドが追加されました。

{% multi_lang_include releases/currents/2026_3_5_26_field_changes.md %}

#### Snowflakeデータシェアのキャンペーンおよびキャンバスフィールド {#campaign-and-canvas-fields-for-snowflake-data-share}

{% multi_lang_include release_type.md release="General availability" %}

[Snowflakeデータシェア]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs)に、66の既存テーブルにわたるキャンペーンおよびキャンバス情報を反映する追加フィールドが含まれるようになりました。

- `campaign_name`
- `canvas_name`
- `canvas_step_name`
- `canvas_variation_name`
- `message_variation_name`
- `conversion_behavior`
- `experiment_split_name`

#### CSVプレインポートバリデーションとエラーレポート {#csv-pre-import-validation-and-error-reporting}

{% multi_lang_include release_type.md release="General availability" %}

[CSVユーザーインポート]({{site.baseurl}}/user_guide/audience/manage_audience/import_users)で、プレインポートバリデーションと詳細なエラーレポートがサポートされるようになりました。インポート前に、**ユーザーをインポート**ページで**インポート前にファイルを検証**を選択すると、Brazeがファイルをスキャンし、完全に失敗する行（エラー）と一部の値がスキップされて成功する行（警告）を特定するレポートを生成します。レポートをダウンロードしてCSVを修正して再アップロードするか、そのまま続行できます。インポート完了後、失敗した行のダウンロード可能なレポートも利用でき、各問題の正確な理由が記載されています。

#### メッセージング診断ダッシュボード

{% multi_lang_include release_type.md release="Early access" %}

[メッセージング診断ダッシュボード]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/diagnostics_dashboard)は、メッセージ送信結果の概要を提供し、トレンドを把握してメッセージング設定の潜在的な問題を診断できます。このダッシュボードは、キャンペーンやキャンバスからのメッセージが期待どおりに送信されなかった理由を理解するのに役立ちます。

### BrazeAI<sup>TM</sup>

#### エージェントコンソールのBrazeエージェント {#braze-agents-in-agent-console}

{% multi_lang_include release_type.md release="General availability" %}

[Brazeエージェント]({{site.baseurl}}/user_guide/brazeai/agents)は、Braze内で作成できるAIパワーのヘルパーです。エージェントは、コンテンツを生成し、インテリジェントな意思決定を行い、データを拡張して、よりパーソナライズされた顧客体験を提供できます。エージェントを作成する際に、その目的を定義し、動作のガードレールを設定します。ライブになった後、エージェントはBrazeに[デプロイ]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents)して、パーソナライズされたコピーの生成、リアルタイムの意思決定、またはカタログフィールドの更新を行うことができます。

### オーケストレーション

#### きめ細かなユーザー権限 {#granular-user-permissions}

{% multi_lang_include release_type.md release="Early access" %}

Brazeは、ユーザーアクセスを管理するためのより柔軟な方法である[きめ細かな権限]({{site.baseurl}}/user_guide/administer/global/user_management/permissions)を導入しています。レガシー権限がきめ細かな権限にどのようにマッピングされるかを含む移行プロセスについては、[きめ細かな権限への移行]({{site.baseurl}}/granular_permissions_migration)を参照してください。

#### チャネルベースのレート制限 {#channel-based-rate-limiting}

{% multi_lang_include release_type.md release="General availability" %}

マルチチャネルのキャンペーンまたはキャンバスの配信速度レート制限を設定する際に、共有レート制限または[チャネルベースの制限]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#multichannel-campaigns-and-canvases)のいずれかを設定できます。マルチチャネルのキャンペーンまたはキャンバスがチャネルベースのレート制限を使用する場合、レート制限は選択した各チャネルに適用されます。たとえば、キャンペーンまたはキャンバスを設定して、キャンペーンまたはキャンバス全体で1分あたり最大5,000件のwebhookと2,500件のSMSメッセージを送信できます。

#### キャンバスコンテキストステップ {#canvas-context-step}

{% multi_lang_include release_type.md release="General availability" %}

[キャンバスコンテキストステップ]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context)を使用すると、ユーザーがキャンバス内を移動する際に1つ以上の変数を作成・更新できます。たとえば、季節割引を管理するキャンバスがある場合、コンテキスト変数を使用して、ユーザーがキャンバスに入るたびに異なる割引コードを保存できます。

### チャネルとタッチポイント

#### Content Blocksでのロケール翻訳 {#translate-locales-in-content-blocks}

{% multi_lang_include release_type.md release="Early access" %}

ワークスペースにロケールを追加した後、Content Block内で[異なる言語のユーザーをターゲット]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages)にできます。

### パートナーシップ

#### Algolia - 検索レコメンデーション {#algolia-search-recommendations}

[Algolia]({{site.baseurl}}/partners/ecommerce/product_search_recommendations/algolia)は、開発者が高速で関連性が高くスケーラブルな検索エクスペリエンスを構築するのに役立つ検索・ディスカバリープラットフォームです。強力なAPIファーストアプローチにより、Algoliaは高度なランキングアルゴリズムとAI駆動のインサイトを組み合わせて、シームレスなサイト検索、ナビゲーション、パーソナライズされたコンテンツディスカバリーを実現します。

#### Anthropic - AIモデルプロバイダー {#anthropic-ai-model-provider}

[Anthropic]({{site.baseurl}}/partners/ai_model_providers/anthropic)は、AIの安全性と研究に取り組む企業で、幅広い言語タスクに対して有用で、正直で、安全な次世代AIアシスタントClaudeを開発しています。

#### Canva - メッセージパーソナライゼーション - クリエイティブスタジオ {#canva-message-personalization-creative-studio}

[Canva]({{site.baseurl}}/partners/canva)は、Canva内の画像をBrazeメディアライブラリに直接同期し、クリエイティブワークフローを合理化し、すべてのメッセージングチャネルでビジュアルアセットを最新の状態に保ちます。

#### DOTS.ECO - リワード {#dotseco-rewards}

[DOTS.ECO]({{site.baseurl}}/partners/additional_channels_and_extensions/extensions/rewards/dots_eco)は、追跡可能なデジタル証明書を通じて、現実世界の環境影響でユーザーに報酬を与えることができます。各証明書には、共有可能な証明書URLや画像URLなどのメタデータを含めることができるため、ユーザーは影響の証明を表示（再訪問）できます。

#### Figma - メッセージパーソナライゼーション - クリエイティブスタジオ {#figma-message-personalization-creative-studio}

[Figma]({{site.baseurl}}/partners/figma)は、製品の構築、デザイン、プロトタイプ作成を可能にするコラボレーティブデザインプラットフォームです。このインテグレーションを使用して、FigmaからBrazeメディアライブラリに画像やビジュアルアセットを直接送信できます。

#### Flybuy - メッセージパーソナライゼーション - ロケーション {#flybuy-message-personalization-location}

Radius Networksの[Flybuy]({{site.baseurl}}/partners/message_personalization/location/flybuy)は、AIパワーのテクノロジーを活用して、ピックアップ、デリバリー、ドライブスルー、ダインインのサービス速度を最適化する、主要なオムニチャネルロケーションプラットフォームです。統合されたMarketing Suiteを通じて、Flybuyはブランドがハイパーターゲットのモーメントベースのメッセージを配信し、エンゲージメントの促進、チェックサイズの増加、より広範なロイヤルティイニシアチブのサポートを支援します。

#### Google Gemini - AIモデルプロバイダー {#google-gemini-ai-model-provider}

[Google Gemini]({{site.baseurl}}/partners/ai_model_providers/google_gemini)は、テキスト、コード、画像にわたる高度な推論を組み合わせたGoogleのAIモデルファミリーで、ブランドがよりスマートでパーソナライズされたエクスペリエンスを提供するのに役立ちます。

#### Limbik - メッセージパーソナライゼーション - パーソナライゼーションエンジン {#limbik-message-personalization-personalization-engines}

[Limbik]({{site.baseurl}}/partners/message_personalization/dynamic_content/personalization_engines/limbik)は、AIレゾナンスレイヤーです。実際のオーディエンスがメッセージ、コンセプト、AI出力をどのように解釈し、反応するかを、市場に届く前に予測します。60以上の国と25以上の言語にわたる継続的な一次調査に基づき、Limbikは人間が検証した合成オーディエンス（マシンスピードでリサーチグレードの精度（95%信頼度、1.5%〜3%の誤差範囲）で実際のオーディエンスの反応をシミュレートするデジタル集団）を提供します。Limbikは、メッセージングがターゲットオーディエンスの信念や感情と共鳴することを即座に確認する能力を提供します。

#### Linkrunner - メッセージオーケストレーション - アトリビューション {#linkrunner-message-orchestration-attribution}

[Linkrunner]({{site.baseurl}}/partners/message_orchestration/attribution/linkrunner)は、ユーザー獲得キャンペーンの追跡と分析に役立つモバイルアトリビューションおよび分析プラットフォームです。

#### Mailizio - メッセージオーケストレーション - テンプレート {#mailizio-message-orchestration-templates}

[Mailizio]({{site.baseurl}}/partners/message_orchestration/templates/Mailizio)は、直感的なビジュアルエディタを使用して再利用可能でブランドセーフなコンテンツを簡単にデザインできるメール作成・管理プラットフォームです。MailizioのBrazeへのインテグレーションにより、コンテンツブロックとメールテンプレートをエクスポートし、同じアセットからアプリ内メッセージを自動的に生成でき、迅速かつ完全にコントロールされたキャンペーン展開が可能になります。

#### Open Loyalty - データと分析 - ロイヤルティ {#open-loyalty-data-and-analytics-loyalty}

[Open Loyalty]({{site.baseurl}}/partners/data_and_analytics/loyalty/openloyalty)は、顧客ロイヤルティおよびリワードプログラムを構築・管理できるクラウドベースのロイヤルティプログラムプラットフォームです。BrazeとOpen Loyaltyのインテグレーションは、ポイント残高、ティア変更、有効期限警告などのロイヤルティデータをリアルタイムでBrazeに直接同期します。これにより、ユーザーのロイヤルティステータスが変更されたときに、パーソナライズされたメッセージ（メール、プッシュ、SMS）をトリガーできます。

#### OpenAI - AIモデルプロバイダー {#openai-ai-model-provider}

[OpenAI]({{site.baseurl}}/partners/ai_model_providers/openai)は、GPTなどの高度なAIモデルを作成し、自然言語の理解と生成を可能にして、ブランドが意味のある顧客インタラクションを構築・スケールできるようにします。

#### Shopgate - チャネル {#shopgate-channels}

[Shopgate]({{site.baseurl}}/partners/additional_channels_and_extensions/additional_channels/shopgate)は、マーチャントがショッピングアプリを作成し、フルフィルメントツールとクライアンテリング（顧客データに基づくパーソナライズされた店内カスタマーサポート）を通じて実店舗の効率を向上させるのに役立つモバイルコマースおよびオムニチャネルプラットフォームです。

#### Splio - データと分析 - コホートインポート {#splio-data-and-analytics-cohort-import}

[Splio]({{site.baseurl}}/partners/data_and_analytics/cohort_import/splio)は、顧客体験を損なうことなくキャンペーン数と収益を増加させるオーディエンス構築ツールで、オンラインとオフラインの両方でCRMキャンペーンのパフォーマンスを追跡する分析を提供します。

### SDK

#### SDKの破壊的更新

最新のSDK更新がリリースされました。破壊的更新はSDK更新セクションに記載されています。その他すべての更新は、対応するSDK変更ログをご確認ください。

{% multi_lang_include releases/sdk/2026_3_5_26_updates.md %}

{% enddetails %}

{% details 2026年2月5日 %}

## 2026年2月5日リリース {#february-5-2026-release}

### BrazeAI<sup>TM</sup>

#### コンテンツオプティマイザー {#content-optimizer}

{% multi_lang_include release_type.md release="Beta" %}

[コンテンツオプティマイザー]({{site.baseurl}}/user_guide/brazeai/content_optimizer)は、継続的で高バリアントなコンテンツテストのキャンバスステップで、自動エンゲージメント最適化を実現します。メッセージステップと同様のドラッグ＆ドロップ可能なインターフェイスを使用して、テストするコンポーネントを定義し、AIを使用してバリアントを生成し（または手動で入力）、Liquidタグを使用してこれらのコンポーネントをメッセージコンテンツにマッピングできます。

非コンテキストのマルチアームバンディットオプティマイザーに基づいて構築されたコンテンツオプティマイザーは、ユーザーごとに1つのメッセージを送信し、予測推奨に基づいて配信するコンポーネントバリアントの組み合わせを決定します。ステップが時間の経過とともにデータを収集すると、パフォーマンスの高いバリアントは送信割り当てが自然に増え、パフォーマンスの低いバリアントは減ります。コンテンツオプティマイザーは、継続的な最適化を可能にするために、一貫した日次ユーザーボリューム（1日あたり少なくとも数千ユーザー）を持つ繰り返し送信キャンバスで最適に動作します。

### データ＆レポート

#### eコマース推奨イベント

{% multi_lang_include release_type.md release="Early access" %}

eコマース推奨イベントと既存の購入イベントを照合するために、[「Places Order」コンバージョンイベント]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/ecommerce_use_cases#conversions-dashboard)を追加しました。これは「Makes Purchase」に似ています。

### チャネルとタッチポイント

#### バナーでのロケール翻訳 {#translate-locales-in-banners}

{% multi_lang_include release_type.md release="Early access" %}

ワークスペースにロケールを追加した後、1つのバナー内で[異なる言語のユーザーをターゲット]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages#use-locales)にできます。

#### ドラッグ＆ドロップContent Blocksの幅設定 {#configure-width-for-drag-and-drop-content-blocks}

ナビゲーションメニューのボタンを選択して、[Content Blockの幅を調整]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=email)できます。メールのグローバルスタイル設定で指定されていない場合、デフォルトの幅は100%です。指定されている場合は、グローバル設定が適用されます。

![幅を編集するオプションを持つ両面矢印。]({% image_buster /assets/img_archive/content_block_width_updated.png %}){: style="max-width:30%;" }

#### 自動IPウォーミングの使用 {#use-automated-ip-warming}

{% multi_lang_include release_type.md release="Early access" %}

[自動IPウォーミング]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming#automated-ip-warming)を使用して、毎日の送信量を徐々に増やし、受信トレイプロバイダーが送信パターンを学習し信頼できるようにします。Brazeは最もエンゲージメントの高いサブスクライバーに最初に送信し、ベストプラクティスに合ったペースで毎日のボリュームが増加します。

### パートナーシップ

#### LinkedIn – キャンバス Audience Sync {#linkedin-canvas-audience-sync}

[Braze Audience Sync to LinkedIn]({{site.baseurl}}/partners/canvas_audience_sync/linkedin_audience_sync)を使用すると、BrazeインテグレーションのユーザーデータをLinkedIn顧客リストに追加して、行動トリガー、セグメンテーションなどに基づいた広告を配信できます。通常、メッセージをトリガーするために使用する基準（プッシュ、メール、SMS、webhookなど）が、Brazeのキャンバスでユーザーデータに基づいて、LinkedIn顧客リストのそのユーザーに広告をトリガーできるようになりました。

#### Oracle Crowdtwist - データと分析 {#oracle-crowdtwist-data-analytics}

[Oracle Crowdtwist]({{site.baseurl}}/partners/crowdtwist)は、ブランドがパーソナライズされた顧客体験を提供できるようにする、主要なクラウドネイティブ顧客ロイヤルティソリューションです。100以上のエンゲージメントパスを提供し、マーケターが顧客のより完全なビューを開発するための迅速な価値実現を提供します。

#### Fullstory - ダイナミックコンテンツ {#fullstory-dynamic-content}

[Fullstory]({{site.baseurl}}/partners/fullstory)の行動データプラットフォームは、テクノロジーリーダーがより優れた、より情報に基づいた意思決定を行うのに役立ちます。デジタル行動データを分析スタックに注入することで、Fullstoryの特許取得済みテクノロジーは、行動データの質の力をスケールで解き放ち、すべてのデジタル訪問をアクション可能なインサイトに変換します。

#### Open Loyalty - データと分析 {#open-loyalty-data-analytics}

[Open Loyalty]({{site.baseurl}}/partners/openloyalty)は、顧客ロイヤルティおよびリワードプログラムを構築・管理できるクラウドベースのロイヤルティプログラムプラットフォームです。BrazeとOpen Loyaltyのインテグレーションは、ポイント残高、ティア変更、有効期限警告などのロイヤルティデータをリアルタイムでBrazeに直接同期します。これにより、ユーザーのロイヤルティステータスが変更されたときに、パーソナライズされたメッセージ（メール、プッシュ、SMS）をトリガーできます。

#### DOTS.ECO - エクステンション {#dotseco-extensions}

[DOTS.ECO]({{site.baseurl}}/partners/dots.eco)は、追跡可能なデジタル証明書を通じて、現実世界の環境影響でユーザーに報酬を与えることができます。各証明書には、共有可能な証明書URLや画像URLなどのメタデータを含めることができるため、ユーザーは影響の証明を表示（再訪問）できます。

#### Mailizio - メッセージオーケストレーション {#mailizio-message-orchestration}

[Mailizio]({{site.baseurl}}/partners/mailizio)は、直感的なビジュアルエディタを使用して再利用可能でブランドセーフなコンテンツを簡単にデザインできるメール作成・管理プラットフォームです。MailizioのBrazeへのインテグレーションにより、コンテンツブロックとメールテンプレートをエクスポートし、同じアセットからアプリ内メッセージを自動的に生成でき、迅速かつ完全にコントロールされたキャンペーン展開が可能になります。

### API {#apis}

#### メディアライブラリPOST API {#media-library-post-apis}

{% multi_lang_include release_type.md release="General availability" %}

メディアライブラリアセットをAPI経由で追加できるようになり、顧客、パートナー、代理店がメッセージ作成ワークフローをより自動化できるようになりました。[API]({{site.baseurl}}/api/endpoints/media_library/manage_assets/create)を使用して、アセットファイルを直接アップロードしたり、既存のURLからファイルをコピーしたりできます。この機能は、インテグレーションとオートメーション機能を解放します。

### Currentsとデータ共有

#### ストレージ送信先およびデータ共有のエージェントコンソールイベント {#agent-console-events-for-storage-destinations-and-datashare}

{% multi_lang_include release_type.md release="General availability" %}

2つの新しい[イベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events)が、ストレージ送信先（AWS S3、Google Cloud Storage、Azure Blob Storage）とSnowflakeデータ共有で利用可能になりました：`agentconsole.AgentExecuted`および`agentconsole.ToolInvocation`。これらのイベントにより、ダウンストリームシステムでエージェントコンソールの使用状況と詳細を分析でき、エージェントの使用状況を理解し最大限に活用するのに役立ちます。エージェントを使用すると、キャンバスやカタログでのコンテンツ生成、インテリジェントな意思決定に基づくユーザーの異なるパスへのルーティングなど、Braze全体で特定のタスクを実行できるインテリジェントエージェントを作成・デプロイできます。詳細については、[Currents変更ログ]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs#changes-in-version-5-release-date-2026-02-04)を参照してください。

#### 各チャネルの新しい「再試行」イベント {#new-retry-events-for-individual-channels}

{% multi_lang_include release_type.md release="General availability" %}

新しい[再試行イベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events)が、メール、LINE、プッシュ通知、SMS、webhook、およびWhatsAppチャネルで利用可能になりました。これらのイベントは、フリークエンシーキャップによってスケジュールされたメッセージがアボートされるのではなく遅延される場合の可視性を提供します。メッセージが優先度を下げられたりフリークエンシーキャップが適用されたりすると、設定された再試行ウィンドウ内で再試行できるようになり、メッセージ配信パターンとフリークエンシーキャップの影響についてより良いインサイトが得られます。詳細については、[Currents変更ログ]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs#changes-in-version-5-release-date-2026-02-04)を参照してください。

#### TokenStateChangeイベントに新しい`time_ms`フィールドを追加 {#add-new-time_ms-field-to-tokenstatechange-event}

{% multi_lang_include release_type.md release="General availability" %}

新しい`time_ms`フィールドが[`users.behaviors.pushnotification.TokenStateChange`]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events)イベントに追加され、プッシュトークンの状態変更をミリ秒レベルの粒度で追跡できるようになりました。この精度の向上により、同じ秒内に複数の変更が発生した場合のプッシュトークンの最新ステータスを理解でき、ダウンストリームシステムで正しいサブスクリプションステータスを持っていることに確信を持てます。詳細については、[Currents変更ログ]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs#changes-in-version-5-release-date-2026-02-04)を参照してください。

#### Tealium送信先への匿名ユーザーの送信 {#send-anonymous-user-to-tealium-destinations}

{% multi_lang_include release_type.md release="General availability" %}

外部ユーザーIDが定義されていないイベントを[Tealium]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/tealium/tealium_for_currents?redirected=1)送信先にストリーミングできるようになりました。Currentsインテグレーションで「匿名ユーザーのイベントを含める」チェックボックスを選択すると、外部ユーザーIDのないイベントが抑制されずに送信先に送信されます。この機能は、ダウンストリーム分析や、識別されていない匿名ユーザーを含むユースケースに不可欠です。

##### カスタムHTTP送信先への匿名ユーザーの送信 {#send-anonymous-user-to-customhttp-destinations}

{% multi_lang_include release_type.md release="Beta" %}

外部ユーザーIDが定義されていないイベントをカスタムHTTP送信先にストリーミングできるようになりました。Currentsインテグレーションで「匿名ユーザーのイベントを含める」チェックボックスを選択すると、外部ユーザーIDのないイベントが抑制されずに送信先に送信されます。この機能は、ダウンストリーム分析や、識別されていない匿名ユーザーを含むユースケースに不可欠です。

#### メールオープンイベント — 「machine_open」フィールド {#email-open-event-machine_open-field}

[メールオープンイベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#email-open-events)が「machine_open」フィールド値を生成するようになり、[_Machine Open_]({{site.baseurl}}/user_guide/analytics/reporting/report_metrics#machine-opens)指標をレポートできます。

### SDK

以下のSDK更新がリリースされました。Swift SDK v14.0.1はユニバーサルリンクの処理に関する問題を修正します。Android SDK v40.2.0は潜在的なメモリリークを修正し、透明なアクティビティが存在する場合に複数のセッションが開かれる問題を解決します。Expo SDK v3.2.0は、ユニバーサルリンクのネイティブSwift SDK処理を設定する`forwardUniversalLinks`オプション（デフォルト：false）を追加します。

#### SDKの破壊的更新

最新のSDK更新がリリースされました。破壊的更新はSDK更新セクションに記載されています。その他すべての更新は、対応するSDK変更ログをご確認ください。

{% multi_lang_include releases/sdk/2026_2_5_26_updates.md %}

{% enddetails %}