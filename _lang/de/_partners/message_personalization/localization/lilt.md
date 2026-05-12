---
nav_title: LILT
article_title: LILT
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und LILT."
alias: /partners/lilt/
page_type: partner
search_tag: Partner
---

# LILT

> [LILT](https://lilt.com/) ist die komplette KI-Lösung für die Übersetzung und Inhaltserstellung in Unternehmen. Mit KI-Agenten und vollautomatisierten Workflows ermöglicht LILT globalen Unternehmen die Skalierung und Optimierung ihres Inhalts-, Produkt-, Kommunikations- und Supportbetriebs.

_Diese Integration wird von LILT gepflegt._

## Über diese Integration {#about-this-integration}

Der LILT Braze Connector ermöglicht die Übersetzung von HTML-E-Mail-Templates mit KI-Geschwindigkeit und in Unternehmensqualität. Fordern Sie eine markengerechte Sofortübersetzung oder eine qualitätsgesicherte verifizierte Übersetzung an und erhalten Sie mehrsprachige E-Mail-Inhalte von LILT direkt in Braze.

## Anwendungsfälle {#use-cases}

Die LILT-Braze-Integration automatisiert und beschleunigt den Übersetzungsprozess und ermöglicht es globalen Marketingteams, ihre mehrsprachigen Campaigns schnell und mit Markenkonsistenz zu starten.

### Optimierter globaler Kampagnenstart {#streamlined-global-campaign-launch}

Starten Sie Marketingkampagnen in mehreren Regionen gleichzeitig, ohne Verzögerungen durch manuelle Übersetzungsübergaben.

- **Szenario:** Ihr Unternehmen bringt ein neues Produkt in 10 Ländern auf den Markt.
- **Lösung:** Ihr Marketingteam stellt das englische E-Mail-Template in Braze fertig, versieht es mit dem Tag `LILT: Ready`, und der LILT Connector zieht den Inhalt automatisch ab. Domänenspezifische Linguist:innen überprüfen die KI-Übersetzungsvorschläge in der LILT-Plattform zur Qualitätssicherung, und der Konnektor pusht die übersetzten Versionen zurück nach Braze.
- **Vorteil:** Verkürzt die Markteinführungszeit Ihrer globalen Campaigns von Tagen auf Stunden, sodass alle Kund:innen die Ankündigung des neuen Produkts zum optimalen Zeitpunkt erhalten können.

### Sofortige markengerechte Lokalisierung {#instant-brand-aligned-localization}

Nutzen Sie die KI von LILT für sofortige, markengerechte Übersetzungen bei zeitkritischer Kommunikation.

- **Szenario:** Sie müssen sofort E-Mails für einen Flash-Sale, ein zeitlich begrenztes Angebot oder eine dringende Dienstunterbrechung in fünf geografischen Märkten versenden.
- **Lösung:** Sie taggen das E-Mail-Template mit `LILT: Instant`. LILT nutzt seine KI und die für Ihr Unternehmen spezifischen linguistischen Ressourcen (wie Terminologie und Stilrichtlinien), um innerhalb von Minuten eine hochwertige, markenkonsistente Übersetzung zu erstellen.
- **Vorteil:** Ermöglicht hyperresponsive Realtime-Kommunikation, ohne dass Markenstimme oder Qualität beeinträchtigt werden – entscheidend für zeitkritisches Marketing.

## Voraussetzungen {#prerequisites}

| Voraussetzung | Beschreibung |
|-----------------------|-----------------|
| Ein LILT-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, ist ein LILT-Konto erforderlich. |
| Ein Braze-REST-API-Schlüssel | Ein Braze-REST-API-Schlüssel mit den folgenden Berechtigungen:<br>- `templates.email.create`<br>- `templates.email.update`<br>- `templates.email.info`<br>- `templates.email.list`<br>- `templates.translations.source.get`<br>- `templates.translations.update`<br>- `templates.translations.get`<br>- `templates.translations.all.get`. <br><br> Erstellen Sie diesen Schlüssel im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel**. |
| Ein Braze-REST-Endpunkt | [Ihre REST-Endpunkt-URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


## Integration

### 1. Schritt: Konfigurieren Sie den LILT Braze Connector {#step-1-configure-the-lilt-braze-connector}

1. Melden Sie sich bei LILT an und gehen Sie dann zu **Connect** > **New Connector** > **Braze**.

![Braze-Konnektor in LILT.]({% image_buster /assets/img/lilt/image_1_select_connector.png %})

{: start="2"}
2. Wählen Sie den gewünschten Lokalisierungs-Workflow für Ihre Braze-Inhalte aus.

![Braze-Workflow in LILT.]({% image_buster /assets/img/lilt/image_2_select_workflow.png %})

{: start="3"}
3. Geben Sie die erforderlichen Konfigurationsdetails ein und überprüfen Sie sie:
- Ihr Braze-API-Schlüssel
- Braze-REST-Endpunkt

![API-Zugangsdaten vervollständigen.]({% image_buster /assets/img/lilt/image_3_api_creds.png %})

{: start="4"}
4. Wählen Sie **Verify**, um die Einrichtung zu testen. Nachdem die Verbindung bestätigt wurde, speichern Sie die Konfiguration.

### 2. Schritt: Bereiten Sie Ihren Braze-Workspace vor {#step-2-prepare-your-braze-workspace}

1. Aktivieren Sie die Mehrsprachigkeitsfunktionen in Ihren Braze-Workspace-Einstellungen.

![Lokalisierungen in Braze einrichten.]({% image_buster /assets/img/lilt/image_4_lilt_locales.png %})

{: start="2"}
2. Erstellen Sie in Braze die folgenden Tags für Ihren LILT-Workflow:
- `LILT: Ready`
- `LILT: In progress`
- `LILT: Sent to LILT`
- `LILT: Delivered`
- `LILT: Needs Attention`
- `LILT: Instant`

![LILT-Tags in Braze einrichten.]({% image_buster /assets/img/lilt/image_5_lilt_tags.png %})

{: start="3"}
### 3. Schritt: Senden Sie Inhalte zur Übersetzung an LILT {#step-3-send-content-to-lilt-for-translation}

1. Nachdem Sie den LILT Braze Connector eingerichtet haben, verwenden Sie Liquid-Übersetzungs-Tags in Ihren Braze-E-Mail-Templates, um die zu übersetzenden Inhalte zu kennzeichnen.
- Beispiel:  {% raw %}`{% translation id_0 %}`Hello, `{{first_name}}!{% endtranslation %}`{% endraw %}
2. Starten Sie die Übersetzung, indem Sie den Tag des Templates aktualisieren, um den gewünschten Workflow anzugeben:
- Wählen Sie `LILT: Ready` für eine verifizierte Übersetzung
- Wählen Sie `LILT: Instant` für eine markengerechte Sofortübersetzung
3. Der LILT Braze Connector wird zu dem von Ihnen festgelegten Zeitpunkt ausgeführt, um die getaggten Inhalte in LILT zu übernehmen. Verfolgen Sie den Übersetzungsfortschritt – die Inhalts-Tags werden in Braze automatisch aktualisiert und spiegeln den Stand Ihres Projekts wider.

![Braze-E-Mail-Template mit Übersetzungs-Tags.]({% image_buster /assets/img/lilt/image_6_braze_template.png %})