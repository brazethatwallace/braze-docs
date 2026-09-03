---
nav_title: API使用アラート
article_title: API使用状況アラート
description: "この記事では、予期しないトラフィックを事前に検出できるAPI使用状況アラートの概要を説明します。"
page_order: 0
---

# API使用アラート {#api-usage-alerts}

> API使用状況アラートは、APIの使用状況を可視化する重要な手段であり、予期しないトラフィックを事前に検知できます。これらのアラートを設定して主要なAPIリクエスト量をトラッキングすることで、リアルタイムで通知を受け取り、問題がマーケティングキャンペーンに影響を与える前に対処できます。

## API 使用量アラートについて {#about-api-usage-alerts}

API 使用量アラートを使用すると、以下のカテゴリのリクエスト量を監視できます。

| API カテゴリ | 詳細 |
|--------------|---------|
| REST API エンドポイント | メッセージの送信、キャンペーンの作成、ユーザーのエクスポートなど、Brazeのバックエンドに対するすべてのREST API呼び出しの使用状況を追跡します。 |
| SDK API リクエスト | アプリ内メッセージのトリガーやユーザーデータの同期など、クライアントアプリのBraze SDKから行われたAPIリクエストを追跡します。<br><br>_*月間アクティブユーザー数 – CY 24-25を購入した顧客のみ利用可能です。_ |
{: .reset-td-br-1 .reset-td-br-2 aria-label="API 使用量アラートについて" }

## API使用量アラートの作成 {#creating-an-api-usage-alert}

API使用量アラートを作成するには、以下の手順に従います。

1. **設定** > **APIと識別子** > **API使用量アラート**に移動し、新しいアラートを作成します。
2. アラートの名前を入力し、アラートを受け取りたいREST APIエンドポイントとAPIキーを選択します。
3. 1つ以上のレスポンスコードを選択し、[アラートしきい値](#api-usage-alert-thresholds)を指定して、アラート条件を定義します。
4. 完了したら、**アラートを有効化**をオンに切り替えます。
    ![1時間以内にTrack usersエンドポイントが100パーセント増加した場合に通知を送信するAPI使用量アラートの例。]({% image_buster /assets/img/api_usage_alerts/api_usage_alerts1.png %})

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
      <td>Within（範囲内）</td>
      <td>アラート評価の時間枠です。</td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 aria-label="アラートしきい値" }

## アラート通知の設定 {#setting-up-alert-notifications}

メールアラート、Webhookアラート、またはその両方を設定できます。Webhookアラートは、Slackチャネルなどの外部プラットフォームにアラートを送信するようなユースケースに非常に便利です。例については、通知設定のためにSlackとアラートを連携する方法についての[ドキュメント]({{site.baseurl}}/user_guide/administer/global/admin_settings/notification_preferences)を参照してください。

![アラートの条件に達すると、選択したメールアドレスにメールが送信されます。]({% image_buster /assets/img/api_usage_alerts/api_usage_alerts2.png %})

### サンプルペイロード {#payload}

以下は、API使用量アラートWebhookのボディのサンプルペイロードです。

```json
{
  "text": "Your My First API Usage Alert alert has triggered. Please note that this alert is reset every 8 hours, and only one notification will be sent per reset period. You can view your alert and usage here: <link>.",
  "data": {
    "alert_name": "My First API Usage Alert",
    "alert_type": "API Usage Alert",
    "app_group_name": "My Workspace",
    "alert_criteria": {
      "response_codes": "201, 202 and 203",
      "threshold_condition": "increase by",
      "threshold_volume": "50%",
      "within": "1 hour"
    },
    "timeframe_start": "2025-03-20 15:35:00",
    "timeframe_end": "2025-03-20 16:35:00",
    "volume": 1500,
    "previous_timeframe_start": "2025-03-20 14:35:00",
    "previous_timeframe_end": "2025-03-20 15:35:00",
    "previous_volume": 1000
  }
}
```

{% alert note %}
`previous_timeframe_start`、`previous_timeframe_end`、および`previous_volume`フィールドはオプションであり、アラートが比較しきい値条件（`increase by`、`decrease by`）を使用する場合にのみ表示されます。これらのフィールドは、`greater than or equal`または`less than or equal`アラートでは省略されます。
{% endalert %}

#### ペイロードフィールドの詳細 {#payload-field-details}

