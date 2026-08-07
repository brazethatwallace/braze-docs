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

## Sobre o Liquid na Braze {#about-liquid-in-braze}

### Como uso snippets de Liquid na Braze? {#how-do-i-use-liquid-snippets-in-braze}

Em muitos casos, você pode incorporar snippets de Liquid acessando suas Campaigns ou Canvas e inserindo Liquid no modal de personalização em áreas como o corpo da mensagem de e-mail ou em seus Segments.

#### Onde posso saber mais? {#where-can-i-learn-more}

Para saber mais sobre Liquid, confira nosso caminho guiado [Personalização dinâmica com Liquid](https://learning.braze.com/path/dynamic-personalization-with-liquid) no Braze Learning. Você também pode consultar a [biblioteca de casos de uso do Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/liquid_use_cases) para inspiração e uma variedade de exemplos de personalização usando Liquid.

### Qual é a diferença entre usar Liquid e Connected Content para personalização? {#whats-the-difference-between-using-liquid-and-connected-content-for-personalization}

O Braze Connected Content é um exemplo de Liquid tag. Ele também é usado para personalização, mas os dados vêm de um endpoint externo em vez de dados armazenados na Braze. Confira nossa seção dedicada de [Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content) para saber mais sobre como expandir a personalização das suas mensagens.

### O que é templating de Liquid? {#what-is-liquid-templating}

Essa é a forma mais comum de usar Liquid na Braze. O templating de Liquid envolve extrair dados do perfil de um usuário para uma mensagem. Esses dados podem variar desde o nome do usuário até eventos personalizados de uma mensagem disparada por evento.

Consulte [Tags de personalização compatíveis]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags) para uma lista completa das Liquid tags compatíveis.

### O uso de Liquid registra pontos de dados? {#does-using-liquid-log-data-points}

Não.

## Tags de personalização e fontes de dados {#personalization-tags-and-data-sources}

### Como posso usar Liquid para enviar uma saudação personalizada? {#how-can-i-use-liquid-to-send-a-personalized-greeting}

Para uma saudação personalizada usando o nome do usuário, utilize os atributos padrão do perfil de usuário, como {% raw %}`{{${first_name}}}` e `{{${last_name}}}`{% endraw %}.

Você também pode usar uma instrução Liquid {% raw %}`{% if X %}`{% endraw %} para fazer renderização condicional com base em qualquer coisa, como o dia da semana ou atributos personalizados. Para saber mais sobre os operadores Liquid compatíveis que podem ser usados em instruções condicionais, confira [Operadores]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/operators).

### Como posso personalizar uma mensagem com base na localização do usuário? {#how-can-i-personalize-a-message-based-on-a-users-location}

{% raw %}
Existe um atributo padrão para a localização do usuário: `{{${most_recent_location}}}`.
{% endraw %}

{% raw %}
### Qual é a diferença entre {{campaign.${name}}} e {{campaign.${message_name}}}? {#whats-the-difference-between-campaignname-and-campaignmessage_name}

Tanto `{{campaign.${name}}}` quanto `{{campaign.${message_name}}}` são tags de personalização Liquid compatíveis. Ambas as tags fazem referência a atributos da Campaign. `{{campaign.${name}}}` indica o nome da sua Campaign, e `{{campaign.${message_name}}}` é o nome da sua variante de mensagem.
{% endraw %}

Para uso em URLs e strings de consulta (por exemplo, quando um nome contém `%` ou espaços), consulte [Nomes de Campaigns em URLs]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags#campaign-names-in-urls).

### Como uso Liquid com objetos aninhados? {#how-do-i-use-liquid-with-nested-objects}

A Braze tem um recurso integrado que gera código Liquid para Segments que podem ser usados em uma mensagem. Especificamente, você pode criar um Segment que corresponda a vários critérios em um objeto.

Para saber mais, confira [Segmentação com múltiplos critérios]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support#segmentation-behavior-with-arrays-of-objects).

### Como uso propriedades de eventos para personalizar uma mensagem que um evento está disparando? {#how-do-i-use-event-attributes-to-personalize-a-message-that-an-event-is-triggering}

{% raw %}
Você pode acessar propriedades de eventos disparados por API com a tag `api_triggered_property`: `{{api_trigger_properties.${attribute_key}}}`.
{% endraw %}

