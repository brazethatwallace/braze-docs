---
nav_title: カタログを作成する
article_title: カタログを作成する
alias: "/catalogs/"
page_order: 1
description: "このリファレンス記事では、Liquidを通してBrazeのキャンペーンでユーザー以外のデータを参照するカタログを作成する方法について説明します。"
---

# カタログを作成する {#create-a-catalog}

> カタログを作成するには、ユーザー以外のデータのCSVファイルをBrazeにインポートします。これにより、その情報にアクセスしてメッセージを充実させることができます。カタログには、任意のタイプのデータを取り込むことができます。このデータは通常、eコマースビジネスの商品情報や、教育プロバイダーのコース情報など、会社のある種のメタデータです。

## ユースケース {#use-cases}

カタログの一般的なユースケースには以下が含まれます。

- 製品
- サービス
- 食品
- 今後のイベント
- 音楽
- パッケージ

この情報をインポートした後、Liquidを通じてカスタム属性やカスタムイベントプロパティにアクセスするのと同様の方法で、メッセージ内でアクセスできるようになります。

## サポートされているデータタイプ {#supported-data-types}

以下の表は、サポートされているカタログのデータタイプと、それぞれの作成・更新方法を示しています。

| データタイプ | 説明 | CSVアップロードで利用可能 | APIおよびCDIで利用可能 |
|--------------|-----------------------------------------------|:------------------------:|:-------------------------:|
| 文字列 | 文字のシーケンスです。 | ✅ はい | ✅ はい |
| 数値 | 整数または浮動小数点の数値です。 | ✅ はい | ✅ はい |
| ブール値 | `true` または `false` の値です。 | ✅ はい | ✅ はい |
| 時刻 | [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)形式でフォーマットされた文字列です。 | ✅ はい | ✅ はい |
| 位置情報 | `[longitude, latitude]` の座標配列です。緯度は-90から90の間、経度は-180から180の間である必要があります。例: `[-73.988103, 40.779109]`。 | ✅ はい | ✅ はい |
| JSONオブジェクト | キーと値のペアを持つネストされたオブジェクトです。プラットフォーム上で表示できますが、作成や更新はAPIまたはCDIを通じてのみ可能です。 | ⛔ いいえ | ✅ はい |
| 文字列配列 | 文字列のリストです。プラットフォーム上で表示できますが、作成や更新はAPIまたはCDIを通じてのみ可能です。最大100要素です。 | ⛔ いいえ | ✅ はい |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## カタログの作成 {#creating-a-catalog}

カタログを作成するには、**データ設定** > **カタログ**に移動し、**新規カタログを作成**を選択して、以下のオプションのいずれかを選択します。

{% tabs local %}
{% tab CSVをアップロード %}
### ステップ 1:CSVファイルを確認する {#step-1-review-your-csv-file}

CSVファイルをアップロードする前に、CSVファイルが以下の要件を満たしていることを確認してください。

| CSVの要件 | 詳細 |
|-----------------|---------|
| ヘッダー | CSVファイルの最初の列は `id` という名前にする必要があり、各行には一意の `id` 値が必要です。 |
| 列 | CSVファイルには最大1,000個のフィールド（列）を含めることができ、各列名は最大250文字です。 |
| ファイルサイズ | Freeプランの場合、企業全体のすべてのCSVファイルの合計サイズは500 MBに制限されています。Proプランの場合、単一のCSVファイルの最大ファイルサイズは2 GBです。 |
| フィールド値 | 各セル（フィールド値）には最大5,000文字を含めることができます。 |
| 有効な文字 | `id` 列とすべてのヘッダー値には、文字、数字、ハイフン、アンダースコアのみを使用できます。 |
| データ型 | CSVアップロードでサポートされているデータ型には、文字列、数値、ブール値、時刻、ジオロケーションがあります。APIおよびCDIでのみ利用可能なデータ型を含む全リストについては、[サポートされるデータ型](#supported-data-types)を参照してください。 |
| フォーマット | 一貫性を維持するため、すべてのテキストを小文字でフォーマットしてください。 |
| エンコーディング | CSVファイルはUTF-8エンコーディングで保存してアップロードしてください。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert note %}
CSVファイルにさらに容量が必要ですか？カタログのアップグレードの詳細については、Brazeアカウントマネージャーにお問い合わせください。
{% endalert %}

