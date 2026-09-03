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

Voici quelques cas d'usage courants des événements personnalisés :

{% multi_lang_include data_activation/custom_event_use_cases.md %}

## Gestion des événements personnalisés {#managing-custom-events}

Vous pouvez gérer, créer ou bloquer des événements personnalisés dans le tableau de bord en accédant à **Data Settings** > **Custom Events**.

### Résolution des problèmes liés aux attributs ou événements personnalisés en double {#troubleshooting-duplicate-custom-attributes-or-events}

{% multi_lang_include data_activation/troubleshooting_duplicate_custom_data_entries.md %}

Sélectionnez le menu à côté d'un événement personnalisé pour accéder aux actions suivantes :

### Blocage {#blocklisting}

Vous pouvez bloquer des événements personnalisés individuels via le menu d'actions, ou sélectionner et bloquer jusqu'à 100 événements en masse.

Lorsque vous bloquez un événement personnalisé :

{% multi_lang_include data_activation/custom_event_block_effects.md %}

De plus, si un événement personnalisé bloqué est actuellement référencé par des filtres ou des déclencheurs dans d'autres zones de Braze, une fenêtre modale d'avertissement apparaîtra pour expliquer que toutes les instances des filtres ou déclencheurs qui le référencent seront supprimées et archivées.

Pour plus de détails sur le blocage et la suppression de données personnalisées, consultez [Bloquer les données personnalisées]({{site.baseurl}}/user_guide/data/activation/custom_data/blocklist_custom_data).

### Ajout de descriptions {#adding-descriptions}

Vous pouvez ajouter une description à un événement personnalisé après sa création si vous disposez de l'[autorisation utilisateur]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) `Manage Events, Attributes, Purchases`. Sélectionnez **Edit description** pour l'événement personnalisé et saisissez ce que vous souhaitez, comme une note pour votre équipe.

### Ajout de tags {#adding-tags}

Vous pouvez ajouter des tags à un événement personnalisé après sa création si vous disposez de l'[autorisation utilisateur]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) « Manage Events, Attributes, Purchases ». Les tags peuvent ensuite être utilisés pour filtrer la liste des événements.

### Exportation des données {#exporting-data}

Pour exporter la liste des événements personnalisés sous forme de fichier CSV, sélectionnez **Export all** en haut de la page. Le fichier CSV est généré et un lien de téléchargement vous est envoyé par e-mail.

{% alert note %}
Il n'y a pas de limite fixe dans le tableau de bord concernant le nombre d'**événements personnalisés** ou d'**attributs personnalisés** distincts que vous pouvez définir ou stocker sur un profil ; les limites pratiques dépendent de la forme des données, du volume d'ingestion et des performances de l'espace de travail. Si vous prévoyez de suivre un très grand catalogue d'événements ou d'attributs, travaillez avec votre équipe de compte Braze sur la modélisation et l'hygiène des données (par exemple, le [blocage]({{site.baseurl}}/user_guide/data/activation/custom_data/blocklist_custom_data) des données inutilisées).
{% endalert %}

## Consulter les rapports d'utilisation {#viewing-usage-reports}

Le rapport d'utilisation répertorie tous les Canvas, Campaigns et Segments qui utilisent un événement personnalisé spécifique. Cette liste n'inclut pas les utilisations de Liquid.

Vous pouvez consulter jusqu'à 100 rapports d'utilisation à la fois en cochant les cases correspondant aux événements personnalisés concernés, puis en sélectionnant **View usage report**.

## Enregistrement des événements personnalisés {#logging-custom-events}

Les événements personnalisés nécessitent une configuration supplémentaire. Consultez la documentation de plateforme suivante pour connaître les méthodes utilisées pour enregistrer les événements personnalisés et comment ajouter des propriétés et des quantités à vos événements personnalisés.

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

Toutes les données stockées sur le **profil utilisateur**, y compris les métadonnées d'événement personnalisé (première ou dernière occurrence, nombre total et X sur Y au cours des 30 derniers jours), sont conservées indéfiniment tant que chaque profil est <a href="/docs/user_archival#active-users">actif</a>.

## Consulter l'historique des événements d'un utilisateur {#view-a-users-event-history}

Utilisez l'onglet **Event History** sur le profil d'un utilisateur pour consulter ses événements personnalisés et achats récents. Cela vous permet de confirmer que votre intégration enregistre correctement les événements et de résoudre les problèmes au niveau de l'utilisateur directement dans le tableau de bord.

Pour consulter l'historique des événements d'un utilisateur :

