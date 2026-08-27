---
nav_title: ベストプラクティス
article_title: ベストプラクティス
toc_headers: h2
page_order: 1
page_type: reference
description: "このページでは、クラウドデータ取り込みの概要、ベストプラクティス、製品の制限事項について説明します。"
---

# ベストプラクティス {#best-practices}

> Brazeクラウドデータ取り込みを使用すると、データウェアハウスやファイルストレージシステムからBrazeへの直接接続を設定して、関連するユーザーデータやカタログデータを同期できます。このデータをBrazeに同期すると、パーソナライゼーション、トリガー、セグメンテーションなどのユースケースに活用できます。

## `UPDATED_AT`列について {#understanding-the-updated_at-column}

{% alert note %}
`UPDATED_AT`はデータウェアハウス連携にのみ関連するものであり、S3同期には適用されません。
{% endalert %}

同期が実行されると、Brazeはデータウェアハウスインスタンスに直接接続し、指定されたテーブルからすべての新しいデータを取得し、Brazeダッシュボード上の対応するデータを更新します。同期が実行されるたびに、Brazeは更新されたデータを反映します。

{% alert important %}
Braze CDIは、行の内容がBrazeの現在のデータと同じかどうかに関係なく、`UPDATED_AT`の値に基づいて厳密に行を同期します。そのため、不要なデータポイント使用量を避けるために、`UPDATED_AT`を適切に使用して新規または更新されたデータのみを同期することを推奨します。
{% endalert %}

### 例：定期的な同期 {#example-recurring-sync}

CDI同期で`UPDATED_AT`がどのように使用されるかを説明するために、ユーザー属性を更新する定期的な同期の例を考えてみましょう。

- ファイルストレージソース
   - Amazon S3

## サポートされるデータ型 {#supported-data-types}

Cloud Data Ingestionは以下のデータ型をサポートしています：
- ユーザー属性（以下を含む）:
   - 階層化カスタム属性
   - オブジェクトの配列
   - 購読ステータス
- カスタムイベント
- 購入イベント
- カタログアイテム
- ユーザー削除リクエスト

### データ型の問題を回避する {#avoiding-data-type-issues}

CDIを使用して外部ソース（DatabricksやSnowflakeなど）からデータを同期する場合、同期前にソースカラムが正しいデータ型を使用していることを確認してください。一般的な問題には以下のようなものがあります：

- **文字列として保存されたタイムスタンプ:** 日付カラムがソースデータベースでvarcharや文字列型ではなく、タイムスタンプ型またはdatetime型を使用していることを確認してください。
- **文字列として保存された数値:** 同期前にソースクエリで数値カラムを整数型または浮動小数点型にキャストしてください。
- **同期間で一貫性のない型:** カラムの型が同期間で変更されると、Brazeが新しいデータを拒否する場合があります。ソーススキーマの一貫性を維持してください。

Brazeダッシュボードでカスタム属性のデータ型を強制または変更する方法については、[カスタムデータの管理]({{site.baseurl}}/user_guide/data/activation/custom_data/managing_custom_data#forcing-data-type-comparisons)を参照してください。

external ID、ユーザーエイリアス、Braze ID、メール、または電話番号でユーザーデータを更新できます。external ID、ユーザーエイリアス、またはBraze IDでユーザーを削除できます。

## 同期される内容 {#what-gets-synced}

同期が実行されるたびに、Brazeはまだ同期されていない行を検索します。これはテーブルまたはビューの`UPDATED_AT`列を使用して確認されます。Brazeは`UPDATED_AT`が最後に同期された`UPDATED_AT`の値よりも後の行をすべて選択してインポートします。実行間に同じタイムスタンプで新しい行が追加された場合、境界タイムスタンプの行も再同期されることがあります。

{% alert important %}
CDIは最後に同期された`UPDATED_AT`の値における行数を追跡します。実行間に同じタイムスタンプで新しい行が追加されると、CDIは包含的な境界（`>=`）に切り替え、すでに処理済みの行を含むそのタイムスタンプのすべての行を再同期します。重複した同期や不要なデータポイント消費を避けるため、同期の実行間で一意の`UPDATED_AT`値を使用してください。詳細については、[重複するタイムスタンプでの行の再同期を避ける](#avoid-resyncing-rows-with-duplicate-timestamps)を参照してください。
{% endalert %}

データウェアハウスで、以下のユーザーと属性をテーブルに追加し、`UPDATED_AT`の時刻をこのデータを追加した時刻に設定します。

<table role="presentation">
  <thead>
    <tr>
      <th>UPDATED_AT</th>
      <th>EXTERNAL_ID</th>
      <th>PAYLOAD</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>2022-07-17 08:30:00</code></td>
      <td><code>customer_1234</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_2": {
        "attribute_a":"example_value_1",
        "attribute_b":"example_value_1"
    },
    "attribute_3":"2019-07-16T19:20:30+1:00"
}
{% endhighlight %}
      </td>
    </tr>
    <tr>
      <td><code>2022-07-18 11:59:23</code></td>
      <td><code>customer_3456</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_2":42,
    "attribute_3":"2019-07-16T19:20:30+1:00",
    "attribute_5":"testing"
}
{% endhighlight %}
      </td>
    </tr>
    <tr>
      <td><code>2022-07-19 09:07:23</code></td>
      <td><code>customer_5678</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_4":true,
    "attribute_5":"testing_123"
}
{% endhighlight %}
      </td>
    </tr>
  </tbody>
