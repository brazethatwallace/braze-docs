---
nav_title: Comparer les options d'ingestion de données
article_title: Comparer les options d'ingestion de données persistante et sans copie
page_order: 1
page_type: reference
description: "Comparez les synchronisations standard de Cloud Data Ingestion, les CDI Segments, les déclencheurs CDI Canvas et l'API /users/track pour choisir comment les données de votre entrepôt ou de vos applications atteignent les profils, Segments et Canvas Braze."
---

# Comparer les options d'ingestion de données persistante et sans copie {#compare-persistent-and-zero-copy-data-ingestion-options}

> Choisissez comment les données de votre entrepôt ou de vos applications atteignent Braze — qu'elles soient copiées sur les profils utilisateur, interrogées sur place pour la segmentation, ou transmises de manière transitoire dans un Canvas — avant de concevoir vos pipelines d'ingestion.

## À propos de cet exemple {#about-this-example}

MovieCanon est un service fictif de streaming de films. Il centralise les données clients, de billetterie et de visionnage dans un entrepôt de données. L'équipe data doit décider comment alimenter Braze pour trois besoins courants :

- **Données de profil :** attributs de palier de fidélité, de valeur vie client et de préférence de genre ou de format qui persistent sur les profils utilisateur Braze.
- **Construction d'audiences :** Segments pilotés par SQL à partir des tables de l'entrepôt sans copier chaque colonne dans Braze.
- **Communication déclenchée :** lignes de l'entrepôt qui doivent déclencher l'entrée dans un Canvas avec une personnalisation propre à chaque ligne, sans qu'il soit nécessaire de la stocker sur le profil.

Braze propose quatre chemins d'ingestion principaux. Les synchronisations standard de Cloud Data Ingestion (CDI) et l'API [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) persistent les données sur les profils. Les CDI Segments (Connected Sources) et les déclencheurs CDI Canvas sont des options sans copie : les données de l'entrepôt restent dans votre entrepôt et ne sont pas écrites sur les profils utilisateur Braze.

Utilisez cette comparaison lorsque vous planifiez votre architecture, dimensionnez le débit ou expliquez les compromis aux parties prenantes techniques et marketing. Elle ne remplace pas les guides de configuration d'intégration pour chaque option.

## Points à prendre en compte {#considerations}

