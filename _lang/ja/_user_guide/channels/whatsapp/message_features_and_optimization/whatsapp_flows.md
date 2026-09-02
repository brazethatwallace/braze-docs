---
nav_title: WhatsApp Flows
article_title: WhatsApp Flows
page_order: 3
description: "このリファレンス記事では、WhatsApp Flowsメッセージの構築と作成に関するステップについて説明します。"
alias: /whatsapp_flows/
page_type: reference
tool:
  - Canvas
channel:
  - WhatsApp
---

# WhatsApp Flows

> WhatsApp Flowsは、既存のWhatsAppチャネルの拡張機能であり、インタラクティブでダイナミックなメッセージングエクスペリエンスを作成できます。このページでは、WhatsApp Flowsの使用方法をステップごとに説明します。

## WhatsApp Flowsの設定 {#setting-up-whatsapp-flows}

1. Metaアカウントにログインします。
2. 以下の2つの主要な場所のいずれかからFlowsを作成します。
    - **アカウントツール：** **Flows**タブに移動して、Flow IDを表示し、新しいFlowを作成します。
    - **テンプレートの管理：** Flowsを作成する場合は、この方法が推奨されます。ここでは、テンプレートを生成し、テンプレート作成プロセス中にFlowオプションを選択できます。

![Flowsテンプレートを作成するページが表示されたWhatsApp Manager。]({% image_buster /assets/img/whatsapp/flows/create_flows_template.png %})

{% alert tip %}
Brazeの[WhatsAppテンプレートビルダー]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/template_builder)を使用して、マーケティングまたはユーティリティのFlowテンプレートを作成することもできます。MetaのWhatsApp ManagerでFlow自体を作成・管理し、Brazeでテンプレートを作成する際にそのFlowを選択します。
{% endalert %}

{: start="3"}
3. 既存のFlowを選択するか、新しいFlowを作成します。Flowを作成する場合は、以下の2つのオプションから選択します。
  - **カスタムフォーム：** 特定の要件がある場合
  - **デザイン済み要素：** より迅速な設定を行う場合

## WhatsApp Flowメッセージとレスポンスの設定 {#configuring-whatsapp-flow-messages-and-responses}

{% tabs local %}
{% tab テンプレートメッセージ %}

1. Brazeキャンバスで、該当するFlowを含むテンプレートメッセージを使用するWhatsAppメッセージステップを作成します。
2. テンプレートの作成を続けます。必要に応じて、メディアや変数コンテンツ、またはその両方をメッセージに追加します。Flowの選択はテンプレート作成時に行われるため、Flowエクスペリエンスの追加情報は不要です。

![WhatsApp Flowテンプレートを使用したWhatsAppメッセージ作成画面。]({% image_buster /assets/img/whatsapp/flows/composer_flow_template.png %}){: style="max-width:80%;"}

{% endtab %}
{% tab レスポンスメッセージ %}

1. Brazeキャンバスで、レスポンスメッセージとFlowメッセージを使用するWhatsAppメッセージステップを作成します。

![WhatsAppレスポンスメッセージタイプとFlowメッセージレイアウトのメッセージステップ。]({% image_buster /assets/img/whatsapp/flows/message_step_flow_message.png %}){: style="max-width:80%;"}

{: start="2"}
2. 該当するFlowを選択し、メッセージの作成を続けます。

![Flowを選択するためのドロップダウンが展開されたFlowメッセージレスポンス作成画面。]({% image_buster /assets/img/whatsapp/flows/flow_message_composer.png %}){: style="max-width:80%;"}

{% endtab %}
{% endtabs %}

### Flowのプレビュー {#preview-flow}

Flowを含むキャンバスを起動する前に、**Preview Flow**を選択してBraze内で直接Flowをプレビューし、期待どおりに動作することを確認できます。また、プレビューでFlowを操作して、ユーザーがFlowをどのようにナビゲートするかを体験し、リアルタイムで調整を行うこともできます。Flowに複数のページが含まれている場合は、各ページを操作できます。

![ユーザーがサインアップを完了するためのフォームを表示するプレビューウィンドウ。]({% image_buster /assets/img/whatsapp/flows/flow_preview.png %}){: style="max-width:50%;"}

## Flowレスポンス全体の保存 {#full-flow}

WhatsApp FlowメッセージをBrazeのキャンバスやキャンペーンに組み込む際、ユーザーがFlowを通じて送信した特定の情報をキャプチャして活用したい場合があります。Brazeは、ユーザーレスポンスの構造に関する追加情報、具体的にはJSONレスポンスの期待される形状を受け取る必要があり、これにより必要な階層化カスタム属性（NCA）スキーマを生成します。

### ステップ 1: Flowカスタム属性の生成 {#step-1-generate-the-flow-custom-attribute}

