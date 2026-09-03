---
nav_title: Currentsイベント変更ログ
page_order: 6
description: "このページには、Currentsの各リリースにおけるイベントの変更点が記載されています。"
tool: Currents
---

# Currents変更ログ {#currents-changelog}

## バージョン12の変更点（リリース日：2026年9月2日） {#changes-in-version-12-release-date-2026-09-02}

### ストレージの変更点: {#changes-for-storage}

* イベントタイプ `users.messages.email.Abort` のフィールド変更：
    * 新しい `string` フィールド `message_extras` を追加：[PII] Liquidレンダリング中にタグ付けされたキーと値のペアのJSON文字列

* イベントタイプ `users.messages.email.Bounce` のフィールド変更：
    * 新しい `int` フィールド `send_time` を追加：対応する送信イベントの時刻

* イベントタイプ `users.messages.email.Click` のフィールド変更：
    * 新しい `int` フィールド `send_time` を追加：対応する送信イベントの時刻（秒単位）
    * 新しい `boolean` フィールド `has_url_parameters` を追加：クリックされたURLにクエリパラメーターが含まれていたかどうか
    * 新しい `boolean` フィールド `link_aliasing_enabled` を追加：このクリックが処理された時点でワークスペースのリンクエイリアスが有効だったかどうか

* イベントタイプ `users.messages.email.Deferral` のフィールド変更：
    * 新しい `int` フィールド `send_time` を追加：対応する送信イベントの時刻

* イベントタイプ `users.messages.email.Delivery` のフィールド変更：
    * 新しい `int` フィールド `send_time` を追加：対応する送信イベントの時刻

* イベントタイプ `users.messages.email.MarkAsSpam` のフィールド変更：
    * 新しい `int` フィールド `send_time` を追加：対応する送信イベントの時刻

* イベントタイプ `users.messages.email.Open` のフィールド変更：
    * 新しい `int` フィールド `send_time` を追加：対応する送信イベントの時刻

* イベントタイプ `users.messages.email.SoftBounce` のフィールド変更：
    * 新しい `int` フィールド `send_time` を追加：対応する送信イベントの時刻

* イベントタイプ `users.messages.line.Abort` のフィールド変更：
    * 新しい `string` フィールド `message_extras` を追加：[PII] Liquidレンダリング中にタグ付けされたキーと値のペアのJSON文字列

* イベントタイプ `users.messages.pushnotification.Abort` のフィールド変更：
    * 新しい `string` フィールド `message_extras` を追加：[PII] Liquidレンダリング中にタグ付けされたキーと値のペアのJSON文字列

* イベントタイプ `users.messages.rcs.Abort` のフィールド変更：
    * 新しい `string` フィールド `message_extras` を追加：[PII] Liquidレンダリング中にタグ付けされたキーと値のペアのJSON文字列

* イベントタイプ `users.messages.sms.Abort` のフィールド変更：
    * 新しい `string` フィールド `message_extras` を追加：[PII] Liquidレンダリング中にタグ付けされたキーと値のペアのJSON文字列

* イベントタイプ `users.messages.webhook.Abort` のフィールド変更：
    * 新しい `string` フィールド `message_extras` を追加：[PII] Liquidレンダリング中にタグ付けされたキーと値のペアのJSON文字列

* イベントタイプ `users.messages.whatsapp.Abort` のフィールド変更：
    * 新しい `string` フィールド `message_extras` を追加：[PII] Liquidレンダリング中にタグ付けされたキーと値のペアのJSON文字列

## バージョン11の変更点（リリース日：2026年8月5日） {#changes-in-version-11-release-date-2026-08-05}

### ストレージの変更:

* 新しいイベントタイプ `contentoptimizer.ComponentStore` を追加しました。

* 新しいイベントタイプ `users.canvas.costep.Conversion` を追加しました。

* 新しいイベントタイプ `users.messages.landingpage.Click` を追加しました。

* 新しいイベントタイプ `users.messages.landingpage.FormSubmission` を追加しました。

