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
このページに記載されている更新の詳細については、アカウントマネージャーにお問い合わせいただくか、[サポートチケットを開封]({{site.baseurl}}/user_guide/administer/personal/braze_support/)してください。また、[SDK変更ログ]({{site.baseurl}}/developer_guide/changelogs/)では、毎月のSDKリリース、改良、および破壊的変更に関する詳細を確認することもできます。
{% endalert %}

{% details 2026年5月28日 %}

## 2026年5月28日リリース {#may-28-2026-release}

### データ＆レポート {#data-reporting}

#### プッシュパフォーマンスダッシュボード {#push-performance-dashboard}

[プッシュパフォーマンスダッシュボード]({{site.baseurl}}/user_guide/analytics/dashboards/channel_performance?tab=push%20performance#push-performance-dashboard)は、プッシュエンゲージメントのチャネルレベルの単一ビューを提供します。送信、バウンス、配信、直接・影響・合計の開封率を設定可能な時間ウィンドウで確認できます。個々のキャンペーンやCanvasesからデータを集計することなく、プッシュチャネル全体の健全性を把握するために使用します。

#### カタログセレクションのジオロケーションフィールド {#geolocation-fields-in-catalog-selections}

{% multi_lang_include release_type.md release="General availability" %}

カタログが、新しいジオロケーションフィールドタイプとカタログセレクション演算子による距離ベースのフィルタリングをサポートするようになりました。これにより、各ユーザーに最寄りのレストランを表示したり、不動産キャンペーンで50km以内の物件をフィルタリングしたり、特定のイベント近くの店舗をターゲットにしたりするなど、よりロケーションに関連したエクスペリエンスを作成できます。都市やリージョンコードで地理的ターゲティングを近似する代わりに、ユーザーの最新のロケーションなどのLiquidユーザー属性を含む中心点への近接度でカタログアイテムをフィルタリングできます。詳細については、[セレクション]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/#how-it-works)を参照してください。

#### レポートビルダーのバナーとRCS {#banner-and-rcs-for-report-builder}

[レポートビルダー]({{site.baseurl}}/report_builder/)がバナーをチャネルとして、RCSをSMSのサブカテゴリーとしてサポートするようになりました。これにより、他のすべてのBrazeチャネルと並べて、カスタムレポートで両方のパフォーマンスを直接測定できます。

#### `ecommerce.cart_updated`イベントアクション {#ecommercecart_updated-event-actions}

[`ecommerce.cart_updated`イベント]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/?tab=ecommerce.cart_updated#code-examples)が`replace`に加えて`add`および`remove`アクションをサポートするようになり、更新のたびにカート全体のスナップショットを送信する代わりに、増分的なカート変更を送信できます。

### BrazeAI<sup>TM</sup>

#### SMS、MMS、RCSメッセージ向けコンテンツオプティマイザー {#content-optimizer-for-sms-mms-and-rcs-messages}

{% multi_lang_include release_type.md release="Beta" %}

[コンテンツオプティマイザー]({{site.baseurl}}/user_guide/brazeai/content_optimizer/)を使用して、SMS、MMS、RCSメッセージのフック、本文、CTAを最適化できます。コンテンツオプティマイザーは、AIを使用して大量のコンテンツバリアントを自動的に生成・評価し、メッセージコンテンツを大規模にテスト・最適化するのに役立つエージェントです。

### オーケストレーション {#orchestration}

#### ワークスペースのタイムゾーン {#workspace-time-zones}

{% multi_lang_include release_type.md release="General availability" %}

[ワークスペースのタイムゾーン]({{site.baseurl}}/user_guide/administer/global/admin_settings/workspace_time_zone/)を使用して、個々のワークスペースに特定のタイムゾーンを定義できます。これにより、スケジュールされたCampaignsやCanvases（ローカルタイムやインテリジェントタイミングを使用しないもの）が、全体的な会社のタイムゾーンではなく、ワークスペースの指定されたタイムゾーンに従って送信されます。

メッセージ送信のワークスペースタイムゾーンは段階的に展開されているため、ダッシュボードにこれらの設定がまだ表示されない場合があります。

### チャネルとタッチポイント {#channels-touchpoints}

#### WhatsApp `inbound_profile_name`

Metaの受信メッセージングwebhookからユーザーのWhatsApp表示名を自動的にキャプチャし、ユーザーのBrazeプロファイルに書き込むことができます。受信WhatsAppメッセージを受信すると、Brazeはプロファイル名を新しいWhatsApp Liquid属性[{% raw %}`{{whats_app.${inbound_profile_name}}}`{% endraw %}]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags/)として公開します。これをCanvasのユーザー更新ステップで参照して、プロファイルフィールドに保存できます。

#### 孤立したSMSサブスクリプション状態 {#orphaned-sms-subscription-states}

Brazeは[孤立したサブスクリプション状態レコードを自動的に管理]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups/#how-braze-handles-orphaned-subscription-states)します（ユーザープロファイルに紐付けられていない電話番号やメールアドレスに保存されたサブスクリプションデータ）。これにより、意図しないサブスクリプション状態の継承を防止します。新しく作成されたユーザープロファイルが、以前に削除された、または無関係なユーザーからサブスクリプション状態を誤って継承するシナリオからユーザーを保護します。

### パートナーシップ {#partnerships}

#### Chord - 顧客データプラットフォーム {#chord-customer-data-platform}

