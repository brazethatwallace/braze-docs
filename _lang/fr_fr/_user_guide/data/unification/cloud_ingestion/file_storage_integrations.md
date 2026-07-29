---
nav_title: Intégrations de stockage de fichiers
article_title: Intégrations de stockage de fichiers
description: "Cette page traite de l'Ingestion de données cloud de Braze et de la synchronisation des données pertinentes d'Amazon S3 ou de Google Cloud Storage vers Braze."
page_order: 4
page_type: reference

---

# Intégrations de stockage de fichiers {#file-storage-integrations}

> Cette page explique comment configurer l'Ingestion de données cloud pour synchroniser les données d'Amazon S3 ou de Google Cloud Storage vers Braze.

## Fonctionnement {#how-it-works}

Vous pouvez utiliser l'Ingestion de données cloud (CDI) pour intégrer directement un ou plusieurs compartiments de stockage de votre compte cloud à Braze. Lorsque vous ajoutez un nouveau fichier à un compartiment, votre fournisseur cloud publie une notification et l'Ingestion de données cloud de Braze synchronise les données.

Le mécanisme de notification dépend de votre fournisseur :

- **Amazon S3 :** Lorsque de nouveaux fichiers sont publiés sur S3, un message est envoyé à une file d'attente Amazon Simple Queue Service (SQS) et Braze consomme ce message pour ingérer le nouveau fichier.
- **Google Cloud Storage (GCS) :** Lorsque de nouveaux fichiers sont finalisés dans le compartiment, GCS publie une notification `OBJECT_FINALIZE` vers un topic Pub/Sub. Braze consomme ces notifications depuis un abonnement Pub/Sub pour ingérer le nouveau fichier.

L'Ingestion de données cloud prend en charge les éléments suivants :

- Fichiers JSON
- Fichiers CSV
- Fichiers Parquet
- Données d'attributs, d'événements personnalisés, d'événements d'achat, de suppression d'utilisateurs et de catalogues

## Configuration de l'Ingestion de données cloud {#setting-up-cloud-data-ingestion}

Les étapes de configuration dépendent de votre fournisseur de stockage de fichiers. Sélectionnez l'onglet correspondant à votre fournisseur, puis complétez la configuration commune dans les sections qui suivent.

{% tabs %}
{% tab Amazon S3 %}

L'intégration nécessite les ressources suivantes :

- Compartiment S3 pour le stockage des données
- File d'attente SQS pour les notifications de nouveaux fichiers
- Rôle IAM pour l'accès de Braze

### Définitions AWS {#aws-definitions}

| Terme | Définition |
| --- | --- |
| Nom de ressource Amazon (ARN) | L'ARN est un identifiant unique pour les ressources AWS. |
| Gestion des identités et des accès (IAM) | IAM est un service Web qui vous permet de contrôler, en toute sécurité, l'accès aux ressources AWS. Dans ce tutoriel, vous allez créer une politique IAM et l'attribuer à un rôle IAM pour intégrer votre compartiment S3 à l'Ingestion de données cloud de Braze. |
| Amazon Simple Queue Service (SQS) | SQS est une file d'attente hébergée qui vous permet d'intégrer des systèmes et des composants logiciels distribués. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Définitions AWS" }

## Configuration de l'Ingestion de données cloud dans AWS {#setting-up-cloud-data-ingestion-in-aws}

### Étape 1 : Créer un compartiment source {#step-1-create-a-source-bucket}

Créez un compartiment S3 à usage général avec les paramètres par défaut dans votre compte AWS. Les compartiments S3 peuvent être réutilisés d'une synchronisation à l'autre, à condition que le dossier soit unique.

Les paramètres par défaut sont les suivants :

- ACL désactivés
- Bloquer tout accès public
- Désactiver la gestion des versions des compartiments
- Chiffrement SSE-S3
  - SSE-S3 est le seul type de chiffrement côté serveur pris en charge. Le chiffrement Amazon KMS n'est pas pris en charge.

Notez bien la région dans laquelle vous avez créé le compartiment, car vous devrez créer une file d'attente SQS dans la même région à l'étape suivante.

### Étape 2 : Créer une file d'attente SQS {#step-2-create-sqs-queue}

Créez une file d'attente SQS pour suivre l'ajout d'objets dans le compartiment que vous avez créé. Utilisez pour l'instant les paramètres de configuration par défaut.

Une file d'attente SQS doit être unique au niveau mondial (par exemple, une seule peut être utilisée pour une synchronisation CDI et ne peut pas être réutilisée dans un autre espace de travail).

