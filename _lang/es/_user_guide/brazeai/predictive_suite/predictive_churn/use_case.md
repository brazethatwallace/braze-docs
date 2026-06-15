---
nav_title: Casos de uso
article_title: "Caso de uso: reducir la tasa de abandonos con contenido oportuno"
description: "Este ejemplo muestra cómo una marca ficticia utiliza Predictive Churn para reducir de forma proactiva el abandono de usuarios."
page_type: tutorial
---

# Caso de uso: reducir la tasa de abandonos con contenido oportuno para reactivar la interacción {#use-case-reduce-churn-with-timely-content-re-engagement}

> Este ejemplo muestra cómo una marca ficticia utiliza Predictive Churn para reducir de forma proactiva el abandono de usuarios. En lugar de esperar a que se produzca el abandono, predice qué usuarios están en riesgo y entrega mensajes personalizados mientras aún están activos.

Supongamos que Camila es administradora de CRM en MovieCanon, una plataforma de streaming de películas independientes, documentales y series internacionales.

El equipo de Camila ha detectado una tendencia preocupante: los usuarios se registran, ven una o dos películas y luego desaparecen. Históricamente, han intentado enviar un correo electrónico genérico con el mensaje «Te echamos de menos» una semana después, pero con una tasa de conversión del 3 %, es demasiado poco y demasiado tarde. La mayoría de los usuarios no vuelven a interactuar, y el abandono se vuelve inevitable.

Camila quiere cambiar eso. En lugar de reaccionar ante el abandono después de que se produzca, utiliza Predictive Churn para identificar a los usuarios que probablemente se volverán inactivos en los próximos 14 días, lo que le da a su equipo la oportunidad de reactivar la interacción con ellos mientras aún están activos.

Este tutorial explica cómo Camila:

- Crea un modelo de predicción de abandono basado en el comportamiento de los usuarios
- Segmenta a los usuarios según su nivel de riesgo
- Crea una campaña de reactivación de la interacción adaptada a las personas con mayor riesgo
- Evalúa el impacto mediante análisis de Campaign

## Paso 1: Crear un modelo de predicción de abandono {#step-1-create-a-churn-prediction-model}

Camila comienza modelando el resultado que quiere evitar: que los usuarios se vuelvan inactivos. Para MovieCanon, el abandono significa no iniciar una transmisión en un plazo de 14 días, por lo que ese es el comportamiento que quiere predecir.

1. En el dashboard de Braze, Camila va a **Analytics** > **Predictive Churn**.
2. Crea una nueva predicción de abandono y la denomina «Riesgo de abandono en 2 semanas».
3. Para definir el abandono, selecciona `do not` y el evento personalizado `stream_started`, que indica una interacción activa.
4. Establece el periodo de predicción en 14 días, lo que significa que el modelo identificará a los usuarios que probablemente pasarán 14 días sin iniciar una nueva transmisión.

![Definición de abandono que muestra el abandono definido como un usuario que no realiza el evento personalizado «stream_started» en los últimos 14 días.]({% image_buster /assets/img/ai_use_cases/churn_definition.png %})

{:start="5"}
5. Selecciona una audiencia de predicción que incluye a todos los usuarios que han desencadenado eventos relevantes en los últimos 30 días, lo que proporciona al modelo suficiente comportamiento reciente del que aprender.
6. Establece el calendario de actualización de las predicciones a semanal para que las puntuaciones se mantengan actualizadas.
7. Selecciona **Create prediction**.

A continuación, el modelo comienza el entrenamiento, analizando comportamientos como las sesiones recientes, la frecuencia de visualización y las interacciones con el contenido para detectar patrones que predicen el abandono. Una hora más tarde, Camila recibe un correo electrónico en el que se le informa de que su predicción ha terminado de entrenarse, por lo que la abre en Braze y comprueba la puntuación de [calidad de la predicción]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/analytics/#prediction_quality). Está etiquetada como «Bueno», lo que significa que las predicciones del modelo probablemente sean precisas y fiables. Confiada en el rendimiento del modelo, sigue adelante.

## Paso 2: Segmentar a los usuarios según el riesgo de abandono {#step-2-segment-users-by-churn-risk}

Una vez que el modelo ha finalizado el entrenamiento, Braze asigna a cada usuario elegible una [puntuación de riesgo de abandono]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/analytics/#churn_score) entre 0 y 100.

Para determinar un umbral inicial para la segmentación, Camila utiliza el control deslizante de la audiencia de predicción para obtener una vista previa del número de usuarios que se encuentran en cada rango de puntuación y la precisión de la predicción en ese nivel. Equilibra la cobertura y la precisión basándose en los verdaderos positivos esperados. Basándose en esto, decide centrarse en las puntuaciones de riesgo superiores a 70.