{% tabs local %}
{% tab 推奨方法 %}

レスポンス構造に関する情報をBrazeに提供する最も簡単な方法は、Flowレスポンスをカスタム属性として保存し、テスト送信を完了することです。

#### Brazeで使用されたことのないFlowを使用する場合 {#using-a-flow-that-hasnt-been-used-in-braze}

Braze内で以前使用されたことのないFlowを使用している場合、**メッセージの作成**で**Flowカスタム属性**セクションを表示すると、情報が表示されないことがあります。これは、スキーマがまだ生成されていないことを意味します。

![Flowカスタム属性を表示するオプションがあるMeta Flowセクション。]({% image_buster /assets/img/whatsapp/flows/flow_custom_attribute.png %}){: style="max-width:70%;"}

これを解決するには、以下の手順を実行します。

1. WhatsAppメッセージステップの設定を完了します。
2. **Flowレスポンスをカスタム属性として保存**にチェックが入っていることを確認します。
3. 自分自身にテストメッセージを送信し、ユーザーとしてFlowを完了します。

これで、BrazeはFlowレスポンスJSONの形状を取得し、カスタム属性を生成できます。

{% endtab %}
{% tab 代替方法 %}

高度なJSONエディターを使用してFlowレスポンスの属性をカスタム属性に保存するか、マルチステップキャンバスを使用してレスポンスを階層化カスタム属性に保存します。

{% subtabs %}
{% subtab 高度なJSONエディター %}

高度なJSONエディターで、{% raw %}`{"attributes": [{"flow_1": {{whats_app.${inbound_flow_response}}}}]}`{% endraw %} と入力します。ここで「flow_1」は、Flowの保存先となるカスタム属性です。

![高度なJSONエディターを使用したユーザーの更新ステップ。]({% image_buster /assets/img/whatsapp/flows/user_update_advanced_json_editor.png %})

{% endsubtab %}
{% subtab UIエディター %}

1. ワークスペースのデータ設定内に、オブジェクトデータタイプのカスタム属性（この例では「flow_1」）がすでに作成されていることを確認します。
2. UIエディターで、Liquid {% raw %}`{{whats_app.${inbound_flow_response}}}`{% endraw %} を使用してカスタム属性にデータを入力し、ユーザーのFlowレスポンス全体を保存します。作成したカスタム属性を選択する前に、キー値を {% raw %}`{{whats_app.${inbound_flow_response}}}`{% endraw %} として入力する必要があります。

![UIエディターを使用したユーザーの更新ステップ。]({% image_buster /assets/img/whatsapp/flows/user_update_ui_editor.png %})

BrazeがFlowレスポンスを受信すると、指定された命名規則で階層化カスタム属性をユーザープロファイルに保存します。そのカスタム属性は、キャンバスの構築時に取得できます。

![「flow_1」カスタム属性の内容を表示するウィンドウ。]({% image_buster /assets/img/whatsapp/flows/user_attribute_flow.png %})

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### ステップ 2: 保存されたFlowレスポンスの表示 {#step-2-view-the-saved-flow-response}

Flowが完了すると、BrazeはFlow IDに基づいた名前でFlowカスタム属性を自動的に作成します。その後、ユーザープロファイルに移動して、**カスタム属性**セクションで保存されたFlowレスポンスをネストされたオブジェクトとして表示できます。

スキーマが生成されると、Flow**カスタム属性**セクションに、各レスポンスの予想されるデータタイプ（例：「文字列」や「文字列配列」）を含む期待される構造が表示されます。

![スキーマドロップダウンが表示されたFlowカスタム属性の詳細ウィンドウ。]({% image_buster /assets/img/whatsapp/flows/flow_custom_attribute_details.png %}){: style="max-width:80%;"}

### 考慮事項 {#considerations}

- **既存の属性:** 特定のFlowのカスタム属性がすでに生成されている場合、Flowはその属性情報を読み込んだ状態で表示されます。この場合、Brazeはすでに期待されるレスポンスメッセージを認識しているため、スキーマを生成するためにテストメッセージを送信する必要はありません。
- **Flowの変更:** スキーマ生成後にFlowに変更を加えた場合、Flowレスポンスの形状が変更されたことをBrazeが理解し、属性構造を適切に調整できるように、追加のテストメッセージを送信する必要があります。このアクションは24時間に1回に制限されています。
- **一貫性:** 生成されたFlowカスタム属性は一貫しており、使用されるキャンバスに関係なく、この特定のFlowに対して同じ属性になります。
- **手動オプション:** **Flowレスポンスをカスタム属性として保存**チェックボックスを選択する必要はありません。[Flowレスポンスから特定のフィールドを特定のカスタム属性に保存する](#saving-specific-fields-from-flow-responses-to-a-specific-custom-attribute)ことで、カスタム属性を手動で生成でき、ユーザーステップの重複を回避できます。

## Flowの回答から特定のフィールドを特定のカスタム属性に保存する {#saving-specific-fields-from-flow-responses-to-a-specific-custom-attribute}

### ステップ1：アクションパスを作成する {#step-1-create-an-action-path}

[アクションパス]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths)キャンバスステップまたはアクションベースのキャンペーンを作成します。**WhatsApp受信メッセージを送信**トリガーと**Flowに回答済み**条件を選択し、該当するFlowまたは**任意のFlow**を選択します。

