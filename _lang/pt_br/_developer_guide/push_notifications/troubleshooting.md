---
page_order: 10.9
nav_title: Solução de problemas
article_title: Solução de problemas de notificações por push para o SDK da Braze
channel:
  - push notifications
---

# Solução de problemas de notificações por push {#troubleshoot-push-notifications}

> Aprenda como solucionar problemas de notificações por push para o SDK da Braze.

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

## Quebras de linha em notificações por push {#push-linebreaks}

Ao redigir notificações por push com Liquid tags, as quebras de linha adjacentes às Liquid tags são automaticamente removidas antes do envio da mensagem. No [criador de notificações por push]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/), essas quebras de linha são adicionadas novamente para que sua mensagem permaneça legível durante a edição. Se você notar quebras de linha ao redor das Liquid tags ao salvar sua mensagem, esse é o comportamento esperado.