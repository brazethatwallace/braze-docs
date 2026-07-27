---
nav_title: Herramientas del dashboard
article_title: Herramientas del dashboard para personalización
page_order: 0
description: "Este artículo de referencia describe la experiencia de Añadir personalización en los editores de mensajes y páginas de inicio de Braze, incluyendo Liquid preformateado, valores predeterminados y mejoras del editor de Liquid como etiquetas de color y sugerencias predictivas."
---

# Herramientas del dashboard para personalización {#dashboard-tools-for-personalization}

> Usa las herramientas del dashboard de Braze para insertar personalización con Liquid sin tener que escribir cada etiqueta a mano. El flujo **Añadir personalización** construye la sintaxis correcta por ti, y el editor de Liquid te ayuda a leer y ampliar plantillas rápidamente.

Para las reglas de sintaxis de Liquid, etiquetas compatibles y patrones avanzados, consulta [Uso de Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid) y [Etiquetas de personalización compatibles]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags).

## Añadir personalización en creadores y configuración {#add-personalization-in-composers-and-settings}

La herramienta **Añadir personalización** aparece junto a los campos de texto con plantillas en todo el panel, incluyendo:

- **Campaign y pasos en Canvas** para canales que admiten Liquid en el cuerpo o los encabezados (por ejemplo, correo electrónico, push, SMS, mensajes dentro de la aplicación, Content Cards y webhooks).
- **Editores de arrastrar y soltar**, donde el control suele estar en la barra de herramientas del bloque o del editor. Por ejemplo, en los mensajes dentro de la aplicación de arrastrar y soltar puedes seleccionar **Añadir personalización**, elegir un tipo de personalización y luego colocar el fragmento de código generado en tu contenido antes de previsualizarlo en **Vista previa y prueba**. Para notas específicas de cada canal, consulta el artículo de arrastrar y soltar o del creador de tu canal (como [Configuración de estilo de mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/channels/in_app_messages/customize/style_settings#add-liquid) o [Crear un correo electrónico con arrastrar y soltar]({{site.baseurl}}/user_guide/channels/email/drag_and_drop)).
- **Creadores especializados** que exponen un selector de personalización; por ejemplo, las [recomendaciones de artículos]({{site.baseurl}}/user_guide/brazeai/item_recommendations/using_recommendations) usan opciones de **Tipo de personalización** como **Recomendación de artículos** dentro del mismo estilo de ventana.
- **Páginas de destino**, donde puedes añadir personalización con Liquid en el editor de arrastrar y soltar o en la configuración de la página y los bloques. Para más detalles, consulta [Personalizar páginas de destino]({{site.baseurl}}/user_guide/messaging/landing_pages/personalize_landing_pages).

## Insertar variables preformateadas y valores predeterminados {#insert-pre-formatted-variables-and-defaults}

La herramienta **Añadir personalización** te ayuda a insertar Liquid con valores predeterminados opcionales para que los datos de perfil vacíos no afecten tu texto.

![El modal Añadir personalización que aparece después de seleccionar insertar personalización. El modal tiene campos para tipo de personalización, atributo, valor predeterminado opcional y muestra una vista previa de la sintaxis Liquid.]({% image_buster /assets/img_archive/insert_liquid_var_arrow.png %}){: style="max-width:90%;"}

La herramienta inserta Liquid con el valor predeterminado que especificaste en el punto donde se encontraba tu cursor. El punto de inserción también se indica en el cuadro de vista previa, que muestra el texto anterior y posterior. Si un bloque de texto está resaltado, el texto resaltado será reemplazado.

![Un GIF del modal Añadir personalización que muestra al usuario insertando "fellow traveler" como valor predeterminado, y el modal reemplazando el texto resaltado "name" en el creador con el fragmento de código Liquid.]({% image_buster /assets/img_archive/insert_var_shot.gif %})

También puedes escribir {% raw %}`{{`{% endraw %} en muchos creadores para usar el autocompletado, o pegar etiquetas desde otro lugar; para más detalles, consulta [Insertar etiquetas]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid#inserting-tags) en **Uso de Liquid**.

### Asignar variables {#assign-variables}

{% raw %}
Algunas operaciones en Liquid requieren que almacenes el valor que deseas manipular como una variable. Esto suele ocurrir cuando tu instrucción Liquid incluye múltiples atributos, propiedades del evento o filtros.

Por ejemplo, supongamos que quieres sumar dos enteros de datos personalizados.

#### Ejemplo incorrecto de Liquid {#incorrect-liquid-example}

No puedes usar:

```liquid
{{custom_attribute.${one}}} | plus: {{custom_attribute.${two}}}
```

Este código Liquid no funciona porque no puedes hacer referencia a múltiples atributos en una sola línea; necesitas asignar una variable a al menos uno de estos valores antes de que se ejecuten las funciones matemáticas. Sumar dos atributos personalizados requeriría dos líneas de Liquid: una para asignar el atributo personalizado a una variable y otra para realizar la suma.

#### Ejemplo correcto de Liquid {#correct-liquid-example}

Puedes usar:

```liquid
{% assign value_one = {{custom_attribute.${one}}} %}
{% assign result = value_one | plus: {{custom_attribute.${two}}} %}
```

#### Tutorial: Usar variables para calcular un saldo {#tutorial-using-variables-to-calculate-a-balance}

Calculemos el saldo actual de un usuario sumando su saldo de tarjeta de regalo y su saldo de recompensas:

Primero, usa la etiqueta `assign` para sustituir el atributo personalizado de `current_rewards_balance` con el término "balance". Esto significa que ahora tienes una variable llamada `balance`, que puedes manipular.

```liquid
{% assign balance = {{custom_attribute.${current_rewards_balance}}} %}
```

A continuación, usaremos el filtro `plus` para combinar el saldo de tarjeta de regalo de cada usuario con su saldo de recompensas, representado por `{{balance}}`.

```liquid
{% assign balance = {{custom_attribute.${current_rewards_balance}}} %}
You have ${{custom_attribute.${giftcard_balance} | plus: {{balance}}}} to spend!
```
{% endraw %}

{% alert tip %}
¿Te encuentras asignando las mismas variables en cada mensaje? En lugar de escribir la etiqueta `assign` una y otra vez, puedes guardar esa etiqueta como un bloque de contenido y colocarla al inicio de tu mensaje.<br><br>

1. [Crea un bloque de contenido]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks#create-a-content-block).
2. Dale un nombre a tu bloque de contenido (sin espacios ni caracteres especiales).
3. Selecciona **Editar** en la parte inferior de la página.
4. Ingresa tus etiquetas `assign`.

Siempre que el bloque de contenido esté al inicio de tu mensaje, cada vez que la variable se inserte en tu mensaje como un objeto, hará referencia a tu atributo personalizado elegido.
{% endalert %}

## Mejoras del editor de Liquid {#liquid-editor-enhancements}

Estos comportamientos del panel facilitan el trabajo con Liquid mientras redactas mensajes.

### Etiquetas de color {#color-labels}

Cada elemento de Liquid corresponde a un color, lo que te permite diferenciar tu Liquid de un vistazo en tu editor de Liquid.

![Diagrama de varias etiquetas de color para diferentes elementos de Liquid.]({% image_buster /assets/img/liquid_color_code.png %})

### Liquid predictivo {#predictive-liquid}

También puedes usar Liquid predictivo para atributos personalizados, nombres de atributos y más mientras construyes tus mensajes personalizados.

![Braze recomendando diferentes atributos de Liquid a medida que se introduce más texto en un campo.]({% image_buster /assets/img/liquid_auto_complete.gif %}){: style="max-width:70%;"}

## Próximos pasos {#next-steps}

- [Uso de Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid): sintaxis, `assign`, condicionales y filtros en Braze
- [Configuración de valores predeterminados]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/setting_default_values): valores predeterminados en Liquid más allá del modal
- [Filtros]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/filters): formato de fechas, operaciones matemáticas, cadenas y más