# Braze MCP 서버 사용하기 {#using-the-braze-mcp-server}

> 원격 Braze MCP 서버에 연결한 후 자연어를 통해 Braze 데이터와 상호작용하는 방법을 배우세요. 자세한 내용은 [Braze MCP 서버]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/){% endif %}를 참조하세요.

{% multi_lang_include mcp_server/beta_alert.md %}

## 필수 조건 {#prerequisites}

이 기능을 사용하려면 먼저 [Braze MCP 서버 설정]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}을 완료해야 합니다.

## 모범 사례 {#best-practices}

자연어 도구를 통해 Braze MCP 서버를 사용할 때 다음 팁을 염두에 두세요:

- 특히 여러 워크스페이스에 접근할 수 있는 경우, 프롬프트에서 워크스페이스를 확인하세요.
- 분석을 요청할 때 날짜 범위와 측정기준을 구체적으로 지정하세요.
- 결과를 검증할 때 에이전트에게 어떤 도구를 사용했는지 확인하도록 요청하세요.
- 영향이 큰 권장 사항은 Braze 대시보드의 소스 데이터와 비교하세요.

## 사용 예시 {#usage-examples}

[Braze MCP 서버를 설정한 후]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}, 자연어로 Braze와 상호작용할 수 있습니다. 시작하는 데 도움이 되는 몇 가지 예시입니다.

### 어떤 워크스페이스에 접근할 수 있나요? {#which-workspaces-can-i-access}

{% tabs %}
{% tab 예시 프롬프트 %}

`Show my available Braze workspaces and tell me which one to use for production campaign analytics.`
{% endtab %}
{% tab 예시 응답 %}

`get_workspaces`를 호출하여 다음 워크스페이스를 찾았습니다:

- `Marketing - Production` (`app_group_id`: `YOUR-APP-GROUP-ID-1`)
- `Marketing - Staging` (`app_group_id`: `YOUR-APP-GROUP-ID-2`)

프로덕션 Campaign 분석 프롬프트에는 `Marketing - Production`을 사용하세요.
{% endtab %}
{% endtabs %}

자세한 내용은 [사용 가능한 API 함수]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#workspaces){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#workspaces){% endif %}를 참조하세요.

### 지난주 Campaign 성과 보기 {#show-me-campaign-performance-for-last-week}

{% tabs %}
{% tab 예시 프롬프트 %}

`In the Marketing - Production workspace, show campaign performance for the last seven days, including sends, opens, clicks, and top performers.`
{% endtab %}
{% tab 예시 응답 %}

요청하신 워크스페이스와 날짜 범위에 대해 `get_campaign_list`와 `get_campaign_dataseries`를 사용했습니다.

요약:

- 총 발송 수: `YOUR-TEST-SENDS`
- 총 열람 수: `YOUR-TEST-OPENS`
- 총 클릭 수: `YOUR-TEST-CLICKS`
- 열람 기준 상위 Campaign: `YOUR-TEST-CAMPAIGN-NAME`

필요하시면 Campaign별, 채널별 또는 일별로 세분화할 수 있습니다.
{% endtab %}
{% endtabs %}

자세한 내용은 [사용 가능한 API 함수]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#campaigns){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#campaigns){% endif %}를 참조하세요.

### 이메일 템플릿 생성하기 {#create-an-email-template}

{% tabs %}
{% tab 예시 프롬프트 %}

`In the Marketing - Production workspace, create an onboarding email template named "YOUR-TEST-TEMPLATE-NAME".`
{% endtab %}
{% tab 예시 응답 %}

`create_email_template`을 사용하여 템플릿을 생성했습니다.

- **템플릿 ID:** `YOUR-TEST-TEMPLATE-ID-123`
- **템플릿 이름:** `YOUR-TEST-TEMPLATE-NAME`
- **워크스페이스:** `Marketing - Production`
{% endtab %}
{% endtabs %}

자세한 내용은 [사용 가능한 API 함수]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#templates){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#templates){% endif %}를 참조하세요.

## 예시 워크플로 {#example-workflows}

이 예시들은 여러 도구를 결합하여 작업을 처음부터 끝까지 완료합니다.

### 여러 워크스페이스에 걸친 보고서 {#report-across-multiple-workspaces}

{% tabs %}
{% tab 예시 프롬프트 %}

`Get me an analytics report for the past week from my US Prod workspace and my EU Prod workspace, and compare total sends and open rates.`
{% endtab %}
{% tab 예시 응답 %}

