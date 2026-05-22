---
nav_title: Tutoriales
article_title: "Tutoriales: Escribir código Liquid"
page_order: 11
description: "Esta página de referencia contiene tutoriales para principiantes que te ayudarán a empezar con el código Liquid."
page_type: tutorial
---

# Tutoriales: Escribir código Liquid {#tutorials-writing-liquid-code}

> ¿Eres nuevo en Liquid? Estos tutoriales te ayudarán a empezar a escribir código Liquid para casos de uso aptos para principiantes. Cada tutorial cubre una combinación diferente de objetivos de aprendizaje, como lógica condicional y operadores.

Cuando termines estos tutoriales, serás capaz de:

- Escribir código Liquid para casos de uso comunes
- Encadenar lógica condicional de Liquid para personalizar mensajes basándote en datos de usuario
- Usar variables y filtros para escribir ecuaciones que utilicen los valores de los atributos
- Reconocer comandos básicos en código Liquid y formarte una idea general de lo que hace el código

| Tutorial | Objetivos de aprendizaje |
| --- | --- |
| [Personalizar mensajes para segmentos de usuarios](#segments) | valores predeterminados, lógica condicional |
| [Recordatorios de carrito abandonado](#reminders) | operadores, lógica condicional |
| [Cuenta regresiva de evento](#countdown) | variables, filtros de fecha |
| [Mensaje mensual de cumpleaños](#birthday) | variables, filtros de fecha, operadores |
| [Promocionar un producto favorito](#favorite-product) | variables, filtros de fecha, ecuaciones, operadores |
{: .reset-br-td-1 .reset-br-td-2 aria-label="Tutoriales: Escribir código Liquid" }

## Mensajes personalizados para segmentos de usuarios {#segments}

Vamos a personalizar mensajes para diferentes segmentos de usuarios, como clientes VIP y nuevos suscriptores.

1. Abre el mensaje con saludos personalizados para enviar cuando tienes y no tienes el nombre del usuario. Para ello, crea una etiqueta de Liquid que incluya el atributo `first_name` y un valor predeterminado a usar si `first_name` está vacío. En este escenario, usemos "traveler" como valor predeterminado.

{% raw %}
```liquid
Happy summer, {{${first_name} | default: "traveler"}}!
```
{% endraw %}

{: start="2"}
2. Ahora, proporcionemos el mensaje a enviar si el usuario es un cliente VIP. Necesitaremos usar una etiqueta de lógica condicional para esto: `if`. Esta etiqueta indicará que si el atributo personalizado `vip_status` es igual a `VIP`, se ejecutará el siguiente Liquid. En este caso, se enviará un mensaje específico.

{% raw %}
```liquid
{% if {{custom_attribute.${vip_status}}} == 'VIP' %}
Thank you for being a VIP customer! Enjoy your exclusive discount code: VIPSUMMR464.
```
{% endraw %}

{: start="3"}
3. Enviemos un mensaje personalizado para los usuarios que son nuevos suscriptores. Usaremos la etiqueta de lógica condicional `elsif` para especificar que si el `vip_status` del usuario es `new`, se enviará el siguiente mensaje.

{% raw %}
```liquid
{% elsif {{custom_attribute.${vip_status}}} == 'new' %}
Thank you for subscribing! Enjoy your welcome discount code: NEWTRAVEL257.
```
{% endraw %}

{: start="4"}
4. ¿Qué pasa con los usuarios que no son VIP ni nuevos? Podemos enviar un mensaje a todos los demás usuarios con la etiqueta `else`, que especifica que el siguiente mensaje debe enviarse si las condiciones anteriores no se cumplen. Luego podemos cerrar la lógica condicional con la etiqueta `endif`, ya que no hay más estados VIP que considerar.

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

## Recordatorios de carrito abandonado {#reminders}

Enviemos mensajes personalizados para recordar a los usuarios los artículos que dejaron en su carrito. Los personalizaremos aún más según cuántos artículos haya en su carrito: si tienen tres artículos o menos, listaremos todos los artículos. Si hay más de tres artículos, enviaremos un mensaje más conciso.

1. Comprobemos si el carrito del usuario está vacío abriendo una lógica condicional de Liquid con el operador `!=`, que significa "no es igual a". En este caso, estableceremos la condición de que el atributo personalizado `cart_items` no sea igual a un valor vacío.

{% raw %}
```liquid
{% if {{custom_attribute.${cart_items}}} != blank %}
```
{% endraw %}

{: start="2"}
2. Luego necesitaremos acotar nuestro enfoque y comprobar si el carrito tiene más de tres artículos usando el operador `>`, que significa "mayor que".

{% raw %}
```liquid
{% if {{custom_attribute.${cart_items}}} | size > 3 %}
```
{% endraw %}

{: start="3"}
3. Escribe un mensaje que salude al usuario por su nombre, o si no está disponible, usa "there" como valor predeterminado. Incluye lo que debe indicarse si hay más de tres artículos en el carrito. Como no queremos abrumar al usuario con una lista completa, listemos los tres primeros `cart_items`.

{% raw %}
```liquid
Hi {{${first_name} | default: 'there'}}, don't forget to complete your purchase! Your items {{custom_attribute.${cart_items[0]}}}, {{custom_attribute.${cart_items[1]}}}, {{custom_attribute.${cart_items[2]}}}, and others are waiting for you.
```
{% endraw %}

{: start="4"}
4. Usa la etiqueta `else` para especificar qué debe ocurrir si las condiciones anteriores no se cumplen (es decir, si `cart_items` está vacío o tiene menos de tres artículos), y luego proporciona el mensaje a enviar. Como tres artículos no ocupan mucho espacio, podemos listarlos todos. Usaremos el operador de Liquid `join` y `,` para especificar que los artículos deben listarse separados por una coma. Cierra la lógica con `endif`.

{% raw %}
```liquid
{% else %}
Hi {{${first_name} | default: 'there'}}, don't forget to complete your purchase! Your items: {{{custom_attribute.${cart_items}}} | join: ', '}  are waiting for you.
{% endif %}
```
{% endraw %}

{: start="5"}
5. Usa `else` y luego un `abort_message` para indicar al código Liquid que no envíe un mensaje si el carrito no cumple ninguna de las condiciones anteriores. Es decir, si el carrito está vacío. Cierra la lógica con `endif`.

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

## Cuenta regresiva de evento {#countdown}

Enviemos a los usuarios un mensaje que indique cuántos días faltan para una venta de aniversario. Para ello, usaremos variables para poder crear ecuaciones que manipulen los valores de los atributos.

1. Primero, asignemos la variable `sale_date` al atributo personalizado `anniversary_date` y apliquemos el filtro `date: "s"`. Esto convierte `anniversary_date` a un formato de marca de tiempo expresado en segundos y luego asigna ese valor a `sale_date`.

{% raw %}
```liquid
{% assign sale_date = {{custom_attribute.${anniversary_date}}} | date: "%s" %}
```
{% endraw %}

{: start="2"}
2. También necesitamos asignar una variable para capturar la marca de tiempo de hoy. Asignemos la variable `today` a `now` (la fecha y hora actuales) y luego apliquemos el filtro `date: "%s"`.

{% raw %}
```liquid
{% assign today =  'now' | date: "%s"  %}
```
{% endraw %}

{: start="3"}
3. Ahora calculemos cuántos segundos hay entre ahora (`today`) y la venta de aniversario (`sale_date`). Para ello, asigna la variable `difference` al valor de `sale_date` menos `today`.

{% raw %}
```liquid
{% assign difference =  event_date | minus: today %}
```
{% endraw %}

{: start="4"}
4. Ahora necesitamos convertir `difference` a un valor que podamos referenciar en un mensaje, ya que no es ideal decirle al usuario cuántos segundos faltan para una venta. Asignemos `difference_days` a `event_date` y dividámoslo entre `86400` para obtener el número de días.

{% raw %}
```liquid
{% assign difference_days = difference | divided_by: 86400 %}
```
{% endraw %}

{: start="5"}
5. Finalmente, creemos el mensaje a enviar.

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

## Mensaje mensual de cumpleaños {#birthday}

Enviemos una promoción especial a todos los usuarios cuyo cumpleaños caiga en el mes actual. Los usuarios que no cumplan años este mes no recibirán ningún mensaje.

1. Primero, obtengamos el mes actual. Asignaremos la variable `this_month` a `now` (la fecha y hora actuales) y luego usaremos el filtro `date: "%B"` para especificar que la variable debe ser igual al mes.

{% raw %}
```liquid
{% assign this_month = 'now' | date: "%B" %}
```
{% endraw %}

{: start="2"}
2. Ahora, obtengamos el mes de nacimiento del `date_of_birth` del usuario. Asignaremos la variable `birth_month` a `date_of_birth` y luego usaremos el filtro `date: "%B"`.

{% raw %}
```liquid
{% assign birth_month = {{${date_of_birth}}} | date: "%B" %}
```
{% endraw %}

{: start="3"}
3. Ahora que tenemos dos variables con un mes como valor, podemos compararlas con lógica condicional. Establezcamos la condición de que `this_month` sea igual al `birth_month` del usuario.

{% raw %}
```liquid
{% if {{this_month}} == {{birth_month}} %}
```
{% endraw %}

{: start="4"}
4. Creemos el mensaje a enviar si este mes es también el mes de nacimiento del usuario.

{% raw %}
```liquid
We heard {{this_month}} is a special month! Enjoy a 50% discount on your purchase with code BIRTHDAY50 until the end of {{this_month}}.
```
{% endraw %}

{: start="5"}
5. Usa la etiqueta `else` para especificar qué ocurre si la condición no se cumple (porque este mes no es el mes de nacimiento del usuario).

{% raw %}
```liquid
{% else %}
```
{% endraw %}

{: start="6"}
6. No queremos enviar un mensaje si el mes de nacimiento del usuario no es este mes, así que usaremos `abort_message` para cancelar el mensaje y luego cerraremos la lógica condicional con `endif`.

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

## Promoción de producto favorito {#favorite-product}

Promocionemos el producto favorito de un usuario si su última fecha de compra fue hace más de seis meses.

1. Primero, usaremos lógica condicional para comprobar si tenemos el producto favorito del usuario y la fecha de última compra.

{% raw %}
```liquid
{% if {{custom_attribute.${favorite_product}}} == blank or {{custom_attribute.${last_purchase_date}}} == blank %}
```
{% endraw %}

{: start="2"}
2. Luego indicaremos que si no tenemos el producto favorito del usuario o la fecha de última compra, no se envíe un mensaje.

{% raw %}
```liquid
{% abort_message("No favorite product or last purchase date") %}
```
{% endraw %}

{: start="3"}
3. Usaremos `else` para especificar qué debe ocurrir si la condición anterior no se cumple (porque _sí_ tenemos el producto favorito del usuario y la fecha de última compra).

{% raw %}
```liquid
{% else %}
```
{% endraw %}

{: start="4"}
4. Si tenemos la fecha de compra, necesitamos asignarla a una variable para poder compararla con la fecha de hoy. Primero, creemos un valor para la fecha de hoy asignando la variable `today` a `now` (la fecha y hora actuales) y usando el filtro `date: "%s"` para convertir el valor a un formato de marca de tiempo expresado en segundos. Añadiremos el filtro `plus: 0` para agregar un "0" a la marca de tiempo. Esto no cambia el valor de la marca de tiempo, pero es útil para usar la marca de tiempo en ecuaciones futuras.


{% raw %}
```liquid
{% assign today = 'now' | date: "%s" | plus: 0 %}
```
{% endraw %}

{: start="5"}
5. Ahora capturemos la fecha de última compra en segundos asignando la variable `last_purchase_date` al atributo personalizado `last_purchase_date` y usando el filtro `date: "s"`. Nuevamente añadiremos el filtro `plus: 0`.

{% raw %}
```liquid
{% assign last_purchase_date = {{custom_attribute.${last_purchase_date}}} | date: "%s" | plus: 0 %}
```
{% endraw %}

{: start="6"}
6. Como la fecha de última compra y la fecha de hoy están en segundos, necesitaremos calcular cuántos segundos hay en seis meses. Hagamos una ecuación (aproximadamente 6 meses * 30,44 días * 24 horas * 60 minutos * 60 segundos) y asignémosla a la variable `six_months`. Usaremos `times` para especificar la multiplicación de las unidades de tiempo.

{% raw %}
```liquid
{% assign six_months = 6 | times: 30.44 | times: 24 | times: 60 | times: 60 %}
```
{% endraw %}

{: start="7"}
7. Ahora que todos nuestros valores de tiempo están en segundos, podemos usar sus valores en ecuaciones. Asignemos una variable llamada `today_minus_last_purchase_date` que tome el valor de hoy y le reste `last_purchase_date`. Esto nos da cuántos segundos han pasado desde la última compra.

{% raw %}
```liquid
{% assign today_minus_last_purchase_date = {{today | minus: last_purchase_date}} %}
```
{% endraw %}

{: start="8"}
8. Ahora comparemos directamente nuestros valores de tiempo en lógica condicional. Definamos la condición como que `today_minus_last_purchase_date` sea mayor o igual (`>=`) a seis meses. En otras palabras, la última compra fue hace al menos seis meses.

{% raw %}
```liquid
{% if today_minus_last_purchase_date >= six_months %}
```
{% endraw %}

{: start="9"}
9. Creemos el mensaje a enviar si la última compra fue hace al menos seis meses.

{% raw %}
```liquid
We noticed it’s been a while since you last purchased {{custom_attribute.${favorite_product}}}. Have you checked out our latest offerings?
```
{% endraw %}

{: start="10"}
10. Usaremos la etiqueta `else` para especificar qué debe ocurrir si la condición no se cumple (porque la compra no fue hace al menos seis meses).

{% raw %}
```liquid
{% else %}
```
{% endraw %}

{: start="11"}
11. Incluiremos un `abort_message` para cancelar el mensaje.

{% raw %}
```liquid
{% abort_message("No favorite product or last purchase date") %}
```
{% endraw %}

{: start="12"}
12. Para terminar, cerraremos el Liquid con dos etiquetas `endif`. La primera `endif` cierra la comprobación condicional del producto favorito o la fecha de última compra, y la segunda `endif` cierra la comprobación condicional de que la fecha de última compra sea de al menos seis meses.

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