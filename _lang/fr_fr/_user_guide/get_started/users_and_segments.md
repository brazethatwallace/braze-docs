---
nav_title: Utilisateurs et segments
article_title: "Pour commencer : Utilisateurs et segments"
page_order: 2
page_type: reference
description: "Cet article donne un aperçu des utilisateurs et des segments, en soulignant leur importance et la façon dont ils peuvent être exploités pour engager votre audience."
---

# Pour commencer : Utilisateurs et segments {#get-started-users-and-segments}

> Comprendre vos utilisateurs et les cibler efficacement est crucial pour envoyer des campagnes marketing personnalisées et ciblées. Cet article donne un aperçu des utilisateurs et des segments, en soulignant leur importance et la façon dont vous pouvez les exploiter pour engager votre audience.

## Utilisateurs {#users}

Dans Braze, les informations sur votre audience sont stockées dans des profils utilisateur. Un [profil utilisateur]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles) est un ensemble complet d'informations et d'attributs qui décrivent un consommateur individuel. Il sert de référentiel central pour stocker et gérer les données liées à son comportement, ses préférences et ses informations démographiques.

### Composantes d'un profil utilisateur {#parts-of-a-user-profile}

En comprenant les profils utilisateur, vous pouvez obtenir des informations sur votre audience et interagir avec elle de manière personnalisée et ciblée. Le profil d'un utilisateur contient de nombreuses informations, mais voici quelques éléments clés :

- **Identifiant utilisateur :** Chaque profil utilisateur est identifié de manière unique par un identifiant utilisateur, appelé `external_id`. Cet identifiant permet à Braze de suivre et d'associer les données utilisateur à travers différents canaux et appareils, offrant une vue unifiée des interactions de chaque utilisateur avec votre marque. Les [profils utilisateur anonymes]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/anonymous_users) (les utilisateurs qui visitent votre site web ou votre application sans se connecter) n'ont pas d'`external_id`, mais peuvent se voir attribuer des [alias d'utilisateur]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/anonymous_users#assigning-user-aliases) comme identifiant alternatif.
- [Attributs](#attributes) **:** Ce sont des informations spécifiques sur l'utilisateur, telles que son nom, son âge, sa localisation ou toute autre information démographique. Vous pouvez utiliser ces attributs pour segmenter votre audience et personnaliser vos messages.
- [Événements](#events) **:** Ce sont des actions effectuées par l'utilisateur, comme effectuer un achat, cliquer sur un lien ou ouvrir une application. Braze suit ces événements pour vous aider à comprendre le comportement et l'engagement de l'utilisateur. Comme les attributs, vous pouvez également utiliser les événements pour segmenter et personnaliser.
- **Achats :** Cette section enregistre l'historique d'achat de l'utilisateur. Elle est essentielle pour comprendre les habitudes d'achat et les préférences de l'utilisateur.
- **Appareils :** Cette section liste les appareils que l'utilisateur a utilisés pour interagir avec votre marque. Cela peut inclure des appareils mobiles, des navigateurs web et des appareils connectés (comme les objets portables et les TV connectées).
- **Engagement :** Cette section contient des informations sur les interactions de l'utilisateur avec les messages que vous lui envoyez, les Segments auxquels il appartient, son statut d'abonnement, et plus encore.
- **Historique des messages :** Il s'agit d'un enregistrement de tous les messages envoyés à l'utilisateur depuis le canal de communication correspondant (tel que l'e-mail ou la notification push).

{% alert tip %}
Les SDK de la plateforme Braze collectent automatiquement 27 attributs et événements différents. En utilisant ces événements et attributs standard, vous pouvez créer des Segments dès que vous intégrez le SDK.
{% endalert %}

### Attributs {#attributes}

Les attributs sont des caractéristiques ou propriétés spécifiques associées à un utilisateur. Ces attributs vous aident à segmenter et cibler les utilisateurs en fonction de leurs traits et intérêts uniques. Il existe deux types d'attributs dans Braze : les attributs standard et les attributs personnalisés.

#### Attributs standard {#standard-attributes}

Les attributs standard sont des attributs prédéfinis que vous pouvez suivre avec Braze après l'intégration du SDK dans votre application. Ce sont des informations courantes sur les utilisateurs que la plupart des applications trouvent utiles, telles que les données démographiques et les données d'appareil. Exemples :

- Prénom
- Nom
- E-mail
- Genre
- Date de naissance
- Pays
- Ville
- Dernière application utilisée
- Langue
- Fuseau horaire

#### Attributs personnalisés {#custom-attributes}

Les [attributs personnalisés]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes) sont des attributs que vous définissez en fonction de vos besoins métier spécifiques. Ils vous permettent de suivre des informations propres à votre application ou à votre activité.

