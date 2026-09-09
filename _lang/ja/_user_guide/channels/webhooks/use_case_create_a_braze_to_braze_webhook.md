---
nav_title: "ユースケース: Braze間Webhookの作成"
article_title: "ユースケース: Braze間Webhookの作成"
page_order: 2
channel:
  - webhooks
description: "このリファレンス記事では、ユーザーの更新とBraze間Webhookの使い分け、およびBraze間Webhookの作成方法について説明します。"
---

# Braze間Webhookの作成 {#create-a-braze-to-braze-webhook}

> Braze間Webhookを使用すると、[キャンペーン]({{site.baseurl}}/user_guide/messaging/canvas)または[キャンバス]({{site.baseurl}}/user_guide/messaging/campaigns)内の[Webhook]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook)を使って、Braze内から[Braze REST API]({{site.baseurl}}/api/basics)を呼び出すことができます。[APIトリガーキャンバス]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases)のトリガーなど、オーケストレーションタスクに使用します。キャンバスから[ユーザー属性]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes)、[カスタムイベント]({{site.baseurl}}/user_guide/data/activation/events/custom_events)、または[購入]({{site.baseurl}}/user_guide/data/activation/events/purchase_events)を更新する場合は、代わりに[ユーザーの更新]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update)を使用してください。ユーザープロファイルの変更用に設計されており、更新をより効率的に処理します。

この記事を最大限に活用するには、[Webhookの仕組み]({{site.baseurl}}/user_guide/channels/webhooks)と、Brazeで[Webhookを作成する]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook)方法に精通している必要があります。

## 別のキャンバスをトリガーするために「送信先に送る」を使用する {#use-send-to-destination-for-triggering-another-canvas}

キャンバス内から2番目のキャンバスをトリガーするには、Braze間Webhookの代わりに[送信先に送る]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/send_to_destination)を使用してください。このキャンバスコンポーネントは、キャンバスジャーニーを接続するために特別に設計されており、あるキャンバスから別のキャンバスにユーザーを送るためのよりシンプルで効率的な方法を提供します。

「送信先に送る」は、Webhookの設定やAPIキーを必要とせずに、ユーザーがそのステップに到達した時点で、送信先キャンバスのエントリ条件とオーディエンス条件に対してユーザーを評価します。条件を満たしたユーザーは送信先キャンバスに入り、後続のステップがある場合はソースキャンバスでもジャーニーを続けることができます。

{% alert tip %}
キャンバスに[送信先に送る]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/send_to_destination)を追加すると、webhookやAPI呼び出しを設定することなく、別のキャンバスジャーニーにユーザーを送ることができます。
{% endalert %}

## ユーザーデータの変更にはユーザー更新を使用する {#use-user-update-for-user-data-changes}

キャンバス内からユーザープロファイルを更新する場合（[カスタム属性]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes)の変更、[カスタムイベント]({{site.baseurl}}/user_guide/data/activation/events/custom_events)の記録、[購入]({{site.baseurl}}/user_guide/data/activation/events/purchase_events)の記録など）は、Braze間webhookではなく[ユーザー更新]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update)を使用してください。

ユーザー更新は複数の変更をまとめてバッチで送信するため、webhookよりも高速です。webhookよりもセットアップが簡単で、[高度なJSONコンポーザー]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update#advanced-json-editor)を使用した複雑な更新もサポートしています。たとえば、ユーザーがメッセージを閲覧した回数をカウントするには、Braze間webhookではなくユーザー更新の[増分・減分機能]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update#increasing-and-decreasing-values)を使用してください。

{% alert tip %}
キャンバスに[ユーザー更新]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update)を追加して、JSONコンポーザーを使用してユーザーの属性、イベント、購入を更新できます。
{% endalert %}

## Braze間Webhookを使用するタイミング {#when-to-use-a-braze-to-braze-webhook}

ユーザー更新は、ユーザープロファイルの更新に関して、Braze間Webhookとほぼ同じタスクを処理できます。単純なカスタム属性を超える複雑な更新については、[高度なJSONコンポーザー]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update#advanced-json-editor)を使用できます。

送信先へ送信を使用すると、Webhookの設定を行わずに、キャンバス内から2番目のキャンバスをトリガーするためのよりシンプルな方法が提供されます。

Braze間Webhookは、専用のキャンバスコンポーネントがないシナリオにおいて、Braze内からBrazeの [REST API]({{site.baseurl}}/api/basics) を呼び出す必要がある場合に使用できます。一般的な例としては、以下のようなものがあります。

- キャンバスから [APIトリガーキャンペーン]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns)をトリガーする
- Brazeの1つのワークフローが専用のキャンバスコンポーネントを持たないAPIを呼び出す必要があるオーケストレーションパターンのために、他の[メッセージングエンドポイント]({{site.baseurl}}/api/endpoints/messaging)を呼び出す

キャンバス内でのユーザー更新には、[ユーザー更新]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update)を使用してください。別のキャンバスをトリガーするには、[送信先へ送信]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/send_to_destination)を使用してください。

