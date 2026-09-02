---
nav_title: Dashboard de referencias del sector
article_title: Dashboard de referencias del sector
alias: "/industry_benchmarks_dashboard/"
page_order: 3
description: "Este artículo ofrece un resumen del dashboard de referencias del sector."
---

# Dashboard de referencias del sector {#industry-benchmarks-dashboard}

> El dashboard de **referencias del sector** compara el rendimiento de participación de tu espacio de trabajo con referencias agregadas y respetuosas con la privacidad de empresas similares en cada sector.

Usa el dashboard de **referencias del sector** para comparar el rendimiento de tu correo electrónico, push, Content Cards y servicio de mensajes cortos con el de empresas similares del sector, e identificar canales y regiones donde hay oportunidades de optimización.

Para ver el dashboard de **referencias del sector**, ve a **Analytics** > **Dashboard Builder** y selecciona **Industry Benchmarks**. Si el dashboard no tiene datos, selecciona **Run Dashboard** para generar los resultados más recientes. Usa los filtros en la parte superior del dashboard para refinar los resultados por vertical del sector o periodo de tiempo.

## Acerca del panel {#about-the-dashboard}

El panel está organizado en cuatro secciones de canal: **Email**, **Push Notification**, **Content Card** y **servicio de mensajes cortos**:

| Sección              | Descripción                                                                                                                                             |
|----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| Tarjetas de indicador clave de rendimiento      | Muestran la tasa de tu espacio de trabajo para cada métrica clave, junto con la diferencia en comparación con la tasa del sector. Una flecha verde hacia arriba indica que tu espacio de trabajo está por encima de la tasa del sector; una flecha roja hacia abajo indica que está por debajo. |
| Gráfico de tendencia mensual | Representa la tasa de tu espacio de trabajo frente a la tasa del sector a lo largo del tiempo, para que puedas identificar estacionalidad y tendencias a largo plazo.                                   |
| Desglose regional    | Desglosa la tasa de tu espacio de trabajo frente a la tasa del sector en distintas regiones, para que puedas detectar dónde el rendimiento regional difiere del sector.         |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Sección" }

En todos los gráficos, la serie de color más claro representa el punto de referencia del sector y la serie más oscura (con el prefijo **Workspace**) representa tu propio rendimiento.

## Métricas disponibles {#available-metrics}

Cada métrica basada en canal está disponible en dos tipos:

| Tipo de métrica | Descripción | Ejemplo |
|----------|---------------------------------------|------------------------------------------------------|
| _Total_ | Cuenta cada evento de participación. | Si un usuario hace clic tres veces, se cuenta como tres clics. |
| _Distinto_ | Cuenta usuarios únicos. | Si un usuario hace clic tres veces, se cuenta como un clic. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Tipo de métrica" }

Las métricas se agrupan por las siguientes combinaciones de industria, región, subindustria y fecha:

- Industria + Fecha
- Industria + Región + Fecha
- Industria + Subindustria + Región + Fecha

Selecciona una pestaña para ver las métricas de cada canal.

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

{% tabs %}
{% tab Correo electrónico %}

<table aria-label="Métricas de correo electrónico"><thead><tr><th>Métrica</th><th>Descripción</th><th>Fórmula</th></tr></thead><tbody>
<tr><td class="no-split"><i>Unique Open Rate</i></td><td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Opens' %} Esta tasa excluye las aperturas de máquina.</td><td class="no-split"><i>Unique Opens</i> / <i>Unique Sends</i></td></tr>
<tr><td class="no-split"><i>Unique Click Rate</i></td><td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Clicks' %}</td><td class="no-split"><i>Unique Clicks</i> / <i>Unique Sends</i></td></tr>
<tr><td class="no-split"><i>Unique Click to Open Rate</i></td><td class="no-split">El porcentaje de usuarios que hicieron clic en un correo electrónico después de abrirlo.</td><td class="no-split"><i>Unique Clicks</i> / <i>Unique Opens</i></td></tr>
</tbody></table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Métricas de correo electrónico" }

![Métricas de referencia de la industria de correo electrónico mostradas en gráficos de líneas y gráficos de barras.]({% image_buster /assets/img/dashboards/email_industry.png %})

{% endtab %}
{% tab Push %}

Las métricas push están disponibles para iOS, Android, Web y en todas las plataformas combinadas.

