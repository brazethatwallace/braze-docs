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

¿No tienes claro si tu mensaje debe enviarse mediante una Campaign o un Canvas? Las Campaigns son mejores para campañas de mensajería únicas y segmentadas, mientras que los Canvas son mejores para recorridos de usuario con varios pasos.

{% tabs %}
{% tab Campaign %}

**Pasos:**

1. Ve a **Mensajería** > **Campaigns** y selecciona **Crear Campaign**.
2. Selecciona **Webhook** o, para campañas dirigidas a múltiples canales, selecciona **Multicanal**.
3. Ponle a tu Campaign un nombre claro y significativo.
4. (Opcional) Añade una descripción para explicar cómo se utilizará esta Campaign.
4. Añade [equipos]({{site.baseurl}}/user_guide/administer/global/user_management/teams) y [etiquetas]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags) según sea necesario.
   * Las etiquetas facilitan la búsqueda de tus campañas y la elaboración de informes. Por ejemplo, al utilizar el [generador de informes]({{site.baseurl}}/user_guide/analytics/reports/report_builder), puedes filtrar por etiquetas específicas.
5. Añade y nombra tantas variantes como necesites para tu Campaign. Puedes elegir diferentes plantillas de webhook para cada una de las variantes añadidas. Para más información sobre este tema, consulta [Pruebas multivariante y A/B]({{site.baseurl}}/user_guide/messaging/ab_testing).

{% alert tip %}
Si todos los mensajes de tu Campaign van a ser similares o tener el mismo contenido, redacta tu mensaje antes de añadir variantes adicionales. Luego puedes elegir **Copiar de variante** en el desplegable **Añadir variante**.
{% endalert %}

{% endtab %}
{% tab Canvas %}

**Pasos:**

{% multi_lang_include messaging/canvas_message_step_setup.md %}

{% endtab %}
{% endtabs %}

## Paso 2: Crea tu webhook {#step-2-build-your-webhook}

Puedes elegir crear un webhook desde cero, usar una plantilla existente o usar una de nuestras plantillas existentes. Luego, crea tu webhook en la pestaña **Compose** del editor.

La pestaña **Compose** consta de los siguientes campos:

- Idioma
- URL del webhook
- Método HTTP
- Cuerpo de la solicitud

![La pestaña "Compose" con un ejemplo de plantilla de webhook.]({% image_buster /assets/img_archive/webhook_compose.png %})

### Idioma {#internationalization}

La [internacionalización]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization) es compatible con la URL y el cuerpo de la solicitud. Para internacionalizar tu mensaje, selecciona **Add languages** y completa los campos obligatorios.

Te recomendamos seleccionar los idiomas antes de escribir tu contenido para que puedas completar el texto donde corresponda en Liquid. Para consultar nuestra lista completa de idiomas disponibles, consulta [Idiomas compatibles]({{site.baseurl}}/developer_guide/localization?tab=android).

Si estás añadiendo texto en un idioma que se escribe de derecha a izquierda, ten en cuenta que la apariencia final de los mensajes de derecha a izquierda depende en gran medida de cómo los rendericen los proveedores de servicios. Para conocer las mejores prácticas sobre la creación de mensajes de derecha a izquierda que se muestren con la mayor precisión posible, consulta [Creación de mensajes de derecha a izquierda]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages).

### URL del webhook {#webhook-url}

La URL del webhook, o URL HTTP, especifica tu endpoint. El endpoint es el lugar donde enviarás la información que estás capturando en el webhook.

Si deseas enviar información a un proveedor, este debería proporcionarte esta URL en su documentación de API. Si estás enviando información a tus propios sistemas, consulta con tu equipo de desarrollo o ingeniería para confirmar que estés usando la URL correcta.

Braze solo permite URLs que se comuniquen a través de los puertos estándar `80` (HTTP) y `443` (HTTPS).

#### Uso de Liquid {#using-liquid}

Puedes personalizar las URLs de tu webhook usando [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid). A veces, ciertos endpoints pueden requerir que identifiques a un usuario o proporciones información específica del usuario como parte de tu URL. Al usar Liquid, asegúrate de incluir un [valor predeterminado]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=web) para cada dato específico del usuario que utilices en tu URL.

### Método HTTP {#http-method}

El método HTTP que debes usar varía según el endpoint al que estés enviando información. En la mayoría de los casos, usarás POST.

| Método HTTP | Descripción |
| ----------- | ----------- |
| POST | Escribe nueva información en el servidor receptor. Este es el método más común que se usa al enviar datos. |
| GET | Recupera información existente, a diferencia de escribir información nueva. Por definición, una solicitud GET no admite un cuerpo de solicitud. |
| PUT | Actualiza la información en el endpoint, reemplazando cualquier información existente con lo que esté en el cuerpo de la solicitud. |
| DELETE | Elimina el recurso en la URL HTTP. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Método HTTP" }

