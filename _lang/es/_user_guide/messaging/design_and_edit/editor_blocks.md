---
nav_title: Bloques de editor
article_title: Bloques de editor de arrastrar y soltar
alias: "/dnd/editor_blocks/"
channel:
- email
- in-app messages
- landing pages
- banners
- preference center
page_order: 3
page_type: reference
description: "Este artículo de referencia cubre los bloques de editor en el editor de arrastrar y soltar para correo electrónico, mensajes dentro de la aplicación, páginas de destino, Banners y centros de preferencias de correo electrónico de arrastrar y soltar."
tool: Media
---

# Bloques de editor de arrastrar y soltar {#drag-and-drop-editor-blocks}

> Los bloques de editor son las piezas que arrastras a las filas y columnas en el editor de arrastrar y soltar.

Selecciona el editor que estás usando:

{% sdktabs %}

{% sdktab email %}
## Bloques de editor de correo electrónico {#email-editor-blocks}

Los bloques de editor se encuentran en la sección **Contenido** para mensajes de correo electrónico. Arrastra un bloque dentro de una columna en el **editor de arrastrar y soltar**; se ajusta automáticamente al ancho de la columna.

Para más información sobre cómo crear correos electrónicos en el **editor de arrastrar y soltar**, consulta [Crear un correo electrónico con arrastrar y soltar]({{site.baseurl}}/user_guide/channels/email/drag_and_drop) y <a href="{{site.baseurl}}/user_guide/channels/email/drag_and_drop/#other-customizations">Otras personalizaciones</a> en ese artículo.

{% alert tip %}
También puedes añadir [atributos personalizados]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes) a cualquier URL dentro de los bloques de editor `Image`, `Button` o `Text`.
{% endalert %}

### Título {#title}

Añade texto para encabezados dentro del correo electrónico.

| Propiedad | Descripción |
|---|---|
| Título | Selecciona el estilo de encabezado. |
| Familia tipográfica | El estilo de fuente para tu título. |
| Peso de fuente | El grosor general de la fuente. |
| Tamaño de fuente | Determina el tamaño de tu texto. |
| Color de texto | Modifica el color del título. |
| Color de enlace | Modifica el color del enlace. |
| Alineación | Mueve el título para que esté orientado a la izquierda, al centro o a la derecha. |
| Altura de línea | Modifica la distancia entre líneas de texto. |
| Espaciado entre letras | Modifica la distancia entre cada carácter. |
| Dirección del texto | De izquierda a derecha por defecto, pero se puede editar para que sea [de derecha a izquierda]({{site.baseurl}}/right_to_left_messages). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Título" }

### Párrafo {#paragraph}

Introduce texto en el mensaje. Una barra de herramientas ayuda con la funcionalidad de edición de fuente y texto.

| Propiedad | Descripción |
|---|---|
| Familia tipográfica | El estilo de fuente para el texto de tu párrafo. |
| Peso de fuente | El grosor general de la fuente. |
| Tamaño de fuente | Determina el tamaño de tu texto. |
| Color de texto | Modifica el color del texto. |
| Color de enlace | Modifica el color del enlace. |
| Alineación | Mueve el texto para que esté orientado a la izquierda, al centro o a la derecha. |
| Espaciado entre párrafos | Modifica el espacio entre párrafos. |
| Altura de línea | Modifica la distancia entre líneas de texto. |
| Espaciado entre letras | Modifica la distancia entre cada carácter. |
| Dirección del texto | De izquierda a derecha por defecto, pero se puede editar para que sea [de derecha a izquierda]({{site.baseurl}}/right_to_left_messages). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Párrafo" }

### Lista {#list}

Añade una lista con viñetas.

| Propiedad | Descripción |
|---|---|
| Tipo de lista | El tipo de lista. Puede ser con viñetas o numerada. |
| Estilo de lista | Determina el estilo de tu lista. |
| Iniciar lista desde | Determina el número inicial de tu lista. |
| Familia tipográfica | El estilo de fuente para el texto de tu párrafo. |
| Peso de fuente | El grosor general de la fuente. |
| Tamaño de fuente | Determina el tamaño de tu texto. |
| Color de texto | Modifica el color del texto. |
| Color de enlace | Modifica el color del enlace. |
| Alineación | Mueve el texto para que esté orientado a la izquierda, al centro o a la derecha. |
| Espaciado entre elementos | Modifica el espacio entre los elementos de la lista. |
| Sangría de elementos | Modifica la sangría de los elementos de la lista. |
| Altura de línea | Modifica la distancia entre líneas de texto. |
| Espaciado entre letras | Modifica la distancia entre cada carácter. |
| Dirección del texto | De izquierda a derecha por defecto, pero se puede editar para que sea [de derecha a izquierda]({{site.baseurl}}/right_to_left_messages). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Lista" }

