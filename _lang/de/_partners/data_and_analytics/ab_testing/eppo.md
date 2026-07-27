---
nav_title: Eppo
article_title: Eppo
description: "Erfahren Sie, wie Sie Eppo in Braze integrieren können."
alias: /partners/eppo/
page_type: partner
search_tag: Partner
---

# Eppo

> [Eppo](https://www.geteppo.com/) ist eine Experimentierplattform der nächsten Generation, die es Teams ermöglicht, A/B-Tests durchzuführen, Features in großem Umfang zu verwalten und KI-gestützte Insights für datengestützte Entscheidungen zu nutzen.

*Diese Integration wird von Eppo verwaltet.*

Die Integration von Braze und Eppo erlaubt es Ihnen, A/B-Tests in Braze einzurichten und die Ergebnisse in Eppo zu analysieren, um Insights zu gewinnen und die Performance der Nachrichten mit langfristigen Geschäftsmetriken wie Umsatz oder Bindung zu verknüpfen.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
|---|---|
| Eppo-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Eppo-Konto. |
| Currents oder Snowflake-Datenfreigabe | Currents oder Snowflake-Datenfreigabe ist erforderlich, damit Eppo die Experimentdaten analysieren kann. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Integration

### 1. Schritt: Currents oder Snowflake-Datenfreigabe in Braze konfigurieren {#step-1-configure-currents-or-snowflake-data-sharing-in-braze}

Eppo analysiert Experimente direkt in Ihrem Data Warehouse. Um die Integration zu ermöglichen, müssen die Daten zum Messaging-Engagement von Braze in dem mit Eppo verbundenen Warehouse verfügbar sein. Mit Currents können Sie Kampagnendaten aus Braze exportieren oder mit [Snowflake-Datenfreigabe]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/) auf Braze-Daten in Ihrer Snowflake-Instanz zugreifen.

### 2. Schritt: Experiment in einer Braze-Kampagne oder einem Canvas einrichten {#step-2-set-up-your-experiment-in-a-braze-campaign-or-canvas}

Sie können in Ihren Campaigns und Canvases native Features für A/B-Tests verwenden. Mehr dazu erfahren Sie unter [Multivariate und A/B-Tests]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/#what-are-multivariate-and-ab-testing).

### 3. Schritt: Eppo für die Messung von Braze-Experimenten einrichten {#step-3-set-up-eppo-to-measure-braze-experiments}

Um Experimente mit Braze-Daten in Eppo durchzuführen, erstellen Sie [Zuweisungstabellen](https://docs.geteppo.com/data-management/definitions/assignment-sql/) in Ihrem Warehouse auf der Grundlage der aus Braze exportierten Nachrichten-Ereignisdaten auf Nutzer:innenebene. Für Canvas- und Campaign-Experimente werden getrennte Tabellen empfohlen, da sie auf unterschiedlichen Metadaten beruhen.

{% tabs local %}
{% tab Canvas-Experimente %}
Für Canvas-Experimente können Zuweisungen entweder erstellt werden:

- Auf der Einstiegsebene von Canvas (`users.canvas.Entry`)
- Oder in einem Canvas-Experiment-Schritt (`users.canvas.experimentstep.SplitEntry`)

In diesen Fällen werden Felder wie `canvas_name`, `experiment_step_id`, `canvas_variation_name` und `experiment_split_id` verwendet, um den Namen und die Variante des Experiments zu definieren.

{% endtab %}

{% tab Campaign-Experimente %}
Bei Campaign-Experimenten verwenden Sie Sendeereignisse (wie Push, E-Mail, SMS), um festzustellen, wann Nutzer:innen das Experiment betreten haben. `campaign_name`, `message_variation_name` und `time` werden verwendet, um die Zuweisungstabelle aufzufüllen.

{% endtab %}
{% endtabs %}

Um nachrichtenspezifische Metriken (wie Klicks oder Öffnungen) zu verfolgen, fügen Sie eine **sekundäre Entität** ein, indem Sie eine `combined_id` erstellen, die die Nutzer-ID mit dem Namen der Campaign oder des Canvas verbindet. Diese `combined_id` wird auch in Ihren Faktentabellen verwendet, um die Metriken mit dem richtigen Experiment und der richtigen Variante abzugleichen.

Eppo verwendet diese Zuweisungen und Faktentabellen, um die Ergebnisse zu analysieren, und es wird empfohlen, ein **Protokoll** in Eppo einzurichten, um die Einrichtung zukünftiger Experimente zu standardisieren. Weitere Informationen finden Sie in der [Dokumentation von Eppo](https://docs.geteppo.com/guides/marketing/integrating-with-braze/).

## Support

Wenn Sie Fragen zur Einrichtung von Braze-Currents, Snowflake-Datenfreigabe oder zur Konfiguration von multivariaten Kampagnen haben, wenden Sie sich an Ihren Customer-Success-Manager von Braze.

Wenn Sie Hilfe bei der Konfiguration von Eppo zur Messung von Braze-Experimenten benötigen, wenden Sie sich an das Eppo-Support-Team.