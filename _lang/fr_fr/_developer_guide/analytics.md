---
nav_title: Analyse
article_title: "À propos de l'analyse pour le SDK de Braze"
page_order: 2.6
description: "Découvrez les analyses du SDK Braze, afin de mieux comprendre quelles données Braze collecte, la différence entre les événements personnalisés et les attributs personnalisés, et les meilleures pratiques de gestion des analyses."
platform:
  - Android
  - Swift
  - Web
  - Cordova
  - FireOS
  - Flutter
  - React Native
  - Roku
  - Unity
  - .NET MAUI
---

# Analyse {#analytics}

> Découvrez les analyses du SDK Braze, afin de mieux comprendre quelles données Braze collecte, la différence entre les événements personnalisés et les attributs personnalisés, et les meilleures pratiques de gestion des analyses.

{% alert tip %}
Lors de la mise en œuvre de Braze, n'oubliez pas de discuter des objectifs marketing avec votre équipe, afin de décider au mieux des données que vous souhaitez suivre et de la manière dont vous souhaitez les suivre avec Braze. Pour un exemple, consultez notre étude de cas sur l'[application Taxi/covoiturage](#example-case) à la fin de ce guide.
{% endalert %}

## Données collectées automatiquement {#automatically-collected-data}

Certaines données utilisateur sont collectées automatiquement par notre SDK, par exemple : première utilisation de l'application, dernière utilisation de l'application, nombre total de sessions, système d'exploitation de l'appareil, etc. Si vous suivez nos guides d'intégration pour déployer nos SDK, vous pourrez tirer parti de cette [collecte de données par défaut]({{site.baseurl}}/user_guide/data/unification/user_data/sdk_data_collection). Consulter cette liste peut vous aider à éviter de stocker plusieurs fois les mêmes informations sur vos utilisateurs. À l'exception du début et de la fin de session, toutes les autres données suivies automatiquement ne sont pas comptabilisées dans votre consommation de points de donnée.

Consultez notre article [Présentation du SDK]({{site.baseurl}}/developer_guide/getting_started/sdk_overview) pour ajouter à la liste d'autorisation les processus qui bloquent la collecte par défaut de certains éléments de données.

## Événements personnalisés {#custom-events}

Les événements personnalisés sont des actions effectuées par vos utilisateurs ; ils sont parfaitement adaptés au suivi des interactions utilisateur à forte valeur avec votre application. L'enregistrement d'un événement personnalisé peut déclencher un nombre illimité de Campaigns de suivi avec des délais configurables, et permet d'utiliser les filtres de segmentation suivants autour de la récence et de la fréquence de cet événement :

| Options de segmentation | Filtre déroulant | Options d'entrée |
| ---------------------| --------------- | ------------- |
| Vérifier si l'événement personnalisé s'est produit **plus de X fois** | **PLUS DE** | **NOMBRE** |
| Vérifier si l'événement personnalisé s'est produit **moins de X fois** | **MOINS DE** | **NOMBRE** |
| Vérifier si l'événement personnalisé s'est produit **exactement X fois** | **EXACTEMENT** | **NOMBRE** |
| Vérifier si l'événement personnalisé s'est produit pour la dernière fois **après la date X** | **APRÈS** | **DATE** |
| Vérifier si l'événement personnalisé s'est produit pour la dernière fois **avant la date X** | **AVANT** | **DATE** |
| Vérifier si l'événement personnalisé s'est produit pour la dernière fois **il y a plus de X jours** | **PLUS DE** | **NOMBRE DE JOURS** (nombre positif) |
| Vérifier si l'événement personnalisé s'est produit pour la dernière fois **il y a moins de X jours** | **MOINS DE** | **NOMBRE DE JOURS** (nombre positif) |
| Vérifier si l'événement personnalisé s'est produit **plus de X fois (max. = 50)** | **PLUS DE** | au cours des **Y derniers jours (Y = 1,3,7,14,21,30)** |
| Vérifier si l'événement personnalisé s'est produit **moins de X fois (max. = 50)** | **MOINS DE** | au cours des **Y derniers jours (Y = 1,3,7,14,21,30)** |
| Vérifier si l'événement personnalisé s'est produit **exactement X fois (max. = 50)** | **EXACTEMENT** | au cours des **Y derniers jours (Y = 1,3,7,14,21,30)** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Événements personnalisés" }

Braze enregistre le nombre de fois où ces événements se sont produits ainsi que la dernière fois qu'ils ont été effectués par chaque utilisateur à des fins de segmentation. Sur la page d'analyse des **événements personnalisés**, vous pouvez visualiser de manière agrégée la fréquence de chaque événement personnalisé, ainsi que par Segment au fil du temps pour une analyse plus détaillée. Cela est particulièrement utile pour observer l'impact de vos Campaigns sur l'activité des événements personnalisés en examinant les lignes grises que Braze superpose sur les séries temporelles pour indiquer la dernière fois qu'une Campaign a été envoyée.

![Un graphique d'analyse d'événement personnalisé montrant des statistiques sur les utilisateurs qui ont ajouté une carte bancaire et effectué une recherche sur une période de trente jours.]({% image_buster /assets/img_archive/custom_event_analytics_example.png %} "custom_event_analytics_example.png")

{% alert note %}
Les [attributs personnalisés incrémentaux]({{site.baseurl}}/api/endpoints/messaging) peuvent être utilisés pour maintenir un compteur sur une action utilisateur, de manière similaire à un événement personnalisé. Cependant, vous ne pourrez pas visualiser les données d'attributs personnalisés sous forme de série temporelle. Les actions utilisateur qui n'ont pas besoin d'être analysées en série temporelle doivent être enregistrées via cette méthode.
{% endalert %}

### Stockage des événements personnalisés {#custom-event-storage}

Toutes les données de profil utilisateur (événements personnalisés, attributs personnalisés, données personnalisées) sont stockées tant que ces profils sont actifs.

### Propriétés des événements personnalisés {#custom-event-properties}

Avec les propriétés des événements personnalisés, Braze vous permet de définir des propriétés sur les événements personnalisés et les achats. Ces propriétés peuvent ensuite être utilisées pour affiner les conditions de déclenchement, améliorer la personnalisation des messages et générer des analyses plus sophistiquées via l'exportation de données brutes. Les valeurs des propriétés peuvent être des chaînes de caractères, des nombres, des booléens ou des objets temporels. Cependant, les valeurs des propriétés ne peuvent pas être des tableaux.

Par exemple, si une application d'e-commerce souhaitait envoyer un message à un utilisateur lorsqu'il abandonne son panier, elle pourrait également améliorer son audience cible et permettre une personnalisation accrue de la Campaign en ajoutant une propriété d'événement personnalisée pour la `cart_value` des paniers des utilisateurs.

![Un exemple d'événement personnalisé qui enverra une Campaign à un utilisateur ayant abandonné son panier avec une valeur de panier supérieure à 100 et inférieure à 200.]({% image_buster /assets/img_archive/customEventProperties.png %} "customEventProperties.png")

Les propriétés des événements personnalisés peuvent également être utilisées pour la personnalisation dans le modèle de message. Toute Campaign utilisant la [livraison par événement]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery) avec un événement déclencheur peut exploiter les propriétés d'événement personnalisées de cet événement pour la personnalisation des messages. Si une application de jeu souhaitait envoyer un message aux utilisateurs ayant terminé un niveau, elle pourrait personnaliser davantage le message avec une propriété indiquant le temps qu'il a fallu aux utilisateurs pour compléter ce niveau. Dans cet exemple, le message est personnalisé pour trois Segments différents à l'aide de la [logique conditionnelle]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic). La propriété d'événement personnalisée appelée ``time_spent`` peut être incluse dans le message en appelant ``{% raw %} {{event_properties.${time_spent}}} {% endraw %}``.

{% raw %}
```liquid
{% if {{event_properties.${time_spent}}} < 600 %}
Congratulations on beating that level so fast! Check out our online portal where you can play against top players from around the world!
{% elsif {{event_properties.${time_spent}}} < 1800 %}
Don't forget to visit the town store between levels to upgrade your tools.
{% else %}
Talk to villagers for essential tips on how to beat levels!
{% endif %}
```
{% endraw %}

Les propriétés des événements personnalisés sont conçues pour vous aider à personnaliser vos messages ou à créer des Campaigns de livraison par événement granulaires. Si vous souhaitez créer des Segments basés sur la récence et la fréquence des propriétés d'événement, contactez votre gestionnaire du succès des clients ou notre équipe d'assistance.

## Attributs personnalisés {#custom-attributes}

Les attributs personnalisés sont des outils extrêmement flexibles qui vous permettent de cibler les utilisateurs avec une précision bien supérieure à celle des attributs standard. Les attributs personnalisés sont parfaits pour stocker des informations propres à votre marque sur vos utilisateurs. Gardez à l'esprit que nous ne stockons pas d'informations de séries temporelles pour les attributs personnalisés, vous n'obtiendrez donc pas de graphiques basés sur ceux-ci, comme dans l'exemple précédent pour les événements personnalisés.

### Stockage des attributs personnalisés {#custom-attribute-storage}

Toutes les données de profil utilisateur (événements personnalisés, attributs personnalisés, données personnalisées) sont stockées aussi longtemps que ces profils sont actifs.

### Types de données des attributs personnalisés {#custom-attribute-data-types}

Les types de données suivants peuvent être stockés en tant qu'attributs personnalisés :

#### Chaînes de caractères (caractères alphanumériques) {#strings-alphanumeric-characters}

Les attributs de type chaîne de caractères sont utiles pour stocker les saisies des utilisateurs, telles qu'une marque préférée, un numéro de téléphone ou la dernière recherche effectuée dans votre application. Les attributs de type chaîne de caractères sont soumis aux [contraintes de longueur](#length-constraints) des données personnalisées (479 octets ; environ 479 caractères mono-octet ou environ 160 caractères pour les écritures multi-octets comme le japonais).

Le tableau suivant décrit les options de segmentation disponibles pour les attributs de type chaîne de caractères.

| Options de segmentation | Filtre déroulant | Options de saisie |
| ---------------------| --------------- | ------------- |
| Vérifier si l'attribut de type chaîne **correspond exactement** à une chaîne saisie | **EQUALS** | **STRING** |
| Vérifier si l'attribut de type chaîne **correspond partiellement** à une chaîne saisie **OU** à une expression régulière | **MATCHES REGEX** | **STRING** **OU** **REGULAR EXPRESSION** |
| Vérifier si l'attribut de type chaîne **ne correspond pas partiellement** à une chaîne saisie **OU** à une expression régulière | **DOES NOT MATCH REGEX** | **STRING** **OU** **REGULAR EXPRESSION** |
| Vérifier si l'attribut de type chaîne **ne correspond pas** à une chaîne saisie | **DOES NOT EQUAL** | **STRING** |
| Vérifier si l'attribut de type chaîne **existe** sur le profil d'un utilisateur | **IS BLANK** | **N/A** |
| Vérifier si l'attribut de type chaîne **n'existe pas** sur le profil d'un utilisateur | **IS NOT BLANK** | **N/A** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Chaînes de caractères (caractères alphanumériques)" }

{% alert important %}
Lors de la segmentation avec le filtre **DOES NOT MATCH REGEX**, il est nécessaire qu'un attribut personnalisé avec une valeur attribuée existe déjà dans le profil utilisateur. Braze suggère d'utiliser la logique « OR » pour vérifier si un attribut personnalisé est vide afin de cibler correctement les utilisateurs.
{% endalert %}

{% alert tip %}
Pour en savoir plus sur l'utilisation de notre filtre d'expressions régulières, consultez cette documentation sur les [expressions régulières compatibles Perl (PCRE)](http://www.regextester.com/pregsyntax.html).
<br>
Ressources supplémentaires sur les expressions régulières :
- [Les expressions régulières avec Braze]({{site.baseurl}}/user_guide/audience/segments/regex)
- [Débogueur et testeur d'expressions régulières](https://regex101.com/)
- [Tutoriel sur les expressions régulières](https://medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285)
{% endalert %}

#### Tableaux {#arrays}

Les attributs de type tableau sont adaptés au stockage de listes d'informations connexes sur vos utilisateurs. Par exemple, stocker les 100 derniers contenus consultés par un utilisateur dans un tableau permet une segmentation par centres d'intérêt spécifiques.

Les tableaux d'attributs personnalisés sont des ensembles unidimensionnels ; les tableaux multidimensionnels ne sont pas pris en charge. **L'ajout d'un élément à un tableau d'attributs personnalisés ajoute l'élément à la fin du tableau, sauf s'il est déjà présent, auquel cas il est déplacé de sa position actuelle vers la fin du tableau.** Par exemple, si un tableau `['hotdog','hotdog','hotdog','pizza']` est importé, il apparaîtra dans l'attribut de type tableau sous la forme `['hotdog', 'pizza']` car seules les valeurs uniques sont prises en charge.

Si le tableau contient son nombre maximum d'éléments, le premier élément est supprimé et le nouvel élément est ajouté à la fin. Voici un exemple de code illustrant le comportement des tableaux dans le SDK web :

```js
var abUser = appboy.getUser();
// initialize array for this user, assuming max length of favorite_foods is set to 4.
abUser.setCustomUserAttribute('favorite_foods', ['pizza', 'wings', 'pasta']); // => ['pizza', 'wings', 'pasta']
abUser.addToCustomAttributeArray('favorite_foods', 'fries'); // => ['pizza', 'wings', 'pasta', 'fries']
abUser.addToCustomAttributeArray('favorite_foods', 'pizza'); // => ['wings', 'pasta', 'fries', 'pizza']
abUser.addToCustomAttributeArray('favorite_foods', 'ice cream'); // => ['pasta', 'fries', 'pizza', 'ice cream']
```

Le nombre par défaut et maximum d'éléments dans un tableau est de 500. Vous pouvez mettre à jour le nombre maximum de tableaux dans le tableau de bord de Braze, sous **Data Settings** > **Custom Attributes**. Les tableaux dépassant le nombre maximum d'éléments sont tronqués pour contenir le nombre maximum d'éléments.

{% alert note %}
Si un attribut personnalisé de type tableau apparaît sur un profil utilisateur mais n'affiche aucune valeur, vérifiez la **Max Length** de l'attribut dans **Data Settings** > **Custom Attributes**. Une **Max Length** de `0` empêche l'affichage des valeurs sur le profil. Pour les étapes de résolution des problèmes, consultez [Types de données des attributs personnalisés]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#arrays).
{% endalert %}

Le tableau suivant décrit les options de segmentation disponibles pour les attributs de type tableau.

| Options de segmentation | Filtre déroulant | Options de saisie |
| ---------------------| --------------- | ------------- |
| Vérifier si l'attribut de type tableau **inclut une valeur qui correspond exactement** à une valeur saisie | **INCLUDES VALUE** | **STRING** |
| Vérifier si l'attribut de type tableau **n'inclut pas une valeur qui correspond exactement** à une valeur saisie | **DOESN'T INCLUDE VALUE** | **STRING** |
| Vérifier si l'attribut de type tableau **contient une valeur qui correspond partiellement** à une valeur saisie **OU** à une expression régulière | **MATCHES REGEX** | **STRING** **OU** **REGULAR EXPRESSION** |
| Vérifier si l'attribut de type tableau **possède une valeur** | **HAS A VALUE** | **N/A** |
| Vérifier si l'attribut de type tableau **est vide** | **IS EMPTY** | **N/A** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Tableaux" }

{% alert note %}
Nous utilisons les [expressions régulières compatibles Perl (PCRE)](http://www.regextester.com/pregsyntax.html).
{% endalert %}

#### Dates

Les attributs temporels sont utiles pour stocker la date de la dernière action spécifique effectuée, ce qui vous permet d'adresser des messages de réengagement ciblés à vos utilisateurs.

{% alert note %}
La date de la dernière occurrence d'un événement personnalisé ou d'un événement d'achat est automatiquement enregistrée et ne doit pas être enregistrée en double via un attribut temporel personnalisé.
{% endalert %}

Les filtres de date utilisant des dates relatives (par exemple, il y a plus d'un jour, il y a moins de 2 jours) mesurent 1 jour comme 24 heures. Toute Campaign que vous exécutez avec ces filtres inclura tous les utilisateurs par tranches de 24 heures. Par exemple, le filtre « dernière utilisation de l'application il y a plus d'un jour » capturera tous les utilisateurs qui « ont utilisé l'application pour la dernière fois il y a plus de 24 heures » à partir du moment exact où la Campaign est exécutée. Il en va de même pour les Campaigns avec des plages de dates plus longues — cinq jours à compter de l'activation correspondront aux 120 heures précédentes.

Le tableau suivant décrit les options de segmentation disponibles pour les attributs temporels.

| Options de segmentation | Filtre déroulant | Options de saisie |
| ---------------------| --------------- | ------------- |
| Vérifier si l'attribut temporel **est antérieur** à une **date sélectionnée** | **BEFORE** | **CALENDAR DATE SELECTOR** |
| Vérifier si l'attribut temporel **est postérieur** à une **date sélectionnée** | **AFTER** | **CALENDAR DATE SELECTOR** |
| Vérifier si l'attribut temporel remonte à **plus de X jours** | **MORE THAN** | **NUMBER OF DAYS AGO** |
| Vérifier si l'attribut temporel remonte à **moins de X jours** | **LESS THAN** | **NUMBER OF DAYS AGO** |
| Vérifier si l'attribut temporel est **dans plus de X jours** dans le futur | **IN MORE THAN** | **NUMBER OF DAYS IN FUTURE** |
| Vérifier si l'attribut temporel est **dans moins de X jours** dans le futur | **IN LESS THAN** | **NUMBER OF DAYS IN FUTURE** |
| Vérifier si l'attribut temporel **existe** sur le profil d'un utilisateur | **BLANK** | **N/A** |
| Vérifier si l'attribut temporel **n'existe pas** sur le profil d'un utilisateur | **IS NOT BLANK** | **N/A** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Dates" }

#### Nombres {#integers}

Les attributs numériques offrent une grande variété de cas d'usage. Les attributs personnalisés numériques incrémentaux sont utiles pour stocker le nombre de fois qu'une action ou un événement donné s'est produit. Les nombres standard ont toutes sortes d'utilisations, comme l'enregistrement de la pointure, du tour de taille ou du nombre de fois qu'un utilisateur a consulté une fonctionnalité ou une catégorie de produit donnée.

{% alert note %}
Les dépenses ne doivent pas être enregistrées par cette méthode. Elles doivent plutôt être enregistrées via nos [méthodes d'achat]({{site.baseurl}}/developer_guide/analytics#purchase-events--revenue-tracking).
{% endalert %}

Le tableau suivant décrit les options de segmentation disponibles pour les attributs numériques.

| Options de segmentation | Filtre déroulant | Options de saisie |
| ---------------------| --------------- | ------------- |
| Vérifier si l'attribut numérique **est supérieur** à un **nombre** | **MORE THAN** | **NUMBER** |
| Vérifier si l'attribut numérique **est inférieur** à un **nombre** | **LESS THAN** | **NUMBER** |
| Vérifier si l'attribut numérique **est exactement égal** à un **nombre** | **EXACTLY** | **NUMBER** |
| Vérifier si l'attribut numérique **n'est pas égal** à un **nombre** | **DOES NOT EQUAL** | **NUMBER** |
| Vérifier si l'attribut numérique **existe** sur le profil d'un utilisateur | **EXISTS** | **N/A** |
| Vérifier si l'attribut numérique **n'existe pas** sur le profil d'un utilisateur | **DOES NOT EXIST** | **N/A** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Nombres #integers" }

#### Booléens (vrai/faux) {#booleans-truefalse}

Les attributs booléens sont utiles pour stocker les statuts d'abonnement et d'autres données binaires simples sur vos utilisateurs. Les options de saisie que nous proposons vous permettent de trouver les utilisateurs pour lesquels une variable a été explicitement définie sur une valeur booléenne, en plus de ceux pour lesquels aucun enregistrement de cet attribut n'existe encore.

Le tableau suivant décrit les options de segmentation disponibles pour les attributs booléens.

| Options de segmentation | Filtre déroulant | Options de saisie |
| ---------------------| --------------- | ------------- |
| Vérifier si la valeur booléenne **est** | **IS** | **TRUE**, **FALSE**, **TRUE OR NOT SET** ou **FALSE OR NOT SET** |
| Vérifier si la valeur booléenne **existe** sur le profil d'un utilisateur | **EXISTS** | **N/A** |
| Vérifier si la valeur booléenne **n'existe pas** sur le profil d'un utilisateur | **DOES NOT EXIST** | **N/A** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Booléens (vrai/faux)" }

## Événements d'achat / suivi des revenus {#purchase-events-revenue-tracking}

L'utilisation de nos méthodes d'achat pour enregistrer les achats in-app établit la valeur vie client (LTV) pour chaque profil utilisateur individuel. Ces données sont consultables sur notre page de revenus sous forme de graphiques chronologiques.

Le tableau suivant décrit les options de segmentation disponibles pour les événements d'achat.

| Options de segmentation | Filtre déroulant | Options de saisie |
| ---------------------| --------------- | ------------- |
| Vérifier si le montant total dépensé en dollars **est supérieur à** un **nombre** | **GREATER THAN** | **NUMBER** |
| Vérifier si le montant total dépensé en dollars **est inférieur à** un **nombre** | **LESS THAN** | **NUMBER** |
| Vérifier si le montant total dépensé en dollars **est exactement** un **nombre** | **EXACTLY** | **NUMBER** |
| Vérifier si le dernier achat a eu lieu **après la date X** | **AFTER** | **TIME** |
| Vérifier si le dernier achat a eu lieu **avant la date X** | **BEFORE** | **TIME** |
| Vérifier si le dernier achat a eu lieu **il y a plus de X jours** | **MORE THAN** | **TIME** |
| Vérifier si le dernier achat a eu lieu **il y a moins de X jours** | **LESS THAN** | **TIME** |
| Vérifier si l'achat a eu lieu **plus de X (max = 50) fois** | **MORE THAN** | au cours des **Y derniers jours (Y = 1,3,7,14,21,30)** |
| Vérifier si l'achat a eu lieu **moins de X (max = 50) fois** | **LESS THAN** | au cours des **Y derniers jours (Y = 1,3,7,14,21,30)** |
| Vérifier si l'achat a eu lieu **exactement X (max = 50) fois** | **EXACTLY** | au cours des **Y derniers jours (Y = 1,3,7,14,21,30)** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Événements d'achat / suivi des revenus" }

{% alert note %}
Si vous souhaitez segmenter en fonction du nombre de fois qu'un achat spécifique a été effectué, vous devez également enregistrer cet achat individuellement en tant qu'[attribut personnalisé incrémentiel](#integers).
{% endalert %}

## Cas d'utilisation : application de taxi/covoiturage {#example-case}

Dans cet exemple, prenons une application de covoiturage qui souhaite déterminer quelles données utilisateur collecter. Les questions et le brainstorming suivants constituent un excellent modèle à suivre pour les équipes marketing et de développement. À la fin de cet exercice, les deux équipes devraient avoir une compréhension claire des événements et attributs personnalisés qu'il est pertinent de collecter pour atteindre leur objectif.

**Question n° 1 : Quel est l'objectif ?**

Leur objectif est simple : ils veulent que les utilisateurs commandent des trajets en taxi via leur application.

**Question n° 2 : Quelles sont les étapes intermédiaires entre l'installation de l'application et cet objectif ?**

1. Il faut que les utilisateurs commencent le processus d'inscription et renseignent leurs informations personnelles.
2. Il faut que les utilisateurs confirment leur inscription en entrant un code reçu par SMS dans l'application.
3. Ils doivent essayer de commander un taxi.
4. Pour commander un taxi, il faut que des taxis soient disponibles au moment de leur recherche.

Ces actions peuvent ensuite être associées aux événements personnalisés suivants :

- Inscription commencée
- Inscription terminée
- Appels de taxi réussis
- Appels de taxi échoués

Une fois les événements définis, vous pouvez lancer les campagnes suivantes :

1. Envoyer des messages aux utilisateurs qui ont commencé l'inscription sans déclencher l'événement « Inscription terminée » dans un certain délai.
2. Envoyer des messages de félicitations aux utilisateurs qui ont terminé leur inscription.
3. Envoyer des excuses et un crédit promotionnel aux utilisateurs dont les appels de taxi ont échoué et qui n'ont pas été suivis d'un appel réussi dans un certain délai.
4. Envoyer des promotions aux utilisateurs les plus actifs ayant de nombreux appels de taxi réussis pour les remercier de leur fidélité.

Et bien plus encore !

**Question n° 3 : Quelles autres informations pourrions-nous connaître sur nos utilisateurs pour enrichir nos messages ?**

- Ont-ils un crédit promotionnel ?
- Quelle note moyenne donnent-ils à leurs chauffeurs ?
- Des codes promotionnels uniques pour l'utilisateur ?

Ces caractéristiques peuvent ensuite être associées aux attributs personnalisés suivants :

- Solde de crédit promotionnel (type décimal)
- Note moyenne du chauffeur (type nombre)
- Code promotionnel unique (type chaîne de caractères)

L'ajout de ces attributs vous permettrait d'envoyer des campagnes aux utilisateurs, par exemple :

1. Rappeler aux utilisateurs qui ne se sont pas connectés depuis sept jours mais qui disposent d'un crédit promotionnel que ce crédit existe et qu'ils devraient revenir sur l'application pour l'utiliser !
2. Envoyer des messages aux utilisateurs qui donnent de mauvaises notes aux chauffeurs pour obtenir un retour direct et comprendre pourquoi ils n'ont pas apprécié leur trajet.
3. Utiliser nos [fonctionnalités de modélisation et de personnalisation des messages]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize) pour intégrer l'attribut de code promotionnel unique dans les messages adressés aux utilisateurs.

## Bonnes pratiques {#best-practices}

### Bonnes pratiques générales {#general-best-practices}

#### Utiliser les propriétés d'événement {#use-event-properties}

- Nommez un événement personnalisé de manière à décrire une action effectuée par un utilisateur.
- Faites un usage généreux des propriétés d'événement personnalisées pour représenter les données importantes relatives à un événement.
- Par exemple, plutôt que de capturer un événement personnalisé distinct pour chacun des 50 films visionnés, il serait plus efficace de capturer simplement le visionnage d'un film comme événement et d'inclure le nom du film en tant que propriété d'événement.

### Bonnes pratiques de développement {#development-best-practices}

#### Définir des ID utilisateur pour chaque utilisateur {#set-user-ids-for-every-user}

Des ID utilisateur doivent être définis pour chacun de vos utilisateurs. Ils doivent être immuables et accessibles lorsqu'un utilisateur ouvre l'application. Nous **recommandons vivement** de fournir cet identifiant, car il vous permettra de :

- Suivre vos utilisateurs sur plusieurs appareils et plateformes, améliorant ainsi la qualité de vos données comportementales et démographiques.
- Importer des données sur vos utilisateurs à l'aide de notre [API de données utilisateur]({{site.baseurl}}/api/endpoints/user_data).
- Cibler des utilisateurs spécifiques avec notre [API de communication]({{site.baseurl}}/api/endpoints/messaging) pour les messages généraux et transactionnels.

Les ID utilisateur doivent comporter moins de 512 caractères et doivent rester privés et difficiles à obtenir (par exemple, il ne doit pas s'agir d'une simple adresse e-mail ou d'un nom d'utilisateur). Si un tel identifiant n'est pas disponible, Braze attribuera un identifiant unique à vos utilisateurs, mais vous ne disposerez pas des fonctionnalités mentionnées pour les ID utilisateur. Vous devez éviter de définir des ID utilisateur pour les utilisateurs pour lesquels vous ne disposez pas d'un identifiant unique qui leur est propre en tant qu'individu. La transmission d'un identifiant d'appareil n'offre aucun avantage par rapport au suivi automatique des utilisateurs anonymes proposé par défaut par Braze. Voici quelques exemples d'ID utilisateur adaptés et inadaptés.

Bonnes options pour les ID utilisateur :

- Adresse e-mail hachée ou nom d'utilisateur unique
- Identifiant de base de données unique

Ces éléments ne doivent pas être utilisés comme ID utilisateur :

- Identifiant d'appareil
- Nombre aléatoire ou identifiant de session
- Tout identifiant non unique
- Adresse e-mail
- Identifiant utilisateur d'un autre fournisseur tiers

{% multi_lang_include alerts/important_alerts.md alert='SDK auth' %}

#### Donner des noms lisibles aux événements et attributs personnalisés {#give-custom-events-and-attributes-readable-names}

Imaginez que vous êtes un marketeur qui commence à utiliser Braze un an ou deux après le déploiement : parcourir une liste déroulante remplie de noms comme « usr_no_acct » sans contexte supplémentaire peut être intimidant. Donner à vos événements et attributs des noms identifiables et lisibles facilitera la vie de tous les utilisateurs de votre plateforme. Voici quelques bonnes pratiques à considérer :

- Ne commencez pas un événement personnalisé par un caractère numérique. La liste déroulante est triée par ordre alphabétique et commencer par un caractère numérique rend plus difficile la segmentation par le filtre de votre choix.
- Essayez de ne pas utiliser d'abréviations obscures ou de jargon technique lorsque c'est possible.
  - Exemple : `usr_ctry` peut convenir comme nom de variable pour le pays d'un utilisateur dans un morceau de code, mais l'attribut personnalisé devrait être envoyé à Braze sous une forme comme `user_country` pour apporter de la clarté à un marketeur utilisant le tableau de bord par la suite.

#### Ne journaliser les attributs que lorsqu'ils changent {#only-log-attributes-when-they-change}

Nous comptabilisons chaque attribut transmis à Braze comme un point de donnée, même si l'attribut transmis contient la même valeur que celle déjà enregistrée. Ne journaliser les données que lorsqu'elles changent permet d'éviter une utilisation redondante des points de donnée et favorise une expérience plus fluide en évitant les appels API inutiles.

#### Éviter de générer des noms d'événements de manière programmatique {#avoid-programmatically-generating-event-names}

Si vous créez constamment de nouveaux noms d'événements, il vous sera impossible de segmenter vos utilisateurs de manière pertinente. Vous devriez généralement capturer des événements génériques (« A regardé une vidéo » ou « A lu un article ») plutôt que des événements très spécifiques tels que (« A regardé Gangnam Style » ou « A lu l'article : Les 10 meilleurs restaurants du centre-ville de Manhattan »). Les données spécifiques à l'événement doivent être incluses en tant que propriété d'événement, et non dans le nom de l'événement.

### Limitations et contraintes techniques {#technical-limitations-and-constraints}

Soyez attentif aux limitations et contraintes suivantes lors du déploiement d'événements personnalisés :

#### Contraintes de longueur {#length-constraints}

Braze impose une limite de longueur en octets (479 octets) pour les noms d'événements personnalisés, les noms d'attributs personnalisés (clés) et les valeurs de chaîne de caractères des événements personnalisés. Les valeurs dépassant cette limite sont tronquées. Exprimé en caractères, cela correspond à environ 479 caractères mono-octet (par exemple, ASCII), ou environ 160 caractères pour les scripts multi-octets tels que le japonais (en supposant environ 3 octets par caractère en UTF-8). Dans l'idéal, gardez les noms et les valeurs aussi courts que possible pour améliorer les performances réseau et la consommation de batterie de votre application — si possible, limitez-les à 50 caractères.

#### Contraintes de contenu {#content-constraints}
Le contenu suivant sera automatiquement supprimé de vos attributs et événements. Veillez à ne pas utiliser les éléments suivants :

- Espaces en début et en fin de chaîne
- Retours à la ligne
- Tous les caractères non numériques dans les numéros de téléphone
  - Exemple : « (732) 178-1038 » sera condensé en « 7321781038 »
- Les caractères non-espacement doivent être convertis en espaces
- Le symbole $ ne doit pas être utilisé comme préfixe pour les événements personnalisés
- Toute valeur d'encodage UTF-8 invalide
  -  « My \x80 Field » sera condensé en « My Field »

#### Clés réservées {#reserved-keys}

Les clés suivantes sont réservées et ne peuvent pas être utilisées comme propriétés d'événement personnalisées :

- `time`
- `product_id`
- `quantity`
- `event_name`
- `price`
- `currency`

#### Définitions des valeurs {#value-definitions}

- Les valeurs entières sont sur 64 bits
- Les décimales ont 15 chiffres décimaux par défaut

### Analyser un champ de nom générique {#parsing-a-generic-name-field}

Si un seul champ de nom générique existe pour un utilisateur (par exemple, « JohnDoe »), vous pouvez attribuer ce titre entier à l'attribut Prénom de votre utilisateur. Vous pouvez également tenter d'extraire le prénom et le nom de famille de l'utilisateur en utilisant les espaces comme séparateurs, mais cette dernière méthode comporte le risque potentiel de mal nommer certains de vos utilisateurs.