* 新しいイベントタイプ `users.messages.landingpage.Impression` を追加しました。

* 新しいイベントタイプ `users.messages.survey.Response` を追加しました。

* イベントタイプ `agentconsole.AgentExecuted` のフィールド変更:
    * 新しい `string` フィールド `thinking_level` を追加しました: リクエストに使用された思考/推論レベル

* イベントタイプ `users.messages.banner.Click` のフィールド変更:
    * 新しい `boolean` フィールド `is_unique` を追加しました: メッセージバリエーションに対するユーザーの初回クリックであるかどうかを示し、ユニーククリック統計にカウントされます

* イベントタイプ `users.messages.banner.Dismiss` のフィールド変更:
    * 新しい `boolean` フィールド `is_unique` を追加しました: メッセージバリエーションに対するユーザーの初回却下であるかどうかを示し、ユニーク却下統計にカウントされます

* イベントタイプ `users.messages.banner.Impression` のフィールド変更:
    * 新しい `boolean` フィールド `is_unique` を追加しました: メッセージバリエーションに対するユーザーの初回インプレッションであるかどうかを示し、ユニークインプレッション統計にカウントされます

* イベントタイプ `users.messages.contentcard.Click` のフィールド変更:
    * 新しい `boolean` フィールド `is_unique` を追加しました: メッセージバリエーションに対するユーザーの初回クリックであるかどうかを示し、ユニーククリック統計にカウントされます

* イベントタイプ `users.messages.contentcard.Dismiss` のフィールド変更:
    * 新しい `boolean` フィールド `is_unique` を追加しました: メッセージバリエーションに対するユーザーの初回却下であるかどうかを示し、ユニーク却下統計にカウントされます

* イベントタイプ `users.messages.contentcard.Impression` のフィールド変更:
    * 新しい `boolean` フィールド `is_unique` を追加しました: メッセージバリエーションに対するユーザーの初回インプレッションであるかどうかを示し、ユニークインプレッション統計にカウントされます

* イベントタイプ `users.messages.featureflag.Impression` のフィールド変更:
    * 新しい `boolean` フィールド `is_unique` を追加しました: このフィーチャーフラグに対するユーザーの初回インプレッションであるかどうかを示し、ユニークインプレッション統計にカウントされます

## バージョン10の変更点（リリース日：2026年7月1日） {#changes-in-version-10-release-date-2026-07-01}

### ストレージの変更点:

* 新しいイベントタイプ `users.canvas.costep.Send` を追加しました。

* 新しいイベントタイプ `users.UserDeleteRequest` を追加しました。

* 新しいイベントタイプ `users.UserOrphan` を追加しました。

* イベントタイプ `users.messages.rcs.Abort` のフィールド変更:
    * 新しい `string` フィールド `canvas_id` を追加: このイベントが属するキャンバスのAPI ID

* イベントタイプ `users.messages.rcs.Click` のフィールド変更:
    * 新しい `string` フィールド `canvas_id` を追加: このイベントが属するキャンバスのAPI ID

* イベントタイプ `users.messages.rcs.Delivery` のフィールド変更:
    * 新しい `string` フィールド `canvas_id` を追加: このイベントが属するキャンバスのAPI ID

* イベントタイプ `users.messages.rcs.InboundReceive` のフィールド変更:
    * 新しい `string` フィールド `canvas_id` を追加: このイベントが属するキャンバスのAPI ID

* イベントタイプ `users.messages.rcs.Read` のフィールド変更:
    * 新しい `string` フィールド `canvas_id` を追加: このイベントが属するキャンバスのAPI ID

* イベントタイプ `users.messages.rcs.Rejection` のフィールド変更:
    * 新しい `string` フィールド `canvas_id` を追加: このイベントが属するキャンバスのAPI ID

* イベントタイプ `users.messages.rcs.Send` のフィールド変更:
    * 新しい `string` フィールド `canvas_id` を追加: このイベントが属するキャンバスのAPI ID

## バージョン9の変更点（リリース日：2026-06-03） {#changes-in-version-9-release-date-2026-06-03}

