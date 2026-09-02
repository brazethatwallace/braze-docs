---
nav_title: Glossar der Metriken
article_title: Glossar der Metriken
layout: report_metrics
page_order: 4
excerpt_separator: ""
page_type: glossary
description: "Dieses Glossar definiert Begriffe, die Sie in Ihren Berichten in Ihrem Braze-Konto finden."
tool: Reports
---

<style>
  .calculation-line {
    color: #5B6B75;
    font-size: 14px;
  }
</style>

{% api %}

## AMP or Accelerated Mobile Pages-Klicks {#amp-clicks}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='AMP or Accelerated Mobile Pages Clicks' %}

{% endapi %}

{% api %}

## AMP or Accelerated Mobile Pages-Öffnungen {#amp-opens}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='AMP or Accelerated Mobile Pages Opens' %}

{% endapi %}

{% api %}

## Zielgruppe {#audience}

{% apitags %}
All
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Audience' %}

<span class="calculation-line">Berechnung: (Anzahl der Empfänger:innen in der Variante) / (Eindeutige Empfänger:innen)</span>

{% endapi %}

{% api %}

## Bounces {#bounces}

{% apitags %}
Email, Web Push, iOS Push
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Bounces' %} Dies kann auftreten, weil kein gültiges Push-Token / Textbaustein vorhanden ist, die Nutzer:innen sich nach dem Start der Campaign abgemeldet haben oder die E-Mail-Adresse ungenau oder deaktiviert ist.

| Kanal | Zusätzliche Informationen |
|-------|-----------------------|
| E-Mail | Ein E-Mail-Bounce für Kund:innen, die SendGrid verwenden, besteht aus Hard Bounces, Spam (`spam_report_drops`) und E-Mails, die an ungültige Adressen gesendet wurden (`invalid_emails`).<br><br>Für E-Mails ist *Bounce %* oder *Bounce-Rate* der Prozentsatz der Nachrichten, die nicht erfolgreich gesendet wurden oder als „zurückgesendet“ oder „nicht erhalten“ von genutzten Versanddiensten gekennzeichnet wurden oder von den vorgesehenen E-Mail-Empfänger:innen nicht empfangen wurden. |
| Push | Diese Nutzer:innen wurden automatisch von allen zukünftigen Push-Benachrichtigungen abgemeldet. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Bounces" }

{::nomarkdown}
<span class="calculation-line">
    Berechnung:
    <ul>
        <li><i>Bounces</i>: Anzahl</li>
        <li><i>Bounce %</i> oder <i>Bounce-Rate %</i>: (Bounces) / (Sends)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

## Body-Klick {#body-click}

{% apitags %}
iOS Push, Android Push
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Body Klick, der or klicken' %}

<span class="calculation-line">Berechnung: (Body-Klicks) / (Impressionen)</span>

{% endapi %}

{% api %}

## Body-Klicks {#body-clicks}

{% apitags %}
In-App Message
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Body Clicks' %}

<span class="calculation-line">Berechnung: (Body-Klicks) / (Impressionen)</span>

{% endapi %}

{% api %}

## Button-1-Klicks {#button-1-clicks}

{% apitags %}
In-App Message
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Button 1 Clicks' %} Das Reporting für _Button-1-Klicks_ funktioniert nur, wenn Sie den **Identifier for Reporting** in der In-App-Nachricht als „0“ angeben.

<span class="calculation-line">Berechnung: (Button-1-Klicks) / (Impressionen)</span>

{% endapi %}

{% api %}

## Button-2-Klicks {#button-2-clicks}

{% apitags %}
In-App Message
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Button 2 Clicks' %} Das Reporting für _Button-2-Klicks_ funktioniert nur, wenn Sie den **Identifier for Reporting** in der In-App-Nachricht als „1“ angeben.

<span class="calculation-line">Berechnung: (Button-2-Klicks) / (Impressionen)</span>

{% endapi %}

{% api %}

## Campaign-Analytics {#campaign-analytics}

{% apitags %}
Feature Flags
{% endapitags %}

