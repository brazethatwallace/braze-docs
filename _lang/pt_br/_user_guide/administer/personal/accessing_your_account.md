---
nav_title: Acessar sua conta
article_title: Acessar sua conta
page_order: 0
page_type: reference
description: "Este artigo aborda como obter sua conta da Braze, como fazer login após receber acesso e como solucionar problemas de acesso e desempenho do dashboard."
---

# Acessar sua conta {#access-your-account}

> Este artigo aborda como obter sua conta da Braze, como fazer login após receber acesso e como solucionar problemas de acesso e desempenho do dashboard.

Se você é o primeiro usuário da Braze na sua empresa e está fazendo login pela primeira vez, você receberá um e-mail de boas-vindas de `@alerts.braze.com` pedindo para confirmar seu e-mail e fazer login no primeiro dia do seu contrato.

Após confirmar sua conta, você pode adicionar usuários adicionais na página [Usuários da empresa]({{site.baseurl}}/user_guide/administer/global/user_management/manage_company_users) do seu dashboard. Todos os usuários recebem um e-mail pedindo para confirmar sua conta após serem adicionados.

Se você não é o primeiro usuário na conta da Braze da sua empresa, entre em contato com o administrador da conta da Braze da sua empresa e peça para criar sua conta. Você receberá um e-mail de boas-vindas de `@alerts.braze.com` pedindo para confirmar seu e-mail e fazer login.

## Fazendo login {#logging-in}

Seja seu primeiro login ou o centésimo, veja como acessar seu dashboard. Se você é o primeiro usuário da sua empresa, siga as orientações na seção anterior. Caso contrário, você pode fazer login após o administrador da Braze na sua empresa criar sua conta.

Você pode fazer login pelo site principal da [Braze.com](https://www.braze.com) ou usar a URL do dashboard que corresponde à sua [instância da Braze]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints) específica. Para sua conveniência, a Braze oferece várias opções de login único (SSO), como:

* [SSO SAML]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup)
    * [Provisionamento just-in-time SAML]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_just_in_time_provisioning)
* [SSO Microsoft Entra]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/microsoft_entra_sso)
* [Okta]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/okta)
* [OneLogin]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/onelogin)

Depois de fazer login na Braze com SSO, você não poderá mais usar sua senha para fazer login no dashboard. Ambos os endereços de e-mail direcionam e-mails para a mesma caixa de entrada, mas a Braze os reconhece como contas separadas quando você faz login. Limpar os cookies encerra sua sessão, então qualquer trabalho não salvo será perdido.

## Navegadores compatíveis {#supported-browsers}

O dashboard da Braze é compatível com os seguintes navegadores:
- Chrome (versão 87 ou mais recente)
- Firefox (versão 85 ou mais recente)
- Safari (versão 15.4 ou mais recente)
- Edge (versão 87 ou mais recente)

Se o seu dashboard da Braze exibir um erro inesperado e a ferramenta de console do navegador mostrar o erro `ReferenceError: structuredClone is not defined`, seu navegador está desatualizado. Se esse erro continuar ocorrendo, desinstale e reinstale o navegador.

## Acessando múltiplos dashboards da Braze {#accessing-multiple-braze-dashboards}

A Braze não permite registrar o mesmo endereço de e-mail para múltiplos usuários do dashboard no mesmo cluster (por exemplo, se você tem dois dashboards no US-01). Você pode usar o mesmo e-mail para criar contas em clusters diferentes (por exemplo, se você tem um dashboard no US-01 e um no US-05). Se você precisa acessar múltiplos dashboards da Braze no mesmo cluster, pode fazer o seguinte:

### Usar aliases de e-mail {#use-email-aliases}

Se o seu provedor de e-mail é o Gmail, você pode criar aliases adicionando um sinal de `+` seguido de qualquer texto ao seu endereço de e-mail. Por exemplo:
- **E-mail original:** `rocky@gmail.com`
- **E-mail de alias:** `rocky+1@gmail.com`

