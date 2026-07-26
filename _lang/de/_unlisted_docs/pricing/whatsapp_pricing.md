---
nav_title: WhatsApp-Preisaktualisierungen
permalink: "/whatsapp_pricing_updates/"
hidden: true
noindex: true
hide_toc: true
---

# WhatsApp-Preisaktualisierungen {#whatsapp-pricing-updates}

## Zusätzliche WhatsApp-Preisänderungen im Oktober 2025 {#additional-whatsapp-pricing-changes-in-october-2025}
*Zuletzt aktualisiert am 3. September 2025*

### Preisänderungen in einigen Regionen {#pricing-changes-in-some-regions}

Ab dem **1. Oktober** aktualisiert Meta die Tarife in bestimmten Märkten.

- **Für Utility- und Authentifizierungsnachrichten:** Die Tarife werden in Argentinien, Ägypten, Mexiko und Nordamerika gesenkt, um sicherzustellen, dass die Preisgestaltung attraktiv bleibt.
- **Für Marketing-Nachrichten:** Die Tarife werden in Mexiko gesenkt, um sicherzustellen, dass die Preisgestaltung weiterhin die Akzeptanz fördert und ein gesundes Messaging-Ökosystem unterstützt.

| Land und Nachrichtentyp | Änderung in % |
| --- | --- |
| Argentinien – Authentifizierung                | -10,04 %  |
| Argentinien – Utility                       | -10,04 %  |
| Ägypten – Authentifizierung                    | -30,43 %  |
| Ägypten – Authentifizierung – International    | -0,58 %   |
| Ägypten – Utility                           | -30,43 %  |
| Mexiko – Marketing                        | -30,08 %  |
| Nordamerika – Authentifizierung            | -70,39 %  |
| Saudi-Arabien – Authentifizierung             | -6,89 %   |
| Saudi-Arabien – Utility                    | -6,89 %   |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Zusätzliche WhatsApp-Preisänderungen im Juli 2025 {#additional-whatsapp-pricing-changes-in-july-2025}
*Zuletzt aktualisiert am 12. Juni 2025*

Zusätzlich zu den zuvor angekündigten Preisaktualisierungen im Juli führt Meta einige weitere Änderungen ein, die ebenfalls am 1. Juli 2025 in Kraft treten.

Hier eine kurze Zusammenfassung der zuvor angekündigten Änderungen:
- Die WhatsApp-Preisgestaltung wechselt von einem „Pro-Konversation“-Modell zu einem „Pro-Nachricht“-Modell. **Die „Pro-Nachricht“-Tarife entsprechen den aktuellen „Pro-Konversation“-Tarifen.**
- Utility-Templates, die als Antwort auf Nutzernachrichten gesendet werden (also innerhalb eines offenen [Kundenservice-Fensters](https://developers.facebook.com/docs/whatsapp/cloud-api/guides/send-messages#customer-service-windows)), sind kostenlos.

*Weitere Details zu diesen Änderungen finden Sie im vorherigen Beitrag vom 12. März weiter unten in diesem Artikel.*

Zusätzliche Änderungen zum 1. Juli (von Meta am 15. Mai angekündigt):
- Meta aktualisiert die Utility- und Authentifizierungstarife in mehreren Märkten im Rahmen fortlaufender Bemühungen, die Preisgestaltung mit alternativen Kanälen vergleichbar zu halten.
    - Die Preise für Utility- und Authentifizierungsnachrichten sinken in allen Märkten außer Indonesien. In Indonesien steigen die Utility-Preise, während die Authentifizierungspreise sinken.
- Meta verfeinert die Definition von Utility basierend auf Nutzerengagement und -stimmung und verschiebt dadurch bestimmte Anwendungsfälle in und aus der Utility-Kategorie. Die neue [Definition für Utility-Templates](https://developers.facebook.com/docs/whatsapp/pricing/updates-to-pricing#updates-to-template-category-guidelines) finden Sie bei Meta.

Für die meisten Kund:innen treten diese Änderungen automatisch am 1. Juli in Kraft.

## Bevorstehende WhatsApp-Preisänderungen im Juli 2025 {#upcoming-whatsapp-pricing-changes-in-july-2025}

*Zuletzt aktualisiert am 12. März 2025 (ursprünglich veröffentlicht am 13. Dezember 2024)*

WhatsApp nimmt ab dem 1. Juli 2025 zwei weitere Änderungen an der Preisgestaltung vor. Braze wird die Preise am selben Tag entsprechend anpassen. Nachfolgend finden Sie eine Zusammenfassung der Änderungen und Best Practices, um sich darauf einzustellen.

### Update 1: Die WhatsApp-Preisgestaltung wechselt von einem „Pro-Konversation“-Modell zu einem „Pro-Nachricht“-Modell. {#update-1-whatsapp-pricing-will-shift-to-a-per-message-model-instead-of-a-per-conversation-model}

**Die „Pro-Nachricht“-Tarife entsprechen den aktuellen „Pro-Konversation“-Tarifen.**

#### Warum wird diese Änderung vorgenommen? {#why-are-they-making-this-change}

Meta wechselt zu einem „Pro-Nachricht“-Modell, um Marken die Berechnung des Return-on-Investment (ROI) zu vereinfachen. Diese Änderung erleichtert es Marken außerdem, direkte ROI-Vergleiche mit anderen Kanälen durchzuführen, die pro Nachricht abgerechnet werden.

#### Wie wirkt sich das auf meine aktuelle WhatsApp-Nutzung aus? {#how-will-this-affect-my-current-whatsapp-usage}

- Aktuelle Konversationen, die mit einem Nachrichten-Template im 24-Stunden-Fenster gesendet werden, sind nicht betroffen.
- **Aktuelle Konversationen, die mit zwei oder mehr Nachrichten-Templates _desselben Typs_ im 24-Stunden-Fenster gesendet werden, werden teurer.** Wenn Sie beispielsweise zwei Marketing-Templates im 24-Stunden-Zeitraum senden, verdoppeln sich die Kosten, da pro Nachrichten-Template abgerechnet wird.

| Beispielszenario | Preisgestaltung vor April 2025 | Preisgestaltung nach April 2025 |
| --- | --- | --- |
| Marke sendet ein Marketing-Template im 24-Stunden-Fenster | Abrechnung für eine Marketing-Konversation | Abrechnung für eine Marketing-Nachricht |
| Marke sendet zwei Marketing-Templates im 24-Stunden-Fenster | Abrechnung für eine Marketing-Konversation | Abrechnung für zwei Marketing-Nachrichten |
| Marke sendet ein Utility-Template im 24-Stunden-Fenster | Abrechnung für eine Utility-Konversation | Abrechnung für eine Utility-Nachricht |
| Marke sendet zwei Utility-Templates im 24-Stunden-Fenster | Abrechnung für eine Utility-Konversation | Abrechnung für zwei Utility-Nachrichten |
| Marke sendet ein Marketing-Template und ein Utility-Template im 24-Stunden-Fenster | Abrechnung für eine Marketing-Konversation und eine Utility-Konversation | Abrechnung für eine Marketing-Nachricht und eine Utility-Nachricht |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

Dieses Update gilt für Marketing-, Utility- und Authentifizierungs-Templates. Service-Konversationen sind seit dem 1. November 2024 kostenlos.

*Hinweis: Dieses Update war ursprünglich für den 1. April, dann den 1. Mai und nun den **1. Juli** geplant.*

### Update 2: Utility-Templates, die während eines 24-Stunden-Kundenservice-Fensters gesendet werden, sind kostenlos. {#update-2-utility-templates-sent-during-a-24-hour-customer-service-window-will-be-free-of-charge}

#### Wie funktioniert das? {#how-does-this-work}

Ein [24-Stunden-Kundenservice-Fenster](https://developers.facebook.com/docs/whatsapp/cloud-api/guides/send-messages#customer-service-windows) wird erstellt, wenn eine Endnutzer:in einer Marke eine Nachricht sendet. Wenn Ihre Marke mit einem Utility-Template antwortet, ist dies kostenlos.

Utility-Templates, die außerhalb eines 24-Stunden-Kundenservice-Fensters gesendet werden (z. B. Utility-Templates, die proaktiv von einer Marke für Kontoerinnerungen und Auftragsstatus-Aktualisierungen gesendet werden), werden weiterhin berechnet.

Wir empfehlen die folgenden Best Practices, um sich auf diese Änderungen einzustellen und Ihr WhatsApp-Marketing-Budget optimal zu nutzen:

- Begrenzen Sie das Senden mehrerer Nachrichten-Templates desselben Typs (ohne Nutzerantwort) im 24-Stunden-Zeitraum. Sie werden nicht mehr berechnet als zuvor unter dem „Pro-Konversation“-Modell. Dies ist auch eine Best Practice, um Ihren Kund:innen qualitativ hochwertige Erlebnisse zu bieten und Nachrichtenmüdigkeit zu vermeiden.
- Verwenden Sie [Antwortnachrichten]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create#response-messages/), wenn Sie auf Nachrichten von Endnutzer:innen antworten. Antwortnachrichten sind kostenlos.

| Beispielszenario | Preisgestaltung vor April 2025 | Preisgestaltung nach April 2025 |
| --- | --- | --- |
| - Marke sendet Marketing-Template <br>- Nutzer:in antwortet <br>- Marke antwortet mit einer Antwortnachricht | Abrechnung für eine Marketing-Konversation | Abrechnung für eine Marketing-Nachricht |
| - Nutzer:in sendet Nachricht an Marke <br>- Marke antwortet mit einer Antwortnachricht | Kostenlos <br> _Klassifiziert als Service-Konversation_ | Kostenlos <br> _Klassifiziert als Service-Konversation_ |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

Wir empfehlen die folgenden Best Practices, um sich auf diese Änderungen einzustellen und Ihr WhatsApp-Marketing-Budget optimal zu nutzen:

- Begrenzen Sie das Senden mehrerer Nachrichten-Templates desselben Typs (ohne Nutzerantwort) im 24-Stunden-Zeitraum. So vermeiden Sie, dass Ihnen mehr berechnet wird als zuvor unter dem „Pro-Konversation“-Modell. Dies ist auch eine Best Practice, um Ihren Kund:innen qualitativ hochwertige Erlebnisse zu bieten und Nachrichtenmüdigkeit zu vermeiden.
- Verwenden Sie [Antwortnachrichten]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create#response-messages), wenn Sie auf Nachrichten von Endnutzer:innen antworten. Antwortnachrichten sind kostenlos.

*Hinweis: Dieses Update war ursprünglich für den 1. April geplant und wurde nun auf den **1. Juli** verschoben.*

## WhatsApp-Preisänderungen von August 2024 bis November 2024 {#whatsapp-pricing-changes-from-august-2024-november-2024}

*Zuletzt aktualisiert am 29. Oktober 2024*

### Utility-Konversationen {#utility-conversations}

Am 1. August 2024 hat Meta die Tarife für Utility-Konversationen gesenkt, um Marken zu ermutigen, mehr geschäftskunden Journeys nach dem Kauf auf der Plattform abzuwickeln. Wir haben diese Kostensenkungen anteilig an Ihre Message-Credits- oder WhatsApp-Credits-Kontingente weitergegeben. Dieses Update trat am selben Tag wie bei Meta in Kraft (1. August).

#### Was sind Utility-Konversationen? {#what-are-utility-conversations}

Utility-Konversationen ermöglichen es Ihnen, auf bestimmte Kundenaktionen oder -anfragen zu reagieren. Beispiele sind Opt-in-Bestätigungen, Bestellaktualisierungen und -bestätigungen, Kontoaktualisierungen oder -benachrichtigungen (z. B. Zahlungserinnerungen) oder Feedback-Umfragen.

#### Wie können Sie von diesem Update profitieren? {#how-can-you-benefit-from-this-update}

Wir empfehlen Ihnen, dieses Update zu nutzen, indem Sie WhatsApp für transaktionsbezogene Nachrichten einsetzen. Sie können auch in Betracht ziehen, einige Ihrer transaktionsbezogenen SMS-Nachrichten auf WhatsApp umzustellen, wenn dies für Ihre Marke sinnvoll ist (basierend auf Ihrer Zielgruppenreichweite und dem Engagement auf jedem Kanal). Dies kann beispielsweise eine gute Option für Kund:innen in Asien, Lateinamerika und Europa sein, wo WhatsApp ein stark genutzter Kanal ist.

### Marketing-Konversationen {#marketing-conversations}

Am 1. Oktober 2024 hat Meta die Preise für Marketing-Konversationen im Vereinigten Königreich um 25 % gesenkt, um die aktuelle Nachfrage widerzuspiegeln. Wir haben diese Kostensenkungen anteilig an Ihre Message-Credits- oder WhatsApp-Credits-Kontingente weitergegeben. Dieses Update trat am selben Tag wie bei Meta in Kraft (1. Oktober).

#### Was sind Marketing-Konversationen? {#what-are-marketing-conversations}

Marketing-Konversationen ermöglichen es Ihnen, eine Vielzahl von Zielen zu erreichen – von der Steigerung der Bekanntheit über die Umsatzförderung bis hin zum Retargeting von Kund:innen. Beispiele sind Ankündigungen neuer Produkte, gezielte Aktionen/Angebote und Kampagnen bei abgebrochenem Einkauf.

### Service-Konversationen {#service-conversations}

Ab dem 1. November 2024 sind alle Service-Konversationen kostenlos. Service-Konversationen verbrauchen keine Message-Credits- oder WhatsApp-Credits-Kontingente mehr. Diese Änderung tritt am selben Tag wie bei Meta in Kraft (1. November).

#### Was sind Service-Konversationen? {#what-are-service-conversations}

Service-Konversationen ermöglichen es Ihnen, auf Kundenanfragen zu reagieren. Dazu gehören Konversationen, die von einer Endnutzer:in gestartet werden und bei denen die Marke mit einer [Antwortnachricht]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create#response-messages) statt mit einem Template antwortet.

#### Wie können Sie von diesem Update profitieren?

Einige Konversationen, die zuvor als „Service“ berechnet wurden, sind jetzt kostenlos. Dazu gehören:

- [Kampagnen für nicht erkannte Antworten]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create#response-messages), bei denen eine Endnutzer:in eine nicht erkannte Nachricht sendet und die Marke mit einer generischen Nachricht über [Antwortnachrichten]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create#response-messages) antwortet. Beispiel: Eine Endnutzer:in sendet eine Nachricht ohne Schlüsselwort und die Marke antwortet mit „Wir können Ihre Nachricht nicht zuordnen. Bitte wenden Sie sich an den Kundensupport.“
- Konversationen, die beginnen, wenn eine Endnutzer:in der Marke ein beworbenes Schlüsselwort sendet und die Marke mit einer [Antwortnachricht]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create#response-messages) antwortet. Häufige Beispiele sind das Opt-in für WhatsApp-Nachrichten oder die Teilnahme an einer bestimmten Aktion.

<br>

Detaillierte Informationen zur Senkung der Utility-Konversationstarife:

| Abrechnungsregion                             | Utility-Senkung in Prozent |
|--------------------------------------------|--------------------------|
| Argentinien                                  | 16,7 %                    |
| Brasilien                                     | 77,1 %                    |
| Chile                                      | 65,9 %                    |
| Kolumbien                                   | 97,6 %                    |
| Ägypten                                      | 92,4 %                    |
| Frankreich                                     | 60,9 %                    |
| Deutschland                                    | 35,5 %                    |
| Indien                                       | 66,7 %                    |
| Indonesien                                  | 0,0 %                     |
| Israel                                     | 71,8 %                    |
| Italien                                      | 28,6 %                    |
| Malaysia                                   | 30,0 %                    |
| Mexiko                                     | 62,4 %                    |
| Niederlande                                | 37,5 %                    |
| Nigeria                                    | 79,0 %                    |
| Nordamerika                              | 73,3 %                    |
| Sonstige                                      | 77,2 %                    |
| Pakistan                                   | 78,7 %                    |
| Peru                                       | 52,3 %                    |
| Übriges Afrika                             | 61,9 %                    |
| Übriger asiatisch-pazifischer Raum                       | 66,7 %                    |
| Übriges Mittel- und Osteuropa          | 43,0 %                    |
| Übriges Lateinamerika                      | 77,1 %                    |
| Übriger Naher Osten                        | 20,7 %                    |
| Übriges Westeuropa                     | 28,6 %                    |
| Russland                                     | 16,1 %                    |
| Saudi-Arabien                               | 54,4 %                    |
| Südafrika                               | 62,0 %                    |
| Spanien                                      | 47,4 %                    |
| Türkei                                     | 43,0 %                    |
| Vereinigte Arabische Emirate                       | 20,7 %                    |
| Vereinigtes Königreich                             | 44,7 %                    |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Um besser zu verstehen, wie Sie von diesen Änderungen profitieren können, wenden Sie sich an Ihren geschäftskunden-Success-Manager.