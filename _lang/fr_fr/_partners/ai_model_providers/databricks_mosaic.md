---
nav_title: Databricks Mosaic
article_title: Databricks Mosaic
description: "Cet article de référence décrit le partenariat entre Braze et Databricks Mosaic, qui vous permet de connecter des modèles Databricks à Braze pour les utiliser avec des agents IA personnalisés."
alias: /partners/databricks_mosaic/
page_type: partner
search_tag: Partner

---

# Databricks Mosaic

> [Databricks Mosaic AI](https://www.databricks.com/product/artificial-intelligence) est la plateforme unifiée de Databricks pour créer, déployer et gérer des modèles d'intelligence artificielle et de machine learning à grande échelle sur la Databricks Data Intelligence Platform.

{% multi_lang_include alerts/important_alerts.md alert='Braze Agents' %}

_Cette intégration est maintenue par Databricks._

## À propos de l'intégration {#about-the-integration}

L'intégration entre Braze et Databricks Mosaic vous permet de connecter votre jeton et votre espace de travail Databricks à Braze afin d'utiliser les modèles Databricks lors de la création d'agents IA personnalisés. Braze utilise vos identifiants Databricks Mosaic pour générer du contenu destiné à vos clients. Grâce à cette intégration, vos agents peuvent générer du texte personnalisé, prendre des décisions en temps réel ou mettre à jour des champs de catalogue à l'aide de modèles Databricks.

## Conditions préalables {#prerequisites}

| Exigences | Description |
|---|---|
| Compte Databricks avec jeton d'accès personnel | Un compte Databricks avec un [jeton d'accès personnel](https://docs.databricks.com/en/dev-tools/auth/pat.html). Pour obtenir de l'aide, contactez votre administrateur ou l'[assistance Databricks](https://help.databricks.com/). |
| Nom de l'espace de travail Databricks | Le nom de l'espace de travail (ou instance) de votre compte Databricks. Il s'agit du sous-domaine précédant `.cloud.databricks.com` ou `.azuredatabricks.net` (par exemple, `dbc-eb57d699-f22c`). |
| Instance Braze | Vous pouvez trouver votre instance Braze sur la [page d'aperçu de l'API]({{site.baseurl}}/api/basics/#endpoints) ou auprès de votre gestionnaire d'onboarding Braze. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Intégration {#integration}

Pour connecter vos identifiants Databricks Mosaic à Braze :

1. Dans le tableau de bord de Braze, accédez à **Intégrations partenaires** > **Partenaires technologiques** et recherchez **Databricks Mosaic Integration**.
2. Saisissez votre **jeton Databricks**.
3. Saisissez le **nom de votre espace de travail Databricks**. Il s'agit du sous-domaine précédant `.cloud.databricks.com` ou `.azuredatabricks.net`.
4. Sélectionnez **Enregistrer**.

Une fois l'enregistrement effectué, Braze affiche un état connecté avec la date et l'heure de la connexion. Vous pouvez sélectionner des modèles Databricks lors de la [création d'un agent personnalisé]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/) dans la Console des agents.

Pour supprimer l'intégration, sélectionnez **Déconnecter** sur la page **Databricks Mosaic Integration**.

Contactez l'[assistance Databricks](https://help.databricks.com/) pour toute question ou tout problème concernant votre intégration.