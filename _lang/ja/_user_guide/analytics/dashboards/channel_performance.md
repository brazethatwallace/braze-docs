---
nav_title: チャネルパフォーマンス
article_title: チャネルパフォーマンスダッシュボード
page_order: 2
page_type: reference
description: "このリファレンス記事では、キャンペーンとキャンバスの両方にわたるチャネル全体のパフォーマンス指標を表示できるチャネルパフォーマンスダッシュボードについて説明します。"
tool:
  - Reports
toc_headers: h2
---

# チャネルパフォーマンスダッシュボード {#channel-performance-dashboards}

> チャネルパフォーマンスダッシュボードは、キャンペーンとキャンバスの両方から、チャネル全体の集計パフォーマンス指標を表示します。これらのダッシュボードは現在、メール、プッシュ、SMSで利用できます。

## ダッシュボード {#dashboards}

タブを選択して、利用可能なチャネルパフォーマンスダッシュボードの詳細を確認してください。

{% tabs %}
{% tab メールのパフォーマンス %}

### メールのパフォーマンスダッシュボード {#email-performance-dashboard}

メールのパフォーマンスダッシュボードを表示するには、**Analytics** > **Email Performance** に移動し、データを表示する期間の日付範囲を選択します。日付範囲は最大1年前まで設定できます。

![過去30日間のメールチャネルエンゲージメントを表示するメールのパフォーマンスダッシュボード。]({% image_buster /assets/img_archive/email_performance_dashboard_1.png %})

![335,630件の送信があり、1日あたり平均11,187.667件のメールキャンペーンの例。]({% image_buster /assets/img_archive/email_performance_dashboard_2.png %}){: style="max-width:40%;float:right;margin-left:15px;border:none;"}

#### 指標の計算方法 {#how-metrics-are-calculated}

{% multi_lang_include analytics/channel_performance_how_metrics_calculated.md channel="email" %}

| 指標 | タイプ | 計算方法 |
| --- | --- | ---- |
| 送信数 | カウント | 日付範囲内の各日の送信数の合計 |
| 配信率 | 率 | （日付範囲内の各日の配信数の合計）/（日付範囲内の各日の送信数の合計） |
| バウンス率 | 率 | （日付範囲内の各日のバウンス数の合計）/（日付範囲内の各日の送信数の合計） |
| 配信停止率 | 率 | （日付範囲内の各日のユニーク配信停止数の合計）/（日付範囲の配信数の合計）<br><br>ここではユニーク配信停止数を使用しており、キャンペーン分析、概要、レポートビルダーでも同様に使用されています。これらの配信停止は、すべてのソース（REST API、CSVインポート、メール、リスト配信停止など）にわたって記録されます。キャンペーンおよびキャンバス分析における配信停止率は、Brazeが配信したメールの配信停止リンクのクリックによって発生した配信停止です。 |
| ユニーク開封率 | 率 | （日付範囲内の各日のユニーク開封数の合計）/（日付範囲の配信数の合計） |
| その他の開封率 | 率 | （日付範囲内の各日のその他の開封数の合計）/（日付範囲の配信数の合計）<br><br>その他の開封には、マシン開封として識別されていないメール（ユーザーがメールを開封した場合など）が含まれます。この指標はユニークではなく、合計開封数のサブ指標です。 |
| ユニーククリック率 | 率 | （日付範囲内の各日のユニーククリック数の合計）/（日付範囲の配信数の合計） |
| ユニーク開封後クリック率 | 率 | （日付範囲内の各日のユニーククリック数の合計）/（日付範囲内の各日のユニーク開封数の合計） |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="指標の計算方法" }

{% endtab %}
{% tab メールインサイト %}

### メールインサイトダッシュボード {#email-insights-dashboard}

メールインサイトダッシュボードは、顧客がメールとどこで、いつやり取りしているかを追跡します。これらのレポートは、メールを最適化してエンゲージメントを高めるための詳細なデータを提供します。メールインサイトダッシュボードには、最大過去6か月分のデータが含まれます。ダッシュボードにアクセスするには、**Analytics** > **Email Performance** > **Email Insights** に移動します。

#### デバイス別エンゲージメント {#engagement-by-device}

**デバイス別エンゲージメント**レポートは、ユーザーがメールとのやり取りに使用しているデバイスの内訳を提供します。このデータは、モバイル、デスクトップ、タブレット、その他のデバイスタイプにわたるメールエンゲージメントを追跡します。このデータは、ユーザーのデバイスから渡されるユーザーエージェント文字列に基づいています。

{% alert note %}
CDNとしてCloudFrontを使用している場合は、ユーザーのユーザーエージェントがメールサービスプロバイダー (ESP) に渡されていることを確認してください。そうしないと、すべてのユーザーエージェントが「Amazon Cloudfront」になります。
{% endalert %}

「その他」カテゴリには、デスクトップ、モバイル、またはタブレットとして識別できないユーザーエージェント文字列が含まれます。たとえば、テレビ、車、ゲーム機、OTT（オーバー・ザ・トップまたはストリーミング）などが該当します。null値や空の値が含まれる場合もあります。

この「その他」カテゴリの内容をより詳しく理解するには、以下のいずれかのオプションを使用してユーザーエージェントを抽出できます。

1. [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents)を使用すると、ユーザーのデバイスから取得された正確なユーザーエージェント文字列が送信されます。
2. [クエリビルダー]({{site.baseurl}}/user_guide/analytics/reports/query_builder)を活用してSQLを使用するか、[AIクエリビルダー]({{site.baseurl}}/user_guide/analytics/reports/query_builder#generating-sql-with-the-ai-query-builder)を使用してユーザーエージェントを表示します。

![モバイル、デスクトップ、タブレット、その他のデバイスのクリック数を表示するデバイス別エンゲージメントレポート。最も多くのクリック数はモバイルデバイスで発生しています。]({% image_buster /assets/img/engagement_by_device_type.png %}){: style="max-width:70%;"}

メール開封については、BrazeはGoogle Image Proxy、Apple Image Proxy、Yahoo Mail Proxyを分離します。これらのサービスは、メールが受信者に配信される前に、メール内のすべての埋め込み画像をキャッシュして読み込みます。その結果、受信者のサーバーではなくメールボックスプロバイダーのサーバーからメール開封がトリガーされ、メール開封数が膨らむ可能性があります。これらのサービスは、画像読み込み時のプライバシー、セキュリティ、パフォーマンス、効率性を向上させることを目的としています。また、これらのプロキシサービスはユーザーエージェントをマスクするため、受信者からの実際の開封が含まれる場合もあり、Brazeはユーザーエージェントを使用してプロキシデータを分類します。

![モバイル、デスクトップ、タブレット、Apple Privacy Proxy、Google Image Proxy、Yahoo Mail Proxy、その他の開封数を表示するデバイス別エンゲージメントレポート。最も多くの開封数はモバイルデバイスで発生しています。]({% image_buster /assets/img/engagement_by_device_type_proxy.png %}){: style="max-width:70%;"}

#### メールボックスプロバイダー別エンゲージメント {#engagement-by-mailbox-provider}

**メールボックスプロバイダー別エンゲージメント**レポートは、クリック数または開封数に貢献している上位のメールボックスプロバイダーを表示します。特定の主要メールボックスプロバイダーをクリックして、特定の受信ドメインの詳細を確認できます。たとえば、このレポートでMicrosoftが上位のメールボックスプロバイダー指標の1つとして表示されている場合、「outlook.com」、「hotmail.com」、「live.com」などの受信ドメインの詳細をさらに表示できます。

![Google、Apple iCloud、Yahoo、Microsoft、Mail.Ru Groupとそれぞれのクリック数を表示するメールボックスプロバイダー別エンゲージメントレポートの例。]({% image_buster /assets/img_archive/mailbox_provider_time_engagement.png %}){: style="max-width:70%;"}

#### エンゲージメントの時間帯 {#time-of-engagement}

**エンゲージメントの時間帯**レポートは、ユーザーがいつメールとやり取りしているかのデータを表示します。これにより、どの曜日や時間帯に顧客からのエンゲージメントが最も高いかなどの疑問に答えることができます。これらのインサイトを活用して、メッセージを送信する最適な日や時間を試し、より高いエンゲージメントを促進できます。これらの時間は会社のタイムゾーンに基づいています。

**曜日別**エンゲージメントレポートは、曜日ごとの開封数またはクリック数の内訳を表示します。

![月曜日と水曜日に最も多くのクリック数がある曜日別エンゲージメントレポートの例。]({% image_buster /assets/img_archive/time_engagement.png %})

**時間帯別**エンゲージメントレポートは、24時間の時間枠内の各時間ごとの開封数またはクリック数の内訳を表示します。

![午前0時から午後11時までの開封数またはクリック数を表示する時間帯別エンゲージメントレポートの例。]({% image_buster /assets/img_archive/time_engagement_day.png %})

メールの分析の詳細については、[メールレポート]({{site.baseurl}}/user_guide/channels/email/reporting)をご確認ください。

{% endtab %}
{% tab SMSパフォーマンス %}

### SMSパフォーマンスダッシュボード {#sms-performance-dashboard}

SMSパフォーマンスダッシュボードを使用するには、**Analytics** > **SMS Performance** に移動し、データを表示する期間の日付範囲を選択します。日付範囲は最大1年前まで設定できます。

![335,630件の送信があり、1日あたり平均11,187.667件のSMSキャンペーンの例。]({% image_buster /assets/img_archive/email_performance_dashboard_2.png %}){: style="max-width:40%;float:right;margin-left:15px;border:none;"}

#### 指標の計算方法

{% multi_lang_include analytics/channel_performance_how_metrics_calculated.md channel="SMS" %}

| 指標 | タイプ | 計算方法 |
| --- | --- | ---- |
| 送信数 | カウント | 日付範囲内の各日の送信数の合計 |
| 確認済み配信率 | 率 | （日付範囲内の各日の配信数の合計）/（日付範囲内の各日の送信数の合計） |
| 配信失敗率 | 率 | （日付範囲内の各日の失敗数の合計）/（日付範囲内の各日の送信数の合計） |
| 拒否率 | 率 | （日付範囲内の各日の拒否数の合計）/（日付範囲内の各日の送信数の合計） |
| クリック率 | 率 | （日付範囲内の各日のクリック数の合計）/（日付範囲内の各日の配信数の合計） |
| 合計オプトイン数 | 率 | 日付範囲内の各日の受信メッセージオプトイン数の合計 |
| 合計オプトアウト数 | 率 | 日付範囲内の各日の受信メッセージオプトアウト数の合計 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="指標の計算方法" }

{% endtab %}
{% tab プッシュパフォーマンス %}

### プッシュパフォーマンスダッシュボード {#push-performance-dashboard}

**プッシュパフォーマンス**ダッシュボードは、プッシュエンゲージメントのチャネルレベルの単一ビューを提供します。送信数、バウンス数、配信数、直接開封率、影響開封率、合計開封率を設定可能な時間枠で確認できます。個別のキャンペーンやキャンバスからデータを集計することなく、プッシュチャネル全体の健全性を把握するために使用します。

ダッシュボードを開くには、**Analytics** > **Dashboard Builder** に移動し、**Push Channel Dashboard** を選択します。日付範囲は最大1年前まで設定できます。

![6,300万件以上の送信があるプッシュキャンペーンの例。]({% image_buster /assets/img_archive/push_performance_dashboard.png %})

#### 指標の計算方法

{% multi_lang_include analytics/channel_performance_how_metrics_calculated.md channel="push" %}

| 指標 | タイプ | 計算方法 |
| --- | --- | ---- |
| 送信数 | カウント | 日付範囲内の各日の送信数の合計 |
| バウンス率 | 率 | （日付範囲内の各日のバウンス数の合計）/（日付範囲内の各日の送信数の合計） |
| 配信率 | 率 | （日付範囲内の各日の配信数の合計）/（日付範囲内の各日の送信数の合計） |
| 直接開封率 | 率 | （日付範囲内の各日の直接開封数の合計）/（日付範囲内の各日の配信数の合計） |
| 影響開封率 | 率 | （日付範囲内の各日の影響開封数の合計）/（日付範囲内の各日の配信数の合計） |
| 合計開封率 | 率 | （日付範囲内の各日の合計開封数の合計）/（日付範囲内の各日の配信数の合計）<br><br>合計開封数には、直接開封数と影響開封数の両方が含まれます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="指標の計算方法" }

{% endtab %}
{% endtabs %}

## ダッシュボードフィルター {#dashboard-filters}

以下のフィルターオプションを使用して、ダッシュボードのデータをフィルタリングできます。

- **タグ:** タグを1つ選択します。適用すると、ダッシュボードには選択したタグの指標のみが表示されます。
- **プラットフォーム:**（プッシュパフォーマンスダッシュボードのみ）プッシュプラットフォームを選択します。**All Push**、**Android**、**iOS**、**Mobile combined**、**Kindle**、**Web** などがあります。適用すると、ダッシュボードには選択したプラットフォームの指標のみが表示されます。
- **キャンバス:** 最大10個のキャンバスを選択します。適用すると、ダッシュボードには選択したキャンバスの指標のみが表示されます。タグフィルターを先に選択した場合、キャンバスフィルターのオプションには選択したタグを持つキャンバスのみが表示されます。
- **キャンペーン:** 最大10個のキャンペーンを選択します。適用すると、ダッシュボードには選択したキャンペーンの指標のみが表示されます。タグフィルターを先に選択した場合、キャンペーンフィルターのオプションには選択したタグを持つキャンペーンのみが表示されます。

![タグとフィルタリングするキャンバスのリストを選択できるチャネルパフォーマンスダッシュボードのフィルターオプション。]({% image_buster /assets/img_archive/dashboard_filters.png %})

## 期間の比較 {#comparing-time-periods}

チャネルパフォーマンスダッシュボードは、日付範囲で選択した期間を、同じ日数の前の期間と自動的に比較します。たとえば、ダッシュボードで日付範囲として「過去7日間」を選択した場合、前期間との比較では、過去7日間の指標とその前の7日間を比較します。カスタム日付範囲（たとえば5月10日から5月15日の6日間分のデータ）を選択した場合、ダッシュボードはその期間の指標を5月4日から5月9日の指標と比較します。

比較は、前期間と現在の期間の変化率であり、2つの期間の差を前期間の指標で割って計算されます。

### 合計数と率の変化を表示する {#viewing-changes-in-total-counts-and-rates}

**Show Change in Totals**（2つの期間間の合計数（配信されたメール数など）を比較）と **Show Change in Rates**（率（配信率など）を比較）を切り替えることができます。

![チャネルパフォーマンスダッシュボードの合計の変化または率の変化の表示を切り替えるラジオボタン。]({% image_buster /assets/img_archive/email_performance_dashboard_3.png %}){: style="max-width:60%"}

## よくある質問 {#frequently-asked-questions}

### ダッシュボードに空の値が表示されるのはなぜですか？ {#why-is-my-dashboard-displaying-empty-values}

指標に空の値が表示されるシナリオはいくつかあります。

- 選択した日付範囲で、Brazeがその特定の指標にゼロを記録した。
- 選択した日付範囲中にメッセージを送信していない。
- 選択した日付範囲で開封、クリック、配信停止などの指標はあったが、配信や送信がなかった。この場合、Brazeは率の指標を計算しません。

より多くの指標を表示するには、日付範囲を拡大してみてください。

### メールダッシュボードでその他の開封数がユニーク開封数より多いのはなぜですか？ {#why-does-my-email-dashboard-display-more-other-opens-than-unique-opens}

*ユニーク開封数*の指標では、Brazeは特定のユーザーによる重複開封（*マシン開封*または*その他の開封*を含む）を重複排除し、ユーザーが複数回開封しても1つの*ユニーク開封*のみがカウントされます。*その他の開封*では、Brazeは重複排除を行いません。

<!---Temporarily hidden until functionality is added

## Empty values in your data {#empty-values-in-your-data}

#### If a metric displays "0%" or "0" {#if-a-metric-displays-0-or-0}

This means Braze recorded zero for that particular metric during the time frame you've selected.

#### If a metric displays "N/A" {#if-a-metric-displays-na}

This means that while Braze recorded positive counts for a particular metric for the time frame you've selected, the denominator for the rate calculation (either sends or deliveries in most cases) was zero. This can occur when emails are sent out on one day and opens and clicks are recorded the following days if your selected time frame does not include the date the messages were sent.

#### If a metric displays "--" {#if-a-metric-displays}

This means Braze hasn't recorded any data for that metric during the time you selected. If you haven't set up or sent any emails yet, learn more about how to do so in our dedicated [Email]({{site.baseurl}}/user_guide/channels/email) section.

--->