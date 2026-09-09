---
nav_title: Configuración de estilos
article_title: "Configuración de estilos de mensajes dentro de la aplicación"
description: "Este artículo de referencia cubre las opciones de estilo disponibles al crear un mensaje dentro de la aplicación con el editor de arrastrar y soltar."
page_order: 1
---

# Configuración de estilos de mensajes dentro de la aplicación {#in-app-message-style-settings}

> La experiencia de edición de arrastrar y soltar se divide en dos secciones: **Build** y **vista previa & Test**. Este artículo cubre lo que necesitas saber para trabajar dentro de la pestaña **Build** del editor y asume que ya has [creado un mensaje dentro de la aplicación]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop).

![Pestaña "Estilos de mensaje".]({% image_buster /assets/img_archive/dnd_iam_message_styles.png %}){: style="float:right;max-width:25%;margin-left:15px;max-width:30%"}

## Estilos a nivel de mensaje {#message-level-styles}

Puedes establecer ciertos estilos que se aplicarán en todos los bloques relevantes de tu mensaje dentro de la aplicación desde la pestaña **Estilos del mensaje**. Por ejemplo, puedes personalizar la fuente de todo el texto o el color de todos los enlaces en tu mensaje.

Los estilos de esta sección se utilizan en todas partes de tu mensaje, excepto donde los sustituyas para un bloque específico. Si tu mensaje tiene [varias páginas]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop#multi-page), también puedes sustituir los estilos a nivel de mensaje para páginas individuales, excepto el tipo de visualización y el ancho máximo.

Para una experiencia de diseño más sencilla, te recomendamos configurar los estilos a nivel de mensaje antes de personalizar los estilos a nivel de bloque.

Para volver a la pestaña **Estilos del mensaje** en cualquier momento:

- Haz clic en el botón X de cierre en las propiedades de un bloque individual
- Selecciona el contenedor del mensaje, el botón X de cierre del mensaje o el fondo del editor

### Fuentes personalizadas {#custom-fonts}

Aceptamos los siguientes tipos de archivo para fuentes: `.ttf`, `.woff`, `.otf` y `.woff2`. Para más información, consulta [Archivos de activos]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html#asset-files).

Puedes añadir múltiples variaciones de una familia de fuentes, ya que es posible que algunas opciones de estilo no estén disponibles para fuentes personalizadas. Actualmente, no admitimos la adición de fuentes a través de URL.

Para añadir una fuente personalizada:

1. Ve a la sección **Contenido** en la pestaña **Estilos del mensaje**.
2. Haz clic en **Añadir fuente personalizada**.
3. Sube tu fuente usando la biblioteca multimedia.

{% alert note %}
La fuente a nivel de mensaje solo se aplicará al mensaje actual y a los mensajes duplicados, pero no a plantillas futuras.
{% endalert %}

## Componentes del mensaje {#message-components}

![Un GIF que muestra la creación de un mensaje dentro de la aplicación promocional.]({% image_buster /assets/img_archive/dnd_iam_create.gif %})

El editor de arrastrar y soltar utiliza dos componentes clave para componer mensajes dentro de la aplicación: **filas** y **bloques**. Todos los bloques deben colocarse en una fila.

### Botón de cierre x {#close-x-button}

Para los mensajes dentro de la aplicación de tipo modal y de pantalla completa, puedes personalizar el botón de cierre que se muestra como <i class="fa-solid fa-xmark"></i> en la parte superior del mensaje. Las opciones de personalización incluyen la posición del botón, el tamaño, el color de relleno, el color de fondo, el estilo del borde y el radio del borde.

![Opciones para personalizar el botón de cierre x en mensajes dentro de la aplicación, incluyendo tamaño del botón, color de relleno, color de fondo, estilo del borde y radio del borde.]({% image_buster /assets/img_archive/close_x_button.png %}){: style="max-width:40%"}

### Estilo de span {#span-styling}

Añadir estilos de span al texto dentro de los mensajes dentro de la aplicación permite una personalización mejorada de la apariencia del mensaje, habilitando el uso de diferentes colores de texto, fuentes y tamaños. El estilo de span ofrece a tus usuarios una experiencia más atractiva y visualmente agradable al dirigir su atención a la información clave y mejorar la claridad general del mensaje.

![Opción que se muestra al resaltar texto en un mensaje dentro de la aplicación. Un pequeño icono de pincel indica que puedes envolver con span para aplicar estilo.]({% image_buster /assets/img_archive/span_1.png %}){: style="max-width:40%"}

![Panel lateral de "Propiedades de span" que permite al usuario final personalizar la familia tipográfica, el peso de fuente, el tamaño de fuente, el espaciado entre letras y el color del texto.]({% image_buster /assets/img_archive/span_2.png %}){: style="max-width:40%"}

### Filas {#rows}

