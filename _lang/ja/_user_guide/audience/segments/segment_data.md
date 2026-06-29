---
nav_title: セグメントデータ
article_title: セグメントデータ
page_order: 4
page_type: reference
description: "このページでは、Brazeダッシュボードのセグメントセクションについて説明し、提供される統計の概要を紹介します。"
alias: /viewing_and_understanding_segment_data/
tool:
  - Segments
  - Reports

---
# セグメントデータ {#segment-data}

> このページでは、Brazeダッシュボードのセグメントセクションについて説明し、提供される統計の概要を紹介します。

## セグメントとメンバーシップに関するデータへのアクセス {#accessing-data-about-your-segments-and-membership}

Brazeダッシュボードの**Segments**ページには、すべてのSegmentsの概要が表示され、各Segmentの詳細データを確認できます。このページで、Segment名を検索して選択すると、データの編集と表示が可能です。Segmentの作成方法については、[Segmentを作成する]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment#creating-a-segment)をご覧ください。

![Segmentsページ]({% image_buster /assets/img_archive/segments.png %})

Segment名を選択すると、Segmentの統計とフィルターを表示したり、フィルターの追加や削除によってSegmentを編集したりできます。変更は必ず保存してください。

[Segmentの分析トラッキング]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking)を有効にすると、このSegmentのセッション、カスタムイベント、収益を時系列で表示できます。

![Segmentの分析トラッキングトグル]({% image_buster /assets/img_archive/A_Tracking_2.png %})

### セグメント統計 {#segment-statistics}

フィルターの追加や削除に応じてリアルタイムで更新される、以下のセグメント統計を確認できます。

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table aria-label="セグメント統計">
  <caption>セグメント統計</caption>
    <thead>
        <tr>
            <th>統計</th>
            <th>定義</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split">Total Users</td>
            <td class="no-split">アプリの合計ユーザー数です。</td>
        </tr>
        <tr>
            <td class="no-split">Selected Users</td>
            <td class="no-split">Segmentに含まれるユーザー数と、全ユーザー群に対する割合です。</td>
        </tr>
        <tr>
            <td class="no-split">LTV (Paying Users)</td>
            <td class="no-split">このSegmentのユーザーあたりの生涯価値（LTV）と、課金ユーザーあたりの生涯価値です。LTVは、生涯収益を生涯ユーザー数で割って算出されます。</td>
        </tr>
        <tr>
            <td class="no-split">Emailable (Opted-In)</td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Emailable' %} <a href="/docs/help/best_practices/spam_regulations#spam-regulationsspam regulations">スパム規制</a> のため、ダブルオプトインポリシーを実装し、最初の確認メール内のリンクをユーザーにクリックしてもらうことで、明示的なオプトインを求めることをお勧めします。より多くのユーザーにオプトインを促すには、<a href="/docs/user_guide/channels/email/subscriptions#segmenting-by-user-subscriptions">オプトインもオプトアウトもしていないユーザー</a> にメッセージをターゲティングできます。</td>
        </tr>
        <tr>
            <td class="no-split">Push Enabled (Opted-In)</td>
            <td class="no-split">Push Enabledは、少なくとも1つのプッシュトークンを持つユーザー数を指します。一部のユーザーは複数のプッシュトークンを持つ場合があります（例えば、iPhoneとiPadの両方を所有している場合）。そのため、このSegmentに送信されるプッシュ通知の数は「Push Enabled」のユーザー数を上回ることがあります。「Opted In」は、プッシュ通知を明示的にオプトインしたユーザー数を指します。プッシュを送信するには、ユーザーが常に明示的にオプトインしている必要があります。</td>
        </tr>
    </tbody>
</table>

### セグメントインサイト {#segment-insights}

ダッシュボードの[セグメントインサイト]({{site.baseurl}}/user_guide/audience/segments/segment_insights)ページにアクセスすると、事前に選択されたKPIのセットに基づいて、あるSegmentが別のSegmentと比較してどのようなパフォーマンスを示しているかを確認できます。

### メッセージングの使用状況 {#messaging-use}
**Messaging Use**セクションには、現在有効なCampaignsおよびCanvasesのうち、どのSegmentsをターゲットにしているかが表示されます。

### メンバーシップの履歴 {#historical-membership}

**Historical Membership**セクションには、Segmentのサイズが時間の経過とともにどのように変化したかが表示されます。ドロップダウンを使用して、日付範囲でSegmentメンバーシップをフィルタリングできます。

Segmentのメンバーシップとサイズの監視について詳しくは、[セグメントサイズの測定]({{site.baseurl}}/user_guide/audience/segments/measuring_segment_size)を参照してください。

