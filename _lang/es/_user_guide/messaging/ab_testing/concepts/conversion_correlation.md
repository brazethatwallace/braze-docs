---
nav_title: Correlación de conversión
article_title: Correlación de conversión
alias: /conversion_correlation/
page_order: 3

page_type: reference
description: "Este artículo de referencia explica el análisis de correlación de conversiones en la página de análisis de Campaign."
tool:
  - Reports

---

# Correlación de conversión {#conversion-correlation}

> El análisis de correlación de conversiones en la página **Campaign Analytics** te ofrece información sobre qué atributos y comportamientos de los usuarios favorecen o perjudican los resultados que has establecido para las campañas.

## Resumen {#overview}

Para cada campaña, Braze revisa una lista de atributos y comportamientos de los usuarios y calcula si están estadísticamente asociados de forma significativa con aumentos o disminuciones en cada uno de los [eventos de conversión]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events) que has elegido para la campaña. También calculamos cuánto más o menos probable es que los usuarios con un atributo o comportamiento determinado conviertan y, si es significativo, lo mostramos en el lado correspondiente de la tabla. Los usuarios con cada atributo o comportamiento de interés se comparan con las tasas de la audiencia total de la campaña en su conjunto. Los comportamientos y atributos que no tienen una correlación significativa con la conversión no se muestran en la tabla.

Para ejecutar un análisis de correlación de conversiones, selecciona el evento de conversión de interés en el menú desplegable.

![Panel de correlación de conversiones que muestra un ejemplo con "Seleccionar un evento de conversión" configurado como "Evento de conversión primaria - A" con la configuración del evento como "Realizó una compra en 12 horas (cualquier producto)".]({% image_buster /assets/img/convcorr.png %})

## ¿Qué se comprueba? {#what-is-checked}

Comprobamos los siguientes atributos tratándolos como variables categóricas. En otras palabras, un usuario tiene o no tiene cada valor posible de estos atributos, y probamos si afectan a la tasa de conversión.

-  País
-  Idioma
-  Género

También comprobamos si lo siguiente afecta a la tasa de conversión:

- Realizar cualquier evento personalizado
- Campaigns y Canvas recibidos en los últimos 30 días (distintos de la campaña que se está evaluando actualmente)

Por último, comprobamos varias variables de comportamiento que pueden tomar múltiples valores. Dividimos las siguientes en cuatro contenedores o cuartiles y luego medimos la asociación de estar en ese cuartil con aumentos o disminuciones en la conversión:

- Edad
- Total de dólares gastados
- Número de sesiones

## ¿Cuándo puedo consultar este análisis? {#when-can-i-check-this-analysis}

Este análisis está disponible al menos 24 horas después de que una campaña comience a enviarse y solo tiene en cuenta los envíos que ocurrieron en los últimos 30 días. Si ningún comportamiento o atributo se correlaciona significativamente con alguno de los eventos de conversión de la campaña, el menú desplegable estará deshabilitado y se mostrará un mensaje informándote de ello.

## Cómo comprueba Braze la significancia {#how-braze-checks-for-significance}

Comprobamos la significancia estadística utilizando el [intervalo de confianza de Wilson](https://en.wikipedia.org/wiki/Binomial_proportion_confidence_interval#Wilson_score_interval). Determinamos con un 95 % de confianza la tasa a la que convirtió la audiencia total de la campaña. Esto se denomina tasa base.

Luego, para cada una de las variables, también calculamos la tasa a la que los usuarios con ese atributo o comportamiento particular de interés convirtieron con un 95 % de confianza. Al dividir eso por la tasa base, podemos medir la proporción. Si es mucho mayor que 1, los usuarios con ese atributo o comportamiento tienen más probabilidades de convertir. Si es mucho menor, tienen menos probabilidades. Mostramos el valor de la proporción en la tabla. El valor solo se muestra si está lo suficientemente alejado de 1 como para ser significativo al nivel de confianza del 95 %.