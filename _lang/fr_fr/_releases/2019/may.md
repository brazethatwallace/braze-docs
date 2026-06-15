---
nav_title: mai
page_order: 8
noindex: true
page_type: update
description: "Cet article contient les notes de version de mai 2019."
---

# Mai 2019 {#may-2019}

## Content Cards

Les Content Cards sont des contenus persistants qui apparaissent dans l'application et les expériences Web des clients.

Avec les Content Cards, vous pouvez envoyer un flux dynamique et hautement ciblé de contenu riche à vos clients, directement dans les applications qu'ils aiment, sans interrompre leur expérience. Vous pouvez également associer les Content Cards à d'autres canaux, comme les e-mails ou les notifications push, pour créer des stratégies marketing cohésives.

![Flux de Content Cards]({% image_buster /assets/img/cc-feed.png %}){: height="50%" width="50%"}

De plus, les Content Cards prennent en charge des fonctionnalités plus personnalisées, notamment l'épinglage de cartes, la fermeture de la carte de contenu, la distribution basée sur l'API, des délais d'expiration de carte personnalisés et l'analyse des cartes.

Utilisez-les pour créer des centres de notification, des flux d'accueil et des flux de promotion.

Vous devrez mettre à jour vers une version prise en charge du SDK Braze :
- iOS : 3.8.0 ou version ultérieure
- Android : 2.6.0 ou ultérieure
- Web : 2.2.0 ou ultérieure

[Pour en savoir plus sur les Content Cards, cliquez ici !]({{site.baseurl}}/user_guide/channels/content_cards/)

{% alert update %}
Les Content Cards pour Currents et notre documentation API pour les Content Cards seront lancées plus tard cette semaine. Restez à l'écoute !
{% endalert %}

## Ajout de la plateforme Roku {#roku-platform-addition}

Braze a ajouté un nouveau canal à ses capacités ! En proposant de nouveaux canaux, nous pouvons permettre à nos clients d'enrichir leurs données grâce à une meilleure compréhension du comportement de visualisation ou de leur offrir des expériences pertinentes sur tous les canaux appropriés.

Vous pouvez désormais [récupérer les données des appareils Roku]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=roku) à des fins d'enrichissement des données et de suivi des événements personnalisés.

## Préférences de notification pour les mises à jour de Canvas ou de campagne {#notification-preferences-for-canvas-or-campaign-updates}

