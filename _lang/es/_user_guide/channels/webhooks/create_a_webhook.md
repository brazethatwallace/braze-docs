---
nav_title: Crear un webhook
article_title: Crear un webhook
page_order: 1
channel:
  - webhooks
description: "Este artículo de referencia explica cómo crear y configurar una campaña de webhook."
search_rank: 2
---

# Crear una campaña de webhook {#create-a-webhook-campaign}

> Crear una campaña de webhook o incluir un webhook en una campaña multicanal te permite desencadenar acciones fuera de la aplicación proporcionando a otros sistemas y aplicaciones información en tiempo real.

Puedes usar webhooks para enviar información a sistemas como Salesforce o Marketo, o a tus sistemas backend. Por ejemplo, podrías querer acreditar en las cuentas de tus clientes una promoción después de que hayan realizado un evento personalizado un determinado número de veces.

{% alert tip %}
Para obtener más información sobre qué son los webhooks y cómo puedes usarlos en Braze, consulta [Webhooks]({{site.baseurl}}/user_guide/channels/webhooks) antes de continuar.
{% endalert %}

## Paso 1: Elige dónde crear tu mensaje {#step-1-choose-where-to-build-your-message}

¿No tienes claro si tu mensaje debe enviarse mediante una campaña o un Canvas? Las campañas son mejores para envíos de mensajería únicos y dirigidos, mientras que los Canvas son mejores para recorridos de usuario de varios pasos.

{% tabs %}
{% tab Campaign %}

**Pasos:**

1. Ve a **Mensajería** > **Campaigns** y selecciona **Crear campaña**.
2. Selecciona **Webhook** o, para campañas dirigidas a múltiples canales, selecciona **Multicanal**.
3. Ponle a tu campaña un nombre claro y significativo.
4. (Opcional) Añade una descripción para explicar cómo se utilizará esta campaña.
4. Añade [equipos]({{site.baseurl}}/user_guide/administer/global/user_management/teams) y [etiquetas]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags) según sea necesario.
   * Las etiquetas facilitan encontrar tus campañas y generar informes a partir de ellas. Por ejemplo, al usar el [generador de informes]({{site.baseurl}}/user_guide/analytics/reports/report_builder), puedes filtrar por etiquetas específicas.
5. Añade y nombra tantas variantes como necesites para tu campaña. Puedes elegir diferentes plantillas de webhook para cada una de las variantes añadidas. Para más información sobre este tema, consulta [Pruebas multivariante y A/B]({{site.baseurl}}/user_guide/messaging/ab_testing).

{% alert tip %}
Si todos los mensajes de tu campaña van a ser similares o tener el mismo contenido, redacta tu mensaje antes de añadir variantes adicionales. Luego puedes elegir **Copiar de variante** en el desplegable **Añadir variante**.
{% endalert %}

{% endtab %}
{% tab Canvas %}

**Pasos:**

1. [Crea tu Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas) usando el creador de Canvas.
2. Después de configurar tu Canvas, añade un paso en el constructor de Canvas. Ponle a tu paso un nombre claro y significativo.
3. Elige una [planificación de paso]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#schedule-your-canvas-step) y especifica un retraso según sea necesario.
4. Filtra tu audiencia para este paso según sea necesario. Puedes refinar aún más los destinatarios de este paso especificando segmentos y añadiendo filtros adicionales. Las opciones de audiencia se comprobarán después del retraso en el momento en que se envíen los mensajes.
5. Elige tu [comportamiento de avance]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#advancement-behavior).
6. Elige cualquier otro canal de mensajería que desees emparejar con tu mensaje.

{% endtab %}
{% endtabs %}

## Paso 2: Crea tu webhook {#step-2-build-your-webhook}

Puedes elegir crear un webhook desde cero, usar una plantilla existente o usar una de nuestras plantillas existentes. Luego, crea tu webhook en la pestaña **Redactar** del editor.

La pestaña **Redactar** consta de los siguientes campos:

- Idioma
- URL del webhook
- Método HTTP
- Cuerpo de la solicitud

![La pestaña "Redactar" con un ejemplo de plantilla de webhook.]({% image_buster /assets/img_archive/webhook_compose.png %})

### Idioma {#internationalization}

La [internacionalización]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies#campaigns-in-multiple-languages) es compatible en la URL y en el cuerpo de la solicitud. Para internacionalizar tu mensaje, selecciona **Añadir idiomas** y completa los campos requeridos.

Te recomendamos seleccionar tus idiomas antes de escribir tu contenido para que puedas rellenar tu texto donde corresponda en Liquid. Para consultar nuestra lista completa de idiomas disponibles, consulta [Idiomas compatibles]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization#languages-supported).

