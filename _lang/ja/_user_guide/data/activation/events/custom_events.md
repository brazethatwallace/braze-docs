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

カスタムイベントとは、ユーザーによって実行されたアクションまたはユーザーに関する更新です。カスタムイベントがログに記録されると、任意の数とタイプのフォローアップキャンペーンをトリガーできます。その後、[セグメンテーションフィルター](#segmentation-filters)を使用して、カスタムイベントの発生頻度や最終発生日時に基づいてユーザーをセグメント化できます。これにより、カスタムイベントは、アプリケーション内の高価値のユーザーインタラクションの追跡に最適です。

## ユースケース {#use-cases}

一般的なカスタムイベントのユースケースをいくつか示します。

- [アクションベースの配信]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery)を使用したカスタムイベントに基づくキャンペーンまたはキャンバスのトリガー
- ユーザーがカスタムイベントを実行した回数、イベントが最後に発生した時刻などに基づくユーザーのセグメント化
- ダッシュボードの[カスタムイベント分析](#analytics)を使用した、各イベントの発生頻度の集計表示
- [ファネル]({{site.baseurl}}/user_guide/analytics/reports/funnel_reports#step-2-select-events-for-funnel-steps)および[リテンション]({{site.baseurl}}/user_guide/analytics/reports/retention_reports)レポートを使用した追加の分析
- [永続的なエントリプロパティ]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties/canvas_persistent_entry_properties)を活用し、キャンバスステップで顧客イベントのメタデータをパーソナライゼーションに使用
- [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents)を使用したより高度な分析の生成
- [離脱条件]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/exit_criteria)を設定して、ユーザーがキャンバスから離脱するタイミングを定義

## カスタムイベントの管理 {#managing-custom-events}

ダッシュボードで**データ設定** > **カスタムイベント**に移動して、カスタムイベントの管理、作成、またはブロックリスト登録を行えます。

カスタムイベントの横にあるメニューを選択すると、以下のアクションを実行できます。

### ブロックリスト登録 {#blocklisting}

アクションメニューから個々のカスタムイベントをブロックリストに登録したり、最大100件のイベントを一括で選択してブロックリストに登録したりできます。

カスタムイベントをブロックすると、以下のようになります。

- そのイベントの今後のデータは収集されません。
- そのイベントのブロックが解除されない限り、既存のデータは利用できません。
- そのイベントはフィルターやグラフに表示されません。

さらに、ブロックされたカスタムイベントがBrazeの他の領域でフィルターやトリガーによって現在参照されている場合、そのイベントを参照しているフィルターやトリガーのすべてのインスタンスが削除およびアーカイブされることを説明する警告モーダルが表示されます。

カスタムデータのブロックリスト登録と削除の詳細については、[カスタムデータのブロックリスト登録]({{site.baseurl}}/user_guide/data/activation/custom_data/blocklist_custom_data)を参照してください。

### 説明の追加 {#adding-descriptions}

`Manage Events, Attributes, Purchases`の[ユーザー権限]({{site.baseurl}}/user_guide/administer/global/user_management/permissions)がある場合、カスタムイベントの作成後に説明を追加できます。カスタムイベントの**説明を編集**を選択し、チームへのメモなど任意の内容を入力してください。

### タグの追加 {#adding-tags}

「Manage Events, Attributes, Purchases」の[ユーザー権限]({{site.baseurl}}/user_guide/administer/global/user_management/permissions)がある場合、カスタムイベントの作成後にタグを追加できます。タグはイベントリストのフィルタリングに使用できます。

### データのエクスポート {#exporting-data}

カスタムイベントのリストをCSVファイルとしてエクスポートするには、ページ上部の**すべてエクスポート**を選択します。CSVファイルが生成され、ダウンロードリンクがメールで送信されます。

{% alert note %}
ダッシュボードには、プロファイルに定義または保存できる**カスタムイベント**や**カスタム属性**の数に固定の上限はありません。実際の制限は、データの形状、取り込み量、ワークスペースのパフォーマンスに依存します。非常に多くのイベントや属性を追跡する予定がある場合は、Brazeアカウントチームにモデリングとデータ管理（例えば、未使用データの[ブロックリスト登録]({{site.baseurl}}/user_guide/data/activation/custom_data/blocklist_custom_data)）についてご相談ください。
{% endalert %}

## 使用状況レポートの表示 {#viewing-usage-reports}

使用状況レポートには、特定のカスタムイベントを使用しているすべてのキャンバス、キャンペーン、セグメントが一覧表示されます。このリストにはLiquidの使用は含まれません。

対象のカスタムイベントの横にあるチェックボックスを選択し、**使用状況レポートを表示**を選択すると、一度に最大100件の使用状況レポートを表示できます。

## カスタムイベントの記録 {#logging-custom-events}

カスタムイベントには追加のセットアップが必要です。以下のプラットフォーム別ドキュメントを参照して、カスタムイベントの記録に使用するメソッドや、プロパティと数量の追加方法をご確認ください。

{% details プラットフォーム別のドキュメントを展開 %}

- [Android and FireOS]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=android)
- [iOS]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=swift)
- [Web]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=web)
- [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/analytics#logging-custom-events)
- [Unity]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=unity)
- [.NET MAUI (formerly Xamarin)]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics#tracking-custom-events)
- [Roku]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=roku)

{% enddetails %}

## カスタムイベントの保存 {#custom-event-storage}

