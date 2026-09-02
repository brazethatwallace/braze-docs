---
nav_title: Gestionar números de teléfono desconocidos
article_title: Gestionar números de teléfono desconocidos
page_order: 3
description: "Este artículo de referencia explica cómo Braze procesa los números de teléfono desconocidos de nuevos usuarios."
page_type: reference
channel:
  - SMS
  - MMS
  - RCS

---

# Gestionar números de teléfono desconocidos: nuevos usuarios {#handle-unknown-phone-numbers-new-users}

> Es posible que, después de poner en marcha servicio de mensajes cortos, MMS y RCS con Braze, recibas mensajes de usuarios desconocidos. Los siguientes pasos describen cómo se procesan un usuario y un número no identificados.

## Flujo de trabajo de adhesión voluntaria/cancelación de suscripción y palabras clave personalizadas para números desconocidos {#opt-inout-and-custom-keyword-workflow-for-unknown-numbers}

Braze gestiona automáticamente un número desconocido de una de estas tres formas:

1. Si se envía por mensaje de texto una palabra clave de adhesión voluntaria:
  * Braze crea un perfil anónimo
  * Nuestro sistema establece el atributo de teléfono
  * Suscribe al usuario al grupo de suscripción correspondiente en función de la palabra clave de adhesión voluntaria recibida por Braze.<br><br>
2. Si se envía por mensaje de texto una palabra clave de cancelación de suscripción:
  * Braze crea un perfil anónimo
  * Nuestro sistema establece el atributo de teléfono
  * Cancela la suscripción del usuario del grupo de suscripción correspondiente en función de la palabra clave de cancelación de suscripción recibida por Braze.<br><br>
3. Si se envía por mensaje de texto cualquier otra palabra clave personalizada:
  * Braze ignora el mensaje de texto y no realiza ninguna acción.