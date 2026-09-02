---
nav_title: Preguntas frecuentes
article_title: Preguntas frecuentes del editor de arrastrar y soltar
alias: "/dnd/faq/"
channel: email
page_order: 5
description: "Preguntas frecuentes sobre el editor de correo electrónico de arrastrar y soltar."
tool:
  - Campaigns
  - Canvas



---

# Preguntas frecuentes {#frequently-asked-questions}

> Esta página ofrece respuestas a algunas preguntas frecuentes relacionadas con el editor de arrastrar y soltar para correo electrónico.

## ¿Puedo previsualizar cómo se ve mi correo electrónico en modo oscuro? {#can-i-preview-how-my-email-appears-in-dark-mode}

Sí. Ve a la sección **Vista previa y prueba** del editor de arrastrar y soltar y activa el **Modo oscuro**. También te recomendamos previsualizar y probar tus correos electrónicos en diferentes plataformas de usuario y utilizar imágenes transparentes para las imágenes de fondo de las filas cuando sea posible.

## ¿Cómo debo diseñar correos electrónicos para el modo oscuro y el modo claro? {#how-should-i-design-emails-for-dark-mode-and-light-mode}

Los correos electrónicos no necesitan enviarse en diseños separados para modo claro y oscuro, ya que los clientes de correo electrónico y los dispositivos pueden aplicar su propio tema oscuro. Sin embargo, esto puede invertir colores u ocultar fondos si no se establecen colores explícitos en el contenedor exterior y las secciones principales. Para evitar esto, recomendamos establecer colores de fondo sólidos para que tu mensaje se lea con claridad tanto en modo oscuro como en modo claro.

Algunos clientes de correo electrónico reemplazan las imágenes de fondo o invierten el texto de bajo contraste en modo oscuro, por lo que el texto del cuerpo puede parecer ausente o mostrarse de forma diferente entre clientes (por ejemplo, Gmail en iOS frente a Android). Establece `background-color` en el contenedor exterior y las secciones principales en lugar de depender únicamente de imágenes de fondo para fondos claros.

## ¿Por qué mi fuente personalizada no aparece en la vista previa del correo electrónico de arrastrar y soltar? {#why-doesnt-my-custom-font-appear-in-drag-and-drop-email-preview}

