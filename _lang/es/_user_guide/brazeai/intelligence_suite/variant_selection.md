---
nav_title: Selección de variante
article_title: Selección de variante
page_order: 1.6
description: "Este artículo cubre la selección de variante de BrazeAI<sup>TM</sup>, una característica que permite a tus campañas A/B optimizar automáticamente para obtener la mejor interacción."
search_rank: 10
toc_headers: h2
---

# Selección de variante de BrazeAI<sup>TM</sup> {#variant-selection}

> La selección de variante de BrazeAI<sup>TM</sup> es una característica que permite que tus pruebas A/B de envío único o recurrentes ejecuten automáticamente un experimento y optimicen para obtener los mejores resultados de interacción.

{% alert note %}
La selección de variante de BrazeAI<sup>TM</sup> actualmente solo está disponible para push.
{% endalert %}

## Requisitos previos {#prerequisites}

Para usar la selección de variante de BrazeAI<sup>TM</sup>, necesitas lo siguiente en tu campaña o Canvas:

{% tabs %}
{% tab Campaign %}
- Añade al menos dos variantes de mensaje.
- Si no estás usando envío único, define al menos un evento de conversión y establece tu ventana de reelegibilidad en 24 horas o más. Las ventanas más cortas no son compatibles, ya que afectarían la integridad de la variante de control.
{% endtab %}

{% tab Canvas %}
- Incluye al menos dos variantes de mensaje en un paso de mensaje.
- Si no estás usando envío único, ten al menos un evento de conversión.
{% endtab %}
{% endtabs %}

## Envío único {#single-send}

Después de añadir tu segunda variante, la selección de variante de BrazeAI<sup>TM</sup> se activa automáticamente, estableciendo los parámetros óptimos para el experimento (hemos observado un incremento de ~25 % al seguir los parámetros óptimos), ejecuta tu experimento y luego envía la variante ganadora. No necesitas hacer nada más.

Para personalizar tu experimento, ofrecemos las siguientes opciones de personalización:

### Objetivo de optimización {#optimization-goal}

Recomendamos usar aperturas a menos que tengas una configuración sólida de eventos de conversión con una cantidad significativa de conversiones, para que el algoritmo tenga los datos que necesita para proporcionar los mejores resultados.
- Aperturas
- Eventos de conversión

### Duración del experimento {#experiment-duration}

Recomendamos usar la duración predeterminada; sin embargo, proporcionamos otras dos opciones, incluyendo la posibilidad de usar tu propia duración personalizada:
- 4 horas
- 24 horas
- 72 horas
- Personalizada

### Grupo de control y distribuciones de variantes {#control-group-and-variant-distributions}

Puedes quitar un grupo de control o editar las distribuciones de variantes, pero recomendamos usar los parámetros óptimos que establecemos.

![Opciones de optimización de variantes para envío único]({% image_buster /assets/img_archive/braze_ai_variant_selection_single_send_options.png %})

## Recurrente {#recurring}

Después de añadir tu segunda variante, la selección de variante de BrazeAI<sup>TM</sup> se activa automáticamente y optimiza continuamente utilizando una prueba estadística de bandido multibrazo. Envía más mensajes a las variantes que tienen mejor rendimiento y menos a las que tienen peor rendimiento.

Comienza con una distribución uniforme para entrenar y optimizar, luego dos veces al día inclina la distribución hacia las variantes de alto rendimiento y la aleja de las de bajo rendimiento hasta que reúne suficiente evidencia para sentir confianza (95 %+) de que ha elegido la distribución óptima.

## Informes {#reporting}

![Informes de incremento]({% image_buster /assets/img_archive/braze_ai_variant_selection_reporting.png %}){: style="float:right;max-width:40%;margin-left:15px;border:0"}

Después de que la prueba se completa para envío único, y después de un breve retraso para envío recurrente, tenemos datos confiables para informar. Reportamos cualquier incremento que la selección de variante de BrazeAI<sup>TM</sup> pueda lograr en el dashboard.

