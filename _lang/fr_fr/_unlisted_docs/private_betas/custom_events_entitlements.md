---
article_title: Événements personnalisés
permalink: "/custom_events_entitlements/"
hidden: true
---

# [![Cours d'apprentissage Braze]({% image_buster /assets/unlisted_docs/img/logos/bl_icon3.png %})](https://learning.braze.com/custom-events-and-attributes){: style="float:right;width:120px;border:0;" class="noimgborder"}Événements personnalisés {#braze-learning-course-image_buster-assetsunlisted_docsimglogosbl_icon3png-httpslearningbrazecomcustom-events-and-attributes-stylefloatrightwidth120pxborder0-classnoimgbordercustom-events}

> Cet article décrit les événements personnalisés et leurs propriétés, les filtres de segmentation associés, les propriétés d'entrée Canvas, les analyses pertinentes, et plus encore. Pour en savoir plus sur les événements Braze en général, consultez [Événements]({{site.baseurl}}/user_guide/data/activation/events).

Les événements personnalisés sont des actions effectuées par vos utilisateurs ou des mises à jour les concernant. Lorsque des événements personnalisés sont enregistrés, ils peuvent déclencher un nombre et un type quelconques de Campaigns de suivi. Vous pouvez ensuite utiliser des [filtres de segmentation](#segmentation-filters) pour segmenter les utilisateurs en fonction de la récence et de la fréquence de ces événements personnalisés. Cela fait des événements personnalisés l'outil idéal pour suivre les interactions utilisateur à forte valeur au sein de votre application.

## Cas d'usage {#use-cases}

Voici quelques cas d'usage courants des événements personnalisés :

{% multi_lang_include data_activation/custom_event_use_cases.md %}

## Droits {#entitlements}

Les droits déterminent votre capacité en événements personnalisés, c'est-à-dire le nombre de noms d'événements différents que vous pouvez définir. Vous pouvez disposer de jusqu'à 2 000 événements personnalisés par espace de travail. Si vous avez besoin d'augmenter cette capacité, contactez votre gestionnaire de compte Braze pour en savoir plus.

Lorsque votre espace de travail approche du nombre maximum d'événements personnalisés, vous recevrez des notifications dans le tableau de bord et par e-mail pour vous aider à anticiper.

Même après avoir atteint la capacité maximale, les événements personnalisés existants peuvent toujours être reçus. Cependant, vous ne pourrez pas créer de nouveaux événements personnalisés. Toute donnée reçue pour des événements personnalisés qui n'existent pas encore ne sera pas traitée.

## Gestion des événements personnalisés {#managing-custom-events}

Vous pouvez gérer, créer ou bloquer des événements personnalisés dans le tableau de bord en accédant à **Data Settings** > **Custom Events**.

Sélectionnez le menu à côté d'un événement personnalisé pour effectuer les actions suivantes :

### Blocage {#blocklisting}

Vous pouvez bloquer des événements personnalisés individuels via le menu d'actions, ou sélectionner et bloquer jusqu'à 100 événements en masse.

Lorsque vous bloquez un événement personnalisé :

{% multi_lang_include data_activation/custom_event_block_effects.md %}

De plus, si un événement personnalisé bloqué est actuellement référencé par des filtres ou des déclencheurs dans d'autres zones de Braze, une fenêtre modale d'avertissement apparaîtra pour expliquer que toutes les instances des filtres ou déclencheurs qui le référencent seront supprimées et archivées.

### Ajout de descriptions {#adding-descriptions}

Vous pouvez ajouter une description à un événement personnalisé après sa création si vous disposez de l'[autorisation utilisateur]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) `Manage Events, Attributes, Purchases`. Sélectionnez **Edit description** pour l'événement personnalisé et saisissez ce que vous souhaitez, comme une note pour votre équipe.

## Ajout d'étiquettes {#adding-tags}

Vous pouvez ajouter des étiquettes à un événement personnalisé après sa création si vous disposez de l'[autorisation utilisateur]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) « Gérer les événements, attributs et achats ». Les étiquettes peuvent ensuite être utilisées pour filtrer la liste des événements.

### Consultation des rapports d'utilisation {#viewing-usage-reports}

Le rapport d'utilisation répertorie tous les Canvas, Campaigns et Segments qui utilisent un événement personnalisé spécifique. La liste n'inclut pas les utilisations de Liquid.

Vous pouvez consulter jusqu'à 100 rapports d'utilisation à la fois en cochant les cases de plusieurs événements personnalisés, puis en sélectionnant **Afficher le rapport d'utilisation**.

## Exporter des données {#exporting-data}

Pour exporter la liste des événements personnalisés sous forme de fichier CSV, sélectionnez le bouton **Export all** en haut de la page. Le fichier CSV sera généré et un lien de téléchargement vous sera envoyé par e-mail.

## Enregistrement des événements personnalisés {#logging-custom-events}

Les événements personnalisés nécessitent une configuration supplémentaire. Consultez les liens vers la documentation de chaque plateforme pour trouver les méthodes utilisées pour enregistrer des événements personnalisés et ajouter des propriétés et des quantités.

{% details Développer pour la documentation par plateforme %}

- [Android et FireOS]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=android)
- [iOS]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=swift)
- [Web]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=web)
- [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/analytics#logging-custom-events)
- [Unity]({{site.baseurl}}/developer_guide/analytics/logging_events/?sdktab=unity)
- [Xamarin]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics#tracking-custom-events)
- [Roku]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=roku)

