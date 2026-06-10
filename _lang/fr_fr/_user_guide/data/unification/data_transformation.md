---
nav_title: Transformation des données
article_title: Transformation des données
page_order: 2
layout: dev_guide
guide_top_header: "Transformation des données"
guide_top_text: "La Transformation des données Braze vous permet de créer et de gérer des intégrations webhook pour automatiser le flux de données depuis des plateformes externes vers Braze. Ces données utilisateur nouvellement intégrées peuvent ensuite servir à des cas d'utilisation marketing encore plus sophistiqués. La Transformation des données Braze peut accélérer l'intégration de vos données, même si vous n'avez que très peu d'expérience en matière de codage, et peut aider à remplacer la dépendance de votre équipe à l'égard des appels d'API manuels, des outils d'intégration tiers, ou même des plateformes de données client."
page_type: landing
description: "Cette page d'accueil regroupe des articles sur la Transformation des données Braze, notamment sur la façon de créer une transformation et sur les cas d'utilisation."
alias: /data_transformation/

guide_featured_title: "Articles de la section"
guide_featured_list:
  - name: Créer une transformation
    link: /docs/user_guide/data/unification/data_transformation/creating_a_transformation
    image: /assets/img/braze_icons/flip-forward.svg
  - name: Cas d'utilisation
    link: /docs/user_guide/data/unification/data_transformation/use_cases
    image: /assets/img/braze_icons/users-01.svg
---

## Fonctionnement {#how-it-works}

De nombreuses plateformes modernes disposent de « webhooks », ou notifications API en temps réel, pour envoyer des informations sur un nouvel événement ou de nouvelles données d'une plateforme à une autre. La Transformation des données fournit :

* Une adresse URL Braze pour recevoir ces webhooks.
* La possibilité de transformer le payload du webhook avec du code JavaScript pour créer des requêtes valides vers divers endpoints de l'API Braze, notamment `/users/track` ou `/catalogs`. Par exemple, pour la destination `/users/track`, vous pouvez choisir les informations à utiliser à partir du webhook et la manière dont vous souhaitez que les données soient représentées sur les profils utilisateur Braze en tant qu'attributs utilisateur, événements ou achats.
* La journalisation pour effectuer l'assurance qualité, la résolution des problèmes et le suivi des performances de vos transformations.

Le résultat final est une intégration webhook qui connecte une plateforme source de votre choix en transformant ses webhooks en mises à jour Braze.

{% details More on webhooks %}
Les webhooks sont des notifications en temps réel envoyées via une requête HTTP POST à une destination spécifique. Les webhooks sont souvent utilisés pour envoyer des données d'un point à un autre : le webhook peut transmettre des données sur une action qui s'est produite et sur les personnes impliquées dans cette action.

Par exemple, une plateforme d'enquête peut envoyer un webhook à une destination de votre choix chaque fois qu'une réponse à un formulaire en ligne est reçue. Ou encore, une plateforme de service client peut envoyer un webhook à une destination de son choix chaque fois qu'un ticket de service client est créé.
{% enddetails %}

## Niveaux de la Transformation des données {#data-transformation-tiers}

Le tableau suivant décrit les différences entre la version gratuite et la version pro de la Transformation des données.

| Domaine | Version gratuite | Data Transformation Pro |
|----|----|----|
| Transformations actives | Jusqu'à 5 par entreprise | Jusqu'à 55 par entreprise |
| Par mois | 300 000 requêtes entrantes par mois | 10 300 000 requêtes entrantes par mois |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Niveaux de la Transformation des données" }

{% alert important %}
Pour demander une mise à niveau vers Data Transformation Pro, contactez votre gestionnaire de compte Braze ou sélectionnez le bouton **Request Upgrade** dans le tableau de bord de Braze.
{% endalert %}

### Limites de débit {#rate-limits}

La limite de débit pour la Transformation des données Braze est de 1 000 requêtes entrantes par minute et par espace de travail. Si vous disposez de Data Transformation Pro et que vous avez besoin d'une limite de débit plus élevée, contactez votre gestionnaire de compte Braze.

## Foire aux questions {#frequently-asked-questions}

### Qu'est-ce qui est synchronisé avec la Transformation des données Braze ? {#what-gets-synced-with-braze-data-transformation}

Toutes les données que la plateforme externe met à disposition dans un webhook peuvent être synchronisées avec Braze. Plus une plateforme externe envoie de données via des webhooks, plus vous disposez d'options pour choisir ce qui est synchronisé.

### Je suis marketeur. Ai-je besoin de ressources de développement pour utiliser la Transformation des données Braze ? {#im-a-marketer-do-i-need-developer-resources-to-use-braze-data-transformation}

Bien que nous serions ravis que les développeurs utilisent également cette fonctionnalité, vous n'avez pas besoin d'en être un pour l'utiliser ! Les marketeurs peuvent également mettre en place des transformations sans faire appel à des développeurs.

### Puis-je quand même utiliser la Transformation des données Braze si ma plateforme externe ne fournit qu'une adresse e-mail ou un numéro de téléphone comme identifiant ? {#can-i-still-use-braze-data-transformation-if-my-external-platform-only-gives-an-email-address-or-phone-number-as-an-identifier}

Oui. Vous pouvez faire en sorte que vos transformations mettent à jour l'endpoint `/users/track` avec l'[adresse e-mail ou le numéro de téléphone comme identifiant]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#example-request-for-updating-a-user-profile-by-email-address).

Pour ce faire, utilisez `email` ou `phone` comme propriété d'identification dans le code de transformation au lieu de `external_id` ou `braze_id`. L'exemple de [code de transformation]({{site.baseurl}}/user_guide/data/unification/data_transformation/use_cases/#example-transformation-code) utilise cette fonctionnalité.

{% alert note %}
Les utilisateurs de l'accès anticipé de la Transformation des données Braze ayant commencé avant avril 2023 connaissent peut-être la fonction `get_user_by_email` qui aidait dans ce cas d'utilisation. Cette fonction est désormais obsolète.
{% endalert %}

### La Transformation des données Braze enregistre-t-elle des points de données ? {#does-braze-data-transformation-log-data-points}

Oui, dans la plupart des cas. La Transformation des données Braze finit par créer un appel `/users/track` qui écrit les attributs, les événements et les achats que vous souhaitez. Ces derniers enregistrent des points de données de la même manière que si l'appel `/users/track` était effectué de manière indépendante. Vous contrôlez le nombre de points de données enregistrés en fonction de la façon dont vous écrivez votre transformation.

### Comment puis-je obtenir de l'aide pour la mise en place de mon cas d'utilisation ou pour mon code de transformation ? {#how-can-i-get-help-setting-up-my-use-case-or-with-my-transformation-code}

Contactez votre gestionnaire de compte Braze pour toute assistance supplémentaire.