### ストレージの変更点:

* イベントタイプ `users.messages.email.Send` のフィールド変更:
    * 新しい `string` フィールド `from_domain` を追加: メールの送信ドメイン

## バージョン8の変更点（リリース日：2026年5月6日） {#changes-in-version-8-release-date-2026-05-06}

### ストレージの変更点:

* 新しいイベントタイプ `users.messages.banner.Dismiss` が追加されました。

* イベントタイプ `users.messages.whatsapp.Abort` のフィールド変更:
    * 新しい `string` フィールド `bsuid` が追加されました: このイベントに関連付けられた受信者のWhatsApp Business-Scoped User IDです。

* イベントタイプ `users.messages.whatsapp.Delivery` のフィールド変更:
    * 新しい `string` フィールド `bsuid` が追加されました: このイベントに関連付けられた受信者のWhatsApp Business-Scoped User IDです。

* イベントタイプ `users.messages.whatsapp.Failure` のフィールド変更:
    * 新しい `string` フィールド `bsuid` が追加されました: このイベントに関連付けられた受信者のWhatsApp Business-Scoped User IDです。

* イベントタイプ `users.messages.whatsapp.InboundReceive` のフィールド変更:
    * 新しい `string` フィールド `bsuid` が追加されました: メッセージの送信元であるユーザーのWhatsApp Business-Scoped User IDです。
    * フィールド `user_phone_number` は*任意*になりました。

* イベントタイプ `users.messages.whatsapp.Read` のフィールド変更:
    * 新しい `string` フィールド `bsuid` が追加されました: このイベントに関連付けられた受信者のWhatsApp Business-Scoped User IDです。

* イベントタイプ `users.messages.whatsapp.Retry` のフィールド変更:
    * 新しい `string` フィールド `bsuid` が追加されました: このイベントに関連付けられた受信者のWhatsApp Business-Scoped User IDです。

* イベントタイプ `users.messages.whatsapp.Send` のフィールド変更:
    * 新しい `string` フィールド `bsuid` が追加されました: このイベントに関連付けられた受信者のWhatsApp Business-Scoped User IDです。

## バージョン7の変更点（リリース日 2026-04-01） {#changes-in-version-7-release-date-2026-04-01}

### ストレージの変更点:

* 新しいイベントタイプ `users.profile.Update` を追加しました。

* イベントタイプ `users.messages.banner.Abort` のフィールド変更:
    * 新しい `string` フィールド `canvas_name` を追加: キャンバスの名前
    * 新しい `string` フィールド `canvas_step_name` を追加: キャンバスステップの名前
    * 新しい `string` フィールド `canvas_variation_name` を追加: このユーザーが受信したキャンバスバリエーションの名前
    * 新しい `string` フィールド `canvas_id` を追加: このイベントが属するキャンバスのAPI ID
    * 新しい `string` フィールド `canvas_step_id` を追加: このイベントが属するキャンバスステップのAPI ID
    * 新しい `string` フィールド `canvas_step_message_variation_id` を追加: このユーザーが受信したキャンバスステップメッセージバリエーションのAPI ID
    * 新しい `string` フィールド `canvas_variation_id` を追加: このイベントが属するキャンバスバリエーションのAPI ID

* イベントタイプ `users.messages.banner.Click` のフィールド変更:
    * 新しい `string` フィールド `canvas_id` を追加: このイベントが属するキャンバスのAPI ID
    * 新しい `string` フィールド `canvas_step_id` を追加: このイベントが属するキャンバスステップのAPI ID
    * 新しい `string` フィールド `canvas_name` を追加: キャンバスの名前
    * 新しい `string` フィールド `canvas_step_name` を追加: キャンバスステップの名前
    * 新しい `string` フィールド `canvas_step_message_variation_id` を追加: このユーザーが受信したキャンバスステップメッセージバリエーションのAPI ID
    * 新しい `string` フィールド `canvas_variation_id` を追加: このイベントが属するキャンバスバリエーションのAPI ID
    * 新しい `string` フィールド `canvas_variation_name` を追加: このユーザーが受信したキャンバスバリエーションの名前