### Botón {#button}

Añade un botón estándar. Las propiedades permiten editar el estilo y configurar el comportamiento del enlace.

| Propiedad | Descripción |
|---|---|
| Opciones de botón | Configura varias opciones del botón, como fuente, tamaño, ancho, color y relleno. |
| Botón al pasar el cursor | El estilo del botón cuando un usuario pasa el cursor sobre él con un ratón o trackpad. Incluye el color de fondo del botón, el color de fuente y los estilos de borde. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Botón" }

#### Comportamiento al hacer clic {#on-click-behavior}

| Propiedad | Descripción |
|---|---|
| Tipo de enlace | Determina la acción al hacer clic en el botón y establece el protocolo apropiado. |
| URL | Dinámico según el tipo de enlace **Abrir página web**. |
| Correo para, asunto y cuerpo | Para el tipo de enlace **Enviar correo electrónico**, establece la dirección de correo del destinatario, el asunto y el contenido que se rellenarán en un borrador de correo electrónico cuando el usuario seleccione el botón. |
| Tel | Para los tipos de enlace **Hacer llamada** y **Enviar SMS**, establece el número de teléfono al que el usuario llamará o enviará un mensaje de texto al seleccionar el botón. |
| Mensaje | Para el tipo de enlace **Enviar SMS**, establece el contenido que se rellenará en un borrador de mensaje SMS cuando el usuario seleccione el botón. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Comportamiento al hacer clic" }

### Divisor {#divider}

Inserta una línea sólida, punteada o discontinua para ayudar con el espaciado.

| Propiedad | Descripción |
|---|---|
| Transparente | Si está habilitado, se eliminan las opciones de línea y ancho. |
| Línea | Los diferentes formatos de línea, ya sea punteada, discontinua o sólida. También puedes modificar el grosor y el color de la línea divisora. |
| Ancho | Ajusta la extensión del divisor en incrementos de 5. |
| Alineación | Mueve la línea para que esté orientada a la izquierda, al centro o a la derecha. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Divisor" }

### Espaciador {#spacer}

Añade espacio o relleno entre otros bloques.

| Propiedad | Descripción |
|---|---|
| Altura | Ajusta la altura del bloque espaciador. El valor predeterminado es 60 px. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Espaciador" }

### Imagen {#image}

Inserta una imagen de la [biblioteca de medios]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library). Para imágenes dinámicas (imágenes con Liquid o contenido conectado), debes establecer una imagen alternativa para usar la configuración de ancho automático. Para las especificaciones de imagen, consulta [especificaciones de imagen de correo electrónico]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/image_specifications#email).

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

| Propiedad | Descripción |
|---|---|
| Ancho automático | Modifica el ancho de la imagen en píxeles. |
| Alineación | Establece la alineación de la imagen a la izquierda, al centro o a la derecha dentro del bloque. |
| Imagen con Liquid | Usa la lógica de [Liquid]({{site.baseurl}}/liquid) para establecer dinámicamente diferentes imágenes dentro del mismo bloque de contenido. |
| URL | Establece una imagen usando la dirección donde está alojada. |
| Texto alternativo | Una breve descripción de la imagen que proporciona a los usuarios la misma información que se muestra en la imagen. Esencial para la accesibilidad de lectores de pantalla o cuando la imagen no se carga. |
| Imagen con esquinas redondeadas | Renderiza la imagen con esquinas redondeadas. Por defecto, las imágenes se renderizan con esquinas cuadradas. |
| Acción | Desencadena una acción cuando el usuario hace clic en la imagen. |
| Opciones de bloque | Configura el relleno alrededor del bloque de imagen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Imagen" }

{% alert tip %}
Para **Ancho automático**, el redimensionamiento automático de imágenes elige el mejor tamaño para la imagen basándose en una combinación del ancho de la imagen y el espacio disponible en el diseño:
- Las imágenes más anchas que el espacio disponible se establecen al 100 % del ancho y mantienen esta proporción en dispositivos móviles, usando todo el ancho de pantalla del dispositivo.
- Las imágenes más pequeñas que el espacio disponible usan el tamaño natural de la imagen para evitar efectos de distorsión o imágenes borrosas.
{% endalert %}

#### Comportamiento del botón de descarga de Gmail {#gmail-download-button-behavior}

Gmail añade automáticamente un botón de descarga a las imágenes que no tienen un hipervínculo (`href`) asociado. Sin embargo, si la relación de aspecto de la imagen es de 299 x 524 px o menor, Gmail no mostrará el botón de descarga.

