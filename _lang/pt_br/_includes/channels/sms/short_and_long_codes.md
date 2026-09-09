# Remetentes de SMS e RCS {#sms-and-rcs-senders}

> Este artigo fornece uma visão geral dos códigos e remetentes disponíveis para o envio de mensagens SMS e RCS.

## Tipos de remetentes de SMS e RCS {#types-of-sms-and-rcs-senders}

{% tabs %}
{% tab Remetente verificado RCS %}

### Remetente verificado RCS {#rcs-verified-sender}

O RCS é um sistema de envio de mensagens moderno que oferece mais recursos do que o SMS tradicional, introduzindo funcionalidades como IDs de remetente com marca, mídia avançada e conteúdo interativo, como carrosséis roláveis, respostas rápidas, botões de CTA e muito mais. Ele foi projetado para oferecer uma experiência de usuário mais elegante e envolvente.

{% alert important %}
Mensagens RCS não podem ser enviadas por serviços de envio de mensagens da Twilio. Grupos de inscrições que usam a Twilio para SMS devem usar um remetente RCS compatível com Infobip (ou outro provedor RCS compatível) para tráfego RCS. Caso contrário, os envios RCS sofrem interrupção no momento do envio.
{% endalert %}

#### Detalhes {#details}

| Componentes visuais | Acesso | Capacidade | MMS ativado | Unidirecional vs. bidirecional |
| --- | --- | --- | --- | --- |
| - Nome da marca<br>- logotipo<br>- legenda opcional<br> - selo de verificação | 4 a 6 semanas para aprovação da operadora | A capacidade e a entrega dependem de o destinatário ter uma conexão de dados ativa (dados móveis ou Wi-Fi). O RCS não depende de limites fixos impostos pela rede como o SMS; as mensagens RCS são enviadas por redes de dados em vez dos canais de sinalização celular tradicionais usados pelo SMS. | N/A | Bidirecional |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Detalhes" }

#### Vantagens e desvantagens {#pros-and-cons}

| Vantagens |
| ---- |
| **Confiança verificada e branding**<br> Ao contrário do SMS tradicional, em que sua marca aparece como um short code aleatório de 5 dígitos ou long code, o RCS permite perfis de remetente verificados. Esses perfis incluem o logotipo, o nome da sua marca e uma marca de verificação "verificado". |
| **Recursos avançados de envio de mensagens**<br> O RCS oferece suporte a carrosséis, vídeos de alta resolução e botões de ação sugerida (como "Reserve agora", "Rastreie o pacote" ou "Pagar conta"). Os usuários podem concluir tarefas complexas sem sair do app de mensagens, o que pode levar a taxas de conversão mais altas do que um simples link de texto. |
{: .reset-td-br-1 aria-label="Vantagens e desvantagens" }

| Desvantagens |
| ---- |
| **Suporte fragmentado**<br> Embora o Google tenha promovido fortemente o RCS para Android e a Apple tenha introduzido recentemente o suporte a RCS para iOS, a implementação ainda pode ser desigual entre diferentes operadoras e regiões. Se o telefone ou a operadora do usuário não oferecer suporte a RCS, a mensagem geralmente é enviada como SMS simples, perdendo assim todos os recursos "avançados" do RCS. |
| **Inconsistências de plataforma**<br> A experiência do usuário com RCS varia dependendo da operadora do destinatário, do modelo do dispositivo e do app de mensagens que ele usa (por exemplo, Google Messages ou iMessage). |
{: .reset-td-br-1 aria-label="Vantagens e desvantagens" }

{% endtab %}
{% tab Short codes de SMS %}

#### Short codes de SMS {#sms-short-codes}

Um short code é um número de 5 a 6 dígitos que pode enviar e receber SMS de e para celulares a taxas mais rápidas do que long codes. Short codes são recomendados para envios de alto volume e sensíveis ao tempo.

Alguns países permitem que você escolha um número específico por uma taxa adicional. Esses short codes são chamados de vanity short codes. Se você tiver interesse em vanity short codes, entre em contato com seu representante de conta da Braze para mais detalhes.

