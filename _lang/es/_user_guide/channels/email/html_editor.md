---
nav_title: Editor HTML
article_title: Crear un correo electrónico con HTML personalizado
page_order: 2
description: "Este artículo de referencia explica cómo crear un correo electrónico con la plataforma Braze. Incluye buenas prácticas sobre cómo redactar tus mensajes, previsualizar tu contenido y planificar tu Campaign o Canvas."
tool:
  - Campaigns
channel:
  - email
search_rank: 1
---

# Crear un correo electrónico con HTML personalizado {#create-an-email-with-custom-html}

> Los mensajes de correo electrónico son ideales para entregar contenido a tus usuarios en sus propios términos. También son herramientas excelentes para volver a captar a usuarios que incluso pueden haber desinstalado tu aplicación. Enviar mensajes de correo electrónico personalizados y adaptados mejorará la experiencia de tus usuarios y les ayudará a obtener el máximo valor de tu aplicación.

Para ver ejemplos de Campaigns de correo electrónico, consulta nuestros [casos de uso](https://www.braze.com/customers).

{% alert tip %}
Si es la primera vez que creas una Campaign de correo electrónico, te recomendamos encarecidamente consultar estos cursos de Braze Learning:<br><br>
- [Adhesiones voluntarias y permisos de correo electrónico](https://learning.braze.com/messaging-channels-email)
- [Proyecto: Construir un programa básico de marketing por correo electrónico](https://learning.braze.com/project-build-a-basic-email-marketing-program)
{% endalert %}

## Paso 1: Elige dónde crear tu mensaje {#step-1-choose-where-to-build-your-message}

Usa Campaigns para mensajería sencilla y única. Usa Canvas para recorridos de usuario con varios pasos.

{% tabs %}
{% tab Campaign %}

1. Ve a **Mensajería** > **Campaigns** y selecciona **Crear Campaign**.
2. Selecciona **Correo electrónico** o, para Campaigns dirigidas a múltiples canales, selecciona **Multicanal**.
3. Asigna a tu Campaign un nombre claro y significativo.
4. Añade [equipos]({{site.baseurl}}/user_guide/administer/global/user_management/teams) y [etiquetas]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags) según sea necesario.
   * Las etiquetas facilitan encontrar tus Campaigns y crear informes a partir de ellas. Por ejemplo, cuando utilizas el [generador de informes]({{site.baseurl}}/user_guide/analytics/reports/report_builder), puedes filtrar por etiquetas específicas.
5. Añade y nombra tantas variantes como necesites para tu Campaign. Para más información sobre este tema, consulta [Pruebas multivariante y A/B]({{site.baseurl}}/user_guide/messaging/ab_testing).

{% alert tip %}
Si todos los mensajes de tu Campaign van a ser similares o van a tener el mismo contenido, redacta tu mensaje antes de añadir variantes adicionales. Después, puedes elegir **Copiar de variante** en el desplegable **Añadir variante**.
{% endalert %}
{% endtab %}
{% tab Canvas %}

{% multi_lang_include messaging/canvas_message_step_setup.md %}
{% endtab %}
{% endtabs %}

{% alert tip %}
Si planeas crear HTML personalizado y necesitas que los fondos se mantengan consistentes en la aplicación móvil de Gmail con el modo oscuro del dispositivo activado, consulta [Aplicación móvil de Gmail y colores de fondo en modo oscuro](#gmail-dark-mode).
{% endalert %}

{% multi_lang_include drag_and_drop/drag_and_drop_access.md variable_name='email html editor' %}

## Paso 2: Selecciona tu experiencia de edición {#step-2-choose-your-template-and-compose-your-email}

Braze ofrece dos experiencias de edición al crear una Campaign de correo electrónico: nuestro [editor de arrastrar y soltar]({{site.baseurl}}/dnd) y nuestro editor HTML estándar. Elige el mosaico correspondiente a la experiencia de edición que prefieras.

![Elegir entre el editor de arrastrar y soltar, el editor HTML o plantillas para tu experiencia de edición de correo electrónico.]({% image_buster /assets/img_archive/choose_email_creation.png %}){: style="max-width:75%" }

Luego, puedes seleccionar una [plantilla de correo electrónico]({{site.baseurl}}/user_guide/messaging/templates/email_templates/email_template) existente, [cargar una plantilla]({{site.baseurl}}/user_guide/messaging/templates/email_templates/html_email_template) desde un archivo (solo editor HTML) o usar una plantilla en blanco.

Si usas el editor HTML y necesitas que los colores de fondo se mantengan consistentes en la aplicación móvil de Gmail cuando el dispositivo está en modo oscuro, consulta [Aplicación móvil de Gmail y colores de fondo en modo oscuro](#gmail-dark-mode).

{% alert tip %}
Recomendamos seleccionar una experiencia de edición por Campaign de correo electrónico. Por ejemplo, elige **HTML Classic** o **Block editor** en una sola Campaign de correo electrónico en lugar de alternar entre editores.
{% endalert %}

## Paso 3: Redacta tu correo electrónico {#step-3-compose-your-email}

Después de seleccionar tu plantilla, verás un resumen de tu correo electrónico donde puedes ir directamente al editor de pantalla completa para redactar tu correo electrónico, cambiar tu información de envío y ver advertencias sobre capacidad de entrega o cumplimiento legal. Puedes alternar entre las pestañas HTML, clásico, texto plano y [AMP]({{site.baseurl}}/user_guide/channels/email/customize/amp_for_email) mientras redactas.

![El botón "Regenerar desde HTML".]({% image_buster /assets/img_archive/regenerate_from_html.png %}){: style="max-width:30%;float:right;margin-left:15px;border:none;" }

Braze actualiza automáticamente la versión de texto plano a partir de la versión HTML hasta que detecta una edición en el texto plano. Una vez que Braze detecta una edición, deja de actualizar el texto plano porque asume que realizaste cambios intencionales. Para restaurar la sincronización automática, ve a **Texto plano** y selecciona **Regenerar desde HTML** (visible solo cuando el texto plano no se está sincronizando).

{% alert tip %}
Para añadir movimiento en un correo electrónico con una vista previa precisa, usa GIF en lugar de elementos que requieran JavaScript, ya que la mayoría de los buzones de entrada no son compatibles con JavaScript.
{% endalert %}


{% alert important %}
Braze elimina automáticamente los controladores de eventos HTML referenciados como atributos. Esto modifica el HTML, así que vuelve a revisar el correo electrónico cuando termines. Obtén más información sobre los [controladores HTML](https://www.w3schools.com/tags/ref_eventattributes.asp).
{% endalert %}

{% alert tip %}
¿Necesitas ayuda para crear un texto increíble? Prueba a usar el [asistente de redacción con IA]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#generate-copy). Introduce el nombre o la descripción de un producto y la IA generará un texto de marketing similar al humano para usar en tus mensajes.

![Botón para iniciar el redactor con IA, ubicado en la pestaña Cuerpo del creador de correos electrónicos.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_email.png %}){: style="max-width:80%"}
{% endalert %}

¿Necesitas ayuda para crear mensajes de derecha a izquierda para idiomas como árabe y hebreo? Consulta [Crear mensajes de derecha a izquierda]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages) para conocer las mejores prácticas.

### Aplicación móvil de Gmail y modo oscuro {#gmail-dark-mode}

La aplicación móvil de Gmail (Android e iOS) puede invertir los colores de fondo cuando el dispositivo está en modo oscuro. Eso puede romper los diseños en los que el fondo del correo electrónico debe coincidir con el borde de una imagen o un color de marca específico.

Para evitar esto, en la celda de la tabla que necesita un fondo estable, usa un `linear-gradient` CSS de un solo color en lugar de `background-color`. Gmail tiene menos probabilidades de invertir ese tratamiento que un color de fondo plano.

Por ejemplo, para mantener un fondo blanco en una celda, usa esto:

```html
<td style="background-image: linear-gradient(#ffffff, #ffffff);">
```

Reemplaza `#ffffff` con el color deseado.

{% alert note %}
Este enfoque no se aplica de forma fiable a los elementos `<table aria-label="Aplicación móvil de Gmail y modo oscuro #gmail-dark-mode">` por sí solos, así que establece el degradado en la celda en lugar de solo en la tabla.
  <caption>Aplicación móvil de Gmail y modo oscuro</caption>
{% endalert %}

Para más información sobre la sintaxis de degradados, consulta [Degradados CSS en W3Schools](https://www.w3schools.com/css/css3_gradients.asp).

### Paso 3.1: Añade tu información de envío {#step-31-add-your-sending-information}

Después de terminar de diseñar y construir tu mensaje de correo electrónico, añade tu información de envío en **Configuración de envío**.

{% multi_lang_include email/sending_info_steps.md %}

{% multi_lang_include alerts/tip_alerts.md alert='Liquid email display name and reply-to address' %}

Una vista previa en el panel derecho se completará con la información de envío que hayas añadido. Esta información también se puede actualizar yendo a **Configuración** > **Preferencias de correo electrónico** > **Configuración de envío**.

#### Avanzado {#advanced}

En **Configuración de envío** > **Avanzado**, activa **CSS en línea** para la mayor compatibilidad con clientes. Si los mensajes se recortan o las imágenes se estiran a la altura de la fila, prueba a desactivar temporalmente el CSS en línea (**off**). Algunas plantillas funcionan mejor sin la inserción de CSS.

También puedes añadir personalización para los encabezados de correo electrónico y extras de correo electrónico para enviar datos adicionales a otros proveedores de servicios de correo electrónico.

##### Archivos adjuntos de correo electrónico {#email-attachments}

También puedes añadir archivos adjuntos de correo electrónico mediante los siguientes métodos:

{% multi_lang_include email/attachment_upload_options.md %}

Consulta las [Directrices de correo electrónico]({{site.baseurl}}/user_guide/channels/email/best_practices/email_guidelines) para conocer las mejores prácticas específicas a tener en cuenta.

##### Encabezados de correo electrónico {#email-headers}

Para añadir encabezados de correo electrónico, selecciona **Añadir nuevo encabezado**. Los encabezados de correo electrónico contienen información sobre el correo electrónico que se envía. Estos [pares clave-valor]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/key_value_pairs) suelen incluir información del remitente, destinatario, protocolo de autenticación y enrutamiento. Braze añade automáticamente la información de encabezado requerida por RFC para que los correos electrónicos lleguen a los proveedores de buzón de entrada.

Braze te ofrece la flexibilidad de añadir encabezados de correo electrónico adicionales según sea necesario para casos de uso avanzados. Hay algunos campos reservados que la plataforma Braze sobrescribirá durante el envío.

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

Los extras de correo electrónico te permiten enviar datos adicionales a otros proveedores de servicios de correo electrónico. Esto solo es aplicable para casos de uso avanzados, por lo que solo debes usar extras de correo electrónico si tu empresa ya tiene esto configurado.

Para añadir extras de correo electrónico, ve a la **Información de envío** y selecciona **Añadir nuevo extra**.

{% alert warning %}
El total de pares clave-valor añadidos no debe superar 1 KB. De lo contrario, los mensajes serán cancelados.
{% endalert %}

Los valores de extras de correo electrónico no se publican en Currents ni en Snowflake. Si buscas enviar metadatos adicionales o valores dinámicos a Currents o Snowflake, usa [`message_extras`]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters/message_extras) en su lugar.

### Paso 3.2: Previsualiza y prueba tu mensaje {#step-3b-preview-and-test-your-message}

Después de terminar de redactar tu correo electrónico, pruébalo antes de enviarlo. Desde la parte inferior de la pantalla de resumen, selecciona **Vista previa y prueba**.

Aquí puedes previsualizar cómo aparecerá tu correo electrónico en el buzón de entrada de un cliente. Con **Previsualizar como usuario** seleccionado, puedes previsualizar tu correo electrónico como un usuario aleatorio, seleccionar un usuario específico o crear un usuario personalizado. Esto te permite verificar que tus llamadas de contenido conectado y personalización funcionan como deberían.

Luego, puedes **Copiar enlace de vista previa** para generar y copiar un enlace de vista previa que se puede compartir y que muestra cómo se verá el correo electrónico para un usuario aleatorio. Para más información, consulta [Vista previa compartible]({{site.baseurl}}/user_guide/messaging/governance/shareable_preview).

También puedes alternar entre las vistas de escritorio, móvil y texto plano para tener una idea de cómo aparecerá tu mensaje en diferentes contextos.

{% alert tip %}
¿Tienes curiosidad por saber cómo se ve tu correo electrónico para los usuarios en modo oscuro? Selecciona el interruptor **Vista previa en modo oscuro** ubicado en la sección **Vista previa y prueba** (solo en el editor de arrastrar y soltar). Si usas el editor HTML, aún puedes abordar el renderizado en modo oscuro de la aplicación móvil de Gmail con [Aplicación móvil de Gmail y modo oscuro](#gmail-dark-mode).
{% endalert %}

Cuando estés listo para una verificación final, selecciona **Envío de prueba** y envía un mensaje de prueba a ti mismo o a un grupo de prueba para confirmar que el correo electrónico se muestra correctamente en todos los dispositivos y clientes.

![Opción de envío de prueba y ejemplo de vista previa de correo electrónico al redactar tu correo electrónico.]({% image_buster /assets/img_archive/newEmailTest.png %})

Si ves algún problema con tu correo electrónico o deseas realizar cambios, selecciona **Editar correo electrónico** para volver al editor.

{% alert tip %}
Los clientes de correo electrónico que son compatibles con el texto de vista previa siempre extraen suficientes caracteres para llenar todo el espacio disponible del texto de vista previa. Sin embargo, esto puede dejarte en situaciones donde el texto de vista previa está incompleto o no optimizado.
<br><br>Para evitar esto, puedes crear espacio en blanco después del texto de vista previa deseado para que los clientes de correo electrónico no extraigan otro texto o caracteres distractores en el contenido del sobre. En la sección **Configuración de envío**, puedes seleccionar la casilla **Añadir espacio en blanco después del preencabezado** para añadir automáticamente espacio en blanco. <br><br>Alternativamente, si necesitas más control, puedes añadir manualmente una cadena de no-uniones de ancho cero (‌`&zwnj;`) y espacios de no separación (`&nbsp;`) después del texto de vista previa que deseas mostrar. <br><br>Cuando se añade al final de tu texto de vista previa en la sección del preencabezado, el siguiente fragmento de código para el editor HTML añadirá el espacio en blanco que buscas:<br><br>

```html
<div style="display: none; max-height: 0px; overflow: hidden;">&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;</div>
```

Para el editor de arrastrar y soltar, añade solo las no-uniones de ancho cero (‌`&zwnj;`) sin el formato `<div>` directamente en el preencabezado en la sección **Configuración de envío**.
{% endalert %}

{% alert note %}
En la aplicación Apple Mail, los enlaces de imagen en correos electrónicos HTML deben usar URL `https://` para que se puedan hacer clic. Usa enlaces seguros para cualquier imagen envuelta en una etiqueta de ancla cuando esperes clics de destinatarios de Apple Mail.
{% endalert %}

### Paso 3.3: Verifica errores de correo electrónico {#step-33-check-for-email-errors}

Antes del envío, el editor señala problemas comunes:

- El nombre para mostrar del remitente y el encabezado no están configurados juntos
- Direcciones de remitente o responder a no válidas
- Claves de encabezado duplicadas
- Errores de sintaxis Liquid
- Content Blocks que incluyen un `<!DOCTYPE html>` completo
- El cuerpo del correo electrónico supera los 400&nbsp;KB
  - Intenta mantener [menos de 102&nbsp;KB]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/guidelines_and_tips#email-size) para evitar recortes.
- Cuerpo o asunto vacío
- Enlace de cancelación de suscripción faltante
- El dominio del remitente no está en la lista de permitidos (envíos con restricción severa)

## Paso 4: Crea el resto de tu campaña o Canvas {#step-4-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab Campaign %}
A continuación, crea el resto de tu campaña. Consulta las siguientes secciones para obtener más información sobre cómo utilizar las herramientas de Braze para crear tu campaña de correo electrónico.

### Elige un calendario de entrega o desencadenante {#choose-delivery-schedule-or-trigger}

Entrega correos electrónicos en función de una hora programada, una acción o un desencadenante de API. Para más información, consulta [Programar tu campaña]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign).

{% alert note %}
Para las Campaigns activadas por API, cuando la acción desencadenante se establece en **Interactuar con Campaign**, seleccionar una opción **Recibir** como interacción hará que tu nueva campaña se desencadene en cuanto Braze marque la Campaign seleccionada como enviada, incluso si ese mensaje rebota o no se entrega.
{% endalert %}

También puedes establecer la duración de la campaña, especificar las [horas tranquilas]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours) y configurar reglas de [limitación de frecuencia]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#about-frequency-capping).

### Elige los usuarios objetivo {#choose-users-to-target}

A continuación, [segmenta a los usuarios]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users) eligiendo segmentos o filtros. Braze muestra una vista previa en vivo de la población del segmento, incluyendo cuántos usuarios son alcanzables a través del correo electrónico. La pertenencia exacta al segmento se calcula justo antes del envío.

