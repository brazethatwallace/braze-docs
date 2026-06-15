---
nav_title: Campaign Connector
article_title: Campaign Connector
page_order: 2
tool: Campaigns
page_type: tutorial
description: "Este artigo explica o que é o Campaign Connector e como usá-lo para entregar conteúdo direcionado e relevante no momento certo."

---
# Campaign Connector

> O Campaign Connector permite criar campanhas que são disparadas quando os usuários interagem com campanhas ativas. Você pode entregar conteúdo direcionado e relevante no momento certo.

## Como funciona

Esse recurso permite direcionar usuários que realizam as seguintes interações com campanhas ativas:

- Visualizar mensagem no app
- Clicar em mensagem no app
- Clicar em botões de mensagem no app
- Clicar em e-mail
- Clicar em alias no e-mail
- Abrir e-mail
- Abrir diretamente notificação por push
- Clicar em botão de notificação por push
- Clicar em página de story por push
- Realizar evento de conversão
- Receber e-mail
- Receber SMS
- Clicar em link encurtado de SMS
- Receber notificação por push
- Receber webhook
- Ser inscrito em um grupo de controle
- Visualizar cartão de conteúdo
- Clicar em cartão de conteúdo
- Dispensar cartão de conteúdo

{% alert important %}
Os gatilhos do Campaign Connector não podem ser usados para disparar campanhas de mensagens no app. Mensagens no app só podem ser disparadas por eventos do SDK, como eventos personalizados ou início de sessão. Para saber mais, consulte [Criar uma mensagem no app]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional/).
{% endalert %}

### Regras de entrega

Note que você não pode usar o Campaign Connector para enviar uma mensagem a um usuário após ele ter concluído uma interação com uma campanha. Por exemplo, se você está executando uma campanha de marketing por nove semanas e configura uma campanha de acompanhamento usando o Campaign Connector no início da quarta semana, a campanha de acompanhamento só entregará mensagens aos usuários que interagiram com a campanha de marketing após a publicação da campanha de acompanhamento (semanas 4 a 9). Portanto, para garantir que suas campanhas de acompanhamento alcancem todos os usuários que você está direcionando, você deve:

- Configurar sua campanha original como rascunho
- Configurar e publicar sua campanha de acompanhamento
- Publicar a campanha original

Essas regras de entrega são particularmente importantes se você está direcionando usuários que estão inscritos em um grupo de controle, recebem um e-mail ou recebem uma notificação por push. Como os usuários serão inscritos no grupo de controle assim que você publicar a campanha original, você deve publicar a campanha de acompanhamento antes de publicar a campanha original. Da mesma forma, se você publicar a campanha original antes da campanha de acompanhamento, muitos usuários poderão receber seu e-mail e/ou notificação por push antes que a campanha de acompanhamento seja publicada.

## Usando o Campaign Connector com suas campanhas

### Etapa 1: Criar uma nova campanha

Redija as mensagens que deseja enviar aos seus usuários. Você pode selecionar uma campanha de canal individual ou campanha multicanais, dependendo do seu caso de uso.

### Etapa 2: Selecionar a interação e a campanha-alvo

1. Selecione [Entrega baseada em ação]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/) e adicione o gatilho "Interagir com campanha" para direcionar usuários que interagem com uma campanha ativa. 
2. Escolha a interação de gatilho. 
3. Em seguida, selecione a campanha ativa que você deseja direcionar.

![]({% image_buster /assets/img_archive/Campaign_Connector1.png %})

### Etapa 3: Definir a postergação do agendamento e adicionar exceções (opcional)

Se você optar por definir uma postergação do agendamento, poderá adicionar uma exceção à ação-gatilho. Por exemplo, você pode querer reenviar uma campanha de e-mail para usuários que não abriram o e-mail original. Nesse cenário, você pode escolher "Recebeu e-mail" como gatilho e definir uma postergação de agendamento de uma semana. Depois, adicione "Abrir e-mail" como exceção. Agora, você reenviará o e-mail para os usuários que não abriram o e-mail original dentro de uma semana após recebê-lo.

![]({% image_buster /assets/img_archive/Campaign_Connector3.png %})

Os eventos de exceção só serão disparados enquanto o usuário estiver aguardando para receber a mensagem associada. Se o usuário realizar a ação antes de aguardar a mensagem, o evento de exceção não será disparado.

### Etapa 4: Continuar com a criação da campanha

Continue criando sua campanha normalmente. Se você quiser garantir que enviará uma mensagem a todos os usuários que vão interagir com uma campanha específica, o ideal é direcionar um segmento que contenha todos os usuários do seu app.

## Casos de uso

Você pode usar o Campaign Connector para direcionar usuários que interagem ou não interagem com campanhas ativas.

Por exemplo, você pode escolher direcionar usuários que clicaram em uma mensagem push promocional sobre frete grátis para enviar a eles uma mensagem push promocional oferecendo 15% de desconto em uma compra.

O Campaign Connector também pode direcionar usuários que recebem uma notificação por push lembrando que abandonaram o carrinho. Por exemplo, você pode querer reenviar a notificação para usuários que não a abriram diretamente. No entanto, provavelmente você vai querer excluir usuários que fizeram uma compra desde o envio da notificação original, mesmo que não a tenham aberto diretamente. Você pode alcançar esse caso de uso adicionando um gatilho "Recebeu notificação por push" para a campanha "Carrinho Abandonado", definindo uma postergação de agendamento e adicionando "Realiza compra" e "Abriu diretamente notificações por push" como exceções.