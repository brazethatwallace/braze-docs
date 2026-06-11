---
nav_title: Registros de sincronización y observabilidad
article_title: Registros de sincronización y observabilidad
page_order: 8
page_type: reference
description: "Esta página ofrece un resumen de las características de observabilidad disponibles en CDI."
---

# Registros de sincronización y observabilidad {#sync-logs-and-observability}

> El panel de **Sync Log** de la Ingesta de datos de Cloud (CDI) te permite supervisar todos los datos procesados por CDI, verificar si los datos se sincronizaron correctamente y diagnosticar cualquier problema con datos «incorrectos» o faltantes.

Para acceder a los registros de sincronización, ve a **Configuración de datos** > **Ingesta de datos de Cloud** y selecciona la pestaña **Sync Log**.

## Comprender el panel de Sync Log {#understanding-the-sync-log-dashboard}

La página principal de **Sync Log** ofrece un resumen de alto nivel de todas tus ejecuciones de sincronización, incluido un resumen de las sincronizaciones recientes según su estado actual o final.

* **Running:** Trabajos de sincronización que están actualmente en curso.
* **Success:** Trabajos de sincronización que se completaron y todas las filas se procesaron correctamente.
* **Partial Success:** Trabajos de sincronización que se completaron, pero una o más filas encontraron un error.
* **Error:** Trabajos de sincronización que no se completaron.
* **Limit Exceeded:** Trabajos de sincronización que dejaron de procesarse porque se superó un límite de datos.

![Un ejemplo de registros de sincronización con un total de 6576 éxitos.]({% image_buster /assets/img/cloud_ingestion/sync_logs1.png %}){: style="max-width:80%"}

Los registros de sincronización también proporcionan los siguientes detalles para cada sincronización:

* **Nombre de sincronización:** El nombre de la configuración de sincronización.
* **ID de ejecución:** Un identificador único para una ejecución específica de la sincronización. Selecciona este ID para ver más detalles. También se puede utilizar en los [puntos finales de la API de CDI]({{site.baseurl}}/api/endpoints/cdi/) o para hacer referencia a una ejecución de sincronización con el soporte de Braze.
* **Estado:** El estado de la ejecución (éxito, éxito parcial, error, en ejecución).
* **Nuevas filas leídas desde la fuente:** El número de filas nuevas extraídas de tu almacén de datos para esta ejecución.
* **Resultados:** Un desglose de cuántas filas se procesaron correctamente o fallaron durante la ejecución.
* **Último `UPDATED_AT`:** La marca de tiempo del registro más reciente procesado en esta ejecución de sincronización.
* **Hora de inicio de la ejecución:** Cuándo comenzó el trabajo de sincronización.
* **Duración de la ejecución:** El tiempo total que tardó en completarse el trabajo de sincronización.

![Detalles de un registro de sincronización.]({% image_buster /assets/img/cloud_ingestion/sync_logs3.png %}){: style="max-width:80%"}

### Retención de datos {#data-retention}

Los datos del registro de sincronización, incluidas todas las cargas útiles a nivel de fila y los detalles de los errores, se conservan durante un máximo de **30 días**. Los registros con más de 30 días de antigüedad se eliminarán automáticamente.

Los metadatos de la ejecución de sincronización, como el número de filas procesadas, se conservan durante al menos 12 meses.

### Filtrado de registros de sincronización {#filtering-sync-logs}

Puedes filtrar la tabla de registros de sincronización para encontrar ejecuciones específicas. Los filtros disponibles incluyen:

* **Fecha de inicio del trabajo:** Selecciona un intervalo predefinido (como «Últimos 30 días») o un intervalo de fechas personalizado.
* **Estado:** Filtra por uno o más estados de sincronización (por ejemplo, mostrar solo los estados **Error** y **Partial Success**).
* **Nombre de sincronización:** Busca una sincronización específica por su nombre.

Para investigar una sincronización específica, selecciona el **Run ID** correspondiente en la tabla de registros de sincronización. En la página de **Run details**, encontrarás un registro detallado, fila por fila, de la sincronización.

### Resumen de la ejecución {#run-overview}

Esta sección resume la ejecución seleccionada, incluyendo la hora de inicio, la hora de finalización, la duración y el número total de filas leídas desde la fuente. También proporciona un recuento de cuántas filas se procesaron correctamente y cuántas dieron lugar a un error.

### Filas procesadas en esta ejecución {#rows-processed-in-this-run}

Esta tabla proporciona visibilidad a nivel de fila de los datos procesados durante la sincronización, lo que te permite validar registros individuales.

* **Buscar:** Puedes buscar un usuario específico dentro de los resultados de la ejecución utilizando la barra **Search by user ID**.
* **Detalles disponibles:**
  * **`UPDATED_AT`:** La marca de tiempo de la columna `UPDATED_AT` para esa fila específica.
  * **ID:** Los identificadores de usuario (como `external_id`, `email` o `alias_name`) utilizados para relacionar el registro con un perfil de usuario de Braze.
  * **Estado:** El estado de procesamiento individual de esa fila (**Success** o **Error**).
  * **Carga útil de origen:** Un enlace para ver la carga útil de datos.
  * **Motivo del error:** Si el estado es **Error**, esta columna muestra un mensaje que explica por qué la fila no se sincronizó.

#### Visualización de cargas útiles {#viewing-payloads}

Para ver los datos exactos enviados a Braze para una fila específica, selecciona **View payload** en la columna de carga útil de **Source**. Esto muestra la carga útil JSON sin procesar que se procesó para ese usuario.

![Ejemplo de carga útil para una fila específica en un registro de sincronización.]({% image_buster /assets/img/cloud_ingestion/sync_logs2.png %}){: style="max-width:80%"}

#### Exportación de registros de sincronización {#exporting-sync-logs}

Selecciona **Export rows** para exportar los registros a nivel de fila de una ejecución de sincronización. A continuación, elige exportar por:

* **Filas con errores:** Descarga un archivo que contiene solo las filas que tenían un estado **Error**.
* **Todas las filas:** Descarga un archivo que contiene todas las filas procesadas en la ejecución.

{% multi_lang_include early_access_beta_alert.md feature='Exporting sync logs for all rows' %}

Los registros no se pueden exportar directamente desde el dashboard. Una vez generada la exportación, recibirás un correo electrónico con un enlace para descargar el archivo de exportación del registro.

## Notificaciones {#notifications}

Puedes configurar notificaciones por correo electrónico para mantenerte informado sobre el estado de tus sincronizaciones CDI. Esta configuración se establece al crear una sincronización y se puede actualizar en cualquier momento.

### Notificaciones de error {#error-notifications}

Se requiere al menos una dirección de correo electrónico de contacto para recibir notificaciones sobre errores a nivel de sincronización. Estas alertas se envían cuando un trabajo de sincronización completo no se ejecuta o no se completa, o si la sincronización encuentra un error que requiere la intervención del usuario, como credenciales caducadas o una tabla de origen faltante.

Las notificaciones adicionales incluyen:

- **Error de fila:** Recibe alertas cuando un determinado porcentaje de filas no se actualiza durante una sincronización.
- **Umbral de fallo (%):** Especifica el porcentaje de fallos en las filas que debe desencadenar una alerta. Por ejemplo, si se establece en **1**, se enviará una notificación si el 1 % o más de las filas de una ejecución de sincronización dan lugar a un error.
- **Sincronización correcta:** Recibe una notificación cuando se complete correctamente una sincronización.
- **Alerta incluso si no hay cambios en las filas:** Recibe una notificación incluso cuando una ejecución de sincronización correcta no procesa ninguna fila nueva o actualizada.