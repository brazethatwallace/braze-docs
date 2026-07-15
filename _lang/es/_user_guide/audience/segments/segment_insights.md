---
nav_title: Información del segmento
article_title: Información del segmento
page_order: 6
page_type: tutorial
tool:
  - Segments
  - Reports
description: "Este artículo te guiará sobre cómo usar, interpretar y compartir la información del segmento."
---

# [![Curso de Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/segmentation-course){: style="float:right;width:120px;border:0;" class="noimgborder"}Información del segmento {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomsegmentation-course-stylefloatrightwidth120pxborder0-classnoimgbordersegment-insights}

> Aprende a usar, interpretar y compartir la información del segmento.

La información del segmento te muestra cómo se desempeña un segmento en comparación con otro a través de un conjunto de KPI preseleccionados.

## Ver la información del segmento {#viewing-segment-insights}

Ve a la página **Información del segmento** de tu dashboard, en **Analytics**, y visualiza hasta 10 segmentos diferentes comparados con una línea base.

![Dashboard de información del segmento que compara tres segmentos, "UK Users", "FR Users" y "CA Users" con un segmento de línea base, "Todos los usuarios".]({% image_buster /assets/img_archive/segment_insights.png %})

El segmento de línea base puede ser un segmento específico que selecciones o un segmento que contenga a todos tus usuarios. Puedes comparar las siguientes estadísticas usando la información del segmento:

| Medida | Descripción | Fórmula |
| --------------------- | ------------- | ------------- |
| Sesiones por día | Número promedio de sesiones diarias de los usuarios del segmento | (n.º total de sesiones) / (n.º de días desde la primera sesión) |
| Días desde la primera sesión | Número promedio de días entre la primera sesión de los usuarios del segmento y ahora | hoy – fecha de la primera sesión |
| Días desde la última sesión | Número promedio de días entre la última sesión de los usuarios del segmento y ahora | hoy – fecha de la última sesión |
| Ingresos de por vida en dólares | Ingresos promedio de por vida en dólares para los usuarios del segmento | gasto de por vida del usuario |
| Días desde la primera compra | Número promedio de días entre la primera sesión y la primera compra de los usuarios del segmento | fecha de la primera compra – fecha de la primera sesión |
| Días desde la última compra | Número promedio de días entre la última compra de los usuarios del segmento y ahora | hoy – fecha de la última compra |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Ver la información del segmento" }

Puedes compartir fácilmente comparaciones específicas con tus compañeros de equipo usando la URL única de la página, y también puedes seleccionar el icono del ojo junto a cada segmento para ver más información sobre ese segmento. Estas comparaciones se restablecerán cuando cambies entre espacios de trabajo.

![Detalles del segmento "Premium Users (iOS VideoApp)" con un gráfico que muestra la membresía histórica y un cuadro que desglosa el tamaño estimado para varios canales de mensajería.]({% image_buster /assets/img_archive/Segment_Insights_Info.png %}){: style="max-width:50%;"}

## Página de detalles del segmento {#segment-details-page}

La información del segmento también se ha integrado directamente en la vista **Detalles del segmento**. Al consultar un segmento en particular que hayas configurado previamente, puedes encontrar las mismas seis estadísticas descritas dentro del cuadro dinámico y gris de estadísticas del segmento. Desde aquí, puedes lanzar rápidamente la herramienta de información del segmento para comparar este segmento en particular con cualquier otro que hayas configurado previamente, pero ten en cuenta que esto sobrescribirá cualquier segmento que hayas seleccionado anteriormente dentro de la herramienta de información del segmento.

![La información del segmento también se ha integrado directamente en la vista Detalles del segmento. Al consultar un segmento en particular que hayas configurado previamente, puedes encontrar las mismas seis estadísticas descritas dentro del cuadro dinámico y gris de estadísticas del segmento. Desde aquí, puedes lanzar rápidamente la herramienta de información del segmento para comparar este segmento en particular con cualquier otro que hayas configurado previamente, pero ten en cuenta que esto sobrescribirá cualquier segmento que hayas seleccionado anteriormente dentro de la herramienta de información del segmento.]({% image_buster /assets/img_archive/Segment_Segment_Insights.png %})

