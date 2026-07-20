---
nav_title: SQL変数
article_title: クエリビルダーのSQL変数
page_order: 2
page_type: reference
description: "クエリビルダーで変数を使用する方法を学び、クエリを再利用してコード内にデータをハードコーディングすることを避けましょう。"
tool: Reports
---

# クエリビルダーのSQL変数 {#query-builder-sql-variables}

> クエリビルダーでSQL変数を使用する方法を学び、クエリを再利用してコード内にデータをハードコーディングすることを避けましょう。

## SQL変数を使用する理由 {#why-use-sql-variables}

SQL変数を使用するメリットには以下があります。

- レポート作成時にキャンペーン IDを貼り付ける代わりに、キャンペーン変数を作成してリストから選択することで時間を節約できます。
- 変数を追加して値を入れ替えることで、将来的にわずかに異なるユースケース（異なるカスタムイベントなど）でレポートを再利用できます。
- 各レポートに必要な編集量を減らすことで、SQLの編集時のユーザーエラーを軽減できます。SQLに慣れているチームメンバーがレポートを作成し、技術的な知識が少ないチームメンバーがそのレポートを使用できます。

## 変数の使用 {#using-variables}

### ステップ 1: 変数を追加する {#step-1-add-a-variable}

クエリに変数を追加するには、以下の構文を使用します。

{% raw %}
```sql
{{variable_type.${custom_label}}}
```
{% endraw %}

以下を置き換えてください。

