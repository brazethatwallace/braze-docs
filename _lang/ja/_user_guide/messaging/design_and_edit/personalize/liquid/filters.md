---
nav_title: フィルター
article_title: Liquid フィルター
page_order: 3
description: "このリファレンスページでは、静的または動的コンテンツを再フォーマットするために使用できるフィルターを一覧にしています。"

---

# フィルター {#filters}

> このリファレンス記事では、Liquidのフィルターの概要と、Brazeでサポートされているフィルターについて説明します。これらのフィルターの活用アイデアをお探しですか？[Liquidユースケースライブラリー]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/liquid_use_cases)をご覧ください。

フィルターは、Liquidで数値、文字列、変数、オブジェクトの出力を変更する方法です。フィルターを使用して、文字列を小文字から大文字に変換したり、加算や除算などの数学的演算を実行したりするなど、静的または動的テキストを再フォーマットできます。

{% alert important %}
BrazeはShopifyのすべてのLiquidフィルターをサポートしているわけではありません。このページでは、Brazeがテスト済みのLiquidフィルターの概要を説明していますが、完全なリストではない場合があります。メッセージを送信する前に、必ずLiquidをテストしてください。<br><br>ここに記載されていないフィルターについてご質問がある場合は、カスタマーサクセスマネージャーにお問い合わせください。
{% endalert %}

## フィルターの構文 {#filter-syntax}

{% raw %}

フィルターは出力タグ `{{ }}` 内に配置し、パイプ文字 `|` で示します。

{% endraw %}

{% tabs local %}
{% tab 入力 %}
{% raw %}
```liquid
{{"Big Sale" | upcase}}
```
{% endraw %}
{% endtab %}
{% tab 出力 %}
{% raw %}
```liquid
BIG SALE
```
{% endraw %}
{% endtab %}
{% endtabs %}

この例では、`Big Sale` が文字列で、`upcase` が適用されるフィルターです。

{% alert note %}
フィルターは `assign` ステートメントと出力タグ {% raw %}(`{{ }}`){% endraw %} で使用できますが、条件文（`if`、`elsif`、`unless`）、`case`/`when`、`for` ループ、または配列アクセスブラケットでは使用できません。これらのコンテキストでフィルター処理された値を使用するには、まず結果を変数に割り当ててください。詳細については、[演算子とフィルターの使用場所]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid#where-to-use-operators-and-filters)を参照してください。
{% endalert %}

### 複数フィルターの構文 {#syntax-for-multiple-filters}

1つの出力に複数のフィルターを使用できます。フィルターは左から右の順に適用されます。

{% tabs local %}
{% tab 入力 %}
{% raw %}
```liquid
 {{ "Big Sale" | upcase | remove: "BIG" }}
```
{% endraw %}
{% endtab %}
{% tab 出力 %}
{% raw %}
```liquid
SALE
```
{% endraw %}
{% endtab %}
{% endtabs %}

## 配列フィルター {#array-filters}

配列フィルターは、配列の出力を変更するために使用します。

