---
nav_title: Übersicht
article_title: Übersicht der Messaging API
page_order: 0
page_type: reference
description: "Erfahren Sie mehr über die Braze Messaging API und ihre Early-Access-Funktionen."
hidden: true
---

# Übersicht der Messaging API {#messaging-api-overview}

Die Braze Messaging API ist eine Reihe von REST-Endpunkten zur Integration von Braze-Messaging-Funktionen ohne ein Braze SDK. Sie können diese Endpunkte von Client- oder Server-Anwendungen aus aufrufen.

{% alert important %}
Diese Seite befindet sich in der Beta-Phase. Features und Dokumentation für die Messaging API können sich ändern. Wenden Sie sich an Ihren Braze Account Manager, um Zugang anzufordern.
{% endalert %}

## Unterstützte Funktionen {#supported-capabilities}

Während des Early Access können Sie die Messaging API verwenden, um:

- [Berechtigte Banner abzurufen]({{site.baseurl}}/api/messaging_api/endpoints/banners/post_sync_banners) für eine externe Nutzer-ID und eine Reihe von Placements
- [Banner-Impression- und Klick-Ereignisse zu melden]({{site.baseurl}}/api/messaging_api/endpoints/banners/post_track_banner_events)

Die Messaging API gibt strukturierte Banner-Eigenschaften zurück, damit Sie eine angepasste Oberfläche erstellen können. Sie gibt kein gerendertes HTML zurück.

## Integrationsanforderungen {#integration-requirements}

Um die Messaging API zu integrieren, benötigen Sie:

- Einen Workspace mit aktivierter Messaging API
- Einen clientseitigen REST-API-Schlüssel für diesen Workspace
- Den REST-Endpunkt für diesen Workspace
- Die externe Nutzer-ID für den/die Nutzer:in
- Den API-Bezeichner für die App

Weitere Informationen zu Zugangsdaten finden Sie unter [Authentifizierung und Sicherheit]({{site.baseurl}}/api/messaging_api/authentication).

## Hinweise zur Messaging API und REST API {#messaging-api-and-rest-api-guidance}

Die Messaging API verwendet dieselben regionalen REST-Endpunkte wie die Braze REST API, verfügt jedoch über einen separaten Authentifizierungs- und Antwortvertrag. Allgemeine REST-API-Hinweise zu privaten serverseitigen Schlüsseln, Antwortkörpern, Fehlern und Rate-Limits gelten nicht, es sei denn, ein Messaging-API-Artikel verweist ausdrücklich darauf.

Verwenden Sie die Endpunkt-Dokumentation der Messaging API als maßgebliche Quelle für Anfragefelder, Antwortkörper, Statuscodes und Limits.