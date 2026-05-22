---
nav_title: ダッシュボードツール
article_title: パーソナライゼーション用ダッシュボードツール
page_order: 0
description: "このリファレンス記事では、Brazeのメッセージエディターおよびランディングページエディターにおけるパーソナライゼーションの追加機能について説明します。事前フォーマット済みのLiquid、デフォルト値、カラーラベルや予測候補などのLiquidエディターの拡張機能を含みます。"
---

# パーソナライゼーション用ダッシュボードツール

> Brazeのダッシュボードツールを使用すると、すべてのタグを手動で記述することなくLiquidパーソナライゼーションを挿入できます。**パーソナライゼーションを追加**フローが適切な構文を自動生成し、Liquidエディターがテンプレートの読み取りと拡張を素早くサポートします。

Liquidの構文ルール、サポートされているタグ、高度なパターンについては、[Liquidの使用]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid/)および[サポートされているパーソナライゼーションタグ]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags/)を参照してください。

## コンポーザーと設定でのパーソナライゼーションの追加

**パーソナライゼーションを追加**ツールは、ダッシュボード全体のテンプレート化されたテキストフィールドの近くに表示されます。以下が含まれます。

- **キャンペーンおよびキャンバスステップ**：本文やヘッダーでLiquidをサポートするチャネル（メール、プッシュ、SMS、アプリ内メッセージ、コンテンツカード、webhookなど）。
- **ドラッグ＆ドロップエディター**：コントロールはブロックまたはエディターツールバーに配置されていることが多いです。たとえば、ドラッグ＆ドロップのアプリ内メッセージでは、**パーソナライゼーションを追加**を選択し、パーソナライゼーションタイプを選んでから、生成されたスニペットをコンテンツに配置し、**プレビュー＆テスト**でプレビューできます。チャネル固有の注意事項については、各チャネルのドラッグ＆ドロップまたはコンポーザーの記事（[アプリ内メッセージのスタイル設定]({{site.baseurl}}/user_guide/channels/in_app_messages/customize/style_settings/#adding-liquid)や[ドラッグ＆ドロップでメールを作成]({{site.baseurl}}/user_guide/channels/email/drag_and_drop/)など）を参照してください。
- **専用コンポーザー**：パーソナライゼーションピッカーを公開するもの。たとえば、[アイテムのおすすめ]({{site.baseurl}}/user_guide/brazeai/item_recommendations/using_recommendations/)では、同じスタイルのウィンドウ内で**パーソナライゼーションタイプ**オプション（**アイテムのおすすめ**など）を使用します。
- **ランディングページ**：ドラッグ＆ドロップエディターまたはページおよびブロック設定でLiquidパーソナライゼーションを追加できます。詳細については、[ランディングページのパーソナライズ]({{site.baseurl}}/user_guide/messaging/landing_pages/personalize_landing_pages/)を参照してください。

## 事前フォーマット済み変数とデフォルト値の挿入

**パーソナライゼーションを追加**ツールは、オプションのデフォルト値付きでLiquidを挿入するのに役立ちます。これにより、プロファイルデータが空の場合でもコピーが崩れることがありません。

![パーソナライゼーションの挿入を選択した後に表示されるパーソナライゼーションの追加モーダル。モーダルには、パーソナライゼーションタイプ、属性、オプションのデフォルト値のフィールドがあり、Liquid構文のプレビューが表示されます。]({% image_buster /assets/img_archive/insert_liquid_var_arrow.png %}){: style="max-width:90%;"}

このツールは、カーソルがあった位置に指定したデフォルト値付きのLiquidを挿入します。挿入位置はプレビューボックスでも確認でき、前後のテキストが表示されます。テキストブロックがハイライトされている場合、ハイライトされたテキストが置き換えられます。

![パーソナライゼーションの追加モーダルのGIF。ユーザーがデフォルト値として「fellow traveler」を入力し、モーダルがコンポーザー内のハイライトされたテキスト「name」をLiquidスニペットに置き換える様子を示しています。]({% image_buster /assets/img_archive/insert_var_shot.gif %})

多くのコンポーザーで {% raw %}`{{`{% endraw %} と入力してオートコンプリートを使用したり、他の場所からタグを貼り付けたりすることもできます。詳細については、**Liquidの使用**の[タグの挿入]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid/#inserting-tags)を参照してください。

### 変数の割り当て

{% raw %}
Liquidの一部の操作では、操作したい値を変数として保存する必要があります。Liquidステートメントに複数の属性、イベントプロパティ、またはフィルターが含まれる場合によく発生します。

たとえば、2つのカスタムデータ整数を加算したい場合を考えてみましょう。

#### 不正なLiquidの例

以下は使用できません。

```liquid
{{custom_attribute.${one}}} | plus: {{custom_attribute.${two}}}
```

このLiquidは、1行で複数の属性を参照できないため機能しません。数学関数が実行される前に、これらの値の少なくとも1つに変数を割り当てる必要があります。2つのカスタム属性を加算するには、2行のLiquidが必要です。1行目でカスタム属性を変数に割り当て、2行目で加算を実行します。

#### 正しいLiquidの例

以下を使用できます。

`````````liquid
{% assign value_one = {{custom_attribute.${one}}} %}
{% assign result = value_one | plus: {{custom_attribute.${two}}} %}
```

#### チュートリアル: 変数を使用して残高を計算する

ユーザーの現在の残高を、ギフトカード残高と報酬残高を加算して計算してみましょう。

まず、`assign` タグを使用して、カスタム属性 `current_rewards_balance` を「balance」という用語に置き換えます。これにより、操作可能な `balance` という名前の変数が作成されます。

`````````liquid
{% assign balance = {{custom_attribute.${current_rewards_balance}}} %}
```

次に、`plus` フィルターを使用して、各ユーザーのギフトカード残高と報酬残高（`{{balance}}` で表される）を合算します。

`````````liquid
{% assign balance = {{custom_attribute.${current_rewards_balance}}} %}
You have ${{custom_attribute.${giftcard_balance} | plus: {{balance}}}} to spend!
```
{% endraw %}

{% alert tip %}
すべてのメッセージで同じ変数を割り当てていませんか？`assign` タグを何度も書く代わりに、そのタグをコンテンツブロックとして保存し、メッセージの先頭に配置できます。<br><br>

1. [コンテンツブロックを作成]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks/#create-a-content-block)します。
2. コンテンツブロックに名前を付けます（スペースや特殊文字は使用しないでください）。
3. ページ下部の**編集**を選択します。
4. `assign` タグを入力します。

コンテンツブロックがメッセージの先頭にある限り、変数がオブジェクトとしてメッセージに挿入されるたびに、選択したカスタム属性を参照します。
{% endalert %}

## Liquidエディターの拡張機能

これらのダッシュボード機能により、メッセージの作成中にLiquidをより簡単に扱えるようになります。

### カラーラベル

各Liquid要素は色に対応しており、Liquidエディターで一目でLiquidを区別できます。

![さまざまなLiquid要素に対応するカラーラベルの図。]({% image_buster /assets/img/liquid_color_code.png %})

### 予測Liquid

パーソナライズされたメッセージを作成する際に、カスタム属性、属性名などに対して予測Liquidを使用することもできます。

![フィールドにテキストが入力されるにつれて、BrazeがさまざまなLiquid属性を推奨する様子。]({% image_buster /assets/img/liquid_auto_complete.gif %}){: style="max-width:70%;"}

## 次のステップ

- [Liquidの使用]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid/) — Brazeでの構文、`assign`、条件分岐、フィルター
- [デフォルト値の設定]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/setting_default_values/) — モーダル以外でのLiquidのデフォルト値
- [フィルター]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/filters/) — 日付、数学、文字列などのフォーマット