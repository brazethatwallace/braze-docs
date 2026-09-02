### Pré-requisitos {#prerequisites}

Antes de usar este método de integração, você precisará [criar uma conta e um contêiner para o Google Tag Manager](https://support.google.com/tagmanager/answer/14842164).

### Etapa 1: Abra a galeria de modelos de tag {#step-1-open-the-tag-template-gallery}

No [Google Tag Manager](https://tagmanager.google.com/), escolha seu espaço de trabalho e selecione **Templates**. No painel **Tag Template**, selecione **Search Gallery**.

![A página de modelos para um espaço de trabalho de exemplo no Google Tag Manager.]({% image_buster /assets/img/web-gtm/search_tag_template_gallery.png %}){: style="max-width:95%;"}

### Etapa 2: Adicione o modelo de tag de inicialização {#step-2-add-the-initialization-tag-template}

Na galeria de modelos, procure por `braze-inc` e selecione **Braze Initialization Tag**.

![A galeria de modelos mostrando os vários modelos "braze-inc".]({% image_buster /assets/img/web-gtm/template_gallery_results.png %}){: style="max-width:80%;"}

Selecione **Add to workspace** > **Add**.

![A página "Braze Initialization Tag" no Google Tag Manager.]({% image_buster /assets/img/web-gtm/add_to_workspace.png %}){: style="max-width:70%;"}

### Etapa 3: Configure a tag {#step-3-configure-the-tag}

Na seção **Templates**, selecione o modelo recém-adicionado.

![A página "Templates" no Google Tag Manager mostrando o modelo Braze Initialization Tag.]({% image_buster /assets/img/web-gtm/select_tag_template.png %}){: style="max-width:95%;"}

Selecione o ícone de lápis para abrir o menu suspenso **Tag Configuration**.

![O bloco Tag Configuration com o ícone de "lápis" mostrado.]({% image_buster /assets/img/web-gtm/gtm-initialization-tag.png %})

Insira as informações mínimas necessárias:

| Campo         | Descrição |
| ------------- | ----------- |
| **API or interface de programação do aplicativo (API) Key**   | Sua [chave de API or interface de programação do aplicativo (API) da Braze]({{site.baseurl}}/api/basics#about-rest-api-keys), encontrada no dashboard da Braze em **Settings** > **App Settings**. |
| **API or interface de programação do aplicativo (API) Endpoint** | A URL do seu endpoint REST or transferir estado representacional. Seu endpoint dependerá da URL da Braze para [sua instância]({{site.baseurl}}/api/basics#endpoints). |
| **SDK or kit de desenvolvimento de software Version**  | A versão `MAJOR.MINOR` mais recente do SDK or kit de desenvolvimento de software Web da Braze listada no [changelog]({{site.baseurl}}/developer_guide/changelogs/?sdktab=web). Por exemplo, se a versão mais recente for `4.1.2`, digite `4.1`. Para saber mais, consulte [Sobre o gerenciamento de versões do SDK or kit de desenvolvimento de software]({{site.baseurl}}/developer_guide/sdk_integration/version_management). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Etapa 3: Configure a tag" }

Para configurações adicionais de inicialização, selecione **Braze Initialization Options** e escolha as opções que você precisar.

![A lista de Braze Initialization Options em "Tag Configuration".]({% image_buster /assets/img/web-gtm/braze_initialization_options.png %}){: style="max-width:65%;"}

### Etapa 4: Escolha as opções de inicialização {#step-4-choose-initialization-options}

A Braze Initialization Tag expõe as seguintes opções. A maioria delas mapeia diretamente para as [`InitializationOptions` do SDK or kit de desenvolvimento de software Web](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions), e algumas correspondem a métodos do SDK or kit de desenvolvimento de software Web que a tag chamará durante a inicialização. Selecione as opções que correspondem às suas necessidades de integração:

| Opção GTM | Configuração ou método do SDK or kit de desenvolvimento de software Web | Descrição |
| --- | --- | --- |
| **Allow HTML In-App Messages** | `allowUserSuppliedJavascript` | Ativa mensagens no app em HTML, Banners e ações de clique em JavaScript fornecidas pelo usuário. Necessário para [mensagens no app em HTML]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html) e [Banners]({{site.baseurl}}/developer_guide/banners/placements/?sdktab=web) que usam HTML personalizado. Ative isso apenas quando confiar no conteúdo HTML e JavaScript, pois permite a execução de JavaScript fornecido pelo usuário. |
| **App Version Number** | `appVersion`, `appVersionNumber` | Versão do app para segmentação (por exemplo, `1.2.3.4`). |
| **Automatically Open New Session** | `braze.openSession()` | Abre uma nova sessão após o SDK or kit de desenvolvimento de software ser inicializado, chamando este método automaticamente. |
| **Automatically show new in app messages** | `braze.automaticallyShowInAppMessages()` | Exibe automaticamente novas mensagens no app quando elas chegam do servidor, chamando este método após a inicialização. |
| **Disable Automatic token por push Maintenance** | `disablePushTokenMaintenance` | Impede que o SDK or kit de desenvolvimento de software sincronize tokens por push com o backend da Braze em novas sessões. |
| **Disable Automatic Service Worker Registration** | `manageServiceWorkerExternally` | Use se você registrar e controlar o service worker por conta própria. |
| **Disable Cookies** | `noCookies` | Usa localStorage em vez de cookies para dados de usuário/sessão. Impede o reconhecimento entre subdomínios. |
| **Disable Font Awesome** | `doNotLoadFontAwesome` | Impede que o SDK or kit de desenvolvimento de software carregue o Font Awesome da rede de distribuição de conteúdo (CDN). Use se seu site já tiver o Font Awesome. |
| **Enable SDK or kit de desenvolvimento de software Authentication** | `enableSdkAuthentication` | Ativa a [autenticação do SDK or kit de desenvolvimento de software]({{site.baseurl}}/developer_guide/sdk_integration/authentication). |
| **Enable Web SDK or kit de desenvolvimento de software Logging** | `enableLogging` | Ativa o registro no console para depuração. Remova antes de ir para produção. |
| **Minimum Interval Between Triggered Messages** | `minimumIntervalBetweenTriggerActionsInSeconds` | Segundos mínimos entre ações-gatilho (padrão: 30). |
| **Open Cards in New Tab** | `openCardsInNewTab` | Abre links de cartões de conteúdo em uma nova guia ao usar a interface padrão do feed. |
| **Service Worker Location** | `serviceWorkerLocation` | Caminho personalizado para o arquivo do service worker (padrão: `/service-worker.js`). |
| **Session Timeout (seconds)** | `sessionTimeoutInSeconds` | Tempo limite da sessão em segundos (padrão: 1800). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Etapa 4: Escolha as opções de inicialização" }

{% alert note %}
Para ativar [mensagens no app em HTML personalizado]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html) ao usar a Braze Initialization Tag no Google Tag Manager, selecione **Allow HTML In-App Messages** em **Braze Initialization Options**. Essa caixa de seleção mapeia para a opção de inicialização `allowUserSuppliedJavascript` em `braze.initialize()` e a define como `true`. A Braze Initialization Tag do Google Tag Manager usa esse rótulo em vez do nome da opção.
{% endalert %}

Para opções não expostas no modelo GTM (como `contentSecurityNonce`, `localization` ou `devicePropertyAllowlist`), use a [inicialização em tempo de execução]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web).

### Etapa 5: Defina para disparar em *todas as páginas* {#step-5-set-to-trigger-on-all-pages}

A tag de inicialização deve ser executada em todas as páginas do seu site. Isso permite que você use métodos do SDK or kit de desenvolvimento de software da Braze e registre análise de dados de web push.

{% alert important %}
**Sequenciamento de tags:** A Braze Initialization Tag deve ser disparada antes de qualquer outra tag que chame métodos do SDK or kit de desenvolvimento de software da Braze (como `braze.getUser()` ou `braze.logCustomEvent()`). Se eventos personalizados, atributos de usuário ou outras chamadas de métodos da Braze forem disparados antes de o SDK or kit de desenvolvimento de software ser inicializado, você poderá encontrar erros como `Uncaught TypeError: Cannot read properties of undefined (reading 'getUser')`. Para garantir o sequenciamento correto, configure sua Braze Initialization Tag como uma tag de configuração ou use o recurso de sequenciamento de tags do GTM para garantir que ela seja disparada primeiro. Para saber mais, consulte [Sequenciamento de tags para tags de ação da Braze]({{site.baseurl}}/developer_guide/sdk_integration/google_tag_manager/?sdktab=web#web_tag-sequencing-for-braze-action-tags).
{% endalert %}

### Etapa 6: Verifique sua integração {#step-6-verify-your-integration}

Você pode verificar sua integração usando qualquer uma das seguintes opções:

- **Opção 1:** Usando a [ferramenta de depuração](https://support.google.com/tagmanager/answer/6107056?hl=en) do Google Tag Manager, você pode verificar se a Braze Initialization Tag está disparando corretamente nas suas páginas ou eventos configurados.
- **Opção 2:** Verifique se há solicitações de rede feitas para a Braze a partir da sua página web. Além disso, a biblioteca global `window.braze` deve agora estar definida.