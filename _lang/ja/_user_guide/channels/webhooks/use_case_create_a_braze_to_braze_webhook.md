---
nav_title: "ユースケース: Braze間Webhookの作成"
article_title: "ユースケース: Braze間Webhookの作成"
page_order: 2
channel:
  - webhooks
description: "このリファレンス記事では、ユーザーの更新とBraze間Webhookの使い分け、およびBraze間Webhookの作成方法について説明します。"

---

# Braze間Webhookの作成 {#create-a-braze-to-braze-webhook}

> Braze間Webhookを使用すると、[キャンペーン]({{site.baseurl}}/user_guide/messaging/canvas/)または[キャンバス]({{site.baseurl}}/user_guide/messaging/campaigns/)内の[Webhook]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook/)を使って、Braze内から[Braze REST API]({{site.baseurl}}/api/basics/)を呼び出すことができます。[APIトリガーキャンバス]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)のトリガーなど、オーケストレーションタスクに使用します。キャンバスから[ユーザー属性]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/)、[カスタムイベント]({{site.baseurl}}/user_guide/data/activation/events/custom_events/)、または[購入]({{site.baseurl}}/user_guide/data/activation/events/purchase_events/)を更新する場合は、代わりに[ユーザーの更新]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update/)を使用してください。ユーザープロファイルの変更用に設計されており、更新をより効率的に処理します。

この記事を最大限に活用するには、[Webhookの仕組み]({{site.baseurl}}/user_guide/channels/webhooks/)と、Brazeで[Webhookを作成する]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook/)方法に精通している必要があります。

## ユーザーデータの変更にはユーザーの更新を使用する {#use-user-update-for-user-data-changes}

キャンバス内からユーザープロファイルを更新する場合（[カスタム属性]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/)の変更、[カスタムイベント]({{site.baseurl}}/user_guide/data/activation/events/custom_events/)の記録、[購入]({{site.baseurl}}/user_guide/data/activation/events/purchase_events/)の記録など）は、Braze間Webhookではなく[ユーザーの更新]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update/)を使用してください。

ユーザーの更新は複数の変更をグループ化してバッチで送信するため、Webhookよりも高速です。Webhookよりもセットアップが簡単で、[高度なJSONコンポーザー]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update/#advanced-json-composer)を使用した複雑な更新もサポートしています。たとえば、ユーザーがメッセージを閲覧した回数をカウントするには、Braze間Webhookではなくユーザーの更新の[値の増減機能]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update/#increasing-and-decreasing-values)を使用してください。

{% alert tip %}
キャンバスに[ユーザーの更新]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update/)を追加して、JSONコンポーザーを使用してユーザーの属性、イベント、購入を更新できます。
{% endalert %}

## Braze間Webhookを使用するタイミング {#when-to-use-a-braze-to-braze-webhook}

ユーザーの更新は、ユーザープロファイルの更新に関して、Braze間Webhookとほぼ同じタスクを処理できます。単純なカスタム属性を超える複雑な更新には、[高度なJSONコンポーザー]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update/#advanced-json-composer)を使用できます。

キャンバスステップからの直接的なユーザー更新以外のシナリオで、Braze内からBrazeの[REST API]({{site.baseurl}}/api/basics/)を呼び出す必要がある場合に、Braze間Webhookを使用できます。一般的な例は以下のとおりです。

- 別のキャンバスから[APIトリガーキャンバス]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)をトリガーする
- Braze内のあるワークフローが、専用のキャンバスコンポーネントを持たないAPIを呼び出す必要があるオーケストレーションパターンで、他の[メッセージングエンドポイント]({{site.baseurl}}/api/endpoints/messaging/)を呼び出す

キャンバス内でのユーザー更新には、[ユーザーの更新]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update/)を使用することを推奨します。

## 前提条件 {#prerequisites}

Braze間Webhookを作成するには、到達したいエンドポイントの権限を持つ[APIキー]({{site.baseurl}}/api/api_key/)が必要です。たとえば、APIトリガーキャンバスをトリガーするには、`canvas.trigger.send`権限を持つAPIキーが必要です。

## Braze間Webhookのセットアップ {#setting-up-your-braze-to-braze-webhook}

Braze間Webhookを作成する一般的なワークフローは以下のステップに従います。

