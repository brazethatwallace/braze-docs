---
nav_title: Braze Go
permalink: "/braze_go/"
hidden: true
noindex: true
hide_toc: true
---

# Braze Go

> Braze Go bietet einen optimierten Zugang zur Braze Customer-Engagement-Plattform, damit Ihre Marketing-Teams überall starten und überallhin gelangen können. Braze Go wurde für Einfachheit und Effizienz entwickelt und ist auf ausgewählte aufstrebende Märkte zugeschnitten.

{% alert important %}
Braze Go ist nicht in allen Märkten verfügbar. Wenn Sie mehr über Braze Go erfahren möchten, kontaktieren Sie Ihren Account Manager.
{% endalert %}

Braze Go bietet die gleiche Funktionalität wie Braze, mit gezielten Änderungen an den folgenden Features:

- Sie können bis zu 30 aktive Campaigns haben.
- Sie können bis zu 20 aktive Canvases haben.
- Das gesamte Standard-Rate-Limit der REST API beträgt 50.000 pro Stunde und Workspace.
    - Für die Nutzung ohne Braze Go erfahren Sie mehr über [REST-API-Limits]({{site.baseurl}}/api/api_limits#rate-limits-by-request-type).
- Die Aufbewahrungsdauer für Interaktionsdaten von Campaigns und Canvases beträgt 2 Monate ohne Wiederherstellung.
    - Für die Nutzung ohne Braze Go erfahren Sie mehr über die [Verfügbarkeit von Messaging-Interaktionsdaten]({{site.baseurl}}/messaging_interaction_data).

{% alert note %}
Interaktionsdaten für Campaigns und Canvases unterscheiden sich von Snowflake-Daten und haben keinerlei Auswirkungen darauf.
{% endalert %}

- Braze-zu-Braze-Webhooks werden nicht unterstützt.
- Filter in Bezug auf Tags werden nicht unterstützt, insbesondere die folgenden Filter:
    - Clicked or Opened Campaign or Canvas with Tag
    - Last Received Message from Campaign or Canvas with Tag
    - Received Campaign or Canvas with Tag
- Braze kann außerdem eine Datenaufbewahrungsrichtlinie für Nutzerprofil-Ereignisse und Kaufdaten implementieren, die Ereignisse, Käufe oder beides entfernt, die älter als 1 Jahr sind und innerhalb von 1 Jahr nicht erneut durchgeführt wurden. Diese Daten wären jedoch weiterhin für 2 Jahre in SQL-Segmenterweiterungen verfügbar.

Wenn eine in diesem Artikel beschriebene Funktionalität aktualisiert wird, wird dies in diesem Artikel berücksichtigt und in unseren [Release Notes]({{site.baseurl}}/help/release_notes#most-recent-braze-release-notes) vermerkt.