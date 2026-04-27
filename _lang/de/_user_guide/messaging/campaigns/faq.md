---
nav_title: FAQ
article_title: FAQ zu Kampagnen
page_order: 10
page_type: FAQ
description: "Diese Seite bietet Antworten auf häufig gestellte Fragen zu Kampagnen."
tool: Campaigns

---

# Häufig gestellte Fragen

> Dieser Artikel bietet Antworten auf einige häufig gestellte Fragen zu Kampagnen.

### Wie erstelle ich eine Multichannel-Kampagne?

Um eine Multichannel-Kampagne zu erstellen, wählen Sie **Messaging** > **Campaigns**. Wählen Sie dann **Kampagne erstellen** > **Multichannel**. Von hier aus können Sie aus den folgenden Messaging-Kanälen wählen: Content-Cards, E-Mail, LINE, Push-Benachrichtigungen, SMS/MMS/RCS, Webhook oder WhatsApp.

### Kann ich meiner Multichannel-Kampagne eine Kontrollgruppe hinzufügen?

Nein, Kontrollgruppen in Kampagnen sind für Einkanal-Messaging gedacht, wie z. B. E-Mail A versus E-Mail B. Als Alternative können Sie [Canvas]({{site.baseurl}}/user_guide/messaging/canvas/) verwenden, um verschiedene Kanäle, Messaging-Inhalte und Zustellzeitpunkte zu testen.

### Welche Möglichkeiten gibt es, Kampagnen zu testen und zu optimieren?

Multivariate Kampagnen und Canvases mit mehreren Varianten sind ein guter Ausgangspunkt! Sie können beispielsweise eine [multivariate Kampagne]({{site.baseurl}}/user_guide/messaging/ab_testing/) durchführen, um eine Nachricht mit verschiedenen Texten oder Betreffzeilen zu testen. Canvases mit mehreren Varianten können helfen, ganze Workflows zu testen.

### Warum ist die Öffnungsrate meiner Kampagne gesunken?

Niedrige Öffnungsraten hängen nicht immer mit einem technischen Problem zusammen. Es kann Probleme mit dem E-Mail-Clipping geben, was zu einem fehlenden Tracking-Pixel führt. Es ist aber auch möglich, dass weniger Nutzer:innen ihre E-Mails öffnen, weil sich der Inhalt oder die Zielgruppengröße geändert hat.

### Wie werden Kampagnen-Zielgruppen ausgewertet?

Standardmäßig prüfen Kampagnen die Zielgruppen-Filter zum Zeitpunkt des Eintritts. Bei aktionsbasierten Kampagnen mit einer Verzögerung gibt es die Option, die Segment-Kriterien zum Sendezeitpunkt erneut auszuwerten, um sicherzustellen, dass die Nutzer:innen zum Zeitpunkt des Nachrichtenversands noch Teil der Zielgruppe sind.

### Warum gibt es einen Unterschied zwischen der Anzahl der eindeutigen Empfänger:innen und der Anzahl der Sendungen für eine bestimmte Kampagne oder ein Canvas?

Eine mögliche Erklärung könnte sein, dass bei der Kampagne oder dem Canvas die erneute Berechtigung aktiviert ist, was bedeutet, dass Nutzer:innen, die für das Segment und die Zustellungseinstellungen qualifiziert sind, die Nachricht mehr als einmal erhalten können. Wenn die erneute Berechtigung nicht aktiviert ist, liegt die wahrscheinliche Erklärung für den Unterschied zwischen Sendungen und eindeutigen Empfänger:innen darin, dass Nutzer:innen mehrere Geräte über verschiedene Plattformen hinweg mit ihren Profilen verknüpft haben.

Wenn Sie beispielsweise ein Canvas haben, das sowohl iOS- als auch Web-Push-Benachrichtigungen enthält, kann eine bestimmte Nutzerin oder ein bestimmter Nutzer mit sowohl Mobil- als auch Desktop-Geräten mehr als eine Nachricht erhalten.