Para evitar que el botón de descarga aparezca en imágenes más grandes, puedes aplicar la solución alternativa del enlace "#":

1. Selecciona el bloque **Imagen**.
2. En el panel **Opciones de bloque**, ve a la sección **Enlace**.
3. Establece el **Tipo de enlace** en **Abrir página web**.
4. Introduce un signo de almohadilla (`#`) en el campo de entrada **URL**.

Añadir este enlace evita que Gmail muestre el botón de descarga sin afectar la experiencia del usuario.

### Video

Crea un enlace a contenido de video. Solo se admiten YouTube y Vimeo.

| Propiedad | Descripción |
|---|---|
| URL | La URL del video. |
| Título | Generado automáticamente a partir de los metadatos del video o se puede personalizar. |
| Estilo del icono de reproducción | Incluye diferentes opciones para el botón de reproducción ubicado en la parte superior de una imagen de video. |
| Color del icono de reproducción | Opción para seleccionar **Claro** u **Oscuro** para el botón de reproducción. |
| Tamaño del icono de reproducción | Elige el tamaño en píxeles para el botón de reproducción. Rango predefinido de 50&nbsp;px a 80&nbsp;px (incrementado en 5&nbsp;px). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Video" }

{% alert tip %}
Los videos alojados en Vimeo solo funcionan si están configurados como públicos. Todas las demás configuraciones de seguridad disponibles en Vimeo (por ejemplo, "Ocultar de Vimeo.com") generan un formato de enlace diferente que no es compatible con este Content Block. Estos tipos de enlaces son alterados por el constructor, lo que impide que Braze genere una miniatura.
{% endalert %}

### Redes sociales {#social}

Inserta iconos de plataformas de redes sociales. Puedes subir imágenes personalizadas para iconos específicos de marca.

| Propiedad | Descripción |
|---|---|
| Seleccionar colección de iconos | Establece el estilo de tu colección de iconos. |
| Configurar colección de iconos | Establece la URL para cada icono social. Incluye el interruptor **Más opciones** para editar el título y el texto alternativo. |
| Alineación | Mueve el icono social para que esté orientado a la izquierda, al centro o a la derecha. |
| Espaciado entre iconos | Determina el espaciado entre cada icono social. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Redes sociales" }

### Iconos {#icons}

Inserta un icono. Puedes subir imágenes personalizadas. Braze usa un icono de marcador de posición de gran tamaño hasta que subas una imagen.

| Propiedad | Descripción |
|---|---|
| Familia tipográfica | El estilo de fuente para el texto de tu párrafo. |
| Peso de fuente | El grosor general de la fuente. |
| Tamaño de fuente | Determina el tamaño de tu texto. |
| Color de texto | Modifica el color del título. |
| Color de enlace | Modifica el color del enlace. |
| Alineación | Mueve el icono para que esté orientado a la izquierda, al centro o a la derecha. |
| Espaciado entre letras | Modifica la distancia entre cada carácter. |
| Tamaño del icono | Determina el tamaño de tu icono. |
| Espaciado del icono | Modifica el espacio del icono. |
| Relleno del icono | Modifica el relleno del icono. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Iconos" }

### HTML

Inserta HTML sin procesar. Recomendado para [Liquid]({{site.baseurl}}/liquid), como contenido conectado o sentencias condicionales.

| Propiedad | Descripción |
|---|---|
| HTML | Añade o edita HTML sin procesar, incluyendo [Liquid]({{site.baseurl}}/liquid) para personalización o lógica condicional. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="HTML" }

### Menú {#menu}

Crea un menú flexible para el mensaje que estás diseñando.

| Propiedad | Descripción |
|---|---|
| Configurar elementos del menú | Añade un elemento de menú. |
| Familia tipográfica | El estilo de fuente para el menú. |
| Tamaño de fuente | El tamaño de tu menú. |
| Color de texto | Modifica el color del menú. |
| Color de enlace | Modifica el color del texto del menú. |
| Alineación | Mueve el menú para que esté orientado a la izquierda, al centro o a la derecha. |
| Espaciado entre letras | Modifica la distancia entre cada carácter. |
| Diseño | Determina el diseño, ya sea horizontal o vertical. |
| Separador | Añade carácter(es) entre las opciones del menú. |
| Menú móvil | Incluye opciones para modificar el tamaño del icono, el color y el tipo de icono cuando se muestra en un dispositivo móvil. |
| Relleno de elementos | Modifica el relleno usando el botón **+** o **-**, o introduciendo un número específico. |
| Todos los lados | Establece un número de relleno consistente si el relleno de elementos está deshabilitado. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Menú" }

