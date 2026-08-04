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
Das **Messaging-Diagnose**-Dashboard ist allgemein verfügbar. Kontaktieren Sie Ihren Customer-Success-Manager, wenn Sie Zugang zu diesem Feature erhalten möchten.
{% endalert %}

{% alert note %}
Um auf das **Messaging-Diagnose**-Dashboard zuzugreifen, benötigen Sie die [Nutzerberechtigungen]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) „Dashboard-Berichte anzeigen“ und „PII anzeigen“ für Ihren Workspace.
{% endalert %}

## Schlüsselkonzepte {#key-concepts}

### Gesendet und zugestellt {#sent-and-delivered}

Es ist wichtig zu verstehen, dass dieses Dashboard darüber berichtet, wie Braze eine Nachricht intern verarbeitet hat – nicht über den endgültigen Zustellungsstatus der Nachricht.

Eine in diesem Dashboard als „gesendet“ markierte Nachricht bedeutet, dass Braze die Nachricht erfolgreich verarbeitet und versandt hat. Bei den meisten Kanälen bedeutet dies, dass Braze die Nachricht an den zuständigen Drittanbieter-Versandpartner übergeben hat. Es garantiert jedoch nicht die endgültige Zustellung an das Gerät der Nutzer:innen.

Wenn Braze eine Nachricht „sendet“, kann die endgültige Zustellung von externen Diensten abhängen. Betrachten Sie die folgenden Beispiele für jeden Kanal.

| Kanal | Beispiel für die endgültige Zustellung |
| --- | --- |
| Content Cards | Die Card wurde gesendet und ist zur Anzeige berechtigt. |
| E-Mail | Braze übergibt die Nachricht an einen E-Mail-Anbieter (ESP). Der ESP ist dann für die endgültige Zustellung verantwortlich. Dieser ESP kann beispielsweise einen „Bounce“ melden, wenn die E-Mail-Adresse ungültig ist oder der Posteingang voll ist. |
| In-App Messages | Die Nachricht wurde von den Nutzer:innen angesehen und eine Impression wurde protokolliert. |
| LINE | Die Nachricht wurde erfolgreich an einen Versandpartner übergeben. |
| Push | Braze übergibt die Nachricht an den entsprechenden Push-Benachrichtigungsdienst (z. B. Apple Push Notification Service für iOS oder Firebase Cloud Messaging für Android). Dieser Dienst ist für die endgültige Zustellung der Benachrichtigung an das Gerät verantwortlich. |
| SMS/MMS/RCS | Braze übergibt die Nachricht an ein SMS-Gateway (wie Twilio). Dieses Gateway ist für die endgültige Zustellung an den Mobilfunkanbieter verantwortlich. |
| Webhooks | Die Webhook-Anfrage wurde erfolgreich durchgeführt und hat eine `2xx`-Antwort zurückgegeben. |
| WhatsApp | Die Nachricht wurde erfolgreich an einen Versandpartner übergeben. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Gesendet und zugestellt" }

### Datenaktualität {#data-freshness}

Die Häufigkeit, mit der die Daten in diesem Dashboard aktualisiert werden, kann je nach Systemlast variieren. Obwohl die Aktualisierungshäufigkeit nicht garantiert wird, beträgt sie in den meisten Fällen voraussichtlich weniger als eine Stunde.

## Dashboard konfigurieren {#configuring-the-dashboard}

Sie können auf das Diagnostik-Dashboard zugreifen, indem Sie zu **Analytics** > **Dashboard Builder** navigieren und **Messaging Diagnostics** aus der Liste der von Braze erstellten Dashboards auswählen.

So führen Sie das Dashboard aus und zeigen Ihre Daten an:

1. Wählen Sie entweder **Campaigns** oder **Canvases** als Quelle für Ihre Dashboard-Berichte aus.
2. Wählen Sie eine oder mehrere Campaigns oder Canvases aus.
3. Wählen Sie **Run Dashboard** aus, um die Daten für Ihre ausgewählten Filter zu laden.

![Beispiel für Campaign- und Canvas-Diagnostik vom 25. bis 31. Mai 2025 für eine Willkommensserie-Campaign.]({% image_buster /assets/img/messaging_diagnostics_dashboard_details_log.png %}){: style="max-width:45%;"} ![Beispiel für Campaign- und Canvas-Diagnostik mit Diagramm beim Hovern vom 25. bis 31. Mai 2025 für eine Willkommensserie-Campaign.]({% image_buster /assets/img/messaging_diagnostics_dashboard_drawer_expanded.png %}){: style="max-width:45%;"}

