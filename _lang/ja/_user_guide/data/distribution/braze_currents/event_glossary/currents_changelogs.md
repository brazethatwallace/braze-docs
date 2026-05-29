---
nav_title: Currents イベント変更ログ
page_order: 6
description: "このページには、Currentsの各リリースにおけるイベントの変更点が記載されています。"
tool: Currents
---

# Currents変更ログ {#currents-changelog}

## バージョン 9 の変更点（リリース日：2026年6月3日） {#changes-in-version-9-release-date-2026-06-03}

### ストレージに関する変更: {#changes-for-storage}

* イベントタイプ `users.messages.email.Send` のフィールド変更:
    * 新しい `string` フィールド `from_domain` を追加しました: メールの送信ドメイン

## バージョン 8 の変更点（リリース日：2026年5月6日） {#changes-in-version-8-release-date-2026-05-06}

### ストレージに関する変更:

* 新しいイベントタイプ `users.messages.banner.Dismiss` を追加しました。

* イベントタイプ `users.messages.whatsapp.Abort` のフィールド変更:
    * 新しい `string` フィールド `bsuid` を追加しました: このイベントに関連付けられた受信者のWhatsApp Business-Scoped User IDです。

* イベントタイプ `users.messages.whatsapp.Delivery` のフィールド変更:
    * 新しい `string` フィールド `bsuid` を追加しました: このイベントに関連付けられた受信者のWhatsApp Business-Scoped User IDです。

* イベントタイプ `users.messages.whatsapp.Failure` のフィールド変更:
    * 新しい `string` フィールド `bsuid` を追加しました: このイベントに関連付けられた受信者のWhatsApp Business-Scoped User IDです。

* イベントタイプ `users.messages.whatsapp.InboundReceive` のフィールド変更:
    * 新しい `string` フィールド `bsuid` を追加しました: メッセージの送信元ユーザーのWhatsApp Business-Scoped User IDです。
    * フィールド `user_phone_number` が*オプション*になりました。

* イベントタイプ `users.messages.whatsapp.Read` のフィールド変更:
    * 新しい `string` フィールド `bsuid` を追加しました: このイベントに関連付けられた受信者のWhatsApp Business-Scoped User IDです。

* イベントタイプ `users.messages.whatsapp.Retry` のフィールド変更:
    * 新しい `string` フィールド `bsuid` を追加しました: このイベントに関連付けられた受信者のWhatsApp Business-Scoped User IDです。

* イベントタイプ `users.messages.whatsapp.Send` のフィールド変更:
    * 新しい `string` フィールド `bsuid` を追加しました: このイベントに関連付けられた受信者のWhatsApp Business-Scoped User IDです。

## バージョン 7 の変更点（リリース日：2026年4月1日） {#changes-in-version-7-release-date-2026-04-01}

### ストレージに関する変更:

* 新しいイベントタイプ `users.profile.Update` を追加しました。

* イベントタイプ `users.messages.banner.Abort` のフィールド変更:
    * 新しい `string` フィールド `canvas_name` を追加しました: Canvasの名前
    * 新しい `string` フィールド `canvas_step_name` を追加しました: Canvasステップの名前
    * 新しい `string` フィールド `canvas_variation_name` を追加しました: このユーザーが受け取ったCanvasバリエーションの名前
    * 新しい `string` フィールド `canvas_id` を追加しました: このイベントが属するCanvasのAPI ID
    * 新しい `string` フィールド `canvas_step_id` を追加しました: このイベントが属するCanvasステップのAPI ID
    * 新しい `string` フィールド `canvas_step_message_variation_id` を追加しました: このユーザーが受け取ったCanvasステップメッセージバリエーションのAPI ID
    * 新しい `string` フィールド `canvas_variation_id` を追加しました: このイベントが属するCanvasバリエーションのAPI ID

