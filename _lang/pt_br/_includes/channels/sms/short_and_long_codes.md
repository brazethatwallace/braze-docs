# Remetentes de SMS e RCS {#sms-and-rcs-senders}

> Este artigo fornece uma visão geral dos códigos e remetentes disponíveis para o envio de mensagens SMS e RCS.

## Tipos de remetentes de SMS e RCS {#types-of-sms-and-rcs-senders}

{% tabs %}
{% tab Remetente verificado RCS %}

### Remetente verificado RCS {#rcs-verified-sender}

O RCS é um sistema de envio de mensagens moderno que oferece mais recursos do que o SMS tradicional, introduzindo funcionalidades como IDs de remetente com marca, mídia rica e conteúdo interativo, como carrosséis roláveis, respostas rápidas, botões de CTA e muito mais. Ele foi projetado para proporcionar uma experiência de usuário mais elegante e envolvente.

{% alert important %}
Mensagens RCS não podem ser enviadas por serviços de envio de mensagens da Twilio. Grupos de inscrições que usam a Twilio para SMS devem usar um remetente RCS compatível com a Infobip (ou outro provedor de RCS compatível) para o tráfego RCS. Caso contrário, os envios de RCS sofrem interrupção no momento do envio.
{% endalert %}

#### Detalhes {#details}

| Componentes visuais | Acesso | Capacidade de envio | MMS ativado | Unidirecional vs. bidirecional |
| --- | --- | --- | --- | --- |
| - Nome da marca<br>- logotipo<br>- legenda opcional<br> - selo de verificação | 4 a 6 semanas para aprovação da operadora | A capacidade de envio e a entrega dependem de o destinatário ter uma conexão de dados ativa (dados móveis ou Wi-Fi). O RCS não depende de limites fixos impostos pela rede como o SMS; as mensagens RCS são enviadas por redes de dados em vez dos canais de sinalização celular tradicionais usados pelo SMS. | N/A | Bidirecional |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Detalhes" }

#### Prós e contras {#pros-and-cons}

| Prós |
| ---- |
| **Confiança verificada e branding**<br> Diferentemente do SMS tradicional, em que sua marca aparece como um short code aleatório de 5 dígitos ou um long code, o RCS permite perfis de remetente verificados. Esses perfis incluem o logotipo, o nome e uma marca de seleção "verificado" da sua marca. |
| **Recursos de mensagens ricas**<br> O RCS oferece suporte a carrosséis, vídeos em alta resolução e botões de ação sugeridos (como "Reservar agora", "Rastrear pacote" ou "Pagar conta"). Os usuários podem concluir tarefas complexas sem sair do app de mensagens, o que pode levar a taxas de conversão mais altas do que um link em texto simples. |
{: .reset-td-br-1 aria-label="Prós e contras" }

| Contras |
| ---- |
| **Suporte fragmentado**<br> Embora o Google tenha impulsionado fortemente o RCS para Android e a Apple tenha introduzido recentemente o suporte a RCS para iOS, a implementação ainda pode ser desigual entre diferentes operadoras e regiões. Se o telefone ou a operadora de um usuário não oferecer suporte a RCS, a mensagem geralmente é enviada como SMS simples, perdendo consequentemente todos os recursos "ricos" do RCS. |
| **Inconsistências entre plataformas**<br> A experiência do usuário com RCS varia dependendo da operadora do destinatário, do modelo do dispositivo e de qual app de mensagens ele usa (por exemplo, Google Messages ou iMessage). |
{: .reset-td-br-1 aria-label="Prós e contras" }

{% endtab %}
{% tab Short codes SMS %}

#### Short codes SMS {#sms-short-codes}

Um short code é um número de 5 a 6 dígitos que pode enviar e receber SMS de e para telefones celulares a taxas mais rápidas do que long codes. Short codes são recomendados para envios de alto volume e sensíveis ao tempo.

Alguns países permitem que você escolha um número específico por uma taxa adicional. Esses short codes são chamados de vanity short codes. Se você tiver interesse em vanity short codes, entre em contato com o representante da sua conta Braze para obter detalhes.

##### Detalhes

| Comprimento | Acesso | Capacidade de envio | MMS ativado | Unidirecional vs. bidirecional |
| --- | --- | --- | --- | --- |
| 5-6 dígitos | Solicitação de 4 a 12 semanas | 100 mensagens por segundo ou mais | Sim | Bidirecional |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Detalhes" }

##### Prós e contras

| Prós |
| ---- |
| **Velocidade e escalabilidade**<br> Short codes são projetados especificamente para tráfego de alto volume. Eles podem enviar mensagens a taxas mais rápidas do que long codes e, como são pré-aprovados diretamente pelas operadoras, têm o menor risco de serem sinalizados por filtros automáticos de SPAM. |
| **Fácil memorização para "chamadas para ação"**<br> Para Campaigns de marketing (por exemplo, "Envie GANHAR para 55555"), um short code é muito mais fácil para os usuários memorizarem e digitarem do que um número de 10 dígitos. Isso torna os short codes o padrão ouro para anúncios em rádio, TV e outdoors, onde o usuário tem apenas alguns segundos para ver ou ouvir o número. |
{: .reset-td-br-1 aria-label="Prós e contras" }

| Contras |
| ---- |
| **Short codes estão disponíveis em menos países**<br> Short codes não estão disponíveis em todos os países. Entre em contato com a equipe da sua conta Braze para consultar sobre os países para os quais você planeja enviar mensagens. |
| **Processo de solicitação mais longo**<br> Diferentemente de long codes e IDs de remetente alfanuméricos, que podem ser provisionados em 1 a 2 semanas em alguns casos, um short code pode levar de 4 a 12 semanas ou mais para ser provisionado. Cada grande operadora deve aprovar manualmente sua solicitação específica antes que o código esteja ativo em sua rede. Se você tem um lançamento de marketing na próxima semana, um short code não é uma opção. |
| **Custo mais alto**<br> Short codes tendem a ser o tipo de remetente mais caro devido às taxas de configuração e aluguel anual. |
{: .reset-td-br-1 aria-label="Prós e contras" }

{% endtab %}
{% tab Long codes SMS %}

#### Long codes SMS {#sms-long-codes}

Um long code é um número de telefone padrão usado para enviar e receber mensagens SMS. Esses números de telefone são normalmente chamados de "long codes" (números de 10 dígitos em muitos países) quando comparados com short codes SMS (números de 5 a 6 dígitos).

##### Detalhes

| Comprimento | Acesso | Capacidade de envio | MMS ativado | Unidirecional vs. bidirecional |
| --- | --- | --- | --- | --- |
| 10 dígitos | Solicitação de 4 a 6 semanas (pode ser mais curta ou mais longa para diferentes países) | Nos Estados Unidos, a capacidade de envio de long codes depende da sua pontuação de confiança 10DLC; em mercados internacionais, a capacidade pode variar ou aumentar em algumas circunstâncias, mas normalmente começa em torno de 10 segmentos de mensagem por segundo (MPS). | Sim | Bidirecional (dependendo de para onde você está enviando) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Detalhes" }

##### Prós e contras

| Prós |
| ---- |
| **Familiaridade e confiança**<br> Long codes se parecem com números de telefone pessoais, geralmente incluindo um código de área local. Para marcas, isso representa um equilíbrio entre presença profissional e uma sensação pessoal e acessível. |
| **Maior disponibilidade mundial**<br> Long codes estão disponíveis em mais de 100 países importantes em todo o mundo. Entre em contato com o seu gerente de sucesso do cliente ou com o [suporte da Braze]({{site.baseurl}}/braze_support) para obter uma lista de países disponíveis. |
{: .reset-td-br-1 aria-label="Prós e contras" }

