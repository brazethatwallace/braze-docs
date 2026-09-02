---
nav_title: Criação de cartões
article_title: Criação de cartões
alias: /card_creation/
description: "Este artigo descreve as diferenças entre a criação do cartão de conteúdo no lançamento da Campaign ou na entrada da etapa do Canvas versus na primeira impressão."
page_order: 0
tool: Campaigns
channel:
  - content cards
toc_headers: h2
---

# Criação de cartões {#card-creation}

> Você pode escolher quando a Braze avalia a elegibilidade do público e a personalização para novas Campaigns de Content Cards e etapas do Canvas, especificando quando o cartão é criado.

## Pré-requisitos {#prerequisites}

Para aproveitar esse recurso, você precisa fazer upgrade para as seguintes versões mínimas do SDK or kit de desenvolvimento de software:

{% sdk_min_versions swift:5.2.0 objc:4.5.0 android:23.0.0 web:4.2.0 %}

No iOS, o Swift SDK or kit de desenvolvimento de software oferece suporte a esse recurso a partir da versão 5.2.0, e o SDK or kit de desenvolvimento de software legado Objective-C oferece suporte a partir da versão 4.5.0. As versões 5.0.0 a 5.1.x do Swift SDK or kit de desenvolvimento de software não oferecem suporte.

Após fazer upgrade do SDK or kit de desenvolvimento de software, seus usuários de dispositivos móveis precisam atualizar o app. Você pode filtrar o público da sua Campaign ou Canvas para [direcionar apenas usuários nas versões mínimas do app]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/new_features#filtering-by-most-recent-app-versions).

## Visão geral {#overview}

{% tabs %}
{% tab Campaign %}

Você pode escolher quando a Braze cria um cartão na etapa **Delivery** ao criar uma nova [campanha de Content Card]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card) com entrega agendada.

![Seção de controles de Content Card ao editar a entrega de um Content Card agendado.]({% image_buster /assets/img_archive/card_creation.png %})

As seguintes opções estão disponíveis:

- **No lançamento da campanha:** O comportamento padrão anterior para Content Cards. A Braze calcula a elegibilidade do público e a personalização quando a campanha é lançada, depois cria o cartão e o armazena até que o usuário abra o app.
- **Na primeira impressão (recomendado):** Quando o usuário abre o app novamente (inicia uma nova [sessão](https://www.braze.com/resources/articles/whats-an-app-session-anyway)), a Braze determina quais Content Cards o usuário é elegível para receber, processa qualquer personalização como Liquid ou Connected Content, e então cria o cartão. Essa opção geralmente oferece melhor desempenho.

Independentemente da opção selecionada, a contagem regressiva da data de expiração do Content Card começa quando a campanha é lançada.

{% endtab %}
{% tab Canvas %}

Você pode escolher quando a Braze cria um cartão na guia **Messaging Channels** de uma [etapa de Mensagem]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step) de Content Card.

![Seção de controles de Content Card ao editar a entrega de um Content Card agendado.]({% image_buster /assets/img_archive/card_creation_canvas.png %})

As seguintes opções estão disponíveis:

- **Na entrada da etapa:** O comportamento padrão anterior para Content Cards. A Braze calcula a elegibilidade do público quando o usuário entra na etapa do Canvas, depois cria o cartão e o armazena até que o usuário abra o app.
- **Na primeira impressão (recomendado):** A Braze calcula a elegibilidade do público quando o usuário entra na etapa do Canvas. Quando o usuário abre o app novamente (inicia uma nova [sessão](https://www.braze.com/resources/articles/whats-an-app-session-anyway)), a Braze processa qualquer personalização como Liquid ou Connected Content, e então cria o cartão. Essa opção oferece melhor desempenho na entrega de cartões e uma personalização mais atualizada.

Independentemente da opção selecionada, a contagem regressiva da data de expiração do Content Card começa quando o usuário entra na etapa do Canvas.

{% alert tip %}
Se você quiser que usuários anônimos vejam um Content Card na primeira sessão, use uma Campaign em vez de um Canvas. Isso acontece porque, quando um usuário anônimo entra em um Canvas, a sessão já foi iniciada, então ele não receberá o Content Card até iniciar uma nova sessão.
{% endalert %}

### Evento de remoção {#removal-event}

Selecione a opção para remover Content Cards quando os usuários concluírem uma compra ou realizarem um evento personalizado. Para usar **Perform Custom Event** como o evento de remoção, selecione variáveis de contexto ou atributos personalizados para comparações ao usar filtros de propriedade.

![Configurações de evento de remoção de Content Card com Perform Custom Event selecionado e filtros de propriedade usando variáveis de contexto ou atributos personalizados.]({% image_buster /assets/img/content_card_removal_event.png %})

### Expiração {#expiration}

Nas configurações de **Expiration (Time in Feed)**, você pode selecionar **Personalize duration** para definir a expiração do Content Card usando variáveis de contexto.

![Configurações de expiração mostrando Personalize duration configurado com uma variável de contexto para a expiração do Content Card.]({% image_buster /assets/img/content_card_personalize_duration.png %})

{% alert important %}
Content Cards têm uma expiração máxima de 30 dias, mesmo quando se usa duração personalizada com variáveis de contexto. Qualquer valor definido acima de 30 dias será limitado a 30 dias. Para mais detalhes, consulte [Expiração do cartão]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card#card-expiration).
{% endalert %}

{% endtab %}
{% endtabs %}

{% alert note %}
Para ambas as opções, após um cartão ser criado, a Braze não recalcula a elegibilidade do público nem a personalização.
{% endalert %}

### Diferenças entre criar cartões no lançamento ou na entrada versus na primeira impressão {#differences}

Esta seção descreve as principais diferenças entre criar cartões no lançamento da campanha ou na entrada da etapa versus na primeira impressão.

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;}
.leftHeader{font-size: 12px; font-weight: bold; background-color: #f4f4f7; text-transform: uppercase; color: #212123; font-family: "Aribau Grotesk Bold", "Aribau Grotesk", "Aribau Grotesk Regular", Arial, Helvetica, sans-serif;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top}
</style>
<table aria-label="Diferenças entre criar cartões no lançamento ou na entrada versus na primeira impressão" class="tg">
  <caption>Diferenças entre criar cartões no lançamento ou na entrada versus na primeira impressão</caption>
<thead>
  <tr>
    <th class="tg-0pky"></th>
    <th class="tg-0pky">No lançamento da campanha / Na entrada da etapa do Canvas</th>
    <th class="tg-0pky">Na primeira impressão</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="leftHeader">Quando usar</td>
    <td class="tg-0pky">Se você precisar que o conteúdo seja capturado em um momento específico (o momento do lançamento).</td>
    <td class="tg-0pky"><ul><li>Se você precisar exibir cartões para usuários novos ou anônimos que possam entrar no Segment or segmento após o lançamento (<a href="#campaign_note">somente Campaigns*</a>).</li><li>Se estiver usando personalização e quiser que o conteúdo mais recente esteja disponível no cartão.</li></ul></td>
  </tr>
  <tr>
    <td class="leftHeader">Público</td>
    <td class="tg-0pky">A Braze avalia a participação no público quando a campanha é enviada.<br><br>Usuários novos ou anônimos não serão avaliados para elegibilidade se tentarem visualizar o cartão após o envio da campanha. Para Campaigns recorrentes, isso acontecerá no próximo intervalo de recorrência.</td>
    <td class="tg-0pky">A Braze avalia a participação quando o usuário abre o app novamente (inicia uma sessão, <a href="#campaign_note">somente Campaigns*</a>).<br><br> Essa configuração terá um alcance de público mais amplo, pois qualquer usuário novo ou anônimo sempre será avaliado para elegibilidade quando tentar visualizar o cartão. <br><br>Além disso, o limite de frequência (limitando o número de pessoas que receberão o cartão) não se aplica quando configurado para a primeira impressão.</td>
  </tr>
  <tr>
    <td class="leftHeader">Personalização</td>
    <td class="tg-0pky">A Braze avalia Liquid, Connected Content e Content Blocks no momento em que a campanha é lançada ou quando o usuário entra na etapa do Canvas. Para Campaigns recorrentes, isso acontecerá no próximo intervalo de recorrência.</td>
    <td class="tg-0pky">A Braze avalia Liquid, Connected Content e Content Blocks no momento da primeira impressão ou após o próximo intervalo de recorrência.</td>
  </tr>
  <tr>
    <td class="leftHeader">Análise de dados</td>
  <td class="tg-0pky"><em>Mensagens Enviadas</em> refere-se ao número de cartões que a Braze criou e disponibilizou. Isso não conta se os usuários visualizaram o cartão.</td>
  <td class="tg-0pky"><em>Mensagens Enviadas</em> refere-se ao número de cartões que a Braze envia a um usuário após o início de uma sessão. No Canvas, se um usuário entra na etapa sem iniciar uma sessão, a Braze não envia um cartão, então essa métrica pode não corresponder ao número de usuários que entram em uma etapa.<br><br>Embora os usuários contatáveis e as impressões não mudem, espere um volume de envio menor (<em>Mensagens Enviadas</em>) ao criar um cartão na primeira impressão em comparação com o lançamento da campanha ou a entrada na etapa do Canvas.</td>
  </tr>
  <tr>
    <td class="leftHeader">Tempo de processamento</td>
  <td class="tg-0pky">A Braze cria cartões para cada usuário elegível no Segment or segmento no momento do lançamento. Para públicos grandes, selecione <b>At First Impression</b> para que os cartões fiquem disponíveis mais rapidamente após o lançamento.</td>
  <td class="tg-0pky">A Braze cria um cartão na primeira vez que um usuário tenta visualizá-lo, então pode levar de 1 a 2 segundos para ser exibido na primeira impressão.</td>
  </tr>
</tbody>
</table>

<p id="campaign_note"><sup>* Este cenário se aplica apenas a Campaigns, pois o público do Canvas é avaliado na entrada do Canvas, não no nível da etapa.</sup></p>

## Considerações {#considerations}

### Campaigns multicanais {#multichannel-campaigns}

Campaigns multicanais não suportam cartões na primeira impressão, então todos os Content Cards são enviados no lançamento da campanha.

### Usar propriedades de contexto do Canvas {#using-canvas-context-properties}

Ao personalizar Content Cards com [propriedades de contexto do Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties), use a sintaxe `${...}` (por exemplo, {%raw%}`{{context.${property_name}}}`{%endraw%}). A notação de ponto sem essa sintaxe (por exemplo, {%raw%}`{{context.property_name}}`{%endraw%}) pode não resolver corretamente em Content Cards, mesmo que funcione em outros canais como push e e-mail.

### Alterar a criação de cartões após o lançamento {#changing-card-creation-after-launch}

A Braze recomenda não alterar a forma como os cartões são criados após o lançamento de uma campanha. Devido às diferenças na forma como Mensagens Enviadas é calculada entre os dois tipos de criação de cartões, alterar a criação dos cartões após o lançamento da campanha pode afetar a precisão do seu volume de envio.

### Tempo de processamento potencial {#potential-processing-time}

Para públicos grandes, selecione a opção de criar cartões na primeira impressão para que os cartões estejam disponíveis rapidamente após o lançamento. Campaigns disparadas no início da sessão também podem se beneficiar da mudança para criação na primeira impressão (disponível por meio de entrega agendada) para melhorar o desempenho.

Quando os cartões são criados na primeira impressão, pode levar alguns segundos para serem processados. A duração desse tempo de processamento depende de vários fatores, como o tamanho do cartão e a complexidade das opções de template da mensagem. Por exemplo, o tempo de processamento para cartões que usam Connected Content é pelo menos tão longo quanto o tempo de resposta do Connected Content.

### Versões anteriores do SDK or kit de desenvolvimento de software {#previous-sdk-versions}

Se o app de um usuário estiver rodando uma versão anterior do SDK or kit de desenvolvimento de software, ele ainda receberá os Content Cards que você enviar. No entanto, os cartões demoram mais para aparecer e podem não ser exibidos até a próxima sincronização de Content Cards.