Die Performance der Nachricht über verschiedene Kanäle hinweg. Die angezeigten Metriken hängen vom ausgewählten Messaging-Kanal ab und davon, ob das [Feature-Flag-Experiment]({{site.baseurl}}/developer_guide/feature_flags/experiments#campaign-analytics) ein multivariater Test ist.

{% endapi %}

{% api %}

## Eingereichte Auswahlen {#choices-submitted}

{% apitags %}
In-App Message
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Choices Submitted' %}

{% endapi %}

{% api %}

## Klick-zu-Öffnungs-Rate {#click-to-open-rate}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Klick, der or klicken-to-Open Rate' %}

<span class="calculation-line">Berechnung: (Eindeutige Klicks) / (Eindeutige Öffnungen) (für E-Mail)</span>

{% endapi %}

{% api %}

## Bestätigte RCS-Zustellungen oder bestätigte Kurzmitteilungsdienst or SMS-Zustellungen {#rcs-confirmed-deliveries-or-sms-confirmed-deliveries}

{% apitags %}
Kurzmitteilungsdienst or SMS/MMS, RCS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Confirmed Deliveries' %} Als Braze-Kund:in werden Zustellungen auf Ihr Kurzmitteilungsdienst or SMS-Kontingent angerechnet.

{::nomarkdown}
<span class="calculation-line">
    Berechnung:
    <ul>
        <li><i>Bestätigte Zustellungen</i>: Anzahl</li>
        <li><i>Bestätigte Zustellungsrate</i>: (Bestätigte Zustellungen) / (Sends)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

## Konfidenz {#confidence}

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, Kurzmitteilungsdienst or SMS/MMS, WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Confidence' %}

{% endapi %}

{% api %}

## Bestätigungsseiten-Button {#confirmation-page-button}

{% apitags %}
In-App Message
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Confirmation Page Button' %}

{% endapi %}

{% api %}

## Bestätigungsseiten-Abweisungen {#confirmation-page-dismissals}

{% apitags %}
In-App Message
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Confirmation Page Dismissals' %}

{% endapi %}

{% api %}

## Conversions (B, C, D) {#conversions-b-c-d}

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, Kurzmitteilungsdienst or SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Conversions (B, C, D)' %} Dieses definierte Ereignis wird von Ihnen beim Erstellen der Campaign festgelegt.

| Kanal | Zusätzliche Informationen |
|-------|-----------------------|
| E-Mail, Push, Webhooks | Conversions werden nach dem ersten Versand getrackt. |
| Content Cards | Conversions werden gezählt, wenn die Nutzer:innen eine Content Card zum ersten Mal ansehen. |
| In-App-Nachrichten | Eine Conversion wird gezählt, wenn die Nutzer:innen die In-App-Nachrichten-Campaign erhalten und angesehen haben und anschließend das spezifische Konversions-Event innerhalb des definierten Konversionsfensters ausführen, unabhängig davon, ob sie auf die Nachricht geklickt haben oder nicht.<br><br>Conversions werden der zuletzt empfangenen Nachricht zugeordnet. Wenn die erneute Berechtigung aktiviert ist, wird die Conversion der zuletzt empfangenen In-App-Nachricht zugewiesen, sofern sie innerhalb des definierten Konversionsfensters erfolgt. Wenn der In-App-Nachricht jedoch bereits eine Conversion zugewiesen wurde, kann die neue Conversion nicht für diese spezifische Nachricht protokolliert werden. Das bedeutet, dass jede In-App-Nachrichten-Zustellung nur mit einer Conversion verknüpft ist. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conversions (B, C, D)" }

{% endapi %}

{% api %}

## Conversions insgesamt {#total-conversions}

{% apitags %}
In-App Message
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Conversions' %}

Wenn Nutzer:innen eine In-App-Nachrichten-Campaign nur einmal ansehen, wird nur eine Conversion gezählt, selbst wenn sie das Konversions-Event später mehrfach ausführen. Wenn jedoch die erneute Berechtigung aktiviert ist und die Nutzer:innen die In-App-Nachrichten-Campaign mehrfach sehen, können die *Conversions insgesamt* einmal für jedes Mal steigen, wenn die Nutzer:innen eine Impression für eine neue Instanz der In-App-Nachrichten-Campaign protokollieren.

Wenn beispielsweise Nutzer:innen eine In-App-Nachricht zweimal Trigger or triggern or triggern und nach jeder In-App-Nachrichten-Impression konvertieren (was zu zwei Conversions führt), steigen die *Conversions insgesamt* um zwei. Wenn es jedoch nur eine In-App-Nachrichten-Impression gab, gefolgt von zwei Konversions-Events, wird nur eine Conversion protokolliert, und die *Conversions insgesamt* steigen um eins.

{% endapi %}

{% api %}

## Nachricht schließen {#close-message}

{% apitags %}
In-App Message
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Close Message' %}

{% endapi %}

{% api %}

## Konversionsrate {#conversion-rate}

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, Kurzmitteilungsdienst or SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Conversion Rate' %}

| Kanal | Zusätzliche Informationen |
|-------|-----------------------|
| In-App-Nachrichten | Die Metrik der täglichen <i>eindeutigen Impressionen</i> wird zur Berechnung der <i>Konversionsrate</i> für In-App-Nachrichten verwendet.<br><br><i>Eindeutige Impressionen</i> für In-App-Nachrichten können nur einmal pro Kalendertag in der Zeitzone Ihres Workspace gezählt werden. Die Anzahl der Male, die Nutzer:innen eine gewünschte Aktion ausführen (eine „Conversion“), kann innerhalb desselben Kalendertags steigen. Während Conversions mehr als einmal pro Tag stattfinden können, können <i>eindeutige Impressionen</i> das nicht. Wenn Nutzer:innen daher eine Conversion innerhalb eines Tages mehrfach ausführen, kann die <i>Konversionsrate</i> entsprechend steigen, aber <i>eindeutige Impressionen</i> werden für diesen Kalendertag nur einmal gezählt. Weitere Details finden Sie unter <a href="/docs/user_guide/channels/in_app_messages/reporting">In-App-Nachrichten-Reporting</a>. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Konversionsrate" }

{::nomarkdown}
<span class="calculation-line">
    Berechnung:
    <ul>
        <li><b>In-App-Nachrichten</b>: (Primäre Conversions) / (Eindeutige Impressionen)</li>
        <li><b>Andere Kanäle</b>: (Primäre Conversions) / (Eindeutige Empfänger:innen)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

## Konversionsfenster {#conversion-window}

{% apitags %}
All
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Conversion Window' %}

{% endapi %}

{% api %}

## Zustellungen {#deliveries}

{% apitags %}
Email, Web Push, iOS Push, Android Push, WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Deliveries' %}

| Kanal | Zusätzliche Informationen |
|-------|-----------------------|
| E-Mail | Bezieht sich auf die Gesamtzahl der Nachrichten (Sends), die erfolgreich an E-Mail-fähige Empfänger:innen gesendet und von diesen empfangen wurden. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Zustellungen" }

{::nomarkdown}
<span class="calculation-line">
    Berechnung:
    <ul>
        <li><i>Zustellungen</i>: Anzahl</li>
        <li><i>Zustellungen %</i>: (Sends - Bounces) / (Sends)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

## RCS-Zustellungsfehler oder Kurzmitteilungsdienst or SMS-Zustellungsfehler {#rcs-delivery-failures-or-sms-delivery-failures}

{% apitags %}
Kurzmitteilungsdienst or SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Delivery Failures' %}

Kontaktieren Sie den <a href="/docs/braze_support">Braze-Support</a>, um Unterstützung beim Verständnis der Gründe für Zustellungsfehler zu erhalten.

<span class="calculation-line">Berechnung: (Sends) - (Sends to Carrier)</span>

{% endapi %}

{% api %}

## Zustellungsfehler {#delivery-failures}

{% apitags %}
RCS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Delivery Failures RCS' %}

Kontaktieren Sie den <a href="/docs/braze_support">Braze-Support</a>, um Unterstützung beim Verständnis der Gründe für Zustellungsfehler zu erhalten.

<span class="calculation-line">Berechnung: (Sends) - (Sends to Carrier)</span>

{% endapi %}

{% api %}

## Fehlgeschlagene Zustellungsrate {#failed-delivery-rate}

{% apitags %}
Kurzmitteilungsdienst or SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Failed Delivery Rate' %}

Kontaktieren Sie den <a href="/docs/braze_support">Braze-Support</a>, um Unterstützung beim Verständnis der Gründe für Zustellungsfehler zu erhalten.

<span class="calculation-line">Berechnung: (Zustellungsfehler) / (Sends)</span>

{% endapi %}

{% api %}

## Direkte Öffnungen {#direct-opens}

{% apitags %}
iOS Push
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Direct Opens' %}

<span class="calculation-line">Berechnung: (Direkte Öffnungen) / (Zustellungen)</span>

{% endapi %}

{% api %}

## E-Mail-fähig {#emailable}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Emailable' %}

<span class="calculation-line">Berechnung: Anzahl</span>

{% endapi %}

{% api %}

## Fehler {#errors}

{% apitags %}
Webhook
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Errors' %} Fehler sind in der Anzahl der <i>Sends</i> enthalten, aber nicht in der Anzahl der <i>eindeutigen Empfänger:innen</i>.

{% endapi %}

{% api %}

## Geschätzte tatsächliche Öffnungen {#estimated-real-opens}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Estimated Real Opens' %}

{% endapi %}

{% api %}

## Fehlschläge {#failures}

{% apitags %}
WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Failures' %} Fehlschläge sind in der Anzahl der <i>Sends</i> enthalten, aber nicht in der Anzahl der <i>Zustellungen</i>.</td>

<span class="calculation-line">Berechnung (<i>Fehlschlagrate</i>): (Fehlschläge) / (Sends)</span>

{% endapi %}

{% api %}

## Feature-Flag-Experiment-Performance {#feature-flag-experiment-performance}

{% apitags %}
Feature Flags
{% endapitags %}

Performance-Metriken für die Nachricht in einem Feature-Flag-Experiment. Die spezifischen angezeigten Metriken variieren je nach Messaging-Kanal und ob das Experiment ein multivariater Test war oder nicht.

{% endapi %}

{% api %}

## Hard Bounce {#hard-bounce}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Hard Bounce' %}

Wenn dies auftritt, markiert Braze die E-Mail-Adresse als ungültig, aktualisiert aber nicht den [Abo-Status]({{site.baseurl}}/user_guide/channels/email/subscriptions) der Nutzer:innen. Wenn eine E-Mail einen Hard Bounce erhält, stoppt Braze alle zukünftigen Anfragen an diese E-Mail-Adresse.

{% endapi %}

{% api %}

## Hilfe {#help}

{% apitags %}
Kurzmitteilungsdienst or SMS/MMS, RCS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Help' %} Eine Nutzerantwort wird jedes Mal gemessen, wenn Nutzer:innen innerhalb von vier Stunden nach Erhalt Ihrer Nachricht eine eingehende Nachricht senden.

{% endapi %}

{% api %}

## Beeinflusste Öffnungen {#influenced-opens}

{% apitags %}
iOS Push, Android Push
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Influenced Opens' %}

<span class="calculation-line">Berechnung: (Beeinflusste Öffnungen) / (Zustellungen)</span>

{% endapi %}

{% api %}

## Lifetime-Umsatz {#lifetime-revenue}

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, Kurzmitteilungsdienst or SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Lifetime Revenue' %}

{% endapi %}

{% api %}

## LTV or Lifetime-Value or Lifetime-Value pro Nutzer:in {#lifetime-value-per-user}

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, Kurzmitteilungsdienst or SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='LTV or Lifetime-Value or Lifetime-Value Per User' %}