### Producto {#product}

Renderiza filas de productos de un [catálogo de productos]({{site.baseurl}}/user_guide/messaging/design_and_edit/product_blocks), ya sea como elementos estáticos de una selección de catálogo (hasta 12) o como productos dinámicos impulsados por un [desencadenador de eCommerce de Canvas]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/ecommerce_use_cases) (hasta 24).

| Propiedad | Descripción |
| --- | --- |
| Tipo de contenido | Establece si los productos provienen de una **selección** fija del catálogo (**Estático**, hasta 12 productos) o de un desencadenador de recomendación de eCommerce de Canvas (**Dinámico**, hasta 24 productos). **Dinámico** solo está disponible en pasos de mensaje de Canvas. |
| Catálogo | Selecciona qué catálogo de productos proporciona los datos del producto y los mapeados de campos. |
| Selección | *(Solo estático)* Selecciona qué conjunto filtrado del catálogo define qué productos aparecen. |
| Mostrar detalles de origen | Alterna el texto de ayuda que muestra el catálogo subyacente o el campo de evento mapeado a cada campo de producto. |
| Imagen de variante | Muestra u oculta la imagen de variante para cada pieza de producto. |
| Título del producto | Muestra u oculta el título del producto para cada pieza. |
| Precio | Muestra u oculta el precio del producto. |
| Botón para URL del producto | Muestra u oculta un botón de llamada a la acción que enlaza a la URL del producto. |
| Cantidad | *(Dinámico, solo Canvas, cuando el desencadenador de entrada no es un evento de vista de producto)* Muestra u oculta la cantidad del producto del evento desencadenador. |
| Orientación del producto | Establece la posición de la imagen dentro de cada pieza: **Imagen a la izquierda**, **Imagen al centro** o **Imagen a la derecha**. |
| Alineación | Establece la alineación horizontal del contenido dentro de cada pieza. |
| Máximo de productos por fila | Establece cuántos productos aparecen por fila: **1**, **2** o **3** (**3** solo está disponible cuando la orientación es **Imagen al centro**). |
| Espaciado entre productos | Establece el espaciado entre productos: **Automático** o **Personalizado**. |
| Espaciado personalizado | *(Cuando se selecciona **Personalizado**)* Establece el espacio en píxeles entre productos. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Producto" }

## Personalización {#personalization}

Puedes añadir personalización a tu correo electrónico usando Liquid o contenido conectado.

- **Liquid:** En **Contenido** > **Personalización**, selecciona un atributo, copia el fragmento de código y pégalo en un bloque de título, párrafo o lista (Liquid básico) o en un bloque HTML (Liquid avanzado). En general, aunque puedes usar Liquid básico en bloques de título, párrafo y lista, recomendamos usar bloques HTML para lógica más compleja y así evitar problemas de diseño. Ten en cuenta que Liquid no es compatible en bloques de imagen ni en campos de URL de botones.
- **[Contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content):** Añade un bloque **HTML** y coloca tu llamada {% raw %}`{% connected_content %}`{% endraw %} allí.

{% endsdktab %}

{% sdktab in-app messages %}
## Bloques de editor de mensajes dentro de la aplicación {#in-app-message-editor-blocks}

Los bloques de editor se encuentran en la sección **Crear** para mensajes dentro de la aplicación. Arrastra un bloque a una columna; se ajusta automáticamente al ancho de la columna. Selecciona un bloque para editar su configuración en el panel del lado derecho.

Para más información sobre cómo crear mensajes dentro de la aplicación en el **editor de arrastrar y soltar**, consulta [Crear un mensaje dentro de la aplicación con arrastrar y soltar]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop).

### Título y párrafo {#title-and-paragraph}

Añade texto de título o párrafo al mensaje.

{% multi_lang_include drag_and_drop/editor_block_properties/title_paragraph.md %}

### Botón

Añade un botón estándar con estilo, enlaces y análisis configurables.

{% multi_lang_include drag_and_drop/editor_block_properties/button_properties.md %}

#### Comportamiento al hacer clic

{% multi_lang_include drag_and_drop/editor_block_properties/button_actions.md %}

### Botón de opción {#radio-button}

Añade una lista de opciones de las cuales los usuarios pueden seleccionar una. Al enviar, el perfil de usuario registra el [atributo personalizado]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes) asociado, que debe ser una cadena para guardarse. Los atributos personalizados con otros tipos de datos no se guardan en el perfil de usuario.

{% multi_lang_include drag_and_drop/editor_block_properties/radio_button_properties.md %}

### Imagen

