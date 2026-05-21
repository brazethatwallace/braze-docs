# Braze MCP 서버를 설정하세요 {#setting-up-the-braze-mcp-server}

> Claude 및 Cursor와 같은 자연어 도구를 사용하여 Braze 데이터와 상호작용할 수 있도록 Braze MCP 서버를 설정하는 방법을 알아보세요. 더 일반적인 정보는 [Braze MCP 서버]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/){% endif %}를 참조하세요.

{% multi_lang_include mcp_server/beta_alert.md %}

## 필수 조건 {#prerequisites}

시작하기 전에 다음이 필요합니다:

| 필수 조건 | 설명 |
|--------------|-------------|
| Braze API 키 | 필요한 권한이 있는 Braze API 키입니다. [Braze MCP 서버를 설정](#create-api-key)할 때 새 키를 생성합니다. |
| MCP 클라이언트 | [Claude](https://claude.ai/), [Cursor](https://cursor.com/), [Google Gemini CLI](https://docs.cloud.google.com/gemini/docs/codeassist/gemini-cli)가 공식적으로 지원됩니다. Braze MCP 서버를 사용하려면 이러한 클라이언트 중 하나에 대한 계정이 있어야 합니다. |
| 터미널 | 명령을 실행하고 도구를 설치할 수 있는 터미널 앱입니다. 선호하는 터미널 앱이나 컴퓨터에 미리 설치된 앱을 사용하세요. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Braze MCP 서버 설정하기

### 1단계: `uv` 설치하기 {#step-1-install-uv}

먼저 `uv`&#8212;의존성 관리 및 Python 패키지 처리를 위한 [Astral의 명령줄 도구](https://docs.astral.sh/uv/getting-started/installation/)를 설치하세요.

{% tabs local %}
{% tab MacOS and Linux %}
터미널 애플리케이션을 열고, 다음 명령을 붙여넣은 후 <kbd>Enter</kbd>를 누르세요.

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

출력은 다음과 유사합니다:

```bash
$ curl -LsSf https://astral.sh/uv/install.sh | sh

downloading uv 0.8.9 aarch64-apple-darwin
no checksums to verify
installing to /Users/Isaiah.Robinson/.local/bin
  uv
  uvx
everything's installed!
```
{% endtab %}

{% tab Windows %}
 Windows PowerShell을 열고, 다음 명령을 붙여넣은 후 <kbd>Enter</kbd>를 누르세요.

```powershell
irm https://astral.sh/uv/install.ps1 | iex
```

출력은 다음과 유사합니다:

```powershell
PS C:\Users\YourUser> irm https://astral.sh/uv/install.ps1 | iex

Downloading uv 0.8.9 (x86_64-pc-windows-msvc)
no checksums to verify
installing to C:\Users\YourUser\.local\bin
  uv.exe
  uvx.exe
everything's installed!
```
{% endtab %}
{% endtabs %}

### 2단계: API 키 생성 {#create-api-key}

Braze MCP 서버에는 읽기 전용 엔드포인트와 쓰기 엔드포인트가 모두 포함되어 있습니다. Braze 고객 프로필에서 데이터를 반환하지는 않습니다. 쓰기 엔드포인트를 사용하면 에이전트가 워크스페이스에서 콘텐츠를 생성하거나 업데이트할 수 있습니다.

API 키를 생성하려면:

1. **설정** > **API 키** > **API 키**로 이동합니다.
2. 새 키를 생성합니다.
3. 키에 다음 권한 중 일부 또는 전부를 할당합니다.

{% alert important %}
에이전트가 사용하기를 원하는 권한만 할당하세요. 에이전트가 Braze에서 변경 작업을 수행하지 못하도록 하려면 API 키를 생성할 때 쓰기 권한을 모두 제외하세요.
{% endalert %}

{% details 지원되는 권한 목록 %}
#### Campaigns

| 엔드포인트 | 필수 권한 |
|----------|---------------------|
| [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/) | `campaigns.data_series` |
| [`/campaigns/details`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details/) | `campaigns.details` |
| [`/campaigns/list`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns/) | `campaigns.list` |
| [`/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics/) | `sends.data_series` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Campaigns" }

#### Canvas

| 엔드포인트 | 필수 권한 |
|----------|---------------------|
| [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics/) | `canvas.data_series` |
| [`/canvas/data_summary`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary/) | `canvas.data_summary` |
| [`/canvas/details`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/) | `canvas.details` |
| [`/canvas/list`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases/) | `canvas.list` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Canvas" }

#### 카탈로그 {#catalogs}

| 엔드포인트 | 필수 권한 |
|----------|---------------------|
| [`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs/) | `catalogs.get` |
| [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk/) | `catalogs.get_items` |
| [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details/) | `catalogs.get_item` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Catalogs" }

#### 클라우드 데이터 수집 {#cloud-data-ingestion}

| 엔드포인트 | 필수 권한 |
|----------|---------------------|
| [`/cdi/integrations`]({{site.baseurl}}/api/endpoints/cdi/get_integration_list/) | `cdi.integration_list` |
| [`/cdi/integrations/{integration_id}/job_sync_status`]({{site.baseurl}}/api/endpoints/cdi/get_job_sync_status/) | `cdi.integration_job_status` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Cloud Data Ingestion" }

#### Content Blocks

`content_blocks.create` 및 `content_blocks.update` 권한은 쓰기 권한입니다. 에이전트가 워크스페이스에서 Content Blocks를 생성하거나 업데이트하도록 하려는 경우에만 추가하세요.

| 엔드포인트 | 필수 권한 |
|----------|---------------------|
| [`/content_blocks/list`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks/) | `content_blocks.list` |
| [`/content_blocks/info`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information/) | `content_blocks.info` |
| [`/content_blocks/create`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block/) | `content_blocks.create` |
| [`/content_blocks/update`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block/) | `content_blocks.update` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Content Blocks" }

#### 커스텀 속성 {#custom-attributes}

| 엔드포인트 | 필수 권한 |
|----------|---------------------|
| [`/custom_attributes`]({{site.baseurl}}/api/endpoints/export/custom_attributes/get_custom_attributes/) | `custom_attributes.get` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Custom Attributes" }

#### 이벤트 {#events}

| 엔드포인트 | 필수 권한 |
|----------|---------------------|
| [`/events/list`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events/) | `events.list` |
| [`/events/data_series`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_analytics/) | `events.data_series` |
| [`/events`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_data/) | `events.get` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Events" }

#### KPI {#kpis}

| 엔드포인트 | 필수 권한 |
|----------|---------------------|
| [`/kpi/new_users/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_daily_new_users_date/) | `kpi.new_users.data_series` |
| [`/kpi/dau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_dau_date/) | `kpi.dau.data_series` |
| [`/kpi/mau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_mau_30_days/) | `kpi.mau.data_series` |
| [`/kpi/uninstalls/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_uninstalls_date/) | `kpi.uninstalls.data_series` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="KPIs" }

#### 미디어 라이브러리 {#media-library}

`media_library.create` 권한은 쓰기 권한입니다. 에이전트가 미디어 라이브러리에 자산을 업로드하도록 하려는 경우에만 추가하세요.

| 엔드포인트 | 필수 권한 |
|----------|---------------------|
| [`/media_library/create`]({{site.baseurl}}/api/endpoints/media_library/manage_assets/create/) | `media_library.create` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Media Library" }

#### 메시지 {#messages}

| 엔드포인트 | 필수 권한 |
|----------|---------------------|
| [`/messages/scheduled_broadcasts`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/get_messages_scheduled/) | `messages.schedule_broadcasts` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Messages" }

#### 환경설정 센터 {#preference-center}

| 엔드포인트 | 필수 권한 |
|----------|---------------------|
| [`/preference_center/v1/list`]({{site.baseurl}}/api/endpoints/preference_center/get_list_preference_center/) | `preference_center.list` |
| [`/preference_center/v1/{preferenceCenterExternalID}`]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center/) | `preference_center.get` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Preference Center" }

