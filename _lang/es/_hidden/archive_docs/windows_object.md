---
nav_title: "Objeto Windows"
article_title: Objeto de mensajería de Windows
page_order: 14
page_type: reference
channel: push
platform:
  - Windows Universal
description: "Este artículo de referencia enumera y explica los diferentes objetos de Windows utilizados en Braze."
hidden: true
---
# Especificación de objetos de Windows {#windows-object-specification}

Los objetos `windows_phone8_push` y `windows_universal_push` se utilizan para definir o solicitar información relacionada con el contenido de Windows Phone 8 Push y Windows Universal Push a través de nuestros [puntos finales de mensajería]({{site.baseurl}}/api/endpoints/messaging/).

## Objeto push de Windows Phone 8 {#windows-phone-8-push-object}

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

## Objeto push de Windows Universal {#windows-universal-push-object}

Consulta el [catálogo de plantillas de notificaciones toast](https://msdn.microsoft.com/en-us/library/windows/apps/hh761494.aspx) de Windows Universal para conocer los detalles sobre las opciones de `push_type`.

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

Para obtener más información sobre el uso del parámetro `extra_launch_string` para la [vinculación en profundidad]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls/#what-is-deep-linking), consulta [Vinculación en profundidad con Windows Universal.]({{site.baseurl}}/developer_guide/platform_integration_guides/windows_universal/push_notifications/integration/#step-4-deep-linking-from-push-into-your-app)