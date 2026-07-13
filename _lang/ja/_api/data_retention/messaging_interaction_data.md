---
nav_title: "メッセージングインタラクションデータ"
article_title: "メッセージングインタラクションデータ"
alias: "/messaging_interaction_data/"
page_order: 1
description: "このリファレンス記事では、キャンペーンおよびキャンバスのインタラクションデータとその利用可能性について説明します。"
page_type: reference
---

# メッセージングインタラクションデータの利用可能性について {#about-messaging-interaction-data-availability}

> キャンペーンおよびキャンバスのメッセージングインタラクションデータについて、Brazeがデータを保持する期間やリターゲティングに使用する機能を含めて説明します。

## メッセージングインタラクションデータとは {#what-is-messaging-interaction-data}

メッセージングインタラクションデータとは、ユーザーが受信したキャンペーンやキャンバスとどのようにやり取りしたかを示すデータです（例：ユーザーがキャンペーンAを開封した、ユーザーがバリアントAを受信した、など）。このデータはリターゲティングに使用されます。

## メッセージングインタラクションデータはいつ利用可能ですか {#when-is-messaging-interaction-data-available}

インタラクションデータは常に利用可能です。アクティブなキャンペーンおよびキャンバスの場合、インタラクションデータは常にリアルタイムで利用できます。

停止されたキャンペーンおよびキャンバスの場合、そのインタラクションデータは、アクティブなキャンペーンまたはキャンバスのリターゲティングフィルターで使用されていない限り、3か月後に期限切れになります。期限切れのインタラクションデータは長期ストレージに移動され、以下に説明するプロセスを使用して復元しない限り利用できません。

期限切れのインタラクションデータは削除されることはなく、いつでも復元できます。

### インタラクションデータを使用する機能 {#features-that-use-interaction-data}

以下の機能はメッセージングインタラクションデータを使用します。

- 特定のキャンペーンまたはキャンバスでリターゲティングするリターゲティングフィルター
    - Clicked Alias in キャンペーン
    - Clicked Alias in キャンバス Step
    - Clicked/Opened キャンペーン
    - Clicked/Opened Step
    - Converted From キャンペーン
    - Converted From キャンバス
    - Entered キャンバス Variation
    - In キャンペーン Control Group
    - In キャンバス Control Group
    - Last Received Message from Specific キャンペーン
    - Last Received Message from Specific キャンバス Step
    - Received キャンペーン Variant
    - Received Message from キャンペーン
    - Received Message from キャンバス Step
- 特定のタグを持つキャンペーンまたはキャンバスでリターゲティングするリターゲティングフィルター
    - Received Message from キャンペーン or キャンバス with Tag
    - Clicked/Opened キャンペーン or キャンバス With Tag
    - Last Received Message from キャンペーン or キャンバス With Tag
- ユーザープロファイルの**キャンペーン Received**および**キャンバス Messages Received**リスト
- `/users/export`エンドポイント
- キャンペーンおよびキャンバスサマリーページの**ユーザーデータ**CSVエクスポート

これらの機能は、期限切れのインタラクションデータを結果に含めません。期限切れのインタラクションデータをこれらの機能の結果に含めるには、期限切れのデータを持つキャンペーンまたはキャンバスを復元してください。

例えば、インタラクションデータが期限切れの場合、キャンバスを起動できません。つまり、キャンバスにチームを追加するなどの編集を保存できません。

### インタラクションデータを使用しない機能 {#features-that-dont-use-interaction-data}

以下の機能はメッセージングインタラクションデータを**使用しません**。つまり、これらの機能はメッセージングインタラクションデータの期限切れの影響を受けません。

- キャンペーンおよびキャンバスの設定
- キャンペーンおよびキャンバスの分析
- 分析レポート（レポートビルダー、クエリビルダー、エンゲージメントレポートなど）
- Currents
- Snowflake Data Share
- セグメントエクステンション
- データポイント
- 以下のリターゲティングフィルター：
    - Clicked Alias in Any キャンペーン or キャンバス Step
    - Feature Flags
    - Hard Bounced
    - Has Marked You As Spam
    - Has Never Received a Message from キャンペーン or キャンバス Step
    - Invalid Phone Number
    - Last Engaged With Message
    - Last Enrolled in Any Control Group
    - Last In App Message Impression
    - Last Received Any Message
    - Last Received Email
    - Last Received Push
    - Last Received SMS
    - Last Received Webhook
    - Last Received WhatsApp
    - Last Sent Specific SMS Inbound Keyword Category
    - Last Viewed News Feed
    - News Feed View Count

