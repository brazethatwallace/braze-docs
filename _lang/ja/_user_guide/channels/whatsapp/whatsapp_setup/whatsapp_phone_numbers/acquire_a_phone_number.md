---
nav_title: "電話番号の取得"
article_title: "WhatsApp電話番号の取得"
page_order: 1
description: "このリファレンス記事では、TwilioおよびInfobipから電話番号を取得する方法について説明します。"
page_type: reference
channel:
  - WhatsApp
---

# WhatsApp電話番号の取得 {#acquire-a-whatsapp-phone-number}

> WhatsAppメッセージングチャネルを使用するには、WhatsAppの[Cloud API](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers)または[On-Premises API](https://developers.facebook.com/docs/whatsapp/on-premises/phone-numbers)の要件を満たす電話番号が必要です。

Brazeが電話番号をプロビジョニングすることはないため、ご自身で電話番号を取得する必要があります。ビジネス向け電話プロバイダーを通じてSIMカード付きの物理的な電話を購入するか、パートナーであるTwilioまたはInfobipを利用できます。**この作業はBrazeを通じて行うことはできないため、ご自身のTwilioまたはInfobipアカウントが必要です。**

## WhatsApp APIの要件 {#whatsapp-api-requirements}

電話番号は以下のWhatsApp APIの要件を満たす必要があります：

- ご自身のビジネスが所有していること
- 国番号と市外局番があること（固定電話や携帯電話番号など）
- 音声通話またはSMSを受信できること
- アカウント設定時にアクセス可能であること（認証コードの受信のため）
- ショートコードでないこと
- WhatsApp Business Platformで以前使用されていないこと
- 個人のWhatsAppアカウントに接続されていないこと

{% alert note %}
Brazeでは、ご自身のビジネスが所有し、継続的にフルアクセスできる番号を使用することを強くお勧めします。WhatsApp埋め込みサインアッププロセスでは、番号を認証するためにこの番号に送信されるメッセージにアクセスする必要があります。後で再度番号を認証する必要がある場合もあるため、番号へのアクセスを維持する必要があります。
{% endalert %}

## Twilio電話番号の取得 {#acquiring-a-twilio-phone-number}

### ステップ1:TwilioコンソールまたはAPIから電話番号を購入する {#step-1-buy-a-phone-number-from-the-twilio-console-or-api}

1. Twilioコンソールから、**Develop** > **Phone Numbers** > **Manage** > **Buy a number** に移動します。このオプションが表示されない場合は、**Explore Products** を選択し、**Super Networks** までスクロールして、**Phone Number** > **Buy a number** を選択します。<br><br>![「Develop」タブが開かれ「Buy a number」オプションが表示されたTwilioコンソール。]({% image_buster /assets/img/whatsapp/develop_buy_number.png %}){: style="max-width:20%;"}<br><br>

2. 希望する市外局番または地域（ある場合）を入力します。番号を見つけたら、**Buy** を選択します。<br><br> ![表示された電話番号を購入するためのボタン。]({% image_buster /assets/img/whatsapp/buy.png %})<br><br>

3. 電話番号を購入したら、**Active Numbers** に移動し、購入した電話番号を選択します。<br><br>![購入した電話番号が表示された「Active Numbers」。]({% image_buster /assets/img/whatsapp/active_numbers.png %}){: style="max-width:70%;"}<br><br>

### ステップ2:電話番号を設定する {#step-2-configure-your-phone-number}

メール経由で認証コードを受信できるようにTwilio電話番号を設定します。**Twilioコンソールで電話番号をWhatsAppにリンクしないでください。**

{% alert warning %}
Twilioコンソールで電話番号をWhatsAppにリンクしないでください。リンクすると、その番号がTwilioのWhatsApp Business Accountに登録されるため、埋め込みサインアップワークフローを通じてBrazeに接続できなくなります。
{% endalert %}

1. Twilioコンソールで、[Active Numbersページ](https://www.twilio.com/console/phone-numbers/incoming)に移動し、購入した電話番号を選択します。
2. **Voice Configuration** セクションに移動し、**Configure with** ドロップダウンで **Webhook, TwiML Bin, Function, Studio Flow, Proxy Service** を選択します。
3. **A call comes in** の行で、**Webhook** を選択し、URLを `https://twimlets.com/voicemail?Email=YOUR_EMAIL_ADDRESS` に設定します。`YOUR_EMAIL_ADDRESS` はご自身のメールアドレスに置き換えてください。

### ステップ3:埋め込みサインアップワークフローを完了する {#step-3-complete-the-embedded-sign-up-workflow}

1. Twilioの設定が完了したら、Brazeダッシュボード > **テクノロジーパートナー** > **WhatsApp** に移動し、**Begin integration** または **Add WhatsApp Business Account**（表示されている方）を選択して、[埋め込みサインアップワークフロー]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/embedded_signup)をトリガーします。<br><br>**Add a phone number for WhatsApp** のステップで、電話番号の認証方法として **Phone call** を選択します。<br><br>![テキストメッセージまたは電話で電話番号を認証するオプションが表示されたセクション。]({% image_buster /assets/img/whatsapp/verify.png %}){: style="max-width:50%;"}<br><br>

2. 認証コードがメールの受信トレイに届くまで数分待ち、認証コードを入力して設定を完了します。

## Infobip電話番号の取得 {#acquiring-an-infobip-phone-number}

1. Infobipコンソールで、**Channels and Numbers** に移動し、**Numbers** を選択します。<br><br>![「Numbers」が下に表示されたInfobipの「Channels and Numbers」セクション。]({% image_buster /assets/img/whatsapp/infoblip_numbers.png %}){: style="max-width:30%;"}<br><br>

2. **Buy Number** > メッセージを送信したい国 > **SMS** を選択します。<br><br>![番号を購入するためのボタン。]({% image_buster /assets/img/whatsapp/infoblip_buy.png %})<br><br>

3. 選択した国によっては、追加の登録プロセスを完了する必要がある場合があります（米国の電話番号の場合、10DLCまたはトールフリーオプションの選択など）。利用可能なオプションを必ず選択してください。<br><br>![番号タイプ（10DLCまたはトールフリー）の選択を求めるページ。]({% image_buster /assets/img/whatsapp/infoblip_10dlc.png %}){: style="max-width:70%;"}<br><br>

4. 利用可能なオファーを選択し、残りのステップを進めて、リクエストが処理されるのを待ちます。**Numbers** > **My Request** に移動してステータスを確認できます。<br><br>![料金やカバレッジなどの情報を含むオファー。]({% image_buster /assets/img/whatsapp/infoblip_offer.png %}){: style="max-width:70%;"}<br><br>

5. 選択した国によっては、Infobipチームから登録の詳細について連絡が来るのを待ちます（米国の10DLCなど）。<br><br>

6. Infobipで電話番号の準備ができたら、Brazeダッシュボード > **テクノロジーパートナー** > **WhatsApp** に移動し、**Begin integration** または **Add WhatsApp Business Account**（表示されている方）を選択して、[埋め込みサインアップワークフロー]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/embedded_signup)をトリガーします。<br><br>**Add a phone number for WhatsApp** のステップで、電話番号の認証方法として **Text message** を選択します。<br><br>![テキストメッセージまたは電話で電話番号を認証するオプションが表示されたセクション。]({% image_buster /assets/img/whatsapp/infoblip_verify.png %})<br><br>

7. Infobipのカスタマーポータルで[analyze logs](https://www.infobip.com/docs/analyze/analyze-logs)を確認して認証コードを取得します。表示されるまで数分かかる場合があります。認証コードを入力して設定を完了します。