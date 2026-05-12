---
nav_title: Abfrage-Templates
article_title: Abfrage-Builder-Templates
page_order: 1
page_type: reference
toc_headers: h2
description: "Dieser Referenzartikel listet die Berichtstypen auf, die Sie mit Braze-Daten aus Snowflake im Abfrage-Builder erstellen können."
tool: Reports
---

# Abfrage-Builder-Templates {#query-builder-templates}

> Greifen Sie auf [Abfrage-Builder]({{site.baseurl}}/user_guide/analytics/reports/query_builder/)-Templates zu, indem Sie beim Erstellen eines Berichts **Query Template** auswählen. Alle Templates zeigen Daten aus den letzten 60 Tagen an, aber Sie können diesen und andere Werte direkt im Editor bearbeiten.<br><br>Definitionen der Metriken, die in Ihren Abfrage-Builder-Berichten erscheinen können, finden Sie im [Glossar der Berichtsmetriken]({{site.baseurl}}/user_guide/analytics/metrics_glossary/). Filtern Sie dort nach dem jeweiligen Kanal.

## Kanal-Templates {#channel-templates}

<style>
table th:nth-child(1) {
    width: 30%;
}
table th:nth-child(2) {
    width: 70%;
}
table td {
    word-break: break-word;
}
</style>

| Abfragename | Beschreibung |
| --- | --- |
| Kanal-Engagement und Umsatz | Dieser Bericht zeigt für jeden Kanal alle Engagement-Metriken (wie Öffnungen und Klicks), Umsatz, Anzahl der Transaktionen und den Durchschnittspreis. {::nomarkdown} <ul> <li> <i>Anzahl der Transaktionen:</i> Anzahl der Kauf-Events </li> <li> <i>Durchschnittspreis:</i> Umsatz geteilt durch Transaktionen </li> </ul> {:/} ![]({% image_buster /assets/img_archive/channel_engagement_revenue.png %}) |
| Käufe und Umsatz nach Segment | Dieser Bericht zeigt Metriken für die Nachrichten, die an ein bestimmtes Segment gesendet wurden. <br><br> Kaufmetriken sind über den gesamten Berichtszeitraum eindeutig. Ein:e Nutzer:in kann höchstens einen Kauf generieren. Der Umsatz berücksichtigt jeden Kauf aus dem Berichtszeitraum. |
| Käufe und Umsatz für Varianten oder Schritte, nach Segment | Dieser Bericht zeigt Metriken für die Varianten oder Canvas-Schritte der Nachrichten, die an jedes Segment gesendet wurden. <br><br> Kaufmetriken sind über den gesamten Berichtszeitraum eindeutig. Ein:e Nutzer:in kann höchstens einen Kauf generieren. Der Umsatz berücksichtigt jeden Kauf aus dem Berichtszeitraum. |
| Top-/Flop-Messaging für Käufe | Dieser Bericht zeigt Kaufmetriken für die besten oder schlechtesten Campaigns, Canvases oder Canvas-Schritte. Jede Zeile ist eine Campaign, ein Canvas oder ein Canvas-Schritt. Sie müssen angeben, ob die besten oder schlechtesten Performer angezeigt werden sollen, und die spezifische Metrik, für die diese Analyse durchgeführt werden soll (z. B. *Eindeutige Käufe nach Empfang*, *Umsatz nach Empfang*, *Eindeutige Empfänger:innen*). <br><br> Die Zeilen in Top-Performer-Berichten werden von den besten zu den schlechtesten sortiert, während die Zeilen in Flop-Performer-Berichten von den schlechtesten zu den besten sortiert werden. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Channel templates" }

## Campaign-Templates {#campaign-templates}

