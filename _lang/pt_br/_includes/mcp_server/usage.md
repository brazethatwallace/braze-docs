# Usando o servidor MCP do Braze {#using-the-braze-mcp-server}

> Aprenda a interagir com seus dados da Braze por meio de linguagem natural após se conectar ao servidor MCP remoto da Braze. Para saber mais, consulte [Servidor MCP do Braze]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/){% endif %}.

{% multi_lang_include mcp_server/beta_alert.md %}

## Pré-requisitos {#prerequisites}

Antes de poder usar esse recurso, você precisará [configurar o servidor MCP do Braze]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}.

## Melhores práticas {#best-practices}

Ao usar o servidor MCP do Braze por meio de ferramentas de linguagem natural, lembre-se destas dicas:

- Confirme o espaço de trabalho no seu prompt, especialmente quando você tem acesso a vários espaços de trabalho.
- Seja específico sobre intervalos de datas e métricas ao solicitar análise de dados.
- Peça ao agente para confirmar quais ferramentas ele usou ao validar os resultados.
- Compare recomendações de alto impacto com os dados de origem no dashboard da Braze.

## Exemplos de uso {#usage-examples}

Após [configurar o servidor MCP do Braze]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}, você pode interagir com a Braze por meio de linguagem natural. Aqui estão alguns exemplos para você começar.

### Quais espaços de trabalho posso acessar? {#which-workspaces-can-i-access}

{% tabs %}
{% tab Exemplo de prompt %}

`Show my available Braze workspaces and tell me which one to use for production campaign analytics.`
{% endtab %}
{% tab Exemplo de resposta %}

Chamei `get_workspaces` e encontrei estes espaços de trabalho:

- `Marketing - Production` (`app_group_id`: `YOUR-APP-GROUP-ID-1`)
- `Marketing - Staging` (`app_group_id`: `YOUR-APP-GROUP-ID-2`)

Use `Marketing - Production` para prompts de análise de dados de campanhas em produção.
{% endtab %}
{% endtabs %}

Para saber mais, consulte [Funções de API disponíveis]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#workspaces){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#workspaces){% endif %}.

### Mostre o desempenho de campanhas da última semana {#show-me-campaign-performance-for-last-week}

{% tabs %}
{% tab Exemplo de prompt %}

`In the Marketing - Production workspace, show campaign performance for the last seven days, including sends, opens, clicks, and top performers.`
{% endtab %}
{% tab Exemplo de resposta %}

Usei `get_campaign_list` e `get_campaign_dataseries` para o espaço de trabalho e intervalo de datas solicitados.

Resumo:

- Total de envios: `YOUR-TEST-SENDS`
- Total de aberturas: `YOUR-TEST-OPENS`
- Total de cliques: `YOUR-TEST-CLICKS`
- Campanha com mais aberturas: `YOUR-TEST-CAMPAIGN-NAME`

Posso detalhar por campanha, canal ou dia, se necessário.
{% endtab %}
{% endtabs %}

Para saber mais, consulte [Funções de API disponíveis]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#campaigns){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#campaigns){% endif %}.

### Criar um modelo de e-mail {#create-an-email-template}

{% tabs %}
{% tab Exemplo de prompt %}

`In the Marketing - Production workspace, create an onboarding email template named "YOUR-TEST-TEMPLATE-NAME".`
{% endtab %}
{% tab Exemplo de resposta %}

Usei `create_email_template` e criei seu modelo.

- **ID do modelo:** `YOUR-TEST-TEMPLATE-ID-123`
- **Nome do modelo:** `YOUR-TEST-TEMPLATE-NAME`
- **Espaço de trabalho:** `Marketing - Production`
{% endtab %}
{% endtabs %}

Para saber mais, consulte [Funções de API disponíveis]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#templates-email){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#templates-email){% endif %}.

## Exemplos de fluxos de trabalho {#example-workflows}

Estes exemplos combinam várias ferramentas para concluir uma tarefa do início ao fim.

### Relatório entre vários espaços de trabalho {#report-across-multiple-workspaces}

{% tabs %}
{% tab Exemplo de prompt %}

