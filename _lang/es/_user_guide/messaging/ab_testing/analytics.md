---
nav_title: Análisis
article_title: Análisis de pruebas A/B
page_order: 10
page_type: reference
description: "Este artículo explica cómo ver e interpretar los resultados de una campaña multivariante o A/B."
---

# Análisis de pruebas multivariantes y A/B {#multivariate-and-ab-test-analytics}

> Este artículo explica cómo ver los resultados de una prueba multivariante o A/B. Si aún no has configurado tu prueba, consulta [Crear pruebas multivariantes y A/B]({{site.baseurl}}/user_guide/messaging/ab_testing/create_tests) para ver los pasos.

Después de que tu campaña se haya lanzado, puedes comprobar el rendimiento de cada variante seleccionando tu campaña en la sección **Campaigns** del dashboard.

## Análisis por opción de optimización {#analytics-by-optimization-option}

Tu vista de análisis variará dependiendo de si seleccionaste una [optimización]({{site.baseurl}}/user_guide/messaging/ab_testing/optimizations) durante la configuración inicial.

### Sin optimización {#no-optimization}

Si seleccionaste **Sin optimización** al configurar tu campaña, tu vista de análisis permanecerá igual. La página **Análisis de campañas** de tu campaña mostrará el rendimiento de tus variantes en comparación con tu grupo de control, si incluiste uno.

![Sección de rendimiento del análisis de campaña para una campaña de correo electrónico con múltiples variantes. La tabla enumera varias métricas de rendimiento para cada variante, como destinatarios, rebotes, clics y conversiones.]({% image_buster /assets/img_archive/ab_analytics_no_optimization.png %})

Para más detalles, consulta el artículo [Análisis de campañas]({{site.baseurl}}/user_guide/analytics/reports/campaign_analytics) para tu canal de mensajería.

### Selección de variante con BrazeAI<sup>TM</sup> (solo push) {#brazeai-variant-selection-push-only}

Si usas la selección de variante con BrazeAI<sup>TM</sup>, dependiendo de si se trata de un envío único o una campaña recurrente, una vez que la ventana del experimento (o el primer período para recurrentes) haya pasado, verás el incremento, si lo hay, en la página de inicio de la campaña. También verás más detalles similares a los de la variante ganadora a continuación si ejecutas una campaña de envío único.

Para más detalles sobre cómo reportamos el incremento en la selección de variante con BrazeAI<sup>TM</sup>, consulta [Selección de variante]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/variant_selection).

![Análisis de campaña que muestra el incremento de la selección de variante con BrazeAI<sup>TM</sup>, incluyendo métricas de comparación después de la ventana del experimento.]({% image_buster /assets/img_archive/braze_ai_variant_selection_reporting.png %})

### Variante ganadora {#winning-variant}

Si seleccionaste **Variante ganadora** como optimización al configurar tu campaña, tienes acceso a una pestaña adicional en el análisis de tu campaña llamada **Resultado de la prueba A/B**. Después de que la variante ganadora se envíe a los usuarios restantes de tu prueba, esta pestaña muestra los resultados de ese envío.

El **Resultado de la prueba A/B** se divide en dos pestañas: **Prueba inicial** y **Variante ganadora**.

{% tabs local %}
{% tab Prueba inicial %}

La pestaña **Prueba inicial** muestra las métricas de cada variante de la prueba A/B inicial enviada a una parte de tu segmento objetivo. Puedes ver un resumen de cómo se desempeñaron todas las variantes y si hubo o no una ganadora durante la prueba.

