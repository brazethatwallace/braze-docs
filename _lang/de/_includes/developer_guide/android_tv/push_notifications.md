## Über Push-Benachrichtigungen für Android TV {#about-push-notifications-for-android-tv}

![Illustration eines Android TV-Geräts für die Anleitung zu Android TV Push-Benachrichtigungen.]({% image_buster /assets/img/Television.png %}){: style="float:right;max-width:25%;margin-left:15px; border: 0"}

Obwohl es sich nicht um ein natives Feature handelt, wird die Push-Integration von Android TV ermöglicht, indem das Braze Android SDK und Firebase Cloud Messaging genutzt werden, um ein Push-Token für Android TV zu registrieren. Es ist jedoch notwendig, eine UI zu erstellen, um die Nutzdaten der Benachrichtigung nach deren Empfang anzuzeigen.

## Voraussetzungen {#prerequisites}

Um dieses Feature nutzen zu können, müssen Sie folgende Schritte ausführen:

- [Braze Android SDK integrieren]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android)
- [Push-Benachrichtigungen für das Braze Android SDK einrichten]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/?tab=android)

## Push-Benachrichtigungen einrichten {#setting-up-push-notifications}

So richten Sie Push-Benachrichtigungen für Android TV ein:

1. Erstellen Sie eine angepasste Ansicht in Ihrer App, um Ihre Benachrichtigungen anzuzeigen.
2. Erstellen Sie eine [angepasste Notification Factory]({{site.baseurl}}/developer_guide/push_notifications/customization?sdktab=android#android_customization-display). Damit wird das Standardverhalten des SDK außer Kraft gesetzt und Sie können die Benachrichtigungen manuell anzeigen lassen. Die Rückgabe von `null` verhindert die Verarbeitung durch das SDK und erfordert angepassten Code, um die Benachrichtigung anzuzeigen. Nachdem diese Schritte abgeschlossen sind, können Sie mit dem Senden von Push-Nachrichten an Android TV beginnen!<br><br>
3. (Optional) Um Klick-Analytics effektiv zu verfolgen, richten Sie Klick-Analytics-Tracking ein. Dies können Sie erreichen, indem Sie einen [Push-Callback]({{site.baseurl}}/developer_guide/push_notifications/customization?sdktab=android#android_push-callback) erstellen, der auf die geöffneten und empfangenen Push-Intents von Braze wartet.

{% alert note %}
Diese Benachrichtigungen **bleiben nicht persistent** und sind für Nutzer:innen nur sichtbar, wenn das Gerät sie anzeigt. Das liegt daran, dass die Benachrichtigungszentrale von Android TV keine historischen Benachrichtigungen unterstützt.
{% endalert %}

## Testen von Android TV Push-Benachrichtigungen {#testing-android-tv-push-notifications}

Um zu testen, ob Ihre Push-Implementierung erfolgreich ist, senden Sie eine Benachrichtigung vom Braze-Dashboard aus, wie Sie es normalerweise bei einem Android-Gerät tun würden.

- **Bei geschlossener Anwendung:** Die Push-Nachricht zeigt eine Toast-Benachrichtigung auf dem Bildschirm an.
- **Bei geöffneter Anwendung:** Sie haben die Möglichkeit, die Nachricht in Ihrer eigenen gehosteten UI anzuzeigen. Wir empfehlen, den UI-Stil der In-App-Nachrichten unseres Android Mobile SDK zu übernehmen.

## Best Practices

Für Marketer, die Braze verwenden, ist das Starten einer Campaign für Android TV identisch mit dem Starten eines Push für Android Mobile Apps. Um ausschließlich diese Geräte anzusprechen, empfehlen wir, bei der Segmentierung die Android TV App auszuwählen.

Die Antworten zu Zustellung und Klicks, die von FCM zurückgegeben werden, folgen der gleichen Konvention wie bei einem Android-Mobilgerät; daher werden alle Fehler im Nachrichten-Aktivitätsprotokoll angezeigt.