| Abfragename | Beschreibung |
| --- | --- |
| Campaign-Umsatz nach Land | Dieser Bericht zeigt den Umsatz pro Land für eine bestimmte Campaign. Um diesen Bericht auszuführen, müssen Sie den API-Bezeichner für eine Campaign angeben. Den API-Bezeichner einer Campaign finden Sie unten auf der Detailseite der jeweiligen Campaign. <br><br> Dieser Bericht zeigt für jedes Land den generierten Umsatz, die Anzahl der Bestellungen, die Anzahl der Retouren, den Nettoumsatz und den Bruttoumsatz.<br><br> {::nomarkdown} <ul> <li> <i>Bestellungen:</i> Anzahl der Kauf-Events </li> <li><i> Retouren:</i> Anzahl der Kauf-Events mit negativen Umsatzwerten </li> <li><i> Nettoumsatz:</i> Umsatz aller Nicht-Retouren </li> <li><i> Bruttoumsatz:</i> Umsatz einschließlich des Werts der Retouren </li></ul>{:/} ![]({% image_buster /assets/img_archive/campaign_revenue_country.png %}){: style="max-width:70%;"} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Campaign templates" }

## Canvas-Templates {#canvas-templates}

| Abfragename | Beschreibung |
| --- | --- |
| Canvas-Umsatz nach Land | Dieser Bericht zeigt den Umsatz pro Land für ein bestimmtes Canvas. Um diesen Bericht auszuführen, müssen Sie den API-Bezeichner für ein Canvas angeben. Den Canvas-API-Bezeichner finden Sie unter **Analyze Variants**. <br><br> Dieser Bericht zeigt für jedes Land den generierten Umsatz, die Anzahl der Bestellungen, die Anzahl der Retouren, den Nettoumsatz und den Bruttoumsatz.<br><br> {::nomarkdown} <ul> <li> <i>Bestellungen:</i> Anzahl der Kauf-Events </li> <li><i> Retouren:</i> Anzahl der Kauf-Events mit negativen Umsatzwerten </li> <li><i> Nettoumsatz:</i> Umsatz aller Nicht-Retouren </li> <li><i> Bruttoumsatz:</i> Umsatz einschließlich des Werts der Retouren </li></ul>{:/} ![]({% image_buster /assets/img_archive/canvas_revenue_country.png %}){: style="max-width:70%;"} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Canvas templates" }

## E-Mail-Templates {#email-templates}

