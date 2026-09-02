---
nav_title: Criar uma mensagem KakaoTalk
article_title: Criar uma mensagem KakaoTalk
description: "Este artigo de referência descreve como criar uma mensagem KakaoTalk."
page_order: 1
alias: /create_kakaotalk_message/
channel:
  - KakaoTalk
---

# Criar uma mensagem KakaoTalk {#create-a-kakaotalk-message}

> Use o [canal de envio de mensagens KakaoTalk]({{site.baseurl}}/kakaotalk) para alcançar usuários diretamente pela plataforma KakaoTalk. Crie uma experiência de usuário personalizada usando Liquid e outros conteúdos dinâmicos para construir um ambiente que promova e aprimore uma experiência rica com a sua marca.<br><br>Para configurar seu canal de envio de mensagens KakaoTalk, consulte [Configurar o KakaoTalk]({{site.baseurl}}/kakaotalk_setup).

## Etapa 1: Escolha onde criar sua mensagem {#step-1-choose-where-to-build-your-message}

O KakaoTalk é compatível com Campaigns e Canvas. Campaigns são mais adequadas para campanhas de mensagens únicas, enquanto Canvas permite orquestrar jornadas de usuários em várias etapas e canais.

{% tabs local %}
{% tab Campaign %}

1. Acesse **Messaging** > **Campaigns** e selecione **Create Campaign**.
2. Selecione **KakaoTalk** para uma campanha de canal único ou **Multichannel Campaign** para uma campanha multicanal.

![Painel com opções para selecionar o canal de envio de mensagens.]({% image_buster /assets/img/kakaotalk/kakaotalk_campaign.png %}){: style="max-width:30%" }

3. Você pode adicionar variantes adicionais à sua campanha, permitindo escolher diferentes tipos de mensagens e layouts. Para saber mais, consulte [Testes multivariantes e A/B]({{site.baseurl}}/user_guide/messaging/ab_testing).

{% endtab %}
{% tab Canvas %}

1. [Crie seu Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas).
2. Adicione uma etapa de mensagem no criador de Canvas e selecione **KakaoTalk**.

![Seleções de canal de envio de mensagens no Canvas.]({% image_buster /assets/img/kakaotalk/kakaotalk_canvas.png %})

{% endtab %}
{% endtabs %}

## Etapa 2: Crie sua mensagem do KakaoTalk {#step-2-compose-your-kakaotalk-message}

1. Selecione o menu suspenso **Canal do KakaoTalk**, que exibe uma lista de canais do KakaoTalk configurados por meio da página de parceiros de tecnologia, e selecione o canal do KakaoTalk a ser usado para enviar a mensagem.
2. Selecione o tipo de mensagem a ser enviada:
   - Texto
   - Imagem
       - Estreita
       - Ampla
   - Item de lista
   - Carrossel

{% tabs local %}
{% tab Texto %}

Uma mensagem de texto do KakaoTalk é a forma mais simples de comunicação: uma mensagem de texto padrão.

### Especificações {#specifications}

| Área | Especificações |
| --- | --- |
| Conteúdo | Conteúdo de texto, incluindo emojis e personalização com Liquid |
| Capacidade de texto | Até 1.000 caracteres |
| Botões | Até 5 botões opcionais. Atualmente, só podem ser usados para abrir uma URL ao clicar. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Especificações" }

![Uma mensagem de texto do KakaoTalk no criador.]({% image_buster /assets/img/kakaotalk/kakaotalk_text.png %})

{% endtab %}
{% tab Imagem %}

Uma imagem é uma mensagem que combina um elemento visual com texto de apoio. A Braze gerencia automaticamente o upload da imagem para os servidores do KakaoTalk.

### Especificações gerais {#general-specifications}

| Área | Especificações |
| --- | --- |
| Conteúdo | Uma imagem e texto de apoio |
| Formatos de arquivo aceitos | JPEG ou PNG |
| Largura recomendada | 500px |
| Tamanho do arquivo | Até 500kb |
| Proporção | Deve estar entre 2:1 (ampla) e 3:4 (alta) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Especificações gerais" }

