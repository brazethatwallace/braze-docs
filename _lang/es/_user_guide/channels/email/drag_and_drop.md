---
nav_title: Editor de arrastrar y soltar
article_title: Crear un correo electrónico con arrastrar y soltar
alias: /dnd/
page_order: 1
description: "Este artículo explica cómo configurar y usar correctamente el editor de arrastrar y soltar para mensajes de correo electrónico."
channel: email
tool:
- Campaigns
- Canvas
---

# Crear un correo electrónico con arrastrar y soltar {#create-an-email-with-drag-and-drop}

> Con el editor de arrastrar y soltar, puedes crear mensajes de correo electrónico completamente personalizados para Campaigns o Canvas, todo sin usar HTML para construir el cuerpo de tu correo electrónico.

## Acerca del editor {#about-the-editor}

El editor de arrastrar y soltar usa [Contenido](#content) y [Filas](#rows) como los dos componentes clave para simplificar tu flujo de trabajo, sin necesidad de usar HTML adicional.

<table aria-label="Acerca del editor" style="width: 100%; table-layout: fixed;">
    <caption>Componentes del editor: contenido y filas</caption>
    <thead>
    <tr>
        <th style="width: 50%;">Contenido</th>
        <th style="width: 50%;">Filas</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td style="text-align: center;">
            <img src="{% image_buster /assets/img/dnd/dnd_content.png %}" alt="La pestaña «Filas» que incluye diferentes combinaciones estructurales para el diseño de tu correo electrónico." style="max-width: 100%; height: auto;">
        </td>
        <td style="text-align: center;">
            <img src="{% image_buster /assets/img/dnd/dnd_rows.png %}" alt="La pestaña «Contenido» que incluye bloques básicos, multimedia y avanzados." style="max-width: 100%; height: auto;">
        </td>
    </tr>
    </tbody>
</table>
{: .reset-td-br-1 aria-label="Acerca del editor" }

### Contenido {#content}

**Contenido** incluye una serie de mosaicos que representan diferentes tipos de contenido que puedes usar en tu mensaje. Están organizados en tres categorías: básico, multimedia y avanzado.

{% tabs %}
{% tab Básico %}

Los bloques básicos son la base de tu correo electrónico. Con estos bloques, puedes añadir cualquiera de los siguientes elementos al cuerpo de tu correo electrónico:

- Título
- Párrafo
- Lista
- Botón
- Divisor
- Espaciador

{% endtab %}
{% tab Multimedia %}

Con los bloques multimedia, puedes añadir diferentes contenidos visuales como imágenes, videos, iconos y enlaces de redes sociales, e iconos personalizables.

{% endtab %}
{% tab Avanzado %}

Aunque el editor de arrastrar y soltar simplifica tu flujo de trabajo con estos bloques, también puedes usar bloques avanzados para insertar HTML o añadir un menú al cuerpo de tu correo electrónico. Ten en cuenta que usar tu propio HTML puede afectar cómo se renderiza el mensaje.

{% endtab %}
{% endtabs %}

### Filas {#rows}

Las **filas** son unidades estructurales que definen la composición horizontal de una sección del mensaje mediante columnas. Puedes usar filas vacías o [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks). Usar más de una columna te permite colocar diferentes elementos de contenido uno al lado del otro. De esta manera, puedes añadir todos los elementos estructurales que necesites a tu mensaje, independientemente de la plantilla que hayas seleccionado al comenzar.

#### Anidar imágenes dentro de bloques de texto {#nesting-images-inside-text-blocks}

No puedes anidar una imagen dentro de un párrafo u otro bloque de texto en el editor de arrastrar y soltar. Para colocar una imagen al lado o dentro de un diseño de texto, usa columnas en una **fila**: por ejemplo, una fila de varias columnas en escritorio con **Hide on mobile** para esa fila, y una fila separada solo para móvil (con **Hide on desktop** y **Do not stack on mobile** según sea necesario) para que la imagen y el texto se alineen correctamente en pantallas pequeñas.

#### Estilo de tarjetas {#cards-style}

**Estilo de tarjetas** es una propiedad de fila que te permite añadir espaciado entre columnas y redondear sus esquinas. Con el formato de estilo de tarjetas, puedes crear diseños más atractivos visualmente para destacar tu contenido más importante, como nuevas características de productos, testimonios, ofertas especiales, novedades y más.

## Uso del editor de arrastrar y soltar {#using-the-drag-and-drop-editor}

¿No tienes claro si tu mensaje de correo electrónico debe enviarse mediante una Campaign o un Canvas? Las Campaigns son mejores para envíos de mensajería únicos y dirigidos, mientras que los Canvas son mejores para recorridos de usuario de varios pasos.

{% alert note %}
No puedes guardar un correo electrónico de arrastrar y soltar desde una Campaign o Canvas directamente en **Templates** > **Email Templates** como una plantilla de correo electrónico. Primero construye en **Templates**, o consulta [¿Puedo guardar mi correo electrónico de arrastrar y soltar como plantilla después de construirlo dentro de mi Campaign o Canvas?]({{site.baseurl}}/user_guide/channels/email/drag_and_drop/faq#can-i-save-my-drag-and-drop-email-as-a-template-after-i-build-it-within-my-campaign-or-canvas) para recrear una plantilla de arrastrar y soltar o exportar HTML con **Download file**.
{% endalert %}

Una vez que hayas seleccionado dónde construir tu mensaje, veamos los pasos para crear un correo electrónico con arrastrar y soltar.

### Paso 1: Selecciona tu plantilla {#step-1-select-your-template}

Después de seleccionar el editor de arrastrar y soltar como tu experiencia de edición, puedes elegir:

- Comenzar con una plantilla en blanco.
- Usar una plantilla de correo electrónico de arrastrar y soltar prediseñada de Braze.
- Usar una plantilla de correo electrónico de arrastrar y soltar guardada.

{% alert note %}
Para usar una plantilla HTML personalizada existente o plantillas creadas por terceros, debes recrear la plantilla yendo a **Content** > **Email** y seleccionando **Drag-And-Drop Editor** como tu experiencia de edición.
{% endalert %}

También puedes acceder a todas las plantillas desde la sección **Templates**.

Después de seleccionar tu plantilla, verás un resumen de tu correo electrónico en **Email Variants** que incluye la información de envío y el cuerpo del correo electrónico.

Luego, selecciona **Edit Email Body** para comenzar a diseñar la estructura del correo electrónico en el editor de arrastrar y soltar.

![La sección «Email Variants» con un ejemplo de cuerpo de correo electrónico.]({% image_buster /assets/img/dnd/dnd_emailvariant.png %})

### Paso 2: Construye tu correo electrónico {#step-2-build-your-email}

La experiencia de edición de arrastrar y soltar se divide en tres secciones: **Sending Settings**, **Content** y **Preview & Test**. La magia de construir el cuerpo de tu correo electrónico ocurre en la sección **Content**. Antes de construir tu correo electrónico, es importante entender los componentes clave que guían tu experiencia de creación de correos electrónicos. Si necesitas repasar, consulta [Acerca del editor](#about-the-editor).

Cuando estés listo, usa los bloques de contenido de arrastrar y soltar para construir tu correo electrónico.

1. Selecciona el panel **Rows**. Arrastra y suelta las configuraciones de filas en el editor principal. Esto definirá el diseño del contenido de tu correo electrónico.
   - Ten en cuenta que las nuevas configuraciones deben arrastrarse a la parte superior o inferior de una sección existente.
   - Cuando selecciones una configuración de fila, aparecerán los ajustes de **Row Properties** para una mayor personalización de los colores de fondo de la fila, imágenes y tamaños de columna personalizados.
2. Selecciona el panel **Content**. Arrastra y suelta los mosaicos de contenido deseados en los componentes de fila.
   - También puedes arrastrar cualquiera de los mosaicos de **Content** al editor principal. Esto crea una fila para el mosaico.
   - Puedes refinar aún más el mosaico seleccionándolo y ajustando los campos en **Content Properties** y **Block Options**. Esto incluye editar el espaciado entre letras, el relleno, la altura de línea y más.

Consulta [Otras personalizaciones](#other-customizations) para conocer otras formas de personalizar aún más tu correo electrónico de arrastrar y soltar.

A medida que construyes tu correo electrónico, puedes alternar entre una vista de escritorio y una vista móvil para previsualizar cómo se verá tu mensaje de correo electrónico para tus grupos de usuarios. Esto verificará que tu contenido sea responsivo, y puedes hacer los ajustes necesarios sobre la marcha.

{% alert tip %}
¿Necesitas ayuda para crear textos increíbles? Prueba usar el [asistente de redacción con inteligencia artificial]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#generate-copy). Introduce un nombre o descripción de producto, y la IA generará textos de marketing similares a los escritos por humanos para usar en tu mensajería.

![Botón del asistente de redacción, ubicado en el panel de contenido junto a la configuración de estilo en el editor de arrastrar y soltar.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_dnd.png %})
{% endalert %}

### Paso 3: Añade tu información de envío {#step-3-add-your-sending-information}

Una vez que hayas terminado de diseñar y construir tu mensaje de correo electrónico, es hora de añadir tu información de envío en la sección **Sending Settings**.

1. En **Sending Info**, selecciona un correo electrónico como **From Display Name + Address**. También puedes personalizar esto seleccionando **Customize From Display Name + Address**.
2. Selecciona un correo electrónico como **Reply-To Address**. También puedes personalizar esto seleccionando **Customize Reply-To Address**.
3. A continuación, selecciona un correo electrónico como **BCC Address** para hacer tu correo electrónico visible para esta dirección.
4. Añade una línea del asunto a tu correo electrónico. Opcionalmente, también puedes añadir un preencabezado y un espacio en blanco después del preencabezado.

{% multi_lang_include alerts/tip_alerts.md alert='Liquid email display name and reply-to address' %}

Una vista previa en el panel derecho se completará con la información de envío que hayas añadido. Esta información también se puede actualizar navegando a **Settings** > **Email Preferences** > **Sending Configuration**.

#### Añadir archivos adjuntos al correo electrónico {#add-email-attachments}

En **Sending Settings** > **Advanced**, puedes añadir archivos adjuntos al correo electrónico mediante los siguientes métodos:

- **Cargar un archivo:** Arrastra y suelta o examina para cargar un archivo directamente desde tu computadora al correo electrónico. Braze valida el tipo y tamaño del archivo (hasta 2&nbsp;MB de forma predeterminada) antes de cargarlo, y luego estos archivos se cargan en la biblioteca de medios. Los archivos que superen el límite de 2&nbsp;MB no se pueden cargar.
- **Usar la biblioteca de medios:** Examina y selecciona entre los activos ya almacenados en la [biblioteca de medios]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library). Se admiten archivos PDF, documentos de Word, archivos de Excel y presentaciones de PowerPoint.
- **Añadir desde URL:** Introduce una URL que apunte al archivo y proporciona un nombre de archivo para mostrar. Dado que Braze no puede verificar el tamaño de URL arbitrarias durante la composición del correo electrónico, el tamaño del archivo se aplica en el momento del envío. Ten en cuenta que Liquid no es compatible en este campo.

Consulta las [Directrices de correo electrónico]({{site.baseurl}}/user_guide/channels/email/best_practices/email_guidelines) para conocer las mejores prácticas específicas a considerar.

#### Personalizar el encabezado de tu correo electrónico (avanzado) {#personalize-your-email-header-advanced}

En **Sending Settings**, puedes añadir personalización para los encabezados del correo electrónico y extras del correo electrónico, lo que te permite enviar datos adicionales a otros proveedores de servicios de correo electrónico. Personalizar un encabezado de correo electrónico, como incluir el nombre del destinatario, también puede contribuir a la probabilidad de que tu correo electrónico sea abierto.

{% alert note %}
La funcionalidad avanzada aparecerá en el creador de la Campaign o Canvas. En la funcionalidad avanzada, puedes modificar tu configuración de CSS en línea e introducir un encabezado o pares clave-valor adicionales (si están configurados).
{% endalert %}

### Paso 4: Prueba tu correo electrónico {#step-4-test-your-email}

Después de añadir tu información de envío, es hora de probar finalmente tu correo electrónico.

{% alert tip %}
Si el correo electrónico se ve diferente en el editor que en la vista previa o el envío de prueba, confirma que todas las etiquetas estén cerradas, los atributos de imagen tengan valores y las imágenes de fondo no estén borrosas en los bordes.
{% endalert %}

Ve a la sección **Preview and Test**. Aquí tienes la opción de previsualizar tu correo electrónico como un usuario o enviar un mensaje de prueba. Esta sección también incluye [Inbox Vision]({{site.baseurl}}/user_guide/channels/email/inbox_vision), que te permite verificar que tu correo electrónico se haya renderizado correctamente en diferentes clientes móviles y web.

{% alert tip %}
También puedes usar el interruptor **Dark Mode Preview** en el panel de vista previa para ver el cuerpo de tu correo electrónico en modo oscuro y ajustar tu correo electrónico según sea necesario.
{% endalert %}

Dado que puedes ver tres versiones diferentes del mismo correo electrónico en el editor real, en Inbox Vision y como un correo electrónico de prueba real, es importante alinear los detalles en todas tus plataformas.

#### Vista previa y envío de prueba {#preview-and-test-send}

Bajo la pestaña **Preview as a User**, puedes seleccionar los siguientes tipos de usuario para previsualizar tu mensaje.

- **Random User:** Braze seleccionará aleatoriamente un usuario de la base de datos y previsualizará el correo electrónico basándose en sus atributos o información de eventos.
- **Select User:** Puedes seleccionar un usuario específico basándote en su dirección de correo electrónico o ID externo. El correo electrónico se previsualizará basándose en los atributos e información de eventos de ese usuario.
- **Custom User:** Puedes personalizar un usuario. Braze ofrecerá campos de entrada para todos los atributos y eventos disponibles. Puedes introducir cualquier información que desees ver en el correo electrónico de vista previa.

{% alert note %}
El usuario aleatorio puede o no ser parte de tus criterios de segmentación. La segmentación se selecciona después, por lo que Braze no conoce tu público objetivo en este punto.
{% endalert %}

También puedes seleccionar **Copy preview link** para generar y copiar un enlace de vista previa compartible que muestre cómo se verá el correo electrónico para un usuario aleatorio. El enlace durará siete días antes de que necesite ser regenerado.

Ten en cuenta que cualquier edición realizada en una plantilla de correo electrónico no se reflejará en un enlace generado previamente. Necesitarás generar un nuevo enlace de vista previa para ver cualquier edición.

![Vista previa de correo electrónico con un botón para «Copy preview link» y copiar el enlace generado.]({% image_buster /assets/img/dnd_email_link_preview.png %})

#### Usar Inbox Vision {#use-inbox-vision}

Inbox Vision te permite ver tus campañas de correo electrónico desde la perspectiva de los clientes de correo electrónico y dispositivos móviles. Para probar tu mensaje de correo electrónico usando Inbox Vision, selecciona **Inbox Vision** en la sección **Preview & Test** y selecciona **Run Inbox Vision**.

Es importante probar y verificar los detalles más finos de tu mensaje de correo electrónico. Por ejemplo, las imágenes de fondo en los mensajes de correo electrónico a veces pueden causar que aparezcan líneas blancas o desconexiones entre imágenes, o clientes como Windows Outlook pueden no mostrar imágenes de fondo. Usar Inbox Vision puede ayudar a identificar estas discrepancias entre clientes. En este escenario, establece un color de fondo alternativo para que estas imágenes se rendericen como se espera.

Para más información, consulta [Enviar mensajes de prueba]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=email).

Después de usar el editor de arrastrar y soltar para diseñar y crear tu mensaje de correo electrónico, continúa [construyendo]({{site.baseurl}}/user_guide/channels/email/html_editor#step-4-build-the-remainder-of-your-campaign-or-canvas) el resto de tu Campaign o Canvas.

{% details Acerca del motor HTML actualizado %}
El motor subyacente que produce HTML a partir del editor de arrastrar y soltar ha sido optimizado y actualizado, lo que resulta en beneficios relacionados con la compresión de archivos HTML y el renderizado.

El tamaño promedio de los datos HTML exportados se ha reducido, lo que lleva a una carga y renderizado más rápidos, menor recorte en dispositivos móviles y menor consumo de ancho de banda.

El renderizado HTML ha mejorado gracias a las siguientes actualizaciones que minimizan el número de comentarios condicionales y consultas de medios CSS. Como resultado, los archivos HTML son más pequeños y están codificados de manera más eficiente.
- Migración de un diseño basado en elementos `<div>` a una base de código con formato estándar `<table aria-label="Usar Inbox Vision">`
  <caption>Usar Inbox Vision</caption>
- Los [bloques de editor (correo electrónico)]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=email) han sido recodificados para mayor concisión
- El código HTML final se comprime para eliminar espacios en blanco entre etiquetas
- Los divisores transparentes se convierten automáticamente en relleno de contenido
{% enddetails %}

## Otras personalizaciones {#other-customizations}

A medida que continúas construyendo correos electrónicos de arrastrar y soltar, puedes personalizar aún más cada cuerpo de correo electrónico usando una combinación de estos detalles creativos para captar la atención e interés de tu audiencia en tu mensaje.

{% alert tip %}
Puedes crear un tema personalizado para tu editor de arrastrar y soltar usando la [configuración de estilo global]({{site.baseurl}}/user_guide/channels/email/customize/email_global_style_settings).
{% endalert %}

### Imágenes con ancho automático {#auto-width-images}

Las imágenes añadidas a tu correo electrónico se configurarán automáticamente en **Auto width**. Para ajustar esta configuración, desactiva **Auto width** y ajusta el porcentaje de ancho según sea necesario.

![Opción de ancho automático en la pestaña Contenido del editor de arrastrar y soltar.]({% image_buster /assets/img/dnd/dnd1.png %})

### Capas de color {#color-layering}

Usando capas de color, puedes cambiar el color del fondo del correo electrónico, el área de contenido y los diferentes componentes de contenido. El orden de color de adelante hacia atrás es: color del componente de contenido, color de fondo del área de contenido y color de fondo.

![Ejemplo de las capas de color en el editor de arrastrar y soltar.]({% image_buster /assets/img/dnd/dnd2.png %})

### Relleno de contenido {#content-padding}

![Opciones de bloque para el editor de arrastrar y soltar.]({% image_buster /assets/img/dnd/dnd3.png %}){: style="float:right;max-width:25%;margin-left:15px;"}

Para ajustar el relleno, desplázate hacia abajo hasta **Block Options** y selecciona **More Options**. Puedes ajustar con precisión tu relleno para que tu correo electrónico se vea perfecto.

### Fondo de contenido {#content-background}

Puedes añadir una imagen de fondo a la configuración de tu fila, lo que te permite incorporar más diseño y contenido visual en tu campaña de correo electrónico.

### Atributo de idioma {#language-attribute}

Puedes configurar el atributo de idioma yendo a la pestaña **Settings** y seleccionando el idioma deseado. También puedes apuntar al atributo de usuario {%raw%} `{{${language}}}` {%endraw%} si el mensaje está destinado a usuarios con valores de idioma dinámicos.

![Configuración del valor de «Idioma» para un correo electrónico.]({% image_buster /assets/img/dnd/language_setting_dnd.png %}){: style="max-width:70%;"}

### Personalización {#personalization}

![Opciones para añadir personalización en el editor de arrastrar y soltar.]({% image_buster /assets/img/dnd/dnd4.png %}){: style="float:right;max-width:25%;margin-left:15px;"}

Liquid básico es compatible con el editor de correo electrónico de arrastrar y soltar. Para añadir personalización a tu correo electrónico:

1. Selecciona **Personalization** en la sección **Content**.
2. Selecciona el tipo de personalización. Esto incluye atributos predeterminados (estándar), atributos de dispositivo, atributos personalizados y más.
3. Busca el atributo que deseas añadir.
4. Copia el fragmento de código Liquid generado y pégalo en el cuerpo de tu correo electrónico.

La personalización con Liquid no es compatible con los bloques de imagen ni con los campos de tipo de enlace de botón.

#### Imágenes dinámicas {#dynamic-images}

Puedes elegir incluir imágenes dinámicas en tu mensajería de correo electrónico incluyendo [contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content) o [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) en el atributo de origen de tu imagen. Por ejemplo, en lugar de una imagen estática, puedes insertar {% raw %} `https://example.com/images/?imageBanner={{first_name}}` {% endraw %} como la URL de la imagen para incluir el nombre del usuario en la imagen. Esto ayuda a personalizar tus correos electrónicos para cada usuario.

{% alert important %}
La URL de tu imagen debe comenzar con `https://`. Usar `http://` provoca un fallo en tu aplicación.
{% endalert %}

### Dirección del texto {#text-direction}

Al redactar tu mensaje, puedes alternar la dirección del texto entre izquierda a derecha y derecha a izquierda seleccionando el botón correspondiente de **Text direction**. Puedes usar esta opción al crear mensajes en idiomas como árabe y hebreo.

![Menú del editor de arrastrar y soltar de correo electrónico con botón para alternar la alineación del texto entre derecha a izquierda e izquierda a derecha.]({% image_buster /assets/img/dnd/dnd_template1.png %}){: style="max-width:50%;"}

La apariencia final de los mensajes de derecha a izquierda depende en gran medida de cómo los proveedores de servicios los renderizan. Para conocer las mejores prácticas sobre cómo crear mensajes de derecha a izquierda que se muestren con la mayor precisión posible, consulta [Crear mensajes de derecha a izquierda]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages).

