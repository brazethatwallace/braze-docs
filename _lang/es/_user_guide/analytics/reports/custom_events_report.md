---
nav_title: Informe de eventos personalizados
article_title: Informe de eventos personalizados
page_order: 6
page_type: reference
description: "Esta página describe cómo usar el informe de eventos personalizados para ver las ocurrencias de eventos personalizados a lo largo del tiempo, desglosadas por segmento."
tool: Reports
---

# Informe de eventos personalizados {#custom-events-report}

> El informe de eventos personalizados te permite ver las ocurrencias de uno o más eventos personalizados a lo largo del tiempo. Puedes desglosar los resultados por segmento, aplicar fórmulas de indicador clave de rendimiento y exportar los datos para un análisis más detallado.

## Ver un informe {#view-a-report}

Para ver este informe desde el panel, ve a **Analytics** > **Custom Events Report**. Selecciona los eventos personalizados que deseas analizar. El gráfico se genera automáticamente después de seleccionar un evento.

![Eventos personalizados]({% image_buster /assets/img_archive/Export_events.png %})

### Eventos personalizados de API y filtros de aplicación {#api-custom-events-and-app-filters}

Los eventos personalizados enviados a través del endpoint [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) pueden incluir opcionalmente `app_id`. A diferencia de los eventos registrados a través del SDK, los eventos de API no se asocian automáticamente con una aplicación. Sin `app_id`, los eventos se registran pero no aparecerán en el gráfico de eventos personalizados cuando se aplica un filtro de aplicación.

## Configura tu informe {#configure-your-report}

Usa las siguientes opciones para personalizar qué datos aparecen en el gráfico de eventos personalizados.

| Opción | Descripción |
| --- | --- |
| Aplicaciones | De forma predeterminada, el informe incluye datos de todas las aplicaciones. Usa este menú desplegable para limitar el informe a una aplicación específica. |
| Desglosar eventos personalizados por | Controla cómo se agrupa la serie temporal del evento personalizado seleccionado. De forma predeterminada, el gráfico muestra la tendencia agregada general por fecha. Cambia a **Custom Events by Hour** para ver patrones intradía, o a **Custom Events per MAU** para normalizar el volumen de eventos respecto a tu recuento de MAU. |
| Filtrar por Segments | Activa esta opción para desglosar los recuentos de eventos por uno o más Segments. Cuando está habilitada, selecciona los Segments que deseas comparar. El gráfico muestra el número de usuarios en cada Segment que realizaron el evento personalizado. |
| Fórmula de indicador clave de rendimiento | Reemplaza el recuento bruto de eventos con una métrica calculada construida a partir de un numerador (como un recuento de eventos personalizados) y un denominador (como usuario activo diario, MAU o el tamaño de un Segment habilitado para análisis). Cuando seleccionas una o más fórmulas, el gráfico traza el valor de cada fórmula a lo largo del rango de fechas seleccionado para que puedas comparar el rendimiento normalizado (por ejemplo, "eventos por usuario activo") en lugar del volumen total de eventos. Si no hay datos disponibles para el rango de tiempo y las fórmulas seleccionadas, Braze muestra un mensaje de "sin datos"; amplía el rango de tiempo o elige fórmulas diferentes. Selecciona **Manage indicador clave de rendimiento formulas** para crear o editar fórmulas. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Configura tu informe" }

## Exportar datos {#export-data}

Para exportar los datos de tus eventos personalizados, selecciona <i class="fas fa-bars" title="Menú contextual del gráfico"></i> **Menú contextual del gráfico** en el gráfico de eventos personalizados y selecciona tu opción de exportación.

{% alert tip %}
Para obtener ayuda con las exportaciones de CSV y API, consulta [Solución de problemas de exportación]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting).
{% endalert %}

## Solución de problemas {#troubleshooting}

### El desglose del Segment no coincide con los totales del espacio de trabajo {#segment-breakdown-doesnt-match-workspace-totals}

Cuando usas **Filtrar por Segments** o limitas el informe con el menú desplegable **Apps**, el gráfico cuenta los usuarios en el Segment (o aplicación) seleccionado que realizaron el evento personalizado, no cada ocurrencia del evento en todo el espacio de trabajo.

Si comparas una línea de Segment con una vista sin filtrar (o con **All Apps**), los totales suelen diferir porque:

- **All Apps** puede incluir usuarios y eventos de todas las aplicaciones del espacio de trabajo.
- Un filtro de una sola aplicación solo incluye perfiles vinculados a esa aplicación.
- Los filtros de Segment cuentan los usuarios que coinciden con la definición del Segment en el momento de la consulta, lo que puede excluir a usuarios que realizaron el evento fuera de los criterios del Segment.

Para comparar de forma equivalente, usa el mismo filtro de aplicación y la misma selección de Segment para cada serie que compares, o exporta los datos y concilia los recuentos en tu herramienta de análisis.