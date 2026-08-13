---
nav_title: Provisionamento automatizado de usuários
article_title: Provisionamento automatizado de usuários
page_order: 3
page_type: reference
description: "Este artigo de referência aborda as informações que precisam ser fornecidas para o provisionamento automatizado de usuários e como e onde usar o token gerado pelo System for Cross-domain Identity Management (SCIM)."
alias: /scim/automated_user_provisioning/

---

# Provisionamento automatizado de usuários {#automated-user-provisioning}

> O provisionamento automatizado de usuários permite criar e gerenciar usuários da Braze por meio de uma API, em vez de fazer isso manualmente no dashboard. A Braze oferece suporte a isso por meio do System for Cross-domain Identity Management (SCIM). Este artigo orienta você sobre quais informações fornecer, como gerar seu token SCIM e onde encontrar seu endpoint da API SCIM.

{% multi_lang_include scim/scim_alerts.md alert='one_integration' %}

## Acessando as configurações de provisionamento SCIM {#accessing-scim-provisioning-settings}

{% alert important %}
A disponibilidade do provisionamento SCIM depende da sua edição da plataforma. Se esse recurso não estiver no seu espaço de trabalho, entre em contato com o seu gerente de sucesso do cliente para mais informações.
{% endalert %}

1. No dashboard da Braze, acesse **Configurações** > **Configuração de administrador** > **Provisionamento SCIM** e selecione **Configurar integração SCIM**.
2. Na etapa **Configuração da Braze**, selecione um método de provisionamento e forneça as configurações de acesso.

![Uma página para configurar a integração SCIM com seções para selecionar um método de provisionamento e fornecer configurações de acesso.]({% image_buster /assets/img_archive/scim_braze_config.png %}){: style="max-width:70%;"}

{: start="3"}
3. Na etapa **Configuração do IdP**, siga as etapas dentro da plataforma para o método de provisionamento selecionado.

{% tabs %}
{% tab Okta - Braze app %}

{% multi_lang_include alerts/early_access_beta_alert.md feature='The Okta integration' %}

