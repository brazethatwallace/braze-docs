---
nav_title: Solución de problemas de webhook y solicitudes de contenido conectado
article_title: Solución de problemas de webhook y solicitudes de contenido conectado
page_order: 3
channel:
  - webhooks
description: "Este artículo explica cómo solucionar los códigos de error de webhook y contenido conectado, incluyendo cuáles son los errores y los pasos para resolverlos."
---

# Solución de problemas de webhook y solicitudes de contenido conectado {#troubleshoot-webhook-and-connected-content-requests}

> Este artículo explica cómo solucionar los códigos de error más comunes de los webhooks y el contenido conectado, y ofrece más explicaciones sobre cómo pueden producirse estos errores en tus solicitudes.

## Errores 4XX {#4xx-errors}

Los errores `4XX` indican que hay un problema con la solicitud enviada al punto de conexión. Estos errores suelen deberse a solicitudes erróneas, como parámetros mal formados, omisión de encabezados de autenticación o URL incorrectas. Ten en cuenta que estos errores también se aplican al [Generador de informes]({{site.baseurl}}/user_guide/analytics/reports/report_builder/).

Consulta la tabla siguiente para ver los detalles del código de error y los pasos para solucionarlo:

<style>
table td {
    word-break: break-word;
}
</style>

<table aria-label="Errores 4XX">
  <caption>Errores 4XX</caption>
  <thead>
    <tr>
      <th>Código de error</th>
      <th>Qué significa</th>
      <th>Pasos para resolver</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>400 Bad Request</b></td>
      <td>Hay una sintaxis no válida en la solicitud.</td>
      <td>
        <ul>
          <li>Comprueba que la carga útil de la solicitud no contenga errores de sintaxis.</li>
          <li>Confirma que todos los campos obligatorios están incluidos y correctamente formateados.</li>
          <li>Si envías una carga útil JSON, valida la estructura JSON.</li>
          <li>Si usas Liquid para incluir etiquetas de personalización en la solicitud del webhook, verifica que el Liquid no se resuelva como un valor en blanco ni produzca caracteres que rompan el JSON (como comillas sin escapar). Previsualiza el mensaje para un usuario de prueba y confirma que la salida renderizada es válida.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>401 Unauthorized</b></td>
      <td>La solicitud requiere la autenticación del usuario.</td>
      <td>
        <ul>
          <li>Comprueba que se incluyen las credenciales de autenticación correctas (como claves de API o tokens) en los encabezados de solicitud.</li>
          <li>Confirma que tienes los permisos de usuario para acceder al punto de conexión.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>403 Forbidden</b></td>
      <td>El punto de conexión entiende la solicitud pero se niega a autorizarla.</td>
      <td>
        <ul>
          <li>Comprueba si la clave de API o el token tienen los permisos necesarios.</li>
          <li>Confirma que tienes los permisos de usuario para acceder al punto de conexión.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>404 Not Found</b></td>
      <td>El punto de conexión no puede encontrar el recurso solicitado.</td>
      <td>
        <ul>
          <li>Comprueba si la URL del punto de conexión contiene errores tipográficos o rutas incorrectas.</li>
          <li>Confirma que el recurso al que intentas acceder existe.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>405 Method Not Allowed</b></td>
      <td>El método de solicitud es conocido por el punto de conexión, pero no es compatible con el recurso de destino.</td>
      <td>
        <ul>
          <li>Comprueba el método HTTP (DELETE, GET, POST, PUT) utilizado en la solicitud.</li>
          <li>Confirma que el punto de conexión admite el método que estás utilizando.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>408 Request Timeout</b></td>
      <td>El punto de conexión ha agotado el tiempo de procesamiento de la solicitud.</td>
      <td>
        <ul>
          <li>Comprueba el método HTTP (DELETE, GET, POST, PUT) utilizado en la solicitud.</li>
          <li>Confirma que el punto de conexión admite el método que estás utilizando.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>409 Conflict</b></td>
      <td>La solicitud está incompleta debido a un conflicto con el estado actual del recurso.</td>
      <td>
        <ul>
          <li>Comprueba el método HTTP (DELETE, GET, POST, PUT) utilizado en la solicitud.</li>
          <li>Confirma que el punto de conexión admite el método que estás utilizando.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>429 Too Many Requests</b></td>
      <td>Se envían demasiadas solicitudes en un tiempo determinado.</td>
      <td>
        <ul>
          <li>Reduce el límite de velocidad en tu campaña o paso en Canvas.</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