| Contras |
| --- |
| **Velocidades de envio mais lentas e limites diários de mensagens**<br> Long codes não foram criados para marketing em massa como os short codes. Se você tentar enviar uma promoção relâmpago urgente para 100.000 pessoas de uma vez a partir de um long code, pode levar horas para que todas as mensagens sejam entregues. Nos EUA, operadoras como a T-Mobile também podem impor limites diários de envio para 10DLC com base na pontuação de confiança da sua marca. |
| **Maior risco de filtragem**<br> Como long codes se parecem com números de telefone pessoais, as operadoras os monitoram de perto para evitar que números "pessoa a pessoa" sejam usados para SPAM. Mesmo com uma Campaign 10DLC registrada, se o conteúdo da sua mensagem for muito "spammy" ou não seguir uma formatação rigorosa, você tem um risco muito maior de ser bloqueado pelas operadoras em comparação com um short code pré-aprovado. |
{: .reset-td-br-1 aria-label="Prós e contras" }

{% endtab %}
{% tab ID de remetente alfanumérico SMS %}

#### ID de remetente alfanumérico SMS {#sms-alphanumeric-sender-id}

Um ID de remetente alfanumérico (frequentemente chamado de "alfa") é uma string reconhecível composta por qualquer combinação de letras e números (geralmente o nome da sua empresa ou marca) exibida como o ID do remetente para envio de mensagens de texto unidirecional.

Eles podem ter até 11 caracteres e conter letras maiúsculas (A-Z) e minúsculas (a-z), espaços e dígitos (0-9). Eles **não podem** conter apenas números.

##### Detalhes

| Comprimento | Acesso | Capacidade de envio | MMS ativado | Unidirecional vs. bidirecional |
| --- | --- | --- | --- | --- |
| Até 11 caracteres | Disponível imediatamente se o pré-registro não for necessário. Caso contrário, de 1 a 4 semanas na maioria dos países onde o registro é obrigatório. | Varia dependendo do país | Não | Unidirecional |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Detalhes" }

##### Prós e contras

