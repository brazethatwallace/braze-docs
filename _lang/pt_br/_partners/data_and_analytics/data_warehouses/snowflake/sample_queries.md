---
nav_title: "Consultas de amostra"
article_title: Consultas de amostra do Snowflake
page_order: 1
description: "Esta página de parceiro oferece algumas consultas de amostra de possíveis casos de uso para referência ao configurar suas consultas do Snowflake."
page_type: partner
search_tag: Partner

---

# Consultas de amostra {#sample-queries}

> Esta página de parceiro oferece algumas consultas de amostra de possíveis casos de uso para referência ao configurar suas consultas.

{% tabs %}
{% tab Filter By Time%}

Uma consulta comum pode ser filtrar eventos por tempo.

Você pode filtrá-los pelo horário de ocorrência. As tabelas de eventos são clusterizadas por `time`, o que torna a filtragem por `time` ideal:
```sql
-- find custom events that occurred after 04/15/2019 @ 7:02pm (UTC) i.e., timestamp=1555354920
SELECT *
FROM users_behaviors_customevent_shared
WHERE time > 1555354920
LIMIT 10;
```
Você também pode filtrar eventos pelo horário em que foram persistidos no data warehouse do Snowflake usando `sf_created_at`. `sf_created_at` e `time` não são iguais, mas geralmente são próximos, então essa consulta deve ter características de desempenho semelhantes:
```sql
-- find custom events that arrived in Snowflake after time 04/15/2019 @ 7:02pm (UTC)
SELECT *
FROM users_behaviors_customevent_shared
WHERE sf_created_at > to_timestamp_ntz('2019-04-15 19:02:00')
LIMIT 10;
```
{% alert note %}
O valor de `sf_created_at` é confiável apenas para eventos que foram persistidos após `Nov 15th, 2019 9:31 pm UTC`.
{% endalert %}
{% endtab %}

{% tab Querying Changelogs%}

Os nomes de Campaigns e os nomes de Canvas não estão presentes nos próprios eventos. Em vez disso, eles são publicados em uma tabela de changelog.

Você pode ver os nomes de Campaigns para eventos relacionados a uma Campaign fazendo um join com a tabela de changelog da Campaign usando uma consulta como:

```sql
SELECT event.id, event.time, ccs.time, ccs.name, ccs.conversion_behaviors[event.conversion_behavior_index]
FROM USERS_CAMPAIGNS_CONVERSION_SHARED event
LEFT JOIN CHANGELOGS_CAMPAIGN_SHARED ccs
ON ccs.id = event.campaign_id
AND ccs.time < event.time
qualify row_number() over (partition by event.id ORDER BY ccs.time DESC) = 1;
```
Algumas observações importantes:
- As funções de [janela](https://docs.snowflake.com/en/sql-reference/functions-analytic.html) do Snowflake são usadas aqui.
- O left join garante que eventos não relacionados a uma Campaign também sejam incluídos.
- Se você vir eventos com `campaign_id`s, mas sem nomes de Campaign, é possível que a Campaign tenha sido criada com um nome antes de o compartilhamento de dados existir como produto.
- Você pode ver os nomes de Canvas usando uma consulta semelhante, fazendo join com a tabela `CHANGELOGS_CANVAS_SHARED`.

Se você quiser ver os nomes de Campaign e de Canvas, talvez precise usar a seguinte subconsulta:
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

Você pode usar essa consulta de funil de push para agregar dados brutos de eventos de envios de push, passando por dados brutos de eventos de entregas, até dados brutos de eventos de aberturas. Essa consulta mostra como todas as tabelas devem ser unidas, já que cada evento bruto normalmente tem uma tabela separada:

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
Você pode usar essa consulta de cadência de envio de e-mail diário para analisar o intervalo entre os e-mails que um usuário recebe.

Por exemplo, se um usuário recebeu dois e-mails em um dia, ele se enquadra em `0 "days since last received"`. Se recebeu um e-mail na segunda-feira e outro na terça-feira, ele fica na coorte `1 "days since last received"`.

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

Você pode usar essa consulta de cliques únicos de e-mail para analisar os cliques únicos de e-mail em um determinado período. O algoritmo para calcular isso é o seguinte:
  1. Particione os eventos pela chave (`app_group_id`, `message_variation_id`, `dispatch_id`, `email_address`).
  2. Em cada partição, ordene os eventos por tempo. O primeiro evento é sempre um evento único.
  3. Para cada evento subsequente, se ele ocorreu mais de sete dias após o anterior, é considerado um evento único.

Podemos usar as [funções de janela](https://docs.snowflake.com/en/sql-reference/functions-analytic.html) do Snowflake para nos ajudar a alcançar isso. A consulta a seguir retorna todos os cliques de e-mail nos últimos 365 dias e indica quais eventos são únicos na coluna `is_unique`:

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

Se você quer ver apenas os eventos únicos, use a cláusula `QUALIFY`:
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
Para ver contagens de eventos únicos agrupados por endereço de e-mail:
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

Use essa consulta de aberturas únicas de e-mail para analisar as aberturas únicas de e-mail em um determinado período. O algoritmo para calcular isso é o seguinte:
  1. Particione os eventos pela chave (`app_group_id`, `message_variation_id`, `dispatch_id`, `email_address`).
  2. Em cada partição, ordene os eventos por tempo. O primeiro evento é sempre um evento único.
  3. Para cada evento subsequente, se ele ocorreu mais de sete dias após o anterior, é considerado um evento único.

Você pode usar as [funções de janela](https://docs.snowflake.com/en/sql-reference/functions-analytic.html) do Snowflake para alcançar isso. A consulta a seguir retorna todas as aberturas de e-mail nos últimos 365 dias e indica quais eventos são únicos na coluna `is_unique`:

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

Para retornar apenas os eventos únicos, use a cláusula `QUALIFY`:
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

Para ver contagens de eventos únicos agrupados por endereço de e-mail:
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

Para uma abordagem alternativa com escopo em uma Campaign, um Canvas ou uma etapa do Canvas específica, use a consulta a seguir. Defina as variáveis de intervalo de datas e identificador e, em seguida, execute as instruções `SELECT` para retornar aberturas únicas calculadas de três formas:

Os resultados da consulta podem diferir ligeiramente das métricas do dashboard em alguns espaços de trabalho. Por exemplo, a unicidade pode ser particionada por `email_address`, e alguns eventos históricos de abertura podem não incluir um endereço de e-mail após a exclusão do perfil. Nesses casos, a paridade exata pode não ser possível para o mesmo período.

Este exemplo retorna três contagens:

- **Aberturas únicas (período contínuo de 7 dias):** aberturas únicas em um período contínuo de sete dias.
- **Aberturas únicas (dentro do intervalo de datas):** aberturas únicas dentro do período especificado, independentemente de aberturas que tenham ocorrido antes desse período.
- **Aberturas únicas (para e-mails entregues no mesmo período):** aberturas únicas em que o evento de entrega correspondente também ocorreu dentro do mesmo período.

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