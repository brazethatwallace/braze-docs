---
nav_title: Transférer des données d'Amazon S3 vers Snowflake
article_title: Transférer des données d'Amazon S3 vers Snowflake
page_order: 7
page_type: tutorial
description: "Cet article pratique vous explique comment transférer des données d'un stockage cloud (comme Amazon S3) vers un entrepôt de données (comme Snowflake) en utilisant le processus ETL."
tool: Currents

---

# Transférer des données d'Amazon S3 vers Snowflake {#transfer-data-from-amazon-s3-to-snowflake}

> Si vos données se trouvent actuellement dans Amazon S3, vous pouvez les transférer vers Snowflake ou un autre entrepôt de données relationnel à l'aide du processus d'extraction, de chargement et de transformation (ELT). Cette page vous explique comment procéder.

{% alert note %}
Si vous avez des cas d'utilisation plus spécifiques et que vous souhaitez que Braze assure le service de votre instance Currents, contactez votre gestionnaire de compte Braze et renseignez-vous sur les Braze Data Professional Services.
{% endalert %}

## Fonctionnement {#how-it-works}

Le processus d'extraction, de chargement et de transformation (ELT) est un processus automatisé qui déplace les données dans [Snowflake](https://www.snowflake.com/), ce qui vous permettra d'utiliser les [blocs Looker de Braze](https://marketplace.looker.com/marketplace/directory) pour visualiser ces données dans Looker afin de générer des informations et des retours pour vos Campaigns, Canvas et Segments.

Une fois que vous avez configuré une exportation Currents vers S3 et que vous recevez des données d'événements en temps réel, vous pouvez configurer votre pipeline ELT en direct dans Snowflake en configurant les composants suivants :

-   [Files d'attente AWS SQS](#aws-sqs-queues)
-   [Snowpipes à ingestion automatique](#auto-ingest-snowpipes)

## Configuration des files d'attente AWS SQS {#configuring-aws-sqs-queues}

Les **Snowpipes à ingestion automatique** s'appuient sur les files d'attente SQS pour envoyer des notifications de S3 vers Snowpipe. Ce processus est géré par Snowflake après la configuration de SQS.

### Étape 1 : Configurer le stage S3 externe {#step-1-configure-the-external-s3-stage}

{% alert note %}
Les tables de votre base de données sont créées à cette étape.
{% endalert %}

1. Lorsque vous configurez Currents dans Braze, spécifiez un chemin de dossier que vos fichiers Currents doivent suivre dans votre compartiment S3. Ici, nous utilisons `currents`, le chemin de dossier par défaut.

2. Créez les éléments suivants dans l'ordre indiqué :
  2.1 Dans AWS, créez une nouvelle **paire de clés publique-privée** pour le compartiment S3 souhaité, avec des autorisations conformes aux exigences de sécurité de votre organisation.
  2.2. Dans Snowflake, créez une base de données et un schéma de votre choix (nommés `currents` et `public` dans l'exemple suivant).
  2.3. Créez un stage Snowflake S3 (appelé `braze_data`) :

```sql
CREATE OR REPLACE STAGE
    currents.public.braze_data
    url='s3://snowpipe-demo/'
    credentials = (AWS_KEY_ID = '...' AWS_SECRET_KEY = '...' );
show stages;
```

{: start="3"}
3. Définissez le format de fichier AVRO pour votre stage.

```sql
CREATE FILE FORMAT
    currents.public.currents_avro
    type = 'avro'
    compression = 'auto';
```

```sql
ALTER STAGE
    currents.public.braze_data
SET
    file_format = currents.public.currents_avro;
```

```sql
CREATE OR REPLACE PIPE
  pipe_users_messages_pushnotification_open
    auto_ingest=true AS

COPY INTO
  users_messages_pushnotification_open
          FROM
           (SELECT
             $1:id::STRING,
             $1:user_id::STRING,
             $1:external_user_id::STRING,
              $1:time::INT,
              $1:timezone::STRING,
              $1:app_id::STRING,
              $1:campaign_id::STRING,
              $1:campaign_name::STRING,
              $1:message_variation_id::STRING,
              $1:canvas_id::STRING,
              $1:canvas_name::STRING,
              $1:canvas_variation_id::STRING,
              $1:canvas_step_id::STRING,
              $1:canvas_step_message_variation_id::STRING,
              $1:platform::STRING,
              $1:os_version::STRING,
              $1:device_model::STRING,
              $1:send_id::STRING,
              $1:device_id::STRING,
              $1:button_action_type::STRING,
              $1:button_string::STRING

              FROM
@currents.public.braze_data/currents/dataexport.prod-01.S3.integration.INTEGRATION_ID_GOES_HERE/event_type=users.messages.pushnotification.Open/);
```

{: start="4"}
4. Enfin, utilisez la commande `show pipes;` pour afficher les informations SQS. Le nom de la file d'attente SQS sera visible dans une nouvelle colonne appelée `NOTIFICATION_CHANNEL`, car ce pipe a été créé en tant que pipe à ingestion automatique.

### Étape 2 : Créer des événements de compartiment {#step-2-create-bucket-events}

1. Dans AWS, accédez au compartiment correspondant au nouveau stage Snowflake. Ensuite, sous l'onglet **Properties**, accédez à **Events**.

![Onglet Properties dans AWS]({% image_buster /assets/img/aws-properties.png %}){: height="50%" width="50%"}

{: start="2"}
2. Créez de nouveaux événements pour chaque ensemble de données Currents, selon vos besoins ([envoi de messages]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events), [comportement des utilisateurs]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events)), ou les deux.

![Création d'un nouvel événement dans AWS]({% image_buster /assets/img/aws-events.png %}){: height="50%" width="50%"}

{: start="3"}
3. Cochez la case appropriée pour les notifications de création d'objet, ainsi que l'ARN en bas du formulaire (provenant de la colonne du canal de notification dans Snowflake).

## Configuration des Snowpipes à ingestion automatique {#auto-ingest-snowpipes}

Pour que la configuration AWS SQS produise les tables correctes, vous devez définir correctement la structure des données entrantes en utilisant les exemples et schémas suivants, déterminés dans notre documentation Currents pour les [événements d'engagement de messages ou événements d'envoi de messages]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events), les [événements de comportement des utilisateurs ou des clients]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events), ou les deux.

Il est essentiel de structurer vos tables conformément aux schémas de Braze Currents, car Braze Currents chargera continuellement des données dans celles-ci via des champs spécifiques avec des types de données spécifiques. Par exemple, un `user_id` sera chargé en tant que chaîne de caractères et sera appelé `user_id` dans les données Currents.

{% alert note %}
  Selon votre intégration Currents, vous pouvez avoir différents événements à configurer (tels que les [événements d'engagement de messages ou événements d'envoi de messages]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) et les [événements de comportement des utilisateurs ou des clients]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events)). Vous pouvez également écrire un script pour une partie ou la totalité de ce processus.
{% endalert %}

