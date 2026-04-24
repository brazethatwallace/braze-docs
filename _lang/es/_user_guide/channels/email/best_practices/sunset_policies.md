---
nav_title: Políticas de desactivación
article_title: Políticas de desactivación para correo electrónico
page_order: 8
page_type: reference
description: "Este artículo cubre las mejores prácticas en torno a las políticas de desactivación y la comprensión de situaciones en las que es mejor dejar de enviar mensajes a usuarios no comprometidos."
channel: email

---

# Políticas de desactivación

> Aunque puede ser tentador enviar campañas a tantos usuarios como sea posible, hay situaciones en las que en realidad es ventajoso dejar de enviar mensajes a usuarios no comprometidos.

Para los correos electrónicos, tu IP de envío tiene una puntuación de reputación que tiene en cuenta la interacción, los informes de correos no deseados, las listas de bloqueo y más. Puedes usar herramientas como [Sender Score](https://www.senderscore.org/) o [Smart Network Data Service de Outlook](https://postmaster.live.com/snds/) para monitorear tu puntuación de reputación. Si tu puntuación de reputación es consistentemente baja, los filtros de ISP y buzones de correo pueden clasificar automáticamente tus correos electrónicos en una carpeta de correo no deseado o de baja prioridad para todos los destinatarios, incluso los comprometidos. Crear una política de desactivación ayuda a entregar tus correos electrónicos solo a destinatarios activos.

Los filtros de segmentación ayudan a evitar que tus mensajes parezcan correo no deseado, permitiéndote implementar fácilmente políticas de desactivación para correos electrónicos, push y notificaciones dentro de la aplicación. Aquí hay algunas cosas a considerar cuando crees una política de desactivación:

- ¿Qué cuenta como un usuario "no comprometido"?
- ¿La interacción se define por clics, compras, uso de la aplicación o una combinación de estos comportamientos?
- ¿Cuánto tiempo debe durar la falta de interacción para que dejes de enviar mensajes?
- ¿Enviarás alguna campaña especial a los usuarios antes de excluirlos de tus segmentos?
- ¿A qué canales de mensajería se aplicará tu política de desactivación?

Por ejemplo, si tienes usuarios que optan por la [protección de la privacidad en los correos electrónicos (MPP) de Apple]({{site.baseurl}}/user_guide/channels/email/best_practices/apple_mail/mpp/), considera cómo esto puede afectar tus campañas de correo electrónico y las métricas de capacidad de entrega, y determina cómo estructurar mejor tu política de desactivación.

Para incorporar políticas de desactivación en tus campañas, crea un [segmento]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment/#creating-a-segment) que excluya automáticamente a los usuarios que han marcado tus correos electrónicos como correo no deseado o que no han interactuado con tus mensajes durante un período de tiempo determinado.

Para configurar estos segmentos, elige los filtros `Has Marked You As Spam` y `Last Engaged With Message` ubicados en la sección **Reorientación** en el menú desplegable de filtros.

Cuando apliques el filtro `Last Engaged With Message`, especifica el tipo de mensajería (push, correo electrónico o notificación dentro de la aplicación) con la que el usuario ha interactuado o no, así como el número de días desde la última interacción del usuario. Después de crear un segmento, elige orientar este segmento con cualquier [canal de mensajería]({{site.baseurl}}/user_guide/channels/).

![Página de detalles del segmento con el filtro "Last Engaged with Message" seleccionado.]({% image_buster /assets/img_archive/email_sunset_policies_new.png %})

Aunque Braze deja de enviar automáticamente correos electrónicos a los usuarios que te han marcado como correo no deseado, el filtro `Has Marked You As Spam` te permite también enviar a estos usuarios mensajes push dirigidos y notificaciones dentro de la aplicación. Este filtro es útil para [campañas de reorientación]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/retargeting_campaigns/#retarget-campaigns). Por ejemplo, puedes enviar a los usuarios no comprometidos mensajes que les recuerden las características y ofertas que se están perdiendo al no abrir tus correos electrónicos.

Las políticas de desactivación pueden ser especialmente útiles en campañas de correo electrónico dirigidas a usuarios inactivos. Aunque estas campañas se centran en segmentos que no han interactuado con tu aplicación durante un período de tiempo, pueden poner en riesgo la capacidad de entrega de tus correos electrónicos si incluyen repetidamente destinatarios no comprometidos. Las políticas de desactivación te permiten dirigirte a usuarios inactivos sin terminar en la carpeta de correo no deseado.