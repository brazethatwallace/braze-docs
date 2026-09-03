이 템플릿을 사용하여 기술 파트너 설명서를 만들 수 있습니다. 예시는 [Scuba Analytics]({{site.baseurl}}/partners/data_and_analytics)를 참조하세요.

{% details 템플릿 보기 %}
{% raw %}
`````markdown
---
nav_title: PARTNER_NAME
article_title: PARTNER_NAME
description: "This reference article outlines the partnership between Braze and PARTNER_NAME."
alias: /partners/PARTNER_NAME/
page_type: partner
search_tag: Partner
---

# ARTICLE_TITLE
<!-- In most cases, the ARTICLE_TITLE will be your company name. If your tool requires several separate pages on Braze Docs, you can add a relevant page descriptor to those pages’ titles, such as "MyCompany Analytics." -->

> DESCRIPTION.
<!-- The description starts with a '>' character and contains an introduction to your company, a link to your main site, and a concise overview of your integration.-->

<-- Only include the following line if the partner manages the integration. If Braze manages the integration, don’t include it. -->
*This integration is maintained by PARTNER_NAME*

## About this integration
<-- Highlight the relationship between your company and Braze and how this partnership helps your customers. -->

ADDITIONAL_INFORMATION.

## Use cases
<!--Though the ‘Use cases’ section is optional, this is a good place to outline typical or even novel use cases for the integration. Use this section as a way to sell or upsell your integration to customers and Braze account teams; it provides context, ideas, and most importantly, a way to visualize the capabilities of your integration.-->

CONTENT.

<!-- When including screenshots, use the following format to specify where each screenshot should be placed. PARTNER_NAME and IMAGE_NAME should be all lowercase. -->
![ALT_TEXT]({% image_buster /assets/img/PARTNER_NAME/IMAGE_NAME.png %})

## Prerequisites
<!-- Most partner integrations require the following prerequisites. However, you may add additional prerequisites as needed. -->

Before you start, you need the following:

| Prerequisite       | Description |
|-----------------------|-----------------|
| A PARTNER_NAME account   | A PARTNER_NAME account is required to take advantage of this partnership.  |
| A Braze REST API key  | A Braze REST API key with `users.track` permissions. <br><br> Create this key in the Braze dashboard from **Settings** > **API Keys**. |
| A Braze REST endpoint | [Your REST endpoint URL]({{site.baseurl}}/developer_guide/rest_api/basics#endpoints). Your endpoint depends on the Braze URL for your instance.  |
{: .reset-td-br-1 .reset-td-br-2 aria-label=”Prerequisites” }

## Integrating TOOL_NAME
<!-- Create step-by-step instructions for integrating your tool with Braze. It's important to be concise and outline the minimum necessary steps. -->

### Step 1: ACTION_TO_COMPLETE

CONTENT.

### Step 2: Make a POST request
<!-- Use the "Make a POST request", "Default behavior," and "Rate limit" sections to outline how users can make a POST request. If this information isn't required for your integration, you can remove these sections. -->

{% alert important %}
The following request uses cURL. For better API request management, we recommend using an API client, such as Postman.
{% endalert %}

To upload your PARTNER_NAME data to Braze, make a POST request to `PARTNER_POST_URL` using the `application/json` content-type:

```bash
curl -X POST "PARTNER_POST_URL" \
-H "content-type: application/json" \
-d '{"braze_host":"BRAZE_API_ENDPOINT", \
"braze_api_key":"BRAZE_API_KEY", \
"PARTNER_host":"HOSTNAME", \
"PARTNER_token":"PARTNER_NAME_API_TOKEN"}'
```

다음을 교체하세요:

| 입력 안내 | 설명 |
|---------------------|---------------------|
| `BRAZE_API_ENDPOINT` | 현재 Braze 인스턴스의 Braze REST 엔드포인트 URL입니다. 자세한 내용은 [REST API 키]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab#rest-api-keys)를 참조하세요. |
| `BRAZE_API_KEY` | `users.track` 권한이 있는 Braze REST API 키입니다. |                                                                                                                                    | `HOSTNAME` | 현재 PARTNER_NAME 인스턴스의 호스트 이름입니다. |
| `PARTNER_NAME_API_TOKEN` | PARTNER_NAME API 토큰입니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="2단계: POST 요청 보내기" }

#### 기본 동작

CONTENT.

#### 사용량 제한

CONTENT.

## TOOL_NAME 커스터마이징
<!-- 추가 커스터마이징 단계를 설명하는 데 사용할 수 있는 선택 섹션입니다. 간결하게 작성하고 최소한의 필요한 단계만 설명하는 것이 중요합니다. -->

### 1단계: ACTION_TO_COMPLETE

CONTENT.

### 2단계: ACTION_TO_COMPLETE

CONTENT.

## Braze에서 TOOL_NAME 사용하기 / USE_CASE
<!-- Braze와 통합을 사용하는 방법을 설명하는 섹션입니다. 예를 들어, Braze로 전송된 데이터에 접근하는 방법, Braze 메시징과 통합을 활용하는 방법, 또는 "사용 사례" 섹션의 특정 사용 사례를 완료하는 방법 등을 설명합니다. -->

### 1단계: ACTION_TO_COMPLETE

CONTENT.

### 2단계: ACTION_TO_COMPLETE

CONTENT.

## 고려 사항
<!-- 사용자가 통합과 상호작용하는 방식에 영향을 줄 수 있는 추가 정보를 나열하는 선택 섹션입니다. -->

### CONSIDERATION_ITEM

CONTENT.

## 문제 해결
<!-- 통합을 설정하는 동안 발생할 수 있는 문제를 안내하는 선택 섹션입니다. 하이퍼링크를 사용하여 사용자를 설명서 사이트로 안내할 수도 있습니다. -->

### TROUBLESHOOTING_ITEM

CONTENT.
`````
{% endraw %}
{% enddetails %}