### Warum kann die Anzahl der Conversions die Anzahl der eindeutigen Nutzer:innen bei Multichannel-Kampagnen übersteigen?

Bei Multichannel-Kampagnen zählt Braze Conversions pro Kanal, nicht pro Nutzer:in. Wenn eine Nutzerin oder ein Nutzer eine einzelne Conversion-Aktion innerhalb des Conversion-Fensters durchführt, ordnet Braze diese Conversion jedem Kanal zu, über den die Person eine Nachricht erhalten hat. Das bedeutet: Wenn eine Nutzerin oder ein Nutzer Nachrichten über mehrere Kanäle erhält (z. B. sowohl E-Mail als auch Push) und konvertiert, zählt Braze mehrere Conversions – eine für jeden Kanal. Dadurch kann die Gesamtzahl der Conversions die Anzahl der eindeutigen Nutzer:innen übersteigen, die konvertiert haben.

Wenn beispielsweise eine Multichannel-Kampagne sowohl eine E-Mail als auch eine Push-Benachrichtigung an eine Nutzerin oder einen Nutzer sendet und diese Person nach dem Erhalt beider Nachrichten und innerhalb des Conversion-Fensters eine Conversion-Aktion durchführt, zählt Braze dies als zwei Conversions – eine der E-Mail und eine dem Push zugeordnet – obwohl es sich um eine einzelne Aktion derselben Person handelt.

### Warum hat meine Kampagne eine kleinere erreichbare Nutzerbasis als das Segment, das ich für die Kampagne verwende?

Wenn Sie eine [Globale Kontrollgruppe]({{site.baseurl}}/user_guide/audience/global_control_group/) eingerichtet haben, verhindert diese, dass ein Prozentsatz Ihrer erreichbaren Zielgruppe Kampagnen erhält. Das bedeutet, dass die Anzahl der erreichbaren Nutzer:innen für Ihr Segment manchmal größer sein kann als die Anzahl der erreichbaren Nutzer:innen für Ihre Kampagne, selbst wenn die Kampagne dasselbe Segment verwendet.

### Was bietet die Zustellung nach Ortszeit?

Die Zustellung nach Ortszeit ermöglicht es Ihnen, Messaging-Kampagnen basierend auf der individuellen Zeitzone der Nutzer:innen an ein Segment zuzustellen. Ohne Zustellung nach Ortszeit werden Kampagnen basierend auf den Zeitzonen-Einstellungen Ihres Unternehmens in Braze geplant.

Beispielsweise würde ein in London ansässiges Unternehmen, das eine Kampagne um 12 Uhr mittags sendet, Nutzer:innen an der Westküste Amerikas um 4 Uhr morgens erreichen. Wenn Ihre App nur in bestimmten Ländern verfügbar ist, stellt dies möglicherweise kein Risiko für Sie dar. Andernfalls empfehlen wir dringend, das Senden von Push-Benachrichtigungen in den frühen Morgenstunden an Ihre Nutzerbasis zu vermeiden.

### Wie erkennt Braze die Zeitzone einer Nutzerin oder eines Nutzers?

Braze ermittelt die Zeitzone automatisch anhand des Geräts. Dies gewährleistet Zeitzonen-Genauigkeit und vollständige Abdeckung Ihrer Nutzer:innen. Nutzer:innen, die über die User API oder anderweitig ohne Zeitzone erstellt wurden, haben die Zeitzone Ihres Unternehmens als Standard-Zeitzone, bis sie in Ihrer App durch das SDK erkannt werden.

Sie können die Zeitzone Ihres Unternehmens in Ihren [Unternehmenseinstellungen]({{site.baseurl}}/user_guide/administer/global/admin_settings/) im Dashboard überprüfen.

### Wann wertet Braze Nutzer:innen für die Zustellung nach Ortszeit aus?

Braze wertet die Eintrittsberechtigung der Nutzer:innen aus zu:

- Samoa-Zeit (UTC+13) oder UTC+14 während der Sommerzeit
- Der Ortszeit des geplanten Tages