- Cloud Data Ingestion est une fonctionnalité chapeau. Les synchronisations CDI standard copient les données sur les profils Braze (comme `/users/track`). Les CDI Segments et les déclencheurs CDI Canvas conservent les données de l'entrepôt en place sans les écrire sur les profils utilisateur Braze.
- Les synchronisations CDI récurrentes peuvent s'exécuter toutes les 15 minutes à une fois par mois. Si vous avez besoin d'une cadence supérieure à 15 minutes, contactez votre gestionnaire du succès des clients ou utilisez l'ingestion via la REST API. Consultez [Braze Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion).
- Les déclencheurs CDI Canvas partagent la limite de débit [`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases) de la REST API avec le reste du trafic vers cet endpoint. `/users/track` possède ses propres limites et règles de regroupement. Les limites par défaut peuvent être relevées. Accédez à **Paramètres** > **API et identifiants** > **Limites API**, et consultez [Limites de débit de l'API]({{site.baseurl}}/api/api_limits).
- Les Connected Sources et les extensions de segments CDI exécutent des requêtes dans votre entrepôt. Vous supportez les coûts de calcul de l'entrepôt ; Braze ne comptabilise pas de points de donnée pour ces requêtes. Consultez [Connected Sources]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/connected_sources).

## Configuration {#setup}

### Étape 1 : Associer votre cas d'usage à un chemin d'ingestion {#step-1-map-your-use-case-to-an-ingestion-path}

Faites correspondre votre objectif au chemin d'ingestion recommandé et déterminez si ce chemin écrit sur les profils Braze.

| Votre objectif | Chemin recommandé | Écriture sur le profil ? |
| --- | --- | --- |
| Persister des attributs, des événements, des achats ou des éléments de catalogue depuis l'entrepôt | Synchronisation CDI standard | Oui (les données sont copiées sur les profils ou catalogues Braze) |
| Construire des audiences à partir de SQL dans l'entrepôt sans copier les tables sources dans Braze | CDI Segments (Connected Sources) | Non (appartenance uniquement) |
| Faire entrer des utilisateurs dans un Canvas avec un contexte de ligne de l'entrepôt qui ne doit pas persister sur le profil | Déclencheurs CDI Canvas | Non (propriétés de contexte Canvas transitoires) |
| Envoyer des données depuis des applications, des serveurs ou des pipelines de streaming en quasi-temps réel | [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) (ou SDK) | Oui (les données persistent sur les profils) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Associer votre cas d'usage à un chemin d'ingestion" }

### Étape 2 : Comparer la persistance, la latence et le débit {#step-2-compare-persistence-latency-and-throughput}

Comparez la façon dont chaque chemin gère la résidence des données, la latence, le débit et la création d'utilisateurs.

| Dimension | Synchronisation CDI standard | CDI Segments | Déclencheurs CDI Canvas | `/users/track` |
| --- | --- | --- | --- | --- |
| Ce qu'il fait | Lecture planifiée d'une table de l'entrepôt ; écrit des attributs, des événements, des achats, des suppressions d'utilisateurs ou des catalogues | Braze interroge votre entrepôt pour les extensions de segments SQL | Des lignes de l'entrepôt déclenchent l'entrée dans un Canvas avec un contexte de ligne comme propriétés de contexte Canvas | Des applications, serveurs ou pipelines de streaming écrivent des attributs, des événements et des achats sur les profils |
| Résidence des données | Copiées et persistées sur les profils Braze | Restent dans votre entrepôt ; rien n'est écrit sur les profils | Les propriétés de contexte Canvas sont transitoires ; non persistées sur les profils | Copiées et persistées sur les profils Braze |
| Latence typique | Pas en temps réel ; cadence de synchronisation minimale de 15 minutes (la fraîcheur de l'entrepôt s'applique également) | Pas en temps réel ; actualisations selon la planification de votre extension de segments (l'appartenance ne se met pas à jour à chaque modification de l'entrepôt) | Pas en temps réel ; limitée par la planification de synchronisation (minimum 15 minutes) | Quasi-temps réel (traitement asynchrone) |
| Notes sur le débit | Résultat complet de la requête par synchronisation ; Braze regroupe en interne vers `/users/track`, `/users/delete` ou les endpoints de catalogue | Durée d'exécution de requête limitée à 60 minutes par source connectée ; pas de limite d'objets par requête | Partage la limite de débit `/canvas/trigger/send` ; environ 3,75 millions d'entrées Canvas par heure par exécution de synchronisation | Jusqu'à 75 objets combinés par requête ; consultez [Limites de débit de l'API]({{site.baseurl}}/api/api_limits) |
| Taille du lot | Pas de limite d'objets côté CDI pour les lectures d'entrepôt | N/A (le résultat de la requête définit l'appartenance) | Une entrée Canvas par ligne d'entrepôt par exécution de synchronisation | 75 attributs, événements et achats combinés par requête (par défaut) |
| Création d'utilisateurs | Oui, sauf si le mode « mise à jour des profils existants uniquement » est activé | Non (les utilisateurs inconnus dans les résultats de la requête sont ignorés) | Non (uniquement les utilisateurs Braze existants) | Oui, sauf si `_update_existing_only` est défini sur true |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="Comparer la persistance, la latence et le débit" }

### Étape 3 : Comparer les exigences de schéma et d'identifiants {#step-3-compare-schema-and-identifier-requirements}

Comparez les colonnes requises et les identifiants pris en charge pour chaque chemin. Configurez un seul type de donnée par synchronisation CDI standard (par exemple, les attributs dans une intégration et les événements dans une autre).

| Dimension | Synchronisation CDI standard | CDI Segments | Déclencheurs CDI Canvas | `/users/track` |
| --- | --- | --- | --- | --- |
| Colonnes requises / format | Identifiant utilisateur + `UPDATED_AT` + `payload` (JSON) par ligne | Le SQL doit renvoyer uniquement `external_user_id` | Identifiant + `UPDATED_AT` + `PROPERTIES` (JSON ; utilisez `{}` si vide) | Corps de requête `/users/track` standard |
| Identifiants pris en charge | `external_id`, alias d'utilisateur, `braze_id`, e-mail ou téléphone | `external_user_id` uniquement (chaîne de caractères) | `external_id` ou alias d'utilisateur uniquement | `external_id`, alias d'utilisateur, `braze_id`, e-mail ou téléphone |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="Comparer les exigences de schéma et d'identifiants" }

### Étape 4 : Implémenter le chemin sélectionné {#step-4-implement-the-path-you-selected}

- **Synchronisation CDI standard :** créez une table ou une vue dans l'entrepôt, puis suivez [Intégrations Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations) et [Configuration des tables]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/table_setup).
- **CDI Segments :** ajoutez une [source connectée]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/connected_sources), puis créez une [extension de segments CDI]({{site.baseurl}}/user_guide/audience/segments/segment_extension/cdi_segments).
- **Déclencheurs CDI Canvas :** configurez une table source avec `PROPERTIES`, créez et lancez un Canvas de destination, puis créez une synchronisation selon [Personnalisation sans copie avec CDI]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/zero_copy_sync).
- **`/users/track` :** envoyez des requêtes depuis votre application ou middleware. Formatez les payloads selon [POST : Créer et mettre à jour des utilisateurs]({{site.baseurl}}/api/endpoints/user_data/post_user_track).

Pour MovieCanon, un schéma courant est le suivant : synchronisations CDI standard pour l'enrichissement nocturne des profils, CDI Segments pour les règles d'audience exclusivement en entrepôt, déclencheurs Canvas pour les parcours liés au statut des billets ou au visionnage avec un contexte au niveau de la ligne, et `/users/track` pour les événements applicatifs en temps réel.

## Articles connexes {#related-articles}

- [Braze Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion)
- [Connected Sources]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/connected_sources)
- [Personnalisation sans copie avec CDI]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/zero_copy_sync)
- [Extensions de segments CDI]({{site.baseurl}}/user_guide/audience/segments/segment_extension/cdi_segments)
- [Configuration des tables pour Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/table_setup)
- [POST : Créer et mettre à jour des utilisateurs]({{site.baseurl}}/api/endpoints/user_data/post_user_track)
- [Limites de débit de l'API]({{site.baseurl}}/api/api_limits)