Si estás añadiendo texto en un idioma que se escribe de derecha a izquierda, ten en cuenta que la apariencia final de los mensajes de derecha a izquierda depende en gran medida de cómo los proveedores de servicios los rendericen. Para conocer las mejores prácticas sobre cómo crear mensajes de derecha a izquierda que se muestren con la mayor precisión posible, consulta [Crear mensajes de derecha a izquierda]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages).

### URL del webhook {#webhook-url}

La URL del webhook, o URL HTTP, especifica tu endpoint. El endpoint es el lugar donde enviarás la información que estás capturando en el webhook.

Si deseas enviar información a un proveedor, este debe proporcionar esta URL en su documentación de API. Si estás enviando información a tus propios sistemas, consulta con tu equipo de desarrollo o ingeniería para confirmar que estás usando la URL correcta.

Braze solo permite URLs que se comunican a través de los puertos estándar `80` (HTTP) y `443` (HTTPS).

#### Uso de Liquid {#using-liquid}

Puedes personalizar las URLs de tu webhook usando [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid). A veces, ciertos endpoints pueden requerir que identifiques a un usuario o proporciones información específica del usuario como parte de tu URL. Al usar Liquid, asegúrate de incluir un [valor predeterminado]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=web) para cada dato específico del usuario que utilices en tu URL.

### Método HTTP {#http-method}

El método HTTP que debes usar varía según el endpoint al que estés enviando información. En la mayoría de los casos, usarás POST.

| Método HTTP | Descripción |
| ----------- | ----------- |
| POST | Escribe nueva información en el servidor receptor. Este es el método más común utilizado al enviar datos. |
| GET | Recupera información existente, a diferencia de escribir nueva información. Por definición, una solicitud GET no admite un cuerpo de solicitud. |
| PUT | Actualiza información en el endpoint, reemplazando cualquier información existente con lo que está en el cuerpo de la solicitud. |
| DELETE | Elimina el recurso en la URL HTTP. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Método HTTP" }

### Cuerpo de la solicitud {#request-body}

El cuerpo de la solicitud es la información que se enviará a la URL que especificaste. Puedes crear el cuerpo de tu solicitud de webhook con pares clave-valor JSON o texto sin formato.

#### Pares clave-valor JSON {#json-key-value-pairs}

Los pares clave-valor JSON te permiten escribir fácilmente una solicitud para un endpoint que espera un formato JSON. Solo puedes usar esto con un endpoint que espere una solicitud JSON. Por ejemplo, si tu clave es `message_body`, el valor correspondiente podría ser `Your order just arrived!`. Después de introducir tu par clave-valor, el creador configurará tu solicitud en sintaxis JSON, y se generará automáticamente una vista previa de tu solicitud JSON.

![Cuerpo de la solicitud configurado con pares clave-valor JSON.]({% image_buster /assets/img/webhook_json_1.png %})

Puedes personalizar tus pares clave-valor usando Liquid, incluyendo cualquier atributo de usuario, [atributo personalizado]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids#additional-notes-and-best-practices) o [propiedad de evento]({{site.baseurl}}/user_guide/data/activation/events/custom_events) en tu solicitud. Por ejemplo, puedes incluir el nombre y el correo electrónico de un cliente en tu solicitud. Asegúrate de incluir un [valor predeterminado]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=web) para cada atributo.

#### Texto sin formato {#raw-text}

La opción de texto sin formato te da la flexibilidad de escribir una solicitud para un endpoint que espera un cuerpo de cualquier formato. Por ejemplo, podrías usar esto para escribir una solicitud para un endpoint que espere que tu solicitud esté en formato XML.

Tanto la [personalización]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) como la [internacionalización]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies#campaigns-in-multiple-languages) usando Liquid son compatibles en texto sin formato.

![Un ejemplo de cuerpo de solicitud con texto sin formato usando Liquid.]({% image_buster /assets/img_archive/webhook_rawtext.png %})

