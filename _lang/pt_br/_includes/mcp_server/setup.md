# Configure o servidor Braze MCP {#setting-up-the-braze-mcp-server}

> Aprenda como configurar o servidor Braze MCP, para que você possa interagir com seus dados do Braze usando ferramentas de linguagem natural como Claude e Cursor. Para mais informações gerais, veja [servidor Braze MCP]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/){% endif %}.

{% multi_lang_include mcp_server/beta_alert.md %}

## Pré-requisitos {#prerequisites}

Antes de começar, você precisará do seguinte:

| Pré-requisito | Descrição |
|--------------|-------------|
| Chave de API da Braze | Uma chave de API da Braze com as permissões necessárias. Você criará uma nova chave quando [configurar seu servidor Braze MCP](#create-api-key). |
| Cliente MCP | [Claude](https://claude.ai/), [Cursor](https://cursor.com/) e [Google Gemini CLI](https://docs.cloud.google.com/gemini/docs/codeassist/gemini-cli) são oficialmente suportados. Você deve ter uma conta em um desses clientes para usar o servidor Braze MCP. |
| Terminal | Um app de terminal para que você possa executar comandos e instalar ferramentas. Use seu app de terminal preferido ou o que já está instalado no seu computador. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Configurando o servidor Braze MCP

### Etapa 1: Instalar `uv` {#step-1-install-uv}

Primeiro, instale `uv`&#8212;uma [ferramenta de linha de comando da Astral](https://docs.astral.sh/uv/getting-started/installation/) para gerenciamento de dependências e manipulação de pacotes Python.

{% tabs local %}
{% tab MacOS e Linux %}
Abra seu app de terminal, cole o seguinte comando e pressione <kbd>Enter</kbd>.

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

A saída é semelhante ao seguinte:

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
 Abra o Windows PowerShell, cole o seguinte comando e pressione <kbd>Enter</kbd>.

```powershell
irm https://astral.sh/uv/install.ps1 | iex
```

A saída é semelhante ao seguinte:

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

### Etapa 2: Criar uma chave de API {#create-api-key}

O servidor Braze MCP inclui endpoints somente leitura e de escrita. Eles não retornam dados de perfis de usuários da Braze. Os endpoints de escrita permitem que agentes criem ou atualizem conteúdo no seu espaço de trabalho.

Para criar sua chave de API:

1. Acesse **Configurações** > **APIs e identificadores** > **Chaves de API**.
2. Crie uma nova chave.
3. Atribua algumas ou todas as permissões a seguir à sua chave.

{% alert important %}
Atribua apenas as permissões que você deseja que seu agente use. Para impedir que seu agente faça alterações na Braze, não inclua permissões de escrita ao criar sua chave de API.
{% endalert %}

{% details Lista de permissões suportadas %}
#### Campaigns

| Endpoint | Permissão necessária |
|----------|---------------------|
| [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/) | `campaigns.data_series` |
| [`/campaigns/details`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details/) | `campaigns.details` |
| [`/campaigns/list`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns/) | `campaigns.list` |
| [`/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics/) | `sends.data_series` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Campaigns" }

#### Canvas

| Endpoint | Permissão necessária |
|----------|---------------------|
| [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics/) | `canvas.data_series` |
| [`/canvas/data_summary`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary/) | `canvas.data_summary` |
| [`/canvas/details`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/) | `canvas.details` |
| [`/canvas/list`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases/) | `canvas.list` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Canvas" }

#### Catalogs

| Endpoint | Permissão necessária |
|----------|---------------------|
| [`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs/) | `catalogs.get` |
| [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk/) | `catalogs.get_items` |
| [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details/) | `catalogs.get_item` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Catalogs" }

#### Cloud Data Ingestion

| Endpoint | Permissão necessária |
|----------|---------------------|
| [`/cdi/integrations`]({{site.baseurl}}/api/endpoints/cdi/get_integration_list/) | `cdi.integration_list` |
| [`/cdi/integrations/{integration_id}/job_sync_status`]({{site.baseurl}}/api/endpoints/cdi/get_job_sync_status/) | `cdi.integration_job_status` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Cloud Data Ingestion" }

#### Content Blocks

As permissões `content_blocks.create` e `content_blocks.update` são permissões de escrita. Adicione-as apenas se quiser que seu agente crie ou atualize blocos de conteúdo no seu espaço de trabalho.

| Endpoint | Permissão necessária |
|----------|---------------------|
| [`/content_blocks/list`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks/) | `content_blocks.list` |
| [`/content_blocks/info`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information/) | `content_blocks.info` |
| [`/content_blocks/create`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block/) | `content_blocks.create` |
| [`/content_blocks/update`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block/) | `content_blocks.update` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Content Blocks" }

#### Custom Attributes

| Endpoint | Permissão necessária |
|----------|---------------------|
| [`/custom_attributes`]({{site.baseurl}}/api/endpoints/export/custom_attributes/get_custom_attributes/) | `custom_attributes.get` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Custom Attributes" }

#### Events

| Endpoint | Permissão necessária |
|----------|---------------------|
| [`/events/list`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events/) | `events.list` |
| [`/events/data_series`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_analytics/) | `events.data_series` |
| [`/events`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_data/) | `events.get` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Events" }

#### KPIs

| Endpoint | Permissão necessária |
|----------|---------------------|
| [`/kpi/new_users/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_daily_new_users_date/) | `kpi.new_users.data_series` |
| [`/kpi/dau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_dau_date/) | `kpi.dau.data_series` |
| [`/kpi/mau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_mau_30_days/) | `kpi.mau.data_series` |
| [`/kpi/uninstalls/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_uninstalls_date/) | `kpi.uninstalls.data_series` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="KPIs" }

#### Media Library

A permissão `media_library.create` é uma permissão de escrita. Adicione-a apenas se quiser que seu agente faça upload de ativos para sua biblioteca de mídia.

| Endpoint | Permissão necessária |
|----------|---------------------|
| [`/media_library/create`]({{site.baseurl}}/api/endpoints/media_library/manage_assets/create/) | `media_library.create` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Media Library" }

#### Messages

| Endpoint | Permissão necessária |
|----------|---------------------|
| [`/messages/scheduled_broadcasts`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/get_messages_scheduled/) | `messages.schedule_broadcasts` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Messages" }

#### Preference Center

| Endpoint | Permissão necessária |
|----------|---------------------|
| [`/preference_center/v1/list`]({{site.baseurl}}/api/endpoints/preference_center/get_list_preference_center/) | `preference_center.list` |
| [`/preference_center/v1/{preferenceCenterExternalID}`]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center/) | `preference_center.get` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Preference Center" }

