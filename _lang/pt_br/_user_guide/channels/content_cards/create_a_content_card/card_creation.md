---
nav_title: Criação de cartões
article_title: Criação de cartões
alias: /card_creation/
description: "Este artigo descreve as diferenças entre a criação do cartão de conteúdo no lançamento da campanha ou na entrada da etapa do Canvas versus na primeira impressão."
page_order: 0
tool: Campaigns
channel:
  - content cards
toc_headers: h2
---

# Criação de cartões {#card-creation}

> Você pode escolher quando a Braze avalia a elegibilidade do público e a personalização para novas campanhas de cartão de conteúdo e etapas do Canvas, especificando quando o cartão é criado.

## Pré-requisitos {#prerequisites}

Para aproveitar esse recurso, você deve fazer upgrade para as seguintes versões mínimas do SDK:

{% sdk_min_versions swift:5.2.0 android:23.0.0 web:4.2.0 %}

Após fazer upgrade do SDK, os usuários de dispositivos móveis precisam atualizar o app. Você pode filtrar o público da sua campanha ou Canvas para [direcionar apenas usuários nessas versões mínimas do app]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions).

## Visão geral {#overview}

{% tabs %}
{% tab Campaign %}

Você pode escolher quando a Braze cria um cartão na etapa **Entrega** ao criar uma nova [campanha de cartão de conteúdo]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card/) com entrega agendada.

![Seção de controles do cartão de conteúdo ao editar a entrega de um cartão de conteúdo agendado.]({% image_buster /assets/img_archive/card_creation.png %})

As seguintes opções estão disponíveis:

- **No lançamento da campanha:** O comportamento padrão anterior para Content Cards. A Braze calcula a elegibilidade do público e a personalização quando a campanha é lançada, depois cria o cartão e o armazena até que o usuário abra o app.
- **Na primeira impressão (recomendado):** Quando o usuário abrir o app novamente (iniciar uma nova [sessão](https://www.braze.com/resources/articles/whats-an-app-session-anyway)), a Braze determina para quais Content Cards o usuário é elegível, processa qualquer personalização como Liquid ou Conteúdo conectado e então cria o cartão. Essa opção geralmente oferece melhor desempenho.

Independentemente da opção selecionada, a contagem regressiva da data de expiração do cartão de conteúdo começa quando a campanha é lançada.

{% endtab %}
{% tab Canvas %}

Você pode escolher quando a Braze cria um cartão na guia **Canais de envio de mensagens** de uma etapa de [Mensagem]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step/) do cartão de conteúdo.

![Seção de controles do cartão de conteúdo ao editar a entrega de um cartão de conteúdo agendado.]({% image_buster /assets/img_archive/card_creation_canvas.png %})

As seguintes opções estão disponíveis:

- **Na entrada da etapa:** O comportamento padrão anterior para Content Cards. A Braze calcula a elegibilidade do público quando o usuário entra na etapa do Canvas, depois cria o cartão e o armazena até que o usuário abra o app.
- **Na primeira impressão (recomendado):** A Braze calcula a elegibilidade do público quando o usuário entra na etapa do Canvas. Quando o usuário abrir o app novamente (iniciar uma nova [sessão](https://www.braze.com/resources/articles/whats-an-app-session-anyway)), a Braze processa qualquer personalização como Liquid ou Conteúdo conectado e então cria o cartão. Essa opção oferece melhor desempenho na entrega de cartões e personalização mais atualizada.

Independentemente da opção selecionada, a contagem regressiva da data de expiração do cartão de conteúdo começa quando o usuário entra na etapa do Canvas.

{% alert tip %}
Se você quiser que usuários anônimos vejam um cartão de conteúdo na primeira sessão, use uma campanha em vez de um Canvas. Isso porque, quando um usuário anônimo entra em um Canvas, a sessão já foi iniciada, então ele não receberá o cartão de conteúdo até iniciar uma nova sessão.
{% endalert %}

### Evento de remoção {#removal-event}

Selecione a opção para remover Content Cards quando os usuários concluírem uma compra ou realizarem um evento personalizado. Para usar **Realizar evento personalizado** como evento de remoção, selecione variáveis de contexto ou atributos personalizados para comparações ao usar filtros de propriedade.

![Configurações de evento de remoção do cartão de conteúdo com Realizar evento personalizado selecionado e filtros de propriedade usando variáveis de contexto ou atributos personalizados.]({% image_buster /assets/img/content_card_removal_event.png %})

### Expiração {#expiration}

Nas configurações de **Expiração (Tempo no feed)**, você pode selecionar **Personalizar duração** para definir a expiração do cartão de conteúdo usando variáveis de contexto.

![Configurações de expiração mostrando Personalizar duração configurada com uma variável de contexto para expiração do cartão de conteúdo.]({% image_buster /assets/img/content_card_personalize_duration.png %})

{% endtab %}
{% endtabs %}

{% alert note %}
Para ambas as opções, após a criação de um cartão, a Braze não recalcula a elegibilidade do público nem a personalização.
{% endalert %}

### Diferenças entre criar cartões no lançamento ou na entrada versus na primeira impressão {#differences}

Esta seção descreve as principais diferenças entre a criação de cartões no lançamento da campanha ou na entrada da etapa versus na primeira impressão.

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;}
.leftHeader{font-size: 12px; font-weight: bold; background-color: #f4f4f7; text-transform: uppercase; color: #212123; font-family: "Sailec W00 Bold",Arial,Helvetica,sans-serif;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top}
</style>
<table class="tg">
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
    <td class="tg-0pky">Se você precisa que o conteúdo seja capturado em um momento específico (o momento do lançamento).</td>
    <td class="tg-0pky"><ul><li>Se você precisa exibir cartões para usuários novos ou anônimos que podem entrar no segmento após o lançamento (<a href="#campaign_note">somente campanhas*</a>).</li><li>Se você está usando personalização e quer que o conteúdo mais recente esteja disponível no cartão.</li></ul></td>
  </tr>
  <tr>
    <td class="leftHeader">Público</td>
    <td class="tg-0pky">A Braze avalia a participação no público quando a campanha é enviada.<br><br>Usuários novos ou anônimos não serão avaliados para elegibilidade se tentarem visualizar o cartão após o envio da campanha. Para campanhas recorrentes, isso acontecerá no próximo intervalo de recorrência.</td>
    <td class="tg-0pky">A Braze avalia a participação quando o usuário abre o app novamente (inicia uma sessão, <a href="#campaign_note">somente campanhas*</a>).<br><br>Essa configuração terá um alcance de público mais amplo, pois qualquer usuário novo ou anônimo sempre será avaliado para elegibilidade quando tentar visualizar o cartão.<br><br>Além disso, o limite de taxa (limitar o número de pessoas que receberão o cartão) não se aplica quando configurado para a primeira impressão.</td>
  </tr>
  <tr>
    <td class="leftHeader">Personalização</td>
    <td class="tg-0pky">A Braze avalia Liquid, Conteúdo conectado e Content Blocks no momento em que a campanha é lançada ou quando o usuário entra na etapa do Canvas. Para campanhas recorrentes, isso acontecerá no próximo intervalo de recorrência.</td>
    <td class="tg-0pky">A Braze avalia Liquid, Conteúdo conectado e Content Blocks no momento da primeira impressão ou após o próximo intervalo de recorrência.</td>
  </tr>
  <tr>
    <td class="leftHeader">Análise de dados</td>
  <td class="tg-0pky"><em>Mensagens enviadas</em> refere-se ao número de cartões que a Braze criou e disponibilizou. Isso não conta se os usuários visualizaram o cartão.</td>
  <td class="tg-0pky"><em>Mensagens enviadas</em> refere-se ao número de cartões que a Braze envia a um usuário após o início de uma sessão. No Canvas, se um usuário entra na etapa sem iniciar uma sessão, a Braze não envia um cartão, então essa métrica pode não corresponder ao número de usuários que entram em uma etapa.<br><br>Embora os usuários contatáveis e as impressões não mudem, espere um volume de envio menor (<em>Mensagens enviadas</em>) ao criar um cartão na primeira impressão em comparação com o lançamento da campanha ou a entrada na etapa do Canvas.</td>
  </tr>
  <tr>
    <td class="leftHeader">Tempo de processamento</td>
  <td class="tg-0pky">A Braze cria cartões para cada usuário elegível no segmento no momento do lançamento. Para públicos grandes, selecione <b>Na primeira impressão</b> para que os cartões fiquem disponíveis mais rapidamente após o lançamento.</td>
  <td class="tg-0pky">A Braze cria um cartão na primeira vez que o usuário tenta visualizá-lo, então pode levar de 1 a 2 segundos para exibir na primeira impressão.</td>
  </tr>
</tbody>
</table>

<p id="campaign_note"><sup>* Esse cenário se aplica apenas a campanhas, pois o público do Canvas é avaliado na entrada do Canvas, não no nível da etapa.</sup></p>

## Considerações {#considerations}

### Usando propriedades de contexto do Canvas {#using-canvas-context-properties}

Ao personalizar Content Cards com [propriedades de contexto do Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties/), use a sintaxe `${...}` (por exemplo, {%raw%}`{{context.${property_name}}}`{%endraw%}). A notação de ponto sem essa sintaxe (por exemplo, {%raw%}`{{context.property_name}}`{%endraw%}) pode não ser resolvida corretamente em Content Cards, mesmo que funcione em outros canais como push e e-mail.

### Alterando a criação de cartão após o lançamento {#changing-card-creation-after-launch}

A Braze recomenda não alterar como os cartões são criados após o lançamento de uma campanha. Devido às diferenças na forma como *Mensagens enviadas* é calculado entre os dois tipos de criação de cartão, alterar como os cartões são criados após o lançamento da campanha pode afetar a precisão do seu volume de envio.

### Tempo de processamento potencial {#potential-processing-time}

Para públicos grandes, selecione a opção de criar cartões na primeira impressão para que os cartões fiquem disponíveis rapidamente após o lançamento. Campanhas disparadas no início da sessão também podem se beneficiar ao mudar para criação na primeira impressão (disponível por meio de entrega agendada) para melhorar o desempenho.

Quando os cartões são criados na primeira impressão, pode levar de 1 a 2 segundos para processá-los. A duração desse tempo de processamento depende de vários fatores, como o tamanho do cartão e a complexidade das opções de modelo da mensagem. Por exemplo, o tempo de processamento para cartões que usam Conteúdo conectado será pelo menos tão longo quanto o tempo de resposta do Conteúdo conectado.

### Versões anteriores do SDK {#previous-sdk-versions}

Se o app de um usuário está executando uma versão anterior do SDK, ele ainda receberá os Content Cards que você enviar. No entanto, os cartões demoram mais para aparecer e podem não ser exibidos até a próxima sincronização de Content Cards.