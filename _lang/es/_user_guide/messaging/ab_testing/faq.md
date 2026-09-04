---
nav_title: Preguntas frecuentes
article_title: Preguntas frecuentes sobre pruebas multivariante y A/B
page_order: 21
page_type: reference
toc_headers: h2
description: "Este artículo cubre las preguntas frecuentes sobre pruebas multivariante y A/B con Braze."
---

# Preguntas frecuentes sobre pruebas multivariante y A/B {#multivariate-and-ab-test-faq}

> Este artículo cubre las preguntas frecuentes sobre pruebas multivariante y A/B con Braze.

## Conceptos básicos de las pruebas {#testing-basics}

### ¿Cuál es la diferencia entre las pruebas A/B y las pruebas multivariante? {#what-is-the-difference-between-ab-testing-and-multivariate-testing}

#### Pruebas A/B {#ab-testing}

En las pruebas A/B, el especialista en marketing experimenta con una única variable dentro de la Campaign (como las líneas del asunto del correo electrónico o la hora de envío del mensaje). Esto implica dividir aleatoriamente un subconjunto de la audiencia en dos o más grupos, presentar a cada grupo una variante diferente y observar cuál exhibe la tasa de conversión más alta. Normalmente, la variante con mejor rendimiento se envía posteriormente al resto de la audiencia.

#### Pruebas multivariante {#multivariate-testing}

Las pruebas multivariante son una extensión de las pruebas A/B, que permiten al especialista en marketing probar múltiples variables a la vez para determinar la combinación más eficaz. Por ejemplo, podrías probar la línea del asunto de tu mensaje de correo electrónico, la imagen que acompaña tu texto y el color del botón de llamada a la acción. Este tipo de prueba te permite explorar más variables y combinaciones de variantes dentro de un solo experimento, y obtener información más rápida y completa que con las pruebas A/B. Sin embargo, probar más variables y combinaciones dentro de un solo experimento requiere una audiencia más grande para alcanzar significación estadística.

### ¿Cómo se calculan los resultados de las pruebas A/B? {#how-are-ab-test-results-calculated}

Braze compara todas las variantes entre sí con pruebas de chi-cuadrado de Pearson, que miden si una variante supera estadísticamente a todas las demás con un nivel de significación de p < 0,05, o lo que denominamos significación del 95 %. Entre todas las variantes que superan este umbral de significación, la variante con mejor rendimiento se determina como la "ganadora".

Esta es una prueba separada de la puntuación de confianza, que solo describe el rendimiento de una variante en comparación con el grupo de control con un valor numérico entre 0 y 100 %. Específicamente, representa nuestra confianza en que la diferencia estandarizada en la tasa de conversión entre la variante y el control es significativamente mayor que el azar.

### ¿Por qué la distribución de variantes no es uniforme? {#why-isnt-the-variant-distribution-even}

La asignación de variantes se aleatoriza en cada envío, por lo que la distribución real puede no coincidir exactamente con los porcentajes configurados, especialmente con tamaños de muestra más pequeños. Para más información, consulta [Distribución de variantes]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/variant_distribution).

## Ejecución y conclusión de pruebas {#running-and-concluding-tests}

### ¿Cuándo termina la prueba inicial? {#when-is-the-initial-test-over}

Para una Campaign de envío único que usa **Optimizar con BrazeAI<sup>TM</sup>**, la prueba inicial termina después de la duración configurada del experimento. BrazeAI<sup>TM</sup> envía entonces la variante con mejor rendimiento a la audiencia restante.

Para Campaigns recurrentes, basadas en acciones y activadas por API que se envían varias veces, **Optimizar con BrazeAI<sup>TM</sup>** realiza un seguimiento continuo del rendimiento de las variantes y redirige el tráfico de la Campaign hacia las variantes con mejor rendimiento.

### ¿Cómo gestiona Braze a los usuarios que recibieron una variante de mensaje en una Campaign recurrente o un paso de entrada de Canvas? {#how-does-braze-handle-users-who-received-a-message-variant-in-a-recurring-campaign-or-canvas-entry-step}

Los usuarios se asignan aleatoriamente a una variante particular antes de recibir la Campaign por primera vez. Cada vez posterior que se recibe la Campaign (o que el usuario vuelve a entrar en una variante en Canvas), reciben la misma variante a menos que se modifiquen los porcentajes de las variantes. Si los porcentajes de las variantes cambian, los usuarios pueden redistribuirse a otras variantes. Los usuarios permanecen en estas variantes hasta que se modifiquen nuevamente los porcentajes. Los usuarios solo se redistribuyen para las variantes que se editaron.