Ambos os endereços de e-mail direcionam os e-mails para a mesma caixa de entrada, mas a Braze os reconhece como contas separadas quando você faz login.

### Criar aliases separados com outros provedores {#create-separate-aliases-with-other-providers}

Se o seu provedor de e-mail não aceita aliases com `+`, você ainda pode criar aliases separados, como configurar `rocky@braze.com` para encaminhar para `rocky.lotito@braze.com`. Isso permite que múltiplos endereços direcionem para a mesma caixa de entrada, sendo reconhecidos como e-mails diferentes pela Braze.

### Usar desenvolvedores multi-empresa {#use-multi-company-developers}

O recurso de desenvolvedores multi-empresa permite compartilhar uma única conta de usuário entre múltiplas empresas. Os usuários do dashboard podem alternar entre dashboards de diferentes empresas a partir do menu de perfil de usuário.

Se você tem SSO e deseja configurar desenvolvedores multi-empresa, é necessário ativar um ID de Entidade SAML personalizado configurando uma integração SAML SSO personalizada. Siga as etapas em [Login iniciado pelo provedor de serviço (SP)]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup), mas aplique estas alterações:
- Altere o **Entity ID** para `braze_dashboard_<companyID>` para cada integração de dashboard.
- Entre em contato com seu gerente de sucesso do cliente ou gerente de conta para ativar o feature flipper `saml_sso_custom_entity_id` para cada dashboard.

#### Autenticação de dois fatores (2FA) {#two-factor-authentication-2fa}

O funcionamento da 2FA para desenvolvedores multi-empresa depende do seu método de 2FA:

- **E-mail e SMS:** Suas configurações de 2FA são copiadas para todas as contas de desenvolvedor vinculadas. Depois de configurar a 2FA por e-mail ou SMS em uma conta, o mesmo método se aplica em todos os dashboards da sua empresa.
- **Senha única baseada em tempo (TOTP):** As configurações de TOTP não são sincronizadas entre contas. Se você usa um app autenticador, deve configurar um código separado para cada dashboard no qual faz login diretamente.

Quando você alterna entre contas de dentro do dashboard, só precisa completar a 2FA uma vez — na primeira vez que faz login em qualquer conta vinculada durante aquela sessão.

### Considerações sobre Single Sign-On (SSO) {#considerations-for-single-sign-on-sso}

Se você usa Single Sign-On (SSO), esteja ciente de que ter múltiplos endereços de e-mail diferentes pode causar complicações. Confirme que suas configurações de SSO estão definidas corretamente para evitar problemas de acesso.

## Solução de problemas {#troubleshooting}

### Redefinição de senha {#resetting-your-password}

Para redefinir sua senha, selecione o link **Forgot your password?** na página de login do dashboard. Você receberá uma solicitação para inserir seu e-mail e receber um link para redefinir sua senha.


#### E-mail de redefinição de senha não recebido {#password-reset-email-not-received}

Se você solicitou uma redefinição de senha, mas não recebeu o e-mail, tente as seguintes etapas de solução de problemas:

{% alert note %}
Se sua empresa utiliza [logon único (SSO)]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup), a página de login pode não exibir **Forgot your password?** nem enviar e-mails de redefinição de senha, pois o login por senha está desativado. Faça login pelo provedor de identidade da sua organização ou entre em contato com o administrador da Braze.
{% endalert %}

1. **Verifique seu endereço de e-mail:** Peça a um administrador que confirme se o e-mail da sua conta está correto em **Settings** > **Company Users**. O link de redefinição é enviado para o e-mail registrado no sistema.
2. **Verifique as pastas de spam e lixo eletrônico:** Procure e-mails de `@alerts.braze.com` na sua pasta de spam ou lixo eletrônico.
3. **Verifique os filtros de e-mail da TI:** Confirme com sua equipe de TI que e-mails de `@alerts.braze.com` não estão sendo bloqueados ou filtrados.
4. **Confirme a instância correta do dashboard:** Verifique se você está solicitando a redefinição a partir da [instância correta do dashboard da Braze]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints). Consulte o administrador da sua conta ou o gerente de sucesso do cliente da Braze se não tiver certeza.
5. **Tente um navegador diferente:** Algumas extensões ou configurações do navegador podem interferir no processo de redefinição de senha. Tente usar um navegador diferente ou uma janela anônima.