* イベントタイプ `users.messages.banner.Impression` のフィールド変更:
    * 新しい `string` フィールド `canvas_id` を追加: このイベントが属するキャンバスのAPI ID
    * 新しい `string` フィールド `canvas_step_id` を追加: このイベントが属するキャンバスステップのAPI ID
    * 新しい `string` フィールド `canvas_name` を追加: キャンバスの名前
    * 新しい `string` フィールド `canvas_step_name` を追加: キャンバスステップの名前
    * 新しい `string` フィールド `canvas_step_message_variation_id` を追加: このユーザーが受信したキャンバスステップメッセージバリエーションのAPI ID
    * 新しい `string` フィールド `canvas_variation_id` を追加: このイベントが属するキャンバスバリエーションのAPI ID
    * 新しい `string` フィールド `canvas_variation_name` を追加: このユーザーが受信したキャンバスバリエーションの名前

## バージョン6の変更点（リリース日：2026年3月4日） {#changes-in-version-6-release-date-2026-03-04}

### Storageの変更点:

* イベントタイプ `agentconsole.AgentExecuted` のフィールド変更:
    * 新しい `string` フィールド `error` を追加: エラーの説明

* イベントタイプ `agentconsole.ToolInvocation` のフィールド変更:
    * 新しい `string` フィールド `request_id` を追加: このLLMリクエスト全体および完全な実行に対する一意のID

* イベントタイプ `users.messages.rcs.InboundReceive` のフィールド変更:
    * 新しい `string` フィールド `canvas_variation_name` を追加: このユーザーが受信したキャンバスバリエーションの名前

## バージョン5の変更点（リリース日：2026年2月4日） {#changes-in-version-5-release-date-2026-02-04}

### ストレージの変更点:

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

## バージョン4の変更点（リリース日：2026年1月7日） {#changes-in-version-4-release-date-2026-01-07}

### ストレージの変更点:

* イベントタイプ `users.behaviors.pushnotification.TokenStateChange` のフィールド変更:
    * 新しい `string` フィールド `push_token` を追加: イベントのプッシュトークン

* イベントタイプ `users.messages.pushnotification.Bounce` のフィールド変更:
    * 新しい `string` フィールド `push_token` を追加: イベントのプッシュトークン

* イベントタイプ `users.messages.pushnotification.Send` のフィールド変更:
    * 新しい `string` フィールド `push_token` を追加: イベントのプッシュトークン

* イベントタイプ `users.messages.rcs.Click` のフィールド変更:
    * 新しい `string` フィールド `canvas_variation_name` を追加: このユーザーが受信したキャンバスバリエーションの名前
    * フィールド `user_phone_number` は*オプション*になりました。

* イベントタイプ `users.messages.rcs.InboundReceive` のフィールド変更:
    * フィールド `user_id` は*オプション*になりました。

* イベントタイプ `users.messages.rcs.Rejection` のフィールド変更:
    * 新しい `string` フィールド `canvas_step_message_variation_id` を追加: このユーザーが受信したキャンバスステップメッセージバリエーションのAPI ID

## バージョン3の変更点（リリース日：2025年10月8日） {#changes-in-version-3-release-date-2025-10-08}

### ストレージの変更点：

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

* イベントタイプ `users.messages.sms.Delivery` のフィールド変更：
    * 新しい `boolean` フィールド `is_sms_fallback` を追加：RCS メッセージが拒否されたために SMS フォールバックメッセージが送信されたことを示します。このメッセージは、配信、配信失敗、または拒否のいずれかの結果になる可能性があります。送信 ID とディスパッチ ID を介して RCS Rejection イベントにリンクできます。

* イベントタイプ `users.messages.sms.DeliveryFailure` のフィールド変更：
    * 新しい `boolean` フィールド `is_sms_fallback` を追加：RCS メッセージが拒否されたために SMS フォールバックメッセージが送信されたことを示します。このメッセージは、配信、配信失敗、または拒否のいずれかの結果になる可能性があります。送信 ID とディスパッチ ID を介して RCS Rejection イベントにリンクできます。

