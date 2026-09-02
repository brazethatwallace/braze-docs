---
page_order: 10.9
nav_title: Fehlerbehebung
article_title: Fehlerbehebung für Push-Benachrichtigungen im Braze SDK or Software-Development-Kit
description: "Diagnostizieren Sie Probleme bei der Zustellung und Anzeige von Push-Benachrichtigungen mithilfe eines Symptomindex, eines standardisierten Untersuchungspfads und plattformspezifischer SDK or Software-Development-Kit-Prüfungen."
channel:
  - push notifications
---

# Fehlerbehebung für Push-Benachrichtigungen {#troubleshoot-push-notifications}

> Verwenden Sie diese Seite, um Probleme bei der Zustellung und Anzeige von Push-Benachrichtigungen auf einem Gerät zu diagnostizieren. Informationen zu Dashboard-seitigen Zustellungsprüfungen (Abo-Status, Segmente, Obergrenzen) finden Sie unter [Fehlerbehebung für Push]({{site.baseurl}}/user_guide/channels/push/troubleshooting).

Bevor Sie mit dem Debugging beginnen, fügen Sie sich als [Testnutzer:in]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#adding-test-users) hinzu und lesen Sie [Testnachrichten senden]({{site.baseurl}}/developer_guide/push_notifications/sending_test_messages).

## Hier starten: Symptom zuordnen {#start-here-match-your-symptom}

Finden Sie das beobachtete Verhalten in der Tabelle und folgen Sie dann den Schritten des jeweiligen Abschnitts. Wenn Sie nicht sicher sind, welcher Abschnitt zutrifft, verwenden Sie den [standardmäßigen Untersuchungspfad](#standard-investigation-path).

| Symptom | Gehe zu |
| --- | --- |
| Push-Benachrichtigung wird auf einer Plattform nicht empfangen | Wählen Sie den entsprechenden SDK or Software-Development-Kit-Tab unter [Plattformspezifische Fehlerbehebung](#platform-specific-troubleshooting) |
| Zeilenumbrüche um Liquid-Tags sehen beim Speichern falsch aus | [Zeilenumbrüche in Push-Benachrichtigungen](#push-linebreaks) |
| Dashboard-Zustellungsprüfungen (Abo, Segment, Limits) | [Fehlerbehebung für Push]({{site.baseurl}}/user_guide/channels/push/troubleshooting) |
| Deeplink aus Push-Benachrichtigung öffnet sich nicht korrekt | [Fehlerbehebung für Deeplinking]({{site.baseurl}}/developer_guide/push_notifications/deep_linking_troubleshooting) |
| Häufige Push-Fehlercodes | [Häufige Push-Fehlermeldungen]({{site.baseurl}}/user_guide/channels/push/push_error_codes) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Push-SDK or Software-Development-Kit-Symptom" }

## Standardmäßiger Untersuchungspfad {#standard-investigation-path}

Verwenden Sie diesen Workflow für jeden Push-Benachrichtigungsvorfall. Beginnen Sie bei Schritt 1.

1. Bestätigen Sie, dass das Gerät einen gültigen Push-Token / Textbaustein hat und die Push-Berechtigung in den Geräteeinstellungen erteilt ist.
2. Bestätigen Sie im Dashboard, dass die/der Testnutzer:in dem Campaign- oder Canvas-[Segment]({{site.baseurl}}/user_guide/channels/push/troubleshooting#segment) entspricht und sich nicht in der [Kontrollgruppe]({{site.baseurl}}/user_guide/channels/push/troubleshooting#control-group-status) befindet.
3. Senden Sie eine [Test-Push-Benachrichtigung]({{site.baseurl}}/developer_guide/push_notifications/sending_test_messages) an das Testgerät.
4. [Aktivieren Sie die ausführliche Protokollierung]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging), reproduzieren Sie das Problem und lesen Sie die plattformspezifische Anleitung in Ihrem [SDK or Software-Development-Kit-Tab](#platform-specific-troubleshooting).
5. Wenn das Problem weiterhin besteht, kontaktieren Sie den [Braze-Support]({{site.baseurl}}/user_guide/administer/personal/braze_support) mit ausführlichen Protokollen, Plattform, SDK or Software-Development-Kit-Version und Campaign- oder Canvas-ID.

## Push-Klicks werden nicht protokolliert {#push-clicks-not-logged}

- Stellen Sie sicher, dass Sie die [Schritte zur Push-Integration]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift#swift_step-33-enable-push-handling) befolgt haben.
- Braze verarbeitet keine Push-Benachrichtigungen, die im Vordergrund stillschweigend empfangen werden (standardmäßiges Vordergrund-Push-Verhalten vor dem `UserNotifications`-Framework). Das bedeutet, dass Links nicht geöffnet und Push-Klicks nicht protokolliert werden. Wenn Ihre Anwendung das `UserNotifications`-Framework noch nicht integriert hat, verarbeitet Braze keine Push-Benachrichtigungen, wenn der Anwendungsstatus `UIApplicationStateActive` ist. Stellen Sie sicher, dass Ihre App Aufrufe an [Push-Verarbeitungsmethoden]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift#swift_step-33-enable-push-handling) nicht verzögert; andernfalls behandelt das Swift SDK or Software-Development-Kit Push-Benachrichtigungen möglicherweise als stille Vordergrund-Push-Ereignisse und verarbeitet sie nicht.

## Zeilenumbrüche in Push-Benachrichtigungen {#push-linebreaks}

Beim Verfassen von Push-Benachrichtigungen mit Liquid-Tags werden Zeilenumbrüche neben Liquid-Tags automatisch entfernt, bevor die Nachricht gesendet wird. Im [Push-Benachrichtigungs-Composer]({{site.baseurl}}/user_guide/channels/push/create_a_push_message) werden diese Zeilenumbrüche wieder eingefügt, damit Ihre Nachricht beim Bearbeiten lesbar bleibt. Wenn Sie beim Speichern Ihrer Nachricht Zeilenumbrüche um Liquid-Tags herum bemerken, ist dies das erwartete Verhalten.