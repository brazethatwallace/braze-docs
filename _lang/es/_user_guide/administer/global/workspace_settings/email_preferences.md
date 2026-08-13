---
nav_title: Preferencias de correo electrónico
article_title: Preferencias de correo electrónico
page_type: reference
page_order: 2
description: "Este artículo de referencia cubre las preferencias de correo electrónico en el panel de Braze, incluyendo configuraciones de envío, píxeles de seguimiento de apertura, páginas de suscripción y pies de página, y más."
tool: Dashboard
channel: email
alias: /email_preferences/
toc_headers: h2

---

# Preferencias de correo electrónico {#email-preferences}

> Preferencias de correo electrónico es donde puedes configurar ajustes específicos de correo electrónico saliente, como pies de página personalizados, páginas personalizadas de adhesión voluntaria y cancelación de suscripción, y más. Incluir estas opciones en tus correos electrónicos salientes crea una experiencia fluida y coherente para tus usuarios.

**Preferencias de correo electrónico** se encuentra en **Configuración** en el panel.

## Configuración de envío {#sending-configuration}

Los ajustes de correo electrónico en la sección **Configuración de envío** determinan qué detalles se incluyen en tus Campaigns de correo electrónico. En particular, estos ajustes están relacionados principalmente con lo que tu usuario ve cuando recibe un correo electrónico de Braze.

### Configuración de correo electrónico saliente {#outbound-email-settings}

Al configurar tus ajustes de correo electrónico, la configuración de correo electrónico saliente identifica qué nombre y direcciones de correo electrónico se utilizan cuando Braze envía correos electrónicos a tus usuarios.

Si necesitas añadir un nuevo dominio o grupo de IP (proveedor de envío) a tu espacio de trabajo, o eliminar uno de la lista disponible, ponte en contacto con tu administrador de éxito de cliente para obtener ayuda.

{% tabs local %}
{% tab Dirección del nombre para mostrar %}

En esta sección, puedes añadir los nombres y direcciones de correo electrónico que puedes utilizar cuando Braze envía correos electrónicos a tus usuarios. Los nombres para mostrar y las direcciones de correo electrónico están disponibles en las opciones de **Información de envío** mientras redactas tu Campaign de correo electrónico. Ten en cuenta que las actualizaciones realizadas en la configuración de correo electrónico saliente no afectan retroactivamente a los envíos existentes.

![Sección "Configuración de correo electrónico saliente" con campos para diferentes nombres para mostrar y dominios.]({% image_buster /assets/img/email_settings/display_name_address.png %})

{% alert note %}
Los clientes de Apple Mail no reconocen el símbolo `@` cuando se utiliza en un nombre para mostrar personalizado. Los diferentes proveedores de buzón controlan cómo se muestra la dirección del nombre para mostrar a sus usuarios, por lo que el nombre para mostrar puede aparecer de forma diferente según el cliente de correo electrónico.
{% endalert %}

#### Personalizar con Liquid {#personalize-with-liquid}

También puedes utilizar [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) en los campos **Nombre para mostrar del remitente**, **Parte local** y **Dominio** para crear dinámicamente una plantilla del nombre del remitente y la dirección de correo electrónico basándote en atributos personalizados. Ten en cuenta que para utilizar Liquid en el campo **Dominio**, debes ir a las opciones de **Información de envío** de una Campaign de correo electrónico y seleccionar la casilla **Personalizar nombre para mostrar del remitente + dirección**.

![Configuración de envío con campos para personalizar el nombre para mostrar del remitente, la dirección y el dominio.]({% image_buster /assets/img/email_settings/email_campaign_domain.png %})

Por ejemplo, puedes utilizar lógica condicional para enviar desde diferentes marcas o regiones:

{% raw %}
```liquid
{% if ${language} == 'en' %}
English Display Name
{% elsif ${language} == 'de' %}
German Display Name
{% else %}
Default to English Display Name
{% endif %}
```
{% endraw %}

{% endtab %}
{% tab Dirección de respuesta %}

Añadir una dirección de correo electrónico en esta sección te permite seleccionarla como dirección de respuesta para tu Campaign de correo electrónico. También puedes establecer una dirección de correo electrónico como predeterminada seleccionando **Establecer como predeterminada**. Estas direcciones de correo electrónico estarán disponibles en las opciones de **Información de envío** mientras redactas tu Campaign de correo electrónico.

![Sección "Dirección de respuesta" con campos para introducir múltiples direcciones de respuesta.]({% image_buster /assets/img/email_settings/reply_to_address.png %}){: style="max-width:75%;" }

{% alert note %}
Los dominios de envío de Braze no aceptan correo electrónico entrante. Si un destinatario responde a un correo electrónico enviado desde un dominio de envío configurado en Braze, su respuesta rebotará con un error `550 5.7.1 relaying denied`. La dirección de respuesta no necesita compartir el mismo dominio que la dirección del remitente. Si necesitas recibir respuestas, por ejemplo, para recopilar confirmaciones de invitaciones de calendario, utiliza un subdominio que no esté configurado para envío y que tenga un buzón de entrada configurado para aceptar correo.
{% endalert %}

