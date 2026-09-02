---
nav_title: Ruta ganadora
article_title: Ruta ganadora en recorridos de experimentos
page_type: reference
description: "Este artículo de referencia cubre la ruta ganadora, una característica que te permite automatizar tus pruebas A/B cuando se activa en un paso de recorrido de experimentos."
tool: Canvas
---

# Ruta ganadora en recorridos de experimentos {#winning-path-in-experiment-paths}

> La ruta ganadora prueba automáticamente las rutas de Canvas y envía a los usuarios posteriores por la ruta con mejor rendimiento.

Cuando la ruta ganadora está activada en un paso de recorrido de experimentos, después de un período de tiempo especificado, todos los usuarios posteriores son enviados por la ruta con la tasa de conversión más alta.

## Uso de la ruta ganadora {#using-winning-path}

### Paso 1: Añadir un paso de recorrido de experimentos {#step-1-add-an-experiment-path-step}

Añade un [recorrido de experimentos]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step) a tu Canvas y, a continuación, activa **Ruta ganadora**.

![Configuración en el recorrido de experimentos titulada "Distribuir usuarios posteriores a la ruta ganadora". La sección incluye un conmutador para la ruta ganadora y opciones para configurar el evento de conversión y la ventana del experimento.]({% image_buster /assets/img/experiment_step/experiment_winning_path_recurring.png %})

### Paso 2: Configurar los ajustes de la ruta ganadora {#step-2-configure-winning-path-settings}

Especifica el evento de conversión que debe determinar el ganador. Si no hay eventos de conversión disponibles, vuelve al primer paso de la configuración del Canvas y [asigna eventos de conversión]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#choose-conversion-events).

Si eliges aperturas o clics como tu evento de conversión, asegúrate de que el primer paso en la ruta sea un [paso de mensaje]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step). Braze solo cuenta la participación del primer paso de mensaje en cada ruta respectiva. Si la ruta comienza con un paso diferente (como un paso de aplazamiento o de ruta de audiencia) y el mensaje viene después, ese mensaje no se incluirá al evaluar el rendimiento.

A continuación, configura la **ventana del experimento**. La **ventana del experimento** especifica cuánto tiempo se ejecuta el experimento antes de que se determine la ruta ganadora y todos los usuarios que sigan sean enviados por esa ruta. La ventana comienza cuando el primer usuario entra en el paso.

![Configuración de la ruta ganadora con el evento de conversión "Clics" seleccionado para una ventana de experimento de 12 horas.]({% image_buster /assets/img/experiment_step/experiment_winning_settings.png %})

### Paso 3: Determinar la alternativa {#statistical-significance}

De forma predeterminada, si los resultados de la prueba no son suficientes para determinar un ganador estadísticamente significativo, todos los usuarios futuros son enviados por la ruta con mejor rendimiento. Como alternativa, puedes seleccionar **Continuar enviando a todos los usuarios futuros la combinación de rutas**. Esta opción envía a los usuarios futuros por la combinación de rutas según los porcentajes especificados en la distribución del recorrido de experimentos.

En caso de empate, Braze selecciona la ruta que aparece primero.

!["Continuar enviando a todos los usuarios futuros la combinación de rutas" seleccionada como lo que sucede con los usuarios si el resultado de la prueba no es estadísticamente significativo.]({% image_buster /assets/img/experiment_step/experiment_winning_statistical.png %})

{% alert note %}
Un grupo de aplazamiento aparece en tu distribución de rutas solo si tu Canvas está configurado para entrada única y tu paso de experimento tiene tres rutas o menos. Los Canvas recurrentes y desencadenados no tienen un grupo de aplazamiento cuando la ruta ganadora está activada.
{% endalert %}

### Paso 4: Añadir tus rutas y lanzar el Canvas {#step-4-add-your-paths-and-launch-the-canvas}

