---
nav_title: Criar uma mensagem
article_title: Criar uma mensagem SMS, MMS ou RCS
page_order: 1
description: "Crie uma mensagem SMS, MMS ou RCS e configure tipos de mensagem, campos, encurtamento de links, configurações de entrega e comportamento específicos do canal."
page_type: reference
alias: /create_sms_mms_rcs_message/
tool:
  - Campaigns
  - Canvas
channel:
  - SMS
  - MMS
  - RCS
search_rank: 1
---

# Criar uma mensagem SMS, MMS ou RCS {#create-an-sms-mms-or-rcs-message}

> Crie mensagens personalizadas de SMS, MMS e Rich Communication Services (RCS) em Campaigns ou Canvas. O grupo de inscrições selecionado determina quais tipos de mensagem e remetentes estão disponíveis.

## Pré-requisitos {#prerequisites}

Antes de começar, verifique se você tem o seguinte:

| Requisito | Descrição |
| --- | --- |
| Configuração do remetente | Conclua a [configuração do remetente]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup). Para enviar MMS, seu grupo de inscrições precisa de um número de telefone com MMS ativado. Para enviar RCS, conclua a [configuração de RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/rcs_setup) e adicione um remetente RCS verificado. |
| Grupo de inscrições | Crie um [grupo de inscrições]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups) que contenha os remetentes para esta mensagem. |
| Números de telefone e consentimento dos usuários | Importe os números de telefone dos usuários e colete as [aceitações de SMS, MMS e RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/collecting_user_opt_ins) apropriadas. |
| Campaign ou Canvas | Use uma Campaign para uma única mensagem direcionada ou Canvas para uma jornada de usuário com várias etapas. |
| Créditos de mensagem ou de ação | Confirme se a sua conta tem créditos disponíveis. O envio de mensagens SMS, MMS e RCS pela Braze utiliza esses créditos. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos para mensagens SMS, MMS e RCS" }

## Criar uma mensagem {#create-a-message}

### Etapa 1: Escolha onde criar sua mensagem {#step-1-choose-where-to-build-your-message}

{% tabs %}
{% tab Campaign %}

1. Acesse **Messaging** > **Campaigns** e selecione **Create Campaign**.
2. Selecione **SMS/MMS/RCS** ou, para campanhas direcionadas a vários canais, selecione **Multichannel Campaign**.
3. Dê à sua campanha um nome claro e significativo.
4. Adicione [Equipes]({{site.baseurl}}/user_guide/administer/global/user_management/teams) e [Tags]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags) conforme necessário.
  - As tags facilitam encontrar e usar suas campanhas em relatórios.
5. Adicione e nomeie as variantes da sua campanha. Você pode incluir variantes de SMS/MMS e RCS na mesma campanha. Para saber mais, consulte [Testes multivariantes e A/B]({{site.baseurl}}/user_guide/messaging/ab_testing).

{% alert tip %}
Se as variantes da sua campanha tiverem conteúdo semelhante, crie a primeira mensagem antes de adicionar mais variantes. Em seguida, selecione **Copy from Variant** no menu suspenso **Add Variant**.
{% endalert %}

{% endtab %}
{% tab Canvas %}

{% multi_lang_include messaging/canvas_message_step_setup.md %}

{% endtab %}
{% endtabs %}

### Etapa 2: Selecione um grupo de inscrições e o tipo de mensagem {#step-2-select-a-subscription-group-and-message-type}

Selecione o **grupo de inscrições** que contém o remetente desta mensagem. A Braze utiliza o grupo selecionado para calcular o público alcançável e determinar a elegibilidade no momento do envio.

O grupo de inscrições selecionado determina quais tipos de mensagem estão disponíveis no criador:

| Tipo de grupo de inscrições | Tipos de mensagem disponíveis |
| --- | --- |
| Somente SMS | SMS |
| SMS com números habilitados para MMS | SMS e MMS |
| Habilitado para RCS com um remetente RCS verificado | RCS e SMS quando o grupo também contém um remetente SMS. MMS também está disponível quando esse remetente é habilitado para MMS. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Tipos de mensagem disponíveis por grupo de inscrições" }

{% alert tip %}
Adicione pelo menos um remetente SMS a um grupo de inscrições RCS para poder enviar um SMS de fallback quando a entrega RCS falhar.
{% endalert %}

Se o grupo de inscrições suportar ambos os protocolos, selecione **SMS/MMS** ou **RCS**. Para RCS, selecione **Text**, **Media** ou **Card**.

### Etapa 3: Componha sua mensagem {#step-3-compose-your-message}

Os campos e limites no criador dependem do tipo de mensagem selecionado.

{% tabs local %}
{% tab SMS e MMS %}

#### Campos e configurações de SMS e MMS {#sms-and-mms-fields-and-settings}

| Campo ou configuração | Descrição |
| --- | --- |
| **Language** | Insere conteúdo específico do idioma na mensagem. |
| **Message** | Insira até 1.600 caracteres, incluindo Liquid, Connected Content e emojis. O criador estima a codificação, a contagem de caracteres e o número de segmentos de SMS faturáveis. Uma mensagem MMS pode conter mídia sem corpo de mensagem. |
| **Media** | Para um grupo de inscrições habilitado para MMS, adicione uma imagem PNG, JPEG ou GIF da biblioteca de mídia ou por URL. Você pode adicionar um vCard em vez de uma imagem. |
| **Link shortening** | Encurta URLs HTTP e HTTPS e rastreia o engajamento. Para encurtamento de links legado, selecione rastreamento básico ou avançado. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Campos e configurações de SMS e MMS" }

As mensagens SMS usam codificação GSM-7 ou UCS-2 e são cobradas por Segment de mensagem. Um único caractere pode alterar a codificação e aumentar o número de segmentos faturáveis. Para regras de codificação, tamanhos de Segment e a calculadora de segmentos, consulte [Calculadoras de faturamento de SMS e RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator).

![Criador de SMS mostrando o texto da mensagem e as estimativas de contagem de caracteres e segmentos.]({% image_buster /assets/img/sms_campaign_compose.png %})

#### Especificações de mídia MMS {#mms-media-specifications}

{% multi_lang_include channels/image_specs.md variable_name='sms and mms' %}

Para enviar dados comerciais que os usuários possam salvar nos contatos do dispositivo, consulte [Cartões de contato]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/create/contact_card). O envio de um cartão de contato é cobrado como MMS.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

A disponibilidade e a renderização de MMS dependem da operadora receptora. Quando uma operadora não pode aceitar MMS, a mídia se torna um link no corpo do SMS por meio do provedor. Evite enviar MMS para números do Google Voice, pois o suporte limitado de MMS pode causar entregas não confiáveis.

Quando um usuário envia mídia de entrada, a Braze expõe suas URLs nos [eventos de entrada de SMS do Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#sms-inbound-received-events) e por meio de {% raw %}`{{sms.${inbound_media_urls}}}`{% endraw %} em Liquid.

{% endtab %}
{% tab RCS %}

#### Tipos de mensagem RCS {#rcs-message-types}

| Tipo de mensagem | Campos e configurações | Limites e comportamento |
| --- | --- | --- |
| **Text** | Corpo da mensagem obrigatório, respostas sugeridas ou ações Open URL opcionais, SMS de fallback opcional e encurtamento de links | O corpo da mensagem pode conter até 1.600 ou 3.072 caracteres, dependendo do provedor de serviço SMS. Adicione até cinco sugestões. |
| **Media** | Imagem, vídeo, documento ou áudio obrigatório; corpo de mensagem opcional; sugestões opcionais, SMS de fallback e encurtamento de links | O corpo da mensagem pode conter até 1.600 ou 3.072 caracteres, dependendo do provedor, e é cobrado como uma mensagem RCS adicional. Adicione até cinco sugestões. |
| **Card** | Cartão de mídia ou cartão somente texto, título, descrição, botões, sugestões opcionais e SMS de fallback opcional | O título pode conter até 200 caracteres. A descrição pode conter até 1.600 ou 2.000 caracteres, dependendo do provedor. Adicione entre um e quatro botões. O suporte do provedor determina se cartões somente texto e sugestões fora do cartão estão disponíveis. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Tipos de mensagem RCS, campos e limites" }

As sugestões podem ser respostas sugeridas, que pré-preenchem a entrada de texto do usuário, ou ações Open URL. Adicione até 25 caracteres de texto a cada sugestão e uma URL de até 2.048 caracteres a cada ação Open URL.

Para qualquer tipo de mensagem RCS, ative **Send SMS if RCS fails** para adicionar uma mensagem de fallback de até 1.600 caracteres. O grupo de inscrições selecionado deve conter um remetente SMS. Para mensagens **Card**, os links na descrição não são clicáveis; use um botão Open URL em vez disso.

Alguns provedores de serviço SMS não suportam mensagens **Media** independentes ou cartões somente texto. O criador exibe apenas os tipos de mensagem RCS suportados. Para mensagens **Card**, o encurtamento de links se aplica apenas aos links no SMS de fallback.

O faturamento de mensagens RCS depende do tipo e do conteúdo da mensagem. Para regras de faturamento básico, rich e rich card, consulte [Faturamento de mensagens RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator#rcs-message-billing).

#### Especificações de mídia RCS {#rcs-media-specifications}

O criador aceita uma URL de mídia com até 1.000 caracteres. Os formatos disponíveis e o tamanho máximo do arquivo dependem do provedor de serviço SMS.

| Tipo de arquivo | Especificações |
| --- | --- |
| Todos | O tamanho máximo do arquivo é 16&nbsp;MB ou 100&nbsp;MB, dependendo do provedor. |
| Imagem | JPEG, JPG, GIF, PNG |
| Vídeo | H263, M4V, MP4, MPEG, MPEG-4, WEBM |
| Documento | PDF. Disponível para mensagens **Media**, mas não para cartões de mídia. |
| Áudio | AAC, MP3, MPEG, MP4, 3GPP, OGG. O suporte do provedor varia. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Especificações de mídia RCS" }

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

{% endtab %}
{% endtabs %}

#### Personalização {#personalization}

Use [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid), [Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content), emojis e conteúdo específico por idioma para personalizar sua mensagem. Inclua um valor padrão para a personalização com Liquid para que perfis com dados incompletos não recebam conteúdo em branco.

Para criar o texto da mensagem a partir de um prompt, use [Gerar texto]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#generate-copy) com o Operator.

Para idiomas escritos da direita para a esquerda, consulte [Criando mensagens da direita para a esquerda]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages).

#### Criar fluxos de mensagens conversacionais (RCS) {#create-conversational-message-workflows-rcs}

Os fluxos de mensagens conversacionais permitem que você responda dinamicamente aos usuários, criando uma experiência de mensagens de ida e volta. Para criar um fluxo, crie um Canvas e combine respostas sugeridas com [jornadas de ação]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths) para direcionar seu fluxo com base na resposta que o usuário selecionar.

1. No criador de Canvas, crie uma etapa de mensagem RCS com várias respostas sugeridas.

![Criador de mensagem RCS com respostas sugeridas.]({% image_buster /assets/img/rcs/suggested_replies.png %})

{: start="2"}
2. Conecte essa mensagem a uma jornada de ação com um grupo de ações para cada resposta sugerida.
3. Para cada grupo de ações:
   - Selecione o disparador **Send an SMS inbound message**.
   - Defina o corpo da mensagem para ser igual à resposta sugerida correspondente.

![Etapa de jornada de ação configurada com três grupos de ações, um para cada resposta sugerida.]({% image_buster /assets/img/rcs/quick_reply.png %})

{: start="4"}
4. Conecte cada grupo de ações a uma etapa de mensagem RCS e adicione conteúdo com base na resposta sugerida associada.
5. Continue o fluxo conversacional adicionando respostas sugeridas a qualquer mensagem de acompanhamento.
6. Repita as etapas 2 a 4 até que o fluxo esteja completo.

![Canvas mostrando um fluxo conversacional com duas jornadas de ação.]({% image_buster /assets/img/rcs/full_conversational_workflow.png %})

### Etapa 4: Configure o encurtamento de links {#step-4-configure-link-shortening}

Ative **Link shortening** para encurtar URLs HTTP e HTTPS e rastrear cliques em links de SMS, MMS e RCS suportados. Dependendo da versão disponível no seu espaço de trabalho, selecione rastreamento básico ou avançado, ou use o encurtamento de links unificado.

O rastreamento avançado adiciona dados de cliques no nível do usuário para segmentação e redirecionamento. O encurtamento de links unificado combina links encurtados de SMS e RCS em um formato personalizado. Para URLs suportadas, comportamento de Liquid, requisitos de teste, domínios personalizados e redirecionamento, consulte [Encurtamento de links]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/link_shortening).

A Braze encurta até 25 links em uma mensagem. Uma URL com mais de 4.000 caracteres não pode ser encurtada e faz com que a mensagem falhe no momento do envio.

### Etapa 5: Prévia e teste da mensagem {#step-5-preview-and-test-your-message}