| Prós | Contras |
| ---- | ---- |
| {::nomarkdown} <ul><li> Melhor reconhecimento da marca </li><li> Em muitos mercados internacionais, as operadoras locais pré-registram e verificam remetentes alfanuméricos, de modo que suas mensagens têm menos probabilidade de serem capturadas por filtros agressivos de SPAM das operadoras que poderiam bloquear long codes aleatórios </li><li> Disponível em até 1 semana se o pré-registro não for necessário </li></ul> {:/} | {::nomarkdown} <ul><li> <a href='/docs/user_guide/message_building_by_channel/sms/keywords/#two-way-messaging-custom-keyword-responses/'>Envio de mensagens bidirecional</a> não é compatível </li><li> Nem todos os países oferecem suporte a esse recurso. Por exemplo, é compatível no Reino Unido, mas é bloqueado nos EUA. </li><li> Alguns países têm um processo extenso de pré-registro que exige a apresentação de documentação legal e prazos mais longos. </li></ul> {:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prós e contras" }

Para saber mais sobre IDs de remetente alfanuméricos, entre em contato com o seu gerente de sucesso do cliente.
{% endtab %}
{% tab Números gratuitos SMS %}

#### Números gratuitos habilitados para SMS {#sms-enabled-toll-free-numbers}

Números gratuitos (toll-free) possuem códigos de área distintos de três dígitos (por exemplo, 800, 888, 877 e 866), permitindo que os usuários entrem em contato com empresas sem serem cobrados. Amplamente usados para atendimento ao cliente, eles também podem lidar com todos os tipos de envio de mensagens A2P (application-to-person), incluindo marketing.

##### Detalhes

| Comprimento | Acesso | Capacidade de envio | MMS ativado | Unidirecional vs. bidirecional |
| --- | --- | --- | --- | --- |
| 10 dígitos | Solicitação de 2 a 4 semanas | Começa em 3 MPS (segmentos por segundo), pode ser aumentado por taxas adicionais | Sim | Bidirecional |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Detalhes" }

##### Prós e contras

| Prós |
| ---- |
| **Imagem profissional**<br> Números gratuitos são amplamente reconhecidos e confiáveis na América do Norte para comunicação empresarial, proporcionando um toque profissional e de autoridade. |
| **Capacidade de envio flexível; sem limites de envio da operadora**<br> Diferentemente de long codes padrão, que podem definir limites de capacidade de envio ou limites de envio da operadora dependendo do país, números gratuitos podem ter a capacidade de envio aumentada para ajudar a suportar volumes maiores e não têm limites diários de envio da operadora nos EUA. |
{: .reset-td-br-1 aria-label="Prós e contras" }

| Contras |
| --- |
| **Impessoal e neutralidade geográfica**<br> Como números gratuitos não possuem um código de área local, eles podem parecer muito "corporativos" ou anônimos. Para um negócio de serviço local, um número gratuito pode ter desempenho inferior a um long code padrão porque carece da conexão com a comunidade e às vezes pode ser confundido com uma linha de telemarketing aleatória. |
| **Camada extra de filtragem de STOP**<br> Números gratuitos possuem uma camada de tratamento de cancelamento fora da Braze que não pode ser removida ou personalizada. Quando um usuário envia "STOP" para o seu número gratuito, ele será descadastrado de mensagens futuras do seu número e receberá uma resposta automática gerada pela rede. Ele não receberá mais mensagens do seu número gratuito até que envie "START" para ser removido da lista de bloqueio do número gratuito. |
{: .reset-td-br-1 aria-label="Prós e contras" }

{% endtab %}
{% endtabs %}

## Usando códigos curtos e códigos longos juntos {#using-short-codes-and-long-codes-together}

Se o seu grupo de inscrições inclui tanto códigos curtos quanto códigos longos, os códigos curtos geralmente são priorizados para mensagens de saída. No entanto, alguns provedores oferecem a funcionalidade de remetente fixo (sticky sender), que pode fazer com que um código longo continue sendo usado para determinados usuários mesmo após um código curto ser adicionado ao pool de remetentes.

O remetente fixo mantém a continuidade das mensagens roteando todas as mensagens para um usuário específico a partir do mesmo número de telefone. Se um usuário recebeu uma mensagem de um código longo antes de um código curto ser adicionado ao seu grupo de inscrições, seu provedor pode continuar usando esse código longo para mensagens futuras a esse usuário, mesmo que o código curto normalmente fosse priorizado.

Esse comportamento é controlado pelos provedores e não pode ser alterado na Braze.

## Configuração {#setup}

Os requisitos e prazos de configuração variam de acordo com o tipo de remetente e o país em que o remetente está sendo provisionado.

{% tabs local %}
{% tab Remetente verificado RCS %}

### Remetente verificado RCS

Os remetentes verificados RCS são provisionados país a país. O processo de verificação e configuração é focado no seu agente ou remetente — a persona digital que interage com os usuários. Você fornecerá ativos de marca e detalhes de verificação.

#### Ativos de marca {#brand-assets}

- **Nome verificado:** O nome que os usuários veem no topo da conversa de mensagens. Deve ser um nome comercial reconhecível, não necessariamente a razão social da empresa.
- **Logo:** Uma imagem de alta resolução com 224x224px. Ela é exibida em um formato circular, então mantenha os elementos críticos centralizados.
- **Banner (imagem de destaque):** Uma imagem de fundo para o cartão de perfil da sua empresa (semelhante a uma foto de capa do Facebook ou LinkedIn).
- **Cor da marca:** Um valor hexadecimal para os botões e elementos de interface, de modo a combinar com a identidade visual da sua empresa.

#### Detalhes de verificação {#verification-details}

- **Ponto de contato (POC):** Isso é fundamental. Você deve fornecer um endereço de e-mail de um colaborador direto da marca (não um e-mail de agência). O Google ou a operadora enviará um e-mail para essa pessoa para confirmar que ela autorizou a Braze a agir em seu nome.
- **Website e política de privacidade:** Um website ativo e uma política de privacidade que explique como você lida com dados de usuários e envio de mensagens.
- **Descrição do caso de uso:** Uma explicação clara do que você está enviando (por exemplo, "Atualizações de entrega de pedidos e suporte ao cliente para compras no varejo").

Os prazos do RCS variam dependendo do país, e à medida que mais operadoras adotam o canal. Atualmente, você pode esperar que um remetente RCS seja aprovado pelas operadoras dentro de 3 a 6 semanas após a solicitação de lançamento.

{% endtab %}
{% tab Short codes SMS %}

### Short codes SMS

Os short codes são provisionados país a país. Dependendo do país, o processo de solicitação de short code é conhecido por ser imprevisível. A Braze está aqui para ajudar você em cada etapa, então, se você deseja um short code, entre em contato com seu gerente de integração ou outro representante da Braze.

A Braze ajudará a reunir todos os materiais e informações necessários para enviar uma solicitação e configurar um novo short code. Os requisitos variam por país, mas muitos exigem pelo menos o seguinte:

| Material da solicitação | Descrição | Requisitos |
|----------------------|----------------|-----------------|
| Chamada para ação (aceitação) | O objetivo principal das divulgações é confirmar que o usuário consente em receber mensagens de texto e compreende a natureza do programa. | {::nomarkdown}<ul><li>Descrição do produto</li><li>Divulgação da frequência de mensagens</li><li>Termos e condições completos OU link para os termos e condições completos</li><li>Política de privacidade OU link para a política de privacidade</li><li>Palavra-chave STOP</li><li>Divulgação "Taxas de mensagens e dados podem ser aplicadas".</li></ul>{:/} |
| Termos e condições | Os termos e condições abrangentes podem ser totalmente apresentados abaixo da chamada para ação ou acessíveis por meio de um link próximo à chamada para ação. | {::nomarkdown}<ul><li>Nome do programa (marca)</li><li>Divulgação da frequência de mensagens</li><li>Descrição do produto</li><li>Informações de contato do atendimento ao cliente</li><li>Informações de cancelamento</li><li>Divulgação "Taxas de mensagens e dados podem ser aplicadas".</li></ul>{:/} |
| Fluxo de mensagens | Programas de mensagens recorrentes devem confirmar a aceitação com uma única mensagem de texto que declare explicitamente em qual programa o usuário se inscreveu e forneça instruções claras de cancelamento.<br><br> A Braze processa mensagens de aceitação, cancelamento e ajuda, atualizando automaticamente o estado do grupo de inscrições para o usuário e seu número de telefone associado em todas as solicitações de entrada.<br><br> Observe que essas palavras-chave e respostas padrão também podem ser personalizadas. | {::nomarkdown}<ul><li>Confirmação de aceitação:<ul><li>Nome do programa (marca) OU descrição do produto</li><li>Informações de cancelamento</li><li>Informações de contato do atendimento ao cliente</li><li>Divulgação da frequência de mensagens</li><li>Divulgação "Taxas de mensagens e dados podem ser aplicadas".</li></ul></li><li>Resposta HELP:<ul><li>Nome do programa (marca) OU descrição do produto</li><li>Informações de contato do atendimento ao cliente (e-mail de suporte ou número de telefone).</li></ul></li><li>Resposta de cancelamento (STOP):<ul><li>Nome do programa (marca) OU descrição do produto</li><li>Confirmação de que nenhuma mensagem adicional será enviada.</li></ul></li></ul>{:/} |
| Mensagens do programa | As mensagens do programa são enviadas no curso normal do programa de short code, após o usuário ter recebido uma confirmação de aceitação. | {::nomarkdown}<ul><li>Instruções de cancelamento devem ser fornecidas em intervalos regulares e pelo menos uma vez por mês.</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Short codes SMS" }

Quando todos os materiais da sua solicitação estiverem prontos, a Braze envia a solicitação aos nossos provedores em seu nome. A solicitação é então revisada e aprovada pelas operadoras locais, que podem fornecer feedback adicional ou solicitar informações complementares. Após todas as operadoras concederem a aprovação, você pode configurar imediatamente o short code para uso na Braze.

O prazo de revisão e aprovação do short code varia, mas normalmente leva de 4 a 12 semanas, dependendo do país e da natureza do programa.

{% alert important %}
Se você já possui seu próprio short code, entre em contato com seu gerente de sucesso do cliente durante o processo de integração para discutir a migração ou transferência do seu short code.
{% endalert %}

{% endtab %}
{% tab Long codes SMS e números gratuitos %}

### Long codes SMS (10DLC) e números gratuitos {#sms-long-codes-10dlc-and-toll-free-numbers}

Em muitos países, a configuração de long codes (também chamados de "10DLCs" ou "códigos longos de 10 dígitos") e números gratuitos para envio de SMS deixou de ser um processo "plug and play" e passou a ser um sistema regulamentado de verificação. As operadoras querem saber exatamente quem você é e o que pretende enviar antes de autorizar o envio.

Durante o processo de configuração do long code, você pode esperar compartilhar detalhes sobre a identidade da sua marca e a intenção da campanha.

#### Identidade da marca {#brand-identity}

- **Razão social:** Deve corresponder exatamente aos seus documentos fiscais (por exemplo, "Acme Corp LLC", não "Acme").
- **Identificação fiscal:** Nos EUA, é o Employer Identification Number (EIN). Internacionalmente, você precisará de um número de Value-Added Tax (VAT) ou um número de registro comercial local (BRN).
- **Presença digital:** Um website ativo e funcional. As operadoras podem verificá-lo para confirmar que você não é uma empresa "de fachada".
- **Contato autorizado:** Nome, e-mail e número de telefone de uma pessoa responsável pela conta.

#### Intenção da campanha {#campaign-intent}

- **Caso de uso:** Informe se você está enviando códigos 2FA, lembretes de compromissos, promoções de marketing ou outros.
- **Mensagens de exemplo:** Forneça de 2 a 5 exemplos do que você enviará.
- **Comprovação de aceitação:** Descreva (e frequentemente mostre uma captura de tela de) como um usuário se inscreve. Exemplos incluem um formulário web com uma caixa de seleção ou uma palavra-chave "Envie START" em um pôster.

A Braze trabalhará com você para coletar todos os detalhes necessários para provisionar seu long code ou número gratuito e, em seguida, enviará os detalhes ao nosso provedor para revisão e aprovação. Após nosso provedor aprovar o programa, configuramos imediatamente o long code ou número gratuito na Braze.

O prazo de configuração depende do país de provisionamento. Normalmente, long codes e números gratuitos levam entre 1 a 4 semanas para serem aprovados.

{% alert important %}
Todos os clientes que atualmente possuem e/ou usam long codes dos EUA para enviar mensagens a clientes nos EUA são obrigados a registrar seus long codes. Para saber mais sobre as especificidades do registro US A2P 10DLC e por que ele é obrigatório, visite nosso [artigo dedicado sobre 10DLC]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup/10dlc).
{% endalert %}