{% multi_lang_include audience/target_audiences.md %}

También puedes optar por enviar tu campaña solo a usuarios que tengan un [estado de suscripción]({{site.baseurl}}/user_guide/channels/email/subscriptions) específico, como aquellos que están suscritos y han optado por recibir correo electrónico.

Opcionalmente, también puedes limitar la entrega a un número determinado de usuarios dentro del segmento, o permitir que los usuarios reciban el mismo mensaje dos veces en caso de que la campaña se repita.

{% alert note %}
Al crear una nueva campaña de correo electrónico, el grupo de control se establece de forma predeterminada en el 20 % y puede ajustarse o eliminarse según sea necesario para tu campaña.
{% endalert %}

#### Campaigns multicanal con correo electrónico y push {#multichannel-campaigns-with-email-and-push}

Para las Campaigns multicanal dirigidas tanto al canal de correo electrónico como al de push, es posible que quieras limitar tu campaña para que solo los usuarios que hayan optado explícitamente por participar reciban el mensaje (excluyendo a los usuarios suscritos o que hayan cancelado la suscripción). Por ejemplo, supongamos que tienes tres usuarios con diferentes estados de adhesión voluntaria:

{% multi_lang_include messaging/intelligent_channel_user_examples.md %}

Para hacerlo, en **Resumen de audiencia**, selecciona enviar esta campaña a "solo usuarios que han optado por participar". Esta opción comprobará que solo los usuarios que han optado por participar reciban tu correo electrónico, y Braze solo enviará tu push a los usuarios que tengan push habilitado de forma predeterminada.

