---
nav_title: Zeotap para Currents
article_title: Zeotap para Currents
description: "Este artículo de referencia describe la asociación entre Braze Currents y Zeotap, una CDP de nueva generación que te ayuda a descubrir y comprender a tu audiencia móvil proporcionando resolución de identidades, información y enriquecimiento de datos."
page_type: partner
tool: Currents
search_tag: Partner
---

# Zeotap para Currents {#zeotap-for-currents}

> [Zeotap](https://zeotap.com/) es una CDP de nueva generación que te ayuda a descubrir y comprender a tu audiencia móvil proporcionando resolución de identidades, información y enriquecimiento de datos.

La integración de Braze y Zeotap te permite ampliar la escala y el alcance de tus campañas sincronizando los segmentos de clientes de Zeotap con los perfiles de usuario de Braze. Con [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/), también puedes conectar los datos a Zeotap para que sean procesables en todo el stack de crecimiento.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| --- | --- |
| Cuenta Zeotap | Se necesita una [cuenta Zeotap](https://zeotap.com/) para beneficiarse de esta asociación. |
| Currents | Para volver a exportar datos a Zeotap, tienes que tener configurado [Braze Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/) en tu cuenta. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Implementación {#implementation}

### Paso 1: Crear una fuente de Currents {#step-1-create-a-currents-source}

1. En Zeotap, ve a **Sources** en **Integrate**.
2. Selecciona **Create Source**.
3. Selecciona **Customer Engagement Channels** como categoría.<br><br>![Una ventana "Create Source" con diferentes categorías, entre ellas "Customer Engagement Channels".]({% image_buster /assets/img/zeotap/cec.png %}){: style="max-width:70%;"}<br><br>
4. Selecciona **Braze** como origen de datos.
5. Introduce un nombre de fuente.
6. Selecciona tu región.<br><br>![Ventana con opciones para seleccionar tu región y entidad de datos.]({% image_buster /assets/img/zeotap/select_region.png %}){: style="max-width:70%;"}<br><br>
7. Selecciona **Create Source**.
8. Ve a la pestaña **Implementation Details** y toma nota de la **API URL** y de la **Write Key**.<br><br>![Detalles de implementación de Braze Currents que contienen la API URL y la Write Key.]({% image_buster /assets/img/zeotap/implementation_details.png %})

### Paso 2: Configurar la transmisión de datos en Currents {#step-2-configure-data-streaming-in-currents}

1. En Braze, ve a **Partner Integrations** > **Data Export**.
2. Selecciona **Create New Current** y **Custom Currents Export**.<br><br>![El botón "Create New Current" con un desplegable que contiene "Custom Currents Export".]({% image_buster /assets/img/zeotap/custom_currents_export.png %}){: style="max-width:60%;"}<br><br>
3. Introduce un nombre de integración y un correo electrónico de contacto en caso de que se produzcan errores con la integración.
4. En **Credentials**, introduce la siguiente información que anotaste en el [Paso 1](#step-1-create-a-currents-source):
- La API URL como **Endpoint**
- La Write Key como **Bearer Token**<br><br>![Secciones para introducir los detalles de la integración y las credenciales.]({% image_buster /assets/img/zeotap/credentials.png %})<br><br>
5. Selecciona los eventos de interacción de mensajes que quieres enviar a Zeotap.<br><br>![La pestaña "General Settings" con una sección para seleccionar eventos de interacción de mensajes.]({% image_buster /assets/img/zeotap/message_engagement_events.png %})
6. Selecciona **Launch Current** para guardar los cambios y empezar a enviar eventos a Zeotap.

{% alert important %}
El conector de Currents no admite usuarios anónimos (usuarios sin `external_id`).
{% endalert %}