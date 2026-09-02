---
nav_title: Census
article_title: Importación de cohortes de Census
description: "Este artículo de referencia describe la funcionalidad de importación de cohortes de Census, una plataforma de integración de datos que te permite crear dinámicamente segmentos de usuarios específicos con datos de tu almacén de datos."
page_type: partner
search_tag: Partner

---

# Importación de cohortes de Census {#census-cohort-import}

> Este artículo describe cómo importar cohortes de usuarios de [Census](https://www.getcensus.com/) a Braze. Para más información sobre la integración de Census, consulta el [artículo principal sobre Census]({{site.baseurl}}/partners/data_and_analytics/reverse_etl/census).

## Integración de importación de cohortes {#cohort-import-integration}

### Paso 1: Crear una conexión de servicio Braze {#step-1-create-braze-service-connection}

Para integrar Census en la plataforma Census, ve a la pestaña **Connections** y selecciona **New Destination** para crear una nueva conexión de servicio Braze.

En la ventana que aparece, asigna un nombre a esta conexión e indica la URL de tu endpoint de Braze, la clave de API REST de Braze y la clave de importación de datos. La clave de importación de datos es necesaria para sincronizar cohortes y se puede encontrar en Braze yendo a **Partner Integrations** > **Technology Partners** > **Census**.

![Diálogo de nuevo destino de Census configurado con las credenciales de importación de cohortes de Braze.]({% image_buster /assets/img/census/add_service.png %}){: style="max-width:60%;"}

### Paso 2: Crear una sincronización de Census {#step-2-create-a-census-sync}

Para sincronizar clientes con Braze, debes crear una sincronización. Aquí definirás dónde sincronizar los datos y cómo quieres que se mapeen los campos entre las dos plataformas.

1. Ve a la pestaña **Syncs** y selecciona **New Sync**.<br><br>
2. En el creador, selecciona el modelo de datos de origen de tu almacén de datos.<br><br>
3. Configura dónde se sincronizará el modelo. Selecciona **Braze** como destino y **User & Cohort** como objeto a sincronizar.<br>![En la ventana "Select a Destination", se selecciona "Braze" como conexión y se enumeran varios objetos.]({% image_buster /assets/img/census/census_2.png %}){: style="max-width:80%;"}<br><br>
4. Selecciona la **Source Column** que identifica a los usuarios que se van a añadir a una cohorte, y selecciona **External User ID** como **Identifier Type**.<br><br>
5. En el desplegable **Cohort Name**, selecciona una cohorte, crea una cohorte o selecciona una columna de origen para rellenar el nombre de la cohorte.<br><br>
6. Utiliza el desplegable **When a record is removed from source data** para seleccionar lo que les ocurre a los usuarios cuando se eliminan del conjunto de datos de origen, como **Do nothing** o **Remove matching record from cohort**.<br><br>
7. Por último, mapea los campos de datos de Census a los campos equivalentes de Braze.<br>![Mapeado de Census]({% image_buster /assets/img/census/census_3.png %}){: style="max-width:80%;"}<br><br>
8. Confirma los detalles y crea la sincronización.

¡Ahora puedes ejecutar tu sincronización!

Durante una sincronización, los campos que mapees se sincronizarán primero con el objeto de usuario para actualizar lo que ya existe en Braze. Después, el usuario actualizado se añadirá a la cohorte especificada.

Tras la sincronización, puedes crear y añadir un Segment de Braze con un filtro de cohorte de Census a futuras Campaigns y Canvas de Braze para dirigirte a esos usuarios.

{% alert note %}
Al utilizar la integración de Census y Braze, Census solo enviará los deltas (datos cambiantes) en cada sincronización a Braze.
{% endalert %}

{% alert important %}
Solo se añadirán o eliminarán de una cohorte los usuarios que ya existan en Braze. La importación de cohortes no creará nuevos usuarios en Braze.
{% endalert %}

## Coincidencia de usuarios {#user-matching}

Los usuarios identificados pueden coincidir por su `external_id` o `alias`. Los usuarios anónimos pueden coincidir por su `device_id`. Los usuarios identificados que fueron creados originalmente como usuarios anónimos no pueden ser identificados por su `device_id`, y deben ser identificados por su `external_id` o `alias`.