---
nav_title: Registros de sincronización y observabilidad
article_title: Registros de sincronización y observabilidad
page_order: 8
page_type: reference
description: "Esta página ofrece un resumen de las características de observabilidad disponibles en CDI."
---

# Registros de sincronización y observabilidad {#sync-logs-and-observability}

> El panel de **Sync Log** de la ingesta de datos en la nube (CDI) te permite supervisar todos los datos procesados por CDI, verificar si los datos se sincronizaron correctamente y diagnosticar cualquier problema con datos «incorrectos» o faltantes.

Para acceder a los registros de sincronización, ve a **Configuración de datos** > **Ingesta de datos en la nube** y selecciona la pestaña **Sync Log**.

<!-- support-analyzer-phase2:cdi_updated_at_row_sync -->
{% alert note %}
Si los recuentos de filas del almacén de datos no coinciden con **Rows Synced** o ves ejecuciones con **Partial Success**, abre el **Run ID** en Sync Log y revisa los valores de **Error reason** a nivel de fila. CDI selecciona filas usando `UPDATED_AT`: las filas con marcas de tiempo ya procesadas, con `UPDATED_AT` sin cambios después de ediciones, o escritas durante una sincronización activa pueden omitirse. Para casos comunes, consulta [¿Por qué "Rows Synced" no coincide con el número en mi almacén de datos?]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/faqs#why-doesnt-rows-synced-match-the-number-in-my-warehouse) y [Preguntas frecuentes sobre la ingesta de datos en la nube]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/faqs).
{% endalert %}

## Comprender el panel de registro de sincronización {#understanding-the-sync-log-dashboard}

La página principal de **Sync Log** proporciona un resumen de alto nivel de todas tus ejecuciones de sincronización, incluyendo un resumen de las sincronizaciones recientes según su estado actual o final.

* **Running:** Trabajos de sincronización que están actualmente en curso.
* **Success:** Trabajos de sincronización que se completaron y todas las filas se procesaron correctamente.
* **Partial Success:** Trabajos de sincronización que se completaron, pero una o más filas encontraron un error.
* **Error:** Trabajos de sincronización que no se pudieron completar.
* **Limit Exceeded:** Trabajos de sincronización que dejaron de procesarse porque se superó un límite de datos.

![Un ejemplo de registros de sincronización con 6.576 éxitos totales.]({% image_buster /assets/img/cloud_ingestion/sync_logs1.png %}){: style="max-width:80%"}

Los registros de sincronización también proporcionan los siguientes detalles para cada sincronización:

* **Sync name:** El nombre de la configuración de sincronización.
* **Run ID:** Un identificador único para una ejecución específica de la sincronización. Selecciona este ID para ver más detalles o para hacer referencia a una ejecución de sincronización con soporte de Braze.
* **Status:** El estado de la ejecución (success, partial success, error, running).
* **New rows read from source:** El número de filas nuevas extraídas de tu almacén de datos para esta ejecución.
* **Results:** Un desglose de cuántas filas tuvieron éxito o fallaron dentro de la ejecución.
* **Last "UPDATED_AT":** La marca de tiempo del registro más reciente procesado en esta ejecución de sincronización.
* **Run start time:** Cuándo comenzó el trabajo de sincronización.
* **Run duration:** El tiempo total que tardó en completarse el trabajo de sincronización.

### Retención de datos {#data-retention}

Los datos del registro de sincronización, incluidas todas las cargas útiles a nivel de fila y los detalles de errores, se conservan durante un máximo de **30 días**. Los registros con más de 30 días se eliminan automáticamente.

Los metadatos de ejecución de sincronización, como el número de filas procesadas, se conservan durante al menos 12 meses.

### Filtrar registros de sincronización {#filtering-sync-logs}

Puedes filtrar la tabla de registros de sincronización para encontrar ejecuciones específicas. Los filtros disponibles incluyen:

* **Job start date:** Selecciona un rango predefinido (como "Last 30 days") o un rango de fechas personalizado.
* **Status:** Filtra por uno o más estados de sincronización (como mostrar solo los estados **Error** y **Partial success**).
* **Sync name:** Busca una sincronización específica por su nombre.

Para investigar una sincronización específica, selecciona el **Run ID** correspondiente en la tabla de registros de sincronización. En la página de **Run details**, encontrarás un registro granular, fila por fila, de la sincronización.

### Resumen de la ejecución {#run-overview}

Esta sección resume la ejecución seleccionada, incluyendo su hora de inicio, hora de finalización, duración y el número total de filas leídas desde el origen. También proporciona un recuento de cuántas filas tuvieron éxito y cuántas resultaron en un error.

### Filas procesadas en esta ejecución {#rows-processed-in-this-run}

Esta tabla proporciona visibilidad a nivel de fila de los datos procesados durante la sincronización, lo que te permite validar registros individuales.

* **Search:** Puedes buscar un usuario específico dentro de los resultados de la ejecución usando la barra **Search by user ID**.
* **Detalles disponibles:**
  * **UPDATED_AT:** La marca de tiempo de la columna `UPDATED_AT` para esa fila específica.
  * **ID:** Los identificadores de usuario (como `external_id`, `email` o `alias_name`) utilizados para hacer coincidir el registro con un perfil de usuario de Braze.
  * **Status:** El estado de procesamiento individual para esa fila (**Success** o **Error**).
  * **Source payload:** Un enlace para ver la carga útil de datos.
  * **Error reason:** Si el estado es **Error**, esta columna proporciona un mensaje que explica por qué la fila no se pudo sincronizar.

#### Ver cargas útiles {#viewing-payloads}

Para ver los datos exactos enviados a Braze para una fila específica, selecciona **View payload** en la columna de carga útil **Source**. Esto muestra la carga útil JSON sin procesar que se procesó para ese usuario.

#### Exportar registros de sincronización {#exporting-sync-logs}

Selecciona **Export rows** para exportar los registros a nivel de fila de una ejecución de sincronización. Luego, elige exportar por:

* **Rows with errors:** Descarga un archivo que contiene solo las filas que tuvieron un estado de **Error**.
* **All rows:** Descarga un archivo que contiene todas las filas procesadas en la ejecución.

{% multi_lang_include alerts/early_access_beta_alert.md feature='Exporting sync logs for all rows' %}

Los registros no se pueden exportar directamente desde el panel. Después de que se genere la exportación, recibirás un correo electrónico con un enlace para descargar el archivo de exportación del registro.

## Notificaciones {#notifications}

Puedes configurar notificaciones por correo electrónico para mantenerte informado sobre el estado de tus sincronizaciones de CDI. Estos ajustes se configuran cuando creas una sincronización y se pueden actualizar en cualquier momento.

### Notificaciones de errores {#error-notifications}

Se requiere al menos una dirección de correo electrónico de contacto para recibir notificaciones de errores a nivel de sincronización. Estas alertas se envían cuando un trabajo de sincronización completo no se ejecuta o no se completa, o si la sincronización encuentra un error que requiere la intervención del usuario para solucionarlo, como credenciales caducadas o una tabla de origen faltante.

Las notificaciones adicionales incluyen:

- **Error de fila:** Recibe alertas cuando un determinado porcentaje de filas no se actualiza dentro de una sincronización.
- **Umbral de fallo (%):** Especifica el porcentaje de fallos de filas que debe desencadenar una alerta. Por ejemplo, establecer este valor en **1** enviaría una notificación si el 1 % o más de las filas en una ejecución de sincronización resultan en un error.
- **Sincronización exitosa:** Recibe una notificación cuando una sincronización se completa correctamente.
- **Alertar incluso si no cambian filas:** Recibe una notificación incluso cuando una ejecución de sincronización exitosa procesa cero filas nuevas o actualizadas.