---
nav_title: "사용 사례"
article_title: SQL 세그먼트 확장 사용 사례
page_order: 2
page_type: glossary
layout: sql_segment_extensions_glossary
alias: "/sql_segments_use_cases/"
description: "이 문서에서는 SQL 세그먼트 확장을 위한 테스트 및 검증된 쿼리를 다룹니다."
tool: Segments
---

{% api %}
## 이벤트 발생 횟수별 사용자 선택 {#select-users-by-how-many-times-an-event-has-occurred}
{% apitags %}
Event
{% endapitags %}

과거에 특정 이메일 Campaign을 두 번 이상 열어본 사용자를 선택합니다.

이 방법은 노출 횟수 기준 인앱 메시지 빈도 제한에도 사용할 수 있습니다. 예를 들어, 동일한 Campaign에서 노출 횟수가 3회를 초과하는 사용자를 Segment 제외 대상으로 선택할 수 있습니다.

```sql
SELECT user_id FROM "USERS_MESSAGES_EMAIL_OPEN_SHARED"
WHERE campaign_api_id='8f7026dc-e9b7-40e6-bdc7-96cf58e80faa'
GROUP BY user_id
HAVING count(*) > 1
```
{% endapi %}

{% api %}
## 동작을 수행하고 등록정보 값을 합산한 사용자 선택 {#select-users-that-performed-an-action-and-sum-up-a-property-value}
{% apitags %}
Property
{% endapitags %}

스포츠 베팅을 한 사용자 중 모든 베팅 합계가 특정 금액을 초과하는 사용자를 선택합니다.

```sql
select user_id from "USERS_BEHAVIORS_CUSTOMEVENT_SHARED"
where name='Bet On Sports'
group by 1 having sum(get_path(parse_json(properties), 'amount')) > 150
```
{% endapi %}

{% api %}
## 특정 기간 내 이벤트 발생 횟수 기준 사용자 선택 {#select-users-based-on-how-many-times-an-event-occurred-in-a-time-range}
{% apitags %}
Event, Time range
{% endapitags %}

최근 30일 동안 이메일을 3회 이상 열어본 사용자를 선택합니다.

이 방법은 다양한 채널에서 반응이 높은 사용자 등 사용자의 참여 수준을 파악하는 데에도 활용할 수 있습니다.

```sql
SELECT user_id, COUNT(DISTINCT id) AS num_emails_opened
FROM USERS_MESSAGES_EMAIL_OPEN_SHARED
WHERE to_timestamp_ntz(time) >= DATEADD(day, -30, CURRENT_TIMESTAMP()) AND to_timestamp_ntz(time) <= CURRENT_TIMESTAMP()
GROUP BY user_id;
HAVING COUNT(DISTINCT id) > 3
```
{% endapi %}

{% api %}
## 여러 기간에 걸쳐 하나 이상의 이벤트를 기록한 사용자 선택 {#select-users-that-recorded-at-least-one-event-across-multiple-time-ranges}
{% apitags %}
Event, Time range
{% endapitags %}

최근 4분기 각각에서 구매를 한 사용자를 선택합니다. 이 사용자 Segment는 [오디언스 동기화]({{site.baseurl}}/partners/canvas_audience_sync)와 함께 사용하여 고가치 유사 고객을 식별하고 신규 고객을 확보하는 데 활용할 수 있습니다.

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
## 특정 등록정보가 포함된 구매 선택 {#select-any-purchase-with-certain-properties}
{% apitags %}
Purchase, Property
{% endapitags %}

14일 이내에 `"type = shops"` 등록정보가 포함된 구매를 한 고객을 선택합니다.

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
## 메시지가 발송되었지만 전달되지 않은 사용자 선택 {#select-users-that-were-sent-a-message-that-wasnt-delivered}
{% apitags %}
Message, Delivery
{% endapitags %}

SMS Campaign 또는 Canvas가 발송되었지만 메시지가 통신사에 도달하지 못한 사용자를 선택합니다. 예를 들어, 대기줄 오버플로로 인해 메시지가 중단되었을 수 있습니다.

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
## 대기줄 오버플로로 인해 통신사에 도달하지 못한 모든 SMS 메시지 찾기 {#find-all-sms-messages-that-were-sent-but-didnt-reach-the-carrier-because-of-queue-overflow}
{% apitags %}
Message, Carrier
{% endapitags %}

