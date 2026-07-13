---
nav_title: 8月
page_order: 6
noindex: true
page_type: update
description: "この記事には、2018年8月のリリースノートが含まれています。"
---
# 2018年8月 {#august-2018}

## iOS 12通知グループ {#ios-12-notification-groups}

最新のiOS 12リリースでは、アプリケーションの通知グループ化（Android通知チャネルに類似）がサポートされています。[Brazeでは、メッセージ作成画面を使用してこのグループ化機能をiOSで利用できます。]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#notification-groups)

## Push Storyトリガー {#push-story-triggering}

Push Storyスライドの特定のページクリックに基づいて、ユーザーをリターゲティングできるようになりました。**キャンペーンとインタラクションした**の追加フィルターを使用します。

## 匿名ユーザーからのS3およびAzureデータイベント {#s3-and-azure-data-events-from-anonymous-users}

Amazon S3およびMicrosoft Azureにデータをエクスポートするお客様が、匿名ユーザーからのイベントを含めることができるようになりました。この機能は、新しく作成された統合ではすべてデフォルトでオンになりますが、既存の統合ではすべてオフのままになります。ご不明な点がございましたら、アカウントマネージャーにお問い合わせいただくか、[サポートチケット]({{site.baseurl}}/braze_support/)を作成してください。

## Mixpanelコホート統合 {#mixpanel-cohorts-integration}

BrazeとMixpanelの両方をご利用のお客様が、[MixpanelコホートをセグメントフィルターとしてBrazeに統合・送信]({{site.baseurl}}/partners/insights/behavioral_analytics/mixpanel_for_currents/#mixpanel-cohort-import)できるようになりました。1回限りの手動エクスポートを設定するか、2時間ごとのダイナミックなエクスポートを設定できます。更新された各ユーザーはデータポイントとしてカウントされますが、Mixpanelからは前回の同期以降の変更のみが送信されます。