| プレースホルダー | 説明 |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| `variable_type`   | 使用したい定義済みの変数タイプ（`campaign`や`catalog_fields`など）。完全なリストについては、[サポートされている変数タイプ](#variable-types)を参照してください。 |
| `custom_label` | クエリビルダーの**変数**タブで変数を識別するために使用されるラベル。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ステップ 1: 変数を追加する" }

以下の例では、ある月の初日から最終日までのユーザー総数をキャンペーンに対してクエリしています。各変数には次のステップで値が割り当てられます。

{% raw %}
```sql
SELECT COUNT(*) AS total_users
FROM USERS_CAMPAIGNS_REVENUE_SHARED
WHERE campaign_id = '{{campaign.${Campaign}}}'
  AND TIME > '{{start_date.${Month First Day}}}'
  AND TIME < '{{end_date.${Month Last Day}}}';
```
{% endraw %}

### ステップ 2: 値を割り当てる {#step-2-assign-a-value}

デフォルトでは、クエリビルダーに**変数**タブは表示されません。クエリに最初の変数を追加した後にのみ表示されます。そこで値を割り当てることができます。選択できる具体的な値は、その変数の[タイプ](#variable-types)によって異なります。

以下の例では、「Summer Feature Launch」キャンペーンが値として割り当てられ、2025年6月の初日と最終日も設定されています。

![クエリビルダーの「変数」タブに上記の例が表示されている画面。]({% image_buster /assets/img/query_builder_example.png %})

## 汎用変数タイプ {#variable-types}

### 数値 {#number}

`number`は他の非文字列変数と組み合わせて使用できます。`5.5`のような小数を含む、正または負の任意の数値を受け付けます。

{% tabs %}
{% tab 使用方法 %}
{% raw %}
```sql
some_number_column < {{number.${custom_label}}}
```
{% endraw %}
{% endtab %}
{% endtabs %}

### 文字列 {#string}

レポート実行間で繰り返される文字列値を変更するために使用します。SQL内で値を複数回ハードコーディングすることを避けるためにこの変数を使用してください。

{% tabs %}
{% tab 使用方法 %}
{% raw %}
```sql
'{{string.${add a string here.}}}'
```
{% endraw %}
{% endtab %}
{% endtabs %}

### リスト {#list}

オプションのリストから選択するために使用します。

{% tabs local %}
{% tab 1つ選択 %}
{% subtabs %}
{% subtab 使用方法 %}
{% raw %}
```sql
{{options.${metrics} | is_radio_button: 'true' | options: '[{"label": "test", "value": "test_value"}, {"label": "test2", "value": "test_value2"}]'}}
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab 複数選択 %}
{% subtabs %}
{% subtab 使用方法 %}
{% raw %}
```sql
{{options.${metrics} | is_multi_select: 'true' | options: '[{"label": "test", "value": "test_value"}, {"label": "test2", "value": "test_value2"}]'}}
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

#### ラジオボタン {#radio-button}

**変数**タブでセレクトドロップダウンの代わりにラジオボタンとしてオプションを表示するために使用します。単独では使用できません&#8212;[リスト](#list)と組み合わせて使用する必要があります。

{% tabs %}
{% tab 使用方法 %}
```sql
is_radio_button: 'true'
```
{% endtab %}
{% endtabs %}

![Brazeでレンダリングされたラジオボタンの例。]({% image_buster /assets/img_archive/sql_variables_campaigns.png %}){: style="max-width:50%;"}

#### 複数選択 {#multi-select}

セレクトドロップダウンで単一選択または複数選択を許可するかどうかを設定します。単独では使用できません&#8212;[リスト](#list)と組み合わせて使用する必要があります。

{% tabs %}
{% tab 使用方法 %}
```sql
is_multi_select: 'true'
```
{% endtab %}
{% endtabs %}

![Brazeでレンダリングされた複数選択リストの例。]({% image_buster /assets/img_archive/sql_variables_productname.png %}){: style="max-width:50%;"}

#### オプション {#options}

ラベルと値の形式で選択可能なオプションのリストを提供するために使用します。ラベルは表示されるもので、値はオプションが選択されたときに変数が置き換えられるものです。単独では使用できません&#8212;[リスト](#list)と組み合わせて使用する必要があります。

{% tabs %}
{% tab 使用方法 %}
```sql
options: '[{"label": "test", "value": "test_value"}, {"label": "test2", "value": "test_value2"}]'
```
{% endtab %}
{% endtabs %}

## Braze固有の変数タイプ {#braze-specific-variable-types}

### 日付範囲 {#date-range}

日付を選択するためのカレンダーを表示するために使用します。`start_date`と`end_date`をUTCの指定された日付のUnixタイムスタンプ（秒単位）に置き換えてください（例: `1696517353`）。オプションで、`start_date`または`end_date`のみを設定して、カレンダーに単一の日付のみを表示することもできます。`start_date`と`end_date`のラベルが一致しない場合、日付範囲ではなく2つの別々の日付として扱われます。

{% tabs %}
{% tab 使用方法 %}
{% raw %}
```
time > {{start_date.${custom_label}}} AND time < {{end_date.${custom_label}}}
```
{% endraw %}
{% endtab %}
{% endtabs %}

日付範囲は以下のオプションのいずれかに設定できます。`start_date`と`end_date`の両方が使用され、同じラベルを共有している場合、すべてのオプションが表示されます。それ以外の場合、1つのみが使用されている場合は、指定されたオプションのみが表示されます。

| オプション | 説明 | 必要な値 |
| --- | --- | --- |
| 相対 | 過去X日間を指定します | `start_date`が必要 |
| 開始日 | 開始日を指定します | `start_date`が必要 |
| 終了日 | 終了日を指定します | `end_date`が必要 |
| 日付範囲 | 開始日と終了日の両方を指定します | `start_date`と`end_date`の両方が必要 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="日付範囲" }

Liquidは指定された日付範囲内にカレンダーを表示するために使用されます。

![Brazeでレンダリングされたカレンダーの例。]({% image_buster /assets/img_archive/query_builder_time_range.png %}){: style="max-width:50%;"}

### キャンペーン

{% tabs local %}
{% tab 1つのキャンペーン %}
1つのキャンペーンを選択するために使用します。キャンバスと同じラベルを共有すると、**変数**タブ内にキャンバスまたはキャンペーンのいずれかを選択するためのラジオボタンが表示されます。

{% subtabs %}
{% subtab 使用方法 %}
{% raw %}
```sql
campaign_id = '{{campaign.${custom_label}}}'
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab 複数のキャンペーン %}
キャンペーンを複数選択するために使用します。キャンバスと同じラベルを共有すると、**変数**タブ内にキャンバスまたはキャンペーンのいずれかを選択するためのラジオボタンが表示されます。

- **置換値:** キャンペーンのBSON ID

{% subtabs %}
{% subtab 使用方法 %}
{% raw %}
```sql
campaign_id IN ({{campaigns.${custom_label}}})
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab キャンペーンバリアント %}
選択されたキャンペーンに属するキャンペーンバリアントを選択するために使用します。キャンペーンまたはキャンペーン変数と併用する必要があります。

- **置換値:** キャンペーンバリアントのAPI ID。`api-id1, api-id2`のようにカンマ区切りの文字列です。

{% subtabs %}
{% subtab 使用方法 %}
{% raw %}
```sql
message_variation_api_id IN ({{campaign_variants.${custom_label}}})
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert important %}
すべてのキャンペーンおよびキャンバス変数は、単一グループ内で状態を同期するために同じ識別子を使用する必要があります。
{% endalert %}

### キャンバス {#canvases}

{% tabs local %}
{% tab 1つのキャンバス %}
1つのキャンバスを選択するために使用します。キャンペーンと同じラベルを共有すると、**変数**タブ内にキャンバスまたはキャンペーンのいずれかを選択するためのラジオボタンが表示されます。

- **置換値:** キャンバスのBSON ID

{% subtabs %}
{% subtab 使用方法 %}
{% raw %}
```sql
canvas_id = '{{canvas.${custom_label}}}'
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab 複数のキャンバス %}
複数のキャンバスを選択するために使用します。キャンペーンと同じラベルを共有すると、**変数**タブ内にキャンバスまたはキャンペーンのいずれかを選択するためのラジオボタンが表示されます。