## Daten interpretieren {#interpreting-the-data}

{% alert note %}
Das Dashboard zeigt nur die Daten der letzten sieben Tage an. Alle Zeitstempel werden in der Zeitzone Ihres Workspace angezeigt.
{% endalert %}

### Zusammenfassungskacheln {#summary-tiles}

Am oberen Rand der Seite befinden sich wichtige Zusammenfassungskacheln für den ausgewählten Zeitraum, die Folgendes anzeigen:

- **Gesendet:** Die Gesamtanzahl der Nachrichten, die Braze erfolgreich verarbeitet und gesendet hat.
  - **E-Mail, SMS/MMS/RCS, WhatsApp, LINE und Push:** Die Nachricht wurde erfolgreich an einen Versandpartner übergeben.
  - **Webhooks:** Die Webhook-Anfrage wurde erfolgreich ausgeführt und hat eine `2xx`-Antwort zurückgegeben.
  - **Content Cards:** Die Card wurde gesendet und ist zur Anzeige berechtigt.
  - **In-App Messages:** Die Nachricht wurde der/dem Nutzer:in angezeigt.
- **Nicht gesendet:** Die Gesamtanzahl der Nachrichten, die abgebrochen wurden. Dies umfasst Canvas-Zielgruppenmitglieder, die den Canvas nicht betreten haben oder den Canvas verlassen haben, weil bei einem Schritt ein Fehler aufgetreten ist oder sie die Exit-Kriterien erfüllt haben, während sie ein Exit-Event ausgeführt haben.

### Nachrichtenergebnisse im Zeitverlauf {#message-outcomes-over-time}

Dieses Zeitreihendiagramm zeigt eine stündliche Aufschlüsselung, warum eine Nachricht abgebrochen wurde oder warum Nutzer:innen aus einem Canvas entfernt wurden. Die Ergebnisbezeichnungen in diesem Chart sind normalisierte Dashboard-Labels, keine rohen Event-Payload-Werte. Dieses Chart zeigt nicht die Anzahl der Sendungen an.

### Detailliertes Protokoll der Nachrichtenergebnisse {#message-outcomes-granular-log}

Das Dashboard zeigt eine detaillierte Tabelle einzelner Nachrichtenergebnisse für Ihre ausgewählten Filter und den Zeitraum. Verwenden Sie diese Tabelle, um bestimmte Datensätze zu überprüfen, einschließlich Zeitstempel, Nutzer-ID, Canvas-Schritt, Ergebnis, Details und Kanal.

Sie können die Tabelle filtern, um sich auf bestimmte Datensätze zu konzentrieren:

- **Nach Ergebnis filtern:** Wählen Sie ein Ergebnis aus dem Ergebnisfilter aus, um nur Zeilen mit diesem Ergebnis anzuzeigen (zum Beispiel `Frequency capped` oder `User not eligible for channel`).
- **Nach Nutzer-ID suchen:** Geben Sie eine Nutzer-ID in das Suchfeld ein, um Zeilen für diese:n bestimmte:n Nutzer:in anzuzeigen.

Wenn Sie beide Filter anwenden, gibt die Tabelle Zeilen zurück, die sowohl dem ausgewählten Ergebnis als auch der eingegebenen Nutzer-ID entsprechen.

Wählen Sie eine Zeile in der Tabelle aus, um das Detailpanel zu öffnen. Das Detailpanel bietet zusätzlichen Kontext zu diesem Ergebnis, und Ask Operator liefert Hinweise zur Behebung, die Ihnen bei der Fehlerbehebung des zugrunde liegenden Problems helfen.

![Detailliertes Ergebnisprotokoll der Messaging-Diagnose mit einer ausgewählten Zeile und Zugang zum Detailpanel.]({% image_buster /assets/img/messaging_diagnostics_dashboard_details_log.png %}){: style="max-width:45%;"} ![Erweitertes Detailpanel der Messaging-Diagnose mit Ergebniskontext und Hinweisen zur Behebung.]({% image_buster /assets/img/messaging_diagnostics_dashboard_drawer_expanded.png %}){: style="max-width:45%;"}