{% endapi %}

{% api %}

## Durchschnittlicher Tagesumsatz {#average-daily-revenue}

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, Kurzmitteilungsdienst or SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Average Daily Revenue' %}

{% endapi %}

{% api %}

## Tägliche Käufe {#daily-purchases}

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, Kurzmitteilungsdienst or SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Daily Purchases' %}

{% endapi %}

{% api %}

## Tagesumsatz pro Nutzer:in {#daily-revenue-per-user}

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, Kurzmitteilungsdienst or SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Daily Revenue Per User' %}

{% endapi %}

{% api %}

## Maschinelle Öffnungen {#machine-opens}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Machine Opens' %} Diese Metrik wird seit dem 11. November 2021 für SendGrid und seit dem 2. Dezember 2021 für SparkPost getrackt. Für Amazon SES werden die Analytics als _Öffnungen_ angezeigt. Bot-Filterung für Klicks wird jedoch unterstützt.

{% endapi %}

{% api %}

## Öffnungen {#opens}

{% apitags %}
Web Push, iOS Push, Android Push
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Opens' %}

{% endapi %}

{% api %}

## Opt-Out {#opt-out}

{% apitags %}
Kurzmitteilungsdienst or SMS/MMS, RCS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Opt-Out' %} Eine Nutzerantwort wird jedes Mal gemessen, wenn Nutzer:innen innerhalb von vier Stunden nach Erhalt Ihrer Nachricht eine eingehende Nachricht senden.