{% tabs %}
  {% tab User Behavior Events %}

1. Créez une table `INTO` dans laquelle nous chargerons continuellement des données en utilisant la structure suivante issue du schéma Currents :

```sql
CREATE TABLE
  users_behaviors_app_firstsession (
        id               STRING,
        user_id          STRING,
        external_user_id STRING,
        app_id           STRING,
        time             INT,
        session_id       STRING,
        gender           STRING,
        country          STRING,
        timezone         STRING,
        language         STRING,
        device_id        STRING,
        sdk_version      STRING,
        platform         STRING,
        os_version       STRING,
        device_model     STRING
    );
```

{: start="2"}
2. Créez le pipe `auto_ingest` et spécifiez :
  2.1. Quelle table charger
  2.2 Comment charger la table suivante

```sql
CREATE OR REPLACE PIPE
  pipe_users_behaviors_app_firstsession
    auto_ingest=true AS

COPY INTO
  users_behaviors_app_firstsession
          FROM
            (SELECT
              $1:id::STRING,
              $1:user_id::STRING,
              $1:external_user_id::STRING,
              $1:app_id::STRING,
              $1:time::INT,
              $1:session_id::STRING,
              $1:gender::STRING,
              $1:country::STRING,
              $1:timezone::STRING,
              $1:language::STRING,
              $1:device_id::STRING,
              $1:sdk_version::STRING,
              $1:platform::STRING,
              $1:os_version::STRING,
              $1:device_model::STRING

              FROM
@currents.public.braze_data/currents/dataexport.prod-01.S3.integration.INTEGRATION_ID_GOES_HERE/event_type=users.behaviors.app.FirstSession/);
```

{% alert warning %}
Vous devez répéter les commandes `CREATE TABLE` et `CREATE PIPE` pour chaque type d'événement.
{% endalert %}

 {% endtab %}
 {% tab Messaging Events %}

1. Créez une table `INTO` dans laquelle nous chargerons continuellement des données en utilisant la structure suivante issue du schéma Currents :

```sql
CREATE TABLE
    public_users_messages_pushnotification_open (
        id STRING,
        user_id STRING,
        external_user_id STRING,
        time INT,
        timezone STRING,
        app_id STRING,
        campaign_id STRING,
        campaign_name STRING,
        message_variation_id STRING,
        canvas_id STRING,
        canvas_name STRING,
        canvas_variation_id STRING,
        canvas_step_id STRING,
        canvas_step_message_variation_id STRING,
        platform STRING,
        os_version STRING,
        device_model STRING,
        send_id STRING,
        device_id STRING,
        button_action_type STRING,
        button_string STRING
        );
```

{: start="2"}
2. Créez le pipe de chargement continu AUTO et spécifiez :
  2.1. Quelle table charger
  2.2 Comment charger la table suivante

```sql
CREATE OR REPLACE PIPE
  pipe_users_messages_pushnotification_open
    auto_ingest=true AS

COPY INTO
  users_messages_pushnotification_open
          FROM
           (SELECT
             $1:id::STRING,
             $1:user_id::STRING,
             $1:external_user_id::STRING,
              $1:time::INT,
              $1:timezone::STRING,
              $1:app_id::STRING,
              $1:campaign_id::STRING,
              $1:campaign_name::STRING,
              $1:message_variation_id::STRING,
              $1:canvas_id::STRING,
              $1:canvas_name::STRING,
              $1:canvas_variation_id::STRING,
              $1:canvas_step_id::STRING,
              $1:canvas_step_message_variation_id::STRING,
              $1:platform::STRING,
              $1:os_version::STRING,
              $1:device_model::STRING,
              $1:send_id::STRING,
              $1:device_id::STRING,
              $1:button_action_type::STRING,
              $1:button_string::STRING

              FROM
@currents.public.braze_data/currents/dataexport.prod-01.S3.integration.INTEGRATION_ID_GOES_HERE/event_type=users.messages.pushnotification.Open/);
```

{% alert warning %}
Vous devez répéter les commandes `CREATE TABLE` et `CREATE PIPE` pour chaque type d'événement.
{% endalert %}

  {% endtab %}
{% endtabs %}

Pour découvrir les types d'analyses que vous pouvez effectuer avec Braze Currents, consultez nos [blocs Looker](https://github.com/llooker?q=braze).

{% alert note %}
Contactez votre gestionnaire de compte Braze si vous avez des questions ou si vous souhaitez que Braze vous accompagne dans ce processus.
{% endalert %}