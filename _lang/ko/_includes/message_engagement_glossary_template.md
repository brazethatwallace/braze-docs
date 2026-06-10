---
nav_title: 메시지 참여 이벤트
layout: message_engagement_events_glossary
alias: /message_events_glossary/
page_order: 5
excerpt_separator: ""
page_type: glossary
description: "이 용어집에는 Braze가 Currents를 사용하여 추적하고 선택한 데이터 웨어하우스로 전송할 수 있는 다양한 메시지 참여 이벤트가 나열되어 있습니다."
tool: Currents
search_rank: 6
lazy_partner_tabs: true
---

<div class="api-glossary-preamble" markdown="1">

{% details 스키마 범위 및 관련 리소스 %}

스토리지 스키마는 데이터 웨어하우스 스토리지 파트너(Google Cloud Storage, Amazon S3, Microsoft Azure Blob Storage)로 전송하는 플랫 파일 이벤트 데이터에 적용됩니다. 다른 파트너에 적용되는 스키마는 [사용 가능한 파트너]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/available_partners/) 목록을 참조하여 해당 페이지를 확인하세요.

{% alert tip %}
이러한 이벤트는 [쿼리 빌더]({{site.baseurl}}/user_guide/analytics/reports/query_builder/), [SQL 세그먼트 확장]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/), [Snowflake 데이터 공유]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/)에서 SQL 테이블로도 사용할 수 있습니다. SQL 테이블 스키마 및 열 세부 정보는 [SQL 테이블 참조]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables/)를 참조하세요.
{% endalert %}

추가 이벤트 권한에 대한 액세스가 필요한 경우 계정 매니저에게 문의하거나 [고객지원 티켓]({{site.baseurl}}/braze_support/)을 개설해 주세요. 이 문서에서 필요한 내용을 찾을 수 없는 경우 [고객 행동 이벤트 라이브러리]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/) 또는 [Currents 샘플 데이터 예시](https://github.com/Appboy/currents-examples/tree/master/sample-data)를 확인하세요.

{% enddetails %}

{% details 메시지 참여 이벤트 구조 및 플랫폼 값 설명 %}

### 이벤트 구조 {#event-structure}

이 이벤트 분석은 일반적으로 메시지 참여 이벤트에 어떤 유형의 정보가 포함되는지 보여줍니다. 구성요소에 대한 확실한 이해를 바탕으로 개발자와 비즈니스 인텔리전스 전략 팀은 수신되는 Currents 이벤트 데이터를 사용하여 데이터 중심 보고서와 차트를 만들고 다른 유용한 데이터 측정기준을 활용할 수 있습니다.

![메시지 참여 이벤트의 분석으로, 사용자별 등록정보, Campaign 또는 Canvas 추적 등록정보, 이벤트별 등록정보로 그룹화된 이메일 탈퇴 이벤트가 표시됩니다]({% image_buster /assets/img/message_engagement_event.png %})

메시지 참여 이벤트는 **사용자별** 등록정보, **Campaign/Canvas 추적** 등록정보, **이벤트별** 등록정보로 구성됩니다.

### 사용자 ID 스키마 {#user-id-schema}

사용자 ID의 이름 지정 규칙에 유의하세요.

| Braze 스키마 | Currents 스키마 | 설명 |
| ----------- | ----------- | ----------- |
| `braze_id` | `"USER_ID"` | Braze에서 자동으로 할당하는 고유 식별자입니다. |
| `external_id` | `"EXTERNAL_USER_ID"` | 고객이 설정한 사용자 프로필의 고유 식별자입니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="User ID schema" }

### 플랫폼 값 {#platform-values}

특정 이벤트는 사용자 기기의 플랫폼을 지정하는 `platform` 값을 반환합니다.
<br>다음 표에서는 반환 가능한 값을 자세히 설명합니다.

| 사용자 기기 | 플랫폼 값 |
| --- | --- |
| iOS | `ios` |
| Android | `android` |
| FireTV | `kindle` |
| Kindle | `kindle` |
| 웹 | `web` |
| tvOS | `tvos` |
| Roku | `roku` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Platform values" }

{% enddetails %}

{% details 메시지 참여 이벤트에 대한 고려 사항 %}

- Currents는 900&nbsp;KB를 초과하는 페이로드를 가진 이벤트를 삭제합니다.
- Canvas Flow과 관련된 오브젝트에는 그룹화에 사용할 수 있는 ID가 있으며, [Canvas 세부 정보 내보내기 엔드포인트]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/)를 통해 사람이 읽을 수 있는 이름으로 변환할 수 있습니다.
- 특정 필드는 Campaign이나 Canvas를 업데이트한 직후에 최신 상태를 즉시 표시하지 않을 수 있습니다:
  - `campaign_name`
  - `canvas_name`
  - `canvas_step_name`
  - `conversion_behavior`
  - `canvas_variation_name`
  - `experiment_split_name`
  - `message_variation_name`
- 이러한 필드에 대해 완전한 일관성이 필요한 경우, 마지막 업데이트 후 한 시간 정도 기다렸다가 사용자에게 메시지를 보내세요.

{% enddetails %}

</div>

<!--overview-end-->