### A Braze suporta um array de arrays em Liquid? {#does-braze-support-an-array-of-arrays-in-liquid}

O Liquid não suporta nativamente arrays de arrays. Armazene os valores como um array de strings separadas por vírgula e use o filtro `split` para analisá-los quando necessário.

## Variáveis e sintaxe {#variables-and-syntax}

### Como atribuir variáveis com Liquid? {#how-do-i-assign-variables-with-liquid}

Você pode criar e atribuir variáveis usando a tag `assign`. Isso cria uma variável no criador de mensagem que também pode ser referenciada ao longo da sua mensagem.

### Quando devo usar `assign` versus `capture`? {#when-should-i-use-assign-versus-capture}

Tanto `assign` quanto `capture` criam variáveis Liquid, mas servem a propósitos diferentes:

- `assign` é para variáveis simples que armazenam um único valor, como um booleano, número ou string simples. Você também pode aplicar um único filtro na mesma linha.
- `capture` é para armazenar um bloco de texto que pode incluir múltiplas variáveis, strings ou expressões complexas.

Use `capture` quando o valor for complexo demais para uma única instrução `assign`, como URLs que usam outras variáveis Liquid ou atributos personalizados como parâmetros. `capture` também é preferido ao implementar variáveis Liquid no corpo de chamadas de Connected Content.

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

### As variáveis Liquid são compartilhadas entre a linha de assunto e o corpo? {#do-liquid-variables-carry-between-subject-line-and-body}

Não. A Braze renderiza cada componente da mensagem separadamente (como linha de assunto, corpo HTML, pré-cabeçalho e título do push). Atribuições ou capturas feitas em um campo não ficam disponíveis em outro. Repita o Liquid ou a chamada de Connected Content em cada campo que precisar do valor.

### O que é a lógica de loop for e como posso usá-la? {#what-is-for-loop-logic-and-how-can-i-use-it}

Loops for também são conhecidos como [tags de iteração](https://shopify.github.io/liquid/tags/iteration/). Usar a lógica de loop for nos seus snippets Liquid permite percorrer blocos de Liquid até que uma condição seja atendida.

Na Braze, isso pode ser usado para verificar itens em um atributo personalizado de array, ou uma lista de valores e objetos retornados por um [catálogo]({{site.baseurl}}/user_guide/data/activation/catalogs), [seleção]({{site.baseurl}}/user_guide/data/activation/catalogs/selections) ou resposta de chamada de [Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content). Especificamente, você pode usar a lógica de loop for como parte do seu envio de mensagens para verificar se um produto está em estoque ou se um produto tem uma avaliação mínima.

Por exemplo, digamos que você tenha um catálogo chamado "Games" com uma seleção chamada "cheap_games". Para obter os títulos dos jogos em "cheap_games", você pode usar este snippet Liquid:

{% raw %}
```liquid
{% catalog_selection_items Games cheap_games %}
{% for item in items %}
 Get this game: {{ item.title }}
{% endfor %}
```
{% endraw %}

Quando as condições definidas forem atendidas, sua mensagem pode prosseguir. Usar essa lógica é uma forma útil de economizar tempo, em vez de repetir blocos Liquid para diferentes condições.

### O que é a lógica de interrupção e como posso usá-la? {#what-is-abort-logic-and-how-can-i-use-it}

A lógica de interrupção permite impedir que uma mensagem seja enviada se as condições forem atendidas. Isso é especialmente útil para evitar que mensagens incompletas sejam enviadas aos seus usuários. Para exemplos de lógica de interrupção nas suas Campaigns de marketing, leia mais em [Interrompendo mensagens]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages).

### Posso usar Liquid dentro da tag `abort_message`? {#can-i-use-liquid-inside-the-abort_message-tag}

Não. A tag {% raw %}`{% abort_message %}`{% endraw %} aceita uma string estática entre aspas, não personalização Liquid. Use outra lógica Liquid antes da tag se precisar de um comportamento de interrupção condicional.

### Como mascarar números de telefone com Liquid? {#how-do-i-mask-phone-numbers-with-liquid}

Você pode mascarar números de telefone usando o filtro `slice` para extrair dígitos específicos e o filtro `append` para combiná-los com caracteres de máscara.

