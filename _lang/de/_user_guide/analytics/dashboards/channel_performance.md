---
nav_title: Kanal-Performance
article_title: Kanal-Performance-Dashboards
page_order: 2
page_type: reference
description: "Dieser Referenzartikel behandelt das Kanal-Performance-Dashboard, mit dem Sie Performance-Metriken für ganze Kanäle über Campaigns und Canvases hinweg anzeigen können."
tool:
  - Reports
toc_headers: h2
---

# Kanal-Performance-Dashboards {#channel-performance-dashboards}

> Kanal-Performance-Dashboards zeigen aggregierte Performance-Metriken für einen gesamten Kanal, sowohl aus Campaigns als auch aus Canvases. Diese Dashboards sind derzeit für E-Mail, Push und SMS verfügbar.

## Dashboards {#dashboards}

Wählen Sie einen Tab aus, um Details zu den verfügbaren Kanal-Performance-Dashboards anzuzeigen.

{% tabs %}
{% tab E-Mail-Performance %}

### E-Mail-Performance-Dashboard {#email-performance-dashboard}

Rufen Sie Ihr E-Mail-Performance-Dashboard auf, indem Sie zu **Analytics** > **Email Performance** navigieren und den Datumsbereich für den Zeitraum auswählen, für den Sie Daten anzeigen möchten. Ihr Datumsbereich kann bis zu ein Jahr in der Vergangenheit liegen.

![E-Mail-Performance-Dashboard, das das E-Mail-Kanal-Engagement der letzten dreißig Tage anzeigt.]({% image_buster /assets/img_archive/email_performance_dashboard_1.png %})

![Eine Beispiel-E-Mail-Campaign mit 335.630 Sends und einem Durchschnitt von 11.187,667 pro Tag.]({% image_buster /assets/img_archive/email_performance_dashboard_2.png %}){: style="max-width:40%;float:right;margin-left:15px;border:none;"}

#### Wie Metriken berechnet werden {#how-metrics-are-calculated}

{% multi_lang_include analytics/channel_performance_how_metrics_calculated.md channel="email" %}

| Metrik | Typ | Berechnung |
| --- | --- | ---- |
| Sends | Anzahl | Gesamtzahl der Sends über jeden Tag im Datumsbereich |
| Zustellrate | Rate | (Gesamtzahl der Zustellungen über jeden Tag im Datumsbereich) / (Gesamtzahl der Sends über jeden Tag im Datumsbereich) |
| Bounce-Rate | Rate | (Gesamtzahl der Bounces über jeden Tag im Datumsbereich) / (Gesamtzahl der Sends über jeden Tag im Datumsbereich) |
| Abmeldungsrate | Rate | (Gesamtzahl der eindeutigen Abmeldungen über jeden Tag im Datumsbereich) / (Gesamtzahl der Zustellungen für einen Datumsbereich)<br><br>Hier werden eindeutige Abmeldungen verwendet, die auch in Campaign-Analytics, der Übersicht und dem Berichts-Builder genutzt werden. Diese Abmeldungen werden über alle Quellen hinweg erfasst (z. B. REST API, CSV-Importe, E-Mails und Listen-Abmeldungen). Die Abmeldungsraten in Campaign- und Canvas-Analytics sind Abmeldungen, die durch einen Klick auf den Abmeldelink in einer von Braze zugestellten E-Mail erfolgen.  |
| Eindeutige Öffnungsrate | Rate | (Gesamtzahl der eindeutigen Öffnungen über jeden Tag im Datumsbereich) / (Gesamtzahl der Zustellungen für einen Datumsbereich) |
| Sonstige Öffnungsrate | Rate | (Gesamtzahl der sonstigen Öffnungen über jeden Tag im Datumsbereich) / (Gesamtzahl der Zustellungen für den Datumsbereich)<br><br>Sonstige Öffnungen umfassen E-Mails, die nicht als maschinelle Öffnungen identifiziert wurden, z. B. wenn eine Nutzer:in eine E-Mail öffnet. Diese Metrik ist nicht eindeutig und ist eine Untermetrik der Gesamtöffnungen.  |
| Eindeutige Klickrate | Rate | (Gesamtzahl der eindeutigen Klicks über jeden Tag im Datumsbereich) / (Gesamtzahl der Zustellungen für einen Datumsbereich) |
| Eindeutige Klick-zu-Öffnungs-Rate | Rate | (Gesamtzahl der eindeutigen Klicks über jeden Tag im Datumsbereich) / (Gesamtzahl der eindeutigen Öffnungen über jeden Tag im Datumsbereich) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="How metrics are calculated" }

