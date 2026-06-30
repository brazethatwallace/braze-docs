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

Seja sua primeira vez fazendo login ou a centésima, veja como acessar seu dashboard. Se você é o primeiro usuário da sua empresa, siga as orientações na seção anterior. Caso contrário, você pode fazer login após o administrador da Braze da sua empresa criar sua conta.

Você pode fazer login pelo site principal da [Braze.com](https://www.braze.com) ou usar a URL do dashboard que corresponde à sua [instância da Braze]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints) específica. Para sua conveniência, a Braze oferece várias opções de login único (SSO), como:

* [SAML SSO]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup)
    * [Provisionamento just-in-time SAML]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_just_in_time_provisioning)
* [Microsoft Entra SSO]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/microsoft_entra_sso)
* [Okta]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/okta)
* [OneLogin]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/onelogin)

Após fazer login na Braze com SSO, você não poderá mais usar sua senha para fazer login no dashboard. Ambos os endereços de e-mail direcionarão os e-mails para a mesma caixa de entrada, mas a Braze os reconhecerá como contas separadas quando você fizer login. Limpar os cookies fará logout, então trabalhos não salvos serão perdidos.

## Navegadores compatíveis {#supported-browsers}

O dashboard da Braze é compatível com os seguintes navegadores:
- Chrome (versão 87 ou mais recente)
- Firefox (versão 85 ou mais recente)
- Safari (versão 15.4 ou mais recente)
- Edge (versão 87 ou mais recente)

Se o seu dashboard da Braze exibir um erro inesperado e a ferramenta de console do navegador mostrar o erro `ReferenceError: structuredClone is not defined`, seu navegador está desatualizado. Se esse erro continuar ocorrendo, desinstale e reinstale seu navegador.

## Acessando múltiplos dashboards da Braze {#accessing-multiple-braze-dashboards}

A Braze não permite registrar o mesmo endereço de e-mail para múltiplos usuários de dashboard no mesmo cluster (por exemplo, se você tem dois dashboards no US-01). Você pode usar o mesmo e-mail para criar contas em clusters diferentes (por exemplo, se você tem um dashboard no US-01 e outro no US-05). Se você precisa acessar múltiplos dashboards da Braze no mesmo cluster, pode fazer o seguinte:

### Usar aliases de e-mail {#use-email-aliases}

Se seu provedor de e-mail é o Gmail, você pode criar aliases adicionando um sinal `+` seguido de qualquer texto ao seu endereço de e-mail. Por exemplo:
- **E-mail original:** `rocky@gmail.com`
- **E-mail alias:** `rocky+1@gmail.com`

Ambos os endereços de e-mail direcionam os e-mails para a mesma caixa de entrada, mas a Braze os reconhece como contas separadas quando você faz login.

### Criar aliases separados com outros provedores {#create-separate-aliases-with-other-providers}

Se seu provedor de e-mail não suporta aliases com `+`, você ainda pode criar aliases separados, como configurar `rocky@braze.com` para encaminhar para `rocky.lotito@braze.com`. Isso permite que múltiplos endereços direcionem para a mesma caixa de entrada enquanto são reconhecidos como e-mails diferentes pela Braze.

### Usar desenvolvedores multi-empresa {#use-multi-company-developers}

O recurso de desenvolvedores multi-empresa permite compartilhar uma única conta de usuário entre múltiplas empresas. Os usuários podem alternar entre diferentes dashboards de empresas pelo menu de perfil do usuário.

Se você usa SSO e deseja configurar desenvolvedores multi-empresa, é necessário ativar um ID de Entidade SAML personalizado configurando uma integração SAML SSO personalizada. Siga as etapas em [Login iniciado pelo prestador de serviço (SP)]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup), mas aplique estas alterações:
- Altere o **Entity ID** para `braze_dashboard_<companyID>` para cada integração de dashboard.
- Entre em contato com seu gerente de sucesso do cliente ou gerente de conta para ativar o feature flipper `saml_sso_custom_entity_id` para cada dashboard.

### Considerações para login único (SSO) {#considerations-for-single-sign-on-sso}

Se você usa login único (SSO), esteja ciente de que ter múltiplos endereços de e-mail diferentes pode gerar complicações. Confirme que suas configurações de SSO estão configuradas corretamente para evitar problemas de acesso.

