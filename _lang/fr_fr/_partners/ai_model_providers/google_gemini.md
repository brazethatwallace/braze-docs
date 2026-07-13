---
nav_title: Google Gemini
article_title: Google Gemini
description: "Cet article de référence présente le partenariat entre Braze et Google Gemini, qui vous permet de connecter les modèles Gemini à Braze pour les utiliser avec des agents d'IA personnalisés."
alias: /partners/gemini/
page_type: partner
search_tag: Partner

---

# Google Gemini

> [Google Gemini](https://deepmind.google/technologies/gemini/) est la famille de modèles d'intelligence artificielle de Google. Elle combine un raisonnement avancé sur le texte, le code et les images pour aider les marques à offrir des expériences plus intelligentes et plus personnalisées.

{% multi_lang_include alerts/important_alerts.md alert='Braze Agents' %}

_Cette intégration est gérée par Google._

## À propos de l'intégration {#about-the-integration}

L'intégration entre Braze et Google Gemini vous permet de connecter Gemini à Braze à l'aide d'une clé API ou en vous connectant avec votre compte Google, afin d'utiliser les modèles Gemini lors de la création d'agents d'IA personnalisés. Grâce à cette intégration, vos agents peuvent générer des textes personnalisés, prendre des décisions en temps réel ou mettre à jour les champs du catalogue à l'aide des modèles Gemini de Google.

## Conditions préalables {#prerequisites}

| Exigences | Description |
|---|---|
| Compte Google Cloud | Un compte Google Cloud avec accès à l'API Gemini. Vous pouvez vous authentifier avec une clé API ou en connectant votre compte Google et en sélectionnant un projet GCP dans le tableau de bord de Braze. Pour obtenir de l'aide, contactez votre administrateur ou l'[assistance Google Cloud](https://cloud.google.com/support). |
| Instance Braze | Vous trouverez votre instance Braze sur la [page d'aperçu de l'API]({{site.baseurl}}/api/basics#endpoints) ou auprès de votre gestionnaire d'onboarding Braze. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Intégration {#integration}

Pour connecter Google Gemini à Braze :

1. Dans le tableau de bord de Braze, accédez à **Intégrations partenaires** > **Partenaires technologiques** et recherchez Google Gemini.
2. Pour la **Méthode d'authentification**, choisissez **Clé API** ou **Connecter un compte Google**.
3. Complétez la configuration selon la méthode choisie :
   - **Clé API :** Sous **Type d'API**, sélectionnez **Gemini API** ou **Gemini Enterprise Agent Platform (anciennement Vertex AI)**. Saisissez votre clé API. Si vous avez sélectionné Gemini Enterprise Agent Platform, saisissez également votre **ID de projet**. Sélectionnez **Enregistrer**.
   - **Connecter un compte Google :** Sélectionnez **Connecter un compte Google**, puis sélectionnez **Connecter Google** et connectez-vous avec votre compte Google. Sélectionnez votre **Projet GCP** dans le menu déroulant. Si Gemini API et Gemini Enterprise Agent Platform sont tous deux activés dans ce projet, choisissez le **Type d'API** que Braze doit utiliser. Sélectionnez **Enregistrer**.

{% alert note %}
**Connecter un compte Google** n'apparaît que pour les espaces de travail où cette option d'authentification est activée.
{% endalert %}

Une fois l'enregistrement effectué, vous pouvez sélectionner les modèles Gemini lors de la [création d'un agent personnalisé]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents) dans la Console des agents.

Contactez l'[assistance Google Cloud](https://cloud.google.com/support) pour tout problème ou toute question concernant votre intégration.