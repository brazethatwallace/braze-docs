---
nav_title: 指標用語集
article_title: 指標用語集
layout: report_metrics
page_order: 4
excerpt_separator: ""
page_type: glossary
description: "この用語集では、Brazeアカウントのレポートに表示される用語を定義しています。"
tool: Reports
---

<style>
  .calculation-line {
    color: #5B6B75;
    font-size: 14px;
  }
</style>

{% api %}

## AMPクリック数 {#amp-clicks}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='AMP Clicks' %}

{% endapi %}

{% api %}

## AMP開封数 {#amp-opens}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='AMP Opens' %}

{% endapi %}

{% api %}

## オーディエンス {#audience}

{% apitags %}
All
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Audience' %}

<span class="calculation-line">計算式: (バリアントの受信者数) / (ユニーク受信者数)</span>

{% endapi %}

{% api %}

## バウンス数 {#bounces}

{% apitags %}
Email, Web Push, iOS Push
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Bounces' %} これは、有効なプッシュトークンがない場合、Campaignの起動後にユーザーが配信停止した場合、またはメールアドレスが不正確もしくは無効化されている場合に発生する可能性があります。

| チャネル | 追加情報 |
|-------|-----------------------|
| メール | SendGridを使用している顧客のメールバウンスは、ハードバウンス、スパム（`spam_report_drops`）、および無効なアドレスへの送信（`invalid_emails`）で構成されます。<br><br>メールの場合、*バウンス率*は、送信に失敗した、または送信サービスから「返送」もしくは「未受信」と指定された、あるいは対象のメール受信可能ユーザーに受信されなかったメッセージの割合です。|
| プッシュ | これらのユーザーは、今後のすべてのプッシュ通知から自動的に配信停止されています。|
{: .reset-td-br-1 .reset-td-br-2 aria-label="バウンス数" }

{::nomarkdown}
<span class="calculation-line">
    計算式:
    <ul>
        <li><i>バウンス数</i>: カウント</li>
        <li><i>バウンス率</i>: (バウンス数) / (送信数)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

## 本文クリック {#body-click}

{% apitags %}
iOS Push, Android Push
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Body Click' %}

<span class="calculation-line">計算式: (本文クリック数) / (インプレッション数)</span>

{% endapi %}

{% api %}

## 本文クリック数 {#body-clicks}

{% apitags %}
In-App Message
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Body Clicks' %}

<span class="calculation-line">計算式: (本文クリック数) / (インプレッション数)</span>

{% endapi %}

{% api %}

## ボタン1クリック数 {#button-1-clicks}

{% apitags %}
In-App Message
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Button 1 Clicks' %} _ボタン1クリック数_のレポートは、アプリ内メッセージで**Identifier for Reporting**を「0」に指定した場合にのみ機能します。

<span class="calculation-line">計算式: (ボタン1クリック数) / (インプレッション数)</span>

{% endapi %}

{% api %}

## ボタン2クリック数 {#button-2-clicks}

{% apitags %}
In-App Message
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Button 2 Clicks' %} _ボタン2クリック数_のレポートは、アプリ内メッセージで**Identifier for Reporting**を「1」に指定した場合にのみ機能します。

<span class="calculation-line">計算式: (ボタン2クリック数) / (インプレッション数)</span>

{% endapi %}

{% api %}

## Campaign分析 {#campaign-analytics}

{% apitags %}
Feature Flags
{% endapitags %}

さまざまなチャネルにおけるメッセージのパフォーマンスです。表示される指標は、選択したメッセージングチャネルと、[フィーチャーフラグ実験]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/experiments/#campaign-analytics)が多変量テストかどうかによって異なります。

{% endapi %}

{% api %}

## 送信された選択肢 {#choices-submitted}

{% apitags %}
In-App Message
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Choices Submitted' %}

{% endapi %}

{% api %}