#### Mascarar todos os dígitos exceto os últimos quatro {#mask-all-but-the-last-four-digits}

Para exibir um número de telefone de 10 dígitos como `******7890`:

{% raw %}
```liquid
{% assign phone = {{${phone_number}}} | split: '' %}
{% assign masked_phone = '' %}
{% for i in (0..5) %}
  {% assign masked_phone = masked_phone | append: '*' %}
{% endfor %}
{% for i in (6..9) %}
  {% assign masked_phone = masked_phone | append: phone[i] %}
{% endfor %}
{{ masked_phone }}
```
{% endraw %}

#### Mostrar os três primeiros e os últimos quatro dígitos {#show-the-first-three-and-last-four-digits}

Para exibir um número de telefone de 10 dígitos como `123***7890`:

{% raw %}
```liquid
{% assign first_part = {{${phone_number}}} | slice: 0, 3 %}
{% assign last_part = {{${phone_number}}} | slice: -4, 4 %}
{% assign masked_phone_number = first_part | append: "***" | append: last_part %}
{{ masked_phone_number }}
```
{% endraw %}

## Canvas, catálogos e propriedades de disparo {#canvas-catalogs-and-trigger-properties}

### Por que meu Liquid disparado por API está falhando na Braze? {#why-is-my-api-triggered-liquid-failing-in-braze}

{% raw %}
Um par extra de chaves é uma causa comum. Por exemplo, `{{{api_trigger_properties.${attribute_key}}}}` não é uma sintaxe de personalização válida na Braze. Use exatamente duas chaves de abertura e duas de fechamento: `{{api_trigger_properties.${attribute_key}}}`.
{% endraw %}

### Existem limites de tamanho para propriedades de contexto do Canvas? {#are-there-size-limits-for-canvas-context-properties}

A Braze não impõe um limite rígido para [propriedades de contexto do Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties), mas mantenha as cargas úteis abaixo de aproximadamente 1 KB (~1.000 caracteres). Objetos maiores podem aumentar o uso de memória e atrasar a renderização de mensagens durante envios de alto volume.

### Por que recebo um erro de Liquid ao visualizar certos tipos de dados no dashboard? {#why-do-i-get-a-liquid-error-when-previewing-certain-data-types-in-the-dashboard}

Alguns tipos de [propriedade de contexto do Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties) exigem coerção em Liquid antes de serem usados em comparações ou operações matemáticas. Por exemplo, quando você precisa de comportamento numérico:

{% raw %}
```liquid
{{context.${property_name} | plus: 0}}
```
{% endraw %}

### Por que meu snippet de Liquid de catálogo retorna uma mensagem de interrupção? {#why-does-my-catalog-liquid-snippet-return-an-abort-message}

Se um snippet de Liquid de catálogo for interrompido durante o envio, recrie o snippet a partir do menu de personalização selecionando itens individuais do catálogo em vez de usar uma seleção em massa ou totalmente dinâmica. Consulte [Catálogos]({{site.baseurl}}/user_guide/data/activation/catalogs) e [Seleções]({{site.baseurl}}/user_guide/data/activation/catalogs/selections).

## Content Blocks e o criador de mensagens {#content-blocks-and-the-message-composer}

### Por que há espaçamento extra em mensagens que usam Content Blocks? {#why-is-there-extra-spacing-in-messages-that-use-content-blocks}

Se você notar espaçamento extra em mensagens enviadas que usam Content Blocks com Liquid, pode haver quebras de parágrafo ou de linha desnecessárias dentro das suas instruções condicionais. Escreva suas instruções condicionais em uma única linha, em vez de distribuí-las em várias linhas.

#### Exemplo {#example}

{% raw %}
```liquid
{% if {{custom_attribute.${has_discount}}} == true %}Discounted Item{% elsif {{custom_attribute.${is_new_arrival}}} == true %}New Arrival{% else %}Regular Item{% endif %}
```
{% endraw %}


### Por que o Liquid em várias linhas cria espaços em branco inesperados nos editores de arrastar e soltar? {#why-does-multi-line-liquid-create-unexpected-whitespace-in-the-drag-and-drop-editors}

