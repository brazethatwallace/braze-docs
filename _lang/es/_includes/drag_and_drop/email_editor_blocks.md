## Uso de bloques de editor de correo electrónico

Los bloques de editor se encuentran en la sección **Contenido** de los mensajes de correo electrónico. Para usar un bloque de editor, arrastra un bloque de editor dentro de una columna en el editor de arrastrar y soltar. Se ajustará automáticamente al ancho de la columna. Cada bloque de editor tiene su propia configuración, como el control granular del relleno.

Para obtener más información sobre cómo usar y personalizar estos bloques de editor en tu correo electrónico, consulta [Otras personalizaciones]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/#other-customizations).

{% alert tip %}
También puedes añadir [atributos personalizados]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/) a cualquier URL dentro de los bloques de editor `Image`, `Button` o `Text`.
{% endalert %}

## Tipos

La siguiente tabla describe cómo los usuarios pueden utilizar cada tipo de bloque de editor.

| Nombre | Descripción |
|---|---|
|Título| Añade texto para encabezados dentro del correo electrónico. | 
|Párrafo| Introduce texto en el mensaje. Una barra de herramientas ayuda con las funciones de edición de fuentes y texto. | 
|Lista| Añade una lista con viñetas. |
|Botón| Añade un botón estándar. Las propiedades de este bloque permiten editar y configurar enlaces fácilmente. | 
|Divisor| Inserta una línea sólida, punteada o discontinua para ayudar con el espaciado.|
|Espaciador| Añade espacio, o "relleno", entre otros bloques. |
|Imagen| Inserta una imagen de la [biblioteca de medios]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/). | 
|Video| Crea un enlace al contenido del video. |
|Social| Inserta el icono de la plataforma de redes sociales. Puedes cargar imágenes personalizadas para iconos específicos de la marca. |
|Iconos| Inserta un icono. Puedes cargar imágenes personalizadas. Braze utiliza un icono de marcador de posición de gran tamaño hasta que cargues una imagen. |
|HTML| Inserta HTML sin formato. Recomendado para [Liquid]({{site.baseurl}}/liquid/), como Contenido conectado o sentencias condicionales. | 
|Menú| Crea un menú flexible para el mensaje que estás diseñando. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Personalización en correo electrónico

- **Liquid:** En **Contenido** > **Personalización**, selecciona un atributo, copia el fragmento de código y pégalo en un bloque de texto (Liquid básico) o en un bloque HTML (Liquid avanzado). En general, aunque puedes usar Liquid básico en bloques de texto, recomendamos usar bloques HTML para lógica más compleja y así evitar problemas de diseño. Ten en cuenta que Liquid no es compatible en bloques de imagen ni en campos de URL de botones.
- **Contenido conectado:** Añade un bloque **HTML** y coloca tu llamada {% raw %}`{% connected_content %}`{% endraw %} allí.

## Propiedades

En las siguientes tablas se proporcionan detalles sobre las propiedades de cada bloque de editor.

### Título
Consulta la siguiente tabla para obtener detalles sobre las propiedades del bloque de editor `Title`.

| Propiedades | Descripción |
|---|---|
|Título| Selecciona el estilo del encabezado. | 
|Familia de fuente| Es el estilo de fuente para tu título. |
|Peso de fuente| Es el grosor general de la fuente. |
|Tamaño de fuente| Determina el tamaño del texto. |
|Color de texto| Modifica el color del título. |
|Color del enlace| Modifica el color del enlace. |
|Alinear| Mueve el título hacia la izquierda, el centro o la derecha. |
|Altura de línea| Modifica la distancia entre líneas de texto. |
|Interlineado| Modifica la distancia entre cada carácter. |
|Dirección del texto| Predeterminado de izquierda a derecha, pero se puede editar para que sea [de derecha a izquierda]({{site.baseurl}}/right_to_left_messages/). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Párrafo

Consulta la siguiente tabla para obtener detalles sobre las propiedades del bloque de editor `Paragraph`.

| Propiedades | Descripción |
|---|---|
|Familia de fuente| Es el estilo de fuente para el texto de tu párrafo. |
|Peso de fuente| Es el grosor general de la fuente. |
|Tamaño de fuente| Determina el tamaño del texto. |
|Color de texto| Modifica el color del título. |
|Color del enlace| Modifica el color del enlace. |
|Alinear| Mueve el título hacia la izquierda, el centro o la derecha. |
|Espaciado entre párrafos| Modifica el espacio entre párrafos. |
|Altura de línea| Modifica la distancia entre líneas de texto. |
|Espaciado de letras| Modifica la distancia entre cada carácter. |
|Dirección del texto| Predeterminado de izquierda a derecha, pero se puede editar para que sea [de derecha a izquierda]({{site.baseurl}}/right_to_left_messages/). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Lista

