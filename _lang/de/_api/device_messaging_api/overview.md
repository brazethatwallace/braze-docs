---
nav_title: Übersicht
article_title: Übersicht der Device Messaging API
page_order: 0
page_type: reference
description: "Erfahren Sie mehr über die Braze Device Messaging API und ihre Early-Access-Funktionen."
hidden: true
---

# Übersicht der Device Messaging API {#device-messaging-api-overview}

Die Braze Device Messaging API ist eine Reihe von REST-Endpunkten zur Integration von Braze-Messaging-Funktionen ohne ein Braze SDK. Sie können diese Endpunkte von Client- oder Server-Anwendungen aus aufrufen.

{% alert important %}
Diese Seite befindet sich in der Beta-Phase. Features und Dokumentation für die Device Messaging API können sich ändern. Wenden Sie sich an Ihren Braze Account Manager, um Zugang anzufordern.
{% endalert %}

## Unterstützte Funktionen {#supported-capabilities}

Während des Early Access können Sie die Device Messaging API nutzen, um:

- [Berechtigte Banner abzurufen]({{site.baseurl}}/api/device_messaging_api/endpoints/banners/post_sync_banners) für eine externe Nutzer-ID und eine Reihe von Placements
- [Banner-Impression- und Klick-Events zu melden]({{site.baseurl}}/api/device_messaging_api/endpoints/banners/post_track_banner_events)

Die Device Messaging API gibt strukturierte Banner-Eigenschaften zurück, sodass Sie eine angepasste Oberfläche erstellen können. Sie gibt kein gerendertes HTML zurück.

## Integrationsanforderungen {#integration-requirements}

Für die Integration der Device Messaging API benötigen Sie:

- Einen Workspace mit aktivierter Device Messaging API
- Einen clientseitigen REST-API-Schlüssel für diesen Workspace
- Den REST-Endpunkt für diesen Workspace
- Die externe Nutzer-ID für den/die Nutzer:in
- Den API-Bezeichner für die App

Weitere Informationen zu Zugangsdaten finden Sie unter [Authentifizierung und Sicherheit]({{site.baseurl}}/api/device_messaging_api/authentication).

## Anleitung zur Device Messaging API und REST API {#device-messaging-api-and-rest-api-guidance}

Die Device Messaging API verwendet dieselben regionalen REST-Endpunkte wie die Braze REST API, verfügt jedoch über einen separaten Authentifizierungs- und Antwortvertrag. Allgemeine Hinweise zur REST API bezüglich privater serverseitiger Schlüssel, Antwortkörper, Fehler und Rate-Limits gelten nicht, es sei denn, ein Artikel zur Device Messaging API verweist ausdrücklich darauf.

Verwenden Sie die Endpunkt-Dokumentation der Device Messaging API als maßgebliche Quelle für Anfragefelder, Antwortkörper, Statuscodes und Limits.