## クリック対開封率 {#click-to-open-rate}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Click-to-Open Rate' %}

<span class="calculation-line">計算式: (ユニーククリック数) / (ユニーク開封数)（メールの場合）</span>

{% endapi %}

{% api %}

## RCS確認済み配信数またはSMS確認済み配信数 {#rcs-confirmed-deliveries-or-sms-confirmed-deliveries}

{% apitags %}
SMS/MMS, RCS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Confirmed Deliveries' %} Brazeの顧客として、配信はSMS割り当てに対して課金されます。

{::nomarkdown}
<span class="calculation-line">
    計算式:
    <ul>
        <li><i>確認済み配信数</i>: カウント</li>
        <li><i>確認済み配信率</i>: (確認済み配信数) / (送信数)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

## 信頼度 {#confidence}

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Confidence' %}

{% endapi %}

{% api %}

## 確認ページボタン {#confirmation-page-button}

{% apitags %}
In-App Message
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Confirmation Page Button' %}

{% endapi %}

{% api %}

## 確認ページの却下数 {#confirmation-page-dismissals}

{% apitags %}
In-App Message
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Confirmation Page Dismissals' %}

{% endapi %}

{% api %}

## コンバージョン (B, C, D) {#conversions-b-c-d}

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Conversions (B, C, D)' %} この定義済みイベントは、Campaignの作成時に設定します。

| チャネル | 追加情報 |
|-------|-----------------------|
| メール、プッシュ、Webhook | コンバージョンは初回送信後に追跡されます。|
| Content Cards | コンバージョンは、ユーザーがContent Cardsを初めて閲覧した時点でカウントされます。|
| アプリ内メッセージ | コンバージョンは、ユーザーがアプリ内メッセージCampaignを受信して閲覧し、その後、定義されたコンバージョンウィンドウ内で特定のコンバージョンイベントを実行した場合にカウントされます。メッセージをクリックしたかどうかは問いません。<br><br>コンバージョンは、最後に受信したメッセージに帰属します。再適格性が有効な場合、コンバージョンは定義されたコンバージョンウィンドウ内で発生した場合に限り、最後に受信したアプリ内メッセージに割り当てられます。ただし、アプリ内メッセージにすでにコンバージョンが割り当てられている場合、その特定のメッセージに対して新しいコンバージョンを記録することはできません。つまり、各アプリ内メッセージの配信は1つのコンバージョンにのみ関連付けられます。|
{: .reset-td-br-1 .reset-td-br-2 aria-label="コンバージョン (B, C, D)" }

{% endapi %}

{% api %}

## 合計コンバージョン数 {#total-conversions}

{% apitags %}
In-App Message
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Conversions' %}

ユーザーがアプリ内メッセージCampaignを1回だけ閲覧した場合、その後コンバージョンイベントを複数回実行しても、カウントされるコンバージョンは1回のみです。ただし、再適格性がオンになっていて、ユーザーがアプリ内メッセージCampaignを複数回閲覧した場合、ユーザーがアプリ内メッセージCampaignの新しいインスタンスのインプレッションを記録するたびに、*合計コンバージョン数*は増加する可能性があります。

例えば、ユーザーがアプリ内メッセージを2回トリガーし、各アプリ内メッセージのインプレッション後にコンバージョンした場合（2回のコンバージョン）、*合計コンバージョン数*は2増加します。ただし、アプリ内メッセージのインプレッションが1回のみで、その後2回のコンバージョンイベントが発生した場合、記録されるコンバージョンは1回のみで、*合計コンバージョン数*は1増加します。

{% endapi %}

{% api %}

## メッセージを閉じる {#close-message}

{% apitags %}
In-App Message
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Close Message' %}

{% endapi %}

{% api %}

## コンバージョン率 {#conversion-rate}

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Conversion Rate' %}

