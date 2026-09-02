---
nav_title: "Objetos Android"
article_title: Objeto de envio de mensagens do Android
page_order: 0
page_type: reference
channel: push
platform: Android
description: "Este artigo de referência lista e explica os diferentes objetos Android usados na Braze."
---
# Objeto Android {#android-object}

> O objeto `android_push` permite que você defina ou solicite informações relacionadas ao conteúdo do Android Push e do Android Push Alert por meio de nossos [endpoints de envio de mensagens]({{site.baseurl}}/api/endpoints/messaging).

## Objeto de push para Android {#android-push-object}

Você deve incluir um objeto de push para Android em `messages` se quiser que os usuários segmentados recebam uma notificação push em seus dispositivos Android. O número total de bytes na string `alert` e no objeto `extra` não deve exceder 4.000. A API de envio de mensagens retorna um erro se você exceder o tamanho de mensagem permitido pelo Google.

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

Você pode enviar notificações "Big Picture" especificando a chave `appboy_image_url` no objeto `extra`. O valor de `appboy_image_url` deve ser uma URL que aponte para o local onde sua imagem está hospedada. As imagens precisam ser cortadas em uma proporção de 2:1 e devem ter pelo menos 600 x 300 px.

### Detalhes adicionais dos parâmetros {#additional-parameter-details}

| Parâmetro | Detalhes |
| --------- | ------- |
| `priority` | Esse parâmetro aceita valores de `-2` a `2`, onde `-2` representa a prioridade "MIN" e `2` representa "MAX". `0` é o valor "DEFAULT". <br> <br> Qualquer valor enviado fora dessa faixa será definido como 0 por padrão. Para saber mais sobre qual nível de prioridade usar, consulte [Prioridade de notificação do Android]({{site.baseurl}}/developer_guide/push_notifications/customization?sdktab=android#android_settings). |
| `android_priority` | Esse parâmetro aceita os valores `normal` ou `high` para especificar a prioridade do remetente FCM. Por padrão, as mensagens são enviadas com a prioridade FCM padrão configurada na página de [Configurações de push]({{site.baseurl}}/user_guide/administer/global/workspace_settings/push_settings#default-fcm-priority-for-android-campaigns).<br><br> Para saber mais sobre como diferentes valores afetam a entrega, consulte [Prioridade de mensagem do Android](https://firebase.google.com/docs/cloud-messaging/android/message-priority). |
| `collapse_key` | O FCM pode armazenar simultaneamente apenas quatro chaves de recolhimento por dispositivo. Se você usar mais de quatro chaves de recolhimento, o FCM não garante quais chaves serão mantidas. A Braze usa uma delas por padrão para Campaigns, portanto, especifique no máximo três chaves de recolhimento adicionais para mensagens Android. |
| `push_icon_image_url` | O valor do parâmetro de ícone grande deve ser uma URL que aponte para o local onde sua imagem está hospedada. <br> <br> As imagens precisam ser cortadas em uma proporção de 1:1 e devem ter pelo menos 40x40. |
| `notification_channel` | Se não for especificado, a Braze tentará enviar a carga útil da notificação com o ID do canal de [fallback do dashboard]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/android/notification_channels#dashboard-fallback-channel). Para saber mais, consulte [Canais de notificação]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/android/notification_channels) e veja as etapas para [definir canais de notificação]({{site.baseurl}}/developer_guide/push_notifications?sdktab=android) durante a integração. |
| `send_to_sync` | Para saber mais sobre mensagens `send_to_sync`, consulte [Notificações silenciosas do Android]({{site.baseurl}}/developer_guide/push_notifications/silent?sdktab=android). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Detalhes adicionais dos parâmetros" }

## Objeto de botão de ação por push para Android {#android-push-action-button-object}

```json
{
  "text": (required, string) the button's text,
  "action": (optional, string) one of "OPEN_APP", "URI", "DEEP_LINK", or "CLOSE", defaults to "OPEN_APP",
  "uri": (optional, string) a web URL or Deep Link URI,
  "use_webview": (optional, boolean) whether to open the web URL inside the app if the action is "URI", defaults to true
}
```

## Objeto push de conversa do Android {#android-conversation-push-object}

{% sdk_min_versions android:15.0.0 %}

Os conceitos desta mensagem correspondem aos da documentação de push [Android People and Conversations](https://developer.android.com/guide/topics/ui/conversations).

```json
{
  "shortcut_id" : (required, string) the sharing shortcut identifier,
  "reply_person_id" : (required, string) the identifier of the Person this push is replying to,
  "messages" : (required, array of Android Conversation Push Message Object),
  "persons" : (required, array of Android Conversation Push Person Object)
}
```

### Objeto de mensagem push de conversa do Android {#android-conversation-push-message-object}

```json
{
  "text" : (required, string) the text of this message,
  "timestamp" : (required, integer) the unix timestamp of when this message was sent,
  "person_id" : (required, string) the Person identifier of this message's sender,
}
```

### Objeto de pessoa push de conversa do Android {#android-conversation-push-person-object}

```json
{
  "id" : (required, string) the identifier of this Person,
  "name" : (required, string) the display name of this Person
}
```

