---
nav_title: 通知設定
article_title: 通知設定
page_order: 1
page_type: reference
description: "このリファレンス記事では、会社アカウントでのメッセージングとアクティビティの監視に使用できるオプションについて説明します。"

---

# 通知設定 {#notification-preferences}

> 会社アカウントのメッセージングとアクティビティを監視する場合は、特定の通知を設定してその宛先を選択できます。

**通知設定**ページでは、会社に関する通知を受信するユーザー（存在する場合）を設定できます。Campaignの配信や技術的なエラーに関する通知を受信するユーザーを設定できます。週次分析レポートの受信者も指定できます。ほとんどの通知について、Brazeはメールとwebhookチャネルをサポートしています。

![Brazeダッシュボードの通知設定ページ]({% image_buster /assets/img_archive/notification_preferences.png %})

このページにアクセスするには、**設定** > **管理者設定** > **通知設定**に移動します。

{% alert tip %}
Slackと統合して通知を受信することもできます。手順については、[受信webhookを使用したメッセージの送信](https://api.slack.com/incoming-webhooks)を参照してください。
{% endalert %}

## 利用可能な通知 {#available-notifications}

利用可能な通知と、それを配信するために使用されるチャネルの説明を次の表に示します。

{% alert note %}
通知の種類によっては、受信者のドロップダウンに**All Dashboard Users**や**All Admins**が表示されない場合があります。手動で入力することもできますが、受信者の値は大文字と小文字が区別され、正確に一致する必要があります。英語以外にローカライズされたダッシュボードの場合は、フレーズを自分で翻訳するのではなく、その通知で候補が表示される際にBrazeが表示する正確な受信者タグを使用してください。
{% endalert %}

| 通知 | 説明 | 利用可能な通知チャネル |
|--------------|-------------|-----------------|
| API使用量アラート | これを選択すると**API使用量ダッシュボード**に移動し、[**API使用量アラート**]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/api_usage_alerts/)タブで主要なAPIリクエスト量を追跡するアラートを設定できます。 | メール、Webhook |
| AWS認証情報エラー | BrazeがデータエクスポートのためにAmazon Web Servicesの認証情報を使用しようとした際にエラーが発生した場合、受信者に通知します。これには、Google Cloud StorageとAzure（Microsoft Cloud Services）の認証エラー通知が含まれます。 | メール、Webhook |
| Campaignの自動停止 | BrazeがCampaignを停止したときに受信者に通知します。 | メール |
| Canvasの自動停止 | BrazeがCanvasを停止したときに受信者に通知します。 | メール |
| Campaignインタラクションの有効期限 | Campaignのインタラクションデータの有効期限が切れる予定のCampaignについて、リターゲティングフィルターで参照され、過去30日間にメッセージの送信に使用されたSegments、Campaigns、またはCanvasesに関する情報とともに受信者に通知します。 | メール |
| Campaign/Canvasの更新 | アクティブなCampaignまたはCanvasが更新または無効化されたとき、および非アクティブなCampaignまたはCanvasが再有効化されたとき、または下書きが起動されたときに受信者に通知します。 | メール |
| Campaign/Canvasのボリューム制限到達 | CampaignまたはCanvasがボリューム制限に達したときに受信者に通知します。 | メール |
| Canvasインタラクションの有効期限 | Canvasのインタラクションデータの有効期限が切れる予定のCanvasについて、リターゲティングフィルターで参照され、過去30日間にメッセージの送信に使用されたSegments、Campaigns、またはCanvasesに関する情報とともに受信者に通知します。 | メール |
| Canvas内のコメント | Canvasに新しいコメントがある場合に受信者に通知します。 | メール |
| コネクテッドコンテンツエラー | コネクテッドコンテンツのエンドポイントでエラーが発生した場合に受信者に通知します。 | メール |
| プッシュエラー | プッシュエンドポイントでエラーが発生した場合に受信者に通知します。 | メール、Webhook |
| スケジュールされたCampaignの制限到達 | 定期的にスケジュールされたCampaignの制限に達した場合に受信者に通知します。 | メール、Webhook |
| スケジュールされたCampaignの送信完了 | スケジュールされたCampaignの送信が完了した場合に受信者に通知します。 | メール、Webhook |
| Webhookエラー | Webhookエンドポイントでエラーが発生した場合に受信者に通知します。 | メール |
| 週次分析レポート | 毎週月曜日に、過去1週間のワークスペースアクティビティの概要を受信者に送信します。受信者は、所属する各ワークスペースの概要を受け取ります。 | メール |
| 日次Canvas/Campaignエントリボリューム制限 | 送信制限に達するたびに通知を送信します。 | メール |
| エージェントコンソールエラー | [エージェントコンソールのエージェント]({{site.baseurl}}/user_guide/brazeai/agents/)が実行制限に達した場合、利用できなくなったモデルを使用している場合、またはLLMプロバイダーとの課金エラーが発生した場合（独自のAPIキーを使用している場合のみ）に受信者に通知します。 | メール |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="利用可能な通知" }

{% alert note %}
[一時停止されたユーザー]({{site.baseurl}}/user_guide/administer/global/user_management/manage_company_users/#suspending-company-users)は、引き続きBrazeから通知を受信する場合があります。
{% endalert %}

## 週次分析レポート {#weekly-analytics-reporting}

Brazeはオプションで、毎週月曜日の午前5時（EST）に、社内で指定したユーザーにメールで週次レポートを送信します。週次レポートに含めるカスタムイベントは、**データ設定** > **カスタムイベント**から選択できます。

週次レポートには最大5つのイベントを含めることができます。

![分析レポートに含めるイベントの選択]({% image_buster /assets/img_archive/company_analytics_report_new.png %})