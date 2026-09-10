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

Les Segments Braze vous offrent de puissants outils de ciblage pour créer des groupes dynamiques d'utilisateurs. Pour la plupart des cas d'usage, cela suffit pour atteindre efficacement votre audience. Les filtres calculés sont conçus pour des cas d'usage avancés où vous devez analyser des comportements remontant jusqu'à deux ans ou appliquer une logique complexe, sans compromettre la rétention des données ni les performances du système. Utilisez les **filtres d'activité utilisateur** pour les critères d'achat et d'événements eCommerce, ou les **filtres d'objets de données** pour le ciblage par compte et par objet personnalisé.

Par exemple, la segmentation par défaut de Braze identifie les utilisateurs qui correspondent à des critères spécifiques que vous définissez, comme repérer un utilisateur ayant récemment acheté l'un de vos produits. Les filtres calculés vous permettent d'aller plus loin, par exemple en identifiant les utilisateurs qui ont acheté une couleur particulière d'un produit spécifique au moins deux fois entre 18 et 24 mois auparavant. Les filtres calculés sont un complément, pas une obligation. Si vous avez besoin de filtres plus avancés ou d'une fenêtre historique plus longue, ils constituent un excellent outil tout en maintenant une utilisation optimisée de vos données.

## Filtres calculés et extensions de Segments SQL {#calculated-filters-and-sql-segment-extensions}

Les [extensions de Segments SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments) et les filtres calculés vous aident tous deux à créer des audiences à partir du comportement d'achat, mais ils utilisent des outils et des sources de données différents. Les extensions de Segments SQL utilisent du SQL que vous écrivez sur vos données Snowflake connectées.

| Comportement | Filtres calculés | Extensions de Segments SQL |
|---|---|---|
| Comment vous définissez l'audience | Choisissez des achats ou des événements eCommerce recommandés, ainsi que des décomptes, des fenêtres temporelles et des filtres de propriétés facultatifs | Écrivez du SQL sur votre connexion Snowflake ; utilisez des modèles, l'actualisation incrémentielle ou l'actualisation complète |
| Où la logique s'exécute | Les critères et l'actualisation sont gérés dans Braze en tant que filtres calculés | La requête s'exécute dans le contexte de votre entrepôt de données selon la configuration de votre extension |
| Page de liste des filtres | Une liste partagée pour les filtres d'activité utilisateur et d'objets de données. La colonne **Segments** indique combien de Segments utilisent chaque filtre, et les statuts de traitement reflètent l'état de génération | Comprend une colonne **Type** et des filtres qui varient selon le type d'extension |
| Cas d'usage typiques | Fréquence d'achat, dépense totale et règles basées sur les propriétés sur la fenêtre sélectionnée | Logique adossée à l'entrepôt de données, jointures entre tables, et fenêtres historiques ou agrégations au-delà du formulaire de filtre calculé |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Filtres calculés et extensions de Segments SQL" }

### Quand utiliser les filtres calculés {#when-to-use-calculated-filters}

Utilisez les filtres calculés lorsque les règles d'activité utilisateur ou d'objets de données guidées par le tableau de bord suffisent et que vous n'avez pas besoin de SQL arbitraire sur les tables de l'entrepôt de données.

### Quand utiliser d'autres types d'extensions de Segments {#when-to-use-other-segment-extension-types}

Utilisez les [extensions de Segments SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments) lorsque vous avez besoin de SQL complet, de données adossées à Snowflake, de modèles ou de modes d'actualisation conçus pour des requêtes d'entrepôt volumineuses ou complexes. Utilisez les [extensions de Segments CDI]({{site.baseurl}}/user_guide/audience/segments/segment_extension/cdi_segments) lorsque vous avez besoin de SQL qui interroge directement votre entrepôt de données en utilisant les données issues des connexions [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion).

### Utiliser les filtres calculés et les extensions de Segments ensemble {#use-calculated-filters-and-segment-extensions-together}