Mensagens de imagem estreita e ampla possuem diferentes limites de caracteres e considerações de botões.

{% subtabs %}
{% subtab Imagem estreita %}

#### Imagem estreita {#narrow-image}

Uma mensagem de imagem estreita apresenta uma imagem ligeiramente mais alta e estreita, com opções mais extensas de texto e botões.

##### Especificações

| Área | Especificações |
| --- | --- |
| Conteúdo | Uma imagem e texto de apoio |
| Capacidade de texto | Até 500 caracteres |
| Botões | Até 5 botões opcionais |
| Origem da imagem | As imagens podem ser adicionadas usando a biblioteca de mídia da Braze ou uma URL direta |
| Personalização | Você pode especificar o comportamento ao clicar na imagem |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Especificações" }

![Uma mensagem estreita do KakaoTalk.]({% image_buster /assets/img/kakaotalk/narrow_image.png %})

{% endsubtab %}
{% subtab Imagem ampla %}

#### Imagem ampla {#wide-image}

Uma mensagem de imagem ampla apresenta uma imagem ampla em destaque, adequada para comunicação visual de alto impacto, com texto de apoio mínimo.

##### Especificações

| Área | Especificações |
| --- | --- |
| Conteúdo | Uma imagem e texto de apoio |
| Capacidade de texto | Até 76 caracteres |
| Botões | Até 2 botões opcionais |
| Origem da imagem | As imagens podem ser adicionadas usando a biblioteca de mídia da Braze ou uma URL direta |
| Personalização | Você pode especificar o comportamento ao clicar na imagem |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Especificações" }

![Uma mensagem ampla do KakaoTalk.]({% image_buster /assets/img/kakaotalk/wide_image.png %})

{% endsubtab %}
{% endsubtabs %}

### Adicionar imagens {#add-images}

Você pode adicionar imagens por meio da biblioteca de mídia da Braze ou colando uma URL que hospede um arquivo JPEG ou PNG. Também é possível especificar o comportamento ao clicar na imagem para redirecionar os usuários que clicarem nela para uma URL específica.

A Braze gerencia automaticamente todos os requisitos de upload de imagem do KakaoTalk, o que significa que você não precisa fazer upload de imagens para os provedores do KakaoTalk antes de enviar mensagens. Basta fazer upload das imagens e enviar a mensagem diretamente da Braze!

![Seção com ícones selecionados para adicionar imagem estreita.]({% image_buster /assets/img/kakaotalk/add_image.png %})

{% endtab %}
{% tab Item de lista %}


Uma mensagem de item de lista do KakaoTalk é projetada para apresentar uma lista de itens de conteúdo em um formato vertical e claro.

Mensagens de item de lista consistem em um cabeçalho, uma seção de lista de itens e uma área opcional de botões.

#### Especificações

| Área | Especificações |
| --- | --- |
| Quantidade de itens | Requer pelo menos 2 ou 3 itens |
| Cabeçalho | Até 250 caracteres |
| Título do item | Até 25 caracteres |
| URL do website (por item, toque na linha) | Obrigatória. Até 250 caracteres. Abre quando o usuário toca na imagem ou no título do item. |
| Botões (nível da mensagem) | Até 5 botões opcionais com suas próprias URLs ou ações |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Especificações" }

![Uma mensagem de item de lista do KakaoTalk.]({% image_buster /assets/img/kakaotalk/item_list.png %})

{% endtab %}
{% tab Carrossel %}

Uma mensagem de carrossel do KakaoTalk inclui até seis cartões roláveis. Cada cartão possui uma imagem, cabeçalho, mensagem, **URL do website** opcional e pelo menos um botão.

Tanto o cartão quanto seus botões usam um campo chamado **URL do website** no criador, mas se aplicam a diferentes alvos de toque:

- **URL do website do cartão:** (Opcional) Abre quando o usuário toca na imagem do cartão. Se você deixar em branco, a imagem não será tocável.
- **URL do website do botão:** Abre quando o usuário toca naquele botão. Cada botão web requer sua própria URL e pode apontar para um destino diferente da imagem do cartão.

As URLs do cartão e do botão são encurtadas e rastreadas de forma independente quando o rastreamento de cliques está ativado.

A Braze faz upload automaticamente das imagens do cartão para os servidores do KakaoTalk quando você envia a mensagem, de forma semelhante às mensagens de imagem.

{% alert note %}
O tipo de mensagem **Carrossel** pode não aparecer no seu espaço de trabalho até que seja ativado para a sua conta.
{% endalert %}

### Especificações

| Área | Especificações |
| --- | --- |
| Cartões | 2 a 6 cartões roláveis |
| Cabeçalho (por cartão) | Até 20 caracteres |
| Mensagem (por cartão) | Até 180 caracteres |
| Imagem (por cartão) | Obrigatória |
| Formatos de arquivo aceitos | JPG ou PNG |
| Largura mínima | 500px |
| Proporção | 2:1, 16:10, 3:2, 4:3, 1:1 ou 3:4 |
| URL do website (por cartão, toque na imagem) | (Opcional) Até 250 caracteres. Abre quando o usuário toca na imagem do cartão. |
| Botões (por cartão) | No mínimo 1, até 2 |
| Texto do botão (por cartão) | Até 8 caracteres |
| Tipos de botão | Abrir URL web, link do app ou resposta de texto |
| URL do website do botão (por botão **Abrir URL web**) | Obrigatória. Até 500 caracteres. Abre quando o usuário toca naquele botão. |
| Personalização | Liquid compatível nos campos do cartão e URLs |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Especificações" }

![Uma mensagem de carrossel do KakaoTalk.]({% image_buster /assets/img/kakaotalk/carousel_message.png %})

{% endtab %}
{% endtabs %}

## Etapa 3: Configurar o rastreamento de cliques {#step-3-set-up-click-tracking}

Quando o rastreamento de cliques do KakaoTalk está ativado, a Braze encurta automaticamente suas URLs, adiciona mecanismos de rastreamento e registra cliques em tempo real. Esses dados permitem que você crie estratégias de segmentação e redirecionamento mais direcionadas, como segmentar usuários com base no comportamento de clique e disparar mensagens em resposta a cliques específicos.

O rastreamento de cliques é compatível com mensagens de texto, imagem, item de lista e carrossel. Ele suporta links dentro de botões e ações de clique em imagens. Você também pode personalizar URLs usando Liquid e domínios personalizados.

Para ativar o rastreamento de cliques, marque **Click Tracking** na seção **Link options** do criador. As URLs são encurtadas usando o domínio padrão da Braze (`https://brz.ai`) ou o domínio personalizado especificado para o grupo de inscrições, e personalizadas para o usuário.

Para detalhes completos sobre rastreamento de cliques, domínios personalizados, personalização com Liquid em URLs, relatórios e redirecionamento, consulte [Rastreamento de cliques do KakaoTalk]({{site.baseurl}}/kakaotalk_click_tracking).

### Redirecionamento de usuários {#retargeting-users}

Você pode redirecionar usuários que clicaram em uma URL em uma mensagem do KakaoTalk usando os seguintes filtros de segmentação e disparadores:

- Disparadores baseados em ação
    - Interact with Campaign
    - Interact with Step

- Filtros de segmentação
    - Clicked/Opened Campaign
    - Clicked/Opened Campaign or Canvas with Tag
    - Clicked/Opened Step

## Etapa 4: Pré-visualize e teste sua mensagem do KakaoTalk {#step-4-preview-and-test-your-kakaotalk-message}

A prévia da mensagem é atualizada automaticamente conforme você compõe sua mensagem do KakaoTalk. Quando estiver pronto para testar, acesse a guia **Teste** para enviar uma mensagem de teste para grupos de teste de conteúdo ou usuários individuais, ou para pré-visualizar a mensagem como um usuário existente ou personalizado diretamente na Braze.

Após selecionar seus usuários de teste, selecione **Enviar teste**. Uma notificação indicará os resultados do seu envio de teste. Para a CJ OliveNetworks, você receberá uma resposta "C100". Se aparecer um erro diferente, consulte a [documentação do usuário do CJ KakaoTalk](https://developers.kakao.com/docs/latest/en/index).

![Janela de prévia de uma mensagem do KakaoTalk.]({% image_buster /assets/img/kakaotalk/preview_message.png %})

{% alert note %}
Para pré-visualizar e enviar uma mensagem de teste para um usuário existente, você precisa ter permissões de "Visualizar IPI". Você pode pré-visualizar e enviar uma mensagem de teste para um usuário personalizado sem essas permissões.
{% endalert %}

Para revisar os resultados de um envio ou solucionar problemas, acesse **Configurações** > **Registro de atividade de mensagens**. Para saber mais, consulte [Registro de atividade de mensagens]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log).

## Etapa 5: Crie o restante da sua campanha ou Canvas {#step-5-build-the-remainder-of-your-campaign-or-canvas}

Consulte as seções a seguir para saber como usar nossas ferramentas da melhor forma para criar mensagens do KakaoTalk.

### Escolha o cronograma de entrega ou o disparo {#choose-delivery-schedule-or-trigger}

As mensagens do KakaoTalk podem ser entregues com base em um horário agendado, uma ação ou um disparo de API or interface de programação do aplicativo (API). Para saber mais sobre opções de agendamento e disparo, consulte [Agendar sua campanha]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign) ou [Tipos de cronograma de entrada]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#entry-schedule-types) (para o seu Canvas).

Você pode especificar controles de entrega, como permitir que os usuários se tornem reelegíveis para receber a Campaign, ou ativar regras de limite de frequência. Para entrega baseada em ação, você também pode definir a duração da Campaign e o [horário de silêncio]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours).

{% alert important %}
O KakaoTalk aplica horário de silêncio de aproximadamente 20:50 a 08:00 no horário padrão da Coreia (KST). As mensagens agendadas durante essa janela não são enviadas até que o horário de silêncio termine. Essa restrição é aplicada pelos provedores de entrega do KakaoTalk (CJ OliveNetworks e Infobip) e se aplica a todos os tipos de mensagem do KakaoTalk, independentemente da configuração opcional de horário de silêncio da Braze.
{% endalert %}

### Escolha os usuários a serem direcionados {#choose-users-to-target}

Direcione os usuários selecionando Segments ou filtros para refinar seu público. Por enquanto, o KakaoTalk só pode enviar mensagens para amigos do canal. Recomendamos definir um atributo personalizado para indicar os amigos do canal, para que você possa segmentar seus usuários corretamente e evitar o envio de mensagens do KakaoTalk para usuários que não podem recebê-las.

### Escolha os eventos de conversão {#choose-conversion-events}

A Braze permite que você rastreie com que frequência os usuários realizam ações específicas, os eventos de conversão, após receberem uma Campaign. Você tem a opção de permitir uma janela de até 30 dias durante a qual uma conversão é contabilizada se o usuário realizar a ação especificada.

Os eventos de conversão ajudam a medir o sucesso da sua Campaign. Por exemplo, se você está tentando incentivar os usuários a usar seu app, defina o evento de conversão como **Starts Session**.

Você também pode definir eventos de conversão personalizados com base no seu caso de uso específico. Seja criativo e pense em como você deseja medir o sucesso da sua Campaign.

## Etapa 6: Revisar e implantar {#step-6-review-and-deploy}

Depois de terminar de criar a última parte da sua Campaign ou Canvas, revise os detalhes, teste e envie!