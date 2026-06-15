---
nav_title: FAQ
article_title: FAQ sobre SMS, MMS e RCS
page_order: 30
description: "Este artigo aborda perguntas frequentes sobre envio de mensagens por SMS, MMS e RCS."
page_type: FAQ
alias: /sms_mms_rcs_faq/
channel:
  - SMS
  - MMS
  - RCS
---

# Perguntas frequentes {#frequently-asked-questions}

> Este artigo aborda perguntas frequentes sobre envio de mensagens por SMS, MMS e RCS.

## Geral {#general}

### O que é um `app_id` no objeto de API de SMS? {#what-is-an-app_id-in-the-sms-api-object}

A chave de API do identificador do app, ou `app_id`, é um parâmetro que associa a atividade a um app específico no seu espaço de trabalho. Ele designa com qual app dentro do espaço de trabalho você está interagindo. Por exemplo, você terá um `app_id` para o seu app iOS, um `app_id` para o seu app Android e um `app_id` para a sua integração web.

Você pode encontrar seu `app_id` navegando até **Configurações** > **Configurações do app** e localizando a seção **Identification**.

### O que acontece se vários usuários tiverem o mesmo número de telefone? {#what-happens-if-multiple-users-have-the-same-phone-number}

Quando vários perfis de usuário que compartilham o mesmo número de telefone (habilitado para SMS) são elegíveis para uma Campaign baseada em ação ou componente do Canvas ao mesmo tempo, disparados pelo evento de um SMS recebido, a Braze fará a deduplicação dos usuários no nível do componente do Canvas. Isso impedirá que os usuários recebam mais de um SMS para um componente do Canvas, mesmo que vários usuários compartilhem o mesmo número de telefone.

{% alert note %}
A Braze não faz deduplicação por número de telefone para Canvas agendados.
{% endalert %}

A Braze usará o seguinte fluxo para determinar o perfil destinatário:
- Verificar qual perfil recebeu SMS mais recentemente (até 7 dias atrás); se existir, enviar para esse usuário.
- Se nenhum tiver recebido SMS nos últimos 7 dias, enviar para o usuário que possui um alias de usuário "phone" correspondente ao número de telefone.
- Se nenhum existir, enviar para um perfil aleatório entre os disponíveis.

Se você receber uma palavra-chave "START" ou "STOP" do número de telefone compartilhado, todos os perfis de usuário serão inscritos e habilitados para SMS ou terão a inscrição cancelada. Isso também se aplica a alterações de estado via API. Por exemplo, se vários perfis com IDs externos diferentes tiverem os mesmos números de telefone, uma alteração de estado do grupo de inscrições pela API atualizará todos os perfis com esse número de telefone, mesmo que apenas um ID externo seja especificado.

{% alert important %}
Se você escalonar seus usuários em um Canvas e tiver horários de programação diferentes para cada componente do Canvas, é possível enviar mensagens duplicadas para um usuário com o mesmo e-mail ou telefone.
{% endalert %}

Para evitar atualizações desnecessariamente grandes, a Braze atualizará no máximo 100 perfis de usuário que compartilham um identificador quando uma atualização de inscrição for feita. Se mais de 100 perfis de usuário compartilharem o mesmo número de telefone, nem todos os perfis serão atualizados.

### O que são short codes compartilhados? {#what-are-shared-short-codes}

Com um short code compartilhado, todas as mensagens de texto, independentemente de qual empresa ou organização as envia, chegam ao dispositivo móvel do consumidor a partir do mesmo número de telefone de 5 a 6 dígitos. Embora os short codes compartilhados tenham custo relativamente baixo e estejam disponíveis imediatamente, isso significa que sua empresa não terá um short code dedicado.

Algumas desvantagens dessa abordagem incluem:

- Se seus clientes cancelarem a inscrição das mensagens de outra empresa que compartilha um short code com você, eles também terão cancelado a inscrição das suas mensagens.
- Se uma empresa violar as regras, as mensagens de todas as empresas serão suspensas.
- Problemas de segurança

## Cobrança e preços {#billing-and-pricing}

### Como serei cobrado pelo SMS? {#how-will-i-be-billed-for-sms}

Além das cobranças por short codes e long codes, a Braze fornece uma cota de mensagens SMS para diferentes países. Ou seja, trabalhamos com você para definir um determinado número de segmentos de mensagem para diferentes países, que você usará para enviar Campaigns de SMS. A cobrança é feita pelo número de segmentos de mensagem enviados por país. Para saber mais sobre como os segmentos de mensagem são calculados, consulte nosso guia de [Segmentos de mensagem e limites de texto]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator/). Seu gerente de conta entrará em contato para informá-lo caso esteja próximo de atingir seu limite máximo, fornecendo relatórios relevantes para mantê-lo informado. Para mais perguntas sobre excedentes, entre em contato com seu representante da Braze.

