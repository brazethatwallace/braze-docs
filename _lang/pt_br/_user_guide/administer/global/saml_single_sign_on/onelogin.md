---
nav_title: OneLogin
article_title: OneLogin
page_order: 4
page_type: tutorial
description: "Este artigo explicará como configurar a Braze para usar o OneLogin para login único."

---

# OneLogin

> O [OneLogin](https://www.onelogin.com/) é uma plataforma de identidade em nuvem que fornece uma solução abrangente para o gerenciamento de identidades de usuários. O OneLogin se integra a aplicativos na nuvem e no local usando SAML 2.0, para login único (SSO), provisionamento de usuários, autenticação multifator e muito mais.

## Requisitos {#requirements}

Ao configurar, será solicitado que você forneça um URL de login e um URL do Assertion Consumer Service (ACS).

| Requisito | Detalhes |
|---|---|
| URL do Assertion Consumer Service (ACS) | `https://<SUBDOMAIN>.braze.com/auth/saml/callback` <br><br> Para domínios da União Europeia, o URL do ACS é `https://<SUBDOMAIN>.braze.eu/auth/saml/callback`. |
| Entity ID | `braze_dashboard` por padrão. Se o seu IdP exigir um Entity ID específico da empresa, ative **Custom Entity ID** em **Security Settings** e use `braze_dashboard_<companyID>`. |
| Domínio da Braze | Você precisará do seu domínio da Braze para configurar a Braze no OneLogin. Se a sua instância for `US-01`, será necessário inserir o URL do seu dashboard no dashboard do OneLogin. <br><br> Por exemplo, se o URL do seu dashboard for `https://dashboard-01.braze.com`, você precisará inserir `dashboard-01.braze.com`.  |
| Chave de API or interface de programação do aplicativo (API) do RelayState | Para ativar o login pelo IdP, acesse **Configurações** > **Configuração e teste** > **APIs e identificadores**, abra a guia **API or interface de programação do aplicativo (API) Keys** e crie uma chave de API or interface de programação do aplicativo (API) com permissões `sso.saml.login`. Para ver as etapas, consulte [Configurando seu RelayState]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup#setting-up-your-relaystate). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos" }

## Login iniciado pelo IdP no OneLogin {#idp-initiated-login-within-onelogin}

### Etapa 1: Configurar o app da Braze {#step-1-configure-the-braze-app}

1. Faça login no [OneLogin](https://app.onelogin.com/login). Clique em **Administration**.![Página de administração do OneLogin.]({% image_buster /assets/img/onelogin_1.jpg %})<br><br>
2. Acesse **Apps** > **Add Apps** na barra de navegação superior. Pesquise por "Braze" e selecione o app da Braze.![Resultados de pesquisa para Braze no OneLogin.]({% image_buster /assets/img/onelogin_2.jpg %})<br><br>
3. Salve o app da Braze na sua empresa.![Salve o app da Braze na sua empresa no OneLogin.]({% image_buster /assets/img/onelogin_3.jpg %})<br><br>
4. Após salvar, acesse **Configuration** e adicione o seu **Braze Domain** e a chave de API **RelayState**. Se o seu IdP exigir um Entity ID específico da empresa, configure também a **ACS URL** (`https://<SUBDOMAIN>.braze.com/auth/saml/callback`) e o Entity ID na [configuração de SAML SSO]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup#requirements).![Guia de configuração do OneLogin para o app da Braze.]({% image_buster /assets/img/onelogin_4.png %})<br><br>
5. A Braze espera as asserções SAML em um [formato específico]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup#step-1-configure-your-identity-provider). Em **Parameters**, os atributos compatíveis com a Braze já devem estar preenchidos. Verifique se estão corretos.![Parâmetros SAML da Braze no OneLogin.]({% image_buster /assets/img/onelogin_5.jpg %})<br><br>
6. Copie o **Certificate** e o **SAML 2.0 Endpoint (HTTP)** necessários para configurar o dashboard da Braze na guia **SSO**.![Certificados para copiar na guia SSO do app da Braze no OneLogin.]({% image_buster /assets/img/onelogin_6.jpg %})

### Etapa 2: Configurar o OneLogin na Braze {#step-2-configure-onelogin-within-braze}

Depois de configurar a Braze no seu OneLogin, eles fornecerão uma URL de destino (`SAML 2.0 Endpoint (HTTP)`) e um certificado `x.509` para inserir na sua conta da Braze.

Após o gerente da sua conta ativar o SAML SSO para a sua conta, acesse **Configurações** > **Configurações da empresa** > **Configurações de administrador** > **Configurações de segurança** e alterne a seção SAML SSO para **ATIVADO**.

Nesta página, insira o seguinte:

| Requisito | Detalhes |
|---|---|
| `SAML Name` | Isso aparecerá como o texto do botão na tela de login. Normalmente é o nome do seu provedor de identidade, como "OneLogin". |
| `Target URL` | Esta é a URL `SAML 2.0 Endpoint (HTTP)` fornecida pelo OneLogin. |
| `Certificate` | O certificado `x.509` codificado em PEM é fornecido pelo seu OneLogin. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Etapa 2: Configurar o OneLogin na Braze" }

Se o seu IdP exigir um Entity ID específico da empresa, ative **Custom Entity ID** em **Configurações de segurança**, copie o valor gerado e cole-o no campo Entity ID do OneLogin. Consulte [Custom Entity ID]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup#custom-entity-id) no artigo de configuração de SAML SSO.

![Configurações de SAML SSO com o botão de alternância selecionado.]({% image_buster /assets/img/samlsso.png %})

{% alert tip %}
Se você deseja que os usuários da sua conta da Braze façam login apenas com SAML SSO, é possível [restringir a autenticação por login único]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup#restriction) em **Configurações** > **Configurações da empresa** > **Configurações de administrador** > **Configurações de segurança**.
{% endalert %}

## Próximas etapas {#next-steps}

Depois que o SSO do OneLogin estiver funcionando:

- [Exija login somente por SAML SSO]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup#restriction) se o login por senha precisar ser desativado.
- [Configure o provisionamento just-in-time de SAML]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_just_in_time_provisioning) para criar automaticamente usuários do dashboard no primeiro login pelo IdP.
- Use [Obtendo um rastreamento SAML]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup#obtaining-a-saml-trace) se os usuários encontrarem erros de login.