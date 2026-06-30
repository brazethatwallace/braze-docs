---
nav_title: コードの使用
article_title: プロモーションコードの使用
page_order: 0.2
description: "CampaignsやCanvasesでプロモーションコードを使用し、使用状況を確認する方法を説明します。"
---

# プロモーションコードの使用 {#use-promotion-codes}

> CampaignsやCanvasesでプロモーションコードを使用し、使用状況を確認する方法を説明します。

## 前提条件 {#prerequisites}

プロモーションコードを使用する前に、[プロモーションコードリストを作成]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/create)する必要があります。

## プロモーションコードの使用 {#using-promotion-codes}

メッセージでプロモーションコードを送信するには、[以前に作成した]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/create#create)プロモーションコードリストの横にある**スニペットをコピー**を選択します。

![メッセージに貼り付けるスニペットをコピーするオプション。]({% image_buster /assets/img/promocodes/promocode9.png %}){: style="max-width:70%"}

コードスニペットをBrazeのメッセージに貼り付け、[Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid)を使用してリストからユニークなプロモーションコードを挿入します。そのコードは送信済みとしてマークされ、他のメッセージが同じコードを送信しないようになります。

![「この春、限定オファーで自分にご褒美を」というメッセージ例の後にコードスニペットが続いている。]({% image_buster /assets/img/promocodes/promocode10.png %}){: style="max-width:70%"}

### キャンバスステップ間での使用 {#across-canvas-steps}

コードスニペットがマルチチャネルメッセージを含むCampaignまたはCanvasで使用される場合、各ユーザーにユニークなコードが割り当てられます。プロモーションコードを参照する複数のステップを持つCanvasでは、ユーザーが入るステップごとに新しいコードが割り当てられます。

Canvasで1つのプロモーションコードを割り当て、ステップ間で再利用するには:

1. 最初のステップ（ユーザーの更新）でプロモーションコードをカスタム属性として割り当てます。
2. 後続のステップでは、新しいコードを生成する代わりに、Liquidを使用してそのカスタム属性を参照します。

ユーザーが複数のチャネルでコードの対象となる場合、各チャネルで同じコードが送信されます。例えば、メールとプッシュの両方でメッセージを受信する場合、同じコードが両方に送信されます。レポートにも単一のコードとして反映されます。

{% alert note %}
利用可能なプロモーションコードがない場合、コードに依存するテストメッセージまたはライブメッセージは送信されません。
{% endalert %}

### アプリ内メッセージCampaign {#promotion-codes-iam-campaigns}

[アプリ内メッセージCampaign]({{site.baseurl}}/user_guide/channels/in_app_messages)を作成した後、アプリ内メッセージの本文に[プロモーションコードリストスニペット]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/manage#using-promotion-codes-1)を挿入できます。アプリ内メッセージのプロモーションコードは、ユーザーがアプリ内メッセージの表示をトリガーした場合にのみ差し引かれ、使用されます。

### テストメッセージ {#test-messages}

テスト送信およびシードグループのメール送信では、別途リクエストしない限りプロモーションコードが消費されます。テスト送信やシードグループのメール送信でプロモーションコードが使用されないようにするには、Brazeアカウントマネージャーに連絡してこの機能の動作を更新してください。

### Currentsでのメッセージエクストラとの使用 {#with-message-extras-for-currents}

{% multi_lang_include partners/shopify.md section='Liquid promotion codes with Currents' %}

## プロモーションコードをユーザープロファイルに保存する {#save-to-profile}

後続のメッセージで同じプロモーションコードを参照するには、コードをカスタム属性としてユーザープロファイルに保存する必要があります。これは、メッセージステップの直前に[ユーザーの更新ステップ]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update)を使用して、割引コードを「Promo Code」などのカスタム属性に割り当てることで実現できます。

まず、ユーザーの更新ステップの各フィールドに以下を選択します:

- **属性名:** Promo Code
- **アクション:** 更新
- **キー値:** プロモーションコードのLiquidコードスニペット（例: {% raw %}`{% promotion('spring25') %}`{% endraw %}）

次に、カスタム属性（この例では {% raw %}`{{custom_attribute.${Promo Code}}}`{% endraw %}）をメッセージに追加します。割引コードがテンプレートとして挿入されます。

## プロモーションコードの使用状況を確認する {#viewing-promotion-code-usage}

残りのコード数は、**プロモーションコード**ページのプロモーションコードリストの**残り**列で確認できます。

![未使用のコードがあるプロモーションコードの例。]({% image_buster /assets/img/promocodes/promocode11.png %})

このコード数は、既存のプロモーションコードリストページを再度開いたときにも確認できます。また、未使用のコードをCSVファイルとしてエクスポートすることもできます。

![残りコード数が992の「Black Friday Sale」というプロモーションコード。]({% image_buster /assets/img/promocodes/promocode12.png %}){: style="max-width:70%"}

## マルチチャネルおよびシングルチャネル送信 {#multichannel-and-single-channel-sends}

マルチチャネルおよび単一送信のCampaignsやCanvasesでは、メッセージのLiquidで参照されるすべてのプロモーションコードは、メッセージが送信される**前に**差し引かれます。これにより以下が保証されます:

- マルチチャネルメッセージのチャネル間で同じプロモーションコードが使用されます。
- メッセージが失敗または中止された場合に、余分なプロモーションコードが使用されません。

ユーザーが1つのメッセージで参照される2つのプロモーションコードリストを持ち、そのメッセージがLiquidの条件分岐タグで分割されている場合でも、ユーザーがどの条件フローに進むかに関係なく、すべてのプロモーションコードが差し引かれます。

ユーザーが新しいキャンバスステップに入るか、Canvasに再入場し、そのユーザーへのメッセージにプロモーションコードのLiquidスニペットが再度適用される場合、新しいプロモーションコードが使用されます。

### 例 {#example}

以下の例では、プロモーションコードリスト`vip-deal`と`regular-deal`の両方が差し引かれます。Liquidは以下の通りです:

{% raw %}
```
{% if user.is_vip %}
  {% promotion('vip-deal') %}
{% else %}
  {% promotion('regular-deal') %}
{% endif %}
```
{% endraw %}

Brazeでは、使用見込み数よりも多くのプロモーションコードをアップロードすることを推奨しています。プロモーションコードリストが期限切れになるか、プロモーションコードが不足した場合、後続のメッセージは中止されます。

{% alert tip %}
**Brazeでのプロモーションコードの消費の仕組みを例えで説明します。**<br><br>メッセージの送信を郵便局で手紙を送ることに例えてみましょう。手紙を窓口係に渡すと、窓口係はその手紙にクーポンを同封する必要があることに気づきます。窓口係はクーポンの束から最初の1枚を取り出し、封筒に入れます。窓口係は手紙を送りますが、何らかの理由で手紙が配達中に紛失してしまいます（クーポンも一緒に失われます）。<br><br>このシナリオでは、Brazeが郵便窓口係であり、プロモーションコードがクーポンです。プロモーションコードの束から取り出された後は、Webhookの結果に関係なく、コードを取り戻すことはできません。
{% endalert %}