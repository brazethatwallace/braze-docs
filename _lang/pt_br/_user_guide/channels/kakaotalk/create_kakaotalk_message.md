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

> Use o [canal de envio de mensagens KakaoTalk]({{site.baseurl}}/kakaotalk/) para alcançar usuários diretamente pela plataforma KakaoTalk. Crie uma experiência de usuário personalizada usando Liquid e outros conteúdos dinâmicos para construir um ambiente que promova e aprimore uma experiência rica com a sua marca.<br><br>Para configurar seu canal de envio de mensagens KakaoTalk, consulte [Configurar o KakaoTalk]({{site.baseurl}}/kakaotalk_setup/).

## Etapa 1: Escolha onde criar sua mensagem {#step-1-choose-where-to-build-your-message}

O KakaoTalk é compatível com Campaigns e Canvas. Campaigns são mais adequadas para campanhas de mensagens únicas, enquanto Canvas permite orquestrar jornadas de usuário em várias etapas e canais.

{% tabs local %}
{% tab Campaign %}

1. Acesse **Messaging** > **Campaigns** e selecione **Create Campaign**.
2. Selecione **KakaoTalk** para uma campanha de canal único, ou **Multichannel Campaign** para uma campanha multicanal.

![Painel com opções para selecionar o canal de envio de mensagens.]({% image_buster /assets/img/kakaotalk/kakaotalk_campaign.png %}){: style="max-width:30%" }

3. Você pode adicionar variantes adicionais à sua campanha, permitindo escolher diferentes tipos de mensagem e layouts. Para saber mais, consulte [Testes multivariantes e A/B](https://www.braze.com/docs/user_guide/messaging/ab_testing/).

{% endtab %}
{% tab Canvas %}

1. [Crie seu Canvas](https://www.braze.com/docs/user_guide/messaging/canvas/create_a_canvas/).
2. Adicione uma etapa de mensagem no criador de Canvas e selecione **KakaoTalk**.

![Seleções de canal de envio de mensagens no Canvas.]({% image_buster /assets/img/kakaotalk/kakaotalk_canvas.png %})

{% endtab %}
{% endtabs %}

## Etapa 2: Componha sua mensagem KakaoTalk {#step-2-compose-your-kakaotalk-message}

1. Selecione o menu suspenso **KakaoTalk channel**, que exibe uma lista de canais KakaoTalk configurados pela página de Parceiros de tecnologia, e selecione o canal KakaoTalk a ser usado para enviar a mensagem.
2. Selecione o tipo de mensagem a enviar:
- Texto
- Imagem
- Item de lista
    - Estreito
    - Largo

![Seção de variantes do KakaoTalk com três tipos de mensagens para selecionar.]({% image_buster /assets/img/kakaotalk/kakaotalk_variants.png %})

{% tabs local %}
{% tab Texto %}

Uma mensagem de texto KakaoTalk é a forma mais simples de comunicação: uma mensagem de texto padrão.

### Especificações {#specifications}

| Área | Especificações |
| --- | --- |
| Conteúdo | Conteúdo de texto, incluindo emojis e personalização com Liquid |
| Capacidade de texto | Até 1.000 caracteres |
| Botões | Até 5 botões opcionais. Atualmente, só podem ser usados para abrir uma URL ao clicar. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Specifications" }

![Uma mensagem de texto KakaoTalk no criador.]({% image_buster /assets/img/kakaotalk/kakaotalk_text.png %})

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
| Proporção | Deve estar entre 2:1 (largo) e 3:4 (alto) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="General specifications" }

Mensagens de imagem estreita e larga possuem diferentes limites de caracteres e considerações de botões.

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
| Origem da imagem | As imagens podem ser adicionadas usando a Biblioteca de mídia da Braze ou uma URL direta |
| Personalização | Você pode especificar o comportamento ao clicar na imagem |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Specifications" }

![Uma mensagem estreita do KakaoTalk.]({% image_buster /assets/img/kakaotalk/narrow_image.png %})

{% endsubtab %}
{% subtab Imagem larga %}

#### Imagem larga {#wide-image}

Uma mensagem de imagem larga apresenta uma imagem larga em destaque, adequada para comunicação visual de alto impacto, com texto de apoio mínimo.

##### Especificações

| Área | Especificações |
| --- | --- |
| Conteúdo | Uma imagem e texto de apoio |
| Capacidade de texto | Até 76 caracteres |
| Botões | Até 2 botões opcionais |
| Origem da imagem | As imagens podem ser adicionadas usando a Biblioteca de mídia da Braze ou uma URL direta |
| Personalização | Você pode especificar o comportamento ao clicar na imagem |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Specifications" }

![Uma mensagem larga do KakaoTalk.]({% image_buster /assets/img/kakaotalk/wide_image.png %})

{% endsubtab %}
{% endsubtabs %}

### Adicionar imagens {#add-images}

Você pode adicionar imagens pela Biblioteca de mídia da Braze ou colando uma URL que hospede um arquivo JPEG ou PNG. Também é possível especificar o comportamento ao clicar na imagem para redirecionar os usuários que clicarem para uma URL específica.

A Braze gerencia automaticamente todos os requisitos de upload de imagem do KakaoTalk, o que significa que você **não precisa** fazer upload de imagens para provedores do KakaoTalk antes de enviar mensagens. Basta fazer upload das imagens e enviar a mensagem diretamente pela Braze!

![Seção com ícones selecionados para adicionar imagem estreita.]({% image_buster /assets/img/kakaotalk/add_image.png %})

{% endtab %}
{% tab Item de lista %}


Uma mensagem de lista de itens do KakaoTalk é projetada para apresentar uma lista de itens de conteúdo em um formato vertical e claro.

Mensagens de item de lista consistem em um cabeçalho, uma seção de lista de itens e uma área opcional de botões.

#### Especificações

| Área | Especificações |
| --- | --- |
| Quantidade de itens | Requer no mínimo 2 ou 3 itens |
| Botões | Até 5 botões opcionais |
| Cabeçalho | Até 250 caracteres |
| Título do item | Até 25 caracteres |
| URL do site (por item) | Até 250 caracteres |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Specifications" }

![Uma mensagem de item de lista do KakaoTalk.]({% image_buster /assets/img/kakaotalk/item_list.png %})

{% endtab %}
{% endtabs %}


## Etapa 3: Configure o rastreamento de cliques {#step-3-set-up-click-tracking}

Quando o rastreamento de cliques do KakaoTalk está ativado, a Braze encurta automaticamente suas URLs, adiciona mecanismos de rastreamento e registra cliques em tempo real. Esses dados permitem criar estratégias de segmentação e redirecionamento mais direcionadas, como segmentar usuários com base no comportamento de cliques e disparar mensagens em resposta a cliques específicos.

O rastreamento de cliques é compatível com mensagens de texto, imagem e item de lista. Ele suporta links dentro de botões e ações de clique em imagens. Você também pode personalizar URLs usando Liquid e domínios personalizados.

Para ativar o rastreamento de cliques, marque **Click Tracking** na seção **Link options** do criador. As URLs serão encurtadas usando o domínio padrão da Braze (`https://brz.ai`) ou o domínio personalizado especificado para o grupo de inscrições, e personalizadas para o usuário.

Para detalhes completos sobre rastreamento de cliques, domínios personalizados, personalização com Liquid em URLs, relatórios e redirecionamento, consulte [Rastreamento de cliques do KakaoTalk]({{site.baseurl}}/kakaotalk_click_tracking/).

### Redirecionar usuários {#retargeting-users}

Você pode redirecionar usuários que clicaram em uma URL em uma mensagem KakaoTalk usando os seguintes filtros de segmentação e gatilhos:

- Gatilhos baseados em ação
    - Interagir com Campaign
    - Interagir com etapa

- Filtros de segmentação
    - Clicou/Abriu Campaign
    - Clicou/Abriu Campaign ou Canvas com tag
    - Clicou/Abriu etapa

## Etapa 4: Pré-visualize e teste sua mensagem KakaoTalk {#step-4-preview-and-test-your-kakaotalk-message}

A pré-visualização da mensagem é atualizada automaticamente conforme você compõe sua mensagem KakaoTalk. Quando estiver pronto para testar, acesse a guia **Test** para enviar uma mensagem de teste para grupos de teste de conteúdo ou usuários individuais, ou para pré-visualizar a mensagem como um usuário existente ou personalizado diretamente na Braze.

Após selecionar seus usuários de teste, selecione **Send Test**. Uma notificação indicará os resultados do seu envio de teste. Para CJ OliveNetworks, você receberá uma resposta "C100". Se aparecer um erro diferente, consulte a [documentação de usuário do CJ KakaoTalk](https://developers.kakao.com/docs/latest/en/index).

![Janela de pré-visualização de uma mensagem KakaoTalk.]({% image_buster /assets/img/kakaotalk/preview_message.png %})

{% alert note %}
Para pré-visualizar e enviar uma mensagem de teste para um usuário existente, você precisa ter permissões de "View PII". Você pode pré-visualizar e enviar uma mensagem de teste para um usuário personalizado sem essas permissões.
{% endalert %}

Para revisar os resultados de um envio ou solucionar problemas, acesse **Settings** > **Message Activity Log**. Para saber mais, consulte [Registro de atividades de envio de mensagem]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log/).

## Etapa 5: Construa o restante da sua campanha ou Canvas {#step-5-build-the-remainder-of-your-campaign-or-canvas}

Consulte as seções a seguir para detalhes sobre como usar melhor nossas ferramentas para criar mensagens KakaoTalk.

### Escolha o cronograma de entrega ou gatilho {#choose-delivery-schedule-or-trigger}

Mensagens KakaoTalk podem ser entregues com base em um horário agendado, uma ação ou um gatilho de API. Para saber mais sobre opções de agendamento e gatilhos, consulte [Agendar sua campanha]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/) ou [Tipos de cronograma de entrada]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/#entry-schedule-types) (para seu Canvas).

