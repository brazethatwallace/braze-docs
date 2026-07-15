---
nav_title: "ユースケース"
article_title: SQL セグメントエクステンションのユースケース
page_order: 2
page_type: glossary
layout: sql_segment_extensions_glossary
alias: "/sql_segments_use_cases/"
description: "この記事では、SQL セグメントエクステンション向けにテスト済みで実証されたクエリを紹介します。"
tool: Segments
---

{% api %}
## イベントの発生回数でユーザーを選択する {#select-users-by-how-many-times-an-event-has-occurred}
{% apitags %}
Event
{% endapitags %}

過去に特定のメールキャンペーンを複数回開封したユーザーを選択します。

これは、インプレッション数によるアプリ内メッセージのキャップにも使用できます。たとえば、3回以上のインプレッションがあるユーザーを選択し、同じキャンペーンのセグメント除外として設定できます。

```sql
SELECT user_id FROM "USERS_MESSAGES_EMAIL_OPEN_SHARED"
WHERE campaign_api_id='8f7026dc-e9b7-40e6-bdc7-96cf58e80faa'
GROUP BY user_id
HAVING count(*) > 1
```
{% endapi %}

{% api %}
## アクションを実行したユーザーを選択し、プロパティ値を合計する {#select-users-that-performed-an-action-and-sum-up-a-property-value}
{% apitags %}
Property
{% endapitags %}

スポーツに賭けを行い、すべての賭け金の合計が特定の金額を超えるユーザーを選択します。

```sql
select user_id from "USERS_BEHAVIORS_CUSTOMEVENT_SHARED"
where name='Bet On Sports'
group by 1 having sum(get_path(parse_json(properties), 'amount')) > 150
```
{% endapi %}

{% api %}
## 時間範囲内のイベント発生回数に基づいてユーザーを選択する {#select-users-based-on-how-many-times-an-event-occurred-in-a-time-range}
{% apitags %}
Event, Time range
{% endapitags %}

過去30日間にメール開封が3回を超えるユーザーを選択します。

これは、さまざまなチャネルにおける反応性の高いユーザーなど、ユーザーのエンゲージメントレベルを判定する場合にも使用できます。

```sql
SELECT user_id, COUNT(DISTINCT id) AS num_emails_opened
FROM USERS_MESSAGES_EMAIL_OPEN_SHARED
WHERE to_timestamp_ntz(time) >= DATEADD(day, -30, CURRENT_TIMESTAMP()) AND to_timestamp_ntz(time) <= CURRENT_TIMESTAMP()
GROUP BY user_id;
HAVING COUNT(DISTINCT id) > 3
```
{% endapi %}

{% api %}
## 複数の時間範囲にわたって少なくとも1回のイベントを記録したユーザーを選択する {#select-users-that-recorded-at-least-one-event-across-multiple-time-ranges}
{% apitags %}
Event, Time range
{% endapitags %}

過去4四半期のそれぞれで購入を行ったユーザーを選択します。このユーザーセグメントは、[オーディエンス同期]({{site.baseurl}}/partners/canvas_audience_sync)と組み合わせて、獲得向けの高価値な類似顧客を特定するために使用できます。

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
## 特定のプロパティを持つ購入を選択する {#select-any-purchase-with-certain-properties}
{% apitags %}
Purchase, Property
{% endapitags %}

14日以内にプロパティ `"type = shops"` を含む購入を行った顧客を選択します。

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
## メッセージが送信されたが配信されなかったユーザーを選択する {#select-users-that-were-sent-a-message-that-wasnt-delivered}
{% apitags %}
Message, Delivery
{% endapitags %}

SMSのキャンペーンまたはキャンバスが送信されたが、メッセージがキャリアに到達しなかったユーザーを選択します。たとえば、キューオーバーフローによってメッセージが停止された場合などです。

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
## キューオーバーフローによりキャリアに到達しなかったすべてのSMSメッセージを検索する {#find-all-sms-messages-that-were-sent-but-didnt-reach-the-carrier-because-of-queue-overflow}
{% apitags %}
Message, Carrier
{% endapitags %}

