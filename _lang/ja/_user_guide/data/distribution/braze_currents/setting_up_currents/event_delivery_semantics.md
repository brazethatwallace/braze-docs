---
nav_title: イベント配信のセマンティクス
article_title: イベント配信のセマンティクス
page_order: 2
page_type: reference
description: "このリファレンス記事では、データウェアハウスストレージパートナーに送信するフラットファイルのイベントデータをCurrentsがどのように管理するかを概説および定義します。"
tool: Currents

---

# イベント配信のセマンティクス {#event-delivery-semantics}

> このページでは、データウェアハウスストレージパートナーに送信するフラットファイルのイベントデータをCurrentsがどのように管理するかを概説および定義します。

データストレージ用のCurrentsは、弊社のプラットフォームから、データウェアハウスの[パートナー接続]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/available_partners)の1つにあるストレージバケットに送信されるデータの連続ストリームです。Currentsは通常のしきい値に達するとストレージバケットにAvroファイルを書き込むので、独自のビジネスインテリジェンス (BI) ツールセットを使用してイベントデータの処理および分析ができます。

{% alert important %}
このコンテンツは、**データウェアハウスストレージパートナー (Google Cloud Storage、Amazon S3、Microsoft Azure Blob Storage) に送信するフラットファイルのイベントデータにのみ適用されます**。<br><br>他のパートナーに適用されるコンテンツについては、[利用可能なパートナー]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/available_partners)のリストを参照し、それぞれのページを確認してください。
{% endalert %}

## テストイベント {#test-events}

Currentsの統合を設定する際は、ストレージバケットとの接続を確認するために**Send Test Events**をクリックしてください。これらのテストイベントは、統合がデータを正しく受信し処理できることを検証するものです。

{% alert important %}
**テストイベントデータ形式：**テストイベントには、各フィールドの正しいデータタイプに合致するプレースホルダー値が含まれていますが、現実的または正確なデータは含まれていません。例えば、`timezone`フィールドには有効なタイムゾーン識別子（「America/Chicago」など）ではなくUUIDのような文字列が含まれている場合があります。また、`campaign_name`や`ip_pool`といった他のフィールドも、実際のデータではなくプレースホルダー値を含んでいることがあります。<br>

これは想定どおりの動作です。テストイベントは主に接続と統合設定のテストを目的としており、データの正確性を検証するためのものではありません。正確なデータを含む実際のイベントを確認するには、テスト用のCurrents統合を使用し、実際のイベントデータをパイプライン経由で送信してください。
{% endalert %}

## 1回以上の配信 {#at-least-once-delivery}

Currentsは高スループットのシステムであるため、「1回以上」のイベント配信を保証します。つまり、ストレージバケットにイベントが重複して書き込まれることがまれにあります。これは、何らかの理由でキューからイベントが再処理された場合に発生します。

ユースケースで「厳密に1回」の配信が必要な場合は、すべてのイベントに付与されるユニーク識別子フィールド（`id`）を使用してイベントの重複を排除できます。ファイルがストレージバケットに書き込まれた時点で弊社の管理外となるため、弊社側から重複排除を保証する方法はありません。

## タイムスタンプ {#timestamps}

CurrentsがエクスポートするすべてのタイムスタンプはUTCタイムゾーンで送信されます。一部のイベントでは、利用可能な場合にタイムゾーンフィールドも含まれており、イベント発生時のユーザーのローカルタイムゾーンをInternet Assigned Numbers Authority (IANA) 形式で提供します。

### レイテンシー {#latency}

SDKまたはAPIを通じてBrazeに送信されるイベントには、過去のタイムスタンプが含まれることがあります。最も顕著な例は、モバイル接続がない場合など、SDKデータがキューに入れられるケースです。この場合、イベントのタイムスタンプはイベントが生成された時点を反映します。つまり、一定の割合のイベントが高レイテンシーに見えることがあります。

## Apache Avro形式 {#apache-avro-format}

