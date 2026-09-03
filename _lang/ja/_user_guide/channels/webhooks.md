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

Webhookの利用可否はBrazeパッケージによって異なります。開始するには、アカウントマネージャーまたはカスタマーサクセスマネージャーにお問い合わせください。

## ユースケース {#use-cases}

Webhookはシステム同士を連携させる優れた方法です。結局のところ、Webhookはアプリが通信する手段です。以下は、Webhookが特に役立つ一般的なシナリオです。

- Brazeとの間でデータを送受信する
- Brazeが直接サポートしていないチャネルを通じて顧客にメッセージを送信する
- Braze APIにリクエストを送信する

より具体的なユースケースには次のようなものがあります。

- webhookとキャンバスを使用して[リードスコアリングワークフロー]({{site.baseurl}}/user_guide/get_started/b2b_use_cases/lead_scoring)を作成し、リードを評価してルーティングします。
- ユーザーがメールを購読解除した場合、Webhookを使用してその同じ情報で分析データベースやCRMを更新し、そのユーザーの行動を包括的に把握できるようにします。
- Facebook MessengerやLineを通じて、ユーザーに[トランザクションメッセージ]({{site.baseurl}}/user_guide/channels/transactional_email/create_a_transactional_email)を送信します。
- Webhookを使用して[Lob.com]({{site.baseurl}}/partners/additional_channels_and_extensions/additional_channels/direct_mail/lob)などのサードパーティサービスと通信し、アプリ内およびWebでのアクティビティに応じて顧客にダイレクトメールを送信します。
- ゲーマーが特定のレベルに達したり、一定のポイントを獲得した場合、Webhookと既存のAPIセットアップを使用して、キャラクターのアップグレードやコインを直接そのアカウントに送信します。Webhookをマルチチャネルメッセージングキャンペーンの一部として送信すれば、プッシュ通知やその他のメッセージを同時に送信して、ゲーマーに報酬を知らせることもできます。
- 航空会社の場合、Webhookと既存のAPIセットアップを使用して、顧客が一定回数のフライトを予約した後にそのアカウントに割引を付与できます。
- 無限の「If This Then That」（[IFTTT](https://ifttt.com/about)）レシピ。たとえば、顧客がメールでアプリにサインインした場合、そのアドレスを自動的にSalesforceに設定できます。

## Webhookのエラーハンドリングとレート制限 {#webhook-error-handling-and-rate-limiting}

Brazeは、特定のHTTPレスポンス（例：`408`、`429`、`5XX`）に対してのみWebhookの配信をリトライします。`401 Unauthorized`やその他の`4XX`エラーを含む、ほとんどのレスポンスはリトライされません。`Retry-After`や`X-Rate-Limit-*`などのレスポンスヘッダーは、**レスポンスがすでにリトライ対象である場合に**バックオフのタイミングに影響を与えることがありますが、リトライ対象セット以外のエラーに対してBrazeがリトライを行うことはありません。

レスポンスコードの一覧表、リトライの制限、タイムアウトの動作については、[レスポンスコードとリトライロジック]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook#response-codes-and-retry-logic)を参照してください。

特定のホストへのWebhookリクエストの大部分が失敗している場合、Brazeはそのホストへのすべての送信試行を一時的に保留します。定義されたクールダウン期間の後に送信が再開され、お客様のシステムが回復できるようになります。

## BrazeパートナーとのWebhookの活用 {#utilizing-webhooks}

Webhookの活用方法は多数あり、テクノロジーパートナー（Alloys）を利用すれば、Webhookを使って顧客やユーザーとのコミュニケーションを直接レベルアップできます。

以下をご覧ください。
* [Messenger]({{site.baseurl}}/partners/additional_channels_and_extensions/additional_channels/instant_chat/messenger)
* [Remerge]({{site.baseurl}}/partners/remerge)
* [Lob.com]({{site.baseurl}}/partners/additional_channels_and_extensions/additional_channels/direct_mail/lob)
* その他多数の[テクノロジーパートナー]({{site.baseurl}}/partners/home)もご確認ください。

## 次のステップ {#next-steps}

{% article_tiles %}
- name: Webhookを作成する
  link: /docs/user_guide/channels/webhooks/create_a_webhook
  description: カスタムイベントでトリガーされるWebhookを設定し、外部エンドポイントにデータを送信します。
- name: Braze間Webhookの作成
  link: /docs/user_guide/channels/webhooks/use_case_create_a_braze_to_braze_webhook
  description: キャンペーンやキャンバスからBraze APIにポストします。
{% endarticle_tiles %}