Quando o código Liquid é distribuído em várias linhas no editor de arrastar e soltar de mensagens no app ou no editor de arrastar e soltar de e-mail, cada bloco {% raw %}`{% %}`{% endraw %} é renderizado como texto não visível. As quebras de linha são preservadas como linhas vazias antes da saída visível, causando espaços em branco inesperados.

#### Solução 1: usar tags de controle de espaço em branco (recomendado) {#solution-1-use-whitespace-control-tags-recommended}

Adicione hifens dentro dos delimitadores de tag para remover os espaços em branco ao redor, mantendo o código legível:

{% raw %}
```liquid
{%- assign event_date = {{custom_attribute.${PreferredPickupDate}}} | date: "%s" -%}
{%- assign today = 'now' | date: "%s" -%}
{%- assign difference = event_date | minus: today -%}
{%- assign difference_days = difference | divided_by: 86400 -%}
Only {{ difference_days }} days until your move!
```
{% endraw %}

#### Solução 2: consolidar o Liquid em uma única linha {#solution-2-consolidate-liquid-onto-a-single-line}

Remova todas as quebras de linha para que o Liquid fique em uma linha contínua:

{% raw %}
```liquid
{% assign event_date = {{custom_attribute.${PreferredPickupDate}}} | date: "%s" %}{% assign today = 'now' | date: "%s" %}{% assign difference = event_date | minus: today %}{% assign difference_days = difference | divided_by: 86400 %}Only {{ difference_days }} days until your move!
```
{% endraw %}

Ambas as abordagens evitam linhas vazias indesejadas na mensagem renderizada. Isso se aplica ao editor de arrastar e soltar de mensagens no app, ao editor de arrastar e soltar de e-mail e a Content Blocks com Liquid. Para saber mais, consulte [Controle de espaço em branco](https://shopify.github.io/liquid/basics/whitespace/).

### Por que meu Content Block não aparece em **Row** na ferramenta de busca do editor de arrastar e soltar? {#why-is-my-content-block-missing-from-row-in-the-drag-and-drop-search-tool}

Alguns Content Blocks não aparecem em **Row** na busca do editor de arrastar e soltar. Adicione um bloco HTML a partir da guia **Content** (**Advanced**) e, em seguida, insira a Liquid tag do Content Block nesse bloco HTML para renderizar o conteúdo do bloco.

### Por que a prévia do meu Content Block de arrastar e soltar é diferente da visualização de composição? {#why-does-my-drag-and-drop-content-block-preview-differ-from-the-compose-view}

Quando você usa um modelo de Content Block com Liquid, as media queries para dispositivos móveis no bloco podem não ser aplicadas na prévia da mesma forma que quando você arrasta o bloco diretamente para uma mensagem. Arrastar o bloco preserva o layout, mas o desvincula do bloco de origem, de modo que edições futuras no bloco não atualizam mais a mensagem automaticamente.

### Como faço para visualizar valores de propriedades de eventos no criador de mensagens? {#how-do-i-preview-event-property-values-in-message-composer}

Use **Preview as Custom User** e insira valores de amostra de propriedades de eventos personalizados para o usuário que você está visualizando. Isso também é útil para mensagens com lógica de interrupção quando você precisa de valores de prévia que não disparem uma interrupção.

## Liquid em mensagens de e-mail {#liquid-in-email-messages}

### Por que minha mensagem é interrompida com "Invalid from email address for recipient:"? {#why-does-my-message-abort-with-invalid-from-email-address-for-recipient}

Essa interrupção ocorre quando o Liquid no endereço **De** produz uma sintaxe inválida, como uma variável ausente, espaços extras ou caracteres não permitidos. Visualize com um usuário teste e verifique se o endereço **De** renderizado corresponde ao domínio de envio configurado.

### Como criar um endereço de resposta dinâmico? {#how-do-i-create-a-dynamic-reply-to-address}

Use Liquid no campo **Responder para** quando seu espaço de trabalho suportar configuração dinâmica de endereço de resposta. Combine com as configurações de nome de exibição do **De** conforme necessário. Consulte [Configurações de e-mail]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences) para opções específicas do espaço de trabalho.

## Solução de problemas de erros de Liquid {#troubleshooting-liquid-errors}

### Por que meu código Liquid não funciona mesmo parecendo correto? {#why-is-my-liquid-code-not-working-when-it-looks-correct}