Si configuras el [encabezado de solicitud](#request-headers-optional) `Content-Type` como `application/x-www-form-url-encoded`, el cuerpo de la solicitud debe estar formateado como una cadena codificada en URL. Por ejemplo:

{% raw %}
```
to={{custom_attribute.${example}}}&text=Your+order+just+arrived
```
{% endraw %}

![Cuerpo de la solicitud con cadena codificada en URL.]({% image_buster /assets/img_archive/webhook_rawtext_URL-encoded.png %})

## Paso 3: Configura ajustes adicionales {#step-3-configure-additional-settings}

### Encabezados de solicitud (opcional) {#request-headers-optional}

Ciertos endpoints pueden requerir que incluyas encabezados en tu solicitud. En la sección **Redactar** del creador, puedes añadir tantos encabezados como necesites.

![Ejemplos de encabezados de solicitud para la clave "Authorization" y la clave "Content-type".]({% image_buster /assets/img_archive/webhook_request_headers_example.png %})

Los encabezados de solicitud más comunes son las especificaciones de `Content-Type` (que describen qué tipo de datos se esperan en el cuerpo, como XML o JSON) y los encabezados de autorización que contienen tus credenciales con tu proveedor o sistema.

Las especificaciones de tipo de contenido deben usar la clave `Content-Type`. Los valores comunes son `application/json` o `application/x-www-form-urlencoded`.

Los encabezados de autorización deben usar la clave `Authorization`. Los valores comunes son {% raw %} `Bearer {{YOUR_TOKEN}}` o `Basic {{YOUR_TOKEN}}` {% endraw %} donde `YOUR_TOKEN` son las credenciales proporcionadas por tu proveedor o sistema.

## Paso 4: Envía un mensaje de prueba {#step-4-test-send-your-message}

Antes de poner tu campaña en marcha, Braze recomienda que pruebes el webhook para asegurarte de que la solicitud está formateada correctamente.

Para hacerlo, cambia a la pestaña **Prueba** y envía un webhook de prueba. Puedes probar el webhook como un usuario aleatorio, un usuario específico (introduciendo su dirección de correo electrónico o ID de usuario externo), o un usuario personalizado con los atributos que elijas.

Después de enviar el webhook de prueba, aparecerá un cuadro de diálogo con el mensaje de respuesta. Si la solicitud del webhook no tiene éxito, consulta el mensaje de error para obtener ayuda en la solución de problemas de tu webhook. El siguiente ejemplo detalla la respuesta de un webhook con una URL de webhook no válida.

```http
404 Not Found

{
  "error": {
    "message": "Unrecognized request URL. Please see https://lob.com/docs or email us at support@lob.com.",
    "status_code": 404
  }
}

```

Para más información, consulta [Enviar mensajes de prueba]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=webhook).

## Paso 5: Construye el resto de tu campaña o Canvas {#step-5-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab Campaign %}

A continuación, construye el resto de tu campaña. Consulta las siguientes secciones para obtener más detalles sobre cómo usar mejor nuestras herramientas para crear webhooks.

### Elige la planificación de entrega o el desencadenante {#choose-delivery-schedule-or-trigger}

Los webhooks pueden entregarse según un horario planificado, una acción o un desencadenante de API. Para más información, consulta [Planificar tu campaña]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign).

Para la entrega basada en acciones, también puedes establecer la duración de la campaña y las [horas tranquilas]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours).

En este paso también puedes especificar controles de entrega, como permitir que los usuarios vuelvan a ser [elegibles]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility#campaigns) para recibir la campaña, o habilitar reglas de [limitación de frecuencia]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#frequency-capping).

### Elige los usuarios objetivo {#choose-users-to-target}

A continuación, debes [dirigirte a los usuarios]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users) eligiendo segmentos o filtros para acotar tu audiencia. En este paso, seleccionas la audiencia más amplia de tus segmentos y la acotas aún más con nuestros filtros, si lo deseas. Recibirás automáticamente una vista previa de la población aproximada de ese segmento. Ten en cuenta que la pertenencia exacta al segmento siempre se calcula antes de enviar el mensaje.

{% multi_lang_include audience/target_audiences.md %}

### Elige eventos de conversión {#choose-conversion-events}

Braze te permite hacer seguimiento de la frecuencia con la que los usuarios realizan acciones específicas, [eventos de conversión]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events), después de recibir una campaña. Tienes la opción de permitir una ventana de hasta 30 días durante la cual se contará una conversión si el usuario realiza la acción especificada.

{% endtab %}

{% tab Canvas %}

Si aún no lo has hecho, completa las secciones restantes de tu paso en Canvas. Para más detalles sobre cómo construir el resto de tu Canvas, implementar pruebas multivariante y selección inteligente, y más, consulta el paso [Construir tu Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-3-build-your-canvas) de nuestra documentación de Canvas.

{% endtab %}
{% endtabs %}

## Paso 6: Revisa y despliega {#step-6-review-and-deploy}

Después de terminar de construir la última parte de tu campaña o Canvas, revisa sus detalles, pruébala y luego ¡envíala!

## Cosas que debes saber {#things-to-know}

### Errores, lógica de reintentos y tiempos de espera {#errors-retry-logic-and-timeouts}

Los webhooks dependen de que los servidores de Braze realicen solicitudes a un endpoint externo, y ocasionalmente pueden ocurrir errores. Los errores más comunes incluyen errores de sintaxis, claves de API caducadas, límites de velocidad y problemas inesperados del lado del servidor. Antes de enviar una campaña de webhook:

- Prueba tu webhook para detectar errores de sintaxis
- Asegúrate de que las variables personalizadas tengan valores predeterminados

Si tu webhook no se envía, se registra un mensaje de error en el [Registro de actividad de mensajes]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log), e incluye detalles como la marca de tiempo del error, el nombre de la aplicación y detalles sobre el error.

