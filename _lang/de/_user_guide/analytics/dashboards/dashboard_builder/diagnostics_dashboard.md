---
nav_title: Messaging-Diagnose-Dashboard
article_title: Messaging-Diagnose-Dashboard
description: "Dieser Referenzartikel behandelt das Messaging-Diagnose-Dashboard, das Ihnen hilft zu verstehen, warum Nachrichten aus Ihren Campaigns oder Canvases möglicherweise nicht wie erwartet gesendet wurden."
alias: /ccdd/
page_order: 2
toc_headers: h2
---

# Messaging-Diagnose-Dashboard {#messaging-diagnostics-dashboard}

> Das **Messaging-Diagnose**-Dashboard bietet eine allgemeine Aufschlüsselung der Ergebnisse beim Nachrichtenversand, mit der Sie Trends erkennen und potenzielle Probleme in Ihrem Messaging-Setup diagnostizieren können. Dieses Dashboard kann Ihnen helfen zu verstehen, warum Nachrichten aus Ihren Campaigns oder Canvases möglicherweise nicht wie erwartet gesendet wurden.

{% alert important %}
Das **Messaging-Diagnose**-Dashboard befindet sich derzeit im Early Access. Kontaktieren Sie Ihren Customer-Success-Manager, wenn Sie an der Teilnahme am Early Access interessiert sind.
{% endalert %}

## Wichtige Konzepte {#key-concepts}

### Gesendet und zugestellt {#sent-and-delivered}

Es ist wichtig zu verstehen, dass dieses Dashboard darüber berichtet, wie Braze eine Nachricht intern verarbeitet hat – nicht über den endgültigen Zustellungsstatus der Nachricht.

Eine in diesem Dashboard als „gesendet“ markierte Nachricht bedeutet, dass Braze die Nachricht erfolgreich verarbeitet und versandt hat. Für die meisten Kanäle bedeutet dies, dass Braze die Nachricht an den entsprechenden Drittanbieter-Versandpartner übergeben hat. Es garantiert jedoch nicht die endgültige Zustellung an das Gerät der Nutzer:innen.

Wenn Braze eine Nachricht „sendet“, kann die endgültige Zustellung von externen Diensten abhängen. Betrachten Sie die folgenden Beispiele für jeden Kanal.

| Kanal | Beispiel für die endgültige Zustellung |
| --- | --- |
| Content Cards | Die Card wurde gesendet und ist zur Anzeige berechtigt. |
| E-Mail | Braze übergibt die Nachricht an einen E-Mail-Anbieter (ESP). Der ESP ist dann für die endgültige Zustellung verantwortlich. Dieser ESP kann beispielsweise einen „Bounce“ melden, wenn die E-Mail-Adresse ungültig ist oder das Postfach voll ist. |
| In-App-Nachrichten | Die Nachricht wurde den Nutzer:innen angezeigt. |
| LINE | Die Nachricht wurde erfolgreich an einen Versandpartner übergeben. |
| Push | Braze übergibt die Nachricht an den entsprechenden Push-Benachrichtigungsdienst (wie Apple Push Notification Service für iOS oder Firebase Cloud Messaging für Android). Dieser Dienst ist für die endgültige Zustellung der Benachrichtigung an das Gerät verantwortlich. |
| SMS/MMS/RCS | Braze übergibt die Nachricht an ein SMS-Gateway (wie Twilio). Dieses Gateway ist für die endgültige Zustellung an den Mobilfunkanbieter verantwortlich. |
| Webhooks | Die Webhook-Anfrage wurde erfolgreich durchgeführt und hat eine `2xx`-Antwort zurückgegeben. |
| WhatsApp | Die Nachricht wurde erfolgreich an einen Versandpartner übergeben. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Gesendet und zugestellt" }

### Datenaktualität {#data-freshness}

