---
nav_title: Lógica condicional de mensajería
article_title: Lógica condicional de mensajería con Liquid
page_order: 6
description: "Este artículo de referencia cubre cómo las etiquetas pueden y deben usarse en tus campañas."

---

# Lógica condicional de mensajería {#conditional-messaging-logic}

> Las [etiquetas](https://docs.shopify.com/themes/liquid-documentation/tags) te permiten incluir lógica de programación en tus campañas de mensajería. Las etiquetas pueden usarse para ejecutar sentencias condicionales, así como para casos de uso avanzados, como asignar variables o iterar a través de un bloque de código. <br><br>Esta página cubre cómo las etiquetas pueden y deben usarse, como por ejemplo cómo manejar valores de atributo nulos, nil y en blanco, y cómo hacer referencia a atributos personalizados.

## Formato de etiquetas {#formatting-tags}

{% raw %}
Una etiqueta debe estar envuelta en `{% %}`.
{% endraw %}

Para facilitarte un poco las cosas, Braze ha incluido un formato de color que se activará en verde y morado si has formateado correctamente tu sintaxis Liquid. El formato verde puede ayudar a identificar etiquetas, mientras que el formato morado resalta las áreas que contienen personalización.

Si tienes dificultades para usar la mensajería condicional, intenta escribir la sintaxis condicional antes de insertar tus atributos personalizados y otros elementos Liquid.

Por ejemplo, añade lo siguiente en el campo de mensaje primero:
{% raw %}
```liquid
{% if X >0 %}
{% else %}
{% endif %}
```

Asegúrate de que se resalte en verde, luego reemplaza la `X` con tu Liquid o contenido conectado elegido usando el `+` azul en la esquina del campo de mensaje, y el `0` con el valor deseado.
<br><br>
Después, añade las variaciones de tu mensaje según las necesites entre los condicionales `else`:
```liquid
{% if {{custom_attribute.${total_spend}}} >0 %}
Thanks for purchasing! Here's another 10% off!
{% else %}
Buy now! Would 5% off convince you?
{% endif %}
```
{% endraw %}

## Lógica condicional {#conditional-logic}

Puedes incluir muchos tipos de [lógica inteligente dentro de los mensajes](http://docs.shopify.com/themes/liquid-documentation/basics), como una sentencia condicional. El siguiente ejemplo usa [condicionales](http://docs.shopify.com/themes/liquid-documentation/tags/control-flow-tags) para internacionalizar una campaña:
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

### Etiquetas condicionales {#conditional-tags}

#### `if` y `elsif` {#if-and-elsif}

La lógica condicional comienza con la etiqueta `if`, que establece la primera condición a verificar. Las condiciones posteriores usan la etiqueta `elsif` y se verificarán si las condiciones anteriores no se cumplen. En este ejemplo, si el dispositivo de un usuario no está configurado en inglés, este código verificará si el dispositivo del usuario está configurado en español, y si eso falla, verificará si el dispositivo está configurado en chino. Si el dispositivo del usuario cumple una de estas condiciones, el usuario recibirá un mensaje en el idioma correspondiente.

#### `else`

Tienes la opción de incluir una sentencia `{% else %}` en tu lógica condicional. Si ninguna de las condiciones que estableciste se cumple, la sentencia `{% else %}` especifica el mensaje que debe enviarse. En este ejemplo, el idioma predeterminado es el inglés si el idioma del usuario no es inglés, español o chino.

#### `case` y `when` {#case-and-when}

`{% case %}`, `{% when %}` y `{% endcase %}` funcionan como una sentencia switch: estableces una expresión después de `case`, y cada rama `when` se ejecuta cuando esa expresión es igual al valor indicado (Liquid usa igualdad internamente, similar a encadenar `if` y `elsif` con `==`). Puedes listar múltiples valores en una etiqueta `when` separándolos con una coma u `or`. Usa `{% else %}` como alternativa cuando nada coincida, y luego cierra con `{% endcase %}`.

Asegúrate de que el formato de tus valores `when` coincida con el tipo de datos. Para texto (como un código de idioma), usa comillas: `{% when 'es' %}`. Para números, omite las comillas: `{% when 2 %}`.

```liquid
{% assign handle = 'cake' %}
{% case handle %}
{% when 'cake' %}
This is a cake
{% when 'cookie' %}
This is a cookie
{% else %}
This is not a cake nor a cookie
{% endcase %}
```

Puedes usar el mismo patrón con etiquetas de personalización de Braze u otras expresiones Liquid en lugar de `handle`. Para más opciones de sintaxis, consulta la [documentación de la etiqueta `case`](https://shopify.dev/docs/api/liquid/tags/case) de Shopify.

#### `endif`

La etiqueta `{% endif %}` señala que has terminado un bloque `if`. Debes incluir la etiqueta `{% endif %}` en cualquier mensaje que use `if`, `elsif`, `unless` o `else` en esa cadena. Si no incluyes una etiqueta `{% endif %}`, obtendrás un error ya que Braze no podrá analizar tu mensaje. Si usas `{% case %}` en su lugar, cierra el bloque con `{% endcase %}`, no con `{% endif %}`.

{% alert note %}
En las etiquetas `if`, `elsif` y `unless`, puedes usar operadores pero no filtros. En las etiquetas `case` y `when`, cada rama coincide cuando la expresión `case` es igual a un valor `when`; los filtros tampoco son compatibles en esas expresiones. Para evaluar un valor filtrado, asigna primero el resultado del filtro a una variable y luego haz referencia a esa variable en tu cláusula `case` o `when`. Para más detalles, consulta [Dónde usar operadores y filtros]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid#where-to-use-operators-and-filters).
{% endalert %}

### Tutorial: Entregar contenido basado en la ubicación {#tutorial-deliver-location-based-content}

Cuando termines este tutorial, podrás usar etiquetas con sentencias "if", "elsif" y "else" para entregar contenido basado en la ubicación de un usuario.

1. Comienza con una etiqueta `if` para establecer qué mensaje debe enviarse cuando la ciudad del usuario sea Nueva York. Si la ciudad del usuario es Nueva York, se cumple esta primera condición y el usuario recibirá un mensaje que especifica su identidad neoyorquina.

```liquid
{% if ${city} == "New York" %}
  🎉 Hey there, New Yorker! We're excited to offer you a special deal!
  Get 20% off your next sandwich at your local Sandwich Emperor.
  Just show this message at the counter to redeem your offer!
```

{: start="2"}
2. A continuación, usa la etiqueta `elseif` para establecer qué mensaje debe enviarse si la ciudad del usuario es Los Ángeles.

```liquid
{% elsif ${city} == "Los Angeles" %}
  🌞 Hello, Los Angeles! Enjoy a sunny day with a delicious sandwich!
  Present this message at our LA restaurant for a 20% discount on your next order!
```

{: start="3"}
3. Usemos otra etiqueta `elseif` para establecer qué mensaje debe enviarse si la ciudad del usuario es Chicago.

```liquid
{% elsif ${city} == "Chicago" %}
  🍕 Chicago, we have a treat for you!
  Swing by our restaurant and get 20% off your favorite sandwich.
  Just show this message to our staff!
```

{: start="4"}
4. Ahora, usemos la etiqueta `{% else %}` para especificar qué mensaje debe enviarse si la ciudad del usuario no es San Francisco, Nueva York ni Chicago.

```liquid
{% else %}
 🥪 Craving a sandwich? Visit us at any of our locations for a delicious meal!
  Check our website for the nearest restaurant to you!
```

{: start="5"}
5. Finalmente, usaremos la etiqueta `{% endif %}` para especificar que nuestra lógica condicional ha terminado.

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

## Manejo de valores de atributo nulos, nil y en blanco {#accounting-for-null-nil-and-blank-attribute-values}

La lógica condicional es una forma útil de manejar valores de atributo que no están configurados en los perfiles de usuario.

### Valores de atributo nulos y nil {#null-and-nil-attribute-values}

Un valor nulo o nil ocurre cuando el valor de un atributo personalizado no se ha configurado. Por ejemplo, un usuario que aún no ha establecido su nombre no tendrá un nombre registrado en Braze.

En algunas circunstancias, es posible que desees enviar un mensaje completamente diferente a los usuarios que tienen un nombre configurado y a los usuarios que no lo tienen.

La siguiente etiqueta te permite especificar un mensaje para usuarios con un atributo "nombre" nulo:

{% raw %}
```liquid
{% if ${first_name} == null %}
  ....
{% endif %}
```
{% endraw %}

![Un ejemplo de mensaje en el panel de Braze, usando un atributo de nombre nulo.]({% image_buster /assets/img/value_null.png %}){: style="max-width:60%;"}

{% raw %}
```liquid
{% if ${first_name} == null %}
We're having a sale! Hurry up and get 10% off all items today only!
{% else %}
Hey {{${first_name} | default: 'there'}}, we're having a sale! Hurry up and get 10% off all items today only!
{% endif %}
```

Ten en cuenta que un valor de atributo nulo no está estrictamente asociado con un tipo de valor (por ejemplo, una cadena "nula" es lo mismo que un arreglo "nulo"), por lo que en el ejemplo anterior, el valor de atributo nulo hace referencia a un nombre no configurado, que sería una cadena.

{% endraw %}

### Valores de atributo en blanco {#blank-attribute-values}

Un valor en blanco ocurre cuando el atributo en un perfil de usuario no está configurado, está configurado con una cadena de espacios en blanco (` `), o está configurado como `false`. Los valores en blanco deben verificarse antes que otras variables para evitar un error de procesamiento de Liquid.

La siguiente etiqueta te permite especificar un mensaje para usuarios que tienen un atributo "nombre" en blanco.

{% raw %}
```liquid
{% if ${first_name} == blank %}
  ....
{% endif %}
```
{% endraw %}

## Referencia a atributos personalizados {#referencing-custom-attributes}

Después de haber [creado atributos personalizados]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes#managing-custom-attributes), puedes hacer referencia a estos atributos personalizados en tu mensajería Liquid.

Al usar lógica condicional, necesitarás conocer el tipo de datos del atributo personalizado para asegurarte de que estás usando la sintaxis correcta. Desde la página **Atributos personalizados** en el panel, busca el tipo de datos asociado con tu atributo personalizado y luego consulta los siguientes ejemplos listados para cada tipo de datos.

![Selección de un tipo de datos para un atributo personalizado. El ejemplo proporcionado muestra un atributo de Favorite_Category con un tipo de datos de cadena.]({% image_buster /assets/img_archive/custom_attribute_data_type.png %}){: style="max-width:80%;"}

{% alert tip %}
Las cadenas y los arreglos requieren apóstrofos rectos a su alrededor, mientras que los booleanos y los enteros nunca llevan apóstrofos.
{% endalert %}

### Booleano {#boolean}

Los [booleanos]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#booleans) son valores binarios y pueden configurarse como `true` o `false`, como `registration_complete: true`. Los valores booleanos no llevan apóstrofos a su alrededor.

{% raw %}

```liquid
{% if {{custom_attribute.${registration_complete}}} == true %}
```

{% endraw %}

### Número {#number}

Los [números]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#custom-attribute-data-types) son valores numéricos, que pueden ser enteros o flotantes. Por ejemplo, un usuario puede tener `shoe_size: 10` o `levels_completed: 287`. Los valores numéricos no llevan apóstrofos a su alrededor.

{% raw %}

```liquid
{% if {{custom_attribute.${shoe_size}}} == 10 %}
```

{% endraw %}

También puedes usar otros [operadores básicos](https://shopify.dev/docs/themes/liquid/reference/basics/operators) como menor que (<) o mayor que (>) para enteros:

{% raw %}

```liquid
{% if {{custom_attribute.${flyer_miles}}} >= 500 %}
```

{% endraw %}

### Cadena {#string}

Una [cadena]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#custom-attribute-data-types) está compuesta por caracteres alfanuméricos y almacena un dato sobre tu usuario. Por ejemplo, puedes tener `favorite_color: red` o `phone_number: 3025981329`. Los valores de cadena deben llevar apóstrofos a su alrededor.

{% raw %}

```liquid
{% if {{custom_attribute.${favorite_color}}} == 'blue' %}
```

{% endraw %}

Para cadenas, puedes usar tanto "==" como "contains" en tu Liquid.

### Arreglo {#array}

Un [arreglo]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#custom-attribute-data-types) es una lista de información sobre tu usuario. Por ejemplo, un usuario puede tener `last_viewed_shows: stranger things, planet earth, westworld`. Los valores de arreglo deben llevar apóstrofos a su alrededor.

{% raw %}

```liquid
{% if {{custom_attribute.${last_viewed_shows}}} contains 'homeland' %}
```

{% endraw %}

Para arreglos, debes usar `contains` y no puedes usar `==`.

#### Cómo funciona `contains` con cadenas versus arreglos {#how-contains-works-with-strings-versus-arrays}

El operador `contains` se comporta de manera diferente dependiendo de si está evaluando una cadena o un arreglo:

- **Cadenas:** `contains` busca una subcadena en cualquier parte del texto.
- **Arreglos:** `contains` busca una coincidencia exacta con un elemento completo dentro del arreglo.

{% alert important %}
Si un atributo está almacenado como un arreglo (por ejemplo, `["med1", "med2", "abc"]`), buscar `contains "ab"` se evaluará como `false` porque ningún elemento individual en esa lista es exactamente `"ab"`.
{% endalert %}

##### Coincidencia de subcadenas en arreglos {#substring-matching-on-arrays}

Si necesitas buscar una coincidencia parcial (subcadena) dentro de un atributo de arreglo, primero debes convertir el arreglo en una sola cadena usando el filtro `join`.

Dado que Braze no admite filtros en línea directamente dentro de bloques condicionales {% raw %}`{% if %}`{% endraw %}, debes seguir un proceso de dos pasos: primero, asigna el valor unido a una variable y luego ejecuta tu verificación condicional.

{% raw %}
```liquid
{% comment %} 1. Convert the array to a string using a comma separator {% endcomment %}
{% assign products_string = {{custom_attribute.${product_array}}} | join: "," %}

{% comment %} 2. Perform the substring check on the new variable {% endcomment %}
{% if products_string contains "ab" %}
  Match found!
{% else %}
  No match.
{% endif %}
```
{% endraw %}


{% alert tip %}
Dado que `join` combina los elementos del arreglo en una sola cadena (separador predeterminado: un solo espacio), las verificaciones de subcadenas pueden coincidir a través de los límites de los elementos (por ejemplo, `["Napa", "boulevard"]` se convierte en `Napa boulevard`, donde `contains "a b"` es `true`). Usa un separador explícito como "," para hacer los límites más claros y reducir las coincidencias accidentales entre elementos.
{% endalert %}

### Hora {#time}

Una marca de tiempo de cuándo ocurrió un evento. Los valores de [hora]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#custom-attribute-data-types) deben tener un [filtro matemático]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/filters#math-filters) aplicado para poder usarse en lógica condicional.

{% raw %}

```liquid
{% assign expire = {{custom_attribute.${subscription_end_date}}} | plus: 0 %}
```

{% endraw %}