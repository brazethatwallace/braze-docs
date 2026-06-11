---
nav_title: "Objet Web"
article_title: Objet de messagerie Web
page_order: 12
page_type: reference
channel: push
platform: Web
description: "Cet article de référence répertorie et explique les différents objets Web utilisés chez Braze."

---
# Objet notification push Web {#web-push-object}

> L'objet `web_push` vous permet de définir ou de demander des informations relatives au contenu de notification push Web et d'alertes push Web via nos [endpoints d'envoi de messages]({{site.baseurl}}/api/endpoints/messaging/).

## Objet notification push Web

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

La valeur de `image_url` doit être une URL qui renvoie vers l'emplacement où votre image est hébergée. Les images doivent être recadrées selon un rapport hauteur/largeur de 1:1.

## Objet bouton d'action push Web {#web-push-action-button-object}

```json
{
  "text": (required, string) the button's text,
  "action": (optional, string) one of "OPEN_APP", "URI", or "CLOSE", defaults to "OPEN_APP",
  "uri": (optional, string) a web URL
}
```
