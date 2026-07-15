---
nav_title: Recorridos de experimentos
article_title: Recorridos de experimentos
alias: /experiment_step/
page_order: 4
page_type: reference
description: "Este artículo cubre los recorridos de experimentos, un componente que te permite probar múltiples rutas de Canvas entre sí y contra un grupo de control en cualquier punto del recorrido del usuario."
tool: Canvas
---

# Recorridos de experimentos {#experiment-paths}

> Los recorridos de experimentos te permiten probar múltiples rutas de Canvas entre sí y contra un grupo de control en cualquier punto del recorrido del usuario. Con este componente, puedes hacer seguimiento del rendimiento de las rutas para tomar decisiones informadas sobre tu recorrido en Canvas.

Cuando incluyes un paso de recorrido de experimentos en tu recorrido de usuario, este asignará aleatoriamente a los usuarios a diferentes rutas (o a un grupo de control opcional) que tú crees. Se asignarán porciones de la audiencia a diferentes rutas según los porcentajes que selecciones, lo que te permite probar diferentes mensajes o rutas entre sí y determinar cuál es más efectiva.

![Un paso de recorrido de experimentos que se divide en Ruta 1, Ruta 2 y Control.]({% image_buster /assets/img/experiment_step/experiment_step.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

## Requisitos previos {#prerequisites}

Para usar recorridos de experimentos, tu Canvas debe incluir eventos de conversión. Aunque no puedes añadir eventos de conversión después de que un Canvas se haya lanzado, puedes clonar el Canvas lanzado y añadir eventos de conversión para agregar recorridos de experimentos.

## Ejemplos {#use-cases}

Los recorridos de experimentos son ideales para probar la entrega, la cadencia, el texto del mensaje y las combinaciones de canales.

- **Entrega:** Compara los resultados entre mensajes enviados con diferentes [retrasos]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step) de tiempo, basados en acciones del usuario ([Rutas de Acción]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths)), y usando [sincronización inteligente]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing#step-1-add-intelligent-timing-1).<br><br>
- **Cadencia:** Prueba múltiples flujos de mensajería durante un período específico. Por ejemplo, podrías probar dos cadencias de incorporación diferentes:
    - Cadencia 1: Enviar 2 mensajes en las primeras 2 semanas del usuario
    - Cadencia 2: Enviar 3 mensajes en las primeras 2 semanas del usuario

    Cuando te diriges a usuarios inactivos, puedes probar la efectividad de enviar dos mensajes de recuperación en una semana frente a enviar solo uno.
- **Texto del mensaje:** Similar a una [prueba A/B]({{site.baseurl}}/user_guide/messaging/ab_testing) estándar, puedes probar diferentes textos de mensaje para ver qué redacción genera una tasa de conversión más alta.<br><br>
- **Combinaciones de canales:** Prueba la efectividad de diferentes combinaciones de canales de mensaje. Por ejemplo, puedes comparar el impacto de usar solo un correo electrónico frente a un correo electrónico combinado con push.

## Crear un recorrido de experimentos {#creating-an-experiment-path}

Para crear un componente de recorridos de experimentos, primero añade un paso a tu Canvas. Arrastra y suelta el componente desde la barra lateral, o haz clic en el botón <i class="fas fa-plus-circle"></i> de signo más en la parte inferior de un paso y selecciona **Experiment Paths**.

En la configuración predeterminada de este componente, hay dos rutas predeterminadas, **Path 1** y **Path 2**, con el 50% de la audiencia enviada por cada ruta. Haz clic en el componente para expandir el panel de **Experiment Settings**, y verás las opciones de configuración del componente.

### Paso 1: Elige el número de rutas y la distribución de la audiencia {#step-1-choose-the-number-of-paths-and-audience-distribution}

Puedes añadir hasta cuatro rutas haciendo clic en **Add Path** y un grupo de control opcional marcando **Add a Control Group**. Usando las casillas de porcentaje para cada ruta, puedes especificar el porcentaje de la audiencia que debe ir por cada ruta y el grupo de control. Los porcentajes proporcionados deben sumar 100% para continuar. Si quieres establecer rápidamente todas las rutas disponibles (y el control) con el mismo porcentaje, haz clic en **Distribute Paths Evenly**.

También puedes elegir si los usuarios del grupo de control deben continuar por el Canvas o salir después de la ventana de seguimiento de conversión para el **Control Group Behavior**. Opcionalmente, puedes añadir una descripción para explicar a otros qué pretende probar este recorrido de experimentos o incluir información adicional que pueda ser útil anotar.

