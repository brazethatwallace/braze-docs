---
nav_title: E-Mail-Analyse-Glossar
article_title: E-Mail-Analyse-Glossar
layout: email_report_metrics
page_order: 0
excerpt_separator: ""
page_type: glossary
description: "Dieses Glossar enthält die Begriffe, die Sie im Analysebereich Ihrer E-Mail-Kampagne oder Ihres Canvas nach dem Start finden werden. Dieses Glossar enthält keine Currents-Metriken."
channel:
  - email
---

<style>
  .calculation-line {
    color: #76848C;
    font-size: 14px;
  }
</style>

{% api %}

### Variante

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Variation' %}

<span class="calculation-line">Berechnung: Anzahl</span>

{% endapi %}

{% api %}

### Per E-Mail versendbar

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Emailable' %}

<span class="calculation-line">Berechnung: Anzahl</span>

{% endapi %}

{% api %}

### Zielgruppe %

{% apitags %}
Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Audience' %}

<span class="calculation-line">Berechnung: (Zahl der Empfänger:innen in der Variante) / (Eindeutige Empfänger:innen)</span>

{% endapi %}

{% api %}

### Eindeutige Empfänger:innen

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Recipients' %} Diese Zahl wird von Braze bereitgestellt.

<span class="calculation-line">Berechnung: Anzahl</span>

{% endapi %}

{% api %}

### Sendungen

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Sends' %}  Diese Metrik wird von Braze bereitgestellt.

<span class="calculation-line">Berechnung: Anzahl</span>

{% endapi %}

{% api %}

### Nachrichten gesendet

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Messages Sent' %}  Diese Metrik wird von Braze bereitgestellt.

<span class="calculation-line">Berechnung: Anzahl</span>

{% endapi %}

{% api %}

### Zustellungen

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Deliveries' %} Bei E-Mails ist *Zustellungen* die Gesamtzahl der Nachrichten (Sendungen), die erfolgreich an E-Mail-fähige Empfänger:innen gesendet und von diesen empfangen wurden.

<span class="calculation-line">Berechnung: (Sendungen) - (Bounces) </span>

{% endapi %}

{% api %}

### Zustellungen %

{% apitags %}
Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Deliveries %' %}

<span class="calculation-line">Berechnung: (Sendungen - Bounces) / (Sendungen) </span>

{% endapi %}

{% api %}

### Bounces

{% apitags %}
Count, Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Bounces' %}

Bei E-Mails ist *Bounce %* oder *Bounce-Rate* der Prozentsatz der Nachrichten, die nicht erfolgreich gesendet wurden oder als „zurückgesendet“ bzw. „nicht empfangen“ von den verwendeten Versanddiensten gekennzeichnet wurden oder von den vorgesehenen E-Mail-fähigen Nutzer:innen nicht empfangen wurden.

Ein E-Mail-Bounce für Kund:innen, die SendGrid verwenden, umfasst Hard Bounces, Spam (`spam_report_drops`) und E-Mails, die an ungültige Adressen gesendet wurden (`invalid_emails`).

{::nomarkdown}
<span class="calculation-line">
    Berechnung:
    <ul>
        <li><b><i>Bounces</i>:</b> Anzahl</li>
        <li><b><i>Bounce %</i> oder <i>Bounce-Rate %</i>:</b> (Bounces) / (Sendungen)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Hard Bounce

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Hard Bounce' %}

Wenn eine E-Mail einen Hard Bounce verursacht oder als Spam markiert wird, kennzeichnet Braze die E-Mail-Adresse als ungültig, aktualisiert jedoch nicht den [Abo-Status]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/) der Nutzer:innen. Braze stoppt alle zukünftigen Sendungen an diese E-Mail-Adresse. Um eine E-Mail-Adresse von Ihrer Hard-Bounce-Liste zu entfernen, verwenden Sie den [Endpunkt zum Entfernen von Hard-Bounce-E-Mails]({{site.baseurl}}/api/endpoints/email/post_remove_hard_bounces/).

<span class="calculation-line">Berechnung: Anzahl </span>

{% endapi %}

{% api %}

### Soft Bounce

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Soft Bounce' %} Wenn eine E-Mail einen Soft Bounce verursacht, wird in der Regel innerhalb von 72 Stunden ein erneuter Zustellversuch unternommen, wobei die Anzahl der Wiederholungsversuche je nach Empfänger:in variiert.

Obwohl Soft Bounces nicht in Ihren Kampagnen-Analytics erfasst werden, können Sie die Soft Bounces im [Nachrichten-Aktivitätsprotokoll]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log/) überwachen oder diese Nutzer:innen mit dem [Soft-Bounce-Segment-Filter]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters/#soft-bounced) von Ihrem Versand ausschließen. Im Nachrichten-Aktivitätsprotokoll können Sie auch den Grund für die Soft Bounces einsehen und mögliche Abweichungen zwischen den „Sendungen“ und „Zustellungen“ Ihrer E-Mail-Campaigns nachvollziehen.

<span class="calculation-line">Berechnung: Anzahl </span>

{% endapi %}

{% api %}

### Spam

{% apitags %}
Count, Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Spam' %}

{::nomarkdown}
<span class="calculation-line">
    Berechnung:
    <ul>
        <li><b><i>Spam</i>:</b> Anzahl</li>
        <li><b><i>Spam %</i> oder <i>Spam-Rate %</i>:</b> (Als Spam markiert) / (Sendungen)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Eindeutige Öffnungen

