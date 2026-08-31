---
nav_title: Ruta ganadora
article_title: Ruta ganadora en recorridos de experimentos
page_type: reference
description: "Este artículo de referencia cubre la ruta ganadora, una característica que te permite automatizar tus pruebas A/B cuando se activa en un paso de recorrido de experimentos."
tool: Canvas
---

# Ruta ganadora en recorridos de experimentos {#winning-path-in-experiment-paths}

> La ruta ganadora es similar a la [variante ganadora]({{site.baseurl}}/user_guide/messaging/ab_testing/optimizations) en Campaigns, y te permite automatizar tus pruebas A/B.

Cuando la ruta ganadora está activada en un paso de recorrido de experimentos, después de un período de tiempo especificado, todos los usuarios posteriores son enviados por la ruta con la tasa de conversión más alta.

## Uso de Recorrido ganador {#using-winning-path}

### Paso 1: Añadir un paso de recorrido de experimentos {#step-1-add-an-experiment-path-step}

Añade un [recorrido de experimentos]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step) a tu Canvas y, a continuación, activa **Recorrido ganador**.

![Configuración del recorrido de experimentos titulada "Distribuir usuarios posteriores al recorrido ganador". La sección incluye un conmutador para Recorrido ganador y opciones para configurar el evento de conversión y la ventana de experimento.]({% image_buster /assets/img/experiment_step/experiment_winning_path_recurring.png %})

### Paso 2: Configurar los ajustes del recorrido ganador {#step-2-configure-winning-path-settings}

Especifica el evento de conversión que debe determinar el ganador. Si no hay eventos de conversión disponibles, vuelve al primer paso de la configuración del Canvas y [asigna eventos de conversión]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#choose-conversion-events).

Si eliges aperturas o clics como evento de conversión, asegúrate de que el primer paso en el recorrido sea un [paso de mensaje]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step). Braze solo cuenta la participación del primer paso de mensaje en cada recorrido respectivo. Si el recorrido comienza con un paso diferente (como un paso de retraso o de ruta de audiencia) y el mensaje viene después, ese mensaje no se incluirá al evaluar el rendimiento.

A continuación, configura la **ventana de experimento**. La **ventana de experimento** especifica cuánto tiempo se ejecuta el experimento antes de que se determine el recorrido ganador y todos los usuarios que sigan sean enviados por ese recorrido. La ventana comienza cuando el primer usuario entra en el paso.

![Configuración del recorrido ganador con el evento de conversión "Clics" seleccionado para una ventana de experimento de 12 horas.]({% image_buster /assets/img/experiment_step/experiment_winning_settings.png %})

### Paso 3: Determinar la alternativa {#statistical-significance}

De forma predeterminada, si los resultados de la prueba no son suficientes para determinar un ganador estadísticamente significativo, todos los usuarios futuros se envían por el recorrido con mejor rendimiento. Como alternativa, puedes seleccionar **Continuar enviando a todos los usuarios futuros la combinación de recorridos**. Esta opción envía a los usuarios futuros por la combinación de recorridos según los porcentajes especificados en la distribución del recorrido de experimentos.

En caso de empate, Braze selecciona el recorrido que aparece primero.

!["Continuar enviando a todos los usuarios futuros la combinación de recorridos" seleccionado como lo que ocurre con los usuarios si el resultado de la prueba no es estadísticamente significativo.]({% image_buster /assets/img/experiment_step/experiment_winning_statistical.png %})

{% alert note %}
Un grupo de retraso aparece en la distribución de recorridos solo si tu Canvas está configurado para entrada única y tu paso de experimento tiene tres recorridos o menos. Los Canvas recurrentes y desencadenados no tienen un grupo de retraso cuando el recorrido ganador está activado.
{% endalert %}

### Paso 4: Añadir los recorridos y lanzar el Canvas {#step-4-add-your-paths-and-launch-the-canvas}

