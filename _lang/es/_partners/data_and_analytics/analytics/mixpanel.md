---
nav_title: Mixpanel
article_title: Mixpanel
alias: /partners/mixpanel/
description: "Este artículo de referencia describe la asociación entre Braze y Mixpanel, una plataforma de análisis empresarial, que te permite importar cohortes de Mixpanel a Braze para crear segmentos de Braze que pueden utilizarse para dirigirse a usuarios en futuras Campaigns o Canvas de Braze."
page_type: partner
search_tag: Partner
tool: Currents
---

# [![Curso de Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/mixpanel-integration-with-braze/339085/scorm/2u7y2e6qrldh2){: style="float:right;width:120px;border:0;" class="noimgborder"}Mixpanel {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecommixpanel-integration-with-braze339085scorm2u7y2e6qrldh2-stylefloatrightwidth120pxborder0-classnoimgbordermixpanel}

> [Mixpanel](https://mixpanel.com/) es una plataforma de análisis empresarial que te permite exportar eventos de Mixpanel a otras plataformas para realizar análisis más profundos. Los datos recopilados pueden utilizarse para elaborar informes personalizados y medir la participación y la retención de los usuarios.

La integración de Braze y Mixpanel te permite [importar cohortes de Mixpanel a Braze]({{site.baseurl}}/partners/data_and_analytics/analytics/mixpanel/mixpanel_cohort_import) para crear segmentos de Braze que pueden dirigirse a usuarios en futuras Campaigns o Canvas de Braze. La sincronización de cohortes actualiza la pertenencia a la cohorte en Braze y no importa eventos ni propiedades de usuario de Mixpanel. Para más detalles, consulta [Importación de cohortes de Mixpanel]({{site.baseurl}}/partners/data_and_analytics/analytics/mixpanel/mixpanel_cohort_import#data-import-integration).

También puedes aprovechar Braze Currents para [exportar tus eventos de Braze a Mixpanel](#data-export-integration) y obtener análisis más profundos de las conversiones, la retención y el uso del producto.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
|---|---|
| Cuenta de Mixpanel | Se requiere una [cuenta de Mixpanel](https://mixpanel.com/) para aprovechar esta integración. |
| Currents | Para exportar datos de vuelta a Mixpanel, necesitas tener [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents#access-currents) configurado en tu cuenta. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración de exportación de datos {#data-export-integration}

En esta sección puedes encontrar una lista completa de los eventos que se pueden exportar de Braze a Mixpanel. Todos los eventos enviados a Mixpanel incluirán el `external_user_id` del usuario como el Distinct ID de Mixpanel. Actualmente, Braze no envía datos de eventos para los usuarios que no tienen configurado su `external_user_id`.

Puedes exportar dos tipos de eventos a Mixpanel: [Eventos de participación en mensajes](#supported-currents-events), que consisten en los eventos de Braze directamente relacionados con el envío de mensajes, y [Eventos de comportamiento del cliente](#supported-currents-events), que incluyen otra actividad de la aplicación o el sitio web, como sesiones, eventos personalizados y compras rastreadas a través de la plataforma. Todos los eventos personalizados tienen el prefijo `[Braze Custom Event]`. Las propiedades de eventos personalizados y las propiedades de eventos de compra tienen los prefijos `[Custom event property]` y `[Purchase property]`, respectivamente.

Ponte en contacto con tu director de cuentas o abre un [ticket de soporte]({{site.baseurl}}/user_guide/administer/personal/braze_support) si necesitas acceso a derechos de eventos adicionales.

### Paso 1: Obtener las credenciales de Mixpanel {#step-1-get-mixpanel-credentials}

En tu panel de Mixpanel, haz clic en **Project Settings** en un proyecto nuevo o existente. Ahí encontrarás el secreto de API de Mixpanel y el token de Mixpanel. Estas credenciales se utilizarán en el siguiente paso para crear tu conexión de Currents.

### Paso 2: Crear un Braze Current {#step-2-create-braze-current}

1. En Braze, ve a **Currents** > **+ Create Current** > **Create Mixpanel Export**.
2. Proporciona un nombre de integración, un correo electrónico de contacto, el secreto de API de Mixpanel y el token de Mixpanel en los campos indicados.
3. Selecciona los eventos que deseas rastrear; se proporciona una lista de eventos disponibles.
4. Selecciona **Launch Current**.

![La página de Braze Mixpanel Currents. Esta página incluye campos para el nombre de integración, correo electrónico de contacto, secreto de API y token de exportación de Mixpanel. La mitad inferior de la página de Currents muestra los eventos de Currents disponibles que puedes enviar.]({% image_buster /assets/img_archive/mixpanel4.png %}){: style="max-width:80%;"}

{% tab note %}
Consulta la [documentación de integración](https://help.mixpanel.com/hc/en-us/articles/360001243663) de Mixpanel para obtener más información.
{% endtab %}

## Eventos de Currents compatibles {#supported-currents-events}

Braze permite exportar los siguientes eventos a Mixpanel:

- [Eventos de interacción con mensajes]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events)
- [Eventos de comportamiento del cliente]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events)

Para consultar la estructura de la carga útil de cada evento, selecciona la pestaña **Mixpanel** en el [glosario de eventos de interacción con mensajes]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) y en el [glosario de eventos de comportamiento del cliente]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events).

## Solución de problemas {#troubleshooting}

### Verificar la clave de API de Mixpanel y el ID externo de Braze {#verify-mixpanel-api-key-and-braze-external-id}

Confirma que tu clave de API de Mixpanel y los valores de `braze_external_id` coincidan con lo que esperas en Braze y Mixpanel. La API de sincronización de cohortes comparte grupos de usuarios entre productos, y la sincronización no funcionará correctamente si el `external_id` en Braze y el identificador que envía Mixpanel no coinciden. Las sincronizaciones de cohortes desde Mixpanel se ejecutan según el calendario de Mixpanel, por ejemplo, una vez o aproximadamente cada dos horas, así que deja tiempo entre cada verificación.

### Verificar el estado de la implementación {#check-implementation-status}

Confirma que `braze_external_id` esté implementado en Mixpanel.

### Establecer la propiedad de usuario directamente {#set-the-user-property-directly}

Para reducir la ambigüedad, establece `braze_external_id` directamente en Mixpanel.

### Configuración automática de la propiedad (SDKs) {#automatic-property-setting-sdks}

El SDK or kit de desarrollo de software de Mixpanel puede establecer `braze_external_id` automáticamente cuando el SDK or kit de desarrollo de software de Braze está integrado en la misma aplicación. Si implementas Mixpanel y Braze juntos, normalmente no necesitas configuración adicional más allá de instalar ambos SDKs.

{% alert note %}
`braze_external_id` no se establece cuando se llama a `changeUser()` en Braze; se establece cuando Mixpanel se inicializa o inicia una sesión (durante el "init" o "start session").
{% endalert %}