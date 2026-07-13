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

Durante a configuração, será solicitado que você forneça uma URL de login e uma URL do Assertion Consumer Service (ACS).

| Requisito | Informações |
|---|---|
| URL do Assertion Consumer Service (ACS) | `https://<SUBDOMAIN>.braze.com/auth/saml/callback` <br><br> Para domínios da União Europeia, a URL do ACS é `https://<SUBDOMAIN>.braze.eu/auth/saml/callback`. <br><br> Em alguns IdPs, isso também pode ser chamado de URL de resposta, URL de login, URL de público ou URI de público. |
| Entity ID | `braze_dashboard` |
| Chave de API do RelayState | Acesse **Configurações** > **Chaves de API** e crie uma chave de API com permissões `sso.saml.login`. Em seguida, insira a chave de API gerada como o parâmetro `RelayState` no seu IdP. Para etapas detalhadas, consulte [Configurando seu RelayState](#setting-up-your-relaystate). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos" }

## Configurando o SAML SSO {#setting-up-saml-sso}

### Etapa 1: Configure seu provedor de identidade {#step-1-configure-your-identity-provider}

Configure a Braze como prestador de serviço (SP) no seu provedor de identidade (IdP) com as seguintes informações. Além disso, configure o mapeamento de atributos SAML.

{% alert important %}
Se você planeja usar o Okta como seu provedor de identidade, certifique-se de usar a integração pré-construída encontrada no [site do Okta](https://www.okta.com/integrations/braze/).
{% endalert %}

| Atributo SAML | Obrigatório? | Atributos SAML aceitos |
|---|---|---|
| `email` | Obrigatório | `email` <br> `mail` <br> `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/email` |
| `first_name` | Opcional | `first_name` <br> `firstname` <br> `firstName`<br>`http://schemas.xmlsoap.org/ws/2005/05/identity/claims/first_name` |
| `last_name` | Opcional | `last_name` <br> `lastname` <br> `lastName` <br>`http://schemas.xmlsoap.org/ws/2005/05/identity/claims/last_name` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Etapa 1: Configure seu provedor de identidade" }

{% alert note %}
A Braze exige apenas `email` na asserção SAML.
{% endalert %}

### Etapa 2: Configure a Braze {#step-2-configure-braze}

Quando você terminar de configurar a Braze no seu provedor de identidade, ele fornecerá uma URL de destino e um certificado `x.509` para inserir na sua conta da Braze.

Depois que o gerente da sua conta ativar o SAML SSO para a sua conta, acesse **Configurações** > **Configurações de administrador** > **Configurações de segurança** e alterne a seção SAML SSO para **ON**.

Na mesma página, insira o seguinte:

| Requisito | Informações |
|---|---|
| SAML Name | Isso aparecerá como o texto do botão na tela de login.<br>Normalmente é o nome do seu provedor de identidade, como "Okta". |
| Target URL | Isso é fornecido após configurar a Braze no seu IdP.<br> Alguns IdPs chamam isso de URL de SSO ou endpoint SAML 2.0. |
| Certificado | O certificado `x.509` fornecido pelo seu provedor de identidade.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Etapa 2: Configure a Braze" }

Certifique-se de que o seu certificado `x.509` siga este formato ao adicioná-lo ao dashboard:

```
-----BEGIN CERTIFICATE-----
<certificate>
-----END CERTIFICATE-----
```

![Configurações de SAML SSO com o botão de alternância selecionado.]({% image_buster /assets/img/samlsso.png %})

### Etapa 3: Faça login na Braze {#step-3-sign-into-braze}

Salve suas configurações de segurança e faça logout. Em seguida, faça login novamente com o seu provedor de identidade.

## Configurando seu RelayState {#setting-up-your-relaystate}

1. Na Braze, acesse **Configurações** > **APIs e identificadores**.
2. Na guia **Chaves de API**, selecione o botão **Criar chave de API**.
3. No campo **Nome da chave de API**, insira um nome para a sua chave.
4. Expanda o menu suspenso **SSO** em **Permissões** e marque **sso.saml.login**.
5. Selecione **Criar chave de API**.
6. Na guia **Chaves de API**, copie o identificador ao lado da chave de API que você criou.
7. Cole a chave de API do RelayState no RelayState do seu IdP (também pode aparecer como "Relay State" ou "Default Relay State" dependendo do seu IdP).

## Comportamento do SSO {#sso-behavior}

Os membros que optarem por usar SSO não poderão mais usar suas senhas como faziam antes. Os usuários que continuarem usando suas senhas poderão fazê-lo, a menos que sejam restringidos pelas configurações a seguir.

## Restrição {#restriction}

Você pode restringir os membros da sua organização para que façam login apenas com Google SSO ou SAML SSO. Para ativar as restrições, acesse **Configurações de segurança** e selecione **Enforce Google SSO only login** ou **Enforce custom SAML SSO only login**.

![Exemplo de configuração da seção "Authentication Rules" com um comprimento mínimo de senha de 8 caracteres e reutilização de senha de 3 vezes. As senhas expirarão após 180 dias, e os usuários serão desconectados após 1.440 minutos de inatividade.]({% image_buster /assets/img/sso3.png %})

Ao ativar as restrições, os usuários da Braze da sua empresa não poderão mais fazer login usando uma senha, mesmo que tenham feito login com uma senha anteriormente.

{% alert important %}
Depois que o SSO é aplicado, não há opção de fallback para login caso a autenticação SSO falhe. Antes de ativar a aplicação do SSO, certifique-se de que a configuração do SSO está correta, todos os certificados estão atualizados e renovados, e suas configurações de segurança estão devidamente gerenciadas para evitar problemas de login.
{% endalert %}

## Obtendo um rastreamento SAML {#obtaining-a-saml-trace}

Se você tiver problemas de login relacionados ao SSO, obter um rastreamento SAML pode ajudar a solucionar problemas na sua conexão SSO, identificando o que é enviado nas solicitações SAML.

### Pré-requisitos {#prerequisites}

Para executar um rastreamento SAML, você precisará de um rastreador SAML. Aqui estão duas opções possíveis com base no seu navegador:

- [Google Chrome](https://chromewebstore.google.com/detail/saml-tracer/mpdajninpobndbfcldcmbpnnbhibjmch)
- [Mozilla Firefox](https://addons.mozilla.org/en-US/firefox/addon/saml-tracer/)

### Etapa 1: Abra o rastreador SAML {#step-1-open-the-saml-tracer}

Selecione o rastreador SAML na barra de navegação do seu navegador. Certifique-se de que **Pause** não esteja selecionado, pois isso impedirá que o rastreador SAML capture o que é enviado nas solicitações SAML. Quando o rastreador SAML estiver aberto, você verá o rastreamento sendo preenchido.

![Rastreador SAML para Google Chrome.]({% image_buster /assets/img/saml_tracer_example.png %})

### Etapa 2: Faça login na Braze usando SSO {#step-2-sign-into-braze-using-sso}

Acesse o dashboard da Braze e tente fazer login usando SSO. Se você encontrar um erro, abra o rastreador SAML e tente novamente. Um rastreamento SAML foi coletado com sucesso se houver uma linha com uma URL como `https://dashboard-XX.braze.com/auth/saml/callback` e uma tag SAML laranja.

### Etapa 3: Exporte e envie para a Braze {#step-3-export-and-send-to-braze}

Selecione **Export**. Em **Select cookie-filter profile**, selecione **None**. Em seguida, selecione **Export**. Isso gerará um arquivo JSON que você pode enviar ao suporte da Braze para solução de problemas adicional.

![Menu "Export SAML-trace preferences" com a opção "None" selecionada.]({% image_buster /assets/img/export_saml_trace_preferences.png %})

## Solução de problemas {#troubleshooting}

### O endereço de e-mail do usuário está configurado corretamente? {#is-the-users-email-address-correctly-set-up}

Se você está recebendo o erro `ERROR_CODE_SSO_INVALID_EMAIL`, o endereço de e-mail do usuário não é válido. Confirme no rastreamento SAML que o campo `saml2:Attribute Name="email"` corresponde ao endereço de e-mail que o usuário está usando para fazer login. Se você usa o Microsoft Entra ID (anteriormente Azure Active Directory), o mapeamento de atributo é `email = user.userprincipalname`.

O endereço de e-mail diferencia maiúsculas de minúsculas e deve corresponder exatamente ao que foi configurado na Braze, incluindo o configurado no seu provedor de identidade (como Okta, OneLogin, Microsoft Entra ID e outros).

Outros erros que indicam problemas com o endereço de e-mail do usuário incluem:
- `ERROR_CODE_SSO_EMAIL_DOES_NOT_EXIST`: O endereço de e-mail do usuário não existe no dashboard.
- `ERROR_CODE_SSO_SESSION_SIGN_IN_EMAIL_MISSING`: O endereço de e-mail do usuário está em branco ou configurado incorretamente.
- `ERROR_CODE_SSO_SESSION_SIGN_IN_EMAIL_MISMATCH` ou `ERROR_CODE_SSO_SIGN_IN_EMAIL_MISMATCH`: O endereço de e-mail do usuário não corresponde ao usado para configurar o SSO.

### Você tem um certificado SAML válido (certificado x.509)? {#do-you-have-a-valid-saml-certificate-x509-certificate}

Você pode validar seu certificado SAML usando [esta ferramenta de validação SAML](https://www.samltool.com/validate_response.php). Observe que um certificado SAML expirado também é um certificado SAML inválido.

### Você fez upload do certificado SAML correto (certificado x.509)? {#did-you-upload-a-correct-saml-certificate-x509-certificate}

Confirme que o certificado na seção `ds:X509Certificate` do rastreamento SAML corresponde ao que você fez upload na Braze. Isso não inclui o cabeçalho `-----BEGIN CERTIFICATE-----` e o rodapé `-----END CERTIFICATE-----`.

### Você digitou incorretamente ou formatou mal o seu certificado SAML (certificado x.509)? {#did-you-mistype-or-misformat-your-saml-certificate-x509-certificate}

Confirme que não há espaços em branco ou caracteres extras no certificado que você enviou no dashboard da Braze.

Ao inserir seu certificado na Braze, ele precisa estar codificado em Privacy Enhanced Mail (PEM) e formatado corretamente (incluindo o cabeçalho `-----BEGIN CERTIFICATE-----` e o rodapé `-----END CERTIFICATE-----`).

Aqui está um exemplo de certificado formatado corretamente:

```
-----BEGIN CERTIFICATE-----
THIS_IS_A_MOCKED_CERTIFICATE_4ysJLTzETANBgkqhkiG9w0BAQsFADA0MTIwMAYDVQQDEylNaWNyb3NvZnQgQXp1cmUgRmVkZXJhdGVkIFNTTyBDZXJ0aWZpY2F0ZTAeFw0yMjA1MjcwOTA4MzFaFw0yNTAbMjcwOTA4MzFaMDQxMjAwBgNVBAMTKU1pY3Jvca9mdCBBenVyZSBGZWRlcmF0ZWQgU1NPIENlcnAFWAOKGPAWIGKJPOAMWANBgkqhkiG9w0BAQEFAAaCAQ8AMIIBCgKCAQEA1+KFJwxoac6jdFztQd+vQu59qM8rgfX5RICk0ODfpXkuDUNudcI0XmOAkKHRoMNPYlmMEf5NSiZ7TMElEPtK9zZlpAoSchxxC0Ndegc1AMFi7i2BsEIqPwrer0G6kx2vuAjdrDROPPafkmwalkfmklaw23FlYmV7doE0Vrj2WxR1PG0eFAdsxPLsO1ny55fPj2ibwaqc0XpDkfTrO9GnFvmZAS8ebYtLZsYAMAGLKWAMLGKAWMLKMFDW6vBDaK290s9FdaWza3GPHTcDstawRhyqbXpVjiqpQ0mtxANW4WduSiohhpeqv05TlSOhx87QalkfmwalfmAWMFLKQEBCwUAA4IBAQBdZ5E9FqICfL1q+G6D1tChKl1Y6I6IVULQb4LESSJRaxv53nakmflwakmMALKFMWOYKAeUWO2hdED54qGMgUnLL6YheQBrsm6ilBC68F7ZFmIzVKycvw65yamWbTMi2f2lF60GNYMrq8sGQUkgO0O2zTN07J9wGTe9M+MAFLKWAMFLKalkmflkawoij4jpcsLXXFZJoHSXnF3+qQuzu+49D6pR2lF7DDW+5+PRoc1QpDSytdXxWzItsjQ6IFRuvIGsbrMg0FVaze7ePdKrc47wSlElno7SQ0H+6g40q25rsDSLO
-----END CERTIFICATE-----
```

### O token de sessão do usuário é válido? {#is-the-users-session-token-valid}

Peça ao usuário afetado para [limpar o cache e os cookies do navegador](https://its.uiowa.edu/services/how-clear-cache-and-cookies-your-web-browser) e, em seguida, tente fazer login com SAML SSO novamente.

### Você configurou seu RelayState? {#did-you-set-your-relaystate}

Se você está recebendo o erro `ERROR_CODE_SSO_INVALID_RELAY_STATE`, seu RelayState pode estar configurado incorretamente ou não existir. Se ainda não fez isso, você precisa configurar seu RelayState no sistema de gerenciamento do seu IdP. Para as etapas, consulte [Configurando seu RelayState](#setting-up-your-relaystate).

### O login bem-sucedido por SSO redireciona você para a página de login da Braze? {#does-successful-sso-sign-in-return-you-to-the-braze-login-page}

Isso pode acontecer quando o RelayState não está configurado corretamente. Confirme que você criou uma chave de API (em **Configurações** > **Chaves de API**) para login pelo IdP e definiu essa chave de API como o parâmetro `RelayState` no seu IdP. O RelayState identifica em qual conta da empresa você está fazendo login. Para instruções passo a passo, consulte [Configurando seu RelayState](#setting-up-your-relaystate).

Se ainda não conseguir fazer login, [fale com o suporte da Braze]({{site.baseurl}}/braze_support) com um rastreamento SAML, se possível. Para ajuda na captura de um rastreamento, consulte [Obtendo um rastreamento SAML](#obtaining-a-saml-trace).

### O usuário está preso em um loop de login entre o Okta e a Braze? {#is-the-user-stuck-in-a-sign-in-loop-between-okta-and-braze}

Se um usuário não consegue fazer login porque está preso em um ciclo entre o SSO do Okta e o dashboard da Braze, você precisa acessar o Okta e definir a URL de destino do SSO para a sua [instância da Braze]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints) (por exemplo, `https://dashboard-07.braze.com`).

Se você está usando outro IdP, verifique se a sua empresa fez upload do certificado SAML ou x.509 correto na Braze.

### Você está usando uma integração manual? {#are-you-using-a-manual-integration}

Se a sua empresa não baixou o app da Braze na loja de apps do seu IdP, você precisa baixar a integração pré-construída. Por exemplo, se o Okta é o seu IdP, você baixaria o app da Braze na [página de integração](https://www.okta.com/integrations/braze/) deles.

## Google SSO

Se a sua empresa usa Google SSO em vez de SAML SSO personalizado, fale com o gerente da sua conta da Braze para ativar o Google SSO no seu espaço de trabalho. Depois de ativado, acesse **Configurações de segurança** e selecione **Enforce Google SSO only login** para exigir a autenticação do Google para todos os usuários da empresa.

Quando a exigência de Google SSO está ativada, os usuários devem fazer login com a autenticação do Google e não poderão mais usar uma senha da Braze. Cada usuário deve fazer login com a conta do Google que corresponde ao endereço de e-mail do dashboard da Braze. Se um usuário selecionar uma conta do Google diferente durante o login, a Braze rejeitará a tentativa de autenticação.

### Solução de problemas do login com Google SSO {#troubleshooting-google-sso-sign-in}

Se alguns usuários não conseguem fazer login com Google SSO, verifique o seguinte:

- O e-mail da conta do Google do usuário corresponde exatamente ao endereço de e-mail do dashboard da Braze.
- O usuário tem acesso a uma conta do Google para o endereço de e-mail da empresa.
- O usuário não está suspenso na Braze (**Configurações** > **Usuários da empresa**).

## Próximas etapas {#next-steps}

Após configurar o SAML SSO, você pode:

- [Exigir login apenas por SSO]({{site.baseurl}}/user_guide/administer/global/admin_settings/security_settings#restriction) nas suas configurações de segurança para restringir os usuários de fazerem login com uma senha.
- [Configurar o provisionamento just-in-time SAML]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_just_in_time_provisioning) para que novos usuários criem automaticamente contas na Braze no primeiro login por SSO.