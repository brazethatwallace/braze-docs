---
nav_title: Horas tranquilas
article_title: Horas tranquilas
page_order: 4
page_type: reference
description: "Este artículo de referencia cubre qué son las horas tranquilas, cómo Braze gestiona los mensajes durante el periodo de silencio y cómo interactúan las horas tranquilas con Intelligent Timing."
---

# Horas tranquilas {#quiet-hours}

> Las horas tranquilas evitan que se envíen mensajes durante una ventana de tiempo específica. Puedes usarlas para evitar contactar a los usuarios en momentos inconvenientes (como durante la noche o temprano en la mañana) y aun así enviar en un momento óptimo fuera de esa ventana.

Las horas tranquilas se configuran a nivel de campaña o Canvas.

## Cómo funcionan las horas tranquilas {#how-quiet-hours-work}

Cuando las horas tranquilas están habilitadas y un mensaje se enviaría durante la ventana restringida, Braze retiene el mensaje y lo entrega en el siguiente momento disponible después de que terminen las horas tranquilas.

Por ejemplo, si las horas tranquilas van de 10 pm a 6 am y un mensaje está planificado para las 5:30 am, Braze lo entrega a las 6 am en su lugar.

{% alert note %}
Las horas tranquilas se aplican en la zona horaria local de cada usuario.
{% endalert %}

## Horas tranquilas e Intelligent Timing {#quiet-hours-and-intelligent-timing}

Las horas tranquilas e Intelligent Timing operan de forma independiente. Habilitar las horas tranquilas no requiere que Intelligent Timing esté activado, y lo mismo aplica a la inversa. En general, recomendamos elegir una u otra opción en lugar de usar ambas juntas, a menos que haya requisitos de políticas, cumplimiento u otros que hagan necesarias las horas tranquilas junto con Intelligent Timing.

- **Sin Intelligent Timing:** Las horas tranquilas actúan como una ventana de no envío para tu hora de envío planificada. Si la hora planificada cae dentro de las horas tranquilas, el mensaje se retiene y se envía cuando la ventana se cierra.
- **Con Intelligent Timing:** Braze aún calcula la hora de envío óptima de cada usuario. Si esa hora cae dentro de las horas tranquilas, el mensaje se retiene y se entrega en el borde más cercano de la ventana de silencio.

Para más información sobre cómo configurar las horas tranquilas dentro de una campaña con Intelligent Timing, consulta [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing/).

## Aspectos a considerar {#things-to-consider}

- **Los mensajes se envían al mismo tiempo cuando terminan las horas tranquilas.** Si una audiencia grande tiene mensajes retenidos durante las horas tranquilas, todos esos mensajes se envían a la vez cuando la ventana se cierra. Para campañas sensibles al tiempo, considera cómo esto afecta los tiempos de entrega.
- **Las horas tranquilas no son lo mismo que cancelar un mensaje.** Cancelar un mensaje lo descarta por completo. Las horas tranquilas retienen el mensaje y lo entregan después.
- **Las horas tranquilas son independientes de la limitación de frecuencia y el límite de velocidad.** Cada uno de estos controles de entrega se aplica de forma independiente. Un mensaje que pasa los límites de frecuencia y velocidad aún puede ser retenido por las horas tranquilas, y un mensaje retenido por las horas tranquilas se evalúa contra los límites de velocidad cuando finalmente se envía. Para más información, consulta [Límite de velocidad y limitación de frecuencia]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/).