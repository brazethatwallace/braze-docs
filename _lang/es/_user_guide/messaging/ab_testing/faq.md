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

En las pruebas A/B, el especialista en marketing experimenta con una sola variable dentro de la campaña (como la línea del asunto del correo electrónico o la hora de envío del mensaje). Esto implica dividir aleatoriamente un subconjunto de la audiencia en dos o más grupos, presentar a cada grupo una variación diferente y observar cuál exhibe la tasa de conversión más alta. Normalmente, la variación con mejor rendimiento se envía posteriormente al resto de la audiencia.

#### Pruebas multivariante {#multivariate-testing}

Las pruebas multivariante son una extensión de las pruebas A/B, que permiten al especialista en marketing probar múltiples variables a la vez para determinar la combinación más efectiva. Por ejemplo, podrías probar la línea del asunto de tu correo electrónico, la imagen que acompaña tu texto y el color del botón CTA. Este tipo de prueba te permite explorar más variables y combinaciones de variaciones dentro de un solo experimento, y obtener información más rápida y completa que con las pruebas A/B. Sin embargo, probar más variables y combinaciones dentro de un solo experimento requiere una audiencia más grande para lograr significancia estadística.

### ¿Cómo se calculan los resultados de las pruebas A/B? {#how-are-ab-test-results-calculated}

Braze compara todas las variantes entre sí con pruebas chi-cuadrado de Pearson, que miden si una variante supera estadísticamente a todas las demás con un nivel de significancia de p < 0,05, o lo que denominamos significancia del 95 %. Entre todas las variantes que superan este umbral de significancia, la variante con mejor rendimiento se determina como la "ganadora".

Esta es una prueba separada de la puntuación de confianza, que solo describe el rendimiento de una variante en comparación con el grupo de control con un valor numérico entre 0 y 100 %. Específicamente, representa nuestra confianza en que la diferencia estandarizada en la tasa de conversión entre la variante y el control es significativamente mayor que el azar.

### ¿Por qué la distribución de variantes no es uniforme? {#why-isnt-the-variant-distribution-even}

La asignación de variantes se aleatoriza en cada envío, por lo que la distribución real puede no coincidir exactamente con los porcentajes configurados, especialmente con tamaños de muestra más pequeños. Para más información, consulta [Distribución de variantes]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/variant_distribution/).

## Ejecución y conclusión de pruebas {#running-and-concluding-tests}

### ¿Cuándo termina la prueba inicial? {#when-is-the-initial-test-over}

Cuando se usa la variante ganadora para campañas de envío único, la prueba termina cuando llega la hora de envío de la variante ganadora. Braze considerará que una variante es la ganadora si muestra la tasa de conversión más alta con un margen estadísticamente significativo.

Para campañas recurrentes, basadas en acciones y desencadenadas por API, puedes usar Intelligent Selection para rastrear continuamente los datos de rendimiento de cada variante y optimizar continuamente el tráfico de la campaña hacia las variantes con mejor rendimiento. Con Intelligent Selection, en lugar de definir explícitamente un grupo de experimento donde los usuarios reciben variantes aleatorias, el algoritmo de Braze refinará continuamente su estimación de la variante con mejor rendimiento, lo que potencialmente permite una selección más rápida del mejor resultado.

### ¿Cómo maneja Braze a los usuarios que recibieron una variante de mensaje en una campaña recurrente o un paso de entrada de Canvas? {#how-does-braze-handle-users-who-received-a-message-variant-in-a-recurring-campaign-or-canvas-entry-step}

Los usuarios se asignan aleatoriamente a una variante particular antes de recibir la campaña por primera vez. Cada vez sucesiva que se recibe la campaña (o el usuario vuelve a entrar en una variante de Canvas), reciben la misma variante a menos que se modifiquen los porcentajes de variantes. Si los porcentajes de variantes cambian, los usuarios pueden ser redistribuidos a otras variantes. Los usuarios permanecen en estas variantes hasta que los porcentajes se modifiquen nuevamente. Los usuarios solo se redistribuyen para las variantes que fueron editadas.

