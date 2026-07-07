---
nav_title: FAQ
article_title: Perguntas frequentes
page_order: 12
description: "Este artigo fornece respostas para perguntas frequentes sobre Liquid."
toc_headers: h2
---

# Perguntas frequentes {#frequently-asked-questions}

> Nesta página, você encontra respostas para perguntas frequentes sobre Liquid.

{% alert note %}
A Braze atualmente não oferece suporte a 100% do Liquid da Shopify, apenas a certas partes, que tentamos descrever em nossa documentação. Teste todas as mensagens que usam Liquid antes de enviá-las, para reduzir o risco de erros ou de uso de Liquid não suportado.
{% endalert %}

## Sobre Liquid na Braze {#about-liquid-in-braze}

### Como uso snippets de Liquid na Braze? {#how-do-i-use-liquid-snippets-in-braze}

Em muitos casos, você pode incorporar snippets de Liquid navegando até suas Campaigns ou Canvas e inserindo Liquid no modal de personalização em áreas como o corpo do e-mail ou nos seus Segments.

#### Onde posso saber mais? {#where-can-i-learn-more}

Para saber mais sobre Liquid, confira nosso caminho de aprendizado guiado [Personalização dinâmica com Liquid](https://learning.braze.com/path/dynamic-personalization-with-liquid) no Braze Learning. Você também pode consultar a [biblioteca de casos de uso de Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/liquid_use_cases) para inspiração e uma variedade de exemplos de personalização usando Liquid.

### Qual é a diferença entre usar Liquid e Conteúdo conectado para personalização? {#whats-the-difference-between-using-liquid-and-connected-content-for-personalization}

O Conteúdo conectado da Braze é um exemplo de Liquid tag. Ele também é usado para personalização, mas os dados vêm de um endpoint externo em vez de dados armazenados na Braze. Confira nossa seção dedicada de [Conteúdo conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content) para saber mais sobre como expandir a personalização das suas mensagens.

### O que é templating de Liquid? {#what-is-liquid-templating}

Essa é a forma mais comum de usar Liquid na Braze. O templating de Liquid envolve puxar dados do perfil de um usuário para uma mensagem. Esses dados podem variar desde o nome do usuário até eventos personalizados de uma mensagem disparada por evento.

Consulte [Tags de personalização suportadas]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags) para uma lista completa das Liquid tags suportadas.

### Usar Liquid registra pontos de dados? {#does-using-liquid-log-data-points}

Não.

## Tags de personalização e fontes de dados {#personalization-tags-and-data-sources}

### Como posso usar Liquid para enviar uma saudação personalizada? {#how-can-i-use-liquid-to-send-a-personalized-greeting}

Para uma saudação personalizada usando o nome do usuário, puxe os atributos padrão do perfil de usuário, como {% raw %}`{{${first_name}}}` e `{{${last_name}}}`{% endraw %}.

Você também pode usar uma instrução {% raw %}`{% if X %}`{% endraw %} de Liquid para fazer renderização condicional com base em qualquer coisa, como o dia da semana ou atributos personalizados. Para saber mais sobre os operadores de Liquid suportados que podem ser usados em instruções condicionais, confira [Operadores]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/operators).

### Como posso personalizar uma mensagem com base no local de um usuário? {#how-can-i-personalize-a-message-based-on-a-users-location}

{% raw %}
Existe um atributo padrão para o local do usuário: `{{${most_recent_location}}}`.
{% endraw %}

{% raw %}
### Qual é a diferença entre {{campaign.${name}}} e {{campaign.${message_name}}}? {#whats-the-difference-between-campaignname-and-campaignmessage_name}

Tanto `{{campaign.${name}}}` quanto `{{campaign.${message_name}}}` são Liquid tags de personalização suportadas. Ambas as tags fazem referência a atributos da Campaign. `{{campaign.${name}}}` indica o nome da sua Campaign, e `{{campaign.${message_name}}}` é o nome da variante da sua mensagem.
{% endraw %}

