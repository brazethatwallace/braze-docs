---
nav_title: décembre
page_order: 0
noindex: true
page_type: update
description: "Cet article contient les notes de version de décembre 2021."
alias: "/help/release_notes/2022/january/"
---
# Décembre 2021 {#december-2021}

## Mise à jour de l'endpoint d'exportation des utilisateurs par segment {#update-to-export-users-by-segment-endpoint}

À partir de décembre 2021, les modifications suivantes entreront en vigueur pour l'endpoint [Exporter les utilisateurs par segment]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/) :

1. Le champ `fields_to_export` dans cette requête API sera requis. L'option permettant d'exporter tous les champs par défaut sera supprimée.
2. Les champs pour `custom_events`, `purchases`, `campaigns_received` et `canvases_received` contiendront uniquement les données des 90 derniers jours.

## Nouvelles propriétés pour les événements d'engagement lié aux messages Currents {#new-properties-for-currents-message-engagement-events}

De nouvelles propriétés ont été ajoutées pour certains [événements d'engagement lié aux messages]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/). Cette mise à jour s'applique aux événements d'engagement lié aux messages Currents suivants et à tous les partenaires qui les utilisent :

- Ajout de `LINK_ID`, `LINK_ALIAS` à :
  - Clic sur e-mail (toutes les destinations)
- Ajout de `USER_AGENT` à :
  - Ouverture d'e-mail
  - Clic sur e-mail
  - E-mail marqué comme spam
- Ajout de `MACHINE_OPEN` à :
  - Ouverture d'e-mail

## Nouvelle étiquette de personnalisation Liquid {#new-liquid-personalization-tag}

Nous prenons désormais en charge le ciblage des utilisateurs qui ont activé les notifications push au premier plan sur leur appareil, via les étiquettes Liquid suivantes :

{% raw %}
- `{{most_recently_used_device.${foreground_push_enabled}}}`
- `{{targeted_device.${foreground_push_enabled}}}`
{% endraw %}

Pour plus d'informations, consultez les [étiquettes de personnalisation prises en charge]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags/).

## À propos des webhooks {#about-webhooks}

Les webhooks sont des outils puissants et flexibles, mais ils peuvent être un peu déroutants. Si vous vous demandez ce que sont les webhooks et comment les utiliser dans Braze, consultez notre nouvel article [À propos des webhooks]({{site.baseurl}}/about_webhooks/).

## Amazon Personalize

Amazon Personalize, c'est comme si vous disposiez de votre propre système de recommandation Amazon machine learning disponible en permanence. Fort de plus de 20 ans d'expérience en matière de recommandation, Amazon Personalize vous permet d'améliorer l'engagement client en proposant des recommandations personnalisées en temps réel sur les produits et le contenu, ainsi que des promotions marketing ciblées.

Si vous souhaitez en savoir plus, consultez notre nouvel article [Amazon Personalize]({{site.baseurl}}/partners/message_personalization/dynamic_content/personalized_recommendations/amazon_personalize/) pour comprendre les cas d'utilisation proposés par Amazon Personalize, les données avec lesquelles il fonctionne, comment configurer le service et comment l'intégrer avec Braze.

## Nouveaux partenariats Braze {#new-braze-partnerships}

### Yotpo – eCommerce

L'intégration de [Yotpo]({{site.baseurl}}/partners/message_personalization/dynamic_content/visual_and_interactive_content/yotpo/) et Braze vous permet de récupérer et d'afficher dynamiquement les évaluations par étoiles, les meilleures critiques et le contenu visuel généré par les utilisateurs sur les produits dans les e-mails et autres canaux de communication au sein de Braze. Vous pouvez également inclure les données de fidélisation des clients dans les e-mails et autres méthodes de communication pour créer une interaction plus personnalisée, ce qui stimule les ventes et la fidélisation.

### Zeotap – Plateforme de données client {#zeotap-customer-data-platform}

Avec l'intégration de [Zeotap]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/zeotap/) et Braze, vous pouvez étendre l'échelle et la portée de vos campagnes en synchronisant les segments de clients Zeotap pour mapper les données utilisateur Zeotap aux comptes utilisateurs Braze. Vous pouvez ensuite exploiter ces données pour offrir des expériences personnalisées et ciblées à vos utilisateurs.