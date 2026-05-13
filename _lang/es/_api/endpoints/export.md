---
nav_title: Exportar
article_title: Puntos finales de exportación
search_tag: Endpoint
page_order: 2
description: "Este artículo de referencia explica los puntos finales de exportación de Braze, incluidos los requisitos previos, lo que puedes exportar, cómo se entregan los datos y una lista completa de puntos finales."
page_type: reference
---

# Puntos finales de exportación {#export-endpoints}

Con esta colección de puntos finales, puedes acceder y exportar diversos niveles de detalle sobre tus KPI, sesiones de aplicación, usuarios, Segments, Campaigns y Canvas. Asegúrate de conocer tu [instancia de Braze]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints/), [clave de API]({{site.baseurl}}/api/api_key/) e [identificador de API]({{site.baseurl}}/api/identifier_types/) al crear tus parámetros y cuerpos de solicitud.

## Requisitos previos {#prerequisites}

Antes de empezar, asegúrate de tener lo siguiente:

| Requisito | Descripción |
| --- | --- |
| Clave de API REST de Braze | Una clave de API REST con los permisos de exportación adecuados para los puntos finales que planeas llamar. Las claves de API tienen un alcance limitado a puntos finales específicos, y los permisos no se pueden cambiar después de la creación. Para más detalles, consulta [Clave de API REST]({{site.baseurl}}/api/basics/#about-rest-api-keys). |
| Identificadores relevantes | Los identificadores de los datos que deseas exportar, como un ID de Campaign, un ID de Segment o un ID de Canvas. Puedes encontrarlos en el dashboard de Braze. Para una lista completa, consulta [Tipos de identificadores de API]({{site.baseurl}}/api/identifier_types/). |
| Credenciales de almacenamiento en la nube (opcional) | Si estás exportando conjuntos de datos grandes, conecta un contenedor de [Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3/), [Microsoft Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents/) o [Google Cloud Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/google_cloud_storage_for_currents/) para que los archivos de exportación se escriban directamente en tu almacenamiento. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

{% alert note %}
Si eres un especialista en marketing o miembro de un equipo sin acceso a la API, coordínate con un desarrollador o administrador de tu organización para configurar las claves de API y las integraciones.
{% endalert %}

## Qué puedes exportar {#what-you-can-export}

La siguiente tabla resume las categorías de datos disponibles a través de las API de exportación.

| Categoría | Qué incluye | Referencia de API |
| --- | --- | --- |
| Campaigns | Análisis de rendimiento, detalles de Campaign, listas de Campaigns y análisis de envíos | [Puntos finales de Campaigns]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/) |
| Canvas | Análisis de series de datos, resúmenes de análisis, detalles de Canvas y listas de Canvas | [Puntos finales de Canvas]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics/) |
| Segments | Listas de Segments, análisis de Segments y detalles de Segments | [Puntos finales de Segments]({{site.baseurl}}/api/endpoints/export/segments/get_segment/) |
| Datos de usuario | Perfiles de usuario completos por identificador o por Segment, y usuarios por grupo de control global | [Puntos finales de datos de usuario]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) |
| KPI | Usuarios activos diarios, usuarios activos al mes, nuevos usuarios diarios y desinstalaciones por fecha | [Puntos finales de KPI]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_dau_date/) |
| Sesiones | Datos de series temporales de sesiones de aplicación | [Punto final de sesiones]({{site.baseurl}}/api/endpoints/export/sessions/get_sessions_analytics/) |
| Eventos personalizados | Nombres de eventos, listas de eventos y análisis de eventos a lo largo del tiempo | [Puntos finales de eventos personalizados]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_data/) |
| Atributos personalizados | Nombres de atributos | [Punto final de atributos personalizados]({{site.baseurl}}/api/endpoints/export/custom_attributes/get_custom_attributes/) |
| Compras | Datos de ingresos por tiempo, listas de ID de productos y recuentos de compras | [Puntos finales de compras]({{site.baseurl}}/api/endpoints/export/purchases/get_revenue_series/) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="What you can export" }

## Cómo se entregan los datos de exportación {#how-export-data-is-delivered}

