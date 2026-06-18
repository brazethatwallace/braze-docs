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
!["Quais são as minhas funções disponíveis da Braze?" sendo perguntado e respondido no Claude.]({% image_buster /assets/img/mcp_server/claude/what_are_my_available_braze_functions.png %}){: style="max-width:85%;"}
{% endtab %}

{% tab Cursor %}
!["Quais são as minhas funções disponíveis da Braze?" sendo perguntado e respondido no Cursor.]({% image_buster /assets/img/mcp_server/cursor/what_are_my_available_braze_functions.png %})
{% endtab %}
{% endtabs %}

Para saber mais sobre a função `list_functions`, consulte [Funções de API disponíveis]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#general-functions){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#general-functions){% endif %}.

### Obter detalhes sobre um ID de Canvas {#get-details-about-a-canvas-id}

{% tabs %}
{% tab Claude %}
!["Obter detalhes sobre um ID de Canvas" sendo perguntado e respondido no Claude.]({% image_buster /assets/img/mcp_server/claude/get_details_about_a_canvas_id.png %}){: style="max-width:85%;"}
{% endtab %}

{% tab Cursor %}
!["Obter detalhes sobre um ID de Canvas" sendo perguntado e respondido no Cursor.]({% image_buster /assets/img/mcp_server/cursor/get_details_about_a_canvas_id.png %})
{% endtab %}
{% endtabs %}

Para saber mais sobre a função `get_canvas_details`, consulte [Funções de API disponíveis]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#canvases){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#canvases){% endif %}.

### Mostre meus Canvas recentes {#show-me-my-recent-canvases}

{% tabs %}
{% tab Claude %}
!["Mostre meus Canvas recentes" sendo perguntado e respondido no Claude.]({% image_buster /assets/img/mcp_server/claude/show_my_recent_canvases.png %}){: style="max-width:85%;"}
{% endtab %}

{% tab Cursor %}
!["Mostre meus Canvas recentes" sendo perguntado e respondido no Cursor.]({% image_buster /assets/img/mcp_server/cursor/show_me_my_recent_canvases.png %})
{% endtab %}
{% endtabs %}

Para saber mais sobre a função `get_canvas_list`, consulte [Funções de API disponíveis]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#canvases){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#canvases){% endif %}.

### Criar um modelo de e-mail {#create-an-email-template}

{% tabs %}
{% tab Cursor %}
!["Criar um modelo de e-mail" sendo perguntado e respondido no Cursor.]({% image_buster /assets/img/mcp_server/cursor/create_an_email_template.png %})
{% endtab %}
{% endtabs %}

Para saber mais sobre a função `create_email_template`, consulte [Funções de API disponíveis]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#templates){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#templates){% endif %}.

### Atualizar um bloco de conteúdo {#update-a-content-block}

{% tabs %}
{% tab Cursor %}
!["Atualizar um bloco de conteúdo" sendo perguntado e respondido no Cursor.]({% image_buster /assets/img/mcp_server/cursor/update_a_content_block.png %})
{% endtab %}
{% endtabs %}

Para saber mais sobre a função `update_content_block`, consulte [Funções de API disponíveis]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#content-blocks){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#content-blocks){% endif %}.

{% multi_lang_include mcp_server/legal_disclaimer.md %}