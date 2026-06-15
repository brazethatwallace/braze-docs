---
nav_title: Configuración de estilos
article_title: "Configuración de estilos de mensajes dentro de la aplicación"
description: "Este artículo de referencia cubre las opciones de estilo disponibles al crear un mensaje dentro de la aplicación con el editor de arrastrar y soltar."
page_order: 1
---

# Configuración de estilos de mensajes dentro de la aplicación {#in-app-message-style-settings}

> La experiencia de edición de arrastrar y soltar se divide en dos secciones: **Build** y **Preview & Test**. Este artículo cubre lo que necesitas saber para trabajar dentro de la pestaña **Build** del editor y asume que ya has [creado un mensaje dentro de la aplicación]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/).

![Pestaña "Estilos de mensaje".]({% image_buster /assets/img_archive/dnd_iam_message_styles.png %}){: style="float:right;max-width:25%;margin-left:15px;max-width:30%"}

## Estilos a nivel de mensaje {#message-level-styles}

Puedes configurar ciertos estilos para que se apliquen a todos los bloques relevantes de tu mensaje dentro de la aplicación desde la pestaña **Message Styles**. Por ejemplo, puedes personalizar la fuente de todo el texto o el color de todos los enlaces de tu mensaje.

Los estilos de esta sección se utilizan en todo tu mensaje, excepto donde los anules para un bloque específico. Si tu mensaje tiene [varias páginas]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/#multi-page), también puedes anular los estilos a nivel de mensaje para páginas individuales, excepto el tipo de visualización y el ancho máximo.

Para una experiencia de diseño más sencilla, te recomendamos configurar los estilos a nivel de mensaje antes de personalizar los estilos a nivel de bloque.

Para volver a la pestaña **Message Styles** en cualquier momento:

- Haz clic en el botón de cierre X en las propiedades de bloques individuales
- Selecciona el contenedor del mensaje, el botón de cierre X del mensaje o el fondo del editor

### Fuentes personalizadas {#custom-fonts}

Aceptamos los siguientes tipos de archivo para fuentes: `.ttf`, `.woff`, `.otf` y `.woff2`. Para más información, consulta [Archivos de activos]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html/#asset-files).

Puedes añadir múltiples variaciones de una familia de fuentes, ya que algunas opciones de estilo pueden no estar disponibles para fuentes personalizadas. Actualmente, no admitimos la adición de fuentes a través de URL.

Para añadir una fuente personalizada:

1. Ve a la sección **Content** en la pestaña **Message styles**.
2. Haz clic en **Add custom font**.
3. Carga tu fuente usando la biblioteca de medios.

{% alert note %}
La fuente a nivel de mensaje solo se aplicará al mensaje actual y a cualquier mensaje duplicado, pero no a plantillas futuras.
{% endalert %}

## Componentes del mensaje {#message-components}

![Un GIF que muestra la creación de un mensaje promocional dentro de la aplicación.]({% image_buster /assets/img_archive/dnd_iam_create.gif %})

El editor de arrastrar y soltar utiliza dos componentes clave para componer mensajes dentro de la aplicación: **filas** y **bloques**. Todos los bloques deben colocarse dentro de una fila.

### Botón de cierre X {#close-x-button}

Para mensajes dentro de la aplicación de tipo modal y pantalla completa, puedes personalizar el botón de cierre que se muestra como <i class="fa-solid fa-xmark"></i> en la esquina superior derecha de tu mensaje. Las opciones de personalización incluyen posición del botón, tamaño, color de relleno, color de fondo, estilo de borde y radio de borde.

![Opciones para personalizar el botón de cierre X en mensajes dentro de la aplicación, incluyendo tamaño del botón, color de relleno, color de fondo, estilo de borde y radio de borde.]({% image_buster /assets/img_archive/close_x_button.png %}){: style="max-width:40%"}

### Estilo span {#span-styling}

Añadir estilo span al texto dentro de los mensajes dentro de la aplicación permite una personalización mejorada de la apariencia del mensaje, habilitando el uso de diferentes colores de texto, fuentes y tamaños. El estilo span ofrece a tus usuarios una experiencia más atractiva y visualmente agradable al dirigir su atención a la información clave y mejorar la claridad general del mensaje.