`get_workspaces`를 호출하여 접근 권한을 확인한 후, 지난 7일간 각 워크스페이스에 대해 `get_campaign_dataseries`를 실행했습니다.

- `US Prod`: `YOUR-TEST-SENDS` 발송, `YOUR-TEST-OPEN-RATE` 열람율
- `EU Prod`: `YOUR-TEST-SENDS` 발송, `YOUR-TEST-OPEN-RATE` 열람율

이번 주에는 `US Prod`에서 더 많은 메시지를 발송했고, `EU Prod`의 열람율이 더 높았습니다. 어느 워크스페이스든 Campaign별 또는 채널별로 세분화할 수 있습니다.
{% endtab %}
{% endtabs %}

### 스테이징에서 프로덕션으로 템플릿 복사하기 {#copy-templates-from-staging-to-production}

{% tabs %}
{% tab 예시 프롬프트 %}

`Copy the email templates from my Staging workspace to my Production workspace.`
{% endtab %}
{% tab 예시 응답 %}

`get_email_templates`와 `get_email_template_info`를 사용하여 `Staging`의 템플릿을 읽은 후, `create_email_template`으로 `Production`에 각 템플릿을 다시 생성했습니다.

- `YOUR-TEST-TEMPLATE-NAME-1`: `Production`에 생성됨 (`YOUR-TEST-TEMPLATE-ID-1`)
- `YOUR-TEST-TEMPLATE-NAME-2`: `Production`에 생성됨 (`YOUR-TEST-TEMPLATE-ID-2`)

`get_email_template_info`에서 지원하지 않는 드래그 앤 드롭 편집기 템플릿은 건너뛰었습니다. 복사된 템플릿을 검토하시겠습니까?
{% endtab %}
{% endtabs %}

### 주간 Campaign 상태 요약 {#summarize-weekly-campaign-health}

{% tabs %}
{% tab 예시 프롬프트 %}

`Give me a weekly campaign health summary for the Production workspace.`
{% endtab %}
{% tab 예시 응답 %}

`get_campaign_list`와 `get_campaign_dataseries`를 사용하여 `Production`의 지난 7일간 활동을 가져왔습니다.

- 총 발송 수: `YOUR-TEST-SENDS`
- 열람율: `YOUR-TEST-OPEN-RATE`
- 클릭률: `YOUR-TEST-CLICK-RATE`
- 전환 기준 상위 Campaign: `YOUR-TEST-CAMPAIGN-NAME`

발송 수가 전주 대비 증가했습니다. 채널별 세분화를 추가하거나 인게이지먼트가 감소하는 Campaign을 표시할 수 있습니다.
{% endtab %}
{% endtabs %}

## 원격 MCP 서버 작동 방식 {#how-the-remote-mcp-server-works}

요청을 보내면 백그라운드에서 몇 가지 단계가 진행됩니다:

1. **클라이언트에 프롬프트를 입력합니다.** 지난주 Campaign 성과를 요청하는 것과 같이 자연어로 요청을 입력합니다.
2. **클라이언트의 모델이 도구를 선택합니다.** 클라이언트의 AI 모델이 요청을 해석하고 `get_campaign_list` 및 `get_campaign_dataseries`와 같은 하나 이상의 Braze 도구 호출로 변환합니다.
3. **Braze가 도구 호출을 실행합니다.** 원격 MCP 서버가 인증된 OAuth 세션을 통해 각 도구 호출을 수신하고, 지정한 워크스페이스를 적용한 후 해당하는 Braze REST API 엔드포인트에 대해 실행합니다.
4. **Braze가 결과를 반환합니다.** 서버가 데이터를 클라이언트로 다시 전송하고, 클라이언트가 이를 포맷하여 사용자에게 표시합니다.

접근 권한은 두 가지의 교집합입니다:

- **연결을 승인할 때 부여된 범위**, 예를 들어 `mcp:tools`.
- **사용자 본인의 대시보드 권한.** 대시보드에서 Campaign을 볼 수 없다면 에이전트도 볼 수 없습니다. 이메일 템플릿을 생성할 수 있다면 에이전트도 생성할 수 있습니다. 에이전트는 사용자 본인의 접근 권한을 초과할 수 없습니다.

워크스페이스 컨텍스트는 로컬 설정 파일에 저장되지 않고 각 요청과 함께 전달되므로, 하나의 연결로 접근 권한이 있는 모든 워크스페이스에서 작업할 수 있습니다.

{% multi_lang_include mcp_server/legal_disclaimer.md %}