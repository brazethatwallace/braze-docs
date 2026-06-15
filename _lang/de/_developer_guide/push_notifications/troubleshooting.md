---
page_order: 10.9
nav_title: Fehlersuche
article_title: Fehlerbehebung bei Push-Benachrichtigungen für das Braze SDK
channel:
  - push notifications
---

# Fehlerbehebung bei Push-Benachrichtigungen {#troubleshoot-push-notifications}

> Erfahren Sie, wie Sie Probleme mit Push-Benachrichtigungen für das Braze SDK beheben können.

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

## Zeilenumbrüche in Push-Benachrichtigungen {#push-linebreaks}

Beim Verfassen von Push-Benachrichtigungen mit Liquid-Tags werden Zeilenumbrüche neben Liquid-Tags automatisch entfernt, bevor die Nachricht gesendet wird. Im [Push-Benachrichtigungs-Composer]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/) werden diese Zeilenumbrüche wieder eingefügt, damit Ihre Nachricht beim Bearbeiten lesbar bleibt. Wenn Sie beim Speichern Ihrer Nachricht Zeilenumbrüche um Liquid-Tags herum bemerken, ist dies das erwartete Verhalten.