| チャネル | 追加情報 |
|-------|-----------------------|
| アプリ内メッセージ | アプリ内メッセージの<i>コンバージョン率</i>の計算には、1日あたりの<i>ユニークインプレッション数</i>の指標が使用されます。<br><br>アプリ内メッセージの<i>ユニークインプレッション数</i>は、ワークスペースのタイムゾーンにおける暦日ごとに1回のみカウントされます。ユーザーが目的のアクション（「コンバージョン」）を完了する回数は、同じ暦日内で増加する可能性があります。コンバージョンは1日に複数回発生する可能性がありますが、<i>ユニークインプレッション数</i>は増加しません。そのため、ユーザーが1日に複数回コンバージョンを完了した場合、<i>コンバージョン率</i>はそれに応じて増加する可能性がありますが、<i>ユニークインプレッション数</i>はその暦日に1回のみカウントされます。詳細については、<a href="/docs/user_guide/channels/in_app_messages/reporting/">アプリ内メッセージレポート</a> を参照してください。|
{: .reset-td-br-1 .reset-td-br-2 aria-label="コンバージョン率" }

{::nomarkdown}
<span class="calculation-line">
    計算式:
    <ul>
        <li><b>アプリ内メッセージ</b>: (1次コンバージョン数) / (ユニークインプレッション数)</li>
        <li><b>その他のチャネル</b>: (1次コンバージョン数) / (ユニーク受信者数)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

## コンバージョンウィンドウ {#conversion-window}

{% apitags %}
All
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Conversion Window' %}

{% endapi %}

{% api %}

## 配信数 {#deliveries}

{% apitags %}
Email, Web Push, iOS Push, Android Push, WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Deliveries' %}

| チャネル | 追加情報 |
|-------|-----------------------|
| メール | メール受信可能な相手に正常に送信され、受信されたメッセージの合計数（送信数）を指します。|
{: .reset-td-br-1 .reset-td-br-2 aria-label="配信数" }

{::nomarkdown}
<span class="calculation-line">
    計算式:
    <ul>
        <li><i>配信数</i>: カウント</li>
        <li><i>配信率</i>: (送信数 - バウンス数) / (送信数)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

## RCS配信失敗数またはSMS配信失敗数 {#rcs-delivery-failures-or-sms-delivery-failures}

{% apitags %}
SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Delivery Failures' %}

配信失敗の理由を理解するには、<a href="/docs/braze_support/">Brazeサポート</a> にお問い合わせください。

<span class="calculation-line">計算式: (送信数) - (キャリアへの送信数)</span>

{% endapi %}

{% api %}

## 配信失敗数 {#delivery-failures}

{% apitags %}
RCS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Delivery Failures RCS' %}

配信失敗の理由を理解するには、<a href="/docs/braze_support/">Brazeサポート</a> にお問い合わせください。

<span class="calculation-line">計算式: (送信数) - (キャリアへの送信数)</span>

{% endapi %}

{% api %}

## 配信失敗率 {#failed-delivery-rate}

{% apitags %}
SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Failed Delivery Rate' %}

配信失敗の理由を理解するには、<a href="/docs/braze_support/">Brazeサポート</a> にお問い合わせください。

<span class="calculation-line">計算式: (配信失敗数) / (送信数)</span>

{% endapi %}

{% api %}

## 直接開封数 {#direct-opens}

{% apitags %}
iOS Push
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Direct Opens' %}

<span class="calculation-line">計算式: (直接開封数) / (配信数)</span>

{% endapi %}

{% api %}

## メール送信可能 {#emailable}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Emailable' %}

<span class="calculation-line">計算式: カウント</span>

{% endapi %}

{% api %}

## エラー数 {#errors}

{% apitags %}
Webhook
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Errors' %} エラーは<i>送信数</i>に含まれますが、<i>ユニーク受信者数</i>には含まれません。

{% endapi %}

{% api %}

## 推定実開封数 {#estimated-real-opens}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Estimated Real Opens' %}