1. キャンペーンまたはキャンバスコンポーネントとして[Webhookを作成]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook/)します。
2. **Blank Template**を選択します。
3. **Compose**タブで、APIユースケースに合わせて**Webhook URL**と**Request Body**を指定します。
4. **Settings**タブで、エンドポイントの要件に応じて**HTTP Method**と**Request Headers**を指定します。
5. 追加の配信設定（たとえば、カスタムイベントからのトリガー）を構成し、キャンペーンまたはキャンバスの残りの部分を構築します。

## 最初のキャンバスから2番目のキャンバスをトリガーする {#trigger-a-second-canvas-from-an-initial-canvas}

このユースケースでは、2つのキャンバスを作成し、Braze間Webhookを使用して最初のキャンバスから2番目のキャンバスをトリガーします。これは、ユーザーが別のキャンバス内の特定のポイントに到達したときのエントリトリガーとして機能します。

1. まず、2番目のキャンバス（最初のキャンバスによってトリガーされるキャンバス）を作成します。
2. キャンバスの**Entry Schedule**で、**API-Triggered**を選択します。
3. **キャンバス ID**をメモしてください。後のステップで必要になります。
4. 2番目のキャンバスのステップの構築を続け、キャンバスを保存します。
5. 最後に、最初のキャンバスを作成します。2番目のキャンバスをトリガーしたいステップを見つけ、Webhookを含む新しいステップを作成します。

Webhookを設定する際は、以下を参照してください。

- **Webhook URL:** [RESTエンドポイントURL]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints/)の後に`/canvas/trigger/send`を付けます。たとえば、`US-06`インスタンスの場合、URLは`https://rest.iad-06.braze.com/canvas/trigger/send`になります。
- **Request Body:** Raw Text

#### リクエストヘッダーとメソッド {#request-headers-and-method}

Brazeでは、APIキーを含む許可用のHTTPヘッダーと、コンテンツタイプを宣言するヘッダーが必要です。

- **Request Headers:**
  - **Authorization:** `Bearer YOUR_API_KEY`
  - **Content-Type:** `application/json`
- **HTTP Method:** `POST`

`YOUR_API_KEY`を`canvas.trigger.send`権限を持つBraze APIキーに置き換えてください。APIキーは、Brazeダッシュボードで**Settings** > **API Keys**に移動して作成できます。

![BrazeダッシュボードでAuthorizationとContent-Typeフィールドを表示するWebhookのリクエストヘッダー。]({% image_buster /assets/img_archive/webhook_settings.png %}){: style="max-width:70%;"}

#### リクエストボディ {#request-body}

テキストフィールドに`/canvas/trigger/send`リクエストを追加します。詳細については、[APIトリガー配信によるCanvasメッセージの送信]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)を参照してください。以下は、このエンドポイントのリクエストボディの例です。`your_canvas_id`は2番目のCanvasのCanvas IDです。

{% raw %}
```json
{
  "canvas_id": "your_canvas_id",
  "recipients": [
    {
      "external_user_id": "{{${user_id}}}"
    }
  ]
}
```
{% endraw %}

ユーザーが最初のキャンバスでこのWebhookステップに到達すると、BrazeはAPIを介してそのユーザーの2番目のキャンバスをトリガーします。

## 考慮事項 {#considerations}

- **ユーザー更新:** キャンバスからユーザープロファイルを更新する場合（属性、イベント、購入）は、効率性とコスト効果を高めるために、Braze間Webhookではなく[ユーザーの更新]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update/)を使用してください。
- Braze間Webhookはエンドポイントの[レート制限]({{site.baseurl}}/api/api_limits/)の対象となります。
- ユーザープロファイルの更新は全体の消費量にカウントされる[データポイント]({{site.baseurl}}/user_guide/data/infrastructure/data_points/)が発生しますが、メッセージングエンドポイントを通じて別のメッセージをトリガーする場合は発生しません。
- [匿名ユーザー]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/#anonymous-user-profiles)をターゲットにするには、Webhookのリクエストボディで`external_id`の代わりに`braze_id`を使用してください。
- Braze間Webhookを[Webhookテンプレート]({{site.baseurl}}/user_guide/messaging/templates/webhook_templates/)として保存して再利用できます。
- [メッセージアクティビティログ]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log/)を確認して、Webhookの失敗を表示およびトラブルシューティングできます。