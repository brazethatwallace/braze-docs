---
nav_title: juin
page_order: 6
noindex: true
page_type: update
description: "Cet article contient les notes de version de juin 2021."
---

# Juin 2021 {#june-2021}

## Campaigns d'e-mails transactionnels {#transactional-email-campaigns}

Les e-mails transactionnels sont ceux envoyés pour faciliter une transaction convenue entre un expéditeur et un destinataire. La [Campaign d'e-mail transactionnel]({{site.baseurl}}/api/api_campaigns/transactional_campaigns) de Braze est spécialement conçue pour envoyer des messages e-mail automatisés et non promotionnels, tels que les confirmations de commande, les réinitialisations de mot de passe, les alertes de facturation ou d'autres notifications critiques pour l'entreprise. De plus, un [endpoint d'e-mail transactionnel]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message) correspondant a été créé. Les e-mails transactionnels et le nouvel endpoint ne sont disponibles que dans le cadre de certains packages Braze.

## Prise en charge des objets imbriqués pour les propriétés d'événement {#nested-object-support-for-event-properties}

Braze prend désormais en charge les [objets imbriqués]({{site.baseurl}}/user_guide/data/activation/events/custom_events/nested_objects) pour les événements personnalisés et les événements d'achat. Les objets imbriqués vous permettent d'envoyer des tableaux de données en tant que propriétés d'événements personnalisés et d'achats. Ces données imbriquées peuvent être utilisées pour créer des modèles d'informations personnalisées dans les messages déclenchés par API grâce à l'utilisation de Liquid et de la notation par points.

## Nouveaux filtres Liquid HMAC {#new-hmac-liquid-filters}

De nouveaux [filtres d'encodage Liquid `hmac_sha1` et `hmac_sha256`]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters) ont été ajoutés à la plateforme Braze.

## Page des événements d'achat {#purchase-event-page}

Vous souhaitez en savoir plus sur les événements d'achat dans Braze ? Consultez notre article dédié aux [événements d'achat]({{site.baseurl}}/user_guide/data/activation/events/purchase_events) pour en apprendre davantage.

## Nouveaux partenariats Braze {#new-braze-partnerships}

### Nexla - Automatisation des workflows {#nexla-workflow-automation}

[Nexla]({{site.baseurl}}/partners/nexla) est le leader des opérations de données unifiées et a été désigné Gartner Cool Vendor en 2021. Les clients qui utilisent Currents pour envoyer des données à des entrepôts de données peuvent tirer parti de Nexla pour extraire, transformer et charger ces données vers d'autres destinations, rendant ainsi les données facilement accessibles dans l'ensemble de votre écosystème. Nexla vous permet d'utiliser Braze Currents pour obtenir des données dans un format personnalisé, livrées à la destination de votre choix en quelques clics.

### Amperity - Plateforme de données client {#amperity-customer-data-platform}

[Amperity]({{site.baseurl}}/partners/amperity) est une plateforme de données client d'entreprise complète qui aide les marques à mieux connaître leurs clients, à prendre des décisions stratégiques et à adopter systématiquement les bonnes actions pour mieux servir leurs consommateurs. Amperity prend en charge la plateforme Braze en fournissant une vue unifiée de vos clients à travers sa CDP et Braze, vous permettant d'envoyer des données Amperity pertinentes vers Braze.

### Digioh - Sondages {#digioh-surveys}

[Digioh]({{site.baseurl}}/partners/digioh) vous aide à développer vos listes, à capturer des données first-party et à exploiter vos données dans vos Campaigns Braze. Le générateur par glisser-déposer facilite la création de formulaires conformes à votre image de marque, de pop-ups, de centres de préférences, de pages de destination et de sondages qui vous connectent à vos clients.

### AppsFlyer Audiences - Attribution/Analytique {#appsflyer-audiences-attributionanalytics}

[AppsFlyer]({{site.baseurl}}/partners/message_orchestration/attribution/appsflyer) est une plateforme d'analytique et d'attribution en marketing mobile qui vous aide à analyser et optimiser vos applications grâce à l'analytique marketing, l'attribution mobile et la création de liens profonds. [AppsFlyer Audiences]({{site.baseurl}}/partners/appsflyer_audiences) vous permet de créer des Segments d'audience et de les transmettre directement à Braze pour créer des Campaigns d'engagement client performantes.