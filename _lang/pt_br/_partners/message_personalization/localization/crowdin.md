---
nav_title: Crowdin
article_title: Crowdin
description: "Use a integração com o Crowdin para traduzir Campaigns, experiências no Canvas, modelos de e-mail e Content Blocks com Translation Memory, glossários e tradução automática."
alias: /partners/crowdin/
page_type: partner
search_tag: Partner

---

# Crowdin

> O [Crowdin](https://crowdin.com/) é uma plataforma de gerenciamento de localização baseada em IA que ajuda equipes a automatizar a tradução de seus softwares, apps e conteúdos de marketing.

Conecte o Crowdin à Braze para gerenciar traduções das suas Campaigns e experiências no Canvas. A sincronização automatizada funciona com tradução automática, Translation Memory e glossários para que os fluxos de trabalho humanos e automatizados permaneçam consistentes.

_Essa integração é mantida pelo Crowdin._

## Sobre a integração {#about-the-integration}

A Crowdin oferece dois apps para a Braze: [Braze Campaigns & Canvas](https://store.crowdin.com/braze-content-translation) e [Braze Email Templates](https://store.crowdin.com/braze-app). Escolha com base nos recursos da Braze que você localiza. A tabela a seguir compara os dois.

### Escolha o app certo da Crowdin {#choose-the-right-crowdin-app}

| Canal ou recurso | Braze Campaigns & Canvas | Braze Email Templates |
| --- | --- | --- |
| **Campaigns** | ✅ Suportado | ❌ Não suportado |
| **Etapas do Canvas** | ✅ Suportado | ❌ Não suportado |
| **Modelos de e-mail** | ❌ Não suportado | ✅ Suportado |
| **Content Blocks** | ❌ Não suportado | ✅ Suportado |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Escolha o app certo da Crowdin" }

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| --- | --- |
| **Conta no Crowdin** | É necessária uma [conta no Crowdin.com](https://accounts.crowdin.com/register) ou uma [conta no Crowdin Enterprise](https://accounts.crowdin.com/workspace/create). |
| **Projeto no Crowdin** | Antes de conectar a Braze, [crie um projeto de tradução](https://support.crowdin.com/creating-project/) no Crowdin ou no Crowdin Enterprise. |
| **Chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze** | Uma chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze com permissões para Campaigns, Canvas, Content Blocks, atributos personalizados, e-mail e modelos. |
| **Endpoint REST or transferir estado representacional da Braze** | A URL específica do seu endpoint REST or transferir estado representacional da Braze (por exemplo, `https://rest.iad-03.braze.com`). |
| **Configurações multilíngue da Braze** | Os locais devem ser configurados no seu dashboard da Braze em **Configurações** > **Configurações de localização**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração Braze Campaigns & Canvas {#braze-campaigns-canvas-integration}

Se você localiza conteúdo dentro de mensagens ativas, use o [app Braze Campaigns & Canvas](https://store.crowdin.com/braze-content-translation) para sincronizar strings traduzíveis dos seus rascunhos de Campaign e Canvas com o suporte multilíngue da Braze.

Para um passo a passo em vídeo, consulte [Integração Braze Campaigns & Canvas](https://youtu.be/ahG1ET4VRKA).

### Etapa 1: Configurar as definições multilíngues na Braze {#step-1-set-up-multi-language-settings-in-braze}

Antes de conectar o Crowdin, adicione seus idiomas de destino na Braze.

1. Na Braze, acesse **Settings** > **Localization Settings**.
2. Adicione os idiomas que você pretende suportar.

![Página de locais na Braze, em Settings, mostrando nomes de locais, chaves de locale e o botão Add locale.]({% image_buster /assets/img/crowdin/braze_locales.png %})

{: start="3"}
3. Anote cada **Locale key** (por exemplo, `en-US`, `fr-FR`, `es-ES`). Você usará esses valores ao mapear idiomas no Crowdin.

### Etapa 2: Configurar o projeto Braze no Crowdin {#step-2-set-up-the-braze-project-in-crowdin}

1. Na sua conta Crowdin Enterprise ou Crowdin.com, acesse **Store** no menu de navegação.
2. Pesquise por **Braze Campaigns & Canvas** e selecione **Install**.

![Crowdin Store com Braze Campaigns & Canvas selecionado e Install destacado.]({% image_buster /assets/img/crowdin/crowdin_store_campaigns_canvas.png %})

{: start="3"}
3. Selecione o projeto (ou projetos) onde deseja usar essa integração.
4. Para abrir a integração, acesse o projeto em **Integrations** > **Braze Campaigns & Canvas**.

#### Conectando a Braze ao Crowdin {#connecting-braze-to-crowdin}

Autorize a conexão com suas credenciais de API or interface de programação do aplicativo (API) da Braze:

![Formulário de conexão Braze Campaigns & Canvas no Crowdin com chave da REST API, endpoint REST e Log in with Braze Campaigns & Canvas.]({% image_buster /assets/img/crowdin/crowdin_campaigns_canvas_login.png %})

- **Chave da REST or transferir estado representacional API or interface de programação do aplicativo (API) da Braze:** Crie-a na Braze em **Settings** > **APIs and Identifiers** > **API or interface de programação do aplicativo (API) Keys**. Conceda as permissões necessárias para essa integração (Campaigns, Canvas, Content Blocks e atributos personalizados).
- **Endpoint REST or transferir estado representacional da Braze:** Insira a URL da sua instância da Braze (por exemplo, `https://rest.iad-03.braze.com`). Para saber mais, consulte [Endpoints da REST or transferir estado representacional API or interface de programação do aplicativo (API)]({{site.baseurl}}/api/basics#endpoints).

![Página de chaves da REST API na Braze com Create API Key e o controle de cópia do REST Endpoint.]({% image_buster /assets/img/crowdin/braze_rest_api_keys.png %})

Selecione **Log in with Braze Campaigns & Canvas**.

### Etapa 3: Configurar o mapeamento de idiomas no Crowdin {#step-3-configure-language-mapping-in-crowdin}

Após conectar sua conta, mapeie cada idioma do projeto Crowdin para o locale correspondente na Braze.

1. No dashboard da integração **Braze Campaigns & Canvas**, selecione o ícone de engrenagem **Settings** na barra de ações superior.

![Tela da integração Braze Campaigns & Canvas com Settings na barra de ações superior.]({% image_buster /assets/img/crowdin/crowdin_campaigns_canvas_settings.png %})

{: start="2"}
2. Abra a guia **General Settings**.
3. Insira as chaves de locale. O Crowdin lista os idiomas do seu projeto (por exemplo, francês, italiano). Em cada campo, insira a **chave de locale da Braze** correspondente.
   - Por exemplo, se a Braze usa `it` para italiano, insira `it` ao lado de italiano no Crowdin.
   - Cada entrada deve corresponder exatamente à **Locale key** daquele locale nas **Localization Settings** da Braze.

![Modal de Settings na guia General Settings, mostrando campos de filtro de arquivos e linhas de mapeamento de idiomas (por exemplo, francês mapeado para fr).]({% image_buster /assets/img/crowdin/crowdin_language_mapping_settings.png %})

{: start="4"}
4. Selecione **Save** para confirmar o mapeamento.

### Etapa 4: Adicionar tags de tradução à sua mensagem na Braze {#step-4-add-translation-tags-to-your-braze-message}

O Crowdin lê as mesmas **tags de tradução** Liquid que a Braze usa para mensagens multilíngues. Adicione {% raw %}`{% translation your_id_here %}` e `{% endtranslation %}`{% endraw %} ao redor de cada trecho de texto, URL de imagem ou URL de link que você deseja traduzir. Cada bloco precisa de um `id` único (por exemplo, `greeting` ou `welcome_header`).

**Exemplo:**

{% raw %}`{% translation greeting %}Hello!{% endtranslation %}`{% endraw %}

Para HTML, Liquid em links e outros padrões, siga as mesmas regras de [Traduzindo locales]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages) (por exemplo, mantenha as tags ao redor dos menores segmentos possíveis e envolva apenas as partes específicas do idioma nas URLs ao localizar links).

Salve sua mensagem na Braze como **Draft** antes que o Crowdin possa detectar e puxar o conteúdo.

### Etapa 5: Gerenciar traduções no Crowdin {#step-5-manage-translations-in-crowdin}

A tela de integração tem dois lados:

- **Painel da Braze:** Suas Campaigns e Canvas.
- **Painel do Crowdin:** Conteúdo já sincronizado para tradução.

![Painéis do Crowdin e Braze Campaigns & Canvas com pastas para campanhas e locales, Sync to Braze e Sync to Crowdin.]({% image_buster /assets/img/crowdin/crowdin_campaigns_canvas_sync_panels.png %})

#### Sincronizando conteúdo {#syncing-content}

1. No painel da **Braze**, marque a caixa de seleção da Campaign ou Canvas que deseja traduzir.
2. Selecione **Sync to Crowdin**.
3. Quando a sincronização estiver concluída, o arquivo aparecerá no painel do **Crowdin**. Os tradutores podem abrir as strings no Crowdin Editor.

#### Enviando traduções de volta para a Braze {#returning-translations-to-braze}

1. Quando as traduções estiverem 100% concluídas no Crowdin, volte à guia **Integrations**.
2. Selecione o conteúdo concluído no painel do **Crowdin**.
3. Selecione **Sync to Braze**. Isso envia as strings traduzidas para as variantes de idioma correspondentes na sua Campaign na Braze.

### Etapa 6: Visualizar a mensagem como um usuário multilíngue na Braze {#step-6-preview-the-message-as-a-multi-language-user-in-braze}

Para confirmar a integração:

1. Abra sua Campaign no **Braze Message Composer**.
2. Acesse a guia **Test**.
3. Selecione **prévia Message as User**.
4. Pesquise um perfil de usuário que tenha um atributo `language` correspondente a um dos seus locales traduzidos.
5. Confirme que o conteúdo muda do idioma de origem para a versão traduzida.

## Integração de modelos de e-mail da Braze {#braze-email-templates-integration}

Se você localiza e-mails no nível do modelo, use o [app Braze Email Templates](https://store.crowdin.com/braze-app) para sincronizar HTML da sua biblioteca de mídia da Braze.

Para um tutorial em vídeo, consulte [Integração de modelos de e-mail da Braze](https://youtu.be/g0YMKW3jEjk).

### Etapa 1: Instalar o app {#step-1-install-the-app}

1. No seu projeto Crowdin, acesse a guia **Store**.
2. Pesquise por **Braze Email Templates** e selecione **Install**.

![Crowdin Store com Braze Email Templates selecionado e Install destacado.]({% image_buster /assets/img/crowdin/crowdin_store_email_templates.png %})

{: start="3"}
3. Selecione o projeto (ou projetos) em que você deseja usar essa integração.
4. Para abrir a integração, acesse **Integrations** > **Braze Email Templates** no seu projeto.

### Etapa 2: Conectar à Braze {#step-2-connect-to-braze}

Autorize a conexão com suas credenciais de API or interface de programação do aplicativo (API) da Braze:

![Formulário de conexão do Crowdin Braze Email Templates com chave da API REST, endpoint REST e Log in with Braze Email Templates.]({% image_buster /assets/img/crowdin/crowdin_email_templates_login.png %}){: style="max-width:85%;"}

1. **Chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze:** Conceda permissões de `templates.email` e `content_blocks` (leitura e gravação). Crie a chave na Braze em **Settings** > **APIs and Identifiers** > **API or interface de programação do aplicativo (API) Keys**.

![Página de chaves da API REST da Braze com Create API Key e o controle de cópia do endpoint REST.]({% image_buster /assets/img/crowdin/braze_rest_api_keys.png %})

{: start="2"}
2. Em **Braze REST or transferir estado representacional endpoint**, use a URL específica da sua instância (por exemplo, `https://rest.iad-03.braze.com`).
3. Selecione **Log in with Braze Email Templates**.

### Etapa 3: Sincronizar conteúdo para tradução {#step-3-sync-content-for-translation}

A tela de integração exibe sua biblioteca da Braze:

- **Painel Braze:** **Email Templates** e **Content Blocks** que você pode sincronizar.
- **Painel Crowdin:** Conteúdo em tradução.

1. No painel **Braze**, marque a caixa de seleção ao lado dos modelos ou blocos que você deseja localizar.
2. Selecione **Sync to Crowdin**.
3. O Crowdin puxa o HTML de origem. Os tradutores trabalham no Editor do Crowdin com uma prévia **WYSIWYG** em tempo real para que o layout permaneça intacto.

![Guia de prévia do Editor do Crowdin mostrando HTML de e-mail localizado e strings traduzíveis.]({% image_buster /assets/img/crowdin/crowdin_editor_wysiwyg_preview.png %}){: style="max-width:85%;"}

### Etapa 4: Entregar modelos traduzidos {#step-4-deliver-translated-templates}

Quando as traduções atingirem 100% de conclusão:

1. Selecione os arquivos concluídos no painel **Crowdin**.
2. Selecione **Sync to Braze**.
3. O Crowdin cria automaticamente versões localizadas desses ativos na sua biblioteca de mídia da Braze (por exemplo, `Template_Name_fr`).

![Painéis do Crowdin e Braze Email Templates listando Email Templates e Content Blocks, com Sync to Braze e Sync to Crowdin.]({% image_buster /assets/img/crowdin/crowdin_email_templates_sync_panels.png %})