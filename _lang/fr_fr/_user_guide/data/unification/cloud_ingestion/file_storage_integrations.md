---
nav_title: Intégrations de stockage de fichiers
article_title: Intégrations de stockage de fichiers
description: "Cette page traite de l'ingestion de données cloud de Braze et de la synchronisation des données pertinentes d'Amazon S3 ou de Google Cloud Storage vers Braze."
page_order: 4
page_type: reference

---

# Intégrations de stockage de fichiers {#file-storage-integrations}

> Cette page explique comment configurer l'ingestion de données cloud pour synchroniser les données d'Amazon S3 ou de Google Cloud Storage vers Braze.

## Fonctionnement {#how-it-works}

Vous pouvez utiliser l'ingestion de données cloud (CDI) pour intégrer directement un ou plusieurs compartiments de stockage de votre compte cloud avec Braze. Lorsque vous ajoutez un nouveau fichier à un compartiment, votre fournisseur cloud publie une notification et l'ingestion de données cloud de Braze synchronise les données.

Le mécanisme de notification dépend de votre fournisseur :

- **Amazon S3 :** Lorsque de nouveaux fichiers sont publiés sur S3, un message est envoyé à une file d'attente Amazon Simple Queue Service (SQS), et Braze consomme ce message pour ingérer le nouveau fichier.
- **Google Cloud Storage (GCS) :** Lorsque de nouveaux fichiers sont finalisés dans le compartiment, GCS publie une notification `OBJECT_FINALIZE` vers un sujet Pub/Sub. Braze consomme ces notifications à partir d'un abonnement Pub/Sub pour ingérer le nouveau fichier.

L'ingestion de données cloud prend en charge les éléments suivants :

- Fichiers JSON
- Fichiers CSV
- Fichiers Parquet
- Données d'attributs, d'événements personnalisés, d'événements d'achat, de suppression d'utilisateurs et de catalogue

## Configuration de l'ingestion de données cloud {#setting-up-cloud-data-ingestion}

Les étapes de configuration dépendent de votre fournisseur de stockage de fichiers. Sélectionnez l'onglet correspondant à votre fournisseur, puis complétez la configuration commune dans les sections qui suivent.

{% tabs %}
{% tab Amazon S3 %}

L'intégration nécessite les ressources suivantes :

- Un compartiment S3 pour le stockage des données
- Une file d'attente SQS pour les notifications de nouveaux fichiers
- Un rôle IAM pour l'accès de Braze

### Définitions AWS {#aws-definitions}

| Terme | Définition |
| --- | --- |
| Amazon Resource Name (ARN) | L'ARN est un identifiant unique pour les ressources AWS. |
| Identity and Access Management (IAM) | IAM est un service web qui vous permet de contrôler de manière sécurisée l'accès aux ressources AWS. Dans ce tutoriel, créez une politique IAM et attribuez-la à un rôle IAM pour intégrer votre compartiment S3 à l'ingestion de données cloud de Braze. |
| Amazon Simple Queue Service (SQS) | SQS est une file d'attente hébergée qui vous permet d'intégrer des systèmes logiciels et des composants distribués. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Définitions AWS" }

## Configuration de l'ingestion de données cloud dans AWS {#setting-up-cloud-data-ingestion-in-aws}

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
7. Notez l'ARN du rôle que vous avez créé et l'ID externe que vous avez généré, car vous en aurez besoin pour créer l'intégration d'ingestion de données cloud.

## Configuration de l'ingestion de données cloud dans Braze {#setting-up-cloud-data-ingestion-in-braze}

1. Commencez par créer une nouvelle source dans le tableau de bord de Braze. Accédez à **Data Settings** > **Cloud Data Ingestion** > **Sources**, sélectionnez **Add data source**, puis sélectionnez **Amazon S3**.
2. Choisissez un nom pour votre source et saisissez les informations issues du processus de configuration AWS pour créer une nouvelle source. Spécifiez les éléments suivants :

  - Role ARN
  - External ID
  - Nom du compartiment
  - Région

![La section S3 Connection Details affichant les champs Credentials (configuration AWS et configuration Braze) et Configuration.]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_1.png %})

{: start="3"}
3. Sélectionnez **Test connection** pour confirmer que Braze peut accéder à votre compartiment. Après un test réussi, sélectionnez **Connect to Source**. Si la connexion échoue, un message d'erreur s'affiche pour vous aider à résoudre le problème.

{: start="4"}
4. Ensuite, créez une nouvelle synchronisation. Accédez à **Data Settings** > **Cloud Data Ingestion** > **Syncs** et sélectionnez **Create data sync**.

