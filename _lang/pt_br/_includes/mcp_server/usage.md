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
**Exemplo de prompt**

`What are my available Braze functions?`

**Exemplo de resposta**

Verifiquei o servidor MCP do Braze com `list_functions` e encontrei 38 funções de API disponíveis.

Aqui estão alguns exemplos por categoria:

- **Análise de dados e gerenciamento de Campaigns**
  - `get_campaign_dataseries`
  - `get_campaign_details`
  - `get_campaign_list`
- **Análise de dados e gerenciamento de Canvas**
  - `get_canvas_data_series`
  - `get_canvas_data_summary`
  - `get_canvas_list`
  - `get_canvas_details`
- **Modelos**
  - `create_email_template`
- **Content Blocks**
  - `create_content_block`
  - `get_content_blocks`
  - `get_content_block_info`
  - `update_content_block`
{% endtab %}

{% tab Cursor %}
**Exemplo de prompt**

`What are my available Braze functions?`

**Exemplo de resposta**

Vou verificar suas funções disponíveis usando o servidor MCP do Braze.

- Chamou `list_functions`

Com base nesse resultado, você tem 38 funções de API da Braze organizadas em categorias como:

- Análise de dados e gerenciamento de Campaigns
- Análise de dados e gerenciamento de Canvas
- Modelos
- Content Blocks

Exemplos de funções incluem:

- `get_campaign_list`
- `get_canvas_list`
- `get_canvas_details`
- `create_email_template`
- `update_content_block`
{% endtab %}
{% endtabs %}

Para saber mais sobre a função `list_functions`, consulte [Funções de API disponíveis]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#general-functions){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#general-functions){% endif %}.

### Obter detalhes sobre um ID de Canvas {#get-details-about-a-canvas-id}

{% tabs %}
{% tab Claude %}
**Exemplo de prompt**

`Get details about canvas ID YOUR-TEST-CANVAS-ID-123`

**Exemplo de resposta**

Recuperei os detalhes de `YOUR-TEST-CANVAS-ID-123` usando `get_canvas_details`.

- **Nome do Canvas:** `YOUR-TEST-CANVAS-NAME`
- **ID:** `YOUR-TEST-CANVAS-ID-123`
- **Status:** Rascunho (não ativado)
- **Criado em:** 15 de jan. de 2026, 10:30 UTC
- **Última atualização:** 16 de jan. de 2026, 14:45 UTC
- **Tipo de programação:** Baseado em tempo
- **Canal principal:** E-mail

Detalhes da mensagem de e-mail:

- **Assunto:** `YOUR-TEST-SUBJECT-LINE`
- **De:** `YOUR-TEST-SENDER@example.com`
- **ID da mensagem:** `YOUR-TEST-MESSAGE-ID-123`
{% endtab %}

{% tab Cursor %}
**Exemplo de prompt**

`Get details about canvas ID YOUR-TEST-CANVAS-ID-123`

**Exemplo de resposta**

Recuperei este Canvas usando `get_canvas_details`:

- **ID do Canvas:** `YOUR-TEST-CANVAS-ID-123`
- **Nome do Canvas:** `YOUR-TEST-CANVAS-NAME`
- **Status:** Rascunho
- **Canal:** E-mail
- **ID da mensagem:** `YOUR-TEST-MESSAGE-ID-123`

Resumo do conteúdo do e-mail:

1. Seção de cabeçalho com imagem da marca
2. Seção de título principal
3. Seção hero com botão de CTA
4. Seção de recursos com conteúdo de apoio
{% endtab %}
{% endtabs %}

Para saber mais sobre a função `get_canvas_details`, consulte [Funções de API disponíveis]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#canvases){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#canvases){% endif %}.

### Mostre meus Canvas recentes {#show-me-my-recent-canvases}

{% tabs %}
{% tab Claude %}
**Exemplo de prompt**

`Show me my recent Canvases`

**Exemplo de resposta**

Verifiquei suas ferramentas disponíveis com `list_functions` e, em seguida, usei `get_canvas_list` para retornar seus Canvas editados mais recentemente.

Canvas mais recentes:

1. **YOUR-TEST-CANVAS-ALPHA**
   - ID: `YOUR-TEST-ID-123`
   - Última edição: 16 de jan. de 2026, 14:45 UTC
2. **YOUR-TEST-CANVAS-BETA**
   - ID: `YOUR-TEST-ID-456`
   - Última edição: 15 de jan. de 2026, 11:10 UTC
3. **YOUR-TEST-CANVAS-GAMMA**
   - ID: `YOUR-TEST-ID-789`
   - Última edição: 14 de jan. de 2026, 20:25 UTC
{% endtab %}

{% tab Cursor %}
**Exemplo de prompt**

`Show me my recent Canvases`

**Exemplo de resposta**

Vou recuperar sua lista de Canvas recentes do servidor MCP do Braze.

- Chamou `list_functions`
- Chamou `get_canvas_list`

Canvas recentes (ordenados pela edição mais recente):

- **Nome do Canvas:** `YOUR-TEST-CANVAS-ALPHA`
  - **Última edição:** 16 de jan. de 2026, 14:45 UTC
  - **ID do Canvas:** `YOUR-TEST-ID-123`
  - **Tags:** `lifecycle`, `email`
- **Nome do Canvas:** `YOUR-TEST-CANVAS-BETA`
  - **Última edição:** 15 de jan. de 2026, 11:10 UTC
  - **ID do Canvas:** `YOUR-TEST-ID-456`
  - **Tags:** `promo`
{% endtab %}
{% endtabs %}

Para saber mais sobre a função `get_canvas_list`, consulte [Funções de API disponíveis]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#canvases){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#canvases){% endif %}.

### Criar um modelo de e-mail {#create-an-email-template}

{% tabs %}
{% tab Claude %}
**Exemplo de prompt**

`Create an email template named "YOUR-TEST-TEMPLATE-NAME" for onboarding messages.`

**Exemplo de resposta**

Criei seu modelo com `create_email_template`.

- **Nome do modelo:** `YOUR-TEST-TEMPLATE-NAME`
- **ID do modelo:** `YOUR-TEST-TEMPLATE-ID-123`
- **Linha de assunto:** `YOUR-TEST-SUBJECT-LINE`
- **Pré-cabeçalho:** `YOUR-TEST-PREHEADER`
- **Criado em:** 16 de jan. de 2026, 15:10 UTC

Agora você pode referenciar `YOUR-TEST-TEMPLATE-ID-123` ao criar ou atualizar Campaigns e Canvas.
{% endtab %}

{% tab Cursor %}
**Exemplo de prompt**

`Create an email template named "YOUR-TEST-TEMPLATE-NAME" for onboarding messages.`

**Exemplo de resposta**

Usei `create_email_template` e criei um novo modelo com sucesso.

- **ID do modelo:** `YOUR-TEST-TEMPLATE-ID-123`
- **Nome do modelo:** `YOUR-TEST-TEMPLATE-NAME`
- **Assunto:** `YOUR-TEST-SUBJECT-LINE`
- **Descrição:** `Onboarding lifecycle template`

Se quiser, também posso gerar um corpo HTML inicial e um fallback em texto simples para este modelo.
{% endtab %}
{% endtabs %}

Para saber mais sobre a função `create_email_template`, consulte [Funções de API disponíveis]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#templates){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#templates){% endif %}.

### Atualizar um bloco de conteúdo {#update-a-content-block}

{% tabs %}
{% tab Claude %}
**Exemplo de prompt**

`Update content block "YOUR-TEST-CONTENT-BLOCK-ID-123" with new body copy for our spring promotion.`

**Exemplo de resposta**

Atualizei seu bloco de conteúdo usando `update_content_block`.

- **ID do bloco de conteúdo:** `YOUR-TEST-CONTENT-BLOCK-ID-123`
- **Nome:** `YOUR-TEST-CONTENT-BLOCK-NAME`
- **Status:** Atualizado
- **Atualizado em:** 16 de jan. de 2026, 15:25 UTC

Pré-visualização:

`YOUR-TEST-CONTENT-BLOCK-BODY-V2`
{% endtab %}

{% tab Cursor %}
**Exemplo de prompt**

`Update content block "YOUR-TEST-CONTENT-BLOCK-ID-123" with new body copy for our spring promotion.`

**Exemplo de resposta**

Executei `update_content_block` e confirmei que a atualização foi concluída.

- **ID do bloco de conteúdo:** `YOUR-TEST-CONTENT-BLOCK-ID-123`
- **Versão anterior:** `v1`
- **Versão atual:** `v2`
- **Última atualização:** 16 de jan. de 2026, 15:25 UTC

Pré-visualização do conteúdo atualizado:

`YOUR-TEST-CONTENT-BLOCK-BODY-V2`
{% endtab %}
{% endtabs %}

Para saber mais sobre a função `update_content_block`, consulte [Funções de API disponíveis]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#content-blocks){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#content-blocks){% endif %}.

{% multi_lang_include mcp_server/legal_disclaimer.md %}