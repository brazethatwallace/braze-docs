---
nav_title: Amazon S3
article_title: Amazon S3
alias: /partners/amazon_s3/
description: "Cet article de référence présente le partenariat entre Braze et Amazon S3, un système de stockage hautement évolutif proposé par Amazon Web Services."
page_type: partner
search_tag: Partner

---

# Amazon S3

> [Amazon S3](https://aws.amazon.com/s3/) est un système de stockage hautement évolutif proposé par Amazon Web Services.

{% alert important %}
Si vous passez d'un fournisseur de stockage cloud à un autre, contactez votre gestionnaire du succès des clients Braze pour obtenir de l'aide sur la configuration et la validation de votre nouvelle intégration.
{% endalert %}

L'intégration de Braze et d'Amazon S3 propose deux stratégies d'intégration :

- Tirez parti de [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents), qui vous permet d'y stocker des données jusqu'à ce que vous souhaitiez les connecter à d'autres plateformes, outils et emplacements.
- Utilisez les exportations de données du tableau de bord (telles que les exportations CSV et les rapports d'engagement).

## Conditions préalables {#prerequisites}

| Condition | Description |
| ----------- | ----------- |
| Compte Amazon S3 | Vous devez disposer d'un compte Amazon S3 pour profiter de ce partenariat. |
| Compartiment S3 dédié | Avant d'intégrer Amazon S3, vous devez créer un compartiment S3 pour votre application.<br><br>Si vous disposez déjà d'un compartiment S3, nous vous recommandons tout de même d'en créer un nouveau spécifiquement pour Braze afin de pouvoir limiter les autorisations. Reportez-vous aux instructions suivantes pour savoir comment créer un nouveau compartiment. |
| Currents | Pour réexporter des données vers Amazon S3, vous devez avoir configuré [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents#access-currents) pour votre compte. Currents n'est pas nécessaire si vous ne configurez que l'archivage des messages. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Création d'un nouveau compartiment S3 {#creating-a-new-s3-bucket}

Pour créer un compartiment pour votre application, procédez comme suit :

1. Ouvrez la [console Amazon S3](https://console.aws.amazon.com/s3/) et suivez les instructions pour vous **connecter** ou **créer un compte avec AWS**.
2. Après vous être connecté, sélectionnez **S3** dans la catégorie **Storage & Content Delivery**.
3. Sélectionnez **Create Bucket** dans l'écran suivant.
4. Lorsque vous y êtes invité, créez votre compartiment et sélectionnez une région AWS.

Braze ne vous permet pas de choisir ou de configurer une région dans le tableau de bord. La région AWS est déterminée par l'endroit où vous créez le compartiment dans la console AWS. L'intégration envoie les données au nom de compartiment que vous fournissez, et AWS achemine automatiquement les requêtes vers la région du compartiment. Si votre connecteur tente de se connecter à une région différente de celle souhaitée (par exemple, `eu-west-1` au lieu de `eu-central-1`), créez ou utilisez un compartiment S3 dans la région souhaitée dans AWS. Il n'y a rien à modifier du côté de Braze.

{% alert note %}
Currents ne prend pas en charge les compartiments dont le [verrouillage d'objet](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html) est configuré.
{% endalert %}

## Intégration {#integration}

Braze dispose de deux stratégies d'intégration différentes avec Amazon S3 : l'une pour [Braze Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) et l'autre pour toutes les exportations de données du tableau de bord (telles que les exportations CSV ou les rapports d'engagement). Les deux intégrations prennent en charge deux méthodes d'authentification ou d'autorisation différentes :

- [Méthode de clé d'accès secrète AWS](#aws-secret-key-auth-method)
- [Méthode ARN de rôle AWS](#aws-role-arn-auth-method)

## Méthode d'authentification par clé secrète AWS {#aws-secret-key-auth-method}

Cette méthode d'authentification génère une clé secrète et un ID de clé d'accès qui permet à Braze de s'authentifier en tant qu'utilisateur sur votre compte AWS pour écrire des données dans votre compartiment.

### Étape 1 : Créer un utilisateur {#secret-key-1}

{% alert note %}
Si vous ne configurez que l'archivage des messages, suivez les étapes de l'onglet **Dashboard Data Export**.
{% endalert %}

Pour récupérer votre ID de clé d'accès et votre clé d'accès secrète, [créez un utilisateur IAM et un groupe d'administrateurs dans AWS](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-admin-group.html).

### Étape 2 : Obtenir les identifiants {#secret-key-2}

Après avoir créé un nouvel utilisateur, sélectionnez **Show User Security Credentials** pour afficher votre ID de clé d'accès et votre clé d'accès secrète. Ensuite, notez ces identifiants quelque part ou sélectionnez le bouton **Download Credentials**, car vous devrez les saisir ultérieurement dans le tableau de bord de Braze.

![Page des identifiants de sécurité de l'utilisateur AWS IAM affichant l'ID de clé d'accès et la clé d'accès secrète.]({% image_buster /assets/img_archive/S3_Credentials.png %})

### Étape 3 : Créer une politique {#secret-key-3}

Accédez à **Policies** > **Get Started** > **Create Policy** pour ajouter des autorisations pour votre utilisateur. Ensuite, sélectionnez **Create Your Own Policy**. Cela accorde des autorisations limitées, de sorte que Braze ne peut accéder qu'aux compartiments spécifiés.

![Écran de création de politique AWS IAM avec les options de politique pour l'intégration S3.]({% image_buster /assets/img_archive/S3_CreatePolicy.png %})

{% alert note %}
Des politiques différentes sont nécessaires pour Currents et l'exportation de données du tableau de bord. `s3:GetObject` est nécessaire pour permettre au backend de Braze de gérer les erreurs.
{% endalert %}

Spécifiez le nom de politique de votre choix et saisissez l'extrait de code suivant dans la section **Policy Document**. Veillez à remplacer `INSERTBUCKETNAME` par le nom de votre compartiment. Sans ces autorisations, l'intégration échoue à la vérification des identifiants et n'est pas créée.

{% alert note %}
Si vous ne configurez que l'archivage des messages, utilisez l'extrait de code de l'onglet **Dashboard Data Export**.
{% endalert %}

{% tabs %}
{% tab Braze Currents %}
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["s3:ListBucket", "s3:GetBucketLocation"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME"]
        },
        {
            "Effect": "Allow",
            "Action": ["s3:PutObject", "s3:GetObject"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME/*"]
        }
    ]
}
```
{% endtab %}
{% tab Dashboard Data Export %}
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["s3:ListBucket", "s3:GetBucketLocation"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME"]
        },
        {
            "Effect": "Allow",
            "Action": ["s3:GetObject", "s3:PutObject", "s3:DeleteObject"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME*", "arn:aws:s3:::INSERTBUCKETNAME/", "arn:aws:s3:::INSERTBUCKETNAME"]
        }
    ]
}
```
{% endtab %}
{% endtabs %}

### Étape 4 : Joindre la politique {#secret-key-4}

Après avoir créé une nouvelle politique, accédez à **Users** et sélectionnez votre utilisateur spécifique. Dans l'onglet **Permissions**, sélectionnez **Attach Policy**, puis la nouvelle politique que vous avez créée. Vous êtes maintenant prêt à lier vos identifiants AWS à votre compte Braze.

![Onglet des autorisations de l'utilisateur AWS IAM avec l'action Attach Policy sélectionnée.]({% image_buster /assets/img_archive/S3_AttachPolicy.png %})

### Étape 5 : Lier Braze à AWS {#secret-key-5}

{% alert note %}
Si vous ne configurez que l'archivage des messages, suivez les étapes de l'onglet **Dashboard Data Export**.
{% endalert %}

{% tabs %}
{% tab Braze Currents %}

Dans Braze, accédez à **Partner Integrations** > **Currents**.

Ensuite, sélectionnez **Create New Current** puis **Amazon S3 Data Export**.

Nommez votre Current. Dans la section **Credentials**, assurez-vous que l'option **AWS Secret Access Key** est sélectionnée, puis saisissez votre ID d'accès S3, votre clé d'accès secrète AWS et le nom du compartiment S3 AWS dans les champs désignés.

![Formulaire de création d'un nouveau Current Braze pour Amazon S3 avec les champs d'identifiants de clé secrète AWS.]({{site.baseurl}}/assets/img/currents-s3-example.png)

{% alert warning %}
Maintenez à jour votre ID de clé d'accès AWS et votre clé d'accès secrète. Si les identifiants de votre connecteur expirent, le connecteur cesse d'envoyer des événements. Si cette situation persiste pendant plus de **5 jours**, les événements du connecteur sont abandonnés et les données sont définitivement perdues.
{% endalert %}

Vous pouvez également ajouter les personnalisations suivantes en fonction de vos besoins :

- **Chemin d'accès au dossier :** La valeur par défaut est `currents`. Si ce dossier n'existe pas, Braze le crée automatiquement pour vous.
- **Chiffrement AES-256 côté serveur, au repos :** La valeur par défaut est OFF et inclut l'en-tête `x-amz-server-side-encryption`.

Sélectionnez **Launch Current** pour continuer.

Une notification vous indique si vos identifiants ont été validés avec succès. AWS S3 est maintenant configuré pour Braze Currents.

{% endtab %}
{% tab Dashboard Data Export %}

Dans Braze, accédez à **Partner Integrations** > **Technology Partners** et sélectionnez **Amazon S3**.

Sur la page **AWS Credentials**, assurez-vous que l'option **AWS Secret Access Key** est sélectionnée, puis saisissez votre ID d'accès AWS, votre clé d'accès secrète AWS et le nom du compartiment S3 AWS dans les champs désignés. Lorsque vous saisissez votre clé secrète, sélectionnez d'abord **Test Credentials** pour vous assurer que vos identifiants fonctionnent, puis sélectionnez **Save** en cas de succès.

![Page d'identifiants du partenaire technologique Amazon S3 dans Braze avec les actions de test et d'enregistrement.]({{site.baseurl}}/assets/img/s3_tech_partners.png)

{% alert tip %}
Vous pouvez toujours récupérer de nouveaux identifiants en accédant à votre utilisateur et en sélectionnant **Create Access Key** dans l'onglet **Security Credentials** de la console AWS.
{% endalert %}

Une notification vous indique si vos identifiants ont été validés avec succès. AWS S3 est désormais intégré à votre compte Braze.

{% endtab %}
{% endtabs %}

## Méthode d'authentification par ARN de rôle AWS {#aws-role-arn-auth-method}

Cette méthode d'authentification génère un nom de ressource Amazon (ARN) de rôle qui permet au compte Amazon de Braze de s'authentifier en tant que membre du rôle que vous avez créé pour écrire des données dans votre compartiment.

### Étape 1 : Créer une politique {#role-arn-1}

Pour commencer, connectez-vous à la console de gestion AWS en tant qu'administrateur de compte. Accédez à la section IAM de la console AWS, sélectionnez **Policies** dans la barre de navigation, puis sélectionnez **Create Policy**.

![Page des politiques AWS IAM avec le bouton Create Policy sélectionné.]({{site.baseurl}}/assets/img/create_policy_1_list.png)

{% alert note %}
Des politiques différentes sont nécessaires pour Currents et l'exportation de données du tableau de bord. `s3:GetObject` est nécessaire pour permettre au backend de Braze de gérer les erreurs.
{% endalert %}

Ouvrez l'onglet **JSON** et saisissez l'extrait de code suivant dans la section **Policy Document**. Veillez à remplacer `INSERTBUCKETNAME` par le nom de votre compartiment. Sélectionnez **Review Policy** lorsque vous avez terminé.

{% alert note %}
Si vous ne configurez que l'archivage des messages, utilisez l'extrait de code de l'onglet **Dashboard Data Export**.
{% endalert %}

{% tabs %}
{% tab Braze Currents %}

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["s3:ListBucket", "s3:GetBucketLocation"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME"]
        },
        {
            "Effect": "Allow",
            "Action": ["s3:PutObject", "s3:GetObject"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME/*"]
        }
    ]
}
```

{% endtab %}
{% tab Dashboard Data Export %}

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["s3:ListBucket", "s3:GetBucketLocation"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME"]
        },
        {
            "Effect": "Allow",
            "Action": ["s3:PutObject", "s3:GetObject","s3:DeleteObject"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME/*"]
        }
    ]
}
```

{% endtab %}
{% endtabs %}

Ensuite, donnez un nom et une description à la politique, puis sélectionnez **Create Policy**.

![Étape de révision de la politique AWS IAM avec les champs pour le nom et la description de la politique.]({{site.baseurl}}/assets/img/create_policy_3_name.png)

![Liste des politiques AWS IAM affichant la politique S3 nouvellement créée.]({{site.baseurl}}/assets/img/create_policy_4_created.png)

### Étape 2 : Créer un rôle {#role-arn-2}

Dans la même section IAM de la console, sélectionnez **Roles** > **Create Role**.

![Page des rôles AWS IAM avec le bouton Create Role sélectionné.]({{site.baseurl}}/assets/img/create_role_1_list.png)

Récupérez votre ID de compte Braze et votre ID externe à partir de votre compte Braze :

- **Currents :** Dans Braze, accédez à **Partner Integrations** > **Currents**. Ensuite, sélectionnez **Create New Current** puis **Amazon S3 Data Export**. Vous trouverez ici les identifiants nécessaires à la création de votre rôle.
- **Exportation de données du tableau de bord :** Dans Braze, accédez à **Partner Integrations** > **Technology Partners** et sélectionnez **Amazon S3**. Vous trouverez ici les identifiants nécessaires à la création de votre rôle. (Créez vos rôles ici si vous ne configurez que l'archivage des messages.)

De retour sur la console AWS, sélectionnez **Another AWS Account** comme type de sélecteur d'entité de confiance. Indiquez votre ID de compte Braze, cochez la case **Require external ID** et saisissez l'ID externe de Braze. Sélectionnez **Next** lorsque vous avez terminé.

![La page S3 « Create Role ». Cette page contient des champs pour le nom du rôle, la description du rôle, les entités de confiance, les politiques et les limites des autorisations.]({{site.baseurl}}/assets/img/create_role_2_another.png)

### Étape 3 : Joindre la politique {#role-arn-3}

Ensuite, attachez la politique que vous avez créée précédemment au rôle. Recherchez la politique dans la barre de recherche et cochez-la pour la joindre. Sélectionnez **Next** lorsque vous avez terminé.

![ARN du rôle]({{site.baseurl}}/assets/img/create_role_3_attach.png)

Donnez un nom et une description au rôle, puis sélectionnez **Create Role**.

![ARN du rôle]({{site.baseurl}}/assets/img/create_role_4_name.png)

Votre nouveau rôle apparaît maintenant dans la liste.

### Étape 4 : Lier à Braze AWS {#role-arn-4}

Dans la console AWS, trouvez votre rôle nouvellement créé dans la liste. Sélectionnez le nom pour ouvrir les détails de ce rôle.

![Page de détails du rôle AWS IAM pour le rôle nouvellement créé.]({{site.baseurl}}/assets/img/create_role_5_created.png)

Prenez note du **Role ARN** en haut de la page de résumé du rôle.

![Résumé du rôle AWS IAM affichant la valeur du Role ARN.]({{site.baseurl}}/assets/img/create_role_6_summary.png)

Retournez sur votre compte Braze et copiez l'ARN du rôle dans le champ prévu à cet effet.

{% alert note %}
Si vous ne configurez que l'archivage des messages, suivez les étapes de l'onglet **Dashboard Data Export**.
{% endalert %}

{% tabs %}
{% tab Braze Currents %}

Dans Braze, accédez à **Partner Integrations** > **Currents**. Ensuite, sélectionnez **Create New Current** puis **Amazon S3 Data Export**.

![Écran de configuration de Braze Currents pour Amazon S3 avec les champs AWS Role ARN et compartiment.]({{site.baseurl}}/assets/img/currents-role-arn.png)

Donnez un nom à votre Current. Ensuite, dans la section **Credentials**, assurez-vous que l'option **AWS Role ARN** est sélectionnée, puis indiquez votre ARN de rôle et le nom du compartiment S3 AWS dans les champs désignés.

Vous pouvez également ajouter les personnalisations suivantes en fonction de vos besoins :

- Chemin d'accès au dossier (par défaut : `currents`)
- Chiffrement AES-256 côté serveur, au repos (désactivé par défaut) — Inclut l'en-tête `x-amz-server-side-encryption`

Sélectionnez **Launch Current** pour continuer. Une notification indique si vos identifiants ont été validés avec succès. AWS S3 est maintenant configuré pour Braze Currents.

{% alert important %}
Si vous recevez une erreur « S3 credentials are invalid », cela peut être dû à une intégration trop rapide après la création d'un rôle dans AWS. Attendez et réessayez. Si le message mentionne un accès `PutObject` ou le chiffrement côté serveur pour les exportations de données du tableau de bord, consultez la section [Résolution des problèmes d'identifiants S3](#troubleshooting).
{% endalert %}

{% endtab %}
{% tab Dashboard Data Export %}

Dans Braze, accédez à la page **Technology Partners** sous **Integrations** et sélectionnez **Amazon S3**.

![Page du partenaire technologique Amazon S3 dans Braze avec les identifiants AWS Role ARN sélectionnés.]({{site.baseurl}}/assets/img/data-export-role-arn.png)

Sur la page **AWS Credentials**, assurez-vous que le bouton radio **AWS Role ARN** est sélectionné, puis saisissez votre ARN de rôle et le nom du compartiment S3 AWS dans les champs désignés. Sélectionnez d'abord **Test Credentials** pour confirmer que vos identifiants fonctionnent correctement, puis sélectionnez **Save** en cas de succès.

{% alert tip %}
Vous pouvez toujours récupérer de nouveaux identifiants en accédant à votre utilisateur et en sélectionnant **Create Access Key** dans l'onglet **Security Credentials** de la console AWS.
{% endalert %}

Une notification vous indique si vos identifiants ont été validés avec succès. AWS S3 est désormais intégré à votre compte Braze.

{% endtab %}
{% endtabs %}

## Mise à jour des identifiants Amazon S3 pour Currents {#updating-currents-credentials}

Vous pouvez mettre à jour les identifiants Amazon S3 sur un connecteur Braze Currents existant sans interrompre l'intégration ni perdre les données déjà exportées vers votre compartiment.

Pour actualiser les identifiants — ou pour basculer entre **AWS Secret Access Key** et **AWS Role ARN** — terminez les étapes IAM et AWS décrites plus haut dans cet article pour la méthode choisie (politiques, utilisateur ou rôle, et identifiants selon les besoins).

Lorsque vous avez terminé de préparer les identifiants dans AWS, accédez à **Partner Integrations** > **Currents** dans Braze, localisez votre connecteur Amazon S3 dans la liste, sélectionnez **Edit**, mettez à jour les **Credentials**, puis sélectionnez **Update Current**. Braze valide les identifiants que vous saisissez ; votre connecteur continue de fonctionner et les données déjà présentes dans votre compartiment restent disponibles. Pour en savoir plus, consultez la section [Mise à jour de Currents dans Configurer Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents#updating-currents).

## Comportement à l'exportation {#export-behavior}

Les utilisateurs qui ont intégré une solution de stockage de données cloud et qui exportent via des API, des rapports de tableau de bord ou des rapports CSV constatent le comportement suivant :

- Toutes les exportations API ne renvoient pas d'URL de téléchargement dans le corps de la réponse et doivent être récupérées via le stockage de données.
- Tous les rapports de tableau de bord et les rapports CSV sont envoyés par e-mail à l'utilisateur pour téléchargement (aucune autorisation de stockage n'est requise) et sauvegardés sur Data Storage.

### Erreur `Unable to connect to S3, please validate that your credentials are correct` {#unable-to-connect-to-s3-please-validate-that-your-credentials-are-correct-error}

Si vous voyez cette erreur lors du téléchargement d'une exportation CSV, ouvrez l'intégration [Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3) sur la page **Technology Partners** et sélectionnez **Test Credentials**. Le résultat explique ce qui a échoué lors de la validation — par exemple, la clé peut ne pas disposer de l'autorisation `GetObject`, ce qui empêche Braze de générer des liens de téléchargement.

Mettez à jour votre politique IAM afin que l'utilisateur ou le rôle d'intégration puisse appeler `s3:GetObject` sur le compartiment S3 et le chemin d'objet configurés dans votre intégration Braze. Pour d'autres problèmes d'exportation, consultez la section [Résolution des problèmes d'exportation]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting).

{% alert important %}
**Exigences relatives au format JSON :** Pour les exportations JSON, Braze utilise le format JSONL (JSON délimité par des retours à la ligne), où chaque ligne contient un objet JSON distinct. Ce format diffère du JSON standard, qui est un tableau ou un objet JSON unique. Chaque ligne du fichier exporté est un objet JSON valide, mais le fichier dans son ensemble n'est pas un document JSON unique valide. Lorsque vous traitez ces fichiers, analysez chaque ligne individuellement en tant qu'objet JSON distinct plutôt que d'essayer d'analyser l'ensemble du fichier comme un document JSON unique.

Les exportations Currents utilisent le format Apache Avro (fichiers `.avro`), et non JSON. Cette exigence de format JSON s'applique aux exportations de données du tableau de bord et aux exportations API.
{% endalert %}

## Connecteurs multiples {#multiple-connectors}

Si vous avez l'intention de créer plusieurs connecteurs Currents pour envoyer des données vers votre compartiment S3, vous pouvez utiliser les mêmes identifiants, mais devez spécifier un chemin de dossier différent pour chacun. Vous pouvez les créer dans le même espace de travail ou les répartir dans plusieurs espaces de travail. Vous avez également la possibilité de créer une politique unique pour chaque intégration ou de créer une politique qui couvre les deux intégrations.

Si vous prévoyez d'utiliser le même compartiment S3 pour Currents et les exportations de données, vous devez créer deux politiques distinctes, car chaque intégration nécessite des autorisations différentes.

## Résolution des problèmes {#troubleshooting}

### Erreur : le compte n'a pas l'accès `PutObject` {#error-account-does-not-have-putobject-access}

Si vous voyez l'erreur suivante lors de l'enregistrement des identifiants Amazon S3 pour les exportations de données du tableau de bord, cela peut être dû à des autorisations incorrectes ou à des paramètres de chiffrement côté serveur.

```
S3 Credentials are invalid because this account does not have 'PutObject access'. Please check the permissions and ensure that this key has access to 'PutObject' in the 'CUSTOMER-BUCKET-HERE' bucket.
```

Pour résoudre ce problème, vérifiez les points suivants.

#### Politique de compartiment incorrecte {#incorrect-bucket-policy}

Confirmez que vous avez créé une politique avec les autorisations correctes telles que décrites dans la section [Intégration Amazon S3](#integration) (utilisez la politique **Dashboard Data Export** pour votre méthode d'authentification).

#### Chiffrement côté serveur {#server-side-encryption}

```
User: arn:aws:sts::XXX:assumed-role/braze-iam-role/braze is not authorized to perform: kms:GenerateDataKey on resource: arn:aws:XXX because no identity-based policy allows the kms:GenerateDataKey action
```

Si vous recevez ce message d'erreur de la part de l'[assistance Braze]({{site.baseurl}}/braze_support) ou dans vos journaux AWS, votre compartiment S3 est configuré avec le chiffrement AWS Key Management Service (SSE-KMS). Braze ne prend pas en charge SSE-KMS pour Currents ou les exportations de données du tableau de bord. Pour résoudre ce problème, désactivez SSE-KMS dans votre compartiment S3.

{% alert note %}
Braze prend en charge le chiffrement côté serveur à l'aide de clés gérées par S3 (SSE-S3), qui est compatible avec Currents et les exportations de données du tableau de bord.
{% endalert %}

#### Vérifier les autorisations supplémentaires {#check-additional-permissions}

Assurez-vous de disposer des autorisations nécessaires, notamment `s3:GetBucketLocation` et `s3:PutObject`.