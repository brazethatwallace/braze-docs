---
nav_title: Meta直接請求
article_title: Meta直接請求
page_order: 7
description: "このリファレンス記事では、Brazeまたはパートナーのクレジットラインではなく、自分のデビットカードまたはクレジットカードでWhatsAppメッセージングコストを支払うためのMeta直接請求の設定方法について説明します。"
page_type: reference
channel:
  - WhatsApp
alias: /whatsapp_meta_direct_billing/
hidden: true
noindex: true
---

# Meta直接請求 {#meta-direct-billing}

> Meta直接請求を使用すると、Brazeまたはパートナーのクレジットラインを通じた請求ではなく、自分のデビットカードまたはクレジットカードでWhatsAppメッセージングコストを直接支払うことができます。

## 前提条件 {#prerequisites}

Meta直接請求を設定する前に、以下の要件を満たしていることを確認してください。

| 要件 | 説明 |
| --- | --- |
| Brazeワークスペースへのアクセス | 埋め込みサインアップフローを開始するには、Brazeで**パートナー連携** > **テクノロジーパートナー**にアクセスする必要があります。 |
| Meta Business マネージャーアカウント | 請求はMeta Business マネージャーの**Billing & payments**で設定します。 |
| デビットカードまたはクレジットカード | 設定を完了するには有効なカードが必要です。一部のアカウントでは月次請求がオプションとして表示される場合がありますが、保証されるものではありません。 |
| 完全なビジネス情報 | ビジネス名、住所、通貨が入力済みで正確である必要があります。Metaはメッセージングを有効にする前にこの情報を審査します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## 設定 {#setup}

### ステップ1：Meta直接請求を選択する {#step-1-select-meta-direct-billing}

1. Brazeで、**パートナー連携** > **テクノロジーパートナー**に移動し、**WhatsApp**を検索して、**WhatsApp Messaging Integration**ページを開きます。
2. **Meta Direct Billing**タブを選択します。これは請求関係がBrazeやInfobipの請求ラインを通じてではなく、Metaと直接であることを意味するため、後から変更しようとするのではなく、続行する前にこのタブを選択することが重要です。
3. **Add a WhatsApp Business Account or phone number**の下で、**Add account or number**を選択します。これにより、Metaの埋め込みサインアップが起動し、Metaにログインしてビジネスポートフォリオを選択し、WhatsApp Businessアカウント（WABA）を作成または選択し、電話番号を確認します。

### ステップ2：Billing & paymentsに移動する {#step-2-go-to-billing-payments}

Metaの埋め込みサインアップを完了した後、以下のいずれかを行います。

- **Add payment method**を選択すると、Meta Business マネージャーに移動します。
- Meta Business マネージャーで、**Billing & payments** > **Accounts**に移動し、WABAを選択します。

### ステップ3：支払い方法を追加する {#step-3-add-a-payment-method}

1. **Add payment method**を選択します。
2. 開いたウィンドウで、**Business location and currency**（例：**Canada, US Dollars USD**）を確認します。これにより請求通貨が決まります。変更が必要な場合は**Edit**を選択してください。
3. **Select payment method**の下に、既存のクレジットラインが表示される場合があります。これらは使用できませんので、選択しないでください。詳細については、[請求ラインの制限事項](#billing-line-restrictions)を参照してください。

![支払い方法の選択ウィンドウ。デビットカードまたはクレジットカードが選択され、既存のInfobipおよびBrazeのクレジットラインは未選択のまま。]({% image_buster /assets/img/whatsapp/payment_methods.png %}){: style="max-width:40%;"}

{: start="4"}
4. **Add payment method**の下で、**Debit or credit カード**を選択し、**Next**を選択します。
5. カード情報を入力し、**Save**を選択します。
6. カードが**Payment methods**の下に表示され、**Default**としてマークされ、マスクされたカード番号と有効期限が表示されます。

{% alert note %}
支払い方法を追加した後に設定ウィンドウを閉じても、電話番号は切断されません。リンクされた番号は保持されます。
{% endalert %}

### ステップ4：ビジネス情報を確認する {#step-4-confirm-your-business-information}

Metaはメッセージングを有効にする前に、ビジネス名、住所、通貨を審査します。ビジネス情報が不完全または不正確な場合、メッセージの送信に失敗したり、無効なビジネス情報エラーが発生したりする可能性があります。

## 請求ラインの制限事項 {#billing-line-restrictions}

支払い方法の一覧に表示されるクレジットライン（例：「Infobip Limited」や「BRAZE INC.」）は、あなたではなく、その特定の企業が所有しています。アカウントの接続方法のために表示されますが、選択することはできません。

## Metaリソース {#meta-resources}

- [Meta Businessヘルプセンター：Billing and payments](https://business.facebook.com/business/help/535561817791563)
- [Meta Businessヘルプセンター：Adding a payment method](https://www.facebook.com/business/help/832746984379005)