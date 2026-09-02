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

Ao configurar, será solicitado que você forneça uma URL do Assertion Consumer Service (ACS).

| Requisito | Detalhes |
|---|---|
| URL do Assertion Consumer Service (ACS) | `https://<SUBDOMAIN>.braze.com/auth/saml/callback` <br> Para alguns provedores de identidade, isso também pode ser chamado de URL de resposta, URL de público ou URI de público. |
| Entity ID | `braze_dashboard` por padrão. <br><br> Para dar a esse dashboard um Entity ID exclusivo, ative um Entity ID personalizado e use o valor gerado (`braze_dashboard_<COMPANY_ID>`). Para ver as etapas, consulte [Usar um Entity ID personalizado]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup#using-a-custom-entity-id). |
| Chave de API or interface de programação do aplicativo (API) RelayState | Para ativar o login pelo provedor de identidade, acesse **Configurações** > **Chaves de API or interface de programação do aplicativo (API)** e crie uma chave de API or interface de programação do aplicativo (API) com permissões `sso.saml.login`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos" }

## Login iniciado pelo provedor de serviço (SP) no SSO do Microsoft Entra {#service-provider-sp-initiated-login-within-microsoft-entra-sso}

### Etapa 1: Adicionar a Braze na galeria {#step-1-add-braze-from-the-gallery}

1. No centro de administração do Microsoft Entra, acesse **Identity** > **Applications** > **Enterprise Applications** e selecione **New application**.
2. Pesquise por **Braze** na caixa de pesquisa, selecione-a no painel de resultados e depois selecione **Add**.

### Etapa 2: Configurar o SSO do Microsoft Entra {#step-2-configure-microsoft-entra-sso}

1. No centro de administração do Microsoft Entra, acesse a página de integração do aplicativo Braze e selecione **Single sign-on**.
2. Na página **Select a single sign-on method**, selecione **SAML** como método.
3. Na página **Set up Single Sign-On with SAML**, selecione o ícone de edição em **Basic SAML Configuration**.
4. Configure o aplicativo no modo iniciado pelo IdP inserindo uma **Reply URL** que combine sua [instância da Braze]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints) com o seguinte padrão: `https://<SUBDOMAIN>.braze.com/auth/saml/callback`.
5. Na mesma seção **Basic SAML Configuration**, deixe o campo **Identifier (Entity ID)** definido como `braze_dashboard`, a menos que esteja usando um [Entity ID personalizado]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup#using-a-custom-entity-id). Nesse caso, insira o valor gerado pelo seu dashboard (`braze_dashboard_<COMPANY_ID>`) para que ele corresponda ao valor exibido nas configurações de segurança da Braze.
6. Configure o RelayState inserindo a chave de API or interface de programação do aplicativo (API) do Relay State gerada no campo **Relay State**.

{% alert important %}
**Não** defina o campo **Sign-On URL**. Deixe esse campo em branco para evitar problemas com o SSO SAML iniciado pelo IdP.
{% endalert %}

{: start="7"}
7. Formate as asserções SAML no formato específico esperado pela Braze. Consulte as guias a seguir sobre atributos de usuário e declarações de usuário para entender como esses atributos e valores devem ser formatados.

{% tabs %}
{% tab User Attributes %}
Você pode gerenciar os valores desses atributos na seção **User Attributes** na página **Application Integration**.

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
O campo de e-mail deve corresponder ao que está configurado para seus usuários na Braze. Na maioria dos casos, é o mesmo que `user.userprincipalname`. No entanto, se você tiver uma configuração diferente, trabalhe com o administrador do sistema para garantir que esses campos correspondam exatamente.
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
O campo de e-mail deve corresponder ao que está configurado para seus usuários na Braze. Na maioria dos casos, é o mesmo que `user.userprincipalname`. No entanto, se você tiver uma configuração diferente, trabalhe com o administrador do sistema para garantir que esses campos correspondam exatamente.
{% endalert %}

Você pode gerenciar essas declarações e valores de usuário na seção **Manage claim**.

{% endtab %}
{% endtabs %}

{: start="8"}
8. Acesse a página **Set up Single Sign-On with SAML**, role até a seção **SAML Signing Certificate** e baixe o **Certificate (Base64)** apropriado com base nas suas necessidades.
9. Acesse a seção **Set up Braze** e copie as URLs apropriadas para uso na [configuração da Braze](#step-3).

### Etapa 3: Configurar o SSO do Microsoft Entra na Braze {#step-3}

Depois de configurar a Braze no centro de administração do Microsoft Entra, o Microsoft Entra fornece uma URL de destino (URL de login) e um certificado **x.509**, que você insere na sua conta da Braze.

Após o gerente da sua conta ativar o SSO SAML para a sua conta, faça o seguinte:

1. Acesse **Configurações** > **Configurações da empresa** > **Configurações de administrador** > **Configurações de segurança** e alterne a seção SSO SAML para **ATIVADO**.
2. Na mesma página, adicione o seguinte:

| Requisito | Detalhes |
|---|---|
| `SAML Name` | Isso aparecerá como o texto do botão na tela de login. Normalmente, é o nome do seu provedor de identidade, como "Microsoft Entra". |
| `Target URL` | Esta é a URL de login fornecida pelo Microsoft Entra. |
| `Certificate` | O certificado `x.509` codificado em PEM é fornecido pelo seu provedor de identidade. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Etapa 3: Configurar o SSO do Microsoft Entra na Braze" }

{% alert tip %}
Se você deseja que os usuários da sua conta da Braze façam login apenas com SSO SAML, é possível [restringir a autenticação de logon único]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup#restriction) na página **Configurações de segurança** em **Regras de autenticação**.
{% endalert %}