{% alert important %}
Veillez à créer cette file SQS dans la même région que celle dans laquelle vous avez créé le compartiment.
{% endalert %}

Pensez à noter l'ARN et l'URL de la file SQS, car vous les utiliserez fréquemment au cours de cette configuration.

![Sélection de l'option « Avancé » avec un exemple d'objet JSON pour définir qui peut accéder à une file d'attente.]({% image_buster /assets/img/cloud_ingestion/s3_ARN.png %})

### Étape 3 : Configurer une politique d'accès {#step-3-set-up-access-policy}

Pour configurer la politique d'accès, sélectionnez **Options avancées**.

Ajoutez la déclaration suivante à la politique d'accès de la file d'attente, en prenant soin de remplacer `YOUR-BUCKET-NAME-HERE` par le nom de votre compartiment, `YOUR-SQS-ARN` par l'ARN de votre file d'attente SQS, et `YOUR-AWS-ACCOUNT-ID` par l'ID de votre compte AWS :

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

1. Dans le compartiment créé à l'étape 1, allez dans **Properties** > **Event notifications**.
2. Donnez un nom à la configuration. Vous pouvez également spécifier un préfixe ou un suffixe à cibler si vous souhaitez que seul un sous-ensemble de fichiers soit ingéré par Braze.
3. Sous **Destination**, sélectionnez **SQS queue** et indiquez l'ARN du SQS que vous avez créé à l'étape 2.

{% alert note %}
Si vous téléchargez vos fichiers dans le dossier racine d'un compartiment S3, puis que vous déplacez certains de ces fichiers vers un dossier spécifique du compartiment, vous risquez de rencontrer une erreur inattendue. Au lieu de cela, vous pouvez modifier les notifications d'événements pour qu'elles soient envoyées uniquement pour les fichiers du préfixe, éviter de placer des fichiers dans le compartiment S3 en dehors de ce préfixe, ou mettre à jour l'intégration sans préfixe, ce qui entraînera alors l'ingestion de tous les fichiers.
{% endalert %}

### Étape 5 : Créer une politique IAM {#step-5-create-an-iam-policy}

Créez une politique IAM pour permettre à Braze d'interagir avec votre compartiment source. Pour commencer, connectez-vous à la console de gestion AWS en tant qu'administrateur de compte.

1. Allez dans la section IAM de la console AWS, sélectionnez **Policies** dans la barre de navigation, puis cliquez sur **Create Policy**.<br><br>![Le bouton « Create Policy » dans la console AWS.]({% image_buster /assets/img/create_policy_1_list.png %})<br><br>

2. Ouvrez l'onglet **JSON** et saisissez l'extrait de code suivant dans la section **Policy Document**, en prenant soin de remplacer `YOUR-BUCKET-NAME-HERE` par le nom de votre compartiment et `YOUR-SQS-ARN-HERE` par le nom de votre file d'attente SQS :

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

![Une politique d'exemple nommée « new-policy-name ».]({% image_buster /assets/img/create_policy_3_name.png %})

![Le champ de description de la politique.]({% image_buster /assets/img/create_policy_4_created.png %})

### Étape 6 : Créer un rôle IAM {#step-6-create-an-iam-role}

Pour terminer la configuration sur AWS, créez un rôle IAM et associez-y la politique IAM de l'étape 5.

1. Dans la même section IAM de la console où vous avez créé la politique IAM, allez dans **Roles** > **Create Role**.

![Le bouton « Create Role ».]({% image_buster /assets/img/create_role_1_list.png %})

{: start="2"}
2. Dans AWS, sélectionnez **Another AWS Account** comme type de sélecteur d'entité de confiance. Indiquez votre ID de compte Braze. Cochez la case **Require external ID**.
3. Dans Braze, accédez à **Paramètres des données** > **Ingestion de données cloud** > **Sources**, sélectionnez **Ajouter une source de données**, puis choisissez **Amazon S3** dans la section des sources de fichiers.
4. Copiez l'**ID de compte Braze** généré automatiquement.

![La page « Ajouter une nouvelle source » affichant les sections Nom de la source et Détails de connexion S3.]({% image_buster /assets/img/braze_account_id.png %})

{: start="6"}
5. Dans AWS, collez l'ID du compte, puis sélectionnez **Next**.

![Page S3 « Create Role ». Cette page comporte des champs pour le nom du rôle, la description du rôle, les entités de confiance, les politiques et les restrictions d'autorisations.]({% image_buster /assets/img/create_role_2_another.png %})<br><br>

{: start="7"}
6. Attachez la politique créée à l'étape 4 au rôle. Recherchez la politique dans la barre de recherche et cochez la case à côté de la politique pour la joindre. Sélectionnez **Next** lorsque vous avez terminé.

![Rôle ARN avec le nom de la nouvelle politique sélectionné.]({% image_buster /assets/img/create_role_3_attach.png %})

Donnez un nom et une description au rôle, puis sélectionnez **Create Role**.

![Un exemple de rôle nommé « new-role-name ».]({% image_buster /assets/img/create_role_4_name.png %})

{: start="8"}
7. Notez l'ARN du rôle que vous avez créé et l'ID externe que vous avez généré, car vous en aurez besoin pour créer l'intégration Ingestion de données cloud.

## Configuration de l'Ingestion de données cloud dans Braze {#setting-up-cloud-data-ingestion-in-braze}

1. Commencez par créer une nouvelle source dans le tableau de bord de Braze. Accédez à **Paramètres des données** > **Ingestion de données cloud** > **Sources**, sélectionnez **Ajouter une source de données**, puis choisissez **Amazon S3**.
2. Choisissez un nom pour votre source et saisissez les informations issues du processus de configuration AWS pour créer une nouvelle source. Précisez les éléments suivants :

  - ARN du rôle
  - ID externe
  - Nom du compartiment
  - Région

![La section Détails de connexion S3 affichant les identifiants (configuration AWS et configuration Braze) et les champs de configuration.]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_1.png %})

{: start="3"}
3. Sélectionnez **Tester la connexion** pour confirmer que Braze peut accéder à votre compartiment. Après un test réussi, sélectionnez **Se connecter à la source**. Si la connexion échoue, un message d'erreur s'affiche pour vous aider à résoudre le problème.

{: start="4"}
4. Ensuite, créez une nouvelle synchronisation. Accédez à **Paramètres des données** > **Ingestion de données cloud** > **Synchronisations** et sélectionnez **Créer une synchronisation de données**.

{: start="5"}
5. Choisissez un nom pour votre synchronisation. Sélectionnez ensuite une source S3 active et saisissez votre table source pour la synchronisation. Sélectionnez un type de données et cliquez sur **Tester la connexion**.

![Une option permettant de tester la connexion avec un aperçu des données.]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_4.png %})

