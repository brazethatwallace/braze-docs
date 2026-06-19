---
nav_title: Exportation des événements de sécurité avec S3
article_title: Exportation des paramètres de sécurité avec S3
page_order: 1
page_type: reference
description: "Cet article de référence explique comment exporter automatiquement les événements de sécurité tous les jours à minuit UTC vers Amazon S3."
---

# Exportation des événements de sécurité avec Amazon S3 {#security-events-export-with-amazon-s3}

> Vous pouvez exporter automatiquement les événements de sécurité vers Amazon S3, un fournisseur de stockage cloud, grâce à une tâche quotidienne qui s'exécute à minuit UTC. Une fois la configuration effectuée, il n'est pas nécessaire d'exporter manuellement les événements de sécurité depuis le tableau de bord. Cette tâche exporte les événements de sécurité des dernières 24 heures au format CSV vers votre stockage S3 configuré. Le fichier CSV présente la même structure qu'un rapport exporté manuellement.

{% alert note %}
La limite de 10 000 lignes s'applique uniquement au téléchargement manuel du rapport CSV à partir du tableau de bord. Les exportations d'événements de sécurité vers S3 ne sont pas soumises à cette limite de lignes.
{% endalert %}

Braze prend en charge deux méthodes d'authentification et d'autorisation S3 différentes pour configurer l'exportation Amazon S3 :

- Méthode de clé d'accès secrète AWS
- Méthode ARN de rôle AWS

## Méthode de clé d'accès secrète AWS {#aws-secret-access-key-method}

Cette méthode génère une clé secrète et un ID de clé d'accès qui permet à Braze de s'authentifier en tant qu'utilisateur sur votre compte AWS pour écrire des données dans votre compartiment.

### Étape 1 : Créer un utilisateur de gestion des identités et des accès (IAM) {#step-1-create-an-identity-and-access-management-iam-user}

