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

- [Hinweise zum Anzeigenamen](https://www.facebook.com/business/help/757569725593362)
- [Meta Insights aktivieren](https://www.facebook.com/business/help/218116047387456)
- [Anforderungen an Telefonnummern](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers)
- [Messaging-Limits](https://developers.facebook.com/docs/whatsapp/messaging-limits)
- [Qualitätsbewertung](https://www.facebook.com/business/help/896873687365001)

## WhatsApp-Produktupdates {#whatsapp-product-updates}

### 2026: Geschäftliche Nutzernamen {#2026-business-usernames}
*Zuletzt aktualisiert: Mai 2026*

Meta führt geschäftliche Nutzernamen für WhatsApp ein – einen optionalen Anzeigenamen, den Unternehmen für ihre WhatsApp-Telefonnummer festlegen können. Wenn ein Nutzername eingerichtet ist, erscheint er in WhatsApp und der WhatsApp Business App in Chatfenstern anstelle der Telefonnummer. Beachten Sie, dass die Verwendung eines Nutzernamens Ihre Telefonnummer nicht verbirgt; sie bleibt in Ihrem Unternehmensprofil jederzeit sichtbar.

Nutzernamen sind über alle WhatsApp-Telefonnummern hinweg eindeutig – keine zwei Nummern, ob privat oder geschäftlich, können denselben Nutzernamen haben. Für die Eindeutigkeit wird die Groß-/Kleinschreibung nicht berücksichtigt, aber Punkte und Unterstriche werden als unterschiedliche Zeichen behandelt. Zum Beispiel sind `myid`, `my.id` und `my_id` allesamt verschiedene Nutzernamen, während `myID` und `myid` als identisch behandelt werden.

Geschäftliche Nutzernamen müssen die folgenden Formatanforderungen erfüllen:

- Enthält nur englische Buchstaben (a–z), Ziffern (0–9), Punkte (`.`) oder Unterstriche (`_`)
- Ist zwischen 3 und 35 Zeichen lang
- Enthält mindestens einen englischen Buchstaben
- Beginnt oder endet nicht mit einem Punkt und enthält keine zwei aufeinanderfolgenden Punkte
- Beginnt nicht mit `www`
- Endet nicht mit einem gängigen Domain-Suffix (wie `.com`, `.org` oder `.net`)

#### Einen reservierten Nutzernamen beanspruchen {#claiming-a-reserved-username}

Bevor die Nutzernamen-Funktion allgemein verfügbar ist, hat Meta möglicherweise bereits einen Nutzernamen für Ihr Unternehmen reserviert – in der Regel passend zu einem bestehenden Facebook-Seiten- oder Instagram-Nutzernamen. Sie können diesen reservierten Nutzernamen beanspruchen oder einen anderen über [WhatsApp Manage](https://business.facebook.com/wa/manage/) wählen. Beanspruchte Nutzernamen werden erst aktiviert, wenn Meta die Funktion verfügbar macht.

Wenn der reservierte Nutzername mit einem bereits mit Ihrer Facebook-Seite oder Ihrem Instagram-Konto verknüpften Nutzernamen übereinstimmt, müssen Sie zunächst Ihre geschäftliche Telefonnummer mit dieser Seite oder diesem Konto verknüpfen. Dies können Sie tun, während Sie den Nutzernamen im WhatsApp Manager:in oder der Meta Business Suite beanspruchen, oder indem Sie Ihre Telefonnummer direkt über die entsprechende Seite oder das Konto hinzufügen. Für die Verknüpfung ist entweder die vollständige Kontrolle über die Seite oder das Konto erforderlich, oder ein grundlegender Teilzugriff mit der Berechtigung `manage_phone`.

#### Anzeige-Priorität in Chatfenstern {#display-priority-in-chat-windows}

Wenn Ihr Unternehmensprofil in einem Chatfenster erscheint, verwendet WhatsApp die folgende Prioritätsreihenfolge (von höchster zu niedrigster):

1. Gespeicherter Kontaktname
2. Verifizierter Unternehmensname oder Name des Official Business Account (OBA)
3. Nutzername
4. Telefonnummer

Weitere Informationen finden Sie in der Meta-Dokumentation zu [geschäftlichen Nutzernamen](https://developers.facebook.com/documentation/business-messaging/whatsapp/business-scoped-user-ids/#business-usernames).

### April 2026: Automatische Archivierung inaktiver Templates {#april-2026-automatic-archival-of-inactive-templates}
*Zuletzt aktualisiert: April 2026*

- Meta archiviert automatisch Templates, die seit 12 Monaten oder länger inaktiv sind.
- Die automatische Archivierung ist für alle WhatsApp Business Accounts aktiviert und kann nicht deaktiviert werden.
- Zu den Template-Aktivitäten gehören das Erstellen, Bearbeiten, Senden, Einlegen eines Einspruchs oder Entarchivieren eines Templates.
- Archivierte Templates können nicht gesendet werden und werden nach 28 Tagen zur endgültigen Löschung vorgemerkt.
- Sie können Templates innerhalb des 28-Tage-Fensters entarchivieren, um sie wiederherzustellen und die geplante Löschung abzubrechen.
- Benachrichtigungen werden über den `message_template_status_update`-Webhook, per E-Mail und über ein einmaliges WhatsApp-Manager:in-Banner gesendet.

Weitere Informationen finden Sie in der Meta-Dokumentation zur [Template-Archivierung](https://developers.facebook.com/documentation/business-messaging/whatsapp/templates/template-archival).

### Juni 2026: Geschäftsbezogene Nutzer-IDs {#june-2026-business-scoped-user-ids}
*Zuletzt aktualisiert: März 2026*

- Meta führt Nutzer-IDs ein, um die Weitergabe von Telefonnummern aus Datenschutzgründen zu ersetzen
- Braze arbeitet vor dem Rollout an einer Lösung
- Erwarteter Rollout von Meta im Juni 2026

### November 2025: [Marketing Messages API für WhatsApp](https://developers.facebook.com/documentation/business-messaging/whatsapp/marketing-messages/overview/) (ehemals Marketing Messages Lite API) {#november-2025-marketing-messages-api-for-whatsapp-formerly-marketing-messages-lite-api}
*Zuletzt aktualisiert: März 2026*

- Ersetzt statische Cloud-API-Limits durch dynamische, Engagement-basierte Limits
- Nicht verfügbar in EMEA, Japan oder Südkorea für optimierte Zustellung
- Utility-/Authentifizierungsnachrichten werden automatisch über die Cloud API weitergeführt

### Oktober 2025: Genehmigungsprozess für Official Business Account (OBA) geändert {#october-2025-official-business-account-oba-approval-process-changed}
*Zuletzt aktualisiert: März 2026*

- Zuvor über den WhatsApp Manager:in für alle Kund:innen zugänglich
- Jetzt beschränkt auf: Regierungs-/große Meta-Werbetreibende, direkte Werbetreibende oder über einen BSP wie Braze (bis zu 5 pro Woche)
- Neue Voraussetzungen: Unternehmensverifizierung, Zwei-Stufen-Verifizierung, genehmigter Anzeigename, Bekanntheit
- Wenden Sie sich an Ihren CSM für Unterstützung

### Oktober 2025: Regionale Preissenkungen {#october-2025-regional-pricing-rate-cuts}
*Zuletzt aktualisiert: März 2026*

- Niedrigere Utility-/Authentifizierungsraten in Argentinien, Ägypten, Mexiko, Nordamerika
- Niedrigere Marketing-Raten in Mexiko (gültig ab 1. Oktober 2025)

### Oktober 2025: Messaging-Limits ändern sich von pro Telefonnummer zu pro Unternehmensportfolio {#october-2025-messaging-limits-change-from-per-phone-to-per-business-portfolio}
*Zuletzt aktualisiert: März 2026*

- Limits werden jetzt über alle Telefonnummern in einem Portfolio geteilt
- Portfolios übernehmen das höchste bestehende Limit
- Schnellerer Zugang zu höheren Limits (innerhalb von 6 Stunden)
- Risiko: Unternehmen ohne eine „unbegrenzte“ Nummer können eine Verringerung der aggregierten Limits feststellen

### 1. Juli 2025: Preisumstellung {#july-1-2025-pricing-overhaul}
*Zuletzt aktualisiert: März 2026*

- Abrechnung pro Nachricht ersetzt Abrechnung pro Konversation
- Utility-Nachrichten, die innerhalb eines 24-Stunden-Servicefensters gesendet werden, wurden kostenlos
- Aktualisierte Utility-/Authentifizierungsraten in mehreren Märkten mit neuen Volumenstufen
- Neue Regeln zur Fehlkategorisierung von Utility-Templates – Unternehmen können mit Template-Ablehnung und Einschränkungen bei der Einreichung konfrontiert werden

### April 2025: Pausierung von Marketing-Nachrichten an US-Telefonnummern {#april-2025-pause-of-marketing-messages-to-us-phone-numbers}
*Zuletzt aktualisiert: August 2026*

Meta pausiert neue geschäftsinitiierte Marketing-Konversationen mit WhatsApp-Nutzer:innen, die eine US-Telefonnummer haben (eine Nummer bestehend aus der Vorwahl `+1` und einer US-Ortsvorwahl). Es gibt derzeit kein geplantes Datum, an dem diese Pausierung aufgehoben wird.

Marketing-Templates können weiterhin innerhalb eines offenen nutzer:inneninitiierten Konversationsfensters zugestellt werden, beispielsweise eines 24-Stunden-Kundenservice-Fensters oder eines 72-Stunden-Gratis-Einstiegspunktfensters, das durch eine [Anzeige, die zu WhatsApp weiterleitet]({{site.baseurl}}/user_guide/channels/whatsapp/use_cases/ads_that_click_to_whatsapp#considerations) geöffnet wurde. Außerhalb dieser Fenster führen Versuche, Marketing-Templates an US-Telefonnummern zu senden, zum Fehlercode `131049`. Utility-, Authentifizierungs-, Service- und Antwortnachrichten bleiben verfügbar.

### März 2025: Einschränkungen bei Fehlnutzung von Template-Kategorien {#march-2025-template-category-misuse-restrictions}
*Zuletzt aktualisiert: März 2026*

- Meta hat Durchsetzungsmaßnahmen für Unternehmen eingeführt, die die Utility-/Marketing-Kategorisierung missbrauchen
- Kann zu 7- bis 30-tägigen Einschränkungen bei der Template-Erstellung und Kategorieüberprüfungen führen

### März 2025: Nutzer:innenindividuelle Limits für Marketing-Template-Nachrichten {#march-2025-per-user-marketing-template-message-limits}
*Zuletzt aktualisiert: August 2025*

Meta wird die Anzahl der Marketing-Template-Nachrichten begrenzen, die ein:e Nutzer:in von allen Unternehmen in einem bestimmten Zeitraum erhalten kann, beginnend mit Nachrichten, die mit geringerer Wahrscheinlichkeit gelesen werden.

Eine Ausnahme ist: Wenn eine Person auf eine Marketing-Nachricht antwortet, startet ein 24-Stunden-Kundenservice-Fenster. Marketing-Nachrichten, die innerhalb dieses Fensters gesendet werden, zählen nicht zum Limit der Person.

Das spezifische Limit variiert je nach Nutzer:in, abhängig von deren Engagement-Level. Erfahren Sie mehr über die nutzer:innenindividuellen Limits für Marketing-Template-Nachrichten in der [WhatsApp-Dokumentation zu nutzer:innenindividuellen Limits für Marketing-Template-Nachrichten](https://developers.facebook.com/docs/whatsapp/cloud-api/guides/send-message-templates#per-user-marketing-template-message-limits).

### Januar 2025: WhatsApp pausiert den Versand von Marketing-Nachrichten an US-Nutzer:innen ab dem 1. April {#january-2025-whatsapp-pausing-marketing-message-sending-to-us-users-starting-april-1}
*Zuletzt aktualisiert: Januar 2025*

WhatsApp wird den Versand von Marketing-Nachrichten an US-Nutzer:innen (Personen mit US-Telefonnummern) ab dem 1. April 2025 pausieren. [Utility-, Service- und Authentifizierungsnachrichten](https://developers.facebook.com/docs/whatsapp/pricing/) sowie [Antwortnachrichten]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message) sind in den USA weiterhin zulässig.

Der Versand von Marketing-Nachrichten (sowie alle anderen Nachrichtentypen) in alle anderen Länder oder Regionen ist weiterhin zulässig und wird nicht beeinträchtigt.

Meta hat uns mitgeteilt, dass dieses Update durchgeführt wird, um die Gesundheit des WhatsApp-Ökosystems in den USA zu erhalten, wo WhatsApp schnell wächst, sich aber noch in einem früheren Stadium befindet (beispielsweise erzielen Marketing-Nachrichten niedrigeres Engagement als in anderen Regionen). Sie werden weiterhin evaluieren, wann der US-Markt bereit ist, Marketing-Nachrichten wieder aufzunehmen.

Die Zustellung von Marketing-Nachrichten an Telefonnummern mit US-Ortsvorwahlen wird von WhatsApp abgelehnt und gibt den Fehlercode 131049 zurück.

### November 2024: Änderungen der WhatsApp-Opt-in-Richtlinie {#november-2024-changes-to-whatsapp-opt-in-policy}
*Zuletzt aktualisiert: Januar 2025*

Meta hat kürzlich seine [Opt-in-Richtlinie](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/) aktualisiert. Anstatt eine kanalspezifische Einwilligung zu verlangen, können Unternehmen Nutzer:innen jetzt auf der Plattform kontaktieren, wenn:

1. Die Person ihre Telefonnummer angegeben hat.
2. Die Person eine Opt-in-Einwilligung für allgemeines Messaging erteilt hat, nicht nur für WhatsApp.

Unternehmen müssen weiterhin alle lokalen Gesetze einhalten und die folgenden Anforderungen bei der Einholung des Opt-in beachten:

- Unternehmen müssen klar angeben, dass eine Person sich für den Empfang von Mitteilungen des Unternehmens entscheidet
- Unternehmen müssen den Firmennamen klar angeben, von dem die Person Nachrichten erhalten wird
- Unternehmen müssen das geltende Recht einhalten

Obwohl WhatsApp seine Richtlinie gelockert hat, empfiehlt Braze weiterhin, ein kanalspezifisches Opt-in für den WhatsApp-Kanal einzuholen, um das beste Kundenerlebnis und die besten Engagement-Raten zu fördern. Sprechen Sie wie immer mit Ihrem Rechtsteam, um zu klären, was für Ihre Marke sinnvoll ist.

### November 2024: Updates zum nutzer:innenindividuellen Marketing-Template-Limit für Personen in den USA vor der Feiertagssaison {#november-2024-updates-to-the-per-user-marketing-template-limit-for-people-in-the-us-ahead-of-the-holiday-season}
*Zuletzt aktualisiert: Dezember 2024*

Seit Meta das nutzer:innenindividuelle Marketing-Template-Limit eingeführt hat, hat Meta signifikante Verbesserungen bei den Leseraten und der Nutzer:innenzufriedenheit festgestellt.

Ab sofort, vor der Feiertagssaison, werden Personen in den USA weniger neue Marketing-Konversationen erhalten. Meta erwartet, dass diese Änderung engagiertere Zielgruppen schafft, was letztlich zu besseren Ergebnissen für Unternehmen führt. Dies kann zu niedrigeren Zustellraten für Ihr Unternehmen führen, wenn Sie Marketing-Nachrichten an US-Telefonnummern senden, was über den Fehlercode `131049` über Braze-Currents und das Nachrichtenaktivitätsprotokoll überwacht werden kann.

Unternehmen in den USA können weiterhin Marketing-Nachrichten in andere Regionen zustellen, und es gibt keine Auswirkungen auf Utility-, Authentifizierungs- oder Servicenachrichten oder Marketing-Template-Nachrichten, die innerhalb eines nutzer:inneninitiierten Konversationsfensters gesendet werden (beispielsweise eine Click-to-WhatsApp-Anzeige oder ein Produktkarussell- oder Coupon-Template, das als Teil einer Konversation gesendet wird).

### November 2024: WhatsApp erweitert qualitätsbasierte Account-Durchsetzungen um Leseraten {#november-2024-whatsapp-expanding-quality-based-account-enforcements-to-include-read-rates}
*Zuletzt aktualisiert: Dezember 2024*

WhatsApp investiert kontinuierlich in neue Wege, um Unternehmen dabei zu helfen, qualitativ hochwertige Erlebnisse für ihre Kund:innen zu schaffen, beispielsweise durch die Reduzierung von Spam-ähnlichem Verhalten auf der Plattform.

Ab dem 22. November begann WhatsApp damit, die bestehenden Qualitätsdurchsetzungen auf Account-Ebene auf WhatsApp Business Accounts (WABAs) mit extrem niedrigen Leseraten auszuweiten. Diese Änderung wird weltweit ausgerollt.

Wenn die Leserate eines Accounts signifikant sinkt (wenn beispielsweise die Mehrheit der vom Account gesendeten Nachrichten ungelesen bleibt), werden Nachrichtenblockaden für den Account durchgesetzt. Der Schweregrad der Blockade steigt, wenn die Leseraten konsistent niedrig bleiben.

Wenn die Leserate eines Accounts extrem niedrig ist, werden die folgenden Maßnahmen ergriffen:

- Der Account wird für das Senden geschäftsinitiierter Nachrichten gesperrt. Er kann weiterhin auf kund:inneninitiierte Nachrichten antworten. Diese anfängliche Sperre ist ein „Soft Lock“ und kann durch Auswahl der Bestätigungsschaltfläche in der Account-Qualität bestätigt werden, um erneut Nachrichten senden zu können.
- Wenn die Leserate nach dem Soft Lock weiter sinkt oder niedrig bleibt, können Unternehmen mit schrittweise zunehmenden Durchsetzungsmaßnahmen konfrontiert werden (beispielsweise einige Tage Messaging-Einschränkungen).
- Unternehmen müssen warten, bis die durchgesetzte Begrenzung abläuft, um erneut Nachrichten senden zu können. Wenn die Leserate nach wiederholten Soft Locks weiterhin niedrig bleibt, wird der Account letztendlich abgemeldet.

#### So bleiben Sie über diese Warnungen und Durchsetzungen informiert {#how-to-stay-updated-on-these-warnings-and-enforcements}

Ähnlich wie bei bestehenden Plattformdurchsetzungen werden Unternehmen über diese Maßnahmen benachrichtigt und können sie über die Seite „Account Quality“ im WhatsApp Business Manager:in bestätigen. Stellen Sie sicher, dass die korrekten Kontaktdaten im WhatsApp Business Manager:in für alle erforderlichen Administrator:innen hinterlegt sind, da die Durchsetzungsbenachrichtigungs-E-Mails basierend auf diesen Informationen gesendet werden.

Benachrichtigungen über schwerwiegende Spam-Verstöße werden:

- Im Benachrichtigungscenter des WhatsApp Business Manager:in angezeigt
- Als Banner im WhatsApp Manager:in angezeigt
- Per E-Mail an alle im WhatsApp Business Manager:in eingerichteten Administrator:innen gesendet

### Mai 2024: Cloud API geht in der Türkei live {#may-2024-cloud-api-going-live-in-trkiye}
*Zuletzt aktualisiert: Mai 2024*

Meta bietet Cloud-API-Unternehmen jetzt Zugang zur Türkei für geschäftliches Messaging. Zuvor war die WhatsApp Cloud API für Unternehmen in der Türkei nutzbar, aber WhatsApp-Nutzer:innen mit türkischen Nummern konnten keine über die Cloud API gesendeten Nachrichten senden oder empfangen.

Meta macht es Nutzer:innen immer deutlich, wenn sie mit einem von Meta gehosteten Unternehmen chatten, und alle Nutzer:innen müssen die entsprechenden WhatsApp-Nutzungsbedingungen und Datenschutzrichtlinien akzeptieren, um mit dem geschäftlichen Messaging fortzufahren. Das Update der Nutzungsbedingungen und Datenschutzrichtlinien von 2021 in der Türkei war pausiert worden, wird aber jetzt ausgerollt. Es ändert nichts an Metas Engagement für den Datenschutz – persönliche Konversationen werden weiterhin durch Ende-zu-Ende-Verschlüsselung geschützt, sodass nur Sie und der beabsichtigte Empfänger sie sehen können. Das Update ermöglicht es türkischen Nutzer:innen, auf optionale Geschäftsfunktionen zuzugreifen, wenn sie sich dafür entscheiden, und bietet mehr Transparenz darüber, wie WhatsApp funktioniert.

Cloud-API-Unternehmen können jetzt Konversationen mit WhatsApp-Nutzer:innen mit türkischen Nummern initiieren, die nun einen Webhook als „gesendet“-Konversation zurückgeben, anstatt des bisherigen Fehlercodes 131026.

Damit eine Geschäftsnachricht „zugestellt“ oder „gelesen“ wird, muss der:die Nutzer:in die WhatsApp-Bedingungen akzeptiert haben. Einem Unternehmen wird nichts berechnet, es sei denn, die Nachricht wird zugestellt.

Nutzer:innen, die eine Nachricht von einem Cloud-API-Unternehmen erhalten oder versuchen, eine Nachricht an ein solches zu senden, wird eine In-App-Benachrichtigung über das Bedingungsupdate angezeigt, die deutlich macht, dass sie einem Cloud-API-Unternehmen erst dann Nachrichten senden können, wenn sie das WhatsApp-Update akzeptiert haben. Darüber hinaus werden Nutzer:innen, die die App auf ihrem Telefon Registrierung oder erneut registrieren, aufgefordert, das WhatsApp-Update zu akzeptieren.

Wenn ein:e Nutzer:in das Update akzeptiert, sieht er:sie den bestehenden Cloud-API-Systemnachrichtenhinweis, wenn er:sie mit einem Cloud-API-Unternehmen chattet.

### Mai 2024: Nutzer:innenindividuelle Limits für Marketing-Template-Nachrichten {#may-2024-per-user-marketing-template-message-limits}
*Zuletzt aktualisiert: Mai 2024*

Meta führt neue Ansätze ein, um qualitativ hochwertige Nutzer:innenerlebnisse aufrechtzuerhalten und das Engagement bei Marketing-Template-Nachrichten auf der WhatsApp-Plattform zu maximieren. Ab dem 23. Mai 2024 wird die Anzahl der Marketing-Template-Nachrichten begrenzt, die jede:r einzelne Nutzer:in von allen Unternehmen, mit denen er:sie interagiert, in einem bestimmten Zeitraum erhalten kann, beginnend mit einer kleinen Anzahl von Konversationen, die mit geringerer Wahrscheinlichkeit gelesen werden. Beachten Sie, dass das Limit basierend auf der Anzahl der Marketing-Template-Nachrichten bestimmt wird, die diese Person bereits von einem beliebigen Unternehmen erhalten hat, und nicht speziell mit Ihrer Marke zusammenhängt. Dies kann jedoch die Zustellbarkeit Ihrer Marketing-Template-Nachrichten beeinflussen.

Das Limit gilt nur für Marketing-Template-Nachrichten, die normalerweise eine neue Marketing-Konversation eröffnen würden. Wenn bereits eine Marketing-Konversation zwischen Ihrer Marke und einem:einer WhatsApp-Nutzer:in offen ist, sind an den:die Nutzer:in gesendete Marketing-Template-Nachrichten nicht betroffen.

Wenn eine Marketing-Template-Nachricht aufgrund des Limits nicht an eine:n bestimmte:n Nutzer:in zugestellt wird, gibt die Cloud API den Fehlercode 131026 zurück. Beachten Sie jedoch, dass diese Fehlercodes ein breites Spektrum von Problemen abdecken, die zur Nicht-Zustellung einer Nachricht führen können, und Meta aus Datenschutzgründen nicht offenlegt, ob die Nachricht tatsächlich aufgrund des Limits nicht zugestellt wurde. Informationen zu Gründen für Nicht-Zustellungen und was Sie tun können, um deren zugrunde liegende Ursache zu ermitteln, finden Sie im [Fehlerbehebungsdokument](https://developers.facebook.com/docs/whatsapp/cloud-api/support#troubleshooting) der Cloud API.

Wenn Sie einen dieser Fehlercodes erhalten und vermuten, dass er auf das Limit zurückzuführen ist, vermeiden Sie es, die Template-Nachricht sofort erneut zu senden, da dies nur zu einer weiteren Fehlerantwort führt.

Weitere Informationen zu diesem Zustellbarkeitsupdate, einschließlich Details zur Überwachung Ihrer Zustellbarkeit und anderer Best Practices für Marketing-Messaging auf WhatsApp, finden Sie in unserem aktuellen [Blogbeitrag](https://www.braze.com/resources/articles/meta-introduces-deliverability-updates-for-whatsapp?utm_campaign=fy25-q2-global-customer-customer-meta-deliverability-updates-for-whatsapp&utm_medium=email-cdb&utm_source=braze&utm_content=blog-meta-deliverability-updates-for-wa-blog).

### April 2024: Template-Pacing für Utility-Templates {#april-2024-template-pacing-for-utility-templates}
*Zuletzt aktualisiert: April 2024*

Letztes Jahr hat WhatsApp Template-Pacing für Marketing-Nachrichten als neuen Weg eingeführt, um Unternehmen zu helfen, das Engagement ihrer Templates zu verbessern und wertvolle Nutzer:innenerlebnisse zu schaffen. Ab dem 30. April wird Template-Pacing auf Utility-Nachrichten ausgeweitet. Wenn ein Utility-Template für einen Account aufgrund von Nutzer:innenfeedback pausiert wird, werden die neuen Utility-Templates, die in den folgenden sieben Tagen für diesen Account erstellt werden, gedrosselt.

### April 2024: Leseraten fließen in die Qualitätsbewertung von Marketing-Templates ein {#april-2024-read-rates-will-affect-quality-rating-for-marketing-templates}
*Zuletzt aktualisiert: März 2024*

WhatsApp testet neue Ansätze, beginnend mit Verbraucher:innen in Indien, um wertvollere Erlebnisse zu schaffen und das Engagement bei Marketing-Konversationen von Unternehmen zu maximieren. Dies kann die Begrenzung der Anzahl von Marketing-Konversationen umfassen, die eine Person von einem beliebigen Unternehmen in einem bestimmten Zeitraum erhält, beginnend mit einer kleinen Anzahl von Konversationen, die mit geringerer Wahrscheinlichkeit gelesen werden. Braze erhält einen Fehlercode, wenn eine Nachricht nicht zugestellt wird.

WhatsApp wird Leseraten als Teil der Qualitätsbewertung für Marketing-Templates berücksichtigen, zusätzlich zu traditionellen Metriken wie Blockierungen und Meldungen. WhatsApp kann Marketing-Nachrichten-Campaigns mit niedrigen Leseraten vorübergehend pausieren, um Unternehmen Zeit zu geben, die Templates mit dem niedrigsten Engagement zu überarbeiten, bevor das Volumen ab dem 1. April 2024 skaliert wird.

### Februar 2024: Experiment zu Marketing-Konversationen {#february-2024-marketing-conversations-experimentation}
*Zuletzt aktualisiert: Februar 2024*

Ab dem 6. Februar 2024 testet WhatsApp neue Ansätze, beginnend mit Verbraucher:innen in Indien, um wertvollere Erlebnisse zu schaffen und das Kund:innen-Engagement bei den Marketing-Konversationen Ihrer Marke zu maximieren. Dies kann die Begrenzung der Anzahl von Marketing-Konversationen umfassen, die ein:e Nutzer:in von Ihrer Marke in einem bestimmten Zeitraum erhält, beginnend mit einer kleinen Anzahl von Konversationen, die mit geringerer Wahrscheinlichkeit gelesen werden.

### Oktober 2023: Template-Pacing {#october-2023-template-pacing}
*Zuletzt aktualisiert: Oktober 2023*

Ab dem 12. Oktober 2023 führt WhatsApp ein Konzept namens „Template-Pacing“ für Marketing-Nachrichten ein. Anstatt Ihre Nachricht gleichzeitig an Ihre gesamte Campaign-Zielgruppe zu senden, wird beim „Template-Pacing“ die Nachricht zunächst an eine kleinere Teilgruppe von Nutzer:innen zugestellt, um Echtzeit-Feedback von Campaign-Empfänger:innen zu sammeln, bevor die verbleibenden Nachrichten gesendet werden.

Das „Pace-Limit“ (die anfängliche Teilmenge der gesendeten Nachrichten) ist variabel und hängt vom Template ab. Nach dem anfänglichen Versand hält WhatsApp die verbleibenden Nachrichten für maximal 30 Minuten zurück. Während dieser Halteperiode wird die Qualität des Templates basierend auf Kund:innenfeedback bewertet. Wenn das Feedback positiv ist, was auf ein qualitativ hochwertiges Template hindeutet, werden die verbleibenden Nachrichten zugestellt. Wenn das Feedback negativ ist, werden die verbleibenden nicht zugestellten Nachrichten verworfen, um weiteres negatives Feedback von einem größeren Teil Ihrer Kund:innen zu verhindern und Ihnen zu helfen, potenzielle Probleme bei der Qualitätsdurchsetzung zu vermeiden (wie Auswirkungen auf die Qualitätsbewertung der Telefonnummer).

Beachten Sie, dass WhatsApp beim Template-Pacing dasselbe System zur Bewertung der Template-Qualität verwendet wie bei der Template-Pausierung. Nachrichten, die beim Template-Pacing nicht zugestellt werden (aufgrund von Templates niedriger Qualität), sind dieselben, die in größerem Umfang pausiert worden wären.

Letztendlich bietet Ihnen dieses Update eine schnellere Feedback-Schleife (30 Minuten statt Stunden oder Tagen bei der Template-Pausierung), sodass Sie Ihre Templates anpassen und ein besseres Kundenerlebnis bieten können.

**Wenn Sie weitere Fragen zu diesem Update haben, kontaktieren Sie Ihre:n Meta-Partner-Vertretung.**

### Juni 2023: Messaging-Experiment {#june-2023-messaging-experimentation}
*Zuletzt aktualisiert: Juni 2023*

Ab dem 14. Juni 2023 führt Meta neue Experimentierpraktiken auf der WhatsApp-Plattform ein, um zu bewerten, wie Marketing-Nachrichten das Verbraucher:innenerlebnis und -Engagement beeinflussen. Dieses Experiment kann Ihre Marketing-Nachrichten betreffen, die über die WhatsApp Business API mit Braze gesendet werden.

Meta beabsichtigt, solche Experimente auf der WhatsApp-Plattform fortzusetzen. Weitere Informationen finden Sie in der [Meta-Dokumentation](https://developers.facebook.com/docs/whatsapp/on-premises/guides/experiments?content_id=86oue5PtwEgcBJl).

**Das WhatsApp-Experiment betrifft nur Marketing-Nachrichten.** Dieses Experiment kann die Zustellung von Marketing-Template-Nachrichten beeinflussen. Utility- und Authentifizierungs-Templates werden weiterhin ohne Auswirkungen durch das Experiment zugestellt.

Im Experiment wählt Meta zufällig etwa 1 % der WhatsApp-Verbraucher:innen als Teilnehmer:innen aus. Wenn eine Person ausgewählt wird, stellt Meta keine Marketing-Template-Nachrichten an diese Verbraucher:innen zu, es sei denn, eine der folgenden Bedingungen trifft zu:

- Die Person hat Ihnen in den letzten 24 Stunden geantwortet;
- Es ist eine bestehende Marketing-Konversation offen; oder
- Die Person hat in den letzten 72 Stunden auf eine WhatsApp-Anzeige geklickt.

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