| Abfragename | Beschreibung |
| --- | --- |
| E-Mail-Bounces nach Domain | Die Anzahl der Bounces pro E-Mail-Domain, aufgeschlüsselt in Gesamt-Bounces, Hard Bounces und Soft Bounces. <br> ![]({% image_buster /assets/img_archive/query_builder_q4.png %}){: style="max-width:60%;"} |
| E-Mail-Zustellungsmetriken nach Tag | Dieser Bericht zeigt Metriken für die an jedem Tag gesendeten Nachrichten, z. B. wie viele E-Mails gesendet, zugestellt, als Soft Bounce oder Hard Bounce zurückgewiesen wurden. <br><br> Alle Metriken sind über den gesamten Berichtszeitraum eindeutig. Wenn beispielsweise eine Willkommens-E-Mail am 21. November einmal als Soft Bounce zurückkam, am 22. November zweimal als Soft Bounce zurückkam und nie zugestellt wurde: {::nomarkdown} <ul><li> Die Metrik <i>Soft Bounces</i> für den 21. November erhöht sich um eins.</li><li> Die Metrik <i>Soft Bounces</i> für den 22. November wird nicht beeinflusst. </li></ul>{:/} ![]({% image_buster /assets/img_archive/email_delivery_day.png %})|
| E-Mail-Engagement-Metriken nach Segment | Dieser Bericht zeigt Metriken für die an jedes Segment gesendeten Nachrichten, z. B. wie viele E-Mails gesendet, zugestellt, als Soft Bounce oder Hard Bounce zurückgewiesen wurden. <br><br> Alle Metriken sind über den gesamten Berichtszeitraum eindeutig. Wenn beispielsweise eine Willkommens-E-Mail am 21. November einmal als Soft Bounce zurückkam, am 22. November zweimal als Soft Bounce zurückkam und nie zugestellt wurde: {::nomarkdown} <ul><li> Die Metrik <i>Soft Bounces</i> für den 21. November erhöht sich um eins. </li><li> Die Metrik <i>Soft Bounces</i> für den 22. November wird nicht beeinflusst.</li></ul>{:/} ![]({% image_buster /assets/img_archive/email_engagement_segment.png %}) |
| E-Mail-Engagement-Metriken für Varianten oder Schritte, nach Segment | Dieser Bericht zeigt Metriken für die Varianten oder Canvas-Schritte der an jedes Segment gesendeten Nachrichten. Diese Metriken umfassen, wie viele E-Mails gesendet, zugestellt, als Soft Bounce oder Hard Bounce zurückgewiesen wurden. <br><br> Alle Metriken sind über den gesamten Berichtszeitraum eindeutig. Wenn beispielsweise eine Willkommens-E-Mail am 21. November einmal als Soft Bounce zurückkam, am 22. November zweimal als Soft Bounce zurückkam und nie zugestellt wurde: {::nomarkdown} <ul><li> Die Metrik <i>Soft Bounces</i> für den 21. November erhöht sich um eins. </li> <li> Die Metrik <i>Soft Bounces</i> für den 22. November wird nicht beeinflusst.</li></ul> {:/} |
| E-Mail-Performance nach Land | Dieser Bericht zeigt die folgenden Metriken für jedes Land: Sendungen, indirekte Öffnungsrate und direkte Öffnungsrate. Das Land ist das Land der Nutzer:innen zum Zeitpunkt des Push-Versands. <br><br> ![]({% image_buster /assets/img_archive/query_builder_q3.png %}) |
| Protokolle zu E-Mail-Abo-Änderungen | Dieser Bericht zeigt die Metriken, die zu den Abo-Änderungen jeder Nutzer:in protokolliert wurden, wie z. B. E-Mail-Adresse, Abo-Status, Zeitpunkt der Statusänderung und das zugehörige Canvas oder die zugehörige Campaign. |
| Opt-ins und Opt-outs für E-Mail-Abo-Gruppen | Dieser Bericht zeigt die Anzahl der eindeutigen Opt-ins und Opt-outs von Nutzer:innen für jede E-Mail-Abo-Gruppe pro Woche. Sie müssen mindestens eine [E-Mail-Abo-Gruppe]({{site.baseurl}}/user_guide/channels/email/subscriptions/) im Workspace haben, um diese Abfrage auszuführen. <br><br> ![]({% image_buster /assets/img_archive/query_builder_q2.png %}){: style="max-width:70%;"} |
| Angeklickte E-Mail-URLs | Dieser Bericht zeigt die Anzahl der Klicks auf jeden Link in einer E-Mail. Um diesen Bericht auszuführen, müssen Sie den API-Bezeichner für eine Campaign oder ein Canvas angeben. Den API-Bezeichner einer Campaign finden Sie unten auf der Detailseite der jeweiligen Campaign und den Canvas-API-Bezeichner unter **Analyze Variants**. <br><br> Dieser Bericht zeigt depersonalisierte Links und eine Klickanzahl für jeden Link. Ihr CSV-Download enthält die Nutzer-IDs aller Nutzer:innen, die geklickt haben, den angeklickten Link und einen Zeitstempel des Klicks. <br><br> *Depersonalisierte URLs:* URLs, bei denen Liquid-Tags entfernt wurden. <br><br> ![]({% image_buster /assets/img_archive/query_builder_q5.png %}){: style="max-width:70%;"} |
| Top-/Flop-Messaging für E-Mail-Engagement | Dieser Bericht zeigt E-Mail-Engagement-Metriken für die besten oder schlechtesten Campaigns, Canvases oder Canvas-Schritte. Sie müssen angeben, ob die besten oder schlechtesten Performer angezeigt werden sollen, und die spezifische Metrik, für die diese Analyse durchgeführt werden soll (z. B. *Gesendet*, *Soft Bounces* und *Eindeutige Öffnungen*). <br><br> Die Zeilen in Top-Performer-Berichten werden von den besten zu den schlechtesten sortiert, während die Zeilen in Flop-Performer-Berichten von den schlechtesten zu den besten sortiert werden. <br><br> ![]({% image_buster /assets/img_archive/top-bottom-email.png %}) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Email templates" }

