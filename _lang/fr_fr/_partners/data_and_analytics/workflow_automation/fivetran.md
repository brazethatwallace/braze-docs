---
nav_title: Fivetran
article_title: Fivetran
alias: /partners/fivetran/
description: "Cet article de référence présente le partenariat entre Braze et Fivetran, un outil d'automatisation des flux de travail qui peut vous aider dans la prise de décision adossée aux données en fournissant des données prêtes à être interrogées dans votre entrepôt cloud."
page_type: partner
search_tag: Partner
tool: Currents

---

# Fivetran

> [Fivetran](https://fivetran.com/) est une marque mondialement reconnue dont les produits axés sur l'analyse et les pipelines entièrement gérés permettent de prendre des décisions fondées sur des données en fournissant des données prêtes à être interrogées dans votre entrepôt cloud.

L'intégration de Braze et Fivetran permet aux utilisateurs de créer un pipeline sans maintenance qui vous permet de collecter et d'analyser les données de Braze en connectant toutes vos applications et bases de données à un entrepôt central. Une fois les données collectées dans l'entrepôt central, les équipes chargées des données peuvent explorer efficacement les données de Braze à l'aide de leurs outils d'aide à la décision préférés.

## Conditions préalables {#prerequisites}

| Condition | Description |
| ----------- | ----------- |
| Compte Fivetran | Un compte [Fivetran](https://fivetran.com/login?next=%2Fdashboard) est nécessaire pour bénéficier de ce partenariat. |
| Clé API REST Braze | Une clé API REST de Braze avec les autorisations suivantes :<br>- users.export.ids<br>- users.export.segment<br>- email.unsubscribe<br>- email.hard_bounces<br>- messages.schedule_broadcasts<br>- campaigns.list<br>- campaigns.details<br>- canvas.list<br>- canvas.details<br>- segments.list<br>- segments.details<br>- purchases.product_list<br>- events.list<br>- feed.list<br>- feed.details<br>- templates.email.info<br>- templates.email.list<br>- subscription.status.get<br>- subscription.groups.get <br><br> Celle-ci peut être créée dans le tableau de bord de Braze à partir de **Settings** > **API Keys**. |
| Endpoint REST Braze  | L'URL de votre endpoint REST. Votre endpoint dépendra de l'[URL de Braze pour votre instance]({{site.baseurl}}/api/basics/#api-definitions). |
| Braze Currents | [Braze Currents](https://www.braze.com/product/data-agility-management/currents/) doit être connecté à Amazon S3 ou à Google Cloud Storage. |
| Amazon S3 ou Google Cloud Storage | Cette intégration nécessite que vous ayez accès à un service Amazon S3 ou à Google Cloud Storage. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Intégration {#integration}

L'intégration Currents suivante est prise en charge pour [Amazon S3](#setting-up-braze-currents-for-s3) et [Google Cloud Storage](#setting-up-braze-currents-for-google-cloud-storage).

### Configuration de Braze Currents pour S3 {#setting-up-braze-currents-for-s3}

#### Étape 1 : Rechercher votre ID externe {#step-one}

Dans le [tableau de bord Fivetran](https://fivetran.com/dashboard), sélectionnez **+ Connector**, puis le connecteur **Braze** pour lancer le formulaire de configuration. Ensuite, sélectionnez **Amazon S3**. Notez l'ID externe fourni ici ; vous en aurez besoin pour permettre à Fivetran d'accéder à votre compartiment S3.

![Le formulaire de configuration du connecteur Braze dans Fivetran. Le champ de l'ID externe nécessaire à cette étape est situé au milieu de la page dans un encadré gris clair.]({% image_buster /assets/img/fivetran_braze_setupform_as3.png %})

#### Étape 2 : Donner à Fivetran l'accès à un compartiment S3 spécifié {#step-2-give-fivetran-access-to-a-specified-s3-bucket}

##### Création d'une politique IAM {#creating-an-iam-policy}

Ouvrez la [console Amazon IAM](https://console.aws.amazon.com/iam/home#home) et accédez à **Policies > Create Policy**.

![Console Amazon IAM avec la liste des politiques.]({% image_buster /assets/img/fivetran_as3_iam.png %})

Ensuite, ouvrez l'onglet **JSON** et collez la politique suivante. Veillez à remplacer `{your-bucket-name}` par le nom de votre compartiment S3.

{% raw %}
```json
{
"Version": "2012-10-17",
"Statement": [
    {
      "Effect": "Allow",
      "Action": [
"s3:Get*",
"s3:List*"
      ],
      "Resource": "arn:aws:s3:::{your-bucket-name}/*"
    },
    {
      "Effect": "Allow",
      "Action": [
"s3:Get*",
"s3:List*"
      ],
      "Resource": "arn:aws:s3:::{your-bucket-name}"
    }
  ]
}
```
{% endraw %}

Enfin, sélectionnez **Review Policy** et donnez à la politique un nom et une description uniques. Sélectionnez **Create Policy** pour créer votre politique.

![Champs permettant de nommer la politique et d'en fournir une description.]({% image_buster /assets/img/fivetran_iam_policy_meta.png %})

##### Créer un rôle IAM {#step-two}

Dans AWS, accédez à **Roles**, puis sélectionnez **Create New Role**.

![La page « Roles » avec le bouton pour créer un nouveau rôle.]({% image_buster /assets/img/fivetran_iam_new_role.png %})

Sélectionnez **Another AWS Account** et indiquez l'ID du compte Fivetran `834469178297`. Veillez à cocher la case **Require external ID**. Vous y indiquerez l'ID externe trouvé à l'étape 1.

![Le champ pour saisir votre « Account ID », une case à cocher pour exiger l'ID externe, et une zone de texte vide pour saisir votre « External ID ».]({% image_buster /assets/img/fivetran_another_aws_account.png %})

Ensuite, sélectionnez **Next: Permissions** pour sélectionner la politique que vous venez de créer.

![Liste des politiques.]({% image_buster /assets/img/fivetran_as3_select_policy.png %})

Sélectionnez **Next: Review**, donnez un nom à votre nouveau rôle (par exemple Fivetran) et sélectionnez **Create Role**. Une fois le rôle créé, sélectionnez-le et notez l'ARN du rôle affiché.

![L'ARN Amazon S3 répertorié dans le rôle.]({% image_buster /assets/img/fivetran_iam_role_arn.png %})

{% alert note %}
Vous pouvez spécifier des autorisations pour l'ARN de rôle que vous désignez pour Fivetran. L'attribution d'autorisations sélectives à ce rôle permet à Fivetran de synchroniser uniquement ce qu'il a le droit de voir.
{% endalert %}

#### Étape 3 : Compléter le connecteur Fivetran {#step-3-complete-the-fivetran-connector}

Dans Fivetran, sélectionnez **+ Connector**, puis le connecteur **Braze** pour lancer le formulaire de configuration. Dans le formulaire, remplissez les champs avec les valeurs appropriées :
- `Destination schema` : un nom de schéma unique.
- `API URL` : votre endpoint REST API de Braze.
- `API Key` : votre clé API REST de Braze.
- `External ID` : l'ID externe défini à l'[étape 2](#step-two) des instructions de configuration de Currents. Cet ID est une valeur fixe.
- `Bucket` : vous le trouverez dans votre compte Braze en accédant à **Partner Integrations** > **Data Export** > le nom de votre Current.
- `Role ARN` : l'ARN du rôle se trouve à l'[étape 1](#step-one) des instructions de configuration de Current.

{% alert important %}
Assurez-vous qu'**Amazon S3** est sélectionné comme choix de **Cloud Storage**.
{% endalert %}

Enfin, sélectionnez **Save & Test**, et Fivetran fera le reste en se synchronisant avec les données de votre compte Braze !

### Configuration de Braze Currents pour Google Cloud Storage {#setting-up-braze-currents-for-google-cloud-storage}

#### Étape 1 : Récupérer votre adresse e-mail Fivetran depuis Google Cloud Storage {#step-one2}

Dans le [tableau de bord Fivetran](https://fivetran.com/dashboard), sélectionnez **+ Connector**, puis le connecteur **Braze** pour lancer le formulaire de configuration. Ensuite, sélectionnez **Google Cloud Storage**. Notez l'adresse e-mail qui apparaît.

![Le formulaire de configuration du connecteur Braze dans Fivetran. Le champ e-mail nécessaire à cette étape est situé au milieu de la page dans un encadré gris clair.]({% image_buster /assets/img/fivetran_braze_setupform_gcs.png %})

#### Étape 2 : Accorder l'accès au compartiment {#step-2-grant-bucket-access}

Accédez à votre [Google Storage Console](https://console.cloud.google.com/storage/browser) et sélectionnez le compartiment avec lequel vous avez configuré Braze Currents, puis sélectionnez **Edit bucket permissions**.

![Les compartiments disponibles dans la console Google Storage. Localisez un compartiment et sélectionnez l'icône verticale à trois points pour ouvrir le menu déroulant qui vous permet de modifier les autorisations du compartiment.]({% image_buster /assets/img/fivetran_edit_bucket_permissions_gcs.png %})

Ensuite, accordez l'accès `Storage Object Viewer` à l'adresse e-mail de l'[étape 1](#step-one2) en ajoutant l'e-mail en tant que membre. Notez le nom du compartiment ; vous en aurez besoin à l'étape suivante pour configurer Fivetran.

![Compartiment avec autorisations.]({% image_buster /assets/img/fivetran_add_members_gcs.png %})

#### Étape 3 : Compléter le connecteur Fivetran

Dans Fivetran, sélectionnez **+ Connector**, puis le connecteur **Braze** pour lancer le formulaire de configuration. Dans le formulaire, remplissez les champs avec les valeurs appropriées :
- `Destination schema` : un nom de schéma unique.
- `API URL` : votre endpoint REST API de Braze.
- `API Key` : votre clé API REST de Braze.
- `Bucket Name` : vous le trouverez dans votre compte Braze en accédant à **Partner Integrations** > **Data Export** > le nom de votre Current.
- `Folder` : vous le trouverez dans votre compte Braze en accédant à **Partner Integrations** > **Data Export** > le nom de votre Current.

{% alert important %}
Assurez-vous que **Google Cloud Storage** est sélectionné comme choix de **Cloud Storage**.
{% endalert %}

Enfin, sélectionnez **Save & Test**, et Fivetran fera le reste en se synchronisant avec les données de votre compte Braze !