![WhatsApp受信メッセージを送信し、任意のFlowに回答したユーザーに対するトリガー。]({% image_buster /assets/img/whatsapp/flows/trigger_responded_flow.png %})

### ステップ2：Flowの回答からフィールドを抽出する {#step-2-extract-fields-from-flow-responses}

階層化カスタム属性または`json_parse` Liquidタグを使用して、Flowの回答から特定のフィールドを抽出できます。

{% tabs %}
{% tab 階層化カスタム属性 %}

ユーザーのFlow回答の特定の部分を保存するには、[Flowの完全な回答を保存する](#full-flow)のすべてのステップを完了してください（**キャンバスの起動を含む**）。参照する階層化カスタム属性を作成するために、キャンバスを起動する必要があります。キャンバスを起動してFlowを完了したら、以下のステップを実行します。

1. UIエディターを使用する後続のユーザー更新ステップを作成します。
2. **パーソナライゼーションを追加**を選択し、**階層化カスタム属性**とFlowが保存されている対応するトップレベルの属性を選択します。

![階層化カスタム属性のパーソナライゼーションを含むユーザー更新ステップ。]({% image_buster /assets/img/whatsapp/flows/nested_custom_attributes.png %})

{: start="3" }
3. 保存したいキー属性を選択し、Liquidを**キー値**フィールドに挿入します。

![選択可能な属性を含む「flow_1」のウィンドウ。]({% image_buster /assets/img/whatsapp/flows/attribute_key.png %})

{: start="4" }
4. 保存先の属性を選択します。
5. テストメッセージを送信してFlowをテストします。

{% endtab %}
{% tab Parse関数 %}

`json_parse` Liquidタグを使用して、Flowから特定の回答を抽出します。たとえば、Flowトークンと選択されたオプションを取り出して、フォローアップメッセージをカスタマイズできます。

UIエディターで以下を選択します。

- **属性名：** YOUR_CUSTOM_ATTRIBUTE（この例では「First_name」）
- **アクション：** 更新
- **キー値：** {% raw %} `{% assign parsed_json = {{whats_app.${inbound_flow_response}}} | json_parse %}{{ parsed_json.FIELDS_THAT_APPLY }}`{% endraw %}

![カスタム属性`inbound_flow_response`を使用したWhatsAppプロパティのパーソナライゼーションを挿入する「パーソナライゼーションを追加」コンポーネントを含むWhatsAppメッセージ作成画面。]({% image_buster /assets/img/whatsapp/flows/parsed_json.png %})

準備ができたら、テストメッセージを送信してFlowをテストします。その後、キャンバスを起動してください。

{% endtab %}
{% endtabs %}

{% alert note %}
新しいWhatsAppメッセージは、キャンバスがLiquid Flowの回答を使用（および再使用）する機能を「クリア」します。そのため、フォローアップメッセージは、Liquid Flowの回答を使用するすべてのユーザー更新ステップ、webhook、またはその他のステップの後に配置してください。
{% endalert %}

## Flowパーソナライゼーションタグの追加 {#adding-a-flow-personalization-tag}

[サポートされているパーソナライゼーションタグ]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags)でLiquidを使用してFlowのレスポンスを利用するには、以下のステップを完了してください。

1. WhatsAppメッセージを作成する際に、<i class="fas fa-plus-circle" aria-label="パーソナライゼーションを追加"></i> **パーソナライゼーションを追加**を選択して、**パーソナライゼーションを追加**ウィンドウを開きます。
2. パーソナライゼーションタイプとして**WhatsAppプロパティ**を選択し、カスタム属性として**inbound_flow_response**を選択します。これにより、ユーザープロファイルに情報を保存したり、メッセージに含めたり、webhookなどの他のサービスに転送したりできます。

![WhatsAppメッセージ作成画面。「パーソナライゼーションを追加」コンポーネントにより、カスタム属性 inbound_flow_response を使用したWhatsAppプロパティのパーソナライゼーションを挿入できます。]({% image_buster /assets/img/whatsapp/flows/inbound_flow_response.png %}){: style="max-width:80%;"}

ご質問やサポートが必要な場合は、[サポート]({{site.baseurl}}/user_guide/administer/personal/braze_support)にお問い合わせください。