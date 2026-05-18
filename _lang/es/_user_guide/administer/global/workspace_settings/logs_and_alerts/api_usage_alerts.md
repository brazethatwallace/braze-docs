---
nav_title: Alertas de uso de API
article_title: Alertas de uso de la API
description: "Este artículo ofrece un resumen de las alertas de uso de la API, que te permiten detectar de forma proactiva el tráfico inesperado."
page_order: 0
---

# Alertas de uso de API {#api-usage-alerts}

> Las alertas de uso de API proporcionan una visibilidad crítica del uso de tus API, lo que te permite detectar de forma proactiva el tráfico inesperado. Al configurar estas alertas para realizar el seguimiento de los volúmenes de solicitudes API clave, podrás recibir notificaciones en tiempo real y resolver los problemas antes de que afecten a tus campañas de marketing.

## Acerca de las alertas de uso de API {#about-api-usage-alerts}

Puedes utilizar las alertas de uso de la API para supervisar los volúmenes de solicitudes de las siguientes categorías:

| Categoría API | Detalles |
|--------------|---------|
| Puntos finales de la REST API | Realiza un seguimiento del uso de todas las llamadas a la REST API realizadas al backend de Braze, como el envío de mensajes, la creación de Campaigns o la exportación de usuarios. |
| Solicitudes de API del SDK | Realiza un seguimiento de las solicitudes de API realizadas desde los SDK de Braze en las aplicaciones de los clientes, como la activación de mensajes dentro de la aplicación o la sincronización de datos de usuario.<br><br>_*Solo disponible para los clientes que hayan adquirido usuarios activos al mes – CY 24-25._ |
{: .reset-td-br-1 .reset-td-br-2 aria-label="About API usage alerts" }

## Creación de una alerta de uso de API {#creating-an-api-usage-alert}

Para crear una alerta de uso de la API:

1. Ve a **Configuración** > **API e identificadores** > **Alertas de uso de API** y crea una nueva alerta.
2. Introduce un nombre para tu alerta y elige los puntos finales de la REST API y las claves de API sobre las que deseas recibir alertas.
3. Define los criterios de tu alerta eligiendo uno o más códigos de respuesta y especificando los [umbrales de alerta](#api-usage-alert-thresholds).
4. Cuando hayas terminado, activa **Alert enabled**.
    ![Un ejemplo de una alerta de uso de API que envía notificaciones cuando el punto de conexión Track users aumenta un 100 por ciento en una hora.]({% image_buster /assets/img/api_usage_alerts/api_usage_alerts1.png %})

## Umbrales de alerta {#api-usage-alert-thresholds}

Cuando definas los criterios de tu alerta, puedes ajustar los siguientes umbrales:

<table aria-label="Alert thresholds #api-usage-alert-thresholds">
  <caption>Umbrales de alerta</caption>
  <thead>
    <tr>
      <th>Campo</th>
      <th>Descripción</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Condición del umbral</td>
      <td>
        Define las condiciones previas al volumen del umbral sobre el que deseas recibir alertas. Se admiten las siguientes:<br><br>
        <ul>
          <li><strong>Increased by</strong> o <strong>Decreased by</strong>: compara las solicitudes con la ventana de tiempo anterior.</li>
          <li><strong>Increased by percentage</strong> o <strong>Decreased by percentage</strong>: compara el cambio porcentual en las solicitudes con la ventana de tiempo anterior.</li>
          <li><strong>Greater than or equal</strong> o <strong>less than or equal</strong>: cuenta las solicitudes en una ventana de tiempo.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>Volumen del umbral</td>
      <td>Se utiliza junto con la condición del umbral.</td>
    </tr>
    <tr>
      <td>En</td>
      <td>La ventana de tiempo para la evaluación de la alerta.</td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 aria-label="Alert thresholds #api-usage-alert-thresholds" }

## Configuración de notificaciones de alerta {#setting-up-alert-notifications}

