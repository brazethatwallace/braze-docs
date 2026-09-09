---
nav_title: "Objeto do Windows"
article_title: Objeto de envio de mensagens do Windows
page_order: 14
page_type: reference
channel: push
platform:
  - Windows Universal
description: "Este artigo de referência lista e explica os diferentes objetos do Windows usados na Braze."
hidden: true
---
# Especificação do objeto do Windows {#windows-object-specification}

Os objetos `windows_phone8_push` e `windows_universal_push` são usados para definir ou solicitar informações relacionadas ao conteúdo de push do Windows Phone 8 e push universal do Windows por meio dos nossos [endpoints de envio de mensagens]({{site.baseurl}}/api/endpoints/messaging).

## Objeto push do Windows Phone 8 {#windows-phone-8-push-object}

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

## Objeto push do Windows Universal {#windows-universal-push-object}

Consulte o [catálogo de modelos de toast](https://msdn.microsoft.com/en-us/library/windows/apps/hh761494.aspx) do Windows Universal para obter detalhes sobre as opções de `push_type`.

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

Para saber mais sobre como usar o parâmetro `extra_launch_string` para [deep linking]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls#what-is-deep-linking), consulte [Deep linking com Windows Universal.]({{site.baseurl}}/hidden/archive_docs/windows_universal/push_notifications#step-5-deep-linking-from-push-into-your-app)