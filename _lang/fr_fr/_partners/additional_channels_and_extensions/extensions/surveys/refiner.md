---
nav_title: Refiner
article_title: Refiner
alias: /partners/refiner/
description: "Cet article de référence décrit le partenariat entre Braze et Refiner, qui vous permet d'envoyer des événements d'enquête et des données de réponse dans Braze pour déclencher des campagnes, segmenter les utilisateurs et mettre à jour les profils utilisateur."
page_type: partner
search_tag: Partner

---

# Refiner

> [Refiner](https://refiner.io) est une plateforme d'enquêtes in-app pour les applications SaaS et mobiles. Elle permet aux équipes produit et voix du client de lancer des enquêtes in-app ciblées et de collecter en continu des données NPS, CSAT, CES, des retours produit et des données utilisateur zero-party.

_Cette intégration est maintenue par Refiner._

## À propos de l'intégration {#about-the-integration}

Utilisez l'intégration Refiner et Braze pour envoyer des événements d'enquête et des données de réponse depuis Refiner vers votre compte Braze. Utilisez ces données pour déclencher des Campaigns Braze en fonction des interactions avec les enquêtes (comme une enquête complétée), segmenter les utilisateurs en fonction des réponses et mettre à jour les profils utilisateur Braze avec des attributs dérivés des réponses aux enquêtes.

## Cas d'usage {#use-cases}

- Segmenter les utilisateurs en fonction des réponses aux enquêtes, comme les scores NPS ou les évaluations CSAT.
- Déclencher des Campaigns personnalisées dans Braze en fonction des résultats d'enquête.
- Piloter des parcours cross-canal à l'aide de Braze Canvas ou d'autres outils d'orchestration.

## Prérequis {#prerequisites}

| Condition | Description |
|---|---|
| Compte Refiner | Un compte [Refiner](https://refiner.io) est requis pour utiliser cette intégration. |
| Clé API REST Braze | Une clé API REST Braze avec les permissions `users.track`. Celle-ci peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés API**. |
| Endpoint REST Braze | L'URL de votre endpoint REST. Votre endpoint dépend de l'[URL Braze de votre instance]({{site.baseurl}}/api/basics#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prérequis" }

## Intégration {#integration}

### Étape 1 : Connecter votre compte Braze {#step-1-connect-your-braze-account}

Dans la section **Integrations** de votre projet Refiner, sélectionnez **Connect Braze**. Saisissez votre clé API REST Braze et l'identifiant de votre instance Braze.

### Étape 2 : Mapper les identifiants utilisateur {#step-2-map-user-identifiers}

Mappez l'identifiant utilisateur Refiner à l'identifiant Braze que vous utilisez, comme un `external_id` Braze ou une adresse e-mail. Cela garantit que les événements sont associés au bon utilisateur dans Braze.

### Étape 3 : Choisir les données à synchroniser {#step-3-choose-data-to-sync}

- Sélectionnez les enquêtes dont vous souhaitez synchroniser les données vers Braze.
- Sélectionnez les événements Refiner à envoyer à Braze, tels que **Survey Seen**, **Survey Dismissed** et **Survey Completed**.

![Le panneau de paramètres d'intégration Refiner affichant les options de sélection d'enquête et de mappage d'événements.]({% image_buster /assets/img/refiner.jpg %})

## Personnaliser Refiner {#customize-refiner}

- Choisissez si les données envoyées à Braze incluent uniquement les réponses aux enquêtes ou également des champs de données de contact supplémentaires.
- Choisissez si les champs de données synchronisés doivent être préfixés par `refiner_` pour les rendre plus faciles à identifier dans votre compte Braze.

## Utiliser les données d'enquête dans Braze {#use-survey-data-in-braze}

Après avoir connecté Braze et Refiner, les événements d'enquête tels que **Saw Survey** ou **Completed Survey** apparaissent sur les profils utilisateur dans votre compte Braze. Utilisez ces événements pour déclencher et personnaliser des messages dans Braze, ou utilisez les données de réponse aux enquêtes pour segmenter les utilisateurs.

{% alert note %}
Vous pouvez également envoyer des enquêtes Refiner par e-mail via Braze. Pour plus de détails, consultez la [documentation d'intégration de Refiner](https://refiner.io/docs/kb/integrations/braze-integration/).
{% endalert %}

## Résolution des problèmes {#troubleshooting}

Si vous rencontrez des problèmes avec l'intégration, consultez les ressources suivantes :

- [Guide d'intégration Refiner et Braze](https://refiner.io/docs/kb/integrations/braze-integration/)
- [Contacter le support Refiner](https://refiner.io/docs/kb/getting-started/contact-support/)