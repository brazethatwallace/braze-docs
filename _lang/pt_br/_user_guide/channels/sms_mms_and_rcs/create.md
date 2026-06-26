---
nav_title: Criar uma mensagem
article_title: Criar uma mensagem SMS, MMS ou RCS
page_order: 1
description: "Este artigo aborda como criar e enviar uma mensagem SMS, MMS ou RCS na Braze."
page_type: reference
alias: /create_sms_mms_rcs_message/
tool:
  - Campaigns
channel:
  - SMS
  - MMS
  - RCS
search_rank: 1
---

# Criar uma mensagem SMS, MMS ou RCS {#create-an-sms-mms-or-rcs-message}

> Campanhas de SMS, MMS e RCS são ótimas para alcançar diretamente e conversar de forma programática com seus clientes. Você pode usar Liquid e outros conteúdos dinâmicos para criar uma experiência pessoal com seus usuários e criar um ambiente que promova e aprimore uma experiência de usuário discreta com sua marca.

## Etapa 1: Escolha onde criar sua mensagem {#step-1-choose-where-to-build-your-message}

Não tem certeza se sua mensagem deve ser enviada usando uma campanha ou um Canvas? Campanhas são melhores para envios de mensagens únicos e direcionados, enquanto Canvas são melhores para jornadas de usuário com várias etapas.

{% tabs %}
{% tab Campaign %}

1. Acesse **Envio de mensagens** > **Campaigns** e selecione **Criar campanha**.
2. Selecione **SMS/MMS/RCS** ou, para campanhas direcionadas a múltiplos canais, selecione **Multicanal**.
3. Dê à sua campanha um nome claro e significativo.
4. Adicione [equipes]({{site.baseurl}}/user_guide/administer/global/user_management/teams) e [tags]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags) conforme necessário.
   * Tags facilitam a busca e a criação de relatórios das suas campanhas. Por exemplo, ao usar o [Criador de relatórios]({{site.baseurl}}/user_guide/analytics/reports/report_builder), você pode filtrar por tags específicas.
5. Adicione e nomeie quantas variantes forem necessárias para sua campanha. Você pode escolher diferentes plataformas, tipos de mensagem e layouts para cada uma das variantes adicionadas. Para saber mais sobre esse tópico, consulte [Testes multivariantes e A/B]({{site.baseurl}}/user_guide/messaging/ab_testing).
   * A Braze permite incluir variantes de SMS e RCS em uma única campanha, para que você possa comparar o desempenho de cada uma.

{% alert tip %}
Se todas as mensagens da sua campanha forem semelhantes ou tiverem o mesmo conteúdo, redija sua mensagem antes de adicionar variantes adicionais. Depois, escolha **Copiar da variante** no menu suspenso **Adicionar variante**.
{% endalert %}

{% endtab %}
{% tab Canvas %}

1. [Crie seu Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas) usando o criador de Canvas.
2. Depois de configurar seu Canvas, adicione uma etapa de mensagem **SMS/MMS/RCS** no construtor de Canvas.
3. Dê à sua etapa um nome claro e significativo.
4. Escolha um [agendamento de etapa]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/delivery_and_entry_types#schedule-delay) e especifique uma postergação conforme necessário.
5. Filtre seu público para esta etapa conforme necessário. Você pode refinar ainda mais os destinatários desta etapa especificando segmentos e adicionando filtros adicionais. As opções de público serão verificadas após a postergação, no momento em que as mensagens forem enviadas.
6. Escolha seu [comportamento de avanço]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/cloning_canvases).
7. Escolha quaisquer outros canais de envio de mensagens que você deseja combinar com sua mensagem.

{% endtab %}
{% endtabs %}

## Etapa 2: Selecione um grupo de inscrições {#step-2-select-a-subscription-group}

Selecione um [grupo de inscrições]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups) para garantir que você está enviando sua mensagem para os usuários corretos. Ao selecionar um grupo de inscrições, a Braze adicionará automaticamente um filtro de segmentação, garantindo que apenas usuários inscritos receberão a campanha.

O grupo de inscrições selecionado determina quais tipos de mensagem estão disponíveis no criador:

| Tipo de grupo de inscrições | Tipos de mensagem disponíveis |
| --- | --- |
| Somente SMS | SMS |
| SMS com números habilitados para MMS | SMS e MMS |
| Habilitado para RCS (com remetente verificado para RCS) | SMS, MMS (se habilitado) e RCS |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Etapa 2: Selecione um grupo de inscrições" }

{% alert tip %}
A Braze recomenda fortemente que todo grupo de inscrições que contenha um remetente RCS também inclua pelo menos um código SMS para fallback. Isso garante que, se uma mensagem RCS não for entregue (por exemplo, devido a incompatibilidade de dispositivo ou cobertura incompleta da operadora), a mensagem ainda chegue ao seu usuário via SMS.
{% endalert %}

Após selecionar seu grupo de inscrições, escolha o tipo de mensagem que deseja redigir. Se seu grupo de inscrições suportar múltiplos tipos, você verá opções para selecionar entre eles.

![Opções para selecionar entre um tipo de mensagem RCS ou SMS/MMS.]({% image_buster /assets/img/rcs/rcs_message_type.png %}){: style="max-width:65%;"}

## Etapa 3: Redija sua mensagem {#step-3-compose-your-message}

A experiência de redação muda dependendo do tipo de mensagem selecionado. Selecione a guia do seu tipo de mensagem.

{% tabs local %}
{% tab SMS %}

Escreva sua mensagem usando idiomas e personalização (Liquid, Conteúdo conectado e emojis) conforme necessário. Certifique-se de seguir nossos limites de texto para reduzir suas chances de cobranças excedentes.

{% alert important %}
Antes de prosseguir, leia as diretrizes sobre [segmentos de mensagem SMS e limites de texto]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator). Segmentos de mensagem SMS são os lotes de caracteres que as operadoras de telefonia usam para medir mensagens de texto. As mensagens são cobradas por segmento de mensagem, então é uma boa ideia entender as nuances de como as mensagens serão divididas.
{% endalert %}

![Criador de SMS na Braze com a mensagem "Olá first_name, agradecemos seu apoio! Que tal passar em uma de nossas lojas e mostrar este SMS para um desconto exclusivo? Responda PARAR para deixar de receber mensagens nossas."]({% image_buster /assets/img/sms_campaign_compose.png %})

### Adicionando um cartão de contato {#adding-a-contact-card}

Você pode adicionar um cartão de contato à sua mensagem SMS para que os clientes possam adicionar as informações da sua empresa e de contato aos contatos do dispositivo. Você pode atribuir propriedades como nome da empresa, número de telefone, endereço, e-mail e uma foto pequena. Consulte [Cartões de contato]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/create/contact_card) para mais detalhes.

{% endtab %}
{% tab MMS %}

Para enviar uma mensagem MMS, seu grupo de inscrições deve ter pelo menos um número de telefone habilitado para MMS. Isso é indicado por uma tag **MMS** ao lado do grupo de inscrições no criador.

Insira o corpo da sua mensagem e, em seguida, faça upload de uma imagem PNG, JPEG ou GIF da [Biblioteca de mídia]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library) ou especifique uma URL de imagem. Apenas uma imagem é suportada por mensagem.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

![A guia de redação para escrever uma mensagem MMS.]({% image_buster /assets/img/sms/mms_composer.png %}){: style="max-width:80%;"}

### Especificações de imagem {#image-specifications}

| Propriedade | Recomendação |
| --- | --- |
| Tamanho | Até 600&nbsp;KB |
| Tipos de arquivo | PNG, JPEG, GIF |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Especificações de imagem" }

### Cartões de contato {#contact-cards}

Você também pode incluir um [cartão de contato]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/create/contact_card) (vCard) em vez de uma imagem.

### Comportamento da operadora {#carrier-behavior}

Mensagens MMS são cobradas a uma taxa diferente das mensagens SMS somente texto. Nem todas as operadoras aceitam MMS. Nesses casos, o MMS é automaticamente convertido em um link de imagem que o usuário pode selecionar.

{% alert note %}
Evite enviar MMS para números do Google Voice. O Google Voice tem suporte limitado a MMS, o que causa entrega de mensagens não confiável.
{% endalert %}

### MMS de entrada e personalização {#inbound-mms-and-personalization}

