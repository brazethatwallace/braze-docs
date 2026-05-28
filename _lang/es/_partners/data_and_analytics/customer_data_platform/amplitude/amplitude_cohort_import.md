---
nav_title: Amplitude
article_title: Importación de cohortes de Amplitude
description: "Este artículo de referencia describe la funcionalidad de importación de cohortes de Amplitude, una plataforma de análisis de productos e inteligencia empresarial."
page_type: partner
search_tag: Partner
---

# Importación de cohortes de Amplitude {#amplitude-cohort-import}

> Este artículo explica cómo importar cohortes de usuarios de [Amplitude](https://amplitude.com/) a Braze. Para más información sobre la integración de Amplitude y sus otras funcionalidades, consulta el [artículo principal de Amplitude]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_audiences/).

## Integración de importación de datos {#data-import-integration}

Cualquier integración que configures contará para el volumen de puntos de datos de tu cuenta.

### Paso 1: Obtener la clave de importación de datos de Braze {#step-1-get-the-braze-data-import-key}

En Braze, ve a **Partner Integrations** > **Technology Partners** y selecciona **Amplitude**. Aquí encontrarás el punto de conexión REST y generarás tu clave de importación de datos de Braze.

Una vez generada, puedes crear una nueva clave o invalidar una existente. La clave de importación de datos y el punto de conexión REST se utilizan en el siguiente paso al configurar un postback en el dashboard de Amplitude.<br><br>![]({% image_buster /assets/img/amplitude3.png %})

### Paso 2: Configurar la integración de Braze en Amplitude {#step-2-set-up-the-braze-integration-in-amplitude}

En Amplitude, ve a **Sources & Destinations** > **[nombre del proyecto]** > **Destinations** > **Braze**. En el mensaje que aparece, proporciona la clave de importación de datos de Braze y el punto de conexión REST, y haz clic en **Save**.

![]({% image_buster /assets/img/amplitude.png %})

### Paso 3: Exportar una cohorte de Amplitude a Braze {#step-3-export-an-amplitude-cohort-to-braze}

En primer lugar, para exportar usuarios de Amplitude a Braze, crea una [cohorte](https://help.amplitude.com/hc/en-us/articles/231881448-Behavioral-Cohorts) de usuarios que desees exportar. Luego, para capturar usuarios identificados y anónimos, configura dos sincronizaciones para esa cohorte con estas propiedades de mapeado de identificadores:
- ID de usuario (ID externo)
- ID del dispositivo

Puedes configurar múltiples conexiones de Braze en tu cuenta de Amplitude. Esto te permite configurar una conexión para sincronizar ID de usuario para usuarios conocidos y otra para sincronizar ID de dispositivo para usuarios anónimos.

Una vez que hayas creado una cohorte, haz clic en **Sync to...** para exportar estos usuarios a Braze.

{% alert important %}
Solo se añadirán o eliminarán de una cohorte los usuarios que ya existan en Braze. La importación de cohortes no creará nuevos usuarios en Braze.
{% endalert %}

#### Definir la cadencia de sincronización {#defining-sync-cadence}

Las sincronizaciones de cohortes pueden configurarse para que se realicen una sola vez, programarse como diarias o cada hora, o incluso en tiempo real, actualizándose cada minuto.

Cualquier integración que configures registrará puntos de datos. Si tienes alguna pregunta sobre los matices de los puntos de datos de Braze, tu director de cuentas de Braze puede responderte.

### Paso 4: Segmentar usuarios en Braze {#step-4-segment-users-in-braze}

En Braze, para crear un segmento de estos usuarios, ve a **Segments** en **Engagement**, asigna un nombre a tu segmento y selecciona **Amplitude Cohorts** como filtro. A continuación, utiliza la opción "includes" y elige la cohorte que creaste en Amplitude.

![En el constructor de segmentos de Braze, el filtro "amplitude_cohorts" está configurado en "includes_value" y "Amplitude cohort test".]({% image_buster /assets/img/amplitude2.png %})

Después de guardarlo, puedes hacer referencia a este segmento durante la creación de un Canvas o una Campaign en el paso de segmentación de usuarios.

## Coincidencia de usuarios {#user-matching}

Los usuarios identificados pueden coincidir por su `external_id` o `alias`. Los usuarios anónimos pueden coincidir por su `device_id`. Los usuarios identificados que fueron creados originalmente como usuarios anónimos no pueden ser identificados por su `device_id`, y deben ser identificados por su `external_id` o `alias`.