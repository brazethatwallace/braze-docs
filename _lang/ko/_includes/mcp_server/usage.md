# Braze MCP 서버 사용하기 {#using-the-braze-mcp-server}

> Claude 및 Cursor와 같은 자연어 도구를 사용하여 Braze 데이터와 상호작용하는 방법을 배우세요. 더 일반적인 정보는 [Braze MCP 서버]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/){% endif %}를 참조하세요.

{% multi_lang_include mcp_server/beta_alert.md %}

## 필수 조건 {#prerequisites}

이 기능을 사용하려면 먼저 [Braze MCP 서버 설정]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}을 완료해야 합니다.

## 모범 사례 {#best-practices}

Claude 및 Cursor와 같은 자연어 도구를 통해 Braze MCP 서버를 사용할 때 최상의 결과를 얻기 위해 다음 팁을 염두에 두세요:

- LLM은 실수를 할 수 있으므로 항상 답변을 다시 확인하세요.
- 데이터 분석 시 필요한 시간 범위를 명확히 지정하세요. 짧은 범위가 더 정확한 결과를 제공하는 경우가 많습니다.
- 정확한 [Braze 용어](https://www.braze.com/resources/articles/glossary)를 사용하여 LLM이 올바른 함수를 호출하도록 하세요.
- 결과가 불완전해 보이면 LLM에게 계속 진행하거나 더 깊이 파고들도록 요청하세요.
- 창의적인 프롬프트를 시도해 보세요! MCP 클라이언트에 따라 CSV 또는 기타 유용한 파일을 내보낼 수 있습니다.

## 사용 예시 {#usage-examples}

[Braze MCP 서버를 설정한 후]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}, Claude 또는 Cursor와 같은 도구를 사용하여 자연어로 Braze와 상호작용할 수 있습니다. 시작하는 데 도움이 되는 몇 가지 예시입니다:

### 내가 사용할 수 있는 Braze 함수는 무엇인가요? {#what-are-my-available-braze-functions}

{% tabs %}
{% tab Claude %}
**예시 프롬프트**

`What are my available Braze functions?`

**예시 응답**

`list_functions`를 사용하여 Braze MCP 서버를 확인한 결과 38개의 사용 가능한 API 함수를 찾았습니다.

다음은 카테고리별 몇 가지 예시입니다:

- **Campaign 분석 및 관리**
  - `get_campaign_dataseries`
  - `get_campaign_details`
  - `get_campaign_list`
- **Canvas 분석 및 관리**
  - `get_canvas_data_series`
  - `get_canvas_data_summary`
  - `get_canvas_list`
  - `get_canvas_details`
- **템플릿**
  - `create_email_template`
- **콘텐츠 블록**
  - `create_content_block`
  - `get_content_blocks`
  - `get_content_block_info`
  - `update_content_block`
{% endtab %}

{% tab Cursor %}
**예시 프롬프트**

`What are my available Braze functions?`

**예시 응답**

Braze MCP 서버를 사용하여 사용 가능한 함수를 확인하겠습니다.

- `list_functions` 호출 완료

결과에 따르면, 다음과 같은 카테고리로 구성된 38개의 Braze API 함수를 사용할 수 있습니다:

- Campaign 분석 및 관리
- Canvas 분석 및 관리
- 템플릿
- 콘텐츠 블록

예시 함수:

- `get_campaign_list`
- `get_canvas_list`
- `get_canvas_details`
- `create_email_template`
- `update_content_block`
{% endtab %}
{% endtabs %}

`list_functions` 함수에 대한 자세한 내용은 [사용 가능한 API 함수]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#general-functions){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#general-functions){% endif %}를 참조하세요.

### Canvas ID에 대한 세부 정보 가져오기 {#get-details-about-a-canvas-id}

{% tabs %}
{% tab Claude %}
**예시 프롬프트**

`Get details about canvas ID YOUR-TEST-CANVAS-ID-123`

**예시 응답**

`get_canvas_details`를 사용하여 `YOUR-TEST-CANVAS-ID-123`의 세부 정보를 가져왔습니다.

- **Canvas 이름:** `YOUR-TEST-CANVAS-NAME`
- **ID:** `YOUR-TEST-CANVAS-ID-123`
- **상태:** 초안 (활성화되지 않음)
- **생성일:** 2026년 1월 15일 오전 10:30 UTC
- **마지막 업데이트:** 2026년 1월 16일 오후 02:45 UTC
- **스케줄 유형:** 시간 기반
- **기본 채널:** 이메일

이메일 메시지 세부 정보:

- **제목:** `YOUR-TEST-SUBJECT-LINE`
- **발신자:** `YOUR-TEST-SENDER@example.com`
- **메시지 ID:** `YOUR-TEST-MESSAGE-ID-123`
{% endtab %}

{% tab Cursor %}
**예시 프롬프트**

`Get details about canvas ID YOUR-TEST-CANVAS-ID-123`

**예시 응답**

`get_canvas_details`를 사용하여 이 Canvas를 가져왔습니다:

- **Canvas ID:** `YOUR-TEST-CANVAS-ID-123`
- **Canvas 이름:** `YOUR-TEST-CANVAS-NAME`
- **상태:** 초안
- **채널:** 이메일
- **메시지 ID:** `YOUR-TEST-MESSAGE-ID-123`

이메일 콘텐츠 요약:

1. 브랜드 이미지가 포함된 헤더 섹션
2. 메인 헤드라인 섹션
3. CTA 버튼이 포함된 히어로 섹션
4. 보조 콘텐츠가 포함된 기능 섹션
{% endtab %}
{% endtabs %}

`get_canvas_details` 함수에 대한 자세한 내용은 [사용 가능한 API 함수]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#canvases){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#canvases){% endif %}를 참조하세요.

