---
nav_title: "GET: Canvas 데이터 요약 분석 내보내기"
article_title: "GET: Canvas 데이터 요약 분석 내보내기"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "이 문서에서는 Canvas 데이터 요약 분석 내보내기 Braze 엔드포인트에 대해 설명합니다."

---
{% api %}
# Canvas 데이터 요약 분석 내보내기 {#export-canvas-data-summary-analytics}
{% apimethod get %}
/canvas/data_summary
{% endapimethod %}

> 이 엔드포인트를 사용하여 Canvas의 시계열 데이터 롤업을 내보내고, Canvas 결과의 간결한 요약을 제공합니다.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#1eb1b760-6b00-4c03-bcfb-12646f2ba6da {% endapiref %}

## 필수 조건 {#prerequisites}

이 엔드포인트를 사용하려면 `canvas.data_summary` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key-permissions)가 필요합니다.

## 사용량 제한 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## 요청 매개변수 {#request-parameters}

| 매개변수 | 필수 | 데이터 유형 | 설명 |
| --------- | -------- | --------- | ----------- |
| `canvas_id` | 필수 | 문자열 | [Canvas API 식별자]({{site.baseurl}}/api/identifier_types)를 참조하세요. |
| `ending_at` | 필수 | 날짜/시간 <br>([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) 문자열) | 데이터 내보내기의 종료 날짜입니다. 요청 시점으로 기본 설정됩니다. |
| `starting_at` | 선택 사항* | 날짜/시간 <br>([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) 문자열) | 데이터 내보내기의 시작 날짜입니다. <br><br>* `length` 또는 `starting_at` 중 하나가 필요합니다. |
| `length` | 선택 사항* | 문자열 | 반환된 시리즈에 포함된 `ending_at` 이전의 최대 일수입니다. 1에서 14 사이여야 합니다(포함). <br><br>* `length` 또는 `starting_at` 중 하나가 필요합니다. |
| `include_variant_breakdown` | 선택 사항 | 부울 | 배리언트 통계를 포함할지 여부입니다(기본값은 `false`). |
| `include_step_breakdown` | 선택 사항 | 부울 | 단계 통계를 포함할지 여부입니다(기본값은 `false`). |
| `include_deleted_step_data` | 선택 사항 | 부울 | 삭제된 단계에 대한 단계 통계를 포함할지 여부입니다(기본값은 `false`). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="요청 매개변수" }

{% alert important %}
Canvas 분석은 Braze에서 회사에 설정된 시간대(대시보드에서 사용하는 시간대와 동일)를 기준으로 일별로 집계됩니다. API는 `starting_at`과 `ending_at`을 해당 시간대의 자정으로 정규화합니다. 통계가 대시보드와 일치하도록 타임스탬프가 회사의 시간대에 맞는지 확인하세요. 예를 들어, 회사 시간대가 UTC+2인 경우 타임스탬프는 UTC+2 기준 오전 12시여야 합니다.
{% endalert %}

## 요청 예시 {#example-request}

{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/canvas/data_summary?canvas_id={{canvas_id}}&ending_at=2018-05-30T23:59:59-05:00&starting_at=2018-05-28T23:59:59-05:00&length=5&include_variant_breakdown=true&include_step_breakdown=true&include_deleted_step_data=true' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## 응답 {#response}

### 전환 이벤트 필드 {#conversion-event-fields}

응답에는 Canvas에 구성된 각 전환 이벤트에 대해 한 쌍의 전환 필드가 포함됩니다. 주요 전환 이벤트는 `conversions`와 `conversions_by_entry_time`을 사용합니다. 각 추가 이벤트는 동일한 기본 이름에 숫자 접미사를 사용하며, 두 번째 이벤트는 `1`부터 시작하여 추가 이벤트마다 1씩 증가합니다.

| Canvas에서의 전환 이벤트 순서 | 전환 필드 | 진입 시간 기준 필드 |
| --- | --- | --- |
| 주요 | `conversions` | `conversions_by_entry_time` |
| 두 번째 | `conversions1` | `conversions1_by_entry_time` |
| 세 번째 | `conversions2` | `conversions2_by_entry_time` |
| 네 번째 | `conversions3` | `conversions3_by_entry_time` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="전환 순서" }

다섯 번째 이후의 이벤트도 동일한 패턴을 따릅니다(예: `conversions4` 및 `conversions4_by_entry_time`). 이러한 필드는 `total_stats`에 나타나며, 분석 세부 정보를 요청하면 `variant_stats`와 `step_stats`에서도 동일한 이름으로 나타납니다.

