---
nav_title: キャンペーンを作成
article_title: キャンペーンを作成
page_order: 1
page_type: tutorial
description: "作成から起動まで、マルチチャネル送信を含むBrazeメッセージングキャンペーンの作成方法、配信のスケジュール、ターゲットオーディエンスの設定、コンバージョンイベントの割り当て、テスト送信、起動について説明します。"
tool: Campaigns
---

# キャンペーンを作成 {#create-a-campaign}

> 1つまたは複数のサポートされているチャネルで、単一のメッセージングステップで消費者にリーチしたい場合はキャンペーンを使用します。マルチステップのジャーニーには、[キャンバス]({{site.baseurl}}/user_guide/messaging/canvas)を使用してください。

## 前提条件 {#prerequisites}

キャンペーンを作成して起動するには、「キャンペーンを編集」と「キャンペーンを起動」の権限が必要です。ワークスペース権限の完全なリストとダッシュボードでの表示方法については、[権限]({{site.baseurl}}/user_guide/administer/global/user_management/permissions)を参照してください。

### 始める前に {#before-you-begin}

- メッセージを受け取るべきユーザーを定義する[セグメント]({{site.baseurl}}/user_guide/audience/segments)を作成または選択します。
- メッセージングチャネル、配信タイプ、コンバージョン目標がユースケースに合っているか、[キャンペーンの基本情報]({{site.baseurl}}/user_guide/messaging/campaigns/campaign_basics)を確認します。
- 配信、ターゲティング、コンバージョンのガイド付きウォークスルーについては、[キャンペーン Setup](https://learning.braze.com/campaign-setup-delivery-targeting-conversions) Brazeラーニングコースを受講してください。

## キャンペーンコンポーザー {#campaign-composer}

キャンペーンコンポーザーでは、配信、オーディエンス、コンバージョン、起動設定を定義します。続行する前に、単一チャネルまたはマルチチャネルのキャンペーンのどちらを作成するかを決めてください。

{% tabs %}
{% tab 単一チャネル %}

単一チャネルキャンペーンは、1回の起動につき1つのメッセージングチャネルでユーザーにリーチします。

### 違い {#whats-different}

#### コンバージョンとレポート {#single-channel-conversions}

単一チャネルキャンペーンの場合、Brazeはそのチャネルからの送信に対して、キャンペーンに割り当てた[コンバージョンイベント]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events)を追跡します。アトリビューションウィンドウとカウントルールについては、[コンバージョントラッキングルール]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events#conversion-tracking-rules)を参照してください。

ワークスペースの[フリークエンシーキャップ]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping)と送信制限は引き続き適用されます。

### 単一チャネルキャンペーンを作成する {#create-a-single-channel-campaign}

キャンペーンを作成するには：

1. **メッセージング** > **キャンペーン** に移動します。
2. **キャンペーンを作成**を選択します。
3. ユースケースに合った[チャネル]({{site.baseurl}}/user_guide/channels)を選択します。
4. [作成ステップ](#step-1-compose-messages)で、そのチャネルのコピーを作成してプレビューします。

各キャンペーンは一度に1つのチャネルタイプを使用します。クリエイティブの分割比較や[ABテスト]({{site.baseurl}}/user_guide/messaging/ab_testing)を実行したい場合は、バリアントを追加してください。

{% endtab %}
{% tab マルチチャネル %}

マルチチャネルキャンペーンは、1回の起動で複数のメッセージングチャネルを通じてユーザーにリーチします。たとえば、メールとプッシュ通知を同時に送信できます。

{% alert note %}
[In-App Messages]({{site.baseurl}}/user_guide/channels/in_app_messages)はマルチチャネルキャンペーンでは利用できません。代わりに単一チャネルキャンペーンまたはキャンバスを作成してください。
{% endalert %}

### 違い

#### コントロールグループ {#multichannel-control-groups}

キャンペーンのコントロールグループは、1つのチャネル内でバリアントを比較します（たとえば、メールAとメールBの比較）。1つのマルチチャネルキャンペーン内でチャネル全体を比較するためには使用されません。チャネル、クリエイティブ、またはタイミングをジャーニー全体でテストするには、[キャンバス]({{site.baseurl}}/user_guide/messaging/canvas)を使用してください。

#### コンバージョンとレポート {#multichannel-conversions}

マルチチャネルキャンペーンの場合、Brazeはチャネルごとに[コンバージョンイベント]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events)を追跡します。ユーザーが複数のチャネルでメッセージを受信した後にコンバージョンした場合、Brazeはそのコンバージョンをそれらのチャネルにアトリビューションできます。コンバージョン数は*ユニークユーザー*を超える場合があり、レートは100%を超える場合があります。完全なルールについては、[コンバージョントラッキングルール]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events#conversion-tracking-rules)を参照してください。

