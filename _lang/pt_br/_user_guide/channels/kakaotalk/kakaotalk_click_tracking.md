---
nav_title: Rastreamento de cliques do KakaoTalk
article_title: Rastreamento de cliques do KakaoTalk
page_order: 3
description: "Esta página aborda como ativar o rastreamento de cliques nas suas mensagens do KakaoTalk, testar links encurtados, usar seu domínio personalizado em links rastreados e mais."
page_type: reference
alias: /kakaotalk_click_tracking/
channel:
 - KakaoTalk
---

# Rastreamento de cliques do KakaoTalk {#kakaotalk-click-tracking}

> Esta página aborda como ativar o rastreamento de cliques nas suas mensagens do KakaoTalk, testar links encurtados, usar seu domínio personalizado em links rastreados e mais.

Quando o rastreamento de cliques do KakaoTalk está ativado, a Braze encurta automaticamente suas URLs, adiciona mecanismos de rastreamento e registra cliques em tempo real. Esses dados permitem que você crie estratégias de segmentação e redirecionamento mais direcionadas, como segmentar usuários com base no comportamento de cliques e disparar mensagens em resposta a cliques específicos.

O rastreamento de cliques do KakaoTalk pode ser usado para mensagens de texto, imagem e itens de lista. Ele suporta links dentro de botões e ações de clique em imagens. Você também pode personalizar URLs usando Liquid e domínios personalizados.

## Como funciona {#how-it-works}

Você pode gerenciar as configurações de rastreamento de cliques do KakaoTalk na seção **Link options** do criador de mensagens. Quando ativado, as URLs serão encurtadas usando o domínio padrão da Braze (`https://brz.ai`) ou o domínio personalizado especificado para o grupo de inscrições, e personalizadas para o usuário.

Qualquer URL que comece com `http://` ou `https://` será encurtada. Você pode ter até 25 URLs em uma mensagem. URLs encurtadas que contêm personalização com Liquid (como rastreamento em nível de usuário ou parâmetros UTM) serão válidas por dois meses.

## Configurar o rastreamento de cliques {#set-up-click-tracking}

### Mensagens de texto {#text-messages}

Para configurar o rastreamento de cliques para uma mensagem de texto:

1. Crie uma mensagem de **Text** e adicione uma URL ao campo de texto ou botão.
2. Na seção **Link options** do criador de mensagens, confirme que **Click Tracking** está marcado. O rastreamento de cliques é ativado por padrão para todas as novas mensagens.

![Criador de mensagens de texto do KakaoTalk mostrando a seção Link options com Click Tracking marcado.]({% image_buster /assets/img/kakaotalk/kakaotalk_text.png %})

### Mensagens de imagem {#image-messages}

Para configurar o rastreamento de cliques para uma mensagem de imagem:

1. Crie uma mensagem de **Image** e defina o comportamento ao clicar para abrir uma URL.
2. Insira uma URL no campo de URL.
3. Na seção **Link options** do criador de mensagens, confirme que **Click Tracking** está marcado.

### Mensagens de itens de lista {#list-item-messages}

Para configurar o rastreamento de cliques para uma mensagem de itens de lista:

1. Crie uma mensagem de **List item** e adicione uma URL ao campo **Website URL** para qualquer item.
2. Na seção **Link options** do criador de mensagens, confirme que **Click Tracking** está marcado.

## Domínios personalizados {#custom-domains}

O rastreamento de cliques do KakaoTalk permite que você use seu próprio domínio para personalizar a aparência das suas URLs encurtadas, ajudando a transmitir uma imagem de marca consistente. Para saber mais, consulte [Domínios personalizados]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/custom_domains).

## Personalização com Liquid em URLs {#liquid-personalization-in-urls}

Você pode construir sua URL dinamicamente diretamente no criador de mensagens da Braze, permitindo adicionar parâmetros UTM dinâmicos às suas URLs ou enviar links exclusivos aos usuários (como direcionar usuários ao carrinho abandonado ou a um produto específico que voltou ao estoque).

As URLs podem ser geradas dinamicamente por meio do uso de qualquer tag de personalização Liquid suportada.

{% raw %}
```
https://example.com/?campaign_utm={{campaign.${api_id}}}&user_attribute={{custom_attribute.${attribute1}}}
```
{% endraw %}

Você também pode encurtar variáveis Liquid definidas de forma personalizada, como mostrado no exemplo a seguir:

{% raw %}
```liquid
{% assign url_var = {{event_properties.${url_slug}}} %}
https://example.com/{{url_var}}
```
{% endraw %}

A Braze encurta URLs que são renderizadas por Liquid, incluindo aquelas incluídas em propriedades de disparo por API. Por exemplo, se {% raw %}`{{api_trigger_properties.${url_value}}}`{% endraw %} representa uma URL válida, a Braze encurtará e rastreará essa URL antes de enviar a mensagem do KakaoTalk.

## Testes {#testing}

Antes de lançar sua Campaign ou Canvas, a prática recomendada é pré-visualizar e testar sua mensagem primeiro. Para isso, acesse a guia **Test** para pré-visualizar e enviar uma mensagem do KakaoTalk para grupos de teste de conteúdo ou para um usuário individual.

A pré-visualização será atualizada com a personalização relevante e a URL encurtada.

{% alert important %}
Se um rascunho for criado dentro de um Canvas ativo, uma URL encurtada não será gerada. A URL encurtada real é gerada quando o rascunho do Canvas é ativado.
{% endalert %}

## Relatórios {#reporting}

A tabela de desempenho do KakaoTalk inclui a coluna **Total Clicks** que mostra uma contagem de eventos de clique por variante e uma taxa de cliques associada. Para mais detalhes sobre métricas do KakaoTalk, consulte [Relatórios do KakaoTalk]({{site.baseurl}}/kakaotalk_reporting).

Os dados de cliques serão reportados automaticamente no dashboard de análise de dados.

## Redirecionar usuários {#retarget-users}

Você pode redirecionar usuários que clicaram em uma URL em uma mensagem do KakaoTalk usando os seguintes filtros de segmentação e gatilhos:

- Gatilhos baseados em ação
    - Interact with Campaign
    - Interact with Step

- Filtros de segmentação
    - Clicked/Opened Campaign
    - Clicked/Opened Campaign or Canvas with Tag
    - Clicked/Opened Step

## Perguntas frequentes {#frequently-asked-questions}

### Os links que recebo ao enviar um teste são URLs reais? {#are-the-links-i-receive-when-test-sending-real-urls}

Sim, URLs reais serão geradas ao enviar um teste. No entanto, a URL exata enviada em uma Campaign lançada pode diferir daquela enviada em um envio de teste.

### Posso adicionar parâmetros UTM a uma URL antes de ela ser encurtada? {#can-i-add-utm-parameters-to-a-url-before-it-is-shortened}

Sim, tanto parâmetros estáticos quanto dinâmicos podem ser adicionados.

### Por quanto tempo as URLs encurtadas permanecem válidas? {#how-long-do-shortened-urls-remain-valid}

URLs personalizadas são válidas por dois meses a partir do momento do registro da URL.

### O SDK da Braze precisa estar instalado para encurtar URLs? {#does-the-braze-sdk-need-to-be-installed-in-order-to-shorten-urls}

Não, o rastreamento de cliques funciona sem nenhuma integração de SDK.

### Eu sei quais usuários individuais estão clicando em uma URL? {#do-i-know-which-individual-users-are-clicking-on-a-url}

Sim. Quando o rastreamento de cliques está ativado, você pode redirecionar usuários que clicaram em URLs usando os [filtros de redirecionamento do KakaoTalk](#retargeting-users).

### O rastreamento de cliques funciona com deep links ou links universais? {#does-click-tracking-work-with-deep-links-or-universal-links}

O rastreamento de cliques se aplica a URLs da web. Para deep links, você pode definir um deep link diretamente como o tipo de ação ao clicar para botões no KakaoTalk — esses não passam por encurtamento de URL ou rastreamento de cliques. Se você preferir usar links universais de provedores como Branch ou Appsflyer, eles podem ser encurtados, mas a Braze não consegue solucionar problemas que possam surgir (como quebra de atribuição ou falha no redirecionamento).