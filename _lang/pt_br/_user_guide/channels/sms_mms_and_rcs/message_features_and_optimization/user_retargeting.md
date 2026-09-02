---
nav_title: "Redirecionamento de usuários"
article_title: "Redirecionamento de usuários"
description: "Este artigo de referência aborda como os usuários podem redirecionar suas mensagens com base nas interações de SMS e RCS de um usuário."
page_type: reference
page_order: 4
alias: /sms_mms_rcs_user_retargeting/
tool:
  - Campaigns
channel:
  - SMS
  - MMS
  - RCS

---

# Redirecionamento de usuários {#user-retargeting}

> Além de alterar o estado de inscrição do usuário e enviar respostas automáticas com base em palavras-chave recebidas, a Braze também registra interações no perfil do usuário para filtragem e disparo de mensagens.<br><br>Esses filtros e gatilhos permitem filtrar ações com base em usuários que receberam ou responderam a Campaigns de SMS, MMS e RCS, ou engajar ainda mais com usuários que clicaram em URLs encurtadas.

{% alert tip %}
Para saber mais sobre palavras-chave personalizadas e como configurar o envio de mensagens bidirecional para aproveitar essas opções de redirecionamento, visite nosso artigo sobre [palavras-chave personalizadas]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/keyword_handling).
{% endalert %}

## Opções de redirecionamento {#retargeting-options}

{% alert note %}
Ao criar públicos com redirecionamento de usuários, você pode querer incluir ou excluir determinados usuários com base em suas preferências e para cumprir leis de privacidade, como o direito de "Não Vender ou Compartilhar" sob a CUP. Os profissionais de marketing devem implementar os filtros relevantes para a elegibilidade dos usuários nos critérios de entrada do Canvas e/ou da Campaign.
{% endalert %}

### Filtrar usuários por SMS, MMS e RCS {#filter-users-by-sms-mms-and-rcs}

Os usuários podem ser filtrados pela última vez que receberam um SMS, MMS ou RCS, ou se receberam um SMS, MMS ou RCS de uma Campaign específica. Os filtros podem ser definidos na etapa **Público-alvo** do criador de Campaigns.

{% alert note %}
Quando uma mensagem é recebida, aberta ou clicada, a Braze atualiza os dados de todos os perfis que compartilham o mesmo número de telefone do perfil que registrou a interação. Usuários que compartilham um número de telefone com alguém que recebeu, abriu ou clicou na mensagem podem corresponder a esse filtro mesmo que não estivessem originalmente na Campaign ou não tenham recebido a mensagem diretamente.
{% endalert %}

#### Filtrar por último SMS/MMS/RCS recebido {#filter-by-last-received-smsmmsrcs}

![Filtro de segmentação Último SMS recebido após 8 de dezembro de 2020.]({% image_buster /assets/img/sms/filter2.png %})

#### Filtrar por mensagens recebidas de uma Campaign de SMS/MMS/RCS {#filter-by-received-messages-from-smsmmsrcs-campaign}

Filtra usuários que receberam uma mensagem de uma Campaign específica. Com esse filtro, você também tem a opção de filtrar aqueles que não receberam mensagens de uma Campaign.

![Filtro de segmentação Recebeu mensagem da Campaign "SMS retargeting".]({% image_buster /assets/img/sms/filter1.png %})

### Disparar mensagens quando os usuários recebem SMS, MMS ou RCS {#trigger-messages}

Para disparar mensagens quando os usuários recebem mensagens de SMS, MMS ou RCS de uma Campaign específica, selecione **Interact with Campaign** como a ação-gatilho para uma Campaign baseada em ação. Em seguida, selecione **Receive SMS** e a Campaign de SMS, MMS ou RCS que você deseja usar.

![Para disparar mensagens quando os usuários recebem mensagens de SMS, MMS ou RCS de uma Campaign específica, selecione Interact with Campaign como a ação-gatilho para uma Campaign baseada em ação. Em seguida, selecione Receive SMS e a Campaign de SMS, MMS ou RCS que você deseja usar.]({% image_buster /assets/img/sms/trigger.png %})

### Filtrar por links de rastreamento avançado {#filter-by-advanced-tracking-links}

Redirecione usuários que clicaram em Campaigns com [links de rastreamento avançado]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/link_shortening).
Apenas Campaigns com rastreamento avançado ativado aparecem nos menus suspensos a seguir:

#### Redirecionar usuários que clicaram em uma Campaign específica de SMS, MMS ou RCS {#retarget-users-who-have-clicked-a-specific-sms-mms-or-rcs-campaign}

1. Crie um Segment usando o filtro **Clicked/Opened Campaign**.
2. Selecione **clicked shortened sms link**.
3. Escolha a Campaign desejada.

![Captura de tela relacionada ao redirecionamento de usuários que clicaram em uma Campaign específica de SMS, MMS ou RCS.]({% image_buster /assets/img/sms/retargeting5.png %})

#### Redirecionar usuários que clicaram em uma etapa específica do Canvas {#retarget-users-who-have-clicked-a-specific-canvas-step}

1. Crie um Segment usando o filtro **Clicked/Opened Step**.
2. Selecione **clicked shortened sms link**.
3. Escolha o Canvas e a etapa do Canvas desejados.

![Captura de tela relacionada ao redirecionamento de usuários que clicaram em uma etapa específica do Canvas.]({% image_buster /assets/img/keyword_example1.jpg %})

## Redirecionamento específico por categoria de palavra-chave {#keyword-category-specific-retargeting}