![Configuración del experimento donde puedes añadir rutas y distribuir el porcentaje de usuarios en cada ruta.]({% image_buster /assets/img/experiment_step/exp_settings.png %})

{% alert note %}
Si la reelegibilidad del Canvas está habilitada, los usuarios que entren al Canvas y vayan por una ruta elegida aleatoriamente irán por la misma ruta de nuevo si se vuelven reelegibles y reingresan al Canvas. Esto mantiene la validez del experimento y los análisis asociados. Si quieres que el paso siempre aleatorice la asignación de rutas, selecciona **Randomized Paths in Experiment Paths**. Esta opción no está disponible cuando se usa la ruta ganadora o los recorridos personalizados.
{% endalert %}

### Paso 2: Activa la ruta ganadora o los recorridos personalizados (opcional) {#step-2}

Puedes elegir optimizar tu experimento activando la [ruta ganadora]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step/winning_path) o los [recorridos personalizados]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step/personalized_paths). Ambas opciones funcionan probando inicialmente tus rutas con una porción de tu audiencia. Después de que el experimento termine, los usuarios restantes y posteriores se envían por la ruta con mejor rendimiento general (ruta ganadora) o por la ruta con mejor rendimiento para cada usuario (recorridos personalizados).

### Paso 3: Crea las rutas {#step-3-create-paths}

Por último, debes construir tus rutas posteriores. Selecciona **Done** y vuelve al constructor de Canvas. Haz clic en el botón <i class="fas fa-plus-circle"></i> de signo más debajo de cada ruta para comenzar a crear recorridos usando las herramientas habituales de Canvas como consideres conveniente, y lanza el Canvas cuando estés listo.

![Añadiendo pasos a cada ruta que se divide desde un componente de recorridos de experimentos.]({% image_buster /assets/img/experiment_step/experiment_downstream_paths.gif %}){: style="max-width:75%"}

Ten en cuenta que las rutas y sus pasos posteriores no se pueden eliminar de un Canvas después de haber sido creados. Sin embargo, una vez lanzado, puedes modificar la distribución de la audiencia entre las rutas como consideres conveniente. Por ejemplo, si un día después de lanzar un Canvas concluyes que una ruta es superior al resto según los análisis, puedes establecer esa ruta al 100% y las demás al 0%. O, dependiendo de tus necesidades, puedes continuar enviando usuarios por múltiples rutas.

{% alert important %}
Para prevenir la contaminación del experimento, si tu Canvas tiene un experimento de ruta ganadora o recorridos personalizados activo o en progreso y actualizas el Canvas activo, independientemente de si actualizas el paso de recorrido de experimentos en sí, el experimento en progreso terminará y el paso del experimento no determinará una ruta ganadora ni recorridos personalizados. Para reiniciar el experimento, puedes desconectar el recorrido de experimentos existente y lanzar uno nuevo, o duplicar el Canvas y lanzar un nuevo Canvas. De lo contrario, los usuarios fluirán a través de la ruta de experimentos como si no se hubiera seleccionado ningún método de optimización. Tampoco puedes activar recorridos personalizados o ruta ganadora para un Canvas ya activo con un paso de recorrido de experimentos.<br><br>Para más información, consulta [Editar Canvas después del lanzamiento]({{site.baseurl}}/post-launch_edits).
{% endalert %}

## Seguimiento del rendimiento {#tracking-performance}

Desde la página de **Canvas Analytics**, selecciona el recorrido de experimentos para abrir una [tabla detallada]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/change_your_canvas_after_launch) idéntica a la pestaña **Analyze Variants** para comparar estadísticas detalladas de rendimiento y conversión entre rutas. También puedes exportar la tabla vía CSV y comparar los cambios porcentuales para las métricas de interés en relación con la ruta o el control que selecciones.

Cada paso en cada ruta muestra estadísticas en la vista de [análisis de Canvas]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics), igual que cualquier paso en Canvas. Sin embargo, ten en cuenta que los análisis de pasos individuales y los análisis de recorridos de experimentos miden las conversiones de manera diferente:

- **Los análisis de recorridos de experimentos** hacen seguimiento de las conversiones desde que el usuario entra al paso de recorrido de experimentos. Esta es la vista recomendada para comparar el rendimiento entre rutas porque todas las rutas comparten el mismo punto de inicio.
- **Los análisis de pasos individuales** (como los análisis de pasos de mensaje) hacen seguimiento de las conversiones desde que el usuario recibe ese paso específico (por ejemplo, cuando se envía el mensaje).

