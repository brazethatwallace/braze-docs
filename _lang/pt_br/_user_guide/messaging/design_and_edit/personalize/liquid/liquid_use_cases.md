---
nav_title: Biblioteca de casos de uso de Liquid
article_title: Biblioteca de casos de uso de Liquid
page_order: 10
search_rank: 2
excerpt_separator: ""
page_type: glossary
layout: liquid_use_case_glossary
description: "Esta landing page reúne exemplos de casos de uso de Liquid organizados por categoria, como aniversários, uso do app, contagens regressivas e muito mais."

---

{% api %}

## Aniversários e feriados {#anniversaries-and-holidays}

{% apitags %}
Anniversaries and holidays
{% endapitags %}

- [Personalizar mensagens com base no ano de aniversário do usuário](#anniversary-year)
- [Personalizar mensagens com base na semana de aniversário do usuário](#birthday-week)
- [Enviar campanhas para usuários no mês de aniversário deles](#birthday-month)
- [Evitar o envio de mensagens em feriados importantes](#holiday-avoid)

### Personalizar mensagens com base no ano de aniversário do usuário {#anniversary-year}

Este caso de uso mostra como calcular o aniversário de uso do app de um usuário com base na data de cadastro inicial e exibir mensagens diferentes de acordo com quantos anos estão sendo comemorados.

{% raw %}
```liquid
{% assign this_month = 'now' | date: "%B" %}
{% assign this_day = 'now' | date: "%d" %}
{% assign anniversary_month = {{custom_attribute.${registration_date}}} | date: "%B" %}
{% assign anniversary_day = {{custom_attribute.${registration_date}}} | date: "%d" %}
{% assign anniversary_year = {{custom_attribute.${registration_date}}} | date: "%Y" %}

{% if this_month == anniversary_month %}
{% if this_day == anniversary_day %}
{% if anniversary_year == '2021' %}
Exactly one year ago today we met for the first time!

{% elsif anniversary_year == '2020' %}
Exactly two years ago today we met for the first time!

{% elsif anniversary_year == '2019' %}
Exactly three years ago today we met for the first time!

{% else %}
{% abort_message("Not same year") %}
{% endif %}

{% else %}
{% abort_message("Not same day") %}
{% endif %}

{% else %}
{% abort_message("Not same month") %}
{% endif %}
```
{% endraw %}

**Explicação:** Aqui, usamos a variável reservada `now` para inserir a data e hora atuais no formato [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601). Os filtros `%B` (mês como "May") e `%d` (dia como "18") formatam o mês e o dia atuais. Em seguida, usamos os mesmos filtros de data e hora nos valores de `signup_date` para garantir que possamos comparar os dois valores usando tags e lógica condicionais.

Depois, repetimos mais três declarações de variáveis para obter `%B` e `%d` da `signup_date`, adicionando também `%Y` (ano como "2021"). Isso transforma a data e hora da `signup_date` apenas no ano. Saber o dia e o mês nos permite verificar se o aniversário do usuário é hoje, e saber o ano nos diz quantos anos se passaram — o que nos permite saber por quantos anos parabenizá-lo!

{% alert tip %} Você pode criar quantas condições quiser, de acordo com os anos em que esteve coletando datas de cadastro. {% endalert %}

### Personalizar mensagens com base na semana de aniversário do usuário {#birthday-week}

Este caso de uso mostra como encontrar o aniversário de um usuário, compará-lo com a data atual e exibir mensagens especiais de aniversário antes, durante e depois da semana de aniversário.

{% raw %}
```liquid
{% assign this_week = 'now' | date: '%W' %}
{% assign birthday_week = {{${date_of_birth}}} | date: '%W' %}
{% assign last_week = {{this_week}} | minus: 1 %}
{% assign next_week = {{this_week}} | plus: 1 %}
{% assign birthday_week_conversion = {{birthday_week}} | plus: 0 %}
{% if {{last_week}} == {{birthday_week_conversion}} %}
Happy birthday for last week!
{% elsif {{birthday_week}} == {{this_week}} %}
Happy birthday for this week!
{% elsif {{next_week}} == {{birthday_week_conversion}} %}
Happy birthday for next week!
{% else %}
No birthday for you!
{% endif %}
```
{% endraw %}

**Explicação:** Semelhante ao caso de uso do [ano de aniversário](#anniversary-year), aqui pegamos a variável reservada `now` e usamos o filtro `%W` (semana, como a semana 12 de 52 no ano) para obter o número da semana do ano em que o aniversário do usuário cai. Se a semana de aniversário do usuário corresponder à semana atual, enviamos uma mensagem de parabéns!

Também incluímos declarações para `last_week` e `next_week` para personalizar ainda mais suas mensagens.

### Enviar campanhas para usuários no mês de aniversário deles {#birthday-month}

Este caso de uso mostra como calcular o mês de aniversário de um usuário, verificar se o aniversário cai no mês atual e, em caso positivo, enviar uma mensagem especial.

{% raw %}
```liquid
{% assign this_month = 'now' | date: "%B" %}
{% assign birth_month = {{${date_of_birth}}} | date: "%B" %}
{% if {{this_month}} == {{birth_month}} %}
Message body
{% else %}
{% abort_message("Not their birthday month") %}
{% endif %}
```
{% endraw %}

**Explicação:** Semelhante ao caso de uso da [semana de aniversário](#birthday-week), exceto que aqui usamos o filtro `%B` (mês como "May") para calcular quais usuários fazem aniversário neste mês. Uma aplicação possível seria enviar uma mensagem para aniversariantes em um e-mail mensal.

### Evitar o envio de mensagens em feriados importantes {#holiday-avoid}

Este caso de uso mostra como enviar mensagens durante o período de festas, evitando os dias de feriados importantes, quando o engajamento tende a ser baixo.

{% raw %}
```liquid
{% assign today = 'now' | date: '%Y-%m-%d' %}
{% if today == "2023-12-24" or today == "2023-12-25" or today == "2023-12-26" %}
{% abort_message %}
{% else %}
Message if today isn't one of the provided holidays.
{% endif %}
```
{% endraw %}

**Explicação:** Aqui, atribuímos o termo `today` à variável reservada `now` (a data e hora atuais), usando os filtros `%Y` (ano como "2023"), `%m` (mês como "12") e `%d` (dia como "25") para formatar a data. Em seguida, executamos nossa declaração condicional para dizer que, se a variável `today` corresponder aos dias de feriado escolhidos, a mensagem será cancelada.

O exemplo fornecido usa a véspera de Natal, o dia de Natal e o dia seguinte ao Natal (Boxing Day).

{% endapi %}

{% api %}

## Uso do app {#app-usage}

{% apitags %}
App usage
{% endapitags %}

- [Enviar mensagens no idioma do usuário se ele não tiver registrado uma sessão](#app-session-language)
- [Personalizar mensagens com base em quando o usuário abriu o app pela última vez](#app-last-opened)
- [Exibir uma mensagem diferente se o usuário usou o app há menos de três dias](#app-last-opened-less-than)

### Enviar mensagens no idioma do usuário se ele não tiver registrado uma sessão {#app-session-language}

Este caso de uso verifica se um usuário registrou uma sessão e, caso contrário, inclui lógica para exibir uma mensagem com base no idioma coletado manualmente por meio de um atributo personalizado, se houver. Se não houver informação de idioma vinculada à conta, a mensagem será exibida no idioma padrão. Se o usuário tiver registrado uma sessão, qualquer informação de idioma vinculada ao usuário será utilizada para exibir a mensagem apropriada.

{% raw %}
```liquid
{% if {{${last_used_app_date}}} == nil %}
{% if {{custom_attribute.${user_language}}} == 'en' %}
Message in English based on custom attribute
{% elsif {{custom_attribute.${user_language}}} == 'fr' %}
Message in French based on custom attribute
{% else %}
Does not have language - Default language
{% endif %}
{% else %}
{% if ${language} == 'en' %}
Message in English based on Language
{% elsif ${language} == 'fr' %}
Message in French based on Language
{% else %}
Has language - Default language
{% endif %}
{% endif %}
```
{% endraw %}

{% raw %}
**Explicação:** Aqui, estamos usando duas declarações `if` agrupadas e aninhadas. A primeira declaração `if` verifica se o usuário iniciou uma sessão, checando se `last_used_app_date` é `nil`. Isso porque `{{${language}}}` é coletado automaticamente pelo SDK quando um usuário registra uma sessão. Se o usuário não registrou uma sessão, ainda não teremos o idioma dele, então verificamos se algum atributo personalizado relacionado ao idioma foi salvo e, com base nessa informação, exibimos uma mensagem nesse idioma, se possível.
{% endraw %}

A segunda declaração `if` apenas verifica o atributo padrão (standard), pois o usuário não tem `nil` para `last_used_app_date`, o que significa que ele registrou uma sessão e temos o idioma dele.

{% alert note %}
[`Nil`](https://shopify.github.io/liquid/basics/types/#nil) é uma variável reservada que é retornada quando o código Liquid não tem resultados. `Nil` é tratado como `false` em um bloco `if`.
{% endalert %}

### Personalizar mensagens com base em quando o usuário abriu o app pela última vez {#app-last-opened}

Este caso de uso calcula a última vez que um usuário abriu seu app e exibe uma mensagem personalizada diferente dependendo do tempo decorrido.

{% raw %}
```liquid
{% assign last_used_date = {{${last_used_app_date}}} | date: "%s" %}
{% assign now = 'now' | date: "%s" %}
{% assign difference_in_days = {{now}} | minus: {{last_used_date}} | divided_by: 86400 %}
{% if {{difference_in_days}} < 3 %}
Happy to see you again!
{% else %}
It's been a while; here are some of our latest updates.
{% endif %}
```
{% endraw %}

### Exibir uma mensagem diferente se o usuário usou o app há menos de três dias {#app-last-opened-less-than}

Este caso de uso calcula há quanto tempo um usuário usou seu app e, dependendo do tempo decorrido, exibe uma mensagem personalizada diferente.

{% raw %}
```liquid
{% assign last_used_date = {{${last_used_app_date}}} | date: "%s" %}
{% assign now = 'now' | date: "%s" %}
{% assign difference_in_days = {{now}} | minus: {{last_used_date}} | divided_by: 86400 %}
{% if {{difference_in_days}} < 3 %}
Message for a recently active user
{% else %}
Message for a less active user
{% endif %}
```
{% endraw %}

{% endapi %}

{% api %}

## Contagens regressivas {#countdowns}

{% apitags %}
Countdowns
{% endapitags %}

- [Adicionar X dias à data de hoje](#countdown-add-x-days)
- [Calcular uma contagem regressiva a partir de um ponto fixo no tempo](#countdown-difference-days)
- [Criar uma contagem regressiva para datas e prioridades de envio específicas](#countdown-shipping-options)
- [Criar uma contagem regressiva em dias](#countdown-days)
- [Criar uma contagem regressiva de dias para horas e minutos](#countdown-dynamic)
- [Mostrar quantos dias faltam até uma determinada data](#countdown-future-date)
- [Exibir quantos dias faltam até a chegada de um atributo de data personalizado](#countdown-custom-date-attribute)
- [Exibir quanto tempo resta e cancelar a mensagem se restar apenas X tempo](#countdown-abort-window)
- [Mensagem no app para enviar X dias antes do fim da assinatura do usuário](#countdown-membership-expiry)
- [Personalizar mensagens no app com base na data e no idioma do usuário](#countdown-personalize-language)
- [Inserir a data de 30 dias a partir de agora, formatada como mês e dia](#countdown-template-date)

### Adicionar X dias à data de hoje {#countdown-add-x-days}

Este caso de uso adiciona um número específico de dias à data atual para referenciar e incluir em mensagens. Por exemplo, você pode querer enviar uma mensagem no meio da semana mostrando eventos na região para o fim de semana.

{% raw %}
```liquid
Here are the movies we're showing on {{ "now" | date:'%s' | plus:259200 | date:"%F" }}!
```
{% endraw %}

O valor de `plus` é sempre em segundos, então terminamos com o filtro `%F` para converter os segundos em dias.

{% alert important %}
Você pode querer incluir uma URL ou deep link para uma lista de eventos na sua mensagem, para direcionar o usuário a uma lista de ações que acontecerão no futuro.
{% endalert %}

### Calcular uma contagem regressiva a partir de um ponto fixo no tempo {#countdown-difference-days}

Este caso de uso calcula a diferença em dias entre uma data específica e a data atual. Essa diferença pode ser usada para exibir uma contagem regressiva para seus usuários.

{% raw %}
```liquid
{% assign event_date = '2023-12-31' | date: "%s" %}
{% assign today = 'now' | date: "%s" %}
{% assign difference = event_date | minus: today %}
{% assign difference_days = difference | divided_by: 86400 %}
you have {{ difference_days }} days left!
```
{% endraw %}

### Criar uma contagem regressiva para datas e prioridades de envio específicas {#countdown-shipping-options}

Este caso de uso captura diferentes opções de envio, calcula o tempo necessário para receber o pedido e exibe mensagens incentivando os usuários a comprar a tempo de receber o pacote até uma determinada data.

{% raw %}
```liquid
{% assign standard_shipping_start = "2023-12-10T00:00-05:00" | date: "%s" %}
{% assign standard_shipping_end = "2023-12-20T13:00-05:00" | date: "%s" %}
{% assign express_shipping_end = "2023-12-22T24:00-05:00" | date: "%s" %}
{% assign overnight_shipping_end = "2023-12-23T24:00-05:00" | date: "%s" %}
{% assign today = 'now' | date: "%s" %}

{% assign difference_s = standard_shipping_end | minus: today %}
{% assign difference_s_days = difference_s | divided_by: 86400.00 | round %}
{% assign difference_e = express_shipping_end | minus: today %}
{% assign difference_e_days = difference_e | divided_by: 86400.00 | round %}
{% assign difference_o = overnight_shipping_end | minus: today %}
{% assign difference_o_days = difference_o | divided_by: 86400.00 | round %}

{% if today >= standard_shipping_start and today <= standard_shipping_end %}
{% if difference_s_days == 0 %}
This is the last day to order with standard shipping, so your order gets here on time for Christmas Eve!
{% elsif difference_s_days == 1 %}
There is {{difference_s_days}} day left to order with standard shipping, so your order gets here on time for Christmas Eve!

{% else %}
There are {{difference_s_days}} days left to order with standard shipping so your order gets here on time for Christmas Eve!
{% endif %}
{% elsif today > standard_shipping_end and today < express_shipping_end %}
{% if difference_e_days == 1 %}
There is {{difference_e_days}} day left to order with express shipping, so your order gets here on time for Christmas Eve!
{% else %}
There are {{difference_e_days}} days left to order with express shipping so your order gets here on time for Christmas Eve!
{% endif %}
{% elsif today >= express_shipping_end and today < overnight_shipping_end %}
This is the last day for overnight shipping so your order gets here on time for Christmas Eve!
{% else %}
{% abort_message("Unable to order and ship in time") %}
{% endif %}
```
{% endraw %}

### Criar uma contagem regressiva em dias {#countdown-days}

Este caso de uso calcula o tempo restante entre um evento específico e a data atual e exibe quantos dias faltam até o evento.

{% raw %}
```liquid
{% assign event_date = {{custom_attribute.${last_selected_event_date}}} | date: "%s" %}
{% assign today =  'now' | date: "%s"  %}
{% assign difference =  event_date | minus: today %}
{% assign difference_days = difference | divided_by: 86400 %}
Your order will arrive in {{ difference_days }} days!
```
{% endraw %}

{% alert important %}
Você precisará de um campo de atributo personalizado com um valor de `date`.
{% endalert %}

### Criar uma contagem regressiva de dias para horas e minutos {#countdown-dynamic}

Este caso de uso calcula o tempo restante entre um evento específico e a data atual. Dependendo do tempo restante até o evento, ele altera o valor de tempo (dias, horas, minutos) para exibir diferentes mensagens personalizadas.

Por exemplo, se faltam dois dias para o pedido de um cliente chegar, você pode dizer "Seu pedido chegará em 2 dias". Já se faltar menos de um dia, você pode mudar para "Seu pedido chegará em 17 horas".

{% raw %}
```liquid
{% assign today =  'now' | date: "%s"  %}
{% assign scheme_finish = "2017-10-13T10:30:30" | date: "%s" %}
{% assign difference_seconds =  scheme_finish | minus: today %}
{% assign difference_minutes = difference_seconds | divided_by: 60 %}
{% assign difference_hours = difference_seconds | divided_by: 3600 %}
{% assign difference_days = difference_seconds | divided_by: 86400 %}
{% if {{difference_minutes}} > 59 and {{difference_minutes}} < 1440 %}
You have {{difference_hours}} hours left till your order arrives!
{% elsif {{difference_minutes}} < 59 %}
You have {{difference_minutes}} minutes left till your order arrives!
{% else %}
You have {{difference_days}} days left till your order arrives!
{% endif %}
```
{% endraw %}

{% alert important %}
Você precisará de um campo de atributo personalizado com um valor de `date`. Também será necessário definir limites de tempo para quando o tempo deve ser exibido em dias, horas e minutos.
{% endalert %}

### Mostrar quantos dias faltam até uma determinada data {#countdown-future-date}

Este caso de uso calcula a diferença entre a data atual e uma data futura de evento e exibe uma mensagem informando quantos dias faltam até o evento.

{% raw %}
```liquid
{% assign event_date = '2024-01-15' | date: "%s" %}
{% assign today = 'now' | date: "%s" %}
{% assign difference = event_date | minus: today %}
{% assign difference_days = difference | divided_by: 86400 %}
There are {{difference_days}} days until your birthday!
```
{% endraw %}

### Exibir quantos dias faltam até a chegada de um atributo de data personalizado {#countdown-custom-date-attribute}

Este caso de uso calcula a diferença em dias entre as datas atual e futura e exibe uma mensagem se a diferença corresponder a um número definido.

Neste exemplo, um usuário receberá uma mensagem dentro de dois dias do atributo de data personalizado. Caso contrário, a mensagem não será enviada.

{% raw %}
```liquid
{% assign today = 'now' | date: '%j' | plus: 0 %}
{% assign surgery_date = {{custom_attribute.${surgery_date}}} | date: '%j' | plus: 0 %}

{% assign difference_days = {{surgery_date}} | minus: {{today}} %}
{% if difference_days == 2 %}
Your surgery is in 2 days on {{custom_attribute.${surgery_date}}}
{% else %}
{% abort_message %}
{% endif %}
```
{% endraw %}

### Exibir quanto tempo resta e cancelar a mensagem se restar apenas X tempo {#countdown-abort-window}

Este caso de uso calcula quanto tempo falta até uma determinada data e, dependendo do tempo restante (pulando o envio se a data estiver muito próxima), exibe diferentes mensagens personalizadas.

Por exemplo, "Você tem x horas restantes para comprar sua passagem para Londres", mas não enviar a mensagem se faltar menos de duas horas para o horário do voo para Londres.

{% raw %}
```liquid
{% assign today =  'now' | date: "%s"  %}
{% assign dep_time = {{event_properties.${outboundDate}}} | date: "%s" %}
{% assign time_to_dep = dep_time | minus: today %}
{% if {{time_to_dep}} < 7200 %}
{% abort_message("OutboundDate less than 2 hours") %}
{% elsif {{time_to_dep}} > 7200 and {{time_to_dep}} < 86400 %}
Don't forget to buy your ticket to {{event_properties.${toStation}}} within next 24 hours!
{% else %}
Still traveling to {{event_properties.${toStation}}} in more than 24 hours? Book now!
{% endif %}
```
{% endraw %}

{% alert important %} Você precisará de uma propriedade de evento personalizado. {% endalert %}

### Mensagem no app para enviar X dias antes do fim da assinatura do usuário {#countdown-membership-expiry}

Este caso de uso captura a data de vencimento da assinatura, calcula quanto tempo falta para expirar e exibe diferentes mensagens com base em quanto tempo resta até o vencimento.

{% raw %}
```liquid
{% assign membership_expiry = {{custom_attribute.${membership_expiry_date}}} | date: "%s" %}
{% assign today = 'now' | date: "%s" %}
{% assign difference = membership_expiry | minus: today %}
{% assign difference_days = difference | divided_by: 86400 %}

{% if difference_days > 4 and difference_days <= 7 %}
You have {{difference_days}} days left in your trial, make sure you upgrade!

{% elsif difference_days > 2 and difference_days <= 4 %}
HURRY! You have {{difference_days}} days left in your trial, make sure you upgrade!

{% elsif difference_days == 2 %}
LAST CHANCE! You have {{difference_days}} days left in your trial. Make sure you upgrade!

{% else %}
You have few days left in your trial. Make sure to upgrade!
{% endif %}
```
{% endraw %}

### Personalizar mensagens no app com base na data e no idioma do usuário {#countdown-personalize-language}

Este caso de uso calcula uma contagem regressiva para um evento e, com base na configuração de idioma do usuário, exibe a contagem regressiva no idioma dele.

Por exemplo, você pode enviar uma série de mensagens de upsell para os usuários uma vez por mês, informando por quanto tempo uma oferta ainda é válida, com quatro mensagens no app:

- Inicial
- Faltam 2 dias
- Falta 1 dia
- Último dia

{% raw %}
```liquid
{% assign today = 'now' | date: "%s" %}
{% assign end_date = "2021-04-16T23:59:59" | date: "%s" %}
{% assign difference = end_date | minus: today %}
{% assign difference_days = difference | divided_by: 86400 %}
{% if {{difference_days}} >= 3 %}
{% if ${language} == 'de' %}

Hallo, das Angebot gilt bis zum 16.04.

{% elsif ${language} == 'ch' %}
Grüezi, das Angebot gilt bis zum 16.04.

{% elsif ${language} == 'en' %}
The offer is valid until 16.04.

{% else %}
The offer is valid until 16.04.

{% endif %}
{% elsif {{difference_days}} == 2 %}
{% if ${language} == 'de' %}
INSERT MESSAGE

{% elsif ${language} == 'ch' %}
INSERT MESSAGE

{% elsif ${language} == 'en' %}
INSERT MESSAGE

{% else %}
INSERT MESSAGE
{% endif %}

{% elsif {{difference_days}} == 1 %}
{% if ${language} == 'de' %}
INSERT MESSAGE

{% elsif ${language} == 'ch' %}
INSERT MESSAGE

{% elsif ${language} == 'en' %}
INSERT MESSAGE

{% else %}
INSERT MESSAGE
{% endif %}

{% elsif {{difference_days}} == 0 %}
{% if ${language} == 'de' %}
Hallo, das Angebot gilt noch heute.

{% elsif ${language} == 'ch' %}
Hallo, das Angebot gilt noch heute.

{% elsif ${language} == 'en' %}
Grüezi, das Angebot gilt noch heute.

{% else %}
Hi, the offer is only valid today.
{% endif %}

{% else %}
{% abort_message("Calculation failed") %}
{% endif %}
```
{% endraw %}

{% alert important %}
Você precisará atribuir um valor de `date` e incluir lógica de cancelamento caso a data fornecida esteja fora do intervalo de datas. Para cálculos exatos de dia, a data final atribuída deve incluir 23:59:59.
{% endalert %}

### Inserir a data de 30 dias a partir de agora, formatada como mês e dia {#countdown-template-date}

Este caso de uso exibe a data de 30 dias a partir de agora para uso em mensagens.

{% raw %}
```liquid
{% assign today = 'now' | date: "%s" %}
{% assign thirty_days = today | plus: 2592000 | date: "%B %d" %}
```
{% endraw %}

{% endapi %}

{% api %}

## Atributo personalizado {#custom-attribute}

{% apitags %}
Custom attribute
{% endapitags %}

- [Personalizar uma mensagem com base em atributos personalizados correspondentes](#attribute-matching)
- [Formatar moeda para convenções numéricas europeias](#european-currency-format)
- [Subtrair dois atributos personalizados para exibir a diferença como valor monetário](#attribute-monetary-difference)
- [Referenciar o primeiro nome de um usuário se o nome completo estiver armazenado no campo first_name](#attribute-first-name)

### Personalizar uma mensagem com base em atributos personalizados correspondentes {#attribute-matching}

Este caso de uso verifica se um usuário possui atributos personalizados específicos e, em caso positivo, exibe diferentes mensagens personalizadas.

{% raw %}
```liquid
{% if custom_attribute.${hasShovel} == true and custom_attribute.${VisitToGroundTooTough} > 0 %}
The ground is very hard. The dirt road goes East.
{% elsif custom_attribute.${hasShovel} == true %}
The dirt road goes East.
{% elsif custom_attribute.${VisitToStart} > 0 %}
The dirt road goes East.
The shovel here.
{% else %}
You are at a dead-end of a dirt road. The road goes to the east. In the distance, you can see that it will eventually fork off. The trees here are very tall royal palms, and they are spaced equidistant from each other.
There is a shovel here.
{% endif %}
```
{% endraw %}

### Formatar moeda para convenções numéricas europeias {#european-currency-format}

Para localidades que usam vírgula como separador decimal e ponto como separador de milhares (por exemplo, Alemanha ou Itália), use os filtros [`money`]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/filters#money-filter) e [`number_with_delimiter`]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters#number-formatting-filters) com `replace` para trocar os separadores. Use `#` como um espaço reservado temporário para que pontos e vírgulas não sejam trocados na mesma passagem.

{% raw %}
```liquid
{{ 1234567.89 | money | number_with_delimiter | replace: '.', '#' | replace: ',', '.' | replace: '#', ',' }}
```

**Saída:** `1.234.567,89`

**Explicação:** O filtro `money` adiciona casas decimais, mas não adiciona um símbolo de moeda ou separadores específicos de localidade. `number_with_delimiter` adiciona separadores de milhares no estilo americano, e os filtros `replace` os convertem para a formatação europeia.
{% endraw %}

### Subtrair dois atributos personalizados para exibir a diferença como valor monetário {#attribute-monetary-difference}

Este caso de uso captura dois atributos personalizados monetários, calcula e exibe a diferença para informar ao usuário quanto falta para atingir sua meta.

{% raw %}
```liquid
{% assign event_goal = {{custom_attribute.${last_selected_event_personal_goal}}} %}
{% assign current_raised =  {{custom_attribute.${last_selected_event_personal_amount_raised}}} %}
{% assign difference =  event_goal | minus: current_raised %}
You only have ${{ difference | round: 0 | number_with_delimiter }} left to raise!
```
{% endraw %}

### Referenciar o primeiro nome de um usuário se o nome completo estiver armazenado no campo first_name {#attribute-first-name}

Este caso de uso captura o primeiro nome de um usuário (se o nome e sobrenome estiverem armazenados em um único campo) e usa esse primeiro nome para exibir uma mensagem de boas-vindas.

{% raw %}
```liquid
{{${first_name} | truncatewords: 1, "" | default: 'hi'}}
{% assign name = {{${first_name}}} | split: ' ' %}
Hi {{name[0]}}, here's your message!
```

**Explicação:** O filtro `split` transforma a string contida em `{{${first_name}}}` em um array. Ao usar `{{name[0]}}`, referenciamos apenas o primeiro item do array, que é o primeiro nome do usuário.

{% endraw %}
{% endapi %}

{% api %}

## Evento personalizado {#custom-event}

{% apitags %}
Custom event
{% endapitags %}

- [Cancelar notificação por push se um evento personalizado estiver a menos de duas horas](#event-abort-push)
- [Enviar uma campanha cada vez que um usuário realizar um evento personalizado três vezes](#event-three-times)
- [Enviar uma mensagem para usuários que compraram de apenas uma categoria](#event-purchased-one-category)
- [Rastrear quantas vezes um evento personalizado ocorreu no último mês](#track)


### Cancelar notificação por push se um evento personalizado estiver a menos de duas horas {#event-abort-push}

Este caso de uso calcula o tempo até um evento e, dependendo do tempo restante, exibe diferentes mensagens personalizadas.

Por exemplo, você pode querer impedir que um push seja enviado se uma propriedade de evento personalizado estiver a menos de duas horas. Este exemplo usa o cenário de um carrinho abandonado para uma passagem de trem.

{% raw %}
```liquid
{% assign today =  'now' | date: "%s"  %}
{% assign dep_time = {{event_properties.${outboundDate_Time}}} | date: "%s" %}
{% assign time_to_dep = dep_time | minus: today %}
{% if {{time_to_dep}} <= 7200 %}
{% abort_message("OutboundDate less than 2 hours") %}
{% elsif {{time_to_dep}} > 7200 and {{time_to_dep}} < 86400 %}
Don't forget to buy your ticket to {{event_properties.${toStation}}} within next 24 hours
{% else %}
Still traveling to {{event_properties.${toStation}}} in more than 24 hours? Book now
{% endif %}
```
{% endraw %}

### Enviar uma campanha cada vez que um usuário realizar um evento personalizado três vezes {#event-three-times}

Este caso de uso verifica se um usuário realizou um evento personalizado três vezes e, em caso positivo, exibe uma mensagem ou envia uma campanha.

{% raw %}
```liquid
{% assign cadence = custom_attribute.${example} | minus: 1 | modulo: 3 %}
{% if custom_attribute.${example} == blank %}
{% abort_message("Error calculating cadence") %}
{% elsif cadence != 0 %}
{% abort_message("Skip message") %}
{% endif %}
Did you forget something in your shopping cart?
```
{% endraw %}

{% alert important %} Você precisa ter uma propriedade de evento com a contagem do evento personalizado ou usar um webhook para o endpoint da Braze. Isso serve para incrementar um atributo personalizado (`example_event_count`) toda vez que o usuário realizar o evento. Este exemplo usa uma cadência de três (1, 4, 7, 10, etc.). Para iniciar a cadência a partir de zero (0, 3, 6, 9, etc.), remova `minus: 1`.
{% endalert %}

### Enviar uma mensagem para usuários que compraram de apenas uma categoria {#event-purchased-one-category}

Este caso de uso captura uma lista das categorias de compra de um usuário e, se existir apenas uma categoria de compra, exibe uma mensagem.

{% raw %}
```liquid
{% assign category = {{custom_attribute.${categories_purchased}}} %}
{% assign uniq_cat = {{category | uniq }} %}
{% if {{uniq_cat | size}} == 1 %}
{{uniq_cat}}
{% else %}
{% abort_message("Purchase category doesn't exist") %}
{% endif %}
```
{% endraw %}

### Rastrear quantas vezes um evento personalizado ocorreu no último mês {#track}

Este caso de uso calcula o número de vezes que um evento personalizado foi registrado entre o 1º dia do mês atual e o mês anterior. Você pode então executar uma chamada users/track para atualizar e armazenar esse valor como um atributo personalizado. Observe que esta campanha precisaria ser executada por dois meses consecutivos antes que os dados mensais possam ser utilizados.

{% raw %}
```liquid

{% capture body %}
{
 "braze_id": "{{${braze_id}}}",
 "fields_to_export": ["custom_events"]
}

{% endcapture %}

{% connected_content YOUR_BRAZE_ENDPOINT/users/export/ids
 :method post
  :headers { "Authorization": "Bearer YOUR_API_KEY" }
  :body {{body}}
 :content_type application/json
 :save response
  :retry %}

{% for custom_event in response.users[0].custom_events %}
{% assign ce_name = custom_event.name %}
{% comment %} The following custom event name will need to be amended for the target custom event. {% endcomment %}

{% if ce_name == "Project Exported" %}
{% comment %}{{custom_event.name}}: {{custom_event.count}}{% endcomment %}
{% assign current_count = custom_event.count %}
{% endif %}
{% endfor %}

{% assign prev_month_count = {{custom_attribute.${projects_exported_prev_month}}} %}
{% assign latest_count = current_count | minus: prev_month_count %}
{% assign now = "now" | date: "%s" %}
{% assign yesterday = {{now}} | minus: 86400 %}
{% assign previous_month = {{yesterday}} | date: "%B" %}
{% assign previous_year = {{yesterday}} | date: "%y" %}
{% assign formatted_month = previous_month | downcase %}
{% comment %}The Custom Event name that is being tracked will be needed to be amended for the target Custom Event in the Attribute Name below. {% endcomment %}
```

```json
"attributes": [
  {
    "external_id":"{{${user_id}}}",
       "projects_exported_{{formatted_month}}_{{previous_year}}": "{{latest_count}}"
  }
]
```

{% endraw %}

{% endapi %}

{% api %}

## Idioma {#language}

{% apitags %}
Language
{% endapitags %}

- [Exibir nomes de meses em um idioma diferente](#language-display-month)
- [Exibir uma imagem com base no idioma do usuário](#language-image-display)
- [Personalizar mensagens com base no dia da semana e no idioma do usuário](#language-personalize-message)

### Exibir nomes de meses em um idioma diferente {#language-display-month}

Este caso de uso exibe a data atual, mês e ano, com o mês em um idioma diferente. O exemplo fornecido usa sueco.

{% raw %}
```liquid
{% assign day = 'now' | date: "%e" %}
{% assign year =  'now' | date: "%Y" %}
{% assign month =  'now' | date: "%B" %}

{% if {{month}} == 'January' %}
{{day}} Januari {{year}}
{% elsif {{month}} == 'February' %}
{{day}} Februari {{year}}
{% elsif {{month}} == 'March' %}
{{day}} Mars {{year}}
{% elsif {{month}} == 'April' %}
{{day}} April {{year}}
{% elsif {{month}} == 'May' %}
{{day}} Maj {{year}}
{% elsif {{month}} == 'June' %}
{{day}} Juni {{year}}
{% elsif {{month}} == 'July' %}
{{day}} Juli {{year}}
{% elsif {{month}} == 'August' %}
{{day}} Augusti {{year}}
{% elsif {{month}} == 'September' %}
{{day}} September {{year}}
{% elsif {{month}} == 'October' %}
{{day}} Oktober {{year}}
{% elsif {{month}} == 'November' %}
{{day}} November {{year}}
{% elsif {{month}} == 'December' %}
{{day}} December {{year}}
{% endif %}
```
{% endraw %}

### Exibir uma imagem com base no idioma do usuário {#language-image-display}

Este caso de uso exibe uma imagem com base no idioma do usuário. Observe que este caso de uso foi testado apenas com imagens enviadas para a Biblioteca de mídia da Braze.

{% raw %}
```liquid
{% if ${language} == 'en' %}
English image URL (for example, https://cdn-staging.braze.com/appboy/communication/assets/image_assets/images/60aecba96a93150c749b4d57/original.png?1622068137)
{% elsif ${language} == 'ru' %}
Russian image URL
{% elsif ${language} == 'es' %}
Spanish image URL
{% else %}
Fallback image URL
{% endif %}
```
{% endraw %}

### Personalizar mensagens com base no dia da semana e no idioma do usuário {#language-personalize-message}

Este caso de uso verifica o dia da semana atual e, com base no dia, se o idioma do usuário estiver definido como uma das opções de idioma fornecidas, exibe uma mensagem específica no idioma dele.

O exemplo fornecido para na terça-feira, mas pode ser repetido para cada dia da semana.

{% raw %}
```liquid
{% assign today  = 'now' | date: '%A' %}

{% if today == 'Monday' %}
{% if ${language} == 'es' %}
Compra hoy y lleva tu aprendizaje de idiomas a niveles más altos. 🚀

{% elsif ${language} == 'en' %}
Purchase today and take your language learning to the next level. 🚀

{% elsif ${language} == 'zh' %}
今天就购买并将您的语言提高到一个新水平吧。🚀

{% else %}
It's Monday, but the language doesn't match
{% endif %}

{% elsif today == 'Tuesday' %}

{% if ${language} == 'zh' %}
不要忘记解锁以获取完整版本哦。🔓

{% elsif ${language} == 'en' %}
Don't forget to unlock the full version of your language. 🔓

{% elsif ${language} == 'ja' %}
すべての機能を使ってみませんか 🔓

{% elsif ${language} == 'es' %}
No te olivides de desbloquear la versión completa del programa de idiomas. 🔓

{% else %}
tuesday default
{% endif %}
{% endif %}
```
{% endraw %}

{% endapi %}

{% api %}

## Diversos {#miscellaneous}

{% apitags %}
Miscellaneous
{% endapitags %}

- [Evitar o envio de e-mails para clientes que bloquearam e-mails de marketing](#misc-avoid-blocked-emails)
- [Usar o estado de inscrição de um cliente para personalizar conteúdo em mensagens](#misc-personalize-content)
- [Colocar em maiúscula a primeira letra de cada palavra em uma string](#misc-capitalize-words-string)
- [Comparar o valor de um atributo personalizado com um array](#misc-compare-array)
- [Criar um lembrete de evento futuro](#misc-event-reminder)
- [Encontrar uma string dentro de um array](#misc-string-in-array)
- [Encontrar o maior valor em um array](#misc-largest-value)
- [Encontrar o menor valor em um array](#misc-smallest-value)
- [Consultar o final de uma string](#misc-query-end-of-string)
- [Consultar valores em um array de um atributo personalizado com múltiplas combinações](#misc-query-array-values)
- [Formatar uma string como número de telefone](#phone-number)

### Evitar o envio de e-mails para clientes que bloquearam e-mails de marketing {#misc-avoid-blocked-emails}

Este caso de uso pega uma lista de usuários bloqueados salva em um Content Block e verifica se esses usuários bloqueados não são contatados ou direcionados em Campaigns ou Canvas futuros.

{% alert important %}
Para usar este Liquid, primeiro salve a lista de e-mails bloqueados em um Content Block. A lista não deve ter espaços ou caracteres adicionais inseridos entre os endereços de e-mail (por exemplo, `test@braze.com,abc@braze.com`).
{% endalert %}

{% raw %}
```liquid
{% assign blocked_emails = {{content_blocks.${BlockedEmailList}}} | split: ',' %}
{% for email in blocked_emails %}
    {% if {{${email_address}}} == email %}
    {% abort_message("Email is blocked") %}
    {% break %}
    {% endif %}
{% endfor %}
Your message here!
```
{% endraw %}

**Explicação:** Aqui, verificamos se o e-mail do potencial destinatário está nesta lista, referenciando o Content Block de e-mails bloqueados. Se o e-mail for encontrado, a mensagem não será enviada.

{% alert note %}
Content Blocks têm um limite de tamanho de 5 MB.
{% endalert %}

### Usar o estado de inscrição de um cliente para personalizar conteúdo em mensagens {#misc-personalize-content}

Este caso de uso usa o estado de inscrição de um cliente para enviar conteúdo personalizado. Clientes inscritos em um grupo de inscrições específico receberão uma mensagem exclusiva para grupos de inscrições de e-mail.

{% raw %}
```liquid
{% if {{subscribed_state.${subscription_group_id}}} == 'subscribed' %}
This is an exclusive message for subscribed users!
{% else %} This is the default message for other users.
{% endif %}
```
{% endraw %}

### Colocar em maiúscula a primeira letra de cada palavra em uma string {#misc-capitalize-words-string}

Este caso de uso pega uma string de palavras, divide-as em um array e coloca em maiúscula a primeira letra de cada palavra.

{% raw %}
```liquid
{% assign words_array = {{custom_attribute.${address}}} | split: ' ' %}
{% for words in {{words_array}} %}
{{ words | capitalize | append: ' ' }}
{% endfor %}
```
{% endraw %}

**Explicação:** Aqui, atribuímos uma variável ao nosso atributo de string escolhido e usamos o filtro `split` para dividir a string em um array. Em seguida, usamos a tag `for` para atribuir a variável `words` a cada um dos itens do nosso array recém-criado, antes de exibir essas palavras com o filtro `capitalize` e o filtro `append` para adicionar espaços entre cada um dos termos.

### Comparar o valor de um atributo personalizado com um array {#misc-compare-array}

Este caso de uso pega uma lista de lojas favoritas, verifica se alguma das lojas favoritas de um usuário está nessa lista e, em caso positivo, exibe uma oferta especial dessas lojas.

{% raw %}
```liquid
{% assign favorite_stores = 'Target,Walmart,Costco' | split: ',' %}
{% for store in favorite_stores %}
{% if {{custom_attribute.${favorited_stores}}} contains {{store}} %}
Today's offer from {{store}}

{% break %}

{% else %}
{% abort_message("No attribute found") %}
{% endif %}
{% endfor %}
```
{% endraw %}

{% alert important %} Esta sequência tem uma tag `break` na declaração condicional principal. Isso faz com que o loop pare quando uma correspondência é encontrada. Se você quiser exibir muitas ou todas as correspondências, remova a tag `break`. {% endalert %}

### Criar um lembrete de evento futuro {#misc-event-reminder}

Este caso de uso permite que os usuários configurem lembretes futuros com base em eventos personalizados. O cenário de exemplo permite que um usuário defina um lembrete para uma data de renovação de apólice que esteja a 26 ou mais dias de distância, onde os lembretes são enviados 26, 13, 7 ou 2 dias antes da data de renovação da apólice.

Com este caso de uso, o seguinte deve ir no corpo de uma [campanha de webhook]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook) ou etapa do Canvas.

{% raw %}
```liquid
{% comment %}
Depending on how the reminder_capture property is passed to Braze, with/without a timestamp, the number of days could impact whether a user falls on either side of the 26/13/7/2-day windows.
Once users have been assigned to a Reminder journey/flow, they are then scheduled to enter a subsequent Canvas.
This 'Event Listener' can be used to split out users into different journeys based on the Custom Event properties sent to Braze.
{% endcomment %}

{% comment %}
When testing, make sure the campaign ID, campaign API endpoint, Canvas ID, Canvas API endpoint are entered correctly. In this example, the Canvas ID and Canvas API endpoint have been set up for sharing with the client. In practice, this can be testing using a campaign ID and Campaign API endpoint.
{% endcomment %}

{% comment %}
The following step calculates how much there is between today's date and the Reminder Date as 'time_to_reminder'.
{% endcomment %}

{% assign today = "now" | date: '%s' %}
{% assign reminder_start_date = {{event_properties.${reminder_date}}} | date: '%s' %}
{% assign time_to_reminder = reminder_start_date | minus: today %}

{% comment %}
The following step checks if the time_to_reminder is more than 26 days away; if this is true, then the user is scheduled to enter the subsequent Canvas 26 days before the reminder_date.
The time is converted from 'seconds from 1970' to the appropriate Reminder Date in the required ISO 8601 format.
N.B. Additional time zones would need to be catered for by adding an additional API Schedule property of "in_local_time"
{% endcomment %}

{% if {{time_to_reminder}} > 2246400 %}
{% assign time_to_first_message = reminder_start_date | plus: 2246400 %}
{{ time_to_first_message | date: '%Y-%m-%dT%H:%M' }}
{
"canvas_id": "954e15bc-af93-9dc8-a863-ad2580f1750e",
"recipients": [
{
"external_user_id": "{{${user_id}}}"
}
],
"trigger_properties" : {
"enquiry_id" : "{{event_properties.${reminder_id}}}",
"reminder_date" : "{{event_properties.${reminder_date} | date: '%Y-%m-%dT%H:%M:%S+0000'}}",
"message_personalisation_X" : "{{event_properties.${property_x}}}",
"message_personalisation_Y" : "{{event_properties.${property_y}}}",
"message_personalisation_Z" : "{{event_properties.${property_z}}}"
},

"schedule": {
"time": "{{ time_to_first_message | date: '%Y-%m-%dT%H:%M:%S+0000' }}"
}
}

{% comment %}
The following step checks if the time_to_reminder is less than 26 days away but more than 13 days away.
Users are scheduled to enter the journey on day 13.
{% endcomment %}

{% elsif 1123200 > {{time_to_reminder}} and {{time_to_reminder}} < 2246399 %}
{% assign time_to_first_message = reminder_start_date | plus: 1123200 %}

{
"canvas_id": "954e15bc-af93-9dc8-a863-ad2580f1750e",
"recipients": [
{
"external_user_id": "{{${user_id}}}"
}
],
"trigger_properties" : {
"enquiry_id" : "{{event_properties.${reminder_id}}}",
"reminder_date" : "{{event_properties.${reminder_date} | date: '%Y-%m-%dT%H:%M:%S+0000'}}",
"message_personalisation_X" : "{{event_properties.${property_x}}}",
"message_personalisation_Y" : "{{event_properties.${property_y}}}",
"message_personalisation_Z" : "{{event_properties.${property_z}}}"
},

"schedule": {
"time": "{{ time_to_first_message | date: '%Y-%m-%dT%H:%M:%S+0000' }}"
}
}

{% comment %}
The following step checks if the time_to_reminder is less than 13 days away but more than seven days away.
Users are scheduled to enter the journey on day 7.
{% endcomment %}

{% elsif 604800 > {{time_to_reminder}} and {{time_to_reminder}} < 1123199 %}
{% assign time_to_first_message = reminder_start_date | plus: 604800 %}

{
"canvas_id": "954e15bc-af93-9dc8-a863-ad2580f1750e",
"recipients": [
{
"external_user_id": "{{${user_id}}}"
}
],
"trigger_properties" : {
"enquiry_id" : "{{event_properties.${reminder_id}}}",
"reminder_date" : "{{event_properties.${reminder_date} | date: '%Y-%m-%dT%H:%M:%S+0000'}}",
"message_personalisation_X" : "{{event_properties.${property_x}}}",
"message_personalisation_Y" : "{{event_properties.${property_y}}}",
"message_personalisation_Z" : "{{event_properties.${property_z}}}"
},

"schedule": {
"time": "{{ time_to_first_message | date: '%Y-%m-%dT%H:%M:%S+0000' }}"
}
}

{% comment %}
The following step checks if the time_to_reminder is less than seven days away but more than two days away.
Users are scheduled to enter the journey on day 2.
{% endcomment %}

{% elsif {{time_to_reminder}} < 604799 and {{time_to_reminder}} > 172860 %}
{% assign time_to_first_message = reminder_start_date | plus: 172800 %}

{
"canvas_id": "954e15bc-af93-9dc8-a863-ad2580f1750e",
"recipients": [
{
"external_user_id": "{{${user_id}}}"
}
],
"trigger_properties" : {
"enquiry_id" : "{{event_properties.${reminder_id}}}",
"reminder_date" : "{{event_properties.${reminder_date} | date: '%Y-%m-%dT%H:%M:%S+0000'}}",
"message_personalisation_X" : "{{event_properties.${property_x}}}",
"message_personalisation_Y" : "{{event_properties.${property_y}}}",
"message_personalisation_Z" : "{{event_properties.${property_z}}}"
},

"schedule": {
"time": "{{ time_to_first_message | date: '%Y-%m-%dT%H:%M:%S+0000' }}"
}
}
{% endif %}
```
{% endraw %}

{% alert important %}

Você precisará de um evento personalizado `reminder_capture`, e as propriedades do evento personalizado devem incluir pelo menos:

- `reminder-id`: Identificador do evento personalizado
- `reminder_date`: Data enviada pelo usuário para quando o lembrete deve ser acionado
- `message_personalisation_X`: Quaisquer propriedades necessárias para personalizar a mensagem no momento do envio

{% endalert %}

### Encontrar uma string dentro de um array {#misc-string-in-array}

Este caso de uso verifica se um array de atributo personalizado contém uma string específica e, se existir, exibe uma mensagem específica.

{% raw %}
```liquid
{% if custom_attribute.${PartnershipProgramsNotLinked} contains 'Hertz' %}
Link your Hertz account to use Hertz Fast Lane.
{% endif %}
```
{% endraw %}

### Encontrar o maior valor em um array {#misc-largest-value}

Este caso de uso calcula o maior valor em um determinado array de atributo personalizado para uso em mensagens ao usuário.

Por exemplo, você pode querer mostrar a um usuário qual é a pontuação mais alta atual ou o maior lance em um item.

{% raw %}
```liquid
{% assign maxValue = 0 %}
{% for attribute in {{custom_attribute.${array_attribute}}} %}
{% assign compareValue = {{attribute | plus: 0}} %}
{% if compareValue > maxValue %}
{% assign maxValue = compareValue %}
{% endif %}
{% endfor %}
{{maxValue}}
```
{% endraw %}

{% alert important %}
Você deve usar um atributo personalizado que tenha um valor inteiro e faça parte de um array (lista). {% endalert %}

### Encontrar o menor valor em um array {#misc-smallest-value}

Este caso de uso calcula o menor valor em um determinado array de atributo personalizado para uso em mensagens ao usuário.

Por exemplo, você pode querer mostrar a um usuário qual é a menor pontuação ou o item mais barato.

{% raw %}
```liquid
{% assign minValue = custom_attribute.${array_attribute}[0] | plus: 0 %}
{% for attribute in {{custom_attribute.${array_attribute}}} %}
{% assign compareValue = {{attribute | plus: 0}} %}
{% if compareValue < minValue %}
{% assign minValue = compareValue %}
{% endif %}
{% endfor %}
{{minValue}}
```
{% endraw %}

{% alert important %} Você deve usar um atributo personalizado que tenha um valor inteiro e faça parte de um array (lista). {% endalert %}

### Consultar o final de uma string {#misc-query-end-of-string}

Este caso de uso consulta o final de uma string para uso em mensagens.

{% raw %}
```liquid
{% assign interest = {{custom_attribute.${Buyer Interest}}} | first %}
{% assign marketplace = interest | split: "" | reverse | join: "" | truncate: 4, "" %}
{% if {{marketplace}} == '3243' %}

Your last marketplace search was on {{custom_attribute.${Last marketplace buyer interest} | date: '%d.%m.%Y'}}. Check out all of our new offers.

{% else %}
{% abort_message() %}
{% endif %}
```
{% endraw %}

### Consultar valores em um array de um atributo personalizado com múltiplas combinações {#misc-query-array-values}

Este caso de uso pega uma lista de programas que estão prestes a expirar, verifica se algum dos programas favoritos de um usuário está nessa lista e, em caso positivo, exibe uma mensagem notificando o usuário de que eles expirarão em breve.

{% raw %}
```liquid
{% assign expired_shows = 'Modern Family,The Rookie,Body of Proof,Felicity' | split: ',' %}
{% for show in expired_shows %}
{% if {{custom_attribute.${Favorite Shows}}} contains {{show}} %}
{% assign new_shows = new_shows | append: {{show}} | append: '*' %}
{% endif %}
{% endfor %}
{% assign new_shows_clean = new_shows | split: '*' %}
{% if new_shows_clean.size != 0 %}

All episodes of {{new_shows_clean | join: ', ' }} expire on 9/8 - watch them now before they're gone!

{% else %}
{% abort_message("Not found") %}
{% endif %}
```
{% endraw %}

{% alert important %} Você precisará encontrar correspondências entre os arrays primeiro e depois construir a lógica no final para separar as correspondências. {% endalert %}

### Formatar uma string como número de telefone {#phone-number}

Este caso de uso mostra como indexar o campo de perfil de usuário `phone_number` (que por padrão é formatado como uma string de inteiros) e reformatá-lo com base nos padrões locais de número de telefone. Por exemplo, 1234567890 para (123)-456-7890.

{% raw %}
```liquid
{% assign phone = {{${phone_number}}} | remove: "-" | split: '' %}

({{ phone[0] }}{{ phone[1] }}{{ phone[2] }})-{{ phone[3] }}{{ phone[4] }}{{ phone[5] }}-{{ phone[6] }}{{ phone[7] }}{{ phone[8] }}{{ phone[9] }}
```
{% endraw %}

{% endapi %}

{% api %}

## Direcionamento por plataforma {#platform-targeting}

{% apitags %}
Platform targeting
{% endapitags %}

- [Diferenciar o texto por sistema operacional do dispositivo](#platform-device-os)
- [Direcionar apenas uma plataforma específica](#platform-target)
- [Direcionar apenas dispositivos iOS com uma versão específica do sistema operacional](#platform-target-ios-version)
- [Direcionar apenas navegadores web](#platform-target-web)
- [Direcionar uma operadora de celular específica](#platform-target-carrier)

### Diferenciar o texto por sistema operacional do dispositivo {#platform-device-os}

Este caso de uso verifica em qual plataforma o usuário está e, dependendo da plataforma, exibe mensagens específicas.

Por exemplo, você pode querer mostrar versões mais curtas do texto da mensagem para usuários de celular, enquanto mostra a versão regular e mais longa para outros usuários. Você também pode mostrar certas mensagens relevantes para usuários de celular que não seriam relevantes para usuários web. Por exemplo, mensagens para iOS podem falar sobre Apple Pay, enquanto mensagens para Android devem mencionar Google Pay.

{% raw %}
```liquid
{% if targeted_device.${platform} == "ios" or targeted_device.${platform} == "android" %}
This is a shorter copy.

{% else %}
This is the regular copy and much longer than the short version.
{% endif %}
```
{% endraw %}

{% alert note %}
Liquid diferencia maiúsculas de minúsculas. `targeted_device.${platform}` retorna o valor todo em minúsculas.
{% endalert %}

### Direcionar apenas uma plataforma específica {#platform-target}

Este caso de uso captura a plataforma do dispositivo do usuário e, dependendo da plataforma, exibe uma mensagem.

Por exemplo, você pode querer enviar uma mensagem apenas para usuários Android. Isso pode ser usado como alternativa à seleção de um app dentro da ferramenta de segmentação.

{% raw %}
```liquid
{% if {{targeted_device.${platform}}} == 'android' %}

This is a message for an Android user!

{% else %}
{% abort_message %}
{% endif %}
```
{% endraw %}

### Direcionar apenas dispositivos com uma versão específica do sistema operacional {#platform-target-ios-version}

Este caso de uso verifica se a versão do sistema operacional de um usuário está dentro de um determinado conjunto de versões e, em caso positivo, exibe uma mensagem específica.

O exemplo usado envia um aviso para usuários com versão do sistema operacional 10.0 ou anterior de que o suporte ao sistema operacional do dispositivo está sendo descontinuado.

{% raw %}
```liquid
{% if {{targeted_device.${os}}} == "10.0" or {{targeted_device.${os}}} == "10.0.1" or {{targeted_device.${os}}} == "10.0.2" or {{targeted_device.${os}}} == "10.0.3" or {{targeted_device.${os}}} == "10.1" or {{targeted_device.${os}}} == "10.2" or {{targeted_device.${os}}} == "10.2.1" or {{targeted_device.${os}}} == "10.3" or {{targeted_device.${os}}} == "10.3.1" or {{targeted_device.${os}}} == "10.3.2" or {{targeted_device.${os}}} == "10.3.3" or {{targeted_device.${os}}} == "10.3.4" or {{targeted_device.${os}}} == "9.3.1" or {{targeted_device.${os}}} == "9.3.2" or {{targeted_device.${os}}} == "9.3.3" or {{targeted_device.${os}}} == "9.3.4" or {{targeted_device.${os}}} == "9.3.5" %}

We are phasing out support for your device's operating system. Be sure to update to the latest software for the best app experience.

{% else %}
{% abort_message %}
{% endif %}
```
{% endraw %}

### Direcionar apenas navegadores web {#platform-target-web}

Este caso de uso verifica se o dispositivo alvo de um usuário roda em Mac ou Windows e, em caso positivo, exibe uma mensagem específica.

{% raw %}
```liquid
{% if {{targeted_device.${os}}} == 'Mac' or {{targeted_device.${os}}} == 'Windows' %}

This message will display on your desktop web browser.

{% else %}
{% abort_message %}
{% endif %}
```
{% endraw %}

O caso de uso a seguir verifica se um usuário web está no iOS ou Android e, em caso positivo, exibe uma mensagem específica.

{% raw %}
```liquid
{% if {{targeted_device.${os}}} == 'iOS' and {{targeted_device.${platform}}} == 'web' %}

Content for iOS.

{% elsif {{targeted_device.${os}}} == 'android' and {{targeted_device.${platform}}} == 'web' %}

Content for Android.

{% else %}
{% abort_message %}
{% endif %}
```
{% endraw %}

### Direcionar uma operadora de celular específica {#platform-target-carrier}

Este caso de uso verifica se a operadora do dispositivo de um usuário é Verizon e, em caso positivo, exibe uma mensagem específica.

Para notificações por push e canais de mensagens no app, você pode especificar a operadora do dispositivo no corpo da mensagem usando Liquid. Se a operadora do destinatário não corresponder, a mensagem não será enviada.

{% raw %}
```liquid
{% if {{targeted_device.${carrier}}} contains "verizon" or {{targeted_device.${carrier}}} contains "Verizon" %}

This is a message for Verizon users!

{% else %}
{% abort_message %}
{% endif %}
```
{% endraw %}

{% endapi %}

{% api %}

## SMS

{% apitags %}
SMS
{% endapitags %}

- [Responder com mensagens diferentes com base na palavra-chave de SMS recebida](#sms-keyword-response)

### Responder com mensagens diferentes com base na palavra-chave de SMS recebida {#sms-keyword-response}

Este caso de uso incorpora processamento dinâmico de palavras-chave de SMS para responder a mensagens recebidas específicas com textos diferentes. Por exemplo, você pode enviar respostas diferentes quando alguém envia "START" versus "JOIN".

{% raw %}
```liquid
{% assign inbound_message = {{sms.${inbound_message_body}}} | downcase | strip %}
{% if inbound_message contains 'start' %}
Thanks for joining our SMS program! Make sure your account is up to date for the best deals!

{% elsif inbound_message contains 'join' %}
Thanks for joining our SMS program! Create an account to get the best deals!

{% else %}
Thanks for joining our SMS program!

{% endif %}
```
{% endraw %}

{% endapi %}

{% api %}

## Fusos horários {#time-zones}

{% apitags %}
Time zones
{% endapitags %}

- [Inserir o fuso horário do usuário no modelo](#users-time-zone)
- [Personalizar uma mensagem dependendo do fuso horário do usuário](#personalize-timezone)
- [Adicionar o fuso horário CST a um atributo personalizado](#time-append-cst)
- [Inserir um timestamp](#time-insert-timestamp)
- [Enviar um push do Canvas apenas durante um período de tempo no fuso horário local do usuário](#time-canvas-window)
- [Enviar uma campanha recorrente de mensagem no app durante um período de tempo no fuso horário local do usuário](#time-reocurring-iam-window)
- [Enviar mensagens diferentes em dias úteis versus fins de semana no fuso horário local do usuário](#time-weekdays-vs-weekends)
- [Enviar mensagens diferentes com base no horário do dia no fuso horário local do usuário](#time-of-day)
- [Cancelar uma mensagem fora de um intervalo de horas no momento do envio](#abort-send-time-hour-range)
- [Cancelar uma mensagem fora de um período de tempo em um fuso horário fixo](#abort-fixed-timezone-window)

{% alert note %}
Se um usuário receber uma mensagem em um horário local inesperado, o fuso horário do dispositivo ou do perfil pode ter mudado (por exemplo, após uma viagem). A entrega por horário local usa o fuso horário do perfil no momento do envio; os usuários podem precisar de uma nova sessão na região habitual antes que valores como {% raw %}`{{${time_zone}}}`{% endraw %} reflitam o esperado. No entanto, você pode [inserir o fuso horário do usuário no modelo](#users-time-zone).
{% endalert %}

### Inserir o fuso horário do usuário no modelo {#users-time-zone}

Por padrão, datas e horários em Liquid são renderizados em Tempo Universal Coordenado (UTC). Para exibir datas e horários no fuso horário local do usuário, use o filtro `time_zone` com o filtro `date`.

#### Atribuir data e hora locais {#assign-local-date-and-time}

Para atribuir uma variável que reflita a data e hora atuais no fuso horário local do usuário, use este formato:

{% raw %}
```liquid
{% assign local_date_time = 'now' | time_zone:{{${time_zone}}} | date: '%B %e, %Y' %}
{{local_date_time}}
```
{% endraw %}

- `now`: Recupera a data e hora atuais em UTC.
- `time_zone`: Recupera o fuso horário local do usuário a partir do atributo padrão usando a tag de personalização {% raw %}`{{${time_zone}}}`{% endraw %}.
- `date`: Formata a data e hora locais do usuário de acordo com suas especificações. No exemplo anterior, o sistema exibe uma string formatada como "February 26, 2026". Para mais opções de formatação, consulte [strftime.net](strftime.net).

#### Aplicar o fuso horário do usuário com atributos personalizados {#apply-the-users-time-zone-with-custom-attributes}

Você pode aplicar o filtro `time_zone` a atributos personalizados, assim:

{% raw %}
```liquid
{{custom_attribute.${date_time_attribute} | time_zone: {{${time_zone}}} | date: '%a, %b %e, %Y'}}
```
{% endraw %}

Isso exibe o `date_time_attribute` formatado como o dia da semana abreviado, seguido pelo mês abreviado, dia e ano com quatro dígitos.

### Personalizar uma mensagem dependendo do fuso horário do usuário {#personalize-timezone}

Este caso de uso exibe mensagens diferentes com base no fuso horário do usuário.

{% raw %}
```liquid
{% if {{${time_zone}}} == 'xx' %}
Message for time zone xx.
{% elsif {{${time_zone}}} == 'yy' %}
Message for time zone yy.
{% else %}
{% abort_message("Invalid time zone") %}
{% endif %}
```
{% endraw %}

### Adicionar o fuso horário CST a um atributo personalizado {#time-append-cst}

Este caso de uso exibe um atributo de data personalizado em um determinado fuso horário.

Opção 1:
{% raw %}
```liquid
{{custom_attribute.${application_expires_date} | time_zone: -0005 | date: '%B, %d %Y' }}
```
{% endraw %}

Opção 2:
{% raw %}
```liquid
{{custom_attribute.${application_expires_date} | time_zone: 'America/Chicago' | date: '%B %d %Y %z' }}
```
{% endraw %}

### Inserir um timestamp {#time-insert-timestamp}

Este caso de uso exibe uma mensagem que inclui um timestamp no fuso horário atual do usuário.

O exemplo a seguir exibe a data no formato AAAA-mm-dd HH:MM:SS, como 2021-05-03 10:41:04.

{% raw %}
```liquid
{{${user_id} | default: 'You'}} received a campaign, rendered at ({{ "now" | time_zone: ${time_zone} | date: "%Y-%m-%d %H:%M:%S" }})
```
{% endraw %}

### Enviar um push do Canvas apenas durante um período de tempo no fuso horário local do usuário {#time-canvas-window}

Este caso de uso verifica o horário do usuário no fuso horário local dele e, se estiver dentro de um horário definido, exibe uma mensagem específica.

{% raw %}
```liquid
{% assign time = 'now' | time_zone: ${time_zone} %}
{% assign hour = time | date: '%H' | plus: 0 %}
{% if hour > 20 or hour < 8 %}
{% abort_message("Outside allowed time window") %}
{% endif %}

Here's a message that will send between 8 am and 8 pm!
```
{% endraw %}

### Enviar uma campanha recorrente de mensagem no app durante um período de tempo no fuso horário local do usuário {#time-reoccurring-iam-window}

Este caso de uso exibe uma mensagem se o horário atual do usuário estiver dentro de um período definido.

Por exemplo, o cenário a seguir informa ao usuário que uma loja está fechada.

{% raw %}
```liquid
{% assign time = 'now' | time_zone: ${time_zone} %}
{% assign hour = time | date: '%H' | plus: 0 %}
{% if hour > 21 or hour < 10 %}

Store's closed. Come back between 11 am and 9 pm!

{% else %}
{% abort_message("Not sent because the store is open") %}
{% endif %}
```
{% endraw %}

### Enviar mensagens diferentes em dias úteis versus fins de semana no fuso horário local do usuário {#time-weekdays-vs-weekends}

Este caso de uso verifica se o dia da semana atual do usuário é sábado ou domingo e, dependendo do dia, exibe mensagens diferentes.

{% raw %}
```liquid
{% assign today = 'now' | time_zone: ${time_zone} | date: "%A" %}
{% if {{today}} == 'Saturday' or {{today}} == 'Sunday' %}
It's {{today}}, why don't you open the app for your transactions?

{% else %}
It's {{today}}, why don't you visit the store?
{% endif %}
```
{% endraw %}

### Enviar mensagens diferentes com base no horário do dia no fuso horário local do usuário {#time-of-day}

Este caso de uso exibe uma mensagem se o horário atual do usuário estiver fora de um período definido.

Por exemplo, você pode querer informar um usuário sobre uma oportunidade com prazo limitado que depende do horário do dia.

{% raw %}
```liquid
{% assign time = 'now' | time_zone: ${time_zone} %}
{% assign hour = time | date: '%H' | plus: 0 %}
{% if hour > 20 or hour < 8 %}
{% abort_message("Outside allowed time window") %}
{% endif %}

Check out this new bar after work today. HH specials!
```
{% endraw %}

{% alert note %} Isso é o oposto do [horário de silêncio]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/delivery_and_entry_types#time-based-options). {% endalert %}

### Cancelar uma mensagem fora de um intervalo de horas no momento do envio {#abort-send-time-hour-range}

Este caso de uso cancela a mensagem quando a hora atual está fora de um intervalo definido. Ele usa o horário em que a mensagem é renderizada, que é UTC por padrão, a menos que você aplique o filtro `time_zone`, e não o fuso horário local do usuário. Para enviar mensagens com base no fuso horário local do usuário, consulte [Enviar mensagens diferentes com base no horário do dia no fuso horário local do usuário](#time-of-day).

{% raw %}
```liquid
{% assign time = 'now' %}
{% assign hour = time | date: '%H' | plus: 0 %}
{% if hour > 20 or hour < 8 %}
{% abort_message("Outside hour range") %}
{% endif %}

Check out this new bar after work today. HH specials!
```
{% endraw %}

### Cancelar uma mensagem fora de um período de tempo em um fuso horário fixo {#abort-fixed-timezone-window}

Este caso de uso cancela a mensagem quando o horário atual está fora de um período definido em um fuso horário específico (horário de Singapura neste exemplo). Você pode usar esse padrão quando precisar de uma regra inspirada no horário de silêncio que esteja vinculada a uma região em vez do atributo `time_zone` de cada usuário.

{% raw %}
```liquid
{% assign time = 'now' | time_zone: 'Asia/Singapore' %}
{% assign hour = time | date: '%H' | plus: 0 %}
{% assign minute = time | date: '%M' | plus: 0 %}

{% if hour < 20 or hour > 21 or (hour == 21 and minute > 45) %}
{% abort_message("Not within eligible time of 8 pm–9:45 pm SGT") %}
{% endif %}

Sign up for our exclusive time-limited offer now!
```
{% endraw %}

{% endapi %}

{% api %}

## Semana/Dia/Mês {#weekdaymonth}

{% apitags %}
Week/Day/Month
{% endapitags %}

- [Inserir o nome do mês anterior em uma mensagem](#month-name)
- [Enviar uma campanha no final de cada mês](#month-end)
- [Enviar uma campanha no último (dia útil) do mês](#day-of-month-last)
- [Enviar uma mensagem diferente a cada dia do mês](#day-of-month)
- [Enviar uma mensagem diferente a cada dia da semana](#day-of-week)
- [Cancelar uma mensagem em uma data específica do calendário](#abort-specific-calendar-date)
- [Cancelar uma mensagem em um dia específico da semana](#abort-specific-weekday)

### Inserir o nome do mês anterior em uma mensagem {#month-name}

Este caso de uso pega o mês atual e exibe o mês anterior para uso em mensagens.

{% raw %}
```liquid
{% assign today = 'now' | date: "%m" %}
{% assign last_month = {{today}} | minus: 1 %}
{% if last_month == 1 %}
{% assign month = "January" %}
{% elsif last_month == 2 %}
{% assign month = "February" %}
{% elsif last_month == 3 %}
{% assign month = "March" %}
{% elsif last_month == 4 %}
{% assign month = "April" %}
{% elsif last_month == 5 %}
{% assign month = "May" %}
{% elsif last_month == 6 %}
{% assign month = "June" %}
{% elsif last_month == 7 %}
{% assign month = "July" %}
{% elsif last_month == 8 %}
{% assign month = "August" %}
{% elsif last_month == 9 %}
{% assign month = "September" %}
{% elsif last_month == 10 %}
{% assign month = "October" %}
{% elsif last_month == 11 %}
{% assign month = "November" %}
{% elsif last_month == 0 %}
{% assign month = "December" %}
{% endif %}

Here's an overview of what your spending looked like in {{month}}.
```
{% endraw %}

Alternativamente, você pode usar o seguinte para obter o mesmo resultado.

{% raw %}
```liquid
{% assign last_month_name = 'now' | date: "%Y-%m-01" | date: '%s' | minus: 1 | date: "%B" %}

Here's an overview of what your spending looked like in {{last_month_name}}.
```
{% endraw %}

### Enviar uma campanha no final de cada mês {#month-end}

Este caso de uso verifica se a data atual está em uma lista de datas e, dependendo da data, exibe uma mensagem específica.

{% alert note %} Isso não considera anos bissextos (29 de fevereiro). {% endalert %}

{% raw %}
```liquid
{% assign current_date = 'now' | date: '%b %d' %}

{% if current_date == "Jan 31" or current_date == "Feb 28" or current_date == "Mar 31" or current_date == "Apr 30" or current_date == "May 31" or current_date == "Jun 30" or current_date == "Jul 31" or current_date == "Aug 31" or current_date == "Sep 30" or current_date == "Oct 31" or current_date == "Nov 30" or current_date == "Dec 31" %}

The date is correct

{% else %}
{% abort_message("Date is not listed") %}
{% endif %}
```
{% endraw %}

### Enviar uma campanha no último (dia útil) do mês {#day-of-month-last}

Este caso de uso captura o mês e o dia atuais e calcula se o dia atual cai no último dia útil do mês.

Por exemplo, você pode querer enviar uma pesquisa para seus usuários na última quarta-feira do mês pedindo feedback sobre o produto.

{% raw %}
```liquid
{% comment %}Pull the day, day name, month, and year from today's date.{% endcomment %}
{% assign current_day = "now" | date: "%d" %}
{% assign current_day_name = "now" | date: "%a" %}
{% assign current_month = "now" | date: "%b" %}
{% assign current_year = "now" | date: "%Y" %}

{% comment %}Assign the correct number of days for the current month.{% endcomment %}

{% if current_month == "Jan" %}
{% assign last_day_of_month = 31 %}
{% elsif current_month == "Mar" %}
{% assign last_day_of_month = 31 %}
{% elsif current_month == "Apr" %}
{% assign last_day_of_month = 30 %}
{% elsif current_month == "May" %}
{% assign last_day_of_month = 31 %}
{% elsif current_month == "Jun" %}
{% assign last_day_of_month = 30 %}
{% elsif current_month == "Jul" %}
{% assign last_day_of_month = 31 %}
{% elsif current_month == "Aug" %}
{% assign last_day_of_month = 31 %}
{% elsif current_month == "Sep" %}
{% assign last_day_of_month = 30 %}
{% elsif current_month == "Oct" %}
{% assign last_day_of_month = 31 %}
{% elsif current_month == "Nov" %}
{% assign last_day_of_month = 30 %}
{% elsif current_month == "Dec" %}
{% assign last_day_of_month = 31 %}
{% endif %}

{% comment %}Assign the correct number of days if the current month is February, taking into account leap years.{% endcomment %}

{% assign leap_year_remainder = current_year | modulo: 4 %}
{% if leap_year_remainder == 0 and current_month == "Feb" %}
{% assign last_day_of_month = 29 %}
{% elsif current_month == "Feb" %}
{% assign last_day_of_month = 28 %}
{% endif %}

{% comment %}Check that today's date is within a week of the last day of the month. If not, abort the message. If so, check that today is Wednesday. If not, abort the message.{% endcomment %}

{% assign diff_in_days = last_day_of_month | minus: current_day | plus: 1%}
{% if diff_in_days <= 7 %}
{% unless current_day_name == "Wed" %}
{% abort_message("Wrong day of the week") %}
{% endunless %}
{% else %}
{% abort_message("Not the last week of the month") %}
{% endif %}
```
{% endraw %}

### Enviar uma mensagem diferente a cada dia do mês {#day-of-month}

Este caso de uso verifica se a data atual corresponde a uma em uma lista e, dependendo do dia, exibe uma mensagem distinta.

{% raw %}
```liquid
{% assign today = 'now' | time_zone: {{${time_zone}}} | date: "%Y-%m-%d" %}
{% assign day_1 = "2019-12-01" | time_zone: {{${time_zone}}} | date: "%Y-%m-%d" %}
{% assign day_2 = "2019-12-02" | time_zone: {{${time_zone}}} | date: "%Y-%m-%d" %}
{% assign day_3 = "2019-12-03" | time_zone: {{${time_zone}}} | date: "%Y-%m-%d" %}

{% if today == day_1 %}
Message for 2019-12-01

{% elsif today == day_2 %}
Message for 2019-12-02

{% elsif today == day_3%}
Message for 2019-12-03

{% else %}
{% abort_message("Date not listed") %}
{% endif %}
```
{% endraw %}

### Enviar uma mensagem diferente a cada dia da semana {#day-of-week}

Este caso de uso verifica o dia da semana atual e, dependendo do dia, exibe uma mensagem distinta.

{% raw %}
```liquid
{% assign today = 'now' | date: "%A" %}
{% case today %}
{% when 'Monday' %}
Monday copy

{% when 'Tuesday' %}
Tuesday copy

{% when 'Wednesday' %}
Wednesday copy

{% when  'Thursday' %}
Thursday copy

{% when  'Friday' %}
Friday copy

{% when 'Saturday' %}
Saturday copy

{% when 'Sunday' %}
Sunday copy

{% else %}
Default copy
{% endcase %}
```
{% endraw %}

{% alert note %}
Você pode substituir a linha "Default copy" por {% raw %}`{% abort_message() %}`{% endraw %} para impedir que a mensagem seja enviada se o dia da semana for desconhecido.
{% endalert %}

### Cancelar uma mensagem em uma data específica do calendário {#abort-specific-calendar-date}

Este caso de uso cancela a mensagem em um mês e dia escolhidos todos os anos (5 de maio no exemplo). Ele compara a data atual com uma string inequívoca de mês e dia construída com o filtro `date`.

{% raw %}
```liquid
{% assign date = 'now' | date: '%d/%m' %}
{% if date == '05/05' %}
{% abort_message('No message on the 5th of May') %}
{% endif %}
```
{% endraw %}

### Cancelar uma mensagem em um dia específico da semana {#abort-specific-weekday}

Este caso de uso cancela a mensagem quando o Liquid é executado em um determinado dia da semana (`Wednesday` no exemplo). O filtro `%A` retorna o nome completo do dia da semana em inglês.

{% raw %}
```liquid
{% assign weekday = 'now' | date: '%A' %}
{% if weekday == 'Wednesday' %}
{% abort_message("No message on Wednesdays") %}
{% endif %}
```
{% endraw %}

{% endapi %}

Muitos exemplos nesta biblioteca usam a tag `abort_message` para pular um envio quando as condições não são atendidas. Para uma referência completa sobre como cancelar envios com Liquid, incluindo padrões baseados em data e hora, consulte [Cancelar mensagens Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages).