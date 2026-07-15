---
nav_title: Distribución de variantes
article_title: Distribución de variantes
page_order: 1
page_type: reference
description: "Este artículo de referencia explica cómo Braze distribuye a los usuarios entre variantes en pruebas A/B y multivariantes."
tool:
  - Campaign
  - Canvas
---

# Distribución de variantes {#variant-distribution}

> Cuando configuras una prueba A/B o multivariante, cada envío asigna de forma independiente a los usuarios a variantes según los porcentajes que configures. Dado que la asignación es aleatoria, la distribución real puede no coincidir exactamente con tus porcentajes, especialmente con tamaños de muestra más pequeños.

## Cómo funciona {#how-it-works}

La distribución entre variantes no siempre es uniforme. Cada vez que se envía un mensaje en una campaña multivariante, Braze selecciona de forma independiente una opción aleatoria según los porcentajes que hayas establecido y asigna una variante en función del resultado. Es como lanzar una moneda: las anomalías son posibles. Si lanzas una moneda 100 veces, probablemente no obtendrás una división exacta de 50-50 entre cara y cruz, aunque solo tengas dos opciones. Podrías obtener 52 caras y 48 cruces.

De manera similar, si quieres dividir múltiples variantes de forma uniforme usando porcentajes con números enteros, asegúrate de que el número de variantes divida a 100 de manera exacta. De lo contrario, algunas variantes tendrán un porcentaje más alto de usuarios distribuidos en esa variante en comparación con otras. Por ejemplo, si tu campaña tiene siete variantes, no puede haber una distribución uniforme de variantes, ya que siete no divide a 100 de manera exacta como número entero. En este caso, tendrías dos variantes del 15 % y cinco variantes del 14 %.

{% alert tip %}
Para distribuir usuarios en un Canvas, puedes añadir un [paso para la división de decisiones]({{site.baseurl}}/decision_split) y separar a los usuarios según sus [números de contenedor aleatorio]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers).
{% endalert %}

## Distribución de mensajes dentro de la aplicación {#in-app-message-distribution}

Al ejecutar una prueba A/B en mensajes dentro de la aplicación, tus análisis pueden parecer mostrar una distribución de variantes más alta entre una variante y otra, incluso si tienen una división de porcentaje uniforme. Por ejemplo, considera el siguiente gráfico de *Destinatarios únicos* para la variante A y la variante C.

![Gráfico de destinatarios únicos que muestra que la variante A tiene un recuento consistentemente más alto que la variante C, a pesar de una división de porcentaje uniforme.]({% image_buster /assets/img/variant_distribution_iam.png %})

La variante A tiene un recuento consistentemente más alto de *Destinatarios únicos* que la variante C. Esto no se debe a la distribución de variantes, sino a cómo se calculan los *Destinatarios únicos* para los mensajes dentro de la aplicación. Para los mensajes dentro de la aplicación, los *Destinatarios únicos* son en realidad *Impresiones únicas*, que es el número total de personas que recibieron y visualizaron el mensaje dentro de la aplicación. Esto significa que si un usuario no recibe el mensaje por cualquier motivo o decide no visualizarlo, no se incluye en el recuento de *Destinatarios únicos*, y la distribución de variantes puede parecer sesgada.