チャネルをまたぐ送信のレート制限については、[マルチチャネルキャンペーンとキャンバス]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#multichannel-campaigns-and-canvases)で説明されています。ワークスペース全体のルール（マルチチャネル送信がキャップにどのようにカウントされるかを含む）については、[フリークエンシーキャップ]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping)を参照してください。

### マルチチャネルキャンペーンを作成する {#create-a-multichannel-campaign}

1. **メッセージング** > **キャンペーン** に移動します。
2. **キャンペーンを作成**を選択します。
3. **マルチチャネル** を選択します。
4. [作成ステップ](#step-1-compose-messages)で、**チャネルを追加** を選択し、必要な各チャネルを選択します。各チャネルのコピーを作成する際に、チャネルアイコンを選択してコンポーザーを切り替えます。

{% endtab %}
{% endtabs %}

## ステップ 1: メッセージを作成する {#step-1-compose-messages}

### キャンペーンの詳細 {#campaign-details}

以下のフィールドを使用して、チームがキャンペーンを見つけて管理するのに役立つメタデータを記録します。

| フィールド | 目的 |
| --- | --- |
| 名前 | キャンペーンの目標を反映した明確な名前を使用します。 |
| 説明 | オプション。コラボレーターのために意図やブリーフへのリンクを説明します。 |
| チーム | オプション。適切なグループがこの送信を編集またはレポートできるように[チーム]({{site.baseurl}}/user_guide/administer/global/user_management/teams)を割り当てます。 |
| タグ | オプション。リストや[レポートビルダー]({{site.baseurl}}/user_guide/analytics/reports/report_builder)などのツールでフィルタリングするために[タグ]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags)を追加します。 |
| キャンペーン ID | コンポーザーまたはサマリーに表示される場合、特定のキャンペーンを参照するAPI呼び出し、レポート、統合のためにこの識別子をコピーします。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="キャンペーンの詳細" }

### チャネルとエディター {#channels-and-editors}

このステップでチャネル固有のコンテンツを作成します。詳細なガイダンスについては、[チャネル]({{site.baseurl}}/user_guide/channels)を参照し、選択したチャネルの記事を開いてください。

### バリアント {#variants}

クリエイティブや配信の分割を比較したい場合は、バリアントを追加します。実験とコントロールの背景については、[多変量テストとABテスト]({{site.baseurl}}/user_guide/messaging/ab_testing)を参照してください。

{% alert tip %}
各バリアントが類似した本文コンテンツを使用する場合は、追加のバリアントを追加する**前に**メッセージを作成してください。次に、**バリアントを追加**メニューから**バリアントからコピー** を使用して、バリアントやチャネル間で作業を再利用します。
{% endalert %}

## ステップ 2: 配信をスケジュールする {#step-2-schedule-delivery}

ユーザーがキャンペーンを受信する資格を得るタイミングを選択します：

| 配信タイプ | 概要 |
| --- | --- |
| [スケジュール配信]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/scheduled_delivery) | 指定した時間またはケイデンスで送信します。 |
| [アクションベースの配信]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery) | ユーザーが行動を実行するか、定義した条件を満たしたときに送信します。 |
| [APIトリガー配信]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery) | システムがBrazeを呼び出して、対象ユーザーに対してキャンペーンをトリガーしたときに送信します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ステップ 2: 配信をスケジュールする" }

Braze全体のスケジューリングの概念については、[キャンペーンをスケジュールする]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign)を参照してください。

### 配信コントロール {#delivery-controls}

配信タイプに応じて、[再適格性]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility)（ユーザーが再びキャンペーンに入れるかどうか）を調整し、ワークスペースの[フリークエンシーキャップ]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping)ルールを適用できます。また、制限された時間枠中にメッセージが送信されないように[クワイエットアワー]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours)を設定することもできます。

## ステップ 3: ターゲットオーディエンスを設定する {#step-3-target-audiences}

**ターゲットオーディエンス** で、キャンペーンを受信する資格のあるユーザーを定義します。完全なターゲティングオプション、UIウォークスルー、スクリーンショットについては、[ユーザーをターゲットにする]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users)を参照してください。

### ターゲティングオプション {#targeting-options}

このセクションでは、セグメントまたはフィルターを選択してオーディエンスを絞り込むことで、ユーザーをターゲットにできます。対象ユーザーは、**配信をスケジュール** ステップで定義したトリガーまたは条件を満たす必要があります。ターゲットオーディエンスは待合室のようなもので、次のアクションが発生したときに前に進めるのは、すでに中にいる人だけです。

ワークスペースの[抑制リスト]({{site.baseurl}}/user_guide/audience/suppression_lists)は、このキャンペーンに例外を許可しない限り、リストに登録されたユーザーを自動的に除外します。

### オーディエンスの概要 {#audience-summary}

