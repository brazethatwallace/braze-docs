---
nav_title: Análisis de Canvas
article_title: Análisis de Canvas
page_order: 2
page_type: reference
description: "Este artículo de referencia describe los diversos análisis e informes que puedes aprovechar para comprender el rendimiento de tu Canvas."
tool:
  - Canvas
  - Reports

---

# Análisis de Canvas {#canvas-analytics}

> Necesitas saber si lo que estás construyendo está generando resultados. Con los análisis de Canvas, puedes obtener una imagen completa para entender cómo las experiencias que estás creando impactan en tus objetivos.

Una vez que hayas creado tu Canvas y lo hayas puesto en vivo, navega a la página **Canvas** y selecciona tu Canvas para abrir la página de detalles. Aquí puedes medir y probar el rendimiento de tu Canvas.

## Resumen de Canvas {#canvas-overview}

La parte superior de la página **Canvas Details** contiene las estadísticas principales del Canvas. Estas incluyen el número de mensajes enviados dentro del Canvas, el número total de veces que los clientes han entrado al Canvas, cuántos han convertido y tu tasa total, los ingresos generados por el Canvas y la audiencia total estimada.

Este es un excelente lugar para obtener un resumen de alto nivel y verificar cómo está funcionando tu Canvas en relación con tu objetivo.

### Usuarios alcanzables y estadísticas exactas {#reachable-users-and-exact-statistics}

Cuando **[Calcular estadísticas exactas]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment/#single-user-segments)** se está ejecutando para las audiencias vinculadas a tu Canvas, Braze puede mostrar brevemente una estimación redondeada en el área de **Usuarios alcanzables**. El total exacto reemplaza la estimación cuando el cálculo finaliza. Selecciona **Show Additional Stats** para ver un desglose completo por canal. El constructor de Canvas documenta el mismo flujo en **Población objetivo**; consulta [Cálculo de la población objetivo]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/#calculating-target-population).

![La página Canvas Details mostrando estadísticas principales que incluyen mensajes enviados, tasa de conversión, entradas totales, ingresos totales, salidas totales y audiencia estimada, con filtros de canal y estadísticas.]({% image_buster /assets/img_archive/Journey_5.png %})

### Cambios desde la última visualización {#changes-since-last-viewed}

El número de actualizaciones al Canvas realizadas por otros miembros de tu equipo se registra mediante la métrica *Cambios desde la última visualización* en la página de resumen del Canvas. Selecciona **Changes Since Last Viewed** para ver un registro de cambios de las actualizaciones al nombre del Canvas, planificación, etiquetas, mensaje, audiencia, estado de aprobación o configuración de acceso del equipo. Para cada actualización, puedes ver quién realizó la actualización y cuándo. Puedes usar este registro de cambios para auditar los cambios en tus Canvas.

## Visualización del rendimiento {#performance-visualization}

A medida que avanzas en la página **Canvas Details**, puedes ver el rendimiento de cada componente, como cuántos usuarios entraron, procedieron al siguiente paso o salieron del Canvas. Selecciona un paso o componente específico de Canvas para enfocar el panel en esa parte del recorrido y revisar sus métricas con más detalle.

{% alert note %}
Para Canvas Flow, un usuario saldrá del Canvas después de entrar y recibir la carga útil del mensaje en el último paso del recorrido del usuario.
{% endalert %}

Las métricas también incluyen impresiones, destinatarios únicos, recuento de conversiones e ingresos generados. Puedes hacer clic en un componente para desglosar aún más tus datos y ver el rendimiento específico por canal.

![Dos ejemplos de detalles de rendimiento para componentes de Canvas. A la izquierda se muestran los detalles de rendimiento de una ruta de usuario con un componente de Canvas. A la derecha se muestran los detalles de rendimiento de un componente de Canvas expandido y un paso anidado que muestra el recuento de impresiones del mensaje dentro de la aplicación.]({% image_buster /assets/img_archive/Journey_6.png %})

## Desglose de rendimiento por variante {#performance-breakdown-by-variant}

En la parte inferior de la página **Canvas Details**, haz clic en **Analyze Variants** para abrir el modal **Analyze Canvas**. Este modal contiene tres pestañas:

- Analyze Variants
- Canvas Funnel Report
- Canvas Retention Report

### Analyze Variants {#analyze-variants}

En la pestaña **Analyze Variants**, puedes ver un desglose del rendimiento por variante y grupo de control, si tienes más de uno. También puedes copiar el identificador de API del Canvas, descargar un archivo CSV de las métricas y copiar las celdas. La pestaña **Analyze Variants** contiene una tabla que te muestra un desglose de cada variante en varios niveles.

Puedes inferir rápidamente las variantes efectivas e identificar las cadencias, contenidos, desencadenantes, tiempos y más adecuados.

