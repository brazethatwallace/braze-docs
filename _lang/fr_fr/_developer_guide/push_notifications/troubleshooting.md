---
page_order: 10.9
nav_title: Résolution des problèmes
article_title: Résolution des problèmes des notifications push pour le SDK Braze
channel:
  - push notifications
---

# Résolution des problèmes des notifications push {#troubleshoot-push-notifications}

> Découvrez comment résoudre les problèmes liés aux notifications push pour le SDK Braze.

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

## Sauts de ligne dans les notifications push {#push-linebreaks}

Lors de la rédaction de notifications push avec des étiquettes Liquid, les sauts de ligne adjacents aux étiquettes Liquid sont automatiquement supprimés avant l'envoi du message. Dans le [compositeur de notifications push]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message), ces sauts de ligne sont réajoutés afin que votre message reste lisible pendant la modification. Si vous remarquez des sauts de ligne autour des étiquettes Liquid lors de l'enregistrement de votre message, il s'agit d'un comportement attendu.