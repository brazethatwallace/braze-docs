---
nav_title: Databricks Mosaic
article_title: Databricks Mosaic
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Databricks Mosaic, mit der Sie Databricks-Modelle mit Braze verbinden können, um sie mit angepassten KI-Agenten zu verwenden."
alias: /partners/databricks_mosaic/
page_type: partner
search_tag: Partner

---

# Databricks Mosaic

> [Databricks Mosaic KI](https://www.databricks.com/product/artificial-intelligence) ist die einheitliche Plattform von Databricks zum Erstellen, Bereitstellen und Verwalten von KI- und maschinellen Lernmodellen im großen Maßstab auf der Databricks Data Intelligence Platform.

{% multi_lang_include alerts/important_alerts.md alert='Braze Agents' %}

_Diese Integration wird von Databricks gepflegt._

## Über die Integration {#about-the-integration}

Die Integration von Braze und Databricks Mosaic ermöglicht es Ihnen, Ihr Databricks-Token / Textbaustein und Ihren Workspace mit Braze zu verbinden, damit Sie Databricks-Modelle beim Erstellen angepasster KI-Agenten verwenden können. Braze nutzt Ihre Databricks-Mosaic-Zugangsdaten, um Inhalte für Ihre Kund:innen zu generieren. Mit dieser Integration können Ihre Agenten personalisierte Texte generieren, Realtime-Entscheidungen treffen oder Katalogfelder mithilfe von Databricks-Modellen aktualisieren.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
|---|---|
| Databricks-Konto mit persönlichem Zugriffstoken | Ein Databricks-Konto mit einem [persönlichen Zugriffstoken](https://docs.databricks.com/en/dev-tools/auth/pat.html). Wenden Sie sich bei Fragen an Ihre:n Administrator:in oder den [Databricks-Support](https://help.databricks.com/). |
| Databricks-Workspace-Name | Der Workspace-Name (oder die Instanz) für Ihr Databricks-Konto. Dies ist die Subdomain vor `.cloud.databricks.com` oder `.azuredatabricks.net` (zum Beispiel `dbc-eb57d699-f22c`). |
| Braze-Instanz | Sie finden Ihre Braze-Instanz auf der [API-Übersichtsseite]({{site.baseurl}}/api/basics/#endpoints) oder über Ihre:n Braze-Onboarding-Manager:in:in. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Integration

So verbinden Sie Ihre Databricks-Mosaic-Zugangsdaten mit Braze:

1. Gehen Sie im Braze-Dashboard zu **Partnerintegrationen** > **Technologie-Partner** und suchen Sie **Databricks Mosaic Integration**.
2. Geben Sie Ihr **Databricks-Token / Textbaustein** ein.
3. Geben Sie Ihren **Databricks-Workspace-Namen** ein. Dies ist die Subdomain vor `.cloud.databricks.com` oder `.azuredatabricks.net`.
4. Wählen Sie **Speichern**.

Nach dem Speichern zeigt Braze einen Verbindungsstatus mit Datum und Uhrzeit der Verbindung an. Sie können Databricks-Modelle auswählen, wenn Sie in der Agentenkonsole [einen angepassten Agenten erstellen]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/).

Um die Integration zu entfernen, wählen Sie auf der Seite **Databricks Mosaic Integration** die Option **Trennen**.

Kontaktieren Sie den [Databricks-Support](https://help.databricks.com/) bei Problemen oder Fragen zu Ihrer Integration.