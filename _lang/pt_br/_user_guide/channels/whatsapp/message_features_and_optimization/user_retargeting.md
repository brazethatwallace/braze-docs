---
nav_title: Redirecionamento de usuários
article_title: Redirecionamento de usuários
page_order: 5
description: "Este artigo de referência aborda como os usuários podem redirecionar suas mensagens com base nas interações do WhatsApp."
page_type: reference
channel:
  - WhatsApp
---

# Redirecionamento de usuários {#user-retargeting}

> Além de alterar o estado de inscrição do usuário, a Braze também registra as interações no perfil de usuário para filtragem e disparo de mensagens.<br><br>Esses filtros e gatilhos permitem filtrar usuários que receberam mensagens do WhatsApp ou que receberam mensagens do WhatsApp de uma Campaign ou etapa do Canvas específica.

## Opções de redirecionamento {#retargeting-options}

{% alert note %}
Ao criar públicos com redirecionamento de usuários, você pode querer incluir ou excluir determinados usuários com base em suas preferências e para cumprir leis de privacidade, como o direito de "Não Vender ou Compartilhar" da CCPA. Os profissionais de marketing devem implementar os filtros relevantes para a elegibilidade dos usuários nos critérios de entrada do Canvas e/ou da Campaign.
{% endalert %}

### Filtrar usuários por WhatsApp {#filter-users-by-whatsapp}

Os usuários podem ser filtrados pela última vez que receberam uma mensagem do WhatsApp ou se receberam uma mensagem do WhatsApp de uma Campaign específica do WhatsApp. Os filtros podem ser definidos na etapa Usuários-alvo do criador de campaigns.

#### Filtrar pela última mensagem do WhatsApp recebida {#filter-by-last-received-whatsapp}

![Filtro para última mensagem do WhatsApp recebida em 22 de abril de 2025.]({% image_buster /assets/img/whatsapp/whatsapp23.png %}){: style="max-width:75%"}

#### Filtrar por mensagens recebidas de uma Campaign do WhatsApp {#filter-by-received-messages-from-whatsapp-campaign}

Filtra usuários que receberam uma mensagem de uma Campaign específica do WhatsApp. Com esse filtro, você também tem a opção de filtrar aqueles que não receberam mensagens de uma Campaign do WhatsApp.

{% alert note %}
Quando uma mensagem do WhatsApp é entregue, aberta ou clicada, a Braze atualiza os dados de todos os perfis que compartilham o mesmo número de telefone do perfil que registrou a interação. Portanto, usuários que compartilham esse número com alguém que recebeu, abriu ou clicou na mensagem podem corresponder aos filtros de "recebeu", mesmo que não tenham recebido a mensagem diretamente.
{% endalert %}

![Filtro para recebimento de uma Campaign do WhatsApp.]({% image_buster /assets/img/whatsapp/whatsapp22.png %}){: style="max-width:75%"}

### Filtrar por engajamento {#filter-by-engagement}

Redirecione usuários que leram ou não leram uma Campaign ou etapa do Canvas do WhatsApp.

#### Redirecionar usuários que abriram/leram uma Campaign específica do WhatsApp {#retarget-users-who-have-openedread-a-specific-whatsapp-campaign}

1. Crie um Segment or segmento usando o filtro **Clicked/Opened Campaign**.
2. Selecione **read WhatsApp message**.
3. Escolha a Campaign desejada.

![Filtro para ter lido uma mensagem do WhatsApp.]({% image_buster /assets/img/whatsapp/whatsapp21.png %}){: style="max-width:75%"}

#### Redirecionar usuários que abriram/leram uma etapa específica do Canvas {#retarget-users-who-have-openedread-a-specific-canvas-step}

1. Crie um Segment or segmento usando o filtro **Clicked/Opened Step**.
2. Selecione **read WhatsApp message**.
3. Escolha o Canvas e as etapas do Canvas desejados.

![Filtro para leitura de uma etapa do WhatsApp.]({% image_buster /assets/img/whatsapp/whatsapp20.png %}){: style="max-width:75%"}

#### Filtrar por atribuição de Campaign ou Canvas {#filter-by-campaign-or-canvas-attribution}

Filtre usuários que abriram/leram uma Campaign ou componente do Canvas ou tag específica do WhatsApp.

![Filtro para abertura de uma mensagem específica do WhatsApp.]({% image_buster /assets/img/whatsapp/whatsapp19.png %}){: style="max-width:75%"}