Cette [nouvelle notification]({{site.baseurl}}/user_guide/administrative/company_settings/notification_preferences/#notification-preferences) vous alertera par e-mail lorsqu'une campagne ou un Canvas est activé, mis à jour, réactivé ou désactivé. Activez cette fonction dans les **Préférences de notification** de votre compte Braze.

## Documentation du partenaire technologique Jampp {#jampp-technology-partner-documentation}

Jampp est une plateforme de performance marketing utilisée pour acquérir et recibler les clients mobiles. Jampp combine des données comportementales avec une technologie prédictive et programmatique pour générer du chiffre d'affaires pour les annonceurs en montrant des publicités personnelles et pertinentes qui inspirent les consommateurs à acheter pour la première fois, ou plus souvent.

Les clients de Braze peuvent [s'intégrer à Jampp]({{site.baseurl}}/partners/jampp/) en configurant le canal webhook de Braze pour diffuser les événements dans Jampp. Les clients ont ainsi la possibilité d'ajouter des ensembles de données plus riches à leurs initiatives de reciblage avec Jampp au sein de l'écosystème de publicité mobile.

## Sélecteur de plateforme pour les messages in-app {#platform-picker-for-in-app-messages}

Notre sélecteur de plateforme facilite la sélection de la destination de vos messages in-app et des plateformes pour lesquelles ils sont conçus, en mettant l'accent sur cette étape dans le processus de création de campagne.

![Sélecteur de plateforme]({% image_buster /assets/img/iam_platforms.gif %})

## Champ Dispatch ID de Currents pour l'e-mail {#dispatch-id-currents-field-for-email}

{% alert update %}
Le comportement de `dispatch_id` diffère entre Canvas et les campagnes, car Braze traite les étapes du Canvas (à l'exception des étapes d'entrée, qui peuvent être planifiées) comme des événements déclenchés, même lorsqu'elles sont « planifiées ». En savoir plus sur le [comportement de `dispatch_id`]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/dispatch_id/) dans Canvas et les campagnes.

_Mise à jour notée en août 2019._
{% endalert %}

Pour continuer à améliorer les capacités de Currents, nous ajoutons `dispatch_id` en tant que champ aux événements e-mail de Currents sur tous les types de connecteurs.

Le `dispatch_id` est l'ID unique généré pour chaque transmission (« dispatch ») envoyée depuis la plateforme Braze.

Alors que tous les clients qui reçoivent un message planifié obtiennent le même `dispatch_id`, les clients qui reçoivent des messages basés sur des actions ou déclenchés par API auront un `dispatch_id` unique par message. Le champ `dispatch_id` vous permet d'identifier l'instance d'une campagne récurrente qui est responsable de la conversion, ce qui vous fournit davantage d'informations sur les types de campagnes qui contribuent à atteindre vos objectifs métier.

## Fonction de tri « Only Show Mine » pour les campagnes {#only-show-mine-campaign-sorting-feature}

Quand un utilisateur coche la case `Only Show Mine` sur la grille des campagnes, les résultats affichés montreront uniquement les campagnes créées par l'utilisateur actuellement connecté. De plus, l'utilisateur peut utiliser la barre de recherche en saisissant `created_by_me:true`.

Et la barre latérale de la grille des campagnes est maintenant redimensionnable !

## Supprimer les utilisateurs par alias {#delete-users-by-alias}

Vous pouvez désormais utiliser l'endpoint `users/delete` pour [supprimer des utilisateurs par alias]({{site.baseurl}}/api/endpoints/user_data/#user-delete-request) !

## Calcul unique pour les clics et les ouvertures d'e-mails {#unique-calculation-for-email-clicks-and-opens}

Les clics uniques et les ouvertures uniques pour l'e-mail sont désormais capturés et affichés sur une période de 7 jours par utilisateur et s'incrémentent de 1 dans cette fenêtre de 7 jours, pour chaque `dispatch_id`.

L'utilisation de `dispatch_id` permet aux messages récurrents de refléter le nombre réel d'ouvertures uniques ou de clics uniques de chaque message. Il sera facile pour les clients de faire correspondre ces données, maintenant que le `dispatch_id` est disponible dans Currents.

Tous les utilisateurs sur Mailjet verront un pic dans ces chiffres, étant donné que la période d'unicité précédente était de plus de 30 jours. Vous auriez dû être averti de cette modification il y a trois (3) semaines. Les clients de SendGrid ne devraient pas voir de différence.

Vous pouvez rechercher ces termes actualisés dans notre [glossaire des indicateurs de rapport]({{site.baseurl}}/user_guide/analytics/metrics_glossary/).

{% alert update %}
Le comportement de `dispatch_id` diffère entre Canvas et les campagnes, car Braze traite les étapes du Canvas (à l'exception des étapes d'entrée, qui peuvent être planifiées) comme des événements déclenchés, même lorsqu'elles sont « planifiées ». [En savoir plus sur le comportement de `dispatch_id`]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/dispatch_id/) dans Canvas et les campagnes.

_Mise à jour notée en août 2019._
{% endalert %}

## Canal le plus engagé {#most-engaged-channel}

{% alert update %}
À partir de la [version du produit de novembre 2019]({{site.baseurl}}/help/release_notes/2019/november/#intelligence-suite), le « canal le plus engagé » a été renommé [« canal intelligent »]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_channel/).
{% endalert %}

Le filtre du canal le plus engagé sélectionne la partie de votre audience pour qui le canal de communication sélectionné est le « meilleur » canal. Dans ce cas, « le meilleur » signifie celui qui a la plus forte probabilité d'engagement, compte tenu de l'historique de l'utilisateur. Vous pouvez sélectionner l'e-mail, les notifications push Web ou les notifications push sur mobile (qui inclut tout système d'exploitation ou appareil mobile disponible) comme canal.

Découvrez ce nouveau filtre dans notre [bibliothèque des filtres de segmentation]({{site.baseurl }}/user_guide/engagement_tools/segments/segmentation_filters/).