すべてのトランザクションメールは、指定した URL に HTTP リクエストとして返送されるイベントステータスポストバックによって補完されます。これにより、リアルタイムでメッセージのステータスを評価し、メッセージが未配信の場合は別のチャネルでユーザーにリーチするアクションを取ったり、Brazeにレイテンシーが発生している場合は内部システムにフォールバックしたりすることができます。

ユニークな識別子を使って、これらの更新を個々のメッセージに関連付けることができます。

- `dispatch_id`: Brazeが各メッセージに対して自動的に生成するユニークな ID です。
- `external_send_id`: 注文番号など、内部システムと更新を照合するために提供するカスタム識別子です。

たとえば、注文確認メールを送信する際にリクエストに `external_send_id: 1234` を含めると、そのメールに対するその後のすべてのイベントポストバック（`Sent` や `Delivered` など）に `external_send_id: 1234` が含まれます。これにより、注文番号 #1234 の顧客が注文確認メールを受け取ったかどうかを確認できます。

### ポストバックの設定 {#setting-up-postbacks}

Brazeダッシュボードで以下を行います。

1. **設定** > **メール設定**に移動します。
2. **トランザクションイベントステータスポストバック**の下に、Brazeがトランザクションメールのステータス更新を送信する URL を入力します。
3. ポストバックをテストします。

![]({% image_buster /assets/img/transactional_webhook_url.png %})

### ポストバック本文 {#postback-body}

```json
{
  "dispatch_id": (string, a randomly-generated unique ID of the instance of this send),
  "status": (string, Current status of message from the following message status table,
  "metadata" : (object, additional information relating to the execution of an event)
   {
     "external_send_id" : (string, If provided at the time of the request, Braze will pass your internal identifier for this send for all postbacks),
     "campaign_api_id" : (string, API identifier of this transactional campaign),
     "received_at": (ISO 8601 DateTime string, Timestamp of when the request was received by Braze, only included for events with "sent" status),
     "enqueued_at": (ISO 8601 DateTime string, Timestamp of when the request was enqueued by Braze, only included for events with "sent" status),
     "executed_at": (ISO 8601 DateTime string, Timestamp of when the request was processed by Braze, only included for events with "sent" status),
     "sent_at": (ISO 8601 DateTime string, Timestamp of when the request was sent to the ESP by Braze, only included for events with "sent" status),
     "processed_at" : (ISO 8601 DateTime string, Timestamp the event was processed by the ESP, only included for events with "processed" status),
     "delivered_at" : (ISO 8601 DateTime string, Timestamp the event was delivered to the user's inbox provider, only included for events with "processed" status),
     "bounced_at" : (ISO 8601 DateTime string, Timestamp the event was bounced by the user's inbox provider, only included for events with "bounced" status),
     "aborted_at" : (ISO 8601 DateTime string, Timestamp the event was Aborted by Braze, only included for events with "aborted" status),
     "reason" : (string, The reason Braze or the Inbox provider was unable to process this message to the user, only included for events with "aborted" or "bounced" status),
   }
}
```

#### メッセージステータス {#message-status}

| ステータス | 説明 |
| ------------ | ----------- |
| `sent` | メッセージがBrazeのメール送信パートナーに正常にディスパッチされました |
| `processed` | メール送信パートナーがメッセージを正常に受信し、ユーザーの受信トレイプロバイダーへの送信準備が完了しました |
| `aborted` | ユーザーがメール送信可能なアドレスを持っていないか、メッセージ本文でLiquidの abort ロジックが呼び出されたため、Brazeがメッセージを正常にディスパッチできませんでした。すべての中止イベントのメタデータオブジェクト内には、メッセージが中止された理由を示す `reason` フィールドが含まれています |
| `delivered` | メッセージがユーザーのメール受信トレイプロバイダーに受け入れられました |
| `bounced` | メッセージがユーザーのメール受信トレイプロバイダーによって拒否されました。すべてのバウンスイベントのメタデータオブジェクト内には、受信トレイプロバイダーから提供されたバウンスエラーコードを反映する `reason` フィールドが含まれています |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Message status" }

### ポストバックの例 {#example-postback}
```json

// Sent Event
{
    "dispatch_id": "acf471119f7449d579e8089032003ded",
    "status": "sent",
    "metadata": {
      "received_at": "2020-08-31T18:58:41.000+00:00",
      "enqueued_at": "2020-08-31T18:58:41.000+00:00",
      "executed_at": "2020-08-31T18:58:41.000+00:00",
      "sent_at": "2020-08-31T18:58:42.000+00:00",
      "campaign_api_id": "417220e4-5a2a-b634-7f7d-9ec891532368",
      "external_send_id" : "34a2ceb3cf6184132f3d816e9984269a"
    }
}

// Processed Event
{
    "dispatch_id": "acf471119f7449d579e8089032003ded",
    "status": "processed",
    "metadata": {
      "processed_at": "2020-08-31T18:58:42.000+00:00",
      "campaign_api_id": "417220e4-5a2a-b634-7f7d-9ec891532368",
      "external_send_id" : "34a2ceb3cf6184132f3d816e9984269a"
    }
}

// Aborted
{
    "dispatch_id": "acf471119f7449d579e8089032003ded",
    "status": "aborted",
    "metadata": {
      "reason": "User not emailable",
      "aborted_at": "2020-08-31T19:04:51.000+00:00",
      "campaign_api_id": "417220e4-5a2a-b634-7f7d-9ec891532368",
      "external_send_id" : "34a2ceb3cf6184132f3d816e9984269a"
    }
}

// Delivered Event
{
    "dispatch_id": "acf471119f7449d579e8089032003ded",
    "status": "delivered",
    "metadata": {
      "delivered_at": "2020-08-31T18:27:32.000+00:00",
      "campaign_api_id": "417220e4-5a2a-b634-7f7d-9ec891532368",
      "external_send_id" : "34a2ceb3cf6184132f3d816e9984269a"
    }
}

// Bounced Event
{
    "dispatch_id": "acf471119f7449d579e8089032003ded",
    "status": "bounced",
    "metadata": {
      "bounced_at": "2020-08-31T18:58:43.000+00:00",
      "reason": "550 5.1.1 The email account that you tried to reach does not exist",
      "campaign_api_id": "417220e4-5a2a-b634-7f7d-9ec891532368",
      "external_send_id" : "34a2ceb3cf6184132f3d816e9984269a"
    }
}

```