* イベントタイプ `users.messages.banner.Click` のフィールド変更:
    * 新しい `string` フィールド `canvas_id` を追加しました: このイベントが属するCanvasのAPI ID
    * 新しい `string` フィールド `canvas_step_id` を追加しました: このイベントが属するCanvasステップのAPI ID
    * 新しい `string` フィールド `canvas_name` を追加しました: Canvasの名前
    * 新しい `string` フィールド `canvas_step_name` を追加しました: Canvasステップの名前
    * 新しい `string` フィールド `canvas_step_message_variation_id` を追加しました: このユーザーが受け取ったCanvasステップメッセージバリエーションのAPI ID
    * 新しい `string` フィールド `canvas_variation_id` を追加しました: このイベントが属するCanvasバリエーションのAPI ID
    * 新しい `string` フィールド `canvas_variation_name` を追加しました: このユーザーが受け取ったCanvasバリエーションの名前

* イベントタイプ `users.messages.banner.Impression` のフィールド変更:
    * 新しい `string` フィールド `canvas_id` を追加しました: このイベントが属するCanvasのAPI ID
    * 新しい `string` フィールド `canvas_step_id` を追加しました: このイベントが属するCanvasステップのAPI ID
    * 新しい `string` フィールド `canvas_name` を追加しました: Canvasの名前
    * 新しい `string` フィールド `canvas_step_name` を追加しました: Canvasステップの名前
    * 新しい `string` フィールド `canvas_step_message_variation_id` を追加しました: このユーザーが受け取ったCanvasステップメッセージバリエーションのAPI ID
    * 新しい `string` フィールド `canvas_variation_id` を追加しました: このイベントが属するCanvasバリエーションのAPI ID
    * 新しい `string` フィールド `canvas_variation_name` を追加しました: このユーザーが受け取ったCanvasバリエーションの名前

## バージョン 6 の変更点（リリース日：2026年3月4日） {#changes-in-version-6-release-date-2026-03-04}

### ストレージに関する変更:

* イベントタイプ `agentconsole.AgentExecuted` のフィールド変更:
    * 新しい `string` フィールド `error` を追加しました: エラーの説明

* イベントタイプ `agentconsole.ToolInvocation` のフィールド変更:
    * 新しい `string` フィールド `request_id` を追加しました: このLLMリクエスト全体と完全な実行に対するユニークID

* イベントタイプ `users.messages.rcs.InboundReceive` のフィールド変更:
    * 新しい `string` フィールド `canvas_variation_name` を追加しました: このユーザーが受け取ったCanvasバリエーションの名前

## バージョン 5 の変更点（リリース日：2026年2月4日） {#changes-in-version-5-release-date-2026-02-04}

### ストレージに関する変更:

* 新しいイベントタイプ `agentconsole.AgentExecuted` を追加しました。

* 新しいイベントタイプ `agentconsole.ToolInvocation` を追加しました。

* 新しいイベントタイプ `users.messages.email.Retry` を追加しました。

* 新しいイベントタイプ `users.messages.line.Retry` を追加しました。

* 新しいイベントタイプ `users.messages.pushnotification.Retry` を追加しました。

* 新しいイベントタイプ `users.messages.sms.Retry` を追加しました。

* 新しいイベントタイプ `users.messages.webhook.Retry` を追加しました。

* 新しいイベントタイプ `users.messages.whatsapp.Retry` を追加しました。

* イベントタイプ `users.behaviors.pushnotification.TokenStateChange` のフィールド変更:
    * 新しい `long` フィールド `time_ms` を追加しました: イベントが発生した時刻（ミリ秒単位）

## バージョン 4 の変更点（リリース日：2026年1月7日） {#changes-in-version-4-release-date-2026-01-07}

### ストレージに関する変更:

* イベントタイプ `users.behaviors.pushnotification.TokenStateChange` のフィールド変更:
    * 新しい `string` フィールド `push_token` を追加しました: イベントのプッシュトークン

* イベントタイプ `users.messages.pushnotification.Bounce` のフィールド変更:
    * 新しい `string` フィールド `push_token` を追加しました: イベントのプッシュトークン

* イベントタイプ `users.messages.pushnotification.Send` のフィールド変更:
    * 新しい `string` フィールド `push_token` を追加しました: イベントのプッシュトークン

* イベントタイプ `users.messages.rcs.Click` のフィールド変更:
    * 新しい `string` フィールド `canvas_variation_name` を追加しました: このユーザーが受け取ったCanvasバリエーションの名前
    * フィールド `user_phone_number` が*オプション*になりました。

