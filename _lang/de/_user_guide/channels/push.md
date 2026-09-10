---
nav_title: Push
article_title: Push
page_order: 7
page_type: landing
description: "Senden Sie zeitkritische Handlungsaufforderungen über mobile und Web-Push-Benachrichtigungen, um Nutzer:innen erneut anzusprechen und Aktionen auszulösen."
channel:
  - push
search_rank: 3
---

# Push {#push}

> Push-Benachrichtigungen senden zeitkritische Handlungsaufforderungen an Mobilgeräte und Webbrowser und sprechen Nutzer:innen erneut an, die Ihre App in letzter Zeit nicht geöffnet haben. Sie führen direkt zu relevanten Inhalten und demonstrieren den fortlaufenden Wert Ihres Produkts. Dieser Hub behandelt die Push-Integration, Opt-in-Strategien, Nachrichtentypen, Best Practices und plattformspezifische Einstellungen für iOS, Android und Web. Ziehen Sie [Push-Primer-Nachrichten]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages) in Betracht, bevor Sie die Systemberechtigung anfordern. Lesen Sie die Integrationsleitfäden für [iOS]({{site.baseurl}}/developer_guide/push_notifications?sdktab=swift), [Android]({{site.baseurl}}/developer_guide/push_notifications?sdktab=android) und [Web]({{site.baseurl}}/developer_guide/push_notifications?sdktab=web), um loszulegen.

[![Braze-Lernkurs]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/path/push-fundamentals){: style="float:right;width:120px;border:0;" class="noimgborder"}

## Voraussetzungen {#prerequisites}

Bevor Sie beginnen, stellen Sie sicher, dass Folgendes vorhanden ist:

- **Push ist in Ihre App oder Website integriert.** Arbeiten Sie mit Ihren Entwickler:innen zusammen, um dies einzurichten. Detaillierte Schritte finden Sie in den Integrationsleitfäden für [iOS]({{site.baseurl}}/developer_guide/push_notifications?sdktab=swift), [Android]({{site.baseurl}}/developer_guide/push_notifications?sdktab=android) und [Internet]({{site.baseurl}}/developer_guide/push_notifications?sdktab=web).
- **Eine Push-Opt-in-Strategie.** Nutzer:innen müssen die Push-Berechtigung auf ihrem Gerät erteilen. Erwägen Sie den Einsatz von [Push-Primer-Nachrichten]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages), um den Mehrwert zu erklären, bevor die Anfrage angezeigt wird.

## Anwendungsfälle {#use-cases}

| Anwendungsfall | Erläuterung |
| --- | --- |
| Erstmaliges Onboarding | Bis Nutzer:innen die ersten Schritte zur Nutzung Ihrer App unternommen haben (z. B. ein Konto registrieren), ist ihr Wert stark eingeschränkt. Verwenden Sie Push-Benachrichtigungen, um Nutzer:innen zu ermutigen, diese Schritte abzuschließen, damit sie Ihre App in vollem Umfang nutzen können. |
| Erste Käufe | Sobald Nutzer:innen mit Ihrer App vertraut sind, können Sie Push-Benachrichtigungen nutzen, um sie zu In-App-Käufer:innen zu machen. |
| Neue Features | Push-Benachrichtigungen können inaktive Nutzer:innen effektiv über neue Features informieren, die sie dazu bewegen könnten, zu Ihrer App zurückzukehren. |
| Zeitlich begrenzte Angebote | Wenn ein Angebot zeitlich begrenzt ist, eignet sich Push hervorragend, um Ihre Nutzer:innen darüber zu informieren, bevor es abläuft. Diese Nachrichten vermitteln in der Regel ein hohes Maß an Dringlichkeit und sind optimal, um kürzlich inaktiv gewordene Nutzer:innen an Ihre App zu erinnern. Wenn Ihre App zum Beispiel ein Spiel ist und Sie einen In-Game-Währungsbonus für eine tägliche Spielserie anbieten, kann eine Benachrichtigung, dass die Serie gefährdet ist, ein effektiver Push sein, nachdem eine bestimmte Anzahl von Tagen erreicht wurde. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Anwendungsfälle" }

