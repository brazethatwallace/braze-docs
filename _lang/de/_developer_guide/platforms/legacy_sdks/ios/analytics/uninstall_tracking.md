---
nav_title: Uninstall-Tracking
article_title: Uninstall-Tracking für iOS
platform: iOS
page_order: 7
description: "Dieser Artikel beschreibt, wie Sie das Uninstall-Tracking für Ihre iOS-Anwendung konfigurieren."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Uninstall-Tracking für iOS {#uninstall-tracking-for-ios}

> In diesem Artikel erfahren Sie, wie Sie das Uninstall-Tracking für Ihre iOS-Anwendung konfigurieren und wie Sie testen können, damit Ihre App keine unerwünschten automatischen Aktionen ausführt, wenn sie einen Push zum Uninstall-Tracking von Braze empfängt.

Das Uninstall-Tracking verwendet Push-Benachrichtigungen im Hintergrund mit einem Braze-Flag in der Payload. Weitere Informationen finden Sie unter [Uninstall-Tracking]({{site.baseurl}}/user_guide/data_and_analytics/tracking/uninstall_tracking#uninstall-tracking) in unserem Benutzerhandbuch.

## 1. Schritt: Hintergrund-Push aktivieren {#step-1-enabling-background-push}

Vergewissern Sie sich, dass Sie die Option **Remote notifications** im Abschnitt **Background Modes** auf dem Tab **Capabilities** Ihres Xcode-Projekts aktiviert haben. Weitere Einzelheiten finden Sie in unserer Dokumentation zur [stillen Push-Benachrichtigung]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/silent_push_notifications).

## 2. Schritt: Braze-Hintergrund-Push prüfen {#step-2-checking-for-braze-background-push}

Braze verwendet Push-Benachrichtigungen im Hintergrund, um Analytics für das Uninstall-Tracking zu sammeln. Stellen Sie sicher, dass Ihre Anwendung [keine unerwünschten Aktionen durchführt]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/customization/ignoring_internal_push), wenn sie Benachrichtigungen zum Uninstall-Tracking empfängt.

## 3. Schritt: Im Dashboard testen {#step-3-test-from-the-dashboard}

Als Nächstes senden Sie sich selbst einen Test-Push vom Dashboard aus. Dieser Test-Push wird Ihr Nutzerprofil nicht aktualisieren.

1. Erstellen Sie auf der Seite **Campaigns** eine Push-Benachrichtigungskampagne und wählen Sie **iOS push** als Plattform.<br><br>
2. Fügen Sie auf der Seite **Settings** den Schlüssel `appboy_uninstall_tracking` mit dem entsprechenden Wert `true` hinzu und markieren Sie **Add Content-Available Flag**.<br><br>
3. Verwenden Sie die Seite **Preview**, um sich selbst einen Test-Push für das Uninstall-Tracking zu senden.<br><br>
4. Vergewissern Sie sich, dass Ihre App beim Empfang des Push keine unerwünschten automatischen Aktionen ausführt.

{% alert important %}
Diese Testschritte sind ein Proxy für das Senden eines Uninstall-Tracking-Push von Braze. Wenn Sie die Badge-Zählung aktiviert haben, wird eine Badge-Nummer zusammen mit dem Test-Push gesendet, aber die Braze-Uninstall-Tracking-Pushes setzen keine Badge-Nummer in Ihrer Anwendung.
{% endalert %}

## 4. Schritt: Uninstall-Tracking aktivieren {#step-4-enable-uninstall-tracking}

Folgen Sie den Anweisungen zur [Aktivierung des Uninstall-Trackings]({{site.baseurl}}/user_guide/data_and_analytics/tracking/uninstall_tracking#uninstall-tracking).