Un único componente de recorrido de experimentos puede contener hasta cuatro rutas. Sin embargo, si tu Canvas está configurado para [entrada única](#one-time-entry), una ruta debe estar reservada para el grupo de aplazamiento que Braze añade automáticamente cuando la ruta ganadora está activada. Esto significa que, para los Canvas con entrada única, puedes añadir hasta tres rutas a tu experimento.

Termina de configurar tu Canvas según sea necesario y luego lánzalo. Cuando el primer usuario haya entrado en el experimento, puedes consultar el Canvas para ver los análisis a medida que llegan y [hacer seguimiento del rendimiento de tu experimento]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step#tracking-performance).

Después de que concluye una ruta ganadora, todos los usuarios posteriores que entren en el Canvas siguen la ruta ganadora, incluidos los usuarios que volvieron a entrar y que anteriormente estaban en el grupo de control del paso de recorrido de experimentos.

## Análisis {#analytics}

Si la ruta ganadora está activada, tu vista de análisis se separa en dos pestañas: **Experimento inicial** y **Ruta ganadora**.

- **Experimento inicial:** Muestra las métricas de cada ruta durante la ventana del experimento, qué ruta fue seleccionada como ganadora y las métricas de conversión del Canvas. El evento de conversión utilizado para elegir al ganador, configurado en los ajustes de la ruta ganadora, podría no ser el mismo que la métrica de conversión destacada en los análisis del Canvas. Para más información sobre cómo los análisis del recorrido de experimentos se relacionan con los eventos de conversión del Canvas y la métrica ganadora, consulta [Recorridos de experimentos]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step#winning-path-performance).
- **Ruta ganadora:** Muestra solo las métricas de la ruta ganadora a partir del momento en que finalizó el experimento inicial.

## Cosas que debes saber {#things-to-know}

### Entrada única {#one-time-entry}

Cuando se utilizan recorridos ganadores en un Canvas en el que los usuarios solo pueden entrar una vez, se incluye automáticamente un grupo de retraso. Durante la duración del experimento, un porcentaje de usuarios se retiene en el grupo de retraso mientras los usuarios restantes entran en tus recorridos de experimentos.

![Paso de experimento con un grupo de retraso para el recorrido ganador]({% image_buster /assets/img/experiment_step/experiment_one_time.png %}){: style="max-width:75%"}

Cuando la prueba finaliza y se determina un recorrido ganador, los usuarios asignados al grupo de retraso se dirigen al recorrido elegido y continúan a través del Canvas.

![Paso de experimento con un grupo de retraso enviado por el recorrido ganador]({% image_buster /assets/img/experiment_step/experiment_one_time_results.png %}){: style="max-width:75%"}

### Entrega según la zona horaria local {#local-time-delivery}

No recomendamos usar la entrega según la zona horaria local en Canvas con recorridos ganadores. Esto se debe a que las ventanas de experimento comienzan cuando el primer usuario pasa a través del paso. Los usuarios que se encuentran en zonas horarias muy tempranas pueden entrar en el paso y desencadenar el inicio de la ventana de experimento mucho antes de lo que esperas, lo que puede provocar que el experimento concluya antes de que la mayoría de tus usuarios en zonas horarias más habituales hayan tenido tiempo suficiente para entrar en el Canvas, convertir, o ambas cosas.

Alternativamente, si deseas usar la entrega local, utiliza una ventana de experimento de 24-48 horas o más. De esa forma, los usuarios en zonas horarias tempranas entran en el Canvas y desencadenan el inicio del experimento, pero queda tiempo suficiente en la ventana de experimento. Los usuarios en zonas horarias posteriores aún tienen tiempo suficiente para entrar en el Canvas y en el paso de experimento con recorridos ganadores y posiblemente convertir antes de que la ventana de experimento expire.

### Variantes basadas en clics {#variants-based-on-clicks}

Si estás configurando una variante de recorrido ganador basada en clics, ten en cuenta que las definiciones de aperturas y clics difieren según el canal. Para conocer las métricas y definiciones específicas por canal, consulta el [Glosario de métricas de informes]({{site.baseurl}}/user_guide/analytics/metrics_glossary) y el [Glosario de métricas de informes de correo electrónico]({{site.baseurl}}/user_guide/channels/email/reporting/analytics_glossary).