## Vorschriften für Push-Nachrichten {#push-message-regulations}

Push erreicht das Gerät Ihrer Kund:innen direkt, daher regeln App- und Store-Richtlinien, wie Sie es verwenden dürfen.

{% alert important %}
Ihre Push-Nachrichten müssen den [Richtlinien für die Überprüfung im Apple App Store](https://developer.apple.com/app-store/review/guidelines/) und den [Google Play-Richtlinien](https://support.google.com/googleplay/android-developer/answer/9888379) entsprechen. Das umfasst Regeln zur Verwendung von Push für Werbung, Spam, Aktionen und verwandte Themen.
{% endalert %}

| Richtlinienquelle | Zusammenfassung |
| --- | --- |
| Apple [3.2.2](https://developer.apple.com/app-store/review/guidelines/#unacceptable) | Zu den unzulässigen Verwendungen gehört die Erstellung einer Oberfläche zur Anzeige von Drittanbieter-Apps, -Erweiterungen oder -Plug-ins, die dem App Store ähnelt, oder als allgemeine Sammlung. |
| Apple [4.5.4](https://developer.apple.com/app-store/review/guidelines/#apple-sites-and-services) | Push darf nicht erforderlich sein, damit die App funktioniert, und darf keine sensiblen persönlichen oder vertraulichen Informationen übermitteln. Verwenden Sie Push nicht für Aktionen oder Direktmarketing, es sei denn, Kund:innen haben über eine Einwilligungserklärung in der Benutzeroberfläche Ihrer App ausdrücklich ein Opt-in gegeben und können sich in der App abmelden. |
| Apple [4.10](https://developer.apple.com/app-store/review/guidelines/#monetizing-built-in-capabilities) | Integrierte Funktionen wie Push-Benachrichtigungen, die Kamera oder das Gyroskop sowie Apple-Dienste wie Apple Music oder iCloud dürfen nicht monetarisiert werden. |
| Google Play — [Unbefugte Nutzung oder Nachahmung von Systemfunktionen](https://developers.google.com/android/play-protect/mobile-unwanted-software#muws-categories) | Apps dürfen Systembenachrichtigungen nicht nachahmen oder beeinträchtigen. Benachrichtigungen auf Systemebene sind nur für wesentliche App-Funktionen vorgesehen (z. B. eine Airline-App, die Nutzer:innen über Angebote informiert, oder ein Spiel, das Nutzer:innen über In-Game-Aktionen benachrichtigt). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Vorschriften für Push-Nachrichten" }

## Häufig gestellte Fragen {#frequently-asked-questions}

### Wann erfasst Braze einen erfolgreichen Versand für Push? {#when-does-braze-record-a-successful-send-for-push}

Braze protokolliert in der Regel einen **Versand**, sobald die Nachricht von Braze an Apple, Google oder Ihren Web-Push-Dienst gesendet wurde. **Zugestellt**, Öffnungen, Bounces und Deinstallationssignale werden separat erfasst und können zeitverzögert eintreffen. Verwenden Sie Step- und Campaign-Level-Analytics zusammen mit der [Push-Fehlerbehebung]({{site.baseurl}}/user_guide/channels/push/troubleshooting), wenn **Versendungen** und nachgelagerte Metriken nicht übereinstimmen.

## Nächste Schritte {#next-steps}

{% article_tiles %}
- name: Push-Einrichtung
  link: /docs/user_guide/channels/push/push_setup
  description: Integrieren Sie Push und konfigurieren Sie Plattformeinstellungen für iOS, Android und Internet.
- name: Push-Nachricht erstellen
  link: /docs/user_guide/channels/push/create_a_push_message
  description: Erstellen und versenden Sie Push-Campaigns und Canvases.
{% endarticle_tiles %}