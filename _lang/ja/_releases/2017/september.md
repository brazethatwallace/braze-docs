---
nav_title: 9月
page_order: 4
noindex: true
page_type: update
description: "この記事には2017年9月のリリースノートが含まれています。"
---

# 2017年9月 {#september-2017}

## エンゲージメントレポートの新機能 {#new-functionality-for-engagement-reports}

特定の期間にわたってキャンペーンの指標を集計するために、[エンゲージメントレポート]({{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports/#engagement-reports)を使用できるようになりました。例えば、四半期の合計開封数や、キャンペーンまたはキャンバスの全期間における合計クリック数をエクスポートできます。必要な操作は以下のとおりです。
- データをエクスポートする期間を選択します。
- 定期的に1人以上の受信者に送信されるエンゲージメントレポートをスケジュールします。
- タグに基づいてキャンペーンとキャンバスをレポートに追加します。

## ユーザープロファイルページの更新 {#updates-to-user-profile-page}

[ユーザープロファイルページ]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles/#using-user-search)が更新されました。

## 閉じるためにユーザーアクションが必要なWebプッシュ通知 {#web-push-notifications-that-require-user-action-to-dismiss}

受信者がメッセージを閉じるためにメッセージの操作を必要とするよう、Chrome Webプッシュのメッセージクローズ動作を設定できるようになりました。この機能を使用するには、Web SDKバージョン1.6.13以降が必要です。

## メールプレヘッダー {#email-preheaders}

Braze内でメールメッセージを作成する際、**送信情報**セクションにプレヘッダーを簡単に挿入できるようになりました。

## 生イベントエクスポート用の新しいAPIエンドポイント {#new-api-endpoint-for-raw-event-export}

新しい[APIエンドポイント]({{site.baseurl}}/developer_guide/rest_api/api_network_connectivity_issues/#whitelisting-brazes-api-endpoint-ip-ranges) `/raw_data/status` を追加しました。これにより、特定の日がRaw Event Exportに読み込まれているかどうかをクエリで確認できます。特定の日の生データが利用可能かどうかを確認し、デバッグやオートメーションに役立てることができます。