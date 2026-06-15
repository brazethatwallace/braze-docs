---
nav_title: 소스별 Campaign 및 Canvas 속성
article_title: 소스별 Campaign 및 Canvas 속성
page_order: 1.5
page_type: reference
description: "이 참조 문서에서는 Liquid, REST API, Currents에서 Campaign 및 Canvas 속성 이름과 ID를 비교합니다."
---

# 소스별 Campaign 및 Canvas 속성 {#campaign-and-canvas-attributes-across-sources}

> Campaign, Canvas, 캔버스 단계 이름과 ID는 모두 Liquid, Braze REST API, Currents에서 사용할 수 있습니다. 이러한 속성은 세 가지 소스 모두에서 동일한 값에 매핑되지만, 이름이 다를 수 있습니다. 이 페이지를 사용하여 세 가지 소스 간의 연결 관계를 파악하세요.

## 사용 사례 {#use-cases}

### Liquid

Campaign 및 Canvas 속성은 대시보드에서 Liquid 태그로 사용할 수 있습니다{% raw %}(`{{campaign.${api_id}}}` 등){% endraw %}. Liquid를 사용하여 메시지 자체, 연결된 콘텐츠 호출 또는 키-값 페어에 이러한 속성을 전달할 수 있습니다. 이는 일반적으로 추적 목적으로 수행됩니다.

### REST API

Campaign 및 Canvas 속성은 [Campaign 세부 정보 내보내기 엔드포인트]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details/) 또는 [Canvas 세부 정보 내보내기 엔드포인트]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/)에서도 사용할 수 있습니다. Braze REST API를 사용하여 매핑, 즉 모든 Canvas 이름과 해당 ID의 목록을 구축할 수 있습니다.

### Currents

Campaign 및 Canvas 속성은 Currents의 [메시지 참여 이벤트]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/)와 연결됩니다. 메시지 단계만 Campaign 속성에 접근할 수 있으며, 다른 캔버스 단계는 Canvas 속성에만 접근할 수 있다는 점에 유의하세요. 이는 푸시 전송이나 이메일 열기가 어떤 Campaign 또는 Canvas 구성요소와 연결되어 있는지 확인하는 데 중요합니다.

## Campaign 속성 {#campaign-attributes}

| 속성 | Liquid | REST API | Currents |
| --- | --- | --- | --- |
| Campaign 이름 | {% raw %}`{{campaign.${name}}}`{% endraw %} | `name` | `campaign_name` |
| Campaign ID | {% raw %}`{{campaign.${api_id}}}`{% endraw %} | N/A (API 호출 자체의 입력으로 사용됨) | `campaign_id` |
| 배리언트 이름 | {% raw %}`{{campaign.${message_name}}}`{% endraw %} | `messages.message_variation_id.name` | N/A (Campaign 세부 정보 내보내기 엔드포인트를 사용하여 배리언트 이름을 배리언트 ID에 매핑) |
| 배리언트 ID | {% raw %}`{{campaign.${message_api_id}}}`{% endraw %} | `messages.message_variation_id` | `message_variation_api_id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Campaign attributes" }

## Canvas 속성 {#canvas-attributes}

| 속성 | Liquid | REST API | Currents |
| --- | --- | --- | --- |
| Canvas 이름 | {% raw %}`{{canvas.${name}}}`{% endraw %} | `name` | `canvas_name` |
| Canvas ID | {% raw %}`{{canvas.${api_id}}}`{% endraw %} | N/A (API 호출 자체의 입력으로 사용됨) | `canvas_id` |
| 배리언트 이름 | {% raw %}`{{canvas.${variant_name}}}`{% endraw %} | `variants.name` | `canvas_variation_name` |
| 배리언트 ID | {% raw %}`{{canvas.${variant_api_id}}}`{% endraw %} | `variants.name.id` | `canvas_variation_id` |
| 단계 이름 (메시지 단계만 해당) | {% raw %}`{{campaign.${name}}}`{% endraw %} | `steps.name` | `canvas_step_name` |
| 단계 ID | {% raw %}`{{campaign.${api_id}}}`{% endraw %} | `steps.id` | `canvas_step_id` |
| 메시지 채널 | N/A | `steps.messages.message_variation_id.channel` | N/A (푸시 전송 또는 이메일 열기와 같은 이벤트 유형에 내재됨) |
| 메시지 ID | {% raw %}`{{campaign.${message_api_id}}}`{% endraw %} | `steps.message.message_variation_id` | `canvas_step_message_variation_api_id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Canvas attributes" }