6. Saisissez les informations restantes issues du processus de configuration AWS. Précisez les éléments suivants :
- URL SQS (doit être unique pour chaque nouvelle intégration)
- Chemin d'accès au dossier (facultatif, doit être unique pour toutes les synchronisations d'un espace de travail)

7. Sélectionnez un type de données et cliquez sur **Tester la connexion** pour confirmer que Braze peut lister les fichiers disponibles à l'ingestion (et non les données contenues dans ces fichiers). Une fois le test réussi, sélectionnez **Suivant : Notifications**.
8. Ajoutez une ou plusieurs adresses e-mail de contact pour recevoir des notifications si la synchronisation est interrompue en raison de problèmes d'accès ou d'autorisations. Si vous le souhaitez, activez les notifications pour les erreurs au niveau de l'utilisateur et les synchronisations réussies.
9. Créez la synchronisation.

{% endtab %}
{% tab Google Cloud Storage %}

L'intégration nécessite les ressources suivantes :

- Un compartiment Cloud Storage pour le stockage des données
- Un topic et un abonnement Pub/Sub pour les notifications de nouveaux fichiers
- Un compte de service dont vous téléchargez la clé JSON vers Braze

### Définitions GCP {#gcp-definitions}

| Terme | Définition |
| --- | --- |
| Projet Google Cloud | Un projet organise toutes vos ressources Google Cloud et est identifié par un ID de projet unique et un numéro de projet. |
| Compartiment Cloud Storage | Un compartiment est le conteneur qui héberge les fichiers de données que vous souhaitez que Braze ingère. |
| Topic Pub/Sub | Un topic est la ressource nommée qui reçoit les notifications de nouveaux fichiers depuis votre compartiment Cloud Storage. |
| Abonnement Pub/Sub | Un abonnement s'attache à un topic et distribue ses messages. Braze consomme les notifications de nouveaux fichiers depuis un abonnement pull. |
| Compte de service | Un compte de service est une identité non humaine que Braze utilise pour accéder à votre compartiment et à votre abonnement. Vous téléchargez sa clé JSON vers Braze. |
| Rôle IAM | Un rôle de gestion des identités et des accès (IAM) est un ensemble d'autorisations que vous accordez au compte de service sur votre compartiment et votre abonnement. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Définitions GCP" }

