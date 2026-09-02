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

Wählen Sie einen Tab aus, um Details zu den verfügbaren Performance-Dashboards für die einzelnen Kanäle anzuzeigen.

{% tabs %}
{% tab E-Mail-Performance %}

### E-Mail-Performance-Dashboard {#email-performance-dashboard}

Rufen Sie Ihr E-Mail-Performance-Dashboard auf, indem Sie zu **Analytics** > **Email Performance** navigieren und den Datumsbereich für den Zeitraum auswählen, den Sie anzeigen möchten. Ihr Datumsbereich kann bis zu ein Jahr in der Vergangenheit liegen.

{% alert note %}
Um das **Email Performance**-Dashboard anzuzeigen, benötigen Sie die Berechtigung „View Usage Data“ oder „View Dashboard Reports“.
{% endalert %}

![E-Mail-Performance-Dashboard mit E-Mail-Kanal-Engagement der letzten dreißig Tage.]({% image_buster /assets/img_archive/email_performance_dashboard_1.png %})

![Eine Beispiel-E-Mail-Campaign mit 335.630 Sends und einem Durchschnitt von 11.187,667 pro Tag.]({% image_buster /assets/img_archive/email_performance_dashboard_2.png %}){: style="max-width:40%;float:right;margin-left:15px;border:none;"}

#### Berechnung der Metriken {#how-metrics-are-calculated}

{% multi_lang_include analytics/channel_performance_how_metrics_calculated.md channel="email" %}

| Metrik | Typ | Berechnung |
| --- | --- | ---- |
| Sends | Anzahl | Gesamtanzahl der Sends über jeden Tag im Datumsbereich |
| Zustellrate | Rate | (Gesamtanzahl der Zustellungen über jeden Tag im Datumsbereich) / (Gesamtanzahl der Sends über jeden Tag im Datumsbereich) |
| Absprungrate | Rate | (Gesamtanzahl der Bounces über jeden Tag im Datumsbereich) / (Gesamtanzahl der Sends über jeden Tag im Datumsbereich) |
| Abmelderate | Rate | (Gesamtanzahl der eindeutigen Abmeldungen über jeden Tag im Datumsbereich) / (Gesamtanzahl der Zustellungen für einen Datumsbereich)<br><br>Hier werden eindeutige Abmeldungen verwendet, die auch in Campaign Analytics, der Übersicht und dem Berichts-Builder genutzt werden. Diese Abmeldungen werden über alle Quellen hinweg erfasst (z. B. REST API, CSV-Importe, E-Mails und List-Unsubscribes). Die Abmelderaten in Campaign- und Canvas-Analytics sind Abmeldungen, die durch einen Abmelde-Klick in einer über Braze zugestellten E-Mail erfolgen. |
| Eindeutige Öffnungsrate | Rate | (Gesamtanzahl der eindeutigen Öffnungen über jeden Tag im Datumsbereich) / (Gesamtanzahl der Zustellungen für einen Datumsbereich) |
| Rate sonstiger Öffnungen | Rate | (Gesamtanzahl der sonstigen Öffnungen über jeden Tag im Datumsbereich) / (Gesamtanzahl der Zustellungen für den Datumsbereich)<br><br>Sonstige Öffnungen umfassen E-Mails, die nicht als maschinelle Öffnungen identifiziert wurden, z. B. wenn ein:e Nutzer:in eine E-Mail öffnet. Diese Metrik ist nicht eindeutig und ist eine Teilmetrik der Gesamtöffnungen. |
| Eindeutige Klickrate | Rate | (Gesamtanzahl der eindeutigen Klicks über jeden Tag im Datumsbereich) / (Gesamtanzahl der Zustellungen für einen Datumsbereich) |
| Eindeutige Klick-zu-Öffnungs-Rate | Rate | (Gesamtanzahl der eindeutigen Klicks über jeden Tag im Datumsbereich) / (Gesamtanzahl der eindeutigen Öffnungen über jeden Tag im Datumsbereich) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Berechnung der Metriken" }

