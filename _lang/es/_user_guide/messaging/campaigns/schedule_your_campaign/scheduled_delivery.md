---
nav_title: Entrega planificada
article_title: Entrega planificada
page_order: 0
page_type: reference
description: "Este artículo de referencia describe las diferencias entre las opciones de planificación por tiempo para la entrega de campañas."
tool: Campaigns

---

# Entrega planificada {#scheduled-delivery}

> Las campañas enviadas mediante entrega planificada por tiempo se entregan en días específicos.

## Opción 1: Enviar tan pronto como se lance la campaña {#option-1-send-as-soon-as-the-campaign-is-launched}

Si eliges enviar un mensaje tan pronto como se lance, tu mensaje comenzará a enviarse en cuanto termines de crear tu Campaign.

![La sección "Entrega" con "Programado" seleccionado y la opción de programación basada en tiempo para enviar tan pronto como se lance la campaña.]({% image_buster /assets/img_archive/schedule_immediately.png %})

Este tipo de programación está diseñado para Campaigns puntuales que deseas enviar de inmediato, como mensajes sobre un evento actual. Una aplicación deportiva, por ejemplo, podría programar notificaciones push sobre actualizaciones de puntuación usando esta opción. Además, al enviar mensajes de prueba dirigidos solo a ti o a tu equipo, esta opción te permite entregarlos de inmediato.

Si planeas editar la Campaign y reenviarla después de ver la prueba, asegúrate de marcar la casilla que hace que los usuarios sean [re-elegibles]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility) para recibir la Campaign. De forma predeterminada, Braze envía una Campaign a un usuario solo una vez, a menos que esa casilla esté marcada.

## Opción 2: Enviar a una hora designada {#option-2-send-at-a-designated-time}

Programar una Campaign para una hora designada te permite especificar los días y las horas en que se envía tu Campaign. Puedes enviar un mensaje una vez, diariamente, semanalmente o mensualmente a una hora determinada del día, así como especificar cuándo debe comenzar y terminar tu Campaign. Esta fecha de finalización es inclusiva, lo que significa que el último envío se realiza en la fecha de finalización.

Si seleccionas una programación recurrente mensual, ten en cuenta que algunos meses pueden no tener el día seleccionado. Por ejemplo, supongamos que configuras una Campaign para que se envíe mensualmente el día 31. En este escenario, Braze envía el último día de ese mes, como el 30 de abril, porque el 31 de abril no existe.

Si seleccionas **Scheduled Delivery** y no eliges enviar en la hora local del usuario, tu Campaign se enviará de acuerdo con la zona horaria especificada en tu página de **Company Settings**.

![Las opciones de programación basadas en el tiempo para enviar una Campaign a una hora designada.]({% image_buster /assets/img_archive/schedule_designated.png %})

### Campaigns en zona horaria local {#local-time-zone-campaigns}

Puedes entregar el mensaje en las zonas horarias locales de los usuarios para que los miembros de tu audiencia internacional no reciban una notificación en horarios inconvenientes. Las Campaigns en zona horaria local deben programarse con 24 horas de anticipación para garantizar que los usuarios elegibles de todas las zonas horarias puedan recibirlas. Consulta las [preguntas frecuentes sobre Campaigns]({{site.baseurl}}/user_guide/messaging/campaigns/faq#how-do-i-schedule-a-local-time-zone-campaign) para entender cómo funcionan las Campaigns en zona horaria local y las reglas de entrega asociadas.

Los Segments a los que se dirigen las Campaigns en zona horaria local deben incluir, como mínimo, una ventana de 2 días para incorporar usuarios de todas las zonas horarias. Por ejemplo, si tu Campaign está programada para enviarse por la noche pero tiene solo una ventana de 1 día, algunos usuarios pueden haber salido del Segment cuando se alcance su zona horaria. Ejemplos de filtros que crean una ventana de 2 días son "último uso hace más de 1 día" y "último uso hace menos de 3 días", o "primera compra hace más de 7 días" y "primera compra hace menos de 9 días".

### Ejemplos {#use-cases}

Las programaciones a hora designada son las más adecuadas para mensajes programados con anticipación y Campaigns recurrentes, como las de incorporación y retención, que se ejecutan regularmente para todos los usuarios calificados.

## Opción 3: Sincronización inteligente {#option-3-intelligent-timing}

La [sincronización inteligente]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing) te permite entregar una Campaign a cada usuario en un momento diferente. Braze calcula el momento de cada individuo en función de cuándo ese usuario suele interactuar con tu aplicación y sus notificaciones. Opcionalmente, puedes especificar que las Campaigns con sincronización inteligente se envíen solo durante una parte determinada del día. Por ejemplo, si estás notificando a los usuarios sobre una promoción que termina a medianoche, es posible que quieras que tus mensajes se envíen a más tardar a las 10 pm.