Use a opção **Okta - Braze app** se você configurou o app da Braze para SAML SSO no Okta. Se você configurou um app personalizado para SSO, siga as instruções na guia [Okta - Custom app integration]({{site.baseurl}}/user_guide/administer/global/user_management/automated_user_provisioning?tab=okta%20-%20custom%20app%20integration#step-1-set-up-scim-provisioning).

{% multi_lang_include scim/scim_alerts.md alert='idp_integration' idp='Okta' %}

## Etapa 1: Configurar o provisionamento SCIM {#step-1-set-up-scim-provisioning}

### Etapa 1.1: Ativar o SCIM {#step-11-enable-scim}

1. No Okta, acesse **Applications** > **Applications** e selecione **Create App Integration**. Selecione **SAML 2.0** como o método de login.
2. Preencha os seguintes detalhes (que estão localizados na [etapa **Configuração do IdP**](#accessing-scim-provisioning-settings) da Braze) para criar um app personalizado:
- Logo do app
- Single sign-on URL
- Audience URL (SP entity ID)
3. Selecione **Finish**.
4. Selecione a guia **General**.
5. Na seção **App Settings**, selecione **Edit**.
6. No campo **Provisioning**, selecione **SCIM**.

### Etapa 1.2: Desativar a visibilidade do aplicativo {#step-12-disable-application-visibility}

1. No campo **Application visibility**, marque a caixa de seleção **Do not display application icon to user**. Isso impede que os usuários acessem o SSO pelo app, que é destinado exclusivamente ao SCIM.
2. Selecione **Save**.

### Etapa 1.3: Configurar a integração SCIM {#step-13-set-up-the-scim-integration}

1. Selecione a guia **Provisioning**.
2. Em **Settings** > **Integration** > **SCIM Connection**, selecione **Edit** e preencha os valores dos campos que aparecem na tabela da página **Setup SCIM provisioning**.

### Etapa 1.4: Testar as credenciais da API {#step-14-test-the-api-credentials}

Selecione **Test API Credentials**. Uma mensagem de verificação aparecerá se a integração for bem-sucedida e você poderá salvar.

### Etapa 1.5: Ativar o provisionamento para o app {#step-15-enable-provisioning-to-the-app}

1. Em **Provisioning** > **Settings** > **To App** > **Provisioning to App**, selecione **Edit**.
2. Ative o seguinte:
    - Create Users
    - Update Users Attributes
    - Deactivate Users
3. Revise e configure a seção **Attribute Mapping** com os mapeamentos que aparecem na tabela da página **Setup SCIM provisioning**.

## Etapa 2: Atribuir usuários ao app {#step-2-assign-users-to-the-app}

1. Selecione a guia **Assignment**.
2. Selecione **Assign** e escolha uma opção.
3. Atribua o app às pessoas que devem ter acesso à Braze.
4. Selecione **Done** quando tiver concluído a atribuição.

{% endtab %}
{% tab Okta - Custom app integration %}

{% multi_lang_include alerts/early_access_beta_alert.md feature='The Okta integration' %}

Use a opção **Okta - Custom app integration** se você configurou um app personalizado para SSO. Se você configurou o app da Braze para SAML SSO no Okta, siga as instruções na guia [Okta - Braze app]({{site.baseurl}}/user_guide/administer/global/user_management/automated_user_provisioning?tab=okta%20-%20braze%20app#step-1-set-up-scim-provisioning).

{% multi_lang_include scim/scim_alerts.md alert='idp_integration' idp='Okta' %}

## Etapa 1: Configurar o provisionamento SCIM

### Etapa 1.1: Ativar o SCIM

1. No Okta, acesse o seu app da Braze.
2. Selecione a guia **General**.
3. Na seção **App Settings**, selecione **Edit**.
4. No campo **Provisioning**, selecione **SCIM**.
5. Selecione **Save**.

### Etapa 1.2: Configurar a integração SCIM {#step-12-set-up-scim-integration}

1. Selecione a guia **Provisioning**.
2. Em **Settings** > **Integration** > **SCIM Connection**, selecione **Edit** e preencha os valores dos campos que aparecem na tabela da página **Setup SCIM provisioning**.
3. Teste as credenciais da API selecionando **Test API Credentials**.
4. Selecione **Save**.

### Etapa 1.3: Ativar o provisionamento para o app {#step-13-enable-provisioning-to-the-app}

1. Em **Provisioning** > **Settings** > **To App** > **Provisioning to App**, selecione **Edit**.
2. Ative o seguinte:
    - Create Users
    - Update Users Attributes
    - Deactivate Users
3. Revise e configure a seção **Attribute Mapping** com os mapeamentos que aparecem na tabela da página **Setup SCIM provisioning**.

## Etapa 2: Atribuir usuários ao app

1. Selecione a guia **Assignment**.
2. Selecione **Assign** e escolha uma opção.
3. Atribua o app às pessoas que devem ter acesso à Braze.
4. Selecione **Done**.

{% endtab %}
{% tab Entra ID %}

{% multi_lang_include alerts/early_access_beta_alert.md feature='The Entra ID integration' %}

{% multi_lang_include scim/scim_alerts.md alert='idp_integration' idp='Entra ID' %}

## Etapa 1: Configurar o app de provisionamento SCIM {#step-1-set-up-scim-provisioning-app}

### Etapa 1.1: Fazer login no centro de administração do Microsoft Entra {#step-11-log-into-microsoft-entra-admin-center}

Faça login no centro de administração do Microsoft Entra.

### Etapa 1.2: Criar e configurar o app SCIM {#step-12-create-and-set-up-your-scim-app}

1. No menu de navegação, acesse **Entra ID** > **Enterprise apps**.
2. Selecione **New application**.
3. Selecione **Create your own application**.
4. No painel, insira um nome para o seu app.
5. Na seção **What are you looking to do with your application?**, selecione **Integrate application you don't find in the gallery (Non-gallery)**.
6. Selecione **Create**.

### Etapa 1.3: Configurar a integração SCIM {#step-13-set-up-scim-integration}

1. Acesse a seção **Manage** > **Provisioning** do seu aplicativo SCIM.
2. Selecione **Connect your application** ou **New configuration** e preencha os valores dos campos que aparecem na tabela da página **Setup SCIM provisioning**.

### Etapa 1.4: Ativar o provisionamento para o app {#step-14-enable-provisioning-to-the-app}

1. Acesse a seção **Manage** > **Attribute mapping (Preview)** do seu aplicativo SCIM.
2. Selecione **Provision Microsoft Entra ID Users**.
3. Revise e configure a seção **Attribute Mapping** para corresponder aos atributos que aparecem na tabela da página **Setup SCIM provisioning**.
4. Feche a página **Attribute Mapping**.

{% alert important %}
O atributo `userName` deve corresponder exatamente ao endereço de e-mail do usuário na Braze para que o SCIM identifique e gerencie os usuários corretamente. Usuários que foram provisionados manualmente na Braze antes da ativação do SCIM não serão convertidos automaticamente em usuários gerenciados pelo IdP, mesmo que sejam adicionados ao aplicativo SCIM. O método de provisionamento deles permanece manual.
{% endalert %}

## Etapa 2: Atribuir usuários ao app

1. Acesse **Manage** > **Users and Groups**.
2. Selecione **Add user/group**.
3. Selecione **None Selected** para atribuir usuários ao app.
4. Selecione o botão **Select** para confirmar a atribuição.

{% endtab %}
{% tab Custom %}

## Etapa 1: Configurar as definições do SCIM {#step-1-configure-your-scim-settings}

- **Espaço de trabalho padrão:** selecione o espaço de trabalho onde novos usuários devem ser adicionados por padrão. Se você não especificar um espaço de trabalho na sua [solicitação da API SCIM]({{site.baseurl}}/post_create_user_account), a Braze atribuirá os usuários a esse espaço de trabalho.
- **Service Origin:** insira o domínio de origem das suas solicitações SCIM. A Braze usa isso no cabeçalho `X-Request-Origin` para verificar a origem das solicitações.
- **Lista de IPs permitidos (opcional):** você pode restringir as solicitações SCIM a endereços IP específicos. Insira uma lista separada por vírgulas ou um intervalo de endereços IP a serem permitidos. O cabeçalho `X-Request-Origin` em cada solicitação é usado para verificar o endereço IP da solicitação em relação à lista de permitidos.

## Etapa 2: Gerar um token SCIM {#step-2-generate-a-scim-token}

Após preencher os campos obrigatórios, pressione **Generate SCIM token** para gerar um token SCIM e ver o endpoint da API SCIM. Certifique-se de copiar o token SCIM antes de sair da página. **Este token aparece apenas uma vez.**

![Campos de endpoint da API SCIM e token SCIM exibidos com valores mascarados e botões de cópia. Abaixo do campo de token há um botão "Reset Token".]({% image_buster /assets/img/scim.png %})

A Braze espera que todas as solicitações SCIM contenham o token bearer da API SCIM anexado por meio de um cabeçalho HTTP `Authorization`.

{% endtab %}
{% endtabs %}