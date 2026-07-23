---
nav_title: Komo
article_title: Komo
description: "Cet article de référence décrit le partenariat entre Braze et Komo, une plateforme d'engagement client spécialisée dans la gamification, le contenu interactif, les compétitions, les prix et la fidélité. Grâce à cette intégration, les données first-party et zero-party capturées dans Komo peuvent être publiées dans Braze."
alias: /partners/komo/
page_type: partner
search_tag: Partner

---

# Komo

> [Komo](https://komo.tech/) est une plateforme d'engagement client spécialisée dans la gamification, le contenu interactif, les concours, les prix et la fidélisation.

_Cette intégration est maintenue par Komo._

## À propos de l'intégration {#about-the-integration}

L'intégration de Braze et Komo vous permet de collecter des données first-party et zero-party via les Komo Engagement Hubs. Ces hubs sont des microsites dynamiques qui offrent du contenu interactif et des fonctionnalités de gamification. Les données utilisateur collectées à partir de ces hubs sont ensuite transmises à l'API Braze.

{% multi_lang_include partners/extensions/landing_pages/komo_integration_bullets.md %}

## Prérequis {#prerequisites}

| Condition | Description |
| ----------- | ----------- |
| Compte Komo | Vous aurez besoin d'un compte Komo actif pour tirer parti de ce partenariat. Rendez-vous sur [Komo](https://komo.tech/) pour commencer un essai dès maintenant. |
| Clé API REST Braze | Une clé API REST Braze avec les permissions `users.track`. <br><br> Celle-ci peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés API**. |
| Endpoint REST Braze | [L'URL de votre endpoint REST]({{site.baseurl}}/developer_guide/rest_api/basics#endpoints). Votre endpoint dépendra de l'URL Braze de votre instance.<br><br>Par exemple, cela devrait ressembler à : https://rest.iad-03.braze.com |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prérequis" }

## Cas d'usage {#use-cases}

{% tabs local %}
{% tab Capture de données - Soumission de formulaire %}

Lorsqu'un utilisateur soumet un formulaire de capture de données personnalisable dans Komo, les champs Komo mappés dans l'intégration Braze sont transmis à Braze via l'appel API `/users/track/`.

Les formulaires de capture de données se trouvent au début ou à la fin des Cards.

{% endtab %}
{% tab Étude de marché - Bientôt disponible %}

Komo permet également de transmettre les données d'étude de marché collectées lorsqu'un utilisateur répond à une question de quiz, un sondage, un test de personnalité, un swiper, et autres. Ces données vous permettront d'enrichir le profil d'un utilisateur au-delà des données collectées via les soumissions de formulaires.

{% endtab %}
{% endtabs %}

## Intégration {#integration}

### Étape 1 : Publier un Hub d'engagement Komo et une carte {#step-1-publish-a-komo-engagement-hub-and-card}

Vous devez publier un Hub Komo contenant au moins une carte avec un formulaire de collecte de données. Une fois publié, vous pouvez tester l'expérience utilisateur de bout en bout et vérifier que l'intégration fonctionne correctement.

![Hub Komo.]({% image_buster /assets/img/Braze Komo Images v2/Braze-Komo-Step1.png %})

### Étape 2 : Ajouter l'application connectée Braze {#step-2-add-the-braze-connected-app}

Dans Komo, accédez à l'onglet **Company Settings**, puis sélectionnez la section **Connected Apps**.

Ensuite, recherchez l'intégration Braze dans la liste et sélectionnez le bouton **Connect** pour activer l'intégration.

![Connexion de l'intégration Braze.]({% image_buster /assets/img/Braze Komo Images v2/Braze-Komo-Step2a.png %}){: style="max-width:50%;"}

![Connexion de l'intégration Braze, étape 2b.]({% image_buster /assets/img/Braze Komo Images v2/Braze-Komo-Step2b.png %})

#### Configurer l'intégration via un workflow {#configure-the-integration-via-a-workflow}

Vous devez maintenant configurer un workflow, au sein d'un Workspace, d'un Site ou d'une carte, pour synchroniser les données vers Braze.

Le choix de définir le workflow au niveau de l'ensemble du Workspace, d'un Site (qui contient plusieurs cartes) ou d'une seule carte dépend de si vous souhaitez que le workflow se déclenche sur plusieurs cartes ou Campaigns.

Après avoir créé un workflow, définissez votre déclencheur, recherchez Braze dans le menu des étapes et ajoutez l'étape « Track User ».

![Configuration de Track User.]({% image_buster /assets/img/Braze Komo Images v2/Braze-Komo-Step3a.png %})

À partir de là, configurez les événements, les attributions et les abonnements que vous souhaitez synchroniser de Komo vers Braze.

![Liste des blocs de contenu.]({% image_buster /assets/img/Braze Komo Images v2/Braze-Komo-Step3b.png %})

## Utiliser l'intégration {#using-the-integration}

Maintenant que votre intégration est opérationnelle, vous pouvez surveiller chaque exécution dans l'onglet Workflow Runs.