Consulta la siguiente tabla para obtener detalles sobre las propiedades del bloque de editor `List`.

| Propiedades | Descripción |
|---|---|
|Tipo de lista| Es el tipo de lista. Puede ser con viñetas o numerada. |
|Tipo de estilo de lista| Determina el estilo de tu lista. |
|Iniciar lista desde| Determina el número inicial de tu lista. |
|Familia de fuente| Es el estilo de fuente para el texto de tu párrafo. |
|Peso de fuente| Es el grosor general de la fuente. |
|Tamaño de fuente| Determina el tamaño del texto. |
|Color de texto| Modifica el color del título. |
|Color del enlace| Modifica el color del enlace. |
|Alinear| Mueve el título hacia la izquierda, el centro o la derecha. |
|Espaciado de elementos de lista| Modifica el espacio entre los elementos de la lista. |
|Sangría de elementos de lista| Modifica la sangría de los elementos de la lista. |
|Altura de línea| Modifica la distancia entre líneas de texto. |
|Espaciado de letras| Modifica la distancia entre cada carácter. |
|Dirección del texto| Predeterminado de izquierda a derecha, pero se puede editar para que sea [de derecha a izquierda]({{site.baseurl}}/right_to_left_messages/). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Divisor

Consulta la siguiente tabla para obtener detalles sobre el bloque de editor `Divider`.

| Propiedades | Descripción |
|---|---|
|Transparente| Si se habilita, se eliminan las opciones de "línea" y "ancho". |
|Línea| Los diferentes formatos de línea, ya sean punteados, de puntos o sólidos. Además, puedes modificar el grosor y el color de la línea divisoria. |
|Ancho| Ajusta la extensión del divisor en incrementos de 5.  |
|Alinear| Mueve la línea hacia la izquierda, el centro o la derecha. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Espaciador

Consulta la siguiente tabla para obtener detalles sobre el bloque de editor `Spacer`.

| Propiedades | Descripción |
|---|---|
|Altura| Ajusta la altura del bloque espaciador. El valor predeterminado es 60 px.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Imagen

Consulta la siguiente tabla para obtener detalles sobre el bloque de editor `Image`. Para imágenes dinámicas (imágenes con Liquid o Contenido conectado), debes establecer una imagen alternativa para usar la configuración de ancho automático. Para las especificaciones de imágenes, consulta nuestras [especificaciones de imágenes de correo electrónico]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/image_specs/#email).

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

| Propiedades | Descripción |
|---|---|
|Ancho automático| Modifica el ancho de la imagen en píxeles. |
|Alinear| Orienta la imagen hacia la izquierda, el centro o la derecha del bloque. |
|Imagen con Liquid| Usa la lógica de [Liquid]({{site.baseurl}}/liquid/) para establecer dinámicamente diferentes imágenes dentro del mismo bloque de contenido. |
|URL| Establece una imagen usando la dirección donde está alojada. |
|Texto alternativo| Una breve descripción de la imagen que proporciona a los usuarios la misma información que se muestra en la imagen. Esto es esencial para la accesibilidad de lectores de pantalla o cuando la imagen no se carga. |
|Imagen con esquinas redondeadas| Renderiza la imagen con esquinas redondeadas. De forma predeterminada, las imágenes se renderizan con esquinas cuadradas. |
|Acción| Desencadena una acción cuando el usuario hace clic en la imagen.|
|Opciones de bloque| Establece el relleno alrededor del bloque de imagen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
Para `Auto Width`, el redimensionamiento automático de imagen elige el mejor tamaño para la imagen basándose en una combinación del ancho de la imagen y el espacio disponible en el diseño:
- Las imágenes más anchas que el espacio disponible se ajustarán al 100 % de ancho y mantendrán esta proporción en dispositivos móviles, utilizando todo el ancho de pantalla del dispositivo.
- Las imágenes más pequeñas que el espacio disponible utilizarán el tamaño natural de la imagen para evitar efectos de distorsión o imágenes borrosas.
{% endalert %}

### Video

Consulta la siguiente tabla para obtener detalles sobre el bloque de editor `Video`.