{% alert important %}
Con esta configuración, no incluyas ningún filtro en el paso **Target Audiences** que limite la audiencia a un solo canal (por ejemplo, `Foreground Push Enabled = True` o `Email Subscription = Opted-In`).
{% endalert %}

### Elige eventos de conversión {#choose-conversion-events}

Braze te permite hacer un seguimiento de la frecuencia con la que los usuarios realizan acciones específicas, [eventos de conversión]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events), después de recibir una campaña. Puedes especificar cualquiera de las siguientes acciones como evento de conversión:

- Abre la aplicación
- Realiza una compra (puede ser una compra genérica o un artículo específico)
- Realiza un evento personalizado específico
- Abre el correo electrónico

Puedes permitir un periodo de hasta 30 días durante el cual Braze contabiliza una conversión si el usuario realiza la acción especificada. Aunque Braze hace un seguimiento automático de las aperturas y los clics, puedes establecer el evento de conversión como una apertura o un clic para usar [Optimizar con BrazeAI<sup>TM</sup>]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/variant_selection).
{% endtab %}

{% tab Canvas %}
Si aún no lo has hecho, completa las secciones restantes de los componentes de tu Canvas. Para obtener más información sobre cómo construir el resto de tu Canvas, incluidas las pruebas multivariante y [Optimizar con BrazeAI<sup>TM</sup>]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#optimize-canvas-variants-with-brazeai), consulta [Construir tu Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-2-build-your-canvas).
{% endtab %}
{% endtabs %}

## Paso 5: Revisar e implementar {#step-5-review-and-deploy}

La sección final resume la campaña que diseñaste. Confirma todos los detalles relevantes y selecciona **Lanzar Campaign**.

Para saber cómo puedes acceder a los resultados de tus Campaigns de correo electrónico, consulta [Informes de correo electrónico]({{site.baseurl}}/user_guide/channels/email/reporting).