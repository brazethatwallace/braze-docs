---
nav_title: API使用アラート
article_title: API使用状況アラート
description: "この記事では、予期しないトラフィックを事前に検出できるAPI使用状況アラートの概要を説明します。"
page_order: 0
---

# API使用アラート {#api-usage-alerts}

> API使用状況アラートは、APIの使用状況を可視化する重要な手段であり、予期しないトラフィックを事前に検知できます。これらのアラートを設定して主要なAPIリクエスト量をトラッキングすることで、リアルタイムで通知を受け取り、問題がマーケティングキャンペーンに影響を与える前に対処できます。

## API使用アラートについて {#about-api-usage-alerts}

API使用状況アラートを使用して、以下のカテゴリのリクエスト量を監視できます。

| APIカテゴリ | 詳細 |
|--------------|---------|
| REST APIエンドポイント | Brazeのバックエンドに対して行われたすべてのREST API呼び出しの使用状況をトラッキングします。例えば、メッセージの送信、キャンペーンの作成、ユーザーのエクスポートなどです。 |
| SDK APIリクエスト | Braze SDKからクライアントアプリに対して行われるAPIリクエストをトラッキングします。例えば、アプリ内メッセージのトリガーやユーザーデータの同期などです。<br><br>_*「月間アクティブユーザー – CY 24-25」を購入したお客様のみ利用可能です。_ |
{: .reset-td-br-1 .reset-td-br-2 aria-label="API使用アラートについて" }

## API使用アラートの作成 {#creating-an-api-usage-alert}

API使用アラートを作成するには：

1. **設定** > **APIキー** > **API使用量アラート**に移動し、新しいアラートを作成します。
2. アラートの名前を入力し、通知を受け取りたいREST APIエンドポイントとAPIキーを選択します。
3. 1つ以上の応答コードを選択し、[アラートしきい値](#api-usage-alert-thresholds)を指定してアラート基準を定義します。
4. 完了したら、**Alert enabled**をオンに切り替えます。
    ![API使用アラートの例。Track usersエンドポイントが1時間以内に100％増加した場合に通知を送信します。]({% image_buster /assets/img/api_usage_alerts/api_usage_alerts1.png %})

## アラートしきい値 {#api-usage-alert-thresholds}

アラート基準を定義する際に、以下のしきい値を調整できます。

<table aria-label="アラートしきい値">
  <caption>アラートしきい値</caption>
  <thead>
    <tr>
      <th>フィールド</th>
      <th>説明</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>しきい値条件</td>
      <td>
        通知を受けたいしきい値ボリュームに至るまでの条件を定義します。以下がサポートされています。<br><br>
        <ul>
          <li><strong>Increased by</strong>または<strong>Decreased by</strong>：リクエストを前回の時間枠と比較します。</li>
          <li><strong>Increased by percentage</strong>または<strong>Decreased by percentage</strong>：リクエストのパーセント変化を前回の時間枠と比較します。</li>
          <li><strong>Greater than or equal</strong>または<strong>less than or equal</strong>：時間枠内のリクエストをカウントします。</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>しきい値ボリューム</td>
      <td>しきい値条件と組み合わせて使用します。</td>
    </tr>
    <tr>
      <td>Within (範囲内)</td>
      <td>アラート評価の時間枠です。</td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 aria-label="アラートしきい値" }

## アラート通知の設定 {#setting-up-alert-notifications}