## Mobilgeräte-Templates {#mobile-templates}

| Abfragename | Beschreibung |
| --- | --- |
| Mobilfunkanbieter | Die Anzahl der Nutzer:innen pro Mobilfunkanbieter, z. B. Verizon und T-Mobile. <br><br> ![]({% image_buster /assets/img_archive/device_carriers.png %}){: style="max-width:50%;"} |
| Gerätemodelle | Die Anzahl der Nutzer:innen pro Gerätemodell, z. B. iPhone 15 Pro und Pixel 7. <br><br> ![]({% image_buster /assets/img_archive/device_models.png %}){: style="max-width:50%;"} |
| Betriebssysteme | Die Anzahl der Nutzer:innen pro Betriebssystem, z. B. 17.4 und Android 14. <br><br> ![]({% image_buster /assets/img_archive/os_version.png %}){: style="max-width:50%;"} |
| Bildschirmauflösungen | Die Anzahl der Nutzer:innen pro Bildschirmauflösung, z. B. 1179x2556 und 750x1334. <br><br> ![]({% image_buster /assets/img_archive/device_screen_resolutions.png %}){: style="max-width:40%;"} |
| SMS-Fehlercodes | Dieser Bericht zeigt den Fehlertyp und die Anzahl der Fehler für jeden SMS-Fehlercode. <br><br>![]({% image_buster /assets/img_archive/sms_errors.png %}){: style="max-width:50%;"} |
| SMS-Anbieterfehler nach Nutzer:in | Dieser Bericht zeigt SMS-Fehlercodes für eine:n bestimmte:n Nutzer:in. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Mobile templates" }

## Push-Templates {#push-templates}

| Abfragename | Beschreibung |
| --- | --- |
| Push-Performance nach Land | Dieser Bericht zeigt die folgenden Metriken für jedes Land: Zustellungen, Öffnungsrate und Klickrate. Das Land ist das Land der Nutzer:innen zum Zeitpunkt des E-Mail-Versands. <br><br> ![]({% image_buster /assets/img_archive/query_builder_q7.png %}){: style="max-width:70%;"} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Push templates" }

## Aufschlüsselung nach Segment {#segment-breakdown}

| Abfragename | Beschreibung |
| -- | -- |
| E-Mail-Engagement-Metriken nach Segment | Dieser Bericht zeigt E-Mail-Performance-Metriken, aufgeschlüsselt nach Segment auf Campaign- oder Canvas-Ebene. |
| Käufe und Umsatz nach Segment | Dieser Bericht zeigt Kauf- und Umsatzmetriken, aufgeschlüsselt nach Segment für eine bestimmte Campaign oder ein bestimmtes Canvas. |
| Top-/Flop-Messaging für E-Mail-Engagement | Dieser Bericht zeigt die Campaigns, Canvases oder Canvas-Schritte mit der besten oder schlechtesten Performance für eine bestimmte E-Mail-Engagement-Metrik. |
| Top-/Flop-Messaging für Käufe | Dieser Bericht zeigt die Campaigns, Canvases oder Canvas-Schritte mit der besten oder schlechtesten Performance für eine bestimmte Kauf- oder Umsatzmetrik. |
| Push-Performance nach Segment | Dieser Bericht zeigt Push-Metriken, aufgeschlüsselt nach Segmenten. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Segment breakdown" }