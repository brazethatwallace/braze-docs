---
nav_title: Daten von Amazon S3 zu Snowflake übertragen
article_title: Daten von Amazon S3 zu Snowflake übertragen
page_order: 7
page_type: tutorial
description: "In diesem Artikel erfahren Sie, wie Sie mit Hilfe des ETL-Prozesses (ETL) Daten aus einem Cloud-Speicher (z. B. Amazon S3) in ein Data Warehouse (z. B. Snowflake) übertragen."
tool: Currents

---

# Daten von Amazon S3 zu Snowflake übertragen {#transfer-data-from-amazon-s3-to-snowflake}

> Wenn sich Ihre Daten derzeit in Amazon S3 befinden, können Sie sie mit dem Prozess Extract, Load, Transform (ELT) in Snowflake oder ein anderes relationales Data Warehouse übertragen. Auf dieser Seite erfahren Sie, wie das funktioniert.

{% alert note %}
Wenn Sie spezifischere Anwendungsfälle haben und möchten, dass Braze Ihre Currents-Instanz betreut, wenden Sie sich an Ihre:n Braze Account Manager:in:in und fragen Sie nach den Braze Data Professional Services.
{% endalert %}

## Funktionsweise {#how-it-works}

Der Prozess Extract, Load, Transform (ELT) ist ein automatisierter Prozess, der Daten in [Snowflake](https://www.snowflake.com/) überträgt, sodass Sie die [Braze Looker Blocks](https://marketplace.looker.com/marketplace/directory) verwenden können, um diese Daten in Looker zu visualisieren und so Insights und Feedback für Ihre Campaigns, Canvases und Segmente zu gewinnen.

Nachdem Sie einen Export von Currents nach S3 eingerichtet haben und Live-Ereignisdaten empfangen, können Sie Ihre Live-ELT-Pipeline in Snowflake konfigurieren, indem Sie die folgenden Komponenten einrichten:

-   [AWS SQS-Warteschlangen](#aws-sqs-queues)
-   [Auto-Ingest Snowpipes](#auto-ingest-snowpipes)

## Konfigurieren von AWS SQS-Warteschlangen {#aws-sqs-queues}

**Auto-Ingest Snowpipes** nutzen SQS-Warteschlangen, um Benachrichtigungen von S3 an Snowpipe zu senden. Dieser Prozess wird von Snowflake verwaltet, nachdem SQS konfiguriert wurde.

### 1. Schritt: Externe S3-Stage konfigurieren {#step-1-configure-the-external-s3-stage}

{% alert note %}
Tabellen in Ihrer Datenbank werden in diesem Schritt erstellt.
{% endalert %}

1. Wenn Sie Currents in Braze einrichten, geben Sie einen Ordnerpfad an, dem Ihre Currents-Dateien in Ihrem S3-Bucket folgen sollen. Hier verwenden wir `currents`, den Standard-Ordnerpfad.

2. Erstellen Sie Folgendes in der angegebenen Reihenfolge:
  2.1 Erstellen Sie in AWS ein neues **Public-Private-Key-Paar** für den gewünschten S3-Bucket mit Berechtigungen gemäß den Sicherheitsanforderungen Ihrer Organisation.
  2.2. Erstellen Sie in Snowflake eine Datenbank und ein Schema Ihrer Wahl (im folgenden Beispiel `currents` und `public` genannt).
  2.3. Erstellen Sie eine Snowflake S3-Stage (hier `braze_data` genannt):

```sql
CREATE OR REPLACE STAGE
    currents.public.braze_data
    url='s3://snowpipe-demo/'
    credentials = (AWS_KEY_ID = '...' AWS_SECRET_KEY = '...' );
show stages;
```

{: start="3"}
3. Definieren Sie das AVRO-Dateiformat für Ihre Stage.

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
4. Verwenden Sie abschließend den Befehl `show pipes;`, um Ihre SQS-Informationen anzuzeigen. Der Name der SQS-Warteschlange wird in einer neuen Spalte namens `NOTIFICATION_CHANNEL` angezeigt, da diese Pipe als Auto-Ingest-Pipe erstellt wurde.

### 2. Schritt: Bucket-Ereignisse erstellen {#step-2-create-bucket-events}

1. Navigieren Sie in AWS zum entsprechenden Bucket der neuen Snowflake-Stage. Gehen Sie dann unter dem Tab **Properties** zu **Events**.

![AWS-Tab „Properties“]({% image_buster /assets/img/aws-properties.png %}){: height="50%" width="50%"}

{: start="2"}
2. Erstellen Sie nach Bedarf neue Ereignisse für jeden Satz von Currents-Daten ([Messaging]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events), [Kundenverhalten]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events)) oder beides.

![Erstellen eines neuen Ereignisses in AWS]({% image_buster /assets/img/aws-events.png %}){: height="50%" width="50%"}

{: start="3"}
3. Aktivieren Sie das entsprechende Kontrollkästchen für die Benachrichtigungen zur Objekterstellung sowie den ARN am unteren Rand des Formulars (aus der Spalte „Notification Channel“ in Snowflake).

## Konfigurieren von Auto-Ingest Snowpipes {#auto-ingest-snowpipes}

Damit die AWS SQS-Konfiguration die richtigen Tabellen erzeugt, müssen Sie die Struktur der eingehenden Daten korrekt definieren. Verwenden Sie dazu die folgenden Beispiele und Schemas aus unserer Currents-Dokumentation für [Messaging-Engagement- oder Messaging-Ereignisse]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events), [Kundenverhalten-Ereignisse]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events) oder beides.

