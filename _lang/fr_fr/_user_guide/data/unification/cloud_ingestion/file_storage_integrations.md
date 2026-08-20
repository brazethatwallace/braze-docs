---
nav_title: Intégrations de stockage de fichiers
article_title: Intégrations de stockage de fichiers
description: "Cette page traite de l'ingestion de données cloud de Braze et de la synchronisation des données pertinentes d'Amazon S3 vers Braze."
page_order: 4
page_type: reference

---

# Intégrations de stockage de fichiers {#file-storage-integrations}

> Cette page explique comment configurer la prise en charge de l'ingestion de données cloud et synchroniser les données pertinentes d'Amazon S3 vers Braze.

## Fonctionnement {#how-it-works}

Vous pouvez utiliser l'ingestion de données cloud (CDI) pour S3 afin d'intégrer directement un ou plusieurs compartiments S3 de votre compte AWS avec Braze. Lorsque de nouveaux fichiers sont publiés sur S3, un message est envoyé à SQS, et l'ingestion de données cloud de Braze prend en charge ces nouveaux fichiers.

L'ingestion de données cloud prend en charge les éléments suivants :

- Fichiers JSON
- Fichiers CSV
- Fichiers Parquet
- Données d'attributs, d'événements personnalisés, d'événements d'achat, de suppression d'utilisateurs et de catalogue

## Prérequis {#prerequisites}

L'intégration nécessite les ressources suivantes :

 - Un compartiment S3 pour le stockage des données
 - Une file d'attente SQS pour les notifications de nouveaux fichiers
 - Un rôle IAM pour l'accès à Braze

### Définitions AWS {#aws-definitions}

Commencez par définir les termes utilisés au cours de cette tâche.

| Terme | Définition |
| --- | --- |
| Amazon Resource Name (ARN) | L'ARN est un identifiant unique pour les ressources AWS. |
| Identity and Access Management (IAM) | IAM est un service web qui vous permet de contrôler de manière sécurisée l'accès aux ressources AWS. Dans ce tutoriel, vous allez créer une politique IAM et l'attribuer à un rôle IAM pour intégrer votre compartiment S3 avec l'ingestion de données cloud de Braze. |
| Amazon Simple Queue Service (SQS) | SQS est une file d'attente hébergée qui vous permet d'intégrer des systèmes logiciels distribués et des composants. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Définitions AWS" }

## Configuration de Cloud Data Ingestion dans AWS {#setting-up-cloud-data-ingestion-in-aws}

### Étape 1 : Créer un compartiment source {#step-1-create-a-source-bucket}

Créez un compartiment S3 à usage général avec les paramètres par défaut dans votre compte AWS. Les compartiments S3 peuvent être réutilisés entre les synchronisations tant que le dossier est unique.

Les paramètres par défaut sont :

- ACL désactivées
- Bloquer tout accès public
- Désactiver le versionnement du compartiment
- Chiffrement SSE-S3
  - SSE-S3 est le seul type de chiffrement côté serveur pris en charge. Le chiffrement Amazon KMS n'est pas pris en charge.

Notez la région dans laquelle vous avez créé le compartiment — vous créerez une file d'attente SQS dans la même région à l'étape suivante.

### Étape 2 : Créer une file d'attente SQS {#step-2-create-sqs-queue}

Créez une file d'attente SQS pour suivre l'ajout d'objets dans le compartiment que vous avez créé. Utilisez les paramètres de configuration par défaut pour le moment.

Une file d'attente SQS doit être unique au niveau mondial (par exemple, une seule peut être utilisée pour une synchronisation CDI et ne peut pas être réutilisée dans un autre espace de travail).

{% alert important %}
Veillez à créer cette file SQS dans la même région que celle dans laquelle vous avez créé le compartiment.
{% endalert %}

Notez l'ARN et l'URL de la file d'attente SQS — vous en aurez fréquemment besoin au cours de cette configuration.

![Sélection de « Advanced » avec un exemple d'objet JSON pour définir qui peut accéder à une file d'attente.]({% image_buster /assets/img/cloud_ingestion/s3_ARN.png %})

### Étape 3 : Configurer la politique d'accès {#step-3-set-up-access-policy}

Pour configurer la politique d'accès, choisissez **Advanced options**.