{% apitags %}
Count, Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Opens' %} Bei E-Mails wird dies über einen Zeitraum von sieben Tagen erfasst. Das bedeutet, dass ein:e einzelne:r Nutzer:in, der/die dieselbe E-Mail nach sieben Tagen erneut öffnet, als neue eindeutige Öffnung gezählt wird. Daher können die Zähler für eindeutige Öffnungen im Dashboard höher sein als eine einfache `DISTINCT user_id`-Abfrage auf Currents-Daten. Um die Dashboard-Zähler mit Currents abzugleichen, filtern Sie nach Events, bei denen `is_unique` den Wert `true` hat.

{::nomarkdown}
<span class="calculation-line">
    Berechnung:
    <ul>
        <li><b><i>Eindeutige Öffnungen</i>:</b> Anzahl</li>
        <li><b><i>Eindeutige Öffnungen %</i> oder <i>Eindeutige Öffnungsrate</i>:</b> (Eindeutige Öffnungen) / (Zustellungen)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Eindeutige Klicks

{% apitags %}
Count, Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Clicks' %} Dies wird bei E-Mails über einen Zeitraum von sieben Tagen erfasst und anhand der <a href='/docs/help/help_articles/data/dispatch_id/'>dispatch_id</a> gemessen. Dies umfasst Klicks auf von Braze bereitgestellte Abmeldelinks. Nach sieben Tagen kann ein weiterer eindeutiger Klick für dieselbe:n Nutzer:in gezählt werden, wenn er/sie erneut klickt. Um die Dashboard-Zähler mit Currents abzugleichen, filtern Sie nach Events, bei denen `is_unique` den Wert `true` hat.

{::nomarkdown}
<span class="calculation-line">
    Berechnung:
    <ul>
        <li><b><i>Eindeutige Klicks</i>:</b> Anzahl</li>
        <li><b><i>Eindeutige Klicks %</i> oder <i>Klickrate</i>:</b> (Eindeutige Klicks) / (Zustellungen)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Abmeldungen oder Unsub

{% apitags %}
Count, Percentage
{% endapitags %}

*Abmeldungen* beziehen sich auf den Standard-Abmeldelink von Braze. Angepasste Abmeldeseiten erhöhen diese Metrik nicht, es sei denn, Sie aktualisieren Nutzer:innen über die API. **Abo-Gruppen-Zeitreihen** spiegeln weiterhin API-gesteuerte Änderungen wider.

{% multi_lang_include analytics/metrics.md metric='Unsubscribers or Unsub' %}

{::nomarkdown}
<span class="calculation-line">
    Berechnung:
    <ul>
        <li><b><i>Abmeldungen</i> oder <i>Unsub</i>:</b> Anzahl</li>
        <li><b><i>Abmeldungen %</i> oder <i>Abmelderate</i>:</b> (Abmeldungen) / (Zustellungen)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Umsatz

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Revenue' %}

<span class="calculation-line">Berechnung: Anzahl </span>

{% endapi %}

{% api %}

### Primäre Conversions (A) oder primäres Konversions-Event

{% apitags %}
Count, Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Primary Conversions (A) or Primary Conversion Event' %} Bei E-Mails, Push und Webhooks beginnt das Tracking der Conversions nach dem ersten Versand.

{::nomarkdown}
<span class="calculation-line">
    Berechnung:
    <ul>
        <li><b><i>Primäre Conversions (A)</i> oder <i>Primäres Konversions-Event</i>:</b> Anzahl</li>
        <li><b><i>Primäre Conversions (A) %</i> oder <i>Primäre Konversions-Event-Rate</i>:</b> (Primäre Conversions) / (Eindeutige Empfänger:innen)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Konfidenz

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Confidence' %}

{% endapi %}

{% api %}

### Maschinelle Öffnungen

{% multi_lang_include analytics/metrics.md metric='Machine Opens' %} Diese Metrik wird seit dem 11. November 2021 für SendGrid und seit dem 2. Dezember 2021 für SparkPost erfasst.

<span class="calculation-line">Berechnung: Anzahl </span>

{% endapi %}

{% api %}

### Sonstige Öffnungen

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Other Opens' %} Beachten Sie, dass ein:e Nutzer:in eine E-Mail auch öffnen kann (wobei die Öffnung zu <i>Sonstige Öffnungen</i> gezählt wird), bevor ein Zähler für <i>Maschinelle Öffnungen</i> protokolliert wird. Wenn ein:e Nutzer:in eine E-Mail einmal (oder mehrmals) nach einem maschinellen Öffnungs-Event aus einem Nicht-Apple-Mail-Posteingang öffnet, wird die Anzahl der Öffnungen durch die:den Nutzer:in zu <i>Sonstige Öffnungen</i> gezählt und nur einmal zu <i>Eindeutige Öffnungen</i>.

<span class="calculation-line">Berechnung: Anzahl </span>

{% endapi %}

{% api %}

### Klick-zu-Öffnungs-Rate

{% apitags %}
Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Click-to-Open Rate' %}

<span class="calculation-line">Berechnung: (Eindeutige Klicks) / (Eindeutige Öffnungen) (für E-Mail)</span>

{% endapi %}