Par exemple, une application de streaming musical pourrait suivre des attributs personnalisés tels que :

- Genre favori
- Nombre de chansons écoutées
- Abonné premium (Oui/Non)
- Artiste favori

Une application de vente au détail, quant à elle, pourrait suivre des attributs personnalisés tels que :

- Taille de vêtement préférée
- Marque favorite
- Nombre d'achats
- Membre du programme de fidélité (Oui/Non)

Les attributs personnalisés vous offrent la flexibilité de collecter et d'analyser les données les plus pertinentes pour votre activité. Cependant, ils nécessitent une configuration supplémentaire.

Les attributs standard et personnalisés peuvent être utilisés pour segmenter votre audience et personnaliser vos messages marketing. Par exemple, vous pourriez envoyer une offre spéciale aux utilisateurs d'une certaine ville (attribut standard) qui ont effectué plus de 10 achats (attribut personnalisé).

### Événements {#events}

Les événements représentent des actions ou comportements spécifiques effectués par les utilisateurs au sein de votre application ou de votre site web. Des exemples d'événements peuvent inclure le lancement d'une application, les achats, la consultation de contenu ou toute autre action. En suivant et en analysant ces événements, vous pouvez obtenir des informations sur le comportement des utilisateurs et les tendances d'engagement.

#### Événements standard {#standard-events}

Les [événements standard]({{site.baseurl}}/user_guide/data/activation/events) sont des événements prédéfinis que Braze suit automatiquement après l'intégration du SDK dans votre application ou votre site. Voici quelques exemples d'événements standard :

- **Début de session :** Cet événement est déclenché lorsqu'un utilisateur ouvre l'application.
- **Fin de session :** Cet événement est déclenché lorsqu'un utilisateur ferme l'application.
- **Achat :** Cet événement est déclenché lorsqu'un utilisateur effectue un achat dans l'application.
- **Clic sur une notification push :** Cet événement est déclenché lorsqu'un utilisateur clique sur une notification push.

#### Événements personnalisés {#custom-events}

Les [événements personnalisés]({{site.baseurl}}/user_guide/data/activation/events/custom_events) sont des événements que vous définissez en fonction des actions spécifiques que vous souhaitez suivre dans votre application ou sur votre site. Par exemple, une application de streaming musical pourrait suivre des événements personnalisés tels que :

- Chanson écoutée
- Playlist créée
- Publicité ignorée

Une application de fitness, quant à elle, pourrait suivre des événements personnalisés tels que :

- Entraînement démarré
- Entraînement terminé
- Record personnel établi

Les événements personnalisés vous offrent la flexibilité de suivre les actions les plus pertinentes pour votre application et votre activité. Cependant, comme les attributs personnalisés, ils nécessitent une configuration supplémentaire.

### Points de donnée {#data-points}

Braze utilise les points de donnée pour vous aider à définir les informations les plus impactantes pour votre activité. Les points de donnée sont un élément essentiel du fonctionnement de Braze et sont utilisés pour la facturation, la tarification et, surtout, la personnalisation et l'optimisation de vos Campaigns marketing.

Les points de donnée sont consommés lorsque les données du profil d'un utilisateur sont mises à jour ou lorsqu'il effectue des actions spécifiques. Ces actions peuvent inclure le démarrage d'une session, la fin d'une session, l'enregistrement d'un événement personnalisé ou la réalisation d'un achat. Il est important de noter que toutes les données collectées par Braze ne sont pas comptabilisées comme des points de donnée. Par exemple, les données et événements collectés par défaut par les services Braze, tels que les jetons de notification push, les informations sur l'appareil et tous les événements de suivi d'engagement des Campaigns, comme les ouvertures d'e-mail et les clics sur les notifications push, ne sont pas comptabilisés comme des points de donnée.

