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

## Fonctionnement {#how-it-works}

Avec Braze Cloud Data Ingestion (CDI), vous configurez une intégration entre votre instance d'entrepôt de données et l'espace de travail Braze pour synchroniser les données de manière récurrente. Cette synchronisation se fait selon la planification que vous déterminez et chaque intégration peut disposer d'une planification différente. Les synchronisations peuvent avoir lieu d'une fois toutes les 15 minutes à une fois par mois. Si vous avez besoin que les synchronisations se produisent à une fréquence supérieure à 15 minutes, contactez votre gestionnaire du succès des clients ou envisagez d'utiliser les appels REST API pour l'ingestion de données en temps réel.

{% alert note %}
La fréquence de synchronisation dans le tableau de bord contrôle la fréquence à laquelle Braze exécute une synchronisation (par exemple, des options telles que toutes les heures ou des exécutions plus fréquentes au sein d'une heure). Elle ne définit pas un intervalle personnalisé supérieur à une heure entre les exécutions. Pour lancer une synchronisation en dehors de la cadence planifiée — par exemple à la demande après le chargement de votre entrepôt — utilisez l'endpoint [Déclencher une synchronisation]({{site.baseurl}}/api/endpoints/cdi/post_job_sync) avec votre ID d'intégration.
{% endalert %}

Lorsqu'une synchronisation s'exécute, Braze se connecte directement à votre instance d'entrepôt de données, récupère toutes les nouvelles données de la table spécifiée et met à jour les données correspondantes sur votre tableau de bord de Braze. À chaque exécution de la synchronisation, toutes les données mises à jour sont reflétées dans Braze.

### Identifier votre ID d'intégration {#finding-your-integration-id}

Vous pouvez trouver votre ID d'intégration dans l'URL lorsque vous consultez une intégration dans le tableau de bord de Braze. Rendez-vous dans **Data Settings** > **Cloud Data Ingestion** et sélectionnez une intégration. L'ID d'intégration apparaît dans l'URL au format `https://[instance].braze.com/integrations/cloud_data_ingestion/[integration_id]`. Par exemple, si votre URL est `https://dashboard-01.braze.com/integrations/cloud_data_ingestion/abc123xyz`, votre ID d'intégration est `abc123xyz`. Vous pouvez utiliser cet ID lorsque vous effectuez des appels API pour déclencher des synchronisations ou vérifier l'état de la synchronisation.

## Cas d'usage {#use-cases}

Grâce aux fonctionnalités de Cloud Data Ingestion de Braze, vous pouvez :

- Créer une intégration simple dans Braze directement depuis votre entrepôt de données ou solution de stockage de fichiers en quelques minutes seulement.
- Synchroniser en toute sécurité les données utilisateur, y compris les attributs, les événements et les achats, depuis votre entrepôt de données vers Braze.
- Fermer la boucle de données avec Braze en combinant l'ingestion de données cloud avec Currents ou Snowflake Data Sharing.

De plus, les [sources connectées]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/connected_sources) constituent une alternative en zéro copie. Vous pouvez demander à Braze d'interroger directement votre entrepôt de données ou votre solution de stockage de fichiers afin de créer des segments CDI — sans avoir à copier les données sous-jacentes vers Braze.

## Sources de données prises en charge {#supported-data-sources}

Cloud Data Ingestion peut synchroniser les données provenant de :

   - Amazon Redshift
   - Databricks
   - Google BigQuery
   - Microsoft Fabric
   - Snowflake
   - Amazon S3

## Types de données pris en charge {#supported-data-types}

Cloud Data Ingestion prend en charge les types de données suivants :

### Données utilisateur {#user-data}
- Attributs utilisateur, y compris :
   - Attributs personnalisés imbriqués
   - Tableaux d'objets
   - Statuts d'abonnement
- Événements personnalisés
- Événements d'achat
- Demandes de suppression d'utilisateurs

### Objets non utilisateur {#non-user-objects}
- Articles de catalogue

### Envoi de messages en zéro copie {#zero-copy-messaging}
- Sources connectées

## Identifiants utilisateur pour l'ingestion de données {#user-identifiers-for-data-ingestion}

