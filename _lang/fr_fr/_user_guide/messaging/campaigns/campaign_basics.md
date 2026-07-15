---
nav_title: Principes de base des campagnes
article_title: Principes de base des campagnes
page_order: 0
page_type: reference
description: "Cet article de référence couvre les principes de base des campagnes, en abordant les différentes questions que vous devriez vous poser lors de la mise en place de vos premières campagnes."
tool: Campaigns

---

# Principes de base des campagnes {#campaigns-basics}

> Cet article de référence couvre les principes de base des campagnes, en abordant les différentes questions que vous devriez vous poser lors de la mise en place de vos premières campagnes.

## Comprendre la structure d'une campagne {#understanding-campaign-structure}

Avant d'entrer dans les détails de la configuration des campagnes, identifions les éléments clés pour comprendre comment les campagnes fonctionnent sur les différents canaux de communication.

Les campagnes constituent une étape de message unique pour communiquer avec vos utilisateurs sur des canaux, plus communément appelés canaux de communication. Ces canaux de communication comprennent les Content Cards, l'e-mail, les messages in-app, les notifications push, les SMS et MMS, ainsi que les webhooks. En identifiant où se trouvent vos clients, vous pouvez exploiter les canaux de communication appropriés pour échanger avec eux.

## Construire le parcours client {#building-the-customer-journey}

Étant donné que les campagnes peuvent être conçues de manière unique selon le canal de communication, vous pouvez utiliser ces cinq questions de visualisation pour identifier et conceptualiser vos stratégies et objectifs d'engagement client.

### Le « quoi » : nommez votre campagne {#the-what-name-your-campaign}

*Qu'essayez-vous d'aider l'utilisateur à faire ou à comprendre ?*

Ne sous-estimez jamais le pouvoir d'un nom. Braze est conçu pour la collaboration, c'est donc le moment idéal pour clarifier la manière dont vous communiquerez vos objectifs à votre équipe. Pour en savoir plus sur les parcours clients, consultez notre cours Braze Learning [Cartographier les cycles de vie des utilisateurs](https://learning.braze.com/mapping-customer-lifecycles) !

### Le « quand » : créez les conditions de démarrage {#the-when-create-starting-conditions}

*Quand un client rencontrera-t-il cette campagne ?*

Les utilisateurs peuvent entrer dans votre campagne de trois manières : à une date et une heure définies (planification), lorsqu'ils effectuent une action spécifique (basé sur une action), ou lorsqu'ils font quelque chose qui déclenche un appel API (déclenché par API).

La distribution planifiée consiste à configurer vos campagnes pour qu'elles soient envoyées à un moment précis, et éventuellement selon une cadence définie. Les campagnes basées sur une action répondent à des comportements spécifiques des clients en temps réel. Cela peut inclure un achat ou une interaction avec une autre campagne. Les campagnes déclenchées par API peuvent être configurées pour identifier des actions clés des clients sur votre plateforme qui, une fois réalisées, déclenchent un appel API vers Braze et envoient vos campagnes.

### Le « qui » : sélectionnez une audience d'entrée {#the-who-select-an-entry-audience}

*Qui essayez-vous d'atteindre ?*

Vous pouvez utiliser des [segments]({{site.baseurl}}/user_guide/audience/segments) prédéfinis pour cibler les utilisateurs en fonction de leurs caractéristiques et actions démographiques, comportementales ou techniques. Ajoutez des filtres supplémentaires lors de la création de votre campagne pour affiner davantage votre segment. Seuls les utilisateurs qui correspondent à ces critères d'audience cible peuvent entrer dans le parcours. Consultez ce tableau pour un résumé rapide des types de filtres disponibles.

| Filtre | Description |
|---|---|
| Données personnalisées | Segmentez les utilisateurs en fonction des événements et des attributs que vous définissez. Permet d'utiliser des fonctionnalités spécifiques à votre produit. |
| Activité de l'utilisateur | Segmentez les clients en fonction de leurs actions et de leurs achats. |
| Reciblage | Segmentez les clients à qui des campagnes précédentes ont été envoyées, qui les ont reçues ou avec lesquelles ils ont interagi. |
| Activité marketing | Segmentez les clients en fonction de comportements universels comme le dernier engagement ou les campagnes reçues. |
| Attributs de l'utilisateur | Segmentez les clients selon leurs attributs et caractéristiques constants. |
| Attribution d'installation | Segmentez les clients selon leur première source, groupe publicitaire, campagne ou annonce. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Le « qui » : sélectionnez une audience d'entrée" }

### Le « pourquoi » : identifiez les événements de conversion {#the-why-identify-conversion-events}

*Pourquoi créez-vous cette campagne ?*

Il est toujours important d'avoir un objectif clair en tête, et les campagnes vous aident à comprendre vos performances par rapport à des indicateurs clés de performance tels que l'engagement de session, les achats et les événements personnalisés. Sélectionner au moins un [événement de conversion]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events) vous permettra de comprendre les performances de votre campagne.

### Le « où » : trouvez mon audience {#the-where-find-my-audience}

*Où puis-je atteindre mon audience le plus efficacement ?*

C'est ici que nous déterminons quels canaux de communication sont les plus pertinents pour votre parcours utilisateur. Idéalement, vous souhaitez atteindre vos utilisateurs là où ils sont les plus actifs.

### Le « comment » : construisez l'expérience {#the-how-build-the-experience}

*Comment créer ma campagne après avoir identifié les cinq questions ?*

Envisagez de mettre en place des variantes et des tests A/B à mesure que vous gagnez en expertise dans la création de campagnes. Notez que les campagnes prennent en charge jusqu'à huit variantes avec un groupe de contrôle. Utilisez les analyses de votre campagne pour prendre des décisions éclairées lors de la construction de votre campagne, en ajustant aussi bien votre audience segmentée que le contenu de vos messages.