Os links de redefinição de senha expiram duas horas após o envio do e-mail. Se o seu link expirou, solicite uma nova redefinição na página de login.

Se nenhuma dessas etapas funcionar, um administrador pode excluir e recriar sua conta de usuário como alternativa. Para saber mais, consulte [Gerenciar usuários da empresa]({{site.baseurl}}/user_guide/administer/global/user_management/manage_company_users).

{% alert note %}
Excluir e recriar uma conta de usuário redefine as permissões e pode afetar a atribuição de ativos para Campaigns, Canvas e outros conteúdos que pertenciam anteriormente a esse usuário.
{% endalert %}

### Limpeza do cache e dos cookies do navegador {#clearing-your-browser-cache-and-cookies}

Se você está enfrentando problemas com o desempenho do dashboard, como a lista de desempenho do dashboard ou de Segment que não carrega, tente limpar o cache e os cookies do navegador seguindo as etapas para o seu respectivo navegador.

{% alert important %}
Limpar os cookies faz logout da sua sessão, então qualquer trabalho não salvo será perdido.
{% endalert %}

- [Limpar cache e cookies no Chrome](https://support.google.com/accounts/answer/32050?hl=en&co=GENIE.Platform%3DDesktop)
- [Limpar cookies no Safari no Mac](https://support.apple.com/en-gb/guide/safari/sfri11471/16.1/mac/13.0)
- [Limpar cookies e dados de sites no Firefox](https://support.mozilla.org/en-US/kb/clear-cookies-and-site-data-firefox)
- [Excluir todos os cookies no Microsoft Edge](https://support.microsoft.com/en-us/windows/manage-cookies-in-microsoft-edge-view-allow-block-delete-and-use-168dab11-0753-043d-7c16-ede5947fc64d#bkmk_deleteallcookies)

Se limpar o cache e os cookies do navegador não resolver seus problemas, entre em contato com o [Suporte]({{site.baseurl}}/support_contact).

### Erro "Aw, Snap!" no Google Chrome {#aw-snap-error-in-google-chrome}

Se o Google Chrome exibe o erro "Aw, Snap!", o Chrome está com dificuldades para carregar a página do dashboard da Braze. Para etapas de solução de problemas, consulte [Obtenha ajuda com mensagens de erro comuns no Chrome](https://support.google.com/chrome/answer/95669?co=GENIE.Platform%3DDesktop&hl=en).

### "Please Refresh Page" ou "Unexpected Error" ao navegar pelo dashboard {#please-refresh-page-or-unexpected-error-while-navigating-the-dashboard}

Esse erro pode aparecer quando um usuário da empresa não pertence a nenhum espaço de trabalho. Para solucionar:

1. Acesse a página [Usuários da empresa]({{site.baseurl}}/user_guide/administer/global/user_management/manage_company_users).
2. Verifique se o usuário foi adicionado a um espaço de trabalho.
3. Se ele não faz parte de nenhum espaço de trabalho, adicione-o e atribua as permissões apropriadas.
4. Peça ao usuário para atualizar o dashboard.
5. Se o problema persistir, entre em contato com o [Suporte]({{site.baseurl}}/support_contact).

### Acesso ao editor de arrastar e soltar {#accessing-the-drag-and-drop-editor}

Para a maioria dos usuários da empresa, o editor de arrastar e soltar deve carregar normalmente. No entanto, se você está usando uma VPN ou está atrás de um firewall, pode ser necessário adicionar um domínio à lista de permissões. Entre em contato com o administrador de TI para verificar se `*.bz-rndr.com` está na lista de permissões.

O editor pode apresentar problemas de carregamento devido ao seguinte:

- **Erro transitório:** São falhas temporárias que podem afetar conectividade, comunicação ou transferência de dados. Felizmente, geralmente se resolvem sozinhas sem exigir intervenção significativa, pois costumam ser causadas por condições passageiras e não indicam problemas sistêmicos.
- **Erro grave:** Pode envolver um problema de infraestrutura ou produto subjacente. Você pode verificar nossa [página de status do sistema Braze](https://braze.statuspage.io/), pois provavelmente já estamos cientes da situação e trabalhando ativamente para resolvê-la.

{% alert important %}
Se você ainda estiver enfrentando problemas, [abra um ticket de suporte]({{site.baseurl}}/user_guide/administer/personal/braze_support). Antes de fazer isso, confirme com o administrador de TI que `*.bz-rndr.com` está na lista de permissões da sua rede.
{% endalert %}

### Acesso ao Braze Learning {#accessing-braze-learning}

Se você está enfrentando problemas para fazer login no Braze Learning e se encontra preso em um loop que redireciona para o dashboard, siga estas etapas:

1. Se você tem várias contas Braze, fazer login com a conta errada duas vezes envia você para o dashboard da Braze. Confirme que está fazendo login na conta correta.
2. Se você tem um bloqueador de anúncios, confirme que ele está desativado. Ele pode bloquear cookies necessários para a funcionalidade de logon único.
3. Acesse **Settings** > **Company Settings** > **Admin Settings** > **Security Settings** e verifique se o logon único (SSO) está ativado.
4. Confirme que o perfil de usuário do seu dashboard inclui nome e sobrenome. Não ter sobrenome pode interromper o processo de login.
5. Acesse o Braze Learning pelo seu dashboard em **Support** > **Braze Learning**.
6. Se os problemas persistirem, considere recriar sua conta. Usuários que acessaram o Braze Learning durante a fase de teste gratuito podem ter dificuldades para acessá-lo agora.

### Problemas com autenticação de dois fatores (2FA) {#two-factor-authentication-2fa-issues}

Se um usuário está enfrentando problemas com a autenticação de dois fatores (2FA) e não consegue acessar o dashboard da Braze, isso pode ter vários motivos. Na maioria das vezes, o usuário pode não ter mais acesso ao número de telefone registrado ou ao dispositivo onde o app Authy está instalado.

Um administrador deve redefinir a 2FA para o usuário afetado fazendo o seguinte:

1. Acesse **Settings** > **User Management**.
2. Selecione o usuário com problemas de 2FA.
3. Em **Two Factor Authentication**, selecione **Reset**.
4. Confirme a redefinição da 2FA quando solicitado.
5. Se a redefinição não resolver o problema imediatamente, limpe seus cookies e cache.

A Braze não pode redefinir a 2FA em nome dos usuários por motivos de segurança. Portanto, se o administrador não conseguir redefinir a 2FA, crie um ticket de suporte.

#### Considerações {#considerations}

- Se a 2FA é obrigatória no nível da empresa: após a redefinição, a Braze solicita que o usuário configure sua 2FA novamente no próximo login.
- Se a 2FA não é obrigatória no nível da empresa: o usuário faz login no dashboard sem precisar configurar a 2FA novamente. Se ele quiser ativar a 2FA, pode fazer isso nas configurações da conta.

{% alert note %}
Esse processo de redefinição também se aplica a usuários que foram bloqueados da conta por solicitar muitos tokens na última hora.
{% endalert %}

### Conta bloqueada {#locked-out-of-account}

Se você está bloqueado da sua conta Braze, pode recuperar o acesso seguindo estas etapas.

Você pode identificar o tipo de bloqueio pela mensagem de erro que recebe:

- [Vejo um erro sobre minha senha.](#password-error)
- [Não vejo um erro, mas a Braze ainda não me deixa entrar.](#instance-error)
- [Vejo um erro sobre suspensão da conta.](#account-suspension)

#### Erro de senha {#password-error}

A segurança da sua conta é importante para nós, e senhas são obrigatórias para fazer login na sua conta Braze.
- Verifique se está fazendo login na [instância correta do dashboard da Braze]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints). Consulte o administrador da sua conta ou o gerente de sucesso do cliente da Braze para confirmar.
- Sua senha pode ter expirado, então você precisa [redefini-la](#resetting-your-password).
- Se você usa um serviço de [logon único]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup), verifique com o administrador da conta se a configuração foi concluída corretamente.
- Se sua empresa possui várias instâncias da Braze, pode estar usando o e-mail incorreto para fazer login.

Em caso de dúvida, você pode sempre [redefinir sua senha](#resetting-your-password).

#### Erro de instância {#instance-error}

Se você está usando a mesma máquina que normalmente usa para fazer login, a Braze deve detectar automaticamente a instância correta. No entanto, se isso não acontecer ou se você está fazendo login pela primeira vez, considere o seguinte:

- Verifique se está fazendo login na [instância correta do dashboard da Braze]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints). Consulte o administrador da sua conta ou o gerente de sucesso do cliente da Braze para confirmar.
- Se sua empresa possui várias instâncias da Braze, pode estar usando o e-mail incorreto para fazer login.

#### Suspensão da conta {#account-suspension}

Isso não acontece com frequência, mas a Braze leva a suspensão e exclusão de contas muito a sério. Se você encontrar um erro "Account has been banned" ao tentar fazer login, sua conta do dashboard está temporariamente suspensa. Isso pode acontecer por vários motivos.

| Motivo | Descrição |
| --- | --- |
| Problemas de pagamento | A conta da sua empresa na Braze pode ter questões de cobrança ou pagamento não resolvidas. |
| Violações de política | A conta pode ter violado os termos de serviço ou as políticas de uso aceitável da Braze. |
| Preocupações de segurança | Atividade suspeita pode ter acionado uma suspensão automática por motivos de segurança. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Motivo da suspensão da conta" }

Para resolver esse problema, entre em contato com o administrador da Braze da sua empresa, o gerente de sucesso do cliente da Braze ou o [Suporte]({{site.baseurl}}/support_contact).

### O dashboard da Braze não carrega ou não funciona como esperado {#braze-dashboard-wont-load-or-work-as-expected}

Primeiro, teste se o dashboard carrega em um navegador diferente. Se o problema não persistir em outro navegador, tente o seguinte:

- **Reinicie o dashboard:** Faça logout, feche o navegador e tente fazer login novamente no dashboard.
- **Atualize o cache local do navegador:** [Limpe seus cookies e o cache do navegador](#clearing-your-browser-cache-and-cookies) e tente fazer login novamente no dashboard.
- **Use plugins ou ferramentas de terceiros compatíveis:** Bloqueadores de anúncios ou softwares de segurança podem impedir o carregamento do dashboard da Braze. Teste desativando o bloqueador de anúncios e fazendo login no dashboard da Braze.
        - Você também pode verificar os logs do console do navegador. Erros relacionados a `ERR_BLOCKED_BY_CLIENT` podem indicar que o conteúdo está sendo bloqueado por um bloqueador de anúncios.
- **Verifique a qualidade da conexão:** A qualidade da sua conexão pode estar baixa. Tente fazer login no dashboard da Braze em um dispositivo diferente.
- **Confirme que está acessando o cluster correto:** Verifique se está fazendo login no cluster atribuído à sua empresa. Por exemplo, você pode estar atribuído ao US-03, mas fazendo login no US-01.
- **Atualize o navegador:** Atualize o navegador para a versão mais recente dos [navegadores compatíveis](#supported-browsers) e tente fazer login no dashboard.

Se o problema ocorrer em todos os navegadores, tente o seguinte:

- **Verifique sua conexão de rede:** Tente desativar sua VPN, se possível, ou desabilite e reabilite sua conexão de rede.
- **Reinicie o dispositivo:** Tente fazer login no dashboard da Braze após reiniciar o dispositivo.

Se você resolveu os problemas anteriores e o dashboard ainda não carrega ou funciona como esperado, entre em contato com o [Suporte]({{site.baseurl}}/user_guide/administer/personal/braze_support).

### O usuário não pertence a nenhum espaço de trabalho {#the-user-belongs-to-no-workspace}

Administradores podem resolver isso acessando **Settings** > **User Management**, verificando as permissões do usuário no nível do espaço de trabalho e adicionando os espaços de trabalho necessários em **Workspaces**.

### Solução de problemas para novos usuários {#troubleshooting-as-a-new-user}

Se você é um novo usuário da Braze e está tendo dificuldades para fazer login ou acessar sua conta pela primeira vez, siga estas etapas para resolver problemas comuns:

#### Não recebi o e-mail de boas-vindas {#i-never-received-the-welcome-email}

- Verifique sua pasta de spam: Confirme se o e-mail de ativação da conta não foi filtrado para a pasta de spam ou lixo eletrônico.
- Verifique seu endereço de e-mail: Peça ao seu administrador que verifique o endereço de e-mail associado à sua nova conta Braze para confirmar que está correto.
- Políticas de TI: Confirme com sua equipe de TI se não existem políticas que possam impedir o recebimento do e-mail de ativação.

#### Recebi o e-mail, mas estou com problemas na configuração da autenticação de dois fatores (2FA) {#i-received-the-email-but-im-stuck-setting-up-two-factor-authentication-2fa}

Se você seleciona **Start setup** durante a configuração da 2FA, mas nunca recebe um código de verificação (por SMS ou e-mail) ou não consegue concluir a configuração do app de autenticação, extensões de navegador, configurações de cookies ou restrições de rede podem estar interferindo. Tente o seguinte:

- Desative bloqueadores de anúncios e ative cookies de terceiros: Bloqueadores de anúncios ou extensões de privacidade podem bloquear o fluxo de verificação da 2FA. Desative-os temporariamente e confirme que cookies de terceiros estão ativados nas configurações do seu navegador.
- Tente um navegador diferente: Mude para um navegador diferente para descartar problemas específicos do navegador.
- Troque de rede: Se você está em uma rede corporativa, políticas de firewall podem interferir na configuração da 2FA. Tente mudar para uma conexão pessoal ou um hotspot móvel.
- Instale um app de autenticação antes da configuração no navegador: Baixe e instale um app de autenticação (como Authy, Google Authenticator ou LastPass Authenticator) no seu dispositivo móvel antes de selecionar **Authenticator app** durante a configuração.
- Exclua perfis de autenticação obsoletos: Se você iniciou anteriormente a configuração do app de autenticação, mas ela não foi concluída, exclua quaisquer perfis obsoletos no seu app e escaneie novamente o QR code.

Se você continuar com dificuldades após tentar essas etapas:

- Redefinir 2FA: Seu administrador pode redefinir a 2FA para sua conta de usuário nas configurações.
- Readicionar usuário: Se os problemas persistirem, o administrador pode excluir sua conta de usuário do dashboard e readicioná-lo. Isso permite a criação do usuário com os mesmos dados.

Se os problemas continuarem após essas etapas, entre em contato com o [Suporte]({{site.baseurl}}/user_guide/administer/personal/braze_support) para obter assistência adicional.

## Próximas etapas {#next-steps}

Depois de acessar sua conta, explore estes recursos:

{% article_tiles %}
- name: O dashboard da Braze
  link: /docs/user_guide/administer/personal/the_braze_dashboard
- name: Configurações de idioma
  link: /docs/user_guide/administer/personal/language_settings
{% endarticle_tiles %}