---
nav_title: "Ejemplos de consultas"
article_title: Consultas de ejemplo de Snowflake
page_order: 1
description: "Esta página del partner ofrece algunas consultas de ejemplo de posibles casos de uso como referencia a la hora de configurar tus consultas de Snowflake."
page_type: partner
search_tag: Partner

---

# Consultas de ejemplo {#sample-queries}

> Esta página del partner ofrece algunas consultas de ejemplo de posibles casos de uso como referencia a la hora de configurar tus consultas.

{% tabs %}
{% tab Filter By Time%}

Una consulta habitual podría ser filtrar los eventos por tiempo.

Puedes filtrarlos por la hora en que se produjeron. Las tablas de eventos están agrupadas por `time`, lo que hace que filtrar por `time` sea óptimo:
```sql
-- find custom events that occurred after 04/15/2019 @ 7:02pm (UTC) i.e., timestamp=1555354920
SELECT *
FROM users_behaviors_customevent_shared
WHERE time > 1555354920
LIMIT 10;
```
También puedes filtrar los eventos por la hora a la que se persistieron en el almacén de datos de Snowflake utilizando `sf_created_at`. `sf_created_at` y `time` no son lo mismo, pero suelen estar cerca, por lo que esta consulta debería tener características de rendimiento similares:
```sql
-- find custom events that arrived in Snowflake after time 04/15/2019 @ 7:02pm (UTC)
SELECT *
FROM users_behaviors_customevent_shared
WHERE sf_created_at > to_timestamp_ntz('2019-04-15 19:02:00')
LIMIT 10;
```
{% alert note %}
El valor de `sf_created_at` solo es fiable para los eventos que se persistieron después de `Nov 15th, 2019 9:31 pm UTC`.
{% endalert %}
{% endtab %}

{% tab Querying Changelogs%}

Los nombres de las Campaigns y de los Canvas no están presentes en los propios eventos. En su lugar, se publican en una tabla de registro de cambios.

Puedes ver los nombres de Campaign de los eventos relacionados con una Campaign uniéndolos a la tabla de registro de cambios de Campaign mediante una consulta como la siguiente:

```sql
SELECT event.id, event.time, ccs.time, ccs.name, ccs.conversion_behaviors[event.conversion_behavior_index]
FROM USERS_CAMPAIGNS_CONVERSION_SHARED event
LEFT JOIN CHANGELOGS_CAMPAIGN_SHARED ccs
ON ccs.id = event.campaign_id
AND ccs.time < event.time
qualify row_number() over (partition by event.id ORDER BY ccs.time DESC) = 1;
```
Algunas cosas importantes a tener en cuenta:
- Aquí se utilizan las funciones de [ventana](https://docs.snowflake.com/en/sql-reference/functions-analytic.html) de Snowflake.
- La unión a la izquierda garantizará que también se incluyan los eventos no relacionados con una Campaign.
- Si ves eventos con `campaign_id`s pero sin nombres de Campaign, existe la posibilidad de que la Campaign se creara con un nombre antes de que el uso compartido de datos existiera como producto.
- Puedes ver los nombres de los Canvas utilizando una consulta similar, pero uniéndolos a la tabla `CHANGELOGS_CANVAS_SHARED`.

Si deseas ver tanto los nombres de las Campaigns como los de los Canvas, es posible que tengas que utilizar la siguiente subconsulta:
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

Puedes utilizar esta consulta de embudo push para agregar datos de eventos en bruto de envíos push, datos de eventos en bruto de entregas y datos de eventos en bruto de aperturas. Esta consulta muestra cómo deben unirse todas las tablas, ya que cada evento en bruto suele tener una tabla independiente:

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
Puedes utilizar esta consulta de cadencia diaria de mensajería por correo electrónico para analizar el tiempo transcurrido entre los correos electrónicos que recibe un usuario.

Por ejemplo, si un usuario recibe dos correos electrónicos en un día, entraría en `0 "days since last received"`. Si recibió un correo electrónico el lunes y otro el martes, entraría en la cohorte `1 "days since last received"`.

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

Puedes utilizar esta consulta de clics únicos de correo electrónico para analizar los clics únicos de correo electrónico en una ventana de tiempo determinada. El algoritmo para calcularlo es el siguiente:
  1. Particionar los eventos por la clave (`app_group_id`, `message_variation_id`, `dispatch_id`, `email_address`).
  2. En cada partición, ordenar los eventos por tiempo; el primer evento siempre es un evento único.
  3. Para cada evento posterior, si ocurrió más de siete días después de su predecesor, se considera un evento único.

Podemos utilizar las [funciones de ventana](https://docs.snowflake.com/en/sql-reference/functions-analytic.html) de Snowflake para lograrlo. La siguiente consulta nos da todos los clics de correo electrónico en los últimos 365 días e indica qué eventos son únicos en la columna `is_unique`:

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

Si solo quieres ver los eventos únicos, utiliza la cláusula `QUALIFY`:
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
Para ver recuentos de eventos únicos agrupados por dirección de correo electrónico:
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

Utiliza esta consulta de Unique Opens de correo electrónico para analizar las aperturas únicas de correo electrónico en una ventana de tiempo determinada. El algoritmo para calcularlo es el siguiente:
  1. Particionar los eventos por la clave (`app_group_id`, `message_variation_id`, `dispatch_id`, `email_address`).
  2. En cada partición, ordenar los eventos por tiempo. El primer evento siempre es un evento único.
  3. Para cada evento posterior, si ocurrió más de siete días después de su predecesor, se considera un evento único.

Puedes utilizar las [funciones de ventana](https://docs.snowflake.com/en/sql-reference/functions-analytic.html) de Snowflake para lograrlo. La siguiente consulta devuelve todas las aperturas de correo electrónico en los últimos 365 días e indica qué eventos son únicos en la columna `is_unique`:

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

Para devolver solo los eventos únicos, utiliza la cláusula `QUALIFY`:
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

Para ver recuentos de eventos únicos agrupados por dirección de correo electrónico:
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

Para un enfoque alternativo limitado a una Campaign, un Canvas o un paso en Canvas específico, utiliza la siguiente consulta. Establece las variables de rango de fechas e identificador y, a continuación, ejecuta las sentencias `SELECT` para obtener las aperturas únicas calculadas de tres formas:

Los resultados de la consulta pueden diferir ligeramente de las métricas del panel en algunos espacios de trabajo. Por ejemplo, la unicidad puede particionarse por `email_address`, y algunos eventos de apertura históricos pueden no incluir una dirección de correo electrónico tras la eliminación del perfil. En esos casos, puede que no sea posible una paridad exacta para el mismo periodo de tiempo.

Este ejemplo devuelve tres recuentos:

- **Unique Opens (en 7 días):** aperturas únicas en un periodo continuo de siete días.
- **Unique Opens (durante la ventana de fechas):** aperturas únicas dentro del periodo de tiempo indicado, independientemente de cualquier apertura que haya ocurrido antes de dicho periodo.
- **Unique Opens (para correos electrónicos entregados en el mismo periodo):** aperturas únicas en las que el evento de entrega asociado también ocurrió dentro de la misma ventana.

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