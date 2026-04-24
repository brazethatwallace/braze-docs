---
nav_title: Kanal-Performance
article_title: Kanal-Performance-Dashboards
page_order: 2
page_type: reference
description: "Dieser Referenzartikel behandelt das Kanal-Performance-Dashboard, mit dem Sie Performance-Metriken für ganze Kanäle über Kampagnen und Canvases hinweg anzeigen können."
tool: 
  - Reports
toc_headers: h2
---

# Kanal-Performance-Dashboards

> Kanal-Performance-Dashboards zeigen aggregierte Performance-Metriken für einen gesamten Kanal, sowohl aus Kampagnen als auch aus Canvases. Diese Dashboards sind derzeit für E-Mail und SMS verfügbar.

## Dashboards

Wählen Sie einen Tab aus, um Details zu den verfügbaren Kanal-Performance-Dashboards anzuzeigen.

{% tabs %}
{% tab Email performance %}

### E-Mail-Performance-Dashboard

Rufen Sie Ihr E-Mail-Performance-Dashboard auf, indem Sie zu **Analytics** > **Email Performance** navigieren und den Datumsbereich für den Zeitraum auswählen, für den Sie Daten anzeigen möchten. Ihr Datumsbereich kann bis zu ein Jahr in der Vergangenheit liegen.

![E-Mail-Performance-Dashboard, das das E-Mail-Kanal-Engagement der letzten dreißig Tage anzeigt.]({% image_buster /assets/img_archive/email_performance_dashboard_1.png %})

#### Wie Metriken berechnet werden

![Eine Beispiel-E-Mail-Kampagne mit 335.630 Sends und einem Durchschnitt von 11.187,667 pro Tag.]({% image_buster /assets/img_archive/email_performance_dashboard_2.png %}){: style="max-width:40%;float:right;margin-left:15px;border:none;"}

