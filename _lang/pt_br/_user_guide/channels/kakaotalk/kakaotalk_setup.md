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

> Este artigo aborda como configurar o [canal de envio de mensagens KakaoTalk]({{site.baseurl}}/kakaotalk) na Braze, incluindo como configurar usuários, reconciliar IDs de usuário e criar usuários teste do KakaoTalk.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| --- | --- |
| Conta com um parceiro KakaoTalk compatível | É necessário ter uma conta com um parceiro KakaoTalk compatível, [CJ OliveNetworks](https://www.braze.com/partners/solutions-partners/cjolivenetworks/) ou [Infobip](https://marketplace.braze.com/partners/infobip), para usar o canal de envio de mensagens KakaoTalk. |
| Canal Business do KakaoTalk | Sua conta do KakaoTalk precisa ser um canal Business do KakaoTalk para enviar mensagens do KakaoTalk pela Braze. Quando você cria uma conta, o status padrão dela é básico. Para transformar sua conta em um canal Business, você precisará verificar sua empresa e fornecer a documentação relevante. |
| Sender Key do KakaoTalk | Uma Sender Key válida do KakaoTalk. |
| Número de telefone de contato | Um número de telefone de contato do administrador do seu canal KakaoTalk. |
| IPs do cluster da Braze na lista de permissões | O registro na lista de permissões de IP é obrigatório para todos os clientes. Registre os endereços IP da Braze para o seu cluster antes de integrar o KakaoTalk na Braze. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

### Registrar endereços IP da Braze {#register-braze-ip-addresses}

Registre os endereços IP da Braze para o seu cluster no dashboard do Comm.One.

1. No dashboard do Comm.One, acesse **Account Management (계정 관리)**, selecione o ícone de menu e depois selecione **View Details (자세히보기)**.
2. Selecione **Center & Upload IP Allowlist (센터&업로드 IP 화이트리스트)**.
3. Adicione os endereços IP do seu cluster da Braze. Para a lista completa de IPs por cluster, consulte [Lista de permissões de IP]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook#ip-allowlisting).

![Dashboard do Comm.One mostrando onde você pode adicionar endereços IP.]({% image_buster /assets/img/kakaotalk/register_braze_ip.png %})

### Tipos de contas do KakaoTalk {#types-of-kakaotalk-accounts}

| Tipo de conta | Descrição |
| --- | --- |
| Canal básico | Um canal KakaoTalk padrão que qualquer organização pode configurar. Ele permite envio de mensagens em massa e chat 1:1 pelo KakaoTalk. |
| [Canal Business](https://www.kakaocorp.com/page/service/service/KakaoTalkChannel) | Um canal KakaoTalk aprimorado e verificado para empresas que exige um processo de solicitação e verificação. Oferece recursos avançados, como {::nomarkdown}<ul><li>Selo de verificado</li><li>Exibição como canal recomendado</li><li>Suporte para envio de mensagens comerciais</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Tipos de contas do KakaoTalk" }

#### Solicitar um canal Business {#apply-for-a-business-channel}

Antes de iniciar a solicitação, reúna a seguinte documentação empresarial:
- Certificado de Registro Empresarial coreano
- Documento de identidade do representante da empresa
- Certificado de vínculo empregatício
- Licenças específicas do setor

{% alert important %}
As informações do seu canal KakaoTalk (como nome do canal, imagem do perfil e outras) devem corresponder exatamente às informações dos seus documentos oficiais enviados.
{% endalert %}

Após reunir sua documentação, siga estas etapas:

1. Faça login no [KakaoTalk Channel Admin Center](https://center-pf.kakao.com/).
2. Selecione o canal KakaoTalk existente que você deseja fazer upgrade.
3. Na seção **Management (관리)**, selecione a opção **Business Channel Application (비즈니스 채널 신청)**.
4. Selecione o botão **Apply** ou **Request (신청)** para iniciar o processo.
5. Forneça as informações necessárias.
6. Aguarde uma notificação com os resultados da análise.

## Integrar o KakaoTalk {#integrate-kakaotalk}

### Conectar o canal KakaoTalk à Braze {#connect-the-kakaotalk-channel-to-braze}

1. Acesse **Partner Integrations** > **Technology Partners** e selecione seu provedor de KakaoTalk.
2. Reúna as credenciais necessárias do seu provedor (consulte a seção a seguir) e insira-as na página de **Technology Partners** e salve.
3. Use as credenciais recém-salvas para envio.

#### CJ OliveNetworks

Acesse seu [dashboard do Comm.One](https://ums.cjmplace.com/) e reúna as informações a seguir.

| Campo | Localização |
| --- | --- |
| **Comm.One Login ID (로그인 아이디)** | Selecione seu perfil. |
| **Sender Key (발신프로필 키)** | Acesse **Template Management (템플릿 관리)** > **Sender Profile Management (발신프로필 관리)**. |
| **Channel name (카카오톡 채널 프로필명)** | No dashboard do Comm.One, acesse **Template Management (템플릿 관리)** > **Sender Profile Management (발신프로필 관리)**. |
| **Sender number (연락처)** | {::nomarkdown}<ol><li>Acesse <b>Account Management (계정 관리)</b>, selecione o ícone de menu e depois selecione <b>View Details (자세히보기)</b>.</li><li>Acesse <b>Business Detailed Information (업체 상세 정보)</b> > <b>Company Information (기업정보)</b></li></ul>{:/} |
| **Credential (ID) & Password (비밀번호)** | Acesse o mesmo local do **Sender number (사업자 등록번호)** e, em seguida, acesse **API** > **Brand Message (브랜드 메시지)**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="CJ OliveNetworks" }

{% tabs local %}
{% tab Comm.One Login ID (로그인 아이디) %}

![Dashboard do Comm.One exibindo um ID de login censurado.]({% image_buster /assets/img/kakaotalk/comm.one_login_id.png %})

{% endtab %}
{% tab Sender Key (발신프로필 키) %}

![Dashboard do Comm.One exibindo uma Sender Key censurada.]({% image_buster /assets/img/kakaotalk/sender_key.png %})

{% alert important %}
Você pode integrar uma Sender Key do KakaoTalk a apenas um espaço de trabalho por vez. Para usar a mesma Sender Key em um espaço de trabalho diferente, primeiro você precisa arquivar o grupo de inscrições do KakaoTalk no espaço de trabalho original e, em seguida, entrar em contato com o [suporte da Braze]({{site.baseurl}}/braze_support) para remover a integração. Depois que a Braze remover a integração, você pode configurá-la no novo espaço de trabalho.
{% endalert %}

![Credenciais para um canal KakaoTalk da Braze.]({% image_buster /assets/img/kakaotalk/cj_credentials.png %})

{% endtab %}
{% tab Channel name (카카오톡 채널 프로필명) %}

![Dashboard do Comm.One exibindo um nome de canal censurado.]({% image_buster /assets/img/kakaotalk/channel_profile_name.png %})

{% endtab %}
{% tab Credential (ID) & Password (비밀번호) %}

![Dashboard do Comm.One exibindo um ID de credencial e senha censurados.]({% image_buster /assets/img/kakaotalk/id_and_password.png %})

{% endtab %}
{% endtabs %}

{% alert note %}
Somente os canais mapeados para um único ID comum podem ser registrados.
{% endalert %}

![Campos na página de Technology Partners para CJ OliveNetworks.]({% image_buster /assets/img/kakaotalk/cj_olivenetworks.png %}){: style="max-width:30%;"}

#### Infobip

Acesse seu dashboard da Infobip e o [KakaoTalk Channel Admin Center](https://center-pf.kakao.com/) para reunir as informações a seguir.

| Campo | Localização |
| --- | --- |
| **API Base URL** | No portal da Infobip, acesse **Developer Tools** > **API Keys**. |
| **API Key** | No portal da Infobip, acesse **Developer Tools** > **API Keys**. |
| **Sender name / Sender key** | No portal da Infobip, acesse **Channels and Numbers** > **Channels** e selecione a guia **Senders**. |
| **Sender profile UUID** | No KakaoTalk Channel Admin Center, acesse **Channels** e encontre o **Search ID** na janela de informações do canal. |
| **Channel name** | No KakaoTalk Channel Admin Center, encontre o **channel name** na mesma janela de informações do canal. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Infobip" }

##### Chave de API e URL base {#api-key-and-base-url}

1. No portal da Infobip, selecione **Developer Tools** > **API Keys**.
2. Na página **API keys**, copie a **API base URL**.

![Página de API Keys da Infobip exibindo a API base URL.]({% image_buster /assets/img/kakaotalk/infobip_api_keys_page.png %})

{: start="3"}
3. Selecione **CREATE API KEY**.
4. Insira o **Name**, selecione a **Expiration date** e, em seguida, selecione os escopos de API necessários para o KakaoTalk. Esses escopos controlam quais ações da API da Infobip sua chave pode executar.

![Página de criação de API Key da Infobip exibindo os campos de nome, data de expiração e escopos de API.]({% image_buster /assets/img/kakaotalk/infobip_api_key_scopes.png %})

{: start="5"}
5. Selecione **CREATE** para gerar a chave.
6. Copie a chave gerada. Você pode retornar a esta página para atualizar o nome, a data de expiração ou os escopos de API.

##### UUID do perfil do remetente e nome do canal {#sender-profile-uuid-and-channel-name}

1. No [KakaoTalk Channel Admin Center](https://center-pf.kakao.com/), selecione **Channels**.
2. Na janela **Channel Information**, encontre o **Channel name** e o **Search id** (UUID do remetente).
3. Insira as **Customer center contact information**. Essa informação é obrigatória ao enviar mensagens de anúncio.

![Janela de informações do canal KakaoTalk exibindo os campos de informações de contato do centro de atendimento ao cliente.]({% image_buster /assets/img/kakaotalk/kakao_customer_center_contact.png %})

{: start="4"}
4. Para visualizar um canal diferente, selecione o ícone do canal no topo do menu.
5. Na lista **My channel**, selecione o canal que deseja visualizar e repita as etapas anteriores.

## Configurar perfis de usuário {#set-user-profiles}

Os perfis de usuário devem ter números de telefone no formato E.164 para receber mensagens pelo KakaoTalk. Os números de telefone são exibidos no perfil de usuário. O KakaoTalk exige que os números de telefone estejam no formato E.164 (por exemplo, `+821025749774`). Isso é diferente de alguns outros canais de envio de mensagens que podem aceitar números de telefone em vários formatos.

### Importar números de telefone {#import-phone-numbers}

Importe números de telefone [fazendo upload de um CSV ou usando a API]({{site.baseurl}}/user_guide/audience/manage_audience/import_users) para criar um usuário. Certifique-se de que os números de telefone estejam no formato E.164 antes da importação.