メールアラート、Webhookアラート、またはその両方を設定できます。Webhookアラートは、Slackチャネルなどの外部プラットフォームにアラートを送信するようなユースケースに非常に便利です。例については、通知設定でSlackと連携する方法に関する[ドキュメント]({{site.baseurl}}/user_guide/administer/global/admin_settings/notification_preferences/#slack-incoming-webhook-integration)をご覧ください。

![アラートの基準に達すると、選択したメールアドレスにメールが送信されます。]({% image_buster /assets/img/api_usage_alerts/api_usage_alerts2.png %})

### サンプルペイロード {#payload}

以下は、API使用状況アラートWebhookのボディのサンプルペイロードです。

```json
{
  "data": {
    "alert_name": "My First API Usage Alert",
    "alert_type": "API Usage Alert",
    "alert_criteria": {
    	"response_codes": ["201", "202", "203"],
    	"threshold_condition": "Increased by %",
    	"threshold_volume": 50,
    	"within": "1 day"
    },
    "timeframe_start": "2025-03-20T15:35:00Z",
    "timeframe_end": "2025-03-20T16:35:00Z",
    "volume": 1500,
    "previous_timeframe_start": "2025-03-20T14:35:00Z",
    "previous_timeframe_end": "2025-03-20T15:35:00Z",
    "previous_volume": 1000
  },
  "text": "Your My First API Usage Alert alert has triggered. You can view your alert and usage here: <link>. Note that this alert will reset in 1 day, as each alert will only send one notification per 8 hours."
}
```

### アラートの例 {#example-alerts}

以下のシナリオで通知を受け取るためのAPI使用状況アラート設定の例をいくつか紹介します。

{% tabs local %}
{% tab APIの健全性 %}
APIの全般的な健全性を監視するためのアラートを設定できます。例えば、APIエラーが前の1時間から20%など大幅に増加した場合にアラートを設定できます。

| エンドポイント | APIキー | 応答コード | しきい値条件 | しきい値ボリューム | 時間枠 |
| --- | --- | --- | --- | --- | --- |
| すべてのエンドポイント | すべてのAPIキー | `4XX` および `5XX` | 10%増加 | 10 | 1時間 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 aria-label="アラートの例" }
{% endtab %}

{% tab エンドポイントのレート制限 %}
ワークスペースが `/users/track` エンドポイントのレート制限に達した場合にアラートを受け取ります。この設定は他のBrazeエンドポイントにも適用できます。

| エンドポイント | APIキー | 応答コード | しきい値条件 | しきい値ボリューム | 時間枠 |
| --- | --- | --- | --- | --- | --- |
| `/users/track` | すべてのAPIキー | `429` | 以上 | 100 | 1時間 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 aria-label="アラートの例" }
{% endtab %}

{% tab APIトリガーのキャンペーン %}
このアラート設定は、APIトリガーのキャンペーンやキャンバスでエラーが発生した場合に通知します。これらの中には優先度の高いものも含まれる場合があります。

| エンドポイント | APIキー | 応答コード | しきい値条件 | しきい値ボリューム | 時間枠 |
| --- | --- | --- | --- | --- | --- |
| {::nomarkdown}<ul><li><code>/campaigns/trigger/send</code></li><li><code>/canvas/trigger/send</code></li><li><code>/messages/send</code></li></ul>{:/} | すべてのAPIキー | `4XX` および `5XX` | 以上 | 1 | 1時間 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 aria-label="アラートの例" }
{% endtab %}

{% tab パートナー連携 %}
パートナー連携がBrazeへのデータ送信を停止した場合にアラートを受け取るには、以下のアラート設定を使用します。

| エンドポイント | APIキー | 応答コード | しきい値条件 | しきい値ボリューム | 時間枠 |
| --- | --- | --- | --- | --- | --- |
| すべてのエンドポイント | パートナー連携に使用しているAPIキー | すべての応答コード | 以下 | 0 | 1日 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 aria-label="アラートの例" }
{% endtab %}
{% endtabs %}

## 注意事項 {#considerations}

- 各アクティブアラートは、メールまたはWebhook通知を8時間に1回のみ送信します。これは、1つのアラートから過剰な通知が送信されるのを防ぐためです。アラートが早すぎるタイミングで通知される場合は、ユースケースに合うようにアラート基準を編集することを検討してください。
- ワークスペースごとに最大10個のアラートを設定できます。