| Propiedades | Descripción |
|---|---|
|URL| La URL del video. Ten en cuenta que solo son compatibles YouTube y Vimeo. |
|Título| Se genera automáticamente a partir de los metadatos del video o puede personalizarse. |
|Estilo del icono de reproducción| Incluye diferentes opciones para el botón de reproducción ubicado en la parte superior de una imagen de video. |
|Color del icono de reproducción| Opción de seleccionar **Claro** u **Oscuro** para el botón de reproducción. |
|Tamaño del icono de reproducción| Elige el tamaño en píxeles del botón de reproducción. Rango prefijado de 50&nbsp;px a 80&nbsp;px (incrementado en 5&nbsp;px). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
Los videos alojados en Vimeo solo funcionarán si están configurados como públicos. Todos los demás ajustes de seguridad disponibles en Vimeo (por ejemplo, "Ocultar de Vimeo.com") generarán un formato de enlace diferente que no es compatible con este bloque de contenido. Este tipo de enlaces son alterados por el constructor, lo que impide que Braze genere una miniatura.
{% endalert %}

### Social

Consulta la siguiente tabla para obtener detalles sobre el bloque de editor `Social`.

| Propiedades | Descripción |
|---|---|
|Seleccionar colección de iconos| Establece el estilo de tu colección de iconos. |
|Configurar colección de iconos| Establece la URL de cada icono social. Incluye la opción **Más opciones** para editar el título y el texto alternativo. |
|Alinear| Mueve el icono social hacia la izquierda, el centro o la derecha. |
|Espaciado entre iconos| Determina el espaciado entre cada icono social. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Iconos

Consulta la siguiente tabla para obtener detalles sobre el bloque de editor `Icons`.

| Propiedades | Descripción |
|---|---|
|Familia de fuente| Es el estilo de fuente para el texto de tu párrafo. |
|Peso de fuente| Es el grosor general de la fuente. |
|Tamaño de fuente| Determina el tamaño del texto. |
|Color de texto| Modifica el color del título. |
|Color del enlace| Modifica el color del enlace. |
|Alinear| Mueve el icono hacia la izquierda, el centro o la derecha. |
|Espaciado de letras| Modifica la distancia entre cada carácter. |
|Tamaño del icono| Determina el tamaño de tu icono. |
|Espaciado del icono| Modifica el espacio del icono. |
|Relleno del icono| Modifica el relleno del icono. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### HTML

Consulta la siguiente tabla para obtener detalles sobre el bloque de editor `HTML`.

| Propiedades | Descripción |
|---|---|
|Editor HTML| Introduce el HTML sin formato. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Menú

Consulta la siguiente tabla para obtener detalles sobre el bloque de editor `Menu`.

| Propiedades | Descripción |
|---|---|
|Configurar elementos del menú| Añade un elemento de menú. |
|Familia de fuente| El estilo que se utilizará para tu menú. |
|Tamaño de fuente| El tamaño de tu menú. |
|Color de texto| Modifica el color del menú. |
|Color del enlace| Modifica el color del texto del menú. |
|Alinear| Mueve el menú hacia la izquierda, el centro o la derecha. |
|Espaciado de letras| Modifica la distancia entre cada carácter. |
|Diseño| Determina si el diseño es horizontal o vertical. |
|Separador| Añade carácter(es) entre las opciones del menú. |
|Menú móvil| Incluye opciones para modificar el tamaño, el color y el tipo de icono cuando se muestra en un dispositivo móvil. |
|Relleno de elementos| Modifica el relleno usando los botones **+** o **-**, o introduciendo un número específico. |
|Todos los lados| Establece un número de relleno consistente si el relleno de elementos está deshabilitado. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Acciones

Puedes asignar una acción que se produzca cuando un usuario toque un botón, un enlace o una imagen del mensaje. También puedes usar [Liquid]({{site.baseurl}}/liquid/) para personalizar las acciones. En las siguientes tablas se proporcionan detalles sobre las acciones de cada bloque de editor.

### Botón

Consulta la siguiente tabla para obtener detalles sobre el bloque de editor `Button`.

| Propiedades | Descripción |
|---|---|
|Tipo de enlace| Determina la acción al hacer clic en el botón y establece el protocolo adecuado. |
|URL| Dinámico según el tipo de enlace **Abrir página web**.|
|Correo electrónico, asunto y cuerpo| Para el tipo de enlace **Enviar correo electrónico**, establece la dirección de correo electrónico del destinatario, el asunto y el contenido que se completarán en un borrador de correo electrónico cuando el usuario seleccione el botón.|
|Tel.| Para los tipos de enlace **Realizar llamada** y **Enviar SMS**, establece el número de teléfono al que el usuario llamará o enviará un mensaje de texto al seleccionar el botón.|
|Mensaje| Para el tipo de enlace **Enviar SMS**, establece el contenido que aparecerá en un borrador de mensaje SMS cuando el usuario seleccione el botón.|
|Opciones de botón| Establece varias opciones del botón, como fuente, ancho, color y otras.|
|Botón al pasar el cursor| El estilo del botón cuando el usuario pasa el cursor por encima con el ratón o el trackpad. Esto incluye el color de fondo del botón, el color de la fuente y los estilos de los bordes.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }