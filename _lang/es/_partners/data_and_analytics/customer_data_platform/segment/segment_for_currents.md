---
nav_title: Segment para Currents
article_title: Segment para Currents
page_order: 2
alias: /partners/segment_for_currents/
description: "Este artículo de referencia describe la asociación entre Braze Currents y Segment, una plataforma de datos de clientes que recopila y encamina información entre fuentes de tu pila de marketing."
page_type: partner
tool: Currents
search_tag: Partner

---

# Segment para Currents {#segment-for-currents}

> [Segment](https://segment.com) es una plataforma de datos de clientes que te ayuda a recopilar, limpiar y activar los datos de tus clientes. Este artículo de referencia ofrece un resumen de la conexión entre Braze Currents y Segment, y describe los requisitos y procesos para una implementación y uso adecuados.

La integración de Braze y Segment te permite aprovechar Braze Currents para exportar tus eventos de Braze a Segment y obtener análisis más profundos de las conversiones, la retención y el uso del producto.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta de Segment | Se necesita una [cuenta de Segment](https://app.segment.com/login) para beneficiarse de esta asociación. |
| Destino Braze | Ya debes haber [configurado Braze como destino]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment/#connection-settings/) en tu integración de Segment.<br><br>Esto incluye proporcionar el centro de datos de Braze y la clave de API REST or transferencia de estado representacional correctos en tu [configuración de conexión]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment#connection-settings). |
| Currents | Para volver a exportar datos a Segment, debes tener configurado [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents#access-currents) en tu cuenta. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración {#integration}

### Paso 1: Obtener la clave de escritura de Segment {#step-1-obtain-segment-write-key}

En tu dashboard de Segment, selecciona tu fuente de Segment. A continuación, ve a **Settings > API keys**. Aquí encontrarás la **Segment Write Key**.

{% alert warning %}
Es importante mantener actualizada tu clave de escritura de Segment. Si las credenciales de tu conector caducan, el conector dejará de enviar eventos. Si esto persiste durante más de **5 días**, los eventos del conector se eliminarán y los datos se perderán permanentemente.
{% endalert %}

### Paso 2: Crear un nuevo conector de Currents {#step-2-create-a-new-currents-connector}

1. En Braze, ve a **Integraciones de socios** > **Exportación de datos**.
2. Haz clic en **+ Create New Current** > **Segment Data Export**.
3. A continuación, proporciona el nombre de la integración, el correo electrónico de contacto, la clave de escritura de Segment y la región de Segment.

![La página de Segment Currents en Braze. Aquí puedes encontrar campos para el nombre de la integración, el correo electrónico de contacto, la región de Segment y la clave de API.]({% image_buster /assets/img/segment/segment_currents_integration_config.png %})

### Paso 3: Exportar eventos de interacción con mensajes {#step-3-export-message-engagement-events}

A continuación, selecciona los eventos de interacción con mensajes que deseas exportar. Consulta la siguiente tabla de eventos y propiedades de exportación. Todos los eventos enviados a Segment incluirán el `external_user_id` del usuario como `userId` y el `braze_id` del usuario como `anonymousId`.

Ten en cuenta que Braze solo envía datos de eventos de usuarios sin `external_user_id` si está marcada la opción **Include events from anonymous users**.

{% multi_lang_include alerts/early_access_beta_alert.md feature='Anonymous user export' %}

![Lista de todos los eventos de interacción con mensajes disponibles en la página de Segment Currents en Braze.]({% image_buster /assets/img/segment/segment_currents_data_config.png %})

Por último, selecciona **Launch Current**.

{% multi_lang_include alerts/warning_alerts.md alert='Segment Currents multiple connectors' %}

Para saber más, visita la [documentación](https://segment.com/docs/connections/sources/catalog/cloud-apps/braze/) de Segment.

## Actualizar tu Current {#updating-your-current}

{% multi_lang_include currents/updating_currents.md %}

## Eventos de Currents compatibles {#supported-currents-events}

Braze admite la exportación de los siguientes eventos a Segment:

- [Eventos de interacción con mensajes]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events)
- [Eventos de comportamiento del cliente]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events)

Para consultar la estructura de la carga útil de cada evento, selecciona la pestaña **Segment** en el [glosario de eventos de interacción con mensajes]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) y en el [glosario de eventos de comportamiento del cliente]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events).