{% endapi %}

{% api %}

## 失敗数 {#failures}

{% apitags %}
WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Failures' %} 失敗は<i>送信数</i>に含まれますが、<i>配信数</i>には含まれません。</td>

<span class="calculation-line">計算式（<i>失敗率</i>）: (失敗数) / (送信数)</span>

{% endapi %}

{% api %}

## フィーチャーフラグ実験のパフォーマンス {#feature-flag-experiment-performance}

{% apitags %}
Feature Flags
{% endapitags %}

フィーチャーフラグ実験におけるメッセージのパフォーマンス指標です。表示される具体的な指標は、メッセージングチャネルと、実験が多変量テストであったかどうかによって異なります。

{% endapi %}

{% api %}

## ハードバウンス {#hard-bounce}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Hard Bounce' %}

この場合、Brazeはメールアドレスを無効としてマークしますが、ユーザーの[サブスクリプションステータス]({{site.baseurl}}/user_guide/channels/email/subscriptions/)は更新しません。メールがハードバウンスした場合、Brazeはこのメールアドレスへの今後のリクエストを停止します。

{% endapi %}

{% api %}

## ヘルプ {#help}

{% apitags %}
SMS/MMS, RCS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Help' %} ユーザーの返信は、メッセージを受信してから4時間以内にユーザーがインバウンドメッセージを送信した場合に計測されます。

{% endapi %}

{% api %}

## 間接開封数 {#influenced-opens}

{% apitags %}
iOS Push, Android Push
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Influenced Opens' %}

<span class="calculation-line">計算式: (間接開封数) / (配信数)</span>

{% endapi %}

{% api %}

## ライフタイム収益 {#lifetime-revenue}

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Lifetime Revenue' %}

{% endapi %}

{% api %}

## ユーザーあたりのライフタイムバリュー {#lifetime-value-per-user}

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Lifetime Value Per User' %}

{% endapi %}

{% api %}

## 1日あたりの平均収益 {#average-daily-revenue}

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Average Daily Revenue' %}

{% endapi %}

{% api %}

## 1日あたりの購入数 {#daily-purchases}

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Daily Purchases' %}

{% endapi %}

{% api %}

## ユーザーあたりの1日の収益 {#daily-revenue-per-user}

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Daily Revenue Per User' %}

{% endapi %}

{% api %}

## マシン開封数 {#machine-opens}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Machine Opens' %} この指標は、SendGridでは2021年11月11日から、SparkPostでは2021年12月2日から追跡されています。Amazon SESの場合、分析は_開封数_として表示されます。ただし、クリックに対するボットフィルタリングはサポートされます。

{% endapi %}

{% api %}

## 開封数 {#opens}

{% apitags %}
Web Push, iOS Push, Android Push
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Opens' %}

{% endapi %}

{% api %}

## オプトアウト {#opt-out}

{% apitags %}
SMS/MMS, RCS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Opt-Out' %} ユーザーの返信は、メッセージを受信してから4時間以内にユーザーがインバウンドメッセージを送信した場合に計測されます。

{% endapi %}

{% api %}

## その他の開封数 {#other-opens}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Other Opens' %} なお、マシン開封数がログに記録される前に、ユーザーがメールを開封する（その開封数がその他の開封数にカウントされる）こともあります。Apple Mail以外の受信トレイからのマシン開封イベントの後にユーザーがメールを1回（またはそれ以上）開封した場合、ユーザーがメールを開封した回数はその他の開封数に計算され、ユニーク開封数には1回のみカウントされます。

{% endapi %}

{% api %}

## リトライ保留中 {#pending-retry}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Pending Retry' %}

{% endapi %}

{% api %}

## 1次コンバージョン (A) または1次コンバージョンイベント {#primary-conversions-a-or-primary-conversion-event}

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Primary Conversions (A) or Primary Conversion Event' %}

