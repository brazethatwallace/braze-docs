---
nav_title: 6月
page_order: 6
noindex: true
page_type: update
description: "この記事には2021年6月のリリースノートが含まれています。"
---

# 2021年6月 {#june-2021}

## トランザクションメールキャンペーン {#transactional-email-campaigns}

トランザクションメールは、送信者と受信者間で合意されたトランザクションを円滑に進めるために送信されるメールです。Brazeの[トランザクションメールキャンペーン]({{site.baseurl}}/api/api_campaigns/transactional_campaigns/)は、注文確認、パスワードリセット、請求アラート、その他のビジネスクリティカルな通知など、自動化された非宣伝的なメールメッセージの送信を目的として構築されています。また、対応する[トランザクションメールエンドポイント]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message/)も作成されました。トランザクションメールと新しいエンドポイントは、一部のBrazeパッケージのみで利用できます。

## イベントプロパティのネストされたオブジェクトのサポート {#nested-object-support-for-event-properties}

Brazeで、カスタムイベントおよび購入イベントの[ネストされたオブジェクト]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/nested_object_support/)がサポートされるようになりました。ネストされたオブジェクトにより、カスタムイベントや購入のプロパティとしてデータの配列を送信できます。このネストされたデータは、Liquidとドット記法を使用することで、APIトリガーメッセージにパーソナライズされた情報をテンプレート化するために使用できます。

## 新しいHMAC Liquidフィルター {#new-hmac-liquid-filters}

新しい[`hmac_sha1`と`hmac_sha256` Liquidエンコードフィルター]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters/)がBrazeプラットフォームに追加されました。

## 購入イベントページ {#purchase-event-page}

Brazeでの購入イベントの詳細について知りたいですか？詳しくは[購入イベント]({{site.baseurl}}/user_guide/data/activation/events/purchase_events/)の記事をご覧ください。

## 新しいBrazeパートナーシップ {#new-braze-partnerships}

### Nexla - ワークフローの自動化 {#nexla-workflow-automation}

[Nexla]({{site.baseurl}}/partners/nexla/)は統合データ運用分野のリーダーであり、2021年のGartner Cool Vendorに選出されています。Currentsを使用してデータウェアハウスにデータを送信するお客様は、Nexlaを活用してそのデータを抽出、変換し、他の場所に読み込むことで、エコシステム全体でデータに簡単にアクセスできるようになります。Nexlaにより、Braze Currentsを使用して、ポイントアンドクリックするだけで、カスタム形式のデータを任意の送信先に配信できます。

### Amperity - 顧客データプラットフォーム {#amperity-customer-data-platform}

[Amperity]({{site.baseurl}}/partners/amperity/)は、包括的なエンタープライズ顧客データプラットフォームであり、ブランドが自社の顧客を知り、戦略的な意思決定を行い、消費者により良いサービスを提供するために適切なアクションを一貫して取ることを支援します。Amperityは、CDPとBraze全体で顧客の統合ビューを提供し、貴重なAmperityデータをBrazeに送信できるようにすることで、Brazeプラットフォームをサポートします。

### Digioh - アンケート {#digioh-surveys}

[Digioh]({{site.baseurl}}/partners/digioh/)は、リストの拡大、ファーストパーティデータの取り込み、Brazeのキャンペーンでのデータの活用を支援します。ドラッグ＆ドロップビルダーを使用すると、ブランドに合わせたフォーム、ポップアップ、ユーザー設定センター、ランディングページ、顧客とのつながりを築くアンケートなどを簡単に作成できます。

### AppsFlyer Audiences - アトリビューション/分析 {#appsflyer-audiences-attributionanalytics}

[AppsFlyer]({{site.baseurl}}/partners/message_orchestration/attribution/appsflyer/)は、モバイルマーケティングにおける分析やアトリビューションを計測するプラットフォームです。マーケティング分析、モバイルアトリビューション、ディープリンクにより、アプリの分析と最適化を支援します。[AppsFlyer Audiences]({{site.baseurl}}/partners/appsflyer_audiences/)を使用すると、オーディエンスセグメントを構築し、これらのセグメントを直接Brazeに渡して、強力なカスタマーエンゲージメントキャンペーンを作成できます。