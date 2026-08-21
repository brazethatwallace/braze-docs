---
nav_title: Filtres calculés
article_title: Filtres calculés
page_order: 5.5
page_type: reference
description: "Cet article de référence explique le fonctionnement des filtres calculés, leur comparaison avec les extensions de segments SQL et comment créer et gérer des filtres calculés."
tool: Segments
---

# Filtres calculés {#calculated-filters}

> Les filtres calculés vous permettent de créer des segments très précis sur une période étendue de l'historique d'un utilisateur. Par exemple, utilisez les filtres calculés pour cibler les utilisateurs qui ont acheté un produit particulier au cours des 16 derniers mois ou qui ont dépensé un certain montant avec votre service. Affinez cette audience en utilisant les propriétés d'événement pour rendre le ciblage encore plus granulaire.

{% alert important %}
Les filtres calculés sont actuellement en accès anticipé. Si vous souhaitez participer à l'accès anticipé, contactez votre gestionnaire de la satisfaction client.
{% endalert %}

## Comment ça fonctionne {#how-it-works}

Les Segments Braze vous offrent des outils de ciblage puissants pour créer des groupes dynamiques d'utilisateurs. Pour la plupart des cas d'usage, cela suffit pour atteindre efficacement votre audience. Les filtres calculés sont conçus pour des cas d'usage avancés où vous devez analyser des comportements remontant jusqu'à deux ans ou appliquer une logique complexe, sans compromettre la rétention des données ni les performances du système. Vous pouvez utiliser les données de votre propre [entrepôt de données]({{site.baseurl}}/user_guide/audience/segments/segment_extension/cdi_segments) pour affiner davantage votre audience.

Par exemple, la segmentation par défaut de Braze identifie les utilisateurs qui correspondent à des critères spécifiques que vous définissez, comme repérer un utilisateur qui a récemment acheté l'un de vos produits. Les filtres calculés vous permettent d'aller plus loin, par exemple en identifiant les utilisateurs qui ont acheté une couleur particulière d'un produit spécifique au moins deux fois entre 18 et 24 mois auparavant. Les filtres calculés sont un complément, pas une obligation. Si vous avez besoin de filtres plus avancés ou d'une fenêtre historique plus longue, ils constituent un excellent outil tout en optimisant votre utilisation des données.

## Filtres calculés et extensions de segments SQL {#calculated-filters-and-sql-segment-extensions}

Les [extensions de segments SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments) et les filtres calculés vous aident tous deux à créer des audiences à partir de comportements d'achat et d'événements personnalisés, mais ils utilisent des outils et des sources de données différents. Les extensions de segments SQL utilisent du SQL que vous écrivez sur vos données Snowflake connectées.

| Comportement | Filtres calculés | Extensions de segments SQL |
|---|---|---|
| Comment vous définissez l'audience | Choisissez des achats, des événements recommandés eCommerce, des interactions avec les messages ou des événements personnalisés, ainsi que des compteurs, des fenêtres temporelles et des filtres de propriétés optionnels | Écrivez du SQL sur votre connexion Snowflake ; utilisez des modèles, l'actualisation incrémentielle ou l'actualisation complète |
| Où la logique s'exécute | Les critères et l'actualisation sont gérés dans Braze en tant que filtres calculés | La requête s'exécute dans le contexte de votre entrepôt de données selon la configuration de votre extension |
| Page de la liste des filtres | Un type de filtre calculé, la colonne **Segments** indique combien de segments utilisent chaque filtre, les statuts **Processing** et **Processing Failed** reflètent l'état de la génération | Inclut une colonne **Type** et des filtres qui varient selon le type d'extension |
| Cas d'usage typiques | Fréquence d'achat, dépenses totales, compteurs d'événements personnalisés et règles basées sur les propriétés sur la fenêtre sélectionnée | Logique adossée à l'entrepôt de données, jointures entre tables, et fenêtres historiques ou agrégations au-delà du formulaire de filtre calculé |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Filtres calculés et extensions de segments SQL" }

### Quand utiliser les filtres calculés {#when-to-use-calculated-filters}

Utilisez les filtres calculés lorsque les règles guidées par le tableau de bord pour les achats, le eCommerce, les interactions avec les messages et les événements personnalisés sont suffisantes et que vous n'avez pas besoin de SQL arbitraire sur les tables de l'entrepôt de données.

### Quand utiliser d'autres types d'extensions de segments {#when-to-use-other-segment-extension-types}

Utilisez les [extensions de segments SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments) lorsque vous avez besoin de SQL complet, de données adossées à Snowflake, de modèles ou de modes d'actualisation conçus pour des requêtes d'entrepôt de données volumineuses ou complexes. Utilisez les [extensions de segments CDI]({{site.baseurl}}/user_guide/audience/segments/segment_extension/cdi_segments) lorsque vous avez besoin de SQL qui interroge directement votre entrepôt de données en utilisant les données des connexions [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion).

### Utiliser les filtres calculés et les extensions de segments ensemble {#use-calculated-filters-and-segment-extensions-together}

Un segment peut référencer un filtre calculé en parallèle d'une extension de segments SQL ou CDI — par exemple, une cohorte définie dans l'entrepôt de données à partir d'une extension, combinée à des règles d'achat ou d'événements personnalisés que vous gérez dans le générateur de filtres calculés.

## Créer un filtre calculé {#create-a-calculated-filter}

Pour créer un filtre calculé, définissez des critères basés sur le comportement des utilisateurs, puis enregistrez et activez le filtre avant de l'utiliser dans un Segment.

### Étape 1 : Configurer les détails {#step-1-set-up-details}

1. Accédez à **Audience** > **Calculated Filters**.
2. Sélectionnez **Create Calculated Filter**.
3. Nommez votre filtre calculé en décrivant les utilisateurs que vous souhaitez cibler. Un nom descriptif facilite la recherche du filtre lorsque vous l'ajoutez à un Segment.
4. (Facultatif) Ajoutez des [tags]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags) pour organiser les filtres calculés dans votre espace de travail.

Vous pouvez également sélectionner **Enable recurring audience update** pour actualiser le filtre selon un calendrier récurrent. Si vous n'activez pas ce paramètre, le filtre calculé ne sera pas actualisé à moins que vous ne mettiez à jour le filtre ou que vous sélectionniez **Update audience**.

### Étape 2 : Choisir vos critères {#step-2-choose-your-criteria}

Choisissez un critère de ciblage basé sur un achat, un événement eCommerce, un événement personnalisé ou une interaction de message. Après avoir sélectionné un type d'événement, choisissez l'événement spécifique, le nombre de fois que l'utilisateur doit l'avoir réalisé (plus de, moins de ou égal à), ainsi que la période.

{% alert note %}
Les filtres **plus de** et **moins de** sont exclusifs : ils n'incluent pas le nombre que vous spécifiez. Par exemple, un filtre pour **plus de 4 fois et moins de 16 fois** inclut les utilisateurs ayant réalisé l'action 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 ou 15 fois.
{% endalert %}

Lorsque vous choisissez votre période, vous pouvez spécifier une plage de dates relative (les X derniers jours), une date de début, une date de fin ou une plage de dates exacte.

![Critères de filtre calculé pour les utilisateurs ayant réalisé un événement personnalisé plus de zéro fois dans la plage de dates du 21 juin 2026 au 27 juin 2026.]({% image_buster /assets/img/segment/calculated_filter_example.png %})

#### Segmentation par propriétés d'événement {#event-property-segmentation}

Pour augmenter la précision du ciblage, sélectionnez **Add Property Filters**. Cela vous permet de filtrer selon les propriétés de votre achat, événement eCommerce ou événement personnalisé. Braze prend en charge la segmentation par propriétés d'événement basée sur les objets de type chaîne de caractères, numérique, booléen et temporel.

Pour les propriétés de type chaîne de caractères, saisissez plusieurs valeurs à la fois, par exemple pour cibler les utilisateurs dont le statut est égal à gold, silver ou bronze. Pour les événements recommandés eCommerce, le menu déroulant des propriétés affiche les propriétés disponibles pour cet événement.

{% alert note %}
Vous n'avez pas besoin de filtres calculés pour utiliser les propriétés d'événement dans votre Segment. Les filtres calculés étendent simplement la fenêtre historique utilisée pour créer un Segment par défaut. Vous pouvez créer un [Segment]({{site.baseurl}}/user_guide/audience/segments) par défaut en temps réel qui utilise les propriétés d'événement des 30 derniers jours. De même, vous pouvez [planifier votre message]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery) pour qu'il se déclenche en temps réel en fonction d'une propriété d'événement, sans filtre calculé nécessaire.
{% endalert %}

### Étape 3 : Enregistrer et activer votre filtre {#step-3-save-and-activate-your-filter}

Sélectionnez **Save** pour enregistrer votre filtre calculé. Vous pouvez enregistrer un filtre sans l'activer, mais vous devez activer un filtre avant qu'il n'apparaisse comme option lors de la création d'un Segment.

Après avoir activé un filtre calculé, Braze l'évalue en temps réel lorsqu'un Segment, une Campaign ou un Canvas qui le référence est évalué.

## Utiliser un filtre calculé dans un segment {#use-a-calculated-filter-in-a-segment}

Après avoir créé et activé un filtre calculé, ajoutez-le lors de la création d'un segment ou de la définition d'une audience pour une Campaign ou un Canvas.

1. Dans le générateur de segments, ouvrez la liste des filtres.
2. Sous **Autres filtres**, sélectionnez **Filtre calculé existant**.
3. Sélectionnez le filtre calculé à inclure dans la définition du segment.

