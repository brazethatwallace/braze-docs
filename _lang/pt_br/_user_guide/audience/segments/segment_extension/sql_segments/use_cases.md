---
nav_title: "Casos de uso"
article_title: Casos de uso de extensões de Segment or segmento or segmento SQL
page_order: 2
page_type: glossary
layout: sql_segment_extensions_glossary
alias: "/sql_segments_use_cases/"
description: "Este artigo contém consultas testadas e comprovadas para extensões de Segment or segmento or segmento SQL."
tool: Segments
---

{% API or interface de programação do aplicativo (API) %}
## Selecionar usuários pela quantidade de vezes que um evento ocorreu {#select-users-by-how-many-times-an-event-has-occurred}
{% apitags %}
Event
{% endapitags %}

Selecione usuários que abriram uma determinada Campaign de e-mail mais de uma vez no passado.

Isso também funciona para limitar mensagens no app pelo número de impressões, como selecionar usuários com mais de três impressões como exclusão de Segment or segmento or segmento na mesma Campaign.

```sql
SELECT user_id FROM "USERS_MESSAGES_EMAIL_OPEN_SHARED"
WHERE campaign_api_id='8f7026dc-e9b7-40e6-bdc7-96cf58e80faa'
GROUP BY user_id
HAVING count(*) > 1
```
{% endapi %}

{% API or interface de programação do aplicativo (API) %}
## Selecionar usuários que realizaram uma ação e somar o valor de uma propriedade {#select-users-that-performed-an-action-and-sum-up-a-property-value}
{% apitags %}
Property
{% endapitags %}

Selecione usuários que fizeram uma aposta em esportes com a soma de todas as suas apostas sendo maior que um determinado valor.

```sql
select user_id from "USERS_BEHAVIORS_CUSTOMEVENT_SHARED"
where name='Bet On Sports'
group by 1 having sum(get_path(parse_json(properties), 'amount')) > 150
```
{% endapi %}

{% API or interface de programação do aplicativo (API) %}
## Selecionar usuários com base na quantidade de vezes que um evento ocorreu em um intervalo de tempo {#select-users-based-on-how-many-times-an-event-occurred-in-a-time-range}
{% apitags %}
Event, Time range
{% endapitags %}

Selecione usuários com mais de três aberturas de e-mail nos últimos 30 dias.

Isso também funciona para determinar os níveis de engajamento dos usuários, como usuários altamente responsivos em diferentes canais.

```sql
SELECT user_id, COUNT(DISTINCT id) AS num_emails_opened
FROM USERS_MESSAGES_EMAIL_OPEN_SHARED
WHERE to_timestamp_ntz(time) >= DATEADD(day, -30, CURRENT_TIMESTAMP()) AND to_timestamp_ntz(time) <= CURRENT_TIMESTAMP()
GROUP BY user_id;
HAVING COUNT(DISTINCT id) > 3
```
{% endapi %}

{% API or interface de programação do aplicativo (API) %}
## Selecionar usuários que registraram pelo menos um evento em múltiplos intervalos de tempo {#select-users-that-recorded-at-least-one-event-across-multiple-time-ranges}
{% apitags %}
Event, Time range
{% endapitags %}

Selecione usuários que fizeram uma compra em cada um dos últimos quatro trimestres. Esse Segment or segmento or segmento de usuários pode ser usado com [audience sync]({{site.baseurl}}/partners/canvas_audience_sync) para identificar clientes semelhantes de alto valor para aquisição.

```sql
ELECT DISTINCT user_id
FROM USERS_BEHAVIORS_PURCHASE_SHARED
WHERE to_timestamp_ntz(time) >= DATEADD(day, -90, CURRENT_TIMESTAMP()) AND to_timestamp_ntz(time) <= CURRENT_TIMESTAMP()
INTERSECT
SELECT DISTINCT user_id
FROM USERS_BEHAVIORS_PURCHASE_SHARED
WHERE to_timestamp_ntz(time) >= DATEADD(day, -180, CURRENT_TIMESTAMP()) AND to_timestamp_ntz(time) <= DATEADD(day, -91, CURRENT_TIMESTAMP())
INTERSECT
SELECT DISTINCT user_id
FROM USERS_BEHAVIORS_PURCHASE_SHARED
WHERE to_timestamp_ntz(time) >= DATEADD(day, -270, CURRENT_TIMESTAMP()) AND to_timestamp_ntz(time) <= DATEADD(day, -181, CURRENT_TIMESTAMP())
INTERSECT
SELECT DISTINCT user_id
FROM USERS_BEHAVIORS_PURCHASE_SHARED
WHERE to_timestamp_ntz(time) >= DATEADD(day, -365, CURRENT_TIMESTAMP()) AND to_timestamp_ntz(time) <= DATEADD(day, -271, CURRENT_TIMESTAMP());
```
{% endapi %}