Damit eine Nutzerin oder ein Nutzer eintrittsberechtigt ist, muss sie oder er beide Prüfungen bestehen. Wenn beispielsweise ein Canvas am 7. August 2021 um 14 Uhr Ortszeit gestartet werden soll, erfordert das Targeting einer Nutzerin oder eines Nutzers in New York die folgenden Berechtigungsprüfungen:

- New York am 6. August 2021 um 21 Uhr
- New York am 7. August 2021 um 14 Uhr

Die Nutzerin oder der Nutzer muss 24 Stunden vor dem Start im Segment sein. Wenn die Nutzerin oder der Nutzer bei der ersten Prüfung nicht berechtigt ist, versucht Braze die zweite Prüfung nicht.

#### Beispiele

Wenn beispielsweise eine Kampagne für 19 Uhr UTC zugestellt werden soll, beginnen wir mit dem Einreihen der Kampagnensendungen, sobald eine Zeitzone identifiziert wird (z. B. Samoa). Das bedeutet, wir bereiten den Versand der Nachricht vor, senden die Kampagne aber noch nicht. Wenn Nutzer:innen bei der Berechtigungsprüfung keinen Filtern entsprechen, fallen sie nicht in die Zielgruppe.

Ein weiteres Beispiel: Angenommen, Sie möchten zwei Kampagnen erstellen, die am selben Tag gesendet werden sollen – eine morgens und eine abends – und einen Filter hinzufügen, dass Nutzer:innen die zweite Kampagne nur erhalten können, wenn sie die erste bereits erhalten haben. Bei der Zustellung nach Ortszeit erhalten einige Nutzer:innen möglicherweise die zweite Kampagne nicht. Das liegt daran, dass wir die Berechtigung prüfen, wenn die Zeitzone der Nutzerin oder des Nutzers identifiziert wird. Wenn der geplante Zeitpunkt in ihrer Zeitzone noch nicht eingetreten ist, haben sie die erste Kampagne noch nicht erhalten und sind daher nicht für die zweite Kampagne berechtigt.

Eine visuelle Darstellung, wie eine Nutzerin oder ein Nutzer bei der ersten Prüfung im Segment sein kann, aber nicht bei der zweiten, finden Sie in dieser Zeitleiste:

![Zeitleiste, die zeigt, wie eine Nutzerin oder ein Nutzer vor der ersten Prüfung in das Segment eintritt und es dann vor der zweiten Prüfung wieder verlässt.]({% image_buster /assets/img/local_time_zone_diagram.png %})

{% details Beschreibung der Zeitleiste %}

1. Nutzer:in A tritt um 6:59 PST (4:59 Samoa-Zeit) in das Segment ein.
2. Braze prüft um 7 Uhr Samoa-Zeit die Segment-Zugehörigkeit, um festzustellen, welche Nutzer:innen in den nächsten 24 Stunden berechtigt sind, die Kampagne zu erhalten. Nutzer:in A ist zu diesem Zeitpunkt im Segment.
3. Das Segment hat ein 24-Stunden-Fenster, daher verlässt Nutzer:in A das Segment 24 Stunden nach dem Beitritt: 6:59 PST (4:59 Samoa-Zeit).
4. Die Ortszeit-Kampagne wird um 7 PST gesendet, aber Nutzer:in A hat das Segment bereits verlassen.

{% enddetails %}

### Wie plane ich eine Kampagne mit Ortszeit?

Wenn Sie eine Kampagne planen, wählen Sie den Versand zu einem bestimmten Zeitpunkt und dann **Kampagne an Nutzer:innen in ihrer Ortszeit senden**.

Braze empfiehlt dringend, alle Ortszeit-Kampagnen 24 Stunden im Voraus zu planen. Da eine solche Kampagne über einen ganzen Tag hinweg gesendet werden muss, stellt die Planung 24 Stunden im Voraus sicher, dass Ihre Nachricht Ihr gesamtes Segment erreicht. Sie können diese Kampagnen jedoch bei Bedarf auch weniger als 24 Stunden im Voraus planen. Beachten Sie, dass Braze keine Nachrichten an Nutzer:innen sendet, die den Sendezeitpunkt um mehr als 1 Stunde verpasst haben.

