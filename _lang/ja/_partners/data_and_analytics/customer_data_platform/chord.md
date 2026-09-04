---
nav_title: Chord
article_title: Chord
description: "Chord顧客データプラットフォーム（CDP）をBrazeに接続し、eコマースイベントやID更新をメッセージング、セグメンテーション、ジャーニーに転送します。"
alias: /partners/chord/
page_type: partner
search_tag: Partner
---

# Chord

> [Chord](https://www.chord.co/)は、eコマースストアフロントからイベントをキャプチャし標準化する顧客データプラットフォームを提供します。ChordをBrazeに接続すると、購入アクティビティ、行動イベント、ID更新がBrazeに流れ込み、パイプラインを自分で構築することなくキャンペーンをトリガーしたりプロファイルを最新の状態に保つことができます。

_このインテグレーションはChordによって管理されています。_

セットアップ、接続オプション、フィールドリストの詳細については、[Chord Brazeインテグレーション](https://docs.chord.co/braze#chord-x-braze-integration)を参照してください。

## 連携について {#about-the-integration}

ChordはストアとBrazeの間のデータレイヤーとして機能します。Chord CDPでBrazeを送信先として接続すると、ChordはトラッキングプランのイベントをBrazeにマッピングします。このデータをセグメント、キャンバス、メッセージのパーソナライゼーションで活用し、消費者がサイト上で行っていることを反映させましょう。

## 前提条件 {#prerequisites}

Chord と Braze を接続する前に、以下の要件を確認してください。

| 要件 | 説明 |
| ----------- | ----------- |
| Chord アカウント | このインテグレーションを使用するには、Chord アカウントが必要です。 |
| Braze API 認証情報 | 必要な認証情報は[接続モード](#connection-modes)によって異なります。クラウドモードでは Braze REST APIキーを使用します。デバイスモードでは Braze SDKの Web チャネル APIキーを使用しますが、これは REST APIキーとは別のものです。 |
| Braze REST エンドポイント | Chord はサーバーサイドデータを [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) および [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify) エンドポイントに送信します。ベース URL は Braze インスタンスに対応しています（例: `https://rest.iad-01.braze.com`）。詳細については、[Braze REST API エンドポイント]({{site.baseurl}}/api/basics#endpoints)を参照してください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="要件" }

## 接続モード {#connection-modes}

Chordは、クラウドモード（Braze REST APIを介したサーバー間通信）とデバイスモード（ChordがBraze Web SDKを初期化し、マッピングされた呼び出しを転送）をサポートしています。Web SDKの全機能（アプリ内メッセージなど）が必要か、サーバーサイドのイベント転送のみが必要かに応じて、適切なモードを選択してください。

### クラウドモード {#cloud-mode}

1. Chordデータプラットフォームで顧客データプラットフォームを開き、**送信先**に移動します。
2. 送信先の横にある**追加**を選択し、カタログから**Braze**を選択して、送信先名とBraze REST APIキーを入力します。
3. 送信先を作成して接続を完了します。

REST APIキーは、Brazeダッシュボードの**設定** > **APIキー**から作成します。古いナビゲーションを使用している場合は、**開発者コンソール** > **API設定**に移動してください。Chordがワークスペースに対して異なる要件を記載していない限り、キーには`users.track`と`users.identify`の権限が必要です。詳細については、[APIキー]({{site.baseurl}}/api/basics)を参照してください。

### デバイスモード {#device-mode}

1. Chordデータプラットフォームで顧客データプラットフォームを開き、**送信先**に移動します。
2. 送信先の横にある**追加**を選択し、カタログから**Braze（デバイスモード）**を選択して、送信先名とWebチャネルAPIキーを入力します。
3. 送信先を作成して接続を完了します。

WebチャネルAPIキーは、Brazeダッシュボードの**設定** > **アプリ設定** > **Web** > **APIキー**から取得します。デバイスモードにはREST APIキーを使用しないでください。

### デバイスモードの設定 {#device-mode-configuration}

Chordの送信先設定で、以下を構成します。

- **Braze Web SDKバージョン：** Chordは顧客データプラットフォームで選択可能なSDKバージョンを公開しています。利用可能な範囲についてはChordのドキュメントで確認してください。
- **SDKエンドポイント：** Brazeインスタンスと一致させる必要があります。詳細については、[APIおよびSDKエンドポイント]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints)を参照してください。
- **イベントおよびSDKオプション：** 例えば、送信するトラッキングまたは識別の動作、ページイベントの処理、アプリ内メッセージの動作、SDKの初期化タイミング、同意関連の設定などです。

## イベントマッピング（デバイスモード） {#event-mapping-device-mode}

デバイスモードを使用する場合、Chord はイベントを以下の表のとおり Braze にマッピングします。

| Chord | Braze |
| ----- | ----- |
| Order completed | `logPurchase` |
| その他の`track`イベント | `logCustomEvent` |
| Identify | ユーザー更新（例：SDKユーザーオブジェクトを通じた属性） |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Chord トラッキングプランに含まれ、Braze の送信先に設定されたイベントのみが転送されます。

## インテグレーションの使用 {#using-the-integration}

### ステップ1：Brazeでイベントを確認する {#step-1-confirm-events-in-braze}

データが流れ始めたら、Brazeでユーザープロファイルまたはイベントツールを開き、イベントと属性が期待どおりに届いていることを確認します。

### ステップ2：オーディエンスとジャーニーを構築する {#step-2-build-audiences-and-journeys}

同期されたイベントと属性を[セグメント]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment)、[キャンバス]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas)、キャンペーンで使用して、店舗での行動に基づいて消費者をターゲティングします。

## ユースケース {#use-cases}

- **購入後のメッセージング：** Chord が完了した注文を受信した際に、確認メッセージ、クロスセル、またはレビューリクエストをトリガーします。
- **プロファイルの強化：** よりクリーンなセグメンテーションのために、Braze属性を Chord の最新の消費者プロファイルデータと同期した状態に保ちます。
- **行動リターゲティング：** Chord の行動イベントを使用して、最近購入やコンバージョンを行っていない消費者にリエンゲージメントします。

## 考慮事項 {#considerations}

{% alert important %}
別のツールがすでに同じイベントをBrazeに送信している場合は、Chord顧客データプラットフォームを介してBrazeを接続する前に、そのインテグレーションの担当者と調整してください。並行して送信先を実行すると、下流で重複イベントが発生する可能性があります。
{% endalert %}

## トラブルシューティング {#troubleshooting}

Brazeにイベントが表示されない場合は、以下を確認してください。

1. Chord 顧客データプラットフォームで、ソースからライブイベントが到着していることを確認します。
2. Brazeの送信先が、インスタンスに対して正しいAPIキー、SDKバージョン（デバイスモード）、およびRESTまたはSDKエンドポイントを使用していることを確認します。
3. 送信先がChordで期待されるソースに接続されていることを確認します。
4. Chordで、APIの送信先またはファンクションログを確認し、`/users/track`および`/users/identify`への呼び出しが成功していることを確認してから、Brazeで再度確認します。

Chord固有のログの場所とUI手順については、[Chord Braze integration](https://docs.chord.co/braze#chord-x-braze-integration)を参照してください。