| フィルター | 定義 | サポート |
| :------------------- | :----------------------------------------------------------------------------------------------------------------- | :-------- |
| [join](https://shopify.dev/docs/api/liquid/filters/join) | パラメーターとして渡された文字で配列の要素を結合します。結果は単一の文字列になります。 | ✅  対応 |
| [first](https://shopify.dev/docs/api/liquid/filters/first) | 配列の最初の要素を返します。カスタム属性配列では、最も古く追加された値です。 | ✅  対応 |
| [last](https://shopify.dev/docs/api/liquid/filters/last) | 配列の最後の要素を返します。カスタム属性配列では、最も最近追加された値です。 | ✅  対応 |
| [compact](https://shopify.dev/api/liquid/filters/compact) | 配列から `nil` アイテムを削除します。 | ✅  対応 |
| [concat](https://shopify.dev/api/liquid/filters/concat) | 配列を別の配列と結合します。 | ✅  対応 |
| [find_index](https://shopify.dev/docs/api/liquid/filters/find_index) | 配列内の指定されたインデックス位置にあるアイテムを返します。配列の最初のアイテムは `[0]` で参照されます。 | ⛔  非対応 |
| [map](https://shopify.dev/api/liquid/filters/map) | 配列要素の属性をパラメーターとして受け取り、各配列要素の値から配列を作成します。 | ✅  対応 |
| [reverse](https://shopify.dev/api/liquid/filters/reverse) | 配列内のアイテムの順序を逆にします。 | ✅  対応 |
| [size](https://shopify.dev/api/liquid/filters/size) | 文字列のサイズ（文字数）または配列のサイズ（要素数）を返します。 | ✅  対応 |
| [slice](https://shopify.dev/api/liquid/filters/slice) | 指定されたインデックスから始まる文字列の部分文字列または配列のサブセットを返します。 | ✅  対応 |
| [sort](https://shopify.dev/api/liquid/filters/sort) | 配列内の要素の指定された属性で配列の要素をソートします。 | ✅  対応 |
| [sort_natural](https://shopify.dev/api/liquid/sort_natural) | 大文字小文字を区別しないアルファベット順で配列内のアイテムをソートします。 | ✅  対応 |
| [uniq](https://shopify.dev/api/liquid/filters/uniq) | 配列内の要素の重複インスタンスを削除します。 | ✅  対応 |
| [where](https://shopify.dev/api/liquid/where) | 特定のプロパティ値を持つアイテムのみを含むように配列をフィルタリングします。 | ✅  対応 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Array filters" }

## カラーフィルター {#color-filters}

[カラーフィルター](https://shopify.dev/api/liquid/filters/color-filters)はBrazeではサポートされていません。

## フォントフィルター {#font-filters}

[フォントフィルター](https://shopify.dev/api/liquid/filters/font-filters)はBrazeではサポートされていません。

## 数学フィルター {#math-filters}

数学フィルターを使用すると、数学的演算を実行できます。1つの出力に複数のフィルターを使用する場合、左から右の順に適用されます。

| フィルター | 定義 | サポート |
| :------ |:----------------| :-------- |
| [abs](https://shopify.dev/api/liquid/filters/abs) | 数値の絶対値を返します。 | ✅  対応 |
| [at_most](https://shopify.dev/api/liquid/filters/at_most) | 数値を最大値に制限します。 | ✅  対応 |
| [at_least](https://shopify.dev/api/liquid/filters/at_least) | 数値を最小値に制限します。 | ✅  対応 |
| [ceil](https://shopify.dev/api/liquid/filters/ceil) | 出力を最も近い整数に切り上げます。 | ✅  対応 |
| [divided_by](https://shopify.dev/api/liquid/filters/divided_by) | 出力を数値で除算します。出力は最も近い整数に切り捨てられます。丸めを防ぐ方法については、以下のヒントを確認してください。 | ✅  対応 |
| [floor](https://shopify.dev/api/liquid/filters/floor) | 出力を最も近い整数に切り捨てます。 | ✅  対応 |
| [minus](https://shopify.dev/api/liquid/filters/minus) | 出力から数値を減算します。 | ✅  対応 |
| [plus](https://shopify.dev/api/liquid/filters/plus) | 出力に数値を加算します。 | ✅  対応 |
| [round](https://shopify.dev/api/liquid/filters/round) | 出力を最も近い整数または指定された小数点以下の桁数に丸めます。 | ✅  対応 |
| [times](https://shopify.dev/api/liquid/filters/times) | 出力に数値を乗算します。 | ✅  対応 |
| [modulo](https://shopify.dev/api/liquid/filters/modulo) | 出力を数値で除算し、余りを返します。 | ✅  対応 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Math filters" }

{% alert tip %}
Liquidで整数（整数値）を整数で除算する場合、答えが浮動小数点数（小数を含む数値）であっても、Liquidは自動的に最も近い整数に切り捨てます。ただし、整数を浮動小数点数で除算すると、常に浮動小数点数が返されます。つまり、整数を浮動小数点数（1.0、2.0、3.0）に変換することで、浮動小数点数を返すことができます。
{% raw %}
<br><br>例えば、`{{15 | divided_by: 2}}` は `7` を出力しますが、`{{15 | divided_by: 2.0}}` は `7.5` を出力します。
{% endraw %}
{% endalert %}

### カスタム属性を使った数学的演算 {#mathematical-operations-with-custom-attributes}

2つのカスタム属性間で数学的演算を実行することはできない点に注意してください。

{% raw %}

```liquid
{{custom_attribute.${current_rewards_balance} | plus: {{custom_attribute.${giftcard_balance}}}}}
```

この例は、1行のLiquidで複数のカスタム属性を参照できないため、動作しません。代わりに、数学関数を実行する前に、これらの値の少なくとも1つを変数に割り当てる必要があります。2つのカスタム属性を加算するには、2行のLiquidが必要です。

1. カスタム属性を変数に割り当てる行
2. 加算を実行する行

#### ユースケース: 現在の残高を計算する {#use-case-calculate-current-balance}

ギフトカード残高とリワード残高を加算して、ユーザーの現在の残高を計算したいとします。

1. `assign` タグを使用して、`current_rewards_balance` のカスタム属性を「balance」という用語に置き換えます。これにより、操作可能な `balance` という名前の変数が作成されます。

```liquid
{% assign balance = {{custom_attribute.${current_rewards_balance}}} %}
```

{: start="2"}
2. `plus` フィルターを使用して、各ユーザーのギフトカード残高とリワード残高（`{{balance}}` オブジェクトで表される）を結合します。
{% endraw %}
{% tabs local %}
{% tab 入力 %}
{% raw %}
```liquid
{% assign balance = {{custom_attribute.${current_rewards_balance}}} %}
You have ${{custom_attribute.${giftcard_balance} | plus: {{balance}}}} to spend!
```
{% endraw %}
{% endtab %}
{% tab 出力 %}
{% raw %}
```liquid
You have $35 to spend!
```
{% endraw %}
{% endtab %}
{% endtabs %}

## 通貨フィルター {#money-filters}

購入情報、口座残高、または金額に関する情報をユーザーに通知する場合は、通貨フィルターを使用する必要があります。通貨フィルターは、小数点が正しい位置にあること、および数値の一部が失われないこと（末尾の厄介な `0` など）を保証します。

| フィルター | 定義 | サポート |
| :--------------- | :--------------- | :-------- |
| [money](https://shopify.dev/api/liquid/filters/money) | 小数点が正しい位置にあり、数値の末尾からゼロが削除されないように数値をフォーマットします。 | ✅  対応 |
| [money_with_currency](https://shopify.dev/api/liquid/filters/money_with_currency) | 通貨記号付きで数値をフォーマットします。 | ⛔  非対応 |
| [money_without_currency](https://shopify.dev/api/liquid/filters/money_without_currency) | 通貨記号なしで数値をフォーマットします。 | ⛔  非対応 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Money filters" }

{% alert important %}
`money` フィルターで数値を正しくフォーマットするには、数値からカンマを削除し、`money` フィルターの前に `plus: 0` フィルターを追加してください。例えば、以下のLiquidを参照してください。<br><br>
{% raw %}
```liquid
{% assign my_int = "350000.25" | plus: 0 %}
{{ my_int | money }}
```
{% endraw %}
{% endalert %}

### Shopifyのmoneyフィルターと Brazeのmoneyフィルターの違い {#shopify-money-filter-versus-braze-money-filter}

{% alert warning %}
Shopifyの `money` フィルターの動作は、Brazeでの使用方法とは異なります。期待される動作の正確な説明については、以下の例を参照してください。
{% endalert %}

{% raw %}
カスタム属性（`account_balance` など）を入力する場合は、常に `money` フィルターを使用して、小数点を正しい位置に配置し、数値の末尾からゼロが削除されないようにする必要があります。

```liquid
${{custom_attribute.${account_balance} | money}}
```
{% endraw %}

| MONEYフィルターあり | MONEYフィルターなし |
| :------------------------------------------ | :------------------------------------------ |
| ![moneyフィルターを適用した場合の表示]({% image_buster /assets/img/with_money_filter.png %}) | ![moneyフィルターを適用しない場合の表示]({% image_buster /assets/img/without_money_filter.png %}) |
| `account_balance` が `17.8` として入力された場合。 | `account_balance` が `17.8` として入力された場合。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Shopify money filter versus Braze money filter" }

Brazeの `money` フィルターは、プリセット設定に従って自動的に小数点を適用しないため、Shopifyとは異なります。例えば、`rewards_redeemed` に `145` の値が含まれている以下のシナリオを見てみましょう。

{% tabs local %}
{% tab 入力 %}
{% raw %}
```liquid
${{event_properties.${rewards_redeemed} | money }}
```
{% endraw %}
{% endtab %}
{% tab 出力 %}
{% raw %}
```liquid
$145.00
```
{% endraw %}
{% endtab %}
{% endtabs %}

Shopifyの [money](https://shopify.dev/api/liquid/filters/money) フィルターによると、出力は `$1.45` になるはずですが、Brazeでは `$145.00` という出力になります。回避策として、`divided_by` フィルターを使用して数値を小数に変換してから、moneyフィルターを適用できます。

{% tabs local %}
{% tab 入力 %}
{% raw %}
```liquid
${{event_properties.${rewards_redeemed} | divided_by: 100.00 | money }}
```
{% endraw %}
{% endtab %}
{% tab 出力 %}
{% raw %}
```liquid
$1.45
```
{% endraw %}
{% endtab %}
{% endtabs %}

## 文字列フィルター {#string-filters}

文字列フィルターは、文字列の出力と変数を操作するために使用します。文字列は英数字の組み合わせで、ストレート引用符で囲む必要があります。

{% alert note %}
Liquidでは、ストレート引用符とカーリー引用符は異なります。テキストエディターからBrazeにLiquidをコピー＆ペーストする際は注意してください。カーリー引用符を使用すると、Liquidでエラーが発生します。Brazeで直接Liquidを記述する場合は、ストレート引用符が自動的に適用されます。
{% endalert %}

| フィルター | 説明 | サポート |
| :--------------- | ------------- | --------- |
| [append](https://shopify.dev/api/liquid/filters/append) | 文字列に文字を追加します。 | ✅  対応 |
| [camelize](https://shopify.dev/docs/api/liquid/filters/camelize) | 文字列をキャメルケースに変換します。 | ⛔  非対応 |
| [capitalize](https://shopify.dev/api/liquid/filters/capitalize) | 文字列の最初の単語を大文字にし、残りの文字を小文字にします。 | ✅  対応 |
| [downcase](https://shopify.dev/api/liquid/filters/downcase) | 文字列を小文字に変換します。 | ✅  対応 |
| [escape](https://shopify.dev/api/liquid/filters/escape) | 文字列をエスケープします。 | ✅  対応 |
| [handleize](https://shopify.dev/api/liquid/filters/handleize) | 文字列をハンドル形式にフォーマットします。 | ⛔  非対応 |
| [md5](https://shopify.dev/api/liquid/filters/md5) | 文字列をMD5ハッシュに変換します。詳細については、[エンコーディングフィルター]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters#encoding-filters)を参照してください。 | ✅  対応 |
| [sha1](https://shopify.dev/api/liquid/filters/sha1) | 文字列をSHA-1ハッシュに変換します。詳細については、[エンコーディングフィルター]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters#encoding-filters)を参照してください。 | ✅  対応 |
| hmac_sha1_hex<br>(旧 [hmac_sha_1](https://shopify.dev/api/liquid/filters/string-filters#hmac_sha1)) | ハッシュメッセージ認証コード（HMAC）を使用して文字列をSHA-1ハッシュに変換します。メッセージの秘密鍵をフィルターのパラメーターとして渡します。詳細については、[エンコーディングフィルター]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters#encoding-filters)を参照してください。 | ✅  対応 |
| [hmac_sha256](https://shopify.dev/api/liquid/filters/hmac_sha256) | ハッシュメッセージ認証コード（HMAC）を使用して文字列をSHA-256ハッシュに変換します。メッセージの秘密鍵をフィルターのパラメーターとして渡します。 | ✅  対応 |
| hmac_sha512 | ハッシュメッセージ認証コード（HMAC）を使用して文字列をSHA-512ハッシュに変換します。メッセージの秘密鍵をフィルターのパラメーターとして渡します。 | ✅  対応 |
| [newline_to_br](https://shopify.dev/api/liquid/filters/newline_to_br) | 文字列内の各改行の前に `<br>` 改行HTMLタグを挿入します。 | ✅  対応 |
| [pluralize](https://shopify.dev/api/liquid/filters/pluralize) | 数値の値に基づいて、英語の文字列の単数形または複数形を出力します。 | ⛔  非対応 |
| [prepend](https://shopify.dev/api/liquid/filters/prepend) | 文字列の先頭に文字を追加します。 | ✅  対応 |
| [remove](https://shopify.dev/api/liquid/filters/remove) | 文字列から部分文字列のすべての出現を削除します。 | ✅  対応 |
| [remove_first](https://shopify.dev/api/liquid/filters/remove_first) | 文字列から部分文字列の最初の出現のみを削除します。 | ✅  対応 |
| [replace](https://shopify.dev/api/liquid/filters/replace) | 文字列のすべての出現を部分文字列で置換します。 | ✅  対応 |
| [replace_first](https://shopify.dev/api/liquid/filters/replace_first) | 文字列の最初の出現を部分文字列で置換します。 | ✅  対応 |
| [slice](https://shopify.dev/api/liquid/filters/slice) | sliceフィルターは、指定されたインデックスから始まる部分文字列を返します。 | ✅  対応 |
| [split](https://shopify.dev/api/liquid/filters/split) | splitフィルターは、パラメーターとして部分文字列を受け取ります。この部分文字列は、文字列を配列に分割するための区切り文字として使用されます。 | ✅  対応 |
| [strip](https://shopify.dev/api/liquid/filters/strip) | 文字列の左右からタブ、スペース、改行（すべての空白文字）を除去します。 | ✅  対応 |
| [lstrip](https://shopify.dev/api/liquid/filters/lstrip) | 文字列の左側からタブ、スペース、改行（すべての空白文字）を除去します。 | ⛔  非対応 |
| [rstrip](https://shopify.dev/api/liquid/filters/rstrip) | 文字列の右側からタブ、スペース、改行（すべての空白文字）を除去します。 | ⛔  非対応 |
| [strip_html](https://shopify.dev/api/liquid/filters/strip_html) | 文字列からすべてのHTMLタグを除去します。 | ✅  対応 |
| [strip_newlines](https://shopify.dev/api/liquid/filters/strip_newlines) | 文字列から改行を削除します。 | ✅  対応 |
| [truncate](https://shopify.dev/api/liquid/filters/truncate) | 最初のパラメーターとして渡された文字数まで文字列を切り詰めます。省略記号（...）が切り詰められた文字列に追加され、文字数に含まれます。 | ✅  対応 |
| [truncatewords](https://shopify.dev/api/liquid/filters/truncatewords) | 最初のパラメーターとして渡された単語数まで文字列を切り詰めます。省略記号（...）が切り詰められた文字列に追加されます。 | ✅  対応 |
| [upcase](https://shopify.dev/api/liquid/filters/upcase) | 文字列を大文字に変換します。 | ✅  対応 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="String filters" }

## 追加のフィルター {#additional-filters}

以下の汎用フィルターは、コンテンツのフォーマットや変換など、さまざまな目的に使用できます。

| フィルター | 説明 | サポート |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------- | :-------- |
| [date](https://shopify.dev/api/liquid/filters/date) | タイムスタンプを別の日付形式に変換します。詳細については、[日付フィルター](#date-filter)を参照してください。 | ✅  対応 |
| [default](https://shopify.dev/api/liquid/filters/default) | 値が割り当てられていない変数にデフォルト値を設定します。文字列、配列、ハッシュで使用できます。 | ✅  対応 |
| [format_address](https://shopify.dev/api/liquid/filters/format_address) | ロケールに応じた順序で住所の要素を出力するように住所をフォーマットします。 | ⛔  非対応 |
| [highlight](https://shopify.dev/api/liquid/filters/highlight) | 送信された検索語に一致する場合、検索結果内の単語をhighlightクラスを持つHTML `<strong>` タグで囲みます。 | ⛔  非対応 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Additional filters" }

エンコーディングフィルターやURLフィルターなど、その他のサポートされているフィルターについては、[高度なフィルター]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters)ページをご覧ください。

### 日付フィルター {#date-filter}

`date` フィルターを使用して、タイムスタンプを別の日付形式に変換できます。`date` フィルターにパラメーターを渡して、タイムスタンプを再フォーマットできます。これらのパラメーターの例については、[strfti.me](http://www.strfti.me/) を参照してください。

例えば、`date_attribute` の値がタイムスタンプ `2021-06-03 17:13:41 UTC` であるとします。

{% tabs local %}
{% tab 入力 %}
{% raw %}
```liquid
{{custom_attribute.${date_attribute} | date: '%b %d'}}
```
{% endraw %}
{% endtab %}
{% tab 出力 %}
{% raw %}
```liquid
03 June
```
{% endraw %}
{% endtab %}
{% endtabs %}

`strftime` フォーマットオプションに加えて、Brazeは `%s` 日付フィルターを使用してタイムスタンプをUnix時間に変換することもサポートしています。例えば、`date_attribute` をUnix時間で取得するには次のようにします。

{% tabs local %}
{% tab 入力 %}
{% raw %}
```liquid
{{custom_attribute.${date_attribute} | date: '%s' }}
```
{% endraw %}
{% endtab %}
{% tab 出力 %}
{% raw %}
```liquid
1433351621
```
{% endraw %}
{% endtab %}
{% endtabs %}