이 쿼리는 특정 Canvas에서 발송되었지만 전달되지 않은 다른 유형의 메시지에도 활용할 수 있습니다.

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
`CANVAS_ID`는 Canvas URL에서 `/canvas/` 뒤에 오는 번호입니다.
{% endapi %}

{% api %}
## 특정 값을 포함하는 등록정보 배열이 있는 구매를 한 사용자 선택 {#select-users-that-made-any-purchase-with-a-property-array-containing-a-specific-value}
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
## 30003 오류가 여러 번 발생하고 전달이 0건인 사용자 찾기 {#find-all-users-that-had-multiple-30003-errors-and-0-deliveries}
{% apitags %}
Error, Delivery
{% endapitags %}

메시지 수신에 실패하고 있지만 필요한 오류 코드가 없어 유효하지 않은 것으로 표시되지 않는 사용자에게 발송을 중단하려는 상황을 해결하는 데 유용합니다. 이러한 사용자를 리타겟하여 전화번호를 업데이트하거나 탈퇴 처리할 수 있습니다.

이 쿼리는 증분 편집기를 사용하며, 최근 90일 동안 거부된 발송이 3건 이상이고 전달이 0건인 사용자를 조회합니다.

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
## 특정 기간 내 특정 이벤트 등록정보 및 이벤트 횟수 조건을 충족하는 사용자 찾기 {#find-users-with-specific-event-properties-and-event-counts-in-a-time-range}
{% apitags %}
Event, Property, Time range
{% endapitags %}

다음 조건을 동시에 충족하는 사용자를 찾습니다:

- 총 거래 금액이 $500 초과 (여러 `Transact` 이벤트의 합계)
- `Funan` 쇼핑몰에서 거래
- 최근 90일 동안 3회 이상 거래

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
## 가장 최근 세션이 특정 기기 모델에서 발생한 사용자 선택 {#select-users-whose-most-recent-session-was-on-a-specific-device-model}
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
## 특정 기간 내 인앱 메시지의 두 번째 버튼을 선택한 사용자 찾기 {#find-users-that-selected-the-second-button-of-an-in-app-message-in-a-specific-time-range}
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
## 최근 3개월 연속으로 구매한 사용자 찾기 {#find-users-that-purchased-in-each-of-the-last-three-calendar-months}
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
## 등록정보가 정수인 경우 특정 등록정보로 커스텀 이벤트를 완료한 사용자 선택 {#select-users-that-completed-a-custom-event-with-a-specific-property-when-property-is-an-integer}
{% apitags %}
Event, Property
{% endapitags %}

최근 6개월 동안 시리즈를 시청했으며 플랫폼을 떠나려는 사용자에게 메시지를 발송합니다.

등록정보는 타이틀 ID이며, 그렇지 않으면 필터에 100개 이상의 타이틀 ID를 포함해야 합니다. 증분 세그먼트 확장은 비용 최적화가 가능하며 헤더에서 날짜 범위를 지정할 수 있습니다.

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
## 사용자가 일일 평균 수신하는 이메일 수 찾기 {#find-the-average-number-of-emails-a-user-receives-daily}
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
SMS 메시지의 경우, 쿼리에서 `USERS_MESSAGES_EMAIL_SEND_SHARED`를 `USERS_MESSAGES_SMS_SEND_SHARED`로 바꾸세요. 푸시 알림의 경우, 쿼리에서 `USERS_MESSAGES_EMAIL_SEND_SHARED`를 `USERS_MESSAGES_SMS_SEND_SHARED`로 바꾸세요.
{% endalert %}
{% endapi %}

{% api %}
## 사용자가 주간 평균 수신하는 이메일 수 찾기 {#find-the-average-number-of-emails-a-user-receives-weekly}
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
SMS 메시지의 경우, 쿼리에서 `USERS_MESSAGES_EMAIL_SEND_SHARED`를 `USERS_MESSAGES_SMS_SEND_SHARED`로 바꾸세요. 푸시 알림의 경우, 쿼리에서 `USERS_MESSAGES_EMAIL_SEND_SHARED`를 `USERS_MESSAGES_SMS_SEND_SHARED`로 바꾸세요.
{% endalert %}
{% endapi %}