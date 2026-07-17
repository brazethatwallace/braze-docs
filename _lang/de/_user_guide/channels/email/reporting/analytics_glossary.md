---
nav_title: E-Mail-Analyse-Glossar
article_title: E-Mail-Analyse-Glossar
layout: email_report_metrics
page_order: 0
excerpt_separator: ""
page_type: glossary
description: "Dieses Glossar enthält die Begriffe, die Sie im Analysebereich Ihrer E-Mail-Campaign oder Ihres Canvas nach dem Start finden werden. Dieses Glossar enthält keine Currents-Metriken."
channel:
  - email
---

> Dieses Glossar definiert Metriken auf dem **Analytics**-Tab für E-Mail-Campaigns und Canvases. Braze bietet keine gehostete Seite „Diese E-Mail im Browser anzeigen“ an – siehe [Kann ich einen „Diese E-Mail im Browser anzeigen“-Link zu meinen E-Mails hinzufügen?]({{site.baseurl}}/user_guide/channels/email/faq#can-i-add-a-view-this-email-in-a-browser-link-to-my-emails) für eine Problemumgehung. Weitere Fehlerbehebung, die mehrere Metriken betrifft, finden Sie unter [E-Mail-FAQ]({{site.baseurl}}/user_guide/channels/email/faq).

<style>
  .calculation-line {
    color: #76848C;
    font-size: 14px;
  }
</style>

{% api %}

### Variante {#variation}

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Variation' %}

<span class="calculation-line">Berechnung: Anzahl</span>

{% endapi %}

{% api %}

### Emailable {#emailable}

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Emailable' %}

<span class="calculation-line">Berechnung: Anzahl</span>

{% endapi %}

{% api %}

### Zielgruppe % {#audience}

{% apitags %}
Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Audience' %}

<span class="calculation-line">Berechnung: (Anzahl der Empfänger:innen in der Variante) / (Eindeutige Empfänger:innen)</span>

{% endapi %}

{% api %}

### Eindeutige Empfänger:innen {#unique-recipients}

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Recipients' %} Diese Zahl wird von Braze bereitgestellt.

<span class="calculation-line">Berechnung: Anzahl</span>

{% endapi %}

{% api %}

### Sends {#sends}

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Sends' %}  Diese Metrik wird von Braze bereitgestellt.

<span class="calculation-line">Berechnung: Anzahl</span>

{% endapi %}

{% api %}

### Gesendete Nachrichten {#messages-sent}

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Messages Sent' %}  Diese Metrik wird von Braze bereitgestellt.

<span class="calculation-line">Berechnung: Anzahl</span>

{% endapi %}

{% api %}

### Zustellungen {#deliveries}

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Deliveries' %} Bei E-Mails ist *Deliveries* die Gesamtzahl der Nachrichten (Sends), die erfolgreich an E-Mail-fähige Empfänger:innen gesendet und von diesen empfangen wurden.

<span class="calculation-line">Berechnung: (Sends) - (Bounces) </span>

{% alert note %}
Für den **Empfangen**-Status auf Nutzer:innen-Ebene und die zugehörige Logik (z. B. Frequency-Capping) markiert Braze Nutzer:innen in der Regel, wenn der Versand verarbeitet und zur Zustellung übergeben wird – nicht erst, wenn der E-Mail-Anbieter (ESP) die endgültige Zustellung an den Posteingang bestätigt. Dadurch werden Zeitverzögerungen zwischen der ESP-Bestätigung und den produktinternen Regeln vermieden. Dies kann von ESP- oder Drittanbieter-Zustellberichten abweichen.
{% endalert %}

{% endapi %}

{% api %}

### Zustellungen %

{% apitags %}
Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Deliveries %' %}

<span class="calculation-line">Berechnung: (Sends - Bounces) / (Sends) </span>

{% endapi %}

{% api %}

### Bounces {#bounces}

{% apitags %}
Count, Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Bounces' %}

Bei E-Mails ist *Bounce %* oder *Bounce-Rate* der Prozentsatz der Nachrichten, die nicht erfolgreich gesendet wurden oder als „zurückgesendet“ bzw. „nicht empfangen“ von den verwendeten Versanddiensten gekennzeichnet wurden oder von den vorgesehenen E-Mail-fähigen Nutzer:innen nicht empfangen wurden.

Ein E-Mail-Bounce für Kund:innen, die SendGrid verwenden, umfasst Hard Bounces, Spam (`spam_report_drops`) und E-Mails, die an ungültige Adressen gesendet wurden (`invalid_emails`).

{% alert note %}
In [Braze-Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) werden temporäre ESP-Zurückstellungen häufig als Soft Bounces dargestellt. Zustellbarkeits-Tools (z. B. native SendGrid-Berichte oder Looker-Modelle) verwenden möglicherweise Zurückstellungen für dieselbe Situation. Zurückstellungen sind in der Regel vorübergehend, und die E-Mail wird nach Wiederholungsversuchen oft zugestellt. Nach längeren Wiederholungsversuchen (bis zu ca. 72 Stunden für Soft Bounces in Campaign-Analytics) kann eine Nachricht je nach ESP als unzustellbar behandelt werden. Currents-E-Mail-Ereignisse sind append-only – ein protokollierter Soft Bounce wird nicht nachträglich entfernt, wenn die Nachricht schließlich zugestellt wird.
{% endalert %}

{::nomarkdown}
<span class="calculation-line">
    Berechnung:
    <ul>
        <li><b><i>Bounces</i>:</b> Anzahl</li>
        <li><b><i>Bounce %</i> oder <i>Bounce-Rate %</i>:</b> (Bounces) / (Sends)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Hard Bounce {#hard-bounce}

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Hard Bounce' %}

Wenn eine E-Mail einen Hard Bounce verursacht oder als Spam markiert wird, kennzeichnet Braze die E-Mail-Adresse als ungültig, aktualisiert jedoch nicht den [Abo-Status]({{site.baseurl}}/user_guide/channels/email/subscriptions) der Nutzer:innen. Braze stoppt alle zukünftigen Sendungen an diese E-Mail-Adresse. Um eine E-Mail-Adresse von Ihrer Hard-Bounce-Liste zu entfernen, verwenden Sie den [Endpunkt zum Entfernen von Hard-Bounce-E-Mails]({{site.baseurl}}/api/endpoints/email/post_remove_hard_bounces).

<span class="calculation-line">Berechnung: Anzahl </span>

{% endapi %}

{% api %}

### Soft Bounce {#soft-bounce}

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Soft Bounce' %} Wenn eine E-Mail einen Soft Bounce verursacht, wird in der Regel innerhalb von 72 Stunden ein erneuter Zustellversuch unternommen, wobei die Anzahl der Wiederholungsversuche je nach Empfänger:in variiert.

Obwohl Soft Bounces nicht in Ihren Campaign-Analytics erfasst werden, können Sie die Soft Bounces im [Nachrichten-Aktivitätsprotokoll]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) überwachen oder diese Nutzer:innen mit dem [Soft-Bounce-Segment-Filter]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#soft-bounced) von Ihrem Versand ausschließen. Im Nachrichten-Aktivitätsprotokoll können Sie auch den Grund für die Soft Bounces einsehen und mögliche Abweichungen zwischen den „Sends“ und „Deliveries“ Ihrer E-Mail-Campaigns nachvollziehen.

<span class="calculation-line">Berechnung: Anzahl </span>

{% endapi %}

{% api %}

### Spam {#spam}

{% apitags %}
Count, Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Spam' %}

{::nomarkdown}
<span class="calculation-line">
    Berechnung:
    <ul>
        <li><b><i>Spam</i>:</b> Anzahl</li>
        <li><b><i>Spam %</i> oder <i>Spam-Rate %</i>:</b> (Als Spam markiert) / (Sends)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Eindeutige Öffnungen {#unique-opens}

{% apitags %}
Count, Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Opens' %} Bei E-Mails wird dies über einen Zeitraum von sieben Tagen erfasst. Das bedeutet, dass ein:e einzelne:r Nutzer:in, der/die dieselbe E-Mail nach sieben Tagen erneut öffnet, als neue eindeutige Öffnung gezählt wird. Daher können die Zähler für eindeutige Öffnungen im Dashboard höher sein als eine einfache `DISTINCT user_id`-Abfrage auf Currents-Daten. Um die Dashboard-Zähler mit Currents abzugleichen, filtern Sie nach Ereignissen, bei denen `is_unique` den Wert `true` hat.

{::nomarkdown}
<span class="calculation-line">
    Berechnung:
    <ul>
        <li><b><i>Unique Opens</i>:</b> Anzahl</li>
        <li><b><i>Unique Opens %</i> oder <i>Unique Open Rate</i>:</b> (Unique Opens) / (Deliveries)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Eindeutige Klicks {#unique-clicks}

{% apitags %}
Count, Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Clicks' %} Dies wird bei E-Mails über einen Zeitraum von sieben Tagen erfasst und anhand der <a href='/docs/user_guide/messaging/messaging_fundamentals/dispatch_id'>dispatch_id</a> (ein einzelner Sendeversuch) gemessen. Dies umfasst Klicks auf von Braze bereitgestellte Abmeldelinks. Erfasste angepasste Abmelde-URLs zählen ebenfalls zu den *Unique Clicks*, wenn Nutzer:innen den Link auswählen. Nach sieben Tagen wird ein weiterer eindeutiger Klick für dieselbe:n Nutzer:in gezählt, wenn er/sie erneut klickt. E-Mail-Engagement-Metriken im Dashboard, einschließlich _Unique Clicks_, werden in Braze berechnet und nicht mit aggregierten ESP-Berichten abgeglichen. Um die Dashboard-Zähler mit Currents abzugleichen, filtern Sie nach Ereignissen, bei denen `is_unique` den Wert `true` hat.

{::nomarkdown}
<span class="calculation-line">
    Berechnung:
    <ul>
        <li><b><i>Unique Clicks</i>:</b> Anzahl</li>
        <li><b><i>Unique Clicks %</i> oder <i>Klickrate</i>:</b> (Unique Clicks) / (Deliveries)</li>
    </ul>
</span>
{:/}

#### Unerwartete Links in der E-Mail-Heatmap {#unexpected-links-on-the-email-heatmap}

Wenn die [E-Mail-Heatmap]({{site.baseurl}}/user_guide/channels/email/reporting) Links anzeigt, die Sie nicht erwarten, überprüfen Sie den HTML-Code der Nachricht auf [Content Blocks]({{site.baseurl}}/user_guide/channels/email/drag_and_drop/dnd_editor_blocks) oder Abstände zwischen Wörtern, die erfasste URLs erzeugen. Verwenden Sie die **Link-Tabelle nach Gesamtklicks** in der Heatmap-Ansicht, um URLs zu identifizieren, die nicht mit dem sichtbaren Text übereinstimmen.

Braze expandiert Liquid-Tags nicht in der Nachrichtenvorschau, sodass der Heatmap-Renderer den angeklickten Link in der Vorschau nicht zuordnen kann. Dies ist das erwartete Verhalten. Der Heatmap-Renderer versucht, angeklickte URLs mit denen in der Nachricht abzugleichen. Wenn sich die URL erheblich unterscheidet, z. B. wenn die gesamte URL als Event-Eigenschaft übergeben wird, kann die Heatmap sie nicht identifizieren.

{% endapi %}

{% api %}

### Gesamtklicks {#total-clicks}

{% apitags %}
Count, Percentage
{% endapitags %}

<i>Total Clicks</i> ist die Gesamtzahl der Klicks von Nutzer:innen auf Links in der zugestellten E-Mail, einschließlich mehrfacher Klicks derselben Nutzer:innen. Dies umfasst Klicks auf Braze-Abmeldelinks und erfasste angepasste Abmelde-URLs.

Wenn *Total Clicks* deutlich höher ist als *Unique Clicks*, scannen Sicherheitstools oder Postfachanbieter Links, ohne dass Nutzer:innen die Nachricht öffnen. Vergleichen Sie *Unique Clicks*, wenn Sie das Engagement intern bewerten.

{% endapi %}

{% api %}

### Abmeldungen {#unsubscribers-or-unsub}

{% apitags %}
Count, Percentage
{% endapitags %}

_Abmeldungen_ beziehen sich auf den Standard-Abmeldelink von Braze. Angepasste Abmeldeseiten erhöhen diese Metrik nicht, es sei denn, Sie aktualisieren Nutzer:innen über die API. **Abo-Gruppen-Zeitreihen** spiegeln weiterhin API-gesteuerte Änderungen wider.

{% multi_lang_include analytics/metrics.md metric='Unsubscribers or Unsub' %}

{::nomarkdown}
<span class="calculation-line">
    Berechnung:
    <ul>
        <li><b><i>Unsubscribers</i> oder <i>Unsub</i>:</b> Anzahl</li>
        <li><b><i>Unsubscribers %</i> oder <i>Unsub Rate</i>:</b> (Unsubscribes) / (Deliveries)</li>
    </ul>
</span>
{:/}

#### Warum sich *Abmeldungen* und Klicks auf den Abmeldelink unterscheiden können {#why-unsubscribes-and-unsubscribe-link-clicks-can-differ}

Vergleichen Sie auf der **Analytics**-Seite einer E-Mail-Campaign oder eines Canvas die Anzahl der *Unsubscribes* mit den Klicks auf die Braze-Abmelde-URL in der Link-Aufschlüsselung, wenn Sie **Total Clicks** oder **Unique Clicks** aufklappen. Die beiden Werte stimmen oft überein, können aber abweichen:

- **Mehr *Unsubscribes* als Klicks auf die Abmelde-URL im E-Mail-Text:** [List-Unsubscribe]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences#list-unsubscribe) ist ein zusätzlicher Abmeldepfad im E-Mail-Header (nicht der Link in Ihrem Nachrichtentext). Wenn sich Nutzer:innen auf diesem Weg abmelden, wird dies zu den *Unsubscribes* gezählt, zählt aber nicht als Klick auf die erfasste Abmelde-URL im Text.
- **Mehr Klicks auf die Abmelde-URL im Text als *Unsubscribes*:** Nutzer:innen können diesen Link mehrmals auswählen. Wenn sie sich abmelden, erneut anmelden und sich wieder abmelden, kann die E-Mail-Analyse mehrere Klicks (z. B. zwei) in der Klick-Aufschlüsselung erfassen.

Weitere Informationen finden Sie unter [Warum sehe ich eine andere Anzahl von Abmeldungen als Klicks auf meinen Abmeldelink?]({{site.baseurl}}/user_guide/channels/email/faq#why-am-i-seeing-a-different-number-of-unsubscribes-than-clicks-on-my-unsubscribe-link).

{% endapi %}

{% api %}

### Umsatz {#revenue}

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Revenue' %}

<span class="calculation-line">Berechnung: Anzahl </span>

{% endapi %}

{% api %}

### Primäre Konversionen (A) oder primäres Konversions-Event {#primary-conversions-a-or-primary-conversion-event}

{% apitags %}
Count, Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Primary Conversions (A) or Primary Conversion Event' %} Bei E-Mails, Push und Webhooks beginnt das Tracking der Konversionen nach dem ersten Versand.

{::nomarkdown}
<span class="calculation-line">
    Berechnung:
    <ul>
        <li><b><i>Primary Conversions (A)</i> oder <i>Primary Conversion Event</i>:</b> Anzahl</li>
        <li><b><i>Primary Conversions (A) %</i> oder <i>Primary Conversion Event Rate</i>:</b> (Primary Conversions) / (Unique Recipients)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Konfidenz {#confidence}

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Confidence' %}

{% endapi %}

{% api %}

### Maschinelle Öffnungen {#machine-opens}

{% multi_lang_include analytics/metrics.md metric='Machine Opens' %} Diese Metrik wird seit dem 11. November 2021 für SendGrid und seit dem 2. Dezember 2021 für SparkPost erfasst.

<span class="calculation-line">Berechnung: Anzahl </span>

{% endapi %}

{% api %}

### Sonstige Öffnungen {#other-opens}

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Other Opens' %} Beachten Sie, dass Nutzer:innen eine E-Mail auch öffnen können (wobei die Öffnung zu <i>Other Opens</i> gezählt wird), bevor ein Zähler für <i>Machine Opens</i> protokolliert wird. Wenn Nutzer:innen eine E-Mail einmal (oder mehrmals) nach einem maschinellen Öffnungs-Ereignis aus einem Nicht-Apple-Mail-Posteingang öffnen, wird die Anzahl der Öffnungen zu <i>Other Opens</i> gezählt und nur einmal zu <i>Unique Opens</i>.

<span class="calculation-line">Berechnung: Anzahl </span>

{% endapi %}

{% api %}

### Geschätzte tatsächliche Öffnungen {#estimated-real-opens}

{% apitags %}
Count, Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Estimated Real Opens' %} Braze berechnet diese Schätzung neu, sobald neue Öffnungs- und Klickdaten eintreffen. Der Wert stabilisiert sich in der Regel einige Tage nach dem Versand, wird aber weiterhin aktualisiert, wenn neue qualifizierende Ereignisse auftreten.

{% endapi %}

{% api %}

### Click-to-Open-Rate {#click-to-open-rate}

{% apitags %}
Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Click-to-Open Rate' %}

<span class="calculation-line">Berechnung: (Unique Clicks) / (Unique Opens) (für E-Mail)</span>

#### Message-Open-Likelihood-Scores (Segmentierung) {#message-open-likelihood-scores-segmentation}

Der Segment-Filter [`Message Open Likelihood`]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#message-open-likelihood) bewertet auf einer Skala von 0–100 %, wie wahrscheinlich es ist, dass Nutzer:innen eine E-Mail öffnen. Nutzer:innen ohne ausreichende Versand- oder Öffnungshistorie für den Kanal werden als leer angezeigt. Bei E-Mails werden maschinelle Öffnungen aus der Berechnung ausgeschlossen, die die aktuelle Nachrichtenhistorie auf diesem Kanal verwendet (siehe [Message-Open-Likelihood-Filter für einzelne Kanäle]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_channel#individual-channels)).

{% endapi %}

## Fehlerbehebung und häufige Fragen zur E-Mail-Berichterstattung {#email-reporting-troubleshooting-and-faqs}

### Abmeldelinks und eindeutige Klicks {#unsubscribe-links-and-unique-clicks}

Wenn Empfänger:innen auf einen Abmeldelink klicken, zählt Braze dies als Klick, da die Aktion eine URL verwendet. Dies gilt sowohl für von Braze bereitgestellte Abmeldelinks als auch für angepasste Abmeldelinks in Ihrem Nachrichtentext. Diese Klicks fließen zusammen mit anderen Link-Klicks in *Unique Clicks* und *Total Clicks* ein. Metrikdefinitionen finden Sie unter [Eindeutige Klicks](#unique-clicks) und unter [Warum sehe ich eine andere Anzahl von Abmeldungen als Klicks auf meinen Abmeldelink?]({{site.baseurl}}/user_guide/channels/email/faq#why-am-i-seeing-a-different-number-of-unsubscribes-than-clicks-on-my-unsubscribe-link).

### Im Browser anzeigen {#view-in-browser}

Braze bietet keine integrierte Funktion „Diese E-Mail im Browser anzeigen“. Hosten Sie den E-Mail-Inhalt auf einer externen Landing-Page (z. B. Ihrer Website) und fügen Sie über das **Link**-Tool im E-Mail-Editor einen Link aus der Nachricht hinzu. Weitere Informationen finden Sie unter [Kann ich einen „Diese E-Mail im Browser anzeigen“-Link zu meinen E-Mails hinzufügen?]({{site.baseurl}}/user_guide/channels/email/faq#can-i-add-a-view-this-email-in-a-browser-link-to-my-emails).

### Aktualisierungen der angepassten Abmeldeseite {#custom-unsubscribe-page-updates}

Änderungen an Ihrer [angepassten Abmeldeseite]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences) werden innerhalb weniger Minuten wirksam. Aktive Sendungen verwenden einen kurzlebigen Cache der Seite, der beim Speichern von Änderungen aktualisiert wird.

### Bounces bei überschrittenem Kontingent und vollem Postfach {#over-quota-and-full-mailbox-bounces}

Ein Bounce wegen überschrittenem Kontingent oder vollem Postfach bedeutet, dass das Postfach der Empfänger:innen keine neuen E-Mails annehmen kann. Diese Adressen können bei neuen Registrierungen mit ungültigen oder riskanten Adressen auftreten oder bei lange inaktiven Profilen, deren Postfächer sich gefüllt haben, während sie inaktiv waren.

Überprüfen Sie die Bounce-Raten nach Segment und Quelle, entfernen Sie Adressen, die wiederholt Hard Bounces verursachen, oder setzen Sie sie auf inaktiv, und verwenden Sie bestätigtes oder doppeltes Opt-in für neue Abonnent:innen. Informationen zur Listenhygiene finden Sie unter [Zustellbarkeitsfallen und Spam-Traps]({{site.baseurl}}/user_guide/channels/email/email_setup/deliverability_pitfalls_and_spam_traps) und [E-Mail-Berichterstattung]({{site.baseurl}}/user_guide/channels/email/reporting#troubleshooting).

### 550 5.7.1 – Unerwünschte E-Mail {#550-571-unsolicited-mail}

Eine `550 5.7.1`-Antwort wie „Our system has detected that this message is likely unsolicited mail“ stammt häufig von strengen Postfachanbietern (z. B. Gmail), wenn Reputations- oder Engagement-Signale schlecht aussehen. Häufige Ursachen sind Spam-Beschwerden, geringes Engagement, gekaufte oder gemietete Listen und plötzliche Volumenspitzen.

Setzen Sie auf einwilligungsbasiertes Listenwachstum, setzen Sie inaktive Abonnent:innen auf inaktiv und überwachen Sie Beschwerde- und Bounce-Raten. Weitere Informationen finden Sie unter [Zustellbarkeitsfallen und Spam-Traps]({{site.baseurl}}/user_guide/channels/email/email_setup/deliverability_pitfalls_and_spam_traps).

### Gute E-Mail-Zustellraten {#good-email-deliverability-rates}

**Zustellung** gibt an, ob der empfangende Server Ihre Nachricht akzeptiert; Sie können dies mit Metriken wie *Deliveries* und Bounce-Rate messen. **Zustellbarkeit** (Posteingangsplatzierung) hängt von der Filterung des Anbieters ab und wird nicht als einzelne Braze-Metrik angezeigt.

Als allgemeine Richtlinie sollten Sie eine Zustellrate von nahezu 99 % mit Hard Bounces unter ca. 1 % anstreben und Öffnungen sowie Klicks für Engagement-Trends beobachten. Die genauen Zielwerte variieren je nach Branche und Versandmuster. Informationen zu Praktiken, die Ihre Reputation unterstützen, finden Sie unter [E-Mail-Zustellbarkeit verbessern]({{site.baseurl}}/user_guide/channels/email/best_practices/improve_deliverability) und [Zustellbarkeitsfallen und Spam-Traps]({{site.baseurl}}/user_guide/channels/email/email_setup/deliverability_pitfalls_and_spam_traps).

### „Campaign is already in delay window, so not enqueueing another“ {#campaign-is-already-in-delay-window-so-not-enqueueing-another}

In der Nachrichtenaktivität oder den Diagnoseprotokollen für [aktionsbasierte Campaigns]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery) bedeutet dieses Verarbeitungsergebnis, dass Braze einen doppelten Versand blockiert hat, während ein früherer Trigger für dieselbe:n Nutzer:in noch innerhalb des Zustellfensters der Campaign liegt. Eine Entprellungssperre verhindert mehrfaches Einreihen in die Warteschlange für denselben Trigger-Burst.

Dieses Ergebnis kann auch auftreten, wenn die Campaign **Sofort senden** anzeigt, sofern eine der folgenden Bedingungen zutrifft:

- Die Campaign verwendet ein [Ausnahme-Event]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/exit_criteria#exception-events) oder eine Sendezeitverzögerung, die das Timing beeinflusst.
- Nutzer:innen haben eine [Wiederzulassungs]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility)-Periode, sodass sie die Nachricht erst nach Ablauf dieses Fensters erneut erhalten können.
- Eine andere Campaign oder ein Canvas-Nachrichtenschritt mit höherer Priorität hat den Sendeplatz belegt, wenn sich Trigger überschneiden.

Wenn Nutzer:innen die Nachricht hätten erhalten sollen, dies aber nicht geschehen ist, prüfen Sie frühere Ergebnisse für denselben Trigger (z. B. E-Mail-Bounce oder nicht für den Kanal aktiviert). Eine andere Nachricht im selben Workflow hat diesen Versand möglicherweise verhindert.