</table>

次のスケジュールされた同期で、Brazeは最後に同期されたタイムスタンプよりも後の`UPDATED_AT`タイムスタンプを持つすべての行を同期します。Brazeはフィールドを更新または追加するため、毎回完全なユーザープロファイルを同期する必要はありません。同期後、ユーザープロファイルには新しい更新が反映されます。

**定期同期、2回目の実行：2022年7月20日午後12時**

<table role="presentation">
  <thead>
    <tr>
      <th>UPDATED_AT</th>
      <th>EXTERNAL_ID</th>
      <th>PAYLOAD</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>2022-07-17 08:30:00</code></td>
      <td><code>customer_1234</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_2": {
        "attribute_a":"example_value_2",
        "attribute_b":"example_value_2"
    },
    "attribute_3":"2019-07-16T19:20:30+1:00"
}
{% endhighlight %}
      </td>
    </tr>
    <tr>
      <td><code>2022-07-18 11:59:23</code></td>
      <td><code>customer_3456</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_2":42,
    "attribute_3":"2019-07-16T19:20:30+1:00",
    "attribute_5":"testing"
}
{% endhighlight %}
      </td>
    </tr>
    <tr>
      <td><code>2022-07-19 09:07:23</code></td>
      <td><code>customer_5678</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_4":true,
    "attribute_5":"testing_123"
}
{% endhighlight %}
      </td>
    </tr>
    <tr>
      <td><code>2022-07-16 00:25:30</code></td>
      <td><code>customer_9012</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_4":false,
    "attribute_5":"testing_123"
}
{% endhighlight %}
      </td>
    </tr>
  </tbody>
</table>

`customer_9012`に新しい行が追加されましたが、その`UPDATED_AT`の値（`2022-07-16 00:25:30`）は保存されたタイムスタンプ（`2022-07-19 09:07:23`）よりも前のため、同期されません。しかし、`customer_5678`の既存の行は保存されたタイムスタンプと同じ`UPDATED_AT`の値を持っているため、包含的な境界により再同期されます。この動作の詳細については、[UPDATED_ATの時刻が同期の時刻と同じにならないようにする](#make-sure-the-updated_at-time-isnt-the-same-time-as-your-sync)を参照してください。保存された`UPDATED_AT`は`2022-07-19 09:07:23`のままです。

**定期同期、3回目の実行：2022年7月21日午後12時**

<table role="presentation">
  <thead>
    <tr>
      <th>UPDATED_AT</th>
      <th>EXTERNAL_ID</th>
      <th>PAYLOAD</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>2022-07-17 08:30:00</code></td>
      <td><code>customer_1234</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_2": {
        "attribute_a":"example_value_1",
        "attribute_b":"example_value_1"
    },
    "attribute_3":"2019-07-16T19:20:30+1:00"
}
{% endhighlight %}
      </td>
    </tr>
    <tr>
      <td><code>2022-07-18 11:59:23</code></td>
      <td><code>customer_3456</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_2":42,
    "attribute_3":"2019-07-16T19:20:30+1:00",
    "attribute_5":"testing"
}
{% endhighlight %}
      </td>
    </tr>
    <tr>
      <td><code>2022-07-19 09:07:23</code></td>
      <td><code>customer_5678</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_4":true,
    "attribute_5":"testing_123"
}
{% endhighlight %}
      </td>
    </tr>
    <tr>
      <td><code>2022-07-16 00:25:30</code></td>
      <td><code>customer_9012</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"xyz",
    "attribute_4":false,
    "attribute_5":"testing_123"
}
{% endhighlight %}
      </td>
    </tr>
    <tr>
      <td><code>2022-07-21 08:30:00</code></td>
      <td><code>customer_1234</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_2": {
        "attribute_a":"example_value_2",
        "attribute_b":"example_value_2"
    },
    "attribute_3":"2019-07-20T19:20:30+1:00"
}
{% endhighlight %}
      </td>
    </tr>
  </tbody>
