---
nav_title: Adobe para Currents
article_title: Adobe para Currents
alias: /partners/adobe_for_currents/
description: "Este artículo de referencia describe la asociación entre Braze Currents y Adobe, una CDP or plataforma de datos de los clientes or plataforma de datos de los clientes que permite a las marcas conectar y mapear sus datos de Adobe (atributos personalizados y segmentos) con Braze en tiempo real."
page_type: partner
tool: Currents
search_tag: Partner
---

# Adobe para Currents {#adobe-for-currents}

> [Adobe](https://www.adobe.com/) es una CDP or plataforma de datos de los clientes or plataforma de datos de los clientes que permite a las marcas conectar y mapear sus datos de Adobe (atributos personalizados y segmentos) con Braze en tiempo real.

La integración de Braze y Adobe te permite controlar fácilmente el flujo de información entre ambos sistemas. Con [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/), también puedes conectar los datos con Adobe para que sean procesables en todo el stack de crecimiento.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| ----------- | ----------- |
| Currents | Para volver a exportar datos a Adobe, debes tener configurado [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) para tu cuenta. |
| Cuenta de Adobe Experience Platform | Se necesita una [cuenta de Adobe Experience Platform](https://experience.adobe.com/#/platform/home) para aprovechar esta asociación. |
| Permiso para crear un conector | Necesitas permisos para crear una conexión de fuente de streaming para utilizar esta integración. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración {#integration}

### Paso 1: Crear un esquema XDM en Adobe {#step-1-create-an-xdm-schema-in-adobe}

1. En Adobe Experience Platform, ve a **Schemas** > selecciona **Create schema** > selecciona **Experience Event** > selecciona **Next**.<br><br>![Página de Adobe Schemas para el esquema llamado "Braze Currents Walk-Through".]({% image_buster /assets/img/adobe/currents_sources.png %})<br><br>
2. Proporciona un nombre y una descripción para tu esquema.
3. En el panel **Composition**, configura los atributos de tu esquema:
- En **Field groups**, selecciona **Add** y, a continuación, añade el grupo de campos **Braze Currents User Event**.
- Selecciona **Save**.

Para más información sobre los esquemas, consulta la documentación de Adobe sobre la [creación de esquemas](https://experienceleague.adobe.com/en/docs/experience-platform/xdm/tutorials/create-schema-ui).

### Paso 2: Conectar Braze a Adobe Experience Platform {#step-2-connect-braze-to-the-adobe-experience-platform}

1. En Adobe Experience Platform, ve a **Sources** > **Catalog** > **Marketing automation**.
2. Selecciona **Add data** para Braze Currents.
3. Sube el [archivo de muestra de Braze Currents](https://github.com/Appboy/currents-examples/blob/master/sample-data/Adobe/adobe_examples.json).<br><br>![Página "Add data" de Adobe.]({% image_buster /assets/img/adobe/currents_add_data.png %})<br><br>
4. Una vez cargado el archivo, proporciona los detalles de tu flujo de datos, incluida la información sobre tu conjunto de datos y el esquema al que lo estás mapeando.
    - Si es la primera vez que conectas una fuente de Braze Currents, crea un nuevo conjunto de datos y asegúrate de utilizar el esquema que creaste en el [Paso 1](#step-1-create-an-xdm-schema-in-adobe).
    - Si no es tu primera vez, utiliza cualquier conjunto de datos existente que haga referencia al esquema de Braze.
5. Configura el mapeado de tus datos y resuelve los problemas.
    - Cambia el mapeado de `id` de `to _braze.appID` a `_id` en el nivel raíz del esquema.
    - Asegúrate de que `properties.is_amp` está mapeado a `_braze.messaging.email.isAMP`.
    - Elimina el mapeado de `time` y `timestamp`, luego selecciona el icono de añadir > **Add calculated field** e introduce **time * 1000**. Selecciona **Save**.
    - Selecciona **Map target field** junto al nuevo campo de origen y mapéalo a **timestamp** en el nivel raíz del esquema. <br><br>![Página "Add data" de Adobe con mapeados.]({% image_buster /assets/img/adobe/currents_mapping.png %})<br><br>
6. Selecciona **Validate** para confirmar que has resuelto los problemas.

{% alert important %}
Las marcas de tiempo de Braze se expresan en segundos. Para reflejar con precisión las marcas de tiempo en Adobe Experience Platform, tus campos calculados deben estar en milisegundos. Para convertir segundos en milisegundos, utiliza el cálculo **time * 1000**.
{% endalert %}

{: start="7"}
7. Selecciona **Next**, revisa los detalles de tu flujo de datos y, a continuación, selecciona **Finish**.<br><br>![Página "Add data" de Adobe sin errores de mapeado.]({% image_buster /assets/img/adobe/currents_no_errors.png %})

### Paso 3: Reunir credenciales {#step-3-gather-credentials}

Recoge las siguientes credenciales para introducirlas en Braze, lo que permitirá a Braze enviar datos a Adobe Experience Platform.

| Campo         | Descripción                          |
|---------------|-------------------------------------|
| Client ID     | El ID de cliente asociado a tu fuente de Adobe Experience Platform. |
| Client Secret | El secreto de cliente asociado a tu fuente de Adobe Experience Platform. |
| Tenant ID     | El ID de tenant asociado a tu fuente de Adobe Experience Platform. |
| Sandbox Name  | El sandbox asociado a tu fuente de Adobe Experience Platform.   |
| Dataflow ID   | El ID de flujo de datos asociado a tu fuente de Adobe Experience Platform.   |
| Streaming Endpoint  | El punto de conexión de streaming asociado a tu fuente de Adobe Experience Platform. Braze lo convierte automáticamente en el punto de conexión de streaming por lotes. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Paso 3: Reunir credenciales" }

### Paso 4: Configurar Currents para transmitir datos a tu origen de datos {#step-4-configure-currents-to-stream-data-to-your-data-source}

1. En Braze, ve a **Partner Integrations** > **Data Export** y, a continuación, selecciona **Create New Current**.
2. Proporciona lo siguiente:
    - Un nombre para el conector
    - Información de contacto para notificaciones sobre el conector
    - Las credenciales del [Paso 3](#step-3-gather-credentials)
3. Selecciona los eventos que quieres recibir.
4. Configura opcionalmente las exclusiones de campos o transformaciones que desees.
5. Selecciona **Launch Current**.