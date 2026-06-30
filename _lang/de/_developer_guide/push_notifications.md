---
nav_title: Push-Benachrichtigungen
article_title: "Push-Benachrichtigungen für das Braze SDK"
page_order: 2.3
description: "Auf dieser Landing-Page finden Sie alles rund um Push-Benachrichtigungen."
---

# Push-Benachrichtigungen {#push-notifications}

> [Push-Benachrichtigungen]({{site.baseurl}}/user_guide/channels/push) ermöglichen es Ihnen, von Ihrer App aus Benachrichtigungen über wichtige Ereignisse zu versenden. Sie können eine Push-Benachrichtigung senden, wenn Sie neue Sofortnachrichten zustellen möchten, aktuelle Eilmeldungen versenden oder die neueste Folge der Lieblingssendung Ihrer Nutzer:innen zum Herunterladen für die Offline-Nutzung bereitsteht. Sie sind auch effizienter als Hintergrundabrufe, da Ihre Anwendung nur bei Bedarf gestartet wird.

{% alert note %}
Wenn **Redirect to web URL** mit **Open web URL inside app** nicht ausgewählt ist, der Link aber trotzdem in der App geöffnet wird, verarbeitet die App möglicherweise die URL selbst (z. B. über Universal Links unter iOS oder App Links unter Android). Um den Link stattdessen im Browser zu öffnen, stellen Sie sicher, dass Ihre App die URL an den Systembrowser delegiert, wenn Nutzer:innen auf die Benachrichtigung tippen, oder passen Sie die URL-Verarbeitung Ihrer App so an, dass die Klickaktion mit der Einstellung im Braze-Dashboard übereinstimmt. Informationen zur Konfiguration von Klickaktionen und URL-Verarbeitung finden Sie in der Push-Dokumentation Ihrer Plattform.
{% endalert %}

{% sdktabs %}
{% sdktab web %}
{% multi_lang_include developer_guide/web/push_notifications.md %}
{% endsdktab %}

{% sdktab android %}
{% multi_lang_include developer_guide/android/push_notifications.md %}
{% endsdktab %}

{% sdktab swift %}
{% multi_lang_include developer_guide/swift/push_notifications.md %}
{% endsdktab %}

{% sdktab android tv %}
{% multi_lang_include developer_guide/android_tv/push_notifications.md %}
{% endsdktab %}

{% sdktab cordova %}
{% multi_lang_include developer_guide/cordova/push_notifications.md %}
{% endsdktab %}

{% sdktab flutter %}
{% multi_lang_include developer_guide/flutter/push_notifications.md %}
{% endsdktab %}

{% sdktab huawei %}
{% multi_lang_include developer_guide/huawei/push_notifications.md %}
{% endsdktab %}

{% sdktab react native %}
{% multi_lang_include developer_guide/react_native/push_notifications.md %}
{% endsdktab %}

{% sdktab safari %}
{% multi_lang_include developer_guide/safari/push_notifications.md %}
{% endsdktab %}

{% sdktab unity %}
{% multi_lang_include developer_guide/unity/push_notifications.md %}
{% endsdktab %}

{% sdktab .NET MAUI (Xamarin)%}
{% multi_lang_include developer_guide/xamarin/push_notifications.md %}
{% endsdktab %}
{% endsdktabs %}