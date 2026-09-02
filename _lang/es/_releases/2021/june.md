---
nav_title: Junio
page_order: 6
noindex: true
page_type: update
description: "Este artículo contiene notas de la versión de junio de 2021."
---

# Junio de 2021 {#june-2021}

## Campaigns de correo transaccional {#transactional-email-campaigns}

Los correos transaccionales son aquellos que se envían para facilitar una transacción acordada entre un remitente y el destinatario. La [Campaign de correo transaccional]({{site.baseurl}}/api/api_campaigns/transactional_campaigns) de Braze está diseñada específicamente para enviar mensajes de correo electrónico automatizados y no promocionales, como confirmaciones de pedidos, restablecimientos de contraseña, alertas de facturación u otras notificaciones de importancia crítica para el negocio. Además, se ha creado un [endpoint de correo transaccional]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message) correspondiente. Los correos transaccionales y el nuevo endpoint solo están disponibles como parte de paquetes de Braze seleccionados.

## Soporte de objetos anidados para propiedades del evento {#nested-object-support-for-event-properties}

Braze ahora admite [objetos anidados]({{site.baseurl}}/user_guide/data/activation/events/custom_events/nested_objects) para eventos personalizados y eventos de compra. Los objetos anidados te permiten enviar matrices de datos como propiedades de eventos personalizados y compras. Estos datos anidados se pueden utilizar para personalizar información en plantillas de mensajes desencadenados por API mediante el uso de Liquid y la notación de puntos.

## Nuevos filtros de Liquid HMAC {#new-hmac-liquid-filters}

Se han añadido a la plataforma Braze nuevos [filtros de codificación Liquid `hmac_sha1` y `hmac_sha256`]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters).

## Página de eventos de compra {#purchase-event-page}

¿Tienes curiosidad sobre los detalles de los eventos de compra en Braze? Visita nuestro artículo dedicado sobre [eventos de compra]({{site.baseurl}}/user_guide/data/activation/events/purchase_events) para obtener más información.

## Nuevas asociaciones de Braze {#new-braze-partnerships}

### Nexla - Automatización de flujos de trabajo {#nexla-workflow-automation}

[Nexla]({{site.baseurl}}/partners/nexla) es líder en operaciones de datos unificadas y fue reconocida como Gartner Cool Vendor en 2021. Los clientes que utilizan Currents para enviar datos a almacenes de datos pueden aprovechar Nexla para extraer, transformar y cargar esos datos en otras ubicaciones, haciendo que los datos sean fácilmente accesibles en todo tu ecosistema. Nexla te permite utilizar Braze Currents para obtener datos en un formato personalizado y entregarlos al destino de tu elección con solo apuntar y hacer clic.

### Amperity - CDP or plataforma de datos de los clientes or plataforma de datos de los clientes {#amperity-customer-data-platform}

[Amperity]({{site.baseurl}}/partners/amperity) es una plataforma integral de datos de clientes empresariales que ayuda a las marcas a conocer a sus clientes, tomar decisiones estratégicas y actuar de manera consistente para servir mejor a sus consumidores. Amperity es compatible con la plataforma Braze al proporcionar una vista unificada de tus clientes a través de su CDP or plataforma de datos de los clientes y Braze, lo que te permite enviar datos valiosos de Amperity a Braze.

### Digioh - Cuestionarios {#digioh-surveys}

[Digioh]({{site.baseurl}}/partners/digioh) te ayuda a hacer crecer tus listas, capturar datos propios y aprovechar tus datos en tus Campaigns de Braze. El constructor de arrastrar y soltar facilita la creación de formularios con tu imagen de marca, ventanas emergentes, centros de preferencias, páginas de destino y cuestionarios que te conectan con tus clientes.

### AppsFlyer Audiences - Atribución/Análisis {#appsflyer-audiences-attributionanalytics}

[AppsFlyer]({{site.baseurl}}/partners/message_orchestration/attribution/appsflyer) es una plataforma de análisis y atribución de marketing móvil que te ayuda a analizar y optimizar tus aplicaciones a través de análisis de marketing, atribución móvil y vinculación en profundidad. [AppsFlyer Audiences]({{site.baseurl}}/partners/appsflyer_audiences) te permite crear Segments de audiencia y pasarlos directamente a Braze para crear potentes Campaigns de interacción con los clientes.