{% endapi %}

{% api %}

## Sonstige Öffnungen {#other-opens}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Other Opens' %} Beachten Sie, dass Nutzer:innen eine E-Mail auch öffnen können (wobei die Öffnung zu den sonstigen Öffnungen zählt), bevor eine maschinelle Öffnung protokolliert wird. Wenn Nutzer:innen eine E-Mail einmal (oder öfter) nach einem maschinellen Öffnungs-Event aus einem Nicht-Apple-Mail-Posteingang öffnen, wird die Anzahl der Male, die die Nutzer:innen die E-Mail öffnen, zu den sonstigen Öffnungen gezählt und nur einmal zu den eindeutigen Öffnungen.

{% endapi %}

{% api %}

## Ausstehender Wiederholungsversuch {#pending-retry}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Pending Retry' %}

{% endapi %}

{% api %}

## Primäre Conversions (A) oder primäres Konversions-Event {#primary-conversions-a-or-primary-conversion-event}

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, Kurzmitteilungsdienst or SMS/MMS, WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Primary Conversions (A) or Primary Conversion Event' %}

| Kanal | Zusätzliche Informationen |
|-------|-----------------------|
| E-Mail, Push, Webhooks | Nach dem ersten Versand. |
| Content Cards, In-App-Nachrichten | Wenn die Nutzer:innen die Content Card oder Nachricht zum ersten Mal ansehen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Primäre Conversions (A) oder primäres Konversions-Event" }

{::nomarkdown}
<span class="calculation-line">
    Berechnung:
    <ul>
        <li><i>Primäre Conversions (A) oder primäres Konversions-Event</i>: Anzahl</li>
        <li><i>Primäre Conversions (A) %</i> oder <i>Primäre Konversions-Event-Rate</i>: (Primäre Conversions) / (Eindeutige Empfänger:innen)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

## Gelesen {#reads}