## Solução de problemas {#troubleshooting}

### Redefinindo sua senha {#resetting-your-password}

Para redefinir sua senha, selecione o link **Forgot your password?** na página de login do dashboard. Você será solicitado a inserir seu e-mail para receber um link de redefinição de senha.

![Login do dashboard com o prompt "Forgot your password?".]({% image_buster /assets/img_archive/enable_reset.png %}){: style="max-width:60%"}

### Limpando o cache e os cookies do navegador {#clearing-your-browser-cache-and-cookies}

Se você está tendo problemas com o desempenho do dashboard, como o dashboard ou a lista de desempenho de segmentos não carregando, tente limpar o cache e os cookies do navegador seguindo as etapas para o seu respectivo navegador.

{% alert important %}
Limpar os cookies faz logout, então trabalhos não salvos serão perdidos.
{% endalert %}

- [Limpar cache e cookies no Chrome](https://support.google.com/accounts/answer/32050?hl=en&co=GENIE.Platform%3DDesktop)
- [Limpar cookies no Safari no Mac](https://support.apple.com/en-gb/guide/safari/sfri11471/16.1/mac/13.0)
- [Limpar cookies e dados de sites no Firefox](https://support.mozilla.org/en-US/kb/clear-cookies-and-site-data-firefox)
- [Excluir todos os cookies no Microsoft Edge](https://support.microsoft.com/en-us/windows/manage-cookies-in-microsoft-edge-view-allow-block-delete-and-use-168dab11-0753-043d-7c16-ede5947fc64d#bkmk_deleteallcookies)

Se limpar o cache e os cookies do navegador não resolver seus problemas, entre em contato com o [Suporte]({{site.baseurl}}/support_contact).

### Erro "Aw, Snap!" no Google Chrome {#aw-snap-error-in-google-chrome}

Se o Google Chrome exibir um erro "Aw, Snap!", o Chrome está com dificuldades para carregar a página do dashboard da Braze. Para etapas de solução de problemas, consulte [Obter ajuda com mensagens de erro comuns no Chrome](https://support.google.com/chrome/answer/95669?co=GENIE.Platform%3DDesktop&hl=en).

### "Please Refresh Page" ou "Unexpected Error" ao navegar no dashboard {#please-refresh-page-or-unexpected-error-while-navigating-the-dashboard}

Este erro pode aparecer quando um usuário da empresa não pertence a nenhum espaço de trabalho. Para solucionar:

1. Acesse a página [Usuários da empresa]({{site.baseurl}}/user_guide/administer/global/user_management/manage_company_users).
2. Verifique se o usuário foi adicionado a um espaço de trabalho.
3. Se não faz parte de nenhum espaço de trabalho, adicione-o e atribua as permissões apropriadas.
4. Peça ao usuário para atualizar o dashboard.
5. Se o problema persistir, entre em contato com o [Suporte]({{site.baseurl}}/support_contact).

### Acessando o editor de arrastar e soltar {#accessing-the-drag-and-drop-editor}

Para a maioria dos usuários da empresa, o editor de arrastar e soltar deve carregar normalmente. No entanto, se você está usando uma VPN ou está atrás de um firewall, pode ser necessário adicionar um domínio à lista de permissões. Entre em contato com o administrador de TI para verificar se `*.bz-rndr.com` está na lista de permissões.

O editor pode apresentar problemas de carregamento devido ao seguinte:

- **Erro transitório:** São falhas temporárias que podem afetar conectividade, comunicação ou transferência de dados. Felizmente, elas geralmente se resolvem sozinhas sem necessidade de intervenção significativa, pois são frequentemente causadas por condições de curta duração e não indicam problemas sistêmicos.
- **Erro grave:** Pode envolver um problema de infraestrutura ou produto subjacente. Você pode verificar nossa [página de status do sistema da Braze](https://braze.statuspage.io/), pois provavelmente já estamos cientes da situação e trabalhando ativamente para resolvê-la.

{% alert important %}
Se você ainda estiver enfrentando problemas, [abra um ticket de suporte]({{site.baseurl}}/user_guide/administer/personal/braze_support). Antes de fazer isso, confirme com o administrador de TI que `*.bz-rndr.com` está na lista de permissões do seu lado.
{% endalert %}

### Acessando o Braze Learning {#accessing-braze-learning}

Se você está tendo problemas para fazer login no Braze Learning e se encontra preso em um loop que redireciona para o dashboard, siga estas etapas:

1. Se você tem múltiplas contas da Braze, fazer login com a conta errada duas vezes envia você para o dashboard da Braze. Confirme que está fazendo login na conta correta.
2. Se você tem um bloqueador de anúncios, confirme que ele está desativado. Ele pode bloquear cookies necessários para a funcionalidade de login único.
3. Acesse **Configurações da empresa** > **Configurações de segurança** e verifique se o login único (SSO) está ativado.
4. Confirme que o perfil de usuário do seu dashboard inclui nome e sobrenome. Não ter um sobrenome pode interromper o processo de login.
5. Acesse o Braze Learning pelo seu dashboard em **Suporte** > **Braze Learning**.
6. Se continuar enfrentando problemas, considere recriar sua conta. Usuários que acessaram o Braze Learning durante a fase de teste gratuito podem ter dificuldades para acessá-lo agora.

### Problemas com autenticação de dois fatores (2FA) {#two-factor-authentication-2fa-issues}

Se um usuário está enfrentando problemas com a autenticação de dois fatores (2FA) e não consegue acessar o dashboard da Braze, pode ser por vários motivos. Mais comumente, ele pode não ter mais acesso ao número de telefone registrado ou ao dispositivo onde o app Authy está instalado.

Um administrador deve redefinir a 2FA para o usuário afetado fazendo o seguinte:

1. Acesse **Gerenciar usuários**.
2. Selecione **Edit User** para o usuário com problemas de 2FA.
3. Escolha a opção para redefinir a 2FA.
4. Confirme a redefinição da 2FA quando solicitado.
5. Se a redefinição não resolver o problema imediatamente, limpe seus cookies e cache.

A Braze não pode redefinir a 2FA em nome dos usuários por motivos de segurança, então se o administrador não conseguir redefinir a 2FA, crie um ticket de suporte.

#### Considerações {#considerations}

- Se a 2FA é obrigatória no nível da empresa: Após a redefinição, a Braze solicita que o usuário configure sua 2FA novamente no próximo login.
- Se a 2FA não é obrigatória no nível da empresa: O usuário faz login no dashboard sem precisar configurar a 2FA novamente. Se quiser ativar a 2FA, pode fazê-lo nas Configurações da conta.

{% alert note %}
Este processo de redefinição também se aplica a usuários que foram bloqueados de sua conta por solicitar muitos tokens na última hora.
{% endalert %}

### Bloqueado da conta {#locked-out-of-account}

Se você está bloqueado da sua conta da Braze, pode recuperar o acesso seguindo as etapas abaixo.

Você pode identificar o tipo de bloqueio pela mensagem de erro que recebe:

- [Vejo um erro sobre minha senha.](#password-error)
- [Não vejo um erro, mas a Braze ainda não me deixa entrar.](#instance-error)
- [Vejo um erro sobre suspensão de conta.](#account-suspension)

#### Erro de senha {#password-error}

A segurança da sua conta é importante para nós, então senhas são obrigatórias para fazer login na sua conta da Braze.
- Verifique se você está fazendo login na [instância correta do dashboard da Braze]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints). Confirme com o administrador da sua conta ou gerente de conta da Braze.
- Sua senha pode ter expirado, então você precisa [redefini-la](#resetting-your-password).
- Se você usa um serviço de [login único]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup), verifique com o administrador da sua conta se a configuração foi concluída corretamente.
- Se sua empresa está em várias instâncias da Braze, você pode estar usando o e-mail incorreto para fazer login.

Em caso de dúvida, você sempre pode [redefinir sua senha](#resetting-your-password).

#### Erro de instância {#instance-error}

Se você está usando a mesma máquina que normalmente usa para fazer login, a Braze deve detectar automaticamente a instância correta. No entanto, se isso não acontecer ou se você está fazendo login pela primeira vez, considere o seguinte:

- Verifique se você está fazendo login na [instância correta do dashboard da Braze]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints). Confirme com o administrador da sua conta ou gerente de conta da Braze.
- Se sua empresa está em várias instâncias da Braze, você pode estar usando o e-mail incorreto para fazer login.

#### Suspensão de conta {#account-suspension}

Isso não acontece com frequência, mas a Braze leva suspensões e exclusões de contas muito a sério. Se você encontrar esse erro, entre em contato com o administrador da Braze da sua empresa, gerente de conta da Braze ou [Suporte][support].

### O dashboard da Braze não carrega ou não funciona como esperado {#braze-dashboard-wont-load-or-work-as-expected}

Primeiro, teste se o dashboard carrega em um navegador diferente. Se o problema não persistir em outro navegador, tente o seguinte:

- **Reinicie o dashboard:** Faça logout, feche o navegador e tente fazer login no dashboard novamente.
- **Atualize o navegador local:** [Limpe seus cookies e cache do navegador](#clearing-your-browser-cache-and-cookies) e tente fazer login no dashboard novamente.
- **Use plugins ou ferramentas de terceiros compatíveis:** Bloqueadores de anúncios ou softwares de segurança podem impedir o carregamento do dashboard da Braze. Teste desativando um bloqueador de anúncios e fazendo login no dashboard da Braze.
        - Você também pode verificar os logs do console do navegador. Erros relacionados a `ERR_BLOCKED_BY_CLIENT` podem indicar que o conteúdo está sendo bloqueado por um bloqueador de anúncios.
- **Verifique a qualidade da conexão:** A qualidade da sua conexão pode estar ruim. Tente fazer login no dashboard da Braze em um dispositivo diferente.
- **Confirme que está acessando o cluster correto:** Certifique-se de que está fazendo login no cluster atribuído à sua empresa. Por exemplo, você pode estar atribuído ao US-03, mas fazendo login no US-01.
- **Atualize seu navegador:** Atualize seu navegador para o [navegador compatível](#supported-browsers) mais recente e tente fazer login no dashboard.

Se o problema ocorrer em todos os navegadores, tente o seguinte:

- **Verifique sua conexão de rede:** Tente desativar sua VPN, se possível, ou desative e reative sua conexão de rede.
- **Reinicie seu dispositivo:** Tente fazer login no dashboard da Braze após reiniciar seu dispositivo.

Se você resolveu os problemas anteriores e o dashboard ainda não carrega ou não funciona como esperado, entre em contato com o [Suporte]({{site.baseurl}}/braze_support).

### O usuário não pertence a nenhum espaço de trabalho {#the-user-belongs-to-no-workspace}

Verifique isso acessando **Configurações** > **Usuários da empresa** e verificando as permissões do usuário no nível do espaço de trabalho. Adicione os espaços de trabalho necessários em **Espaços de trabalho**.

### Solução de problemas como novo usuário {#troubleshooting-as-a-new-user}

Se você é um novo usuário da Braze com dificuldades para fazer login ou acessar sua conta pela primeira vez, siga estas etapas para resolver problemas comuns:

#### Não recebi o e-mail de boas-vindas {#i-never-received-the-welcome-email}

- Verifique sua pasta de spam: Confirme que o e-mail de ativação da conta não foi filtrado para sua pasta de spam ou lixo eletrônico.
- Verifique seu endereço de e-mail: Peça ao seu administrador para verificar o endereço de e-mail associado à sua nova conta da Braze para confirmar que está correto.
- Políticas de TI: Confirme com sua equipe de TI se não há políticas que possam impedir o recebimento do e-mail de ativação.

#### Recebi o e-mail, mas estou travado na configuração da autenticação de dois fatores (2FA) {#i-received-the-email-but-im-stuck-setting-up-two-factor-authentication-2fa}

- Redefinir 2FA: Se você está tendo problemas para configurar a 2FA, seu administrador pode redefinir a 2FA para sua conta de usuário nas configurações.
- Readicionar usuário: Se os problemas persistirem, o administrador pode excluir sua conta de usuário do dashboard e readicioná-lo. Isso permite a criação do usuário com os mesmos dados.

Se os problemas continuarem após essas etapas, entre em contato com o [Suporte]({{site.baseurl}}/braze_support) para assistência adicional.

## Próximas etapas {#next-steps}

Após acessar sua conta, explore estes recursos:

- [O dashboard da Braze]({{site.baseurl}}/user_guide/administer/personal/the_braze_dashboard) para aprender a navegar pelos principais recursos e ferramentas.
- [Configurações de idioma]({{site.baseurl}}/user_guide/administer/personal/language_settings) para definir o idioma preferido do seu dashboard.