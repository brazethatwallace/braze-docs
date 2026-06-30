---
nav_title: Preferencias de notificación
article_title: Preferencias de notificación
page_order: 1
page_type: reference
description: "Este artículo de referencia cubre las opciones disponibles para supervisar la mensajería y la actividad en la cuenta de tu empresa."

---

# Preferencias de notificación {#notification-preferences}

> Si quieres supervisar la mensajería y la actividad en la cuenta de tu empresa, puedes optar por configurar notificaciones específicas y seleccionar a dónde van.

La página **Preferencias de notificación** es donde puedes configurar quién (si alguien) recibe notificaciones sobre tu empresa. Puedes configurar quién debe recibir notificaciones sobre la entrega de campañas o errores técnicos. También puedes especificar destinatarios para el informe de análisis semanal. Para la mayoría de las notificaciones, Braze admite canales de correo electrónico y webhook.

Para acceder a esta página, ve a **Configuración** > **Configuración de administrador** > **Preferencias de notificación**.

{% alert tip %}
También puedes integrarte con Slack para recibir notificaciones. Para conocer los pasos, consulta [Enviar mensajes utilizando webhooks entrantes](https://api.slack.com/incoming-webhooks).
{% endalert %}

## Notificaciones disponibles {#available-notifications}

La siguiente tabla describe las notificaciones disponibles y qué canales se utilizan para entregarlas.

{% alert note %}
Dependiendo del tipo de notificación, **All Dashboard Users** y **All Admins** podrían no aparecer en el menú desplegable de destinatarios. Puedes escribirlos manualmente; los valores de destinatario distinguen entre mayúsculas y minúsculas y deben coincidir exactamente. Para dashboards localizados fuera del inglés, utiliza la etiqueta de destinatario exacta que Braze muestra cuando hay sugerencias disponibles para esa notificación, en lugar de traducir la frase tú mismo.
{% endalert %}

| Notificación | Descripción | Canales de notificación disponibles |
|--------------|-------------|-----------------|
| Alertas de uso de API | Al seleccionar esta opción, accedes al **dashboard de uso de API**, donde puedes ir a la pestaña [**Alertas de uso de API**]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/api_usage_alerts) y configurar alertas para rastrear los volúmenes clave de solicitudes de API. | Correo electrónico, Webhook |
| Errores de credenciales de AWS | Notifica a los destinatarios cuando Braze recibe un error al intentar usar tus credenciales de Amazon Web Services para una exportación de datos. Esto incluye notificaciones de errores de credenciales para Google Cloud Storage y Azure (Microsoft Cloud Services). | Correo electrónico, Webhook |
| Campaign detenida automáticamente | Notifica a los destinatarios cuando Braze ha detenido una Campaign. | Correo electrónico |
| Canvas detenido automáticamente | Notifica a los destinatarios cuando Braze ha detenido un Canvas. | Correo electrónico |
| Expiración de interacción de Campaign | Notifica a los destinatarios sobre cualquier Campaign cuya información de interacción esté próxima a expirar, junto con información sobre Segments, Campaigns o Canvas que la referencien en un filtro de reorientación y que se hayan utilizado para enviar un mensaje en los últimos 30 días. | Correo electrónico |
| Campaign/Canvas actualizado | Notifica a los destinatarios cuando una Campaign o un Canvas activo se actualiza o desactiva, así como cuando una Campaign o un Canvas inactivo se reactiva o se lanzan borradores. | Correo electrónico |
| Límite de volumen de Campaign/Canvas alcanzado | Notifica a los destinatarios cuando una Campaign o un Canvas alcanza su límite de volumen. | Correo electrónico |
| Expiración de interacción de Canvas | Notifica a los destinatarios sobre cualquier Canvas cuya información de interacción esté próxima a expirar, junto con información sobre Segments, Campaigns o Canvas que lo referencien en un filtro de reorientación y que se hayan utilizado para enviar un mensaje en los últimos 30 días. | Correo electrónico |
| Comentarios en Canvas | Notifica a los destinatarios cuando un Canvas tiene nuevos comentarios. | Correo electrónico |
| Errores de contenido conectado | Notifica a los destinatarios cuando un punto de conexión de contenido conectado tiene errores. | Correo electrónico |
| Errores de push | Notifica a los destinatarios cuando un punto de conexión push tiene errores. | Correo electrónico, Webhook |
| Límite de Campaign planificada alcanzado | Notifica a los destinatarios cuando se ha alcanzado el límite de una Campaign planificada recurrente. | Correo electrónico, Webhook |
| Campaign planificada terminó de enviarse | Notifica a los destinatarios cuando una Campaign planificada ha terminado de enviarse. | Correo electrónico, Webhook |
| Errores de webhook | Notifica a los destinatarios cuando un punto de conexión de webhook tiene errores. | Correo electrónico |
| Informe de análisis semanal | Envía un resumen de la actividad del espacio de trabajo de la semana anterior a los destinatarios cada lunes. Los destinatarios reciben un resumen de cada espacio de trabajo al que pertenecen. | Correo electrónico |
| Límites de volumen de entrada diaria de Canvas/Campaign | Envía notificaciones cada vez que se alcanza un límite de envío. | Correo electrónico |
| Error de la Consola de Agente | Notifica a los destinatarios cuando un agente de la [Consola de Agente]({{site.baseurl}}/user_guide/brazeai/agents) ha alcanzado su límite de invocación, utiliza un modelo que ya no está disponible o encuentra un error de facturación con su proveedor de LLM (solo con clave de API propia). | Correo electrónico |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Notificaciones disponibles" }

{% alert note %}
Los [usuarios suspendidos]({{site.baseurl}}/user_guide/administer/global/user_management/manage_company_users#suspending-company-users) aún pueden recibir notificaciones de Braze.
{% endalert %}

## Informe de análisis semanal {#weekly-analytics-reporting}

Braze envía opcionalmente un informe semanal por correo electrónico a las personas que designes dentro de tu empresa cada lunes a las 5 am EST. Puedes seleccionar los eventos personalizados que se incluirán en el informe semanal desde **Configuración de datos** > **Eventos personalizados**.

Puedes seleccionar hasta cinco eventos para incluir en tu informe semanal:

![Selección de eventos para incluir en el informe de análisis]({% image_buster /assets/img_archive/company_analytics_report_new.png %})