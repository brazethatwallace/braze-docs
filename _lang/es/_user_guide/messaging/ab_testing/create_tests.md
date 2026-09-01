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

## Paso 1: Crea tu campaign {#step-1-create-your-campaign}

1. Ve a **Messaging** > **Campaigns**.
2. Selecciona **Create campaign** y un canal para la campaign en la sección que permite pruebas multivariantes y A/B. Para obtener documentación detallada sobre cada canal de mensajería, consulta [Crear una campaign]({{site.baseurl}}/user_guide/messaging/campaigns/creating_campaign).

## Paso 2: Compón tus variantes {#step-2-compose-your-variants}

Puedes crear hasta ocho variantes de tu mensaje, diferenciando entre títulos, contenido, imágenes y más. La cantidad de diferencias entre los mensajes determina si se trata de una prueba multivariante o A/B. Una prueba A/B examina el efecto de cambiar una variable, mientras que una prueba multivariante examina dos o más.

Para obtener algunas ideas sobre cómo empezar a diferenciar tus variantes, consulta [Consejos para diferentes canales](#tips-different-channels).

![Selección de "Add Variant" para una Campaign.]({% image_buster /assets/img/ab_create_2.png %})

## Paso 3: Programa tu campaña {#step-3-schedule-your-campaign}

Programar tu campaña multivariante funciona igual que programar cualquier otra campaña de Braze. Todos los [tipos de entrega]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/delivery_and_entry_types) estándar están disponibles.

Una vez que comienza una prueba multivariante, no puedes realizar cambios en la campaña. Si cambias los parámetros, como la línea del asunto o el cuerpo HTML, Braze considera que el experimento está comprometido y lo desactiva de inmediato.

Para optimizar automáticamente tus variantes, consulta [Optimización de pruebas A/B con BrazeAI]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/variant_selection). Las Campaigns de envío único y de envío múltiple utilizan métodos y requisitos de optimización diferentes.

## Paso 4: Elige un segmento y distribuye a tus usuarios entre variantes {#step-4-choose-a-segment-and-distribute-your-users-across-variants}

Selecciona los segmentos a los que deseas dirigirte y luego distribuye a los miembros entre las variantes seleccionadas y el [grupo de control](#including-a-control-group) opcional. Para conocer las mejores prácticas sobre cómo elegir un segmento con el que realizar pruebas, consulta [Elegir un segmento](#choosing-a-segment).

En las campañas compatibles, activa **Optimizar con BrazeAI<sup>TM</sup>** para optimizar automáticamente la distribución de variantes. Para una Campaign de envío único, Braze reserva parte de la audiencia para un segundo envío optimizado. Para una Campaign de envío múltiple, BrazeAI<sup>TM</sup> ajusta la distribución a lo largo del tiempo.

### Grupo de control {#including-a-control-group}

Puedes reservar un porcentaje de tu público objetivo para un grupo de control aleatorio. Los usuarios del grupo de control no reciben la prueba, pero Braze monitorea su tasa de conversión durante la duración de la Campaign.

Cuando revises tus resultados, puedes comparar las tasas de conversión de tus variantes con una tasa de conversión de referencia proporcionada por tu grupo de control. Esto te permite comparar tanto los efectos de tus variantes como los efectos de tus variantes frente a la tasa de conversión que resultaría si no enviaras ningún mensaje.

![Panel de pruebas A/B que muestra el desglose porcentual del grupo de control, la variante 1, la variante 2 y la variante 3, con un 25 % para cada grupo.]({% image_buster /assets/img/ab_create_4.png %})

{% alert important %}
No se recomienda usar un grupo de control para determinar un ganador por _aperturas_ o _clics_. Dado que el grupo de control no recibe el mensaje, esos usuarios no pueden realizar aperturas ni clics. Por lo tanto, la tasa de conversión de ese grupo es del 0 % por definición y no constituye una comparación significativa con las variantes.
{% endalert %}

#### Grupos de control y pruebas A/B {#control-groups-and-ab-testing}

Cuando utilices un límite de velocidad con una prueba A/B, el límite de velocidad no se aplica al grupo de control de la misma manera que al grupo de prueba, lo cual es una posible fuente de sesgo temporal. Usa ventanas de conversión apropiadas para evitar este sesgo.

#### Grupos de control con Optimizar con BrazeAI<sup>TM</sup> {#control-groups-with-optimize-with-brazeai}

Para una Campaign de envío múltiple con [Optimizar con BrazeAI<sup>TM</sup>]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/variant_selection), el tamaño inicial del grupo de control depende del número de variantes. Si cada variante recibe más del 20 % de los usuarios, el grupo de control comienza en el 20 % y las variantes dividen el 80 % restante de manera equitativa. Con más variantes, el grupo de control comienza siendo más pequeño. A medida que BrazeAI<sup>TM</sup> analiza el rendimiento, el grupo de control puede crecer o reducirse.

## Paso 5: Designa un evento de conversión (opcional) {#step-5-designate-a-conversion-event-optional}

Configurar un evento de conversión para una Campaign te permite ver cuántos destinatarios de esa Campaign realizaron una acción determinada después de recibirla.

Esto solo afecta la prueba si elegiste **Tasa de conversión primaria** en los pasos anteriores. Para obtener más información, consulta [Eventos de conversión]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events).

## Paso 6: Revisar y lanzar {#step-6-review-and-launch}

En la página de confirmación, revisa los detalles de tu Campaign multivariante y lanza la prueba. A continuación, aprende a [comprender los resultados de tu prueba]({{site.baseurl}}/user_guide/messaging/ab_testing/analytics).

## Cosas que debes saber {#things-to-know}

Si tu experimento ya ha comenzado a enviarse y editas el mensaje, el experimento queda invalidado y los resultados del experimento se eliminan.

- Para evitar cualquier interferencia con el comportamiento esperado del experimento, te recomendamos no editar los mensajes dentro de la hora siguiente al lanzamiento de la Campaign del experimento.
- Si tu experimento ha finalizado y editas el mensaje después del envío, los resultados del experimento permanecen disponibles en los análisis de tu panel. Sin embargo, si relanzas la Campaign, los resultados del experimento se eliminan.

### Consejos para diferentes canales {#tips-different-channels}

Según el canal que selecciones, puedes probar diferentes componentes de tu mensaje. Por ejemplo, puedes intentar componer variantes con una idea de lo que quieres probar y lo que esperas demostrar. ¿Qué palancas tienes a tu disposición y cuáles son los efectos deseados? Aunque hay millones de posibilidades que puedes investigar mediante pruebas multivariantes y A/B, tenemos algunas sugerencias para empezar:

| Canal | Aspectos del mensaje que puedes cambiar | Resultados a buscar |
| ---------------------| --------------- | ------------- |
| Push | Texto <br> Uso de imágenes y emojis <br> Vínculos profundos <br> Presentación de números (por ejemplo, "triple" frente a "aumenta un 200 %") <br> Presentación del tiempo (por ejemplo, "termina a medianoche" frente a "termina en 6 horas") | Aperturas <br> Tasa de conversión |
| Correo electrónico | Asunto <br> Nombre de remitente <br> Saludo <br> Cuerpo del texto <br> Uso de imágenes y emojis <br> Presentación de números (por ejemplo, "triple" frente a "aumenta un 200 %") <br> Presentación del tiempo (por ejemplo, "termina a medianoche" frente a "termina en 6 horas") | Aperturas <br> Tasa de conversión |
| Mensaje dentro de la aplicación | Aspectos enumerados para "push" <br> [Especificaciones de imagen de mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library#image-specifications) | Clic <br> Tasa de conversión |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Consejos para diferentes canales" }

{% alert tip %}
Al ejecutar pruebas A/B, no olvides generar [informes de embudo]({{site.baseurl}}/user_guide/analytics/reports/funnel_reports) que te permitan comprender cómo cada variante impactó tu embudo de conversión, especialmente si la "conversión" para tu negocio implica tomar múltiples pasos o acciones.
{% endalert %}

Además, la duración ideal de tu prueba también puede variar según el canal. Ten en cuenta la cantidad promedio de tiempo que la mayoría de los usuarios pueden necesitar para interactuar con cada canal.

Por ejemplo, si estás probando un push, puedes obtener resultados significativos más rápido que al probar un correo electrónico, ya que los usuarios ven los push inmediatamente, pero pueden pasar días antes de que vean o abran un correo electrónico. Si estás probando mensajes dentro de la aplicación, ten en cuenta que los usuarios deben abrir la aplicación para ver la Campaign, por lo que deberías esperar más tiempo para recopilar resultados tanto de tus usuarios que abren la aplicación con más frecuencia como de tus usuarios más típicos.

Si no estás seguro de cuánto tiempo debe durar tu prueba, [Optimizar con BrazeAI<sup>TM</sup>]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/variant_selection) puede configurar y ejecutar automáticamente la optimización.

