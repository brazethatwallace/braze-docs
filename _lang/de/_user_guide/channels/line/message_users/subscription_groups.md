---
nav_title: Abo-Gruppen
article_title: Abo-Gruppen
page_order: 1
description: "Dieser Artikel behandelt Abo-Gruppen für LINE-Nachrichten."
page_type: reference
channel:
 - LINE
alias: /line/subscription_groups/
---

# LINE-Abo-Gruppen {#line-subscription-groups}

> Es gibt zwei Abo-Status für LINE-Nutzer:innen: abonniert und abgemeldet. Jede Abo-Gruppe ist mit einem eigenen LINE-Kanal verbunden. Einen kanalübergreifenden Überblick über Abo-Gruppen finden Sie unter [Abo-Gruppen]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_groups).

| Status | Definition |
| --- | --- |
| Abonniert | Die Nutzer:in ist dem LINE-Kanal innerhalb ihrer LINE-App gefolgt. Nutzer:innen werden automatisch abonniert, wenn sie nach Abschluss der Integrationsschritte folgen. |
| Abgemeldet | Die Nutzer:in ist dem LINE-Kanal innerhalb ihrer LINE-App nicht gefolgt oder hat den LINE-Kanal explizit entfolgt. <br><br> Nutzer:innen, die sich von einer LINE-Abo-Gruppe abmelden, erhalten keine LINE-Nachrichten mehr von Sendekanälen, die zu dieser Abo-Gruppe gehören. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="LINE-Abo-Gruppen" }

## Abo-Gruppe einer Nutzer:in für LINE festlegen {#set-a-users-line-subscription-group}

LINE verwaltet den Abo-Status der Nutzer:innen. Braze verarbeitet die Follow- und Unfollow-Ereignisse, die den Abo-Status aktualisieren.

{% alert important %}
LINE-Abo-Gruppen können nicht zwischen Workspaces verschoben werden. Wenn Sie einen LINE-Kanal in einem anderen Workspace nach dem Archivieren seiner Abo-Gruppe erneut integrieren, erstellt Braze eine neue Abo-Gruppe im Ziel-Workspace – die ursprüngliche verbleibt im ersten Workspace.
{% endalert %}

## Archivierungsverhalten {#archive-behavior}

- **Standardmäßige Archivierung:** Wenn Sie eine LINE-Abo-Gruppe archivieren und den Kanal nicht in einem anderen Workspace erneut integrieren, können Sie die Abo-Gruppe später wieder aus dem Archiv holen.
- **Permanente Archivierung:** Wenn Sie den LINE-Kanal nach der Archivierung seiner Abo-Gruppe in einem anderen Workspace erneut integrieren, wird die ursprüngliche Abo-Gruppe dauerhaft archiviert und kann nicht über das Dashboard wiederhergestellt werden.

Informationen zu den Schritten für die erneute Kanalintegration finden Sie unter [LINE-Einrichtung]({{site.baseurl}}/user_guide/channels/line/line_setup#re-integrate-a-line-channel-in-another-workspace).