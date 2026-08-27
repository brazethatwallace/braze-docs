---
nav_title: Device Messaging API
article_title: Device Messaging API
search_tag: Endpoint
page_order: 2.2
layout: dev_guide
permalink: /api/device_messaging_api
description: "Diese Landing-Page stellt die Braze Device Messaging API vor."
page_type: landing
hidden: true
guide_top_header: "Device Messaging API"
guide_top_text: "Verwenden Sie die Braze Device Messaging API, um Banner-Eigenschaften abzurufen und Banner-Impression- und Klick-Ereignisse zu melden, ohne ein Braze SDK zu integrieren. Die Device Messaging API unterstützt client- und serverseitige Integrationen und verwendet clientseitige REST-API-Schlüssel, die auf einen einzelnen Workspace beschränkt sind."
guide_top_text2: "Hinweis: Diese API ruft nur Eigenschaften für ein bestimmtes Banner ab, nicht das Banner-HTML."
guide_featured_title: "Erste Schritte"
guide_featured_list:
  - name: "Device Messaging API – Übersicht"
    link: /docs/api/device_messaging_api/overview
    image: /assets/img/braze_icons/annotation-info.svg
  - name: "Authentifizierung und Sicherheit"
    link: /docs/api/device_messaging_api/authentication
    image: /assets/img/braze_icons/key-01.svg
  - name: "Fehlerbehandlung und Wiederholungsversuche"
    link: /docs/api/device_messaging_api/error_handling
    image: /assets/img/braze_icons/alert-circle.svg
  - name: "Rate-Limits"
    link: /docs/api/device_messaging_api/rate_limits
    image: /assets/img/braze_icons/speedometer-01.svg
guide_menu_title: "Banner-Endpunkte"
guide_menu_list:
  - name: "POST: Banner für eine:n Nutzer:in abrufen"
    link: /docs/api/device_messaging_api/endpoints/banners/post_sync_banners
    image: /assets/img/braze_icons/download-01.svg
  - name: "POST: Banner-Analytics-Ereignisse tracken"
    link: /docs/api/device_messaging_api/endpoints/banners/post_track_banner_events
    image: /assets/img/braze_icons/line-chart-up-02.svg
---

{% alert important %}
Diese Seite befindet sich in der Betaphase. Features und Dokumentation für die Device Messaging API können sich ändern.
{% endalert %}