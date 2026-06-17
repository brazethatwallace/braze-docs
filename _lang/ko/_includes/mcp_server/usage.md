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
**Example prompt:** `What are my available Braze functions?`

**Example response:** Called `list_functions` and returned categories like Campaign, Canvas, Templates, and Content Blocks with sample functions such as `get_canvas_list` and `create_email_template`.
{% endtab %}

{% tab Cursor %}
**Example prompt:** `What are my available Braze functions?`

**Example response:** Queried `list_functions`, confirmed available function groups, and listed examples including `get_canvas_details` and `update_content_block`.
{% endtab %}
{% endtabs %}

`list_functions` 함수에 대한 자세한 내용은 [사용 가능한 API 함수]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#general-functions){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#general-functions){% endif %}를 참조하세요.

### Canvas ID에 대한 세부 정보 가져오기 {#get-details-about-a-canvas-id}

{% tabs %}
{% tab Claude %}
**Example prompt:** `Get details about canvas ID YOUR-TEST-CANVAS-ID-123`

**Example response:** Used `get_canvas_details` and returned sample metadata (status, channel, created/updated time) for `YOUR-TEST-CANVAS-ID-123`.
{% endtab %}

{% tab Cursor %}
**Example prompt:** `Get details about canvas ID YOUR-TEST-CANVAS-ID-123`

**Example response:** Returned Canvas and message details with dummy values like `YOUR-TEST-MESSAGE-ID-123` and `YOUR-TEST-SUBJECT-LINE`.
{% endtab %}
{% endtabs %}

`get_canvas_details` 함수에 대한 자세한 내용은 [사용 가능한 API 함수]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#canvases){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#canvases){% endif %}를 참조하세요.

### 내 최근 Canvases 보여주기 {#show-me-my-recent-canvases}

{% tabs %}
{% tab Claude %}
**Example prompt:** `Show me my recent Canvases`

**Example response:** Called `get_canvas_list` and returned recent items such as `YOUR-TEST-CANVAS-ALPHA` with IDs like `YOUR-TEST-ID-123`.
{% endtab %}

{% tab Cursor %}
**Example prompt:** `Show me my recent Canvases`

**Example response:** Listed recently edited Canvases with sample values for name, last edited time, ID, and tags.
{% endtab %}
{% endtabs %}

`get_canvas_list` 함수에 대한 자세한 내용은 [사용 가능한 API 함수]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#canvases){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#canvases){% endif %}를 참조하세요.

### 이메일 템플릿 생성하기 {#create-an-email-template}

{% tabs %}
{% tab Cursor %}
**Example prompt:** `Create an email template named "YOUR-TEST-TEMPLATE-NAME".`

**Example response:** Created a template via `create_email_template` and returned `YOUR-TEST-TEMPLATE-ID-123`.
{% endtab %}
{% endtabs %}

`create_email_template` 함수에 대한 자세한 내용은 [사용 가능한 API 함수]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#templates){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#templates){% endif %}를 참조하세요.

### 콘텐츠 블록 업데이트하기 {#update-a-content-block}

{% tabs %}
{% tab Cursor %}
**Example prompt:** `Update content block "YOUR-TEST-CONTENT-BLOCK-ID-123".`

**Example response:** Updated the block with `update_content_block` and confirmed `YOUR-TEST-CONTENT-BLOCK-ID-123` moved to a new version.
{% endtab %}
{% endtabs %}

`update_content_block` 함수에 대한 자세한 내용은 [사용 가능한 API 함수]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#content-blocks){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#content-blocks){% endif %}를 참조하세요.

{% multi_lang_include mcp_server/legal_disclaimer.md %}