## Configuration de l'Ingestion de données cloud dans Google Cloud {#setting-up-cloud-data-ingestion-in-google-cloud}

### Étape 1 : Créer un compartiment Cloud Storage {#step-1-create-a-cloud-storage-bucket}

Dans la console Google Cloud, accédez à **Cloud Storage** > **Buckets** > **Create**. Notez l'ID du projet et le nom du compartiment — vous en aurez besoin lors de la configuration de la source dans Braze. Nous recommandons d'activer l'accès uniforme au niveau du compartiment afin que les autorisations soient gérées avec IAM.

Vous pouvez également créer le compartiment avec gcloud :

```shell
gcloud storage buckets create gs://YOUR-BUCKET-NAME \
  --project=YOUR-PROJECT-ID \
  --location=YOUR-REGION \
  --uniform-bucket-level-access
```

### Étape 2 : Créer un topic et un abonnement Pub/Sub {#step-2-create-a-pubsub-topic-and-subscription}

Dans la console Google Cloud, accédez à **Pub/Sub** > **Topics** > **Create topic**. Vous pouvez laisser Google créer un abonnement par défaut, ou en créer un séparément. Ensuite, créez un abonnement **pull** sur ce topic.

Vous pouvez également utiliser gcloud :

```shell
gcloud pubsub topics create YOUR-TOPIC --project=YOUR-PROJECT-ID
gcloud pubsub subscriptions create YOUR-SUBSCRIPTION \
  --topic=YOUR-TOPIC --project=YOUR-PROJECT-ID --ack-deadline=60
```

Notez l'**ID de l'abonnement** — Braze a besoin de l'abonnement (et non du topic) lorsque vous créez la synchronisation. L'abonnement doit être de type pull.

### Étape 3 : Envoyer les notifications du compartiment vers le topic {#step-3-send-bucket-notifications-to-the-topic}

{% alert important %}
La création d'une notification Cloud Storage vers Pub/Sub n'est pas disponible dans la console Google Cloud. Vous devez utiliser gcloud (illustré ici), Terraform ou l'API JSON. Pour en savoir plus, consultez [Configurer les notifications Pub/Sub pour Cloud Storage](https://cloud.google.com/storage/docs/reporting-changes#enabling) dans la documentation Google Cloud.
{% endalert %}

Commencez par accorder à l'agent de service Cloud Storage l'autorisation de publier sur le topic, puis créez la notification pour `OBJECT_FINALIZE`. L'événement `OBJECT_FINALIZE` se déclenche chaque fois qu'un nouvel objet est créé ou finalisé dans le compartiment.