Las exportaciones de API devuelven datos en formato JSON, a diferencia de los archivos CSV que descargas desde el dashboard. El método de entrega depende de si tienes almacenamiento en la nube conectado:

- **Sin almacenamiento en la nube:** Braze escribe los archivos de exportación en su propio contenedor de S3 e incluye una URL de descarga temporal en la respuesta de la API. Esta URL expira después de cuatro horas, y la exportación se empaqueta como un archivo comprimido (ZIP o GZIP, según el parámetro `output_format`) que contiene archivos JSON. Cada línea en los archivos JSON representa un objeto de datos.
- **Con almacenamiento en la nube conectado:** Braze escribe los archivos de exportación directamente en tu contenedor configurado. La respuesta de la API no incluye una URL de descarga. Los archivos siguen tus propias políticas de retención y suelen ser más fiables para exportaciones grandes.

{% alert tip %}
"Almacenamiento en la nube" se refiere a tu propio contenedor de almacenamiento (por ejemplo, Amazon S3, Microsoft Azure Blob Storage o Google Cloud Storage). Puedes conectar tu contenedor en **Integraciones de socios** > **Socios tecnológicos** para que Braze pueda escribir archivos de exportación directamente en él.
{% endalert %}

Para más detalles sobre la entrega de exportaciones y la solución de problemas, consulta [Solución de problemas de exportación]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting/).

## Puntos finales de exportación

La siguiente tabla enumera todas las API de exportación disponibles.

| Categoría | Método | Punto final |
| --- | --- | --- |
| Campaigns | GET | [Campaign Analytics]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/) |
| Campaigns | GET | [Campaign Details]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details/) |
| Campaigns | GET | [Campaigns List]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns/) |
| Campaigns | GET | [Send Analytics]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics/) |
| Canvas | GET | [Canvas Data Series Analytics]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics/) |
| Canvas | GET | [Canvas Analytics Summary]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary/) |
| Canvas | GET | [Canvas Details]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/) |
| Canvas | GET | [Canvas List]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases/) |
| Eventos personalizados | GET | [Custom Events]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_data/) |
| Eventos personalizados | GET | [Custom Events List]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events/) |
| Eventos personalizados | GET | [Custom Event Analytics]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_analytics/) |
| Atributos personalizados | GET | [Custom Attributes]({{site.baseurl}}/api/endpoints/export/custom_attributes/get_custom_attributes/) |
| KPI | GET | [KPIs for Daily New Users by Date]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_daily_new_users_date/) |
| KPI | GET | [KPIs for Daily Active Users by Date]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_dau_date/) |
| KPI | GET | [KPIs for Monthly Active Users Over Last 30 Days]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_mau_30_days/) |
| KPI | GET | [KPIs for Uninstalls by Date]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_uninstalls_date/) |
| Compras | GET | [Product IDs List]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id/) |
| Compras | GET | [Number of Purchases]({{site.baseurl}}/api/endpoints/export/purchases/get_number_of_purchases/) |
| Compras | GET | [Revenue Data by Time]({{site.baseurl}}/api/endpoints/export/purchases/get_revenue_series/) |
| Segments | GET | [Segment List]({{site.baseurl}}/api/endpoints/export/segments/get_segment/) |
| Segments | GET | [Segment Analytics]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics/) |
| Segments | GET | [Segment Details]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details/) |
| Sesiones | GET | [App Sessions Time-Series Data]({{site.baseurl}}/api/endpoints/export/sessions/get_sessions_analytics/) |
| Datos de usuario | POST | [User Data by Identifier]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) |
| Datos de usuario | POST | [User Data by Segment]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/) |
| Datos de usuario | POST | [User Data by Global Control Group]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group/) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Export endpoints" }

## Artículos relacionados {#related-articles}

Para exportaciones puntuales desde el dashboard, consulta estos artículos:

- [Exportar datos de Campaign]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_campaign_results_data/)
- [Exportar datos de Canvas]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_canvas_data/)
- [Exportar datos de Segment a CSV]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/segment_data_to_csv/)