Lors de la synchronisation des données utilisateur via Cloud Data Ingestion, vous pouvez identifier les utilisateurs à l'aide d'un ou plusieurs des types d'identifiants suivants. Chaque ligne de votre table source doit contenir une valeur pour un seul type d'identifiant à la fois, mais votre table peut inclure des colonnes pour un, deux, trois, quatre ou les cinq types d'identifiants.

| Identifiant | Description |
|------------|-------------|
| `EXTERNAL_ID` | L'ID externe qui identifie le profil utilisateur à créer ou à mettre à jour. Cela doit correspondre à la valeur `external_id` utilisée dans Braze. |
| `ALIAS_NAME` et `ALIAS_LABEL` | Ces deux colonnes créent un objet alias d'utilisateur. `alias_name` doit être un identifiant unique et `alias_label` spécifie le type d'alias. Les utilisateurs peuvent avoir plusieurs alias avec différentes étiquettes, mais seulement un `alias_name` par `alias_label`. |
| `BRAZE_ID` | L'identifiant utilisateur Braze généré par le SDK Braze. Il n'est pas possible de créer de nouveaux utilisateurs à l'aide d'un Braze ID via Cloud Data Ingestion. Pour créer de nouveaux utilisateurs, spécifiez un ID utilisateur externe ou un alias d'utilisateur. |
| `EMAIL` | L'adresse e-mail de l'utilisateur. Si plusieurs profils avec la même adresse e-mail existent, le profil le plus récemment mis à jour est prioritaire pour les mises à jour. Si vous indiquez à la fois l'adresse e-mail et le numéro de téléphone, l'adresse e-mail est utilisée comme identifiant principal. |
| `PHONE` | Le numéro de téléphone de l'utilisateur. Si plusieurs profils avec le même numéro de téléphone existent, le profil le plus récemment mis à jour est prioritaire pour les mises à jour. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Identifiants utilisateur pour l'ingestion de données" }

Pour obtenir des informations détaillées sur la configuration des colonnes de table et les exigences de formatage du payload, consultez la documentation sur la [configuration des tables pour Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/table_setup).

Pour des instructions de configuration spécifiques à chaque source et des exemples SQL, consultez les [intégrations d'entrepôts de données]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations).

## Utilisation des points de donnée {#data-point-usage}

Pour les clients bénéficiant d'une facturation basée sur les points de donnée, la facturation par point de donnée pour Cloud Data Ingestion est équivalente à la facturation des mises à jour via l'[endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track). Pour plus d'informations, reportez-vous à la section [Points de donnée]({{site.baseurl}}/user_guide/data/infrastructure/data_points).

{% alert important %}
Braze Cloud Data Ingestion est pris en compte dans la limite de débit disponible. Si vous envoyez des données par une autre méthode, la limite de débit est combinée entre l'API Braze et Cloud Data Ingestion.
{% endalert %}

## Limites du produit {#product-limitations}

| Limitation | Description |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Nombre d'intégrations | Le nombre d'intégrations que vous pouvez configurer n'est pas limité. Cependant, vous ne pouvez configurer qu'une seule intégration par table ou vue. |
| Nombre de lignes | Par défaut, chaque exécution peut synchroniser jusqu'à 500 millions de lignes. Toute synchronisation comportant plus de 500 millions de nouvelles lignes est interrompue. Si vous avez besoin d'une limite plus élevée, contactez votre gestionnaire du succès des clients Braze ou l'assistance Braze. |
| Attributs par ligne | Chaque ligne doit contenir un seul ID utilisateur et un objet JSON comportant jusqu'à 250 attributs. Chaque clé de l'objet JSON compte pour un attribut (c'est-à-dire qu'un tableau compte pour un attribut). |
| Taille du payload | Chaque ligne peut contenir un payload allant jusqu'à 1 Mo. Les payloads supérieurs à 1 Mo sont rejetés et l'erreur « Payload was greater than 1MB » est consignée dans le journal de synchronisation avec l'ID externe associé et le payload tronqué. |
| Type de données | Vous pouvez synchroniser les attributs utilisateur, les événements et les achats via Cloud Data Ingestion. |
| Région Braze | Ce produit est disponible dans toutes les régions Braze. Toute région Braze peut se connecter à n'importe quelle région de données source. |
| Région source | Braze se connecte à votre entrepôt de données ou à votre environnement cloud, quelle que soit la région ou le fournisseur de services cloud. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Limites du produit" }