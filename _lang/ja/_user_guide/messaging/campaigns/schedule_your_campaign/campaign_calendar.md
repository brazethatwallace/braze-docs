---
nav_title: コンテンツカレンダー
article_title: コンテンツカレンダー
page_order: 4
tool: Campaigns
page_type: reference
description: "このリファレンスページでは、コンテンツカレンダーのコンポーネントについて説明します。"
---

# コンテンツカレンダー {#content-calendar}

> コンテンツカレンダーは、今後スケジュールされたキャンペーンの概要を一目で確認できます。

メッセージングデータを分析し、スケジュールされたキャンペーンを表示・管理できます。カレンダーを開くには、**コンテンツ** > **コンテンツカレンダー**を選択します。

## メッセージング分析 {#messaging-analytics}

メッセージング分析セクションには、最近のキャンペーンおよび今後スケジュールされたキャンペーンに関する2つのレポートが含まれています。

- **今後のメッセージタイプ:** 今後14日以内にスケジュールされたプッシュ、メール、アプリ内メッセージングキャンペーンの数。
- **送信済みメッセージ:** 過去14日間に送信および開封されたメッセージの数。

レポート内の特定の日のメッセージング分析を表示するには、その日にカーソルを合わせます。

![メッセージング分析内の「今後のメッセージタイプ」と「送信済みメッセージ」のグラフ。]({% image_buster /assets/img/campaign_calendar/content_calendar_messaging_analytics.png %})

データのコピーをダウンロードするには、<i class="fa-solid fa-bars" style="color: #2e7487;" aria-hidden="true" aria-label="チャートコンテキストメニューを開く"></i> **チャートコンテキストメニュー**を選択し、希望のファイル形式を選択します。

## 送信カレンダー {#send-calendar}

送信カレンダーには、当月のスケジュールされたキャンペーンが表示されます。キャンバス、アクションベースのキャンペーン、APIトリガーのキャンペーンは含まれません。

キャンペーンは**凡例**でタイプ別に色分けされています。

- 青はマルチチャネルキャンペーンを示します。
- 紫は多変量キャンペーンを示します。
- グレーは無効化されたキャンペーンを示します。

{% alert note %}
アプリ内メッセージは常にアクションベースであるため、送信カレンダーには表示されません。
{% endalert %}

<i class="fa-solid fa-chevron-left" style="color: #2e7487;" aria-hidden="true"></i> **前月を表示**または<i class="fa-solid fa-chevron-right" style="color: #2e7487;" aria-hidden="true"></i> **翌月を表示**を選択して月を変更できます。当月に戻るには、**今日**を選択します。

![当月のスケジュールされたすべてのキャンペーンを表示する送信カレンダー。]({% image_buster /assets/img/campaign_calendar/content_calendar_sends.png %})

カレンダーでキャンペーンを選択すると、キャンペーンの表示や変更ができます。詳細については、[キャンペーンの管理]({{site.baseurl}}/user_guide/messaging/campaigns/manage_campaigns)を参照してください。