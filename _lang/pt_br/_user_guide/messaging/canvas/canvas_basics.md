---
nav_title: Conceitos básicos do Canvas
article_title: Conceitos básicos do Canvas
page_order: 0
page_type: reference
description: "Este artigo de referência aborda os conceitos básicos do Canvas, cobrindo diversas perguntas que você deve se fazer ao configurar seu primeiro Canvas."
tool: Canvas

---

# Conceitos básicos do Canvas {#canvas-basics}

> Este artigo de referência aborda os conceitos básicos do Canvas, cobrindo diversas perguntas que você deve se fazer ao configurar seu primeiro Canvas. Também explicaremos os cinco Ws (o quê, quando, quem, por quê e onde) da visualização e como isso pode moldar e definir a forma como você constrói seu Canvas.

## Entendendo a estrutura do Canvas {#understanding-canvas-structure}

Antes de entrar nos detalhes mais específicos da [configuração do Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas), vamos identificar as partes principais que compõem um Canvas.

{% tabs %}
  {% tab Canvas %}
  O Canvas é uma interface unificada onde profissionais de marketing criam campanhas com múltiplas mensagens. É como uma ferramenta de programação visual, que permite construir uma jornada de usuário coesa a partir de uma série de etapas.

  ![Um exemplo de Canvas com uma etapa de divisão de decisão em duas jornadas de usuário diferentes, dependendo se o usuário tem push ativado.]({% image_buster /assets/img/canvas_intro/canvas_intro.gif %})

  {% endtab %}

  {% tab Jornada %}

  Uma jornada, ou comumente chamada de jornada do usuário, é a experiência individual de um usuário dentro do Canvas.<br><br> ![Um gráfico com a jornada do cliente para um novo usuário. Um usuário anônimo instala um app, Kat cria uma conta, Kat não abre o app por uma semana, uma notificação por push traz Kat de volta ao app, e então Kat usa o app regularmente.]({% image_buster /assets/img_archive/Journey_2.png %}){: style="max-width:90%;"}

  {% endtab %}

  {% tab Construtor do Canvas %}
  O construtor do Canvas mapeia as etapas a serem seguidas ao criar seu Canvas. Isso inclui itens básicos como nomear seu Canvas e adicionar equipes. Essencialmente, o construtor do Canvas é a configuração essencial necessária antes de começar a construir seu Canvas. Aqui, você pode controlar a forma como seus usuários iniciam e completam sua jornada do cliente com opções para editar o [cronograma de entrada]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-12-determine-your-canvas-entry-schedule), o [público-alvo]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-13-set-your-target-entry-audience) e as [configurações de envio]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-14-select-your-send-settings).<br><br> ![O construtor do Canvas na seção Básico para um Canvas chamado "New Canvas".]({% image_buster /assets/img_archive/canvas_flow_entry_wizard.png %}){: style="max-width:90%;"}

  {% endtab %}

  {% tab Variantes %}
  Uma variante é o caminho que cada cliente segue em sua jornada. O Canvas suporta até oito variantes com um grupo de controle. Você controla qual segmento do seu público seguirá cada variante.<br><br> ![Selecionando o botão "Adicionar variante".]({% image_buster /assets/img/canvas_intro/add_canvas_variant.gif %})

  {% endtab %}

  {% tab Etapas %}
  Uma etapa no Canvas é um ponto de decisão de marketing: "se isso, então aquilo." Aproveite os [componentes do Canvas]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components) para construir as etapas de uma jornada do usuário.<br><br> ![Exemplo de adição de uma etapa de postergação a um Canvas.]({% image_buster /assets/img/canvas_intro/add_canvas_step.gif %}) <br><br> Quando um usuário entra em um Canvas, ele começa na primeira etapa. Cada etapa tem condições que determinam se um usuário pode avançar para a próxima etapa. Dentro de uma etapa, você pode definir gatilhos ou agendar a entrega, refinar o direcionamento adicionando filtros ou marcando eventos de exceção, e especificar diferentes canais como notificações por push ou eventos de webhook. No Canvas, as etapas ocorrem em sequência, ou seja, a primeira etapa ocorre antes que a segunda possa acontecer. Digamos que temos um Canvas com as seguintes etapas: Etapa de postergação A com um atraso de 24 horas, Etapa de mensagem A com uma mensagem push e Etapa de mensagem B com uma mensagem no app. O Usuário A fica retido em uma postergação de 24 horas. Depois, após as 24 horas, ele receberá uma mensagem push e, em seguida, uma mensagem no app.

  {% endtab %}
{% endtabs %}