![Error de webhook con el mensaje "An active access token must be used to query information about the current user".]({% image_buster /assets/img_archive/webhook-error.png %})

Si el mensaje de error no es lo suficientemente claro sobre el origen del error, deberías consultar la documentación del endpoint de API que estás usando. Normalmente proporcionan una explicación de los códigos de error que utiliza el endpoint, así como las causas habituales.

#### Códigos de respuesta y lógica de reintentos {#response-codes-and-retry-logic}

Cuando se envía la solicitud del webhook, el servidor receptor devolverá un código de respuesta indicando qué ocurrió con la solicitud. La siguiente tabla resume las diferentes respuestas que el servidor puede enviar, cómo afectan a los análisis de la campaña y si, en caso de errores, Braze intentará reenviar la campaña:

| Código de respuesta | ¿Marcado como recibido? | ¿Reintentos? |
|---------------|-----------|----------|
| `20x` (éxito)  | Sí |   N/A  |
| `30x` (redirección)  | No | No |
| `408` (tiempo de espera de solicitud)  | No | Sí |
| `429` (límite de velocidad)  | No | Sí |
| `Otros 4XX` (error del cliente)  | No | No |
| `5XX` (error del servidor)   | No | Sí |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Códigos de respuesta y lógica de reintentos" }

{% alert note %}
Braze reintenta los códigos de estado mencionados anteriormente en esta sección hasta cinco veces en 30 minutos usando retirada exponencial. Si no podemos alcanzar tu endpoint, los reintentos pueden distribuirse a lo largo de un período de 24 horas.<br><br>Cada webhook tiene un tiempo de espera de 90 segundos antes de que se agote.
{% endalert %}

Los encabezados de respuesta `Retry-After` y de límite de velocidad pueden afectar cuánto tiempo espera Braze antes de un intento **reintentable** (por ejemplo, después de `408`, `429` o `5XX`). No hacen que las respuestas no reintentables, como `401`, sean elegibles para reintento.

#### Autenticación y credenciales de contenido conectado {#authentication-and-connected-content-credentials}

La solicitud HTTP saliente del webhook no admite adjuntar [credenciales de contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call#authentication-types) (`:basic_auth` o `:auth_credentials`) para autenticarse contra tu endpoint. Configura la autenticación usando **Encabezados de solicitud** en el webhook en su lugar. Para obtener un token o secreto en el momento del envío, puedes colocar una etiqueta {% raw %}`{% connected_content %}`{% endraw %} en un campo de encabezado o cuerpo para que Liquid lo resuelva antes de que se envíe el webhook.

#### Plantillas de webhook guardadas y uso en campañas {#saved-webhook-templates-and-campaign-usage}

Braze no proporciona un informe integrado que liste cada campaña o paso en Canvas que haga referencia a una **plantilla de webhook guardada** determinada. Para auditar el uso, revisa los pasos de webhook que usen la misma URL y método HTTP, o ponte en contacto con [soporte de Braze]({{site.baseurl}}/support_contact).

#### Solución de problemas y detalles adicionales de errores {#troubleshooting-and-additional-error-details}

Para explicaciones detalladas, pasos de solución de problemas y orientación sobre cómo resolver errores específicos de webhook, consulta [Solución de problemas de solicitudes de webhook y contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/troubleshooting_webhooks_and_connected_content). También encontrarás más explicaciones sobre cómo funciona nuestro sistema de detección de hosts no saludables y cómo Braze proporciona notificaciones de errores a través de correos electrónicos automatizados y registro adicional en Braze Currents.

### Lista de IPs permitidas {#ip-allowlisting}

Cuando se envía un webhook desde Braze, los servidores de Braze realizan solicitudes de red a los servidores de nuestros clientes o de terceros. Con la lista de IPs permitidas, puedes verificar que las solicitudes de webhook provienen de Braze, añadiendo una capa de seguridad.

Braze enviará webhooks desde las siguientes IPs. Las IPs listadas se añaden automática y dinámicamente a cualquier clave de API que haya sido habilitada para la lista de permitidos.

{% alert important %}
Si estás haciendo un webhook de Braze a Braze y usas la lista de permitidos, deberías incluir todas las siguientes IPs, incluyendo `127.0.0.1`.
{% endalert %}

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

### Eliminar usuarios {#delete-users}

Para eliminar un usuario individual o un segmento de usuarios, ve a **Audiencia** > **Gestionar audiencia** > **Eliminar usuarios**. El panel admite la eliminación masiva de segmentos (hasta 10 millones de perfiles), incluye una ventana de cancelación de 7 días y no consume los límites de velocidad compartidos de la REST API. Para conocer los pasos, límites y permisos, consulta [Eliminar usuarios]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles/delete_users).

Para la eliminación programática en lotes más pequeños, usa el [endpoint `/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete) en lugar de una campaña de webhook.