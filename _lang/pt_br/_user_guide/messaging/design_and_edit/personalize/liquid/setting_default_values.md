---
nav_title: Definir valores padrão
article_title: Definir valores padrão no Liquid
page_order: 5
description: "Este artigo de referência aborda como definir valores de fallback padrão para qualquer atributo de personalização que você usa nas suas mensagens."

---

# Definir valores padrão {#set-default-values}

> Valores de fallback padrão podem ser definidos para qualquer atributo de personalização que você usa nas suas mensagens. Este artigo aborda como os valores padrão funcionam, como configurá-los e como usá-los nas suas mensagens.

{% raw %}

## Como funcionam {#how-they-work}

Valores padrão podem ser adicionados especificando um [filtro Liquid](http://docs.shopify.com/themes/liquid-documentation/filters) (use `|` para distinguir o filtro inline, conforme mostrado) com o nome "default."

```
| default: 'Insert Your Desired Default Here'
```

Se um valor padrão não for fornecido e o campo estiver ausente ou não definido no usuário, o campo ficará em branco na mensagem.

O exemplo a seguir mostra a sintaxe correta para adicionar um valor padrão. Neste caso, as palavras "Valued User" substituirão o atributo `{{ ${first_name} }}` se o campo `first_name` do usuário estiver vazio ou indisponível.

```liquid
Hi {{ ${first_name} | default: 'Valued User' }}, thanks for using the App!
```

Para uma usuária chamada Janet Doe, a mensagem apareceria como:

```
Hi Janet, thanks for using the App!
```

Ou...

```
Hi Valued User, thanks for using the App!
```
{% endraw %}

{% alert important %}
O valor padrão será exibido para valores vazios (empty), mas não para valores em branco (blank). Um valor vazio não contém nada, enquanto um valor em branco contém caracteres de espaço em branco (como espaços) e nenhum outro caractere. Por exemplo, uma string vazia pode ser `""` e uma string em branco pode ser `" "`.
{% endalert %}

## Definindo valores padrão para diferentes tipos de dados {#setting-default-values-for-different-data-types}

O exemplo anterior nesta seção mostra como definir um valor padrão para uma string. Você pode definir valores padrão para qualquer tipo de dado Liquid que tenha o valor `empty`, `nil` (indefinido) ou `false`, incluindo strings, booleanos, arrays, objetos e números.

### Caso de uso: booleanos {#use-case-booleans}

Digamos que você tenha um atributo personalizado booleano chamado `premium_user` e queira enviar uma mensagem personalizada com base no status premium do usuário. Alguns usuários não têm um status premium definido, então você precisará configurar um valor padrão para capturar esses usuários.

1. Você vai atribuir uma variável chamada `is_premium_user` ao atributo `premium_user` com um valor padrão de `false`. Isso significa que, se `premium_user` for `nil`, o valor de `is_premium_user` será `false` por padrão.

{% raw %}
```liquid
{% assign is_premium_user = {{custom_attribute.${premium_user}}} | default: false %}
```

{: start="2"}
2. Em seguida, use lógica condicional para especificar a mensagem a ser enviada se `is_premium_user` for `true`. Em outras palavras, o que enviar se `premium_user` for `true`. Você também vai atribuir um valor padrão ao nome do usuário, caso não tenhamos o nome dele.

```liquid
{% if is_premium_user %}
Hi {{${first_name} | default: 'premium user'}}, thank you for being a premium user!
```

{: start="3"}
3. Por fim, especifique qual mensagem enviar se `is_premium_user` for `false` (o que significa que `premium_user` é `false` ou `nil`). Depois, feche a lógica condicional.

```liquid
{% else %}
Hi {{${first_name} | default: 'valued user'}}, consider upgrading to premium for more benefits!
{% endif %}
```
{% endraw %}

{% details Código Liquid completo %}
{% raw %}
```liquid
{% assign is_premium_user = {{custom_attribute.${premium_user}}} | default: false %}
{% if is_premium_user %}
Hi {{${first_name} | default: 'premium user'}}, thank you for being a premium user!
{% else %}
Hi {{${first_name} | default: 'valued user'}}, consider upgrading to premium for more benefits!
{% endif %}
```
{% endraw %}
{% enddetails %}

### Caso de uso: números {#use-case-numbers}

Digamos que você tenha um atributo personalizado numérico chamado `reward_points` e queira enviar uma mensagem com os pontos de recompensa do usuário. Alguns usuários não têm pontos de recompensa definidos, então você precisará configurar um valor padrão para contemplar esses usuários.

1. Comece a mensagem se dirigindo ao nome do usuário ou a um valor padrão de `Valued User`, caso você não tenha o nome dele.

{% raw %}
```liquid
Hi {{${first_name} | default: 'valued user'}},
```
{% endraw %}

{: start="2"}
2. Termine a mensagem com a quantidade de pontos de recompensa que o usuário possui, usando o atributo personalizado chamado `reward_points` e o valor padrão de `0`. Todos os usuários cujo `reward_points` tiver valor `nil` terão `0` pontos de recompensa na mensagem.

{% raw %}
```liquid
Hi {{${first_name} | default: 'valued user'}}, you have {{custom_attribute.${reward_points} | default: 0}} reward points.
```
{% endraw %}

### Caso de uso: objetos {#use-case-objects}

Digamos que você tenha um objeto de atributo personalizado aninhado chamado `location` que contém as propriedades `city` e `state`. Se alguma dessas propriedades não estiver definida, você quer incentivar o usuário a fornecê-las.

1. Dirija-se ao usuário pelo nome e inclua um valor padrão, caso você não tenha o nome dele.

{% raw %}
```liquid
Hi {{${first_name} | default: 'valued user'}},
```
{% endraw %}

{: start="2"}
2. Escreva uma mensagem dizendo que você gostaria de confirmar o local associado à conta do usuário.

{% raw %}
```liquid
We'd like to confirm the location associated with your account. We use this location to send you promotions and offers for stores nearest you. You can update your location in your profile settings.
```
{% endraw %}

{: start="3"}
3. Insira o local do usuário na mensagem e atribua valores padrão para quando a propriedade de endereço não estiver definida.

{% raw %}
```liquid
Your location:
City: {{custom_attribute.${address.city} | default: 'Unknown'}}
State: {{custom_attribute.${address.state} | default: 'Unknown'}}
```
{% endraw %}

{% details Código Liquid completo %}
{% raw %}
```liquid
Hi {{${first_name} | default: 'valued user'}}

We'd like to confirm the location associated with your account. We use this location to send you promotions and offers for stores nearest you. You can update your location in your profile settings.

Your location:
City: {{custom_attribute.${address.city} | default: 'Unknown'}}
State: {{custom_attribute.${address.state} | default: 'Unknown'}}
```
{% endraw %}
{% enddetails %}

### Caso de uso: arrays {#use-case-arrays}

Digamos que você tenha um atributo personalizado de array chamado `upcoming_trips` que contém viagens com as propriedades `destination` e `departure_date`. Você quer enviar mensagens personalizadas aos usuários com base em se eles têm viagens agendadas.

1. Escreva uma lógica condicional para especificar que uma mensagem não deve ser enviada se `upcoming_trips` estiver `empty`.

{% raw %}
```liquid
{% if {{custom_attribute.${upcoming_trips}}} == empty %}
{% abort_message('No upcoming trips scheduled') %}
```
{% endraw %}

{: start="2"}
2. Especifique qual mensagem enviar se `upcoming_trips` tiver conteúdo:<br><br>**2a.** Dirija-se ao usuário e inclua um valor padrão, caso você não tenha o nome dele. <br>**2b.** Use uma tag `for` para especificar que você extrairá propriedades (ou informações) de cada viagem contida em `upcoming_trips`. <br>**2c.** Liste as propriedades na mensagem e inclua um valor padrão para quando `departure_date` não estiver definido. (Digamos que `destination` seja obrigatório para a criação de uma viagem, então você não precisa definir um valor padrão para ele.)<br>**2d.** Feche a tag `for` e depois feche a lógica condicional.

{% raw %}
```liquid
{% else %}
Hello {{${first_name} | default: 'fellow traveler'}},
  Here are your upcoming trips:
  <ul>
  {% for trip in {{custom_attribute.${upcoming_trips}}} %}
    <li>
      Destination: {{trip.destination}}
      Departure Date: {{trip.departure_date | default: 'Date not set'}}
    </li>
  {% endfor %}
  </ul>
{% endif %}
```
{% endraw %}

{% details Código Liquid completo %}
{% raw %}
```liquid
{% if {{custom_attribute.${upcoming_trips}}} == blank %}
{% abort_message('No upcoming trips scheduled') %}
{% else %}
Hello {{${first_name} | default: 'fellow traveler'}},
  Here are your upcoming trips:
  <ul>
  {% for trip in {{custom_attribute.${upcoming_trips}}} %}
    <li>
      Destination: {{trip.destination}}
      Departure Date: {{trip.departure_date | default: 'Date not set'}}
    </li>
  {% endfor %}
  </ul>
{% endif %}
```
{% endraw %}
{% enddetails %}

[31]:https://docs.shopify.com/themes/liquid/tags/variable-tags
[32]:https://docs.shopify.com/themes/liquid/tags/iteration-tags
[37]:#accounting-for-null-attribute-values