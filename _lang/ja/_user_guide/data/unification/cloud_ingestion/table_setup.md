---
nav_title: テーブル設定
article_title: クラウドデータ取り込みのテーブル設定
toc_headers: h2
page_order: 2
page_type: reference
description: "CDIソーステーブルの設定方法と、ペイロードフォーマット要件との違いについて説明します。"
---

# クラウドデータ取り込みのテーブル設定 {#cloud-data-ingestion-table-setup}

> このページでは、クラウドデータ取り込み（CDI）に関連する2つの異なる要件、ソーステーブルの設定とペイロードフォーマットについて説明します。

## テーブル設定とペイロードフォーマットの違いを理解する {#understand-table-setup-compared-to-payload-formatting}

CDIユーザーデータ同期では、以下の両方を設定します。

| レイヤー | 制御する内容 |
| --- | --- |
| ソーステーブルの設定 | 必須カラム、ユーザー識別子、`UPDATED_AT`の同期動作 |
| ペイロードフォーマット | `PAYLOAD`内のJSONフィールド（属性、イベント、購入のオブジェクト構造を含む） |
{: .reset-td-br-1 .reset-td-br-2 aria-label="テーブル設定とペイロードフォーマットの違いを理解する" }

Brazeはまずソーステーブルから行を読み取り、次に選択されたデータタイプに基づいて`PAYLOAD`フィールドを検証します。

## ソーステーブルを設定する {#set-up-your-source-table}

データウェアハウスのユーザーデータ同期では、ソーステーブルまたはビューに以下を含める必要があります。

- `UPDATED_AT`
- `PAYLOAD`
- 1つ以上のサポートされているユーザー識別子カラム:
  - `EXTERNAL_ID`
  - `ALIAS_NAME`と`ALIAS_LABEL`
  - `BRAZE_ID`
  - `EMAIL`
  - `PHONE`

テーブルに複数の識別子カラムが含まれている場合でも、各行には一度に1つの識別子タイプのみを含めてください。

### `UPDATED_AT`の要件 {#updated_at-requirements}

- 夏時間の問題を避けるため、`UPDATED_AT`の値はUTCで保存してください。
- Brazeは、`UPDATED_AT`が最後に同期された値より後の行を同期します。
- 新しい行が同じタイムスタンプを共有している場合、境界タイムスタンプの行が再同期されることがあります。

重複タイムスタンプと増分更新に関するガイダンスについては、[クラウドデータ取り込みのベストプラクティス]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/best_practices#avoid-resyncing-rows-with-duplicate-timestamps)を参照してください。

{% alert note %}
ファイルストレージソースは異なる設定要件を使用し、`UPDATED_AT`をサポートしていません。詳細については、[ファイルストレージ統合]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/file_storage_integrations#required-file-formats)を参照してください。
{% endalert %}

## `PAYLOAD`カラムを設定する {#set-up-the-payload-column}

`PAYLOAD`の値は、選択されたデータタイプに対してBrazeの`/users/track`エンドポイントで使用されるものと同じオブジェクトフォーマットに従います。

| データタイプ | フォーマット参照 |
| --- | --- |
| `attributes` | [ユーザー属性オブジェクト]({{site.baseurl}}/api/objects_filters/user_attributes_object) |
| `events` | [イベントオブジェクト]({{site.baseurl}}/api/objects_filters/event_object) |
| `purchases` | [購入オブジェクト]({{site.baseurl}}/api/objects_filters/purchase_object) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="PAYLOADカラムを設定する" }

階層化属性の場合は、[オブジェクトプロパティとしての日付のキャプチャ]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support#capturing-dates-as-object-properties)に記載されているフォーマットを使用して日付を含めてください。

### ペイロードの例 {#payload-examples}

{% tabs local %}
{% tab 階層化カスタム属性 %}
カスタム属性同期のペイロードカラムに階層化カスタム属性を含めることができます。

```json
{
      "most_played_song": {
        "song_name": "Solea",
        "artist_name": "Miles Davis",
        "album_name": "Sketches of Spain",
        "genre": "Jazz",
        "play_analytics": {
            "count": 1000,
            "top_10_listeners": true
        }
      }
}
```

{% endtab %}
{% tab イベント %}
イベントを同期するには、イベント名が必須です。`time`フィールドはISO 8601文字列または`yyyy-MM-dd'T'HH:mm:ss:SSSZ`フォーマットで指定してください。`time`フィールドが存在しない場合、Brazeは`UPDATED_AT`カラムの値をイベント時刻として使用します。`app_id`や`properties`などのその他のフィールドはオプションです。

1行につき1つのイベントを同期できます。

```json
{
    "app_id" : "your-app-id",
    "name" : "rented_movie",
    "time" : "2013-07-16T19:20:45+01:00",
    "properties": {
        "movie": "The Sad Egg",
        "director": "Alex Smith"
    }
}
```

{% endtab %}
{% tab 購入 %}
購入イベントを同期するには、`product_id`、`currency`、`price`が必須です。オプションの`time`フィールドはISO 8601文字列または`yyyy-MM-dd'T'HH:mm:ss:SSSZ`フォーマットで指定してください。`time`フィールドが存在しない場合、Brazeは`UPDATED_AT`カラムの値をイベント時刻として使用します。`app_id`、`quantity`、`properties`などのその他のフィールドはオプションです。

1行につき1つの購入イベントを同期できます。

```json
{
    "app_id" : "11ae5b4b-2445-4440-a04f-bf537764c9ad",
    "product_id" : "Completed Order",
    "currency" : "USD",
    "price" : 219.98,
    "time" : "2013-07-16T19:20:30+01:00",
    "properties" : {
        "products" : [ { "name": "Monitor", "category": "Gaming", "product_amount": 19.99 },
        { "name": "Gaming Keyboard", "category": "Gaming ", "product_amount": 199.99 }
        ]
    }
}
```

{% endtab %}
{% tab 購読グループ %}
購読グループのステータスを同期するには、各行に1つ以上の`subscription_group_id`と`subscription_state`のペアを含めてください。
```json
{
    "subscription_groups" : [
        {
            "subscription_group_id": "subscription_group_identifier_1",
            "subscription_state": "unsubscribed"
        },
        {
            "subscription_group_id": "subscription_group_identifier_2",
            "subscription_state": "subscribed"
        },
        {
            "subscription_group_id": "subscription_group_identifier_3",
            "subscription_state": "subscribed"
        }
      ]
}
```
{% endtab %}
{% endtabs %}

## 関連するCDI設定ドキュメント {#related-cdi-setup-docs}

- ソース固有のDDL例については、[データウェアハウス統合]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations#step-1-set-up-tables-or-views)を参照してください。
- ファイルベースの設定については、[ファイルストレージ統合]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/file_storage_integrations)を参照してください。
- 同期動作と最適化のガイダンスについては、[クラウドデータ取り込みのベストプラクティス]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/best_practices)を参照してください。