---
nav_title: Microsoft Foundry
article_title: Microsoft Foundry
description: "Cet article de référence décrit le partenariat entre Braze et Microsoft Foundry, qui vous permet de connecter des modèles d'IA gérés par Foundry à Braze pour les utiliser avec des agents IA personnalisés."
alias: /partners/microsoft_foundry/
page_type: partner
search_tag: Partner

---

# Microsoft Foundry

> [Microsoft Foundry](https://azure.microsoft.com/en-us/products/ai-foundry) est une plateforme Azure unifiée de type plateforme en tant que service (PaaS) pour les opérations d'IA d'entreprise, les créateurs de modèles et le développement d'applications.

{% multi_lang_include alerts/early_access_beta_alert.md feature='The Microsoft Foundry integration' %}

## À propos de l'intégration {#about-the-integration}

L'intégration de Braze et Microsoft Foundry vous permet d'utiliser des modèles d'IA générative gérés dans Microsoft Foundry lors de la création d'agents IA personnalisés. L'intégration prend actuellement en charge deux modèles : gpt-5.4-mini et gpt-5.4-nano. Grâce à cette intégration, vos agents peuvent générer du contenu personnalisé, prendre des décisions en temps réel ou mettre à jour des champs de Catalogue à l'aide de modèles gérés par Foundry.

{% multi_lang_include alerts/important_alerts.md alert='Braze Agents' %}

## Conditions préalables {#prerequisites}

| Exigences | Description |
|---|---|
| Un compte Azure avec un abonnement actif | Pour obtenir de l'aide, contactez votre administrateur ou consultez les [options de compte Azure](https://azure.microsoft.com/en-us/pricing/purchase-options/azure-account). |
| Instance Microsoft Foundry | Une instance Microsoft Foundry pour créer un projet. |
| Projet Microsoft Foundry | Un projet au sein de votre instance Foundry pour héberger les modèles déployés. |
| Modèles déployés | Au moins un des modèles pris en charge déployé dans le projet Foundry. |
| Instance Braze | Vous pouvez trouver votre instance Braze sur la [page d'aperçu de l'API]({{site.baseurl}}/api/basics#endpoints) ou auprès de votre gestionnaire d'onboarding Braze. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Déployer les modèles pris en charge dans Foundry {#deploy-supported-models-in-foundry}

L'intégration de Braze avec Microsoft Foundry prend en charge deux modèles : gpt-5.4-mini et gpt-5.4-nano. Les deux doivent être déployés dans un projet Foundry au sein de l'instance Foundry que vous intégrez.

Pour créer le projet Foundry et déployer les modèles, suivez la [documentation Microsoft Foundry](https://learn.microsoft.com/en-us/azure/foundry/tutorials/quickstart-create-foundry-resources?tabs=portal) :

1. Connectez-vous à Microsoft Foundry via votre portail Azure.
2. Dans Microsoft Foundry, créez un projet pour héberger les modèles que vous souhaitez intégrer à Braze.
3. Décidez si vous souhaitez utiliser gpt-5.4-mini, gpt-5.4-nano, ou les deux.
4. Pour chaque modèle que vous souhaitez utiliser, déployez-le en suivant la documentation Microsoft Foundry. Ne modifiez pas le nom de déploiement par défaut, sinon l'intégration de ce modèle pourrait ne plus fonctionner.

## Intégration {#integration}

Pour connecter votre instance Foundry à Braze :

1. Accédez à **Intégrations partenaires** > **Partenaires technologiques** dans le tableau de bord de Braze et recherchez **Microsoft Foundry**.
2. Saisissez votre **clé API Microsoft Foundry**.
3. Saisissez le **nom de votre instance Microsoft Foundry**. Il s'agit du sous-domaine situé avant `.services.ai.azure.com`.
4. Sélectionnez **Enregistrer**.

Après l'enregistrement, Braze affiche un état connecté avec la date et l'heure de la connexion. Vous pouvez sélectionner les modèles Foundry lors de la [création d'un agent personnalisé]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents) dans la Console des agents.

{% alert important %}
Pour utiliser gpt-5.4-mini ou gpt-5.4-nano, vous devez déployer chaque modèle dans votre projet Foundry sans modifier le nom de déploiement par défaut.
{% endalert %}

Pour confirmer que l'intégration fonctionne, accédez à la Console des agents et créez un agent de test en utilisant l'un de vos modèles déployés. Saisissez une instruction simple, telle que « Raconte-moi une blague », et lancez une invocation de test pour vérifier que le modèle répond comme prévu.

Pour supprimer l'intégration, sélectionnez **Déconnecter** sur la page **Intégration Microsoft Foundry**.

Contactez l'[assistance Azure](https://azure.microsoft.com/en-us/support/options/) pour toute question ou tout problème concernant votre intégration.