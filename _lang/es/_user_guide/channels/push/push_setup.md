---
nav_title: "Configuración"
article_title: Configuración push
page_order: 0
layout: dev_guide
guide_top_header: "Configuración push"
guide_top_text: "Comprende el ciclo de vida de los tokens de notificaciones push y los estados de suscripción para asegurarte de que tus notificaciones push lleguen a los usuarios correctos."

page_type: landing
description: "Aprende sobre el ciclo de vida de los tokens de notificaciones push y los estados de suscripción para notificaciones push en Braze."

guide_featured_title: "Artículos de la sección"
guide_featured_list:
  - name: Ciclo de vida del token de notificaciones push
    link: /docs/user_guide/channels/push/push_setup/push_token_lifecycle
    image: /assets/img/braze_icons/refresh-ccw-02.svg
  - name: Estados de suscripción push
    link: /docs/user_guide/channels/push/push_setup/push_subscription_states
    image: /assets/img/braze_icons/users-01.svg
---

## Requisitos previos {#prerequisites}

Antes de poder crear y enviar mensajes push con Braze, tienes que trabajar con tus desarrolladores para integrar push en tu sitio web o aplicación. Para conocer los pasos detallados, consulta nuestras guías de integración para cada plataforma:

- [iOS]({{site.baseurl}}/developer_guide/push_notifications?sdktab=swift)
- [Android]({{site.baseurl}}/developer_guide/push_notifications?sdktab=android)
- [Web]({{site.baseurl}}/developer_guide/push_notifications?sdktab=web)

## Preparación para push {#push-priming}

Ten en cuenta que los usuarios necesitan dar su adhesión voluntaria a push para recibir tus mensajes, lo que significa que es buena idea usar mensajes dentro de la aplicación para explicar a tus clientes por qué quieres enviarles notificaciones push y cómo habilitar push les beneficiará. Este proceso se llama [preparación para push]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages).