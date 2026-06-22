---
nav_title: 6月
page_order: 7
noindex: true
page_type: update
description: "この記事には2020年6月のリリースノートが含まれています。"
---
# 2020年6月 {#june-2020}

## リテンションレポート {#retention-reports}

リテンションレポートで、[キャンペーン]({{site.baseurl}}/user_guide/messaging/campaigns/test_campaigns/retention_reports/)および[キャンバス]({{site.baseurl}}/user_guide/analytics/reports/retention_reports/)の範囲リテンションが利用できるようになりました。範囲リテンションは、特定の期間中に戻ってきて、選択したリテンションイベントを実行するユーザーの数を測定します。

## ユーザートラックAPIの更新 {#user-track-api-updates}

[`users/track`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)のデフォルトレートが、2020年6月2日以降に作成されたダッシュボード企業では1分あたり50,000 APIリクエストになりました。この日付より前に作成された既存の企業とそのワークスペースは、`users/track`エンドポイントへの無制限のAPIリクエストが引き続き許可されます。

Brazeは、APIおよびインフラの安定性と信頼性の目標に向けたステップとして、最も頻繁に使用される顧客向けエンドポイントにこのデフォルトを課しています。課せられる制限は非常に緩やかであり、ダッシュボード企業とその通常業務にはほとんど影響しません。この制限の引き上げが必要な場合は、カスタマーサクセスマネージャーまたはサポートチームに連絡して増額をリクエストしてください。