---
nav_title: Webhookとコネクテッドコンテンツのトラブルシューティング
article_title: Webhookとコネクテッドコンテンツリクエストのトラブルシューティング
page_order: 4
description: "症状インデックス、HTTPエラーテーブル、異常ホスト検出のガイダンスを使用して、Webhookとコネクテッドコンテンツのエラーを診断します。"
---

# Webhookとコネクテッドコンテンツリクエストのトラブルシューティング {#troubleshoot-webhook-and-connected-content-requests}

> このページでは、Webhookとコネクテッドコンテンツの一般的なエラーコードのトラブルシューティング方法について説明します。設定については、[Webhookの作成]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook)と[API呼び出しの実行]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call)を参照してください。

## ここから始めましょう：症状を照合する {#start-here-match-your-symptom}

以下の表で症状を照合し、該当するセクションに移動してください。

| 症状 | 移動先 |
| --- | --- |
| メッセージアクティビティログの `4XX` クライアントエラー | [4XX エラー](#4xx-errors) |
| `5XX` サーバーエラーまたはタイムアウト | [5XX エラー](#5xx-errors) |
| `598 Host Unhealthy` またはリクエストの一時的な停止 | [異常なホストの検出]({{site.baseurl}}/support_contact) |
| Connected Contentがプレビューまたは送信時に空白で表示される | [Connected Contentがレスポンスボディを返さない](#connected-content-returns-no-response-body) |
| Brazeからの自動エラーメール | [自動メールとメッセージアクティビティログのエントリ](#automated-emails-and-message-activity-log-entries) |
| Currentsでwebhookの失敗イベントが必要 | [Braze Currentsでの追加の失敗インサイト](#additional-failure-insights-in-braze-currents) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="webhookとConnected Contentの症状" }

## 標準的な調査パス {#standard-investigation-path}

Webhookまたは Connected Content リクエストが失敗したり、正しくレンダリングされない場合は、このワークフローを使用してください。ステップ1から開始します。

1. [メッセージアクティビティログ]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log)を開き、エラーコード、タイムスタンプ、エンドポイントURLを確認します。
2. `4XX` エラーの場合、エンドポイントのドキュメントと照らし合わせて、リクエスト構文、認証ヘッダー、URLパス、HTTPメソッドを確認します。
3. `5XX` エラーの場合、エンドポイントの正常性、レート制限、およびBrazeがそのホストを異常と判定していないかを確認します。
4. Connected Contentの場合、テストユーザーでメッセージをプレビューし、Liquidが空白やJSONを破壊する値に解決されていないことを確認します。
5. 異常ホスト検出が関係している可能性がある場合は、[Brazeサポート](#unhealthy-host-detection)に連絡する前に[異常ホスト検出](#unhealthy-host-detection)を確認してください。

## 4XX エラー {#4xx-errors}

`4XX` エラーは、エンドポイントに送信されたリクエストに問題があることを示します。これらのエラーは通常、不正なパラメーター、認証ヘッダーの欠落、不正な URL など、誤ったリクエストが原因で発生します。これらのエラーは[レポートビルダー]({{site.baseurl}}/user_guide/analytics/reports/report_builder)にも適用されます。

エラーコードの詳細と解決手順については、以下の表を参照してください。

<style>
table td {
    word-break: break-word;
}
</style>

<table aria-label="4XX エラー">
  <thead>
    <tr>
      <th>エラーコード</th>
      <th>意味</th>
      <th>解決手順</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>400 Bad Request</b></td>
      <td>リクエストに無効な構文があります。</td>
      <td>
        <ul>
          <li>リクエストペイロードに構文エラーがないか確認してください。</li>
          <li>すべての必須フィールドが含まれ、正しくフォーマットされていることを確認してください。</li>
          <li>JSON ペイロードを送信している場合は、JSON 構造を検証してください。</li>
          <li>Liquid を使用して Webhook リクエストにパーソナライゼーションタグをテンプレート化している場合は、Liquid が空白の値に解決されたり、JSON を壊す文字（エスケープされていない引用符など）を生成したりしないことを確認してください。テストユーザーでメッセージをプレビューして、レンダリングされた出力が有効であることを確認してください。</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>401 Unauthorized</b></td>
      <td>リクエストにはユーザー認証が必要です。</td>
      <td>
        <ul>
          <li>正しい認証情報（API キーやトークンなど）がリクエストヘッダーに含まれていることを確認してください。</li>
          <li>エンドポイントにアクセスするためのユーザー権限があることを確認してください。</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>403 Forbidden</b></td>
      <td>エンドポイントはリクエストを理解しましたが、承認を拒否しました。</td>
      <td>
        <ul>
          <li>API キーまたはトークンに必要な権限があるか確認してください。</li>
          <li>エンドポイントにアクセスするためのユーザー権限があることを確認してください。</li>
          <li>リクエストが一貫して <code>403</code> を返し、認証が正しいように見える場合、サーバー、API ゲートウェイ、または WAF が Braze の送信 IP アドレスをブロックしている可能性があります。Braze クラスターの IP を許可リストに追加してください。Webhook については、<a href="{{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook#ip-allowlisting">IP 許可リスト</a> を参照してください。Connected Content については、<a href="{{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call#connected-content-ip-allowlisting">Connected Content IP 許可リスト</a> を参照してください。</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>404 Not Found</b></td>
      <td>エンドポイントがリクエストされたリソースを見つけることができません。</td>
      <td>
        <ul>
          <li>エンドポイント URL にタイプミスや不正なパスがないか確認してください。</li>
          <li>アクセスしようとしているリソースが存在することを確認してください。</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>405 Method Not Allowed</b></td>
      <td>リクエストメソッドはエンドポイントに認識されていますが、対象リソースではサポートされていません。</td>
      <td>
        <ul>
          <li>リクエストで使用されている HTTP メソッド（DELETE、GET、POST、PUT）を確認してください。</li>
          <li>エンドポイントが使用しているメソッドをサポートしていることを確認してください。</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>408 Request Timeout</b></td>
      <td>エンドポイントがリクエストの処理中にタイムアウトしました。</td>
      <td>
        <ul>
          <li>リクエストで使用されている HTTP メソッド（DELETE、GET、POST、PUT）を確認してください。</li>
          <li>エンドポイントが使用しているメソッドをサポートしていることを確認してください。</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>409 Conflict</b></td>
      <td>リソースの現在の状態との競合により、リクエストが完了しませんでした。</td>
      <td>
        <ul>
          <li>リクエストで使用されている HTTP メソッド（DELETE、GET、POST、PUT）を確認してください。</li>
          <li>エンドポイントが使用しているメソッドをサポートしていることを確認してください。</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>429 Too Many Requests</b></td>
      <td>一定時間内に送信されたリクエストが多すぎます。</td>
      <td>
        <ul>
          <li>キャンペーンまたはキャンバスステップのレート制限を下げてください。</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

## 5XX エラー {#5xx-errors}

`5XX` エラーは、エンドポイントに問題があることを示します。これらのエラーは通常、サーバー側の問題が原因で発生します。

| エラーコード                    | 意味                                                                                                                                         |
|-------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| **500 Internal Server Error** | エンドポイントがリクエストの完了を妨げる予期しない状態に遭遇しました。                                                       |
| **502 Bad Gateway**           | エンドポイントが上流サーバーから無効なレスポンスを受信しました。                                                                                   |
| **503 Service Unavailable**   | エンドポイントは一時的な過負荷またはメンテナンスのため、現在リクエストを処理できません。                                                    |
| **504 Gateway Timeout**       | エンドポイントが上流サーバーからタイムリーなレスポンスを受信できませんでした。                                                                               |
| **529 Host Overloaded**       | エンドポイントのホストが過負荷状態で応答できませんでした。 |
| **598 Host Unhealthy**        | エンドポイントのホストが一時的に異常とマークされているため、Brazeがレスポンスをシミュレートしました。詳細については、[異常ホスト検出](#unhealthy-host-detection)を参照してください。 |
| **599 Connection Error**      | Brazeがエンドポイントへの接続を確立しようとした際にネットワーク接続タイムアウトエラーが発生しました。エンドポイントが不安定またはダウンしている可能性があります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="5XX エラー" }

### 5XX エラーの解決 {#resolving-5xx-errors}

一般的な `5XX` エラーのトラブルシューティングのヒントを以下に示します。

- **メッセージアクティビティログ**で利用可能な具体的な詳細についてエラーメッセージを確認してください。webhookの場合は、Brazeホームページの**パフォーマンスの推移**セクションに移動し、webhookの統計を選択してください。ここから、エラーが発生したタイムスタンプを確認できます。
- エンドポイントに過負荷をかけるほど多くのリクエストを送信していないことを確認してください。バッチ送信やレート制限の調整を行い、エラーが減少するかどうかを確認できます。

## 異常ホスト検出 {#unhealthy-host-detection}

BrazeのWebhookとコネクテッドコンテンツは、ターゲットホストが高い割合で著しい遅延や過負荷を経験し、タイムアウト、リクエスト過多、またはBrazeがターゲットエンドポイントと正常に通信できないその他の結果が生じている場合に検出する異常ホスト検出メカニズムを採用しています。これは、ターゲットホストの問題の原因となっている可能性のある不要な負荷を軽減するためのセーフガードとして機能します。また、Brazeインフラの安定化と高速なメッセージング速度の維持にも役立ちます。

検出しきい値はWebhookとコネクテッドコンテンツで異なります。
- **Webhookの場合**: 1分間の移動時間枠内で失敗が3,000件を超えた場合（ホスト名とアプリグループのユニークな組み合わせごと&#8212;エンドポイントパスごとではありません）、Brazeはターゲットホストへのリクエストを1分間一時的に停止します。
- **コネクテッドコンテンツの場合**: 1分間の移動時間枠内で失敗が3,000件を超え、かつエラー率が90%を超えた場合（ホスト名とアプリグループのユニークな組み合わせごと&#8212;エンドポイントパスごとではありません）、Brazeはターゲットホストへのリクエストを1分間一時的に停止します。

リクエストが停止されると、Brazeは `598` エラーコードで応答をシミュレートし、異常な状態を示します。1分後、ホストが正常であることが確認された場合、Brazeはフルスピードでリクエストを再開します。ホストがまだ異常な場合、Brazeは再試行する前にさらに1分間待機します。

以下のエラーコードが異常ホスト検出の失敗カウントに寄与します: `408`、`429`、`502`、`503`、`504`、`529`。

Webhookの場合、Brazeは異常ホスト検出によって停止されたHTTPリクエストを自動的にリトライします。この自動リトライはエクスポネンシャルバックオフを使用し、失敗するまで数回のみリトライします。Webhookエラーの詳細については、[エラー、リトライロジック、タイムアウト]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook#errors-retry-logic-and-timeouts)を参照してください。

コネクテッドコンテンツの場合、ターゲットホストへのリクエストが異常ホスト検出によって停止されると、Brazeはエラー応答コードを受信したかのようにメッセージのレンダリングを続行し、Liquidロジックに従います。これらのコネクテッドコンテンツリクエストが異常ホスト検出によって停止された際にリトライされるようにするには、`:retry` オプションを使用してください。`:retry` オプションの詳細については、[コネクテッドコンテンツのリトライ]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/connected_content_retries)を参照してください。

異常ホスト検出が問題を引き起こしていると思われる場合は、[Brazeサポート]({{site.baseurl}}/support_contact)にお問い合わせください。

### コネクテッドコンテンツがレスポンスボディを返さない場合 {#connected-content-returns-no-response-body}

**症状:** コネクテッドコンテンツの呼び出しがメッセージプレビューまたは送信で空白として表示されます。

コネクテッドコンテンツの呼び出しがメッセージプレビューまたは送信で空白として表示される場合は、以下を確認してください。

- **URL内のノーブレークスペース:** Brazeはリクエストを行う前に、コネクテッドコンテンツURLからノーブレークスペース（`&nbsp;` またはUnicode `U+00A0`）を除去します。URLがドキュメントやダッシュボードのフィールドからコピーされ、文字間にノーブレークスペースが挿入されていた場合、リクエストが失敗するか、使用可能なボディが返されない可能性があります。URLをプレーンテキストで再入力するか、隠れたスペースを削除してから、再度プレビューしてください。
- **HTTPエラーと空のボディ:** ステータスコード300以上やホストがブロックされている場合、コネクテッドコンテンツは空の文字列をレンダリングすることがあります。[API呼び出しの実行]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call)を参照し、**メッセージアクティビティログ**で失敗を確認してください。

## 自動メールとメッセージアクティビティログのエントリ {#automated-emails-and-message-activity-log-entries}

### 自動メールの設定 {#setting-up-automated-emails}

ワークスペースで24時間以内にWebhookまたはコネクテッドコンテンツのエンドポイントエラー（リトライを含む）が100,000件を超えた場合、Brazeはエラーの解決方法に関する以下の情報を含むメールを送信します。

- ワークスペース名
- キャンバスまたはキャンペーンへのリンク
- エンドポイントURL
- エラーコード
- エラーが最後に観測された時刻
- メッセージアクティビティログおよび関連ドキュメントへのリンク

{% alert note %}
エラーしきい値はワークスペースごとに設定できます。このしきい値を調整するには、[Brazeサポート]({{site.baseurl}}/support_contact)にお問い合わせください。
{% endalert %}

エンドポイントエラーは以下のとおりです。

- **`4XX`:** `400`、`401`、`403`、`404`、`405`、`408`、`409`、`429`
- **`5XX`:** `500`、`502`、`503`、`504`、`598`、`599`

これらのメールはワークスペースレベルで1日1回のみ送信されます。これらのメールに登録しているユーザーがいない場合、Brazeはすべての会社管理者に通知します。

これらのメールを受信するには、以下の手順を実行してください。

1. **設定** > **管理者設定** > **通知設定**に移動します。
2. **キャンバスとキャンペーン**セクションで**Connected Content Errors**と**Webhook Errors**を選択します。

### メッセージアクティビティログのエントリ {#message-activity-log-entries}

失敗が発生した場合、[メッセージアクティビティログ]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log)に関連するエントリが少なくとも1つあります。リクエストがリトライされて最終的に成功した場合、その詳細はCurrentsとSnowflakeデータ共有で確認できます。リトライ後にリクエストが最終的に成功した場合でも、エラーは自動メールをトリガーする可能性があることに注意してください。

### Braze Currentsでの追加の失敗インサイト {#additional-failure-insights-in-braze-currents}

Webhook関連の問題に対する透明性を高めるため、BrazeはWebhookの失敗イベントの詳細をCurrentsとSnowflakeデータ共有にストリーミングします。これらのイベントには、失敗したWebhookリクエスト（HTTP `4xx` または `5xx` 応答など）が含まれ、Webhookの問題がメッセージ配信にどのように影響するかについてより高い可観測性を提供します。失敗イベントには、最終的なエラーとリトライ中のエラーの両方が含まれることに注意してください。

{% alert note %}
コネクテッドコンテンツリクエストは、これらのWebhook失敗イベントには含まれません。
{% endalert %}

詳細については、[メッセージエンゲージメントイベント用語集]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events)を参照してください。