* イベントタイプ `users.messages.sms.Rejection` のフィールド変更：
    * 新しい `boolean` フィールド `is_sms_fallback` を追加：RCS メッセージが拒否されたために SMS フォールバックメッセージが送信されたことを示します。このメッセージは、配信、配信失敗、または拒否のいずれかの結果になる可能性があります。送信 ID とディスパッチ ID を介して RCS Rejection イベントにリンクできます。

* イベントタイプ `users.messages.whatsapp.Delivery` のフィールド変更：
    * 新しい `string` フィールド `flow_id` を追加：WhatsApp マネージャーにおけるフローの一意の ID です。メッセージに WhatsApp フローに応答するための CTA が含まれている場合に存在します。
    * 新しい `string` フィールド `template_name` を追加：[PII] WhatsApp マネージャーにおけるテンプレートの名前です。テンプレートメッセージを送信する場合に存在します。
    * 新しい `string` フィールド `message_id` を追加：Meta がこのメッセージに対して生成した一意の ID です。

* イベントタイプ `users.messages.whatsapp.Failure` のフィールド変更：
    * 新しい `string` フィールド `message_id` を追加：Meta がこのメッセージに対して生成した一意の ID です。
    * 新しい `string` フィールド `template_name` を追加：[PII] WhatsApp マネージャーにおけるテンプレートの名前です。テンプレートメッセージを送信する場合に存在します。
    * 新しい `string` フィールド `flow_id` を追加：WhatsApp マネージャーにおけるフローの一意の ID です。メッセージに WhatsApp フローに応答するための CTA が含まれている場合に存在します。

* イベントタイプ `users.messages.whatsapp.InboundReceive` のフィールド変更：
    * 新しい `string` フィールド `catalog_id` を追加：受信メッセージで商品が参照されている場合のカタログ ID です。それ以外の場合は空です。
    * 新しい `string` フィールド `product_id` を追加：受信メッセージで商品が参照されている場合の商品 SKU です。それ以外の場合は空です。
    * 新しい `string` フィールド `flow_id` を追加：WhatsApp マネージャーにおけるフローの一意の ID です。ユーザーが WhatsApp フローに応答している場合に存在します。
    * 新しい `string` フィールド `flow_response_json` を追加：[PII] ユーザーが応答したフォームの値です。ユーザーが WhatsApp フローに応答している場合に存在します。
    * 新しい `string` フィールド `message_id` を追加：Meta がこのメッセージに対して生成した一意の ID です。
    * 新しい `string` フィールド `in_reply_to` を追加：このメッセージが返信先としたメッセージの message_id です。

* イベントタイプ `users.messages.whatsapp.Read` のフィールド変更：
    * 新しい `string` フィールド `template_name` を追加：[PII] WhatsApp マネージャーにおけるテンプレートの名前です。テンプレートメッセージを送信する場合に存在します。
    * 新しい `string` フィールド `message_id` を追加：Meta がこのメッセージに対して生成した一意の ID です。
    * 新しい `string` フィールド `flow_id` を追加：WhatsApp マネージャーにおけるフローの一意の ID です。メッセージに WhatsApp フローに応答するための CTA が含まれている場合に存在します。

* イベントタイプ `users.messages.whatsapp.Send` のフィールド変更：
    * 新しい `string` フィールド `flow_id` を追加：WhatsApp マネージャーにおけるフローの一意の ID です。メッセージに WhatsApp フローに応答するための CTA が含まれている場合に存在します。
    * 新しい `string` フィールド `template_name` を追加：[PII] WhatsApp マネージャーにおけるテンプレートの名前です。テンプレートメッセージを送信する場合に存在します。
    * 新しい `string` フィールド `message_id` を追加：Meta がこのメッセージに対して生成した一意の ID です。

## バージョン2の変更点（リリース日未定） {#changes-in-version-2-release-date-null}

### ストレージの変更点:

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