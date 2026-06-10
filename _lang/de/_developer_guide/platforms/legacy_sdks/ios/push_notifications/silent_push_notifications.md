---
nav_title: Stille Push-Benachrichtigungen
article_title: Stille Push-Benachrichtigungen für iOS
platform: iOS
page_order: 4
description: "Dieser Referenzartikel behandelt die Implementierung stiller Push-Benachrichtigungen in Ihrer iOS-Anwendung."
channel:
  - push

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Stille Push-Benachrichtigungen {#silent-push-notifications}

Push-Benachrichtigungen ermöglichen es Ihnen, Ihre App bei wichtigen Ereignissen zu benachrichtigen. Sie können eine Push-Benachrichtigung senden, wenn Sie neue Sofortnachrichten zustellen möchten, aktuelle Eilmeldungen versenden oder die neueste Folge der Lieblingssendung Ihrer Nutzer:innen zum Herunterladen für die Offline-Nutzung bereitsteht. Push-Benachrichtigungen können auch still sein – sie enthalten dann keine Warnmeldung und keinen Ton und dienen ausschließlich dazu, die Oberfläche Ihrer App zu aktualisieren oder Hintergrundarbeiten auszulösen.

Push-Benachrichtigungen eignen sich hervorragend für sporadische, aber unmittelbar wichtige Inhalte, bei denen die Verzögerung zwischen Hintergrundabrufen möglicherweise nicht akzeptabel ist. Push-Benachrichtigungen können auch deutlich effizienter sein als Hintergrundabrufe, da Ihre Anwendung nur bei Bedarf gestartet wird.

Push-Benachrichtigungen unterliegen Rate-Limits – senden Sie also ruhig so viele, wie Ihre Anwendung benötigt. iOS und die APNs-Server steuern, wie oft sie zugestellt werden, und Sie bekommen keine Probleme, wenn Sie zu viele senden. Wenn Ihre Push-Benachrichtigungen gedrosselt werden, werden sie möglicherweise verzögert, bis das Gerät das nächste Mal ein Keep-Alive-Paket sendet oder eine andere Benachrichtigung erhält.

## Stille Push-Benachrichtigungen senden {#sending-silent-push-notifications}

Um eine stille Push-Benachrichtigung zu senden, setzen Sie das Flag `content-available` in der Nutzlast einer Push-Benachrichtigung auf `1`. Wenn Sie eine stille Push-Benachrichtigung senden, möchten Sie möglicherweise auch einige Daten in die Nutzlast der Benachrichtigung aufnehmen, damit Ihre Anwendung auf das Ereignis Bezug nehmen kann. Dies kann Ihnen einige Netzwerkanfragen ersparen und die Reaktionsfähigkeit Ihrer App verbessern.

{% alert warning %}
Es wird davon abgeraten, sowohl einen Titel als auch einen Textkörper zusammen mit `content-available=1` anzuhängen, da dies zu undefiniertem Verhalten führen kann. Um sicherzustellen, dass eine Benachrichtigung wirklich still ist, schließen Sie sowohl den Titel als auch den Text aus, wenn Sie das `content-available`-Flag auf `1` setzen. Weitere Einzelheiten finden Sie in der offiziellen [Apple-Dokumentation über Hintergrundaktualisierungen](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/pushing_background_updates_to_your_app).
{% endalert %}

Das `content-available`-Flag kann sowohl im Braze-Dashboard als auch in unserem [Apple-Push-Objekt]({{site.baseurl}}/api/objects_filters/messaging/apple_object/) in der [Messaging-API]({{site.baseurl}}/api/endpoints/messaging/) gesetzt werden.

![Das Braze-Dashboard mit dem Kontrollkästchen „content-available“ im Tab „Einstellungen“ des Push-Composers.]({% image_buster /assets/img_archive/remote_notification.png %} "content available")

## Stille Push-Benachrichtigungen zum Triggern von Hintergrundarbeiten verwenden {#use-silent-push-notifications-to-trigger-background-work}

Stille Push-Benachrichtigungen können Ihre App aus dem Zustand „Angehalten“ oder „Nicht ausgeführt“ aufwecken, um Inhalte zu aktualisieren oder bestimmte Aufgaben auszuführen, ohne Ihre Nutzer:innen darüber zu informieren.

Um stille Push-Benachrichtigungen zum Triggern von Hintergrundarbeiten zu verwenden, richten Sie das `content-available`-Flag gemäß den vorhergehenden Anweisungen ohne Nachricht oder Ton ein. Richten Sie den Hintergrundmodus Ihrer App ein, um `remote notifications` unter dem Tab **Capabilities** in Ihren Projekteinstellungen zu aktivieren. Eine Remote-Benachrichtigung ist einfach eine normale Push-Benachrichtigung mit gesetztem `content-available`-Flag.

![Xcode mit dem Kontrollkästchen „remote notifications“ unter „capabilities“.]({% image_buster /assets/img_archive/background_mode.png %} "background mode enabled")

Die Aktivierung des Hintergrundmodus für Remote-Benachrichtigungen ist für das [Uninstall-Tracking]({{site.baseurl}}/developer_guide/analytics/tracking_uninstalls/?sdktab=swift) erforderlich.

Auch wenn der Hintergrundmodus für Remote-Benachrichtigungen aktiviert ist, startet das System Ihre App nicht im Hintergrund, wenn die Nutzer:innen das Beenden der Anwendung erzwungen haben. Die Nutzer:innen müssen die Anwendung explizit starten oder das Gerät neu starten, bevor die App vom System automatisch im Hintergrund gestartet werden kann.

Weitere Informationen finden Sie unter [Hintergrundaktualisierungen pushen](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/pushing_background_updates_to_your_app?language=objc) und [`application:didReceiveRemoteNotification:fetchCompletionHandler:`](https://developer.apple.com/library/ios/documentation/UIKit/Reference/UIApplicationDelegate_Protocol/index.html#//apple_ref/occ/intfm/UIApplicationDelegate/application:didReceiveRemoteNotification:fetchCompletionHandler:).

## Einschränkungen bei stillen iOS-Benachrichtigungen {#ios-silent-notifications-limitations}

Das iOS-Betriebssystem kann Benachrichtigungen für einige Features einschränken. Beachten Sie, dass bei Schwierigkeiten mit diesen Features die iOS-Einschränkung für stille Benachrichtigungen die Ursache sein könnte.

Braze verfügt über mehrere Features, die auf stille Push-Benachrichtigungen unter iOS angewiesen sind:

| Feature | Nutzererlebnis |
|---|---|
| Uninstall-Tracking | Nutzer:innen erhalten nachts eine stille Uninstall-Tracking-Push-Benachrichtigung. |
| Geofences | Stille Synchronisierung von Geofences vom Server zum Gerät. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Weitere Einzelheiten finden Sie in der Dokumentation zu Apples [Instanzmethode](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623013-application) und [nicht empfangenen Benachrichtigungen](https://developer.apple.com/library/content/technotes/tn2265/_index.html#//apple_ref/doc/uid/DTS40010376-CH1-TNTAG23).

[8]:https://developer.apple.com/library/content/technotes/tn2265/_index.html#//apple_ref/doc/uid/DTS40010376-CH1-TNTAG23