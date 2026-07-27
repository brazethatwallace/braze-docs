---
nav_title: Treasure Data pour Currents
article_title: Treasure Data pour Currents
description: "Cet article de référence présente le partenariat entre Braze Currents et Treasure Data, une plateforme de données client d'entreprise qui diffuse les données d'événements Braze vers Treasure Data à des fins d'analyse et d'activation."
page_type: partner
tool: Currents
alias: /partners/treasure_data_for_currents/
search_tag: Partner
---


# Treasure Data pour Currents {#treasure-data-for-currents}

> [Treasure Data](https://www.treasuredata.com/) est une plateforme de données client (CDP) qui collecte et achemine des informations provenant de sources multiples vers divers autres emplacements de votre stack marketing.

L'intégration de Braze et Treasure Data vous permet de contrôler le flux d'informations entre les deux systèmes. Avec Currents, vous pouvez diffuser les données d'événements Braze vers Treasure Data et les rendre exploitables dans l'ensemble de vos outils de croissance.

La méthode recommandée est le connecteur **Braze Currents Streaming** dans Treasure Data, associé à un **Custom Currents Export** dans Braze. Cette approche offre :

- La diffusion d'événements en temps réel de Braze vers Treasure Data
- Le routage automatique optionnel par type d'événement vers des tables distinctes
- Un schéma plat, interrogeable en SQL, qui ne nécessite pas d'analyse JSON

{% alert important %}
Le connecteur Braze Currents Streaming est en version bêta. Contactez le support Treasure Data pour l'activer sur votre compte Treasure Data. Pour les détails de configuration côté partenaire, consultez l'[intégration d'importation Braze Currents](https://docs.treasuredata.com/int/braze-currents-import-integration) de Treasure Data.
{% endalert %}

## Conditions préalables {#prerequisites}

| Condition | Description |
| ----------- | ----------- |
| Compte Treasure Data | Un [compte Treasure Data](https://console.treasuredata.com) actif est nécessaire pour bénéficier de ce partenariat. |
| Currents | Pour exporter des données vers Treasure Data, vous devez avoir configuré [Braze Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents#how-to-access-currents) pour votre compte. |
| Connecteur Braze Currents Streaming | Contactez le support Treasure Data pour activer le connecteur Braze Currents Streaming (bêta) sur votre compte Treasure Data. |
| Clé API d'écriture Treasure Data | Une clé API d'écriture Treasure Data authentifie le flux entrant depuis Braze. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Intégration {#integration}

### Étape 1 : Configurer le connecteur dans Treasure Data {#step-1-configure-the-connector-in-treasure-data}

1. Dans la console Treasure Data, accédez à **Connections** > **New Connection**.
2. Sélectionnez **Braze Currents Streaming**.
3. Sous **Authentication**, saisissez votre clé API d'écriture Treasure Data.
4. Sous **Source Settings**, configurez les éléments suivants :

| Champ | Description |
| ----- | ----------- |
| Source Name | Un nom descriptif pour cette connexion |
| Datastore | Sélectionnez **Plazma** |
| Database | La base de données Treasure Data où les événements sont stockés |
| Table | La table de destination par défaut |
| Multiple Tables | Sélectionnez cette option pour router chaque type d'événement Braze vers sa propre table |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Paramètres de la source" }

5. Une fois la configuration enregistrée, copiez l'**Unique ID** (`task_id`). Vous aurez besoin de cette valeur à l'étape suivante.

### Étape 2 : Créer un Custom Currents Export dans Braze {#step-2-create-a-custom-currents-export-in-braze}

L'option **Treasure Data Export** dans l'interface Braze Currents utilise la méthode héritée Postback API et n'est plus recommandée. Utilisez plutôt **Custom Currents Export**.

1. Dans Braze, accédez à **Partner Integrations** > **Data Export**.
2. Sélectionnez **Create New Current** > **Custom Currents Export**.
3. Saisissez un nom d'intégration et une adresse e-mail de contact pour les notifications d'erreur.
4. Sous **Credentials**, saisissez l'URL de l'endpoint correspondant à votre région Treasure Data. Saisissez votre clé API d'écriture Treasure Data comme **Bearer Token**.

| Région | URL de l'endpoint |
| ------ | ------------ |
| US | `https://braze-in-streaming.treasuredata.com/v1/task/{TASK_ID}` |
| EU | `https://braze-in-streaming.eu01.treasuredata.com/v1/task/{TASK_ID}` |
| AP02 | `https://braze-in-streaming.ap02.treasuredata.com/v1/task/{TASK_ID}` |
| Tokyo | `https://braze-in-streaming.treasuredata.co.jp/task/v1/{TASK_ID}` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="URL des endpoints par région" }

Remplacez `{TASK_ID}` par l'Unique ID que vous avez copié à l'[étape 1](#step-1-configure-the-connector-in-treasure-data).

5. Sélectionnez les types d'événements que vous souhaitez exporter. Les connexions Custom Currents peuvent envoyer des événements pour les utilisateurs identifiés et pour les utilisateurs sans `external_user_id`. Treasure Data ingère les deux.
6. Sélectionnez **Launch Current**.

{% alert warning %}
Maintenez votre clé API d'écriture Treasure Data et l'URL de l'endpoint à jour. Si l'endpoint est inaccessible pendant plus de **5&nbsp;jours**, Braze abandonne les événements du connecteur et les données sont définitivement perdues.
{% endalert %}

## Interroger vos données {#query-your-data}

Une fois les événements en cours de diffusion, interrogez-les avec SQL. Treasure Data aplatit le payload, vous n'avez donc pas besoin d'analyser du JSON.

```sql
SELECT
  id AS event_id,
  event_type,
  user_external_user_id,
  properties_campaign_name,
  properties_email_address,
  time
FROM your_database.your_table
WHERE TD_INTERVAL(time, '-1d', 'JST')
```

{% alert note %}
Le champ `time` dans Treasure Data correspond à l'horodatage auquel Treasure Data a reçu et traité l'événement, et non à l'heure d'occurrence originale de l'événement dans Braze.
{% endalert %}

Si vous avez sélectionné **Multiple Tables**, chaque type d'événement est stocké dans sa propre table (par exemple, `users_message_email_open` ou `users_behaviors_purchase`).

Pour confirmer que les données arrivent, exécutez une requête de comptage quelques minutes après le lancement du Current :

```sql
SELECT COUNT(*)
FROM your_table
WHERE TD_INTERVAL(time, '-1h')
```

## Schéma des données {#data-schema}

Treasure Data aplatit le JSON imbriqué jusqu'à deux niveaux de profondeur :

| Type JSON | Type de colonne Treasure Data |
| --------- | ------------------------- |
| string | string |
| number | long |
| boolean | string |
| array | JSON string |
| object (niveau 1) | `field_name` |
| object (niveau 2) | `parent_field_name_field_name` |
| null | omis |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Mappage des types de données" }

Les noms de colonnes utilisent uniquement des lettres minuscules et des underscores.

## Limites {#limits}

| Élément | Limite |
| ---- | ----- |
| Taille maximale du payload | 1&nbsp;Mo par requête |
| Taille du lot | 100 événements par lot (par défaut) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Limites" }

## Détails de l'intégration {#integration-details}

Braze prend en charge l'exportation de toutes les données répertoriées dans les [glossaires d'événements Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) vers Treasure Data. Cela inclut toutes les propriétés des événements d'[engagement des messages]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) et de [comportement des clients]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events).

La structure du payload des données exportées est la même que celle des connecteurs HTTP personnalisés. Vous pouvez consulter des exemples de payloads dans le [dépôt d'exemples de connecteurs HTTP personnalisés](https://github.com/Appboy/currents-examples/tree/master/sample-data/Custom%20HTTP/users/behaviors).

## Migrer depuis la méthode héritée Postback {#migrate-from-the-legacy-postback-method}

Si vous utilisiez précédemment **Treasure Data Export** (Postback) dans Braze :

1. Effectuez la configuration du Custom Currents Export décrite dans cet article.
2. Confirmez que les événements arrivent dans la nouvelle table.
3. Désactivez l'ancien Current basé sur Postback dans Braze.

Les données héritées stockées sous forme de tableaux JSON bruts peuvent toujours être interrogées avec `JSON_PARSE` et `UNNEST`. Les nouvelles données ingérées via le connecteur de streaming utilisent le schéma plat décrit dans [Schéma des données](#data-schema).