</table>

この3回目の実行では、`customer_1234`に新しい行が追加され、その`UPDATED_AT`の値（`2022-07-21 08:30:00`）は保存されたタイムスタンプよりも後のため、同期されます。この新しい行と、保存されたタイムスタンプと同じ`UPDATED_AT`を持つ`customer_5678`の既存の行の両方が同期されます。保存された`UPDATED_AT`は`2022-07-21 08:30:00`に更新されます。

{% alert note %}
`UPDATED_AT`の値は、特定の同期の実行開始時刻よりも後の値にすることも可能です。ただし、これは推奨されません。最後の`UPDATED_AT`タイムスタンプが「未来」に押し出され、その後の同期でそれ以前の値が同期されなくなるためです。
{% endalert %}

## `UPDATED_AT`列にはUTCタイムスタンプを使用する {#use-a-utc-timestamp-for-the-updated_at-column}

`UPDATED_AT`列は、夏時間に関する問題を防ぐためにUTCで設定する必要があります。可能な限り、`CURRENT_DATE()`ではなく`SYSDATE()`などのUTC専用の関数を使用してください。

## 重複タイムスタンプによる行の再同期を避ける {#avoid-resyncing-rows-with-duplicate-timestamps}

CDIは、最後に同期された`UPDATED_AT`タイムスタンプにおける行数を追跡します。CDIが前回の実行以降に同じタイムスタンプで新しい行が追加されたことを検出すると、包含境界（`>=`）を使用してそのタイムスタンプのすべての行（すでに処理済みのものを含む）を再選択します。それ以外の場合、CDIは排他境界（`>`）を使用し、最後に同期された値よりも厳密に後の行のみを選択します。

例えば、同期が`UPDATED_AT = 2025-04-01 00:00:00`の5行を処理し、後から同じタイムスタンプで6行目が追加された場合、次の同期はカウントの変化を検出し、6行すべてを再同期します。これにより、重複データや不要なデータポイント消費が発生する可能性があります。

これを避けるには：

- `VIEW`に対して同期を設定する場合、デフォルト値として`CURRENT_TIMESTAMP`を使用しないでください。`UPDATED_AT`フィールドがクエリの実行時刻に評価されるため、同期が実行されるたびにすべてのデータが同期されてしまいます。
- 長時間実行されるパイプラインやクエリがソーステーブルにデータを書き込んでいる場合、同期と同時に実行することを避けるか、挿入される各行に同じタイムスタンプを使用することを避けてください。
- トランザクションを使用して、同じタイムスタンプを共有するすべての行を書き込みます。
- ユニークで単調増加する`UPDATED_AT`の値を使用して、処理済みの行が再選択されることを防ぎます。

### 例：後続の更新を管理する {#example-managing-subsequent-updates}

この例では、最初にデータを同期し、その後の更新では変更されたデータ（差分）のみを更新する一般的なプロセスを示します。ユーザーデータを含むテーブル`EXAMPLE_DATA`があるとします。1日目のテーブルには次の値があります：

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;font-size: 14px; font-weight: bold; background-color: #f4f4f7; text-transform: lowercase; color: #212123; font-family: "Aribau Grotesk Bold", "Aribau Grotesk", "Aribau Grotesk Regular", Arial, Helvetica, sans-serif;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top;word-break:normal}
</style>

