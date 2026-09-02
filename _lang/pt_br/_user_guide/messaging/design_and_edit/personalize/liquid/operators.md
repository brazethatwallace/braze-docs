---
nav_title: Operadores
article_title: Operadores Liquid
page_order: 2
description: "Esta página de referência apresenta os operadores compatíveis com Liquid, além de exemplos relevantes."

---

# Operadores {#operators}

> Liquid é compatível com muitos [operadores](https://docs.shopify.com/themes/liquid/basics/operators) que podem ser usados em suas instruções condicionais. Esta página aborda os operadores compatíveis com Liquid e apresenta casos de uso de como você pode utilizá-los em suas mensagens.

Esta tabela lista os operadores compatíveis. Observe que parênteses são caracteres inválidos em Liquid e impedem que suas tags funcionem.

| Sintaxe | Descrição do operador |
|---------|-----------|
| ==  | igual a        |
| !=  | diferente de|
|  >  | maior que  |
| <   | menor que     |
| >=| maior ou igual a|
| <= | menor ou igual a |
| or | condição A ou condição B|
| and | condição A e condição B|
| contains | verifica se uma string ou array de strings contém uma string|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Operadores" }

{% alert note %}
Os operadores podem ser usados em instruções condicionais (`if`, `elsif`, `unless`), mas não em instruções `assign`, loops `for` ou colchetes de acesso a arrays. Nas tags `case` e `when`, cada Branch or ramificação or ramificação compara a expressão `case` com um valor `when` usando igualdade, em vez de expressões arbitrárias com operadores. Para exemplos, consulte [Lógica condicional de mensagens]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic#case-and-when). Para uma explicação completa, consulte [Onde usar operadores e filtros]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid#where-to-use-operators-and-filters).
{% endalert %}

## Agrupando condições sem parênteses {#grouping-conditions-without-parentheses}

Liquid não é compatível com parênteses para agrupar expressões. Para avaliar lógica booleana complexa como `(a and b) or c`, use instruções `if` aninhadas ou variáveis intermediárias.

Por exemplo, para verificar se um valor satisfaz uma condição composta, atribua uma variável intermediária:

{% raw %}
```liquid
{% assign qualifies = false %}
{% if points > 100 %}
{% assign qualifies = true %}
{% elsif points == 100 and member_level == 'gold' %}
{% assign qualifies = true %}
{% endif %}

{% if qualifies %}
You qualify for a reward!
{% endif %}
```
{% endraw %}

## Tutoriais {#tutorials}

Vamos ver alguns tutoriais para aprender a usar esses operadores em suas campanhas de marketing:

### Escolher uma mensagem com um atributo personalizado de número inteiro {#choose-a-message-with-an-integer-custom-attribute}

Vamos enviar notificações por push com descontos promocionais personalizados para usuários que fizeram ou não compras. A notificação por push usará um atributo personalizado de número inteiro chamado `total_spend` para verificar o gasto total de um usuário.

1. Escreva uma instrução condicional usando o operador maior que (`>`) para verificar se o gasto total do usuário é maior que `0`, indicando que ele fez uma compra. Em seguida, crie uma mensagem para enviar a esses usuários.

{% raw %}
```liquid
{% if {{custom_attribute.${total_spend}}} >0 %}
Surprise! We added a 15% discount code to your account that automatically applies to your next order.
```
{% endraw %}

{: start="2"}
2. Adicione a tag {% raw %}`{% else %}`{% endraw %} para capturar usuários cujo gasto total é igual a `0` ou não existe. Em seguida, crie uma mensagem para enviar a esses usuários.

{% raw %}
```liquid
{% else %}
Need a sign to update your wardrobe? We added a 15% discount code to your account that will automatically apply to your first order.
```
{% endraw %}

{: start="3"}
3. Feche a lógica condicional com a tag {% raw %}`{% endif %}`{% endraw %}.

{% raw %}
```liquid
{% endif %}
```
{% endraw %}

![Criador de notificação por push com o código Liquid completo do tutorial.]({% image_buster /assets/img/liquid-if-totalspend.png %}){: width="100%"}

{% details Código Liquid completo %}
{% raw %}
```liquid
{% if {{custom_attribute.${total_spend}}} >0 %}
Surprise! We added a 15% discount code to your account that automatically applies to your next order.
{% else %}
Need a sign to update your wardrobe? We added a 15% discount code to your account that will automatically apply to your first order.
{% endif %}
```
{% endraw %}
{% enddetails %}

Agora, se o atributo personalizado "Total Spend" de um usuário for maior que `0`, ele receberá a mensagem:

```
Surprise! We added a 15% discount code to your account that automatically applies to your next order.
```
Se o atributo personalizado "Total Spend" de um usuário não existir ou for igual a `0`, ele receberá a seguinte mensagem:

```
Need a sign to update your wardrobe? We added a 15% discount code to your account that will automatically apply to your first order.
```

### Escolher uma mensagem com um atributo personalizado de string {#choose-a-message-with-a-string-custom-attribute}

Vamos enviar notificações por push para os usuários e personalizar a mensagem com base no jogo mais recente de cada um. Isso usará um atributo personalizado de string chamado `recent_game` para verificar qual jogo o usuário jogou por último.

1. Escreva uma instrução condicional usando o operador igual a (`==`) para verificar se o jogo mais recente do usuário é *Awkward Dinner Party*. Em seguida, crie uma mensagem para enviar a esses usuários.

{% raw %}
```liquid
{% if {{custom_attribute.${recent_game}}} == 'Awkward Dinner Party' %}
You are formally invited to our next dinner party. Log on next week for another round of delectable dishes and curious conversations.
```
{% endraw %}

{: start="2"}
2. Use a tag `elsif` com o operador igual a (`==`) para verificar se o jogo mais recente do usuário é *Proxy War 3: War of Thirst*. Em seguida, crie uma mensagem para enviar a esses usuários.

{% raw %}
```liquid
{% elsif {{custom_attribute.${recent_game}}} == 'Proxy War 3: War of Thirst' %}
Your fleet awaits your next orders. Log on when you're ready to rejoin the war for hydration.
```
{% endraw %}

{: start="3"}
3. Use a tag `elsif` com os operadores "diferente de" (`!=`) e "e" (`and`) para verificar se o usuário tem um jogo recente (ou seja, o valor não está em branco) e se o jogo não é *Awkward Dinner Party* nem *Proxy War 3: War of Thirst*. Em seguida, crie uma mensagem para enviar a esses usuários.

{% raw %}
```liquid
{% elsif {{custom_attribute.${recent_game}}} != blank and {{custom_attribute.${recent_game}}} != 'Awkward Dinner Party' and {{custom_attribute.${recent_game}}} != 'Proxy War 3: War of Thirst' %}
Limited Time Deal! Get 15% off our best-selling classics!
```
{% endraw %}

{: start="4"}
4. Adicione a tag {% raw %}`{% else %}`{% endraw %} para capturar usuários que não têm um jogo recente. Em seguida, crie uma mensagem para enviar a esses usuários.

{% raw %}
```liquid
{% else %}
Hey! I've got a deal for you. Buy 2 of our newest releases and get 10% off!
```
{% endraw %}

{: start="5"}
5. Feche a lógica condicional com a tag {% raw %}`{% endif %}`{% endraw %}.

{% raw %}
```liquid
{% endif %}
```
{% endraw %}

{% details Código Liquid completo %}
{% raw %}
```liquid
{% if {{custom_attribute.${recent_game}}} == 'Awkward Dinner Party' %}
You are formally invited to our next dinner party. Log on next week for another round of delectable dishes and curious conversations.
{% elsif {{custom_attribute.${recent_game}}} == 'Proxy War 3: War of Thirst' %}
Your fleet awaits your next orders. Log on when you're ready to rejoin the war for hydration.
{% elsif {{custom_attribute.${recent_game}}} != blank and {{custom_attribute.${recent_game}}} != 'Awkward Dinner Party' and {{custom_attribute.${recent_game}}} != 'Proxy War 3: War of Thirst' %}
Limited Time Deal! Get 15% off our best-selling classics!
{% else %}
Hey! I've got a deal for you. Buy 2 of our newest releases and get 10% off!
{% endif %}
```
{% endraw %}
{% enddetails %}

![Criador de notificação por push com o código Liquid completo do tutorial.]({% image_buster /assets/img/liquid-if-elsif-games.png %})

Agora, se o último jogo do usuário foi *Awkward Dinner Party*, ele receberá esta mensagem:

```
You are formally invited to our next dinner party. Log on next week for another round of delectable dishes and curious conversations.
```

Se o jogo mais recente do usuário for *Proxy War 3: War of Thirst*, ele receberá esta mensagem:

```
Your fleet awaits your next orders. Log on when you're ready to rejoin the war for hydration.
```

Se o usuário jogou recentemente um jogo que não era *Awkward Dinner Party* nem *Proxy War 3: War of Thirst*, ele receberá esta mensagem:

```
Limited Time Deal! Get 15% off our best-selling classics!
```

Se o usuário não jogou nenhum jogo ou se esse atributo personalizado não existe no perfil dele, ele receberá esta mensagem:

```
Hey! I've got a deal for you. Buy 2 of our newest releases and get 10% off!
```

### Cancelar mensagem com base no local {#abort-message-based-on-location}

Você pode cancelar uma mensagem com base em praticamente qualquer coisa. Vamos cancelar uma mensagem se o usuário não estiver em uma área específica, já que ele pode não se qualificar para a promoção, evento ou entrega.

1. Escreva uma instrução condicional usando o operador igual a (`==`) para verificar se o fuso horário do usuário é `America/Los_Angeles` e, em seguida, crie uma mensagem para enviar a esses usuários.

{% raw %}
```liquid
{% if {{${time_zone}}} == 'America/Los_Angeles' %}
Stream now!
```
{% endraw %}

{: start="2"}
2. Para evitar o envio de mensagens a usuários fora do fuso horário `America/Los_Angeles`, envolva as tags {% raw %}`{% else %}`{% endraw %} e {% raw %}`{% endif %}`{% endraw %} ao redor de uma tag {% raw %}`{% abort_message () %}`{% endraw %}.

{% raw %}
```liquid
{% else %}
{% abort_message () %}
{% endif %}
```
{% endraw %}

{% details Código Liquid completo %}
{% raw %}
```liquid
{% if {{${time_zone}}} =='America/Los_Angeles' %}
Stream now!
{% else %}
{% abort_message () %}
{% endif %}
```
{% endraw %}
{% enddetails %}

![Criador de notificação por push com o código Liquid completo do tutorial.]({% image_buster /assets/img/abort-if.png %})

Você também pode [cancelar mensagens]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/aborting_connected_content) com base em Conteúdo Conectado.

