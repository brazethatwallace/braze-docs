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

<style>
  .calculation-line {
    color: #76848C;
    font-size: 14px;
  }
</style>

{% api %}

### バリエーション {#variation}

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

メールがハードバウンスした場合やスパムとしてマークされた場合、Brazeはそのメールアドレスを無効としてマークしますが、ユーザーの[サブスクリプションステータス]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/)は更新しません。Brazeはそのメールアドレスへの今後の送信を停止します。ハードバウンスリストからメールアドレスを削除するには、[ハードバウンスメール削除エンドポイント]({{site.baseurl}}/api/endpoints/email/post_remove_hard_bounces/)を使用してください。

<span class="calculation-line">計算式: カウント </span>

{% endapi %}

{% api %}

### ソフトバウンス {#soft-bounce}

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Soft Bounce' %} メールがソフトバウンスした場合、通常72時間以内に再試行しますが、再試行回数は受信者によって異なります。

ソフトバウンスはCampaignの分析では追跡されませんが、[メッセージアクティビティログ]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log/)で監視したり、[ソフトバウンスSegmentフィルター]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters/#soft-bounced)を使用してこれらのユーザーを送信対象から除外したりできます。メッセージアクティビティログでは、ソフトバウンスの理由を確認し、メールCampaignの「送信数」と「配信数」の間の差異を把握することもできます。

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

{% multi_lang_include analytics/metrics.md metric='Unique Clicks' %} これはメールの場合7日間にわたって追跡され、<a href='/docs/help/help_articles/data/dispatch_id/'>dispatch_id</a> で測定されます。Brazeが提供する配信停止リンクのクリックも含まれます。7日後に同じユーザーが再度クリックした場合、別のユニーククリックとしてカウントされます。Currentsからダッシュボードのカウントと一致させるには、`is_unique` が `true` のイベントでフィルタリングしてください。

{::nomarkdown}
<span class="calculation-line">
    計算式:
    <ul>
        <li><b><i>ユニーククリック数</i>:</b> カウント</li>
        <li><b><i>ユニーククリック率 (%)</i> または <i>クリック率</i>:</b> (ユニーククリック数) / (配信数)</li>
    </ul>
</span>
{:/}

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

- ***配信停止*が本文の配信停止URLのクリック数より多い場合:** [リスト配信停止]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences/#list-unsubscribe)は、メールヘッダーに含まれる追加の配信停止パスです（メッセージ本文のリンクではありません）。ユーザーがこの方法で配信停止した場合、*配信停止*にはカウントされますが、本文内のトラッキング対象の配信停止URLのクリックとしてはカウントされません。
- **本文の配信停止URLのクリック数が*配信停止*より多い場合:** ユーザーがそのリンクを複数回選択する場合があります。配信停止後に再度サブスクライブし、再び配信停止した場合、メール分析ではクリック内訳に複数のクリック（例: 2回）が記録されることがあります。

詳細については、[配信停止リンクのクリック数と配信停止数が異なるのはなぜですか？]({{site.baseurl}}/user_guide/channels/email/faq/#why-am-i-seeing-a-different-number-of-unsubscribes-than-clicks-on-my-unsubscribe-link)を参照してください。

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

### クリック開封率 {#click-to-open-rate}

{% apitags %}
Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Click-to-Open Rate' %}

<span class="calculation-line">計算式: (ユニーククリック数) / (ユニーク開封数)（メールの場合）</span>

{% endapi %}