### Os preços de MMS e SMS são diferentes? {#does-mms-and-sms-pricing-differ}

MMS e SMS têm custos diferentes e são cobrados separadamente com base no volume. Entre em contato com a equipe de integração da Braze para obter informações sobre preços.

### Como posso evitar excedentes? {#how-can-i-avoid-overages}

Embora não possamos prometer que você nunca terá um excedente, você pode seguir estas precauções para diminuir as chances de ultrapassar seus limites:

- Preste atenção ao número de caracteres no seu SMS. Enviar involuntariamente mais de um segmento pode causar excedentes. Para mais detalhes, consulte nosso [detalhamento de segmentos]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator/).
- Calcule cuidadosamente os caracteres do seu SMS para considerar Liquid ou Conteúdo conectado. O criador de SMS da Braze no seu dashboard não estima nem considera o uso de nenhum desses recursos.
- Considere o tipo de codificação que sua mensagem usa — se sua mensagem usa codificação GSM-7, você geralmente pode estimar que consegue enviar uma mensagem com 128 caracteres por segmento de mensagem. Se sua mensagem usa codificação [UCS-2](https://en.wikipedia.org/wiki/Universal_Coded_Character_Set), você geralmente pode estimar que consegue enviar uma mensagem com 67 caracteres por segmento de mensagem.
- Teste, teste e teste! Sempre teste suas mensagens SMS antes do lançamento, especialmente ao usar Liquid e Conteúdo conectado.

### Se uma mensagem for enviada para um telefone fixo, ela ainda contará no meu total de envios de SMS? {#if-a-message-is-sent-to-a-landline-will-the-message-still-count-toward-my-sms-send-count}

Nos EUA, Canadá e Reino Unido:
- Se um SMS for enviado para um telefone fixo, ele será marcado como **Undelivered**. A Twilio ainda cobrará pela tentativa de entrega, então mensagens marcadas como **Sent**, **Delivered** ou **Undelivered** nos seus registros de mensagens serão cobradas.
- No Reino Unido, algumas operadoras converterão o SMS em uma mensagem de voz, entregando a mensagem.

Em outros países:
- A Twilio retornará um erro, e você não será cobrado pela tentativa de envio do SMS.

### Por que o dashboard da Braze está me avisando que posso ser cobrado por segmentos de mensagem adicionais quando minha mensagem tem menos de 160 (GSM-7) ou 70 (UCS-2) caracteres? {#why-is-the-braze-dashboard-warning-me-i-may-be-charged-for-additional-message-segments-when-my-message-is-under-160-gsm-7-or-70-ucs-2-characters}

Você pode ser cobrado por segmentos de mensagem adicionais se tiver personalização com Liquid incluída na sua mensagem. A renderização de blocos de conteúdo não ocorre até que a mensagem esteja sendo preparada para envio. Quando você está editando um SMS com um bloco de conteúdo, a Braze não sabe o que o bloco de conteúdo conterá, mas fornece uma estimativa aproximada. Recomendamos que os usuários usem o painel de teste para pré-visualizar a mensagem e entender melhor o que esperar.

## Envio e entregabilidade {#sending-and-deliverability}

### Posso incluir links em um SMS? {#can-you-include-links-in-an-sms}

Você pode incluir qualquer link em qualquer Campaign de SMS que desejar. No entanto, há algumas considerações:

- Links podem ocupar grande parte do limite de 160 caracteres do SMS. Se você incluir um link e texto, isso pode resultar em duas mensagens SMS em vez de apenas uma.
- Empresas frequentemente usam encurtadores de links para reduzir o impacto de caracteres de um link. No entanto, se enviar um link encurtado por um long code, as operadoras podem bloquear ou rejeitar a mensagem, pois podem suspeitar do redirecionamento do link.
- Usar um [short code]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup/) seria o tipo de número mais confiável para incluir links.

A Braze também possui seu próprio recurso de encurtamento de links que encurta links e fornece análise de dados de cliques automaticamente. Consulte [Encurtamento de links]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/link_shortening/) para mais informações.

### É necessário limitar a taxa de envio de mensagens SMS? {#do-you-need-to-rate-limit-how-fast-you-send-sms-messages}

A taxa de concorrência e throughput padrão permite cerca de 360.000 mensagens por hora por short code. Throughput adicional requer short codes adicionais.

### Como adicionar URLs à lista de permissões para SMS? {#how-do-you-allowlist-urls-for-sms}

