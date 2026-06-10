---
nav_title: Usar Liquid
article_title: Usar Liquid
page_order: 0
description: "Este artículo de referencia ofrece un resumen de los casos de uso comunes de Liquid y cómo incluir etiquetas de Liquid en tu mensajería."
search_rank: 2
---

# [![Curso de Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/path/dynamic-personalization-with-liquid){: style="float:right;width:120px;border:0;" class="noimgborder"}Usar Liquid {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecompathdynamic-personalization-with-liquid-stylefloatrightwidth120pxborder0-classnoimgborderuse-liquid}

> Este artículo muestra cómo puedes usar una variedad de atributos de usuario para insertar dinámicamente información personal en tu mensajería.

Liquid es un lenguaje de plantillas de código abierto desarrollado por Shopify y escrito en Ruby. Puedes usarlo en Braze para extraer datos del perfil de usuario en tus mensajes y personalizar esos datos. Por ejemplo, puedes usar etiquetas de Liquid para crear mensajes condicionales, como enviar diferentes ofertas basadas en la fecha de aniversario de suscripción de un usuario. Además, los filtros pueden manipular datos, como dar formato a la fecha de registro de un usuario desde una marca de tiempo a un formato más legible, como "15 de enero de 2022". Para más detalles sobre la sintaxis de Liquid y sus capacidades, consulta [Etiquetas de personalización compatibles]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags/).

## Cómo funciona {#how-it-works}

Las etiquetas de Liquid actúan como marcadores de posición en tus mensajes que pueden extraer información consentida de la cuenta de tu usuario y habilitar prácticas de personalización y mensajería relevante.

En el siguiente bloque, puedes ver un uso dual de una etiqueta de Liquid para llamar al nombre del usuario, así como una etiqueta predeterminada en caso de que un usuario no tenga su nombre registrado.

{% raw %}
```liquid
Hi {{ ${first_name} | default: 'Valued User' }}, thanks for using the App!
```
{% endraw %}

Para una usuaria llamada Janet Doe, el mensaje aparecería como:

```
Hi Janet, thanks for using the App!
```

O...

```
Hi Valued User, thanks for using the App!
```

{% alert important %}
Los comentarios HTML (`<!-- -->`) se eliminan antes de que se lea cualquier Liquid, por lo que las etiquetas de Liquid dentro de los comentarios HTML **no se** renderizan en tu mensaje. Para un renderizado correcto, asegúrate de que todas las etiquetas de Liquid que quieras usar estén fuera de los comentarios HTML.
{% endalert %}

## Valores compatibles para sustituir {#supported-values-to-substitute}

Los siguientes valores pueden sustituirse en un mensaje, dependiendo de su disponibilidad:

- [Información básica del usuario]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags/) (por ejemplo, `first_name`, `last_name`, `email_address`)
- [Atributos personalizados]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/)
    - [Atributos personalizados anidados]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support/#liquid-templating)
- [Propiedades de eventos personalizados]({{site.baseurl}}/user_guide/data/activation/events/custom_events/)
- [Información del dispositivo usado más recientemente]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags/#most-recently-used-device-information)
- [Información del dispositivo objetivo]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags/#targeted-device-information)

También puedes extraer contenido directamente de un servidor web a través del [Contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/) de Braze.

{% alert important %}
Braze actualmente es compatible con Liquid hasta e incluyendo Liquid 5 de Shopify.
{% endalert %}

## Usar Liquid {#using-liquid}

Usando [etiquetas de Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags/), puedes elevar la calidad de tus mensajes enriqueciéndolos con un toque personal.

### Sintaxis de Liquid {#liquid-syntax}

Liquid sigue una estructura específica, o sintaxis, que deberás tener en cuenta mientras creas personalización dinámica. Aquí tienes algunas reglas básicas a recordar:

1. **Usa comillas rectas en Braze:** Hay una diferencia entre las comillas tipográficas (**' '**) y las comillas rectas (**&#39; &#39;**). Usa comillas rectas (**&#39; &#39;**) en tu Liquid en Braze. Puedes ver comillas tipográficas al copiar y pegar desde ciertos editores de texto, lo que puede causar problemas en tu Liquid. Si introduces las comillas directamente en el dashboard de Braze, ¡no tendrás problemas!
2. **Las llaves van en pares:** Cada llave debe abrirse y cerrarse **{ }**. ¡Asegúrate de usar llaves!
3. **Las sentencias if van en pares:** Por cada `if`, necesitas un `endif` para indicar que la sentencia `if` ha terminado.
4. **Las sentencias case van en pares:** Por cada `case`, necesitas un `endcase` para cerrar el bloque.
5. **Los nombres de variables deben usar caracteres ASCII:** Los nombres de variables de Liquid (creados con `assign` o `capture`) solo admiten letras ASCII, dígitos y guiones bajos. Los nombres de atributos de personalización de Braze (dentro de `custom_attribute.${...}` o `event_properties.${...}`) pueden incluir caracteres no ASCII.

#### Dónde usar operadores y filtros {#where-to-use-operators-and-filters}

Los operadores (como `==`, `!=`, `>`, `and`, `or`) y los filtros (como `| size`, `| plus`) solo pueden usarse en contextos específicos de Liquid.

| Contexto | Operadores | Filtros |
|-----------|-----------|---------|
| `assign` | No compatible | Compatible |
| `if`, `elsif`, `unless` | Compatible | No compatible |
| `case`, `when` | Solo coincidencia de igualdad[^case_when_ops] | No compatible |
| `for` | No compatible | No compatible |
| Acceso a arrays (`[ ]`) | No compatible | No compatible |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Dónde usar operadores y filtros" }

[^case_when_ops]: En las etiquetas `case` y `when`, Liquid compara la expresión `case` con cada valor `when` usando igualdad (similar a encadenar `if` y `elsif` con `==`). No puedes usar operadores de comparación arbitrarios ni operadores lógicos dentro de una cláusula `when` como lo haces con `if` y `elsif`. Para ver ejemplos, consulta [Lógica de mensajería condicional]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic/#case-and-when-tags).

Cuando necesites un valor filtrado en un contexto que no admite filtros, asigna primero el resultado a una variable.

{% raw %}

##### Usar el resultado de un filtro en un condicional {#use-a-filter-result-in-a-conditional}

No puedes usar un filtro directamente en una sentencia condicional. Esto es incorrecto:

```liquid
{% if my_array | size > 3 %}
You have more than 3 items!
{% endif %}
```

En su lugar, asigna el resultado del filtro a una variable:

```liquid
{% assign array_size = my_array | size %}
{% if array_size > 3 %}
You have more than 3 items!
{% endif %}
```

##### Usar el resultado de un filtro en un bucle for {#use-a-filter-result-in-a-for-loop}

No puedes aplicar un filtro al iterable en un bucle `for`. Esto es incorrecto:

```liquid
{% for item in my_array | reverse %}
{{ item }}
{% endfor %}
```

En su lugar, asigna el valor filtrado a una variable:

```liquid
{% assign reversed = my_array | reverse %}
{% for item in reversed %}
{{ item }}
{% endfor %}
```

##### Usar el resultado de un filtro para acceso a arrays {#use-a-filter-result-for-array-access}

No puedes usar un filtro dentro de corchetes. Esto es incorrecto:

```liquid
{{ my_array[my_var | minus: 1] }}
```

En su lugar, asigna primero el valor filtrado:

```liquid
{% assign adjusted_index = my_var | minus: 1 %}
{{ my_array[adjusted_index] }}
```

##### Almacenar el resultado de una comparación en una variable {#store-a-comparison-result-in-a-variable}

No puedes usar un operador en una sentencia `assign`. Esto es incorrecto:

```liquid
{% assign is_vip = total_spend > 100 %}
{% if is_vip %}
Welcome to the VIP lounge!
{% endif %}
```

En su lugar, usa un condicional para establecer la variable:

```liquid
{% assign is_vip = false %}
{% if total_spend > 100 %}
{% assign is_vip = true %}
{% endif %}

{% if is_vip %}
Welcome to the VIP lounge!
{% endif %}
```

{% endraw %}

#### Atributos predeterminados y atributos personalizados {#default-attributes-and-custom-attributes}

{% raw %}

Si incluyes el siguiente texto en tu mensaje: `{{${first_name}}}`, el nombre del usuario (extraído del perfil de usuario) se sustituirá cuando se envíe el mensaje. Puedes usar el mismo formato con otros atributos predeterminados del usuario.

Si deseas usar el valor de un atributo personalizado, debes añadir el espacio de nombres "custom_attribute" a la variable. Por ejemplo, para usar un atributo personalizado llamado "zip code", incluirías `{{custom_attribute.${zip code}}}` en tu mensaje.

### Insertar etiquetas {#inserting-tags}

Puedes insertar etiquetas escribiendo dos llaves de apertura `{{` en cualquier mensaje, lo que activará una función de autocompletado que seguirá actualizándose a medida que escribas. Incluso puedes seleccionar una variable de las opciones que aparecen mientras escribes.

Si estás usando una etiqueta personalizada, puedes copiar y pegar la etiqueta en el mensaje que desees.

#### Excepciones para llaves dobles {#exceptions-for-double-brackets}

Si usas una etiqueta dentro de otra etiqueta de Liquid, como `{% assign %}` o `{% if %}`, puedes usar llaves dobles o ninguna llave. Solo cuando la etiqueta está sola debe estar encerrada en llaves dobles. Para simplificar, siempre puedes usar llaves dobles.

Las siguientes etiquetas son todas correctas:

```liquid
{% if custom_attribute.${Number_Game_Attended} == 1 %}
{% if {{custom_attribute.${Number_Game_Attended}}} == 1 %}

{% assign value_one = {{custom_attribute.${one}}} %}
{% assign value_one = custom_attribute.${one} %}
```

{% endraw %}

{% alert note %}

Si usas Liquid en tus mensajes de correo electrónico, asegúrate de:

1. Insertarlo usando el editor HTML en lugar del editor clásico. El editor clásico puede interpretar el Liquid como texto plano. Por ejemplo, el Liquid se interpretaría como {% raw %}`Hi {{ ${first_name} }}, thanks for using our service!`{% endraw %} en lugar de insertar el nombre del usuario mediante la plantilla.
2. Colocar el código Liquid solo dentro de la etiqueta `<body>`. Colocarlo fuera de esta etiqueta puede causar un renderizado inconsistente en la entrega.

{% endalert %}

### Cambiar entre los editores HTML y clásico {#switching-between-html-and-classic-editors}

Cuando cambias entre los editores HTML y clásico, los fragmentos de código de Liquid y los Content Blocks pueden cambiar de posición en tu mensaje. Revisa tu plantilla después de cambiar de editor. Si necesitas un control de diseño más predecible, usa el editor de arrastrar y soltar.

### Insertar variables preformateadas {#inserting-pre-formatted-variables}

Puedes insertar variables preformateadas con valores predeterminados a través del modal **Añadir personalización** ubicado cerca de cualquier campo de texto con plantilla.

![El modal Añadir personalización que aparece después de seleccionar insertar personalización. El modal tiene campos para tipo de personalización, atributo, valor predeterminado opcional y muestra una vista previa de la sintaxis de Liquid.]({% image_buster /assets/img_archive/insert_liquid_var_arrow.png %}){: style="max-width:90%;"}

El modal insertará Liquid con tu valor predeterminado especificado en el punto donde estaba tu cursor. El punto de inserción también se especifica mediante el cuadro de vista previa, que muestra el texto anterior y posterior. Si un bloque de texto está resaltado, el texto resaltado será reemplazado.

![Un GIF del modal Añadir personalización que muestra al usuario insertando "fellow traveler" como valor predeterminado, y el modal reemplazando el texto resaltado "name" en el compositor con el fragmento de código de Liquid.]({% image_buster /assets/img_archive/insert_var_shot.gif %})