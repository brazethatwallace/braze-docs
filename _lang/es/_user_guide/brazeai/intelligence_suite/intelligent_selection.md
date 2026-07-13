---
nav_title: Intelligent Selection
article_title: Intelligent Selection
page_order: 1.0
description: "Este artículo trata sobre Intelligent Selection, una característica que analiza el rendimiento de una campaña recurrente o Canvas dos veces al día y ajusta automáticamente el porcentaje de usuarios que reciben cada variante de mensaje."
search_rank: 10
toc_headers: h2
---

# Intelligent Selection {#intelligent-selection}

> Intelligent Selection es una característica que analiza el rendimiento de una campaña recurrente o Canvas dos veces al día y ajusta automáticamente el porcentaje de usuarios que reciben cada variante de mensaje.

## Requisitos previos {#prerequisites}

{% tabs %}
{% tab Campaign %}
Antes de añadir Intelligent Selection a tu campaña, asegúrate de haberlo configurado todo correctamente:

- Tu campaña se envía según un calendario periódico. No se admiten las campañas de envío único.
- Has añadido al menos dos variantes de mensaje.
- Has definido un evento de conversión para medir el rendimiento entre las distintas variantes.
- La ventana de reelegibilidad se ha fijado en 24 horas o más. No se admiten ventanas más cortas, ya que afectarían a la integridad de la variante de control. Para obtener más información, consulta [estas preguntas frecuentes]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_selection#why-is-re-eligibility-in-less-than-24-hours-not-available-when-combined-with-intelligent-selection).
{% endtab %}

{% tab Canvas %}
Para utilizar Intelligent Selection en un Canvas, confirma lo siguiente:
- Tu Canvas incluye al menos dos variantes de mensaje en un paso de mensaje.
- Has añadido al menos un evento de conversión.
{% endtab %}
{% endtabs %}

## Acerca de Intelligent Selection {#about-intelligent-selection}

