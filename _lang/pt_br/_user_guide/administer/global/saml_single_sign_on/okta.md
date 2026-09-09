---
nav_title: Okta
article_title: Okta
page_order: 3
page_type: tutorial
description: "Este artigo orientará sobre como configurar a Braze para usar o Okta para login único."

---

# Okta

> O Okta conecta qualquer pessoa a qualquer aplicativo em qualquer dispositivo. É um serviço de gerenciamento de identidade de nível empresarial, construído para a nuvem, mas compatível com muitos aplicativos locais. Com o Okta, sua equipe de TI pode gerenciar o acesso de qualquer colaborador a qualquer aplicativo ou dispositivo.

{% alert note %}
O app pré-configurado da Braze no marketplace do Okta usa o Entity ID compartilhado `braze_dashboard`. Se você precisar de um Entity ID exclusivo para este dashboard — por exemplo, para conectar vários dashboards da Braze por meio do Okta — configure um app SAML personalizado em vez do app do marketplace e siga as instruções em [Usar um Entity ID personalizado]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup#using-a-custom-entity-id).
{% endalert %}

## Requisitos {#requirements}

| Requisito | Detalhes |
| ----------- | ------- |
| Okta ativada para sua conta | Entre em contato com o gerente de conta da Braze para ativar isso em sua conta. |
| Privilégios de administrador na Okta | Certifique-se de que você tem privilégios de administrador antes de configurar a Okta. |
| Privilégios de administrador na Braze | Certifique-se de que você tem privilégios de administrador antes de configurar a Okta. |
| Chave de API RelayState | Para ativar o login por IdP, acesse **Configurações** > **Configuração e teste** > **APIs e identificadores**, abra a guia **API Keys** e crie uma chave de API com permissões `sso.saml.login`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos" }

## Etapa 1: Configurar a Braze {#step-1-configure-braze}

### Etapa 1a: Acessar as configurações de segurança na Braze {#step-1a-navigate-to-security-settings-in-braze}

Depois que o gerente de conta tiver ativado o SSO SAML para a sua conta, acesse **Configurações** > **Configurações de administrador** > **Configurações de segurança** e alterne a seção SSO SAML para **ON**.

![SSO SAML da Okta ativado na página de configurações de segurança.]({% image_buster/assets/img/Okta/okta1.png %})

### Etapa 1b: Editar as configurações de SSO SAML {#step-1b-edit-saml-sso-settings}

No dashboard de administração da Okta, a Okta fornece um URL de destino (URL de login) e um certificado `x.509`, que você deve inserir na página **Configurações de segurança** da sua conta Braze.

![Captura de tela relacionada à etapa 1b: editar configurações de SSO SAML.]({% image_buster /assets/img/Okta/okta5.png %}){: style="max-width:75%"}

| Requisito | Detalhes |
|---|---|
| `SAML Name` | Aparecerá como o texto do botão na tela de login. Normalmente é o nome do seu provedor de identidade. Por exemplo, "Okta". |
| `Target URL` | Este é o URL de login fornecido pelo dashboard de administração da Okta. Encontre-o acessando **Applications** > seu aplicativo > guia **General** > **App Embed Link** > **Embed Link**. |
| `Certificate` | O certificado `x.509` codificado em PEM é fornecido pelo seu provedor de identidade. Você deve copiá-lo e colá-lo neste campo. Recupere-o na Okta acessando **SAML Signing Certificates** e selecionando **Actions** > **Download certificate**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Etapa 1b: Editar as configurações de SSO SAML" }

Selecione **Save Changes** na parte inferior da página quando terminar.

{% alert note %}
Se o seu provedor de identidade exigir um Entity ID SAML específico da empresa e a sua conta oferecer suporte para isso, ative **Custom Entity ID** em **Configurações de segurança** e configure a Okta com `braze_dashboard_<companyID>`. O Entity ID padrão é `braze_dashboard`. A configuração **Custom Entity ID** não está disponível para todas as empresas. Para saber mais, consulte [Configuração de SSO SAML]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup#requirements).
{% endalert %}

## Etapa 2: Configurar a Okta {#step-2-configure-okta}

Na Okta, selecione a guia **Sign On** para o app SAML da Braze e clique em **Edit**.

Em seguida, insira a chave de API do RelayState com a permissão `sso.saml.login` no campo **Default Relay State**.

![RelayState padrão da Okta na guia Sign On.]({% image_buster /assets/img/Okta/okta2.png %}){: style="max-width:75%"}

Certifique-se de salvar essas novas configurações.

{% alert tip %}
Se você quiser que os usuários da sua conta Braze façam login apenas com SAML SSO, é possível [restringir a autenticação de logon único]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup#restriction) em **Configurações** > **Configurações da empresa** > **Configurações de administrador** > **Configurações de segurança**.
{% endalert %}

## Etapa 3: Fazer login {#step-3-log-in}

Agora você deve conseguir fazer login na Braze usando a Okta!

![Login no dashboard da Braze com SSO da Okta ativado.]({% image_buster /assets/img/Okta/okta4.png %}){: style="max-width:60%"}