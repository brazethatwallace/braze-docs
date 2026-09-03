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

Rufen Sie Ihr E-Mail-Performance-Dashboard auf, indem Sie zu **Analytics** > **Email Performance** navigieren und den Datumsbereich für den gewünschten Zeitraum auswählen. Ihr Datumsbereich kann bis zu ein Jahr in der Vergangenheit liegen.

{% alert note %}
Um das **Email Performance**-Dashboard anzuzeigen, benötigen Sie die Berechtigung „View Usage Data“ oder „View Dashboard Reports“.
{% endalert %}

![E-Mail-Performance-Dashboard mit E-Mail-Kanal-Engagement der letzten dreißig Tage.]({% image_buster /assets/img_archive/email_performance_dashboard_1.png %})

![Eine beispielhafte E-Mail-Campaign mit 335.630 Sendungen und einem Durchschnitt von 11.187,667 pro Tag.]({% image_buster /assets/img_archive/email_performance_dashboard_2.png %}){: style="max-width:40%;float:right;margin-left:15px;border:none;"}

#### Wie Metriken berechnet werden {#how-metrics-are-calculated}

{% multi_lang_include analytics/channel_performance_how_metrics_calculated.md channel="email" %}

| Metrik | Typ | Berechnung |
| --- | --- | ---- |
| Sendungen | Anzahl | Gesamtzahl der Sendungen über jeden Tag im Datumsbereich |
| Zustellrate | Rate | (Gesamtzahl der Zustellungen über jeden Tag im Datumsbereich) / (Gesamtzahl der Sendungen über jeden Tag im Datumsbereich) |
| Absprungrate | Rate | (Gesamtzahl der Bounces über jeden Tag im Datumsbereich) / (Gesamtzahl der Sendungen über jeden Tag im Datumsbereich) |
| Abmelderate | Rate | (Gesamtzahl der eindeutigen Abmeldungen über jeden Tag im Datumsbereich) / (Gesamtzahl der Zustellungen für einen Datumsbereich)<br><br>Hier werden eindeutige Abmeldungen verwendet, die auch in Campaign Analytics, der Übersicht und dem Berichts-Builder genutzt werden. Diese Abmeldungen werden über alle Quellen hinweg erfasst (z. B. REST API, CSV-Importe, E-Mails und Listen-Abmeldungen). Die Abmelderaten in Campaign- und Canvas-Analytics sind Abmeldungen, die durch einen Abmelde-Klick in einer über Braze zugestellten E-Mail erfolgen. |
| Eindeutige Öffnungsrate | Rate | (Gesamtzahl der eindeutigen Öffnungen über jeden Tag im Datumsbereich) / (Gesamtzahl der Zustellungen für einen Datumsbereich) |
| Rate sonstiger Öffnungen | Rate | (Gesamtzahl der sonstigen Öffnungen über jeden Tag im Datumsbereich) / (Gesamtzahl der Zustellungen für einen Datumsbereich)<br><br>Sonstige Öffnungen umfassen E-Mails, die nicht als maschinelle Öffnungen identifiziert wurden, z. B. wenn Nutzer:innen eine E-Mail öffnen. Diese Metrik ist nicht eindeutig und ist eine Untermetrik der Gesamtöffnungen. |
| Eindeutige Klickrate | Rate | (Gesamtzahl der eindeutigen Klicks über jeden Tag im Datumsbereich) / (Gesamtzahl der Zustellungen für einen Datumsbereich) |
| Eindeutige Klick-zu-Öffnungs-Rate | Rate | (Gesamtzahl der eindeutigen Klicks über jeden Tag im Datumsbereich) / (Gesamtzahl der eindeutigen Öffnungen über jeden Tag im Datumsbereich) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Wie Metriken berechnet werden" }

{% endtab %}
{% tab E-Mail-Insights %}

### E-Mail-Insights-Dashboard {#email-insights-dashboard}

Das E-Mail-Insights-Dashboard zeigt, wo und wann Ihre Kund:innen mit Ihren E-Mails interagieren. Diese Berichte können umfangreiche und detaillierte Daten darüber liefern, wie Sie Ihre E-Mails optimieren können, um ein höheres Engagement zu erzielen. Das E-Mail-Insights-Dashboard enthält Daten der letzten sechs Monate. Um auf das Dashboard zuzugreifen, navigieren Sie zu **Analytics** > **Email Performance** > **Email Insights**.