{% alert note %}
Kanalfilter gelten für Ergebnisse, die an einen bestimmten Messaging-Kanal gebunden sind. Einige Ergebnisse sind kanalunabhängig und können daher auch in aggregierten Ansichten erscheinen, wenn Sie einen Kanalfilter anwenden.
{% endalert %}

### Abbruchergebnisse {#abort-outcomes}

Die folgenden Definitionen erklären die im Dashboard angezeigten Abbruchergebnisse. Die Ergebnisse sind nach Kategorien gruppiert, damit Sie das gesuchte Ergebnis leichter finden.

{% alert note %}
Abbruchergebnisse in der Messaging-Diagnose sind menschenlesbare Dashboard-Labels. In [Currents-Message-Engagement-Events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) werden Abbruchinformationen mit Feldern wie `abort_type` und `abort_log` dargestellt. Da diese Datensätze unterschiedliche Darstellungen und Verarbeitungspfade haben, können Zählungen oder Bezeichnungen zwischen Currents und der Messaging-Diagnose abweichen.
{% endalert %}

#### Inhalt und Rendering {#content-and-rendering}

| Abbruchergebnis | Erklärung |
| ---- | ---- |
| Content Card abgelaufen | Die Content Card ist abgelaufen, bevor die/der Nutzer:in sie gesehen hat. |
| Content Card ungültig | Die Content Card enthielt Fehler und wurde nicht an die/den Nutzer:in gesendet. Häufige Gründe hierfür sind: {::nomarkdown}<ul><li> Maximale Größe überschritten (2 KB) </li><li> Ablaufdatum ist ungültig </li><li> Nachricht enthält ungültige Zeichen </li></ul>{:/} |
| Connected Content fehlgeschlagen | Braze hat versucht, die Nachricht zu senden, aber Connected Content ist nach der maximalen Anzahl von Wiederholungsversuchen (Standard: fünf) fehlgeschlagen. **Hinweis:** Diese Zählung gibt die Anzahl der Nachrichten an, die aufgrund des Erreichens der maximalen Wiederholungsversuche abgebrochen wurden, nicht die Gesamtzahl der fehlgeschlagenen Connected-Content-Anfragen. |
| Rendering-Timeout für In-App-Nachricht | Nach mehreren Wiederholungsversuchen konnte das Liquid nicht gerendert werden und es kam zu einem Timeout. |
| Liquid-Abbruch | Der Liquid-Tag [abort_message]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages) wurde aufgerufen, sodass der Versand abgebrochen wurde. |
| Liquid-Rendering-Timeout | Das Rendern des Liquid-Templates hat zu lange gedauert. Dies tritt am häufigsten bei Bannern, In-App-Nachrichten und E-Mails auf. |
| Liquid-Syntaxfehler | Das Liquid-Template hatte einen Parsing-Fehler, sodass die Nachricht abgebrochen wurde. |
| Medien-URL-Fehler | Braze konnte die Medien-URL in der Nachricht nicht verarbeiten. Dies kann passieren, wenn die URL blockiert oder ungültig ist, ein Timeout auftritt, einen ungültigen HTTP-Status zurückgibt oder die SSL-Validierung fehlschlägt. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Inhalt und Rendering" }

#### Campaign- und Canvas-Status {#campaign-and-canvas-state}

| Abbruchergebnis | Erklärung |
| ---- | ---- |
| Verzögerungsschritt fehlgeschlagen | Der [Verzögerungsschritt]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step#personalized-delays) ist fehlgeschlagen, wodurch die/der Nutzer:in den Canvas verlassen hat. Dieser Fehler kann auftreten, wenn: {::nomarkdown}<ul><li> Die dem personalisierten Verzögerungsschritt übergebene Variable leer oder ein ungültiger Typ war </li><li> Die Verzögerung die maximal zulässige Dauer innerhalb des Canvas überschreitet</li></ul>{:/} |
| Ausnahme- oder Exit-Event | Die/der Nutzer:in war zuvor berechtigt, die Nachricht zu erhalten, hat aber entweder {::nomarkdown}<ul><li> ein <a href="/docs/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery#step-3-select-exception-events">Ausnahme-Event</a> für eine aktionsbasierte Campaign ausgeführt, sodass die Nachricht abgebrochen wurde, oder </li><li> die Canvas-<a href="/docs/user_guide/messaging/canvas/create_a_canvas#setting-exit-criteria">Exit-Kriterien</a> erfüllt und wurde daher mitten in der Journey entfernt.</li></ul>{:/} |
| Inaktive Campaign | Die Campaign wurde gestoppt, während die Nachricht unterwegs war, sodass sie abgebrochen wurde. |
| Inaktiver Canvas | Der Canvas wurde gestoppt, bevor die/der Nutzer:in die Journey betreten hat. |
| Inaktiver Canvas-Schritt | Dies kann im Canvas auftreten, wenn: {::nomarkdown}<ul><li> Der Canvas-Schritt gelöscht wurde </li> <li>Der Canvas gestoppt wurde, wodurch alle Schritte inaktiv werden </li></ul>{:/} |
| Volumenlimit erreicht | Die Campaign hat das festgelegte Volumenlimit erreicht, sodass der Versand abgebrochen wurde. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Campaign- und Canvas-Status" }

