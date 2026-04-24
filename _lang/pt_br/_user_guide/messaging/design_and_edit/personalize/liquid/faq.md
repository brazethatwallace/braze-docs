---
nav_title: FAQ
article_title: Perguntas frequentes
page_order: 12
description: "Este artigo fornece respostas para perguntas frequentes sobre Liquid."

---

# Perguntas frequentes

> Nesta página, você encontrará respostas para algumas perguntas frequentes sobre Liquid.<br><br>A Braze atualmente não oferece suporte a 100% do Liquid da Shopify, apenas a certas partes que tentamos descrever em nossa documentação. Recomendamos fortemente que você teste todas as mensagens que usam Liquid antes de enviá-las, para reduzir o risco de erros ou de uso de Liquid não suportado.

### Como uso snippets de Liquid na Braze?

Em muitos casos, você pode incorporar snippets de Liquid navegando até suas campanhas ou Canvas e inserindo Liquid no modal de personalização em áreas como o corpo do e-mail ou nos seus segmentos.

#### Onde posso saber mais?

Para saber mais sobre Liquid, confira nosso caminho de aprendizado guiado [Personalização dinâmica com Liquid](https://learning.braze.com/path/dynamic-personalization-with-liquid) no Braze Learning! Você também pode consultar a [biblioteca de casos de uso de Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/liquid_use_cases/) para inspiração e uma variedade de exemplos de personalização usando Liquid.

### Qual é a diferença entre usar Liquid e Conteúdo conectado para personalização?

O Conteúdo conectado da Braze é um exemplo de Liquid tag. Ele também é usado para personalização, mas os dados vêm de um endpoint externo em vez de dados armazenados na Braze. Confira nossa seção dedicada de [Conteúdo conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/) para saber mais sobre como expandir a personalização das suas mensagens.

### O que é templating de Liquid?

Essa é a forma mais comum de usar Liquid na Braze. O templating de Liquid envolve puxar dados do perfil de um usuário para uma mensagem. Esses dados podem variar desde o nome do usuário até eventos personalizados de uma mensagem disparada por evento.

Consulte [Tags de personalização suportadas]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags/) para uma lista completa das Liquid tags suportadas.

### Como atribuo variáveis com Liquid?

Você pode criar e atribuir variáveis usando a tag `assign`. Isso cria uma variável no criador de mensagens que também pode ser referenciada ao longo da sua mensagem.

### Usar Liquid registra pontos de dados?

Não.

### Como posso usar Liquid para enviar uma saudação personalizada?

Para uma saudação personalizada usando o nome do usuário, você pode puxar os atributos padrão do perfil de usuário, como {% raw %} `{{${first_name}}}`, `{{${last_name}}}`.

Você também pode usar uma instrução `{% if X %}` {% endraw %} de Liquid para fazer renderização condicional com base em qualquer coisa, como o dia da semana ou atributos personalizados. Para saber mais sobre os operadores de Liquid suportados que podem ser usados em instruções condicionais, confira [Operadores]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/operators/).

### Como posso personalizar uma mensagem com base no local de um cliente?

{% raw %}
Existe um atributo padrão para o local do usuário: `{{${most_recent_location}}}`.

### Qual é a diferença entre {{campaign.${name}}} e {{campaign.${message_name}}}?

Tanto `{{campaign.${name}}}` quanto `{{campaign.${message_name}}}` são Liquid tags de personalização suportadas. Ambas as tags fazem referência a atributos da campanha. `{{campaign.${name}}}` indica o nome da sua campanha, e `{{campaign.${message_name}}}` é o nome da variante da sua mensagem.
{% endraw %}

### Como uso Liquid com objetos aninhados?

A Braze tem um recurso integrado que gera código Liquid para segmentos que podem ser usados em uma mensagem. Especificamente, você pode criar um segmento que corresponda a múltiplos critérios em um objeto.

Para saber mais, confira [Segmentação com múltiplos critérios]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support/#multi-criteria-segmentation).

### Como uso atributos de evento para personalizar uma mensagem que um evento está disparando?

{% raw %}
Você pode acessar propriedades de eventos disparados por API com a tag `api_triggered_property`: `{{api_trigger_properties.${attribute_key}}}`.
{% endraw %}

### O que é lógica de cancelamento e como posso usá-la?

A lógica de cancelamento permite que você interrompa o envio de uma mensagem se as condições forem atendidas. Isso é especialmente útil para evitar que mensagens incompletas sejam enviadas aos seus usuários. Para exemplos de lógica de cancelamento nas suas campanhas de marketing, leia mais em [Cancelamento de mensagens]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages/).

### O que é lógica de loop for e como posso usá-la?

Loops for também são conhecidos como [tags de iteração](https://shopify.github.io/liquid/tags/iteration/). Usar lógica de loop for nos seus snippets de Liquid permite que você percorra blocos de Liquid até que uma condição seja atendida.

Na Braze, isso pode ser usado para verificar itens em um atributo personalizado de array, ou uma lista de valores e objetos retornados por uma chamada de [catálogo]({{site.baseurl}}/user_guide/data/activation/catalogs/), [seleção]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/) ou resposta de [Conteúdo conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/). Especificamente, você pode usar lógica de loop for como parte do seu envio de mensagens para verificar se um produto está em estoque ou se um produto tem uma avaliação mínima.

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

### Por que há espaçamento extra em mensagens que usam Blocos de conteúdo?

Se você notar espaçamento extra em mensagens enviadas que usam Blocos de conteúdo com Liquid, pode haver quebras de parágrafo ou de linha desnecessárias dentro das suas instruções condicionais. Escreva suas instruções condicionais em uma única linha em vez de em múltiplas linhas.

#### Exemplo

{% raw %}
```liquid
{% if {{custom_attribute.${has_discount}}} == true %}Discounted Item{% elsif {{custom_attribute.${is_new_arrival}}} == true %}New Arrival{% else %}Regular Item{% endif %}
{% endraw %}

### When should I use `assign` versus `capture`?

Both `assign` and `capture` create Liquid variables, but they serve different purposes:

- `assign` is for simple variables that store a single value, such as a boolean, number, or simple string. You can also apply a single filter in the same line.
- `capture` is for storing a block of text that may include multiple variables, strings, or complex expressions. Use `capture` when the value is too complex for a single `assign` statement, such as URLs that utilize other Liquid variables or custom attributes as parameters. `capture` is also preferred when implementing Liquid variables in the body of Connected Content calls.

#### Examples

{% raw %}
```liquid
{% comment %} Valid assign usage {% endcomment %}
{% assign name = {{custom_attribute.${first_name}}} %}
{% assign price = {{custom_attribute.${price}}} | plus: 0 %}

{% comment %} Use capture for complex strings {% endcomment %}
{% capture greeting %}Hello, {{custom_attribute.${first_name}}}! Your order #{{custom_attribute.${order_id}}} is ready.{% endcapture %}
{{ greeting }}
```
{% endraw %}