Las fuentes personalizadas se cargan en la vista previa del editor cuando un bloque de **Texto** en el mensaje hace referencia a la fuente. Si la vista previa sigue mostrando una fuente alternativa después de configurar una fuente personalizada en la configuración del **Drag-and-Drop Email Editor**, añade un bloque de **Texto** que utilice esa fuente para que el editor la cargue en la vista previa. Confirma que el uso compartido de recursos entre orígenes (CORS) esté habilitado en tu archivo de fuente. Vuelve a comprobar **vista previa and Test** y tus clientes de correo electrónico de destino antes de enviar. Para ver los pasos de configuración, consulta [Fuente personalizada]({{site.baseurl}}/user_guide/channels/email/customize/email_global_style_settings#custom-font).

## ¿Cómo puedo conservar el formato de texto cuando copio y pego desde otra aplicación? {#how-can-i-carry-over-text-formatting-when-i-copy-and-paste-from-another-application}

Los distintos editores de texto y aplicaciones tienen sus propias formas de gestionar el formato de texto, que pueden no ser reconocidas de forma universal. Cuando copias y pegas texto con formato desde fuera de Braze en el editor de arrastrar y soltar, es posible que el formato enriquecido no se conserve.

Para pegar texto sin formato enriquecido, usa uno de estos métodos:
- En Mac: Pulsa <kbd>cmd</kbd>+<kbd>shift</kbd>+<kbd>V</kbd> en lugar de <kbd>cmd</kbd>+<kbd>V</kbd>
- En Windows: Pulsa <kbd>ctrl</kbd>+<kbd>shift</kbd>+<kbd>V</kbd> en lugar de <kbd>ctrl</kbd>+<kbd>V</kbd>
- Haz clic derecho dentro del editor y selecciona **Pegar y adaptar estilo**

## ¿Cómo puedo cambiar el relleno del correo electrónico en móvil sin actualizar el relleno en la vista web? {#how-can-i-change-the-email-padding-on-mobile-without-updating-the-padding-in-the-web-view}

No puedes editar el relleno exclusivamente para las vistas de móvil y web, por lo que cualquier cambio se refleja en ambas vistas. Sin embargo, puedes añadir lógica CSS en el editor HTML que establezca el relleno en función de diferentes tamaños de pantalla. Esto no es compatible con el editor de arrastrar y soltar, así que puedes exportar el archivo HTML y usar el editor HTML en su lugar.

## ¿Cómo puedo optimizar una fila de botones para que permanezca horizontal en escritorio y móvil? {#how-can-i-optimize-a-row-of-buttons-to-remain-horizontal-on-desktop-and-mobile}

Al crear un correo electrónico con el editor de arrastrar y soltar, si creas una fila horizontal de botones de llamada a la acción, es posible que los botones cambien a una orientación vertical en dispositivos móviles.

Para mantener el mismo formato en todos los tamaños de dispositivo, te recomendamos crear una fila separada con botones de llamada a la acción que tengan un relleno optimizado para móvil y estén configurados para ocultar la fila en un dispositivo de escritorio. Tener dos filas separadas significa que puedes establecer el relleno deseado para la mejor representación del texto en dispositivos de escritorio y móviles.

## ¿Puedo ajustar la altura de la fila en el editor de arrastrar y soltar? {#can-i-adjust-the-row-height-in-the-drag-and-drop-editor}

La altura de la fila se ajusta automáticamente al contenido. Como alternativa, te recomendamos que:
1. Añadas un bloque divisor.
2. Hagas clic en el conmutador para activar su transparencia.
3. Ajustes la altura.

## ¿Es posible crear capas en el editor? ¿Puedo añadir una imagen de fondo, superponer una imagen y añadir una capa de texto encima? {#is-it-possible-to-build-layers-in-the-editor-can-i-add-a-background-image-layer-on-an-image-and-add-a-text-layer-over-that}

El editor de arrastrar y soltar actualmente admite dos capas. Puedes establecer una imagen de fondo de fila y personalizar los colores de fondo.

## ¿Puedo guardar mi correo electrónico de arrastrar y soltar como plantilla después de crearlo en mi Campaign o Canvas? {#can-i-save-my-drag-and-drop-email-as-a-template-after-i-build-it-within-my-campaign-or-canvas}

No. No puedes guardar un correo electrónico de arrastrar y soltar desde una Campaign o Canvas como una **plantilla de correo electrónico** de arrastrar y soltar en **Plantillas** > **Plantillas de correo electrónico**. Recrea el diseño en **Plantillas** > **Plantillas de correo electrónico**, o la próxima vez comienza desde una plantilla guardada. Para obtener instrucciones, consulta [Crear una plantilla de correo electrónico]({{site.baseurl}}/user_guide/messaging/templates/email_templates/email_template).

Si necesitas una plantilla HTML reutilizable, selecciona **Descargar archivo** mientras editas el cuerpo de arrastrar y soltar, abre el HTML del ZIP y pega el código en una [plantilla de correo electrónico HTML]({{site.baseurl}}/user_guide/messaging/templates/email_templates/html_email_template) usando el editor de código HTML. Después, vuelve a verificar Liquid, los enlaces y los activos alojados.

Para más información sobre dónde se encuentran las plantillas, consulta [Plantillas y medios]({{site.baseurl}}/user_guide/messaging/templates).

## ¿Por qué no puedo cambiar el color de relleno de un botón en el editor de arrastrar y soltar? {#why-cant-i-change-a-buttons-fill-color-in-the-drag-and-drop-editor}

Los estilos a nivel de página pueden anular los estilos a nivel de mensaje. Si actualizar **Relleno** en un botón o bloque no hace nada, prueba lo siguiente:
1. Abre la [configuración global de estilos de correo electrónico]({{site.baseurl}}/user_guide/channels/email/customize/email_global_style_settings) y selecciona **Reset to default** en el estilo de página en conflicto para que el color a nivel de mensaje pueda aplicarse.
2. Establece el color de nuevo en el bloque.

## ¿Puedo añadir archivos adjuntos de correo electrónico al editor de arrastrar y soltar? {#can-i-add-email-attachments-to-the-drag-and-drop-editor}

Sí. Puedes añadir archivos adjuntos a tu mensaje de correo electrónico yendo a **Configuración de envío** > **Avanzado**.

## ¿Cómo descargo el HTML sin procesar de un correo electrónico de arrastrar y soltar? {#how-do-i-download-the-raw-html-for-a-drag-and-drop-email}

El editor de arrastrar y soltar incluye **Descargar archivo** como opción para exportar tu correo electrónico como un archivo HTML dentro de un archivo ZIP.

1. Abre tu Campaign o Canvas y edita el mensaje de correo electrónico.
2. Selecciona **Editar cuerpo del correo electrónico** para abrir el editor de arrastrar y soltar.
3. Selecciona **Descargar archivo**.
4. Extrae el archivo comprimido para acceder al HTML generado.

{% alert tip %}
En Windows, mueve el archivo ZIP a una ubicación permanente (como Descargas) antes de extraerlo. Extraer desde una carpeta temporal puede impedir que accedas al archivo HTML después de que esa carpeta se borre.
{% endalert %}

Puedes pegar ese HTML en un [bloque HTML]({{site.baseurl}}/user_guide/channels/email/drag_and_drop#content) o en el editor HTML cuando necesites ediciones de bajo nivel (por ejemplo, para [desactivar el seguimiento de clics en enlaces específicos]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links#turning-off-click-tracking-on-a-link-to-link-basis)).

## ¿Por qué se rompe mi diseño de arrastrar y soltar? {#why-is-my-drag-and-drop-layout-breaking}

Los problemas de diseño suelen deberse a **HTML o CSS personalizados** que entran en conflicto con el marcado que genera el editor. Prueba estos pasos:

1. Elimina o aísla los bloques de HTML personalizado para ver si el problema desaparece.
2. Revisa la configuración del **editor de correo electrónico de arrastrar y soltar** en busca de fuentes personalizadas que podrían no cargarse en todos los clientes.
3. En **Row Properties**, revisa el relleno y el ancho de las columnas.
4. Cuando añadas HTML personalizado, opta por diseños basados en tablas, imágenes fluidas y anchos de tabla totales que se ajusten al ancho de tu correo electrónico: las imágenes con píxeles fijos o las estructuras que no usan tablas suelen romperse en Outlook y otros clientes.

## ¿Por qué mi Content Block no se muestra en la vista previa del correo electrónico? {#why-doesnt-my-content-block-render-in-email-preview}

Si un Content Block no se muestra en la vista previa del correo electrónico, comprueba si hay etiquetas de anclaje sin cerrar. Para las URL de contenido conectado, utiliza el filtro `replace` para convertir los ampersands con doble codificación (`&amp;amp;`) en un ampersand con codificación simple (`&amp;`). Limita el anidamiento de Content Blocks a dos niveles.

## ¿Por qué un Content Block de arrastrar y soltar pierde el estilo móvil dentro de un bloque de código personalizado? {#why-does-a-drag-and-drop-content-block-lose-mobile-styling-inside-a-custom-code-block}

Cuando colocas un **Content Block** de arrastrar y soltar dentro de un bloque de **código personalizado** (HTML), es posible que el estilo y la alineación específicos para dispositivos móviles del Content Block no se apliquen en el mensaje enviado. Cuando tanto el Content Block como la plantilla utilizan el editor de arrastrar y soltar, añade el Content Block como su propia fila en lugar de anidarlo dentro de código personalizado.

Cuando apiles varios Content Blocks, utiliza una fila separada para cada bloque en lugar de colocar varios bloques en una sola fila.

## ¿Por qué el editor de arrastrar y soltar ignora la configuración de alineación? {#why-is-the-drag-and-drop-editor-ignoring-alignment-settings}

Si el editor de arrastrar y soltar ignora la configuración de alineación, elimina el CSS personalizado o los bloques HTML, elimina las fuentes personalizadas, comprueba si hay conflictos de CSS y evita duplicar bloques de fila. Ponte en contacto con soporte de Braze si el problema persiste.

## ¿Por qué el código de color hexadecimal que elegí no coincide con la fuente de mi correo electrónico? {#why-does-my-chosen-hex-color-code-not-match-the-font-in-my-email}

Si estás utilizando un Content Block, el bloque puede tener su propia configuración de color de fuente. Selecciona el bloque de texto dentro del Content Block y elimina cualquier anulación local de **Font color** para que tu color hexadecimal del estilo global o de párrafo pueda aplicarse.