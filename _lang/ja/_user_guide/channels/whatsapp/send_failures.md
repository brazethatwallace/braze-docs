---
nav_title: 送信失敗
article_title: WhatsApp送信失敗の調査
page_order: 22
page_type: reference
description: "キャンペーン分析、メッセージアクティビティログ、Currentsを使用して、WhatsApp送信失敗と一般的なMetaエラーコードを調査します。"
tool:
  - Reports
channel:
  - WhatsApp
---

# WhatsApp送信失敗の調査 {#investigate-whatsapp-send-failures}

> WhatsAppの配信数や既読数が予想より低い場合、またはキャンペーン分析で**失敗**が増加している場合に、このページを参照してください。

## 調査ワークフロー {#investigation-workflow}

以下のステップを順番に進めてください。

1. **キャンペーンまたはキャンバス分析で失敗を確認します。** メッセージステップを開き、**失敗**の件数と失敗率を確認します。送信数や配信数と比較して失敗が多い場合は、次のステップに進みます。
2. **メッセージアクティビティログでエラーコードを確認します。** 同じ送信の[メッセージアクティビティログ]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log)を開き、失敗したメッセージでフィルタリングして、プロバイダーのエラーコード（例：ユーザーごとのマーケティング制限を示す`131049`）を確認します。[一般的な失敗コード](#common-failure-codes)を使用してコードを解釈し、次のステップを決定します。
3. **Currentsで失敗をエクスポートして分析またはリターゲティングに活用します。** エラーコードを特定したら、Currentsを通じてWhatsApp送信失敗イベントをエクスポートします。そのデータを使用して、ウェアハウスで失敗の傾向を分析したり、セグメントを作成して別のチャネルでユーザーをリターゲティングしたりできます。

## 一般的な失敗コード {#common-failure-codes}

| エラーコード | 一般的な原因 | 次のステップ |
|---|---|---|
| `131049` | Metaのユーザーごとのマーケティング頻度制限または米国マーケティング一時停止 | [Metaリソース]({{site.baseurl}}/user_guide/channels/whatsapp/meta_resources)および[他のBrazeチャネルでのユーザーリターゲティング]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/optimized_delivery#retargeting-users-on-other-braze-channels)を参照してください |
| `130472` | Metaマーケティング実験のホールドアウト | [MetaリソースFAQ]({{site.baseurl}}/user_guide/channels/whatsapp/meta_resources#faq)を参照してください |
| `131026` | さまざまな未配信理由（Metaは詳細を開示していません） | 即時の再試行は避けてください。[Meta Cloud APIトラブルシューティング](https://developers.facebook.com/docs/whatsapp/cloud-api/support#troubleshooting)を確認してください |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="一般的なWhatsApp失敗コード" }