---
nav_title: Recorridos personalizados
article_title: Recorridos personalizados en recorridos de experimentos
page_type: reference
description: "Los recorridos personalizados te permiten personalizar cualquier punto de un recorrido de Canvas para usuarios individuales en función de la probabilidad de conversión."
tool: Canvas
---

# Recorridos personalizados en recorridos de experimentos {#personalized-paths-in-experiment-paths}

> Los recorridos personalizados son similares a la [variante personalizada]({{site.baseurl}}/user_guide/messaging/ab_testing/optimizations#personalized-variant) en Campaigns y te permiten personalizar cualquier punto de un recorrido de Canvas para usuarios individuales en función de la probabilidad de conversión.

## Cómo funcionan los recorridos personalizados {#how-personalized-paths-works}

Cuando los recorridos personalizados están activados en un paso de recorrido de experimentos, el comportamiento es ligeramente diferente dependiendo de si tu Canvas está configurado para enviarse una sola vez o de forma recurrente:

- **Canvas de envío único:** Un grupo de usuarios se retiene en un grupo de retraso. Los usuarios restantes pasan a una prueba inicial para entrenar un modelo predictivo durante un período que tú configuras (al menos 24 horas para obtener mejores resultados). Después de la prueba, se crea un modelo que aprende qué comportamientos de los usuarios se asociaron con una mayor probabilidad de conversión en un recorrido determinado. Finalmente, cada usuario del grupo de retraso se envía por el recorrido con mayor probabilidad de generar una conversión para ellos, en función de los comportamientos que exhiben y lo que el modelo predictivo aprendió durante la prueba inicial.
- **Canvas recurrentes, desencadenados por acción y desencadenados por API:** Se realiza un experimento inicial con todos los usuarios que entran en el recorrido de experimentos durante una ventana especificada. Para mantener la integridad del experimento, si un usuario recibe múltiples mensajes antes de que termine la ventana, se le asignará la misma variante cada vez. Después de la ventana del experimento, cada usuario se envía por el recorrido con mayor probabilidad de generar una conversión para ellos.

## Uso de recorridos personalizados {#using-personalized-paths}

### Paso 1: Añadir un recorrido de experimentos {#step-1-add-an-experiment-path}

Añade un [recorrido de experimentos]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step) a tu Canvas y luego activa **Recorridos personalizados**.

![Añade un recorrido de experimentos a tu Canvas y luego activa Recorridos personalizados.]({% image_buster /assets/img/experiment_step/experiment_personalized_path.png %})

### Paso 2: Configurar los ajustes de recorridos personalizados {#step-2-configure-personalized-paths-settings}

Especifica el evento de conversión que debe determinar el ganador. Si no hay eventos de conversión disponibles, vuelve al primer paso de la configuración de Canvas y [asigna eventos de conversión]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#choose-conversion-events).

Si eliges aperturas o clics como tu evento de conversión, asegúrate de que el primer paso en el recorrido sea un [paso de mensaje]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step). Braze solo cuenta la participación del primer paso de mensaje en cada recorrido respectivo. Si el recorrido comienza con un paso diferente (como un paso de retraso o de ruta de audiencia) y el mensaje viene después, ese mensaje no se incluirá al evaluar el rendimiento.

Luego configura la **Ventana del experimento**. La **Ventana del experimento** determina durante cuánto tiempo los usuarios serán enviados por todos los recorridos antes de elegir el mejor recorrido para cada usuario en el grupo de retraso. La ventana comienza cuando el primer usuario entra en el paso.

![Captura de pantalla relacionada con el paso 2: configurar los ajustes de recorridos personalizados.]({% image_buster /assets/img/experiment_step/experiment_personalized_settings.png %})

### Paso 3: Determinar la alternativa {#step-3-determine-fallback}

De forma predeterminada, si los resultados de la prueba no son suficientes para determinar un ganador estadísticamente significativo, todos los usuarios futuros se enviarán por el recorrido con mejor rendimiento.

Alternativamente, puedes seleccionar **Continuar enviando a todos los usuarios futuros la combinación de recorridos**.

![Alternativamente, puedes seleccionar Continuar enviando a todos los usuarios futuros la combinación de recorridos.]({% image_buster /assets/img/experiment_step/experiment_winning_statistical.png %})

Esta opción enviará a los usuarios futuros por la combinación de recorridos según los porcentajes especificados en la distribución del recorrido de experimentos.

![Captura de pantalla relacionada con el paso 3: determinar la alternativa.]({% image_buster /assets/img/experiment_step/experiment_personalized_percentages.png %})

{% alert note %}
Si el experimento se completa con resultados insuficientes, solo se muestra la pestaña **Experimento inicial** porque el modelo determina que la personalización no superaría el rendimiento de un solo recorrido con mejor rendimiento. Para más detalles, consulta [Análisis](#analytics).
{% endalert %}

### Paso 4: Añadir tus recorridos y lanzar el Canvas {#step-4-add-your-paths-and-launch-the-canvas}

{% tabs local %}
{% tab Canvas de envío único %}

Un solo componente de recorrido de experimentos puede contener hasta cuatro recorridos. Sin embargo, para Canvas de envío único, puedes añadir hasta tres recorridos cuando los recorridos personalizados están activados. El cuarto recorrido debe reservarse para el grupo de retraso que Braze añade automáticamente a tu experimento.

Termina de configurar tu Canvas según sea necesario y luego lánzalo. Cuando el primer usuario haya entrado en el experimento, puedes consultar el Canvas para ver los análisis a medida que llegan y [hacer seguimiento del rendimiento de tu experimento]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step#tracking-performance).

![Captura de pantalla relacionada con el paso 4: añadir tus recorridos y lanzar el Canvas.]({% image_buster /assets/img/experiment_step/experiment_personalized_delay_group_pending.png %}){: style="max-width:75%;" }

Cuando la ventana del experimento pase y el experimento esté completo, Braze enviará a los usuarios del grupo de retraso a sus recorridos respectivos con la mayor probabilidad personalizada de conversión, basándose en la recomendación del modelo predictivo.

![Captura de pantalla relacionada con el paso 4: añadir tus recorridos y lanzar el Canvas.]({% image_buster /assets/img/experiment_step/experiment_personalized_delay_group_complete.png %}){: style="max-width:75%;" }

{% endtab %}
{% tab Canvas recurrente, desencadenado por acción o desencadenado por API %}

Puedes probar hasta cuatro recorridos en un solo recorrido de experimentos. Añade tus recorridos y termina de configurar tu Canvas según sea necesario, luego lánzalo.

Cuando el primer usuario haya entrado en el experimento, puedes consultar el Canvas para ver los análisis a medida que llegan y [hacer seguimiento del rendimiento de tu experimento]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step#tracking-performance).

Cuando la ventana del experimento pase y el experimento esté completo, todos los usuarios posteriores que entren en el Canvas se enviarán por el recorrido con mayor probabilidad de generar una conversión para ellos.

![Captura de pantalla relacionada con el paso 4: añadir tus recorridos y lanzar el Canvas.]({% image_buster /assets/img/experiment_step/experiment_personalized_recurring_analytics.png %}){: style="max-width:75%;" }

{% endtab %}
{% endtabs %}

## Análisis {#analytics}

Cuando los recorridos personalizados están activados y producen resultados suficientes, tu vista de análisis se separa en dos pestañas: **Experimento inicial** y **Recorridos personalizados**.

Si el experimento se completa con resultados insuficientes (por ejemplo, cuando la mejora proyectada del modelo es inferior al umbral del 0,5 % o no se identifican segmentos de usuarios significativos), solo se muestra la pestaña **Experimento inicial** porque el modelo determina que la personalización no superaría el rendimiento de un solo recorrido con mejor rendimiento. En este caso, se aplica el comportamiento alternativo que configuraste y no hay análisis de recorridos personalizados disponibles.

{% tabs local %}
{% tab Experimento inicial %}

La pestaña **Experimento inicial** muestra las métricas de cada recorrido durante la ventana del experimento. Puedes ver un resumen de cómo se desempeñaron todos los recorridos para los eventos de conversión especificados.

![Resultados de un experimento inicial enviado para determinar el recorrido con mejor rendimiento para cada usuario. Una tabla muestra el rendimiento de cada recorrido basándose en varias métricas para el canal objetivo.]({% image_buster /assets/img/experiment_step/experiment_personalized_analytics_tab1.png %})

De forma predeterminada, la prueba busca asociaciones entre los eventos personalizados de los usuarios y sus preferencias de recorrido, o la variante de mensaje a la que un usuario responde mejor. Este análisis detecta si los eventos personalizados aumentan o disminuyen la probabilidad de responder a un recorrido en particular. Estas relaciones se utilizan luego para determinar qué usuarios se asignan a qué recorrido después de que pase la ventana del experimento.

Las relaciones entre eventos personalizados y preferencias de recorrido se muestran en la tabla de la pestaña **Experimento inicial**.

![Captura de pantalla relacionada con los análisis.]({% image_buster /assets/img_archive/experiment_personalized_analytics_custom_data.png %})

Si la prueba no puede encontrar una relación significativa entre los eventos personalizados y las preferencias de recorrido, recurre a un método de análisis basado en sesiones, y no se muestran tablas de datos de eventos personalizados.

{% details Método de análisis alternativo %}

**Método de análisis basado en sesiones**<br>
Si se utiliza el método alternativo para determinar los recorridos personalizados, la pestaña **Experimento inicial** muestra un desglose de las variantes preferidas de los usuarios basándose en una combinación de ciertas características.

Estas características son:

- **Recencia:** Cuándo tuvieron su última sesión
- **Frecuencia:** Con qué frecuencia tienen sesiones
- **Antigüedad:** Cuánto tiempo llevan siendo usuarios

![La tabla de características de usuario, que muestra qué usuarios se predice que prefieren el recorrido 1 y el recorrido 2 en función de los tres contenedores en los que se encuentran para recencia, frecuencia y antigüedad.]({% image_buster /assets/img/experiment_step/experiment_personalized_analytics_tab1_2.png %})

Piensa en la recencia como cuán reciente fue su última interacción contigo, la frecuencia como cuán a menudo interactúan, y la antigüedad como el tiempo total que llevan interactuando contigo. Agrupamos a los usuarios en "contenedores" basándonos en estas tres cosas (como se explica en la tabla de **Características de usuario**) y luego vemos qué contenedor prefiere qué recorrido. Es como clasificar a los usuarios en cientos de listas diferentes según cuándo compraron contigo por última vez, con qué frecuencia compran y cuánto tiempo llevan siendo clientes.

Cuando se trata de elegir un mensaje para un usuario, Braze examina los contenedores en los que se encuentra. Cada contenedor ejerce una influencia distinta en la selección de recorrido para los usuarios. Cuantificamos esta influencia usando un método estadístico llamado [regresión logística](https://en.wikipedia.org/wiki/Logistic_regression), que es una forma de predecir el comportamiento futuro basándose en acciones pasadas. Este método tiene en cuenta las interacciones de los usuarios durante el envío inicial del mensaje. Esta tabla solo resume los resultados mostrando con qué recorrido tendieron a interactuar los usuarios de cada contenedor.

En última instancia, Braze combina todos estos datos para seleccionar un recorrido de mensaje personalizado para cada usuario, para asegurarse de que sea lo más atractivo y relevante posible para ellos.

{% alert note %}
Los intervalos de tiempo para cada contenedor se determinan en función de los datos de usuario específicos del Canvas, que pueden variar entre Canvas.
{% endalert %}

**Cómo se seleccionan los recorridos personalizados**<br>
Con este método, el mensaje recomendado para un usuario individual es la suma de los efectos de su recencia, frecuencia y antigüedad específicas. La recencia, la frecuencia y la antigüedad se dividen en contenedores, como se ilustra en la tabla de **Características de usuario**. El rango de tiempo de cada contenedor se determina por los datos de los usuarios en cada Canvas individual y cambiará de un Canvas a otro.

Cada contenedor puede tener una contribución o "empuje" diferente hacia cada recorrido. La fuerza del empuje para cada contenedor se determina a partir de las respuestas de los usuarios en el experimento inicial usando [regresión logística](https://en.wikipedia.org/wiki/Logistic_regression). Esta tabla solo resume los resultados mostrando con qué recorrido tendieron a interactuar los usuarios de cada contenedor. El recorrido personalizado real de cualquier usuario individual depende de la suma de los efectos de los tres contenedores en los que se encuentra, uno por cada característica.

{% enddetails %}

{% endtab %}
{% tab Recorridos personalizados %}

La pestaña **Recorridos personalizados** muestra los resultados del experimento final, donde los usuarios del grupo de retraso se enviaron por el recorrido con mejor rendimiento para ellos.

Las tres tarjetas en esta página muestran tu mejora proyectada, los resultados generales y los resultados proyectados si hubieras enviado solo el recorrido ganador. Incluso si no hay mejora, lo cual puede suceder a veces, el resultado es el mismo que enviar solo el recorrido ganador (una prueba A/B tradicional).

- **Mejora proyectada:** La mejora en tu evento de conversión seleccionado gracias al uso de recorridos personalizados en lugar de enviar a todos los usuarios por el recorrido con mejor rendimiento general.
- **Resultados generales:** Los resultados del segundo envío basados en tu evento de conversión.
- **Resultados proyectados:** Los resultados proyectados del segundo envío basados en tu métrica de optimización elegida si hubieras enviado solo la variante ganadora.

![Pestaña de recorridos personalizados para un Canvas. Las tarjetas muestran la mejora proyectada, las conversiones generales (con recorridos personalizados) y las Unique Opens proyectadas (con el recorrido ganador).]({% image_buster /assets/img/experiment_step/experiment_personalized_analytics_tab2.png %})

{% endtab %}
{% endtabs %}

## Uso de recorridos personalizados con entrega según la zona horaria local {#using-personalized-paths-with-local-time-delivery}

No recomendamos usar la entrega según la zona horaria local en Canvas con recorridos personalizados. Esto se debe a que las ventanas de experimento comienzan cuando el primer usuario pasa por ellas. Los usuarios que se encuentran en zonas horarias muy tempranas pueden entrar en el paso y desencadenar el inicio de la ventana del experimento mucho antes de lo que esperas, lo que puede resultar en que el experimento concluya antes de que la mayoría de tus usuarios en zonas horarias más típicas hayan tenido suficiente tiempo para entrar en el Canvas y convertir.

Alternativamente, si deseas usar la entrega local, utiliza una ventana de experimento de 24-48 horas o más. De esa manera, los usuarios en zonas horarias tempranas entran en el Canvas y desencadenan el inicio del experimento, pero queda tiempo suficiente en la ventana del experimento. Los usuarios en zonas horarias más tardías aún tendrán tiempo suficiente para entrar en el Canvas y en el paso de recorrido de experimentos con recorridos personalizados y posiblemente convertir antes de que la ventana del experimento expire.