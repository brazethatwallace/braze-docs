---
nav_title: データタイプ
article_title: データタイプ
page_order: 1
page_type: reference
description: "Brazeのカスタム属性、イベントプロパティ、カタログでサポートされているデータタイプのリファレンスです。"
toc_headers: h2
---

# データタイプ {#data-types}

> このページでは、カスタム属性、イベントプロパティ、カタログでサポートされているデータタイプをまとめています。各カスタムデータタイプは、サポートされるデータタイプと制約がそれぞれ若干異なります。

## 定義 {#definitions}

以下の表を使用して、ユーザープロファイル属性、イベントデータ、またはカタログアイテムに使用できるデータタイプを確認してください。各タイプの使用方法と制約については、後続のセクションを参照してください。

<table role="presentation" class="definitions-table reset-td-br-1 reset-td-br-2 reset-td-br-3 reset-td-br-4 reset-td-br-5">
  <thead>
    <tr>
      <th>データタイプ</th>
      <th>定義</th>
      <th>カスタム属性</th>
      <th>イベントプロパティ</th>
      <th>カタログ</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>ブール値</td>
      <td>値は <code>true</code> または <code>false</code></td>
      <td>✅ サポート</td>
      <td>✅ サポート</td>
      <td>✅ サポート</td>
    </tr>
    <tr>
      <td>数値</td>
      <td>整数または小数</td>
      <td>✅ サポート</td>
      <td>✅ サポート</td>
      <td>✅ サポート</td>
    </tr>
    <tr>
      <td>文字列</td>
      <td>テキスト。255文字以下</td>
      <td>✅ サポート</td>
      <td>✅ サポート</td>
      <td>✅ サポート</td>
    </tr>
    <tr>
      <td>時間</td>
      <td>標準形式（<a href="https://en.wikipedia.org/wiki/ISO_8601">ISO 8601</a>）の日付と時刻</td>
      <td>✅ サポート</td>
      <td>✅ サポート</td>
      <td>✅ サポート</td>
    </tr>
    <tr>
      <td>配列</td>
      <td>値の順序付きリスト</td>
      <td>✅ サポート</td>
      <td>✅ サポート</td>
      <td>✅ サポート</td>
    </tr>
    <tr>
      <td>オブジェクト</td>
      <td>名前付きフィールドを持つ構造化データ（ネストされたキーと値のペア）</td>
      <td>✅ サポート</td>
      <td>✅ サポート</td>
      <td>✅ サポート</td>
    </tr>
    <tr>
      <td>オブジェクトの配列</td>
      <td>オブジェクトのリスト</td>
      <td>✅ サポート</td>
      <td>❌ 非サポート</td>
      <td>❌ 非サポート</td>
    </tr>
  </tbody>
</table>

### 重要な考慮事項 {#important-considerations}

- **配列:** カスタム属性とイベントプロパティにはサイズ制限があります。イベントプロパティの配列内では日時はサポートされていません。カタログは文字列配列のみをサポートし、最大100要素です。
- **オブジェクト:** Brazeでは、カスタム属性の場合は「階層化カスタム属性」、イベントプロパティの場合は「ネストされたオブジェクト」、カタログの場合は「JSONオブジェクト」として表示されます。
- **時間:** イベントプロパティでは、このタイプは「Datetime」と表示されます。

## カスタム属性のデータタイプ {#custom-attribute-data-types}

カスタム属性は、[定義](#definitions)の表に記載されているデータタイプをサポートしています。以下では、サポートされている各データタイプの使用方法とセグメンテーションについて説明します。

{% tabs %}
{% tab ブール値 %}

カスタム属性は、アクションメニューから個別にブロックリストに追加できます。また、最大100個の属性を選択して一括でブロックリストに追加することもできます。カスタム属性をブロックすると、その属性に関するデータは収集されなくなり、既存のデータは再有効化しない限り利用できなくなります。また、ブロックリストに追加された属性はフィルターやグラフに表示されません。さらに、その属性がBrazeダッシュボードの他の領域でフィルターやトリガーによって現在参照されている場合、警告モーダルが表示され、それを参照しているフィルターやトリガーのすべてのインスタンスが削除およびアーカイブされることが説明されます。

### 個人を特定できる情報（PII）としてマークする {#marking-as-personally-identifiable-information-pii}

管理者は、このページからカスタム属性を作成し、PIIとしてマークすることもできます。これらの属性は、管理者および「View カスタム属性 Marked as PII」権限を持つダッシュボードユーザーにのみ表示されます。

### 説明の追加 {#adding-descriptions}

`Manage Events, Attributes, Purchases`[ユーザー権限]({{site.baseurl}}/user_guide/administer/global/user_management/permissions)を持っている場合、カスタム属性の作成後に説明を追加できます。カスタム属性を編集し、チームへのメモなど任意の内容を入力してください。

### タグの追加 {#adding-tags}

「Manage Events, Attributes, Purchases」[ユーザー権限]({{site.baseurl}}/user_guide/administer/global/user_management/permissions)を持っている場合、カスタム属性の作成後にタグを追加できます。その後、タグを使用して属性のリストをフィルタリングできます。

### カスタム属性の削除 {#removing-custom-attributes}

ユーザープロファイルからカスタム属性を削除するには、2つの方法があります。

- [ユーザーの更新ステップ]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update)で、削除するカスタム属性名を選択します。
- APIリクエストで[`/users/track`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track)に`null`値を設定します。