Além das três categorias padrão de palavras-chave (Opt-in, Descadastramento e Ajuda), você também pode criar até 25 categorias de palavras-chave próprias, permitindo identificar palavras-chave e respostas arbitrárias. Essas categorias podem ser usadas para filtragem e redirecionamento. Para saber mais sobre categorias globais de palavras-chave e como configurá-las, consulte [Processamento de palavras-chave]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing).

### Filtrar por recência {#filter-by-recency}

Filtre pela recência de um usuário respondendo ao seu programa de SMS, MMS ou RCS. Esse filtro avaliará a última data em que um usuário enviou uma mensagem de entrada que está dentro de uma das categorias de palavras-chave.

![Filtro de segmentação Último SMS enviado para o grupo de inscrições "Marketing SMS" com a palavra-chave "Opt-in" após 11 de agosto de 2020.]({% image_buster /assets/img/sms/retargeting1.png %})

### Filtrar por atribuição de Campaign ou Canvas {#filter-by-campaign-or-canvas-attribution}

Filtre por usuários que responderam a uma Campaign ou componente do Canvas específico de SMS, MMS ou RCS, categoria de palavra-chave ou tag.

#### Filtrar por resposta a uma Campaign específica com categoria de palavra-chave {#filter-by-replied-to-a-specific-campaign-with-keyword-category}

![Campaign com o filtro "Has replied to SMS" para a Campaign "SMS-283" "Promoção". Abaixo do filtro, o recurso menciona "Este filtro expirará 25 meses após a última mensagem ser enviada de 'Promoção' se não estiver sendo usado em nenhuma Campaign ativa."]({% image_buster /assets/img/sms/clicked_opened_campaign.png %})

#### Filtrar por resposta a uma Campaign ou Canvas com uma tag específica {#filter-by-replied-to-a-campaign-or-canvas-with-a-specific-tag}

![Campaign com o filtro "Has replied to SMS" para Campaign ou Canvas com a tag "Curbside Messaging Service C".]({% image_buster /assets/img/sms/clicked_opened_campaign_canvas_tag.png %})

#### Filtrar por resposta a uma etapa específica {#filter-by-replied-to-a-specific-step}

![Campaign com o filtro "Has replied to SMS" para a etapa "SMS Double Opt" "Step - Help".]({% image_buster /assets/img/sms/clicked_opened_step.png %})

### Disparar mensagens por palavra-chave {#trigger-messages-by-keyword}

As mensagens podem ser disparadas quando os usuários enviam mensagens de entrada com base em categorias de palavras-chave (o usuário enviou qualquer uma das palavras-chave) ou outras palavras-chave (o usuário enviou uma palavra-chave que não se enquadra em nenhuma das categorias existentes). Esses gatilhos são definidos na etapa de Entrega do criador de Campaigns.

Ao avaliar se uma mensagem de entrada corresponde a um evento de gatilho definido, os espaços iniciais e finais são removidos antes do início da avaliação.

{% alert tip %}
Se um Canvas baseado em ação for disparado por uma mensagem de entrada de SMS ou MMS, você pode referenciar [propriedades Liquid de SMS compatíveis]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags) em qualquer etapa do Canvas até a próxima jornada de ação.
{% endalert %}

#### Disparar por categoria de palavra-chave de entrada {#trigger-by-inbound-keyword-category}

![Campaign de SMS baseada em ação com o filtro de segmentação Enviou a palavra-chave "Opt-in" para o grupo de inscrições "Marketing SMS".]({% image_buster /assets/img/sms/retargeting2.png %}){: style="margin-top:10px;"}

#### Disparar por palavras-chave arbitrárias {#trigger-by-arbitrary-keywords}

Observe que, ao disparar uma mensagem com uma resposta de palavra-chave "Outra", você tem a oportunidade de avaliar o corpo da palavra-chave em uma correspondência exata de texto. Essa correspondência segue as mesmas regras mencionadas: apenas a **mensagem exata de uma única palavra** é processada (sem distinção entre _maiúsculas e minúsculas_). Uma palavra-chave enviada como `Hello Braze!` não corresponderia aos critérios mostrados no exemplo a seguir.

![Campaign de SMS baseada em ação com a categoria de palavra-chave como "Outra" onde o corpo da mensagem é exatamente "Hello" ou "Hey".]({% image_buster /assets/img/sms/retargeting3.png %}){: style="margin-top:10px;"}

#### Modelar palavras-chave {#template-keywords}

Ao disparar uma Campaign ou componente do Canvas com um SMS ou MMS de entrada, você pode opcionalmente modelar o texto ou anexos de mídia que o usuário enviou no corpo da sua Campaign ou Canvas com Liquid. Isso permite acessar a resposta do usuário, que você pode incluir na sua resposta, aplicar lógica condicional ou qualquer outra coisa que você possa fazer com Liquid.

{% raw %}

```liquid
Sorry, we didn't recognize {{sms.${inbound_message_body}}}. Text HELP for help or STOP to stop.
```

```liquid
{% if {{sms.${inbound_message_body}}} == "SNEAKERS" %}
OK, you're subscribed to updates on all our sneaker deals!
{% elsif {{sms.${inbound_message_body}}} == "SHIRTS" %}
Shirt deals coming up for you!
{% else %}
Want to receive a specific deal? Just text us the category you're interested in. For example SHIRTS or SNEAKERS.
{% endif %}
```

{% endraw %}

[16]: {% image_buster /assets/img/keyword_example1.jpg %}
[16]: {% image_buster /assets/img/sms/retargeting4.png %}