<table aria-label="Métricas push"><thead><tr><th>Métrica</th><th>Descripción</th><th>Fórmula</th></tr></thead><tbody>
<tr><td class="no-split"><i>Direct Open Rate</i></td><td class="no-split">{% multi_lang_include analytics/metrics.md metric='Direct Opens' %}</td><td class="no-split"><i>Direct Opens</i> / <i>Unique Sends</i></td></tr>
<tr><td class="no-split"><i>Influenced Open Rate</i></td><td class="no-split">{% multi_lang_include analytics/metrics.md metric='Influenced Opens' %}</td><td class="no-split"><i>Influenced Opens</i> / <i>Unique Sends</i></td></tr>
<tr><td class="no-split"><i>Total Open Rate</i></td><td class="no-split">{% multi_lang_include analytics/metrics.md metric='Opens' %}</td><td class="no-split">(<i>Direct Opens</i> + <i>Influenced Opens</i>) / <i>Unique Sends</i></td></tr>
</tbody></table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Métricas push" }

![Métricas de referencia de la industria push mostradas en gráficos de líneas y gráficos de barras.]({% image_buster /assets/img/dashboards/push_industry.png %})

{% endtab %}
{% tab servicio de mensajes cortos %}

<table aria-label="Métricas de servicio de mensajes cortos"><thead><tr><th>Métrica</th><th>Descripción</th><th>Fórmula</th></tr></thead><tbody>
<tr><td class="no-split"><i>Delivery Rate</i></td><td class="no-split">{% multi_lang_include analytics/metrics.md metric='Deliveries' %}</td><td class="no-split"><i>Deliveries</i> / <i>Unique Sends</i></td></tr>
<tr><td class="no-split"><i>Short Link Click Rate</i></td><td class="no-split">El porcentaje de usuarios que hicieron clic en un enlace corto después de recibir un servicio de mensajes cortos.</td><td class="no-split"><i>Short Link Clicks</i> / <i>Unique Sends</i></td></tr>
</tbody></table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Métricas de servicio de mensajes cortos" }

![Métricas de referencia de la industria de SMS mostradas en gráficos de líneas y gráficos de barras.]({% image_buster /assets/img/dashboards/sms_industry.png %})

{% endtab %}
{% tab Content Cards %}

<table aria-label="Métricas de Content Cards"><thead><tr><th>Métrica</th><th>Descripción</th><th>Fórmula</th></tr></thead><tbody>
<tr><td class="no-split"><i>Click Rate</i></td><td class="no-split">El porcentaje de usuarios que recibieron una Content Card e hicieron clic en un enlace.</td><td class="no-split"><i>Unique Clicks</i> / <i>Unique Impressions</i></td></tr>
</tbody></table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Métricas de Content Cards" }

![Métricas de referencia de la industria de Content Cards mostradas en gráficos de líneas y gráficos de barras.]({% image_buster /assets/img/dashboards/content_card_industry.png %})

{% endtab %}
{% endtabs %}

## Metodología {#methodology}

Los benchmarks de Braze se calculan mediante un proceso de tres pasos diseñado para producir cifras estables y representativas.

### Paso 1: Muestreo dinámico {#step-1-dynamic-sampling}

En lugar de analizar cada punto de datos, Braze selecciona una muestra representativa. El método de muestreo sobremuestrea los grupos de usuarios más pequeños para garantizar una representación adecuada y se ajusta según el tamaño de la empresa, de modo que un número reducido de empresas muy grandes no distorsione los resultados de toda una industria.

### Paso 2: Eliminación de valores atípicos {#step-2-outlier-removal}

Braze identifica y elimina los valores atípicos estadísticos. Esto reduce significativamente la volatilidad en los datos con un impacto mínimo en las tasas de rendimiento promedio, lo que significa que las anomalías se eliminan sin alterar las tendencias subyacentes.

### Paso 3: Ponderación por poststratificación {#step-3-post-stratification-weighting}

La muestra se pondera para reflejar la población del mundo real. Se aplican pesos a los subgrupos para corregir cualquier desequilibrio residual del muestreo, lo que da como resultado benchmarks finales que son representativos e imparciales.

## Gobernanza de datos {#data-governance}

- **Ciclo de actualización:** Los datos se actualizan mensualmente el día 5 de cada mes y están vigentes hasta el último mes completado.
- **Privacidad:** Todos los benchmarks se agregan y se desidentifican para proteger la información del usuario.