---
nav_title: Canales
article_title: Canales
page_order: 5
layout: dev_guide
guide_top_header: "Canales"
guide_top_text: "Llega a tus usuarios a través del canal adecuado en el momento adecuado. Elige entre canales dentro del producto, como mensajes dentro de la aplicación, Content Cards y Banners, o canales fuera del producto, como push, correo electrónico, SMS y WhatsApp."

page_type: landing
description: "Llega a tus usuarios a través de canales de mensajería dentro y fuera del producto en Braze."

guide_featured_title: "Canales dentro del producto"
guide_featured_list:
  - name: Mensajes dentro de la aplicación
    link: /docs/user_guide/channels/in_app_messages
    image: /assets/img/braze_icons/phone-02.svg
  - name: Content Cards
    link: /docs/user_guide/channels/content_cards
    image: /assets/img/braze_icons/sticker-square.svg
  - name: Banners
    link: /docs/user_guide/channels/banners
    image: /assets/img/braze_icons/layout-top.svg

guide_menu_title: "Canales fuera del producto"
guide_menu_list:
  - name: Correo electrónico
    link: /docs/user_guide/channels/email
    image: /assets/img/braze_icons/mail-01.svg
  - name: Correo electrónico transaccional
    link: /docs/user_guide/channels/transactional_email
    image: /assets/img/braze_icons/bank-note-02.svg
  - name: Páginas de inicio
    link: /docs/user_guide/messaging/landing_pages
    image: /assets/img/braze_icons/file-02.svg
  - name: LINE
    link: /docs/user_guide/channels/line
    image: /assets/img/braze_icons/message-chat-circle.svg
  - name: Notificaciones en vivo
    link: /docs/developer_guide/live_notifications/
    image: /assets/img/braze_icons/phone-02.svg
  - name: Push
    link: /docs/user_guide/channels/push
    image: /assets/img/braze_icons/marker-pin-05.svg
  - name: "SMS, MMS y RCS"
    link: /docs/user_guide/channels/sms_mms_and_rcs
    image: /assets/img/braze_icons/message-text-circle-01.svg
  - name: Webhooks
    link: /docs/user_guide/channels/webhooks
    image: /assets/img/braze_icons/brackets.svg
  - name: WhatsApp
    link: /docs/user_guide/channels/whatsapp
    image: /assets/img/braze_icons/whatsapp.svg
---

## Elegir un canal de mensajería {#choosing-a-message-channel}

Al determinar qué canal de mensajería es el más adecuado para tus Campaigns y Canvas, piensa siempre en el contenido y la urgencia de tu mensaje:

- **Contenido** se refiere a lo visualmente atractivo que es tu mensaje. Puedes añadir multimedia y otros activos a tu texto para enriquecer tu contenido.
- **Urgencia** es una medida de la rapidez con la que un mensaje puede notificar a tu usuario y captar su atención. Las notificaciones que el usuario puede ver de inmediato tienen una urgencia alta, mientras que los mensajes que requieren que el usuario inicie sesión en tu aplicación tienen una urgencia baja.

La matriz de mensajería de Braze simplifica la selección de canales al mapear la **complejidad del contenido** frente a la **urgencia de entrega**. Al equilibrar estos dos factores, puedes ayudar a que tu mensaje conecte en lugar de interrumpir.

![Las notificaciones push en móvil/web son contenido simple, urgencia alta; los correos electrónicos son contenido enriquecido, urgencia alta; los mensajes dentro de la aplicación/navegador son contenido simple, urgencia baja; las Content Cards son urgencia baja, contenido enriquecido]({% image_buster /assets/img_archive/messaging_matrix.png %})

Aunque la matriz destaca los canales principales, es adaptable: SMS y WhatsApp, por ejemplo, son herramientas de alta urgencia que escalan hacia contenido enriquecido cuando se utilizan formatos multimedia. Para saber más sobre cómo puedes aprovechar esta matriz, consulta nuestro curso de Braze Learning sobre [mensajería de canales cruzados](https://learning.braze.com/cross-channel-messaging).

## Recursos de accesibilidad {#accessibility-resources}

Puedes usar Braze para crear campañas de mensajería accesibles en cada canal. Trabaja con tus ingenieros para asegurarte de cumplir con los estándares de accesibilidad en tu implementación. Si deseas orientación adicional, te recomendamos:

- [Fundamentos de mensajería accesible](https://learning.braze.com/accessible-messaging-foundations): aprende los principios fundamentales de accesibilidad que se aplican a las comunicaciones de marca en este curso de Braze Learning.
- [Crear mensajes accesibles]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/accessibility/): aprende a añadir texto alternativo y estructurar tu contenido para tecnologías de asistencia directamente en Braze.

Si tienes comentarios sobre la accesibilidad de Braze o de los mensajes enviados desde Braze, nos encantaría conocerlos. Abre el menú **Support** en el encabezado global y selecciona **Share feedback** para enviarnos tus opiniones.