---
nav_title: Entrega planificada
article_title: Entrega planificada
page_order: 0
page_type: reference
description: "Este artículo de referencia describe las diferencias entre las opciones de planificación por tiempo para la entrega de campañas."
tool: Campaigns

---

# Entrega planificada

> Las campañas enviadas mediante entrega planificada por tiempo se entregan en días específicos.

## Opción 1: Enviar tan pronto como se lance la campaña

Si eliges enviar un mensaje tan pronto como se lance, tu mensaje comenzará a enviarse en cuanto termines de crear tu campaña.

![La sección "Entrega" con "Planificada" seleccionado y la opción de planificación por tiempo de enviar tan pronto como se lance la campaña.]({% image_buster /assets/img_archive/schedule_immediately.png %})

Este tipo de planificación está diseñado para campañas puntuales que deseas enviar de inmediato, como mensajes sobre un evento actual. Una aplicación deportiva, por ejemplo, podría planificar notificaciones push sobre actualizaciones de marcadores usando esta opción. Además, al enviar mensajes de prueba dirigidos solo a ti o a tu equipo, esta opción te permite entregarlos de inmediato.

Si planeas editar la campaña y reenviarla después de ver la prueba, asegúrate de marcar la casilla que hace que los usuarios sean [reelegibles]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility/) para recibir la campaña. De forma predeterminada, Braze envía una campaña a un usuario solo una vez, a menos que esa casilla esté marcada.

## Opción 2: Enviar a una hora designada

Planificar una campaña para una hora designada te permite especificar los días y las horas en que se envía tu campaña. Puedes enviar un mensaje una vez, diariamente, semanalmente o mensualmente a una hora determinada del día, así como especificar cuándo debe comenzar y terminar tu campaña. Esta fecha de finalización es inclusiva, lo que significa que el último envío se realiza en la fecha de finalización.

Si seleccionas una planificación recurrente mensual, ten en cuenta que algunos meses pueden no tener el día seleccionado. Por ejemplo, supongamos que configuras una campaña para enviarse mensualmente el día 31. En este caso, Braze envía el último día de ese mes, como el 30 de abril, porque el 31 de abril no existe.

Si seleccionas **Entrega planificada** y no eliges enviar en la hora local del usuario, tu campaña se enviará según la zona horaria especificada en tu página de **Configuración de empresa**.

![Las opciones de planificación por tiempo para enviar una campaña a una hora designada.]({% image_buster /assets/img_archive/schedule_designated.png %})

### Campañas en zona horaria local

Puedes entregar el mensaje en las zonas horarias locales de los usuarios para que los miembros de tu audiencia internacional no reciban una notificación en horarios inconvenientes. Las campañas en zona horaria local deben planificarse con 24 horas de anticipación para garantizar que los usuarios elegibles de todas las zonas horarias puedan recibirlas. Consulta las [preguntas frecuentes sobre campañas]({{site.baseurl}}/user_guide/messaging/campaigns/faq#how-do-i-schedule-a-local-time-zone-campaign/) para entender cómo funcionan las campañas en zona horaria local y las reglas de entrega asociadas.

Los segmentos dirigidos con campañas en zona horaria local deben incluir, como mínimo, una ventana de 2 días para incorporar usuarios de todas las zonas horarias. Por ejemplo, si tu campaña está planificada para enviarse por la noche pero tiene solo una ventana de 1 día, algunos usuarios pueden haber salido del segmento cuando se alcance su zona horaria. Ejemplos de filtros que crean una ventana de 2 días son "último uso hace más de 1 día" y "último uso hace menos de 3 días", o "primera compra hace más de 7 días" y "primera compra hace menos de 9 días".

### Casos de uso

Las planificaciones a hora designada son más adecuadas para mensajes planificados con anticipación y campañas recurrentes, como las de incorporación y retención, que se ejecutan regularmente para todos los usuarios cualificados.

## Opción 3: Intelligent Timing

[Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing/) te permite entregar una campaña a cada usuario en un momento diferente. Braze calcula el momento de cada individuo en función de cuándo ese usuario suele interactuar con tu aplicación y sus notificaciones. Opcionalmente, puedes especificar que las campañas con Intelligent Timing se envíen solo durante una parte determinada del día. Por ejemplo, si estás notificando a los usuarios sobre una promoción que termina a medianoche, es posible que quieras que tus mensajes se envíen a las 10 pm como máximo.

![Las opciones de planificación por tiempo para usar Intelligent Timing y enviar una campaña en el momento más popular de uso de la aplicación entre todos los usuarios.]({% image_buster /assets/img_archive/schedule_intelligent.png %})

### Reglas de entrega

Dado que el momento óptimo de un usuario puede ser cualquier hora a lo largo de las 24 horas, todas las campañas con Intelligent Timing deben planificarse con 24 horas de anticipación. Además, de manera similar a las campañas a hora designada, los mensajes con una ventana de 1 día perderán a los usuarios que salgan del segmento antes de que se alcance su hora óptima en su zona horaria. Los segmentos para campañas con Intelligent Timing deben incorporar como mínimo una ventana de 3 días para tener esto en cuenta.

Si el perfil de un usuario no tiene suficientes datos para calcular un momento óptimo, puedes elegir un método alternativo para enviar durante el momento más popular de uso de la aplicación entre todos los usuarios o establecer una hora alternativa personalizada.

### Casos de uso

Las campañas con Intelligent Timing funcionan mejor para mensajes puntuales y recurrentes donde hay cierta flexibilidad en cuanto al momento de entrega, como cuando no son adecuadas para noticias de última hora o anuncios con hora específica.

## Evaluación de criterios de audiencia con retrasos

Para las campañas que usan entrega planificada, los criterios de audiencia siempre se evalúan en el momento del envío planificado, no cuando se lanza la campaña. Esto se aplica a cualquier retraso entre la planificación y el envío, por ejemplo, límites de velocidad, zona horaria local, Intelligent Timing o una planificación desencadenada.