##### Detalhes

| Comprimento | Acesso | Capacidade | MMS ativado | Unidirecional vs. bidirecional |
| --- | --- | --- | --- | --- |
| 5 a 6 dígitos | Solicitação de 4 a 12 semanas | 100 MPS ou mais | Sim | Bidirecional |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Detalhes" }

##### Vantagens e desvantagens

| Vantagens |
| ---- |
| **Velocidade e escalabilidade**<br> Short codes são projetados especificamente para tráfego de alto volume. Eles podem enviar mensagens a taxas mais rápidas do que long codes e, por serem pré-aprovados diretamente pelas operadoras, apresentam o menor risco de serem sinalizados por filtros automáticos de SPAM. |
| **Fáceis de memorizar para "chamadas para ação"**<br> Para Campaigns de marketing (por exemplo, "Envie GANHE para 55555"), um short code é muito mais fácil para os usuários memorizarem e digitarem do que um número de 10 dígitos. Isso torna os short codes o padrão ouro para anúncios de rádio, TV e outdoors, em que o usuário tem apenas alguns segundos para ver ou ouvir o número. |
{: .reset-td-br-1 aria-label="Vantagens e desvantagens" }

| Desvantagens |
| ---- |
| **Short codes estão disponíveis em menos países**<br> Short codes não estão disponíveis em todos os países. Entre em contato com a equipe de conta da Braze para consultar sobre os países para os quais você planeja enviar mensagens. |
| **Processo de solicitação mais longo**<br> Ao contrário de long codes e IDs de remetente alfanuméricos, que podem ser provisionados em 1 a 2 semanas em alguns casos, um short code pode levar de 4 a 12 semanas ou mais para ser provisionado. Cada grande operadora deve aprovar manualmente sua solicitação específica antes que o código esteja ativo em sua rede. Se você tem um lançamento de marketing na próxima semana, um short code não é uma opção. |
| **Custo mais alto**<br> Short codes tendem a ser o tipo de remetente mais caro devido às taxas de configuração e aluguel anual. |
{: .reset-td-br-1 aria-label="Vantagens e desvantagens" }

{% endtab %}
{% tab Long codes de SMS %}

#### Long codes de SMS {#sms-long-codes}

Um long code é um número de telefone padrão usado para enviar e receber mensagens SMS. Esses números de telefone são normalmente chamados de "long codes" (números de 10 dígitos em muitos países) quando comparados com short codes de SMS (números de 5 a 6 dígitos).

##### Detalhes

| Comprimento | Acesso | Capacidade | MMS ativado | Unidirecional vs. bidirecional |
| --- | --- | --- | --- | --- |
| 10 dígitos | Solicitação de 4 a 6 semanas (pode ser menor ou maior para diferentes países) | Nos Estados Unidos, a capacidade de long code depende da sua pontuação de confiança 10DLC; em mercados internacionais, a capacidade pode variar ou aumentar em algumas circunstâncias, mas normalmente começa em torno de 10 segmentos de mensagem por segundo (MPS). | Sim | Bidirecional (dependendo de para onde você está enviando) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Detalhes" }

##### Vantagens e desvantagens

| Vantagens |
| ---- |
| **Familiaridade e confiança**<br> Long codes se parecem com números de telefone pessoais, geralmente incluindo um código de área local. Para marcas, isso representa um equilíbrio entre presença profissional e uma sensação pessoal e acessível. |
| **Maior disponibilidade mundial**<br>Long codes estão disponíveis em mais de 100 países ao redor do mundo. Entre em contato com seu CSM ou com o [suporte da Braze]({{site.baseurl}}/braze_support) para obter uma lista dos países disponíveis.|
{: .reset-td-br-1 aria-label="Vantagens e desvantagens" }