セグメントまたはフィルターを追加した後、**オーディエンスの概要** はそのセグメント母集団の概要をプレビューとして表示します。これには、選択したチャネルを通じてリーチ可能なセグメント内のユーザー数が含まれます。リーチ可能な数は、ワークスペースデータ、チャネル設定、フィルターを反映しています。正確なセグメントメンバーシップは常にメッセージ送信前に計算されることに注意してください。非常に大きなオーディエンスの場合、Brazeは正確な統計を計算するまで推定値を表示する場合があります。

### ユーザー検索 {#user-lookup}

セグメントまたはフィルターを追加した後、ユーザーを検索してセグメント条件に一致するかどうかを確認することで、オーディエンスが期待どおりに設定されているかテストできます。これを行うには、**ユーザー検索** セクションでユーザーの`external_id`または`braze_id`を検索します。ここではメールアドレスで検索することはできません。詳細については、[セグメントのテスト]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment#testing-segments)を参照してください。

ユーザーがセグメント、フィルター、アプリの条件に一致する場合、アラートがその旨を表示します。ユーザーがセグメント、フィルター、またはアプリの条件の一部またはすべてに一致しない場合、トラブルシューティングのために不足している条件がリストされます。

### これらのユーザーに送信する {#send-to-these-users}

サブスクリプションベースのチャネル（メール、SMSなど）の場合、**これらのユーザーに送信** を使用して、購読中でメールにオプトインしているユーザーなど、特定のサブスクリプションステータスを持つユーザーにのみキャンペーンを送信します。

### 送信量を制限する {#limit-send-volume}

メッセージを受信するユーザーの総数を制限できます。これはキャンペーンフィルターとは独立したチェックとして機能します。詳細については、[最大ユーザーキャップの設定]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#setting-a-maximum-user-cap)を参照してください。

### このキャンペーンの送信レートを制限する {#limit-the-rate-at-which-this-campaign-sends}

大規模なキャンペーンがユーザーアクティビティの急増を引き起こし、サーバーに過負荷をかけることが予想される場合、メッセージ送信の1分あたりのレート制限を指定できます。これにより、Brazeは1分以内にレート制限の設定を超えて送信しません。詳細については、[配信速度のレート制限]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting)を参照してください。

### ABテスト {#ab-testing}

単一チャネルをターゲットとするキャンペーンに対して、複数のデバイスを含む場合でも、[多変量テストまたはABテスト]({{site.baseurl}}/user_guide/messaging/ab_testing)を作成できます。たとえば、プッシュキャンペーンで多変量テストまたはABテストを使用したい場合、iOSデバイスのみまたはAndroidデバイスのみをターゲットにできます。同じキャンペーン内で両方のデバイスタイプをターゲットにすることはできません。

1回送信がスケジュールされたプッシュ、メール、Webhookのキャンペーンでは、[最適化]({{site.baseurl}}/user_guide/messaging/ab_testing/optimizations)も使用できます。最適化は、ABテストからターゲットオーディエンスの一部を予約し、最初のテストの結果に基づいて2回目の最適化された送信のために保持します。

## ステップ 4: コンバージョンイベントを割り当てる {#step-4-assign-conversion-events}

[コンバージョンイベント]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events)は、ユーザーがキャンペーンを受信した後（またはコントロールグループに入った後）の成果を測定します。Brazeのデフォルトは、短い時間枠（3日間）内の**セッション開始**です。KPIに合ったコンバージョンイベントを定義でき、キャンペーンごとに最大4つのイベントを設定できます。

起動後は、[コンバージョンダッシュボード]({{site.baseurl}}/user_guide/analytics/dashboards/conversions)を使用して、複数のキャンペーンまたはキャンバス全体のコンバージョントレンドを分析し、チャネルを比較し、日付範囲、アトリビューション方法、内訳を1か所で調整できます。

{% alert important %}
キャンペーン起動後にコンバージョンイベントを追加または削除することはできません。起動前にイベントを確認してください。
{% endalert %}

## ステップ 5: サマリーを確認して起動する {#step-5-review-summary-and-launch}

**レビューサマリー** ステップでは、スケジュール、オーディエンス、バリアント、メッセージングの選択内容が表示されます。キャンペーンを起動する前に：

1. セグメント、バリアント、配信設定が意図と一致していることを確認します。
2. テストデバイスまたは内部受信者で、レンダリングと動作を検証するために[テストメッセージを送信]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages)します。

準備ができたら、**キャンペーンを起動** を選択します。

### 承認 {#approvals}

ワークスペースで承認を使用している場合、キャンペーンを承認する権限を持つチームメイトが起動前に承認する必要があります。詳細については、[キャンペーンとキャンバスの承認]({{site.baseurl}}/user_guide/messaging/governance/approvals)を参照してください。

## 関連記事 {#related-articles}

- [デザインと編集]({{site.baseurl}}/user_guide/messaging/design_and_edit)
- [ABテスト]({{site.baseurl}}/user_guide/messaging/ab_testing)
- [送信前に知っておくべきこと]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/know_before_you_send)
- [キャンペーン分析]({{site.baseurl}}/user_guide/analytics/reports/campaign_analytics)