---
nav_title: "Anwendungsfälle"
article_title: Anwendungsfälle für SQL-Segmenterweiterungen
page_order: 2
page_type: glossary
layout: sql_segment_extensions_glossary
alias: "/sql_segments_use_cases/"
description: "Dieser Artikel enthält getestete und bewährte Abfragen für SQL-Segmenterweiterungen."
tool: Segments
---

{% api %}
## Nutzer:innen nach Häufigkeit eines Events auswählen {#select-users-by-how-many-times-an-event-has-occurred}
{% apitags %}
Event
{% endapitags %}

Wählen Sie Nutzer:innen aus, die eine bestimmte E-Mail-Campaign in der Vergangenheit mehr als einmal geöffnet haben.

Dies funktioniert auch für das Capping von In-App-Nachrichten nach Anzahl der Impressionen, z. B. um Nutzer:innen mit mehr als drei Impressionen als Segmentausschluss für dieselbe Campaign auszuwählen.

```sql
SELECT user_id FROM "USERS_MESSAGES_EMAIL_OPEN_SHARED"
WHERE campaign_api_id='8f7026dc-e9b7-40e6-bdc7-96cf58e80faa'
GROUP BY user_id
HAVING count(*) > 1
```
{% endapi %}

{% api %}
## Nutzer:innen auswählen, die eine Aktion ausgeführt haben, und einen Eigenschaftswert summieren {#select-users-that-performed-an-action-and-sum-up-a-property-value}
{% apitags %}
Property
{% endapitags %}

Wählen Sie Nutzer:innen aus, die eine Sportwette platziert haben, wobei die Summe aller Wetten einen bestimmten Betrag übersteigt.

```sql
select user_id from "USERS_BEHAVIORS_CUSTOMEVENT_SHARED"
where name='Bet On Sports'
group by 1 having sum(get_path(parse_json(properties), 'amount')) > 150
```
{% endapi %}

{% api %}
## Nutzer:innen basierend auf der Häufigkeit eines Events in einem Zeitraum auswählen {#select-users-based-on-how-many-times-an-event-occurred-in-a-time-range}
{% apitags %}
Event, Time range
{% endapitags %}

Wählen Sie Nutzer:innen mit mehr als drei E-Mail-Öffnungen in den letzten 30 Tagen aus.

Dies funktioniert auch zur Bestimmung des Engagement-Levels von Nutzer:innen, z. B. um besonders aktive Nutzer:innen über verschiedene Kanäle hinweg zu identifizieren.

```sql
SELECT user_id, COUNT(DISTINCT id) AS num_emails_opened
FROM USERS_MESSAGES_EMAIL_OPEN_SHARED
WHERE to_timestamp_ntz(time) >= DATEADD(day, -30, CURRENT_TIMESTAMP()) AND to_timestamp_ntz(time) <= CURRENT_TIMESTAMP()
GROUP BY user_id;
HAVING COUNT(DISTINCT id) > 3
```
{% endapi %}

{% api %}
## Nutzer:innen auswählen, die mindestens ein Event in mehreren Zeiträumen aufgezeichnet haben {#select-users-that-recorded-at-least-one-event-across-multiple-time-ranges}
{% apitags %}
Event, Time range
{% endapitags %}

Wählen Sie Nutzer:innen aus, die in jedem der letzten vier Quartale einen Kauf getätigt haben. Dieses Nutzersegment kann mit [Audience Sync]({{site.baseurl}}/partners/canvas_audience_sync) verwendet werden, um hochwertige Lookalike-Kund:innen für die Akquise zu identifizieren.

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
## Jeden Kauf mit bestimmten Eigenschaften auswählen {#select-any-purchase-with-certain-properties}
{% apitags %}
Purchase, Property
{% endapitags %}

Wählen Sie Kund:innen aus, die innerhalb von 14 Tagen einen Kauf mit der Eigenschaft `"type = shops"` getätigt haben.

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
## Nutzer:innen auswählen, denen eine Nachricht gesendet, aber nicht zugestellt wurde {#select-users-that-were-sent-a-message-that-wasnt-delivered}
{% apitags %}
Message, Delivery
{% endapitags %}

Wählen Sie Nutzer:innen aus, denen eine SMS-Campaign oder ein Canvas gesendet wurde, die Nachricht aber nicht beim Carrier angekommen ist. Beispielsweise könnte die Nachricht durch einen Warteschlangenüberlauf gestoppt worden sein.

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
## Alle SMS-Nachrichten finden, die gesendet, aber wegen Warteschlangenüberlauf nicht an den Carrier übermittelt wurden {#find-all-sms-messages-that-were-sent-but-didnt-reach-the-carrier-because-of-queue-overflow}
{% apitags %}
Message, Carrier
{% endapitags %}