## メッセージングインタラクションデータを復元するには {#how-do-i-restore-messaging-interaction-data}

インタラクションデータを復元するには、以下の手順に従ってください。

1. 期限切れのキャンペーンまたはキャンバスに移動します。
2. キャンペーンまたはキャンバスのランディングページの上部にあるバナーで**Restore interaction data**を選択します。

また、**キャンペーン**ページからキャンペーンを選択し、**Restore interaction data**を選択することで、複数のキャンペーンのインタラクションデータを復元することもできます。

インタラクションデータの復元にかかる時間はさまざまですが、ほとんどの場合、5〜15分程度です。復元が完了すると、メールが届きます。

### タグによる復元 {#restoring-by-tag}

特定のタグを持つ期限切れのキャンペーンまたはキャンバスのインタラクションデータを復元することもできます。

1. **キャンペーン**または**キャンバス**ページに移動し、該当するタグで検索します。
2. キャンペーンまたはキャンバスを選択します。
3. **Restore interaction data**を選択して、それらのキャンペーンまたはキャンバスのデータを復元します。

さらに3か月間非アクティブな状態が続くと、これらのキャンペーンまたはキャンバスは再び期限切れになります。

### タグによるリターゲティング {#retargeting-by-tag}

タグによるリターゲティングを行うリターゲティングフィルターを使用するキャンペーンは、期限切れの対象から除外されません。タグによるリターゲティングを行うリターゲティングフィルターには以下が含まれます。

- Received Message from キャンペーン or キャンバス with Tag
- Clicked/Opened キャンペーン or キャンバス With Tag
- Last Received Message from キャンペーン or キャンバス With Tag

## 過去のメッセージングインタラクションデータの利用可能性 {#when-was-messaging-interaction-data-available-in-the-past}

以前は、キャンペーンまたはキャンバスが以下の条件を満たした場合、メッセージインタラクションデータは削除されていました。

- 25暦月間メッセージを送信していない、かつ
- アクティブなキャンペーン、キャンバス、またはContent Cardsのリターゲティングに使用されていない。

以前にメッセージングインタラクションデータが削除されたキャンペーンおよびキャンバスは、キャンペーン、キャンバス、およびセグメントのリターゲティングフィルターで使用できません。

## トラブルシューティング {#troubleshooting}

期限切れのインタラクションデータを持つキャンペーン、キャンバス、またはContent Cardsを再開またはアーカイブ解除しようとすると、以下のエラーメッセージが表示される場合があります。

| エラーメッセージ | 表示されるタイミング | トラブルシューティング |
| --- | --- | --- |
| 「Can't resume キャンバス because at least one キャンバス is using filters or segments that have expired data. Remove these and try again.」 | 期限切れのインタラクションデータを持つフィルターまたはセグメントを使用する1つ以上のキャンバスを再開しようとした場合（一括アクション） | フィルターで参照されているキャンペーンまたはキャンバスの[インタラクションデータを復元する](#how-do-i-restore-messaging-interaction-data)か、影響を受けるフィルターをキャンバスから削除します |
| 「Can't resume {name} because it is using filters or segments that have expired data. Remove these and try again.」 | 期限切れのインタラクションデータを持つフィルターまたはセグメントを使用する単一のキャンバスを再開しようとした場合 | フィルターで参照されているキャンペーンまたはキャンバスの[インタラクションデータを復元する](#how-do-i-restore-messaging-interaction-data)か、影響を受けるフィルターをキャンバスから削除します |
| 「Resume is only available for stopped キャンバス with available interaction data」 | 一括アクションメニューからキャンバスを再開しようとしたが、キャンバスのインタラクションデータが期限切れの場合 | キャンバスの[インタラクションデータを復元します](#how-do-i-restore-messaging-interaction-data) |
| 「You can't resume these キャンペーン. One or more キャンペーン include expired filters.」 | 期限切れのインタラクションデータを持つフィルターを使用する1つ以上のキャンペーンを再開しようとした場合 | フィルターで参照されているキャンペーンまたはキャンバスの[インタラクションデータを復元する](#how-do-i-restore-messaging-interaction-data)か、影響を受けるフィルターをキャンペーンから削除します |
| 「You can't unarchive these Cards. One or more Cards include expired filters.」 | 期限切れのインタラクションデータを持つフィルターを使用する1つ以上のContent Cardsをアーカイブ解除しようとした場合 | フィルターで参照されているキャンペーンまたはキャンバスの[インタラクションデータを復元する](#how-do-i-restore-messaging-interaction-data)か、影響を受けるフィルターをカードから削除します |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="一般的なエラーメッセージ" }