Die Häufigkeit, mit der die Daten in diesem Dashboard aktualisiert werden, kann je nach Systemlast variieren. Obwohl die Aktualisierungshäufigkeit nicht garantiert wird, beträgt sie in den meisten Fällen wahrscheinlich weniger als eine Stunde.

## Dashboard konfigurieren {#configuring-the-dashboard}

Sie können auf das Diagnose-Dashboard zugreifen, indem Sie zu **Analytics** > **Dashboard Builder** navigieren und **Messaging Diagnostics** aus der Liste der von Braze erstellten Dashboards auswählen.

Um das Dashboard auszuführen und Ihre Daten anzuzeigen:

1. Wählen Sie entweder **Campaigns** oder **Canvases** als Quelle für Ihre Dashboard-Berichte.
2. Wählen Sie eine oder mehrere Campaigns oder Canvases aus.
3. Wählen Sie **Run Dashboard**, um die Daten für Ihre ausgewählten Filter zu laden.

![Beispiel für Campaign- und Canvas-Diagnose vom 25. Mai bis 31. Mai 2025 für eine Willkommensserie-Campaign.]({% image_buster /assets/img/messaging_diagnostics_dashboard_details_log.png %}){: style="max-width:45%;"} ![Beispiel für Campaign- und Canvas-Diagnose mit Chart bei Hover vom 25. Mai bis 31. Mai 2025 für eine Willkommensserie-Campaign.]({% image_buster /assets/img/messaging_diagnostics_dashboard_drawer_expanded.png %}){: style="max-width:45%;"}

## Daten interpretieren {#interpreting-the-data}

{% alert note %}
Das Dashboard zeigt nur Daten der letzten sieben Tage an. Alle Zeitstempel werden in der Zeitzone Ihres Workspace angezeigt.
{% endalert %}

### Zusammenfassungskacheln {#summary-tiles}

Am oberen Rand der Seite befinden sich wichtige Zusammenfassungskacheln für Ihren ausgewählten Zeitraum, die Folgendes anzeigen:

- **Sent:** Die Gesamtanzahl der Nachrichten, die Braze erfolgreich verarbeitet und gesendet hat.
  - **E-Mail, SMS/MMS/RCS, WhatsApp, LINE und Push:** Die Nachricht wurde erfolgreich an einen Versandpartner übergeben.
  - **Webhooks:** Die Webhook-Anfrage wurde erfolgreich durchgeführt und hat eine `2xx`-Antwort zurückgegeben.
  - **Content Cards:** Die Card wurde gesendet und ist zur Anzeige berechtigt.
  - **In-App-Nachrichten:** Die Nachricht wurde den Nutzer:innen angezeigt.
- **Not Sent:** Die Gesamtanzahl der abgebrochenen Nachrichten. Dies umfasst Canvas-Zielgruppenmitglieder, die den Canvas nicht betreten haben oder den Canvas verlassen haben, weil bei einem Schritt ein Fehler aufgetreten ist oder sie die Ausstiegskriterien erfüllt haben, während sie ein Ausstiegs-Event ausgeführt haben.

### Nachrichtenergebnisse im Zeitverlauf {#message-outcomes-over-time}

Dieses Zeitreihen-Chart zeigt eine stündliche Aufschlüsselung, warum eine Nachricht abgebrochen oder warum Nutzer:innen aus einem Canvas entfernt wurden. Die Ergebnisbezeichnungen in diesem Chart sind normalisierte Dashboard-Bezeichnungen, keine Rohwerte aus dem Event-Payload. Dieses Chart zeigt nicht die Anzahl der Sends an.

### Detailliertes Protokoll der Nachrichtenergebnisse {#message-outcomes-granular-log}

Das Dashboard zeigt eine detaillierte Tabelle einzelner Nachrichtenergebnisse für Ihre ausgewählten Filter und den Zeitraum. Verwenden Sie diese Tabelle, um bestimmte Datensätze zu überprüfen, einschließlich Zeitstempel, Nutzer-ID, Canvas-Schritt, Ergebnis, Details und Kanal.

