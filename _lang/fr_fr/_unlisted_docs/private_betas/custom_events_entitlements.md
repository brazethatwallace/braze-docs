---
article_title: Événements personnalisés
permalink: "/custom_events_entitlements/"
hidden: true
---

# [![Cours Braze Learning]({% image_buster /assets/unlisted_docs/img/logos/bl_icon3.png %})](https://learning.braze.com/custom-events-and-attributes){: style="float:right;width:120px;border:0;" class="noimgborder"}Événements personnalisés {#braze-learning-course-image_buster-assetsunlisted_docsimglogosbl_icon3png-httpslearningbrazecomcustom-events-and-attributes-stylefloatrightwidth120pxborder0-classnoimgbordercustom-events}

> Cet article décrit les événements personnalisés et leurs propriétés, les filtres de segmentation associés, les propriétés d'entrée Canvas, les analyses pertinentes, et plus encore. Pour en savoir plus sur les événements Braze en général, consultez [Événements](https://www.braze.com/docs/user_guide/data/custom_data/events/).

Les événements personnalisés sont des actions effectuées par vos utilisateurs ou des mises à jour les concernant. Lorsque des événements personnalisés sont enregistrés, ils peuvent déclencher un nombre et un type quelconques de campagnes de suivi. Vous pouvez ensuite utiliser des [filtres de segmentation](#segmentation-filters) pour segmenter les utilisateurs en fonction de la récence et de la fréquence de ces événements personnalisés. Cela fait des événements personnalisés l'outil idéal pour suivre les interactions utilisateur à forte valeur au sein de votre application.

## Cas d'utilisation {#use-cases}

Voici quelques cas d'utilisation courants des événements personnalisés :

- Déclencher une campagne ou un Canvas basé sur un événement personnalisé en utilisant la [livraison par événement](https://www.braze.com/docs/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/)
- Segmenter les utilisateurs en fonction du nombre de fois qu'ils ont effectué un événement personnalisé, de la dernière occurrence de l'événement, et autres critères similaires
- Utiliser les [analyses d'événements personnalisés](https://www.braze.com/docs/user_guide/data_and_analytics/custom_data/custom_events#custom-event-analytics) du tableau de bord pour visualiser un agrégat de la fréquence de chaque événement
- Trouver des analyses supplémentaires à l'aide des rapports d'[entonnoir](https://www.braze.com/docs/user_guide/data_and_analytics/reporting/funnel_reports/#step-2-select-events-for-funnel-steps) et de [rétention](https://www.braze.com/docs/user_guide/analytics/reporting/retention_reports/)
- Exploiter les [propriétés d'entrée persistantes](https://www.braze.com/docs/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/canvas_persistent_entry_properties/) pour utiliser les métadonnées de votre événement client à des fins de personnalisation dans vos étapes Canvas
- Générer des analyses plus sophistiquées avec [Currents](https://www.braze.com/docs/user_guide/data/braze_currents/)
- Configurer des [critères de sortie](https://www.braze.com/docs/user_guide/engagement_tools/canvas/create_a_canvas/exit_criteria) pour définir quand les utilisateurs doivent quitter votre Canvas

## Droits d'utilisation {#entitlements}

Les droits d'utilisation déterminent la capacité de vos événements personnalisés, qui suit le nombre de noms d'événements différents que vous définissez. Vous pouvez avoir jusqu'à 2 000 événements personnalisés par espace de travail. Si vous devez augmenter votre capacité, contactez votre gestionnaire de compte Braze pour plus d'informations.

Lorsque votre espace de travail approche du nombre maximum d'événements personnalisés, vous recevrez des notifications dans le tableau de bord et par e-mail pour vous aider à rester informé.

Même après avoir atteint la capacité maximale, les événements personnalisés existants peuvent toujours être reçus. Cependant, vous ne pourrez pas créer de nouveaux événements personnalisés. Toute donnée reçue pour des événements personnalisés qui n'existent pas encore ne sera pas traitée.

## Gérer les événements personnalisés {#managing-custom-events}

Vous pouvez gérer, créer ou bloquer des événements personnalisés dans le tableau de bord en accédant à **Paramètres des données** > **Événements personnalisés**.

Sélectionnez le menu à côté d'un événement personnalisé pour les actions suivantes :

### Blocage {#blocklisting}

Vous pouvez bloquer des événements personnalisés individuels via le menu d'actions, ou sélectionner et bloquer jusqu'à 100 événements en masse.

Lorsque vous bloquez un événement personnalisé :

- Les données futures ne seront plus collectées pour cet événement.
- Les données existantes ne seront pas disponibles tant que cet événement n'est pas débloqué.
- Cet événement n'apparaîtra pas dans les filtres ou les graphiques.

De plus, si un événement personnalisé bloqué est actuellement référencé par des filtres ou des déclencheurs dans d'autres zones de Braze, une fenêtre modale d'avertissement apparaîtra pour expliquer que toutes les instances des filtres ou déclencheurs qui le référencent seront supprimées et archivées.

### Ajout de descriptions {#adding-descriptions}

Vous pouvez ajouter une description à un événement personnalisé après sa création si vous disposez de l'[autorisation utilisateur](https://www.braze.com/docs/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/) `Manage Events, Attributes, Purchases`. Sélectionnez **Modifier la description** pour l'événement personnalisé et saisissez ce que vous souhaitez, comme une note pour votre équipe.

## Ajout d'étiquettes {#adding-tags}

Vous pouvez ajouter des étiquettes à un événement personnalisé après sa création si vous disposez de l'[autorisation utilisateur](https://www.braze.com/docs/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/) « Manage Events, Attributes, Purchases ». Les étiquettes peuvent ensuite être utilisées pour filtrer la liste des événements.

### Affichage des rapports d'utilisation {#viewing-usage-reports}

Le rapport d'utilisation répertorie tous les Canvas, Campaigns et segments utilisant un événement personnalisé spécifique. La liste n'inclut pas les utilisations de Liquid.

Vous pouvez afficher jusqu'à 100 rapports d'utilisation à la fois en cochant les cases de plusieurs événements personnalisés, puis en sélectionnant **Afficher le rapport d'utilisation**.

## Exportation des données {#exporting-data}

Pour exporter la liste des événements personnalisés sous forme de fichier CSV, sélectionnez le bouton **Tout exporter** en haut de la page. Le fichier CSV sera généré et un lien de téléchargement vous sera envoyé par e-mail.

## Enregistrement des événements personnalisés {#logging-custom-events}

Les événements personnalisés nécessitent une configuration supplémentaire. Consultez la liste ci-dessous pour la documentation de chaque plateforme, où vous trouverez des informations sur les méthodes utilisées pour enregistrer les événements personnalisés et comment ajouter des propriétés et des quantités à vos événements personnalisés.

{% details Développer pour la documentation par plateforme %}

- [Android et FireOS](https://www.braze.com/docs/developer_guide/analytics/logging_events/?tab=android)
- [iOS](https://www.braze.com/docs/developer_guide/analytics/logging_events/?tab=swift)
- [Web](https://www.braze.com/docs/developer_guide/analytics/logging_events/?tab=web)
- [React Native](https://www.braze.com/docs/developer_guide/platform_integration_guides/react_native/analytics/#logging-custom-events)
- [Unity](https://www.braze.com/docs/developer_guide/platform_integration_guides/unity/Analytics/logging_custom_events/)
- [Xamarin](https://www.braze.com/docs/developer_guide/platform_integration_guides/xamarin/analytics/#tracking-custom-events)
- [Roku](https://www.braze.com/docs/developer_guide/analytics/logging_events/?tab=roku)

{% enddetails %}

## Stockage des événements personnalisés {#custom-event-storage}

Toutes les données stockées sur le **profil utilisateur**, y compris les métadonnées des événements personnalisés (première ou dernière occurrence, nombre total et X en Y sur 30 jours), sont conservées indéfiniment tant que chaque profil est [actif](https://www.braze.com/docs/user_guide/data_and_analytics/user_data_collection/user_archival/#active-users).

## Filtres de segmentation {#segmentation-filters}

Le tableau suivant présente les filtres disponibles pour segmenter les utilisateurs par événements personnalisés.

| Options de segmentation | Filtre déroulant | Options de saisie |
| ---------------------| --------------- | ------------- |
| Vérifier si l'événement personnalisé s'est produit **plus de X fois** | **PLUS DE** | **NOMBRE** |
| Vérifier si l'événement personnalisé s'est produit **moins de X fois** | **MOINS DE** | **NOMBRE** |
| Vérifier si l'événement personnalisé s'est produit **exactement X fois** | **EXACTEMENT** | **NOMBRE** |
| Vérifier si l'événement personnalisé s'est produit pour la dernière fois **après la date X** | **APRÈS** | **DATE** |
| Vérifier si l'événement personnalisé s'est produit pour la dernière fois **avant la date X** | **AVANT** | **DATE** |
| Vérifier si l'événement personnalisé s'est produit pour la dernière fois **il y a plus de X jours** | **PLUS DE** | **NOMBRE DE JOURS** (nombre positif) |
| Vérifier si l'événement personnalisé s'est produit pour la dernière fois **il y a moins de X jours** | **MOINS DE** | **NOMBRE DE JOURS** (nombre positif) |
| Vérifier si l'événement personnalisé s'est produit **plus de X fois (max = 50)** | **PLUS DE** | au cours des **Y derniers jours (Y = 1, 3, 7, 14, 21, 30)** |
| Vérifier si l'événement personnalisé s'est produit **moins de X fois (max = 50)** | **MOINS DE** | au cours des **Y derniers jours (Y = 1, 3, 7, 14, 21, 30)** |
| Vérifier si l'événement personnalisé s'est produit **exactement X fois (max = 50)** | **EXACTEMENT** | au cours des **Y derniers jours (Y = 1, 3, 7, 14, 21, 30)** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Analyses {#analytics}

Braze enregistre le nombre de fois que les événements personnalisés se sont produits et la dernière fois qu'ils ont été effectués par chaque utilisateur à des fins de segmentation. Consultez ces analyses en accédant à **Analytics** > **Rapport d'événements personnalisés**.

Sur la page **Rapport d'événements personnalisés** du tableau de bord, vous pouvez visualiser de manière agrégée la fréquence de chaque événement personnalisé. Les lignes grises superposées sur la série temporelle indiquent la dernière fois qu'une campagne a été envoyée, ce qui est utile pour voir comment vos campagnes ont affecté l'activité des événements personnalisés.

![Graphique du nombre d'événements personnalisés sur la page Événements personnalisés du tableau de bord montrant les tendances d'un événement personnalisé][8]

Vous pouvez également utiliser les **Filtres** pour ventiler vos événements personnalisés par heure, utilisateurs actifs mensuels (MAU), segments ou formules d'indicateurs clés de performance.

{% alert tip %}
[Incrémentez les attributs personnalisés](https://www.braze.com/docs/user_guide/data_and_analytics/custom_data/custom_attributes/#integers) pour maintenir un compteur sur une action utilisateur similaire à un événement personnalisé. Cependant, vous ne pouvez pas visualiser les données d'attributs personnalisés dans une série temporelle. Les actions utilisateur qui n'ont pas besoin d'être analysées dans une série temporelle doivent être enregistrées à l'aide de cette méthode.
{% endalert %}

### Pourquoi les analyses d'événements personnalisés ne s'affichent pas {#why-custom-events-analytics-arent-showing}

Les segments créés avec des données d'événements personnalisés ne peuvent pas afficher les données historiques antérieures à leur création.

## Propriétés d'événement personnalisé {#custom-event-properties}

Les propriétés d'événement personnalisé sont des métadonnées ou des attributs d'événement personnalisé qui décrivent une occurrence spécifique d'un événement. Ces propriétés peuvent être utilisées pour affiner les conditions de déclenchement, augmenter la personnalisation des messages, suivre les conversions et générer des analyses plus sophistiquées via l'exportation de données brutes.

Les propriétés d'événement personnalisé ne sont pas stockées sur le profil Braze et ne consomment donc pas de points de donnée (voir [Points de donnée](#data-points) pour les exceptions).

{% alert important %}
Chaque événement personnalisé ou achat peut avoir jusqu'à 256 propriétés d'événement personnalisé distinctes. Si un événement personnalisé ou un achat est enregistré avec plus de 256 propriétés, seules les 256 premières seront capturées et disponibles à l'utilisation.
{% endalert %}

### Format attendu {#expected-format}

Les valeurs des propriétés doivent être un objet dont les clés sont les noms des propriétés et les valeurs sont les valeurs des propriétés. Les noms de propriétés doivent être des chaînes de caractères non vides de 255 caractères ou moins, sans signe dollar (`$`) en début.

Les valeurs de propriétés peuvent être de l'un des types de données suivants :

| Type de données | Description |
| --- | --- |
| Nombres | Sous forme d'[entiers](https://en.wikipedia.org/wiki/Integer) ou de [nombres à virgule flottante](https://en.wikipedia.org/wiki/Floating-point_arithmetic) |
| Booléens | Valeur `true` ou `false`. |
| Dates et heures | Formatées en chaînes de caractères au format [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) ou `yyyy-MM-dd'T'HH:mm:ss:SSSZ`. Non prises en charge dans les tableaux. |
| Chaînes de caractères | 255 caractères ou moins. |
| Tableaux | Les tableaux ne peuvent pas contenir de dates et heures. |
| Objets | Les objets seront ingérés sous forme de chaînes de caractères. |
| Objets imbriqués | Objets situés à l'intérieur d'autres objets. Pour en savoir plus, consultez la section de cet article sur les [objets imbriqués](#nested-objects).
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Les objets de propriétés d'événement contenant des valeurs de type tableau ou objet peuvent avoir un payload de propriété d'événement allant jusqu'à 100&nbsp;Ko.

Vous pouvez modifier le type de données de votre propriété d'événement personnalisé, mais soyez conscient des impacts du [changement de type de données](https://www.braze.com/docs/help/help_articles/data/change_custom_data_type/) après la collecte des données.

### Utilisation des propriétés d'événement personnalisé {#using-custom-event-properties}

Les propriétés d'événement personnalisé peuvent être utilisées pour qualifier les déclencheurs de campagne, suivre les conversions et personnaliser les messages.

#### Déclencher des messages {#trigger-messages}

Utilisez les propriétés d'événement personnalisé pour affiner davantage votre audience pour une campagne ou un Canvas particulier. Par exemple, si vous avez une application d'e-commerce et souhaitez envoyer un message à un utilisateur lorsqu'il abandonne son panier, vous pouvez ajouter une propriété d'événement personnalisé `cart value` pour améliorer votre audience cible et permettre une personnalisation accrue de la campagne.

![Filtres de propriétés d'événement personnalisé pour un panier abandonné. Deux filtres sont combinés avec un opérateur ET pour envoyer cette campagne aux utilisateurs qui ont abandonné leur panier avec une valeur de panier comprise entre 100 et 200 dollars][16]

Les propriétés d'événement personnalisé imbriquées sont également prises en charge dans la [livraison par événement][19].

![Filtres de propriétés d'événement personnalisé pour un panier abandonné. Un filtre est sélectionné si un article du panier a un prix supérieur à 100 dollars.][20]

#### Personnaliser les messages {#personalize-messages}

Vous pouvez également utiliser les propriétés d'événement personnalisé pour la personnalisation dans le modèle de message. Toute campagne utilisant la [livraison par événement][19] avec un événement déclencheur peut utiliser les propriétés d'événement personnalisé de cet événement pour la personnalisation des messages.

Par exemple, si vous avez une application de jeu et souhaitez envoyer un message aux utilisateurs qui ont terminé un niveau, vous pourriez personnaliser davantage votre message avec une propriété indiquant le temps qu'il a fallu aux utilisateurs pour terminer ce niveau. Dans cet exemple, le message est personnalisé pour trois segments différents en utilisant la [logique conditionnelle][18]. La propriété d'événement personnalisé appelée `time_spent` peut être incluse dans le message en appelant ``{% raw %} {{event_properties.${time_spent}}} {% endraw %}``.

{% raw %}
```liquid
{% if {{event_properties.${time_spent}}} < 600 %}
Incredible work, hero! Are you ready to test your skills against other powerful heroes? Visit the Arena for real-time battles with top players from around the globe.
{% elsif {{event_properties.${time_spent}}} < 1800 %}
Great job, hero! Don't forget to visit the town store between levels to upgrade your tools.
{% else %}
Well done, hero! Talk to villagers for tips on how to beat levels faster and unlock more rewards.
{% endif %}
```
{% endraw %}

{% alert warning %}
Si l'utilisateur n'a pas de connexion internet, les messages in-app déclenchés avec des propriétés d'événement personnalisé modélisées (par exemple, {% raw %}``{{event_properties.${time_spent}}}``{% endraw %}) échoueront et ne s'afficheront pas.
{% endalert %}

Pour une liste complète des étiquettes Liquid qui entraîneront la livraison des messages in-app en tant que messages in-app modélisés, consultez la [Foire aux questions](https://www.braze.com/docs/user_guide/message_building_by_channel/in-app_messages/faq/#what-are-templated-in-app-messages/).

##### Considérations relatives aux filtres {#considerations-with-filters}

- **Appels API :** Lors d'appels API utilisant le filtre « est vide », une propriété d'événement personnalisé est considérée comme « vide » si elle est exclue de l'appel. Par exemple, si vous incluez `"event_property": ""`, vos utilisateurs seront considérés comme « non vide ».
- **Entiers :** Lors du filtrage d'une propriété d'événement personnalisé de type nombre et que le nombre est très grand, n'utilisez pas le filtre « exactement ». Si un nombre est trop grand, il peut être arrondi à une certaine longueur, et votre filtre ne fonctionnera pas comme prévu.

#### Segmentation

Utilisez la segmentation par propriétés d'événement pour cibler les utilisateurs en fonction des événements personnalisés effectués et des propriétés associées à ces événements. Cela augmente vos options de filtrage lors de la segmentation par achat et événements personnalisés.

Les propriétés d'événement pour les événements personnalisés sont mises à jour en temps réel pour tout segment qui les utilise. Vous pouvez gérer les propriétés en accédant à **Paramètres des données** > **Événements personnalisés** et en sélectionnant **Gérer les propriétés** pour l'événement personnalisé associé. Les propriétés d'événement personnalisé utilisées dans certains filtres de segment ont un historique de consultation maximal de 30 jours.

##### Ajout de propriétés d'événement pour la segmentation {#adding-event-properties-for-segmentation}

Vous aurez besoin de l'[autorisation utilisateur](https://www.braze.com/docs/user_guide/data/data_points/#viewing-data-point-usage) « Manage Custom Event Property Segmentation » pour créer des segments basés sur la récence et la fréquence des propriétés d'événement.

Par défaut, vous pouvez avoir 20 propriétés d'événement segmentables par espace de travail. Contactez votre gestionnaire de compte Braze pour augmenter cette limite.

Pour ajouter des propriétés d'événement pour la segmentation, procédez comme suit :

1. Accédez à votre événement personnalisé et sélectionnez **Gérer les propriétés**.
2. Sélectionnez le bouton bascule **Activer la segmentation** pour ajouter la propriété d'événement à la segmentation. Vous pourrez accéder à des options de filtrage supplémentaires lors de la segmentation.

Les filtres de segmentation par propriétés d'événement incluent :

- A effectué un événement personnalisé avec la propriété A ayant la valeur B, X fois au cours des Y derniers jours.
- A effectué un achat avec la propriété A ayant la valeur B, X fois au cours des Y derniers jours.
- Permet de segmenter sur une période de 1 à 30 jours.

![Un groupe de filtres qui « a effectué 'Panier abandonné' avec la propriété 'nombre d'articles' et la valeur '2' 'plus de' '1' fois au cours des '30' derniers jours calendaires.][3]

Les données ne sont enregistrées pour une propriété d'événement donnée qu'après son activation par votre gestionnaire de la satisfaction client, et les propriétés d'événement ne sont disponibles qu'à partir de cette date.

##### Points de donnée {#data-points}

En ce qui concerne l'utilisation de l'abonnement, les propriétés d'événement personnalisé activées pour la segmentation avec les filtres suivants sont toutes comptées comme des points de donnée distincts en plus du point de donnée compté par l'événement personnalisé lui-même :

- `X Custom Event Property in Y Days`
- `X Purchase Property in Y Days`

### Propriétés d'entrée Canvas et propriétés d'événement {#canvas-entry-properties-and-event-properties}

Vous pouvez utiliser `canvas_entry_properties` et `event_properties` dans vos parcours utilisateur Canvas. Consultez [Propriétés d'entrée Canvas et propriétés d'événement](https://www.braze.com/docs/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/) pour plus d'informations et d'exemples.

{% tabs local %}
{% tab Propriétés d'entrée Canvas %}

Les [propriétés d'entrée Canvas](https://www.braze.com/docs/api/objects_filters/canvas_entry_properties_object/) sont les propriétés que vous associez aux Canvas déclenchés par une action ou par l'API. Notez que l'objet `canvas_entry_properties` a une taille maximale de 50 Ko.

{% alert note %}
Pour les canaux de messages in-app en particulier, `canvas_entry_properties` ne peut être référencé que dans Canvas Flow et dans l'éditeur Canvas d'origine si vous avez activé les propriétés d'entrée persistantes dans l'éditeur d'origine dans le cadre de l'accès anticipé précédent.
{% endalert %}

Pour les messages Canvas Flow, `canvas_entry_properties` peut être utilisé dans n'importe quelle étape de message avec ce format Liquid : ``{% raw %} canvas_entry_properties.${property_name} {% endraw %}``. Notez que les événements doivent être des événements personnalisés ou des événements d'achat pour être utilisés de cette manière.

#### Cas d'utilisation {#use-case}

{% raw %}
Supposons qu'un magasin de détail, RetailApp, envoie la requête suivante : `"canvas_entry_properties" : {"product_name" : "shoes", "product_price" : 79.99}`. RetailApp peut extraire le nom du produit (shoes) dans un message avec le Liquid `{{canvas_entry_properties.${product_name}}}`.
{% endraw %}

RetailApp peut également déclencher des messages spécifiques à envoyer pour différentes propriétés `product_name` dans un Canvas qui cible les utilisateurs après qu'ils ont déclenché un événement d'achat. Par exemple, ils peuvent envoyer des messages différents aux utilisateurs qui ont acheté des chaussures et aux utilisateurs qui ont acheté autre chose en ajoutant le Liquid suivant dans une étape de message.

{% raw %}
```markdown
{% if  {{canvas_entry_properties.${product_name}}} == "shoes" %}
  Your order is set to ship soon. While you're waiting, why not step up your shoe care routine with a little upgrade? Check out our selection of shoelaces and premium shoe polish.
{% else %}
  Your order will be on its way shortly. If you missed something, you have until the end of the week to add more items to your cart for the same discounts.
{% endif %}

```
{% endraw %}

{% details Développer pour l'éditeur Canvas d'origine %}

Depuis le 28 février 2023, vous ne pouvez plus créer ni dupliquer de Canvas à l'aide de l'éditeur d'origine. Cette section est disponible à titre de référence uniquement.

Pour les Canvas créés avec l'éditeur d'origine, `canvas_entry_properties` ne peut être référencé que dans la première étape complète d'un Canvas.

{% enddetails %}
{% endtab %}

{% tab Propriétés d'événement %}

{% alert important %}
Vous ne pouvez pas utiliser `event_properties` dans la première étape de message. Vous devez plutôt utiliser `canvas_entry_properties` ou ajouter une étape Parcours d'actions avec l'événement correspondant **avant** l'étape de message qui inclut `event_properties`.
{% endalert %}

Les propriétés d'événement font référence aux propriétés que vous définissez pour les événements personnalisés et les achats. Ces `event_properties` peuvent être utilisées dans les campagnes avec livraison par événement et dans les Canvas.

Dans Canvas Flow, les propriétés d'événement personnalisé et d'événement d'achat peuvent être utilisées en Liquid dans n'importe quelle étape de message qui suit une étape Parcours d'actions. Assurez-vous d'utiliser {% raw %} ``{{event_properties.${property_name}}}``{% endraw %} si vous référencez ces `event_properties`. Ces événements doivent être des événements personnalisés ou des événements d'achat pour être utilisés de cette manière dans le composant de message.

Dans la première étape de message suivant un Parcours d'actions, vous pouvez utiliser les `event_properties` liées à l'événement référencé dans ce Parcours d'actions. Ces `event_properties` ne peuvent être utilisées que si l'utilisateur a effectivement effectué l'action (et n'est pas allé dans le groupe Tous les autres). Vous pouvez avoir d'autres étapes (qui ne sont pas une autre étape Parcours d'actions ou de message) entre ce Parcours d'actions et l'étape de message.

{% details Développer pour l'éditeur Canvas d'origine %}

Depuis le 28 février 2023, vous ne pouvez plus créer ni dupliquer de Canvas à l'aide de l'éditeur d'origine. Cette section est disponible à titre de référence uniquement.

Pour l'éditeur Canvas d'origine, `event_properties` ne peut pas être utilisé dans les étapes complètes planifiées. Cependant, vous pouvez utiliser `event_properties` dans la première étape complète d'un Canvas basé sur une action, même si l'étape complète est planifiée.

{% enddetails %}

{% endtab %}
{% endtabs %}

### Objets imbriqués {#nested-objects}

Vous pouvez utiliser des objets imbriqués (des objets à l'intérieur d'un autre objet) pour envoyer des données JSON imbriquées en tant que propriétés d'événements personnalisés et d'achats. Ces données imbriquées peuvent être utilisées pour modéliser des informations personnalisées dans les messages, déclencher des envois de messages et segmenter les utilisateurs.

Pour en savoir plus, consultez notre page dédiée sur les [objets imbriqués](https://www.braze.com/docs/user_guide/data/custom_data/custom_events/nested_objects/).

## Stockage des propriétés d'événement personnalisé {#custom-event-property-storage}

Les propriétés d'événement personnalisé sont conçues pour vous aider à augmenter la précision du ciblage et rendre les messages encore plus personnalisés. Les propriétés d'événement personnalisé peuvent être stockées dans Braze à court et à long terme.

Vous pouvez segmenter en fonction des valeurs des propriétés d'événement de deux manières :

1. **Sur 30 jours :** Le personnel d'assistance Braze peut activer la segmentation par propriétés d'événement basée sur la fréquence et la récence de valeurs spécifiques de propriétés d'événement au sein des segments Braze. Si vous souhaitez exploiter les propriétés d'événement au sein des segments, contactez votre chargé de compte Braze ou votre gestionnaire de la satisfaction client. Cette option aura un impact sur l'utilisation des données.<br><br>
2. **Sur 30 jours et au-delà :** Pour couvrir la segmentation par propriétés d'événement à court et à long terme, vous pouvez utiliser les [extensions de segments](https://www.braze.com/docs/user_guide/engagement_tools/segments/segment_extension/). Cette fonctionnalité segmente les utilisateurs en fonction des événements personnalisés et des propriétés d'événement suivis au cours des deux dernières années. Cette option n'aura pas d'impact sur l'utilisation des données.

Contactez votre gestionnaire de la satisfaction client Braze pour des recommandations sur la meilleure approche en fonction de vos besoins spécifiques.

[1]: {% image_buster /assets/unlisted_docs/img/custom_events_entitlements/nested_object1.png %}
[2]: {% image_buster /assets/unlisted_docs/img/custom_events_entitlements/nested_object2.png %}
[3]: {% image_buster /assets/unlisted_docs/img/custom_events_entitlements/nested_object3.png %}
[4]: {% image_buster /assets/unlisted_docs/img/custom_events_entitlements/nested_event_properties_segmentation.png %}
[5]: {% image_buster /assets/unlisted_docs/img/custom_events_entitlements/nested_event_properties_personalization.png %}
[6]: {% image_buster /assets/unlisted_docs/img/custom_events_entitlements/schema_generation_example.png %}
[8]: {% image_buster /assets/unlisted_docs/img/custom_events_entitlements/custom_event_analytics_example.png %} "custom_event_analytics_example.png"
[16]: {% image_buster /assets/unlisted_docs/img/custom_events_entitlements/customEventProperties.png %} "customEventProperties.png"
[18]: https://www.braze.com/docs/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/
[19]: https://www.braze.com/docs/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/
[20]: {% image_buster /assets/unlisted_docs/img/custom_events_entitlements/customEventPropertiesNested.png %} "customEventPropertiesNested.png"