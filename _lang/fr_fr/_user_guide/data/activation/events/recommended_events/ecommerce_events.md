---
nav_title: Utiliser les événements recommandés pour le commerce électronique
article_title: Comment utiliser les événements recommandés pour le commerce électronique
page_type: reference
alias: /ecommerce_events/
description: "Découvrez comment utiliser les événements recommandés pour le commerce électronique dans Braze, y compris les fonctionnalités prises en charge, les indicateurs clés et les bonnes pratiques pour la segmentation et l'envoi de messages."
---

# Comment utiliser les événements eCommerce {#how-to-use-ecommerce-events}

> Les [événements recommandés]({{site.baseurl}}/recommended_events) pour le commerce électronique utilisent un schéma partagé au niveau de la commande, ce qui permet à Braze de construire des fonctionnalités fiables à partir de vos données eCommerce, notamment les profils utilisateur, la segmentation, l'envoi de messages, le reporting et les recommandations basées sur l'IA. Les sections de cet article expliquent comment utiliser chaque fonctionnalité dans Braze.<br><br> Consultez les [schémas d'événements]({{site.baseurl}}/user_guide/data/activation/events/recommended_events#event-schemas) pour les exigences de propriétés et les types de données, et [Validation et résolution des problèmes des événements]({{site.baseurl}}/user_guide/data/activation/events/recommended_events#event-validation-and-troubleshooting) pour savoir ce qui se passe lorsqu'un événement échoue à la validation.

Comme les événements eCommerce suivent un schéma prévisible, Braze peut construire des fonctionnalités fiables par-dessus, du suivi du chiffre d'affaires et des modèles de Canvas prêts à l'emploi aux recommandations basées sur l'IA. Les sections suivantes vous offrent un aperçu rapide de chaque fonctionnalité avec des liens vers la documentation complète.

{% alert note %}
Les événements eCommerce de Braze et leurs propriétés d'événement segmentables ne sont pas comptabilisés dans les [points de donnée]({{site.baseurl}}/user_guide/data/infrastructure/data_points).
{% endalert %}

<a id="transactions-tab" aria-hidden="true"></a>

## Onglet Commerce {#commerce-tab}

L'onglet **Commerce** de chaque profil utilisateur combine deux modules : **Activité des commandes** (indicateurs calculés de chiffre d'affaires et de commandes) et **Panier actif** (le dernier panier issu des événements `ecommerce.cart_updated`).

### Activité des commandes {#order-activity}

Le module **Activité des commandes** affiche trois indicateurs calculés qui se mettent à jour en temps réel au fur et à mesure du traitement des événements. Le modèle au niveau de la commande de ces calculs sépare clairement les prix des produits de la valeur totale de la commande.

{% alert note %}
Les événements recommandés pour le commerce électronique ne remplissent pas la section **Historique des achats** de l'onglet **Commerce**. L'historique des achats est alimenté par les événements d'achat hérités. Utilisez les indicateurs du tableau suivant pour le chiffre d'affaires et l'activité de commande provenant des événements recommandés.
{% endalert %}

| Indicateur | Formule |
| ----- | ----- |
| Chiffre d'affaires total | somme (`order_placed.total_value`) − somme (`order_refunded.total_value`) |
| Nombre total de commandes | nombre (distinct `order_placed`) − nombre (distinct `order_cancelled`) |
| Valeur totale des remboursements | somme (`order_refunded.total_value`) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Indicateurs d'activité des commandes" }

### Panier actif {#active-cart}

Le module **Panier actif** affiche le dernier panier sur le profil utilisateur. Cette vue est particulièrement utile pendant vos tests. Vous pouvez l'utiliser pour confirmer le contenu du panier, valider les parcours basés sur le panier ou vérifier que les événements `ecommerce.cart_updated` mettent bien à jour le profil comme prévu.

Le **Panier actif** inclut les éléments suivants :