Quando um cliente envia uma mensagem de entrada que inclui mídia, a Braze expõe a mídia nos [eventos de entrada de SMS do Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#sms-inbound-received-events) e em Liquid como {% raw %}`{{sms.${inbound_media_urls}}}`{% endraw %} (por exemplo, em mensagens de redirecionamento ou acompanhamento). Para saber mais sobre o uso de propriedades de SMS de entrada no Canvas, consulte [Etapa de mensagem]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step).

{% endtab %}
{% tab RCS %}

Assista a este passo a passo rápido para ver como criar uma mensagem RCS de texto ou mídia.

{% multi_lang_include video.html id="3y0iiqqygw" source="wistia" %}

Escolha entre um tipo de mensagem **Texto** ou **Mídia**.

![Opções para selecionar entre um tipo de mensagem Texto ou Mídia.]({% image_buster /assets/img/rcs/rcs_text_media.png %}){: style="max-width:65%;"}

{% subtabs %}
{% subtab Texto %}

Mensagens RCS de texto focam no texto como meio. Se sua mensagem tiver até 160 caracteres sem elementos ricos, ela é cobrada como uma mensagem RCS básica. Se você exceder 160 caracteres ou usar um elemento rico, ela é cobrada como uma mensagem RCS rica (única) com um limite de 3.072 caracteres.

**Recursos:**

- Todos os recursos de SMS estão incluídos, com rastreamento avançado disponível para rastreamento de cliques em URL.
- **Respostas sugeridas**: Botões contendo respostas sugeridas que os usuários podem selecionar para preencher automaticamente no campo de texto.
- **Ações sugeridas**: Botões que iniciam uma ação no dispositivo do usuário. Atualmente, a Braze suporta ações sugeridas OpenURL, que redirecionam os usuários para uma página da web ou outro local identificado por URL.

![Três ações sugeridas para uma mensagem RCS promovendo estilos de moda em tendência.]({% image_buster /assets/img/rcs/rcs_suggested_actions.gif %}){: style="max-width:70%;"}

**Considerações:**

- Android e iOS podem truncar de forma diferente: o Android mostra o texto completo da mensagem rica, enquanto o iOS trunca após a terceira linha.
- Você pode adicionar até cinco botões por mensagem. Eles podem ser ações sugeridas ou respostas sugeridas.
- Blocos de texto longos e muitos botões podem sobrecarregar os destinatários; prefira a simplicidade quando possível.
- Em alguns casos, pode ser mais econômico enviar mensagens de texto mais longas via RCS do que via SMS, porque mensagens SMS mais longas são divididas em múltiplos segmentos cobráveis, enquanto mensagens RCS são cobradas por mensagem.

{% endsubtab %}
{% subtab Mídia %}

Mensagens RCS de mídia permitem usar formatos de mídia envolventes que não são possíveis com SMS, incluindo arquivos de imagem, vídeo e documento.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

**Recursos:**

- Suporta tudo disponível nos tipos de mensagem de texto, incluindo texto, respostas sugeridas e ações sugeridas.
- Arquivos de imagem (JPEG, PNG) enviados da [Biblioteca de mídia]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library).
- Arquivos de vídeo (MP4, MPEG, MV4) adicionados por URL no criador de mensagens.
- Arquivos de documento (PDF) adicionados por URL no criador de mensagens.

![Criador de RCS com uma opção para fazer upload de um arquivo de mídia.]({% image_buster /assets/img/rcs/rcs_media_type.png %})

**Especificações de arquivo:**

| Tipo de arquivo | Especificações |
| --- | --- |
| Todos | Tamanho do arquivo limitado a 100 MB. A URL do arquivo pode ter até 2.048 caracteres. |
| Imagem | Formatos suportados: JPG, JPEG, GIF |
| Vídeo | Formatos suportados: H263, M4V, MP4, MPEG-4, MPEG, WEBM |
| Documento | Formato suportado: PDF |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Especificações de arquivo" }

**Considerações:**

A experiência do usuário ao receber mensagens RCS pode variar com base na cobertura da operadora, hardware do dispositivo móvel e sistema operacional. O RCS se integra de forma mais natural com dispositivos Android, e diferentes dispositivos podem renderizar a experiência em diferentes velocidades e qualidades.

{% endsubtab %}
{% endsubtabs %}

