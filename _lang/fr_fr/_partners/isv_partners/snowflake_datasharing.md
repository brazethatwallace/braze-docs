---
nav_title: Partage de données Snowflake
hidden: true
---

# Intégration du partage de données Snowflake {#snowflake-data-sharing-integration}

> Lorsque Snowflake Data Share est utilisé comme méthode d'intégration, Braze provisionne un partage vers votre instance Snowflake au nom du client. Ce partage inclut automatiquement tous les événements liés à l'engagement des messages et au comportement des utilisateurs.

Les partages sont provisionnés par client après l'achat d'un droit de partage de données Snowflake. Lorsqu'un client demande un partage de données, Braze ajoute un partage à l'espace de travail du client, et ce dernier peut utiliser l'interface en libre-service pour ajouter les données du compte Snowflake du partenaire concerné.

![Provisionnement du partage de données Snowflake dans le tableau de bord de Braze]({% image_buster /assets/img/snowflake.png %})

Une fois le partage provisionné, toutes les données sont immédiatement accessibles depuis l'instance Snowflake en tant que partage de données entrant.

![Partage de données entrant Snowflake dans l'instance Snowflake du client]({% image_buster /assets/img/snowflake2.png %})

Dans votre instance Snowflake, vous verrez un partage par région. Chaque table comporte une colonne, `app_group_id`, qui fait office de clé de locataire pour Braze. Lorsque de nouveaux clients sont ajoutés à un partage au sein d'une même région, ils apparaissent sous la forme de différents `app_group_ids` dans les tables existantes.

{% alert important %}
Braze héberge actuellement toutes les données au niveau de l'utilisateur dans les régions Snowflake AWS US East-1 et EU-Central (Francfort). Bien que Braze puisse effectuer des partages inter-régions, il est plus rentable pour les clients de partager avec `US-EAST-1` et/ou `EU-CENTRAL-1`.
{% endalert %}

{% alert tip %}
Téléchargez les [schémas des tables brutes](/docs/assets/download_file/data-sharing-raw-table-schemas.txt) ou utilisez cet ensemble d'[exemples de données d'événements](https://app.snowflake.com/marketplace/listing/GZT0Z5I4XY0/braze-braze-user-event-demo-dataset) disponible sur la place de marché Snowflake pour vous familiariser avec les événements partagés.
{% endalert %}

## Gestion des événements en double {#handling-duplicate-events}

Les doublons sont possibles, mais tous les événements possèdent un identifiant unique : la colonne ID. Les doublons peuvent être supprimés à l'aide de `select distinct(id)`.

## Changements disruptifs et non disruptifs {#breaking-versus-non-breaking-changes}

### Changements non disruptifs {#non-breaking-changes}

{% multi_lang_include partners/snowflake/non_breaking_changes.md %}

{% alert important %}
Les nouvelles colonnes étant considérées comme non disruptives, Braze recommande vivement de lister explicitement les colonnes d'intérêt dans chaque requête plutôt que d'utiliser des requêtes `SELECT *`. Vous pouvez également créer des vues qui nomment explicitement les colonnes, puis interroger ces vues au lieu des tables directement.
{% endalert %}

### Changements disruptifs {#breaking-changes}

{% multi_lang_include partners/snowflake/breaking_changes.md %}

## Mise à jour des tables SNAPSHOTS et CHANGELOGS {#when-snapshots-and-changelogs-tables-are-updated}

Les tables SNAPSHOTS et CHANGELOGS suivent les modifications apportées aux Campaigns et aux Canvas. Comprendre quand ces tables sont mises à jour est important pour interroger les variations de messages et les configurations Canvas les plus récentes.

### CHANGELOGS_CAMPAIGN_SHARED

Une ligne est ajoutée à `CHANGELOGS_CAMPAIGN_SHARED` lorsque :
- La Campaign est lancée, OU
- L'un des champs suivants pouvant faire l'objet d'un instantané est modifié :
  - Nom
  - Actions (y compris les modifications du contenu des messages)
  - Comportements de conversion

{% alert important %}
Enregistrer ou mettre à jour le brouillon post-lancement ne déclenche pas automatiquement une mise à jour. La mise à jour n'est déclenchée que lorsque vous lancez la Campaign ou appliquez les modifications du brouillon post-lancement à la Campaign active.
{% endalert %}

### SNAPSHOTS_CAMPAIGN_MESSAGE_VARIATION_SHARED

`SNAPSHOTS_CAMPAIGN_MESSAGE_VARIATION_SHARED` est dérivé de `CHANGELOGS_CAMPAIGN_SHARED`. Cette table extrait et aplatit la colonne des actions de `CHANGELOGS_CAMPAIGN_SHARED` en enregistrements de variations de messages individuels. Elle est mise à jour en conséquence lorsque `CHANGELOGS_CAMPAIGN_SHARED` est mis à jour.

### CHANGELOGS_CANVAS_SHARED

Une ligne est ajoutée à `CHANGELOGS_CANVAS_SHARED` lorsque :
- Le Canvas est lancé, OU
- L'un des champs suivants pouvant faire l'objet d'un instantané est modifié :
  - Nom
  - Comportements de conversion
  - Variations (pourcentage, affectations de la première étape, noms des variations)

{% alert important %}
Enregistrer ou mettre à jour le brouillon post-lancement ne déclenche pas automatiquement une mise à jour. La mise à jour n'est déclenchée que lorsque vous lancez le Canvas ou appliquez les modifications du brouillon post-lancement au Canvas actif.
{% endalert %}

### SNAPSHOTS_CANVAS_VARIATION_SHARED

`SNAPSHOTS_CANVAS_VARIATION_SHARED` est dérivé de `CHANGELOGS_CANVAS_SHARED`. Cette table utilise le même modèle d'extraction que `SNAPSHOTS_CAMPAIGN_MESSAGE_VARIATION_SHARED` et est mise à jour en conséquence lorsque `CHANGELOGS_CANVAS_SHARED` est mis à jour.

### SNAPSHOTS_CANVAS_STEP_SHARED

Une ligne est ajoutée à `SNAPSHOTS_CANVAS_STEP_SHARED` lorsque :
- Le Canvas est lancé, OU
- Le Canvas actif est mis à jour (le brouillon post-lancement est appliqué), OU
- L'un des champs suivants pouvant faire l'objet d'un instantané est modifié :
  - Nom
  - Actions (y compris les modifications du contenu des messages au sein des variations de messages)

{% alert important %}
Enregistrer le brouillon post-lancement ne déclenche pas automatiquement une mise à jour. La mise à jour n'est déclenchée que lorsque vous lancez le Canvas ou appliquez les modifications du brouillon post-lancement au Canvas actif.
{% endalert %}

### SNAPSHOTS_CANVAS_FLOW_STEP_SHARED

Une ligne est ajoutée à `SNAPSHOTS_CANVAS_FLOW_STEP_SHARED` lorsque :
- Le Canvas est lancé, OU
- Le Canvas actif est mis à jour (le brouillon post-lancement est appliqué), OU
- L'un des champs suivants pouvant faire l'objet d'un instantané est modifié :
  - Nom

{% alert important %}
Enregistrer le brouillon post-lancement ne déclenche pas automatiquement une mise à jour. La mise à jour n'est déclenchée que lorsque vous lancez le Canvas ou appliquez les modifications du brouillon post-lancement au Canvas actif.
{% endalert %}

## Conformité au règlement général sur la protection des données (RGPD) {#general-data-protection-regulation-gdpr-compliance}

{% multi_lang_include partners/snowflake_pii_gdpr.md %}