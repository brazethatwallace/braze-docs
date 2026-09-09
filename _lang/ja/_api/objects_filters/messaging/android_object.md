---
nav_title: "Androidオブジェクト"
article_title: Androidメッセージングオブジェクト
page_order: 0
page_type: reference
channel: push
platform: Android
description: "このリファレンス記事では、Brazeで使用されるさまざまなAndroidオブジェクトを一覧にして説明します。"
---
# Androidオブジェクト {#android-object}

> `android_push`オブジェクトを使用すると、[メッセージングエンドポイント]({{site.baseurl}}/api/endpoints/messaging)を介してAndroidプッシュ通知およびAndroidプッシュアラートコンテンツに関連する情報を定義またはリクエストできます。

## Androidプッシュオブジェクト {#android-push-object}

ターゲットユーザーのAndroidデバイスにプッシュを送信したい場合は、`messages`にAndroidプッシュオブジェクトを含める必要があります。`alert`文字列と`extra`オブジェクトの合計バイト数は4,000を超えないようにしてください。メッセージングAPIは、Googleが許可するメッセージサイズを超えた場合にエラーを返します。

```json
{
   "alert": (required, string) the notification message,
   "title": (required, string) the title that appears in the notification drawer,
   "extra": (optional, object) additional keys and values to be sent in the push,
   "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under (must be an Android Push Message),
   "notification_channel_id": (optional, string) the channel ID the notification is sent with,
   "priority": (optional, integer) the notification priority value,
   "android_priority": (optional, string) the FCM sender priority,
   "send_to_sync": (optional, if set to true we throw an error if "alert" or "title" is set),
   "collapse_key": (optional, string) the collapse key for this message,
   // Specifying "default" in the sound field plays the standard notification sound
   "sound": (optional, string) the location of a custom notification sound within the app,
   "custom_uri": (optional, string) a web URL, or Deep Link URI,
   "use_webview": (optional, boolean) whether to open the web URL inside the app if the action is "URI", defaults to false,
   "summary_text": (optional, string),
   "time_to_live": (optional, integer (maximum of 2,419,200 seconds)),
   "notification_id": (optional, integer),
   "push_icon_image_url": (optional, string) an image URL for the large icon,
   "accent_color": (optional, integer) accent color to be applied by the standard Style templates when presenting this notification, an RGB integer value,
   "send_to_most_recent_device_only": (optional, boolean) defaults to false, if set to true, Braze only sends this push to a user's most recently used Android device, rather than all eligible Android devices,
   "buttons" : (optional, array of Android push action button objects) push action buttons to display
   "conversation_data" : (optional, Android Conversation Push Object) the data to be displayed through Conversation Push
}
```

`extra`オブジェクト内でキー`appboy_image_url`を指定することで、「ビッグピクチャー」通知を送信できます。`appboy_image_url`の値は、画像がホストされている場所へのURLである必要があります。画像は2:1のアスペクト比にトリミングし、少なくとも600 x 300 pxにする必要があります。

### パラメーターの詳細 {#additional-parameter-details}

| パラメーター | 詳細 |
| --------- | ------- |
| `priority` | このパラメーターは`-2`から`2`までの値を受け付けます。`-2`は「MIN」優先度、`2`は「MAX」を表します。`0`は「DEFAULT」値です。<br> <br> この範囲外で送信された値はデフォルトで0になります。どの優先度レベルを使用するかの詳細については、[Android通知の優先度]({{site.baseurl}}/developer_guide/push_notifications/customization?sdktab=android#android_settings)を参照してください。 |
| `android_priority` | このパラメーターはFCM送信者の優先度を指定するために`normal`または`high`の値を受け付けます。デフォルトでは、メッセージは[プッシュ設定]({{site.baseurl}}/user_guide/administer/global/workspace_settings/push_settings#default-fcm-priority-for-android-campaigns)ページで構成されたデフォルトのFCM優先度で送信されます。<br><br> 異なる値が配信にどのように影響するかの詳細については、[Androidメッセージの優先度](https://firebase.google.com/docs/cloud-messaging/android/message-priority)を参照してください。 |
| `collapse_key` | FCMはデバイスごとに同時に最大4つの折りたたみキーのみを保存できます。4つ以上の折りたたみキーを使用すると、FCMはどのキーが保持されるか保証しません。Brazeはキャンペーンにデフォルトでこれらのうち1つを使用するため、Androidメッセージには追加の折りたたみキーを最大3つまで指定するようにしてください。 |
| `push_icon_image_url` | 大きいアイコンパラメーターの値は、画像がホストされている場所へのURLである必要があります。<br> <br> 画像は1:1のアスペクト比にトリミングし、少なくとも40x40にする必要があります。 |
| `notification_channel` | これが指定されていない場合、Brazeは[ダッシュボードフォールバック]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/android/notification_channels#dashboard-fallback-channel)チャネルIDで通知ペイロードの送信を試みます。詳細については、[通知チャネル]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/android/notification_channels)を参照し、統合時の[通知チャネルの定義]({{site.baseurl}}/developer_guide/push_notifications?sdktab=android)ステップを確認してください。 |
| `send_to_sync` | `send_to_sync`メッセージの詳細については、[サイレントAndroid通知]({{site.baseurl}}/developer_guide/push_notifications/silent?sdktab=android)を参照してください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="パラメーターの詳細" }

## Androidプッシュアクションボタンオブジェクト {#android-push-action-button-object}

```json
{
  "text": (required, string) the button's text,
  "action": (optional, string) one of "OPEN_APP", "URI", "DEEP_LINK", or "CLOSE", defaults to "OPEN_APP",
  "uri": (optional, string) a web URL or Deep Link URI,
  "use_webview": (optional, boolean) whether to open the web URL inside the app if the action is "URI", defaults to true
}
```

## Android会話プッシュオブジェクト {#android-conversation-push-object}

{% sdk_min_versions android:15.0.0 %}

このメッセージのコンセプトは、[Android People and Conversations](https://developer.android.com/guide/topics/ui/conversations)のプッシュドキュメントに記載されているコンセプトに対応しています。

```json
{
  "shortcut_id" : (required, string) the sharing shortcut identifier,
  "reply_person_id" : (required, string) the identifier of the Person this push is replying to,
  "messages" : (required, array of Android Conversation Push Message Object),
  "persons" : (required, array of Android Conversation Push Person Object)
}
```

### Android会話プッシュメッセージオブジェクト {#android-conversation-push-message-object}

```json
{
  "text" : (required, string) the text of this message,
  "timestamp" : (required, integer) the unix timestamp of when this message was sent,
  "person_id" : (required, string) the Person identifier of this message's sender,
}
```

### Android会話プッシュPersonオブジェクト {#android-conversation-push-person-object}

```json
{
  "id" : (required, string) the identifier of this Person,
  "name" : (required, string) the display name of this Person
}
```