{% tabs %}
{% tab Envío único %}
Después de que la cohorte de entrenamiento envía, Braze espera el periodo de tiempo en la configuración de duración y revisa los datos. Basándose en la distribución de las variantes competidoras, calculamos un promedio de cómo sería el rendimiento si no se hubiera realizado ninguna optimización, y luego calculamos el incremento basándonos en la variante ganadora.

Por ejemplo (asumiendo una distribución uniforme):
- Variante 1: 3,5 %
- Variante 2: 3 %
- Variante 3: 2,5 %
- Variante 4: 2 %

La tasa de apertura sin optimización es 2,75 % (.035*.25 + .03*.25 + 0.025*.25 + 0.02*.25), la selección de variante elige la variante 1, 3,5 %, por lo que el incremento es 27,3 %
{% endtab %}

{% tab Recurrente %}
Braze analiza rutinariamente los resultados cuando hacemos ajustes y muestra el incremento basándose en el promedio del incremento de cada periodo.

Calculamos el incremento de los periodos basándonos en cuánto ajustamos, de manera similar al envío único.

Por ejemplo:
- Variante 1: 3,5 %, 25 % de la cohorte
- Variante 2: 3 %, 25 % de la cohorte
- Variante 3: 2,5 %, 25 % de la cohorte
- Variante 4: 2 %, 25 % de la cohorte

La tasa de apertura sin optimización es 2,75 % (.035*.25 + .03*.25 + 0.025*.25 + 0.02*.25). La selección de variante pondera más fuertemente a las de mayor rendimiento.

Digamos que hace lo siguiente:
- Variante 1: 65 %
- Variante 2: 15 %
- Variante 3: 10 %
- Variante 4: 5 %

Esto equivale a una tasa de apertura elegida de 3,075 % (.035*.65 + .03*.15 + 0.025*.1 + 0.02*.05), lo que representa un incremento de 11,8 %. Calculamos eso en cada periodo y luego lo promediamos a lo largo del periodo de optimización.
{% endtab %}
{% endtabs %}

## Preguntas frecuentes {#faq}

### ¿Por qué la reelegibilidad en menos de 24 horas no está disponible cuando se combina con la selección de variante para campañas o Canvas recurrentes? {#why-is-re-eligibility-in-less-than-24-hours-not-available-when-combined-with-variant-selection-for-recurring-campaigns-or-canvases}

No permitimos que las campañas con selección de variante tengan reelegibilidad en una ventana demasiado corta porque nuestras pruebas muestran que afecta la integridad de la variante de control y posiblemente conduce a distribuciones no deseadas.

### ¿Por qué mis variantes muestran envíos iguales durante las primeras etapas de mi campaña recurrente? {#why-are-my-variants-showing-equal-sends-during-the-early-stages-of-my-recurring-campaign}

La selección de variante solo determina las asignaciones finales de variantes después de un periodo de entrenamiento, donde los envíos se distribuyen uniformemente entre las variantes. Se ajusta con el tiempo a medida que nota tendencias de rendimiento. Si no quieres enviar de manera uniforme durante las primeras etapas de tu campaña, usa variantes fijas para una prueba A/B tradicional.

### ¿La selección de variante recurrente deja de optimizar sin elegir un ganador claro? {#does-recurring-variant-selection-stop-optimizing-without-picking-a-clear-winner}

Sí, deja de optimizar cuando tiene un 95 % de confianza en que continuar el experimento no mejorará la tasa de conversión en más de un 1 % de su tasa actual.

### ¿Por qué no puedo habilitar la selección de variante en mi Canvas o campaña? {#why-cant-i-enable-variant-selection-in-my-canvas-or-campaign}

Para envío único, no puedes habilitar la selección de variante si tu Canvas o campaña está compuesto por una sola variante.

Para recurrente, no puedes habilitar la selección de variante si:
- No has añadido eventos de conversión a tu campaña o Canvas.
- Tienes la reelegibilidad habilitada con una ventana de menos de 24 horas.
- Tu Canvas o campaña está compuesto por una sola variante.