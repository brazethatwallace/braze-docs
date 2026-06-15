---
nav_title: 11月
page_order: 1
noindex: true
page_type: update
description: "この記事には、2021年11月のリリースノートが含まれています。"
---
# 2021年11月 {#november-2021}

## クリック開封率レポート指標 {#click-to-open-rate-reporting-metric}
Brazeは、[レポートビルダー]({{site.baseurl}}/user_guide/analytics/reports/report_builder/)で利用可能な新しいメール指標「クリック開封率」を追加しました。この指標は、開封されたメールのうちクリックされた割合を表します。

## マシンオープンレポート指標 {#machine-open-reporting-metric}

新しいメール指標「[マシンオープン]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/analytics_glossary/#machine-opens)」が、キャンバスおよびキャンペーンの分析ページでメール向けに利用可能になりました。この指標は、人為的ではないメール開封（Appleのサーバーによって開封されたものなど）を特定し、開封総数のサブセットとして表示されます。

## random_bucket_number Liquid変数 {#randombucketnumber-liquid-variable}
メッセージパーソナライゼーションの[サポートされているLiquid変数]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/#supported-personalization-tags)のリストに、変数`random_bucket_number`が追加されました。

## iOS 15リッチプッシュ通知ガイドライン {#ios-15-rich-push-notification-guidelines}
新しい[iOSプッシュ通知ガイドライン]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/rich_notifications/)がiOSリッチドキュメントに追加されました。通知状態に関する情報やテキスト切り捨て変数の内訳が含まれています。

## EUでWebhookとコネクテッドコンテンツのホワイトリストに登録するIP {#ips-to-whitelist-in-eu-for-webhooks-and-connected-content}
EUでWebhookとコネクテッドコンテンツのホワイトリストに追加するIPが、[Webhook]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook/)および[コネクテッドコンテンツ]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call/)の記事に追加されました。これらの新しいIPには`18.157.135.97`、`3.123.166.46`、`3.64.27.36`、`3.65.88.25`、`3.68.144.188`、`3.70.107.88`が含まれます。

## 購入エクスポートエンドポイント {#export-purchases-endpoint}
Brazeに新しい[`/purchases/product_list`エンドポイント]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id/)が追加されました。このエンドポイントは、製品IDのページ分割されたリストを返します。

## 新しいBrazeパートナーシップ {#new-braze-partnerships}

### Adobe - 顧客データプラットフォーム {#adobe-customer-data-platform}
Brazeと[Adobe]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/adobe/#adobe)の統合により、ブランドはAdobeデータ（カスタム属性やセグメント）をリアルタイムでBrazeに接続・マッピングできます。ブランドはこのデータに基づいて行動し、パーソナライズされたターゲットを絞ったエクスペリエンスをユーザーに提供できます。

### BlueConic - 顧客データプラットフォーム {#blueconic-customer-data-platform}
[Blueconic]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/blueconic/#blueconic)を使用すると、会社ユーザーはデータを永続的な個別のプロファイルに統合し、顧客タッチポイントやシステムを横断して同期できます。これにより、カスタマーライフサイクルオーケストレーション、モデリングと分析、デジタル製品とエクスペリエンス、オーディエンスベースの収益化など、成長に重点を置いた幅広いイニシアチブをサポートできます。

### Worthy - ダイナミックコンテンツ {#worthy-dynamic-content}
Brazeと[Worthy]({{site.baseurl}}/partners/message_personalization/dynamic_content/worthy/#worthy)の統合により、Worthyのドラッグ＆ドロップダイナミックコンテンツエディターを使用して、パーソナライズされたリッチなアプリ内エクスペリエンスを簡単に作成し、Brazeを通じて配信できます。

### Judo - ダイナミックコンテンツ {#judo-dynamic-content}
[Judo]({{site.baseurl}}/partners/message_personalization/dynamic_content/judo/#judo)とBrazeの統合により、キャンペーンのコンポーネントを上書きしてJudoエクスペリエンスに置き換えることができます。BrazeのデータはJudoエクスペリエンスでパーソナライズされたコンテンツをサポートするために使用できます。ユーザーイベントとエクスペリエンスからのデータは、アトリビューションとターゲティングのためにBrazeにフィードバックできます。

### Line - メッセージング {#line-messaging}
[Line]({{site.baseurl}}/partners/message_orchestration/additional_channels/messaging/line/#line)とBrazeの統合により、BrazeのWebhook、高度なセグメンテーション、パーソナライゼーション、およびトリガー機能を活用して、[Line Messaging API](https://developers.line.biz/en/docs/messaging-api/overview/)を介してLineのユーザーにメッセージを送信できます。

### RevenueCat - 決済 {#revenuecat-payments}
[RevenueCat]({{site.baseurl}}/partners/data_and_infrastructure_agility/payments/revenuecat/#revenuecat)とBrazeの統合により、顧客の購入およびサブスクリプションライフサイクルイベントをプラットフォーム間で自動的に同期できます。これにより、無料トライアル中にオプトアウトした顧客への働きかけや、請求に問題のある顧客へのリマインダーの送信など、顧客のサブスクリプションライフサイクルステージに対応するキャンペーンを作成できます。

### Punchh - ロイヤルティ {#punchh-loyalty}
[Punchh]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/punchh/#punchh)はBrazeと提携し、ギフトやロイヤルティのために2つのプラットフォーム間でデータを同期しています。Brazeで公開されたデータはセグメンテーションに利用でき、Brazeで設定されたWebhookテンプレートを介してユーザーデータをPunchhに同期できます。