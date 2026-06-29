---
nav_title: メール分析用語集
article_title: メール分析用語集
layout: email_report_metrics
page_order: 0
excerpt_separator: ""
page_type: glossary
description: "この用語集には、起動後のメールCampaignまたはCanvasの分析セクションに表示される用語が含まれています。この用語集には、Currentsの指標は含まれていません。"
channel:
  - email
---

> この用語集では、メールCampaignおよびCanvasesの**Analytics**タブに表示される指標を定義しています。Brazeはホスト型の「このメールをブラウザで表示」ページを提供していません。回避策については、[メールに「ブラウザでこのメールを表示」リンクを追加できますか？]({{site.baseurl}}/user_guide/channels/email/faq#can-i-add-a-view-this-email-in-a-browser-link-to-my-emails)を参照してください。複数の指標にまたがるその他のトラブルシューティングについては、[メールFAQ]({{site.baseurl}}/user_guide/channels/email/faq)を参照してください。

<style>
  .calculation-line {
    color: #76848C;
    font-size: 14px;
  }
</style>

{% api %}

### バリアント {#variation}

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Variation' %}

<span class="calculation-line">計算式: カウント</span>

{% endapi %}

{% api %}

### メール可能 {#emailable}

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Emailable' %}

<span class="calculation-line">計算式: カウント</span>

{% endapi %}

{% api %}

### オーディエンス (%) {#audience}

{% apitags %}
Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Audience' %}

<span class="calculation-line">計算式: (バリアントの受信者数) / (ユニーク受信者数)</span>

{% endapi %}

{% api %}

### ユニーク受信者数 {#unique-recipients}

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Recipients' %} この数値はBrazeから提供されます。

<span class="calculation-line">計算式: カウント</span>

{% endapi %}

{% api %}

### 送信数 {#sends}

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Sends' %}  この指標はBrazeから提供されます。

<span class="calculation-line">計算式: カウント</span>

{% endapi %}

{% api %}

### 送信済みメッセージ {#messages-sent}

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Messages Sent' %}  この指標はBrazeから提供されます。

<span class="calculation-line">計算式: カウント</span>

{% endapi %}

{% api %}

### 配信数 {#deliveries}

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Deliveries' %} メールの場合、*配信数*は、メール可能な相手に正常に送信され、受信されたメッセージ（送信数）の合計です。

<span class="calculation-line">計算式: (送信数) - (バウンス数) </span>

{% alert note %}
ユーザーレベルの**受信済み**ステータスおよび関連ロジック（フリークエンシーキャップなど）について、Brazeは通常、メールサービスプロバイダー（ESP）が受信トレイへの最終配信を確認した時点ではなく、送信が処理され配信のために引き渡された時点でユーザーをマークします。これにより、ESPの確認と製品内ルールの間のタイミングギャップを回避できます。ESPやサードパーティの配信レポートとは異なる場合があります。
{% endalert %}

{% endapi %}

{% api %}

### 配信率 (%)

{% apitags %}
Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Deliveries %' %}

<span class="calculation-line">計算式: (送信数 - バウンス数) / (送信数) </span>

{% endapi %}

{% api %}

### バウンス {#bounces}

{% apitags %}
Count, Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Bounces' %}

メールの場合、*バウンス率*は、送信に失敗した、または使用している送信サービスから「返送」もしくは「未受信」と指定された、あるいは対象のメール可能なユーザーに受信されなかったメッセージの割合です。

SendGridを使用している顧客のメールバウンスは、ハードバウンス、スパム（`spam_report_drops`）、および無効なアドレスへの送信メール（`invalid_emails`）で構成されます。

{% alert note %}
[Braze Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents)では、ESPによる一時的な遅延はソフトバウンスとして表されることが多いです。配信ツール（例: ネイティブのSendGridレポートやLookerモデル）でも、同じ状況に対して遅延を使用する場合があります。遅延は通常一時的なもので、再試行後にメールが配信されることが多いです。長期間の再試行（Campaign分析でのソフトバウンスの場合、最大約72時間）の後、ESPによってはメッセージが配信不能として扱われる場合があります。Currentsのメールイベントは追記専用です。ログに記録されたソフトバウンスは、メッセージが最終的に配信された場合でも後から削除されません。
{% endalert %}

{::nomarkdown}
<span class="calculation-line">
    計算式:
    <ul>
        <li><b><i>バウンス</i>:</b> カウント</li>
        <li><b><i>バウンス率 (%)</i> または <i>バウンス率 (%)</i>:</b> (バウンス数) / (送信数)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### ハードバウンス {#hard-bounce}

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Hard Bounce' %}

メールがハードバウンスした場合やスパムとしてマークされた場合、Brazeはそのメールアドレスを無効としてマークしますが、ユーザーの[サブスクリプションステータス]({{site.baseurl}}/user_guide/channels/email/subscriptions)は更新しません。Brazeはそのメールアドレスへの今後の送信を停止します。ハードバウンスリストからメールアドレスを削除するには、[ハードバウンスメール削除エンドポイント]({{site.baseurl}}/api/endpoints/email/post_remove_hard_bounces)を使用してください。

<span class="calculation-line">計算式: カウント </span>

{% endapi %}

{% api %}

### ソフトバウンス {#soft-bounce}

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Soft Bounce' %} メールがソフトバウンスした場合、通常72時間以内に再試行しますが、再試行回数は受信者によって異なります。

ソフトバウンスはCampaignの分析では追跡されませんが、[メッセージアクティビティログ]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log)で監視したり、[ソフトバウンスSegmentフィルター]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#soft-bounced)を使用してこれらのユーザーを送信対象から除外したりできます。メッセージアクティビティログでは、ソフトバウンスの理由を確認し、メールCampaignの「送信数」と「配信数」の間の差異を把握することもできます。

