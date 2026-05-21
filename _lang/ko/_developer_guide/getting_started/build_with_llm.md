---
nav_title: LLM으로 구축하기
article_title: LLM을 활용한 구축
page_order: 4
description: "Braze 설명서와 함께 AI 코딩 어시스턴트를 사용하여 SDK 통합 워크플로우를 가속화하는 방법을 알아보세요."
platform:
  - Web
  - React Native
---

# LLM을 활용한 구축 {#building-with-an-llm}

> AI 코딩 어시스턴트를 활용하여 Braze 통합 워크플로우를 가속화하세요. Context7을 통해 IDE를 Braze Docs MCP 서버에 연결하고, 개발 환경에서 정확하고 최신의 SDK 가이드를 직접 확인하세요.

AI 코딩 어시스턴트는 통합 코드 작성, 문제 해결, Braze SDK 기능 탐색을 도와줄 수 있지만, 올바른 컨텍스트가 제공될 때에만 가능합니다. Braze Docs MCP 서버는 AI 어시스턴트에 Braze 설명서에 대한 직접 접근 권한을 제공하여, 최신 SDK 참조 자료를 기반으로 정확한 코드 스니펫을 생성하고 기술적 질문에 답변할 수 있도록 합니다.

## Braze Docs MCP에 연결하기 {#connecting-to-the-braze-docs-mcp}

[Context7](https://context7.com/braze-inc/braze-docs)은 AI 어시스턴트와 Braze 설명서 라이브러리 사이의 가교 역할을 합니다. IDE의 MCP 구성에 Context7을 추가하면 AI 어시스턴트가 전체 Braze 설명서를 쿼리하여 관련 SDK 참조 자료, 코드 예제 및 통합 가이드를 필요할 때마다 검색할 수 있습니다.

### Context7 설정하기 {#setting-up-context7}

Context7을 통해 AI 어시스턴트를 Braze Docs MCP에 연결하려면 IDE의 `mcp.json` 파일에 다음 구성을 추가하세요.

{% tabs %}
{% tab Cursor %}
[Cursor](https://cursor.com/)에서 **Settings** > **Tools and Integrations** > **MCP Tools** > **Add Custom MCP**로 이동한 후 다음 스니펫을 추가하세요:

```json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp@latest"]
    }
  }
}
```

구성을 저장하고 Cursor를 다시 시작하세요. 프롬프트에 `use context7`을 포함하면 AI 어시스턴트가 Context7을 통해 Braze 설명서에 접근할 수 있습니다.
{% endtab %}

{% tab Claude %}
Claude Desktop에서 **Settings** > **Developer** > **Edit Config**로 이동한 후, `claude_desktop_config.json` 파일에 다음 내용을 추가하세요:

```json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp@latest"]
    }
  }
}
```

구성을 저장하고 Claude Desktop을 다시 시작하세요.
{% endtab %}

{% tab VS Code %}
VS Code의 `settings.json` 또는 `.vscode/mcp.json` 파일에 다음 내용을 추가하세요:

```json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp@latest"]
    }
  }
}
```

구성을 저장하고 VS Code를 다시 시작하세요.
{% endtab %}
{% endtabs %}

{% alert note %}
Context7은 [Braze MCP 서버]({{site.baseurl}}/developer_guide/mcp_server/)와 다릅니다. Context7은 AI 어시스턴트에게 **Braze 설명서**에 대한 접근 권한을 제공하며, Braze MCP 서버는 Campaigns, Segments, 분석 등 **Braze 워크스페이스 데이터**에 대한 읽기 전용 접근 권한을 제공합니다. 두 가지를 함께 사용하면 보다 완벽한 AI 지원 개발 환경을 경험할 수 있습니다.
{% endalert %}

## Braze SDK 개발을 위한 프롬프트 작성하기 {#writing-prompts-for-braze-sdk-development}

Context7을 설정한 후, 프롬프트에 `use context7`을 포함하여 AI 어시스턴트가 Braze 설명서를 컨텍스트로 가져오도록 지시하세요. 다음 예시는 일반적인 SDK 작업에 효과적인 프롬프트를 작성하는 방법을 보여줍니다.

### React Native SDK {#react-native-sdk}

이 프롬프트는 [Braze React Native SDK]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=react%20native)의 일반적인 통합 작업을 보여줍니다.

#### SDK 초기화 {#initializing-the-sdk}

```text
Using the Braze React Native SDK, show me how to initialize the SDK
in my App.tsx with an API key and custom endpoint. Include the
configuration for automatic session tracking. Use context7.
```

#### 속성을 포함한 커스텀 이벤트 로깅 {#logging-custom-events-with-properties}

```text
I need to track user activity in my React Native app using the Braze
React Native SDK. Show me how to log a custom event called
"ProductViewed" with properties for product_id, category, and price.
Use context7.
```

#### 푸시 알림 설정 {#setting-up-push-notifications}

```text
Using the Braze React Native SDK, walk me through requesting push
notification permissions on both iOS and Android 13+. Include the
code for registering the push token with Braze. Use context7.
```

#### 인앱 메시지 처리 {#handling-in-app-messages}

```text
Show me how to subscribe to in-app messages using the Braze React
Native SDK, including how to log impressions and button clicks
programmatically. Use context7.
```

### 웹 SDK {#web-sdk}

이 프롬프트는 [Braze 웹 SDK]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web)의 일반적인 통합 작업을 보여줍니다.