#### 구매 {#purchases}

| 엔드포인트 | 필수 권한 |
|----------|---------------------|
| [`/purchases/product_list`]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id/) | `purchases.product_list` |
| [`/purchases/revenue_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_revenue_series/) | `purchases.revenue_series` |
| [`/purchases/quantity_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_number_of_purchases/) | `purchases.quantity_series` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Purchases" }

#### Segments

| 엔드포인트 | 필수 권한 |
|----------|---------------------|
| [`/segments/list`]({{site.baseurl}}/api/endpoints/export/segments/get_segment/) | `segments.list` |
| [`/segments/data_series`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics/) | `segments.data_series` |
| [`/segments/details`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details/) | `segments.details` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Segments" }

#### 발송 {#sends}

| 엔드포인트 | 필수 권한 |
|----------|---------------------|
| [`/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics/) | `sends.data_series` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Sends" }

#### 세션 {#sessions}

| 엔드포인트 | 필수 권한 |
|----------|---------------------|
| [`/sessions/data_series`]({{site.baseurl}}/api/endpoints/export/sessions/get_sessions_analytics/) | `sessions.data_series` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Sessions" }

#### SDK 인증 키 {#sdk-authentication-keys}

| 엔드포인트 | 필수 권한 |
|----------|---------------------|
| [`/app_group/sdk_authentication/keys`]({{site.baseurl}}/api/endpoints/sdk_authentication/get_sdk_authentication_keys/) | `sdk_authentication.keys` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="SDK Authentication Keys" }

#### 구독 {#subscription}

| 엔드포인트 | 필수 권한 |
|----------|---------------------|
| [`/subscription/status/get`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/) | `subscription.status.get` |
| [`/subscription/user/status`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups/) | `subscription.groups.get` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Subscription" }

#### 템플릿 {#templates}

`templates.email.create` 및 `templates.email.update` 권한은 쓰기 권한입니다. 에이전트가 워크스페이스에서 이메일 템플릿을 생성하거나 업데이트하도록 하려는 경우에만 추가하세요.

| 엔드포인트 | 필수 권한 |
|----------|---------------------|
| [`/templates/email/list`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates/) | `templates.email.list` |
| [`/templates/email/info`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_see_email_template_information/) | `templates.email.info` |
| [`/templates/email/create`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template/) | `templates.email.create` |
| [`/templates/email/update`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template/) | `templates.email.update` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Templates" }
{% enddetails %}

{% alert warning %}
기존 API 키를 재사용하지 마세요. MCP 클라이언트 전용으로 새 키를 생성하세요. 에이전트에 필요한 권한만 할당하세요. 에이전트는 부여된 모든 권한을 사용하려고 시도할 수 있으므로, 에이전트가 Braze에서 변경 작업을 수행하지 않기를 원한다면 쓰기 권한은 제외하세요.
{% endalert %}

### 3단계: 식별자 및 엔드포인트 가져오기 {#step-3-get-your-identifier-and-endpoint}

MCP 클라이언트를 구성할 때 API 키의 식별자와 워크스페이스의 REST 엔드포인트가 필요합니다. 이 세부 정보를 확인하려면 대시보드의 **API 키** 페이지로 돌아가세요&#8212;[다음 단계](#configure-client)에서 참조할 수 있도록 이 페이지를 열어 두세요.

![Braze의 API 키 페이지에서 새로 생성된 API 키와 사용자의 REST 엔드포인트를 보여줍니다.]({% image_buster /assets/img/mcp_server/get_indentifer_and_endpoint.png %}){: style="max-width:85%;"}

### 4단계: MCP 클라이언트 구성 {#configure-client}

미리 제공된 구성 파일을 사용하여 MCP 클라이언트를 구성하세요.

{% tabs %}
{% tab Claude %}
[Claude Desktop](https://claude.ai/download) 커넥터 디렉토리를 사용하여 MCP 서버를 설정하세요.

1. Claude Desktop에서 **Settings** > **Connectors** > **Browse Connectors** > **Desktop Extensions** > **Braze MCP Server** > **Install**로 이동합니다.
2. API 키와 기본 URL을 입력합니다.
3. 구성을 저장하고 Claude Desktop을 재시작합니다.

{% endtab %}

{% tab Cursor %}
[Cursor](https://cursor.com/)에서 **Settings** > **Tools and Integrations** > **MCP Tools** > **Add Custom MCP**로 이동한 다음 다음 스니펫을 추가하세요:

```json
{
  "mcpServers": {
    "braze": {
      "command": "uvx",
      "args": ["--native-tls", "braze-mcp-server@latest"],
      "env": {
        "BRAZE_API_KEY": "your-braze-api-key",
        "BRAZE_BASE_URL": "your-braze-endpoint-url"
      }
    }
  }
}
```

`key-identifier`와 `rest-endpoint`를 Braze의 **API 키** 페이지에서 해당 값으로 교체하세요. 구성은 다음과 유사해야 합니다:

```json
{
  "mcpServers": {
    "braze": {
      "command": "uvx",
      "args": ["--native-tls", "braze-mcp-server@latest"],
      "env": {
        "BRAZE_API_KEY": "2e8b-3c6c-d12e-bd75-4f0e2a8e5c71",
        "BRAZE_BASE_URL": "https://torchie.braze.com"
      }
    }
  }
}
```

완료되면 구성을 저장하고 Cursor를 재시작하세요.
{% endtab %}
{% tab Gemini CLI %}
Gemini CLI는 `~/.gemini/settings.json`에서 사용자 설정을 읽습니다. 이 파일이 존재하지 않으면 터미널에서 다음을 실행하여 생성할 수 있습니다:

```powershell
mkdir -p ~/.gemini
nano ~/.gemini/settings.json
```

다음으로, 터미널 프롬프트에서 `@BZXXXXXXXX` 앞의 정확한 문자열로 `yourname`을 교체하세요. 그런 다음 Braze의 **API 키** 페이지에서 해당 값으로 `key-identifier`와 `rest-endpoint`를 교체하세요.

구성은 다음과 유사해야 합니다:

```json
{
  "mcpServers": {
    "braze": {
      "command": "/Users/yourname/.local/bin/uvx",
      "args": ["--native-tls", "braze-mcp-server@latest"],
      "env": {
        "BRAZE_API_KEY": "2e8b-3c6c-d12e-bd75-4f0e2a8e5c71",
        "BRAZE_BASE_URL": "https://torchie.braze.com"
      }
    }
  }
}
```

완료되면 구성을 저장하고 Gemini CLI를 재시작하세요. 그런 다음 Gemini에서 다음 명령을 실행하여 Braze MCP 서버가 나열되어 있고 도구와 스키마를 사용할 수 있는지 확인하세요:

```powershell
gemini
/mcp
/mcp desc
/mcp schema
```

사용 가능한 도구와 스키마가 있는 `braze` 서버가 나열되어야 합니다.

{% endtab %}
{% endtabs %}

### 5단계: 테스트 프롬프트 보내기 {#step-5-send-a-test-prompt}

Braze MCP 서버를 설정한 후 MCP 클라이언트에 테스트 프롬프트를 보내보세요. 다른 예제 및 모범 사례는 [Braze MCP 서버 사용하기]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/usage/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/usage/){% endif %}를 참조하세요.

{% tabs %}
{% tab Claude %}
![Claude에서 사용 가능한 Braze 기능이 무엇인지 질문하고 답변을 받는 모습입니다.]({% image_buster /assets/img/mcp_server/claude/what_are_my_available_braze_functions.png %}){: style="max-width:85%;"}
{% endtab %}

{% tab Cursor %}
![Cursor에서 사용 가능한 Braze 기능이 무엇인지 질문하고 답변을 받는 모습입니다.]({% image_buster /assets/img/mcp_server/cursor/what_are_my_available_braze_functions.png %})
{% endtab %}

{% tab Gemini CLI %}
![Gemini CLI에서 사용 가능한 Braze 기능이 무엇인지 질문하고 답변을 받는 모습입니다.]({% image_buster /assets/img/mcp_server/gemini_cli/what_are_my_available_braze_functions.png %})
{% endtab %}
{% endtabs %}

## 문제 해결 {#troubleshooting}

### 터미널 오류 {#terminal-errors}

#### `uvx` 명령을 찾을 수 없음 {#uvx-command-not-found}

`uvx` 명령을 찾을 수 없다는 오류가 발생하면 `uv`를 재설치하고 터미널을 재시작하세요.

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

#### `spawn uvx ENOENT` 오류 {#spawn-uvx-enoent-error}

`spawn uvx ENOENT` 오류가 발생하면 클라이언트의 구성 파일에서 파일 경로를 업데이트해야 할 수 있습니다. 먼저 터미널을 열고 다음 명령을 실행하세요:

```bash
which uvx
```

명령은 다음과 유사한 메시지를 반환해야 합니다:

```bash
/Users/alex-lee/.local/bin/uvx
```

메시지를 클립보드에 복사하고 [클라이언트의 구성 파일](#configure-client)을 여세요. `"command": "uvx"`를 복사한 경로로 교체한 후 클라이언트를 재시작하세요. 예를 들어:

```json
"command": "/Users/alex-lee/.local/bin/uvx"
```

#### 패키지 설치 실패 {#package-installation-fails}

패키지 설치가 실패하면 특정 Python 버전을 대신 설치해 보세요.

```bash
uvx --python 3.12 braze-mcp-server@latest
```

### 클라이언트 구성 {#client-configuration}

#### MCP 클라이언트가 Braze 서버를 찾을 수 없음 {#mcp-client-cant-find-the-braze-server}

1. MCP 클라이언트 구성 구문이 올바른지 확인하세요.
2. 구성 변경 후 MCP 클라이언트를 재시작하세요.
3. `uvx`가 시스템 `PATH`에 있는지 확인하세요.

#### 인증 오류 {#authentication-errors}

1. `BRAZE_API_KEY`가 올바르고 활성 상태인지 확인하세요.
2. `BRAZE_BASE_URL`이 Braze 인스턴스와 일치하는지 확인하세요.
3. API 키에 [올바른 권한](#create-api-key)이 있는지 확인하세요.

#### 연결 시간 초과 또는 네트워크 오류 {#connection-timeouts-or-network-errors}

1. `BRAZE_BASE_URL`이 인스턴스에 대해 올바른지 확인하세요.
2. 네트워크 연결 및 방화벽 설정을 확인하세요.
3. 기본 URL에서 HTTPS를 사용하고 있는지 확인하세요.

{% multi_lang_include mcp_server/legal_disclaimer.md %}