### Cuerpo de la solicitud {#request-body}

El cuerpo de la solicitud es la información que se enviará a la URL que especificaste. Puedes crear el cuerpo de la solicitud de tu webhook con pares clave-valor JSON o texto sin formato.

#### Pares clave-valor JSON {#json-key-value-pairs}

Los pares clave-valor JSON te permiten escribir fácilmente una solicitud para un endpoint que espere un formato JSON. Solo puedes usar esto con un endpoint que espere una solicitud JSON. Por ejemplo, si tu clave es `message_body`, el valor correspondiente podría ser `Your order just arrived!`. Una vez que hayas introducido tu par clave-valor, el creador configurará tu solicitud en sintaxis JSON y se rellenará automáticamente una vista previa de tu solicitud JSON.

![Cuerpo de la solicitud configurado con pares clave-valor JSON.]({% image_buster /assets/img/webhook_json_1.png %})

Puedes personalizar tus pares clave-valor usando Liquid, incluyendo cualquier atributo de usuario, [atributo personalizado]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes?sdktab=swift) o [propiedad de evento]({{site.baseurl}}/user_guide/data/activation/events/custom_events) en tu solicitud. Por ejemplo, puedes incluir el nombre y el correo electrónico de un cliente en tu solicitud. Asegúrate de incluir un [valor predeterminado]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=web) para cada atributo.

#### Texto sin formato {#raw-text}

La opción de texto sin formato te da la flexibilidad de escribir una solicitud para un endpoint que espere un cuerpo en cualquier formato. Por ejemplo, podrías usar esto para escribir una solicitud para un endpoint que espere que tu solicitud esté en formato XML.

Tanto la [personalización]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) como la [internacionalización]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization) usando Liquid son compatibles con el texto sin formato.

![Un ejemplo de un cuerpo de solicitud con texto sin formato usando Liquid.]({% image_buster /assets/img_archive/webhook_rawtext.png %})

Si configuras el [encabezado de solicitud](#request-headers-optional) `Content-Type` como `application/x-www-form-url-encoded`, el cuerpo de la solicitud debe tener formato de cadena codificada en URL. Por ejemplo:

{% raw %}
```
to={{custom_attribute.${example}}}&text=Your+order+just+arrived
```
{% endraw %}

![Cuerpo de la solicitud con cadena codificada en URL.]({% image_buster /assets/img_archive/webhook_rawtext_URL-encoded.png %})

## Paso 3: Configurar ajustes adicionales {#step-3-configure-additional-settings}

### Encabezados de solicitud (opcional) {#request-headers-optional}

Ciertos endpoints pueden requerir que incluyas encabezados en tu solicitud. En la sección **Redactar** del creador, puedes añadir tantos encabezados como necesites.

![Ejemplos de encabezados de solicitud para la clave "Authorization" y la clave "Content-type".]({% image_buster /assets/img_archive/webhook_request_headers_example.png %})

Los encabezados de solicitud más comunes son las especificaciones de [`Content-Type`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Type) (que describen qué tipo de datos esperar en el cuerpo, como XML o JSON) y los encabezados de [`Authorization`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization) que contienen tus credenciales con tu proveedor o sistema.

{% alert note %}
Los nombres de los encabezados HTTP no distinguen entre mayúsculas y minúsculas según [RFC 7230, sección 3.2 ("Each header field consists of a case-insensitive field name")](https://datatracker.ietf.org/doc/html/rfc7230#section-3.2). Si tu endpoint receptor o cualquier servicio intermedio (como CDN) transforma las mayúsculas y minúsculas de los encabezados, esto no afectará el procesamiento de los encabezados: `Content-Type`, `content-type` y `CONTENT-TYPE` se tratan de forma idéntica.
{% endalert %}

Las especificaciones de tipo de contenido deben usar la clave `Content-Type`. Los valores comunes son `application/json` o `application/x-www-form-urlencoded`.

Los encabezados de autorización deben usar la clave `Authorization`. Los valores comunes son {% raw %} `Bearer {{YOUR_TOKEN}}` o `Basic {{YOUR_TOKEN}}` {% endraw %} donde `YOUR_TOKEN` son las credenciales proporcionadas por tu proveedor o sistema.

## Paso 4: Envío de prueba de tu mensaje {#step-4-test-send-your-message}

Antes de activar tu campaña, Braze recomienda que pruebes el webhook para asegurarte de que la solicitud tiene el formato correcto.

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

## Paso 5: Construye el resto de tu Campaign o Canvas {#step-5-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab Campaign %}

A continuación, construye el resto de tu Campaign. Consulta las siguientes secciones para obtener más detalles sobre cómo utilizar mejor nuestras herramientas para crear webhooks.

### Elige el horario de entrega o el desencadenante {#choose-delivery-schedule-or-trigger}

Los webhooks pueden entregarse basándose en un horario programado, una acción o un desencadenante de API. Para más información, consulta [Programar tu Campaign]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign).

Para la entrega basada en acciones, también puedes establecer la duración de la Campaign y las [horas tranquilas]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours).