1. Camila navega hasta Segments en Braze.
2. Crea un [segmento]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment/) utilizando el [filtro de puntuación de riesgo de abandono]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters/#churn-risk-score) y selecciona la predicción de abandono que ha creado:
   - **Probabilidad de abandono:** puntuación superior a 70

![Filtrado de segmento para usuarios con una puntuación de riesgo de abandono superior a 70.]({% image_buster /assets/img/ai_use_cases/churn_risk_score.png %})

## Paso 3: Dirigirse a los usuarios en riesgo con contenido recurrente de reactivación de la interacción {#step-3-target-at-risk-users-with-recurring-re-engagement-content}

Con su predicción y su segmento listos, Camila configura una Campaign recurrente que llega automáticamente a los usuarios que se encuentran en situación de riesgo cada semana.

1. Camila crea una Campaign recurrente y habilita [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing/), de modo que cada mensaje se entrega cuando cada usuario individual tiene más probabilidades de interactuar, en lugar de basarse en un día y una hora fijos.
2. Se enfoca en el segmento «Probabilidad de abandono» que acaba de crear.
3. Establece el evento de conversión de la Campaign como el evento personalizado `stream_started`, para realizar el seguimiento del número de usuarios que realmente regresan para ver el contenido.
4. Camila elige el correo electrónico como su canal principal, ya que le permite destacar múltiples selecciones de contenido personalizado en un formato visualmente rico sin demasiada presión. El correo electrónico incluye:
   - Una lista de visualización personalizada basada en [recomendaciones de elementos de IA]({{site.baseurl}}/user_guide/brazeai/item_recommendations/), seleccionadas de forma dinámica del catálogo de MovieCanon
   - Una llamada a la acción que los lleva directamente a la aplicación.

Esto garantiza que, cada semana, MovieCanon solo llegue a los usuarios que necesitan un empujoncito, sin exceso de mensajería ni conjeturas.

### Ejemplo de correo electrónico {#example-email}

- **Línea del asunto:** No dejes estos títulos en suspenso
- **Encabezado:** Tu próxima gran serie te está esperando
- **Cuerpo:** ¿Hace tiempo que no pulsas el botón de reproducción? No te preocupes, hemos seleccionado algunas opciones especialmente para ti. Desde thrillers de ritmo lento hasta documentales galardonados, aquí hay algo con tu nombre escrito.
- **CTA:** Ver más selecciones

## Paso 4: Medir el rendimiento {#step-4-measure-performance}

Después de unas semanas, Camila revisa el [análisis de su Campaign]({{site.baseurl}}/user_guide/channels/email/reporting/) para evaluar el rendimiento de la estrategia.

Observa lo siguiente:

- *Tasa de apertura:* 31 %
- *Tasa de clics:* 15 %
- *Tasa de conversión* (transmisión iniciada en un plazo de 48 horas): 11 %

En comparación con la antigua Campaign «Te echamos de menos» (en la que las tasas de conversión rondaban el 3 %), este nuevo flujo reduce la tasa de abandono en el grupo objetivo en un 28 %. Analiza el [informe de embudo]({{site.baseurl}}/user_guide/analytics/reports/funnel_reports/) para detectar dónde abandonan los usuarios. Aunque las tasas de apertura y clics son buenas, nota una ligera fricción entre los clics y las conversiones, lo que la lleva a plantearse probar diferentes textos para las llamadas a la acción o experimentar con el diseño.

Para comprender el impacto a largo plazo, Camila también realiza el seguimiento del volumen de usuarios que entran en el segmento «Probabilidad de abandono» semana tras semana. Esto le ayuda a evaluar el estado general del ciclo de vida y a definir la estrategia de retención a un nivel más amplio. Por último, vuelve a visitar la página de [análisis de predicciones]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/analytics/) de su predicción de abandono para comparar los usuarios que abandonan previstos con los reales, una comprobación útil para asegurarse de que el modelo funciona según lo esperado.

Basándose en esta información, Camila tiene previsto realizar pruebas A/B con las líneas del asunto, probar diferentes intervalos de tiempo y experimentar con formatos de contenido, como recomendaciones en forma de carrusel en un mensaje dentro de la aplicación.

Gracias a Predictive Churn, Intelligent Timing y la personalización basada en inteligencia artificial, el equipo de Camila no solo reacciona ante el abandono, sino que se adelanta a él. Y su Campaign se ejecuta discretamente en segundo plano, llegando a las personas adecuadas, en el momento adecuado, con contenido que realmente les interesa.