{% endtab %}
{% tab E-Mail-Insights %}

### E-Mail-Insights-Dashboard {#email-insights-dashboard}

Das E-Mail-Insights-Dashboard verfolgt, wo und wann Ihre Kund:innen mit Ihren E-Mails interagieren. Diese Berichte können umfangreiche und detaillierte Daten darüber liefern, wie Sie Ihre E-Mails optimieren können, um ein höheres Engagement zu erzielen. Das E-Mail-Insights-Dashboard enthält Daten von bis zu den letzten sechs Monaten. Um auf das Dashboard zuzugreifen, navigieren Sie zu **Analytics** > **Email Performance** > **Email Insights**.

#### Engagement nach Gerät {#engagement-by-device}

Der Bericht **Engagement by Device** bietet eine Aufschlüsselung darüber, welche Geräte Ihre Nutzer:innen verwenden, um mit Ihren E-Mails zu interagieren. Diese Daten verfolgen das E-Mail-Engagement über Mobilgeräte, Desktop, Tablet und andere Gerätetypen. Die Daten basieren auf dem User-Agent-String, der von den Geräten Ihrer Nutzer:innen übermittelt wird.

{% alert note %}
Wenn Sie CloudFront als Ihr CDN verwenden, stellen Sie sicher, dass der User-Agent Ihrer Nutzer:innen an den ESP weitergeleitet wird. Andernfalls wird jeder User-Agent als „Amazon Cloudfront“ angezeigt.
{% endalert %}

Die Kategorie „Other“ umfasst jeden User-String, der nicht als Desktop, Mobilgerät oder Tablet identifiziert werden kann. Zum Beispiel Fernseher, Auto, Spielekonsole, OTT (Over-the-Top oder Streaming) und ähnliches. Dies kann auch Null- oder leere Werte umfassen.

Um besser zu verstehen, was in dieser Kategorie „Other“ enthalten ist, können Sie die User-Agents mit einer der folgenden Optionen extrahieren:

