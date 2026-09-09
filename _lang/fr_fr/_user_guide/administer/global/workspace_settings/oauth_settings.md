---
nav_title: Accès OAuth et MCP
article_title: Accès OAuth et MCP dans un espace de travail
page_order: 10
page_type: reference
description: "Découvrez les contrôles d'accès OAuth et MCP que vous pouvez gérer par espace de travail, et ceux qui restent à l'échelle de l'entreprise dans les paramètres d'administration."
---

# Accès OAuth et MCP dans un espace de travail {#oauth-and-mcp-access-in-a-workspace}

> La politique OAuth à l'échelle de l'entreprise est configurée dans les [paramètres d'administration]({{site.baseurl}}/user_guide/administer/global/admin_settings/oauth_admin). Dans un espace de travail, vous accordez à chaque utilisateur l'autorisation d'utiliser le serveur MCP.

Vous ne pouvez pas activer ou désactiver l'accès MCP OAuth pour un seul espace de travail.

## Ce qui est à l'échelle de l'entreprise et ce qui est par espace de travail {#whats-company-wide-versus-per-workspace}

| Contrôle | À l'échelle de l'entreprise | Par espace de travail |
| --- | --- | --- |
| **Accès MCP OAuth** | Oui. Cette option se trouve dans **Paramètres** > **Paramètres d'administration** > **OAuth** sous **Contrôles d'accès globaux**. | Non. Les administrateurs d'espace de travail ne peuvent pas remplacer le paramètre de l'entreprise. |
| Autorisation « Use MCP Server » | Non. | Oui. Accordez cette autorisation pour chaque espace de travail auquel l'utilisateur doit accéder via le serveur MCP. |
| Autorisations du tableau de bord reflétées par MCP | Non. | Oui. Le client MCP ne peut utiliser que les fonctionnalités de Braze auxquelles l'utilisateur a déjà accès dans cet espace de travail. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Contrôles OAuth à l'échelle de l'entreprise et par espace de travail" }

## Si l'accès MCP OAuth est désactivé pour l'entreprise {#if-mcp-oauth-access-is-off-for-the-company}

Lorsque l'**accès MCP OAuth** est désactivé dans les **paramètres d'administration**, Braze refuse l'authentification MCP OAuth pour tous les espaces de travail. Les utilisateurs disposant de l'autorisation « Use MCP Server » ne peuvent toujours pas se connecter, et il n'existe aucun paramètre au niveau de l'espace de travail pour réactiver l'accès MCP OAuth.

Les utilisateurs qui tentent de se connecter peuvent voir un message indiquant que l'accès MCP à distance n'a pas été activé pour l'entreprise. Un administrateur de l'entreprise peut activer l'**accès MCP OAuth** dans **Paramètres** > **Paramètres d'administration** > **OAuth**.

Pour en savoir plus sur l'accès MCP OAuth au niveau de l'entreprise et sur les personnes autorisées à modifier ce paramètre, consultez [Gérer les paramètres OAuth]({{site.baseurl}}/user_guide/administer/global/admin_settings/oauth_admin).