| チャネル | 追加情報 |
|-------|-----------------------|
| メール、プッシュ、Webhook | 初回送信後。|
| Content Cards、アプリ内メッセージ | ユーザーがContent Cardsまたはメッセージを初めて閲覧した時点。|
{: .reset-td-br-1 .reset-td-br-2 aria-label="1次コンバージョン (A) または1次コンバージョンイベント" }

{::nomarkdown}
<span class="calculation-line">
    計算式:
    <ul>
        <li><i>1次コンバージョン (A) または1次コンバージョンイベント</i>: カウント</li>
        <li><i>1次コンバージョン (A) 率</i>または<i>1次コンバージョンイベント率</i>: (1次コンバージョン数) / (ユニーク受信者数)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

## 既読数 {#reads}

{% apitags %}
WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Reads' %}

{% endapi %}

{% api %}

## 既読率 {#read-rate}

{% apitags %}
WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Read Rate' %}

<span class="calculation-line">計算式: (開封確認付き既読数) / (送信数)</span>

{% endapi %}

{% api %}

## 受信済み {#received}

{% apitags %}
Email, Content Cards, In-App Message, Web Push, iOS Push, Android Push, SMS/MMS, WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Received' %}

| チャネル | 追加情報 |
|-------|-------|
| Content Cards | ユーザーがアプリ内でカードを閲覧した時点で受信済みとなります。|
| プッシュ | Brazeサーバーからプッシュプロバイダーにメッセージが送信された時点で受信済みとなります。|
| メール | Brazeサーバーからメールサービスプロバイダーにメッセージが送信された時点で受信済みとなります。|
| SMS/MMS | SMSプロバイダーが上流キャリアおよび送信先デバイスから確認を受信した後に「配信済み」となります。|
| アプリ内メッセージ | 定義されたトリガーアクションに基づいて表示された時点で受信済みとなります。|
| WhatsApp | 定義されたトリガーアクションに基づいて表示された時点で受信済みとなります。|
{: .reset-td-br-1 .reset-td-br-2 aria-label="受信済み" }

{% endapi %}

{% api %}

## RCS拒否数またはSMS拒否数 {#rcs-rejections-or-sms-rejections}

{% apitags %}
SMS/MMS, RCS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Rejections' %} Brazeの顧客として、拒否はSMS割り当てに対して課金されます。

{::nomarkdown}
<span class="calculation-line">
    計算式:
    <ul>
        <li><i>拒否数</i>: カウント</li>
        <li><i>拒否率</i>: (拒否数) / (送信数)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

## 収益 {#revenue}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Revenue' %}

{% endapi %}

{% api %}

## 送信済み {#sent}

{% apitags %}
SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Sent' %}

<span class="calculation-line">計算式: カウント</span>

{% endapi %}

{% api %}

## 送信数 {#sends}

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, RCS, WhatsApp, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Sends' %} この指標はBrazeによって提供されます。スケジュールされたCampaignを起動すると、この指標にはレート制限によりまだ送信されていないメッセージも含め、送信されたすべてのメッセージが含まれます。

{% alert tip %}
Content Cardsの場合、この指標は[カード作成]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card/card_creation/)で選択した内容によって計算方法が異なります。

- **起動時またはステップエントリ時:** 作成され、閲覧可能なカードの数です。ユーザーがカードを閲覧したかどうかはカウントされません。
- **初回インプレッション時:** ユーザーに表示されたカードの数です。
{% endalert %}

<span class="calculation-line">計算式: カウント</span>

{% endapi %}

{% api %}

## 送信メッセージ数 {#messages-sent}

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, WhatsApp, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Messages Sent' %} この指標はBrazeによって提供されます。スケジュールされたCampaignを起動すると、この指標にはレート制限によりまだ送信されていないメッセージも含め、送信されたすべてのメッセージが含まれます。

{% alert tip %}
Content Cardsの場合、この指標は[カード作成]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card/card_creation/)で選択した内容によって計算方法が異なります。