Sie können die Tabelle filtern, um sich auf bestimmte Datensätze zu konzentrieren:

- **Nach Ergebnis filtern:** Wählen Sie ein Ergebnis aus dem Ergebnisfilter, um nur Zeilen mit diesem Ergebnis anzuzeigen (z. B. `Frequency capped` oder `User not eligible for channel`).
- **Nach Nutzer-ID suchen:** Geben Sie eine Nutzer-ID in das Suchfeld ein, um Zeilen für diese bestimmten Nutzer:innen anzuzeigen.

Wenn Sie beide Filter anwenden, gibt die Tabelle Zeilen zurück, die sowohl dem ausgewählten Ergebnis als auch der eingegebenen Nutzer-ID entsprechen.

Wählen Sie eine Zeile in der Tabelle aus, um das Detailpanel zu öffnen. Das Detailpanel bietet zusätzlichen Kontext zu diesem Ergebnis, und Ask Operator liefert Hinweise zur Fehlerbehebung, um Ihnen bei der Diagnose des zugrunde liegenden Problems zu helfen.

![Detailliertes Protokoll der Messaging-Diagnose-Ergebnisse mit einer ausgewählten Zeile und Zugang zum Detailpanel.]({% image_buster /assets/img/messaging_diagnostics_dashboard_details_log.png %}){: style="max-width:45%;"} ![Erweitertes Detailpanel der Messaging-Diagnose mit Ergebniskontext und Hinweisen zur Fehlerbehebung.]({% image_buster /assets/img/messaging_diagnostics_dashboard_drawer_expanded.png %}){: style="max-width:45%;"}

{% alert note %}
Kanalfilter gelten für Ergebnisse, die an einen bestimmten Messaging-Kanal gebunden sind. Einige Ergebnisse sind kanalunabhängig und können daher auch in aggregierten Ansichten erscheinen, wenn Sie einen Kanalfilter anwenden.
{% endalert %}

### Abbruchergebnisse {#abort-outcomes}

Die folgenden Definitionen erklären die im Dashboard angezeigten Abbruchergebnisse. Die Ergebnisse sind nach Kategorien gruppiert, um das Auffinden des gesuchten Ergebnisses zu erleichtern.

{% alert note %}
Abbruchergebnisse in der Messaging-Diagnose sind lesbare Dashboard-Bezeichnungen. In [Currents-Nachrichten-Engagement-Events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) werden Abbruchinformationen mit Feldern wie `abort_type` und `abort_log` dargestellt. Da diese Datensätze unterschiedliche Darstellungen und Verarbeitungspfade haben, können Zählungen oder Bezeichnungen zwischen Currents und der Messaging-Diagnose abweichen.
{% endalert %}

#### Inhalt und Rendering {#content-and-rendering}

| Abbruchergebnis | Erklärung |
| ---- | ---- |
| Content-Card abgelaufen | Die Content-Card ist abgelaufen, bevor die Nutzer:innen sie gesehen haben. |
| Content-Card ungültig | Die Content-Card enthielt Fehler und wurde nicht an die Nutzer:innen gesendet. Einige häufige Gründe dafür sind: {::nomarkdown}<ul><li> Maximale Größe überschritten (2 KB) </li><li> Ablaufdatum ist ungültig </li><li> Nachricht enthält ungültige Zeichen </li></ul>{:/} |
| Connected-Content fehlgeschlagen | Braze hat versucht, die Nachricht zu senden, aber Connected-Content ist nach der maximalen Anzahl von Wiederholungsversuchen (Standard ist fünf) fehlgeschlagen. **Hinweis:** Diese Zahl stellt die Anzahl der Nachrichten dar, die aufgrund des Erreichens der maximalen Anzahl von Wiederholungsversuchen abgebrochen wurden, nicht die Gesamtanzahl der fehlgeschlagenen Connected-Content-Anfragen. |
| In-App-Nachrichten-Rendering-Timeout | Nach mehreren Wiederholungsversuchen konnte das Liquid nicht gerendert werden und es kam zu einem Timeout. |
| Liquid-Abbruch | Der [abort_message]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages)-Liquid-Tag wurde aufgerufen, sodass der Versand abgebrochen wurde. |
| Liquid-Rendering-Timeout | Das Rendern des Liquid-Templates hat zu lange gedauert. Tritt am häufigsten bei Bannern, In-App-Nachrichten und E-Mails auf. |
| Liquid-Syntaxfehler | Das Liquid-Template hatte einen Parsing-Fehler, sodass die Nachricht abgebrochen wurde. |
| Medien-URL fehlgeschlagen | Braze konnte die Medien-URL in der Nachricht nicht verarbeiten. Dies kann passieren, wenn die URL blockiert oder ungültig ist, ein Timeout auftritt, ein ungültiger HTTP-Status zurückgegeben wird oder die SSL-Validierung fehlschlägt. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Inhalt und Rendering" }

