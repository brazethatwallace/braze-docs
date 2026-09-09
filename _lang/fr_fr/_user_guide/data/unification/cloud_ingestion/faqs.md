---
nav_title: FAQ
article_title: "FAQ sur l'ingestion de données cloud"
page_order: 10
page_type: FAQ
description: "Cette page répond aux questions fréquemment posées sur l'ingestion de données cloud."
toc_headers: h2
---

# Questions fréquemment posées {#frequently-asked-questions}

> Cette page contient des réponses à certaines questions fréquemment posées concernant l'ingestion de données cloud.

## Pourquoi ai-je reçu un e-mail : « Error in CDI Sync » ? {#why-was-i-emailed-error-in-cdi-sync}

Ce type d'e-mail signifie généralement qu'il y a un problème avec votre configuration CDI. Voici quelques problèmes courants et comment les résoudre :

### CDI ne peut pas accéder à l'entrepôt de données ou à la table avec vos identifiants {#cdi-cant-access-the-data-warehouse-or-table-using-your-credentials}

Cela peut signifier que les identifiants dans CDI sont incorrects ou mal configurés sur l'entrepôt de données. Pour plus d'informations, consultez [Intégrations d'entrepôt de données]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations).

### La table est introuvable {#the-table-cannot-be-found}

Essayez de mettre à jour votre intégration avec la bonne configuration de base de données ou créez les ressources correspondantes sur l'entrepôt de données, telles que `database/table`.

### Le catalogue est introuvable {#the-catalog-cannot-be-found}

Le catalogue configuré dans l'intégration n'existe pas dans le catalogue Braze. Un catalogue peut avoir été supprimé après la mise en place de l'intégration. Pour résoudre le problème, mettez à jour l'intégration pour utiliser un autre catalogue ou créez un nouveau catalogue correspondant au nom du catalogue dans l'intégration.

## Pourquoi ai-je reçu un e-mail : « Erreurs de lignes dans votre synchronisation CDI » ? {#why-was-i-emailed-row-errors-in-your-cdi-sync}

Ce type d'e-mail signifie que certaines de vos données n'ont pas pu être traitées lors de la synchronisation. Pour connaître l'erreur spécifique, vous pouvez consulter les journaux dans Braze en accédant à **CDI** > **Sync Log**.

## Comment corriger l'erreur « Time must be string in ISO8601 Format » lors de la configuration CDI ? {#how-do-i-fix-time-must-be-string-in-iso8601-format-in-cdi-setup}

Cette erreur signifie que la valeur `time` de l'événement dans votre payload CDI n'est pas dans un format datetime pris en charge.

Pour les payloads d'événements et d'achats, formatez `time` sous l'une des formes suivantes :

- Une chaîne ISO 8601, ou
- `yyyy-MM-dd'T'HH:mm:ss:SSSZ`

Si `time` est omis, Braze utilise `UPDATED_AT` comme horodatage de l'événement.

Pour connaître l'ensemble des exigences relatives aux payloads, consultez la section [Configuration des tables pour l'ingestion de données cloud]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/table_setup).

## Comment corriger les erreurs pour Test Connection et les e-mails de support ? {#how-do-i-fix-errors-for-test-connection-and-support-emails}

{% tabs %}
{% tab Snowflake %}
### Test Connection est lent {#test-connection-runs-slow}

Test Connection s'exécute sur votre entrepôt de données, donc augmenter la capacité de l'entrepôt peut améliorer sa vitesse. L'utilisation d'une instance SQL serverless réduira le temps de préchauffage et améliorera le débit des requêtes, mais peut entraîner des coûts d'intégration légèrement plus élevés.

### Erreur de connexion à l'instance Snowflake : Incoming request with IP is not allowed to access Snowflake {#error-connecting-to-snowflake-instance-incoming-request-with-ip-is-not-allowed-to-access-snowflake}

Essayez d'ajouter les adresses IP officielles de Braze à votre liste d'adresses IP autorisées. Pour plus d'informations, consultez [Intégrations d'entrepôts de données]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations), ou autorisez les adresses IP pertinentes :

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