Wenn es beispielsweise 13 Uhr ist und Sie eine Ortszeit-Kampagne für 15 Uhr planen, wird die Kampagne sofort an alle Nutzer:innen gesendet, deren Ortszeit zwischen 15 und 16 Uhr liegt, aber nicht an Nutzer:innen, deren Ortszeit 17 Uhr ist. Außerdem darf der von Ihnen gewählte Sendezeitpunkt in der Zeitzone Ihres Unternehmens noch nicht verstrichen sein.

Das Bearbeiten einer Ortszeit-Kampagne, die weniger als 24 Stunden im Voraus geplant ist, ändert den Zeitplan der Nachricht nicht. Wenn Sie sich entscheiden, eine Ortszeit-Kampagne auf einen späteren Zeitpunkt zu verschieben (z. B. 19 Uhr statt 18 Uhr), erhalten Nutzer:innen, die zum ursprünglichen Sendezeitpunkt im Zielsegment waren, die Nachricht weiterhin zum ursprünglichen Zeitpunkt (18 Uhr). Wenn Sie eine Ortszeit-Kampagne auf einen früheren Zeitpunkt verschieben (z. B. 16 Uhr statt 17 Uhr), wird die Kampagne trotzdem an alle Segment-Mitglieder zum ursprünglichen Zeitpunkt (17 Uhr) gesendet.

{% alert note %}
Bei Canvas-Komponenten müssen Nutzer:innen nicht 24 Stunden in der Komponente sein, um die nächste Komponente in der User Journey bei der Zustellung nach Ortszeit zu erhalten.
{% endalert %}

Wenn Sie Nutzer:innen erlaubt haben, erneut für die Kampagne berechtigt zu werden, erhalten sie diese erneut zum ursprünglichen Zeitpunkt (17 Uhr). Bei allen nachfolgenden Vorkommen Ihrer Kampagne werden Ihre Nachrichten jedoch nur zum aktualisierten Zeitpunkt gesendet.

### Wann werden Änderungen an Ortszeit-Kampagnen wirksam?

Zielsegmente für Ortszeit-Kampagnen sollten mindestens ein 48-Stunden-Fenster für zeitbasierte Filter enthalten, um die Zustellung an das gesamte Segment zu gewährleisten. Betrachten Sie beispielsweise ein Segment, das Nutzer:innen an ihrem zweiten Tag mit den folgenden Filtern anspricht:

- App erstmals vor mehr als 1 Tag verwendet
- App erstmals vor weniger als 2 Tagen verwendet

Die Zustellung nach Ortszeit kann Nutzer:innen in diesem Segment verfehlen, abhängig vom Zustellzeitpunkt und der Ortszeit der Nutzer:innen. Dies liegt daran, dass eine Nutzerin oder ein Nutzer das Segment verlassen kann, bevor ihre oder seine Zeitzone die Zustellung auslöst.

### Welche Änderungen kann ich an geplanten Kampagnen vor dem Start vornehmen?

Wenn die Kampagne geplant ist, müssen Sie Änderungen an allem außer der Nachrichtenkomposition vornehmen, bevor wir die Nachrichten zum Senden einreihen. Wie bei allen Kampagnen können Sie Konversions-Events nach dem Start nicht mehr bearbeiten.

### Ich habe meine geplante Kampagne aktualisiert. Warum wurde sie nicht gestartet?

Dies kann passieren, wenn eine Kampagne genau zu dem Zeitpunkt gestartet werden soll, zu dem sie aktualisiert wurde. Wenn es beispielsweise gerade 15:10 Uhr ist und Sie die Kampagne auf 15:10 Uhr geändert und **Kampagne aktualisieren** ausgewählt haben, ist es jetzt nach 15:10 Uhr, was bedeutet, dass der geplante Startzeitpunkt bereits verstrichen ist. Anstatt die Kampagne für denselben Zeitpunkt zu planen, wählen Sie **Senden, sobald die Kampagne gestartet wird**.