<span class="calculation-line">計算式: カウント </span>

{% endapi %}

{% api %}

### スパム {#spam}

{% apitags %}
Count, Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Spam' %}

{::nomarkdown}
<span class="calculation-line">
    計算式:
    <ul>
        <li><b><i>スパム</i>:</b> カウント</li>
        <li><b><i>スパム率 (%)</i> または <i>スパム率 (%)</i>:</b> (スパムとしてマーク) / (送信数)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### ユニーク開封数 {#unique-opens}

{% apitags %}
Count, Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Opens' %} メールの場合、これは7日間にわたって追跡されます。つまり、同じユーザーが7日後に同じメールを再度開封した場合、新しいユニーク開封としてカウントされます。そのため、ダッシュボードのユニーク開封数は、Currentsデータに対する単純な `DISTINCT user_id` クエリよりも高くなる場合があります。Currentsからダッシュボードのカウントと一致させるには、`is_unique` が `true` のイベントでフィルタリングしてください。

{::nomarkdown}
<span class="calculation-line">
    計算式:
    <ul>
        <li><b><i>ユニーク開封数</i>:</b> カウント</li>
        <li><b><i>ユニーク開封率 (%)</i> または <i>ユニーク開封率</i>:</b> (ユニーク開封数) / (配信数)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### ユニーククリック数 {#unique-clicks}

{% apitags %}
Count, Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Clicks' %} これはメールの場合7日間にわたって追跡され、<a href='/docs/user_guide/messaging/messaging_fundamentals/dispatch_id'>dispatch_id</a>（1回の送信試行）ごとに測定されます。Brazeが提供する配信停止リンクのクリックも含まれます。トラッキング対象のカスタム配信停止URLも、ユーザーがリンクを選択した場合に*ユニーククリック数*にカウントされます。7日後に同じユーザーが再度クリックした場合、別のユニーククリックとしてカウントされます。*ユニーククリック数*を含むダッシュボードのメールエンゲージメント指標はBrazeで計算されており、ESPの集計レポートとは照合されません。Currentsからダッシュボードのカウントと一致させるには、`is_unique` が `true` のイベントでフィルタリングしてください。

{::nomarkdown}
<span class="calculation-line">
    計算式:
    <ul>
        <li><b><i>ユニーククリック数</i>:</b> カウント</li>
        <li><b><i>ユニーククリック率 (%)</i> または <i>クリック率</i>:</b> (ユニーククリック数) / (配信数)</li>
    </ul>