## 前提条件 {#prerequisites}

Braze-to-Braze webhookを作成するには、到達したいエンドポイントの権限を持つ[APIキー]({{site.baseurl}}/api/basics)が必要です。例えば、APIトリガーのキャンバスをトリガーするには、`canvas.trigger.send` 権限を持つAPIキーが必要です。

## Braze間Webhookの設定 {#setting-up-your-braze-to-braze-webhook}

Braze間Webhookを作成する一般的なワークフローは、以下のステップに従います。

1. キャンペーンまたはキャンバスコンポーネントとして[Webhookを作成]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook)します。
2. **空白テンプレート**を選択します。
3. **作成**タブで、APIユースケースに応じた**Webhook URL**と**リクエストボディ**を指定します。
4. **設定**タブで、エンドポイントの要件に応じて**HTTPメソッド**と**リクエストヘッダー**を指定します。
5. 追加の配信設定（例えば、カスタムイベントによるトリガーなど）を構成し、キャンペーンまたはキャンバスの残りの部分を構築します。

## 最初のキャンバスから2番目のキャンバスをトリガーする {#trigger-a-second-canvas-from-an-initial-canvas}

このユースケースでは、2つのキャンバスを作成し、Braze間webhookを使用して最初のキャンバスから2番目のキャンバスをトリガーします。これは、ユーザーが別のキャンバスの特定のポイントに到達したときのエントリトリガーとして機能します。

{% alert note %}
**キャンバスステップとのインタラクション**トリガーはキャンペーンでのみ使用でき、アクションベースのキャンバスエントリには使用できません。別のキャンバスでユーザーが特定のステップに到達したことに基づいてキャンバスをトリガーする必要がある場合は、このBraze間webhookアプローチまたは[送信先]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/send_to_destination)キャンバスコンポーネントを使用してください。
{% endalert %}

1. まず、最初のキャンバスによってトリガーされる2番目のキャンバスを作成します。
2. キャンバスの**エントリスケジュール**で、**APIトリガー**を選択します。
3. **キャンバスID**をメモしてください。後のステップで必要になります。
4. 2番目のキャンバスのステップの構築を続け、キャンバスを保存します。
5. 最後に、最初のキャンバスを作成します。2番目のキャンバスをトリガーしたいステップを見つけ、webhookで新しいステップを作成します。

webhookを設定する際は、以下を参照してください。

- **Webhook URL：**[RESTエンドポイントURL]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints)の後に`/canvas/trigger/send`を追加します。たとえば、`US-06`インスタンスの場合、URLは`https://rest.iad-06.braze.com/canvas/trigger/send`になります。
- **リクエストボディ：**Raw Text

### リクエストヘッダーとメソッド {#request-headers-and-method}

Brazeでは、APIキーを含む認証用のHTTPヘッダーと、コンテンツタイプを宣言するヘッダーが必要です。

- **リクエストヘッダー：**
  - **Authorization：**`Bearer YOUR_API_KEY`
  - **Content-Type：**`application/json`
- **HTTPメソッド：**`POST`

`YOUR_API_KEY`を`canvas.trigger.send`権限を持つBraze APIキーに置き換えてください。Brazeダッシュボードで**設定** > **APIキー**に移動してAPIキーを作成できます。

![BrazeダッシュボードでAuthorizationとContent-Typeフィールドを表示するwebhookのリクエストヘッダー。]({% image_buster /assets/img_archive/webhook_settings.png %}){: style="max-width:70%;"}

#### リクエストボディ {#request-body}

テキストフィールドに`/canvas/trigger/send`リクエストを追加します。詳細については、[APIトリガー配信によるキャンバスメッセージの送信]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases)を参照してください。以下は、このエンドポイントのリクエストボディの例です。`your_canvas_id`は2番目のキャンバスのキャンバスIDです。

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

ユーザーが最初のキャンバスでこのwebhookステップに到達すると、BrazeはAPIを通じてそのユーザーに対して2番目のキャンバスをトリガーします。

## 考慮事項 {#considerations}

- **ユーザー更新:** キャンバスからユーザープロファイルを更新する場合（属性、イベント、購入）、Braze間webhookよりも効率性とコスト効果に優れた[ユーザー更新]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update)を使用してください。
- Braze間webhookにはエンドポイントの[レート制限]({{site.baseurl}}/api/api_limits)が適用されます。
- ユーザープロファイルの更新には[データポイント]({{site.baseurl}}/user_guide/data/infrastructure/data_points)が発生し、全体の消費量にカウントされます。一方、メッセージングエンドポイントを介して別のメッセージをトリガーする場合はデータポイントは発生しません。
- [匿名ユーザー]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#anonymous-user-profiles)をターゲットにするには、webhookのリクエストボディで `external_id` の代わりに `braze_id` を使用してください。
- Braze間webhookを[webhookテンプレート]({{site.baseurl}}/user_guide/messaging/templates/webhook_templates)として保存し、再利用できます。
- [メッセージアクティビティログ]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log)でwebhookの失敗を確認し、トラブルシューティングできます。