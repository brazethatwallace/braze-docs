---
nav_title: Errores y respuestas
article_title: Errores y respuestas de la API
description: "Este artículo de referencia cubre los distintos errores y respuestas del servidor que pueden surgir al utilizar la API de Braze y cómo solucionarlos."
page_type: reference
page_order: 2.3

---
# Errores y respuestas de la API {#api-errors-and-responses}

> Este artículo de referencia cubre los distintos errores y respuestas del servidor que pueden surgir al utilizar la API de Braze y cómo solucionarlos.

## Respuestas del servidor {#server-responses}

Si tu carga útil POST fue aceptada por nuestros servidores, los mensajes con éxito reciben la siguiente respuesta:

```json
{
  "message" : "success"
}
```

Ten en cuenta que "success" solo significa que la carga útil de la API RESTful se formó correctamente y se pasó a nuestros servicios de notificaciones push, correo electrónico u otros servicios de mensajería. No significa que los mensajes se hayan entregado realmente, ya que factores adicionales podrían impedir la entrega del mensaje (por ejemplo, un dispositivo podría estar sin conexión, el token de notificaciones push podría ser rechazado por los servidores de Apple, o podrías haber proporcionado un ID de usuario desconocido).

### ¿Por qué mi solicitud devuelve éxito cuando no se entregó ningún mensaje? {#why-does-my-request-return-success-when-no-message-was-delivered}