Un Segment peut référencer un filtre calculé en parallèle d'une extension de Segments SQL ou CDI — par exemple, une cohorte définie dans l'entrepôt de données via une extension, combinée à des règles d'achat que vous gérez dans le générateur de filtres calculés.

## Créer un filtre calculé {#create-a-calculated-filter}

Pour créer un filtre calculé, choisissez un type de filtre si vous y êtes invité, définissez vos critères, puis enregistrez et activez le filtre avant de l'utiliser dans un Segment.

### Étape 1 : Configurer les détails {#step-1-set-up-details}

1. Accédez à **Audience** > **Calculated Filters**.
2. Sélectionnez **Create filter**.
3. Si votre espace de travail a les [Comptes]({{site.baseurl}}/user_guide/data/activation/accounts) activés, sélectionnez un type de filtre :
   - **User activity filters :** Actions et comportements des utilisateurs.
   - **Data Object filters :** Attributs et relations des objets de données.
4. Saisissez un nom décrivant l'audience que vous souhaitez cibler. Un nom descriptif facilite la recherche du filtre lorsque vous l'ajoutez à un Segment.
5. (Facultatif) Ajoutez des [tags]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags) pour organiser les filtres calculés dans votre espace de travail.

Pour les **User activity filters**, sélectionnez **Enable recurring audience update** afin d'actualiser le filtre selon un calendrier récurrent. Si vous n'activez pas ce paramètre, le filtre ne s'actualise pas, sauf si vous le mettez à jour ou sélectionnez **Update audience**. Les **Data Object filters** sont mis à jour toutes les heures.

### Étape 2 : Choisir vos critères {#step-2-choose-your-criteria}