#### Campaign- und Canvas-Status {#campaign-and-canvas-state}

| Abbruchergebnis | Erklärung |
| ---- | ---- |
| Verzögerungsschritt fehlgeschlagen | Der [Verzögerungsschritt]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step#personalized-delays) ist fehlgeschlagen, wodurch die Nutzer:innen den Canvas verlassen haben. Dieser Fehler kann auftreten, wenn: {::nomarkdown}<ul><li> Die Variable, die dem personalisierten Verzögerungsschritt bereitgestellt wurde, leer oder ein ungültiger Typ war </li><li> Die Verzögerung die maximal zulässige Dauer innerhalb des Canvas überschreitet</li></ul>{:/} |
| Ausnahme- oder Ausstiegs-Event | Die Nutzer:innen waren zuvor berechtigt, die Nachricht zu erhalten, haben aber entweder {::nomarkdown}<ul><li> ein <a href="/docs/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery#step-3-select-exception-events">Ausnahme-Event</a> für eine aktionsbasierte Campaign ausgeführt, sodass die Nachricht abgebrochen wurde, oder </li><li> die Canvas-<a href="/docs/user_guide/messaging/canvas/create_a_canvas#setting-exit-criteria">Ausstiegskriterien</a> erfüllt, sodass sie mitten in der Journey entfernt wurden.</li></ul>{:/} |
| Inaktive Campaign | Die Campaign wurde gestoppt, während die Nachricht unterwegs war, sodass sie abgebrochen wurde. |
| Inaktiver Canvas | Der Canvas wurde gestoppt, bevor die Nutzer:innen die Journey betreten haben. |
| Inaktiver Canvas-Schritt | Dies kann im Canvas auftreten, wenn: {::nomarkdown}<ul><li> Der Canvas-Schritt gelöscht wurde </li> <li>Der Canvas gestoppt wurde, wodurch alle Schritte inaktiv werden </li></ul>{:/} |
| Volumenlimit erreicht | Die Campaign hat das festgelegte Volumenlimit erreicht, sodass der Versand abgebrochen wurde. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Campaign- und Canvas-Status" }

#### Rate-Limiting und Timing {#rate-limiting-and-timing}

| Abbruchergebnis | Erklärung |
| ---- | ---- |
| Frequency-Capping erreicht | Die Nutzer:innen haben bereits die maximale Anzahl an Nachrichten erhalten, die gemäß den [Frequency-Capping]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#about-frequency-capping)-Regeln Ihres Workspace zulässig sind, sodass der Versand abgebrochen wurde. |
| Ruhezeiten-Abbruch | Ruhezeiten waren für die Campaign oder den Canvas-Schritt aktiviert, wobei der Fallback auf **Nachricht abbrechen** eingestellt war. Die Nutzer:innen haben die Campaign getriggert oder den Canvas-Nachrichtenschritt während der Ruhezeiten betreten, sodass die Nachricht abgebrochen wurde. Dies führt jedoch nicht dazu, dass die Nutzer:innen den Canvas verlassen. |
| Rate-Limiting über 72 Stunden | Die Nachricht wurde aufgrund von [Rate-Limits für die Zustellgeschwindigkeit]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting) länger als 72 Stunden gedrosselt, sodass der Versand abgebrochen wurde. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Rate-Limiting und Timing" }