- **ID du panier** — Identifiant du panier ayant reçu en dernier un événement `ecommerce.cart_updated`.
- **Dernière mise à jour** — Horodatage de la mise à jour la plus récente du panier.
- **Valeur totale du panier** — Valeur totale des articles dans le panier actuel.
- **Voir les produits** — Un lien pour ouvrir la liste des produits dans le panier (jusqu'à 50 produits).

## Orchestration eCommerce {#ecommerce-orchestration}

### Segmentation {#segmentation}

Braze propose trois moyens de segmenter les utilisateurs à partir des données eCommerce :

- **Filtres eCommerce :** Utilisez la catégorie **eCommerce** dans le segmenteur, qui contient des filtres alimentés par les événements eCommerce recommandés (tels que **Last Order Placed**, **Total Revenue** et **Average Order Value**). Pour une liste complète des filtres disponibles, consultez [Filtres de Segment]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters).
- **Filtres d'événements personnalisés :** Les événements eCommerce se comportant comme des événements personnalisés, tous les filtres d'événements personnalisés existants fonctionnent immédiatement. Par exemple, vous pouvez filtrer par « A effectué l'événement personnalisé `ecommerce.order_placed` plus de X fois » ou « A effectué pour la première fois l'événement personnalisé `ecommerce.order_placed` ».
- **Extensions de segments :** Pour segmenter à partir de propriétés d'événements imbriquées, y compris le tableau de produits imbriqué ou les propriétés des objets de métadonnées, utilisez les [extensions de segments]({{site.baseurl}}/user_guide/audience/segments/segment_extension) avec le filtrage des propriétés d'événements imbriquées. Cela vous permet de créer des audiences comme « les utilisateurs qui ont acheté le produit SKU-123 au cours des 90 derniers jours » ou de combiner des critères portant sur différentes propriétés de la même commande.

{% alert important %}
Les extensions de segments pour les événements eCommerce recommandés sont une fonctionnalité payante en accès anticipé. Si vous souhaitez participer à l'accès anticipé, contactez votre gestionnaire de la satisfaction client. Vérifiez que votre plan inclut l'accès avant de recommander la segmentation par propriétés imbriquées à votre équipe.
{% endalert %}

### Déclenchement {#triggering}

Vous pouvez utiliser des déclencheurs d'événements personnalisés effectués avec les événements eCommerce dans l'ensemble de Braze, comme avec n'importe quel autre événement personnalisé. Pour les flux de panier abandonné, utilisez le déclencheur **Perform Cart Updated Event** pour capturer correctement les mises à jour du panier.

De plus, Braze propose un déclencheur dédié **Places Order**, qui vous permet de démarrer des parcours ou d'effectuer des actions en fonction de toute commande passée, ou de commandes incluant un produit spécifique. Vous pouvez filtrer ce déclencheur par nom de produit, `product_id` ou `variant_id` pour cibler des scénarios d'achat spécifiques. Pour en savoir plus, consultez [Livraison par événement]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery).

