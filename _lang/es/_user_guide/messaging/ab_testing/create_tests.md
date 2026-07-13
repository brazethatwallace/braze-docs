---
nav_title: Crear pruebas
article_title: Crear pruebas
page_order: 1
page_type: reference
description: "Este artículo explica cómo crear pruebas multivariantes y pruebas A/B con Braze."

local_redirect: #optimizations
  optimizations: '/docs/user_guide/messaging/ab_testing/optimizations'
---

# Crear pruebas multivariantes y pruebas A/B {#creating-tests}

> Puedes crear una prueba multivariante o A/B para cualquier campaña que se dirija a un solo canal. Por ejemplo, si quieres usar pruebas multivariantes o A/B para una campaña push, puedes dirigirte a dispositivos iOS y Android en la misma campaña.

![El menú desplegable que aparece al seleccionar el botón "Crear campaña" para elegir entre multicanal o canal único.]({% image_buster /assets/img/ab_create_1.png %}){: style="max-width:25%;float:right;margin-left:15px;" }

## Paso 1: Crea tu campaña {#step-1-create-your-campaign}

1. Ve a **Mensajería** > **Campaigns**.
2. Selecciona **Crear campaña** y un canal para la campaña en la sección que permite pruebas multivariantes y A/B. Para documentación detallada sobre cada canal de mensajería, consulta [Crear una campaña]({{site.baseurl}}/user_guide/messaging/campaigns/creating_campaign).

## Paso 2: Redacta tus variantes {#step-2-compose-your-variants}

Puedes crear hasta ocho variantes de tu mensaje, diferenciando entre títulos, contenido, imágenes y más. El número de diferencias entre los mensajes determina si se trata de una prueba multivariante o A/B. Una prueba A/B examina el efecto de cambiar una variable, mientras que una prueba multivariante examina dos o más.

Para obtener ideas sobre cómo empezar a diferenciar tus variantes, consulta [Consejos para diferentes canales](#tips-different-channels).

![Seleccionar "Añadir variante" para una campaña.]({% image_buster /assets/img/ab_create_2.png %})

## Paso 3: Planifica tu campaña {#step-3-schedule-your-campaign}

Planificar tu campaña multivariante funciona igual que planificar cualquier otra campaña de Braze. Todos los [tipos de entrega]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/delivery_and_entry_types) estándar están disponibles.

Una vez que comienza una prueba multivariante, no puedes hacer cambios en la campaña. Si cambias los parámetros, como la línea del asunto o el cuerpo HTML, Braze considera que el experimento está comprometido y lo desactiva inmediatamente.

{% alert important %}
Para usar una [optimización]({{site.baseurl}}/user_guide/messaging/ab_testing/optimizations) (disponible para canales seleccionados), planifica tu campaña para que se entregue una sola vez. Las optimizaciones no están disponibles para campañas que se repiten o que tienen la reelegibilidad activada.
{% endalert %}

## Paso 4: Elige un segmento y distribuye a tus usuarios entre variantes {#step-4-choose-a-segment-and-distribute-your-users-across-variants}

Selecciona los segmentos a los que dirigirte y luego distribuye a los miembros entre las variantes seleccionadas y el [grupo de control](#including-a-control-group) opcional. Para conocer las mejores prácticas sobre cómo elegir un segmento para las pruebas, consulta [Elegir un segmento](#choosing-a-segment).

Para campañas push, de correo electrónico y webhook planificadas para enviarse una sola vez, también puedes usar una [optimización]({{site.baseurl}}/user_guide/messaging/ab_testing/optimizations). Una optimización reserva una parte de tu audiencia objetivo de la prueba A/B y la retiene para un segundo envío optimizado basado en los resultados de la primera prueba.

### Grupo de control {#including-a-control-group}

Puedes reservar un porcentaje de tu audiencia objetivo para un grupo de control aleatorio. Los usuarios del grupo de control no reciben la prueba, pero Braze monitorea su tasa de conversión durante la duración de la campaña.

Al ver tus resultados, puedes comparar las tasas de conversión de tus variantes con una tasa de conversión de referencia proporcionada por tu grupo de control. Esto te permite comparar tanto los efectos de tus variantes como los efectos de tus variantes frente a la tasa de conversión que resultaría si no enviaras ningún mensaje.

![Panel de pruebas A/B que muestra el desglose porcentual del grupo de control, variante 1, variante 2 y variante 3 con un 25 % para cada grupo.]({% image_buster /assets/img/ab_create_4.png %})

{% alert important %}
No se recomienda usar un grupo de control al determinar un ganador por _aperturas_ o _clics_. Dado que el grupo de control no recibirá el mensaje, esos usuarios no pueden realizar ninguna apertura ni clic. Por lo tanto, la tasa de conversión de ese grupo es del 0 % por definición y no constituye una comparación significativa con las variantes.
{% endalert %}

#### Grupos de control y pruebas A/B {#control-groups-and-ab-testing}

Al usar un límite de velocidad con una prueba A/B, el límite de velocidad no se aplica al grupo de control de la misma manera que al grupo de prueba, lo cual es una fuente potencial de sesgo temporal. Usa ventanas de conversión apropiadas para evitar este sesgo.

#### Grupos de control con Intelligent Selection {#control-groups-with-intelligent-selection}

El tamaño del grupo de control para una campaña con [Intelligent Selection]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_selection) se basa en el número de variantes. Si cada variante se envía a más del 20 % de los usuarios, entonces el grupo de control es del 20 % y las variantes se dividen equitativamente en el 80 % restante. Sin embargo, si tienes suficientes variantes como para que cada una se envíe a menos del 20 % de los usuarios, entonces el grupo de control debe reducirse. Cuando Intelligent Selection comienza a analizar el rendimiento de tu prueba, el grupo de control crece o se reduce en función de los resultados.