<table aria-label="例：後続の更新を管理する">
  <caption>例：後続の更新を管理する</caption>
    <thead>
        <tr>
            <th>external_id</th>
            <th>attribute_1</th>
            <th>attribute_2</th>
            <th>attribute_3</th>
            <th>attribute_4</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>12345</td>
            <td>823</td>
            <td>blue</td>
            <td>380</td>
            <td>FALSE</td>
        </tr>
        <tr>
            <td>23456</td>
            <td>28</td>
            <td>blue</td>
            <td>823</td>
            <td>TRUE</td>
        </tr>
        <tr>
            <td>34567</td>
            <td>234</td>
            <td>blue</td>
            <td>384</td>
            <td>TRUE</td>
        </tr>
        <tr>
            <td>45678</td>
            <td>245</td>
            <td>red</td>
            <td>349</td>
            <td>TRUE</td>
        </tr>
        <tr>
            <td>56789</td>
            <td>1938</td>
            <td>red</td>
            <td>813</td>
            <td>FALSE</td>
        </tr>
    </tbody>
</table>

このデータをCDIが期待する形式に変換するには、次のクエリを実行します：

```sql
SELECT
    CURRENT_TIMESTAMP AS UPDATED_AT,
    EXTERNAL_ID AS EXTERNAL_ID,
    TO_JSON(
        OBJECT_CONSTRUCT(
            'attribute_1', attribute_1,
            'attribute_2', attribute_2,
            'attribute_3', attribute_3,
            'attribute_4', attribute_4
        )
    ) AS PAYLOAD
FROM EXAMPLE_DATA;
```

このデータはまだBrazeに同期されていないため、CDIのソーステーブルにすべて追加します：

