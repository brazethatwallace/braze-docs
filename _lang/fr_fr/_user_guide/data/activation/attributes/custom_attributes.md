---
nav_title: Attributs personnalisés
article_title: Attributs personnalisés
page_order: 1
page_type: reference
description: "Cette page décrit les attributs personnalisés et présente les différents types de données d'attributs personnalisés."
search_rank: 1
---

# [![Cours d'apprentissage Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/custom-events-and-attributes){: style="float:right;width:120px;border:0;" class="noimgborder"}Attributs personnalisés

> Cette page traite des attributs personnalisés, qui regroupent les caractéristiques propres à vos utilisateurs. Les attributs personnalisés sont particulièrement adaptés au stockage d'informations sur vos utilisateurs ou de données relatives à des actions à faible valeur au sein de votre application.

Une fois stockés dans Braze, les attributs personnalisés permettent de créer des segments d'audience et de personnaliser les messages à l'aide de Liquid. Gardez à l'esprit que Braze ne conserve pas de données chronologiques pour les attributs personnalisés : vous ne pouvez donc pas générer de graphiques à partir de ceux-ci, contrairement aux Événements personnalisés.

## Cas d'utilisation

Voici quelques cas d'utilisation courants des attributs personnalisés :

- Cibler et exclure des audiences en segmentant les utilisateurs selon des caractéristiques telles que le niveau de fidélité, le statut d'abonnement, la langue préférée ou le type de forfait
- Personnaliser les messages avec [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/) en référençant des attributs comme le prénom de l'utilisateur, ses points de récompense ou sa catégorie préférée
- Suivre les étapes du cycle de vie et les états utilisateur, comme l'étape d'onboarding, le statut du compte ou la date de fin d'essai
- Comptabiliser les actions à faible valeur avec des [attributs numériques]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types/#numbers), par exemple en incrémentant un attribut `feature_views_count` chaque fois qu'un utilisateur consulte une fonctionnalité
- Enregistrer la dernière occurrence d'actions à faible valeur à l'aide d'[attributs temporels]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types/#time), comme `last_support_ticket_at` ou `last_password_reset_at`
- Stocker les centres d'intérêt et l'historique des utilisateurs sous forme de [tableaux]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types/#arrays), tels que les genres préférés ou les contenus récemment consultés, pour un ciblage basé sur les intérêts
- Stocker des données de profil plus riches sous forme d'[objets]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support/) ou de [tableaux d'objets]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects/), comme des préférences structurées ou plusieurs adresses enregistrées
- Déclencher des messages basés sur des actions lorsqu'une valeur d'attribut change à l'aide de [déclencheurs d'attributs]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/attribute_triggers/), par exemple en envoyant une notification de montée en niveau lorsque l'attribut `rewards_tier` d'un utilisateur change

## Gérer les attributs personnalisés {#managing-custom-attributes}

Pour créer et gérer des attributs personnalisés dans le tableau de bord, accédez à **Paramètres des données** > **Attributs personnalisés**.

![Quatre attributs personnalisés de type booléen.]({% image_buster /assets/img/export_custom_attributes.png %})

La colonne **Dernière mise à jour** indique la date de la dernière modification de l'attribut personnalisé, par exemple la dernière fois qu'il a été ajouté à la liste de blocage ou activé.

{% alert important %}
Pour un ciblage correct des messages, assurez-vous que le type de données de votre attribut personnalisé correspond bien à l'attribut personnalisé réel. <br><br>Par exemple, si `newsletter_subscribed` est défini comme une chaîne de caractères, votre syntaxe Liquid devrait ressembler à {% raw %}```{% if {{custom_attribute.${newsletter_subscribed}}} == 'true' %}```{% endraw %}. Si `newsletter_subscribed` est défini comme une valeur booléenne, la syntaxe Liquid ne doit pas contenir de guillemets simples : {% raw %}```{% if {{custom_attribute.${newsletter_subscribed}}} == true %}```{% endraw %}.
{% endalert %}

Depuis cette page, vous pouvez afficher, gérer, créer ou bloquer des attributs personnalisés existants. Sélectionnez le menu à côté d'un attribut personnalisé pour accéder aux actions suivantes :

### Blocage {#blocklisting}

Vous pouvez bloquer des attributs personnalisés individuellement via le menu d'actions, ou sélectionner et bloquer jusqu'à 100 attributs en masse.

Lorsque vous bloquez un attribut personnalisé :

- Les données futures ne seront plus collectées pour cet attribut.
- Les données existantes ne seront pas disponibles tant que l'attribut n'est pas débloqué.
- Cet attribut n'apparaîtra pas dans les filtres ni dans les graphiques.

De plus, si un attribut personnalisé bloqué est actuellement référencé par des filtres ou des déclencheurs dans d'autres zones de Braze, une fenêtre modale d'avertissement apparaîtra pour vous informer que toutes les instances de filtres ou de déclencheurs qui le référencent seront supprimées et archivées.

Pour plus de détails sur le blocage et la suppression de données personnalisées, consultez [Bloquer des données personnalisées]({{site.baseurl}}/user_guide/data/activation/custom_data/blocklist_custom_data/).

### Marquer comme information personnelle identifiable (PII)

Les administrateurs peuvent également créer des attributs personnalisés et les marquer comme PII depuis cette page. Ces attributs ne sont visibles que par les administrateurs et les utilisateurs du tableau de bord disposant de l'autorisation « Afficher les attributs personnalisés marqués comme PII ».

