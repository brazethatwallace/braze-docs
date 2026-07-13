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

O Crowdin oferece dois apps para a Braze: [Braze Campaigns & Canvas](https://store.crowdin.com/braze-content-translation) e [Braze Email Templates](https://store.crowdin.com/braze-app). Escolha com base nos recursos da Braze que você localiza. A tabela a seguir compara os dois.

### Escolha o app certo do Crowdin {#choose-the-right-crowdin-app}

| Canal ou recurso | Braze Campaigns & Canvas | Braze Email Templates |
| --- | --- | --- |
| **Campaigns** | ✅ Compatível | ❌ Não compatível |
| **Etapas do Canvas** | ✅ Compatível | ❌ Não compatível |
| **Modelos de e-mail** | ❌ Não compatível | ✅ Compatível |
| **Content Blocks** | ❌ Não compatível | ✅ Compatível |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Escolha o app certo do Crowdin" }

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| --- | --- |
| **Conta do Crowdin** | É necessário ter uma [conta no Crowdin.com](https://accounts.crowdin.com/register) ou uma [conta no Crowdin Enterprise](https://accounts.crowdin.com/workspace/create). |
| **Projeto do Crowdin** | Antes de conectar a Braze, [crie um projeto de tradução](https://support.crowdin.com/creating-project/) no Crowdin ou no Crowdin Enterprise. |
| **Chave da API REST da Braze** | Uma chave da API REST da Braze com permissões para Campaigns, Canvas, Content Blocks, atributos personalizados, e-mail e modelos. |
| **Endpoint REST da Braze** | A URL específica do seu endpoint REST da Braze (por exemplo, `https://rest.iad-03.braze.com`). |
| **Configurações multilíngues da Braze** | Os locales devem estar configurados no dashboard da Braze em **Settings** > **Localization Settings**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração Braze Campaigns & Canvas {#braze-campaigns-canvas-integration}

Se você localiza conteúdo dentro de mensagens ativas, use o [app Braze Campaigns & Canvas](https://store.crowdin.com/braze-content-translation) para sincronizar strings traduzíveis dos rascunhos das suas Campaigns e Canvas com o suporte multilíngue da Braze.

Para um passo a passo em vídeo, consulte [Integração Braze Campaigns & Canvas](https://youtu.be/ahG1ET4VRKA).

### Etapa 1: Configure as definições multilíngues na Braze {#step-1-set-up-multi-language-settings-in-braze}

Antes de conectar o Crowdin, adicione seus idiomas de destino na Braze.

1. Na Braze, acesse **Settings** > **Localization Settings**.
2. Adicione os idiomas que você pretende suportar.

![Página de locales da Braze em Settings, mostrando nomes de locale, chaves de locale e Add locale.]({% image_buster /assets/img/crowdin/braze_locales.png %})

{: start="3"}
3. Anote cada **Locale key** (por exemplo, `en-US`, `fr-FR`, `es-ES`). Você usará esses valores ao mapear idiomas no Crowdin.

### Etapa 2: Configure o projeto da Braze no Crowdin {#step-2-set-up-the-braze-project-in-crowdin}

1. Na sua conta do Crowdin Enterprise ou Crowdin.com, acesse a **Store** no menu de navegação.
2. Pesquise por **Braze Campaigns & Canvas** e selecione **Install**.

![Crowdin Store com Braze Campaigns & Canvas selecionado e Install destacado.]({% image_buster /assets/img/crowdin/crowdin_store_campaigns_canvas.png %})

{: start="3"}
3. Selecione o projeto (ou projetos) onde deseja usar essa integração.
4. Para abrir a integração, acesse **Integrations** > **Braze Campaigns & Canvas** no seu projeto.

#### Conectando a Braze ao Crowdin {#connecting-braze-to-crowdin}

Autorize a conexão com suas credenciais de API da Braze:

![Formulário de conexão do Crowdin Braze Campaigns & Canvas com chave da API REST, endpoint REST e Log in with Braze Campaigns & Canvas.]({% image_buster /assets/img/crowdin/crowdin_campaigns_canvas_login.png %})

- **Braze REST API key:** Crie-a na Braze em **Settings** > **APIs and Identifiers** > **API Keys**. Conceda as permissões necessárias para essa integração (Campaigns, Canvas, Content Blocks e atributos personalizados).
- **Braze REST endpoint:** Insira a URL da sua instância da Braze (por exemplo, `https://rest.iad-03.braze.com`). Para saber mais, consulte [Endpoints da REST API]({{site.baseurl}}/api/basics#endpoints).

![Página de chaves da API REST da Braze com Create API Key e o controle de cópia do endpoint REST.]({% image_buster /assets/img/crowdin/braze_rest_api_keys.png %})

Selecione **Log in with Braze Campaigns & Canvas**.

### Etapa 3: Configure o mapeamento de idiomas no Crowdin {#step-3-configure-language-mapping-in-crowdin}

Após conectar sua conta, mapeie cada idioma do projeto Crowdin para o locale correspondente da Braze.

1. No painel da integração **Braze Campaigns & Canvas**, selecione o ícone de engrenagem **Settings** na barra de ações superior.

![Tela da integração Braze Campaigns & Canvas com Settings na barra de ações superior.]({% image_buster /assets/img/crowdin/crowdin_campaigns_canvas_settings.png %})

{: start="2"}
2. Abra a guia **General Settings**.
3. Insira as chaves de locale. O Crowdin lista os idiomas do seu projeto (por exemplo, francês, italiano). Em cada campo, insira a **chave de locale da Braze** correspondente.
   - Por exemplo, se a Braze usa `it` para italiano, insira `it` ao lado de italiano no Crowdin.
   - Cada entrada deve corresponder exatamente à **Locale key** daquele locale nas **Localization Settings** da Braze.

![Modal de configurações na guia General Settings, mostrando campos de filtro de arquivo e linhas de mapeamento de idiomas (por exemplo, francês mapeado para fr).]({% image_buster /assets/img/crowdin/crowdin_language_mapping_settings.png %})

{: start="4"}
4. Selecione **Save** para confirmar o mapeamento.

### Etapa 4: Adicione tags de tradução à sua mensagem na Braze {#step-4-add-translation-tags-to-your-braze-message}

O Crowdin lê as mesmas **tags de tradução** Liquid que a Braze usa para mensagens multilíngues. Adicione {% raw %}`{% translation your_id_here %}` e `{% endtranslation %}`{% endraw %} ao redor de cada trecho de texto, URL de imagem ou URL de link que você deseja traduzir. Cada bloco precisa de um `id` único (por exemplo, `greeting` ou `welcome_header`).

**Exemplo:**

{% raw %}`{% translation greeting %}Hello!{% endtranslation %}`{% endraw %}

Para HTML, Liquid em links e outros padrões, siga as mesmas regras descritas em [Traduzindo locales]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales) (por exemplo, mantenha as tags ao redor dos menores segmentos possíveis e envolva apenas as partes específicas do idioma nas URLs ao localizar links).

Salve sua mensagem na Braze como **Draft** antes que o Crowdin possa detectar e extrair o conteúdo.

### Etapa 5: Gerencie traduções no Crowdin {#step-5-manage-translations-in-crowdin}

A tela da integração tem dois lados:

- **Painel da Braze:** Suas Campaigns e Canvas.
- **Painel do Crowdin:** Conteúdo já sincronizado para tradução.

![Painéis do Crowdin e Braze Campaigns & Canvas com pastas para Campaigns e locales, Sync to Braze e Sync to Crowdin.]({% image_buster /assets/img/crowdin/crowdin_campaigns_canvas_sync_panels.png %})

#### Sincronizando conteúdo {#syncing-content}

1. No painel da **Braze**, marque a caixa de seleção da Campaign ou do Canvas que deseja traduzir.
2. Selecione **Sync to Crowdin**.
3. Quando a sincronização for concluída, o arquivo aparecerá no painel do **Crowdin**. Os tradutores podem abrir as strings no Editor do Crowdin.

#### Enviando traduções de volta para a Braze {#returning-translations-to-braze}

1. Quando as traduções estiverem 100% concluídas no Crowdin, volte à guia **Integrations**.
2. Selecione o conteúdo concluído no painel do **Crowdin**.
3. Selecione **Sync to Braze**. Isso envia as strings traduzidas para as variantes de idioma correspondentes na sua Campaign da Braze.

### Etapa 6: Visualize a mensagem como um usuário multilíngue na Braze {#step-6-preview-the-message-as-a-multi-language-user-in-braze}

Para confirmar a integração:

1. Abra sua Campaign no **criador de mensagens da Braze**.
2. Acesse a guia **Test**.
3. Selecione **Preview Message as User**.
4. Pesquise um perfil de usuário que tenha um atributo `language` correspondente a um dos seus locales traduzidos.
5. Confirme que o conteúdo muda do idioma de origem para a versão traduzida.

## Integração Braze Email Templates {#braze-email-templates-integration}

Se você localiza e-mails no nível do modelo, use o [app Braze Email Templates](https://store.crowdin.com/braze-app) para sincronizar HTML da sua biblioteca de mídia da Braze.

Para um passo a passo em vídeo, consulte [Integração Braze Email Templates](https://youtu.be/g0YMKW3jEjk).

### Etapa 1: Instale o app {#step-1-install-the-app}

1. No seu projeto do Crowdin, acesse a guia **Store**.
2. Pesquise por **Braze Email Templates** e selecione **Install**.

![Crowdin Store com Braze Email Templates selecionado e Install destacado.]({% image_buster /assets/img/crowdin/crowdin_store_email_templates.png %})

{: start="3"}
3. Selecione o projeto (ou projetos) onde deseja usar essa integração.
4. Para abrir a integração, acesse **Integrations** > **Braze Email Templates** no seu projeto.

### Etapa 2: Conecte-se à Braze {#step-2-connect-to-braze}

Autorize a conexão com suas credenciais de API da Braze:

![Formulário de conexão do Crowdin Braze Email Templates com chave da API REST, endpoint REST e Log in with Braze Email Templates.]({% image_buster /assets/img/crowdin/crowdin_email_templates_login.png %}){: style="max-width:85%;"}

1. **Braze REST API key:** Conceda permissões de `templates.email` e `content_blocks` (leitura e escrita). Crie a chave na Braze em **Settings** > **APIs and Identifiers** > **API Keys**.

![Página de chaves da API REST da Braze com Create API Key e o controle de cópia do endpoint REST.]({% image_buster /assets/img/crowdin/braze_rest_api_keys.png %})

{: start="2"}
2. Para o **Braze REST endpoint**, use a URL específica da sua instância (por exemplo, `https://rest.iad-03.braze.com`).
3. Selecione **Log in with Braze Email Templates**.

### Etapa 3: Sincronize conteúdo para tradução {#step-3-sync-content-for-translation}

A tela da integração mostra sua biblioteca da Braze:

- **Painel da Braze:** **Modelos de e-mail** e **Content Blocks** que você pode sincronizar.
- **Painel do Crowdin:** Conteúdo em tradução.

1. No painel da **Braze**, marque a caixa de seleção ao lado dos modelos ou blocos que deseja localizar.
2. Selecione **Sync to Crowdin**.
3. O Crowdin extrai o código-fonte HTML. Os tradutores trabalham no Editor do Crowdin com uma **prévia WYSIWYG** ao vivo para que o layout permaneça intacto.

![Guia de prévia do Editor do Crowdin mostrando HTML de e-mail localizado e strings traduzíveis.]({% image_buster /assets/img/crowdin/crowdin_editor_wysiwyg_preview.png %}){: style="max-width:85%;"}

### Etapa 4: Entregue os modelos traduzidos {#step-4-deliver-translated-templates}

Quando as traduções atingirem 100% de conclusão:

1. Selecione os arquivos concluídos no painel do **Crowdin**.
2. Selecione **Sync to Braze**.
3. O Crowdin cria automaticamente versões localizadas desses ativos na sua biblioteca de mídia da Braze (por exemplo, `Template_Name_fr`).

![Painéis do Crowdin e Braze Email Templates listando modelos de e-mail e Content Blocks, com Sync to Braze e Sync to Crowdin.]({% image_buster /assets/img/crowdin/crowdin_email_templates_sync_panels.png %})