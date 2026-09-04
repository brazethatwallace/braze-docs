---
nav_title: Comprender las instalaciones de usuarios
article_title: Comprender las instalaciones de usuarios
page_order: 7
page_type: reference
description: "Este artículo de referencia describe las instalaciones de usuarios (seguimiento de atribución de instalación) y las diferentes formas de aplicar esta información en tu campaña."
tool:
  - Campaigns
  - Segments
---

# Comprender las instalaciones de usuarios {#understanding-user-installs}

> El seguimiento de atribución de instalación es una excelente manera de mejorar tu relación inicial con tu usuario. Saber cómo, dónde y, lo que es aún más importante, por qué un usuario instala tu aplicación te permite comprender mejor quién es tu usuario y cómo deberías presentarle tu aplicación.

Aunque Braze no proporciona seguimiento de atribución de instalación, podemos integrarnos con [servicios]({{site.baseurl}}/partners/message_orchestration) como Branch y AppsFlyer para proporcionarte fácilmente datos de instalación.

## Segmenta a tus usuarios {#segment-your-users}

Una vez que tu usuario instala tu aplicación, puedes empezar a segmentarlo en función de los siguientes [filtros de atribución de instalación]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#install-attribution). Por ejemplo, una aplicación de viajes podría añadir a los usuarios que llegaron a través de un anuncio relacionado con ofertas de vacaciones en la playa a un Segment "Amantes de la playa". Del mismo modo, una aplicación de música podría segmentar a los usuarios en función del género musical mostrado en el anuncio que llevó a la instalación.

## Buenas prácticas {#best-practices}

### Incorporación personalizada {#personalized-onboarding}

Ahora que tienes más información sobre tu usuario, puedes personalizar su proceso de incorporación. Esto podría ser tan simple como cambiar las imágenes en tus mensajes para que se ajusten a sus preferencias, o tan complejo como crear una incorporación de usuario única para cada anuncio que pueda conducir a una instalación. Para escalar una secuencia totalmente completa de mensajes que pueda tener en cuenta el comportamiento del usuario, consulta nuestra documentación sobre [Canvas]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases).

### Datos de referencia del anuncio {#reference-data-from-the-ad}

Los usuarios pueden sentirse atraídos por tu aplicación gracias a una oferta promocional o un sorteo. Usar datos de atribución de instalación te permite enviar Campaigns que contengan códigos de descuento u ofertas solo a los usuarios que instalaron la aplicación gracias a estas promociones. De forma similar, si tu anuncio contiene información sobre un producto en particular (como una película específica en una aplicación de video o una oferta en una aplicación de comercio electrónico), puedes enviar Campaigns que dirijan a los usuarios a la página correcta de tu aplicación.

## Evaluar los esfuerzos publicitarios {#evaluate-advertising-efforts}

Los datos de atribución de instalación pueden ser valiosos para evaluar la efectividad de diferentes Campaigns de marketing. Revisar qué anuncios y Campaigns están generando la mayor cantidad de instalaciones y cuáles se están quedando atrás puede usarse para enfocar tus recursos en los anuncios más atractivos.