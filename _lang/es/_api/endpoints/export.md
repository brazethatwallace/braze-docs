---
nav_title: Exportar
article_title: Endpoints de exportación
search_tag: Endpoint
page_order: 2
description: "Este artículo de referencia explica los endpoints de exportación de Braze, incluidos los requisitos previos, lo que puedes exportar, cómo se entregan los datos y una lista completa."
page_type: reference
---

# Endpoints de exportación {#export-endpoints}

Con esta colección de endpoints, puedes acceder y exportar diversos niveles de detalle sobre tus indicador clave de rendimiento, sesiones de aplicación, usuarios, Segments, Campaigns y Canvas. Asegúrate de conocer tu [instancia de Braze]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints), [clave de API]({{site.baseurl}}/api/basics) e [identificador de API]({{site.baseurl}}/api/identifier_types) al crear tus parámetros y cuerpos de solicitud.

## Requisitos previos {#prerequisites}

Antes de empezar, asegúrate de tener lo siguiente:

| Requisito | Descripción |
| --- | --- |
| Clave de API REST or transferencia de estado representacional de Braze | Una clave de API REST or transferencia de estado representacional con los permisos de exportación apropiados para los endpoints que planeas llamar. Las claves de API tienen un alcance limitado a endpoints específicos, y los permisos no se pueden cambiar después de la creación. Para más detalles, consulta [Clave de API REST or transferencia de estado representacional]({{site.baseurl}}/api/basics#about-rest-api-keys). |
| Identificadores relevantes | Los identificadores de los datos que deseas exportar, como un ID de Campaign, un ID de Segment o un ID de Canvas. Puedes encontrarlos en el panel de Braze. Para una lista completa, consulta [Tipos de identificadores de API]({{site.baseurl}}/api/identifier_types). |
| Credenciales de almacenamiento en el cloud (opcional) | Si estás exportando conjuntos de datos grandes, conecta un contenedor de [Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3), [Microsoft Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents) o [Google Cloud Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/google_cloud_storage_for_currents) para que los archivos de exportación se escriban directamente en tu almacenamiento. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

{% alert note %}
Si eres un especialista en marketing o miembro de un equipo sin acceso a la API, coordina con un desarrollador o administrador de tu organización para configurar las claves de API y las integraciones.
{% endalert %}

## Lo que puedes exportar {#what-you-can-export}

La siguiente tabla resume las categorías de datos disponibles a través de las API de exportación.

| Categoría | Qué incluye | Referencia de la API |
| --- | --- | --- |
| Campaigns | Análisis de rendimiento, detalles de Campaign, listas de Campaigns y análisis de envíos | [Endpoints de Campaign]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics) |
| Canvas | Análisis de series de datos, resúmenes de análisis, detalles de Canvas y listas de Canvas | [Endpoints de Canvas]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics) |
| Segments | Listas de Segments, análisis de Segments y detalles de Segments | [Endpoints de Segment]({{site.baseurl}}/api/endpoints/export/segments/get_segment) |
| Datos de usuario | Perfiles de usuario completos por identificador o por segmento, y usuarios por grupo de control global | [Endpoints de datos de usuario]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier) |
| KPIs | Usuarios activos diarios, MAU or usuarios activos al mes or usuarios activos al mes, nuevos usuarios diarios y desinstalaciones por fecha | [Endpoints de indicador clave de rendimiento]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_dau_date) |
| Sesiones | Datos de series temporales de sesiones de la aplicación | [Endpoint de sesiones]({{site.baseurl}}/api/endpoints/export/sessions/get_sessions_analytics) |
| Eventos personalizados | Nombres de eventos, listas de eventos y análisis de eventos a lo largo del tiempo | [Endpoints de eventos personalizados]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_data) |
| Atributos personalizados | Nombres de atributos | [Endpoint de atributos personalizados]({{site.baseurl}}/api/endpoints/export/custom_attributes/get_custom_attributes) |
| Compras | Datos de ingresos por tiempo, listas de ID de producto y recuentos de compras | [Endpoints de compras]({{site.baseurl}}/api/endpoints/export/purchases/get_revenue_series) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Lo que puedes exportar" }

## Cómo se entregan los datos de exportación {#how-export-data-is-delivered}