![El modal Analyze Canvas con la pestaña Analyze Variants seleccionada, mostrando una tabla comparativa para Path 1 y Path 2 con entradas, envíos, ingresos, tasas de conversión, porcentaje de cambio y métricas de confianza.]({% image_buster /assets/img_archive/analyze_variants.png %})

Las métricas básicas incluyen las siguientes:

- **Variant API Identifier:** El identificador de API de tu variante, que puedes usar en tus llamadas a la API.
- **Total Entries:** El número total de usuarios que han entrado en la variante en Canvas.
- **Total Sends:** El número total de mensajes enviados en la variante en Canvas.
- **Total Steps:** El número total de pasos en la variante en Canvas.
- **Total Revenue:** Los ingresos totales en dólares de los destinatarios del Canvas dentro de la ventana de conversión primaria establecida. *Total Revenue* es la suma de las compras atribuidas a los usuarios que recibieron esa variante durante esa ventana. Las compras aún cuentan para *Total Revenue* incluso cuando el usuario no realiza el evento de conversión primaria configurado, siempre que la compra se encuentre dentro de las reglas de atribución de la ventana.

{% alert note %}
Al igual que las conversiones, los ingresos se registran técnicamente a nivel de Canvas, pero se atribuyen al componente más reciente y a la variante más reciente de la cual el usuario ha recibido un mensaje (o en la que entró, si aún no ha recibido un mensaje).<br><br>
Por ejemplo, si un usuario completa dos pasos y luego realiza una compra, esos ingresos se atribuyen al segundo componente y a la variante en la que entró. Si entra al Canvas pero realiza una compra antes de recibir el primer componente del Canvas, esos ingresos se atribuyen a la variante en la que entró, pero no a ningún componente.
{% endalert %}

Más allá de eso, puedes ver un desglose más explícito de los [eventos de conversión]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events/), incluyendo lo siguiente:

- Totales de conversión y tasas de conversión para cada evento de conversión
- Incremento respecto a la variante de control
- Confianza estadística para cada evento de conversión

### Cómo se registran las conversiones {#how-conversions-are-tracked}

Un usuario solo puede convertir una vez por evento de conversión por entrada al Canvas. Las conversiones se asignan al mensaje más reciente recibido por el usuario para esa entrada. El resumen del Canvas refleja todas las conversiones realizadas por los usuarios en esa ruta, independientemente de si recibieron un mensaje o no. Cada paso posterior solo mostrará las conversiones que ocurrieron mientras ese era el paso más reciente que el usuario recibió.

Considera el siguiente ejemplo: un Canvas tiene 10 notificaciones push y el evento de conversión es "Abre la aplicación" (o "Inicio de sesión").
- El usuario A abre la aplicación después de entrar pero antes de recibir el primer mensaje.
- El usuario B abre la aplicación después de cada notificación push.

El resumen del Canvas mostrará dos conversiones, mientras que los pasos individuales mostrarán una conversión en el primer paso y ninguna en todos los pasos posteriores. Si las horas tranquilas están activas cuando ocurre el evento de conversión, se aplicarán las mismas reglas.

Ahora, supongamos que tenemos un Canvas con horas tranquilas y ocurren los siguientes eventos:

1. El usuario A entra en un Canvas.
2. El primer paso es un paso de retraso dentro de las horas tranquilas establecidas, por lo que el mensaje se suprime.
3. El usuario A realiza el evento de conversión.

El usuario A contará como convertido en la variante general del Canvas, pero no en el paso, ya que no recibió el paso.

Para nuestro último ejemplo, supongamos que tenemos un Canvas con la reelegibilidad activada. Si un usuario reelegible realiza el evento de conversión en la primera entrada y en la segunda entrada, se contarán dos conversiones.

### Informe de embudo {#funnel-report}

El informe de embudo ofrece un informe visual que te permite analizar los recorridos que tus clientes realizan después de recibir un Canvas. Si tu Canvas utiliza un grupo de control o múltiples variantes, podrás comprender cómo las diferentes variantes han impactado el embudo de conversión a un nivel más granular y optimizar en función de estos datos. Para más información sobre los informes de embudo, consulta [Informes de embudo]({{site.baseurl}}/user_guide/analytics/reports/funnel_reports/).

### Informe de retención {#retention-report}

La retención de usuarios es una de las métricas más importantes para cualquier especialista en marketing. Mantener a los usuarios comprometidos regresando por más indica que el negocio está saludable. Braze ahora te permite medir la retención de usuarios directamente en la página **Canvas Analytics**. Para más información sobre cómo leer e interpretar tu informe de retención, consulta [Informes de retención]({{site.baseurl}}/user_guide/analytics/reports/retention_reports/).