#### `null`値の設定 {#setting-the-null-value}

{% alert important %}
属性を`null`に設定することと`""`（空文字列）に設定することは同じではありません。
{% endalert %}

- `null`は属性をユーザープロファイルから完全に削除します。プロファイルに表示されず、**IS NOT BLANK**フィルターにもマッチしません。
- `""`は属性を空文字列の値に設定します。属性は空文字列の値としてプロファイルに表示されますが、**IS NOT BLANK**フィルターにはマッチしません（空白として扱われます）。

さらに、`""`は文字列型の属性にのみ有効です。属性のデータタイプがダッシュボードで文字列以外の型（ブール値、数値、時間など）に設定されている場合、`""`を送信しても値はクリアされません。代わりに`null`を使用してください。

### データのエクスポート {#exporting-data}

カスタム属性のリストをCSVファイルとしてエクスポートするには、ページ上部の**Export all**を選択します。システムがCSVファイルを生成し、ダウンロードリンクをメールで送信します。

## 使用状況レポートの表示 {#viewing-usage-reports}

使用状況レポートには、特定のカスタム属性を使用しているすべてのキャンバス、キャンペーン、セグメントが一覧表示されます。このリストにはLiquidの使用は含まれません。

対象のカスタム属性のチェックボックスを選択してから**View usage report**を選択することで、一度に最大100件の使用状況レポートを表示できます。

### 値タブ {#values-tab}

使用状況レポートを表示する際に、**Values**タブを選択すると、約250,000人のユーザーのサンプルに基づいて、選択したカスタム属性の上位の値を確認できます。結果はユーザーのサブセットからサンプリングされるため、サンプルにはすべての既存の値が含まれていない場合があります。つまり、**Values**タブはトラブルシューティングや、すべてのユーザーのデータを組み込む必要があるユースケースには使用しないでください。

![選択されたカスタム属性の使用状況レポート。「Values」タブが開かれており、「US」や「PR」などの国属性の値を示す円グラフが表示されています。]({% image_buster /assets/img/usage_report_values.png %}){: style="max-width:80%;"}

## カスタム属性の設定 {#setting-custom-attributes}

以下に、カスタム属性の設定に使用される各プラットフォームのメソッドを示します。

{% details プラットフォーム別のドキュメントを展開 %}

- [AndroidおよびFireOS]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes?sdktab=android)
- [iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes?sdktab=swift)
- [Web]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes?sdktab=web)
- [React Native]({{site.baseurl}}/developer_guide/analytics)
- [Unity]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes?sdktab=unity)
- [.NET MAUI（旧Xamarin）]({{site.baseurl}}/developer_guide/analytics?sdktab=xamarin)
- [Roku]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes)

{% enddetails %}

## カスタム属性のストレージ {#custom-attribute-storage}

カスタム属性データを含む**ユーザープロファイル**に保存されたすべてのデータは、各プロファイルが[アクティブ]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival#active-users)である限り、無期限に保持されます。

## カスタム属性のデータタイプ

カスタム属性は非常に柔軟なツールであり、優れたターゲティングを可能にします。

以下のデータタイプをカスタム属性として保存できます。

