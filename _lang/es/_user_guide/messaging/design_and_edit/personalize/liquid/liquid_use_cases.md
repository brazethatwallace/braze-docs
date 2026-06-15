---
nav_title: Biblioteca de casos de uso de Liquid
article_title: Biblioteca de casos de uso de Liquid
page_order: 10
search_rank: 2
excerpt_separator: ""
page_type: glossary
layout: liquid_use_case_glossary
description: "Esta página de inicio alberga ejemplos de casos de uso de Liquid organizados por categoría, como aniversarios, uso de la aplicación, cuentas regresivas y más."

---

{% api %}

## Aniversarios y festivos {#anniversaries-and-holidays}

{% apitags %}
Anniversaries and holidays
{% endapitags %}

- [Personalizar mensajes según el año de aniversario de un usuario](#anniversary-year)
- [Personalizar mensajes según la semana de cumpleaños de un usuario](#birthday-week)
- [Enviar Campaigns a usuarios en su mes de cumpleaños](#birthday-month)
- [Evitar enviar mensajes en festivos importantes](#holiday-avoid)

### Personalizar mensajes según el año de aniversario de un usuario {#anniversary-year}

Este caso de uso muestra cómo calcular el aniversario de un usuario en la aplicación a partir de su fecha de registro inicial y mostrar diferentes mensajes según cuántos años está celebrando.

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

**Explicación:** Aquí usamos la variable reservada `now` para insertar la fecha y hora actuales en formato [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601). Los filtros `%B` (mes como "May") y `%d` (día como "18") formatean el mes y el día actuales. Luego usamos los mismos filtros de fecha y hora en los valores de `signup_date` para asegurarnos de poder comparar ambos valores usando etiquetas condicionales y lógica.

Después repetimos tres declaraciones de variables más para obtener `%B` y `%d` de `signup_date`, pero también añadimos `%Y` (año como "2021"). Esto convierte la fecha y hora de `signup_date` en solo el año. Conocer el día y el mes nos permite verificar si el aniversario del usuario es hoy, y conocer el año nos dice cuántos años han pasado, lo que nos permite saber por cuántos años felicitarle.

{% alert tip %} Puedes crear tantas condiciones como años lleves recopilando fechas de registro. {% endalert %}

### Personalizar mensajes según la semana de cumpleaños de un usuario {#birthday-week}

Este caso de uso muestra cómo encontrar el cumpleaños de un usuario, compararlo con la fecha actual y luego mostrar mensajes especiales de cumpleaños antes, durante y después de su semana de cumpleaños.

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

**Explicación:** Similar al caso de uso del [año de aniversario](#anniversary-year), aquí tomamos la variable reservada `now` y usamos el filtro `%W` (semana, como la semana 12 de 52 en un año) para obtener el número de semana del año en el que cae el cumpleaños del usuario. Si la semana de cumpleaños del usuario coincide con la semana actual, le enviamos un mensaje de felicitación.

También incluimos declaraciones para `last_week` y `next_week` para personalizar aún más tu mensajería.

### Enviar Campaigns a usuarios en su mes de cumpleaños {#birthday-month}

Este caso de uso muestra cómo calcular el mes de cumpleaños de un usuario, verificar si su cumpleaños cae en el mes actual y, de ser así, enviar un mensaje especial.

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

**Explicación:** Similar al caso de uso de la [semana de cumpleaños](#birthday-week), excepto que aquí usamos el filtro `%B` (mes como "May") para calcular qué usuarios cumplen años este mes. Una posible aplicación podría ser dirigirse a los usuarios que cumplen años en un correo electrónico mensual.

### Evitar enviar mensajes en festivos importantes {#holiday-avoid}

Este caso de uso muestra cómo enviar mensajes durante el período festivo evitando los días de festivos importantes, cuando la interacción probablemente sea baja.

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

**Explicación:** Aquí asignamos el término `today` a la variable reservada `now` (la fecha y hora actuales), usando los filtros `%Y` (año como "2023"), `%m` (mes como "12") y `%d` (día como "25") para formatear la fecha. Luego ejecutamos nuestra declaración condicional para decir que si la variable `today` coincide con los días festivos de tu elección, el mensaje será cancelado.

El ejemplo proporcionado usa Nochebuena, Navidad y el día después de Navidad (Boxing Day).

{% endapi %}

{% api %}

## Uso de la aplicación {#app-usage}

{% apitags %}
App usage
{% endapitags %}

- [Enviar mensajes en el idioma de un usuario si no ha registrado una sesión](#app-session-language)
- [Personalizar mensajes según cuándo un usuario abrió la aplicación por última vez](#app-last-opened)
- [Mostrar un mensaje diferente si un usuario usó la aplicación hace menos de tres días](#app-last-opened-less-than)

### Enviar mensajes en el idioma de un usuario si no ha registrado una sesión {#app-session-language}

Este caso de uso verifica si un usuario ha registrado una sesión y, si no, incluye lógica para mostrar un mensaje basado en el idioma recopilado manualmente a través de un atributo personalizado, si existe. Si no hay información de idioma vinculada a su cuenta, mostrará el mensaje en el idioma predeterminado. Si un usuario ha registrado una sesión, extraerá cualquier información de idioma vinculada al usuario y mostrará el mensaje apropiado.

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
**Explicación:** Aquí usamos dos declaraciones `if` agrupadas y anidadas. La primera declaración `if` verifica si el usuario ha iniciado una sesión comprobando si `last_used_app_date` es `nil`. Esto se debe a que `{{${language}}}` es recopilado automáticamente por el SDK cuando un usuario registra una sesión. Si el usuario no ha registrado una sesión, aún no tendremos su idioma, por lo que esto verifica si se han guardado atributos personalizados relacionados con el idioma y, basándose en esa información, mostrará un mensaje en ese idioma, si es posible.
{% endraw %}

La segunda declaración `if` simplemente verifica el atributo estándar (predeterminado) porque el usuario no tiene `nil` para `last_used_app_date`, lo que significa que ha registrado una sesión y tenemos su idioma.

{% alert note %}
[`Nil`](https://shopify.github.io/liquid/basics/types/#nil) es una variable reservada que se devuelve cuando el código Liquid no tiene resultados. `Nil` se trata como `false` en un bloque `if`.
{% endalert %}

### Personalizar mensajes según cuándo un usuario abrió la aplicación por última vez {#app-last-opened}

Este caso de uso calcula la última vez que un usuario abrió tu aplicación y mostrará un mensaje personalizado diferente según el tiempo transcurrido.

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

### Mostrar un mensaje diferente si un usuario usó la aplicación hace menos de tres días {#app-last-opened-less-than}

Este caso de uso calcula hace cuánto tiempo un usuario usó tu aplicación y, según el tiempo transcurrido, mostrará un mensaje personalizado diferente.

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

## Cuentas regresivas {#countdowns}

{% apitags %}
Countdowns
{% endapitags %}

- [Añadir X días a la fecha de hoy](#countdown-add-x-days)
- [Calcular una cuenta regresiva desde un punto fijo en el tiempo](#countdown-difference-days)
- [Crear una cuenta regresiva para fechas y prioridades de envío específicas](#countdown-shipping-options)
- [Crear una cuenta regresiva en días](#countdown-days)
- [Crear una cuenta regresiva de días a horas a minutos](#countdown-dynamic)
- [Mostrar cuántos días faltan hasta una fecha determinada](#countdown-future-date)
- [Mostrar cuántos días faltan hasta que llegue un atributo de fecha personalizado](#countdown-custom-date-attribute)
- [Mostrar cuánto tiempo queda y cancelar el mensaje si solo queda X tiempo](#countdown-abort-window)
- [Mensaje dentro de la aplicación para enviar X días antes de que termine la membresía del usuario](#countdown-membership-expiry)
- [Personalizar mensajes dentro de la aplicación según la fecha y el idioma del usuario](#countdown-personalize-language)
- [Insertar la fecha 30 días a partir de ahora, formateada como mes y día](#countdown-template-date)

### Añadir x días a la fecha de hoy {#countdown-add-x-days}

Este caso de uso añade un número específico de días a la fecha actual para referenciar y añadir en mensajes. Por ejemplo, puedes querer enviar un mensaje a mitad de semana que muestre eventos en la zona para el fin de semana.

{% raw %}
```liquid
Here are the movies we're showing on {{ "now" | date:'%s' | plus:259200 | date:"%F" }}!
```
{% endraw %}

El valor de `plus` siempre estará en segundos, por lo que terminamos con el filtro `%F` para convertir los segundos a días.

{% alert important %}
Puede que quieras incluir una URL o vínculo profundo a una lista de eventos en tu mensaje para poder enviar al usuario a una lista de actividades que ocurrirán en el futuro.
{% endalert %}

### Calcular una cuenta regresiva desde un punto fijo en el tiempo {#countdown-difference-days}

Este caso de uso calcula la diferencia en días entre una fecha específica y la fecha actual. Esta diferencia se puede usar para mostrar una cuenta regresiva a tus usuarios.

{% raw %}
```liquid
{% assign event_date = '2023-12-31' | date: "%s" %}
{% assign today = 'now' | date: "%s" %}
{% assign difference = event_date | minus: today %}
{% assign difference_days = difference | divided_by: 86400 %}
you have {{ difference_days }} days left!
```
{% endraw %}

### Crear una cuenta regresiva para fechas y prioridades de envío específicas {#countdown-shipping-options}

Este caso de uso captura diferentes opciones de envío, calcula el tiempo que tardaría en recibirse y muestra mensajes animando a los usuarios a comprar a tiempo para recibir su paquete en una fecha determinada.

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

### Crear una cuenta regresiva en días {#countdown-days}

Este caso de uso calcula el tiempo restante entre un evento específico y la fecha actual y muestra cuántos días faltan para el evento.

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
Necesitarás un campo de atributo personalizado con un valor de tipo `date`.
{% endalert %}

### Crear una cuenta regresiva de días a horas a minutos {#countdown-dynamic}

Este caso de uso calcula el tiempo restante entre un evento específico y la fecha actual. Según el tiempo restante hasta el evento, cambiará el valor de tiempo (días, horas, minutos) para mostrar diferentes mensajes personalizados.

Por ejemplo, si faltan dos días para que llegue el pedido de un cliente, podrías decir: "Tu pedido llegará en 2 días". Mientras que si falta menos de un día, podrías cambiarlo a "Tu pedido llegará en 17 horas".

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
Necesitarás un campo de atributo personalizado con un valor de tipo `date`. También necesitarás establecer umbrales de tiempo para cuándo quieres que el tiempo se muestre en días, horas y minutos.
{% endalert %}

### Mostrar cuántos días faltan hasta una fecha determinada {#countdown-future-date}

Este caso de uso calcula la diferencia entre la fecha actual y una fecha de evento futura y muestra un mensaje indicando cuántos días faltan para el evento.

{% raw %}
```liquid
{% assign event_date = '2024-01-15' | date: "%s" %}
{% assign today = 'now' | date: "%s" %}
{% assign difference = event_date | minus: today %}
{% assign difference_days = difference | divided_by: 86400 %}
There are {{difference_days}} days until your birthday!
```
{% endraw %}

### Mostrar cuántos días faltan hasta que llegue un atributo de fecha personalizado {#countdown-custom-date-attribute}

Este caso de uso calcula la diferencia en días entre las fechas actual y futura y muestra un mensaje si la diferencia coincide con un número establecido.

En este ejemplo, un usuario recibirá un mensaje dentro de los dos días del atributo de fecha personalizado. De lo contrario, el mensaje no se enviará.

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

### Mostrar cuánto tiempo queda y cancelar el mensaje si solo queda x tiempo {#countdown-abort-window}

Este caso de uso calculará cuánto falta hasta una fecha determinada y, según la duración (omitiendo el mensaje si la fecha es demasiado próxima), mostrará diferentes mensajes personalizados.

Por ejemplo, "Te quedan x horas para comprar tu boleto a Londres", pero no enviar el mensaje si faltan menos de dos horas para la hora del vuelo a Londres.

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

{% alert important %} Necesitarás una propiedad de evento personalizado. {% endalert %}

### Mensaje dentro de la aplicación para enviar x días antes de que termine la membresía de los usuarios {#countdown-membership-expiry}

Este caso de uso captura la fecha de caducidad de la membresía, calcula cuánto falta para que expire y muestra diferentes mensajes según cuánto falta para que la membresía expire.

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

### Personalizar mensajes dentro de la aplicación según la fecha y el idioma de los usuarios {#countdown-personalize-language}

Este caso de uso calcula una cuenta regresiva hasta un evento y, según la configuración de idioma del usuario, mostrará la cuenta regresiva en su idioma.

Por ejemplo, podrías enviar una serie de mensajes de venta adicional a los usuarios una vez al mes para informarles cuánto tiempo sigue vigente una oferta con cuatro mensajes dentro de la aplicación:

- Inicial
- Quedan 2 días
- Queda 1 día
- Último día

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
Necesitarás asignar un valor de tipo `date` e incluir lógica de cancelación si la fecha dada cae fuera del rango de fechas. Para cálculos de días exactos, la fecha de finalización asignada debe incluir 23:59:59.
{% endalert %}

### Insertar la fecha 30 días a partir de ahora, formateada como mes y día {#countdown-template-date}

Este caso de uso mostrará la fecha 30 días a partir de ahora para usar en mensajería.

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

- [Personalizar un mensaje basado en atributos personalizados coincidentes](#attribute-matching)
- [Formatear moneda para convenciones numéricas europeas](#european-currency-format)
- [Restar dos atributos personalizados para mostrar la diferencia como valor monetario](#attribute-monetary-difference)
- [Hacer referencia al nombre de un usuario si su nombre completo está almacenado en el campo first_name](#attribute-first-name)

### Personalizar un mensaje basado en atributos personalizados coincidentes {#attribute-matching}

Este caso de uso verifica si un usuario tiene atributos personalizados específicos y, de ser así, mostrará diferentes mensajes personalizados.

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

### Formatear moneda para convenciones numéricas europeas {#european-currency-format}

Para las configuraciones regionales que usan una coma como separador decimal y un punto como separador de miles (por ejemplo, Alemania o Italia), usa los filtros [`money`]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/filters/#money-filter) y [`number_with_delimiter`]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters/#number-formatting-filters) con `replace` para intercambiar los separadores. Usa `#` como marcador de posición temporal para que los puntos y las comas no se intercambien en la misma pasada.

{% raw %}
```liquid
{{ 1234567.89 | money | number_with_delimiter | replace: '.', '#' | replace: ',', '.' | replace: '#', ',' }}
```

**Resultado:** `1.234.567,89`

**Explicación:** El filtro `money` añade decimales pero no añade un símbolo de moneda ni separadores específicos de la configuración regional. `number_with_delimiter` añade separadores de miles al estilo estadounidense, y los filtros `replace` los convierten al formato europeo.
{% endraw %}

### Restar dos atributos personalizados para mostrar la diferencia como valor monetario {#attribute-monetary-difference}

Este caso de uso captura dos atributos personalizados monetarios, luego calcula y muestra la diferencia para informar a los usuarios cuánto les falta para alcanzar su meta.

{% raw %}
```liquid
{% assign event_goal = {{custom_attribute.${last_selected_event_personal_goal}}} %}
{% assign current_raised =  {{custom_attribute.${last_selected_event_personal_amount_raised}}} %}
{% assign difference =  event_goal | minus: current_raised %}
You only have ${{ difference | round: 0 | number_with_delimiter }} left to raise!
```
{% endraw %}

### Hacer referencia al nombre de un usuario si su nombre completo está almacenado en el campo first_name {#attribute-first-name}

Este caso de uso captura el nombre de un usuario (si tanto el nombre como el apellido están almacenados en un solo campo) y luego usa este nombre para mostrar un mensaje de bienvenida.

{% raw %}
```liquid
{{${first_name} | truncatewords: 1, "" | default: 'hi'}}
{% assign name = {{${first_name}}} | split: ' ' %}
Hi {{name[0]}}, here's your message!
```

**Explicación:** El filtro `split` convierte la cadena contenida en `{{${first_name}}}` en un arreglo. Al usar `{{name[0]}}`, solo hacemos referencia al primer elemento del arreglo, que es el nombre del usuario.

{% endraw %}
{% endapi %}

{% api %}

## Evento personalizado {#custom-event}

{% apitags %}
Custom event
{% endapitags %}

- [Cancelar notificación push si un evento personalizado está dentro de dos horas a partir de ahora](#event-abort-push)
- [Enviar una Campaign cada vez que un usuario realiza un evento personalizado tres veces](#event-three-times)
- [Enviar un mensaje a usuarios que solo han comprado de una categoría](#event-purchased-one-category)
- [Rastrear cuántas veces ocurrió un evento personalizado en el último mes](#track)


### Cancelar notificación push si un evento personalizado está dentro de dos horas a partir de ahora {#event-abort-push}

Este caso de uso calcula el tiempo hasta un evento y, según la cantidad de tiempo restante, mostrará diferentes mensajes personalizados.

Por ejemplo, puedes querer evitar que se envíe una notificación push si una propiedad de evento personalizado pasará en las próximas dos horas. Este ejemplo usa el escenario de un carrito abandonado para un boleto de tren.

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

### Enviar una Campaign cada vez que un usuario realiza un evento personalizado tres veces {#event-three-times}

Este caso de uso verifica si un usuario ha realizado un evento personalizado tres veces y, de ser así, mostrará un mensaje o enviará una Campaign.

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

{% alert important %} Debes tener una propiedad de evento del conteo de eventos personalizados o usar un webhook a tu punto de conexión de Braze. Esto es para incrementar un atributo personalizado (`example_event_count`) cada vez que el usuario realiza el evento. Este ejemplo usa una cadencia de tres (1, 4, 7, 10, etc.). Para iniciar la cadencia desde cero (0, 3, 6, 9, etc.), elimina `minus: 1`.
{% endalert %}

### Enviar un mensaje a usuarios que solo han comprado de una categoría {#event-purchased-one-category}

Este caso de uso captura una lista de las categorías de las que un usuario ha comprado y, si solo existe una categoría de compra, mostrará un mensaje.

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

### Rastrear cuántas veces ocurrió un evento personalizado en el último mes {#track}

Este caso de uso calcula el número de veces que se ha registrado un evento personalizado entre el 1.º del mes actual y el mes anterior. Luego puedes ejecutar una llamada users/track para actualizar y almacenar este valor como un atributo personalizado. Ten en cuenta que esta Campaign necesitaría ejecutarse durante dos meses consecutivos antes de que los datos mensuales puedan usarse.

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

- [Mostrar nombres de meses en un idioma diferente](#language-display-month)
- [Mostrar una imagen según el idioma de un usuario](#language-image-display)
- [Personalizar mensajería según el día de la semana y el idioma del usuario](#language-personalize-message)

### Mostrar nombres de meses en un idioma diferente {#language-display-month}

Este caso de uso mostrará la fecha actual, el mes y el año, con el mes en un idioma diferente. El ejemplo proporcionado usa sueco.

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

### Mostrar una imagen según el idioma de un usuario {#language-image-display}

Este caso de uso mostrará una imagen según el idioma de un usuario. Ten en cuenta que este caso de uso solo se ha probado con imágenes cargadas en la biblioteca de medios de Braze.

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

### Personalizar mensajería según el día de la semana y el idioma del usuario {#language-personalize-message}

Este caso de uso verifica el día actual de la semana y, según el día, si el idioma del usuario está configurado en una de las opciones de idioma proporcionadas, mostrará un mensaje específico en su idioma.

El ejemplo proporcionado se detiene en martes, pero puede repetirse para cada día de la semana.

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

## Varios {#miscellaneous}

{% apitags %}
Miscellaneous
{% endapitags %}

- [Evitar enviar correos electrónicos a clientes que han bloqueado correos de marketing](#misc-avoid-blocked-emails)
- [Usar el estado de suscripción de un cliente para personalizar contenido en mensajes](#misc-personalize-content)
- [Poner en mayúscula la primera letra de cada palabra en una cadena](#misc-capitalize-words-string)
- [Comparar el valor de un atributo personalizado con un arreglo](#misc-compare-array)
- [Crear un recordatorio de evento próximo](#misc-event-reminder)
- [Encontrar una cadena dentro de un arreglo](#misc-string-in-array)
- [Encontrar el valor más grande en un arreglo](#misc-largest-value)
- [Encontrar el valor más pequeño en un arreglo](#misc-smallest-value)
- [Consultar el final de una cadena](#misc-query-end-of-string)
- [Consultar valores en un arreglo desde un atributo personalizado con múltiples combinaciones](#misc-query-array-values)
- [Formatear una cadena como número de teléfono](#phone-number)

### Evitar enviar correos electrónicos a clientes que han bloqueado correos de marketing {#misc-avoid-blocked-emails}

Este caso de uso toma una lista de usuarios bloqueados guardada en un Content Block y verifica que esos usuarios bloqueados no sean contactados ni segmentados en próximas Campaigns o Canvas.

{% alert important %}
Para usar este Liquid, primero guarda la lista de correos electrónicos bloqueados dentro de un Content Block. La lista no debe tener espacios adicionales ni caracteres insertados entre las direcciones de correo electrónico (por ejemplo, `test@braze.com,abc@braze.com`).
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

**Explicación:** Aquí verificamos si el correo electrónico de tu destinatario potencial está en esta lista haciendo referencia al Content Block de correos electrónicos bloqueados. Si se encuentra el correo electrónico, el mensaje no se enviará.

{% alert note %}
Los Content Blocks tienen un límite de tamaño de 5 MB.
{% endalert %}

### Usar el estado de suscripción de un cliente para personalizar contenido en mensajes {#misc-personalize-content}

Este caso de uso toma el estado de suscripción de un cliente para enviar contenido personalizado. Los clientes que están suscritos a un grupo de suscripción específico recibirán un mensaje exclusivo para grupos de suscripción de correo electrónico.

{% raw %}
```liquid
{% if {{subscribed_state.${subscription_group_id}}} == 'subscribed' %}
This is an exclusive message for subscribed users!
{% else %} This is the default message for other users.
{% endif %}
```
{% endraw %}

### Poner en mayúscula la primera letra de cada palabra en una cadena {#misc-capitalize-words-string}

Este caso de uso toma una cadena de palabras, las divide en un arreglo y pone en mayúscula la primera letra de cada palabra.

{% raw %}
```liquid
{% assign words_array = {{custom_attribute.${address}}} | split: ' ' %}
{% for words in {{words_array}} %}
{{ words | capitalize | append: ' ' }}
{% endfor %}
```
{% endraw %}

**Explicación:** Aquí hemos asignado una variable a nuestro atributo de cadena elegido y hemos usado el filtro `split` para dividir la cadena en un arreglo. Luego hemos usado la etiqueta `for` para asignar la variable `words` a cada uno de los elementos en nuestro arreglo recién creado, antes de mostrar esas palabras con el filtro `capitalize` y el filtro `append` para añadir espacios entre cada uno de los términos.

### Comparar el valor de un atributo personalizado con un arreglo {#misc-compare-array}

Este caso de uso toma una lista de tiendas favoritas, verifica si alguna de las tiendas favoritas de un usuario está en esa lista y, de ser así, mostrará una oferta especial de esas tiendas.

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

{% alert important %} Esta secuencia tiene una etiqueta `break` en la declaración condicional principal. Esto hace que el bucle se detenga cuando se encuentra una coincidencia. Si quieres mostrar muchas o todas las coincidencias, elimina la etiqueta `break`. {% endalert %}

### Crear un recordatorio de evento próximo {#misc-event-reminder}

Este caso de uso permite a los usuarios configurar recordatorios próximos basados en eventos personalizados. El escenario de ejemplo permite a un usuario establecer un recordatorio para una fecha de renovación de póliza que está a 26 o más días de distancia, donde los recordatorios se envían 26, 13, 7 o 2 días antes de la fecha de renovación de la póliza.

Con este caso de uso, lo siguiente debe ir en el cuerpo de una [Campaign de webhook]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook/) o paso en Canvas.

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

Necesitarás un evento personalizado `reminder_capture`, y las propiedades del evento personalizado deben incluir al menos:

- `reminder-id`: Identificador del evento personalizado
- `reminder_date`: Fecha enviada por el usuario en la que vence su recordatorio
- `message_personalisation_X`: Cualquier propiedad necesaria para personalizar el mensaje en el momento del envío

{% endalert %}

### Encontrar una cadena dentro de un arreglo {#misc-string-in-array}

Este caso de uso verifica si un arreglo de atributos personalizados contiene una cadena específica y, si existe, mostrará un mensaje específico.

{% raw %}
```liquid
{% if custom_attribute.${PartnershipProgramsNotLinked} contains 'Hertz' %}
Link your Hertz account to use Hertz Fast Lane.
{% endif %}
```
{% endraw %}

### Encontrar el valor más grande en un arreglo {#misc-largest-value}

Este caso de uso calcula el valor más alto en un arreglo de atributos personalizados dado para usar en la mensajería al usuario.

Por ejemplo, puedes querer mostrar a un usuario cuál es la puntuación más alta actual o la oferta más alta en un artículo.

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
Debes usar un atributo personalizado que tenga un valor entero y sea parte de un arreglo (lista). {% endalert %}

### Encontrar el valor más pequeño en un arreglo {#misc-smallest-value}

Este caso de uso calcula el valor más bajo en un arreglo de atributos personalizados dado para usar en la mensajería al usuario.

Por ejemplo, puedes querer mostrar a un usuario cuál es la puntuación más baja o el artículo más barato.

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

{% alert important %} Debes usar un atributo personalizado que tenga un valor entero y sea parte de un arreglo (lista). {% endalert %}

### Consultar el final de una cadena {#misc-query-end-of-string}

Este caso de uso consulta el final de una cadena para usar en mensajería.

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

### Consultar valores en un arreglo desde un atributo personalizado con múltiples combinaciones {#misc-query-array-values}

Este caso de uso toma una lista de programas que están por expirar, verifica si alguno de los programas favoritos de un usuario está en esa lista y, de ser así, mostrará un mensaje notificando al usuario que expirarán pronto.

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

{% alert important %} Primero necesitarás encontrar coincidencias entre los arreglos y luego construir la lógica al final para separar las coincidencias. {% endalert %}

### Formatear una cadena como número de teléfono {#phone-number}

Este caso de uso te muestra cómo indexar el campo de perfil de usuario `phone_number` (que por defecto está formateado como una cadena de enteros) y reformatearlo según tus estándares locales de número de teléfono. Por ejemplo, 1234567890 a (123)-456-7890.

{% raw %}
```liquid
{% assign phone = {{${phone_number}}} | remove: "-" | split: '' %}

({{ phone[0] }}{{ phone[1] }}{{ phone[2] }})-{{ phone[3] }}{{ phone[4] }}{{ phone[5] }}-{{ phone[6] }}{{ phone[7] }}{{ phone[8] }}{{ phone[9] }}
```
{% endraw %}

{% endapi %}

{% api %}

## Segmentación por plataforma {#platform-targeting}

{% apitags %}
Platform targeting
{% endapitags %}

- [Diferenciar el texto según el sistema operativo del dispositivo](#platform-device-os)
- [Segmentar solo una plataforma específica](#platform-target)
- [Segmentar solo dispositivos iOS con una versión específica del sistema operativo](#platform-target-ios-version)
- [Segmentar solo navegadores web](#platform-target-web)
- [Segmentar un operador móvil específico](#platform-target-carrier)

### Diferenciar el texto según el sistema operativo del dispositivo {#platform-device-os}

Este caso de uso verifica en qué plataforma está un usuario y, según su plataforma, mostrará mensajería específica.

Por ejemplo, puedes querer mostrar a los usuarios móviles versiones más cortas del texto del mensaje mientras muestras a otros usuarios la versión regular más larga del texto. También podrías mostrar a los usuarios móviles cierta mensajería relevante para ellos pero que no sería relevante para usuarios web. Por ejemplo, la mensajería de iOS podría hablar sobre Apple Pay, pero la mensajería de Android debería mencionar Google Pay.

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
Liquid distingue entre mayúsculas y minúsculas, `targeted_device.${platform}` devuelve el valor todo en minúsculas.
{% endalert %}

### Segmentar solo una plataforma específica {#platform-target}

Este caso de uso capturará la plataforma del dispositivo de los usuarios y, según la plataforma, mostrará un mensaje.

Por ejemplo, puedes querer enviar un mensaje solo a usuarios de Android. Esto se puede usar como alternativa a seleccionar una aplicación dentro de la herramienta de segmentación.

{% raw %}
```liquid
{% if {{targeted_device.${platform}}} == 'android' %}

This is a message for an Android user!

{% else %}
{% abort_message %}
{% endif %}
```
{% endraw %}

### Segmentar solo dispositivos con una versión específica del sistema operativo {#platform-target-ios-version}

Este caso de uso verifica si la versión del sistema operativo de un usuario está dentro de un conjunto determinado de versiones y, de ser así, mostrará un mensaje específico.

El ejemplo usado envía una advertencia a los usuarios con una versión del sistema operativo 10.0 o anterior de que se está dejando de dar soporte al sistema operativo de su dispositivo.

{% raw %}
```liquid
{% if {{targeted_device.${os}}} == "10.0" or {{targeted_device.${os}}} == "10.0.1" or {{targeted_device.${os}}} == "10.0.2" or {{targeted_device.${os}}} == "10.0.3" or {{targeted_device.${os}}} == "10.1" or {{targeted_device.${os}}} == "10.2" or {{targeted_device.${os}}} == "10.2.1" or {{targeted_device.${os}}} == "10.3" or {{targeted_device.${os}}} == "10.3.1" or {{targeted_device.${os}}} == "10.3.2" or {{targeted_device.${os}}} == "10.3.3" or {{targeted_device.${os}}} == "10.3.4" or {{targeted_device.${os}}} == "9.3.1" or {{targeted_device.${os}}} == "9.3.2" or {{targeted_device.${os}}} == "9.3.3" or {{targeted_device.${os}}} == "9.3.4" or {{targeted_device.${os}}} == "9.3.5" %}

We are phasing out support for your device's operating system. Be sure to update to the latest software for the best app experience.

{% else %}
{% abort_message %}
{% endif %}
```
{% endraw %}

### Segmentar solo navegadores web {#platform-target-web}

Este caso de uso verifica si el dispositivo objetivo de un usuario ejecuta Mac o Windows y, de ser así, mostrará un mensaje específico.

{% raw %}
```liquid
{% if {{targeted_device.${os}}} == 'Mac' or {{targeted_device.${os}}} == 'Windows' %}

This message will display on your desktop web browser.

{% else %}
{% abort_message %}
{% endif %}
```
{% endraw %}

El siguiente caso de uso verifica si un usuario web está en iOS o Android y, de ser así, mostrará un mensaje específico.

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

### Segmentar un operador móvil específico {#platform-target-carrier}

Este caso de uso verifica si el operador del dispositivo de un usuario es Verizon y, de ser así, mostrará un mensaje específico.

Para notificaciones push y canales de mensajes dentro de la aplicación, puedes especificar el operador del dispositivo en el cuerpo de tu mensaje usando Liquid. Si el operador del dispositivo del destinatario no coincide, el mensaje no se enviará.

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

- [Responder con diferentes mensajes según la palabra clave de SMS entrante](#sms-keyword-response)

### Responder con diferentes mensajes según la palabra clave de SMS entrante {#sms-keyword-response}

Este caso de uso incorpora procesamiento dinámico de palabras clave de SMS para responder a mensajes entrantes específicos con diferentes textos de mensaje. Por ejemplo, puedes enviar diferentes respuestas cuando alguien envía "START" versus "JOIN".

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

## Zonas horarias {#time-zones}

{% apitags %}
Time zones
{% endapitags %}

- [Insertar la zona horaria del usuario en una plantilla](#users-time-zone)
- [Personalizar un mensaje según la zona horaria de un usuario](#personalize-timezone)
- [Añadir la zona horaria CST a un atributo personalizado](#time-append-cst)
- [Insertar una marca de tiempo](#time-insert-timestamp)
- [Enviar una notificación push de Canvas solo durante una ventana de tiempo en la zona horaria local del usuario](#time-canvas-window)
- [Enviar una Campaign recurrente de mensajes dentro de la aplicación entre una ventana de tiempo en la zona horaria local del usuario](#time-reocurring-iam-window)
- [Enviar diferentes mensajes en días laborables versus fines de semana en la zona horaria local del usuario](#time-weekdays-vs-weekends)
- [Enviar diferentes mensajes según la hora del día en la zona horaria local del usuario](#time-of-day)
- [Cancelar un mensaje fuera de un rango de horas en el momento del envío](#abort-send-time-hour-range)
- [Cancelar un mensaje fuera de una ventana de tiempo en una zona horaria fija](#abort-fixed-timezone-window)

{% alert note %}
Si un usuario recibe un mensaje en una hora local inesperada, es posible que la zona horaria de su dispositivo o perfil haya cambiado (por ejemplo, después de viajar). La entrega en hora local usa la zona horaria del perfil en el momento del envío; los usuarios pueden necesitar una nueva sesión en su región habitual antes de que valores como {% raw %}`{{${time_zone}}}`{% endraw %} reflejen lo que esperas. Sin embargo, puedes [insertar la zona horaria del usuario en una plantilla](#users-time-zone).
{% endalert %}

### Insertar la zona horaria del usuario en una plantilla {#users-time-zone}

De forma predeterminada, las fechas y horas en Liquid se representan en Tiempo Universal Coordinado (UTC). Para mostrar fechas y horas en la zona horaria local del usuario, usa el filtro `time_zone` con el filtro `date`.

#### Asignar fecha y hora local {#assign-local-date-and-time}

Para asignar una variable que refleje la fecha y hora actuales en la zona horaria local del usuario, usa este formato:

{% raw %}
```liquid
{% assign local_date_time = 'now' | time_zone:{{${time_zone}}} | date: '%B %e, %Y' %}
{{local_date_time}}
```
{% endraw %}

- `now`: Recupera la fecha y hora actuales en UTC.
- `time_zone`: Recupera la zona horaria local del usuario desde el atributo predeterminado usando la etiqueta de personalización {% raw %}`{{${time_zone}}}`{% endraw %}.
- `date`: Formatea la fecha y hora local del usuario según tus especificaciones. En el ejemplo anterior, el sistema muestra una cadena formateada como "February 26, 2026". Para más opciones de formato, consulta [strftime.net](strftime.net).

#### Aplicar la zona horaria del usuario con atributos personalizados {#apply-the-users-time-zone-with-custom-attributes}

Puedes aplicar el filtro `time_zone` a atributos personalizados, así:

{% raw %}
```liquid
{{custom_attribute.${date_time_attribute} | time_zone: {{${time_zone}}} | date: '%a, %b %e, %Y'}}
```
{% endraw %}

Esto muestra el `date_time_attribute` formateado como el día de la semana abreviado, seguido del mes abreviado, el día y el año de cuatro dígitos.

### Personalizar un mensaje según la zona horaria de un usuario {#personalize-timezone}

Este caso de uso muestra diferentes mensajes según la zona horaria de un usuario.

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

### Añadir la zona horaria CST a un atributo personalizado {#time-append-cst}

Este caso de uso muestra un atributo de fecha personalizado en una zona horaria determinada.

Opción 1:
{% raw %}
```liquid
{{custom_attribute.${application_expires_date} | time_zone: -0005 | date: '%B, %d %Y' }}
```
{% endraw %}

Opción 2:
{% raw %}
```liquid
{{custom_attribute.${application_expires_date} | time_zone: 'America/Chicago' | date: '%B %d %Y %z' }}
```
{% endraw %}

### Insertar una marca de tiempo {#time-insert-timestamp}

Este caso de uso muestra un mensaje que incluye una marca de tiempo en la zona horaria actual del usuario.

El siguiente ejemplo mostrará la fecha como AAAA-mm-dd HH:MM:SS, como 2021-05-03 10:41:04.

{% raw %}
```liquid
{{${user_id} | default: 'You'}} received a campaign, rendered at ({{ "now" | time_zone: ${time_zone} | date: "%Y-%m-%d %H:%M:%S" }})
```
{% endraw %}

### Enviar una notificación push de Canvas solo durante una ventana de tiempo en la zona horaria local del usuario {#time-canvas-window}

Este caso de uso verifica la hora de un usuario en su zona horaria local y, si cae dentro de un tiempo establecido, mostrará un mensaje específico.

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

### Enviar una Campaign recurrente de mensajes dentro de la aplicación entre una ventana de tiempo en la zona horaria local del usuario {#time-reoccurring-iam-window}

Este caso de uso mostrará un mensaje si la hora actual del usuario cae dentro de una ventana establecida.

Por ejemplo, el siguiente escenario le informa a un usuario que una tienda está cerrada.

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

### Enviar diferentes mensajes en días laborables versus fines de semana en la zona horaria local del usuario {#time-weekdays-vs-weekends}

Este caso de uso verificará si el día actual de la semana del usuario es sábado o domingo y, según el día, mostrará diferentes mensajes.

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

### Enviar diferentes mensajes según la hora del día en la zona horaria local del usuario {#time-of-day}

Este caso de uso mostrará un mensaje si la hora actual del usuario cae fuera de una ventana establecida.

Por ejemplo, puedes querer informar a un usuario sobre una oportunidad sensible al tiempo que depende de la hora del día.

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

{% alert note %} Esto es lo opuesto a las [horas tranquilas]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/delivery_and_entry_types/#time-based-options). {% endalert %}

### Cancelar un mensaje fuera de un rango de horas en el momento del envío {#abort-send-time-hour-range}

Este caso de uso cancela el mensaje cuando la hora actual cae fuera de un rango definido. Usa la hora en la que se renderiza el mensaje, que es UTC por defecto a menos que apliques el filtro `time_zone`, no la zona horaria local del usuario. Para enviar mensajes basados en la zona horaria local de un usuario, consulta [Enviar diferentes mensajes según la hora del día en la zona horaria local del usuario](#time-of-day).

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

### Cancelar un mensaje fuera de una ventana de tiempo en una zona horaria fija {#abort-fixed-timezone-window}

Este caso de uso cancela el mensaje cuando la hora actual cae fuera de una ventana definida en una zona horaria específica (hora de Singapur en este ejemplo). Puedes usar este patrón cuando necesitas una regla inspirada en horas tranquilas que esté vinculada a una región en lugar del atributo `time_zone` de cada usuario.

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

## Semana/Día/Mes {#weekdaymonth}

{% apitags %}
Week/Day/Month
{% endapitags %}

- [Insertar el nombre del mes anterior en un mensaje](#month-name)
- [Enviar una Campaign al final de cada mes](#month-end)
- [Enviar una Campaign el último (día laborable) del mes](#day-of-month-last)
- [Enviar un mensaje diferente cada día del mes](#day-of-month)
- [Enviar un mensaje diferente cada día de la semana](#day-of-week)
- [Cancelar un mensaje en una fecha específica del calendario](#abort-specific-calendar-date)
- [Cancelar un mensaje en un día específico de la semana](#abort-specific-weekday)

### Insertar el nombre del mes anterior en un mensaje {#month-name}

Este caso de uso tomará el mes actual y mostrará el mes anterior para usar en mensajería.

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

Alternativamente, puedes usar lo siguiente para obtener el mismo resultado.

{% raw %}
```liquid
{% assign last_month_name = 'now' | date: "%Y-%m-01" | date: '%s' | minus: 1 | date: "%B" %}

Here's an overview of what your spending looked like in {{last_month_name}}.
```
{% endraw %}

### Enviar una Campaign al final de cada mes {#month-end}

Este caso de uso verificará si la fecha actual cae dentro de una lista de fechas y, según la fecha, mostrará un mensaje específico.

{% alert note %} Esto no tiene en cuenta los años bisiestos (29 de febrero). {% endalert %}

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

### Enviar una Campaign el último (día laborable) del mes {#day-of-month-last}

Este caso de uso captura el mes y día actuales y calcula si el día actual cae dentro del último día laborable del mes.

Por ejemplo, puedes querer enviar un cuestionario a tus usuarios el último miércoles del mes pidiendo comentarios sobre el producto.

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

### Enviar un mensaje diferente cada día del mes {#day-of-month}

Este caso de uso verifica si la fecha actual coincide con una en una lista y, según el día, mostrará un mensaje distinto.

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

### Enviar un mensaje diferente cada día de la semana {#day-of-week}

Este caso de uso verifica el día actual de la semana y, según el día, mostrará un mensaje distinto.

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
Puedes reemplazar la línea "Default copy" con {% raw %}`{% abort_message() %}`{% endraw %} para evitar que el mensaje se envíe si el día de la semana es desconocido.
{% endalert %}

### Cancelar un mensaje en una fecha específica del calendario {#abort-specific-calendar-date}

Este caso de uso cancela el mensaje en un mes y día elegidos cada año (5 de mayo en el ejemplo). Compara la fecha actual con una cadena inequívoca de mes-día construida con el filtro `date`.

{% raw %}
```liquid
{% assign date = 'now' | date: '%d/%m' %}
{% if date == '05/05' %}
{% abort_message('No message on the 5th of May') %}
{% endif %}
```
{% endraw %}

### Cancelar un mensaje en un día específico de la semana {#abort-specific-weekday}

Este caso de uso cancela el mensaje cuando Liquid se ejecuta en un día de la semana determinado (`Wednesday` en el ejemplo). El filtro `%A` devuelve el nombre completo del día de la semana en inglés.

{% raw %}
```liquid
{% assign weekday = 'now' | date: '%A' %}
{% if weekday == 'Wednesday' %}
{% abort_message("No message on Wednesdays") %}
{% endif %}
```
{% endraw %}

{% endapi %}

Muchos ejemplos en esta biblioteca usan la etiqueta `abort_message` para omitir un envío cuando no se cumplen las condiciones. Para una referencia completa sobre cómo cancelar envíos con Liquid, incluidos patrones basados en fecha y hora, consulta [Cancelar mensajes Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages/).