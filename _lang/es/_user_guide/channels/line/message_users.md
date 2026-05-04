---
nav_title: Enviar mensajes a usuarios
article_title: Enviar mensajes a usuarios
page_order: 3
description: "Este artículo de referencia cubre cómo chatear con usuarios usando Campaigns y Canvas con plantillas."
page_type: reference
channel:
 - LINE
alias: /line/messaging_users/
---

# Enviar mensajes a usuarios de LINE {#message-line-users}

> LINE es un canal de comunicación bidireccional. Puedes ir más allá de enviar mensajes a los usuarios y entablar conversaciones con ellos usando Campaigns y Canvas con plantillas. Este artículo cubre los detalles del envío de mensajes a usuarios, como la configuración de palabras desencadenantes para mensajes de entrada y respuestas no reconocidas.

Existen varios métodos para conversar con los usuarios a través de LINE, como el uso de palabras desencadenantes de LINE. También puedes usar llamadas a la acción (CTA) para fomentar la interacción de los usuarios con tus mensajes de LINE.

## Desencadenantes basados en acciones {#action-based-triggers}

Puedes crear Campaigns y Canvas que se inicien, se ramifiquen y tengan cambios a mitad de recorrido cuando recibas un mensaje de LINE de entrada (un mensaje enviado por un usuario) que contenga una palabra desencadenante. Asegúrate de elegir palabras desencadenantes que coincidan con lo que esperas que los usuarios envíen.

### Campaign

Configura tus palabras desencadenantes al programar una Campaign con entrega basada en acciones.

![Desencadenante basado en acciones que dice "Enviar esta campaña a los usuarios que enviaron un LINE de entrada al grupo de suscripción donde el cuerpo del mensaje es" y un campo en blanco.]({% image_buster /assets/img/line/trigger_word_campaign.png %})

### Canvas

Configura tus palabras desencadenantes dentro de las [rutas de acción]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths/) en tu Canvas.

![Ruta de acción con un desencadenante que dice "Enviar esta campaña a los usuarios que enviaron un LINE de entrada al grupo de suscripción donde el cuerpo del mensaje es" y un campo en blanco.]({% image_buster /assets/img/line/trigger_word_canvas.png %})

### Requisitos {#requirements}

Cada letra de tu palabra desencadenante debe estar en mayúsculas al crear tu Campaign o Canvas, aunque Braze no requiere que las palabras desencadenantes de entrada estén en mayúsculas. Por ejemplo, si tu palabra desencadenante es "JOIN2023", un mensaje de entrada de "jOin2023" seguirá activando el Canvas o la Campaign.

Si no se especifica ninguna palabra desencadenante, la Campaign o el Canvas se ejecutará para *todos* los mensajes de LINE de entrada. Esto incluye mensajes que coincidan con frases en Campaigns y Canvas activos, en cuyo caso el usuario recibirá dos mensajes de LINE.

## Respuestas no reconocidas {#unrecognized-responses}

Deberías incluir una opción de desencadenante para respuestas no reconocidas en Canvas interactivos. Esto informa a los usuarios sobre los comandos disponibles (o palabras desencadenantes) y establece sus expectativas para el canal.

### Crear un desencadenante para respuestas no reconocidas {#creating-a-trigger-for-unrecognized-responses}

Después de crear grupos de acciones para las frases de filtro personalizadas, añade otro grupo de acciones a la ruta de acción para **Send LINE message** y no marques **Where the message body**. Esto capturará todas las respuestas no reconocidas de los usuarios, de forma similar a una cláusula "else".

Para este mensaje, deberías enviar un mensaje de LINE informando al usuario de que este canal no está monitoreado por una persona y, si es necesario, guiarlo hacia un canal de soporte.