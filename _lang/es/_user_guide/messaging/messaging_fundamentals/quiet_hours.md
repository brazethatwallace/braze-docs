---
nav_title: Horas tranquilas
article_title: Horas tranquilas
page_order: 4
page_type: reference
description: "Este artículo de referencia cubre qué son las horas tranquilas, cómo Braze gestiona los mensajes durante el periodo de silencio y cómo interactúan las horas tranquilas con la sincronización inteligente."
---

# Horas tranquilas {#quiet-hours}

> Las horas tranquilas evitan que se envíen mensajes durante una ventana de tiempo específica. Puedes usarlas para evitar contactar a los usuarios en momentos inconvenientes (como durante la noche o temprano en la mañana) y aun así enviar en un momento óptimo fuera de esa ventana.

Las horas tranquilas se configuran a nivel de Campaign o Canvas. También puedes establecer [horas tranquilas del espacio de trabajo]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours/workspace_quiet_hours) como predeterminado para un canal de mensajería en todo tu espacio de trabajo (acceso anticipado).

## Cómo funcionan las horas tranquilas {#how-quiet-hours-work}

Cuando las horas tranquilas están habilitadas y un mensaje se enviaría durante la ventana restringida, Braze retiene el mensaje y lo entrega en el siguiente horario disponible después de que finalicen las horas tranquilas.

Por ejemplo, si las horas tranquilas van de 10 pm a 6 am y un mensaje está programado para las 5:30 am, Braze lo entrega a las 6 am en su lugar.

{% alert note %}
Las horas tranquilas se aplican en la zona horaria local de cada usuario.
{% endalert %}

## Horas tranquilas y sincronización inteligente {#quiet-hours-and-intelligent-timing}

Las horas tranquilas y la sincronización inteligente funcionan de forma independiente. Habilitar las horas tranquilas no requiere que la sincronización inteligente esté activada, y lo mismo ocurre a la inversa. En general, recomendamos elegir una u otra en lugar de usar ambas juntas, a menos que haya requisitos de política, cumplimiento u otros que hagan necesarias las horas tranquilas junto con la sincronización inteligente.

- **Sin sincronización inteligente:** Las horas tranquilas actúan como una ventana de no envío para tu hora de envío programada. Si la hora programada cae dentro de las horas tranquilas, el mensaje se retiene y se envía cuando la ventana se cierra.
- **Con sincronización inteligente:** Braze sigue calculando la hora de envío óptima de cada usuario. Si esa hora cae dentro de las horas tranquilas, el mensaje se retiene y se entrega en el borde más cercano de la ventana de silencio.

Para obtener más información sobre cómo configurar las horas tranquilas dentro de una Campaign con sincronización inteligente, consulta [Sincronización inteligente]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing).

## Consideraciones {#considerations}

- **Los mensajes se envían al mismo tiempo cuando terminan las horas tranquilas.** Si una audiencia grande tiene mensajes retenidos durante las horas tranquilas, todos esos mensajes se envían a la vez cuando la ventana se cierra. Para Campaigns con plazos ajustados, considera cómo esto afecta la sincronización de la entrega.
- **Las horas tranquilas no son lo mismo que cancelar un mensaje.** Cancelar un mensaje lo descarta por completo. Las horas tranquilas retienen el mensaje y lo entregan más tarde.
- **Las horas tranquilas no reevalúan la pertenencia a un Segment para un envío retenido.** Braze verifica la pertenencia al Segment cuando se desencadena el mensaje. Si el usuario es elegible en ese momento, Braze retiene el mensaje y lo envía cuando terminan las horas tranquilas. Esto es independiente de [reevaluar la pertenencia al Segment en el momento del envío]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery#audience-criteria-evaluation) o de las [validaciones de entrega]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#delivery-validations) de Canvas.
- **Las horas tranquilas son independientes de la limitación de frecuencia y los límites de velocidad.** Cada uno de estos controles de entrega se aplica de forma independiente. Un mensaje que supera los límites de frecuencia y de velocidad aún puede ser retenido por las horas tranquilas, y un mensaje retenido por las horas tranquilas se evalúa contra los límites de velocidad cuando finalmente se envía. Para más información, consulta [Límites de velocidad y limitación de frecuencia]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping).

## Artículos relacionados {#related-articles}

- [Horas tranquilas del espacio de trabajo]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours/workspace_quiet_hours)