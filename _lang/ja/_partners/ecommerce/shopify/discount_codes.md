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
| Shopifyストアを設定する | [BrazeでShopifyストアを設定]({{site.baseurl}}/shopify_overview)済みであることを確認します。 |
| 一括割引コードボットアプリをインストールする | Shopifyアプリストアで[一括割引コードボット](https://apps.shopify.com/bulk-discount-generator)アプリをダウンロードします。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="要件" }

## ユニークな割引コードを生成する {#generating-unique-discount-codes}

### ステップ1:割引コードを設定する {#step-1-configure-your-discount-codes}

一括割引コードボットを使用して、生成するコードの数、コードの長さ、割引額などに基づいて割引コードを設定します。

![割引セットの設定オプション。][1]

### ステップ2:コードをエクスポートする {#step-2-export-your-codes}

一括割引コードボットの検索バーで割引セットを検索し、**Export Codes** > **Download Codes** を選択して、CSVファイルをダウンロードフォルダにダウンロードします。

![割引セットを表示するドロップダウンと、選択するためのボタンが並んだ検索バー。][2]{: style="max-width:70%;"}

CSVファイルの1行目を削除し、列ヘッダー「Promo」を除去します。これにより「Promo」がBrazeの割引コードになるのを防ぐことができます。

![CSVファイルの行ヘッダー「Promo」の削除を示すフローチャート。][3]{: style="max-width:60%;"}

### ステップ3:Brazeに割引コードを追加する {#step-3-add-your-discount-codes-to-braze}

Brazeで、**Data Settings** > **Promotion Codes** > **Create Promotion Code List** に移動し、[割引コードリストを設定]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/create#create)します。一括割引コードボットで設定した有効期限と一致していることを確認してください。

次にCSVファイルをアップロードし、**Save List** を選択します。

### ステップ4:Brazeのキャンペーンまたはキャンバスステップに割引コードを追加する {#step-4-add-your-discount-codes-to-a-braze-campaign-or-canvas-step}

ユニークな割引コードを1回限りのキャンペーンで使用したい場合、または異なるキャンペーンやキャンバスステップでユーザーが複数のユニークなコードを受け取っても構わない場合は、保存したプロモーションコードリストからコードのLiquidスニペットをコピーします。

![Liquidのコードスニペットとそれをコピーするボタン。][4]{: style="max-width:60%;"}

キャンペーンまたはキャンバスステップにLiquidスニペットを貼り付けます。

<video autoplay muted loop playsinline loading="lazy" style="max-width:100%;" aria-label="キャンバスステップにLiquidスニペットが追加される様子を示す動画。">
  <source src="{% image_buster /assets/img/shopify/liquid_promo_code.mp4 %}" type="video/mp4">
</video>

キャンペーンやキャンバスで割引コードが何度参照されても、ユーザーに単一のユニークな割引コードを受け取らせたい場合は、最初のメッセージステップの直前に[ユーザー更新]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update)ステップを作成し、割引コードを「Promo Code」のようなカスタム属性に割り当てます。

{% alert tip %}
**Data Settings** > **Custom Attributes** に移動して[カスタム属性を作成]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes)することもできます。
{% endalert %}

ユーザー更新ステップで、各フィールドに対して以下を行います。
- **Attribute Name:** **Promo Code** を選択します。
- **Action:** **Update** を選択します。
- **Key Value:** Liquidのコードスニペットを貼り付けます。

![Liquidスニペットで「Promo Code」属性を更新するユーザー更新ステップ。][6]

これで、カスタム属性 {% raw %}`{{custom_attribute.${Promo Code}}}`{% endraw %} を任意のメッセージに追加でき、割引コードがテンプレート化されます。

## 割引コードの動作 {#discount-code-behavior}

{% details マルチチャネルキャンペーンまたはキャンバスステップ %}

割引コードスニペットがマルチチャネルキャンペーンやキャンバスステップで使用されると、ユーザーは常にユニークなコードを受け取ります。ユーザーが複数のチャネルを通じてコードを受け取る資格がある場合、各チャネルを通じて同じコードを受け取ることになります。つまり、対象となるユーザーは、そのキャンペーンまたはキャンバスステップによって送信されたすべてのメッセージで1つのコードのみを受け取ります。

{% enddetails %}

{% details 異なるキャンバスステップまたは別々のキャンペーン %}

割引コードが同じキャンバス内の複数のステップまたは別々のキャンペーンで参照される場合、対象となるユーザーには複数のユニークなプロモーションコード（各キャンバスステップまたはキャンペーンにつき1つのコード）が発行されます。

{% enddetails %}

[1]: {% image_buster /assets/img/shopify/configure_discount_codes.png %}
[2]: {% image_buster /assets/img/shopify/export_discount_codes.png %}
[3]: {% image_buster /assets/img/shopify/edited_codes_csv.png %}
[4]: {% image_buster /assets/img/shopify/liquid_code_snippet.png %}
[6]: {% image_buster /assets/img/shopify/user_update_step.png %}