Las filas son unidades estructurales que definen la composición horizontal de una sección del mensaje mediante el uso de celdas.

![Filas que puedes añadir en tu mensaje dentro de la aplicación.]({% image_buster /assets/img_archive/dnd_iam_rows.png %}){: style="max-width:40%"}

Cuando se selecciona una fila, puedes añadir o eliminar el número de columnas que necesites desde la sección **Personalización de columnas** para colocar diferentes elementos de contenido uno junto a otro.

También puedes deslizar para ajustar el tamaño de las columnas existentes.

![Ajuste de columnas desde la sección "Personalización de columnas".]({% image_buster /assets/img_archive/dnd_iam_column_customization.gif %}){: style="max-width:40%"}

Como práctica recomendada, da formato a las propiedades de tus filas y columnas antes de dar formato a cualquiera de los bloques dentro de las filas. Hay muchos lugares donde puedes ajustar el espaciado y la alineación, así que empezar por la base facilita la edición a medida que avanzas.

#### Imagen de fondo {#background-image}

Puedes añadir una imagen de fondo a una fila en el panel **Propiedades de la fila**. Activa **Imagen de fondo** y luego proporciona una URL de imagen o selecciona una imagen de la [biblioteca de medios]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library). Por último, configura tu texto alternativo, tamaño, posición y si la imagen se repite para crear patrones a lo largo de la fila.

![Una imagen de fondo de una pizza con un patrón de repetición horizontal.]({% image_buster /assets/img_archive/background_row.png %})

### Bloques {#blocks}

Los bloques representan diferentes tipos de contenido que puedes usar en tu mensaje. Arrastra uno dentro de un segmento de fila existente y se ajustará automáticamente al ancho de la celda.