* イベントタイプ `users.messages.rcs.InboundReceive` のフィールド変更:
    * フィールド `user_id` が*オプション*になりました。

* イベントタイプ `users.messages.rcs.Rejection` のフィールド変更:
    * 新しい `string` フィールド `canvas_step_message_variation_id` を追加しました: このユーザーが受け取ったCanvasステップメッセージバリエーションのAPI ID

## バージョン 3 の変更点（リリース日：2025年10月8日） {#changes-in-version-3-release-date-2025-10-08}

### ストレージに関する変更:

* 新しいイベントタイプ `users.messages.line.Abort` を追加しました。

* 新しいイベントタイプ `users.messages.line.Click` を追加しました。

* 新しいイベントタイプ `users.messages.line.InboundReceive` を追加しました。

* 新しいイベントタイプ `users.messages.line.Send` を追加しました。

* 新しいイベントタイプ `users.messages.rcs.Abort` を追加しました。

* 新しいイベントタイプ `users.messages.rcs.Click` を追加しました。

* 新しいイベントタイプ `users.messages.rcs.Delivery` を追加しました。

* 新しいイベントタイプ `users.messages.rcs.InboundReceive` を追加しました。

* 新しいイベントタイプ `users.messages.rcs.Read` を追加しました。

* 新しいイベントタイプ `users.messages.rcs.Rejection` を追加しました。

* 新しいイベントタイプ `users.messages.rcs.Send` を追加しました。

* イベントタイプ `users.messages.sms.Delivery` のフィールド変更:
    * 新しい `boolean` フィールド `is_sms_fallback` を追加しました: RCSメッセージが拒否されたため、SMSフォールバックメッセージが送信されたことを示します。このメッセージは配信、配信失敗、または拒否になる可能性があります。送信IDとディスパッチIDを使用してRCS Rejectionイベントにリンクできます。

* イベントタイプ `users.messages.sms.DeliveryFailure` のフィールド変更:
    * 新しい `boolean` フィールド `is_sms_fallback` を追加しました: RCSメッセージが拒否されたため、SMSフォールバックメッセージが送信されたことを示します。このメッセージは配信、配信失敗、または拒否になる可能性があります。送信IDとディスパッチIDを使用してRCS Rejectionイベントにリンクできます。

* イベントタイプ `users.messages.sms.Rejection` のフィールド変更:
    * 新しい `boolean` フィールド `is_sms_fallback` を追加しました: RCSメッセージが拒否されたため、SMSフォールバックメッセージが送信されたことを示します。このメッセージは配信、配信失敗、または拒否になる可能性があります。送信IDとディスパッチIDを使用してRCS Rejectionイベントにリンクできます。（イベントプロパティ）

* イベントタイプ `users.messages.whatsapp.Delivery` のフィールド変更:
    * 新しい `string` フィールド `flow_id` を追加しました: WhatsApp ManagerにおけるフローのユニークID。メッセージにWhatsApp Flowへの応答を求めるCTAが含まれている場合に存在します。
    * 新しい `string` フィールド `template_name` を追加しました: [PII] WhatsApp Manager内のテンプレートの名前。テンプレートメッセージを送信する場合に存在します。
    * 新しい `string` フィールド `message_id` を追加しました: このメッセージに対してMetaが生成したユニークID

* イベントタイプ `users.messages.whatsapp.Failure` のフィールド変更:
    * 新しい `string` フィールド `message_id` を追加しました: このメッセージに対してMetaが生成したユニークID
    * 新しい `string` フィールド `template_name` を追加しました: [PII] WhatsApp Manager内のテンプレートの名前。テンプレートメッセージを送信する場合に存在します。
    * 新しい `string` フィールド `flow_id` を追加しました: WhatsApp ManagerにおけるフローのユニークID。メッセージにWhatsApp Flowへの応答を求めるCTAが含まれている場合に存在します。

