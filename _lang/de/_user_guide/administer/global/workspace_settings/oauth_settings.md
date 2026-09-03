---
nav_title: OAuth und MCP-Zugriff
article_title: OAuth und MCP-Zugriff in einem Workspace
page_order: 10
page_type: reference
description: "Erfahren Sie, welchen OAuth- und MCP-Zugriff Sie pro Workspace steuern können und was unternehmensweit in den Administratoreinstellungen konfiguriert wird."
---

# OAuth und MCP-Zugriff in einem Workspace {#oauth-and-mcp-access-in-a-workspace}

> Die unternehmensweite OAuth-Richtlinie wird in den [Administratoreinstellungen]({{site.baseurl}}/user_guide/administer/global/admin_settings/oauth_admin) konfiguriert. In einem Workspace erteilen Sie einzelnen Nutzer:innen die Berechtigung, den MCP-Server zu verwenden.

Sie können den MCP-OAuth-Zugriff nicht für einen einzelnen Workspace aktivieren oder deaktivieren.

## Unternehmensweit vs. pro Workspace {#whats-company-wide-versus-per-workspace}

| Steuerung | Unternehmensweit | Pro Workspace |
| --- | --- | --- |
| **MCP-OAuth-Zugriff** | Ja. Dieser Schalter befindet sich unter **Einstellungen** > **Administratoreinstellungen** > **OAuth** im Abschnitt **Globale Zugriffskontrollen**. | Nein. Workspace-Administratoren können die Unternehmenseinstellung nicht überschreiben. |
| Berechtigung „Use MCP Server“ | Nein. | Ja. Erteilen Sie diese Berechtigung für jeden Workspace, auf den die Nutzer:innen über den MCP-Server zugreifen sollen. |
| Dashboard-Berechtigungen, die vom MCP gespiegelt werden | Nein. | Ja. Der MCP-Client kann nur die Braze-Features nutzen, auf die die Nutzer:innen in diesem Workspace bereits Zugriff haben. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Unternehmensweite vs. Workspace-spezifische OAuth-Steuerungen" }

## Wenn der MCP-OAuth-Zugriff für das Unternehmen deaktiviert ist {#if-mcp-oauth-access-is-off-for-the-company}

Wenn **MCP-OAuth-Zugriff** in den **Administratoreinstellungen** deaktiviert ist, verweigert Braze MCP-OAuth für jeden Workspace. Nutzer:innen mit der Berechtigung „Use MCP Server“ können sich trotzdem nicht verbinden, und es gibt keine Workspace-Einstellung, um den MCP-OAuth-Zugriff wieder zu aktivieren.

Nutzer:innen, die versuchen, eine Verbindung herzustellen, sehen möglicherweise eine Nachricht, dass der Remote-MCP-Zugriff für das Unternehmen nicht aktiviert wurde. Ein Unternehmensadministrator kann **MCP-OAuth-Zugriff** unter **Einstellungen** > **Administratoreinstellungen** > **OAuth** aktivieren.

Informationen zum unternehmensweiten MCP-OAuth-Zugriff und dazu, wer diese Einstellung ändern kann, finden Sie unter [OAuth-Einstellungen verwalten]({{site.baseurl}}/user_guide/administer/global/admin_settings/oauth_admin).