{% alert tip %}
Antes de añadir bloques, configura los [estilos a nivel de mensaje](#set-message-level-styles) para el contenedor del mensaje, la fuente, los colores y cualquier otra cosa que quieras personalizar. Luego puedes personalizar los bloques individuales según sea necesario. El **Botón de cierre** permanecerá en la sección superior de tu mensaje para que los usuarios siempre tengan la opción de descartarlo.
{% endalert %}

![Cajas de arrastrar y soltar para seleccionar.]({% image_buster /assets/img_archive/dnd_iam_editor_blocks.png %}){: style="max-width:40%"}

Cada bloque tiene su configuración, como control granular del relleno. El panel del lado derecho cambia automáticamente a un panel de estilos para el elemento de contenido seleccionado. Para más información, consulta [Propiedades de los bloques de editor]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=in-app%20messages#inappmessages_properties).

A medida que construyes tu mensaje dentro de la aplicación, puedes seleccionar una vista de móvil, tableta o escritorio en la barra de herramientas para previsualizar cómo se ve tu mensaje dentro de la aplicación para tus grupos de usuarios. Esto garantiza que tu contenido sea receptivo y puedas hacer los ajustes necesarios sobre la marcha.

## Detalles creativos {#creative-details}

### Pantalla completa en pantallas más grandes {#fullscreen}

En una tableta o un navegador de escritorio, un mensaje dentro de la aplicación a pantalla completa se situará en el centro de la pantalla de la aplicación. Cualquier edición del ancho máximo del mensaje a pantalla completa solo se aplicará a dispositivos de tableta y escritorio.

![Ejemplo de mensaje dentro de la aplicación a pantalla completa.]({% image_buster /assets/img_archive/dnd_iam_fullscreen_example.png %}){: style="border:none"}

### Añadir una imagen de fondo {#add-a-background-image}

Puedes añadir una imagen al fondo de tu mensaje desde la pestaña **Estilos de mensaje**.

1. En el área del lienzo, selecciona el contenedor de fondo. Esta es la sección desplazable de tu mensaje.
2. En la pestaña **Estilos de mensaje**, activa **Imagen de fondo**.
3. Añade una imagen de tu biblioteca multimedia o introduce la URL donde está alojada tu imagen.

{% alert tip %}
Si tienes problemas para seleccionar un bloque determinado, puedes usar la flecha hacia arriba en la barra de herramientas en línea del bloque para mover el foco hacia cada bloque principal.
{% endalert %}

#### Intercambiar imágenes de fondo con Liquid {#swap-background-images-with-liquid}

Para intercambiar dinámicamente imágenes de fondo en función de los datos de usuario (como atributos personalizados o propiedades de usuario), utiliza bloques {% raw %}`{% capture %}`{% endraw %} de Liquid para asignar la URL de imagen correcta a una variable antes de que se carguen el HTML y el CSS.

Coloca tu lógica de Liquid al principio de tu mensaje y luego haz referencia a la variable capturada en el campo de URL de la imagen de fondo. Esto selecciona la imagen correcta según los datos de cada usuario.

Después de capturar la URL de la imagen, usa {% raw %}`{{ image_url | strip }}`{% endraw %} para generar la URL con los espacios en blanco adicionales eliminados. Luego puedes pegar este Liquid en el campo de URL de la imagen de fondo para mostrar dinámicamente diferentes imágenes a diferentes usuarios.

##### Ejemplo {#example}

{% raw %}
```liquid
{% capture image_url %}
{% if {{custom_attribute.${membership_tier}}} == 'gold' %}
https://example.com/images/gold-background.png
{% elsif {{custom_attribute.${membership_tier}}} == 'silver' %}
https://example.com/images/silver-background.png
{% else %}
https://example.com/images/default-background.png
{% endif %}
{% endcapture %}
{{ image_url | strip }}
```
{% endraw %}

### Añadir Liquid {#add-liquid}

![Icono para añadir personalización con Liquid.]({% image_buster /assets/img_archive/dnd_iam_liquid.png %}){: style="float:right;max-width:25%;margin-left:15px"}

Para añadir [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) a tu mensaje dentro de la aplicación, selecciona <i class="fa-solid fa-circle-plus"></i> **Añadir personalización** en la barra de herramientas del editor. Aquí puedes añadir varios tipos de personalización, como atributos predeterminados, atributos de dispositivo, atributos personalizados y más.

A continuación, toma tu fragmento de código de Liquid generado e insértalo en tu mensaje. Después de diseñar y crear tu mensaje dentro de la aplicación, ve a **Vista previa y prueba** para previsualizar tu mensaje.

### Usar el redactor con IA {#use-the-ai-copywriter}

Cuando un bloque de texto esté seleccionado en tu mensaje dentro de la aplicación, selecciona <i class="fa-solid fa-wand-magic-sparkles" title="Redactor con IA"></i> **Redactor con IA** en la barra de herramientas del bloque para iniciar el [asistente de redacción con IA]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#generate-copy). El asistente de redacción con IA envía un nombre o descripción breve del producto a la herramienta de generación de texto GPT3 de OpenAI para generar textos de marketing similares a los humanos para tus mensajes.

{% alert tip %}
Puedes ahorrarte algunos clics resaltando el texto dentro del bloque antes de hacer clic en el icono. El texto resaltado se añadirá a la herramienta y el texto se generará de inmediato.
{% endalert %}

![GIF del redactor con IA.]({% image_buster /assets/img_archive/dnd_iam_ai_copywriter.gif %})

### Restablecer estilos a los valores predeterminados {#reset-styles-to-default}

Las propiedades que hayas cambiado respecto a su estilo predeterminado se marcan con un punto naranja. Para restablecer una propiedad específica a su estilo predeterminado, pasa el cursor sobre el campo y selecciona **Restablecer a predeterminado**.

![Punto naranja que restablece el tamaño de texto a su tamaño predeterminado.]({% image_buster /assets/img_archive/dnd_iam_reset_styles.gif %}){: style="max-width:45%"}

También puedes restablecer todos los estilos de un elemento seleccionado haciendo clic en <i class="fas fa-paintbrush" title="Botón para copiar o pegar estilos"></i> junto al nombre del panel de propiedades y seleccionando **Restablecer a estilos predeterminados**.

### Copiar y pegar estilos {#copy-and-paste-styles}

Después de realizar cambios en el estilo de un elemento, puedes copiar y pegar esos estilos en otro elemento. Al pegar estilos, solo se aplican las propiedades relevantes para ese elemento.

![Menú desplegable con la opción de copiar estilos.]({% image_buster /assets/img_archive/dnd_iam_copypaste_styles.png %}){: style="float:right;margin-left:15px;max-width:35%"}

1. Con el elemento seleccionado, selecciona <i class="fas fa-paintbrush" title="Copiar o pegar estilos"></i> **Copiar o pegar estilos** junto al nombre del panel de propiedades (por ejemplo, si tienes un botón seleccionado, junto a "Propiedades del botón").
2. Haz clic en **Copiar estilos** y selecciona el elemento donde deseas aplicar el estilo copiado.
3. Selecciona <i class="fas fa-paintbrush" title="Copiar o pegar estilos"></i> **Copiar o pegar estilos** de nuevo y elige **Pegar estilos**.

#### Atajos de teclado {#keyboard-shortcuts}

También puedes usar atajos de teclado para copiar y pegar estilos:

| Acción        | Mac                                            | Windows                                           |
| ------------- | ---------------------------------------------- | ------------------------------------------------- |
| Copiar estilos  | <kbd>⌘</kbd> + <kbd>Shift</kbd> + <kbd>c</kbd> | <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>c</kbd> |
| Pegar estilos | <kbd>⌘</kbd> + <kbd>Shift</kbd> + <kbd>v</kbd> | <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>v</kbd> |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Atajos de teclado" }