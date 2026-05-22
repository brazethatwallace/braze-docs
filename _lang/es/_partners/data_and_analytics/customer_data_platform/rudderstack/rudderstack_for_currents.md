---
nav_title: RudderStack para Currents
article_title: RudderStack para Currents
description: "Este artículo describe la asociación entre Braze Currents y RudderStack, una infraestructura de datos de clientes de código abierto que ofrece una integración perfecta de Braze para tus aplicaciones Android, iOS y web."
page_type: partner
tool: Currents
search_tag: Partner

---

# RudderStack para Currents {#rudderstack-for-currents}

> [RudderStack](https://www.rudderstack.com/) te permite recopilar, transformar y activar los datos de clientes en toda tu pila, aprovechando tu almacén de datos en la nube como fuente central de la verdad. Este artículo ofrece un resumen de cómo establecer una conexión entre Braze Currents y RudderStack.

La integración de Braze y RudderStack te permite aprovechar Braze Currents para exportar tus eventos de Braze a RudderStack para impulsar análisis más profundos.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| --- | --- |
| Cuenta de RudderStack | Se requiere una [cuenta de RudderStack](https://app.rudderstack.com/login) para beneficiarse de esta asociación. |
| Destino Braze | Te sugerimos que hayas configurado [Braze como destino]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/rudderstack/rudderstack/#integration) en RudderStack. |
| Currents | Para volver a exportar datos a RudderStack, necesitas tener configurado [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) para tu cuenta. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración {#integration}

### Paso 1: Crear un origen de datos para Braze dentro de RudderStack {#step-1-create-a-data-source-for-braze-within-rudderstack}

En primer lugar, debes crear una fuente de Braze en la aplicación web de RudderStack. Puedes encontrar instrucciones para crear un origen de datos en el sitio web de [RudderStack](https://www.rudderstack.com/docs/sources/event-streams/cloud-apps/braze-currents/).

Una vez completado, RudderStack proporcionará una URL de webhook, incluida la clave de escritura, que deberás utilizar en el siguiente paso. Puedes encontrar la URL del webhook en la pestaña **Settings** de tu fuente de Braze.

### Paso 2: Crear Current {#step-2-create-current}

En Braze, ve a **Currents > + Create Current > RudderStack Export**. Proporciona el nombre de la integración, el correo electrónico de contacto, la URL del webhook de RudderStack (que va en el campo clave) y la región de RudderStack.

### Paso 3: Exportar eventos {#step-3-export-events}

A continuación, selecciona los eventos que deseas exportar. Por último, haz clic en **Launch Current**.

Todos los eventos enviados a RudderStack incluirán el `external_user_id` del usuario. En este momento, Braze no envía datos de eventos a RudderStack para los usuarios que no tienen configurado su `external_user_id`.

## Detalles de la integración {#integration-details}

Braze admite la exportación a RudderStack de todos los datos incluidos en los [glosarios de eventos de Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/).

La estructura de la carga útil para los datos exportados es la misma que la de los conectores HTTP personalizados, que puedes consultar en el [repositorio de ejemplos de conectores HTTP personalizados](https://github.com/Appboy/currents-examples/tree/master/sample-data/Custom%20HTTP/users/behaviors).