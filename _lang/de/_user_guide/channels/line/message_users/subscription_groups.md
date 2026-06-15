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

> Es gibt zwei Abo-Status für LINE-Nutzer:innen: abonniert und abgemeldet. LINE kann bis zu 100 Abo-Gruppen pro Workspace haben, wobei jede Abo-Gruppe mit einem eigenen LINE-Kanal verbunden ist.

| Status | Definition |
| --- | --- |
| Abonniert | Die Nutzer:in ist dem LINE-Kanal innerhalb ihrer LINE-App gefolgt. Nutzer:innen werden automatisch abonniert, wenn sie nach Abschluss der Integrationsschritte folgen. |
| Abgemeldet | Die Nutzer:in ist dem LINE-Kanal innerhalb ihrer LINE-App nicht gefolgt, oder hat den LINE-Kanal explizit entfolgt. <br><br> Nutzer:innen, die sich von einer LINE-Abo-Gruppe abmelden, erhalten keine LINE-Nachrichten mehr von Sendekanälen, die zu dieser Abo-Gruppe gehören. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="LINE subscription groups" }

## LINE-Abo-Gruppe von Nutzer:innen festlegen {#setting-a-users-line-subscription-group}

LINE hostet den Abo-Status der Nutzer:innen. Braze verarbeitet die Follow- und Unfollow-Ereignisse, die den Abo-Status aktualisieren.