1. Allez dans **Audience** > **Search Users**, puis sélectionnez un utilisateur pour ouvrir son profil.
2. Sélectionnez l'onglet **Event History**.

L'onglet répertorie les événements personnalisés et les achats de l'utilisateur au cours des 30 derniers jours, jusqu'à ses 100 événements les plus récents, classés du plus récent au plus ancien.

Chaque événement comprend :

- **Type d'événement :** indique si l'événement est un événement personnalisé ou un achat.
- **Nom de l'événement :** le nom de l'événement tel qu'il a été enregistré.
- **Heure :** le moment où l'événement s'est produit.
- **Propriétés :** les propriétés d'événement complètes pour cette occurrence, affichées au format JSON.

Les cas d'usage courants incluent :

- Vérifier que votre intégration SDK ou API envoie les événements comme prévu pendant le développement ou après une mise en production.
- Résoudre les problèmes liés au fait qu'un utilisateur est entré ou non dans une Campaign ou un Canvas déclenché par un événement.
- Investiguer un problème de support pour un utilisateur spécifique sans avoir à configurer une exportation de données.

{% alert note %}
La consultation de l'onglet **Event History** nécessite les autorisations utilisateur **Search Users**, **View PII** et **View User Event Properties**, car les propriétés d'événement peuvent contenir des données personnelles. Pour plus d'informations, consultez [Autorisations utilisateur de l'entreprise]({{site.baseurl}}/user_guide/administer/global/user_management/permissions).
{% endalert %}

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
| Vérifier si l'événement personnalisé s'est produit **plus de X fois (max = 50)** | **PLUS DE** | au cours des **Y derniers jours (Y = 1,3,7,14,21,30)** |
| Vérifier si l'événement personnalisé s'est produit **moins de X fois (max = 50)** | **MOINS DE** | au cours des **Y derniers jours (Y = 1,3,7,14,21,30)** |
| Vérifier si l'événement personnalisé s'est produit **exactement X fois (max = 50)** | **EXACTEMENT** | au cours des **Y derniers jours (Y = 1,3,7,14,21,30)** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Filtres de segmentation" }

## Analyse {#analytics}

Braze enregistre le nombre de fois où des événements personnalisés se sont produits et la dernière fois qu'ils ont été effectués par chaque utilisateur à des fins de segmentation. Pour la configuration des rapports, les filtres et les options d'exportation, consultez [Rapport d'événements personnalisés]({{site.baseurl}}/user_guide/analytics/reports/custom_events_report).

Sur la page **Custom Events Report**, vous pouvez visualiser de manière agrégée la fréquence de chaque événement personnalisé. Les lignes grises superposées sur la série temporelle indiquent la dernière fois qu'une Campaign a été envoyée, ce qui est utile pour observer l'impact de vos Campaigns sur l'activité des événements personnalisés.

![Graphique du nombre d'événements personnalisés sur la page Custom Events du tableau de bord montrant les tendances d'un événement personnalisé]({% image_buster /assets/img_archive/custom_event_analytics_example.png %} "custom_event_analytics_example.png")

Vous pouvez également utiliser les **filtres** pour ventiler vos événements personnalisés par heure, utilisateurs actifs mensuels (MAU), Segments ou formules de KPI.

![Filtres du graphique d'événements personnalisés]({% image_buster /assets/img/custom_events_report_filters.png %}){: style="max-width:40%;"}

{% alert tip %}
[Incrémentez les attributs personnalisés]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#custom-attribute-data-types) pour maintenir un compteur sur une action utilisateur similaire à un événement personnalisé. Cependant, vous ne pouvez pas visualiser les données d'attributs personnalisés sous forme de série temporelle. Les actions utilisateur qui n'ont pas besoin d'être analysées sous forme de série temporelle doivent être enregistrées à l'aide de cette méthode.
{% endalert %}

### Pourquoi l'analyse des événements personnalisés ne s'affiche pas {#why-custom-events-analytics-arent-showing}

Les Segments créés avec des données d'événements personnalisés ne peuvent pas afficher les données historiques antérieures à leur création.

## Propriétés d'événement personnalisé {#custom-event-properties}

Les propriétés d'événement personnalisé sont des métadonnées ou des attributs d'événement personnalisé qui décrivent une occurrence spécifique d'un événement. Ces propriétés peuvent être utilisées pour affiner les conditions de déclenchement, augmenter la personnalisation des messages, suivre les conversions et générer des analyses plus sophistiquées via l'exportation de données brutes.

Pour en savoir plus, consultez [Propriétés d'événement personnalisé]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties).