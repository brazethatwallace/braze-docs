---
nav_title: Événements personnalisés
article_title: Événements personnalisés
page_order: 1
page_type: reference
description: "Cet article décrit les événements et propriétés personnalisés, la segmentation, l'utilisation, les propriétés d'entrée dans Canvas, l'endroit où consulter les analyses pertinentes, et plus encore."
search_rank: 2
---

# [![Cours d'apprentissage Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/custom-events-and-attributes){: style="float:right;width:120px;border:0;" class="noimgborder"} Événements personnalisés {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomcustom-events-and-attributes-stylefloatrightwidth120pxborder0-classnoimgbordercustom-events}

> Cet article décrit les événements et propriétés personnalisés, l'historique des événements du profil utilisateur, les filtres de segmentation associés, les propriétés d'entrée dans Canvas, les analyses pertinentes, et plus encore. Pour en savoir plus sur les événements de Braze en général, consultez la rubrique [Événements]({{site.baseurl}}/user_guide/data/activation/events).

Les événements personnalisés sont des actions effectuées par vos utilisateurs, ou des mises à jour les concernant. Lorsque des événements personnalisés sont enregistrés, ils peuvent déclencher un nombre et un type quelconque de campagnes de suivi. Vous pouvez ensuite utiliser des [filtres de segmentation](#segmentation-filters) pour segmenter les utilisateurs en fonction de la fréquence et du caractère récent de ces événements personnalisés. Les événements personnalisés sont donc les mieux adaptés au suivi des interactions utilisateur de grande valeur au sein de votre application.

## Cas d'usage {#use-cases}

Parmi les cas d'usage courants d'événements personnalisés figurent les situations suivantes :

{% multi_lang_include data_activation/custom_event_use_cases.md %}

## Gérer les événements personnalisés {#managing-custom-events}

Vous pouvez gérer, créer ou bloquer des événements personnalisés dans le tableau de bord en accédant à **Paramètres des données** > **Événements personnalisés**.

Sélectionnez le menu à côté d'un événement personnalisé pour effectuer les actions suivantes :

### Blocage {#blocklisting}

Vous pouvez bloquer des événements personnalisés individuellement via le menu d'actions, ou sélectionner et bloquer jusqu'à 100 événements en masse.

Lorsque vous bloquez un événement personnalisé :

{% multi_lang_include data_activation/custom_event_block_effects.md %}

De plus, si un événement personnalisé bloqué est actuellement référencé par des filtres ou des déclencheurs dans d'autres zones de Braze, une fenêtre modale d'avertissement apparaîtra pour expliquer que toutes les instances de filtres ou de déclencheurs qui le référencent seront supprimées et archivées.

Pour plus de détails sur le blocage et la suppression de données personnalisées, consultez [Bloquer des données personnalisées]({{site.baseurl}}/user_guide/data/activation/custom_data/blocklist_custom_data).

### Ajouter des descriptions {#adding-descriptions}

Vous pouvez ajouter une description à un événement personnalisé après sa création si vous disposez de l'[autorisation utilisateur]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) `Manage Events, Attributes, Purchases`. Sélectionnez **Modifier la description** pour l'événement personnalisé et saisissez ce que vous souhaitez, comme une note pour votre équipe.

### Ajouter des étiquettes {#adding-tags}

Vous pouvez ajouter des étiquettes à un événement personnalisé après sa création si vous disposez de l'[autorisation utilisateur]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) « Manage Events, Attributes, Purchases ». Les étiquettes peuvent ensuite être utilisées pour filtrer la liste des événements.

### Exporter des données {#exporting-data}

Pour exporter la liste des événements personnalisés sous forme de fichier CSV, sélectionnez **Tout exporter** en haut de la page. Le fichier CSV est généré et un lien de téléchargement vous est envoyé par e-mail.

{% alert note %}
Il n'y a pas de limite fixe dans le tableau de bord quant au nombre d'**événements personnalisés** ou d'**attributs personnalisés** distincts que vous pouvez définir ou stocker sur un profil ; les limites pratiques dépendent de la forme des données, du volume d'ingestion et des performances de l'espace de travail. Si vous prévoyez de suivre un très grand catalogue d'événements ou d'attributs, collaborez avec votre équipe de compte Braze sur la modélisation et l'hygiène des données (par exemple, le [blocage]({{site.baseurl}}/user_guide/data/activation/custom_data/blocklist_custom_data) des données inutilisées).
{% endalert %}

## Consulter les rapports d'utilisation {#viewing-usage-reports}

Le rapport d'utilisation répertorie tous les Canvas, Campaigns et Segments qui utilisent un événement personnalisé spécifique. Cette liste n'inclut pas les utilisations de Liquid.

Vous pouvez consulter jusqu'à 100 rapports d'utilisation à la fois en cochant les cases correspondantes à côté des événements personnalisés, puis en sélectionnant **Afficher le rapport d'utilisation**.

## Enregistrer des événements personnalisés {#logging-custom-events}

Les événements personnalisés nécessitent une configuration supplémentaire. Consultez la documentation de chaque plateforme ci-dessous pour en savoir plus sur les méthodes utilisées pour enregistrer des événements personnalisés et sur la façon d'ajouter des propriétés et des quantités à vos événements personnalisés.

{% details Développer pour la documentation par plateforme %}

- [Android et FireOS]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=android)
- [iOS]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=swift)
- [Web]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=web)
- [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/analytics#logging-custom-events)
- [Unity]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=unity)
- [.NET MAUI (anciennement Xamarin)]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics#tracking-custom-events)
- [Roku]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=roku)

{% enddetails %}

