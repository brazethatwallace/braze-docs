---
nav_title: OAuth-Einstellungen
article_title: OAuth-Einstellungen verwalten
page_order: 4
page_type: reference
description: "Erfahren Sie, wie Sie den MCP-OAuth-Zugriff für den Braze-MCP-Server verwalten."
---

# OAuth-Einstellungen verwalten {#manage-oauth-settings}

> OAuth-Einstellungen steuern den unternehmensweiten Zugriff auf den [Braze-MCP-Server]({{site.baseurl}}/user_guide/brazeai/mcp_server).

OAuth-Einstellungen gelten für Ihr gesamtes Unternehmen. Die den einzelnen Nutzer:innen zugewiesenen Berechtigungen bestimmen, auf welche Workspaces und Features sie über den MCP-Server zugreifen können.

## Voraussetzungen {#requirements}

| Voraussetzung | Beschreibung |
| --- | --- |
| Berechtigung „Admin“ | Sie benötigen die unternehmensweite Berechtigung „Admin“, um OAuth-Einstellungen anzuzeigen oder den MCP-OAuth-Zugriff ein- oder auszuschalten. |
| Berechtigung „Use MCP Server“ | Nutzer:innen benötigen diese Berechtigung für jeden Workspace, auf den sie über den MCP-Server zugreifen möchten. Diese Berechtigung ist unabhängig von der Berechtigung „Admin“, die zur Verwaltung der OAuth-Einstellungen verwendet wird. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen für die Verwaltung von OAuth-Einstellungen" }

Weitere Informationen zum Zuweisen von Berechtigungen finden Sie unter [Nutzer:innenberechtigungen]({{site.baseurl}}/user_guide/administer/global/user_management/permissions).

## Funktionsweise des OAuth-Zugriffs {#how-oauth-access-works}

OAuth-Einstellungen und Nutzer:innenberechtigungen wirken zusammen:

- Unternehmensweite OAuth-Einstellungen legen fest, ob Nutzer:innen MCP-Clients mit Braze verbinden können.
- Die Berechtigung „Use MCP Server“ bestimmt, ob einzelne Nutzer:innen den MCP-Server in einem Workspace verwenden können.
- Die vorhandenen Dashboard-Berechtigungen der Nutzer:innen bestimmen, auf welche Braze-Daten und -Features ein MCP-Client zugreifen kann.
- Eine OAuth-Verbindung kann nur auf die Workspaces zugreifen, für die die jeweiligen Nutzer:innen autorisiert sind.

Das Aktivieren des MCP-OAuth-Zugriffs gewährt Nutzer:innen keine neuen Workspace-Berechtigungen. Ebenso wird durch das Entfernen einer Dashboard-Berechtigung diese Funktion auch vom verbundenen MCP-Client der Nutzer:innen entfernt.

## Unternehmens- und Workspace-Steuerung {#company-and-workspace-controls}

Die OAuth-Richtlinie wird auf Unternehmensebene gespeichert. Workspace-Admins können **MCP-OAuth-Zugriff** nicht für einen einzelnen Workspace überschreiben.

| Steuerung | Konfigurationsort | Geltungsbereich |
| --- | --- | --- |
| **MCP-OAuth-Zugriff** | **Einstellungen** > **Admin-Einstellungen** > **OAuth** | Gesamtes Unternehmen. Wenn dies deaktiviert ist, wird MCP-OAuth in jedem Workspace verweigert. |
| Berechtigung „Use MCP Server“ | **Einstellungen** > **Nutzer:innenverwaltung** | Pro Workspace. Nutzer:innen benötigen diese Berechtigung in jedem Workspace, auf den sie über den MCP-Server zugreifen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Unternehmens- und Workspace-OAuth-Steuerungen" }

Nur Nutzer:innen mit der Berechtigung „Admin“ können den **MCP-OAuth-Zugriff** ändern. Informationen dazu, wie Workspace-Berechtigungen mit dieser Unternehmenseinstellung interagieren, finden Sie unter [OAuth und MCP-Zugriff]({{site.baseurl}}/user_guide/administer/global/workspace_settings/oauth_settings).

## MCP-OAuth-Zugriff ein- oder ausschalten {#turn-mcp-oauth-access-on-or-off}

So Update or aktualisieren or aktualisieren Sie den MCP-OAuth-Zugriff für Ihr Unternehmen:

1. Gehen Sie zu **Einstellungen** > **Admin-Einstellungen** > **OAuth**.
2. Schalten Sie unter **Globale Zugriffssteuerungen** den **MCP-OAuth-Zugriff** ein oder aus.

Wenn der **MCP-OAuth-Zugriff** aktiviert ist, können Nutzer:innen mit der Berechtigung „Use MCP Server“ genehmigte MCP-Clients autorisieren.

Wenn er deaktiviert ist, wird der OAuth-Zugriff auf den MCP-Server für alle Nutzer:innen und Workspaces in Ihrem Unternehmen verweigert. Bestehende MCP-Verbindungen funktionieren nicht mehr, sobald sie ihr OAuth-Zugriffstoken das nächste Mal verwenden oder Update or aktualisieren or aktualisieren.

Wenn Braze den Remote-MCP-Server für Ihre Umgebung deaktiviert hat, ist der Schalter **MCP-OAuth-Zugriff** deaktiviert und eine Meldung erklärt, dass die Unternehmenseinstellung keine Wirkung hat, bis der Remote-MCP-Server wieder aktiviert wird.

## OAuth-Aktivität überwachen {#audit-oauth-activity}

Braze zeichnet OAuth-Verbindungen zum MCP-Server im [Sicherheitsereignisbericht]({{site.baseurl}}/user_guide/administer/global/admin_settings/security_settings#security-event-report) auf. Verwenden Sie diesen Bericht, um zu prüfen, wann sich Nutzer:innen über OAuth verbinden.

Um den MCP-Zugriff einzelner Nutzer:innen zu widerrufen, entfernen Sie die Berechtigung „Use MCP Server“ für diese Nutzer:innen. Hinweise zur Einrichtung und Fehlerbehebung finden Sie unter [Braze-MCP-Server einrichten]({{site.baseurl}}/user_guide/brazeai/mcp_server/setup).