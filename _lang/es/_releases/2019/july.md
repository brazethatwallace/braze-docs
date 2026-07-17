---
nav_title: Julio
page_order: 6
noindex: true
page_type: update
description: "Este artículo contiene notas de la versión de julio de 2019."
---

# Julio de 2019 {#july-2019}

{% alert update %}
Braze ha tenido dos (has leído bien, **dos**) ciclos de lanzamiento de productos este mes. La última versión está anotada en la parte superior, ¡la anterior [empieza más abajo en esta página](#earlier-this-month)!
{% endalert %}

## SAML/SSO

[El inicio de sesión único]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on) (SSO) proporciona a las empresas una forma segura y centralizada de controlar el acceso al panel de Braze. En resumen, se puede utilizar un único conjunto de credenciales para acceder a diferentes aplicaciones, incluida Braze.

Además de la compatibilidad de [Google Sign-In con OAuth 2.0](https://developers.google.com/identity/protocols/OAuth2), a las empresas les gustaría que SSO fuera compatible con Security Assertion Markup Language (SAML). Esto les permite integrarse fácilmente con grandes proveedores de identidad (IdP), como [Azure Active Directory]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/microsoft_entra_sso) y [Okta]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/okta), que admiten los últimos estándares del sector (SAML 2.0).

Braze es compatible con:
- [OneLogin]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/onelogin)
- [Azure Active Directory]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/microsoft_entra_sso)
- [Okta]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/okta)

## Se muestra la clave de API de evento de Adjust {#adjust-event-api-key-shows}

Hemos actualizado la página del partner de Adjust para que los clientes puedan acceder a esta clave de API.

## Nuevos partners {#new-partners}

¡Algunos partners nuevos se unieron a nuestro programa Alloys y se agregaron a nuestra documentación! Saluda a:
- [FiveTran]({{site.baseurl}}/partners/fivetran)
- [Talon.One]({{site.baseurl}}/partners/talonone)
- [Voucherify]({{site.baseurl}}/partners/voucherify)

## Mejora de los detalles de Campaign {#campaign-details-improvement}

Los detalles ampliados de Campaign se muestran ahora en la sección... espera... **Campaign Details** de la página de **Campaign**.

## Mostrar solo las mías en Segments y Canvas {#show-only-mine-in-segments-canvas}

El filtro "Mostrar solo las mías" de la página de **Campaigns** ha demostrado ser muy popular. Como resultado, ¡también vamos a añadir esta opción a las listas de Canvas y Segments!

### Comportamiento de avance {#advancement-behavior}

Ahora puedes elegir [cuándo un usuario avanza]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/cloning_canvases) de un paso en Canvas al siguiente. Estas opciones incluyen "Message Sent" y "Entire Audience After Delay".

### Mensajes dentro de la aplicación en Canvas {#in-app-messages-in-canvas}

¡[Los mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas) ya están disponibles en Canvas! Añade un paso en Canvas y explora los canales disponibles para añadir un mensaje dentro de la aplicación.

# A principios de este mes {#earlier-this-month}

## Eliminación de la imagen del perfil de usuario {#user-profile-image-removal}

Estamos eliminando las fotos de perfil de usuario que aparecen en los perfiles de usuario de Braze y en las búsquedas de usuarios.

## Contenido conectado en Content Cards {#connected-content-in-content-cards}

Ahora puedes utilizar cadenas y funciones de [contenido conectado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content#about-connected-content) en las [Content Cards]({{site.baseurl}}/user_guide/channels/content_cards).

Las llamadas de contenido conectado a servidores externos se producirán cuando se envíe realmente una tarjeta, no cuando el usuario vea la tarjeta. Al igual que en el correo electrónico, el contenido dinámico se calculará y determinará en el momento del envío, y no cuando se visualice realmente una tarjeta.

## Dirección "responder a" nula {#null-reply-to-address}

Ahora los clientes pueden establecer un valor `null` para la dirección "responder a" de un mensaje de correo electrónico desde la página **Configuración del correo electrónico** en Braze o utilizando la [API]({{site.baseurl}}/api/objects_filters/messaging/email_object). Si se utiliza, las respuestas se enviarán a la dirección "De" indicada. Ahora puedes personalizar el campo de dirección "De" como `dan@emailaddress.com`, y tus clientes podrán responder directamente a Dan.

Para establecer un valor `null` para la dirección "responder a" de un mensaje de correo electrónico de Braze, ve a **Administrar configuración** en la navegación y, a continuación, a la pestaña **Configuración del correo electrónico**. Desplázate hasta la sección **Configuración de correo electrónico saliente** y selecciona **Excluir "Responder a" y enviar respuestas a "De"** como dirección predeterminada.

## Comparaciones de Campaigns {#campaign-comparisons}

Mira [varias Campaigns a la vez para comparar su rendimiento relativo]({{site.baseurl}}/report_builder), una al lado de la otra en Braze, ¡en una sola ventana!

## Plantilla del ID de envío en mensajes con Liquid {#template-dispatch-id-into-messages-with-liquid}

{% alert note %}
El comportamiento de `dispatch_id` difiere entre Canvas y Campaigns porque Braze trata los pasos en Canvas (excepto los pasos de entrada, que pueden programarse) como eventos desencadenados, incluso cuando están "programados". Más información sobre [el comportamiento de `dispatch_id`]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/dispatch_id) en Canvas y Campaigns.
{% endalert %}

Si quieres hacer un seguimiento del envío de un mensaje desde dentro del mensaje (en una URL, por ejemplo), puedes utilizar la plantilla `dispatch_id`. Puedes encontrar el formato para ello en nuestra lista de etiquetas de personalización compatibles, en [Canvas Attributes]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags).

Esto se comporta igual que `api_id`, en el sentido de que como `api_id` no está disponible en el momento de crear la Campaign, se incluye en la plantilla como marcador de posición y se previsualizará como `dispatch_id_for_unsent_campaign`. El ID se genera antes de enviar el mensaje y se incluirá en el momento del envío.

{% alert warning %}
La plantilla Liquid de `dispatch_id_for_unsent_campaign` no funciona con los mensajes dentro de la aplicación, ya que los mensajes dentro de la aplicación no tienen `dispatch_id`.
{% endalert %}

## La configuración "Mostrar solo las mías" persiste {#show-only-mine-setting-persists}

El filtro "Mostrar solo las mías" de la cuadrícula de Campaigns permanecerá activado siempre que visites la página **Campaigns**.

## Actualizaciones de las pruebas A/B {#ab-testing-updates}

Puedes enviar una única [prueba A/B]({{site.baseurl}}/user_guide/messaging/ab_testing) con hasta ocho variantes (y un control opcional) a un porcentaje especificado por el usuario de la audiencia de una Campaign, y luego enviar la mejor variante a la audiencia restante a una hora programada previamente.