---
nav_title: Verfügbare Partner
article_title: Verfügbare Currents-Partner
page_order: 1
page_type: reference
description: "Dieser Referenzartikel beschreibt die Datenpartner, die Sie für die Integration mit Braze-Currents verwenden können, und deren Anwendungsfälle."
tool: Currents
---

# Verfügbare Partner {#available-partners}

> Auf dieser Seite finden Sie eine Liste der Datenpartner, die Sie in Braze-Currents integrieren können, sowie einen Überblick über deren Anwendungsfälle.

{% alert note %}
Die Namenskonventionen für Ereignisse, die für einen Partner aus Braze fließen, stimmen möglicherweise nicht mit denen anderer Partner überein. Zum Beispiel lautet das Currents-Ereignis für E-Mail-Öffnungen in Segment `Email Opened`, während es in Mixpanel `Email Open` heißt.
{% endalert %}

## Data-Warehouse-Speicher {#data-warehouse-storage}
Data-Warehouse-Speicher bieten eine Sammelquelle für alle Informationen, die über Currents gestreamt werden. Diese Partner können entweder als Warehouses (zur Speicherung von Flat Files) dienen oder zur Nutzung von Business-Intelligence-Tools und Algorithmen für maschinelles Lernen eingesetzt werden, um Insights zur Marketing-Performance zu gewinnen und vieles mehr.

* [Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3)
* [Google Cloud Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/google_cloud_storage_for_currents)
* [Microsoft Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents)

Wir sind so überzeugt von der Leistungsfähigkeit von Currents und Data Warehouses im Zusammenspiel, dass [wir sie selbst nutzen]({{site.baseurl}}/user_guide/data/distribution/braze_currents/use_cases/how_braze_uses_currents)!

## Kundendaten {#customer-data}

Diese Customer Data Platforms sammeln und leiten Informationen aus mehreren Quellen an verschiedene Ziele weiter, damit Sie Braze-Daten optimal nutzen können.

* [mParticle]({{site.baseurl}}/partners/mparticle_for_currents)
* [Segment]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/segment/segment_for_currents)
* [Tealium]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/tealium/tealium_for_currents)
* [Treasure Data]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/treasure_data/treasure_data_for_currents)
* [RudderStack]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/rudderstack/rudderstack_for_currents)
* [Adobe]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/adobe/adobe_for_currents)
* [Amperity]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amperity#using-amperity-with-braze-currents)

## Verhaltensanalysen {#behavioral-analytics}

Diese Partner sind auf Produktanalytik und Business-Intelligence spezialisiert und können Ihnen helfen, mit Ihren Nutzer:innen auf Basis ihrer Aktionen zu interagieren.

* [Amplitude]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_for_currents)
* [Mixpanel]({{site.baseurl}}/partners/data_and_analytics/analytics/mixpanel)
* [Heap]({{site.baseurl}}/partners/data_and_analytics/analytics/heap/heap_cohort_import)

## Datentools {#data-tools}

Erstellen Sie Ihre eigene angepasste Integration, indem Sie Currents-Ereignisdaten direkt an einen HTTP-Endpunkt streamen, den Sie besitzen und betreiben.

* [Angepasster HTTP-Konnektor]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/custom_http_connector)