En este paso también puedes especificar controles de entrega, como permitir que los usuarios vuelvan a ser [elegibles]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility#turning-on-re-eligibility) para recibir la Campaign, o habilitar reglas de [limitación de frecuencia]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#about-frequency-capping).

### Elige los usuarios objetivo {#choose-users-to-target}

A continuación, debes [segmentar a los usuarios]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users) eligiendo Segments o filtros para acotar tu audiencia. En este paso, seleccionas la audiencia más amplia de tus Segments y la reduces aún más con nuestros filtros, si lo deseas. Recibes automáticamente una vista previa de cómo es aproximadamente la población de ese Segment. Ten en cuenta que la pertenencia exacta al Segment siempre se calcula antes de que se envíe el mensaje.

{% multi_lang_include audience/target_audiences.md %}

### Elige eventos de conversión {#choose-conversion-events}

Braze te permite hacer seguimiento de la frecuencia con la que los usuarios realizan acciones específicas, [eventos de conversión]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events), después de recibir una Campaign. Tienes la opción de permitir una ventana de hasta 30 días durante la cual se contará una conversión si el usuario realiza la acción especificada.

{% endtab %}

{% tab Canvas %}

Si aún no lo has hecho, completa las secciones restantes de tu paso en Canvas. Para obtener detalles sobre cómo construir el resto de tu Canvas, incluyendo pruebas multivariante y [Optimizar con BrazeAI<sup>TM</sup>]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#optimize-canvas-variants-with-brazeai), consulta [Construir tu Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-2-build-your-canvas).

{% endtab %}
{% endtabs %}

## Paso 6: Revisar e implementar {#step-6-review-and-deploy}

Cuando hayas terminado de crear la última de tus Campaign o Canvas, revisa sus detalles, pruébala y envíala.

## Cosas que debes saber {#things-to-know}

### Errores, lógica de reintento y tiempos de espera {#errors-retry-logic-and-timeouts}

Los webhooks dependen de los servidores de Braze que realizan solicitudes a un endpoint externo, y ocasionalmente pueden ocurrir errores. Los errores más comunes incluyen errores de sintaxis, claves de API expiradas, límites de velocidad y problemas inesperados del lado del servidor. Antes de enviar una campaña de webhook:

- Prueba tu webhook en busca de errores de sintaxis
- Asegúrate de que las variables personalizadas tengan valores predeterminados

Si tu webhook no se envía, se registra un mensaje de error en el [registro de actividad de mensajes]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log), e incluye detalles como la marca de tiempo del error, el nombre de la aplicación y detalles sobre el error.

![Error de webhook con el mensaje "An active access token must be used to query information about the current user".]({% image_buster /assets/img_archive/webhook-error.png %})

Si el mensaje de error no es lo suficientemente claro respecto al origen del error, deberías consultar la documentación del endpoint de API que estás utilizando. Generalmente proporcionan una explicación de los códigos de error que utiliza el endpoint, así como las causas habituales.

#### Códigos de respuesta y lógica de reintento {#response-codes-and-retry-logic}

Cuando se envía la solicitud de webhook, el servidor receptor devolverá un código de respuesta indicando qué ocurrió con la solicitud. La siguiente tabla resume las diferentes respuestas que el servidor puede enviar, cómo afectan a los análisis de Campaign y si, en caso de errores, Braze intentará reenviar la Campaign:

| Código de respuesta | ¿Marcado como recibido? | ¿Reintentos? |
|---------------|-----------|----------|
| `20x` (éxito)  | Sí |   N/A  |
| `30x` (redirección)  | No | No |
| `408` (tiempo de espera de solicitud)  | No | Sí |
| `429` (límite de velocidad)  | No | Sí |
| `Otros 4XX` (error del cliente)  | No | No |
| `5XX` (error del servidor)   | No | Sí |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Códigos de respuesta y lógica de reintento" }

{% alert note %}
Braze reintenta los códigos de estado mencionados anteriormente en esta sección hasta cinco veces en un plazo de 30 minutos utilizando retirada exponencial. Si no podemos alcanzar tu endpoint, los reintentos pueden distribuirse en un periodo de 24 horas.<br><br>Cada webhook tiene un tiempo de espera máximo de 90 segundos.
{% endalert %}

