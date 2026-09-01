---
nav_title: Alertas de uso de API
article_title: Alertas de uso de la API
description: "Este artículo ofrece un resumen de las alertas de uso de la API, que te permiten detectar de forma proactiva el tráfico inesperado."
page_order: 0
---

# Alertas de uso de API {#api-usage-alerts}

> Las alertas de uso de API proporcionan una visibilidad crítica del uso de tus API, lo que te permite detectar de forma proactiva el tráfico inesperado. Al configurar estas alertas para realizar el seguimiento de los volúmenes de solicitudes API clave, podrás recibir notificaciones en tiempo real y resolver los problemas antes de que afecten a tus campañas de marketing.

## Acerca de las alertas de uso de API {#about-api-usage-alerts}

Puedes usar las alertas de uso de API para monitorizar los volúmenes de solicitudes en las siguientes categorías:

| Categoría de API | Detalles |
|--------------|---------|
| Endpoints de REST API | Realiza el seguimiento del uso de todas las llamadas a la REST API realizadas al backend de Braze, como el envío de mensajes, la creación de Campaigns o la exportación de usuarios. |
| Solicitudes de API del SDK | Realiza el seguimiento de las solicitudes de API realizadas desde los SDK de Braze en las aplicaciones del cliente, como desencadenar mensajes dentro de la aplicación o sincronizar datos de usuario.<br><br>_*Solo disponible para clientes que hayan adquirido usuarios activos al mes – CY 24-25._ |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Acerca de las alertas de uso de API" }

## Crear una alerta de uso de API {#creating-an-api-usage-alert}

Para crear una alerta de uso de API:

1. Ve a **Configuración** > **API e identificadores** > **Alertas de uso de API** y crea una nueva alerta.
2. Introduce un nombre para tu alerta y elige los endpoints de la REST API y las claves de API sobre los que deseas recibir alertas.
3. Define los criterios de tu alerta eligiendo uno o más códigos de respuesta y especificando los [umbrales de alerta](#api-usage-alert-thresholds).
4. Cuando hayas terminado, activa **Alerta habilitada**.
    ![Un ejemplo de una alerta de uso de API que envía notificaciones cuando el endpoint Track users aumenta en un 100 por ciento en una hora.]({% image_buster /assets/img/api_usage_alerts/api_usage_alerts1.png %})

## Umbrales de alerta {#api-usage-alert-thresholds}

Cuando definas los criterios de tu alerta, puedes ajustar los siguientes umbrales:

<table aria-label="Umbrales de alerta">
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
{: .reset-td-br-1 .reset-td-br-2 aria-label="Umbrales de alerta" }

## Configurar notificaciones de alerta {#setting-up-alert-notifications}

Puedes configurar una alerta por correo electrónico, una alerta por webhook o ambas. Las alertas por webhook pueden ser muy útiles para ejemplos como enviar una alerta a plataformas externas, como un canal de Slack. Para ver un ejemplo, consulta nuestra [documentación]({{site.baseurl}}/user_guide/administer/global/admin_settings/notification_preferences) sobre cómo integrar alertas con Slack para nuestras preferencias de notificación.

![Se enviará un correo electrónico a la dirección seleccionada cuando se alcancen los criterios de la alerta.]({% image_buster /assets/img/api_usage_alerts/api_usage_alerts2.png %})

### Carga útil de ejemplo {#payload}

A continuación se muestra una carga útil de ejemplo para el cuerpo de un webhook de alerta de uso de API.

```json
{
  "text": "Your My First API Usage Alert alert has triggered. Please note that this alert is reset every 8 hours, and only one notification will be sent per reset period. You can view your alert and usage here: <link>.",
  "data": {
    "alert_name": "My First API Usage Alert",
    "alert_type": "API Usage Alert",
    "app_group_name": "My Workspace",
    "alert_criteria": {
      "response_codes": "201, 202 and 203",
      "threshold_condition": "increase by",
      "threshold_volume": "50%",
      "within": "1 hour"
    },
    "timeframe_start": "2025-03-20 15:35:00",
    "timeframe_end": "2025-03-20 16:35:00",
    "volume": 1500,
    "previous_timeframe_start": "2025-03-20 14:35:00",
    "previous_timeframe_end": "2025-03-20 15:35:00",
    "previous_volume": 1000
  }
}
```

{% alert note %}
Los campos `previous_timeframe_start`, `previous_timeframe_end` y `previous_volume` son opcionales y solo aparecen cuando la alerta utiliza una condición de umbral comparativo (`increase by`, `decrease by`). Estos campos se omiten para las alertas `greater than or equal` o `less than or equal`.
{% endalert %}

#### Detalles de los campos de la carga útil {#payload-field-details}

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `text` | cadena | Mensaje de alerta legible para humanos. |
| `data.alert_name` | cadena | Nombre de la alerta. |
| `data.alert_type` | cadena | Tipo de alerta (siempre `"API Usage Alert"`). |
| `data.app_group_name` | cadena | Nombre del espacio de trabajo. |
| `data.alert_criteria.response_codes` | cadena | Códigos de respuesta seleccionados para la alerta. Devuelve `"all response codes"` si no se selecciona ninguno, un código único como `"201"`, o múltiples códigos como `"201, 202 and 203"`. |
| `data.alert_criteria.threshold_condition` | cadena | Tipo de condición: `"increase by"`, `"decrease by"`, `"greater than or equal"` o `"less than or equal"`. |
| `data.alert_criteria.threshold_volume` | cadena o número | Valor del umbral. Cuando la condición utiliza un porcentaje, es una cadena que termina en `%` (por ejemplo, `"50%"`). Cuando la condición utiliza un valor numérico, es un número (por ejemplo, `50`). |
| `data.alert_criteria.within` | cadena | Ventana de tiempo para la evaluación de la alerta (por ejemplo, `"1 day"`). |
| `data.timeframe_start` | cadena | Inicio del período de la alerta en formato UTC `YYYY-MM-DD HH:MM:SS`. |
| `data.timeframe_end` | cadena | Fin del período de la alerta en formato UTC `YYYY-MM-DD HH:MM:SS`. |
| `data.volume` | número | Volumen de solicitudes durante el período de la alerta. |
| `data.previous_timeframe_start` | cadena | (Opcional) Inicio del período anterior. Solo presente para condiciones de umbral comparativo. |
| `data.previous_timeframe_end` | cadena | (Opcional) Fin del período anterior. Solo presente para condiciones de umbral comparativo. |
| `data.previous_volume` | número | (Opcional) Volumen de solicitudes durante el período anterior. Solo presente para condiciones de umbral comparativo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Detalles de los campos de la carga útil" }

### Alertas de ejemplo {#example-alerts}

A continuación se muestran algunas formas de configurar tus alertas de uso de API para recibir notificaciones en los siguientes escenarios.

{% tabs local %}
{% tab Salud de la API %}
Puedes configurar alertas para supervisar el estado general de tu API. Por ejemplo, puedes configurar estas alertas cuando los errores de API aumenten drásticamente, como un 20 % respecto a la hora anterior.

| Endpoint | Clave de API | Código de respuesta | Condición del umbral | Volumen del umbral | Dentro de |
| --- | --- | --- | --- | --- | --- |
| Todos los endpoints | Todas las claves de API | `4XX` y `5XX` | Aumento del 10 % | 10 | 1 hora |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 aria-label="Alertas de ejemplo" }
{% endtab %}