Un solo componente de recorrido de experimentos puede contener hasta cuatro recorridos. Sin embargo, si tu Canvas está configurado para [entrada única](#one-time-entry), un recorrido debe estar reservado para el grupo de retraso que Braze añade automáticamente cuando se activa el recorrido ganador. Esto significa que, para los Canvas con entrada única, puedes añadir hasta tres recorridos a tu experimento.

Termina de configurar tu Canvas según sea necesario y luego lánzalo. Cuando el primer usuario haya entrado en el experimento, puedes comprobar el Canvas para ver los análisis a medida que llegan y [hacer un seguimiento del rendimiento de tu experimento]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step#tracking-performance).

Una vez que concluye un recorrido ganador, todos los usuarios posteriores que entran en el Canvas recorren el recorrido ganador, incluidos los usuarios que volvieron a entrar y que anteriormente estaban en el grupo de control del paso de recorrido de experimentos.

## Análisis {#analytics}

Si la ruta ganadora está activada, tu vista de análisis se separa en dos pestañas: **Experimento inicial** y **Ruta ganadora**.

- **Experimento inicial:** Muestra las métricas de cada ruta durante la ventana del experimento, qué ruta fue seleccionada como ganadora y las métricas de conversión del Canvas. El evento de conversión utilizado para elegir al ganador, configurado en los ajustes de la ruta ganadora, podría no ser el mismo que la métrica de conversión destacada en los análisis del Canvas. Para más información sobre cómo los análisis del recorrido de experimentos se relacionan con los eventos de conversión del Canvas y la métrica ganadora, consulta [Recorridos de experimentos]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step#winning-path-and-personalized-paths-performance).
- **Ruta ganadora:** Muestra solo las métricas de la ruta ganadora a partir del momento en que finalizó el experimento inicial.

## Cosas que debes saber {#things-to-know}

### Entrada única {#one-time-entry}

Cuando se utiliza Recorridos ganadores en un Canvas en el que los usuarios solo pueden entrar una vez, se incluye automáticamente un Grupo de demora. Durante la duración del experimento, un porcentaje de usuarios se mantiene en el Grupo de demora mientras los usuarios restantes entran en tus Recorridos de experimentos.

![Paso de experimento con un Grupo de demora para Recorrido ganador]({% image_buster /assets/img/experiment_step/experiment_one_time.png %}){: style="max-width:75%"}

Cuando la prueba finaliza y se determina un Recorrido ganador, los usuarios asignados al Grupo de demora se dirigen al recorrido elegido y continúan a través del Canvas.

![Paso de experimento con un Grupo de demora enviado por el Recorrido ganador]({% image_buster /assets/img/experiment_step/experiment_one_time_results.png %}){: style="max-width:75%"}

### Entrega según la zona horaria local {#local-time-delivery}

No recomendamos utilizar la entrega según la zona horaria local en Canvas con Recorridos ganadores. Esto se debe a que las ventanas de experimentación comienzan cuando el primer usuario pasa por ellas. Los usuarios que se encuentran en zonas horarias muy tempranas pueden entrar en el paso y desencadenar el inicio de la ventana de experimentación mucho antes de lo esperado, lo que puede dar lugar a que el experimento concluya antes de que la mayoría de tus usuarios en zonas horarias más habituales hayan tenido tiempo suficiente para entrar en el Canvas, convertir, o ambas cosas.

Alternativamente, si deseas utilizar la entrega local, usa una ventana de experimentación de 24-48 horas o más. De esta forma, los usuarios en zonas horarias tempranas entran en el Canvas y desencadenan el inicio del experimento, pero queda tiempo de sobra en la ventana de experimentación. Los usuarios en zonas horarias más tardías aún tienen tiempo suficiente para entrar en el Canvas y en el paso de experimento con Recorridos ganadores y posiblemente convertir antes de que la ventana de experimentación expire.

### Variantes basadas en clics {#variants-based-on-clicks}

Si estás configurando una variante de Recorrido ganador basada en clics, ten en cuenta que las definiciones de aperturas y clics difieren según el canal. Para métricas y definiciones específicas por canal, consulta el [Glosario de métricas de informe]({{site.baseurl}}/user_guide/analytics/metrics_glossary) y el [Glosario de métricas de informe de correo electrónico]({{site.baseurl}}/user_guide/channels/email/reporting/analytics_glossary).