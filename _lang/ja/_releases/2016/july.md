---
nav_title: 7月
page_order: 6
noindex: true
page_type: update
description: "この記事には2016年7月のリリースノートが含まれています。"
---

# 2016年7月 {#july-2016}

## エラータイプによる開発者コンソールのエラーログのフィルタリング {#filtering-the-developer-consoles-error-log-by-error-type}

このアップグレードにより、開発者コンソールのメッセージエラーログを使用して、Braze統合の問題をトラブルシューティングしやすくなります。このユーザビリティ更新では、メッセージエラーログをタイプ別にフィルターできるようになり、特定の統合の問題をより簡単に見つけて特定できます。

## 最後に送信されたアンインストール追跡プッシュのタイムスタンプを追加 {#added-timestamp-for-last-uninstall-tracking-push-sent}

Brazeは、顧客のアプリにサイレントプッシュを送信し、どのデバイスが応答するかを確認することでアンインストールを検出します。この機能により、アンインストール追跡が最後に実行された日時を示す目立たないタイムスタンプが追加されます。このタイムスタンプは、アンインストール追跡が設定されている設定ページで確認できます。[アンインストール追跡]({{site.baseurl}}/user_guide/analytics/tracking/uninstall_tracking/)について詳しくはこちらをご覧ください。

![アンインストール追跡チェックボックス]({% image_buster /assets/img_archive/uninstall_tracking_checkbox.png %})

## Webhookテストの機能強化 {#added-webhook-testing-enhancements}

キャンペーンを本番に設定する前に、BrazeからライブWebhookメッセージをテスト送信できるようになりました。テストメッセージを送信することで、安全なサンドボックス環境でメッセージとサーバーエンドポイントが適切に設定されていることを確認できます。[webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#creating-a-webhook)について詳しくはこちらをご覧ください。

## キャンペーン受信者CSVエクスポートに受信メッセージのバリエーションを追加 {#added-message-variation-received-to-campaign-recipients-csv-export}

キャンペーン受信者CSVエクスポートに、受信したメッセージのバリエーションを示すカラムを追加しました。Brazeからの[データエクスポート]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/)について詳しくはこちらをご覧ください。

## インプレッション数のおおよその制限 {#approximate-limit-on-number-of-impressions}

アプリ内メッセージが一定数のインプレッションを獲得すると、Brazeはユーザーがそのメッセージを受け取る資格を得ることを停止します。インプレッションのおおよその[制限の設定]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#setting-a-max-impression-cap)について詳しくはこちらをご覧ください。

![アプリ内メッセージのインプレッション上限]({% image_buster /assets/img_archive/approx_limit_for_IAM.png %})