### HTML

#### Atributos HTML para enlaces {#html-attributes-to-links}

![La sección «Atributos» con el atributo «clicktracking» desactivado para un enlace.]({% image_buster /assets/img/dnd_custom_attributes.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Al usar enlaces, botones, imágenes y videos en el editor de arrastrar y soltar, selecciona **Add new attribute** en **Attributes** en la sección **Content** para añadir información adicional a las etiquetas HTML en los correos electrónicos. Esto puede ser especialmente útil para la personalización de mensajes, la segmentación y el estilo.

Un caso de uso común es insertar un atributo en tu etiqueta de anclaje para desactivar el seguimiento de clics al enviar a través de Braze.

* **SendGrid:** `clicktracking = "off"`
* **SparkPost:** `data-msys-clicktrack = "0"`

Otro caso de uso común es marcar enlaces específicos como enlaces universales. Los enlaces universales son enlaces que redirigen a tu aplicación, brindando a tus usuarios una experiencia integrada.

* **SendGrid:** `universal = "true"`
* **SparkPost:** `data-msys-sublink = "open-in-app"` (se debe configurar una [subruta personalizada](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve#custom-link-sub-paths))

Para configurar enlaces universales, consulta [Enlaces universales y App Links]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links).

Alternativamente, puedes integrarte con uno de nuestros partners de atribución, como [Branch]({{site.baseurl}}/partners/message_orchestration/deeplinking/branch_for_deeplinking) o [AppsFlyer]({{site.baseurl}}/partners/message_orchestration/attribution/appsflyer/appsflyer#email-deep-linking-and-click-tracking), para gestionar enlaces universales.

Por último, hay atributos predefinidos disponibles para ayudar a que tu mensaje sea accesible. Obtén más información en nuestro artículo dedicado [Crear mensajes accesibles en Braze]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/accessibility).

#### Etiquetas head personalizadas {#custom-head-tags}

Usa etiquetas `<head>` para añadir CSS y metadatos en tu mensaje de correo electrónico. Por ejemplo, puedes usar estas etiquetas para añadir una hoja de estilos o un favicon. Liquid es compatible con las etiquetas `<head>`.

Todo lo que se añada fuera de las etiquetas `<head>` se añadirá después de la etiqueta `<body>` en tu correo electrónico. Esto significa que el contenido añadido se mostrará en el correo electrónico.

##### Etiquetas y atributos permitidos por etiqueta {#allowed-tags-and-attributes-by-tag}

| Nombre de etiqueta | Descripción | Ejemplo |
| --- | --- | --- |
| `base` | Especifica la URL base para todas las URL relativas en el mensaje. | `<base href="https://example.com" target="_blank">` |
| `link`| Define relaciones entre el mensaje y recursos externos. | `<link href="styles.css" rel="stylesheet" type="text/css">` |
| `meta` | Proporciona metadatos como la descripción de la página o palabras clave. | `<meta name="description" content="Free Web tutorials">` |
| `style` | Incorpora estilos CSS internos. | `<style type="text/css" media="screen">body { font-size: 16px; }</style>` |
| `title` | Establece el título del documento que se muestra en las pestañas del navegador. | `<title>StyleRyde</title>` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Etiquetas y atributos permitidos por etiqueta" }

| Etiqueta | Atributo | Descripción | Ejemplo |
| --- | --- | --- | --- |
| `base` | `href` | URL base a usar para las URL relativas. | ```<base href="https://braze.com">``` |
| `base` | `target`| Destino predeterminado para todos los hipervínculos y formularios. | ```<base target="_blank">``` |
| `link` | `href` | URL del recurso externo. | ```<link href="style.css">``` |
| `link` | `rel` | Define relaciones entre el mensaje actual y el enlazado. | ```<link rel="stylesheet">``` |
| `link` | `type` | Tipo de recurso enlazado. | ```<link type="text/css">``` |
| `link` | `sizes` | Especifica los tamaños de los iconos. | ```<link rel="icon" sizes="32x32" href="favicon-32.png">``` |
| `link` | `media` | Especifica el medio o dispositivo para el que se aplican los estilos. | ```<link rel="stylesheet" media="screen" href="style.css">``` |
| `meta` | `name` | Establece el título del documento que se muestra en las pestañas del navegador. | ```<meta name="viewport" content="width=device-width, initial-scale=1">``` |
| `meta` | `content` | Establece el título del documento que se muestra en las pestañas del navegador. | ```<meta name="description" content="Page about our newest products">``` |
| `meta` | `charset` | Declara la codificación de caracteres. | ```<meta charset="UTF-8">``` |
| `meta` | `property` | Establece el título del documento que se muestra en las pestañas del navegador. | ```<meta property="og:title" content="Website title">``` |
| `style` | `type` | Tipo MIME del contenido de estilo. | {% raw %}```<style type="text/css">p { color: red; }</style>```{% endraw %} |
| `style` | `media` | Especifica el medio o dispositivo para el que se aplican los estilos. | ```<style media="print">body { font-size: 12pt; }</style>``` |
| `title` | Sin atributos | La etiqueta `title` no acepta ningún atributo. | ```<title>Kitchenerie</title>``` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Etiquetas y atributos permitidos por etiqueta" }

{% alert note %}
Los nombres de los enlaces pueden tener hasta 63 bytes y se truncan automáticamente si exceden el límite.
{% endalert %}