---
nav_title: Okta
article_title: Okta
page_order: 3
page_type: tutorial
description: "Este artigo orientará sobre como configurar a Braze para usar o Okta para login único."

---

# Okta

> O Okta conecta qualquer pessoa a qualquer aplicativo em qualquer dispositivo. É um serviço de gerenciamento de identidade de nível empresarial, construído para a nuvem, mas compatível com muitos aplicativos locais. Com o Okta, sua equipe de TI pode gerenciar o acesso de qualquer colaborador a qualquer aplicativo ou dispositivo.

## Requisitos {#requirements}

| Requisito | Informações |
| ----------- | ------- |
| Okta ativado para sua conta | Entre em contato com seu gerente de conta da Braze para ativar essa opção em sua conta. |
| Privilégios de administrador do Okta | Certifique-se de ter privilégios de administrador antes de configurar o Okta. |
| Privilégios de administrador da Braze | Certifique-se de ter privilégios de administrador antes de configurar o Okta. |
| Chave de API RelayState | Para ativar o login IdP, acesse **Configurações** > **Chaves de API** e crie uma chave de API com permissões de `sso.saml.login`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos" }

## Etapa 1: Configure a Braze {#step-1-configure-braze}

### Etapa 1a: Navegue até as configurações de segurança na Braze {#step-1a-navigate-to-security-settings-in-braze}

Depois que o gerente da sua conta ativar o SAML SSO para sua conta, acesse **Configurações** > **Configurações de administrador** > **Configurações de segurança** e alterne a seção SAML SSO para **LIGADO**.

![Okta SAML SSO ativado na página de configurações de segurança.]({% image_buster/assets/img/Okta/okta1.png %})

### Etapa 1b: Edite as configurações de SAML SSO {#step-1b-edit-saml-sso-settings}

No dashboard de administração do Okta, o Okta fornece uma URL de destino (URL de login) e um certificado `x.509`, que você deve inserir na página **Configurações de segurança** da sua conta na Braze.

![]({% image_buster /assets/img/Okta/okta5.png %}){: style="max-width:75%"}

| Requisito | Informações |
|---|---|
| `SAML Name` | Isso aparecerá como o texto do botão na tela de login. Normalmente é o nome do seu provedor de identidade, por exemplo, "Okta". |
| `Target URL` | Esta é a URL de login fornecida pelo dashboard de administração do Okta. Encontre-a acessando **Applications** > seu aplicativo > guia **General** > **App Embed Link** > **Embed Link**. |
| `Certificate` | O certificado `x.509` codificado em PEM é fornecido pelo seu provedor de identidade. Você deve copiá-lo e colá-lo neste campo. Recupere-o no Okta acessando **SAML Signing Certificates** e selecionando **Actions** > **Download certificate**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Etapa 1b: Edite as configurações de SAML SSO" }

Selecione **Salvar alterações** na parte inferior da página quando concluir.

## Etapa 2: Configure o Okta {#step-2-configure-okta}

No Okta, selecione a guia **Sign On** para o app SAML da Braze e clique em **Edit**.

Em seguida, insira a chave de API RelayState com permissão `sso.saml.login` no campo **Default Relay State**.

![Okta Default RelayState na guia Sign On.]({% image_buster /assets/img/Okta/okta2.png %}){: style="max-width:75%"}

Certifique-se de salvar essas novas configurações.

{% alert tip %}
Se você deseja que os usuários da sua conta na Braze façam login apenas com SAML SSO, é possível [restringir a autenticação de login único]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup/#restriction) na página **Configurações da empresa**.
{% endalert %}

## Etapa 3: Faça login {#step-3-log-in}

Agora você deve conseguir fazer login na Braze usando o Okta!

![Login no dashboard da Braze com Okta SSO ativado.]({% image_buster /assets/img/Okta/okta4.png %}){: style="max-width:60%"}