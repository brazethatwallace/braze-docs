---
nav_title: "Web-Push"
article_title: Web-Push-Benachrichtigungen
page_order: 8.5
page_type: reference
description: "Diese Referenzseite bietet einen kurzen Überblick über Web-Push-Benachrichtigungen und verlinkt zu den notwendigen Schritten, um eine zu erstellen."
platform: Web
channel:
  - push

---

# Web-Push {#web-push}

> Erfahren Sie mehr über Web-Push-Benachrichtigungen bei Braze und finden Sie Ressourcen, um Ihre eigenen zu erstellen.

Web-Push ist eine weitere großartige Möglichkeit, Nutzer:innen Ihrer Webanwendung anzusprechen. Kund:innen, die Ihre Website über [unterstützte Browser](#supported-browsers) besuchen, können sich für den Empfang von Web-Push-Benachrichtigungen Ihrer Webanwendung anmelden – unabhängig davon, ob die Webseite geladen ist oder nicht.

## Voraussetzungen {#prerequisites}

Bevor Sie Push-Nachrichten mit Braze erstellen und senden können, müssen Sie mit Ihren Entwickler:innen zusammenarbeiten, um Push in Ihre Website zu integrieren. Detaillierte Schritte finden Sie in unserem [Leitfaden zur Web-Push-Integration]({{site.baseurl}}/developer_guide/push_notifications?sdktab=web).

### Push-Berechtigung {#push-permission}

Jede Marke kann Web-Push-Benachrichtigungen auf ihrer Website integrieren und nutzen. Die Benachrichtigungen können sowohl aktuelle als auch frühere Webbesucher:innen erreichen, solange diese einen Webbrowser geöffnet haben. Besucher:innen müssen jedoch [dem Empfang von Benachrichtigungen zustimmen]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states#push-permission) – genau wie bei herkömmlichen mobilen App-Push-Benachrichtigungen.

{% alert tip %}
Erwägen Sie den Einsatz einer In-Browser-Nachricht, um Nutzer:innen zur Zustimmung für Web-Push zu bewegen – auch bekannt als [Push-Primer]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages).
{% endalert %}

## Übersicht {#overview}

Web-Push-Benachrichtigungen liefern dringende, handlungsrelevante Updates, die schnelle Conversions fördern. Mit Web-Push können Sie:

- Nachrichten genau dann auslösen, wenn sich wichtige Daten ändern, z. B. wenn ein Preis sinkt
- Nutzer:innen mit klaren Call-to-Action-Buttons zurück auf Ihre Website bringen
- Ihre Push-Benachrichtigungen mit Produkt- und Kundeninformationen personalisieren, um Ihre Nachricht relevant zu gestalten

Web-Push funktioniert genauso wie App-Push-Benachrichtigungen auf Ihrem Telefon. Weitere Informationen zum Erstellen einer Web-Push-Benachrichtigung finden Sie unter [Push-Benachrichtigung erstellen]({{site.baseurl}}/user_guide/channels/push/create_a_push_message).

![Web-Push-Beispiel mit derselben Push-Nachricht auf einem Laptop und einem Telefon.]({% image_buster /assets/img_archive/Macbook_Push.png %}){: style="border:none"}

## Mögliche Anwendungsfälle {#potential-use-cases}

Hier sind einige Beispiele für gängige Anwendungsfälle von Web-Push-Nachrichten.

| Anwendungsfall | Beschreibung |
| --- | --- |
| Kostenlose Demo | Ermutigen Sie neue Besucher:innen auf Ihrer Website, sich für kostenlose Demos anzumelden. Indem Sie Nutzer:innen die Möglichkeit geben, zu erleben, was Sie besonders macht, erhöhen Sie die Wahrscheinlichkeit, dass sie zahlende Kund:innen werden. |
| App-Download | Leiten Sie Web-Nutzer:innen zu Ihrer mobilen App, damit sie noch mehr Wert aus Ihren Produkten ziehen können. Nutzen Sie Personalisierung, um App-Vorteile basierend auf ihren aktuellen Engagement-Mustern hervorzuheben. |
| Rabatte und Aktionen | Steigern Sie das Bewusstsein der Kund:innen für zeitlich begrenzte Ereignisse und Aktionen. Kommunizieren Sie über mehrere Kanäle, einschließlich Web-Push, um die Bekanntheit der Aktionen Ihrer Marke zu erhöhen. |
| Abgebrochener Einkauf | Senden Sie automatisierte Erinnerungen an Nutzer:innen, die ihre Transaktionen nicht abgeschlossen haben, um sie zurück zum Checkout-Prozess zu bringen. <br><br>Untersuchungen von Braze haben ergeben, dass Web-Push 53 % effektiver als E-Mail und 23 % wirkungsvoller als mobiler Push ist, wenn es darum geht, Empfänger:innen dazu zu bringen, zurückzukehren und einen Kauf abzuschließen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Mögliche Anwendungsfälle" }

## Unterstützte Browser {#supported-browsers}

Die folgenden Browser unterstützen Web-Push-Benachrichtigungen.

{% multi_lang_include alerts/important_alerts.md alert='Web push private browsing' %}

- Chrome (und Chrome für Android-Mobilgeräte)
- Safari (Version 16 oder neuer)
- Firefox (und Firefox für Android-Mobilgeräte)
- Opera
- Edge

Weitere Informationen zu den Push-Protokollstandards und der Browserunterstützung finden Sie in den Ressourcen basierend auf Ihrem Browser:

- [Safari (Desktop)](https://developer.apple.com/notifications/safari-push-notifications/)
- [Safari (Mobilgerät)]({{site.baseurl}}/developer_guide/push_notifications?sdktab=safari)
- [Mozilla Firefox](https://developer.mozilla.org/en-us/docs/web/api/push_api#browser_compatibility)
- [Microsoft Edge](https://learn.microsoft.com/en-us/microsoft-edge/progressive-web-apps-chromium/how-to/push)

## 410 (Gone) und ungültige Web-Push-Endpunkte {#410-gone-and-invalid-web-push-endpoints}

Browser und Push-Dienste können **410 Gone** (oder ähnliche Fehler wie „Endpunkt nicht gültig“) zurückgeben, wenn ein Web-Push-Abo nicht mehr akzeptiert wird. Häufige Ursachen sind:

- Die Nutzer:innen haben Benachrichtigungen für Ihre Website in den Browser- oder Betriebssystemeinstellungen deaktiviert.
- Ein anderes Kundenprofil hat sich im selben Browserprofil angemeldet, sodass der Endpunkt auf den/die neue:n Abonnent:in rotiert wurde.
- Das Abo ist nach einer langen Zeit ohne Engagement abgelaufen – nachdem die Nutzer:innen erneut zugestimmt haben, wird in der nächsten Sitzung ein neues Abo erstellt.

Nachdem die Nutzer:innen Benachrichtigungen wieder aktiviert haben, lösen Sie den normalen Web-Push-Registrierungsablauf Ihrer Website erneut aus, damit Braze den neuen Abo-Endpunkt speichert.