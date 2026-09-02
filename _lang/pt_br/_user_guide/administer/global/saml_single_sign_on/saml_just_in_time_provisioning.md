---
nav_title: Provisionamento Just-in-Time com SAML
article_title: Provisionamento Just-in-Time com SAML
page_order: 1
page_type: tutorial
description: "Este artigo explica como configurar o provisionamento just-in-time com SAML para permitir que novos usuários da empresa criem uma conta na Braze no primeiro login."
---

# Provisionamento just-in-time com SAML {#saml-just-in-time-provisioning}

> O provisionamento just-in-time funciona com o [SAML SSO]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup) para permitir que novos usuários da empresa criem uma conta na Braze no primeiro login. Isso elimina a necessidade de os administradores criarem manualmente uma conta para um novo usuário da empresa, escolherem suas permissões, atribuí-lo a um espaço de trabalho e aguardarem a ativação da conta.

Como medida de segurança, o provisionamento just-in-time com SAML (JITP) funciona apenas para usuários com domínios de e-mail que já existem na sua empresa. O JITP só é possível para domínios em que já existe pelo menos um desenvolvedor confirmado e que não seja de simulação na empresa.

Por exemplo, digamos que a conta `jon.smith@decorumsoft.com` pode usar o JITP para fazer login na Decorumsoft. A conta `jane.smith@decorumsoft.com` tem o mesmo domínio e também pode ter o provisionamento permitido. No entanto, se você tentar usar o JITP com `jon.smith@decorumsoft.eu`, o provisionamento não será permitido porque não existe uma conta `decorumsoft.eu` no dashboard da Braze da Decorumsoft.

Para abrir uma exceção para uma empresa, entre em contato com o [suporte da Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support).

## Pré-requisitos {#prerequisites}

O provisionamento JITP por SAML exige que o SSO SAML esteja configurado e integrado. Ele não é compatível com o SSO do Google e só é compatível com fluxos de login iniciados pelo provedor de identidade (IdP-initiated).

| Requisito | Detalhes |
|---|---|
| SSO SAML | Configurado e testado antes de ativar o JITP. Consulte [Configuração do SSO SAML]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup). |
| Login iniciado pelo IdP | Os usuários devem fazer login pelo portal do IdP no primeiro acesso. O login iniciado pelo SP sozinho não provisiona novos usuários. |
| Domínio de e-mail | O domínio de e-mail do usuário já deve existir na sua empresa (pelo menos um desenvolvedor confirmado, sem simulação, com esse domínio). |
| Capacitação da empresa | A Braze precisa ativar o recurso `saml_jit_provisioning` para a sua empresa antes que o toggle **Automatic user provisioning** apareça. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos do JITP" }

{% alert important %}
O provisionamento just-in-time por SAML precisa ser ativado para a sua empresa pela Braze. Entre em contato com o seu gerente de conta ou com o [suporte da Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support) se o toggle **Automatic user provisioning** não estiver disponível.
{% endalert %}

## Como o JITP funciona {#how-jitp-works}

Quando o JITP está ativado e um novo usuário faz login pelo seu IdP pela primeira vez:

1. A Braze valida a asserção SAML e verifica se o domínio de e-mail do usuário é permitido para o JITP.
2. A Braze cria uma conta de usuário no dashboard usando o e-mail da asserção SAML.
3. A Braze atribui o espaço de trabalho padrão e o conjunto de permissões configurados em **Security Settings**.
4. O usuário pode acessar a Braze imediatamente, sem necessidade de um convite ou etapa de ativação separada.

O JITP não atualiza permissões de usuários existentes. Ele apenas cria contas para usuários que ainda não existem na sua empresa.

## Configurando o provisionamento just-in-time (JITP) com SAML {#setting-up-saml-just-in-time-provisioning-jitp}

Peça a um administrador da Braze para fazer o seguinte:

1. Navegue até **Configurações** > **Configurações da empresa** > **Configurações de administrador** > **Configurações de segurança**.
2. Na seção **SAML SSO**, ative a opção **Automatic user provisioning**.
3. Selecione um espaço de trabalho padrão para adicionar um novo usuário da empresa.
4. Selecione o conjunto de permissões padrão a ser atribuído a esse novo usuário da empresa. Para saber como criar um conjunto de permissões, consulte [Definindo permissões de usuário]({{site.baseurl}}/user_guide/administer/global/user_management/permissions).

{% alert note %}
Se a sua empresa usa permissões granulares, revise o conjunto de permissões padrão após a migração para confirmar que os novos usuários provisionados via JITP recebam o acesso pretendido.
{% endalert %}

5. Selecione **Salvar alterações**.
6. Nas configurações do seu provedor de SSO, adicione todos os usuários que precisam de acesso à Braze ao diretório do seu provedor de SSO.
7. Instrua os usuários a acessar a Braze pelo portal do IdP no primeiro login. Depois disso, o botão de login único SAML será exibido para logins futuros.

## Perguntas frequentes {#frequently-asked-questions}

### Como desativo o JITP SAML? {#how-do-i-disable-saml-jitp}

Após configurar o JITP, você deve [entrar em contato com o suporte]({{site.baseurl}}/user_guide/administer/personal/braze_support) para desativá-lo.

### O JITP pode atribuir permissões diferentes por usuário? {#can-jitp-assign-different-permissions-per-user}

Não. Todos os usuários criados pelo JITP recebem o espaço de trabalho e o conjunto de permissões padrão configurados em **Security Settings**. Para atribuir acessos diferentes, crie usuários manualmente ou use o [provisionamento automatizado de usuários via SCIM]({{site.baseurl}}/scim/automated_user_provisioning).

### O JITP funciona com login iniciado pelo SP? {#does-jitp-work-with-sp-initiated-login}

Não. O JITP é executado apenas durante o login iniciado pelo IdP, quando o usuário começa pelo portal do provedor de identidade.

## Solução de problemas {#troubleshooting}

### O usuário não foi provisionado no primeiro login com SSO {#user-was-not-provisioned-on-first-sso-sign-in}

Verifique o seguinte:

- O JITP está ativado e salvo em **Configurações de segurança**.
- O usuário fez login pelo portal do IdP (iniciado pelo IdP), não apenas pela página de login da Braze.
- O domínio de e-mail do usuário já existe na sua empresa.
- A asserção SAML inclui um atributo `email` válido que corresponde ao endereço com o qual o usuário faz login.

### O botão de login único não aparece com o Microsoft Entra ID {#single-sign-on-button-doesnt-appear-with-microsoft-entra-id}

O campo **Sign-On URL** no formulário **Basic SAML Configuration** do Microsoft Entra para a Braze pode fazer com que os usuários vejam apenas a opção de senha, e não um botão de SSO, ao fazer login iniciado pelo IdP. Para evitar esse problema, deixe o campo **Sign-On URL** em branco ao configurar a Braze no centro de administração do Microsoft Entra.