---
nav_title: 9월
page_order: 4
noindex: true
page_type: update
description: "이 문서에는 2017년 9월의 릴리스 노트가 포함되어 있습니다."
---

# 2017년 9월 {#september-2017}

## 참여 보고서의 새로운 기능 {#new-functionality-for-engagement-reports}

이제 [참여 보고서]({{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports/#engagement-reports)를 사용하여 특정 기간 동안 Campaign에 대한 측정기준을 집계할 수 있습니다. 예를 들어, 분기별 총 열람 수 또는 Campaign이나 Canvas의 전체 기간 동안의 총 클릭 수를 내보낼 수 있습니다. 다음 단계만 수행하면 됩니다:
- 데이터를 내보낼 기간을 선택합니다.
- 한 명 이상의 수신자에게 정기적으로 전송되는 참여 보고서를 스케줄합니다.
- 태그를 기반으로 Campaigns와 Canvases를 보고서에 추가합니다.

## 고객 프로필 페이지 업데이트 {#updates-to-user-profile-page}

[고객 프로필 페이지]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles/#using-user-search)가 업데이트되었습니다.

## 해제하려면 사용자 동작이 필요한 웹 푸시 알림 {#web-push-notifications-that-require-user-action-to-dismiss}

이제 Chrome 웹 푸시에 대해 메시지 닫기 동작을 설정하여 수신자가 메시지와 상호 작용해야만 메시지가 해제되도록 할 수 있습니다. 이 기능을 사용하려면 웹 SDK 버전 1.6.13 이상이 필요합니다.

## 이메일 프리헤더 {#email-preheaders}

이제 Braze 내에서 이메일 메시지를 작성할 때 **Sending Info** 섹션에서 프리헤더를 쉽게 삽입할 수 있습니다.

## 원시 이벤트 내보내기를 위한 새로운 API 엔드포인트 {#new-api-endpoint-for-raw-event-export}

특정 날짜가 원시 이벤트 내보내기에 로드되었는지 쿼리할 수 있는 새로운 [API 엔드포인트]({{site.baseurl}}/developer_guide/rest_api/api_network_connectivity_issues/#whitelisting-brazes-api-endpoint-ip-ranges)인 `/raw_data/status`를 추가했습니다. 특정 날짜의 원시 데이터를 사용할 수 있는지 확인하여 디버깅 및 자동화에 활용할 수 있습니다.