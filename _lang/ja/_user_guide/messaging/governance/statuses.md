---
nav_title: ステータス
article_title: ステータス
page_order: 5
description: "CampaignおよびCanvasのステータスと、ダッシュボードでの使用方法について説明します。"
tool:
    - Campaigns
    - Canvas
---

# CampaignとCanvasのステータス {#campaign-and-canvas-statuses}

> CampaignおよびCanvasのステータスと、ダッシュボードでの使用方法について説明します。

## ステータスでフィルタリングする {#filtering-by-status}

CampaignまたはCanvasをステータスでフィルタリングするには、**すべてのステータス**を選択し、ステータスを選びます。

![Brazeダッシュボードの「すべてのステータス」ドロップダウン。]({% image_buster /assets/img/messaging_fundamentals/filter-by-status.png %}){: style="max-width:70%;"}

## ステータスを変更する {#changing-the-status}

CampaignまたはCanvasのステータスを変更するには、<i class="fas fa-ellipsis-vertical"></i>メニューを選択し、ステータスを選びます。

![Brazeダッシュボードに表示されたCanvasの一覧。1つのCanvasのメニューが開いている状態。]({% image_buster /assets/img/messaging_fundamentals/change-status.png %})

## 利用可能なステータス {#available-statuses}

CampaignおよびCanvasで利用可能なステータスは以下のとおりです。

| ステータス | 説明 |
| --- | --- |
| アクティブ | アクティブなCampaignおよびCanvasは送信処理中です。デフォルトでは、それぞれのページにアクティブなCampaignおよびCanvasが表示されます。 |
| 下書き | CampaignおよびCanvasの下書きは保存されていますが、起動されていません。編集を続けて送信を開始するには、Brazeダッシュボードで**メッセージング**に移動し、**Canvas**または**Campaigns**を選択して下書きを選びます。 |
| アーカイブ | アーカイブされたCampaignおよびCanvasは、送信が終了したメッセージです。これらのCampaignおよびCanvasは、[**ホーム**]({{site.baseurl}}/user_guide/analytics/dashboards/home)ページおよび[**収益**]({{site.baseurl}}/user_guide/analytics/reports/revenue_report)ページの統計グラフからも削除されます。|
| 停止済み | 停止済みのCampaignおよびCanvasは一時停止されていますが、引き続き編集できます。Canvasを再開するには、Canvasビルダーの**Summary**ステップに移動し、**Resume Canvas**を選択します。Campaignの場合は、<i class="fas fa-ellipsis-vertical"></i>メニューを選択し、**Resume**を選びます。詳細については、[停止済みCanvasの動作](#stopped-canvas-behavior)を参照してください。 |
| アイドル | CampaignまたはCanvasがメッセージを送信しなくなると、Brazeはアイドルステータスを割り当て、CampaignおよびCanvasの一覧の整理と管理を支援します。自動的に停止されるCampaignまたはCanvasと、関連する停止日を確認できます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="利用可能なステータス" }

### 停止済みCanvasの動作 {#stopped-canvas-behavior}

Canvasが停止されると、以下のことが発生します。

- **スケジュールされたメッセージ:** Canvas内のユーザーの位置に関係なく、スケジュールされたメッセージは送信されません。これには、レート制限によりキューに入れられたユーザーも含まれます。
- **メール送信:** メール送信はすぐに停止しない場合があります。メールサービスプロバイダー（ESP）が既存のリクエストの処理を続行する可能性があるためです。
- **遅延ステップ:** [遅延ステップ]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step)にいるユーザーは通常どおりそこに留まりますが、設定された期間が終了するとCanvasを退出します。
- **下書きの変更:** Canvasが停止されると、Canvasへの下書きの変更は破棄されます。

Canvasを再開するには、Canvasビルダーの**Summary**ステップに移動し、**Resume Canvas**を選択します。再開されると、以前停止されたメッセージはスケジュールどおりに送信されます&#8212;スケジュールされた時間がまだ過ぎていない場合に限ります。

## ベストプラクティス {#best-practices}

### ステータスでメッセージを監視する {#monitor-your-messages-by-status}

ステータスでメッセージを監視して、パフォーマンスの詳細を確認できます。たとえば、一連のアクティブなCampaignがある場合、エンゲージメント指標で各Campaignのパフォーマンスを評価し、必要に応じて調整を行うことができます。停止済みのCanvasがいくつかある場合は、メッセージングのために再開すべきか、完全にアーカイブすべきかを検討できます。

{% alert tip %}
整理するためのその他の方法をお探しですか？[チーム]({{site.baseurl}}/user_guide/administer/global/user_management/teams)や[タグ]({{site.baseurl}}/user_guide/messaging/governance/tags)を追加して、一目でより多くのコンテキストを提供しましょう。
{% endalert %}

### アクティブなメッセージを監査する {#audit-your-active-messages}

アクティブなCampaignおよびCanvasの監査を実施することで、関連性とパフォーマンスを評価し、古くなったCampaignおよびCanvasを削除または更新して、メッセージングを常に最新の状態に保つことができます。