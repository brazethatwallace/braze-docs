---
nav_title: "複数のビジネスアカウント"
article_title: "複数のビジネスアカウント"
page_order: 5
description: "このリファレンス記事では、WhatsAppビジネスアカウントと電話番号を追加する手順について説明します。"
page_type: reference
channel:
  - WhatsApp
---

# 複数のWhatsAppビジネスアカウントと電話番号 {#multiple-whatsapp-business-accounts-and-phone-numbers}

> 各ワークスペースに複数のWhatsAppビジネスアカウントとサブスクリプショングループ（および電話番号）を追加できます。<br><br>各サブスクリプショングループは1つのユニークな電話番号に接続されるため、同じ電話番号を複数のサブスクリプショングループに接続したり、複数の電話番号を1つのサブスクリプショングループに接続したりすることはできません。

## 複数のWhatsAppビジネスアカウント {#multiple-whatsapp-business-accounts}

複数のWhatsAppビジネスアカウントは、複数のブランドを持つBrazeワークスペースのユーザーにWhatsAppメッセージを送信したい場合に便利です。各ビジネスアカウントはWhatsApp内で独立して運用され、独自の電話番号、メッセージテンプレート、品質評価を持っています。

同じMeta Business マネージャー内にネストされたビジネスアカウントは、ユーザーアクセス権限管理とカタログも共有します（カタログはBrazeではまだサポートされていません）。

![BrazeとWhatsAppエコシステムの図。ワークスペースとWhatsAppビジネスアカウントの接続関係を示しています。1つのサブスクリプショングループに1つの電話番号、1つのワークスペースに複数のWhatsAppビジネスアカウント、1つのワークスペースに複数のMeta Business Portfolioを接続できます。]({% image_buster /assets/img/whatsapp/whatsapp_braze_ecosystem.png %})

### WhatsAppビジネスアカウントの追加 {#adding-a-whatsapp-business-account}

ワークスペースごとに最大10個のWhatsAppビジネスアカウントを追加できます。ビジネスアカウントは異なるMeta Business マネージャーにネストできます。アカウントを追加するには：

1. **テクノロジーパートナー** > **WhatsApp**に移動し、**Add WhatsApp Business Account**を選択します。

![WhatsAppメッセージング統合セクション。ビジネスアカウントの追加、またはサブスクリプショングループと番号の追加オプションが表示されています。]({% image_buster /assets/img/whatsapp/multiple_wabas.png %})

{: start="2"}
2. サインアップワークフローを進めます。詳細なステップバイステップのウォークスルーについては、[WhatsApp埋め込みサインアップ]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/embedded_signup)を参照してください。

{% alert important %}
電話番号は、他のWhatsAppアカウントに登録されていないことを含め、WhatsApp電話番号のすべての要件を満たす必要があります。
{% endalert %}

## 複数のサブスクリプショングループと電話番号 {#multiple-subscription-groups-and-phone-numbers}

メッセージテンプレートは、同じWhatsAppビジネスアカウント内のすべての電話番号間で共有されます。WhatsAppサブスクリプショングループの詳細については、[サブスクリプショングループ]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups)を参照してください。

各WhatsApp電話番号は、ユーザーに個別のWhatsAppチャットとして表示されます。WhatsAppビジネスアカウント内の各電話番号は互いに独立して動作するため、以下の項目について同じ値または異なる値を持つことができます：
- 表示名
- ステータス
- 品質評価
- メッセージング制限

### サブスクリプショングループと電話番号の追加 {#adding-a-subscription-group-and-phone-number}

WhatsAppビジネスアカウントごとに最大20個のサブスクリプショングループ（および送信用電話番号）を追加できます。サブスクリプショングループと電話番号を追加するには：

1. **テクノロジーパートナー** > **WhatsApp**に移動し、**Add Subscription Group and Number**を選択します。

![WhatsAppメッセージング統合セクション。ビジネスアカウントの追加、またはサブスクリプショングループと番号の追加オプションが表示されています。]({% image_buster /assets/img/whatsapp/multiple_wabas.png %})

{: start="2"}
2. サインアップワークフローを進めます。<br><br>**Select your WhatsApp Business Account**ステップで、既存のWhatsAppビジネスアカウントを選択し、新しい電話番号を追加します。この番号は、他のWhatsAppアカウントに登録されていないことを含め、WhatsApp電話番号のすべての要件を満たす必要があります。

### サブスクリプショングループと電話番号の削除 {#removing-a-subscription-group-and-phone-number}

1. **オーディエンス** > **サブスクリプション**に移動し、サブスクリプショングループをアーカイブします。
2. Meta Business マネージャーに移動し、電話番号を削除します。