{% API or interface de programação do aplicativo (API) %}
## Selecionar qualquer compra com determinadas propriedades {#select-any-purchase-with-certain-properties}
{% apitags %}
Purchase, Property
{% endapitags %}

Selecione clientes que fizeram qualquer compra contendo a propriedade `"type = shops"` nos últimos 14 dias.

```sql
SELECT
user_id
FROM
USERS_BEHAVIORS_PURCHASE_SHARED
WHERE
product_id IS NOT NULL
AND
get_path(
parse_json(properties),
'propertyname'
) = 'propertyvalue'
AND
to_timestamp_ntz(time) >= DATEADD(day, -14, CURRENT_TIMESTAMP())
AND
to_timestamp_ntz(time) <= CURRENT_TIMESTAMP()
GROUP BY 1
HAVING COUNT(id) > 0;
```
{% endapi %}

{% API or interface de programação do aplicativo (API) %}
## Selecionar usuários que receberam uma mensagem que não foi entregue {#select-users-that-were-sent-a-message-that-wasnt-delivered}
{% apitags %}
Message, Delivery
{% endapitags %}

Selecione usuários que receberam o envio de uma Campaign ou Canvas de SMS, mas a mensagem não chegou à operadora. Por exemplo, a mensagem pode ter sido interrompida por um estouro de fila.

```sql
SELECT
user_id
FROM
USERS_MESSAGES_SMS_SEND_SHARED
WHERE
CANVAS_ID='63067c50740cc3377f8200d5'
AND TO_PHONE_NUMBER NOT IN (SELECT TO_PHONE_NUMBER FROM USERS_MESSAGES_SMS_CARRIERSEND_SHARED WHERE CANVAS_ID='63067c50740cc3377f8200d5')
GROUP BY 1
HAVING COUNT(id) > 0;
```
{% endapi %}

{% API or interface de programação do aplicativo (API) %}
## Encontrar todas as mensagens SMS que foram enviadas mas não chegaram à operadora por causa de estouro de fila {#find-all-sms-messages-that-were-sent-but-didnt-reach-the-carrier-because-of-queue-overflow}
{% apitags %}
Message, Carrier
{% endapitags %}

Isso pode ser reutilizado para outros tipos de mensagens enviadas de um Canvas específico que não foram entregues.

```sql
SELECT
user_id
FROM
USERS_MESSAGES_SMS_SEND_SHARED
WHERE
CANVAS_ID='id pulled from URL'
AND TO_PHONE_NUMBER NOT IN (SELECT TO_PHONE_NUMBER FROM USERS_MESSAGES_SMS_CARRIERSEND_SHARED WHERE CANVAS_ID='id pulled from URL')
GROUP BY 1
HAVING COUNT(id) > 0;
```
`CANVAS_ID` é o número após `/canvas/` na URL do seu Canvas.
{% endapi %}

{% API or interface de programação do aplicativo (API) %}
## Selecionar usuários que fizeram qualquer compra com um array de propriedades contendo um valor específico {#select-users-that-made-any-purchase-with-a-property-array-containing-a-specific-value}
{% apitags %}
Purchase, Property
{% endapitags %}

```sql
SELECT DISTINCT EXTERNAL_USER_ID
FROM "USERS_BEHAVIORS_PURCHASE_SHARED",
LATERAL FLATTEN(input=>parse_json(properties):modifiers) as f
WHERE f.VALUE::STRING = 'Bacon'
```
{% endapi %}

{% API or interface de programação do aplicativo (API) %}
## Encontrar todos os usuários que tiveram múltiplos erros 30003 e 0 entregas {#find-all-users-that-had-multiple-30003-errors-and-0-deliveries}
{% apitags %}
Error, Delivery
{% endapitags %}

Isso é útil para resolver situações em que você deseja parar de enviar para usuários que não estão recebendo mensagens, mas não estão sendo marcados como inválidos porque não possuem o código de erro necessário. Você pode redirecionar esses usuários para atualizar o número de telefone ou cancelar a inscrição deles.

