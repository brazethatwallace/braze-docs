---
nav_title: "Exemples de requêtes"
article_title: Exemples de requêtes Snowflake
page_order: 1
description: "Cette page partenaire propose quelques exemples de requêtes pour différents cas d'usage à consulter lors de la configuration de vos requêtes Snowflake."
page_type: partner
search_tag: Partner

---

# Exemples de requêtes {#sample-queries}

> Cette page partenaire propose quelques exemples de requêtes pour différents cas d'usage à consulter lors de la configuration de vos requêtes.

{% tabs %}
{% tab Filter By Time%}

Une requête courante consiste à filtrer les événements par date et heure.

Vous pouvez les filtrer par le moment de leur occurrence. Les tables d'événements sont regroupées par `time`, ce qui rend le filtrage par `time` optimal :
```sql
-- find custom events that occurred after 04/15/2019 @ 7:02pm (UTC) i.e., timestamp=1555354920
SELECT *
FROM users_behaviors_customevent_shared
WHERE time > 1555354920
LIMIT 10;
```
Vous pouvez également filtrer les événements selon l'heure à laquelle ils ont été enregistrés dans l'entrepôt de données Snowflake à l'aide du champ `sf_created_at`. `sf_created_at` et `time` ne sont pas identiques mais sont généralement proches, cette requête devrait donc avoir des caractéristiques de performance similaires :
```sql
-- find custom events that arrived in Snowflake after time 04/15/2019 @ 7:02pm (UTC)
SELECT *
FROM users_behaviors_customevent_shared
WHERE sf_created_at > to_timestamp_ntz('2019-04-15 19:02:00')
LIMIT 10;
```
{% alert note %}
La valeur de `sf_created_at` n'est fiable que pour les événements enregistrés après le `15 novembre 2019 à 21 h 31 UTC`.
{% endalert %}
{% endtab %}

{% tab Querying Changelogs%}

Les noms de Campaign et de Canvas ne sont pas présents dans les événements eux-mêmes. Ils sont publiés dans une table de journal des modifications.

Vous pouvez afficher les noms des Campaigns pour les événements liés à une Campaign en effectuant une jointure avec la table du journal des modifications des Campaigns à l'aide d'une requête comme :

