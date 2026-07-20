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

## インテグレーションについて {#about-the-integration}

Chordは、ストアとBrazeの間のデータレイヤーとして機能します。Chord CDPでBrazeを送信先として接続すると、ChordはトラッキングプランのイベントをBrazeにマッピングします。そのデータをセグメント、キャンバス、メッセージパーソナライゼーションで使用して、消費者がサイト上で行っていることを反映できます。

## 前提条件 {#prerequisites}

ChordとBrazeを接続する前に、以下を確認してください。

| 要件 | 説明 |
| ----------- | ----------- |
| Chordアカウント | このインテグレーションを使用するにはChordアカウントが必要です。 |
| Braze API認証情報 | 必要な認証情報は[接続モード](#connection-modes)によって異なります。クラウドモードではBraze REST APIキーを使用します。デバイスモードではBraze SDK用のWebチャネルAPIキーを使用し、これはREST APIキーとは別のものです。 |
| Braze RESTエンドポイント | Chordはサーバーサイドデータを[`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)および[`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/)エンドポイントに送信します。ベースURLはBrazeインスタンスに従います（例：`https://rest.iad-01.braze.com`）。詳細については、[Braze REST APIエンドポイント]({{site.baseurl}}/api/basics/#endpoints)を参照してください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requirements" }

## 接続モード {#connection-modes}

Chordはクラウドモード（Braze REST APIを介したサーバー間呼び出し）とデバイスモード（ChordがBraze Web SDKを初期化し、マッピングされた呼び出しを転送）をサポートしています。完全なWeb SDK機能（例：アプリ内メッセージ）が必要か、サーバーサイドのイベント転送のみが必要かに応じてモードを選択してください。

### クラウドモード {#cloud-mode}

1. Chordデータプラットフォームで、CDPを開き**Destinations**に移動します。
2. Destinationsの横にある**Add**を選択し、カタログから**Braze**を選択して、送信先名とBraze REST APIキーを入力します。
3. 送信先を作成して接続を完了します。

REST APIキーはBrazeダッシュボードの**設定** > **API キー**から作成します。古いナビゲーションを使用している場合は、**開発者コンソール** > **API 設定**に移動してください。Chordがワークスペースに対して異なる要件を文書化していない限り、キーには`users.track`と`users.identify`の権限が必要です。詳細については、[APIキー]({{site.baseurl}}/api/api_key/)を参照してください。

### デバイスモード {#device-mode}

1. Chordデータプラットフォームで、CDPを開き**Destinations**に移動します。
2. Destinationsの横にある**Add**を選択し、カタログから**Braze (device mode)**を選択して、送信先名とWebチャネルAPIキーを入力します。
3. 送信先を作成して接続を完了します。

WebチャネルAPIキーはBrazeダッシュボードの**Settings** > **App Settings** > **Web** > **API Key**から取得します。デバイスモードにはREST APIキーを使用しないでください。

### デバイスモードの設定 {#device-mode-configuration}

Chordの送信先設定で、以下を設定します。

- **Braze Web SDKバージョン：** ChordはCDPで選択可能なSDKバージョンを公開しています。利用可能な範囲はChordのドキュメントで確認してください。
- **SDKエンドポイント：** Brazeインスタンスと一致する必要があります。詳細については、[APIおよびSDKエンドポイント]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints/)を参照してください。
- **イベントおよびSDKオプション：** 例えば、送信するtrackまたはidentifyの動作、ページイベントの処理、アプリ内メッセージの動作、SDK初期化のタイミング、同意関連の設定などです。

## イベントマッピング（デバイスモード） {#event-mapping-device-mode}

デバイスモードを使用する場合、Chordはイベントを以下の表のようにBrazeにマッピングします。

| Chord | Braze |
| ----- | ----- |
| Order completed | `logPurchase` |
| その他の`track`イベント | `logCustomEvent` |
| Identify | ユーザー更新（例：SDKユーザーオブジェクトを介した属性） |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Chordトラッキングプランに含まれ、Braze送信先に設定されたイベントのみが転送されます。

## インテグレーションの使用 {#using-the-integration}

### ステップ1：Brazeでイベントを確認する {#step-1-confirm-events-in-braze}

データが流れ始めたら、Brazeでユーザープロファイルまたはイベントツールを開き、イベントと属性が期待どおりに到着していることを確認します。

### ステップ2：オーディエンスとジャーニーを構築する {#step-2-build-audiences-and-journeys}

同期されたイベントと属性を[セグメント]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment/)、[キャンバス]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/)、キャンペーンで使用して、ストアの行動に基づいて消費者をターゲティングします。

## ユースケース {#use-cases}

- **購入後メッセージング：** Chordが完了した注文を受信したときに、確認、クロスセル、またはレビューリクエストをトリガーします。
- **プロファイルエンリッチメント：** Chordからの最新の消費者プロファイルデータとBrazeの属性を同期させ、よりクリーンなセグメンテーションを実現します。
- **行動リターゲティング：** Chordの行動イベントを使用して、最近購入やコンバージョンを行っていない消費者に再エンゲージします。

## 考慮事項 {#considerations}

{% alert important %}
別のツールが既に同じイベントをBrazeに送信している場合は、Chord CDPを通じてBrazeを接続する前に、そのインテグレーションの管理者と調整してください。並行して送信先を実行すると、ダウンストリームで重複イベントが発生する可能性があります。
{% endalert %}

## トラブルシューティング {#troubleshooting}

イベントがBrazeに表示されない場合：

1. Chord CDPで、ソースからライブイベントが到着していることを確認します。
2. Braze送信先が正しいAPIキー、SDKバージョン（デバイスモード）、およびインスタンスに対応するRESTまたはSDKエンドポイントを使用していることを確認します。
3. 送信先がChordで期待されるソースに接続されていることを確認します。
4. Chordで、API送信先またはファンクションログを確認し、`/users/track`および`/users/identify`への呼び出しが成功していることを確認してから、Brazeで再度確認します。

Chord固有のログの場所とUIの手順については、[Chord Brazeインテグレーション](https://docs.chord.co/braze#chord-x-braze-integration)を参照してください。