Puedes configurar una alerta por correo electrónico, una alerta por webhook o ambas. Las alertas por webhook pueden ser muy útiles para casos de uso como el envío de alertas a plataformas externas, como un canal de Slack. Para ver un ejemplo, consulta nuestra [documentación](https://www.braze.com/docs/user_guide/administer/global/admin_settings/notification_preferences#slack-incoming-webhook-integration) sobre la integración de alertas con Slack en nuestras preferencias de notificación.

![Se enviará un correo electrónico a la dirección seleccionada cuando se cumplan los criterios de la alerta.]({% image_buster /assets/img/api_usage_alerts/api_usage_alerts2.png %})

### Ejemplo de carga útil {#payload}

A continuación se muestra un ejemplo de carga útil para el cuerpo de un webhook de alerta de uso de API.

```json
{
  "data": {
    "alert_name": "My First API Usage Alert",
    "alert_type": "API Usage Alert",
    "alert_criteria": {
    	"response_codes": ["201", "202", "203"],
    	"threshold_condition": "Increased by %",
    	"threshold_volume": 50,
    	"within": "1 day"
    },
    "timeframe_start": "2025-03-20T15:35:00Z",
    "timeframe_end": "2025-03-20T16:35:00Z",
    "volume": 1500,
    "previous_timeframe_start": "2025-03-20T14:35:00Z",
    "previous_timeframe_end": "2025-03-20T15:35:00Z",
    "previous_volume": 1000
  },
  "text": "Your My First API Usage Alert alert has triggered. You can view your alert and usage here: <link>. Note that this alert will reset in 1 day, as each alert will only send one notification per 8 hours."
}
```

### Ejemplos de alertas {#example-alerts}

A continuación se muestran algunas formas de configurar tus alertas de uso de API para recibir notificaciones en los siguientes escenarios.

{% tabs local %}
{% tab Salud de la API %}
Puedes configurar alertas para supervisar el estado general de tu API. Por ejemplo, puedes configurar estas alertas cuando los errores de API aumenten drásticamente, como un 20 % respecto a la hora anterior.

| Punto de conexión | Clave de API | Código de respuesta | Condición del umbral | Volumen del umbral | En |
| --- | --- | --- | --- | --- | --- |
| Todos los puntos finales | Todas las claves de API | `4XX` y `5XX` | Aumentó en 10 % | 10 | 1 hora |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 aria-label="Example alerts" }
{% endtab %}

{% tab Límite de velocidad del punto de conexión %}
Recibe una alerta cuando tu espacio de trabajo alcance su límite de velocidad para el punto de conexión `/users/track`. También puedes aplicar esta configuración a otros puntos finales de Braze.

| Punto de conexión | Clave de API | Código de respuesta | Condición del umbral | Volumen del umbral | En |
| --- | --- | --- | --- | --- | --- |
| `/users/track` | Todas las claves de API | `429` | Mayor o igual que | 100 | 1 hora |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 aria-label="Example alerts" }
{% endtab %}

{% tab Campaigns desencadenadas por API %}
Esta configuración de alerta te notifica cuando se producen errores en Campaigns y Canvas desencadenados por API, algunos de los cuales pueden ser de alta prioridad.

| Punto de conexión | Clave de API | Código de respuesta | Condición del umbral | Volumen del umbral | En |
| --- | --- | --- | --- | --- | --- |
| {::nomarkdown}<ul><li><code>/campaigns/trigger/send</code></li><li><code>/canvas/trigger/send</code></li><li><code>/messages/send</code></li></ul>{:/} | Todas las claves de API | `4XX` y `5XX` | Mayor o igual que | 1 | 1 hora |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 aria-label="Example alerts" }
{% endtab %}

{% tab Integraciones de socios %}
Utiliza la siguiente configuración de alerta para recibir una notificación cuando una integración de socio deje de enviar datos a Braze.

| Punto de conexión | Clave de API | Código de respuesta | Condición del umbral | Volumen del umbral | En |
| --- | --- | --- | --- | --- | --- |
| Todos los puntos finales | La clave de API utilizada para tu integración del socio | Todos los códigos de respuesta | Menor o igual que | 0 | 1 día |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 aria-label="Example alerts" }
{% endtab %}
{% endtabs %}

## Consideraciones {#considerations}

- Cada alerta activa solo enviará una notificación por correo electrónico o webhook una vez cada 8 horas. Esto es para evitar demasiadas notificaciones de una sola alerta. Si tu alerta te notifica prematuramente, considera editar los criterios de la alerta para que se ajusten mejor a tu caso de uso.
- Puedes tener hasta 10 alertas por espacio de trabajo.