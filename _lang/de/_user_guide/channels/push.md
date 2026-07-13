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

# Push

> Push-Benachrichtigungen sind eine bewährte Methode, um zeitkritische Handlungsaufforderungen über Mobilgeräte oder das Internet zu senden und Nutzer:innen erneut anzusprechen, die die App schon länger nicht mehr geöffnet haben. Sie führen Nutzer:innen direkt zu Inhalten und demonstrieren den Wert Ihrer Anwendung.

[![Braze-Lernkurs]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/path/push-fundamentals){: style="float:right;width:120px;border:0;" class="noimgborder"}

## Voraussetzungen {#prerequisites}

Bevor Sie beginnen, stellen Sie sicher, dass Folgendes vorhanden ist:

- **Push ist in Ihre App oder Website integriert.** Arbeiten Sie mit Ihren Entwickler:innen zusammen, um dies einzurichten. Detaillierte Schritte finden Sie in den Integrationsleitfäden für [iOS]({{site.baseurl}}/developer_guide/push_notifications?sdktab=swift), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications?tab=android) und [Web]({{site.baseurl}}/developer_guide/push_notifications?sdktab=web).
- **Eine Push-Opt-in-Strategie.** Nutzer:innen müssen die Push-Berechtigung auf ihrem Gerät erteilen. Erwägen Sie den Einsatz von [Push-Primer-Nachrichten]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages), um den Mehrwert zu erklären, bevor Sie die Aufforderung anzeigen.

## Anwendungsfälle {#use-cases}

| Anwendungsfall | Erklärung |
| --- | --- |
| Erstes Onboarding | Solange Nutzer:innen die ersten Schritte zur Nutzung Ihrer App nicht unternommen haben (z. B. ein Konto registrieren), ist ihr Wert stark eingeschränkt. Nutzen Sie Push-Benachrichtigungen, um Nutzer:innen zu ermutigen, diese Schritte abzuschließen, damit sie Ihre App vollständig nutzen können. |
| Erstkäufe | Sobald Nutzer:innen mit Ihrer App vertraut sind, können Sie Push-Benachrichtigungen nutzen, um sie zu In-App-Käufer:innen zu konvertieren. |
| Neue Features | Push-Benachrichtigungen können effektiv sein, um inaktive Nutzer:innen über neue Features zu informieren, die sie zurück in Ihre App locken könnten. |
| Zeitlich begrenzte Angebote | Wenn ein Angebot zeitlich begrenzt ist, ist Push eine hervorragende Möglichkeit, Ihre Nutzer:innen darüber zu informieren, bevor es abläuft. Diese Nachrichten vermitteln in der Regel ein hohes Maß an Dringlichkeit und eignen sich optimal, um kürzlich inaktiv gewordene Nutzer:innen an Ihre App zu erinnern. Wenn Ihre App beispielsweise ein Spiel ist und Sie einen In-Game-Währungsbonus für eine tägliche Spielserie anbieten, kann es ein effektiver Push sein, Nutzer:innen darauf hinzuweisen, dass ihre Serie gefährdet ist, nachdem sie eine bestimmte Anzahl von Tagen erreicht haben. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Anwendungsfälle" }

## Vorschriften für Push-Nachrichten {#push-message-regulations}

Push erreicht das Gerät Ihrer Kund:innen direkt, daher regeln App- und Store-Richtlinien, wie Sie es verwenden dürfen.

{% alert important %}
Ihre Push-Nachrichten müssen den [Richtlinien für die Überprüfung im Apple App Store](https://developer.apple.com/app-store/review/guidelines/) und den [Google-Play-Richtlinien](https://support.google.com/googleplay/android-developer/answer/9888379) entsprechen. Dazu gehören Regeln zur Nutzung von Push für Werbung, Spam, Aktionen und verwandte Themen.
{% endalert %}

| Richtlinienquelle | Zusammenfassung |
| --- | --- |
| Apple [3.2.2](https://developer.apple.com/app-store/review/guidelines/#unacceptable) | Unzulässige Verwendungen umfassen die Erstellung einer Oberfläche zur Anzeige von Drittanbieter-Apps, Erweiterungen oder Plug-ins, die dem App Store ähneln, oder als allgemeine Sammlung. |
| Apple [4.5.4](https://developer.apple.com/app-store/review/guidelines/#apple-sites-and-services) | Push darf nicht für die Funktion der App erforderlich sein und darf keine sensiblen persönlichen oder vertraulichen Informationen enthalten. Verwenden Sie Push nicht für Aktionen oder Direktmarketing, es sei denn, Kund:innen haben sich ausdrücklich über eine Einwilligungserklärung in der UI Ihrer App angemeldet und können sich in der App abmelden. |
| Apple [4.10](https://developer.apple.com/app-store/review/guidelines/#monetizing-built-in-capabilities) | Sie dürfen integrierte Funktionen wie Push-Benachrichtigungen, die Kamera oder das Gyroskop sowie Apple-Dienste wie Apple Music oder iCloud nicht monetarisieren. |
| Google Play – [Unbefugte Nutzung oder Nachahmung von Systemfunktionen](https://developers.google.com/android/play-protect/mobile-unwanted-software#muws-categories) | Apps dürfen Systembenachrichtigungen nicht nachahmen oder beeinträchtigen. Benachrichtigungen auf Systemebene sind nur für wesentliche App-Features vorgesehen (z. B. eine Airline-App, die Nutzer:innen über Angebote informiert, oder ein Spiel, das Nutzer:innen über In-Game-Aktionen benachrichtigt). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Vorschriften für Push-Nachrichten" }

## Häufig gestellte Fragen {#frequently-asked-questions}

### Wann protokolliert Braze einen erfolgreichen Versand für Push? {#when-does-braze-record-a-successful-send-for-push}

Braze protokolliert in der Regel einen **Versand**, sobald die Nachricht von Braze an Apple, Google oder Ihren Web-Push-Dienst übermittelt wurde. **Zugestellt**, Öffnungen, Bounces und Deinstallationssignale werden separat erfasst und können später eintreffen. Verwenden Sie Schritt- und Campaign-Analytics zusammen mit der [Push-Fehlerbehebung]({{site.baseurl}}/user_guide/channels/push/troubleshooting), wenn **Versendungen** und nachgelagerte Metriken nicht übereinstimmen.

## Nächste Schritte {#next-steps}

- [Push-Einrichtung]({{site.baseurl}}/user_guide/channels/push/push_setup)
- [Eine Push-Nachricht erstellen]({{site.baseurl}}/user_guide/channels/push/create_a_push_message)