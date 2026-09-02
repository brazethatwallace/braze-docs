---
nav_title: Google tag manager
article_title: Google Tag Manager with the Braze SDK
platform:
  - Android
  - FireOS
  - Swift
page_order: 1.1
description: "Learn how to initialize the Braze SDK using methods like runtime initialization, delayed initialization, or Google Tag Manager."

---
## Sobre o Google Tag Manager para Web {#google-tag-manager}

O Google Tag Manager (GTM) permite que você adicione, remova e edite tags remotamente em seu site sem precisar de uma liberação de código de produção ou recursos de engenharia. A Braze oferece os seguintes modelos para o Web SDK:

| Tipo de tag | Caso de uso |
|--------|--------|
| Tag de inicialização | Essa tag permite que você [integre o Web Braze SDK]({{site.baseurl}}/developer_guide/sdk_integration/?tab=google%20tag%20manager&sdktab=web) sem precisar modificar o código do seu site. |
| Tag de ação | Essa tag permite que você [crie Content Cards]({{site.baseurl}}/developer_guide/content_cards/?sdktab=web#web_using-google-tag-manager), [defina atributos do usuário]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?tab=google%20tag%20manager&sdktab=web) e [gerencie a coleta de dados]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?tab=google%20tag%20manager&sdktab=web). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Sobre o Google Tag Manager para Web" }

## Sequenciamento de tags para tags de ação da Braze {#tag-sequencing-for-braze-action-tags}

A tag Braze Initialization deve ser disparada antes de qualquer tag que chame métodos do SDK da Braze (como `braze.getUser()`, `braze.logCustomEvent()` ou `braze.logPurchase()`). Se esses métodos forem disparados antes da inicialização do SDK, você poderá encontrar erros como `Uncaught TypeError: Cannot read properties of undefined (reading 'getUser')`.

Para configurar o sequenciamento de tags no Google Tag Manager:

1. Abra a tag que chama métodos do SDK da Braze (como uma tag HTML personalizada ou tag de ação da Braze).
2. Acesse **Advanced Settings** > **Tag Sequencing**.
3. Selecione **A tag that fires before [this tag] is fired**.
4. Escolha sua tag **Braze Initialization**.

Isso garante que o SDK esteja totalmente carregado antes que outras tags tentem chamar métodos da Braze.

Para saber mais, consulte [Verificar o sequenciamento de tags para eventos personalizados]({{site.baseurl}}/developer_guide/content_cards/?sdktab=web#web_tag-sequencing).

## Solução de problemas

### Sessões do Web SDK atribuídas ao usuário errado

Se o GTM disparar tags de inicialização ou de evento da Braze antes de o seu app identificar o usuário autenticado, sessões e eventos podem ser vinculados ao perfil errado. Inicialize o Web SDK, chame `changeUser()` com o `external_id` do usuário autenticado e, em seguida, chame `openSession()` antes de qualquer tag que registre eventos ou defina atributos. Use o sequenciamento de tags do GTM ou disparadores de consentimento para que as tags da Braze sejam executadas somente após a conclusão do fluxo de autenticação.

### Registro no console do Web SDK com Shopify ou instalações via tag de script

O app embed do Shopify carrega o Web SDK com o registro no console desativado. Defina o registro na tag de inicialização do GTM ou nas opções de `initialize()`. O dashboard da Braze não inclui um controle de registro para esses carregadores.

Se os logs da Braze aparecerem no console do navegador, remova `enableLogging: true` da tag de inicialização do GTM ou do HTML personalizado antes de publicar em produção. Após a inicialização, use `toggleLogging()` ou o parâmetro de URL `?brazeLogging=true`. Para ver todas as opções do Web SDK, consulte [Registro detalhado]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging).

Se a Braze não inicializar ou os eventos não aparecerem conforme esperado, confirme que o contêiner do GTM está publicado, que os disparadores e a ordem de execução das tags estão alinhados com a [estratégia de ciclo de vida e inicialização]({{site.baseurl}}/developer_guide/sdk_integration) do seu SDK, e que os dispositivos de teste não estão bloqueando os endpoints da Braze.

Para falhas de inicialização, verifique se a tag da Braze ou o provedor de tag personalizado recebe o `actionType` e os parâmetros esperados (consulte as guias Android, Swift e Web nesta página). Para obter registro detalhado ao validar eventos disparados pelo GTM, ative o registro de depuração do SDK da sua plataforma conforme descrito nos guias de integração vinculados nessas guias.