1. [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/) sendet Ihnen den genauen User-Agent-String, der von den Geräten Ihrer Nutzer:innen abgerufen wurde.
2. Nutzen Sie unseren [Abfrage-Builder]({{site.baseurl}}/user_guide/analytics/reports/query_builder/), um SQL oder unseren [KI-Abfrage-Builder]({{site.baseurl}}/user_guide/analytics/reports/query_builder/#generating-sql-with-the-ai-query-builder) zu verwenden, um die User-Agents anzuzeigen.

![Bericht „Engagement by Device“, der die Anzahl der Klicks für Mobilgeräte, Desktop, Tablet und andere Geräte zeigt. Die meisten Klicks erfolgen auf Mobilgeräten.]({% image_buster /assets/img/engagement_by_device_type.png %}){: style="max-width:70%;"}

Bei E-Mail-Öffnungen trennt Braze Google Image Proxy, Apple Image Proxy und Yahoo Mail Proxy. Diese Dienste cachen und laden alle eingebetteten Bilder in einer E-Mail, bevor sie an die Empfänger:in zugestellt wird. Dadurch wird eine E-Mail-Öffnung von den Servern des Mailbox-Anbieters statt vom Server der Empfänger:in ausgelöst, was zu überhöhten E-Mail-Öffnungen führen kann. Diese Dienste sollen Datenschutz, Sicherheit, Performance und Effizienz beim Laden von Bildern verbessern. Dies kann auch echte Öffnungen von Empfänger:innen enthalten, da diese Proxy-Dienste den User-Agent maskieren und Braze Proxy-Daten anhand des User-Agents kategorisiert.

![Bericht „Engagement by Device“, der die Anzahl der Klicks für Mobilgerät, Desktop, Tablet, Apple Privacy Proxy, Google Image Proxy, Yahoo Mail Proxy und Other zeigt. Die meisten Öffnungen erfolgen auf Mobilgeräten.]({% image_buster /assets/img/engagement_by_device_type_proxy.png %}){: style="max-width:70%;"}

#### Engagement nach Mailbox-Anbieter {#engagement-by-mailbox-provider}

Der Bericht **Engagement by Mailbox Provider** zeigt die wichtigsten Mailbox-Anbieter an, die zu Ihren Klicks oder Öffnungen beitragen. Sie können auf bestimmte führende Mailbox-Anbieter klicken, um Details zu spezifischen Empfangs-Domains anzuzeigen. Wenn beispielsweise Microsoft in diesem Bericht als einer Ihrer Top-Mailbox-Anbieter aufgeführt ist, können Sie weitere Details zu deren Empfangs-Domains anzeigen, wie z. B. „outlook.com“, „hotmail.com“, „live.com“ und mehr.

![Ein Beispiel für den Bericht „Engagement by Mailbox Provider“ mit Google, Apple iCloud, Yahoo, Microsoft und Mail.Ru Group und der entsprechenden Anzahl von Klicks.]({% image_buster /assets/img_archive/mailbox_provider_time_engagement.png %}){: style="max-width:70%;"}

#### Zeitpunkt des Engagements {#time-of-engagement}

Der Bericht **Time of Engagement** zeigt Daten darüber an, wann Nutzer:innen mit Ihren E-Mails interagieren. Dies kann helfen, Fragen zu beantworten wie: An welchem Wochentag oder zu welcher Uhrzeit ist das Engagement Ihrer Kund:innen am höchsten? Mit diesen Insights können Sie experimentieren, an welchem Tag oder zu welcher Uhrzeit Sie Ihre Nachrichten senden sollten, um ein höheres Engagement zu erzielen. Beachten Sie, dass diese Zeiten auf der Zeitzone Ihres Unternehmens basieren.

Der Engagement-Bericht **Day of the week** schlüsselt Öffnungen oder Klicks nach Wochentag auf.

![Ein Beispiel für den Engagement-Bericht „Day of the week“ mit den meisten Klicks am Montag und Mittwoch.]({% image_buster /assets/img_archive/time_engagement.png %})

Der Engagement-Bericht **Time of the day** schlüsselt Öffnungen oder Klicks nach jeder Stunde in einem 24-Stunden-Zeitfenster auf.

![Ein Beispiel für den Engagement-Bericht „Time of the day“ mit Öffnungen oder Klicks von 0 Uhr bis 23 Uhr.]({% image_buster /assets/img_archive/time_engagement_day.png %})

Weitere Informationen zu Analytics für Ihre E-Mails finden Sie unter [E-Mail-Reporting]({{site.baseurl}}/user_guide/channels/email/reporting/).

{% endtab %}
{% tab SMS-Performance %}

### SMS-Performance-Dashboard {#sms-performance-dashboard}

Um Ihr SMS-Performance-Dashboard zu verwenden, navigieren Sie zu **Analytics** > **SMS Performance** und wählen Sie den Datumsbereich für den Zeitraum aus, für den Sie Daten anzeigen möchten. Ihr Datumsbereich kann bis zu ein Jahr in der Vergangenheit liegen.

![Eine Beispiel-SMS-Campaign mit 335.630 Sends und einem Durchschnitt von 11.187,667 pro Tag.]({% image_buster /assets/img_archive/email_performance_dashboard_2.png %}){: style="max-width:40%;float:right;margin-left:15px;border:none;"}

#### Wie Metriken berechnet werden

{% multi_lang_include analytics/channel_performance_how_metrics_calculated.md channel="SMS" %}

| Metrik | Typ | Berechnung |
| --- | --- | ---- |
| Sends | Anzahl | Gesamtzahl der Sends über jeden Tag im Datumsbereich |
| Bestätigte Zustellrate | Rate | (Gesamtzahl der Zustellungen über jeden Tag im Datumsbereich) / (Gesamtzahl der Sends über jeden Tag im Datumsbereich) |
| Zustellfehlerrate | Rate | (Gesamtzahl der Fehler über jeden Tag im Datumsbereich) / (Gesamtzahl der Sends über jeden Tag im Datumsbereich) |
| Ablehnungsrate | Rate | (Gesamtzahl der Ablehnungen über jeden Tag im Datumsbereich) / (Gesamtzahl der Sends über jeden Tag im Datumsbereich) |
| Klickrate | Rate | (Gesamtzahl der Klicks über jeden Tag im Datumsbereich) / (Gesamtzahl der Zustellungen über jeden Tag im Datumsbereich) |
| Gesamte Opt-ins | Rate | Gesamtzahl der eingehenden Nachrichten-Opt-ins über jeden Tag im Datumsbereich |
| Gesamte Opt-outs | Rate | Gesamtzahl der eingehenden Nachrichten-Opt-outs über jeden Tag im Datumsbereich |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="How metrics are calculated" }

