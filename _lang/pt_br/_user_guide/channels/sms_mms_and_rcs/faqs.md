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

A chave de API do identificador de app, ou `app_id`, é um parâmetro que associa a atividade a um app específico no seu espaço de trabalho. Ele designa com qual app dentro do espaço de trabalho você está interagindo. Por exemplo, você tem um `app_id` para o seu app iOS, um `app_id` para o seu app Android e um `app_id` para a sua integração web.

Para SMS, o parâmetro `app_id` é obrigatório ao enviar mensagens SMS pela API (como o endpoint `/messages/send`). Ele especifica qual app no seu espaço de trabalho está associado à atividade de SMS ou chamada de API. Você pode usar qualquer `app_id` válido de um app configurado no seu espaço de trabalho para envio de mensagens SMS, independentemente de o usuário ter esse app específico no perfil.

Você pode encontrar seu `app_id` acessando **Configurações** > **Configurações do app** e localizando a seção **Identification**.

### O que acontece se vários usuários tiverem o mesmo número de telefone? {#what-happens-if-multiple-users-have-the-same-phone-number}

Quando vários perfis de usuário que compartilham o mesmo número de telefone (ativado para SMS) são elegíveis para uma Campaign baseada em ação ou componente de Canvas ao mesmo tempo, disparados pelo evento de um SMS recebido, a Braze fará a deduplicação de usuários no nível do componente de Canvas. Isso impedirá que os usuários recebam mais de um SMS para um componente de Canvas, mesmo que vários usuários compartilhem o mesmo número de telefone.

{% alert note %}
A Braze não faz deduplicação por número de telefone em Canvas agendados.
{% endalert %}

A Braze usará o seguinte fluxo para determinar o perfil destinatário:
- Verificar qual perfil recebeu SMS mais recentemente (até 7 dias atrás); se existir, enviar para esse usuário.
- Se nenhum tiver recebido SMS nos últimos 7 dias, enviar para o usuário que tem um alias de usuário "phone" correspondente ao número de telefone.
- Se nenhum existir, enviar para um perfil aleatório entre os disponíveis.

Se você receber uma palavra-chave "START" ou "STOP" do número de telefone compartilhado, todos os perfis de usuário serão inscritos e ativados para SMS ou terão a inscrição cancelada. Isso também se aplica a alterações de status via API. Por exemplo, se vários perfis com IDs externos diferentes tiverem os mesmos números de telefone, uma alteração de status do grupo de inscrições pela API atualizará todos os perfis com aquele número de telefone, mesmo que apenas um ID externo seja especificado.

{% alert important %}
Se você escalonar seus usuários em um Canvas e tiver horários de agendamento diferentes para cada componente de Canvas, é possível enviar mensagens duplicadas para um usuário com o mesmo e-mail ou telefone.
{% endalert %}

Para evitar atualizações desnecessariamente grandes, a Braze atualizará no máximo 100 perfis de usuário que compartilham um identificador quando uma atualização de inscrição for feita. Se mais de 100 perfis de usuário compartilharem o mesmo número de telefone, nem todos os perfis serão atualizados.

### Por que vejo um pico de inscrições de SMS de uma fonte específica? {#why-do-i-see-a-spike-in-sms-subscriptions-from-a-specific-source}