- **置換値:** キャンバスのBSON ID

{% subtabs %}
{% subtab 使用方法 %}
{% raw %}
```sql
canvas_id IN ({{canvases.${custom_label}}})
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab キャンバスバリアント %}
選択されたキャンバスに属するキャンバスバリアントを選択するために使用します。キャンバスまたはキャンバス変数と併用する必要があります。1つ以上のキャンバスバリアントAPI IDを、`api-id1, api-id2`のようにカンマ区切りの文字列として設定します。

{% subtabs %}
{% subtab 使用方法 %}
{% raw %}
```sql
canvas_variation_api_id IN ({{canvas_variants.${custom_label}}})
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab 1つのキャンバスステップ %}
選択されたキャンバスに属するキャンバスステップを選択するために使用します。キャンバス変数と併用する必要があります。

{% subtabs %}
{% subtab 使用方法 %}
{% raw %}
```sql
canvas_step_api_id = '{{canvas_step.${custom_label}}}'
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab 複数のキャンバスステップ %}
選択されたキャンバスに属するキャンバスステップを選択するために使用します。キャンバスまたはキャンバス変数と併用する必要があります。

{% subtabs %}
{% subtab 使用方法 %}
{% raw %}
```sql
canvas_step_api_id IN ({{canvas_steps.${custom_label}}})
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert important %}
すべてのキャンペーンおよびキャンバス変数は、単一グループ内で状態を同期するために同じ識別子を使用する必要があります。
{% endalert %}

### 製品 {#products}

`products`はBrazeダッシュボードから1つ以上の製品を選択するために使用します。

{% tabs %}
{% tab 使用方法 %}
{% raw %}
```sql
({{products.${custom_label}}})
```
{% endraw %}
{% endtab %}

{% tab 例 %}
{% raw %}
```sql
SELECT product_name
FROM FULL_GAME_AND_DLC
WHERE product_id IN ({{products.${Games with DLC}}});
```
{% endraw %}
{% endtab %}
{% endtabs %}

### カスタムイベント {#custom-events}

リストから1つ以上のカスタムイベントまたはカスタムイベントプロパティを選択します。

{% tabs local %}
{% tab イベント %}
`custom_events`はBrazeダッシュボードから1つ以上のカスタムイベントを選択するために使用します。

{% subtabs %}
{% subtab 使用方法 %}
{% raw %}
```sql
'{{custom_events.${custom_label}}}'
```
{% endraw %}
{% endsubtab %}

{% subtab 例 %}
{% raw %}
```sql
SELECT event_name
FROM CUSTOM_EVENTS_TABLE
WHERE event_name IN ({{custom_events.${Purchased Game}}});
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab プロパティ %}
`custom_event_properties`は現在選択されているカスタムイベントから1つ以上のプロパティを選択するために使用します。`custom_events`変数が設定されている必要があります。

{% subtabs %}
{% subtab 使用方法 %}
{% raw %}
```sql
name = '{{custom_event_properties.${property names)}}}'
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### ワークスペース {#workspace}

`workspace`はBrazeダッシュボードから単一のワークスペースを選択するために使用します。

{% tabs %}
{% tab 使用方法 %}
{% raw %}
```sql
workspace_id = '{{workspace.${app_group_id}}}'
```
{% endraw %}
{% endtab %}
{% endtabs %}

### カタログ {#catalogs}

リストから1つ以上のカタログまたはカタログフィールドを選択します。

{% tabs local %}
{% tab カタログ %}
`catalogs`はBrazeダッシュボードから1つ以上のカタログを選択するために使用します。

{% subtabs %}
{% subtab 使用方法 %}
{% raw %}
```sql
catalog_id = '{{catalogs.${catalog}}}'
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab カタログフィールド %}
`catalog_fields`は現在選択されているカタログから1つ以上のフィールドを設定するために使用します。`catalogs`変数が設定されている必要があります。

{% subtabs %}
{% subtab 使用方法 %}
{% raw %}
```sql
field_name = '{{catalog_fields.${custom_label}}}'
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### セグメント

[分析トラッキング]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking)が有効になっているセグメントを選択するために使用します。セグメントの分析IDに設定します。これは、このカラムが利用可能なテーブルの`user_segment_membership_ids`カラムに格納されているIDに対応します。

