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

## WhatsAppへ誘導する広告の設定 {#setting-up-ads-that-click-to-whatsapp}

1. Meta広告マネージャーで、ステップバイステップガイド「[WhatsAppへ誘導する広告の作成方法](https://business.whatsapp.com/products/create-ads-that-click-to-whatsapp)」に従って、Facebook、Instagram、その他のプラットフォームで広告を作成します。自動応答は設定**しないでください**。応答はBrazeで設定します。

![エンゲージメント広告を作成するための作成画面を表示した広告マネージャー。]({% image_buster /assets/img/whatsapp/meta_ads_composer.png %})

事前入力メッセージを設定する際、ユーザーからWhatsApp Businessアカウントに送信されるメッセージに、特定の広告に対する応答をトリガーするために使用する特定の単語やフレーズを含めます。この例では、フードデリバリーアプリが広告で宣伝している「free delivery」を使用しています。

![事前入力メッセージが「I want free delivery」に設定された広告マネージャーのテンプレート作成画面。]({% image_buster /assets/img/whatsapp/pre_filled_message.png %})

{% alert tip %}
広告をクリックするとブランドとの会話が始まることを、「WhatsAppで今すぐチャット」などのフレーズを使用して広告の説明文で明確にしましょう。
{% endalert %}

{: start="2"}
2. Brazeで、アクションベースのオプションが**Send a WhatsApp inbound message**で、メッセージ本文が「YOUR_TRIGGER_WORD」であるアクションベースのキャンバスを設定します。この例では、フードデリバリーアプリが「free delivery」を使用しています。

![トリガーイベントが「Send a WhatsApp inbound message」で、メッセージ本文が「free delivery」の正規表現に一致するアクションベースのBraze キャンバスのエントリスケジュール。]({% image_buster /assets/img/whatsapp/action_based_free_delivery.png %})

{: start="3"}
3. 顧客がキャンバスに入った直後（遅延なしなど）に送信される応答メッセージをキャンバスで設定します。広告をクリックすることは技術的にはオプトインに該当しますが、応答メッセージでは、WhatsAppで今後のマーケティングメッセージを受け取りたいかどうかをユーザーに確認することをお勧めします。

{% alert tip %}
クイック返信（「はい」や「いいえ」など）を使用して応答メッセージを設定し、ユーザーがオプトインするかどうかをすばやく示せるようにしましょう。
{% endalert %}

広告で約束した割引コード、オファー、その他の情報を提供することも忘れないでください。

![「Yes」と「No Thanks」のボタン返信があるWhatsAppメッセージ作成画面。]({% image_buster /assets/img/whatsapp/quick_replies.png %})

![トリガーイベントが「Sent inbound WhatsApp to subscription group」で、トリガーワードが「YES」の「Opting in」グループを含むキャンバスステップ。]({% image_buster /assets/img/whatsapp/opting_in_step.png %})

{: start="4"}
4. 以下のいずれかの更新方法でユーザープロファイルのサブスクリプションステータスを更新して、ユーザーをオプトインさせます。
    - REST APIを通じてサブスクリプションステータスを更新するBraze間Webhookを作成します。
    - 高度なJSONエディターを使用して、[ユーザーのWhatsApp キャンバスへのサブスクリプションステータスを更新する]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups/#whatsapp-opt-in-and-opt-out-process)テンプレートでユーザープロファイルを更新します。

![高度なJSONエディターを使用してユーザープロファイルを更新するユーザーの更新キャンバスステップ。]({% image_buster /assets/img/whatsapp/user_update_step_json.png %})

![オプトイン、オプトアウト、その他のユーザーの3つのアクションパスを含む、WhatsAppへ誘導する広告を送信するためのワークフローを示すキャンバス。]({% image_buster /assets/img/whatsapp/ads_that_click_canvas.png %})

## 考慮事項 {#considerations}

WhatsAppへ誘導する広告から開始された会話は、以下の条件を満たす場合、無料です。

- ユーザーがWhatsAppへ誘導する広告などの[無料エントリポイント](https://developers.facebook.com/docs/whatsapp/pricing#free-entry-point-conversations)を通じてメッセージを送信した場合、24時間の[カスタマーサービスウィンドウ](https://developers.facebook.com/docs/whatsapp/cloud-api/guides/send-messages#customer-service-windows)が開き、その間にあらゆる種類のメッセージをそのユーザーに送信できます。
- カスタマーサービスウィンドウ内（24時間以内）に応答した場合、72時間の無料エントリポイントが開き、72時間のウィンドウ内のすべてのメッセージが無料になります。
- 応答メッセージは無料です。