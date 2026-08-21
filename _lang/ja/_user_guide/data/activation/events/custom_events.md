---
nav_title: カスタムイベント
article_title: カスタムイベント
page_order: 1
page_type: reference
description: "この記事では、カスタムイベントとプロパティ、セグメンテーション、使用法、キャンバスエントリプロパティ、関連する分析の表示場所などについて説明します。"
search_rank: 2
---

# [![Braze Learning コース]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/custom-events-and-attributes){: style="float:right;width:120px;border:0;" class="noimgborder"}カスタムイベント {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomcustom-events-and-attributes-stylefloatrightwidth120pxborder0-classnoimgbordercustom-events}

> この記事では、カスタムイベントとプロパティ、ユーザープロファイルのイベント履歴、関連するセグメンテーションフィルター、キャンバスエントリプロパティ、関連する分析などについて説明します。Brazeのイベント全般については、[イベント]({{site.baseurl}}/user_guide/data/activation/events)を参照してください。

カスタムイベントとは、ユーザーによって実行されたアクションまたはユーザーに関する更新です。カスタムイベントが記録されると、任意の数とタイプのフォローアップキャンペーンをトリガーできます。その後、[セグメンテーションフィルター](#segmentation-filters)を使用して、カスタムイベントの発生頻度や最終発生日時に基づいてユーザーをセグメント化できます。これにより、カスタムイベントは、アプリケーション内の高価値のユーザーインタラクションの追跡に最適です。

## ユースケース {#use-cases}

一般的なカスタムイベントのユースケースには、以下のようなものがあります。

{% multi_lang_include data_activation/custom_event_use_cases.md %}

## カスタムイベントの管理 {#managing-custom-events}

ダッシュボードで**データ設定** > **カスタムイベント**に移動して、カスタムイベントの管理、作成、またはブロックリスト登録を行うことができます。

### 重複するカスタム属性またはイベントのトラブルシューティング {#troubleshooting-duplicate-custom-attributes-or-events}

{% multi_lang_include data_activation/troubleshooting_duplicate_custom_data_entries.md %}

カスタムイベントの横にあるメニューを選択すると、以下のアクションを実行できます。

### ブロックリスト登録 {#blocklisting}

アクションメニューから個々のカスタムイベントをブロックリストに登録したり、最大100件のイベントを一括で選択してブロックリストに登録したりできます。

カスタムイベントをブロックした場合:

{% multi_lang_include data_activation/custom_event_block_effects.md %}

さらに、ブロックされたカスタムイベントが現在Brazeの他の領域でフィルターやトリガーによって参照されている場合、そのイベントを参照しているフィルターやトリガーのすべてのインスタンスが削除およびアーカイブされることを説明する警告モーダルが表示されます。

ブロックリスト登録とカスタムデータの削除の詳細については、[カスタムデータのブロックリスト登録]({{site.baseurl}}/user_guide/data/activation/custom_data/blocklist_custom_data)を参照してください。

### 説明の追加 {#adding-descriptions}

`Manage Events, Attributes, Purchases` の[ユーザー権限]({{site.baseurl}}/user_guide/administer/global/user_management/permissions)を持っている場合、カスタムイベントの作成後に説明を追加できます。カスタムイベントの**説明を編集**を選択し、チームへのメモなど、任意の内容を入力してください。

### タグの追加 {#adding-tags}

「Manage Events, Attributes, Purchases」の[ユーザー権限]({{site.baseurl}}/user_guide/administer/global/user_management/permissions)を持っている場合、カスタムイベントの作成後にタグを追加できます。追加したタグを使用して、イベントのリストをフィルタリングできます。

### データのエクスポート {#exporting-data}

カスタムイベントのリストをCSVファイルとしてエクスポートするには、ページ上部の**すべてエクスポート**を選択します。CSVファイルが生成され、ダウンロードリンクがメールで送信されます。

{% alert note %}
プロファイルに定義または保存できる**カスタムイベント**や**カスタム属性**の数に、ダッシュボード上の固定の上限はありません。実際の制限は、データの形状、取り込み量、およびワークスペースのパフォーマンスに依存します。非常に大規模なイベントや属性のカタログをトラッキングする予定がある場合は、モデリングとデータ管理（例えば、未使用データの[ブロックリスト登録]({{site.baseurl}}/user_guide/data/activation/custom_data/blocklist_custom_data)）についてBrazeアカウントチームにご相談ください。
{% endalert %}

## 使用状況レポートの表示 {#viewing-usage-reports}

使用状況レポートには、特定のカスタムイベントを使用しているすべてのキャンバス、キャンペーン、セグメントが一覧表示されます。このリストにはLiquidの使用は含まれません。

該当するカスタムイベントの横にあるチェックボックスを選択し、**使用状況レポートを表示**を選択することで、一度に最大100件の使用状況レポートを表示できます。

## カスタムイベントのログ記録 {#logging-custom-events}

カスタムイベントには追加の設定が必要です。カスタムイベントのログ記録に使用するメソッドや、プロパティや数量をカスタムイベントに追加する方法については、以下のプラットフォームのドキュメントを参照してください。

{% details プラットフォーム別のドキュメントを展開 %}

- [Android および FireOS]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=android)
- [iOS]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=swift)
- [Web]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=web)
- [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/analytics#logging-custom-events)
- [Unity]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=unity)
- [.NET MAUI（旧 Xamarin）]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics#tracking-custom-events)
- [Roku]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=roku)

