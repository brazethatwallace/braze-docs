---
nav_title: Construa com um LLM
article_title: Construindo com um LLM
page_order: 4
description: "Aprenda a usar assistentes de codificação com IA junto à documentação da Braze para acelerar seu fluxo de trabalho de integração de SDK."
platform:
  - Web
  - React Native
---

# Construindo com um LLM {#building-with-an-llm}

> Use assistentes de codificação com IA para acelerar seu fluxo de trabalho de integração com a Braze. Conecte seu IDE ao servidor MCP da documentação da Braze por meio do Context7 e obtenha orientações precisas e atualizadas sobre SDK diretamente no seu ambiente de desenvolvimento.

Assistentes de codificação com IA podem ajudar você a escrever código de integração, solucionar problemas e explorar recursos do SDK da Braze&#8212;mas apenas se tiverem o contexto correto. O servidor MCP da documentação da Braze fornece ao seu assistente de IA acesso direto à documentação da Braze, para que ele possa gerar trechos de código precisos e responder a perguntas técnicas com base nas referências mais recentes do SDK.

## Conectando-se ao MCP da documentação da Braze {#connecting-to-the-braze-docs-mcp}

O [Context7](https://context7.com/braze-inc/braze-docs) serve como a ponte entre seu assistente de IA e a biblioteca de documentação da Braze. Ao adicionar o Context7 à configuração MCP do seu IDE, seu assistente de IA pode consultar todo o conjunto de documentação da Braze e recuperar referências relevantes de SDK, exemplos de código e guias de integração sob demanda.

### Configurando o Context7 {#setting-up-context7}

Para conectar seu assistente de IA ao MCP da documentação da Braze por meio do Context7, adicione a seguinte configuração ao arquivo `mcp.json` do seu IDE.

{% tabs %}
{% tab Cursor %}
No [Cursor](https://cursor.com/), acesse **Settings** > **Tools and Integrations** > **MCP Tools** > **Add Custom MCP** e adicione o seguinte trecho:

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

Salve a configuração e reinicie o Cursor. Seu assistente de IA agora pode acessar a documentação da Braze por meio do Context7 quando você incluir `use context7` nos seus prompts.
{% endtab %}

{% tab Claude %}
No Claude Desktop, acesse **Settings** > **Developer** > **Edit Config** e adicione o seguinte ao seu arquivo `claude_desktop_config.json`:

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

Salve a configuração e reinicie o Claude Desktop.
{% endtab %}

{% tab VS Code %}
Adicione o seguinte ao seu arquivo `settings.json` ou `.vscode/mcp.json` do VS Code:

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

Salve a configuração e reinicie o VS Code.
{% endtab %}
{% endtabs %}

{% alert note %}
O Context7 é diferente do [servidor MCP da Braze]({{site.baseurl}}/developer_guide/mcp_server/). O Context7 fornece ao seu assistente de IA acesso à **documentação da Braze**, enquanto o servidor MCP da Braze fornece acesso somente leitura aos **dados do seu espaço de trabalho na Braze** (como Campaigns, Segments e análise de dados). Você pode usar ambos juntos para uma experiência de desenvolvimento assistida por IA mais completa.
{% endalert %}

## Escrevendo prompts para o desenvolvimento com o SDK da Braze {#writing-prompts-for-braze-sdk-development}

Depois de configurar o Context7, inclua `use context7` nos seus prompts para sinalizar ao seu assistente de IA que ele deve buscar a documentação da Braze como contexto. Os exemplos a seguir mostram como escrever prompts eficazes para tarefas comuns do SDK.

### SDK do React Native {#react-native-sdk}

Esses prompts demonstram tarefas comuns de integração para o [SDK React Native da Braze]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=react%20native).

#### Inicializando o SDK {#initializing-the-sdk}

```text
Using the Braze React Native SDK, show me how to initialize the SDK
in my App.tsx with an API key and custom endpoint. Include the
configuration for automatic session tracking. Use context7.
```

#### Registrando eventos personalizados com propriedades {#logging-custom-events-with-properties}

```text
I need to track user activity in my React Native app using the Braze
React Native SDK. Show me how to log a custom event called
"ProductViewed" with properties for product_id, category, and price.
Use context7.
```

#### Configurando notificações por push {#setting-up-push-notifications}

```text
Using the Braze React Native SDK, walk me through requesting push
notification permissions on both iOS and Android 13+. Include the
code for registering the push token with Braze. Use context7.
```

#### Lidando com mensagens no app {#handling-in-app-messages}

```text
Show me how to subscribe to in-app messages using the Braze React
Native SDK, including how to log impressions and button clicks
programmatically. Use context7.
```

### SDK da Web {#web-sdk}

Esses prompts demonstram tarefas comuns de integração para o [SDK Web da Braze]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web).

#### Inicializando o SDK

```text
Using the Braze Web SDK, show me how to initialize the SDK with
braze.initialize(), including the API key, base URL, and options
for enabling logging and automatic in-app message display.
Use context7.
```

#### Rastreamento de eventos personalizados e compras {#tracking-custom-events-and-purchases}

```text
Using the Braze Web SDK, create a JavaScript module that logs a
custom event called "VideoPlayed" with properties for video_id,
duration_seconds, and completion_percentage. Also show how to log
a purchase with product ID, price, currency code, and quantity.
Use context7.
```

#### Registrando-se para push na web {#registering-for-web-push}

```text
Using the Braze Web SDK, provide the HTML and JavaScript needed to
register a user for web push notifications after they click a
"Subscribe to updates" button. Include the service worker setup.
Use context7.
```

#### Gerenciando atributos de usuário {#managing-user-attributes}

```text
Using the Braze Web SDK, show me how to set standard user attributes
(first name, email, country) and custom user attributes (favorite_genre,
subscription_tier) for the current user. Use context7.
```

## Documentação em texto simples {#plain-text-documentation}

Você pode acessar a documentação do Guia do Desenvolvedor da Braze como arquivos de texto simples otimizados para ferramentas de IA e LLMs. Esses arquivos fornecem a documentação da Braze em um formato que assistentes de IA podem analisar e entender sem a sobrecarga da renderização em HTML.

| Arquivo | Descrição |
|------|-------------|
| [llms.txt]({{site.baseurl}}/developer_guide/llms.txt) | Um índice das páginas de documentação do desenvolvedor da Braze com títulos e descrições. Use como ponto de partida para descobrir a documentação disponível. |
| [llms-full.txt]({{site.baseurl}}/developer_guide/llms-full.txt) | A documentação completa do desenvolvedor da Braze em um único arquivo de texto simples, formatado para consumo por LLMs. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Documentação em texto simples" }

Esses arquivos seguem o [padrão llms.txt](https://llmstxt.org/), uma convenção emergente para tornar a documentação acessível a ferramentas de IA. Você pode referenciar esses arquivos diretamente nos seus prompts ou colar o conteúdo deles em um LLM para contexto.