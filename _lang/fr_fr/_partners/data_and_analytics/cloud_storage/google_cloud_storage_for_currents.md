---
nav_title: Google Cloud Storage
article_title: Google Cloud Storage
alias: /partners/google_cloud_storage_for_currents/
description: "Cet article de référence présente le partenariat entre Braze et Google Cloud Storage, une solution de stockage d'objets très évolutive pour les données non structurées."
page_type: partner
tool: Currents
search_tag: Partner

---

# Google Cloud Storage

> [Google Cloud Storage](https://cloud.google.com/storage/) est un système de stockage d'objets très évolutif pour les données non structurées proposé par Google dans la suite de produits Cloud Computing.

{% alert important %}
Si vous passez d'un fournisseur de stockage en nuage à un autre, contactez votre gestionnaire de la satisfaction client Braze pour obtenir de l'aide sur la configuration et la validation de votre nouvelle intégration.
{% endalert %}

L'intégration de Braze et Google Cloud Storage vous permet de transmettre en continu les données Currents vers Google Cloud Storage. Vous pouvez par la suite utiliser un processus ETL (extraction, transformation et chargement) pour transférer vos données vers d'autres emplacements, comme Google BigQuery.

## Prérequis {#prerequisites}

| Condition | Description |
| ----------- | ----------- |
| Compte Google Cloud Storage | Un compte Google Cloud Storage est requis pour tirer parti de ce partenariat. |
| Currents | Pour exporter des données vers Google Cloud Storage, vous devez avoir configuré [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents#access-currents) pour votre compte. Currents n'est pas requis si vous configurez uniquement l'archivage des messages. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prérequis" }

## Intégration {#integration}

Pour intégrer Google Cloud Storage, vous devez configurer les identifiants appropriés permettant à Braze d'obtenir des informations sur les compartiments de stockage utilisés pour l'écriture (`storage.buckets.get`) et de créer des objets dans ce compartiment (`storage.objects.create`).

{% alert note %}
Workload Identity Federation (WIF) n'est pas pris en charge comme méthode d'authentification pour Currents. Vous devez utiliser un compte de service avec une clé privée JSON.
{% endalert %}

Pour ce faire, suivez les instructions ci-dessous, qui vous guideront dans la création d'un rôle et d'un compte de service générant une clé privée à utiliser dans votre intégration Currents.

### Étape 1 : Créer un rôle {#step-1-create-role}

Créez un nouveau rôle dans votre console Google Cloud Platform en accédant à **IAM & admin** > **Roles** > **+ Create Role**.

![Page des rôles IAM de Google Cloud avec l'action Create Role.]({% image_buster /assets/img/gcs1.png %})

Donnez un nom au rôle, puis sélectionnez **+Add Permissions** et choisissez les éléments suivants :

- `storage.objects.create`
- `storage.objects.delete`
- `storage.objects.list`
- `storage.objects.get`
- `storage.buckets.get`

{% alert note %}
La permission `storage.objects.delete` est facultative. Elle permet à Braze de nettoyer les fichiers incomplets.<br><br>Dans de rares cas, Google Cloud peut interrompre les connexions prématurément, ce qui amène Braze à écrire des fichiers incomplets dans Google Cloud Storage. Dans la plupart des cas, Braze réessaiera et créera un nouveau fichier avec les données correctes, laissant l'ancien fichier dans Google Cloud Storage.
{% endalert %}

{% alert important %}
Si votre compartiment utilise un [espace de noms hiérarchique](https://cloud.google.com/storage/docs/hns-overview), vous devez également ajouter la permission `storage.folders.create`. Sur ces compartiments, les dossiers sont des ressources gérées, et Braze a donc besoin de cette permission pour créer la structure de dossiers de vos fichiers exportés. Sans elle, Braze ne peut pas écrire dans le compartiment et l'intégration ne parvient pas à exporter les données.
{% endalert %}

Lorsque vous avez terminé, sélectionnez **Create**.

![Éditeur de rôle personnalisé Google Cloud avec les permissions de stockage sélectionnées.]({% image_buster /assets/img/gcs2.png %})

### Étape 2 : Créer un nouveau compte de service {#step-2-create-a-new-service-account}

#### Étape 2.1 : Créer le compte de service {#step-21-create-the-service-account}

Créez un nouveau compte de service dans votre console Google Cloud Platform en accédant à **IAM & admin** > **Service Accounts** et en sélectionnant **Create Service Account**.

![Page des comptes de service Google Cloud avec Create Service Account sélectionné.]({% image_buster /assets/img/gcs3.png %})

Ensuite, donnez un nom au compte de service et accordez-lui l'accès à votre rôle personnalisé nouvellement créé.

![Dans Google Cloud Platform, sur la page de création de services, saisissez le nom de votre rôle dans le champ « Select a Role ».]({% image_buster /assets/img/gcs4.png %})

#### Étape 2.2 : Créer une clé {#step-22-create-a-key}

En bas de la page, utilisez le bouton **Create Key** pour créer une clé privée **JSON** à utiliser dans Braze. Une fois la clé créée, elle sera téléchargée sur votre machine.

![Boîte de dialogue de création de clé de compte de service Google Cloud configurée sur le type de clé JSON.]({% image_buster /assets/img/gcs5.png %})

### Étape 3 : Configurer Currents dans Braze {#step-3-set-up-currents-in-braze}

Dans Braze, accédez à **Currents** > **+ Create Current** > **Google Cloud Storage Data Export** et fournissez le nom de votre intégration ainsi qu'une adresse e-mail de contact.

Ensuite, téléversez votre clé privée JSON sous **GCS JSON Credentials** et indiquez le nom de votre compartiment GCS ainsi que le préfixe GCS (facultatif). Notez que vous devez générer ces identifiants via Google Cloud Platform, comme décrit dans les étapes précédentes.

{% alert important %}
Il est important de maintenir votre fichier d'identifiants à jour ; si les identifiants de votre connecteur expirent, le connecteur cessera d'envoyer des événements. Si cette situation persiste pendant plus de **5 jours**, les événements du connecteur seront supprimés et les données seront définitivement perdues.
{% endalert %}

![La page Google Cloud Storage Currents dans Braze. Cette page contient des champs pour le nom de l'intégration, l'adresse e-mail de contact, les identifiants JSON GCS, le nom du compartiment GCS et le préfixe.]({% image_buster /assets/img/gcs6.png %})

Enfin, faites défiler jusqu'en bas de la page et sélectionnez les événements d'engagement lié aux messages ou les événements de comportement client que vous souhaitez exporter. Une fois terminé, lancez votre Current.

### Étape 4 : Configurer les exportations Google Cloud Storage {#step-4-set-up-google-cloud-storage-exports}

Pour configurer les exportations Google Cloud Storage (GCS), accédez à **Technology Partners** > **Google Cloud Storage**, saisissez vos identifiants GCS et sélectionnez **Make this the default data export destination**.

Gardez à l'esprit que l'organisation et le contenu de tous les fichiers exportés seront identiques entre les intégrations AWS S3, Microsoft Azure et Google Cloud Storage.

{% alert important %}
Veillez à saisir la valeur JSON complète [générée par Google Cloud](https://cloud.google.com/iam/docs/keys-create-delete).
{% endalert %}

![La page Google Cloud Storage dans le tableau de bord de Braze.]({% image_buster /assets/img/gcs7.png %}){: style="max-width:70%;"}

### Étape 5 : Tester les identifiants de votre compte de service (facultatif) {#step-5-test-your-service-account-credentials-optional}

Votre compte de service Google Cloud IAM doit disposer des permissions suivantes :

- `storage.objects.create`
- `storage.objects.delete`
- `storage.objects.list`
- `storage.objects.get`
- `storage.buckets.get`

Pour vérifier ces permissions dans le tableau de bord de Braze, accédez à la page **Google Cloud Storage**, puis sélectionnez **Test Credentials**.

![La section des identifiants Google Cloud Storage dans le tableau de bord de Braze.]({% image_buster /assets/img/gcs8.png %}){: style="max-width:70%;"}

## Comportement d'exportation {#export-behavior}

Les utilisateurs qui ont intégré une solution de stockage de données dans le cloud et qui tentent d'exporter des API, des rapports de tableau de bord ou des rapports CSV constateront le comportement suivant :

- Toutes les exportations d'API ne renverront pas d'URL de téléchargement dans le corps de la réponse et devront être récupérées via le stockage de données.
- Tous les rapports de tableau de bord et les rapports CSV seront envoyés par e-mail à l'utilisateur pour téléchargement (aucune autorisation de stockage requise) et sauvegardés sur le stockage de données.

{% alert important %}
**Exigence de format JSON** : Pour les exportations JSON, Braze utilise le format JSONL (JSON délimité par des sauts de ligne), où chaque ligne contient un objet JSON distinct. Ce format diffère du JSON standard, qui est un tableau ou un objet JSON unique. Chaque ligne du fichier exporté est un objet JSON valide, mais le fichier dans son ensemble n'est pas un document JSON valide unique. Lors du traitement de ces fichiers, analysez chaque ligne individuellement en tant qu'objet JSON distinct plutôt que de tenter d'analyser l'ensemble du fichier comme un seul document JSON.

Les exportations Currents utilisent le format Apache Avro (fichiers `.avro`), et non JSON. Cette exigence de format JSON s'applique aux exportations de données du tableau de bord et aux exportations d'API qui utilisent le format JSON.
{% endalert %}

## Résolution des problèmes {#troubleshooting}

### Les identifiants Google Cloud Storage ne sont pas valides {#google-cloud-storage-credentials-are-invalid}

Si vous recevez l'erreur suivante lorsque vous tentez de saisir vos identifiants :

```
Google Cloud Storage Credentials are invalid. Please ensure that your credentials string, bucket name, and prefix are valid. You do not have read permission.
```

Assurez-vous que votre compte de service Google Cloud IAM dispose des autorisations suivantes :

- `storage.objects.create`
- `storage.objects.delete`
- `storage.objects.list`
- `storage.objects.get`
- `storage.buckets.get`

Après vérification, vous pouvez [tester vos identifiants dans le tableau de bord de Braze](#step-5-test-your-service-account-credentials-optional).