---
nav_title: FAQ
article_title: レート制限とフリークエンシーキャップ FAQ
page_order: 0
page_type: FAQ
description: "この記事では、レート制限とフリークエンシーキャップに関するよくある質問への回答を提供します。"
tool: Campaigns

---

# よくある質問 {#frequently-asked-questions}

> この記事では、レート制限とフリークエンシーキャップに関するよくある質問への回答を提供します。

### アクティブなCanvasの送信スロットルを変更した場合、すでにCanvas内にいるユーザーに影響しますか？ {#if-i-change-a-send-throttle-on-an-active-canvas-does-it-affect-users-already-in-the-canvas}

はい。Canvasのレート制限を増減すると、更新された制限は新しいメッセージに対して有効になります。更新がCanvas全体に反映されるまでに若干の遅延が生じる場合があります。

### ユーザーがCanvasのメッセージステップに到達したが、グローバルフリークエンシーキャップを超えている場合はどうなりますか？ {#what-happens-if-a-user-reaches-a-canvas-message-step-but-is-over-the-global-frequency-cap}

ユーザーはキャップされたチャネルでの送信を受信しませんが、メッセージステップの進行ルールには引き続き従います。メッセージステップは、グローバルフリークエンシーキャップによりメッセージが送信されなかった場合でもユーザーを進行させるため、次のキャンバスステップに進みます。進行ケースの完全なリストについては、[ユーザーの進行方法]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step/#how-users-advance)を参照してください。

### Canvas内でフリークエンシーキャップされたユーザーを特定するにはどうすればよいですか？ {#how-can-i-identify-users-who-were-frequency-capped-in-a-canvas}

フリークエンシーキャップされたユーザーは、そのステップの送信イベントを生成しません。これらのユーザーを特定するには、[Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/)を使用して、`abort_type`が`frequency_capped`であるメッセージ中止イベントを追跡できます。または、[セグメントエクステンション]({{site.baseurl}}/user_guide/audience/segments/segment_extension/)を作成して、Canvasに入ったが期待されるメッセージを受信しなかったユーザーを分析できます。

### 「1日あたり」のグローバルフリークエンシーキャップでは、暦日とタイムゾーンはどのように使用されますか？ {#how-are-calendar-days-and-time-zones-used-for-per-day-global-frequency-caps}

グローバルフリークエンシーキャップはユーザーのタイムゾーンを使用し、ローリング24時間ではなく暦日でカウントします。例については、[配信ルール]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/#delivery-rules)を参照してください。

### グローバルフリークエンシーキャップはトリガーされたアプリ内メッセージに適用されますか？ {#does-global-frequency-capping-apply-to-triggered-in-app-messages}

いいえ、グローバルフリークエンシーキャップはプッシュ、メール、SMS、Webhook、WhatsApp、LINEメッセージにのみ適用されます。

### フリークエンシーキャップは受信したCampaignを制限しますか、それとも送信内の個別メッセージを制限しますか？ {#does-frequency-capping-limit-campaigns-received-or-individual-messages-inside-a-send}

フリークエンシーキャップはディスパッチごとに適用されます。各CampaignまたはCanvasステップの送信がキャップにカウントされ、送信内の各バリアントやプラットフォームではありません。詳細については、[配信ルール]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/#delivery-rules)を参照してください。

### 複数のメッセージが同時に対象となり、キャップ内に収まるのが一部のみの場合、どのメッセージが送信されますか？ {#if-several-messages-are-eligible-at-the-same-time-and-only-some-fit-under-the-cap-which-messages-send}

Brazeは上限まで送信します。同じ時間枠内で複数の送信が競合する場合、最初に処理されたメッセージがキャップにカウントされます。その時間枠内の残りの送信はキャップされます。

### 失敗したWebhookはグローバルフリークエンシーキャップにカウントされますか？ {#do-failed-webhooks-count-toward-the-global-frequency-cap}

いいえ。Webhookは、Brazeが配信成功を記録した時点でキャップにカウントされます。Webhookの失敗レスポンス（例：`4xx`や`5xx`ステータスコード）はキャップにカウントされません。