## Errores 5XX {#5xx-errors}

Los errores `5XX` indican que hay un problema con el punto de conexión. Estos errores suelen deberse a problemas del servidor.

| Código de error | Qué significa |
|-------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| **500 Internal Server Error** | El punto de conexión encontró una condición inesperada que le impidió completar la solicitud. |
| **502 Bad Gateway** | El punto de conexión recibió una respuesta no válida del servidor ascendente. |
| **503 Service Unavailable** | El punto de conexión no puede gestionar actualmente la solicitud debido a una sobrecarga temporal o a mantenimiento. |
| **504 Gateway Timeout** | El punto de conexión no recibió una respuesta oportuna del servidor ascendente. |
| **529 Host Overloaded** | El host del punto de conexión está sobrecargado y no pudo responder. |
| **598 Host Unhealthy** | Braze simuló la respuesta porque el host del punto de conexión está marcado temporalmente como en mal estado. Consulta [Detección de host en mal estado](#unhealthy-host-detection) para más información. |
| **599 Connection Error** | Braze experimentó un error de tiempo de espera de conexión de red al intentar establecer una conexión con el punto de conexión, lo que significa que el punto de conexión puede ser inestable o estar caído. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Errores 5XX" }

### Resolver errores 5XX {#resolving-5xx-errors}

Aquí tienes consejos para la solución de problemas comunes de errores `5XX`:

- Revisa el mensaje de error para ver los detalles específicos disponibles en el **Registro de actividad de mensajes**. Para los webhooks, ve a la sección **Performance Over Time** de la página de inicio de Braze y selecciona las estadísticas de los webhooks. Desde aquí, puedes encontrar la marca de tiempo que indica cuándo se produjeron los errores.
- Asegúrate de no enviar demasiadas solicitudes que sobrecarguen el punto de conexión. Puedes enviar por lotes o ajustar el límite de velocidad para comprobar si así se reducen los errores.

## Detección de host en mal estado {#unhealthy-host-detection}

Los webhooks de Braze y el contenido conectado emplean un mecanismo de detección de host en mal estado para detectar cuando el host de destino experimenta una alta tasa de lentitud significativa o una sobrecarga que provoca tiempos de espera, demasiadas solicitudes u otros resultados que impiden que Braze se comunique correctamente con el punto de conexión de destino. Actúa como salvaguarda para reducir la carga innecesaria que pueda estar causando dificultades al host de destino. También sirve para estabilizar la infraestructura de Braze y mantener velocidades rápidas de mensajería.

Los umbrales de detección difieren entre los webhooks y el contenido conectado:
- **Para webhooks**: Si el número de **fallos supera los 3.000 en cualquier ventana de tiempo móvil de un minuto** (por combinación única de nombre de host y grupo de aplicaciones&#8212;**no** por ruta de punto de conexión), Braze detendrá temporalmente las solicitudes al host de destino durante un minuto.
- **Para contenido conectado**: Si el número de **fallos supera los 3.000 Y la tasa de error supera el 90 % en cualquier ventana de tiempo móvil de un minuto** (por combinación única de nombre de host y grupo de aplicaciones&#8212;**no** por ruta de punto de conexión), Braze detendrá temporalmente las solicitudes al host de destino durante un minuto.

Cuando las solicitudes se detienen, Braze simula respuestas con un código de error `598` para indicar el mal estado. Al cabo de un minuto, Braze reanudará las solicitudes a toda velocidad si se comprueba que el host está en buen estado. Si el host sigue en mal estado, Braze esperará otro minuto antes de volver a intentarlo.

Los siguientes códigos de error contribuyen al recuento de fallos del detector de host en mal estado: `408`, `429`, `502`, `503`, `504`, `529`.

Para los webhooks, Braze reintentará automáticamente las solicitudes HTTP que fueron detenidas por el detector de host en mal estado. Este reintento automático utiliza una retirada exponencial y solo lo intentará unas pocas veces antes de fallar. Para más información sobre los errores de webhook, consulta [Errores, lógica de reintentos y tiempos de espera]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#errors-retry-logic-and-timeouts).

Para el contenido conectado, si las solicitudes al host de destino se detienen por el detector de host en mal estado, Braze continuará renderizando mensajes y seguirá tu lógica Liquid como si hubiera recibido un código de respuesta de error. Si quieres asegurarte de que estas solicitudes de contenido conectado se reintentan cuando son detenidas por el detector de host en mal estado, utiliza la opción `:retry`. Para más información sobre la opción `:retry`, consulta [Reintentos de contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/connected_content_retries/).

Si crees que la detección de host en mal estado puede estar causando problemas, ponte en contacto con [soporte de Braze]({{site.baseurl}}/support_contact/).

## Correos electrónicos automatizados y entradas en el registro de actividad de mensajes {#automated-emails-and-message-activity-log-entries}

### Configuración de correos electrónicos automatizados {#setting-up-automated-emails}

Si experimentas más de 100.000 errores de webhook o de punto de conexión de contenido conectado (incluidos los reintentos) en un espacio de trabajo en un periodo de 24 horas, recibirás un correo electrónico con la siguiente información sobre cómo resolver los errores.

- Nombre del espacio de trabajo
- Un enlace al Canvas o a la campaña
- URL del punto de conexión
- Código de error
- Hora en que se observó el error por última vez
- Enlaces al Registro de actividad de mensajes y documentación relacionada

{% alert note %}
Puedes configurar el umbral de error por espacio de trabajo. Para ajustar este umbral, ponte en contacto con [soporte de Braze]({{site.baseurl}}/support_contact/).
{% endalert %}

Los errores del punto de conexión son:

- **`4XX`:** `400`, `401`, `403`, `404`, `405`, `408`, `409`, `429`
- **`5XX`:** `500`, `502`, `503`, `504`, `598`, `599`

Estos correos electrónicos solo se envían una vez al día a nivel de espacio de trabajo. Si ningún usuario se registra para recibir estos correos electrónicos, se notificará a todos los administradores de la empresa.

Para registrarte y recibir estos correos electrónicos, haz lo siguiente:

1. Ve a **Settings** > **Admin Settings** > **Notification Preferences**.
2. Selecciona **Connected Content Errors** y **Webhook Errors** en la sección **Canvas & Campaigns**.

### Entradas del registro de actividad de mensajes {#message-activity-log-entries}

Si se produce un fallo, habrá al menos una entrada en el [Registro de actividad de mensajes]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log/) relacionada con él. Si la solicitud se reintenta y finalmente tiene éxito, esos detalles estarán disponibles en Currents y Snowflake Data Share. Ten en cuenta que, aunque una solicitud finalmente tenga éxito tras un reintento, los errores pueden seguir activando el correo electrónico automatizado.

### Información adicional sobre fallos en Braze Currents {#additional-failure-insights-in-braze-currents}

Para aumentar la transparencia de los problemas relacionados con los webhooks, Braze transmite eventos detallados de fallos de webhooks a Currents y Snowflake Data Sharing. Estos eventos incluyen solicitudes de webhook fallidas (como respuestas HTTP `4xx` o `5xx`), lo que proporciona mayor capacidad de observación sobre cómo los problemas de webhook pueden afectar a la entrega de mensajes. Ten en cuenta que los eventos de fallo incluyen errores terminales, así como errores que se están reintentando.

{% alert note %}
Las solicitudes de contenido conectado no se incluyen en estos eventos de fallo de webhook.
{% endalert %}

Para más información, consulta el [glosario de eventos de interacción con mensajes]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/).