### Was ist die „sichere Zone", bevor Nachrichten einer geplanten Kampagne eingereiht werden?

Wir empfehlen, Änderungen an Nachrichten innerhalb der folgenden Zeiten vorzunehmen:

- **Einmalig geplante Kampagnen:** Bearbeiten Sie bis zum geplanten Sendezeitpunkt.
- **Wiederkehrend geplante Kampagnen:** Bearbeiten Sie bis zum geplanten Sendezeitpunkt.
- **Ortszeit-Kampagnen:** Bearbeiten Sie bis zu 24 Stunden vor dem geplanten Sendezeitpunkt.
- **Kampagnen mit optimalem Sendezeitpunkt:** Bearbeiten Sie bis zu 24 Stunden vor dem Tag, an dem die Kampagne gesendet werden soll.

Wenn Sie Änderungen außerhalb dieser Empfehlungen vornehmen, werden die Aktualisierungen möglicherweise nicht in der gesendeten Nachricht widergespiegelt. Wenn Sie beispielsweise den Sendezeitpunkt drei Stunden vor dem geplanten Versand einer Kampagne um 12 Uhr Ortszeit ändern, kann Folgendes passieren:

- Braze sendet keine Nachrichten an Nutzer:innen, die den Sendezeitpunkt um mehr als eine Stunde verpasst haben.
- Bereits eingereihte Nachrichten werden möglicherweise weiterhin zum ursprünglich eingereihten Zeitpunkt gesendet, nicht zum angepassten Zeitpunkt.

Wenn Sie Änderungen vornehmen müssen, empfehlen wir, die aktuelle Kampagne zu stoppen (dies storniert alle eingereihten Nachrichten). Sie können dann die Kampagne duplizieren, die erforderlichen Änderungen vornehmen und die neue Kampagne starten. Möglicherweise müssen Sie Nutzer:innen von dieser Kampagne ausschließen, die die erste Kampagne bereits erhalten haben. Stellen Sie sicher, dass Sie die Kampagnen-Zeitpläne neu anpassen, um den Zeitzonen-Versand zu berücksichtigen.

### Warum sind an einem Tag mit Zeitumstellung keine Nutzer:innen in meine täglich geplante Kampagne eingetreten?

An Tagen mit Zeitumstellung (Sommerzeit/Winterzeit) können täglich geplante Kampagnen bis zu eine Stunde früher oder später als üblich ausgeführt werden, je nachdem, ob die Uhren vor- oder zurückgestellt werden. Wenn Ihr Segment auf angepassten Attributen oder Events mit Zeitstempeln basiert, die innerhalb einer Stunde des geplanten Sendezeitpunkts liegen, sind diese Nutzer:innen möglicherweise noch nicht qualifiziert, wenn die Kampagne am Tag der Zeitumstellung die Berechtigung auswertet.

Angenommen, Nutzer:innen erhalten typischerweise ein Update eines angepassten Attributs um 15 Uhr UTC, und Ihre Kampagne läuft täglich um 10:30 Uhr in New York (Eastern Time). Während New York in der Standardzeit (UTC-5) ist, entspricht 10:30 Uhr ET 15:30 Uhr UTC, sodass die Kampagne nach der Protokollierung des Attributs läuft. Wenn New York zur Sommerzeit (UTC-4) wechselt, entspricht 10:30 Uhr ET 14:30 Uhr UTC, sodass die Kampagne am Tag der Zeitumstellung vor dem Attribut-Update um 15 Uhr UTC laufen kann. Da das qualifizierende Attribut noch nicht existiert, werden diese Nutzer:innen herausgefiltert. Wenn die erneute Berechtigung deaktiviert ist, können Nutzer:innen, die an vorherigen Tagen eingetreten sind, nicht erneut eintreten, was zu null Eintritten für diesen Tag führt.

Um dies zu vermeiden, stellen Sie sicher, dass Ihre Updates angepasster Attribute oder Events mehr als eine Stunde vor dem geplanten Sendezeitpunkt der Kampagne erfolgen.

