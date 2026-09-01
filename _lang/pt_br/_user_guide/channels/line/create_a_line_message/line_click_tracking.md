---
nav_title: Rastreamento de cliques do LINE
article_title: Rastreamento de cliques do LINE
page_order: 2
description: "Esta página aborda como ativar o rastreamento de cliques nas suas mensagens LINE, testar links encurtados, usar seu domínio personalizado em links rastreados e muito mais."
page_type: reference
alias: /line/click_tracking/
channel:
 - LINE
---

# Rastreamento de cliques do LINE {#line-click-tracking}

> Esta página aborda como ativar o rastreamento de cliques nas suas mensagens LINE, testar links encurtados, usar seu domínio personalizado em links rastreados e muito mais.


Quando o rastreamento de cliques do LINE está ativado, a Braze encurta automaticamente suas URLs, adiciona mecanismos de rastreamento e registra cliques em tempo real. Embora o LINE ofereça dados agregados de cliques, a Braze fornece informações granulares de usuários que são oportunas e acionáveis. Esses dados permitem que você crie estratégias de segmentação e redirecionamento mais direcionadas, como segmentar usuários com base no comportamento de cliques e disparar mensagens em resposta a cliques específicos.

O rastreamento de cliques do LINE pode ser usado para mensagens de texto, rich e baseadas em cartão. Ele suporta links dentro de botões e áreas mapeadas por imagem que possuem uma URL como ação ao clicar. Você também pode personalizar URLs usando Liquid e domínios personalizados.

## Como funciona {#how-it-works}

Você pode gerenciar as configurações de rastreamento de cliques do LINE na guia **Settings** ao criar uma mensagem. Quando ativado, os URLs serão encurtados usando o domínio padrão da Braze (`https://brz.ai`) ou o domínio personalizado especificado para o grupo de inscrições, e personalizados para o usuário.

Qualquer URL que comece com `http://` ou `https://` será encurtado. Você pode ter até 25 URLs em uma mensagem. URLs encurtados que contêm personalização Liquid (como rastreamento em nível de usuário ou parâmetros UTM) serão válidos por dois meses.

## Configurando o rastreamento de cliques {#setting-up-click-tracking}

### Mensagens de texto {#text-messages}

Para configurar o rastreamento de cliques em uma mensagem de texto:

1. Arraste uma mensagem de **Texto** para o criador e adicione uma URL ao campo de texto.

![Criador de mensagens LINE com uma mensagem de texto contendo uma URL longa antes do encurtamento.]({% image_buster /assets/img/line/click_tracking_text_message.png %})

{: start="2"}
2. Acesse a guia **Settings** e confirme que o **Click Tracking** está ativado. O rastreamento de cliques é ativado por padrão para todas as novas mensagens.

{% alert note %}
Você pode visualizar prévias do link encurtado nas guias **Settings** ou **Preview & Test**. O link completo será exibido no criador enquanto você constrói sua mensagem.
{% endalert %}

![Guia "Settings" do criador de mensagens LINE com "Click Tracking" ativado e uma prévia de mensagem de texto contendo uma URL encurtada: https://olaf.brz.ai/p/9rcfdqdD]({% image_buster /assets/img/line/click_tracking_settings.png %})

### Mensagens rich {#rich-messages}

Para configurar o rastreamento de cliques em uma mensagem rich:

1. Arraste uma **Rich message** para o criador e selecione um modelo.
2. Selecione **URI** para o **comportamento ao clicar** da área tocável aplicável.
3. Insira uma URL no campo **Open URL**.

![Criador de mensagens LINE com uma mensagem rich com duas áreas tocáveis, cada uma contendo uma URL.]({% image_buster /assets/img/line/rich_message_click_tracking.png %})

{: start="4"}
4. Acesse a guia **Settings** e confirme que o **Click Tracking** está ativado. O rastreamento de cliques é ativado por padrão para todas as novas mensagens.

### Mensagens baseadas em cartão {#card-based-messages}

Para configurar o rastreamento de cliques em uma mensagem baseada em cartão:

1. Arraste uma **Card-based message** para o criador.
2. Selecione **URI** para o **comportamento ao clicar** do cartão ou das áreas de botão aplicáveis.

![Criador de mensagens LINE com uma mensagem baseada em cartão com dois botões, cada um contendo uma URL.]({% image_buster /assets/img/line/card_based_message_click_tracking.png %})

{: start="3"}
3. Acesse a guia **Settings** e confirme que o **Click Tracking** está ativado. O rastreamento de cliques é ativado por padrão para todas as novas mensagens.

{% alert note %}
URLs nos campos **Title** ou **Description** não serão encurtadas porque esses campos não são clicáveis no LINE.
{% endalert %}

## Domínios personalizados {#custom-domains}

O rastreamento de cliques do LINE permite que você use seu próprio domínio para personalizar a aparência das suas URLs encurtadas, ajudando a transmitir uma imagem de marca consistente. Para saber mais, consulte [Domínios personalizados]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/custom_domains).

## Personalização Liquid em URLs {#liquid-personalization-in-urls}

