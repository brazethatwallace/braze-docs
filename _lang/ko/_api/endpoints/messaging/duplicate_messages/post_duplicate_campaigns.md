---
nav_title: "POST: Campaign 복제"
article_title: "POST: Campaign 복제"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "이 문서에서는 Campaign 복제 엔드포인트에 대한 세부 정보를 설명합니다."

---
{% api %}
# API를 사용하여 Campaign 복제 {#duplicate-campaigns-using-the-api}
{% apimethod post core_endpoint|/docs/core_endpoints %}
/campaigns/duplicate
{% endapimethod %}

> 이 엔드포인트를 사용하여 Campaign을 복제합니다. 이 API 엔드포인트는 [Braze 대시보드에서 Campaign을 복제하는 것][1]과 유사합니다.

## 필수 조건 {#prerequisites}

이 엔드포인트를 사용하려면 `campaigns.duplicate` 권한으로 API 키를 생성해야 합니다.

## 사용량 제한 {#rate-limit}

이 엔드포인트는 분당 100회의 API 호출로 제한됩니다.

## 요청 본문 {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "campaign_id": (required, string) The campaign identifier,
  "name": (required, string) The name of the resulting campaign,
  "description": (optional, string) The description of the resulting campaign,
  "tag_names": (optional, string) The tags of the resulting campaign,
}
```

## 요청 매개변수 {#request-parameters}

| 매개변수 | 필수 | 데이터 유형 | 설명 |
| --------- | ---------| --------- | ----------- |
| `campaign_id` | 필수 | 문자열 | [Campaign 식별자]({{site.baseurl}}/api/identifier_types)를 참조하세요. |
| `name` | 필수 | 문자열 | 결과 Campaign의 이름입니다. |
| `description` | 선택 사항 | 문자열 | 결과 Campaign의 설명 필드입니다. |
| `tag_names` | 선택 사항 | 문자열 | 결과 Campaign의 태그입니다. 기존 태그여야 합니다. 요청에 새 태그를 추가하면 원래 Campaign에 있던 태그를 덮어씁니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="요청 매개변수" }


## 응답 {#response}

이 엔드포인트는 `202` 상태 코드를 반환하며, Campaign 생성은 비동기적으로 처리됩니다. [보안 이벤트 다운로드][2]를 사용하여 Campaign이 언제, 어떤 API 키에 의해 복제되었는지 기록을 확인할 수 있습니다.


[1]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/duplicating_segments_and_campaigns#duplicating-segments-campaigns-and-canvases
[2]: {{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/#downloading-a-security-event-report

{% endapi %}