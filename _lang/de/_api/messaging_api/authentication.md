---
nav_title: Authentifizierung und Sicherheit
article_title: Authentifizierung und Sicherheit der Device Messaging API
permalink: /api/device_messaging_api/authentication
page_order: 1
page_type: reference
description: "Erfahren Sie, wie Sie Anfragen an die Device Messaging API sicher authentifizieren."
hidden: true
---

# Authentifizierung und Sicherheit der Device Messaging API {#device-messaging-api-authentication-and-security}

{% alert important %}
Diese Seite befindet sich in der Betaphase. Features und Dokumentation für die Device Messaging API können sich ändern.
{% endalert %}

Die Device Messaging API verwendet clientseitige REST-API-Schlüssel. Diese Schlüssel unterscheiden sich von den privaten REST-API-Schlüsseln, die für serverseitige Braze-REST-API-Anfragen verwendet werden.

## Clientseitige REST-API-Schlüssel {#client-side-rest-api-keys}

Clientseitige REST-API-Schlüssel sind auf einen Workspace beschränkt und auf Berechtigungen der Device Messaging API eingeschränkt. Sie können diese Schlüssel in Client-Anwendungen einbetten.

{% alert important %}
Verwenden Sie in einer Client-Anwendung ausschließlich einen clientseitigen REST-API-Schlüssel. Geben Sie niemals einen privaten serverseitigen REST-API-Schlüssel in clientseitigem Code preis.
{% endalert %}

So erstellen Sie einen clientseitigen REST-API-Schlüssel:

1. Gehen Sie im Braze-Dashboard zu **Einstellungen** > **APIs und Bezeichner** > **API-Schlüssel**.
2. Wählen Sie **API-Schlüssel erstellen** aus.
3. Wählen Sie unter **Schlüsseltyp** die Option **Client** aus.
4. Weisen Sie die Berechtigung `banners.sync` zum Abrufen von Bannern, die Berechtigung `banners.track` zum Melden von Banner-Events oder beide zu.

## Anfragen authentifizieren {#authenticating-requests}

Senden Sie den clientseitigen REST-API-Schlüssel als Bearer-Token im `Authorization`-Header:

```bash
Authorization: Bearer {YOUR_CLIENT_SIDE_REST_API_KEY}
```

Verwenden Sie HTTPS und den [REST-Endpunkt]({{site.baseurl}}/api/basics#endpoints) für Ihre Braze-Instanz.

## Nutzer:innen-Identität {#user-identity}

Ein clientseitiger REST-API-Schlüssel authentifiziert die aufrufende App und den Workspace, nicht die Nutzer:innen. Die `external_user_id` in einer Anfrage identifiziert die Nutzer:innen, die mit Banner-Inhalten und -Events verknüpft sind.

Wenden Sie die Autorisierungskontrollen Ihrer App an, bevor Sie Anfragen an die Device Messaging API stellen.

## Authentifizierungsfehler {#authentication-errors}

Authentifizierungs- und Berechtigungsfehler können je nach Endpunkt variieren. Informationen dazu finden Sie in der Statuscode-Tabelle des jeweiligen Endpunkts und unter [Fehlerbehandlung der Device Messaging API]({{site.baseurl}}/api/device_messaging_api/error_handling).