### ユーザープレビュー {#user-preview}

Segmentのユーザー固有の詳細情報を表示するには、**User Data**をクリックし、**User Preview**を選択します。

このページでは、性別、年齢、セッション数、プッシュやメールにオプトインしているかどうかなど、さまざまなユーザー固有の属性を確認できます。

ワークスペースのサイズに対してSegmentが非常に小さい場合、ユーザープレビューでユーザーが0人と表示されることがあります。これは必ずしもSegmentにユーザーがいないことを意味するわけではありません。[正確な統計を計算]({{site.baseurl}}/user_guide/audience/segments/measuring_segment_size#statistics-for-segment-size)を実行して、Segmentの正確なサイズを確認してください。

![ユーザープレビュー]({% image_buster /assets/img_archive/user_preview.png %})

## Segment別のパフォーマンスデータの表示 {#viewing-performance-data-by-segment}

[クエリビルダーのレポートテンプレート]({{site.baseurl}}/user_guide/analytics/reports/query_builder/data_by_segments)を使用して、Campaigns、Canvases、バリアント、ステップのパフォーマンス指標をSegment別に分解できます。

## クエリビルダーを使用したセグメント分解レポートの作成 {#creating-a-segment-breakdown-report-using-query-builder}

[クエリビルダー]({{site.baseurl}}/user_guide/analytics/reports/query_builder)テンプレートからレポートを作成するには、**Query Builder**に移動し、以下の手順を実行します。

1. **Create SQL Query** > **Query Template**を選択します。
2. 「segment breakdowns」を含む指標を持つテンプレートでフィルタリングします。
3. 使用するテンプレートを選択します。
4. [変数](#variables)タブで、SQLテンプレートの変数を入力します。
5. （オプション）テンプレート内のSQLを直接編集します。
6. **Run Query**を選択します。結果がテーブルに表示されます。

## 変数 {#variables}

レポートを生成する前に、**Variables**タブに移動して、レポートビルダーテンプレートに必要な情報を入力します。必須変数はレポートによって異なります。

変数には以下が含まれます。

- **CampaignまたはCanvas：** 1つまたは複数のCampaignsやCanvasesを含めることができます（指定できるCampaignsやCanvasesの数に上限はありません）。CampaignsやCanvasesを指定しない場合、レポートには選択した期間のすべてのCampaignsまたはCanvasesが含まれます。
- **バリアント：** バリアントレベルの分解を提供するテンプレートを使用する場合、CampaignまたはCanvasを選択した後、そのCampaignまたはCanvas内のバリアントを選択できます。複数のバリアントを選択すると、結果はバリアント別にグループ化されます。
- **ステップ：** Canvasバリアントを選択した場合、キャンバスステップを選択できます。Canvasバリアントを先に選択しないと、ステップは選択できません。
- **期間：** データを取得する期間を指定します。期間を指定しない場合、デフォルトで過去30日間が適用されます。
- **製品名：** 購入データのレポートを実行する場合、データを取得する特定の製品を指定できます。
- **コンバージョンウィンドウ：** 収益および購入データを含むレポートでは常に必須です。メールの受信またはクリック後、Brazeが購入や収益を帰属させる日数です。
- **Segments：** データを分解するSegmentsを指定します。指定しない場合、レポートは分析トラッキングが有効になっているすべてのSegmentsに対して実行されます。
- **タグ：** **Variables**でタグを指定すると、特定のタグを持つすべてのCampaignsまたはCanvasesに対してレポートを実行できます。複数のタグを含めることができます。タグと特定のCampaignsまたはCanvasesの両方をレポートに追加した場合、レポートにはタグと指定されたCampaignsまたはCanvasesの両方のデータが含まれます。

## データの利用可能性 {#data-availability}

以下の両方の条件が満たされている期間のデータが利用可能です。

1. データを確認したいSegmentsに対して[セグメント分析トラッキング]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking)が有効になっている。
2. Segment別パフォーマンスデータ機能が有効になっている。

この機能が会社で有効になる前の期間のデータにはアクセスできません。例えば、Segment Aの分析トラッキングが10月1日に有効になり、この機能が会社で10月2日に有効になった場合、10月2日以降に指標を記録したCampaignsおよびCanvasesのSegment Aのデータのみを表示できます。

会社でこの機能が10月2日に有効になり、Segment Bの分析トラッキングが10月3日に有効になった場合、10月3日以降に指標を記録したCampaignsおよびCanvasesのSegment Bのデータのみを表示できます。