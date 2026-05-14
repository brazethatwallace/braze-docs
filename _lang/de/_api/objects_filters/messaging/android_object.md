---
nav_title: "Android-Objekte"
article_title: Android-Messaging-Objekt
page_order: 0
page_type: reference
channel: push
platform: Android
description: "Dieser Referenzartikel listet die verschiedenen Android-Objekte auf, die bei Braze verwendet werden, und erklärt sie."

---
# Android-Objekt {#android-object}

> Mit dem Objekt `android_push` können Sie über unsere [Messaging-Endpunkte]({{site.baseurl}}/api/endpoints/messaging/) Informationen zu Android-Push- und Android-Push-Alert-Inhalten definieren oder anfragen.

## Android-Push-Objekt {#android-push-object}

Sie müssen ein Android-Push-Objekt in `messages` einbinden, wenn Sie möchten, dass die von Ihnen angesprochenen Nutzer:innen einen Push auf ihren Android-Geräten erhalten. Die Gesamtzahl der Bytes in Ihrem `alert`-String und `extra`-Objekt sollte 4.000 nicht überschreiten. Die Messaging-API gibt einen Fehler zurück, wenn Sie die von Google zulässige Nachrichtengröße überschreiten.

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

Sie können „Big Picture“-Benachrichtigungen senden, indem Sie den Schlüssel `appboy_image_url` im Objekt `extra` angeben. Der Wert für `appboy_image_url` sollte eine URL sein, die auf den Speicherort Ihres gehosteten Bildes verweist. Bilder müssen auf ein Seitenverhältnis von 2:1 zugeschnitten werden und sollten mindestens 600 x 300 px groß sein.

### Zusätzliche Parameterdetails {#additional-parameter-details}

| Parameter | Details |
| --------- | ------- |
| `priority` | Dieser Parameter akzeptiert Werte von `-2` bis `2`, wobei `-2` für die Priorität „MIN“ und `2` für „MAX“ steht. `0` ist der „DEFAULT“-Wert. <br> <br> Alle Werte, die außerhalb dieses Bereichs gesendet werden, werden standardmäßig auf 0 gesetzt. Weitere Informationen darüber, welche Prioritätsstufe Sie verwenden sollten, finden Sie unter [Android-Benachrichtigungspriorität]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/customization/advanced_settings/#notification-priority). |
| `android_priority` | Dieser Parameter akzeptiert die Werte `normal` oder `high`, um die FCM-Senderpriorität anzugeben. Standardmäßig werden Nachrichten mit der auf der Seite [Push-Einstellungen]({{site.baseurl}}/user_guide/administrative/app_settings/push_settings/#default-fcm-priority-for-android-campaigns) konfigurierten Standard-FCM-Priorität gesendet.<br><br> Weitere Informationen darüber, wie sich unterschiedliche Werte auf die Zustellung auswirken, finden Sie unter [Android-Nachrichtenpriorität](https://firebase.google.com/docs/cloud-messaging/android/message-priority). |
| `collapse_key` | FCM kann pro Gerät nur bis zu vier Collapse Keys gleichzeitig speichern. Wenn Sie mehr als vier Collapse Keys verwenden, übernimmt FCM keine Garantie dafür, welche Schlüssel erhalten bleiben. Braze verwendet standardmäßig einen dieser Schlüssel für Campaigns. Stellen Sie daher sicher, dass Sie nur bis zu drei zusätzliche Collapse Keys für Android-Nachrichten angeben. |
| `push_icon_image_url` | Der Wert für den Parameter „Großes Symbol“ sollte eine URL sein, die auf den Speicherort Ihres gehosteten Bildes verweist. <br> <br> Bilder müssen auf ein Seitenverhältnis von 1:1 zugeschnitten werden und sollten mindestens 40x40 groß sein. |
| `notification_channel` | Wenn dies nicht angegeben wird, versucht Braze, die Benachrichtigungs-Payload mit der [Dashboard-Fallback]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/notification_channels/#dashboard-fallback-channel)-Kanal-ID zu senden. Weitere Informationen finden Sie unter [Benachrichtigungskanäle]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/android/notification_channels/) und in den Schritten zur [Definition von Benachrichtigungskanälen]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/#step-5-define-notification-channels) während der Integration. |
| `send_to_sync` | Weitere Informationen zu `send_to_sync`-Nachrichten finden Sie unter [Stille Android-Benachrichtigungen]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/silent_push_notifications/#silent-push-notifications). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Zusätzliche Parameterdetails" }

## Android-Push-Action-Button-Objekt {#android-push-action-button-object}

```json
{
  "text": (required, string) the button's text,
  "action": (optional, string) one of "OPEN_APP", "URI", "DEEP_LINK", or "CLOSE", defaults to "OPEN_APP",
  "uri": (optional, string) a web URL or Deep Link URI,
  "use_webview": (optional, boolean) whether to open the web URL inside the app if the action is "URI", defaults to true
}
```

## Android-Konversations-Push-Objekt {#android-conversation-push-object}

{% sdk_min_versions android:15.0.0 %}

Die Konzepte in dieser Nachricht entsprechen denen in der Push-Dokumentation zu [Android People and Conversations](https://developer.android.com/guide/topics/ui/conversations).

```json
{
  "shortcut_id" : (required, string) the sharing shortcut identifier,
  "reply_person_id" : (required, string) the identifier of the Person this push is replying to,
  "messages" : (required, array of Android Conversation Push Message Object),
  "persons" : (required, array of Android Conversation Push Person Object)
}
```

### Android-Konversations-Push-Nachrichtenobjekt {#android-conversation-push-message-object}

```json
{
  "text" : (required, string) the text of this message,
  "timestamp" : (required, integer) the unix timestamp of when this message was sent,
  "person_id" : (required, string) the Person identifier of this message's sender,
}
```

### Android-Konversations-Push-Personenobjekt {#android-conversation-push-person-object}

```json
{
  "id" : (required, string) the identifier of this Person,
  "name" : (required, string) the display name of this Person
}
```