Por ejemplo, supongamos que tenemos una campaña o Canvas con tres variantes. Si solo se cambian o actualizan la variante A y la variante B, los usuarios de la variante C no serán redistribuidos porque el porcentaje de la variante C no cambió. Los grupos de control permanecen consistentes si el porcentaje de variante no cambia. Los usuarios que previamente recibieron mensajes no pueden entrar en el grupo de control en un envío posterior, ni ningún usuario en el grupo de control puede recibir un mensaje.

{% alert note %}
Un usuario puede ser marcado como que "recibió" un mensaje si comparte un identificador de canal (como un correo electrónico o número de teléfono) con alguien que recibió, abrió o hizo clic en el mensaje.
{% endalert %}

#### ¿Qué pasa con los recorridos de experimentos? {#what-about-experiment-paths}

Lo mismo aplica porque los recorridos de Canvas que siguen a un experimento también son variantes.

#### ¿Puedo tomar acciones para redistribuir usuarios en campañas y Canvas? {#can-i-take-actions-to-redistribute-users-in-campaigns-and-canvases}

La única forma de redistribuir usuarios en Canvas es usar [Recorridos aleatorios en recorridos de experimentos]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step/#step-1-choose-the-number-of-paths-and-audience-distribution), que siempre aleatorizará las asignaciones de recorridos cuando los usuarios vuelvan a entrar en el Canvas. Sin embargo, esto no es un experimento estándar y podría invalidar cualquier resultado del experimento porque el grupo de control puede contaminarse con usuarios del tratamiento.

## Confianza y sesgo {#confidence-and-bias}

### ¿La confianza aumenta con el tiempo? {#does-confidence-increase-over-time}

La confianza aumenta con el tiempo si todo lo demás se mantiene constante. Mantener constante significa que no hay otros factores de marketing que puedan influir en las variantes, como que la variante A hable de una oferta del 25 % de descuento que termina a mitad de la prueba.

La confianza es una medida de cuán seguro está Braze de que la variante es diferente del control. A medida que se envían más mensajes, el poder estadístico de la prueba aumenta, lo que incrementaría la confianza en que las diferencias medidas en el rendimiento no se deben al azar. Generalmente, un tamaño de muestra más grande aumenta nuestra confianza para identificar diferencias más pequeñas en el rendimiento entre variantes y control.

### ¿Pueden las asignaciones de grupo de control y prueba introducir sesgo en las pruebas? {#can-control-and-test-group-assignments-introduce-bias-to-testing}

No hay una forma práctica en que los atributos o comportamientos de un usuario antes de la creación de una campaña o Canvas particular puedan variar sistemáticamente entre variantes y control.

Para asignar usuarios a variantes de mensaje, variantes de Canvas o sus respectivos grupos de control, comenzamos vinculando su ID de usuario generado aleatoriamente con el ID de campaña o Canvas generado aleatoriamente. Luego, aplicamos un algoritmo de hash sha256 y dividimos ese resultado entre 100, quedándonos con el residuo (también conocido como módulo con 100). Finalmente, ordenamos a los usuarios en segmentos que corresponden a las asignaciones de porcentaje para variantes (y control opcional) elegidas en el dashboard.

### ¿Por qué no puedo usar límites de velocidad con un grupo de control? {#why-cant-i-use-rate-limiting-with-a-control-group}

Braze actualmente no admite límites de velocidad con pruebas A/B que tienen un grupo de control. Esto se debe a que los límites de velocidad no se aplican al grupo de control de la misma manera que a las variantes, lo que introduce sesgo. En su lugar, considera usar [Intelligent Selection]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_selection/), que ajusta automáticamente el porcentaje de usuarios que recibirán cada variante basándose en los análisis y el rendimiento de la campaña.