---
nav_title: Predictive Events
article_title: Predictive Events
description: "Este artículo trata sobre Predictive Events (antes compra predictiva), una herramienta de Braze Predictive Suite que ofrece a los especialistas en marketing la posibilidad de identificar y enviar mensajes a los usuarios en función de la probabilidad de que realicen un evento."
page_order: 9
alias: /predictive_purchases/
search_rank: 1
---

# Predictive Events {#predictive-events}

> Predictive Events es una potente herramienta de Braze Predictive Suite que permite identificar y enviar mensajes a los usuarios en función de la probabilidad de que realicen un evento. Cuando creas una predicción de eventos, Braze entrena un modelo de aprendizaje automático utilizando [árboles de decisión con gradiente reforzado](https://en.wikipedia.org/wiki/Gradient_boosting) para aprender de la actividad previa y predecir la actividad futura.

## Acerca de Predictive Events {#about-predictive-events}

Una vez creada la predicción, a los usuarios se les asigna una [puntuación de probabilidad]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/analytics/#purchase_score) entre 0 y 100 que indica la probabilidad de que realicen el evento seleccionado. Cuanto mayor sea la puntuación, más probable es que el usuario realice ese evento. Los usuarios también se clasifican en categorías de probabilidad baja, media y alta.

El verdadero valor de Predictive Events reside en utilizar los resultados de la predicción para crear un segmento o una Campaign. Los especialistas en marketing pueden crear Campaigns específicas directamente en la página de **predicción** para obtener resultados inmediatos que aumenten los ingresos, o guardar un segmento para una futura Campaign o Canvas. ¿No sabes a quién dirigirte primero? Lee nuestras [consideraciones estratégicas]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/messaging_users/#strategy) para enviar mensajes a los usuarios en función de su puntuación de probabilidad.

![Gráfico titulado "Cómo funciona Predictive Events", que muestra los datos de usuario canalizados hacia el modelo de aprendizaje automático. La etiqueta dice "Entrena con datos históricos, compara el comportamiento de los usuarios que realizaron el evento en un periodo determinado con los que no lo hicieron". También muestra los resultados del aprendizaje automático, donde se clasifica a los usuarios de menor a mayor probabilidad de realizar el evento. La etiqueta dice "Predice la probabilidad de eventos futuros, asigna una puntuación de probabilidad a los usuarios para una segmentación precisa y conveniente."]({% image_buster /assets/img/how_predictive_events_works.png %})

## Acceso a Predictive Events {#accessing-predictive-events}

{% multi_lang_include brazeai/predictions_page_access.md %}

Antes de adquirir esta característica, está disponible en modo vista previa. Esto te permitirá ver una predicción de demostración con datos sintéticos, así como crear un modelo de predicción de vista previa cada vez. Esta predicción se creará basándose en tus datos de usuario reales, pero no te permitirá dirigirte a los usuarios para enviarles mensajes según su puntuación de probabilidad. Tampoco se actualizará regularmente tras su creación.

Con la vista previa, también puedes editar y reconstruir esta única predicción o archivarla y crear otras para probar la [calidad de predicción]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/analytics/#prediction_quality) esperada de [diferentes audiencias]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/creating_an_event_prediction/#audience) y familiarizarte con los análisis.