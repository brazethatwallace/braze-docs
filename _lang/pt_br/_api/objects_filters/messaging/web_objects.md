---
nav_title: "Objeto da Web"
article_title: Objeto de mensagens pela internet
page_order: 12
page_type: reference
channel: push
platform: Web
description: "Este artigo de referência lista e explica os diferentes objetos da Web usados na Braze."

---
# Objeto de push para a web {#web-push-object}

> O objeto `web_push` permite que você defina ou solicite informações relacionadas ao conteúdo de push para a web e alertas de push para a web por meio de nossos [endpoints de envio de mensagens]({{site.baseurl}}/api/endpoints/messaging/).

## Objeto de push para a web

```json
{
   "alert": (required, string) the notification message,
   "title": (required, string) the title that appears in the notification drawer,
   "extra": (optional, object) additional keys and values to be sent in the push,
   "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under (must be an Kindle/FireOS Push Message),
   "custom_uri": (optional, string) a web URL,
   "image_url": (optional, string) URL for image to show,
   "large_image_url": (optional, string) URL for large image, supported on Chrome Windows/Android,
   "require_interaction": (optional, boolean) whether to require the user to dismiss the notification. for a list of supported platforms, see: "https://developer.mozilla.org/en-US/docs/Web/API/Notification/requireInteraction#browser_compatibility",
   "time_to_live": (optional, integer (seconds)),
   "send_to_most_recent_device_only" : (optional, boolean) defaults to false, if set to true, Braze will only send this push to a user's most recently used browser, rather than all eligibles browsers,
   "buttons" : (optional, array of Web push action button objects) push action buttons to display
}
```

O valor de `image_url` deve ser um URL que aponte para o local onde sua imagem está hospedada. As imagens precisam ser cortadas em uma proporção de 1:1.

## Objeto de botão de ação por push da Web {#web-push-action-button-object}

```json
{
  "text": (required, string) the button's text,
  "action": (optional, string) one of "OPEN_APP", "URI", or "CLOSE", defaults to "OPEN_APP",
  "uri": (optional, string) a web URL
}
```