Die Berechnungen für die verschiedenen Metriken im E-Mail-Performance-Dashboard sind dieselben wie auf der Ebene einzelner Nachrichten (z. B. Kampagnen-Analytics). In diesem Dashboard werden die Metriken über alle Kampagnen und Canvases für den von Ihnen ausgewählten Datumsbereich aggregiert. Weitere Informationen zu diesen Definitionen finden Sie unter [E-Mail-Metriken]({{site.baseurl}}/user_guide/channels/email/reporting/analytics_glossary/#email-metrics).

Jede Kachel zeigt zuerst die Raten-Metrik, gefolgt von der Zähl-Metrik (mit Ausnahme von *Sends*, das die Zähl-Metrik gefolgt vom Tagesdurchschnitt anzeigt). Zum Beispiel enthält die Kachel für eindeutige Klicks die *Eindeutige Klickrate* aus Ihrem ausgewählten Zeitraum und die Gesamtzahl der eindeutigen Klicks aus diesem Zeitraum. Jede Kachel zeigt außerdem den [Vergleich zum vorherigen Zeitraum](#comparing-time-periods).

| Metrik | Typ | Berechnung |
| --- | --- | ---- |
| Sends | Anzahl | Gesamtzahl der Sends über jeden Tag im Datumsbereich |
| Zustellrate | Rate | (Gesamtzahl der Zustellungen über jeden Tag im Datumsbereich) / (Gesamtzahl der Sends über jeden Tag im Datumsbereich) |
| Bounce-Rate | Rate | (Gesamtzahl der Bounces über jeden Tag im Datumsbereich) / (Gesamtzahl der Sends über jeden Tag im Datumsbereich) |
| Abmeldungsrate | Rate | (Gesamtzahl der eindeutigen Abmeldungen über jeden Tag im Datumsbereich) / (Gesamtzahl der Zustellungen für einen Datumsbereich)<br><br>Hier werden eindeutige Abmeldungen verwendet, die auch in Kampagnen-Analytics, der Übersicht und dem Berichts-Builder genutzt werden. Diese Abmeldungen werden über alle Quellen hinweg erfasst (z. B. REST API, CSV-Importe, E-Mails und Listen-Abmeldungen). Die Abmeldungsraten in Kampagnen- und Canvas-Analytics sind Abmeldungen, die durch einen Klick auf den Abmeldelink in einer von Braze zugestellten E-Mail erfolgen.  |
| Eindeutige Öffnungsrate | Rate | (Gesamtzahl der eindeutigen Öffnungen über jeden Tag im Datumsbereich) / (Gesamtzahl der Zustellungen für einen Datumsbereich) |
| Sonstige Öffnungsrate | Rate | (Gesamtzahl der sonstigen Öffnungen über jeden Tag im Datumsbereich) / (Gesamtzahl der Zustellungen für den Datumsbereich)<br><br>Sonstige Öffnungen umfassen E-Mails, die nicht als maschinelle Öffnungen identifiziert wurden, z. B. wenn eine Nutzer:in eine E-Mail öffnet. Diese Metrik ist nicht eindeutig und ist eine Untermetrik der Gesamtöffnungen.  |
| Eindeutige Klickrate | Rate | (Gesamtzahl der eindeutigen Klicks über jeden Tag im Datumsbereich) / (Gesamtzahl der Zustellungen für einen Datumsbereich) |
| Eindeutige Klick-zu-Öffnungs-Rate | Rate | (Gesamtzahl der eindeutigen Klicks über jeden Tag im Datumsbereich) / (Gesamtzahl der eindeutigen Öffnungen über jeden Tag im Datumsbereich) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Email insights %}

### E-Mail-Insights-Dashboard

Das E-Mail-Insights-Dashboard verfolgt, wo und wann Ihre Kund:innen mit Ihren E-Mails interagieren. Diese Berichte können umfangreiche und detaillierte Daten darüber liefern, wie Sie Ihre E-Mails optimieren können, um ein höheres Engagement zu erzielen. Das E-Mail-Insights-Dashboard enthält Daten von bis zu den letzten sechs Monaten. Um auf das Dashboard zuzugreifen, navigieren Sie zu **Analytics** > **Email Performance** > **Email Insights**.

#### Engagement nach Gerät

Der Bericht **Engagement by Device** bietet eine Aufschlüsselung darüber, welche Geräte Ihre Nutzer:innen verwenden, um mit Ihren E-Mails zu interagieren. Diese Daten verfolgen das E-Mail-Engagement über Mobilgeräte, Desktop, Tablet und andere Gerätetypen. Die Daten basieren auf dem User-Agent-String, der von den Geräten Ihrer Nutzer:innen übermittelt wird.

{% alert note %}
Wenn Sie CloudFront als Ihr CDN verwenden, stellen Sie sicher, dass der User-Agent Ihrer Nutzer:innen an den ESP weitergeleitet wird. Andernfalls wird jeder User-Agent als „Amazon Cloudfront" angezeigt.
{% endalert %}

Die Kategorie „Other" umfasst jeden User-String, der nicht als Desktop, Mobilgerät oder Tablet identifiziert werden kann. Zum Beispiel Fernseher, Auto, Spielekonsole, OTT (Over-the-Top oder Streaming) und ähnliches. Dies kann auch Null- oder leere Werte umfassen.

Um besser zu verstehen, was in dieser Kategorie „Other" enthalten ist, können Sie die User-Agents mit einer der folgenden Optionen extrahieren:

1. [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/) sendet Ihnen den genauen User-Agent-String, der von den Geräten Ihrer Nutzer:innen abgerufen wurde.
2. Nutzen Sie unseren [Abfrage-Builder]({{site.baseurl}}/user_guide/analytics/reports/query_builder/), um SQL oder unseren [KI-Abfrage-Builder]({{site.baseurl}}/user_guide/analytics/reports/query_builder#generating-sql-with-the-ai-query-builder) zu verwenden, um die User-Agents anzuzeigen.

![Bericht „Engagement by Device", der die Anzahl der Klicks für Mobilgeräte, Desktop, Tablet und andere Geräte zeigt. Die meisten Klicks erfolgen auf Mobilgeräten.]({% image_buster /assets/img/engagement_by_device_type.png %}){: style="max-width:70%;"}

Bei E-Mail-Öffnungen trennt Braze Google Image Proxy, Apple Image Proxy und Yahoo Mail Proxy. Diese Dienste cachen und laden alle eingebetteten Bilder in einer E-Mail, bevor sie an die Empfänger:in zugestellt wird. Dadurch wird eine E-Mail-Öffnung von den Servern des Mailbox-Anbieters statt vom Server der Empfänger:in ausgelöst, was zu überhöhten E-Mail-Öffnungen führen kann. Diese Dienste sollen Datenschutz, Sicherheit, Performance und Effizienz beim Laden von Bildern verbessern. Dies kann auch echte Öffnungen von Empfänger:innen enthalten, da diese Proxy-Dienste den User-Agent maskieren und Braze Proxy-Daten anhand des User-Agents kategorisiert.

![Bericht „Engagement by Device", der die Anzahl der Klicks für Mobilgerät, Desktop, Tablet, Apple Privacy Proxy, Google Image Proxy, Yahoo Mail Proxy und Other zeigt. Die meisten Öffnungen erfolgen auf Mobilgeräten.]({% image_buster /assets/img/engagement_by_device_type_proxy.png %}){: style="max-width:70%;"}

#### Engagement nach Mailbox-Anbieter

Der Bericht **Engagement by Mailbox Provider** zeigt die wichtigsten Mailbox-Anbieter an, die zu Ihren Klicks oder Öffnungen beitragen. Sie können auf bestimmte führende Mailbox-Anbieter klicken, um Details zu spezifischen Empfangs-Domains anzuzeigen. Wenn beispielsweise Microsoft in diesem Bericht als einer Ihrer Top-Mailbox-Anbieter aufgeführt ist, können Sie weitere Details zu deren Empfangs-Domains anzeigen, wie z. B. „outlook.com", „hotmail.com", „live.com" und mehr.

![Ein Beispiel für den Bericht „Engagement by Mailbox Provider" mit Google, Apple iCloud, Yahoo, Microsoft und Mail.Ru Group und der entsprechenden Anzahl von Klicks.]({% image_buster /assets/img_archive/mailbox_provider_time_engagement.png %}){: style="max-width:70%;"}

#### Zeitpunkt des Engagements

Der Bericht **Time of Engagement** zeigt Daten darüber an, wann Nutzer:innen mit Ihren E-Mails interagieren. Dies kann helfen, Fragen zu beantworten wie: An welchem Wochentag oder zu welcher Uhrzeit ist das Engagement Ihrer Kund:innen am höchsten? Mit diesen Insights können Sie experimentieren, an welchem Tag oder zu welcher Uhrzeit Sie Ihre Nachrichten senden sollten, um ein höheres Engagement zu erzielen. Beachten Sie, dass diese Zeiten auf der Zeitzone Ihres Unternehmens basieren.

Der Engagement-Bericht **Day of the week** schlüsselt Öffnungen oder Klicks nach Wochentag auf.

![Ein Beispiel für den Engagement-Bericht „Day of the week" mit den meisten Klicks am Montag und Mittwoch.]({% image_buster /assets/img_archive/time_engagement.png %})

Der Engagement-Bericht **Time of the day** schlüsselt Öffnungen oder Klicks nach jeder Stunde in einem 24-Stunden-Zeitfenster auf.

![Ein Beispiel für den Engagement-Bericht „Time of the day" mit Öffnungen oder Klicks von 0 Uhr bis 23 Uhr.]({% image_buster /assets/img_archive/time_engagement_day.png %})

Weitere Informationen zu Analytics für Ihre E-Mails finden Sie unter [E-Mail-Reporting]({{site.baseurl}}/user_guide/channels/email/reporting/).

{% endtab %}
{% tab SMS performance %}

### SMS-Performance-Dashboard

Um Ihr SMS-Performance-Dashboard zu verwenden, navigieren Sie zu **Analytics** > **SMS Performance** und wählen Sie den Datumsbereich für den Zeitraum aus, für den Sie Daten anzeigen möchten. Ihr Datumsbereich kann bis zu ein Jahr in der Vergangenheit liegen.

#### Wie Metriken berechnet werden

![Eine Beispiel-SMS-Kampagne mit 335.630 Sends und einem Durchschnitt von 11.187,667 pro Tag.]({% image_buster /assets/img_archive/email_performance_dashboard_2.png %}){: style="max-width:40%;float:right;margin-left:15px;border:none;"}

Die Berechnungen für die verschiedenen Metriken im SMS-Performance-Dashboard sind dieselben wie auf der Ebene einzelner Nachrichten (z. B. Kampagnen-Analytics). In diesem Dashboard werden die Metriken über alle Kampagnen und Canvases für den von Ihnen ausgewählten Datumsbereich aggregiert. Weitere Informationen zu diesen Definitionen finden Sie unter [SMS-Metriken]({{site.baseurl}}/sms_mms_rcs_reporting/).

Jede Kachel zeigt zuerst die Raten-Metrik, gefolgt von der Zähl-Metrik (mit Ausnahme von _Sends_, das die Zähl-Metrik gefolgt vom Tagesdurchschnitt anzeigt). Jede Kachel zeigt außerdem den [Vergleich zum vorherigen Zeitraum](#comparison-to-last-period-change-in-totals-or-rates).

| Metrik | Typ | Berechnung |
| --- | --- | ---- |
| Sends | Anzahl | Gesamtzahl der Sends über jeden Tag im Datumsbereich |
| Bestätigte Zustellrate | Rate | (Gesamtzahl der Zustellungen über jeden Tag im Datumsbereich) / (Gesamtzahl der Sends über jeden Tag im Datumsbereich) |
| Zustellfehlerrate | Rate | (Gesamtzahl der Fehler über jeden Tag im Datumsbereich) / (Gesamtzahl der Sends über jeden Tag im Datumsbereich) |
| Ablehnungsrate | Rate | (Gesamtzahl der Ablehnungen über jeden Tag im Datumsbereich) / (Gesamtzahl der Sends über jeden Tag im Datumsbereich) |
| Klickrate | Rate | (Gesamtzahl der Klicks über jeden Tag im Datumsbereich) / (Gesamtzahl der Zustellungen über jeden Tag im Datumsbereich) |
| Gesamte Opt-ins | Rate | Gesamtzahl der eingehenden Nachrichten-Opt-ins über jeden Tag im Datumsbereich |
| Gesamte Opt-outs | Rate | Gesamtzahl der eingehenden Nachrichten-Opt-outs über jeden Tag im Datumsbereich |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% endtabs %}

## Dashboard-Filter

Sie können die Daten in Ihrem Dashboard mit den folgenden Filteroptionen filtern:

- **Tag:** Wählen Sie einen Tag aus. Nach der Anwendung zeigt Ihr Dashboard nur Metriken für den ausgewählten Tag an.
- **Canvas:** Wählen Sie bis zu 10 Canvases aus. Nach der Anwendung zeigt Ihr Dashboard nur Metriken für die ausgewählten Canvases an. Wenn Sie zuerst einen Tag-Filter auswählen, umfassen Ihre Canvas-Filteroptionen nur Canvases, die den ausgewählten Tag haben.
- **Kampagne:** Wählen Sie bis zu 10 Kampagnen aus. Nach der Anwendung zeigt Ihr Dashboard nur Metriken für die ausgewählten Kampagnen an. Wenn Sie zuerst einen Tag-Filter auswählen, umfassen Ihre Kampagnen-Filteroptionen nur Kampagnen, die den ausgewählten Tag haben.

![Filteroptionen im Kanal-Performance-Dashboard, in dem Sie einen Tag und eine Liste von Canvases zum Filtern auswählen können.]({% image_buster /assets/img_archive/dashboard_filters.png %})

## Zeiträume vergleichen

Das Kanal-Performance-Dashboard vergleicht automatisch den im Datumsbereich ausgewählten Zeitraum mit dem vorherigen Zeitraum, der die gleiche Anzahl an Tagen umfasst. Wenn Sie beispielsweise „Letzte 7 Tage" als Datumsbereich im Dashboard auswählen, vergleicht der Vergleich zum vorherigen Zeitraum die Metriken der letzten sieben Tage mit den sieben Tagen davor. Wenn Sie einen benutzerdefinierten Datumsbereich auswählen – sagen wir vom 10. Mai bis zum 15. Mai, also sechs Tage an Daten – vergleicht das Dashboard die Metriken aus diesen Tagen mit den Metriken vom 4. Mai bis zum 9. Mai.

Der Vergleich ist die prozentuale Veränderung zwischen dem vorherigen und dem aktuellen Zeitraum, berechnet durch die Differenz der beiden Zeiträume geteilt durch die Metrik des vorherigen Zeitraums.

### Änderungen bei Gesamtzahlen und Raten anzeigen

Sie können zwischen **Show Change in Totals** – das die Gesamtzahlen (z. B. die Anzahl der zugestellten E-Mails) zwischen den beiden Zeiträumen vergleicht – und **Show Change in Rates** – das die Raten (z. B. die Zustellrate) vergleicht – umschalten.

![Optionsfelder zum Umschalten zwischen der Anzeige von Änderungen bei Gesamtzahlen oder Änderungen bei Raten für das Kanal-Performance-Dashboard.]({% image_buster /assets/img_archive/email_performance_dashboard_3.png %}){: style="max-width:60%"}

## Häufig gestellte Fragen

### Warum zeigt mein Dashboard leere Werte an?

Es gibt einige Szenarien, die zu leeren Werten für eine Metrik führen können:

- Braze hat für diese bestimmte Metrik im ausgewählten Datumsbereich Nullwerte erfasst.
- Sie haben im ausgewählten Datumsbereich keine Nachrichten gesendet.
- Obwohl es Metriken wie Öffnungen, Klicks oder Abmeldungen für einen ausgewählten Datumsbereich gab, gab es keine Zustellungen oder Sends. In diesem Fall berechnet Braze keine Raten-Metrik.

Um mehr Metriken zu sehen, versuchen Sie, den Datumsbereich zu erweitern.

### Warum zeigt mein E-Mail-Dashboard mehr sonstige Öffnungen als eindeutige Öffnungen an?

Für die Metrik _Eindeutige Öffnungen_ dedupliziert Braze alle wiederholten Öffnungen, die von einer bestimmten Nutzer:in registriert werden (unabhängig davon, ob sie _Maschinelle Öffnungen_ oder _Sonstige Öffnungen_ umfassen), sodass nur eine einzige _Eindeutige Öffnung_ gezählt wird, wenn eine Nutzer:in mehrfach öffnet. Bei _Sonstigen Öffnungen_ findet keine Deduplizierung statt.

<!---Temporarily hidden until functionality is added

## Empty values in your data

#### If a metric displays "0%" or "0"

This means Braze recorded zero for that particular metric during the time frame you've selected.

#### If a metric displays "N/A"

This means that while Braze recorded positive counts for a particular metric for the time frame you've selected, the denominator for the rate calculation (either sends or deliveries in most cases) was zero. This can occur when emails are sent out on one day and opens and clicks are recorded the following days if your selected time frame does not include the date the messages were sent.

#### If a metric displays "--"

This means Braze hasn't recorded any data for that metric during the time you selected. If you haven't set up or sent any emails yet, learn more about how to do so in our dedicated [Email]({{site.baseurl}}/user_guide/channels/email/) section.

--->