#### Personalizar con Liquid

También puedes utilizar [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) en el campo **Dirección de respuesta** para crear dinámicamente una plantilla de la dirección de respuesta basándote en atributos personalizados. Por ejemplo, puedes utilizar lógica condicional para enviar respuestas a diferentes regiones o departamentos:

{% raw %}
```liquid
{% if {{custom_attribute.${region}}} == 'US' %}
{% assign address = "us-support@example.com" %}
{% elsif {{custom_attribute.${region}}} == 'EU' %}
{% assign address = "eu-support@example.com" %}
{% else %}
{% assign address = "global-support@example.com" %}{% endif %}{{address}}
```
{% endraw %}

{% alert tip %}
Si utilizas un bloque de contenido para rellenar la **Dirección de respuesta**, asegúrate de que el valor final renderizado sea una dirección de correo electrónico válida e incluya un `@`. Braze no puede validar esto cuando guardas la configuración porque el valor final no se conoce hasta el momento del envío.

- Si tu bloque de contenido almacena la parte local (el texto antes de `@`) y el dominio por separado, construye el campo como una sola dirección (por ejemplo, {% raw %}`{{content_blocks.${reply_to_local}}}@{{content_blocks.${reply_to_domain}}}`{% endraw %}).
{% endalert %}

{% endtab %}
{% tab Dirección CCO %}

Esta sección te permite gestionar las direcciones CCO que puedes añadir a los mensajes de correo electrónico salientes enviados desde Braze. Añadir una dirección CCO a un mensaje de correo electrónico envía una copia idéntica del mensaje que tu usuario recibe a tu buzón de entrada CCO. Esta es una herramienta útil para conservar copias de los mensajes que enviaste a tus usuarios para requisitos de cumplimiento o problemas de atención al cliente. Los correos electrónicos CCO no se incluyen en los informes ni en los análisis de correo electrónico.

Las direcciones CCO están disponibles para Amazon SES, SendGrid y SparkPost. Como alternativa a las direcciones CCO, recomendamos utilizar el [archivado de mensajes]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/message_archiving) para guardar una copia de los mensajes enviados a los usuarios con fines de archivado o cumplimiento.

{% multi_lang_include alerts/important_alerts.md alert='BCC address billable emails' %}

Después de añadir una dirección, estará disponible para seleccionarla al redactar un correo electrónico en Campaigns o pasos en Canvas. Selecciona **Establecer como predeterminada** junto a una dirección para que se seleccione de forma predeterminada al lanzar una nueva Campaign de correo electrónico o componente de Canvas. Para anular esto a nivel de mensaje, puedes seleccionar **Sin CCO** al configurar tu mensaje.

Si necesitas que todos los mensajes de correo electrónico enviados desde Braze incluyan una dirección CCO, puedes seleccionar la opción **Requerir una dirección CCO para todas tus Campaigns de correo electrónico**. Esto requerirá que selecciones una dirección predeterminada, que se seleccionará automáticamente en las nuevas Campaigns de correo electrónico o pasos en Canvas. La dirección predeterminada también se añadirá automáticamente a todos los mensajes activados a través de nuestra REST API. No es necesario cambiar la solicitud de API existente para incluir la dirección.

#### CCO dinámico {#dynamic-bcc}

Con el CCO dinámico, puedes utilizar Liquid en tu dirección CCO. Ten en cuenta que esta característica solo está disponible en **Preferencias de correo electrónico** y no se puede configurar en la propia Campaign. Solo se permite una dirección CCO por destinatario de correo electrónico.

Por ejemplo, puedes añadir {% raw %}`{{custom_attribute.${support_agent}}}`{% endraw %} como dirección CCO para los correos electrónicos de tu equipo de soporte.

![Sección de dirección CCO de la pestaña de configuración de correo electrónico con una dirección CCO que utiliza Liquid.]({% image_buster /assets/img/email_settings/dynamic_bcc.png %}){: style="max-width:90%;" }

{% endtab %}
{% endtabs %}

## Píxel de seguimiento de apertura {#open-tracking-pixel}

