---
nav_title: Utiliser les événements recommandés pour le commerce électronique
article_title: Comment utiliser les événements recommandés pour le commerce électronique
page_type: reference
alias: /ecommerce_events/
description: "Découvrez comment utiliser les événements recommandés pour le commerce électronique dans Braze, y compris les fonctionnalités prises en charge, les indicateurs clés et les bonnes pratiques pour la segmentation, l'envoi de messages et le reporting."
---

# Comment utiliser les événements eCommerce {#how-to-use-ecommerce-events}

> Les [événements recommandés]({{site.baseurl}}/recommended_events/) pour le commerce électronique utilisent un schéma partagé au niveau de la commande, ce qui permet à Braze de construire des fonctionnalités fiables à partir de vos données eCommerce, notamment les profils utilisateur, la segmentation, l'envoi de messages, le reporting et les recommandations basées sur l'intelligence artificielle. Les sections de cet article expliquent comment utiliser chaque fonctionnalité dans Braze.<br><br> Consultez les [schémas d'événements]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/#event-schemas) pour les exigences de propriétés et les types de données, et [Validation et résolution des problèmes des événements]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/#event-validation-and-troubleshooting) pour savoir ce qui se passe lorsqu'un événement échoue à la validation.

Comme les événements eCommerce suivent un schéma prévisible, Braze peut construire des fonctionnalités fiables par-dessus, du suivi du chiffre d'affaires et des modèles de Canvas prêts à l'emploi aux recommandations basées sur l'intelligence artificielle. Les sections suivantes vous offrent un aperçu rapide de chaque fonctionnalité avec des liens vers la documentation complète.

{% alert note %}
Les événements eCommerce de Braze et leurs propriétés d'événement segmentables ne sont pas comptabilisés dans les [points de donnée]({{site.baseurl}}/user_guide/data/infrastructure/data_points/).
{% endalert %}

## Onglet Transactions {#transactions-tab}

L'onglet **Transactions** de chaque profil utilisateur offre une vue en temps réel de l'activité commerciale d'un utilisateur en affichant trois indicateurs calculés qui se mettent à jour au fur et à mesure du traitement des événements. Le modèle au niveau de la commande de ces calculs sépare clairement les prix des produits de la valeur totale de la commande.

{% alert note %}
Les événements recommandés pour le commerce électronique ne remplissent pas la section **Historique des achats** de l'onglet **Transactions**. L'historique des achats est alimenté par les événements d'achat hérités. Utilisez les indicateurs du tableau suivant pour le chiffre d'affaires et l'activité de commande provenant des événements recommandés.
{% endalert %}

| Indicateur | Formule |
| ----- | ----- |
| Chiffre d'affaires total | somme (`order_placed.total_value`) − somme (`order_refunded.total_value`) |
| Nombre total de commandes | nombre (distinct `order_placed`) − nombre (distinct `order_cancelled`) |
| Valeur totale des remboursements | somme (`order_refunded.total_value`) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Transactions tab" }

![Section Activité des commandes avec le chiffre d'affaires total, le nombre total de commandes et la valeur totale des remboursements.]({% image_buster /assets/img/recommended_events/order_activity.png %}){: style="max-width:60%"}

## Orchestration eCommerce {#ecommerce-orchestration}

### Segmentation {#segmentation}

Les événements eCommerce se comportent comme des événements personnalisés, ce qui signifie que tous les filtres d'événements personnalisés existants fonctionnent immédiatement. Par exemple, vous pourriez filtrer par « A effectué l'événement personnalisé `ecommerce.order_placed` plus de X fois ».

Pour le ciblage basé sur des données produit imbriquées (comme des ID de produit spécifiques, des noms de variantes ou des seuils de prix), utilisez les [Extensions de segments]({{site.baseurl}}/user_guide/audience/segments/segment_extension/) avec le filtrage par propriétés d'événement imbriquées. Cela vous permet de créer des audiences comme « les utilisateurs ayant acheté le produit SKU-123 au cours des 90 derniers jours » ou de combiner des critères sur différentes propriétés de la même commande.

{% alert important %}
Les Extensions de segments sont une fonctionnalité payante. Vérifiez que votre forfait inclut l'accès avant de recommander la segmentation par propriétés imbriquées à votre équipe.
{% endalert %}

### Déclenchement {#triggering}

Vous pouvez utiliser les déclencheurs d'événements personnalisés effectués avec les événements eCommerce dans tout Braze, comme avec les autres événements personnalisés. Pour les flux de panier abandonné, utilisez le déclencheur **Perform Cart Updated Event** pour capturer correctement les mises à jour du panier.

De plus, Braze propose un déclencheur dédié **Places Order**, qui vous permet de démarrer des parcours ou d'effectuer des actions en fonction de toute commande passée, ou de commandes incluant un produit spécifique. Vous pouvez filtrer ce déclencheur par nom de produit, `product_id` ou `variant_id` pour cibler des scénarios d'achat spécifiques. Pour plus d'informations, consultez [Livraison par événement]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/).

![Déclencheur Places Order avec une option sélectionnée pour passer n'importe quelle commande.]({% image_buster /assets/img/recommended_events/places_order_trigger.png %})

### Personnalisation Liquid {#liquid-personalization}

Les événements eCommerce prennent en charge la [personnalisation Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid/) de la même manière que les événements personnalisés ; vous pouvez référencer les propriétés d'événement directement dans vos messages. Pour intégrer des images de produits, des prix ou d'autres données de catalogue dans vos messages, associez votre catalogue à l'événement en utilisant `product_id` ou `variant_id` comme identifiant de liaison. L'étiquette Liquid {% raw %}`{% shopping_cart %}`{% endraw %} vous permet de parcourir le contenu actuel du panier d'un utilisateur pour les rappels de panier abandonné, les incitations au paiement ou les confirmations de commande. Pour des exemples de code prêts à l'emploi, consultez les [cas d'utilisation eCommerce]({{site.baseurl}}/ecommerce_use_cases/).

Pour une alternative sans code, les [blocs produit en glisser-déposer]({{site.baseurl}}/user_guide/messaging/design_and_edit/product_blocks/) sont disponibles dans le programme d'accès anticipé.

### Modèles de Canvas eCommerce {#ecommerce-canvas-templates}

Braze propose des modèles de Canvas prêts à l'emploi préconfigurés avec les événements recommandés pour le commerce électronique comme critères d'entrée, de sortie et de conversion, afin que vous puissiez lancer des flux de cycle de vie sans configuration personnalisée. Chaque modèle est livré avec des designs d'e-mail en glisser-déposer et prend en charge les blocs produit en glisser-déposer (actuellement en accès anticipé). Pour des cas d'utilisation détaillés et des exemples Liquid, consultez les [cas d'utilisation eCommerce]({{site.baseurl}}/ecommerce_use_cases/).

Ces modèles couvrent les flux de cycle de vie eCommerce les plus courants. Utilisez-les comme point de départ, puis personnalisez le timing, les canaux et le contenu créatif pour votre audience.

{% tabs %}
{% tab Navigation abandonnée %}

Réengage les utilisateurs qui ont consulté un produit mais ne l'ont pas ajouté à leur panier.

Utilisez ce modèle lorsque vous souhaitez ramener les visiteurs pour qu'ils reconsidèrent les produits qu'ils ont récemment consultés sans passer à l'action.

| Paramètre | Valeur |
| --- | --- |
| Événement d'entrée | `ecommerce.product_viewed` |
| Événements de sortie | `ecommerce.product_viewed`, `ecommerce.cart_updated`, `ecommerce.checkout_started`, Placed Order |
| Événement de conversion | Placed Order |
{: .reset-td-br-1 .reset-td-br-2 aria-label="eCommerce Canvas templates" }

{% endtab %}
{% tab Panier abandonné %}

Récupère les utilisateurs qui ont ajouté des articles à leur panier mais n'ont pas commencé le paiement.

Utilisez ce modèle lorsque vous souhaitez rappeler aux utilisateurs les articles dans leur panier et les inciter à finaliser leur achat.

| Paramètre | Valeur |
| --- | --- |
| Événement d'entrée | `ecommerce.cart_updated` |
| Événements de sortie | `ecommerce.cart_updated`, `ecommerce.checkout_started`, Placed Order |
| Événement de conversion | Placed Order |
{: .reset-td-br-1 .reset-td-br-2 aria-label="eCommerce Canvas templates" }

{% alert tip %}
L'événement `ecommerce.cart_updated` utilise un modèle de remplacement. Chaque événement envoyé écrase l'état du panier de l'utilisateur. Utilisez l'étiquette Liquid {% raw %}`{% shopping_cart %}`{% endraw %} dans votre message pour afficher dynamiquement le contenu actuel du panier au moment de l'envoi.
{% endalert %}

{% endtab %}
{% tab Paiement abandonné %}

Récupère les utilisateurs qui ont commencé le paiement mais n'ont pas finalisé l'achat.

Utilisez ce modèle lorsque vous souhaitez récupérer des achats à l'étape de l'entonnoir où l'intention est la plus forte.

| Paramètre | Valeur |
| --- | --- |
| Événement d'entrée | `ecommerce.checkout_started` |
| Événement de sortie | Placed Order |
| Événement de conversion | Placed Order |
{: .reset-td-br-1 .reset-td-br-2 aria-label="eCommerce Canvas templates" }

{% endtab %}
{% tab Confirmation de commande et enquête %}

Confirme un achat réussi et envoie ensuite une enquête de satisfaction pour collecter des avis et stimuler l'engagement post-achat.

Utilisez ce modèle lorsque vous souhaitez rationaliser la communication post-achat et recueillir les retours clients dans un seul flux de travail.

| Paramètre | Valeur |
| --- | --- |
| Événement d'entrée | `ecommerce.order_placed` |
| Événement de conversion | Start Session ou `ecommerce.product_viewed` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="eCommerce Canvas templates" }

{% endtab %}
{% endtabs %}

#### Personnaliser les modèles {#customize-templates}

Ces modèles sont conçus comme point de départ. Les personnalisations courantes incluent :
  - **Personnaliser l'e-mail :** chaque modèle inclut un e-mail préconfiguré créé avec l'éditeur glisser-déposer, entièrement modifiable pour correspondre à votre marque et votre contenu.
  - **Ajouter des canaux :** associez l'e-mail avec le push, le SMS ou les messages in-app pour un renforcement cross-canal.
  - **Ajouter des délais et des arbres décisionnels :** segmentez les utilisateurs par comportement (par exemple, panier de forte valeur par rapport à un panier de faible valeur) ou définissez des périodes d'attente entre les messages.
  - **Changer le contenu créatif :** remplacez le modèle d'e-mail inclus par le style visuel de votre marque.
  - **Utiliser les blocs produit :** utilisez les blocs produit en glisser-déposer (dans le programme d'accès anticipé) pour afficher dynamiquement le contenu du panier abandonné ou les produits consultés sans écrire de Liquid personnalisé.

Pour des stratégies de cycle de vie plus avancées, y compris des exemples de personnalisation Liquid, consultez les [cas d'utilisation eCommerce]({{site.baseurl}}/ecommerce_use_cases/).

## Reporting eCommerce {#ecommerce-reporting}

Les événements recommandés pour le commerce électronique alimentent les mêmes surfaces de chiffre d'affaires que les clients utilisent déjà aujourd'hui. Lorsque votre intégration envoie des événements eCommerce, les rapports suivants incluent automatiquement le chiffre d'affaires eCommerce :

| Rapport | Ce qu'il affiche |
|---------------------------------------------|-------------------------------------------|
| Rapport sur les revenus | Chiffre d'affaires total, chiffre d'affaires quotidien moyen, achats quotidiens et chiffre d'affaires par utilisateur au fil du temps, toutes sources confondues, pour la plage de dates et les applications sélectionnées. |
| Tableau de bord Last Touch Attribution Revenue | Chiffre d'affaires attribué à la dernière campagne ou au dernier Canvas avec lequel un utilisateur a interagi avant de passer une commande. Les événements de contact incluent les clics sur les e-mails, les ouvertures de push, les clics sur les cartes de contenu, les clics sur les messages in-app et les clics sur les liens courts SMS ou WhatsApp. |
| Analyses des campagnes et des Canvas | Chiffre d'affaires total attribué à une campagne ou un Canvas spécifique dans la fenêtre de conversion principale. |
| Rapport de conversions | Chiffre d'affaires lié aux événements de conversion sur les campagnes et les Canvas.<br> **Remarque :** pour comptabiliser le chiffre d'affaires de `ecommerce.order_placed`, la campagne ou le Canvas doit utiliser le type d'événement de conversion « Place Order » comme événement de conversion. |
| Statistiques des segments | Comparaisons de chiffre d'affaires entre les segments dans le tableau de bord Statistiques des segments. |
| Générateur de rapports | Indicateurs de chiffre d'affaires dans les rapports personnalisés créés dans le Générateur de rapports. |
| Générateur de tableaux de bord | Indicateurs de chiffre d'affaires dans les tableaux de bord personnalisés créés dans le Générateur de tableaux de bord. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="eCommerce reporting" }

Pour les champs calculés non liés à l'utilisateur (par exemple, le chiffre d'affaires d'une campagne ou d'un Canvas), le chiffre d'affaires est calculé de la même manière dans tous les rapports : `price` multiplié par `quantity` par produit dans la commande, sommé sur l'ensemble des produits de chaque événement `order_placed`.

{% alert note %}
Pour éviter le double comptage du chiffre d'affaires, n'envoyez pas à la fois des achats hérités et des événements recommandés pour le commerce électronique pour les mêmes commandes. Si vous prévoyez de passer des achats hérités aux événements recommandés, coordonnez le changement avec votre équipe de compte Braze avant d'effectuer toute modification d'intégration.<br><br>
Les calculs de chiffre d'affaires plafonnent les quantités individuelles de produits à `1 000` unités par commande. Si un champ `quantity` est manquant pour un produit, la valeur par défaut est `1`. L'événement `order_placed` d'origine conserve la quantité complète que vous avez envoyée — seul le calcul du chiffre d'affaires applique le plafond.
{% endalert %}

### BrazeAI<sup>TM</sup>

[Predictive Events]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/), [Predictive Churn]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/) et les [recommandations d'articles]({{site.baseurl}}/user_guide/brazeai/item_recommendations/) prennent en charge les événements eCommerce comme événements cibles et signaux, et disposent d'une option dédiée « Order Placed ». Le schéma standardisé rend ces modèles plus fiables car les données sont cohérentes sur l'ensemble de votre base d'utilisateurs.

### Exporter les données {#export-data}

Braze propose plusieurs moyens d'exporter les données d'événements eCommerce pour les utiliser dans votre entrepôt de données, vos outils de BI ou vos systèmes en aval. Les événements recommandés pour le commerce électronique sont exportés via les mêmes canaux que vos autres données d'événements.

| Chemin d'exportation | Ce qui est inclus |
|------------------------------------- |------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/) | Les événements eCommerce sont diffusés en tant qu'événements personnalisés ; recherchez l'espace de noms `ecommerce.*` pour les trouver. Les produits de chaque commande sont disponibles en tant qu'achats. |
| [Partage de données Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/data_sharing/) | Les événements eCommerce sont partagés en tant qu'événements personnalisés ; recherchez l'espace de noms `ecommerce.*` pour les trouver. Les produits de chaque commande sont disponibles dans la table des achats. |
| [Exporter les données de segment en CSV]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/segment_data_to_csv/) | Export CSV des membres du segment. Pour inclure les événements eCommerce, sélectionnez-les par nom dans le menu déroulant des événements personnalisés. |
| [Exporter le profil utilisateur par segment (API)]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/#prerequisites) | Données de profil utilisateur pour les membres du segment, renvoyées via l'API. Les événements eCommerce sont inclus en tant qu'événements personnalisés. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Export data" }

### Comment segmenter les utilisateurs par produit spécifique ? {#how-do-i-segment-users-by-a-specific-product}

Le segmenteur vous permet de filtrer par le nombre de fois qu'un utilisateur a effectué un événement eCommerce. Pour filtrer par propriétés de produit spécifiques (comme `product_id` ou `product_name`), utilisez les [Extensions de segments]({{site.baseurl}}/user_guide/audience/segments/segment_extension/), qui prennent en charge le filtrage par propriétés d'événement imbriquées. Par exemple, vous pouvez trouver tous les utilisateurs ayant acheté le produit « SKU-123 » au cours des 90 derniers jours.