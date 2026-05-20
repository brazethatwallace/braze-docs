---
nav_title: "サンプルクエリ"
article_title: Snowflake サンプルクエリ
page_order: 1
description: "このパートナーページでは、Snowflakeクエリを設定する際に参照できるユースケースのサンプルクエリをいくつか紹介しています。"
page_type: partner
search_tag: Partner

---

# サンプルクエリ {#sample-queries}

> このパートナーページでは、クエリを設定する際に参照できるユースケースのサンプルクエリを紹介します。

{% tabs %}
{% tab Filter By Time%}

一般的なクエリとして、時間によるイベントのフィルタリングがあります。

発生時刻でイベントをフィルタリングできます。イベントテーブルは `time` でクラスタリングされているため、`time` によるフィルタリングが最適です。
```sql
-- find custom events that occurred after 04/15/2019 @ 7:02pm (UTC) i.e., timestamp=1555354920
SELECT *
FROM users_behaviors_customevent_shared
WHERE time > 1555354920
LIMIT 10;
```
また、`sf_created_at` を使用して、Snowflakeデータウェアハウスにイベントが永続化された時刻でフィルタリングすることもできます。`sf_created_at` と `time` は同一ではありませんが通常は近い値になるため、このクエリも同様のパフォーマンス特性を持ちます。
`````````sql
-- find custom events that arrived in Snowflake after time 04/15/2019 @ 7:02pm (UTC)
SELECT *
FROM users_behaviors_customevent_shared
WHERE sf_created_at > to_timestamp_ntz('2019-04-15 19:02:00')
LIMIT 10;
```
{% alert note %}
`sf_created_at` の値は、`Nov 15th, 2019 9:31 pm UTC` 以降に永続化されたイベントに対してのみ信頼できます。
{% endalert %}
{% endtab %}

{% tab Querying Changelogs%}

キャンペーン名とキャンバス名はイベント自体には含まれていません。代わりに、変更ログテーブルに公開されます。

次のようなクエリでキャンペーンの変更ログテーブルと結合することで、キャンペーンに関連するイベントのキャンペーン名を確認できます。

`````````sql
SELECT event.id, event.time, ccs.time, ccs.name, ccs.conversion_behaviors[event.conversion_behavior_index]
FROM USERS_CAMPAIGNS_CONVERSION_SHARED event
LEFT JOIN CHANGELOGS_CAMPAIGN_SHARED ccs
ON ccs.id = event.campaign_id
AND ccs.time < event.time
qualify row_number() over (partition by event.id ORDER BY ccs.time DESC) = 1;
```
いくつかの重要な注意点があります。
- ここではSnowflakeの[window](https://docs.snowflake.com/en/sql-reference/functions-analytic.html)関数を使用しています。
- 左結合により、キャンペーンに関連しないイベントも含まれます。
- `campaign_id` があるにもかかわらずCampaign名が表示されないイベントがある場合、そのCampaignはデータ共有が製品として存在する前に作成された可能性があります。
- `CHANGELOGS_CANVAS_SHARED` テーブルと結合する同様のクエリを使用して、キャンバス名を確認することもできます。

キャンペーンとキャンバスの両方の名前を表示したい場合は、次のサブクエリを使用する必要があります。
`````````sql
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

このプッシュファネルクエリを使用して、プッシュ送信の生イベントデータから配信の生イベントデータ、さらに開封の生イベントデータまでを集約できます。このクエリは、各生イベントが通常個別のテーブルを持つため、すべてのテーブルを結合する方法を示しています。

`````````sql

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
この日次メールメッセージングケイデンスクエリを使用して、ユーザーがメールを受信する間隔を分析できます。

たとえば、ユーザーが1日に2通のメールを受信した場合、`0 "days since last received"` に該当します。月曜日に1通、火曜日に1通受信した場合は、`1 "days since last received"` コホートに分類されます。

`````````sql
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

このユニークメールクリック数クエリを使用して、指定された時間枠内のユニークなメールクリックを分析できます。これを計算するアルゴリズムは次のとおりです。
  1. キー（`app_group_id`、`message_variation_id`、`dispatch_id`、`email_address`）でイベントをパーティション分割します。
  2. 各パーティション内でイベントを時間順に並べ、最初のイベントは常にユニークイベントとなります。
  3. 後続のすべてのイベントについて、前のイベントから7日以上経過して発生した場合、ユニークイベントと見なされます。

Snowflakeの[ウィンドウ関数](https://docs.snowflake.com/en/sql-reference/functions-analytic.html)を使用してこれを実現できます。次のクエリは、過去365日間のすべてのメールクリックを返し、`is_unique` 列でどのイベントがユニークであるかを示します。

`````````sql
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

ユニークイベントのみを表示したい場合は、`QUALIFY` 句を使用します。
`````````sql
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
メールアドレスごとにグループ化されたユニークイベント数をさらに確認するには、次のようにします。
`````````sql
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

このクエリを使用して、Snowflakeのメール開封イベントから**ユニーク開封数**を近似できます。たとえば、ダッシュボードの**Unique Opens**列との照合に利用できます。

この例では3つのカウントを返します。

- **Unique Opens (over 7 days)：** 7日間のローリング期間におけるユニーク開封数です。
- **Unique Opens (during date window)：** 指定された期間内のユニーク開封数です。期間前に発生した開封は考慮されません。
- **Unique Opens (for emails delivered within same timeframe)：** 対応する配信イベントも同じ期間内に発生したユニーク開封数です（その期間内に配信されたメッセージに紐づく開封のみを確認したい場合に便利です）。

{% raw %}
`````````sql
/*
    Set or comment out variables if not required. These are set per session.
    You can obtain the from and to dates from the Campaign/キャンバス/キャンバス step URL. These are the startDate and endDate parameters.

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