Ajoutez l'instruction suivante à la politique d'accès de la file d'attente, en prenant soin de remplacer `YOUR-BUCKET-NAME-HERE` par le nom de votre compartiment, `YOUR-SQS-ARN` par l'ARN de votre file d'attente SQS, et `YOUR-AWS-ACCOUNT-ID` par l'ID de votre compte AWS :

``` json
{
  "Sid": "braze-cdi-s3-sqs-publish",
  "Effect": "Allow",
  "Principal": {
    "Service": "s3.amazonaws.com"
  },
  "Action": "SQS:SendMessage",
  "Resource": "YOUR-SQS-ARN",
  "Condition": {
    "StringEquals": {
      "aws:SourceAccount": "YOUR-AWS-ACCOUNT-ID"
    },
    "ArnLike": {
      "aws:SourceArn": "arn:aws:s3:::YOUR-BUCKET-NAME-HERE"
    }
  }
}
```

### Étape 4 : Ajouter une notification d'événement au compartiment S3 {#step-4-add-an-event-notification-to-the-s3-bucket}

1. Dans le compartiment créé à l'étape 1, accédez à **Properties** > **Event notifications**.
2. Donnez un nom à la configuration. Vous pouvez éventuellement spécifier un préfixe ou un suffixe pour cibler uniquement un sous-ensemble de fichiers à ingérer par Braze.
3. Sous **Destination**, sélectionnez **SQS queue** et fournissez l'ARN de la file SQS que vous avez créée à l'étape 2.

{% alert note %}
Si vous chargez vos fichiers dans le dossier racine d'un compartiment S3 puis déplacez certains fichiers vers un dossier spécifique dans le compartiment, vous pourriez rencontrer une erreur inattendue. À la place, vous pouvez modifier les notifications d'événement pour n'envoyer que les fichiers correspondant au préfixe, éviter de placer des fichiers dans le compartiment S3 en dehors de ce préfixe, ou mettre à jour l'intégration sans préfixe, ce qui ingère alors tous les fichiers.
{% endalert %}

### Étape 5 : Créer une politique IAM {#step-5-create-an-iam-policy}

Créez une politique IAM pour permettre à Braze d'interagir avec votre compartiment source. Pour commencer, connectez-vous à la console de gestion AWS en tant qu'administrateur de compte.

1. Accédez à la section IAM de la console AWS, sélectionnez **Policies** dans la barre de navigation, puis sélectionnez **Create Policy**.<br><br>![Le bouton « Create policy » dans la console AWS.]({% image_buster /assets/img/create_policy_1_list.png %})<br><br>

2. Ouvrez l'onglet **JSON** et saisissez l'extrait de code suivant dans la section **Policy Document**, en prenant soin de remplacer `YOUR-BUCKET-NAME-HERE` par le nom de votre compartiment, et `YOUR-SQS-ARN-HERE` par le nom de votre file d'attente SQS :

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["s3:ListBucket", "s3:GetObjectAttributes", "s3:GetObject"],
            "Resource": ["arn:aws:s3:::YOUR-BUCKET-NAME-HERE"]
        },
        {
            "Effect": "Allow",
            "Action": ["s3:ListBucket", "s3:GetObjectAttributes", "s3:GetObject"],
            "Resource": ["arn:aws:s3:::YOUR-BUCKET-NAME-HERE/*"]
        },
        {
            "Effect": "Allow",
            "Action": [
                "sqs:DeleteMessage",
                "sqs:GetQueueUrl",
                "sqs:ReceiveMessage",
                "sqs:GetQueueAttributes"
            ],
            "Resource": "YOUR-SQS-ARN-HERE"
        }
    ]
}

