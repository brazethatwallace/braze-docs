---
nav_title: "Mensajes dentro de la aplicación"
article_title: "Mensajes dentro de la aplicación"
page_order: 5
page_type: landing
alias: /in-app_messages/
description: "Involucra a los usuarios con mensajes dentro de la aplicación personalizados que mejoran la experiencia del usuario utilizando una variedad de diseños y herramientas de personalización en Braze."
channel:
  - in-app messages
search_rank: 5
---

# Mensajes dentro de la aplicación {#in-app-messages}

> Los mensajes dentro de la aplicación te ayudan a hacer llegar contenido a tus usuarios sin interrumpir su día con una notificación push. Los mensajes dentro de la aplicación personalizados y adaptados mejoran la experiencia del usuario y ayudan a tu audiencia a obtener el máximo valor de tu aplicación. Con una variedad de diseños y herramientas de personalización entre las que elegir, los mensajes dentro de la aplicación involucran a tus usuarios más que nunca.

## Requisitos previos {#prerequisites}

Antes de poder enviar mensajes dentro de la aplicación, necesitas integrar el [SDK de Braze]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=web) en tu aplicación o sitio web. No se requiere ninguna configuración adicional.

Para las versiones mínimas del SDK y los requisitos específicos de cada característica, consulta:
- [Editor de arrastrar y soltar]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop)
- [Tipos de mensaje]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types)

## Casos de uso {#use-cases}

Con el rico nivel de contenido que ofrecen los mensajes dentro de la aplicación, puedes aprovechar este canal para una variedad de casos de uso:

| Caso de uso | Explicación |
| --- | --- |
| Preparación para push | Ejecuta una Campaign de [preparación para push]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages) utilizando un mensaje enriquecido dentro de la aplicación para mostrar a tus clientes el beneficio de optar por las notificaciones push de tu aplicación o sitio, y presentarles una solicitud para conceder permiso de push.
| Ventas y promociones | Usa mensajes modales dentro de la aplicación para recibir a los clientes con contenido multimedia visualmente atractivo que contenga códigos promocionales estáticos u ofertas. Incentívalos a realizar compras o conversiones cuando de otro modo no lo habrían hecho. |
| Fomentar la adopción de características | Anima a los clientes a usar otras partes de tu aplicación o a aprovechar un servicio. |
| Campaigns altamente personalizadas | Coloca mensajes dentro de la aplicación como lo primero que tus clientes ven cuando entran en tu aplicación o sitio. Añade algunas características de personalización de Braze, como [Contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content), para impulsar a los usuarios a tomar acción y así hacer que tu alcance sea más efectivo.
{: .reset-td-br-1 .reset-td-br-2 aria-label="Casos de uso" }

Otros casos de uso a considerar incluyen los siguientes:

- Nuevas características de la aplicación
- Gestión de la aplicación
- Reseñas
- Actualizaciones de la aplicación
- Sorteos y concursos

## Tipos de mensaje estándar {#standard-message-types}

Las siguientes pestañas muestran cómo se ve para tus usuarios abrir uno de nuestros tipos de mensaje estándar dentro de la aplicación: deslizamiento hacia arriba, modal y mensajes dentro de la aplicación a pantalla completa.

{% tabs %}
{% tab Deslizamiento hacia arriba %}

Los mensajes de deslizamiento hacia arriba suelen aparecer en la parte superior e inferior de la pantalla de la aplicación (puedes configurar esto cuando creas tu mensaje). Son ideales para alertar a tus usuarios sobre nuevos términos de servicio, cookies y otros fragmentos de información.

![Mensaje dentro de la aplicación de deslizamiento hacia arriba que aparece desde la parte inferior de la pantalla de la aplicación. El deslizamiento incluye un icono de imagen y un mensaje breve.]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Modal %}

Los modales aparecen en el centro de la pantalla del dispositivo con una superposición de pantalla que ayuda a destacarlos del fondo de tu aplicación. Son perfectos para sugerir de forma evidente que tu usuario aproveche una venta o sorteo.

![Mensaje modal dentro de la aplicación que aparece en el centro de una aplicación y un sitio web como un diálogo. El modal incluye una imagen, encabezado, cuerpo del mensaje y dos botones.]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Pantalla completa %}

Los mensajes a pantalla completa son exactamente lo que esperarías: ocupan toda la pantalla del dispositivo. Este tipo de mensaje es ideal cuando realmente necesitas la atención de tu usuario, como para actualizaciones obligatorias de la aplicación.

![Mensaje dentro de la aplicación a pantalla completa que ocupa la pantalla de una aplicación. El mensaje a pantalla completa incluye una imagen grande, encabezado, cuerpo del mensaje y dos botones.]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% endtabs %}

Además de estas plantillas de mensaje predeterminadas, también puedes personalizar aún más tu mensajería utilizando mensajes dentro de la aplicación con HTML personalizado, modales web con CSS o formularios de captura de correo electrónico web. Para más información, consulta [Personalizar]({{site.baseurl}}/user_guide/channels/in_app_messages/customize).

Para saber cómo la entrega con plantilla en el momento de la visualización afecta el registro de **cancelación**, consulta [Preguntas frecuentes sobre mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/channels/in_app_messages/faq).

## Próximos pasos {#next-steps}

- [Crea un mensaje dentro de la aplicación con el editor de arrastrar y soltar]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop)
- [Crea un mensaje dentro de la aplicación con el editor tradicional]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional)

{% multi_lang_include alerts/important_alerts.md alert='network dependency' %}