### Ajouter des descriptions

Vous pouvez ajouter une description à un attribut personnalisé après sa création si vous disposez de l'[autorisation utilisateur]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/) `Manage Events, Attributes, Purchases`. Sélectionnez **Modifier la description** pour l'attribut personnalisé et saisissez ce que vous souhaitez, par exemple une note pour votre équipe.

### Ajouter des étiquettes

Vous pouvez ajouter des étiquettes à un attribut personnalisé après sa création si vous disposez de l'[autorisation utilisateur]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/) « Manage Events, Attributes, Purchases ». Les étiquettes peuvent ensuite être utilisées pour filtrer la liste des attributs.

### Supprimer des attributs personnalisés

Il existe deux façons de supprimer des attributs personnalisés des profils utilisateur :

* Sélectionnez le nom de l'attribut personnalisé à supprimer dans une [étape de Mise à jour utilisateur]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update#removing-custom-attributes).
* Définissez la valeur `null` dans votre requête API vers l'[endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track#user-track).

### Exporter les données

Pour exporter la liste des attributs personnalisés sous forme de fichier CSV, sélectionnez **Tout exporter** en haut de la page. Le fichier CSV est généré et un lien de téléchargement vous est envoyé par e-mail.

## Modifier le type d'un attribut personnalisé

### Conditions préalables

L'attribut personnalisé ne doit pas être actuellement utilisé dans des campagnes, Canvas ou segments actifs. Si vous tentez de modifier le type de données alors que l'attribut est encore référencé, le tableau de bord affiche une erreur et bloque la modification.

### Modifier le type de données

1. Arrêtez toutes les campagnes ou Canvas actifs qui utilisent l'attribut dans des segments ou des filtres.
2. Supprimez l'attribut de tous les filtres de segments, campagnes et Canvas.
3. Accédez à **Paramètres des données** > **Attributs personnalisés** (ou **Événements personnalisés**), trouvez l'attribut et mettez-le à jour avec le type de données souhaité.
4. Mettez à jour les valeurs de l'attribut sur les profils utilisateur existants pour qu'elles correspondent au nouveau type de données (par exemple, en utilisant l'[endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)).
5. Réappliquez l'attribut aux segments, campagnes et Canvas concernés, puis réactivez les campagnes ou Canvas arrêtés.

### Points importants

- **Les données utilisateur ne sont pas mises à jour rétroactivement.** Si un profil utilisateur contenait l'attribut avec l'ancien type de données, cette valeur reste inchangée. Le filtre de segmentation recherche le nouveau type de données, de sorte que les utilisateurs ayant l'ancienne valeur sont exclus des segments correspondants tant que leur profil n'est pas mis à jour.
- **Les nouvelles données doivent correspondre au nouveau type de données.** Après la modification, les appels API ou événements SDK qui envoient l'ancien type de données pour cet attribut ne seront pas acceptés. Seules les valeurs correspondant au nouveau type de données sont ingérées.
- **Les filtres ne sont pas mis à jour automatiquement.** Les segments et filtres de campagne référençant l'attribut modifié ne sont pas mis à jour rétroactivement. Vous devez les supprimer et les recréer après la modification.

## Consulter les rapports d'utilisation

Le rapport d'utilisation répertorie tous les Canvas, campagnes et segments qui utilisent un attribut personnalisé spécifique. Cette liste n'inclut pas les utilisations de Liquid.

Vous pouvez consulter jusqu'à 100 rapports d'utilisation à la fois en cochant les cases correspondantes à côté des attributs personnalisés, puis en sélectionnant **Afficher le rapport d'utilisation**.

### Onglet valeurs

Lors de la consultation d'un rapport d'utilisation, sélectionnez l'onglet **Valeurs** pour afficher les principales valeurs des attributs personnalisés sélectionnés, basées sur un échantillon d'environ 250 000 utilisateurs. Notez que les résultats étant issus d'un sous-ensemble d'utilisateurs, l'échantillon ne comprend pas toutes les valeurs existantes. L'onglet **Valeurs** ne doit donc pas être utilisé pour la résolution des problèmes ni pour des cas d'utilisation nécessitant l'intégration des données de tous les utilisateurs.

![Rapport d'utilisation pour les attributs personnalisés sélectionnés avec un onglet « Valeurs » ouvert montrant un graphique circulaire des valeurs de l'attribut pays, telles que « US » et « PR ».]({% image_buster /assets/img/usage_report_values.png %}){: style="max-width:80%;"}

## Définir des attributs personnalisés

Voici les méthodes utilisées sur les différentes plateformes pour définir des attributs personnalisés.

{% details Développer pour la documentation par plateforme %}

- [Android et FireOS]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=android)
- [iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=swift)
- [Web]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=web)
- [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/analytics/#logging-custom-attributes)
- [Unity]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=unity)
- [.NET MAUI (anciennement Xamarin)]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics/#setting-custom-attributes)
- [Roku]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/)

{% enddetails %}

## Stockage des attributs personnalisés

Toutes les données stockées dans le **profil utilisateur**, y compris les données d'attributs personnalisés, sont conservées indéfiniment tant que chaque profil est [actif]({{site.baseurl}}/user_archival#active-users).

Pour une référence complète de tous les types de données pouvant être stockés en tant qu'attributs personnalisés — y compris les valeurs booléennes, les nombres, les chaînes de caractères, les tableaux, les dates, les objets et les tableaux d'objets — consultez [Types de données des attributs personnalisés]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types/).