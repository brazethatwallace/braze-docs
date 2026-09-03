---
nav_title: "WhatsAppへ誘導する広告"
article_title: "WhatsAppへ誘導する広告"
page_order: 1
description: "このリファレンス記事では、WhatsAppへ誘導する広告の設定と使用方法をステップバイステップで説明します。"
page_type: reference
alias: /whatsapp_use_cases/
channel:
  - WhatsApp
---

# WhatsAppへ誘導する広告 {#ads-that-click-to-whatsapp}

> このページでは、WhatsAppへ誘導する広告の設定と使用方法をステップバイステップで説明します。これにより、チームのWhatsAppプログラムをさらに強化できます。

WhatsAppへ誘導する広告は、Facebook、Instagram、その他のプラットフォーム上のMeta広告から新規顧客と既存顧客の両方を獲得する効率的な方法です。これらの広告を使用して、製品やサービスを宣伝しながら、ユーザーにWhatsAppでの存在を知らせましょう。

![Calorie Rocketの無料配達を宣伝するFacebook広告と、ユーザーが広告のボタンを選択した際に表示されるWhatsApp会話。]({% image_buster /assets/img/whatsapp/ads_that_click_whatsapp.png %}){: style="max-width:70%;"}

## Click to WhatsApp広告の設定 {#setting-up-ads-that-click-to-whatsapp}

1. Meta広告マネージャーで、ステップバイステップガイド「[Click to WhatsApp広告の作成方法](https://business.whatsapp.com/products/create-ads-that-click-to-whatsapp)」に従って、Facebook、Instagram、またはその他のプラットフォームで広告を作成します。自動応答は**設定しないでください**。応答はBrazeで設定します。

![エンゲージメント広告を作成するための作成画面が表示された広告マネージャー。]({% image_buster /assets/img/whatsapp/meta_ads_composer.png %})

事前入力メッセージを設定する際、ユーザーからWhatsApp Businessアカウントに送信されるメッセージに、特定の広告に対するレスポンスをトリガーするために使用する特定の単語やフレーズを含めます。この例では、フードデリバリーアプリが広告で宣伝している「free delivery」を使用しています。

![事前入力メッセージに「I want free delivery」と入力された広告マネージャーのテンプレート作成画面。]({% image_buster /assets/img/whatsapp/pre_filled_message.png %})

{% alert tip %}
広告をクリックするとブランドとの会話が始まることを、「今すぐWhatsAppでチャット」などのフレーズを使用して広告の説明文で明確にしてください。
{% endalert %}

{: start="2"}
2. Brazeで、アクションベースのオプションが**WhatsApp受信メッセージを送信**で、メッセージ本文が「YOUR_TRIGGER_WORD」であるアクションベースのキャンバスを設定します。この例では、フードデリバリーアプリが「free delivery」を使用しています。

![トリガーイベントが「WhatsApp受信メッセージを送信」で、メッセージ本文が「free delivery」の正規表現に一致するアクションベースのBrazeキャンバスのエントリスケジュール。]({% image_buster /assets/img/whatsapp/action_based_free_delivery.png %})

{: start="3"}
3. 顧客がキャンバスに入った直後（例えば、遅延なし）に送信されるレスポンスメッセージをキャンバスで設定します。広告をクリックすることは技術的にはオプトインに該当しますが、レスポンスメッセージでは、WhatsAppで今後のマーケティングメッセージを受け取りたいかどうかをユーザーに確認することをお勧めします。

{% alert tip %}
ユーザーがオプトインするかどうかをすばやく示せるように、クイック返信（「はい」や「いいえ」など）を使用してレスポンスメッセージを設定してください。
{% endalert %}

広告で約束した割引コード、オファー、またはその他の情報を提供することも忘れないでください。

![「はい」と「いいえ」のボタン返信が表示されたWhatsAppメッセージ作成画面。]({% image_buster /assets/img/whatsapp/quick_replies.png %})

![トリガーイベントが「購読グループへのWhatsApp受信メッセージを送信」で、トリガーワードが「YES」の「オプトイン」グループを含むキャンバスステップ。]({% image_buster /assets/img/whatsapp/opting_in_step.png %})

{: start="4"}
4. 以下のいずれかの更新方法でユーザープロファイルの購読ステータスを更新して、ユーザーをオプトインさせます。
    - REST APIを通じて購読ステータスを更新するBraze間Webhookを作成します。
    - 高度なJSONエディターを使用して、[ユーザーのWhatsAppキャンバスへの購読ステータスを更新する]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups#whatsapp-opt-in-and-opt-out-process)テンプレートでユーザープロファイルを更新します。

![高度なJSONエディターを使用してユーザープロファイルを更新するユーザー更新キャンバスステップ。]({% image_buster /assets/img/whatsapp/user_update_step_json.png %})

![オプトイン、オプトアウト、その他全員の3つのアクションパスを含む、Click to WhatsApp広告を送信するためのワークフローを示すキャンバス。]({% image_buster /assets/img/whatsapp/ads_that_click_canvas.png %})

## 考慮事項 {#considerations}

Click to WhatsApp広告から開始される会話は、以下の条件を満たす場合、無料となります。

- ユーザーがClick to WhatsApp広告などの[無料エントリポイント](https://developers.facebook.com/docs/whatsapp/pricing#free-entry-point-conversations)を通じてメッセージを送信すると、24時間の[カスタマーサービスウィンドウ](https://developers.facebook.com/docs/whatsapp/cloud-api/guides/send-messages#customer-service-windows)が開き、その間にそのユーザーに対してあらゆる種類のメッセージを送信できます。
- カスタマーサービスウィンドウ内（24時間以内）に返信すると、72時間の無料エントリポイントが開き、その72時間のウィンドウ内のすべてのメッセージが無料となります。