<table role="presentation">
  <thead>
    <tr>
      <th>UPDATED_AT</th>
      <th>EXTERNAL_ID</th>
      <th>PAYLOAD</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>2023-03-16 15:00:00</td>
      <td>12345</td>
      <td><code>{ "ATTRIBUTE_1": "823", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"380", "ATTRIBUTE_4":"FALSE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-16 15:00:00</td>
      <td>23456</td>
      <td><code>{ "ATTRIBUTE_1": "28", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"823", "ATTRIBUTE_4":"TRUE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-16 15:00:00</td>
      <td>34567</td>
      <td><code>{ "ATTRIBUTE_1": "234", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"384", "ATTRIBUTE_4":"TRUE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-16 15:00:00</td>
      <td>45678</td>
      <td><code>{ "ATTRIBUTE_1": "245", "ATTRIBUTE_2":"red", "ATTRIBUTE_3":"349", "ATTRIBUTE_4":"TRUE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-16 15:00:00</td>
      <td>56789</td>
      <td><code>{ "ATTRIBUTE_1": "1938", "ATTRIBUTE_2":"red", "ATTRIBUTE_3":"813", "ATTRIBUTE_4":"FALSE"}</code></td>
    </tr>
  </tbody>
</table>

同期が実行され、Brazeは「2023-03-16 15:00:00」までの利用可能なすべてのデータを同期したと記録します。次に、2日目の朝にETLが実行され、ユーザーテーブルの一部のフィールドが更新されます（*で示されています）：

<table aria-label="例：後続の更新を管理する">
  <caption>例：後続の更新を管理する。*は前回の同期以降に更新されたフィールドを示します。</caption>
    <thead>
        <tr>
            <th>external_id</th>
            <th>attribute_1</th>
            <th>attribute_2</th>
            <th>attribute_3</th>
            <th>attribute_4</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>12345</td>
            <td style="background-color: #FFFF00;">145*</td>
            <td style="background-color: #FFFF00;">red*</td>
            <td>380</td>
            <td style="background-color: #FFFF00;">TRUE*</td>
        </tr>
        <tr>
            <td>23456</td>
            <td style="background-color: #FFFF00;">15*</td>
            <td>blue</td>
            <td>823</td>
            <td>TRUE</td>
        </tr>
        <tr>
            <td>34567</td>
            <td>234</td>
            <td>blue</td>
            <td style="background-color: #FFFF00;">495*</td>
            <td style="background-color: #FFFF00;">FALSE*</td>
        </tr>
        <tr>
            <td>45678</td>
            <td>245</td>
            <td style="background-color: #FFFF00;">green*</td>
            <td>349</td>
            <td>TRUE</td>
        </tr>
        <tr>
            <td>56789</td>
            <td>1938</td>
            <td>red</td>
            <td style="background-color: #FFFF00;">693*</td>
            <td>FALSE</td>
        </tr>
    </tbody>
</table>

ここで、変更された値のみをCDIソーステーブルに追加する必要があります。古い行を更新するのではなく、これらの行を追加（アペンド）できます。そのテーブルは次のようになります：

<table role="presentation">
  <thead>
    <tr>
      <th>UPDATED_AT</th>
      <th>EXTERNAL_ID</th>
      <th>PAYLOAD</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>2023-03-16 15:00:00</td>
      <td>12345</td>
      <td><code>{ "ATTRIBUTE_1": "823", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"380", "ATTRIBUTE_4":"FALSE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-16 15:00:00</td>
      <td>23456</td>
      <td><code>{ "ATTRIBUTE_1": "28", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"823", "ATTRIBUTE_4":"TRUE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-16 15:00:00</td>
      <td>34567</td>
      <td><code>{ "ATTRIBUTE_1": "234", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"384", "ATTRIBUTE_4":"TRUE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-16 15:00:00</td>
      <td>45678</td>
      <td><code>{ "ATTRIBUTE_1": "245", "ATTRIBUTE_2":"red", "ATTRIBUTE_3":"349", "ATTRIBUTE_4":"TRUE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-16 15:00:00</td>
      <td>56789</td>
      <td><code>{ "ATTRIBUTE_1": "1938", "ATTRIBUTE_2":"red", "ATTRIBUTE_3":"813", "ATTRIBUTE_4":"FALSE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-17 09:30:00</td>
      <td>12345</td>
      <td><code>{ "ATTRIBUTE_1": "145", "ATTRIBUTE_2":"red", "ATTRIBUTE_4":"TRUE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-17 09:30:00</td>
      <td>23456</td>
      <td><code>{ "ATTRIBUTE_1": "15"}</code></td>
    </tr>
    <tr>
      <td>2023-03-17 09:30:00</td>
      <td>34567</td>
      <td><code>{ "ATTRIBUTE_3":"495", "ATTRIBUTE_4":"FALSE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-17 09:30:00</td>
      <td>45678</td>
      <td><code>{ "ATTRIBUTE_2":"green"}</code></td>
    </tr>
    <tr>
      <td>2023-03-17 09:30:00</td>
      <td>56789</td>
      <td><code>{ "ATTRIBUTE_3":"693"}</code></td>
    </tr>
  </tbody>
</table>

CDIは新しい行のみを同期するため、次に実行される同期では最後の5行のみが同期されます。

## その他のヒント {#additional-tips}

### 消費量を最小限に抑えるため、新規または更新された属性のみを書き込む {#only-write-new-or-updated-attributes-to-minimize-consumption}

同期が実行されるたびに、Brazeは以前に同期されていない行を探します。これはテーブルまたはビューの`UPDATED_AT`列を使用して確認されます。Brazeは、`UPDATED_AT`が最後に同期された`UPDATED_AT`値よりも新しいすべての行を選択してインポートします。これは、現在のユーザープロファイルの値と同じかどうかに関係なく行われます。境界タイムスタンプの行も、新しい行が同じタイムスタンプを共有している場合に再同期される可能性があります。このため、追加または更新したい属性のみを同期することをお勧めします。

CDIを使用した場合のデータポイント使用量は、REST APIやSDKなどの他の取り込み方法と同じです。そのため、ソーステーブルに新規または更新された属性のみを追加するようにしてください。

### `EXTERNAL_ID`を`PAYLOAD`列から分離する {#separate-external_id-from-payload-column}

`PAYLOAD`オブジェクトにexternal IDやその他のIDタイプを含めないでください。

### 属性を削除する {#remove-an-attribute}

ユーザープロファイルから属性を省略したい場合は、`null`に設定できます。属性を変更せずに保持したい場合は、更新されるまでBrazeに送信しないでください。属性を完全に削除するには、`TO_JSON(OBJECT_CONSTRUCT_KEEP_NULL(...))`を使用します。

### 増分更新を行う {#make-incremental-updates}

同時更新による意図しない上書きを防ぐため、データに増分更新を行ってください。

{% alert important %}
* **異なる属性への更新：** 大多数のケースでは、2つの更新がユーザーの同じ属性に影響を与えない場合、完全に独立した結果になります。たとえば、ユーザーの`Color`属性を更新し、別途`Size`属性を更新する場合、数秒以内に発生しても両方の更新が正しく適用されます。
* **同じ属性への更新：** 単一の同期実行中に複数の更新が同じ属性をターゲットにすると、競合が発生する可能性があります。これらのまれなケースでは、一方の更新がもう一方を上書きする場合があります。この動作を防ぐ最善の方法は、CDI同期のソースデータが各ユーザーの最新の状態のみを反映するようにするか、特定のユーザーまたはユーザー＋属性ペアのすべての更新を単一の行に含めることです。
* **オブジェクト配列オペレーター：** 独立した更新の唯一の例外は、オブジェクト配列の`$add`、`$remove`、`$update`オペレーターであり、同じ配列への更新が互いに影響する可能性があります。
* **イベント：** 各イベントは一意であり、関連付けられたタイムスタンプを持つため、競合はイベントに影響しません。
{% endalert %}

この動作を防ぐ最善の方法は、CDI同期のソースデータが各ユーザーの最新の状態のみを反映するようにするか、特定のユーザーまたはユーザー＋属性ペアのすべての更新を単一の行に含めることです。

### 別のテーブルからJSON文字列を作成する {#create-a-json-string-from-another-table}

各属性を個別の列に内部的に保存する場合は、Brazeとの同期を設定するために、それらの列をJSON文字列に変換する必要があります。これを行うには、次のようなクエリを使用できます。

{% tabs local %}
{% tab Snowflake %}
Snowflakeでこのクエリを使用して、ソース列をCDIフィールドにフォーマットします。
```sql
CREATE TABLE "EXAMPLE_USER_DATA"
    (attribute_1 string,
     attribute_2 string,
     attribute_3 number,
     my_user_id string);

SELECT
    CURRENT_TIMESTAMP as UPDATED_AT,
    my_user_id as EXTERNAL_ID,
    TO_JSON(
        OBJECT_CONSTRUCT (
            'attribute_1',
            attribute_1,
            'attribute_2',
            attribute_2,
            'yet_another_attribute',
            attribute_3)
    )as PAYLOAD FROM "EXAMPLE_USER_DATA";
```
{% endtab %}
{% tab Redshift %}
Redshiftでこのクエリを使用して、ソース列をCDIフィールドにフォーマットします。
```sql
CREATE TABLE "EXAMPLE_USER_DATA"
    (attribute_1 string,
     attribute_2 string,
     attribute_3 number,
     my_user_id string);

SELECT
    CURRENT_TIMESTAMP as UPDATED_AT,
    my_user_id as EXTERNAL_ID,
    JSON_SERIALIZE(
        OBJECT (
            'attribute_1',
            attribute_1,
            'attribute_2',
            attribute_2,
            'yet_another_attribute',
            attribute_3)
    ) as PAYLOAD FROM "EXAMPLE_USER_DATA";
```
{% endtab %}
{% tab BigQuery %}
BigQueryでこのクエリを使用して、ソース列をCDIフィールドにフォーマットします。
```sql
CREATE OR REPLACE TABLE BRAZE.EXAMPLE_USER_DATA (attribute_1 string,
     attribute_2 STRING,
     attribute_3 NUMERIC,
     my_user_id STRING);

SELECT
    CURRENT_TIMESTAMP as UPDATED_AT,
    my_user_id as EXTERNAL_ID,
    TO_JSON(
      STRUCT(
        'attribute_1' AS attribute_1,
        'attribute_2'AS attribute_2,
        'yet_another_attribute'AS attribute_3
      )
    ) as PAYLOAD
  FROM BRAZE.EXAMPLE_USER_DATA;
```
{% endtab %}
{% tab Databricks %}
Databricksでこのクエリを使用して、ソース列をCDIフィールドにフォーマットします。
```sql
CREATE OR REPLACE TABLE BRAZE.EXAMPLE_USER_DATA (
    attribute_1 string,
    attribute_2 STRING,
    attribute_3 NUMERIC,
    my_user_id STRING
);

SELECT
    CURRENT_TIMESTAMP as UPDATED_AT,
    my_user_id as EXTERNAL_ID,
    TO_JSON(
      STRUCT(
        attribute_1,
        attribute_2,
        attribute_3
      )
    ) as PAYLOAD
  FROM BRAZE.EXAMPLE_USER_DATA;
```
{% endtab %}
{% tab Microsoft Fabric %}
Microsoft Fabricでこのクエリを使用して、ソース列をCDIフィールドにフォーマットします。
```sql
CREATE TABLE [braze].[users] (
    attribute_1 VARCHAR,
    attribute_2 VARCHAR,
    attribute_3 VARCHAR,
    attribute_4 VARCHAR,
    user_id VARCHAR
)
GO

CREATE VIEW [braze].[user_update_example]
AS SELECT
    user_id as EXTERNAL_ID,
    CURRENT_TIMESTAMP as UPDATED_AT,
    JSON_OBJECT('attribute_1':attribute_1, 'attribute_2':attribute_2, 'attribute_3':attribute_3, 'attribute_4':attribute_4) as PAYLOAD

FROM [braze].[users] ;
```
{% endtab %}

{% endtabs %}

### `UPDATED_AT`タイムスタンプを使用する {#use-the-updated_at-timestamp}

Brazeは`UPDATED_AT`タイムスタンプを使用して、正常に同期されたデータを追跡します。CDIは、最後に同期されたタイムスタンプの行数も追跡します。実行間にそのタイムスタンプと同じ新しい行が追加された場合、CDIはそのタイムスタンプのすべての行を再同期するため、データが重複する可能性があります。詳細とヒントについては、[重複タイムスタンプの行の再同期を回避する](#avoid-resyncing-rows-with-duplicate-timestamps)を参照してください。

### テーブルの設定 {#table-configuration}

ベストプラクティスやコードスニペットを共有するための公開[GitHubリポジトリ](https://github.com/braze-inc/braze-examples/tree/main/cloud-data-ingestion)があります。独自のスニペットを投稿するには、プルリクエストを作成してください。

### データのフォーマット {#data-formatting}

クラウドデータ取り込みのテーブル設定要件とペイロードのフォーマット要件は、[クラウドデータ取り込みのテーブル設定]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/table_setup)に記載されています。

このページでは以下を区別できます。

- ソーステーブルの要件（必須列、識別子列、`UPDATED_AT`の動作）
- ペイロードの要件（各データタイプで`/users/track`オブジェクト形式に一致する必要があるフィールド）

### データウェアハウスクエリのタイムアウトを回避する {#avoid-timeouts-for-data-warehouse-queries}

最適なパフォーマンスと潜在的なエラーを回避するために、クエリは1時間以内に完了することをお勧めします。クエリがこの時間枠を超える場合は、データウェアハウスの設定を確認してください。ウェアハウスに割り当てられるリソースを最適化することで、クエリの実行速度を向上させることができます。

## 製品の制限事項 {#product-limitations}

| 制限事項            | 説明                                                                                                                                                                        |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 連携数 | 設定できる連携の数に制限はありません。ただし、テーブルまたはビューごとに設定できる連携は1つのみです。                                             |
| 行数         | デフォルトでは、各実行で最大5億行を同期できます。Brazeは5億行を超える新しい行がある同期を停止します。これより高い制限が必要な場合は、BrazeのカスタマーサクセスマネージャーまたはBrazeサポートにお問い合わせください。 |
| 行あたりの属性数     | 各行には、1つのユーザーIDと最大250個の属性を含むJSONオブジェクトが含まれている必要があります。JSONオブジェクトの各キーは1つの属性としてカウントされます（つまり、配列は1つの属性としてカウントされます）。 |
| ペイロードサイズ           | 各行には最大1 MBのペイロードを含めることができます。Brazeは1&nbsp;MBを超えるペイロードを拒否し、「Payload was greater than 1MB」というエラーを、関連するexternal IDおよび切り捨てられたペイロードとともに同期ログに記録します。 |
| データ型              | クラウドデータ取り込みを通じて、ユーザー属性、イベント、購入を同期できます。                                                                                                  |
| Brazeリージョン           | この製品はすべてのBrazeリージョンで利用できます。どのBrazeリージョンからでも、任意のソースデータリージョンに接続できます。                                                                              |
| ソースリージョン       | Brazeは、任意のリージョンまたはクラウドプロバイダーのデータウェアハウスまたはクラウド環境に接続します。                                                                                        |
{: .reset-td-br-1 .reset-td-br-2 aria-label="製品の制限事項" }

<br><br>