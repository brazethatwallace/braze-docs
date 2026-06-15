---
nav_title: Justuno
article_title: Justuno
description: "Découvrez comment intégrer Justuno à Braze afin d'exploiter les données clients sur les deux plateformes pour créer des expériences plus personnalisées pour toutes les audiences."

alias: /partners/justuno
page_type: partner
search_tag: Partner
---

# Justuno

> [Justuno](https://www.justuno.com/) vous permet de créer des expériences visiteurs entièrement optimisées pour toutes vos audiences grâce à des segments dynamiques, offrant le ciblage le plus avancé disponible&#8212;le tout sans impacter la vitesse du site ni augmenter le travail de développement. Analysez les taux de conversion en consultant des analyses personnalisées telles que le nombre de profils créés, le taux de retour des visiteurs influencés et les pages par session afin de conserver un avantage marketing dans votre secteur. Justuno vous permet d'augmenter le chiffre d'affaires par visiteur, d'établir des engagements clients significatifs et de développer votre activité. Optimisez l'ensemble du parcours de l'audience de bout en bout avec une plateforme connectée.

## Cas d'utilisation {#use-cases}

Braze permet à tout marketeur de collecter et d'agir sur n'importe quelle quantité de données provenant de n'importe quelle source, afin d'engager de manière créative avec les clients en temps réel, sur tous les canaux, à partir d'une seule plateforme.

L'intégration de Justuno et de Braze vous offre le meilleur des deux mondes. Vous pouvez combiner les données clients enregistrées dans Braze avec les données visiteurs et clients enregistrées dans Justuno et créer des expériences plus personnalisées pour toutes les audiences. Vous augmentez ainsi l'efficacité de vos campagnes marketing et de vos engagements clients.

## Conditions préalables {#prerequisites}

| Clé API REST de Braze | Une clé API REST de Braze avec les autorisations `users.track` et `custom_attributes.get`.<br><br>Celle-ci peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés API**. |
| Endpoint REST de Braze | L'URL de votre endpoint REST. Votre endpoint dépendra de l'[URL de Braze pour votre instance]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Intégration de Justuno à Braze {#integrating-justuno-with-braze}

### Étape 1 : Créer des attributs personnalisés dans Braze {#step-1-create-custom-attributes-in-braze}

Pour synchroniser les attributs utilisateurs de Justuno vers Braze, vous devrez créer ces attributs dans Braze si ce n'est pas déjà fait. Vous pouvez le faire en allant dans **Paramètres des données** > **Attributs personnalisés**, puis en créant vos attributs personnalisés. Pour une présentation complète, consultez [Gérer les attributs personnalisés dans Braze]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/).

### Étape 2 : Ajouter l'application Braze à Justuno {#step-2-add-the-braze-app-to-justuno}

#### Étape 2.1 : Ajouter l'application à votre compte {#step-21-add-it-to-your-account}

Pour ajouter l'application Braze à votre compte Justuno, allez dans **Account Settings** > **Apps**, puis recherchez et sélectionnez l'application Braze.

![La page « Connect Apps » dans Justuno avec l'application Braze affichée dans la liste des résultats de recherche.]({% image_buster /assets/img/justuno/search-for-braze.png %})

Saisissez la clé API et l'URL de base [que vous avez créées précédemment](#prerequisites), puis sélectionnez **Connect**.

![La fenêtre contextuelle d'authentification de Braze demandant une clé API de Braze et une URL de base.]({% image_buster /assets/img/justuno/authenticate-braze.png %}){: style="max-width:75%;"}

#### Étape 2.2 : Ajouter l'application à votre flux de travail {#step-22-add-it-to-your-workflow}

Pour ajouter l'application Braze à votre [flux de travail Justuno](https://hub.justuno.com/knowledge/workflows-overview), glissez-déposez l'action **Sync to App** dans votre flux de travail, puis choisissez **Select App** > **Braze**.

![L'option « Select App » située sur l'action « Sync to App ».]({% image_buster /assets/img/justuno/select-app.png %}){: style="max-width:45%;"}

### Étape 3 : Connecter vos groupes d'abonnement Braze {#step-3-connect-your-braze-subscription-groups}

Pour envoyer des données de profil depuis Justuno vers un groupe d'abonnement e-mail ou SMS spécifique de Braze, vous devez ajouter leur ID à l'application Braze dans votre flux de travail Justuno.

| Type d'ID | Requis ? | Description |
|---|---|---|
| ID du groupe d'abonnement SMS de Braze | Oui | Cet ID est utilisé pour recueillir le consentement SMS à partir des profils utilisateurs. Si aucun ID n'est saisi dans Justuno, les profils n'auront pas de consentement lorsque Justuno transmettra ce profil à Braze. |
| ID du groupe d'abonnement e-mail de Braze | Non | Si cet ID n'est pas saisi dans Justuno, Justuno enverra les données du profil à Braze en tant qu'utilisateur sans groupe d'abonnement associé. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Étape 3 : Connecter vos groupes d'abonnement Braze" }

#### Étape 3.1 : Localiser les ID dans Braze {#step-31-locate-the-ids-in-braze}

Pour localiser ces ID dans le tableau de bord de Braze :

1. Allez dans **Audience** > **Subscriptions**.
2. Pour chaque groupe d'abonnement, notez l'ID situé dans la colonne ID.

#### Étape 3.2 : Ajouter les ID à l'application Braze {#step-32-add-the-ids-to-the-braze-app}

Dans votre flux de travail Justuno, ouvrez l'application Braze, puis saisissez les ID de chaque groupe d'abonnement.

![L'application Braze ouverte dans un flux de travail Justuno avec la possibilité d'ajouter des ID de groupes d'abonnement e-mail et SMS.]({% image_buster /assets/img/justuno/enter-subscription-groups.png %}){: style="max-width:55%;"}

### Étape 4 : Configurer vos attributs {#step-4-configure-your-attributes}

Les attributs suivants sont automatiquement synchronisés de Justuno vers Braze :

- E-mail
- Téléphone
- Prénom
- Nom
- Langue
- Genre
- Pays

Pour synchroniser des attributs supplémentaires :

1. Dans l'application Braze au sein de votre flux de travail, sélectionnez **Sync Another Property**.
    ![L'application Braze ouverte dans un flux de travail Justuno affichant l'option « Sync Another Property ».]({% image_buster /assets/img/justuno/sync-another-property.png %}){: style="max-width:55%;"}
2. Choisissez les attributs de Braze que vous souhaitez synchroniser.
3. Faites correspondre les propriétés dans Justuno avec leurs équivalents dans Braze (tels que les identifiants de réseaux sociaux, la date d'anniversaire, les préférences d'achat, les réponses aux enquêtes, etc.). Gardez à l'esprit que ces propriétés sont considérées comme des données zero-party ou first-party. Pour en savoir plus, consultez [Justuno : collecte de données visiteurs](https://www.justuno.com/guides/zero-first-party-data/).
4. Dans le générateur de flux de travail, choisissez **Save**, **Preview** ou **Publish** pour votre flux de travail.
    ![Le menu « Publish » ouvert avec les options Save, Preview et l'historique des versions.]({% image_buster /assets/img/justuno/publish-workflow.png %}){: style="max-width:45%;"}

## Informations importantes {#things-to-know}

- Vous devez saisir manuellement l'ID du groupe d'abonnement dans les paramètres de l'application.
- Les types de données suivants de Braze ne sont **pas pris en charge** : objet, tableau d'objets.
- Le consentement implicite par SMS est fourni lorsque le champ de consentement SMS de Justuno n'est pas utilisé.
- Le consentement explicite par SMS est respecté si le design Justuno inclut le champ de consentement.