{% apitags %}
WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Reads' %}

{% endapi %}

{% api %}

## Leserate {#read-rate}

{% apitags %}
WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Read Rate' %}

<span class="calculation-line">Berechnung: (Gelesen mit Lesebestätigungen) / (Sends)</span>

{% endapi %}

{% api %}

## Erhalten {#received}

{% apitags %}
Email, Content Cards, In-App Message, Web Push, iOS Push, Android Push, Kurzmitteilungsdienst or SMS/MMS, WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Received' %}

| Kanal | Zusätzliche Informationen |
|-------|-------|
| Content Cards | Erhalten, wenn Nutzer:innen die Card in der App ansehen. |
| Push | Erhalten, wenn Nachrichten vom Braze-Server an den Push-Anbieter gesendet werden. |
| E-Mail | Erhalten, wenn Nachrichten vom Braze-Server an den E-Mail-Anbieter gesendet werden. |
| Kurzmitteilungsdienst or SMS/MMS | „Zugestellt“, nachdem der Kurzmitteilungsdienst or SMS-Anbieter eine Bestätigung vom vorgelagerten Carrier und dem Zielgerät erhalten hat. |
| In-App-Nachricht | Erhalten zum Zeitpunkt der Anzeige basierend auf der definierten Trigger or triggern-Aktion. |
| WhatsApp | Erhalten zum Zeitpunkt der Anzeige basierend auf der definierten Trigger or triggern-Aktion. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Erhalten" }

{% endapi %}

{% api %}

## RCS-Ablehnungen oder Kurzmitteilungsdienst or SMS-Ablehnungen {#rcs-rejections-or-sms-rejections}

{% apitags %}
Kurzmitteilungsdienst or SMS/MMS, RCS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Rejections' %} Als Braze-Kund:in werden Ablehnungen auf Ihr Kurzmitteilungsdienst or SMS-Kontingent angerechnet.

{::nomarkdown}
<span class="calculation-line">
    Berechnung:
    <ul>
        <li><i>Ablehnungen</i>: Anzahl</li>
        <li><i>Ablehnungsrate</i>: (Ablehnungen) / (Sends)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

## Umsatz {#revenue}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Revenue' %}

{% endapi %}

{% api %}

## Gesendet {#sent}

{% apitags %}
Kurzmitteilungsdienst or SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Sent' %}

<span class="calculation-line">Berechnung: Anzahl</span>

{% endapi %}

{% api %}

## Sends {#sends}

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, Kurzmitteilungsdienst or SMS/MMS, RCS, WhatsApp, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Sends' %} Diese Metrik wird von Braze bereitgestellt. Beachten Sie, dass beim Start einer geplanten Campaign diese Metrik alle gesendeten Nachrichten umfasst, unabhängig davon, ob sie aufgrund von Rate-Limiting bereits versendet wurden oder nicht.

{% alert tip %}
Für Content Cards wird diese Metrik je nach Ihrer Auswahl für die [Card-Erstellung]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card/card_creation) unterschiedlich berechnet:

- **Beim Start oder Schritteintritt:** Die Anzahl der erstellten und verfügbaren Cards. Dies zählt nicht, ob die Nutzer:innen die Card angesehen haben.
- **Bei der ersten Impression:** Die Anzahl der den Nutzer:innen angezeigten Cards.
{% endalert %}

<span class="calculation-line">Berechnung: Anzahl</span>

{% endapi %}

{% api %}

## Gesendete Nachrichten {#messages-sent}

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, Kurzmitteilungsdienst or SMS/MMS, WhatsApp, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Messages Sent' %}  Diese Metrik wird von Braze bereitgestellt. Beachten Sie, dass beim Start einer geplanten Campaign diese Metrik alle gesendeten Nachrichten umfasst, unabhängig davon, ob sie aufgrund von Rate-Limiting bereits versendet wurden oder nicht.

{% alert tip %}
Für Content Cards wird diese Metrik je nach Ihrer Auswahl für die [Card-Erstellung]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card/card_creation) unterschiedlich berechnet:

- **Beim Start oder Schritteintritt:** Die Anzahl der erstellten und verfügbaren Cards. Dies zählt nicht, ob die Nutzer:innen die Card angesehen haben.
- **Bei der ersten Impression:** Die Anzahl der den Nutzer:innen angezeigten Cards.
{% endalert %}

<span class="calculation-line">Berechnung: Anzahl</span>

{% endapi %}

{% api %}

## Sends an Carrier {#sends-to-carrier}

{% apitags %}
Kurzmitteilungsdienst or SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Sends to Carrier' %}

{::nomarkdown}
<span class="calculation-line">
    Berechnung:
    <ul>
        <li><i>Sends an Carrier</i>: Anzahl</li>
        <li><i>Sends-an-Carrier-Rate</i>: (Sends an Carrier) / (Sends)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

