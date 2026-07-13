---
nav_title: Exportieren
article_title: Endpunkte exportieren
search_tag: Endpoint
page_order: 2
description: "Dieser Referenzartikel erläutert die Braze-Export-Endpunkte, einschließlich Voraussetzungen, exportierbarer Daten, Datenbereitstellung und einer vollständigen Liste der Endpunkte."
page_type: reference
---

# Endpunkte exportieren {#export-endpoints}

Mit dieser Sammlung von Endpunkten können Sie auf verschiedene Details zu Ihren KPIs, App-Sitzungen, Nutzer:innen, Segmenten, Campaigns und Canvases zugreifen und diese exportieren. Stellen Sie sicher, dass Sie Ihre [Braze-Instanz]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints), Ihren [API-Schlüssel]({{site.baseurl}}/api/api_key) und Ihren [API-Bezeichner]({{site.baseurl}}/api/identifier_types) kennen, wenn Sie Ihre Parameter und Anfragen erstellen.

## Voraussetzungen {#prerequisites}

Bevor Sie beginnen, stellen Sie sicher, dass Sie über Folgendes verfügen:

| Anforderung | Beschreibung |
| --- | --- |
| Braze-REST-API-Schlüssel | Ein REST-API-Schlüssel mit den entsprechenden Export-Berechtigungen für die Endpunkte, die Sie aufrufen möchten. API-Schlüssel sind auf bestimmte Endpunkte beschränkt, und Berechtigungen können nach der Erstellung nicht mehr geändert werden. Weitere Informationen finden Sie unter [REST-API-Schlüssel]({{site.baseurl}}/api/basics#about-rest-api-keys). |
| Relevante Bezeichner | Die Bezeichner für die Daten, die Sie exportieren möchten, z. B. eine Campaign-ID, Segment-ID oder Canvas-ID. Diese finden Sie im Braze-Dashboard. Eine vollständige Liste finden Sie unter [API-Bezeichnertypen]({{site.baseurl}}/api/identifier_types). |
| Cloud-Storage-Zugangsdaten (optional) | Wenn Sie große Datensätze exportieren, verbinden Sie einen [Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3)-, [Microsoft Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents)- oder [Google Cloud Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/google_cloud_storage_for_currents)-Bucket, damit Exportdateien direkt in Ihren Speicher geschrieben werden. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

{% alert note %}
Wenn Sie Marketer oder Teammitglied ohne API-Zugang sind, stimmen Sie sich mit einem Entwickler oder Administrator in Ihrer Organisation ab, um API-Schlüssel und Integrationen einzurichten.
{% endalert %}

## Was Sie exportieren können {#what-you-can-export}

Die folgende Tabelle fasst die Datenkategorien zusammen, die über die Export-APIs verfügbar sind.

| Kategorie | Enthaltene Daten | API-Referenz |
| --- | --- | --- |
| Campaigns | Performance-Analytics, Campaign-Details, Campaign-Listen und Versand-Analytics | [Campaign-Endpunkte]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics) |
| Canvases | Datenreihen-Analytics, Analytics-Zusammenfassungen, Canvas-Details und Canvas-Listen | [Canvas-Endpunkte]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics) |
| Segmente | Segment-Listen, Segment-Analytics und Segment-Details | [Segment-Endpunkte]({{site.baseurl}}/api/endpoints/export/segments/get_segment) |
| Nutzerdaten | Vollständige Nutzerprofile nach Bezeichner oder nach Segment sowie Nutzer:innen nach globaler Kontrollgruppe | [Nutzerdaten-Endpunkte]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier) |
| KPIs | Täglich aktive Nutzer:innen, monatlich aktive Nutzer:innen, täglich neue Nutzer:innen und Deinstallationen nach Datum | [KPI-Endpunkte]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_dau_date) |
| Sitzungen | Zeitreihendaten zu App-Sitzungen | [Sitzungen-Endpunkt]({{site.baseurl}}/api/endpoints/export/sessions/get_sessions_analytics) |
| Angepasste Events | Event-Namen, Event-Listen und Event-Analytics im Zeitverlauf | [Endpunkte für angepasste Events]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_data) |
| Angepasste Attribute | Attributnamen | [Endpunkt für angepasste Attribute]({{site.baseurl}}/api/endpoints/export/custom_attributes/get_custom_attributes) |
| Käufe | Umsatzdaten nach Zeit, Produkt-ID-Listen und Kaufanzahlen | [Kauf-Endpunkte]({{site.baseurl}}/api/endpoints/export/purchases/get_revenue_series) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Was Sie exportieren können" }