## Construindo a jornada do cliente {#building-the-customer-journey}

Usar os cinco Ws (o quê, quando, quem, por quê e onde) da visualização pode ajudar a identificar suas estratégias de engajamento do cliente e a criar uma jornada de mensagens personalizada para cada um dos seus usuários.

### O "quê": Nomeie seu Canvas {#the-what-name-your-canvas}

*O que você está tentando ajudar o usuário a fazer ou entender?*

Nunca subestime o poder do nome. A Braze foi construída para colaboração, então este é um bom momento para alinhar como você comunicará os objetivos com sua equipe.

Você pode adicionar tags e nomear as etapas e variantes em um Canvas. Para saber mais sobre jornadas do cliente, confira nosso curso do Braze Learning sobre [mapeamento de ciclos de vida do usuário](https://learning.braze.com/mapping-customer-lifecycles).

### O "por quê": Identifique eventos de conversão {#the-why-identify-conversion-events}

*Com base no "quê", por que você está construindo este Canvas?*

É sempre importante ter um objetivo definido em mente, e o Canvas ajuda você a entender como está se saindo em relação a KPIs como engajamento de sessão, compras e eventos personalizados.

Selecionar pelo menos um [evento de conversão]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events) dará a você a capacidade de entender como otimizar o desempenho dentro do Canvas. E se seu Canvas tiver múltiplas variantes ou um grupo de controle, a Braze usará o evento de conversão para determinar a melhor variação para atingir esse objetivo.

* **Iniciar sessão**: Quero que meus usuários voltem e interajam com o app.
* **Realizar compra**: Quero que meus usuários comprem.
* **Realizar evento personalizado**: Quero que meus usuários realizem uma ação específica que estou rastreando como um evento personalizado.
* **Fazer upgrade do app**: Quero que meus usuários atualizem a versão do app.

### O "quando": Crie condições de início {#the-when-create-starting-conditions}

*Quando um usuário iniciará essa experiência?*

Sua resposta determinará os detalhes de quando e como seu Canvas será entregue ao seu cliente. Os usuários podem entrar no seu Canvas de duas formas: por agendamento ou por gatilhos baseados em ação.

{% alert tip %}
Confira [Funcionalidades baseadas em tempo]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/delivery_and_entry_types) para Canvas para mais estratégias e respostas a perguntas comuns.
{% endalert %}

A entrega agendada permite que você envie um Canvas imediatamente para seu público-alvo. Você também pode configurá-lo para envio regular ou agendá-lo para um horário específico no futuro. Canvas baseados em ação respondem a comportamentos específicos do cliente conforme eles acontecem. Por exemplo, um gatilho baseado em ação pode incluir abrir um app, realizar uma compra, interagir com outra campanha ou acionar qualquer evento personalizado. No momento em que a ação ocorre, você pode fazer o Canvas enviar mensagens aos seus usuários.

### O "quem": Selecione um público {#the-who-select-an-audience}

*Quem você está tentando alcançar?*

Para definir seu "quem", você pode usar segmentos pré-definidos disponíveis no Canvas. Você também pode adicionar mais filtros para focar ainda mais na conexão com seu público-alvo. Após construir esses segmentos, apenas os usuários que correspondem aos critérios do público-alvo podem entrar na jornada do Canvas, levando a uma experiência mais personalizada. Veja esta tabela com os filtros disponíveis e como eles segmentam seus usuários para se adequar ao seu caso de uso.

| Filtro | Descrição |
|---------------------|-----------------------------------------------------------------------------------------------------|
| Dados personalizados | Segmente usuários com base em eventos e atributos que você define. Pode usar recursos específicos do seu produto. |
| Atividade do usuário | Segmente clientes com base em suas ações e compras. |
| Redirecionamento | Segmente clientes que receberam, visualizaram ou interagiram com Canvas anteriores. |
| Atividade de marketing | Segmente clientes com base em comportamentos universais, como o último engajamento. |
| Atributos do usuário | Segmente clientes por seus atributos e características constantes. |
| Atribuição da instalação | Segmente clientes pela primeira origem, grupo de anúncios, campanha ou anúncio. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="O 'quem': Selecione um público" }