Se você observar um aumento inesperadamente grande nas contagens de inscrição — especialmente ao analisar dados do endpoint [`/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status) por meio do Currents — isso pode ser causado por perfis de usuário duplicados.

Quando uma solicitação é feita ao endpoint `/subscription/status/set` com apenas um número de telefone (sem `external_id` fornecido), a Braze atualiza todos os perfis de usuário que compartilham aquele número de telefone. Se o seu espaço de trabalho tiver perfis duplicados, a contagem de usuários que atualizaram seu status de inscrição ficará inflada, mesmo que apenas um número de telefone tenha sido alterado.

Para analisar os dados de inscrição de forma mais precisa ao consultar o Currents, atualize sua consulta para contar números de telefone distintos em vez de contar todos os eventos de alteração de status de inscrição.

### O que são códigos curtos compartilhados? {#what-are-shared-short-codes}

Com um código curto compartilhado, todas as mensagens de texto, independentemente de qual empresa ou organização as envia, chegam ao dispositivo móvel do consumidor a partir do mesmo número de telefone de 5 a 6 dígitos. Embora os códigos curtos compartilhados tenham custo relativamente baixo e estejam disponíveis imediatamente, isso significa que sua empresa não terá um código curto dedicado.

Algumas desvantagens dessa abordagem incluem:

- Se os seus clientes cancelarem a inscrição das mensagens de outra empresa que compartilha um código curto com você, eles também terão cancelado a inscrição das suas mensagens.
- Se uma empresa violar as regras, as mensagens de todas as empresas serão suspensas.
- Problemas de segurança

## Faturamento e preços {#billing-and-pricing}

### Como serei cobrado pelo SMS? {#how-will-i-be-billed-for-sms}

Além das cobranças por códigos curtos e longos, a Braze oferece uma cota de mensagens SMS para diferentes países. Ou seja, trabalhamos com você para definir um determinado número de segmentos de mensagem para diferentes países, que você usará para enviar campanhas de SMS. O faturamento é feito pelo número de segmentos de mensagem enviados por país. Para saber mais sobre como os segmentos de mensagem são calculados, consulte nosso guia de [Segmentos de mensagem e limites de texto]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator). Seu gerente de conta entrará em contato para informá-lo caso esteja próximo de atingir seu limite máximo, fornecendo relatórios relevantes para mantê-lo informado. Para outras dúvidas sobre excedentes, entre em contato com seu representante da Braze.

### Os preços de MMS e SMS são diferentes? {#does-mms-and-sms-pricing-differ}

MMS e SMS têm custos diferentes e são cobrados separadamente com base no volume. Entre em contato com a equipe de integração da Braze para obter informações sobre preços.

### Como posso evitar excedentes? {#how-can-i-avoid-overages}

Embora não possamos garantir que você nunca terá um excedente, você pode seguir estas precauções para diminuir as chances de ultrapassar seus limites:

- Preste atenção ao número de caracteres no seu SMS. Enviar involuntariamente mais de um segmento pode causar excedentes. Para mais detalhes, consulte nosso [detalhamento de segmentos]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator).
- Calcule cuidadosamente os caracteres do seu SMS considerando Liquid ou Connected Content. O criador de SMS da Braze no dashboard não estima nem considera o uso de nenhum desses recursos.
- Considere o tipo de codificação que sua mensagem utiliza. Se sua mensagem usa codificação GSM-7, você geralmente pode estimar 160 caracteres por segmento de mensagem (menos se usar caracteres da tabela de extensão GSM-7). Se sua mensagem usa codificação [UCS-2](https://en.wikipedia.org/wiki/Universal_Coded_Character_Set), você geralmente pode estimar 67 caracteres por segmento de mensagem.
- Teste, teste e teste! Sempre teste suas mensagens SMS antes do envio, especialmente ao usar Liquid e Connected Content.

### Se uma mensagem for enviada para um telefone fixo, ela ainda contará no meu total de envios de SMS? {#if-a-message-is-sent-to-a-landline-will-the-message-still-count-toward-my-sms-send-count}

Nos EUA, Canadá e Reino Unido:
- Se um SMS for enviado para um telefone fixo, ele será marcado como **Undelivered**. O comportamento de faturamento depende do seu provedor de serviço de SMS. Com a Twilio, a tentativa de entrega ainda é cobrada, então mensagens marcadas como **Sent**, **Delivered** ou **Undelivered** nos seus registros de mensagens são faturadas.
- No Reino Unido, algumas operadoras convertem o SMS em uma mensagem de voz, entregando a mensagem.

Em outros países:
- Com a Twilio, um erro é gerado e você não é cobrado pela tentativa de envio da mensagem SMS.

### Por que o dashboard da Braze está me avisando que posso ser cobrado por segmentos de mensagem adicionais quando minha mensagem tem menos de 160 (GSM-7) ou 67 (UCS-2) caracteres? {#why-is-the-braze-dashboard-warning-me-i-may-be-charged-for-additional-message-segments-when-my-message-is-under-160-gsm-7-or-67-ucs-2-characters}

Você pode ser cobrado por segmentos de mensagem adicionais se houver personalização com Liquid incluída na sua mensagem. A renderização de blocos de conteúdo não ocorre até que a mensagem esteja sendo preparada para envio. Quando você está editando um SMS com um bloco de conteúdo, a Braze não sabe o que o bloco de conteúdo conterá, mas fornece uma estimativa aproximada. Recomendamos que os usuários utilizem o painel de teste para visualizar a mensagem e entender melhor o que esperar.

## Envio e entregabilidade {#sending-and-deliverability}

### Posso incluir links em um SMS? {#can-you-include-links-in-an-sms}

Você pode incluir qualquer link em qualquer Campaign de SMS que desejar. No entanto, há algumas preocupações a considerar:

- Links podem ocupar grande parte do limite de 160 caracteres do SMS. Se você incluir um link e texto, isso pode resultar em duas mensagens SMS em vez de apenas uma.
- Empresas frequentemente usam encurtadores de links para reduzir o impacto na contagem de caracteres. No entanto, ao enviar um link encurtado por um long code, as operadoras podem bloquear ou rejeitar a mensagem, pois podem suspeitar do redirecionamento do link.
- Usar um [short code]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup) seria o tipo de número mais confiável para incluir links.

A Braze também tem seu próprio recurso de encurtamento de links, que encurta links e fornece análise de cliques automaticamente. Consulte [Encurtamento de links]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/link_shortening) para saber mais.

### É necessário limitar a taxa de envio de mensagens SMS? {#do-you-need-to-rate-limit-how-fast-you-send-sms-messages}

A taxa de simultaneidade e throughput padrão permite cerca de 360.000 mensagens por hora por short code. Throughput adicional requer short codes adicionais.

### Como colocar URLs na lista de permissões para SMS? {#how-do-you-allowlist-urls-for-sms}

Antes de enviar mensagens SMS contendo URLs para usuários em determinados países (por exemplo, Suécia ou países nórdicos), você precisa registrar essas URLs junto à operadora. Entre em contato com seu gerente de atendimento ao cliente da Braze para obter ajuda. Esse processo leva cerca de cinco dias.

### Quais são as melhores práticas de envio para evitar a detecção de SPAM no SMS? {#what-are-the-best-sending-practices-to-avoid-spam-detection-for-sms}

1. Certifique-se de que as instruções de aceitação e cancelamento de inscrição sejam claras.
2. Garanta que você (a marca) tenha um relacionamento com o cliente.
3. Certifique-se de que o conteúdo seja relevante para o relacionamento e para o que o usuário aceitou receber.

Para mais orientações sobre como evitar a detecção de SPAM, visite as [Diretrizes de leis e regulamentos de SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations).

### Quantos caracteres um emoji utiliza? {#how-many-characters-does-an-emoji-use}

Emojis podem ser complicados, pois não existe uma contagem de caracteres padrão para todos os emojis. Há o risco de o emoji exceder o limite de caracteres e dividir o SMS em várias mensagens, mesmo que apareça como uma única mensagem no criador da Braze. Ao testar suas mensagens, você pode verificar melhor se uma mensagem será dividida usando nossa [calculadora de segmentos]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator#segment-calculator).

## Grupos de inscrições e aceitação/cancelamento {#subscription-groups-and-opt-inopt-out}

### Como criar lógica para aceitações seletivas de SMS de forma que os usuários fiquem no grupo de inscrições correto? {#how-do-you-create-logic-for-selective-opt-ins-to-sms-so-users-are-in-the-right-subscription-group}

Palavras-chave personalizadas seriam registradas como eventos personalizados, então você precisaria criar segmentos com base nas palavras-chave que os clientes podem enviar por mensagem de texto. Por exemplo, se um usuário aceita receber SMS para mensagens VIP, mas não para alertas, você pode criar um segmento VIP e um segmento de alertas e, em seguida, atribuir o usuário ao segmento apropriado.

### Se um usuário enviar "Stop" para nosso short code, ele é desinscrito do grupo de inscrições? {#if-a-user-texts-stop-to-our-short-code-are-they-unsubscribed-from-the-subscription-group}

Como isso aparece no perfil de usuário? O grupo de inscrições é exibido como desinscrito em **Contact Settings**, e há eventos personalizados para inscrição e cancelamento de inscrição.

### Se um usuário cancelou a inscrição e envia uma palavra-chave para nosso short code ou long code, ele recebe a resposta que configuramos para essa palavra-chave na Braze? {#if-a-user-is-opted-out-and-sends-a-keyword-to-our-short-and-long-code-do-they-receive-the-response-we-configured-for-that-keyword-in-braze}

Se um usuário cancelou a inscrição e envia uma palavra-chave de uma das [categorias de palavras-chave padrão]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/optin_optout), ele receberá a resposta correspondente a essa palavra-chave. Se um usuário cancelou a inscrição e envia uma [palavra-chave personalizada]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/keyword_handling), ele não receberá a resposta correspondente a essa palavra-chave.

### As propriedades de evento de SMS capturam palavras-chave dentro de uma frase? {#will-sms-event-properties-capture-keywords-in-a-sentence}

Para que uma palavra-chave seja reconhecida dentro de uma frase (por exemplo, "please stop texting me"), você precisará usar uma instrução Liquid na mensagem para reconhecer a palavra específica. As propriedades de evento têm um limite de 256 caracteres; fora isso, não há limite de caracteres.

## Testes {#testing}

### As mensagens de texto de teste contam para os limites? {#do-test-text-messages-count-toward-limits}

Sim, contam. Leve isso em consideração ao testar mensagens.

### Um usuário precisa fazer parte de um grupo de inscrições de SMS para receber mensagens de teste por SMS? {#does-a-user-need-to-be-part-of-an-sms-subscription-group-to-receive-sms-test-messages}

Sim, precisa. Os usuários devem ter um número de telefone válido, fazer parte do grupo de inscrições de SMS usado para o envio de teste e ter pelo menos um país selecionado em **Geographic Permissions** para SMS.

### Existe uma maneira de verificar se um alias existe em um perfil de usuário? {#is-there-a-way-to-see-if-an-alias-exists-on-a-user-profile}

Os aliases não são visíveis no perfil de usuário. Você precisaria usar os endpoints de [exportação de dados de usuários]({{site.baseurl}}/api/endpoints/export) para confirmar se os aliases foram definidos.

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

### Por que meu MMS com imagem falha ao enviar? {#why-does-my-mms-with-an-image-fail-to-send}

Alguns provedores de SMS validam o cabeçalho `Content-Type` nas URLs de imagem. Se um MMS com imagem for interrompido, confirme se a URL da imagem hospedada retorna `image/png` ou outro tipo de imagem compatível (por exemplo, com `curl -I <image-url>`). Hospede novamente o ativo na biblioteca de mídia da Braze ou em uma CDN que sirva o `Content-Type` correto.

### Por que a imagem do meu cartão de contato não aparece em um MMS? {#why-doesnt-my-contact-card-image-appear-in-an-mms}

As fotos de cartões de contato em MMS podem não ser exibidas quando o arquivo do cartão de contato faz referência a uma URL de imagem que o dispositivo do destinatário não consegue acessar. Crie o cartão de contato em um celular, exporte o arquivo e faça upload na biblioteca de mídia para usar na sua mensagem MMS.

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

**Total de opt-ins** e **Total de descadastramentos** no dashboard de [desempenho de SMS/MMS/RCS]({{site.baseurl}}/user_guide/analytics/dashboards) contam alterações de inscrição geradas pelo processamento de palavras-chave de SMS recebidos (por exemplo, um usuário enviando uma palavra-chave de opt-in para o seu short code). Eles não incluem todas as atualizações de inscrição feitas pela REST API, pelo dashboard ou por outras fontes.

Para analisar opt-ins e descadastramentos por origem, use o [Criador de consultas]({{site.baseurl}}/user_guide/analytics/reports/query_builder) em `USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED` e filtre por `STATE_CHANGE_SOURCE` (por exemplo, **Rest API** versus **Inbound Message**).