{: start="5"}
5. Choisissez un nom pour votre synchronisation. Sélectionnez ensuite une source S3 active et saisissez votre table source pour la synchronisation. Sélectionnez un type de données, puis sélectionnez **Test Connection**.

![Une option pour tester la connexion avec un aperçu des données.]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_4.png %})

6. Saisissez les informations restantes issues du processus de configuration AWS. Spécifiez les éléments suivants :
- URL SQS (doit être unique pour chaque nouvelle intégration)
- Chemin du dossier (optionnel, doit être unique entre les synchronisations d'un même espace de travail)

7. Sélectionnez un type de données, puis sélectionnez **Test Connection** pour confirmer que Braze peut lister les fichiers disponibles à l'ingestion (pas les données contenues dans ces fichiers). Une fois le test réussi, sélectionnez **Next: Notifications**.
8. Ajoutez une ou plusieurs adresses e-mail de contact pour les notifications en cas de dysfonctionnement de la synchronisation dû à des problèmes d'accès ou de permissions. Vous pouvez également activer les notifications pour les erreurs au niveau utilisateur et les synchronisations réussies.
9. Créez la synchronisation.

{% endtab %}
{% tab Google Cloud Storage %}

L'intégration nécessite les ressources suivantes :

- Un compartiment Cloud Storage pour le stockage des données
- Un sujet et un abonnement Pub/Sub pour les notifications de nouveaux fichiers
- Un compte de service dont vous chargez la clé JSON dans Braze

### Définitions GCP {#gcp-definitions}

| Terme | Définition |
| --- | --- |
| Projet Google Cloud | Un projet organise toutes vos ressources Google Cloud et est identifié par un ID de projet unique et un numéro de projet. |
| Compartiment Cloud Storage | Un compartiment est le conteneur qui stocke les fichiers de données que vous souhaitez faire ingérer par Braze. |
| Sujet Pub/Sub | Un sujet est la ressource nommée qui reçoit les notifications de nouveaux fichiers depuis votre compartiment Cloud Storage. |
| Abonnement Pub/Sub | Un abonnement est rattaché à un sujet et distribue ses messages. Braze consomme les notifications de nouveaux fichiers à partir d'un abonnement de type pull. |
| Compte de service | Un compte de service est une identité non humaine que Braze utilise pour accéder à votre compartiment et à votre abonnement. Vous chargez sa clé JSON dans Braze. |
| Rôle IAM | Un rôle Identity and Access Management (IAM) est une collection de permissions que vous attribuez au compte de service sur votre compartiment et votre abonnement. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Définitions GCP" }

## Configuration de l'ingestion de données cloud dans Google Cloud {#setting-up-cloud-data-ingestion-in-google-cloud}

### Étape 1 : Créer un compartiment Cloud Storage {#step-1-create-a-cloud-storage-bucket}

Dans la console Google Cloud, accédez à **Cloud Storage** > **Buckets** > **Create**. Notez l'ID du projet et le nom du compartiment — vous en aurez besoin lors de la configuration de la source dans Braze. Nous recommandons d'activer l'accès uniforme au niveau du compartiment afin que les permissions soient gérées avec IAM.

Vous pouvez également créer le compartiment avec gcloud :

```shell
gcloud storage buckets create gs://YOUR-BUCKET-NAME \
  --project=YOUR-PROJECT-ID \
  --location=YOUR-REGION \
  --uniform-bucket-level-access
```

### Étape 2 : Créer un sujet et un abonnement Pub/Sub {#step-2-create-a-pubsub-topic-and-subscription}

Dans la console Google Cloud, accédez à **Pub/Sub** > **Topics** > **Create topic**. Vous pouvez laisser Google créer un abonnement par défaut, ou en créer un séparément. Créez ensuite un abonnement de type **pull** sur ce sujet.

Vous pouvez également utiliser gcloud :

```shell
gcloud pubsub topics create YOUR-TOPIC --project=YOUR-PROJECT-ID
gcloud pubsub subscriptions create YOUR-SUBSCRIPTION \
  --topic=YOUR-TOPIC --project=YOUR-PROJECT-ID --ack-deadline=60
```

Notez l'**ID de l'abonnement** — Braze a besoin de l'abonnement (et non du sujet) lorsque vous créez la synchronisation. L'abonnement doit être de type pull.

{% alert warning %}
Ne configurez pas de file d'attente de lettres mortes sur cet abonnement. Braze ne prend pas en charge les files d'attente de lettres mortes pour les abonnements d'ingestion de données cloud. Pour en savoir plus, consultez la section [Dead-letter topics](https://cloud.google.com/pubsub/docs/dead-letter-topics) dans la documentation Google Cloud.
{% endalert %}

### Étape 3 : Envoyer les notifications du compartiment vers le sujet {#step-3-send-bucket-notifications-to-the-topic}

{% alert important %}
La création d'une notification Cloud Storage vers Pub/Sub n'est pas disponible dans la console Google Cloud. Vous devez utiliser gcloud (présenté ici), Terraform ou l'API JSON. Pour en savoir plus, consultez la section [Configure Pub/Sub notifications for Cloud Storage](https://cloud.google.com/storage/docs/reporting-changes#enabling) dans la documentation Google Cloud.
{% endalert %}

Commencez par attribuer à l'agent de service Cloud Storage la permission de publier vers le sujet, puis créez la notification pour `OBJECT_FINALIZE`. L'événement `OBJECT_FINALIZE` se déclenche chaque fois qu'un nouvel objet est créé ou finalisé dans le compartiment.

```shell
# Get the Cloud Storage service agent for your project
gcloud storage service-agent --project=YOUR-PROJECT-ID

# Assign it Pub/Sub Publisher on the topic
gcloud pubsub topics add-iam-policy-binding YOUR-TOPIC \
  --project=YOUR-PROJECT-ID \
  --member="serviceAccount:service-YOUR-PROJECT-NUMBER@gs-project-accounts.iam.gserviceaccount.com" \
  --role="roles/pubsub.publisher"

# Create the OBJECT_FINALIZE notification (optionally scope to a folder with --object-prefix)
gcloud storage buckets notifications create gs://YOUR-BUCKET-NAME \
  --topic=YOUR-TOPIC \
  --event-types=OBJECT_FINALIZE \
  --payload-format=json
```

Remplacez les marques substitutives suivantes dans ces commandes :

- `YOUR-PROJECT-ID` : l'ID de votre projet Google Cloud, l'identifiant lisible par l'humain (par exemple, `my-gcp-project`).
- `YOUR-TOPIC` : le sujet Pub/Sub que vous avez créé à l'[étape 2](#step-2-create-a-pubsub-topic-and-subscription).
- `YOUR-BUCKET-NAME` : le nom de votre compartiment Cloud Storage.
- `YOUR-PROJECT-NUMBER` : le numéro de votre projet, l'identifiant numérique utilisé dans l'adresse e-mail de l'agent de service Cloud Storage. Il est différent de l'ID de projet. Vous le trouverez sur le **Dashboard** de la console Google Cloud, ou en exécutant la commande suivante :

```shell
gcloud projects describe YOUR-PROJECT-ID --format="value(projectNumber)"
```

### Étape 4 : Créer un compte de service {#step-4-create-a-service-account}

Dans la console Google Cloud, accédez à **IAM & Admin** > **Service Accounts** > **Create service account**.

Vous pouvez également utiliser gcloud :

```shell
gcloud iam service-accounts create braze-cdi-gcs \
  --project=YOUR-PROJECT-ID \
  --display-name="Braze CDI GCS"
```

### Étape 5 : Attribuer les permissions {#step-5-assign-permissions}

Le connecteur nécessite exactement les permissions suivantes : `storage.buckets.get`, `storage.objects.get` et `storage.objects.list` sur le compartiment, et `pubsub.subscriptions.consume` sur l'abonnement. Vous pouvez les attribuer avec un rôle personnalisé ou des rôles prédéfinis.

**Rôle personnalisé :** créez un rôle personnalisé avec exactement ces permissions et liez-le au compartiment et à l'abonnement :

```shell
gcloud iam roles create brazeCdiGcs --project=YOUR-PROJECT-ID \
  --title="Braze CDI GCS" \
  --permissions=storage.buckets.get,storage.objects.get,storage.objects.list,pubsub.subscriptions.consume \
  --stage=GA

gcloud storage buckets add-iam-policy-binding gs://YOUR-BUCKET-NAME \
  --member="serviceAccount:braze-cdi-gcs@YOUR-PROJECT-ID.iam.gserviceaccount.com" \
  --role="projects/YOUR-PROJECT-ID/roles/brazeCdiGcs"

gcloud pubsub subscriptions add-iam-policy-binding YOUR-SUBSCRIPTION \
  --project=YOUR-PROJECT-ID \
  --member="serviceAccount:braze-cdi-gcs@YOUR-PROJECT-ID.iam.gserviceaccount.com" \
  --role="projects/YOUR-PROJECT-ID/roles/brazeCdiGcs"
```

**Rôles prédéfinis :** attribuez `roles/storage.objectViewer` et `roles/storage.legacyBucketReader` sur le compartiment, et `roles/pubsub.subscriber` sur l'abonnement. Le rôle `objectViewer` fournit `storage.objects.get` et `storage.objects.list`, et le rôle `legacyBucketReader` fournit `storage.buckets.get` :

```shell
gcloud storage buckets add-iam-policy-binding gs://YOUR-BUCKET-NAME \
  --member="serviceAccount:braze-cdi-gcs@YOUR-PROJECT-ID.iam.gserviceaccount.com" \
  --role="roles/storage.objectViewer"
gcloud storage buckets add-iam-policy-binding gs://YOUR-BUCKET-NAME \
  --member="serviceAccount:braze-cdi-gcs@YOUR-PROJECT-ID.iam.gserviceaccount.com" \
  --role="roles/storage.legacyBucketReader"
gcloud pubsub subscriptions add-iam-policy-binding YOUR-SUBSCRIPTION \
  --project=YOUR-PROJECT-ID \
  --member="serviceAccount:braze-cdi-gcs@YOUR-PROJECT-ID.iam.gserviceaccount.com" \
  --role="roles/pubsub.subscriber"
```

### Étape 6 : Créer une clé JSON {#step-6-create-a-json-key}

Dans la console Google Cloud, ouvrez le compte de service, accédez à **Keys** > **Add key** > **Create new key**, puis sélectionnez **JSON**.

Vous pouvez également utiliser gcloud :

```shell
gcloud iam service-accounts keys create braze-cdi-gcs-key.json \
  --iam-account=braze-cdi-gcs@YOUR-PROJECT-ID.iam.gserviceaccount.com
```

## Configuration de l'ingestion de données cloud dans Braze

1. Dans Braze, accédez à **Data Settings** > **Cloud Data Ingestion** > **Sources**, sélectionnez **Add data source**, puis sélectionnez **Google Cloud Storage**.

![L'écran « Add New Source » avec Google Cloud Storage sélectionné dans la liste des sources de données.]({% image_buster /assets/img/cloud_ingestion/gcs_source_picker.png %})

{: start="2"}
2. Remplissez les champs de la source :
    - **Bucket** — le nom de votre compartiment
    - **Project ID** — l'ID de votre projet GCP
    - **Service account JSON key** — chargez le fichier de clé de l'étape 6 et donnez un nom à l'identifiant

![Le formulaire de source Google Cloud Storage affichant les champs Bucket, Project ID et chargement des identifiants.]({% image_buster /assets/img/cloud_ingestion/gcs_source_form.png %})

{: start="3"}
3. Sélectionnez **Test connection**, puis sélectionnez **Connect to Source**.
4. Créez une synchronisation. Accédez à **Data Settings** > **Cloud Data Ingestion** > **Syncs** et sélectionnez **Create data sync**. Choisissez un nom de synchronisation et un **Data Type** (tel que **User Attributes**, **Custom Events**, **Purchase Events**, **Catalog** ou **Delete Users**), puis sélectionnez **Next**.
5. À l'étape **Data definition**, sélectionnez votre source GCS, puis spécifiez les éléments suivants :
    - **Pub/Sub subscription ID** — l'ID d'abonnement de l'étape 2 (pas le sujet)
    - **Folder path** (optionnel) — un préfixe de chemin au sein du compartiment (voir [Synchroniser un dossier dans un compartiment partagé](#syncing-a-folder-in-a-shared-bucket))

![Le formulaire de synchronisation Google Cloud Storage affichant les champs Pub/Sub subscription ID et Folder path.]({% image_buster /assets/img/cloud_ingestion/gcs_sync_form.png %})

{: start="6"}
6. Sélectionnez **Preview and validate** pour confirmer que Braze peut atteindre l'abonnement et lister les fichiers disponibles à l'ingestion. Un test réussi affiche les fichiers existants dans le compartiment, mais ces fichiers ne seront pas synchronisés automatiquement.
7. Ajoutez une ou plusieurs adresses e-mail de contact pour les notifications d'erreur. Les synchronisations Google Cloud Storage sont pilotées par les événements, aucune planification n'est donc nécessaire — Braze ingère les nouveaux fichiers au fur et à mesure de leur chargement. Vérifiez le résumé, puis sélectionnez **Create sync**.

### Synchroniser un dossier dans un compartiment partagé {#syncing-a-folder-in-a-shared-bucket}

Vous pouvez réutiliser un même compartiment pour plusieurs synchronisations, mais chaque synchronisation doit cibler un dossier distinct **et** disposer de son propre abonnement Pub/Sub dédié.


{% alert important %}
Le chemin du dossier et l'abonnement doivent tous deux être uniques entre les synchronisations d'un même espace de travail lorsque plusieurs synchronisations partagent le même compartiment source. Comme indiqué à l'[étape 2](#step-2-create-a-pubsub-topic-and-subscription), ne configurez pas de file d'attente de lettres mortes sur ces abonnements.
{% endalert %}

Pour chaque dossier que vous souhaitez synchroniser dans un compartiment partagé :

1. Définissez le champ **Folder** de la synchronisation sur le préfixe de chemin (par exemple, `attributes/`). Braze ne liste et n'ingère que les objets dont le chemin commence par ce préfixe.
2. Créez un sujet dédié et une notification limitée au préfixe pour ce dossier, puis créez un abonnement sur ce sujet :

    ```shell
    # One topic per folder
    gcloud pubsub topics create YOUR-ATTRIBUTES-TOPIC --project=YOUR-PROJECT-ID

    # Assign the Cloud Storage service agent publisher on the topic
    gcloud pubsub topics add-iam-policy-binding YOUR-ATTRIBUTES-TOPIC \
      --project=YOUR-PROJECT-ID \
      --member="serviceAccount:service-YOUR-PROJECT-NUMBER@gs-project-accounts.iam.gserviceaccount.com" \
      --role="roles/pubsub.publisher"

    # Notification scoped to the folder with --object-prefix
    gcloud storage buckets notifications create gs://YOUR-BUCKET-NAME \
      --topic=YOUR-ATTRIBUTES-TOPIC --event-types=OBJECT_FINALIZE \
      --payload-format=json --object-prefix=attributes/

    # One subscription per sync
    gcloud pubsub subscriptions create YOUR-ATTRIBUTES-SUBSCRIPTION \
      --topic=YOUR-ATTRIBUTES-TOPIC --project=YOUR-PROJECT-ID --ack-deadline=60
    ```

3. Attribuez au compte de service Braze la permission de consommer sur cet abonnement, comme à l'[étape 5](#step-5-assign-permissions) :

    ```shell
    gcloud pubsub subscriptions add-iam-policy-binding YOUR-ATTRIBUTES-SUBSCRIPTION \
      --project=YOUR-PROJECT-ID \
      --member="serviceAccount:braze-cdi-gcs@YOUR-PROJECT-ID.iam.gserviceaccount.com" \
      --role="roles/pubsub.subscriber"
    ```

    Si vous avez créé le rôle personnalisé à l'[étape 5](#step-5-assign-permissions), utilisez `--role="projects/YOUR-PROJECT-ID/roles/brazeCdiGcs"` à la place.
4. Lorsque vous créez la synchronisation dans Braze, saisissez le nouvel **ID d'abonnement Pub/Sub** et le **chemin du dossier** de ce dossier afin que la synchronisation n'ingère que les fichiers de ce dossier.


{% endtab %}
{% endtabs %}

## Formats de fichiers requis {#required-file-formats}

Les formats de fichiers requis sont les mêmes pour Amazon S3 et Google Cloud Storage. L'ingestion de données cloud prend en charge les fichiers JSON, CSV et Parquet. Les colonnes requises dépendent du type de données :

- Les données utilisateur (attributs, événements personnalisés, événements d'achat) utilisent des identifiants utilisateur et un payload
- Les données de catalogue utilisent des identifiants de catalogue

Si vous utilisez le stockage de fichiers pour les données de catalogue, utilisez cette page avec [Synchroniser et supprimer les données de catalogue]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data) pour les exigences et le comportement spécifiques aux catalogues.

Braze n'impose aucune exigence supplémentaire concernant les noms de fichiers au-delà de ce qu'impose votre fournisseur de stockage de fichiers. Les noms de fichiers doivent être uniques. L'ajout d'un horodatage permet de garantir l'unicité.

Pour des exemples de tous les types de fichiers pris en charge (attributs, événements personnalisés, achats, catalogues et suppressions d'utilisateurs), consultez les fichiers exemples dans [braze-examples](https://github.com/braze-inc/braze-examples/tree/main/cloud-data-ingestion/braze-examples/payloads/file_storage).

### Identifiants utilisateur {#user-identifiers}

Pour les synchronisations de données utilisateur (attributs, événements personnalisés, événements d'achat), chaque ligne de votre fichier source nécessite exactement un identifiant utilisateur et une colonne `payload`. Un fichier source peut contenir des lignes avec différents types d'identifiants, mais chaque ligne individuelle ne doit en utiliser qu'un seul.

| Identifiant | Description |
| --- | --- |
| `EXTERNAL_ID` | Identifie l'utilisateur que vous souhaitez mettre à jour. Doit correspondre à la valeur `external_id` utilisée dans Braze. |
| `ALIAS_NAME` et `ALIAS_LABEL` | Ces deux colonnes créent un objet d'alias d'utilisateur. `alias_name` doit être un identifiant unique, et `alias_label` spécifie le type d'alias. Les utilisateurs peuvent avoir plusieurs alias avec des libellés différents, mais un seul `alias_name` par `alias_label`. |
| `BRAZE_ID` | L'identifiant utilisateur Braze. Il est généré par le SDK Braze, et de nouveaux utilisateurs ne peuvent pas être créés à l'aide d'un Braze ID via l'ingestion de données cloud. Pour créer de nouveaux utilisateurs, spécifiez un ID externe ou un alias d'utilisateur. |
| `EMAIL` | L'adresse e-mail de l'utilisateur. Si plusieurs profils avec la même adresse e-mail existent, le profil mis à jour le plus récemment est prioritaire pour les mises à jour. Si vous incluez à la fois l'e-mail et le téléphone, Braze utilise l'e-mail comme identifiant principal. |
| `PHONE` | Le numéro de téléphone de l'utilisateur. Si plusieurs profils avec le même numéro de téléphone existent, le profil mis à jour le plus récemment est prioritaire pour les mises à jour. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Identifiants utilisateur" }

En plus d'un identifiant, chaque ligne doit contenir une colonne `payload` avec une chaîne JSON des champs que vous souhaitez synchroniser vers l'utilisateur dans Braze.

{% alert note %}
Contrairement aux sources d'entrepôt de données, la colonne `UPDATED_AT` n'est ni requise ni prise en charge pour les synchronisations par stockage de fichiers.
{% endalert %}

### Identifiants de catalogue {#catalog-identifiers}

Pour les synchronisations de catalogue, votre fichier source doit contenir les colonnes suivantes. Les fichiers de catalogue utilisent des identifiants différents de ceux des fichiers de données utilisateur.

| Colonne | Obligatoire | Description |
| --- | --- | --- |
| `ID` | Oui | L'identifiant unique de l'élément de catalogue. Utilisé pour créer, mettre à jour ou supprimer l'élément dans Braze. |
| `payload` | Oui | Une chaîne JSON des champs et valeurs du catalogue à synchroniser. Doit correspondre au schéma de votre catalogue dans Braze. |
| `DELETED` | Non | Lorsque la valeur est `true`, l'élément de catalogue correspondant à l'`ID` est supprimé du catalogue dans Braze. Omettez cette colonne ou définissez-la sur `false` pour les opérations de création ou de mise à jour. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Identifiants de catalogue" }

### Exemples {#examples}

{% tabs %}
{% tab Attributs JSON %}
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
{% tab Événements personnalisés JSON %}
``` json
{"external_id":"s3-qa-0","payload":"{\"app_id\": \"YOUR_APP_ID\", \"name\": \"view-206\", \"time\": \"2024-04-02T14:34:08\", \"properties\": {\"bool_value\": false, \"preceding_event\": \"unsubscribe\", \"important_number\": 206}}"}
{"external_id":"s3-qa-1","payload":"{\"app_id\": \"YOUR_APP_ID\", \"name\": \"view-206\", \"time\": \"2024-04-02T14:34:08\", \"properties\": {\"bool_value\": false, \"preceding_event\": \"unsubscribe\", \"important_number\": 206}}"}
```
{% alert important %}
Chaque ligne de votre fichier source doit contenir du JSON valide, sinon le fichier sera ignoré.
{% endalert %}
{% endtab %}
{% tab Événements d'achat JSON %}
``` json
{"external_id":"s3-qa-0","payload":"{\"app_id\": \"YOUR_APP_ID\", \"product_id\": \"product-11\", \"currency\": \"BSD\", \"price\": 8.511527858335066, \"time\": \"2024-04-02T14:34:08\", \"quantity\": 19, \"properties\": {\"is_a_boolean\": true, \"important_number\": 40, \"preceding_event\": \"click\"}}"}
{"external_id":"s3-qa-1","payload":"{\"app_id\": \"YOUR_APP_ID\", \"product_id\": \"product-11\", \"currency\": \"BSD\", \"price\": 8.511527858335066, \"time\": \"2024-04-02T14:34:08\", \"quantity\": 19, \"properties\": {\"is_a_boolean\": true, \"important_number\": 40, \"preceding_event\": \"click\"}}"}
```
{% alert important %}
Chaque ligne de votre fichier source doit contenir du JSON valide, sinon le fichier sera ignoré.
{% endalert %}

{% endtab %}
{% tab Attributs CSV %}
```plaintext
external_id,payload
s3-qa-load-0-d0daa196-cdf5-4a69-84ae-4797303aee75,"{""name"": ""SNXIM"", ""age"": 54, ""subscriber"": true, ""retention"": {""previous_purchases"": 19, ""vip"": true}, ""last_visit"": ""2023-08-08T16:03:26.598806""}"
s3-qa-load-1-d0daa196-cdf5-4a69-84ae-4797303aee75,"{""name"": ""0J747"", ""age"": 73, ""subscriber"": false, ""retention"": {""previous_purchases"": 22, ""vip"": false}, ""last_visit"": ""2023-08-08T16:03:26.598816""}"
s3-qa-load-2-d0daa196-cdf5-4a69-84ae-4797303aee75,"{""name"": ""EP1U0"", ""age"": 99, ""subscriber"": false, ""retention"": {""previous_purchases"": 23, ""vip"": false}, ""last_visit"": ""2023-08-08T16:03:26.598822""}"
```
{% endtab %}
{% tab Catalogues CSV %}
```plaintext
ID,PAYLOAD,DELETED
85,"{""product_name"": ""Product 85"", ""price"": 85.85}",false
1,"{""product_name"": ""Product 1"", ""price"": 1.01}",true
```
Incluez une colonne `DELETED` facultative. Lorsque `DELETED` est défini sur `true`, cet élément de catalogue est supprimé du catalogue dans Braze. Pour la liste complète des colonnes requises, consultez [Identifiants de catalogue](#catalog-identifiers). Pour le comportement de suppression, consultez [Suppression d'éléments de catalogue](#deleting-catalog-items). Pour un flux de configuration de catalogue de bout en bout (y compris la création du catalogue cible et le comportement de synchronisation), consultez [Synchroniser et supprimer les données de catalogue]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data).
{% endtab %}

{% endtabs %}

## Suppression de données {#deleting-data}

L'ingestion de données cloud pour le stockage de fichiers prend en charge la suppression d'utilisateurs et d'éléments de catalogue via des téléversements de fichiers. Utilisez des synchronisations et des formats de fichiers distincts pour chaque type.

- **[Suppression d'utilisateurs](#deleting-users)** – Créez une synchronisation avec le type de données **Delete Users** et téléversez des fichiers contenant uniquement des identifiants d'utilisateurs (sans payload).
- **[Suppression d'éléments de catalogue](#deleting-catalog-items)** – Utilisez votre synchronisation de catalogue existante et ajoutez une colonne `deleted` (ou `DELETED`) pour marquer les éléments à supprimer.

### Suppression d'utilisateurs {#deleting-users}

Pour supprimer des profils utilisateur dans Braze à l'aide de fichiers dans votre compartiment source :

1. Créez une nouvelle synchronisation d'ingestion de données cloud (même configuration que pour les autres synchronisations).
2. Lors de la configuration de la synchronisation dans Braze, définissez **Data Type** sur **Delete Users**.
3. Téléversez dans votre compartiment source des fichiers contenant uniquement des colonnes d'identifiants d'utilisateurs. N'incluez pas de colonne `payload` : la synchronisation échoue si un payload est présent, afin d'éviter les suppressions accidentelles.

Chaque ligne du fichier doit identifier exactement un utilisateur à l'aide de l'un des éléments suivants :

| Identifiant | Description |
| --- | --- |
| `EXTERNAL_ID` | Correspond à l'`external_id` utilisé dans Braze. |
| `ALIAS_NAME` et `ALIAS_LABEL` | Les deux colonnes ensemble identifient l'utilisateur par alias. |
| `BRAZE_ID` | ID d'utilisateur généré par Braze (utilisateurs existants uniquement). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Suppression d'utilisateurs" }

{% alert important %}
La suppression d'utilisateurs est permanente et ne peut pas être annulée. N'incluez que les utilisateurs que vous souhaitez réellement supprimer. Pour plus de détails, consultez [Supprimer des utilisateurs avec l'ingestion de données cloud]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/delete_users).
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

1. Utilisez la même synchronisation que celle que vous utilisez pour [synchroniser les données de catalogue]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data) (type de données **Catalogs**).
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

Lorsque la synchronisation s'exécute, les lignes avec `deleted: true` entraînent la suppression de l'élément de catalogue correspondant dans Braze. Pour le comportement complet de synchronisation et de suppression de catalogue, consultez [Synchroniser et supprimer des données de catalogue]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data).

## Informations importantes {#things-to-know}

- Les fichiers ajoutés au compartiment source ne doivent pas dépasser 512&nbsp;Mo. Cette limite s'applique à Amazon S3 et à Google Cloud Storage. Les fichiers de plus de 512&nbsp;Mo génèrent une erreur et ne sont pas synchronisés avec Braze.
- Bien qu'il n'y ait pas de limite supplémentaire sur le nombre de lignes par fichier, nous recommandons d'utiliser des fichiers plus petits pour améliorer la vitesse d'exécution de vos synchronisations. Par exemple, l'ingestion d'un fichier de 500&nbsp;Mo prendrait considérablement plus de temps que celle de cinq fichiers distincts de 100&nbsp;Mo.
- Il n'y a pas de limite supplémentaire sur le nombre de fichiers téléchargés dans un laps de temps donné.
- L'ordonnancement n'est pas pris en charge à l'intérieur des fichiers ni entre les fichiers. Nous recommandons de regrouper les mises à jour périodiquement si vous surveillez d'éventuelles conditions de concurrence.

## Résolution des problèmes {#troubleshooting}

### Téléchargement et traitement des fichiers {#uploading-files-and-processing}

Le CDI ne traite que les fichiers ajoutés après la création de la synchronisation. Dans ce processus, Braze recherche les nouveaux fichiers ajoutés, ce qui déclenche une nouvelle notification. Celle-ci lance une nouvelle synchronisation pour traiter le nouveau fichier. Pour Amazon S3, la notification est un message envoyé à SQS. Pour Google Cloud Storage, il s'agit d'un message `OBJECT_FINALIZE` envoyé à Pub/Sub.

Vous pouvez utiliser des fichiers existants pour vérifier que Braze peut accéder à votre compartiment et détecter les fichiers à ingérer, mais ils ne sont pas synchronisés avec Braze. Pour que le CDI les traite, vous devez re-télécharger dans le compartiment source tous les fichiers existants que vous souhaitez synchroniser.

### Gestion des erreurs de fichiers inattendues (Amazon S3) {#handling-unexpected-file-errors-amazon-s3}

Si vous observez un nombre élevé d'erreurs ou de fichiers en échec, il est possible qu'un autre processus ajoute des fichiers dans le compartiment S3 dans un dossier autre que le dossier cible du CDI.

Lorsque des fichiers sont téléchargés dans le compartiment source mais pas dans le dossier source, le CDI traite la notification SQS sans effectuer aucune action sur le fichier, ce qui peut apparaître comme une erreur.

Si votre problème est lié aux notifications S3 ou aux permissions de destination SQS (par exemple, des erreurs de validation de destination), consultez la documentation AWS :

- [Activer et configurer les notifications d'événements à l'aide de la console Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/enable-event-notifications.html)
- [Accorder les permissions de publication de messages de notification d'événements vers une destination](https://docs.aws.amazon.com/AmazonS3/latest/userguide/grant-destinations-permissions-to-s3.html)
- [Résolution des problèmes dans Amazon SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-troubleshooting.html)

### Gestion des erreurs de fichiers inattendues (Google Cloud Storage) {#handling-unexpected-file-errors-google-cloud-storage}

Comme pour Amazon S3, le CDI ne traite que les fichiers téléchargés après la création de la synchronisation. Chaque nouvel objet déclenche un message `OBJECT_FINALIZE` vers votre sujet Pub/Sub. Pour ingérer des fichiers qui existent déjà dans le compartiment, re-téléchargez-les.

Si les fichiers ne sont pas ingérés, vérifiez les éléments suivants :

- La notification du compartiment existe. Listez les notifications du compartiment avec `gcloud storage buckets notifications list gs://YOUR-BUCKET-NAME`.
- L'agent de service Cloud Storage dispose du rôle `roles/pubsub.publisher` sur le sujet.
- Le compte de service Braze dispose de la permission de consommation sur l'abonnement (`pubsub.subscriptions.consume`, attribuée via le rôle personnalisé ou `roles/pubsub.subscriber`).
- L'abonnement n'a pas de file d'attente de lettres mortes configurée. Braze ne prend pas en charge les files d'attente de lettres mortes pour les abonnements d'ingestion de données Cloud.

Pour plus d'informations, consultez [Notifications Pub/Sub pour Cloud Storage](https://cloud.google.com/storage/docs/pubsub-notifications) dans la documentation Google Cloud.