### O "onde": Encontre meu público {#the-where-find-my-audience}

*Onde posso alcançar melhor meu público?*

É aqui que determinamos quais canais de envio de mensagens fazem mais sentido para a jornada do seu usuário. Idealmente, você quer alcançar seus usuários onde eles são mais acessíveis. Com isso em mente, você pode usar qualquer um dos seguintes canais com o Canvas:
* [E-mail]({{site.baseurl}}/user_guide/channels/email)
* [Push]({{site.baseurl}}/user_guide/channels/push)
* [Mensagens no app]({{site.baseurl}}/user_guide/channels/in_app_messages)
* [Content Cards]({{site.baseurl}}/user_guide/channels/content_cards)
* [SMS ou MMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs)
* [Webhook]({{site.baseurl}}/user_guide/channels/webhooks)

### O "como": Construa a experiência completa {#the-how-build-the-complete-experience}

*Como construo minha jornada no Canvas depois de identificar os cinco Ws?*

O "como" resume coletivamente como você criará seu Canvas e como alcançará seus usuários com sua mensagem. Por exemplo, para que uma mensagem seja eficaz, você deve otimizar o timing do envio de mensagens considerando os fusos horários dos seus diferentes usuários.

Responder ao "como" também determina a cadência de envio de um Canvas para seu público (como uma vez por semana ou quinzenalmente) e quais canais de envio de mensagens utilizar para cada Canvas que você construir, conforme descrito no "onde".

## Caso de uso: Fluxo de integração de clientes {#use-case-customer-onboarding-flow}

Por exemplo, digamos que você é um profissional de marketing da MovieCanon, uma empresa de serviços de streaming online, e está encarregado de criar um fluxo de integração para novos usuários do seu app. Referenciando os cinco Ws, podemos construir o Canvas da seguinte forma.

* **O quê**: O nome do nosso Canvas será "Nova Jornada de Integração".
* **Por quê**: O objetivo do nosso Canvas é dar boas-vindas aos nossos usuários e fazer com que continuem interagindo com o app.
* **Quando**: Depois que um usuário abrir o app pela primeira vez, queremos enviar um e-mail de boas-vindas.
* **Quem**: Estamos direcionando novos usuários que estão usando nosso app pela primeira vez.
* **Onde**: Temos confiança de que podemos alcançar novos usuários por e-mail, que é como fizemos todo o nosso envio de mensagens anteriormente.
* **Como**: Queremos definir uma postergação de um dia para não sobrecarregar nossos novos usuários com notificações. Após essa postergação, enviaremos um e-mail com uma lista dos filmes e séries mais populares para incentivá-los a continuar usando o app.

## Dicas gerais {#general-tips}

### Determine quando e como usar etapas e variantes {#determine-when-and-how-to-use-steps-and-variants}

Cada Canvas deve ter pelo menos uma variante e pelo menos uma etapa. A partir daí, o céu é o limite — então como você decide o formato do seu Canvas? É aqui que seus objetivos, dados e hipóteses entram em jogo. O brainstorm do "como" e "onde" ajudará você a mapear o formato e a estrutura corretos do seu Canvas.

### Trabalhe de trás para frente {#work-backwards}

Alguns objetivos têm sub-objetivos menores. Por exemplo, se você quer converter um usuário gratuito em assinante, pode precisar de uma página com seus serviços de inscrição detalhados. Um visitante pode precisar ver as opções antes de comprar. Você pode concentrar seus esforços de envio de mensagens em mostrar essa página antes de uma página de checkout. Trabalhar de trás para frente para entender a jornada que um cliente deve percorrer para chegar ao seu objetivo é fundamental para guiá-lo até a conversão.

### Diversifique suas mensagens {#mix-up-your-messaging}

Você já executou uma campanha semelhante no passado? Ou há uma em execução atualmente? Tente usar aquela mensagem e adicionar mais personalização a ela. Experimente um novo filtro ou adicione uma mensagem de acompanhamento. Conforme você diversifica suas técnicas de envio de mensagens, monitore seu desempenho e continue otimizando fazendo mudanças incrementais.