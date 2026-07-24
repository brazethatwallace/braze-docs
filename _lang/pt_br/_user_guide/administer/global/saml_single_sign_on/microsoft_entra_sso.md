---
nav_title: Microsoft Entra SSO
article_title: Microsoft Entra SSO
page_order: 2
page_type: tutorial
description: "Este artigo mostra como configurar os recursos de login único do Microsoft Entra com a Braze."

---

# Microsoft Entra SSO {#microsoft-entra-sso}

> O [Microsoft Entra SSO](https://learn.microsoft.com/en-us/entra/identity/saas-apps/braze-tutorial) é o serviço de gerenciamento de identidade e acesso baseado em nuvem da Microsoft, que ajuda seus colaboradores a fazer login e acessar recursos. Você pode usar o Entra SSO para controlar o acesso aos seus apps e recursos de apps, com base nas necessidades do seu negócio.

## Requisitos {#requirements}

Durante a configuração, será solicitado que você forneça uma URL do Assertion Consumer Service (ACS).

| Requisito | Informações |
|---|---|
| URL do Assertion Consumer Service (ACS) | `https://<SUBDOMAIN>.braze.com/auth/saml/callback` <br> Para alguns provedores de identidade, isso também pode ser chamado de URL de resposta, URL de público ou URI de público. |
| ID da entidade | `braze_dashboard`|
| Chave de API RelayState | Para ativar o login do provedor de identidade, acesse **Configurações** > **Chaves de API** e crie uma chave de API com permissões `sso.saml.login`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos" }

## Login iniciado pelo prestador de serviço (SP) no Microsoft Entra SSO {#service-provider-sp-initiated-login-within-microsoft-entra-sso}

### Etapa 1: Adicionar a Braze a partir da galeria {#step-1-add-braze-from-the-gallery}

1. No centro de administração do Microsoft Entra, acesse **Identity** > **Applications** > **Enterprise Applications** e selecione **New application**.
2. Pesquise por **Braze** na caixa de pesquisa, selecione-a no painel de resultados e depois selecione **Add**.

### Etapa 2: Configurar o Microsoft Entra SSO {#step-2-configure-microsoft-entra-sso}

1. No centro de administração do Microsoft Entra, acesse a página de integração do aplicativo da Braze e selecione **Single sign-on**.
2. Na página **Select a single sign-on method**, selecione **SAML** como seu método.
3. Na página **Set up Single Sign-On with SAML**, selecione o ícone de edição para **Basic SAML Configuration**.
4. Configure o aplicativo no modo iniciado pelo IdP inserindo uma **Reply URL** que combine sua [instância da Braze]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints) com o seguinte padrão: `https://<SUBDOMAIN>.braze.com/auth/saml/callback`.
5. Configure o RelayState inserindo sua chave de API gerada para o Relay State no campo **Relay State**.

{% alert important %}
**Não** preencha o campo **Sign-On URL**. Deixe este campo em branco para evitar problemas com seu SAML SSO iniciado pelo IdP.
{% endalert %}

{: start="6"}
6. Formate as asserções SAML no formato específico esperado pela Braze. Consulte as guias a seguir sobre atributos de usuário e declarações de usuário para entender como esses atributos e valores devem ser formatados.

{% tabs %}
{% tab User Attributes %}
Você pode gerenciar os valores desses atributos na seção **User Attributes** da página **Application Integration**.

Use os seguintes pares de atributos:

- `givenname` = `user.givenname`
- `surname`= `user.surname`
- `emailaddress` = `user.mail`
- `name` = `user.userprincipalname`
- `email` = `user.userprincipalname`
- `first_name` = `user.givenname`
- `last_name` = `user.surname`
- `Unique User Identifier` = `user.userprincipalname`

{% alert important %}
É extremamente importante que o campo de e-mail corresponda ao que está configurado para seus usuários na Braze. Na maioria dos casos, será o mesmo que `user.userprincipalname`. No entanto, se você tiver uma configuração diferente, trabalhe com o administrador do sistema para garantir que esses campos correspondam exatamente.
{% endalert %}

{% endtab %}
{% tab User Claims %}

Na página **Set up Single Sign-On with SAML**, selecione **Edit** para abrir o diálogo **User Attributes**. Em seguida, edite as declarações de usuário de acordo com o formato adequado.

Use os seguintes pares de nomes de declaração:

- `claims/givenname` = `user.givenname`
- `claims/surname` = `user.surname`
- `claims/emailaddress` = `user.userprincipalname`
- `claims/name` = `user.userprincipalname`
- `claims/nameidentifier` = `user.userprincipalname`

{% alert important %}
É extremamente importante que o campo de e-mail corresponda ao que está configurado para seus usuários na Braze. Na maioria dos casos, será o mesmo que `user.userprincipalname`. No entanto, se você tiver uma configuração diferente, trabalhe com o administrador do sistema para garantir que esses campos correspondam exatamente.
{% endalert %}

Você pode gerenciar essas declarações e valores de usuário na seção **Manage claim**.

{% endtab %}
{% endtabs %}

{: start="8"}
8. Acesse a página **Set up Single Sign-On with SAML**, role até a seção **SAML Signing Certificate** e baixe o **Certificate (Base64)** apropriado com base nos seus requisitos.
9. Acesse a seção **Set up Braze** e copie as URLs apropriadas para uso na [configuração da Braze](#step-3).

### Etapa 3: Configurar o Microsoft Entra SSO na Braze {#step-3}

Depois de configurar a Braze no centro de administração do Microsoft Entra, o Microsoft Entra fornecerá uma URL de destino (URL de login) e um certificado **x.509** que você inserirá na sua conta da Braze.

Depois que o gerente da sua conta tiver ativado o SAML SSO para a sua conta, faça o seguinte:

1. Acesse **Configurações** > **Configurações de administrador** > **Configurações de segurança** e alterne a seção SAML SSO para **ATIVADO**.
2. Na mesma página, adicione o seguinte:

| Requisito | Informações |
|---|---|
| `SAML Name` | Isso aparecerá como o texto do botão na tela de login. Normalmente é o nome do seu provedor de identidade, como "Microsoft Entra". |
| `Target URL` | Esta é a URL de login fornecida pelo Microsoft Entra.|
| `Certificate` | O certificado `x.509` codificado em PEM é fornecido pelo seu provedor de identidade. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Etapa 3: Configurar o Microsoft Entra SSO na Braze" }

{% alert tip %}
Se você deseja que os usuários da sua conta da Braze façam login apenas com SAML SSO, você pode [restringir a autenticação de login único]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup#restriction) na página **Configurações da empresa**.
{% endalert %}