---
nav_title: Okendo
article_title: Okendo
description: "Découvrez comment intégrer Okendo à Braze."
page_type: partner
search_tag: Partner
alias: /partners/okendo/
---

# Okendo

> [Okendo](https://okendo.io/) est une plateforme unifiée de marketing client qui fournit des outils pour cultiver l'engagement, développer le bouche-à-oreille et maximiser la valeur vie client afin de mobiliser vos clients pour une croissance plus rapide et plus efficace.

*Cette intégration est maintenue par Okendo.*

## À propos de l'intégration {#about-the-integration}

L'intégration de Braze avec Okendo fonctionne sur plusieurs produits de la plateforme d'Okendo, notamment les évaluations, la fidélisation, les recommandations, les enquêtes et les quiz. Okendo envoie des événements personnalisés et des attributs utilisateur à Braze, qui peuvent être utilisés pour personnaliser et déclencher des messages.

## Conditions préalables {#prerequisites}

| Condition | Description |
|------------------------|-----------------------------------------------------------------------------|
| Compte Okendo | Un compte Okendo est nécessaire pour bénéficier de ce partenariat. |
| Clé API REST Braze | Une clé API REST Braze avec les autorisations `users.track`. Elle peut être créée dans le tableau de bord de Braze depuis **Settings** > **API Keys**. |
| Endpoint REST de Braze | [L'URL de votre endpoint REST]({{site.baseurl}}/api/basics/#endpoints). Votre endpoint dépend de l'URL Braze de votre instance. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Intégration {#integration}

### Étape 1 : Configurer le connecteur Braze dans Okendo {#step-1-set-up-braze-connector-in-okendo}

1. Dans Okendo, accédez à **Settings** > **Integrations** > **Email & SMS** > **Braze**.
2. Ajoutez l'endpoint de l'API et la clé API dans les paramètres d'**Integration**.

### Étape 2 : Configurer votre identifiant {#step-2-configure-your-identifier}

Le champ `external_id` est utilisé pour identifier l'utilisateur associé à chaque événement. Activez l'option **Use Shopify Customer ID for Braze user identification** pour associer le champ aux ID des clients Shopify. Sinon, désactivez-la pour l'associer à l'adresse e-mail de chaque utilisateur.

## Synchronisation des événements et des attributs d'Okendo avec Braze {#syncing-okendo-events-and-attributes-to-braze}

### Événements personnalisés {#custom-events}

{% alert note %}
Pour des exemples de données d'événements, reportez-vous à la [documentation d'Okendo](https://support.okendo.io/en/articles/10396885-getting-started-with-braze-and-okendo#h_679a212e3c).
{% endalert %}

#### Événements d'évaluation {#review-events}

- Okendo Review Created
- Okendo Review Request

#### Événements de recommandation {#referral-events}

- Sent Okendo Referral
- Opted In to Okendo Referrals
- Okendo Referral Invitation
- Received Okendo Referral Coupon
- Redeemed Okendo Referral Coupon
- Okendo Referral Rejected

#### Événements de fidélisation {#loyalty-events}

- Enrolled in Okendo Loyalty
- Okendo Loyalty Points Awarded
- Okendo Loyalty Points Redeemed
- Okendo Loyalty Tier Changed
- Okendo Loyalty Points Adjusted

#### Événement d'enquête {#survey-event}

- Submitted Okendo Survey

#### Événement de quiz {#quiz-event}

- Submitted Okendo Quiz

### Attributs personnalisés {#custom-attributes}

Okendo envoie les données du profil utilisateur sous forme d'attributs personnalisés dans Braze, qui peuvent être utilisés pour créer des segments d'audience. En voici quelques exemples :

- Questions de profil posées dans les enquêtes et lors de la soumission d'une évaluation, telles que l'âge, la date d'anniversaire, le type de peau et la couleur des cheveux
- Indicateurs d'évaluation tels que la _note moyenne d'évaluation_ et le _sentiment moyen d'évaluation_
- Indicateurs de fidélisation tels que le _solde de points_ et le _niveau VIP_
- Indicateurs de recommandation tels que le _nombre de recommandations réussies_ et le _chiffre d'affaires total des recommandations_
- Score Net Promoter Score collecté à partir d'une enquête

## Utilisation de Braze avec les produits Okendo {#using-braze-with-okendo-products}

En fonction du produit Okendo, vous devez effectuer des étapes supplémentaires pour utiliser Braze et Okendo ensemble. Reportez-vous aux articles suivants pour plus de détails :

- [Intégration des évaluations avec Braze](https://support.okendo.io/en/articles/10509722-integrating-reviews-with-braze#h_09c4575b39)
- [Intégration de la fidélisation avec Braze](https://support.okendo.io/en/articles/10509615-integrating-loyalty-with-braze#h_47129ea105)
- [Intégration des recommandations avec Braze](https://support.okendo.io/en/articles/10509748-build-a-canvas-in-braze-to-trigger-referral-emails#h_32fb5ba542)
- [Intégration des enquêtes avec Braze](https://support.okendo.io/en/articles/11546662-integrating-surveys-with-braze)
- [Intégration des quiz avec Braze](https://support.okendo.io/en/articles/10509739-build-a-canvas-in-braze-to-send-quiz-recommendations#h_53748cb121)

{% alert note %}
Pour obtenir de l'aide sur la configuration de l'intégration, contactez l'équipe d'assistance d'Okendo.
{% endalert %}