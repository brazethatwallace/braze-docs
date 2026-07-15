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

Sí. Ve a la sección **Preview and Test** del editor de arrastrar y soltar y activa **Dark mode**. También recomendamos previsualizar y probar tus correos electrónicos en diferentes plataformas de usuario y usar imágenes transparentes para las imágenes de fondo de las filas cuando sea posible.

## ¿Cómo debo diseñar correos electrónicos para modo oscuro y modo claro? {#how-should-i-design-emails-for-dark-mode-and-light-mode}

Los correos electrónicos no necesitan enviarse en diseños separados de modo claro y oscuro, ya que los clientes y dispositivos de correo electrónico pueden aplicar su propio tema oscuro. Sin embargo, esto puede invertir colores u ocultar fondos si no se establecen colores explícitos en el contenedor exterior y las secciones principales. Para evitar esto, recomendamos establecer colores de fondo sólidos para que tu mensaje se lea claramente tanto en modo oscuro como en modo claro.

Algunos clientes de correo electrónico reemplazan las imágenes de fondo o invierten el texto de bajo contraste en modo oscuro, por lo que el texto del cuerpo puede parecer que falta o renderizarse de forma diferente entre clientes (por ejemplo, Gmail en iOS frente a Android). Establece `background-color` en el contenedor exterior y las secciones principales en lugar de depender solo de imágenes de fondo para fondos claros.

## ¿Por qué mi fuente personalizada no aparece en la vista previa del correo electrónico de arrastrar y soltar? {#why-doesnt-my-custom-font-appear-in-drag-and-drop-email-preview}

