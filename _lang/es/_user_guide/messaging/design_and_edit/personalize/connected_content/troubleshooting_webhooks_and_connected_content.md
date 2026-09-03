---
nav_title: Solución de problemas de webhooks y contenido conectado
article_title: Solución de problemas de solicitudes de webhook y contenido conectado
page_order: 4
description: "Diagnostica errores de webhooks y contenido conectado usando un índice de síntomas, tablas de errores HTTP y orientación sobre la detección de hosts no saludables."
---

# Solución de problemas de solicitudes de webhook y contenido conectado {#troubleshoot-webhook-and-connected-content-requests}

> Usa esta página para solucionar problemas de códigos de error comunes de webhooks y contenido conectado. Para la configuración, consulta [Crear un webhook]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook) y [Realizar una llamada a la API]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call). Para inspeccionar una solicitud de contenido conectado en la vista previa, consulta [Depurador de contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/debugger).

## Empieza aquí: Identifica tu síntoma {#start-here-match-your-symptom}

Identifica tu síntoma en la tabla para navegar a la sección relevante.

| Síntoma | Ir a |
| --- | --- |
| Error de cliente `4XX` en el registro de actividad de mensajes | [Errores 4XX](#4xx-errors) |
| Error de servidor `5XX` o tiempo de espera agotado | [Errores 5XX](#5xx-errors) |
| `598 Host Unhealthy` o solicitudes detenidas brevemente | [Detección de host no saludable](#unhealthy-host-detection) |
| El contenido conectado aparece en blanco en la vista previa o el envío | [El contenido conectado no devuelve cuerpo de respuesta](#connected-content-returns-no-response-body) |
| Necesitas inspeccionar una solicitud de contenido conectado en la vista previa | [Depurador de contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/debugger) |
| Correo electrónico automatizado de Braze | [Correos electrónicos automatizados y entradas del registro de actividad de mensajes](#automated-emails-and-message-activity-log-entries) |
| Necesitas eventos de fallo de webhook en Currents | [Información adicional sobre fallos en Braze Currents](#additional-failure-insights-in-braze-currents) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Síntoma de webhook y contenido conectado" }

## Ruta de investigación estándar {#standard-investigation-path}

Utiliza este flujo de trabajo cuando una solicitud de webhook o contenido conectado falle o se represente de forma incorrecta. Empieza en el paso 1.

1. Abre el [registro de actividad de mensajes]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) y anota el código de error, la marca de tiempo y la URL del endpoint.
2. Para errores `4XX`, verifica la sintaxis de la solicitud, los encabezados de autenticación, la ruta de la URL y el método HTTP con la documentación del endpoint.
3. Para errores `5XX`, comprueba el estado del endpoint, los límites de velocidad y si Braze marcó el host como no saludable.
4. Para contenido conectado, previsualiza el mensaje para un usuario de prueba. Usa el [depurador de contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/debugger) para inspeccionar la solicitud y la respuesta, y confirma que Liquid no se resuelve con valores en blanco o que rompan el JSON.
5. Si la detección de hosts no saludables puede estar implicada, revisa [Detección de hosts no saludables](#unhealthy-host-detection) antes de ponerte en contacto con [soporte de Braze]({{site.baseurl}}/support_contact).

## Errores 4XX {#4xx-errors}

Los errores `4XX` indican que hay un problema con la solicitud enviada al endpoint. Estos errores suelen deberse a solicitudes erróneas, incluidos parámetros con formato incorrecto, encabezados de autenticación faltantes o URL incorrectas. Ten en cuenta que estos errores también se aplican al [generador de informes]({{site.baseurl}}/user_guide/analytics/reports/report_builder).

Consulta la siguiente tabla para obtener detalles sobre los códigos de error y los pasos para resolverlos:

<style>
table td {
    word-break: break-word;
}
</style>

<table aria-label="Errores 4XX">
  <thead>
    <tr>
      <th>Código de error</th>
      <th>Qué significa</th>
      <th>Pasos para resolverlo</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>400 Bad Request</b></td>
      <td>La sintaxis de la solicitud no es válida.</td>
      <td>
        <ul>
          <li>Verifica la carga útil de la solicitud en busca de errores de sintaxis.</li>
          <li>Confirma que todos los campos obligatorios están incluidos y con el formato correcto.</li>
          <li>Si estás enviando una carga útil JSON, valida la estructura del JSON.</li>
          <li>Si estás usando Liquid para incluir etiquetas de personalización en la solicitud de webhook, verifica que el Liquid no se resuelva con un valor en blanco ni produzca caracteres que rompan el JSON (como comillas sin escapar). Previsualiza el mensaje para un usuario de prueba y confirma que la salida renderizada es válida.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>401 Unauthorized</b></td>
      <td>La solicitud requiere autenticación de usuario.</td>
      <td>
        <ul>
          <li>Verifica que las credenciales de autenticación correctas (como claves de API o tokens) estén incluidas en los encabezados de la solicitud.</li>
          <li>Confirma que tienes los permisos de usuario para acceder al endpoint.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>403 Forbidden</b></td>
      <td>El endpoint entiende la solicitud, pero se niega a autorizarla.</td>
      <td>
        <ul>
          <li>Verifica si la clave de API o el token tiene los permisos necesarios.</li>
          <li>Confirma que tienes los permisos de usuario para acceder al endpoint.</li>
          <li>Si las solicitudes devuelven consistentemente <code>403</code> y la autenticación parece correcta, es posible que tu servidor, puerta de enlace de API o WAF esté bloqueando las direcciones IP de salida de Braze. Añade las IP de tu clúster de Braze a la lista de permitidos. Para webhooks, consulta <a href="{{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook#ip-allowlisting">Lista de IP permitidas</a>. Para contenido conectado, consulta <a href="{{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call#connected-content-ip-allowlisting">Lista de IP permitidas de contenido conectado</a>.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>404 Not Found</b></td>
      <td>El endpoint no puede encontrar el recurso solicitado.</td>
      <td>
        <ul>
          <li>Verifica la URL del endpoint en busca de errores tipográficos o rutas incorrectas.</li>
          <li>Confirma que el recurso al que intentas acceder existe.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>405 Method Not Allowed</b></td>
      <td>El endpoint conoce el método de solicitud, pero el recurso de destino no lo admite.</td>
      <td>
        <ul>
          <li>Verifica el método HTTP (DELETE, GET, POST, PUT) utilizado en la solicitud.</li>
          <li>Confirma que el endpoint admite el método que estás usando.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>408 Request Timeout</b></td>
      <td>El endpoint agotó el tiempo de espera al procesar la solicitud.</td>
      <td>
        <ul>
          <li>Verifica el método HTTP (DELETE, GET, POST, PUT) utilizado en la solicitud.</li>
          <li>Confirma que el endpoint admite el método que estás usando.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>409 Conflict</b></td>
      <td>La solicitud está incompleta debido a un conflicto con el estado actual del recurso.</td>
      <td>
        <ul>
          <li>Verifica el método HTTP (DELETE, GET, POST, PUT) utilizado en la solicitud.</li>
          <li>Confirma que el endpoint admite el método que estás usando.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>429 Too Many Requests</b></td>
      <td>Se han enviado demasiadas solicitudes en un período de tiempo determinado.</td>
      <td>
        <ul>
          <li>Reduce el límite de velocidad en tu Campaign o paso en Canvas.</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

## Errores 5XX {#5xx-errors}

Los errores `5XX` indican que hay un problema con el endpoint. Estos errores suelen deberse a problemas del lado del servidor.

| Código de error                    | Qué significa                                                                                                                                         |
|-------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| **500 Internal Server Error** | El endpoint encontró una condición inesperada que le impidió completar la solicitud.                                                       |
| **502 Bad Gateway**           | El endpoint recibió una respuesta no válida del servidor ascendente.                                                                                   |
| **503 Service Unavailable**   | El endpoint no puede gestionar la solicitud en este momento debido a una sobrecarga temporal o mantenimiento.                                                    |
| **504 Gateway Timeout**       | El endpoint no recibió una respuesta oportuna del servidor ascendente.                                                                               |
| **529 Host Overloaded**       | El host del endpoint está sobrecargado y no pudo responder. |
| **598 Host Unhealthy**        | Braze simuló la respuesta porque el host del endpoint está temporalmente marcado como no saludable. Para más información, consulta [Detección de hosts no saludables](#unhealthy-host-detection). |
| **599 Connection Error**      | Braze experimentó un error de tiempo de espera de conexión de red al intentar establecer una conexión con el endpoint, lo que significa que el endpoint puede ser inestable o estar caído. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Errores 5XX" }

### Resolución de errores 5XX {#resolving-5xx-errors}

Aquí tienes algunos consejos para la solución de problemas de los errores `5XX` más comunes:

- Revisa el mensaje de error en busca de detalles específicos disponibles en el **Registro de actividad de mensajes**. Para webhooks, ve a la sección **Performance Over Time** en la página de inicio de Braze y selecciona las estadísticas de webhooks. Desde ahí, puedes encontrar la marca de tiempo que indica cuándo ocurrieron los errores.
- Asegúrate de que no estás enviando demasiadas solicitudes que sobrecarguen el endpoint. Puedes enviar en lotes o ajustar el límite de velocidad para comprobar si esto reduce los errores.

## Detección de host no saludable {#unhealthy-host-detection}

Los webhooks y el contenido conectado de Braze emplean un mecanismo de detección de host no saludable para detectar cuándo el host de destino experimenta una alta tasa de lentitud significativa o sobrecarga que resulta en tiempos de espera agotados, demasiadas solicitudes u otros resultados que impiden a Braze comunicarse exitosamente con el endpoint de destino. Actúa como una protección para reducir la carga innecesaria que puede estar causando problemas al host de destino. También sirve para estabilizar la infraestructura de Braze y mantener velocidades de mensajería rápidas.

Los umbrales de detección difieren entre webhooks y contenido conectado:
- **Para webhooks**: Si el número de fallos supera los 3000 en cualquier ventana de tiempo móvil de un minuto (por combinación única de nombre de host y grupo de aplicaciones&#8212;no por ruta de endpoint), Braze detiene temporalmente las solicitudes al host de destino durante un minuto.
- **Para contenido conectado**: Si el número de fallos supera los 3000 Y la tasa de error supera el 90 % en cualquier ventana de tiempo móvil de un minuto (por combinación única de nombre de host y grupo de aplicaciones&#8212;no por ruta de endpoint), Braze detiene temporalmente las solicitudes al host de destino durante un minuto.

Cuando las solicitudes se detienen, Braze simula respuestas con un código de error `598` para indicar el mal estado de salud. Después de un minuto, Braze reanuda las solicitudes a velocidad completa si se determina que el host está saludable. Si el host sigue no saludable, Braze espera otro minuto antes de intentarlo de nuevo.

Los siguientes códigos de error contribuyen al recuento de fallos del detector de host no saludable: `408`, `429`, `502`, `503`, `504`, `529`.

Para webhooks, Braze reintenta automáticamente las solicitudes HTTP que fueron detenidas por el detector de host no saludable. Este reintento automático utiliza retirada exponencial y solo reintenta unas pocas veces antes de fallar. Para más información sobre errores de webhook, consulta [Errores, lógica de reintentos y tiempos de espera]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook#errors-retry-logic-and-timeouts).

Para contenido conectado, si las solicitudes al host de destino son detenidas por el detector de host no saludable, Braze continúa renderizando mensajes y siguiendo tu lógica Liquid como si hubiera recibido un código de respuesta de error. Si quieres asegurarte de que estas solicitudes de contenido conectado se reintenten cuando son detenidas por el detector de host no saludable, usa la opción `:retry`. Para más información sobre la opción `:retry`, consulta [Reintentos de contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/connected_content_retries).

Si crees que la detección de host no saludable puede estar causando problemas, ponte en contacto con [soporte de Braze]({{site.baseurl}}/support_contact).

### El contenido conectado no devuelve cuerpo de respuesta {#connected-content-returns-no-response-body}

**Síntoma:** Una llamada de contenido conectado se renderiza en blanco en la vista previa o el envío de tu mensaje.

Si una llamada de contenido conectado se renderiza en blanco en la vista previa o el envío de tu mensaje, usa el [Depurador de contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/debugger) para inspeccionar la solicitud y la respuesta, y luego comprueba lo siguiente:

- **Espacios de no separación en la URL:** Braze elimina los espacios de no separación (`&nbsp;` o Unicode `U+00A0`) de las URL de contenido conectado antes de realizar la solicitud. Si tu URL fue copiada de un documento o campo del panel que insertó espacios de no separación entre caracteres, la solicitud puede fallar o no devolver un cuerpo utilizable. Vuelve a escribir la URL en texto plano o elimina los espacios ocultos, y luego previsualiza de nuevo.
- **Respuestas de redirección (`3xx`):** El contenido conectado no sigue redirecciones. Solo las respuestas `2xx` se tratan como exitosas, por lo que un `301` o `302` puede renderizarse en blanco incluso cuando la misma URL funciona en Postman. Usa la URL de destino final o configura el endpoint para que devuelva una respuesta `2xx` (normalmente `200`) en la URL que Braze llama. Consulta [¿Por qué falla el contenido conectado cuando mi endpoint devuelve una redirección?]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call#why-does-connected-content-fail-when-my-endpoint-returns-a-redirect-301-or-302).
- **Errores HTTP y cuerpos vacíos:** Para códigos de estado fuera del rango `2xx` o hosts bloqueados, el contenido conectado puede renderizar una cadena vacía. Consulta [Realizar una llamada a la API]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call) y revisa los fallos en el **Registro de actividad de mensajes**.

## Correos electrónicos automatizados y entradas del registro de actividad de mensajes {#automated-emails-and-message-activity-log-entries}

### Configuración de correos electrónicos automatizados {#setting-up-automated-emails}

Si experimentas más de 100 000 errores de endpoint de webhook o contenido conectado (incluyendo reintentos) en un espacio de trabajo en un período de 24 horas, Braze te envía un correo electrónico que incluye la siguiente información sobre cómo resolver los errores.

- Nombre del espacio de trabajo
- Un enlace al Canvas o a la campaña
- URL del endpoint
- Código de error
- Hora en que se observó el error por última vez
- Enlaces al registro de actividad de mensajes y documentación relacionada

{% alert note %}
Puedes configurar el umbral de errores por espacio de trabajo. Para ajustar este umbral, ponte en contacto con [soporte de Braze]({{site.baseurl}}/support_contact).
{% endalert %}

Los errores de endpoint son:

- **`4XX`:** `400`, `401`, `403`, `404`, `405`, `408`, `409`, `429`
- **`5XX`:** `500`, `502`, `503`, `504`, `598`, `599`

Estos correos electrónicos solo se envían una vez al día a nivel de espacio de trabajo. Si ningún usuario se suscribe a estos correos electrónicos, Braze notifica a todos los administradores de la empresa.

Para suscribirte a recibir estos correos electrónicos, haz lo siguiente:

1. Ve a **Configuración** > **Configuración de administrador** > **Preferencias de notificación**.
2. Selecciona **Connected Content Errors** y **Webhook Errors** en la sección **Canvas & Campaigns**.

### Entradas del registro de actividad de mensajes {#message-activity-log-entries}

Si ocurre un fallo, hay al menos una entrada en el [Registro de actividad de mensajes]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) relacionada con él. Si la solicitud se reintenta y finalmente tiene éxito, esos detalles están disponibles en Currents y en el uso compartido de datos de Snowflake. Ten en cuenta que incluso si una solicitud finalmente tiene éxito después de un reintento, los errores aún pueden desencadenar el correo electrónico automatizado.

### Información adicional sobre fallos en Braze Currents {#additional-failure-insights-in-braze-currents}

Para aumentar la transparencia en problemas relacionados con webhooks, Braze transmite eventos detallados de fallos de webhook a Currents y al uso compartido de datos de Snowflake. Estos eventos incluyen solicitudes de webhook fallidas (como respuestas HTTP `4xx` o `5xx`), proporcionando mayor observabilidad sobre cómo los problemas de webhook pueden afectar la entrega de mensajes. Ten en cuenta que los eventos de fallo incluyen tanto errores terminales como errores que se están reintentando.

{% alert note %}
Las solicitudes de contenido conectado no están incluidas en estos eventos de fallo de webhook.
{% endalert %}

Para más información, consulta el [Glosario de eventos de interacción con mensajes]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events).