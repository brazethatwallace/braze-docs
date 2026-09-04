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

ワークスペース内でデータウェアハウスのデータをセグメンテーションに使用するには、[接続ソース]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/connected_sources)を作成し、次に[セグメントエクステンション]({{site.baseurl}}/user_guide/audience/segments/segment_extension)内で CDI セグメントを作成する必要があります。CDI セグメントエクステンションを使用すると、CDI 接続を通じて利用可能になったデータを使って、自社のデータウェアハウスに直接クエリを実行する SQL を記述し、Braze 内でターゲティングできるユーザーグループを作成できます。

## CDI セグメントの作成 {#creating-a-cdi-segment}

### ステップ1: ソースを設定する {#step-1-set-up-your-source}

最初の CDI セグメントエクステンションを作成する前に、[接続ソース]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/connected_sources)の手順に従って、データウェアハウスとの新しい接続ソースを設定します。

### ステップ2: セグメントを作成する {#step-2-create-a-segment}

1. **オーディエンス** > **セグメントエクステンション**に移動し、**新しいエクステンションを作成**を選択します。
2. **セグメントエクステンション作成エクスペリエンスの選択**メニューで、**フルリフレッシュ (CDI セグメントを含む)**を選択します。

![作成オプションが表示された「セグメントエクステンション作成エクスペリエンスの選択」メニュー。]({% image_buster /assets/img/segment/segment_extension_modal.png %}){: style="max-width:60%;"}

{: start="3"}
3. **このセグメントエクステンションのデータソースを選択**メニューで、**CDI データテーブル**を選択します。このメニューは、少なくとも1つの[接続ソース]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/connected_sources)を設定した後にのみ表示されます。

![CDI データテーブルオプションが表示された「このセグメントエクステンションのデータソースを選択」メニュー。]({% image_buster /assets/img/segment/cdi_data_tables.png %}){: style="max-width:60%;"}

{: start="4"}
4. 使用する接続を選択し、クエリを記述します。各接続には固有のデータテーブルセットがあります。開発チームは CDI 設定時に接続とデータテーブルを構成できます。
5. **ソースエクスプローラー**を選択すると、スキーマや利用可能な説明を含む、使用可能なデータテーブルを確認できます。

![スキーマや利用可能な説明を含む、使用可能なデータテーブルが表示されたソースエクスプローラー。]({% image_buster /assets/img/segment/connection_schema_with_descriptions.png %}){: style="max-width:100%;"}

{: start="6"}
6. [Braze SQL 構文]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments#step-2-write-your-sql)を使用して、セグメント用の SQL を記述します。すべての CDI セグメントエクステンションでは、選択カラムとして `external_user_id` を使用する必要があり、`external_user_id` はBrazeでユーザーに設定されたものと一致する必要があります。<br><br>
クエリ結果にBrazeに存在しないユーザーが含まれている場合、それらのユーザーは無視されます。Brazeは CDI セグメントエクステンションの出力に基づいて新しいユーザーを作成しません。

{% alert important %}
`external_user_id` は文字列値である必要があります。ソース ID が数値として格納されている場合（例：`client_id` が整数型の場合）、Brazeの `external_id` 型と一致するように [SQL で文字列にキャストしてください](https://www.w3schools.com/sql/func_sqlserver_cast.asp)。
{% endalert %}

{: start="7"}
7. Brazeセグメント内で[このセグメントエクステンションを使用]({{site.baseurl}}/user_guide/audience/segments/segment_extension#step-6-use-your-extension-in-a-segment)して、このオーディエンスにキャンペーンまたはキャンバスを送信します。

{% alert tip %}
セグメントエクステンションのプレビュー方法、セグメントエクステンションの管理方法、自動メンバーシップ更新の実行方法については、[SQL セグメントエクステンション]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments)を参照してください。
{% endalert %}

## 考慮事項 {#considerations}

- セグメントエクステンションは、1つの接続からのデータのみを参照でき、複数の接続からは参照できません。
- セグメントエクステンションは、データソースとして CDI データまたは Braze Snowflake（Currents）データのいずれかを使用できます。セグメントエクステンション内でデータソースを混在させることはできませんが、複数のセグメントエクステンションを作成してセグメント内で一緒に参照することができます。

## トラブルシューティング {#troubleshooting}

- クエリは、**クラウドデータ取り込み**ページで各接続同期に設定された最大実行時間に達するとタイムアウトする場合があります。許可される最大実行時間は60分です。
- SQLがデータウェアハウスに適した構文で記述されていることを確認してください。