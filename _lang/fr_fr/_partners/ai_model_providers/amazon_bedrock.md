---
nav_title: Amazon Bedrock
article_title: Amazon Bedrock
description: "Cet article de référence décrit le partenariat entre Braze et Amazon Bedrock, qui vous permet de connecter des modèles Bedrock à Braze pour les utiliser avec des agents IA personnalisés."
alias: /partners/amazon_bedrock/
page_type: partner
search_tag: Partner

---

# Amazon Bedrock

> [Amazon Bedrock](https://aws.amazon.com/bedrock/) est un service AWS entièrement géré qui fournit un accès à des modèles de fondation proposés par les principales entreprises d'IA via une API unifiée, permettant aux marques de créer et de faire évoluer des applications d'IA générative sur AWS.

{% multi_lang_include alerts/early_access_beta_alert.md feature='The Amazon Bedrock integration' %}

## À propos de l'intégration {#about-the-integration}

L'intégration entre Braze et Amazon Bedrock vous permet de connecter vos identifiants Amazon Bedrock à Braze afin d'utiliser les modèles hébergés sur Bedrock lors de la création d'agents IA personnalisés. Grâce à cette intégration, vos agents peuvent générer du contenu personnalisé, prendre des décisions en temps réel ou mettre à jour des champs de catalogue à l'aide des modèles disponibles via Amazon Bedrock.

Lorsque vous connectez Amazon Bedrock, Braze affiche un ensemble sélectionné de modèles Bedrock pour les agents personnalisés. Les modèles disponibles dans Braze peuvent différer du catalogue complet de votre compte AWS.

Braze utilise l'endpoint `bedrock-mantle` d'Amazon Bedrock pour cette intégration. Amazon Bedrock documente également un endpoint `bedrock-runtime` distinct avec une prise en charge différente des modèles et des fonctionnalités. Lorsque vous consultez la documentation AWS pour vérifier la disponibilité ou le comportement, suivez les instructions relatives à [`bedrock-mantle`](https://docs.aws.amazon.com/bedrock/latest/userguide/endpoints.html).

{% multi_lang_include alerts/important_alerts.md alert='Braze Agents' %}

## Prérequis {#prerequisites}

| Exigences | Description |
|---|---|
| Un compte AWS avec accès à Amazon Bedrock | Un compte AWS avec accès à Amazon Bedrock dans la région AWS où vos modèles sont hébergés. Pour obtenir de l'aide, contactez votre administrateur ou le [support AWS](https://aws.amazon.com/support). |
| Accès aux modèles Amazon Bedrock | Accès dans votre compte AWS aux modèles Bedrock que vous prévoyez d'utiliser. Certains modèles, comme ceux d'Anthropic, nécessitent que l'accès soit accordé sur votre compte AWS. Tous les modèles ne sont pas disponibles dans chaque région AWS — vérifiez la disponibilité régionale de chaque modèle dans la console Amazon Bedrock ou dans [Disponibilité régionale par modèle](https://docs.aws.amazon.com/bedrock/latest/userguide/models-region-compatibility.html) avant de vous connecter. |
| Identifiants d'authentification | Soit une [clé API Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/api-keys.html) à long terme, soit — lorsque l'authentification par rôle IAM est activée pour votre espace de travail — un rôle IAM que Braze peut assumer. |
| Instance Braze | Vous pouvez trouver votre instance Braze sur la [page d'aperçu de l'API]({{site.baseurl}}/api/basics#endpoints) ou auprès de votre gestionnaire d'onboarding Braze. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prérequis" }

## Intégration {#integration}

Pour connecter Amazon Bedrock à Braze :

1. Accédez à **Partner Integrations** > **Technology Partners** dans le tableau de bord de Braze, puis recherchez et sélectionnez **Amazon Bedrock**.
2. Pour **Authentication method**, choisissez **API key** ou **AWS IAM role** (lorsque disponible).
3. Complétez la configuration pour la méthode choisie :
   - **API key :** Saisissez votre **clé API Amazon Bedrock** à long terme. Sélectionnez la **région AWS** où vos modèles Bedrock sont hébergés. Sélectionnez **Save**.
   - **AWS IAM role :** Utilisez les valeurs affichées par Braze pour configurer la politique de confiance de votre rôle IAM, puis saisissez les détails du rôle dans Braze :
     1. Copiez l'**identifiant de compte AWS Braze** et autorisez ce compte dans la politique de confiance de votre rôle IAM.
     2. Copiez l'**ID externe Braze** et exigez-le dans la politique de confiance de votre rôle avec une condition `sts:ExternalId`. Sélectionnez **Generate new external ID** si vous avez besoin d'une nouvelle valeur.
     3. Saisissez l'**ARN du rôle AWS** pour le rôle IAM disposant des permissions Amazon Bedrock. L'ARN doit correspondre à `arn:aws:iam::<account-id>:role/<role-name>`.
     4. Sélectionnez la **région AWS** où vos modèles Bedrock sont hébergés.
     5. Sélectionnez **Save**.

{% alert note %}
**AWS IAM role** n'apparaît que pour les espaces de travail où cette option d'authentification est activée. Avec l'authentification par rôle IAM, Braze assume votre rôle pour générer des identifiants Amazon Bedrock à courte durée de vie et ne stocke pas de clé API à long terme.
{% endalert %}

Après l'enregistrement, Braze affiche un statut de connexion avec la date et l'heure de la connexion. Vous pouvez sélectionner des modèles Amazon Bedrock lors de la [création d'un agent personnalisé]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents) dans la console Agent.

{% alert important %}
Tous les modèles Amazon Bedrock ne sont pas disponibles dans chaque région AWS. Avant de sélectionner une **région AWS** dans Braze, ouvrez les détails du modèle dans Amazon Bedrock et confirmez que le modèle répertorie cette région. Les modèles qui ne sont pas disponibles dans votre région connectée renvoient des erreurs lors de l'invocation de l'agent (par exemple, que le modèle n'existe pas ou n'est plus disponible). Consultez [Models at a glance](https://docs.aws.amazon.com/bedrock/latest/userguide/model-cards.html) pour plus de détails.
{% endalert %}

Pour confirmer que l'intégration fonctionne, accédez à la console Agent et créez un agent de test en utilisant l'un de vos modèles Bedrock. Saisissez une instruction telle que « Raconte-moi une blague » et lancez une invocation de test pour vérifier que le modèle répond comme prévu.

Pour supprimer l'intégration, sélectionnez **Disconnect** sur la page **Amazon Bedrock integration**.

Pour tout problème lié à votre compte ou vos identifiants Amazon Bedrock, contactez le [support AWS](https://aws.amazon.com/support).