Escreva sua mensagem usando idiomas e personalização ([Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid), [Conteúdo conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content) e emojis) conforme necessário. Certifique-se de seguir os limites de texto para reduzir suas chances de cobranças excedentes.

{% alert important %}
Antes de prosseguir, leia as [diretrizes de tipo de mensagem RCS](#step-3-compose-your-message) acima. Mensagens RCS são [cobradas por mensagem]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator), então é uma boa ideia entender o que pode ser incluído em cada tipo.
{% endalert %}

{% endtab %}
{% endtabs %}

### Dicas {#tips}

#### Usando Liquid {#using-liquid}

{% raw %}
Se você planeja usar Liquid, certifique-se de incluir um valor padrão para a personalização escolhida para que, caso o perfil do usuário esteja incompleto, ele não receba um espaço em branco `Olá, !` em vez do nome ou uma frase coerente.
{% endraw %}

#### Gerando texto com IA {#generating-ai-copy}

Experimente usar o [Assistente de Copywriting com IA]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#generate-copy). Insira o nome ou a descrição de um produto, e a IA gerará um texto de marketing semelhante ao humano para uso no seu envio de mensagens.

![Botão Iniciar Copywriter com IA, localizado no campo Mensagem do criador de SMS.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_sms.png %}){: style="max-width:60%"}

#### Criando mensagens da direita para a esquerda {#creating-right-to-left-messages}

A aparência final das mensagens da direita para a esquerda depende em grande parte de como os provedores de serviço as renderizam. Para práticas recomendadas sobre como criar mensagens da direita para a esquerda que sejam exibidas da forma mais precisa possível, consulte [Criando mensagens da direita para a esquerda]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages).

#### Criar fluxos de mensagens conversacionais (RCS) {#create-conversational-message-workflows-rcs}

Fluxos de mensagens conversacionais permitem responder dinamicamente aos usuários, criando uma experiência de mensagens de ida e volta. Para construir um fluxo, crie um Canvas e combine respostas sugeridas com [Jornadas de ação]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths) para direcionar seu fluxo com base na resposta que o usuário selecionar.

1. No construtor de Canvas, crie uma etapa de mensagem RCS com múltiplas respostas sugeridas.

![Criador de mensagem RCS com respostas sugeridas.]({% image_buster /assets/img/rcs/suggested_replies.png %})

{: start="2"}
2. Conecte essa mensagem a uma Jornada de ação com um grupo de ação para cada resposta sugerida.
3. Para cada grupo de ação:
   - Selecione o gatilho **Enviar uma mensagem SMS de entrada**.
   - Defina o corpo da mensagem para ser o mesmo da resposta sugerida correspondente.

![Etapa de Jornada de ação configurada com três grupos de ação, um para cada resposta sugerida.]({% image_buster /assets/img/rcs/quick_reply.png %})

{: start="4"}
4. Conecte cada grupo de ação a uma etapa de mensagem RCS e adicione conteúdo com base na resposta sugerida associada.
5. Continue o fluxo conversacional adicionando respostas sugeridas a quaisquer mensagens de acompanhamento.
6. Repita as etapas 2 a 4 até que o fluxo esteja completo.

![Canvas mostrando um fluxo conversacional com duas Jornadas de ação.]({% image_buster /assets/img/rcs/full_conversational_workflow.png %})

## Etapa 4: Pré-visualize e teste sua mensagem {#step-4-preview-and-test-your-message}

A Braze sempre recomenda pré-visualizar e testar sua mensagem antes de enviá-la. Alterne para a guia **Teste** para enviar um SMS, MMS ou RCS de teste para [grupos de teste de conteúdo]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#content-test-groups) ou usuários individuais, ou pré-visualize a mensagem como um usuário diretamente na Braze.

