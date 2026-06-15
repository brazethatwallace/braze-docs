---
nav_title: Transférer les données vers Redshift
article_title: Transférer des données vers Redshift
page_order: 8
page_type: tutorial
description: "Cet article pratique vous explique comment transférer des données d'Amazon S3 vers Redshift par le biais d'un processus d'extraction, de transformation et de chargement (ETL)."
tool: Currents

---

# Transférer les données vers Redshift

> [Amazon Redshift](https://aws.amazon.com/redshift/) est un entrepôt de données populaire qui fonctionne sur Amazon Web Services aux côtés d'Amazon S3. Les données Braze provenant de Currents sont structurées de manière à pouvoir être transférées directement vers Redshift.

La procédure suivante décrit comment transférer des données depuis Amazon S3 vers Redshift via un processus ETL (extraire, transformer, charger). Pour obtenir le code source complet, veuillez consulter le [référentiel GitHub](https://github.com/Appboy/currents-examples) des exemples Currents.

{% alert important %}
Notez que ce n'est qu'une des nombreuses options que vous pouvez choisir lorsqu'il s'agit de transférer vos données vers les emplacements les plus avantageux pour vous.
{% endalert %}

## Aperçu du chargeur S3 vers Redshift

Le script [`s3loader.py`](https://github.com/Appboy/currents-examples/tree/master/redshift-s3-loader) utilise une table manifeste distincte dans la même base de données Redshift pour garder une trace des fichiers qui ont déjà été copiés. La structure générale est la suivante :

1. Répertorier tous les fichiers dans S3, puis identifier les nouveaux fichiers depuis la dernière exécution de `s3loader.py` en comparant la liste avec le contenu de la table manifeste.
2. Créer un fichier [manifeste](http://docs.aws.amazon.com/redshift/latest/dg/loading-data-files-using-manifest.html) contenant les nouveaux fichiers.
3. Exécuter une requête `COPY` pour copier les nouveaux fichiers de S3 vers Redshift à l'aide du fichier manifeste.
4. Insérer les noms des fichiers copiés dans la table manifeste distincte dans Redshift.
5. Valider.

## Dépendances

Vous devez installer le SDK Python AWS et Psycopg pour exécuter le chargeur :

```bash
pip install boto3
pip install psycopg2
```

## Autorisations

### Rôle Redshift avec accès en lecture à S3

Si ce n'est pas déjà fait, suivez la [documentation AWS](http://docs.aws.amazon.com/redshift/latest/gsg/rs-gsg-create-an-iam-role.html) pour créer un rôle capable d'exécuter des commandes `COPY` sur vos fichiers dans S3.

### Règles entrantes du VPC Redshift

Si votre cluster Redshift se trouve dans un VPC, vous devez configurer le VPC pour autoriser les connexions depuis le serveur sur lequel vous exécutez le chargeur S3. Accédez à votre cluster Redshift et sélectionnez l'entrée VPC Security Groups à laquelle vous souhaitez que le chargeur se connecte. Ajoutez ensuite une nouvelle règle entrante : **Type** = Redshift, **Protocol** = TCP, **Port** = le port de votre cluster, **Source** = l'adresse IP du serveur exécutant le chargeur (ou « Anywhere » pour les tests).

### Utilisateur Identity and Access Management (IAM) avec accès complet à S3

Le chargeur S3 nécessite un accès en lecture aux fichiers contenant vos données Currents, ainsi qu'un accès complet à l'emplacement des fichiers manifestes qu'il génère pour les commandes Redshift `COPY`. Créez un nouvel utilisateur Identity and Access Management (IAM) avec l'autorisation `AmazonS3FullAccess` depuis la [console IAM](https://console.aws.amazon.com/iam/home#/users). Enregistrez les identifiants, car vous devrez les transmettre au chargeur.

Vous pouvez transmettre les identifiants d'accès au chargeur via des variables d'environnement, le fichier d'identifiants partagé (`~/.aws/credentials`) ou le [fichier de configuration AWS](http://boto3.readthedocs.io/en/latest/guide/configuration.html#configuring-credentials). Vous pouvez également les inclure directement dans le chargeur en les affectant aux champs `aws_access_key_id` et `aws_secret_access_key` au sein d'un objet `S3LoadJob`, mais nous déconseillons de coder en dur les identifiants dans votre code source.

## Utilisation

### Exemple d'utilisation

Le programme suivant charge les données de l'événement `users.messages.contentcard.Impression` depuis S3 vers la table `content_card_impression` dans Redshift.

```
if __name__ == '__main__':
    host = '{YOUR_CLUSTER}.redshift.amazonaws.com'
    port = 5439
    database = '{YOUR_DATABASE}'
    user = '{YOUR_USER}'
    password = '{YOUR_PASSWORD}'
    role = '{YOUR_REDSHIFT_ROLE_ARN}'

    # Do not hard code these credentials.
    aws_access_key_id = None
    aws_secret_access_key = None

    # Content Card Impression Avro fields:
    #   id            - string
    #   user_id       - string
    #   external_user_id - string (nullable)
    #   app_id        - string
    #   content_card_id  - string
    #   campaign_id   - string (nullable)
    #   send_id       - string (nullable)
    #   time          - int
    #   platform      - string (nullable)
    #   device_model  - string (nullable)

    print('Loading Content Card Impression...')
    cc_impression_s3_bucket = '{YOUR_CURRENTS_BUCKET}'
    cc_impression_s3_prefix = '{YOUR_CURRENTS_PREFIX}'
    cc_impression_redshift_table = 'content_card_impression'
    cc_impression_redshift_column_def = [
        ('id', 'text'),
        ('user_id', 'text'),
        ('external_user_id', 'text'),
        ('app_id', 'text'),
        ('content_card_id', 'text'),
        ('campaign_id', 'text'),
        ('send_id', 'text'),
        ('time', 'integer'),
        ('platform', 'text'),
        ('device_model', 'text')
    ]

    cc_impression_redshift = RedshiftEndpoint(host, port, database, user, password,
        cc_impression_redshift_table, cc_impression_redshift_column_def)
    cc_impression_s3 = S3Endpoint(cc_impression_s3_bucket, cc_impression_s3_prefix)

    cc_impression_job = S3LoadJob(cc_impression_redshift, cc_impression_s3, role,
        aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
    cc_impression_job.perform()
```

### Identifiants

Pour exécuter le chargeur, vous devez d'abord fournir le `host`, le `port` et la `database` de votre cluster Redshift, ainsi que le `user` et le `password` d'un utilisateur Redshift autorisé à exécuter des requêtes `COPY`. Vous devez également fournir l'ARN du rôle Redshift avec accès en lecture à S3 que vous avez créé dans une section précédente.

```
host = '{YOUR_CLUSTER}.redshift.amazonaws.com'
port = 5439
database = '{YOUR_DATABASE}'
user = '{YOUR_USER}'
password = '{YOUR_PASSWORD}'
role = '{YOUR_REDSHIFT_ROLE_ARN}'
```

### Configuration du job

Vous devez fournir le compartiment S3 et le préfixe de vos fichiers d'événements, ainsi que le nom de la table Redshift dans laquelle vous souhaitez effectuer le `COPY`.

De plus, pour exécuter un `COPY` de fichiers Avro avec l'option « auto » comme l'exige le chargeur, la définition des colonnes de votre table Redshift doit correspondre aux noms des champs du schéma Avro, comme illustré dans le programme d'exemple, avec le mappage de types approprié (par exemple, `string` vers `text`, `int` vers `integer`).

Vous pouvez également passer une option `batch_size` au chargeur si la copie de tous les fichiers en une seule fois prend trop de temps. L'utilisation de `batch_size` permet au chargeur de copier et valider de manière incrémentale un lot à la fois, sans avoir à tout copier simultanément. Le temps nécessaire pour charger un lot dépend de la valeur de `batch_size`, de la taille de vos fichiers et de la taille de votre cluster Redshift.

```
# Content Card Impression Avro fields:
#   id            - string
#   user_id       - string
#   external_user_id - string (nullable)
#   app_id        - string
#   content_card_id  - string
#   campaign_id   - string (nullable)
#   send_id       - string (nullable)
#   time          - int
#   platform      - string (nullable)
#   device_model  - string (nullable)
cc_impression_s3_bucket = '{YOUR_CURRENTS_BUCKET}'
cc_impression_s3_prefix = '{YOUR_CURRENTS_PREFIX}'
cc_impression_redshift_table = 'content_card_impression'
cc_impression_redshift_column_def = [
    ('id', 'text'),
    ('user_id', 'text'),
    ('external_user_id', 'text'),
    ('app_id', 'text'),
    ('content_card_id', 'text'),
    ('campaign_id', 'text'),
    ('send_id', 'text'),
    ('time', 'integer'),
    ('platform', 'text'),
    ('device_model', 'text')
]
cc_impression_batch_size = 1000
```