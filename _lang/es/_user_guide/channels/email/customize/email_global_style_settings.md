---
nav_title: "Configuración global de estilos de correo electrónico"
article_title: "Configuración global de estilos de correo electrónico"
alias: "/dnd/global_style_settings/"
channel: email
page_order: 3
description: "Este artículo de referencia explica cómo configurar los estilos globales de correo electrónico en el editor de arrastrar y soltar para tus Campaigns y Canvas."
tool:
  - Campaigns
  - Canvas
---

# Configuración global de estilos de correo electrónico {#email-global-style-settings}

> Con la configuración global de estilos, puedes personalizar la apariencia de tus campañas de correo electrónico y Canvas. Puedes añadir y personalizar un tema predeterminado para tu editor de arrastrar y soltar. Esto incluye editar tus estilos para títulos de correo electrónico, texto, botones y más. Usar una combinación de estos ajustes puede ayudarte a crear una apariencia consistente en toda tu mensajería de correo electrónico.

Para editar tu configuración global de estilos, ve a **Configuración** > **Preferencias de correo electrónico** > **Preferencias de correo electrónico de arrastrar y soltar**. Después de editar los estilos en el editor de correo electrónico de arrastrar y soltar, selecciona **Guardar**. Para personalizar aún más tus campañas de correo electrónico y Canvas, consulta cómo puedes incorporar [bloques del editor (correo electrónico)]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=email).

![Sección de configuración global de estilos de correo electrónico en la pestaña de configuración del editor de correo electrónico de arrastrar y soltar.]({% image_buster /assets/img_archive/dnd_global_style_settings.png %})

{% alert note %}
Las actualizaciones realizadas en la configuración global de estilos se aplicarán a todas las campañas de correo electrónico y Canvas futuros.
{% endalert %}

## Estilo básico {#basic-styling}

En **Estilo básico**, puedes configurar los colores predeterminados del fondo del correo electrónico y del contenido para tus Campaigns y Canvas de correo electrónico. También puedes seleccionar una fuente predeterminada, añadir una fuente personalizada y editar los colores de los enlaces.

![Opciones de estilo básico que incluyen opciones para editar los colores de fondo del correo electrónico y del contenido, el nombre de fuente predeterminado y el color de enlace predeterminado.]({% image_buster /assets/img_archive/dnd_basic_styling.png %})

## Fuente personalizada {#custom-font}

Con las fuentes personalizadas, puedes añadir manualmente una fuente web para mantener la coherencia de marca en diversas plataformas de correo electrónico. Puedes añadir una fuente personalizada para cada sección de estilo.

{% alert note %}
Cualquier configuración de font-weight en el CSS se ignora. En su lugar, selecciona uno de los pesos predeterminados al redactar el mensaje.
{% endalert %}

### Requisitos {#requirements}

Antes de añadir una fuente personalizada, verifica que el archivo de fuente personalizada cumpla con los siguientes requisitos:

- CORS debe estar habilitado en el servidor que proporciona el archivo de fuente personalizada. Esto normalmente lo gestiona tu equipo de TI.
  - El archivo de fuente personalizada debe tener el encabezado: `Access-Control-Allow-Origin: *`
- La URL del archivo debe apuntar a un archivo CSS (no WOFF ni OTF).
- El nombre de la fuente personalizada debe coincidir con el nombre del font face en el archivo CSS.

{% alert important %}
El proveedor de fuentes personalizadas puede recopilar datos personales de tus destinatarios. Debes revisar las políticas de tu proveedor de fuentes antes de usarlo.
{% endalert %}

### Añadir una fuente personalizada {#adding-a-custom-font}

Para añadir una fuente personalizada, haz lo siguiente:

1. En la sección **Default Font Name** de **Basic Styling**, selecciona **Add a custom font**.
2. En el campo **Font Name**, introduce el mismo nombre de fuente que aparece en tu archivo de origen de fuente personalizada. Asegúrate de que el nombre esté correctamente escrito en mayúsculas y con el espaciado adecuado.
3. Introduce la URL correspondiente en el campo **Font URL**.
4. Verifica que la vista previa muestre tu fuente personalizada.
5. Selecciona **Save** para usar la fuente personalizada como tu fuente de correo electrónico predeterminada.

{% alert important %}
Gmail no admite fuentes personalizadas, por lo que tu fuente personalizada puede mostrarse como una fuente del sistema predeterminada. Para otras plataformas de correo electrónico, verifica que tu fuente personalizada se muestre correctamente antes de enviar tu mensajería de correo electrónico.
{% endalert %}

Para usar otras fuentes personalizadas en tus Campaigns de correo electrónico, puedes crear una [plantilla de correo electrónico]({{site.baseurl}}/user_guide/messaging/templates/email_templates/email_template) o [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks) que incluya la fuente personalizada. Por ejemplo, puedes crear una plantilla de correo electrónico específica diseñada con fuentes personalizadas festivas adaptadas a la temática de tu promoción. Asegúrate de verificar que la fuente elegida sea segura para la web y compatible con tus plataformas de correo electrónico.