これは、特定のキャンバスから送信されたが配信されなかった他の種類のメッセージにも転用できます。

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
`CANVAS_ID` は、キャンバスのURLの `/canvas/` の後にある番号です。
{% endapi %}

{% api %}
## 特定の値を含むプロパティ配列を持つ購入を行ったユーザーを選択する {#select-users-that-made-any-purchase-with-a-property-array-containing-a-specific-value}
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
## 30003エラーが複数回発生し、配信が0件のユーザーを検索する {#find-all-users-that-had-multiple-30003-errors-and-0-deliveries}
{% apitags %}
Error, Delivery
{% endapitags %}

これは、メッセージの受信に失敗しているが、必要なエラーコードがないために無効としてマークされていないユーザーへの送信を停止したい場合に役立ちます。これらのユーザーをリターゲティングして電話番号を更新させるか、配信停止にすることができます。

このクエリはインクリメンタルエディターを使用し、過去90日間に3回以上の拒否送信があり、配信が0件のユーザーを検索します。

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
## 特定のイベントプロパティとイベント回数を持つユーザーを時間範囲内で検索する {#find-users-with-specific-event-properties-and-event-counts-in-a-time-range}
{% apitags %}
Event, Property, Time range
{% endapitags %}

以下の条件を同時に満たすユーザーを検索します。

- 合計取引額が500ドルを超える（複数の `Transact` イベントの合計）
- モール `Funan` で取引した
- 過去90日間に3回以上取引した

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
## 最新のセッションが特定のデバイスモデルであるユーザーを選択する {#select-users-whose-most-recent-session-was-on-a-specific-device-model}
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
## 特定の時間範囲内でアプリ内メッセージの2番目のボタンを選択したユーザーを検索する {#find-users-that-selected-the-second-button-of-an-in-app-message-in-a-specific-time-range}
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
## 過去3暦月のそれぞれで購入を行ったユーザーを検索する {#find-users-that-purchased-in-each-of-the-last-three-calendar-months}
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
## プロパティが整数の場合に特定のプロパティを持つカスタムイベントを完了したユーザーを選択する {#select-users-that-completed-a-custom-event-with-a-specific-property-when-property-is-an-integer}
{% apitags %}
Event, Property
{% endapitags %}

過去6か月間にシリーズを視聴し、プラットフォームを離れようとしているユーザーにメッセージを送信します。

プロパティはタイトルIDです。そうでなければ、フィルターに100以上のタイトルIDを含める必要があります。インクリメンタルセグメントエクステンションはコスト最適化が可能で、ヘッダーで日付範囲を指定できます。

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
## ユーザーが1日に受信するメールの平均数を求める {#find-the-average-number-of-emails-a-user-receives-daily}
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
SMSメッセージの場合は、クエリ内の `USERS_MESSAGES_EMAIL_SEND_SHARED` を `USERS_MESSAGES_SMS_SEND_SHARED` に置き換えてください。プッシュ通知の場合は、クエリ内の `USERS_MESSAGES_EMAIL_SEND_SHARED` を `USERS_MESSAGES_SMS_SEND_SHARED` に置き換えてください。
{% endalert %}
{% endapi %}

{% api %}
## ユーザーが1週間に受信するメールの平均数を求める {#find-the-average-number-of-emails-a-user-receives-weekly}
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
SMSメッセージの場合は、クエリ内の `USERS_MESSAGES_EMAIL_SEND_SHARED` を `USERS_MESSAGES_SMS_SEND_SHARED` に置き換えてください。プッシュ通知の場合は、クエリ内の `USERS_MESSAGES_EMAIL_SEND_SHARED` を `USERS_MESSAGES_SMS_SEND_SHARED` に置き換えてください。
{% endalert %}
{% endapi %}