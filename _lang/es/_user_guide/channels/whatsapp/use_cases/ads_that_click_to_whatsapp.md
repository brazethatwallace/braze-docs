---
nav_title: "Anuncios que redirigen a WhatsApp"
article_title: "Anuncios que redirigen a WhatsApp"
page_order: 1
description: "Este artículo de referencia proporciona una guía paso a paso para configurar y usar anuncios que redirigen a WhatsApp."
page_type: reference
alias: /whatsapp_use_cases/
channel:
  - WhatsApp
---

# Anuncios que redirigen a WhatsApp {#ads-that-click-to-whatsapp}

> Esta página proporciona una guía paso a paso para configurar y usar anuncios que redirigen a WhatsApp, para que tú y tu equipo puedan potenciar su programa de WhatsApp.

Los anuncios que redirigen a WhatsApp son una forma eficiente de atraer tanto a clientes nuevos como existentes desde anuncios de Meta en Facebook, Instagram u otras plataformas. Usa estos anuncios para promocionar tus productos y servicios mientras haces que los usuarios conozcan tu presencia en WhatsApp.

![Un anuncio de Facebook de Calorie Rocket que promociona entrega gratuita, y la conversación de WhatsApp correspondiente que ocurre cuando un usuario selecciona el botón del anuncio.]({% image_buster /assets/img/whatsapp/ads_that_click_whatsapp.png %}){: style="max-width:70%;"}

## Configuración de anuncios que hacen clic a WhatsApp {#setting-up-ads-that-click-to-whatsapp}

1. En Meta Ads Administrador, crea un anuncio en Facebook, Instagram u otras plataformas siguiendo la guía paso a paso [Cómo crear anuncios que hacen clic a WhatsApp](https://business.whatsapp.com/products/create-ads-that-click-to-whatsapp). **No** configures respuestas automatizadas; configurarás las respuestas en Braze en su lugar.

![Ads Manager con un creador para crear un anuncio de participación.]({% image_buster /assets/img/whatsapp/meta_ads_composer.png %})

Al configurar el mensaje prellenado, que será enviado por el usuario a tu cuenta de WhatsApp Business, incluye una palabra o frase específica que usarás para desencadenar una respuesta específica para ese anuncio en particular. En este ejemplo, una aplicación de entrega de comida usa "free delivery" porque eso es lo que se promociona en su anuncio.

![Creador de plantillas de Ads Manager con un mensaje prellenado de "I want free delivery".]({% image_buster /assets/img/whatsapp/pre_filled_message.png %})

{% alert tip %}
Deja claro en la descripción del anuncio que al hacer clic en el anuncio se iniciará una conversación con tu marca usando frases como "Chatea ahora en WhatsApp".
{% endalert %}

{: start="2"}
2. En Braze, configura un Canvas basado en acciones donde la opción basada en acciones sea **Send a WhatsApp inbound message** y el cuerpo del mensaje sea "TU_PALABRA_DESENCADENANTE". En este ejemplo, una aplicación de entrega de comida usa "free delivery".

![Programación de entrada para un Canvas de Braze basado en acciones, con el evento desencadenante de "Send a WhatsApp inbound message" y un cuerpo de mensaje que coincide con regex de "free delivery".]({% image_buster /assets/img/whatsapp/action_based_free_delivery.png %})

{: start="3"}
3. Configura un mensaje de respuesta en el Canvas que se envíe inmediatamente después de que el cliente entre en el Canvas (por ejemplo, sin demora). Aunque hacer clic en el anuncio técnicamente constituye una adhesión voluntaria, te recomendamos configurar tu mensaje de respuesta para preguntar al usuario si desea recibir futuros mensajes de marketing de tu parte en WhatsApp.

{% alert tip %}
Configura tu mensaje de respuesta con respuestas rápidas (como "Sí" o "No, gracias") para que los usuarios puedan indicar rápidamente si desean adherirse.
{% endalert %}

¡No olvides proporcionar también cualquier código de descuento, oferta u otra información prometida en el anuncio!

![Creador de mensajes de WhatsApp con respuestas de botón de "Yes" y "No Thanks".]({% image_buster /assets/img/whatsapp/quick_replies.png %})

![Paso en Canvas con un grupo "Opting in" con un evento desencadenante de "Sent inbound WhatsApp to subscription group" y una palabra desencadenante de "YES".]({% image_buster /assets/img/whatsapp/opting_in_step.png %})

{: start="4"}
4. Adhiere a los usuarios actualizando el estado de suscripción de los perfiles de usuario con uno de los siguientes métodos de actualización:
    - Crea un webhook de Braze a Braze que actualice el estado de suscripción a través de la REST or transferencia de estado representacional API.
    - Usa el editor JSON avanzado para actualizar el perfil de usuario con la plantilla para [actualizar el estado de suscripción de un usuario a un Canvas de WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups#whatsapp-opt-in-and-opt-out-process).

![Paso de actualización de usuario en Canvas que usa el editor JSON avanzado para actualizar el perfil de usuario.]({% image_buster /assets/img/whatsapp/user_update_step_json.png %})

![Canvas que muestra el flujo de trabajo para enviar anuncios que hacen clic a WhatsApp, incluyendo tres Rutas de Acción: adhesión voluntaria, exclusión voluntaria y todos los demás.]({% image_buster /assets/img/whatsapp/ads_that_click_canvas.png %})

## Consideraciones {#considerations}

Las conversaciones que comienzan a partir de un anuncio que redirige a WhatsApp son gratuitas si se cumplen las siguientes condiciones:

- Si un usuario te envía un mensaje a través de un [punto de entrada gratuito](https://developers.facebook.com/docs/whatsapp/pricing#free-entry-point-conversations), como un anuncio que redirige a WhatsApp, se abre una [ventana de servicio al cliente](https://developers.facebook.com/docs/whatsapp/cloud-api/guides/send-messages#customer-service-windows) de 24 horas en la que puedes enviar a ese usuario cualquier tipo de mensaje.
- Si respondes dentro de la ventana de servicio al cliente (en un plazo de 24 horas), se abre un punto de entrada gratuito durante 72 horas, y todos los mensajes dentro de esa ventana de 72 horas serán gratuitos.