{% endtab %}
{% tab ID de remetente alfanumérico SMS %}

### ID de remetente alfanumérico SMS

Os IDs de remetente alfanuméricos são altamente regulamentados porque podem ser facilmente falsificados para phishing. Embora alguns países permitam que qualquer pessoa configure e envie a partir de um nome, em muitos países você deve primeiro comprovar que é proprietário da marca.

Você pode ser solicitado a fornecer os seguintes detalhes para configurar um ID de remetente alfanumérico.

- **ID preferido:** Uma string de até 11 caracteres. Deve conter pelo menos uma letra e não pode ser uma palavra genérica como "BANK" ou "INFO".
- **Comprovação de propriedade da marca:** Seu certificado de marca registrada ou um documento de registro comercial (por exemplo, um certificado de constituição emitido nos últimos 12 meses).
- **Carta de autorização:** Uma carta assinada em papel timbrado da sua empresa autorizando a Braze e nosso provedor a enviar mensagens em seu nome usando esse ID específico.
- **Modelos de mensagens de exemplo:** Em várias regiões, você deve registrar os "modelos" exatos das mensagens que pretende enviar. Desvios nas mensagens reais podem causar falhas de entrega nesses países.

O prazo para configurar um ID de remetente alfanumérico depende muito de o país permitir configuração "Dinâmica" (imediata, sem necessidade de registro) ou exigir "Pré-registro". Em países que exigem pré-registro, o prazo de configuração varia, mas normalmente leva entre 1 a 4 semanas.

{% endtab %}
{% endtabs %}

## Perguntas frequentes {#frequently-asked-questions}

Para respostas às perguntas frequentes sobre remetentes de SMS e RCS, consulte nossa página de [perguntas frequentes sobre SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/sms/faqs#frequently-asked-questions).