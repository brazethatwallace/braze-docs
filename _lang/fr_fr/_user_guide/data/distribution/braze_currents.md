---
page_order: 1
nav_title: Currents
article_title: Currents

layout: dev_guide

page_type: landing
description: "Cette page d'accueil répertorie les articles sur le produit de données Braze appelé Currents. Vous y trouverez des informations sur la configuration de Currents, les partenaires disponibles, la sémantique de distribution, les glossaires d'événements, et plus encore."
tool: currents
search_rank: 9
guide_top_header: "Braze Currents"
guide_top_text: "Comprendre l'impact de votre stratégie d'engagement est essentiel pour orienter l'itération et l'optimisation de vos communications avec vos utilisateurs. Pour intégrer étroitement ces précieuses données d'engagement au reste de vos opérations et contribuer à amplifier votre investissement dans la science des données, la plateforme Braze assure le suivi d'un large éventail de données d'événements issues de votre intégration à des fins d'analyse, de reciblage et d'autres cas d'utilisation ailleurs dans vos propres systèmes. <br> <br>L'outil Currents est un flux de données en temps réel de vos événements d'engagement. Il constitue l'exportation la plus robuste et la plus granulaire de la plateforme Braze. Il fournit vos données dans un type de fichier Avro à l'un de nos nombreux <a href='/docs/user_guide/data/distribution/braze_currents/setting_up_currents/available_partners'>partenaires de données</a>, vous permettant d'utiliser les données uniques et précieuses que Braze crée pour alimenter vos efforts d'aide à la décision (BI) et d'analytique dans d'autres plateformes de premier ordre."

guide_featured_title: "Articles de la section"
guide_featured_list:
  - name: Configurer Currents
    link: /docs/user_guide/data/distribution/braze_currents/setting_up_currents
    image: /assets/img/braze_icons/building-01.svg
  - name: Glossaire des événements Currents
    link: /docs/user_guide/data/distribution/braze_currents/event_glossary
    image: /assets/img/braze_icons/data.svg
  - name: Cas d'utilisation
    link: /docs/user_guide/data/distribution/braze_currents/use_cases
    image: /assets/img/braze_icons/expand-05.svg
  - name: FAQ
    link: /docs/user_guide/data/distribution/braze_currents/faq
    image: /assets/img/braze_icons/annotation-question.svg
---

## Fonctionnalités de Currents {#currents-capabilities}

Currents vous permet de :
* Diffuser les données d'événements Braze vers un entrepôt de données ou vers l'un de nos [partenaires d'analyse]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/available_partners) pour une analyse approfondie.
* Diffuser les données d'événements Braze en continu pour alimenter des outils d'aide à la décision, des algorithmes de machine learning, et bien plus encore.
* Acheminer les données d'événements Braze vers divers autres systèmes à l'aide de [Tealium]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/tealium/tealium), [Segment]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/segment/segment) ou [mParticle]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/mparticle/mparticle_for_currents).

Les possibilités offertes par les données d'événements accessibles via Currents sont nombreuses. [Braze utilise également Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/use_cases/how_braze_uses_currents) !

## Modèle de distribution des données Currents {#currents-data-distribution-model}

Currents utilise des pools de droits d'accès pour contrôler la création de connecteurs et le suivi facultatif des événements.

- Les **droits d'accès aux événements d'engagement** sont nécessaires pour chaque connecteur Currents standard que vous créez.
- Les **droits d'accès aux événements de comportement client** sont nécessaires lorsque vous activez l'option **Track Customer Behavior and User Events** sur un connecteur.
- Les **droits d'accès aux profils utilisateur et aux attributs** sont nécessaires lorsque vous activez l'option **Track user profiles and attributes** sur un connecteur.

Les connecteurs Currents de test utilisent une limite de test distincte et ne consomment pas les droits d'accès aux connecteurs standard.

Si vous atteignez une limite de droits d'accès, consultez la section [Résolution des problèmes de configuration de Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents#troubleshooting) et la [FAQ sur Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/faq), ou contactez votre gestionnaire de compte.

## Comment accéder à Currents {#how-to-access-currents}

Un connecteur Currents est déjà inclus dans bon nombre de nos offres de niveau professionnel et entreprise. Si vous souhaitez utiliser Currents, contactez votre gestionnaire de compte. Votre gestionnaire de compte et nos spécialistes des données peuvent vous accompagner dans la [configuration et l'intégration de Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents).

<br><br>