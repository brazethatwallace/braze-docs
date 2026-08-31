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

Para utilizar recorridos de experimentos, tu Canvas debe incluir eventos de conversión. Aunque no puedes añadir eventos de conversión después de que un Canvas se haya lanzado, puedes clonar el Canvas lanzado y añadir eventos de conversión para agregar recorridos de experimentos.

## Ejemplos {#use-cases}

Los recorridos de experimentos son más adecuados para probar la entrega, la cadencia, el texto de los mensajes y las combinaciones de canales.

- **Entrega:** Compara los resultados entre mensajes enviados con diferentes [retrasos]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step) de tiempo, basados en acciones del usuario ([Rutas de Acción]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths)), y utilizando [sincronización inteligente]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing#step-1-add-intelligent-timing-1).<br><br>
- **Cadencia:** Prueba múltiples flujos de mensajería durante un período específico. Por ejemplo, podrías probar dos cadencias de incorporación diferentes:
    - Cadencia 1: Enviar 2 mensajes en las primeras 2 semanas del usuario
    - Cadencia 2: Enviar 3 mensajes en las primeras 2 semanas del usuario

    Al dirigirte a usuarios inactivos, puedes probar la eficacia de enviar dos mensajes de recuperación en una semana frente a enviar solo uno.
- **Texto del mensaje:** De forma similar a una [prueba A/B]({{site.baseurl}}/user_guide/messaging/ab_testing) estándar, puedes probar diferentes textos de mensaje para ver qué redacción genera una tasa de conversión más alta.<br><br>
- **Combinaciones de canales:** Prueba la eficacia de diferentes combinaciones de canales de mensajería. Por ejemplo, puedes comparar el impacto de usar solo un correo electrónico frente a un correo electrónico combinado con un push.

## Creación de un recorrido de experimentos {#creating-an-experiment-path}

Para crear un componente de recorrido de experimentos, primero añade un paso a tu Canvas. Arrastra y suelta el componente desde la barra lateral, o haz clic en el botón <i class="fas fa-plus-circle"></i> de suma en la parte inferior de un paso y selecciona **Recorrido de experimentos**.

En la configuración predeterminada de este componente, hay dos recorridos predeterminados, **Recorrido 1** y **Recorrido 2**, con el 50% de la audiencia enviada por cada recorrido. Haz clic en el componente para expandir el panel de **Configuración del experimento**, y verás las opciones de configuración del componente.

### Paso 1: Elige el número de recorridos y la distribución de la audiencia {#step-1-choose-the-number-of-paths-and-audience-distribution}

Puedes añadir hasta cuatro recorridos haciendo clic en **Añadir recorrido** y un grupo de control opcional marcando **Añadir un grupo de control**. Usando las casillas de porcentaje de cada recorrido, puedes especificar el porcentaje de la audiencia que debe ir a cada recorrido y al grupo de control. Los porcentajes proporcionados deben sumar el 100% para continuar. Si deseas establecer rápidamente todos los recorridos disponibles (y el control) en el mismo porcentaje, haz clic en **Distribuir recorridos equitativamente**.

También puedes elegir si los usuarios del grupo de control deben continuar por el Canvas o salir después de la ventana de seguimiento de conversiones para el **Comportamiento del grupo de control**. Opcionalmente, puedes añadir una descripción para explicar a otros qué pretende probar este recorrido de experimentos o incluir información adicional que pueda ser útil anotar.

![Configuración del experimento donde puedes añadir recorridos y distribuir el porcentaje de usuarios en cada recorrido.]({% image_buster /assets/img/experiment_step/exp_settings.png %})

{% alert note %}
Si la reelegibilidad del Canvas está habilitada, los usuarios que entren en el Canvas y sigan un recorrido elegido al azar seguirán el mismo recorrido de nuevo si se vuelven reelegibles y reingresan al Canvas. Esto mantiene la validez del experimento y los análisis asociados. Si quieres que el paso siempre aleatorice la asignación de recorridos, selecciona **Recorridos aleatorios en recorridos de experimentos**. Esta opción no está disponible cuando se utiliza la ruta ganadora o los recorridos personalizados.
{% endalert %}

### Paso 2: Activa la ruta ganadora o los recorridos personalizados (opcional) {#step-2}