Inserta una imagen de la [biblioteca de medios]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library).

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

{% multi_lang_include drag_and_drop/editor_block_properties/image_properties.md %}

Para las especificaciones de imagen, consulta nuestras [especificaciones de imagen de mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/image_specifications#in-app-messages).

#### Comportamiento al hacer clic

{% multi_lang_include drag_and_drop/editor_block_properties/image_actions.md %}

### Enlace {#link}

Inserta un hipervínculo en el que los usuarios pueden hacer clic para navegar a una URL especificada. Puede estar incrustado dentro del texto o ser independiente.

{% multi_lang_include drag_and_drop/editor_block_properties/link_properties.md %}

#### Comportamiento al hacer clic

{% multi_lang_include drag_and_drop/editor_block_properties/link_actions.md %}

### Espaciador

Añade espacio o relleno entre otros bloques.

{% multi_lang_include drag_and_drop/editor_block_properties/spacer.md %}

### Código personalizado {#custom-code}

Inserta HTML, CSS o JavaScript personalizado para personalización avanzada.

| Propiedad | Descripción |
| --- | --- |
| Código personalizado | Te permite añadir, editar o eliminar HTML, CSS y JavaScript para un mensaje dentro de la aplicación. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Código personalizado" }

### Captura de teléfono {#phone-capture}

Inserta un campo de formulario para números de teléfono. Al enviar, el usuario se suscribe al grupo de suscripción de [SMS]({{site.baseurl}}/sms_rcs_subscription_groups) o [WhatsApp]({{site.baseurl}}/whatsapp_subscription_groups).

{% multi_lang_include drag_and_drop/editor_block_properties/phone_capture.md %}

### Captura de correo electrónico {#email-capture}

Inserta un campo de formulario para direcciones de correo electrónico. Al enviar, la dirección de correo electrónico se añade al perfil de ese usuario en Braze.

{% multi_lang_include drag_and_drop/editor_block_properties/email_capture.md %}

### Texto corto {#short-text}

Inserta un campo de formulario que admite atributos estándar (como nombre y apellido) o una cadena de atributo personalizado de tu elección.

{% multi_lang_include drag_and_drop/editor_block_properties/short_text_properties.md %}

### Desplegable {#dropdown}

Inserta un desplegable con una lista predefinida de elementos de los cuales los usuarios pueden seleccionar uno. Puedes añadir cualquier cadena de atributo personalizado a la lista.

{% multi_lang_include drag_and_drop/editor_block_properties/dropdown_properties.md %}

### Casilla de verificación {#checkbox}

Inserta una casilla de verificación. Si el usuario marca la casilla, el [atributo personalizado booleano]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#custom-attribute-data-types) del bloque se establece en `true`. Si se deja sin marcar, su atributo se establece en `false`.

{% multi_lang_include drag_and_drop/editor_block_properties/checkbox_properties.md %}

### Grupo de casillas de verificación {#checkbox-group}

Los usuarios pueden seleccionar entre múltiples opciones. Los valores se establecen o añaden a un [atributo personalizado de tipo array]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#custom-attribute-data-types) definido.

{% multi_lang_include drag_and_drop/editor_block_properties/checkbox_group_properties.md %}

### Texto largo {#long-text}

Campo de texto multilínea para flujos de tipo cuestionario. Si no ves este bloque, contacta con [soporte de Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support) o tu administrador de éxito de cliente de Braze.

{% multi_lang_include drag_and_drop/editor_block_properties/long_text.md %}

<!-- Saved row is not yet released. Uncomment when available.
### Fila guardada {#saved-row}

Inserta una fila reutilizable que guardaste anteriormente como un Content Block de arrastrar y soltar. Las filas guardadas **no están vinculadas** al Content Block original — si el original se actualiza, necesitarás arrastrarlo al editor de nuevo para obtener la última versión. Para más información, consulta [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks). Si no ves **Fila guardada** en **Filas**, contacta con [soporte de Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support) o tu administrador de éxito de cliente de Braze.
-->

## Cosas que debes saber {#things-to-know}

- **Video:** El creador estándar no incluye un bloque de video dedicado. Usa **Código personalizado** para incrustar un reproductor si es necesario. Para más información, consulta [Mensajes dentro de la aplicación: preguntas frecuentes]({{site.baseurl}}/user_guide/channels/in_app_messages/faq).

{% endsdktab %}

{% sdktab landing pages %}
## Bloques de editor de páginas de destino {#landing-page-editor-blocks}

Los bloques de editor para páginas de destino se encuentran en la sección **Crear** del **editor de arrastrar y soltar**, en **Filas** y categorías de bloques. Arrastra un bloque a una columna de fila; se ajusta automáticamente al ancho de la columna. Selecciona un bloque para editar su configuración en el panel de propiedades del lado derecho.

Para más información sobre cómo crear y publicar páginas de destino, consulta [Crear páginas de destino]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages).

