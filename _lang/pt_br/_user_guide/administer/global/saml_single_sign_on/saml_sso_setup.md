---
nav_title: Configuração de SAML SSO
article_title: Configuração de SAML SSO
page_order: 0
page_type: tutorial
toc_headers: h2
description: "Este artigo mostra como ativar o login único SAML para a sua conta da Braze."
---

# Login iniciado pelo prestador de serviço (SP) {#service-provider-sp-initiated-login}

> Este artigo mostra como ativar o login único SAML para a sua conta da Braze e como obter um rastreamento SAML.

## Requisitos {#requirements}

Após a configuração, será solicitado que você forneça uma URL de login e uma URL do Assertion Consumer Service (ACS).

| Requisito | Detalhes |
|---|---|
| URL do Assertion Consumer Service (ACS) | `https://<SUBDOMAIN>.braze.com/auth/saml/callback` <br><br> Para domínios da União Europeia, a URL do ACS é `https://<SUBDOMAIN>.braze.eu/auth/saml/callback`. <br><br> Para alguns IdPs, essa URL também pode ser chamada de URL de resposta, URL de login, URL de público ou URI de público. |
| Entity ID | `braze_dashboard` por padrão. Se o seu IdP exigir um Entity ID específico da empresa, ative **Custom Entity ID** em **Configurações de segurança** e use `braze_dashboard_<companyID>`. |
| Chave de API do RelayState | Acesse **Configurações** > **Configuração e teste** > **APIs e identificadores**, abra a guia **API Keys** e crie uma chave de API com permissões `sso.saml.login`. Insira a chave de API gerada como o parâmetro `RelayState` no seu IdP. Para etapas detalhadas, consulte [Configurando seu RelayState](#setting-up-your-relaystate). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos" }

## Configuração de SAML SSO {#setting-up-saml-sso}

### Etapa 1: Configure seu provedor de identidade {#step-1-configure-your-identity-provider}

Configure a Braze como prestador de serviço (SP) no seu provedor de identidade (IdP) com as seguintes informações. Além disso, configure o mapeamento de atributos SAML.

{% alert important %}
Se você planeja usar o Okta como seu provedor de identidade, certifique-se de usar a integração pré-construída encontrada no [site do Okta](https://www.okta.com/integrations/braze/).
{% endalert %}

| Atributo SAML | Obrigatório? | Atributos SAML aceitos |
|---|---|---|
|`email` | Obrigatório | `email` <br> `mail` <br> `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/email` |
| `first_name` | Opcional | `first_name` <br> `firstname` <br> `firstName`<br>`http://schemas.xmlsoap.org/ws/2005/05/identity/claims/first_name` |
| `last_name` | Opcional | `last_name` <br> `lastname` <br> `lastName` <br>`http://schemas.xmlsoap.org/ws/2005/05/identity/claims/last_name` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Etapa 1: Configure seu provedor de identidade" }

{% alert note %}
A Braze requer apenas `email` na asserção SAML.
{% endalert %}

### Etapa 2: Configure a Braze {#step-2-configure-braze}

Quando você terminar de configurar a Braze no seu provedor de identidade, ele fornecerá um URL de destino e um certificado `x.509` para inserir na sua conta da Braze.

Depois que o gerente de conta ativar o SAML SSO para a sua conta, acesse **Configurações** > **Configurações da empresa** > **Configurações de administrador** > **Configurações de segurança** e alterne a seção SAML SSO para **ON**.

Na mesma página, insira o seguinte:

| Requisito | Detalhes |
|---|---|
| Nome SAML | Isso aparecerá como o texto do botão na tela de login.<br>Normalmente é o nome do seu provedor de identidade, como "Okta". |
| URL de destino | Esse URL é fornecido após a configuração da Braze no seu IdP.<br> Alguns IdPs referenciam isso como URL de SSO ou endpoint SAML 2.0. |
| Certificado | O certificado `x.509` fornecido pelo seu provedor de identidade.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Etapa 2: Configure a Braze" }

### ID de entidade personalizado {#custom-entity-id}

Por padrão, a Braze usa `braze_dashboard` como o ID de entidade (também chamado de Audience ou Audience URI em alguns IdPs). Se o seu IdP exigir um ID de entidade específico da empresa:

1. Em **Configurações de segurança**, ative **Custom Entity ID**.
2. Copie o ID de entidade gerado (`braze_dashboard_<companyID>`).
3. Cole esse valor no campo Entity ID, Audience ou Audience URI do seu IdP.
4. Salve as alterações na Braze e no seu IdP antes de testar o login.

{% alert important %}
Os usuários não conseguirão fazer login até que o ID de entidade corresponda na Braze e no seu IdP. O ID de entidade personalizado requer configuração adicional no seu provedor de identidade.
{% endalert %}

Certifique-se de que o certificado `x.509` siga este formato ao adicioná-lo ao dashboard:

```
-----BEGIN CERTIFICATE-----
<certificate>
-----END CERTIFICATE-----
```

![Configurações de SAML SSO com o botão de alternância selecionado.]({% image_buster /assets/img/samlsso.png %})

### Etapa 3: Faça login na Braze {#step-3-sign-into-braze}

Salve suas configurações de segurança e faça logout. Em seguida, faça login novamente com o seu provedor de identidade.

## Usando um Entity ID personalizado {#using-a-custom-entity-id}

Por padrão, todo dashboard da Braze usa o Entity ID compartilhado `braze_dashboard`. Um Entity ID personalizado dá ao seu dashboard um identificador único, para que o provedor de identidade possa verificar que as solicitações de login são destinadas a esse dashboard específico. Isso é útil se você estiver configurando SAML SSO em várias empresas da Braze no mesmo provedor de identidade.

Usar um Entity ID personalizado é opcional. Se você não ativá-lo, seu dashboard continuará usando `braze_dashboard`.

{% alert warning %}
O [app pré-configurado da Braze no marketplace do Okta](https://www.okta.com/integrations/braze/) exige o Entity ID compartilhado `braze_dashboard` e não é compatível com um Entity ID personalizado. Se você já tem SAML SSO configurado com o app da Braze no marketplace do Okta, ativar um Entity ID personalizado sem atualizar o campo Entity ID no Okta por meio de um app SAML personalizado vai interromper o login e pode bloquear o acesso dos usuários ao dashboard. Para usar um Entity ID personalizado com o Okta, configure um app SAML personalizado.
{% endalert %}

### Etapa 1: Ativar o Entity ID personalizado {#step-1-turn-on-the-custom-entity-id}

Acesse **Configurações** > **Configuração de administrador** > **Configuração de segurança** e abra a seção SAML Single Sign-On. Ative o toggle **Custom Entity ID**. A Braze gera um Entity ID único para o seu dashboard no formato `braze_dashboard_<COMPANY_ID>`. Se você não encontrar a opção **Custom Entity ID**, entre em contato com o gerente de conta da Braze.

### Etapa 2: Atualizar seu provedor de identidade {#step-2-update-your-identity-provider}

Copie o Entity ID gerado e cole no campo Entity ID do aplicativo da Braze no seu provedor de identidade. Dependendo do provedor, esse campo pode ser chamado de **Entity ID**, **Audience** ou **Audience URI**.

{% alert important %}
O Entity ID precisa ser o mesmo na Braze e no seu provedor de identidade. Até que ambos os lados usem o mesmo valor, os usuários não conseguirão fazer login com SAML SSO. Atualize seu provedor de identidade antes de salvar esta página para evitar bloquear o acesso dos usuários.
{% endalert %}

### Etapa 3: Salvar e testar {#step-3-save-and-test}

Salve suas configurações de segurança, faça logout e depois faça login novamente por meio do seu provedor de identidade para confirmar que o login funciona com o Entity ID personalizado.

## Configurando seu RelayState {#setting-up-your-relaystate}

1. Na Braze, acesse **Configurações** > **Configuração e Teste** > **APIs e Identificadores**.
2. Na guia **Chaves de API**, selecione o botão **Criar chave de API**.
3. No campo **Nome da chave de API**, insira um nome para sua chave.
4. Expanda o dropdown **SSO** em **Permissões** e marque **sso.saml.login**.
5. Selecione **Criar chave de API**.
6. Na guia **Chaves de API**, copie o identificador ao lado da chave de API que você criou.
7. Cole a chave de API do RelayState no RelayState do seu provedor de identidade (também pode aparecer como "Relay State" ou "Default Relay State" dependendo do seu provedor de identidade).

## Login iniciado pelo IdP {#idp-initiated-login}

Alguns provedores de identidade oferecem suporte ao login iniciado pelo IdP, em que os usuários começam pelo portal do IdP em vez da página de login da Braze. O login iniciado pelo IdP requer uma chave de API RelayState válida e a configuração correta da URL ACS. Guias de configuração específicos por provedor:

- [Okta]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/okta)
- [OneLogin]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/onelogin)
- [Microsoft Entra SSO]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/microsoft_entra_sso)

{% alert note %}
O login iniciado pelo IdP com Microsoft Entra SSO requer que o campo **Sign-On URL** seja deixado em branco. Consulte [Microsoft Entra SSO]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/microsoft_entra_sso) para mais detalhes.
{% endalert %}

## Comportamento do SSO {#sso-behavior}

Os membros que optarem por usar SSO não poderão mais usar sua senha. Os usuários que continuarem a usar sua senha poderão fazê-lo, a menos que sejam restritos pelas configurações a seguir.

## Restrição {#restriction}

Você pode restringir os membros da sua organização para que façam login apenas com Google SSO ou SAML SSO. Para ativar as restrições, acesse **Configurações** > **Configurações da empresa** > **Configurações de administrador** > **Configurações de segurança** e selecione **Enforce Google SSO only login** ou **Enforce custom SAML SSO only login**.

![Exemplo de configuração da seção "Regras de autenticação" com um comprimento mínimo de senha de 8 caracteres e reutilização de senha de 3 vezes. As senhas expirarão após 180 dias, e os usuários serão desconectados após 1.440 minutos de inatividade.]({% image_buster /assets/img/sso3.png %})

Ao ativar as restrições, os usuários da Braze da sua empresa não poderão mais fazer login usando uma senha, mesmo que já tenham feito login com senha anteriormente.

{% alert important %}
Após a aplicação do SSO, não há opção de fallback para login caso a autenticação SSO falhe. Antes de ativar a aplicação do SSO, verifique se a configuração do SSO está correta, se todos os certificados estão atualizados e renovados e se as configurações de segurança estão devidamente gerenciadas para evitar problemas de login.
{% endalert %}

## Obtendo um rastreamento SAML {#obtaining-a-saml-trace}

Se você tiver problemas de login relacionados ao SSO, obter um rastreamento SAML pode ajudar a solucionar sua conexão SSO identificando o que é enviado nas requisições SAML.

### Pré-requisitos {#prerequisites}

Para executar um rastreamento SAML, você precisará de um rastreador SAML. Aqui estão duas opções possíveis com base no seu navegador:

- [Google Chrome](https://chromewebstore.google.com/detail/saml-tracer/mpdajninpobndbfcldcmbpnnbhibjmch)
- [Mozilla Firefox](https://addons.mozilla.org/en-US/firefox/addon/saml-tracer/)

### Etapa 1: Abra o rastreador SAML {#step-1-open-the-saml-tracer}

Selecione o rastreador SAML na barra de navegação do seu navegador. Certifique-se de que **Pause** não esteja selecionado, pois isso impedirá que o rastreador SAML capture o que é enviado nas requisições SAML. Quando o rastreador SAML estiver aberto, você verá o rastreamento sendo preenchido.

![Rastreador SAML para Google Chrome.]({% image_buster /assets/img/saml_tracer_example.png %})

### Etapa 2: Faça login na Braze usando SSO {#step-2-sign-into-braze-using-sso}

Acesse seu dashboard da Braze e tente fazer login usando SSO. Se você encontrar um erro, abra o rastreador SAML e tente novamente. Um rastreamento SAML foi coletado com sucesso se houver uma linha com uma URL como `https://dashboard-XX.braze.com/auth/saml/callback` e uma tag SAML laranja.

### Etapa 3: Exporte e envie para o suporte da Braze {#step-3-export-and-send-to-braze}

Selecione **Export**. Em **Select cookie-filter profile**, selecione **None**. Em seguida, selecione **Export**. Isso gerará um arquivo JSON que você pode enviar ao suporte da Braze para solução de problemas adicional.

![Menu de preferências "Export SAML-trace preferences" com a opção "None" selecionada.]({% image_buster /assets/img/export_saml_trace_preferences.png %})

## Solução de problemas {#troubleshooting}

### O endereço de e-mail do usuário está configurado corretamente? {#is-the-users-email-address-correctly-set-up}

Se você está recebendo o erro `ERROR_CODE_SSO_INVALID_EMAIL`, o endereço de e-mail do usuário não é válido. Confirme no rastreamento SAML que o campo `saml2:Attribute Name="email"` corresponde ao endereço de e-mail que o usuário está usando para fazer login. Se você usa o Microsoft Entra ID (anteriormente Azure Active Directory), o mapeamento de atributo é `email = user.userprincipalname`.

O endereço de e-mail diferencia maiúsculas de minúsculas e deve corresponder exatamente ao que foi configurado na Braze, incluindo o configurado no seu provedor de identidade (como Okta, OneLogin, Microsoft Entra ID, entre outros).

Outros erros que indicam problemas com o endereço de e-mail do usuário incluem:
- `ERROR_CODE_SSO_EMAIL_DOES_NOT_EXIST`: O endereço de e-mail do usuário não está no dashboard.
- `ERROR_CODE_SSO_SESSION_SIGN_IN_EMAIL_MISSING`: O endereço de e-mail do usuário está em branco ou configurado incorretamente.
- `ERROR_CODE_SSO_SESSION_SIGN_IN_EMAIL_MISMATCH` ou `ERROR_CODE_SSO_SIGN_IN_EMAIL_MISMATCH`: O endereço de e-mail do usuário não corresponde ao usado para configurar o SSO.

### Você tem um certificado SAML válido (certificado x.509)? {#do-you-have-a-valid-saml-certificate-x509-certificate}

Você pode validar seu certificado SAML usando [esta ferramenta de validação SAML](https://www.samltool.com/validate_response.php). Note que um certificado SAML expirado também é um certificado SAML inválido.

### Você carregou um certificado SAML correto (certificado x.509)? {#did-you-upload-a-correct-saml-certificate-x509-certificate}

Confirme que o certificado na seção `ds:X509Certificate` do rastreamento SAML corresponde ao que você carregou na Braze. Isso não inclui o cabeçalho `-----BEGIN CERTIFICATE-----` e o rodapé `-----END CERTIFICATE-----`.

### Você digitou incorretamente ou formatou mal seu certificado SAML (certificado x.509)? {#did-you-mistype-or-misformat-your-saml-certificate-x509-certificate}

Confirme que não há espaços em branco ou caracteres extras no certificado que você enviou no dashboard da Braze.

Ao inserir seu certificado na Braze, ele precisa estar codificado em Privacy Enhanced Mail (PEM) e formatado corretamente (incluindo o cabeçalho `-----BEGIN CERTIFICATE-----` e o rodapé `-----END CERTIFICATE-----`).

Aqui está um exemplo de certificado formatado corretamente:

```
-----BEGIN CERTIFICATE-----
THIS_IS_A_MOCKED_CERTIFICATE_4ysJLTzETANBgkqhkiG9w0BAQsFADA0MTIwMAYDVQQDEylNaWNyb3NvZnQgQXp1cmUgRmVkZXJhdGVkIFNTTyBDZXJ0aWZpY2F0ZTAeFw0yMjA1MjcwOTA4MzFaFw0yNTAbMjcwOTA4MzFaMDQxMjAwBgNVBAMTKU1pY3Jvca9mdCBBenVyZSBGZWRlcmF0ZWQgU1NPIENlcnAFWAOKGPAWIGKJPOAMWANBgkqhkiG9w0BAQEFAAaCAQ8AMIIBCgKCAQEA1+KFJwxoac6jdFztQd+vQu59qM8rgfX5RICk0ODfpXkuDUNudcI0XmOAkKHRoMNPYlmMEf5NSiZ7TMElEPtK9zZlpAoSchxxC0Ndegc1AMFi7i2BsEIqPwrer0G6kx2vuAjdrDROPPafkmwalkfmklaw23FlYmV7doE0Vrj2WxR1PG0eFAdsxPLsO1ny55fPj2ibwaqc0XpDkfTrO9GnFvmZAS8ebYtLZsYAMAGLKWAMLGKAWMLKMFDW6vBDaK290s9FdaWza3GPHTcDstawRhyqbXpVjiqpQ0mtxANW4WduSiohhpeqv05TlSOhx87QalkfmwalfmAWMFLKQEBCwUAA4IBAQBdZ5E9FqICfL1q+G6D1tChKl1Y6I6IVULQb4LESSJRaxv53nakmflwakmMALKFMWOYKAeUWO2hdED54qGMgUnLL6YheQBrsm6ilBC68F7ZFmIzVKycvw65yamWbTMi2f2lF60GNYMrq8sGQUkgO0O2zTN07J9wGTe9M+MAFLKWAMFLKalkmflkawoij4jpcsLXXFZJoHSXnF3+qQuzu+49D6pR2lF7DDW+5+PRoc1QpDSytdXxWzItsjQ6IFRuvIGsbrMg0FVaze7ePdKrc47wSlElno7SQ0H+6g40q25rsDSLO
-----END CERTIFICATE-----
```

### O token de sessão do usuário é válido? {#is-the-users-session-token-valid}

Peça ao usuário afetado para [limpar o cache e os cookies do navegador](https://its.uiowa.edu/services/how-clear-cache-and-cookies-your-web-browser) e depois tentar fazer login com SAML SSO novamente.

### Você configurou seu RelayState? {#did-you-set-your-relaystate}

Se você está recebendo o erro `ERROR_CODE_SSO_INVALID_RELAY_STATE`, seu RelayState pode estar mal configurado ou inexistente. Se ainda não fez isso, você precisa definir seu RelayState no sistema de gerenciamento do seu IdP. Para ver as etapas, consulte [Configurando seu RelayState](#setting-up-your-relaystate).

### O login SSO bem-sucedido redireciona você de volta para a página de login da Braze? {#does-successful-sso-sign-in-return-you-to-the-braze-login-page}

Isso pode ocorrer quando o RelayState não está configurado corretamente. Confirme que você criou uma chave de API (em **Configurações** > **Configuração e testes** > **APIs e identificadores**) para login pelo IdP e definiu essa chave de API como o parâmetro `RelayState` no seu IdP. O RelayState identifica em qual conta da empresa você está fazendo login. Para instruções passo a passo, consulte [Configurando seu RelayState](#setting-up-your-relaystate).

Se você ainda não conseguir fazer login, [entre em contato com o suporte da Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support) com um rastreamento SAML, se possível. Para ajuda na captura de um rastreamento, consulte [Obtendo um rastreamento SAML](#obtaining-a-saml-trace).

### O usuário está preso em um loop de login entre o Okta e a Braze? {#is-the-user-stuck-in-a-sign-in-loop-between-okta-and-braze}

Se um usuário não consegue fazer login porque está preso em um ciclo entre o SSO do Okta e o dashboard da Braze, você precisa acessar o Okta e definir o destino da URL de SSO para a sua [instância da Braze]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints) (por exemplo, `https://dashboard-07.braze.com`).

Se você está usando outro IdP, verifique se sua empresa carregou o certificado SAML ou x.509 correto na Braze.

### Você está usando uma integração manual? {#are-you-using-a-manual-integration}

Se sua empresa não baixou o app da Braze na loja de apps do seu IdP, você precisa baixar a integração pré-construída. Por exemplo, se o Okta é seu IdP, você deve baixar o app da Braze na [página de integração](https://www.okta.com/integrations/braze/) deles.

## Google SSO {#google-sso}

Se a sua empresa usa Google SSO em vez de SAML personalizado, fale com o gerente da sua conta da Braze para ativar o Google SSO no seu espaço de trabalho. Depois de ativado, acesse **Configurações** > **Configurações da empresa** > **Configurações de administrador** > **Configurações de segurança** e selecione **Enforce Google SSO only login** para exigir a autenticação do Google para todos os usuários da empresa.

Quando a exigência de Google SSO está ativada, os usuários devem fazer login com a autenticação do Google e não poderão mais usar uma senha da Braze. Cada usuário deve fazer login com a conta do Google que corresponde ao endereço de e-mail do dashboard da Braze. Se um usuário selecionar uma conta do Google diferente durante o login, a Braze rejeitará a tentativa de autenticação.

### Solução de problemas do login com Google SSO {#troubleshooting-google-sso-sign-in}

Se alguns usuários não conseguem fazer login com Google SSO, verifique o seguinte:

- O e-mail da conta do Google do usuário corresponde exatamente ao endereço de e-mail do dashboard da Braze.
- O usuário tem acesso a uma conta do Google para o endereço de e-mail da empresa.
- O usuário não está suspenso na Braze (**Configurações** > **Usuários da empresa**).

## Próximas etapas {#next-steps}

Após configurar o SSO SAML, você pode:

{% article_tiles %}
- name: Exigir login somente por SSO
  link: /docs/user_guide/administer/global/admin_settings/security_settings#single-sign-on-sso-authentication
- name: Configurar o provisionamento just-in-time SAML
  link: /docs/user_guide/administer/global/saml_single_sign_on/saml_just_in_time_provisioning
{% endarticle_tiles %}