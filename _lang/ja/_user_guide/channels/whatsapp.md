---
nav_title: WhatsApp
article_title: WhatsApp
page_order: 10
page_type: landing
channel:
  - WhatsApp
search_rank: 3
description: "Brazeを通じて、サポート、通知、プロモーションキャンペーンのためにパーソナライズされたWhatsAppメッセージで顧客にリーチできます。"
alias: /whatsapp/
---

# WhatsApp

> WhatsAppは、世界中で利用されているピアツーピアメッセージングプラットフォームで、ビジネス向けの会話ベースのメッセージングを提供しています。BrazeのWhatsAppチャネルを使用すると、ユーザーが日常的に利用しているスレッド型の会話を通じて、サポートメッセージ、通知、プロモーションキャンペーンを送信できます。このハブでは、WhatsAppのセットアップ、メッセージタイプ、テンプレート、購読管理、レポートについて説明します。まず[WhatsAppセットアップ]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup)でMeta BusinessアカウントとWhatsApp Businessアカウントを接続し、最初のテンプレートベースのメッセージを作成してください。新規ユーザーにプロモーションメッセージを送信する前に、[オプトインとオプトアウト]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/opt_ins_and_opt_outs)を確認してください。

## 前提条件 {#prerequisites}

WhatsAppの利用可否は、Brazeパッケージによって異なります。利用を開始するには、アカウントマネージャーまたはカスタマーサクセスマネージャーにお問い合わせください。

開始する前に、以下の事項を確認してください。

- Meta Business Managerアカウントおよび WhatsApp Businessアカウント
- [Cloud API](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers)の要件を満たすWhatsApp電話番号

詳細な手順については、[WhatsAppセットアップ]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup)を参照してください。

## ユースケース {#use-cases}

| ユースケース | 説明 |
| --- | --- |
| カスタマーサポート | リアルタイムの双方向会話を実現し、問い合わせへの対応、問題のトラブルシューティング、パーソナライズされたアシスタンスを提供します。 |
| 注文通知 | 注文確認、配送状況の更新、配達通知をWhatsApp上で直接顧客に送信します。 |
| 予約リマインダー | タイムリーな予約リマインダーでノーショーを削減し、顧客が確認やリスケジュールを行えるようにします。 |
| プロモーションキャンペーン | ターゲティングされたプロモーション、製品発表、パーソナライズされたオファーをリッチメディアメッセージで顧客に届けます。 |
| 双方向会話 | 顧客が返信、質問、フィードバックの提供を行えるインタラクティブなメッセージングで、より深い関係を構築します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ユースケース" }

## よくある質問 {#frequently-asked-questions}

### WhatsAppをBrazeに接続するにはどうすればよいですか？ {#how-do-i-connect-whatsapp-to-braze}

Meta Business Managerアカウントと WhatsApp Businessアカウントを作成し、[WhatsAppセットアップ]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup)のステップを完了してください。

### WhatsAppではどのようなメッセージタイプを送信できますか？ {#what-message-types-can-i-send-on-whatsapp}

アウトバウンドメッセージには承認済みテンプレートを使用し、双方向の会話にはサポートされているセッションメッセージを使用します。サポートされているメッセージタイプについては、[WhatsAppメッセージの作成]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message)を参照してください。

### ユーザーはWhatsAppメッセージのオプトインが必要ですか？ {#do-users-need-to-opt-in-to-whatsapp-messages}

はい。プロモーションまたは定期的なWhatsAppメッセージを送信する前に、ユーザーのオプトインを取得する必要があります。購読の管理については、[オプトインとオプトアウト]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/opt_ins_and_opt_outs)を参照してください。

## 次のステップ {#next-steps}

- [WhatsAppセットアップ]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup)
- [WhatsAppメッセージを作成する]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message)