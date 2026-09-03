# Utilisation du serveur Braze MCP {#using-the-braze-mcp-server}

> Découvrez comment interagir avec vos données Braze en langage naturel après vous être connecté au serveur Braze MCP distant. Pour plus d'informations, consultez [Serveur Braze MCP]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/){% endif %}.

{% multi_lang_include mcp_server/beta_alert.md %}

## Prérequis {#prerequisites}

Avant de pouvoir utiliser cette fonctionnalité, vous devrez [configurer le serveur Braze MCP]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}.

## Bonnes pratiques {#best-practices}

Lorsque vous utilisez le serveur Braze MCP via des outils de langage naturel, gardez ces conseils à l'esprit :

- Confirmez l'espace de travail dans votre prompt, surtout si vous avez accès à plusieurs espaces de travail.
- Soyez précis concernant les plages de dates et les indicateurs lorsque vous demandez des analyses.
- Demandez à l'agent de confirmer quels outils il a utilisés lors de la validation des résultats.
- Comparez les recommandations à fort impact avec les données sources dans le tableau de bord de Braze.

## Exemples d'utilisation {#usage-examples}

Après avoir [configuré le serveur Braze MCP]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}, vous pouvez interagir avec Braze en langage naturel. Voici quelques exemples pour commencer.

### Quels espaces de travail puis-je consulter ? {#which-workspaces-can-i-access}

{% tabs %}
{% tab Exemple de prompt %}

`Show my available Braze workspaces and tell me which one to use for production campaign analytics.`
{% endtab %}
{% tab Exemple de réponse %}

J'ai appelé `get_workspaces` et trouvé les espaces de travail suivants :

- `Marketing - Production` (`app_group_id` : `YOUR-APP-GROUP-ID-1`)
- `Marketing - Staging` (`app_group_id` : `YOUR-APP-GROUP-ID-2`)

Utilisez `Marketing - Production` pour les prompts d'analyse de Campaigns en production.
{% endtab %}
{% endtabs %}

Pour en savoir plus, consultez [Fonctions API disponibles]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#workspaces){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#workspaces){% endif %}.

### Afficher les performances des Campaigns de la semaine dernière {#show-me-campaign-performance-for-last-week}

{% tabs %}
{% tab Exemple de prompt %}

`In the Marketing - Production workspace, show campaign performance for the last seven days, including sends, opens, clicks, and top performers.`
{% endtab %}
{% tab Exemple de réponse %}

J'ai utilisé `get_campaign_list` et `get_campaign_dataseries` pour l'espace de travail et la plage de dates demandés.

Résumé :

- Total d'envois : `YOUR-TEST-SENDS`
- Total d'ouvertures : `YOUR-TEST-OPENS`
- Total de clics : `YOUR-TEST-CLICKS`
- Meilleure Campaign par ouvertures : `YOUR-TEST-CAMPAIGN-NAME`

Je peux détailler ces résultats par Campaign, par canal ou par jour si nécessaire.
{% endtab %}
{% endtabs %}

Pour en savoir plus, consultez [Fonctions API disponibles]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#campaigns){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#campaigns){% endif %}.

### Créer un modèle d'e-mail {#create-an-email-template}

{% tabs %}
{% tab Exemple de prompt %}

`In the Marketing - Production workspace, create an onboarding email template named "YOUR-TEST-TEMPLATE-NAME".`
{% endtab %}
{% tab Exemple de réponse %}

J'ai utilisé `create_email_template` et créé votre modèle.

- **ID du modèle :** `YOUR-TEST-TEMPLATE-ID-123`
- **Nom du modèle :** `YOUR-TEST-TEMPLATE-NAME`
- **Espace de travail :** `Marketing - Production`
{% endtab %}
{% endtabs %}

Pour en savoir plus, consultez [Fonctions API disponibles]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#templates){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#templates){% endif %}.

## Exemples de flux de travail {#example-workflows}

Ces exemples combinent plusieurs outils pour accomplir une tâche du début à la fin.

### Rapport sur plusieurs espaces de travail {#report-across-multiple-workspaces}

{% tabs %}
{% tab Exemple de prompt %}

`Get me an analytics report for the past week from my US Prod workspace and my EU Prod workspace, and compare total sends and open rates.`
{% endtab %}
{% tab Exemple de réponse %}

