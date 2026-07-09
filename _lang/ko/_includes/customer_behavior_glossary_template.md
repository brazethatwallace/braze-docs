---
# This file is a template consumed by the external `braze-currents-generate-docs` tool
# (braze-agent-plugins / braze-currents plugin) to generate the Currents event glossary
# docs. It is not referenced from within braze-docs, so do not delete it as "unused".
nav_title: 고객 행동 및 사용자 이벤트
article_title: 고객 행동 및 사용자 이벤트
layout: customer_behavior_events_glossary
page_order: 4
excerpt_separator: ""
page_type: glossary
description: "이 용어집에는 Braze가 추적하고 Currents를 사용하여 선택한 데이터 웨어하우스로 전송할 수 있는 다양한 고객 행동 및 사용자 이벤트가 나열되어 있습니다."
tool: Currents
search_rank: 7
---

<div class="api-glossary-preamble" markdown="1">

{% details 스키마 범위 및 관련 리소스 %}

스토리지 스키마는 데이터 웨어하우스 스토리지 파트너(Google Cloud Storage, Amazon S3, Microsoft Azure Blob Storage)로 전송하는 플랫 파일 이벤트 데이터에 적용됩니다. 여기에 나열된 일부 이벤트 및 대상 조합은 아직 일반적으로 사용할 수 없습니다. 다양한 파트너가 지원하는 이벤트에 대한 정보는 [사용 가능한 파트너]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/available_partners) 목록을 참조하고 해당 페이지를 확인하세요.

{% alert tip %}
이러한 이벤트는 [쿼리 빌더]({{site.baseurl}}/user_guide/analytics/reports/query_builder), [SQL 세그먼트 확장]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments), [Snowflake 데이터 공유]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake)에서 SQL 테이블로도 사용할 수 있습니다. SQL 테이블 스키마 및 열 세부 정보는 [SQL 테이블 참조]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables)를 참조하세요.
{% endalert %}

추가 이벤트 권한에 대한 액세스가 필요한 경우 Braze 담당자에게 문의하거나 [지원 티켓]({{site.baseurl}}/braze_support)을 열어주세요. 이 페이지에서 필요한 내용을 찾을 수 없는 경우 [메시지 인게이지먼트 이벤트 라이브러리]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) 또는 [Currents 샘플 데이터 예시](https://github.com/Appboy/currents-examples/tree/master/sample-data)를 확인하세요.

{% enddetails %}

{% details 고객 행동 및 사용자 이벤트 구조와 플랫폼 값 설명 %}

## 이벤트 구조 {#event-structure}

이 고객 행동 및 사용자 이벤트 분석은 고객 행동 또는 사용자 이벤트에 일반적으로 포함되는 정보 유형을 보여줍니다. 구성 요소를 확실히 이해하면 개발자와 비즈니스 인텔리전스 전략 팀이 수신되는 Currents 이벤트 데이터를 사용하여 데이터 중심 보고서와 차트를 만들고 기타 유용한 데이터 측정기준을 활용할 수 있습니다.

![사용자별 속성, 행동별 속성, 기기별 속성으로 그룹화된 속성이 나열된 구매 이벤트를 보여주는 사용자 이벤트 분석]({% image_buster /assets/img/customer_engagement_event.png %})

고객 행동 및 사용자 이벤트는 **사용자별** 속성, **행동별** 속성, **기기별** 속성으로 구성됩니다.

### 플랫폼 값 {#platform-values}

특정 이벤트는 사용자 기기의 플랫폼을 지정하는 `platform` 값을 반환합니다.
<br>다음 표에는 반환될 수 있는 값이 자세히 나와 있습니다.

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

{% details 고객 행동 및 사용자 이벤트에 대한 고려 사항 %}

- Currents는 900&nbsp;KB를 초과하는 과도하게 큰 페이로드를 가진 이벤트를 삭제합니다.
- 이 용어집의 많은 이벤트는 SDK에서 시작됩니다. `token_state_change`와 같은 일부 이벤트는 SDK 또는 백엔드에서 시작될 수 있습니다(예: 푸시 바운스에 대한 응답). `sdk_version`, `gender`, `language`, `country` 필드는 SDK에서 시작된 이벤트에 대해서만 설정됩니다. 백엔드에서 시작된 이벤트이거나 해당 정보를 사용할 수 없거나 사용자에 대해 설정되지 않은 경우 이러한 필드는 `null`일 수 있습니다.

{% enddetails %}

</div>

<!--overview-end-->