{% tabs %}
{% tab Filtres d'objets de données %}

Si vous avez sélectionné **Data Object filters**, choisissez un objet de données, puis ajoutez des conditions d'attributs, de relations ou de groupes de filtres. Pour le ciblage basé sur les comptes, consultez [Objets de compte]({{site.baseurl}}/user_guide/data/activation/accounts).

{% endtab %}
{% tab Filtres d'activité utilisateur %}

Si **Create filter** ouvre directement le générateur d'activité utilisateur, ou si vous sélectionnez **User activity filters**, choisissez l'une des options de **Criterion** suivantes pour le ciblage :

- **Made a Purchase**
- **Performed an eCommerce event**

Après avoir sélectionné un type d'événement, choisissez l'événement spécifique, le nombre de fois que l'utilisateur doit l'avoir réalisé (plus de, moins de ou égal à) et la période.

{% alert note %}
Les filtres **plus de** et **moins de** sont exclusifs : ils n'incluent pas le nombre que vous spécifiez. Par exemple, un filtre pour **plus de 4 fois et moins de 16 fois** inclut les utilisateurs ayant un total de 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 ou 15 fois.
{% endalert %}

Lorsque vous choisissez votre période, vous pouvez spécifier une plage de dates relative (les X derniers jours), une date de début, une date de fin ou une plage de dates exacte. Pour les plages relatives, saisissez de **1** à **730** jours (deux ans). Pour les plages de dates absolues, la date de début doit se situer dans les deux dernières années et la date de fin dans les deux prochaines années.

#### Segmentation par propriétés d'événement {#event-property-segmentation}

Pour augmenter la précision du ciblage, sélectionnez **Add event property filters**. Cela vous permet de filtrer selon les propriétés de votre achat ou événement eCommerce. Braze prend en charge la segmentation par propriétés d'événement basée sur les chaînes de caractères, les valeurs numériques, les booléens et les objets temporels.

Pour les propriétés de type chaîne de caractères, saisissez plusieurs valeurs à la fois — par exemple, pour cibler les utilisateurs dont le statut est égal à gold, silver ou bronze. Pour les événements recommandés eCommerce, le menu déroulant des propriétés se remplit avec les propriétés disponibles pour cet événement.

{% alert note %}
Vous n'avez pas besoin de filtres calculés pour utiliser les propriétés d'événement dans votre Segment. Les filtres calculés étendent simplement la fenêtre historique utilisée pour créer un Segment par défaut. Vous pouvez créer un [Segment]({{site.baseurl}}/user_guide/audience/segments) par défaut en temps réel qui utilise les propriétés d'événement des 30 derniers jours. De même, vous pouvez [planifier votre message]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery) pour qu'il se déclenche en temps réel en fonction d'une propriété d'événement — aucun filtre calculé n'est requis.
{% endalert %}

{% endtab %}
{% endtabs %}

### Étape 3 : Enregistrer et activer votre filtre {#step-3-save-and-activate-your-filter}

Sélectionnez **Save as draft** pour enregistrer un nouveau filtre calculé sans l'activer. Pour un filtre activé, sélectionnez **Save changes** pour enregistrer vos modifications. Vous devez sélectionner **Activate filter** avant que le filtre ne soit disponible dans le générateur de Segments.

Après avoir activé un filtre calculé, Braze commence à calculer son audience. Lorsque le traitement est terminé, vous pouvez sélectionner le filtre lors de la création d'une audience.

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

La page **Calculated Filters** répertorie ensemble les filtres d'activité des utilisateurs et les filtres d'objets de données. Vous pouvez affiner la liste à l'aide des contrôles disponibles, mais la page ne propose pas de contrôle de filtrage par type ni de colonne **Type**. Utilisez la colonne **Segments** pour voir combien de Segments utilisent chaque filtre calculé.

### Libellés de statut {#status-labels}

Chaque filtre calculé affiche l'un des statuts suivants. **Processing** et **Processing failed** apparaissent lorsque la génération de l'audience est en cours ou ne s'est pas terminée avec succès.

| Statut | Description |
|---|---|
| Active | Le filtre est activé et disponible pour une utilisation dans les Segments. |
| Draft | Le filtre est enregistré mais pas activé. |
| Archived | Le filtre est archivé. |
| Refresh disabled | Les mises à jour récurrentes de l'audience sont désactivées. Braze peut définir automatiquement ce statut lorsqu'un filtre avec actualisation planifiée n'est pas utilisé. |
| Processing | Braze traite une mise à jour du filtre. |
| Processing failed | La dernière tentative de traitement ne s'est pas terminée avec succès. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Libellés de statut" }

### Modifier et gérer des filtres individuels {#edit-and-manage-individual-filters}

Ouvrez le menu contextuel d'un filtre calculé pour effectuer une action. Les actions disponibles dépendent du statut du filtre.

Pour les filtres qui ne sont pas archivés, le menu contextuel comprend **Edit**, **Messaging use**, **Archive** et **Update audience**. **Update audience** est disponible pour les filtres actifs qui ne sont pas en cours de traitement. Vous pouvez modifier un filtre calculé pendant qu'il est en cours de traitement, mais vous ne pouvez pas enregistrer vos modifications tant que le traitement n'est pas terminé.

#### Archiver {#can-i-archive-calculated-filters-if-they-exist-in-an-active-campaign}

Avant d'archiver un filtre calculé, vérifiez s'il est toujours utilisé. L'archivage peut silencieusement interrompre des Campaigns, des Canvas ou des Segments actifs qui le référencent.

- **Filtres d'objets de données :** Si une Campaign, un Canvas ou un Segment actif référence encore le filtre, l'archiver signifie que cette Campaign, ce Canvas ou ce Segment ne correspondra à aucun utilisateur lors de son prochain lancement ou envoi. Supprimez d'abord la référence pour éviter cela.
- **Filtres d'activité des utilisateurs :** Si un brouillon de Campaign ou de Canvas référence encore le filtre, l'archiver fige l'audience de ce brouillon aux derniers résultats actualisés du filtre. Elle ne sera plus mise à jour tant que vous n'aurez pas supprimé la référence.

Pour savoir où un filtre est utilisé, sélectionnez **Messaging use** dans son menu contextuel.

Vous ne pouvez pas archiver un filtre calculé qui est référencé par une Campaign, un Canvas ou un Segment actif (et non en brouillon). Supprimez ces références avant de l'archiver. Si vous archivez plusieurs filtres de types différents en même temps, vous verrez une confirmation distincte pour chaque type.

{% alert note %}
Votre espace de travail peut contenir jusqu'à 100 filtres calculés actifs à la fois. Contactez votre gestionnaire de compte Braze si vous devez augmenter cette limite.
{% endalert %}

#### Désarchiver {#unarchive}

Vous pouvez désarchiver un filtre de l'une des manières suivantes :

- Sélectionnez **Unarchive** dans le menu contextuel du filtre.
- Sélectionnez un ou plusieurs filtres archivés, puis sélectionnez **Unarchive**.
- Ouvrez un filtre calculé archivé et sélectionnez **Unarchive** sur sa page.

Lorsque vous désarchivez un filtre, son statut revient à ce qu'il était avant l'archivage :

- Un brouillon revient à **Draft**.
- Un filtre activé revient à **Active**, est comptabilisé dans la limite de filtres actifs, et Braze lance une actualisation de l'audience.

Attendez la fin du traitement avant de désarchiver un filtre qui affiche **Processing**. Si vous avez atteint la limite de filtres actifs, archivez un filtre actif avant d'en désarchiver un autre.

#### Enregistrer ou activer {#save-versus-activate}

Vous pouvez enregistrer un filtre calculé sans l'activer. Les filtres inactifs restent dans votre espace de travail, mais ne peuvent pas être ajoutés à des Segments tant que vous ne les avez pas activés. Sélectionnez **Activate filter** pour utiliser le filtre dans la segmentation.

## Questions fréquentes {#frequently-asked-questions}

### Puis-je créer un filtre calculé qui utilise plusieurs événements personnalisés ? {#can-i-create-a-calculated-filter-that-uses-multiple-custom-events}

Lorsque vous utilisez des filtres calculés, vous pouvez sélectionner un événement personnalisé, un événement d'achat, un événement eCommerce ou une interaction de canal. Cependant, vous pouvez combiner plusieurs filtres calculés avec un opérateur AND ou OR lors de la création du Segment.

Vous pouvez ajouter plusieurs événements ou référencer plusieurs tables Snowflake en utilisant les [extensions de segments SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments).

### Puis-je utiliser des tableaux dans les filtres calculés ? {#can-i-use-arrays-in-calculated-filters}

Oui. Pour utiliser des tableaux, ajoutez des crochets (`[]`) au nom de votre propriété. Si votre propriété est `location_code`, vous saisiriez `location_code[]`.

Braze utilise `[]` pour parcourir les tableaux et vérifier si un élément du tableau parcouru correspond à la propriété d'événement. Par exemple, vous pourriez créer un filtre calculé d'utilisateurs qui correspondent à au moins une valeur d'une propriété de tableau.

### Comment Braze calcule-t-il la période pour une période relative de « X derniers jours » ? {#how-does-braze-calculate-the-time-period-for-a-relative-time-period-of-last-x-days}

Lorsque les filtres calculés calculent la période relative (« X derniers jours »), l'heure de début est fixée à minuit UTC. Par exemple, pour un filtre calculé qui s'actualise le 2024-09-16 à 21:00 UTC et spécifie 10 jours, l'heure de début est fixée au 2024-09-06 à 00:00 UTC, et non au 2024-09-06 à 21:00 UTC. Les filtres calculés utilisent toujours l'heure UTC pour les fenêtres temporelles ; le fuseau horaire de votre espace de travail ne s'applique pas.

Cependant, vous pouvez spécifier des fuseaux horaires en utilisant les [extensions de segments SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments) pour identifier les utilisateurs ayant effectué un événement il y a 10 jours en se basant sur minuit à l'heure de l'entreprise, ou les utilisateurs ayant effectué l'événement il y a 10 jours en se basant sur l'heure actuelle.