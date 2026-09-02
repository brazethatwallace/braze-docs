---
nav_title: FAQ
article_title: FAQ zu Campaigns
page_order: 10
page_type: FAQ
description: "Diese Seite enthält Antworten auf häufig gestellte Fragen zu Campaigns."
tool: Campaigns
---

# Häufig gestellte Fragen {#frequently-asked-questions}

> Dieser Artikel enthält Antworten auf einige häufig gestellte Fragen zu Campaigns.

## Wie erstelle ich eine Multichannel-Campaign? {#how-do-i-create-a-multichannel-campaign}

Siehe [Multichannel-Campaigns]({{site.baseurl}}/user_guide/messaging/campaigns/creating_campaign#create-a-multichannel-campaign) unter **Campaign erstellen** für Einrichtungsschritte und unterstützte Kanäle.

### Kann ich meiner Multichannel-Campaign eine Kontrollgruppe hinzufügen? {#can-i-add-a-control-group-to-my-multichannel-campaign}

Siehe [Kontrollgruppen]({{site.baseurl}}/user_guide/messaging/campaigns/creating_campaign#multichannel-control-groups) unter **Campaign erstellen**. Für kanalübergreifende Tests verwenden Sie [Canvas]({{site.baseurl}}/user_guide/messaging/canvas).

### Welche Möglichkeiten gibt es, mit dem Testen und Optimieren von Campaigns zu beginnen? {#what-are-some-ways-i-can-start-testing-and-optimizing-campaigns}

Multivariate Campaigns und Canvases mit mehreren Varianten sind ein hervorragender Einstieg! Sie können zum Beispiel eine [multivariate Campaign]({{site.baseurl}}/user_guide/messaging/ab_testing) durchführen, um eine Nachricht mit verschiedenen Texten oder Betreffzeilen zu testen. Canvases mit mehreren Varianten können helfen, gesamte Workflows zu testen.

### Warum ist die Öffnungsrate meiner Campaign gesunken? {#why-did-the-open-rate-for-my-campaign-decrease}

Niedrige Öffnungsraten hängen nicht immer mit einem technischen Problem zusammen. Es kann Probleme mit dem E-Mail-Clipping geben, was dazu führt, dass das Tracking-Pixel fehlt. Es ist aber auch möglich, dass weniger Nutzer:innen ihre E-Mails aufgrund des Inhalts oder aufgrund von Änderungen der Zielgruppengröße öffnen.

### Wie werden Campaign-Zielgruppen ausgewertet? {#how-are-campaign-audiences-evaluated}

Standardmäßig prüfen Campaigns die Zielgruppenfilter zum Eintrittszeitpunkt. Bei aktionsbasierten Campaigns mit einer Verzögerung gibt es die Option, die Segment-Kriterien zum Sendezeitpunkt erneut auszuwerten, um sicherzustellen, dass Nutzer:innen beim Versand der Nachricht noch Teil der Zielgruppe sind.

### Warum gibt es einen Unterschied zwischen der Anzahl eindeutiger Empfänger:innen und der Anzahl der Sendungen für eine bestimmte Campaign oder ein Canvas? {#why-is-there-a-difference-between-the-number-of-unique-recipients-and-the-number-of-sends-for-a-given-campaign-or-canvas}

Eine mögliche Erklärung ist, dass die Campaign oder das Canvas die erneute Qualifikation aktiviert hat, sodass Nutzer:innen, die die Segment- und Zustellungsbedingungen erfüllen, die Nachricht mehr als einmal erhalten können. Wenn die erneute Qualifikation nicht aktiviert ist, liegt die wahrscheinliche Erklärung für den Unterschied zwischen Sendungen und eindeutigen Empfänger:innen darin, dass Nutzer:innen mehrere Geräte über verschiedene Plattformen hinweg haben, die mit ihren Profilen verknüpft sind.

Wenn Sie beispielsweise ein Canvas haben, das sowohl iOS- als auch Web-Push-Benachrichtigungen enthält, kann eine bestimmte Nutzer:in mit sowohl mobilen als auch Desktop-Geräten mehr als eine Nachricht erhalten.

### Warum ist die Anzahl der *eindeutigen Empfänger:innen* höher als die Anzahl der Nutzer:innen, die ich angesprochen habe? {#why-is-_unique-recipients_-higher-than-the-number-of-users-i-targeted}

Die Anzahl der *eindeutigen Empfänger:innen* kann höher sein als die erwartete Zielgruppe, da Braze für die Berichterstattung tägliche eindeutige Empfänger:innen erfasst. So kann Braze Konversionen innerhalb des Konversionsfensters jedes Mal zuordnen, wenn eine Nutzer:in die Nachricht erhält, anstatt mehrere Empfänge zu einem einzigen Lifetime-Wert zusammenzufassen (was die Konversionsberechnung verzerren würde).

Wenn eine Nutzer:in beispielsweise am Montag und erneut am Freitag eine Campaign erhält und nach jedem Versand konvertiert, kann Braze dies als zwei Empfänge und zwei Konversionen melden. Würde Braze nur eine einzige Lifetime-„Eindeutigkeit“ über beide Sendungen zählen, würden Sie entweder eine gültige Konversion verlieren oder doppelt gegen eine:n Empfänger:in zählen, was die Campaign-Performance schwerer lesbar macht.

Dasselbe Muster gilt für wiederkehrende Campaigns und die erneute Qualifikation: Wenn zwei Nutzer:innen heute und morgen jeweils einen wiederkehrenden Versand erhalten, zählt *Eindeutige Empfänger:innen* vier tägliche Empfängerzeilen, nicht zwei Profile.

### Warum kann die Anzahl der Konversionen die Anzahl der eindeutigen Nutzer:innen bei Multichannel-Campaigns übersteigen? {#why-can-the-number-of-conversions-exceed-the-number-of-unique-users-for-multichannel-campaigns}

Siehe [Konversionen und Berichterstattung]({{site.baseurl}}/user_guide/messaging/campaigns/creating_campaign#multichannel-conversions) unter **Campaign erstellen** und [Regeln für das Konversions-Tracking]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events#conversion-tracking-rules) unter **Konversions-Events**.

### Warum hat meine Campaign eine kleinere erreichbare Nutzerbasis als das Segment, das ich für die Campaign verwende? {#why-does-my-campaign-have-a-smaller-reachable-user-base-than-the-segment-that-im-using-for-the-campaign}

Wenn Sie eine [globale Kontrollgruppe]({{site.baseurl}}/user_guide/audience/global_control_group) eingerichtet haben, verhindert diese, dass ein Prozentsatz Ihrer erreichbaren Zielgruppe Campaigns erhält. Das bedeutet, dass die Anzahl der erreichbaren Nutzer:innen für Ihr Segment manchmal größer sein kann als die Anzahl der erreichbaren Nutzer:innen für Ihre Campaign, selbst wenn die Campaign dasselbe Segment verwendet.

### Was bietet die Zustellung nach Ortszeit? {#what-does-local-time-zone-delivery-offer}

Die Zustellung nach Ortszeit ermöglicht es Ihnen, Messaging-Campaigns an ein Segment basierend auf der individuellen Zeitzone der Nutzer:innen zuzustellen. Ohne Zustellung nach Ortszeit werden Campaigns basierend auf den Zeitzoneneinstellungen Ihres Unternehmens in Braze geplant.

Ein in London ansässiges Unternehmen, das eine Campaign um 12 Uhr mittags sendet, erreicht beispielsweise Nutzer:innen an der Westküste Amerikas um 4 Uhr morgens. Wenn Ihre App nur in bestimmten Ländern verfügbar ist, stellt dies möglicherweise kein Risiko für Sie dar. Andernfalls empfehlen wir dringend, das Senden von Push-Benachrichtigungen in den frühen Morgenstunden an Ihre Nutzerbasis zu vermeiden.

### Wie erkennt Braze die Zeitzone einer Nutzer:in? {#how-does-braze-recognize-a-users-time-zone}

Braze ermittelt die Zeitzone einer Nutzer:in automatisch anhand ihres Geräts. Dies gewährleistet Zeitzonen-Genauigkeit und vollständige Abdeckung Ihrer Nutzer:innen. Nutzer:innen, die über die User API oder anderweitig ohne Zeitzone erstellt werden, haben die Zeitzone Ihres Unternehmens als Standardzeitzone, bis sie in Ihrer App durch das SDK erkannt werden.

Sie können die Zeitzone Ihres Unternehmens in Ihren [Unternehmenseinstellungen]({{site.baseurl}}/user_guide/administer/global/admin_settings) im Dashboard überprüfen.

### Wann wertet Braze Nutzer:innen für die Zustellung nach Ortszeit aus? {#when-does-braze-evaluate-users-for-local-time-zone-delivery}

Braze wertet die Eintrittsberechtigung von Nutzer:innen zu folgenden Zeitpunkten aus:

- Samoa-Zeit (UTC+13) am geplanten Tag
- Die Ortszeit am geplanten Tag

Damit eine Nutzer:in eintrittsberechtigt ist, muss sie beide Prüfungen bestehen. Wenn beispielsweise ein Canvas am 7. August 2021 um 14 Uhr Ortszeit starten soll, dann erfordert das Targeting einer Nutzer:in in New York die folgenden Berechtigungsprüfungen:

- New York am 6. August 2021 um 21 Uhr
- New York am 7. August 2021 um 14 Uhr

Um einzutreten, muss eine Nutzer:in zu beiden Auswertungszeitpunkten Ihrer Zielgruppe und Ihren Filtern entsprechen. Wenn die Nutzer:in bei der ersten Prüfung nicht berechtigt ist, führt Braze die zweite Prüfung nicht durch. Es gibt keine Mindestdauer, die eine Nutzer:in vor dem Start im Segment gewesen sein muss. Nur die Berechtigung zum jeweiligen Prüfzeitpunkt ist entscheidend.

Dieses Auswertungsverhalten ist unabhängig davon, [wie weit im Voraus Sie die Campaign im Dashboard planen](#how-do-i-schedule-a-local-time-zone-campaign). Eine Planung von mindestens 24 Stunden im Voraus ist eine Empfehlung, da sie dazu beiträgt, Nachrichten über das gesamte 24-Stunden-Ortszeit-Fenster zuzustellen – keine Anforderung, dass jede Nutzer:in 24 Stunden lang in der Zielgruppe gewesen sein muss.

#### Beispiele {#examples}

Wenn beispielsweise eine Campaign um 19 Uhr UTC zugestellt werden soll, beginnen wir mit der Einreihung der Campaign-Sendungen, sobald eine Zeitzone identifiziert wird (wie z. B. Samoa). Das bedeutet, wir bereiten den Versand der Nachricht vor, senden die Campaign aber noch nicht. Wenn Nutzer:innen bei der Berechtigungsprüfung keinem Filter entsprechen, gehören sie nicht zur Zielgruppe.

Nehmen wir als weiteres Beispiel an, Sie möchten zwei Campaigns erstellen, die am selben Tag gesendet werden sollen – eine morgens und eine abends – und einen Filter hinzufügen, dass Nutzer:innen die zweite Campaign nur erhalten können, wenn sie die erste bereits erhalten haben. Bei der Zustellung nach Ortszeit erhalten einige Nutzer:innen die zweite Campaign möglicherweise nicht. Das liegt daran, dass wir die Berechtigung prüfen, wenn die Zeitzone der Nutzer:in identifiziert wird. Wenn die geplante Zeit in ihrer Zeitzone noch nicht eingetreten ist, haben sie die erste Campaign noch nicht erhalten und sind somit für die zweite Campaign nicht berechtigt.

Die folgende Zeitleiste setzt eine Segment-Definition voraus, die ein zeitlich begrenztes Mitgliedschaftsfenster enthält. In diesem Beispiel verlassen Nutzer:innen das Segment 24 Stunden nach dem Beitritt. Dieses Filterverhalten ist ein Grund, warum eine Nutzer:in die erste Prüfung bestehen und bei der zweiten durchfallen kann.

![Zeitleiste einer Nutzer:in, die vor der ersten Prüfung in das Segment eintritt und es vor der zweiten wieder verlässt.]({% image_buster /assets/img/local_time_zone_diagram.png %})

{% details Beschreibung der Zeitleiste %}

1. Nutzer:in A tritt um 6:59 Uhr PST (4:59 Uhr Samoa-Zeit) in das Segment ein.
2. Braze prüft um 7 Uhr Samoa-Zeit die Segmentzugehörigkeit, um festzustellen, welche Nutzer:innen in den nächsten 24 Stunden berechtigt sind, die Campaign zu erhalten. Nutzer:in A ist zu diesem Zeitpunkt im Segment.
3. Das Segment hat ein 24-Stunden-Fenster, sodass Nutzer:in A das Segment 24 Stunden nach dem Beitritt verlässt: 6:59 Uhr PST (4:59 Uhr Samoa-Zeit).
4. Die Ortszeit-Campaign sendet um 7 Uhr PST, aber Nutzer:in A hat das Segment bereits verlassen.

{% enddetails %}

### Wie plane ich eine Campaign mit Ortszeitversand? {#how-do-i-schedule-a-local-time-zone-campaign}

Der vorherige Abschnitt beschreibt, wann Braze die Berechtigung für die Zustellung nach Ortszeit auswertet (die beiden Prüfungen). Dieser Abschnitt beschreibt, wann Sie den Campaign-Zeitplan im Dashboard festlegen (Planungsvorlaufzeit) und welche Nutzer:innen die Nachricht noch erhalten, wenn Sie mit weniger als 24 Stunden Vorlauf planen.

Wählen Sie beim Planen einer Campaign aus, sie zu einem festgelegten Zeitpunkt zu senden, und wählen Sie dann **Campaign an Nutzer:innen in ihrer Ortszeit senden**.

Braze empfiehlt dringend, alle Ortszeit-Campaigns mindestens 24 Stunden im Voraus zu planen. Da eine solche Campaign über einen ganzen Tag hinweg gesendet werden muss, stellt eine 24-Stunden-Vorausplanung sicher, dass Ihre Nachricht Ihr gesamtes Segment erreicht. Sie können diese Campaigns jedoch bei Bedarf auch mit weniger als 24 Stunden Vorlauf planen. Beachten Sie, dass Braze keine Nachrichten an Nutzer:innen sendet, deren Sendezeit um mehr als 1 Stunde überschritten ist.

Wenn es beispielsweise 13 Uhr ist und Sie eine Ortszeit-Campaign für 15 Uhr planen, wird die Campaign sofort an alle Nutzer:innen gesendet, deren Ortszeit zwischen 15 und 16 Uhr liegt, aber nicht an Nutzer:innen, deren Ortszeit 17 Uhr ist. Außerdem darf die von Ihnen gewählte Sendezeit in der Zeitzone Ihres Unternehmens noch nicht verstrichen sein.

Das Bearbeiten einer Ortszeit-Campaign, die weniger als 24 Stunden im Voraus geplant ist, ändert den Zeitplan der Nachricht nicht. Wenn Sie sich entscheiden, eine Ortszeit-Campaign auf eine spätere Zeit zu ändern (z. B. 19 Uhr statt 18 Uhr), erhalten Nutzer:innen, die zum Zeitpunkt der ursprünglichen Sendezeit im Ziel-Segment waren, die Nachricht weiterhin zur ursprünglichen Zeit (18 Uhr). Wenn Sie eine Ortszeit-Campaign auf eine frühere Zeit ändern (z. B. 16 Uhr statt 17 Uhr), wird die Campaign trotzdem an alle Segmentmitglieder zur ursprünglichen Zeit (17 Uhr) gesendet.

{% alert note %}
Für Canvas-Komponenten müssen Nutzer:innen nicht 24 Stunden in der Komponente verweilen, um die nächste Komponente in der User-Journey bei Ortszeitversand zu erhalten.
{% endalert %}

Wenn Sie Nutzer:innen die erneute Qualifikation für die Campaign erlaubt haben, erhalten sie sie erneut zur ursprünglichen Zeit (17 Uhr). Bei allen nachfolgenden Vorkommen Ihrer Campaign werden Ihre Nachrichten jedoch nur zur aktualisierten Zeit gesendet.

### Wann werden Änderungen an Ortszeit-Campaigns wirksam? {#when-do-changes-to-local-time-zone-campaigns-take-effect}

Zielsegmente für Ortszeit-Campaigns sollten für zeitbasierte Filter mindestens ein 48-Stunden-Fenster enthalten, um die Zustellung an das gesamte Segment zu gewährleisten. Betrachten Sie beispielsweise ein Segment, das Nutzer:innen an ihrem zweiten Tag mit den folgenden Filtern anspricht:

- App erstmals vor mehr als 1 Tag verwendet
- App erstmals vor weniger als 2 Tagen verwendet

Die Zustellung nach Ortszeit kann Nutzer:innen in diesem Segment verfehlen, abhängig von der Zustellzeit und der Ortszeit der Nutzer:innen. Das liegt daran, dass eine Nutzer:in das Segment verlassen kann, bevor ihre Zeitzone die Zustellung auslöst.

### Welche Änderungen kann ich an geplanten Campaigns vor dem Start vornehmen? {#what-changes-can-i-make-to-scheduled-campaigns-ahead-of-launch}

Wenn die Campaign geplant ist, müssen Sie alle Bearbeitungen außer der Nachrichtenkomposition vornehmen, bevor wir die Nachrichten zum Versand einreihen. Wie bei allen Campaigns können Sie Konversions-Events nach dem Start nicht mehr bearbeiten.

### Ich habe meine geplante Campaign aktualisiert. Warum wurde sie nicht gestartet? {#i-updated-my-scheduled-campaign-why-didnt-it-launch}

Dies kann passieren, wenn eine Campaign genau zu dem Zeitpunkt gestartet werden soll, zu dem sie aktualisiert wurde. Wenn es beispielsweise gerade 15:10 Uhr ist und Sie die Campaign auf 15:10 Uhr geändert und **Campaign aktualisieren** ausgewählt haben, ist es jetzt nach 15:10 Uhr, was bedeutet, dass die geplante Startzeit bereits verstrichen ist. Anstatt die Campaign für dieselbe Uhrzeit zu planen, wählen Sie **Senden, sobald die Campaign gestartet wird**.

### Was ist die „Sicherheitszone“ bevor Nachrichten einer geplanten Campaign eingereiht werden? {#what-is-the-safe-zone-before-messages-on-a-scheduled-campaign-are-enqueued}

Wir empfehlen, Änderungen an Nachrichten innerhalb der folgenden Zeiträume vorzunehmen:

- **Einmalig geplante Campaigns:** Bearbeiten Sie bis zum geplanten Sendezeitpunkt.
- **Wiederkehrend geplante Campaigns:** Bearbeiten Sie bis zum geplanten Sendezeitpunkt.
- **Ortszeit-Campaigns:** Bearbeiten Sie bis zu 24 Stunden vor dem geplanten Sendezeitpunkt.
- **Campaigns mit optimalem Sendezeitpunkt:** Bearbeiten Sie bis zu 24 Stunden vor dem Tag, an dem die Campaign gesendet werden soll.

Wenn Sie Änderungen außerhalb dieser Empfehlungen vornehmen, werden die Aktualisierungen möglicherweise nicht in der gesendeten Nachricht widergespiegelt. Wenn Sie beispielsweise die Sendezeit drei Stunden vor einer um 12 Uhr Ortszeit geplanten Campaign ändern, kann Folgendes passieren:

- Braze sendet keine Nachrichten an Nutzer:innen, deren Sendezeit um mehr als eine Stunde überschritten ist.
- Bereits eingereihte Nachrichten können weiterhin zum ursprünglich eingereihten Zeitpunkt gesendet werden, nicht zum angepassten Zeitpunkt.

Wenn Sie Änderungen vornehmen müssen, empfehlen wir, die aktuelle Campaign zu stoppen (dadurch werden alle eingereihten Nachrichten abgebrochen). Sie können dann die Campaign duplizieren, die erforderlichen Änderungen vornehmen und die neue Campaign starten. Möglicherweise müssen Sie Nutzer:innen von dieser Campaign ausschließen, die die erste Campaign bereits erhalten haben. Stellen Sie sicher, dass Sie die Campaign-Zeitpläne anpassen, um den Zeitzonenversand zu berücksichtigen.

### Warum sind am Tag der Zeitumstellung keine Nutzer:innen in meine täglich geplante Campaign eingetreten? {#why-did-no-users-enter-my-daily-scheduled-campaign-on-daylight-saving-time-day}

An Tagen der Zeitumstellung (Sommerzeit/Winterzeit) können täglich geplante Campaigns je nachdem, ob die Uhren vor- oder zurückgestellt werden, bis zu eine Stunde früher oder später als gewöhnlich ausgeführt werden. Wenn Ihr Segment auf angepassten Attributen oder Events mit Zeitstempeln basiert, die innerhalb einer Stunde vor der geplanten Sendezeit liegen, qualifizieren sich diese Nutzer:innen am Tag der Zeitumstellung möglicherweise noch nicht, wenn die Campaign die Berechtigung auswertet.

Nehmen wir beispielsweise an, Nutzer:innen erhalten typischerweise eine Aktualisierung eines angepassten Attributs um 15 Uhr UTC, und Ihre Campaign läuft täglich um 10:30 Uhr in New York (Eastern Time). Während New York in der Standardzeit (UTC-5) ist, entspricht 10:30 Uhr ET 15:30 Uhr UTC, sodass die Campaign nach der Attributprotokollierung ausgeführt wird. Wenn New York zur Sommerzeit (UTC-4) wechselt, entspricht 10:30 Uhr ET 14:30 Uhr UTC, sodass die Campaign am Zeitumstellungstag vor der Attributaktualisierung um 15 Uhr UTC ausgeführt werden kann. Da das qualifizierende Attribut noch nicht existiert, werden diese Nutzer:innen herausgefiltert. Wenn die erneute Qualifikation deaktiviert ist, können Nutzer:innen, die an vorherigen Tagen eingetreten sind, nicht erneut eintreten, was zu null Eintritten an diesem Tag führt.

Um dies zu vermeiden, stellen Sie sicher, dass Ihre Aktualisierungen angepasster Attribute oder Events mehr als eine Stunde vor der geplanten Sendezeit der Campaign erfolgen.

### Warum stimmt die Anzahl der Nutzer:innen, die in eine Campaign eintreten, nicht mit der erwarteten Anzahl überein? {#why-does-the-number-of-users-entering-a-campaign-not-match-the-expected-number}

Die Anzahl der Nutzer:innen, die in eine Campaign eintreten, kann von Ihrer erwarteten Anzahl abweichen, je nachdem, wie Zielgruppen und Trigger ausgewertet werden. In Braze wird eine Zielgruppe vor dem Trigger ausgewertet (es sei denn, Sie verwenden einen [Attributänderungs-]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/attribute_triggers#change-custom-attribute-value)Trigger). Dies führt dazu, dass Nutzer:innen aus der Campaign herausfallen, wenn sie nicht anfänglich Teil Ihrer ausgewählten Zielgruppe sind, bevor Trigger-Aktionen ausgewertet werden.

{% alert tip %}
Wenn Sie weitere Unterstützung bei der Fehlerbehebung von Campaigns benötigen, wenden Sie sich bitte innerhalb von 30 Tagen nach Auftreten des Problems an den Braze-Support, da uns nur die Diagnoseprotokolle der letzten 30 Tage vorliegen.
{% endalert %}

### Warum haben Nutzer:innen meine Campaign zweimal erhalten, nachdem ich sie bearbeitet habe? {#why-did-users-receive-my-campaign-twice-after-i-edited-it}

Wenn Sie eine laufende Campaign bearbeiten, ohne sie vorher zu stoppen, können Nutzer:innen die Nachricht zweimal erhalten. Das passiert, weil die Bearbeitung einer laufenden Campaign Nutzer:innen für die aktualisierte Version erneut einreiht, während die ursprüngliche Warteschlange noch verarbeitet wird. Nutzer:innen, die die ursprüngliche Nachricht noch nicht erhalten haben, können in beiden Warteschlangen landen. Um dies zu verhindern, [stoppen Sie die Campaign]({{site.baseurl}}/user_guide/messaging/campaigns/manage_campaigns/change_your_campaign_after_launch#stopping-your-campaign) immer, bevor Sie Änderungen vornehmen.

### Was ist der Unterschied zwischen den Optionen „CSV-Export Nutzerdaten“ und „CSV-Export E-Mail-Adressen“ auf meiner Campaign-Analytics-Seite? {#what-is-the-difference-between-the-csv-export-user-data-and-csv-export-email-address-options-on-my-campaign-analytics-page}

Wenn Sie die Option **CSV-Export E-Mail-Adressen** auswählen, werden nur Daten für Nutzer:innen mit E-Mail-Adressen heruntergeladen. Wenn Sie beispielsweise ein Segment mit 100.000 Nutzer:innen haben, aber nur 50.000 davon E-Mail-Adressen haben, und Sie auf **CSV-Export E-Mail-Adressen** klicken, enthält der Export nur 50.000 Datenzeilen. Im Vergleich dazu exportiert **CSV-Export Nutzerdaten** alle Nutzerdaten.

### Kann ich nach einer Campaign anhand ihrer API-Kennung suchen? {#can-i-search-for-a-campaign-by-its-api-identifier}

Ja, verwenden Sie den Filter `api_id:YOUR_API_ID` auf der **Campaigns**-Seite, um nach einer Campaign anhand ihrer API-Kennung zu suchen. Weitere Informationen finden Sie unter [Campaigns suchen]({{site.baseurl}}/user_guide/messaging/campaigns/manage_campaigns/search_campaigns).

### Warum werden Leerzeichen in Eingabefeldern anders angezeigt als im dargestellten Text? {#why-does-whitespace-appear-differently-in-input-fields-versus-displayed-text}

Die Leerzeichenbehandlung unterscheidet sich zwischen Eingabefeldern und angezeigten Textkomponenten aufgrund des CSS-Stylings. In Textkomponenten mit dem Standard-CSS `white-space: normal` werden mehrere aufeinanderfolgende Leerzeichen bei der Anzeige zu einem einzigen Leerzeichen zusammengefasst. Dies ist das Standard-HTML-Verhalten für gerenderten Text.

Eingabefelder bewahren mehrere Leerzeichen genau so, wie Sie sie eingeben, da Sie den genauen Abstand für eine akkurate Dateneingabe sehen und bearbeiten müssen. Das bedeutet, dass Text mit mehreren Leerzeichen in einem Eingabefeld (wo alle Leerzeichen erhalten bleiben) anders aussehen kann als bei der Anzeige in anderen Teilen des Dashboards (wo CSS mehrere Leerzeichen zusammenfassen kann).

Wenn Sie beispielsweise einen Campaign-Namen oder einen UTM-Parameter mit mehreren Leerzeichen in ein Eingabefeld eingeben, sehen Sie alle Leerzeichen erhalten. Wenn derselbe Text jedoch in Suchergebnissen, Campaign-Listen oder anderen Textkomponenten erscheint, können mehrere Leerzeichen aufgrund der CSS-Leerzeichenbehandlung als ein einziges Leerzeichen erscheinen.

### Was ist der Unterschied zwischen API-Campaigns und API-getriggerten Campaigns? {#what-is-the-difference-between-api-campaigns-and-api-triggered-campaigns}

API-getriggerte Campaigns ermöglichen es Ihnen, Campaign-Texte, multivariates Testen und Regeln für die erneute Qualifikation im Braze-Dashboard zu verwalten, während die Zustellung dieses Inhalts von Ihren eigenen Servern und Systemen getriggert wird. Diese Nachrichten können auch zusätzliche Daten enthalten, die in Echtzeit in die Nachrichten eingebunden werden.

API-Campaigns werden verwendet, um die über die API gesendeten Nachrichten zu tracken. Im Gegensatz zu den meisten Campaigns legen Sie weder die Nachricht, noch die Empfänger:innen oder den Zeitplan fest, sondern übergeben die Bezeichner in Ihren API-Aufrufen.

### Wie kann ich bestätigen, ob meine Nutzer:innen eine API-getriggerte Campaign erhalten haben? {#how-can-i-confirm-if-my-users-received-an-api-triggered-campaign}

Sie können [ein Segment erstellen]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment), indem Sie den Filter **Campaign erhalten** verwenden und dann die spezifische API-getriggerte Campaign auswählen, die Sie überprüfen möchten. Nachdem Sie das Segment gespeichert haben, verwenden Sie den [`/users/export/segment`-Endpunkt]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment), um die Nutzer:innen in diesem Segment zu exportieren.

### Kann ich eine Campaign löschen? {#can-i-delete-a-campaign}

Nein, aber Sie können [eine Campaign archivieren]({{site.baseurl}}/user_guide/messaging/governance/archiving).

### Was ist der Unterschied zwischen aktionsbasierten und API-getriggerten Campaigns? {#what-is-the-difference-between-action-based-and-api-triggered-campaigns}

<style>
table th:nth-child(1) {
    width: 50%;
}
table th:nth-child(3) {
    width: 50%;
}
</style>

#### Aktionsbasiert {#action-based}

Campaigns mit aktionsbasierter Zustellung oder Event-getriggerte Campaigns sind sehr effektiv für transaktionsbezogene oder leistungsbasierte Nachrichten und ermöglichen es Ihnen, diese nach Abschluss eines bestimmten Events durch eine Nutzer:in auszulösen.

| Vorteile | Nachteile |
| ---- | ---- |
| • Sichtbarkeit eingehender JSON-Payloads in der Plattform (wenn das Event durch eine Testnutzer:in ausgelöst wird) über das **Nachrichtenaktivitätsprotokoll**<br><br>• Personalisierungselemente sind in den angepassten Event-Eigenschaften enthalten<br><br>• Angepasste Events können verwendet werden, um Segments von Nutzer:innen zu erstellen, die für die Nachricht berechtigt sind | • Verbraucht Datenpunkte |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Aktionsbasiert" }

#### API-getriggert {#api-triggered}

API-getriggerte und Server-getriggerte Campaigns sind ideal für fortgeschrittenere Transaktionen und ermöglichen es Ihnen, die Zustellung von Campaign-Inhalten von Ihren eigenen Servern und Systemen zu triggern. Die API-Anfrage zum Triggern der Nachricht kann auch zusätzliche Daten enthalten, die in Echtzeit in die Nachricht eingebunden werden.

| Vorteile | Hinweise |
| ---- | ---- |
| • Verbraucht keine Datenpunkte<br><br>• Personalisierungselemente sind in den JSON-Payload-Eigenschaften enthalten | • Ermöglicht es nicht, ein Segment von Nutzer:innen zu erstellen, die für die Nachricht in den JSON-Payload-Eigenschaften berechtigt sind<br><br>• Eingehende JSON-Payloads können nicht über das **Nachrichtenaktivitätsprotokoll** eingesehen werden |
{: .reset-td-br-1 .reset-td-br-2 aria-label="API-getriggert" }

### Was sollte ich bei der Einreichung eines Support-Tickets für einen „Request Timed Out“-Fehler angeben? {#what-should-i-include-when-submitting-a-support-ticket-for-a-request-timed-out-error}

Wenn Sie beim Erstellen oder Bearbeiten einer Campaign oder eines Canvas einen „Request Timed Out“-Fehler erhalten und den [Braze-Support]({{site.baseurl}}/user_guide/administer/personal/braze_support) kontaktieren müssen, geben Sie die folgenden Informationen an, um die Lösung zu beschleunigen:

{% multi_lang_include messaging/support_ticket_request_timed_out_details.md context='campaign' %}

### Warum stimmen meine Sende-Analytics nicht mit dem von mir festgelegten maximalen Empfängerlimit überein? {#why-dont-my-send-analytics-match-the-maximum-recipient-limit-i-set}

Wenn Sie ein maximales Empfängerlimit zu einer aktiven Campaign hinzufügen oder ändern, wird das Limit aus folgenden Gründen möglicherweise nicht in Ihren Sende-Analytics widergespiegelt:

- **Limit nach dem Start hinzugefügt:** Wenn das maximale Empfängerlimit nicht beim Start der Campaign festgelegt ist, werden Nachrichten, die bereits eingereiht sind, bevor Sie das Limit anwenden, trotzdem gesendet. Das Limit gilt nur für Sendungen, die Sie nach dem Speichern der Änderung einreihen.
- **Zusammenspiel mit Rate-Limiting:** Wenn eine Campaign auch einem Rate-Limit unterliegt, können Nachrichten über ein längeres Zeitfenster verteilt werden. Das maximale Empfängerlimit wird ausgewertet, wenn Nachrichten eingereiht werden, nicht wenn sie zugestellt werden. Wenn das Limit geändert wird, während Nachrichten bereits in der Warteschlange sind, gilt das ursprüngliche Limit für diese Nachrichten.
- **Wiederkehrende Campaigns:** Bei wiederkehrenden Campaigns wird das maximale Empfängerlimit für jeden geplanten Versand unabhängig ausgewertet. Das Ändern des Limits zwischen den Sendungen passt vorherige Sendezähler nicht rückwirkend an.

Um Abweichungen zu vermeiden, legen Sie das maximale Empfängerlimit vor dem Start der Campaign fest und vermeiden Sie Änderungen, während Sendungen laufen.

### Warum sind die Sendungen niedriger als die geschätzte Zielgruppengröße? {#why-are-sends-lower-than-the-estimated-audience-size}

Mehrere Faktoren können dazu führen, dass die Anzahl der Sendungen niedriger ist als die geschätzte Zielgruppengröße:

- **Aktionsbasierte Zustellung:** Nutzer:innen generieren Sendungen erst, nachdem sie den Trigger ausgeführt haben, sodass Sendungen sich über die Zeit ansammeln und hinter der vorab angezeigten Schätzung zurückbleiben können, die beim Erstellen der Campaign angezeigt wurde.
- **Zielgruppenänderungen nach dem Start:** Das Ändern von Eintritts- oder Zielfiltern nach dem Start kann dazu führen, dass die Momentaufnahme der **geschätzten Zielgruppe** nicht mehr mit den Nutzer:innen übereinstimmt, die sich bei späteren Sendungen noch qualifizieren (z. B. wenn Nutzer:innen nicht berechtigt sind, erneut einzutreten).
- **Zielgruppenpfad-Schritt:** Für Canvas sendet ein [Zielgruppenpfade]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths)-Schritt nur an Nutzer:innen, die dem höchstpriorisierten Branch entsprechen, für den sie sich qualifizieren, was die Sendungen im Vergleich zu einer flachen Segmentzählung reduzieren kann.
- **Kontrollgruppen:** Wenn eine [globale Kontrollgruppe]({{site.baseurl}}/user_guide/audience/global_control_group) oder eine Campaign-Kontrollgruppe verwendet wird, wird ein Teil der Zielgruppe von der Zustellung zurückgehalten.
- **Zustellzeitpunkt und -fenster:** Bei Ortszeit- oder geplanten Campaigns müssen Nutzer:innen sich sowohl zum Eintritts- als auch zum Sendezeitpunkt qualifizieren; Nutzer:innen in bestimmten Zeitzonen können außerhalb des Zustellfensters liegen.
- **E-Mail-Deduplizierung:** Ihre Campaign oder Ihr Canvas spricht mehrere Nutzer:innen mit übereinstimmenden E-Mail-Adressen an, sodass zum Sendezeitpunkt eine zufällige Nutzer:in mit dieser E-Mail-Adresse ausgewählt wird. Die Nachricht wird nur einmal gesendet und dedupliziert, damit sie nicht mehrfach an dieselbe E-Mail-Adresse gesendet wird, aber Ihre geschätzte Zielgruppengröße enthält alle Nutzer:innen.
- **E-Mail-Zustellbarkeitsfilter:** Bei E-Mail-Campaigns schließt Braze Nutzer:innen aus, die einen Hard-Bounce hatten, sich von E-Mails abgemeldet haben, als Spam markiert wurden, keine E-Mail-Adresse in ihrem Profil haben oder nicht bei einer erforderlichen Abo-Gruppe angemeldet sind. Diese Prüfungen erfolgen zum Sendezeitpunkt, sodass eine Nutzer:in, die in Ihrem Segment vorhanden ist, trotzdem von der tatsächlichen Sendezählung ausgeschlossen werden kann.
- **CSV-Import-Timing:** Wenn die Segmentzugehörigkeit durch [CSV-Import]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import) gepflegt wird, werden E-Mail-Adressen, die nach dem Versand einer geplanten Campaign hinzugefügt werden, von diesem Versand nicht erreicht. Da Braze keine Momentaufnahme der Segmentzugehörigkeit zum Sendezeitpunkt aufbewahrt, kann die aktuelle Segmentgröße die Anzahl der tatsächlich kontaktierten Nutzer:innen übersteigen.
- **Globales Frequency-Capping:** Workspace-weite Limits können verhindern, dass berechtigte Nutzer:innen im selben Zeitfenster eine weitere Nachricht erhalten, was die tatsächlichen Sendungen reduziert.
- **Neu importierte Nutzer:innen:** Profile, die gerade erst berechtigt wurden, erhalten die Nachricht möglicherweise erst bei der nächsten Auswertung oder dem nächsten Sendedurchlauf, sodass die Zählung bei einem späteren Durchlauf aufholt.
- **Push-Erreichbarkeit:** Bestätigen Sie bei Push-Campaigns, dass die Zielgruppe für die richtige App Push-aktiviert ist. Wenn Sie nicht nach Push-aktivierten Nutzer:innen filtern, kann die geschätzte Zielgruppe Profile enthalten, die kein Push empfangen können. Prüfen Sie **Erreichbare Nutzer:innen** im Schritt **Zielgruppe zusammenstellen** für eine genauere operative Schätzung.
- **Rate-Limiting:** Ein [Rate-Limit für die Zustellgeschwindigkeit]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting) begrenzt, wie viele Nachrichten Braze pro Minute während eines einzelnen Sendevorgangs versendet. Braze verteilt die Zustellung über ein längeres Fenster, sodass einige Sendungen verzögert werden, noch nicht in der Zählung erscheinen oder nicht abgeschlossen werden, wenn das Limit im Verhältnis zur berechtigten Zielgruppe niedrig ist.
- **Fenster für erneute Qualifikation:** Nutzer:innen, die noch nicht wieder qualifikationsberechtigt sind, erhalten die Nachricht während der Abklingzeit nicht erneut, sodass die Sendungen für diesen Zeitraum unter der geschätzten Zielgruppengröße liegen.
- **Berichtszeitraum:** Der Analytics-Zeitbereich umfasst möglicherweise nicht jeden Versand.
- **Segment-Neuauswertung:** Bei aktionsbasierten oder geplanten Campaigns, die zum Sendezeitpunkt erneut auswerten, qualifizieren sich Nutzer:innen, die beim Einreihen der Campaign im Segment waren, möglicherweise nicht mehr, wenn die Nachricht tatsächlich gesendet wird.
- **Sende-Limits:** Eine maximale Nutzer:innenanzahl (oder ein ähnliches Limit) unter **Zielgruppe zusammenstellen** stoppt die Zustellung, wenn das Limit erreicht ist.
- **Strenge Geräte- oder Browser-Filter:** Filter, die nur die neuesten App-Versionen oder Browser berücksichtigen, verkleinern die erreichbare Menge zum Sendezeitpunkt im Vergleich zu einer breiten Segmentvorschau.

### Wo finde ich häufig gestellte Fragen zum globalen Frequency-Capping? {#where-are-frequently-asked-questions-about-global-frequency-capping}

Für Fragen zu Kalendertagen, stillem Push, Webhooks, Canvas-Verhalten und verwandten Themen, siehe die [Häufig gestellten Fragen]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/faq) zu [Rate-Limiting und Frequency-Capping]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping).

