---
nav_title: octobre
page_order: 2
noindex: true
page_type: update
description: "Cet article contient les notes de version d'octobre 2021."
---

# Octobre 2021 {#october-2021}

## Tableau de bord d'utilisation des points de données {#data-points-usage-dashboard}

Utilisez le tableau de bord **Utilisation totale des points de données** pour suivre le rythme d'utilisation de vos points de données par rapport à votre allocation contractuelle. Ce tableau de bord fournit des informations sur votre contrat, le cycle de facturation en cours, les données de facturation de l'entreprise et les données de facturation de l'espace de travail. Pour plus d'informations, consultez la section [Facturation]({{site.baseurl}}/user_guide/onboarding_with_braze/subscription_and_usage#total-data-points-dashboard).

## Modification de la régénération des extensions de segments {#change-to-segment-extension-regeneration}

À partir du 1er février 2022, le paramètre permettant de régénérer les extensions quotidiennement sera automatiquement désactivé pour les [extensions de segments]({{site.baseurl}}/user_guide/audience/segments/segment_extension) inutilisées. Braze définit une extension non utilisée comme une extension répondant aux critères suivants :

- Non utilisée dans des campagnes, Canvas ou segments actifs
- Non utilisée dans des campagnes, Canvas ou segments inactifs (brouillon, arrêtés, archivés)
- Non modifiée depuis plus de 7 jours

Braze informera le contact de l'entreprise ainsi que la personne ayant créé l'extension lorsque ce paramètre sera désactivé. L'option permettant de régénérer les extensions quotidiennement peut être réactivée à tout moment.

## Guides de déploiement avancés Android {#android-advanced-implementation-guides}

### Content Cards

Ce [guide de déploiement]({{site.baseurl}}/developer_guide/content_cards) optionnel et avancé couvre les considérations de code des Content Cards, trois cas d'usage personnalisés créés par notre équipe, des extraits de code associés et des conseils sur l'enregistrement des impressions, des clics et des fermetures.

### Messages in-app {#in-app-messaging}

Ce [guide de déploiement]({{site.baseurl}}/developer_guide/in_app_messages/customization/?sdktab=android) optionnel et avancé couvre les considérations de code pour les messages in-app, trois cas d'usage personnalisés créés par notre équipe et des extraits de code associés.

### Notifications push {#push-notifications}

Ce [guide de déploiement]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android) optionnel et avancé couvre les moyens de tirer parti d'une sous-classe personnalisée de `FirebaseMessagingService` pour exploiter au mieux vos notifications push. Il comprend un cas d'usage personnalisé créé par notre équipe, des extraits de code associés et des conseils sur l'enregistrement des analyses.

## Nouveaux partenariats Braze {#new-braze-partnerships}

### Adobe - Plateforme de données client {#adobe-customer-data-platform}

Construite sur l'Adobe Experience Platform, la plateforme de données client en temps réel d'Adobe (real-time CDP) aide les entreprises à rassembler des données connues et anonymes provenant de plusieurs sources d'entreprise afin de créer des profils clients pouvant être utilisés pour offrir des expériences client personnalisées sur tous les canaux et appareils en temps réel.

L'intégration de Braze et du CDP [Adobe]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/adobe) permet aux marques de connecter et de mapper leurs données Adobe (attributs personnalisés et segments) vers Braze en temps réel. Les marques peuvent ensuite exploiter ces données pour offrir des expériences personnalisées et ciblées à ces utilisateurs.

### Shopify - eCommerce

[Shopify]({{site.baseurl}}/partners/shopify) est une entreprise mondiale de commerce de premier plan offrant des outils fiables pour démarrer, développer, commercialiser et gérer une entreprise de vente au détail de toute taille. L'intégration entre Braze et Shopify permet aux marques de connecter leur boutique Shopify de façon fluide avec Braze pour transmettre certains webhooks Shopify dans Braze. Tirez parti des stratégies cross-canal et des Canvas de Braze pour recibler vos utilisateurs avec des messages sur les paniers abandonnés afin de les inciter à finaliser leur achat, ou reciblez les utilisateurs en fonction de leurs achats précédents.