Dies kann auch für andere Nachrichtentypen verwendet werden, die aus einem bestimmten Canvas gesendet, aber nicht zugestellt wurden.

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
`CANVAS_ID` ist die Nummer nach `/canvas/` in Ihrer Canvas-URL.
{% endapi %}

{% api %}
## Nutzer:innen auswählen, die einen Kauf mit einem Eigenschafts-Array getätigt haben, das einen bestimmten Wert enthält {#select-users-that-made-any-purchase-with-a-property-array-containing-a-specific-value}
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
## Alle Nutzer:innen finden, die mehrere 30003-Fehler und 0 Zustellungen hatten {#find-all-users-that-had-multiple-30003-errors-and-0-deliveries}
{% apitags %}
Error, Delivery
{% endapitags %}

Dies ist hilfreich, um Situationen zu lösen, in denen Sie den Versand an Nutzer:innen stoppen möchten, die keine Nachrichten empfangen, aber nicht als ungültig markiert werden, weil sie nicht den erforderlichen Fehlercode haben. Sie können diese Nutzer:innen entweder erneut ansprechen, um ihre Telefonnummer zu aktualisieren, oder sie abmelden.

Diese Abfrage verwendet den inkrementellen Editor und sucht nach Nutzer:innen mit drei oder mehr abgelehnten Sendungen in den letzten 90 Tagen und null Zustellungen.

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
## Nutzer:innen mit bestimmten Event-Eigenschaften und Event-Anzahlen in einem Zeitraum finden {#find-users-with-specific-event-properties-and-event-counts-in-a-time-range}
{% apitags %}
Event, Property, Time range
{% endapitags %}

Finden Sie Nutzer:innen, die gleichzeitig die folgenden Bedingungen erfüllen:

- Haben einen Gesamtwert von mehr als 500 $ transagiert (die Summe mehrerer `Transact`-Events)
- Haben im Einkaufszentrum `Funan` transagiert
- Haben in den letzten 90 Tagen mehr als dreimal transagiert

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
## Nutzer:innen auswählen, deren letzte Sitzung auf einem bestimmten Gerätemodell stattfand {#select-users-whose-most-recent-session-was-on-a-specific-device-model}
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
## Nutzer:innen finden, die den zweiten Button einer In-App-Nachricht in einem bestimmten Zeitraum ausgewählt haben {#find-users-that-selected-the-second-button-of-an-in-app-message-in-a-specific-time-range}
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
## Nutzer:innen finden, die in jedem der letzten drei Kalendermonate einen Kauf getätigt haben {#find-users-that-purchased-in-each-of-the-last-three-calendar-months}
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
## Nutzer:innen auswählen, die ein angepasstes Event mit einer bestimmten Eigenschaft abgeschlossen haben, wenn die Eigenschaft ein Integer ist {#select-users-that-completed-a-custom-event-with-a-specific-property-when-property-is-an-integer}
{% apitags %}
Event, Property
{% endapitags %}

Senden Sie eine Nachricht an Nutzer:innen, die in den letzten sechs Monaten eine Serie angesehen haben und kurz davor stehen, die Plattform zu verlassen.

Die Eigenschaft ist die Titel-ID; andernfalls müssten Sie über 100 Titel-IDs in einem Filter angeben. Die inkrementelle Segmenterweiterung kann kostenoptimiert werden, und Sie können den Datumsbereich im Header festlegen.

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
## Die durchschnittliche Anzahl der E-Mails ermitteln, die Nutzer:innen täglich erhalten {#find-the-average-number-of-emails-a-user-receives-daily}
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
Ersetzen Sie für SMS-Nachrichten `USERS_MESSAGES_EMAIL_SEND_SHARED` durch `USERS_MESSAGES_SMS_SEND_SHARED` in der Abfrage. Ersetzen Sie für Push-Benachrichtigungen `USERS_MESSAGES_EMAIL_SEND_SHARED` durch `USERS_MESSAGES_SMS_SEND_SHARED` in der Abfrage.
{% endalert %}
{% endapi %}

{% api %}
## Die durchschnittliche Anzahl der E-Mails ermitteln, die Nutzer:innen wöchentlich erhalten {#find-the-average-number-of-emails-a-user-receives-weekly}
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
Ersetzen Sie für SMS-Nachrichten `USERS_MESSAGES_EMAIL_SEND_SHARED` durch `USERS_MESSAGES_SMS_SEND_SHARED` in der Abfrage. Ersetzen Sie für Push-Benachrichtigungen `USERS_MESSAGES_EMAIL_SEND_SHARED` durch `USERS_MESSAGES_SMS_SEND_SHARED` in der Abfrage.
{% endalert %}
{% endapi %}