```sql
SELECT event.id, event.time, ccs.time, ccs.name, ccs.conversion_behaviors[event.conversion_behavior_index]
FROM USERS_CAMPAIGNS_CONVERSION_SHARED event
LEFT JOIN CHANGELOGS_CAMPAIGN_SHARED ccs
ON ccs.id = event.campaign_id
AND ccs.time < event.time
qualify row_number() over (partition by event.id ORDER BY ccs.time DESC) = 1;
```
Quelques points importants à noter :
- Les fonctions de [fenêtrage](https://docs.snowflake.com/en/sql-reference/functions-analytic.html) de Snowflake sont utilisées ici.
- La jointure gauche garantit que les événements non liés à une Campaign seront également inclus.
- Si vous voyez des événements avec des `campaign_id` mais sans noms de Campaign, il est possible que la Campaign ait été créée avec un nom avant que le partage de données n'existe en tant que produit.
- Vous pouvez afficher les noms de Canvas en utilisant une requête similaire, en effectuant la jointure avec la table `CHANGELOGS_CANVAS_SHARED` à la place.

Si vous souhaitez voir à la fois les noms de Campaign et de Canvas, vous pouvez utiliser la sous-requête suivante :
```sql
SELECT campaign_join.*, canvas.name AS canvas_name
FROM
(SELECT e.id AS event_id, e.external_user_id, e.time, e.user_id, e.device_id, e.sf_created_at,
    e.campaign_api_id, e.canvas_id, e.canvas_step_api_id,
    campaign.name AS campaign_name
  FROM USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED AS e
  LEFT JOIN CHANGELOGS_CAMPAIGN_SHARED AS campaign ON campaign.id = e.campaign_id
  WHERE e.time >= 1574830800 AND e.time <= 1575176399
  qualify row_number() over (partition by e.id ORDER BY campaign.time DESC) = 1) AS campaign_join
LEFT JOIN CHANGELOGS_CANVAS_SHARED AS Canvas ON canvas.id = campaign_join.canvas_id
qualify row_number() over (partition by campaign_join.event_id ORDER BY canvas.time DESC) = 1;
```
{% endtab %}
{% tab Push Funnel %}

Vous pouvez utiliser cette requête d'entonnoir push pour agréger les données brutes d'événements d'envoi de notifications push, en passant par les données brutes de distribution, jusqu'aux données brutes d'ouverture. Cette requête montre comment toutes les tables doivent être jointes, car chaque événement brut possède généralement une table séparée :

```sql

SELECT
    COUNT(DISTINCT send."ID" ) AS "users_messages_pushnotification_send.push_sent",
    COALESCE((COUNT(DISTINCT send."ID" )),0)-COALESCE((COUNT(DISTINCT bounce."ID" )),0) AS "users_messages_pushnotification_send.push_delivered",
    COUNT(DISTINCT open."ID" ) AS "users_messages_pushnotification_open.push_opens"
FROM users_messages_pushnotification_send_shared AS send
LEFT JOIN USERS_MESSAGES_PUSHNOTIFICATION_OPEN_shared AS open ON (send."USER_ID")=(open."USER_ID")
    AND
    (send."DEVICE_ID")=(open."DEVICE_ID")
    AND
    ((send."MESSAGE_VARIATION_API_ID")=(open."MESSAGE_VARIATION_API_ID")
    OR
    (send."CANVAS_STEP_API_ID")=(open."CANVAS_STEP_API_ID"))
LEFT JOIN users_messages_pushnotification_bounce_shared AS bounce ON (send."USER_ID")=(bounce."USER_ID")
    AND
    (send."DEVICE_ID")=(bounce."DEVICE_ID")
    AND
    ((send."MESSAGE_VARIATION_API_ID")=(bounce."MESSAGE_VARIATION_API_ID")
    OR
    (send."CANVAS_STEP_API_ID")=(bounce."CANVAS_STEP_API_ID"))
LIMIT 500;
```

{% endtab %}
{% tab Email Cadence %}
Vous pouvez utiliser cette requête de cadence d'envoi d'e-mails quotidienne pour analyser le délai entre les e-mails reçus par un utilisateur.

Par exemple, si un utilisateur reçoit deux e-mails en une journée, il se retrouve dans la catégorie `0 "days since last received"`. S'il reçoit un e-mail le lundi et un autre le mardi, il se retrouve dans la cohorte `1 "days since last received"`.

```sql
WITH email_messaging_cadence AS (WITH deliveries AS
      (SELECT TO_TIMESTAMP(time) AS delivered_timestamp,
      email_address AS delivered_address,
      message_variation_api_id AS d_message_variation_api_id,
      canvas_step_api_id AS d_canvas_step_api_id,
      campaign_api_id AS d_campaign_api_id,
      canvas_api_id AS d_canvas_api_id,
      id AS delivered_id,
      rank() over (partition by delivered_address ORDER BY delivered_timestamp ASC) AS delivery_event,
      min(delivered_timestamp) over (partition by delivered_address ORDER BY delivered_timestamp ASC) AS first_delivered,
      datediff(day, lag(delivered_timestamp) over (partition by delivered_address ORDER BY delivered_timestamp ASC), delivered_timestamp) AS diff_days,
      datediff(week, lag(delivered_timestamp) over (partition by delivered_address ORDER BY delivered_timestamp ASC), delivered_timestamp) AS diff_weeks
      from USERS_MESSAGES_EMAIL_DELIVERY_SHARED GROUP BY 1,2,3,4,5,6,7),      opens AS
      (SELECT DISTINCT email_address AS open_address,
      message_variation_api_id AS o_message_variation_api_id,
      canvas_step_api_id AS o_canvas_step_api_id
      FROM USERS_MESSAGES_EMAIL_OPEN_SHARED),      clicks AS
      (SELECT DISTINCT email_address AS click_address,
      message_variation_api_id AS c_message_variation_api_id,
      canvas_step_api_id AS c_canvas_step_api_id
      FROM USERS_MESSAGES_EMAIL_CLICK_SHARED)      SELECT * FROM deliveries
      LEFT JOIN opens
      ON (deliveries.delivered_address)=(opens.open_address)
      AND ((deliveries.d_message_variation_api_id)=(opens.o_message_variation_api_id) OR (deliveries.d_canvas_step_api_id)=(opens.o_canvas_step_api_id))
      LEFT JOIN clicks
      ON (deliveries.delivered_address)=(clicks.click_address)
      AND ((deliveries.d_message_variation_api_id)=(clicks.c_message_variation_api_id) OR (deliveries.d_canvas_step_api_id)=(clicks.c_canvas_step_api_id))
      )
SELECT
    email_messaging_cadence."DIFF_DAYS"  AS "email_messaging_cadence.days_since_last_received",
    (count(distinct email_messaging_cadence."OPEN_ADDRESS", email_messaging_cadence."O_MESSAGE_VARIATION_API_ID")
      +count(distinct email_messaging_cadence."OPEN_ADDRESS", email_messaging_cadence."O_CANVAS_STEP_API_ID"))/(COUNT(DISTINCT email_messaging_cadence."DELIVERED_ID" ))  AS "email_messaging_cadence.unique_open_rate"
FROM email_messaging_cadence GROUP BY 1
ORDER BY 1
LIMIT 500;
```
{% endtab %}
{% tab Unique Email Clicks %}

Vous pouvez utiliser cette requête de clics e-mail uniques pour analyser les clics e-mail uniques dans une fenêtre de temps donnée. L'algorithme de calcul est le suivant :
  1. Partitionner les événements par la clé (`app_group_id`, `message_variation_id`, `dispatch_id`, `email_address`).
  2. Dans chaque partition, ordonner les événements par date ; le premier événement est toujours un événement unique.
  3. Pour chaque événement suivant, s'il s'est produit plus de sept jours après son prédécesseur, il est considéré comme un événement unique.

Vous pouvez utiliser les [fonctions de fenêtrage](https://docs.snowflake.com/en/sql-reference/functions-analytic.html) de Snowflake pour y parvenir. La requête suivante renvoie tous les clics e-mail des 365 derniers jours et indique quels événements sont uniques dans la colonne `is_unique` :

```sql
SELECT id, app_group_id, message_variation_api_id, dispatch_id, email_address, time,
  ROW_NUMBER()       OVER (PARTITION BY app_group_id, message_variation_api_id, dispatch_id, email_address order by time) row_number,
  LAG(time, 1, time) OVER (PARTITION BY app_group_id, message_variation_api_id, dispatch_id, email_address order by time) previous_time,
  time - previous_time AS diff,
  IFF(row_number = 1, true, IFF(diff >= 7*24*3600, true, false)) AS is_unique
FROM USERS_MESSAGES_EMAIL_CLICK_SHARED
WHERE
  time < DATE_PART('EPOCH_SECOND', TO_TIMESTAMP(CURRENT_TIMESTAMP()))
  AND time > DATE_PART('EPOCH_SECOND', TO_TIMESTAMP(CURRENT_TIMESTAMP())) - 365*24*3600;
```

Si vous souhaitez uniquement voir les événements uniques, utilisez la clause `QUALIFY` :
```sql
SELECT id, app_group_id, message_variation_api_id, dispatch_id, email_address, time,
  ROW_NUMBER()       OVER (PARTITION BY app_group_id, message_variation_api_id, dispatch_id, email_address order by time) row_number,
  LAG(time, 1, time) OVER (PARTITION BY app_group_id, message_variation_api_id, dispatch_id, email_address order by time) previous_time,
  time - previous_time AS diff,
  IFF(row_number = 1, true, IFF(diff >= 7*24*3600, true, false)) AS is_unique
FROM USERS_MESSAGES_EMAIL_CLICK_SHARED
WHERE
  time < DATE_PART('EPOCH_SECOND', TO_TIMESTAMP(CURRENT_TIMESTAMP()))
  AND time > DATE_PART('EPOCH_SECOND', TO_TIMESTAMP(CURRENT_TIMESTAMP())) - 365*24*3600
QUALIFY is_unique = true;
```
Pour afficher le nombre d'événements uniques regroupés par adresse e-mail :
```sql
WITH unique_events AS(
  SELECT id, app_group_id, message_variation_api_id, dispatch_id, email_address, time,
  ROW_NUMBER()       OVER (PARTITION BY app_group_id, message_variation_api_id, dispatch_id, email_address order by time) row_number,
  LAG(time, 1, time) OVER (PARTITION BY app_group_id, message_variation_api_id, dispatch_id, email_address order by time) previous_time,
  time - previous_time AS diff,
  IFF(row_number = 1, true, iff(diff >= 7*24*3600, true, false)) AS is_unique
FROM USERS_MESSAGES_EMAIL_CLICK_SHARED
WHERE
  time < DATE_PART('EPOCH_SECOND', TO_TIMESTAMP(CURRENT_TIMESTAMP()))
  AND time > DATE_PART('EPOCH_SECOND', TO_TIMESTAMP(CURRENT_TIMESTAMP())) - 365*24*3600
QUALIFY is_unique = true)
SELECT email_address, count(*) AS count
FROM unique_events
GROUP BY email_address;
```
{% endtab %}
{% tab Unique Email Opens %}

Utilisez cette requête d'ouvertures e-mail uniques pour analyser les ouvertures e-mail uniques dans une fenêtre de temps donnée. L'algorithme de calcul est le suivant :
  1. Partitionner les événements par la clé (`app_group_id`, `message_variation_id`, `dispatch_id`, `email_address`).
  2. Dans chaque partition, ordonner les événements par date. Le premier événement est toujours un événement unique.
  3. Pour chaque événement suivant, s'il s'est produit plus de sept jours après son prédécesseur, il est considéré comme un événement unique.

Vous pouvez utiliser les [fonctions de fenêtrage](https://docs.snowflake.com/en/sql-reference/functions-analytic.html) de Snowflake pour y parvenir. La requête suivante renvoie toutes les ouvertures e-mail des 365 derniers jours et indique quels événements sont uniques dans la colonne `is_unique` :

```sql
SELECT id, app_group_id, message_variation_api_id, dispatch_id, email_address, time,
  ROW_NUMBER()       OVER (PARTITION BY app_group_id, message_variation_api_id, dispatch_id, email_address order by time) row_number,
  LAG(time, 1, time) OVER (PARTITION BY app_group_id, message_variation_api_id, dispatch_id, email_address order by time) previous_time,
  time - previous_time AS diff,
  IFF(row_number = 1, true, IFF(diff >= 7*24*3600, true, false)) AS is_unique
FROM USERS_MESSAGES_EMAIL_OPEN_SHARED
WHERE
  time < DATE_PART('EPOCH_SECOND', TO_TIMESTAMP(CURRENT_TIMESTAMP()))
  AND time > DATE_PART('EPOCH_SECOND', TO_TIMESTAMP(CURRENT_TIMESTAMP())) - 365*24*3600;
```

Pour ne renvoyer que les événements uniques, utilisez la clause `QUALIFY` :
```sql
SELECT id, app_group_id, message_variation_api_id, dispatch_id, email_address, time,
  ROW_NUMBER()       OVER (PARTITION BY app_group_id, message_variation_api_id, dispatch_id, email_address order by time) row_number,
  LAG(time, 1, time) OVER (PARTITION BY app_group_id, message_variation_api_id, dispatch_id, email_address order by time) previous_time,
  time - previous_time AS diff,
  IFF(row_number = 1, true, IFF(diff >= 7*24*3600, true, false)) AS is_unique
FROM USERS_MESSAGES_EMAIL_OPEN_SHARED
WHERE
  time < DATE_PART('EPOCH_SECOND', TO_TIMESTAMP(CURRENT_TIMESTAMP()))
  AND time > DATE_PART('EPOCH_SECOND', TO_TIMESTAMP(CURRENT_TIMESTAMP())) - 365*24*3600
QUALIFY is_unique = true;
```

Pour afficher le nombre d'événements uniques regroupés par adresse e-mail :
```sql
WITH unique_events AS(
  SELECT id, app_group_id, message_variation_api_id, dispatch_id, email_address, time,
  ROW_NUMBER()       OVER (PARTITION BY app_group_id, message_variation_api_id, dispatch_id, email_address order by time) row_number,
  LAG(time, 1, time) OVER (PARTITION BY app_group_id, message_variation_api_id, dispatch_id, email_address order by time) previous_time,
  time - previous_time AS diff,
  IFF(row_number = 1, true, iff(diff >= 7*24*3600, true, false)) AS is_unique
FROM USERS_MESSAGES_EMAIL_OPEN_SHARED
WHERE
  time < DATE_PART('EPOCH_SECOND', TO_TIMESTAMP(CURRENT_TIMESTAMP()))
  AND time > DATE_PART('EPOCH_SECOND', TO_TIMESTAMP(CURRENT_TIMESTAMP())) - 365*24*3600
QUALIFY is_unique = true)
SELECT email_address, count(*) AS count
FROM unique_events
GROUP BY email_address;
```

Pour une approche alternative limitée à une Campaign, un Canvas ou une étape du Canvas spécifique, utilisez la requête suivante. Définissez la plage de dates et les variables d'identifiant, puis exécutez les instructions `SELECT` pour obtenir les ouvertures uniques calculées de trois manières différentes.

Les résultats de la requête peuvent différer légèrement des indicateurs du tableau de bord dans certains espaces de travail. Par exemple, l'unicité peut être partitionnée par `email_address`, et certains événements d'ouverture historiques peuvent ne pas inclure d'adresse e-mail après la suppression d'un profil. Dans ces cas, une parité exacte peut ne pas être possible pour la même période.

Cet exemple renvoie trois comptages :

- **Ouvertures uniques (sur 7 jours) :** ouvertures uniques sur une période glissante de sept jours.
- **Ouvertures uniques (pendant la fenêtre de dates) :** ouvertures uniques au cours de la période donnée, indépendamment de toute ouverture survenue avant cette période.
- **Ouvertures uniques (pour les e-mails distribués dans le même intervalle) :** ouvertures uniques dont l'événement de distribution associé s'est également produit dans la même fenêtre.

{% raw %}
```sql
/*
    Set or comment out variables if not required. These are set per session.
    You can obtain the from and to dates from the Campaign/Canvas/Canvas step URL. These are the startDate and endDate parameters.

    For example, endDate=1234567890&startDate=1234500000

    To run, select all of this code block (CMD + A) and run to first set the necessary variables and run the SELECT statements below.
*/

SET fromDateTime = '1234500000';
SET toDateTime = '1234567890';
-- SET campaignID = '';
-- SET canvasID = '';
SET canvasStepID = '0123456789abcdef01234567';

SELECT
    'Unique Opens (over 7 days)' metric, COUNT(DISTINCT(user_id, dispatch_id)) total
FROM
    users_messages_email_open_shared
WHERE
/* Comment out where not required */
    -- campaign_id = $campaignID AND
    -- canvas_id = $canvasID AND
    canvas_step_id = $canvasStepID AND
    time BETWEEN $fromDateTime and $toDateTime AND
    not exists (select
                umeo.user_id
            from
                users_messages_email_open_shared umeo
            where
                umeo.user_id = users_messages_email_open_shared.user_id and
                umeo.canvas_step_id = users_messages_email_open_shared.canvas_step_id and
                to_timestamp(umeo.time) between dateadd(day, -7, to_timestamp(users_messages_email_open_shared.time)) and dateadd(second, -1, to_timestamp(users_messages_email_open_shared.time)))
UNION
SELECT
    'Unique Opens (during date window)' metric, COUNT(DISTINCT(user_id, dispatch_id)) total
FROM
    users_messages_email_open_shared
WHERE
/* Comment out where not required */
    -- campaign_id = $campaignID AND
    -- canvas_id = $canvasID AND
    canvas_step_id = $canvasStepID AND
    time BETWEEN $fromDateTime and $toDateTime
UNION
SELECT
    'Unique Opens (for emails delivered within same timeframe)' metric, COUNT(DISTINCT(user_id, dispatch_id)) total
FROM
    users_messages_email_open_shared
WHERE
/* Comment out where not required */
    -- campaign_id = $campaignID AND
    -- canvas_id = $canvasID AND
    canvas_step_id = $canvasStepID AND
    time BETWEEN $fromDateTime and $toDateTime AND
    EXISTS (select user_id
            from users_messages_email_delivery_shared umed
            where
                umed.user_id = users_messages_email_open_shared.user_id and
                umed.dispatch_id = users_messages_email_open_shared.dispatch_id and
                umed.time between $fromDateTime and $toDateTime);
```
{% endraw %}
{% endtab %}
{% endtabs %}