{% endtab %}
{% tab Push-Performance %}

### Push-Performance-Dashboard {#push-performance-dashboard}

Das **Push Performance**-Dashboard bietet Ihnen eine kanalübergreifende Ansicht des Push-Engagements, einschließlich Sends, Bounces, Zustellungen sowie direkter, beeinflusster und gesamter Öffnungsraten über ein konfigurierbares Zeitfenster. Nutzen Sie es, um den allgemeinen Zustand Ihres Push-Kanals zu verstehen, ohne Daten aus einzelnen Campaigns oder Canvases zusammenführen zu müssen.

Um das Dashboard zu öffnen, navigieren Sie zu **Analytics** > **Dashboard Builder** und wählen Sie **Push Channel Dashboard** aus. Ihr Datumsbereich kann bis zu ein Jahr in der Vergangenheit liegen.

![Eine Beispiel-Push-Campaign mit über 63 Millionen Sends.]({% image_buster /assets/img_archive/push_performance_dashboard.png %})

#### Wie Metriken berechnet werden

{% multi_lang_include analytics/channel_performance_how_metrics_calculated.md channel="push" %}

| Metrik | Typ | Berechnung |
| --- | --- | ---- |
| Sends | Anzahl | Gesamtzahl der Sends über jeden Tag im Datumsbereich |
| Bounce-Rate | Rate | (Gesamtzahl der Bounces über jeden Tag im Datumsbereich) / (Gesamtzahl der Sends über jeden Tag im Datumsbereich) |
| Zustellrate | Rate | (Gesamtzahl der Zustellungen über jeden Tag im Datumsbereich) / (Gesamtzahl der Sends über jeden Tag im Datumsbereich) |
| Direkte Öffnungsrate | Rate | (Gesamtzahl der direkten Öffnungen über jeden Tag im Datumsbereich) / (Gesamtzahl der Zustellungen über jeden Tag im Datumsbereich) |
| Beeinflusste Öffnungsrate | Rate | (Gesamtzahl der beeinflussten Öffnungen über jeden Tag im Datumsbereich) / (Gesamtzahl der Zustellungen über jeden Tag im Datumsbereich) |
| Gesamte Öffnungsrate | Rate | (Gesamtzahl der Gesamtöffnungen über jeden Tag im Datumsbereich) / (Gesamtzahl der Zustellungen über jeden Tag im Datumsbereich)<br><br>Gesamtöffnungen umfassen sowohl direkte Öffnungen als auch beeinflusste Öffnungen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="How metrics are calculated" }

{% endtab %}
{% endtabs %}

## Dashboard-Filter {#dashboard-filters}

Sie können die Daten in Ihrem Dashboard mit den folgenden Filteroptionen filtern:

- **Tag:** Wählen Sie einen Tag aus. Nach der Anwendung zeigt Ihr Dashboard nur Metriken für den ausgewählten Tag an.
- **Plattformen:** (Nur Push-Performance-Dashboard) Wählen Sie eine Push-Plattform aus, z. B. **All Push**, **Android**, **iOS**, **Mobile combined**, **Kindle** oder **Web**. Nach der Anwendung zeigt Ihr Dashboard nur Metriken für die ausgewählte Plattform an.
- **Canvas:** Wählen Sie bis zu 10 Canvases aus. Nach der Anwendung zeigt Ihr Dashboard nur Metriken für die ausgewählten Canvases an. Wenn Sie zuerst einen Tag-Filter auswählen, umfassen Ihre Canvas-Filteroptionen nur Canvases, die den ausgewählten Tag haben.
- **Campaign:** Wählen Sie bis zu 10 Campaigns aus. Nach der Anwendung zeigt Ihr Dashboard nur Metriken für die ausgewählten Campaigns an. Wenn Sie zuerst einen Tag-Filter auswählen, umfassen Ihre Campaign-Filteroptionen nur Campaigns, die den ausgewählten Tag haben.

