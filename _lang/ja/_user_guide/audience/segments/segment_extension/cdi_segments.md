---
nav_title: CDI セグメントエクステンション
article_title: CDI セグメントエクステンション
page_order: 0
page_type: reference
alias: /cdi_segment_extensions/
tool:
- Segments
description: "この記事では、CDI セグメントエクステンションがクラウドデータ取り込みを使用してデータウェアハウスにクエリを実行し、Brazeでオーディエンスを定義する方法について説明します。"

---

# CDI セグメントエクステンション {#cdi-segment-extensions}

> Brazeの[クラウドデータ取り込み]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion)（CDI）を使用すると、データウェアハウスまたはファイルストレージシステムからBrazeへの直接接続を設定し、関連するユーザーデータやカタログデータを定期的に同期できます。

{% alert warning %}
CDI セグメントエクステンションはデータウェアハウスに直接クエリを実行するため、データウェアハウスでこれらのクエリを実行する際に発生するすべてのコストが課金されます。CDI セグメントエクステンションは[SQLセグメントクレジット]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments#credits)を消費せず、セグメントエクステンションの上限にもカウントされず、データポイントも記録されません。
{% endalert %}

## 前提条件 {#prerequisites}

Brazeワークスペース内でセグメンテーションにデータウェアハウスのデータを使用するには、[接続済みソース]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/connected_sources)を作成してから、[セグメントエクステンション]({{site.baseurl}}/user_guide/audience/segments/segment_extension)内でCDIセグメントを作成する必要があります。CDI セグメントエクステンションを使用すると、CDI接続を通じて利用可能になったデータを使用して、独自のデータウェアハウスに直接クエリを実行するSQLを記述し、Braze内でターゲティングできるユーザーグループを作成できます。

## CDIセグメントの作成 {#creating-a-cdi-segment}

### ステップ1:ソースを設定する {#step-1-set-up-your-source}

最初のCDI セグメントエクステンションを作成する前に、[接続済みソース]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/connected_sources)の手順に従って、データウェアハウスとの新しい接続済みソースを設定します。

### ステップ2:セグメントを作成する {#step-2-create-a-segment}

まず、新しい[セグメントエクステンション]({{site.baseurl}}/user_guide/audience/segments/segment_extension)を作成し、**Full refresh** を選択します。

![セグメントエクステンションのモーダル配置例]({% image_buster /assets/img/segment/segment_extension_modal.png %}){: style="max-width:60%;"}

データソースとして **CDI Data Tables** を選択します。

![ステップ2に関連するスクリーンショット：セグメントの作成]({% image_buster /assets/img/segment/cdi_data_tables.png %}){: style="max-width:60%;"}

CDI設定の一環として、CDI セグメントエクステンションで使用するさまざまな接続を選択できます。各接続には特定のデータテーブルのセットがあります。開発チームがCDI設定時に接続とデータテーブルを構成できます。

利用可能なデータテーブル（スキーマや利用可能な説明を含む）を表示するには、**Reference** を選択します。準備ができたら、接続を選択します。

![利用可能なデータテーブル（スキーマや利用可能な説明を含む）を表示するには、「Reference」を選択します。準備ができたら、接続を選択します。]({% image_buster /assets/img/segment/connection_schema_with_descriptions.png %}){: style="max-width:100%;"}

次に、[Braze SQL構文]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments#step-2-write-your-sql)を使用してセグメントのSQLを記述します。

すべてのCDI セグメントエクステンションでは、選択カラムとして `external_user_id` を使用する必要があり、`external_user_id` はBrazeでユーザーに設定されたものと一致する必要があることに注意してください。

{% alert important %}
`external_user_id` は**文字列**値である必要があります。ソースIDが数値として保存されている場合（例えば、`client_id` が整数の場合）、Brazeの `external_id` 型と一致するように[SQLで文字列にキャストしてください](https://www.w3schools.com/sql/func_sqlserver_cast.asp)。
{% endalert %}

クエリ結果にBrazeに存在しないユーザーが含まれている場合、それらのユーザーは無視されます。BrazeはCDI セグメントエクステンションの出力に基づいて新しいユーザーを作成しません。

{% alert tip %}
セグメントエクステンションのプレビュー方法、セグメントエクステンションの管理方法、自動メンバーシップ更新の実行方法については、[SQLセグメントエクステンション]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments)を参照してください。
{% endalert %}

最後に、Brazeセグメント内で[このセグメントエクステンションを使用]({{site.baseurl}}/user_guide/audience/segments/segment_extension#step-6-use-your-extension-in-a-segment)して、このオーディエンスにキャンペーンまたはキャンバスを送信できます。

## 考慮事項 {#considerations}

- セグメントエクステンションは、複数ではなく1つの接続からのデータのみを参照できます。
- セグメントエクステンションは、データソースとしてCDIデータまたはBraze Snowflake（Currents）データのいずれかを使用できます。セグメントエクステンション内でデータソースを混在させることはできませんが、セグメント内で一緒に参照する複数のセグメントエクステンションを作成できます。

## トラブルシューティング {#troubleshooting}

- クエリは、**クラウドデータ取り込み**ページで各接続同期に設定された最大実行時間に達するとタイムアウトする場合があります。許可される最大実行時間は60分です。
- SQLがデータウェアハウスに適した構文で記述されていることを確認してください。