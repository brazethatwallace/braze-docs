---
nav_title: 6月
page_order: 6
noindex: true
page_type: update
description: "この記事には2021年6月のリリースノートが含まれています。"
---

# 2021年6月 {#june-2021}

## トランザクションメールキャンペーン {#transactional-email-campaigns}

トランザクションメールとは、送信者と受信者の間で合意された取引を促進するために送信されるメールです。Brazeの[トランザクションメールキャンペーン]({{site.baseurl}}/api/api_campaigns/transactional_campaigns)は、注文確認、パスワードリセット、請求アラート、その他のビジネスクリティカルな通知など、自動化された非プロモーションメールメッセージの送信を目的として構築されています。さらに、対応する[トランザクションメールエンドポイント]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message)も作成されています。トランザクションメールと新しいエンドポイントは、一部のBrazeパッケージでのみ利用できます。

## カスタムイベントプロパティのネストオブジェクトサポート {#nested-object-support-for-event-properties}

Brazeは、カスタムイベントおよび購入イベントの[ネストオブジェクト]({{site.baseurl}}/user_guide/data/activation/events/custom_events/nested_objects)をサポートするようになりました。ネストオブジェクトを使用すると、カスタムイベントや購入のプロパティとしてデータの配列を送信できます。このネストされたデータは、Liquidおよびドット記法を使用して、APIトリガーメッセージでパーソナライズされた情報をテンプレート化するために使用できます。

## 新しいHMAC Liquidフィルター {#new-hmac-liquid-filters}

Brazeプラットフォームに、新しい[`hmac_sha1`および`hmac_sha256` Liquidエンコーディングフィルター]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters)が追加されました。

## 購入イベントページ {#purchase-event-page}

Brazeの購入イベントの詳細について知りたいですか？専用の[購入イベント]({{site.baseurl}}/user_guide/data/activation/events/purchase_events)の記事をご覧ください。

## Brazeの新しいパートナーシップ {#new-braze-partnerships}

### Nexla - ワークフローオートメーション {#nexla-workflow-automation}

[Nexla]({{site.baseurl}}/partners/nexla)は、統合データオペレーションのリーダーであり、2021年のGartner Cool Vendorに選ばれています。Currentsを使用してデータウェアハウスにデータを送信しているお客様は、Nexlaを活用してそのデータの抽出、変換、読み込みを他の場所に行い、エコシステム全体でデータに簡単にアクセスできるようになります。Nexlaを使用すると、Braze Currentsを通じてカスタム形式のデータを、シンプルなポイント＆クリック操作でお好みの送信先に配信できます。

### Amperity - 顧客データプラットフォーム {#amperity-customer-data-platform}

[Amperity]({{site.baseurl}}/partners/amperity)は、包括的なエンタープライズ顧客データプラットフォームであり、ブランドが顧客をより深く理解し、戦略的な意思決定を行い、消費者により良いサービスを提供するための適切なアクションを一貫して実行できるよう支援します。AmperityはCDPとBraze全体で顧客の統一ビューを提供することでBrazeプラットフォームをサポートし、貴重なAmperityデータをBrazeに送信できるようにします。

### Digioh - アンケート {#digioh-surveys}

[Digioh]({{site.baseurl}}/partners/digioh)は、リストの拡大、ファーストパーティデータの取得、そしてBrazeキャンペーンでのデータ活用を支援します。ドラッグ＆ドロップビルダーにより、ブランドに合ったフォーム、ポップアップ、ユーザー設定センター、ランディングページ、アンケートを簡単に作成し、顧客とつながることができます。

### AppsFlyer Audiences - アトリビューション／分析 {#appsflyer-audiences-attributionanalytics}

[AppsFlyer]({{site.baseurl}}/partners/message_orchestration/attribution/appsflyer)は、モバイルマーケティング分析とアトリビューションのプラットフォームであり、マーケティング分析、モバイルアトリビューション、ディープリンクを通じてアプリの分析と最適化を支援します。[AppsFlyer Audiences]({{site.baseurl}}/partners/appsflyer_audiences)を使用すると、オーディエンスセグメントを構築し、それらのセグメントをBrazeに直接送信して、強力なカスタマーエンゲージメントキャンペーンを作成できます。