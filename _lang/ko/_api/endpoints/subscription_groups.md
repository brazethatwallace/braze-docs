---
nav_title: 구독 그룹
article_title: 구독 그룹 엔드포인트
page_order: 7
layout: dev_guide

#Required
description: "이 랜딩 페이지에서는 이메일 및 SMS에 대한 Braze 구독 그룹 엔드포인트를 설명하고 나열합니다."
page_type: landing
search_tag: Endpoint

guide_top_header: "구독 그룹 엔드포인트"
guide_top_text: "구독 그룹 REST API를 사용하여 Braze 대시보드의 **구독 그룹** 페이지에 저장한 구독 그룹을 프로그래밍 방식으로 관리할 수 있습니다. 이는 SMS 및 이메일 구독 그룹 모두에 적용됩니다.<br><br> 구독 그룹 생성에 대한 안내를 찾고 계신가요? <a href='/docs/user_guide/message_building_by_channel/sms/sms_subscription_group/'>SMS 구독 그룹</a> 및 <a href='/docs/user_guide/message_building_by_channel/email/managing_user_subscriptions/'>이메일 구독 그룹</a> 문서를 확인하세요."

guide_featured_title: ""
guide_featured_list:
  - name: "GET: 사용자의 구독 그룹 상태 나열"
    link: /docs/api/endpoints/subscription_groups/get_list_user_subscription_group_status
    image: /assets/img/braze_icons/users-01.svg
  - name: "GET: 사용자의 구독 그룹 나열"
    link: /docs/api/endpoints/subscription_groups/get_list_user_subscription_groups
    image: /assets/img/braze_icons/users-01.svg
  - name: "POST: 사용자의 구독 그룹 상태 업데이트"
    link: /docs/api/endpoints/subscription_groups/post_update_user_subscription_group_status
    image: /assets/img/braze_icons/user-plus-01.svg
  - name: "POST: 사용자의 구독 그룹 상태 업데이트 V2"
    link: /docs/api/endpoints/subscription_groups/post_update_user_subscription_group_status_v2
    image: /assets/img/braze_icons/user-edit.svg
---
<br>
<br>


## 구독 그룹 시계열 이해하기 {#understand-subscription-group-timeseries}

**구독 그룹** 페이지에서 시계열 차트는 다음을 보고합니다:

- **구독 그룹 크기:** 특정 날짜에 해당 그룹에 가입된 사용자 수
- **구독 그룹 가입 취소 크기:** 특정 날짜에 해당 그룹에서 가입 취소된 사용자 수

대시보드 안내는 [구독 그룹 크기 보기]({{site.baseurl}}/user_guide/channels/email/subscriptions#viewing-subscription-group-sizes)를 참조하세요.

이 측정기준은 그룹별로 다릅니다. 글로벌 이메일 구독 상태를 반영하는 세그먼트 필터 `Email Subscription Status is Unsubscribed`와는 다를 수 있으며, 이 필터는 단일 구독 그룹이 아닌 전체 이메일 구독 상태를 나타냅니다. 매우 큰 워크스페이스의 경우, 정확한 수치를 사용할 수 없을 때 Braze가 추정 수치를 표시할 수 있습니다.

## 이메일 캡처 양식에서 중복 사용자 방지하기 {#avoid-duplicate-users-from-email-capture-forms}

이메일 캡처 양식에서 사용자를 생성하기 전에 [`/subscription/status/get`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status)을 호출하여 프로필이 이미 존재하는지 확인하세요. 응답이 "User not found"인 경우 [`/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status)을 사용하여 사용자를 생성합니다. 그렇지 않으면 중복을 생성하는 대신 기존 프로필을 업데이트하세요.

## Snowflake `USERS_MESSAGES_EMAIL_UNSUBSCRIBE` 이벤트 {#snowflake-users_messages_email_unsubscribe-events}

`USERS_MESSAGES_EMAIL_UNSUBSCRIBE` Snowflake 테이블은 수신자 측에서 발생한 메시지 수준의 이메일 가입 취소를 기록합니다. 여기에는 가입 취소 링크 클릭, 이메일 클라이언트의 원클릭 List-Unsubscribe, 환경설정 센터 제출, 이메일 서비스 공급자가 보고한 가입 취소가 포함됩니다. REST API를 통한 가입 취소는 이 테이블에 포함되지 않으며, 대신 [`users.behaviors.subscriptiongroup.StateChange`]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#subscription-group-state-change-events) 또는 [`users.behaviors.subscription.GlobalStateChange`]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#global-subscription-state-change-events) 이벤트를 발생시킵니다.

## SMS 테스트 메시지와 구독 그룹 {#sms-test-messages-and-subscription-groups}

SMS 테스트 메시지를 수신하려면 수신자가 테스트 발송 시 선택한 SMS 구독 그룹에 속해 있어야 합니다.