</span>
{:/}

#### メールヒートマップ上の予期しないリンク {#unexpected-links-on-the-email-heatmap}

[メールヒートマップ]({{site.baseurl}}/user_guide/channels/email/reporting)に予期しないリンクが表示される場合は、メッセージのHTMLで[コンテンツブロック]({{site.baseurl}}/user_guide/channels/email/drag_and_drop/dnd_editor_blocks)やトラッキングURLを生成する単語間のスペースを確認してください。ヒートマップビューの**リンクテーブル（合計クリック数別）**を使用して、表示されているコピーと一致しないURLを特定してください。

{% endapi %}

{% api %}

### 合計クリック数 {#total-clicks}

{% apitags %}
Count, Percentage
{% endapitags %}

<i>合計クリック数</i>は、配信されたメール内のリンクをユーザーがクリックした合計回数で、同じユーザーによる複数回のクリックを含みます。Brazeの配信停止リンクおよびトラッキング対象のカスタム配信停止URLのクリックも含まれます。

*合計クリック数*が*ユニーククリック数*よりも大幅に多い場合、セキュリティツールやメールボックスプロバイダーがユーザーの開封なしにリンクをスキャンしている可能性があります。エンゲージメントを内部で評価する際は*ユニーククリック数*を比較してください。

{% endapi %}

{% api %}

### 配信停止 {#unsubscribers-or-unsub}

{% apitags %}
Count, Percentage
{% endapitags %}

*配信停止*は、Brazeの標準配信停止リンクを反映しています。カスタム購読解除ページでは、APIを使用してユーザーを更新しない限り、この指標は増加しません。**サブスクリプショングループ時系列**には、APIによる変更が引き続き反映されます。

{% multi_lang_include analytics/metrics.md metric='Unsubscribers or Unsub' %}

{::nomarkdown}
<span class="calculation-line">
    計算式:
    <ul>
        <li><b><i>配信停止数</i> または <i>購読解除</i>:</b> カウント</li>
        <li><b><i>配信停止率 (%)</i> または <i>購読解除率</i>:</b> (配信停止数) / (配信数)</li>
    </ul>
</span>
{:/}

#### *配信停止*と配信停止リンクのクリック数が異なる理由 {#why-unsubscribes-and-unsubscribe-link-clicks-can-differ}

メールCampaignまたはCanvasの**Analytics**ページで、*配信停止*数と、**Total Clicks**または**Unique Clicks**を展開した際のリンク別内訳に表示されるBraze配信停止URLのクリック数を比較してください。この2つは一致することが多いですが、異なる場合もあります。

- ***配信停止*が本文の配信停止URLのクリック数より多い場合:** [リスト配信停止]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences#list-unsubscribe)は、メールヘッダーに含まれる追加の配信停止パスです（メッセージ本文のリンクではありません）。ユーザーがこの方法で配信停止した場合、*配信停止*にはカウントされますが、本文内のトラッキング対象の配信停止URLのクリックとしてはカウントされません。
- **本文の配信停止URLのクリック数が*配信停止*より多い場合:** ユーザーがそのリンクを複数回選択する場合があります。配信停止後に再度サブスクライブし、再び配信停止した場合、メール分析ではクリック内訳に複数のクリック（例: 2回）が記録されることがあります。