{% enddetails %}

## Stockage des événements personnalisés {#custom-event-storage}

Toutes les données stockées sur le **profil utilisateur**, y compris les métadonnées des événements personnalisés (première ou dernière occurrence, nombre total et X sur Y au cours des 30 derniers jours), sont conservées indéfiniment tant que chaque profil est [actif]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival#active-users).

## Filtres de segmentation {#segmentation-filters}

Le tableau suivant présente les filtres disponibles pour segmenter les utilisateurs par événements personnalisés.

| Options de segmentation | Filtre déroulant | Options de saisie |
| ---------------------| --------------- | ------------- |
| Vérifier si l'événement personnalisé s'est produit **plus de X fois** | **MORE THAN** | **NUMBER** |
| Vérifier si l'événement personnalisé s'est produit **moins de X fois** | **LESS THAN** | **NUMBER** |
| Vérifier si l'événement personnalisé s'est produit **exactement X fois** | **EXACTLY** | **NUMBER** |
| Vérifier si l'événement personnalisé s'est produit pour la dernière fois **après la date X** | **AFTER** | **TIME** |
| Vérifier si l'événement personnalisé s'est produit pour la dernière fois **avant la date X** | **BEFORE** | **TIME** |
| Vérifier si l'événement personnalisé s'est produit pour la dernière fois **il y a plus de X jours** | **MORE THAN** | **NUMBER OF DAYS AGO** (nombre positif) |
| Vérifier si l'événement personnalisé s'est produit pour la dernière fois **il y a moins de X jours** | **LESS THAN** | **NUMBER OF DAYS AGO** (nombre positif) |
| Vérifier si l'événement personnalisé s'est produit **plus de X fois (max = 50)** | **MORE THAN** | au cours des **Y derniers jours (Y = 1,3,7,14,21,30)** |
| Vérifier si l'événement personnalisé s'est produit **moins de X fois (max = 50)** | **LESS THAN** | au cours des **Y derniers jours (Y = 1,3,7,14,21,30)** |
| Vérifier si l'événement personnalisé s'est produit **exactement X fois (max = 50)** | **EXACTLY** | au cours des **Y derniers jours (Y = 1,3,7,14,21,30)** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Analyse {#analytics}

Braze enregistre le nombre de fois où des événements personnalisés se sont produits ainsi que la dernière fois qu'ils ont été effectués par chaque utilisateur à des fins de segmentation. Pour la configuration des rapports, les filtres et les options d'exportation, consultez le [rapport des événements personnalisés]({{site.baseurl}}/user_guide/analytics/reports/custom_events_report).

Sur la page **Custom Events Report**, vous pouvez visualiser de manière agrégée la fréquence de chaque événement personnalisé. Les lignes grises superposées sur la série temporelle indiquent la dernière fois qu'une campagne a été envoyée, ce qui est utile pour observer l'impact de vos campagnes sur l'activité des événements personnalisés.

![Graphique du nombre d'événements personnalisés sur la page Custom Events du tableau de bord montrant les tendances pour un événement personnalisé][8]

Vous pouvez également utiliser les **Filtres** pour ventiler vos événements personnalisés par heure, utilisateurs actifs mensuels (MAU), Segments ou formules de KPI.

{% alert tip %}
[Incrémentez des attributs personnalisés]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes#integers) pour tenir un compteur sur une action utilisateur similaire à un événement personnalisé. Cependant, vous ne pouvez pas visualiser les données d'attributs personnalisés dans une série temporelle. Les actions utilisateur qui n'ont pas besoin d'être analysées dans une série temporelle doivent être enregistrées à l'aide de cette méthode.
{% endalert %}

### Pourquoi l'analyse des événements personnalisés ne s'affiche pas {#why-custom-events-analytics-arent-showing}

Les Segments créés à partir de données d'événements personnalisés ne peuvent pas afficher les données historiques antérieures à leur création.

## Propriétés des événements personnalisés {#custom-event-properties}

Les propriétés des événements personnalisés sont des métadonnées ou des attributs d'événements personnalisés qui décrivent une occurrence spécifique d'un événement. Ces propriétés peuvent être utilisées pour affiner les conditions de déclenchement, améliorer la personnalisation des messages, suivre les conversions et générer des analyses plus sophistiquées grâce à l'exportation de données brutes.

Les propriétés des événements personnalisés ne sont pas stockées sur le profil Braze et ne consomment donc pas de points de donnée (consultez [Points de donnée](#data-points) pour les exceptions).

{% alert important %}
Chaque événement personnalisé ou achat peut avoir jusqu'à 256 propriétés d'événement personnalisé distinctes. Si un événement personnalisé ou un achat est enregistré avec plus de 256 propriétés, seules les 256 premières seront capturées et disponibles pour utilisation.
{% endalert %}

### Format attendu {#expected-format}

Les valeurs des propriétés doivent être un objet dont les clés sont les noms des propriétés et les valeurs sont les valeurs des propriétés. Les noms des propriétés doivent être des chaînes de caractères non vides de 255 caractères maximum, sans signe dollar (`$`) en début.

Les valeurs des propriétés peuvent être de l'un des types de données suivants :

| Type de données | Description |
| --- | --- |
| Nombres | Sous forme d'[entiers](https://en.wikipedia.org/wiki/Integer) ou de [floats](https://en.wikipedia.org/wiki/Floating-point_arithmetic) |
| Booléens | Valeur `true` ou `false`. |
| Dates et heures | Formatées en tant que chaînes de caractères au format [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) ou `yyyy-MM-dd'T'HH:mm:ss:SSSZ`. Non prises en charge dans les tableaux. |
| Chaînes de caractères | 255 caractères ou moins. |
| Tableaux | Les tableaux ne peuvent pas contenir de dates et heures. |
| Objets | Les objets seront ingérés sous forme de chaînes de caractères. |
| Objets imbriqués | Objets à l'intérieur d'autres objets. Pour en savoir plus, consultez la section de cet article sur les [Objets imbriqués](#nested-objects).
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Les objets de propriétés d'événement contenant des valeurs de tableau ou d'objet peuvent avoir un payload de propriété d'événement allant jusqu'à 100&nbsp;Ko.

Vous pouvez modifier le type de données de votre propriété d'événement personnalisé, mais soyez conscient des impacts liés au [changement de types de données]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#changing-custom-attribute-or-event-data-type) après la collecte des données.

### Utiliser les propriétés des événements personnalisés {#using-custom-event-properties}

Les propriétés des événements personnalisés peuvent être utilisées pour qualifier les déclencheurs de Campaign, suivre les conversions et personnaliser les messages.

#### Déclencher des messages {#trigger-messages}

Utilisez les propriétés des événements personnalisés pour affiner davantage votre audience pour une Campaign ou un Canvas spécifique. Par exemple, si vous disposez d'une application d'e-commerce et souhaitez envoyer un message à un utilisateur lorsqu'il abandonne son panier, vous pouvez ajouter une propriété d'événement personnalisé `cart value` pour améliorer votre audience cible et permettre une personnalisation accrue de la Campaign.

![Filtres de propriétés d'événement personnalisé pour un panier abandonné. Deux filtres sont combinés avec un opérateur ET pour envoyer cette Campaign aux utilisateurs qui ont abandonné leur panier avec une valeur de panier comprise entre 100 et 200 dollars][16]

Les propriétés d'événement personnalisé imbriquées sont également prises en charge dans la [livraison par événement][19].

![Filtres de propriétés d'événement personnalisé pour un panier abandonné. Un filtre est sélectionné si un article du panier a un prix supérieur à 100 dollars.][20]

#### Personnaliser les messages {#personalize-messages}

Vous pouvez également utiliser les propriétés des événements personnalisés pour la personnalisation au sein du modèle de message. Toute Campaign utilisant la [livraison par événement][19] avec un événement déclencheur peut utiliser les propriétés d'événement personnalisé de cet événement pour la personnalisation des messages.

Par exemple, si vous disposez d'une application de jeu et souhaitez envoyer un message aux utilisateurs qui ont terminé un niveau, vous pourriez personnaliser davantage votre message avec une propriété indiquant le temps mis par les utilisateurs pour terminer ce niveau. Dans cet exemple, le message est personnalisé pour trois Segments différents à l'aide de la [logique conditionnelle][18]. La propriété d'événement personnalisé appelée `time_spent` peut être incluse dans le message en appelant ``{% raw %} {{event_properties.${time_spent}}} {% endraw %}``.

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
Si l'utilisateur n'a pas de connexion Internet, les messages in-app déclenchés avec des propriétés d'événement personnalisé modélisées (par exemple, {% raw %}``{{event_properties.${time_spent}}}``{% endraw %}) échoueront et ne s'afficheront pas.
{% endalert %}

Pour une liste complète des étiquettes Liquid qui feront en sorte que les messages in-app soient distribués en tant que messages in-app modélisés, consultez les [Questions fréquemment posées]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/faq/#what-are-templated-in-app-messages/).

##### Considérations relatives aux filtres {#considerations-with-filters}

- **Appels API :** Lorsque vous effectuez des appels API et utilisez le filtre « est vide », une propriété d'événement personnalisé est considérée comme « vide » si elle est exclue de l'appel. Par exemple, si vous incluiez `"event_property": ""`, vos utilisateurs seraient considérés comme « non vides ».
- **Entiers :** Lorsque vous filtrez par une propriété d'événement personnalisé de type nombre et que le nombre est très grand, n'utilisez pas le filtre « exactement ». Si un nombre est trop grand, il peut être arrondi à une certaine longueur, et votre filtre ne fonctionnera donc pas comme prévu.

#### Segmentation

Utilisez la segmentation par propriétés d'événement pour cibler les utilisateurs en fonction des événements personnalisés réalisés et des propriétés associées à ces événements. Cela augmente vos options de filtrage lors de la segmentation par achats et événements personnalisés.

Les propriétés d'événement pour les événements personnalisés sont mises à jour en temps réel pour tout Segment qui les utilise. Vous pouvez gérer les propriétés en accédant à **Data Settings** > **Custom Events** et en sélectionnant **Manage properties** pour l'événement personnalisé associé. Les propriétés d'événement personnalisé utilisées dans certains filtres de Segment ont un historique de consultation maximum de 30 jours.

##### Ajouter des propriétés d'événement pour la segmentation {#adding-event-properties-for-segmentation}

Vous aurez besoin de l'[autorisation utilisateur]({{site.baseurl}}/user_guide/data/data_points#viewing-data-point-usage) « Manage Custom Event Property Segmentation » pour créer des Segments basés sur la récence et la fréquence des propriétés d'événement.

Par défaut, vous pouvez avoir 20 propriétés d'événement segmentables par espace de travail. Contactez votre gestionnaire de compte Braze pour augmenter cette limite.

Pour ajouter des propriétés d'événement pour la segmentation, procédez comme suit :

1. Accédez à votre événement personnalisé et sélectionnez **Manage properties**.
2. Sélectionnez le bouton **Enable segmentation** pour ajouter la propriété d'événement à la segmentation. Vous pouvez accéder à des options de filtrage supplémentaires lors de la segmentation.

Les filtres de segmentation par propriétés d'événement incluent :

{% multi_lang_include data_activation/custom_event_property_filters.md %}

![Un groupe de filtres « a l'événement "Abandoned Cart" avec la propriété "number of items" et la valeur "2" "plus de" "1" "1 fois au cours des "30" derniers jours calendaires.][3]

Les données ne sont enregistrées pour une propriété d'événement donnée qu'après son activation par votre gestionnaire du succès des clients, et les propriétés d'événement ne sont disponibles qu'à partir de cette date.

##### Points de donnée {#data-points}

En ce qui concerne l'utilisation de l'abonnement, les propriétés d'événement personnalisé activées pour la segmentation avec les filtres suivants sont toutes comptées comme des points de donnée distincts, en plus du point de donnée comptabilisé par l'événement personnalisé lui-même :

- `X Custom Event Property in Y Days`
- `X Purchase Property in Y Days`

### Propriétés d'entrée Canvas et propriétés d'événement {#canvas-entry-properties-and-event-properties}

Vous pouvez utiliser `canvas_entry_properties` et `event_properties` dans vos parcours utilisateur Canvas. Consultez [Propriétés d'entrée Canvas et propriétés d'événement]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties) pour plus d'informations et d'exemples.

{% tabs local %}
{% tab Propriétés d'entrée Canvas %}

Les [propriétés d'entrée Canvas]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object) sont les propriétés que vous mappez pour les Canvas déclenchés par une action ou par l'API. Notez que l'objet `canvas_entry_properties` a une limite de taille maximale de 50 Ko.

{% alert note %}
Pour les canaux de messages in-app spécifiquement, `canvas_entry_properties` ne peut être référencé dans Canvas Flow et l'éditeur Canvas d'origine que si vous avez activé les propriétés d'entrée persistantes dans l'éditeur d'origine dans le cadre de l'accès anticipé précédent.
{% endalert %}

Pour les messages Canvas Flow, `canvas_entry_properties` peut être utilisé dans n'importe quelle étape Message avec ce format Liquid : ``{% raw %} canvas_entry_properties.${property_name} {% endraw %}``. Notez que les événements doivent être des événements personnalisés ou des événements d'achat pour être utilisés de cette manière.

#### Cas d'usage {#use-case}

{% raw %}
Imaginons qu'un magasin de détail, RetailApp, ait la requête suivante : `"canvas_entry_properties" : {"product_name" : "shoes", "product_price" : 79.99}`. RetailApp peut intégrer le nom du produit (shoes) dans un message avec le Liquid `{{canvas_entry_properties.${product_name}}}`.
{% endraw %}

RetailApp peut également déclencher des messages spécifiques à envoyer pour différentes propriétés `product_name` dans un Canvas qui cible les utilisateurs après qu'ils ont déclenché un événement d'achat. Par exemple, ils peuvent envoyer des messages différents aux utilisateurs qui ont acheté des chaussures et aux utilisateurs qui ont acheté autre chose en ajoutant le Liquid suivant dans une étape Message.

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
Vous ne pouvez pas utiliser `event_properties` dans la première étape Message. Vous devez plutôt utiliser `canvas_entry_properties` ou ajouter une étape Action Paths avec l'événement correspondant **avant** l'étape Message qui inclut `event_properties`.
{% endalert %}

Les propriétés d'événement font référence aux propriétés que vous définissez pour les événements personnalisés et les achats. Ces `event_properties` peuvent être utilisées dans les Campaigns avec livraison par événement et dans les Canvas.

Dans Canvas Flow, les propriétés des événements personnalisés et des événements d'achat peuvent être utilisées en Liquid dans n'importe quelle étape Message qui suit une étape Action Paths. Assurez-vous d'utiliser {% raw %} ``{{event_properties.${property_name}}}``{% endraw %} lorsque vous référencez ces `event_properties`. Ces événements doivent être des événements personnalisés ou des événements d'achat pour être utilisés de cette manière dans le composant Message.

Dans la première étape Message suivant un Action Path, vous pouvez utiliser les `event_properties` liées à l'événement référencé dans cet Action Path. Ces `event_properties` ne peuvent être utilisées que si l'utilisateur a effectivement réalisé l'action (et n'est pas allé dans le groupe Everyone Else). Vous pouvez avoir d'autres étapes (qui ne sont ni un autre Action Paths ni une étape Message) entre cet Action Paths et l'étape Message.

{% details Développer pour l'éditeur Canvas d'origine %}

Depuis le 28 février 2023, vous ne pouvez plus créer ni dupliquer de Canvas à l'aide de l'éditeur d'origine. Cette section est disponible à titre de référence uniquement.

Pour l'éditeur Canvas d'origine, `event_properties` ne peut pas être utilisé dans les étapes complètes planifiées. Cependant, vous pouvez utiliser `event_properties` dans la première étape complète d'un Canvas basé sur une action, même si l'étape complète est planifiée.

{% enddetails %}

{% endtab %}
{% endtabs %}

### Objets imbriqués {#nested-objects}

Vous pouvez utiliser des objets imbriqués (des objets à l'intérieur d'un autre objet) pour envoyer des données JSON imbriquées en tant que propriétés d'événements personnalisés et d'achats. Ces données imbriquées peuvent être utilisées pour modéliser des informations personnalisées dans les messages, déclencher des envois de messages et segmenter les utilisateurs.

Pour en savoir plus, consultez notre page dédiée sur les [Objets imbriqués]({{site.baseurl}}/user_guide/data/activation/events/custom_events/nested_objects).

## Stockage des propriétés d'événement personnalisé {#custom-event-property-storage}

Les propriétés d'événement personnalisé sont conçues pour vous aider à affiner la précision de votre ciblage et à rendre vos messages encore plus personnalisés. Les propriétés d'événement personnalisé peuvent être stockées dans Braze à court et à long terme.

Vous pouvez segmenter en fonction des valeurs des propriétés d'événement de deux manières :

1. **Dans les 30 jours :** le personnel d'assistance Braze peut activer la segmentation par propriété d'événement en fonction de la fréquence et de la récence de valeurs spécifiques de propriétés d'événement au sein des Segments Braze. Si vous souhaitez tirer parti des propriétés d'événement au sein des Segments, contactez votre responsable de compte Braze ou votre gestionnaire du succès des clients. Cette option aura un impact sur l'utilisation des données.<br><br>
2. **Dans les 30 jours et au-delà :** pour couvrir la segmentation par propriété d'événement à court et à long terme, vous pouvez utiliser les [extensions de segments]({{site.baseurl}}/user_guide/audience/segments/segment_extension). Cette fonctionnalité segmente les utilisateurs en fonction des événements personnalisés et des propriétés d'événement suivis au cours des deux dernières années. Cette option n'aura pas d'impact sur l'utilisation des données.

Contactez votre gestionnaire du succès des clients Braze pour obtenir des recommandations sur la meilleure approche en fonction de vos besoins spécifiques.

[1]: {% image_buster /assets/unlisted_docs/img/custom_events_entitlements/nested_object1.png %}
[2]: {% image_buster /assets/unlisted_docs/img/custom_events_entitlements/nested_object2.png %}
[3]: {% image_buster /assets/unlisted_docs/img/custom_events_entitlements/nested_object3.png %}
[4]: {% image_buster /assets/unlisted_docs/img/custom_events_entitlements/nested_event_properties_segmentation.png %}
[5]: {% image_buster /assets/unlisted_docs/img/custom_events_entitlements/nested_event_properties_personalization.png %}
[6]: {% image_buster /assets/unlisted_docs/img/custom_events_entitlements/schema_generation_example.png %}
[8]: {% image_buster /assets/unlisted_docs/img/custom_events_entitlements/custom_event_analytics_example.png %} "custom_event_analytics_example.png"
[16]: {% image_buster /assets/unlisted_docs/img/custom_events_entitlements/customEventProperties.png %} "customEventProperties.png"
[18]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/
[19]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/
[20]: {% image_buster /assets/unlisted_docs/img/custom_events_entitlements/customEventPropertiesNested.png %} "customEventPropertiesNested.png"