- **起動時またはステップエントリ時:** 作成され、閲覧可能なカードの数です。ユーザーがカードを閲覧したかどうかはカウントされません。
- **初回インプレッション時:** ユーザーに表示されたカードの数です。
{% endalert %}

<span class="calculation-line">計算式: カウント</span>

{% endapi %}

{% api %}

## キャリアへの送信数 {#sends-to-carrier}

{% apitags %}
SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Sends to Carrier' %}

{::nomarkdown}
<span class="calculation-line">
    計算式:
    <ul>
        <li><i>キャリアへの送信数</i>: カウント</li>
        <li><i>キャリアへの送信率</i>: (キャリアへの送信数) / (送信数)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

## ソフトバウンス {#soft-bounce}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Soft Bounce' %} メールがソフトバウンスした場合、通常72時間以内にリトライしますが、リトライ回数は受信者によって異なります。

_ソフトバウンス_は_遅延_とは異なります。このリトライ期間中にメールが正常に配信されなかった場合、Brazeは試行されたCampaign送信ごとに1つのソフトバウンスイベントを送信します。2025年2月25日以前は、これらのリトライは1回のCampaign送信に対して複数のソフトバウンスとしてカウントされていました。

ソフトバウンスはCampaign分析では追跡されませんが、[メッセージアクティビティログ]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log/)で監視できます。また、これらのユーザーを送信から除外したり、[ソフトバウンスSegmentフィルター]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters/#soft-bounced)を使用して過去30日間のソフトバウンス数を確認したりすることもできます。メッセージアクティビティログでは、ソフトバウンスの理由を確認し、メールキャンペーンの「送信数」と「配信数」の間の差異を理解することもできます。

{% endapi %}

{% api %}

## スパム {#spam}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Spam' %}

{% alert note %}
スパム報告はメールサービスプロバイダーによって直接処理され、フィードバックループを通じてBrazeに中継されます。ほとんどのフィードバックループは実際の報告の一部のみを報告するため、_スパム_指標は実際の合計の一部を表すことが多いです。メールサービスプロバイダーのみがスパム報告の実際の量を確認できるため、_スパム_は網羅的ではなく、参考指標として捉えてください。
{% endalert %}

{::nomarkdown}
<span class="calculation-line">
    計算式:
    <ul>
        <li><i>スパム</i>: カウント</li>
        <li><i>スパム率</i>: (スパムとしてマーク) / (送信数)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

## 調査ページの却下数 {#survey-page-dismissals}

{% apitags %}
In-App Message
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Survey Page Dismissals' %}

{% endapi %}

{% api %}

## 調査の送信数 {#survey-submissions}

{% apitags %}
In-App Message
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Survey Submissions' %}

{% endapi %}

{% api %}

## 合計クリック数 {#total-clicks}

{% apitags %}
Email, Content Cards, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Clicks' %}

| チャネル | 追加情報 |
|-------|-------|
| LINE | 1日あたり最低20メッセージのしきい値に達した後に追跡されます。AMPメールにはHTMLおよびプレーンテキストバージョンの両方で記録されたクリックが含まれます。この数値はスパム対策ツールによって人為的に膨らむ場合があります。|
| バナー | 配信されたメッセージ内でクリックしたユーザーの合計数（および割合）です。同じユーザーが複数回クリックした場合も含まれます。|
{: .reset-td-br-1 .reset-td-br-2 aria-label="合計クリック数" }

{::nomarkdown}
<span class="calculation-line">
    計算式:
    <ul>
        <li><b>メール:</b> (合計クリック数) / (配信数)</li>
        <li><b>Content Cards:</b> (合計クリック数) / (合計インプレッション数)</li>
        <li><b>SMS:</b> (クリック開封数) / (配信数)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

## 合計却下数 {#total-dismissals}