詳細については、[配信停止リンクのクリック数と配信停止数が異なるのはなぜですか？]({{site.baseurl}}/user_guide/channels/email/faq#why-am-i-seeing-a-different-number-of-unsubscribes-than-clicks-on-my-unsubscribe-link)を参照してください。

{% endapi %}

{% api %}

### 収益 {#revenue}

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Revenue' %}

<span class="calculation-line">計算式: カウント </span>

{% endapi %}

{% api %}

### 1次コンバージョン (A) または1次コンバージョンイベント {#primary-conversions-a-or-primary-conversion-event}

{% apitags %}
Count, Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Primary Conversions (A) or Primary Conversion Event' %} メール、プッシュ、webhookの場合、最初の送信後からコンバージョンの追跡を開始します。

{::nomarkdown}
<span class="calculation-line">
    計算式:
    <ul>
        <li><b><i>1次コンバージョン (A)</i> または <i>1次コンバージョンイベント</i>:</b> カウント</li>
        <li><b><i>1次コンバージョン (A) %</i> または <i>1次コンバージョンイベント率</i>:</b> (1次コンバージョン数) / (ユニーク受信者数)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### 信頼度 {#confidence}

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Confidence' %}

{% endapi %}

{% api %}

### マシン開封 {#machine-opens}

{% multi_lang_include analytics/metrics.md metric='Machine Opens' %} この指標は、SendGridでは2021年11月11日から、SparkPostでは2021年12月2日から追跡されています。

<span class="calculation-line">計算式: カウント </span>

{% endapi %}

{% api %}

### その他の開封 {#other-opens}

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Other Opens' %} ユーザーは、<i>マシン開封</i>のカウントが記録される前にメールを開封する（<i>その他の開封</i>としてカウントされる開封など）こともできます。マシン開封イベントの後に、Apple Mail以外の受信トレイからユーザーがメールを1回以上開封した場合、そのユーザーがメールを開封した回数は<i>その他の開封</i>に加算され、<i>ユニーク開封</i>には1回のみカウントされます。

<span class="calculation-line">計算式: カウント </span>

{% endapi %}

{% api %}

### 推定実開封数 {#estimated-real-opens}

{% apitags %}
Count, Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Estimated Real Opens' %} Brazeは、新しい開封およびクリックデータが届くたびにこの推定値を再計算します。値は通常、送信後数日で安定しますが、新しい対象イベントが発生した場合は引き続き更新されます。

{% endapi %}

{% api %}

### クリック開封率 {#click-to-open-rate}

{% apitags %}
Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Click-to-Open Rate' %}

<span class="calculation-line">計算式: (ユニーククリック数) / (ユニーク開封数)（メールの場合）</span>

#### メッセージ開封可能性スコア（セグメンテーション） {#message-open-likelihood-scores-segmentation}

[`Message Open Likelihood`]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#message-open-likelihood) Segmentフィルターは、ユーザーがメールを開封する可能性を0〜100のスケールでスコアリングします。チャネルに対する十分な送信または開封履歴がないユーザーは空白として表示されます。メールの場合、マシン開封は計算から除外され、そのチャネルの最近のメッセージ履歴が使用されます（[個別チャネルのメッセージ開封可能性フィルター]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_channel#individual-channels)を参照）。

{% endapi %}

## メールレポートのトラブルシューティングとFAQ {#email-reporting-troubleshooting-and-faqs}

### 配信停止リンクとユニーククリック数 {#unsubscribe-links-and-unique-clicks}

受信者が配信停止リンクをクリックすると、そのアクションはURLを使用するため、Brazeはクリックとしてカウントします。これはBrazeが提供する配信停止リンクと、メッセージ本文内のカスタム配信停止リンクの両方に適用されます。これらのクリックは、他のリンクのクリックとともに*ユニーククリック数*と*合計クリック数*に加算されます。指標の定義については、上記の[ユニーククリック数](#unique-clicks)および[配信停止リンクのクリック数と配信停止数が異なるのはなぜですか？]({{site.baseurl}}/user_guide/channels/email/faq#why-am-i-seeing-a-different-number-of-unsubscribes-than-clicks-on-my-unsubscribe-link)を参照してください。

### ブラウザで表示 {#view-in-browser}

Brazeには「このメールをブラウザで表示」機能は組み込まれていません。メールコンテンツを外部のランディングページ（Webサイトなど）にホストし、メールエディターの**リンク**ツールを使用してメッセージからリンクを追加してください。詳細については、[メールに「ブラウザでこのメールを表示」リンクを追加できますか？]({{site.baseurl}}/user_guide/channels/email/faq#can-i-add-a-view-this-email-in-a-browser-link-to-my-emails)を参照してください。

### カスタム購読解除ページの更新 {#custom-unsubscribe-page-updates}

[カスタム購読解除ページ]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences)への変更は数分以内に反映されます。ライブ送信では、変更を保存した際に更新される短期間のキャッシュが使用されます。

### 容量超過およびメールボックスフルのバウンス {#over-quota-and-full-mailbox-bounces}

容量超過またはメールボックスフルのバウンスは、受信者のメールボックスが新しいメールを受け付けられないことを意味します。無効またはリスクのあるアドレスを持つ新規登録者や、受信トレイが休止状態の間にいっぱいになった長期間非アクティブなプロファイルの中にこれらのアドレスが見られることがあります。

Segmentとソースごとにバウンス率を確認し、繰り返しハードバウンスするアドレスを削除またはサンセットし、新規サブスクライバーには確認済みまたはダブルオプトインを使用してください。リスト衛生のプラクティスについては、[配信性の落とし穴とスパムトラップ]({{site.baseurl}}/user_guide/channels/email/email_setup/deliverability_pitfalls_and_spam_traps)および[メールレポート]({{site.baseurl}}/user_guide/channels/email/reporting#troubleshooting)を参照してください。

### 550 5.7.1 迷惑メール {#550-571-unsolicited-mail}

`550 5.7.1`レスポンス（「このメッセージは迷惑メールである可能性が高いとシステムが検出しました」など）は、レピュテーションやエンゲージメントのシグナルが低い場合に、厳格なメールボックスプロバイダー（例: Gmail）から返されることが多いです。一般的な原因には、スパム苦情、低エンゲージメント、購入またはレンタルしたリスト、急激な送信量の増加などがあります。

同意ベースのリスト成長に注力し、非アクティブなサブスクライバーをサンセットし、苦情率とバウンス率を監視してください。詳細については、[配信性の落とし穴とスパムトラップ]({{site.baseurl}}/user_guide/channels/email/email_setup/deliverability_pitfalls_and_spam_traps)を参照してください。

### 良好なメール配信率 {#good-email-deliverability-rates}

**配信**とは、受信サーバーがメッセージを受け入れるかどうかであり、*配信数*やバウンス率などの指標で測定できます。**配信性**（受信トレイへの到達）はプロバイダーのフィルタリングに依存し、Brazeの単一の指標としては表示されません。

一般的なガイドラインとして、配信率は99%近くを目指し、ハードバウンスは約1%未満に抑え、開封数とクリック数でエンゲージメントの傾向を監視してください。正確な目標は業界や送信パターンによって異なります。レピュテーションをサポートするプラクティスについては、[メール配信性の向上]({{site.baseurl}}/user_guide/channels/email/best_practices/improve_deliverability)および[配信性の落とし穴とスパムトラップ]({{site.baseurl}}/user_guide/channels/email/email_setup/deliverability_pitfalls_and_spam_traps)を参照してください。

### 「Campaignは既に遅延ウィンドウ内のため、別のエンキューは行いません」 {#campaign-is-already-in-delay-window-so-not-enqueueing-another}

[アクションベースCampaign]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery)のメッセージアクティビティまたは診断ログで、この処理結果は、同じユーザーに対する以前のトリガーがCampaignの配信ウィンドウ内にある間に、Brazeが重複送信をブロックしたことを意味します。デバウンスロックにより、同じトリガーバーストに対する複数のエンキューが防止されます。

Campaignが**即時送信**と表示されている場合でも、以下のいずれかに該当する場合にこの結果が表示されることがあります。

- Campaignが[例外イベント]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/exit_criteria#exception-events)またはタイミングに影響する送信時遅延を使用している。
- ユーザーに[再適格性]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility)期間が設定されており、そのウィンドウが経過するまでメッセージを再度受信できない。
- トリガーが重複した際に、より高い優先度を持つ別のCampaignまたはCanvasメッセージステップが送信スロットを消費した。

ユーザーがメッセージを受信すべきだったのに受信しなかった場合は、同じトリガーに対する以前の結果（例: メールバウンスやチャネルが有効でないなど）を確認してください。同じワークフロー内の別のメッセージがこの送信を妨げた可能性があります。