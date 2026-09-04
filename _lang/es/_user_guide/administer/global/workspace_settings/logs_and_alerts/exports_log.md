---
nav_title: Registro de exportaciones
article_title: Registro de exportaciones
page_order: 2
page_type: reference
description: "Esta página cubre el registro de exportaciones, que te permite ver el estado de los trabajos de exportación y cancelar las exportaciones en curso."
---

# Registro de exportaciones {#exports-log}

> Utiliza la página **Registro de exportaciones** para ver el estado de los trabajos de exportación y cancelar las exportaciones en curso directamente desde la plataforma Braze. El registro de exportaciones admite exportaciones de Segments y de [listas de supresión]({{site.baseurl}}/user_guide/audience/suppression_lists) iniciadas desde el panel o desde la [API de exportación de usuarios]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment).

Puedes encontrar el registro de exportaciones yendo a **Configuración** > **Configuración y pruebas** > **Registro de exportaciones**.

## Lo que muestra el registro de exportaciones {#what-the-exports-log-shows}

El registro de exportaciones enumera los trabajos de exportación del espacio de trabajo actual. Cada fila representa un intento de exportación e incluye el nombre del Segment o la lista de supresión, el origen de la exportación, el estado y las marcas de tiempo.

| Columna | Descripción |
|--------|-------------|
| ID de exportación | Identificador único del trabajo de exportación. Selecciona este ID para abrir los detalles de la exportación o compartir el registro. |
| Nombre del Segment | Nombre del Segment o la lista de supresión exportados. |
| Tipo de Segment | Si la exportación es para un **Segment** o una **lista de supresión**. |
| Origen | Desde dónde se desencadenó la exportación: **Panel** (exportación CSV desde la interfaz) o **API** (API de exportación de usuarios). |
| Estado | Estado actual del trabajo de exportación. Consulta [Estados de exportación](#export-statuses). |
| Iniciado en | Cuándo comenzó el trabajo de exportación. |
| Finalizado en | Cuándo se completó, falló o canceló el trabajo de exportación. En blanco mientras el trabajo está en curso. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Columnas del registro de exportaciones" }

## Estados de exportación {#export-statuses}

| Estado | Descripción |
|--------|-------------|
| In Progress | El trabajo de exportación se está ejecutando. |
| Complete | La exportación finalizó correctamente. |
| Failed | La exportación no se completó. |
| Cancelled | La exportación se canceló antes de completarse. |
| Cancelling | Una solicitud de cancelación está en curso. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Estados de exportación" }

Solo puedes cancelar exportaciones con el estado **In Progress**. Si una exportación ya no se está ejecutando, la acción de cancelar no está disponible.

## Detalles de la exportación {#export-details}

Selecciona un **Export ID** para ver detalles adicionales de ese trabajo, incluyendo:

| Campo | Descripción |
|-------|-------------|
| Destination | Dónde se entregan los archivos exportados (por ejemplo, una ruta de almacenamiento en el cloud cuando corresponda). |
| Fields Exported | Campos del perfil de usuario incluidos en la exportación. |
| Self Hosted | Si la exportación utiliza entrega alojada por el cliente. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Campos de detalles de exportación" }

Desde la página de detalles de la exportación, puedes cancelar una exportación en curso o compartir un enlace a la entrada del registro.

## Flujos de trabajo de exportación relacionados {#related-export-workflows}

| Tipo de exportación | Cómo empezar | Documentación |
|-------------|--------------|---------------|
| Exportación CSV de Segment | **Audiencia** > **Segments** > selecciona un segmento > **Datos de usuario** > **Exportación CSV** | [Exportar datos de segmentos a CSV]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/segment_data_to_csv) |
| Exportación de lista de supresión | **Audiencia** > **Listas de supresión** | [Listas de supresión]({{site.baseurl}}/user_guide/audience/suppression_lists) |
| Exportación de segmentos por API | `POST /users/export/segment` | [POST: Exportar perfil de usuario por segmento]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Flujos de trabajo de exportación relacionados" }

## Cancelar una exportación pendiente {#cancelling-a-pending-export}

Puedes cancelar las exportaciones pendientes directamente desde la página **Registro de exportaciones** seleccionando el menú <i class="fas fa-ellipsis-vertical"></i> y luego seleccionando **Cancelar exportación**, o seleccionando el **ID de exportación** y luego seleccionando **Cancelar exportación** en la página de la exportación.

## Compartir un registro de exportación específico {#sharing-a-specific-export-log}

Comparte un registro de exportación seleccionando el **Export ID** y luego seleccionando **Share Log**.