{% apitags %}
Content Cards, Banners
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Dismissals' %} Content Cardsの場合、ユーザーが同じCampaignから2つの異なるカードを受信し、両方を却下した場合、このカウントは2増加します。再適格性を使用すると、ユーザーがカードを受信するたびに_合計却下数_を1回ずつ増加させることができます。各カードは異なるメッセージです。バナーの場合、却下動作が有効になっている場合に各却下がカウントされます。

{::nomarkdown}
<span class="calculation-line">
    計算式:
    <ul>
        <li><i>合計却下数:</i> カウント</li>
        <li><i>合計却下率:</i> 合計却下数 / 合計インプレッション数</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

## 合計インプレッション数 {#total-impressions}

{% apitags %}
In-App Message, Content Cards
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Impressions' %} この数値は、BrazeがSDKから受信したインプレッションイベントの合計です。

| チャネル | 追加情報 |
|-------|-----------------------|
| Content Cards | 特定のContent Cardsに対して記録されたインプレッションの合計数です。同じユーザーに対して複数回増加する可能性があります。|
| アプリ内メッセージ | 複数のデバイスがあり、再適格性がオフの場合、ユーザーはアプリ内メッセージを1回のみ表示されます。ユーザーが複数のデバイスを使用していても、最初にターゲットされたデバイスでのみ表示されます。これは、プロファイルがデバイスを統合しており、ユーザーがデバイス間で1つのユーザーIDでログインしていることを前提としています。再適格性がオンの場合、ユーザーがアプリ内メッセージを表示するたびにインプレッションが記録されます。詳細については、<a href="/docs/user_guide/channels/in_app_messages/reporting/">アプリ内メッセージレポート</a> を参照してください。|
{: .reset-td-br-1 .reset-td-br-2 aria-label="合計インプレッション数" }

<span class="calculation-line">計算式: カウント</span>

{% endapi %}

{% api %}

## 合計開封数 {#total-opens}

{% apitags %}
Email, iOS Push, Android Push, Web Push, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Opens' %}

| チャネル | 追加情報 |
|-------|-----------------------|
| LINE | 1日あたり最低20メッセージのしきい値に達した後に追跡されます。|
| AMPメール | HTMLおよびプレーンテキストバージョンの合計開封数です。|
{: .reset-td-br-1 .reset-td-br-2 aria-label="合計開封数" }

{::nomarkdown}
<span class="calculation-line">
    計算式:
    <ul>
        <li><b>メール<i>合計開封数</i>:</b> カウント</li>
        <li><b>メール<i>合計開封率</i>:</b> (開封数) / (配信数)</li>
        <li><b>Webプッシュ<i>合計開封数</i>:</b> <i>直接開封数</i>のカウント</li>
        <li><b>Webプッシュ<i>合計開封率</i>:</b> (合計開封数) / (配信数)</li>
        <li><b>iOS、Android、Kindleプッシュ<i>合計開封数</i>:</b> (直接開封数) + (間接開封数)</li>
        <li><b>iOS、Android、Kindleプッシュ<i>合計開封率</i>:</b> (合計開封数) / (配信数)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

## 合計収益 {#total-revenue}

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Revenue' %} この指標は、<a href='/docs/user_guide/analytics/reports/report_builder'>レポートビルダー</a> を通じたCampaign比較レポートでのみ利用可能です。

{% endapi %}

{% api %}

## ユニーククリック数 {#unique-clicks}

{% apitags %}
Email, Content Cards, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Clicks' %}

これには、Brazeが提供する配信停止リンクのクリックが含まれます。

| チャネル | 追加情報 |
|-------|-----------------------|
| メール | 7日間にわたって追跡されます。|
| LINE | 1日あたり最低20メッセージのしきい値に達した後に追跡されます。|
{: .reset-td-br-1 .reset-td-br-2 aria-label="ユニーククリック数" }