### 최근 Canvases 보기 {#show-me-my-recent-canvases}

{% tabs %}
{% tab Claude %}
**예시 프롬프트**

`Show me my recent Canvases`

**예시 응답**

`list_functions`로 사용 가능한 도구를 확인한 후 `get_canvas_list`를 사용하여 가장 최근에 편집된 Canvases를 가져왔습니다.

최근 Canvases:

1. **YOUR-TEST-CANVAS-ALPHA**
   - ID: `YOUR-TEST-ID-123`
   - 마지막 수정일: 2026년 1월 16일 오후 02:45 UTC
2. **YOUR-TEST-CANVAS-BETA**
   - ID: `YOUR-TEST-ID-456`
   - 마지막 수정일: 2026년 1월 15일 오전 11:10 UTC
3. **YOUR-TEST-CANVAS-GAMMA**
   - ID: `YOUR-TEST-ID-789`
   - 마지막 수정일: 2026년 1월 14일 오후 08:25 UTC
{% endtab %}

{% tab Cursor %}
**예시 프롬프트**

`Show me my recent Canvases`

**예시 응답**

Braze MCP 서버에서 최근 Canvas 목록을 가져오겠습니다.

- `list_functions` 호출 완료
- `get_canvas_list` 호출 완료

최근 Canvases (최근 편집순 정렬):

- **Canvas 이름:** `YOUR-TEST-CANVAS-ALPHA`
  - **마지막 수정일:** 2026년 1월 16일 오후 02:45 UTC
  - **Canvas ID:** `YOUR-TEST-ID-123`
  - **태그:** `lifecycle`, `email`
- **Canvas 이름:** `YOUR-TEST-CANVAS-BETA`
  - **마지막 수정일:** 2026년 1월 15일 오전 11:10 UTC
  - **Canvas ID:** `YOUR-TEST-ID-456`
  - **태그:** `promo`
{% endtab %}
{% endtabs %}

`get_canvas_list` 함수에 대한 자세한 내용은 [사용 가능한 API 함수]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#canvases){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#canvases){% endif %}를 참조하세요.

### 이메일 템플릿 생성하기 {#create-an-email-template}

{% tabs %}
{% tab Claude %}
**예시 프롬프트**

`Create an email template named "YOUR-TEST-TEMPLATE-NAME" for onboarding messages.`

**예시 응답**

`create_email_template`을 사용하여 템플릿을 생성했습니다.

- **템플릿 이름:** `YOUR-TEST-TEMPLATE-NAME`
- **템플릿 ID:** `YOUR-TEST-TEMPLATE-ID-123`
- **제목란:** `YOUR-TEST-SUBJECT-LINE`
- **프리헤더:** `YOUR-TEST-PREHEADER`
- **생성일:** 2026년 1월 16일 오후 03:10 UTC

이제 Campaigns 및 Canvases를 생성하거나 업데이트할 때 `YOUR-TEST-TEMPLATE-ID-123`을 참조할 수 있습니다.
{% endtab %}

{% tab Cursor %}
**예시 프롬프트**

`Create an email template named "YOUR-TEST-TEMPLATE-NAME" for onboarding messages.`

**예시 응답**

`create_email_template`을 사용하여 새 템플릿을 성공적으로 생성했습니다.

- **템플릿 ID:** `YOUR-TEST-TEMPLATE-ID-123`
- **템플릿 이름:** `YOUR-TEST-TEMPLATE-NAME`
- **제목:** `YOUR-TEST-SUBJECT-LINE`
- **설명:** `Onboarding lifecycle template`

원하시면 이 템플릿에 대한 기본 HTML 본문과 일반 텍스트 대체 콘텐츠도 생성할 수 있습니다.
{% endtab %}
{% endtabs %}

`create_email_template` 함수에 대한 자세한 내용은 [사용 가능한 API 함수]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#templates){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#templates){% endif %}를 참조하세요.

### 콘텐츠 블록 업데이트하기 {#update-a-content-block}

{% tabs %}
{% tab Claude %}
**예시 프롬프트**

`Update content block "YOUR-TEST-CONTENT-BLOCK-ID-123" with new body copy for our spring promotion.`

**예시 응답**

`update_content_block`을 사용하여 콘텐츠 블록을 업데이트했습니다.

- **콘텐츠 블록 ID:** `YOUR-TEST-CONTENT-BLOCK-ID-123`
- **이름:** `YOUR-TEST-CONTENT-BLOCK-NAME`
- **상태:** 업데이트됨
- **업데이트 일시:** 2026년 1월 16일 오후 03:25 UTC

미리보기:

`YOUR-TEST-CONTENT-BLOCK-BODY-V2`
{% endtab %}

{% tab Cursor %}
**예시 프롬프트**

`Update content block "YOUR-TEST-CONTENT-BLOCK-ID-123" with new body copy for our spring promotion.`

**예시 응답**

`update_content_block`을 실행하여 업데이트가 완료되었음을 확인했습니다.

- **콘텐츠 블록 ID:** `YOUR-TEST-CONTENT-BLOCK-ID-123`
- **이전 버전:** `v1`
- **현재 버전:** `v2`
- **마지막 업데이트:** 2026년 1월 16일 오후 03:25 UTC

업데이트된 콘텐츠 미리보기:

`YOUR-TEST-CONTENT-BLOCK-BODY-V2`
{% endtab %}
{% endtabs %}

`update_content_block` 함수에 대한 자세한 내용은 [사용 가능한 API 함수]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#content-blocks){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#content-blocks){% endif %}를 참조하세요.

{% multi_lang_include mcp_server/legal_disclaimer.md %}