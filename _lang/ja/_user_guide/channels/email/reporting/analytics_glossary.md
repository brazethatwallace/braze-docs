---
nav_title: メール分析用語集
article_title: メール分析用語集
layout: email_report_metrics
page_order: 0
excerpt_separator: ""
page_type: glossary
description: "この用語集には、起動後のメールキャンペーンまたはキャンバスの分析セクションに表示される用語が含まれています。この用語集には、Currents の指標は含まれていません。"
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

### バリエーション

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Variation' %}

<span class="calculation-line">計算式: カウント</span>

{% endapi %}

{% api %}

### メール可能

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Emailable' %}

<span class="calculation-line">計算式: カウント</span>

{% endapi %}

{% api %}

### オーディエンス (%)

{% apitags %}
Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Audience' %}

<span class="calculation-line">計算式: (バリアントの受信者数) / (ユニーク受信者数)</span>

{% endapi %}

{% api %}

### ユニーク受信者数

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Recipients' %} この数値は Braze から提供されます。

<span class="calculation-line">計算式: カウント</span>

{% endapi %}

{% api %}

### 送信数

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Sends' %}  この指標は Braze から提供されます。

<span class="calculation-line">計算式: カウント</span>

{% endapi %}

{% api %}

### 送信済みメッセージ

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Messages Sent' %}  この指標は Braze から提供されます。

<span class="calculation-line">計算式: カウント</span>

{% endapi %}

{% api %}

### 配信数

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

### バウンス

{% apitags %}
Count, Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Bounces' %}

メールの場合、*バウンス率*は、送信に失敗した、または使用している送信サービスから「返送」もしくは「未受信」と指定された、あるいは対象のメール可能なユーザーに受信されなかったメッセージの割合です。

SendGrid を使用している顧客のメールバウンスは、ハードバウンス、スパム（`spam_report_drops`）、および無効なアドレスへの送信メール（`invalid_emails`）で構成されます。

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

### ハードバウンス

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Hard Bounce' %}

メールがハードバウンスした場合やスパムとしてマークされた場合、Braze はそのメールアドレスを無効としてマークしますが、ユーザーの[サブスクリプションステータス]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/)は更新しません。Braze はそのメールアドレスへの今後の送信を停止します。ハードバウンスリストからメールアドレスを削除するには、[ハードバウンスメール削除エンドポイント]({{site.baseurl}}/api/endpoints/email/post_remove_hard_bounces/)を使用してください。

<span class="calculation-line">計算式: カウント </span>

{% endapi %}

{% api %}

### ソフトバウンス

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Soft Bounce' %} メールがソフトバウンスした場合、通常72時間以内に再試行しますが、再試行回数は受信者によって異なります。

ソフトバウンスは Campaign の分析では追跡されませんが、[メッセージアクティビティログ]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log/)で監視したり、[ソフトバウンス Segment フィルター]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters/#soft-bounced)を使用してこれらのユーザーを送信対象から除外したりできます。メッセージアクティビティログでは、ソフトバウンスの理由を確認し、メール Campaign の「送信数」と「配信数」の間の差異を把握することもできます。

<span class="calculation-line">計算式: カウント </span>

{% endapi %}

{% api %}

### スパム

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

### ユニーク開封数

{% apitags %}
Count, Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Opens' %} メールの場合、これは7日間にわたって追跡されます。つまり、同じユーザーが7日後に同じメールを再度開封した場合、新しいユニーク開封としてカウントされます。そのため、ダッシュボードのユニーク開封数は、Currents データに対する単純な `DISTINCT user_id` クエリよりも高くなる場合があります。Currents からダッシュボードのカウントと一致させるには、`is_unique` が `true` のイベントでフィルタリングしてください。

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

### ユニーククリック数

{% apitags %}
Count, Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Clicks' %} これはメールの場合7日間にわたって追跡され、<a href='/docs/help/help_articles/data/dispatch_id/'>dispatch_id</a> で測定されます。Braze が提供する配信停止リンクのクリックも含まれます。7日後に同じユーザーが再度クリックした場合、別のユニーククリックとしてカウントされます。Currents からダッシュボードのカウントと一致させるには、`is_unique` が `true` のイベントでフィルタリングしてください。

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

### 配信停止

{% apitags %}
Count, Percentage
{% endapitags %}

*配信停止*は、Braze の標準配信停止リンクを反映しています。カスタム購読解除ページでは、API を使用してユーザーを更新しない限り、この指標は増加しません。**サブスクリプショングループ時系列**には、API による変更が引き続き反映されます。

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

{% endapi %}

{% api %}

### 収益

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Revenue' %}

<span class="calculation-line">計算式: カウント </span>

{% endapi %}

{% api %}

### 1次コンバージョン (A) または1次コンバージョンイベント

{% apitags %}
Count, Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Primary Conversions (A) or Primary Conversion Event' %} メール、プッシュ、webhook の場合、最初の送信後からコンバージョンの追跡を開始します。

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

### 信頼度

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Confidence' %}

{% endapi %}

{% api %}

### マシン開封

{% multi_lang_include analytics/metrics.md metric='Machine Opens' %} この指標は、SendGrid では2021年11月11日から、SparkPost では2021年12月2日から追跡されています。

<span class="calculation-line">計算式: カウント </span>

{% endapi %}

{% api %}

### その他の開封

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Other Opens' %} ユーザーは、<i>マシン開封</i>のカウントが記録される前にメールを開封する（<i>その他の開封</i>としてカウントされる開封など）こともできます。マシン開封イベントの後に、Apple Mail 以外の受信トレイからユーザーがメールを1回以上開封した場合、そのユーザーがメールを開封した回数は<i>その他の開封</i>に加算され、<i>ユニーク開封</i>には1回のみカウントされます。

<span class="calculation-line">計算式: カウント </span>

{% endapi %}

{% api %}

### クリック開封率

{% apitags %}
Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Click-to-Open Rate' %}

<span class="calculation-line">計算式: (ユニーククリック数) / (ユニーク開封数)（メールの場合）</span>

{% endapi %}