#### Nutzerberechtigung und Profil {#user-eligibility-and-profile}

| Abbruchergebnis | Erklärung |
| ---- | ---- |
| Doppelter Nutzerbezeichner | Mehrere Nutzer:innen mit einem übereinstimmenden Bezeichner (wie externe ID, E-Mail-Adresse, Telefonnummer) waren berechtigt, diese Nachricht zu erhalten. Um doppelte Sends an dieselben Nutzer:innen zu verhindern, wurde diese Nachricht abgebrochen. |
| Nutzer:innen haben Vorprüfung für Nachrichtenschritt nicht bestanden | Braze führt einen ersten Durchlauf grundlegender Vorprüfungen für Zielgruppenberechtigung, Wiederberechtigung und Kanalberechtigung durch, bevor die vollständigen Zustellungsvalidierungen für einen Canvas-Nachrichtenschritt ausgeführt werden. Dieses Ergebnis bedeutet, dass die Nutzer:innen oder die Nachricht eine dieser Prüfungen nicht bestanden haben, sodass die Nachricht für diesen Schritt abgebrochen wurde. |
| Nutzer:innen haben Vorprüfung für getriggerte Nachricht nicht bestanden | Braze führt einen ersten Durchlauf grundlegender Vorprüfungen für Zielgruppenberechtigung, Wiederberechtigung und Kanalberechtigung durch, bevor eine Nachricht aus diesem Trigger erstellt wird. Dieses Ergebnis bedeutet, dass die Nutzer:innen oder die Nachricht eine dieser Prüfungen nicht bestanden haben, sodass die Nachricht abgebrochen wurde. |
| Nutzer:innen nicht mehr berechtigt | Die Nutzer:innen waren ursprünglich in der Zielgruppe, entsprachen aber nicht mehr den Zielgruppenkriterien, bevor Braze die Nachricht gesendet oder sie in den Canvas aufgenommen hat. Die Zeit zwischen dem ursprünglichen Erfüllen der Zielgruppenkriterien und dem Herausfallen aus der Zielgruppe kann auf Verzögerungen zurückzuführen sein durch: {::nomarkdown}<ul><li>Intelligentes Timing</li><li>Ruhezeiten</li><li>Ortszeit</li><li>Rate-Limits für die Zustellgeschwindigkeit (nicht anwendbar für Canvas-Eintritt)</li><li>Verzögerungen in der Messaging-Pipeline</li></ul>{:/} |
| Nutzer:innen nicht für Schritt berechtigt | Die Nutzer:innen haben die festgelegten [Zustellungsvalidierungen]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#delivery-validations) für den Nachrichtenschritt nicht erfüllt oder waren Teil einer [Unterdrückungsliste]({{site.baseurl}}/user_guide/audience/suppression_lists). Abhängig von den Einstellungen der **Zustellungsvalidierungen** haben die Nutzer:innen den Canvas verlassen oder sind zum nächsten Schritt weitergegangen. |
| Nutzer:innen nicht wiederberechtigt | Die Nutzer:innen waren berechtigt, die Nachricht zu erhalten oder den Canvas zu betreten, aber der Versand wurde aufgrund von Wiederberechtigungs- oder Wiedereintrittseinstellungen abgebrochen. Dies kann passieren, wenn die Nutzer:innen die Campaign bereits erhalten haben oder den Canvas zu kürzlich betreten haben, wenn ein anderer Versand für dieselbe Campaign bereits für diese Nutzer:innen läuft, oder wenn die Wiederberechtigung oder der Wiedereintritt deaktiviert ist. |
| Nutzerprofil nicht gefunden | Die Nutzer:innen haben entweder nie existiert oder existieren nicht mehr in Braze. Einige häufige Fälle sind: {::nomarkdown}<ul><li> Die Nutzer:innen wurden über API-Messaging angesprochen, existierten aber nie in Braze. </li><li>Die Nutzer:innen wurden gelöscht, bevor die Nachricht gesendet oder der Canvas-Schritt ausgeführt wurde. </li><li>Die Nutzer:innen wurden mit einem anderen Profil zusammengeführt, bevor die Nachricht gesendet wurde.</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Nutzerberechtigung und Profil" }