| フィールド | タイプ | 説明 |
|-------|------|-------------|
| `text` | string | 人間が読めるアラートメッセージ。 |
| `data.alert_name` | string | アラートの名前。 |
| `data.alert_type` | string | アラートのタイプ（常に`"API Usage Alert"`）。 |
| `data.app_group_name` | string | ワークスペース名。 |
| `data.alert_criteria.response_codes` | string | アラートに選択されたレスポンスコード。何も選択されていない場合は`"all response codes"`を返し、単一のコードの場合は`"201"`、複数のコードの場合は`"201, 202 and 203"`のように返します。 |
| `data.alert_criteria.threshold_condition` | string | 条件タイプ：`"increase by"`、`"decrease by"`、`"greater than or equal"`、または`"less than or equal"`。 |
| `data.alert_criteria.threshold_volume` | string または number | しきい値。条件がパーセンテージを使用する場合は`%`で終わる文字列です（例：`"50%"`）。条件が数値を使用する場合は数値です（例：`50`）。 |
| `data.alert_criteria.within` | string | アラート評価の時間ウィンドウ（例：`"1 day"`）。 |
| `data.timeframe_start` | string | UTC形式`YYYY-MM-DD HH:MM:SS`でのアラート期間の開始。 |
| `data.timeframe_end` | string | UTC形式`YYYY-MM-DD HH:MM:SS`でのアラート期間の終了。 |
| `data.volume` | number | アラート期間中のリクエストボリューム。 |
| `data.previous_timeframe_start` | string | （オプション）前の期間の開始。比較しきい値条件の場合にのみ存在します。 |
| `data.previous_timeframe_end` | string | （オプション）前の期間の終了。比較しきい値条件の場合にのみ存在します。 |
| `data.previous_volume` | number | （オプション）前の期間中のリクエストボリューム。比較しきい値条件の場合にのみ存在します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="ペイロードフィールドの詳細" }

### アラートの設定例 {#example-alerts}

以下のシナリオで通知を受け取るためのAPI使用量アラート設定の方法をいくつか紹介します。

{% tabs local %}
{% tab APIの健全性 %}
APIの全般的な健全性を監視するためのアラートを設定できます。たとえば、APIエラーが前の1時間から20%のように大幅に増加した場合にアラートを設定できます。

| エンドポイント | APIキー | レスポンスコード | しきい値条件 | しきい値ボリューム | 期間 |
| --- | --- | --- | --- | --- | --- |
| すべてのエンドポイント | すべてのAPIキー | `4XX`および`5XX` | 10%増加 | 10 | 1時間 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 aria-label="アラートの設定例" }
{% endtab %}

{% tab エンドポイントのレート制限 %}
ワークスペースが`/users/track`エンドポイントのレート制限に達した場合にアラートを受け取ります。この設定は他のBrazeエンドポイントにも適用できます。

| エンドポイント | APIキー | レスポンスコード | しきい値条件 | しきい値ボリューム | 期間 |
| --- | --- | --- | --- | --- | --- |
| `/users/track` | すべてのAPIキー | `429` | 以上 | 100 | 1時間 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 aria-label="アラートの設定例" }
{% endtab %}

{% tab APIトリガーキャンペーン %}
このアラート設定は、APIトリガーのキャンペーンやキャンバスでエラーが発生した場合に通知します。これらの中には優先度の高いものが含まれる場合があります。

| エンドポイント | APIキー | レスポンスコード | しきい値条件 | しきい値ボリューム | 期間 |
| --- | --- | --- | --- | --- | --- |
| {::nomarkdown}<ul><li><code>/campaigns/trigger/send</code></li><li><code>/canvas/trigger/send</code></li><li><code>/messages/send</code></li></ul>{:/} | すべてのAPIキー | `4XX`および`5XX` | 以上 | 1 | 1時間 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 aria-label="アラートの設定例" }
{% endtab %}

{% tab パートナー連携 %}
パートナー連携がBrazeへのデータ送信を停止した場合にアラートを受け取るには、以下のアラート設定を使用します。

| エンドポイント | APIキー | レスポンスコード | しきい値条件 | しきい値ボリューム | 期間 |
| --- | --- | --- | --- | --- | --- |
| すべてのエンドポイント | パートナー連携に使用しているAPIキー | すべてのレスポンスコード | 以下 | 0 | 1日 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 aria-label="アラートの設定例" }
{% endtab %}
{% endtabs %}

## 注意事項 {#considerations}

- 各アクティブアラートは、メールまたはWebhook通知を8時間ごとに1回のみ送信します。これは、単一のアラートから通知が過剰に送信されるのを防ぐためです。アラートが早すぎるタイミングで通知を送る場合は、ユースケースに合うようにアラート条件の編集を検討してください。
- ワークスペースごとに最大10個のアラートを設定できます。