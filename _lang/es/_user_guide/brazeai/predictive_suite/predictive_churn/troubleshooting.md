---
nav_title: Solución de problemas
article_title: Solución de problemas de Predictive Churn
description: "Diagnostica errores de entrenamiento y audiencia de Predictive Churn utilizando un índice de síntomas y requisitos de datos."
page_order: 3

---

# Solución de problemas de Predictive Churn {#troubleshoot-predictive-churn}

> Usa esta página para resolver errores de entrenamiento y audiencia de Predictive Churn. Para análisis y calidad del modelo, consulta [Análisis de Predictive Churn]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/analytics).

Predictive Churn (y cualquier modelo de aprendizaje automático) solo es tan bueno como los datos disponibles para el modelo. También depende de tener un volumen suficiente de usuarios en el espacio de trabajo.

## Empieza aquí: identifica tu síntoma {#start-here-match-your-symptom}

Busca el mensaje de error, la advertencia o el resultado que ves al crear una predicción en la sección que explica cómo solucionarlo.

| Síntoma | Ir a |
| --- | --- |
| Error "No hay suficientes datos para entrenar" | [No hay suficientes datos para entrenar](#not-enough-data-to-train) |
| Advertencia "No hay suficientes usuarios no perdidos en el pasado" | [Audiencia de predicción demasiado pequeña](#problems-with-prediction-audience-size) |
| La audiencia de predicción supera el límite de tamaño | [Audiencia de predicción demasiado grande](#prediction-audience-size-is-too-big) |
| La calidad de la predicción está por debajo del 40 % | [La predicción tiene una calidad deficiente](#prediction-has-poor-quality) |
| No tienes claro si tus datos se ajustan al modelo | [Consideraciones sobre los datos](#data-considerations) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Síntoma de Predictive Churn" }

## Ruta de investigación estándar {#standard-investigation-path}

Usa este flujo de trabajo cuando la creación de una predicción falla o estás bloqueado por requisitos de datos o audiencia. Comienza en el paso 1.

1. Confirma que Predictive Churn está activado para tu empresa y que el espacio de trabajo tiene suficientes MAU (MAU), generalmente 300,000 MAU en un solo espacio de trabajo.
2. Revisa tu definición de cancelación. Los filtros demasiado restrictivos reducen la cantidad de usuarios perdidos disponibles para el entrenamiento.
3. Revisa la definición de tu audiencia de predicción. Muy pocos usuarios históricos que no cancelaron bloquean el entrenamiento del modelo.
4. Confirma que los eventos personalizados (no solo los atributos personalizados) capturan las acciones de alto valor que indican riesgo de cancelación.
5. Si los errores persisten después de ampliar las definiciones, ponte en contacto con [soporte de Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support).

## No hay suficientes datos para entrenar {#not-enough-data-to-train}

**Síntoma:** Ves un error de "No hay suficientes datos para entrenar" al crear una predicción.

Este error aparece cuando tu definición de cancelación es demasiado restrictiva y devuelve muy pocos usuarios perdidos.

Para solucionarlo, cambia el número de días, las acciones que definen la cancelación para captar más usuarios, o ambos. Asegúrate de que estás utilizando correctamente los filtros `AND/OR` para no crear definiciones excesivamente restrictivas.

{% alert important %}
Aunque Predictive Churn está activado a nivel de empresa, algunos espacios de trabajo pueden no tener suficientes usuarios para crear predicciones. Normalmente, necesitas 300.000 MAU en un solo espacio de trabajo.
{% endalert %}

## Problemas con el tamaño de la audiencia de predicción {#problems-with-prediction-audience-size}

**Síntoma:** Ves el mensaje "Not enough past non-churners to reliably build the Prediction."

![Requisitos de datos de predicción que muestran 31 usuarios perdidos anteriores (cumple el requisito) y 0 usuarios no perdidos anteriores (por debajo del mínimo). Un mensaje de advertencia indica que no hay suficientes usuarios no perdidos para construir la predicción.]({% image_buster /assets/img/churn/audience_size_error.png %})

Al construir tu audiencia de predicción para ajustar el tipo de uso contra el que quieres que se entrene tu modelo, es posible que encuentres este mensaje notificándote que tu audiencia de predicción tiene muy pocos usuarios.

Si la definición de tu audiencia de predicción es demasiado estricta, es posible que no tengas un grupo lo suficientemente grande de usuarios tanto históricos como activos con los que trabajar. Para solucionarlo, cambia la cantidad de días y el tipo de atributos utilizados en esta definición, modifica las acciones que definen la cancelación, o ambas cosas.

Si tu audiencia de predicción sigue siendo un problema incluso después de modificar tus definiciones, es posible que tengas muy pocos usuarios para soportar esta característica opcional. Intenta construir una predicción sin las capas y filtros adicionales.

## El tamaño de la audiencia de predicción es demasiado grande {#prediction-audience-size-is-too-big}

**Síntoma:** La definición de tu audiencia de predicción supera el tamaño máximo permitido.

Una definición de audiencia de predicción no puede superar los 100 millones de usuarios. Si ves un mensaje que indica que tu audiencia es demasiado grande, añade más capas a tu audiencia o cambia el periodo de tiempo en el que se basa.

## La predicción tiene mala calidad {#prediction-has-poor-quality}

**Síntoma:** La [calidad de la predicción]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/analytics) es del 39 % o inferior.

![Captura de pantalla relacionada con una predicción de mala calidad.]({% image_buster /assets/img/churn/churn3.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Si tu modelo tiene una calidad de predicción del 40 % o superior, estás en una buena posición. Pero si la calidad de la predicción cae al 39 % o menos, es posible que necesites editar las definiciones de cancelación y audiencia de predicción para que sean más específicas o tengan ventanas de tiempo diferentes.

Si no puedes cumplir con el requisito de tamaño de audiencia al crear las definiciones de predicción y, al mismo tiempo, lograr una calidad de predicción superior al 40 %, es probable que los datos enviados a Braze no sean ideales para este caso de uso, que no haya suficientes usuarios con los que construir un modelo, o que el ciclo de vida de tu producto sea más largo de lo que admite nuestra ventana retrospectiva actual de 60 días.

## Consideraciones sobre los datos {#data-considerations}

Las siguientes son preguntas que debes hacerte al configurar Predictive Churn. Los modelos de aprendizaje automático solo son tan buenos como los datos que los entrenan, por lo que tener buenas prácticas de higiene de datos y comprender lo que entra en el modelo marcará una gran diferencia.

- ¿Qué acciones de alto valor conducen a la retención y la fidelización?
- ¿Has configurado eventos personalizados que se correspondan con estas acciones específicas? Predictive Churn funciona con eventos personalizados, no con atributos personalizados.
- ¿Piensas en ventanas de tiempo dentro de las cuales definirás la cancelación? Puedes definir la cancelación como algo que ocurre hasta en 60 días.
- ¿Has tenido en cuenta las épocas del año que dan lugar a comportamientos atípicos de los usuarios, como las vacaciones? Los cambios rápidos en el comportamiento de los consumidores afectarán a tus predicciones.