## Soft Bounce {#soft-bounce}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Soft Bounce' %} Wenn eine E-Mail einen Soft Bounce erhält, wird in der Regel innerhalb von 72 Stunden ein erneuter Versuch unternommen, wobei die Anzahl der Wiederholungsversuche je nach Empfänger:in variiert.

Beachten Sie, dass sich _Soft Bounces_ von _Deferrals_ unterscheiden. Wenn während dieses Wiederholungszeitraums keine E-Mail erfolgreich zugestellt wird, sendet Braze ein Soft-Bounce-Event pro versuchtem Campaign-Versand. Vor dem 25. Februar 2025 wurden diese Wiederholungsversuche als mehrere Soft Bounces für einen Campaign-Versand gezählt.

Obwohl Soft Bounces nicht in Ihren Campaign-Analytics getrackt werden, können Sie die Soft Bounces im [Nachrichten-Aktivitätsprotokoll]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) überwachen. Sie können diese Nutzer:innen auch von Ihrem Versand ausschließen oder die Anzahl der Soft Bounces der letzten 30 Tage mit dem [Soft-Bounced-Segmentfilter]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#soft-bounced) einsehen. Im Nachrichten-Aktivitätsprotokoll können Sie auch den Grund für die Soft Bounces sehen und mögliche Abweichungen zwischen den „Sends“ und „Zustellungen“ für Ihre E-Mail-Campaigns nachvollziehen.

{% endapi %}

{% api %}

## Spam {#spam}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Spam' %}

{% alert note %}
Spam-Beschwerden werden direkt von E-Mail-Anbietern bearbeitet und dann über eine Feedback-Schleife an Braze weitergeleitet. Die meisten Feedback-Schleifen melden nur einen Teil der tatsächlichen Beschwerden, sodass die _Spam_-Metrik oft nur einen Bruchteil der tatsächlichen Gesamtzahl darstellt. Nur E-Mail-Anbieter können das tatsächliche Volumen der Spam-Beschwerden einsehen, was bedeutet, dass _Spam_ als indikative, nicht erschöpfende Metrik betrachtet werden sollte.
{% endalert %}

{::nomarkdown}
<span class="calculation-line">
    Berechnung:
    <ul>
        <li><i>Spam</i>: Anzahl</li>
        <li><i>Spam %</i> oder <i>Spam-Rate %</i>: (Als Spam markiert) / (Sends)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

## Umfrageseiten-Abweisungen {#survey-page-dismissals}

{% apitags %}
In-App Message
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Survey Page Dismissals' %}

{% endapi %}

{% api %}

## Umfrage-Einreichungen {#survey-submissions}

{% apitags %}
In-App Message
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Survey Submissions' %}

{% endapi %}

{% api %}

## Klicks insgesamt {#total-clicks}

{% apitags %}
Email, Content Cards, Kurzmitteilungsdienst or SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Clicks' %}

| Kanal | Zusätzliche Informationen |
|-------|-------|
| LINE | Wird getrackt, nachdem ein Mindestschwellenwert von 20 Nachrichten pro Tag erreicht wurde. AMP or Accelerated Mobile Pages-E-Mails umfassen Klicks, die sowohl in HTML- als auch in Nur-Text-Versionen erfasst werden. Diese Zahl kann durch Anti-Spam-Tools künstlich erhöht sein. |
| Banner | Die Gesamtzahl (und der Prozentsatz) der Nutzer:innen, die innerhalb der zugestellten Nachricht geklickt haben, unabhängig davon, ob dieselben Nutzer:innen mehrfach klicken. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Klicks insgesamt" }

{::nomarkdown}
<span class="calculation-line">
    Berechnung:
    <ul>
        <li><b>E-Mail:</b> (Klicks insgesamt) / (Zustellungen)</li>
        <li><b>Content Cards:</b> (Klicks insgesamt) / (Impressionen insgesamt)</li>
        <li><b>Kurzmitteilungsdienst or SMS:</b> (Klick-Öffnungen) / (Zustellungen)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

## Abweisungen insgesamt {#total-dismissals}

{% apitags %}
Content Cards, Banners
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Dismissals' %} Wenn Nutzer:innen bei Content Cards zwei verschiedene Cards aus derselben Campaign erhalten und beide abweisen, erhöht sich diese Zahl um zwei. Die erneute Berechtigung ermöglicht es, die _Abweisungen insgesamt_ jedes Mal zu erhöhen, wenn Nutzer:innen eine Card erhalten; jede Card ist eine separate Nachricht. Bei Bannern wird jede Abweisung gezählt, wenn das Abweisungsverhalten aktiviert ist.

{::nomarkdown}
<span class="calculation-line">
    Berechnung:
    <ul>
        <li><i>Abweisungen insgesamt:</i> Anzahl</li>
        <li><i>Abweisungsrate insgesamt:</i> Abweisungen insgesamt / Impressionen insgesamt</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