Você pode construir dinamicamente sua URL diretamente no criador da Braze, permitindo adicionar parâmetros UTM dinâmicos às suas URLs ou enviar links exclusivos aos usuários (como direcionar usuários ao carrinho abandonado ou a um produto específico que voltou ao estoque).
Você pode gerar URLs dinamicamente usando qualquer tag de personalização Liquid compatível.

{% raw %}
```
https://example.com/?campaign_utm={{campaign.${api_id}}}&user_attribute={{custom_attribute.${attribute1}}}
```
{% endraw %}

Você também pode encurtar variáveis Liquid personalizadas, conforme mostrado no exemplo a seguir:

{% raw %}
```liquid
{% assign url_var = {{event_properties.${url_slug}}} %}
https://example.com/{{url_var}}
```
{% endraw %}

## Encurtar URLs renderizadas por variáveis Liquid {#shorten-urls-rendered-by-liquid-variables}

A Braze encurta URLs que são renderizadas por Liquid, incluindo aquelas presentes em propriedades de disparo de API. Por exemplo, se {% raw %}`{{api_trigger_properties.${url_value}}}`{% endraw %} representar uma URL válida, encurtamos e rastreamos essa URL antes de enviar a mensagem LINE.

## Testes {#testing}

Antes de lançar sua Campaign ou Canvas, é uma prática recomendada pré-visualizar e testar sua mensagem primeiro. Para isso, acesse a guia **Teste** para pré-visualizar e enviar uma mensagem LINE para grupos de teste de conteúdo ou para um usuário individual.

Essa prévia será atualizada com a personalização relevante e a URL encurtada.

{% alert important %}
Se um rascunho for criado dentro de um Canvas ativo, uma URL encurtada não será gerada. A URL encurtada real é gerada quando o rascunho do Canvas é ativado.
{% endalert %}

## Relatórios {#reporting}

A tabela de desempenho do LINE inclui a coluna **Total Clicks** que mostra uma contagem de eventos de clique por variante e uma taxa de cliques associada. Para saber mais sobre as métricas do LINE, consulte [Desempenho de mensagens do LINE]({{site.baseurl}}/user_guide/channels/line/reporting).

![Desempenho de uma etapa do Canvas no LINE.]({% image_buster /assets/img/line/line_step_performance.png %}){: style="max-width:30%;"}

Os dados de cliques serão automaticamente reportados no dashboard de análise de dados.

![Dashboard de análise de desempenho do LINE.]({% image_buster /assets/img/line/line_performance.png %})

## Redirecionamento de usuários {#retargeting-users}

Você pode redirecionar usuários que clicaram em uma URL em uma mensagem LINE usando os seguintes filtros de segmentação e disparadores:

- Disparadores baseados em ação
    - Interagir com Campaign
    - Interagir com etapa

![Disparador de entrega baseada em ação do LINE.]({% image_buster /assets/img/line/line_action_based.png %})

- Filtros de segmentação
    - Clicou/Abriu Campaign
    - Clicou/Abriu Campaign ou Canvas com tag
    - Clicou/Abriu etapa

![Grupo de filtros exibindo todos os três filtros de segmentação: "Clicou/Abriu Campaign", "Clicou/Abriu Campaign ou Canvas com tag" e "Clicou/Abriu etapa".]({% image_buster /assets/img/line/line_segmentation_filters.png %})

## Perguntas frequentes {#frequently-asked-questions}

### Os links que recebo ao fazer envios de teste são URLs reais? {#are-the-links-i-receive-when-test-sending-real-urls}

Sim, URLs reais são geradas ao fazer envios de teste. No entanto, a URL exata enviada em uma Campaign lançada pode ser diferente daquela enviada em um envio de teste.

### Posso adicionar parâmetros UTM a uma URL antes de ela ser encurtada? {#can-i-add-utm-parameters-to-a-url-before-it-is-shortened}

Sim, tanto parâmetros estáticos quanto dinâmicos podem ser adicionados.

### Por quanto tempo as URLs encurtadas permanecem válidas? {#how-long-do-shortened-urls-remain-valid}

As URLs personalizadas são válidas por dois meses a partir do momento do registro da URL.

### O SDK da Braze precisa estar instalado para encurtar URLs? {#does-the-braze-sdk-need-to-be-installed-in-order-to-shorten-urls}

Não, o rastreamento de cliques funciona sem nenhuma integração SDK.

### É possível saber quais usuários individuais estão clicando em uma URL? {#do-i-know-which-individual-users-are-clicking-on-a-url}

Sim. Quando o rastreamento de cliques está ativado, você pode redirecionar usuários que clicaram em URLs usando os [filtros de redirecionamento do LINE](#retargeting-users).

### O rastreamento de cliques funciona com deep links ou links universais? {#does-click-tracking-work-with-deep-links-or-universal-links}

O rastreamento de cliques não funciona com deep links. Você pode encurtar links universais de provedores como Branch ou Appsflyer, mas a Braze não consegue solucionar problemas que possam surgir ao fazer isso (como quebrar a atribuição ou falhar no redirecionamento).

### As prévias no app do LINE contam como cliques? {#do-previews-on-the-line-app-count-as-clicks}

Não, elas não contribuem para a taxa de cliques de mensagens do LINE.