* イベントタイプ `users.messages.whatsapp.InboundReceive` のフィールド変更:
    * 新しい `string` フィールド `catalog_id` を追加しました: インバウンドメッセージで製品が参照されている場合のカタログID。それ以外の場合は空です。
    * 新しい `string` フィールド `product_id` を追加しました: インバウンドメッセージで製品が参照されている場合の製品SKU。それ以外の場合は空です。
    * 新しい `string` フィールド `flow_id` を追加しました: WhatsApp ManagerにおけるフローのユニークID。ユーザーがWhatsApp Flowに応答している場合に存在します。
    * 新しい `string` フィールド `flow_response_json` を追加しました: [PII] ユーザーが応答したフォームの値。ユーザーがWhatsApp Flowに応答している場合に存在します。
    * 新しい `string` フィールド `message_id` を追加しました: このメッセージに対してMetaが生成したユニークID
    * 新しい `string` フィールド `in_reply_to` を追加しました: このメッセージが返信した元メッセージのmessage_id

* イベントタイプ `users.messages.whatsapp.Read` のフィールド変更:
    * 新しい `string` フィールド `template_name` を追加しました: [PII] WhatsApp Manager内のテンプレートの名前。テンプレートメッセージを送信する場合に存在します。
    * 新しい `string` フィールド `message_id` を追加しました: このメッセージに対してMetaが生成したユニークID
    * 新しい `string` フィールド `flow_id` を追加しました: WhatsApp ManagerにおけるフローのユニークID。メッセージにWhatsApp Flowへの応答を求めるCTAが含まれている場合に存在します。

* イベントタイプ `users.messages.whatsapp.Send` のフィールド変更:
    * 新しい `string` フィールド `flow_id` を追加しました: WhatsApp ManagerにおけるフローのユニークID。メッセージにWhatsApp Flowへの応答を求めるCTAが含まれている場合に存在します。
    * 新しい `string` フィールド `template_name` を追加しました: [PII] WhatsApp Manager内のテンプレートの名前。テンプレートメッセージを送信する場合に存在します。
    * 新しい `string` フィールド `message_id` を追加しました: このメッセージに対してMetaが生成したユニークID

## バージョン 2 の変更点（リリース日なし） {#changes-in-version-2-release-date-null}

### ストレージに関する変更:

* 新しいイベントタイプ `users.behaviors.app.FirstSession` を追加しました。

* 新しいイベントタイプ `users.behaviors.app.SessionEnd` を追加しました。

* 新しいイベントタイプ `users.behaviors.app.SessionStart` を追加しました。

* 新しいイベントタイプ `users.behaviors.CustomEvent` を追加しました。

* 新しいイベントタイプ `users.behaviors.InstallAttribution` を追加しました。

* 新しいイベントタイプ `users.behaviors.liveactivity.PushToStartTokenChange` を追加しました。

* 新しいイベントタイプ `users.behaviors.liveactivity.UpdateTokenChange` を追加しました。

* 新しいイベントタイプ `users.behaviors.Location` を追加しました。

* 新しいイベントタイプ `users.behaviors.Purchase` を追加しました。

* 新しいイベントタイプ `users.behaviors.pushnotification.TokenStateChange` を追加しました。

* 新しいイベントタイプ `users.behaviors.subscription.GlobalStateChange` を追加しました。

* 新しいイベントタイプ `users.behaviors.subscriptiongroup.StateChange` を追加しました。

* 新しいイベントタイプ `users.behaviors.Uninstall` を追加しました。

* 新しいイベントタイプ `users.campaigns.Conversion` を追加しました。

* 新しいイベントタイプ `users.campaigns.EnrollInControl` を追加しました。

* 新しいイベントタイプ `users.canvas.Conversion` を追加しました。

* 新しいイベントタイプ `users.canvas.Entry` を追加しました。

* 新しいイベントタイプ `users.canvas.exit.MatchedAudience` を追加しました。

* 新しいイベントタイプ `users.canvas.exit.PerformedEvent` を追加しました。

* 新しいイベントタイプ `users.canvas.experimentstep.Conversion` を追加しました。

* 新しいイベントタイプ `users.canvas.experimentstep.SplitEntry` を追加しました。

* 新しいイベントタイプ `users.canvasstep.Progression` を追加しました。

