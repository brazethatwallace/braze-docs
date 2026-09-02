---
nav_title: Paramètres OAuth
article_title: Gérer les paramètres OAuth
page_order: 4
page_type: reference
description: "Découvrez comment gérer l'accès OAuth MCP pour le serveur MCP de Braze."
---

# Gérer les paramètres OAuth {#manage-oauth-settings}

> Les paramètres OAuth gèrent l'accès à l'échelle de l'entreprise au [serveur MCP de Braze]({{site.baseurl}}/user_guide/brazeai/mcp_server).

Les paramètres OAuth s'appliquent à l'ensemble de votre entreprise. Les permissions attribuées à chaque utilisateur déterminent les espaces de travail et les fonctionnalités auxquels ils peuvent accéder via le serveur MCP.

## Conditions requises {#requirements}

| Condition | Description |
| --- | --- |
| Permission « Admin » | Vous devez disposer de la permission « Admin » au niveau de l'entreprise pour consulter les paramètres OAuth ou activer/désactiver l'accès OAuth MCP. |
| Permission « Use MCP Server » | Les utilisateurs doivent disposer de cette permission pour chaque espace de travail auquel ils souhaitent accéder via le serveur MCP. Cette permission est distincte de la permission « Admin » utilisée pour gérer les paramètres OAuth. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions requises pour gérer les paramètres OAuth" }

Pour plus d'informations sur l'attribution des permissions, consultez [Permissions utilisateur]({{site.baseurl}}/user_guide/administer/global/user_management/permissions).

## Fonctionnement de l'accès OAuth {#how-oauth-access-works}

Les paramètres OAuth et les permissions utilisateur fonctionnent ensemble :

- Les paramètres OAuth à l'échelle de l'entreprise déterminent si les utilisateurs peuvent connecter des clients MCP à Braze.
- La permission « Use MCP Server » détermine si un utilisateur individuel peut utiliser le serveur MCP dans un espace de travail.
- Les permissions existantes du tableau de bord de l'utilisateur déterminent les données et fonctionnalités de Braze auxquelles un client MCP peut accéder.
- Une connexion OAuth ne peut accéder qu'aux espaces de travail auxquels l'utilisateur est autorisé à accéder.

L'activation de l'accès OAuth MCP n'accorde pas de nouvelles permissions d'espace de travail aux utilisateurs. De même, la suppression d'une permission du tableau de bord retire cette capacité du client MCP connecté de l'utilisateur.

## Contrôles au niveau de l'entreprise et de l'espace de travail {#company-and-workspace-controls}

La politique OAuth est stockée au niveau de l'entreprise. Les administrateurs d'espace de travail ne peuvent pas remplacer l'**accès OAuth MCP** pour un seul espace de travail.

| Contrôle | Où le configurer | Portée |
| --- | --- | --- |
| **Accès OAuth MCP** | **Paramètres** > **Paramètres d'administration** > **OAuth** | Entreprise entière. Lorsque ce paramètre est désactivé, l'accès OAuth MCP est refusé dans tous les espaces de travail. |
| Permission « Use MCP Server » | **Paramètres** > **Gestion des utilisateurs** | Par espace de travail. Les utilisateurs ont besoin de cette permission dans chaque espace de travail auquel ils accèdent via le serveur MCP. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Contrôles OAuth au niveau de l'entreprise et de l'espace de travail" }

Seuls les utilisateurs disposant de la permission « Admin » peuvent modifier l'**accès OAuth MCP**. Pour comprendre comment les permissions d'espace de travail interagissent avec ce paramètre d'entreprise, consultez [OAuth et accès MCP]({{site.baseurl}}/user_guide/administer/global/workspace_settings/oauth_settings).

## Activer ou désactiver l'accès OAuth MCP {#turn-mcp-oauth-access-on-or-off}

Pour mettre à jour l'accès OAuth MCP de votre entreprise :

1. Accédez à **Paramètres** > **Paramètres d'administration** > **OAuth**.
2. Dans **Contrôles d'accès globaux**, activez ou désactivez l'**accès OAuth MCP**.

Lorsque l'**accès OAuth MCP** est activé, les utilisateurs disposant de la permission « Use MCP Server » peuvent autoriser les clients MCP approuvés.

Lorsqu'il est désactivé, l'accès OAuth au serveur MCP est refusé pour tous les utilisateurs et espaces de travail de votre entreprise. Les connexions MCP existantes cessent de fonctionner la prochaine fois qu'elles utilisent ou actualisent leur jeton d'accès OAuth.

Si Braze a désactivé le serveur MCP distant pour votre environnement, le basculeur **Accès OAuth MCP** est désactivé et un message explique que le paramètre d'entreprise n'a aucun effet tant que le serveur MCP distant n'est pas réactivé.

## Auditer l'activité OAuth {#audit-oauth-activity}

Braze enregistre les connexions OAuth au serveur MCP dans le [rapport d'événements de sécurité]({{site.baseurl}}/user_guide/administer/global/admin_settings/security_settings#security-event-report). Utilisez ce rapport pour auditer les connexions des utilisateurs via OAuth.

Pour révoquer l'accès MCP d'un utilisateur, supprimez la permission « Use MCP Server » de cet utilisateur. Pour des conseils de configuration et de résolution des problèmes, consultez [Configurer le serveur MCP de Braze]({{site.baseurl}}/user_guide/brazeai/mcp_server/setup).