---
nav_title: Currents용 RudderStack
article_title: Currents용 RudderStack
description: "이 문서에서는 Android, iOS 및 웹 애플리케이션을 위한 원활한 Braze 통합을 제공하는 오픈 소스 고객 데이터 인프라인 RudderStack과 Braze 커런츠 간의 파트너십에 대해 설명합니다."
page_type: partner
tool: Currents
search_tag: Partner

---

# Currents용 RudderStack {#rudderstack-for-currents}

> [RudderStack](https://www.rudderstack.com/)을 사용하면 클라우드 데이터 웨어하우스를 중앙 신뢰 소스로 활용하여 스택 전반에서 고객 데이터를 수집, 변환 및 활성화할 수 있습니다. 이 문서에서는 Braze 커런츠와 RudderStack 간의 연결을 설정하는 방법에 대한 개요를 제공합니다.

Braze와 RudderStack 통합을 통해 Braze 커런츠를 활용하여 Braze 이벤트를 RudderStack으로 내보내 더 심층적인 분석을 수행할 수 있습니다.

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
| --- | --- |
| RudderStack 계정 | 이 파트너십을 활용하려면 [RudderStack 계정](https://app.rudderstack.com/login)이 필요합니다. |
| Braze 대상 | RudderStack에서 [Braze를 대상으로 설정]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/rudderstack/rudderstack/#integration)해 두는 것을 권장합니다. |
| Currents | 데이터를 RudderStack으로 다시 내보내려면 계정에 [Braze 커런츠]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents)가 설정되어 있어야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="필수 조건" }

## 통합 {#integration}

### 1단계: RudderStack 내에서 Braze용 데이터 소스 생성 {#step-1-create-a-data-source-for-braze-within-rudderstack}

먼저 RudderStack 웹 앱에서 Braze 소스를 생성해야 합니다. 데이터 소스 생성에 대한 지침은 [RudderStack](https://www.rudderstack.com/docs/sources/event-streams/cloud-apps/braze-currents/) 사이트에서 확인할 수 있습니다.

완료되면 RudderStack에서 쓰기 키가 포함된 웹훅 URL을 제공하며, 다음 단계에서 이를 사용해야 합니다. 웹훅 URL은 Braze 소스의 **설정** 탭에서 찾을 수 있습니다.

### 2단계: Current 생성 {#step-2-create-current}

Braze에서 **Currents > + Create Current > RudderStack Export**로 이동합니다. 통합 이름, 연락처 이메일, RudderStack 웹훅 URL(키 필드에 입력), RudderStack 리전을 입력합니다.

### 3단계: 이벤트 내보내기 {#step-3-export-events}

다음으로 내보내려는 이벤트를 선택합니다. 마지막으로 **Launch Current**을 클릭합니다.

RudderStack으로 전송되는 모든 이벤트에는 사용자의 `external_user_id`가 포함됩니다. 현재 Braze는 `external_user_id`가 설정되지 않은 사용자에 대해서는 RudderStack으로 이벤트 데이터를 전송하지 않습니다.

## 통합 세부 정보 {#integration-details}

Braze는 [Currents 이벤트 용어집]({{site.baseurl}}/user_guide/data/distribution/braze_currents/)에 나열된 모든 데이터를 RudderStack으로 내보내는 것을 지원합니다.

내보낸 데이터의 페이로드 구조는 커스텀 HTTP 커넥터의 페이로드 구조와 동일하며, [커스텀 HTTP 커넥터 예제 리포지토리](https://github.com/Appboy/currents-examples/tree/master/sample-data/Custom%20HTTP/users/behaviors)에서 확인할 수 있습니다.