![Opción que se muestra al resaltar texto en un mensaje dentro de la aplicación. Un pequeño icono de pincel indica que puedes envolver con span para aplicar estilo.]({% image_buster /assets/img_archive/span_1.png %}){: style="max-width:40%"}

![Panel lateral de "Propiedades de span" que permite al usuario final personalizar la familia de fuentes, el peso de la fuente, el tamaño de la fuente, el espaciado entre letras y el color del texto.]({% image_buster /assets/img_archive/span_2.png %}){: style="max-width:40%"}

### Filas {#rows}

Las filas son unidades estructurales que definen la composición horizontal de una sección del mensaje mediante celdas.

![Filas que puedes añadir en tu mensaje dentro de la aplicación.]({% image_buster /assets/img_archive/dnd_iam_rows.png %}){: style="max-width:40%"}

Cuando se selecciona una fila, puedes añadir o eliminar el número de columnas que necesites desde la sección **Column customization** para colocar diferentes elementos de contenido uno al lado del otro.

También puedes deslizar para ajustar el tamaño de las columnas existentes.

![Ajuste de columnas desde la sección "Column customization".]({% image_buster /assets/img_archive/dnd_iam_column_customization.gif %}){: style="max-width:40%"}

Como buena práctica, formatea las propiedades de tus filas y columnas antes de formatear cualquiera de los bloques dentro de las filas. Hay muchos lugares donde puedes ajustar el espaciado y la alineación, así que empezar desde la base facilita la edición a medida que avanzas.

#### Imagen de fondo {#background-image}

Puedes añadir una imagen de fondo a una fila en el panel **Row properties**. Activa **Background image** y luego proporciona una URL de imagen o selecciona una imagen de la [biblioteca de medios]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/). Finalmente, configura tu texto alternativo, tamaño, posición y si la imagen se repite para crear patrones a lo largo de la fila.

![Una imagen de fondo de fila de una pizza con un patrón de repetición horizontal.]({% image_buster /assets/img_archive/background_row.png %})

### Bloques {#blocks}

Los bloques representan diferentes tipos de contenido que puedes usar en tu mensaje. Arrastra uno dentro de un segmento de fila existente y se ajustará automáticamente al ancho de la celda.

