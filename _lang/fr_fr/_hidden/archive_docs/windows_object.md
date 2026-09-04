---
nav_title: "Objet Windows"
article_title: Objet de messagerie Windows
page_order: 14
page_type: reference
channel: push
platform:
  - Windows Universal
description: "Cet article de référence répertorie et explique les différents objets Windows utilisés chez Braze."
hidden: true
---
# Spécification de l'objet Windows {#windows-object-specification}

Les objets `windows_phone8_push` et `windows_universal_push` sont utilisés pour définir ou demander des informations relatives au contenu de notification push Windows Phone 8 et Windows Universal via nos [endpoints d'envoi de messages]({{site.baseurl}}/api/endpoints/messaging).

## Objet de notification push Windows Phone 8 {#windows-phone-8-push-object}

```json
{
   "push_type": (optional, string) must be "toast",
   "toast_title": (optional, string) the notification title,
   "toast_content": (required, string) the notification message,
   "toast_navigation_uri": (optional, string) page uri to send user to,
   "toast_hash": (optional, object) additional keys and values to send,
   "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under (must be a Windows Phone 8 Push Message)
}
```

## Objet de notification push Windows Universal {#windows-universal-push-object}

Consultez le [catalogue de modèles toast](https://msdn.microsoft.com/en-us/library/windows/apps/hh761494.aspx) Windows Universal pour obtenir des détails sur les options de `push_type`.

```json
{
   "push_type": (required, string) one of: "toast_text_01", "toast_text_02", "toast_text_03", "toast_text_04", "toast_image_and_text_01", "toast_image_and_text_02", "toast_image_and_text_03", or "toast_image_and_text_04",
   "toast_text1": (required, string) the first line of text in the template,
   "toast_text2": (optional, string) the second line of text (for templates with > 1 line of text),
   "toast_text3": (optional, string) the third line of text (for the *_04 templates),
   "toast_text_img_name": (optional, string) the path for the image for the templates that include an image,
   "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under (must be a Windows Universal Push Message),
   "extra_launch_string": (optional, string) used to add deep linking functionality by passing extra values to the launch string
}
```

Pour plus d'informations sur l'utilisation du paramètre `extra_launch_string` pour la [création de liens profonds]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls#what-is-deep-linking), consultez la section [Deep Linking avec Windows Universal.]({{site.baseurl}}/hidden/archive_docs/windows_universal/push_notifications#step-5-deep-linking-from-push-into-your-app)