{% endtab %}
{% tab E-Mail-Insights %}

### E-Mail-Insights-Dashboard {#email-insights-dashboard}

Das E-Mail-Insights-Dashboard verfolgt, wo und wann Ihre Kund:innen mit Ihren E-Mails interagieren. Diese Berichte können umfangreiche und detaillierte Daten darüber liefern, wie Sie Ihre E-Mails optimieren können, um ein höheres Engagement zu erzielen. Das E-Mail-Insights-Dashboard enthält Daten der letzten sechs Monate. Um auf das Dashboard zuzugreifen, navigieren Sie zu **Analytics** > **Email Performance** > **Email Insights**.

#### Engagement nach Gerät {#engagement-by-device}

Der Bericht **Engagement by Device** bietet eine Aufschlüsselung der Geräte, die Ihre Nutzer:innen für die Interaktion mit Ihren E-Mails verwenden. Diese Daten verfolgen das E-Mail-Engagement über Mobilgeräte, Desktop, Tablet und andere Gerätetypen. Die Daten basieren auf dem User-Agent-String, der von den Geräten Ihrer Nutzer:innen übermittelt wird.

{% alert note %}
Wenn Sie CloudFront als CDN verwenden, stellen Sie sicher, dass der User-Agent Ihrer Nutzer:innen an den ESP weitergeleitet wird. Andernfalls wird jeder User-Agent als „Amazon Cloudfront“ angezeigt.
{% endalert %}

Die Kategorie „Other“ umfasst alle User-Strings, die nicht als Desktop, Mobilgerät oder Tablet identifiziert werden können. Beispiele sind Fernseher, Autos, Spielekonsolen, OTT (Over-the-Top- oder Streaming-Geräte) und Ähnliches. Dies kann auch Null- oder leere Werte beinhalten.

Um besser zu verstehen, was in dieser Kategorie „Other“ enthalten ist, können Sie die User-Agents über eine der folgenden Optionen extrahieren:

1. [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) sendet Ihnen den genauen User-Agent-String, der von den Geräten Ihrer Nutzer:innen abgerufen wurde.
2. Nutzen Sie unseren [Query Builder]({{site.baseurl}}/user_guide/analytics/reports/query_builder), um SQL oder unseren [AI Query Builder]({{site.baseurl}}/user_guide/analytics/reports/query_builder#generating-sql-with-the-ai-query-builder) zur Anzeige der User-Agents zu verwenden.

![Bericht „Engagement by Device“ mit der Anzahl der Klicks für Mobilgeräte, Desktop, Tablet und andere Geräte. Die meisten Klicks erfolgen auf Mobilgeräten.]({% image_buster /assets/img/engagement_by_device_type.png %}){: style="max-width:70%;"}

Bei E-Mail-Öffnungen separiert Braze Google Image Proxy, Apple Image Proxy und Yahoo Mail Proxy. Diese Dienste laden alle eingebetteten Bilder in einer E-Mail zwischen und laden sie vorab, bevor sie an die Empfänger:innen zugestellt wird. Dadurch wird eine E-Mail-Öffnung auf den Servern des Mailbox-Anbieters statt auf dem Server der Empfänger:innen ausgelöst, was zu überhöhten E-Mail-Öffnungen führen kann. Diese Dienste dienen dem Schutz der Privatsphäre, der Sicherheit, der Performance und der Effizienz beim Laden von Bildern. Dies kann auch echte Öffnungen von Empfänger:innen enthalten, da diese Proxy-Dienste den User-Agent maskieren und Braze Proxy-Daten anhand des User-Agents kategorisiert.

![Bericht „Engagement by Device“ mit der Anzahl der Klicks für Mobilgeräte, Desktop, Tablet, Apple Privacy Proxy, Google Image Proxy, Yahoo Mail Proxy und Sonstige. Die meisten Öffnungen erfolgen auf Mobilgeräten.]({% image_buster /assets/img/engagement_by_device_type_proxy.png %}){: style="max-width:70%;"}

#### Engagement nach Mailbox-Anbieter {#engagement-by-mailbox-provider}

Der Bericht **Engagement by Mailbox Provider** zeigt die wichtigsten Mailbox-Anbieter an, die zu Ihren Klicks oder Öffnungen beitragen. Sie können auf bestimmte führende Mailbox-Anbieter klicken, um die Details zu den jeweiligen Empfangs-Domains anzuzeigen. Wenn beispielsweise Microsoft in diesem Bericht als einer Ihrer wichtigsten Mailbox-Anbieter aufgeführt ist, können Sie weitere Details zu deren Empfangs-Domains anzeigen, wie z. B. „outlook.com“, „hotmail.com“, „live.com“ und weitere.

![Ein Beispielbericht „Engagement by Mailbox Provider“ mit Google, Apple iCloud, Yahoo, Microsoft und Mail.Ru Group und den entsprechenden Klickzahlen.]({% image_buster /assets/img_archive/mailbox_provider_time_engagement.png %}){: style="max-width:70%;"}

#### Zeitpunkt des Engagements {#time-of-engagement}

Der Bericht **Time of Engagement** zeigt Daten darüber an, wann Nutzer:innen mit Ihren E-Mails interagieren. Dies kann helfen, Fragen zu beantworten wie: An welchem Wochentag oder zu welcher Uhrzeit ist das Engagement Ihrer Kund:innen am höchsten? Mit diesen Insights können Sie experimentieren, welcher Tag oder welche Uhrzeit am besten für den Versand Ihrer Nachrichten geeignet ist, um ein höheres Engagement zu erzielen. Beachten Sie, dass diese Zeiten auf der Zeitzone Ihres Unternehmens basieren.

Der Engagement-Bericht **Day of the week** schlüsselt Öffnungen oder Klicks nach Wochentag auf.

![Ein Beispielbericht „Day of the week“ mit den meisten Klicks am Montag und Mittwoch.]({% image_buster /assets/img_archive/time_engagement.png %})

Der Engagement-Bericht **Time of the day** schlüsselt Öffnungen oder Klicks nach jeder Stunde in einem 24-Stunden-Zeitfenster auf.

![Ein Beispielbericht „Time of the day“ mit Öffnungen oder Klicks von 0 bis 23 Uhr.]({% image_buster /assets/img_archive/time_engagement_day.png %})

Weitere Informationen zu Analytics für Ihre E-Mails finden Sie unter [E-Mail-Reporting]({{site.baseurl}}/user_guide/channels/email/reporting).

{% endtab %}
{% tab SMS-Performance %}

### SMS-Performance-Dashboard {#sms-performance-dashboard}

Um Ihr SMS-Performance-Dashboard zu verwenden, navigieren Sie zu **Analytics** > **SMS Performance** und wählen Sie den Datumsbereich für den Zeitraum aus, den Sie anzeigen möchten. Ihr Datumsbereich kann bis zu ein Jahr in der Vergangenheit liegen.

![Eine Beispiel-SMS-Campaign mit 335.630 Sends und einem Durchschnitt von 11.187,667 pro Tag.]({% image_buster /assets/img_archive/email_performance_dashboard_2.png %}){: style="max-width:40%;float:right;margin-left:15px;border:none;"}

#### Berechnung der Metriken

{% multi_lang_include analytics/channel_performance_how_metrics_calculated.md channel="SMS" %}

| Metrik | Typ | Berechnung |
| --- | --- | ---- |
| Sends | Anzahl | Gesamtanzahl der Sends über jeden Tag im Datumsbereich |
| Rate bestätigter Zustellungen | Rate | (Gesamtanzahl der Zustellungen über jeden Tag im Datumsbereich) / (Gesamtanzahl der Sends über jeden Tag im Datumsbereich) |
| Rate fehlgeschlagener Zustellungen | Rate | (Gesamtanzahl der Fehlschläge über jeden Tag im Datumsbereich) / (Gesamtanzahl der Sends über jeden Tag im Datumsbereich) |
| Rate der Ablehnungen | Rate | (Gesamtanzahl der Ablehnungen über jeden Tag im Datumsbereich) / (Gesamtanzahl der Sends über jeden Tag im Datumsbereich) |
| Klickrate | Rate | (Gesamtanzahl der Klicks über jeden Tag im Datumsbereich) / (Gesamtanzahl der Zustellungen über jeden Tag im Datumsbereich) |
| Gesamt-Opt-ins | Rate | Gesamtanzahl der eingehenden Nachrichten-Opt-ins über jeden Tag im Datumsbereich |
| Gesamt-Opt-outs | Rate | Gesamtanzahl der eingehenden Nachrichten-Opt-outs über jeden Tag im Datumsbereich |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Berechnung der Metriken" }

{% endtab %}
{% tab Push-Performance %}

### Push-Performance-Dashboard {#push-performance-dashboard}

Das **Push Performance**-Dashboard bietet Ihnen eine kanalweite Ansicht des Push-Engagements über alle Ihre Campaigns und Canvases hinweg, sodass Sie den Zustand des Kanals verstehen können, ohne Daten einzelner Nachrichten zusammenfassen zu müssen.

Um das Dashboard zu öffnen, navigieren Sie zu **Analytics** > **Push Performance** und wählen Sie den Datumsbereich für den Zeitraum aus, den Sie anzeigen möchten. Ihr Datumsbereich kann bis zu ein Jahr in der Vergangenheit liegen.

![Push-Performance-Dashboard mit Push-Kanal-Engagement der letzten dreißig Tage.]({% image_buster /assets/img_archive/push_performance_dashboard_performance_tab.png %})

#### Übersicht {#overview}

Das Übersichts-Banner fasst vier zentrale Metriken für Ihren ausgewählten Datumsbereich zusammen: *Sends*, *Zustellrate*, *Öffnungsrate* und *Konversionsrate*. Jede Kachel zeigt einen Primärwert, eine unterstützende Anzahl und einen Tooltip mit zusätzlichen statistischen Details.

Die Konversionsrate in diesem Dashboard bezieht sich ausschließlich auf Ihr primäres Konversions-Event. Um sekundäre Konversions-Events zu analysieren, verwenden Sie den [Berichts-Builder]({{site.baseurl}}/user_guide/analytics/reports/report_builder).

#### Engagement im Zeitverlauf {#engagement-over-time}

Im Abschnitt „Engagement im Zeitverlauf“ wird jede Metrik als Liniendiagramm über Ihren ausgewählten Datumsbereich dargestellt:

- Sends
- Gesamtöffnungen
- Direkte Öffnungen
- Beeinflusste Öffnungen
- Direkte Öffnungsrate
- Konversionsrate
- Bounces

Sie können einen Branchen-Benchmark in das Diagramm der direkten Öffnungsrate einblenden. Benchmarks sind standardmäßig deaktiviert. Weitere Informationen finden Sie unter [Benchmarking](#benchmarking).

#### Berechnung der Metriken

{% multi_lang_include analytics/channel_performance_how_metrics_calculated.md channel="push" %}

| Metrik | Typ | Berechnung |
| --- | --- | ---- |
| Sends | Anzahl | Gesamtanzahl der Sends über jeden Tag im Datumsbereich |
| Zustellrate | Rate | (Gesamtanzahl der Zustellungen über jeden Tag im Datumsbereich) / (Gesamtanzahl der Sends über jeden Tag im Datumsbereich) |
| Absprungrate | Rate | (Gesamtanzahl der Bounces über jeden Tag im Datumsbereich) / (Gesamtanzahl der Sends über jeden Tag im Datumsbereich) |
| Direkte Öffnungsrate | Rate | (Gesamtanzahl der direkten Öffnungen über jeden Tag im Datumsbereich) / (Gesamtanzahl der Zustellungen über jeden Tag im Datumsbereich) |
| Beeinflusste Öffnungsrate | Rate | (Gesamtanzahl der beeinflussten Öffnungen über jeden Tag im Datumsbereich) / (Gesamtanzahl der Zustellungen über jeden Tag im Datumsbereich) |
| Gesamtöffnungsrate | Rate | (Gesamtanzahl der Gesamtöffnungen über jeden Tag im Datumsbereich) / (Gesamtanzahl der Zustellungen über jeden Tag im Datumsbereich)<br><br>Die Gesamtöffnungen umfassen sowohl direkte als auch beeinflusste Öffnungen. |
| Konversionsrate | Rate | (Gesamtanzahl der primären Konversionen über jeden Tag im Datumsbereich) / (Gesamtanzahl der Empfänger:innen über jeden Tag im Datumsbereich) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Berechnung der Metriken" }

{% endtab %}
{% tab Push-Insights %}

### Push-Insights-Dashboard {#push-insights-dashboard}

Das Push-Insights-Dashboard zeigt Muster auf, wie Ihre Zielgruppe auf Push-Benachrichtigungen reagiert, sodass Sie anpassen können, was und wie oft Sie senden. Um darauf zuzugreifen, navigieren Sie zu **Analytics** > **Push Performance** > **Insights**.

#### Frequenz {#frequency}

Der Frequenzbericht zeigt den Zusammenhang zwischen der Anzahl der Push-Benachrichtigungen, die ein:e Nutzer:in erhält, und der Öffnungsrate, sodass Sie den Punkt finden können, ab dem zusätzliche Sends kein Engagement mehr erzeugen. Das Diagramm hebt ein empfohlenes Sendevolumen basierend auf Benchmark-Daten für Ihre Branche hervor.

{% alert important %}
Die Frequenz- und Kadenzberichte verwenden ein Analysefenster von mindestens drei Monaten. Wenn Sie einen kürzeren Datumsbereich auswählen, kann Braze das Startdatum erweitern, um bis zu drei Monate an Daten einzubeziehen, sofern verfügbar. Diese Berichte werden nicht von Tag-, Campaign-, Canvas- oder Plattformfiltern beeinflusst – sie spiegeln immer Ihr gesamtes Push-Volumen für den ausgewählten Datumsbereich wider.
{% endalert %}

#### Kadenz {#cadence}

Während der Frequenzbericht Ihnen sagt, wie viele Nachrichten Sie senden sollten, zeigt der Kadenzbericht, wie Sie diese zeitlich verteilen sollten. Er stellt die Öffnungsrate in Bezug zur Sendekadenz dar, sodass Sie sehen können, ob das Bündeln Ihrer Sends – beispielsweise drei Push-Benachrichtigungen am Wochenende – Engagement kostet, im Vergleich zu einer Verteilung über die Woche.

Verwenden Sie ihn zusammen mit dem Frequenzbericht: Die Frequenz legt Ihr Volumenziel fest, die Kadenz die Verteilung.

#### Performance-Verteilung der Campaigns {#campaign-performance-distribution}

Dieser Bericht stellt jede Push-Campaign in Ihrem Datumsbereich nach Öffnungsrate und Konversionsrate dar, sodass Sie Ihre stärksten und schwächsten Performer nebeneinander sehen und nach Gemeinsamkeiten suchen können.

Klicken Sie im Diagramm der Campaign-Performance-Verteilung auf das Drei-Punkte-Symbol und wählen Sie **Datentabelle anzeigen**, um eine sortierbare Tabelle mit denselben Campaigns anzuzeigen. Sie können nach Öffnungsrate oder Konversionsrate sortieren, um die Performer zu ranken, und darüber die Analytics einer einzelnen Campaign öffnen.

{% endtab %}
{% tab Push-Zustellbarkeit %}

### Push-Zustellbarkeits-Dashboard {#push-deliverability-dashboard}

Das Push-Zustellbarkeits-Dashboard verfolgt den Zustand Ihrer Push-Zielgruppe im Zeitverlauf, sodass Sie sehen können, wie sich Ihr Messaging auf Ihre erreichbare Basis auswirkt. Um darauf zuzugreifen, navigieren Sie zu **Analytics** > **Push Performance** > **Deliverability**.

Dieses Dashboard wird nur nach Datumsbereich gefiltert, und jede Metrik wird nach Plattform aufgeschlüsselt.

#### Absprungrate {#bounce-rate}

Bounces über Ihren ausgewählten Datumsbereich, aufgeschlüsselt nach Plattform. Sie können einen Branchen-Benchmark in dieses Diagramm einblenden. Dieser ist standardmäßig deaktiviert.

#### Deinstallationsrate {#uninstall-rate}

Deinstallationen über Ihren ausgewählten Datumsbereich, aufgeschlüsselt nach Plattform. Verwenden Sie dies, um zu sehen, ob ein intensiver Sendezeitraum damit zusammenfiel, dass Nutzer:innen abgewandert sind. Die Deinstallationsdaten hängen von Ihrer Uninstall-Tracking-Konfiguration ab. Siehe [Uninstall-Tracking]({{site.baseurl}}/user_guide/analytics/tracking/uninstall_tracking). Uninstall-Tracking wird für iOS, Android (außer Huawei) und Kindle unterstützt. Wenn das Uninstall-Tracking deaktiviert ist, sind die Deinstallationsraten-Daten weniger vollständig und möglicherweise weniger genau. Je nach Betriebssystem können Deinstallationsberichte später oder in Batches eintreffen, sodass das Diagramm möglicherweise nicht das genaue Deinstallationsdatum widerspiegelt.

#### Berechnung der Metriken

| Metrik | Typ | Berechnung |
| --- | --- | ---- |
| Deinstallationsrate | Rate | (Gesamtanzahl der Geräte, bei denen Braze ein Deinstallationssignal erhalten hat, über jeden Tag im Datumsbereich) / (Gesamtanzahl der Geräte mit gültigen Token über jeden Tag im Datumsbereich) |
| Absprungrate | Rate | (Gesamtanzahl der Bounces über jeden Tag im Datumsbereich) / (Gesamtanzahl der Sends über jeden Tag im Datumsbereich) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Berechnung der Metriken" }

{% endtab %}
{% endtabs %}

## Dashboard-Filter {#dashboard-filters}

Sie können die Daten in Ihrem Dashboard mithilfe der folgenden Filteroptionen filtern:

- **Tag:** Wählen Sie ein Tag aus. Nach Anwendung zeigt Ihr Dashboard nur Metriken für Ihr ausgewähltes Tag an. Beachten Sie, dass das Push-Dashboard mehrere Tags unterstützt.
- **Plattformen:** (Nur Push-Dashboards) Wählen Sie eine Push-Plattform aus, z. B. **All Push**, **Android**, **iOS**, **Mobile combined**, **Kindle** oder **Web**. Nach Anwendung zeigt Ihr Dashboard nur Metriken für die ausgewählte Plattform an.
- **Canvas:** Wählen Sie bis zu 10 Canvases aus. Nach Anwendung zeigt Ihr Dashboard nur Metriken für Ihre ausgewählten Canvases an. Wenn Sie zuerst einen Tag-Filter auswählen, enthalten Ihre Canvas-Filteroptionen nur Canvases mit dem ausgewählten Tag.
- **Campaign:** Wählen Sie bis zu 10 Campaigns aus. Nach Anwendung zeigt Ihr Dashboard nur Metriken für Ihre ausgewählten Campaigns an. Wenn Sie zuerst einen Tag-Filter auswählen, enthalten Ihre Campaign-Filteroptionen nur Campaigns mit dem ausgewählten Tag.

{% alert note %}
Filter werden in den verschiedenen Push-Dashboards unterschiedlich angewendet. Das Push-Performance-Dashboard unterstützt alle Filter. Das Push-Zustellbarkeits-Dashboard unterstützt nur den Datumsbereich, wobei eine Plattform-Aufschlüsselung in jedem Chart angezeigt wird. Die Frequenz- und Kadenzberichte im Push-Insights-Dashboard unterstützen nur den Datumsbereich.
{% endalert %}

![Filteroptionen im Channel-Performance-Dashboard, in dem Sie ein Tag und eine Liste von Canvases zum Filtern auswählen können.]({% image_buster /assets/img_archive/dashboard_filters.png %})

## Zeiträume vergleichen {#comparing-time-periods}

Das Channel-Performance-Dashboard vergleicht automatisch den ausgewählten Zeitraum im Datumsbereich mit dem vorherigen Zeitraum, wobei die gleiche Anzahl an Tagen zugrunde gelegt wird. Wenn Sie beispielsweise „Letzte 7 Tage“ als Datumsbereich im Dashboard auswählen, werden die Metriken der letzten sieben Tage mit den sieben Tagen davor verglichen. Wenn Sie einen benutzerdefinierten Datumsbereich auswählen – sagen wir vom 10. Mai bis zum 15. Mai, also sechs Tage an Daten –, vergleicht das Dashboard die Metriken aus diesem Zeitraum mit den Metriken vom 4. Mai bis 9. Mai.

Der Vergleich ist die prozentuale Veränderung zwischen dem vorherigen und dem aktuellen Zeitraum. Sie wird berechnet, indem die Differenz zwischen den beiden Zeiträumen durch die Metrik des vorherigen Zeitraums geteilt wird.

### Änderungen bei Gesamtzahlen und Raten anzeigen {#viewing-changes-in-total-counts-and-rates}

Sie können zwischen **Show Change in Totals** – das die Gesamtzahlen (z. B. die Anzahl der zugestellten E-Mails) zwischen den beiden Zeiträumen vergleicht – und **Show Change in Rates** – das die Raten (z. B. die Zustellrate) vergleicht – umschalten.

![Optionsschaltflächen zum Wechseln zwischen der Anzeige von Änderungen bei Gesamtzahlen oder Änderungen bei Raten im Channel-Performance-Dashboard.]({% image_buster /assets/img_archive/email_performance_dashboard_3.png %}){: style="max-width:60%"}

## Benchmarking {#benchmarking}

Auf den Push-Dashboards können Sie Ihre Performance mit aggregierten, anonymisierten Daten von Braze vergleichen.

### Verfügbare Benchmarks {#available-benchmarks}

| Benchmark | Anzeige | Standard |
| --- | --- | ---- |
| Direkte Öffnungsrate | Push-Performance | Aus |
| Absprungrate | Push-Zustellbarkeit | Aus |
| Häufigkeit | Push-Insights | An |
| Kadenz | Push-Insights | An |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Verfügbare Benchmarks" }

Benchmarks für direkte Öffnungsrate und Absprungrate werden nach Plattform aufgeschlüsselt. Alle Push-Benchmarks werden anhand der Öffnungsrate gemessen, nicht anhand der Konversionsrate.

### Branchen vergleichen {#comparing-verticals}

Benchmark-Daten sind nach Branche aufgeteilt. Ihr Dashboard zeigt standardmäßig die Branche Ihres Kontos an, und Sie können über das Dropdown-Menü eine andere zum Vergleich auswählen.

### Regionen vergleichen {#comparing-regions}

Benchmark-Daten sind nach Region aufgeteilt. Ihr Dashboard zeigt standardmäßig die Region Ihres Kontos an, und Sie können über das Dropdown-Menü eine andere zum Vergleich auswählen.

{% alert note %}
Wenn die neuesten Benchmark-Daten für den ausgewählten Zeitraum nicht verfügbar sind, zeigt Braze einen prognostizierten Benchmark an.

Benchmark-Daten werden monatlich aktualisiert.
{% endalert %}

## Häufig gestellte Fragen {#frequently-asked-questions}

### Warum zeigt mein Dashboard leere Werte an? {#why-is-my-dashboard-displaying-empty-values}

Es gibt einige Szenarien, die zu leeren Werten für eine Metrik führen können:

- Braze hat für die betreffende Metrik in Ihrem ausgewählten Datumsbereich Nullwerte erfasst.
- Sie haben im ausgewählten Datumsbereich keine Nachrichten gesendet.
- Obwohl es für einen ausgewählten Datumsbereich Metriken wie Öffnungen, Klicks oder Abmeldungen gab, wurden keine Zustellungen oder Sendungen verzeichnet. In diesem Fall berechnet Braze keine Ratenmetrik.

Um mehr Metriken zu sehen, versuchen Sie, den Datumsbereich zu erweitern.

### Warum zeigt mein E-Mail-Dashboard mehr „Other Opens“ als eindeutige Öffnungen an? {#why-does-my-email-dashboard-display-more-other-opens-than-unique-opens}

Für die Metrik _Eindeutige Öffnungen_ dedupliziert Braze alle wiederholten Öffnungen, die von einer bestimmten Nutzer:in registriert wurden (unabhängig davon, ob es sich um _Machine Opens_ oder _Other Opens_ handelt), sodass nur eine einzige _eindeutige Öffnung_ gezählt wird, wenn eine Nutzer:in mehrfach öffnet. Bei _Other Opens_ führt Braze keine Deduplizierung durch.

### Warum sind meine Frequenz- und Kadenzberichte leer? {#why-are-my-frequency-and-cadence-reports-empty}

Diese Berichte verwenden ein Analysefenster von drei Monaten. Wenn Ihr ausgewählter Bereich kürzer ist, kann Braze den Bereich erweitern, um frühere Daten einzubeziehen, sofern diese verfügbar sind.

Wenn Ihr Datumsbereich lang genug ist und die Berichte trotzdem leer sind, stehen möglicherweise noch keine Benchmark-Daten für Ihren Workspace zur Verfügung. Wenden Sie sich an den Braze-Support, wenn Sie Fragen haben.

### Warum ändern meine Filter die Frequenz- und Kadenzberichte nicht? {#why-dont-my-filters-change-the-frequency-and-cadence-reports}

Die Frequenz- und Kadenzberichte spiegeln immer Ihr gesamtes Push-Volumen wider, da ihr Wert aus der Messung der gesamten Nachrichtenlast für eine Nutzer:in resultiert. Eine Filterung auf eine Teilmenge von Campaigns würde unterschätzen, wie viele Nachrichten die Nutzer:in tatsächlich erhalten hat. Nur der Datumsbereichsfilter wird angewendet.
<!---Temporarily hidden until functionality is added

## Leere Werte in Ihren Daten {#empty-values-in-your-data}

### Wenn eine Metrik „0 %“ oder „0“ anzeigt {#if-a-metric-displays-0-or-0}

Das bedeutet, dass Braze für diese bestimmte Metrik im ausgewählten Zeitraum den Wert null erfasst hat.

#### Wenn eine Metrik „N/A“ anzeigt {#if-a-metric-displays-na}

Das bedeutet, dass Braze zwar positive Werte für eine bestimmte Metrik im ausgewählten Zeitraum erfasst hat, der Nenner für die Ratenberechnung (in den meisten Fällen Sendungen oder Zustellungen) jedoch null war. Dies kann vorkommen, wenn E-Mails an einem Tag versendet werden und Öffnungen sowie Klicks an den darauffolgenden Tagen erfasst werden, Ihr ausgewählter Zeitraum jedoch nicht das Datum umfasst, an dem die Nachrichten gesendet wurden.

#### Wenn eine Metrik „--“ anzeigt {#if-a-metric-displays}

Das bedeutet, dass Braze für diese Metrik im ausgewählten Zeitraum keine Daten erfasst hat. Wenn Sie noch keine E-Mails eingerichtet oder gesendet haben, erfahren Sie mehr darüber in unserem speziellen Abschnitt [E-Mail]({{site.baseurl}}/user_guide/channels/email).

--->