`Get me an analytics report for the past week from my US Prod workspace and my EU Prod workspace, and compare total sends and open rates.`
{% endtab %}
{% tab Exemplo de resposta %}

Chamei `get_workspaces` para confirmar o acesso e, em seguida, executei `get_campaign_dataseries` para cada espaço de trabalho nos últimos sete dias.

- `US Prod`: `YOUR-TEST-SENDS` envios, `YOUR-TEST-OPEN-RATE` taxa de abertura
- `EU Prod`: `YOUR-TEST-SENDS` envios, `YOUR-TEST-OPEN-RATE` taxa de abertura

`US Prod` enviou mais mensagens nesta semana, enquanto `EU Prod` teve a taxa de abertura mais alta. Posso detalhar qualquer espaço de trabalho por campanha ou canal.
{% endtab %}
{% endtabs %}

### Copiar modelos de staging para produção {#copy-templates-from-staging-to-production}

{% tabs %}
{% tab Exemplo de prompt %}

`Copy the email templates from my Staging workspace to my Production workspace.`
{% endtab %}
{% tab Exemplo de resposta %}

Usei `get_email_templates` e `get_email_template_info` para ler os modelos em `Staging` e, em seguida, `create_email_template` para recriar cada um em `Production`.

- `YOUR-TEST-TEMPLATE-NAME-1`: criado em `Production` (`YOUR-TEST-TEMPLATE-ID-1`)
- `YOUR-TEST-TEMPLATE-NAME-2`: criado em `Production` (`YOUR-TEST-TEMPLATE-ID-2`)

Pulei os modelos do editor de arrastar e soltar, que não são suportados por `get_email_template_info`. Avise se quiser que eu revise os modelos copiados.
{% endtab %}
{% endtabs %}

### Resumo semanal de integridade de campanhas {#summarize-weekly-campaign-health}

{% tabs %}
{% tab Exemplo de prompt %}

`Give me a weekly campaign health summary for the Production workspace.`
{% endtab %}
{% tab Exemplo de resposta %}

Usei `get_campaign_list` e `get_campaign_dataseries` para obter os últimos sete dias de atividade em `Production`.

- Total de envios: `YOUR-TEST-SENDS`
- Taxa de abertura: `YOUR-TEST-OPEN-RATE`
- Taxa de cliques: `YOUR-TEST-CLICK-RATE`
- Campanha com mais conversões: `YOUR-TEST-CAMPAIGN-NAME`

Os envios aumentaram em relação à semana anterior. Posso adicionar um detalhamento por canal ou sinalizar campanhas com engajamento em queda.
{% endtab %}
{% endtabs %}

## Como o servidor MCP remoto funciona {#how-the-remote-mcp-server-works}

Quando você envia uma solicitação, algumas etapas acontecem nos bastidores:

1. **Você envia um prompt ao seu cliente.** Você digita uma solicitação em linguagem natural, como pedir o desempenho de campanhas da última semana.
2. **O modelo do cliente seleciona ferramentas.** O modelo de IA no seu cliente interpreta sua solicitação e a traduz em uma ou mais chamadas de ferramentas da Braze, como `get_campaign_list` e `get_campaign_dataseries`.
3. **A Braze executa a chamada de ferramenta.** O servidor MCP remoto recebe cada chamada de ferramenta pela sua sessão OAuth autenticada, aplica o espaço de trabalho que você especificou e a executa no endpoint correspondente da REST API da Braze.
4. **A Braze retorna o resultado.** O servidor envia os dados de volta ao seu cliente, que os formata e apresenta para você.

Seu acesso é a interseção de duas coisas:

- **Os escopos concedidos quando você autorizou a conexão**, como `mcp:tools`.
- **Suas próprias permissões de usuário no dashboard.** Se você não pode visualizar campanhas no dashboard, seu agente também não pode. Se você pode criar modelos de e-mail, seu agente também pode. Um agente nunca pode exceder seu próprio acesso.

O contexto do espaço de trabalho é passado com cada solicitação em vez de ser armazenado em um arquivo de configuração local, então uma única conexão pode funcionar em todos os espaços de trabalho aos quais você tem acesso autorizado.

{% multi_lang_include mcp_server/legal_disclaimer.md %}