[![Curso de Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/email-open-tracking-pixel/){: style="float:right;width:120px;border:0;" class="noimgborder"}

El píxel de seguimiento de apertura de correo electrónico es una imagen invisible de 1 x 1&nbsp;px que se inserta automáticamente en el HTML de tu correo electrónico. Este píxel ayuda a Braze a detectar si tus usuarios han abierto tu correo electrónico. Cuando el cliente de correo electrónico de un usuario realiza una solicitud a nuestro píxel de seguimiento, la solicitud puede contener información como la dirección IP, el agente de usuario y la marca de tiempo. La información de apertura de correo electrónico puede ser muy útil, ya que te ayuda a determinar estrategias de marketing eficaces al comprender las tasas de apertura correspondientes.

### Ubicación {#placement}

El comportamiento predeterminado en Braze es añadir el píxel de seguimiento en la parte inferior de tu correo electrónico, normalmente en una etiqueta `<body>`. Para la mayoría de los usuarios, este es el lugar ideal para colocar el píxel.

Aunque el píxel ya está diseñado para causar la menor cantidad posible de cambios visuales, cualquier cambio visual no intencionado sería menos visible en la parte inferior de un correo electrónico. Este también es el comportamiento predeterminado para proveedores de correo electrónico como SendGrid y SparkPost.

Para reducir comportamientos inesperados, mantén Liquid dentro de las etiquetas `<html>`. Las etiquetas de nivel de documento anidadas o duplicadas pueden cambiar la forma en que se analiza el correo electrónico y dónde se coloca el píxel, lo que puede afectar al seguimiento de apertura y al diseño. Para más información, consulta [Uso de Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid).

### Actualizar la ubicación {#update-the-placement}

Braze actualmente permite anular la ubicación predeterminada del píxel de seguimiento de apertura del ESP (la última etiqueta en el `<body>` de un correo electrónico) para moverlo a la primera etiqueta en el `<body>`.

![Sección "Píxel de seguimiento de apertura" con las opciones para mover para SendGrid, SparkPost o Amazon SES.]({% image_buster /assets/img/open_pixel.png %}){: style="max-width:80%;" }

Para cambiar la ubicación:

1. En Braze, ve a **Configuración** > **Preferencias de correo electrónico**.
2. Selecciona una de las siguientes opciones: **Move for SendGrid**, **Move for SparkPost** o **Move for Amazon SES**
3. Selecciona **Guardar**.

Después de guardar, Braze envía instrucciones especiales al ESP para colocar el píxel de seguimiento de apertura en la parte superior de todos los correos electrónicos HTML.

{% alert important %}
La habilitación de SSL envuelve la URL del píxel de seguimiento con HTTPS en lugar de HTTP. Si tu SSL está mal configurado, puede afectar la eficacia del píxel de seguimiento.
{% endalert %}

{% alert important %}
El seguimiento de clics se aplica solo a los enlaces que comienzan con `http://` o `https://`. Los enlaces `mailto:` (por ejemplo, `mailto:support@example.com`) no se reescriben para el seguimiento.
{% endalert %}

## Encabezado list-unsubscribe {#list-unsubscribe}

{% alert note %}
Desde el 15 de junio de 2026, cuando el encabezado de cancelación de suscripción con un clic de list-unsubscribe está configurado para aplicarse a un grupo de suscripción específico, Braze ya no incluye el encabezado mailto en los correos electrónicos. Los usuarios que cancelan la suscripción a través del encabezado list-unsubscribe solo se dan de baja de ese grupo de suscripción específico, no de forma global.
{% endalert %}

Usar un encabezado list-unsubscribe permite a tus destinatarios cancelar fácilmente la suscripción de correos electrónicos de marketing mostrando un botón **Unsubscribe** dentro de la interfaz del buzón de correo, y no en el cuerpo del mensaje.

Los envíos de prueba normalmente no incluyen encabezados list-unsubscribe. Si el encabezado en vivo aparece depende del proveedor de buzón de correo y se basa en la reputación: una reputación del remitente más fuerte generalmente mejora la visibilidad.

![Interfaz del buzón de correo del cliente de correo electrónico con una opción de cancelar suscripción junto al mensaje, donde list-unsubscribe aparece fuera del cuerpo del mensaje.]({% image_buster /assets/img_archive/list_unsub_img1.png %}){: style="float:right;max-width:60%;margin-left:15px;"}

Cuando un destinatario selecciona **Unsubscribe**, el proveedor de buzón de correo envía la solicitud de cancelación de suscripción al destino definido en el encabezado del correo electrónico.

Habilitar list-unsubscribe es una buena práctica de capacidad de entrega y un requisito en algunos de los principales proveedores de buzón de correo. Anima a los usuarios finales a eliminarse de forma segura de los mensajes no deseados, en lugar de presionar el botón de correo no deseado en un cliente de correo electrónico, lo cual es perjudicial para la reputación de envío y la capacidad de entrega del correo electrónico.

Al [administrar tus suscripciones en Gmail](https://support.google.com/mail/answer/15621070?sjid=2292320204527911296-NC), Gmail también puede extraer el enlace de cancelación de suscripción del cuerpo del mensaje, pero prioriza el list-unsubscribe si está presente en el encabezado.

### ¿Desactivar el encabezado list-unsubscribe elimina el botón Cancelar suscripción de Gmail? {#does-turning-off-the-list-unsubscribe-header-remove-the-gmail-unsubscribe-button}

No. Desactivar la configuración del encabezado list-unsubscribe de Braze elimina el encabezado `List-Unsubscribe` de los mensajes que Braze envía, pero no controla si Gmail muestra una opción de **Unsubscribe** en la interfaz del buzón de correo. Como se mencionó en la sección anterior, Gmail aún puede mostrar una opción de cancelación de suscripción a partir de enlaces en el cuerpo del mensaje o usar otra lógica del proveedor. Si el encabezado aparece en el mensaje sin formato es independiente de si Gmail muestra una opción de cancelación de suscripción a los destinatarios. Para más información, consulta las [preguntas frecuentes sobre las directrices para remitentes de correo electrónico de Gmail](https://support.google.com/a/answer/14229414).

### Soporte de proveedores de buzón de correo {#mailbox-provider-support}

La siguiente tabla resume el soporte de los proveedores de buzón de correo para el encabezado "mailto:", la URL de list-unsubscribe y la cancelación de suscripción con un clic ([RFC 8058](https://datatracker.ietf.org/doc/html/rfc8058)).

| Encabezado list-unsubscribe | Encabezado mailto: | URL de list-unsubscribe | Cancelación de suscripción con un clic (RFC 8058) |
| ----- | --- | --- | --- |
| Gmail | Compatible* | Compatible | Compatible |
| Gmail Mobile | No compatible | No compatible | No compatible |
| Apple Mail | Compatible | No compatible | No compatible |
| Outlook.com | Compatible | No compatible | No compatible |
| Yahoo! Mail | Compatible* | No compatible | Compatible |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Soporte de proveedores de buzón de correo" }

_*Yahoo y Gmail eventualmente dejarán de usar el encabezado "mailto:" y solo admitirán la cancelación con un clic._

Mostrar el encabezado es determinado en última instancia por el proveedor de buzón de correo. Para verificar si el encabezado list-unsubscribe está incluido en el correo electrónico sin formato (texto) para el destinatario en Gmail, haz lo siguiente:

1. Selecciona **Show Original** en el correo electrónico. Esto abre una nueva pestaña con la versión sin formato del correo electrónico y sus encabezados.
2. Busca "List-Unsubscribe". Para la cancelación de suscripción con un clic, muchos proveedores también incluyen un encabezado "List-Unsubscribe-Post". Confirma que ambos aparezcan en el mensaje sin formato cuando esperas que la cancelación con un clic esté disponible.

Si el encabezado está en la versión sin formato del correo electrónico pero no se muestra, el proveedor de buzón de correo ha decidido no mostrar la opción de cancelación de suscripción, lo que significa que no tenemos más información sobre por qué el proveedor de buzón de correo no muestra el encabezado. Ver el encabezado list-unsubscribe depende en última instancia de la reputación. En la mayoría de los casos, cuanto mejor sea tu reputación del remitente con el proveedor de buzón de correo, más probable es que aparezca el encabezado list-unsubscribe.

### Encabezado de cancelación de suscripción de correo electrónico en espacios de trabajo {#email-unsubscribe-header-in-workspaces}

![Seleccionando "usuarios que están suscritos o con adhesión voluntaria" para los usuarios a los que enviar.]({% image_buster /assets/img/email_settings/email_unsub_header_workspaces.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

Cuando la característica de encabezado de cancelación de suscripción de correo electrónico está activada, esta configuración se aplica a todo el espacio de trabajo, no a nivel de empresa. Se agrega a Campaigns y Canvas que están configurados para enviar a usuarios que están suscritos o con adhesión voluntaria, o usuarios con adhesión voluntaria en el paso **Target Audience** de los constructores de Campaigns y Canvas.

Al usar el "valor predeterminado del espacio de trabajo", Braze no agrega el encabezado de cancelación de suscripción con un clic para Campaigns que se consideran transaccionales, que están configuradas para "enviar a todos los usuarios, incluidos los usuarios cancelados". Para anular esto y agregar el encabezado de cancelación de suscripción con un clic al enviar a usuarios cancelados, puedes seleccionar **Unsubscribe globally from all emails** en la configuración de list-unsubscribe con un clic a nivel de mensaje.

### Encabezado list-unsubscribe predeterminado {#default-list-unsubscribe-header}

{% alert important %}
Gmail tiene la intención de que los remitentes implementen la cancelación de suscripción con un clic para todos sus mensajes comerciales y promocionales salientes a partir del 1 de junio de 2024. Para más información, consulta las [directrices para remitentes de Gmail](https://support.google.com/mail/answer/81126?hl=en#subscriptions&zippy=%2Crequirements-for-sending-or-more-messages-per-day:~:text=Make%20it%20easy%20to%20unsubscribe) y las [preguntas frecuentes sobre las directrices para remitentes de correo electrónico de Gmail](https://support.google.com/a/answer/14229414#zippy=%2Cwhat-time-range-or-duration-is-used-when-calculating-spam-rate%2Cif-the-list-header-is-missing-is-the-message-body-checked-for-a-one-click-unsubscribe-link%2Cif-unsubscribe-links-are-temporarily-unavailable-due-to-maintenance-or-other-reasons-are-messages-flagged-as-spam%2Ccan-a-one-click-unsubscribe-link-to-a-landing-or-preferences-page%2Cwhat-is-a-bulk-sender%2Chow-can-bulk-senders-make-sure-theyre-meeting-the-sender-guidelines%2Cdo-the-sender-guidelines-apply-to-messages-sent-to-google-workspace-accounts%2Cdo-the-sender-guidelines-apply-to-messages-sent-from-google-workspace-accounts%2Cwhat-happens-if-senders-dont-meet-the-requirements-in-the-sender-guidelines%2Cif-messages-are-rejected-because-they-dont-meet-the-sender-guidelines-do-you-send-an-error-message-or-other-alert%2Cwhat-happens-when-sender-spam-rate-exceeds-the-maximum-spam-rate-allowed-by-the-guidelines%2Cwhat-is-the-dmarc-alignment-requirement-for-bulk-senders%2Cif-messages-fail-dmarc-authentication-can-they-be-delivered-using-ip-allow-lists-or-spam-bypass-lists-or-will-these-messages-be-quarantined%2Ccan-bulk-senders-get-technical-support-for-email-delivery-issues%2Cdo-all-messages-require-one-click-unsubscribe:~:text=for%20mitigations.-,Unsubscribe%20links,-Do%20all%20messages). Yahoo anunció un cronograma de principios de 2024 para los requisitos actualizados. Para más información, consulta [Más seguro, menos correo no deseado: aplicando estándares de correo electrónico para una mejor experiencia](https://blog.postmaster.yahooinc.com/).
{% endalert %}

Para usar la característica de cancelación de suscripción de Braze para procesar cancelaciones de suscripción directamente, selecciona **Include a one-click list-unsubscribe (mailto and HTTP) email header for emails sent to subscribed or opted-in users** y selecciona **Braze default** como la URL estándar de Braze y mail-to.

![Opción para incluir automáticamente un encabezado list-unsubscribe para correos electrónicos enviados a usuarios suscritos o con adhesión voluntaria.]({% image_buster /assets/img/email_settings/email_unsubscribe_header.png %})

Braze admite las siguientes versiones del encabezado list-unsubscribe:

| Versión de list-unsubscribe | Descripción |
| ----- | --- |
| Un clic (RFC 8058) | Ofrece una forma sencilla para que los destinatarios cancelen la suscripción de correos electrónicos con un solo clic. Este es un requisito de Yahoo y Gmail para remitentes masivos. |
| URL de list-unsubscribe o HTTPS | Proporciona a los destinatarios un enlace que los dirige a una página web donde pueden cancelar la suscripción. |
| Mailto | Especifica una dirección de correo electrónico como destino para que el mensaje de solicitud de cancelación de suscripción sea enviado del destinatario a la marca. <br><br> _Para procesar solicitudes de cancelación de suscripción por mailto list-unsubscribe, dichas solicitudes necesitan incluir la dirección de correo electrónico tal como está almacenada en Braze para el usuario final que está cancelando la suscripción. Esto puede ser proporcionado por la dirección "from" del correo electrónico desde donde el usuario final está cancelando la suscripción, el asunto codificado o el cuerpo codificado del correo electrónico recibido por el usuario final del cual está cancelando la suscripción. En casos muy limitados, algunos proveedores de buzón de correo no se adhieren al protocolo [RFC 2368](https://datatracker.ietf.org/doc/html/rfc2368), lo que resulta en que la dirección de correo electrónico no se pase correctamente. Esto puede llevar a que una solicitud de cancelación de suscripción no pueda ser procesada en Braze._ |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Encabezado list-unsubscribe predeterminado" }

Cuando Braze recibe una solicitud de list-unsubscribe de un usuario a través de cualquiera de los métodos del [encabezado list-unsubscribe predeterminado](#default-list-unsubscribe-header), el estado de suscripción global de correo electrónico de este usuario se establece como cancelado. Si no hay coincidencia, Braze no procesa esta solicitud.

### Cancelación de suscripción con un clic {#one-click-unsubscribe}

Usar la cancelación de suscripción con un clic para el encabezado list-unsubscribe ([RFC 8058](https://datatracker.ietf.org/doc/html/rfc8058)) se enfoca en proporcionar una forma fácil para que los destinatarios cancelen la suscripción de correos electrónicos.

### Cancelación de suscripción con un clic a nivel de mensaje {#message-level-one-click-list-unsubscribe}

La configuración de cancelación de suscripción con un clic a nivel de mensaje anula la característica de encabezado de cancelación de suscripción de correo electrónico configurada para los espacios de trabajo. Aplica el comportamiento de cancelación de suscripción con un clic por Campaign o paso en Canvas para los siguientes usos:

- Agregar una cancelación de suscripción con un clic de Braze para un grupo de suscripción específico para admitir múltiples marcas/listas dentro de un espacio de trabajo
- Alternar entre la cancelación de suscripción predeterminada de Braze o una URL personalizada
- Agregar tu URL personalizada de cancelación de suscripción con un clic
- Omitir la cancelación de suscripción con un clic en este mensaje

{% alert note %}
La configuración de cancelación de suscripción con un clic a nivel de mensaje solo está disponible cuando se usa el editor de arrastrar y soltar y el editor HTML actualizado. Si estás usando el editor HTML anterior, cambia al editor HTML actualizado para usar esta característica.
{% endalert %}

En tu editor de correo electrónico, ve a **Sending Settings** > **Sending Info**. Selecciona entre las siguientes opciones:

- **Use workspace default**: Usa la configuración del **Email Unsubscribe Header** establecida en **Email Preferences**. Cualquier cambio realizado en esta configuración se aplica a todos los mensajes.
- **Unsubscribe globally from all emails**: Usa el encabezado predeterminado de cancelación de suscripción con un clic de Braze. Los usuarios que hacen clic en el botón de cancelar suscripción tienen su estado de suscripción global de correo electrónico establecido como "Unsubscribed".
- **Unsubscribe from specific subscription group**: Usa el grupo de suscripción especificado. Braze cancela la suscripción de los usuarios que hacen clic en el botón de cancelar suscripción del grupo de suscripción seleccionado.
    - Al seleccionar un grupo de suscripción, agrega el filtro **Subscription Group** en **Target Audiences** para dirigirte solo a los usuarios que están suscritos a este grupo específico. El grupo de suscripción seleccionado para la cancelación de suscripción con un clic debe coincidir con el grupo de suscripción al que te estás dirigiendo. Si hay una discrepancia en el grupo de suscripción, puedes correr el riesgo de enviar a un usuario que está intentando cancelar la suscripción de un grupo de suscripción del que ya está cancelado.

{% alert important %}
La configuración **Unsubscribe from specific subscription group** solo se aplica al encabezado list-unsubscribe con un clic. El encabezado mailto list-unsubscribe no se ve afectado al seleccionar esta opción. Esto significa que un destinatario que cancela la suscripción usando este método registra una cancelación de suscripción global, no una cancelación del grupo de suscripción específico. Para excluir el encabezado mailto list-unsubscribe de cancelar globalmente la suscripción de los usuarios, al seleccionar esta configuración, ponte en contacto con [soporte de Braze]({{site.baseurl}}/support_contact).
{% endalert %}

- **Custom**: Agrega tu URL personalizada de cancelación de suscripción con un clic para que proceses las cancelaciones de suscripción directamente.
- **Exclude unsubscribe**

{% alert important %}
Excluir la cancelación de suscripción con un clic o cualquier mecanismo de cancelación de suscripción solo debe hacerse para mensajería transaccional, como restablecimientos de contraseña, recibos y correos electrónicos de confirmación.
{% endalert %}

Ajustar esta configuración anula el comportamiento predeterminado para la cancelación de suscripción con un clic de list-unsubscribe en este correo electrónico.

![Ajustes de envío en el editor de correo electrónico con opciones de cancelación de suscripción con un clic a nivel de mensaje, incluyendo valor predeterminado del espacio de trabajo y URL personalizada.]({% image_buster /assets/img/email_settings/one_click_list_unsubscribe_message_level.png %}){: style="max-width:70%;"}

#### Requisitos {#requirements}

Si estás enviando correos electrónicos usando tu propia funcionalidad personalizada de cancelación de suscripción, debes cumplir con los siguientes requisitos para asegurarte de que la URL de cancelación de suscripción con un clic que configuraste esté de acuerdo con RFC 8058:

* La URL debe poder manejar solicitudes POST de cancelación de suscripción.
* La URL debe comenzar con `https://`.
* La URL no debe devolver una redirección HTTPS ni un cuerpo. Los enlaces de cancelación de suscripción con un clic que van a una página de destino u otro tipo de página web no cumplen con RFC 8058.
* Las solicitudes POST no deben establecer cookies.

Selecciona **Custom list-unsubscribe header** para agregar tu propio endpoint de cancelación de suscripción con un clic configurado, y un "mailto:" opcional. Braze requiere una entrada para la URL para admitir un encabezado list-unsubscribe personalizado porque la cancelación de suscripción con un clic HTTP es un requisito de Yahoo y Gmail para remitentes masivos.

![Preferencias de correo electrónico con campos de encabezado list-unsubscribe personalizado para una URL de cancelación de suscripción con un clic y un mailto opcional.]({% image_buster /assets/img/email_settings/email_unsubscribe_header_custom.png %}){: style="max-width:80%;"}

## Añadir prefijos a las líneas de asunto del correo electrónico {#append-email-subject-lines}

Usa el conmutador para incluir "[TEST]" y "[SEED]" en las líneas de asunto de tus correos electrónicos de prueba y semilla. Esto puede ayudar a identificar cualquier Campaign de correo electrónico enviada como prueba.

![Conmutador de preferencias de correo electrónico del espacio de trabajo que añade los prefijos TEST y SEED a las líneas de asunto de los correos electrónicos de prueba y semilla.]({% image_buster /assets/img/email_settings/test_and_seed_email_subject_line.png %}){: style="max-width:70%;"}

## CSS en línea en correos electrónicos nuevos de forma predeterminada {#inline-css-on-new-emails-by-default}

El CSS en línea es una técnica que aplica automáticamente estilos CSS en línea para tus correos electrónicos y correos electrónicos nuevos. Para algunos clientes de correo electrónico, esto puede mejorar la forma en que se renderizan tus correos electrónicos.

Cambiar esta configuración no afecta a ninguno de tus mensajes de correo electrónico ni plantillas existentes. Puedes anular este valor predeterminado en cualquier momento mientras redactas mensajes o plantillas. Para más información, consulta [CSS en línea]({{site.baseurl}}/user_guide/channels/email/html_editor/css_inline).

## Resuscribir usuarios cuando cambia su correo electrónico {#resubscribe-users-when-their-email-changes}

Puedes resuscribir automáticamente a los usuarios cuando cambian su dirección de correo electrónico. Por ejemplo, si un usuario del espacio de trabajo que previamente canceló su suscripción cambia su dirección de correo electrónico a una que no está en la lista de cancelación de suscripción de Braze, se resuscribe automáticamente.

![Configuración del espacio de trabajo que resuscribe automáticamente a los usuarios cuando cambia su dirección de correo electrónico.]({% image_buster /assets/img/email_settings/resubscribe_users.png %}){: style="max-width:90%;" }

## Páginas de suscripción y pies de página {#subscription-pages-and-footers}

{% tabs local %}
{% tab Pie de página personalizado %}

Para correos electrónicos comerciales, la [Ley CAN-SPAM](https://en.wikipedia.org/wiki/CAN-SPAM_Act_of_2003) exige que todos los correos electrónicos comerciales incluyan una opción para cancelar suscripción. Con la configuración de pie de página personalizado, puedes cumplir con la Ley CAN-SPAM y, al mismo tiempo, personalizar el pie de página de exclusión de correo electrónico. Para mantener el cumplimiento, debes añadir tu pie de página personalizado a todos los correos electrónicos enviados como parte de Campaigns en este espacio de trabajo.

Ten en cuenta los siguientes requisitos al crear un pie de página personalizado para tu mensajería por correo electrónico:
- Debe incluir una URL de cancelación de suscripción y una dirección postal física.
- Debe tener un tamaño inferior a 100 KB.

![Editor de pie de página de correo electrónico personalizado con campos de enlace de cancelación de suscripción y dirección postal para el cumplimiento de CAN-SPAM.]({% image_buster /assets/img/email_settings/custom_footer.png %})

Para la creación de plantillas Liquid de pie de página personalizado, consulta [Pies de página personalizados]({{site.baseurl}}/user_guide/channels/email/subscriptions#changing-email-subscriptions).

{% endtab %}
{% tab Página de cancelación de suscripción personalizada %}

Braze te permite configurar una **página de cancelación de suscripción personalizada** con tu propio HTML. Esta página aparece después de que un usuario haya seleccionado cancelar la suscripción en la parte inferior de un correo electrónico. Ten en cuenta que esta página debe tener un tamaño inferior a 750 KB.

![Editor HTML de página de cancelación de suscripción personalizada y vista previa de la página que se muestra después de que un usuario cancela la suscripción de correo electrónico.]({% image_buster /assets/img/email_settings/custom_unsubscribe.png %})

{% multi_lang_include email/external_font_domains.md page_type='unsubscribe' %}

{% endtab %}
{% tab Página de adhesión voluntaria personalizada %}

Puedes crear una página de adhesión voluntaria personalizada utilizando tu propio HTML. Incluir esto en tu correo electrónico puede ser especialmente beneficioso si deseas que tu marca y mensaje se mantengan consistentes a lo largo del ciclo de vida de tu usuario. Ten en cuenta que esta página debe tener un tamaño inferior a 750 KB.

![Editor HTML de página de adhesión voluntaria personalizada y vista previa para la confirmación de suscripción de correo electrónico con marca.]({% image_buster /assets/img/email_settings/custom_opt_in.png %})

{% multi_lang_include email/external_font_domains.md page_type='opt-in' %}

{% endtab %}
{% endtabs %}

{% alert tip %}
Cuando estés en la sección **Vista previa** de una página de suscripción o pie de página, selecciona **Copiar enlace de vista previa** para generar y copiar un enlace de vista previa que se puede compartir y que muestra cómo se ve el pie de página del correo electrónico, la página de cancelación de suscripción o la página de adhesión voluntaria para un usuario aleatorio. Para más información, consulta [Vista previa compartible]({{site.baseurl}}/user_guide/messaging/governance/shareable_preview).
{% endalert %}

## Preguntas frecuentes {#frequently-asked-questions}

### Cancelación de suscripción con un clic

{% details ¿Puede la URL de cancelación de suscripción con un clic (a través del encabezado list-unsubscribe) enlazar a un centro de preferencias? %}
No, eso no cumple con el RFC 8058, lo que significa que no cumplirás con el requisito de cancelación de suscripción con un clic de Yahoo y Gmail.
{% enddetails %}

{% details ¿Por qué recibo el mensaje de error "Your email body does not include an unsubscribe link" al crear mi centro de preferencias? %}
Un centro de preferencias no se considera un enlace de cancelación de suscripción. Tus destinatarios de correo electrónico deben tener la opción de cancelar la suscripción de cualquier correo electrónico comercial para cumplir con la normativa CAN-SPAM.
{% enddetails %}

{% details ¿Necesito editar Campaigns y Canvas de correo electrónico anteriores para aplicar la configuración de cancelación de suscripción con un clic después de habilitarla? %}
Si no tienes ninguno de los casos de uso para la configuración de cancelación de suscripción con un clic a nivel de mensaje, no se requiere ninguna acción siempre que la configuración esté activada en **Preferencias de correo electrónico**. Braze añade automáticamente los encabezados de cancelación de suscripción con un clic a todos los mensajes de marketing y promocionales salientes. Sin embargo, si necesitas configurar el comportamiento de cancelación de suscripción con un clic a nivel de mensaje individual, debes actualizar las Campaigns de correo electrónico y los pasos en Canvas anteriores de forma correspondiente.
{% enddetails %}

{% details Puedo ver el encabezado list-unsubscribe y de cancelación de suscripción con un clic en el mensaje original o en los datos sin procesar, pero ¿por qué no veo el botón Cancelar suscripción en Gmail o Yahoo? %}
Gmail y Yahoo deciden en última instancia si muestran o no el encabezado list-unsubscribe o de cancelación de suscripción con un clic. Para remitentes nuevos o remitentes con baja reputación del remitente, esto puede ocasionar que el botón de cancelación de suscripción no se muestre.
{% enddetails %}

{% details ¿El encabezado personalizado de cancelación de suscripción con un clic es compatible con Liquid? %}
Sí, Liquid y la lógica condicional son compatibles para permitir URL dinámicas de cancelación de suscripción con un clic en el encabezado.
{% enddetails %}

{% alert tip %}
Si añades lógica condicional, evita tener valores de salida que agreguen espacios en blanco a tu URL, ya que Braze no elimina estos espacios en blanco.
{% endalert %}

### Cancelación de suscripción con un clic a nivel de mensaje

{% details Si añado los encabezados de correo electrónico para la cancelación con un clic de forma manual, y tengo activado el encabezado de cancelación de suscripción de correo electrónico, ¿cuál es el comportamiento esperado? %}
Los encabezados de correo electrónico añadidos para la cancelación de suscripción con un clic se aplican a todos los envíos futuros de esta Campaign.
{% enddetails %}

{% details ¿Por qué los grupos de suscripción deben coincidir entre las variantes del mensaje para poder lanzar? %}
Para una Campaign con pruebas A/B, Braze envía aleatoriamente a un usuario una de las variantes. Si tienes dos grupos de suscripción diferentes configurados en la misma Campaign (la variante A está configurada con el grupo de suscripción A, y la variante B está configurada con el grupo de suscripción B), no podemos garantizar que los usuarios que solo están suscritos al grupo de suscripción B reciban la variante B. Puede haber un escenario en el que los usuarios cancelen la suscripción de un grupo de suscripción del que ya se habían dado de baja.
{% enddetails %}

{% details La configuración del encabezado de cancelación de suscripción de correo electrónico está desactivada en Preferencias de correo electrónico, pero en la información de envío de mi Campaign, la configuración de cancelación de suscripción con un clic está establecida en "Usar predeterminado del espacio de trabajo". ¿Es un error? %}
No. Si la configuración del espacio de trabajo está desactivada y la configuración del mensaje está establecida en **Usar predeterminado del espacio de trabajo**, entonces Braze sigue lo que está configurado en **Preferencias de correo electrónico**. Esto significa que no añadimos el encabezado de cancelación de suscripción con un clic para la Campaign.
{% enddetails %}

{% details ¿Qué sucede si se archiva un grupo de suscripción? ¿Esto afecta la cancelación de suscripción con un clic en los correos electrónicos enviados? %}
Si un grupo de suscripción referenciado en **Información de envío** para la cancelación con un clic se archiva, Braze sigue procesando las cancelaciones de suscripción con un clic. El grupo de suscripción ya no aparece en el panel (filtro de Segment, perfil de usuario y áreas similares).
{% enddetails %}

{% details ¿La configuración de cancelación de suscripción con un clic está disponible para plantillas de correo electrónico? %}
No, actualmente no tenemos planes de añadir esto para plantillas de correo electrónico, ya que estas plantillas no están asignadas a un dominio de envío. {% multi_lang_include product_feedback_cta.md context="gap" feature="per-domain sending for email templates" %}
{% enddetails %}

{% details ¿Esta característica verifica que la URL de cancelación de suscripción con un clic añadida a la opción personalizada sea válida? %}
No, no verificamos ni validamos ningún enlace en el panel de Braze. Asegúrate de probar correctamente tu URL antes del lanzamiento.
{% enddetails %}