#### Engagement nach Gerät {#engagement-by-device}

Der Bericht **Engagement by Device** bietet eine Aufschlüsselung der Geräte, die Ihre Nutzer:innen für die Interaktion mit Ihren E-Mails verwenden. Diese Daten erfassen das E-Mail-Engagement auf Mobilgeräten, Desktops, Tablets und anderen Gerätetypen. Die Daten basieren auf dem User-Agent-String, der von den Geräten Ihrer Nutzer:innen übermittelt wird.

{% alert note %}
Wenn Sie CloudFront als Ihr CDN verwenden, stellen Sie sicher, dass der User-Agent Ihrer Nutzer:innen an den ESP weitergeleitet wird. Andernfalls wird jeder User-Agent als „Amazon Cloudfront“ angezeigt.
{% endalert %}

Die Kategorie „Other“ umfasst alle User-Strings, die nicht als Desktop, Mobilgerät oder Tablet identifiziert werden können. Dazu gehören beispielsweise Fernseher, Autos, Spielekonsolen, OTT (Over-the-Top oder Streaming) und ähnliche Geräte. Dies kann auch Null- oder leere Werte umfassen.

Um besser zu verstehen, was in dieser Kategorie „Other“ enthalten ist, können Sie die User-Agents mit einer der folgenden Optionen extrahieren:

1. [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) sendet Ihnen den exakten User-Agent-String, der von den Geräten Ihrer Nutzer:innen abgerufen wurde.
2. Nutzen Sie unseren [Query Builder]({{site.baseurl}}/user_guide/analytics/reports/query_builder), um SQL zu verwenden, oder unseren [AI Query Builder]({{site.baseurl}}/user_guide/analytics/reports/query_builder#generating-sql-with-the-ai-query-builder), um die User-Agents anzuzeigen.

![Bericht „Engagement by Device“ mit der Anzahl der Klicks für Mobilgeräte, Desktops, Tablets und andere Geräte. Die meisten Klicks erfolgen auf Mobilgeräten.]({% image_buster /assets/img/engagement_by_device_type.png %}){: style="max-width:70%;"}

Bei E-Mail-Öffnungen trennt Braze Google Image Proxy, Apple Image Proxy und Yahoo Mail Proxy. Diese Dienste cachen und laden alle eingebetteten Bilder in einer E-Mail, bevor sie an die Empfänger:innen zugestellt wird. Dadurch wird eine E-Mail-Öffnung von den Servern des Postfachanbieters statt vom Server der Empfänger:innen ausgelöst, was zu überhöhten E-Mail-Öffnungen führen kann. Diese Dienste sollen Datenschutz, Sicherheit, Performance und Effizienz beim Laden von Bildern verbessern. Dies kann auch echte Öffnungen von Empfänger:innen enthalten, da diese Proxy-Dienste den User-Agent maskieren und Braze Proxy-Daten anhand des User-Agents kategorisiert.

![Bericht „Engagement by Device“ mit der Anzahl der Klicks für Mobilgeräte, Desktops, Tablets, Apple Privacy Proxy, Google Image Proxy, Yahoo Mail Proxy und Sonstige. Die meisten Öffnungen erfolgen auf Mobilgeräten.]({% image_buster /assets/img/engagement_by_device_type_proxy.png %}){: style="max-width:70%;"}

#### Engagement nach Postfachanbieter {#engagement-by-mailbox-provider}

Der Bericht **Engagement by Mailbox Provider** zeigt die wichtigsten Postfachanbieter an, die zu Ihren Klicks oder Öffnungen beitragen. Sie können auf bestimmte führende Postfachanbieter klicken, um Details zu spezifischen Empfangsdomains anzuzeigen. Wenn beispielsweise Microsoft in diesem Bericht als einer Ihrer wichtigsten Postfachanbieter aufgeführt ist, können Sie weitere Details zu deren Empfangsdomains wie „outlook.com“, „hotmail.com“, „live.com“ und mehr einsehen.

![Ein beispielhafter Bericht „Engagement by Mailbox Provider“ mit Google, Apple iCloud, Yahoo, Microsoft und Mail.Ru Group sowie der entsprechenden Anzahl von Klicks.]({% image_buster /assets/img_archive/mailbox_provider_time_engagement.png %}){: style="max-width:70%;"}

#### Zeitpunkt des Engagements {#time-of-engagement}

Der Bericht **Time of Engagement** zeigt Daten darüber an, wann Nutzer:innen mit Ihren E-Mails interagieren. Dies kann helfen, Fragen zu beantworten wie: An welchem Wochentag oder zu welcher Uhrzeit ist das Engagement Ihrer Kund:innen am höchsten? Mit diesen Insights können Sie experimentieren, an welchem Tag oder zu welcher Uhrzeit Sie Ihre Nachrichten senden sollten, um ein höheres Engagement zu erzielen. Beachten Sie, dass diese Zeiten auf der Zeitzone Ihres Unternehmens basieren.

Der Engagement-Bericht **Day of the week** schlüsselt Öffnungen oder Klicks nach Wochentag auf.

![Ein beispielhafter Engagement-Bericht „Day of the week“ mit den meisten Klicks am Montag und Mittwoch.]({% image_buster /assets/img_archive/time_engagement.png %})

Der Engagement-Bericht **Time of the day** schlüsselt Öffnungen oder Klicks nach jeder Stunde in einem 24-Stunden-Zeitfenster auf.

![Ein beispielhafter Engagement-Bericht „Time of the day“ mit Öffnungen oder Klicks von 0 Uhr bis 23 Uhr.]({% image_buster /assets/img_archive/time_engagement_day.png %})

Weitere Informationen zu Analytics für Ihre E-Mails finden Sie unter [E-Mail-Reporting]({{site.baseurl}}/user_guide/channels/email/reporting).

{% endtab %}
{% tab SMS-Performance %}

### SMS-Performance-Dashboard {#sms-performance-dashboard}

Um Ihr SMS-Performance-Dashboard zu verwenden, navigieren Sie zu **Analytics** > **SMS Performance** und wählen Sie den Datumsbereich für den gewünschten Zeitraum aus. Ihr Datumsbereich kann bis zu ein Jahr in der Vergangenheit liegen.

![Eine beispielhafte SMS-Campaign mit 335.630 Sendungen und einem Durchschnitt von 11.187,667 pro Tag.]({% image_buster /assets/img_archive/email_performance_dashboard_2.png %}){: style="max-width:40%;float:right;margin-left:15px;border:none;"}

#### Wie Metriken berechnet werden

{% multi_lang_include analytics/channel_performance_how_metrics_calculated.md channel="SMS" %}

| Metrik | Typ | Berechnung |
| --- | --- | ---- |
| Sendungen | Anzahl | Gesamtzahl der Sendungen über jeden Tag im Datumsbereich |
| Rate bestätigter Zustellungen | Rate | (Gesamtzahl der Zustellungen über jeden Tag im Datumsbereich) / (Gesamtzahl der Sendungen über jeden Tag im Datumsbereich) |
| Rate fehlgeschlagener Zustellungen | Rate | (Gesamtzahl der Fehler über jeden Tag im Datumsbereich) / (Gesamtzahl der Sendungen über jeden Tag im Datumsbereich) |
| Ablehnungsrate | Rate | (Gesamtzahl der Ablehnungen über jeden Tag im Datumsbereich) / (Gesamtzahl der Sendungen über jeden Tag im Datumsbereich) |
| Klickrate | Rate | (Gesamtzahl der Klicks über jeden Tag im Datumsbereich) / (Gesamtzahl der Zustellungen über jeden Tag im Datumsbereich) |
| Gesamte Opt-ins | Rate | Gesamtzahl der eingehenden Nachrichten-Opt-ins über jeden Tag im Datumsbereich |
| Gesamte Opt-outs | Rate | Gesamtzahl der eingehenden Nachrichten-Opt-outs über jeden Tag im Datumsbereich |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Wie Metriken berechnet werden" }

{% endtab %}
{% tab Push-Performance %}

### Push-Performance-Dashboard {#push-performance-dashboard}

Das **Push Performance**-Dashboard bietet Ihnen eine kanalübergreifende Ansicht des Push-Engagements, einschließlich Sendungen, Bounces, Zustellungen sowie direkter, beeinflusster und gesamter Öffnungsraten über ein konfigurierbares Zeitfenster. Verwenden Sie es, um den allgemeinen Zustand Ihres Push-Kanals zu verstehen, ohne Daten aus einzelnen Campaigns oder Canvases zusammenfassen zu müssen.

Um das Dashboard zu öffnen, navigieren Sie zu **Analytics** > **Dashboard Builder** und wählen Sie **Push Channel Dashboard** aus. Ihr Datumsbereich kann bis zu ein Jahr in der Vergangenheit liegen.

![Eine beispielhafte Push-Campaign mit über 63 Millionen Sendungen.]({% image_buster /assets/img_archive/push_performance_dashboard.png %})

#### Wie Metriken berechnet werden

{% multi_lang_include analytics/channel_performance_how_metrics_calculated.md channel="push" %}

| Metrik | Typ | Berechnung |
| --- | --- | ---- |
| Sendungen | Anzahl | Gesamtzahl der Sendungen über jeden Tag im Datumsbereich |
| Absprungrate | Rate | (Gesamtzahl der Bounces über jeden Tag im Datumsbereich) / (Gesamtzahl der Sendungen über jeden Tag im Datumsbereich) |
| Zustellrate | Rate | (Gesamtzahl der Zustellungen über jeden Tag im Datumsbereich) / (Gesamtzahl der Sendungen über jeden Tag im Datumsbereich) |
| Direkte Öffnungsrate | Rate | (Gesamtzahl der direkten Öffnungen über jeden Tag im Datumsbereich) / (Gesamtzahl der Zustellungen über jeden Tag im Datumsbereich) |
| Beeinflusste Öffnungsrate | Rate | (Gesamtzahl der beeinflussten Öffnungen über jeden Tag im Datumsbereich) / (Gesamtzahl der Zustellungen über jeden Tag im Datumsbereich) |
| Gesamte Öffnungsrate | Rate | (Gesamtzahl der Gesamtöffnungen über jeden Tag im Datumsbereich) / (Gesamtzahl der Zustellungen über jeden Tag im Datumsbereich)<br><br>Gesamtöffnungen umfassen sowohl direkte als auch beeinflusste Öffnungen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Wie Metriken berechnet werden" }

{% endtab %}
{% endtabs %}

## Dashboard-Filter {#dashboard-filters}

Sie können die Daten in Ihrem Dashboard mithilfe der folgenden Filteroptionen filtern:

- **Tag:** Wählen Sie ein Tag aus. Nach der Anwendung zeigt Ihr Dashboard nur Metriken für das ausgewählte Tag an.
- **Plattformen:** (nur Push-Performance-Dashboard) Wählen Sie eine Push-Plattform aus, z. B. **All Push**, **Android**, **iOS**, **Mobile combined**, **Kindle** oder **Web**. Nach der Anwendung zeigt Ihr Dashboard nur Metriken für die ausgewählte Plattform an.
- **Canvas:** Wählen Sie bis zu 10 Canvases aus. Nach der Anwendung zeigt Ihr Dashboard nur Metriken für die ausgewählten Canvases an. Wenn Sie zuerst einen Tag-Filter auswählen, umfassen die Optionen für Canvas-Filter nur Canvases, die das ausgewählte Tag enthalten.
- **Campaign:** Wählen Sie bis zu 10 Campaigns aus. Nach der Anwendung zeigt Ihr Dashboard nur Metriken für die ausgewählten Campaigns an. Wenn Sie zuerst einen Tag-Filter auswählen, umfassen die Optionen für Campaign-Filter nur Campaigns, die das ausgewählte Tag enthalten.

![Filteroptionen im Channel-Performance-Dashboard, in dem Sie ein Tag und eine Liste von Canvases zum Filtern auswählen können.]({% image_buster /assets/img_archive/dashboard_filters.png %})

## Zeiträume vergleichen {#comparing-time-periods}

Das Channel-Performance-Dashboard vergleicht automatisch den im Datumsbereich ausgewählten Zeitraum mit dem vorherigen Zeitraum, wobei die gleiche Anzahl an Tagen zugrunde gelegt wird. Wenn Sie beispielsweise „Letzte 7 Tage“ als Datumsbereich im Dashboard auswählen, werden die Metriken der letzten sieben Tage mit denen der sieben Tage davor verglichen. Wenn Sie einen benutzerdefinierten Datumsbereich auswählen – sagen wir vom 10. Mai bis zum 15. Mai, also sechs Tage an Daten –, vergleicht das Dashboard die Metriken aus diesem Zeitraum mit den Metriken vom 4. Mai bis zum 9. Mai.

Der Vergleich zeigt die prozentuale Veränderung zwischen dem vorherigen und dem aktuellen Zeitraum, berechnet als Differenz der beiden Zeiträume geteilt durch die Metrik des vorherigen Zeitraums.

### Änderungen bei Gesamtzahlen und Raten anzeigen {#viewing-changes-in-total-counts-and-rates}

Sie können zwischen **Show Change in Totals** – zum Vergleich der Gesamtzahlen (z. B. der Anzahl zugestellter E-Mails) zwischen den beiden Zeiträumen – und **Show Change in Rates** – zum Vergleich der Raten (z. B. der Zustellrate) – umschalten.

![Optionsfelder zum Umschalten zwischen der Anzeige von Änderungen bei Gesamtzahlen oder Änderungen bei Raten im Channel-Performance-Dashboard.]({% image_buster /assets/img_archive/email_performance_dashboard_3.png %}){: style="max-width:60%"}

## Häufig gestellte Fragen {#frequently-asked-questions}

### Warum zeigt mein Dashboard leere Werte an? {#why-is-my-dashboard-displaying-empty-values}

Es gibt einige Szenarien, die zu leeren Werten für eine Metrik führen können:

- Braze hat für die betreffende Metrik im ausgewählten Zeitraum Nullwerte erfasst.
- Sie haben im ausgewählten Zeitraum keine Nachrichten gesendet.
- Obwohl es im ausgewählten Zeitraum Metriken wie Öffnungen, Klicks oder Abmeldungen gab, wurden keine Zustellungen oder Sendungen verzeichnet. In diesem Fall berechnet Braze keine Ratenmetrik.

Um mehr Metriken zu sehen, versuchen Sie, den Zeitraum zu erweitern.

### Warum zeigt mein E-Mail-Dashboard mehr „Other Opens“ als „Unique Opens“ an? {#why-does-my-email-dashboard-display-more-other-opens-than-unique-opens}

Für die Metrik _Unique Opens_ dedupliziert Braze alle wiederholten Öffnungen, die von einer bestimmten Nutzer:in registriert werden (unabhängig davon, ob es sich um _Machine Opens_ oder _Other Opens_ handelt), sodass nur eine einzige _Unique Open_ gezählt wird, wenn eine Nutzer:in mehrfach öffnet. Bei _Other Opens_ führt Braze keine Deduplizierung durch.

<!---Temporarily hidden until functionality is added

## Leere Werte in Ihren Daten {#empty-values-in-your-data}

### Wenn eine Metrik „0 %“ oder „0“ anzeigt {#if-a-metric-displays-0-or-0}

Das bedeutet, dass Braze für diese bestimmte Metrik im ausgewählten Zeitraum den Wert null erfasst hat.

#### Wenn eine Metrik „N/A“ anzeigt {#if-a-metric-displays-na}

Das bedeutet, dass Braze zwar positive Werte für eine bestimmte Metrik im ausgewählten Zeitraum erfasst hat, der Nenner für die Ratenberechnung (in den meisten Fällen Sendungen oder Zustellungen) jedoch null war. Dies kann vorkommen, wenn E-Mails an einem Tag versendet werden und Öffnungen sowie Klicks an den folgenden Tagen erfasst werden, Ihr ausgewählter Zeitraum jedoch nicht das Datum umfasst, an dem die Nachrichten gesendet wurden.

#### Wenn eine Metrik „--“ anzeigt {#if-a-metric-displays}

Das bedeutet, dass Braze im ausgewählten Zeitraum keine Daten für diese Metrik erfasst hat. Wenn Sie noch keine E-Mails eingerichtet oder versendet haben, erfahren Sie mehr darüber in unserem Abschnitt [E-Mail]({{site.baseurl}}/user_guide/channels/email).

--->