Una respuesta `message: success` o `2XX` significa que Braze aceptó y puso en cola la solicitud para los endpoints involucrados, no que cada destinatario haya recibido un mensaje. Para mensajería, la entrega aún depende de la elegibilidad del canal, los tokens, los errores del proveedor y la validación del contenido. Consulta la tabla de [errores fatales]({{site.baseurl}}/api/errors#fatal-errors) para conocer los errores HTTP que bloquean los envíos, y los análisis de tu Campaign o Canvas para las métricas de entrega posteriores.

Para endpoints como [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify), que no envían mensajes, un mensaje de éxito solo significa que Braze recibió la solicitud para procesarla. Si no hay coincidencia con el alias después del procesamiento, la solicitud se detiene.

Si tu mensaje es exitoso pero tiene errores no fatales, recibes la siguiente respuesta:

```json
{
  "message" : "success", "errors" : [<minor error message>]
}
```

En caso de éxito, cualquier mensaje que no se haya visto afectado por un error en el array `errors` se entrega igualmente. Si tu mensaje tiene un error fatal, recibes la siguiente respuesta:

```json
{
  "message" : <fatal error message>, "errors" : [<minor error message>]
}
```

## Respuestas para ID de envío con seguimiento {#responses-for-tracked-send-ids}

Los análisis siempre están disponibles para Campaigns. Además, los análisis están disponibles para una instancia de envío de Campaign específica cuando la Campaign se envía como difusión. Cuando el seguimiento está disponible para una instancia de envío de Campaign específica, recibes la siguiente respuesta:

```json
{
  "message": "success", "send_id" : "example_send_id"
}
```

El ID de envío proporcionado se puede utilizar como parámetro para el endpoint `/send/data_series` para obtener análisis específicos del envío.

## Errores {#errors}

El elemento de código de estado de una respuesta del servidor es un número de 3 dígitos donde el primer dígito del código define la clase de respuesta.

- La **clase 2XX** de código de estado (no fatal) indica que **tu solicitud** fue recibida, entendida y aceptada con éxito.
- La **clase 4XX** de código de estado (fatal) indica un **error del cliente**. Consulta la tabla de errores fatales para ver la lista completa de códigos de error 4XX y sus descripciones.
- La **clase 5XX** de código de estado (fatal) indica un **error del servidor**. Hay varias causas posibles, por ejemplo, el servidor al que intentas acceder no puede ejecutar la solicitud, el servidor está en mantenimiento y no puede ejecutar la solicitud, o el servidor experimenta altos niveles de tráfico. Cuando esto ocurre, te recomendamos reintentar tu solicitud con retirada exponencial. En caso de un incidente o interrupción, Braze no puede volver a ejecutar ninguna llamada a la REST API que haya fallado durante la ventana del incidente. Debes reintentar todas las llamadas que fallaron durante la ventana del incidente.
  - Un **error 502** es un fallo antes de que la solicitud llegue al servidor de destino.
  - Un **error 503** significa que la solicitud llegó al servidor de destino, pero no se puede completar porque no hay suficiente capacidad, hay un problema de red, o algo similar.
  - Un **error 504** indica que un servidor no recibió una respuesta de otro servidor en una posición superior de la cadena.

### Errores fatales {#fatal-errors}

Los siguientes códigos de estado y mensajes de error asociados se devuelven si tu solicitud encuentra un error fatal.

{% alert warning %}
Todos los siguientes códigos de error indican que no se envía ningún mensaje.
{% endalert %}

| Código de error | Descripción |
|---|---|
| `5XX Internal Server Error` | Reintenta tu solicitud con retirada exponencial.|
| `400 Bad Request` | Sintaxis incorrecta. Un JSON no válido devuelve HTTP 400. El campo `error` puede incluir un mensaje indicando que debes pasar `application/json` válido en el cuerpo de la solicitud, o `Error while parsing request body. Please check your syntax.` Consulta [Error al analizar el cuerpo de la solicitud](#error-while-parsing-request-body).|
| `400 No Recipients` | No hay ID externos, ID de segmento ni tokens de notificaciones push en la solicitud.|
| `400 Invalid Campaign ID` | No se encontró ninguna Campaign de API de mensajería para el ID de Campaign proporcionado.|
| `400 Message Variant Unspecified` | Proporcionaste un ID de Campaign pero no un ID de variante de mensaje.|
| `400 Invalid Message Variant` | Proporcionaste un ID de Campaign válido, pero el ID de variante de mensaje no coincide con ninguno de los mensajes de esa Campaign.|
| `400 Mismatched Message Type` | Proporcionaste una variante de mensaje del tipo de mensaje incorrecto para al menos uno de tus mensajes.|
| `400 Invalid Extra Push Payload` | Proporcionaste la clave `extra` para `apple_push` o `android_push`, pero no es un diccionario.|
| `400 Max Input Length Exceeded` | Para `/users/track`, este error se produce al exceder el número máximo de objetos permitidos en una sola solicitud. El límite depende del modelo de límite de velocidad: para la mayoría de los clientes, cada solicitud admite hasta 75 objetos en total combinados entre `attributes`, `events` y `purchases`. Para clientes con límites de velocidad heredados, cada array admite hasta 75 objetos de forma independiente. Para más información, consulta [POST: Crear y actualizar usuarios]({{site.baseurl}}/api/endpoints/user_data/post_user_track).|
| `400 The max number of external_ids and aliases per request was exceeded` | Se produce al llamar a más de 50 ID externos.|
| `400 The max number of ids per request was exceeded` | Se produce al llamar a más de 50 ID externos.|
| `400 No message to send` | No se especificó ninguna carga útil para el mensaje.|
| `400 Slideup Message Length Exceeded` | El mensaje de deslizamiento hacia arriba contiene más de 140 caracteres.|
| `400 Apple Push Length Exceeded` | La carga útil JSON tiene más de 1.912 bytes.|
| `400 Android Push Length Exceeded` | La carga útil JSON tiene más de 4.000 bytes.|
| `400 Bad Request` | No se puede analizar la fecha y hora de `send_at`.|
| `400 Bad Request` | En tu solicitud, `in_local_time` es verdadero pero `time` ya ha pasado en la zona horaria de tu empresa.|
| `401 Unauthorized` | Clave de API no válida. Las causas comunes incluyen:<br><br>- **Encabezado Authorization faltante o mal formado.** El valor del encabezado debe ser `Bearer` seguido de un espacio y luego tu clave de API: `Authorization: Bearer YOUR-API-KEY`. Los errores comunes incluyen omitir `Bearer`, omitir la clave después de `Bearer` o encerrar el valor entre comillas.<br>- **Endpoint REST incorrecto.** Estás enviando la solicitud a la [instancia]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints) incorrecta. Por ejemplo, si tu cuenta está en nuestra instancia de la UE (`https://dashboard-01.braze.eu`), la solicitud debe enviarse a `https://rest.fra-01.braze.eu`.<br>- **Permisos insuficientes.** Cada clave de API tiene un alcance definido para un espacio de trabajo y un conjunto de permisos específicos. Verifica los permisos de la clave en **Configuración** > **Claves de API** en el panel.<br>- **Clave de API incorrecta.** Las claves de API son específicas del espacio de trabajo. Una clave de un espacio de trabajo no se puede utilizar para autenticar solicitudes de un espacio de trabajo diferente. |
| `403 Forbidden` | El plan de tarifas no lo admite, o la cuenta está inactivada.|
| `403 Access Denied` | La clave de REST API que estás utilizando no tiene permisos suficientes. Las causas comunes incluyen: {::nomarkdown}<ul><li><strong>La clave de API es anterior a la característica.</strong> Si la clave de API se creó antes de que se lanzara una característica (como los grupos de suscripción o los catálogos), la clave no hereda automáticamente esos permisos. Crea una nueva clave de API con los permisos necesarios en <strong>Configuración</strong> &gt; <strong>Claves de API</strong>.</li><li><strong>Falta el permiso específico del endpoint.</strong> Cada endpoint de API requiere un alcance de permiso específico (por ejemplo, <code>users.track</code> o <code>email.status</code>). Verifica que los permisos de la clave coincidan con el endpoint al que estás llamando.</li><li><strong>Barra diagonal al final o error tipográfico en la URL.</strong> Por ejemplo, <code>/users/track/</code> (con una barra diagonal al final) en lugar de <code>/users/track</code> puede producir errores inesperados.</li></ul>{:/}|
| `404 Not Found` | URL no válida. |
| `415 Unsupported Media Type` | El encabezado de solicitud `Content-Type` falta o es incorrecto. En la página de **Configuración**, añade `Content-Type` con un valor de `application/json`. |
| `429 Rate Limited` | Se excedió el límite de velocidad. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Errores fatales" }

### Error al analizar el cuerpo de la solicitud {#error-while-parsing-request-body}

Braze devuelve HTTP 400 cuando el cuerpo de la solicitud no es un JSON válido. Esto se aplica a los endpoints REST que aceptan un cuerpo JSON, como POST, PUT y PATCH.

El campo `error` incluye un mensaje indicando que debes pasar `application/json` válido en el cuerpo de la solicitud. También puedes ver `Error while parsing request body. Please check your syntax.`

Las causas comunes incluyen comas al final, comentarios dentro del JSON, cadenas entre comillas simples, una llave de apertura `{` adicional antes de la carga útil o el envío de una cadena concatenada en lugar de un objeto codificado en JSON.

Antes de reintentar:

1. Valida la carga útil con un validador de JSON.
2. Establece `Content-Type: application/json` y envía JSON codificado en UTF-8.
3. Confirma que tu cliente HTTP codifica el objeto en JSON en lugar de concatenar cadenas sin procesar.

Para los límites de tamaño de carga útil y de objetos por solicitud de `/users/track`, consulta [¿Por qué obtengo `400 Bad Request` con un error de sintaxis o análisis?]({{site.baseurl}}/api/endpoints/user_data/post_user_track#why-do-i-get-400-bad-request-with-a-bad-syntax-or-parse-error).