Las fuentes personalizadas se cargan en la vista previa del editor cuando un bloque de **Text** en el mensaje hace referencia a la fuente. Si la vista previa sigue mostrando una fuente alternativa después de configurar una fuente personalizada en la configuración del **editor de correo electrónico de arrastrar y soltar**, agrega un bloque de **Text** que use esa fuente para que el editor la cargue en la vista previa. Confirma que el uso compartido de recursos entre orígenes (CORS) esté habilitado en tu archivo de fuente. Vuelve a verificar **Preview and Test** y tus clientes de correo electrónico de destino antes de enviar. Para los pasos de configuración, consulta [Fuente personalizada]({{site.baseurl}}/user_guide/channels/email/customize/email_global_style_settings#custom-font).

## ¿Cómo puedo cambiar el relleno del correo electrónico en móvil sin actualizar el relleno en la vista web? {#how-can-i-change-the-email-padding-on-mobile-without-updating-the-padding-in-the-web-view}

No puedes editar el relleno para las vistas de móvil y web de forma independiente, por lo que cualquier edición se refleja en ambas vistas. Sin embargo, puedes agregar lógica CSS en el editor HTML que establezca el relleno según diferentes tamaños de pantalla. Esto no es compatible con el editor de arrastrar y soltar, así que puedes exportar el archivo HTML y usar el editor HTML en su lugar.

## ¿Cómo puedo optimizar una fila de botones para que permanezcan horizontales en escritorio y móvil? {#how-can-i-optimize-a-row-of-buttons-to-remain-horizontal-on-desktop-and-mobile}

Al crear un correo electrónico con el editor de arrastrar y soltar, si creas una fila horizontal de botones de llamada a la acción, es posible que los botones cambien a una orientación vertical en móvil.

Para mantener el mismo formato en diferentes tamaños de dispositivo, recomendamos crear una fila separada con botones de llamada a la acción que tengan un relleno optimizado para móvil y estén configurados para ocultar la fila en un dispositivo de escritorio. Tener dos filas separadas significa que puedes establecer el relleno deseado para la mejor representación del texto en dispositivos de escritorio y móviles.

## ¿Puedo ajustar la altura de la fila en el editor de arrastrar y soltar? {#can-i-adjust-the-row-height-in-the-drag-and-drop-editor}

La altura de la fila se ajusta automáticamente al contenido. Como alternativa, recomendamos que:
1. Agregues un bloque divisor.
2. Hagas clic en el interruptor para activar su transparencia.
3. Ajustes la altura.

## ¿Es posible crear capas en el editor? ¿Puedo agregar una imagen de fondo, superponer una imagen y agregar una capa de texto encima? {#is-it-possible-to-build-layers-in-the-editor-can-i-add-a-background-image-layer-on-an-image-and-add-a-text-layer-over-that}

El editor de arrastrar y soltar actualmente admite dos capas. Puedes establecer una imagen de fondo de fila y personalizar los colores de fondo.

## ¿Puedo guardar mi correo electrónico de arrastrar y soltar como plantilla después de crearlo dentro de mi campaña o Canvas? {#can-i-save-my-drag-and-drop-email-as-a-template-after-i-build-it-within-my-campaign-or-canvas}

No. No puedes guardar un correo electrónico de arrastrar y soltar desde una campaña o Canvas como una **plantilla de correo electrónico** de arrastrar y soltar en **Templates** > **Email Templates**. Recrea el diseño en **Templates** > **Email Templates**, o la próxima vez comienza desde una plantilla guardada. Para obtener instrucciones, consulta [Crear una plantilla de correo electrónico]({{site.baseurl}}/user_guide/messaging/templates/email_templates/email_template).

Si necesitas una plantilla HTML reutilizable, selecciona **Download file** mientras editas el cuerpo de arrastrar y soltar, abre el HTML del archivo ZIP y pega el código en una [plantilla de correo electrónico HTML]({{site.baseurl}}/user_guide/messaging/templates/email_templates/html_email_template) usando el editor de código HTML. Vuelve a verificar el Liquid, los enlaces y los activos alojados después.

Para más información sobre dónde se encuentran las plantillas, consulta [Plantillas y medios]({{site.baseurl}}/user_guide/messaging/templates).

## ¿Por qué no puedo cambiar el color de relleno de un botón en el editor de arrastrar y soltar? {#why-cant-i-change-a-buttons-fill-color-in-the-drag-and-drop-editor}

Los estilos a nivel de página pueden anular los estilos a nivel de mensaje. Si actualizar **Fill** en un botón o bloque no tiene efecto, intenta lo siguiente:
1. Abre la [configuración global de estilos de correo electrónico]({{site.baseurl}}/user_guide/channels/email/customize/email_global_style_settings) y selecciona **Reset to default** en el estilo de página en conflicto para que el color a nivel de mensaje pueda aplicarse.
2. Establece el color de nuevo en el bloque.

## ¿Puedo agregar archivos adjuntos de correo electrónico en el editor de arrastrar y soltar? {#can-i-add-email-attachments-to-the-drag-and-drop-editor}

Sí. Puedes agregar archivos adjuntos a tu mensaje de correo electrónico yendo a **Sending Settings** > **Advanced**.

## ¿Cómo descargo el HTML sin procesar de un correo electrónico de arrastrar y soltar? {#how-do-i-download-the-raw-html-for-a-drag-and-drop-email}

1. Abre tu campaña o Canvas y edita el mensaje de correo electrónico.
2. Selecciona **Edit email body** para abrir el editor de arrastrar y soltar.
3. Selecciona **Download file** (en la parte inferior del editor). Extrae el archivo para acceder al HTML generado.

Puedes pegar ese HTML en un [bloque HTML]({{site.baseurl}}/user_guide/channels/email/drag_and_drop#content) o en el editor HTML cuando necesites ediciones de bajo nivel, por ejemplo, para [desactivar el seguimiento de clics en enlaces específicos]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links#turning-off-click-tracking-on-a-link-to-link-basis).

## ¿Por qué se rompe mi diseño de arrastrar y soltar? {#why-is-my-drag-and-drop-layout-breaking}

Los problemas de diseño suelen deberse a **HTML o CSS personalizado** que entra en conflicto con el código que genera el editor. Prueba estos pasos:

1. Elimina o aísla los bloques HTML personalizados para ver si el problema desaparece.
2. Revisa la configuración del **editor de correo electrónico de arrastrar y soltar** en busca de fuentes personalizadas que puedan no cargarse en todos los clientes.
3. En **Row Properties**, revisa el relleno y los anchos de las columnas.
4. Cuando agregues HTML personalizado, usa diseños basados en tablas, imágenes fluidas y anchos de tabla totales que se ajusten al ancho de tu correo electrónico; las imágenes con píxeles fijos o las estructuras que no son de tabla suelen romperse en Outlook y otros clientes.

## ¿Por qué mi Content Block no se renderiza en la vista previa del correo electrónico? {#why-doesnt-my-content-block-render-in-email-preview}

Si un Content Block no se renderiza en la vista previa del correo electrónico, verifica que no haya etiquetas de anclaje sin cerrar. Para las URL de contenido conectado, usa el filtro `replace` para convertir los ampersands doblemente codificados (`&amp;amp;`) en un solo ampersand codificado (`&amp;`). Limita el anidamiento de Content Blocks a dos niveles.

## ¿Por qué un Content Block de arrastrar y soltar pierde los estilos móviles dentro de un bloque de código personalizado? {#why-does-a-drag-and-drop-content-block-lose-mobile-styling-inside-a-custom-code-block}

Cuando colocas un **Content Block** de arrastrar y soltar dentro de un bloque de **Custom Code** (HTML), los estilos y la alineación específicos para móvil del Content Block pueden no aplicarse en el mensaje enviado. Cuando tanto el Content Block como la plantilla usan el editor de arrastrar y soltar, agrega el Content Block como su propia fila en lugar de anidarlo dentro de código personalizado.

Cuando apiles varios Content Blocks, usa una fila separada para cada bloque en lugar de colocar varios bloques en una sola fila.

## ¿Por qué el editor de arrastrar y soltar ignora la configuración de alineación? {#why-is-the-drag-and-drop-editor-ignoring-alignment-settings}

Si el editor de arrastrar y soltar ignora la configuración de alineación, elimina los bloques de CSS o HTML personalizados, elimina las fuentes personalizadas, verifica si hay conflictos de CSS y evita duplicar bloques de fila. Ponte en contacto con soporte de Braze si el problema persiste.