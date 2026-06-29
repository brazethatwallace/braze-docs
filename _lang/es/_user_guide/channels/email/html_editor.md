---
nav_title: Editor HTML
article_title: Crear un correo electrónico con HTML personalizado
page_order: 2
description: "Este artículo de referencia explica cómo crear un correo electrónico con la plataforma Braze. Incluye buenas prácticas sobre cómo redactar tus mensajes, previsualizar tu contenido y planificar tu campaña o Canvas."
tool:
  - Campaigns
channel:
  - email
search_rank: 1
---

# Crear un correo electrónico con HTML personalizado {#create-an-email-with-custom-html}

> Los mensajes de correo electrónico son ideales para entregar contenido a tus usuarios en sus propios términos. También son herramientas excelentes para volver a captar a usuarios que incluso pueden haber desinstalado tu aplicación. Enviar mensajes de correo electrónico personalizados y adaptados mejorará la experiencia de tus usuarios y les ayudará a obtener el máximo valor de tu aplicación.

Para ver ejemplos de campañas de correo electrónico, consulta nuestros [casos de uso](https://www.braze.com/customers).

{% alert tip %}
Si es la primera vez que creas una campaña de correo electrónico, te recomendamos encarecidamente consultar estos cursos de Braze Learning:<br><br>
- [Adhesiones voluntarias y permisos de correo electrónico](https://learning.braze.com/messaging-channels-email)
- [Proyecto: Construir un programa básico de marketing por correo electrónico](https://learning.braze.com/project-build-a-basic-email-marketing-program)
{% endalert %}

## Paso 1: Elige dónde crear tu mensaje {#step-1-choose-where-to-build-your-message}

Usa campañas para mensajes simples y únicos. Usa Canvas para recorridos de usuario con múltiples pasos.

{% tabs %}
{% tab Campaign %}

1. Ve a **Messaging** > **Campaigns** y selecciona **Create Campaign**.
2. Selecciona **Email** o, para campañas dirigidas a múltiples canales, selecciona **Multichannel**.
3. Dale a tu campaña un nombre claro y significativo.
4. Añade [equipos]({{site.baseurl}}/user_guide/administer/global/user_management/teams/) y [etiquetas]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags/) según sea necesario.
   * Las etiquetas facilitan encontrar tus campañas y generar informes a partir de ellas. Por ejemplo, al usar el [Generador de informes]({{site.baseurl}}/user_guide/analytics/reports/report_builder/), puedes filtrar por etiquetas específicas.
5. Añade y nombra tantas variantes como necesites para tu campaña. Para más información sobre este tema, consulta [Pruebas multivariantes y A/B]({{site.baseurl}}/user_guide/messaging/ab_testing/).

{% alert tip %}
Si todos los mensajes de tu campaña van a ser similares o tener el mismo contenido, redacta tu mensaje antes de añadir variantes adicionales. Luego puedes elegir **Copy from Variant** en el desplegable **Add Variant**.
{% endalert %}
{% endtab %}
{% tab Canvas %}

1. [Crea tu Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/) usando el compositor de Canvas.
2. Después de configurar tu Canvas, añade un paso en el constructor de Canvas. Dale a tu paso un nombre claro y significativo.
3. Elige una [planificación de paso]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/delivery_and_entry_types/#schedule-delay) y especifica un retraso según sea necesario.
4. Filtra tu audiencia para este paso, según sea necesario. Puedes refinar aún más los destinatarios de este paso especificando segmentos y añadiendo filtros adicionales. Las opciones de audiencia se verificarán después del retraso, en el momento en que se envíen los mensajes.
5. Elige tu [comportamiento de avance]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/cloning_canvases/).
6. Elige cualquier otro canal de mensajería que desees combinar con tu mensaje.
{% endtab %}
{% endtabs %}

{% alert tip %}
Si planeas crear HTML personalizado y necesitas que los fondos se mantengan consistentes en la aplicación móvil de Gmail con el modo oscuro del dispositivo activado, consulta [Aplicación móvil de Gmail y modo oscuro](#gmail-dark-mode).
{% endalert %}

{% multi_lang_include drag_and_drop/drag_and_drop_access.md variable_name='email html editor' %}

## Paso 2: Selecciona tu experiencia de edición {#step-2-choose-your-template-and-compose-your-email}

Braze ofrece dos experiencias de edición al crear una campaña de correo electrónico: nuestro [editor de arrastrar y soltar]({{site.baseurl}}/dnd/) y nuestro editor HTML estándar. Elige el mosaico correspondiente a la experiencia de edición que prefieras.

![Elegir entre el editor de arrastrar y soltar, el editor HTML o plantillas para tu experiencia de edición de correo electrónico.]({% image_buster /assets/img_archive/choose_email_creation.png %}){: style="max-width:75%" }

Luego, puedes seleccionar una [plantilla de correo electrónico]({{site.baseurl}}/user_guide/channels/email/html_editor/#creating-an-email-template) existente, [cargar una plantilla]({{site.baseurl}}/user_guide/messaging/templates/email_templates/html_email_template/) desde un archivo (solo editor HTML) o usar una plantilla en blanco.

Si usas el editor HTML y necesitas que los colores de fondo se mantengan consistentes en la aplicación móvil de Gmail cuando el dispositivo está en modo oscuro, consulta [Aplicación móvil de Gmail y colores de fondo en modo oscuro](#gmail-dark-mode).

{% alert tip %}
Recomendamos seleccionar una experiencia de edición por campaña de correo electrónico. Por ejemplo, elige **HTML Classic** o **Block editor** en una sola campaña de correo electrónico en lugar de alternar entre editores.
{% endalert %}

## Paso 3: Redacta tu correo electrónico {#step-3-compose-your-email}

Después de seleccionar tu plantilla, verás un resumen de tu correo electrónico donde puedes ir directamente al editor de pantalla completa para redactar tu correo, cambiar tu información de envío y ver advertencias sobre capacidad de entrega o cumplimiento legal. Puedes alternar entre las pestañas HTML, clásica, texto plano y [AMP]({{site.baseurl}}/user_guide/channels/email/customize/amp_for_email/) mientras redactas.

![El botón «Regenerar desde HTML».]({% image_buster /assets/img_archive/regenerate_from_html.png %}){: style="max-width:30%;float:right;margin-left:15px;border:none;" }

Braze actualiza automáticamente la versión de texto plano a partir de la versión HTML hasta que detecta una edición en el texto plano. Después de que Braze detecta una edición, deja de actualizar el texto plano porque asume que realizaste cambios intencionales. Para restaurar la sincronización automática, ve a **Plaintext** y selecciona **Regenerate from HTML** (visible solo cuando el texto plano no se está sincronizando).

{% alert tip %}
Para añadir movimiento en un correo electrónico con una vista previa precisa, usa GIF en lugar de elementos que requieran JavaScript, ya que la mayoría de las bandejas de entrada no admiten JavaScript.
{% endalert %}


{% alert important %}
Braze elimina automáticamente los controladores de eventos HTML referenciados como atributos. Esto modifica el HTML, así que vuelve a revisar el correo electrónico después de terminar. Obtén más información sobre [controladores HTML](https://www.w3schools.com/tags/ref_eventattributes.asp).
{% endalert %}

{% alert tip %}
¿Necesitas ayuda para crear textos increíbles? Prueba usar el [asistente de redacción con inteligencia artificial]({{site.baseurl}}/user_guide/brazeai/operator/capabilities/#generate-copy). Introduce un nombre o descripción de producto y la IA generará textos de marketing similares a los escritos por humanos para usar en tus mensajes.

![Botón Lanzar el redactor con IA, ubicado en la pestaña Cuerpo del compositor de correo electrónico.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_email.png %}){: style="max-width:80%"}
{% endalert %}

¿Necesitas ayuda para crear mensajes de derecha a izquierda para idiomas como árabe y hebreo? Consulta [Crear mensajes de derecha a izquierda]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages/) para conocer las buenas prácticas.

### Aplicación móvil de Gmail y modo oscuro {#gmail-dark-mode}

La aplicación móvil de Gmail (Android e iOS) puede invertir los colores de fondo cuando el dispositivo está en modo oscuro. Esto puede romper diseños donde el fondo del correo electrónico debe coincidir con el borde de una imagen o un color de marca específico.

Para evitar esto, en la celda de tabla que necesita un fondo estable, usa un `linear-gradient` CSS de un solo color en lugar de `background-color`. Gmail tiene menos probabilidades de invertir ese tratamiento que un color de fondo plano.

Por ejemplo, para mantener un fondo blanco en una celda, usa esto:

```html
<td style="background-image: linear-gradient(#ffffff, #ffffff);">
```

Reemplaza `#ffffff` con el color que desees.

{% alert note %}
Este enfoque no se aplica de forma fiable solo a elementos `<table aria-label="Gmail mobile app and dark mode #gmail-dark-mode">`, así que establece el degradado en la celda en lugar de solo en la tabla.
  <caption>Gmail mobile app and dark mode</caption>
{% endalert %}

Para más información sobre la sintaxis de degradados, consulta [Degradados CSS en W3Schools](https://www.w3schools.com/css/css3_gradients.asp).

### Paso 3.1: Añade tu información de envío {#step-31-add-your-sending-information}

Después de terminar de diseñar y construir tu mensaje de correo electrónico, añade tu información de envío en **Sending Settings**.

1. En **Sending Info**, selecciona un correo electrónico como **From Display Name + Address**. También puedes personalizar esto seleccionando **Customize From Display Name + Address**.
2. Selecciona un correo electrónico como **Reply-To Address**. También puedes personalizar esto seleccionando **Customize Reply-To Address**.
3. A continuación, selecciona un correo electrónico como **BCC Address** para hacer tu correo visible a esta dirección.
4. Añade una línea del asunto a tu correo electrónico. Opcionalmente, también puedes añadir un preencabezado y un espacio en blanco después del preencabezado.

{% multi_lang_include alerts/tip_alerts.md alert='Liquid email display name and reply-to address' %}

Una vista previa en el panel derecho se completará con la información de envío que hayas añadido. Esta información también se puede actualizar yendo a **Settings** > **Email Preferences** > **Sending Configuration**.

#### Avanzado {#advanced}

En **Sending Settings** > **Advanced**, activa **inline CSS** para la compatibilidad más amplia con clientes. Si los mensajes se recortan o las imágenes se estiran a la altura de la fila, prueba desactivar temporalmente inline CSS. Algunas plantillas funcionan mejor sin inlining.

También puedes añadir personalización para encabezados de correo electrónico y extras de correo electrónico para enviar datos adicionales a otros proveedores de servicios de correo electrónico.

##### Archivos adjuntos de correo electrónico {#email-attachments}

También puedes añadir archivos adjuntos de correo electrónico mediante los siguientes métodos:

- **Cargar un archivo:** Arrastra y suelta o busca para cargar un archivo directamente desde tu computadora al correo electrónico. Braze valida el tipo y tamaño del archivo (hasta 2&nbsp;MB de forma predeterminada) antes de cargarlo, y luego estos archivos se cargan en la biblioteca de medios. Los archivos que superen el límite de 2&nbsp;MB no se pueden cargar.
- **Usar la biblioteca de medios:** Busca y selecciona entre los activos ya almacenados en la [biblioteca de medios]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/). Se admiten archivos PDF, documentos de Word, archivos de Excel y presentaciones de PowerPoint.
- **Añadir desde URL:** Introduce una URL que apunte al archivo y proporciona un nombre de archivo para mostrar. Dado que Braze no puede verificar el tamaño de URLs arbitrarias durante la composición del correo electrónico, el tamaño del archivo se aplica en el momento del envío. Ten en cuenta que Liquid no es compatible en este campo.

Consulta las [directrices de correo electrónico]({{site.baseurl}}/user_guide/channels/email/best_practices/email_guidelines/) para conocer las buenas prácticas específicas a considerar.

##### Encabezados de correo electrónico {#email-headers}

Para añadir encabezados de correo electrónico, selecciona **Add New Header**. Los encabezados de correo electrónico contienen información sobre el correo que se está enviando. Estos [pares clave-valor]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/key_value_pairs/) normalmente incluyen información del remitente, destinatario, protocolo de autenticación y enrutamiento. Braze añade automáticamente la información de encabezado requerida por RFC para que los correos electrónicos lleguen a los proveedores de bandeja de entrada.

Braze te permite la flexibilidad de añadir encabezados de correo electrónico adicionales según sea necesario para casos de uso avanzados. Hay algunos campos reservados que la plataforma Braze sobrescribirá durante el envío.

Evita usar las siguientes claves:

<style>
#reserved-fields td {
    word-break: break-word;
    width: 33%;
}
</style>

<table aria-label="Encabezados de correo electrónico" id="reserved-fields">
  <caption>Encabezados de correo electrónico</caption>
<thead>
  <tr>
    <th>Campos reservados</th>
    <th></th>
    <th></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>BCC</td>
    <td>dkim-signature</td>
    <td>Reply-To</td>
  </tr>
  <tr>
    <td>CC</td>
    <td>From</td>
    <td>Subject</td>
  </tr>
  <tr>
    <td>Content-Transfer-Encoding</td>
    <td>MIME-Version</td>
    <td>To</td>
  </tr>
  <tr>
    <td>Content-Type</td>
    <td>Received</td>
    <td>x-sg-eid</td>
  </tr>
  <tr>
    <td>DKIM-Signature</td>
    <td>received</td>
    <td>x-sg-id</td>
  </tr>
</tbody>
</table>

##### Añadir extras de correo electrónico {#adding-email-extras}

Los extras de correo electrónico te permiten enviar datos adicionales a otros proveedores de servicios de correo electrónico. Esto solo es aplicable para casos de uso avanzados, por lo que solo deberías usar extras de correo electrónico si tu empresa ya tiene esto configurado.

Para añadir extras de correo electrónico, ve a **Sending Info** y selecciona **Add New Extra**.

{% alert warning %}
El total de pares clave-valor añadidos no debe superar 1 KB. De lo contrario, los mensajes serán cancelados.
{% endalert %}

Los valores de extras de correo electrónico no se publican en Currents ni en Snowflake. Si buscas enviar metadatos adicionales o valores dinámicos a Currents o Snowflake, usa [`message_extras`]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters/message_extras/) en su lugar.

### Paso 3.2: Previsualiza y prueba tu mensaje {#step-3b-preview-and-test-your-message}

Después de terminar de redactar tu correo electrónico, pruébalo antes de enviarlo. Desde la parte inferior de la pantalla de resumen, selecciona **Preview and Test**.

Aquí puedes previsualizar cómo aparecerá tu correo electrónico en la bandeja de entrada de un cliente. Con **Preview as User** seleccionado, puedes previsualizar tu correo como un usuario aleatorio, seleccionar un usuario específico o crear un usuario personalizado. Esto te permite comprobar que tus llamadas de contenido conectado y personalización funcionan como deberían.

Luego, puedes usar **Copy preview link** para generar y copiar un enlace de vista previa compartible que muestre cómo se verá el correo electrónico para un usuario aleatorio. El enlace durará siete días antes de que necesite ser regenerado.

También puedes alternar entre las vistas de escritorio, móvil y texto plano para tener una idea de cómo aparecerá tu mensaje en diferentes contextos.

{% alert tip %}
¿Tienes curiosidad por saber cómo se ve tu correo electrónico para los usuarios en modo oscuro? Selecciona el interruptor **Dark Mode Preview** ubicado en la sección **Preview and Test** (solo editor de arrastrar y soltar). Si usas el editor HTML, aún puedes abordar el renderizado del modo oscuro en la aplicación móvil de Gmail con [Aplicación móvil de Gmail y modo oscuro](#gmail-dark-mode).
{% endalert %}

Cuando estés listo para una revisión final, selecciona **Test Send** y envía un mensaje de prueba a ti mismo o a un grupo de prueba para confirmar que el correo electrónico se muestra correctamente en diferentes dispositivos y clientes.

![Opción de envío de prueba y ejemplo de vista previa de correo electrónico al redactar tu correo.]({% image_buster /assets/img_archive/newEmailTest.png %})

Si ves algún problema con tu correo electrónico o quieres hacer cambios, selecciona **Edit Email** para volver al editor.

{% alert tip %}
Los clientes de correo electrónico que admiten texto de vista previa siempre extraen suficientes caracteres para llenar todo el espacio disponible de texto de vista previa. Sin embargo, esto puede dejarte en situaciones donde el texto de vista previa está incompleto o no optimizado.
<br><br>Para evitar esto, puedes crear un espacio en blanco después del texto de vista previa deseado para que los clientes de correo electrónico no extraigan otro texto o caracteres que distraigan en el contenido del sobre. Para hacerlo, añade una cadena de no-uniones de ancho cero (‌`&zwnj;`) y espacios de no separación (`&nbsp;`) después del texto de vista previa que deseas mostrar. <br><br>Cuando se añade al final de tu texto de vista previa en la sección de preencabezado, el siguiente fragmento de código para el editor HTML añadirá el espacio en blanco que buscas:<br><br>

```html
<div style="display: none; max-height: 0px; overflow: hidden;">&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;</div>
```

Para el editor de arrastrar y soltar, añade solo las no-uniones de ancho cero (‌`&zwnj;`) sin el formato `<div>` directamente en el preencabezado en la sección **Sending Settings**.
{% endalert %}

{% alert note %}
En la aplicación Apple Mail, los enlaces de imágenes en correos electrónicos HTML deben usar URLs `https://` para que se puedan hacer clic. Usa enlaces seguros para cualquier imagen envuelta en una etiqueta de anclaje cuando esperes clics de destinatarios de Apple Mail.
{% endalert %}

### Paso 3.3: Verifica errores de correo electrónico {#step-33-check-for-email-errors}

Antes de enviar, el editor señala problemas comunes:

- Nombre para mostrar del remitente y encabezado no configurados juntos
- Direcciones de remitente o responder a no válidas
- Claves de encabezado duplicadas
- Errores de sintaxis Liquid
- Content Blocks que incluyen un `<!DOCTYPE html>` completo
- El cuerpo del correo electrónico supera los 400&nbsp;KB
  - Apunta a [menos de 102&nbsp;KB]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/guidelines_and_tips/#email-size) para evitar recortes.
- Cuerpo o asunto en blanco
- Falta el enlace para cancelar suscripción
- El dominio del remitente no está en la lista de permitidos (los envíos se limitan considerablemente)

## Paso 4: Construye el resto de tu campaña o Canvas {#step-4-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab Campaign %}
A continuación, construye el resto de tu campaña. Consulta las siguientes secciones para obtener más detalles sobre cómo usar las herramientas de Braze para crear tu campaña de correo electrónico.

### Elige la planificación de entrega o el desencadenante {#choose-delivery-schedule-or-trigger}

Entrega correos electrónicos basándote en un horario planificado, una acción o un desencadenante de API. Para más información, consulta [Planificar tu campaña]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/).

{% alert note %}
Para campañas desencadenadas por API, cuando la acción desencadenante se establece en **Interact With Campaign**, seleccionar una opción de **Receive** como la interacción hará que tu nueva campaña se desencadene tan pronto como Braze marque la campaña seleccionada como enviada, incluso si ese mensaje rebota o no se entrega.
{% endalert %}

También puedes establecer la duración de la campaña, especificar [horas tranquilas]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours/) y configurar reglas de [limitación de frecuencia]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/#frequency-capping).

### Elige los usuarios objetivo {#choose-users-to-target}

A continuación, [dirige a los usuarios]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users/) eligiendo segmentos o filtros. Braze muestra una vista previa en vivo de la población del segmento, incluyendo cuántos usuarios son alcanzables por correo electrónico. La membresía exacta del segmento se calcula justo antes del envío.

{% multi_lang_include audience/target_audiences.md %}

También puedes elegir enviar tu campaña solo a usuarios que tengan un [estado de suscripción]({{site.baseurl}}/user_guide/channels/email/subscriptions/) específico, como aquellos que están suscritos y han optado por recibir correos electrónicos.

Opcionalmente, también puedes limitar la entrega a un número específico de usuarios dentro del segmento, o permitir que los usuarios reciban el mismo mensaje dos veces en caso de recurrencia de la campaña.

{% alert note %}
Al crear una nueva campaña de correo electrónico, el grupo de control se establece por defecto en 20 % y se puede ajustar o eliminar según sea necesario para tu campaña.
{% endalert %}

#### Campañas multicanal con correo electrónico y push {#multichannel-campaigns-with-email-and-push}

Para campañas multicanal dirigidas tanto a canales de correo electrónico como push, es posible que desees limitar tu campaña para que solo los usuarios que hayan optado explícitamente reciban el mensaje (excluyendo a los usuarios suscritos o que cancelaron su suscripción). Por ejemplo, supongamos que tienes tres usuarios con diferentes estados de adhesión voluntaria:

- **Usuario A** está suscrito a correo electrónico y tiene push habilitado. Este usuario no recibe el correo electrónico pero recibirá el push.
- **Usuario B** ha optado por recibir correo electrónico pero no tiene push habilitado. Este usuario recibirá el correo electrónico pero no recibe el push.
- **Usuario C** ha optado por recibir correo electrónico y tiene push habilitado. Este usuario recibirá tanto el correo electrónico como el push.

Para hacerlo, en **Audience Summary**, selecciona enviar esta campaña a «opted-in users only». Esta opción verificará que solo los usuarios que hayan optado recibirán tu correo electrónico, y Braze solo enviará tu push a los usuarios que tengan push habilitado de forma predeterminada.

{% alert important %}
Con esta configuración, no incluyas ningún filtro en el paso **Target Audiences** que limite la audiencia a un solo canal (por ejemplo, `Foreground Push Enabled = True` o `Email Subscription = Opted-In`).
{% endalert %}

### Elige eventos de conversión {#choose-conversion-events}

Braze te permite rastrear con qué frecuencia los usuarios realizan acciones específicas, [eventos de conversión]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events/), después de recibir una campaña. Puedes especificar cualquiera de las siguientes acciones como evento de conversión:

- Abre la aplicación
- Realiza una compra (puede ser una compra genérica o un artículo específico)
- Realiza un evento personalizado específico
- Abre el correo electrónico

Puedes permitir una ventana de hasta 30 días durante la cual Braze cuenta una conversión si el usuario realiza la acción especificada. Aunque Braze rastrea aperturas y clics automáticamente, puedes establecer el evento de conversión como una apertura o un clic para usar [Intelligent Selection]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_selection/).
{% endtab %}

{% tab Canvas %}
Si aún no lo has hecho, completa las secciones restantes de los componentes de tu Canvas. Para más detalles sobre cómo construir el resto de tu Canvas, implementar pruebas multivariantes e Intelligent Selection, y más, consulta el paso [Construir tu Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/#step-3-build-your-canvas) de nuestra documentación de Canvas.
{% endtab %}
{% endtabs %}

## Paso 5: Revisa y despliega {#step-5-review-and-deploy}

La sección final resume la campaña que diseñaste. Confirma todos los detalles relevantes y selecciona **Launch Campaign**.

Para saber cómo puedes acceder a los resultados de tus campañas de correo electrónico, consulta [Informes de correo electrónico]({{site.baseurl}}/user_guide/channels/email/reporting/).