Debido a que estas ventanas de conversión tienen diferentes puntos de inicio, pueden mostrar diferentes tasas de conversión para la misma ruta, especialmente cuando hay retrasos entre el paso del experimento y un mensaje posterior. Para la comparación más fiable entre rutas, usa los análisis de recorridos de experimentos.

### Rendimiento de ruta ganadora y recorridos personalizados {#winning-path-and-personalized-paths-performance}

Aprovecha la ruta ganadora para hacer seguimiento del rendimiento durante un período de tiempo y luego enviar automáticamente a los usuarios posteriores por la ruta con mejor rendimiento. Para más información sobre los análisis cuando la **ruta ganadora** o los **recorridos personalizados** están activados para tu experimento, consulta:

- [Ruta ganadora]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step/winning_path#analytics)
- [Recorridos personalizados]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step/personalized_paths#analytics)

La métrica ganadora y los análisis mostrados en los recorridos de experimentos pueden diferir:

- El evento de conversión que configuras para la **ruta ganadora** o los **recorridos personalizados** determina cómo Braze compara las rutas y selecciona un ganador durante la ventana del experimento.
- Los análisis de recorridos de experimentos siguen el mismo marco de [eventos de conversión]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events) de Canvas que el resto del Canvas, incluyendo tu [evento de conversión primaria]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events#primary-conversion-event). Como resultado, las métricas destacadas en el panel pueden no coincidir con la métrica ganadora.
- Para push, *Direct Opens* y *Total Opens* difieren. Para más información, consulta [Influenced Opens]({{site.baseurl}}/user_guide/analytics/tracking/influenced_opens).

### Configuración adicional {#additional-settings}

Los recorridos de experimentos registran a los usuarios que entran en cada paso y convierten mientras están en la ruta asignada. Esto hace seguimiento de todos los eventos de conversión especificados en la configuración del Canvas. En la pestaña **Additional Settings**, ingresa cuántos días (entre 1 y 30) quieres que este experimento haga seguimiento de las conversiones. La ventana de tiempo que especifiques aquí determina durante cuánto tiempo se hace seguimiento de los eventos de conversión (elegidos en la configuración del Canvas) para el experimento. Las ventanas de conversión por evento especificadas en la configuración del Canvas no se aplican al seguimiento de este paso y son reemplazadas por esta ventana de conversión.

La ventana de conversión comienza cuando el usuario entra al paso de recorrido de experimentos, no cuando se envía un mensaje posterior. Si una ruta incluye retrasos, como un paso de retraso o [sincronización inteligente]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing), esos retrasos consumen parte de la ventana de conversión.

{% alert important %}
Si estás usando sincronización inteligente en un paso de mensaje dentro de un recorrido de experimentos, el tiempo entre la entrada al experimento y el envío real del mensaje reduce la ventana de conversión efectiva para esa ruta. Por ejemplo, si tu experimento tiene una ventana de conversión de 5 días y la sincronización inteligente retrasa el mensaje 2 días, los usuarios en esa ruta solo tienen 3 días después de recibir el mensaje para convertir dentro de la ventana del experimento, aunque los análisis propios del paso de mensaje hacen seguimiento de las conversiones desde el momento del envío del mensaje.<br><br>Para obtener análisis de experimentos más limpios, coloca cualquier retraso (como pasos de retraso) **antes** del paso de recorrido de experimentos en lugar de dentro de un recorrido de experimentos. De esta manera, todas las rutas comienzan desde el mismo punto y los retrasos no consumen parte de la ventana de conversión.
{% endalert %}

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Por qué los envíos difieren entre rutas cuando la división del experimento parece equitativa? {#why-do-sends-differ-across-paths-when-the-experiment-split-looks-even}

Los _envíos_ posteriores dependen de los pasos de cada ruta, los retrasos, la elegibilidad del canal y el contenido, no solo de la división porcentual en el recorrido de experimentos. Por ejemplo, diferentes retrasos, tiempos de envío inteligentes o el estado de suscripción pueden cambiar cuántos usuarios reciben un mensaje incluso cuando la asignación de rutas fue equilibrada. Para comparar los resultados de las rutas, usa los [análisis de recorridos de experimentos](#tracking-performance), que miden las conversiones desde un punto de entrada común.

### ¿Cuánto dura la ventana de conversión del experimento? {#how-long-does-the-experiment-conversion-window-last}

La ventana de conversión de **Additional Settings** (de 1 a 30 días) comienza cuando el usuario entra al paso de recorrido de experimentos. El tiempo transcurrido en pasos de retraso posteriores o esperando la sincronización inteligente cuenta dentro de esa ventana. Consulta [Seguimiento del rendimiento](#tracking-performance) para más detalles.