Pour récupérer votre clé d'accès secrète et votre ID de clé d'accès, vous devrez créer un utilisateur IAM en suivant les instructions de la section [Configurer votre compte AWS](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started-account-iam.html#create-an-admin).

### Étape 2 : Obtenir les identifiants {#step-2-get-credentials}

1. Après avoir créé un nouvel utilisateur, générez la clé d'accès et téléchargez votre ID de clé d'accès et votre clé d'accès secrète.

![Page récapitulative d'un rôle appelé « liyu-chen-test ».]({% image_buster /assets/img/security_export/credentials1.png %})

{: start="2"}
2. Notez ces identifiants quelque part ou téléchargez les fichiers d'identifiants, car vous devrez les saisir dans Braze ultérieurement.

![Champs contenant la clé d'accès et la clé d'accès secrète.]({% image_buster /assets/img/security_export/retrieve_access_keys.png %})

### Étape 3 : Créer une politique {#step-3-create-policy}

1. Accédez à **IAM** (Identity and Access Management) > **Policies** > **Create Policy** pour ajouter des autorisations à votre utilisateur.
2. Sélectionnez **Create Your Own Policy**, ce qui accorde des autorisations limitées afin que Braze ne puisse accéder qu'aux compartiments spécifiés.
3. Indiquez un nom de politique de votre choix.
4. Saisissez l'extrait de code suivant dans la section **Policy Document**. Veillez à remplacer « INSERTBUCKETNAME » par le nom de votre compartiment. Sans ces autorisations, l'intégration échouera lors de la vérification des identifiants et ne sera pas créée.

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

### Étape 4 : Attacher la politique {#step-4-attach-policy}

1. Après avoir créé une nouvelle politique, accédez à **Users** et sélectionnez votre utilisateur spécifique.
2. Dans l'onglet **Permissions**, sélectionnez **Add Permissions**, attachez directement la politique, puis sélectionnez cette politique.

Vous êtes maintenant prêt à lier vos identifiants AWS à votre compte Braze !

### Étape 5 : Lier Braze à AWS {#step-5-link-braze-to-aws}

1. Dans Braze, accédez à **Paramètres** > **Paramètres de l'entreprise** > **Paramètres d'administration** > **Paramètres de sécurité** et faites défiler jusqu'à la section **Security Event Download**.
2. Activez **Export to AWS S3** sous **Export to cloud storage** et sélectionnez **AWS secret access key** pour activer l'exportation S3.
3. Saisissez les informations suivantes :

- ID de clé d'accès AWS
- Nom du compartiment AWS
- Clé d'accès secrète AWS
    - Lors de la saisie de cette clé, sélectionnez d'abord **Test Credentials** pour vérifier que vos identifiants fonctionnent.

![Page « Security Event Download » avec les identifiants de compte Braze et les ID externes Braze renseignés.]({% image_buster /assets/img/security_export/security_event_download1.png %})

{: start="4"}
4. Sélectionnez **Enregistrer les modifications**.

L'intégration d'AWS S3 avec votre compte Braze est terminée !

## Méthode ARN de rôle AWS {#aws-role-arn-method}

La méthode ARN de rôle AWS génère un nom de ressource Amazon (ARN) de rôle qui permet au compte Amazon de Braze de s'authentifier en tant que membre de ce rôle.

### Étape 1 : Créer une politique {#step-1-create-policy}

1. Connectez-vous à la console de gestion AWS en tant qu'administrateur de compte.
2. Dans la console AWS, accédez à la section **IAM** (Identity and Access Management) > **Policies**, puis sélectionnez **Create Policy**.

![Page avec une liste de politiques et un bouton « Create policy ».]({% image_buster /assets/img/security_export/policies.png %})

{: start="3"}
3. Ouvrez l'onglet **JSON** et saisissez l'extrait de code suivant dans la section **Policy Document**. Veillez à remplacer `INSERTBUCKETNAME` par le nom de votre compartiment.

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

{: start="4"}
4. Sélectionnez **Next** après avoir vérifié la politique.

![Page permettant de vérifier votre politique et d'ajouter éventuellement des autorisations.]({% image_buster /assets/img/security_export/specify_permissions.png %})

{: start="5"}
5. Donnez un nom et une description à la politique, puis sélectionnez **Create Policy**.

![Page pour vérifier et créer votre politique.]({% image_buster /assets/img/security_export/review_and_create.png %})

### Étape 2 : Créer un rôle {#step-2-create-role}

1. Dans Braze, accédez à **Paramètres** > **Paramètres de l'entreprise** > **Paramètres d'administration** > **Paramètres de sécurité** et faites défiler jusqu'à la section **Security Event Download**.
2. Sélectionnez **AWS Role ARN**.
3. Notez les identifiants nécessaires pour créer votre rôle : l'ID de compte Braze et l'ID externe Braze.

![Page « Security Event Download » avec les identifiants de compte Braze et les ID externes Braze renseignés.]({% image_buster /assets/img/security_export/security_event_download2.png %})

4. Dans la console AWS, accédez à la section **IAM** (Identity and Access Management) > **Roles** > **Create Role**.
5. Sélectionnez **Another AWS Account** comme type d'entité de confiance.
6. Fournissez votre ID de compte Braze, cochez la case **Require external ID**, puis saisissez votre ID externe Braze.
7. Sélectionnez **Next** une fois terminé.

![Page avec des options pour sélectionner un type d'entité de confiance et fournir des informations sur votre compte AWS.]({% image_buster /assets/img/security_export/select_trusted_entity.png %})

### Étape 3 : Attacher la politique {#step-3-attach-policy}

1. Recherchez la politique que vous avez créée précédemment dans la barre de recherche, puis cochez la case à côté de la politique pour l'attacher.
2. Sélectionnez **Next**.

![Liste de politiques avec des colonnes pour leur type et leur description.]({% image_buster /assets/img/security_export/add_permissions.png %})

{: start="3"}
3. Donnez un nom et une description au rôle, puis sélectionnez **Create Role**.

![Champs pour fournir les détails du rôle, tels que le nom, la description, la politique de confiance, les autorisations et les étiquettes.]({% image_buster /assets/img/security_export/name_review_create.png %})

Votre rôle nouvellement créé apparaîtra dans la liste !

### Étape 4 : Lier à Braze AWS {#step-4-link-to-braze-aws}

1. Dans la console AWS, trouvez votre rôle nouvellement créé dans la liste. Sélectionnez le nom pour ouvrir les détails de ce rôle et notez l'**ARN**.

![Page récapitulative d'un rôle appelé « security-event-export-olaf ».]({% image_buster /assets/img/security_export/credentials2.png %})

{: start="2"}
2. Dans Braze, accédez à **Paramètres** > **Paramètres de l'entreprise** > **Paramètres d'administration** > **Paramètres de sécurité** et faites défiler jusqu'à la section **Security Event Download**.

![Section « Security Event Download » avec un bouton bascule activé pour « Export to AWS S3 ».]({% image_buster /assets/img/security_export/security_event_download3.png %})

{: start="3"}
3. Assurez-vous que **AWS role ARN** est sélectionné, puis saisissez votre ARN de rôle et le nom de votre compartiment AWS S3 dans les champs prévus à cet effet.
4. Sélectionnez **Test Credentials** pour vérifier que vos identifiants fonctionnent correctement.
5. Sélectionnez **Enregistrer les modifications**.

L'intégration d'AWS S3 avec votre compte Braze est terminée !