Antes de enviar mensagens SMS contendo URLs para usuários em determinados países (por exemplo, Suécia ou países nórdicos), você precisa registrar essas URLs junto à operadora. Entre em contato com seu gerente de atendimento ao cliente da Braze para ajudar. Esse processo levará cerca de cinco dias.

### Quais são as melhores práticas de envio para evitar detecção de spam no SMS? {#what-are-the-best-sending-practices-to-avoid-spam-detection-for-sms}

1. Certifique-se de que as instruções de opt-in e descadastramento sejam claras.
2. Garanta que você (a marca) tenha um relacionamento com o cliente.
3. Certifique-se de que o conteúdo seja relevante para o relacionamento e para o que o usuário optou por receber.

Para mais diretrizes sobre como evitar detecção de spam, visite as [diretrizes de leis e regulamentações de SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations/).

### Quantos caracteres um emoji usa? {#how-many-characters-does-an-emoji-use}

Emojis podem ser complicados, pois não há uma contagem de caracteres padrão para todos os emojis. Existe o risco de o emoji exceder o limite de caracteres e dividir o SMS em várias mensagens, apesar de aparecer como uma única mensagem no criador da Braze. Ao testar suas mensagens, você pode verificar melhor se uma mensagem será dividida usando nossa [calculadora de segmentos]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator/#segment-calculator).

## Grupos de inscrições e opt-in/descadastramento {#subscription-groups-and-opt-inopt-out}

### Como criar lógica para opt-ins seletivos de SMS para que os usuários fiquem no grupo de inscrições correto? {#how-do-you-create-logic-for-selective-opt-ins-to-sms-so-users-are-in-the-right-subscription-group}

Palavras-chave personalizadas seriam registradas como eventos personalizados, então você precisaria criar segmentos com base nas palavras-chave que os clientes podem enviar por mensagem. Por exemplo, se um usuário optar por receber SMS para mensagens VIP, mas não para alertas, você pode criar um segmento VIP e um segmento de alertas, e então atribuir o usuário ao segmento apropriado.

### Se um usuário enviar "Stop" para nosso short code, ele terá a inscrição cancelada do grupo de inscrições? {#if-a-user-texts-stop-to-our-short-code-are-they-unsubscribed-from-the-subscription-group}

Como isso aparece no perfil do usuário? O grupo de inscrições reverterá para 2 traços (- -), e haverá eventos personalizados para inscrição e cancelamento de inscrição.

### Se um usuário tiver o descadastramento ativo e enviar uma palavra-chave para nosso short code e long code, ele receberá a resposta que configuramos para essa palavra-chave na Braze? {#if-a-user-is-opted-out-and-sends-a-keyword-to-our-short-and-long-code-do-they-receive-the-response-we-configured-for-that-keyword-in-braze}

Se um usuário tiver o descadastramento ativo e enviar uma palavra-chave de uma das [categorias de palavras-chave padrão]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/optin_optout/), ele receberá a resposta para essa palavra-chave. Se um usuário tiver o descadastramento ativo e enviar uma [palavra-chave personalizada]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/keyword_handling/), ele não receberá a resposta para essa palavra-chave.

### As propriedades de evento de SMS capturam palavras-chave em uma frase? {#will-sms-event-properties-capture-keywords-in-a-sentence}

Para que uma palavra-chave seja reconhecida dentro de uma frase (por exemplo, "por favor, pare de me enviar mensagens"), você precisará usar uma instrução Liquid na mensagem para reconhecer a palavra específica. As propriedades de evento têm um limite de 256 caracteres; fora isso, não há limite de caracteres.

## Testes {#testing}

### Mensagens de teste contam para os limites? {#do-test-text-messages-count-toward-limits}

Sim, contam. Tenha isso em mente ao testar mensagens.

### Um usuário precisa fazer parte de um grupo de inscrições de SMS para receber mensagens de teste de SMS? {#does-a-user-need-to-be-part-of-an-sms-subscription-group-to-receive-sms-test-messages}

Sim. Os usuários devem ter um número de telefone válido, fazer parte do grupo de inscrições de SMS usado para o envio de teste e ter pelo menos um país selecionado em **Geographic Permissions** para SMS.

### Existe uma maneira de verificar se um alias existe em um perfil de usuário? {#is-there-a-way-to-see-if-an-alias-exists-on-a-user-profile}

Os aliases não são visíveis no perfil do usuário. Você precisaria usar os endpoints de [Exportar dados de usuários]({{site.baseurl}}/api/endpoints/export/) para confirmar que os aliases foram definidos.

## MMS

