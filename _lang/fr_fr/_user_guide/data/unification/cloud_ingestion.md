---
nav_title: Cloud Data Ingestion
article_title: Cloud Data Ingestion de Braze
alias: /cloud_ingestion/
description: "Cet article de référence décrit les sources de Cloud Data Ingestion de Braze, ainsi que les recommandations pour la configuration des données."
page_order: 1
toc_headers: h2
---

# Cloud Data Ingestion de Braze {#braze-cloud-data-ingestion}

> Braze Cloud Data Ingestion (CDI) vous permet de configurer une connexion directe depuis votre solution de stockage de données afin de synchroniser les données utilisateur pertinentes et d'autres données non utilisateur vers Braze. Ces données peuvent ensuite être utilisées à des fins de personnalisation ou de segmentation pour optimiser vos cas d'usage marketing. L'intégration flexible de Cloud Data Ingestion prend en charge les structures de données complexes, y compris les JSON imbriqués et les tableaux d'objets.

## Comment ça fonctionne {#how-it-works}

Avec l'ingestion de données cloud (CDI) de Braze, vous configurez une intégration entre votre instance d'entrepôt de données et votre espace de travail Braze pour synchroniser les données de manière récurrente. Cette synchronisation s'exécute selon une planification que vous définissez, et chaque intégration peut avoir une planification différente. Les synchronisations peuvent s'exécuter aussi fréquemment que toutes les 15 minutes ou aussi rarement qu'une fois par mois. Si vous avez besoin de synchronisations plus fréquentes que toutes les 15 minutes, contactez votre gestionnaire du succès des clients ou envisagez d'utiliser des appels REST API pour l'ingestion de données en temps réel.

Les intégrations de stockage de fichiers Amazon S3 sont pilotées par événement. Braze ingère les nouveaux fichiers lorsque les notifications S3/SQS arrivent. Pour les détails de configuration, consultez [Intégrations de stockage de fichiers]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/file_storage_integrations).

{% alert note %}
La fréquence de synchronisation dans le tableau de bord contrôle la fréquence à laquelle Braze exécute une synchronisation (par exemple, des options telles que des exécutions toutes les heures ou plus fréquentes au sein d'une heure). Elle ne définit pas un intervalle personnalisé supérieur à une heure entre les exécutions. Pour lancer une synchronisation en dehors de la cadence planifiée — par exemple, à la demande après la fin du chargement de votre entrepôt — utilisez l'endpoint [Déclencher une synchronisation]({{site.baseurl}}/api/endpoints/cdi/post_job_sync) avec votre ID d'intégration.
{% endalert %}

Lorsqu'une synchronisation s'exécute, Braze se connecte directement à votre instance d'entrepôt de données, récupère toutes les nouvelles données de la table spécifiée et met à jour les données correspondantes sur votre tableau de bord de Braze. À chaque exécution de la synchronisation, toutes les données mises à jour sont reflétées dans Braze.

### Trouver votre ID d'intégration {#finding-your-integration-id}

Vous pouvez trouver votre ID d'intégration dans l'URL lorsque vous consultez une intégration dans le tableau de bord de Braze. Accédez à **Data Settings** > **Cloud Data Ingestion** et sélectionnez une intégration. L'ID d'intégration apparaît dans l'URL au format `https://[instance].braze.com/integrations/cloud_data_ingestion/[integration_id]`. Par exemple, si votre URL est `https://dashboard-01.braze.com/integrations/cloud_data_ingestion/abc123xyz`, votre ID d'intégration est `abc123xyz`. Vous pouvez utiliser cet ID lors d'appels API pour déclencher des synchronisations ou vérifier le statut d'une synchronisation.

## Cas d'usage {#use-cases}

Grâce aux fonctionnalités d'ingestion de données cloud de Braze, vous pouvez :

- Créer une intégration simple directement depuis votre entrepôt de données ou votre solution de stockage de fichiers vers Braze en quelques minutes seulement.
- Synchroniser en toute sécurité les données utilisateur, y compris les attributs, les événements et les achats, depuis votre entrepôt de données vers Braze.
- Boucler la boucle des données avec Braze en combinant l'ingestion de données cloud avec Currents ou le partage de données Snowflake.

De plus, les [Sources connectées]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/connected_sources) constituent une alternative en zéro copie. Vous pouvez faire en sorte que Braze interroge directement votre entrepôt de données ou votre solution de stockage de fichiers pour construire des segments CDI &#8212; le tout sans copier les données sous-jacentes dans Braze.

## Sources de données prises en charge {#supported-data-sources}

L'ingestion de données cloud peut synchroniser des données depuis :

   - Amazon Redshift
   - Databricks
   - Google BigQuery
   - Microsoft Fabric
   - Snowflake
   - Amazon S3

## Types de données pris en charge {#supported-data-types}

L'ingestion de données cloud prend en charge les types de données suivants :

### Données utilisateur {#user-data}
- Attributs utilisateur, y compris :
   - Attributs personnalisés imbriqués
   - Tableaux d'objets
   - Statuts d'abonnement
- Événements personnalisés
- Événements d'achat
- Demandes de suppression d'utilisateurs

### Objets non-utilisateur {#non-user-objects}
- Éléments de catalogue

### Communication en zéro copie {#zero-copy-messaging}
- Sources connectées

## Identifiants utilisateur pour l'ingestion de données {#user-identifiers-for-data-ingestion}

Lors de la synchronisation des données utilisateur via l'ingestion de données cloud, vous pouvez identifier les utilisateurs à l'aide d'un ou plusieurs des types d'identifiants suivants. Chaque ligne de votre table source ne doit contenir une valeur que pour un seul type d'identifiant à la fois, mais votre table peut inclure des colonnes pour un, deux, trois, quatre ou les cinq types d'identifiants.

| Identifiant | Description |
|------------|-------------|
| `EXTERNAL_ID` | L'ID externe qui identifie le profil utilisateur à créer ou à mettre à jour. Il doit correspondre à la valeur `external_id` utilisée dans Braze. |
| `ALIAS_NAME` et `ALIAS_LABEL` | Ces deux colonnes créent un objet alias d'utilisateur. `alias_name` doit être un identifiant unique, et `alias_label` spécifie le type d'alias. Les utilisateurs peuvent avoir plusieurs alias avec différents labels, mais un seul `alias_name` par `alias_label`. |
| `BRAZE_ID` | L'identifiant utilisateur Braze généré par le SDK Braze. Il n'est pas possible de créer de nouveaux utilisateurs à l'aide d'un Braze ID via l'ingestion de données cloud. Pour créer de nouveaux utilisateurs, spécifiez un ID externe ou un alias d'utilisateur. |
| `EMAIL` | L'adresse e-mail de l'utilisateur. Si plusieurs profils avec la même adresse e-mail existent, le profil mis à jour le plus récemment est prioritaire pour les mises à jour. Si vous incluez à la fois l'e-mail et le téléphone, l'e-mail est utilisé comme identifiant principal. |
| `PHONE` | Le numéro de téléphone de l'utilisateur. Si plusieurs profils avec le même numéro de téléphone existent, le profil mis à jour le plus récemment est prioritaire pour les mises à jour. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Identifiants utilisateur pour l'ingestion de données" }

Pour des informations détaillées sur la configuration des colonnes de table et les exigences de formatage du payload, consultez [Configuration des tables pour l'ingestion de données cloud]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/table_setup).

Pour des instructions de configuration spécifiques à chaque source et des exemples SQL, consultez [Intégrations d'entrepôts de données]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations).

## Consommation de points de données {#data-point-usage}

Pour les clients facturés sur la base des points de données, la facturation des points de données pour l'ingestion de données cloud est équivalente à la facturation des mises à jour via l'[endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track). Consultez la section [Points de données]({{site.baseurl}}/user_guide/data/infrastructure/data_points) pour plus d'informations.

{% alert important %}
L'ingestion de données cloud de Braze est prise en compte dans la limite de débit disponible. Par conséquent, si vous envoyez des données via une autre méthode, la limite de débit est combinée entre l'API Braze et l'ingestion de données cloud.
{% endalert %}

## Limites du produit {#product-limitations}

| Limitation            | Description                                                                                                                                                                        |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Nombre d'intégrations | Il n'y a pas de limite au nombre d'intégrations que vous pouvez configurer. Cependant, vous ne pouvez configurer qu'une seule intégration par table ou vue.                                             |
| Nombre de lignes         | Par défaut, chaque exécution peut synchroniser jusqu'à 500 millions de lignes. Toute synchronisation comportant plus de 500 millions de nouvelles lignes est interrompue. Si vous avez besoin d'une limite plus élevée, contactez votre gestionnaire du succès des clients Braze ou le support Braze. |
| Attributs par ligne     | Chaque ligne doit contenir un seul ID utilisateur et un objet JSON contenant jusqu'à 250 attributs. Chaque clé de l'objet JSON compte comme un attribut (c'est-à-dire qu'un tableau compte comme un seul attribut). |
| Taille du payload           | Chaque ligne peut contenir un payload d'une taille maximale de 1 Mo. Les payloads de plus de 1 Mo sont rejetés, et l'erreur « Payload was greater than 1MB » est consignée dans le journal de synchronisation avec l'ID externe associé et le payload tronqué. |
| Type de données              | Vous pouvez synchroniser des attributs utilisateur, des événements personnalisés, des événements d'achat, des éléments de catalogue, des demandes de suppression d'utilisateurs et des déclencheurs Canvas via l'ingestion de données cloud.                                                                                                  |
| Région Braze           | Ce produit est disponible dans toutes les régions Braze. N'importe quelle région Braze peut se connecter à n'importe quelle région source de données.                                                                              |
| Région source       | Braze se connecte à votre entrepôt de données ou à votre environnement cloud dans n'importe quelle région ou chez n'importe quel fournisseur cloud.                                                                                        |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Limites du produit" }