---
nav_title: Tutoriais
article_title: "Tutoriais: Escrevendo código Liquid"
page_order: 11
description: "Esta página de referência contém tutoriais para iniciantes que ajudam você a começar a escrever código Liquid."
page_type: tutorial
---

# Tutoriais: Escrevendo código Liquid {#tutorials-writing-liquid-code}

> Novo no Liquid? Estes tutoriais vão ajudar você a começar a escrever código Liquid para casos de uso voltados a iniciantes. Cada tutorial aborda uma combinação diferente de objetivos de aprendizado, como lógica condicional e operadores.

Ao concluir estes tutoriais, você será capaz de:

- Escrever código Liquid para casos de uso comuns
- Encadear lógica condicional Liquid para personalizar mensagens com base em dados de usuários
- Usar variáveis e filtros para escrever equações que utilizam os valores de atributos
- Reconhecer comandos básicos no código Liquid e ter uma compreensão geral sobre o que o código está fazendo

| Tutorial | Objetivos de aprendizado |
| --- | --- |
| [Personalizar mensagens para segmentos de usuários](#segments) | valores padrão, lógica condicional |
| [Lembretes de carrinho abandonado](#reminders) | operadores, lógica condicional |
| [Contagem regressiva para evento](#countdown) | variáveis, filtros de data |
| [Mensagem mensal de aniversário](#birthday) | variáveis, filtros de data, operadores |
| [Promover um produto favorito](#favorite-product) | variáveis, filtros de data, equações, operadores |
{: .reset-br-td-1 .reset-br-td-2 aria-label="Tutoriais: Escrevendo código Liquid" }

## Mensagens personalizadas para segmentos de usuários {#segments}

Vamos personalizar mensagens para diferentes segmentos de usuários, como clientes VIP e novos assinantes.

1. Abra a mensagem com saudações personalizadas para enviar quando você tem e quando não tem o nome do usuário. Para isso, crie uma Liquid tag que inclua o atributo `first_name` e um valor padrão para usar caso `first_name` esteja em branco. Neste cenário, vamos usar "traveler" como valor padrão.

{% raw %}
```liquid
Happy summer, {{${first_name} | default: "traveler"}}!
```
{% endraw %}

{: start="2"}
2. Agora, vamos definir a mensagem a ser enviada se o usuário for um cliente VIP. Precisaremos usar uma tag de lógica condicional para isso: `if`. Essa tag vai dizer que, se o atributo personalizado `vip_status` for igual a `VIP`, o Liquid a seguir será executado. Neste caso, uma mensagem específica será enviada.

{% raw %}
```liquid
{% if {{custom_attribute.${vip_status}}} == 'VIP' %}
Thank you for being a VIP customer! Enjoy your exclusive discount code: VIPSUMMR464.
```
{% endraw %}

{: start="3"}
3. Vamos enviar uma mensagem personalizada para usuários que são novos assinantes. Usaremos a tag de lógica condicional `elsif` para especificar que, se o `vip_status` do usuário for `new`, a mensagem a seguir será enviada.

{% raw %}
```liquid
{% elsif {{custom_attribute.${vip_status}}} == 'new' %}
Thank you for subscribing! Enjoy your welcome discount code: NEWTRAVEL257.
```
{% endraw %}

{: start="4"}
4. E os usuários que não são VIP nem novos? Podemos enviar uma mensagem para todos os outros usuários com a tag `else`, que especifica que a mensagem a seguir deve ser enviada se as condições anteriores não forem atendidas. Então podemos fechar a lógica condicional com a tag `endif`, já que não há mais status VIP a considerar.

{% raw %}
```liquid
{% else %}
Thanks for traveling with us! Enjoy your unique discount code: SUMMRTRVLS240.
{% endif %}
```
{% endraw %}

{% details Código Liquid completo %}
{% raw %}
```liquid
Happy summer, {{${first_name} | default: "traveler"}}!
{% if {{custom_attribute.${vip_status}}} == 'VIP' %}
Thank you for being a VIP customer! Enjoy your exclusive discount code: VIPSUMMR464.
{% elsif {{custom_attribute.${vip_status}}} == 'new' %}
Thank you for subscribing! Enjoy your welcome discount code: NEWTRAVEL257.
{% else %}
Thanks for traveling with us! Enjoy your unique discount code: SUMMRTRVLS240.
{% endif %}
```
{% endraw %}
{% enddetails %}

## Lembretes de carrinho abandonado {#reminders}

Vamos enviar mensagens personalizadas para lembrar os usuários sobre itens deixados no carrinho. Vamos personalizar ainda mais com base na quantidade de itens no carrinho: se houver três itens ou menos, listaremos todos eles. Se houver mais de três itens, enviaremos uma mensagem mais concisa.

1. Vamos verificar se o carrinho do usuário está vazio abrindo uma lógica condicional Liquid com o operador `!=`, que significa "não é igual a". Neste caso, definiremos a condição como o atributo personalizado `cart_items` não sendo igual a um valor em branco.

{% raw %}
```liquid
{% if {{custom_attribute.${cart_items}}} != blank %}
```
{% endraw %}

{: start="2"}
2. Em seguida, precisaremos restringir nosso foco e verificar se o carrinho tem mais de três itens usando o operador `>`, que significa "maior que".

{% raw %}
```liquid
{% if {{custom_attribute.${cart_items}}} | size > 3 %}
```
{% endraw %}

{: start="3"}
3. Escreva uma mensagem que cumprimente o usuário pelo nome ou, se não estiver disponível, use "there" como valor padrão. Inclua o que deve ser dito se houver mais de três itens no carrinho. Como não queremos sobrecarregar o usuário com uma lista completa, vamos listar os três primeiros `cart_items`.

{% raw %}
```liquid
Hi {{${first_name} | default: 'there'}}, don't forget to complete your purchase! Your items {{custom_attribute.${cart_items[0]}}}, {{custom_attribute.${cart_items[1]}}}, {{custom_attribute.${cart_items[2]}}}, and others are waiting for you.
```
{% endraw %}

{: start="4"}
4. Use a tag `else` para especificar o que deve acontecer se as condições anteriores não forem atendidas (ou seja, se `cart_items` estiver em branco ou tiver menos de três itens), e então forneça a mensagem a ser enviada. Como três itens não ocupam muito espaço, podemos listar todos eles. Usaremos o operador Liquid `join` e `,` para especificar que os itens devem ser listados separados por vírgula. Feche a lógica com `endif`.

{% raw %}
```liquid
{% else %}
Hi {{${first_name} | default: 'there'}}, don't forget to complete your purchase! Your items: {{{custom_attribute.${cart_items}}} | join: ', '}  are waiting for you.
{% endif %}
```
{% endraw %}

{: start="5"}
5. Use `else` e depois um `abort_message` para dizer ao código Liquid para não enviar uma mensagem se o carrinho não atender a nenhuma das condições anteriores. Em outras palavras, se o carrinho estiver vazio. Feche a lógica com `endif`.

{% raw %}
```liquid
{% else %}
{% abort_message('No items in cart') %}
{% endif %}
```
{% endraw %}

{% details Código Liquid completo %}
{% raw %}
```liquid
{% if {{custom_attribute.${cart_items}}} != blank %}
{% if {{custom_attribute.${cart_items}}} | size > 3 %}
Hi {{${first_name} | default: 'there'}}, don't forget to complete your purchase! Your items {{custom_attribute.${cart_items[0]}}}, {{custom_attribute.${cart_items[1]}}}, {{custom_attribute.${cart_items[2]}}}, and others are waiting for you.
{% else %}
Hi {{${first_name} | default: 'there'}}, don't forget to complete your purchase! Your items: {{{custom_attribute.${cart_items}}} | join: ', '}  are waiting for you.
{% endif %}
{% else %}
{% abort_message('No items in cart') %}
{% endif %}
```
{% endraw %}
{% enddetails %}

## Contagem regressiva para evento {#countdown}

Vamos enviar aos usuários uma mensagem informando quantos dias faltam para uma liquidação de aniversário. Para isso, usaremos variáveis para criar equações que manipulam os valores de atributos.

1. Primeiro, vamos atribuir a variável `sale_date` ao atributo personalizado `anniversary_date` e aplicar o filtro `date: "s"`. Isso converte `anniversary_date` para um formato de timestamp expresso em segundos e então atribui esse valor a `sale_date`.

{% raw %}
```liquid
{% assign sale_date = {{custom_attribute.${anniversary_date}}} | date: "%s" %}
```
{% endraw %}

{: start="2"}
2. Também precisamos atribuir uma variável para capturar o timestamp de hoje. Vamos atribuir a variável `today` a `now` (a data e hora atuais) e então aplicar o filtro `date: "%s"`.

{% raw %}
```liquid
{% assign today =  'now' | date: "%s"  %}
```
{% endraw %}

{: start="3"}
3. Agora vamos calcular quantos segundos existem entre agora (`today`) e a Liquidação de Aniversário (`sale_date`). Para isso, atribua a variável `difference` ao valor de `sale_date` menos `today`.

{% raw %}
```liquid
{% assign difference =  event_date | minus: today %}
```
{% endraw %}

{: start="4"}
4. Agora precisamos converter `difference` para um valor que possamos referenciar em uma mensagem, já que não é ideal dizer ao usuário quantos segundos faltam para uma liquidação. Vamos atribuir `difference_days` a `event_date` e dividi-lo por `86400` para obter o número de dias.

{% raw %}
```liquid
{% assign difference_days = difference | divided_by: 86400 %}
```
{% endraw %}

{: start="5"}
5. Por fim, vamos criar a mensagem a ser enviada.

{% raw %}
```liquid
Get ready! Our Anniversary Sale is in {{ difference_days }} days!
```
{% endraw %}

{% details Código Liquid completo %}
{% raw %}
```liquid
{% assign sale_date = {{custom_attribute.${anniversary_date}}} | date: "%s" %}
{% assign today =  'now' | date: "%s"  %}
{% assign difference =  event_date | minus: today %}
{% assign difference_days = difference | divided_by: 86400 %}
Get ready! Our Anniversary Sale is in {{ difference_days }} days!
```
{% endraw %}
{% enddetails %}

## Mensagem mensal de aniversário {#birthday}

Vamos enviar uma promoção especial para todos os usuários cujo aniversário cai no mês atual. Usuários que não fazem aniversário neste mês não receberão nenhuma mensagem.

1. Primeiro, vamos obter o mês atual. Atribuiremos a variável `this_month` a `now` (a data e hora atuais) e usaremos o filtro `date: "%B"` para especificar que a variável deve ser igual ao mês.

{% raw %}
```liquid
{% assign this_month = 'now' | date: "%B" %}
```
{% endraw %}

{: start="2"}
2. Agora, vamos obter o mês de nascimento a partir do `date_of_birth` do usuário. Atribuiremos a variável `birth_month` a `date_of_birth` e usaremos o filtro `date: "%B"`.

{% raw %}
```liquid
{% assign birth_month = {{${date_of_birth}}} | date: "%B" %}
```
{% endraw %}

{: start="3"}
3. Agora que temos duas variáveis com um mês como valor, podemos compará-las com lógica condicional. Vamos definir a condição como `this_month` sendo igual ao `birth_month` do usuário.

{% raw %}
```liquid
{% if {{this_month}} == {{birth_month}} %}
```
{% endraw %}

{: start="4"}
4. Vamos criar a mensagem a ser enviada se este mês também for o mês de aniversário do usuário.

{% raw %}
```liquid
We heard {{this_month}} is a special month! Enjoy a 50% discount on your purchase with code BIRTHDAY50 until the end of {{this_month}}.
```
{% endraw %}

{: start="5"}
5. Use a tag `else` para especificar o que acontece se a condição não for atendida (porque este mês não é o mês de aniversário do usuário).

{% raw %}
```liquid
{% else %}
```
{% endraw %}

{: start="6"}
6. Não queremos enviar uma mensagem se o mês de aniversário do usuário não for este mês, então usaremos `abort_message` para cancelar a mensagem e fechar a lógica condicional com `endif`.

{% raw %}
```liquid
{% abort_message("Not their birthday month") %}
{% endif %}
```
{% endraw %}

{% details Código Liquid completo %}
{% raw %}
```liquid
{% assign this_month = 'now' | date: "%B" %}
{% assign birth_month = {{${date_of_birth}}} | date: "%B" %}
{% if {{this_month}} == {{birth_month}} %}
We heard {{this_month}} is a special month! Enjoy a 50% discount on your purchase with code BIRTHDAY50 until the end of {{this_month}}.
{% else %}
{% abort_message("Not their birthday month") %}
{% endif %}
```
{% endraw %}
{% enddetails %}

## Promoção de produto favorito {#favorite-product}

Vamos promover o produto favorito de um usuário se a última data de compra dele foi há mais de seis meses.

1. Primeiro, usaremos lógica condicional para verificar se temos o produto favorito e a última data de compra do usuário.

{% raw %}
```liquid
{% if {{custom_attribute.${favorite_product}}} == blank or {{custom_attribute.${last_purchase_date}}} == blank %}
```
{% endraw %}

{: start="2"}
2. Em seguida, definiremos que, se não tivermos o produto favorito ou a última data de compra do usuário, a mensagem não deve ser enviada.

{% raw %}
```liquid
{% abort_message("No favorite product or last purchase date") %}
```
{% endraw %}

{: start="3"}
3. Usaremos `else` para especificar o que deve acontecer se a condição acima não for atendida (porque nós _temos_ o produto favorito e a última data de compra do usuário).

{% raw %}
```liquid
{% else %}
```
{% endraw %}

{: start="4"}
4. Se temos a data de compra, precisamos atribuí-la a uma variável para compará-la com a data de hoje. Primeiro, vamos criar um valor para a data de hoje atribuindo a variável `today` a `now` (a data e hora atuais) e usando o filtro `date: "%s"` para converter o valor em um formato de timestamp expresso em segundos. Adicionaremos o filtro `plus: 0` para adicionar um "0" ao timestamp. Isso não altera o valor do timestamp, mas é útil para usar o timestamp em equações futuras.


{% raw %}
```liquid
{% assign today = 'now' | date: "%s" | plus: 0 %}
```
{% endraw %}

{: start="5"}
5. Agora vamos capturar a última data de compra em segundos atribuindo a variável `last_purchase_date` ao atributo personalizado `last_purchase_date` e usando o filtro `date: "s"`. Novamente adicionaremos o filtro `plus: 0`.

{% raw %}
```liquid
{% assign last_purchase_date = {{custom_attribute.${last_purchase_date}}} | date: "%s" | plus: 0 %}
```
{% endraw %}

{: start="6"}
6. Como a última data de compra e a data de hoje estão em segundos, precisaremos calcular quantos segundos existem em seis meses. Vamos criar uma equação (aproximadamente 6 meses * 30,44 dias * 24 horas * 60 minutos * 60 segundos) e atribuí-la à variável `six_months`. Usaremos `times` para especificar a multiplicação das unidades de tempo.

{% raw %}
```liquid
{% assign six_months = 6 | times: 30.44 | times: 24 | times: 60 | times: 60 %}
```
{% endraw %}

{: start="7"}
7. Agora que todos os nossos valores de tempo estão em segundos, podemos usar seus valores em equações. Vamos atribuir uma variável chamada `today_minus_last_purchase_date` que pega o valor de hoje e subtrai dele o `last_purchase_date`. Isso nos dá quantos segundos se passaram desde a última compra.

{% raw %}
```liquid
{% assign today_minus_last_purchase_date = {{today | minus: last_purchase_date}} %}
```
{% endraw %}

{: start="8"}
8. Agora vamos comparar diretamente nossos valores de tempo na lógica condicional. Vamos definir a condição como `today_minus_last_purchase_date` sendo maior ou igual (`>=`) a seis meses. Em outras palavras, a última compra foi há pelo menos seis meses.

{% raw %}
```liquid
{% if today_minus_last_purchase_date >= six_months %}
```
{% endraw %}

{: start="9"}
9. Vamos criar a mensagem a ser enviada se a última compra foi há pelo menos seis meses.

{% raw %}
```liquid
We noticed it’s been a while since you last purchased {{custom_attribute.${favorite_product}}}. Have you checked out our latest offerings?
```
{% endraw %}

{: start="10"}
10. Usaremos a tag `else` para especificar o que deve acontecer se a condição não for atendida (porque a compra não foi há pelo menos seis meses).

{% raw %}
```liquid
{% else %}
```
{% endraw %}

{: start="11"}
11. Incluiremos um `abort_message` para cancelar a mensagem.

{% raw %}
```liquid
{% abort_message("No favorite product or last purchase date") %}
```
{% endraw %}

{: start="12"}
12. Para finalizar, encerraremos o Liquid com duas tags `endif`. O primeiro `endif` fecha a verificação condicional do produto favorito ou da última data de compra, e o segundo `endif` fecha a verificação condicional de a última compra ter sido há pelo menos seis meses.

{% raw %}
```liquid
{% endif %}
{% endif %}
```
{% endraw %}

{% details Código Liquid completo %}
{% raw %}
```liquid
{% if {{custom_attribute.${favorite_product}}} == blank or {{custom_attribute.${last_purchase_date}}} == blank %}
{% abort_message("No favorite product or last purchase date") %}
{% else %}
{% assign today = 'now' | date: "%s" | plus: 0 %}
{% assign last_purchase_date = {{custom_attribute.${last_purchase_date}}} | date: "%s" | plus: 0 %}
{% assign six_months = 6 | times: 30.44 | times: 24 | times: 60 | times: 60 %}
{% assign today_minus_last_purchase_date = {{today | minus: last_purchase_date}} %}
{% if today_minus_last_purchase_date >= six_months %}
We noticed it’s been a while since you last purchased {{custom_attribute.${favorite_product}}}. Have you checked out our latest offerings?
{% else %}
{% abort_message("Last purchase was less than six months ago") %}
{% endif %}
{% endif %}
```
{% endraw %}
{% enddetails %}