### Erreur d'exécution SQL due à la configuration client : 002003 (42S02): SQL compilation error: does not exist or not authorized {#error-executing-sql-due-to-customer-config-002003-42s02-sql-compilation-error-does-not-exist-or-not-authorized}

Si la table n'existe pas, créez-la. Si la table existe, vérifiez que l'utilisateur et le rôle disposent des permissions de lecture sur la table.

### Could not use schema {#could-not-use-schema}

Si vous recevez cette erreur, accordez l'accès à ce schéma pour l'utilisateur ou le rôle spécifié.

### Could not use role {#could-not-use-role}

Si vous recevez cette erreur, autorisez cet utilisateur à utiliser le rôle spécifié.

### User access disabled {#user-access-disabled}

Si vous recevez cette erreur, autorisez cet utilisateur à accéder à votre compte Snowflake.

### Erreur de connexion à l'instance Snowflake avec la clé actuelle et l'ancienne clé {#error-connecting-to-snowflake-instance-with-current-and-old-key}

Si vous recevez cette erreur, assurez-vous que l'utilisateur utilise la clé publique actuelle telle qu'affichée dans votre tableau de bord de Braze.
{% endtab %}

{% tab Redshift %}
### Test Connection est lent

Test Connection s'exécute sur votre entrepôt de données, donc augmenter la capacité de l'entrepôt peut améliorer sa vitesse. L'utilisation d'une instance SQL serverless réduira le temps de préchauffage et améliorera le débit des requêtes, mais peut entraîner des coûts d'intégration légèrement plus élevés.

### Permission denied for relation {table_name} {#permission-denied-for-relation-table_name}

Si vous recevez cette erreur :

  - Accordez la permission `usage` sur le schéma pour cet utilisateur.
  - Accordez la permission `select` sur la table pour cet utilisateur.

### Create Connection Error {#create-connection-error}

Si vous recevez cette erreur, vérifiez que l'endpoint et le port Redshift sont corrects.

### Create SSH Tunnel Error {#create-ssh-tunnel-error}

Si vous recevez cette erreur :

  - Vérifiez que la clé publique de votre tableau de bord de Braze se trouve sur l'hôte EC2 utilisé pour le tunnel SSH.
  - Vérifiez que votre nom d'utilisateur est correct.
  - Vérifiez que le tunnel SSH est correct.
{% endtab %}

{% tab BigQuery %}
### Test Connection est lent

Test Connection s'exécute sur votre entrepôt de données, donc augmenter la capacité de l'entrepôt peut améliorer sa vitesse. L'utilisation d'une instance SQL serverless réduira le temps de préchauffage et améliorera le débit des requêtes, mais peut entraîner des coûts d'intégration légèrement plus élevés.

### User does not have permission to query table {#user-does-not-have-permission-to-query-table}

Si vous recevez cette erreur, ajoutez les permissions utilisateur pour interroger la table.

### Your usage exceeded the custom quota {#your-usage-exceeded-the-custom-quota}

Si vous recevez cette erreur, votre quota doit être mis à jour afin que vous puissiez continuer la synchronisation au rythme actuel.

### Table was not found in location {region} Location {#table-was-not-found-in-location-region-location}

Si vous recevez cette erreur, vérifiez que votre table se trouve dans le bon projet et le bon jeu de données.

### Invalid JWT Signature {#invalid-jwt-signature}

Si vous recevez cette erreur, vérifiez que le service API BigQuery est activé pour votre compte.
{% endtab %}

{% tab Databricks %}
### Test Connection est lent

Test Connection s'exécute sur votre entrepôt de données, donc augmenter la capacité de l'entrepôt peut améliorer sa vitesse. Pour Databricks, il peut y avoir deux à cinq minutes de préchauffage lorsque Braze se connecte à des instances SQL Classic et Pro, ce qui entraînera des retards lors de la configuration et du test de la connexion, ainsi qu'au début des synchronisations planifiées. L'utilisation d'une instance SQL serverless réduira le temps de préchauffage et améliorera le débit des requêtes, mais peut entraîner des coûts d'intégration légèrement plus élevés.