- [ブール値](#booleans)
- [数値](#numbers)
- [文字列](#strings)
- [配列](#arrays)
- [時間](#time)
- [オブジェクト]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support)
- [オブジェクトの配列]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects)

### ブール値（true/false） {#booleans}

ブール属性は、購読ステータスなど、ユーザーに関するシンプルなバイナリデータを保存するのに便利です。変数が明示的にtrueまたはfalseに設定されているユーザーに加え、その属性がまだ記録されていないユーザーも検索できます。

**ブール値**属性では、以下のセグメンテーションオプションが利用可能です。

| セグメンテーションオプション | ドロップダウンフィルター | 入力オプション | 例 |
| ---------------------| --------------- | ------------- | -------- |
| ブール値がtrue、false、trueまたは未設定、falseまたは未設定の**いずれかであるか**を確認する | **IS** | **TRUE**、**FALSE**、**TRUE OR NOT SET**、または**FALSE OR NOT SET** | このフィルターが`coffee_drinker`を指定する場合、ユーザーは以下の状況でこのフィルターにマッチします: <br> {::nomarkdown}<ul><li>このフィルターが<code>true</code>でユーザーが<code>coffee_drinker</code>の値を持つ場合</li><li>このフィルターが<code>false</code>でユーザーが<code>coffee_drinker</code>の値を持たない場合</li><li>このフィルターが<code>true or not set</code>でユーザーが<code>coffee_drinker</code>の値を持つか値がない場合</li><li>このフィルターが<code>false or not set</code>でユーザーが<code>coffee_drinker</code>を持たないか値がない場合</li></ul>{:/} |
| ブール値がユーザーのプロファイルに**存在し**、nullでないかを確認する | **IS NOT BLANK** | **N/A** | このフィルターが`coffee_drinker`を指定し、ユーザーが`coffee_drinker`属性の値を持つ場合、ユーザーはこのフィルターにマッチします。 |
| ブール値がユーザーのプロファイルに**存在しない**か、nullであるかを確認する | **IS BLANK** | **N/A** | このフィルターが`coffee_drinker`を指定し、ユーザーが`coffee_drinker`属性を持たないか、`coffee_drinker`の値がnullである場合、ユーザーはこのフィルターにマッチします。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Booleans (true/false) #booleans" }

{% endtab %}
{% tab 数値 %}

{% alert tip %}
支出金額はこの方法で記録するべきではありません。代わりに[購入イベント]({{site.baseurl}}/user_guide/data/activation/events/purchase_events)で記録してください。
{% endalert %}

**数値**属性では、以下のセグメンテーションオプションが利用可能です。

| セグメンテーションオプション | ドロップダウンフィルター | 入力オプション | 例 |
| ---------------------| --------------- | ------------- | -------- |
| 数値属性が**数値と正確に一致する**かを確認する | **EXACTLY** | **NUMBER** | このフィルターが`10`を指定し、ユーザープロファイルの値が`10`の場合、ユーザーはこのフィルターにマッチします。 |
| 数値属性が**数値と等しくない**かを確認する | **DOES NOT EQUAL** | **NUMBER** | このフィルターが`10`を指定し、ユーザープロファイルの値が`10`でない場合、ユーザーはこのフィルターにマッチします。 |
| 数値属性が**数値より大きい**かを確認する | **MORE THAN** | **NUMBER** | このフィルターが`10`を指定し、ユーザープロファイルの値が`10`より大きい場合、ユーザーはこのフィルターにマッチします。 |
| 数値属性が**数値より小さい**かを確認する | **LESS THAN** | **NUMBER** | このフィルターが`10`を指定し、ユーザープロファイルの値が`10`より小さい場合、ユーザーはこのフィルターにマッチします。 |
| 数値属性がユーザーのプロファイルに**存在し**、nullでないかを確認する | **IS NOT BLANK** | **N/A** | ユーザープロファイルに指定された数値属性が含まれている場合、値に関係なく、ユーザーはこのフィルターにマッチします。 |
| 数値属性がユーザーのプロファイルに**存在しない**か、nullであるかを確認する | **IS BLANK** | **N/A** | ユーザープロファイルに指定された数値属性が含まれていないか、属性の値がnullの場合、ユーザーはこのフィルターにマッチします。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Booleans (true/false) #booleans" }

#### 数値属性の詳細 {#number-attribute-details}

- 「正確に0」および「未満」フィルターにはNULLフィールドを持つユーザーが含まれます
  - カスタム属性の値を持たないユーザーを除外するには、**is not blank**フィルターを含める必要があります。

{% endtab %}
{% tab 文字列 %}

文字列属性の最大長は255文字です。単語の間、前、または後にスペースを含む値を入力した場合、Brazeはそのスペースもチェックします。

**文字列**属性では、以下のセグメンテーションオプションが利用可能です。

| セグメンテーションオプション | ドロップダウンフィルター | 入力オプション | 例 |
| ---------------------| --------------- | ------------- | -------- |
| 文字列属性が入力された文字列**または**正規表現に**部分一致する**かを確認する | **MATCHES REGEX** | **STRING****または****REGULAR EXPRESSION** <br>大文字小文字を区別しない。最大32,764文字 |
| 文字列属性が入力された文字列**または**正規表現に**部分一致しない**かを確認する | **DOES NOT MATCH REGEX** * | **STRING****または****REGULAR EXPRESSION**<br>大文字小文字を区別しない。最大32,764文字 |
| 文字列属性がユーザーのプロファイルに**存在し**、空文字列でないかを確認する | **IS NOT BLANK** | **N/A** | このフィルターが`favorite_genre`を指定し、ユーザープロファイルに`favorite_genre`属性がある場合、属性値に関係なくユーザーはこのフィルターにマッチします。例えば、ユーザーは`sci-fi`、`romance`、または他の値を持つことができます。|
| 文字列属性がユーザーのプロファイルに**存在しない**かを確認する | **BLANK** | **N/A** | このフィルターが`favorite_genre`を指定し、ユーザープロファイルに`favorite_genre`属性がない場合、ユーザーはこのフィルターにマッチします。|
| 文字列が入力された文字列の**いずれかに完全一致する**かを確認する | **IS ANY OF** | **STRING**<br>大文字小文字を区別する。複数の文字列を指定可能（最大256） | このフィルターが`book`、`bookmark`、`reading light`を指定し、ユーザープロファイルにそれらの文字列のうち少なくとも1つがある場合、ユーザーはこのフィルターにマッチします。 |
| 文字列属性が入力された文字列の**いずれにも完全一致しない**かを確認する | **IS NONE OF** |**STRING**<br>大文字小文字を区別する。複数の文字列を指定可能（最大256） | このフィルターが`book`、`bookmark`、`reading light`を指定し、ユーザープロファイルにそれらの文字列のいずれも含まれていない場合、ユーザーはこのフィルターにマッチします。|
| 文字列属性が入力された文字列の**いずれかに部分一致する**かを確認する | **CONTAINS ANY OF** | **STRING**<br>大文字小文字を区別する。複数の文字列を指定可能（最大256） | このフィルターが`gold`を指定し、ユーザープロファイルの文字列に`gold`が含まれている場合（例えば`gold_tier`や`former_gold_tier`）、ユーザーはこのフィルターにマッチします。 |
| 文字列属性が入力された文字列の**いずれにも部分一致しない**かを確認する | **DOESN'T CONTAIN ANY OF** | **STRING**<br>大文字小文字を区別する。複数の文字列を指定可能（最大256） | このフィルターが`gold`を指定し、ユーザープロファイルのいずれの文字列にも`gold`が含まれていない場合、ユーザーはこのフィルターにマッチします。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Number attribute details" }

{% multi_lang_include alerts/note_alerts.md alert='Custom Attributes time attribute' %}

{% alert important %}
**DOES NOT MATCH REGEX**フィルターを使用してセグメンテーションする場合、そのユーザープロファイルに値が割り当てられたカスタム属性がすでに存在している必要があります。Brazeでは、カスタム属性が空白であるかどうかを確認するために「OR」ロジックを使用し、ユーザーが適切にターゲティングされるようにすることを推奨しています。
{% endalert %}

{% endtab %}
{% tab 配列 %}

### 配列 {#arrays}

配列の最大サイズは100&nbsp;KBです。属性のデフォルトの長さは最大500項目です（例えば、「視聴済み映画」のような属性を500に設定した場合、ユーザーが501本目の映画を視聴すると、最初の映画が削除され、最新の映画が追加されます）。単語の間、前、または後にスペースを含む値を入力した場合、Brazeはそのスペースもチェックします。

配列型のカスタム属性は[CSVインポート]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import)ではインポートできません。配列の値をアップロードするには、[`/users/track`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track)または[Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion)を使用してください。

{% alert note %}
属性がデータタイプを自動検出するように設定されている場合、最大長を増やすオプションは利用できません。データタイプを配列に設定する必要があります。
{% endalert %}

#### トラブルシューティング：配列カスタム属性がユーザープロファイルに値を表示しない {#troubleshooting-array-custom-attribute-shows-no-value-on-a-user-profile}

配列カスタム属性がユーザープロファイルに表示されているが値が表示されない場合は、属性の**最大長**がダッシュボードで`0`に設定されていないか確認してください。

1. **データ設定** > **カスタム属性**に移動します。
2. **配列**でリストをフィルターします。
3. 属性を見つけて**最大長**を確認します。
4. **最大長**が`0`の場合、`0`より大きい値に更新します。

**最大長**を`0`に設定すると、ユーザープロファイルに値が表示されなくなります。

SDKに焦点を当てた配列の動作例については、[分析の概要]({{site.baseurl}}/developer_guide/analytics)を参照してください。

**配列**属性では、以下のセグメンテーションオプションが利用可能です。

| セグメンテーションオプション | ドロップダウンフィルター | 入力オプション | 例 |
| ---------------------| --------------- | ------------- | -------- |
| 配列属性が入力された値に**完全一致する値を含む**かを確認する | **INCLUDES VALUE** | **STRING** | このフィルターが`sci-fi`を指定し、ユーザープロファイルに`sci-fi`の値がある場合、ユーザーはこのフィルターにマッチします。|
| 配列属性が入力された値に**完全一致する値を含まない**かを確認する | **DOESN'T INCLUDE VALUE** | **STRING** | このフィルターが`sci-fi`を指定し、ユーザープロファイルに`sci-fi`の値がない場合、ユーザーはこのフィルターにマッチします。|
| 配列属性が入力された値**または**正規表現に**部分一致する値を含む**かを確認する | **MATCHES REGEX** | **STRING****または****REGULAR EXPRESSION**<br>最大32,764文字 | |
| 配列属性が**何らかの値を持つ**か、空でないかを確認する | **HAS A VALUE** | **N/A** | このフィルターが`favorite_genres`を指定し、ユーザープロファイルに何らかの値を持つ`favorite_genres`が含まれている場合、ユーザーはこのフィルターにマッチします。 |
| 配列属性が**空である**か、存在しないかを確認する | **IS EMPTY** | **N/A** | このフィルターが`favorite_genres`を指定し、ユーザープロファイルに`favorite_genres`が含まれていないか、`favorite_genres`があるが値がない場合、ユーザーはこのフィルターにマッチします。|
| 配列属性が入力された値の**いずれかに完全一致する値を含む**かを確認する | **INCLUDES ANY OF** | **STRING**<br>大文字小文字を区別する。複数の値を指定可能（最大256） | このフィルターが`sci-fi, fantasy, romance`を指定し、ユーザープロファイルに`sci-fi`、`fantasy`、`romance`の任意の組み合わせがある場合（そのうちの1つだけ、例えば`sci-fi`のみでも可）。ユーザーは`sci-fi`、`fantasy`、`romance`のいずれかを持っていれば、`horror`や他の値も持つことができます。|
| 配列属性が入力された値の**いずれにも完全一致する値を含まない**かを確認する | **INCLUDES NONE OF** | **STRING**<br>大文字小文字を区別する。複数の値を指定可能（最大256） | このフィルターが`sci-fi, fantasy, romance`を指定し、ユーザープロファイルに`sci-fi`、`fantasy`、`romance`の任意の組み合わせがない場合、ユーザーはこのフィルターにマッチします。ユーザーは`sci-fi`、`fantasy`、`romance`のいずれも持っていなければ、`horror`や他の値を持つことができます。|
| 配列属性が入力された値の**いずれかに部分一致する値を含む**かを確認する | **VALUES CONTAIN ANY OF** | **STRING**<br>大文字小文字を区別する。複数の値を指定可能（最大256） | このフィルターが`gold`を指定し、ユーザープロファイルの配列内の少なくとも1つの文字列に`gold`が含まれている場合、ユーザーはこのフィルターにマッチします。これには`gold_tier`、`former_gold_tier`などの文字列値が含まれます。|
| 配列属性が入力された値の**いずれにも部分一致する値を含まない**かを確認する | **VALUES DON'T CONTAIN ANY OF** | **STRING**<br>大文字小文字を区別する。複数の値を指定可能（最大256） | このフィルターが`gold`を指定し、ユーザープロファイルの配列内のいずれの文字列にも`gold`が含まれていない場合、ユーザーはこのフィルターにマッチします。つまり、`gold_tier`や`former_gold_tier`のような文字列値を持つユーザーはこのフィルターにマッチしません。|
| 配列属性が入力された値の**すべてを含む**かを確認する | **IS ALL OF** | **STRING**<br>大文字小文字を区別する。複数の値を指定可能（最大256） | このフィルターが`sci-fi, fantasy, romance`を指定し、ユーザープロファイルにそれらのすべての値がある場合、ユーザーはこのフィルターにマッチします。ユーザーは`horror`や他の値も持つことができ、このフィルターにマッチします。|
| 配列属性が入力された値の**すべてを含んでいない**かを確認する | **ISN'T ALL OF** | **STRING**<br>大文字小文字を区別する。複数の値を指定可能（最大256） | このフィルターが`sci-fi, fantasy, romance`を指定し、ユーザープロファイルにそれらのすべての値がない場合、ユーザーはこのフィルターにマッチします。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Number attribute details" }

{% alert tip %}
正規表現（regex）の使い方について詳しくは、以下のリソースを参照してください:

- [Perl互換正規表現（PCRE）](https://www.regextester.com/pregsyntax.html)
- [Brazeでの正規表現]({{site.baseurl}}/user_guide/audience/segments/regex)
- [正規表現デバッガーとテスター](https://www.regex101.com/)
- [正規表現チュートリアル](https://www.medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285)
{% endalert %}

{% endtab %}
{% tab 時間 %}

時間属性は、特定のアクションが最後に実行された時間を保存するのに便利で、ユーザーにコンテンツ固有のリエンゲージメントメッセージを提供できます。

相対日付を使用した時間フィルター（例：1日以上前、2日未満前）は、1日を24時間として測定します。これらのフィルターを使用して実行するキャンペーンには、24時間単位のすべてのユーザーが含まれます。例えば、`last used app more than 1 day ago`は、キャンペーンが実行される正確な時刻から「24時間以上前にアプリを最後に使用した」すべてのユーザーをキャプチャします。より長い日付範囲が設定されたキャンペーンでも同様です。したがって、有効化から5日間は直前の120時間を意味します。

時間範囲内にある時間属性を持つユーザーをターゲットにするには、2つのオーディエンスフィルターを使用します。下限には`in more than`、上限には`in less than`を使用してください。1つのフィルターではその範囲の両側を表現できません。例えば、今後24時間以内（現在から1日後まで）の時間属性を持つユーザーをターゲットにするには、`in more than 0 days`と`in less than 1 day`を適用します。

{% alert warning %}
カスタムイベントまたは購入イベントが最後に発生した日付は自動的に記録されるため、カスタム時間属性を通じて再度記録する必要はありません。
{% endalert %}

**時間**属性では、以下のセグメンテーションオプションが利用可能です。

| セグメンテーションオプション | ドロップダウンフィルター | 入力オプション | 例 |
| ---------------------| --------------- | ------------- | -------- |
| 時間属性が**選択した日付より前**かを確認する | **BEFORE** | **カレンダー日付セレクター** | このフィルターが`2024-01-31`を指定し、ユーザープロファイルの日付が`2024-1-31`より前の場合、ユーザーはこのフィルターにマッチします。 |
| 時間属性が**選択した日付より後**かを確認する | **AFTER** | **カレンダー日付セレクター** | このフィルターが`2024-01-31`を指定し、ユーザープロファイルの日付が`2024-1-31`より後の場合、ユーザーはこのフィルターにマッチします。 |
| 時間属性が**X日以上前**かを確認する | **MORE THAN** | **日数前** | このフィルターが`7`を指定し、ユーザープロファイルの日付が7日以上前の場合、ユーザーはこのフィルターにマッチします。 |
| 時間属性が**X日未満前**かを確認する | **LESS THAN** | **日数前** | このフィルターが`7`を指定し、ユーザープロファイルの日付が7日未満前の場合、ユーザーはこのフィルターにマッチします。|
| 時間属性が**X日以上先**かを確認する | **IN MORE THAN** | **将来の日数** | このフィルターが`7`を指定し、ユーザープロファイルの日付が7日以上先の場合、ユーザーはこのフィルターにマッチします。|
| 時間属性が**X日未満先**かを確認する | **IN LESS THAN** | **将来の日数** | このフィルターが`7`を指定し、ユーザープロファイルの日付が7日未満先の場合、ユーザーはこのフィルターにマッチします。|
| 時間属性がユーザーのプロファイルに**存在し**、nullでないかを確認する | **IS NOT BLANK** | **N/A** | このフィルターがユーザープロファイル上にある時間属性を指定する場合、ユーザーはこのフィルターにマッチします。|
| 時間属性がユーザーのプロファイルに**存在しない**か、nullであるかを確認する | **IS BLANK** | **N/A** | このフィルターがユーザープロファイル上にない時間属性を指定する場合、ユーザーはこのフィルターにマッチします。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Number attribute details" }

{% alert note %}
**in less than**または**in more than**演算子を90日以上で使用する場合、セグメントを保存するときにBrazeは自動的に値を週に変換します。例えば、90日は13週に変換されます。
{% endalert %}

#### 時間属性の詳細 {#time-attribute-details}

{% multi_lang_include data_activation/day_of_recurring_event_filter.md %}

{% endtab %}
{% tab オブジェクト %}

階層化カスタム属性を使用して、カスタム属性のデータタイプとしてオブジェクトを送信できます。詳細については、[階層化カスタム属性]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support)を参照してください。

{% endtab %}
{% tab オブジェクトの配列 %}

オブジェクトの配列を使用して、関連する属性をグループ化します。詳細については、[オブジェクトの配列]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects)を参照してください。

{% endtab %}
{% endtabs %}

カスタム属性のデータタイプは変更できますが、その影響に注意する必要があります。詳細については、[カスタム属性またはイベントのデータタイプの変更](#changing-custom-attribute-or-event-data-type)を参照してください。

### 統合演算子 {#consolidated-operators}

属性フィルター、カスタム属性フィルター、および階層化カスタム属性フィルターで使用できる演算子のリストを統合しました。これらの演算子を使用する既存のフィルターがある場合、新しい演算子を使用するように自動的に更新されます。

| データタイプ | 旧演算子 | 新演算子 | 値 |
| --- | --- | --- | --- |
| 文字列 | equals | is any of | 1つ以上の値 |
| 文字列 | does not equal | is none of | 1つ以上の値 |
| 配列 | includes value | includes any of | 1つ以上の値 |
| 配列 | doesn't include value | includes none of | 1つ以上の値 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Consolidated operators #consolidated-operators" }

## イベントプロパティのデータタイプ {#event-property-data-types}

イベントをログに記録する際、追加情報（例えば、商品名や価格）をイベントプロパティとして添付できます。各プロパティには名前と値があります。イベントプロパティの値は、[定義](#definitions)の表に記載されているデータタイプをサポートしています（時間はイベントプロパティでは「Datetime」と表示されます）。

### 期待される形式 {#expected-format}

プロパティ値はオブジェクトとして送信されます。キーはプロパティ名、値はプロパティ値です。プロパティ名は空でない文字列で、255文字以下、先頭にドル記号（`$`）を含めないでください。

イベントプロパティ固有のルール:

- **時間（Datetime）:** [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)または`yyyy-MM-dd'T'HH:mm:ss:SSSZ`形式を使用します。配列内ではサポートされていません。
- **配列:** 配列内では日時はサポートされていません。
- **ネストされたオブジェクト:** [ネストされたオブジェクト]({{site.baseurl}}/user_guide/data/activation/events/custom_events/nested_objects)を参照してください。
- **ペイロード:** 配列またはオブジェクトの値を含むイベントプロパティオブジェクトは、最大102,400バイト（100&nbsp;KiB）です。

カスタムイベントプロパティのデータタイプは変更できますが、データ収集後の[データタイプの変更](#changing-custom-attribute-or-event-data-type)の影響に注意してください。

イベントプロパティの完全な動作、予約キー、トリガーやパーソナライゼーションでの使用方法については、[カスタムイベントプロパティ]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties)を参照してください。

## 購入イベントと収益 {#purchase-events-and-revenue}

購入および収益データは、[購入イベント]({{site.baseurl}}/user_guide/data/activation/events/purchase_events)または推奨eコマースイベントを通じて記録されます。

{% alert note %}
推奨イベントには、データタイプが設定された事前定義のスキーマがあります。詳細については、[eコマース推奨イベント]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events)を参照してください。
{% endalert %}

購入イベントをログに記録すると、各ユーザープロファイルのLTV or 生涯価値（LTV）が確立され、このデータは収益ページで時系列で表示できます。使用金額、最終購入日、時間枠内の購入回数などでセグメンテーションできます。

### 購入イベントプロパティのデータタイプ {#purchase-event-property-data-types}

購入イベントプロパティの値（購入の`properties`オブジェクト）は、[定義](#definitions)の表に記載されているデータタイプをサポートしており、[イベントプロパティ](#expected-format)と同じ構造および命名規則に従います。

{% include data_activation/purchase_event_property_data_types.md %}

購入オブジェクトの完全なスキーマと例については、[購入オブジェクト]({{site.baseurl}}/api/objects_filters/purchase_object)を参照してください。購入イベントのログ記録、セグメンテーションフィルター、および完全な詳細については、[購入イベント]({{site.baseurl}}/user_guide/data/activation/events/purchase_events)を参照してください。

## カスタム属性またはイベントのデータタイプの変更 {#changing-custom-attribute-or-event-data-type}

カスタム属性またはイベントのデータタイプを変更するには:

1. **データ設定**に移動し、**カスタム属性**または**カスタムイベント**を選択します。
2. リストから属性またはイベントを見つけ、<i class="fa fa-ellipsis-v" aria-hidden="true"></i> **その他のアクション**を選択します。
3. ドロップダウンから新しい**データタイプ**を選択します。
4. **保存**を選択します。

カスタム属性またはイベントのデータタイプを変更する場合（例えば、`time`を`string`に変更する場合）、以下の点を考慮してください。

- **フィルターは自動的に更新されません。** 変更された属性またはイベントを使用しているセグメント、キャンペーン、キャンバス、またはその他の場所は更新されません。データタイプを変更する前に、セグメントやフィルターでその属性を使用しているキャンペーンやキャンバスを停止し、それを参照しているフィルターから属性を削除してください。
- **既存のユーザーデータは遡及的に更新されません。** 変更前にユーザープロファイルに変更された属性があった場合、その値は古いデータタイプのままです。フィルターが新しいデータタイプを検索するため、変更された属性を含むセグメントからユーザーが外れる可能性があります。それらのユーザープロファイルを更新して（例えば、[`/users/track`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track)を使用して）、新しいタイプに一致させ、必要に応じてセグメントに再度入るようにしてください。
- **新しいデータは新しいタイプに一致する必要があります。** 変更された属性に対して以前のデータタイプを送信するAPIコールは受け付けられません。新しいデータタイプを送信してください。

{% alert important %}
自動検出によるカスタム属性データタイプの更新を防止する機能は、現在早期アクセス中です。参加をご希望の場合は、カスタマーサクセスマネージャーにお問い合わせください。
{% endalert %}

## カタログのデータタイプ {#catalog-data-types}

カタログは、[定義](#definitions)の表に記載されているタイプをサポートしています。以下の表は、各タイプ、作成または更新の方法、形式と例を示しています。

| データタイプ | 説明 | CSVアップロードで利用可能 | APIおよびCDIで利用可能 |
| --- | --- | --- | --- |
| 文字列 | 文字のシーケンス（例: 名前、説明、ID）。 | ✅ はい | ✅ はい |
| 数値 | 整数または浮動小数点の数値（例: 価格、数量、評価）。 | ✅ はい | ✅ はい |
| ブール値 | `true`または`false`の値。 | ✅ はい | ✅ はい |
| 時間 | [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)形式の日付と時刻、またはUnixタイムスタンプ（秒）。 | ✅ はい | ✅ はい |
| JSONオブジェクト（オブジェクト） | キーと値のペアを持つネストされたオブジェクト。プラットフォームに表示されますが、APIまたはCDIを通じてのみ作成または更新できます。 | ❌ いいえ | ✅ はい |
| 文字列配列（配列） | 文字列のリスト。プラットフォームに表示されますが、APIまたはCDIを通じてのみ作成または更新できます。最大100要素。 | ❌ いいえ | ✅ はい |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Catalog data types #catalog-data-types" }

### 形式と例 {#format-and-examples}

| データタイプ | 形式 | 例 |
| --- | --- | --- |
| 文字列 | テキスト | <code>"Hello World"</code> |
| 時間 | ISO 8601またはUnixタイムスタンプ（秒） | <code>"2024-03-15T14:30:00Z"</code> |
| ブール値 | <code>true</code>または<code>false</code> | <code>true</code> |
| 数値 | 整数または小数 | <code>42</code>または<code>19.99</code> |
| オブジェクト | JSONオブジェクト | <code>{"key": "value", "price": 10}</code> |
| 配列 | 文字列の配列 | <code>["red", "blue", "green"]</code> |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Format and examples" }

カタログの作成と更新については、[カタログの作成]({{site.baseurl}}/user_guide/data/activation/catalogs/create)を参照してください。