---
nav_title: トランザクションメール
article_title: トランザクションメール
page_order: 4
page_type: landing
channel:
  - email
search_rank: 3
description: "BrazeでAPI呼び出しによってトリガーされる重要かつ時間的制約のある通知のために、トランザクションメールを送信します。"
---

# トランザクションメール {#transactional-email}

> トランザクションメールは、お客様と顧客の間で合意された取引を円滑に進めるために、自動化された非プロモーションメッセージを送信する目的で構築されています。Brazeのトランザクションメールキャンペーンを使用して、注文確認、パスワードリセット、配送状況の更新など、API呼び出しによってトリガーされる重要かつ時間的制約のある通知を送信できます。

## 前提条件 {#prerequisites}

トランザクションメールは、特定のBrazeパッケージの一部としてのみ利用可能です。詳細については、Brazeカスタマーサクセスマネージャーに連絡するか、[サポートチケット]({{site.baseurl}}/braze_support/)を開いてください。

開始する前に、以下を準備してください。

- IP・ドメイン設定、認証、IPウォーミングを含む[メールセットアップ]({{site.baseurl}}/user_guide/channels/email/email_setup/)の完了
- `transactional.send`権限を持つ**Braze REST APIキー**

## ユースケース {#use-cases}

トランザクションメールは、非プロモーションのサービストリガーメッセージを送信するために設計されています。一般的なユースケースには以下が含まれます。

| ユースケース | 説明 |
| --- | --- |
| 注文確認 | 顧客の購入が受領され、処理中であることを確認します。 |
| パスワードリセット | 顧客がアカウントの認証情報をリセットするための安全で時間的制約のあるリンクを配信します。 |
| 配送通知 | トラッキング情報や配達予定日を含め、注文が発送されたことを顧客に通知します。 |
| アカウントアラート | 支払い失敗、サブスクリプション変更、セキュリティアラートなど、重要なアカウント関連の通知を送信します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Use cases" }

## トランザクションメールとマーケティングメールの違い {#how-transactional-email-differs-from-marketing-email}

トランザクションメールは、速度と信頼性に最適化された専用のBraze[トランザクションHTTP API]({{site.baseurl}}/api/api_campaigns/transactional_api_campaign/)を通じて送信されます。マーケティングメールとは異なり、トランザクションメールには以下の特徴があります。

- マーケティングコミュニケーションへのオプトインを必要としません
- スケジュールやアクションベースのトリガーではなく、API呼び出しによってトリガーされます
- 時間的制約のあるコンテンツに対して、ほぼリアルタイムの配信をサポートします

## 次のステップ {#next-steps}

- [トランザクションメールの作成]({{site.baseurl}}/user_guide/channels/transactional_email/create_a_transactional_email/)
- [トラッキング]({{site.baseurl}}/user_guide/channels/transactional_email/tracking/)