Acesse a guia **Test** para visualizar a prévia da mensagem como um usuário ou enviar um SMS, MMS ou RCS de teste para um [grupo de teste de conteúdo]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#content-test-groups) ou usuário individual.

{% alert tip %}
Use a [calculadora de segmentos de SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator#segment-calculator) para estimar quantos segmentos sua mensagem contém.
{% endalert %}

![Prévia do texto do SMS na guia Test do criador. Na seção de perfil, o campo nome está definido como "James". Na seção de prévia, o SMS agora diz "Hi James, we appreciate your support!"]({% image_buster /assets/img/sms_campaign_test.png %})

Para MMS, o telefone receptor determina se a mídia aparece antes ou depois do corpo da mensagem.

{% alert note %}
Como a renderização RCS é controlada pelo sistema operacional do usuário, fabricante do dispositivo, operadora e app de mensagens (por exemplo, Google Messages vs. Apple Messages), a aparência da mensagem pode variar. A prévia mostrada na Braze pode não corresponder exatamente ao que o usuário final recebe. Valide a renderização final em dispositivos reais sempre que possível. Para detalhes sobre a renderização RCS em dispositivos iOS, consulte [Por que minha mensagem RCS não renderiza corretamente em dispositivos iOS?]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/faqs#why-doesnt-my-rcs-message-render-accurately-on-ios-devices). Para GIFs em rich cards, consulte [Por que GIFs em rich cards RCS aparecem estáticos no iOS?]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/faqs#why-do-gifs-in-rcs-rich-cards-appear-static-on-ios).
{% endalert %}

Para saber mais, consulte [Enviar mensagens de teste]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=sms%2Fmms%20and%20rcs).

### Etapa 6: Construa o restante da campanha ou Canvas {#step-6-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab Campaign %}

#### Escolha um cronograma ou disparador de entrega {#choose-a-delivery-schedule-or-trigger}

Entregue mensagens em um horário agendado ou em resposta a uma ação ou disparador de API. Para opções de agendamento e disparadores, consulte [Agende sua campanha]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign).

Configure controles de entrega como [reelegibilidade]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility#turning-on-re-eligibility) e [limite de frequência]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#about-frequency-capping). Para entrega baseada em ação, defina a duração da campanha e o [horário de silêncio]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours).

#### Escolha os usuários-alvo {#choose-users-to-target}

[Direcione usuários]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users) selecionando Segments e filtros. A Braze calcula a associação exata ao Segment antes de enviar a mensagem.

O grupo de inscrições selecionado filtra os usuários inscritos. Os destinatários de SMS e MMS também precisam de um número de telefone válido. Os destinatários de RCS precisam de um dispositivo e conexão de operadora com capacidade RCS; use um SMS de fallback para alcançar usuários elegíveis quando a entrega RCS falhar.

{% multi_lang_include audience/target_audiences.md %}

Para direcionamento por cliques e interações, consulte [Redirecionamento de usuários]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/user_retargeting).

#### Escolha eventos de conversão {#choose-conversion-events}

Use [eventos de conversão]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events) para medir ações após um usuário receber a campanha. Defina uma janela de conversão de até 30 dias.

{% endtab %}
{% tab Canvas %}

Complete as seções restantes do seu Canvas. Para cronogramas de entrada, configurações de público e controles de envio, consulte [Criar um Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas).

{% endtab %}
{% endtabs %}

### Etapa 7: Revise e implante {#step-7-review-and-deploy}

Depois de finalizar a construção da sua campanha ou Canvas, revise os detalhes e teste a mensagem antes de enviá-la.

Após o lançamento, use os [relatórios de SMS, MMS e RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/reporting) para acompanhar o desempenho das mensagens.

## Informações importantes {#things-to-know}

- O SMS é cobrado por Segment de mensagem, o MMS tem sua própria taxa, e o RCS é cobrado por tipo de mensagem. Consulte as [calculadoras de faturamento de SMS e RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator) antes de enviar.
- O MMS é compatível com uma imagem ou vCard. O suporte da operadora determina se os destinatários recebem a mídia ou um link para a imagem.
- Os recursos e limites do RCS variam de acordo com o provedor de serviços de SMS. O criador exibe apenas as opções disponíveis para o grupo de inscrições selecionado.
- Você pode enviar um correio de voz pré-gravado como áudio em uma mensagem RCS do tipo **Mídia**.
- O comportamento de renderização e interação varia de acordo com o dispositivo, a operadora, o sistema operacional e o app de mensagens.