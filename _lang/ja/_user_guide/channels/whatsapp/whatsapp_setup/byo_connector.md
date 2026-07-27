---
nav_title: BYO WhatsAppコネクター
article_title: Bring Your Own WhatsAppコネクター
page_order: 2
description: "このリファレンス記事では、Bring Your Own WhatsAppコネクターのセットアップ手順を説明します。このコネクターにより、BrazeからInfobip WhatsApp Business Managerにアクセスできるようになります。"
page_type: reference
channel:
  - WhatsApp
---

# Bring Your Own WhatsAppコネクター {#bring-your-own-whatsapp-connector}

> Bring Your Own（BYO）WhatsAppコネクターは、BrazeとInfobipのパートナーシップを提供するもので、BrazeにInfobip WhatsApp Business Manager（WABA）へのアクセスを許可します。これにより、Brazeでセグメンテーション、パーソナライゼーション、キャンペーンオーケストレーションを活用しながら、メッセージングコストをInfobipと直接管理・支払いできます。Brazeは、送信メッセージ、受信メッセージ処理、WhatsAppフロー、分析など、WhatsAppチャネルが提供する既存の機能をすべて維持します。

## 要件 {#requirements}

| 要件 | 説明 |
| --- | --- |
| Infobipアカウント | BYO WhatsAppコネクターを使用するには、Infobipアカウントが必要です。 |
| メッセージまたはアクションクレジット | WhatsAppメッセージを送信する際に、Brazeアクションクレジットを消費します。 |
| WhatsApp要件 | すべての[WhatsApp要件]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup#prerequisites)を完了してください。 |
| 電話番号 | 利便性のため、[Infobipを通じて電話番号を取得する](https://www.infobip.com/docs/numbers/getting-started)ことをお勧めします。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="要件" }

## セットアップ {#set-up}

BYO WhatsAppコネクターをセットアップする前に、WhatsApp Businessアカウントの過去の送信がInfobipを通じて行われていないことを確認してください。

### サポートされるケース {#supported-cases}

- WhatsApp Businessアカウントと電話番号がこれまでパートナーに接続されたことがない
- WhatsApp Businessアカウントがネイティブ統合を通じてBrazeに直接接続されている
    - [WhatsApp電話番号の移行]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/whatsapp_phone_numbers/migrate_a_phone_number)の手順に従い、電話番号を1つずつ新しいWhatsApp Businessアカウントに移行してください。
- WhatsApp BusinessアカウントがBrazeおよびInfobip以外のソリューションプロバイダーに接続されている
    - [WhatsApp電話番号の移行]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/whatsapp_phone_numbers/migrate_a_phone_number)の手順に従い、電話番号を1つずつ新しいWhatsApp Businessアカウントに移行してください。

## ステップ 1:Infobipアカウント情報の取得 {#step-1}

1. Infobipで、WhatsApp Businessアカウントに使用するアカウントを特定します。
2. **Developer Tools** > **API Keys** に移動し、**Create API Key** を選択します。

![作成日が「16/12/2025」、有効期限が「16/12/36」の「Create API key」ページ。]({% image_buster /assets/img/whatsapp/byo_connector/create_api_key.png %})

{: start="3"}
3. 「Braze - My Workspace Name - My WABA Name」など、わかりやすい名前をキーに付けます。
4. トークンの有効期限切れの問題を避けるため、十分先の有効期限を設定します。
    - 有効期限前に新しいAPIキーを生成してWABAを再接続するようメモしておいてください。
5. 以下のスコープを選択します:
- `Message:send`
- `Whatsapp:manage`
- `Whatsapp:message:send`
- `Account-management:manage`
- `Subscriptions:manage`
- `Metrics:manage`
6. キーを作成したら、APIキーをコピーします。
    - キーは作成後、限られた時間内にのみコピーできます。将来別のWhatsApp Businessアカウントを接続する必要がある場合は、これらの手順を繰り返して新しいキーを作成できます。