{% alert tip %}
Se você quiser testar em quantos segmentos seu SMS pode ser dividido, teste o comprimento do seu texto com a [calculadora de segmentos SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator#segment-calculator).
{% endalert %}

![Pré-visualização do texto SMS na guia Teste do criador. Na seção de perfil, o campo Nome está definido como "James". Na seção de pré-visualização, o SMS agora diz "Olá James, agradecemos seu apoio!"]({% image_buster /assets/img/sms_campaign_test.png %})

{% alert note %}
Para MMS, a ordenação dos ativos (imagem e corpo da mensagem) não pode ser personalizada. A ordenação depende do telefone que recebe a mensagem.
{% endalert %}

{% alert note %}
Como a renderização do RCS é controlada pelo sistema operacional do usuário, fabricante do dispositivo, operadora e app de mensagens (por exemplo, Google Messages vs. Apple Messages), a aparência da mensagem pode variar. A pré-visualização mostrada na Braze pode não corresponder exatamente ao que o usuário final recebe. Valide a renderização final em dispositivos reais sempre que possível. Para saber mais sobre a renderização do RCS em dispositivos iOS, consulte [Por que minha mensagem RCS não é renderizada corretamente em dispositivos iOS?]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/faqs#why-doesnt-my-rcs-message-render-accurately-on-ios-devices).
{% endalert %}

Para mais informações, consulte [Enviar mensagens de teste]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages/?tab=sms%2Fmms%20and%20rcs).

## Etapa 5: Construa o restante da sua campanha ou Canvas {#step-5-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab Campaign %}

Em seguida, construa o restante da sua campanha. Consulte as seções a seguir para mais detalhes sobre como usar melhor nossas ferramentas para criar sua mensagem.

### Escolha o agendamento ou gatilho de entrega {#choose-delivery-schedule-or-trigger}

As mensagens podem ser entregues com base em um horário agendado, uma ação ou um gatilho de API. Para saber mais, consulte [Agendando sua campanha]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign).

Para entrega baseada em ação, você também pode definir a duração da campanha e o [horário de silêncio]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours).

Nesta etapa, você também pode especificar controles de entrega, como permitir que os usuários se tornem [reelegíveis]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility#campaigns) para receber a campanha, ou ativar regras de [limite de frequência]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#frequency-capping).

### Escolha os usuários a direcionar {#choose-users-to-target}

Em seguida, [direcione os usuários]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users) escolhendo segmentos ou filtros para restringir seu público. Você já deve ter escolhido o grupo de inscrições, que restringe os usuários pelo nível ou categoria de comunicação que desejam ter com você.

{% multi_lang_include target_audiences.md %}

Selecione o público maior dos seus segmentos e restrinja ainda mais esse segmento com filtros opcionais. Você receberá automaticamente uma pré-visualização da população aproximada desse segmento. Tenha em mente que a composição exata do segmento é sempre calculada antes do envio da mensagem.

{% alert tip %}
Interessado em redirecionamento? Consulte [Redirecionamento de usuários]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/user_retargeting) para saber mais.
{% endalert %}

### Escolha eventos de conversão {#choose-conversion-events}

A Braze permite rastrear com que frequência os usuários realizam ações específicas, [eventos de conversão]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events), após receberem uma campanha. Você tem a opção de permitir uma janela de até 30 dias durante a qual uma conversão será contada se o usuário realizar a ação especificada.

Eventos de conversão ajudam a medir o sucesso da sua campanha. Por exemplo:

- Se você está usando geotargeting para disparar uma mensagem cujo objetivo final é o usuário fazer uma compra, defina o evento de conversão como `Purchase`.
- Se você está tentando direcionar o usuário para o seu app, defina o evento de conversão como `Starts Session`.

Você também pode definir eventos de conversão personalizados com base no seu caso de uso específico.

{% endtab %}
{% tab Canvas %}

Se ainda não o fez, conclua as seções restantes do seu componente de Canvas. Para mais detalhes sobre como construir o restante do seu Canvas, implementar testes multivariantes e Seleção inteligente, e mais, consulte a etapa [Construa seu Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-3-build-your-canvas) da nossa documentação de Canvas.

{% endtab %}
{% endtabs %}

## Etapa 6: Revise e implante {#step-6-review-and-deploy}

Depois de terminar de construir a última parte da sua campanha ou Canvas, revise seus detalhes, teste e envie!

Em seguida, confira [Relatórios de SMS, MMS e RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/reporting) para saber como acessar os resultados das suas campanhas.

## Perguntas frequentes {#frequently-asked-questions}

### Posso enviar mensagens de voz pré-gravadas com RCS? {#can-i-send-pre-recorded-voicemails-with-rcs}

Sim, você pode usar mensagens de mídia para suportar arquivos de áudio.