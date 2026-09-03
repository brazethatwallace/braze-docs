---
nav_title: Abrechnung
article_title: Abrechnung
alias: /subscription_and_usage/
page_order: 5
page_type: reference
description: "Dieser Referenzartikel behandelt die Seite „Abrechnung“, auf der Sie Ihren Datenverbrauch überwachen und prüfen können."
tool: Dashboard
search_rank: 5
---

# Abrechnung {#billing}

> Erfahren Sie, wie Sie die Seite **Abrechnung** nutzen, um Ihren Datenverbrauch über Workspaces, Apps und Event-Quellen hinweg zu überwachen und zu prüfen. Dieser Artikel behandelt die verschiedenen Abschnitte auf der Seite und die Informationen, die sie Ihnen liefern können.

Um zur Seite **Abrechnung** zu navigieren, gehen Sie zu **Einstellungen** > **Abrechnung**.

Die Seite **Abrechnung** enthält die folgenden Tabs:

- [Abos und Nutzung](#subscriptions-and-usage)
- [Meistgenutzte Events und Attribute nach App](#most-used-events-and-attributes-by-app)
- [Datenpunkt-Nutzung gesamt](#total-data-points-dashboard)

## Abonnements und Nutzung {#subscriptions-and-usage}

Der Tab **Abonnements und Nutzung** enthält Nutzungsdiagramme und Ihre Vertragsdetails. Die Daten auf dieser Seite werden täglich um 22:00 Uhr Eastern Time (ET) aktualisiert. Sie spiegeln keine Realtime-Aktivitäten wider.

### Nutzungsdiagramme {#usage-graphs}

Hier finden Sie Nutzungsdiagramme, die für Ihre Workspaces gelten. Ihr eigenes Dashboard kann je nach den von Ihnen erworbenen Produkten unterschiedliche Nutzungsmetriken anzeigen.

![Nutzungsdiagramm mit monatlich eindeutigen Besucher:innen]({% image_buster /assets/img/subscription_and_billing4.png %}){: style="max-width:90%;"}

Diese Diagramme können monatlich aktive Nutzer:innen, monatlich eindeutige Besucher:innen und E-Mail-Versendungen anzeigen. Nutzungsdiagramme wie diese sind besonders hilfreich, wenn Sie die Nutzung budgetieren und ein tieferes Verständnis dafür gewinnen möchten, welche Workspaces zur Gesamtnutzung beitragen.

### Vertragsdetails {#contract-details}

Die Vertragsdetails listen das Start- und Enddatum Ihres aktuellen Vertrags mit Braze auf.

#### Hinweise {#considerations}

Wenn Ihr Vertrag monatlich eindeutige Besucher:innen (MUV) verwendet und Sie zu einem Vertrag wechseln, der nur monatlich aktive Nutzer:innen (MAU) nutzt, werden Ihre historischen Daten weiterhin im MUV-Diagramm angezeigt, und Ihre neuen Daten erscheinen nur im MAU-Diagramm. Wenn Ihr Vertrag beispielsweise im Oktober endet, zeigt das MUV-Diagramm Daten bis Ende September an.

## Meistgenutzte Events und Attribute nach App {#most-used-events-and-attributes-by-app}

Unter **Meistgenutzte Events und Attribute nach App** können Sie die Treiber Ihrer Attribut- und angepassten Event-Datenpunkt-Nutzung überprüfen.

![Meistgenutzte Events und Attribute nach App]({% image_buster /assets/img/most_used_events_attributes_time.png %})

Für jede App können Sie **Aufschlüsselung anzeigen** auswählen, um eine geschätzte Anzahl für jedes spezifische angepasste Attribut, Profilattribut und angepasste Event für den ausgewählten Zeitraum anzuzeigen, sowie den prozentualen Anteil der Attribut- und Event-Updates dieser App, die durch dieses Attribut oder Event verursacht wurden.

![Tab „Aufschlüsselung“ für meistgenutzte Events und Attribute nach App]({% image_buster /assets/img/most_used_events_attributes_2.png %}){: style="max-width:60%"}

Datenaufschlüsselungen wie diese können Ihnen helfen zu verstehen, welche spezifischen Datenpunkte große Prozentsätze Ihres Kontingents ausmachen. Wir empfehlen, diese Informationen von Zeit zu Zeit zu überprüfen, um sicherzustellen, dass Sie keine Datenpunkte auf versehentliche und unnötige Weise verbrauchen. Ihr Customer-Success-Manager kann Ihnen Orientierung geben, wie Sie das Beste aus Ihrem aktuellen Plan herausholen, oder Optionen für mehr Flexibilität anbieten.

## Dashboard „Gesamt-Datenpunkte“ {#total-data-points-dashboard}

Der Tab **Gesamt-Datenpunkt-Nutzung** bietet einen detaillierten Einblick in Ihre Datenpunkt-Nutzung. Sie können alle Daten in diesem Bereich entweder nach Wochen oder Monaten aggregiert anzeigen.

{% alert note %}
Datenpunkt-Informationen werden alle 24 Stunden zwischengespeichert.
{% endalert %}

Wenn Sie Admin sind und den Tab **Gesamt-Datenpunkt-Nutzung** nicht sehen können, stellen Sie sicher, dass Ihr Browser Drittanbieter-Cookies für Ihre Braze-Dashboard-Domain zulässt und sich nicht im Inkognito-Modus befindet.

![Datenpunkt-Nutzung nach Wochen filtern]({% image_buster /assets/img/subscription_and_billing2.png %})

### Vertragsdetails

Hier finden Sie Informationen darüber, wann Ihr aktueller Braze-Vertrag beginnt und endet, sowie zugeteilte Datenpunkte und eine Summe aller Datenpunkte, die bisher in Ihrem aktuellen Vertrag verwendet wurden.

Die Felder in diesem Bereich sind wie folgt definiert:

- **Vertragstyp:** Abrechnungszeitraum-Struktur, entweder jährlich oder mehrjährig.
- **Vertragsbeginn und -ende:** Start- und Enddatum des gesamten Vertrags.
- **Zugeteilte Datenpunkte:** Die Menge der im Vertrag pro Abrechnungszeitraum zugeteilten Datenpunkte.
- **Vertragliche Datenpunkt-Nutzung:** Eine kumulative Gesamtsumme aller über die Vertragslaufzeit protokollierten Datenpunkte, die im nächsten Abrechnungszeitraum nicht zurückgesetzt wird.

### Unternehmens-Abrechnungsdaten {#company-billing-data}

#### Gesamte Datenpunkt-Nutzung auf App-Ebene {#app-level-total-data-point-usage}

Dieses Diagramm zeigt Ihre Datenpunkt-Nutzung über alle Apps hinweg.

![Gesamte Datenpunkt-Nutzung auf App-Ebene zeigt die verwendeten Datenpunkte für jede App.]({% image_buster /assets/img/app_level_total.png %})

Wählen Sie eine der Summen aus, um die Tabelle **Datenpunkt-Nutzung im Zeitverlauf** anzuzeigen, die Ihre wöchentlichen Datenpunkt-Gesamtwerte für jeden Workspace enthält. Zeilen mit einer leeren Spalte **App-Name** stellen Datenpunkte dar, die keiner App zugeordnet sind (z. B. Datenpunkte, die in Anfragen ohne angegebene `app_id` verwendet werden).

![Datenpunkt-Nutzung im Zeitverlauf mit wöchentlichen Datenpunkt-Gesamtwerten für zwei Workspaces.]({% image_buster /assets/img/data_point_usage_time.png %})

#### Workspace-Datenpunkt-Nutzung {#workspace-data-point-usage}

Dieses Diagramm ermöglicht es Ihnen, die gesamte Datenpunkt-Nutzung eines Unternehmens nach Workspace zu bewerten. Es gibt Ihnen die Möglichkeit einzuschätzen, wie jeder Workspace zur Datenpunkt-Nutzung des Unternehmens beiträgt.

![Diagramm zur Workspace-Datenpunkt-Nutzung für zwei Workspaces]({% image_buster /assets/img/appgroup_datapoint_usage.png %}){: style="max-width:90%;"}

#### Datenpunkt-Nutzung im Abrechnungszyklus nach Event-Quelle {#billing-cycle-data-point-usage-by-event-source}

Dieses Diagramm ermöglicht es Ihnen zu sehen, wie sich die Datenpunkt-Nutzung auf verschiedene Event-Quellen verteilt, wie z. B. verschiedene API-Attribute, angepasste Events und Sessions.

![Datenpunkt-Nutzung im Abrechnungszyklus nach Event-Quelle mit Darstellung der Datenpunkt-Verteilung auf verschiedene Event-Quellen.]({% image_buster /assets/img/event_source_stats.png %})

#### Datenpunkt-Nutzung im Zeitverlauf {#data-point-usage-over-time}

Dieses Diagramm gibt Ihnen die Möglichkeit, schnell Ihre gesamte Datenpunkt-Nutzung im Vergleich zu Ihrer zugeteilten Menge an Datenpunkten zu sehen.

![Datenpunkt-Nutzung im Zeitverlauf mit Vergleich der zugeteilten Datenpunkte im aktuellen Abrechnungszyklus und der laufenden Gesamtsumme]({% image_buster /assets/img/company_data_point_usage_time.png %}){: style="max-width:90%;"}

## Nächste Schritte {#next-steps}

{% article_tiles %}
- name: Benachrichtigungseinstellungen
  link: /docs/user_guide/administer/global/admin_settings/notification_preferences
- name: Dashboard zur Nutzung von Credits
  link: /docs/credits_usage_dashboard
{% endarticle_tiles %}