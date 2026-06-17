# Usando o servidor MCP do Braze {#using-the-braze-mcp-server}

> Aprenda a interagir com seus dados da Braze por meio de linguagem natural usando ferramentas como Claude e Cursor. Para saber mais, consulte [Servidor MCP do Braze]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/){% endif %}.

{% multi_lang_include mcp_server/beta_alert.md %}

## Pré-requisitos {#prerequisites}

Antes de poder usar esse recurso, você precisará [configurar o servidor MCP do Braze]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}.

## Melhores práticas {#best-practices}

Ao usar o servidor MCP do Braze por meio de ferramentas de linguagem natural como Claude e Cursor, lembre-se destas dicas para obter os melhores resultados:

- Os LLMs podem cometer erros, portanto, certifique-se sempre de verificar as respostas.
- Para análise de dados, seja claro quanto ao intervalo de tempo necessário. Intervalos mais curtos geralmente fornecem resultados mais precisos.
- Use a [terminologia exata da Braze](https://www.braze.com/resources/articles/glossary) para que seu LLM chame a função correta.
- Se os resultados parecerem incompletos, solicite ao seu LLM que continue ou aprofunde a pesquisa.
- Experimente prompts criativos! Dependendo do seu cliente MCP, você poderá exportar um CSV ou outros arquivos úteis.

## Exemplos de uso {#usage-examples}

Após [configurar o servidor MCP do Braze]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}, você pode interagir com a Braze por meio de linguagem natural usando ferramentas como Claude ou Cursor. Aqui estão alguns exemplos para você começar:

### Quais são as minhas funções disponíveis da Braze? {#what-are-my-available-braze-functions}

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

Para saber mais sobre a função `list_functions`, consulte [Funções de API disponíveis]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#general-functions){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#general-functions){% endif %}.

### Obter detalhes sobre um ID de Canvas {#get-details-about-a-canvas-id}

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

Para saber mais sobre a função `get_canvas_details`, consulte [Funções de API disponíveis]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#canvases){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#canvases){% endif %}.

### Mostre meus Canvas recentes {#show-me-my-recent-canvases}

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

Para saber mais sobre a função `get_canvas_list`, consulte [Funções de API disponíveis]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#canvases){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#canvases){% endif %}.

### Criar um modelo de e-mail {#create-an-email-template}

{% tabs %}
{% tab Cursor %}
**Example prompt:** `Create an email template named "YOUR-TEST-TEMPLATE-NAME".`

**Example response:** Created a template via `create_email_template` and returned `YOUR-TEST-TEMPLATE-ID-123`.
{% endtab %}
{% endtabs %}

Para saber mais sobre a função `create_email_template`, consulte [Funções de API disponíveis]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#templates){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#templates){% endif %}.

### Atualizar um bloco de conteúdo {#update-a-content-block}

{% tabs %}
{% tab Cursor %}
**Example prompt:** `Update content block "YOUR-TEST-CONTENT-BLOCK-ID-123".`

**Example response:** Updated the block with `update_content_block` and confirmed `YOUR-TEST-CONTENT-BLOCK-ID-123` moved to a new version.
{% endtab %}
{% endtabs %}

Para saber mais sobre a função `update_content_block`, consulte [Funções de API disponíveis]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#content-blocks){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#content-blocks){% endif %}.

{% multi_lang_include mcp_server/legal_disclaimer.md %}