{% enddetails %}

## カスタムイベントのストレージ {#custom-event-storage}

**ユーザープロファイル**に保存されるすべてのデータ（カスタムイベントのメタデータ（最初または最後の発生、合計カウント、30日間のX in Y）を含む）は、各プロファイルが<a href="/docs/user_archival#active-users">アクティブ</a> である限り、無期限に保持されます。

## ユーザーのイベント履歴を表示する {#view-a-users-event-history}

ユーザープロファイルの**イベント履歴**タブを使用して、そのユーザーの最近のカスタムイベントと購入を表示します。これにより、インテグレーションがイベントを正しく記録しているかどうかを確認し、ダッシュボードで直接ユーザーレベルの問題をトラブルシューティングできます。

ユーザーのイベント履歴を表示するには:

1. **オーディエンス** > **ユーザー検索**に移動し、ユーザーを選択してプロファイルを開きます。
2. **イベント履歴**タブを選択します。

このタブには、過去30日間のユーザーのカスタムイベントと購入が、最新のものから古いものの順に最大100件まで表示されます。

各イベントには以下の情報が含まれます:

- **イベントタイプ:** イベントがカスタムイベントか購入かを示します。
- **イベント名:** 記録されたイベント名です。
- **時刻:** イベントが発生した日時です。
- **プロパティ:** その発生に関するすべてのイベントプロパティがJSONとして表示されます。

一般的なユースケースには以下が含まれます:

- 開発中またはリリース後に、SDKまたはAPIインテグレーションが期待どおりにイベントを送信しているかどうかを確認する。
- ユーザーがイベントトリガーのキャンペーンやキャンバスにエントリしたかどうか、またはしなかった理由をトラブルシューティングする。
- データエクスポートを設定せずに、特定のユーザーのサポート問題を調査する。

{% alert note %}
**イベント履歴**タブを表示するには、イベントプロパティに個人データが含まれる可能性があるため、**ユーザー検索**、**PIIの表示**、および**ユーザーイベントプロパティの表示**のユーザー権限が必要です。詳細については、[会社のユーザー権限]({{site.baseurl}}/user_guide/administer/global/user_management/permissions)を参照してください。
{% endalert %}

## セグメンテーションフィルター {#segmentation-filters}

以下の表は、カスタムイベントによるユーザーのセグメンテーションに使用できるフィルターを示しています。

