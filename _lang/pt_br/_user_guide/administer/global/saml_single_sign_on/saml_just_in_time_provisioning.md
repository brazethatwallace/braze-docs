---
nav_title: Provisionamento Just-in-Time com SAML
article_title: Provisionamento Just-in-Time com SAML
page_order: 1
page_type: tutorial
description: "Este artigo explica como configurar o provisionamento just-in-time com SAML para permitir que novos usuários da empresa criem uma conta na Braze no primeiro login."

---

# Provisionamento just-in-time com SAML

> O provisionamento just-in-time funciona com o [SAML SSO]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup/) para permitir que novos usuários da empresa criem uma conta na Braze no primeiro login. Isso elimina a necessidade de os administradores criarem manualmente uma conta para um novo usuário da empresa, escolherem suas permissões, atribuí-lo a um espaço de trabalho e aguardarem a ativação da conta.

Como medida de segurança, o provisionamento just-in-time com SAML (JITP) funciona apenas para usuários com domínios de e-mail que já existem na sua empresa. O JITP só é possível para domínios em que já existe pelo menos um desenvolvedor confirmado e que não seja de simulação na empresa.

Por exemplo, digamos que a conta `jon.smith@decorumsoft.com` pode usar o JITP para fazer login na Decorumsoft. A conta `jane.smith@decorumsoft.com` tem o mesmo domínio e também pode ter o provisionamento permitido. No entanto, se você tentar usar o JITP com `jon.smith@decorumsoft.eu`, o provisionamento não será permitido porque não existe uma conta `decorumsoft.eu` no dashboard da Braze da Decorumsoft.

Para abrir uma exceção para uma empresa, entre em contato com o [Suporte]({{site.baseurl}}/braze_support/).

## Pré-requisitos

O JITP com SAML exige que o SAML SSO esteja configurado e integrado. Ele não é compatível com o Google SSO e só é suportado para fluxos de login iniciados pelo provedor de identidade (IdP-initiated).

## Configurando o provisionamento just-in-time com SAML (JITP)

Peça a um administrador da Braze para fazer o seguinte:

1. Navegue até **Configurações** > **Configurações de administrador** > **Configurações de segurança**.
2. Na seção **SAML SSO**, ative a opção **Automatic user provisioning**.
3. Selecione um espaço de trabalho padrão para adicionar um novo usuário da empresa.
4. Selecione o conjunto de permissões padrão a ser atribuído a esse novo usuário da empresa. Para saber como criar um conjunto de permissões, consulte [Definindo permissões de usuário]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/).
6. Selecione **Salvar alterações** na parte inferior da página.
7. Nas configurações do seu provedor de SSO, adicione todos os usuários que precisam de acesso à Braze ao diretório do seu provedor de SSO.
8. Instrua os usuários a acessarem a Braze pelo portal do IdP no primeiro login. Depois disso, o botão de login único com SAML será exibido para logins futuros.

## Perguntas frequentes

### Como desativo o JITP com SAML?

Após configurar o JITP, você deve [entrar em contato com o Suporte]({{site.baseurl}}/braze_support/) para desativá-lo.

## Solução de problemas

### O botão de login único não aparece com o Microsoft Entra ID

O campo **Sign-On URL** no formulário **Basic SAML Configuration** do Microsoft Entra para a Braze pode fazer com que os usuários vejam apenas a opção de senha, e não o botão de SSO, no login iniciado pelo IdP. Para evitar esse problema, deixe o campo **Sign-On URL** em branco ao configurar a Braze no centro de administração do Microsoft Entra.