## Impressionen insgesamt {#total-impressions}

{% apitags %}
In-App Message, Content Cards
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Impressions' %} Diese Zahl ist eine Summe der Impressions-Events, die Braze von den SDKs erhält.

| Kanal | Zusätzliche Informationen |
|-------|-----------------------|
| Content Cards | Die Gesamtzahl der für eine bestimmte Content Card protokollierten Impressionen. Diese kann für dieselben Nutzer:innen mehrfach erhöht werden. |
| In-App-Nachrichten | Wenn es mehrere Geräte gibt und die erneute Berechtigung deaktiviert ist, sollten die Nutzer:innen die In-App-Nachricht nur einmal sehen. Selbst wenn die Nutzer:innen mehrere Geräte verwenden, sehen sie die Nachricht nur auf dem ersten Gerät, das angesprochen wird. Dies setzt voraus, dass das Profil konsolidierte Geräte hat und die Nutzer:innen eine Nutzer-ID haben, mit der sie geräteübergreifend angemeldet sind. Wenn die erneute Berechtigung aktiviert ist, wird eine Impression jedes Mal protokolliert, wenn die Nutzer:innen die In-App-Nachricht sehen. Weitere Details finden Sie unter <a href="/docs/user_guide/channels/in_app_messages/reporting">In-App-Nachrichten-Reporting</a>. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Impressionen insgesamt" }

<span class="calculation-line">Berechnung: Anzahl</span>

{% endapi %}

{% api %}

## Öffnungen insgesamt {#total-opens}

{% apitags %}
Email, iOS Push, Android Push, Web Push, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Opens' %}

| Kanal | Zusätzliche Informationen |
|-------|-----------------------|
| LINE | Wird getrackt, nachdem ein Mindestschwellenwert von 20 Nachrichten pro Tag erreicht wurde. |
| AMP or Accelerated Mobile Pages-E-Mails | Die Gesamtöffnungen für die HTML- und Nur-Text-Versionen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Öffnungen insgesamt" }

{::nomarkdown}
<span class="calculation-line">
    Berechnung:
    <ul>
        <li><b>E-Mail <i>Öffnungen insgesamt</i>:</b> Anzahl</li>
        <li><b>E-Mail <i>Öffnungsrate insgesamt</i>:</b> (Öffnungen) / (Zustellungen)</li>
        <li><b>Web-Push <i>Öffnungen insgesamt</i>:</b> Anzahl der <i>direkten Öffnungen</i></li>
        <li><b>Web-Push <i>Öffnungsrate insgesamt</i>:</b> (Öffnungen insgesamt) / (Zustellungen)</li>
        <li><b>iOS-, Android- und Kindle-Push <i>Öffnungen insgesamt</i>:</b> (Direkte Öffnungen) + (Beeinflusste Öffnungen)</li>
        <li><b>iOS-, Android- und Kindle-Push <i>Öffnungsrate insgesamt</i>:</b> (Öffnungen insgesamt) / (Zustellungen)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

## Gesamtumsatz {#total-revenue}

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, Kurzmitteilungsdienst or SMS/MMS, WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Revenue' %} Diese Metrik ist nur in Campaign-Vergleichsberichten über den <a href='/docs/user_guide/analytics/reports/report_builder'>Berichts-Builder</a> verfügbar.

{% endapi %}

{% api %}

## Eindeutige Klicks {#unique-clicks}

{% apitags %}
Email, Content Cards, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Clicks' %}

Dies umfasst Klicks auf von Braze bereitgestellte Abmeldelinks.

| Kanal | Zusätzliche Informationen |
|-------|-----------------------|
| E-Mail | Wird über einen Zeitraum von sieben Tagen getrackt. |
| LINE | Wird getrackt, nachdem ein Mindestschwellenwert von 20 Nachrichten pro Tag erreicht wurde. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Eindeutige Klicks" }

{::nomarkdown}
<span class="calculation-line">
    Berechnung:
    <ul>
        <li><i>Eindeutige Klicks</i>: Anzahl</li>
        <li><b>Content Cards</b> <i>Eindeutige Klicks %</i> oder <i>Eindeutige Klickrate</i>: (Eindeutige Klicks) / (Eindeutige Impressionen)</li>
        <li><b>E-Mail</b> <i>Eindeutige Klicks %</i> oder <i>Eindeutige Klickrate</i>: (Eindeutige Klicks) / (Zustellungen)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

## Eindeutige Abweisungen {#unique-dismissals}

{% apitags %}
Content Cards
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Dismissals' %}

<span class="calculation-line">Berechnung: (Eindeutige Abweisungen) / (Eindeutige Impressionen)</span>

{% endapi %}

{% api %}

## Eindeutige tägliche Impressionen {#unique-daily-impressions}