![Las opciones de programación basadas en el tiempo para usar la sincronización inteligente y enviar una Campaign en el momento más popular de uso de la aplicación entre todos los usuarios.]({% image_buster /assets/img_archive/schedule_intelligent.png %})

### Reglas de entrega {#delivery-rules}

Dado que el momento óptimo de un usuario puede ser cualquier hora a lo largo de 24 horas en todas las zonas horarias globales, todas las Campaigns con sincronización inteligente deben programarse con 48 horas de antelación. Programar con 48 horas de anticipación tiene en cuenta la entrega a todos los usuarios en todo el mundo, ya que un solo día abarca aproximadamente 48 horas en todas las zonas horarias. Además, de forma similar a las Campaigns con hora designada, los mensajes con una ventana de 1 día no alcanzan a los usuarios que salen del Segment antes de que se alcance su hora óptima en su zona horaria. Los Segments para Campaigns con sincronización inteligente deben incorporar como mínimo una ventana de 3 días para tener esto en cuenta.

Si el perfil de un usuario no tiene suficientes datos para calcular un momento óptimo, puedes elegir un método alternativo para enviar durante el momento más popular de uso de la aplicación entre todos los usuarios o una hora alternativa personalizada establecida.

### Ejemplos

Las Campaigns con sincronización inteligente funcionan mejor para mensajes únicos y recurrentes en los que hay cierta flexibilidad en cuanto al momento de entrega, como cuando no son adecuadas para noticias de última hora o anuncios con hora programada.

## Evaluación de criterios de audiencia con retrasos {#audience-criteria-evaluation-with-delays}

Para Campaigns que usan entrega programada, los criterios de audiencia siempre se evalúan en el momento del envío programado, no cuando se lanza la Campaign. Esto se aplica a cualquier retraso entre la programación y el envío, por ejemplo, límites de velocidad, zona horaria local, sincronización inteligente o un programa de desencadenamiento.

## Solución de problemas {#troubleshooting}

### ¿Por qué mi Campaign de correo electrónico programada no alcanzó a toda la audiencia estimada? {#why-didnt-my-scheduled-email-campaign-reach-the-entire-estimated-audience}

Los envíos pueden ser inferiores a la audiencia estimada cuando los usuarios no tienen una dirección de correo electrónico, no están suscritos al correo electrónico o son excluidos por filtros de capacidad de entrega en el momento del envío. Un cambio reciente en la dirección de correo electrónico de un usuario también puede afectar la elegibilidad cuando los criterios de audiencia se reevalúan en el momento del envío. Para más factores, consulta [¿Por qué los envíos son inferiores al tamaño de audiencia estimado?]({{site.baseurl}}/user_guide/messaging/campaigns/faq#why-are-sends-lower-than-the-estimated-audience-size).

### ¿Por qué mi Campaign se envió un día antes de la hora programada? {#why-did-my-campaign-send-a-day-before-the-scheduled-time}

Si una Campaign se envía antes del horario que configuraste en **Configuración de la empresa**, habilita **Enviar en la zona horaria local** o añade una ventana de tiempo de entrega para Campaigns con sincronización inteligente. Sin esos ajustes, la evaluación de zona horaria puede poner en cola los envíos para usuarios en zonas horarias más tempranas antes de la hora programada prevista. Para más información, consulta [Campaigns en zona horaria local](#local-time-zone-campaigns) y [¿Cuándo evalúa Braze a los usuarios para la entrega en zona horaria local?]({{site.baseurl}}/user_guide/messaging/campaigns/faq#when-does-braze-evaluate-users-for-local-time-zone-delivery).