Es ist entscheidend, dass Sie Ihre Tabellen gemäß den Braze-Currents-Schemas strukturieren, da Braze-Currents kontinuierlich Daten über bestimmte Felder mit bestimmten Datentypen in diese laden wird. Beispielsweise wird eine `user_id` als String geladen und in den Currents-Daten als `user_id` bezeichnet.

{% alert note %}
  Je nach Ihrer Currents-Integration müssen Sie möglicherweise verschiedene Ereignisse einrichten (z. B. [Messaging-Engagement- oder Messaging-Ereignisse]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) und [Kundenverhalten-Ereignisse]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events)). Sie können auch ein Skript für einen Teil oder den gesamten Prozess schreiben.
{% endalert %}

{% tabs %}
  {% tab User Behavior Events %}

1. Erstellen Sie eine Tabelle, in die (`INTO`) Sie kontinuierlich Daten laden werden, unter Verwendung der folgenden Struktur aus dem Currents-Schema:

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
2. Erstellen Sie die `auto_ingest`-Pipe und geben Sie Folgendes an:
  2.1. Welche Tabelle geladen werden soll
  2.2 Wie die folgende Tabelle geladen werden soll

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
Sie müssen die Befehle `CREATE TABLE` und `CREATE PIPE` für jeden Event-Typ wiederholen.
{% endalert %}

 {% endtab %}
 {% tab Messaging Events %}

1. Erstellen Sie eine Tabelle, in die (`INTO`) Sie kontinuierlich Daten laden werden, unter Verwendung der folgenden Struktur aus dem Currents-Schema:

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
2. Erstellen Sie die AUTO-Pipe für kontinuierliches Laden und geben Sie Folgendes an:
  2.1. Welche Tabelle geladen werden soll
  2.2 Wie die folgende Tabelle geladen werden soll

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
Sie müssen die Befehle `CREATE TABLE` und `CREATE PIPE` für jeden Event-Typ wiederholen.
{% endalert %}

  {% endtab %}
{% endtabs %}

Informationen zu den Arten von Analytics, die Sie mit Braze-Currents durchführen können, finden Sie in unseren [Looker Blocks](https://github.com/llooker?q=braze).

{% alert note %}
Kontaktieren Sie Ihre:n Braze Account Manager:in:in, wenn Sie Fragen haben oder daran interessiert sind, dass Braze Sie durch diesen Prozess begleitet.
{% endalert %}