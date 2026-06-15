---
nav_title: "Cas d'utilisation"
article_title: Cas d'utilisation des extensions de segments SQL
page_order: 2
page_type: glossary
layout: sql_segment_extensions_glossary
alias: "/sql_segments_use_cases/"
description: "Cet article contient des requêtes testées et éprouvées pour les extensions de segments SQL."
tool: Segments
---

{% api %}
## Sélectionner des utilisateurs en fonction du nombre d'occurrences d'un événement {#select-users-by-how-many-times-an-event-has-occurred}
{% apitags %}
Event
{% endapitags %}

Sélectionnez les utilisateurs qui ont ouvert une certaine campagne par e-mail plus d'une fois par le passé.

Cela fonctionne également pour le plafonnement des messages in-app par nombre d'impressions, par exemple en sélectionnant les utilisateurs ayant plus de trois impressions comme exclusion de segment sur la même campagne.

```sql
SELECT user_id FROM "USERS_MESSAGES_EMAIL_OPEN_SHARED"
WHERE campaign_api_id='8f7026dc-e9b7-40e6-bdc7-96cf58e80faa'
GROUP BY user_id
HAVING count(*) > 1
```
{% endapi %}

{% api %}
## Sélectionner des utilisateurs ayant effectué une action et additionner la valeur d'une propriété {#select-users-that-performed-an-action-and-sum-up-a-property-value}
{% apitags %}
Property
{% endapitags %}

Sélectionnez les utilisateurs qui ont parié sur des sports et dont la somme de tous les paris est supérieure à un certain montant.

```sql
select user_id from "USERS_BEHAVIORS_CUSTOMEVENT_SHARED"
where name='Bet On Sports'
group by 1 having sum(get_path(parse_json(properties), 'amount')) > 150
```
{% endapi %}

{% api %}
## Sélectionner des utilisateurs en fonction du nombre d'occurrences d'un événement dans une plage de temps {#select-users-based-on-how-many-times-an-event-occurred-in-a-time-range}
{% apitags %}
Event, Time range
{% endapitags %}

Sélectionnez les utilisateurs ayant plus de trois ouvertures d'e-mail au cours des 30 derniers jours.

Cela fonctionne également pour déterminer les niveaux d'engagement des utilisateurs, comme les utilisateurs très réactifs sur différents canaux.

```sql
SELECT user_id, COUNT(DISTINCT id) AS num_emails_opened
FROM USERS_MESSAGES_EMAIL_OPEN_SHARED
WHERE to_timestamp_ntz(time) >= DATEADD(day, -30, CURRENT_TIMESTAMP()) AND to_timestamp_ntz(time) <= CURRENT_TIMESTAMP()
GROUP BY user_id;
HAVING COUNT(DISTINCT id) > 3
```
{% endapi %}

{% api %}
## Sélectionner des utilisateurs ayant enregistré au moins un événement sur plusieurs plages de temps {#select-users-that-recorded-at-least-one-event-across-multiple-time-ranges}
{% apitags %}
Event, Time range
{% endapitags %}

Sélectionnez les utilisateurs ayant effectué un achat au cours de chacun des quatre derniers trimestres. Ce segment d'utilisateurs peut être utilisé avec la [synchronisation d'audience]({{site.baseurl}}/partners/canvas_audience_sync/) pour identifier des clients similaires à forte valeur à des fins d'acquisition.

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
## Sélectionner tout achat avec certaines propriétés {#select-any-purchase-with-certain-properties}
{% apitags %}
Purchase, Property
{% endapitags %}

Sélectionnez les clients ayant effectué un achat contenant la propriété `"type = shops"` au cours des 14 derniers jours.

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
## Sélectionner des utilisateurs auxquels un message a été envoyé mais non distribué {#select-users-that-were-sent-a-message-that-wasnt-delivered}
{% apitags %}
Message, Delivery
{% endapitags %}

Sélectionnez les utilisateurs auxquels une campagne SMS ou un Canvas a été envoyé, mais dont le message n'a pas atteint l'opérateur. Par exemple, le message peut avoir été bloqué par un débordement de file d'attente.

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
## Trouver tous les messages SMS envoyés mais n'ayant pas atteint l'opérateur en raison d'un débordement de file d'attente {#find-all-sms-messages-that-were-sent-but-didnt-reach-the-carrier-because-of-queue-overflow}
{% apitags %}
Message, Carrier
{% endapitags %}

Cela peut être réutilisé pour d'autres types de messages envoyés depuis un Canvas particulier qui n'ont pas été distribués.

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
`CANVAS_ID` est le numéro qui suit `/canvas/` dans l'URL de votre Canvas.
{% endapi %}

{% api %}
## Sélectionner des utilisateurs ayant effectué un achat avec un tableau de propriétés contenant une valeur spécifique {#select-users-that-made-any-purchase-with-a-property-array-containing-a-specific-value}
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
## Trouver tous les utilisateurs ayant eu plusieurs erreurs 30003 et 0 distribution {#find-all-users-that-had-multiple-30003-errors-and-0-deliveries}
{% apitags %}
Error, Delivery
{% endapitags %}

Cela est utile pour résoudre les situations où vous souhaitez arrêter d'envoyer des messages à des utilisateurs qui ne les reçoivent pas, mais qui ne sont pas marqués comme invalides car ils n'ont pas le code d'erreur requis. Vous pouvez soit recibler ces utilisateurs pour mettre à jour leur numéro de téléphone, soit les désabonner.

Cette requête utilise l'éditeur incrémentiel et recherche les utilisateurs ayant trois envois rejetés ou plus au cours des 90 derniers jours et zéro distribution.

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
## Trouver des utilisateurs avec des propriétés d'événement et des comptages d'événements spécifiques dans une plage de temps {#find-users-with-specific-event-properties-and-event-counts-in-a-time-range}
{% apitags %}
Event, Property, Time range
{% endapitags %}

Trouvez les utilisateurs qui remplissent simultanément les conditions suivantes :

- Ont effectué des transactions d'une valeur totale supérieure à 500 $ (la somme de plusieurs événements `Transact`)
- Ont effectué des transactions au centre commercial `Funan`
- Ont effectué plus de trois transactions au cours des 90 derniers jours

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
## Sélectionner des utilisateurs dont la session la plus récente était sur un modèle d'appareil spécifique {#select-users-whose-most-recent-session-was-on-a-specific-device-model}
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
## Trouver des utilisateurs ayant sélectionné le deuxième bouton d'un message in-app dans une plage de temps spécifique {#find-users-that-selected-the-second-button-of-an-in-app-message-in-a-specific-time-range}
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
## Trouver des utilisateurs ayant effectué un achat au cours de chacun des trois derniers mois calendaires {#find-users-that-purchased-in-each-of-the-last-three-calendar-months}
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
## Sélectionner des utilisateurs ayant effectué un événement personnalisé avec une propriété spécifique lorsque la propriété est un entier {#select-users-that-completed-a-custom-event-with-a-specific-property-when-property-is-an-integer}
{% apitags %}
Event, Property
{% endapitags %}

Envoyez un message aux utilisateurs qui ont regardé une série au cours des six derniers mois et qui sont sur le point de quitter la plateforme.

La propriété est l'ID du titre ; autrement, vous devriez inclure plus de 100 ID de titre dans un filtre. L'extension de segment incrémentielle peut être optimisée en termes de coût et vous pouvez spécifier la plage de dates dans l'en-tête.

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
## Trouver le nombre moyen d'e-mails qu'un utilisateur reçoit quotidiennement {#find-the-average-number-of-emails-a-user-receives-daily}
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
Pour les messages SMS, remplacez `USERS_MESSAGES_EMAIL_SEND_SHARED` par `USERS_MESSAGES_SMS_SEND_SHARED` dans la requête. Pour les notifications push, remplacez `USERS_MESSAGES_EMAIL_SEND_SHARED` par `USERS_MESSAGES_SMS_SEND_SHARED` dans la requête.
{% endalert %}
{% endapi %}

{% api %}
## Trouver le nombre moyen d'e-mails qu'un utilisateur reçoit par semaine {#find-the-average-number-of-emails-a-user-receives-weekly}
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
Pour les messages SMS, remplacez `USERS_MESSAGES_EMAIL_SEND_SHARED` par `USERS_MESSAGES_SMS_SEND_SHARED` dans la requête. Pour les notifications push, remplacez `USERS_MESSAGES_EMAIL_SEND_SHARED` par `USERS_MESSAGES_SMS_SEND_SHARED` dans la requête.
{% endalert %}
{% endapi %}