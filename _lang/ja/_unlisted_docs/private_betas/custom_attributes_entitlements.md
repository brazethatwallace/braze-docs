---
article_title: カスタム属性
permalink: "/custom_attributes_entitlements/"
hidden: true
---

# [![Braze Learningコース]({% image_buster /assets/unlisted_docs/img/logos/bl_icon3.png %})](https://learning.braze.com/custom-events-and-attributes){: style="float:right;width:120px;border:0;" class="noimgborder"}カスタム属性 {#braze-learning-course-image_buster-assetsunlisted_docsimglogosbl_icon3png-httpslearningbrazecomcustom-events-and-attributes-stylefloatrightwidth120pxborder0-classnoimgbordercustom-attributes}

> このページでは、ユーザー固有の特性を集めたカスタム属性について説明します。カスタム属性は、ユーザーに関する属性や、アプリケーション内の低価値アクションに関する情報を保存するのに最適です。

Brazeに保存されたカスタム属性は、オーディエンスセグメントの構築やLiquidを使用したメッセージのパーソナライズに使用できます。カスタム属性には時系列情報が保存されないため、カスタムイベントのようにグラフを取得することはできません。

## エンタイトルメント {#entitlements}

エンタイトルメントは、カスタム属性の容量を決定します。これは、定義するさまざまな属性名の数を追跡するものです。ワークスペースごとに最大1,000個のカスタム属性を設定できます。容量を増やす必要がある場合は、Brazeアカウントマネージャーに連絡して詳細をご確認ください。

ワークスペースがカスタム属性の上限数に近づくと、ダッシュボードおよびメールで通知が届き、状況を把握できるようになっています。

容量の上限に達した後も、既存のカスタム属性は引き続き受信できます。ただし、新しいカスタム属性を作成することはできません。まだ存在しないカスタム属性に対して受信されたデータは処理されません。

## カスタム属性の管理 {#managing-custom-attributes}

ダッシュボードでカスタム属性を作成・管理するには、**[データ設定]** > **[カスタム属性]** に移動します。

![ブール型の4つのカスタム属性。]({% image_buster /assets/unlisted_docs/img/custom_attributes_entitlements/export_custom_attributes.png %})

**[最終更新日]** 列には、カスタム属性が最後に編集された日時（ブロックリストへの追加やアクティブへの変更など）が表示されます。

{% alert important %}
メッセージのターゲティングを正しく行うために、カスタム属性のデータ型が実際のカスタム属性と一致していることを確認してください。
{% endalert %}

このページから、既存のカスタム属性を表示、管理、作成、またはブロックリストに追加できます。カスタム属性の横にあるメニューを選択すると、以下のアクションが表示されます。

### ブロックリストへの追加 {#blocklisting}

カスタム属性は、アクションメニューで個別にブロックリストに追加することも、最大100個の属性を選択して一括でブロックリストに追加することもできます。カスタム属性をブロックすると、その属性に関するデータは収集されなくなり、既存のデータは再アクティブ化しない限り利用できなくなります。また、ブロックリストに追加された属性はフィルターやグラフに表示されません。さらに、その属性がBrazeダッシュボードの他の領域でフィルターやトリガーによって参照されている場合は、それを参照しているすべてのフィルターやトリガーのインスタンスが削除・アーカイブされることを説明する警告モーダルが表示されます。

### 個人を特定できる情報（PII）としてのマーク {#marking-as-personally-identifiable-information-pii}

管理者は、このページからカスタム属性を作成し、PIIとしてマークすることもできます。これらの属性は、管理者および「PIIとしてマークされたカスタム属性を表示」権限を持つダッシュボードユーザーにのみ表示されます。

### 説明の追加 {#adding-descriptions}

`Manage Events, Attributes, Purchases` の[ユーザー権限]({{site.baseurl}}/user_guide/administer/global/user_management/permissions)を持っている場合、カスタム属性の作成後に説明を追加できます。カスタム属性を編集し、チームへのメモなど任意の内容を入力してください。

### タグの追加 {#adding-tags}

「Manage Events, Attributes, Purchases」の[ユーザー権限]({{site.baseurl}}/user_guide/administer/global/user_management/permissions)を持っている場合、カスタム属性の作成後にタグを追加できます。追加したタグは、属性リストのフィルタリングに使用できます。