```

{: start="3"}
3. Sélectionnez **Review Policy** lorsque vous avez terminé.

4. Donnez un nom et une description à la politique, puis sélectionnez **Create Policy**.

![Un exemple de politique nommée « new-policy-name ».]({% image_buster /assets/img/create_policy_3_name.png %})

![Le champ de description de la politique.]({% image_buster /assets/img/create_policy_4_created.png %})

### Étape 6 : Créer un rôle IAM {#step-6-create-an-iam-role}

Pour terminer la configuration sur AWS, créez un rôle IAM et attachez-y la politique IAM de l'étape 5.

1. Dans la même section IAM de la console où vous avez créé la politique IAM, accédez à **Roles** > **Create Role**.

![Le bouton « Create role ».]({% image_buster /assets/img/create_role_1_list.png %})

{: start="2"}
2. Dans AWS, sélectionnez **Another AWS Account** comme type d'entité de confiance. Fournissez l'ID de votre compte Braze. Cochez la case **Require external ID**.
3. Dans Braze, accédez à **Data Settings** > **Cloud Data Ingestion** > **Sources**, sélectionnez **Add data source**, puis sélectionnez **Amazon S3** dans la section des sources de fichiers.
4. Copiez l'**ID de compte Braze** généré automatiquement.

![La page « Add New Source » affichant les sections Source Name et S3 Connection Details.]({% image_buster /assets/img/braze_account_id.png %})

{: start="6"}
5. Dans AWS, collez l'ID de compte, puis sélectionnez **Next**.

![La page S3 « Create Role ». Cette page contient des champs pour le nom du rôle, la description du rôle, les entités de confiance, les politiques et la limite de permissions.]({% image_buster /assets/img/create_role_2_another.png %})<br><br>

{: start="7"}
6. Attachez la politique créée à l'étape 4 au rôle. Recherchez la politique dans la barre de recherche et cochez la case à côté de la politique pour l'attacher. Sélectionnez **Next** lorsque vous avez terminé.

![ARN du rôle avec la politique new-policy-name sélectionnée.]({% image_buster /assets/img/create_role_3_attach.png %})

Donnez un nom et une description au rôle, puis sélectionnez **Create Role**.

![Un exemple de rôle nommé « new-role-name ».]({% image_buster /assets/img/create_role_4_name.png %})

{: start="8"}
7. Notez l'ARN du rôle que vous avez créé et l'ID externe que vous avez généré, car vous en aurez besoin pour créer l'intégration Cloud Data Ingestion.

## Configuration de l'ingestion de données cloud dans Braze {#setting-up-cloud-data-ingestion-in-braze}

1. Commencez par créer une nouvelle source dans le tableau de bord de Braze. Accédez à **Data Settings** > **Cloud Data Ingestion** > **Sources**, sélectionnez **Add data source**, puis sélectionnez **Amazon S3**.
2. Choisissez un nom pour votre source et saisissez les informations issues du processus de configuration AWS pour créer une nouvelle source. Spécifiez les éléments suivants :

  - Role ARN
  - ID externe
  - Nom du compartiment
  - Région

![La section des détails de connexion S3 affichant les identifiants (configuration AWS et configuration Braze) et les champs de configuration.]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_1.png %})

{: start="3"}
3. Sélectionnez **Test connection** pour confirmer que Braze peut accéder à votre compartiment. Après un test réussi, sélectionnez **Connect to Source**. Si la connexion échoue, un message d'erreur s'affiche pour vous aider à résoudre le problème.

{: start="4"}
4. Ensuite, créez une nouvelle synchronisation. Accédez à **Data Settings** > **Cloud Data Ingestion** > **Syncs** et sélectionnez **Create data sync**.

{: start="5"}
5. Choisissez un nom pour votre synchronisation. Sélectionnez ensuite une source S3 active et saisissez votre table source pour la synchronisation. Sélectionnez un type de données et sélectionnez **Test Connection**.

![Une option pour tester la connexion avec un aperçu des données.]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_4.png %})

6. Saisissez les informations restantes issues du processus de configuration AWS. Spécifiez les éléments suivants :
- URL SQS (doit être unique pour chaque nouvelle intégration)
- Chemin du dossier (facultatif, doit être unique parmi les synchronisations d'un espace de travail)

7. Sélectionnez un type de données et sélectionnez **Test Connection** pour confirmer que Braze peut lister les fichiers disponibles à ingérer (pas les données contenues dans ces fichiers). Une fois le test réussi, sélectionnez **Next: Notifications**.
8. Ajoutez une ou plusieurs adresses e-mail de contact pour les notifications en cas de rupture de la synchronisation due à des problèmes d'accès ou de permissions. Vous pouvez également activer les notifications pour les erreurs au niveau utilisateur et les synchronisations réussies.
9. Créez la synchronisation.

## Formats de fichiers requis {#required-file-formats}

L'ingestion de données cloud prend en charge les fichiers JSON, CSV et Parquet. Les colonnes requises dépendent du type de données :

- Les données utilisateur (attributs, événements personnalisés, événements d'achat) utilisent des identifiants utilisateur et un payload
- Les données de catalogue utilisent des identifiants de catalogue

Si vous utilisez S3 pour les données de catalogue, consultez cette page ainsi que [Synchroniser et supprimer des données de catalogue]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data) pour les exigences et comportements spécifiques aux catalogues.

Braze n'impose aucune exigence supplémentaire concernant les noms de fichiers au-delà de ce qu'AWS impose. Les noms de fichiers doivent être uniques. L'ajout d'un horodatage permet de garantir cette unicité.

Pour des exemples de tous les types de fichiers pris en charge (attributs, événements personnalisés, achats, catalogues et suppressions d'utilisateurs), consultez les fichiers d'exemple dans [braze-examples](https://github.com/braze-inc/braze-examples/tree/main/cloud-data-ingestion/braze-examples/payloads/file_storage).

### Identifiants utilisateur {#user-identifiers}

Pour les synchronisations de données utilisateur (attributs, événements personnalisés, événements d'achat), chaque ligne de votre fichier source nécessite exactement un identifiant utilisateur et une colonne `payload`. Un fichier source peut contenir des lignes avec différents types d'identifiants, mais chaque ligne individuelle ne doit en utiliser qu'un seul.

| Identifiant | Description |
| --- | --- |
| `EXTERNAL_ID` | Identifie l'utilisateur que vous souhaitez mettre à jour. Doit correspondre à la valeur `external_id` utilisée dans Braze. |
| `ALIAS_NAME` et `ALIAS_LABEL` | Ces deux colonnes créent un objet alias d'utilisateur. `alias_name` doit être un identifiant unique, et `alias_label` spécifie le type d'alias. Les utilisateurs peuvent avoir plusieurs alias avec des libellés différents, mais un seul `alias_name` par `alias_label`. |
| `BRAZE_ID` | L'identifiant utilisateur Braze. Il est généré par le SDK Braze, et de nouveaux utilisateurs ne peuvent pas être créés à l'aide d'un Braze ID via l'ingestion de données cloud. Pour créer de nouveaux utilisateurs, spécifiez un ID externe ou un alias d'utilisateur. |
| `EMAIL` | L'adresse e-mail de l'utilisateur. Si plusieurs profils avec la même adresse e-mail existent, le profil mis à jour le plus récemment est prioritaire pour les mises à jour. Si vous incluez à la fois l'e-mail et le téléphone, Braze utilise l'e-mail comme identifiant principal. |
| `PHONE` | Le numéro de téléphone de l'utilisateur. Si plusieurs profils avec le même numéro de téléphone existent, le profil mis à jour le plus récemment est prioritaire pour les mises à jour. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Identifiants utilisateur" }

En plus d'un identifiant, chaque ligne doit inclure une colonne `payload` contenant une chaîne JSON des champs que vous souhaitez synchroniser vers l'utilisateur dans Braze.

{% alert note %}
Contrairement aux sources d'entrepôt de données, la colonne `UPDATED_AT` n'est ni requise ni prise en charge pour les synchronisations de stockage de fichiers.
{% endalert %}

### Identifiants de catalogue {#catalog-identifiers}

Pour les synchronisations de catalogue, votre fichier source doit contenir les colonnes suivantes. Les fichiers de catalogue utilisent des identifiants différents de ceux des fichiers de données utilisateur.

| Colonne | Obligatoire | Description |
| --- | --- | --- |
| `ID` | Oui | L'identifiant unique de l'élément de catalogue. Utilisé pour créer, mettre à jour ou supprimer l'élément dans Braze. |
| `payload` | Oui | Une chaîne JSON des champs et valeurs du catalogue à synchroniser. Doit correspondre au schéma de votre catalogue dans Braze. |
| `DELETED` | Non | Lorsque la valeur est `true`, l'élément de catalogue avec l'`ID` correspondant est supprimé du catalogue dans Braze. Omettez cette colonne ou définissez-la sur `false` pour les opérations de création ou de mise à jour. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Identifiants de catalogue" }

### Exemples {#examples}

{% tabs %}
{% tab JSON Attributes %}
``` json
{"external_id":"s3-qa-0","payload":"{\"name\": \"GT896\", \"age\": 74, \"subscriber\": true, \"retention\": {\"previous_purchases\": 21, \"vip\": false}, \"last_visit\": \"2023-08-08T16:03:26.600803\"}"}
{"external_id":"s3-qa-1","payload":"{\"name\": \"HSCJC\", \"age\": 86, \"subscriber\": false, \"retention\": {\"previous_purchases\": 0, \"vip\": false}, \"last_visit\": \"2023-08-08T16:03:26.600824\"}"}
{"external_id":"s3-qa-2","payload":"{\"name\": \"YTMQZ\", \"age\": 43, \"subscriber\": false, \"retention\": {\"previous_purchases\": 23, \"vip\": true}, \"last_visit\": \"2023-08-08T16:03:26.600831\"}"}
{"external_id":"s3-qa-3","payload":"{\"name\": \"5P44M\", \"age\": 15, \"subscriber\": true, \"retention\": {\"previous_purchases\": 7, \"vip\": true}, \"last_visit\": \"2023-08-08T16:03:26.600838\"}"}
{"external_id":"s3-qa-4","payload":"{\"name\": \"WMYS7\", \"age\": 11, \"subscriber\": true, \"retention\": {\"previous_purchases\": 0, \"vip\": false}, \"last_visit\": \"2023-08-08T16:03:26.600844\"}"}
{"external_id":"s3-qa-5","payload":"{\"name\": \"KCBLK\", \"age\": 47, \"subscriber\": true, \"retention\": {\"previous_purchases\": 11, \"vip\": true}, \"last_visit\": \"2023-08-08T16:03:26.600850\"}"}
{"external_id":"s3-qa-6","payload":"{\"name\": \"T93MJ\", \"age\": 47, \"subscriber\": true, \"retention\": {\"previous_purchases\": 10, \"vip\": false}, \"last_visit\": \"2023-08-08T16:03:26.600856\"}"}
```
{% alert important %}
Chaque ligne de votre fichier source doit contenir du JSON valide, sinon le fichier sera ignoré.
{% endalert %}
{% endtab %}
{% tab JSON Custom Events %}
``` json
{"external_id":"s3-qa-0","payload":"{\"app_id\": \"YOUR_APP_ID\", \"name\": \"view-206\", \"time\": \"2024-04-02T14:34:08\", \"properties\": {\"bool_value\": false, \"preceding_event\": \"unsubscribe\", \"important_number\": 206}}"}
{"external_id":"s3-qa-1","payload":"{\"app_id\": \"YOUR_APP_ID\", \"name\": \"view-206\", \"time\": \"2024-04-02T14:34:08\", \"properties\": {\"bool_value\": false, \"preceding_event\": \"unsubscribe\", \"important_number\": 206}}"}
```
{% alert important %}
Chaque ligne de votre fichier source doit contenir du JSON valide, sinon le fichier sera ignoré.
{% endalert %}
{% endtab %}
{% tab JSON Purchase Events %}
``` json
{"external_id":"s3-qa-0","payload":"{\"app_id\": \"YOUR_APP_ID\", \"product_id\": \"product-11\", \"currency\": \"BSD\", \"price\": 8.511527858335066, \"time\": \"2024-04-02T14:34:08\", \"quantity\": 19, \"properties\": {\"is_a_boolean\": true, \"important_number\": 40, \"preceding_event\": \"click\"}}"}
{"external_id":"s3-qa-1","payload":"{\"app_id\": \"YOUR_APP_ID\", \"product_id\": \"product-11\", \"currency\": \"BSD\", \"price\": 8.511527858335066, \"time\": \"2024-04-02T14:34:08\", \"quantity\": 19, \"properties\": {\"is_a_boolean\": true, \"important_number\": 40, \"preceding_event\": \"click\"}}"}
```
{% alert important %}
Chaque ligne de votre fichier source doit contenir du JSON valide, sinon le fichier sera ignoré.
{% endalert %}

{% endtab %}
{% tab CSV Attributes %}
```plaintext
external_id,payload
s3-qa-load-0-d0daa196-cdf5-4a69-84ae-4797303aee75,"{""name"": ""SNXIM"", ""age"": 54, ""subscriber"": true, ""retention"": {""previous_purchases"": 19, ""vip"": true}, ""last_visit"": ""2023-08-08T16:03:26.598806""}"
s3-qa-load-1-d0daa196-cdf5-4a69-84ae-4797303aee75,"{""name"": ""0J747"", ""age"": 73, ""subscriber"": false, ""retention"": {""previous_purchases"": 22, ""vip"": false}, ""last_visit"": ""2023-08-08T16:03:26.598816""}"
s3-qa-load-2-d0daa196-cdf5-4a69-84ae-4797303aee75,"{""name"": ""EP1U0"", ""age"": 99, ""subscriber"": false, ""retention"": {""previous_purchases"": 23, ""vip"": false}, ""last_visit"": ""2023-08-08T16:03:26.598822""}"
```
{% endtab %}
{% tab CSV Catalogs  %}
```plaintext
ID,PAYLOAD,DELETED
85,"{""product_name"": ""Product 85"", ""price"": 85.85}",false
1,"{""product_name"": ""Product 1"", ""price"": 1.01}",true
```
Incluez une colonne `DELETED` facultative. Lorsque `DELETED` est `true`, cet élément de catalogue est supprimé du catalogue dans Braze. Pour la liste complète des colonnes requises, consultez [Identifiants de catalogue](#catalog-identifiers). Pour le comportement de suppression, consultez [Suppression d'éléments de catalogue](#deleting-catalog-items). Pour un flux de configuration de catalogue de bout en bout (y compris la création du catalogue cible et le comportement de synchronisation), consultez [Synchroniser et supprimer des données de catalogue]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data).
{% endtab %}

{% endtabs %}

## Suppression de données {#deleting-data}

L'ingestion de données cloud pour S3 prend en charge la suppression d'utilisateurs et d'éléments de catalogue via le téléversement de fichiers. Utilisez des synchronisations et des formats de fichiers distincts pour chaque type.

- **[Suppression d'utilisateurs](#deleting-users)** – Créez une synchronisation avec le type de données **Delete Users** et téléversez des fichiers contenant uniquement des identifiants utilisateur (sans payload).
- **[Suppression d'éléments de catalogue](#deleting-catalog-items)** – Utilisez votre synchronisation de catalogue existante et ajoutez une colonne `deleted` (ou `DELETED`) pour marquer les éléments à supprimer.

### Suppression d'utilisateurs {#deleting-users}

Pour supprimer des profils utilisateur dans Braze à l'aide de fichiers dans S3 :

1. Créez une nouvelle synchronisation d'ingestion de données cloud (même [configuration AWS et Braze](#setting-up-cloud-data-ingestion-in-aws) que pour les autres synchronisations).
2. Lors de la configuration de la synchronisation dans Braze, définissez **Data Type** sur **Delete Users**.
3. Téléversez dans votre compartiment S3 des fichiers contenant uniquement les colonnes d'identifiants utilisateur. N'incluez pas de colonne `payload` — la synchronisation échoue si un payload est présent, afin d'éviter les suppressions accidentelles.

Chaque ligne du fichier doit identifier exactement un utilisateur à l'aide de l'un des éléments suivants :

| Identifiant | Description |
| --- | --- |
| `EXTERNAL_ID` | Correspond à l'`external_id` utilisé dans Braze. |
| `ALIAS_NAME` et `ALIAS_LABEL` | Les deux colonnes ensemble identifient l'utilisateur par alias. |
| `BRAZE_ID` | ID utilisateur généré par Braze (utilisateurs existants uniquement). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Suppression d'utilisateurs" }

{% alert important %}
La suppression d'utilisateurs est permanente et ne peut pas être annulée. N'incluez que les utilisateurs que vous avez l'intention de supprimer. Pour plus de détails, consultez [Supprimer des utilisateurs avec l'ingestion de données cloud]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/delete_users).
{% endalert %}

**Exemple – JSON (suppression d'utilisateurs) :**
```jsonl
{"external_id":"user-to-delete-001"}
{"external_id":"user-to-delete-002"}
{"braze_id":"braze-id-from-profile"}
```

**Exemple – CSV (suppression d'utilisateurs) :**
```plaintext
external_id
user-to-delete-001
user-to-delete-002
```

Lorsque la synchronisation s'exécute, Braze traite les nouveaux fichiers dans le compartiment et supprime les profils utilisateur correspondants.

### Suppression d'éléments de catalogue {#deleting-catalog-items}

Pour supprimer des éléments d'un catalogue à l'aide du stockage de fichiers :

1. Utilisez la même synchronisation S3 que celle utilisée pour [synchroniser les données de catalogue]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data) (type de données **Catalogs**).
2. Dans vos fichiers CSV ou JSON, ajoutez une colonne optionnelle **`deleted`** (ou **`DELETED`**).
3. Définissez `deleted` sur `true` pour tout élément de catalogue que vous souhaitez supprimer du catalogue dans Braze.

Chaque ligne nécessite toujours `ID` et `payload`. Pour les lignes marquées pour suppression, le payload peut être minimal ; Braze supprime l'élément par `ID`.

**Exemple – JSON (suppression d'élément de catalogue) :**
```jsonl
{"id":"85","payload":"{\"product_name\": \"Product 85\", \"price\": 85.85}"}
{"id":"1","payload":"{\"product_name\": \"Product 1\", \"price\": 1.01}","deleted":true}
```

**Exemple – CSV (suppression d'élément de catalogue) :**
```plaintext
ID,PAYLOAD,DELETED
85,"{""product_name"": ""Product 85"", ""price"": 85.85}",false
1,"{""product_name"": ""Product 1"", ""price"": 1.01}",true
```

Lorsque la synchronisation s'exécute, les lignes avec `deleted: true` entraînent la suppression de l'élément de catalogue correspondant dans Braze. Pour en savoir plus sur le comportement de synchronisation et de suppression de catalogue, consultez [Synchroniser et supprimer des données de catalogue]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data).

## Points importants {#things-to-know}

- Les fichiers ajoutés au compartiment S3 source ne doivent pas dépasser 512&nbsp;Mo. Les fichiers de plus de 512&nbsp;Mo génèrent une erreur et ne sont pas synchronisés avec Braze.
- Bien qu'il n'y ait pas de limite supplémentaire sur le nombre de lignes par fichier, nous recommandons d'utiliser des fichiers plus petits pour améliorer la vitesse d'exécution de vos synchronisations. Par exemple, l'ingestion d'un fichier de 500&nbsp;Mo prendrait considérablement plus de temps que celle de cinq fichiers distincts de 100&nbsp;Mo.
- Il n'y a pas de limite supplémentaire sur le nombre de fichiers téléversés dans un laps de temps donné.
- L'ordonnancement n'est pas pris en charge au sein des fichiers ni entre eux. Nous recommandons de regrouper les mises à jour périodiquement si vous surveillez d'éventuelles conditions de concurrence.

## Résolution des problèmes {#troubleshooting}

### Téléchargement et traitement des fichiers {#uploading-files-and-processing}

L'ingestion de données cloud (CDI) ne traite que les fichiers ajoutés après la création de la synchronisation. Au cours de ce processus, Braze recherche les nouveaux fichiers ajoutés, ce qui déclenche un nouveau message vers SQS. Cela lance une nouvelle synchronisation pour traiter le nouveau fichier.

Vous pouvez utiliser des fichiers existants pour vérifier que Braze peut accéder à votre compartiment et détecter les fichiers à ingérer, mais ils ne sont pas synchronisés avec Braze. Pour que le CDI les traite, vous devez re-télécharger vers S3 tous les fichiers existants que vous souhaitez synchroniser.

### Gestion des erreurs de fichiers inattendues {#handling-unexpected-file-errors}

Si vous observez un nombre élevé d'erreurs ou de fichiers en échec, il est possible qu'un autre processus ajoute des fichiers au compartiment S3 dans un dossier différent du dossier cible pour le CDI.

Lorsque des fichiers sont téléchargés dans le compartiment source mais pas dans le dossier source, le CDI traite la notification SQS, mais n'effectue aucune action sur le fichier, ce qui peut apparaître comme une erreur.

Si votre problème est lié aux notifications S3 ou aux autorisations de destination SQS (par exemple, des erreurs de validation de destination), consultez la documentation AWS :

- [Activation et configuration des notifications d'événements à l'aide de la console Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/enable-event-notifications.html)
- [Octroi d'autorisations pour publier des messages de notification d'événements vers une destination](https://docs.aws.amazon.com/AmazonS3/latest/userguide/grant-destinations-permissions-to-s3.html)
- [Résolution des problèmes dans Amazon SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-troubleshooting.html)