```shell
# Get the Cloud Storage service agent for your project
gcloud storage service-agent --project=YOUR-PROJECT-ID

# Grant it Pub/Sub Publisher on the topic
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

- `YOUR-PROJECT-ID` : l'ID de votre projet Google Cloud, l'identifiant lisible (par exemple, `my-gcp-project`).
- `YOUR-TOPIC` : le topic Pub/Sub que vous avez créé à l'[étape 2](#step-2-create-a-pubsub-topic-and-subscription).
- `YOUR-BUCKET-NAME` : le nom de votre compartiment Cloud Storage.
- `YOUR-PROJECT-NUMBER` : le numéro de votre projet, l'identifiant numérique utilisé dans l'adresse e-mail de l'agent de service Cloud Storage. Il est différent de l'ID du projet. Vous le trouverez sur le **Dashboard** de la console Google Cloud, ou en exécutant la commande suivante :

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

### Étape 5 : Accorder les autorisations {#step-5-grant-permissions}

Le connecteur nécessite exactement ces autorisations : `storage.buckets.get`, `storage.objects.get` et `storage.objects.list` sur le compartiment, et `pubsub.subscriptions.consume` sur l'abonnement. Vous pouvez les accorder avec un rôle personnalisé ou des rôles prédéfinis.

**Rôle personnalisé :** Créez un rôle personnalisé avec exactement ces autorisations et liez-le au compartiment et à l'abonnement :

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

**Rôles prédéfinis :** Accordez `roles/storage.objectViewer` et `roles/storage.legacyBucketReader` sur le compartiment, et `roles/pubsub.subscriber` sur l'abonnement. Le rôle `objectViewer` fournit `storage.objects.get` et `storage.objects.list`, et `legacyBucketReader` fournit `storage.buckets.get` :

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

## Configuration de l'Ingestion de données cloud dans Braze

1. Dans Braze, accédez à **Paramètres des données** > **Ingestion de données cloud** > **Sources**, sélectionnez **Ajouter une source de données**, puis choisissez **Google Cloud Storage**.

![L'écran « Ajouter une nouvelle source » avec Google Cloud Storage sélectionné dans la liste des sources de données.]({% image_buster /assets/img/cloud_ingestion/gcs_source_picker.png %})

{: start="2"}
2. Remplissez les champs de la source :
    - **Bucket** — le nom de votre compartiment
    - **Project ID** — l'ID de votre projet GCP
    - **Service account JSON key** — téléchargez le fichier de clé de l'étape 6 et donnez un nom à l'identifiant

![Le formulaire de source Google Cloud Storage affichant les champs Bucket, Project ID et téléchargement d'identifiant.]({% image_buster /assets/img/cloud_ingestion/gcs_source_form.png %})

{: start="3"}
3. Sélectionnez **Tester la connexion**, puis sélectionnez **Se connecter à la source**.
4. Créez une synchronisation. Accédez à **Paramètres des données** > **Ingestion de données cloud** > **Synchronisations** et sélectionnez **Créer une synchronisation de données**. Choisissez un nom de synchronisation et un **Type de données** (tel que **Attributs utilisateur**, **Événements personnalisés**, **Événements d'achat**, **Catalogue** ou **Supprimer les utilisateurs**), puis sélectionnez **Suivant**.
5. À l'étape **Définition des données**, sélectionnez votre source GCS, puis précisez les éléments suivants :
    - **ID d'abonnement Pub/Sub** — l'ID de l'abonnement de l'étape 2 (et non le topic)
    - **Chemin d'accès au dossier** (facultatif) — un préfixe de chemin dans le compartiment (voir [Synchroniser un dossier dans un compartiment partagé](#syncing-a-folder-in-a-shared-bucket))

![Le formulaire de synchronisation Google Cloud Storage affichant les champs ID d'abonnement Pub/Sub et chemin d'accès au dossier.]({% image_buster /assets/img/cloud_ingestion/gcs_sync_form.png %})

{: start="6"}
6. Sélectionnez **Prévisualiser et valider** pour confirmer que Braze peut atteindre l'abonnement et lister les fichiers disponibles à l'ingestion. Un test réussi listera les fichiers existants dans le compartiment, mais ces fichiers ne seront pas synchronisés automatiquement.
7. Ajoutez une ou plusieurs adresses e-mail de contact pour les notifications d'erreur. Les synchronisations Google Cloud Storage sont pilotées par les événements, aucune planification n'est donc nécessaire — Braze ingère les nouveaux fichiers au fur et à mesure de leur téléchargement. Vérifiez le résumé, puis sélectionnez **Créer la synchronisation**.

### Synchroniser un dossier dans un compartiment partagé {#syncing-a-folder-in-a-shared-bucket}

Vous pouvez réutiliser un même compartiment pour plusieurs synchronisations, mais chaque synchronisation doit cibler un dossier distinct **et** disposer de son propre abonnement Pub/Sub dédié.

{% alert important %}
Le chemin d'accès au dossier et l'abonnement doivent tous deux être uniques pour toutes les synchronisations d'un espace de travail lorsque plusieurs synchronisations partagent le même compartiment source.
{% endalert %}

Pour chaque dossier que vous souhaitez synchroniser dans un compartiment partagé :

1. Définissez le champ **Dossier** de la synchronisation sur le préfixe de chemin (par exemple, `attributes/`). Braze ne listera et n'ingérera que les objets dont le chemin commence par ce préfixe.
2. Créez un topic dédié et une notification limitée au préfixe pour ce dossier, puis créez un abonnement sur ce topic :

    ```shell
    # One topic per folder
    gcloud pubsub topics create YOUR-ATTRIBUTES-TOPIC --project=YOUR-PROJECT-ID

    # Grant the Cloud Storage service agent publisher on the topic
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