Essa consulta usa o editor incremental e busca usuários com três ou mais envios rejeitados nos últimos 90 dias e zero entregas.

```sql
SELECT
  $date(time), user_id, COUNT(id)
FROM
  USERS_MESSAGES_SMS_REJECTION_SHARED
WHERE
  provider_error_code = '30003'
  AND
  time > $start_date
    AND TO_PHONE_NUMBER NOT IN (SELECT TO_PHONE_NUMBER FROM USERS_MESSAGES_SMS_DELIVERY_SHARED)
GROUP BY 1, 2;
```
{% endapi %}

{% API or interface de programação do aplicativo (API) %}
## Encontrar usuários com propriedades de evento específicas e contagens de eventos em um intervalo de tempo {#find-users-with-specific-event-properties-and-event-counts-in-a-time-range}
{% apitags %}
Event, Property, Time range
{% endapitags %}

Encontre usuários que atendam às seguintes condições simultaneamente:

- Realizaram transações com um valor total superior a $500 (a soma de múltiplos eventos `Transact`)
- Realizaram transações no shopping `Funan`
- Realizaram transações mais de três vezes nos últimos 90 dias

```sql
SELECT
USER_ID
FROM
USERS_BEHAVIORS_CUSTOMEVENT_SHARED
WHERE
TIME > $start_date
AND NAME = 'Transact'
AND get_path(parse_json(properties), 'mall') = 'Funan'
GROUP BY
USER_ID
HAVING
SUM(get_path(parse_json(properties), 'total_value')) > 500
AND COUNT(*) > 3
```
{% endapi %}

{% API or interface de programação do aplicativo (API) %}
## Selecionar usuários cuja sessão mais recente foi em um modelo de dispositivo específico {#select-users-whose-most-recent-session-was-on-a-specific-device-model}
{% apitags %}
Session, Device
{% endapitags %}

```sql
select user_id, external_user_id, device_id, platform, os_version, device_model, to_timestamp(max(time)) last_session
from users_behaviors_app_sessionstart
where app_group_id = ''
and date_trunc(day, to_timestamp(time)) <= to_timestamp('2023-08-07')
and device_model = ''
group by user_id, external_user_id, device_id, platform, os_version, device_model
```
{% endapi %}

{% API or interface de programação do aplicativo (API) %}
## Encontrar usuários que selecionaram o segundo botão de uma mensagem no app em um intervalo de tempo específico {#find-users-that-selected-the-second-button-of-an-in-app-message-in-a-specific-time-range}
{% apitags %}
Time range
{% endapitags %}

```sql
SELECT DISTINCT USER_ID, to_timestamp_ntz(time)
FROM USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED
WHERE to_timestamp_ntz(time) >= '2023-08-03'::timestamp_ntz
AND to_timestamp_ntz(time) <= '2023-08-09'::timestamp_ntz
AND BUTTON_ID = '1'
AND CAMPAIGN_ID = '64c8cd9c4d38d13091957b1c'
```
{% endapi %}

{% API or interface de programação do aplicativo (API) %}
## Encontrar usuários que compraram em cada um dos últimos três meses calendário {#find-users-that-purchased-in-each-of-the-last-three-calendar-months}
{% apitags %}
Purchase, Time range
{% endapitags %}

```sql
SELECT DISTINCT user_id
FROM USERS_BEHAVIORS_PURCHASE_SHARED
WHERE to_timestamp_ntz(time) >= '2023-09-01'::timestamp_ntz
AND to_timestamp_ntz(time) <= '2023-09-30'::timestamp_ntz
INTERSECT
SELECT DISTINCT user_id
FROM USERS_BEHAVIORS_PURCHASE_SHARED
WHERE to_timestamp_ntz(time) >= '2023-10-01'::timestamp_ntz
AND to_timestamp_ntz(time) <= '2023-10-31'::timestamp_ntz
INTERSECT
SELECT DISTINCT user_id
FROM USERS_BEHAVIORS_PURCHASE_SHARED
WHERE to_timestamp_ntz(time) >= '2023-11-01'::timestamp_ntz
AND to_timestamp_ntz(time) <= '2023-11-30'::timestamp_ntz;
```
{% endapi %}