[Chord](https://www.chord.co/)は、eコマースストアフロントからイベントをキャプチャし標準化する顧客データプラットフォームを提供します。ChordをBrazeに接続すると、購入アクティビティ、行動イベント、アイデンティティの更新がBrazeに流れ込み、パイプラインを自分で構築することなく、キャンペーンをトリガーしてプロファイルを最新の状態に保つことができます。

詳細については、[Chord]({{site.baseurl}}/partners/chord/)を参照してください。

#### Better Email - テンプレート {#better-email-templates}

[Better Email](https://www.betteremail.dev)は、メールデザインシステムを中心に構築されたコラボレーティブなメール作成プラットフォームです。チームは、ブロックとスタイルの共有システムから本番対応のメールをデザイン、管理、エクスポートでき、開発者やエージェンシーに依存することなく、大規模にブランドの一貫性を確保できます。

詳細については、[Better Email]({{site.baseurl}}/partners/better_email/)を参照してください。

#### DailyPlay - ダイナミックコンテンツ {#dailyplay-dynamic-content}

[DailyPlay](https://dailyplay.ai/)はゲーミフィケーションプラットフォームです。パーソナライズされたブランドゲームと組み込みのリワードシステムを起動して、エンゲージメントを深め、リテンションを向上させるために使用します。

詳細については、[DailyPlay]({{site.baseurl}}/partners/dailyplay/)を参照してください。

### SDK

#### SDKの破壊的更新 {#sdk-breaking-updates}

以下のSDK更新がリリースされました。破壊的更新は下記のとおりです。その他すべての更新は、対応するSDK変更ログをご確認ください。

- [Flutter SDK 19.0.0](https://pub.dev/packages/braze_plugin/changelog#1900)
    - サポートされるDartの最小バージョンは`2.17.0`です。
    - SDKログがDartレイヤーで制御されるようになりました。
    - ネイティブSDKバインディングを更新。ネイティブAndroidブリッジを[Braze Android SDK 41.1.1から42.2.0に](https://github.com/braze-inc/braze-android-sdk/compare/v41.1.1...v42.2.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)更新。
    - クラッシュを修正。
- [Cordova 16.0.1](https://github.com/braze-inc/braze-cordova-sdk/releases/tag/16.0.1)
    - `cordova-ios` 8と`SwiftDelegate`テンプレートを使用する際のiOS初期化を修正。
- [Unity SDK 11.0.0](https://github.com/braze-inc/braze-unity-sdk/blob/master/CHANGELOG.md)
    - ネイティブSDKバインディングを更新。ネイティブiOSブリッジをBraze [Swift SDK 13.2.0から14.1.0に](https://github.com/braze-inc/braze-swift-sdk/compare/13.2.0...14.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)更新。
    - ネイティブAndroidブリッジを[Braze Android SDK 36.0.0から42.2.0に](https://github.com/braze-inc/braze-android-sdk/compare/v36.0.0...v42.2.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)更新。
        - 最小限必要なAndroid SDKバージョンは23です。詳細については、[Braze Android SDKバージョン情報](https://github.com/braze-inc/braze-android-sdk?tab=readme-ov-file#version-information)を参照してください。
    - 最小限必要なUnityバージョンをUnity 6（[6000.0.66f2](https://unity.com/releases/editor/whats-new/6000.0.66f2)以降）に更新。
    - News Feedを削除。
        - `RequestFeedRefresh()`、`RequestFeedRefreshFromCache()`、`LogFeedDisplayed()`、`LogCardImpression(string)`、`LogCardClicked(string)`を削除。
    - 軽微なバグを修正。
- [React Native 20.1.0](https://github.com/braze-inc/braze-react-native-sdk/releases/tag/20.1.0)
    - Android SDKバインディングを更新。
    - プッシュ通知のディープリンクの問題を修正。
- [Segment Swift 8.0.0](https://github.com/braze-inc/braze-segment-swift/blob/main/CHANGELOG.md#800)
    - `14.0.0+` SemVer仕様のリリースを必要とするようにBraze Swift SDKバインディングを更新。
        - これにより、Braze SDKの`14.0.0`から`15.0.0`（含まない）までのあらゆるバージョンとの互換性が確保されます。
        - 潜在的な破壊的変更の詳細については、[`14.0.0`の変更ログエントリ](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1400)を参照してください。
    - SDK認証のサポートを追加。

{% enddetails %}
{% details 2026年4月30日 %}

## 2026年4月30日リリース {#april-30-2026-release}

### データ＆レポート

#### 個別プロファイル作成のためのクイックユーザー追加 {#quick-user-add-for-individual-profile-creation}

{% multi_lang_include release_type.md release="General availability" %}

**ユーザーをインポート**から**クイックユーザー追加**を選択し、メールアドレスまたはexternal IDを入力することで、個別のユーザープロファイルを作成できるようになりました。

以前は、このワークフローからユーザーを作成するにはCSVアップロードまたは自動取り込み方法が必要でした。

詳細については、[CSVインポート]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import/)を参照してください。

#### ゼロコピーCDI同期によるCanvasトリガー {#zero-copy-cdi-syncs-for-canvas-triggers}

{% multi_lang_include release_type.md release="General availability" %}

CDIがゼロコピーパーソナライゼーション用の`Canvas triggers`データタイプをサポートするようになりました。ウェアハウスまたはS3データからCanvasをトリガーし、Brazeユーザープロファイルにフィールドを保持せずにコンテキストフィールドを渡すことができます。

以前は、CDI同期ではこのタイプのパーソナライゼーションワークフローのためにデータをBrazeプロファイルに書き込む必要がありました。

詳細については、[CDIを使用したゼロコピーパーソナライゼーション]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/zero_copy_sync/)を参照してください。

#### eコマース推奨イベント {#ecommerce-recommended-events}

{% multi_lang_include release_type.md release="General availability" %}

[eコマース推奨イベント]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/)は、購入ジャーニーの6つのステップをカバーします：`product_viewed`、`cart_updated`、`checkout_started`、`order_placed`、`order_cancelled`、`order_refunded`。これらのイベントを正常に送信すると、Brazeはデータを検証し、拡大するプラットフォーム機能のセットで利用可能にします。

### Currentsとデータ共有 {#currents-and-datashare}

#### 新しいバナーおよびWhatsApp Currents更新 {#new-banner-and-whatsapp-currents-updates}

{% multi_lang_include release_type.md release="General availability" %}

Currentsとデータ共有に、新しい`Banner.Dismiss`イベントと既存のWhatsAppイベントの追加フィールドが含まれるようになりました。

以前は、これらのバナー却下イベントとWhatsAppフィールドはエクスポートデータで利用できませんでした。

詳細については、[Currents変更ログ]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs/)を参照してください。

### オーケストレーション

#### 多言語翻訳 {#multi-language-translations}

{% multi_lang_include release_type.md release="General availability" %}

複雑なコードを必要としないワンタイムのロケール設定で[多言語メッセージ]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages/)を作成し、すべての市場に自信を持って送信できます。

#### きめ細かな権限の移行 {#granular-permissions-migration}

{% multi_lang_include release_type.md release="General availability" %}

アカウントにアクセスし特定のアクションを実行できるユーザーを管理することは、セキュリティと運用効率の両方にとって重要です。より多くのコントロールを提供するために、Brazeはアカウント全体でユーザーアクセスを管理するためのより柔軟で正確な方法である[きめ細かな権限]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/granular_permissions_migration/)を導入しています。

#### 送信先Canvasコンポーネント {#send-to-destination-canvas-component}

{% multi_lang_include release_type.md release="General availability" %}

[送信先ステップ]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/send_to_destination/)を使用すると、あるCanvasから別のCanvasにユーザーを送信できます。たとえば、プロモーションオファーのメッセージングを共有する2つのCanvasがある場合、送信先を使用してこれらのCanvasを接続できます。

#### Canvasコンテキストの機能強化 {#canvas-context-enhancements}

{% multi_lang_include release_type.md release="General availability" %}

Canvasで、コンテキスト変数を参照して以下を設定できるようになりました。

- Content Cardsの削除イベント
- Content Cardsの有効期限

詳細については、[カード作成]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card/card_creation/?tab=canvas)を参照してください。

#### メッセージステップの配信バリデーション進行動作 {#delivery-validation-advancement-behavior-for-message-steps}

{% multi_lang_include release_type.md release="General availability" %}

[配信バリデーション]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step/#delivery-validations)は、メッセージ送信時にオーディエンスが配信基準を満たしていることを確認するための追加チェックを提供します。ユーザーがメッセージステップの設定された配信バリデーションを満たさない場合、**配信バリデーション進行動作**設定を使用して、ユーザーが次のステップに進むかCanvasを退出するかを決定できます。

#### ワークスペースメッセージングレート制限 {#workspace-messaging-rate-limits}

{% multi_lang_include release_type.md release="General availability" %}

[ワークスペースメッセージングレート制限]({{site.baseurl}}/user_guide/administer/global/workspace_settings/messaging_rate_limits/)を使用して、プラットフォームからの送信メッセージの配信レートを調整し、ユーザーが必要なメッセージを確実に受信できるようにします。ワークスペースメッセージングレート制限は段階的に展開されているため、ダッシュボードにこれらの設定がまだ表示されない場合があります。

### チャネルとタッチポイント

#### WhatsAppテンプレートビルダー {#whatsapp-template-builder}

{% multi_lang_include release_type.md release="Early access" %}

[WhatsAppテンプレートビルダー]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/)を使用すると、BrazeとMeta Business Managerを切り替えることなく、Braze内で直接WhatsAppメッセージテンプレートを作成・送信できます。Metaがテンプレートを承認した後、必要な数のCampaignsやCanvasesで使用できます。

#### Shopify製品タグ、メタフィールド、コレクション {#shopify-product-tags-metafields-and-collections}

{% multi_lang_include release_type.md release="General availability" %}

Shopifyストアから[Shopify製品タグ、コレクション、メタフィールドをBrazeカタログに同期]({{site.baseurl}}/partners/ecommerce/shopify/shopify_catalogs/)できるようになりました。これにより、カスタムの回避策なしで、パーソナライゼーション、セグメンテーション、カタログベースのメッセージングのためのより豊富な製品データが提供されます。

### パートナーシップ

#### GRAVITY - データと分析 - ロイヤルティ {#gravity-data-and-analytics-loyalty}

{% multi_lang_include release_type.md release="General availability" %}

[GRAVTY®](https://www.lji.io/)は、Loyalty Juggernaut Inc.（LJI）のエンタープライズグレードのロイヤルティプラットフォームで、小売、旅行、レストラン（クイックサービスレストランを含む）、金融サービスのブランドが次世代プログラムを設計、管理、スケールできるようにし、パーソナライズされたデータ主導のエクスペリエンスを通じて、エンゲージメント、リテンション、顧客生涯価値の測定可能な成長を促進します。

<!-- Use this section to list any new SDKs or SDK updates that are already released. -->
### SDK

以下のSDK更新がリリースされました。詳細については、[SDK変更ログ]({{site.baseurl}}/releases/sdk_changelogs/)を参照してください。

#### SDKの破壊的更新

{% multi_lang_include release_type.md release="General availability" %}

以下のSDK更新がリリースされました。破壊的更新は下記のとおりです。その他すべての更新は、対応するSDK変更ログをご確認ください。

- [React Native SDK 19.2.0](https://github.com/braze-inc/braze-react-native-sdk/releases/tag/19.2.0)
    - 遅延初期化サポート。
- [Android SDK 42.0.0](https://github.com/braze-inc/braze-android-sdk/releases/tag/v42.0.0)
    - アプリ内メッセージとバナーのバグ修正。
- [Swift SDK 14.1.0](https://github.com/braze-inc/braze-swift-sdk/releases/tag/14.1.0)
    - バナー却下サポート。
- [Web SDK 6.7.0](https://github.com/braze-inc/braze-web-sdk/releases/tag/v6.7.0)
    - バナー却下サポート。
- [Android SDK 42.1.0](https://github.com/braze-inc/braze-android-sdk/releases/tag/v42.1.0)
    - バナー却下サポート。
- [Braze Segment Android 17.0.0](https://github.com/braze-inc/braze-segment-android/releases/tag/v17.0.0)
    - これはBraze Segment Androidプラグインの最終リリースです。Analytics-Androidを使用しており、2026年3月にサポート終了となりました。[Analytics-Kotlin](https://github.com/segmentio/analytics-kotlin)を使用する[Braze Segment Kotlinプラグイン](https://github.com/braze-inc/braze-segment-kotlin)に移行してください。
    - ネイティブSDKバージョンをアップグレード。

{% enddetails %}
{% details 2026年4月2日 %}

## 2026年4月2日リリース {#april-2-2026-release}

### データ＆レポート

#### Currentsおよびデータ共有イベントの新しいバナーチャネルフィールド {#new-banner-channel-fields-in-currents-and-datashare-events}

Brazeは、Currentsおよびデータ共有エクスポートの既存のバナーチャネルイベントにフィールドを追加しました。これらのイベントおよびフィールドの更新一覧については、[バージョン7の変更点]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs/#changes-for-storage)を参照してください。

#### CurrentsのMixpanel EUおよびインドデータセンターサポート {#mixpanel-eu-and-india-data-center-support-for-currents}

Currents Mixpanelインテグレーションが、MixpanelのEUおよびインドデータセンターをサポートするようになりました。Mixpanelインテグレーションを設定する際に、BrazeがデータをどのMixpanelリージョンに送信するかを選択できます。この更新は、相互顧客向けのMixpanelの国際的な拡大をサポートします。詳細については、[Mixpanel]({{site.baseurl}}/partners/data_and_analytics/analytics/mixpanel/)を参照してください。

#### 再利用可能なクラウドデータ取り込み（CDI）ソースと同期 {#reusable-cloud-data-ingestion-cdi-sources-and-syncs}

{% multi_lang_include release_type.md release="Early access" %}

クラウドデータ取り込み（CDI）に、ソースと同期を分離する新しいデザインが導入され、1つのソースを複数の同期で再利用できるようになりました。既存の同期は、ダウンタイムなしで新しいソースと同期モデルに自動的に移行されます。**クラウドデータ取り込み** > **ソース**に移動して、ソースの表示、編集、作成を行い、同期を作成する際にドロップダウンからソースを選択します。この変更により、繰り返しのセットアップが削減され、将来の機能強化の基盤が構築されます。詳細については、[データウェアハウスインテグレーションの設定]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/#setting-up-data-warehouse-integrations)を参照してください。

### BrazeAI<sup>TM</sup>

#### BrazeAI Operator<sup>TM</sup>からサポートチケットを提出 {#file-support-tickets-from-brazeai-operatortm}

{% multi_lang_include release_type.md release="General availability" %}

[BrazeAI Operator]({{site.baseurl}}/user_guide/brazeai/operator/)に、ダッシュボードを離れずにBrazeサポートチケットを提出するフローが追加されました。手順、自動的に含まれるコンテキスト、および迅速な解決のためのヒントについては、[BrazeAI Operatorでサポートチケットを提出]({{site.baseurl}}/user_guide/brazeai/operator/support_tickets/)を参照してください。

### オーケストレーション

#### 多言語翻訳

{% multi_lang_include release_type.md release="General availability" %}

ワークスペースにロケールを追加した後、[多言語翻訳]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/)を使用して、1つのプッシュ、メール、バナー、アプリ内メッセージ、またはContent Block内で異なる言語のユーザーをターゲットにできます。

![ロケールプレビュー]({% image_buster /assets/img/multi-language_support/multi_language_user_preview.png %}){: style="max-width:70%;"}

#### Canvasコンテキストの機能強化

{% multi_lang_include release_type.md release="General availability" %}

Canvasで、コンテキスト変数を参照して以下を設定できるようになりました。

- メッセージステップのバナーおよびアプリ内メッセージの[有効期限]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/#set-an-expiration)
- アクションパスステップの[パーソナライズされた遅延]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/#action-path-delays)

コンテキスト変数名フィールドでは、コンテキスト変数名を入力するか、ステップエディタのドロップダウンから選択することもできます。詳細については、[コンテキスト]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/)および[コンテキスト変数]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/)を参照してください。

### チャネルとタッチポイント

#### KakaoTalk

{% multi_lang_include release_type.md release="General availability" %}

[KakaoTalk]({{site.baseurl}}/kakaotalk/)は、ブロードキャストメッセージングおよびユーザーとの1:1チャットを可能にするメッセージングチャネルです。Liquidやその他のダイナミックコンテンツを使用してパーソナライズされたユーザーエクスペリエンスを作成し、ブランドとの豊かなユーザーエクスペリエンスを育成・強化する環境を構築します。

![KakaoTalkリストアイテムメッセージ。]({% image_buster /assets/img/kakaotalk/wide_image.png %}){: style="max-width:70%;"}

#### Canvasのバナー {#banners-in-canvas}

{% multi_lang_include release_type.md release="General availability" %}

Canvasの[メッセージステップ]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/)のメッセージングチャネルとして[バナー]({{site.baseurl}}/user_guide/message_building_by_channel/banners/)を使用できます。バナーを使用すると、リアルタイムのユーザー適格性と動作を反映して、アプリやWebサイトのコンテンツを動的にパーソナライズできます。

### パートナーシップ

#### CataBoom - メッセージパーソナライゼーション - ビジュアルとインタラクティブコンテンツ {#cataboom-message-personalization-visual-and-interactive-content}

[CataBoom]({{site.baseurl}}/partners/cataboom/)はゲーミフィケーションプラットフォームです。ブランドはこれを使用して、スピン・トゥ・ウィンゲーム、クイズ、インスタントウィンゲームなどのインタラクティブなデジタルエクスペリエンスを構築・起動します。これらのエクスペリエンスはエンゲージメントを深め、ファーストパーティデータを収集します。

#### Denada - メッセージオーケストレーション - テンプレート {#denada-message-orchestration-templates}

[Denada]({{site.baseurl}}/partners/denada/)は、AIを活用したマーケティングクリエイティブプラットフォームで、専門家が自然な会話を通じてオンブランドのマーケティング素材を作成できます。Denadaを使用すると、チームはデザインの専門知識がなくても、アイデアから完成したメールコンテンツまで進めることができます。

#### Poq - eコマース - モバイルアプリプラットフォーム {#poq-ecommerce-mobile-app-platform}

[Poq]({{site.baseurl}}/partners/poq/)は、エンタープライズビジネスがフルネイティブのiOSおよびAndroidアプリを迅速に起動、管理、スケールできるようにし、コマースを推進しブランドの約束を実現する高パフォーマンスのモバイルエクスペリエンスを提供します。

#### The Trade Desk – Canvas Audience Sync

[Braze Audience Sync to The Trade Desk]({{site.baseurl}}/partners/canvas_audience_sync/trade_desk_audience_sync/)を使用すると、ファーストパーティのユーザーデータをBrazeからThe Trade Deskに動的に同期して、広告リターゲティング、類似モデリング、抑制に活用できます。

### SDK

#### 統合開発環境（IDE）をDocs MCPに接続 {#connect-your-integrated-development-environment-ide-to-the-docs-mcp}

AIコーディングアシスタントを使用して、統合開発環境（IDE）をContext7経由でBraze Docs MCPに接続することで、Brazeインテグレーションワークフローを加速できます。これにより、アシスタントが最新のBrazeドキュメントに直接アクセスでき、開発環境でより正確なSDKガイダンス、コード例、トラブルシューティングヘルプを生成できます。Cursor、Claude Desktop、VS Codeでのセットアップ手順については、[LLMを使用した構築]({{site.baseurl}}/developer_guide/getting_started/build_with_llm/#connecting-to-the-braze-docs-mcp)を参照してください。

#### SDKの破壊的更新

以下のSDK更新がリリースされました。破壊的更新は下記のとおりです。その他すべての更新は、対応するSDK変更ログをご確認ください。

- [Cordova 15.0.0](https://github.com/braze-inc/braze-cordova-sdk/releases/tag/15.0.0)
    - ネイティブAndroidブリッジを[Braze Android SDK 39.0.0から41.1.1に](https://github.com/braze-inc/braze-android-sdk/compare/v39.0.0...v41.1.1#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)更新。
    - ネイティブiOSブリッジを[Braze Swift SDK 13.2.0から14.0.1に](https://github.com/braze-inc/braze-swift-sdk/compare/13.2.0...14.0.1#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)更新。
    - 成功コールバックに関する`subscribeToInAppMessage`の問題を修正。
- [Roku SDK 2.2.1](https://github.com/braze-inc/braze-roku-sdk/releases/tag/v2.2.1)
    - デバイスの接続が断続的またはない場合に、テンプレート化されたアプリ内メッセージの失敗したHTTPリクエストを処理する際のクラッシュを修正。
- [Web SDK 6.6.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md#660)
    - デフォルトの400日からCookieの有効期間を設定する`cookieExpiryInDays`初期化オプションを追加。
- [Flutter SDK 18.0.0](https://pub.dev/packages/braze_plugin/changelog#1800)
    - 遅延初期化サポートを追加。
    - iOSインテグレーションプロセスを合理化し、Content Cards、バナー、フィーチャーフラグ、アプリ内メッセージ、またはプッシュ通知の更新をネイティブSDKから転送するためのネイティブコードの記述が不要に。
        - SDKは、Brazeインスタンスが作成されたときにこれらのサブスクリプションを自動的に設定するようになりました。
        - これはAndroidの既存の動作と一致します。
        - 移行するには、`AppDelegate`内の`braze.contentCards.subscribeToUpdates()`、`braze.banners.subscribeToUpdates()`、`braze.notifications.subscribeToUpdates`、`braze.featureFlags.subscribeToUpdates`、および`braze.inAppMessagePresenter`への手動呼び出しを削除してください。
        - デフォルトでは、アプリ内メッセージが表示されます。これをオーバーライドするには、`BrazePlugin.configure(_:postInitialization:)`の`postInitialization`クロージャを使用してカスタムアプリ内メッセージプレゼンターを設定してください。
- [Swift SDK 14.0.4](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1404)
    - SDKの再初期化時のプッシュオートメーションに関するバグを修正。
    - Push Storiesで無効な画像がフィルタリングされない問題を修正。
- [Swift SDK 14.0.3](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1403)

{% enddetails %}

{% details 2026年3月5日 %}

## 2026年3月5日リリース {#march-5-2026-release}

### データ＆レポート

#### 新しいデータセンター {#new-data-center}

{% multi_lang_include release_type.md release="General availability" %}

Brazeは新しい[データセンター]({{site.baseurl}}/user_guide/data/infrastructure/data_centers/)を開設しました：JP-01。Brazeアカウントの設定時にリージョン固有のデータセンターにサインアップできます。

#### コンテキスト変数 {#context-variables}

{% multi_lang_include release_type.md release="General availability" %}

[コンテキスト変数]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context/)は、特定のCanvas内でのユーザーのジャーニー中に作成・使用できる一時的なデータです。ユーザーがCanvasに入るたびに（以前に入ったことがある場合でも）、コンテキスト変数は最新のエントリデータとCanvas設定に基づいて再定義されます。このアプローチにより、各Canvasエントリが独自の独立したコンテキストを維持でき、ユーザーは各状態の特定のコンテキストを保持しながら、同じジャーニー内で複数のアクティブな状態を持つことができます。

#### クラウドデータ取り込みソース {#cloud-data-ingestion-sources}

{% multi_lang_include release_type.md release="Early access" %}

[クラウドデータ取り込み]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/file_storage_integrations/#setting-up-cloud-data-ingestion-in-braze)に、ソースと同期を分離する新しいUIが導入され、1つのソースを任意の数の同期で再利用できるようになりました。これにより、重複する設定が削減され、複数の同期がある場合のセットアップが簡素化されます。既存の同期がある場合、ダウンタイムなしで新しいソースと同期の構造に自動的に移行されます。開始するには、**クラウドデータ取り込み** > **ソース**に移動して、ソースの表示、編集、作成を行い、同期を作成する際にドロップダウンからソースを選択します。

#### Currentsおよびデータ共有イベントの追加フィールド {#additional-fields-for-currents-and-data-share-events}

{% multi_lang_include release_type.md release="General availability" %}

[Currentsおよびデータ共有イベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs/#changes-in-version-5-release-date-2026-02-04)に、分析およびダウンストリームシステムで利用可能なデータを深めるための以下の新しいフィールドが追加されました。

- `agentconsole.AgentExecuted`：`error`（文字列）を追加—発生したエラーの説明。
- `agentconsole.ToolInvocation`：`request_id`（文字列）を追加—全体的なLLMリクエストと完全な実行のための一意のID。
- `users.messages.rcs.InboundReceive`：`canvas_variation_name`（文字列）を追加—ユーザーが受け取ったCanvasバリエーションの名前。

#### SnowflakeデータシェアのCampaignおよびCanvasフィールド {#campaign-and-canvas-fields-for-snowflake-data-share}

{% multi_lang_include release_type.md release="General availability" %}

[Snowflakeデータシェア]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs/#changes-for-data-sharing-3)に、66の既存テーブルにわたるCampaignおよびCanvas情報を反映する追加フィールドが含まれるようになりました。

- `campaign_name`
- `canvas_name`
- `canvas_step_name`
- `canvas_variation_name`
- `message_variation_name`
- `conversion_behavior`
- `experiment_split_name`

#### CSVプレインポートバリデーションとエラーレポート {#csv-pre-import-validation-and-error-reporting}

{% multi_lang_include release_type.md release="General availability" %}

[CSVユーザーインポート]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/)で、プレインポートバリデーションと詳細なエラーレポートがサポートされるようになりました。インポート前に、**ユーザーをインポート**ページで**インポート前にファイルを検証**を選択すると、Brazeがファイルをスキャンし、完全に失敗する行（エラー）と一部の値がスキップされて成功する行（警告）を特定するレポートを生成します。レポートをダウンロードしてCSVを修正して再アップロードするか、そのまま続行できます。インポート完了後、失敗した行のダウンロード可能なレポートも利用でき、各問題の正確な理由が記載されています。

#### メッセージング診断ダッシュボード {#messaging-diagnostics-dashboard}

{% multi_lang_include release_type.md release="Early access" %}

[メッセージング診断ダッシュボード]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/diagnostics_dashboard/)は、メッセージ送信結果の概要を提供し、トレンドを把握してメッセージング設定の潜在的な問題を診断できます。このダッシュボードは、CampaignsやCanvasesからのメッセージが期待どおりに送信されなかった理由を理解するのに役立ちます。

### BrazeAI<sup>TM</sup>

#### エージェントコンソールのBrazeエージェント {#braze-agents-in-agent-console}

{% multi_lang_include release_type.md release="General availability" %}

[Brazeエージェント]({{site.baseurl}}/user_guide/brazeai/agents/)は、Braze内で作成できるAIパワーのヘルパーです。エージェントは、コンテンツを生成し、インテリジェントな決定を行い、データを拡張して、よりパーソナライズされたカスタマーエクスペリエンスを提供できます。エージェントを作成する際に、その目的を定義し、動作のガードレールを設定します。ライブになった後、エージェントはBrazeに[デプロイ]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents/)して、パーソナライズされたコピーの生成、リアルタイムの意思決定、またはカタログフィールドの更新を行うことができます。

### オーケストレーション

#### きめ細かなユーザー権限 {#granular-user-permissions}

{% multi_lang_include release_type.md release="Early access" %}

Brazeは、ユーザーアクセスを管理するためのより柔軟な方法である[きめ細かな権限]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/)を導入しています。レガシー権限がきめ細かな権限にどのようにマッピングされるかを含む移行プロセスについては、[きめ細かな権限への移行]({{site.baseurl}}/granular_permissions_migration/)を参照してください。

#### チャネルベースのレート制限 {#channel-based-rate-limiting}

{% multi_lang_include release_type.md release="General availability" %}

マルチチャネルのCampaignまたはCanvasの配信速度レート制限を設定する際に、共有レート制限または[チャネルベースの制限]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/#multichannel-campaigns-and-canvases)のいずれかを設定できます。マルチチャネルのCampaignまたはCanvasがチャネルベースのレート制限を使用する場合、レート制限は選択した各チャネルに適用されます。たとえば、CampaignまたはCanvasを設定して、CampaignまたはCanvas全体で1分あたり最大5,000件のwebhookと2,500件のSMSメッセージを送信できます。

#### Canvasコンテキストステップ {#canvas-context-step}

{% multi_lang_include release_type.md release="General availability" %}

[Canvasコンテキストステップ]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context/)を使用すると、ユーザーがCanvas内を移動する際に1つ以上の変数を作成・更新できます。たとえば、季節割引を管理するCanvasがある場合、コンテキスト変数を使用して、ユーザーがCanvasに入るたびに異なる割引コードを保存できます。

### チャネルとタッチポイント

#### Content Blocksでのロケール翻訳 {#translate-locales-in-content-blocks}

{% multi_lang_include release_type.md release="Early access" %}

ワークスペースにロケールを追加した後、Content Block内で[異なる言語のユーザーをターゲット]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages/)にできます。

### パートナーシップ

#### Algolia - 検索レコメンデーション {#algolia-search-recommendations}

[Algolia]({{site.baseurl}}/partners/ecommerce/product_search_recommendations/algolia/)は、開発者が高速で関連性が高くスケーラブルな検索エクスペリエンスを構築するのに役立つ検索・ディスカバリープラットフォームです。強力なAPIファーストアプローチにより、Algoliaは高度なランキングアルゴリズムとAI駆動のインサイトを組み合わせて、シームレスなサイト検索、ナビゲーション、パーソナライズされたコンテンツディスカバリーを実現します。

#### Anthropic - AIモデルプロバイダー {#anthropic-ai-model-provider}

[Anthropic]({{site.baseurl}}/partners/ai_model_providers/anthropic/)は、AIの安全性と研究に取り組む企業で、幅広い言語タスクに対して有用で、正直で、安全な次世代AIアシスタントClaudeを開発しています。

#### Canva - メッセージパーソナライゼーション - クリエイティブスタジオ {#canva-message-personalization-creative-studio}

[Canva]({{site.baseurl}}/partners/canva/)は、Canva内の画像をBrazeメディアライブラリに直接同期し、クリエイティブワークフローを合理化し、すべてのメッセージングチャネルでビジュアルアセットを最新の状態に保ちます。

#### DOTS.ECO - リワード {#dotseco-rewards}

[DOTS.ECO]({{site.baseurl}}/partners/additional_channels_and_extensions/extensions/rewards/dots_eco/)は、追跡可能なデジタル証明書を通じて、現実世界の環境影響でユーザーに報酬を与えることができます。各証明書には、共有可能な証明書URLや画像URLなどのメタデータを含めることができるため、ユーザーは影響の証明を表示（再訪問）できます。

#### Figma - メッセージパーソナライゼーション - クリエイティブスタジオ {#figma-message-personalization-creative-studio}

[Figma]({{site.baseurl}}/partners/figma/)は、製品の構築、デザイン、プロトタイプ作成を可能にするコラボレーティブデザインプラットフォームです。このインテグレーションを使用して、FigmaからBrazeメディアライブラリに画像やビジュアルアセットを直接送信できます。

#### Flybuy - メッセージパーソナライゼーション - ロケーション {#flybuy-message-personalization-location}

Radius Networksの[Flybuy]({{site.baseurl}}/partners/message_personalization/location/flybuy/)は、AIパワーのテクノロジーを活用して、ピックアップ、デリバリー、ドライブスルー、ダインインのサービス速度を最適化する、主要なオムニチャネルロケーションプラットフォームです。統合されたMarketing Suiteを通じて、Flybuyはブランドがハイパーターゲットのモーメントベースのメッセージを配信し、エンゲージメントの促進、チェックサイズの増加、より広範なロイヤルティイニシアチブのサポートを支援します。

#### Google Gemini - AIモデルプロバイダー {#google-gemini-ai-model-provider}

[Google Gemini]({{site.baseurl}}/partners/ai_model_providers/google_gemini/)は、テキスト、コード、画像にわたる高度な推論を組み合わせたGoogleのAIモデルファミリーで、ブランドがよりスマートでパーソナライズされたエクスペリエンスを提供するのに役立ちます。

#### Limbik - メッセージパーソナライゼーション - パーソナライゼーションエンジン {#limbik-message-personalization-personalization-engines}

[Limbik]({{site.baseurl}}/partners/message_personalization/dynamic_content/personalization_engines/limbik/)は、AIレゾナンスレイヤーです。実際のオーディエンスがメッセージ、コンセプト、AI出力をどのように解釈し、反応するかを、市場に届く前に予測します。60以上の国と25以上の言語にわたる継続的な一次調査に基づき、Limbikは人間が検証した合成オーディエンス（マシンスピードでリサーチグレードの精度（95%信頼度、1.5%〜3%の誤差範囲）で実際のオーディエンスの反応をシミュレートするデジタル集団）を提供します。Limbikは、メッセージングがターゲットオーディエンスの信念や感情と共鳴することを即座に確認する能力を提供します。

#### Linkrunner - メッセージオーケストレーション - アトリビューション {#linkrunner-message-orchestration-attribution}

[Linkrunner]({{site.baseurl}}/partners/message_orchestration/attribution/linkrunner/)は、ユーザー獲得キャンペーンの追跡と分析に役立つモバイルアトリビューションおよび分析プラットフォームです。

#### Mailizio - メッセージオーケストレーション - テンプレート {#mailizio-message-orchestration-templates}

[Mailizio]({{site.baseurl}}/partners/message_orchestration/templates/Mailizio/)は、直感的なビジュアルエディタを使用して再利用可能でブランドセーフなコンテンツを簡単にデザインできるメール作成・管理プラットフォームです。MailizioのBrazeへのインテグレーションにより、コンテンツブロックとメールテンプレートをエクスポートし、同じアセットからアプリ内メッセージを自動的に生成でき、迅速かつ完全にコントロールされたキャンペーン展開が可能になります。

#### Open Loyalty - データと分析 - ロイヤルティ {#open-loyalty-data-and-analytics-loyalty}

[Open Loyalty]({{site.baseurl}}/partners/data_and_analytics/loyalty/openloyalty/)は、顧客ロイヤルティおよびリワードプログラムを構築・管理できるクラウドベースのロイヤルティプログラムプラットフォームです。BrazeとOpen Loyaltyのインテグレーションは、ポイント残高、ティア変更、有効期限警告などのロイヤルティデータをリアルタイムでBrazeに直接同期します。これにより、ユーザーのロイヤルティステータスが変更されたときに、パーソナライズされたメッセージ（メール、プッシュ、SMS）をトリガーできます。

#### OpenAI - AIモデルプロバイダー {#openai-ai-model-provider}

[OpenAI]({{site.baseurl}}/partners/ai_model_providers/openai/)は、GPTなどの高度なAIモデルを作成し、自然言語の理解と生成を可能にして、ブランドが意味のある顧客インタラクションを構築・スケールできるようにします。

#### Shopgate - チャネル {#shopgate-channels}

[Shopgate]({{site.baseurl}}/partners/additional_channels_and_extensions/additional_channels/shopgate/)は、マーチャントがショッピングアプリを作成し、フルフィルメントツールとクライアンテリング（顧客データに基づくパーソナライズされた店内カスタマーサポート）を通じて実店舗の効率を向上させるのに役立つモバイルコマースおよびオムニチャネルプラットフォームです。

#### Splio - データと分析 - コホートインポート {#splio-data-and-analytics-cohort-import}

[Splio]({{site.baseurl}}/partners/data_and_analytics/cohort_import/splio/)は、カスタマーエクスペリエンスを損なうことなくキャンペーン数と収益を増加させるオーディエンス構築ツールで、オンラインとオフラインの両方でCRMキャンペーンのパフォーマンスを追跡する分析を提供します。

### SDK

#### SDKの破壊的更新

以下のSDK更新がリリースされました。破壊的更新は下記のとおりです。その他すべての更新は、対応するSDK変更ログをご確認ください。

- [Android SDK 41.1.1](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)
- [Flutter SDK 17.1.0](https://pub.dev/packages/braze_plugin/changelog)
- [Swift SDK 14.0.2](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
- [Xamarin SDK 9.0.0](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/CHANGELOG.md)
    - Androidバインディングを[Braze Android SDK 37.0.0から41.0.0に](https://github.com/braze-inc/braze-android-sdk/compare/v37.0.0...v41.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)更新。
    - iOSバインディングを[Braze Swift SDK 13.3.0から14.0.1に](https://github.com/braze-inc/braze-swift-sdk/compare/13.3.0...14.0.1#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)更新。
    - Braze Android SDKに必要な新しい推移的NuGet依存関係を追加：
        - Xamarin.AndroidX.DataStore.Preferences (1.1.7.1)
        - Xamarin.KotlinX.Serialization.Json.Jvm (1.9.0.2)
        - Xamarin.Kotlin.StdLibが2.0.21.3から2.3.0.1に更新されました。プロジェクトがこのパッケージを古いバージョンに明示的にピン留めしている場合、復元エラーを回避するために更新する必要があります。
    - News Feed機能を削除。
        - この機能はネイティブAndroid SDKのバージョン[38.0.0](https://github.com/braze-inc/braze-android-sdk/releases/tag/v38.0.0)で削除されました。
        - この機能はネイティブSwift SDKのバージョン[14.0.0](https://github.com/braze-inc/braze-swift-sdk/releases/tag/14.0.0)で削除されました。
    - BRZInAppMessageDismissalReason.BRZInAppMessageDismissalReasonWipeData列挙型ケースがBRZInAppMessageDismissalReason.WipeDataに名前変更されました。
- [Expo Plugin 4.0.0](https://github.com/braze-inc/braze-expo-plugin/releases/tag/4.0.0)
    - このバージョンにはBraze React Native SDK 19.0.0が必要です。
    - （Android）データ永続化レイヤーのメモリリークを修正。
    - （Android）アプリが終了状態から起動された場合のプッシュ通知ディープリンクを処理するためのBraze.getInitialPushPayload()のサポートを追加。これにより、アプリがコールドスタートされた場合にAndroidでプッシュ通知からのディープリンクが処理されない問題が解決されます。
- [React Native SDK 19.0.0](https://github.com/braze-inc/braze-react-native-sdk/releases/tag/19.0.0)
    - ネイティブSwift SDKバージョンバインディングをBraze Swift SDK 13.3.0から14.0.1に更新。
    - ネイティブAndroid SDKバージョンバインディングをBraze Android SDK 40.0.2から41.0.0に更新。

{% enddetails %}

{% details 2026年2月5日 %}

## 2026年2月5日リリース {#february-5-2026-release}

### BrazeAI<sup>TM</sup>

#### コンテンツオプティマイザー {#content-optimizer}

{% multi_lang_include release_type.md release="Beta" %}

[コンテンツオプティマイザー]({{site.baseurl}}/user_guide/brazeai/content_optimizer/)は、継続的で高バリアントなコンテンツテストのCanvasステップで、自動エンゲージメント最適化を実現します。メッセージステップと同様のドラッグアンドドロップ可能なインターフェイスを使用して、テストするコンポーネントを定義し、AIを使用してバリアントを生成し（または手動で入力）、Liquidタグを使用してこれらのコンポーネントをメッセージコンテンツにマッピングできます。

非コンテキストのマルチアームバンディットオプティマイザに基づいて構築されたコンテンツオプティマイザーは、ユーザーごとに1つのメッセージを送信し、予測推奨に基づいて配信するコンポーネントバリアントの組み合わせを決定します。ステップが時間の経過とともにデータを収集すると、パフォーマンスの高いバリアントは送信割り当てが自然に増え、パフォーマンスの低いバリアントは減ります。コンテンツオプティマイザーは、継続的な最適化を可能にするために、一貫した日次ユーザーボリューム（1日あたり少なくとも数千ユーザー）を持つ繰り返し送信Canvasesで最適に動作します。

### データ＆レポート

#### eコマース推奨イベント

{% multi_lang_include release_type.md release="Early access" %}

eコマース推奨イベントと既存の購入イベントを照合するために、[「Places Order」コンバージョンイベント]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/ecommerce_use_cases/#conversions-report)を追加しました。これは「Makes Purchase」に似ています。

### チャネルとタッチポイント

#### バナーでのロケール翻訳 {#translate-locales-in-banners}

{% multi_lang_include release_type.md release="Early access" %}

ワークスペースにロケールを追加した後、1つのバナー内で[異なる言語のユーザーをターゲット]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages/#translating-locales)にできます。

#### ドラッグアンドドロップContent Blocksの幅設定 {#configure-width-for-drag-and-drop-content-blocks}

ナビゲーションメニューのボタンを選択して、[Content Blockの幅を調整]({{site.baseurl}}/user_guide/channels/email/drag_and_drop/dnd_editor_blocks/#using-the-editor-to-add-a-content-block)できます。メールのグローバルスタイル設定で指定されていない場合、デフォルトの幅は100%です。指定されている場合は、グローバル設定が適用されます。

![幅を編集するオプションを持つ両面矢印。]({% image_buster /assets/img_archive/content_block_width_updated.png %}){: style="max-width:30%;" }

#### 自動IPウォーミングの使用 {#use-automated-ip-warming}

{% multi_lang_include release_type.md release="Early access" %}

[自動IPウォーミング]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/#automated-ip-warming)を使用して、毎日の送信量を徐々に増やし、受信トレイプロバイダーが送信パターンを学習し信頼できるようにします。Brazeは最もエンゲージメントの高いサブスクライバーに最初に送信し、ベストプラクティスに合ったペースで毎日のボリュームが増加します。

### パートナーシップ

#### LinkedIn – Canvas Audience Sync

[Braze Audience Sync to LinkedIn]({{site.baseurl}}/partners/canvas_audience_sync/linkedin_audience_sync/)を使用すると、BrazeインテグレーションのユーザーデータをLinkedIn顧客リストに追加して、行動トリガー、セグメンテーションなどに基づいた広告を配信できます。通常、メッセージをトリガーするために使用する基準（プッシュ、メール、SMS、webhookなど）が、BrazeのCanvasでユーザーデータに基づいて、LinkedIn顧客リストのそのユーザーに広告をトリガーできるようになりました。

#### Oracle Crowdtwist - データと分析 {#oracle-crowdtwist-data-analytics}

[Oracle Crowdtwist]({{site.baseurl}}/partners/crowdtwist/)は、ブランドがパーソナライズされたカスタマーエクスペリエンスを提供できるようにする、主要なクラウドネイティブ顧客ロイヤルティソリューションです。100以上のエンゲージメントパスを提供し、マーケターが顧客のより完全なビューを開発するための迅速な価値実現を提供します。

#### Fullstory - ダイナミックコンテンツ {#fullstory-dynamic-content}

[Fullstory]({{site.baseurl}}/partners/fullstory/)の行動データプラットフォームは、テクノロジーリーダーがより優れた、より情報に基づいた意思決定を行うのに役立ちます。デジタル行動データを分析スタックに注入することで、Fullstoryの特許取得済みテクノロジーは、行動データの質の力をスケールで解き放ち、すべてのデジタル訪問をアクション可能なインサイトに変換します。

#### Open Loyalty - データと分析 {#open-loyalty-data-analytics}

[Open Loyalty]({{site.baseurl}}/partners/openloyalty/)は、顧客ロイヤルティおよびリワードプログラムを構築・管理できるクラウドベースのロイヤルティプログラムプラットフォームです。BrazeとOpen Loyaltyのインテグレーションは、ポイント残高、ティア変更、有効期限警告などのロイヤルティデータをリアルタイムでBrazeに直接同期します。これにより、ユーザーのロイヤルティステータスが変更されたときに、パーソナライズされたメッセージ（メール、プッシュ、SMS）をトリガーできます。

#### DOTS.ECO - エクステンション {#dotseco-extensions}

[DOTS.ECO]({{site.baseurl}}/partners/docs.eco)は、追跡可能なデジタル証明書を通じて、現実世界の環境影響でユーザーに報酬を与えることができます。各証明書には、共有可能な証明書URLや画像URLなどのメタデータを含めることができるため、ユーザーは影響の証明を表示（再訪問）できます。

#### Mailizio - メッセージオーケストレーション {#mailizio-message-orchestration}

[Mailizio]({{site.baseurl}}/partners/mailizio/)は、直感的なビジュアルエディタを使用して再利用可能でブランドセーフなコンテンツを簡単にデザインできるメール作成・管理プラットフォームです。MailizioのBrazeへのインテグレーションにより、コンテンツブロックとメールテンプレートをエクスポートし、同じアセットからアプリ内メッセージを自動的に生成でき、迅速かつ完全にコントロールされたキャンペーン展開が可能になります。

### API {#apis}

#### メディアライブラリPOST API {#media-library-post-apis}

{% multi_lang_include release_type.md release="General availability" %}

メディアライブラリアセットをAPI経由で追加できるようになり、顧客、パートナー、代理店がメッセージ作成ワークフローをより自動化できるようになりました。[API]({{site.baseurl}}/api/endpoints/media_library/manage_assets/create/)を使用して、アセットファイルを直接アップロードしたり、既存のURLからファイルをコピーしたりできます。この機能は、インテグレーションとオートメーション機能を解放します。

### Currentsとデータ共有

#### ストレージ送信先およびデータ共有のエージェントコンソールイベント {#agent-console-events-for-storage-destinations-and-datashare}

{% multi_lang_include release_type.md release="General availability" %}

2つの新しい[イベント](http://braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events)が、ストレージ送信先（AWS S3、GCS、Azure Blob Storage）とSnowflakeデータ共有で利用可能になりました：`agentconsole.AgentExecuted`および`agentconsole.ToolInvocation`。これらのイベントにより、ダウンストリームシステムでエージェントコンソールの使用状況と詳細を分析でき、エージェントの使用状況を理解し最大限に活用するのに役立ちます。エージェントを使用すると、Canvasesやカタログでのコンテンツ生成、インテリジェントな意思決定に基づくユーザーの異なるパスへのルーティングなど、Braze全体で特定のタスクを実行できるインテリジェントエージェントを作成・デプロイできます。詳細については、[Currents変更ログ](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs#changes-in-version-5-release-date-2026-02-04)を参照してください。

#### 各チャネルの新しい「再試行」イベント {#new-retry-events-for-individual-channels}

{% multi_lang_include release_type.md release="General availability" %}

新しい[再試行イベント](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events)が、メール、LINE、プッシュ通知、SMS、webhook、およびWhatsAppチャネルで利用可能になりました。これらのイベントは、フリークエンシーキャップによってスケジュールされたメッセージがアボートされるのではなく遅延される場合の可視性を提供します。メッセージが優先度を下げられたりフリークエンシーキャップが適用されたりすると、設定された再試行ウィンドウ内で再試行できるようになり、メッセージ配信パターンとフリークエンシーキャップの影響についてより良いインサイトが得られます。詳細については、[Currents変更ログ](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs#changes-in-version-5-release-date-2026-02-04)を参照してください。

#### TokenStateChangeイベントに新しい「time_ms」フィールドを追加 {#add-new-time_ms-field-to-tokenstatechange-event}

{% multi_lang_include release_type.md release="General availability" %}

新しい`time_ms`フィールドが[`users.behaviors.pushnotification.TokenStateChange`](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events)イベントに追加され、プッシュトークンの状態変更をミリ秒レベルの粒度で追跡できるようになりました。この精度の向上により、同じ秒内に複数の変更が発生した場合のプッシュトークンの最新ステータスを理解でき、ダウンストリームシステムで正しいサブスクリプションステータスを持っていることに確信を持てます。詳細については、[Currents変更ログ](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs#changes-in-version-5-release-date-2026-02-04)を参照してください。

#### Tealium送信先への匿名ユーザーの送信 {#send-anonymous-user-to-tealium-destinations}

{% multi_lang_include release_type.md release="General availability" %}

外部ユーザーIDが定義されていないイベントを[Tealium]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/tealium/tealium_for_currents?redirected=1#tealium-for-currents)送信先にストリーミングできるようになりました。Currentsインテグレーションで「匿名ユーザーのイベントを含める」チェックボックスを選択すると、外部ユーザーIDのないイベントが抑制されずに送信先に送信されます。この機能は、ダウンストリーム分析や、識別されていない匿名ユーザーを含むユースケースに不可欠です。

##### カスタムHTTP送信先への匿名ユーザーの送信 {#send-anonymous-user-to-customhttp-destinations}

{% multi_lang_include release_type.md release="Beta" %}

外部ユーザーIDが定義されていないイベントをカスタムHTTP送信先にストリーミングできるようになりました。Currentsインテグレーションで「匿名ユーザーのイベントを含める」チェックボックスを選択すると、外部ユーザーIDのないイベントが抑制されずに送信先に送信されます。この機能は、ダウンストリーム分析や、識別されていない匿名ユーザーを含むユースケースに不可欠です。

#### メールオープンイベント — 「machine_open」フィールド {#email-open-event-machine_open-field}

[メールオープンイベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/#email-open-events)が「machine_open」フィールド値を生成するようになり、[_Machine Open_]({{site.baseurl}}/user_guide/analytics/reporting/report_metrics/#machine-opens)メトリクスをレポートできます。

### SDK

以下のSDK更新がリリースされました。Swift SDK v14.0.1はユニバーサルリンクの処理に関する問題を修正します。Android SDK v40.2.0は潜在的なメモリリークを修正し、透明なアクティビティが存在する場合に複数のセッションが開かれる問題を解決します。Expo SDK v3.2.0は、ユニバーサルリンクのネイティブSwift SDK処理を設定する`forwardUniversalLinks`オプション（デフォルト：false）を追加します。

#### SDKの破壊的更新

以下のSDK更新がリリースされました。破壊的更新は下記のとおりです。その他すべての更新は、対応するSDK変更ログをご確認ください。

- [Android SDK 41.0.0](https://github.com/braze-inc/braze-android-sdk/releases/tag/v41.0.0)
    - `BrazeConfig.Builder.setIsLocationCollectionEnabled()`を`setIsAutomaticLocationCollectionEnabled()`に名前変更。
    - `BrazeConfig.isLocationCollectionEnabled`を`isAutomaticLocationCollectionEnabled`に名前変更。
    - `BrazeConfigurationProvider.isLocationCollectionEnabled`を`isAutomaticLocationCollectionEnabled`に名前変更。
- [Android SDK 40.2.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#4020)
- [Expo Plugin 3.2.0](https://github.com/braze-inc/braze-expo-plugin/blob/main/CHANGELOG.md)
- [Swift SDK 14.0.1](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)

{% enddetails %}

{% details 2026年1月8日 %}
## 2026年1月8日リリース {#january-8-2026-release}

### データ＆レポート

#### Currentsイベントの更新 {#updates-to-currents-events}

{% multi_lang_include release_type.md release="General availability" %}

バージョン4では、以下の変更がCurrentsに加えられました。

* イベントタイプ`users.behaviors.pushnotification.TokenStateChange`のフィールド変更：
    * 新しい`string`フィールド`push_token`を追加：イベントのプッシュトークン
* イベントタイプ`users.messages.pushnotification.Bounce`のフィールド変更：
    * 新しい`string`フィールド`push_token`を追加：イベントのプッシュトークン
* イベントタイプ`users.messages.pushnotification.Send`のフィールド変更：
    * 新しい`string`フィールド`push_token`を追加：イベントのプッシュトークン
* イベントタイプ`users.messages.rcs.Click`のフィールド変更：
    * 新しい`string`フィールド`canvas_variation_name`を追加：このユーザーが受け取ったCanvasバリエーションの名前
    * フィールド`user_phone_number`が*オプション*になりました。
* イベントタイプ`users.messages.rcs.InboundReceive`のフィールド変更：
    * フィールド`user_id`が*オプション*になりました。
* イベントタイプ`users.messages.rcs.Rejection`のフィールド変更：
    * 新しい`string`フィールド`canvas_step_message_variation_id`を追加：このユーザーが受け取ったキャンバスステップメッセージバリエーションのAPI ID

リリースごとのイベント変更については、[Currents変更ログ]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs/)を参照してください。

#### すべての行による同期ログのエクスポート {#export-sync-logs-by-all-rows}

{% multi_lang_include release_type.md release="Early access" %}

[クラウドデータ取り込み**同期ログ**ダッシュボード]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_logs/#exporting-sync-logs)で、同期実行の行レベルログのエクスポートを以下から選択できます。

* **エラーのある行：** **Error**ステータスの行のみを含むファイルをダウンロードします。
* **すべての行：** 実行で処理されたすべての行を含むファイルをダウンロードします。

### チャネルとタッチポイント

#### Bring Your Own（BYO）WhatsAppコネクター {#bring-your-own-byo-whatsapp-connector}

[Bring Your Own（BYO）WhatsAppコネクター]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/byo_connector/)は、BrazeとInfobipの間のパートナーシップで、InfobipのWhatsApp Business Manager（WABA）へのBrazeアクセスを提供します。これにより、セグメンテーション、パーソナライゼーション、キャンペーンオーケストレーションにはBrazeを使用しながら、Infobipで直接メッセージングコストを管理・支払いできます。

#### Canvasのバナー

{% multi_lang_include release_type.md release="Early access" %}

Canvasの[メッセージステップ]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step/)のメッセージングチャネルとして**バナー**を選択できます。ドラッグアンドドロップエディタを使用してパーソナライズされたインラインメッセージを作成し、各ユーザーセッションの開始時に自動的に更新される、非侵入的でコンテキストに関連するエクスペリエンスを提供します。

#### ダイナミックBCC {#dynamic-bcc}

{% multi_lang_include release_type.md release="General availability" %}

[ダイナミックBCC]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences/?tab=bcc%20address#dynamic-bcc)では、BCCアドレスにLiquidを使用できます。この機能は**メール設定**でのみ利用可能で、キャンペーン自体では設定できません。メール受信者ごとに1つのBCCアドレスのみが許可されます。

#### チャネルベースのレート制限 {#channel-based-rate-limits}

マルチチャネルのCampaignまたはCanvas全体で共有されるレート制限の代わりに、チャネルごとに特定のレート制限を選択できます。この場合、レート制限は選択した各チャネルに適用されます。たとえば、CampaignまたはCanvasを設定して、CampaignまたはCanvas全体で1分あたり最大5,000件のwebhookと2,500件のSMSメッセージを送信できます。詳細については、[レート制限とフリークエンシーキャップ]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/)を参照してください。

### パートナーシップ

#### LILT - ローカライゼーション {#lilt-localization}

[LILT]({{site.baseurl}}/partners/lilt/)は、エンタープライズ翻訳とコンテンツ作成のための完全なAIソリューションです。LILTにより、グローバル組織はAIエージェントと完全に自動化されたワークフローを使用して、コンテンツ、製品、コミュニケーション、サポート業務を拡張・最適化できます。

### SDKの破壊的更新

以下のSDK更新がリリースされました。破壊的更新は下記のとおりです。その他すべての更新は、対応するSDK変更ログをご確認ください。

- [Android 40.1.1](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#4011)
- [Android SDK 40.1.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#4010)
- [Swift SDK 14.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
    - News Feedを削除。
        - これにより、News Feedに関連するすべてのUI要素、データモデル、アクションが完全に削除されます。
- [Web SDK 6.4.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)

{% enddetails %}

{% details 2025年12月9日 %}

## 2025年12月9日 {#december-9-2025}

### データ＆レポート

#### ランディングページへのGoogle Tag Managerの追加 {#adding-google-tag-manager-to-a-landing-page}

ランディングページにGoogle Tag Managerを追加するには、ドラッグアンドドロップエディタでランディングページにカスタムコードブロックを追加し、[Tag Managerコード]({{site.baseurl}}/user_guide/messaging/landing_pages/#adding-google-tag-manager-to-a-landing-page)をブロックに挿入します。

### オーケストレーション

#### SMS Liquidユースケース {#sms-liquid-use-case}

[受信SMSキーワードに基づいて異なるメッセージで応答する]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/liquid_use_cases/#sms-keyword-response)ユースケースは、特定の受信メッセージに異なるメッセージコピーで応答するためのダイナミックなSMSキーワード処理を組み込んでいます。たとえば、誰かが「START」と「JOIN」のテキストを送信した場合に異なる応答を送信できます。

#### コネクテッドコンテンツの許可リスト {#allowlisting-for-connected-content}

[コネクテッドコンテンツ]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call/)に使用する特定のURLを許可リストに登録できます。この機能にアクセスするには、カスタマーサクセスマネージャーにお問い合わせください。

### チャネルとタッチポイント

#### SMS文字エンコーディング {#sms-character-encoding}

[SMSセグメント計算機]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator/#segment-calculator)に文字エンコーディング機能が追加されました。**文字エンコーディングを表示**を選択して、どの文字がGSM-7またはUCS-2としてエンコードされているかを確認できます。

![SMSセグメント計算機。テキストボックスにSMSのサンプルメッセージが入力され、文字エンコーディングが有効になっています。]({% image_buster /assets/img/sms/character_encoding.png %}){: style="max-width:70%;"}

#### 最適化されたWhatsAppメッセージ {#whatsapp-messages-with-optimization}

WhatsApp用のMM APIは100%の配信可能性を提供しないため、他のチャネルでメッセージを受信していない可能性のあるユーザーをリターゲティングする方法を理解することが重要です。

ユーザーをリターゲティングするには、特定のメッセージを受信しなかったユーザーのセグメントを構築することをお勧めします。これを行うには、エラーコード`131049`でフィルタリングします。これは、WhatsAppのユーザーごとのマーケティングテンプレート制限の適用によりマーケティングテンプレートメッセージが送信されなかったことを示します。[Braze CurrentsまたはSQLセグメントエクステンションを使用]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/optimized_delivery/#retargeting-users-on-other-braze-channels)して実行できます。

### パートナーシップ

#### OtherLevels - ダイナミックコンテンツ {#otherlevels-dynamic-content}

[OtherLevels]({{site.baseurl}}/partners/otherlevels/)は、生成AIを使用して、従来のコンテンツをオンブランドのパーソナライズされた動画やリッチメディアエクスペリエンスに大規模に変換することで、スポーツブランド、パブリッシャー、オペレーターが顧客とどのようにつながるかを変革するエクスペリエンスプラットフォームです。

### SDK

#### SDKの破壊的更新

以下のSDK更新がリリースされました。破壊的更新は下記のとおりです。その他すべての更新は、対応するSDK変更ログをご確認ください。

- [Web SDK 6.3.1](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)

{% enddetails %}

{% details 2025年11月11日 %}

## 2025年11月11日 {#november-11-2025}

### データの柔軟性 {#data-flexibility}

#### `Live Activities Push to Start Registered for App`セグメンテーションフィルター {#live-activities-push-to-start-registered-for-app-segmentation-filter}

`Live Activities Push to Start Registered for App`フィルターは、特定のアプリのiOSプッシュ通知を介してLive Activityを開始するように登録されているかどうかによってユーザーをセグメント化します。

#### RFM SQLセグメントエクステンション {#rfm-sql-segment-extension}

[RFM（recency、frequency、monetary）セグメントエクステンション]({{site.baseurl}}/rfm_segments/)を作成して、購買習慣を測定することで最良のユーザーをターゲットにできます。

RFM分析は、各カテゴリ（recency、frequency、monetary）について0〜3のスケールでユーザーをスコアリングすることで最良のユーザーを特定するマーケティング手法です。3が最良のスコアで、0が最悪のスコアです。recency、frequency、monetaryの値はすべて、選択した特定の時間範囲のデータに基づいています。

#### カスタム属性 — 値 {#custom-attributes-values}

使用状況レポートを表示する際に、[**値**タブ]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/#values-tab)を選択して、約250,000ユーザーのサンプルに基づいて選択したカスタム属性の上位値を表示できます。

#### クラウドデータ取り込みの同期ログとオブザーバビリティ {#sync-logs-and-observability-for-cloud-data-ingestion}

{% multi_lang_include release_type.md release="General availability" %}

クラウドデータ取り込み（CDI）[同期ログダッシュボード]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_logs/)では、CDIによって処理されたすべてのデータを監視し、データが正常に同期されたかどうかを確認し、「不正」または欠落データの問題を診断できます。

#### マルチルールフィーチャーフラグ展開 {#multi-rule-feature-flag-rollouts}

[マルチルールフィーチャーフラグ展開]({{site.baseurl}}/developer_guide/feature_flags/create/#multi-rule-feature-flag-rollouts)を使用して、ユーザーを評価するための一連のルールを定義します。これにより、正確なセグメンテーションとコントロールされた機能リリースが可能になります。この方法は、同じ機能を多様なオーディエンスにデプロイする場合に最適です。

#### ドラッグアンドドロップ製品ブロックのカタログフィールドへのマッピング {#mapping-to-catalog-fields-for-drag-and-drop-product-blocks}

カタログ設定で、**製品ブロック**トグルを選択して、カタログの[特定のフィールドと情報にマッピング]({{site.baseurl}}/user_guide/messaging/design_and_edit/product_blocks/#catalog-setup)できます。これにより、製品タイトル、製品URL、画像URLとして使用するフィールドを選択できます。

#### Currentsでのフリークエンシーキャップ中止イベント {#frequency-capping-abort-events-in-currents}

Currentsを使用する際に、チャネルの中止イベントで`abort_type`を参照できるようになりました。これにより、メッセージがフリークエンシーキャップのために中止されたことが識別され、どのフリークエンシーキャップルールが中止の原因になったかが含まれます。これは、フリークエンシーキャップルールの設定方法を知らせるのに役立ちます。具体的なCurrentsイベントの詳細については、[メッセージエンゲージメントイベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/)を参照してください。

### 強力なチャネル {#robust-channels}

#### バックグラウンド行画像 {#background-row-images}

{% multi_lang_include release_type.md release="General availability" %}

**行プロパティ**パネルで、アプリ内メッセージまたはランディングページに[バックグラウンド行画像を追加]({{site.baseurl}}/user_guide/channels/in_app_messages/customize/style_settings/#background-image)できます。**バックグラウンド画像**をオンに切り替え、画像URLを入力するか、[メディアライブラリ]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/)から画像を選択します。最後に、代替テキスト、サイズ、位置、および画像を繰り返して行全体にパターンを作成するかどうかを設定します。

![水平リピートパターンを持つピザのバックグラウンド行画像。]({% image_buster /assets/img_archive/background_row.png %})

#### プレビューリンクをコピー {#copy-preview-link}

[バナー]({{site.baseurl}}/user_guide/channels/banners/create_a_banner/#step-5-test-your-message-optional)、[メールカスタムフッター]({{site.baseurl}}/user_guide/channels/email/customize/custom_email_footer/#creating-your-custom-footer)、および[メールオプトインと配信停止ページ]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences/?tab=custom%20footer#subscription-pages-and-footers)で**プレビューリンクをコピー**を使用して、ランダムなユーザーに対してコンテンツがどのように表示されるかを示す共有可能なリンクを生成できます。

#### 配信を最適化したWhatsAppメッセージ {#whatsapp-messages-with-optimized-delivery}

Metaの高度なAIシステムを使用して、マーケティングメッセージを、最もエンゲージする可能性の高いユーザーに配信し、配信可能性とメッセージエンゲージメントを大幅に向上させます。

[配信を最適化したWhatsAppメッセージ]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/optimized_delivery/)は、Metaの新しい[Marketing Messages Lite API](https://developers.facebook.com/docs/whatsapp/marketing-messages-lite-api/)を使用して送信され、従来のCloud APIと比較して優れたパフォーマンスを提供します。この新しい送信パイプラインは、メッセージを価値あるものとして受け取りたいユーザーにより良くリーチするのに役立ちます。

#### WhatsApp Flows

WhatsApp FlowメッセージをBraze CanvasまたはCampaignに組み込む場合、ユーザーがFlowを通じて送信する特定の情報をキャプチャして活用できます。Brazeは、必要な階層化カスタム属性（NCA）スキーマを生成するために、ユーザーレスポンスの構造、特にJSONレスポンスの予想される形状に関する追加情報を受け取る必要があります。

[Flowレスポンスをカスタム属性として保存]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/whatsapp_flows/?tab=recommended%20method#step-1-generate-the-flow-custom-attribute)し、テスト送信を完了することで、レスポンス構造に関する情報をBrazeに提供できるようになりました。

#### 編集可能なユーザープレビュー {#editable-user-preview}

[ランダムまたは既存のユーザーから個々のフィールドを編集]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages/?tab=webhook#customizing-an-existing-user)して、メッセージ内のダイナミックコンテンツをテストできます。**編集**を選択して、選択したユーザーを変更可能なカスタムユーザーに変換します。

![「ユーザーとしてプレビュー」タブと「編集」ボタン。]({% image_buster /assets/img_archive/edit_user_preview.png %}){: style="max-width:50%;"}

### AIとMLのオートメーション {#ai-and-ml-automation}

#### BrazeAI Decisioning Studio™ Go

以下の設定記事を参照して、[BrazeAI Decisioning Studio™ Go]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/)とのインテグレーションを設定できるようになりました。

- [Braze]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/connect_data_sources/)
- [Klaviyo]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/connect_data_sources/)
- [Salesforce Marketing Cloud]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/connect_data_sources/)

#### Brazeエージェントの新機能 {#new-features-for-braze-agents}

{% multi_lang_include release_type.md release="Beta" %}

[Brazeエージェント]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/)をカスタマイズできるようになりました。

- エージェントのレスポンスに従うための[ブランドガイドライン]({{site.baseurl}}/user_guide/administer/global/workspace_settings/brand_guidelines/)の適用。
- カタログを参照してメッセージをさらにパーソナライズ。
- [出力形式]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/#output-format)を指定してエージェントの出力を構造化。
- エージェントの出力の偏差レベルを[temperature]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/#temperature)で調整。

### BrazeAI Operator<sup>TM</sup>でのChatGPTモデル {#chatgpt-models-with-brazeai-operatortm}

{% multi_lang_include release_type.md release="Beta" %}

[Operator]({{site.baseurl}}/user_guide/brazeai/operator/)で異なるリクエストタイプに使用する以下のGPTモデルから選択できます。

- GPT-5 nano
- GPT-5 mini（デフォルト）
- GPT-5

### 新しいBrazeパートナーシップ {#new-braze-partnerships}

#### StackAdapt - 広告 {#stackadapt-advertising}

[StackAdapt]({{site.baseurl}}/partners/stackadapt/)は、ターゲットを絞ったパフォーマンス駆動の広告を配信するAI駆動のマーケティングプラットフォームです。BrazeからStackAdapt Data Hubにユーザープロファイルデータを同期できます。2つのプラットフォームを接続することで、顧客の統一されたビューを作成し、ファーストパーティデータを有効化して広告パフォーマンスを向上させることができます。

#### Cloudinary - ダイナミックコンテンツ {#cloudinary-dynamic-content}

[Cloudinary]({{site.baseurl}}/partners/cloudinary/)は、チャネルやカスタマージャーニー全体のあらゆるキャンペーンに大規模に画像や動画を管理、編集、最適化、配信できる画像・動画プラットフォームです。統合して有効にすると、Cloudinaryのメディア管理がBraze CampaignsおよびCanvasesにダイナミックでコンテキストに応じたパーソナライズされたアセット配信を提供します。

#### Kameleoon - ABテスト {#kameleoon-ab-testing}

[Kameleoon]({{site.baseurl}}/partners/kameleoon/)は、実験、AIパワーのパーソナライゼーション、機能管理機能を1つの統一プラットフォームに備えた最適化ソリューションです。

### SDKの更新 {#sdk-updates}

以下のSDK更新がリリースされました。破壊的更新は下記のとおりです。その他すべての更新は、対応するSDK変更ログをご確認ください。

- [React Native SDK 18.0.0](https://github.com/braze-inc/braze-react-native-sdk/blob/16.1.0/CHANGELOG.md)
    - `subscribeToInAppMessage`のコールバックおよび`Braze.Events.IN_APP_MESSAGE_RECEIVED`の`addListener`のTypescript型を修正。
        - これらのリスナーは、新しい`InAppMessageEvent`型のコールバックを適切に返すようになりました。以前は、`BrazeInAppMessage`型を返すようにメソッドに注釈が付けられていましたが、実際には`String`を返していました。
         - いずれかのサブスクリプションAPIを使用している場合は、このバージョンに更新した後もアプリ内メッセージの動作が変更されていないことを確認してください。`BrazeProject.tsx`のサンプルコードを参照してください。
    - API `logInAppMessageClicked`、`logInAppMessageImpression`、`logInAppMessageButtonClicked`は、既存のパブリックインターフェイスに合わせて`BrazeInAppMessage`オブジェクトのみを受け入れるようになりました。
        - 以前は、`BrazeInAppMessage`オブジェクトと`String`の両方を受け入れていました。
    - `BrazeInAppMessage.toString()`はJSON文字列表現の代わりに人間が読み取れる文字列を返すようになりました。
        - アプリ内メッセージのJSON文字列表現を取得するには、`BrazeInAppMessage.inAppMessageJsonString`を使用してください。
    - iOSでは、`[[BrazeReactUtils sharedInstance] formatPushPayload:withLaunchOptions:]`が`[BrazeReactDataTranslator formatPushPayload:withLaunchOptions:]`に移動されました。
        - この新しいメソッドは、インスタンスメソッドではなくクラスメソッドになりました。
    - `BrazeReactUtils`メソッドにnullabilityアノテーションを追加。
    - 以下の非推奨メソッドおよびプロパティをAPIから削除：
        - `getInstallTrackingId(callback:)`は`getDeviceId`が優先されます。
        - `registerAndroidPushToken(token:)`は`registerPushToken`が優先されます。
        - `setGoogleAdvertisingId(googleAdvertisingId:adTrackingEnabled:)`は`setAdTrackingEnabled`が優先されます。
        - `PushNotificationEvent.push_event_type`は`payload_type`が優先されます。
        - `PushNotificationEvent.deeplink`は`url`が優先されます。
        - `PushNotificationEvent.content_text`は`body`が優先されます。
        - `PushNotificationEvent.raw_android_push_data`は`android`が優先されます。
        - `PushNotificationEvent.kvp_data`は`braze_properties`が優先されます。
    - ネイティブAndroid SDKバージョンバインディングを[Braze Android SDK 39.0.0から40.0.2に](https://github.com/braze-inc/braze-android-sdk/compare/v39.0.0...v40.0.2#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)更新。
- [.NET MAUI (Xamarin) SDK Version 8.0.0](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/CHANGELOG.md)
    - iOSバインディングを[Braze Swift SDK 12.1.0から13.3.0に](https://github.com/braze-inc/braze-swift-sdk/compare/12.1.0...13.3.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)更新。Xcode 26サポートを含みます。
- [Flutter SDK 16.0.0](https://pub.dev/packages/braze_plugin/changelog)
    - ネイティブAndroidブリッジを[Braze Android SDK 39.0.0から40.0.0に](https://github.com/braze-inc/braze-android-sdk/compare/v39.0.0...v40.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)更新。
- [Braze Swift SDK 13.3.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
- [Web SDK 6.3.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
- [Android SDK 40.0.0-40.0.2](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)

{% enddetails %}