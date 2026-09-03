---
nav_title: 고객 프로필
layout: user_profiles_event_glossary
page_order: 4
excerpt_separator: ""
page_type: glossary
description: "이 용어집에는 Braze가 추적하고 Currents를 사용하여 선택한 데이터 웨어하우스로 전송할 수 있는 고객 프로필 업데이트가 나열되어 있습니다."
tool: Currents
search_rank: 7
---

<div class="api-glossary-preamble" markdown="1">

{% alert tip %}
이러한 이벤트는 [쿼리 빌더]({{site.baseurl}}/user_guide/analytics/reports/query_builder), [SQL 세그먼트 확장]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments), [Snowflake 데이터 공유]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake)에서 SQL 테이블로도 사용할 수 있습니다. SQL 테이블 스키마 및 열 세부 정보는 [SQL 테이블 참조]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables)를 참조하세요. Snowflake 데이터 공유의 고객 프로필 속성 뷰 스키마는 [고객 프로필 속성]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/user_attributes)을 참조하세요.
{% endalert %}

추가 이벤트 권한에 대한 액세스가 필요한 경우 Braze 담당자에게 문의하거나 [지원 티켓]({{site.baseurl}}/user_guide/administer/personal/braze_support)을 열어주세요. 이 페이지에서 필요한 정보를 찾을 수 없는 경우 [고객 행동 이벤트 라이브러리]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events), [메시지 인게이지먼트 이벤트 라이브러리]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) 또는 [Currents 샘플 데이터 예시](https://github.com/Appboy/currents-examples/tree/master/sample-data)를 참조하세요.

{% details 고객 프로필 업데이트 이벤트 구조 설명 %}

### 이벤트 구조 {#event-structure}

이 고객 행동 및 사용자 이벤트 분석은 고객 프로필 업데이트 이벤트에 일반적으로 포함되는 정보 유형을 보여줍니다. 구성 요소를 확실히 이해하면 개발자와 비즈니스 인텔리전스 전략 팀이 수신되는 Currents 이벤트 데이터를 활용하여 데이터 중심 보고서와 차트를 만들고, 기타 유용한 데이터 측정기준을 활용할 수 있습니다.

{% alert important %}
스토리지 스키마는 Google Cloud Storage, Amazon S3, Microsoft Azure Blob Storage와 같은 데이터 웨어하우스 스토리지 파트너에게 전송되는 플랫 파일 이벤트 데이터에 적용됩니다. 여기에 나열된 일부 이벤트 및 대상 조합은 아직 일반 제공되지 않습니다. 파트너별 지원 이벤트에 대한 정보는 [사용 가능한 파트너]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/available_partners) 및 관련 파트너 페이지를 참조하세요.

Currents는 페이로드가 900KB보다 큰 이벤트를 삭제합니다.
{% endalert %}

{% enddetails %}

</div>

<!--overview-end-->