Por ejemplo, supongamos que tenemos una Campaign o Canvas con tres variantes. Si solo se modifican o actualizan la Variante A y la Variante B, los usuarios en la Variante C no se redistribuirán porque el porcentaje de la Variante C no se modificó. Los grupos de control permanecen consistentes si el porcentaje de la variante no cambia. Los usuarios que recibieron mensajes anteriormente no pueden entrar en el grupo de control en un envío posterior, ni ningún usuario en el grupo de control puede recibir un mensaje en ningún momento.

{% alert note %}
Un usuario puede marcarse como que ha "recibido" un mensaje si comparte un identificador de canal (como un correo electrónico o número de teléfono) con alguien que recibió, abrió o hizo clic en el mensaje.
{% endalert %}

#### ¿Y los recorridos de experimentos? {#what-about-experiment-paths}

Lo mismo aplica porque los recorridos en Canvas que siguen a un experimento también son variantes.

#### ¿Puedo tomar acciones para redistribuir usuarios en Campaigns y Canvas? {#can-i-take-actions-to-redistribute-users-in-campaigns-and-canvases}

La única forma de redistribuir usuarios en Canvas es usar [Recorridos aleatorios en recorridos de experimentos]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step#step-1-choose-the-number-of-paths-and-audience-distribution), que siempre asignará los recorridos de forma aleatoria cuando los usuarios vuelvan a entrar en el Canvas. Sin embargo, esto no es un experimento estándar y podría invalidar cualquier resultado del experimento porque el grupo de control puede contaminarse con usuarios del tratamiento.

## Confianza y sesgo {#confidence-and-bias}

### ¿La confianza aumenta con el tiempo? {#does-confidence-increase-over-time}

La confianza aumenta con el tiempo si todo lo demás se mantiene constante. Mantener constante significa que no hay otros factores de marketing que puedan influir en las variantes, como que la variante A hable de una oferta del 25 % de descuento que finalice a mitad de la prueba.

La confianza es una medida de cuán seguro está Braze de que la variante es diferente del grupo de control. A medida que se envían más mensajes, el poder estadístico de la prueba aumenta, lo que incrementaría la confianza de que las diferencias medidas en el rendimiento no se deben al azar. En general, un tamaño de muestra mayor aumenta nuestra confianza para identificar diferencias más pequeñas en el rendimiento entre las variantes y el grupo de control.

Sin embargo, si las tasas de conversión entre las variantes y el grupo de control convergen (se acercan entre sí) a medida que se envían más mensajes, la confianza puede disminuir, porque la diferencia medida que te interesa se está reduciendo, lo que puede superar el beneficio de un tamaño de muestra mayor.

### ¿Pueden las asignaciones a grupos de control y de prueba introducir sesgo en las pruebas? {#can-control-and-test-group-assignments-introduce-bias-to-testing}

No hay ninguna forma práctica de que los atributos o comportamientos de un usuario antes de la creación de una Campaign o Canvas en particular puedan variar de forma sistemática entre las variantes y el grupo de control.

Para asignar usuarios a variantes de mensaje, variantes en Canvas o sus respectivos grupos de control, comenzamos vinculando su ID de usuario generado aleatoriamente con el ID de Campaign o Canvas generado aleatoriamente. A continuación, aplicamos un algoritmo de hash sha256 y dividimos ese resultado entre 100, quedándonos con el resto (también conocido como módulo con 100). Por último, ordenamos a los usuarios en segmentos que corresponden a los porcentajes de asignación para las variantes (y el grupo de control opcional) elegidos en el panel.

### ¿Por qué no puedo usar el límite de velocidad con un grupo de control? {#why-cant-i-use-rate-limiting-with-a-control-group}

Braze actualmente no admite el límite de velocidad con pruebas A/B que tienen un grupo de control. El límite de velocidad no se aplica al grupo de control de la misma manera que a las variantes, lo que introduce sesgo. En su lugar, considera usar [Optimizar con BrazeAI<sup>TM</sup>]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/variant_selection), que ajusta automáticamente el porcentaje de usuarios que reciben cada variante en función del rendimiento de la Campaign.