### Elegir un Segment {#choosing-a-segment}

Dado que diferentes Segments de tus usuarios pueden responder de manera diferente a la mensajería, el éxito de un mensaje en particular dice algo tanto sobre el mensaje en sí como sobre su Segment objetivo. Por lo tanto, intenta diseñar una prueba teniendo en cuenta tu Segment objetivo.

Por ejemplo, mientras que los usuarios activos pueden tener tasas de respuesta iguales a "¡Esta oferta expira mañana!" y "¡Esta oferta expira en 24 horas!", los usuarios que no han abierto la aplicación en una semana pueden ser más receptivos al segundo texto, ya que crea una mayor sensación de urgencia.

Además, al elegir en qué Segment ejecutar tu prueba, asegúrate de considerar si el tamaño de ese Segment es lo suficientemente grande para tu prueba. En general, las pruebas multivariantes y A/B con más variantes requieren un grupo de prueba más grande para obtener resultados estadísticamente significativos. Esto se debe a que más variantes resultan en menos usuarios viendo cada variante individual.

{% alert tip %}
Como guía, probablemente necesites alrededor de 15.000 usuarios por variante (incluido el grupo de control) para lograr un 95 % de confianza en los resultados de tu prueba. Sin embargo, la cantidad exacta de usuarios que necesitas podría ser mayor o menor, dependiendo de tu caso particular. Para una orientación más exacta sobre los tamaños de muestra de variantes, considera consultar una [calculadora de tamaño de muestra](https://www.calculator.net/sample-size-calculator.html).
{% endalert %}

### Sesgo y aleatorización {#bias-and-randomization}

Una pregunta común sobre las asignaciones de grupos de control y de prueba es si pueden introducir sesgo en tus pruebas. Otros a veces se preguntan cómo sabemos si estas asignaciones son realmente aleatorias.

Los usuarios se asignan a variantes de mensaje, variantes en Canvas o sus respectivos grupos de control concatenando su ID de usuario (generado aleatoriamente) con el ID de Campaign o Canvas (generado aleatoriamente), tomando el módulo de ese valor con 100 y luego ordenando a los usuarios en segmentos que corresponden a las asignaciones de porcentaje para las variantes y el control opcional elegido en el panel. Por lo tanto, no hay forma práctica de que los comportamientos de los usuarios antes de crear una Campaign o Canvas particular puedan variar sistemáticamente entre variantes y control. Tampoco es práctico ser más aleatorio (o más exactamente, pseudoaleatorio) que esta implementación.

#### Errores que debes evitar {#mistakes-to-avoid}

Hay algunos errores comunes que debes evitar para no crear la apariencia de diferencias basadas en el canal de mensajería si las audiencias no se filtran correctamente.

Por ejemplo, si envías un mensaje push a una audiencia amplia con un grupo de control, el grupo de prueba envía mensajes solo a los usuarios con un token de notificaciones push. Sin embargo, el grupo de control incluye tanto a los usuarios que tienen un token de notificaciones push como a los que no. En este caso, tu audiencia inicial para la Campaign o Canvas debe filtrar por tener un token de notificaciones push (`Foreground Push Enabled` es `true`). Lo mismo debe hacerse para la elegibilidad de recibir mensajes en otros canales: que hayan dado su consentimiento, que tengan un token de notificaciones push o que estén suscritos.

Ten en cuenta que si una variante de control no contiene ningún paso en Canvas, los eventos de criterios de salida no se registran para los usuarios en la variante de control.

{% alert note %}
Si usas manualmente números de contenedor aleatorio para grupos de control, consulta los [aspectos a tener en cuenta]({{site.baseurl}}/user_guide/audience/global_control_group#things-to-watch-for) en tus grupos de control.
{% endalert %}