* 新しいイベントタイプ `users.messages.banner.Abort` を追加しました。

* 新しいイベントタイプ `users.messages.banner.Click` を追加しました。

* 新しいイベントタイプ `users.messages.banner.Impression` を追加しました。

* 新しいイベントタイプ `users.messages.contentcard.Abort` を追加しました。

* 新しいイベントタイプ `users.messages.contentcard.Click` を追加しました。

* 新しいイベントタイプ `users.messages.contentcard.Dismiss` を追加しました。

* 新しいイベントタイプ `users.messages.contentcard.Impression` を追加しました。

* 新しいイベントタイプ `users.messages.contentcard.Send` を追加しました。

* 新しいイベントタイプ `users.messages.email.Abort` を追加しました。

* 新しいイベントタイプ `users.messages.email.Bounce` を追加しました。

* 新しいイベントタイプ `users.messages.email.Click` を追加しました。

* 新しいイベントタイプ `users.messages.email.Deferral` を追加しました。

* 新しいイベントタイプ `users.messages.email.Delivery` を追加しました。

* 新しいイベントタイプ `users.messages.email.MarkAsSpam` を追加しました。

* 新しいイベントタイプ `users.messages.email.Open` を追加しました。

* 新しいイベントタイプ `users.messages.email.Send` を追加しました。

* 新しいイベントタイプ `users.messages.email.SoftBounce` を追加しました。

* 新しいイベントタイプ `users.messages.email.Unsubscribe` を追加しました。

* 新しいイベントタイプ `users.messages.featureflag.Impression` を追加しました。

* 新しいイベントタイプ `users.messages.inappmessage.Abort` を追加しました。

* 新しいイベントタイプ `users.messages.inappmessage.Click` を追加しました。

* 新しいイベントタイプ `users.messages.inappmessage.Impression` を追加しました。

* 新しいイベントタイプ `users.messages.liveactivity.Outcome` を追加しました。

* 新しいイベントタイプ `users.messages.liveactivity.Send` を追加しました。

* 新しいイベントタイプ `users.messages.pushnotification.Abort` を追加しました。

* 新しいイベントタイプ `users.messages.pushnotification.Bounce` を追加しました。

* 新しいイベントタイプ `users.messages.pushnotification.IosForeground` を追加しました。

* 新しいイベントタイプ `users.messages.pushnotification.Open` を追加しました。

* 新しいイベントタイプ `users.messages.pushnotification.Send` を追加しました。

* 新しいイベントタイプ `users.messages.sms.Abort` を追加しました。

* 新しいイベントタイプ `users.messages.sms.CarrierSend` を追加しました。

* 新しいイベントタイプ `users.messages.sms.Delivery` を追加しました。

* 新しいイベントタイプ `users.messages.sms.DeliveryFailure` を追加しました。

* 新しいイベントタイプ `users.messages.sms.InboundReceive` を追加しました。

* 新しいイベントタイプ `users.messages.sms.Rejection` を追加しました。

* 新しいイベントタイプ `users.messages.sms.Send` を追加しました。

* 新しいイベントタイプ `users.messages.sms.ShortLinkClick` を追加しました。

* 新しいイベントタイプ `users.messages.webhook.Abort` を追加しました。

* 新しいイベントタイプ `users.messages.webhook.Failure` を追加しました。

* 新しいイベントタイプ `users.messages.webhook.Send` を追加しました。

* 新しいイベントタイプ `users.messages.whatsapp.Abort` を追加しました。

* 新しいイベントタイプ `users.messages.whatsapp.Click` を追加しました。

* 新しいイベントタイプ `users.messages.whatsapp.Delivery` を追加しました。

* 新しいイベントタイプ `users.messages.whatsapp.Failure` を追加しました。

* 新しいイベントタイプ `users.messages.whatsapp.InboundReceive` を追加しました。

* 新しいイベントタイプ `users.messages.whatsapp.Read` を追加しました。

* 新しいイベントタイプ `users.messages.whatsapp.Send` を追加しました。

* 新しいイベントタイプ `users.RandomBucketNumberUpdate` を追加しました。