**ユーザープロファイル**に保存されるすべてのデータ（カスタムイベントのメタデータ（初回または最終発生日時、合計回数、30日間のX in Y）を含む）は、各プロファイルが[アクティブ]({{site.baseurl}}/user_archival#active-users)である限り無期限に保持されます。

## ユーザーのイベント履歴の表示 {#view-a-users-event-history}

{% alert important %}
イベント履歴は現在、早期アクセス段階です。参加をご希望の場合は、Brazeアカウントマネージャーにお問い合わせください。
{% endalert %}

ユーザープロファイルの**イベント履歴**タブを使用して、そのユーザーの最近のカスタムイベントと購入を確認できます。これにより、インテグレーションがイベントを正しく記録しているかどうかを確認し、ダッシュボード上で直接ユーザーレベルの問題をトラブルシューティングできます。

ユーザーのイベント履歴を表示するには:

1. **オーディエンス** > **ユーザーを検索**に移動し、ユーザーを選択してプロファイルを開きます。
2. **イベント履歴**タブを選択します。

このタブには、過去30日間のユーザーのカスタムイベントと購入が、最新のものから順に最大100件表示されます。

各イベントには以下の情報が含まれます。

- **イベントタイプ:** イベントがカスタムイベントか購入かを示します。
- **イベント名:** 記録されたイベント名です。
- **時刻:** イベントが発生した日時です。
- **プロパティ:** その発生のイベントプロパティの全体がJSONとして表示されます。

一般的なユースケースには以下が含まれます。

- 開発中またはリリース後に、SDKまたはAPIインテグレーションが期待どおりにイベントを送信しているかどうかを確認する。
- ユーザーがイベントトリガーのキャンペーンまたはキャンバスにエントリしたかどうか、またはしなかった理由をトラブルシューティングする。
- データエクスポートを設定せずに、特定のユーザーのサポート問題を調査する。

{% alert note %}
**イベント履歴**タブの表示には、イベントプロパティに個人データが含まれる可能性があるため、**ユーザーを検索**、**PIIの表示**、および**ユーザーイベントプロパティの表示**のユーザー権限が必要です。詳しくは、[会社のユーザー権限]({{site.baseurl}}/user_guide/administer/global/user_management/permissions)を参照してください。
{% endalert %}

## セグメンテーションフィルター {#segmentation-filters}

以下の表は、カスタムイベントに基づいてユーザーをセグメント化するために使用できるフィルターを示しています。

| セグメンテーションオプション | ドロップダウンフィルター | 入力オプション |
| ---------------------| --------------- | ------------- |
| カスタムイベントが**X回を超えて**発生したかどうかを確認する | **MORE THAN** | **NUMBER** |
| カスタムイベントが**X回未満**発生したかどうかを確認する | **LESS THAN** | **NUMBER** |
| カスタムイベントが**正確にX回**発生したかどうかを確認する | **EXACTLY** | **NUMBER** |
| カスタムイベントが**X日以降に**最後に発生したかどうかを確認する | **AFTER** | **TIME** |
| カスタムイベントが**X日より前に**最後に発生したかどうかを確認する | **BEFORE** | **TIME** |
| カスタムイベントが**X日以上前に**最後に発生したかどうかを確認する | **MORE THAN** | **NUMBER OF DAYS AGO**（正の数） |
| カスタムイベントが**X日以内に**最後に発生したかどうかを確認する | **LESS THAN** | **NUMBER OF DAYS AGO**（正の数） |
| カスタムイベントが**X回（最大50回）を超えて**発生したかどうかを確認する | **MORE THAN** | 過去**Y日間（Y = 1,3,7,14,21,30）** |
| カスタムイベントが**X回（最大50回）未満**発生したかどうかを確認する | **LESS THAN** | 過去**Y日間（Y = 1,3,7,14,21,30）** |
| カスタムイベントが**正確にX回（最大50回）**発生したかどうかを確認する | **EXACTLY** | 過去**Y日間（Y = 1,3,7,14,21,30）** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="セグメンテーションフィルター" }

## 分析 {#analytics}

Brazeは、各ユーザーについてカスタムイベントの発生回数と最終実行日時を記録し、セグメンテーションに活用します。これらの分析は、**Analytics** > **カスタムイベントレポート**に移動して確認できます。

ダッシュボードの**カスタムイベントレポート**ページでは、各カスタムイベントの発生頻度を集計で表示できます。時系列に重ねて表示されるグレーの線は、キャンペーンが最後に送信された日時を示しており、キャンペーンがカスタムイベントのアクティビティにどのような影響を与えたかを確認するのに役立ちます。

![ダッシュボードのカスタムイベントページにあるカスタムイベント数グラフ。カスタムイベントのトレンドを表示しています]({% image_buster /assets/img_archive/custom_event_analytics_example.png %} "custom_event_analytics_example.png")

**フィルター**を使用して、カスタムイベントを時間別、月間アクティブユーザー数（MAU）別、セグメント別、またはKPI計算式別に分類することもできます。

![カスタムイベントグラフのフィルター]({% image_buster /assets/img/custom_events_report_filters.png %}){: style="max-width:40%;"}

{% alert tip %}
[カスタム属性のインクリメント]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes#integers)を使用すると、カスタムイベントと同様にユーザーアクションのカウンターを保持できます。ただし、カスタム属性データを時系列で表示することはできません。時系列で分析する必要のないユーザーアクションは、この方法で記録してください。
{% endalert %}

### カスタムイベント分析が表示されない理由 {#why-custom-events-analytics-arent-showing}

カスタムイベントデータで作成されたセグメントは、作成前の過去の履歴データを表示できません。

## カスタムイベントプロパティ {#custom-event-properties}

カスタムイベントプロパティは、イベントの特定の発生を記述するカスタムイベントのメタデータまたは属性です。これらのプロパティは、トリガー条件のさらなる絞り込み、メッセージングにおけるパーソナライゼーションの向上、コンバージョンのトラッキング、および生データエクスポートによるより高度な分析の生成に使用できます。

詳しくは、[カスタムイベントプロパティ]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties)を参照してください。