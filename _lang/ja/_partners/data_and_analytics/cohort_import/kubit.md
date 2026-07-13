---
nav_title: Kubit
article_title: Kubit コホートインポート
description: "このリファレンス記事では、Kubitのコホートインポート機能について説明します。Kubitは、製品インサイトを即座に提供するノーコードのセルフサービス分析プラットフォームであり、KubitユーザーコホートをインポートしてBrazeメッセージングでターゲットにすることができます。"
page_type: partner
search_tag: Partner
---

# Kubit コホートインポート {#kubit-cohort-import}

> この記事では、[Kubit](https://kubit.ai/)からBrazeにユーザーコホートをインポートする方法を説明します。Kubitとその他の機能の統合についての詳細は、[Kubitのメイン記事]({{site.baseurl}}/partners/data_and_analytics/analytics/kubit)を参照してください。

## データインポートの統合 {#data-import-integration}

### ステップ1:Brazeデータインポートキーを取得する {#step-1-get-the-braze-data-import-key}

Brazeで**パートナー連携** > **テクノロジーパートナー**に移動し、**Kubit**を選択します。ここでRESTエンドポイントを確認し、Brazeデータインポートキーを生成できます。

生成後、新しいキーを作成するか、既存のキーを無効にできます。データインポートキーとRESTエンドポイントは、次のステップでKubitのダッシュボードでポストバックを設定する際に使用します。

![BrazeのKubitテクノロジーパートナーページ。]({% image_buster /assets/img/kubit/kubit.png %}){: style="max-width:90%;"}

### ステップ2:KubitでBrazeを設定する {#step-2-configure-braze-in-kubit}

Kubitサポート担当者に、BrazeデータインポートキーとBraze RESTエンドポイントを提供します。統合の設定は担当者側で行い、統合が有効になったら連絡があります。

### ステップ3:Brazeにコホートをインポートする {#step-3-import-cohorts-to-braze}

#### Kubitでコホートを作成する {#create-a-cohort-in-kubit}
Kubitで[コホートを作成](https://www.kubit.ai/doc/fundamentals#cohort)し、ターゲットユーザーの条件を定義します。<br><br>![ターゲットユーザーの条件が設定されたKubitコホートビルダー。]({% image_buster /assets/img/kubit/create_cohort.png %}){: style="max-width:80%;"}

#### ユーザーをBrazeにインポートする {#import-users-to-braze}
コホートを保存したら、Brazeにインポートしてセグメントで使用できます。これらのセグメントは、ターゲットを絞ったメールやプッシュキャンペーン、キャンバスの作成に利用できます。

これを行うには、既存のコホートに移動し、**Cohort Control**で**Import to Braze**を選択します。

![Import to Brazeが選択されたKubitのCohort Controlメニュー。]({% image_buster /assets/img/kubit/import_to_braze.png %}){: style="max-width:80%;"}

次に、希望するインポート頻度を選択します。ワンタイムインポートでは、今すぐ1回インポートできます。スケジュールインポートでは、毎日、毎週、または毎月の特定の時刻にインポートできます。各コホートに設定できるライブインポートスケジュールは1つだけです。

![Brazeインポートの頻度オプションが表示されたKubitインポートスケジュール設定。]({% image_buster /assets/img/kubit/import_schedule.png %}){: style="max-width:40%;"}

{% alert important %}
Braze内に既に存在するユーザーのみがコホートに追加または削除されます。コホートインポートではBrazeに新しいユーザーは作成されません。
{% endalert %}

#### インポートステータスを確認する {#verify-import-status}
インポートが完了すると、インポートスケジュールで指定された受信者にメール通知が送信されます。また、Kubitの**Schedule**でコホートのインポートステータスを確認することもできます。スケジュール履歴には、すべてのインポート実行時間、結果、およびBrazeにインポートされたコホート内のユーザー総数が表示されます。<br><br>![インポート実行時間、結果、インポートされたユーザー数が表示されたKubitスケジュール履歴。]({% image_buster /assets/img/kubit/import_history.png %})<br><br>そのインポートスケジュールの**Import to Braze**アイコンをクリックすることで、手動でインポートをトリガーできます。

### ステップ4:Kubitコホートでセグメントを作成する {#step-4-create-braze-segments-with-kubit-cohorts}
Brazeにコホートをインポートしたら、それらをフィルターとして使用してセグメントを作成し、キャンペーンやキャンバスに含めることができます。[Brazeセグメントの作成方法]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment#step-4-add-filters-to-your-segment)の詳細については、セグメントのドキュメントを参照してください。

![Brazeセグメントビルダーで、ユーザー属性「Kubitコホート」が「includes_value」に設定され、利用可能なコホートのリストが表示されている画面。]({% image_buster /assets/img/kubit/segment_with_kubit_cohorts.png %}){: style="max-width:70%;"}

## ユーザーマッチング {#user-matching}

識別されたユーザーは、`external_id`または`alias`のどちらかで照合できます。匿名ユーザーは、`device_id`で照合できます。元々匿名ユーザーとして作成された識別済みユーザーは、`device_id`では識別できず、`external_id`または`alias`で識別する必要があります。