### Command failed because warehouse was stopped {#command-failed-because-warehouse-was-stopped}

Si vous recevez cette erreur, assurez-vous que l'entrepôt Databricks est en cours d'exécution.

### Service: Amazon S3; Status Code: 403; Error Code: 403 Forbidden

Si vous recevez cette erreur, consultez [Databricks: Forbidden error while accessing S3 data](https://kb.databricks.com/security/forbidden-access-to-s3-data).
{% endtab %}
{% endtabs %}

## Comment mettre à jour mes préférences d'alerte par e-mail pour les intégrations CDI ? {#how-do-i-update-my-email-alert-preferences-for-cdi-integrations}

Chaque intégration possède ses propres préférences de notification. Accédez à la page CDI et sélectionnez le nom de l'intégration que vous souhaitez mettre à jour. Dans la section **Notification preferences**, vous pouvez modifier la façon dont vous recevez les alertes concernant l'intégration sélectionnée.

## Pourquoi l'erreur « Incorrect Integration Object » s'affiche-t-elle ? {#why-am-i-seeing-an-incorrect-integration-object-error}

Cette erreur se produit lorsque vous essayez de mettre à jour les préférences de notification d'une intégration CDI et que deux espaces de travail ou plus possèdent des intégrations pointant vers le même compartiment ou dossier de stockage cloud. Chaque emplacement de stockage cloud ne peut être utilisé que par une seule intégration à la fois.

Pour résoudre ce problème :

1. Identifiez quel autre espace de travail possède une intégration CDI utilisant le même emplacement de stockage.
2. Supprimez ou reconfigurez l'intégration en conflit dans l'autre espace de travail.
3. Une fois le conflit résolu, vous pouvez mettre à jour les préférences de notification.

L'erreur ne devrait plus apparaître et vous devriez pouvoir mettre à jour vos préférences de notification avec succès. Si vous rencontrez toujours des problèmes, [ouvrez un ticket d'assistance]({{site.baseurl}}/user_guide/administer/personal/braze_support).

## Que se passe-t-il si un UPDATED_AT futur est synchronisé avec une intégration ? {#what-happens-if-a-future-updated_at-gets-synced-with-an-integration}

CDI utilise `UPDATED_AT` pour déterminer quelles données sont nouvelles. Après la synchronisation d'un `UPDATED_AT` futur, toutes les données antérieures à cette date et heure futures ne seront pas traitées. Pour corriger cela :

1. Corrigez `UPDATED_AT`.
2. Supprimez toutes les anciennes données déjà synchronisées avec Braze.
3. Créez une nouvelle intégration pour traiter à nouveau cette table.

## Pourquoi le nombre de « Rows Synced » ne correspond-il pas au nombre dans mon entrepôt de données ? {#why-doesnt-rows-synced-match-the-number-in-my-warehouse}

CDI utilise `UPDATED_AT` pour déterminer quels enregistrements récupérer lors d'une synchronisation. Consultez [cette illustration]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion#how-it-works) pour comprendre le fonctionnement. Au début d'une exécution de synchronisation, CDI interroge votre entrepôt de données pour obtenir tous les enregistrements dont la valeur `UPDATED_AT` est postérieure à la dernière valeur `UPDATED_AT` traitée. Les enregistrements situés exactement à l'horodatage limite peuvent également être re-synchronisés si de nouvelles lignes partagent cet horodatage. Tout enregistrement récupéré au moment de l'exécution de la requête est synchronisé dans Braze. Voici les cas courants où un enregistrement pourrait ne pas être synchronisé :

- Vous ajoutez des enregistrements à la table avec une valeur `UPDATED_AT` qui a déjà été traitée.
- Vous mettez à jour les valeurs des enregistrements après leur traitement par une synchronisation, mais vous laissez `UPDATED_AT` inchangé.
- Vous ajoutez ou mettez à jour des enregistrements pendant qu'une synchronisation est en cours. Selon le moment où la requête CDI s'exécute, des conditions de concurrence peuvent empêcher certains enregistrements d'être récupérés.