### Título y párrafo

Añade texto de encabezado o cuerpo. Útil para estructurar secciones y mejorar la legibilidad.

{% multi_lang_include drag_and_drop/editor_block_properties/title_paragraph.md %}

### Botón

Añade un elemento clicable para acciones como abrir un enlace o enviar un formulario.

{% multi_lang_include drag_and_drop/editor_block_properties/button_properties.md %}

#### Comportamiento al hacer clic

{% multi_lang_include drag_and_drop/editor_block_properties/button_actions.md %}

{% alert important %}
Si configuras un botón con **Enviar formulario al hacer clic en el botón** y abres una URL web en una nueva pestaña, Safari en iOS puede bloquear la navegación. Abre la URL posterior al envío en la misma pestaña cuando envíes formularios. Para más información, consulta [Crear páginas de destino]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages).
{% endalert %}

### Botón de opción

Añade una lista de opciones de las cuales los usuarios pueden seleccionar una. Usa el panel de propiedades para configurar las opciones disponibles y el atributo personalizado que recibe el valor seleccionado. El perfil de usuario registra el valor seleccionado como un [atributo personalizado de tipo cadena]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes) cuando se envía el formulario. Los atributos personalizados con otros tipos de datos no se guardan en el perfil de usuario.

{% multi_lang_include drag_and_drop/editor_block_properties/radio_button_properties.md %}

### Imagen

Muestra una imagen desde una carga o URL externa.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

{% multi_lang_include drag_and_drop/editor_block_properties/image_properties.md %}

#### Comportamiento al hacer clic

{% multi_lang_include drag_and_drop/editor_block_properties/image_actions.md %}

### Enlace

Añade un hipervínculo que los usuarios pueden seleccionar para ir a una URL. Puede estar dentro del texto o ser independiente.

{% multi_lang_include drag_and_drop/editor_block_properties/link_properties.md %}

#### Comportamiento al hacer clic

{% multi_lang_include drag_and_drop/editor_block_properties/link_actions.md %}

### Espaciador

Añade espaciado vertical entre elementos.

{% multi_lang_include drag_and_drop/editor_block_properties/spacer.md %}

### Código personalizado