## Solução de problemas {#troubleshooting}

### O envio de teste não chega ao usar `abort_message` {#test-send-doesnt-arrive-when-using-abort_message}

Se você usar [`abort_message`]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages) e um envio de teste nunca chegar, o usuário de prévia pode estar sem os atributos que seu Liquid espera. A lógica de interrupção é executada durante a renderização; quando ela é acionada, a Braze não envia a mensagem. Faça a prévia com um usuário que tenha os dados de perfil necessários ou use **Pré-visualizar como usuário** para testar campos de destinatário que forneçam os mesmos valores que seu público de produção teria.

### A prévia pode converter incorretamente os tipos de propriedade {#preview-may-incorrectly-coerce-property-types}

Ao pré-visualizar uma mensagem no dashboard, a maioria das variáveis (como atributos personalizados) é convertida para o tipo correto. No entanto, algumas variáveis não têm um tipo definido que a prévia possa consultar:

- `api_trigger_properties`
- `canvas_entry_properties`
- `context`

Para essas propriedades, a prévia tenta inferir o tipo a partir do valor. Isso significa que um valor que você pretende que seja uma **string** pode ser interpretado incorretamente como um **número**. Por exemplo, se o valor de uma propriedade for a string `"3"`, a prévia pode convertê-lo para o inteiro `3`, o que pode causar comportamento inesperado em operações de string como `contains` ou `split`.

Se você observar resultados inesperados na prévia ao usar esses tipos de propriedade, lembre-se de que a inferência de tipo da prévia pode não corresponder ao que acontece no momento do envio. No momento do envio, os tipos de dados reais do evento de disparo ou da chamada de API or interface de programação do aplicativo (API) são preservados.

Para forçar um tipo específico na prévia, você pode converter explicitamente o valor:

{% raw %}
```liquid
{% comment %} Force a value to be treated as a number {% endcomment %}
{% assign orders = {{canvas_entry_properties.${number_of_orders}}} | plus: 0 %}

{% comment %} Force a value to be treated as a string {% endcomment %}
{% assign code = {{api_trigger_properties.${promo_code}}} | append: "" %}
```
{% endraw %}