En réfléchissant soigneusement aux informations à suivre en tant que points de donnée, vous ciblez les données ayant le plus d'impact sur l'expérience de vos utilisateurs. Votre gestionnaire de compte Braze vous aidera à recommander les meilleures pratiques en matière de données adaptées à vos besoins.

Consultez notre article dédié pour en savoir plus sur les [points de donnée]({{site.baseurl}}/user_guide/data/infrastructure/data_points).

## Segments {#segments}

La [segmentation]({{site.baseurl}}/user_guide/audience/segments) vous permet de cibler les utilisateurs en fonction de leurs caractéristiques et actions démographiques, comportementales, sociales ou techniques (c'est-à-dire les attributs et événements). Une utilisation créative et intelligente de la segmentation et de l'automatisation des communications vous permet de faire progresser vos utilisateurs de façon fluide tout au long de leur parcours client.

Conseils pour travailler avec les Segments :

- Les Segments dans Braze sont dynamiques : les utilisateurs entrent et sortent constamment des Segments, car ils ne répondent pas toujours aux critères. Les utilisateurs qui répondent aux critères d'un Segment au moment de l'envoi seront les destinataires de cette Campaign ou de ce Canvas.
    - Si vous souhaitez que votre Segment soit statique, vous pouvez utiliser les extensions de segments. Les extensions de segments (avec la [régénération désactivée]({{site.baseurl}}/user_guide/audience/segments/segment_extension#step-4-designate-refresh-settings-optional)) représentent votre audience sous la forme d'un instantané unique à un moment donné.
- Vous n'êtes pas limité à l'utilisation d'un seul filtre à la fois. Créez des Segments finement ajustés et granulaires en superposant plusieurs filtres les uns sur les autres.
- Vous pouvez utiliser les actions ou les inactions de vos utilisateurs pour comprendre comment les contacter là où ils souhaitent interagir avec vous. Ces actions peuvent être des événements personnalisés, une interaction avec une Campaign ou un Canvas existant, ou même un message spécifique au sein d'un Canvas.

### Cas d'usage {#use-case}

Supposons que vous gérez une boutique de vêtements en ligne et que vous avez mis en place un flux de communication pour envoyer une série d'e-mails aux utilisateurs qui ont ajouté un article à leur panier sans finaliser l'achat. Ce flux de panier abandonné pourrait inclure un premier e-mail de rappel, un e-mail de suivi proposant une réduction, et un dernier e-mail de rappel.

![Capture d'écran liée au cas d'usage.]({% image_buster /assets/img/getting_started/segment_example.png %}){: style="max-width:70%" }

Vous pourriez créer un Segment d'utilisateurs ayant déclenché l'événement personnalisé « Added Item to Cart » sans avoir déclenché l'événement personnalisé « Completed Purchase ». Ensuite, au sein de ce Segment, vous pourriez identifier davantage les utilisateurs qui ont ouvert le premier e-mail de rappel (interaction avec un message spécifique) mais qui n'ont pas effectué d'achat.

![Vous pourriez créer un Segment d'utilisateurs ayant déclenché l'événement personnalisé « Added Item to Cart » sans avoir déclenché l'événement personnalisé « Completed Purchase ». Ensuite, au sein de ce Segment, vous pourriez identifier davantage les utilisateurs qui ont ouvert le premier e-mail de rappel (interaction avec un message spécifique) mais qui n'ont pas effectué d'achat.]({% image_buster /assets/img/getting_started/segment_example_breakdown.png %})

Ce Segment pourrait être ciblé par une Campaign plus agressive pour essayer de convertir ces utilisateurs en acheteurs. Par exemple, vous pourriez leur envoyer une offre spéciale ou une recommandation personnalisée basée sur les articles de leur panier.

Ce n'est qu'un exemple de la façon dont vous pouvez utiliser les actions et inactions des utilisateurs, les événements personnalisés et les données d'interaction pour créer des Segments et adapter vos stratégies marketing dans Braze.