---
nav_title: Webhook
article_title: Webhook
page_order: 9
page_type: landing
alias: /about_webhooks/
description: "カスタムイベントをトリガーとするBrazeのwebhookでシステムを接続し、外部エンドポイントにデータやプログラムによるメッセージを送信できます。"
channel:
  - webhooks
search_rank: 3
---

# Webhook {#webhooks}

> Webhookとは、特定の条件が満たされたときに、あるシステムから別のシステムへ自動的に送信されるメッセージです。Brazeでは、この条件は通常カスタムイベントのトリガーです。Webhookはデータやプログラム機能へのダイナミックかつ柔軟なアクセスを提供し、プロセスを効率化するカスタマージャーニーの構築を可能にします。

## 前提条件 {#prerequisites}

Webhookの利用可否はBrazeのパッケージによって異なります。開始するには、アカウントマネージャーまたはカスタマーサクセスマネージャーにお問い合わせください。

## ユースケース {#use-cases}

Webhookはシステム同士を接続する優れた方法です。そもそもwebhookはアプリ同士が通信する手段です。以下は、webhookが特に役立つ一般的なシナリオです。

- Brazeとの間でデータを送受信する
- Brazeが直接サポートしていないチャネルを通じて顧客にメッセージを送信する
- Braze APIにポストする

より具体的なユースケースには以下のようなものがあります。

- webhookとキャンバスを使用して[リードスコアリングワークフロー]({{site.baseurl}}/user_guide/get_started/b2b_use_cases/lead_scoring/)を作成し、リードの評価とルーティングを行います。
- ユーザーがメールの配信停止を行った場合、webhookを使用して分析データベースやCRMに同じ情報を更新し、そのユーザーの動作を包括的に把握できるようにします。
- Facebook MessengerやLine内のユーザーに[トランザクションメッセージ]({{site.baseurl}}/api/api_campaigns/transactional_api_campaign/)を送信します。
- [Lob.com]({{site.baseurl}}/partners/additional_channels_and_extensions/additional_channels/direct_mail/lob/)などのサードパーティサービスとの通信にwebhookを使用して、アプリ内およびWebアクティビティに応じてダイレクトメールを顧客に送信します。
- ゲーマーが特定のレベルに到達したり、一定のポイントを獲得した場合、webhookと既存のAPIセットアップを使用して、キャラクターのアップグレードやコインを直接アカウントに送信できます。マルチチャネルメッセージングキャンペーンの一部としてwebhookを送信すれば、プッシュ通知やその他のメッセージを送信して、報酬についてゲーマーに同時に知らせることができます。
- 航空会社の場合、webhookと既存のAPIセットアップを使用して、顧客が一定数のフライトを予約した後に割引をアカウントに付与できます。
- 無限の「If This Then That」（[IFTTT](https://ifttt.com/about)）レシピ。例えば、顧客がメールでアプリにサインインした場合、そのアドレスを自動的にSalesforceに設定できます。

## Webhookのエラー処理とレート制限 {#webhook-error-handling-and-rate-limiting}

Brazeは特定のHTTPレスポンス（例：`408`、`429`、`5XX`）に対してのみwebhookの配信をリトライします。`401 Unauthorized`やその他の`4XX`エラーを含むほとんどのレスポンスはリトライされません。`Retry-After`や`X-Rate-Limit-*`などのレスポンスヘッダーは、**レスポンスがすでにリトライ対象である場合に**バックオフのタイミングに影響を与えることがありますが、リトライ対象外のエラーに対してBrazeがリトライを行うことはありません。

レスポンスコードの完全な一覧表、リトライ制限、タイムアウトの動作については、[レスポンスコードとリトライロジック]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook/#response-codes-and-retry-logic)を参照してください。

特定のホストへのwebhookリクエストの大部分が失敗している場合、Brazeはそのホストへのすべての送信試行を一時的に延期します。定義されたクールダウン期間の後に送信が再開され、システムの回復が可能になります。

## Brazeパートナーとのwebhookの活用 {#utilizing-webhooks}

Webhookの活用方法は多数あり、テクノロジーパートナー（Alloys）を利用すれば、webhookを使って顧客やユーザーとのコミュニケーションを直接レベルアップできます。

以下をご覧ください。
* [Messenger]({{site.baseurl}}/partners/additional_channels_and_extensions/additional_channels/instant_chat/messenger/)
* [Remerge]({{site.baseurl}}/partners/remerge/)
* [Lob.com]({{site.baseurl}}/partners/additional_channels_and_extensions/additional_channels/direct_mail/lob/)
* その他多数の[テクノロジーパートナー]({{site.baseurl}}/partners/home/)もご確認ください。

## 次のステップ {#next-steps}

- [Webhookを作成する]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook/)
- [Braze間webhookを作成する]({{site.baseurl}}/user_guide/channels/webhooks/use_case_create_a_braze_to_braze_webhook/)