---
nav_title: Establecer valores predeterminados
article_title: Establecer valores predeterminados de Liquid
page_order: 5
description: "Este artículo de referencia explica cómo establecer valores alternativos predeterminados para cualquier atributo de personalización que uses en tus mensajes."

---

# Establecer valores predeterminados

{% raw %}

> Se pueden establecer valores alternativos predeterminados para cualquier atributo de personalización que uses en tus mensajes. Este artículo explica cómo funcionan los valores predeterminados, cómo configurarlos y cómo usarlos en tus mensajes.

## Cómo funcionan

Los valores predeterminados se pueden añadir especificando un [filtro Liquid](http://docs.shopify.com/themes/liquid-documentation/filters) (usa `|` para distinguir el filtro en línea, como se muestra) con el nombre "default."

```
| default: 'Insert Your Desired Default Here'
```

Si no se proporciona un valor predeterminado y el campo no existe o no está configurado en el usuario, el campo aparecerá en blanco en el mensaje.

El siguiente ejemplo muestra la sintaxis correcta para añadir un valor predeterminado. En este caso, las palabras "Valued User" reemplazarán el atributo `{{ ${first_name} }}` si el campo `first_name` del usuario está vacío o no está disponible.

```liquid
Hi {{ ${first_name} | default: 'Valued User' }}, thanks for using the App!
```

Para una usuaria llamada Janet Doe, el mensaje aparecería como:

```
Hi Janet, thanks for using the App!
```

O...

```
Hi Valued User, thanks for using the App!
```
{% endraw %}

{% alert important %}
El valor predeterminado se mostrará para valores vacíos (empty), pero no para valores en blanco (blank). Un valor vacío no contiene nada, mientras que un valor en blanco contiene caracteres de espacio en blanco (como espacios) y ningún otro carácter. Por ejemplo, una cadena vacía podría verse como `""` y una cadena en blanco podría verse como `" "`.
{% endalert %}

## Establecer valores predeterminados para diferentes tipos de datos

El ejemplo anterior muestra cómo establecer un valor predeterminado para una cadena. Puedes establecer valores predeterminados para cualquier tipo de datos Liquid que tenga el valor `empty`, `nil` (indefinido) o `false`, lo que incluye cadenas, booleanos, arrays, objetos y números.

### Caso de uso: booleanos

Supongamos que tienes un atributo personalizado booleano llamado `premium_user` y quieres enviar un mensaje personalizado basado en el estado premium del usuario. Algunos usuarios no tienen un estado premium configurado, por lo que necesitarás establecer un valor predeterminado para contemplar a esos usuarios.

1. Asignarás una variable llamada `is_premium_user` al atributo `premium_user` con un valor predeterminado de `false`. Esto significa que si `premium_user` es `nil`, el valor de `is_premium_user` será `false` de forma predeterminada.

{% raw %}
```liquid
{% assign is_premium_user = {{custom_attribute.${premium_user}}} | default: false %}
```

{: start="2"}
2. Luego, usa lógica condicional para especificar el mensaje a enviar si `is_premium_user` es `true`. En otras palabras, qué enviar si `premium_user` es `true`. También asignarás un valor predeterminado al nombre del usuario, en caso de que no tengamos su nombre.

```liquid
{% if is_premium_user %}
Hi {{${first_name} | default: 'premium user'}}, thank you for being a premium user!
```

{: start="3"}
3. Finalmente, especifica qué mensaje enviar si `is_premium_user` es `false` (lo que significa que `premium_user` es `false` o `nil`). Luego cerrarás la lógica condicional.

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

### Caso de uso: números

Supongamos que tienes un atributo personalizado numérico llamado `reward_points` y quieres enviar un mensaje con los puntos de recompensa del usuario. Algunos usuarios no tienen puntos de recompensa configurados, por lo que necesitarás establecer un valor predeterminado para contemplar a esos usuarios.

1. Comienza el mensaje dirigiéndote al nombre del usuario o con un valor predeterminado de `Valued User`, en caso de que no tengas su nombre.

{% raw %}
```liquid
Hi {{${first_name} | default: 'valued user'}},
```
{% endraw %}

{: start="2"}
2. Termina el mensaje con la cantidad de puntos de recompensa que tiene el usuario usando el atributo personalizado llamado `reward_points` y el valor predeterminado de `0`. Todos los usuarios cuyo `reward_points` tenga un valor `nil` tendrán `0` puntos de recompensa en el mensaje.

{% raw %}
```liquid
Hi {{${first_name} | default: 'valued user'}}, you have {{custom_attribute.${reward_points} | default: 0}} reward points.
```
{% endraw %}

### Caso de uso: objetos

Supongamos que tienes un objeto de atributo personalizado anidado llamado `location` que contiene las propiedades `city` y `state`. Si alguna de estas propiedades no está configurada, quieres animar al usuario a proporcionarlas.

1. Dirígete al usuario por su nombre e incluye un valor predeterminado, en caso de que no tengas su nombre.

{% raw %}
```liquid
Hi {{${first_name} | default: 'valued user'}},
```
{% endraw %}

{: start="2"}
2. Escribe un mensaje que diga que te gustaría confirmar la ubicación del usuario.

{% raw %}
```liquid
We'd like to confirm the location associated with your account. We use this location to send you promotions and offers for stores nearest you. You can update your location in your profile settings.
```
{% endraw %}

{: start="3"}
3. Inserta la ubicación del usuario en el mensaje y asigna valores predeterminados para cuando la propiedad de dirección no esté configurada.

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

### Caso de uso: arrays

Supongamos que tienes un atributo personalizado de tipo array llamado `upcoming_trips` que contiene viajes con las propiedades `destination` y `departure_date`. Quieres enviar a los usuarios mensajes personalizados según si tienen viajes programados.

1. Escribe lógica condicional para especificar que no se debe enviar un mensaje si `upcoming_trips` está `empty`.

{% raw %}
```liquid
{% if {{custom_attribute.${upcoming_trips}}} == empty %}
{% abort_message('No upcoming trips scheduled') %}
```
{% endraw %}

{: start="2"}
2. Especifica qué mensaje enviar si `upcoming_trips` tiene contenido:<br><br>**2a.** Dirígete al usuario e incluye un valor predeterminado, en caso de que no tengas su nombre. <br>**2b.** Usa una etiqueta `for` para especificar que extraerás propiedades (o información) de cada viaje contenido en `upcoming_trips`. <br>**2c.** Enumera las propiedades en el mensaje e incluye un valor predeterminado para cuando `departure_date` no esté configurado. (Supongamos que `destination` es obligatorio para crear un viaje, por lo que no necesitas establecer un valor predeterminado para eso.)<br>**2d.** Cierra la etiqueta `for` y luego cierra la lógica condicional.

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