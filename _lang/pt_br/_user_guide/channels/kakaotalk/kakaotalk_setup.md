---
nav_title: Configurar o KakaoTalk
article_title: Configurar o KakaoTalk
description: "Este artigo de referência descreve como configurar seu canal KakaoTalk, incluindo como configurar usuários, reconciliar IDs de usuário e criar usuários teste."
page_order: 0
alias: /kakaotalk_setup/
channel:
  - KakaoTalk
---

# Configurar o KakaoTalk {#set-up-kakaotalk}

> Este artigo aborda como configurar o [canal de envio de mensagens KakaoTalk]({{site.baseurl}}/kakaotalk/) na Braze, incluindo como configurar usuários, reconciliar IDs de usuário e criar usuários teste do KakaoTalk.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| --- | --- |
| Conta com um parceiro KakaoTalk compatível | É necessário ter uma conta com um parceiro KakaoTalk compatível, [CJ OliveNetworks](https://www.braze.com/partners/solutions-partners/cjolivenetworks/) ou Infobip, para usar o canal de envio de mensagens KakaoTalk. |
| Canal Business do KakaoTalk | Sua conta KakaoTalk deve ser um canal Business do KakaoTalk para enviar mensagens KakaoTalk pela Braze. Quando você cria uma conta, o status padrão é básico. Para tornar sua conta um canal Business, você precisará verificar sua empresa e fornecer a documentação relevante. |
| Sender Key do KakaoTalk | Um Sender Key válido do KakaoTalk. |
| Número de telefone de contato | Um número de telefone de contato para o administrador do seu canal KakaoTalk. |
| IPs do cluster da Braze na lista de permissões | O registro na lista de permissões de IP é obrigatório para todos os clientes. Registre os endereços IP da Braze para o seu cluster antes de integrar o KakaoTalk na Braze. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

### Registrar endereços IP da Braze {#register-braze-ip-addresses}

Registre os endereços IP da Braze para o seu cluster no dashboard Comm.One.

1. No dashboard Comm.One, acesse **Account Management (계정 관리)**, selecione o ícone de menu e depois selecione **View Details (자세히보기)**.
2. Selecione **Center & Upload IP Allowlist (센터&업로드 IP 화이트리스트)**.
3. Adicione os endereços IP do seu cluster da Braze. Para a lista completa de IPs por cluster, consulte [Lista de permissões de IP]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook/#ip-allowlisting).

![Dashboard Comm.One mostrando onde você pode adicionar endereços IP.]({% image_buster /assets/img/kakaotalk/register_braze_ip.png %})

### Tipos de contas KakaoTalk {#types-of-kakaotalk-accounts}

| Tipo de conta | Descrição |
| --- | --- |
| Canal básico | Um canal KakaoTalk padrão que qualquer organização pode configurar. Ele permite envio de mensagens em massa e chat 1:1 pelo KakaoTalk. |
| [Canal Business](https://www.kakaocorp.com/page/service/service/KakaoTalkChannel) | Um canal KakaoTalk aprimorado e verificado para empresas que requer um processo de solicitação e verificação. Ele oferece recursos avançados, como {::nomarkdown}<ul><li>Selo de verificação</li><li>Aparição como canal recomendado</li><li>Suporte para mensagens empresariais</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Tipos de contas KakaoTalk" }

#### Solicitar um canal Business {#apply-for-a-business-channel}

Antes de iniciar a solicitação, reúna a seguinte documentação empresarial:
- Certificado de Registro Empresarial Coreano
- Documento de identidade do representante da empresa
- Certificado de emprego
- Licenças específicas do setor

{% alert important %}
As informações no seu canal KakaoTalk (como nome do canal, imagem de perfil e outros) devem corresponder exatamente às informações nos seus documentos oficiais enviados.
{% endalert %}

Após reunir sua documentação, siga estas etapas:

1. Faça login no [Centro de Administração de Canais KakaoTalk](https://center-pf.kakao.com/).
2. Selecione o canal KakaoTalk existente que deseja fazer upgrade.
3. Na seção **Management (관리)**, selecione a opção **Business Channel Application (비즈니스 채널 신청)**.
4. Selecione o botão **Apply** ou **Request (신청)** para iniciar o processo.
5. Forneça as informações necessárias.
6. Aguarde uma notificação com os resultados da análise.

## Integrar o KakaoTalk {#integrate-kakaotalk}

### Etapa 1: Conectar o canal KakaoTalk à Braze {#step-1-connect-the-kakaotalk-channel-to-braze}

1. Acesse **Integrações de parceiros** > **Parceiros de tecnologia** e selecione seu provedor KakaoTalk.
2. Reúna as credenciais necessárias para seu provedor (veja abaixo), insira-as na página **Parceiros de tecnologia** e salve.
3. Use as credenciais recém-salvas para envio.

#### CJ OliveNetworks

Acesse seu [dashboard Comm.One](https://ums.cjmplace.com/) e reúna as seguintes informações.

| Campo | Localização |
| --- | --- |
| **Comm.One Login ID (로그인 아이디)** | Selecione seu perfil. |
| **Sender Key (발신프로필 키)** | Acesse **Template Management (템플릿 관리)** > **Sender Profile Management (발신프로필 관리)**. |
| **Channel name (카카오톡 채널 프로필명)** | No seu dashboard Comm.One, acesse **Template Management (템플릿 관리)** > **Sender Profile Management (발신프로필 관리)**. |
| **Sender number (연락처)** | {::nomarkdown}<ol><li>Acesse <b>Account Management (계정 관리)</b>, selecione o ícone de menu e depois selecione <b>View Details (자세히보기)</b>.</li><li>Acesse <b>Business Detailed Information (업체 상세 정보)</b> > <b>Company Information (기업정보)</b></li></ul>{:/} |
| **Credential (ID) e Password (비밀번호)** | Acesse o mesmo local do **Sender number (사업자 등록번호)** e depois acesse **API** > **Brand Message (브랜드 메시지)**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="CJ OliveNetworks" }

{% tabs local %}
{% tab Comm.One Login ID (로그인 아이디) %}

![Dashboard Comm.One mostrando um ID de login censurado.]({% image_buster /assets/img/kakaotalk/comm.one_login_id.png %})

{% endtab %}
{% tab Sender Key (발신프로필 키) %}

![Dashboard Comm.One mostrando um Sender Key censurado.]({% image_buster /assets/img/kakaotalk/sender_key.png %})

{% alert important %}
Você pode integrar um Sender Key do KakaoTalk em apenas um espaço de trabalho por vez. Para usar o mesmo Sender Key em um espaço de trabalho diferente, primeiro você deve arquivar o grupo de inscrições do KakaoTalk no espaço de trabalho original e depois entrar em contato com o [suporte da Braze]({{site.baseurl}}/braze_support/) para remover a integração. Após a Braze remover a integração, você pode configurar a integração no novo espaço de trabalho.
{% endalert %}

![Credenciais para um canal KakaoTalk da Braze.]({% image_buster /assets/img/kakaotalk/cj_credentials.png %})

{% endtab %}
{% tab Channel name (카카오톡 채널 프로필명) %}

![Dashboard Comm.One mostrando um nome de canal censurado.]({% image_buster /assets/img/kakaotalk/channel_profile_name.png %})

{% endtab %}
{% tab Credential (ID) e Password (비밀번호) %}

![Dashboard Comm.One mostrando um ID de credencial e senha censurados.]({% image_buster /assets/img/kakaotalk/id_and_password.png %})

{% endtab %}
{% endtabs %}

{% alert note %}
Somente os canais mapeados para um único ID comum podem ser registrados.
{% endalert %}

![Campos na página Parceiros de tecnologia para CJ OliveNetworks.]({% image_buster /assets/img/kakaotalk/cj_olivenetworks.png %}){: style="max-width:30%;"}

#### Infobip

Acesse seu dashboard Infobip e reúna as seguintes informações.

| Campo | Localização |
| --- | --- |
| **API Base URL** | Selecione **Developer Tools** > **API Keys**. |
| **API Key** | Selecione **Developer Tools** > **API Keys**. |
| **Sender name / Sender key** | Selecione **Channels and Numbers** > **Channels** e depois selecione a guia **Senders**. |
| **Sender profile UUID** | Fornecido diretamente pela Infobip. Entre em contato com a Infobip se você não tiver essa informação. |
| **Channel name** | Fornecido diretamente pela Infobip. Entre em contato com a Infobip se você não tiver essa informação. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Infobip" }

## Configurar perfis de usuário {#set-user-profiles}

Os perfis de usuário devem ter números de telefone no formato E.164 para receber mensagens pelo KakaoTalk. Os números de telefone são exibidos no perfil de usuário. O KakaoTalk exige que os números de telefone estejam no formato E.164 (por exemplo, `+821025749774`). Isso difere de alguns outros canais de envio de mensagens que podem aceitar números de telefone em múltiplos formatos.

![Perfil de usuário para um usuário teste com um número de telefone no formato E.164.]({% image_buster /assets/img/kakaotalk/standard_phone_number.png %}){: style="max-width:50%;"}

### Importar números de telefone {#import-phone-numbers}

Importe números de telefone [fazendo upload de um CSV ou usando a API]({{site.baseurl}}/user_guide/data/unification/user_data/import_users/) para criar um usuário. Certifique-se de que os números de telefone estejam no formato E.164 antes de importar.