{% tab Límite de velocidad del endpoint %}
Recibe una alerta cuando tu espacio de trabajo alcance su límite de velocidad para el endpoint `/users/track`. También puedes aplicar esta configuración a otros endpoints de Braze.

| Endpoint | Clave de API | Código de respuesta | Condición del umbral | Volumen del umbral | Dentro de |
| --- | --- | --- | --- | --- | --- |
| `/users/track` | Todas las claves de API | `429` | Mayor o igual a | 100 | 1 hora |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 aria-label="Alertas de ejemplo" }
{% endtab %}

{% tab Campaigns activadas por API %}
Esta configuración de alerta te notifica cuando se producen errores en Campaigns y Canvas activados por API, algunos de los cuales pueden ser de alta prioridad.

| Endpoint | Clave de API | Código de respuesta | Condición del umbral | Volumen del umbral | Dentro de |
| --- | --- | --- | --- | --- | --- |
| {::nomarkdown}<ul><li><code>/campaigns/trigger/send</code></li><li><code>/canvas/trigger/send</code></li><li><code>/messages/send</code></li></ul>{:/} | Todas las claves de API | `4XX` y `5XX` | Mayor o igual a | 1 | 1 hora |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 aria-label="Alertas de ejemplo" }
{% endtab %}

{% tab Integraciones de partners %}
Utiliza la siguiente configuración de alerta para recibir una notificación cuando una integración de partner deje de enviar datos a Braze.

| Endpoint | Clave de API | Código de respuesta | Condición del umbral | Volumen del umbral | Dentro de |
| --- | --- | --- | --- | --- | --- |
| Todos los endpoints | La clave de API utilizada para tu integración del partner | Todos los códigos de respuesta | Menor o igual a | 0 | 1 día |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 aria-label="Alertas de ejemplo" }
{% endtab %}
{% endtabs %}

## Consideraciones {#considerations}

- Cada alerta activa solo enviará una notificación por correo electrónico o webhook una vez cada 8 horas. Esto es para evitar demasiadas notificaciones de una sola alerta. Si tu alerta te está notificando prematuramente, considera editar los criterios de la alerta para que se ajusten mejor a tu caso de uso.
- Puedes tener hasta 10 alertas por espacio de trabajo.