Se o seu código Liquid parece sintaticamente correto, mas não está funcionando, verifique se há aspas inteligentes (aspas curvas como `' '` ou `" "`) e travessões inteligentes (travessões longos como `—`) em vez de aspas retas (`' '` ou `" "`) e hifens (`-`). O Liquid reconhece apenas caracteres ASCII retos, então aspas e travessões inteligentes causarão erros de análise.

Isso acontece frequentemente quando a configuração de teclado do macOS **Usar aspas e travessões inteligentes** está ativada, o que converte automaticamente os caracteres enquanto você digita no dashboard da Braze.

Para desativar essa configuração no macOS:

1. Acesse **Ajustes do Sistema** > **Teclado** > **Entrada de Texto** > **Editar**.
2. Desmarque **Usar aspas e travessões inteligentes**.

| Exemplo | Aspas curvas (não funciona) | Aspas retas (funciona) |
| --- | --- | --- |
| Valor padrão | {% raw %}`{{${first_name} | default: 'Torchie'}}`{% endraw %} | {% raw %}`{{${first_name} | default: 'Torchie'}}`{% endraw %} |
| Condicional | {% raw %}`{% if ${country} contains 'US' %}`{% endraw %} | {% raw %}`{% if ${country} contains 'US' %}`{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Exemplos de aspas inteligentes" }

Isso se aplica a valores padrão, condicionais e qualquer outro Liquid que use aspas. Aspas curvas e retas podem parecer iguais na tela, então compare seu código com cuidado ou cole-o em um editor de texto simples.

Para saber mais sobre o uso de aspas no Liquid, consulte [Sintaxe do Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid#liquid-syntax).

### Por que estou vendo o erro de Liquid "Unexpected end token"? {#why-am-i-seeing-an-unexpected-end-token-liquid-error}

Esse erro geralmente indica chaves extras ou ausentes. Não aninhe {% raw %}`{{ }}`{% endraw %} dentro de outra expressão de tag Liquid. Por exemplo, use {% raw %}`{{custom_attribute.${date_of_birth} | date: '%s'}}`{% endraw %} em vez de envolver a referência do atributo em um par adicional de chaves.

### Por que a tentativa de reconexão do Connected Content não está disponível para minha mensagem no app? {#why-is-connected-content-retry-unavailable-for-my-in-app-message}

{% raw %}
A tag `{% connected_content %}` com tentativa de reconexão não é compatível com todos os tipos de mensagem, incluindo alguns formatos de mensagem no app. Remova os parâmetros de tentativa de reconexão ou use um canal compatível para chamadas de Connected Content com nova tentativa.
{% endraw %}

### Por que estou vendo "Liquid Error: Comparison of Time with String Failed"? {#why-am-i-seeing-liquid-error-comparison-of-time-with-string-failed}

Esse erro ocorre ao comparar um atributo personalizado de tempo ou uma propriedade de evento diretamente com um valor em branco (uma string vazia). O Liquid não suporta comparações diretas entre tipos de dados diferentes, como um objeto de tempo e uma string.

A seguir, um exemplo comum que causa esse erro:

{% raw %}
```liquid
{% if {{custom_attribute.${expiration_date}}} == blank %}
  <a>Some words</a>
{% endif %}
```
{% endraw %}

Isso falha porque não é possível comparar um atributo personalizado com tipo de dados de tempo com uma string (`blank`).

Para resolver, converta o atributo de tempo em uma string atribuindo-o a uma variável e usando o filtro `default` quando o atributo for avaliado como em branco no momento da renderização:

{% raw %}
```liquid
{% assign expiration_date = {{custom_attribute.${expiration_date}}} | default: "" %}

{% if expiration_date == blank %}
  <a>Example Words</a>
{% endif %}
```
{% endraw %}


Ao comparar um atributo personalizado de tempo com a hora atual ou datas futuras, use a mesma abordagem:

{% raw %}
```liquid
{% assign today = 'now' | date: '%s' %}
{% assign month = 'now' | date: '%s' | plus: 2592000 %}
{% assign expiration_date = {{custom_attribute.${expiration_date}}} | default: "" %}

{% if expiration_date == blank %}
  <a>Example Words</a>
{% elsif expiration_date >= today and expiration_date >= month %}
  <a>More Words</a>
{% endif %}
```
{% endraw %}