## Paso 5: Designa un evento de conversión (opcional) {#step-5-designate-a-conversion-event-optional}

Configurar un evento de conversión para una campaña te permite ver cuántos destinatarios de esa campaña realizaron una acción particular después de recibirla.

Esto solo afecta a la prueba si elegiste **Primary Conversion Rate** en los pasos anteriores. Para más información, consulta [Eventos de conversión]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events).

## Paso 6: Revisa y lanza {#step-6-review-and-launch}

En la página de confirmación, revisa los detalles de tu campaña multivariante y lanza la prueba. A continuación, aprende cómo [entender los resultados de tu prueba]({{site.baseurl}}/user_guide/messaging/ab_testing/analytics).

## Cosas que debes saber {#things-to-know}

Si tu experimento ya ha comenzado a enviarse y editas el mensaje, el experimento queda invalidado y se eliminan todos los resultados del experimento.

- Para evitar cualquier interferencia con el comportamiento esperado del experimento, te recomendamos no editar los mensajes dentro de la hora posterior al lanzamiento de la campaña del experimento.
- Si tu experimento está completado y editas el mensaje después del envío, los resultados del experimento permanecen disponibles en el análisis de tu panel. Sin embargo, si relanzas la campaña, los resultados del experimento se eliminan.

### Consejos para diferentes canales {#tips-different-channels}

Dependiendo del canal que selecciones, puedes probar diferentes componentes de tu mensaje. Por ejemplo, puedes intentar redactar variantes con una idea de lo que quieres probar y lo que esperas demostrar. ¿Qué palancas puedes mover y cuáles son los efectos deseados? Aunque hay millones de posibilidades que puedes investigar usando pruebas multivariantes y A/B, aquí tienes algunas sugerencias para empezar:

| Canal | Aspectos del mensaje que puedes cambiar | Resultados a buscar |
| ---------------------| --------------- | ------------- |
| Push | Texto <br> Uso de imágenes y emojis <br> Vínculos profundos <br> Presentación de números (por ejemplo, "triple" versus "aumento del 200 %") <br> Presentación del tiempo (por ejemplo, "termina a medianoche" versus "termina en 6 horas") | Aperturas <br> Tasa de conversión |
| Correo electrónico | Asunto <br> Nombre para mostrar <br> Saludo <br> Cuerpo del texto <br> Uso de imágenes y emojis <br> Presentación de números (por ejemplo, "triple" versus "aumento del 200 %") <br> Presentación del tiempo (por ejemplo, "termina a medianoche" versus "termina en 6 horas") | Aperturas <br> Tasa de conversión |
| Mensaje dentro de la aplicación | Aspectos listados para "push" <br> [Especificaciones de imagen para mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library#in-app-messages) | Clic <br> Tasa de conversión |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Consejos para diferentes canales" }

{% alert tip %}
Al ejecutar pruebas A/B, no olvides generar [informes de embudo]({{site.baseurl}}/user_guide/analytics/reports/funnel_reports) que te permitan entender cómo cada variante impactó tu embudo de conversión, especialmente si la "conversión" para tu negocio implica realizar múltiples pasos o acciones.
{% endalert %}

Además, la duración ideal de tu prueba también puede variar según el canal. Ten en cuenta la cantidad promedio de tiempo que la mayoría de los usuarios pueden necesitar para interactuar con cada canal.

Por ejemplo, si estás probando un push, puedes obtener resultados significativos más rápido que al probar un correo electrónico, ya que los usuarios ven las notificaciones push de inmediato, pero pueden pasar días antes de que vean o abran un correo electrónico. Si estás probando mensajes dentro de la aplicación, ten en cuenta que los usuarios deben abrir la aplicación para ver la campaña, por lo que deberías esperar más tiempo para recopilar resultados tanto de los usuarios que abren la aplicación con más frecuencia como de los usuarios más típicos.

Si no estás seguro de cuánto tiempo debe durar tu prueba, la función [Intelligent Selection]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_selection) puede ser útil para encontrar una variante ganadora de manera eficiente.

