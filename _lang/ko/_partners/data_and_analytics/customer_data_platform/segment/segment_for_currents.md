---
nav_title: Currents용 Segment
article_title: Currents용 Segment
page_order: 2
alias: /partners/segment_for_currents/
description: "이 참조 문서에서는 마케팅 스택의 소스 간에 정보를 수집하고 라우팅하는 고객 데이터 플랫폼인 Segment와 Braze Currents 간의 파트너십에 대해 설명합니다."
page_type: partner
tool: Currents
search_tag: Partner

---

# Currents용 Segment {#segment-for-currents}

> [Segment](https://segment.com)는 고객 데이터를 수집, 정리 및 활성화하는 데 도움이 되는 고객 데이터 플랫폼입니다. 이 참조 문서에서는 Braze Currents와 Segment 간의 연결에 대한 개요를 제공하고, 올바른 구현 및 사용을 위한 요구 사항과 프로세스를 설명합니다.

Braze와 Segment 통합을 통해 Braze Currents를 활용하여 Braze 이벤트를 Segment로 내보내 전환, 리텐션 및 제품 사용에 대한 심층 분석을 수행할 수 있습니다.

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Segment 계정 | 이 파트너십을 활용하려면 [Segment 계정](https://app.segment.com/login)이 필요합니다. |
| Braze 대상 | Segment 통합에서 이미 [Braze를 대상으로 설정]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment/#connection-settings/)해야 합니다.<br><br>여기에는 [연결 설정]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment/#connection-settings)에서 올바른 Braze 데이터 센터와 REST API 키를 제공하는 것이 포함됩니다. |
| Currents | 데이터를 Segment로 다시 내보내려면 계정에 [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents)가 설정되어 있어야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 통합 {#integration}

### 1단계: Segment 쓰기 키 얻기 {#step-1-obtain-segment-write-key}

Segment 대시보드에서 Segment 소스를 선택합니다. 그런 다음 **Settings > API keys**로 이동합니다. 여기에서 **Segment Write Key**를 찾을 수 있습니다.

{% alert warning %}
Segment 쓰기 키를 최신 상태로 유지하는 것이 중요합니다. 커넥터의 자격 증명이 만료되면 커넥터가 이벤트 전송을 중단합니다. 이 상태가 **5일** 이상 지속되면 커넥터의 이벤트가 삭제되고 데이터가 영구적으로 손실됩니다.
{% endalert %}

### 2단계: 새 Currents 커넥터 만들기 {#step-2-create-a-new-currents-connector}

1. Braze에서 **Partner Integrations** > **Data Export**로 이동합니다.
2. **+ Create New Current** > **Segment Data Export**를 클릭합니다.
3. 그런 다음 통합 이름, 연락처 이메일, Segment 쓰기 키 및 Segment 리전을 입력합니다.

![Braze의 Segment Currents 페이지. 여기에서 통합 이름, 연락처 이메일, Segment 리전 및 API 키 필드를 찾을 수 있습니다.]({% image_buster /assets/img/segment/segment_currents_integration_config.png %})

### 3단계: 메시지 참여 이벤트 내보내기 {#step-3-export-message-engagement-events}

다음으로, 내보내려는 메시지 참여 이벤트를 선택합니다. 아래 나열된 내보내기 이벤트 및 등록정보 테이블을 참조하세요. Segment로 전송되는 모든 이벤트에는 사용자의 `external_user_id`가 `userId`로, 사용자의 `braze_id`가 `anonymousId`로 포함됩니다.

**Include events from anonymous users**가 체크되어 있는 경우에만 Braze가 `external_user_id`가 없는 사용자의 이벤트 데이터를 전송한다는 점에 유의하세요.

{% multi_lang_include early_access_beta_alert.md feature='Anonymous user export' %}

![Braze의 Segment Currents 페이지에서 사용 가능한 모든 메시지 참여 이벤트 목록.]({% image_buster /assets/img/segment/segment_currents_data_config.png %})

마지막으로, **Launch Current**를 선택합니다.

{% multi_lang_include alerts/warning_alerts.md alert='Segment Currents multiple connectors' %}

자세한 내용은 Segment [설명서](https://segment.com/docs/connections/sources/catalog/cloud-apps/braze/)를 참조하세요.

## Currents 업데이트하기 {#updating-your-current}

{% multi_lang_include updating_currents.md %}

## 지원되는 Currents 이벤트 {#supported-currents-events}

Braze는 다음 이벤트를 Segment로 내보내는 것을 지원합니다:

- [메시지 참여 이벤트]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/)
- [고객 행동 이벤트]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/)

각 이벤트의 페이로드 구조에 대해서는 [메시지 참여 이벤트 용어집]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/) 및 [고객 행동 이벤트 용어집]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/)에서 **Segment** 탭을 선택하세요.