Você pode especificar controles de entrega, como permitir que os usuários se tornem elegíveis novamente para receber a campanha, ou ativar regras do limite de frequência. Para entrega baseada em ação, você também pode definir a duração da campanha e o [horário de silêncio]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours/).

### Escolha os usuários a direcionar {#choose-users-to-target}

Direcione usuários selecionando segmentos ou filtros para refinar seu público. Por enquanto, o KakaoTalk só pode enviar mensagens para amigos do canal. Recomendamos definir um atributo personalizado para indicar amigos do canal, para que você possa segmentar seus usuários adequadamente e evitar o envio de mensagens KakaoTalk para usuários que não podem recebê-las.

### Escolha eventos de conversão {#choose-conversion-events}

A Braze permite rastrear com que frequência os usuários realizam ações específicas (eventos de conversão) após receberem uma campanha. Você tem a opção de permitir um período de até 30 dias durante o qual uma conversão é contabilizada se o usuário realizar a ação especificada.

Eventos de conversão ajudam a medir o sucesso da sua campanha. Por exemplo, se você está tentando incentivar os usuários a usar seu app, defina o evento de conversão como **Starts Session**.

Você também pode definir eventos de conversão personalizados com base no seu caso de uso específico. Seja criativo e pense em como deseja medir o sucesso da sua campanha.

## Etapa 6: Revise e implante {#step-6-review-and-deploy}

Depois de terminar de construir sua campanha ou Canvas, revise os detalhes, teste e envie!