## Casos de uso {#insights-use-cases}

### Comparar patrones de uso demográfico y de compra {#comparing-demographic-usage-and-purchasing-patterns}

Uno de los mejores usos de la información del segmento es responder preguntas sobre el impacto de la demografía de los usuarios en el uso de la aplicación y la efectividad de las campañas, como:

- ¿Ciertos grupos demográficos de usuarios se desempeñan significativamente mejor o peor que el promedio?
- ¿Debería replantear la localización de una campaña en particular?
- ¿Una campaña está captando la atención de un grupo demográfico en particular?
- ¿Qué objetivos debería establecer para una campaña dirigida a un grupo demográfico en particular?

La información del segmento puede ayudar a descubrir diferencias entre los grupos demográficos de usuarios. El siguiente ejemplo muestra una comparación de la base de usuarios de una aplicación por idioma, ilustrando cómo los hablantes de inglés tienden a tener un LTV y niveles de actividad más altos que los hablantes de otros idiomas.

![Desglose de información del segmento para segmentos de inglés, alemán, francés y español.]({% image_buster /assets/img_archive/Segment_Language_Insights.png %})

En este ejemplo, los hablantes de alemán se registraron hace más tiempo en promedio, lo que podría explicar por qué ya no son tan activos. Esto podría deberse a una multitud de factores. Por ejemplo, si la aplicación se lanzó primero en Europa pero ahora es más popular en EE. UU., donde la mayoría de las personas hablan inglés o español. Para obtener hallazgos más sólidos al analizar KPI entre grupos demográficos, es sensato probar los hallazgos de un estudio general de demografía (por ejemplo, si el idioma impacta el LTV en todos los usuarios) observando una población más pequeña y similar para ver si los hallazgos persisten.

Para mejorar las conversiones entre hablantes de idiomas distintos al inglés, un buen primer paso sería [localizar las campañas]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization) al idioma del dispositivo del usuario y asegurarse de que el texto de esos mensajes esté captando a los usuarios mediante una [campaña multivariante]({{site.baseurl}}/user_guide/messaging/ab_testing#creating-tests) para probar diferentes versiones del texto en el idioma extranjero.

### Comprender los indicadores de mayores ingresos {#understanding-indicators-of-higher-revenue}

Lograr que los usuarios se conviertan en compradores puede ser difícil, e intentar empujar a usuarios nuevos, inactivos o desinteresados directamente hacia la compra puede llevar al usuario a desinstalar tu aplicación. La información del segmento puede ayudarte a descubrir acciones que llevan a los usuarios más adelante en el embudo de compra sin requerir que compren de inmediato, por ejemplo, suscribirse a tu boletín, compartir en redes sociales o registrarse para mensajes promocionales. Por ejemplo, puedes trazar el impacto en las compras de diferentes comportamientos dentro de una aplicación de comercio electrónico.

![Desglose de información del segmento para usuarios que compartieron en redes sociales, se registraron para promociones y se suscribieron al boletín.]({% image_buster /assets/img_archive/Segment_Insights_Events1.png %})

En este caso, relativamente pocos usuarios están actualmente registrados para mensajes promocionales y no son tan activos, pero estos usuarios generan mayores ingresos de por vida. Para aumentar los ingresos, podría ser una buena idea incluir una invitación para registrarse en mensajes promocionales en las campañas de incorporación. Para volver a captar a los usuarios inactivos, un buen plan sería enviar una [campaña típica para usuarios inactivos]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/capturing_lapsing_users#capture-lapsing-users) y dirigirse a los [usuarios que convirtieron]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/retargeting_campaigns#converted-from-campaign-filter) con una campaña posterior para registrarse en mensajes promocionales.