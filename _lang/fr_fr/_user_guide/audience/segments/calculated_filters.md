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
Les filtres calculés sont actuellement en accès anticipé. Si vous souhaitez participer à l'accès anticipé, contactez votre gestionnaire de compte Braze.
{% endalert %}

## Comment ça fonctionne {#how-it-works}

Les Segments Braze vous offrent des outils de ciblage puissants pour créer des groupes d'utilisateurs dynamiques. Pour la plupart des cas d'usage, cela suffit à atteindre votre audience efficacement. Les filtres calculés sont conçus pour des cas d'usage avancés où vous devez analyser des comportements remontant jusqu'à deux ans ou appliquer une logique complexe, sans compromettre la rétention des données ni les performances du système. Vous pouvez utiliser les données de votre propre [entrepôt de données]({{site.baseurl}}/user_guide/audience/segments/segment_extension/cdi_segments) pour affiner davantage votre audience.

Par exemple, la segmentation par défaut de Braze identifie les utilisateurs correspondant à des critères spécifiques que vous définissez, comme repérer un utilisateur qui a récemment acheté l'un de vos produits. Les filtres calculés vous permettent d'aller plus loin, par exemple en identifiant les utilisateurs qui ont acheté une couleur particulière d'un produit spécifique au moins deux fois entre 18 et 24 mois auparavant. Les filtres calculés sont un complément, pas une obligation. Si vous avez besoin de filtres plus avancés ou d'une fenêtre historique plus longue, c'est un excellent outil pour vous aider tout en optimisant l'utilisation de vos données.

## Filtres calculés et extensions de segments SQL {#calculated-filters-and-sql-segment-extensions}

Les [extensions de segments SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments) et les filtres calculés vous aident tous deux à créer des audiences à partir de comportements d'achat et d'événements personnalisés, mais ils utilisent des outils et des sources de données différents. Les extensions de segments SQL utilisent du SQL que vous écrivez sur vos données Snowflake connectées.

| Comportement | Filtres calculés | Extensions de segments SQL |
|---|---|---|
| Comment vous définissez l'audience | Choisissez des achats, des événements recommandés eCommerce, des interactions de messages ou des événements personnalisés, ainsi que des compteurs, des fenêtres temporelles et des filtres de propriétés optionnels | Écrivez du SQL sur votre connexion Snowflake ; utilisez des modèles, une actualisation incrémentale ou une actualisation complète |
| Où s'exécute la logique | Les critères et l'actualisation sont gérés dans Braze en tant que filtres calculés | La requête s'exécute dans le contexte de votre entrepôt de données selon la configuration de votre extension |
| Page de liste des filtres | Une liste partagée pour les filtres d'activité utilisateur et d'objets de données ; la colonne **Segments** indique combien de segments utilisent chaque filtre, et les statuts de traitement reflètent l'état de génération | Inclut une colonne **Type** et des filtres qui varient selon le type d'extension |
| Cas d'usage typiques | Fréquence d'achat, dépenses totales, compteurs d'événements personnalisés et règles basées sur les propriétés sur la fenêtre sélectionnée | Logique adossée à l'entrepôt de données, jointures entre tables, et fenêtres historiques ou agrégations allant au-delà du formulaire de filtre calculé |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Filtres calculés et extensions de segments SQL" }

### Quand utiliser les filtres calculés {#when-to-use-calculated-filters}

Utilisez les filtres calculés lorsque les règles guidées par le tableau de bord pour l'activité utilisateur ou les objets de données sont suffisantes et que vous n'avez pas besoin de SQL arbitraire sur les tables de l'entrepôt de données.

### Quand utiliser d'autres types d'extensions de segments {#when-to-use-other-segment-extension-types}

Utilisez les [extensions de segments SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments) lorsque vous avez besoin de SQL complet, de données adossées à Snowflake, de modèles ou de modes d'actualisation conçus pour des requêtes d'entrepôt de données volumineuses ou complexes. Utilisez les [extensions de segments CDI]({{site.baseurl}}/user_guide/audience/segments/segment_extension/cdi_segments) lorsque vous avez besoin de SQL qui interroge directement votre entrepôt de données à l'aide des données provenant de connexions d'[ingestion de données cloud]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion).

### Utiliser les filtres calculés et les extensions de segments ensemble {#use-calculated-filters-and-segment-extensions-together}

Un segment peut référencer un filtre calculé en même temps qu'une extension de segments SQL ou CDI — par exemple, une cohorte définie dans l'entrepôt de données à partir d'une extension, associée à des règles d'achat ou d'événements personnalisés que vous gérez dans le générateur de filtres calculés.

## Créer un filtre calculé {#create-a-calculated-filter}

Pour créer un filtre calculé, choisissez un type de filtre si vous y êtes invité, définissez vos critères, puis enregistrez et activez le filtre avant de l'utiliser dans un Segment.

### Étape 1 : Configurer les détails {#step-1-set-up-details}

1. Accédez à **Audience** > **Calculated Filters**.
2. Sélectionnez **Create filter**.
3. Si votre espace de travail a les [Comptes]({{site.baseurl}}/user_guide/data/activation/accounts) activés, sélectionnez un type de filtre :
   - **User activity filters :** actions et comportements des utilisateurs.
   - **Data Object filters :** attributs et relations pour les objets de données.
4. Saisissez un nom qui décrit l'audience que vous souhaitez cibler. Un nom descriptif facilite la recherche du filtre lorsque vous l'ajoutez à un Segment.
5. (Facultatif) Ajoutez des [tags]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags) pour organiser les filtres calculés dans votre espace de travail.

Pour les **User activity filters**, sélectionnez **Enable recurring audience update** afin d'actualiser le filtre selon un calendrier récurrent. Si vous n'activez pas ce paramètre, le filtre ne s'actualise que lorsque vous le mettez à jour ou sélectionnez **Update audience**. Les **Data Object filters** sont mis à jour toutes les heures.

### Étape 2 : Choisir vos critères {#step-2-choose-your-criteria}

{% tabs %}
{% tab Filtres d'objets de données %}

Si vous avez sélectionné **Data Object filters**, choisissez un objet de données, puis ajoutez des conditions d'attribut, de relation ou de groupe de filtres. Pour le ciblage basé sur les comptes, consultez [Objets de compte]({{site.baseurl}}/user_guide/data/activation/accounts).

{% endtab %}
{% tab Filtres d'activité utilisateur %}

Si **Create filter** ouvre directement le générateur d'activité utilisateur, ou si vous sélectionnez **User activity filters**, choisissez l'une des options de **Criterion** suivantes pour le ciblage :

- **Made a Purchase**
- **Performed an eCommerce event**
- **Performed a Custom Event**
- **Interacted with Message Channel**

Les options de **Criterion** disponibles varient en fonction des fonctionnalités activées pour votre espace de travail. **Performed an eCommerce event** est toujours disponible. Si vous ne voyez pas une option dont vous avez besoin, contactez votre gestionnaire de compte Braze.

Après avoir sélectionné un type d'événement, choisissez l'événement spécifique, le nombre de fois que l'utilisateur doit l'avoir effectué (plus de, moins de ou égal à), ainsi que la période.

{% alert note %}
Les filtres **plus de** et **moins de** sont exclusifs : ils n'incluent pas le nombre que vous spécifiez. Par exemple, un filtre pour **plus de 4 fois et moins de 16 fois** inclut les utilisateurs ayant eu 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 ou 15 fois.
{% endalert %}

Lorsque vous choisissez votre période, vous pouvez spécifier une plage de dates relative (les X derniers jours), une date de début, une date de fin ou une plage de dates exacte.

![Critères d'un filtre calculé pour les utilisateurs ayant effectué un événement personnalisé plus de zéro fois dans la plage de dates du 21 juin 2026 au 27 juin 2026.]({% image_buster /assets/img/segment/calculated_filter_example.png %})

#### Segmentation par propriétés d'événement {#event-property-segmentation}

Pour améliorer la précision du ciblage, sélectionnez **Add Property Filters**. Cela vous permet de filtrer selon les propriétés de votre achat, de votre événement eCommerce ou de votre événement personnalisé. Braze prend en charge la segmentation par propriétés d'événement basée sur les objets de type chaîne de caractères, numérique, booléen et temporel.

Pour les propriétés de type chaîne de caractères, saisissez plusieurs valeurs à la fois, par exemple pour cibler les utilisateurs dont le statut est égal à gold, silver ou bronze. Pour les événements recommandés eCommerce, le menu déroulant des propriétés affiche les propriétés disponibles pour cet événement.

{% alert note %}
Vous n'avez pas besoin de filtres calculés pour utiliser les propriétés d'événement dans votre Segment. Les filtres calculés étendent simplement la fenêtre historique utilisée pour créer un Segment par défaut. Vous pouvez créer un [Segment]({{site.baseurl}}/user_guide/audience/segments) par défaut en temps réel qui utilise les propriétés d'événement des 30 derniers jours. De même, vous pouvez [planifier votre message]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery) pour qu'il se déclenche en temps réel en fonction d'une propriété d'événement, sans filtre calculé nécessaire.
{% endalert %}

{% endtab %}
{% endtabs %}

### Étape 3 : Enregistrer et activer votre filtre {#step-3-save-and-activate-your-filter}

Sélectionnez **Save as draft** pour enregistrer un nouveau filtre calculé sans l'activer. Pour un filtre activé, sélectionnez **Save changes** pour enregistrer vos modifications. Vous devez sélectionner **Activate filter** avant qu'un brouillon n'apparaisse comme option lors de la création d'un Segment.

Après avoir activé un filtre calculé, Braze commence à calculer son audience. Une fois le traitement terminé, vous pouvez sélectionner le filtre lors de la création d'une audience.

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

La page **Calculated Filters** répertorie les filtres d'activité utilisateur et d'objets de données ensemble. Vous pouvez affiner la liste à l'aide des contrôles disponibles, mais la page ne comprend pas de contrôle de filtrage par type ni de colonne **Type**. Utilisez la colonne **Segments** pour voir combien de Segments utilisent chaque filtre calculé.

### Libellés de statut {#status-labels}

Chaque filtre calculé affiche l'un des statuts suivants. **Processing** et **Processing failed** s'affichent lorsque la génération de l'audience est en cours ou ne s'est pas terminée avec succès.

| Statut | Description |
|---|---|
| Active | Le filtre est activé et disponible pour être utilisé dans les Segments. |
| Draft | Le filtre est enregistré mais non activé. |
| Archived | Le filtre est archivé. |
| Refresh disabled | Les mises à jour récurrentes de l'audience sont désactivées. |
| Processing | Braze traite une mise à jour du filtre. |
| Processing failed | La tentative de traitement la plus récente ne s'est pas terminée avec succès. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Libellés de statut" }

### Modifier et gérer des filtres individuels {#edit-and-manage-individual-filters}

Ouvrez le menu de la ligne d'un filtre calculé pour effectuer une action. Les actions disponibles dépendent du statut du filtre.

Pour les filtres qui ne sont pas archivés, le menu de la ligne comprend **Edit**, **Messaging use**, **Archive** et **Update audience**. **Update audience** est disponible pour les filtres actifs qui ne sont pas en cours de traitement. Vous pouvez modifier un filtre calculé pendant son traitement, mais vous ne pouvez pas enregistrer vos modifications tant que le traitement n'est pas terminé.

{% alert note %}
Votre espace de travail peut contenir jusqu'à 100 filtres calculés actifs à la fois. Contactez votre gestionnaire de compte Braze si vous avez besoin d'augmenter cette limite.
{% endalert %}

#### Désarchiver {#unarchive}

Vous pouvez désarchiver un filtre de l'une des manières suivantes :

- Sélectionnez **Unarchive** dans le menu de la ligne du filtre.
- Sélectionnez un ou plusieurs filtres archivés, puis sélectionnez **Unarchive**.
- Ouvrez un filtre calculé archivé et sélectionnez **Unarchive** sur sa page.

Lorsque vous désarchivez un filtre, son statut revient à celui qu'il avait avant l'archivage :

- Un brouillon revient à **Draft**.
- Un filtre activé revient à **Active**, est comptabilisé dans la limite de filtres actifs et Braze lance une actualisation de l'audience.

Attendez la fin du traitement avant de désarchiver un filtre qui affiche **Processing**. Si vous avez atteint la limite de filtres actifs, archivez un filtre actif avant d'en désarchiver un autre.

#### Enregistrer ou activer {#save-versus-activate}

Vous pouvez enregistrer un filtre calculé sans l'activer. Les filtres inactifs restent dans votre espace de travail mais ne peuvent pas être ajoutés aux Segments tant que vous ne les activez pas. Sélectionnez **Activate filter** pour utiliser le filtre dans la segmentation.

## Questions fréquentes {#frequently-asked-questions}

### Puis-je créer un filtre calculé qui utilise plusieurs événements personnalisés ? {#can-i-create-a-calculated-filter-that-uses-multiple-custom-events}

Lorsque vous utilisez des filtres calculés, vous pouvez sélectionner un événement personnalisé, un événement d'achat, un événement eCommerce ou une interaction de canal. Cependant, vous pouvez combiner plusieurs filtres calculés avec un ET ou un OU lors de la création du Segment.

Vous pouvez ajouter plusieurs événements ou référencer plusieurs tables Snowflake en utilisant les [extensions de segments SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments).

### Puis-je archiver un filtre calculé s'il est en cours d'utilisation ? {#can-i-archive-calculated-filters-if-they-exist-in-an-active-campaign}

Non. Avant de pouvoir archiver un filtre calculé, supprimez-le de toutes les Campaigns, Canvas et Segments qui l'utilisent.

### Puis-je utiliser des tableaux dans les filtres calculés ? {#can-i-use-arrays-in-calculated-filters}

Oui. Pour utiliser des tableaux, ajoutez des crochets (`[]`) au nom de votre propriété. Si votre propriété est `location_code`, vous devez saisir `location_code[]`.

Braze utilise `[]` pour parcourir les tableaux et vérifier si un élément du tableau parcouru correspond à la propriété d'événement. Par exemple, vous pourriez créer un filtre calculé d'utilisateurs qui correspondent à au moins une valeur d'une propriété de type tableau.

### Comment Braze calcule-t-il la période pour une période relative de « X derniers jours » ? {#how-does-braze-calculate-the-time-period-for-a-relative-time-period-of-last-x-days}

Lorsque les filtres calculés calculent la période relative (« X derniers jours »), l'heure de début est définie à minuit UTC. Par exemple, pour un filtre calculé qui s'actualise le 2024-09-16 à 21:00 UTC et spécifie 10 jours, l'heure de début est définie au 2024-09-06 00:00 UTC, et non au 2024-09-06 21:00 UTC.

Cependant, vous pouvez spécifier les fuseaux horaires en utilisant des segments SQL pour identifier les utilisateurs qui ont effectué l'événement personnalisé il y a 10 jours en se basant sur minuit dans le fuseau horaire de l'entreprise, ou les utilisateurs qui ont effectué l'événement il y a 10 jours en se basant sur l'heure actuelle.