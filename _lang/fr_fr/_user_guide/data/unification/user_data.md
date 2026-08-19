---
nav_title: Données utilisateur
article_title: Données des utilisateurs dans Braze
page_order: 4
layout: dev_guide
guide_top_header: "Données des utilisateurs dans Braze"
guide_top_text: "Avant de finaliser votre déploiement de Braze, assurez-vous que vos équipes marketing et développement ont échangé sur vos objectifs marketing. Il est utile de partir de ces objectifs et de raisonner à rebours pour décider quelles données suivre et comment les suivre avec Braze."

page_type: landing
description: "Cette page d'accueil regroupe les articles relatifs à la collecte de données utilisateur. Vous y trouverez des ressources sur les définitions d'archivage, l'importation d'utilisateurs, le cycle de vie du profil utilisateur, les cas d'usage, les bonnes pratiques, et plus encore."

guide_featured_title: "Articles de la section"
guide_featured_list:
  - name: Collecte de données SDK
    link: /docs/user_guide/data/unification/user_data/sdk_data_collection
    image: /assets/img/braze_icons/bar-chart-01.svg
  - name: Cycle de vie du profil utilisateur
    link: /docs/user_guide/data/unification/user_data/user_profile_lifecycle
    image: /assets/img/braze_icons/refresh-ccw-05.svg
  - name: Cas d'usage de collecte de données
    link: /docs/user_guide/data/unification/user_data/collection_use_case
    image: /assets/img/braze_icons/data.svg
  - name: Bonnes pratiques de collecte
    link: /docs/user_guide/data/unification/user_data/best_practices
    image: /assets/img/braze_icons/thumbs-up.svg
  - name: Importer des utilisateurs
    link: /docs/user_guide/audience/manage_audience/import_users
    image: /assets/img/braze_icons/users-01.svg
  - name: Supprimer des utilisateurs
    link: /docs/user_guide/audience/manage_audience/user_profiles/delete_users
    image: /assets/img/braze_icons/edit-05.svg
  - name: Utilisateurs anonymes
    link: /docs/user_guide/data/unification/user_data/user_profile_lifecycle/anonymous_users
    image: /assets/img/braze_icons/user-circle.svg
  - name: Codes des langues
    link: /docs/user_guide/data/unification/user_data/language_codes
    image: /assets/img/braze_icons/globe-04.svg
---

<br>

{% alert important %}
Braze bloque les profils utilisateur (« utilisateurs fictifs ») ayant plus de 5 000 000 de sessions, plus de 20 000 noms d'événements personnalisés distincts ou plus de 20 000 noms de produits distincts dans les achats, car ils résultent généralement d'une mauvaise intégration. Lorsqu'un profil est bloqué, Braze cesse d'ingérer toutes les données entrantes pour ce profil, qu'elles proviennent des SDK ou de la REST API. Si vous constatez que cela s'est produit pour un utilisateur légitime, contactez votre gestionnaire de compte Braze.
{% endalert %}

<br>