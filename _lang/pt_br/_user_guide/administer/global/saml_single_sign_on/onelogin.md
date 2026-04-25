---
nav_title: OneLogin
article_title: OneLogin
page_order: 4
page_type: tutorial
description: "Este artigo explicará como configurar a Braze para usar o OneLogin para logon único."

---

# OneLogin

> [O OneLogin](https://www.onelogin.com/) é uma plataforma de identidade em nuvem que fornece uma solução abrangente para o gerenciamento de identidades de usuários. O OneLogin se integra a aplicativos na nuvem e no local usando SAML 2.0, para logon único (SSO), provisionamento de usuários, autenticação multifator e muito mais.

## Requisitos

Após a configuração, solicitaremos que você forneça uma URL de login e um URL do Assertion Consumer Service (ACS).

| Requisito | Informações |
|---|---|
| Domínio Braze | Você precisará de seu domínio Braze para configurar a Braze no OneLogin. Se a sua instância for `US-01`, será necessário inserir o URL do painel no painel do OneLogin. <br><br> Por exemplo, se o URL do seu dashboard for `https://dashboard-01.braze.com`, você precisará inserir `dashboard-01.braze.com`.  |
| Chave de API do RelayState | Para ativar o login IdP, Acessar **Configurações** > **Chaves de API** e criar uma chave de API com permissões de `sso.saml.login`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Login iniciado por IdP no OneLogin

### Etapa 1: Configurar o app Braze

1. Faça o registro no [OneLogin](https://app.onelogin.com/login). Clique em **Administration**.![Página de administração do OneLogin.]({% image_buster /assets/img/onelogin_1.jpg %})<br><br>
2. Acesse **Apps** > **Add Apps** na barra de navegação superior. Pesquise por "Braze" e selecione o app Braze.![Resultados da pesquisa por Braze no OneLogin.]({% image_buster /assets/img/onelogin_2.jpg %})<br><br>
3. Salve o app Braze na sua empresa.![]({% image_buster /assets/img/onelogin_3.jpg %})<br><br>
4. Após salvar, acesse **Configuration** e adicione seu **Braze Domain** e a chave de API do **RelayState**.![Guia de configuração do OneLogin para o app Braze.]({% image_buster /assets/img/onelogin_4.png %})<br><br>
5. A Braze espera as asserções SAML em um [formato específico]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup/#configure-your-identity-provider). Em **Parameters**, os atributos compatíveis com a Braze já devem estar preenchidos. Verifique se estão corretos.![Parâmetros SAML da Braze no OneLogin.]({% image_buster /assets/img/onelogin_5.jpg %})<br><br>
6. Copie o **Certificate** e o **SAML 2.0 Endpoint (HTTP)** necessários para configurar o dashboard da Braze na guia **SSO**.![Certificados para copiar da guia SSO do app Braze no OneLogin.]({% image_buster /assets/img/onelogin_6.jpg %})

### Etapa 2: Configurar o OneLogin na Braze

Depois de configurar a Braze no OneLogin, eles fornecerão uma URL de destino (`SAML 2.0 Endpoint (HTTP)`) e um certificado `x.509` que você inserirá na sua conta Braze.

Após o gerente da sua conta ativar o SAML SSO para a sua conta, acesse **Configurações** > **Configurações de administrador** > **Configurações de segurança** e alterne a seção SAML SSO para **ATIVADO**.

Nesta página, insira o seguinte:

| Requisito | Informações |
|---|---|
| `SAML Name` | Isso aparecerá como o texto do botão na tela de login. Normalmente é o nome do seu provedor de identidade, como "OneLogin". |
| `Target URL` | Este é o URL `SAML 2.0 Endpoint (HTTP)` fornecido pelo OneLogin.|
| `Certificate` | O certificado `x.509` codificado em PEM é fornecido pelo seu OneLogin. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Configurações de SAML SSO com o botão de alternância selecionado.]({% image_buster /assets/img/samlsso.png %})

{% alert tip %}
Se você deseja que os usuários da sua conta Braze façam login apenas com SAML SSO, é possível [restringir a autenticação de login único]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup/#restriction) na página de **Configurações da empresa**.
{% endalert %}