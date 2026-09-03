---
nav_title: 4월
page_order: 8
noindex: true
page_type: update
description: "이 문서에는 2021년 4월의 릴리스 노트가 포함되어 있습니다."
---
# 2021년 4월 {#april-2021}

## iOS 푸시 고급 구현 가이드 {#ios-push-advanced-implementation-guide}

이 상세 가이드에서는 푸시 알림 콘텐츠 앱 확장 기능을 활용하여 푸시 메시지를 최대한 활용하는 방법을 다룹니다. 저희 팀이 구축한 세 가지 커스텀 사용 사례(인터랙티브 푸시, 데이터 캡처 푸시, 진행 상태 기반 푸시)와 함께 코드 스니펫 및 분석 로깅에 대한 안내가 포함되어 있습니다. 자세한 내용은 [iOS 푸시 고급 구현 가이드]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/implementation_guide)를 확인하세요.

## MMS(멀티미디어 메시지 서비스)에 대한 VFC 지원 {#vfc-support-for-multimedia-message-service-mms}

vCard는 가상 연락처 파일(VCF)이라고도 하며, 주소록/연락처에 쉽게 가져올 수 있는 비즈니스/연락처 정보를 전송하기 위한 표준화된 파일 형식입니다. 이러한 VCF 파일은 이제 [MMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/create)를 통해 전송하고 Braze 미디어 라이브러리에 추가할 수 있습니다.

## 사용자 삭제 업데이트 {#updates-to-user-delete}

2020년 10월, 사용자 삭제가 데이터 주체의 전화번호 또는 이메일 주소를 처리하는 방식에 대한 [개선]({{site.baseurl}}/releases/2020/october)이 이루어졌습니다.

## 새로운 Braze 파트너십 {#new-braze-partnerships}

### Airbridge - 기여도 {#airbridge-attribution}

[Airbridge와 Braze 통합]({{site.baseurl}}/partners/message_orchestration/attribution/airbridge)을 통해 모든 오가닉 및 비오가닉 설치 기여도 데이터를 Braze로 전달하여 더욱 개인화된 마케팅 Campaigns를 구축하고 사용자가 어디에서 유입되었는지 정확히 파악할 수 있습니다.

### Kubit - 분석 {#kubit-analytics}

[Kubit]({{site.baseurl}}/partners/data_and_analytics/analytics/kubit)은 즉각적인 제품 인사이트를 제공하는 노코드 셀프 서비스 분석 플랫폼입니다. Braze와의 원활한 노코드 통합을 통해 사용자 코호트 정보를 Braze로 가져오고 특정 코호트를 타겟팅하는 인게이지먼트 Campaigns를 실행할 수 있습니다. 또한 Snowflake 보안 데이터 공유를 활용하면 Braze의 원시 Campaign 및 노출 횟수 데이터를 Kubit의 제품 분석과 통합하여 이러한 Campaigns의 효과를 실시간으로 측정할 수 있습니다.

### Census - 고객 데이터 플랫폼 {#census-customer-data-platform}

[Census]({{site.baseurl}}/partners/data_and_analytics/reverse_etl/census)를 사용하면 엔지니어링 부서의 지속적인 도움 없이도 고객 데이터를 동기화하여 고객 성공, 영업, 마케팅 팀이 동일한 정보를 공유할 수 있습니다.

### Treasure Data - 고객 데이터 플랫폼 {#treasure-data-customer-data-platform}

[Treasure Data]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/treasure_data)는 데이터, 인사이트, 인게이지먼트를 완벽하게 조화시켜 관련성 높은 고객 경험을 제공합니다. 실행 가능한 지표를 바탕으로 마케팅, 영업, 고객 서비스를 포함한 CX 팀은 비용을 효과적으로 최적화하고 전체 고객 여정에 걸쳐 옴니채널 상호작용을 개인화할 수 있습니다.

## Jacquard - A/B 테스트 {#jacquard-ab-testing}

Braze 고객 참여는 멀티채널 마케팅을 통해 관계를 구축합니다. [Jacquard]({{site.baseurl}}/partners/message_personalization/dynamic_content/content_optimization_testing/jacquard)와 함께 Braze는 브랜드 보이스에 맞춤화된 브랜드 언어를 채널 전반에 걸쳐 대규모로 배포할 수 있습니다. Jacquard의 딥러닝 엔진은 테스트를 처리하고, 결과를 모니터링하며, 학습한 내용을 바탕으로 새로운 언어를 생성합니다.