![Filteroptionen im Kanal-Performance-Dashboard, in dem Sie einen Tag und eine Liste von Canvases zum Filtern auswählen können.]({% image_buster /assets/img_archive/dashboard_filters.png %})

## Zeiträume vergleichen {#comparing-time-periods}

Das Kanal-Performance-Dashboard vergleicht automatisch den im Datumsbereich ausgewählten Zeitraum mit dem vorherigen Zeitraum, der die gleiche Anzahl an Tagen umfasst. Wenn Sie beispielsweise „Letzte 7 Tage“ als Datumsbereich im Dashboard auswählen, vergleicht der Vergleich zum vorherigen Zeitraum die Metriken der letzten sieben Tage mit den sieben Tagen davor. Wenn Sie einen benutzerdefinierten Datumsbereich auswählen – sagen wir vom 10. Mai bis zum 15. Mai, also sechs Tage an Daten – vergleicht das Dashboard die Metriken aus diesen Tagen mit den Metriken vom 4. Mai bis zum 9. Mai.

Der Vergleich ist die prozentuale Veränderung zwischen dem vorherigen und dem aktuellen Zeitraum, berechnet durch die Differenz der beiden Zeiträume geteilt durch die Metrik des vorherigen Zeitraums.

### Änderungen bei Gesamtzahlen und Raten anzeigen {#viewing-changes-in-total-counts-and-rates}

Sie können zwischen **Show Change in Totals** – das die Gesamtzahlen (z. B. die Anzahl der zugestellten E-Mails) zwischen den beiden Zeiträumen vergleicht – und **Show Change in Rates** – das die Raten (z. B. die Zustellrate) vergleicht – umschalten.

![Optionsfelder zum Umschalten zwischen der Anzeige von Änderungen bei Gesamtzahlen oder Änderungen bei Raten für das Kanal-Performance-Dashboard.]({% image_buster /assets/img_archive/email_performance_dashboard_3.png %}){: style="max-width:60%"}

## Häufig gestellte Fragen {#frequently-asked-questions}

### Warum zeigt mein Dashboard leere Werte an? {#why-is-my-dashboard-displaying-empty-values}

Es gibt einige Szenarien, die zu leeren Werten für eine Metrik führen können:

- Braze hat für diese bestimmte Metrik im ausgewählten Datumsbereich Nullwerte erfasst.
- Sie haben im ausgewählten Datumsbereich keine Nachrichten gesendet.
- Obwohl es Metriken wie Öffnungen, Klicks oder Abmeldungen für einen ausgewählten Datumsbereich gab, gab es keine Zustellungen oder Sends. In diesem Fall berechnet Braze keine Raten-Metrik.

Um mehr Metriken zu sehen, versuchen Sie, den Datumsbereich zu erweitern.

### Warum zeigt mein E-Mail-Dashboard mehr sonstige Öffnungen als eindeutige Öffnungen an? {#why-does-my-email-dashboard-display-more-other-opens-than-unique-opens}

Für die Metrik *Eindeutige Öffnungen* dedupliziert Braze alle wiederholten Öffnungen, die von einer bestimmten Nutzer:in registriert werden (unabhängig davon, ob sie *Maschinelle Öffnungen* oder *Sonstige Öffnungen* umfassen), sodass nur eine einzige *Eindeutige Öffnung* gezählt wird, wenn eine Nutzer:in mehrfach öffnet. Bei *Sonstigen Öffnungen* findet keine Deduplizierung statt.

<!---Temporarily hidden until functionality is added

## Empty values in your data

#### If a metric displays "0%" or "0"

This means Braze recorded zero for that particular metric during the time frame you've selected.

#### If a metric displays "N/A"

This means that while Braze recorded positive counts for a particular metric for the time frame you've selected, the denominator for the rate calculation (either sends or deliveries in most cases) was zero. This can occur when emails are sent out on one day and opens and clicks are recorded the following days if your selected time frame does not include the date the messages were sent.

#### If a metric displays "--"

This means Braze hasn't recorded any data for that metric during the time you selected. If you haven't set up or sent any emails yet, learn more about how to do so in our dedicated [Email]({{site.baseurl}}/user_guide/channels/email/) section.

--->