| Desvantagens |
| --- |
| **Velocidades de envio mais lentas e limites diários de envio de mensagens**<br> Long codes não são projetados para marketing em massa como os short codes. Se você tentar enviar uma promoção relâmpago urgente para 100.000 pessoas de uma vez a partir de um long code, pode levar horas para que todas as mensagens sejam entregues. Nos EUA, operadoras como a T-Mobile também podem impor limites diários de envio para 10DLC com base na pontuação de confiança da sua marca. |
| **Maior risco de filtragem**<br> Como long codes se parecem com números de telefone pessoais, as operadoras os monitoram de perto para evitar que números "pessoa-a-pessoa" sejam usados para SPAM. Mesmo com uma Campaign 10DLC registrada, se o conteúdo da sua mensagem for muito "spam" ou não seguir uma formatação rigorosa, você terá um risco muito maior de ser bloqueado pelas operadoras em comparação com um short code pré-aprovado. |
{: .reset-td-br-1 aria-label="Vantagens e desvantagens" }

{% endtab %}
{% tab ID de remetente alfanumérico de SMS %}

#### ID de remetente alfanumérico de SMS {#sms-alphanumeric-sender-id}

Um ID de remetente alfanumérico (frequentemente chamado de "alpha") é uma string reconhecível composta por qualquer combinação de letras e números (geralmente o nome da sua empresa ou marca) exibida como o ID do remetente para envio de mensagens de texto unidirecional.

Eles podem ter até 11 caracteres e conter letras maiúsculas (A-Z) e minúsculas (a-z), espaços e dígitos (0-9). Eles **não podem** conter apenas números.

##### Detalhes

| Comprimento | Acesso | Capacidade | MMS ativado | Unidirecional vs. bidirecional |
| --- | --- | --- | --- | --- |
| Até 11 caracteres | Disponível imediatamente se o pré-registro não for necessário. Caso contrário, 1 a 4 semanas na maioria dos países onde o registro é obrigatório. | Varia dependendo do país | Não | Unidirecional |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Detalhes" }

##### Vantagens e desvantagens