Après avoir ajouté le filtre, sélectionnez l'icône à côté du menu déroulant du filtre pour afficher les détails du filtre et confirmer les critères appliqués à votre audience.

![Filtre calculé dans un générateur de segments avec une icône pour afficher plus de détails.]({% image_buster /assets/img/segment/view_cf_details.png %}){: style="max-width:70%;"}

Pour plus d'informations sur la création de segments, consultez [Créer un segment]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment).

## Gérer les filtres calculés {#manage-calculated-filters}

Accédez à **Audience** > **Calculated Filters** pour afficher, modifier et gérer les filtres calculés dans votre espace de travail.

La page **Calculated Filters** répertorie tous les filtres calculés de votre espace de travail. Vous pouvez affiner la liste à l'aide des contrôles disponibles. Comme il n'existe qu'un seul type de filtre calculé, il n'y a pas d'option pour filtrer par type, et le tableau n'inclut pas de colonne **Type**. Utilisez la colonne **Segments** pour voir combien de Segments utilisent chaque filtre calculé.

### Libellés de statut {#status-labels}

Chaque filtre calculé affiche l'un des statuts suivants. **Processing** et **Processing Failed** s'affichent lorsque la génération de l'audience est en cours ou ne s'est pas terminée avec succès.

| Statut | Description |
|---|---|
| Active | Le filtre est activé et disponible pour être utilisé dans les Segments. |
| Draft | Le filtre est enregistré mais pas activé. |
| Archived | Le filtre est archivé. |
| Processing | Braze traite une mise à jour du filtre. |
| Processing Failed | La dernière tentative de traitement ne s'est pas terminée avec succès. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Libellés de statut" }

### Modifier et gérer des filtres individuels {#edit-and-manage-individual-filters}

Ouvrez le menu contextuel d'un filtre calculé pour le modifier, l'archiver, actualiser l'audience ou voir comment il est utilisé dans la communication. Vous ne pouvez pas modifier un filtre calculé pendant qu'il est en cours de traitement.

{% alert note %}
Votre espace de travail peut contenir jusqu'à 100 filtres calculés activés à la fois. Contactez votre gestionnaire de compte Braze si vous avez besoin d'augmenter cette limite.
{% endalert %}

#### Enregistrer ou activer {#save-versus-activate}

Vous pouvez enregistrer un filtre calculé sans l'activer. Les filtres inactifs restent dans votre espace de travail, mais ne peuvent pas être ajoutés à des Segments tant que vous ne les avez pas activés. Sélectionnez **Activate filter** pour utiliser le filtre dans la segmentation.

## Questions fréquentes {#frequently-asked-questions}

### Puis-je créer un filtre calculé qui utilise plusieurs événements personnalisés ? {#can-i-create-a-calculated-filter-that-uses-multiple-custom-events}

Lorsque vous utilisez des filtres calculés, vous pouvez sélectionner un événement personnalisé, un événement d'achat, un événement eCommerce ou une interaction de canal. Cependant, vous pouvez combiner plusieurs filtres calculés avec un ET ou un OU lors de la création du Segment.

Vous pouvez ajouter plusieurs événements ou référencer plusieurs tables Snowflake en utilisant les [extensions de segments SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments).

### Puis-je archiver des filtres calculés s'ils existent dans une Campaign active ? {#can-i-archive-calculated-filters-if-they-exist-in-an-active-campaign}

Non. Avant de pouvoir archiver un filtre calculé, vous devez le retirer de toutes les communications actives.

### Puis-je utiliser des tableaux dans les filtres calculés ? {#can-i-use-arrays-in-calculated-filters}

Oui. Pour utiliser des tableaux, ajoutez des crochets (`[]`) au nom de votre propriété. Si votre propriété est `location_code`, vous devez saisir `location_code[]`.

Braze utilise `[]` pour parcourir les tableaux et vérifier si un élément du tableau parcouru correspond à la propriété d'événement. Par exemple, vous pourriez créer un filtre calculé d'utilisateurs qui correspondent à au moins une valeur d'une propriété de tableau.

### Comment Braze calcule-t-il la période pour une période relative de « X derniers jours » ? {#how-does-braze-calculate-the-time-period-for-a-relative-time-period-of-last-x-days}

Lorsque les filtres calculés calculent la période relative (« X derniers jours »), l'heure de début est fixée à minuit UTC. Par exemple, pour un filtre calculé qui s'actualise à 2024-09-16 21:00 UTC et spécifie 10 jours, l'heure de début est fixée à 2024-09-06 00:00 UTC, et non à 2024-09-06 21:00 UTC.

Cependant, vous pouvez spécifier les fuseaux horaires en utilisant des segments SQL pour identifier les utilisateurs qui ont effectué l'événement personnalisé il y a 10 jours en se basant sur minuit dans le fuseau horaire de l'entreprise, ou les utilisateurs qui ont effectué l'événement il y a 10 jours en se basant sur l'heure actuelle.