![Déclencheur Places Order avec une option sélectionnée pour passer n'importe quelle commande.]({% image_buster /assets/img/recommended_events/places_order_trigger.png %})

### Personnalisation Liquid {#liquid-personalization}

Les événements eCommerce prennent en charge la [personnalisation Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid) de la même manière que les événements personnalisés ; vous pouvez référencer les propriétés d'événement directement dans vos messages. Pour intégrer des images de produits, des tarifs ou d'autres données de catalogue dans vos messages, associez votre catalogue à l'événement en utilisant `product_id` ou `variant_id` comme identifiant de liaison. L'étiquette Liquid {% raw %}`{% shopping_cart %}`{% endraw %} vous permet de parcourir le contenu actuel du panier d'un utilisateur pour les rappels de panier abandonné, les incitations au passage en caisse ou les confirmations de commande. Pour des exemples de code prêts à l'emploi, consultez [Cas d'usage eCommerce]({{site.baseurl}}/ecommerce_use_cases).

Pour une alternative sans code, les [blocs de produits en glisser-déposer]({{site.baseurl}}/user_guide/messaging/design_and_edit/product_blocks) sont disponibles dans le programme d'accès anticipé.

### Modèles Canvas eCommerce {#ecommerce-canvas-templates}

Braze fournit des modèles Canvas prêts à l'emploi, préconfigurés avec les événements eCommerce recommandés comme critères d'entrée, de sortie et de conversion, afin que vous puissiez lancer des flux de cycle de vie sans configuration personnalisée. Chaque modèle est livré avec des designs d'e-mail en glisser-déposer et prend en charge les blocs de produits en glisser-déposer (actuellement en accès anticipé). Pour des cas d'usage détaillés et des exemples Liquid, consultez [Cas d'usage eCommerce]({{site.baseurl}}/ecommerce_use_cases).

Ces modèles couvrent les flux de cycle de vie eCommerce les plus courants. Utilisez-les comme point de départ, puis personnalisez le calendrier, les canaux et les créations pour votre audience.

{% tabs %}
{% tab Navigation abandonnée %}

Relance les utilisateurs qui ont consulté un produit mais ne l'ont pas ajouté à leur panier.

Utilisez ce modèle lorsque vous souhaitez ramener les visiteurs vers des produits qu'ils ont récemment consultés sans passer à l'action.

| Paramètre | Valeur |
| --- | --- |
| Événement d'entrée | `ecommerce.product_viewed` |
| Événements de sortie | `ecommerce.product_viewed`, `ecommerce.cart_updated`, `ecommerce.checkout_started`, Placed Order |
| Événement de conversion | Placed Order |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Modèles Canvas eCommerce" }

{% endtab %}
{% tab Panier abandonné %}

Récupère les utilisateurs qui ont ajouté des articles à leur panier mais n'ont pas commencé le passage en caisse.

Utilisez ce modèle lorsque vous souhaitez rappeler aux utilisateurs les articles dans leur panier et les inciter à finaliser leur achat.

| Paramètre | Valeur |
| --- | --- |
| Événement d'entrée | `ecommerce.cart_updated` |
| Événements de sortie | `ecommerce.cart_updated`, `ecommerce.checkout_started`, Placed Order |
| Événement de conversion | Placed Order |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Modèles Canvas eCommerce" }

{% alert tip %}
L'événement `ecommerce.cart_updated` prend en charge le remplacement complet du panier (chaque événement peut décrire l'intégralité du panier) ou les mises à jour incrémentielles en utilisant les valeurs `add` et `remove` pour la propriété facultative `action`. Choisissez une approche par panier et évitez de mélanger remplacement et mises à jour incrémentielles du panier pour le même `cart_id`. Le panier enregistré conserve la devise (`currency`) du dernier événement de panier ; une mise à jour du panier dans une devise différente remplace le panier enregistré au lieu de mélanger les valeurs de deux devises. Utilisez l'étiquette Liquid {% raw %}`{% shopping_cart %}`{% endraw %} dans votre message pour afficher dynamiquement le contenu actuel du panier au moment de l'envoi.
{% endalert %}

{% endtab %}
{% tab Passage en caisse abandonné %}

Récupère les utilisateurs qui ont commencé le passage en caisse mais n'ont pas finalisé l'achat.

Utilisez ce modèle lorsque vous souhaitez récupérer des achats au stade le plus avancé de l'entonnoir.

| Paramètre | Valeur |
| --- | --- |
| Événement d'entrée | `ecommerce.checkout_started` |
| Événement de sortie | Placed Order |
| Événement de conversion | Placed Order |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Modèles Canvas eCommerce" }

{% endtab %}
{% tab Confirmation de commande et enquête %}

Confirme un achat réussi et envoie ensuite une enquête de satisfaction pour collecter des avis et favoriser l'engagement post-achat.

Utilisez ce modèle lorsque vous souhaitez rationaliser la communication post-achat et recueillir les retours clients dans un seul flux de travail.

| Paramètre | Valeur |
| --- | --- |
| Événement d'entrée | `ecommerce.order_placed` |
| Événement de conversion | Start Session ou `ecommerce.product_viewed` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Modèles Canvas eCommerce" }

{% endtab %}
{% endtabs %}

#### Personnaliser les modèles {#customize-templates}

Ces modèles sont conçus comme point de départ. Les personnalisations courantes comprennent :
  - **Personnaliser l'e-mail :** Chaque modèle inclut un e-mail préconfiguré créé avec l'éditeur en glisser-déposer, entièrement modifiable pour correspondre à votre marque et à votre contenu.
  - **Ajouter des canaux :** Combinez l'e-mail avec des notifications push, des SMS ou des In-App Messages pour un renforcement cross-canal.
  - **Ajouter des délais et des arbres décisionnels :** Segmentez les utilisateurs par comportement (par exemple, panier à haute valeur par rapport à un panier à faible valeur) ou définissez des périodes d'attente entre les messages.
  - **Changer le créatif :** Remplacez le modèle d'e-mail inclus par le style visuel de votre marque.
  - **Utiliser les blocs de produits :** Utilisez les blocs de produits en glisser-déposer (dans le programme d'accès anticipé) pour afficher dynamiquement le contenu du panier abandonné ou les produits consultés sans écrire de code Liquid personnalisé.

Pour des stratégies de cycle de vie plus avancées, y compris des exemples de personnalisation Liquid, consultez [Cas d'usage eCommerce]({{site.baseurl}}/ecommerce_use_cases).

## Rapports eCommerce {#ecommerce-reporting}

Les événements eCommerce recommandés alimentent les mêmes surfaces de chiffre d'affaires que les clients utilisent déjà aujourd'hui. Lorsque votre intégration envoie des événements eCommerce, les rapports suivants incluent automatiquement le chiffre d'affaires eCommerce :

| Rapport                                      | Ce qu'il affiche                             |
|---------------------------------------------|-------------------------------------------|
| Rapport de revenus                              | Chiffre d'affaires total, chiffre d'affaires quotidien moyen, achats quotidiens et chiffre d'affaires par utilisateur au fil du temps, toutes sources confondues, pour la plage de dates et les applications sélectionnées.                                                                                     |
| Tableau de bord de chiffre d'affaires en attribution au dernier contact     | Chiffre d'affaires attribué à la dernière Campaign ou au dernier Canvas avec lequel un utilisateur a interagi avant de passer une commande. Les événements de contact incluent les clics sur les e-mails, les ouvertures de notifications push, les clics sur les Content Cards, les clics sur les In-App Messages et les clics sur les liens courts SMS ou WhatsApp. |
| Analyse des Campaigns et Canvas                | Chiffre d'affaires total attribué à une Campaign ou un Canvas spécifique dans la fenêtre de conversion principale.                                                                                   |
| Rapport de conversions                          | Chiffre d'affaires lié aux événements de conversion sur les Campaigns et Canvas.<br> **Remarque :** pour comptabiliser le chiffre d'affaires `ecommerce.order_placed`, la Campaign ou le Canvas doit utiliser le type d'événement de conversion « Place Order » comme événement de conversion.                                                                                    |
| Segment Insights                            | Comparaisons de chiffre d'affaires entre Segments dans le tableau de bord des statistiques des segments.                                                               |
| Générateur de rapports                              | Indicateurs de chiffre d'affaires dans les rapports personnalisés créés dans le générateur de rapports.                                                                                  |
| Générateur de tableaux de bord                           | Indicateurs de chiffre d'affaires dans les tableaux de bord personnalisés créés dans le générateur de tableaux de bord.                                                                                  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Rapports eCommerce" }

Pour les champs calculés non liés à l'utilisateur (par exemple, le chiffre d'affaires d'une Campaign ou d'un Canvas), le chiffre d'affaires est calculé de la même manière dans tous les rapports : `price` multiplié par `quantity` par produit dans la commande, le tout additionné pour l'ensemble des produits de chaque événement `order_placed`.

{% alert note %}
Les calculs de chiffre d'affaires plafonnent les quantités individuelles de produits à 1 000 unités par commande. Si le champ de quantité est manquant pour un produit, la valeur par défaut est d'une unité. L'événement `ecommerce.order_placed` d'origine conserve la quantité complète que vous avez envoyée — seul le calcul du chiffre d'affaires applique le plafond.<br><br>
Si vous migrez depuis les événements d'achat hérités vers `ecommerce.order_placed`, coordonnez-vous avec votre équipe de compte Braze avant d'effectuer toute modification d'intégration. Pendant la période de transition, envoyez à la fois les événements d'achat hérités et les événements `ecommerce.order_placed` pour confirmer qu'ils se déclenchent correctement et pour préparer la migration de vos Campaigns, Canvas et Segments actifs vers le nouvel événement. Votre équipe de compte peut ensuite vous aider à planifier la bascule pour passer le reporting de chiffre d'affaires des événements d'achat hérités à `ecommerce.order_placed`.
{% endalert %}

### BrazeAI<sup>TM</sup>

Les [événements prédictifs]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events), la [prédiction du taux d'attrition]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn) et les [recommandations d'articles]({{site.baseurl}}/user_guide/brazeai/item_recommendations) prennent en charge les événements eCommerce en tant qu'événements cibles et signaux, et disposent d'une option dédiée « Order Placed ». Le schéma standardisé rend ces modèles plus fiables, car les données sont cohérentes au sein de votre base d'utilisateurs.

### Exporter les données {#export-data}

Braze propose plusieurs moyens d'exporter les données d'événements eCommerce pour les utiliser dans votre entrepôt de données, vos outils de BI ou vos systèmes en aval. Les événements eCommerce recommandés sont exportés via les mêmes canaux que vos autres données d'événements.

| Chemin d'exportation                         | Ce qui est inclus                                                                                                                                                                                 |
|------------------------------------- |------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents)                            | Les événements eCommerce sont diffusés en tant qu'événements personnalisés ; recherchez l'espace de noms `ecommerce.*` pour les trouver. Les produits de chaque commande sont disponibles en tant qu'achats.                                                |
| [Partage de données Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/data_sharing)               | Les événements eCommerce sont partagés en tant qu'événements personnalisés ; recherchez l'espace de noms `ecommerce.*` pour les trouver. Les produits de chaque commande sont disponibles dans la table des achats.                                   |
| [Exporter les données de Segment au format CSV]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/segment_data_to_csv)           | Export CSV des membres d'un Segment. Pour inclure les événements eCommerce, sélectionnez-les par nom dans le menu déroulant des événements personnalisés.                                                                                |
| [Exporter le profil utilisateur par Segment (API)]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment#prerequisites) | Données de profil utilisateur pour les membres d'un Segment, renvoyées via l'API. Les événements eCommerce sont inclus en tant qu'événements personnalisés.                                                                                        |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Exporter les données" }

### Comment segmenter les utilisateurs par produit spécifique ? {#how-do-i-segment-users-by-a-specific-product}

Le segmenteur vous permet de filtrer par le nombre de fois qu'un utilisateur a effectué un événement eCommerce. Pour filtrer par propriétés de produit spécifiques (telles que `product_id` ou `product_name`), utilisez les [extensions de segments]({{site.baseurl}}/user_guide/audience/segments/segment_extension), qui prennent en charge le filtrage par propriétés d'événement imbriquées. Par exemple, vous pouvez trouver tous les utilisateurs ayant acheté le produit « SKU-123 » au cours des 90 derniers jours.