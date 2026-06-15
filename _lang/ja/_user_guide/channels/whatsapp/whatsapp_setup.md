---
nav_title: "セットアップ"
article_title: "WhatsAppセットアップ"
alias: /partners/whatsapp/
description: "この記事では、前提条件や推奨される次のステップを含む、Braze WhatsAppチャネルのセットアップ方法について説明します。"
page_type: partner
search_tag: Partner
page_order: 0
channel:
  - WhatsApp
search_rank: 2
---

# WhatsAppセットアップ {#whatsapp-setup}

> [WhatsApp](https://www.whatsapp.com/)ビジネスメッセージングは、世界中で利用されている人気のピアツーピアメッセージングプラットフォームで、企業向けの会話ベースのメッセージングを提供しています。

## 前提条件 {#prerequisites}

連携を進める前に、以下の事項を確認してください。

- **オプトインポリシー:** WhatsAppでは、企業が顧客からメッセージングへのオプトインを取得することが求められます。
- **WhatsAppコンテンツルール:** WhatsAppには、遵守すべきいくつかの[コンテンツルール](https://www.whatsapp.com/legal/commerce-policy?l=en)があります。
- **コンプライアンス:** 適用されるすべてのBrazeおよびMetaのドキュメント、ならびに適用される[Metaポリシー](https://www.whatsapp.com/legal/?lang=en)に準拠してください。
- **24時間の会話制限:** 企業が最初のテンプレートメッセージを送信するか、ユーザーがメッセージを送信した後、24時間の時間枠が発生し、その間に双方がメッセージをやり取りできます。
- **会話の開始:** ユーザーはいつでも会話を開始できます。企業は承認済みのメッセージテンプレートを通じてのみ会話を開始できます。
<br><br>

| 要件 | 説明 |
| ---| --- |
| Meta Business Managerアカウント | このメッセージングチャネルを利用するには、Meta Businessアカウントが必要です。 |
| WhatsApp Businessアカウント | このメッセージングチャネルを利用するには、WhatsApp Businessアカウントが必要です。 |
| WhatsApp電話番号 | メッセージングチャネルを使用するには、WhatsAppの[Cloud API](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers)または[On-Premises API](https://developers.facebook.com/docs/whatsapp/on-premises/phone-numbers)の要件を満たす電話番号を取得する必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 連携 {#integration}

### ステップ 1:WhatsApp MessengerをBrazeに接続する {#step-1-connect-whatsapp-messenger-to-braze}

Brazeで、**パートナー連携** > **テクノロジーパートナー**に移動し、**WhatsApp**を検索します。

WhatsAppパートナーページで、**Begin Integration**を選択します。

![連携を開始するボタンがあるWhatsAppパートナーページ。]({% image_buster /assets/img/whatsapp/whatsapp1.png %}){: style="max-width:70%;"}

開いたウィンドウで、**Begin Integration**ボタンが表示されるまで**Next**を選択します。ボタンを選択して連携プロセスを開始します。

![BrazeをWhatsAppに接続するための手順。]({% image_buster /assets/img/whatsapp/instructions.png %}){: style="max-width:50%;"}

### ステップ 2:WhatsAppセットアップ {#step-2-whatsapp-setup}

次に、Brazeセットアップワークフローが表示されます。ステップバイステップのウォークスルーについては、[WhatsApp埋め込みサインアップ]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/embedded_signup/)を参照してください。

このフローでは、以下を行います。
1. MetaおよびWhatsApp Businessアカウントを作成または選択します。[WhatsApp表示名ガイドライン](https://www.facebook.com/business/help/757569725593362)を確認してください。<br><br>お客様の会社には、既に少なくとも1つのMeta Businessアカウントが存在している可能性があります。その場合は、WhatsApp Businessアカウントを配置したいアカウントを選択してください。WhatsAppのユーザー権限とビジネス認証は、Meta Businessアカウントで一元管理されます。<br><br>
2. WhatsApp Businessプロファイルを作成します。
3. WhatsApp Business番号を認証します。<br><br>

セットアップが完了すると、ユーザー向けの専用WhatsAppサブスクリプショングループが作成されます。

### ステップ 3:WhatsAppテンプレートを作成する {#step-3-create-whatsapp-templates}

承認済みのWhatsAppメッセージテンプレートのみが、顧客との会話を開始するために使用できます。WhatsAppテンプレートは[Meta Business Manager](https://www.facebook.com/business/help/2055875911147364?id=2129163877102343)で作成できます。BrazeがサポートするWhatsAppメッセージング機能の一覧については、[サポートされているWhatsApp機能]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message/#supported-whatsapp-features)をご確認ください。

1. **[テンプレートマネージャー](https://business.facebook.com/wa/manage/message-templates)に移動する**<br>
Meta Business Managerで、**Account Tools**の下にある**Message Templates**を選択します。
次に、**Create Templates**を選択します。<br><br>![メッセージテンプレートの一覧があるWhatsApp Manager。]({% image_buster /assets/img/whatsapp/whatsapp2.png %}){: style="max-width:100%;"}<br><br>
2. **メッセージ設定**<br>
新しいメッセージテンプレートコンポーザーで、メッセージのカテゴリを選択し、テンプレートに名前を付け、サポートする言語を選択します。言語は後から削除または追加できます。<br><br>
	利用可能なメッセージテンプレートカテゴリには以下が含まれます。
	- マーケティング: 認知度とエンゲージメントを高めるために、プロモーションオファー、製品のお知らせなどを送信します
	- ユーティリティ: 重要な情報を共有するために、アカウント更新、注文更新、アラートなどを送信します
	- 認証: 顧客がアカウントにアクセスするためのコードを送信します<br><br>
	![マーケティング、ユーティリティ、認証のカテゴリがあるメッセージテンプレートコンポーザー。]({% image_buster /assets/img/whatsapp/whatsapp3.png %}){: style="max-width:100%;"}<br><br>
3. **テンプレートを編集する**<br>
次に、メッセージテンプレートを作成します。<br><br>テキストまたはメディアヘッダー、テキスト本文、メッセージフッター、ボタンを設定できます。動画およびドキュメントヘッダーは現在利用できず、ヘッダーはテキストまたは画像タイプのいずれかである必要があります。追加するメディアはレビュープロセスのサンプルとして機能し、テンプレートメッセージには**含まれません**。メディアはBrazeで追加する必要があります。メッセージのプレビューがパネルに表示されます。<br><br>MetaはLiquidをサポートしていませんが、後でBrazeでLiquid変数に置き換えることができる変数をテンプレートに組み込むことができます。**+ Add variable**ボタンを選択して行います。<br><br>![テンプレートコンポーザー。]({% image_buster /assets/img/whatsapp/whatsapp4.png %}){: style="max-width:100%;"}

テンプレートが完成したら、**Submit**を押します。

#### テンプレートの承認時間 {#template-approval-time}

メッセージテンプレートの承認ステータスは、Meta Business Managerの**Message Template**ページ、またはBrazeでキャンペーンやキャンバスを作成する際に確認できます。さらに、通知権限の設定に応じて、WhatsAppチームからメールで通知を受け取ることもできます。

{% alert note %}
承認済みテンプレートは、任意の数のキャンペーンやキャンバスで使用できます。また、任意の数のオプトインユーザーに送信することもできます。これは、テンプレートの品質が低下しない限り有効です。
{% endalert %}

### ステップ 4:WhatsApp キャンペーンを作成する {#step-4-create-a-whatsapp-campaign}

WhatsAppテンプレートが承認されたら、ダッシュボードに移動して[WhatsApp キャンバスまたはキャンペーン]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message/)を作成できます。

{% alert note %}
WhatsApp Businessアカウントが作成されると、Metaが初期メッセージング制限を決定します。詳細については、[スループット]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup/10dlc/#throughput)をご確認ください。
{% endalert %}

## 次のステップ {#next-steps}

連携が完了したら、以下の2つのMetaプロセスを完了することをお勧めします。
- [ビジネス認証](https://www.facebook.com/business/help/2058515294227817?id=180505742745347)
	- 既存のMeta Business Managerを使用している場合、ビジネス認証が既に完了している可能性があります。
- [公式ビジネスアカウント](https://www.facebook.com/business/help/604726921052590?ref=search_new_0)

また、[ユーザーの電話番号]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/user_phone_numbers/)についてお読みいただき、[組織でテンプレート](https://www.facebook.com/business/help/2169003770027706?id=2190812977867143)を作成するためにアクセスが必要なユーザーを追加することもお勧めします。

### WhatsApp Cloud APIローカルストレージ {#whatsapp-cloud-api-local-storage}

BrazeはWhatsAppの[Cloud APIローカルストレージ](https://developers.facebook.com/docs/whatsapp/cloud-api/overview/local-storage?content_id=ka6F9gESPqhQpm5)をサポートしています。これを有効にするには、Brazeカスタマーサポートマネージャーにお問い合わせください。