#### Rate-Limiting und Timing {#rate-limiting-and-timing}

| Abbruchergebnis | Erklärung |
| ---- | ---- |
| Frequency-Capping erreicht | Die/der Nutzer:in hat bereits die maximale Anzahl an Nachrichten erhalten, die gemäß den [Frequency-Capping]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#about-frequency-capping)-Regeln Ihres Workspace zulässig sind, sodass der Versand abgebrochen wurde. |
| Ruhezeiten-Abbruch | Ruhezeiten waren für die Campaign oder den Canvas-Schritt aktiviert, wobei der Fallback auf **Nachricht abbrechen** eingestellt war. Die/der Nutzer:in hat die Campaign getriggert oder den Canvas-Nachrichtenschritt während der Ruhezeiten betreten, sodass die Nachricht abgebrochen wurde. Dies führt jedoch nicht dazu, dass die/der Nutzer:in den Canvas verlässt. |
| Rate-Limiting über 72 Stunden | Die Nachricht wurde aufgrund von [Rate-Limits für die Zustellgeschwindigkeit]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting) länger als 72 Stunden gedrosselt, sodass der Versand abgebrochen wurde. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Rate-Limiting und Timing" }

#### Nutzerberechtigung und Profil {#user-eligibility-and-profile}

| Abbruchergebnis | Erklärung |
| ---- | ---- |
| Doppelter Nutzerbezeichner | Mehrere Nutzer:innen mit einem übereinstimmenden Bezeichner (wie externe ID, E-Mail-Adresse, Telefonnummer) waren berechtigt, diese Nachricht zu erhalten. Um doppelte Sendungen an dieselbe Person zu vermeiden, wurde diese Nachricht abgebrochen. |
| Nutzer:in hat Vorprüfung für Nachrichtenschritt nicht bestanden | Braze führt einen ersten Satz grundlegender Vorprüfungen für Zielgruppenberechtigung, Wiederberechtigung und Kanalberechtigung durch, bevor die vollständigen Zustellungsvalidierungen für einen Canvas-Nachrichtenschritt erfolgen. Dieses Ergebnis bedeutet, dass die/der Nutzer:in oder die Nachricht eine dieser Prüfungen nicht bestanden hat, sodass die Nachricht für diesen Schritt abgebrochen wurde. |
| Nutzer:in hat Vorprüfung für getriggerte Nachricht nicht bestanden | Braze führt einen ersten Satz grundlegender Vorprüfungen für Zielgruppenberechtigung, Wiederberechtigung und Kanalberechtigung durch, bevor eine Nachricht zum Senden aus diesem Trigger erstellt wird. Dieses Ergebnis bedeutet, dass die/der Nutzer:in oder die Nachricht eine dieser Prüfungen nicht bestanden hat, sodass die Nachricht abgebrochen wurde. |
| Nutzer:in nicht mehr berechtigt | Die/der Nutzer:in war ursprünglich in der Zielgruppe, entsprach aber nicht mehr den Zielgruppenkriterien, bevor Braze die Nachricht gesendet oder die/den Nutzer:in in den Canvas aufgenommen hat. Die Zeit zwischen dem erstmaligen Erfüllen der Zielgruppenkriterien und dem Herausfallen aus der Zielgruppe kann auf Verzögerungen zurückzuführen sein durch: {::nomarkdown}<ul><li>Intelligentes Timing</li><li>Ruhezeiten</li><li>Ortszeit</li><li>Rate-Limits für die Zustellgeschwindigkeit (nicht anwendbar für Canvas-Entry)</li><li>Verzögerungen in der Messaging-Pipeline</li></ul>{:/} |
| Nutzer:in nicht für Schritt berechtigt | Die/der Nutzer:in hat die festgelegten [Zustellungsvalidierungen]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#delivery-validations) für den Nachrichtenschritt nicht erfüllt oder war Teil einer [Unterdrückungsliste]({{site.baseurl}}/user_guide/audience/suppression_lists). Abhängig von den Einstellungen der **Zustellungsvalidierungen** hat die/der Nutzer:in den Canvas möglicherweise verlassen oder ist zum nächsten Schritt weitergegangen. |
| Nutzer:in nicht wiederberechtigt | Die/der Nutzer:in war berechtigt, die Nachricht zu erhalten oder den Canvas zu betreten, aber der Versand wurde aufgrund von Wiederberechtigungs- oder Wiedereintrittseinstellungen abgebrochen. Dies kann passieren, wenn die/der Nutzer:in die Campaign bereits erhalten oder den Canvas kürzlich betreten hat, wenn ein anderer Versand für dieselbe Campaign bereits für diese:n Nutzer:in läuft oder wenn Wiederberechtigung oder Wiedereintritt deaktiviert ist. |
| Nutzerprofil nicht gefunden | Die/der Nutzer:in hat entweder nie existiert oder existiert nicht mehr in Braze. Häufige Fälle sind: {::nomarkdown}<ul><li> Die/der Nutzer:in wurde über API-Messaging angesprochen, existierte aber nie in Braze. </li><li>Die/der Nutzer:in wurde gelöscht, bevor die Nachricht gesendet oder der Canvas-Schritt ausgeführt wurde. </li><li>Die/der Nutzer:in wurde mit einem anderen Profil zusammengeführt, bevor die Nachricht gesendet wurde.</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Nutzerberechtigung und Profil" }

