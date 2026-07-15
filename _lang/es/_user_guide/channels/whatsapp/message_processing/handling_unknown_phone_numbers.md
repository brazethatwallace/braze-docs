---
nav_title: "Gestionar números de teléfono desconocidos"
article_title: "Gestionar números de teléfono desconocidos"
description: "Este artículo de referencia explica cómo Braze gestiona los números de teléfono desconocidos de usuarios de WhatsApp."
page_type: reference
channel:
  - WhatsApp
page_order: 50
---

# Gestionar números de teléfono desconocidos {#handle-unknown-phone-numbers}

> Es posible que, después de poner en marcha WhatsApp con Braze, recibas mensajes de usuarios desconocidos. Los siguientes pasos describen cómo se procesan un usuario y un número no identificados.

## Flujo de trabajo de adhesión voluntaria/cancelación de suscripción y palabras clave personalizadas para números desconocidos {#opt-inout-and-custom-keyword-workflow-for-unknown-numbers}

Braze primero intentará encontrar un usuario con un número coincidente. Si no se encuentra ninguno, Braze gestiona automáticamente un número desconocido de una de estas dos formas:

1. **Si se ha configurado una palabra desencadenante con un [Canvas de adhesión voluntaria]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/opt_ins_and_opt_outs):**
- Braze crea un perfil anónimo
- Se asigna un alias de usuario al perfil con los siguientes detalles:
  - Un `alias_name` con el valor del número de teléfono proporcionado por el usuario
  - Un `alias_label` con el valor `phone`
- Nuestro sistema establece el atributo de teléfono
- El usuario se suscribe al grupo de suscripción correspondiente según la lógica configurada en el Canvas<br><br>
2. **Si no se ha configurado un Canvas de adhesión voluntaria:**
- Braze crea un perfil anónimo
- Se asigna un alias de usuario al perfil con los siguientes detalles:
  - Un `alias_name` con el valor del número de teléfono proporcionado por el usuario
  - Un `alias_label` con el valor `phone`
- Nuestro sistema establece el atributo de teléfono
- El estado de suscripción del usuario será de forma predeterminada `unsubscribed` para todos los grupos de suscripción de WhatsApp<br><br>