| Vantagens | Desvantagens |
| ---- | ---- |
| {::nomarkdown} <ul><li> Melhor reconhecimento de marca </li><li> Em muitos mercados internacionais, operadoras locais pré-registram e verificam remetentes alfanuméricos, de modo que suas mensagens têm menos chances de serem capturadas por filtros agressivos de SPAM que poderiam bloquear long codes aleatórios </li><li> Disponível em 1 semana se o pré-registro não for necessário </li></ul> {:/} | {::nomarkdown} <ul><li> <a href='/docs/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/keyword_handling#two-way-messaging-custom-keyword-responses'>Envio de mensagens bidirecional</a> não é compatível </li><li> Nem todos os países oferecem suporte a esse recurso. Por exemplo, ele é compatível no Reino Unido, mas é bloqueado nos EUA. </li><li> Alguns países têm um processo extenso de pré-registro que exige a apresentação de documentação legal e prazos mais longos. </li></ul> {:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Vantagens e desvantagens" }

Para saber mais sobre IDs de remetente alfanuméricos, entre em contato com seu CSM.
{% endtab %}
{% tab Números gratuitos de SMS %}

#### Números gratuitos habilitados para SMS {#sms-enabled-toll-free-numbers}

Números gratuitos possuem códigos de área de três dígitos distintos (por exemplo, 800, 888, 877 e 866), permitindo que os usuários entrem em contato com empresas sem serem cobrados. Amplamente usados para atendimento ao cliente, eles também podem lidar com todos os tipos de envio de mensagens A2P (application-to-person), incluindo marketing.

##### Detalhes

| Comprimento | Acesso | Capacidade | MMS ativado | Unidirecional vs. bidirecional |
| --- | --- | --- | --- | --- |
| 10 dígitos | Solicitação de 2 a 4 semanas | Começa em 3 MPS (segmentos por segundo), pode ser aumentado por taxas adicionais | Sim | Bidirecional |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Detalhes" }

##### Vantagens e desvantagens

| Vantagens |
| ---- |
| **Imagem profissional**<br> Números gratuitos são amplamente reconhecidos e confiáveis na América do Norte para comunicação empresarial, proporcionando um toque profissional e de autoridade. |
| **Capacidade flexível; sem limites de envio da operadora**<br> Ao contrário de long codes padrão, que podem definir limites de capacidade ou de envio da operadora dependendo do país, números gratuitos podem ter sua capacidade aumentada para oferecer suporte a volumes maiores e não possuem limites diários de envio da operadora nos EUA.|
{: .reset-td-br-1 aria-label="Vantagens e desvantagens" }

| Desvantagens |
| --- |
| **Impessoal e neutralidade geográfica**<br> Como números gratuitos não possuem um código de área local, eles podem parecer muito "corporativos" ou anônimos. Para uma empresa de serviço local, um número gratuito pode ter desempenho inferior a um long code padrão porque não tem a conexão com a comunidade e às vezes pode ser confundido com uma linha aleatória de telemarketing. |
| **Camada extra de filtragem STOP**<br> Números gratuitos possuem uma camada de gestão de cancelamento fora da Braze que não pode ser removida ou personalizada. Quando um usuário envia "STOP" para seu número gratuito, ele terá sua inscrição cancelada para futuras mensagens desse número e receberá uma resposta automática gerada pela rede. Ele não receberá mais mensagens do seu número gratuito até que envie "START" para ser removido da lista de bloqueio do número gratuito. |
{: .reset-td-br-1 aria-label="Vantagens e desvantagens" }

{% endtab %}
{% endtabs %}

## Uso de short codes e long codes juntos {#using-short-codes-and-long-codes-together}

Se o seu grupo de inscrições inclui tanto short codes quanto long codes, os short codes são normalmente priorizados para mensagens de saída. No entanto, alguns provedores oferecem a funcionalidade de sticky sender, que pode fazer com que um long code continue sendo usado para determinados usuários mesmo após um short code ser adicionado ao pool de remetentes.

O sticky sender mantém a continuidade das mensagens roteando todas as mensagens para um usuário específico a partir do mesmo número de telefone. Se um usuário recebeu uma mensagem de um long code antes de um short code ser adicionado ao seu grupo de inscrições, seu provedor pode continuar usando esse long code para mensagens futuras a esse usuário, mesmo que o short code normalmente fosse priorizado.

Esse comportamento é controlado pelos provedores e não pode ser alterado na Braze.

## Configuração {#setup}

Os requisitos e prazos de configuração variam de acordo com o tipo de remetente e o país em que o remetente está sendo provisionado.

{% tabs local %}
{% tab Remetente verificado por RCS %}

### Remetente verificado por RCS

Os remetentes verificados por RCS são provisionados país a país. O processo de verificação e configuração se concentra no seu agente ou remetente — a persona digital que interage com os usuários. Você fornecerá ativos de marca e detalhes de verificação.

#### Ativos de marca {#brand-assets}

- **Nome verificado:** O nome que os usuários veem no topo da conversa. Deve ser um nome comercial reconhecível, não necessariamente a razão social da sua empresa.
- **Logo:** Uma imagem de alta resolução com 224x224px. Ela é exibida em um formato circular, então mantenha os elementos críticos centralizados.
- **Banner (imagem de destaque):** Uma imagem de fundo para o cartão de perfil da sua empresa (semelhante a uma foto de capa do Facebook ou LinkedIn).
- **Cor da marca:** Um valor hexadecimal para os botões e elementos de interface, de modo a combinar com a identidade visual da sua empresa.

#### Detalhes de verificação {#verification-details}

- **Ponto de contato (POC):** Isso é essencial. Você deve fornecer um endereço de e-mail de um colaborador direto da marca (não um e-mail de agência). O Google ou a operadora enviará um e-mail para essa pessoa para confirmar que ela autorizou a Braze a agir em seu nome.
- **Website e política de privacidade:** Um website ativo e uma política de privacidade que explique como você lida com os dados de usuários e o envio de mensagens.
- **Descrição do caso de uso:** Uma explicação clara do que você está enviando (por exemplo, "Atualizações de entrega de pedidos e suporte ao cliente para compras no varejo").

Os prazos do RCS variam de acordo com o país, e à medida que mais operadoras adotam o canal. Atualmente, você pode esperar que um remetente RCS seja aprovado pelas operadoras dentro de 3 a 6 semanas após a solicitação de lançamento.

{% endtab %}
{% tab Short codes de SMS %}

### Short codes de SMS

Os short codes são provisionados país a país. Dependendo do país, o processo de solicitação de short code é notório por ser imprevisível. A Braze está aqui para ajudar você em cada etapa, então, se você deseja um short code, entre em contato com o seu gerente de integração ou outro representante da Braze.

A Braze auxiliará na coleta de todos os materiais e informações necessários para enviar uma solicitação e configurar um novo short code. Os requisitos variam por país, mas muitos exigem pelo menos o seguinte:

| Material da solicitação | Descrição | Requisitos |
|----------------------|----------------|-----------------|
| Chamada para ação (Aceitação) | O principal objetivo das divulgações é confirmar que o usuário consente em receber mensagens de texto e compreende a natureza do programa. | {::nomarkdown}<ul><li>Product Description</li><li>Message frequency disclosure</li><li>Complete terms and conditions OR link to complete terms and conditions</li><li>Privacy policy OR link to privacy policy</li><li>STOP keyword</li><li>"Message and data rates may apply" disclosure.</li></ul>{:/} |
| Termos e condições | Os termos e condições abrangentes podem ser apresentados integralmente abaixo da chamada para ação ou acessíveis por meio de um link próximo à chamada para ação. | {::nomarkdown}<ul><li>Program (brand) name</li><li>Message frequency disclosure</li><li>Product description</li><li>Customer care contact information</li><li>Opt-out information</li><li>"Message and data rates may apply" disclosure.</li></ul>{:/} |
| Fluxo de mensagens | Programas de mensagens recorrentes devem confirmar a aceitação com uma única mensagem de texto que declare explicitamente em qual programa o usuário se inscreveu e forneça instruções claras de cancelamento.<br><br> A Braze processa mensagens de aceitação, cancelamento e ajuda, atualizando automaticamente o estado do grupo de inscrições para o usuário e o número de telefone associado em todas as solicitações de entrada.<br><br> Observe que essas palavras-chave e respostas padrão também podem ser personalizadas. | {::nomarkdown}<ul><li>Opt-In Confirmation:<ul><li>Program (brand) name OR product description</li><li>Opt-out information</li><li>Customer care contact information</li><li>Message frequency disclosure</li><li>"Message and data rates may apply" disclosure.</li></ul></li><li>HELP response:<ul><li>Program (brand) name OR product description</li><li>Customer care contact information (support email or phone number).</li></ul></li><li>Opt-out (STOP) response:<ul><li>Program (brand) name OR product description</li><li>Confirmation that no further messages will be delivered.</li></ul></li></ul>{:/} |
| Mensagens do programa | As mensagens do programa são enviadas no curso normal do programa de short code, após o usuário ter recebido uma confirmação de aceitação. | {::nomarkdown}<ul><li>Opt-out instructions should be provided at regular intervals and at least once per month.</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Short codes de SMS" }

Quando todos os materiais da solicitação estiverem prontos, a Braze envia a solicitação aos nossos provedores em seu nome. A solicitação é então analisada e aprovada pelas operadoras locais, que podem fornecer feedback adicional ou solicitar informações complementares. Depois que todas as operadoras derem a aprovação, você pode configurar imediatamente o short code para uso na Braze.

O prazo de análise e aprovação do short code varia, mas normalmente leva de 4 a 12 semanas, dependendo do país e da natureza do programa.

{% alert important %}
Se você já possui seu próprio short code, entre em contato com o seu CSM durante o processo de integração para discutir a migração ou transferência do seu short code.
{% endalert %}

{% endtab %}
{% tab Long codes de SMS e números gratuitos %}

### Long codes de SMS (10DLC) e números gratuitos {#sms-long-codes-10dlc-and-toll-free-numbers}

Em muitos países, a configuração de long codes (também chamados de "10DLCs" ou "códigos longos de 10 dígitos") e números gratuitos para envio de SMS deixou de ser um processo simples e passou a ser um sistema regulado de verificação. As operadoras querem saber exatamente quem você é e o que pretende dizer antes de você enviar.

Durante o processo de configuração de long code, você pode esperar compartilhar detalhes sobre a identidade da sua marca e a intenção da sua campanha.

#### Identidade da marca {#brand-identity}

- **Razão social:** Deve corresponder exatamente aos seus documentos fiscais (por exemplo, "Acme Corp LLC", não "Acme").
- **Identificação fiscal:** Nos EUA, é o Employer Identification Number (EIN). Internacionalmente, você precisará de um número de Value-Added Tax (VAT) ou um número de registro comercial local (BRN).
- **Presença digital:** Um website ativo e funcional. As operadoras podem verificá-lo para confirmar que você não é uma empresa fictícia.
- **Contato autorizado:** Nome, e-mail e número de telefone de uma pessoa responsável pela conta.

#### Intenção da campanha {#campaign-intent}

- **Caso de uso:** Informe se você está enviando códigos 2FA, lembretes de compromissos, promoções de marketing ou outros.
- **Mensagens de exemplo:** Forneça de 2 a 5 exemplos do que você enviará.
- **Comprovação de aceitação:** Descreva (e frequentemente mostre uma captura de tela de) como um usuário se inscreve. Exemplos incluem um formulário web com uma caixa de seleção ou uma palavra-chave "Envie INICIAR" em um pôster.

A Braze trabalhará com você para coletar todos os detalhes necessários para provisionar seu long code ou número gratuito, e então enviará os detalhes ao nosso provedor para análise e aprovação. Após o nosso provedor aprovar o programa, configuramos imediatamente o long code ou número gratuito na Braze.

O prazo de configuração depende do país de provisionamento. Normalmente, long codes e números gratuitos levam entre 1 e 4 semanas para serem aprovados.

{% alert important %}
Todos os clientes que atualmente possuem e/ou utilizam long codes dos EUA para enviar mensagens a clientes nos EUA são obrigados a registrar seus long codes. Para saber mais sobre os detalhes do registro A2P 10DLC dos EUA e por que ele é necessário, visite nosso [artigo dedicado sobre 10DLC]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup/10dlc).
{% endalert %}

{% endtab %}
{% tab ID de remetente alfanumérico de SMS %}

### ID de remetente alfanumérico de SMS

Os IDs de remetente alfanumérico são altamente regulamentados porque podem ser facilmente falsificados para phishing. Embora alguns países permitam que qualquer pessoa configure e envie a partir de um nome, em muitos países você deve primeiro comprovar que é proprietário da marca.

Você pode ser solicitado a fornecer os seguintes detalhes para configurar um ID de remetente alfanumérico.

- **ID preferido:** Uma string de até 11 caracteres. Deve conter pelo menos uma letra e não pode ser uma palavra genérica como "BANK" ou "INFO".
- **Comprovação de propriedade da marca:** Seu Certificado de Marca Registrada ou um Documento de Registro Comercial (por exemplo, um Certificado de Constituição emitido nos últimos 12 meses).
- **Carta de autorização:** Uma carta assinada em papel timbrado da sua empresa, autorizando a Braze e nosso provedor a enviar mensagens em seu nome usando aquele ID específico.
- **Modelos de mensagens de exemplo:** Em várias regiões, você deve registrar os "modelos" exatos das mensagens que pretende enviar. Desvios nas mensagens reais podem causar falhas de entrega nesses países.

O prazo para configurar um ID de remetente alfanumérico depende muito de o país permitir configuração "Dinâmica" (imediata, sem necessidade de registro) ou exigir "Pré-registro". Em países que exigem pré-registro, o prazo de configuração varia, mas normalmente leva entre 1 e 4 semanas.

{% endtab %}
{% endtabs %}

## Perguntas frequentes {#frequently-asked-questions}

Para respostas sobre perguntas frequentes sobre remetentes de SMS e RCS, consulte nossa página de [perguntas frequentes sobre SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/faqs).