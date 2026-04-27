---
nav_title: Lógica condicional de mensagens
article_title: Lógica condicional de mensagens com Liquid
page_order: 6
description: "Este artigo de referência aborda como as tags podem e devem ser usadas nas suas campanhas."

---

# Lógica condicional de mensagens

> As [tags](https://docs.shopify.com/themes/liquid-documentation/tags) permitem incluir lógica de programação nas suas campanhas de mensagens. As tags podem ser usadas para executar instruções condicionais, bem como para casos de uso avançados, como atribuir variáveis ou iterar por um bloco de código. <br><br>Esta página aborda como as tags podem e devem ser usadas, como lidar com valores de atributos nulos, nil e em branco, e como referenciar atributos personalizados.

## Formatação de tags

{% raw %}
Uma tag deve estar envolvida em `{% %}`.
{% endraw %}

Para facilitar um pouco a sua vida, a Braze incluiu formatação de cores que será ativada em verde e roxo se você tiver formatado corretamente a sintaxe Liquid. A formatação verde ajuda a identificar tags, enquanto a formatação roxa destaca áreas que contêm personalização.

Se estiver com dificuldade para usar mensagens condicionais, tente escrever a sintaxe condicional antes de inserir seus atributos personalizados e outros elementos Liquid.

Por exemplo, adicione o seguinte no campo de mensagem primeiro:
{% raw %}
```liquid
{% if X >0 %}
{% else %}
{% endif %}
```

Certifique-se de que ele fique destacado em verde e, em seguida, substitua o `X` pelo Liquid ou Conteúdo conectado escolhido usando o `+` azul no canto do campo de mensagem, e o `0` pelo valor desejado.
<br><br>
Depois, adicione suas variações de mensagem conforme necessário entre as condicionais `else`:
```liquid
{% if {{custom_attribute.${total_spend}}} >0 %}
Thanks for purchasing! Here's another 10% off!
{% else %}
Buy now! Would 5% off convince you?
{% endif %}
```
{% endraw %}

## Lógica condicional

Você pode incluir muitos tipos de [lógica inteligente nas mensagens](http://docs.shopify.com/themes/liquid-documentation/basics), como uma instrução condicional. O exemplo a seguir usa [condicionais](http://docs.shopify.com/themes/liquid-documentation/tags/control-flow-tags) para internacionalizar uma campanha:
{% raw %}

```liquid
{% if ${language} == 'en' %}
This is a message in English from Braze!
{% elsif ${language} == 'es' %}
Este es un mensaje en español de Braze !
{% elsif ${language} == 'zh' %}
这是一条来自Braze的中文消息。
{% else %}
This is a message from Braze! This is going to go to anyone who did not match the other specified languages!
{% endif %}
```

### Tags condicionais

#### `if` e `elsif`

A lógica condicional começa com a tag `if`, que define a primeira condição a ser verificada. As condições subsequentes usam a tag `elsif` e serão verificadas se as condições anteriores não forem atendidas. Neste exemplo, se o dispositivo de um usuário não estiver configurado para inglês, o código verificará se o dispositivo está configurado para espanhol e, se isso falhar, verificará se está configurado para chinês. Se o dispositivo do usuário atender a uma dessas condições, o usuário receberá uma mensagem no idioma correspondente.

#### `else`

Você tem a opção de incluir uma instrução `{% else %}` na sua lógica condicional. Se nenhuma das condições definidas for atendida, a instrução `{% else %}` especifica a mensagem que deve ser enviada. Neste exemplo, o padrão é inglês se o idioma do usuário não for inglês, espanhol ou chinês.

#### `endif`

A tag `{% endif %}` sinaliza que você terminou sua lógica condicional. Você deve incluir a tag `{% endif %}` em qualquer mensagem com lógica condicional. Se você não incluir uma tag `{% endif %}` na sua lógica condicional, receberá um erro, pois a Braze não conseguirá processar sua mensagem.

{% alert note %}
As tags condicionais (`if`, `elsif`, `unless`) suportam operadores, mas não filtros. Para avaliar um valor filtrado em uma condicional, atribua o resultado do filtro a uma variável primeiro e depois referencie essa variável. Para mais detalhes, consulte [Onde usar operadores e filtros]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid/#where-to-use-operators-and-filters).
{% endalert %}

### Tutorial: Entregar conteúdo baseado em localização

Ao concluir este tutorial, você será capaz de usar tags com instruções "if", "elsif" e "else" para entregar conteúdo com base na localização do usuário.

1. Comece com uma tag `if` para definir qual mensagem deve ser enviada quando a cidade do usuário for Nova York. Se a cidade do usuário for Nova York, essa primeira condição é atendida e o usuário receberá uma mensagem identificando-o como nova-iorquino.

```liquid
{% if ${city} == "New York" %}
  🎉 Hey there, New Yorker! We're excited to offer you a special deal!
  Get 20% off your next sandwich at your local Sandwich Emperor.
  Just show this message at the counter to redeem your offer!
```

{: start="2"}
2. Em seguida, use a tag `elseif` para definir qual mensagem deve ser enviada se a cidade do usuário for Los Angeles.

```liquid
{% elsif ${city} == "Los Angeles" %}
  🌞 Hello, Los Angeles! Enjoy a sunny day with a delicious sandwich!
  Present this message at our LA restaurant for a 20% discount on your next order!
```

{: start="3"}
3. Vamos usar outra tag `elseif` para definir qual mensagem deve ser enviada se a cidade do usuário for Chicago.

```liquid
{% elsif ${city} == "Chicago" %}
  🍕 Chicago, we have a treat for you!
  Swing by our restaurant and get 20% off your favorite sandwich.
  Just show this message to our staff!
```

{: start="4"}
4. Agora, vamos usar a tag `{% else %}` para especificar qual mensagem deve ser enviada se a cidade do usuário não for San Francisco, Nova York ou Chicago.

```liquid
{% else %}
 🥪 Craving a sandwich? Visit us at any of our locations for a delicious meal!
  Check our website for the nearest restaurant to you!
```

{: start="5"}
5. Por fim, usaremos a tag `{% endif %}` para indicar que nossa lógica condicional está concluída.

```liquid
{% endif %}
```

{% endraw %}

{% details Código Liquid completo %}

{% raw %}
```liquid
{% if ${city} == "New York City" %}
  🎉 Hey there, New Yorker! We're excited to offer you a special deal!
  Get 20% off your next sandwich at our New York location.
  Just show this message at the counter to redeem your offer!
{% elsif ${city} == "Los Angeles" %}
  🌞 Hello, Los Angeles! Enjoy a sunny day with a delicious sandwich!
  Present this message at our LA restaurant for a 20% discount on your next order!
{% elsif ${city} == "Chicago" %}
  🍕 Chicago, we have a treat for you!
  Swing by our restaurant and get 20% off your favorite sandwich.
  Just show this message to our staff!
{% else %}
  🥪 Craving a sandwich? Visit us at any of our locations for a delicious meal!
  Check our website for the nearest restaurant to you!
{% endif %}
```
{% endraw %}

{% enddetails %}

## Lidando com valores de atributos nulos, nil e em branco

A lógica condicional é uma forma útil de lidar com valores de atributos que não estão definidos nos perfis de usuário.

### Valores de atributos nulos e nil

Um valor nulo ou nil ocorre quando o valor de um atributo personalizado não foi definido. Por exemplo, um usuário que ainda não definiu seu nome não terá um nome registrado na Braze.

Em algumas circunstâncias, você pode querer enviar uma mensagem completamente diferente para usuários que têm um nome definido e para usuários que não têm.

A tag a seguir permite especificar uma mensagem para usuários com um atributo "nome" nulo:

{% raw %}
```liquid
{% if ${first_name} == null %}
  ....
{% endif %}
```
{% endraw %}

![Exemplo de mensagem no dashboard da Braze, usando um atributo "nome" nulo.]({% image_buster /assets/img/value_null.png %}){: style="max-width:60%;"}

{% raw %}
```liquid
{% if ${first_name} == null %}
We're having a sale! Hurry up and get 10% off all items today only!
{% else %}
Hey {{${first_name} | default: 'there'}}, we're having a sale! Hurry up and get 10% off all items today only!
{% endif %}
```

Observe que um valor de atributo nulo não está estritamente associado a um tipo de valor (por exemplo, uma string "nula" é o mesmo que um array "nulo"). Portanto, no exemplo acima, o valor de atributo nulo faz referência a um nome não definido, que seria uma string.

{% endraw %}

### Valores de atributos em branco

Um valor em branco ocorre quando o atributo em um perfil de usuário não está definido, está definido com uma string de espaço em branco (` `) ou está definido como `false`. Valores em branco devem ser verificados antes de outras variáveis para evitar um erro de processamento Liquid.

A tag a seguir permite especificar uma mensagem para usuários que têm um atributo "nome" em branco.

{% raw %}
```liquid
{% if ${first_name} == blank %}
  ....
{% endif %}
```
{% endraw %}

## Referenciando atributos personalizados

Depois de [criar atributos personalizados]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/#managing-custom-attributes), você pode referenciar esses atributos personalizados nas suas mensagens Liquid.

Ao usar lógica condicional, você precisará saber o tipo de dados do atributo personalizado para garantir que está usando a sintaxe correta. Na página **Atributos personalizados** no dashboard, procure o tipo de dados associado ao seu atributo personalizado e consulte os exemplos a seguir listados para cada tipo de dados.

![Selecionando um tipo de dados para um atributo personalizado. O exemplo mostra um atributo Favorite_Category com tipo de dados string.]({% image_buster /assets/img_archive/custom_attribute_data_type.png %}){: style="max-width:80%;"}

{% alert tip %}
Strings e arrays exigem apóstrofos retos ao redor deles, enquanto booleanos e inteiros nunca terão apóstrofos.
{% endalert %}

#### Booleano

[Booleanos]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/#booleans) são valores binários e podem ser definidos como `true` ou `false`, como `registration_complete: true`. Valores booleanos não têm apóstrofos ao redor deles.

{% raw %}

```liquid
{% if {{custom_attribute.${registration_complete}}} == true %}
```

{% endraw %}

#### Número

[Números]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/#numbers) são valores numéricos, que podem ser inteiros ou decimais. Por exemplo, um usuário pode ter `shoe_size: 10` ou `levels_completed: 287`. Valores numéricos não têm apóstrofos ao redor deles.

{% raw %}

```liquid
{% if {{custom_attribute.${shoe_size}}} == 10 %}
```

{% endraw %}

Você também pode usar outros [operadores básicos](https://shopify.dev/docs/themes/liquid/reference/basics/operators) como menor que (<) ou maior que (>) para inteiros:

{% raw %}

```liquid
{% if {{custom_attribute.${flyer_miles}}} >= 500 %}
```

{% endraw %}

#### String

Uma [string]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/#strings) é composta por caracteres alfanuméricos e armazena um dado sobre o seu usuário. Por exemplo, você pode ter `favorite_color: red` ou `phone_number: 3025981329`. Valores de string devem ter apóstrofos ao redor deles.

{% raw %}

```liquid
{% if {{custom_attribute.${favorite_color}}} == 'blue' %}
```

{% endraw %}

Para strings, você pode usar tanto "==" quanto "contains" no seu Liquid.

#### Array

Um [array]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/#arrays) é uma lista de informações sobre o seu usuário. Por exemplo, um usuário pode ter `last_viewed_shows: stranger things, planet earth, westworld`. Valores de array devem ter apóstrofos ao redor deles.

{% raw %}

```liquid
{% if {{custom_attribute.${last_viewed_shows}}} contains 'homeland' %}
```

{% endraw %}

Para arrays, você deve usar "contains" e não pode usar "==".

#### Hora

Um registro de data e hora de quando um evento ocorreu. Valores de [hora]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/#time) devem ter um [filtro matemático]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/filters/#math-filters) aplicado para serem usados em lógica condicional.

{% raw %}

```liquid
{% assign expire = {{custom_attribute.${subscription_end_date}}} | plus: 0 %}
```

{% endraw %}