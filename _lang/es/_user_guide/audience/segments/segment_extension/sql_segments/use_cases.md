---
nav_title: "Casos de uso"
article_title: Casos de uso de extensiones de segmento SQL
page_order: 2
page_type: glossary
layout: sql_segment_extensions_glossary
alias: "/sql_segments_use_cases/"
description: "Este artículo contiene consultas probadas y comprobadas para extensiones de segmento SQL."
tool: Segments
---

{% api %}
## Seleccionar usuarios por la cantidad de veces que ha ocurrido un evento {#select-users-by-how-many-times-an-event-has-occurred}
{% apitags %}
Event
{% endapitags %}

Selecciona usuarios que abrieron una determinada Campaign de correo electrónico más de una vez en el pasado.

Esto también funciona para limitar mensajes dentro de la aplicación por número de impresiones, como seleccionar usuarios con más de tres impresiones como exclusión de segmento en la misma Campaign.

```sql
SELECT user_id FROM "USERS_MESSAGES_EMAIL_OPEN_SHARED"
WHERE campaign_api_id='8f7026dc-e9b7-40e6-bdc7-96cf58e80faa'
GROUP BY user_id
HAVING count(*) > 1
```
{% endapi %}

{% api %}
## Seleccionar usuarios que realizaron una acción y sumar el valor de una propiedad {#select-users-that-performed-an-action-and-sum-up-a-property-value}
{% apitags %}
Property
{% endapitags %}

Selecciona usuarios que hicieron una apuesta deportiva cuya suma total de todas sus apuestas sea mayor que una cantidad determinada.

```sql
select user_id from "USERS_BEHAVIORS_CUSTOMEVENT_SHARED"
where name='Bet On Sports'
group by 1 having sum(get_path(parse_json(properties), 'amount')) > 150
```
{% endapi %}

{% api %}
## Seleccionar usuarios en función de cuántas veces ocurrió un evento en un rango de tiempo {#select-users-based-on-how-many-times-an-event-occurred-in-a-time-range}
{% apitags %}
Event, Time range
{% endapitags %}

Selecciona usuarios con más de tres aperturas de correo electrónico en los últimos 30 días.

Esto también funciona para determinar los niveles de interacción de los usuarios, como usuarios altamente receptivos en diferentes canales.

```sql
SELECT user_id, COUNT(DISTINCT id) AS num_emails_opened
FROM USERS_MESSAGES_EMAIL_OPEN_SHARED
WHERE to_timestamp_ntz(time) >= DATEADD(day, -30, CURRENT_TIMESTAMP()) AND to_timestamp_ntz(time) <= CURRENT_TIMESTAMP()
GROUP BY user_id;
HAVING COUNT(DISTINCT id) > 3
```
{% endapi %}

{% api %}
## Seleccionar usuarios que registraron al menos un evento en múltiples rangos de tiempo {#select-users-that-recorded-at-least-one-event-across-multiple-time-ranges}
{% apitags %}
Event, Time range
{% endapitags %}

Selecciona usuarios que realizaron una compra en cada uno de los últimos cuatro trimestres. Este segmento de usuarios se puede utilizar con [audience sync]({{site.baseurl}}/partners/canvas_audience_sync) para identificar clientes similares de alto valor para la adquisición.

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

{% api %}
## Seleccionar cualquier compra con determinadas propiedades {#select-any-purchase-with-certain-properties}
{% apitags %}
Purchase, Property
{% endapitags %}

Selecciona clientes que realizaron cualquier compra que contenga la propiedad `"type = shops"` en 14 días.

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

{% api %}
## Seleccionar usuarios a los que se les envió un mensaje que no fue entregado {#select-users-that-were-sent-a-message-that-wasnt-delivered}
{% apitags %}
Message, Delivery
{% endapitags %}

Selecciona usuarios a los que se les envió una Campaign de servicio de mensajes cortos o un Canvas, pero el mensaje no llegó al operador. Por ejemplo, el mensaje podría haber sido detenido por un desbordamiento de cola.

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

{% api %}
## Encontrar todos los mensajes servicio de mensajes cortos que se enviaron pero no llegaron al operador debido a un desbordamiento de cola {#find-all-sms-messages-that-were-sent-but-didnt-reach-the-carrier-because-of-queue-overflow}
{% apitags %}
Message, Carrier
{% endapitags %}

Esto se puede reutilizar para otros tipos de mensajes enviados desde un Canvas en particular que no fueron entregados.

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
`CANVAS_ID` es el número que aparece después de `/canvas/` en la URL de tu Canvas.
{% endapi %}

{% api %}
## Seleccionar usuarios que realizaron cualquier compra con un array de propiedades que contenga un valor específico {#select-users-that-made-any-purchase-with-a-property-array-containing-a-specific-value}
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

{% api %}
## Encontrar todos los usuarios que tuvieron múltiples errores 30003 y 0 entregas {#find-all-users-that-had-multiple-30003-errors-and-0-deliveries}
{% apitags %}
Error, Delivery
{% endapitags %}

Esto es útil para resolver situaciones en las que quieres dejar de enviar a usuarios que no están recibiendo mensajes pero que no se marcan como no válidos porque no tienen el código de error requerido. Puedes reorientar a estos usuarios para que actualicen su número de teléfono o cancelar su suscripción.

Esta consulta utiliza el editor incremental y busca usuarios con tres o más envíos rechazados en los últimos 90 días y cero entregas.

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

{% api %}
## Encontrar usuarios con propiedades de evento específicas y recuentos de eventos en un rango de tiempo {#find-users-with-specific-event-properties-and-event-counts-in-a-time-range}
{% apitags %}
Event, Property, Time range
{% endapitags %}

Encuentra usuarios que cumplan las siguientes condiciones simultáneamente:

- Realizaron transacciones por un valor total superior a $500 (la suma de múltiples eventos `Transact`)
- Realizaron transacciones en el centro comercial `Funan`
- Realizaron transacciones más de tres veces en los últimos 90 días

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

{% api %}
## Seleccionar usuarios cuya sesión más reciente fue en un modelo de dispositivo específico {#select-users-whose-most-recent-session-was-on-a-specific-device-model}
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

{% api %}
## Encontrar usuarios que seleccionaron el segundo botón de un mensaje dentro de la aplicación en un rango de tiempo específico {#find-users-that-selected-the-second-button-of-an-in-app-message-in-a-specific-time-range}
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

{% api %}
## Encontrar usuarios que compraron en cada uno de los últimos tres meses calendario {#find-users-that-purchased-in-each-of-the-last-three-calendar-months}
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

{% api %}
## Seleccionar usuarios que completaron un evento personalizado con una propiedad específica cuando la propiedad es un entero {#select-users-that-completed-a-custom-event-with-a-specific-property-when-property-is-an-integer}
{% apitags %}
Event, Property
{% endapitags %}

Envía un mensaje a usuarios que vieron una serie en los últimos seis meses y están a punto de abandonar la plataforma.

La propiedad es el ID del título; de lo contrario, necesitarías incluir más de 100 ID de título en un filtro. La extensión de segmento incremental se puede optimizar en cuanto a costos y puedes especificar el rango de fechas en el encabezado.

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

{% api %}
## Encontrar el número promedio de correos electrónicos que un usuario recibe diariamente {#find-the-average-number-of-emails-a-user-receives-daily}
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
Para mensajes servicio de mensajes cortos, reemplaza `USERS_MESSAGES_EMAIL_SEND_SHARED` con `USERS_MESSAGES_SMS_SEND_SHARED` en la consulta. Para notificaciones push, reemplaza `USERS_MESSAGES_EMAIL_SEND_SHARED` con `USERS_MESSAGES_SMS_SEND_SHARED` en la consulta.
{% endalert %}
{% endapi %}

{% api %}
## Encontrar el número promedio de correos electrónicos que un usuario recibe semanalmente {#find-the-average-number-of-emails-a-user-receives-weekly}
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
Para mensajes servicio de mensajes cortos, reemplaza `USERS_MESSAGES_EMAIL_SEND_SHARED` con `USERS_MESSAGES_SMS_SEND_SHARED` en la consulta. Para notificaciones push, reemplaza `USERS_MESSAGES_EMAIL_SEND_SHARED` con `USERS_MESSAGES_SMS_SEND_SHARED` en la consulta.
{% endalert %}
{% endapi %}