Para uso em URLs e query strings (por exemplo, quando um nome contém `%` ou espaços), consulte [Nomes de Campaign em URLs]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags#campaign-names-in-urls).

### Como uso Liquid com objetos aninhados? {#how-do-i-use-liquid-with-nested-objects}

A Braze tem um recurso integrado que gera código Liquid para Segments que podem ser usados em uma mensagem. Especificamente, você pode criar um Segment que corresponda a múltiplos critérios em um objeto.

Para saber mais, confira [Segmentação com múltiplos critérios]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support#multi-criteria-segmentation).

### Como uso atributos de evento para personalizar uma mensagem que um evento está disparando? {#how-do-i-use-event-attributes-to-personalize-a-message-that-an-event-is-triggering}

{% raw %}
Você pode acessar propriedades de eventos disparados por API com a tag `api_triggered_property`: `{{api_trigger_properties.${attribute_key}}}`.
{% endraw %}

### A Braze suporta array de arrays em Liquid? {#does-braze-support-an-array-of-arrays-in-liquid}

O Liquid não suporta nativamente arrays de arrays. Armazene os valores como um array de strings separadas por vírgula e use o filtro `split` para analisá-los quando necessário.

## Variáveis e sintaxe {#variables-and-syntax}

### Como atribuo variáveis com Liquid? {#how-do-i-assign-variables-with-liquid}

Você pode criar e atribuir variáveis usando a tag `assign`. Isso cria uma variável no criador de mensagens que também pode ser referenciada ao longo da sua mensagem.

### Quando devo usar `assign` versus `capture`? {#when-should-i-use-assign-versus-capture}

Tanto `assign` quanto `capture` criam variáveis de Liquid, mas servem a propósitos diferentes:

- `assign` é para variáveis simples que armazenam um único valor, como um booleano, número ou string simples. Você também pode aplicar um único filtro na mesma linha.
- `capture` é para armazenar um bloco de texto que pode incluir múltiplas variáveis, strings ou expressões complexas.

Use `capture` quando o valor for complexo demais para uma única instrução `assign`, como URLs que utilizam outras variáveis de Liquid ou atributos personalizados como parâmetros. `capture` também é preferido ao implementar variáveis de Liquid no corpo de chamadas de Conteúdo conectado.

#### Exemplos {#examples}

{% raw %}
```liquid
{% comment %}Use assign for custom attributes{% endcomment %}
{% assign name = {{custom_attribute.${first_name}}} %}
{% assign price = {{custom_attribute.${price}}} | plus: 0 %}

{% comment %}Use assign for a simple variable{% endcomment %}
{% assign discount_label = "20% off" %}
Hello {{ customer.first_name | default: "there" }}, enjoy {{ discount_label }} on your next order!

{% comment %}Use capture for complex strings{% endcomment %}
{% capture greeting %}Hello, {{custom_attribute.${first_name}}}! Your order #{{custom_attribute.${order_id}}} is ready.{% endcapture %}
{{ greeting }}

{% comment %}Use capture to create conditional content{% endcomment %}
{% capture promo_block %}
{% if customer.vip == true %}
As a VIP member, you get free shipping.
{% else %}
Join our VIP program to unlock free shipping.
{% endif %}
{% endcapture %}
```
{% endraw %}

### As variáveis de Liquid são compartilhadas entre a linha de assunto e o corpo? {#do-liquid-variables-carry-between-subject-line-and-body}

Não. A Braze renderiza cada componente da mensagem separadamente (como linha de assunto, corpo HTML, pré-cabeçalho e título de push). Atribuições ou capturas feitas em um campo não ficam disponíveis em outro. Repita a chamada de Liquid ou Conteúdo conectado em cada campo que precisar do valor.

### O que é lógica de loop for e como posso usá-la? {#what-is-for-loop-logic-and-how-can-i-use-it}

Loops for também são conhecidos como [tags de iteração](https://shopify.github.io/liquid/tags/iteration/). Usar lógica de loop for nos seus snippets de Liquid permite que você percorra blocos de Liquid até que uma condição seja atendida.

Na Braze, isso pode ser usado para verificar itens em um atributo personalizado de array, ou uma lista de valores e objetos retornados por uma chamada de [catálogo]({{site.baseurl}}/user_guide/data/activation/catalogs), [seleção]({{site.baseurl}}/user_guide/data/activation/catalogs/selections) ou resposta de [Conteúdo conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content). Especificamente, você pode usar lógica de loop for como parte do seu envio de mensagens para verificar se um produto está em estoque ou se um produto tem uma avaliação mínima.

Por exemplo, digamos que você tenha um catálogo chamado "Games" que tem uma seleção chamada "cheap_games". Para puxar os títulos dos jogos em "cheap_games", você pode usar este snippet de Liquid:

{% raw %}
```liquid
{% catalog_selection_items Games cheap_games %}
{% for item in items %}
 Get this game: {{ item.title }}
{% endfor %}
```
{% endraw %}

Quando as condições definidas forem atendidas, sua mensagem pode prosseguir. Usar essa lógica é uma forma útil de economizar tempo, em vez de repetir blocos de Liquid para diferentes condições.

### O que é lógica de cancelamento e como posso usá-la? {#what-is-abort-logic-and-how-can-i-use-it}

A lógica de cancelamento permite que você interrompa o envio de uma mensagem se as condições forem atendidas. Isso é especialmente útil para evitar que mensagens incompletas sejam enviadas aos seus usuários. Para exemplos de lógica de cancelamento nas suas Campaigns de marketing, leia mais em [Cancelamento de mensagens]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages).

### Posso usar Liquid dentro da tag `abort_message`? {#can-i-use-liquid-inside-the-abort_message-tag}

Não. A tag {% raw %}`{% abort_message %}`{% endraw %} aceita uma string estática entre aspas, não personalização com Liquid. Use outra lógica de Liquid antes da tag se precisar de um comportamento condicional de cancelamento.

## Canvas, catálogos e propriedades de gatilho {#canvas-catalogs-and-trigger-properties}

### Por que meu Liquid disparado por API está falhando na Braze? {#why-is-my-api-triggered-liquid-failing-in-braze}

{% raw %}
Uma causa comum é um par extra de chaves. Por exemplo, `{{{api_trigger_properties.${attribute_key}}}}` não é uma sintaxe de personalização válida na Braze. Use exatamente duas chaves de abertura e duas de fechamento: `{{api_trigger_properties.${attribute_key}}}`.
{% endraw %}

### Existem limites de tamanho para propriedades de contexto do Canvas? {#are-there-size-limits-for-canvas-context-properties}

A Braze não impõe um limite rígido para [propriedades de contexto do Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties), mas mantenha as cargas úteis abaixo de aproximadamente 1 KB (~1.000 caracteres). Objetos maiores podem aumentar o uso de memória e atrasar a renderização de mensagens durante envios de alto volume.

### Por que recebo um erro de Liquid ao pré-visualizar certos tipos de dados no dashboard? {#why-do-i-get-a-liquid-error-when-previewing-certain-data-types-in-the-dashboard}

Alguns tipos de [propriedade de contexto do Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties) exigem coerção em Liquid antes de serem usados em comparações ou operações matemáticas. Por exemplo, quando você precisa de comportamento numérico:

{% raw %}
```liquid
{{context.${property_name} | plus: 0}}
```
{% endraw %}

### Por que meu snippet de Liquid de catálogo retorna uma mensagem de cancelamento? {#why-does-my-catalog-liquid-snippet-return-an-abort-message}

Se um snippet de Liquid de catálogo for cancelado durante o envio, recrie o snippet a partir do menu de personalização selecionando itens individuais do catálogo em vez de usar uma seleção em massa ou totalmente dinâmica. Consulte [Catálogos]({{site.baseurl}}/user_guide/data/activation/catalogs) e [Seleções]({{site.baseurl}}/user_guide/data/activation/catalogs/selections).

## Content Blocks e o criador de mensagens {#content-blocks-and-the-message-composer}

### Por que há espaçamento extra em mensagens que usam Content Blocks? {#why-is-there-extra-spacing-in-messages-that-use-content-blocks}

