---
nav_title: Segments
article_title: Segments
page_order: 3
layout: dev_guide
guide_top_header: "Segments"
guide_top_text: "La segmentation de l'audience est essentielle à une stratégie marketing efficace : elle vous évite de sur-cibler, d'importuner ou de manquer une connexion potentielle avec un client. Consultez les articles suivants pour découvrir comment segmenter et filtrer votre audience pour en tirer le meilleur parti (pour vous comme pour eux)."
descriptions: "La segmentation de l'audience est essentielle à une stratégie marketing efficace : elle vous évite de sur-cibler, d'importuner ou de manquer une connexion potentielle avec un client. Consultez cette page d'accueil pour découvrir comment segmenter et filtrer votre audience pour en tirer le meilleur parti (pour vous comme pour eux)."
search_rank: 4
tool: Segments
page_type: landing
description: "Cette page d'accueil couvre les articles sur la segmentation au sein des campagnes du tableau de bord. Vous y trouverez des informations sur la configuration d'un segment, les filtres, les entonnoirs, les statistiques, les extensions et bien plus encore."

guide_featured_title: "Articles de la section"
guide_featured_list:
  - name: Créer un segment
    link: /docs/user_guide/audience/segments/creating_a_segment
    image: /assets/img/braze_icons/pie-chart-01.svg
  - name: Gérer les segments
    link: /docs/user_guide/audience/segments/managing_segments
    image: /assets/img/braze_icons/edit-05.svg
  - name: Filtres de segmentation
    link: /docs/user_guide/audience/segments/segmentation_filters
    image: /assets/img/braze_icons/flag-02.svg
  - name: Données de segment
    link: /docs/user_guide/audience/segments/segment_data
    image: /assets/img/braze_icons/bar-chart-01.svg
  - name: Extensions de segments
    link: /docs/user_guide/audience/segments/segment_extension
    image: /assets/img/braze_icons/users-01.svg
  - name: Statistiques des segments
    link: /docs/user_guide/audience/segments/segment_insights
    image: /assets/img/braze_icons/pie-chart-01.svg

guide_menu_title: "Autres articles"
guide_menu_list:
  - name: Ciblage par localisation
    link: /docs/user_guide/audience/segments/location_targeting
    image: /assets/img/braze_icons/marker-pin-06.svg
  - name: Expressions régulières
    link: /docs/user_guide/audience/segments/regex
    image: /assets/img/braze_icons/search-sm.svg
  - name: Mesurer la taille d'un segment
    link: /docs/user_guide/audience/segments/measuring_segment_size
    image: /assets/img/braze_icons/pie-chart-02.svg
  - name: "Cas d'utilisation : segmenter avec des attributs personnalisés imbriqués"
    link: /docs/user_guide/audience/segments/segment_with_nested_custom_attributes
    image: /assets/img/braze_icons/dataflow-02.svg
  - name: Résolution des problèmes
    link: /docs/user_guide/audience/segments/troubleshooting
    image: /assets/img/braze_icons/annotation-question.svg

---

## À propos des segments Braze {#about-braze-segments}

Dans Braze, les segments sont des groupes dynamiques d'utilisateurs qui correspondent à des critères spécifiques que vous définissez, tels que des attributs utilisateur, des comportements utilisateur et des événements personnalisés. Vous pouvez affiner vos critères en imbriquant des segments dans d'autres segments et en appliquant des fonctionnalités supplémentaires, réduisant ainsi la portée de votre audience afin d'envoyer du contenu hautement personnalisé et engageant aux bons utilisateurs.

Vous pouvez créer autant de segments que vous le souhaitez pour cibler vos utilisateurs. Explorez différentes combinaisons de fonctionnalités de segments et de filtres de segmentation pour découvrir des façons créatives d'exploiter vos données utilisateur, et débloquez de nouvelles manières d'envoyer des messages pertinents à vos utilisateurs et d'augmenter l'engagement.

Consultez les cas d'utilisation ci-dessous pour un aperçu de la façon dont les segments Braze peuvent vous aider à cibler vos utilisateurs.

### Cas d'utilisation {#use-cases}

- **Messages de bienvenue :** Segmentez les nouveaux utilisateurs afin de leur envoyer des e-mails d'onboarding ou des messages in-app qui leur présentent votre application.
- **Récompenses de fidélité :** Segmentez les utilisateurs en fonction de leur fréquence d'achat, de l'anniversaire de leur adhésion ou d'autres jalons, et envoyez des offres exclusives ou des récompenses à vos utilisateurs les plus fidèles.
- **Déclencheurs comportementaux :** Segmentez les utilisateurs en fonction de leurs actions, comme l'abandon d'un panier lors du paiement, pour déclencher des messages in-app ou des notifications push.
- **Recommandations de produits :** Segmentez les utilisateurs ayant acheté des produits spécifiques et envoyez-leur des recommandations pour des produits complémentaires ou de gamme supérieure.
- **Test A/B :** Segmentez les utilisateurs pour effectuer des tests A/B avec différents messages, lignes d'objet ou contenus afin de déterminer ce qui résonne le mieux auprès des utilisateurs selon leur âge, leur genre et d'autres attributs.

#### Cas d'utilisation des extensions de segments {#segment-extension-use-cases}

Vous pouvez affiner davantage vos segments en utilisant les [extensions de segments]({{site.baseurl}}/user_guide/audience/segments/segment_extension) pour cibler les utilisateurs en fonction d'événements personnalisés ou de comportements d'achat stockés pendant toute la durée de vie de leur profil utilisateur.

- **Achats historiques :** Segmentez les utilisateurs selon qu'ils ont acheté une couleur spécifique d'un produit spécifique au moins deux fois au cours des deux dernières années.
- **Événements et interactions avec les messages :** Segmentez les utilisateurs selon qu'ils ont effectué un achat au cours des trente derniers jours et ont également interagi avec un message in-app spécifique.
- **Interrogation des données :**
  - **Interroger Snowflake :** Segmentez les utilisateurs avec des données combinées provenant de Braze et de sources externes, telles qu'un CRM ou un entrepôt de données, en utilisant les [extensions de segments SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments) pour interroger Snowflake.
  - **Synchroniser depuis un entrepôt de données :** Segmentez les utilisateurs avec des données directement synchronisées depuis votre entrepôt de données ou votre système de stockage de fichiers vers Braze en utilisant les [extensions de segments CDI]({{site.baseurl}}/user_guide/audience/segments/segment_extension/cdi_segments).