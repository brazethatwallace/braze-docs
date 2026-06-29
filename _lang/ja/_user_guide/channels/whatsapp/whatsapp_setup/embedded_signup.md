---
nav_title: 埋め込みサインアップ
article_title: WhatsApp埋め込みサインアップ
page_order: 1
description: "このリファレンス記事では、BrazeにおけるWhatsApp埋め込みサインアップワークフローの手順を説明します。"
page_type: reference
channel:
  - WhatsApp
---

# WhatsApp埋め込みサインアップ {#whatsapp-embedded-signup}

> このリファレンス記事では、BrazeにおけるWhatsApp埋め込みサインアップワークフローの手順を説明します。

WhatsApp埋め込みサインアップワークフローは、Brazeワークスペースに初めて[WhatsAppを統合する]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/)とき、および既存のWhatsApp統合に[WhatsApp Businessアカウントを追加する]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups/)ときにアクセスします。

{% alert note %}
Brazeワークスペースには[複数のWhatsApp Businessアカウント]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups/)を追加できます。ただし、各WhatsApp Businessアカウントは1つのBrazeワークスペースにのみ追加できます。
{% endalert %}

## ワークフローへのアクセス {#accessing-the-workflow}

**パートナー連携** > **テクノロジーパートナー**に移動し、**WhatsApp**を検索して選択します。次の選択はユースケースによって異なります。

- ワークスペースにWhatsAppを統合する場合は、**Begin Integration**を選択します。<br><br>![統合を開始するボタンがあるWhatsAppパートナーページ。]({% image_buster /assets/img/whatsapp/whatsapp1.png %}){: style="max-width:80%;"}<br><br>
- 既存のWhatsApp統合にWhatsApp Businessアカウントを追加する場合は、**Add WhatsApp Business Account**を選択します。<br><br>![WhatsApp Businessアカウントまたはサブスクリプショングループと番号を追加するオプションがある「WhatsApp Messaging Integration」。]({% image_buster /assets/img/whatsapp/multiple_wabas.png %}){: style="max-width:80%;"}

ここからのワークフローは、どちらのユースケースでも同じです。

## WhatsApp埋め込みサインアップワークフロー {#whatsapp-embedded-signup-workflow}

1. Meta（Facebook）ログインウィンドウで、**Login as**または**Continue**を選択します。<br><br>![Metaログインウィンドウ。]({% image_buster /assets/img/whatsapp/login_screen.png %}){: style="max-width:60%;"}<br><br>
2. Brazeと共有する権限を確認し、**Get Started**を選択します。<br><br>![統合のためにBrazeと共有する権限のリスト。]({% image_buster /assets/img/whatsapp/get_started.png %}){: style="max-width:50%;"}<br><br>
3. この画面で以下を設定し、**Next**を選択します。
- **Business portfolio**ドロップダウンでビジネスポートフォリオを選択します。これはWhatsApp Businessアカウントに接続されるため、期待するビジネスポートフォリオが表示されない場合は、権限を確認してください。
- **WhatsApp business account**フィールドで、**Create a new WhatsApp Business Account**を選択します。これは、ワークスペースに別のWhatsApp Businessアカウントを追加する場合や、そのアカウントがすでにMetaに存在する場合も同様です。ドロップダウンから既存のWhatsApp Businessアカウントを選択するのではなく、このオプションを選択してください。<br><br>![ビジネスポートフォリオ名を含むビジネス情報を入力するフィールドがあるウィンドウ。]({% image_buster /assets/img/whatsapp/business_info.png %}){: style="max-width:50%;"}<br><br>
4. 以下のドロップダウンフィールドを選択し、**Next**を選択します。
- **Choose a WhatsApp Business account**：WhatsApp Businessアカウントを作成
- **Create or select a WhatsApp Business profile**：新しいWhatsApp Businessプロファイルを作成<br><br>![WhatsApp Businessアカウントとプロファイルを選択または作成するかを指定するフィールド。]({% image_buster /assets/img/whatsapp/create_select_waba.png %}){: style="max-width:50%;"}<br><br>
5. 以下の情報を入力し、**Next**を選択します。
- WhatsApp Businessアカウント名
- WhatsApp Business表示名
- カテゴリ<br><br>![新しいWhatsApp Businessアカウントの詳細を入力するフィールド。]({% image_buster /assets/img/whatsapp/waba_details.png %}){: style="max-width:50%;"}<br><br>
6. 電話番号を入力し、**Text message**または**Phone call**を選択します。新しい番号の場合、その番号は他のWhatsAppアカウントに登録されていないことを含め、WhatsAppの電話番号要件を満たしている必要があります。既存の番号を移行する場合（ステップ3を参照）、Metaでその番号がすでに使用中と表示されても、警告を無視して移行を完了してください。<br><br>![電話番号を追加するフィールド。]({% image_buster /assets/img/whatsapp/add_phone_number.png %}){: style="max-width:50%;"}<br><br>
7. 2要素認証コードを入力し、**Next**を選択します。<br><br>![2要素認証コードの入力フィールド。]({% image_buster /assets/img/whatsapp/two_factor.png %}){: style="max-width:50%;"}<br><br>
8. WhatsApp Businessアカウントが受け取る権限を確認し、**Continue**を選択します。<br><br>![WhatsApp Businessアカウントがリクエストする権限のリスト。]({% image_buster /assets/img/whatsapp/permissions.png %}){: style="max-width:50%;"}<br><br>
9. 完了です！<br><br>![メッセージの送信を開始する準備ができたことを示すウィンドウ。]({% image_buster /assets/img/whatsapp/finish.png %}){: style="max-width:50%;"}