#### SDK 초기화

```text
Using the Braze Web SDK, show me how to initialize the SDK with
braze.initialize(), including the API key, base URL, and options
for enabling logging and automatic in-app message display.
Use context7.
```

#### 커스텀 이벤트 및 구매 추적 {#tracking-custom-events-and-purchases}

```text
Using the Braze Web SDK, create a JavaScript module that logs a
custom event called "VideoPlayed" with properties for video_id,
duration_seconds, and completion_percentage. Also show how to log
a purchase with product ID, price, currency code, and quantity.
Use context7.
```

#### 웹 푸시 등록 {#registering-for-web-push}

```text
Using the Braze Web SDK, provide the HTML and JavaScript needed to
register a user for web push notifications after they click a
"Subscribe to updates" button. Include the service worker setup.
Use context7.
```

#### 사용자 속성 관리 {#managing-user-attributes}

```text
Using the Braze Web SDK, show me how to set standard user attributes
(first name, email, country) and custom user attributes (favorite_genre,
subscription_tier) for the current user. Use context7.
```

## 일반 텍스트 설명서 {#plain-text-documentation}

Braze 개발자 가이드 설명서를 AI 도구 및 LLM에 최적화된 일반 텍스트 파일로 이용할 수 있습니다. 이 파일들은 HTML 렌더링의 부담 없이 AI 어시스턴트가 구문 분석하고 이해할 수 있는 형식으로 Braze 설명서를 제공합니다.

| 파일 | 설명 |
|------|-------------|
| [llms.txt](https://www.braze.com/docs/developer_guide/llms.txt) | 제목과 설명이 포함된 Braze 개발자 설명서 페이지 색인입니다. 사용 가능한 설명서를 찾기 위한 출발점으로 활용하세요. |
| [llms-full.txt](https://www.braze.com/docs/developer_guide/llms-full.txt) | LLM이 소비할 수 있도록 포맷팅된 단일 일반 텍스트 파일로 제공되는 완전한 Braze 개발자 설명서입니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Plain text documentation" }

이 파일들은 AI 도구가 설명서에 접근할 수 있도록 하는 새로운 표준인 [llms.txt 표준](https://llmstxt.org/)을 따릅니다. 프롬프트에서 이 파일들을 직접 참조하거나, 내용을 LLM에 붙여넣어 컨텍스트로 활용할 수 있습니다.