{% alert note %}
`total_stats`, `variant_stats`, `step_stats`에서 `conversions`는 Canvas의 [주요 전환 이벤트]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events) 횟수입니다. 추가 전환 이벤트를 구성하면 페이로드에 두 번째, 세 번째 및 이후 이벤트에 대한 `conversions1`, `conversions2` 및 더 높은 인덱스의 필드가 포함될 수 있습니다. 이는 `/campaigns/data_series` 엔드포인트의 [다변량 응답]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics#multivariate-response)과 유사합니다. `_by_entry_time`으로 끝나는 필드가 있는 경우, 해당 전환은 Canvas 진입 시간을 기준으로 귀속됩니다.
{% endalert %}

```json
{
  "data": {
    "name": (string) the Canvas name,
    "total_stats": {
      "revenue": (float) the number of dollars of revenue (USD),
      "entries": (int) the number of entries,
      "conversions": (int) the number of conversions for the primary conversion event,
      "conversions_by_entry_time": (int) the number of conversions for the primary conversion event by entry time,
      "conversions1": (optional, int) the number of conversions for the second conversion event,
      "conversions1_by_entry_time": (optional, int) the number of conversions for the second conversion event by entry time,
      "conversions2": (optional, int) the number of conversions for the third conversion event,
      "conversions2_by_entry_time": (optional, int) the number of conversions for the third conversion event by entry time,
      "conversions3": (optional, int) the number of conversions for the fourth conversion event,
      "conversions3_by_entry_time": (optional, int) the number of conversions for the fourth conversion event by entry time
    },
    "variant_stats": (optional) {
      "00000000-0000-0000-0000-0000000000000": (string) the API identifier for the variant {
        "name": (string) the name of the variant,
        "revenue": (float) the number of dollars of revenue (USD),
        "conversions": (int) the number of conversions for the primary conversion event,
        "conversions_by_entry_time": (optional, int) the number of conversions for the primary conversion event by entry time,
        "conversions1": (optional, int) the number of conversions for the second conversion event,
        "conversions1_by_entry_time": (optional, int) the number of conversions for the second conversion event by entry time,
        "conversions2": (optional, int) the number of conversions for the third conversion event,
        "conversions2_by_entry_time": (optional, int) the number of conversions for the third conversion event by entry time,
        "conversions3": (optional, int) the number of conversions for the fourth conversion event,
        "conversions3_by_entry_time": (optional, int) the number of conversions for the fourth conversion event by entry time,
        "entries": (int) the number of entries
      },
      ... (more variants)
    },
    "step_stats": (optional) {
      "00000000-0000-0000-0000-0000000000000": (string) the API identifier for the step {
        "name": (string) the name of the step,
        "revenue": (float) the number of dollars of revenue (USD),
        "conversions": (int) the number of conversions for the primary conversion event,
        "conversions_by_entry_time": (int) the number of conversions for the primary conversion event by entry time,
        "conversions1": (optional, int) the number of conversions for the second conversion event,
        "conversions1_by_entry_time": (optional, int) the number of conversions for the second conversion event by entry time,
        "conversions2": (optional, int) the number of conversions for the third conversion event,
        "conversions2_by_entry_time": (optional, int) the number of conversions for the third conversion event by entry time,
        "conversions3": (optional, int) the number of conversions for the fourth conversion event,
        "conversions3_by_entry_time": (optional, int) the number of conversions for the fourth conversion event by entry time,
        "messages": {
          "android_push": (name of channel) [
            {
              "sent": (int) the number of sends,
              "opens": (int) the number of opens,
              "influenced_opens": (int) the total number of opens (includes both direct opens and influenced opens),
              "bounces": (int) the number of bounces
              ... (more stats for channel)
            }
          ],
          ... (more channels)
        }
      },
      ... (more steps)
    }
  },
  "message": (string) returns 'success' when the request completes without errors
}
```

{% alert important %}
API 응답에서 `influenced_opens` 필드는 총 열람 수(직접 열람과 영향받은 열람을 모두 포함)를 나타냅니다. Braze 대시보드에서 "영향받은 열람"은 직접 열람을 제외한 영향받은 열람만을 의미합니다. 이는 API의 레거시 명명 규칙 때문입니다.
{% endalert %}

## 관련 문서 {#related-articles}

- [내보내기 문제 해결]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting)


{% endapi %}