### ステップ 2:CSVをアップロードする {#step-2-upload-csv}

ファイルをアップロードゾーンにドラッグ＆ドロップするか、**CSVをアップロード**を選択してファイルを選択します。

![ファイルをアップロードゾーンにドラッグ＆ドロップするか、「CSVをアップロード」を選択してファイルを選択します。]({% image_buster /assets/img_archive/catalog_CSV_upload.png %}){: style="max-width:80%;"}

各列のデータ型を選択します。

{% alert note %}
このデータ型はカタログの設定後に編集できません。また、CSVアップロードでは `NULL` 値はサポートされておらず、文字列として扱われます。
{% endalert %}

![カタログ設定後にデータ型を編集することはできません。また、CSVアップロードではNULL値はサポートされず、文字列として扱われます。]({% image_buster /assets/img_archive/catalog_data_type.png %}){: style="max-width:80%;"}

カタログの名前と任意の説明を入力します。カタログの命名には以下の要件に留意してください。

  - 一意である必要があります
  - 最大250文字
  - 数字、文字、ハイフン、アンダースコアのみ使用可能

{% alert tip %}
[カタログ名にテンプレートを使用する](#template-catalog-names)こともでき、言語やキャンペーンなどの変数に基づいてカタログ名を動的に生成できます。
{% endalert %}

![「my_catalog」という名前のカタログ。]({% image_buster /assets/img_archive/in_browser_catalog.png %}){: style="max-width:80%;"}

**カタログを処理**を選択してカタログを作成します。

{% alert important %}
CSVファイルは、このセクションの前述の[ティア](#tiers)を超えている場合、拒否される可能性があります。
{% endalert %}

### チュートリアル：CSVファイルからカタログを作成する {#tutorial-creating-a-catalog-from-a-csv-file}

このチュートリアルでは、2つのゲーム、その価格、および画像リンクをリストしたカタログを使用します。

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;font-size: 14px; font-weight: bold; background-color: #f4f4f7; text-transform: lowercase; color: #212123; font-family: "Aribau Grotesk Bold", "Aribau Grotesk", "Aribau Grotesk Regular", Arial, Helvetica, sans-serif;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top;word-break:normal}
</style>
<table class="tg" aria-label="チュートリアル：CSVファイルからカタログを作成する">
<thead>
  <tr>
    <th class="tg-0pky">id</th>
    <th class="tg-0pky">title</th>
    <th class="tg-0pky">price</th>
    <th class="tg-0pky">image_link</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky">1234</td>
    <td class="tg-0pky">Tales</td>
    <td class="tg-0pky">7.49</td>
    <td class="tg-0pky">https://picsum.photos/200</td>
  </tr>
  <tr>
    <td class="tg-0pky">1235</td>
    <td class="tg-0pky">Regeneration</td>
    <td class="tg-0pky">22.49</td>
    <td class="tg-0pky">https://picsum.photos/200</td>
  </tr>
</tbody>
</table>

CSVファイルをアップロードしてカタログを作成します。`id`、`title`、`price`、`image_link` のデータ型はそれぞれ文字列、文字列、数値、文字列です。

{% alert note %}
このデータ型はカタログの設定後に編集できません。
{% endalert %}

![4つのカタログ列名：「id」、「title」、「price」、「image_link」。]({% image_buster /assets/img_archive/catalog_data_type.png %}){: style="max-width:85%;"}

次に、このカタログを「games_catalog」と名付けて、**カタログを処理**ボタンを選択します。Brazeはカタログの作成前にエラーがないか確認します。

![「games_catalog」という名前のカタログ。]({% image_buster /assets/img_archive/catalog_new_name.png %}){: style="max-width:85%;"}

カタログの作成後にこの名前を編集することはできません。カタログを削除して、同じカタログ名を使用して更新版を再アップロードできます。

カタログを作成したら、[キャンペーンでのカタログの参照]({{site.baseurl}}/user_guide/data/activation/catalogs/using_catalogs)を開始できます。

{% alert important %}
以前にアップロードしたCSVファイルは、アップロード日から30日間、**カタログ**ページからダウンロードできます。30日後、ファイルは完全に削除され、アクセスできなくなります。
{% endalert %}
{% endtab %}

{% tab ブラウザーで作成 %}
### 前提条件 {#prerequisites}

ブラウザーでカタログを編集または作成するには、ワークスペースに対して以下の[ユーザー権限]({{site.baseurl}}/user_guide/administer/global/user_management/permissions)が必要です。

- カタログの表示
- カタログの編集
- カタログのエクスポート
- カタログの削除

### ステップ 1:カタログの詳細を入力する {#step-1-enter-catalog-details}

カタログの名前と任意の説明を入力します。カタログの命名には以下の要件に留意してください。

- 一意である必要があります
- 最大250文字
- 数字、文字、ハイフン、アンダースコアのみ使用可能

{% alert tip %}
[カタログ名にテンプレートを使用する](#template-catalog-names)こともでき、言語やキャンペーンなどの変数に基づいてカタログ名を動的に生成できます。
{% endalert %}

![「my_catalog」という名前のカタログ。]({% image_buster /assets/img_archive/in_browser_catalog.png %}){: style="max-width:80%;"}

### ステップ 2:カタログを作成する {#step-2-create-your-catalog}

リストからカタログを選択し、**カタログを更新** > **フィールドを追加**を選択します。**フィールド名**を入力し、ドロップダウンを使用してデータ型を選択します。必要に応じて繰り返します。

![「rating」と「name」の2つのフィールドの例。]({% image_buster /assets/img_archive/add_catalog_fields.png %}){: style="max-width:50%;"}

**カタログを更新** > **アイテムを追加**を選択し、前に追加したフィールドに基づいて情報を入力してカタログにアイテムを追加します。次に、**アイテムを保存**または**保存して別のアイテムを追加**を選択してアイテムの追加を続けます。

![カタログアイテムの追加。]({% image_buster /assets/img_archive/add_catalog_items.png %}){: style="max-width:50%;"}

{% alert note %}
Brazeはダッシュボードのタイムスタンプに基づいて時刻値を処理します。たとえば、列の値が「03/13/2024」で、タイムゾーンが太平洋時間の場合、この時刻はBrazeに「Mar 12, 2024, 5:00 PM」としてインポートされます。
{% endalert %}
{% endtab %}
{% endtabs %}

## カタログのデータ型 {#catalog-data-types}

カタログは、データを効果的に整理・構造化するためにさまざまなデータ型をサポートしています。次の表は、サポートされている各データ型と、CSVおよびAPIの型名へのマッピングを説明しています。

| データ型 | 形式 | 例 | 説明 |
|-----------|--------|---------|-------------|
| String | テキスト | `"Hello World"` | 名前、説明、IDなどのテキストデータに使用される任意の文字列です。CSVおよびAPIインポートの`string`型に相当します。 |
| Time | ISO 8601またはUnixタイムスタンプ（秒） | `"2024-03-15T14:30:00Z"` | ISO 8601またはUnixタイムスタンプ（秒）形式の日時の値です。APIの`time`型、CSVインポートの`datetime`型に相当します。 |
| Boolean | `true`または`false` | `true` | trueまたはfalseの状態を表す論理値です。CSVおよびAPIインポートの`boolean`型に相当します。 |
| Number | 整数または小数 | `42`または`19.99` | 価格、数量、評価などに使用される整数および浮動小数点数を含む数値です。CSVインポートの`integer`型および`float`型、APIの`number`型に相当します。 |
| Geolocation | `[longitude, latitude]`配列 | `[-73.988103, 40.779109]` | 地理的な位置を表す座標ペアです。経度は-180から180の範囲、緯度は-90から90の範囲でなければなりません。APIの`type`値は`geo`です。カタログUIの**Add Fields**ドロワー、CSVアップロード、またはREST APIで追加できます。 |
| Object | JSONオブジェクト | `{"key": "value", "price": 10}` | 複雑なネストされたデータ構造です。APIの`type`値は`object`です。ダッシュボードではJSON Objectとして表示されます。APIまたはCloud Data Ingestion（CDI）経由でのみ利用可能です。 |
| Array | 文字列の配列 | `["red", "blue", "green"]` | 文字列値のリストです。APIの`type`値は`array`です。ダッシュボードではString arrayとして表示されます。APIまたはCDI経由でのみ利用可能です。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

## カタログ名でのテンプレートの使用 {#template-catalog-names}

カタログに名前を付ける際、カタログ名にテンプレートを使用することもできます。これにより、言語やキャンペーンなどの変数に基づいてカタログ名をダイナミックに生成できます。例えば、次のように使用できます。

{% raw %}
```liquid
{% assign language = "content_spanish" %}

{% catalog_items {{language}} fall_campaign %}
{{ items[0].body }}
```
{% endraw %}

## カタログの管理 {#managing-catalogs}

### ダッシュボードで {#in-the-dashboard}

CSVをアップロードした後、またはブラウザーでカタログを作成した後にカタログを更新するには、**カタログを更新** > **CSVをアップロード**を選択し、カタログのアイテムを更新、追加、または削除するかを選択します。

### REST APIを使用する {#using-the-rest-api}

カタログの構築が進むにつれて、[カタログ一覧エンドポイント]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs)を使用してワークスペース内のカタログのリストを返すこともできます。

REST APIはJSONオブジェクトや文字列配列を含む、すべての[カタログデータタイプ](#supported-data-types)をサポートしています。JSONオブジェクトと文字列配列は、REST APIを通じてのみ作成または更新できます。

### Cloud Data Ingestionを使用する {#using-cloud-data-ingestion}

[Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data)を通じて、データウェアハウス（Snowflake、Redshift、BigQuery、Databricks、Microsoft Fabric、S3など）からカタログデータを直接同期し、スケジュールに基づいてカタログを維持できます。

## カタログアイテムの管理 {#managing-catalog-items}

カタログの管理に加えて、非同期および同期エンドポイントを使用してカタログアイテムを管理することもできます。これには、カタログアイテムの編集や削除、カタログアイテムの詳細の一覧表示が含まれます。

たとえば、個々のカタログアイテムを編集する場合は、[`/catalogs/catalog_name/items/item_id`エンドポイント]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/patch_catalog_item)を使用できます。

## カタログストレージ {#tiers}

無料版のカタログでは、会社全体のすべてのCSVファイルの合計で最大500 MBのファイルサイズがサポートされています。一方、Catalogs Proバージョンでは、単一のCSVファイルに対して最大2 GBのファイルサイズがサポートされています。

{% alert important %}
Brazeダッシュボードに表示されるパッケージのエンタイトルメントは、表示上の理由から最も近い単位に丸められていますが、購入したエンタイトルメントの全量が付与されています。カタログストレージのアップグレードをリクエストするには、Brazeのアカウントマネージャーにお問い合わせください。
{% endalert %}

### 無料版 {#free-version}

無料版カタログのストレージサイズは最大500&nbsp;MBです。500&nbsp;MB未満であれば、アイテム数に制限はありません。

#### Catalogs Pro {#catalogs-pro}

会社レベルで、Catalogs Proの最大ストレージはカタログデータのサイズに基づきます。ストレージサイズのオプションは、5&nbsp;GB、10&nbsp;GB、15&nbsp;GBのいずれかです。なお、無料版のストレージ（500&nbsp;MB）はこれらの各プランに含まれています。

## 仕様 {#specifications}

以下の表は、カタログに含めることができる内容の仕様をまとめたものです。

| エリア | 仕様 |
|------|-----------|
| アイテム値の文字数 | 1つの値につき最大5,000文字。たとえば、`description`というラベルのフィールドがある場合、そのフィールド内の最大文字数は5,000文字です。 |
| アイテム列名の文字数 | 最大250文字 |
| カタログあたりのセレクション数 | カタログあたり最大30セレクション |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
カタログのLiquidタグは再帰的に使用できません。つまり、同じLiquid評価内で別のカタログアイテムを呼び出すカタログアイテムを参照することはできません。
{% endalert %}