Los encabezados de respuesta `Retry-After` y de límite de velocidad pueden afectar cuánto tiempo espera Braze antes de un intento **reintentable** (por ejemplo, después de `408`, `429` o `5XX`). No hacen que las respuestas no reintentables, como `401`, sean elegibles para reintento.

<!-- support-analyzer-phase2:webhook_delivery_failures -->
{% alert note %}
Si los envíos de webhook parecen estar ausentes en los análisis, abre el [registro de actividad de mensajes]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) para la Campaign o paso en Canvas. Braze solo reintenta ciertas respuestas (por ejemplo, `408`, `429` y `5XX`); la mayoría de los otros errores de cliente `4XX`, incluido `401 Unauthorized`, **no** se reintentan. Para la tabla completa de respuestas, consulta [Códigos de respuesta y lógica de reintento](#response-codes-and-retry-logic).
{% endalert %}


#### 403 Forbidden y listas de IP permitidas {#403-forbidden-and-ip-allowlisting}

Las respuestas `403 Forbidden` significan que tu endpoint recibió la solicitud pero la rechazó. Las causas comunes incluyen autenticación inválida o ausente, permisos de API insuficientes y reglas de red (como un firewall o un firewall de aplicaciones web) que bloquean las direcciones IP de salida de Braze.

Si las solicitudes de webhook devuelven consistentemente `403` y tus encabezados de autenticación son correctos, añade las IP de Braze a la lista de permitidas de tu clúster en el servidor que recibe el webhook. Consulta [Listas de IP permitidas](#ip-allowlisting). Las solicitudes de contenido conectado utilizan las mismas IP de salida; consulta [Listas de IP permitidas de contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call#connected-content-ip-allowlisting).

Para otros pasos de solución de problemas con `4XX`, consulta [Solución de problemas de solicitudes de webhook y contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/troubleshooting_webhooks_and_connected_content#4xx-errors).

#### Autenticación y credenciales de contenido conectado {#authentication-and-connected-content-credentials}

La solicitud HTTP de webhook saliente no admite adjuntar [credenciales de contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call#authentication-types) (`:basic_auth` o `:auth_credentials`) para autenticarte contra tu endpoint. En su lugar, configura la autenticación utilizando **Encabezados de solicitud** en el webhook. Para obtener un token o secreto en el momento del envío, puedes colocar una etiqueta {% raw %}`{% connected_content %}`{% endraw %} en un campo de encabezado o cuerpo para que Liquid la resuelva antes de que se envíe el webhook.

#### Plantillas de webhook guardadas y uso en Campaigns {#saved-webhook-templates-and-campaign-usage}

Braze no proporciona un informe integrado que liste cada Campaign o paso en Canvas que haga referencia a una **plantilla de webhook guardada** determinada. Para auditar el uso, revisa los pasos de webhook que utilicen la misma URL y método HTTP, o contacta con [soporte de Braze]({{site.baseurl}}/support_contact).

#### Solución de problemas y detalles adicionales de errores {#troubleshooting-and-additional-error-details}

Para explicaciones detalladas, pasos de solución de problemas y orientación para resolver errores específicos de webhook, consulta [Solución de problemas de solicitudes de webhook y contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/troubleshooting_webhooks_and_connected_content). También encontrarás más explicaciones sobre cómo funciona nuestro sistema de detección de hosts en mal estado y cómo Braze proporciona notificaciones de errores a través de correos electrónicos automatizados y registros adicionales en Braze Currents.

### Listas de IP permitidas {#ip-allowlisting}

Cuando se envía un webhook desde Braze, los servidores de Braze realizan solicitudes de red a los servidores de nuestros clientes o de terceros. Con las listas de IP permitidas, puedes verificar que las solicitudes de webhook provienen de Braze, añadiendo una capa de seguridad.

Braze enviará webhooks desde las siguientes IP. Las IP listadas se añaden automática y dinámicamente a cualquier clave de API que haya sido incluida en la lista de permitidas.

{% alert important %}
Si estás realizando un webhook de Braze a Braze y utilizas listas de permitidas, deberías incluir todas las siguientes IP, incluida `127.0.0.1`.
{% endalert %}

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

### Eliminar usuarios {#delete-users}

Para eliminar un usuario individual o un Segment de usuarios, ve a **Audiencia** > **Gestionar audiencia** > **Eliminar usuarios**. El panel admite la eliminación masiva de Segments (hasta 10 millones de perfiles), incluye una ventana de cancelación de 7 días y no consume los límites de velocidad compartidos de la REST or transferencia de estado representacional API. Para los pasos, límites y permisos, consulta [Eliminar usuarios]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles/delete_users).

Para la eliminación programática en lotes más pequeños, utiliza el [endpoint `/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete) en lugar de una campaña de webhook.