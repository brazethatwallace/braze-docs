---
nav_title: Políticas de extinción
article_title: Políticas de extinción para el correo electrónico
page_order: 8
page_type: reference
description: "Este artículo aborda las mejores prácticas en torno a las políticas de extinción y la comprensión de las situaciones en las que es mejor interrumpir los mensajes a los usuarios desvinculados."
channel: email

---

# Políticas de extinción {#sunset-policies}

> Aunque tengas la tentación de enviar campañas a tantos usuarios como puedas, hay situaciones en las que es realmente ventajoso detener los mensajes a los usuarios desvinculados.

En el caso del correo electrónico, la reputación de tu IP de envío y de tu dominio tiene en cuenta la participación, los informes de correos no deseados, las listas de bloqueo y más. Si la reputación se mantiene baja, los ISP y los filtros de buzones de correo pueden clasificar automáticamente tus correos electrónicos en una carpeta de correo no deseado o de baja prioridad para todos los destinatarios, no solo los inactivos. Las políticas de extinción limitan los envíos continuos a usuarios desvinculados, lo que ayuda a proteger la reputación; combínalas con un monitoreo regular para que puedas detectar problemas a tiempo.

## Monitorizar la salud de IP y dominio {#monitor-ip-and-domain-health}

Usa el [Centro de capacidad de entrega]({{site.baseurl}}/user_guide/analytics/dashboards/deliverability_center) para rastrear cómo los proveedores de buzón de correo perciben tus envíos:

- **Google Postmaster Tools** (después de conectar tu cuenta): reputación de IP, reputación de dominio, errores de entrega, autenticación (SPF, DKIM, DMARC) y métricas de cifrado para visibilidad relacionada con Gmail.
- **Microsoft Smart Network Data Services (SNDS)** (cuando se configura para tus IPs): salud de IP de buzones de Outlook y Microsoft, incluyendo resultados de filtros, tasas de quejas e impactos en trampas de correo no deseado.

Para una higiene de envío más amplia, consulta [Mejorar la capacidad de entrega del correo electrónico]({{site.baseurl}}/user_guide/channels/email/best_practices/improve_deliverability) y [Problemas de capacidad de entrega y trampas de correo no deseado]({{site.baseurl}}/user_guide/channels/email/email_setup/deliverability_pitfalls_and_spam_traps).

También puedes aprovechar herramientas externas como [Sender Score](https://www.senderscore.org/) o [Outlook Smart Network Data Services](https://postmaster.live.com/snds/) fuera de Braze para obtener señales adicionales.

## Usa listas de supresión {#use-suppression-lists}

Las [listas de supresión]({{site.baseurl}}/user_guide/audience/suppression_lists) son grupos de usuarios definidos con filtros de Segment que no reciben Campaigns ni Canvas de forma predeterminada, incluso cuando aparecen en el Segment objetivo. Para destinatarios inactivos o no comprometidos, una lista de supresión actúa como una protección a nivel de espacio de trabajo. Cuando los usuarios cumplen tus criterios de inactividad, dejan de recibir la mayoría de los mensajes sin que tengas que editar cada Segment o Campaign.

Para alinearte con una política de desactivación, crea la lista de supresión con filtros que capturen a los usuarios que ya no deberían recibir correo electrónico promocional continuo (por ejemplo, `Last Engaged With Message` u otros filtros en **Retargeting**) usando la misma ventana de retrospectiva y las mismas opciones de canal que utilizas para "no comprometidos" en tu política. La membresía es dinámica, por lo que los usuarios entran cuando cumplen los filtros y salen cuando vuelven a interactuar.

Si aún deseas que ciertos envíos lleguen a usuarios inactivos, como una recuperación final o recorridos transaccionales aprobados, configura etiquetas de excepción en la lista de supresión para que las Campaigns o Canvas con esas etiquetas se entreguen cuando los usuarios estén en la audiencia objetivo. Las listas de supresión funcionan junto con la segmentación, que puede definir a quién incluyes en un envío. Para conocer los pasos de configuración, permisos y límites, consulta [Configurar listas de supresión]({{site.baseurl}}/user_guide/audience/suppression_lists#setup).

## Usa filtros de segmentación {#use-segmentation-filters}

Los filtros de segmentación ayudan a evitar que tus mensajes parezcan correo no deseado, ya que te permiten implementar fácilmente políticas de extinción para correos electrónicos, push y notificaciones dentro de la aplicación. Aquí tienes algunas cosas a considerar cuando crees una política de extinción:

- ¿Qué cuenta como un usuario "no comprometido"?
- ¿La participación se define por clics, compras, uso de la aplicación o una combinación de estos comportamientos?
- ¿Cuánto tiempo debe durar la falta de participación para que dejes de enviar mensajes?
- ¿Entregarás alguna Campaign especial a los usuarios antes de excluirlos de tus Segments?
- ¿A qué canales de mensajería se aplicará tu política de extinción?

Por ejemplo, si tienes usuarios que optan por la [protección de la privacidad en los correos electrónicos (MPP) de Apple]({{site.baseurl}}/user_guide/channels/email/best_practices/apple_mail/mpp), considera cómo esto puede afectar tus Campaigns de correo electrónico y las métricas de capacidad de entrega, y determina cómo estructurar mejor tu política de extinción.

Para incorporar políticas de extinción en tus Campaigns, crea un [Segment]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment) que excluya automáticamente a los usuarios que hayan marcado tus correos electrónicos como correo no deseado o que no hayan interactuado con tus mensajes durante un período de tiempo determinado.

Para configurar estos Segments, elige los filtros `Has Marked You As Spam` y `Last Engaged With Message` ubicados en la sección **Reorientación** en el menú desplegable de filtros.

Cuando apliques el filtro `Last Engaged With Message`, especifica el tipo de mensajería (push, correo electrónico o notificación dentro de la aplicación) con la que el usuario ha interactuado o no, así como el número de días desde la última interacción del usuario. Después de crear un Segment, elige orientar este Segment con cualquier [canal de mensajería]({{site.baseurl}}/user_guide/channels).

![Página de detalles de Segment con el filtro "Last Engaged with Message" seleccionado.]({% image_buster /assets/img_archive/email_sunset_policies_new.png %})

Aunque Braze deja de enviar automáticamente correos electrónicos a los usuarios que te han marcado como correo no deseado, el filtro `Has Marked You As Spam` te permite también enviar a estos usuarios mensajes push dirigidos y notificaciones dentro de la aplicación. Este filtro es útil para [Campaigns de reorientación]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/retargeting_campaigns). Por ejemplo, puedes enviar a los usuarios no comprometidos mensajes que les recuerden las características y ofertas que se están perdiendo cuando no abren tus correos electrónicos.

Las políticas de extinción pueden ser especialmente útiles en Campaigns de correo electrónico dirigidas a usuarios inactivos. Aunque estas Campaigns se centran en Segments que no han interactuado con tu aplicación durante un período de tiempo, pueden poner en riesgo la capacidad de entrega de tus correos electrónicos si incluyen repetidamente destinatarios no comprometidos. Las políticas de extinción te permiten dirigirte a usuarios inactivos sin terminar en la carpeta de correo no deseado.