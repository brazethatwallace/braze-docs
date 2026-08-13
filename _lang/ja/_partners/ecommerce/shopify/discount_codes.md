---
nav_title: 固有の割引コード
article_title: ユニークな割引コードを送る
alias: /shopify_discount_codes/
page_order: 7
description: "この参考記事では、Shopifyの一括割引コードボットでBrazeプロモーションコードを使用し、キャンペーンやキャンバスを通じてユニークな割引コードを送信する、コミュニティから投稿されたユースケースを取り上げます。"
---

# Shopifyを通じてユニークな割引コードを送信する {#send-unique-discount-codes-through-shopify}

> このコミュニティから投稿されたユースケースは、Brazeの[プロモーションコード]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes)をShopify一括割引コードボットとともに使用し、キャンペーンやキャンバス用にユニークな割引コードを生成する方法を示します。ユニークな割引コードは、一般的なプロモーションコードの悪用を防ぐのに役立ちます。

{% alert important %}
これはコミュニティから提出された統合であり、Brazeは直接サポートしていません。一括割引コードボットはShopifyによって直接サポートされています。Brazeがサポートしているのは Brazeプロモーションコードのみです。
{% endalert %}

## 要件 {#requirements}

| 要件 | 説明 |
| --- | --- |
| Shopifyストアのセットアップ | [BrazeでShopifyストアをセットアップ]({{site.baseurl}}/shopify_overview)済みであることを確認してください。 |
| Bulk Discount Code Botアプリのインストール | Shopifyアプリストアで[Bulk Discount Code Bot](https://apps.shopify.com/bulk-discount-generator)アプリをダウンロードしてください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="要件" }

## ユニークなディスカウントコードの生成 {#generating-unique-discount-codes}

### ステップ1：ディスカウントコードを設定する {#step-1-configure-your-discount-codes}

Bulk Discount Code Botを使用して、生成するコード数、コードの長さ、割引額などに基づいてディスカウントコードを設定します。

![ディスカウントセットの設定オプション。][1]

### ステップ2：コードをエクスポートする {#step-2-export-your-codes}

Bulk Discount Code Botの検索バーでディスカウントセットを見つけ、**Export Codes** > **Download Codes** を選択して、CSVファイルをダウンロードフォルダにダウンロードします。

![ディスカウントセットが表示されたドロップダウン付きの検索バーと、選択可能なボタンの行。][2]{: style="max-width:70%;"}

CSVファイルで、行1を削除して列ヘッダー「Promo」を除去します。これにより、「Promo」がBrazeでディスカウントコードとして登録されるのを防ぎます。

![CSVファイルで行ヘッダー「Promo」を削除する手順を示すフローチャート。][3]{: style="max-width:60%;"}

### ステップ3：ディスカウントコードをBrazeに追加する {#step-3-add-your-discount-codes-to-braze}

Brazeで、**Data Settings** > **Promotion Codes** > **Create Promotion Code List** に移動し、[ディスカウントコードリストを設定]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/create#create)します。Bulk Discounts Code Botで設定した有効期限と一致させてください。

次に、CSVファイルをアップロードし、**Save List** を選択します。

### ステップ4：ディスカウントコードをBrazeのキャンペーンまたはキャンバスステップに追加する {#step-4-add-your-discount-codes-to-a-braze-campaign-or-canvas-step}

ユニークなディスカウントコードを単発送信のキャンペーンで使用する場合、または異なるキャンペーンやキャンバスステップ間でユーザーが複数のユニークコードを受け取っても問題ない場合は、保存したプロモーションコードリストからコードのLiquidスニペットをコピーします。

![コピーボタン付きのLiquidコードスニペット。][4]{: style="max-width:60%;"}

Liquidスニペットをキャンペーンまたはキャンバスステップに貼り付けます。

<video autoplay muted loop playsinline loading="lazy" style="max-width:100%;" aria-label="キャンバスステップにLiquidスニペットを追加する様子を示す動画。">
  <source src="{% image_buster /assets/img/shopify/liquid_promo_code.mp4 %}" type="video/mp4">
</video>

キャンペーンやキャンバスでディスカウントコードが何回参照されても、ユーザーに1つのユニークなディスカウントコードのみを受け取らせたい場合は、最初のメッセージステップの直前に[ユーザー更新]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update)ステップを作成し、ディスカウントコードを「Promo Code」などのカスタム属性に割り当てます。

{% alert tip %}
**Data Settings** > **Custom Attributes** に移動して、[カスタム属性を作成]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes)することもできます。
{% endalert %}

ユーザー更新ステップで、各フィールドに対して以下を行います。
- **Attribute Name：** **Promo Code** を選択します。
- **Action：** **Update** を選択します。
- **Key Value：** Liquidコードスニペットを貼り付けます。

![「Promo Code」属性をLiquidスニペットで更新するユーザー更新ステップ。][6]

これで、任意のメッセージにカスタム属性 {% raw %}`{{custom_attribute.${Promo Code}}}`{% endraw %} を追加でき、ディスカウントコードがテンプレートとして挿入されます。

## 割引コードの動作 {#discount-code-behavior}

{% details マルチチャネルキャンペーンまたはキャンバスステップ %}

マルチチャネルキャンペーンまたはキャンバスステップで割引コードスニペットを使用する場合、ユーザーは常にユニークなコードを受け取ります。ユーザーが複数のチャネルを通じてコードを受け取る資格がある場合、各チャネルで同じコードを受け取ります。つまり、対象のユーザーは、そのキャンペーンまたはキャンバスステップから送信されるすべてのメッセージを通じて、1つのコードのみを受け取ります。

{% enddetails %}

{% details 異なるキャンバスステップまたは別々のキャンペーン %}

割引コードが同じキャンバス内の複数のステップまたは別々のキャンペーンで参照されている場合、対象のユーザーは複数のユニークなプロモーションコード（キャンバスステップまたはキャンペーンごとに1つのコード）を受け取ります。

{% enddetails %}

[1]: {% image_buster /assets/img/shopify/configure_discount_codes.png %}
[2]: {% image_buster /assets/img/shopify/export_discount_codes.png %}
[3]: {% image_buster /assets/img/shopify/edited_codes_csv.png %}
[4]: {% image_buster /assets/img/shopify/liquid_code_snippet.png %}
[6]: {% image_buster /assets/img/shopify/user_update_step.png %}