## Wie Exportdaten bereitgestellt werden {#how-export-data-is-delivered}

API-Exporte geben Daten im JSON-Format zurück, im Gegensatz zu den CSV-Dateien, die Sie vom Dashboard herunterladen. Die Bereitstellungsmethode hängt davon ab, ob Sie Cloud-Storage verbunden haben:

- **Ohne Cloud-Storage:** Braze schreibt die Exportdateien in seinen eigenen S3-Bucket und fügt der API-Antwort eine temporäre Download-URL hinzu. Diese URL läuft nach vier Stunden ab, und der Export wird als komprimiertes Archiv (ZIP oder GZIP, abhängig vom Parameter `output_format`) bereitgestellt, das JSON-Dateien enthält. Jede Zeile in den JSON-Dateien repräsentiert ein Datenobjekt.
- **Mit verbundenem Cloud-Storage:** Braze schreibt die Exportdateien direkt in Ihren konfigurierten Bucket. Die API-Antwort enthält keine Download-URL. Die Dateien unterliegen Ihren eigenen Aufbewahrungsrichtlinien und sind in der Regel zuverlässiger für große Exporte.

{% alert tip %}
„Cloud-Storage“ bezeichnet Ihren eigenen Speicher-Bucket (z. B. Amazon S3, Microsoft Azure Blob Storage oder Google Cloud Storage). Sie können Ihren Bucket unter **Partnerintegrationen** > **Technologie-Partner** verbinden, damit Braze Exportdateien direkt dorthin schreiben kann.
{% endalert %}

Weitere Details zur Exportbereitstellung und Fehlerbehebung finden Sie unter [Export-Fehlerbehebung]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting).

## Export-Endpunkte

Die folgende Tabelle listet alle verfügbaren Export-APIs auf.

| Kategorie | Methode | Endpunkt |
| --- | --- | --- |
| Campaigns | GET | [Campaign-Analytics]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics) |
| Campaigns | GET | [Campaign-Details]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details) |
| Campaigns | GET | [Campaign-Liste]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns) |
| Campaigns | GET | [Versand-Analytics]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics) |
| Canvases | GET | [Canvas-Datenreihen-Analytics]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics) |
| Canvases | GET | [Canvas-Analytics-Zusammenfassung]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary) |
| Canvases | GET | [Canvas-Details]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details) |
| Canvases | GET | [Canvas-Liste]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases) |
| Angepasste Events | GET | [Angepasste Events]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_data) |
| Angepasste Events | GET | [Liste angepasster Events]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events) |
| Angepasste Events | GET | [Analytics angepasster Events]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_analytics) |
| Angepasste Attribute | GET | [Angepasste Attribute]({{site.baseurl}}/api/endpoints/export/custom_attributes/get_custom_attributes) |
| KPIs | GET | [KPIs für täglich neue Nutzer:innen nach Datum]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_daily_new_users_date) |
| KPIs | GET | [KPIs für täglich aktive Nutzer:innen nach Datum]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_dau_date) |
| KPIs | GET | [KPIs für monatlich aktive Nutzer:innen in den letzten 30 Tagen]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_mau_30_days) |
| KPIs | GET | [KPIs für Deinstallationen nach Datum]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_uninstalls_date) |
| Käufe | GET | [Produkt-IDs-Liste]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id) |
| Käufe | GET | [Anzahl der Käufe]({{site.baseurl}}/api/endpoints/export/purchases/get_number_of_purchases) |
| Käufe | GET | [Umsatzdaten nach Zeit]({{site.baseurl}}/api/endpoints/export/purchases/get_revenue_series) |
| Segmente | GET | [Segment-Liste]({{site.baseurl}}/api/endpoints/export/segments/get_segment) |
| Segmente | GET | [Segment-Analytics]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics) |
| Segmente | GET | [Segment-Details]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details) |
| Sitzungen | GET | [App-Sitzungen-Zeitreihendaten]({{site.baseurl}}/api/endpoints/export/sessions/get_sessions_analytics) |
| Nutzerdaten | POST | [Nutzerdaten nach Bezeichner]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier) |
| Nutzerdaten | POST | [Nutzerdaten nach Segment]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment) |
| Nutzerdaten | POST | [Nutzerdaten nach globaler Kontrollgruppe]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Export-Endpunkte" }

## Verwandte Artikel {#related-articles}

Für einmalige Exporte aus dem Dashboard lesen Sie diese Artikel:

- [Campaign-Daten exportieren]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_campaign_results_data)
- [Canvas-Daten exportieren]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_canvas_data)
- [Segment-Daten als CSV exportieren]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/segment_data_to_csv)