### Warum hat meine Campaign sinkende Senderaten? {#why-is-my-campaign-experiencing-lower-send-rates}

Wenn Sie feststellen, dass Ihre täglich geplanten Campaigns im Laufe der Zeit an weniger Nutzer:innen senden, prüfen Sie Folgendes:

- **Prüfen Sie, ob die erneute Qualifikation aktiviert ist:** Ohne erneute Qualifikation sendet Braze jeder Nutzer:in nur einmal eine Nachricht. Bei täglich geplanten Campaigns sind nur Nutzer:innen berechtigt, die der Zielgruppe entsprechen und die Nachricht noch nicht erhalten haben. Da immer mehr Nutzer:innen die Nachricht erhalten, hat jeder spätere Versand weniger berechtigte Nutzer:innen, sodass das Sendevolumen sinkt.
- **Prüfen Sie, ob die Zielgruppe eine feste Mitgliedschaft hat:** Zielgruppen, die aus einer festen Nutzerliste erstellt wurden (z. B. ein [CSV-Import]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import), der als Segmentfilter verwendet wird), erhalten nicht automatisch neue Mitglieder. Ohne neue Eintritte kann sich das Sendevolumen nicht erholen, wenn Nutzer:innen bereits kontaktiert wurden.

Für [Rate-Limits für die Zustellgeschwindigkeit]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting) und andere Faktoren, die die Sendungen für einen einzelnen Vorgang verringern, siehe [Warum sind die Sendungen niedriger als die geschätzte Zielgruppengröße?](#why-are-sends-lower-than-the-estimated-audience-size).

### Warum können eindeutige Empfänger:innen die Sendungen bei E-Mail und SMS übersteigen? {#why-can-unique-recipients-exceed-sends-for-email-and-sms}

Bei E-Mail und SMS inkrementiert Braze **Eindeutige Empfänger:innen** vor dem ESP-Sendeversuch und inkrementiert **Sendungen** nach einer erfolgreichen ESP-Antwort. Permanente Fehler (wie ungültige E-Mail-Adressen) oder doppelte Adressen führen dazu, dass die eindeutigen Empfänger:innen die Sendungen übersteigen.

### Warum stimmt **Zuletzt gesendet** nicht mit meiner geplanten Sendezeit überein? {#why-doesnt-last-sent-match-my-scheduled-send-time}

Bei einer Campaign mit einem einzelnen geplanten Versand stimmt **Zuletzt gesendet** mit der Startzeit überein. Bei wiederkehrenden Campaigns mit aktiviertem **In Ortszeit senden** kann **Zuletzt gesendet** früher als die geplante Zeit erscheinen, da Sendungen an Nutzer:innen in früheren Zeitzonen (z. B. GMT vs. PST) vor der Workspace-Planzeit abgeschlossen werden.

### Warum zeigt eine gestoppte historische Campaign keine Metriken mehr auf der **Analytics**-Seite an? {#why-does-a-stopped-historical-campaign-no-longer-show-metrics-on-the-analytics-page}

Der Tab **Analytics** zeigt standardmäßig die letzten 90 Tage an. Wenn die Campaign zuletzt außerhalb dieses Fensters gesendet hat, können Metriken als null erscheinen, bis Sie den Datumsbereich auf der **Analytics**-Seite anpassen, um den Zeitraum einzuschließen, in dem die Campaign gesendet hat. Weitere Informationen finden Sie unter [Campaign-Analytics]({{site.baseurl}}/user_guide/analytics/reports/campaign_analytics).

**Interaktionsdaten wiederherstellen** stellt keine Campaign-Analytics wieder her. Es gilt nur für Retargeting-Filter und die Nutzer:innen-Interaktionshistorie. Weitere Informationen finden Sie unter [Messaging-Interaktionsdaten]({{site.baseurl}}/messaging_interaction_data).