![6つのスコープが追加された「Braze Example API Key」。]({% image_buster /assets/img/whatsapp/byo_connector/api_key.png %})

{: start="7"}
7. アカウントのAPIベースURLをコピーします。

![APIベースURLがハイライトされた「API keys」ページ。]({% image_buster /assets/img/whatsapp/byo_connector/api_base_url.png %})

## ステップ 2:埋め込みサインアップの開始 {#step-2-start-the-embedded-signup}

1. Brazeで、**パートナー連携** > **テクノロジーパートナー** > **WhatsApp** に移動します。
2. **BYO Connector - Infobip** タブを選択します。

![WhatsAppテクノロジーパートナーページ。]({% image_buster /assets/img/whatsapp/byo_connector/byo_tab_tech_parners.png %})

{: start="3"}
3. [ステップ 1](#step-1)で取得したAPIキーとベースURLを入力します。
4. **Connect** を選択します。
5. 以下の点に注意しながら、[埋め込みサインアップワークフロー]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/embedded_signup#whatsapp-embedded-signup-workflow)を進めます:
- 別のBusiness Solution Providerが使用しているビジネスポートフォリオと同じものは選択できません。
- 別のBusiness Solution Providerが使用している電話番号は選択できません。
- 既存のWABAを選択するのではなく、新しいWABAを作成する必要があります。

{% alert note %}
認証コードを受け取るには、Infobipダッシュボード > **Analyze** > **Logs** に移動し、受信SMSメッセージからコードを取得してください。
{% endalert %}

![認証コードを含む受信SMSメッセージを表示するメッセージログ。]({% image_buster /assets/img/whatsapp/byo_connector/verification_code.png %})

セットアップが完了すると、電話番号がWhatsApp Business Groupの下にサブスクリプショングループとして表示されます。WhatsApp Business Groupには、接続先のInfobipアカウント名とAPIベースURLが含まれます。ネイティブ統合を通じて接続されたアカウントには、Infobipアカウント名は表示されません。

{% alert note %}
各WhatsApp Businessアカウントを1つのInfobipアカウントに接続してください。追加の電話番号やサブスクリプショングループを接続するたびに、WhatsApp Businessアカウントがすでにinfobipアカウントに接続されている場合は、既存アカウントのAPI認証情報を再入力する必要があります。
{% endalert %}

## ステップ 3:メッセージの送信 {#step-3-sending-messages}

以下を含むネイティブ統合の送信プロセスに従ってください:
- [サブスクリプショングループへのユーザー登録]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups)
- [WhatsAppメッセージの作成]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message)

## セットアップのトラブルシューティング {#troubleshooting-setup}

### WhatsApp Businessアカウント IDを取得できない {#couldnt-retrieve-whatsapp-business-account-id}

WhatsApp Businessアカウントが別のBrazeワークスペースに接続されていないことを確認してください。

### WhatsApp Businessアカウント IDをInfobipと共有できない {#couldnt-share-whatsapp-business-account-id-with-infobip}

1. WhatsApp BusinessアカウントがBrazeまたは別のパートナーに接続されていないことを確認してください。
2. WhatsApp Businessアカウント内の電話番号が別のInfobipアカウントに接続されていないことを確認してください。インポートされた番号の場合は、Infobipで番号を見つけて **Cancel number** を選択できます。

## 注意事項 {#considerations}

Brazeの既存機能はすべてサポートされていますが、以下のユースケースは現在サポートされていません。

| ユースケース | 理由 |
| --- | --- |
| BrazeとInfobipの両方で受信メッセージを処理する | いずれかのシステムによってトリガーされるロジックチェーンが発生し、重複した、場合によっては矛盾するメッセージスレッドが生成される可能性があるためです。 |
| BrazeとInfobipの両方からメッセージを送信する | Brazeに接続されたWhatsApp Businessアカウントの場合、すべての送信はBrazeから行われます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="注意事項" }