### カスタム属性の削除 {#removing-custom-attributes}

ユーザープロファイルからカスタム属性を削除するには、2つの方法があります。

* [ユーザー更新ステップ]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update#removing-custom-attributes)で、削除するカスタム属性名を選択します。
* [`/users/track` エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track)へのAPIリクエストで `null` 値を設定します。

### 使用状況レポートの表示 {#viewing-usage-reports}

使用状況レポートには、特定のカスタム属性を使用しているすべてのキャンバス、キャンペーン、セグメントが一覧表示されます。このリストにはLiquidの使用は含まれません。

対象のカスタム属性の横にあるチェックボックスを選択し、**[使用状況レポートを表示]** を選択すると、一度に最大100件の使用状況レポートを表示できます。

### データのエクスポート {#exporting-data}

カスタム属性のリストをCSVファイルとしてエクスポートするには、ページ上部の **[すべてエクスポート]** を選択します。CSVファイルが生成され、ダウンロードリンクがメールで送信されます。

## カスタム属性の設定 {#setting-custom-attributes}

以下は、カスタム属性の設定に使用される各プラットフォームのメソッドの一覧です。

{% details プラットフォーム別のドキュメントを展開 %}

- [Android and FireOS]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=android)
- [iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=swift)
- [Web]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=web)
- [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/analytics#logging-custom-attributes)
- [Unity]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=unity)
- [Xamarin]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics#setting-custom-attributes)
- [Roku]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes)

{% enddetails %}

## カスタム属性のストレージ {#custom-attribute-storage}

**ユーザープロファイル**に保存されるすべてのデータ（カスタム属性データを含む）は、各プロファイルが[アクティブ]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival#active-users)である限り、無期限に保持されます。

## カスタム属性のデータ型 {#custom-attribute-data-types}

カスタム属性は非常に柔軟なツールであり、優れたターゲティングを実現します。

以下のデータ型をカスタム属性として保存できます。