Una variante que parezca rendir más que las demás se enviará a más usuarios, mientras que las variantes de bajo rendimiento se dirigirán a menos usuarios. Cada ajuste se realiza mediante un [algoritmo estadístico](https://en.wikipedia.org/wiki/Multi-armed_bandit) que garantiza que Braze se adapta a las diferencias reales de rendimiento y no solo al azar.

![Sección de pruebas A/B de una campaña con Intelligent Selection habilitada.]({% image_buster /assets/img/intelligent_selection1.png %})

Intelligent Selection:
- Observa repetidamente los datos de rendimiento y desplaza gradualmente el tráfico de la campaña hacia las variantes ganadoras.
- Comprueba que más usuarios reciben tu variante de mejor rendimiento sin sacrificar la confianza estadística.
- Descarta las variantes de bajo rendimiento e identifica las de alto rendimiento más rápidamente que con una [prueba A/B tradicional]({{site.baseurl}}/user_guide/messaging/ab_testing).
- Realiza pruebas con más frecuencia y con mayor seguridad de que tus usuarios verán tu mejor mensaje.

Intelligent Selection funciona mejor en campañas que se envían más de una vez. Necesita datos de rendimiento iniciales para empezar a optimizar, por lo que las campañas de envío único no se beneficiarán de ello. Para esas campañas, recomendamos utilizar una [prueba A/B]({{site.baseurl}}/user_guide/messaging/ab_testing) tradicional.

Puedes añadir Intelligent Selection a tus campañas y Canvas.

{% tabs %}
{% tab Campaign %}
Intelligent Selection puede añadirse a cualquier campaña multienvío en el paso **Target Audiences** del compositor de campañas de Braze. Las campañas que solo se envían una vez no pueden aprovechar esta característica.

{% alert note %}
Intelligent Selection no se puede utilizar en campañas con un periodo de reelegibilidad inferior a 24 horas, ya que afectaría a la integridad de la variante de control. Para obtener más información, consulta las [preguntas frecuentes sobre inteligencia]({{site.baseurl}}/user_guide/brazeai/intelligence/faqs#why-is-re-eligibility-in-less-than-24-hours-not-available-when-combined-with-intelligent-selection).
{% endalert %}
{% endtab %}

{% tab Canvas %}
Añade al menos un evento de conversión y dos variantes a tu Canvas. A continuación, selecciona uno de los porcentajes de variantes en el paso de compilación.

![Un Canvas con dos variantes, cada una ajustada al 50 % de distribución de variantes, que permite habilitar Intelligent Selection.]({% image_buster /assets/img/intelligent_selection.png %})

Esto te permite editar la distribución de variantes y activar Intelligent Selection.

![Opción de Intelligent Selection activada para un Canvas.]({% image_buster /assets/img_archive/canvas_intelligent_selection.png %})

Intelligent Selection no estará disponible si aún no has añadido eventos de conversión a tu Canvas o si tu Canvas se compone de una sola variante.

{% alert note %}
Los Canvas pueden utilizar Intelligent Selection con la reelegibilidad habilitada, pero Braze no puede garantizar que un usuario reciba la misma variante al volver a entrar, ya que la asignación óptima cambia con el tiempo. Las campañas requieren una ventana de reelegibilidad de 24 horas o más cuando Intelligent Selection está activada. Para obtener más información, consulta [¿Por qué no se puede volver a ser elegible en menos de 24 horas cuando se combina con Intelligent Selection?](#why-is-re-eligibility-in-less-than-24-hours-not-available-when-combined-with-intelligent-selection).
{% endalert %}
{% endtab %}
{% endtabs %}

## Tiempo de ejecución {#run-time}

Para las campañas y los Canvas, Intelligent Selection funcionará hasta que reúna suficientes pruebas sobre las tasas de conversión "verdaderas" de las variantes. "Suficiente" viene determinado por una métrica especial llamada "arrepentimiento". Puedes pensar que es similar a la confianza, en el sentido de que Intelligent Selection se desactivará cuando haya suficientes datos para saber qué variante es la mejor.

En la mayoría de los casos, Intelligent Selection elegirá una de las variantes como la variante ganadora. Esta variante recibirá el 100 % de la audiencia para futuros envíos.

{% alert note %}
Es posible que Intelligent Selection deje de optimizar sin elegir un único ganador claro. Intelligent Selection deja de optimizar cuando tiene un 95 % de confianza en que continuar el experimento no mejorará la tasa de conversión en más de un 1 % de su tasa actual.
{% endalert %}

## Distribución de variantes de Intelligent Selection {#intelligent-selection-variant-distribution}

Intelligent Selection basa su distribución de variantes en el estado actual de las conversiones de la campaña. Solo determina las distribuciones finales tras el periodo de entrenamiento.

Esto significa que, durante las primeras etapas de la campaña, tanto las asignaciones de Intelligent Selection del 99 % como las del 1 % pueden recibir aproximadamente el mismo número de envíos, pero los porcentajes finales para la asignación de variantes pueden fijarse en 99 %–1 %.

Si no deseas que Intelligent Selection envíe 50/50 durante las primeras etapas de la campaña, te recomendamos utilizar una prueba A/B tradicional con variantes fijas.

## Preguntas frecuentes {#faq}

### ¿Por qué no se puede volver a ser elegible en menos de 24 horas cuando se combina con Intelligent Selection? {#why-is-re-eligibility-in-less-than-24-hours-not-available-when-combined-with-intelligent-selection}

No permitimos que las campañas con Intelligent Selection vuelvan a ser elegibles en un plazo demasiado corto, porque afectaría a la integridad de la variante de control. Al crear un intervalo de 24 horas, ayudamos a garantizar que el algoritmo dispondrá de un conjunto de datos estadísticamente válido con el que trabajar.

Normalmente, las campañas con reelegibilidad harán que los usuarios vuelvan a entrar en la misma variante que recibieron antes. Con Intelligent Selection, Braze no puede garantizar que un usuario reciba la misma variante de campaña, porque la distribución de variantes se habría desplazado debido al aspecto de asignación óptima de esta característica. Si se permitiera al usuario volver a entrar antes de que Intelligent Selection volviera a examinar el rendimiento de la variante, los datos podrían estar sesgados debido a los usuarios que volvieron a entrar.

Por ejemplo, si una campaña utiliza estas variantes:

- Variante A: 20 %
- Variante B: 20 %
- Control: 60 %

Entonces la distribución de variantes podría ser la siguiente para la segunda ronda:

- Variante A: 15 %
- Variante B: 25 %
- Control: 60 %

### ¿Por qué mis variantes de Intelligent Selection muestran envíos iguales durante las primeras fases de mi campaña? {#why-are-my-intelligent-selection-variants-showing-equal-sends-during-the-early-stages-of-my-campaign}

Intelligent Selection asigna variantes de envío en función del estado actual de conversión de la campaña. Solo determina las asignaciones finales de variantes tras un periodo de entrenamiento, en el que los envíos se reparten uniformemente entre las variantes. Si no quieres que Intelligent Selection envíe uniformemente durante las primeras fases de tu campaña, utiliza variantes fijas para una prueba A/B tradicional.

### ¿Dejará Intelligent Selection de optimizar sin elegir un claro ganador? {#will-intelligent-selection-stop-optimizing-without-picking-a-clear-winner}

Intelligent Selection dejará de optimizar cuando tenga un 95 % de confianza en que continuar el experimento no mejorará la tasa de conversión en más de un 1 % de su tasa actual.

### ¿Por qué no puedo habilitar Intelligent Selection en mi Canvas o campaña (aparece en gris)? {#why-cant-i-enable-intelligent-selection-in-my-canvas-or-campaign-grayed-out}

Intelligent Selection no estará disponible si:

- No has añadido eventos de conversión a tu campaña o Canvas
- Estás creando una campaña de envío único
- Tu campaña tiene habilitada la reelegibilidad con una ventana inferior a 24 horas
- Tu Canvas está compuesto por una única variante sin variantes adicionales ni grupos de control añadidos
- Tu Canvas está compuesto por un único grupo de control, sin variantes añadidas