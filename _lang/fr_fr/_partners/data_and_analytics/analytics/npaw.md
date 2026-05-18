---
nav_title: NPAW
article_title: NPAW
alias: /partners/npaw/
description: "Cet article de référence décrit le partenariat entre Braze et NPAW, une plateforme d'analyse de données intelligente qui fournit des informations exploitables aux principaux professionnels des médias en ligne."
page_type: partner
search_tag: Partner
hidden: true

---

# NPAW

> [NPAW](https://nicepeopleatwork.com/), également connue sous le nom de _Nice People at Work_, est une plateforme d'analyse de données intelligente qui fournit des informations exploitables aux principaux professionnels des médias en ligne. Grâce à la suite d'outils YOUBORA de NPAW, les clients de Braze peuvent désormais tirer parti d'une intelligence artificielle prédictive et robuste pour mieux comprendre le comportement des clients et stimuler l'engagement sur toutes les plateformes.

# Conditions préalables {#prerequisites}

| Exigence   | Origine | Description |
| --------------|------|-------------|
| Clé API YOUBORA | [Paramètres YOUBORA](https://youbora.nicepeopleatwork.com/users/login) | Une clé API générée lors de l'inscription de l'utilisateur et qui se trouve dans l'onglet **Settings**. |
| ID | [Paramètres Braze](https://dashboard.braze.com/sign_in) | YOUBORA vous permet de lier le logiciel à Braze via un ***Braze ID***, un ***external User ID*** ou un ***User ID***. |
| Endpoint | [Paramètres Braze](https://dashboard.braze.com/sign_in) | Un endpoint URL entièrement personnalisable et configurable via votre tableau de bord de Braze. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

# Intégration analytique {#analytics-integration}

## Accès à la page des intégrations {#accessing-the-integrations-page}

Après vous être connecté à votre compte de la suite d'outils YOUBORA, accédez à la page Integrations en sélectionnant l'option **Integrations** dans le menu déroulant du compte.

![Menu déroulant NPAW]({% image_buster /assets/img/npaw_dropdown.png %})

## Configuration de votre intégration {#configuring-your-integration}

Une fois que vous avez accédé à la page d'intégration, faites défiler la page vers le bas jusqu'à voir l'option d'intégration **Braze**. Après avoir cliqué dessus, celle-ci s'agrandira et proposera un certain nombre de paramètres requis à remplir :

![Intégration NPAW]({% image_buster /assets/img/npaw_integration.png %})

Remplissez les champs avec les informations appropriées recueillies dans la section des conditions préalables, où :
* **Connector Name** est une chaîne de caractères **alphanumérique** qui sera utilisée pour faire référence à cette intégration à l'avenir. Cette valeur peut être définie comme vous le souhaitez tant qu'elle ne contient **que** des lettres et des chiffres.
* **User ID** est l'identifiant précédemment choisi pour associer votre logiciel YOUBORA à votre compte Braze. Par exemple, si vous choisissez d'effectuer le lien via votre **Braze ID**, sélectionnez **Braze ID** dans la liste déroulante pour attribuer la valeur au champ approprié.
* **API Key** est la clé API de votre suite d'outils YOUBORA qui se trouve dans la section **API** sous **Settings**.
* **Endpoint** est l'endpoint URL personnalisable précédemment configuré dans votre tableau de bord de Braze.

Une fois tous les champs remplis, il suffit de cliquer sur le bouton **Connect** pour établir une connexion et enregistrer les modifications apportées.

## Utilisation de votre intégration NPAW {#using-your-npaw-integration}

Une fois que vous avez terminé de configurer votre intégration avec Braze, accédez au produit **Users** et sélectionnez le **Sample Manager** dans le **Sections Manager**.

Après avoir créé un échantillon dans le **Sample Manager**, vous pouvez maintenant cliquer sur l'icône à trois points sur le côté droit pour envoyer tous les utilisateurs de votre échantillon vers Braze.

![Gestionnaire d'échantillons NPAW]({% image_buster /assets/img/npaw_sample_manager.png %})

Désormais, une fois que vous avez envoyé vos utilisateurs vers Braze, vous pouvez passer à l'action et concentrer vos Campaigns sur des segments d'utilisateurs pour réengager les utilisateurs inactifs, contacter vos utilisateurs les plus fidèles ou effectuer toute action sur n'importe quel segment d'utilisateurs !