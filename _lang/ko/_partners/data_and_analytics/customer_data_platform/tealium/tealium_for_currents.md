---
nav_title: Tealium for Currents
article_title: Tealium for Currents
page_order: 3
alias: /partners/tealium_for_currents/
description: "이 참조 문서에서는 마케팅 스택의 소스 간에 정보를 수집하고 라우팅하는 고객 데이터 플랫폼인 Tealium과 Braze 커런츠 간의 파트너십에 대해 설명합니다."
page_type: partner
tool: Currents
search_tag: Partner

---

# Tealium for Currents

> [Tealium](https://www.tealium.com)은 여러 소스에서 정보를 수집하고 마케팅 스택의 다양한 위치로 라우팅하는 고객 데이터 플랫폼입니다.

Braze와 Tealium 통합을 사용하면 두 시스템 간의 정보 흐름을 원활하게 제어할 수 있습니다. Currents를 사용하면 데이터를 Tealium에 연결하여 전체 성장 스택에서 활용할 수도 있습니다.

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Tealium EventStream 또는 Tealium AudienceStream | 이 파트너십을 활용하려면 [Tealium 계정](https://my.tealiumiq.com/)이 필요합니다. |
| Currents | 데이터를 Tealium으로 다시 내보내려면 계정에 [Braze 커런츠]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents)가 설정되어 있어야 합니다. |
| Tealium URL | Tealium 대시보드로 이동하여 수집 URL을 복사하면 얻을 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="필수 조건" }

## 통합 {#integration}

### 1단계: Tealium 내에서 Braze용 데이터 소스 생성 {#step-1-create-a-data-source-for-braze-within-tealium}

데이터 소스 생성에 대한 안내는 [Tealium](https://docs.tealium.com/server-side/data-sources/webhooks/braze-currents/) 사이트에서 확인할 수 있습니다. 완료되면 Tealium에서 복사할 데이터 소스 URL을 제공하며, 이를 다음 단계에서 사용합니다.

### 2단계: Current 생성 {#step-2-create-current}

Braze에서 **Currents** > **+ Create Current** > **Tealium Export**로 이동합니다. 통합 이름, 연락처 이메일, Tealium URL을 입력합니다.

다음으로, 사용 가능한 이벤트 목록에서 추적할 항목을 선택합니다. 기본적으로 Tealium으로 전송되는 모든 이벤트에는 사용자의 `external_user_id`가 포함됩니다. 그러나 **Include events from anonymous users** 체크박스를 선택하면 `external_user_id`가 없는 이벤트도 Tealium으로 전송할 수 있습니다.

통합 설정을 완료한 후 **Launch Current**을 선택합니다.

{% alert important %}
Tealium URL을 항상 최신 상태로 유지하는 것이 중요합니다. 커넥터의 URL이 올바르지 않으면 Braze에서 이벤트를 전송할 수 없습니다. 이 상태가 **5일** 이상 지속되면 커넥터의 이벤트가 삭제되고 데이터가 영구적으로 손실됩니다.
{% endalert %}

## 통합 세부 정보 {#integration-details}

Braze는 [Currents 이벤트 용어집]({{site.baseurl}}/user_guide/data/distribution/braze_currents/)에 나열된 모든 데이터([메시지 참여]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/) 및 [고객 행동]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/) 이벤트의 모든 등록정보 포함)를 Tealium으로 내보내기를 지원합니다.

내보낸 데이터의 페이로드 구조는 커스텀 HTTP 커넥터의 페이로드 구조와 동일하며, [커스텀 HTTP 커넥터 예제 리포지토리](https://github.com/Appboy/currents-examples/tree/master/sample-data/Custom%20HTTP/users/behaviors)에서 확인할 수 있습니다.