### Warum stimmt die Anzahl der Nutzer:innen, die in eine Kampagne eintreten, nicht mit der erwarteten Anzahl überein?

Die Anzahl der Nutzer:innen, die in eine Kampagne eintreten, kann von Ihrer erwarteten Anzahl abweichen, da Zielgruppen und Trigger unterschiedlich ausgewertet werden. In Braze wird eine Zielgruppe vor dem Trigger ausgewertet (es sei denn, es wird ein [Änderung eines Attributs]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/attribute_triggers#change-custom-attribute-value)-Trigger verwendet). Dies führt dazu, dass Nutzer:innen aus der Kampagne herausfallen, wenn sie nicht zunächst Teil Ihrer ausgewählten Zielgruppe sind, bevor Trigger-Aktionen ausgewertet werden.

{% alert tip %}
Für weitere Unterstützung bei der Fehlerbehebung von Kampagnen wenden Sie sich bitte innerhalb von 30 Tagen nach Auftreten Ihres Problems an den Braze-Support, da uns nur die Diagnoseprotokolle der letzten 30 Tage zur Verfügung stehen.
{% endalert %}

### Was ist der Unterschied zwischen den Optionen „Nutzerdaten als CSV exportieren" und „E-Mail-Adressen als CSV exportieren" auf meiner Kampagnen-Analytics-Seite?

Die Auswahl der Option **E-Mail-Adressen als CSV exportieren** lädt nur Daten für Nutzer:innen mit E-Mail-Adressen herunter. Wenn Sie beispielsweise ein Segment von 100.000 Nutzer:innen haben, aber nur 50.000 davon E-Mail-Adressen haben, und Sie auf **E-Mail-Adressen als CSV exportieren** klicken, enthält der Export nur 50.000 Datenzeilen. Im Vergleich dazu exportiert die Auswahl von **Nutzerdaten als CSV exportieren** alle Nutzerdaten.

### Kann ich nach einer Kampagne anhand ihres API-Bezeichners suchen?

Ja, verwenden Sie den Filter `api_id:YOUR_API_ID` auf der Seite **Campaigns**, um nach einer Kampagne anhand ihres API-Bezeichners zu suchen. Weitere Informationen finden Sie unter [Kampagnen suchen]({{site.baseurl}}/user_guide/messaging/campaigns/manage_campaigns/search_campaigns/).

### Warum werden Leerzeichen in Eingabefeldern anders angezeigt als im dargestellten Text?

Die Behandlung von Leerzeichen unterscheidet sich zwischen Eingabefeldern und dargestellten Textkomponenten aufgrund von CSS-Styling. In Textkomponenten mit der Standard-CSS-Eigenschaft `white-space: normal` werden mehrere aufeinanderfolgende Leerzeichen bei der Anzeige zu einem einzigen Leerzeichen zusammengefasst. Dies ist das Standard-HTML-Verhalten für gerenderten Text.

Eingabefelder bewahren mehrere Leerzeichen genau so, wie Sie sie eingeben, da Sie die exakten Abstände für eine genaue Dateneingabe sehen und bearbeiten müssen. Das bedeutet, dass Text mit mehreren Leerzeichen unterschiedlich aussehen kann, wenn er in einem Eingabefeld angezeigt wird (wo alle Leerzeichen erhalten bleiben) im Vergleich zur Anzeige in anderen Teilen des Dashboards (wo CSS mehrere Leerzeichen zusammenfassen kann).

Wenn Sie beispielsweise einen Kampagnennamen oder UTM-Parameter mit mehreren Leerzeichen in ein Eingabefeld eingeben, sehen Sie alle Leerzeichen erhalten. Wenn derselbe Text jedoch in Suchergebnissen, Kampagnenlisten oder anderen Textkomponenten erscheint, können mehrere Leerzeichen aufgrund der CSS-Leerzeichenbehandlung als ein einziges Leerzeichen erscheinen.

### Was ist der Unterschied zwischen API-Kampagnen und API-getriggerten Kampagnen?

API-getriggerte Kampagnen ermöglichen es Ihnen, Kampagnentexte, multivariate Tests und Regeln zur erneuten Berechtigung im Braze-Dashboard zu verwalten, während Sie die Zustellung dieser Inhalte von Ihren eigenen Servern und Systemen aus triggern. Diese Nachrichten können auch zusätzliche Daten enthalten, die in Echtzeit in die Nachrichten eingebunden werden.

API-Kampagnen werden verwendet, um über die API gesendete Nachrichten zu tracken. Im Gegensatz zu den meisten Kampagnen geben Sie nicht die Nachricht, die Empfänger:innen oder den Zeitplan an, sondern übergeben die Bezeichner in Ihren API-Aufrufen.

### Was ist der Unterschied zwischen aktionsbasierten und API-getriggerten Kampagnen?

<style>
table th:nth-child(1) {
    width: 50%;
}
table th:nth-child(3) {
    width: 50%;
}
</style>

#### Aktionsbasiert

Aktionsbasierte Zustellungskampagnen oder Event-getriggerte Kampagnen sind sehr effektiv für transaktionale oder erfolgsbasierte Nachrichten und ermöglichen es Ihnen, den Versand auszulösen, nachdem eine Nutzerin oder ein Nutzer ein bestimmtes Event abgeschlossen hat.

| Vorteile | Nachteile |
| ---- | ---- |
| • Sichtbarkeit eingehender JSON-Payloads in der Plattform (wenn das Event von einer Testnutzerin oder einem Testnutzer getriggert wird) über das **Nachrichten-Aktivitätsprotokoll**<br><br>• Personalisierungselemente sind in den angepassten Event-Eigenschaften enthalten<br><br>• Angepasste Events können verwendet werden, um Segmente von Nutzer:innen zu erstellen, die für die Nachricht berechtigt sind | • Verbraucht Datenpunkte |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### API-getriggert

API-getriggerte und servergetriggerte Kampagnen sind ideal für die Handhabung komplexerer Transaktionen und ermöglichen es Ihnen, die Zustellung von Kampagneninhalten von Ihren eigenen Servern und Systemen aus zu triggern. Die API-Anfrage zum Triggern der Nachricht kann auch zusätzliche Daten enthalten, die in Echtzeit in die Nachricht eingebunden werden.

| Vorteile | Hinweise |
| ---- | ---- |
| • Verbraucht keine Datenpunkte<br><br>• Personalisierungselemente sind in den JSON-Payload-Eigenschaften enthalten | • Ermöglicht es nicht, ein Segment von Nutzer:innen zu erstellen, die für die Nachricht in den JSON-Payload-Eigenschaften berechtigt sind<br><br>• Eingehende JSON-Payloads können nicht über das **Nachrichten-Aktivitätsprotokoll** eingesehen werden |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Was sollte ich angeben, wenn ich ein Support-Ticket für einen „Request Timed Out"-Fehler einreiche?

Wenn Sie beim Erstellen oder Bearbeiten einer Kampagne oder eines Canvas auf einen „Request Timed Out"-Fehler stoßen und den [Braze-Support]({{site.baseurl}}/braze_support/) kontaktieren müssen, geben Sie die folgenden Informationen an, um die Lösung zu beschleunigen:

- **Bildschirmaufnahme:** Eine Aufnahme der Schritte, die Sie vor dem Auftreten des Fehlers durchgeführt haben, einschließlich aller Seitenwechsel.
- **Zeitstempel und Zeitzone:** Der genaue Zeitpunkt, zu dem der Fehler aufgetreten ist, und Ihre Zeitzone.
- **Browser und Version:** Der Browser, den Sie verwenden (z. B. Chrome 120, Safari 17), und ob Sie versucht haben, den Fehler in einem anderen Browser zu reproduzieren.
- **Schritte zur Reproduktion:** Eine klare Beschreibung der Aktionen, die den Fehler auslösen, einschließlich aller spezifischen Kampagnen- oder Canvas-Einstellungen.
- **Netzwerkprotokolle (optional):** Öffnen Sie die Entwicklertools Ihres Browsers (Tab **Network**), reproduzieren Sie den Fehler und exportieren Sie das Netzwerkprotokoll als HAR-Datei (HTTP Archive). Dies hilft dem Support-Team zu identifizieren, welcher API-Aufruf das Timeout verursacht.

### Warum stimmen meine Sende-Analytics nicht mit dem von mir festgelegten maximalen Empfängerlimit überein?

Wenn Sie ein maximales Empfängerlimit zu einer aktiven Kampagne hinzufügen oder ändern, wird das Limit aus folgenden Gründen möglicherweise nicht in Ihren Sende-Analytics widergespiegelt:

- **Limit nach dem Start hinzugefügt:** Wenn das maximale Empfängerlimit beim Start der Kampagne nicht festgelegt ist, werden Nachrichten, die bereits vor der Anwendung des Limits eingereiht wurden, trotzdem gesendet. Das Limit gilt nur für Sendungen, die Sie nach dem Speichern der Änderung einreihen.
- **Interaktion mit Rate-Limiting:** Wenn eine Kampagne auch Rate-Limiting unterliegt, können Nachrichten über ein längeres Zeitfenster verteilt werden. Das maximale Empfängerlimit wird beim Einreihen der Nachrichten ausgewertet, nicht bei der Zustellung. Wenn das Limit geändert wird, während sich Nachrichten bereits in der Warteschlange befinden, gilt das ursprüngliche Limit für diese Nachrichten.
- **Wiederkehrende Kampagnen:** Bei wiederkehrenden Kampagnen wertet jeder geplante Versand das maximale Empfängerlimit unabhängig aus. Eine Änderung des Limits zwischen den Sendungen passt die vorherigen Sendezahlen nicht rückwirkend an.

Um Abweichungen zu vermeiden, legen Sie das maximale Empfängerlimit vor dem Start der Kampagne fest und vermeiden Sie Änderungen, während Sendungen in Bearbeitung sind.

### Warum sind die Sendungen niedriger als die geschätzte Zielgruppengröße?

Mehrere Faktoren können dazu führen, dass die Anzahl der Sendungen niedriger ist als die geschätzte Zielgruppengröße:

- **Segment-Neubewertung:** Bei aktionsbasierten oder geplanten Kampagnen, die zum Sendezeitpunkt neu ausgewertet werden, sind Nutzer:innen, die beim Einreihen der Kampagne im Segment waren, möglicherweise nicht mehr qualifiziert, wenn die Nachricht tatsächlich gesendet wird.
- **Kontrollgruppen:** Wenn eine [Globale Kontrollgruppe]({{site.baseurl}}/user_guide/audience/global_control_group/) oder eine Kontrollgruppe auf Kampagnenebene verwendet wird, wird ein Teil der Zielgruppe von der Zustellung ausgeschlossen.
- **Zustellzeitpunkt und -fenster:** Bei Ortszeit- oder geplanten Kampagnen müssen Nutzer:innen sowohl zum Eintritts- als auch zum Sendezeitpunkt qualifiziert sein; Nutzer:innen in bestimmten Zeitzonen können außerhalb des Zustellfensters liegen.
- **Rate-Limiting:** Wenn Rate-Limiting angewendet wird, werden Nachrichten über die Zeit verteilt und einige Sendungen können verzögert werden oder noch nicht in der Zählung berücksichtigt sein.
- **E-Mail-Zustellbarkeitsfilter:** Bei E-Mail-Kampagnen schließt Braze Nutzer:innen aus, die einen Hard-Bounce hatten, sich von E-Mails abgemeldet haben, als Spam markiert wurden, keine E-Mail-Adresse in ihrem Profil haben oder nicht bei einer erforderlichen Abo-Gruppe angemeldet sind. Diese Prüfungen werden zum Sendezeitpunkt durchgeführt, sodass eine Nutzerin oder ein Nutzer, die oder der in Ihrem Segment vorhanden ist, trotzdem von der tatsächlichen Sendezählung ausgeschlossen werden kann.