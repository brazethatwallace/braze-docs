---
nav_title: Importación de cohortes Hightouch
article_title: Importación de cohortes Hightouch
description: "Este artículo de referencia describe la funcionalidad de importación de cohortes de Hightouch, una plataforma para sincronizar los datos de tus clientes desde tu almacén a las herramientas empresariales."
page_type: partner
search_tag: Partner

---
# Importación de cohortes Hightouch {#hightouch-cohort-import}

> Este artículo describe cómo importar cohortes de usuarios de [Hightouch](https://hightouch.io) a Braze para que puedas enviar campañas segmentadas basadas en datos que solo pueden existir en tu almacén. Para más información sobre la integración de Hightouch y sus otras funcionalidades, consulta el [artículo principal sobre Hightouch]({{site.baseurl}}/partners/data_and_analytics/reverse_etl/hightouch/hightouch).

## Integración de la importación de datos {#data-import-integration}

### Paso 1: Obtener la clave de importación de datos de Braze {#step-1-get-the-braze-data-import-key}
En Braze, ve a **Integraciones de socios** > **Socios tecnológicos** y selecciona **Hightouch**.

Aquí encontrarás tu endpoint REST y generarás tu clave de importación de datos de Braze. Una vez generada la clave, puedes crear una nueva o invalidar una existente.<br><br>![Página de partner tecnológico de Hightouch en Braze que muestra el endpoint REST y los controles de la clave de importación de datos.]({% image_buster /assets/img/hightouch/data_import_key.png %}){: style="max-width:90%;"}

### Paso 2: Añadir cohortes de Braze como destino en Hightouch {#step-2-add-braze-cohorts-as-a-destination-in-hightouch}
Ve a la página **Destination** en tu espacio de trabajo de Hightouch, busca **Braze Cohorts** y haz clic en **Continue**. Desde ahí, ingresa tu endpoint REST y tu clave de importación de datos y haz clic en **Continue**.<br><br>![Configuración de destino en Hightouch para Braze Cohorts con campos de credenciales.]({% image_buster /assets/img/hightouch/cohort1.png %}){: style="max-width:90%;"}

### Paso 3: Sincronizar un modelo (o audiencia) en Braze Cohorts {#step-3-sync-a-model-or-audience-into-braze-cohorts}
En Hightouch, usando tu [modelo](https://hightouch.io/docs/getting-started/create-your-first-sync/#create-a-model) o [audiencia](https://hightouch.io/docs/audiences/usage/) creados, crea una nueva sincronización. A continuación, selecciona el destino Braze Cohorts que creaste en el paso anterior. Por último, en la configuración de destino de Braze Cohorts, selecciona el identificador con el que deseas hacer la coincidencia y decide si quieres que Hightouch cree una nueva cohorte de Braze o actualice una existente.<br><br>![Configuración de sincronización de Braze Cohorts en Hightouch con opciones de identificador de coincidencia y cohorte.]({% image_buster /assets/img/hightouch/cohort2.png %}){: style="max-width:90%;"}

{% alert important %}
Solo se añadirán o eliminarán de una cohorte los usuarios que ya existan en Braze. La importación de cohortes no creará nuevos usuarios en Braze.
{% endalert %}

### Paso 4: Crear un segmento de Braze a partir de la audiencia personalizada de Hightouch {#step-4-create-a-braze-segment-from-the-hightouch-custom-audience}
En Braze, ve a **Segments**, crea un nuevo segmento y selecciona **Hightouch Cohorts** como filtro. Desde aquí, puedes elegir qué cohorte de Hightouch deseas incluir. Una vez creado tu segmento de cohorte de Hightouch, puedes seleccionarlo como filtro de audiencia al crear una Campaign o Canvas.<br><br>![Constructor de segmentos de Braze usando el filtro Hightouch Cohorts.]({% image_buster /assets/img/hightouch/cohort3.png %}){: style="max-width:90%;"}

### Uso de esta integración {#using-this-integration}
Para utilizar tu segmento de Hightouch, crea una Campaign o Canvas de Braze y selecciona el segmento como tu público objetivo.<br><br>![Paso de segmentación de audiencia en Braze con un segmento respaldado por Hightouch seleccionado.]({% image_buster /assets/img/hightouch/cohort4.png %}){: style="max-width:90%;"}

## Coincidencia de usuarios {#user-matching}

Los usuarios identificados pueden coincidir por su `external_id` o `alias`. Los usuarios anónimos pueden coincidir por su `device_id`. Los usuarios identificados que fueron creados originalmente como usuarios anónimos no pueden ser identificados por su `device_id`, y deben ser identificados por su `external_id` o `alias`.