### Fuente alternativa {#fallback-font}

Las fuentes alternativas se usan para el título, el encabezado y el cuerpo del texto cuando tu fuente predeterminada no es compatible con el proveedor de buzón de entrada o el sistema operativo. De forma predeterminada, Braze establece automáticamente Arial como fuente alternativa cuando se guardan los ajustes de estilo global. También tienes la opción de añadir serif o sans serif como opciones para tu familia de fuentes predeterminada.

![Un ejemplo de "Arial" como fuente alternativa con "Sans-serif" como familia de fuentes.]({% image_buster /assets/img_archive/dnd_fallbacks.png %})

Puedes añadir hasta 17 fuentes alternativas. La primera fuente alternativa seleccionada será la que se intente usar primero. La fuente alternativa solo se aplicará a plantillas, Campaigns de correo electrónico y componentes de Canvas recién creados. La fuente alternativa no se establece automáticamente para los mensajes que se crearon antes de que se especificara la fuente alternativa. Recomendamos encarecidamente seleccionar fuentes alternativas que sean similares a tu mensajería de correo electrónico para mantener la coherencia de tu marca.

## Estilo de los títulos {#title-styling}

Aquí puedes ajustar los estilos de los títulos de tu correo electrónico editando el tamaño de fuente, el color de fuente y la alineación del texto.

![Configuración de estilo de títulos con un encabezado principal y un encabezado secundario alineados al centro.]({% image_buster /assets/img_archive/dnd_title_styling.png %})

Opcionalmente, puedes sobrescribir el estilo predeterminado del tema de tu editor de arrastrar y soltar. Selecciona **Sobrescribir estilo predeterminado** para aplicar tu elección de estilo de título. Esto puede incluir configurar una fuente y un color de enlace diferentes.

## Estilo de párrafo {#paragraph-styling}

Para establecer un estilo de párrafo predeterminado, ve a **Paragraph Styling**, introduce el **Font Size** y selecciona **Font Color** para elegir un color de fuente. También puedes ajustar el estilo del bloque para el cuerpo del texto editando los valores de **Padding Top**, **Padding Right**, **Padding Bottom** y **Padding Left**. Esto se aplicará al espaciado alrededor de las cuatro áreas que rodean el bloque de párrafo.

![Configuración de estilo de párrafo para texto con fuente de 14 pt.]({% image_buster /assets/img_archive/dnd_paragraph_styling.png %})

## Estilo de listas {#list-styling}

Al añadir listas a tus mensajes, la sección **List Styling** crea consistencia en la forma en que se diseñan tus listas. Esto incluye detalles como:

- Tamaño de fuente
- Color de fuente
- Peso de fuente
- Altura de línea
- Alineación
- Dirección del texto
- Espaciado entre letras
- Espaciado entre elementos de la lista
- Sangría de elementos de la lista
- Tipo de lista
- Estilo del tipo de lista

Puedes configurar el **List Type** para que sea numerado o con viñetas. El **List Style Type** ofrece personalización adicional para el estilo de tus listas. Por ejemplo, puedes configurar los tipos de lista para que siempre tengan viñetas y que cada viñeta sea un cuadrado.

![Configuración de estilo de lista para una lista con viñetas.]({% image_buster /assets/img_archive/dnd_list_styling.png %})

## Estilo de los botones {#button-styling}

En la sección **Estilo de los botones**, puedes editar los siguientes estilos predeterminados para el botón:
- Color de fondo
- Tamaño de fuente
- Color de fuente
- Radio del borde
- Color del borde
- Grosor del borde
- Relleno del botón

![Configuración de estilo de los botones para un botón rectangular con fondo azul.]({% image_buster /assets/img_archive/dnd_button_styling.png %})

Al igual que con todas las demás secciones de estilo, puedes ajustar el estilo del bloque editando los valores de **Relleno superior**, **Relleno derecho**, **Relleno inferior** y **Relleno izquierdo**.

## Ancho de la plantilla de correo electrónico {#email-template-width}

Usando el ancho de la plantilla de correo electrónico, puedes ajustar y establecer un ancho para mantener la consistencia en tus Campaigns de correo electrónico.

![Ancho de la plantilla de correo electrónico establecido en 600px.]({% image_buster /assets/img_archive/dnd_email_template_width.png %})

## Ancho de Content Blocks {#content-block-width}

Esta configuración vendrá preconfigurada para todos los Content Blocks futuros. Los Content Blocks existentes no se actualizarán. Puedes configurar todos los Content Blocks para que se establezcan al 100%, ajustándose al ancho donde se inserta un Content Block, o definir un valor específico en píxeles.

Recomendamos que el ancho del Content Block coincida con el ancho de la plantilla de correo electrónico.

![Ancho de Content Block establecido en 600 px.]({% image_buster /assets/img_archive/dnd_content_block_width_update.png %})