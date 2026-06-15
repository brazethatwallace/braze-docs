---
nav_title: Septiembre
page_order: 4
noindex: true
page_type: update
description: "Este artículo contiene notas de la versión de septiembre de 2019."
---

# Septiembre de 2019 {#september-2019}

## Aplicación Braze dentro de OneLogin {#braze-app-within-onelogin}

Los clientes podrán simplemente buscar y seleccionar Braze dentro de [OneLogin]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/onelogin/) para iniciar sesión como SP o IdP. Esto significa que los clientes no tendrán que añadir una aplicación personalizada dentro de OneLogin. Como resultado, esto debería rellenar previamente ciertos ajustes como los atributos que hemos visto surgir desde el lanzamiento de SAML SSO.

## Asociación con Rokt Calendar {#rokt-calendar-partnership}

[Rokt Calendar]({{site.baseurl}}/partners/home/) ofrece a los clientes de Braze la posibilidad de alinear sus iniciativas de marketing personalizado y ampliar el contenido personalizado al calendario del usuario final. De este modo, se consigue una experiencia más fluida para el usuario final y se desarrolla aún más la adherencia a los servicios de nuestros clientes. Los clientes podrán...

- Enviar una invitación de calendario a través de la plataforma Braze para "guardar la fecha" y ampliar nuestra comunicación.
- Actualizar una invitación existente si el contenido del evento ha cambiado.

## Asociación con Passkit {#passkit-partnership}

Con [Passkit]({{site.baseurl}}/partners/additional_channels_and_extensions/additional_channels/mobile_wallet/passkit/), los clientes de Braze podrán ampliar su interacción con los clientes a la billetera móvil. Podrán personalizar campañas de billetera utilizando la potente segmentación de Braze y orquestarlas junto con canales como push, mensajes dentro de la aplicación y más.

## Devolución del valor del ID de envío a través de los puntos finales de mensajería {#dispatch-id-value-return-via-messaging-endpoints}

El `dispatch_id` de un mensaje se incluirá en las siguientes respuestas del punto final de mensajería:
- [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/#sending-messages-via-API-triggered-delivery)
- [`/campaigns/trigger/schedule`]({{site.baseurl}}/api/endpoints/messaging/#create-schedule-endpoint)
- [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/#sending-messages-immediately-via-api-only)
- [`/messages/schedule`]({{site.baseurl}}/api/endpoints/messaging/#create-schedule-endpoint)
- [`/canvases/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/#canvas)
- [`/canvases/trigger/schedule`]({{site.baseurl}}/api/endpoints/messaging/#api-triggered-canvases)

De este modo, los clientes que utilicen mensajería transaccional podrán rastrear la llamada a través de Currents.

## Registros de cambios de Canvas {#canvas-changelogs}

¿Alguna vez te has preguntado quién está trabajando en un Canvas en tu cuenta? ¡No te lo preguntes más! Ahora puedes acceder a los registros de cambios de Canvas.

![Registros de cambios de Canvas]({% image_buster /assets/img/canvas-changelog1.png %})
![Registros de cambios de Canvas]({% image_buster /assets/img/canvas-changelog2.png %})