Se você notar espaçamento extra em mensagens enviadas que usam Content Blocks com Liquid, pode haver quebras de parágrafo ou de linha desnecessárias dentro das suas instruções condicionais. Escreva suas instruções condicionais em uma única linha em vez de em múltiplas linhas.

#### Exemplo {#example}

{% raw %}
```liquid
{% if {{custom_attribute.${has_discount}}} == true %}Discounted Item{% elsif {{custom_attribute.${is_new_arrival}}} == true %}New Arrival{% else %}Regular Item{% endif %}
```
{% endraw %}

### Por que meu Content Block não aparece em **Row** na ferramenta de busca do editor de arrastar e soltar? {#why-is-my-content-block-missing-from-row-in-the-drag-and-drop-search-tool}

Alguns Content Blocks não aparecem em **Row** na busca do editor de arrastar e soltar. Adicione um bloco HTML a partir da guia **Content** (**Advanced**) e insira a Liquid tag do Content Block nesse bloco HTML para renderizar o conteúdo do bloco.

### Por que a pré-visualização do meu Content Block no editor de arrastar e soltar difere da visualização de composição? {#why-does-my-drag-and-drop-content-block-preview-differ-from-the-compose-view}

Quando você usa um Content Block com Liquid como modelo, as media queries para dispositivos móveis no bloco podem não ser aplicadas na pré-visualização da mesma forma que quando você arrasta o bloco diretamente para uma mensagem. Arrastar o bloco preserva o layout, mas o desacopla do bloco de origem, então edições futuras no bloco não atualizam mais a mensagem automaticamente.

### Como pré-visualizo valores de propriedades de evento no criador de mensagens? {#how-do-i-preview-event-property-values-in-message-composer}

Use **Pré-visualizar como usuário personalizado** e insira valores de amostra de propriedades de evento personalizado para o usuário que você está pré-visualizando. Isso também é útil para mensagens com lógica de cancelamento quando você precisa de valores de pré-visualização que não disparem um cancelamento.

## Liquid em mensagens de e-mail {#liquid-in-email-messages}

### Por que minha mensagem é cancelada com "Invalid from email address for recipient:"? {#why-does-my-message-abort-with-invalid-from-email-address-for-recipient}

Esse cancelamento ocorre quando o Liquid no campo **De** produz uma sintaxe inválida, como uma variável ausente, espaços extras ou caracteres não permitidos. Faça a pré-visualização com um usuário teste e verifique se o endereço **De** renderizado corresponde ao seu domínio de envio configurado.

### Como crio um endereço de resposta (Reply-To) dinâmico? {#how-do-i-create-a-dynamic-reply-to-address}

Use Liquid no campo **Reply-To** quando seu espaço de trabalho suportar configuração dinâmica de Reply-To. Combine com as configurações de nome de exibição do campo **De** conforme necessário. Consulte [Configurações de e-mail]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences) para opções específicas do espaço de trabalho.

## Solução de problemas com erros de Liquid {#troubleshooting-liquid-errors}

### Por que estou vendo um erro de Liquid "Unexpected end token"? {#why-am-i-seeing-an-unexpected-end-token-liquid-error}

Esse erro geralmente indica chaves extras ou ausentes. Não aninhe {% raw %}`{{ }}`{% endraw %} dentro de outra expressão de tag Liquid. Por exemplo, use {% raw %}`{{custom_attribute.${date_of_birth} | date: '%s'}}`{% endraw %} em vez de envolver a referência do atributo em um par adicional de chaves.

### Por que a tentativa de repetição do Conteúdo conectado não está disponível para minha mensagem no app? {#why-is-connected-content-retry-unavailable-for-my-in-app-message}

{% raw %}
A tag `{% connected_content %}` com tentativa de repetição não é suportada para todos os tipos de mensagem, incluindo alguns formatos de mensagem no app. Remova os parâmetros de tentativa de repetição ou use um canal suportado para chamadas de Conteúdo conectado com repetição.
{% endraw %}