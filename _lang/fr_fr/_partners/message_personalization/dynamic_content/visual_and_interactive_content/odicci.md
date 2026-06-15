---
nav_title: Odicci
article_title: Odicci
description: "Guide étape par étape pour intégrer Odicci à Braze afin de créer des campagnes marketing personnalisées"
alias: /partners/odicci/
page_type: partner
search_tag: Partner
---

# Intégrer Odicci à Braze {#integrate-odicci-with-braze}

> Découvrez comment intégrer Braze à [Odicci](https://www.odicci.com/), une plateforme qui donne aux entreprises les moyens d'acquérir, d'engager et de fidéliser leurs clients grâce à des expériences omnicanales axées sur la fidélisation.

{% alert tip %}
Consultez le [Centre d'aide Odicci](https://help.odicci.com) pour obtenir des ressources supplémentaires et des FAQ.
{% endalert %}

## Cas d'utilisation {#use-cases}

Vous pouvez connecter la plateforme Odicci à Braze pour un partage fluide des données et la gestion des campagnes, ce qui inclut :

- L'envoi automatique à Braze des données d'audience collectées dans les expériences Odicci.
- Le déclenchement de campagnes marketing personnalisées en fonction des interactions des utilisateurs.
- Le mappage des champs entre Odicci et Braze pour assurer une synchronisation précise des données.

## Exemple {#example}

Un détaillant utilise les expériences gamifiées d'Odicci pour collecter des adresses e-mail en vue d'une campagne marketing.

1. Un client termine un jeu dans Odicci en fournissant son adresse e-mail.
2. Odicci synchronise automatiquement ces données avec Braze.
3. Braze déclenche un e-mail de remerciement personnalisé et inclut un code de réduction.

## Conditions préalables {#prerequisites}

Avant de commencer, vous aurez besoin des éléments suivants :

| Prérequis | Description |
|---------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| Un compte Odicci | Un compte Odicci avec accès à la section **Integrations** est nécessaire pour profiter de ce partenariat. |
| Clé API REST Braze | Une clé API REST Braze avec les autorisations `users.track` et `campaigns.list`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Intégration d'Odicci {#integrating-odicci}

### Étape 1 : Activer l'intégration dans Odicci {#step-1-enable-the-integration-in-odicci}

1. Connectez-vous à votre compte Odicci.
2. Accédez à la section **Settings > Integrations**.
3. Recherchez l'intégration **Braze** et cliquez sur **Connect**.

   ![Connecter l'intégration Braze]({% image_buster /assets/img/odicci/braze_connect.png %})

4. Saisissez votre clé API REST Braze dans le champ prévu à cet effet.
5. Enregistrez les paramètres pour activer l'intégration au niveau du compte.

### Étape 2 : Obtenir votre clé API REST Braze {#step-2-obtain-your-braze-rest-api-key}

1. Connectez-vous à votre compte Braze.
2. Accédez à **Console de développement > Clés API REST**.
3. Créez une nouvelle clé API ou copiez une clé existante disposant de l'autorisation `users.track`.

### Étape 3 : Activer l'intégration au niveau de l'expérience {#step-3-activate-the-integration-at-the-experience-level}

1. Créez ou ouvrez une **expérience** dans Odicci Studio.
2. Accédez à **Studio > Settings > Integrations**.
3. Repérez la case à cocher **Braze** et cochez-la pour activer l'intégration pour l'expérience.
4. Enregistrez vos modifications.

### Étape 4 : Mapper les champs {#step-4-map-fields}

1. Après avoir activé l'intégration, restez dans la section **Studio > Settings > Integrations**.
2. Mappez les champs de votre expérience Odicci (par exemple, `Email`, `Name`) à leurs champs correspondants dans Braze.
3. Enregistrez votre configuration.

   ![Configuration du mappage des champs]({% image_buster /assets/img/odicci/braze_field_mapping.png %})

### Étape 5 : Tester l'intégration {#step-5-test-the-integration}

1. Exécutez l'expérience dans Odicci pour collecter des données de test.
2. Vérifiez que les données se synchronisent correctement avec Braze en consultant le tableau de bord de Braze ou les journaux de données.
3. Assurez-vous que les champs mappés sont correctement renseignés dans Braze.

## Résolution des problèmes {#troubleshooting}

Si vous rencontrez des problèmes avec l'intégration, envisagez les solutions suivantes. Pour obtenir de l'aide supplémentaire, contactez l'[assistance Odicci](https://help.odicci.com).

### Clé API non valide {#api-key-not-valid}

Vérifiez à nouveau votre clé API Braze et assurez-vous qu'elle dispose des autorisations nécessaires. Ensuite, saisissez à nouveau la clé API dans les paramètres d'intégration d'Odicci.

### Les données ne se synchronisent pas {#data-not-syncing}

Vérifiez que les champs de la section **Field Mapping** sont correctement configurés. Ensuite, assurez-vous que la clé API dispose des autorisations nécessaires pour l'importation des données utilisateur.

### La campagne ne se déclenche pas {#campaign-not-triggering}

Vérifiez les paramètres de la campagne dans Braze pour vous assurer que l'audience ou les conditions de déclenchement correctes sont définies.