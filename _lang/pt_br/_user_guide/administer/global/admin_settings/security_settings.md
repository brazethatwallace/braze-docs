---
nav_title: Configurações de segurança
article_title: Configurações de segurança
page_order: 2
toc_headers: h2
page_type: reference
description: "Este artigo de referência aborda configurações genéricas de segurança entre empresas, incluindo regras de autenticação, lista de permissões de IP, IPI e autenticação de dois fatores (2FA)."
---

# Configurações de segurança {#security-settings}

> Como administrador, a segurança é uma alta prioridade na sua lista de preocupações. A página **Configurações de segurança** pode ajudar você a gerenciar as configurações de segurança genéricas e entre empresas, incluindo regras de autenticação, lista de permissões de IP e autenticação de dois fatores.

Para acessar essa página, acesse **Configurações** > **Configurações da empresa** > **Configurações de administrador** > **Configurações de segurança**.

## Regras de autenticação {#authentication-rules}

### Comprimento da senha {#password-length}

Use este campo para alterar o comprimento mínimo exigido para senhas. O mínimo padrão é de oito caracteres.

### Complexidade da senha {#password-complexity}

Selecione **Exigir senhas complexas** para exigir que as senhas incluam pelo menos um de cada um dos seguintes:
- Letra maiúscula
- Letra minúscula
- Número
- Caractere especial (qualquer caractere que não seja uma letra ou número, como `!`, `@`, `#` ou `(`)

### Reutilização de senha {#password-re-usability}

Determina o número mínimo de novas senhas que devem ser definidas antes que um usuário possa reutilizar uma senha. O padrão é três.

### Regras de expiração de senha {#password-expiration-rules}

Use este campo para definir quando você deseja que os usuários da sua conta Braze redefinam suas senhas.

### Regras de duração da sessão {#session-duration-rules}

Use este campo para definir por quanto tempo a Braze manterá sua sessão ativa. Depois que a Braze considerar sua sessão inativa (sem atividade pelo número definido de minutos), a Braze fará o logout do usuário. O número máximo de minutos que você pode inserir é 10.080 (equivalente a uma semana) se a autenticação de dois fatores estiver ativada para a sua empresa; caso contrário, a duração máxima da sessão é de 1.440 minutos (equivalente a 24 horas).

### Autenticação por login único (SSO) {#single-sign-on-sso-authentication}

Você pode restringir seus usuários a fazer login usando uma senha ou SSO.

Para [SSO SAML]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on), os clientes precisam definir suas configurações SAML antes de aplicar a restrição. Se os clientes usam SSO do Google, eles só precisam aplicar a página de configurações de segurança sem nenhum esforço adicional.

## Lista de permissões de IP do dashboard {#dashboard-ip-allowlisting}

Use o campo exibido para adicionar à lista de permissões endereços IP e sub-redes específicos a partir dos quais os usuários podem fazer login na sua conta (por exemplo, a partir de uma rede corporativa ou VPN). Especifique endereços IP e sub-redes como intervalos CIDR em uma lista separada por vírgulas. Se não for especificado, os usuários poderão fazer login a partir de qualquer endereço IP.

## Autenticação de dois fatores (2FA) {#two-factor-authentication-2fa}

A autenticação de dois fatores é obrigatória para todos os usuários da empresa. Ela adiciona um segundo nível de verificação de identidade ao login de uma conta, tornando-o mais seguro do que apenas um nome de usuário e uma senha. Se o seu dashboard não oferecer suporte à autenticação de dois fatores, entre em contato com o seu CSM.

Quando a autenticação de dois fatores está ativada:

- Além de inserir uma senha, os usuários precisam inserir um código de verificação ao fazer login na conta da Braze. O código pode ser enviado por um app autenticador, e-mail ou SMS.
- A caixa de seleção **Lembrar desta conta por 30 dias** fica disponível para os usuários.

A Braze bloqueia o acesso de usuários que não configurarem a autenticação de dois fatores na conta da Braze. Os usuários da conta da Braze também podem configurar a autenticação de dois fatores por conta própria em **Configurações da conta**, mesmo que não seja exigido pelo administrador.

Não se esqueça de salvar suas alterações antes de sair da página!

### Lembrar desta conta por 30 dias {#remember-me}

Esse recurso está disponível quando a autenticação de dois fatores está ativada.

Ao selecionar **Lembrar desta conta por 30 dias**, um cookie é armazenado no seu dispositivo, exigindo que você faça login com autenticação de dois fatores apenas uma vez ao longo de 30 dias.

![Caixa de seleção Lembrar desta conta por 30 dias]({% image_buster /assets/img/remember_me.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

Clientes com várias contas em uma mesma empresa no dashboard podem ter problemas ao usar esse recurso, pois o cookie está vinculado a um dispositivo específico. Se os usuários usarem o mesmo dispositivo para fazer login em várias contas, o cookie será substituído para as contas previamente autorizadas naquele dispositivo. A Braze espera que apenas um dispositivo esteja associado a uma conta, e não um dispositivo para várias contas.

### Redefinição da autenticação do usuário {#resetting-user-authentication}

Se você estiver com dificuldades para fazer login com a autenticação de dois fatores, entre em contato com os administradores da sua empresa para redefinir sua autenticação de dois fatores. Os administradores podem realizar as seguintes etapas:

1. Acessar **Configurações** > **Configurações da empresa** > **Gerenciamento de usuários** > **Usuários da empresa**.
2. Selecionar o usuário na lista fornecida.
3. Selecionar **Redefinir** em **Autenticação de dois fatores**.

Uma redefinição pode resolver problemas comuns de autenticação, como dificuldades com apps autenticadores, e-mail de verificação que não é enviado, falha no login devido a interrupções de SMS ou erro do usuário, entre outros.

### Requisitos para 2FA no nível da empresa {#requirements-for-2fa-at-the-company-level}

Primeiro, verifique se a 2FA está ativada no seu dashboard acessando **Configurações** > **Configurações da empresa** > **Configurações de administrador** > **Configurações de segurança** > **Autenticação de dois fatores**. Se o botão de alternância estiver cinza, a 2FA não foi ativada para a sua empresa e não é obrigatória para todos os usuários da empresa.

#### Opções do usuário quando a 2FA não é obrigatória {#user-options-when-2fa-isnt-mandatory}

Se a 2FA não for obrigatória no nível da empresa, os usuários individuais podem configurar a 2FA por conta própria na página de configurações da conta. Nesse caso, os usuários não serão bloqueados de suas contas se não configurarem. Você pode identificar quais usuários optaram por ativar a 2FA verificando a lista de **Usuários da empresa**.

#### Requisitos quando a 2FA é obrigatória {#requirements-when-2fa-is-mandatory}

Se a 2FA for obrigatória no nível da empresa, os usuários que não a configurarem em suas próprias contas ao fazer login serão bloqueados do dashboard. Os usuários devem concluir a configuração da 2FA para manter o acesso.

{% alert important %}
A 2FA é obrigatória para todos os usuários da empresa somente se o Single Sign-On (SSO) não estiver ativado. Se o SSO estiver em uso, a 2FA não precisa ser obrigatória no nível da empresa.
{% endalert %}

## Configurar a 2FA manualmente {#manually-set-up-2fa}

Para ativar manualmente a autenticação de dois fatores (2FA) na sua conta da Braze, siga estas etapas:

1. Na Braze, selecione o ícone do seu perfil no cabeçalho global e, em seguida, selecione **Gerenciar sua conta**. Role até a seção **Two-Factor Authentication** e selecione **Start Setup**.
2. Insira sua senha no modal de login e selecione **Check Password**.
3. No modal **Two-Factor Authentication Setup**, insira seu número de telefone e selecione **Enable**.
4. Copie o código de sete dígitos gerado no seu e-mail ou mensagem SMS, volte à Braze e cole-o no modal **Two-Factor Authentication Setup**. Selecione **Verify**.
5. (Opcional) Para não precisar inserir a 2FA pelos próximos 30 dias, ative a opção **Remember this account for 30 days**.

## Acesso elevado {#elevated-access}

O Acesso elevado adiciona uma camada extra de segurança para ações sensíveis no dashboard da Braze. Quando ativo, os usuários precisam verificar novamente a conta antes de exportar um Segment ou visualizar uma chave de API. Para usar o Acesso elevado, acesse **Configuração** > **Configurações da empresa** > **Configuração de administrador** > **Configurações de segurança** e ative a opção.

Se um usuário não conseguir fazer a reverificação, ele será redirecionado para onde estava e não poderá continuar com a ação sensível. Após a reverificação bem-sucedida, não será necessário repetir o processo na próxima hora, a menos que ele faça logout primeiro.

## Download de relatório de eventos de segurança {#security-event-report}

O relatório de eventos de segurança é um relatório CSV de eventos de segurança, como convites de conta, remoções de conta, tentativas de login bem-sucedidas e malsucedidas, e outras atividades. Você pode usá-lo para realizar auditorias internas.

Para baixar esse relatório, faça o seguinte:

1. Acesse **Configurações** > **Configurações da empresa** > **Configurações de administrador** > **Configurações de segurança**.
2. Vá até a seção **Download de eventos de segurança**.
3. Selecione **Baixar relatório**.

Esse download manual de relatório contém apenas os 10.000 eventos de segurança mais recentes da sua conta. Se o CSV exportado contiver exatamente 10.001 linhas (incluindo a linha de cabeçalho), você atingiu o limite de 10.000 eventos do relatório e eventos mais antigos podem não estar incluídos.

Para exportar eventos de segurança para o Amazon S3 sem esse limite de linhas, consulte [Exportação de eventos de segurança com Amazon S3]({{site.baseurl}}/user_guide/administer/global/admin_settings/security_settings/security_export_s3).

### Definições das colunas do CSV {#csv-column-definitions}

O CSV do relatório de eventos de segurança contém as seguintes colunas:

| Coluna | Descrição |
|--------|-------------|
| CreatedAt | Timestamp de quando o evento foi registrado, em UTC. |
| EmailAtTimeOfEvent | Endereço de e-mail do usuário do dashboard que disparou o evento, conforme registrado no momento do evento. |
| CurrentEmail | Endereço de e-mail atual do usuário do dashboard que disparou o evento. Se o usuário não existir mais, o ID de desenvolvedor é usado. |
| EventName | Tipo de evento de segurança. Consulte o menu suspenso **Eventos de segurança reportados** após esta tabela. |
| OtherAccount | Endereço de e-mail de outro usuário do dashboard afetado pelo evento, quando aplicável (por exemplo, quando uma conta é adicionada ou removida). |
| JsonProperties | Propriedades específicas do evento em formato JSON. Os campos incluídos variam por tipo de evento. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Definições das colunas do CSV" }

As [exportações para S3]({{site.baseurl}}/user_guide/administer/global/admin_settings/security_settings/security_export_s3) incluem essas colunas mais `Version`, a versão do esquema para o formato de exportação (atualmente `1`).

{% details Eventos de segurança reportados %}
### Login e conta {#login-and-account}
- Signed In
- Failed Login
- Two-Factor Auth Setup Completed
- Two-Factor Auth Reset Completed
- Cleared Developer 2FA
- Added Additional Developer
- Added Account
- Developer Suspended
- Developer Unsuspended
- Developer Updated
- Removed Developer
- Removed Account
- User Subscription Status Updated
- User Updated
- Developer Account Updated

### Acesso elevado
- Started Elevated Access Flow
- Completed Elevated Access Flow
- Failed 2FA Verification For Elevated Access
- Enabled Elevated Access Enforcement
- Disabled Elevated Access Enforcement

Campaign
- Added Campaign
- Edited Campaign

Canvas
- Added Canvas
- Edited Canvas

### Segment
- Added Segment
- Edited Segment
- Exported data to CSV
- Exported Segment via API
- Segment Users Deleted
- Cleared Cohort

### Chave da API REST {#rest-api-key}
- Added REST API key
- Removed REST API key

### Credencial de autenticação básica {#basic-authentication-credential}
- Added Basic Auth credential
- Updated Basic Auth credential
- Removed Basic Auth credential

### Permissão {#permission}
- Cleared Developer 2FA
- Updated Account Permission
- Added Team
- Edited Team
- Archived Team
- Unarchived Team
- Created App Group Permission Set
- Edited App Group Permission Set
- Removed App Group Permission Set
- Created Custom Role
- Updated Custom Role
- Deleted Custom Role

### Configurações da empresa {#company-settings}
- Added App Group
- Added App
- Company Settings Changed
- Updated Company Security Settings
- Updated Security Event Cloud Export
- Added Landing Pages Custom Domain
- Removed Landing Pages Custom Domain
- Custom Domain Created
- Custom Domain Deleted
- Enabled Global Control Group
- Disabled Global Control Group
- Updated Global Control Exclusions
- Updated Subscription Group SMS Allow List

### Modelo de e-mail {#email-template}
- Added Email Template
- Updated Email Template

### Credencial de push {#push-credential}
Updated Push Credential
Removed Push Credential

### Depurador do SDK {#sdk-debugger}
- Started SDK Debugger Session
- Exported SDK Debugger Log

### Usuários {#users}
- Users Deleted
- Users Viewed
- User Import Started
- User Subscription Group Status Updated
- User Deleted
- Single User Deletion Cancelled
- Bulk User Deletion Cancelled

### Catálogos {#catalogs}
- Catalog Created
- Catalog Deleted

### Braze Agents
- Created Agent
- Edited Agent

### BrazeAI Operator
- Requested BrazeAI Operator Response
- BrazeAI Operator Responded
{% enddetails %}

## Visualização de informações pessoais identificáveis (IPI) {#view-pii}

A permissão **Visualizar IPI** é acessível apenas a alguns usuários selecionados da empresa. Por padrão, todos os administradores têm a permissão **Visualizar IPI** ativada nas permissões de usuário. Isso significa que eles podem ver todos os atributos padrão e personalizados que sua empresa definiu como IPI em todo o dashboard. Quando essa permissão é desativada para os usuários, eles não poderão ver nenhum desses atributos.

{% alert note %}
Você precisa da permissão **Visualizar IPI** para usar o [Criador de consultas]({{site.baseurl}}/user_guide/analytics/reports/query_builder/building_queries), pois ele permite acesso direto a alguns dados de clientes.
{% endalert %}

Para as capacidades existentes de permissão de equipe, consulte [Definição de permissões de usuário]({{site.baseurl}}/user_guide/administer/global/user_management/permissions).

### Definição de IPI {#defining-pii}

{% alert important %}
Selecionar e definir determinados campos como campos de IPI afeta apenas o que os usuários podem visualizar no dashboard da Braze e não impacta como os dados do usuário final nesses campos de IPI são tratados.<br><br>Consulte sua equipe jurídica para alinhar as configurações do seu dashboard com quaisquer regulamentações e políticas de privacidade aplicáveis à sua empresa, incluindo aquelas relacionadas à [retenção de dados]({{site.baseurl}}/data_retention).
{% endalert %}

Você pode selecionar os campos que sua empresa designa como IPI no dashboard. Para fazer isso, acesse **Configurações** > **Configurações da empresa** > **Configurações de administrador** > **Configurações de segurança**.

Os seguintes atributos podem ser designados como IPI e ocultados dos usuários da empresa que não possuem permissões de **Visualizar IPI**.

#### Atributos potenciais de IPI {#potential-pii-attributes}

| Atributos padrão | Atributos personalizados |
| ------------------- | ----------------- |
| {::nomarkdown}<ul> <li>Endereço de e-mail </li> <li> Número de telefone </li> <li> Nome </li> <li> Sobrenome </li> <li> Gênero </li> <li> Data de nascimento </li> <li> IDs de dispositivo </li> <li> LINE ID </li> <li> Localização mais recente </li> </ul> {:/} | {::nomarkdown} <ul> <li> Todos os atributos personalizados<ul><li>Atributos personalizados individuais podem ser marcados como IPI se você não precisar ocultar todos os atributos.</li></ul></li> </ul> {:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Atributos potenciais de IPI" }

### Áreas limitadas {#limited-areas}

O seguinte pressupõe que todos os campos estão definidos como IPI, e os usuários mencionados são usuários da empresa que utilizam a plataforma Braze. Além disso, os atributos "anteriores" referem-se àqueles na tabela [Atributos potenciais de IPI](#potential-pii-attributes). Remover permissões de IPI de um usuário pode impactar a usabilidade além dessas áreas listadas.

| Navegação no dashboard | Resultado | Notas |
| -------------------- | ------ | ----- |
| Pesquisa de usuários | O usuário que faz login não consegue pesquisar por endereço de e-mail, número de telefone, nome ou sobrenome: {::nomarkdown} <ul> <li> Não verá os atributos padrão e personalizados anteriores ao visualizar um perfil de usuário. </li> <li> Não poderá editar os atributos padrão anteriores de um perfil de usuário no dashboard da Braze. </li> <li> Não poderá atualizar o status de inscrição em um perfil de usuário. </li></ul> {:/} | O acesso a esta seção ainda requer acesso para visualizar um perfil de usuário. |
| Importação de usuários | O usuário não pode baixar arquivos da página **Importação de usuários**. | |
| {::nomarkdown} <ul> <li> Segments </li> <li> Campaigns </li> <li> Canvas </li> </ul> {:/} | No menu suspenso **Dados de usuários**: {::nomarkdown} <ul> <li> O usuário não terá a opção <b>Exportar endereços de e-mail em CSV</b>. </li> <li> O usuário não receberá os atributos padrão e personalizados anteriores no arquivo CSV ao selecionar <b>Exportar dados de usuários em CSV</b>. </li> </ul> {:/} | |
| Grupo de teste interno | O usuário não terá acesso aos atributos padrão anteriores de qualquer usuário adicionado ao grupo de teste interno. | |
| Registro de atividades de envio de mensagem | O usuário não terá acesso aos atributos padrão anteriores de quaisquer usuários identificados no registro de atividades de envio de mensagem. | |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Áreas limitadas" }

{% alert note %}
Ao pré-visualizar uma mensagem, a permissão **Visualizar IPI** não é aplicada, então os usuários podem ver os [atributos padrão anteriores](#potential-pii-attributes) se eles foram referenciados na mensagem por meio de Liquid.
{% endalert %}

## Preferências de exclusão de dados {#data-deletion-preferences}

Você pode usar esta configuração para definir preferências sobre se a Braze deve excluir determinados campos durante o processo de exclusão de usuários para eventos. Essas preferências afetam apenas os dados de usuários que a Braze excluiu.

Quando um usuário é excluído, a Braze remove todas as IPI dos dados de eventos, mas retém os dados anonimizados para fins de análise de dados. Alguns campos definidos pelo usuário podem conter IPI se você enviar informações do usuário final para a Braze. Se esses campos contiverem IPI, você pode optar por excluir os dados quando a Braze anonimizar os dados de eventos de usuários excluídos; se os campos não contiverem IPI, você pode mantê-los para análise de dados.

Você é responsável por determinar as preferências corretas para o seu espaço de trabalho. A melhor maneira de determinar as configurações apropriadas é revisar com as equipes internas que enviam dados de eventos para a Braze e com as equipes que usam extras de mensagens na Braze para confirmar se os campos podem conter IPI.

### Campos relevantes {#relevant-fields}

| Nome ou tipo do evento | Campo | Notas |
| -------------------- | ------ | ----- |
| Evento personalizado | properties |  |
| Evento de compra | properties |  |
| Envio de mensagem | message_extras | Vários tipos de evento contêm um campo `message_extras`. A preferência se aplica a todos os tipos de evento de envio de mensagem que suportam `message_extras`, incluindo tipos de evento adicionados no futuro. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Campos relevantes" }

{% alert warning %}
**A exclusão é permanente!** Se você optar por remover quaisquer campos do Snowflake para usuários excluídos, a configuração se aplica a todos os dados históricos nos seus espaços de trabalho e a quaisquer eventos de usuários excluídos no futuro. Depois que a Braze executar o processo para aplicar as configurações aos dados históricos de eventos de usuários excluídos, você **não poderá recuperar** os dados.
{% endalert %}

### Configurar preferências {#configure-preferences}

Defina as preferências padrão marcando as caixas de seleção de quaisquer campos que a Braze deve remover caso um usuário seja excluído. Selecione quaisquer campos que contenham IPI. Essa preferência se aplica a todos os espaços de trabalho atuais e futuros, a menos que espaços de trabalho sejam adicionados explicitamente a um grupo de preferências.

Para personalizar preferências por espaço de trabalho, você pode adicionar grupos de preferências com configurações diferentes do padrão. As configurações padrão são aplicadas a quaisquer espaços de trabalho que não foram adicionados a um grupo de preferências adicional, incluindo espaços de trabalho criados no futuro.

![Seção de Preferências de exclusão de dados com o botão de alternância ativado para personalizar preferências de exclusão de dados por espaço de trabalho.]({% image_buster /assets/img/deletion_preferences_1.png %})

## Solução de problemas {#troubleshooting}

### Problemas de loop na configuração da autenticação de dois fatores (2FA) {#two-factor-authentication-2fa-setup-loop-issues}

Se você ficar preso em um loop após inserir seu número de telefone para 2FA e for redirecionado de volta à página de login, isso provavelmente se deve a uma falha na verificação na primeira tentativa. Para resolver esse problema, siga estas etapas:

1. Desative bloqueadores de anúncios.
2. Ative os cookies nas configurações do navegador.
3. Reinicie seu PC ou notebook.
4. Tente configurar a 2FA novamente.

Se o problema persistir após essas etapas, entre em contato com o [Suporte]({{site.baseurl}}/user_guide/administer/personal/braze_support) para obter assistência.

### Não é possível ativar a autenticação de dois fatores (2FA) {#cant-enable-two-factor-authentication-2fa}

Se a 2FA estiver ativada, mas nada acontecer ao selecionar o botão **Enable**, isso pode ser porque seu navegador está bloqueando o redirecionamento necessário para enviar o código de verificação por SMS. Veja as etapas para solucionar esse problema:

1. Suspenda temporariamente os bloqueadores de anúncios que estiverem ativados no navegador.
2. Confirme que você ativou os cookies de terceiros nas configurações do navegador.
3. Tente configurar a 2FA.

### O código de verificação não é enviado {#verification-code-doesnt-send}

Se você tiver problemas ao inserir seu número de telefone na página do Authy e não receber um SMS, siga estas etapas:

1. Instale o app Authy no seu celular e faça login no autenticador Authy.
2. Insira seu número de telefone e verifique o app Authy em busca de alterações ou notificações por SMS.
3. Se ainda não receber o SMS, tente usar uma conexão de rede diferente, como sua rede doméstica ou uma rede Wi-Fi não corporativa. Redes corporativas podem ter políticas de segurança que interferem na entrega de SMS.

Se os problemas persistirem, exclua o perfil antigo no app Authy e escaneie o código QR novamente para configurar a 2FA. Certifique-se de que você desativou os bloqueadores de anúncios, ativou os cookies de terceiros ou usou um navegador diferente antes de tentar a configuração novamente.

## Próximos passos {#next-steps}

Para saber mais sobre autenticação e acesso, consulte:

- [SAML e login único]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on) para configurar o SSO com seu provedor de identidade.
- [Permissões]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) para controlar quais ações os usuários podem realizar no dashboard.