#### Kanal und Zustellung {#channel-and-delivery}

| Abbruchergebnis | Erklärung |
| ---- | ---- |
| Zustellungsfehler beim Partner | Braze hat 24 Stunden lang versucht, diese Nachricht an Ihren Zustellungspartner zu senden, aber der Partner hat während des gesamten Zeitfensters temporäre Fehler zurückgegeben. |
| Push-Zugangsdaten ungültig | Die [Push-Zugangsdaten]({{site.baseurl}}/user_guide/channels/push/faqs#why-doesnt-an-opted-in-user-have-a-push-token) für diese App fehlen oder sind ungültig, sodass der Versand abgebrochen wurde. Aktualisieren Sie Ihre Zugangsdaten in den **App-Einstellungen**. |
| Abo-Gruppen-Fehler | Die Nachricht konnte aufgrund von Problemen mit der Abo-Gruppen- oder Messaging-Dienst-Konfiguration nicht gesendet werden. Häufige Gründe sind fehlende Sendenummern für SMS oder WhatsApp oder nicht unterstütztes MMS beim konfigurierten Messaging-Dienst. |
| Nutzer:in nicht für Kanal berechtigt | Die/der Nutzer:in ist nicht berechtigt, diese Nachricht auf dem ausgewählten Kanal zu erhalten. Häufige Gründe sind fehlende oder ungültige Kanalbezeichner, keine berechtigten Push-Token, Einschränkungen des Abo-Status, nicht unterstützte Kanalfunktionen oder blockierte Länder für telefonbasierte Kanäle. |
| Webhook fehlgeschlagen | Der Webhook hat einen nicht erfolgreichen Antwortcode (nicht `2xx`) erhalten. Häufige Fehlercodes können `4XX`-Client-Fehler, `5XX`-Server-Fehler oder Timeout oder `598 Host Unhealthy` oder kurzzeitig angehaltene Anfragen sein. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Kanal und Zustellung" }

## Häufig gestellte Fragen {#frequently-asked-questions}

### Was bedeutet ein „Pre-Check“-Fehler? {#what-does-a-pre-check-failure-mean}

Ein „Pre-Check“ ist eine schnelle, gebündelte Validierungsprüfung, die ganz am Anfang einer Pipeline-Stufe ausgeführt wird (z. B. wenn eine Nachricht getriggert oder ein Canvas-Nachrichtenschritt gesendet wird). Stellen Sie sich das als einen frühzeitigen Abbruch vor, der auf maximale Geschwindigkeit ausgelegt ist. Anstatt viele einzelne, ressourcenintensive Prüfungen durchzuführen (wie die Validierung jedes Details eines Nutzerprofils), bündelt Braze mehrere grundlegende Validierungen in einem „ersten Durchlauf“.

Wenn ein:e Nutzer:in diese gebündelte Prüfung nicht besteht, wird er/sie sofort ausgeschlossen. Dieser gebündelte Ansatz ermöglicht es Braze, große Nachrichtenvolumen mit hoher Geschwindigkeit zu verarbeiten, und kann zu einer schnelleren, stabileren Performance Ihrer Campaigns und Canvases beitragen, indem die Verarbeitungslatenz pro Nachricht reduziert wird.

### Was bedeutet ein Abbruchgrund „Sonstige“? {#what-does-an-other-abort-outcome-mean}

Dabei handelt es sich um Abbrüche, die in keine der bestehenden Dashboard-Kategorien fallen. Wenn Sie weiterhin einen großen Anteil an Abbrüchen mit „Sonstige“ feststellen, wenden Sie sich an den [Braze-Support]({{site.baseurl}}/braze_support) für weitere Unterstützung.

### Warum ist die Summe aus _Nicht gesendet_ und _Gesendet_ kleiner als meine erwartete Zielgruppengröße? {#why-is-the-sum-of-_not-sent_-and-_sent_-lower-than-my-expected-audience-size}

Das kann verschiedene Gründe haben:

- **Zielgruppenkriterien:** Weniger Nutzer:innen als erwartet haben möglicherweise die Zielgruppenkriterien erfüllt (z. B. waren sie nicht im Segment oder hatten nicht die erforderlichen Attribute), als die Campaign oder der Canvas gestartet wurde.
- **Verarbeitung läuft noch:** Nachrichten werden möglicherweise noch aktiv verarbeitet. Nutzer:innen befinden sich möglicherweise noch in früheren Schritten des Canvas und haben noch keine Nachrichtenschritte erreicht.
- **Datenaktualität:** Die Dashboard-Daten werden ungefähr alle 15 Minuten aktualisiert, dies ist jedoch nicht garantiert. Die neuesten Daten für diese Campaign oder diesen Canvas haben das Dashboard möglicherweise noch nicht erreicht.
- **Sonderfälle:** Es besteht eine geringe Wahrscheinlichkeit, dass Sie auf einen Sonderfall stoßen, der in diesem Dashboard derzeit nicht erfasst wird. Wenn Sie dies vermuten, wenden Sie sich an den [Braze-Support]({{site.baseurl}}/user_guide/administer/personal/braze_support).

### Warum ist die Summe aus _Nicht gesendet_ und _Gesendet_ größer als die Zielgruppe einer Campaign oder eines Canvas? {#why-is-the-sum-of-_not-sent_-and-_sent_-greater-than-the-audience-for-a-campaign-and-canvas}

Das kann folgende Gründe haben:

- **Mehrkanalige Nachrichten:** Die Campaign oder der Canvas-Schritt wurde so konfiguriert, dass über mehrere Kanäle gesendet wird (z. B. SMS und E-Mail). Ein:e einzelne:r Nutzer:in kann für einen Kanal (z. B. E-Mail) das Ergebnis „Gesendet“ und für einen anderen (z. B. „Nutzer:in nicht für Kanal berechtigt“) das Ergebnis „Abbruch“ erhalten. In diesem Fall würde diese:r Nutzer:in im Chart zweimal gezählt: einmal als „Gesendet“ und einmal als „Abbruch“.
  - **Beispiel:** Sie senden eine Push-Campaign an 100 Nutzer:innen und zielen dabei auf iOS und Android ab. Wenn ein:e Nutzer:in nur ein iOS-Gerät hat, erhält er/sie die iOS-Push-Benachrichtigung („Gesendet“), löst aber auch einen Abbruch für die Android-Push-Benachrichtigung aus („Nutzer:in nicht für Kanal berechtigt“).
- **Mehrere Nachrichtenschritte (nur Canvas):** Ihr Canvas kann in einem bestimmten Pfad mehr als einen Nachrichtenschritt enthalten. Dieses Dashboard aggregiert alle Ergebnisse, sodass ein:e einzelne:r Nutzer:in mehrfach gezählt werden kann, wenn er/sie innerhalb des ausgewählten Zeitraums mehrere Nachrichtenschritte durchläuft.
- **Testnachrichten:** Testversand (der im Dashboard mitgezählt wird) kann die Gesamtzahlen über die Zielgruppengröße hinaus erhöhen.