Inserta HTML, CSS o JavaScript personalizado para personalización avanzada, como [Google Tag Manager]({{site.baseurl}}/user_guide/messaging/landing_pages#adding-google-tag-manager-to-a-landing-page).

| Propiedad | Descripción |
| --- | --- |
| Código personalizado | Te permite añadir, editar o eliminar HTML, CSS y JavaScript. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Código personalizado" }

<!-- Countdown timer is not yet released. Uncomment when available.
### Temporizador de cuenta regresiva {#countdown-timer}

Muestra una cuenta regresiva hasta una fecha y hora que establezcas. Si no ves este bloque, contacta con [soporte de Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support) o tu administrador de éxito de cliente de Braze.

Después de añadir un bloque de **Temporizador de cuenta regresiva**, usa el panel de propiedades para establecer la fecha y hora objetivo, las etiquetas y el estilo.
-->

### Captura de correo electrónico

Añade un campo de formulario para direcciones de correo electrónico. Al enviar, la dirección se guarda en el perfil de Braze del usuario.

{% multi_lang_include drag_and_drop/editor_block_properties/email_capture.md %}

### Captura de teléfono

Añade un campo de formulario para números de teléfono. Al enviar, suscribe al usuario a tu grupo de suscripción de [SMS]({{site.baseurl}}/sms_rcs_subscription_groups) o [WhatsApp]({{site.baseurl}}/whatsapp_subscription_groups) seleccionado.

{% multi_lang_include drag_and_drop/editor_block_properties/phone_capture.md %}

### Campo de entrada {#input-field}

Añade un campo de formulario para atributos estándar (por ejemplo, nombre o apellido) o una cadena de atributo personalizado.

{% multi_lang_include drag_and_drop/editor_block_properties/short_text_properties.md %}

### Desplegable

Una lista predefinida de elementos; los usuarios eligen uno. Puedes mapear valores a cadenas de atributo personalizado.

{% multi_lang_include drag_and_drop/editor_block_properties/dropdown_properties.md %}

### Casilla de verificación

Cuando se marca, establece el [atributo personalizado booleano]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#custom-attribute-data-types) del bloque en `true`; cuando no se marca, en `false`.

{% multi_lang_include drag_and_drop/editor_block_properties/checkbox_properties.md %}

### Grupo de casillas de verificación

Los usuarios eligen múltiples opciones; los valores se establecen o añaden a un [atributo personalizado de tipo array]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#custom-attribute-data-types) definido.

{% multi_lang_include drag_and_drop/editor_block_properties/checkbox_group_properties.md %}

### Texto largo

Campo de texto multilínea para flujos de tipo cuestionario. Si no ves este bloque, contacta con [soporte de Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support) o tu administrador de éxito de cliente de Braze. Este bloque no está disponible para páginas de destino estándar.

{% multi_lang_include drag_and_drop/editor_block_properties/long_text.md %}

<!-- Saved row is not yet released. Uncomment when available.
### Fila guardada

Inserta una fila reutilizable que guardaste anteriormente como un Content Block de arrastrar y soltar. Las filas guardadas **no están vinculadas** al Content Block original — si el original se actualiza, necesitarás arrastrarlo al editor de nuevo para obtener la última versión. Para más información, consulta [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks). Si no ves **Fila guardada** en **Filas**, contacta con [soporte de Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support) o tu administrador de éxito de cliente de Braze.
-->

## Cosas que debes saber

- **Video:** El creador estándar no incluye un bloque de video dedicado. Usa **Código personalizado** para incrustar un reproductor si es necesario. Para más información, consulta [Páginas de destino]({{site.baseurl}}/user_guide/messaging/landing_pages).

{% endsdktab %}

{% sdktab banners %}
## Bloques de editor de Banner {#banner-editor-blocks}

En el creador de Banner, arrastra filas y bloques desde la sección **Crear** al lienzo para diseñar tu mensaje. Selecciona **Estilos** para ajustar el estilo a nivel de página, o selecciona un bloque o fila para editar sus propiedades en el panel lateral.

Para el flujo completo de creación de Banner, consulta [Crear un Banner]({{site.baseurl}}/user_guide/channels/banners/create_a_banner#compose-a-banner).

El creador de Banner ofrece los mismos tipos de bloques de diseño que otras superficies de arrastrar y soltar, pero no el conjunto completo de bloques de formulario (por ejemplo, no hay bloques de botón de opción, texto corto, desplegable ni casilla de verificación). Puedes añadir bloques de **Captura de teléfono** y **Captura de correo electrónico**; solo se permite **un** bloque de captura de teléfono y **un** bloque de captura de correo electrónico por mensaje.

### Título y párrafo

Añade texto de encabezado o cuerpo con opciones de texto enriquecido.

{% multi_lang_include drag_and_drop/editor_block_properties/title_paragraph.md %}

### Botón

Añade un botón clicable. Puedes configurar enlaces y opciones de análisis en el panel de propiedades.

{% multi_lang_include drag_and_drop/editor_block_properties/button_properties.md %}

#### Comportamiento al hacer clic

{% multi_lang_include drag_and_drop/editor_block_properties/button_actions.md %}

Para más información, consulta [Definir el comportamiento al hacer clic]({{site.baseurl}}/user_guide/channels/banners/create_a_banner#step-32-define-on-click-behavior-optional) en el artículo de Banner.

### Imagen

Muestra una imagen desde una URL alojada. Configura las opciones de visualización en el panel de propiedades.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

{% multi_lang_include drag_and_drop/editor_block_properties/image_properties.md %}

#### Comportamiento al hacer clic

{% multi_lang_include drag_and_drop/editor_block_properties/image_actions.md %}

### Enlace

Inserta un hipervínculo que los usuarios pueden seleccionar.

{% multi_lang_include drag_and_drop/editor_block_properties/link_properties.md %}

#### Comportamiento al hacer clic

{% multi_lang_include drag_and_drop/editor_block_properties/link_actions.md %}

### Espaciador

Añade espaciado vertical entre bloques.

{% multi_lang_include drag_and_drop/editor_block_properties/spacer.md %}

### Código personalizado

Inserta HTML personalizado para diseños avanzados o contenido incrustado (por ejemplo, video). Los clics dentro de HTML personalizado no se rastrean a menos que llames a `brazeBridge.logClick()` — consulta [Código personalizado y puente JavaScript para Banners]({{site.baseurl}}/user_guide/channels/banners/custom_code).

| Propiedad | Descripción |
| --- | --- |
| Código personalizado | Añade o edita HTML (y activos relacionados) para el Banner. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Código personalizado" }

### Captura de teléfono

Recopila un número de teléfono. Al enviar, suscribe al usuario a tu grupo de suscripción de [SMS]({{site.baseurl}}/sms_rcs_subscription_groups) o [WhatsApp]({{site.baseurl}}/whatsapp_subscription_groups) seleccionado. Solo uno por Banner.

{% multi_lang_include drag_and_drop/editor_block_properties/phone_capture.md %}

### Captura de correo electrónico

Recopila una dirección de correo electrónico y la añade al perfil de Braze del usuario al enviar. Solo uno por Banner.

{% multi_lang_include drag_and_drop/editor_block_properties/email_capture.md %}

### Texto largo

Campo de texto multilínea para flujos de tipo cuestionario. Si no ves este bloque, contacta con [soporte de Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support) o tu administrador de éxito de cliente de Braze.

{% multi_lang_include drag_and_drop/editor_block_properties/long_text.md %}

<!-- Saved row is not yet released. Uncomment when available.
### Fila guardada

Inserta una fila reutilizable que guardaste anteriormente como un Content Block de arrastrar y soltar. Las filas guardadas **no están vinculadas** al Content Block original — si el original se actualiza, necesitarás arrastrarlo al editor de nuevo para obtener la última versión. Para más información, consulta [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks). Si no ves **Fila guardada** en **Filas**, contacta con [soporte de Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support) o tu administrador de éxito de cliente de Braze.
-->

## Cosas que debes saber

- **Video:** El creador estándar no incluye un bloque de video dedicado. Usa **Código personalizado** para incrustar un reproductor si es necesario. Para más información, consulta [Banners: preguntas frecuentes]({{site.baseurl}}/user_guide/channels/banners/faq).
- **Liquid:** La mayoría de Liquid es compatible; hay excepciones como las etiquetas de re-renderizado de catálogo. Para más información, consulta [Banners: preguntas frecuentes]({{site.baseurl}}/user_guide/channels/banners/faq).

{% endsdktab %}

{% sdktab preference center %}
## Bloques de editor del centro de preferencias {#preference-center-editor-blocks}

Arrastra bloques desde la sección **Crear** a una fila en el editor de arrastrar y soltar del centro de preferencias. Cada bloque tiene su propia configuración; el panel del lado derecho cambia a propiedades o estilo para el elemento seleccionado.

Antes de editar bloques, añade grupos de suscripción y configura el **bloque inteligente** de suscripción (consulta la siguiente sección). Para el flujo de configuración completo, consulta [Crear un centro de preferencias de correo electrónico con arrastrar y soltar]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center/dnd_preference_center).

### Título y párrafo

Añade texto de encabezado o cuerpo con opciones de texto enriquecido.

{% multi_lang_include drag_and_drop/editor_block_properties/title_paragraph.md %}

### Botón

Añade un botón clicable (por ejemplo, **Guardar** o navegación).

{% multi_lang_include drag_and_drop/editor_block_properties/button_properties.md %}

### Imagen

Muestra una imagen de la [biblioteca de medios]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library) o una URL.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

{% multi_lang_include drag_and_drop/editor_block_properties/image_properties.md %}

### Espaciador

Añade espaciado vertical entre bloques.

{% multi_lang_include drag_and_drop/editor_block_properties/spacer.md %}

### Grupos de suscripción (bloque inteligente) {#subscription-groups-smart-block}

Añade un bloque de plantilla que lista los grupos de suscripción, controles opcionales de **Suscribirse a todos** / **Cancelar suscripción de todos** y descripciones. Configúralo después de añadir grupos en el flujo de trabajo del centro de preferencias.

Después de [añadir grupos de suscripción]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center/dnd_preference_center#step-3-add-subscription-groups-to-the-preference-center), selecciona el bloque inteligente en el lienzo para:

- Reordenar grupos de suscripción
- Añadir o eliminar grupos
- Añadir o eliminar descripciones
- Alternar **Suscribirse a todos** y **Cancelar suscripción de todos** para los grupos en ese bloque

El control **Cancelar suscripción de todos** en la parte inferior de la plantilla predeterminada es obligatorio y realiza una [cancelación de suscripción global]({{site.baseurl}}/user_guide/channels/email/subscriptions#subscription-states) del correo electrónico.

## Cosas que debes saber

- **Estilos comunes:** Puedes establecer valores predeterminados a nivel de página en **Estilos comunes** antes de ajustar bloques individuales. Para más información, consulta [Personalizar el centro de preferencias usando el editor de arrastrar y soltar]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center/dnd_preference_center#step-4-customize-the-preference-center-using-the-drag-and-drop-editor).
- **Página de confirmación:** Cambia a **Página de confirmación** en la parte superior del editor para dar estilo a la experiencia posterior al guardado usando los mismos tipos de bloques.

{% endsdktab %}

{% endsdktabs %}