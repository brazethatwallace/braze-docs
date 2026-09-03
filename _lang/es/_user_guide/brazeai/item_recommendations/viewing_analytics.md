---
nav_title: Análisis
article_title: "Análisis de recomendaciones de artículos"
description: "Obtén información sobre el análisis de recomendaciones de artículos y cómo verlos en Braze."
page_order: 1.3
---

# Análisis de recomendaciones de artículos {#item-recommendation-analytics}

> Obtén información sobre el análisis de recomendaciones de artículos y cómo verlos en Braze.

## Ver análisis {#view-analytics}

Puedes ver los análisis de tu recomendación para comprobar qué artículos se recomendaron a los usuarios y cuán preciso fue el modelo de recomendación.

1. Ve a **Analytics** > **Item Recommendation**.
2. Selecciona tu recomendación de la lista.

## Métricas disponibles {#available-metrics}

### Audiencia {#audience}

Estas métricas describen tu audiencia de recomendaciones. Dependiendo del tipo de recomendación y los datos de análisis disponibles, la sección **Audiencia** puede incluir **Precisión** y **Cobertura**.

Para las recomendaciones **Personalizadas con IA**, la tarjeta **Tipo de recomendación** muestra la tasa de personalización estimada, los usuarios con el evento configurado y la población total. Para las recomendaciones **Más recientes**, muestra la proporción de usuarios que reciben recomendaciones **Más recientes** frente a la alternativa de **Más populares**. Las recomendaciones **Más populares** y **Tendencias** no muestran un desglose del tipo de recomendación a nivel de usuario.

![Métricas de audiencia de recomendaciones que muestran precisión, cobertura y tipos de recomendación divididos entre elementos personalizados y más populares.]({% image_buster /assets/img/item_recs_analytics_1.png %}){: style="max-width:80%;"}

Consulta la siguiente tabla para más información:

| Métrica              | Descripción |
| ------------------- | ---------- |
| **Precisión**           | El porcentaje de veces que el modelo adivinó correctamente el siguiente artículo que un usuario compró. La precisión depende en gran medida del tamaño y la composición específicos de tu catálogo, y debe usarse como guía para entender con qué frecuencia el modelo es correcto.<br><br>En pruebas anteriores, los modelos han funcionado bien con números de precisión que van del 6 al 20 %. Esta métrica se actualiza cuando el modelo se reentrena.  |
| **Cobertura**            | Qué porcentaje de los artículos disponibles en el catálogo se recomiendan a al menos un usuario. Puedes esperar una mayor cobertura de artículos con recomendaciones de artículos personalizadas en comparación con las más populares. |
| **Tasa de personalización** | Para las recomendaciones **Personalizadas con IA**, el porcentaje estimado de usuarios con recomendaciones personalizadas almacenadas en su perfil, calculado contra el número total de usuarios que han realizado el evento configurado en los últimos 24 meses. Los usuarios que realizaron el evento pero no tienen suficientes datos para generar una recomendación personalizada reciben los artículos más populares como alternativa cuando se les envía un mensaje. |
| **Tipo de recomendación** | Para las recomendaciones **Más recientes**, el porcentaje de usuarios que reciben recomendaciones **Más recientes** en comparación con la alternativa de **Más populares**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Audiencia" }

### Artículos {#items}

Esta tabla incluye métricas sobre tus artículos personalizados, más recientes y más populares de tu catálogo.

![Tablas lado a lado que enumeran los artículos asignados a los usuarios, separados por recomendaciones personalizadas y recomendaciones más populares.]({% image_buster /assets/img/item_recs_analytics_2.png %})

Consulta la siguiente tabla para más información:

| Métrica              | Descripción |
| ------------------- | ---------- |
| **Artículos personalizados**<br><br>**Artículos más recientes** | Esta columna enumera cada artículo del catálogo en orden descendente de los más recomendados a los usuarios. Esta columna también muestra cuántos usuarios fueron asignados a cada artículo por el modelo.<br><br>Se mostrarán los artículos **Personalizados** o **Más recientes** dependiendo del [tipo de recomendación]({{site.baseurl}}/user_guide/brazeai/item_recommendations). |
| **Artículos más populares** | Esta columna enumera cada artículo del catálogo en orden descendente de popularidad. La popularidad aquí se refiere a los artículos del catálogo con los que los usuarios interactúan con mayor frecuencia en todo el espacio de trabajo. Los más populares se usan como alternativa cuando las recomendaciones personalizadas o más recientes no pueden calcularse para un usuario individual. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Artículos" }

### Resumen {#overview}

Este es un resumen de la configuración de recomendación elegida, que incluye cuándo se actualizó la recomendación por última vez.

![Tabla de resumen de recomendaciones que muestra el tipo, catálogo, tipo de evento, nombre del evento personalizado, nombre de la propiedad y fecha de última actualización.]({% image_buster /assets/img/item_recs_analytics_3.png %}){: style="max-width:50%" }