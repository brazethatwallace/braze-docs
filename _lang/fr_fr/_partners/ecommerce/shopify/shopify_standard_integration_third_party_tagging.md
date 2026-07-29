---
nav_title: Intégration standard de Shopify avec tags tiers
article_title: Intégration standard de Shopify avec tags tiers
description: "Cet article de référence explique comment configurer l'intégration standard de Shopify avec un outil d'étiquetage tiers."
page_type: partner
search_tag: Partner
alias: /shopify_standard_integration_third_party_tagging/
page_order: 2
---

# Intégration standard de Shopify avec un outil de tags tiers {#shopify-standard-integration-with-third-party-tagging-tool}

> Cette page vous guide dans l'utilisation d'outils tiers, comme Google Tag Manager, avec l'[intégration standard de Shopify]({{site.baseurl}}/shopify_standard_integration) pour initialiser et charger le SDK Web de Braze.

Pour les boutiques en ligne Shopify, nous vous recommandons d'utiliser la méthode d'intégration standard de Braze pour prendre en charge les SDK de Braze sur votre site. Toutefois, nous comprenons que vous puissiez préférer utiliser un outil tiers, comme Google Tag Manager. Si vous choisissez d'utiliser un outil tiers avec le connecteur Shopify de Braze, gardez à l'esprit que l'intégration Braze et l'app embed géreront le SDK pendant le processus de paiement.

## Conditions requises {#requirements}

- **Clé API cohérente entre votre outil tiers et le connecteur Shopify :** la clé API doit être cohérente entre Braze et votre outil tiers. Cela permet d'éviter la création d'utilisateurs en double et de maintenir la compatibilité entre les SDK.
  - **Emplacement de la clé API :** après l'onboarding du chemin d'intégration standard, l'intégration créera automatiquement une application web Braze nommée « Shopify ». Récupérez la clé API au sein de l'intégration qui est utilisée avec la configuration de votre outil tiers.
- **Versions du SDK cohérentes entre votre outil tiers et le connecteur Shopify :** les nouveaux clients sont provisionnés sur la dernière version du SDK lors de la configuration. Votre outil tiers doit utiliser la même version du SDK que celle configurée dans les paramètres d'intégration de Braze. Les clients existants sont notifiés lorsqu'une version plus récente est disponible et peuvent effectuer la mise à niveau eux-mêmes depuis les paramètres d'intégration.
- **Cohérence du moment d'initialisation du SDK :** dans les paramètres d'intégration standard de Shopify, vous pouvez sélectionner les SDK à initialiser au démarrage de la session ou lors de l'identification d'un compte. Ce paramètre doit être cohérent entre votre outil tiers et Braze. Les incohérences pourraient entraîner des problèmes en aval pour l'utilisateur et la synchronisation des données.

{% alert note %}
Nous vous recommandons d'utiliser exclusivement la méthode d'intégration standard plutôt que de l'utiliser en tandem avec des gestionnaires de tags tiers, ce qui peut entraîner des conflits entre le SDK de Braze et les outils tiers. Si vous utilisez un outil tiers, testez-le pour vous assurer que tout fonctionne comme prévu.
{% endalert %}

## Mise en place de l'intégration avec un outil tiers {#setting-up-the-integration-with-a-third-party-tool}

Si vous ne suivez pas les étapes indiquées, vous risquez d'être confronté à des problèmes inattendus ; veillez donc à les respecter scrupuleusement.

1. Suivez les étapes fournies dans la [configuration de l'intégration standard de Shopify]({{site.baseurl}}/shopify_standard_integration). Lors de l'[activation des SDK Web de Braze]({{site.baseurl}}/partners/ecommerce/shopify/shopify_standard_integration#step-2-enable-braze-web-sdks), cochez la case indiquant que vous utilisez un outil tiers pour ajouter le SDK Web de Braze à votre site Shopify.
2. Allez dans **Paramètres** > **Paramètres de l'application**, sélectionnez l'application web **Shopify**, puis copiez la **clé API pour Shopify sur le Web**.
3. Collez la clé API dans la configuration du SDK Web de votre outil tiers et définissez la version du SDK pour qu'elle corresponde à celle de l'intégration Shopify de Braze.

{% alert note %}
Si vous utilisez Google Tag Manager, veillez à ce que les versions du SDK soient alignées entre GTM et la configuration de votre intégration Shopify de Braze.
{% endalert %}

## Capture des données Shopify et synchronisation des utilisateurs {#capturing-shopify-data-and-syncing-users}

Tant que le SDK Web est accessible sur le front-end de votre site Shopify via un outil tiers, l'intégration standard capturera les données Shopify et synchronisera les utilisateurs comme prévu.

## Considérations et clauses de non-responsabilité {#considerations-and-disclaimers}

- **Paramètres d'initialisation :** si vous modifiez vos paramètres d'initialisation via votre outil tiers, la synchronisation des utilisateurs et des données peut être impactée. Par exemple, si vous choisissez d'initialiser votre SDK lorsqu'un formulaire de consentement aux cookies est accepté, Braze ne recevra pas de suivi des utilisateurs anonymes ni de données tant que l'utilisateur n'aura pas donné son consentement.
- **La définition d'attributs directement par le biais de `dataLayer` n'est pas prise en charge :** utilisez `window.braze` au lieu de `dataLayer` pour définir les attributs.
- **Utilisateurs potentiellement en double :** si la clé API ne correspond pas entre Braze et votre outil tiers, des utilisateurs en double peuvent être créés.
- **Incompatibilité du SDK :** l'utilisation d'un numéro de version incorrect peut entraîner des problèmes avec les méthodes du SDK.