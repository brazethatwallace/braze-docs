---
# This file is a template consumed by the external `braze-currents-generate-docs` tool
# (braze-agent-plugins / braze-currents plugin) to generate the Currents event glossary
# docs. It is not referenced from within braze-docs, so do not delete it as "unused".
nav_title: 메시지 인게이지먼트 이벤트
layout: message_engagement_events_glossary
alias: /message_events_glossary/
page_order: 5
excerpt_separator: ""
page_type: glossary
description: "이 용어집에는 Braze가 추적하고 Currents를 사용하여 선택한 데이터 웨어하우스로 전송할 수 있는 다양한 메시지 인게이지먼트 이벤트가 나열되어 있습니다."
tool: Currents
search_rank: 6
lazy_partner_tabs: true
---

<div class="api-glossary-preamble" markdown="1">

{% details 스키마 범위 및 관련 리소스 %}

스토리지 스키마는 데이터 웨어하우스 스토리지 파트너(Google Cloud Storage, Amazon S3, Microsoft Azure Blob Storage)에 전송하는 플랫 파일 이벤트 데이터에 적용됩니다. 다른 파트너에 적용되는 스키마는 [사용 가능한 파트너]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/available_partners) 목록을 참조하고 해당 페이지를 확인하세요.

{% alert tip %}
이러한 이벤트는 [쿼리 빌더]({{site.baseurl}}/user_guide/analytics/reports/query_builder), [SQL 세그먼트 확장]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments), [Snowflake 데이터 공유]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake)에서 SQL 테이블로도 사용할 수 있습니다. SQL 테이블 스키마 및 열 세부 정보는 [SQL 테이블 참조]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables)를 참조하세요.
{% endalert %}

추가 이벤트 권한에 대한 액세스가 필요한 경우 계정 매니저에게 문의하거나 [지원 티켓]({{site.baseurl}}/braze_support)을 열어 주세요. 이 문서에서 필요한 내용을 찾을 수 없는 경우 [고객 행동 이벤트 라이브러리]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events) 또는 [Currents 샘플 데이터 예시](https://github.com/Appboy/currents-examples/tree/master/sample-data)를 확인하세요.

{% enddetails %}

{% details 메시지 인게이지먼트 이벤트 구조 및 플랫폼 값 설명 %}

## 이벤트 구조 {#event-structure}

이 이벤트 분석은 메시지 인게이지먼트 이벤트에 일반적으로 포함되는 정보 유형을 보여줍니다. 구성 요소를 확실히 이해하면 개발자와 비즈니스 인텔리전스 전략 팀이 수신되는 Currents 이벤트 데이터를 사용하여 데이터 중심 보고서와 차트를 만들고 기타 유용한 데이터 측정기준을 활용할 수 있습니다.

![사용자별 속성, Campaign 또는 Canvas 추적 속성, 이벤트별 속성으로 그룹화된 속성이 나열된 이메일 탈퇴 이벤트를 보여주는 메시지 인게이지먼트 이벤트 분석]({% image_buster /assets/img/message_engagement_event.png %})

메시지 인게이지먼트 이벤트는 **사용자별** 속성, **Campaign/Canvas 추적** 속성, **이벤트별** 속성으로 구성됩니다.

### 사용자 ID 스키마 {#user-id-schema}

사용자 ID의 명명 규칙에 유의하세요.

| Braze 스키마 | Currents 스키마 | 설명 |
| ----------- | ----------- | ----------- |
| `braze_id` | `"USER_ID"` | Braze에서 자동으로 할당하는 고유 식별자입니다. |
| `external_id` | `"EXTERNAL_USER_ID"` | 고객이 설정한 사용자 프로필의 고유 식별자입니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="사용자 ID 스키마" }

### 플랫폼 값 {#platform-values}

특정 이벤트는 사용자 기기의 플랫폼을 지정하는 `platform` 값을 반환합니다.
<br>다음 표에는 반환될 수 있는 값이 나열되어 있습니다.

| 사용자 기기 | 플랫폼 값 |
| --- | --- |
| iOS | `ios` |
| Android | `android` |
| FireTV | `kindle` |
| Kindle | `kindle` |
| 웹 | `web` |
| tvOS | `tvos` |
| Roku | `roku` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="플랫폼 값" }

{% enddetails %}

{% details 메시지 인게이지먼트 이벤트 관련 고려 사항 %}

- Currents는 페이로드가 900&nbsp;KB를 초과하는 이벤트를 삭제합니다.
- Canvas Flow와 관련된 객체에는 그룹화에 사용할 수 있는 ID가 있으며, [Canvas 세부 정보 내보내기 엔드포인트]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details)를 통해 사람이 읽을 수 있는 이름으로 변환할 수 있습니다.
- Campaign 또는 Canvas를 업데이트한 직후에는 특정 필드에 최신 상태가 즉시 표시되지 않을 수 있습니다.
  - `campaign_name`
  - `canvas_name`
  - `canvas_step_name`
  - `conversion_behavior`
  - `canvas_variation_name`
  - `experiment_split_name`
  - `message_variation_name`
- 이러한 필드에 대해 완전한 일관성이 필요한 경우, 마지막 업데이트 후 1시간을 기다린 다음 사용자에게 메시지를 보내세요.

{% enddetails %}

</div>

<!--overview-end-->