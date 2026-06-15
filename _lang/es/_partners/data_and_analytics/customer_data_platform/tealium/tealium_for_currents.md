---
nav_title: Tealium para Currents
article_title: Tealium para Currents
page_order: 3
alias: /partners/tealium_for_currents/
description: "Este artículo de referencia describe la asociación entre Braze Currents y Tealium, una plataforma de datos de los clientes que recopila y encamina información entre fuentes de tu stack de marketing."
page_type: partner
tool: Currents
search_tag: Partner

---

# Tealium para Currents {#tealium-for-currents}

> [Tealium](https://www.tealium.com) es una plataforma de datos de los clientes que recopila y encamina información de múltiples fuentes a una variedad de otras ubicaciones en tu stack de marketing.

La integración de Braze y Tealium te permite controlar fácilmente el flujo de información entre los dos sistemas. Con Currents, también puedes conectar los datos a Tealium para que sean procesables en todo el stack de crecimiento.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| ----------- | ----------- |
| Tealium EventStream o Tealium AudienceStream | Se necesita una [cuenta de Tealium](https://my.tealiumiq.com/) para beneficiarse de esta asociación. |
| Currents | Para poder exportar datos a Tealium, debes tener configurado [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) en tu cuenta. |
| URL de Tealium | Puedes obtenerla navegando a tu dashboard de Tealium y copiando la URL de ingesta.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración {#integration}

### Paso 1: Crear un origen de datos para Braze en Tealium {#step-1-create-a-data-source-for-braze-within-tealium}

Las instrucciones para crear un origen de datos se encuentran en el sitio de [Tealium](https://docs.tealium.com/server-side/data-sources/webhooks/braze-currents/). Una vez completado, Tealium te proporcionará una URL de origen de datos para copiar, que utilizarás en el siguiente paso.

### Paso 2: Crear un Current {#step-2-create-current}

En Braze, ve a **Currents** > **+ Create Current** > **Tealium Export**. Proporciona un nombre de integración, un correo electrónico de contacto y tu URL de Tealium.

A continuación, selecciona lo que deseas rastrear de la lista de eventos disponibles. De forma predeterminada, todos los eventos enviados a Tealium incluyen el `external_user_id` del usuario. Sin embargo, puedes seleccionar la casilla **Include events from anonymous users** para enviar también a Tealium los eventos que no tengan un `external_user_id`.

Después de configurar tu integración, selecciona **Launch Current**.

{% alert important %}
Es importante mantener actualizada tu URL de Tealium. Si la URL de tu conector es incorrecta, Braze no podrá enviar eventos. Si esto persiste durante más de **5 días**, los eventos del conector se eliminarán y los datos se perderán permanentemente.
{% endalert %}

## Detalles de la integración {#integration-details}

Braze admite la exportación a Tealium de todos los datos enumerados en los [glosarios de eventos de Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/) (incluidas todas las propiedades tanto de los eventos de [interacción con mensajes]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/) como de [comportamiento del cliente]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/)).

La estructura de la carga útil de los datos exportados es la misma que la de los conectores HTTP personalizados, que puede consultarse en el [repositorio de ejemplos de conectores HTTP personalizados](https://github.com/Appboy/currents-examples/tree/master/sample-data/Custom%20HTTP/users/behaviors).