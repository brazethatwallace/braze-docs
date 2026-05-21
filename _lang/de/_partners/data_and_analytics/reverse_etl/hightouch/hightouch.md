---
nav_title: Hightouch
article_title: Hightouch
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Hightouch, einer Plattform zur Synchronisierung Ihrer Kundendaten aus Ihrem Data Warehouse mit Business-Tools."
page_type: partner
search_tag: Partner

---

# Hightouch

> [Hightouch](https://hightouch.io) ist eine moderne Plattform für die Datenintegration, mit der Sie Kund:innen-, Produkt- oder proprietäre Daten aus Ihrem Data Warehouse oder Data Lake mit jeder App Ihrer Wahl synchronisieren können – ganz ohne Unterstützung Ihrer IT- oder Entwicklerteams.

Die Integration von Braze und Hightouch ermöglicht es Ihnen, bessere Campaigns in Braze mit aktuellen Kundendaten aus Ihrem Data Warehouse zu erstellen. Durch die automatische Synchronisierung von Kundendaten in Braze müssen Sie sich nicht mehr um die Datenkonsistenz kümmern und können sich auf den Aufbau erstklassiger Kundenerlebnisse konzentrieren.

Mit dieser Integration können Sie auch [Nutzer:innen-Kohorten in Braze importieren]({{site.baseurl}}/partners/data_and_analytics/reverse_etl/hightouch/hightouch_cohort_import/) und gezielte Campaigns auf der Grundlage von Daten versenden, die möglicherweise nur in Ihrem Warehouse vorhanden sind.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
|---|---|
| Hightouch-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Hightouch-Konto. |
| Braze REST-API-Schlüssel | Ein Braze REST-API-Schlüssel mit den Berechtigungen `users.track` und `users.export.ids`. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze REST-Endpunkt | Ihre URL für den REST-Endpunkt. Ihr Endpunkt hängt von der [Braze-URL für Ihre Instanz]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) ab.<br><br>Hightouch benötigt den Namen des Clusters, in dem sich Ihre Braze-Instanz befindet. Wenn Ihr Braze-Endpunkt zum Beispiel `https://rest.iad-01.braze.com` ist, benötigen Sie nur `iad-01`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Anwendungsfälle {#use-cases}

* Synchronisieren Sie Daten über Nutzer:innen und Konten in Braze, um hyper-personalisierte Campaigns zu erstellen.
* Aktualisieren Sie Ihre Braze Segments automatisch mit aktuellen Daten aus Ihrem Data Warehouse.
* Bieten Sie bessere Erlebnisse, indem Sie Daten von anderen Kund:innen-Touchpoints in Braze einbringen.
* Importieren Sie Kohorten von Nutzer:innen in Braze, um gezielte Campaigns und Canvases zu versenden.

## Integration

### 1. Schritt: Erstellen Sie Ihr Hightouch-Braze-Ziel {#step-1-create-your-hightouch-braze-destination}

1. Klicken Sie auf der Hightouch-Plattform im Bereich **Destinations** auf **Add destination**.
2. Wählen Sie **Braze** aus der Liste der verfügbaren Ziele aus.
3. Geben Sie Ihren Braze REST-Endpunkt (ohne „https://rest.“) und Ihren Braze REST-API-Schlüssel an.<br><br>![]({% image_buster /assets/img/hightouch/hightouch_braze_setup.png %})

### 2. Schritt: Synchronisierung von Objekten und Ereignissen {#step-2-object-and-event-syncing}

Hightouch unterstützt die Synchronisierung sowohl mit Nutzer:innen-Objekten als auch mit Ereignissen.

| Ziel | Beschreibung | Unterstützte Modi |
|---|---|---|
| Objekt | Synchronisiert Datensätze mit Objekten wie Nutzer:innen oder Organisationen in Ihrem Ziel. | Upsert oder Update |
| Ereignisse | Synchronisiert Datensätze als Ereignisse in Ihr Ziel; dies geschieht häufig in Form eines Track-Aufrufs. | Ereignis-Tracking oder Kauf-Tracking |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="2. Schritt: Synchronisierung von Objekten und Ereignissen" }

{% alert note %}
Weitere Informationen darüber, wie sich Synchronisierungen auf die Protokollierung von Datenpunkten auswirken, finden Sie bei [Hightouch](https://hightouch.com/docs/destinations/braze#syncing-and-data-point-consumption).
{% endalert %}

#### Synchronisieren von Braze-Objekten {#syncing-braze-objects}

Sie können Hightouch-Objekte (Nutzer:innen-Felder) mit den entsprechenden Braze-Standard- oder angepassten Feldern synchronisieren. Sie können auch einen Datensatzabgleich durchführen, um die Daten zwischen den beiden Plattformen zu vereinheitlichen.

#### Synchronisierung von Braze-Ereignissen {#syncing-braze-events}

Hightouch ermöglicht Ihnen das Tracking von Ereignis- und Kaufdaten und deren Synchronisierung mit Braze. In Hightouch können mehrere Optionen eingestellt werden, die sich auf das Synchronisierungsverhalten auswirken, z. B. die Einrichtung von Tracking-Daten und die Definition des Verhaltens bei nicht vorhandenen Nutzer:innen.

{% alert important %}
Weitere Anweisungen zur Synchronisierung von Objekten und Ereignissen finden Sie in der [Hightouch-Dokumentation](https://hightouch.io/docs/destinations/braze/).
{% endalert %}



## Demo zur Integration {#integration-demo}

<div class="video-container">
    <iframe width="560" height="315" src="https://drive.google.com/file/d/1KQdCwZzV88hXMx7AMWgh8izqkldtNv5p/preview" title="Demo zur Hightouch-Integration" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>