{% API or interface de programação do aplicativo (API) %}
## Selecionar usuários que concluíram um evento personalizado com uma propriedade específica quando a propriedade é um inteiro {#select-users-that-completed-a-custom-event-with-a-specific-property-when-property-is-an-integer}
{% apitags %}
Event, Property
{% endapitags %}

Enviar uma mensagem para usuários que assistiram a uma série nos últimos seis meses e estão prestes a deixar a plataforma.

A propriedade é o ID do título; caso contrário, você precisaria incluir mais de 100 IDs de título em um filtro. A extensão de Segment or segmento or segmento incremental pode ser otimizada em termos de custo, e você pode especificar o intervalo de datas no cabeçalho.

```sql
SELECT
  $date(time),
  USER_ID,
  COUNT(*)
FROM
  USERS_BEHAVIORS_CUSTOMEVENT_SHARED
WHERE
  TIME > $start_date
  AND NAME = 'event name'
  AND (PARSE_JSON(PROPERTIES):property_name::INT) IN (1, 2)
GROUP BY
  1, 2;
```
{% endapi %}

{% API or interface de programação do aplicativo (API) %}
## Encontrar a média diária de e-mails que um usuário recebe {#find-the-average-number-of-emails-a-user-receives-daily}
{% apitags %}
Message
{% endapitags %}

```sql
WITH user_email_counts AS (
  SELECT
    USER_ID,
    COUNT(*) AS total_emails,
    DATEDIFF(day, MIN(TO_DATE(DATE_TRUNC('day', TO_TIMESTAMP_NTZ(TIME)))), MAX(TO_DATE(DATE_TRUNC('day', TO_TIMESTAMP_NTZ(TIME))))) AS days
  FROM USERS_MESSAGES_EMAIL_SEND_SHARED
  GROUP BY USER_ID
  HAVING COUNT(USER_ID) > 1
),

-- Then, calculate the average number of emails received by each user daily
user_daily_average AS (
  SELECT
    USER_ID,
    days,
    CASE
      WHEN days = 0 THEN total_emails  -- If the user received all emails in one day, the average for that user is the total number of emails
      ELSE total_emails / days  -- Otherwise, it's the total number of emails divided by the number of days
    END AS daily_average
  FROM user_email_counts
)

-- The total daily average is the average of all users
SELECT
  AVG(daily_average)
FROM user_daily_average;
```

{% alert tip %}
Para mensagens SMS, substitua `USERS_MESSAGES_EMAIL_SEND_SHARED` por `USERS_MESSAGES_SMS_SEND_SHARED` na consulta. Para notificações por push, substitua `USERS_MESSAGES_EMAIL_SEND_SHARED` por `USERS_MESSAGES_SMS_SEND_SHARED` na consulta.
{% endalert %}
{% endapi %}

{% API or interface de programação do aplicativo (API) %}
## Encontrar a média semanal de e-mails que um usuário recebe {#find-the-average-number-of-emails-a-user-receives-weekly}
{% apitags %}
Message
{% endapitags %}

```sql
WITH user_email_counts AS (
  SELECT
    USER_ID,
    COUNT(*) AS total_emails,
    DATEDIFF(week, MIN(TO_DATE(DATE_TRUNC('week', TO_TIMESTAMP_NTZ(TIME)))), MAX(TO_DATE(DATE_TRUNC('week', TO_TIMESTAMP_NTZ(TIME))))) AS weeks
  FROM USERS_MESSAGES_EMAIL_SEND_SHARED
  GROUP BY USER_ID
  HAVING COUNT(USER_ID) > 1
),

-- Then, calculate the average number of emails received by each user weekly
user_weekly_average AS (
  SELECT
    USER_ID,
    CASE
      WHEN weeks = 0 THEN total_emails  -- If the user received all emails in the same week, the average is the total number of emails
      ELSE total_emails / weeks  -- Otherwise, it's the total number of emails divided by the number of weeks
    END AS weekly_average
  FROM user_email_counts
)

-- The total weekly average is the average of all users
SELECT
  AVG(weekly_average) AS average_weekly_emails
FROM user_weekly_average;
```
{% alert tip %}
Para mensagens SMS, substitua `USERS_MESSAGES_EMAIL_SEND_SHARED` por `USERS_MESSAGES_SMS_SEND_SHARED` na consulta. Para notificações por push, substitua `USERS_MESSAGES_EMAIL_SEND_SHARED` por `USERS_MESSAGES_SMS_SEND_SHARED` na consulta.
{% endalert %}
{% endapi %}