- [ブーリアン](#booleans)
- [数値](#numbers)
- [文字列](#strings)
- [配列](#arrays)
- [日時](#time)
- [オブジェクト]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support)
- [オブジェクト配列]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects)

### ブーリアン（真/偽） {#booleans}

ブーリアン属性は、購読ステータスなど、ユーザーに関するシンプルなバイナリデータを保存するのに便利です。変数が明示的にtrueまたはfalseに設定されているユーザーだけでなく、その属性のレコードがまだないユーザーも検索できます。

| セグメンテーションオプション | ドロップダウンフィルター | 入力オプション | 例 |
| ---------------------| --------------- | ------------- | -------- |
| ブーリアン値がtrue、false、trueまたは未設定、falseまたは未設定の**いずれかであるか**を確認する | **IS** | **TRUE**、**FALSE**、**TRUE OR NOT SET**、または **FALSE OR NOT SET** | このフィルターが`coffee_drinker`を指定している場合、ユーザーは以下の状況でこのフィルターに一致します: <br> {::nomarkdown}<ul><li>フィルターが<code>true</code>で、ユーザーが<code>coffee_drinker</code>の値を持っている場合</li><li>フィルターが<code>false</code>で、ユーザーが<code>coffee_drinker</code>の値を持っていない場合</li><li>フィルターが<code>true or not set</code>で、ユーザーが<code>coffee_drinker</code>の値を持っているか、値がない場合</li><li>フィルターが<code>false or not set</code>で、ユーザーが<code>coffee_drinker</code>の値もいかなる値も持っていない場合</li></ul>{:/} |
| ブーリアン値がユーザーのプロファイルに**存在し**、nullでないかを確認する | **IS NOT BLANK** | **N/A** | このフィルターが`coffee_drinker`を指定しており、ユーザーが属性`coffee_drinker`の値を持っている場合、ユーザーはこのフィルターに一致します。 |
| ブーリアン値がユーザーのプロファイルに**存在しない**か、nullであるかを確認する | **IS BLANK** | **N/A** | このフィルターが`coffee_drinker`を指定しており、ユーザーが属性`coffee_drinker`を持っていないか、`coffee_drinker`の値がnullの場合、ユーザーはこのフィルターに一致します。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### 数値 {#numbers}

数値属性には[整数](https://en.wikipedia.org/wiki/Integer)と[浮動小数点数](https://en.wikipedia.org/wiki/Floating-point_arithmetic)が含まれ、幅広いユースケースがあります。インクリメント型の数値カスタム属性は、データ上限にカウントされることなく、特定のアクションやイベントが発生した回数を保存するのに便利です。標準的な数値にはさまざまな用途があります。例えば、以下の記録に使用できます。

- 靴のサイズ
- ウエストのサイズ
- ユーザーが特定の製品機能やカテゴリーを閲覧した回数

{% alert tip %}
支出金額はこの方法で記録するべきではありません。代わりに[購入メソッド](#purchase-revenue-tracking)を使用して記録してください。
{% endalert %}

| セグメンテーションオプション | ドロップダウンフィルター | 入力オプション | 例 |
| ---------------------| --------------- | ------------- | -------- |
| 数値属性が**数値**と**正確に一致するか**を確認する | **EXACTLY** | **NUMBER** | このフィルターが`10`を指定しており、ユーザープロファイルに値`10`がある場合、ユーザーはこのフィルターに一致します。 |
| 数値属性が**数値**と**等しくないか**を確認する | **DOES NOT EQUAL** | **NUMBER** | このフィルターが`10`を指定しており、ユーザープロファイルに値`10`がない場合、ユーザーはこのフィルターに一致します。 |
| 数値属性が**数値**より**大きいか**を確認する | **MORE THAN** | **NUMBER** | このフィルターが`10`を指定しており、ユーザープロファイルに`10`より大きい値がある場合、ユーザーはこのフィルターに一致します。 |
| 数値属性が**数値**より**小さいか**を確認する | **LESS THAN** | **NUMBER** | このフィルターが`10`を指定しており、ユーザープロファイルに`10`より小さい値がある場合、ユーザーはこのフィルターに一致します。 |
| 数値属性がユーザーのプロファイルに**存在し**、nullでないかを確認する | **IS NOT BLANK** | **N/A** | ユーザープロファイルに指定された数値属性が値に関係なく含まれている場合、ユーザーはこのフィルターに一致します。 |
| 数値属性がユーザーのプロファイルに**存在しない**か、nullであるかを確認する | **IS BLANK** | **N/A** | ユーザープロファイルに指定された数値属性が含まれていないか、属性の値がnullの場合、ユーザーはこのフィルターに一致します。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### 数値属性の詳細 {#number-attribute-details}

- 「正確に0」と「未満」のフィルターには、NULLフィールドを持つユーザーが含まれます
  - カスタム属性に値を持たないユーザーを除外するには、**is not blank**フィルターを含める必要があります。

### 文字列（英数字） {#strings}

文字列属性は、お気に入りのブランド、電話番号、アプリケーション内での最後の検索文字列など、ユーザー入力を保存するのに便利です。文字列属性は最大255文字まで設定できます。

単語の間、前、または後にスペースを含む値を入力した場合、Brazeも同じスペースをチェックすることに注意してください。

| セグメンテーションオプション | ドロップダウンフィルター | 入力オプション | 例 |
| ---------------------| --------------- | ------------- | -------- |
| 文字列属性が入力された文字列と**正確に一致するか**を確認する | **EQUALS** | **STRING**<br>大文字・小文字を区別 | このフィルターが`book`を指定しており、ユーザープロファイルの`last_item_purchased`の文字列属性に`book`が含まれている場合、ユーザーはこのフィルターに一致します。 |
| 文字列属性が入力された文字列**または**正規表現と**部分的に一致するか**を確認する | **MATCHES REGEX** | **STRING** **または** **REGULAR EXPRESSION** <br>大文字・小文字を区別しない; 最大32,764文字 |
| 文字列属性が入力された文字列**または**正規表現と**部分的に一致しないか**を確認する | **DOES NOT MATCH REGEX** * | **STRING** **または** **REGULAR EXPRESSION**<br>大文字・小文字を区別しない; 最大32,764文字 |
| 文字列属性が入力された文字列と**一致しないか**を確認する | **DOES NOT EQUAL** | **STRING**<br>大文字・小文字を区別しない | このフィルターが`book`を指定しており、ユーザープロファイルの`last_item_purchased`の文字列属性に`book`が含まれていない場合、ユーザーはこのフィルターに一致します。|
| 文字列属性がユーザーのプロファイルに**存在し**、空の文字列でないかを確認する | **IS NOT BLANK** | **N/A** | このフィルターが`favorite_genre`を指定しており、ユーザープロファイルに属性`favorite_genre`がある場合、属性値に関係なくユーザーはこのフィルターに一致します。例えば、ユーザーは`sci-fi`、`romance`、またはその他の値を持つことができます。|
| 文字列属性がユーザーのプロファイルに**存在しないか**を確認する | **BLANK** | **N/A** | このフィルターが`favorite_genre`を指定しており、ユーザープロファイルに属性`favorite_genre`がない場合、ユーザーはこのフィルターに一致します。|
| 文字列が入力された文字列の**いずれかと正確に一致するか**を確認する | **IS ANY OF** | **STRING**<br>大文字・小文字を区別; 複数の文字列が許可（最大256） | このフィルターが`book`、`bookmark`、`reading light`を指定しており、ユーザープロファイルにそれらの文字列の少なくとも1つがある場合、ユーザーはこのフィルターに一致します。 |
| 文字列属性が入力された文字列の**いずれとも正確に一致しないか**を確認する | **IS NONE OF** | **STRING**<br>大文字・小文字を区別; 複数の文字列が許可（最大256） | このフィルターが`book`、`bookmark`、`reading light`を指定しており、ユーザープロファイルにそれらの文字列のいずれも含まれていない場合、ユーザーはこのフィルターに一致します。|
| 文字列属性が入力された文字列の**いずれかを部分的に含むか**を確認する | **CONTAINS ANY OF** | **STRING**<br>大文字・小文字を区別; 複数の文字列が許可（最大256） | このフィルターが`gold`を指定しており、ユーザープロファイルの文字列に`gold`が含まれている場合（`gold_tier`や`former_gold_tier`など）、ユーザーはこのフィルターに一致します。 |
| 文字列属性が入力された文字列の**いずれも部分的に含まないか**を確認する | **DOESN'T CONTAIN ANY OF** | **STRING**<br>大文字・小文字を区別; 複数の文字列が許可（最大256） | このフィルターが`gold`を指定しており、ユーザープロファイルの文字列に`gold`が含まれていない場合、ユーザーはこのフィルターに一致します。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% alert note %}
「12-1-2021」や「12/1/2021」のような日付文字列はdatetimeオブジェクトに変換され、[日時属性]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes#time)として扱われます。
{% endalert %}

{% alert important %}
**DOES NOT MATCH REGEX**フィルターを使用してセグメンテーションを行う場合、そのユーザープロファイルに値が割り当てられたカスタム属性がすでに存在している必要があります。Brazeでは、カスタム属性が空白かどうかを確認する「OR」ロジックを使用して、ユーザーが適切にターゲティングされるようにすることを推奨しています。
{% endalert %}

### 配列 {#arrays}

配列属性は、ユーザーに関する関連情報のリストを保存するのに適しています。例えば、ユーザーが視聴した最新100件のコンテンツを配列に保存することで、特定の興味に基づくセグメンテーションが可能になります。

デフォルトでは、属性の配列の最大長は25に設定されており、個別の配列に対して最大100まで増やすことができます。例えば、「視聴した映画」のような属性を送信しており、100に設定されている場合、ユーザーが101番目の映画を視聴すると、最初の映画が配列から削除され、最新の映画が追加されます。

この最大値を増やしたい場合は、カスタマーサクセスマネージャーにご連絡ください。ダッシュボード管理者は、**設定の管理**ページの**カスタム属性**タブから、個別の配列の最大長を100以上に増やすことができます。

単語の間、前、または後にスペースを含む値を入力した場合、Brazeも同じスペースをチェックすることに注意してください。

{% alert note %}
最大長を増やすオプションは、属性がデータ型を自動検出するように設定されている場合は利用できません。データ型は配列に設定する必要があります。
{% endalert %}

| セグメンテーションオプション | ドロップダウンフィルター | 入力オプション | 例 |
| ---------------------| --------------- | ------------- | -------- |
| 配列属性に入力された値と**正確に一致する値が含まれるか**を確認する | **INCLUDES VALUE** | **STRING** | このフィルターが`sci-fi`を指定しており、ユーザープロファイルに値`sci-fi`がある場合、ユーザーはこのフィルターに一致します。|
| 配列属性に入力された値と**正確に一致する値が含まれないか**を確認する | **DOESN'T INCLUDE VALUE** | **STRING** | このフィルターが`sci-fi`を指定しており、ユーザープロファイルに値`sci-fi`がない場合、ユーザーはこのフィルターに一致します。|
| 配列属性に入力された値**または**正規表現と**部分的に一致する値が含まれるか**を確認する | **MATCHES REGEX** | **STRING** **または** **REGULAR EXPRESSION**<br>最大32,764文字 | |
| 配列属性に**何らかの値があるか**、または空でないかを確認する | **HAS A VALUE** | **N/A** | このフィルターが`favorite_genres`を指定しており、ユーザープロファイルに何らかの値を持つ`favorite_genres`が含まれている場合、ユーザーはこのフィルターに一致します。 |
| 配列属性が**空であるか**、存在しないかを確認する | **IS EMPTY** | **N/A** | このフィルターが`favorite_genres`を指定しており、ユーザープロファイルに`favorite_genres`が含まれていないか、`favorite_genres`が含まれているが値がない場合、ユーザーはこのフィルターに一致します。|
| 配列属性に入力された値の**いずれかと正確に一致する値が含まれるか**を確認する | **INCLUDES ANY OF** | **STRING**<br>大文字・小文字を区別; 複数の値が許可（最大256） | このフィルターが`sci-fi, fantasy, romance`を指定しており、ユーザープロファイルに`sci-fi`、`fantasy`、`romance`のいずれかの組み合わせがある場合（1つだけ、例えば`sci-fi`のみでも一致）。ユーザーは`sci-fi`、`fantasy`、`romance`のいずれかも持っていれば、`horror`やその他の値を持つこともできます。|
| 配列属性に入力された値の**いずれとも正確に一致する値が含まれないか**を確認する | **INCLUDES NONE OF** | **STRING**<br>大文字・小文字を区別; 複数の値が許可（最大256） | このフィルターが`sci-fi, fantasy, romance`を指定しており、ユーザープロファイルに`sci-fi`、`fantasy`、`romance`のいずれの組み合わせも持っていない場合、ユーザーはこのフィルターに一致します。ユーザーは`sci-fi`、`fantasy`、`romance`のいずれも持っていなければ、`horror`やその他の値を持つことができます。|
| 配列属性に入力された値の**いずれかを部分的に含む値があるか**を確認する | **VALUES CONTAIN ANY OF** | **STRING**<br>大文字・小文字を区別; 複数の値が許可（最大256） | このフィルターが`gold`を指定しており、ユーザープロファイルの配列に少なくとも1つの文字列に`gold`が含まれている場合、ユーザーはこのフィルターに一致します。これには`gold_tier`、`former_gold_tier`などの文字列値が含まれます。|
| 配列属性に入力された値の**いずれも部分的に含む値がないか**を確認する | **VALUES DON'T CONTAIN ANY OF** | **STRING**<br>大文字・小文字を区別; 複数の値が許可（最大256） | このフィルターが`gold`を指定しており、ユーザープロファイルの配列のいずれの文字列にも`gold`が含まれていない場合、ユーザーはこのフィルターに一致します。つまり、`gold_tier`や`former_gold_tier`のような文字列値を持つユーザーはこのフィルターに一致しません。|
| 配列属性に入力された値の**すべてが含まれるか**を確認する | **IS ALL OF** | **STRING**<br>大文字・小文字を区別; 複数の値が許可（最大256） | このフィルターが`sci-fi, fantasy, romance`を指定しており、ユーザープロファイルにそれらすべての値がある場合、ユーザーはこのフィルターに一致します。ユーザーは`horror`やその他の値も持っていてもこのフィルターに一致します。|
| 配列属性に入力された値の**すべてが含まれていないか**を確認する | **ISN'T ALL OF** | **STRING**<br>大文字・小文字を区別; 複数の値が許可（最大256） | このフィルターが`sci-fi, fantasy, romance`を指定しており、ユーザープロファイルにそれらすべての値がない場合、ユーザーはこのフィルターに一致します。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% alert tip %}
正規表現（regex）の使い方について詳しくは、以下のリソースをご参照ください:
- [Perl互換正規表現（PCRE）](https://www.regextester.com/pregsyntax.html)
- [Brazeでの正規表現]({{site.baseurl}}/user_guide/audience/segments/regex)
- [正規表現デバッガーとテスター](https://www.regex101.com/)
- [正規表現チュートリアル](https://www.medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285)
{% endalert %}

### 日時 {#time}

日時属性は、特定のアクションが最後に実行された日時を保存するのに便利です。これにより、コンテンツに特化したリエンゲージメントメッセージングをユーザーに提供できます。

相対日付を使用する日時フィルター（例: 1日以上前、2日未満前）は、1日を24時間として計算します。これらのフィルターを使用して実行するキャンペーンには、24時間単位のすべてのユーザーが含まれます。例えば、`last used app more than 1 day ago`は、キャンペーンが実行される正確な時刻から「24時間以上前にアプリを最後に使用した」すべてのユーザーを対象とします。より長い日付範囲で設定されたキャンペーンにも同じことが当てはまります。つまり、有効化から5日間は過去120時間を意味します。

例えば、将来の24時間から48時間の間に日時属性を持つユーザーをターゲットにするセグメントを作成するには、`in more than 1 day in the future`と`in less than 2 days in the future`のフィルターを適用します。

{% alert warning %}
カスタムイベントまたは購入イベントが最後に発生した日付は自動的に記録されるため、カスタム日時属性を使用して再度記録する必要はありません。
{% endalert %}

| セグメンテーションオプション | ドロップダウンフィルター | 入力オプション | 例 |
| ---------------------| --------------- | ------------- | -------- |
| 日時属性が**選択した日付より前**であるかを確認する | **BEFORE** | **CALENDAR DATE SELECTOR** | このフィルターが`2024-01-31`を指定しており、ユーザープロファイルに`2024-1-31`より前の日付がある場合、ユーザーはこのフィルターに一致します。 |
| 日時属性が**選択した日付より後**であるかを確認する | **AFTER** | **CALENDAR DATE SELECTOR** | このフィルターが`2024-01-31`を指定しており、ユーザープロファイルに`2024-1-31`より後の日付がある場合、ユーザーはこのフィルターに一致します。 |
| 日時属性が**X日以上前**であるかを確認する | **MORE THAN** | **NUMBER OF DAYS AGO** | このフィルターが`7`を指定しており、ユーザープロファイルに7日以上前の日付がある場合、ユーザーはこのフィルターに一致します。 |
| 日時属性が**X日未満前**であるかを確認する | **LESS THAN** | **NUMBER OF DAYS AGO** | このフィルターが`7`を指定しており、ユーザープロファイルに7日未満前の日付がある場合、ユーザーはこのフィルターに一致します。|
| 日時属性が**将来のX日以上先**であるかを確認する | **IN MORE THAN** | **NUMBER OF DAYS IN FUTURE** | このフィルターが`7`を指定しており、ユーザープロファイルに将来7日以上先の日付がある場合、ユーザーはこのフィルターに一致します。|
| 日時属性が**将来のX日未満先**であるかを確認する | **IN LESS THAN** | **NUMBER OF DAYS IN FUTURE** | このフィルターが`7`を指定しており、ユーザープロファイルに将来7日未満先の日付がある場合、ユーザーはこのフィルターに一致します。|
| 日時属性がユーザーのプロファイルに**存在し**、nullでないかを確認する | **IS NOT BLANK** | **N/A** | このフィルターがユーザープロファイルに存在する日時属性を指定している場合、ユーザーはこのフィルターに一致します。|
| 日時属性がユーザーのプロファイルに**存在しない**か、nullであるかを確認する | **IS BLANK** | **N/A** | このフィルターがユーザープロファイルに存在しない日時属性を指定している場合、ユーザーはこのフィルターに一致します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### 日時属性の詳細 {#time-attribute-details}

{% multi_lang_include data_activation/day_of_recurring_event_filter.md %}

### オブジェクト {#objects}

階層化カスタム属性を使用して、カスタム属性のデータ型としてオブジェクトを送信できます。詳細については、[階層化カスタム属性]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support)をご参照ください。

### オブジェクト配列 {#arrays-of-objects}

オブジェクト配列を使用して、関連する属性をグループ化します。詳細については、[オブジェクト配列]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects)の記事をご参照ください。

### 演算子の統合 {#consolidated-operators}

属性フィルター、カスタム属性フィルター、階層化カスタム属性フィルターで使用できる演算子のリストを統合しました。これらの演算子を使用する既存のフィルターがある場合、新しい演算子を使用するように自動的に更新されます。

| データ型 | 旧演算子 | 新演算子 | 値 |
| --- | --- | --- | --- |
| 文字列 | equals | is any of | 1つ以上の値 |
| 文字列 | does not equal | is none of | 1つ以上の値 |
| 配列 | includes value | includes any of | 1つ以上の値 |
| 配列 | doesn't include value | includes none of | 1つ以上の値 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## 購入と収益のトラッキング {#purchase-revenue-tracking}

購入メソッドを使用してアプリ内購入を記録すると、各ユーザープロファイルのLTV（LTV）が確立されます。このデータは、収益ページで時系列として表示できます。

| セグメンテーションオプション | ドロップダウンフィルター | 入力オプション | 例 |
| ---------------------| --------------- | ------------- | -------- |
| 合計支出金額が**数値**より**大きい**かを確認する | **GREATER THAN** | **NUMBER** | このフィルターが`500`を指定し、ユーザープロファイルの値が`500`より大きい場合、ユーザーはこのフィルターに一致します。 |
| 合計支出金額が**数値**より**小さい**かを確認する | **LESS THAN** | **NUMBER** | このフィルターが`500`を指定し、ユーザープロファイルの値が`500`より小さい場合、ユーザーはこのフィルターに一致します。|
| 合計支出金額が**数値**と**正確に一致する**かを確認する | **EXACTLY** | **NUMBER** | このフィルターが`500`を指定し、ユーザープロファイルの値が`500`の場合、ユーザーはこのフィルターに一致します。 |
| 最後の購入が**X日以降**に行われたかを確認する | **AFTER** | **TIME** | このフィルターが`2024/31/1`を指定し、ユーザーの最後の購入が`2024/31/1`以降の場合、ユーザーはこのフィルターに一致します。|
| 最後の購入が**X日以前**に行われたかを確認する | **BEFORE** | **TIME** | このフィルターが`2024/31/1`を指定し、ユーザーの最後の購入が`2024/31/1`以前の場合、ユーザーはこのフィルターに一致します。|
| 最後の購入が**X日以上前**に行われたかを確認する | **MORE THAN** | **TIME** | このフィルターが`7`を指定し、ユーザーの最後の購入が今日から7日以上前の場合、ユーザーはこのフィルターに一致します。|
| 最後の購入が**X日未満前**に行われたかを確認する | **LESS THAN** | **TIME** | このフィルターが`7`を指定し、ユーザーの最後の購入が今日から7日未満前の場合、ユーザーはこのフィルターに一致します。|
| 購入が**X回（最大50回）以上**行われたかを確認する | **MORE THAN** | 過去**Y日間（Y = 1,3,7,14,21,30）** | このフィルターが`7`回と`21`日を指定し、ユーザーが過去21日間に7回以上購入した場合、ユーザーはこのフィルターに一致します。|
| 購入が**X回（最大50回）未満**行われたかを確認する | **LESS THAN** | 過去**Y日間（Y = 1,3,7,14,21,30）** | このフィルターが`7`回と`21`日を指定し、ユーザーが過去21日間に7回未満購入した場合、ユーザーはこのフィルターに一致します。|
| 購入が**正確にX回（最大50回）**行われたかを確認する | **EXACTLY** | 過去**Y日間（Y = 1,3,7,14,21,30）** | このフィルターが`7`回と`21`日を指定し、ユーザーが過去21日間に正確に7回購入した場合、ユーザーはこのフィルターに一致します。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% alert tip %}
特定の購入が発生した回数でセグメンテーションしたい場合は、その購入を[インクリメント型カスタム属性]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_custom_attributes#incrementingdecrementing-custom-attributes)として個別に記録する必要があります。
{% endalert %}

カスタム属性のデータタイプは変更できますが、[データタイプの変更]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#changing-custom-attribute-or-event-data-type)の影響に注意してください。