### Há alguma alteração nos dados do Currents ao enviar um MMS? {#are-there-any-changes-to-currents-data-when-sending-an-mms}

Não, o mesmo nível de insight será fornecido ao enviar uma mensagem MMS.

### Posso controlar a ordem em que a imagem e o corpo da mensagem de um MMS são entregues? {#can-i-control-the-order-in-which-the-image-and-message-body-of-an-mms-are-delivered}

A Braze não tem controle sobre a ordem de exibição quando tanto o corpo da mensagem quanto as imagens estão incluídos em uma mensagem MMS. Isso depende de vários fatores, incluindo, mas não se limitando a:

- A operadora que recebe a mensagem
- O dispositivo que recebe a mensagem
- O tamanho total da mensagem

### O MMS requer um processo de integração separado? {#does-mms-require-a-separate-onboarding-process}

Não. O MMS agora está incluído no nosso processo de integração de SMS. Clientes existentes que já passaram pela integração podem começar a enviar Campaigns de MMS após concluir as seguintes etapas:

1. Adquirir o MMS.
2. Entrar em contato com a equipe de integração da Braze para solicitar a ativação do recurso de MMS. Isso habilitará o MMS e um grupo de inscrições de SMS/MMS será criado ou atualizado para você.

Em seguida, a equipe de integração da Braze garantirá que seus short codes e long codes estejam habilitados (nos EUA e Canadá) para MMS. Eles também atualizarão seus grupos de inscrições para mostrar seus números atuais que foram adicionados ou habilitados para MMS. Após essas etapas serem concluídas, você poderá enviar mensagens MMS imediatamente pelo nosso criador nativo de SMS.

### Por que não consigo encontrar o MMS no meu dashboard mesmo com o recurso habilitado? {#why-cant-i-find-mms-on-my-dashboard-even-though-the-feature-is-enabled}

O MMS só é exibido no dashboard da Braze quando um grupo de inscrições é considerado "habilitado para MMS". Isso é refletido por uma tag de MMS ao selecionar o grupo de inscrições no criador de uma mensagem SMS/MMS. Isso significa que pelo menos um número no grupo de inscrições é capaz de enviar uma mensagem MMS.

Além disso, certas situações exigirão que a Twilio reautorize a habilitação de short codes que originalmente não tinham MMS habilitado. Esse processo de aprovação pode levar semanas.

## RCS

### Por que minha mensagem RCS não é renderizada corretamente em dispositivos iOS? {#why-doesnt-my-rcs-message-render-accurately-on-ios-devices}

As mensagens RCS podem ser renderizadas de forma diferente em dispositivos iOS dependendo do sistema operacional e do app de mensagens. Em dispositivos iOS, os seguintes comportamentos podem ocorrer:

- Ações sugeridas de diferentes mensagens RCS na mesma conversa podem ser agrupadas e exibidas na ordem errada.
- Botões de rich cards e ações sugeridas que estão fora do rich card podem permanecer visíveis mesmo após tocar em um botão de rich card ou em uma ação sugerida.

{% alert note %}
A Braze envia a carga útil de RCS que você compõe, enquanto o cliente de mensagens controla como as ações sugeridas são ordenadas, agrupadas e ocultadas. Certifique-se de testar as mensagens RCS, especialmente aquelas que usam rich cards com ações sugeridas ou respostas sugeridas, em dispositivos Android e iOS antes de enviar.
{% endalert %}

### Posso enviar mensagens de voz pré-gravadas com RCS? {#can-i-send-pre-recorded-voicemails-with-rcs}

Sim, você pode usar mensagens de mídia para enviar arquivos de áudio.

### Por que os opt-ins de SMS via REST API não correspondem ao **Total de opt-ins** no desempenho de SMS/MMS/RCS? {#why-do-rest-api-sms-opt-ins-not-match-total-opt-ins-on-smsmmsrcs-performance}

**Total de opt-ins** e **Total de descadastramentos** no dashboard de [desempenho de SMS/MMS/RCS]({{site.baseurl}}/user_guide/analytics/dashboards/) contam alterações de inscrição geradas pelo processamento de palavras-chave de SMS recebidos (por exemplo, um usuário enviando uma palavra-chave de opt-in para o seu short code). Eles não incluem todas as atualizações de inscrição feitas pela REST API, pelo dashboard ou por outras fontes.

Para analisar opt-ins e descadastramentos por origem, use o [Criador de consultas]({{site.baseurl}}/user_guide/analytics/reports/query_builder/) em `USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED` e filtre por `STATE_CHANGE_SOURCE` (por exemplo, **Rest API** versus **Inbound Message**).