{% apitags %}
Content Cards, Banners
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Daily Impressions' %}

Diese Zahl wird von Braze bereitgestellt und basiert auf der `user_id`. Eindeutige tägliche Impressionen werden auf Campaign- oder Canvas-Schritt-Ebene gezählt.

<span class="calculation-line">Berechnung: Anzahl</span>

{% endapi %}

{% api %}

## Eindeutige Impressionen {#unique-impressions}

{% apitags %}
In-App Message, Content Cards
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Impressions' %}

| Kanal | Zusätzliche Informationen |
|-------|-----------------------|
| In-App-Nachrichten | Eindeutige Impressionen können an einem neuen Kalendertag in der Zeitzone Ihres Workspace erneut erhöht werden, wenn die erneute Berechtigung aktiviert ist und die Nutzer:innen die Trigger or triggern-Aktion ausführen. Wenn die erneute Berechtigung aktiviert ist, gilt <i>Eindeutige Impressionen</i> = <i>Eindeutige Empfänger:innen</i>. Weitere Details finden Sie unter <a href="/docs/user_guide/channels/in_app_messages/reporting">In-App-Nachrichten-Reporting</a>. |
| Content Cards | Die Zählung sollte sich nicht erhöhen, wenn Nutzer:innen eine Card ein zweites Mal ansehen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Eindeutige Impressionen" }

<span class="calculation-line">Berechnung: Anzahl</span>

{% endapi %}

{% api %}

## Eindeutige Öffnungen {#unique-opens}

{% apitags %}
Email, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Opens' %} Bei der Auswertung eines bestimmten Zeitraums können die <i>eindeutigen Öffnungen</i> höher erscheinen als die <i>Sends</i> für denselben Zeitraum. Dies kann auftreten, weil Nutzer:innen möglicherweise noch Öffnungs-Events für Nachrichten protokollieren, die außerhalb dieses Zeitraums gesendet wurden. Über die gesamte Campaign-Dauer sind die <i>eindeutigen Öffnungen</i> immer niedriger als die gesamten <i>Sends</i>.

| Kanal | Zusätzliche Informationen |
|-------|-----------------------|
| E-Mail | Wird über einen Zeitraum von 7 Tagen getrackt. |
| LINE | Wird getrackt, nachdem ein Mindestschwellenwert von 20 Nachrichten pro Tag erreicht wurde. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Eindeutige Öffnungen" }

{::nomarkdown}
<span class="calculation-line">
    Berechnung:
    <ul>
        <li><i>Eindeutige Öffnungen</i>: Anzahl</li>
        <li><i>Eindeutige Öffnungen %</i> oder <i>Eindeutige Öffnungsrate</i>: (Eindeutige Öffnungen) / (Zustellungen)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

## Eindeutige Empfänger:innen {#unique-recipients}

{% apitags %}
Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, Kurzmitteilungsdienst or SMS/MMS, RCS, WhatsApp, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Recipients' %}

Da ein:e Betrachter:in jeden Tag ein:e eindeutige:r Empfänger:in sein kann, sollten Sie erwarten, dass dieser Wert höher ist als die <i>eindeutigen Impressionen</i>. Diese Zahl wird von Braze bereitgestellt und basiert auf der `user_id`. Eindeutige Empfänger:innen werden auf Campaign- oder Canvas-Schritt-Ebene gezählt, nicht auf der Ebene des <a href='{{ site.homeurl }}{{ site.baseurl }}/api/identifier_types/#send-identifier'>Send-Identifiers</a>.

Nutzer:innen, die einen Bounce verursachen, zählen weiterhin zu den <i>eindeutigen Empfänger:innen</i>, wenn Braze sie als Empfänger:in für diesen Versandtag zählt. <i>Eindeutige Empfänger:innen</i> basieren auf den Nutzer:innen, die Braze für die Nachricht an diesem Tag angesprochen hat, nicht nur auf erfolgreichen Zustellungen.

<span class="calculation-line">Berechnung: Anzahl</span>

{% endapi %}

{% api %}

## Abmelder:innen oder Abmeldungen {#unsubscribers-or-unsub}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unsubscribers or Unsub' %}

{::nomarkdown}
<span class="calculation-line">
    Berechnung:
    <ul>
        <li><i>Abmelder:innen</i> oder <i>Abmeldungen</i>: Anzahl</li>
        <li><i>Abmelder:innen %</i> oder <i>Abmelderate</i>: (Abmeldungen) / (Zustellungen)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

## Abmeldungen {#unsubscribes}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unsubscribes' %}

<span class="calculation-line">Berechnung: (Abmeldungen) / (Zustellungen)</span>

{% endapi %}

{% api %}

## Variante {#variation}

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, Kurzmitteilungsdienst or SMS/MMS, WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Variation' %}

<span class="calculation-line">Berechnung: Anzahl</span>

{% endapi %}