Las exportaciones de la API devuelven datos en formato JSON, a diferencia de los archivos CSV que descargas del panel. El método de entrega depende de si tienes almacenamiento en el cloud conectado:

- **Sin almacenamiento en el cloud:** Braze escribe los archivos de exportación en su propio contenedor de S3 e incluye una URL de descarga temporal en la respuesta de la API. Esta URL caduca a las cuatro horas, y la exportación se empaqueta como un archivo comprimido (ZIP o GZIP, según el parámetro `output_format`) que contiene archivos JSON. Cada línea de los archivos JSON representa un objeto de datos.
- **Con almacenamiento en el cloud conectado:** Braze escribe los archivos de exportación directamente en tu contenedor configurado. La respuesta de la API no incluye una URL de descarga. Los archivos siguen tus propias políticas de retención y suelen ser más fiables para exportaciones grandes.

{% alert tip %}
"Almacenamiento en el cloud" se refiere a tu propio contenedor de almacenamiento (por ejemplo, Amazon S3, Microsoft Azure Blob Storage o Google Cloud Storage). Puedes conectar tu contenedor en **Integraciones de partners** > **Partners tecnológicos** para que Braze pueda escribir los archivos de exportación directamente en él.
{% endalert %}

Para más detalles sobre la entrega de exportaciones y la solución de problemas, consulta [Solución de problemas de exportación]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting).

## Endpoints de exportación

La siguiente tabla muestra todas las API de exportación disponibles.

| Categoría | Método | Endpoint |
| --- | --- | --- |
| Campaigns | GET | [Análisis de Campaign]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics) |
| Campaigns | GET | [Detalles de Campaign]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details) |
| Campaigns | GET | [Lista de Campaigns]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns) |
| Campaigns | GET | [Análisis de envío]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics) |
| Canvas | GET | [Análisis de series de datos de Canvas]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics) |
| Canvas | GET | [Resumen de análisis de Canvas]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary) |
| Canvas | GET | [Detalles de Canvas]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details) |
| Canvas | GET | [Lista de Canvas]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases) |
| Eventos personalizados | GET | [Eventos personalizados]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_data) |
| Eventos personalizados | GET | [Lista de eventos personalizados]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events) |
| Eventos personalizados | GET | [Análisis de eventos personalizados]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_analytics) |
| Atributos personalizados | GET | [Atributos personalizados]({{site.baseurl}}/api/endpoints/export/custom_attributes/get_custom_attributes) |
| indicador clave de rendimiento | GET | [indicador clave de rendimiento de nuevos usuarios diarios por fecha]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_daily_new_users_date) |
| indicador clave de rendimiento | GET | [indicador clave de rendimiento de usuarios activos diarios por fecha]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_dau_date) |
| indicador clave de rendimiento | GET | [indicador clave de rendimiento de MAU or usuarios activos al mes or usuarios activos al mes en los últimos 30 días]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_mau_30_days) |
| indicador clave de rendimiento | GET | [indicador clave de rendimiento de desinstalaciones por fecha]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_uninstalls_date) |
| Compras | GET | [Lista de ID de productos]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id) |
| Compras | GET | [Número de compras]({{site.baseurl}}/api/endpoints/export/purchases/get_number_of_purchases) |
| Compras | GET | [Datos de ingresos por período]({{site.baseurl}}/api/endpoints/export/purchases/get_revenue_series) |
| Segments | GET | [Lista de Segments]({{site.baseurl}}/api/endpoints/export/segments/get_segment) |
| Segments | GET | [Análisis de Segment]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics) |
| Segments | GET | [Detalles de Segment]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details) |
| Sesiones | GET | [Datos de series temporales de sesiones de la aplicación]({{site.baseurl}}/api/endpoints/export/sessions/get_sessions_analytics) |
| Datos de usuario | POST | [Datos de usuario por identificador]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier) |
| Datos de usuario | POST | [Datos de usuario por Segment]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment) |
| Datos de usuario | POST | [Datos de usuario por grupo de control global]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Endpoints de exportación" }

## Artículos relacionados {#related-articles}

Para exportaciones puntuales desde el panel, consulta estos artículos:

- [Exportar datos de Campaign]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_campaign_results_data)
- [Exportar datos de Canvas]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_canvas_data)
- [Exportar datos de Segment a CSV]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/segment_data_to_csv)