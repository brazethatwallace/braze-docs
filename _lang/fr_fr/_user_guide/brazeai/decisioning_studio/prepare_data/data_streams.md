---
nav_title: Snapshots et flux d'événements
article_title: Snapshots et flux d'événements
page_order: 4
page_type: reference
description: "Cet article de référence explique la différence entre les données de type snapshot et les données de type flux d'événements, et comment chacune doit être structurée et transmise à BrazeAI Decisioning Studio."
---

# Snapshots et flux d'événements {#snapshots-versus-event-streams}

> Les données se répartissent en deux catégories fondamentales : les snapshots (état) et les flux d'événements (ce qui s'est passé). Comprendre cette distinction et l'appliquer correctement est l'une des choses les plus importantes que vous puissiez faire pour garantir que votre agent Decisioning Studio apprenne efficacement.

## Données de type snapshot (état) {#snapshot-data-state}

Un snapshot représente l'état d'un client à un moment précis. Il répond à la question : « À quoi ressemble ce client en ce moment ? »

Un snapshot est statique et agrégé. Il reflète le résultat cumulé de tous les changements jusqu'à cet instant. C'est idéal pour les profils clients, les caractéristiques calculées (par exemple, « jours depuis le dernier achat », « niveau de fidélité », « score d'attrition »).

### Champs requis {#required-fields}

| Champ | Objectif |
|-------|---------|
| Identifiant client | À qui correspond cet enregistrement |
| Date du snapshot | Quand ce snapshot a été pris |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Champs requis" }

### Comment les snapshots doivent être mis à jour {#how-snapshots-should-be-updated}

- **Déclencheur :** Basé sur le temps, pas sur les événements. Les snapshots doivent être générés selon un calendrier fixe (par exemple, quotidiennement), indépendamment du fait qu'un client ait eu une activité ce jour-là ou non.
- **Périmètre :** Chaque mise à jour doit inclure tous les clients concernés, y compris ceux qui n'ont eu aucun événement.
- **Méthode :** Ajoutez de nouveaux enregistrements de snapshot au jeu de données plutôt que d'écraser les valeurs précédentes. Cela préserve l'historique des états pour l'entraînement du modèle.

### Requêter les données de snapshot pour une livraison quotidienne {#query-snapshot-data-for-daily-delivery}

Decisioning Studio exécute son pipeline de recommandation une fois par jour. Lors de la livraison des données de snapshot, exportez le snapshot de la veille à chaque exécution du pipeline :

```sql
SELECT *
FROM snapshot_data
WHERE snapshot_date = {t-1} -- on pipeline run date t, export the snapshot from t-1
```

## Données de type flux d'événements (flux) {#event-stream-data-flow}

Un flux d'événements enregistre des actions discrètes au moment où elles se produisent. Il répond à la question : « Qu'a fait ce client, et quand ? » Un flux d'événements est idéal pour les données brutes, immuables, incrémentales et chronologiques. Chaque enregistrement représente un fait survenu à un moment précis. Par exemple, utilisez ce flux de données pour les enregistrements d'activation, les journaux d'engagement (ouvertures, clics), les événements de conversion ou les utilisations de coupons.

### Champs requis

| Champ | Objectif |
|-------|---------|
| Identifiant client | À qui se rapporte cet événement |
| Type d'événement | Ce qui s'est passé (par exemple, activation, conversion, clic) |
| Horodatage de l'événement | Quand l'événement s'est réellement produit |
| Horodatage de création | Quand cet enregistrement a été créé dans votre système (voir la note dans la section suivante) |
| Propriétés d'événement | Métadonnées supplémentaires sur l'événement ; plus elles sont riches, mieux Decisioning Studio peut relier les événements à travers le parcours client |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Champs requis" }

{% alert important %}
L'horodatage de l'événement et l'horodatage de création sont des champs différents et tous deux sont requis. L'horodatage de l'événement enregistre le moment où l'action s'est réellement produite. L'horodatage de création enregistre le moment où l'entrée de données a été écrite dans votre système, ce qui peut être plus tard en raison de délais de traitement. Ne confondez pas les deux.
{% endalert %}

### Comment les flux d'événements doivent être mis à jour {#how-event-streams-should-be-updated}

- **Déclencheur :** Basé sur les événements. De nouveaux enregistrements sont ajoutés lorsque de nouveaux événements se produisent.
- **Périmètre :** Seuls les clients ayant eu un événement obtiennent de nouveaux enregistrements.
- **Méthode :** Les enregistrements existants sont immuables. Les mises à jour sont toujours des insertions de nouveaux enregistrements.

### Requêter les données d'événements pour une livraison quotidienne {#query-event-data-for-daily-delivery}

Utilisez `create_timestamp`, et non `event_timestamp`, pour découper les exports quotidiens. Les événements sont parfois écrits dans votre système après qu'ils se sont produits (arrivées tardives). Si vous découpez sur `event_timestamp`, ces enregistrements arrivés en retard seront définitivement manqués.

```sql
-- Correct: use create_timestamp to ensure late-arriving events are captured
SELECT *
FROM events_data
WHERE DATE(create_timestamp) = {t-1} -- on run date t, export all records created yesterday
```

```sql
-- Incorrect: slicing on event_timestamp will permanently lose late-arriving events
SELECT *
FROM events_data
WHERE DATE(event_timestamp) = {t-1}
```

Par exemple : si un événement s'est produit le 1er janvier mais n'a été écrit dans votre système que le 2 janvier, un découpage par `event_timestamp` le 2 janvier le manquerait entièrement. Un découpage par `create_timestamp` le capture correctement.

## Pour les intégrations natives Braze {#for-native-braze-integrations}

Braze fournit deux mécanismes intégrés qui correspondent directement à ces deux types de données.

### Attributs personnalisés : données de type snapshot {#custom-attributes-snapshot-data}

Les attributs personnalisés stockent l'état au niveau de l'utilisateur à un moment donné. Ils constituent le véhicule approprié pour les profils clients et les caractéristiques calculées (par exemple, `churn_score`, `total_purchases_last_30d`). Ils ne sont **pas** adaptés aux données d'événements brutes, car ils écrasent les valeurs au lieu de les accumuler.

### Braze Currents : données de type flux d'événements {#braze-currents-event-stream-data}

Braze Currents fournit des données de flux d'événements brutes et immuables. La table `USER_BEHAVIOR_CUSTOM_EVENTS` capture chaque instance d'un événement personnalisé au moment où il se produit, ce qui en fait la source appropriée pour les événements d'activation, d'engagement et de conversion.

{% alert tip %}
Considérez les attributs personnalisés comme la source de l'état client et Braze Currents comme la source des événements de comportement client. N'utilisez pas les attributs personnalisés pour transmettre des données d'événements brutes à Decisioning Studio.
{% endalert %}

## Problèmes courants {#common-issues}

### Transmettre des données d'événements sous forme de snapshot {#pass-event-data-as-a-snapshot}

Agréger des données d'événements dans des champs de snapshot avant de les envoyer à Decisioning Studio entraîne plusieurs problèmes :

- **Perte de granularité :** Une fois les données agrégées en un résumé quotidien au niveau client, les enregistrements d'événements individuels sont perdus. Decisioning Studio ne peut pas les reconstituer.
- **Horodatages imprécis :** Un champ comme « last_email_sent » vous indique l'occurrence la plus récente, mais perd l'historique complet des événements et rend l'attribution précise impossible.
- **Mises à jour fantômes :** Même les jours où aucun événement ne s'est produit, l'enregistrement de snapshot est mis à jour, créant des entrées en double difficiles à dédupliquer.

Si vous utilisez Braze, utilisez les exports Currents (et non les attributs personnalisés) pour transmettre les données d'événements brutes à Decisioning Studio.

### Mettre à jour les données de snapshot sur un déclencheur d'événement {#update-snapshot-data-on-an-event-trigger}

Certains déploiements ne mettent à jour les données de snapshot que lorsqu'un événement se produit, par exemple en recalculant une caractéristique uniquement lorsqu'un client effectue un achat. Cela entraîne l'obsolescence des caractéristiques qui dépendent du passage du temps pour les clients qui n'ont pas eu d'événement récent.

Par exemple, une caractéristique comme `days_since_last_purchase` a une valeur correcte différente chaque jour. Si elle n'est recalculée que lors d'un achat, elle restera figée à une valeur incorrecte pour tous les clients qui n'ont pas acheté récemment. Mettez toujours à jour les données de snapshot selon un calendrier basé sur le temps qui couvre tous les clients, chaque jour.