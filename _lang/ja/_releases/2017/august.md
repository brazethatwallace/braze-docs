---
nav_title: 8月
page_order: 5
noindex: true
page_type: update
description: "この記事には2017年8月のリリースノートが含まれています。"
---

# 2017年8月 {#august-2017}

## プッシュアクションボタンの更新 {#update-to-push-action-buttons}

REST APIメッセージングエンドポイントに[プッシュアクションボタン]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_action_buttons/#how-to-use-action-buttons)のサポートを追加しました。

## Liquidテンプレートの更新 {#update-to-liquid-templating}

以下の情報に基づいて[メッセージをパーソナライズ]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags/)できるようになりました：
- 送信先のデバイス、
- デバイスID、
- 通信事業者、
- IDFA、
- モデル、
- OS、
- プラットフォーム

## APIトリガーキャンバス {#api-triggered-canvas}

キャンペーン用の既存のエンドポイントと一致するAPIエンドポイント（送信、スケジュール、更新、削除）を介して[キャンバス]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/)をトリガーできるようになり、マーケティングの自動化と最適化をさらに進めることができます。

## Webプッシュアクションボタン {#web-push-action-buttons}

Chrome用のWeb SDKにプッシュアクションボタンのサポートを追加しました。ユーザーの多忙な生活を簡素化する状況に即した選択肢を提供することで、エンゲージメントを高めることができます。[プッシュ通知のベストプラクティス]({{site.baseurl}}/user_guide/channels/push/best_practices/)をご確認ください。

## 新しいAPIエンドポイント {#new-api-endpoints}

新しいAPIエンドポイントを公開しました。/email/hard_bouncesでは、メールアドレスまたは指定された日付範囲でハードバウンスを取得でき、/messages/scheduled_broadcastsでは、スケジュールされたキャンペーンおよびスケジュールされたエントリのキャンバスが次に開始される時刻を取得できます。これらの新しいエンドポイントにより、キャンペーンのさらなるカスタマイズと最適化が可能になります。[APIエンドポイント]({{site.baseurl}}/developer_guide/rest_api/basics/#what-is-a-rest-api)について詳しくはこちらをご覧ください。

## ジオフェンス {#geofences}

ジオフェンスという新機能を追加しました。顧客が定義済みの地理的エリアに出入りする際にリアルタイムでメッセージをトリガーでき、顧客とのパーソナライズされた関連性の高いコミュニケーションが可能になります。[ロケーションマーケティング]({{site.baseurl}}/developer_guide/geofences/?sdktab=android)について詳しくはこちらをご覧ください。

## メールエディターの更新 {#update-to-email-editor}

新しいメールエディターにダイナミックなオートコンプリート機能を追加しました。Liquidを使用する際に顧客の実際のカスタム属性やイベントでオートコンプリートできるようになり、作業がより簡単になります。[メールのベストプラクティス]({{site.baseurl}}/user_guide/channels/email/best_practices/)について詳しくはこちらをご覧ください。

## 日付フィルターの更新 {#update-to-date-filters}

「該当なし」の日付フィルターを追加しました。これにより、メッセージを一度も受信または操作したことのない顧客をターゲットにでき、クリーンな顧客リストを維持してメールの配信到達性を確保できます。[フィルター]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#segmentation-filters)について詳しくはこちらをご覧ください。

## キャンバスの更新 {#update-to-canvas}

各キャンバスバリアントの上部にパーセンテージが追加され、どのバリアントがより良いパフォーマンスを発揮しているかが一目でわかるようになりました。[キャンバス]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/)について詳しくはこちらをご覧ください。

## インテリジェントセレクションを使用したキャンバス {#canvas-with-intelligent-selection}

キャンバスにインテリジェントセレクションが追加され、キャンバスをより効率的にテストできるようになりました。[Intelligence Suite]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/)について詳しくはこちらをご覧ください。

## メール表示名の更新 {#update-to-email-display-names}

メールの表示名に特殊なUTF-8文字のサポートを追加しました。これにより、顧客向けにさらにパーソナライズされたメールを作成できます。[メールのベストプラクティス]({{site.baseurl}}/user_guide/channels/email/best_practices/)について詳しくはこちらをご覧ください。

## エンゲージメントレポートCSV集計 {#engagement-reports-csv-aggregation}

選択されているキャンペーンやキャンバスの数に関係なく、すべてのキャンペーンとすべてのキャンバスの統合データを2つの別々のファイルで受け取ることができるようになりました。必要なときに必要なすべてのデータを入手できます。[エンゲージメントレポート]({{site.baseurl}}/user_guide/analytics/reports/engagement_reports/)について詳しくはこちらをご覧ください。

> [2017年9月のリリースノート]({{site.baseurl}}/releases/2017/september/)に記載されているように、特定の期間のデータを集計したり、定期的にエクスポートを実行するスケジュールを設定したりできるようになりました。