{% alert tip %}
Pour éviter ces comportements à l'avenir, nous recommandons d'utiliser des valeurs `UPDATED_AT` croissantes de manière monotone et de ne pas mettre à jour la table pendant l'exécution de votre synchronisation planifiée.
{% endalert %}

## Ai-je besoin de valeurs `UPDATED_AT` majoritairement distinctes pour les importations CDI volumineuses ? {#do-i-need-mostly-distinct-updated_at-values-for-large-cdi-imports}

Oui. Pour les exécutions à haut volume (par exemple, plus d'environ 10 millions de lignes), assurez-vous que vos données sources possèdent des valeurs `UPDATED_AT` majoritairement distinctes. Si trop de lignes partagent le même horodatage, le CDI a plus de chances de resélectionner des lignes aux horodatages limites lors des exécutions suivantes. Cela peut augmenter les synchronisations en double et la consommation de points de donnée.

Pour plus d'informations sur le comportement aux limites du CDI, consultez [Éviter la resynchronisation de lignes avec des horodatages en double]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/best_practices#avoid-resyncing-rows-with-duplicate-timestamps).

### Où exécuter ces vérifications SQL ? {#where-do-i-run-these-sql-checks}

Exécutez les vérifications directement dans l'éditeur SQL de votre entrepôt de données, sur la même table ou vue utilisée par votre intégration CDI :

- Snowflake : **Projects** > **Worksheets** (pour plus d'informations, consultez [Snowflake Worksheets](https://docs.snowflake.com/en/user-guide/ui-snowsight-worksheets-gs))
- Redshift : Query Editor v2 (pour plus d'informations, consultez [Using Amazon Redshift Query Editor v2](https://docs.aws.amazon.com/redshift/latest/mgmt/query-editor-v2.html))
- BigQuery : BigQuery Studio SQL workspace (pour plus d'informations, consultez [BigQuery Studio introduction](https://cloud.google.com/bigquery/docs/bigquery-studio-introduction))
- Databricks : éditeur SQL (SQL warehouse) (pour plus d'informations, consultez [Databricks SQL editor](https://docs.databricks.com/en/sql/user/sql-editor/))
- Fabric : éditeur de requêtes SQL

Suivez ce processus avant d'activer ou de mettre à l'échelle une synchronisation volumineuse :

1. Identifiez la table ou vue source CDI exacte ainsi que la fenêtre de synchronisation que vous souhaitez valider.
2. Ouvrez l'éditeur SQL de votre entrepôt et sélectionnez la même base de données et le même schéma utilisés par le CDI, puis utilisez un rôle disposant d'un accès en lecture à la table ou vue source.
3. Exécutez la requête de comptage des horodatages distincts pour mesurer le nombre de valeurs `UPDATED_AT` distinctes dans cette fenêtre.
4. Exécutez la requête qui regroupe par `UPDATED_AT` et compte les lignes pour identifier les horodatages présentant un nombre de lignes inhabituellement élevé.
5. Si de nombreuses lignes partagent des horodatages identiques, ajustez votre processus d'ingestion afin que les lots consécutifs utilisent des valeurs `UPDATED_AT` progressivement plus récentes, ou augmentez la précision des horodatages pour une meilleure répartition des lignes.
6. Réexécutez les deux requêtes jusqu'à ce que la concentration soit réduite, puis lancez ou mettez à l'échelle votre synchronisation.
7. Après le lancement, surveillez **CDI** > **Sync Log** pour détecter un volume de resynchronisation inattendu aux horodatages limites.

Utilisez des vérifications comme celles-ci dans votre entrepôt :

```sql
SELECT
  COUNT(*) AS total_rows,
  COUNT(DISTINCT UPDATED_AT) AS distinct_timestamps,
  ROUND(COUNT(*) * 1.0 / NULLIF(COUNT(DISTINCT UPDATED_AT), 0), 2) AS avg_rows_per_timestamp
FROM YOUR_CDI_SOURCE_TABLE
WHERE UPDATED_AT >= CAST('2026-04-01 00:00:00' AS TIMESTAMP)
  AND UPDATED_AT < CAST('2026-04-02 00:00:00' AS TIMESTAMP);
```

```sql
SELECT
  UPDATED_AT,
  COUNT(*) AS rows_at_timestamp
FROM YOUR_CDI_SOURCE_TABLE
WHERE UPDATED_AT >= CAST('2026-04-01 00:00:00' AS TIMESTAMP)
  AND UPDATED_AT < CAST('2026-04-02 00:00:00' AS TIMESTAMP)
GROUP BY UPDATED_AT
ORDER BY rows_at_timestamp DESC
LIMIT 20;
```

Si votre entrepôt ne prend pas en charge `LIMIT` (par exemple, Fabric), utilisez une syntaxe équivalente telle que `TOP`.

## Pourquoi une synchronisation CDI avec un petit nombre de lignes peut-elle prendre plusieurs minutes ? {#why-can-a-cdi-sync-with-a-small-number-of-rows-still-take-several-minutes}

Une synchronisation CDI comprend une période de démarrage fixe avant que le traitement des lignes ne commence. Comme ce temps de démarrage est similaire quelle que soit la taille de la synchronisation, une petite synchronisation peut tout de même prendre plusieurs minutes et paraître plus lente en nombre de lignes par minute. Le temps total de synchronisation dépend toujours de la complexité de votre requête source, de la forme des données et de la capacité disponible dans votre entrepôt de données. Pour en savoir plus, consultez [Intégrations d'entrepôt de données]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations).

## Lors d'une synchronisation, l'ordre est-il préservé si plusieurs enregistrements partagent le même ID ? {#during-a-sync-is-the-order-preserved-if-multiple-records-share-the-same-id}

L'ordre de traitement n'est pas prévisible à 100 %. Par exemple, si plusieurs lignes possèdent le même `EXTERNAL_ID` dans la table lors d'une synchronisation, il n'est pas possible de garantir quelle valeur sera retenue dans le profil final. Si vous mettez à jour le même `EXTERNAL_ID` avec différents attributs dans la colonne payload, toutes les modifications sont reflétées une fois la synchronisation terminée.

## Pourquoi de nouveaux utilisateurs ne sont-ils pas créés à partir de ma synchronisation CDI ? {#why-are-new-users-not-being-created-from-my-cdi-sync}

Si votre intégration CDI a l'option **Update existing users only** activée, seuls les utilisateurs qui existent déjà dans Braze sont mis à jour, et aucun nouvel utilisateur n'est créé. Cela signifie que si une ligne de votre table de synchronisation fait référence à un `EXTERNAL_ID` qui ne correspond à aucun utilisateur Braze existant, cette ligne est ignorée.

Pour créer de nouveaux utilisateurs via CDI, désactivez le basculement **Update existing users only** dans les paramètres de votre intégration. Accédez à **Data Settings** > **Cloud Data Ingestion** et sélectionnez une intégration.

## Quelles sont les mesures de sécurité pour l'ingestion de données cloud (CDI) ? {#what-are-the-security-measures-for-cdi}

### Nos mesures {#our-measures}

Braze a mis en place les mesures suivantes pour l'ingestion de données cloud :

- Tous les identifiants sont chiffrés dans notre base de données, et seuls certains employés disposent d'un accès authentifié.
- Nous utilisons des connexions chiffrées pour transférer les données vers les entrepôts de données des clients.
- Nous effectuons des requêtes vers les endpoints de l'API Braze en utilisant les mêmes clés API et connexions TLS que celles que nous recommandons à nos clients.
- Nous mettons régulièrement à jour nos bibliothèques et appliquons les correctifs de sécurité.

### Vos mesures {#your-measures}

Nous vous recommandons, à vous et à votre équipe, de mettre en place les mesures de sécurité suivantes de votre côté :

- Restreignez l'accès aux identifiants au minimum requis pour le fonctionnement de l'ingestion de données cloud. En effet, nous devons pouvoir exécuter des requêtes de sélection (et de comptage) sur les tables et vues spécifiques.
- Restreignez les adresses IP pouvant accéder aux tables aux [adresses IP Braze]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations#step-1-set-up-tables-or-views) officiellement publiées.