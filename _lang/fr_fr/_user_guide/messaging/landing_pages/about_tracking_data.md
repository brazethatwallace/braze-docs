---
nav_title: À propos du suivi des données
article_title: À propos du suivi des données des pages d'accueil
description: "Découvrez le suivi et les données anonymisées pour les pages d'accueil dans Braze."
page_order: 10
alias: /landing_pages/data_tracking/
---

# À propos du suivi des données des pages d'accueil {#about-landing-page-tracking-data}

> Découvrez le suivi et les données anonymisées pour les pages d'accueil dans Braze.

## Méthodes de suivi {#tracking-methods}

### SDK Web {#web-sdk}

Le SDK Web de Braze est initialisé lorsqu'un utilisateur soumet un formulaire sur une page d'accueil. Avant la soumission du formulaire, aucune donnée personnelle n'est collectée et le SDK ne suit pas activement les utilisateurs. Une fois l'initialisation terminée, le SDK ne stocke aucune donnée dans le navigateur (comme les cookies, le stockage local ou autres).

Le SDK Web de Braze est initialisé immédiatement lorsqu'un utilisateur accède à la page d'accueil via un lien généré par une étiquette Liquid {% raw %}`{% landing_page_url %}`{% endraw %} dans un message Braze.

Lorsqu'un formulaire est soumis, le SDK collecte les données suivantes :

- Événement de soumission de formulaire (nom de l'événement et heure de soumission)
- Données spécifiées par votre équipe dans le formulaire (comme le nom, l'e-mail et le numéro de téléphone)
- Heure de début de session
- ID de l'appareil (un identifiant unique qui est généré, mais non stocké, pour l'appareil)
- Pays déterminé par l'adresse IP

### Données anonymisées {#anonymized-data}

Avant qu'un utilisateur ne soumette un formulaire, les données suivies sur une page d'accueil consistent uniquement en des informations anonymisées et non identifiables. Il s'agit d'indicateurs agrégés standard de sites web, comme le nombre de pages vues (impressions) et de clics qu'une page d'accueil reçoit.

Étant donné que ces données ne sont pas liées à des utilisateurs identifiables, elles ne peuvent pas être utilisées pour recibler ou suivre le comportement individuel des utilisateurs.

## Fusion des profils utilisateur en double {#merging-duplicate-user-profiles}

Braze ne fusionne pas automatiquement les utilisateurs en fonction d'attributs, tels que l'e-mail ou le téléphone, lorsqu'un formulaire de page d'accueil est soumis. Si un formulaire est soumis avec un e-mail ou un numéro de téléphone correspondant à un profil utilisateur existant, Braze crée un profil utilisateur distinct.

Pour fusionner les profils utilisateur en double, vous pouvez :

- Déclencher l'[endpoint `/users/merge`]({{site.baseurl}}/api/endpoints/user_data/post_users_merge) lorsqu'un formulaire de page d'accueil est soumis afin de fusionner le nouveau profil avec un profil existant.
- Planifier une [fusion en masse]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users#bulk-merging) pour fusionner périodiquement les profils en double en fonction d'identifiants correspondants.