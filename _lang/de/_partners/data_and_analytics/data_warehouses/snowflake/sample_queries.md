---
nav_title: "Musterabfragen"
article_title: Snowflake-Musterabfragen
page_order: 1
description: "Auf dieser Partnerseite finden Sie einige Beispielabfragen für mögliche Anwendungsfälle, auf die Sie beim Einrichten Ihrer Snowflake-Abfragen zurückgreifen können."
page_type: partner
search_tag: Partner

---

# Musterabfragen {#sample-queries}

> Auf dieser Partnerseite finden Sie einige Beispielabfragen für mögliche Anwendungsfälle, auf die Sie beim Einrichten Ihrer Abfragen zurückgreifen können.

{% tabs %}
{% tab Filter By Time%}

Eine gängige Abfrage ist das Filtern von Events nach Zeit.

Sie können sie nach dem Zeitpunkt des Vorkommens filtern. Die Event-Tabellen sind nach `time` geclustert, sodass die Filterung nach `time` optimal ist:
```sql
-- find custom events that occurred after 04/15/2019 @ 7:02pm (UTC) i.e., timestamp=1555354920
SELECT *
FROM users_behaviors_customevent_shared
WHERE time > 1555354920
LIMIT 10;
```
Sie können Events auch nach dem Zeitpunkt filtern, zu dem sie im Snowflake Data Warehouse persistiert wurden, indem Sie `sf_created_at` verwenden. `sf_created_at` und `time` sind nicht identisch, liegen aber in der Regel nahe beieinander, sodass diese Abfrage ähnliche Performance-Eigenschaften haben sollte:
```sql
-- find custom events that arrived in Snowflake after time 04/15/2019 @ 7:02pm (UTC)
SELECT *
FROM users_behaviors_customevent_shared
WHERE sf_created_at > to_timestamp_ntz('2019-04-15 19:02:00')
LIMIT 10;
```
{% alert note %}
Der Wert von `sf_created_at` ist nur für Events zuverlässig, die nach dem `15. November 2019, 21:31 Uhr UTC` persistiert wurden.
{% endalert %}
{% endtab %}

{% tab Querying Changelogs%}

Campaign- und Canvas-Namen sind nicht in den Events selbst enthalten. Stattdessen werden sie in einer Changelog-Tabelle veröffentlicht.

Sie können Campaign-Namen für Events im Zusammenhang mit einer Campaign anzeigen, indem Sie über eine Abfrage wie die folgende mit der Campaign-Changelog-Tabelle verknüpfen:

```sql
SELECT event.id, event.time, ccs.time, ccs.name, ccs.conversion_behaviors[event.conversion_behavior_index]
FROM USERS_CAMPAIGNS_CONVERSION_SHARED event
LEFT JOIN CHANGELOGS_CAMPAIGN_SHARED ccs
ON ccs.id = event.campaign_id
AND ccs.time < event.time
qualify row_number() over (partition by event.id ORDER BY ccs.time DESC) = 1;
```
Einige wichtige Punkte sind zu beachten:
- Hier werden die [Fensterfunktionen](https://docs.snowflake.com/en/sql-reference/functions-analytic.html) von Snowflake verwendet.
- Der Left Join sorgt dafür, dass auch Events, die nicht mit einer Campaign in Verbindung stehen, berücksichtigt werden.
- Wenn Sie Events mit `campaign_id`s sehen, aber keine Campaign-Namen, besteht die Möglichkeit, dass die Campaign mit einem Namen erstellt wurde, bevor Datenfreigabe als Produkt existierte.
- Sie können Canvas-Namen mit einer ähnlichen Abfrage anzeigen, indem Sie stattdessen mit der Tabelle `CHANGELOGS_CANVAS_SHARED` verknüpfen.

Wenn Sie sowohl Campaign- als auch Canvas-Namen sehen möchten, müssen Sie möglicherweise die folgende Unterabfrage verwenden:
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

Sie können diese Push-Funnel-Abfrage verwenden, um Push-Sende-Rohdaten über Zustellungs-Rohdaten bis hin zu Öffnungs-Rohdaten zu aggregieren. Diese Abfrage zeigt, wie alle Tabellen miteinander verknüpft werden sollten, da jedes Rohereignis in der Regel eine eigene Tabelle hat:

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
Mit dieser Abfrage zur täglichen E-Mail-Messaging-Kadenz können Sie die Zeitspanne zwischen den E-Mails analysieren, die Nutzer:innen erhalten.

Wenn Nutzer:innen zum Beispiel zwei E-Mails an einem Tag erhalten haben, fallen diese unter `0 "days since last received"`. Wenn sie eine E-Mail am Montag und eine am Dienstag erhalten haben, würden sie in die Kohorte `1 "days since last received"` fallen.

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

Sie können diese Abfrage für eindeutige E-Mail-Klicks verwenden, um die eindeutigen E-Mail-Klicks in einem bestimmten Zeitfenster zu analysieren. Der Algorithmus zur Berechnung lautet wie folgt:
  1. Unterteilen Sie die Events nach dem Schlüssel (`app_group_id`, `message_variation_id`, `dispatch_id`, `email_address`).
  2. Ordnen Sie die Events in jeder Partition nach Zeit, wobei das erste Event immer ein eindeutiges Event ist.
  3. Jedes nachfolgende Event, das mehr als sieben Tage nach seinem Vorgänger eintritt, wird als eindeutiges Event betrachtet.

Dazu können wir die [Fensterfunktionen](https://docs.snowflake.com/en/sql-reference/functions-analytic.html) von Snowflake verwenden. Die folgende Abfrage liefert uns alle E-Mail-Klicks der letzten 365 Tage und zeigt in der Spalte `is_unique` an, welche Events eindeutig sind:

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

Wenn Sie nur die eindeutigen Events sehen möchten, verwenden Sie die `QUALIFY`-Klausel:
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
Um die Anzahl eindeutiger Events gruppiert nach E-Mail-Adresse anzuzeigen:
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

Verwenden Sie diese Abfrage, um **eindeutige Öffnungen** aus Snowflake-E-Mail-Öffnungs-Events zu approximieren – zum Beispiel, um sie mit der Spalte **Unique Opens** im Dashboard abzugleichen.

Dieses Beispiel gibt drei Zählwerte zurück:

- **Unique Opens (over 7 days):** Eindeutige Öffnungen über einen rollierenden Zeitraum von sieben Tagen.
- **Unique Opens (during date window):** Eindeutige Öffnungen innerhalb des angegebenen Zeitraums. Dies gilt unabhängig von Öffnungen, die vor dem Zeitraum stattgefunden haben.
- **Unique Opens (for emails delivered within same timeframe):** Eindeutige Öffnungen, bei denen das zugehörige Zustellungs-Event ebenfalls innerhalb desselben Fensters stattfand (nützlich, wenn Sie nur Öffnungen für Nachrichten sehen möchten, die in diesem Zeitraum zugestellt wurden).

{% raw %}
```sql
/*
    Set or comment out variables if not required. These are set per session.
    You can obtain the from and to dates from the Campaign/Canvas/Canvas step URL. These are the startDate and endDate parameters.

    For example, endDate=1656799199&startDate=1656194400

    To run, select all of this code block (CMD + A) and run to first set the necessary variables and run the SELECT statements below.
*/

SET fromDateTime = '1656194400';
SET toDateTime = '1656799199';
-- SET campaignID = '';
-- SET canvasID = '';
SET canvasStepID = '61b0a249745a0c5ac67a11d3';

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