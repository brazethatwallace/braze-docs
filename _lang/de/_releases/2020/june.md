---
nav_title: Juni
page_order: 7
noindex: true
page_type: update
description: "Dieser Artikel enthält Versionshinweise für Juni 2020."
---
# Juni 2020 {#june-2020}

## Bindungsberichte {#retention-reports}

Bindungsberichte bieten jetzt eine Bereichsbindung für [Campaigns]({{site.baseurl}}/user_guide/messaging/campaigns/test_campaigns/retention_reports/) und [Canvase]({{site.baseurl}}/user_guide/analytics/reports/retention_reports/). Die Bereichsbindung misst, wie viele Nutzer:innen in bestimmten Zeitintervallen zurückkommen und ein ausgewähltes Bindungs-Event durchführen.

## Nutzer:innen tracken – API-Updates {#user-track-api-updates}

Der [Endpunkt `users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) hat jetzt eine Standardrate von 50.000 API-Anfragen pro Minute für Dashboard-Unternehmen, die nach dem 2. Juni 2020 erstellt wurden. Bestehende Unternehmen, die vor diesem Datum erstellt wurden, und ihre Workspaces sind weiterhin zu unbegrenzten API-Anfragen an den Endpunkt `users/track` berechtigt.

 Braze setzt diesen Standard für unseren am meisten genutzten kundenorientierten Endpunkt ein, um unsere Ziele in Bezug auf Stabilität und Zuverlässigkeit unserer API und Infrastruktur zu erreichen. Das Limit ist sehr großzügig bemessen und wird nur sehr wenige Dashboard-Unternehmen und deren regulären Betrieb betreffen. Sollten Sie eine Erhöhung dieses Limits benötigen, wenden Sie sich an Ihren CSM or Customer-Success-Manager or Customer-Success-Manager:in oder unser Support-Team, um eine Erhöhung anzufordern.