#### Kanal und Zustellung {#channel-and-delivery}

| Abbruchergebnis | Erklärung |
| ---- | ---- |
| Partner-Zustellungs-Timeout | Braze hat 24 Stunden lang versucht, diese Nachricht an Ihren Zustellungspartner zu senden, aber der Partner hat während des gesamten Zeitfensters temporäre Fehler zurückgegeben. |
| Push-Zugangsdaten ungültig | Die [Push-Zugangsdaten]({{site.baseurl}}/user_guide/channels/push/faqs#valid-push-token) für diese App fehlen oder sind ungültig, sodass der Versand abgebrochen wurde. Aktualisieren Sie Ihre Zugangsdaten in den **App Settings**. |
| Abo-Gruppen-Fehler | Die Nachricht konnte aufgrund von Problemen mit der Abo-Gruppen- oder Messaging-Dienst-Konfiguration nicht gesendet werden. Häufige Gründe sind fehlende Sendenummern für SMS oder WhatsApp oder nicht unterstütztes MMS im konfigurierten Messaging-Dienst. |
| Nutzer:innen nicht für Kanal berechtigt | Die Nutzer:innen sind nicht berechtigt, diese Nachricht auf dem ausgewählten Kanal zu empfangen. Häufige Gründe sind fehlende oder ungültige Kanalbezeichner, keine berechtigten Push-Token, Einschränkungen des Abo-Status, nicht unterstützte Kanalfunktionen oder gesperrte Länder für telefonbasierte Kanäle. |
| Webhook fehlgeschlagen | Der Webhook hat einen nicht erfolgreichen Antwortcode (nicht `2xx`) erhalten. Weitere Details finden Sie im [Nachrichten-Aktivitätsprotokoll]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log#dev-console-troubleshooting). Protokolle, die älter als 60 Stunden sind, werden bereinigt und sind nicht mehr zugänglich; Webhook-Fehler werden mit bis zu 20 Protokollen pro Stunde erfasst. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Kanal und Zustellung" }

## Häufig gestellte Fragen {#frequently-asked-questions}

### Was bedeutet ein „Vorprüfungs“-Fehler? {#what-does-a-pre-check-failure-mean}

Eine „Vorprüfung“ bezieht sich auf eine schnelle, gebündelte Validierungsprüfung, die ganz am Anfang einer Pipeline-Stufe ausgeführt wird (z. B. wenn eine Nachricht getriggert wird oder ein Canvas-Nachrichtenschritt gesendet wird). Stellen Sie sich dies als einen frühen Ausstieg vor, der auf maximale Geschwindigkeit ausgelegt ist. Anstatt viele separate, ressourcenintensive Prüfungen durchzuführen (wie die Validierung jedes Details eines Nutzerprofils), bündelt Braze mehrere grundlegende Validierungen in einem „ersten Durchlauf“.

Wenn Nutzer:innen diese einzelne gebündelte Prüfung nicht bestehen, werden sie sofort entfernt. Dieser gebündelte Ansatz ermöglicht es Braze, massive Nachrichtenvolumen mit hoher Geschwindigkeit zu verarbeiten, und kann zu einer schnelleren, stabileren Performance Ihrer Campaigns und Canvases beitragen, indem die Verarbeitungslatenz für jede Nachricht reduziert wird.

### Was bedeutet ein „Sonstiges“-Abbruchergebnis? {#what-does-an-other-abort-outcome-mean}

Dies sind Abbrüche, die in keine der bestehenden Dashboard-Kategorien fallen. Wenn Sie einen großen Anteil an Abbrüchen mit „Sonstiges“ feststellen, kontaktieren Sie den [Braze-Support]({{site.baseurl}}/braze_support) für weitere Unterstützung.

### Warum ist die Summe von _Not Sent_ und _Sent_ niedriger als meine erwartete Zielgruppengröße? {#why-is-the-sum-of-_not-sent_-and-_sent_-lower-than-my-expected-audience-size}

Dies kann mehrere Gründe haben:

- **Zielgruppenkriterien:** Weniger Nutzer:innen als erwartet haben möglicherweise die Zielgruppenkriterien erfüllt (z. B. waren sie nicht im Segment oder hatten nicht die erforderlichen Attribute), als die Campaign oder der Canvas gestartet wurde.
- **Verarbeitung läuft:** Nachrichten werden möglicherweise noch aktiv verarbeitet. Nutzer:innen befinden sich möglicherweise noch in früheren Schritten des Canvas und haben noch keine Nachrichtenschritte erreicht.
- **Datenaktualität:** Die Dashboard-Daten werden ungefähr alle 15 Minuten aktualisiert, dies ist jedoch nicht garantiert. Die neuesten Daten für diese Campaign oder diesen Canvas haben das Dashboard möglicherweise noch nicht erreicht.
- **Sonderfälle:** Es besteht eine geringe Wahrscheinlichkeit, dass Sie auf einen Sonderfall stoßen, der derzeit nicht in diesem Dashboard erfasst wird. Wenn Sie dies vermuten, kontaktieren Sie den [Braze-Support]({{site.baseurl}}/user_guide/administer/personal/braze_support).

### Warum ist die Summe von _Not Sent_ und _Sent_ größer als die Zielgruppe einer Campaign oder eines Canvas? {#why-is-the-sum-of-_not-sent_-and-_sent_-greater-than-the-audience-for-a-campaign-and-canvas}

Dies kann aus folgenden Gründen auftreten:

- **Mehrkanal-Nachrichten:** Die Campaign oder der Canvas-Schritt war so konfiguriert, dass über mehrere Kanäle gesendet wird (z. B. SMS und E-Mail). Einzelne Nutzer:innen können ein „Gesendet“-Ergebnis für einen Kanal (z. B. E-Mail) und ein „Abbruch“-Ergebnis für einen anderen erhalten (z. B. „Nutzer:innen nicht für Kanal berechtigt“). In diesem Fall würden diese Nutzer:innen im Chart zweimal gezählt: einmal als „Gesendet“ und einmal als „Abbruch“.
  - **Beispiel:** Sie senden eine Push-Campaign an 100 Nutzer:innen, die sowohl iOS als auch Android anspricht. Wenn Nutzer:innen nur ein iOS-Gerät haben, erhalten sie den iOS-Push („Gesendet“), lösen aber auch einen Abbruch für den Android-Push aus („Nutzer:innen nicht für Kanal berechtigt“).
- **Mehrere Nachrichtenschritte (nur Canvas):** Ihr Canvas kann mehr als einen Nachrichtenschritt in einem bestimmten Pfad haben. Dieses Dashboard aggregiert alle Ergebnisse, sodass einzelne Nutzer:innen mehrfach gezählt werden können, wenn sie innerhalb des ausgewählten Zeitraums mehrere Nachrichtenschritte durchlaufen.
- **Testnachrichten:** Testversand (der im Dashboard gezählt wird) lässt die Gesamtzahlen höher erscheinen als die Zielgruppengröße.