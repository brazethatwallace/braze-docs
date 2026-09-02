---
nav_title: Kubit
article_title: Importación de cohortes de Kubit
description: "Este artículo de referencia describe la funcionalidad de importación de cohortes de Kubit, una plataforma de análisis de autoservicio sin código que ofrece información instantánea sobre los productos, lo que te permite importar cohortes de usuarios de Kubit y dirigirlas a la mensajería de Braze."
page_type: partner
search_tag: Partner
---

# Importación de cohortes de Kubit {#kubit-cohort-import}

> Este artículo describe cómo importar cohortes de usuarios de [Kubit](https://kubit.ai/) a Braze. Para más información sobre la integración de Kubit y sus otras funcionalidades, consulta el [artículo principal sobre Kubit]({{site.baseurl}}/partners/data_and_analytics/analytics/kubit).

## Integración de la importación de datos {#data-import-integration}

### Paso 1: Obtener la clave de importación de datos de Braze {#step-1-get-the-braze-data-import-key}

En Braze, ve a **Integraciones de socios** > **Socios tecnológicos** y selecciona **Kubit**. Aquí encontrarás el endpoint REST y generarás tu clave de importación de datos de Braze.

Una vez generada, puedes crear una nueva clave o invalidar una existente. La clave de importación de datos y el endpoint REST se utilizan en el siguiente paso cuando se configura un postback en el panel de Kubit.

![La página de partners tecnológicos de Kubit en Braze.]({% image_buster /assets/img/kubit/kubit.png %}){: style="max-width:90%;"}

### Paso 2: Configurar Braze en Kubit {#step-2-configure-braze-in-kubit}

Proporciona la clave de importación de datos de Braze y el endpoint REST de Braze a tu contacto de soporte de Kubit. Ellos configurarán la integración por su parte y te avisarán cuando la integración esté en vivo.

### Paso 3: Importar cohortes a Braze {#step-3-import-cohorts-to-braze}

#### Crear una cohorte en Kubit {#create-a-cohort-in-kubit}
[Crea una cohorte](https://www.kubit.ai/doc/fundamentals#cohort) en Kubit y define los criterios de tus usuarios objetivo.<br><br>![Constructor de cohortes de Kubit con criterios de usuarios objetivo configurados.]({% image_buster /assets/img/kubit/create_cohort.png %}){: style="max-width:80%;"}

#### Importar usuarios a Braze {#import-users-to-braze}
Una vez que hayas guardado tu cohorte, puedes importarla a Braze para utilizarla en segmentos de Braze. Estos segmentos pueden utilizarse para crear campañas de correo electrónico o push específicas y Canvas.

Para ello, ve a tu cohorte existente y, en **Cohort Control**, selecciona **Import to Braze**.

![Menú de control de cohortes de Kubit con la opción Import to Braze seleccionada.]({% image_buster /assets/img/kubit/import_to_braze.png %}){: style="max-width:80%;"}

A continuación, selecciona la cadencia de importación deseada. Las importaciones únicas te permiten importar una sola vez de forma inmediata. Las importaciones programadas te permiten importar diaria, semanal o mensualmente a una hora determinada. Ten en cuenta que cada cohorte solo puede tener un programa de importación en vivo.

![Configuración de programación de importación de Kubit con opciones de cadencia para importaciones a Braze.]({% image_buster /assets/img/kubit/import_schedule.png %}){: style="max-width:40%;"}

{% alert important %}
Solo se añadirán o eliminarán de una cohorte los usuarios que ya existan en Braze. La importación de cohortes no creará nuevos usuarios en Braze.
{% endalert %}

#### Verificar el estado de la importación {#verify-import-status}
Una vez finalizada la importación, se enviará una notificación por correo electrónico a los destinatarios especificados en el programa de importación. También puedes comprobar el estado de importación de una cohorte en **Schedule** en Kubit. El historial de programación mostrará la hora de ejecución de cada importación, el resultado y el número total de usuarios de la cohorte que se importaron a Braze.<br><br>![Historial de programación de Kubit que muestra los tiempos de ejecución de importación, los resultados y los recuentos de usuarios importados.]({% image_buster /assets/img/kubit/import_history.png %})<br><br>Puedes activar manualmente una importación haciendo clic en el icono **Import to Braze** para ese programa de importación.

### Paso 4: Crear segmentos de Braze con cohortes de Kubit {#step-4-create-braze-segments-with-kubit-cohorts}
Después de importar cohortes a Braze, puedes utilizarlas como filtros para crear segmentos de Braze e incluirlos en campañas de Braze o Canvas. Visita nuestra documentación de segmentos para obtener más información sobre [cómo crear segmentos de Braze]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment#step-4-add-filters-to-your-segment).

![En el constructor de segmentos de Braze, el atributo de usuario "Kubit cohorts" está configurado en "includes_value" y muestra una lista de las cohortes disponibles.]({% image_buster /assets/img/kubit/segment_with_kubit_cohorts.png %}){: style="max-width:70%;"}

## Coincidencia de usuarios {#user-matching}

Los usuarios identificados pueden coincidir por su `external_id` o `alias`. Los usuarios anónimos pueden coincidir por su `device_id`. Los usuarios identificados que fueron creados originalmente como usuarios anónimos no pueden ser identificados por su `device_id`, y deben ser identificados por su `external_id` o `alias`.