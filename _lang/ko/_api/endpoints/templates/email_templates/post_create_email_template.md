---
nav_title: "POST: 이메일 템플릿 생성"
article_title: "POST: 이메일 템플릿 생성"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "이 문서에서는 이메일 템플릿 생성 Braze 엔드포인트에 대한 자세한 내용을 설명합니다."
---
{% api %}
# 이메일 템플릿 생성 {#create-email-template}
{% apimethod post %}
/templates/email/create
{% endapimethod %}

> 이 엔드포인트를 사용하여 Braze 대시보드에서 이메일 템플릿을 생성할 수 있습니다.

이 템플릿은 **템플릿 및 미디어** 페이지에서 사용할 수 있습니다. 이 엔드포인트의 응답에는 후속 API 호출에서 템플릿을 업데이트하는 데 사용할 수 있는 `email_template_id` 필드가 포함됩니다.

{% alert tip %}
[Braze MCP 서버]({{site.baseurl}}/user_guide/brazeai/mcp_server)를 통해 [`create_email_template`]({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions#templates) 함수를 사용하여 이 엔드포인트를 호출할 수도 있습니다. 이를 통해 Claude 및 Cursor와 같은 AI 도구가 자연어 프롬프트를 사용하여 이메일 템플릿을 생성할 수 있습니다.
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5eb1fe0d-2795-474d-aaf2-c4e2977dc94b {% endapiref %}

## 필수 조건 {#prerequisites}
이 엔드포인트를 사용하려면 `templates.email.create` 권한이 있는 [API 키]({{site.baseurl}}/api/api_key)가 필요합니다.

## 사용량 제한 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## 요청 본문 {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
   "template_name": (required, string) The name of your email template,
   "subject": (required, string) The email template subject line,
   "body": (required, string) The email template body that may include HTML,
   "plaintext_body": (optional, string) A plaintext version of the email template body,
   "preheader": (optional, string) The email preheader used to generate previews in some clients,
   "tags": (optional, Array of Strings) Tags must already exist,
   "should_inline_css": (optional, Boolean) If `true`, the `inline_css` feature is used on this template.
 }
```

## 요청 매개변수 {#request-parameters}

| 매개변수 | 필수 | 데이터 유형 | 설명 |
| --------- | ---------| --------- | ----------- |
| `template_name` | 필수 | 문자열 | 이메일 템플릿의 이름입니다. |
| `subject` | 필수 | 문자열 | 이메일 템플릿 제목란입니다. |
| `body` | 필수 | 문자열 | HTML을 포함할 수 있는 이메일 템플릿 본문입니다. 최대 400&nbsp;KB. |
| `plaintext_body` | 선택 사항 | 문자열 | 이메일 템플릿 본문의 일반 텍스트 버전입니다. |
| `preheader` | 선택 사항 | 문자열 | 일부 클라이언트에서 미리보기를 생성하는 데 사용되는 이메일 프리헤더입니다. |
| `tags` | 선택 사항 | 문자열 | [태그]({{site.baseurl}}/user_guide/messaging/governance/tags)가 이미 존재해야 합니다. |
| `should_inline_css` | 선택 사항 | 부울 | 템플릿별로 `inline_css` 기능을 활성화하거나 비활성화합니다. 제공하지 않으면 Braze는 앱 그룹의 기본값 설정을 사용합니다. `true` 또는 `false` 중 하나가 예상됩니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="요청 매개변수" }

## 요청 예시 {#example-request}
```
curl --location --request POST 'https://rest.iad-01.braze.com/templates/email/create' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "template_name": "email_template_name",
  "subject": "Welcome to my email template!",
  "body": "This is the text within my email body and https://www.braze.com/ here is a link to Braze.com.",
  "plaintext_body": "This is the text within my email body and here is a link to https://www.braze.com/.",
  "preheader": "My preheader is pretty cool.",
  "tags": ["Tag1", "Tag2"]
}'
```

## 응답 예시 {#example-response}

```json
{
  "email_template_id": "232b6d29-7e41-4106-a0ab-1c4fe915d701",
  "message": "success"
}
```

## 문제 해결 {#troubleshooting}

다음 표에는 반환될 수 있는 오류와 관련 문제 해결 단계가 나와 있습니다.

| 오류 | 문제 해결 |
| --- | --- |
| 템플릿 이름은 필수 항목입니다 | 템플릿 이름을 입력하세요. |
| 태그는 배열이어야 합니다 | 태그는 문자열 배열 형식이어야 합니다(예: `["marketing", "promotional", "transactional"]`). |
| 모든 태그는 문자열이어야 합니다 | 태그가 따옴표(`""`)로 묶여 있는지 확인하세요. |
| 일부 태그를 찾을 수 없습니다 | 이메일 템플릿을 생성할 때 태그를 추가하려면 해당 태그가 이미 Braze에 존재해야 합니다. |
| 이메일에 유효한 Content Blocks 이름이 있어야 합니다 | 이메일에 이 환경에 존재하지 않는 Content Blocks가 포함되어 있을 수 있습니다. |
| `should_inline_css`에 대한 잘못된 값입니다. `true` 또는 `false` 중 하나가 예상되었습니다. | 이 매개변수는 부울 값(true 또는 false)만 허용합니다. `should_inline_css` 값이 따옴표(`""`)로 묶이지 않았는지 확인하세요. 따옴표로 묶으면 값이 문자열로 전송됩니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="문제 해결" }

{% endapi %}