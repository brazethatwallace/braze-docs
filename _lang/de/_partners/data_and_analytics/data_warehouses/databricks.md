---
nav_title: Databricks
article_title: Databricks
description: "Dieser Artikel beschreibt Databricks Delta Sharing mit Braze (geschlossene Beta), mit dem Sie in Ihrem Databricks-Konto auf Braze-Engagement- und Campaign-Daten zugreifen können."
page_type: partner
search_tag: Partner
permalink: /databricks/
hidden: true
---

# Databricks

> [Databricks](https://www.databricks.com/) ist eine einheitliche, offene Analytics-Plattform zum Erstellen, Bereitstellen, Teilen und Pflegen von unternehmenstauglichen Daten-, Analytics- und KI-Lösungen im großen Maßstab. Die Databricks Data Intelligence Platform lässt sich in Cloud-Speicher und Sicherheitslösungen in Ihrem Cloud-Konto integrieren und verwaltet und stellt Cloud-Infrastruktur für Sie bereit.

{% alert important %}
Databricks Delta Sharing mit Braze befindet sich in der **geschlossenen Beta**. Verfügbarkeit, unterstützte Regionen und Produktverhalten können sich ändern. Kontaktieren Sie Ihren Braze-geschäftskunden-Success-Manager, um teilzunehmen oder zu bestätigen, ob dieses Feature für Ihren Workspace aktiviert ist.
{% endalert %}

## Delta Sharing (Braze zu Databricks) {#delta-sharing-braze-to-databricks}

Databricks [Delta Sharing](https://docs.databricks.com/en/delta-sharing/index.html) ermöglicht es Ihnen, Daten sicher mit Geschäftsbereichen und Tochtergesellschaften über Clouds oder Regionen hinweg zu teilen, ohne die Daten zu kopieren oder zu replizieren.

**Verwenden Sie Delta Sharing, wenn Sie Folgendes möchten:**
- Braze-Ereignis- und Campaign-Daten mit Databricks SQL abfragen
- Komplexe Berichte erstellen und Attribution-Modellierung durchführen
- Braze-Daten mit anderen Daten in Ihrem Databricks-Konto verknüpfen
- Ihre Engagement-Daten über Kanäle, Branchen und Geräteplattformen hinweg vergleichen

Einrichtungsanweisungen finden Sie unter [Databricks Delta Sharing]({{site.baseurl}}/delta_sharing/).

Mehr über Delta Sharing auf Databricks erfahren Sie unter [Was ist Delta Sharing?](https://www.databricks.com/product/delta-sharing).

## Voraussetzungen {#prerequisites}

Bevor Sie dieses Feature nutzen können, müssen Sie Folgendes abschließen:

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Braze-Zugang | Um auf dieses Feature in Braze zuzugreifen, kontaktieren Sie Ihren Braze-Konto- oder geschäftskunden-Success-Manager. |
| Databricks-Konto | Ein Databricks-Konto mit `admin`-Berechtigungen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

Wenn Sie bereit sind, das Teilen zu konfigurieren und geteilte Daten abzufragen, fahren Sie mit [Databricks Delta Sharing]({{site.baseurl}}/delta_sharing/) fort.