| セグメンテーションオプション | ドロップダウンフィルター | 入力オプション |
| ---------------------| --------------- | ------------- |
| カスタムイベントが **X回を超えて** 発生したかどうかを確認する | **MORE THAN** | **NUMBER** |
| カスタムイベントが **X回未満** 発生したかどうかを確認する | **LESS THAN** | **NUMBER** |
| カスタムイベントが **正確にX回** 発生したかどうかを確認する | **EXACTLY** | **NUMBER** |
| カスタムイベントが最後に **X日以降に** 発生したかどうかを確認する | **AFTER** | **TIME** |
| カスタムイベントが最後に **X日より前に** 発生したかどうかを確認する | **BEFORE** | **TIME** |
| カスタムイベントが最後に **X日以上前に** 発生したかどうかを確認する | **MORE THAN** | **NUMBER OF DAYS AGO**（正の数） |
| カスタムイベントが最後に **X日未満前に** 発生したかどうかを確認する | **LESS THAN** | **NUMBER OF DAYS AGO**（正の数） |
| カスタムイベントが **X回（最大50回）を超えて** 発生したかどうかを確認する | **MORE THAN** | 過去 **Y日間（Y = 1、3、7、14、21、30）** |
| カスタムイベントが **X回（最大50回）未満** 発生したかどうかを確認する | **LESS THAN** | 過去 **Y日間（Y = 1、3、7、14、21、30）** |
| カスタムイベントが **正確にX回（最大50回）** 発生したかどうかを確認する | **EXACTLY** | 過去 **Y日間（Y = 1、3、7、14、21、30）** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="セグメンテーションフィルター" }

## 分析 {#analytics}

Brazeは、カスタムイベントが発生した回数と、各ユーザーが最後にそのイベントを実行した時刻をセグメンテーション用に記録します。レポートの設定、フィルター、エクスポートオプションについては、[カスタムイベントレポート]({{site.baseurl}}/user_guide/analytics/reports/custom_events_report)を参照してください。

**カスタムイベントレポート**ページでは、各カスタムイベントの発生頻度を集計して確認できます。時系列に重ねて表示されるグレーの線は、キャンペーンが最後に送信された時刻を示しており、キャンペーンがカスタムイベントのアクティビティにどのような影響を与えたかを確認するのに役立ちます。

![ダッシュボードのカスタムイベントページに表示されるカスタムイベントのカウントグラフ。カスタムイベントのトレンドを示しています]({% image_buster /assets/img_archive/custom_event_analytics_example.png %} "custom_event_analytics_example.png")

また、**フィルター**を使用して、カスタムイベントを時間別、月間アクティブユーザー数（MAU）別、セグメント別、またはKPI計算式別に分類することもできます。

![カスタムイベントグラフのフィルター]({% image_buster /assets/img/custom_events_report_filters.png %}){: style="max-width:40%;"}

{% alert tip %}
[カスタム属性のインクリメント]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#custom-attribute-data-types)を使用すると、カスタムイベントと同様のユーザーアクションのカウンターを保持できます。ただし、カスタム属性データを時系列で表示することはできません。時系列で分析する必要のないユーザーアクションは、この方法で記録してください。
{% endalert %}

### カスタムイベント分析が表示されない理由 {#why-custom-events-analytics-arent-showing}

カスタムイベントデータを使用して作成されたセグメントでは、作成前の過去の履歴データを表示することはできません。

## カスタムイベントプロパティ {#custom-event-properties}

カスタムイベントプロパティは、イベントの特定の発生を記述するカスタムイベントのメタデータまたは属性です。これらのプロパティは、トリガー条件のさらなる絞り込み、メッセージングにおけるパーソナライゼーションの向上、コンバージョンのトラッキング、および生データエクスポートによるより高度な分析の生成に使用できます。

詳細については、[カスタムイベントプロパティ]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties)を参照してください。