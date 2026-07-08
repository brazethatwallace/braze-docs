---
nav_title: サブスクリプショングループ
article_title: サブスクリプショングループエンドポイント
page_order: 7
layout: dev_guide

#Required
description: "このランディングページでは、メールとSMSのBrazeサブスクリプショングループエンドポイントについて説明し、一覧表示します。"
page_type: landing
search_tag: Endpoint

guide_top_header: "サブスクリプショングループエンドポイント"
guide_top_text: "サブスクリプショングループREST APIを使用して、Brazeダッシュボードの<strong>サブスクリプショングループ</strong>ページに保存したサブスクリプショングループをプログラムで管理します。これは、SMSとメールの両方のサブスクリプショングループに適用されます。<br><br>サブスクリプショングループの作成に関するガイダンスをお探しですか？<a href='/docs/user_guide/message_building_by_channel/sms/sms_subscription_group'>SMSサブスクリプショングループ</a> と<a href='/docs/user_guide/message_building_by_channel/email/managing_user_subscriptions'>メールサブスクリプショングループ</a> の記事をご覧ください。"

guide_featured_title: ""
guide_featured_list:
  - name: "GET: ユーザーのサブスクリプショングループステータスを一覧表示"
    link: /docs/api/endpoints/subscription_groups/get_list_user_subscription_group_status
    image: /assets/img/braze_icons/users-01.svg
  - name: "GET: ユーザーのサブスクリプショングループを一覧表示"
    link: /docs/api/endpoints/subscription_groups/get_list_user_subscription_groups
    image: /assets/img/braze_icons/users-01.svg
  - name: "POST: ユーザーのサブスクリプショングループステータスを更新"
    link: /docs/api/endpoints/subscription_groups/post_update_user_subscription_group_status
    image: /assets/img/braze_icons/user-plus-01.svg
  - name: "POST: ユーザーのサブスクリプショングループステータスを更新 V2"
    link: /docs/api/endpoints/subscription_groups/post_update_user_subscription_group_status_v2
    image: /assets/img/braze_icons/user-edit.svg
---
<br>
<br>


## サブスクリプショングループの時系列を理解する {#understand-subscription-group-timeseries}

**サブスクリプショングループ**ページの時系列チャートでは、以下の指標がレポートされます。

- **サブスクリプショングループサイズ：** 特定の日付にそのグループを購読しているユーザー数
- **サブスクリプショングループ購読解除サイズ：** 特定の日付にそのグループから購読解除したユーザー数

ダッシュボードのガイダンスについては、[サブスクリプショングループサイズの表示]({{site.baseurl}}/user_guide/channels/email/subscriptions#viewing-subscription-group-sizes)を参照してください。

これらの指標はグループ固有のものです。セグメントフィルター`Email Subscription Status is Unsubscribed`とは異なる場合があります。このフィルターは、単一のサブスクリプショングループではなく、グローバルなメールサブスクリプション状態を反映します。非常に大規模なワークスペースでは、正確なカウントが利用できない場合にBrazeが推定カウントを表示することがあります。

## メールキャプチャフォームからの重複ユーザーを回避する {#avoid-duplicate-users-from-email-capture-forms}

メールキャプチャフォームからユーザーを作成する前に、[`/subscription/status/get`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status)を呼び出して、プロファイルが既に存在するかどうかを確認します。応答が「User not found」の場合は、[`/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status)を使用してユーザーを作成します。それ以外の場合は、重複を作成するのではなく、既存のプロファイルを更新してください。

## Snowflakeの`USERS_MESSAGES_EMAIL_UNSUBSCRIBE`イベント {#snowflake-users_messages_email_unsubscribe-events}

Snowflakeの`USERS_MESSAGES_EMAIL_UNSUBSCRIBE`テーブルには、受信者側から発生したメッセージレベルのメール購読解除が記録されます。これには、購読解除リンクのクリック、メールクライアントのワンクリックList-Unsubscribe、ユーザー設定センターからの送信、メールサービスプロバイダー (ESP) から報告された購読解除が含まれます。REST APIを通じて行われた購読解除はこのテーブルには含まれません。それらは代わりに[`users.behaviors.subscriptiongroup.StateChange`]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#subscription-group-state-change-events)または[`users.behaviors.subscription.GlobalStateChange`]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#global-subscription-state-change-events)イベントを発行します。

## SMSテストメッセージとサブスクリプショングループ {#sms-test-messages-and-subscription-groups}

SMSテストメッセージを受信するには、受信者がテスト送信時に選択したSMSサブスクリプショングループに所属している必要があります。