3. Accordez au compte de service Braze l'autorisation de consommer cet abonnement, comme à l'[étape 5](#step-5-grant-permissions) :

    ```shell
    gcloud pubsub subscriptions add-iam-policy-binding YOUR-ATTRIBUTES-SUBSCRIPTION \
      --project=YOUR-PROJECT-ID \
      --member="serviceAccount:braze-cdi-gcs@YOUR-PROJECT-ID.iam.gserviceaccount.com" \
      --role="roles/pubsub.subscriber"
    ```

    Si vous avez créé le rôle personnalisé à l'[étape 5](#step-5-grant-permissions), utilisez `--role="projects/YOUR-PROJECT-ID/roles/brazeCdiGcs"` à la place.
4. Lorsque vous créez la synchronisation dans Braze, saisissez l'**ID d'abonnement Pub/Sub** et le **chemin d'accès au dossier** de ce dossier afin que la synchronisation n'ingère que les fichiers de ce dossier.


{% endtab %}
{% endtabs %}

## Formats de fichiers requis {#required-file-formats}

Les formats de fichiers requis sont les mêmes pour Amazon S3 et Google Cloud Storage. L'Ingestion de données cloud prend en charge les fichiers JSON, CSV et Parquet. Les colonnes requises dépendent du type de données :

- Les données utilisateur (attributs, événements personnalisés, événements d'achat) utilisent des identifiants utilisateur et un payload
- Les données de catalogue utilisent des identifiants de catalogue

Si vous utilisez le stockage de fichiers pour les données de catalogue, consultez cette page ainsi que [Synchroniser et supprimer les données du catalogue]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data) pour les exigences et le comportement spécifiques aux catalogues.

Braze n'impose pas d'exigences supplémentaires en matière de noms de fichiers au-delà de celles imposées par votre fournisseur de stockage de fichiers. Les noms de fichiers doivent être uniques. Nous vous recommandons d'ajouter un horodatage pour garantir l'unicité.

Pour obtenir des exemples de tous les types de fichiers pris en charge (attributs, événements personnalisés, achats, catalogues et suppressions d'utilisateurs), consultez les fichiers d'exemple dans [braze-examples](https://github.com/braze-inc/braze-examples/tree/main/cloud-data-ingestion/braze-examples/payloads/file_storage).

### Identifiants des utilisateurs {#user-identifiers}

Pour les synchronisations de données utilisateur (attributs, événements personnalisés, événements d'achat), chaque ligne de votre fichier source doit contenir exactement un identifiant utilisateur et une colonne `payload`. Un fichier source peut contenir des lignes avec différents types d'identifiants, mais chaque ligne individuelle ne doit en utiliser qu'un seul.

| Identifiant | Description |
| --- | --- |
| `EXTERNAL_ID` | Identifie l'utilisateur que vous souhaitez mettre à jour. Doit correspondre à la valeur `external_id` utilisée dans Braze. |
| `ALIAS_NAME` et `ALIAS_LABEL` | Ces deux colonnes créent un objet alias d'utilisateur. `alias_name` doit être un identifiant unique et `alias_label` spécifie le type d'alias. Les utilisateurs peuvent avoir plusieurs alias avec des libellés différents, mais un seul `alias_name` par `alias_label`. |
| `BRAZE_ID` | L'identifiant utilisateur Braze. Celui-ci est généré par le SDK de Braze, et il n'est pas possible de créer de nouveaux utilisateurs à l'aide d'un ID Braze via l'Ingestion de données cloud. Pour créer de nouveaux utilisateurs, spécifiez un ID externe ou un alias d'utilisateur. |
| `EMAIL` | L'adresse e-mail de l'utilisateur. S'il existe plusieurs profils avec la même adresse e-mail, le profil mis à jour le plus récemment sera prioritaire. Si vous indiquez à la fois l'e-mail et le téléphone, Braze utilisera l'e-mail comme identifiant principal. |
| `PHONE` | Le numéro de téléphone de l'utilisateur. S'il existe plusieurs profils avec le même numéro de téléphone, le profil mis à jour le plus récemment sera prioritaire. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Identifiants des utilisateurs" }

En plus d'un identifiant, chaque ligne doit contenir une colonne `payload` avec une chaîne JSON des champs que vous souhaitez synchroniser avec l'utilisateur dans Braze.

{% alert note %}
Contrairement aux sources d'entrepôt de données, la colonne `UPDATED_AT` n'est ni requise ni prise en charge pour les synchronisations de stockage de fichiers.
{% endalert %}

### Identifiants de catalogue {#catalog-identifiers}

Pour les synchronisations de catalogue, votre fichier source doit contenir les colonnes suivantes. Les fichiers de catalogue utilisent des identifiants différents de ceux des fichiers de données utilisateur.

| Colonne | Requis | Description |
| --- | --- | --- |
| `ID` | Oui | L'identifiant unique de l'élément de catalogue. Utilisé pour créer, mettre à jour ou supprimer l'élément dans Braze. |
| `payload` | Oui | Une chaîne JSON des champs et valeurs du catalogue à synchroniser. Doit correspondre au schéma de votre catalogue dans Braze. |
| `DELETED` | Non | Lorsque la valeur est `true`, l'élément de catalogue correspondant à l'`ID` est supprimé du catalogue dans Braze. Omettez cette colonne ou définissez-la sur `false` pour les opérations de création ou de mise à jour. |
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
Incluez une colonne `DELETED` facultative. Lorsque `DELETED` est `true`, cet élément de catalogue est supprimé du catalogue dans Braze. Pour la liste complète des colonnes requises, consultez [Identifiants de catalogue](#catalog-identifiers). Pour le comportement de suppression, consultez [Suppression d'éléments de catalogue](#deleting-catalog-items). Pour un flux de configuration de catalogue de bout en bout (y compris la création du catalogue cible et le comportement de synchronisation), consultez [Synchroniser et supprimer les données du catalogue]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data).
{% endtab %}

{% endtabs %}

## Suppression des données {#deleting-data}

L'Ingestion de données cloud pour le stockage de fichiers prend en charge la suppression d'utilisateurs et d'éléments de catalogue via le téléchargement de fichiers. Utilisez des synchronisations et des formats de fichiers distincts pour chaque type.

- **[Suppression d'utilisateurs](#deleting-users)** – Créez une synchronisation avec le type de données **Supprimer les utilisateurs** et téléchargez des fichiers contenant uniquement les identifiants des utilisateurs (sans payload).
- **[Suppression d'éléments de catalogue](#deleting-catalog-items)** – Utilisez votre synchronisation de catalogue existante et ajoutez une colonne `deleted` (ou `DELETED`) pour marquer les éléments à supprimer.

### Suppression d'utilisateurs {#deleting-users}

Pour supprimer des profils utilisateurs dans Braze à l'aide de fichiers dans votre compartiment source :

1. Créez une nouvelle synchronisation Ingestion de données cloud (même configuration que pour les autres synchronisations).
2. Lors de la configuration de la synchronisation dans Braze, définissez le **Type de données** sur **Supprimer les utilisateurs**.
3. Téléchargez vers votre compartiment source des fichiers contenant uniquement des colonnes d'identifiant utilisateur. N'incluez pas de colonne `payload` — la synchronisation échouera si un payload est présent, afin d'éviter toute suppression accidentelle.

Chaque ligne du fichier doit identifier exactement un utilisateur à l'aide de l'un des éléments suivants :

| Identifiant | Description |
| --- | --- |
| `EXTERNAL_ID` | Correspond à l'`external_id` utilisé dans Braze. |
| `ALIAS_NAME` et `ALIAS_LABEL` | Les deux colonnes ensemble identifient l'utilisateur par son alias. |
| `BRAZE_ID` | ID utilisateur généré par Braze (utilisateurs existants uniquement). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Suppression d'utilisateurs" }

{% alert important %}
La suppression d'utilisateurs est définitive et irréversible. N'incluez que les utilisateurs que vous avez l'intention de supprimer. Pour plus d'informations, consultez [Supprimer des utilisateurs avec l'Ingestion de données cloud]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/delete_users).
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

Lorsque la synchronisation s'exécute, Braze traite les nouveaux fichiers dans le compartiment et supprime les profils utilisateurs correspondants.

### Suppression d'éléments de catalogue {#deleting-catalog-items}

Pour supprimer des éléments d'un catalogue à l'aide du stockage de fichiers :

1. Utilisez la même synchronisation que celle utilisée pour [synchroniser les données du catalogue]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data) (type de données **Catalogues**).
2. Dans vos fichiers CSV ou JSON, ajoutez une colonne facultative **`deleted`** (ou **`DELETED`**).
3. Définissez `deleted` sur `true` pour tout élément de catalogue que vous souhaitez supprimer du catalogue dans Braze.

Chaque ligne nécessite toujours `ID` et `payload`. Pour les lignes marquées pour suppression, le payload peut être minimal ; Braze supprime l'élément par `ID`.

**Exemple – JSON (suppression d'un élément de catalogue) :**
```jsonl
{"id":"85","payload":"{\"product_name\": \"Product 85\", \"price\": 85.85}"}
{"id":"1","payload":"{\"product_name\": \"Product 1\", \"price\": 1.01}","deleted":true}
```

**Exemple – CSV (suppression d'un élément de catalogue) :**
```plaintext
ID,PAYLOAD,DELETED
85,"{""product_name"": ""Product 85"", ""price"": 85.85}",false
1,"{""product_name"": ""Product 1"", ""price"": 1.01}",true
```

Lorsque la synchronisation s'exécute, les lignes contenant `deleted: true` entraînent la suppression de l'élément de catalogue correspondant dans Braze. Pour en savoir plus sur le comportement de synchronisation et de suppression des catalogues, consultez [Synchroniser et supprimer les données du catalogue]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data).

## Bon à savoir {#things-to-know}

- Les fichiers ajoutés au compartiment source ne doivent pas dépasser 512&nbsp;Mo. Cette limite s'applique à Amazon S3 et à Google Cloud Storage. Les fichiers de plus de 512&nbsp;Mo entraîneront une erreur et ne seront pas synchronisés vers Braze.
- Bien qu'il n'y ait pas de limite supplémentaire au nombre de lignes par fichier, nous vous recommandons d'utiliser des fichiers plus petits pour accélérer vos synchronisations. Par exemple, l'ingestion d'un fichier de 500&nbsp;Mo prendrait beaucoup plus de temps que celle de cinq fichiers distincts de 100&nbsp;Mo.
- Il n'y a pas de limite supplémentaire au nombre de fichiers téléchargés dans un temps donné.
- L'ordonnancement n'est pas pris en charge au sein des fichiers ni entre les fichiers. Nous vous recommandons de regrouper les mises à jour périodiquement si vous surveillez d'éventuelles conditions de concurrence.

## Résolution des problèmes {#troubleshooting}

### Téléchargement et traitement des fichiers {#uploading-files-and-processing}

CDI ne traite que les fichiers ajoutés après la création de la synchronisation. Au cours de ce processus, Braze recherche les nouveaux fichiers ajoutés, ce qui déclenche une nouvelle notification. Cela lance une nouvelle synchronisation pour traiter le nouveau fichier. Pour Amazon S3, la notification est un message vers SQS. Pour Google Cloud Storage, il s'agit d'un message `OBJECT_FINALIZE` vers Pub/Sub.

Vous pouvez utiliser les fichiers existants pour vérifier que Braze peut accéder à votre compartiment et détecter les fichiers à ingérer, mais ils ne sont pas synchronisés vers Braze. Pour que CDI puisse les traiter, vous devez télécharger à nouveau vers le compartiment source tous les fichiers existants que vous souhaitez synchroniser.

### Gestion des erreurs de fichiers inattendues (Amazon S3) {#handling-unexpected-file-errors-amazon-s3}

Si vous observez un nombre élevé d'erreurs ou de fichiers en échec, il se peut qu'un autre processus ajoute des fichiers au compartiment S3 dans un dossier autre que le dossier cible pour CDI.

Lorsque des fichiers sont téléchargés dans le compartiment source mais pas dans le dossier source, CDI traite la notification SQS mais n'entreprend aucune action sur le fichier, ce qui peut apparaître comme une erreur.

Si votre problème est lié aux notifications S3 ou aux autorisations de destination SQS (par exemple, des erreurs de validation de destination), consultez la documentation AWS :

- [Activation et configuration des notifications d'événements à l'aide de la console Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/enable-event-notifications.html)
- [Octroi d'autorisations pour publier des messages de notification d'événements vers une destination](https://docs.aws.amazon.com/AmazonS3/latest/userguide/grant-destinations-permissions-to-s3.html)
- [Résolution des problèmes dans Amazon SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-troubleshooting.html)

### Gestion des erreurs de fichiers inattendues (Google Cloud Storage) {#handling-unexpected-file-errors-google-cloud-storage}

Comme pour Amazon S3, CDI ne traite que les fichiers téléchargés après la création de la synchronisation. Chaque nouvel objet déclenche un message `OBJECT_FINALIZE` vers votre topic Pub/Sub. Pour ingérer des fichiers qui existent déjà dans le compartiment, téléchargez-les à nouveau.

Si les fichiers ne sont pas ingérés, vérifiez les points suivants :

- La notification du compartiment existe. Listez les notifications du compartiment avec `gcloud storage buckets notifications list gs://YOUR-BUCKET-NAME`.
- L'agent de service Cloud Storage dispose du rôle `roles/pubsub.publisher` sur le topic.
- Le compte de service Braze dispose de l'autorisation de consommer l'abonnement (`pubsub.subscriptions.consume`, accordée via le rôle personnalisé ou `roles/pubsub.subscriber`).

Pour plus d'informations, consultez [Notifications Pub/Sub pour Cloud Storage](https://cloud.google.com/storage/docs/pubsub-notifications) dans la documentation Google Cloud.