## Stockage des événements personnalisés {#custom-event-storage}

Toutes les données stockées dans le **profil utilisateur**, y compris les métadonnées des événements personnalisés (première ou dernière occurrence, nombre total et X sur Y au cours des 30 derniers jours), sont conservées indéfiniment tant que chaque profil est <a href="/docs/user_archival#active-users">actif</a>.

## Consulter l'historique des événements d'un utilisateur {#view-a-users-event-history}

{% alert important %}
L'historique des événements est actuellement en accès anticipé. Contactez votre gestionnaire de compte Braze si vous souhaitez y participer.
{% endalert %}

Utilisez l'onglet **Historique des événements** sur le profil d'un utilisateur pour consulter ses événements personnalisés et achats récents. Cela vous permet de confirmer que votre intégration enregistre correctement les événements et de résoudre les problèmes au niveau de l'utilisateur directement dans le tableau de bord.

Pour consulter l'historique des événements d'un utilisateur :

1. Accédez à **Audience** > **Rechercher des utilisateurs**, puis sélectionnez un utilisateur pour ouvrir son profil.
2. Sélectionnez l'onglet **Historique des événements**.

L'onglet répertorie les événements personnalisés et les achats de l'utilisateur au cours des 30 derniers jours, jusqu'à ses 100 événements les plus récents, classés du plus récent au plus ancien.

Chaque événement comprend :

- **Type d'événement :** indique s'il s'agit d'un événement personnalisé ou d'un achat.
- **Nom de l'événement :** le nom de l'événement tel qu'il a été enregistré.
- **Heure :** le moment où l'événement s'est produit.
- **Propriétés :** les propriétés complètes de l'événement pour cette occurrence, affichées au format JSON.

Parmi les cas d'usage courants :

- Vérifier que votre intégration SDK ou API envoie les événements comme prévu pendant le développement ou après une mise en production.
- Résoudre un problème lié au fait qu'un utilisateur est entré ou non dans une campagne ou un Canvas déclenché par un événement.
- Investiguer un problème d'assistance pour un utilisateur spécifique sans avoir à configurer une exportation de données.

{% alert note %}
La consultation de l'onglet **Historique des événements** nécessite les autorisations utilisateur **Rechercher des utilisateurs**, **Voir les informations personnelles** et **Voir les propriétés d'événement utilisateur**, car les propriétés d'événement peuvent contenir des données personnelles. Pour en savoir plus, consultez [Autorisations utilisateur de l'entreprise]({{site.baseurl}}/user_guide/administer/global/user_management/permissions).
{% endalert %}

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
| Vérifier si l'événement personnalisé s'est produit **plus de X fois (max = 50)** | **MORE THAN** | au cours des **Y derniers jours (Y = 1, 3, 7, 14, 21, 30)** |
| Vérifier si l'événement personnalisé s'est produit **moins de X fois (max = 50)** | **LESS THAN** | au cours des **Y derniers jours (Y = 1, 3, 7, 14, 21, 30)** |
| Vérifier si l'événement personnalisé s'est produit **exactement X fois (max = 50)** | **EXACTLY** | au cours des **Y derniers jours (Y = 1, 3, 7, 14, 21, 30)** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Filtres de segmentation" }

## Analyses {#analytics}

Braze enregistre le nombre de fois que chaque événement personnalisé s'est produit ainsi que la date de sa dernière occurrence pour chaque utilisateur, à des fins de segmentation. Consultez ces analyses en accédant à **Analytics** > **Rapport d'événements personnalisés**.

Sur la page **Rapport d'événements personnalisés** du tableau de bord, vous pouvez visualiser de manière agrégée la fréquence de chaque événement personnalisé. Les lignes grises superposées sur la série temporelle indiquent la dernière fois qu'une campagne a été envoyée, ce qui est utile pour observer l'impact de vos campagnes sur l'activité des événements personnalisés.

![Graphique du nombre d'événements personnalisés sur la page Événements personnalisés du tableau de bord montrant les tendances d'un événement personnalisé]({% image_buster /assets/img_archive/custom_event_analytics_example.png %} "custom_event_analytics_example.png")

Vous pouvez également utiliser les **filtres** pour ventiler vos événements personnalisés par heure, utilisateurs actifs mensuels (MAU), Segments ou formules de KPI.

![Filtres du graphique d'événements personnalisés]({% image_buster /assets/img/custom_events_report_filters.png %}){: style="max-width:40%;"}

{% alert tip %}
[Incrémentez des attributs personnalisés]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#custom-attribute-data-types) pour maintenir un compteur sur une action utilisateur similaire à un événement personnalisé. Cependant, vous ne pouvez pas visualiser les données d'attributs personnalisés sous forme de série temporelle. Les actions utilisateur qui n'ont pas besoin d'être analysées sous forme de série temporelle doivent être enregistrées avec cette méthode.
{% endalert %}

### Pourquoi les analyses d'événements personnalisés ne s'affichent pas {#why-custom-events-analytics-arent-showing}

Les Segments créés à partir de données d'événements personnalisés ne peuvent pas afficher les données historiques antérieures à leur création.

## Propriétés d'événement personnalisé {#custom-event-properties}

Les propriétés d'événement personnalisé sont des métadonnées ou des attributs d'événement personnalisé qui décrivent une occurrence spécifique d'un événement. Ces propriétés peuvent être utilisées pour affiner les conditions de déclenchement, augmenter la personnalisation des messages, suivre les conversions et générer des analyses plus sophistiquées via l'exportation de données brutes.

Pour en savoir plus, consultez [Propriétés d'événement personnalisé]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties).