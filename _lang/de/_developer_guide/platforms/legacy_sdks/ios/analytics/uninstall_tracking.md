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

Das Uninstall-Tracking verwendet Push-Benachrichtigungen im Hintergrund mit einem Braze-Flag in der Payload. Weitere Informationen finden Sie unter [Uninstall-Tracking]({{site.baseurl}}/user_guide/analytics/tracking/uninstall_tracking) in unserem Benutzerhandbuch.

## Schritt 1: Hintergrund-Push aktivieren {#step-1-enabling-background-push}

Stellen Sie sicher, dass Sie die Option **Remote notifications** im Abschnitt **Background Modes** im Tab **Capabilities** Ihres Xcode-Projekts aktiviert haben. Weitere Informationen finden Sie in unserer Dokumentation zu [stillen Push-Benachrichtigungen]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/silent_push_notifications).

## Schritt 2: Prüfung auf Braze-Hintergrund-Push {#step-2-checking-for-braze-background-push}

Braze verwendet Hintergrund-Push-Benachrichtigungen, um Uninstall-Tracking-Analytics zu erfassen. Stellen Sie sicher, dass Ihre Anwendung [keine unerwünschten Aktionen ausführt]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/customization/ignoring_internal_push), wenn sie unsere Uninstall-Tracking-Benachrichtigungen empfängt.

## Schritt 3: Vom Dashboard aus testen {#step-3-test-from-the-dashboard}

Senden Sie sich als Nächstes einen Test-Push über das Dashboard. Dieser Test-Push aktualisiert Ihr Kundenprofil nicht.

1. Erstellen Sie auf der Seite **Campaigns** eine Push-Benachrichtigungs-Campaign und wählen Sie **iOS push** als Ihre Plattform aus.<br><br>
2. Fügen Sie auf der Seite **Settings** den Schlüssel `appboy_uninstall_tracking` mit dem entsprechenden Wert `true` hinzu und aktivieren Sie **Add Content-Available Flag**.<br><br>
3. Verwenden Sie die Seite **Preview**, um sich selbst einen Test-Push für das Uninstall-Tracking zu senden.<br><br>
4. Überprüfen Sie, dass Ihre App bei Erhalt des Push keine unerwünschten automatischen Aktionen ausführt.

{% alert important %}
Diese Testschritte dienen als Stellvertreter für das Senden eines Uninstall-Tracking-Push von Braze. Wenn Badge-Zähler aktiviert sind, wird zusammen mit dem Test-Push eine Badge-Nummer gesendet, aber die Uninstall-Tracking-Pushes von Braze setzen keine Badge-Nummer in Ihrer Anwendung.
{% endalert %}

## Schritt 4: Uninstall-Tracking aktivieren {#step-4-enable-uninstall-tracking}

Befolgen Sie die Anweisungen zum [Aktivieren von Uninstall-Tracking]({{site.baseurl}}/user_guide/analytics/tracking/uninstall_tracking).