Puedes elegir optimizar tu experimento activando la [ruta ganadora]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step/winning_path) o los [recorridos personalizados]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step/personalized_paths). Ambas opciones funcionan probando inicialmente tus recorridos con una parte de tu audiencia. Después de que el experimento termine, los usuarios restantes y posteriores son enviados por el recorrido con mejor rendimiento en general (ruta ganadora) o el recorrido con mejor rendimiento para cada usuario (recorridos personalizados).

### Paso 3: Crea los recorridos {#step-3-create-paths}

Por último, debes construir tus recorridos posteriores. Selecciona **Listo** y regresa al constructor de Canvas. Haz clic en el botón <i class="fas fa-plus-circle"></i> de suma debajo de cada recorrido para comenzar a crear trayectos usando las herramientas habituales de Canvas como consideres adecuado, y lanza el Canvas cuando estés listo.

![Añadir pasos a cada recorrido que se divide desde un componente de recorrido de experimentos.]({% image_buster /assets/img/experiment_step/experiment_downstream_paths.gif %}){: style="max-width:75%"}

Ten en cuenta que los recorridos y sus pasos posteriores no pueden eliminarse de un Canvas una vez creados. Sin embargo, una vez lanzado, puedes modificar la distribución de la audiencia entre recorridos como consideres oportuno. Por ejemplo, si un día después de lanzar un Canvas concluyes que un recorrido es superior al resto según los análisis, puedes establecer ese recorrido al 100% y los demás al 0%. O, dependiendo de tus necesidades, puedes seguir enviando usuarios por múltiples recorridos.

{% alert important %}
Para evitar la contaminación del experimento, si tu Canvas tiene un experimento de ruta ganadora o recorrido personalizado activo o en curso y actualizas el Canvas activo, independientemente de si actualizas el paso de recorrido de experimentos en sí, el experimento en curso terminará y el paso del experimento no determinará una ruta ganadora ni recorridos personalizados. Para reiniciar el experimento, puedes desconectar el recorrido de experimentos existente y lanzar uno nuevo, o duplicar el Canvas y lanzar un nuevo Canvas. De lo contrario, los usuarios fluirán por el recorrido de experimentos como si no se hubiera seleccionado ningún método de optimización. Tampoco puedes activar recorridos personalizados o la ruta ganadora para un Canvas ya activo con un paso de recorrido de experimentos.<br><br>Para más información, consulta [Editar Canvas después del lanzamiento]({{site.baseurl}}/post-launch_edits).
{% endalert %}

## Seguimiento del rendimiento {#tracking-performance}

Desde la página de **análisis de Canvas**, selecciona el recorrido de experimentos para abrir una [tabla detallada]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/change_your_canvas_after_launch) idéntica a la pestaña **Analizar variantes** para comparar estadísticas detalladas de rendimiento y conversión entre recorridos. También puedes exportar la tabla en formato CSV y comparar los cambios porcentuales de las métricas de interés en relación con el recorrido o el control que selecciones.

Cada paso en cada recorrido muestra estadísticas en la vista de [análisis de Canvas]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics), igual que cualquier paso de Canvas. Sin embargo, ten en cuenta que los análisis de pasos individuales y los análisis de recorridos de experimentos miden las conversiones de forma diferente:

- **Los análisis de recorridos de experimentos** hacen seguimiento de las conversiones a partir del momento en que el usuario entra en el paso de recorrido de experimentos. Esta es la vista recomendada para comparar el rendimiento entre recorridos porque todos los recorridos comparten el mismo punto de inicio.
- **Los análisis de pasos individuales** (como los análisis de pasos de mensaje) hacen seguimiento de las conversiones a partir del momento en que el usuario recibe ese paso específico (por ejemplo, cuando se envía el mensaje).

Dado que estas ventanas de conversión tienen puntos de inicio diferentes, pueden mostrar tasas de conversión distintas para el mismo recorrido, especialmente cuando hay retrasos entre el paso de experimento y un mensaje posterior. Para la comparación más fiable entre recorridos, utiliza los análisis de recorridos de experimentos.

### Rendimiento de la ruta ganadora y los recorridos personalizados {#winning-path-and-personalized-paths-performance}