### Elegir un segmento {#choosing-a-segment}

Dado que diferentes segmentos de tus usuarios pueden responder de manera diferente a los mensajes, el éxito de un mensaje particular dice algo tanto sobre el mensaje en sí como sobre su segmento objetivo. Por lo tanto, intenta diseñar una prueba teniendo en cuenta tu segmento objetivo.

Por ejemplo, mientras que los usuarios activos pueden tener tasas de respuesta iguales a "¡Esta oferta expira mañana!" y "¡Esta oferta expira en 24 horas!", los usuarios que no han abierto la aplicación en una semana pueden ser más receptivos a la segunda redacción, ya que crea una mayor sensación de urgencia.

Además, al elegir en qué segmento ejecutar tu prueba, asegúrate de considerar si el tamaño de ese segmento es lo suficientemente grande para tu prueba. En general, las pruebas multivariantes y A/B con más variantes requieren un grupo de prueba más grande para obtener resultados estadísticamente significativos. Esto se debe a que más variantes resultan en menos usuarios viendo cada variante individual.

{% alert tip %}
Como guía, probablemente necesites alrededor de 15 000 usuarios por variante (incluyendo el grupo de control) para lograr un 95 % de confianza en los resultados de tu prueba. Sin embargo, el número exacto de usuarios que necesitas podría ser mayor o menor, dependiendo de tu caso particular. Para una orientación más precisa sobre los tamaños de muestra de las variantes, considera consultar una [calculadora de tamaño de muestra](https://www.calculator.net/sample-size-calculator.html).
{% endalert %}

### Sesgo y aleatorización {#bias-and-randomization}

Una pregunta común sobre las asignaciones de grupos de control y de prueba es si pueden introducir sesgo en tus pruebas. Otros a veces se preguntan cómo sabemos si estas asignaciones son verdaderamente aleatorias.

Los usuarios se asignan a variantes de mensaje, variantes en Canvas o sus respectivos grupos de control concatenando su ID de usuario (generado aleatoriamente) con el ID de la campaña o Canvas (generado aleatoriamente), tomando el módulo de ese valor con 100 y luego ordenando a los usuarios en segmentos que corresponden a las asignaciones de porcentaje para las variantes y el control opcional elegidos en el panel. Por lo tanto, no hay una forma práctica en que los comportamientos de los usuarios antes de crear una campaña o Canvas particular puedan variar sistemáticamente entre variantes y control. Tampoco es práctico ser más aleatorio (o más precisamente, pseudoaleatorio) que esta implementación.

#### Errores a evitar {#mistakes-to-avoid}

Hay algunos errores comunes que debes evitar para no crear la apariencia de diferencias basadas en el canal de mensajería si las audiencias no se filtran correctamente.

Por ejemplo, si envías un mensaje push a una audiencia amplia con un grupo de control, el grupo de prueba envía mensajes solo a usuarios con un token de notificaciones push. Sin embargo, el grupo de control incluye tanto a usuarios que tienen un token de notificaciones push como a usuarios que no lo tienen. En este caso, tu audiencia inicial para la campaña o Canvas debe filtrar por tener un token de notificaciones push (`Foreground Push Enabled` es `true`). Lo mismo debe hacerse para la elegibilidad de recibir mensajes en otros canales: estar suscrito, tener un token de notificaciones push o estar registrado.

Ten en cuenta que si una variante de control no contiene ningún paso en Canvas, los eventos de criterios de salida no se registran para los usuarios en la variante de control.

{% alert note %}
Si usas manualmente números de contenedor aleatorio para grupos de control, consulta [cosas a tener en cuenta]({{site.baseurl}}/user_guide/audience/global_control_group#things-to-watch-for) en tus grupos de control.
{% endalert %}