{% alert tip %}
Antes de añadir bloques, configura los [estilos a nivel de mensaje](#set-message-level-styles) para el contenedor del mensaje, la fuente, los colores y cualquier otra cosa que quieras personalizar. Luego puedes personalizar bloques individuales según sea necesario. El **botón de cierre** permanecerá en la sección superior de tu mensaje para que los usuarios siempre tengan la opción de descartar el mensaje.
{% endalert %}

![Cajas de arrastrar y soltar para seleccionar.]({% image_buster /assets/img_archive/dnd_iam_editor_blocks.png %}){: style="max-width:40%"}

Cada bloque tiene su propia configuración, como control granular del relleno. El panel del lado derecho cambia automáticamente a un panel de estilos para el elemento de contenido seleccionado. Para más información, consulta [Propiedades de bloques del editor]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=in-app%20messages#inappmessages_properties).

A medida que construyes tu mensaje dentro de la aplicación, puedes seleccionar una vista de móvil, tableta o escritorio en la barra de herramientas para previsualizar cómo se verá tu mensaje dentro de la aplicación para tus grupos de usuarios. Esto asegurará que tu contenido sea adaptable y podrás hacer los ajustes necesarios sobre la marcha.

## Detalles creativos {#creative-details}

### Pantalla completa en pantallas más grandes {#fullscreen}

En un navegador de tableta o escritorio, un mensaje dentro de la aplicación de pantalla completa se ubicará en el centro de la pantalla de la aplicación. Cualquier edición al ancho máximo del mensaje de pantalla completa solo se aplicará a dispositivos de tableta y escritorio.

![Ejemplo de mensaje dentro de la aplicación a pantalla completa.]({% image_buster /assets/img_archive/dnd_iam_fullscreen_example.png %}){: style="border:none"}

### Añadir una imagen de fondo {#adding-a-background-image}

Puedes añadir una imagen al fondo de tu mensaje desde la pestaña **Message styles**.

1. En el área del Canvas, selecciona el contenedor de fondo. Esta es la sección desplazable de tu mensaje.
2. En la pestaña **Message styles**, activa **Background image**.
3. Añade una imagen desde tu biblioteca de medios o introduce la URL donde está alojada tu imagen.

{% alert tip %}
Si tienes problemas para seleccionar un bloque determinado, puedes usar la flecha hacia arriba en la barra de herramientas en línea del bloque para mover el foco hacia arriba a cada bloque padre.
{% endalert %}

### Añadir Liquid {#adding-liquid}

![Icono para añadir personalización con Liquid.]({% image_buster /assets/img_archive/dnd_iam_liquid.png %}){: style="float:right;max-width:25%;margin-left:15px"}

Para añadir [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/) a tu mensaje dentro de la aplicación, selecciona <i class="fa-solid fa-circle-plus"></i> **Add Personalization** desde la barra de herramientas del editor. Aquí puedes añadir varios tipos de personalización como atributos predeterminados, atributos de dispositivo, atributos personalizados y más.

A continuación, toma tu fragmento de código Liquid generado e insértalo en tu mensaje. Después de diseñar y construir tu mensaje dentro de la aplicación, ve a **Preview & Test** para previsualizar tu mensaje.

### Usar el asistente de redacción con inteligencia artificial {#using-the-ai-copywriter}

Cuando un bloque de texto está seleccionado en tu mensaje dentro de la aplicación, selecciona <i class="fa-solid fa-wand-magic-sparkles" title="Asistente de redacción con IA"></i> **AI copywriter** en la barra de herramientas del bloque para lanzar el [asistente de redacción con inteligencia artificial]({{site.baseurl}}/user_guide/brazeai/generative_ai/copywriting/). El asistente de redacción con inteligencia artificial pasa un nombre o descripción breve del producto a la herramienta de generación de texto GPT3 de OpenAI para generar textos de marketing similares a los escritos por humanos para tu mensajería.

{% alert tip %}
Puedes ahorrarte algunos clics resaltando el texto dentro del bloque antes de hacer clic en el icono. El texto resaltado se añadirá a la herramienta y se generará el texto de inmediato.
{% endalert %}

![GIF del asistente de redacción con IA.]({% image_buster /assets/img_archive/dnd_iam_ai_copywriter.gif %})

### Restablecer estilos a los valores predeterminados {#resetting-styles-to-default}

Las propiedades que hayas cambiado respecto a su estilo predeterminado están marcadas con un punto naranja. Para restablecer una propiedad específica a su estilo predeterminado, pasa el cursor sobre el campo y selecciona **Reset to default**.

![Punto naranja que restablece el tamaño de texto a su tamaño predeterminado.]({% image_buster /assets/img_archive/dnd_iam_reset_styles.gif %}){: style="max-width:45%"}

También puedes restablecer todos los estilos de un elemento seleccionado haciendo clic en <i class="fas fa-paintbrush" title="Botón de copiar o pegar estilos"></i> junto al nombre del panel de propiedades y seleccionando **Reset to default styles**.

### Copiar y pegar estilos {#copying-and-pasting-styles}

Después de hacer cambios en el estilo de un elemento, puedes copiar y pegar esos estilos en otro elemento. Al pegar estilos, solo se aplican las propiedades relevantes para ese elemento.

![Menú desplegable con la opción de copiar estilos.]({% image_buster /assets/img_archive/dnd_iam_copypaste_styles.png %}){: style="float:right;margin-left:15px;max-width:35%"}

1. Con el elemento seleccionado, haz clic en <i class="fas fa-paintbrush" title="Copiar o pegar estilos"></i> **Copy or paste styles** junto al nombre del panel de propiedades (por ejemplo, si tienes un botón seleccionado, junto a "Button properties").
2. Haz clic en **Copy styles** y selecciona el elemento donde deseas aplicar el estilo copiado.
3. Haz clic en <i class="fas fa-paintbrush" title="Copiar o pegar estilos"></i> **Copy or paste styles** de nuevo y elige **Paste styles**.

#### Atajos de teclado {#keyboard-shortcuts}

También puedes usar atajos de teclado para copiar y pegar estilos:

| Acción | Mac | Windows |
| ------------ | ---------------------------------------------- | ------------------------------------------------- |
| Copiar estilos | <kbd>⌘</kbd> + <kbd>Shift</kbd> + <kbd>c</kbd> | <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>c</kbd> |
| Pegar estilos | <kbd>⌘</kbd> + <kbd>Shift</kbd> + <kbd>v</kbd> | <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>v</kbd> |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Atajos de teclado" }