#### Purchases

| Endpoint | Permissão necessária |
|----------|---------------------|
| [`/purchases/product_list`]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id/) | `purchases.product_list` |
| [`/purchases/revenue_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_revenue_series/) | `purchases.revenue_series` |
| [`/purchases/quantity_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_number_of_purchases/) | `purchases.quantity_series` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Purchases" }

#### Segments

| Endpoint | Permissão necessária |
|----------|---------------------|
| [`/segments/list`]({{site.baseurl}}/api/endpoints/export/segments/get_segment/) | `segments.list` |
| [`/segments/data_series`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics/) | `segments.data_series` |
| [`/segments/details`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details/) | `segments.details` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Segments" }

#### Sends

| Endpoint | Permissão necessária |
|----------|---------------------|
| [`/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics/) | `sends.data_series` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Sends" }

#### Sessions

| Endpoint | Permissão necessária |
|----------|---------------------|
| [`/sessions/data_series`]({{site.baseurl}}/api/endpoints/export/sessions/get_sessions_analytics/) | `sessions.data_series` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Sessions" }

#### SDK Authentication Keys

| Endpoint | Permissão necessária |
|----------|---------------------|
| [`/app_group/sdk_authentication/keys`]({{site.baseurl}}/api/endpoints/sdk_authentication/get_sdk_authentication_keys/) | `sdk_authentication.keys` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="SDK Authentication Keys" }

#### Subscription

| Endpoint | Permissão necessária |
|----------|---------------------|
| [`/subscription/status/get`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/) | `subscription.status.get` |
| [`/subscription/user/status`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups/) | `subscription.groups.get` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Subscription" }

#### Templates

As permissões `templates.email.create` e `templates.email.update` são permissões de escrita. Adicione-as apenas se quiser que seu agente crie ou atualize modelos de e-mail no seu espaço de trabalho.

| Endpoint | Permissão necessária |
|----------|---------------------|
| [`/templates/email/list`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates/) | `templates.email.list` |
| [`/templates/email/info`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_see_email_template_information/) | `templates.email.info` |
| [`/templates/email/create`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template/) | `templates.email.create` |
| [`/templates/email/update`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template/) | `templates.email.update` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Templates" }
{% enddetails %}

{% alert warning %}
Não reutilize uma chave de API existente. Crie uma especificamente para seu cliente MCP. Atribua apenas as permissões que seu agente precisa. Os agentes podem tentar usar qualquer permissão que você conceder, então não inclua permissões de escrita se você não quiser que seu agente faça alterações na Braze.
{% endalert %}

### Etapa 3: Obtenha seu identificador e endpoint {#step-3-get-your-identifier-and-endpoint}

Quando você configurar seu cliente MCP, precisará do identificador da sua chave de API e do endpoint REST do seu espaço de trabalho. Para obter esses detalhes, volte para a página **Chaves de API** no dashboard&#8212;mantenha esta página aberta, para que você possa consultá-la durante [a próxima etapa](#configure-client).

![A página "Chaves de API" na Braze mostrando uma chave de API recém-criada e o endpoint REST do usuário.]({% image_buster /assets/img/mcp_server/get_indentifer_and_endpoint.png %}){: style="max-width:85%;"}

### Etapa 4: Configure seu cliente MCP {#configure-client}

Configure seu cliente MCP usando o arquivo de configuração pré-fornecido.

{% tabs %}
{% tab Claude %}
Configure seu servidor MCP usando o diretório de conectores do [Claude Desktop](https://claude.ai/download).

1. No Claude Desktop, acesse **Settings** > **Connectors** > **Browse Connectors** > **Desktop Extensions** > **Braze MCP Server** > **Install**.
2. Insira sua chave de API e URL base.
3. Salve a configuração e reinicie o Claude Desktop.

{% endtab %}

{% tab Cursor %}
No [Cursor](https://cursor.com/), acesse **Settings** > **Tools and Integrations** > **MCP Tools** > **Add Custom MCP** e adicione o seguinte trecho:

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

Substitua `key-identifier` e `rest-endpoint` pelos valores correspondentes da página **Chaves de API** na Braze. Sua configuração deve ser semelhante ao seguinte:

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

Quando terminar, salve a configuração e reinicie o Cursor.
{% endtab %}
{% tab Gemini CLI %}
O Gemini CLI lê as configurações do usuário de `~/.gemini/settings.json`. Se esse arquivo não existir, você pode criá-lo executando o seguinte no seu terminal:

```powershell
mkdir -p ~/.gemini
nano ~/.gemini/settings.json
```

Em seguida, substitua `yourname` pela string exata antes de `@BZXXXXXXXX` no prompt do seu terminal. Depois, substitua `key-identifier` e `rest-endpoint` pelos valores correspondentes da página **Chaves de API** na Braze.

Sua configuração deve ser semelhante ao seguinte:

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

Quando terminar, salve a configuração e reinicie o Gemini CLI. Em seguida, no Gemini, execute os seguintes comandos para verificar se o servidor Braze MCP está listado e se as ferramentas e o esquema estão disponíveis para uso:

```powershell
gemini
/mcp
/mcp desc
/mcp schema
```

Você deve ver o servidor `braze` listado com as ferramentas e o esquema disponíveis para uso.

{% endtab %}
{% endtabs %}

### Etapa 5: Envie um prompt de teste {#step-5-send-a-test-prompt}

Depois de configurar o servidor Braze MCP, tente enviar um prompt de teste para o seu cliente MCP. Para outros exemplos e práticas recomendadas, veja [Usando o servidor Braze MCP]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/usage/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/usage/){% endif %}.

{% tabs %}
{% tab Claude %}
**Prompt de exemplo:** `What are my available Braze functions?`
**Resposta de exemplo:** Usou `list_functions` e retornou as categorias de funções disponíveis do Braze MCP.
{% endtab %}

{% tab Cursor %}
**Prompt de exemplo:** `What are my available Braze functions?`
**Resposta de exemplo:** Consultou `list_functions` e listou funções como `get_canvas_list`.
{% endtab %}

{% tab Gemini CLI %}
**Prompt de exemplo:** `What are my available Braze functions?`
**Resposta de exemplo:** Consultou `list_functions` no Gemini CLI e retornou as categorias de funções disponíveis do Braze MCP e funções de exemplo.
{% endtab %}
{% endtabs %}

## Solução de problemas {#troubleshooting}

### Erros de terminal {#terminal-errors}

#### Comando `uvx` não encontrado {#uvx-command-not-found}

Se você receber um erro informando que o comando `uvx` não foi encontrado, reinstale `uv` e reinicie seu terminal.

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

#### Erro `spawn uvx ENOENT` {#spawn-uvx-enoent-error}

Se você receber um erro `spawn uvx ENOENT`, pode ser necessário atualizar o caminho do arquivo no arquivo de configuração do seu cliente. Primeiro, abra seu terminal e execute o seguinte comando:

```bash
which uvx
```

O comando deve retornar uma mensagem semelhante à seguinte:

```bash
/Users/alex-lee/.local/bin/uvx
```

Copie a mensagem para sua área de transferência e abra [o arquivo de configuração do seu cliente](#configure-client). Substitua `"command": "uvx"` pelo caminho que você copiou e reinicie seu cliente. Por exemplo:

```json
"command": "/Users/alex-lee/.local/bin/uvx"
```

#### A instalação do pacote falha {#package-installation-fails}

Se a instalação do seu pacote falhar, tente instalar uma versão específica do Python.

```bash
uvx --python 3.12 braze-mcp-server@latest
```

### Configuração do cliente {#client-configuration}

#### "Esta extensão não é compatível com seu dispositivo" {#this-extension-is-not-compatible-with-your-device}

Se você vir esse erro ao instalar a extensão do servidor Braze MCP, isso pode indicar uma das seguintes situações:

- **Seu dispositivo não atende aos requisitos**: Algumas extensões de servidor MCP exigem versões específicas do sistema operacional ou hardware.
- **Ferramentas de desenvolvimento ausentes (somente macOS)**: No macOS, a instalação da extensão requer ferramentas de desenvolvedor de linha de comando para executar comandos Python. Se essas ferramentas não estiverem instaladas, a instalação falhará com esse erro.

Para instalar as ferramentas de desenvolvedor de linha de comando no macOS, execute o seguinte no seu terminal:

```bash
xcode-select --install
```

Após a conclusão da instalação, reinicie seu cliente MCP e tente instalar a extensão novamente.

#### O cliente MCP não consegue encontrar o servidor Braze {#mcp-client-cant-find-the-braze-server}

1. Verifique se a sintaxe da configuração do seu cliente MCP está correta.
2. Reinicie seu cliente MCP após as alterações de configuração.
3. Verifique se `uvx` está no `PATH` do seu sistema.

#### Erros de autenticação {#authentication-errors}

1. Verifique se seu `BRAZE_API_KEY` está correto e ativo.
2. Certifique-se de que seu `BRAZE_BASE_URL` corresponde à sua instância da Braze.
3. Verifique se sua chave de API tem as [permissões corretas](#create-api-key).

#### Timeouts de conexão ou erros de rede {#connection-timeouts-or-network-errors}

1. Verifique se seu `BRAZE_BASE_URL` está correto para sua instância.
2. Verifique sua conexão de rede e as configurações do firewall.
3. Certifique-se de que está usando HTTPS na sua URL base.

{% multi_lang_include mcp_server/legal_disclaimer.md %}