{% tabs %}
{% tab 使用方法 %}
{% raw %}
```sql
{{segments.${analytics_segments}}}
```
{% endraw %}
{% endtab %}
{% endtabs %}

### タグ {#tags}

キャンペーンおよびキャンバスのタグを選択するために使用します。選択されたタグに関連付けられた、シングルクォートでカンマ区切りのBSON IDを持つキャンペーンおよびキャンバスに設定されます。

{% tabs %}
{% tab 使用方法 %}
{% raw %}
```sql
{{tags.${some tags}}}
```
{% endraw %}
{% endtab %}
{% endtabs %}

## 変数メタデータ {#variable-metadata}

メタデータを変数に付加して動作を変更できます。変数ラベルの後にパイプ（ &#124; ）文字を使用してメタデータを追加します。メタデータの順序は関係なく、任意の数を追加できます。また、すべてのタイプのメタデータは任意の変数に使用できますが、特定の変数に固有の特殊メタデータは除きます（その場合は該当箇所に記載されます）。すべてのメタデータの使用はオプションであり、変数のデフォルト動作を変更するために使用されます。

{% tabs %}
{% tab 使用方法 %}
{% raw %}
```sql
{{string.${my var}| is_required: 'false' | description: 'My optional string var'}}
```
{% endraw %}
{% endtab %}
{% endtabs %}

### ブール値 {#boolean}

変数の値が入力されているかどうかを判定するために使用します。これは、変数の値が入力されていない場合に条件をショートサーキットしたいオプション変数に便利です。他の変数の値に応じて`true`または`false`に設定できます。

{% tabs %}
{% tab 使用方法 %}
{% raw %}
```sql
{{string.${type_name_has_no_value} | visible: 'false'}} or {{string.${type_name_has_value} | visible: 'false'}}
```
{% endraw %}
{% endtab %}
{% endtabs %}

`type`と`name`は参照される変数を指します。例えば、以下のオプション変数をショートサーキットする場合: {% raw %}`{{campaigns.${messaging}}`{% endraw %}:

{% raw %}
```sql
{{string.${campaigns_messaging_has_no_value}  | visible: 'false'}} OR campaign_id IN ({{campaigns.${messaging} | is_required: 'false'}})
```
{% endraw %}

### 表示 {#visible}

変数を表示するかどうかを設定します。すべての変数はデフォルトで**変数**タブに表示され、そこで値を入力できます。

他の変数に依存する値を持つ特殊な変数がいくつかあります（例: 別の変数に値があるかどうかなど）。これらの特殊変数は非表示としてマークされ、**変数**タブには表示されません。

{% tabs %}
{% tab 使用方法 %}
```sql
visible: 'false'
```
{% endtab %}
{% endtabs %}

### 必須 {#required}

変数がデフォルトで必須かどうかを設定します。変数の値が空の場合、通常は不正なクエリになります。

{% tabs %}
{% tab 使用方法 %}
```sql
required: 'false'
```
{% endtab %}
{% endtabs %}

### 順序 {#order}

**変数**タブ内の変数の位置を選択するために使用します。

{% tabs %}
{% tab 使用方法 %}
```sql
order: '1'
```
{% endtab %}
{% endtabs %}

### 引用符の付加 {#include-quotes}

{% tabs local %}
{% tab シングルクォート %}
変数の値をシングルクォートで囲むために使用します。

{% subtabs %}
{% subtab 使用方法 %}
```sql
include_quotes: 'true'
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab ダブルクォート %}
変数の値をダブルクォートで囲むために使用します。

{% subtabs %}
{% subtab 使用方法 %}
```sql
include_double_quotes: 'true'
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### プレースホルダー {#placeholder}

変数の入力フィールドに表示されるプレースホルダーテキストを指定するために使用します。

{% tabs %}
{% tab 使用方法 %}
```sql
placeholder: 'enter some value'
```
{% endtab %}
{% endtabs %}

### 説明 {#description}

変数の入力フィールドの下に表示される説明テキストを指定するために使用します。

{% tabs %}
{% tab 使用方法 %}
```sql
description: 'some description'
```
{% endtab %}
{% endtabs %}

### デフォルト値 {#default-value}

値が指定されていない場合の変数のデフォルト値を指定するために使用します。

{% tabs %}
{% tab 使用方法 %}
```sql
default_value: '5'
```
{% endtab %}
{% endtabs %}

### ラベルを非表示にする {#hide-label}

変数のラベルを非表示にするために使用します。

{% tabs %}
{% tab 使用方法 %}
```sql
hide_label: 'true'
```
{% endtab %}
{% endtabs %}