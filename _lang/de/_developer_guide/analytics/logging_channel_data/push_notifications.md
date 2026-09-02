---
nav_title: Push-Benachrichtigungen
article_title: Push-Benachrichtigungsdaten über das Braze SDK or Software-Development-Kit protokollieren
page_order: 7.2
description: "Erfahren Sie, wie Sie Push-Benachrichtigungsdaten über das Braze SDK or Software-Development-Kit protokollieren können."
noindex: true
---

# Push-Benachrichtigungsdaten protokollieren {#log-push-notification-data}

> Erfahren Sie, wie Sie Push-Benachrichtigungsdaten über das Braze SDK or Software-Development-Kit protokollieren können.

{% sdktabs %}
{% sdktab android %}
## Daten über die Braze-API protokollieren (empfohlen) {#logging-data-with-the-braze-api-recommended}

Sie können Analytics in Realtime protokollieren, indem Sie Aufrufe an den [`/users/track`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track) senden. Um Analytics zu protokollieren, senden Sie den `braze_id`-Wert aus dem Braze-Dashboard, um festzustellen, welches Kundenprofil or Nutzerprofil aktualisiert werden soll.

![Beispiel für ein personalisiertes Push-Dashboard]({% image_buster /assets/img/push_implementation_guide/android_braze_id_configuration.png %}){: style="max-width:79%;"}

## Daten manuell protokollieren {#manually-logging-data}

Abhängig von den Details Ihres Payloads können Sie Analytics manuell innerhalb Ihrer `FirebaseMessagingService.onMessageReceived`-Implementierung oder Ihrer Startaktivität protokollieren. Ihre `FirebaseMessagingService`-Unterklasse muss die Ausführung innerhalb von 9 Sekunden nach dem Aufruf abschließen, um nicht vom Android-System [markiert oder beendet](https://firebase.google.com/docs/cloud-messaging/android/receive) zu werden.

{% endsdktab %}

{% sdktab swift %}
{% multi_lang_include developer_guide/swift/analytics/logging_push_data.md %}
{% endsdktab %}
{% endsdktabs %}