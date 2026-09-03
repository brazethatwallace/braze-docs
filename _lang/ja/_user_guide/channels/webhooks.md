---
nav_title: Webhook
article_title: Webhook
page_order: 9
page_type: landing
alias: /about_webhooks/
description: "カスタムイベントをトリガーとするBrazeのWebhookでシステムを接続し、外部エンドポイントにデータやプログラムによるメッセージを送信できます。"
channel:
  - webhooks
search_rank: 3
---

# Webhook {#webhooks}

> Webhookとは、特定の条件が満たされたときに、あるシステムから別のシステムへ自動的に送信されるメッセージです。Brazeでは、この条件は通常カスタムイベントのトリガーです。Webhookはデータやプログラム機能へのダイナミックかつ柔軟なアクセスを提供し、プロセスを効率化するカスタマージャーニーの構築を可能にします。

## 前提条件 {#prerequisites}

Webhookの利用可能性は、お客様のBrazeパッケージによって異なります。開始するには、アカウントマネージャーまたはカスタマーサクセスマネージャーにお問い合わせください。

## ユースケース {#use-cases}

Webhookは、システム同士を接続する優れた方法です。そもそもWebhookとは、アプリケーション同士がコミュニケーションする仕組みです。以下に、Webhookが特に役立つ一般的なシナリオを紹介します。

- Brazeとの間でデータを送受信する
- Brazeが直接サポートしていないチャネルを通じて顧客にメッセージを送信する
- Braze APIにリクエストを送信する

より具体的なユースケースには、以下のようなものがあります。

- Webhookとキャンバスを使用して[リードスコアリングワークフロー]({{site.baseurl}}/user_guide/get_started/b2b_use_cases/lead_scoring)を作成し、リードの評価とルーティングを行います。
- ユーザーがメールの購読解除を行った場合、Webhookを使用して同じ情報で分析データベースやCRMを更新し、そのユーザーの行動を包括的に把握できるようにします。
- Facebook MessengerやLineを通じてユーザーに[トランザクションメッセージ]({{site.baseurl}}/user_guide/channels/transactional_email/create_a_transactional_email)を送信します。
- Webhookを使用して[Lob.com]({{site.baseurl}}/partners/additional_channels_and_extensions/additional_channels/direct_mail/lob)などのサードパーティサービスと通信し、アプリ内やWebでのアクティビティに応じて顧客にダイレクトメールを送信します。
- ゲーマーが特定のレベルに到達したり、一定のポイントを獲得した場合、Webhookと既存のAPIセットアップを使用して、キャラクターのアップグレードやコインを直接アカウントに送信できます。Webhookをマルチチャネルメッセージングキャンペーンの一部として送信すれば、プッシュ通知やその他のメッセージを送信して、報酬についてゲーマーに同時に通知することもできます。
- 航空会社の場合、Webhookと既存のAPIセットアップを使用して、顧客が一定数のフライトを予約した後に割引をアカウントに付与できます。
- 無限に広がる「If This Then That」（[IFTTT](https://ifttt.com/about)）レシピ。たとえば、顧客がメールでアプリにサインインした場合、そのアドレスを自動的にSalesforceに設定できます。

## Webhookのエラー処理とレート制限 {#webhook-error-handling-and-rate-limiting}

Brazeは、特定のHTTPレスポンス（たとえば`408`、`429`、`5XX`）に対してのみWebhookの配信をリトライします。`401 Unauthorized`やその他の`4XX`エラーを含むほとんどのレスポンスはリトライされません。`Retry-After`や`X-Rate-Limit-*`などのレスポンスヘッダーは、**レスポンスがすでにリトライ対象である場合に**バックオフのタイミングに影響を与えることがありますが、リトライ対象外のエラーに対してBrazeがリトライを行うようにはなりません。

レスポンスコードの一覧表、リトライ制限、タイムアウトの動作については、[レスポンスコードとリトライロジック]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook#response-codes-and-retry-logic)を参照してください。

特定のホストへのWebhookリクエストの大半が失敗している場合、Brazeはそのホストへのすべての送信試行を一時的に保留します。定義されたクールダウン期間の後に送信が再開され、システムが回復できるようになります。

## BrazeパートナーとのWebhookの活用 {#utilizing-webhooks}

Webhookの活用方法は多数あり、テクノロジーパートナー（Alloys）を利用すれば、Webhookを使って顧客やユーザーとのコミュニケーションを直接レベルアップできます。

以下をご覧ください。
* [Messenger]({{site.baseurl}}/partners/additional_channels_and_extensions/additional_channels/instant_chat/messenger)
* [Remerge]({{site.baseurl}}/partners/remerge)
* [Lob.com]({{site.baseurl}}/partners/additional_channels_and_extensions/additional_channels/direct_mail/lob)
* その他多数の[テクノロジーパートナー]({{site.baseurl}}/partners/home)もご確認ください。

## 次のステップ {#next-steps}

- [Webhookを作成する]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook)
- [Braze間Webhookの作成]({{site.baseurl}}/user_guide/channels/webhooks/use_case_create_a_braze_to_braze_webhook)