J'ai appelé `get_workspaces` pour confirmer l'accès, puis exécuté `get_campaign_dataseries` pour chaque espace de travail sur les sept derniers jours.

- `US Prod` : `YOUR-TEST-SENDS` envois, `YOUR-TEST-OPEN-RATE` taux d'ouverture
- `EU Prod` : `YOUR-TEST-SENDS` envois, `YOUR-TEST-OPEN-RATE` taux d'ouverture

`US Prod` a envoyé plus de messages cette semaine, tandis que `EU Prod` a obtenu le meilleur taux d'ouverture. Je peux détailler chaque espace de travail par Campaign ou par canal.
{% endtab %}
{% endtabs %}

### Copier des modèles de staging vers la production {#copy-templates-from-staging-to-production}

{% tabs %}
{% tab Exemple de prompt %}

`Copy the email templates from my Staging workspace to my Production workspace.`
{% endtab %}
{% tab Exemple de réponse %}

J'ai utilisé `get_email_templates` et `get_email_template_info` pour lire les modèles dans `Staging`, puis `create_email_template` pour recréer chacun d'entre eux dans `Production`.

- `YOUR-TEST-TEMPLATE-NAME-1` : créé dans `Production` (`YOUR-TEST-TEMPLATE-ID-1`)
- `YOUR-TEST-TEMPLATE-NAME-2` : créé dans `Production` (`YOUR-TEST-TEMPLATE-ID-2`)

J'ai ignoré les modèles de l'éditeur par glisser-déposer, que `get_email_template_info` ne prend pas en charge. Dites-moi si vous souhaitez que je passe en revue les modèles copiés.
{% endtab %}
{% endtabs %}

### Résumé hebdomadaire de la santé des Campaigns {#summarize-weekly-campaign-health}

{% tabs %}
{% tab Exemple de prompt %}

`Give me a weekly campaign health summary for the Production workspace.`
{% endtab %}
{% tab Exemple de réponse %}

J'ai utilisé `get_campaign_list` et `get_campaign_dataseries` pour récupérer les sept derniers jours d'activité dans `Production`.

- Total des envois : `YOUR-TEST-SENDS`
- Taux d'ouverture : `YOUR-TEST-OPEN-RATE`
- Taux de clics : `YOUR-TEST-CLICK-RATE`
- Campaign avec le plus de conversions : `YOUR-TEST-CAMPAIGN-NAME`

Les envois ont augmenté d'une semaine à l'autre. Je peux ajouter une ventilation par canal ou signaler les Campaigns dont l'engagement est en baisse.
{% endtab %}
{% endtabs %}

## Fonctionnement du serveur MCP distant {#how-the-remote-mcp-server-works}

Lorsque vous envoyez une requête, plusieurs étapes se déroulent en arrière-plan :

1. **Vous formulez votre demande dans le client.** Vous saisissez une requête en langage naturel, par exemple en demandant les performances des Campaigns de la semaine dernière.
2. **Le modèle du client sélectionne les outils.** Le modèle d'IA de votre client interprète votre requête et la traduit en un ou plusieurs appels d'outils Braze, tels que `get_campaign_list` et `get_campaign_dataseries`.
3. **Braze exécute l'appel d'outil.** Le serveur MCP distant reçoit chaque appel d'outil via votre session OAuth authentifiée, applique l'espace de travail que vous avez spécifié et l'exécute sur l'endpoint REST API de Braze correspondant.
4. **Braze renvoie le résultat.** Le serveur renvoie les données à votre client, qui les met en forme et vous les présente.

Votre accès est l'intersection de deux éléments :

- **Les scopes accordés lors de l'autorisation de la connexion**, tels que `mcp:tools`.
- **Vos propres permissions d'utilisateur du tableau de bord.** Si vous ne pouvez pas consulter les Campaigns dans le tableau de bord, votre agent ne le peut pas non plus. Si vous pouvez créer des modèles d'e-mail, votre agent le peut aussi. Un agent ne peut jamais dépasser votre propre niveau d'accès.

Le contexte de l'espace de travail est transmis avec chaque requête plutôt que stocké dans un fichier de configuration local, de sorte qu'une seule connexion peut fonctionner sur tous les espaces de travail auxquels vous êtes autorisé à accéder.

{% multi_lang_include mcp_server/legal_disclaimer.md %}