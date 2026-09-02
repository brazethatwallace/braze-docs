---
nav_title: Tellius
article_title: Tellius
alias: /partners/tellius/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Tellius, einer Plattform für Decision Intelligence und Augmented Analytics, die es Ihnen erlaubt, Daten zu nutzen, ohne auf BI-Ingenieure angewiesen zu sein, um Dashboards zu erstellen und Insights zu generieren, um bessere Marketing-Entscheidungen zu treffen."
page_type: partner
search_tag: Partner

---

# Tellius

> [Tellius](https://www.tellius.com/), eine Plattform für Decision Intelligence und Augmented Analytics, ermöglicht es Ihnen, Fragen zu Ihren Daten mit Hilfe der natürlichsprachlichen Suche zu beantworten und mit KI-gestützten Insights das „Warum“ zu verstehen.

Die Integration von Braze und Tellius ermöglicht es Nutzer:innen, Daten zu nutzen, ohne auf BI-Ingenieure angewiesen zu sein, um Dashboards zu erstellen und Insights zu generieren, um bessere Marketing-Entscheidungen zu treffen. Diese Integration setzt voraus, dass Braze-Daten in Snowflake gespeichert sind. Tellius kann sich direkt mit Snowflake verbinden und Push-Abfragen mit der Integration im Live-Modus durchführen.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Tellius-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Tellius-Konto. Sie können Ihre Tellius-Journey mit einer [kostenlosen Demo](https://www.tellius.com/free-trial/) beginnen. |
| Snowflake-Datenfreigabeprogramm | Wenn Sie bereits Snowflake-Kund:in sind, wenden Sie sich an Ihre Braze-Vertretung, um sich über das Snowflake-Datenfreigabeprogramm zu informieren, mit dem Sie Ihre Braze-Daten in Ihre Snowflake-Instanz übertragen können. |
| Snowflake-Lesekonto | Wenn Sie kein:e Snowflake-Kund:in sind, wenden Sie sich an Ihre Braze-Vertretung, um ein Snowflake-Lesekonto zu erhalten, das für Sie eingerichtet werden kann, damit Sie auf Ihre Braze-Daten zugreifen können. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Integration

### 1. Schritt: Zugang zu Braze über Snowflake erhalten {#step-1-obtain-access-to-braze-through-snowflake}

Braze speichert granulare Kundendaten in Snowflake. Sie können Ihre Braze-Daten nutzen, um Insights über das Braze-Snowflake-Datenfreigabeprogramm zu generieren oder ein Snowflake-Lesekonto zu erhalten.

Folgen Sie der [Snowflake-Integration]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/), um sich einzurichten.

### 2. Schritt: Tellius mit Braze-Daten in Snowflake verbinden {#step-2-connect-tellius-to-braze-data-in-snowflake}

Verbinden Sie Tellius mit Braze-Daten in Snowflake mit einer der folgenden Methoden:

- Direkter Zugang: Um Daten in Tellius zu laden, folgen Sie den Schritten unter [Datensätze laden](https://help.tellius.com/article/jn6o59d5gk-load-datasets).
- OAuth-Zugang: Für den OAuth-Zugriff auf Snowflake befolgen Sie die Schritte für die [OAuth-Authentifizierung](https://help.tellius.com/article/11517w63b6-oauth-authentication-for-snowflake).

### 3. Schritt: Business View in Tellius aus geladenen Daten erstellen {#step-3-create-business-view-in-tellius-from-loaded-data}

Um mit der natürlichsprachlichen Suche und automatisierten Insights zu beginnen, erstellen Sie eine [Business View](https://help.tellius.com/article/hy9yvh5tom-create-business-view) und wählen Sie Datensätze aus Ihrer Snowflake-Verbindung aus.

### 4. Schritt: Den größten Nutzen aus Ihren Daten mit Tellius herausholen {#step-4-get-the-most-value-out-of-your-data-using-tellius}

In Tellius gibt es eine geführte Oberfläche, die Sie durch die Features der Plattform führt. Weitere Fragen und Anleitungen finden Sie in der vollständigen [Wissensdatenbank](https://help.tellius.com/).