Aprovecha las rutas ganadoras para hacer seguimiento del rendimiento durante un período de tiempo y, a continuación, enviar automáticamente a los usuarios posteriores por el recorrido con mejor rendimiento. Para obtener más información sobre los análisis cuando la **ruta ganadora** o los **recorridos personalizados** están activados en tu experimento, consulta:

- [Ruta ganadora]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step/winning_path#analytics)
- [Recorridos personalizados]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step/personalized_paths#analytics)

La métrica ganadora y los análisis mostrados en los recorridos de experimentos pueden diferir:

- El evento de conversión que configures para la **ruta ganadora** o los **recorridos personalizados** determina cómo Braze compara los recorridos y selecciona un ganador durante la ventana del experimento.
- Los análisis de recorridos de experimentos siguen el mismo marco de [eventos de conversión]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events) de Canvas que el resto del Canvas, incluido tu [evento de conversión primaria]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events#primary-conversion-event). Como resultado, las métricas destacadas en el panel podrían no coincidir con la métrica ganadora.
- Para push, *Direct Opens* y *Total Opens* difieren. Para obtener más información, consulta [Influenced Opens]({{site.baseurl}}/user_guide/analytics/tracking/influenced_opens).

### Configuración adicional {#additional-settings}

Los recorridos de experimentos registran a los usuarios que entran en cada paso y convierten mientras están en el recorrido asignado. Esto hace seguimiento de todos los eventos de conversión especificados en la configuración del Canvas. En la pestaña **Configuración adicional**, introduce cuántos días (entre 1 y 30) quieres que este experimento haga seguimiento de las conversiones. La ventana de tiempo que especifiques aquí determina durante cuánto tiempo se hace seguimiento de los eventos de conversión (elegidos en la configuración del Canvas) para el experimento. Las ventanas de conversión por evento especificadas en la configuración del Canvas no se aplican al seguimiento de este paso y son reemplazadas por esta ventana de conversión.

La ventana de conversión comienza cuando el usuario entra en el paso de recorrido de experimentos, no cuando se envía un mensaje posterior. Si un recorrido incluye retrasos, como un paso de retraso o la [sincronización inteligente]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing), esos retrasos consumen parte de la ventana de conversión.

{% alert important %}
Si utilizas la sincronización inteligente en un paso de mensaje dentro de un recorrido de experimentos, el tiempo entre la entrada al experimento y el envío real del mensaje reduce la ventana de conversión efectiva para ese recorrido. Por ejemplo, si tu experimento tiene una ventana de conversión de 5 días y la sincronización inteligente retrasa el mensaje 2 días, los usuarios en ese recorrido solo tienen 3 días después de recibir el mensaje para convertir dentro de la ventana del experimento, aunque los análisis propios del paso de mensaje hagan seguimiento de las conversiones a partir del momento del envío del mensaje.<br><br>Para obtener análisis de experimentos más limpios, coloca cualquier retraso (como pasos de retraso) **antes** del paso de recorrido de experimentos en lugar de dentro de un recorrido de experimentos. De esta manera, todos los recorridos parten del mismo punto y los retrasos no consumen parte de la ventana de conversión.
{% endalert %}

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Por qué los envíos difieren entre recorridos cuando la división del experimento parece uniforme? {#why-do-sends-differ-across-paths-when-the-experiment-split-looks-even}

Los _envíos_ posteriores dependen de los pasos, retrasos, elegibilidad de canal y contenido de cada recorrido, no solo del porcentaje de división en el recorrido de experimentos. Por ejemplo, diferentes retrasos, sincronización inteligente o estados de suscripción pueden cambiar cuántos usuarios reciben un mensaje, incluso cuando la asignación de recorridos fue equilibrada. Para comparar los resultados de los recorridos, utiliza los [análisis del recorrido de experimentos](#tracking-performance), que miden las conversiones desde un punto de entrada común.

### ¿Cuánto dura la ventana de conversión del experimento? {#how-long-does-the-experiment-conversion-window-last}

La ventana de conversión en **Configuración adicional** (de 1 a 30 días) comienza cuando el usuario entra en el paso de recorrido de experimentos. El tiempo transcurrido en pasos de retraso posteriores o a la espera de la sincronización inteligente cuenta dentro de esa ventana. Consulta [Seguimiento del rendimiento](#tracking-performance) para más detalles.