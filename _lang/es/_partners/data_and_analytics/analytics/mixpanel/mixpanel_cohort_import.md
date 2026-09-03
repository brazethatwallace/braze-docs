---
nav_title: Mixpanel
article_title: Importación de cohortes de Mixpanel
description: "Este artículo de referencia describe la funcionalidad de importación de cohortes de Mixpanel, una plataforma de análisis empresarial, que permite importar cohortes de Mixpanel a Braze para crear segmentos de Braze que se pueden utilizar para dirigirse a usuarios en futuras Campaigns o Canvas de Braze."
page_type: partner
search_tag: Partner
---

# Importación de cohortes de Mixpanel {#mixpanel-cohort-import}

> Este artículo describe cómo importar cohortes de usuarios de [Mixpanel](https://mixpanel.com/) a Braze. Para obtener más información sobre la integración de Mixpanel y sus otras funcionalidades, consulta el [artículo principal sobre Mixpanel]({{site.baseurl}}/partners/data_and_analytics/analytics/mixpanel).

## Integración de importación de datos {#data-import-integration}

Cuando sincronizas una cohorte de Mixpanel a Braze, Braze recibe actualizaciones de pertenencia a la cohorte para los usuarios que Mixpanel puede asociar con perfiles de Braze existentes. Después de una sincronización, puedes dirigirte a esos usuarios con el filtro de segmento **Mixpanel cohorts**.

La sincronización de cohortes no importa eventos de Mixpanel, propiedades de usuario de Mixpanel ni atributos personalizados a Braze. El comportamiento del conector, incluida la cadencia de sincronización, se controla en Mixpanel. Para obtener detalles de configuración, consulta la [documentación de sincronización de cohortes de Braze de Mixpanel](https://docs.mixpanel.com/docs/cohort-sync/integrations/braze). Para los requisitos de coincidencia de usuarios, consulta [Coincidencia de usuarios](#user-matching).

Cualquier integración que configures registrará puntos de datos. Si tienes alguna pregunta sobre los matices de los puntos de datos de Braze, tu director de cuentas de Braze puede responderte.

{% alert important %}
En cumplimiento de las políticas de retención de datos de Mixpanel, los eventos enviados antes del 1 de enero de 2010 se eliminarán durante la importación.
{% endalert %}

### Paso 1: Obtener la clave de importación de datos de Braze {#step-1-get-the-braze-data-import-key}

En Braze, ve a **Integraciones de socios** > **Socios tecnológicos** y selecciona **Mixpanel**. Aquí encontrarás el endpoint REST y generarás tu clave de importación de datos de Braze.

Una vez generada, puedes crear una nueva clave o invalidar una existente. La clave de importación de datos y el endpoint REST se utilizan en el siguiente paso al configurar un postback en el panel de Mixpanel.<br><br>![Página de partner tecnológico de Braze para Mixpanel que muestra la clave de importación de datos y el endpoint.]({% image_buster /assets/img_archive/currents-mixpanel-edit.png %})

### Paso 2: Configurar la integración de Braze en Mixpanel {#step-2-set-up-the-braze-integration-in-mixpanel}

1. En Mixpanel, ve a **Data Management > Integrations.**
2. Selecciona la pestaña de integración de Braze y selecciona **Connect**.
3. En el mensaje que aparece, introduce la clave de importación de datos de Braze y el endpoint REST.
4. Selecciona **Continue**.

![Modal de configuración de la integración de Braze en Mixpanel con campos para la clave y el endpoint.]({% image_buster /assets/img_archive/mixpanel2.png %}){: style="max-width:50%;"}

### Paso 3: Exportar una cohorte de Mixpanel a Braze {#step-3-export-a-mixpanel-cohort-to-braze}

En Mixpanel, ve a **Data Management > Cohorts**. Selecciona la cohorte que deseas enviar a Braze y luego selecciona **Export to Braze**. Por último, selecciona una sincronización única o una sincronización dinámica. Seleccionar la sincronización dinámica mantiene la cohorte actualizada en una programación recurrente controlada por Mixpanel. Para conocer la cadencia de sincronización más reciente, consulta la [documentación de sincronización de cohortes de Braze de Mixpanel](https://docs.mixpanel.com/docs/cohort-sync/integrations/braze).

![Flujo de exportación de cohortes de Mixpanel que muestra las opciones de sincronización con Export to Braze.]({% image_buster /assets/img_archive/mixpanel3.png %}){: style="max-width:50%;"}

{% alert important %}
Solo se añadirán o eliminarán de una cohorte los usuarios que ya existan en Braze. La importación de cohortes no creará nuevos usuarios en Braze.
{% endalert %}

### Paso 4: Segmentar usuarios en Braze {#step-4-segment-users-in-braze}

En Braze, para crear un segmento de estos usuarios, ve a **Audiencia** > **Segmentos**, asigna un nombre a tu segmento y selecciona **Mixpanel_Cohorts** como filtro. A continuación, utiliza la opción "includes" y elige la cohorte que creaste en Mixpanel.

![En el creador de segmentos de Braze, el filtro de atributos de usuario "Mixpanel cohorts" se establece en "includes" y "Braze cohort".]({% image_buster /assets/img_archive/mixpanel1.png %})

Después de guardarlo, puedes hacer referencia a este segmento durante la creación de Canvas o Campaigns en el paso de segmentación de usuarios.

## Coincidencia de usuarios {#user-matching}

Los usuarios identificados pueden coincidir por su `external_id` o `alias`. Los usuarios anónimos pueden coincidir por su `device_id`. Los usuarios identificados que fueron creados originalmente como usuarios anónimos no pueden ser identificados por su `device_id`, y deben ser identificados por su `external_id` o `alias`.

## Solución de problemas {#troubleshooting}

Si una sincronización de cohortes de Mixpanel parece incompleta o no se actualiza para ciertos usuarios, consulta [Solución de problemas]({{site.baseurl}}/partners/data_and_analytics/analytics/mixpanel#troubleshooting) en el artículo principal de Mixpanel.

Para pasos específicos del conector y la cadencia de sincronización, consulta la [documentación de sincronización de cohortes de Braze de Mixpanel](https://docs.mixpanel.com/docs/cohort-sync/integrations/braze).