---
nav_title: Validity
article_title: Validity
alias: /partners/validity/
description: "このリファレンス記事では、BrazeとValidity（メール到達性プラットフォーム）のパートナーシップについて説明します。Validityは、EverestシードリストをBrazeに同期し、キャンペーンやキャンバスの受信トレイ配置テストを自動化します。"
page_type: partner
search_tag: Partner
---

# Validity

> [Validity Everest](https://www.validity.com/everest/)は、受信トレイへの配置を測定し、送信レピュテーションを保護するメール到達性プラットフォームです。BrazeとValidityの統合により、EverestシードリストをBrazeに同期し、条件を満たすキャンペーンやキャンバスに自動的にシードを送信し、エンゲージメント指標をValidity Inboxに取り込むことで、シードベースの配置と実際の購読者エンゲージメントを比較できます。

_この統合はValidityによって管理されています。_

## 統合について {#about-the-integration}

Validityは、Brazeでメールシードリストユーザーを作成・管理し、シードアドレスがアクティブかつ抑制されていない状態を維持します。キャンペーンまたはキャンバスにシードを送信する準備ができると、Validityはそのシードリストにコピーを送信し、配信、バウンス、開封、クリック、購読解除などのエンゲージメント指標を、受信トレイ配置データとともにValidity Inboxに表示します。

## ユースケース {#use-cases}

### 自動シーディング {#auto-seeding}

Validityの自動シーディングでは、Brazeのキャンペーンまたはキャンバスが条件を満たす送信量に達したことを検出し、そのキャンペーンのコンテンツのコピーをValidityシードリストに送信します。シード送信は、`validity_seed`カスタム属性が`true`に設定されているユーザーを対象とします。

## 前提条件 {#prerequisites}

開始する前に、以下が必要です。

| 要件 | 説明 |
| ----------- | ----------- |
| Validityアカウント | このパートナーシップを利用するには、Validityアカウントが必要です。 |
| Braze REST APIキー | 以下の権限を持つBraze REST APIキー：`users.track`、`users.delete`、`email.bounce.remove`、`email.spam.remove`、`campaigns.list`、`campaigns.details`、`campaigns.data_series`、`canvas.list`、`canvas.details`、`canvas.data_series`、`content_blocks.list`、`content_blocks.info`、`messages.send`。<br><br> このキーは、Brazeダッシュボードの**設定** > **APIと識別子**から作成します。 |
| Braze RESTエンドポイント | [RESTエンドポイントURL]({{site.baseurl}}/api/basics#endpoints)。エンドポイントは、お使いのインスタンスのBraze URLによって異なります。例：`rest.iad-01.braze.com`。 |
| Brazeアプリ識別子 | シード送信を帰属させるBrazeアプリ識別子。**設定** > **APIと識別子** > **アプリ識別子**で確認できます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## Validityの統合 {#integrating-validity}

### ステップ1：Brazeの認証情報をValidityと共有する {#step-1-share-braze-credentials-with-validity}

Validityには、Brazeダッシュボードの**設定** > **APIと識別子**から以下の3つの認証情報が必要です。

- REST APIキー（[前提条件](#prerequisites)に記載されている権限を含む）
- RESTエンドポイント
- アプリ識別子

これらの認証情報をValidityの担当者と共有してください。担当者が統合の設定を完了します。Validityは、統合を有効にする前に、Brazeへのライブテストコールで認証情報を検証します。Validityの連絡先が不明な場合は、[support@validity.com](mailto:support@validity.com)にメールしてください。

統合が有効になると、Validityは定期的なサイクル（10分ごと）でEverestシードリストをBrazeに同期します。Validityは、Brazeでシードユーザーを作成、更新、削除し、Everestの現在のシードリストと整合性を保ちます。

### ステップ2：Validityシードユーザー用のBrazeセグメントを作成する（オプション） {#step-2-optionally-create-a-braze-segment-for-validity-seed-users}

セグメントの作成はオプションです。自動シーディングは、条件を満たす送信が検出されるたびに、`validity_seed`カスタム属性でフィルタリングされた[Connected Audience]({{site.baseurl}}/api/objects_filters/connected_audience)オブジェクトを使用してテストメールを送信します。セグメントを作成したり、キャンペーンに添付したりする必要はありません。

Braze内でこのオーディエンスを参照用に表示したい場合は、**オーディエンス** > **セグメント**で`validity_seed`が`true`のフィルターを使用してセグメントを作成してください。

Validityは、以下のスキーマを使用して[`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track)エンドポイントでユーザーを作成します。

```bash
curl -X POST "https://YOUR_API_ENDPOINT/users/track" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_BRAZE_API_KEY" \
  -d '{
    "attributes": [
      {
        "email": "example1@example.com",
        "validity_seed": true
      },
      {
        "email": "example2@example.com",
        "validity_seed": true
      }
    ],
    "events": [
      {
        "email": "example1@example.com",
        "name": "validity_seed_event",
        "time": "2026-07-02T18:00:00.000Z"
      }
    ]
  }'
```

これらのユーザーには、常にブール値`true`のカスタム属性`validity_seed`が含まれます。Validityは、各シードユーザーに対して`validity_seed_event`カスタムイベントも送信し、Brazeアカウントでアクティブユーザーとして登録されるようにします。

## 考慮事項 {#considerations}

### シード送信の仕組み {#how-seed-sends-work}

Validityは、キャンペーンおよびキャンバスの詳細エンドポイントを通じてキャンペーンの本文、件名、差出人アドレスを取得し、Brazeの[`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages)エンドポイントを通じてそのコンテンツのコピーをシードリストに配信します。Brazeダッシュボードには、引き続き元のキャンペーンのみが表示されます。

### 自動シーディングのしきい値 {#auto-seeding-threshold}

Validityは、キャンペーンまたはキャンバスが設定された送信量のしきい値（デフォルトでは10,000送信）を超えたことを検出し、その時点でシードテストを送信します。キャンペーンやキャンバスにシードオーディエンスを追加する必要はありません。

シードテストは、シードリスト上のアドレスにメールキャンペーンを送信し、配置データを収集し、オーディエンスへの送信前または送信と並行して問題を特定するのに役立ちます。受信トレイ配置指標は、キャンペーンが受信トレイ、スパムフォルダー、または未着のいずれに分類されたかを示します。これらの指標を使用して、受信トレイへの配置を確認し、到達性の問題を検出してください。

シードテストは、メールがスパムフォルダーに入ったり未着になったりする原因の診断にも役立ちます。ヘッダーデータ、認証（SPF、DKIM、DMARC）、リンク検証、デザインレンダリングを確認することで、受信トレイ配置率を改善するための手順を把握できます。

### シードリストの健全性 {#seed-list-health}

Validityはシードリストユーザーを監視し、効果が低下し始めた場合（例えば、メールサービスプロバイダー（ESP）がシードリストのオーディエンスメンバーをスパムとしてフラグし始めた場合など）に更新または削除することがあります。これらの権限により、Validityはシードリストの健全性を監視し、リストを適切に更新できます。

### ダイナミックコンテンツの処理方法 {#how-dynamic-content-is-handled}

Brazeのメールでは、実際の受信者のプロファイルに紐づいたLiquidパーソナライゼーションがよく使用されます。シードアドレスにはそのプロファイルデータがないため、Validityはシーディング前に各メールをサニタイザーで処理します。サニタイザーはContent Blocksを解決し、基本的なLiquidロジックを評価し、解決できないもの（名など）を表示可能な`[REDACTED]`プレースホルダーに置き換えます。ライブConnected Content APIのみで構築されたセクションは、シードでは空白で表示されます。

サニタイザーはオン・オフを切り替えることができます。オフにすると、Brazeはシード送信のLiquidパーソナライゼーションを、実際の受信者と同じ方法で解決します。

### Inbox Aggregate

自動シーディングを有効にすると、Inbox Aggregateも有効になります。この機能は、実際のBraze送信（シード送信とは別）からエンゲージメント指標（送信、配信、バウンス、開封、クリック、購読解除）を取得し、受信トレイ配置データとともにValidity Inboxに表示します。2つの機能は独立したスケジュールで実行され、個別に管理する必要はありません。