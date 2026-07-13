---
nav_title: API de exportación
article_title: API de exportación
page_order: 5
page_type: reference
description: "Este artículo de referencia te ayuda a decidir cuándo usar las API de exportación en lugar de descargas CSV desde el dashboard."
platform: API

---

# API de exportación {#export-apis}

> Esta página te ayuda a decidir cuándo usar las API de exportación en lugar de descargas CSV desde el dashboard.

Las API de exportación de Braze te permiten exportar datos de Braze de forma programática como JSON. Para obtener detalles sobre lo que puedes exportar, los requisitos previos y cómo funciona la entrega, consulta [Puntos finales de exportación]({{site.baseurl}}/api/endpoints/export).

## Cuándo usar las API de exportación en lugar de descargas CSV {#when-to-use-export-apis-instead-of-csv-downloads}

La siguiente tabla describe escenarios comunes en los que usar la API de exportación es una mejor opción que una descarga CSV desde el dashboard.

| Escenario | Detalles |
| --- | --- |
| Tu exportación es demasiado grande para el dashboard | Las exportaciones CSV del dashboard están limitadas a 500 000 filas. Si estás exportando datos de un segmento con más de 500 000 usuarios, usa la API de exportación, que no tiene límite en la cantidad que puedes exportar. |
| Quieres automatizar informes recurrentes | Programa exportaciones de API a través de una integración para obtener datos de forma periódica sin interacción manual con el dashboard. |
| Necesitas alimentar herramientas externas con datos | Envía los datos de exportación directamente a herramientas de BI, almacenes de datos u otras plataformas de análisis. |
| Necesitas datos que no están disponibles como exportación CSV del dashboard | Algunas categorías de datos, incluidos KPI, series de ingresos, análisis de eventos personalizados y datos de sesión, solo están disponibles a través de la API. |
| Quieres interactuar con los datos de forma programática | Usa la salida JSON para procesamiento personalizado, transformaciones o integraciones. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Cuándo usar las API de exportación en lugar de descargas CSV" }

{% alert tip %}
Para obtener ayuda con las exportaciones CSV y de API, consulta [Solución de problemas de exportación]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting).
{% endalert %}