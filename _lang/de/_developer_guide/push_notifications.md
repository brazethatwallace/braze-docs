---
nav_title: Push-Benachrichtigungen
article_title: Push-Benachrichtigungen
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
## Über Push-Benachrichtigungen für Android TV {#about-push-notifications-for-android-tv}

![Illustration eines Android-TV-Geräts für die Anleitung zu Android-TV-Push-Benachrichtigungen.]({% image_buster /assets/img/Television.png %}){: style="float:right;max-width:25%;margin-left:15px; border: 0"}

Obwohl es sich nicht um ein natives Feature handelt, wird die Android-TV-Push-Integration durch die Nutzung des Braze Android SDK und Firebase Cloud Messaging ermöglicht, um ein Push-Token / Textbaustein für Android TV zu registrieren. Sie müssen jedoch eine UI erstellen, um den Benachrichtigungs-Payload nach dem Empfang anzuzeigen.

## Voraussetzungen {#prerequisites}

Um dieses Feature zu nutzen, müssen Sie Folgendes abschließen:

- [Das Braze Android SDK integrieren]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android)
- [Push-Benachrichtigungen für das Braze Android SDK einrichten]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android)

## Push-Benachrichtigungen einrichten {#setting-up-push-notifications}

So richten Sie Push-Benachrichtigungen für Android TV ein:

1. Erstellen Sie eine angepasste Ansicht in Ihrer App, um Ihre Benachrichtigungen anzuzeigen.
2. Erstellen Sie eine [angepasste Benachrichtigungs-Factory]({{site.baseurl}}/developer_guide/push_notifications/customization?sdktab=android#android_customization-display). Dies überschreibt das Standardverhalten des SDK und ermöglicht es Ihnen, die Benachrichtigungen manuell anzuzeigen. Durch die Rückgabe von `null` wird verhindert, dass das SDK die Benachrichtigung verarbeitet, und es ist angepasster Code erforderlich, um die Benachrichtigung anzuzeigen. Nach Abschluss dieser Schritte können Sie Push-Benachrichtigungen an Android TV senden.<br><br>
3. (Optional) Um Klick-Analytics effektiv zu tracken, richten Sie Klick-Analytics-Tracking ein. Dies kann durch die Erstellung eines [Push-Callbacks]({{site.baseurl}}/developer_guide/push_notifications/customization?sdktab=android#android_push-callback) erreicht werden, der auf Braze-Push-Opened- und -Received-Intents lauscht.

{% alert note %}
Diese Benachrichtigungen bleiben nicht bestehen und sind für Nutzer:innen nur sichtbar, wenn das Gerät sie anzeigt. Dies liegt daran, dass das Benachrichtigungscenter von Android TV keine historischen Benachrichtigungen unterstützt.
{% endalert %}

## Android-TV-Push-Benachrichtigungen testen {#testing-android-tv-push-notifications}

Um zu testen, ob Ihre Push-Implementierung erfolgreich ist, senden Sie eine Benachrichtigung über das Braze-Dashboard, wie Sie es normalerweise für ein Android-Gerät tun würden.

- **Wenn die Anwendung geschlossen ist**: Die Push-Nachricht wird als Toast-Benachrichtigung auf dem Bildschirm angezeigt.
- **Wenn die Anwendung geöffnet ist**: Sie haben die Möglichkeit, die Nachricht in Ihrer eigenen gehosteten UI anzuzeigen. Orientieren Sie sich am UI-Styling der In-App-Nachrichten des Android Mobile SDK.

## Best Practices {#best-practices}

Für Marketer, die Braze verwenden, ist das Starten einer Campaign für Android TV identisch mit dem Starten eines Push an Android-Mobile-Apps. Um diese Geräte exklusiv anzusprechen, wählen Sie die Android-TV-App in der Segmentierung aus.

Die von FCM zurückgegebene Antwort zu Zustellung und Klicks folgt derselben Konvention wie bei einem mobilen Android-Gerät; daher sind alle Fehler im Nachrichtenaktivitätsprotokoll sichtbar.

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