Braze Currentsのデータストレージ統合は、`.avro`形式でデータを出力します。[Apache Avro](https://avro.apache.org/)を選択した理由は、スキーマの進化をネイティブにサポートする柔軟なデータ形式であり、幅広いデータ製品でサポートされているためです。

- Avroはほぼすべての主要なデータウェアハウスでサポートされています。
- データをS3に残しておきたい場合、AvroはCSVやJSONよりも圧縮率が高いため、ストレージコストが削減され、データの解析に使用するCPUも少なくて済む可能性があります。
- Avroはデータの書き込みまたは読み取り時にスキーマを必要とします。スキーマは時間の経過とともに進化させることができ、既存の処理を壊すことなくフィールドの追加に対応できます。

Currentsは、以下の形式を使用してイベントタイプごとにファイルを作成します。

```
<your-bucket-prefix>/dataexport.<cluster-identifier>.<connection-type-identifier>.integration.<integration-id>/event_type=<event-type>/date=<date>/version=<currents_version>/<environment>/dataexport.<cluster-identifier>.<connection-type-identifier>.integration.<integration-id>+<partition>+<offset>.avro
```

{% alert tip %}
スクロールバーのためにコードが見えませんか？修正方法は[Brazeユーザーガイドのホームページ]({{site.baseurl}}/user_guide)をご覧ください。
{% endalert %}

例えば、プッシュ送信イベントのパスは以下のようになります。

```
currents-export/dataexport.prod-01.S3.integration.69cadaaed2d51b7c75b1a3e5/event_type=users.messages.pushnotification.Send/date=2025-04-01-17/version=6/us-01/dataexport.prod-01.S3.integration.69cadaaed2d51b7c75b1a3e5+0+123456.avro
```

`version`パスセグメントは、`version=6`のような単純な整数のCurrentsバージョン値です。

| ファイル名セグメント | 定義 |
|---|---|
| `<your-bucket-prefix>` | このCurrents統合に設定されたプレフィックスです。 |
| `<cluster-identifier>` | Brazeの内部使用向けです。「prod-01」、「prod-02」、「prod-03」、「prod-04」などの文字列になります。すべてのファイルは同じクラスター識別子を持ちます。|
| `<connection-type-identifier>` | 接続タイプの識別子です。オプションは「S3」、「AzureBlob」、「GCS」です。 |
| `<integration-id>` | このCurrents統合のユニークIDです。 |
| `<event-type>` | ファイル内のイベントのタイプです。 |
| `<date>` | イベントがUTCタイムゾーンで処理のためにシステムのキューに入れられた時間です。YYYY-MM-DD-HH形式です。 |
| `version=<currents_version>` | パイプラインパスのCurrentsバージョンです。この値は`6`のような単純な整数です。 |
| `<environment>` | Brazeの内部使用向けです。 |
| `<partition>` | Brazeの内部使用向けです。整数です。 |
| `<offset>`| Brazeの内部使用向けです。整数です。同じ時間内に送信された異なるファイルは、異なる`<offset>`パラメーターを持ちます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Apache Avro形式" }

{% alert tip %}
ファイルの命名規則は変更される場合があります。Brazeでは、バケット内の &lt;your-bucket-prefix&gt; をプレフィックスとするすべてのキーを検索することを推奨します。
{% endalert %}

### Avro書き込みしきい値 {#avro-write-threshold}

通常の状況では、Brazeは5分ごとまたは15,000イベントごとのいずれか早い方のタイミングでストレージバケットにデータファイルを書き込みます。高負荷時には、1ファイルあたり最大100,000イベントを含む大きなデータファイルを書き込む場合があります。

{% alert important %}
Currentsは空のファイルを書き込むことはありません。
{% endalert %}

### Avroスキーマの変更 {#avro-schema-changes}

Brazeは、フィールドの追加、変更、または削除に伴い、Avroスキーマを変更する場合があります。ここでは、破壊的変更と非破壊的変更の2種類の変更があります。すべてのスキーマ変更はCurrentsのリリースにまとめられ、各リリースではストレージパスの`version=<currents_version>`セグメントが更新されます（例：`version=6`から`version=7`）。Azure Blob Storage、Google Cloud Storage、Amazon S3に書き込まれるCurrentsイベントは、以下のパス形式を使用します。

```
<your-bucket-prefix>/<currents-integration-id>/event_type=<event-type>/date=<date>/version=<currents_version>/<environment>/<avro-file>
```

#### 非破壊的変更 {#non-breaking-changes}

Avroスキーマにフィールドが追加される場合、これは非破壊的変更とみなされます。追加されるフィールドは常に「オプション」のAvroフィールド（デフォルト値が`null`など）であるため、[Avroスキーマ解決仕様](http://avro.apache.org/docs/current/spec.html#schema+resolution)に従って古いスキーマと「一致」します。これらの追加は、既存のETL（Extract, Transform, and Load）プロセスに影響を与えないはずです。フィールドはETLプロセスに追加されるまで単に無視されます。

{% alert important %}
新しいフィールドが追加された際にフローが中断されないよう、ETLの設定では処理するフィールドを明示的に指定することを推奨します。
{% endalert %}

#### 破壊的変更 {#breaking-changes}

Avroスキーマからフィールドが削除または変更される場合、これは破壊的変更とみなされます。破壊的変更では、使用中のフィールドが期待どおりに記録されなくなる可能性があるため、既存のETLプロセスの修正が必要になる場合があります。

すべての破壊的変更は、リリース前に事前に通知されます。

バージョンごとの変更の完全な履歴については、[Currents変更ログ]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs)を参照してください。