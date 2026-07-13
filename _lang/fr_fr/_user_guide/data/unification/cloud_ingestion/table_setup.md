---
nav_title: Configuration des tables
article_title: Configuration des tables pour l'Ingestion de données cloud
toc_headers: h2
page_order: 2
page_type: reference
description: "Découvrez comment configurer votre table source CDI et en quoi cette configuration diffère des exigences de formatage du payload."
---

# Configuration des tables pour l'Ingestion de données cloud {#cloud-data-ingestion-table-setup}

> Utilisez cette page pour distinguer deux exigences liées mais distinctes de l'Ingestion de données cloud (CDI) : la configuration de la table source et le formatage du payload.

## Comprendre la configuration des tables par rapport au formatage du payload {#understand-table-setup-compared-to-payload-formatting}

Pour les synchronisations de données utilisateur CDI, configurez les deux éléments suivants :

| Couche | Ce qu'elle contrôle |
| --- | --- |
| Configuration de la table source | Colonnes requises, identifiants utilisateur et comportement de synchronisation `UPDATED_AT` |
| Formatage du payload | Champs JSON dans `payload`, y compris la structure des objets pour les attributs, les événements et les achats |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Comprendre la configuration des tables par rapport au formatage du payload" }

Braze lit d'abord les lignes de votre table source, puis valide le champ `payload` en fonction du type de données sélectionné.

## Configurer votre table source {#set-up-your-source-table}

Pour les synchronisations de données utilisateur depuis un entrepôt de données, votre table ou vue source doit inclure :

- `UPDATED_AT`
- `payload`
- Une ou plusieurs colonnes d'identifiants utilisateur prises en charge :
  - `EXTERNAL_ID`
  - `ALIAS_NAME` et `ALIAS_LABEL`
  - `BRAZE_ID`
  - `EMAIL`
  - `PHONE`

Chaque ligne doit inclure un seul type d'identifiant à la fois, même si votre table contient plusieurs colonnes d'identifiants.

### Exigences pour `UPDATED_AT` {#updated_at-requirements}

- Stockez les valeurs `UPDATED_AT` en UTC pour éviter les problèmes liés aux changements d'heure.
- Braze synchronise les lignes dont la valeur `UPDATED_AT` est postérieure à la dernière valeur synchronisée.
- Les lignes situées exactement à l'horodatage limite peuvent être resynchronisées si de nouvelles lignes partagent cet horodatage.

Pour des conseils sur les horodatages en double et les mises à jour incrémentales, consultez les [bonnes pratiques de l'Ingestion de données cloud]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/best_practices#avoid-resyncing-rows-with-duplicate-timestamps).

{% alert note %}
Les sources de stockage de fichiers utilisent des exigences de configuration différentes et ne prennent pas en charge `UPDATED_AT`. Pour plus de détails, consultez [Intégrations de stockage de fichiers]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/file_storage_integrations#required-file-formats).
{% endalert %}

## Configurer la colonne `payload` {#set-up-the-payload-column}

La valeur `payload` suit les mêmes formats d'objets utilisés par l'endpoint Braze `/users/track` pour le type de données sélectionné.

| Type de données | Référence de formatage |
| --- | --- |
| `attributes` | [Objet d'attributs utilisateur]({{site.baseurl}}/api/objects_filters/user_attributes_object#migrating-push-tokens) |
| `events` | [Objet d'événements]({{site.baseurl}}/api/objects_filters/event_object) |
| `purchases` | [Objet d'achats]({{site.baseurl}}/api/objects_filters/purchase_object) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Configurer la colonne payload" }

Pour les attributs imbriqués, incluez les dates en utilisant le format décrit dans [Capturer des dates en tant que propriétés d'objet]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support#capturing-dates-as-object-properties).

### Exemples de payloads {#payload-examples}

{% tabs local %}
{% tab Attributs personnalisés imbriqués %}
Vous pouvez inclure des attributs personnalisés imbriqués dans la colonne payload pour une synchronisation d'attributs personnalisés.

```json
{
      "most_played_song": {
        "song_name": "Solea",
        "artist_name": "Miles Davis",
        "album_name": "Sketches of Spain",
        "genre": "Jazz",
        "play_analytics": {
            "count": 1000,
            "top_10_listeners": true
        }
      }
}
```

{% endtab %}
{% tab Événement %}
Pour synchroniser des événements, un nom d'événement est requis. Formatez le champ `time` en tant que chaîne ISO 8601 ou au format `yyyy-MM-dd'T'HH:mm:ss:SSSZ`. Si le champ `time` n'est pas présent, Braze utilise la valeur de la colonne `UPDATED_AT` comme heure de l'événement. Les autres champs, y compris `app_id` et `properties`, sont facultatifs.

Vous pouvez synchroniser un événement par ligne.

```json
{
    "app_id" : "your-app-id",
    "name" : "rented_movie",
    "time" : "2013-07-16T19:20:45+01:00",
    "properties": {
        "movie": "The Sad Egg",
        "director": "Alex Smith"
    }
}
```

{% endtab %}
{% tab Achat %}
Pour synchroniser des événements d'achat, `product_id`, `currency` et `price` sont requis. Formatez le champ facultatif `time` en tant que chaîne ISO 8601 ou au format `yyyy-MM-dd'T'HH:mm:ss:SSSZ`. Si le champ `time` n'est pas présent, Braze utilise la valeur de la colonne `UPDATED_AT` comme heure de l'événement. Les autres champs, y compris `app_id`, `quantity` et `properties`, sont facultatifs.

Vous pouvez synchroniser un événement d'achat par ligne.

```json
{
    "app_id" : "11ae5b4b-2445-4440-a04f-bf537764c9ad",
    "product_id" : "Completed Order",
    "currency" : "USD",
    "price" : 219.98,
    "time" : "2013-07-16T19:20:30+01:00",
    "properties" : {
        "products" : [ { "name": "Monitor", "category": "Gaming", "product_amount": 19.99 },
        { "name": "Gaming Keyboard", "category": "Gaming ", "product_amount": 199.99 }
        ]
    }
}
```

{% endtab %}
{% tab Groupes d'abonnement %}
Pour synchroniser les statuts des groupes d'abonnement, incluez une ou plusieurs paires `subscription_group_id` et `subscription_state` dans chaque ligne.
```json
{
    "subscription_groups" : [
        {
            "subscription_group_id": "subscription_group_identifier_1",
            "subscription_state": "unsubscribed"
        },
        {
            "subscription_group_id": "subscription_group_identifier_2",
            "subscription_state": "subscribed"
        },
        {
            "subscription_group_id": "subscription_group_identifier_3",
            "subscription_state": "subscribed"
        }
      ]
}
```
{% endtab %}
{% endtabs %}

## Documentation connexe sur la configuration CDI {#related-cdi-setup-docs}

- Pour des exemples DDL spécifiques aux sources, consultez [Intégrations d'entrepôts de données]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations#step-1-set-up-tables-or-views).
- Pour la configuration basée sur les fichiers, consultez [Intégrations de stockage de fichiers]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/file_storage_integrations).
- Pour des conseils sur le comportement de synchronisation et l'optimisation, consultez les [bonnes pratiques de l'Ingestion de données cloud]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/best_practices).