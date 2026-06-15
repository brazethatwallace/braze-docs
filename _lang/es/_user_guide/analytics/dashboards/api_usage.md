---
nav_title: Uso de la API
article_title: Dashboard de uso de la API
alias: "/api_usage/"
page_order: 5
description: "Este artículo ofrece un resumen del dashboard de uso de la API."
---

# Dashboard de uso de la API {#api-usage-dashboard}

> El dashboard de uso de la API te permite monitorizar el tráfico entrante de la API REST hacia Braze para comprender las tendencias en tu uso de nuestras API REST y solucionar posibles problemas.

## Acerca del dashboard de uso de la API {#about-the-api-usage-dashboard}

Para ver tu dashboard de uso de la API, ve a **Settings** > **APIs and Identifiers** y selecciona **Dashboard**.

El dashboard predeterminado muestra todas las solicitudes entrantes de la API REST para tu espacio de trabajo durante el último día (24 horas). Según tu caso de uso, puedes ajustar los controles del dashboard para filtrar o agrupar el tráfico y también configurar el intervalo de tiempo del dashboard.

![Dashboard de uso de la API con 130 solicitudes totales, con una tasa de éxito del 70 por ciento y una tasa de error del 30 por ciento.]({% image_buster /assets/img/api_usage_dashboard/api_usage_dashboard.png %})

## Métricas disponibles {#available-metrics}

El dashboard de uso de la API incluye las siguientes estadísticas:

| Métrica         | Descripción |
|----------------|-------------|
| Solicitudes totales | El número total de solicitudes enviadas a Braze para tu espacio de trabajo actual, dados los filtros y controles aplicados al dashboard. |
| Tasa de éxito   | El porcentaje de solicitudes totales en las que Braze devolvió una respuesta de éxito `2XX`. |
| Tasa de error     | El porcentaje de solicitudes totales en las que Braze devolvió una respuesta de error `4XX` o `5XX`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Available metrics" }

## Uso del dashboard {#using-the-dashboard}

![Filtros para aplicar al dashboard, que incluyen: clave de API, punto de conexión, códigos de respuesta, agrupar datos y fecha.]({% image_buster /assets/img/api_usage_dashboard/filters.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

### Filtros {#filters}

Selecciona **Filters** para aplicar filtros que limiten la vista del tráfico de la API REST de tu espacio de trabajo, incluyendo:

- Clave de API
- Punto de conexión
- Código de respuesta

### Agrupar datos {#group-data}

Puedes agrupar datos en distintas series de datos para explorar diferentes patrones en tu uso, incluyendo:

- Códigos de respuesta (predeterminado)
- Punto de conexión de la API
- Clave de API
- Solo éxito y error

### Fecha {#date}

Ajusta el filtro de fecha para mostrar un intervalo de tiempo menor o mayor según sea necesario. Esto incluye:

- Hoy (predeterminado)
- Personalizado
- Últimas 3 horas
- Últimas 6 horas
- Últimas 12 horas
- Últimas 24 horas
- Ayer
- Últimos 7 días
- Últimos 14 días
- Últimos 30 días
- Mes en curso

{% alert note %}
Las opciones **Últimas 3 horas** y **Últimas 6 horas** mostrarán el tráfico por minutos. Los períodos de tiempo más largos mostrarán el tráfico cada cinco minutos, hora o día.
{% endalert %}

## Consideraciones {#considerations}

El dashboard de uso de la API incluye todas las solicitudes de la API REST que Braze recibió y para las que devolvió una respuesta `2XX`, `4XX` o `5XX`. Esto incluye las salidas de Transformación de datos y las sincronizaciones de Ingesta de datos de Cloud. El tráfico del SDK y los pasos de Actualización de usuario no se incluyen en este dashboard.

Los datos mostrados en el dashboard pueden tener un breve retraso a la hora de reflejar el tráfico reciente. Durante períodos de alto uso, puedes actualizar el dashboard hasta 4 veces por minuto. Es posible que debas esperar unos minutos antes de volver a actualizar el dashboard.

## Artículos relacionados {#related-articles}

- [Alertas de uso de la API]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/api_usage_alerts/)
- [Límites de velocidad]({{site.baseurl}}/api/api_limits/)