Si una variante superó a todas las demás con más del 95 % de [confianza]({{site.baseurl}}/user_guide/messaging/ab_testing/analytics#understanding-confidence), Braze marca esa variante con la etiqueta "Ganadora".

Si ninguna variante supera a todas las demás con un 95 % de confianza y elegiste enviar la variante con mejor rendimiento de todos modos, la variante con mejor rendimiento se enviará igualmente y se indicará con la etiqueta "Ganadora".

![Resultados de una prueba inicial enviada para determinar la variante ganadora donde ninguna variante tuvo un rendimiento mejor que las demás con suficiente confianza para alcanzar el umbral del 95 por ciento de confianza para significancia estadística.]({% image_buster /assets/img_archive/ab_analytics_wv_insufficient_confidence.png %})

#### Cómo se selecciona la variante ganadora {#how-the-winning-variant-is-selected}

Braze compara todas las variantes entre sí con [pruebas chi-cuadrado de Pearson](https://en.wikipedia.org/wiki/Pearson%27s_chi-squared_test). Esto mide si una variante supera estadísticamente a todas las demás con un nivel de significancia de p < 0,05, o lo que denominamos significancia del 95 %. Si es así, la variante ganadora se indica con la etiqueta "Ganadora".

Esta es una prueba separada de la puntuación de confianza, que solo describe el rendimiento de una variante en comparación con el grupo de control con un valor numérico entre 0 y 100 %.

Una variante puede tener mejor rendimiento que el grupo de control, pero la prueba chi-cuadrado verifica si una variante es mejor que todas las demás. Las [pruebas de seguimiento](#recommended-follow-ups) pueden proporcionar más detalles.

{% endtab %}
{% tab Variante ganadora %}

La pestaña **Variante ganadora** muestra los resultados del segundo envío, donde cada usuario restante recibió la variante con mejor rendimiento de la prueba inicial. Tu **% de audiencia** sumará el porcentaje del segmento objetivo que reservaste para el grupo de la variante ganadora.

![Resultados de la variante ganadora enviada al grupo de la variante ganadora.]({% image_buster /assets/img_archive/ab_analytics_wv_1.png %})

{% endtab %}
{% endtabs %}

Si quieres ver el rendimiento de la variante ganadora a lo largo de toda la campaña, incluyendo los envíos de la prueba A/B, consulta la página **Análisis de campañas**.

### Variante personalizada {#personalized-variant}

Si seleccionaste **Variante personalizada** como optimización al configurar tu campaña, el **Resultado de la prueba A/B** se divide en dos pestañas: **Prueba inicial** y **Variante personalizada**.

{% tabs local %}
{% tab Prueba inicial %}

La pestaña **Prueba inicial** muestra las métricas de cada variante de la prueba A/B inicial enviada a una parte de tu segmento objetivo.

![Resultados de una prueba inicial enviada para determinar la variante con mejor rendimiento para cada usuario. Una tabla muestra el rendimiento de cada variante basándose en varias métricas para el canal objetivo.]({% image_buster /assets/img_archive/ab_analytics_pv_initial_test_1.png %})

De forma predeterminada, la prueba busca asociaciones entre los eventos personalizados de cada usuario y sus preferencias de variante de mensaje. Este análisis detecta si los eventos personalizados aumentan o disminuyen la probabilidad de responder a una variante de mensaje en particular. Estas relaciones se utilizan luego para determinar qué usuarios reciben qué variante de mensaje en el envío final.

Las relaciones entre eventos personalizados y preferencias de mensaje se muestran en la tabla de la pestaña **Envío inicial**.

![Tablas de datos de eventos personalizados para la variante 1 y la variante 2 que muestran las puntuaciones de impacto de los eventos personalizados e indican cómo cada evento influye en la preferencia de variante.]({% image_buster /assets/img_archive/ab_analytics_pv_3.png %})

Si la prueba no puede encontrar una relación significativa entre los eventos personalizados y las preferencias de ruta, recurre a un método de análisis basado en sesiones, y no se muestran tablas de datos de eventos personalizados.

{% details Método de análisis alternativo %}

**Método de análisis basado en sesiones**<br>
Si se utiliza el método alternativo para determinar las variantes personalizadas, la pestaña **Prueba inicial** muestra un desglose de las variantes preferidas de los usuarios basándose en una combinación de ciertas características.

Estas características son:

- **Recencia:** Cuándo tuvieron su última sesión
- **Frecuencia:** Con qué frecuencia tienen sesiones
- **Antigüedad:** Cuánto tiempo llevan siendo usuarios

Por ejemplo, la prueba puede encontrar que la mayoría de los usuarios prefieren la variante A, pero los usuarios que tuvieron una sesión hace aproximadamente 3-12 días, tienen entre 1-12 días entre sesiones y fueron creados en los últimos 67-577 días tienden a preferir la variante B. Por lo tanto, los usuarios en esa subpoblación recibieron la variante B en el segundo envío, mientras que el resto recibió la variante A.

![La tabla de características de usuario, que muestra qué usuarios se predice que preferirán la variante A y la variante B basándose en los tres contenedores en los que se encuentran para recencia, frecuencia y antigüedad.]({% image_buster /assets/img_archive/ab_analytics_pv_initial_test_2.png %})

**Cómo se seleccionan las variantes personalizadas**<br>
Con este método, el mensaje recomendado para un usuario individual es la suma de los efectos de su recencia, frecuencia y antigüedad específicas. La recencia, la frecuencia y la antigüedad se dividen en contenedores, como se ilustra en la tabla de **Características de usuario**. El rango de tiempo de cada contenedor se determina por los datos de los usuarios en cada campaña individual y cambiará de una campaña a otra.

Cada contenedor puede tener una contribución o "impulso" diferente hacia cada variante de mensaje. La fuerza del impulso para cada contenedor se determina a partir de las respuestas de los usuarios en el envío inicial utilizando [regresión logística](https://en.wikipedia.org/wiki/Logistic_regression). Esta tabla solo resume los resultados mostrando con qué variante tendieron a interactuar los usuarios en cada contenedor. La variante personalizada real de cualquier usuario individual depende de la suma de los efectos de los tres contenedores en los que se encuentra, uno para cada característica.

{% enddetails %}

{% endtab %}
{% tab Variante personalizada %}

La pestaña **Variante personalizada** muestra los resultados del segundo envío, donde cada usuario restante recibió la variante con la que era más probable que interactuara.

Las tres tarjetas en esta página muestran tu incremento proyectado, los resultados generales y los resultados proyectados si hubieras enviado solo la variante ganadora en su lugar. Incluso si no hay incremento, lo cual puede suceder a veces, el resultado es el mismo que enviar solo la variante ganadora (una prueba A/B tradicional).

- **Incremento proyectado:** La mejora en tu métrica de optimización seleccionada para este envío debido al uso de variantes personalizadas en lugar de una prueba A/B estándar (si los usuarios restantes solo hubieran recibido la variante ganadora).
- **Resultados generales:** Los resultados del segundo envío basados en tu métrica de optimización elegida (*Aperturas únicas*, *Clics únicos* o *Evento de conversión primaria*).
- **Resultados proyectados:** Los resultados proyectados del segundo envío basados en tu métrica de optimización elegida si hubieras enviado solo la variante ganadora en su lugar.

![Pestaña de variante personalizada para una campaña optimizada para aperturas únicas. Las tarjetas muestran el incremento proyectado, las aperturas únicas generales (con variante personalizada) y las aperturas únicas proyectadas (con variante ganadora).]({% image_buster /assets/img_archive/ab_analytics_pv_1.png %})

La tabla en esta página muestra las métricas de cada variante del envío de la variante personalizada. Tu **% de audiencia** suma el porcentaje del segmento objetivo que reservaste para el grupo de la variante personalizada.

![Tabla de resultados del envío de variante personalizada que muestra las métricas de rendimiento para la variante A, la variante B y todas las variaciones, incluyendo porcentaje de audiencia, envíos, entregas, aperturas, clics y conversiones.]({% image_buster /assets/img_archive/ab_analytics_pv_2.png %})

{% endtab %}
{% endtabs %}

## Entender la confianza {#understanding-confidence}

La confianza es la medida estadística de cuán seguros estamos de que una diferencia en los datos, como las tasas de conversión, es real y no se debe simplemente al azar.

{% alert note %}
¿No ves la confianza en tus resultados? La confianza solo aparecerá si tienes un grupo de control.
{% endalert %}

Una parte importante de tus resultados es la confianza de los mismos. Por ejemplo, ¿qué pasa si el grupo de control tuvo una tasa de conversión del 20 % y la variante A tuvo una tasa de conversión del 25 %? Esto parece indicar que enviar la variante A es más efectivo que no enviar ningún mensaje. Tener una confianza del 95 % significa que la diferencia entre las dos tasas de conversión probablemente se debe a una diferencia real en las respuestas de los usuarios y que solo hay un 5 % de probabilidad de que la diferencia haya ocurrido por azar.

Braze compara la tasa de conversión de cada variante con la tasa de conversión del grupo de control mediante un procedimiento estadístico llamado [prueba&nbsp;Z](https://en.wikipedia.org/wiki/Z-test). Un resultado con un 95 % o más de confianza, como en el ejemplo anterior, indica que la diferencia es estadísticamente significativa. Esto aplica en cualquier lugar donde veas una métrica de confianza en el dashboard de Braze que describa la diferencia entre dos mensajes o poblaciones de usuarios.

En general, se necesita una confianza de al menos el 95 % para demostrar que tus resultados reflejan las preferencias reales de los usuarios y no se deben al azar. En pruebas científicas rigurosas, el 95 % de confianza (o lo que comúnmente se denomina que el valor "p" sea menor que 0,05) es el punto de referencia común utilizado para determinar la significancia estadística. Si continuamente no logras alcanzar el 95 % de confianza, intenta aumentar el tamaño de tu muestra o reducir el número de variantes.

La confianza refleja cuán probable es que una diferencia observada entre las tasas de conversión de la variante y del grupo de control sea real y no se deba al azar. Es una función del tamaño de la muestra y la magnitud de la diferencia entre las tasas de conversión. Que las tasas de conversión generales sean altas o bajas normalmente es menos importante que la diferencia observada y el tamaño de la muestra para determinar la fuerza de la medida de confianza. Es posible que una variante tenga una tasa de conversión muy diferente a otra y aun así no tenga un 95 % o más de confianza. También es posible que dos conjuntos de variantes tengan tasas de conversión o de incremento similares y, sin embargo, diferente confianza.

A medida que llegan más datos, la confianza puede disminuir si las tasas de conversión de la variante y del grupo de control se acercan entre sí: la diferencia que estás midiendo se hace más pequeña, lo que puede superar el efecto de un tamaño de muestra mayor.

### Resultados estadísticamente no significativos {#statistically-insignificant-results}

Una prueba que no tiene un 95 % de confianza aún puede contener información importante. Aquí hay algunas cosas que puedes aprender de una prueba con resultados estadísticamente no significativos:

- Es posible que todas tus variantes hayan tenido aproximadamente el mismo efecto. Saber esto te ahorra el tiempo que habrías dedicado a hacer estos cambios. A veces, puedes descubrir que las tácticas de marketing convencionales, como repetir tu llamada a la acción, no necesariamente funcionan para tu audiencia.
- Aunque tus resultados pueden haberse debido al azar, pueden orientar la hipótesis para tu próxima prueba. Si múltiples variantes parecen tener resultados aproximadamente iguales, ejecuta algunas de ellas nuevamente junto con nuevas variantes para ver si puedes encontrar una alternativa más efectiva. Si una variante tiene mejor rendimiento, pero no por una cantidad significativa, puedes realizar otra prueba en la que la diferencia de esta variante sea más exagerada.
- ¡Sigue probando! Una prueba con resultados no significativos debería llevar a ciertas preguntas. ¿Realmente no hubo diferencia entre tus variantes? ¿Deberías haber estructurado tu prueba de manera diferente? Puedes responder estas preguntas ejecutando pruebas de seguimiento.
- Aunque las pruebas son útiles para descubrir qué tipo de mensajería genera más respuesta de tu audiencia, también es importante entender qué alteraciones en la mensajería tienen solo un efecto insignificante. Esto te permite seguir probando en busca de otra alternativa más efectiva, o ahorrar el tiempo que se habría dedicado a decidir entre dos mensajes alternativos.

Ya sea que tu prueba tenga un ganador claro o no, puede ser útil ejecutar una [prueba de seguimiento](#recommended-follow-ups) para confirmar tus resultados o aplicar tus hallazgos a un escenario ligeramente diferente.

## Discrepancias entre el grupo de control y la variante {#discrepancies-between-the-control-group-and-variant}

En campañas de mensajes dentro de la aplicación con divisiones A/B o multivariantes, los porcentajes que configuras son objetivos de asignación. Las impresiones reportadas rara vez coinciden exactamente con esos porcentajes, porque solo los usuarios que realizan la acción desencadenante registran impresiones, y los usuarios del grupo de control que desencadenan la acción registran una impresión aunque nunca vean un mensaje.

Por ejemplo, supongamos que una campaña tiene una audiencia objetivo de 200 usuarios en el momento del lanzamiento, con 100 usuarios en el grupo de control y 100 usuarios en la variante.

Los 100 usuarios en la variante reciben la carga útil del mensaje dentro de la aplicación, y 50 de ellos realizan la acción desencadenante y ven el mensaje dentro de la aplicación. Los 100 usuarios en el grupo de control solo se rastrean si realizan la acción desencadenante de la campaña, y 75 de ellos realizan la acción desencadenante y registran una impresión pero no ven el mensaje dentro de la aplicación.

A pesar de la división inicial 50/50, las impresiones únicas registradas no están equilibradas. El grupo de la variante tiene 50 impresiones, mientras que el grupo de control tiene 75 impresiones.

### Retrasos en mensajes dentro de la aplicación {#in-app-message-delays}

Para campañas de mensajes dentro de la aplicación desencadenados que incluyen visualizaciones retrasadas, las impresiones del grupo de control se registrarán cuando el usuario final habría recibido originalmente el mensaje dentro de la aplicación. Por ejemplo, si una campaña está configurada para retrasar la visualización una hora, las impresiones del grupo de control no se registrarán hasta que haya pasado el retraso de una hora. Esto ayuda con el seguimiento preciso de las impresiones relacionadas con el momento previsto de la entrega del mensaje.

## Seguimientos recomendados {#recommended-follow-ups}

Una prueba multivariante y A/B puede (¡y debería!) inspirar ideas para futuras pruebas, así como guiarte hacia cambios en tu estrategia de mensajería. Las posibles acciones de seguimiento incluyen las siguientes:

### Cambiar tu estrategia de mensajería basándote en los resultados de la prueba {#change-your-messaging-strategy-based-on-test-results}

Tus resultados multivariantes pueden llevarte a cambiar la forma en que redactas o formateas tu mensajería.

### Cambiar la forma en que entiendes a tus usuarios {#change-the-way-you-understand-your-users}

Cada prueba arrojará luz sobre los comportamientos de tus usuarios, cómo responden a diferentes canales de mensajería y las diferencias (y similitudes) entre tus segmentos.

### Mejorar la forma en que estructuras futuras pruebas {#improve-the-way-you-structure-future-tests}

¿Tu tamaño de muestra fue demasiado pequeño? ¿Las diferencias entre tus variantes fueron demasiado sutiles? Cada prueba brinda una oportunidad para aprender cómo mejorar futuras pruebas. Si tu confianza es baja, tu tamaño de muestra es demasiado pequeño y debería ampliarse para futuras pruebas. Si no encuentras una diferencia clara entre el rendimiento de tus variantes, es posible que las diferencias fueran demasiado sutiles para tener un efecto perceptible en las respuestas de los usuarios.

### Ejecutar una prueba de seguimiento con un tamaño de muestra mayor {#run-a-follow-up-test-with-a-larger-sample-size}

Las muestras más grandes aumentarán las posibilidades de detectar pequeñas diferencias entre variantes.

### Ejecutar una prueba de seguimiento usando un canal de mensajería diferente {#run-a-follow-up-test-using-a-different-messaging-channel}

Si descubres que una estrategia particular es muy efectiva en un canal, es posible que quieras probar esa estrategia en otros canales. Si un tipo de mensaje es efectivo en un canal pero no en otro, puedes concluir que ciertos canales son más propicios para ciertos tipos de mensajes. O quizás hay una diferencia entre los usuarios que son más propensos a habilitar las notificaciones push y aquellos que son más propensos a prestar atención a los mensajes dentro de la aplicación. En última instancia, ejecutar este tipo de prueba te ayudará a aprender cómo tu audiencia interactúa con tus diferentes canales de comunicación.

### Ejecutar una prueba de seguimiento en un segmento diferente de usuarios {#run-a-follow-up-test-on-a-different-segment-of-users}

Para hacer esto, crea otra prueba con el mismo canal de mensajería y variantes, pero elige un segmento diferente de usuarios. Por ejemplo, si un tipo de mensajería fue extremadamente efectivo para usuarios activos, puede ser útil investigar su efecto en usuarios inactivos. Es posible que los usuarios inactivos respondan de manera similar, o que prefieran otra de las otras variantes. Esta prueba te ayudará a aprender más sobre tus diferentes segmentos y cómo responden a diferentes tipos de mensajes. ¿Por qué hacer suposiciones sobre tus segmentos cuando puedes basar tu estrategia en datos?

### Ejecutar una prueba de seguimiento basada en información de una prueba anterior {#run-a-follow-up-test-based-on-insights-from-a-previous-test}

Usa la información que recopilas de pruebas anteriores para guiar las futuras. ¿Una prueba anterior sugiere que una técnica de mensajería es más efectiva? ¿No estás seguro de qué aspecto específico de una variante la hizo mejor? Ejecutar pruebas de seguimiento basadas en estas preguntas te ayudará a generar hallazgos valiosos sobre tus usuarios.

### Comparar el impacto a largo plazo de diferentes variantes {#compare-the-long-term-impact-of-different-variants}

Si estás realizando pruebas A/B de mensajes de reactivación de la interacción, no olvides comparar el impacto a largo plazo de diferentes variantes usando [Informes de retención]({{site.baseurl}}/user_guide/analytics/reports/retention_reports). Puedes usar los informes de retención para analizar cómo cada variante impactó cualquier comportamiento de usuario de tu elección días, semanas o un mes después de la recepción del mensaje, y ver si hay incremento.