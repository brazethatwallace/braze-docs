---
nav_title: Meta-Ressourcen
article_title: Meta-Ressourcen
page_order: 6
description: "Dieser Artikel bietet hilfreiche Meta-Dokumentation, Informationen und Ressourcen, um Ihr Verständnis der WhatsApp-Integration zu verbessern."
alias: /meta_resources/
page_type: reference
channel:
  - WhatsApp

---

# Meta-Ressourcen {#meta-resources}

> Diese Seite bietet hilfreiche Meta-Dokumentation, Produktupdates und häufig gestellte Fragen, um Ihr Verständnis der WhatsApp-Integration mit Braze zu verbessern.

## Meta-Dokumentation {#meta-documentation}

Lesen Sie die folgende Meta-Dokumentation für Hinweise zu Anzeigenamen, Telefonnummern und mehr.

- [Hinweise zu Anzeigenamen](https://www.facebook.com/business/help/757569725593362)
- [Meta Insights aktivieren](https://www.facebook.com/business/help/218116047387456)
- [Anforderungen an Telefonnummern](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers)
- [Nachrichtenlimits](https://developers.facebook.com/docs/whatsapp/messaging-limits)
- [Qualitätsbewertung](https://www.facebook.com/business/help/896873687365001)

## WhatsApp-Produktupdates {#whatsapp-product-updates}

### 2026: Geschäftliche Nutzernamen {#2026-business-usernames}
*Zuletzt aktualisiert: Mai 2026*

Meta führt geschäftliche Nutzernamen für WhatsApp ein – einen optionalen Anzeigenamen, den Unternehmen für ihre WhatsApp-Telefonnummer übernehmen können. Wenn ein Nutzername festgelegt ist, erscheint er in den Chat-Fenstern der WhatsApp- und WhatsApp-Business-App anstelle der Telefonnummer. Beachten Sie, dass die Übernahme eines Nutzernamens Ihre Telefonnummer nicht verbirgt; sie bleibt immer in Ihrem Unternehmensprofil sichtbar.

Nutzernamen sind über alle WhatsApp-Telefonnummern hinweg eindeutig – keine zwei Nummern, weder von Verbraucher:innen noch von Unternehmen, können denselben Nutzernamen teilen. Für die Eindeutigkeit wird nicht zwischen Groß- und Kleinschreibung unterschieden, aber Punkte und Unterstriche werden als unterschiedliche Zeichen behandelt. Zum Beispiel sind `myid`, `my.id` und `my_id` alle unterschiedliche Nutzernamen, während `myID` und `myid` als identisch behandelt werden.

Geschäftliche Nutzernamen müssen die folgenden Formatanforderungen erfüllen:

- Enthält nur englische Buchstaben (a–z), Ziffern (0–9), Punkte (`.`) oder Unterstriche (`_`)
- Ist zwischen 3 und 35 Zeichen lang
- Enthält mindestens einen englischen Buchstaben
- Beginnt oder endet nicht mit einem Punkt und enthält keine zwei aufeinanderfolgenden Punkte
- Beginnt nicht mit `www`
- Endet nicht mit einem gängigen Domain-Suffix (wie `.com`, `.org` oder `.net`)

#### Einen reservierten Nutzernamen beanspruchen {#claiming-a-reserved-username}

Bevor die Nutzernamen-Funktion allgemein verfügbar ist, hat Meta möglicherweise einen Nutzernamen für Ihr Unternehmen vorab reserviert – typischerweise passend zu einem bestehenden Facebook-Seiten- oder Instagram-Nutzernamen. Sie können diesen reservierten Nutzernamen beanspruchen oder einen anderen über [WhatsApp Manage](https://business.facebook.com/wa/manage/) wählen. Beanspruchte Nutzernamen werden erst aktiviert, wenn Meta die Funktion verfügbar macht.

Wenn der reservierte Nutzername mit einem bereits mit Ihrer Facebook-Seite oder Ihrem Instagram-Konto verknüpften übereinstimmt, müssen Sie zunächst Ihre geschäftliche Telefonnummer mit dieser Seite oder diesem Konto verknüpfen. Sie können dies beim Beanspruchen des Nutzernamens im WhatsApp Manager oder in der Meta Business Suite tun, oder indem Sie Ihre Telefonnummer direkt von der entsprechenden Seite oder dem Konto hinzufügen. Die Verknüpfung erfordert entweder die vollständige Kontrolle über die Seite oder das Konto oder einen grundlegenden Teilzugriff mit der Berechtigung `manage_phone`.

#### Anzeige-Priorität in Chat-Fenstern {#display-priority-in-chat-windows}

Wenn Ihr Unternehmensprofil in einem Chat-Fenster erscheint, verwendet WhatsApp die folgende Prioritätsreihenfolge (von höchster zu niedrigster):

1. Gespeicherter Kontaktname
2. Verifizierter Unternehmensname oder Official Business Account (OBA)-Name
3. Nutzername
4. Telefonnummer

Weitere Informationen finden Sie in Metas Dokumentation zu [geschäftlichen Nutzernamen](https://developers.facebook.com/documentation/business-messaging/whatsapp/business-scoped-user-ids/#business-usernames).

### April 2026: Automatische Archivierung inaktiver Templates {#april-2026-automatic-archival-of-inactive-templates}
*Zuletzt aktualisiert: April 2026*

- Meta archiviert automatisch Templates, die seit 12 Monaten oder länger inaktiv sind.
- Die automatische Archivierung ist für alle WhatsApp-Geschäftskonten aktiviert und kann nicht deaktiviert werden.
- Template-Aktivität umfasst das Erstellen, Bearbeiten, Senden, Einlegen eines Einspruchs oder Dearchivieren eines Templates.
- Archivierte Templates können nicht gesendet werden und sind nach 28 Tagen zur endgültigen Löschung vorgesehen.
- Sie können Templates innerhalb des 28-Tage-Fensters dearchivieren, um sie wiederherzustellen und die geplante Löschung abzubrechen.
- Benachrichtigungen werden über den `message_template_status_update`-Webhook, per E-Mail und über ein einmaliges WhatsApp-Manager-Banner gesendet.

Weitere Informationen finden Sie in Metas Dokumentation zur [Template-Archivierung](https://developers.facebook.com/documentation/business-messaging/whatsapp/templates/template-archival).

### Juni 2026: Geschäftsbezogene Nutzer-IDs {#june-2026-business-scoped-user-ids}
*Zuletzt aktualisiert: März 2026*

- Meta führt Nutzer-IDs ein, um die Weitergabe von Telefonnummern aus Datenschutzgründen zu ersetzen
- Braze arbeitet vor dem Rollout an einer Lösung
- Erwarteter Rollout von Meta im Juni 2026

### November 2025: [Marketing Messages API für WhatsApp](https://developers.facebook.com/documentation/business-messaging/whatsapp/marketing-messages/overview/) (ehemals Marketing Messages Lite API) {#november-2025-marketing-messages-api-for-whatsapphttpsdevelopersfacebookcomdocumentationbusiness-messagingwhatsappmarketing-messagesoverview-formerly-marketing-messages-lite-api}
*Zuletzt aktualisiert: März 2026*

- Ersetzt statische Cloud-API-Limits durch dynamische, Engagement-basierte Limits
- Nicht verfügbar in EMEA, Japan oder Südkorea für optimierte Zustellung
- Utility-/Authentifizierungsnachrichten laufen automatisch weiter über die Cloud API

### Oktober 2025: Genehmigungsprozess für Official Business Account (OBA) geändert {#october-2025-official-business-account-oba-approval-process-changed}
*Zuletzt aktualisiert: März 2026*

- Zuvor für alle Kund:innen über den WhatsApp Manager zugänglich
- Jetzt beschränkt auf: Regierungen/große Meta-Werbetreibende, Direktwerbetreibende oder über einen BSP wie Braze (bis zu 5 pro Woche)
- Neue Voraussetzungen: Unternehmensverifizierung, Zwei-Faktor-Verifizierung, genehmigter Anzeigename, Bekanntheit
- Wenden Sie sich an Ihren Customer-Success-Manager für Unterstützung

### Oktober 2025: Regionale Preissenkungen {#october-2025-regional-pricing-rate-cuts}
*Zuletzt aktualisiert: März 2026*

- Niedrigere Utility-/Authentifizierungsraten in Argentinien, Ägypten, Mexiko, Nordamerika
- Niedrigere Marketing-Raten in Mexiko (gültig ab 1. Oktober 2025)

### Oktober 2025: Nachrichtenlimits ändern sich von pro Telefonnummer zu pro Unternehmensportfolio {#october-2025-messaging-limits-change-from-per-phone-to-per-business-portfolio}
*Zuletzt aktualisiert: März 2026*

- Limits werden jetzt über alle Telefonnummern in einem Portfolio geteilt
- Portfolios übernehmen das höchste bestehende Limit
- Schnellerer Zugang zu höheren Limits (innerhalb von 6 Stunden)
- Risiko: Unternehmen ohne eine „unbegrenzte“ Nummer können einen Rückgang der aggregierten Limits erleben

### 1. Juli 2025: Preisumstellung {#july-1-2025-pricing-overhaul}
*Zuletzt aktualisiert: März 2026*

- Pro-Nachricht-Abrechnung ersetzt Pro-Konversation-Abrechnung
- Utility-Nachrichten, die innerhalb eines 24-Stunden-Servicefensters gesendet werden, wurden kostenlos
- Aktualisierte Utility-/Authentifizierungsraten in mehreren Märkten mit neuen Volumenstufen
- Neue Regeln zur Fehlkategorisierung von Utility-Templates – Unternehmen können mit Template-Ablehnung und Einreichungsbeschränkungen rechnen

### April 2025: Pausierung von Marketing-Nachrichten an US-Telefonnummern {#april-2025-pause-of-marketing-messages-to-us-phone-numbers}
*Zuletzt aktualisiert: August 2025*

Meta wird die Zustellung aller Marketing-Template-Nachrichten an WhatsApp-Nutzer:innen mit einer US-Telefonnummer (eine Nummer bestehend aus der Vorwahl `+1` und einer US-Ortsvorwahl) pausieren. Es gibt derzeit kein geplantes Datum, wann diese Pausierung aufgehoben wird.

Jeder Versuch, ein Template an eine:n WhatsApp-Nutzer:in mit einer US-Telefonnummer zu senden, führt zum Fehler `131049`.

### März 2025: Einschränkungen bei Fehlkategorisierung von Templates {#march-2025-template-category-misuse-restrictions}
*Zuletzt aktualisiert: März 2026*

- Meta hat Durchsetzungsmaßnahmen für Unternehmen eingeführt, die die Utility-/Marketing-Kategorisierung missbrauchen
- Kann zu 7–30-tägigen Einschränkungen bei der Template-Erstellung und Kategorieüberprüfungen führen

### März 2025: Pro-Nutzer:in-Limits für Marketing-Template-Nachrichten {#march-2025-per-user-marketing-template-message-limits}
*Zuletzt aktualisiert: August 2025*

Meta wird die Anzahl der Marketing-Template-Nachrichten begrenzen, die ein:e Nutzer:in von allen Unternehmen in einem bestimmten Zeitraum erhalten kann, beginnend mit Nachrichten, die weniger wahrscheinlich gelesen werden.

Eine Ausnahme ist: Wenn eine Person auf eine Marketing-Nachricht antwortet, wird ein 24-Stunden-Kundenservice-Fenster gestartet. Marketing-Nachrichten, die innerhalb dieses Fensters gesendet werden, zählen nicht zum Limit der Person.

Das spezifische Limit variiert je nach Nutzer:in, abhängig von deren Engagement-Level. Erfahren Sie mehr über WhatsApps Pro-Nutzer:in-Limits für Marketing-Template-Nachrichten [hier](https://developers.facebook.com/docs/whatsapp/cloud-api/guides/send-message-templates#per-user-marketing-template-message-limits).

### Januar 2025: WhatsApp pausiert den Versand von Marketing-Nachrichten an US-Nutzer:innen ab dem 1. April {#january-2025-whatsapp-pausing-marketing-message-sending-to-us-users-starting-april-1}
*Zuletzt aktualisiert: Januar 2025*

WhatsApp wird den Versand von Marketing-Nachrichten an US-Nutzer:innen (Personen mit US-Telefonnummern) ab dem 1. April 2025 pausieren. [Utility-, Service- und Authentifizierungsnachrichten](https://developers.facebook.com/docs/whatsapp/pricing/) sowie [Antwortnachrichten]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message/#response-messages) sind in den USA weiterhin erlaubt.

Der Versand von Marketing-Nachrichten (sowie allen anderen Nachrichtentypen) in alle anderen Länder oder Regionen ist weiterhin erlaubt und wird nicht beeinträchtigt.

Meta hat uns mitgeteilt, dass sie dieses Update durchführen, um die Gesundheit des WhatsApp-Ökosystems in den USA zu erhalten, wo WhatsApp schnell wächst, sich aber noch in einem früheren Stadium befindet (zum Beispiel haben Marketing-Nachrichten ein geringeres Engagement als in anderen Regionen). Sie werden weiterhin evaluieren, wann der US-Markt bereit ist, Marketing-Nachrichten wieder aufzunehmen.

Die Zustellung von Marketing-Nachrichten an Telefonnummern mit US-Ortsvorwahlen wird von WhatsApp abgelehnt und gibt den Fehlercode 131049 zurück.

### November 2024: Änderungen der WhatsApp-Opt-in-Richtlinie {#november-2024-changes-to-whatsapp-opt-in-policy}
*Zuletzt aktualisiert: Januar 2025*

Meta hat kürzlich seine [Opt-in-Richtlinie](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/) aktualisiert. Anstatt eine kanalspezifische Einwilligung zu verlangen, können Unternehmen Nutzer:innen jetzt auf der Plattform kontaktieren, wenn:

1. Die Person ihre Telefonnummer angegeben hat.
2. Die Person eine Opt-in-Genehmigung für allgemeines Messaging erteilt hat, nicht nur für WhatsApp.

Unternehmen müssen weiterhin alle lokalen Gesetze einhalten und die folgenden Anforderungen beim Einholen des Opt-ins beachten:

- Unternehmen müssen klar angeben, dass eine Person dem Erhalt von Kommunikation vom Unternehmen zustimmt
- Unternehmen müssen klar den Unternehmensnamen angeben, von dem eine Person Nachrichten erhalten wird
- Unternehmen müssen geltendes Recht einhalten

Obwohl WhatsApp seine Richtlinie gelockert hat, empfiehlt Braze weiterhin, ein spezifisches Opt-in für den WhatsApp-Kanal einzuholen, um das beste Kundenerlebnis und die besten Engagement-Raten zu fördern. Wie immer sollten Sie sich mit Ihrem Rechtsteam beraten, was für Ihre Marke sinnvoll ist.

### November 2024: Updates zum Pro-Nutzer:in-Limit für Marketing-Templates für Personen in den USA vor der Feiertagssaison {#november-2024-updates-to-the-per-user-marketing-template-limit-for-people-in-the-us-ahead-of-the-holiday-season}
*Zuletzt aktualisiert: Dezember 2024*

Seit Meta das Pro-Nutzer:in-Limit für Marketing-Templates eingeführt hat, hat Meta signifikante Verbesserungen bei den Leseraten und der Nutzerstimmung festgestellt.

Ab sofort, vor der Feiertagssaison, werden Personen in den USA weniger neue Marketing-Konversationen erhalten. Meta erwartet, dass diese Änderung engagiertere Zielgruppen schafft, was letztendlich zu besseren Ergebnissen für Unternehmen führt. Dies kann zu niedrigeren Zustellraten für Ihr Unternehmen führen, wenn Sie Marketing-Nachrichten an US-Telefonnummern senden, was mit dem Fehlercode `131049` über Braze-Currents und das Nachrichten-Aktivitätsprotokoll überwacht werden kann.

Unternehmen in den USA können weiterhin Marketing-Nachrichten in andere Regionen zustellen, und es gibt keine Auswirkungen auf Utility-, Authentifizierungs- oder Servicenachrichten oder Marketing-Template-Nachrichten, die innerhalb eines von Nutzer:innen initiierten Konversationsfensters gesendet werden (zum Beispiel eine Click-to-WhatsApp-Anzeige oder ein Produktkarussell- oder Coupon-Template, das als Teil einer Konversation gesendet wird).

### November 2024: WhatsApp erweitert qualitätsbasierte Kontodurchsetzungen um Leseraten {#november-2024-whatsapp-expanding-quality-based-account-enforcements-to-include-read-rates}
*Zuletzt aktualisiert: Dezember 2024*

WhatsApp investiert kontinuierlich in neue Wege, um Unternehmen dabei zu helfen, qualitativ hochwertige Erlebnisse für ihre Kund:innen zu schaffen, wie zum Beispiel die Reduzierung von Spam-ähnlichem Verhalten auf ihrer Plattform.

Am 22. November begann WhatsApp, seine bestehenden Qualitätsdurchsetzungen auf Kontoebene für WhatsApp-Geschäftskonten (WABAs) mit extrem niedrigen Leseraten zu erweitern. Diese Änderung wird weltweit ausgerollt.

Wenn die Leserate eines Kontos signifikant sinkt (zum Beispiel die Mehrheit der vom Konto gesendeten Nachrichten ungelesen bleibt), werden Nachrichtenblockierungen für das Konto durchgesetzt. Die Schwere der Blockierung nimmt zu, wenn dauerhaft niedrige Leseraten in großem Umfang vorliegen.

Wenn die Leserate des Kontos extrem niedrig ist, werden die folgenden Maßnahmen ergriffen:

- Das Konto wird daran gehindert, geschäftsinitiierte Nachrichten zu senden. Es kann weiterhin auf von Kund:innen initiierte Nachrichten antworten. Diese anfängliche Blockierung ist eine „Soft-Sperre“ und kann durch Auswahl des Bestätigungsbuttons in der Kontoqualität aufgehoben werden, um wieder Nachrichten senden zu können.
- Wenn die Leserate nach der Soft-Sperre weiter sinkt oder niedrig bleibt, können Unternehmen mit einer schrittweisen Verschärfung der Durchsetzungsmaßnahmen rechnen (zum Beispiel einige Tage Nachrichtenbeschränkungen).
- Unternehmen müssen warten, bis das durchgesetzte Limit abläuft, um wieder Nachrichten senden zu können. Wenn die Leserate nach wiederholten Soft-Sperren weiterhin niedrig bleibt, wird das Konto schließlich deaktiviert.

#### So bleiben Sie über diese Warnungen und Durchsetzungen informiert {#how-to-stay-updated-on-these-warnings-and-enforcements}

Ähnlich wie bei bestehenden Plattformdurchsetzungen werden Unternehmen über diese Maßnahmen benachrichtigt und können sie über die Seite „Kontoqualität“ im WhatsApp Business Manager bestätigen. Stellen Sie sicher, dass Sie die korrekten Kontaktdaten im WhatsApp Business Manager für alle erforderlichen Administrator:innen hinterlegt haben, da die Benachrichtigungs-E-Mails zur Durchsetzung auf Basis dieser Informationen versendet werden.

Benachrichtigungen über schwere Spam-Verstöße werden:

- Im Benachrichtigungscenter des WhatsApp Business Managers angezeigt
- Als Banner im WhatsApp Manager angezeigt
- Per E-Mail an alle im WhatsApp Business Manager eingerichteten Administrator:innen gesendet

### Mai 2024: Cloud API geht in der Türkei live {#may-2024-cloud-api-going-live-in-trkiye}
*Zuletzt aktualisiert: Mai 2024*

Meta bietet Cloud-API-Unternehmen jetzt Zugang zur Türkei für geschäftliches Messaging. Zuvor war die WhatsApp Cloud API für Unternehmen in der Türkei nutzbar, aber WhatsApp-Nutzer:innen mit türkischen Nummern konnten keine Nachrichten senden oder empfangen, die über die Cloud API gesendet wurden.

Meta macht es Nutzer:innen immer deutlich, wenn sie mit einem von Meta gehosteten Unternehmen chatten, und alle Nutzer:innen müssen die relevanten WhatsApp-Nutzungsbedingungen und die Datenschutzrichtlinie akzeptieren, um mit dem geschäftlichen Messaging fortzufahren. Das Update der Nutzungsbedingungen und Datenschutzrichtlinie von 2021 in der Türkei war pausiert worden, wird aber jetzt ausgerollt. Es ändert nichts an Metas Engagement für den Datenschutz – persönliche Gespräche werden weiterhin durch Ende-zu-Ende-Verschlüsselung geschützt, was bedeutet, dass nur Sie und die beabsichtigte Empfängerin bzw. der beabsichtigte Empfänger sie sehen können. Das Update ermöglicht es türkischen Nutzer:innen, auf optionale Geschäftsfunktionen zuzugreifen, wenn sie dies wünschen, und bietet mehr Transparenz darüber, wie WhatsApp funktioniert.

Cloud-API-Unternehmen können jetzt Konversationen mit WhatsApp-Nutzer:innen mit türkischen Nummern initiieren, die nun einen Webhook als „gesendet“-Konversation zurückgeben, anstatt des bisherigen Fehlercodes 131026.

Damit eine Geschäftsnachricht als „zugestellt“ oder „gelesen“ gilt, muss die:der Nutzer:in die WhatsApp-Bedingungen akzeptieren. Einem Unternehmen wird nur dann eine Gebühr berechnet, wenn die Nachricht zugestellt wird.

Nutzer:innen, die eine Nachricht von einem Cloud-API-Unternehmen erhalten oder versuchen, eine zu senden, wird eine In-App-Benachrichtigung über das Bedingungsupdate angezeigt, die deutlich macht, dass sie einem Cloud-API-Unternehmen erst dann Nachrichten senden können, wenn sie das WhatsApp-Update akzeptiert haben. Darüber hinaus werden Nutzer:innen, die die App auf ihrem Telefon registrieren oder erneut registrieren, aufgefordert, das WhatsApp-Update zu akzeptieren.

Wenn ein:e Nutzer:in das Update akzeptiert, wird die bestehende Cloud-API-Systemnachricht angezeigt, wenn sie mit einem Cloud-API-Unternehmen chatten.

### Mai 2024: Pro-Nutzer:in-Limits für Marketing-Template-Nachrichten {#may-2024-per-user-marketing-template-message-limits}
*Zuletzt aktualisiert: Mai 2024*

Meta führt neue Ansätze ein, um qualitativ hochwertige Nutzererlebnisse aufrechtzuerhalten und das Engagement mit Marketing-Template-Nachrichten auf der WhatsApp-Plattform zu maximieren. Ab dem 23. Mai 2024 wird die Anzahl der Marketing-Template-Nachrichten begrenzt, die jede:r einzelne Nutzer:in von allen Unternehmen, mit denen sie interagieren, in einem bestimmten Zeitraum erhalten kann, beginnend mit einer kleinen Anzahl von Konversationen, die weniger wahrscheinlich gelesen werden. Beachten Sie, dass das Limit auf der Anzahl der Marketing-Template-Nachrichten basiert, die diese Person bereits von einem beliebigen Unternehmen erhalten hat, und nicht speziell mit Ihrer Marke zusammenhängt. Dies kann jedoch die Zustellbarkeit Ihrer Marketing-Template-Nachrichten beeinflussen.

Das Limit gilt nur für Marketing-Template-Nachrichten, die normalerweise eine neue Marketing-Konversation eröffnen würden. Wenn bereits eine Marketing-Konversation zwischen Ihrer Marke und einem:einer WhatsApp-Nutzer:in offen ist, werden Marketing-Template-Nachrichten, die an die:den Nutzer:in gesendet werden, nicht beeinträchtigt.

Wenn eine Marketing-Template-Nachricht aufgrund des Limits nicht an eine:n bestimmte:n Nutzer:in zugestellt wird, gibt die Cloud API den Fehlercode 131026 zurück. Beachten Sie jedoch, dass diese Fehlercodes eine Vielzahl von Problemen abdecken, die zur Nichtzustellung einer Nachricht führen können, und Meta aus Datenschutzgründen nicht offenlegen wird, ob die Nachricht tatsächlich aufgrund des Limits nicht zugestellt wurde. Weitere Informationen finden Sie im [Fehlerbehebungsdokument](https://developers.facebook.com/docs/whatsapp/cloud-api/support#troubleshooting) der Cloud API für Beschreibungen der Nichtzustellungsgründe und was Sie tun können, um deren zugrunde liegende Ursache zu ermitteln.

Wenn Sie einen dieser Fehlercodes erhalten und vermuten, dass er auf das Limit zurückzuführen ist, vermeiden Sie es, die Template-Nachricht sofort erneut zu senden, da dies nur zu einer weiteren Fehlerantwort führt.

Weitere Informationen zu diesem Zustellbarkeitsupdate, einschließlich Details zur Überwachung Ihrer Zustellbarkeit und anderer Best Practices für Marketing-Messaging auf WhatsApp, finden Sie in unserem aktuellen [Blogbeitrag](https://www.braze.com/resources/articles/meta-introduces-deliverability-updates-for-whatsapp?utm_campaign=fy25-q2-global-customer-customer-meta-deliverability-updates-for-whatsapp&utm_medium=email-cdb&utm_source=braze&utm_content=blog-meta-deliverability-updates-for-wa-blog).

### April 2024: Template-Pacing für Utility-Templates {#april-2024-template-pacing-for-utility-templates}
*Zuletzt aktualisiert: April 2024*

Letztes Jahr hat WhatsApp Template-Pacing für Marketing-Nachrichten als neue Methode eingeführt, um Unternehmen dabei zu helfen, das Engagement ihrer Templates zu verbessern und wertvolle Nutzererlebnisse zu schaffen. Ab dem 30. April wird Template-Pacing auf Utility-Nachrichten ausgeweitet. Wenn ein Utility-Template für ein Konto aufgrund von Nutzerfeedback pausiert wird, werden die neuen Utility-Templates, die in den nächsten sieben Tagen erstellt werden, gedrosselt.

### April 2024: Leseraten beeinflussen die Qualitätsbewertung für Marketing-Templates {#april-2024-read-rates-will-affect-quality-rating-for-marketing-templates}
*Zuletzt aktualisiert: März 2024*

WhatsApp testet neue Ansätze, beginnend mit Verbraucher:innen in Indien, um wertvollere Erlebnisse zu schaffen und das Engagement mit den Marketing-Konversationen von Unternehmen zu maximieren. Dies kann die Begrenzung der Anzahl von Marketing-Konversationen umfassen, die eine Person von einem beliebigen Unternehmen in einem bestimmten Zeitraum erhält, beginnend mit einer kleinen Anzahl von Konversationen, die weniger wahrscheinlich gelesen werden. Braze erhält einen Fehlercode, wenn eine Nachricht nicht zugestellt wird.

WhatsApp wird beginnen, Leseraten als Teil der Qualitätsbewertung für Marketing-Templates zu berücksichtigen, neben traditionellen Metriken wie Blockierungen und Meldungen. WhatsApp kann Marketing-Campaigns mit niedrigen Leseraten vorübergehend pausieren, um Unternehmen Zeit zu geben, die Templates mit dem geringsten Engagement zu überarbeiten, bevor das Volumen ab dem 1. April 2024 skaliert wird.

### Februar 2024: Experiment mit Marketing-Konversationen {#february-2024-marketing-conversations-experimentation}
*Zuletzt aktualisiert: Februar 2024*

Ab dem 6. Februar 2024 testet WhatsApp neue Ansätze, beginnend mit Verbraucher:innen in Indien, um wertvollere Erlebnisse zu schaffen und das Customer-Engagement mit den Marketing-Konversationen Ihrer Marke zu maximieren. Dies kann die Begrenzung der Anzahl von Marketing-Konversationen umfassen, die ein:e Nutzer:in von Ihrer Marke in einem bestimmten Zeitraum erhält, beginnend mit einer kleinen Anzahl von Konversationen, die weniger wahrscheinlich gelesen werden.

### Oktober 2023: Template-Pacing {#october-2023-template-pacing}
*Zuletzt aktualisiert: Oktober 2023*

Ab dem 12. Oktober 2023 führt WhatsApp ein Konzept namens „Template-Pacing“ für Marketing-Nachrichten ein. Anstatt Ihre Nachricht gleichzeitig an Ihre gesamte Campaign-Zielgruppe zu senden, liefert „Template-Pacing“ die Nachricht zunächst an eine kleinere Teilmenge von Nutzer:innen, um Echtzeit-Feedback von Campaign-Empfänger:innen zu sammeln, bevor die verbleibenden Nachrichten gesendet werden.

Das „Pace-Limit“ (die anfängliche Teilmenge der gesendeten Nachrichten) ist variabel und hängt vom Template ab. Nach dem ersten Versand hält WhatsApp die verbleibenden Nachrichten für maximal 30 Minuten zurück. Während dieser Halteperiode wird die Qualität des Templates basierend auf Kundenfeedback bewertet. Wenn das Feedback positiv ist und auf ein qualitativ hochwertiges Template hinweist, werden die verbleibenden Nachrichten zugestellt. Wenn das Feedback negativ ist, werden die verbleibenden nicht zugestellten Nachrichten verworfen, um weiteres negatives Feedback von einem größeren Teil Ihrer Kund:innen zu verhindern und Ihnen zu helfen, potenzielle Probleme mit der Qualitätsdurchsetzung zu vermeiden (wie Auswirkungen auf die Qualitätsbewertung der Telefonnummer).

Beachten Sie, dass WhatsApp dasselbe System zur Bewertung der Template-Qualität beim Template-Pacing verwendet wie bei der Template-Pausierung. Nachrichten, die während des Template-Pacings nicht zugestellt werden (aufgrund von Templates mit niedriger Qualität), sind dieselben, die in größerem Umfang pausiert worden wären.

Letztendlich bietet Ihnen dieses Update eine schnellere Feedback-Schleife (30 Minuten statt Stunden oder Tagen bei der Template-Pausierung), sodass Sie Ihre Templates anpassen und ein besseres Kundenerlebnis bieten können.

**Wenn Sie weitere Fragen zu diesem Update haben, wenden Sie sich an Ihre:n Meta-Partnervertreter:in.**

### Juni 2023: Messaging-Experiment {#june-2023-messaging-experimentation}
*Zuletzt aktualisiert: Juni 2023*

Ab dem 14. Juni 2023 führt Meta neue Experimentierverfahren auf der WhatsApp-Plattform ein, um zu bewerten, wie Marketing-Nachrichten das Verbrauchererlebnis und das Engagement beeinflussen. Dieses Experiment kann Ihre Marketing-Nachrichten betreffen, die über die WhatsApp Business API mit Braze gesendet werden.

Meta beabsichtigt, solche Experimente auf der WhatsApp-Plattform fortzusetzen. Weitere Informationen finden Sie in [Metas Dokumentation](https://developers.facebook.com/docs/whatsapp/on-premises/guides/experiments?content_id=86oue5PtwEgcBJl).

**Das WhatsApp-Experiment betrifft nur Marketing-Nachrichten.** Dieses Experiment hat das Potenzial, die Zustellung von Marketing-Template-Nachrichten zu beeinflussen. Utility- und Authentifizierungs-Templates werden weiterhin ohne Auswirkungen durch das Experiment zugestellt.

Im Experiment wählt Meta zufällig etwa 1 % der WhatsApp-Verbraucher:innen als Teilnehmer:innen aus. Wenn sie ausgewählt werden, wird Meta keine Marketing-Nachrichten-Templates an diese Verbraucher:innen zustellen, es sei denn, eine der folgenden Bedingungen trifft zu:

- Wenn ein:e Verbraucher:in Ihnen in den letzten 24 Stunden geantwortet hat;
- Wenn eine bestehende Marketing-Konversation offen ist; oder
- Wenn eine WhatsApp-Anzeige von dem:der Verbraucher:in in den letzten 72 Stunden angeklickt wurde.

## Häufig gestellte Fragen {#faq}

### Wie erfahre ich, ob meine Marketing-Nachricht von Metas Experiment betroffen war? {#how-will-i-know-if-my-marketing-message-was-impacted-by-metas-experiment}

Wenn eine Nachricht aufgrund des Experiments nicht zugestellt wird, wird ein spezifischer Fehlercode im Aktivitätsprotokoll und in Currents angezeigt. Die Nachricht wird auch als Fehler gezählt und in Ihre WhatsApp-Fehlermetriken über alle Berichte im Braze-Dashboard einbezogen. Für diese Nachrichten werden Ihnen keine Kosten berechnet.

Dieser Fehlercode 130472 lautet „User's number is part of an experiment.“ Weitere Informationen zu WhatsApp Cloud API-Fehlercodes finden Sie in [Metas Dokumentation](https://developers.facebook.com/docs/whatsapp/cloud-api/support/error-codes?content_id=8SJRLBEjYGvXO9k).

### Kann ich mich von Metas Experiment abmelden? {#can-i-opt-out-of-metas-experiment}

Nein, Meta erlaubt keine Abmeldung vom Experiment. Alle Anbieter und Nutzer:innen der WhatsApp Business API unterliegen diesem Meta-Experiment.

### Kann ich versuchen, ein Template später erneut zu senden? {#can-i-try-to-resend-a-template-later}

Es gibt keinen festen Zeitrahmen für dieses Experiment. Daher kann ein:e Verbraucher:in weiterhin dem Experiment unterliegen.

### Was kann ich tun, wenn meine Marketing-Nachrichten aufgrund von Metas Experiment nicht zugestellt werden? {#what-can-i-do-if-my-marketing-messages-are-not-delivered-due-to-metas-experiment}

Wir empfehlen, andere Braze-Kanäle wie E-Mail, SMS, Push-Benachrichtigungen oder In-App-Nachrichten zu nutzen, um eine Nachricht mit ähnlichem Inhalt an Ihre beabsichtigten Nutzer:innen zu senden.