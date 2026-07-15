---
page_order: 10.9
nav_title: Solución de problemas
article_title: Solución de problemas con las notificaciones push para el SDK de Braze
channel:
  - push notifications
---

# Solución de problemas con las notificaciones push {#troubleshoot-push-notifications}

> Aprende a solucionar problemas relacionados con las notificaciones push para el SDK de Braze.

{% sdktabs %}
{% sdktab web %}
{% multi_lang_include developer_guide/web/push_notifications/troubleshooting.md %}
{% endsdktab %}

{% sdktab android %}
{% multi_lang_include developer_guide/android/push_notifications/troubleshooting.md %}
{% endsdktab %}

{% sdktab swift %}
{% multi_lang_include developer_guide/swift/push_notifications/troubleshooting.md %}
{% endsdktab %}

{% sdktab fireos %}
{% multi_lang_include developer_guide/android/push_notifications/troubleshooting.md %}
{% endsdktab %}

{% sdktab .NET MAUI (Xamarin) %}
{% multi_lang_include developer_guide/xamarin/push_notifications/troubleshooting.md %}
{% endsdktab %}
{% endsdktabs %}

## Saltos de línea en las notificaciones push {#push-linebreaks}

Al redactar notificaciones push con etiquetas de Liquid, los saltos de línea adyacentes a las etiquetas de Liquid se eliminan automáticamente antes de que se envíe el mensaje. En el [compositor de notificaciones push]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message), estos saltos de línea se vuelven a añadir para que tu mensaje siga siendo legible mientras lo editas. Si notas saltos de línea alrededor de las etiquetas de Liquid al guardar tu mensaje, se trata de un comportamiento esperado.