{::nomarkdown}
<span class="calculation-line">
    計算式:
    <ul>
        <li><i>ユニーククリック数</i>: カウント</li>
        <li><b>Content Cards</b> <i>ユニーククリック率</i>: (ユニーククリック数) / (ユニークインプレッション数)</li>
        <li><b>メール</b> <i>ユニーククリック率</i>: (ユニーククリック数) / (配信数)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

## ユニーク却下数 {#unique-dismissals}

{% apitags %}
Content Cards
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Dismissals' %}

<span class="calculation-line">計算式: (ユニーク却下数) / (ユニークインプレッション数)</span>

{% endapi %}

{% api %}

## ユニークデイリーインプレッション数 {#unique-daily-impressions}

{% apitags %}
Content Cards, Banners
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Daily Impressions' %}

この数値はBrazeから受信され、`user_id`に基づいています。ユニークデイリーインプレッション数はCampaignまたはCanvasステップレベルでカウントされます。

<span class="calculation-line">計算式: カウント</span>

{% endapi %}

{% api %}

## ユニークインプレッション数 {#unique-impressions}

{% apitags %}
In-App Message, Content Cards
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Impressions' %}

| チャネル | 追加情報 |
|-------|-----------------------|
| アプリ内メッセージ | 再適格性がオンでユーザーがトリガーアクションを実行した場合、ワークスペースのタイムゾーンにおける新しい暦日にユニークインプレッション数が再度増加する可能性があります。再適格性がオンの場合、<i>ユニークインプレッション数</i> = <i>ユニーク受信者数</i>となります。詳細については、<a href="/docs/user_guide/channels/in_app_messages/reporting/">アプリ内メッセージレポート</a> を参照してください。|
| Content Cards | ユーザーがカードを2回目に閲覧しても、カウントは増加しません。|
{: .reset-td-br-1 .reset-td-br-2 aria-label="ユニークインプレッション数" }

<span class="calculation-line">計算式: カウント</span>

{% endapi %}

{% api %}

## ユニーク開封数 {#unique-opens}

{% apitags %}
Email, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Opens' %}

| チャネル | 追加情報 |
|-------|-----------------------|
| メール | 7日間にわたって追跡されます。|
| LINE | 1日あたり最低20メッセージのしきい値に達した後に追跡されます。|
{: .reset-td-br-1 .reset-td-br-2 aria-label="ユニーク開封数" }

{::nomarkdown}
<span class="calculation-line">
    計算式:
    <ul>
        <li><i>ユニーク開封数</i>: カウント</li>
        <li><i>ユニーク開封率</i>: (ユニーク開封数) / (配信数)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

## ユニーク受信者数 {#unique-recipients}

{% apitags %}
Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, RCS, WhatsApp, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Recipients' %}

閲覧者は毎日ユニーク受信者になり得るため、この数値は<i>ユニークインプレッション数</i>よりも高くなることが予想されます。この数値はBrazeから受信され、`user_id`に基づいています。ユニーク受信者数はCampaignまたはCanvasステップレベルでカウントされ、<a href='{{ site.homeurl }}{{ site.baseurl }}/api/identifier_types/#send-identifier'>送信識別子</a> レベルではカウントされません。

<span class="calculation-line">計算式: カウント</span>

{% endapi %}

{% api %}

## 配信停止者数 {#unsubscribers-or-unsub}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unsubscribers or Unsub' %}

{::nomarkdown}
<span class="calculation-line">
    計算式:
    <ul>
        <li><i>配信停止者数</i>: カウント</li>
        <li><i>配信停止率</i>: (配信停止数) / (配信数)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

## 配信停止数 {#unsubscribes}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unsubscribes' %}

<span class="calculation-line">計算式: (配信停止数) / (配信数)</span>

{% endapi %}

{% api %}

## バリエーション {#variation}

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Variation' %}

<span class="calculation-line">計算式: カウント</span>

{% endapi %}