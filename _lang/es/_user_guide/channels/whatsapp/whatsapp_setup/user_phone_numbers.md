---
nav_title: "Números de teléfono de usuario"
article_title: Números de teléfono de usuario de WhatsApp
page_order: 3
description: "Este artículo de referencia cubre el formato de números de teléfono de WhatsApp, cómo importar números de teléfono, así como cómo añadir usuarios a grupos de suscripción de WhatsApp."
page_type: reference
channel:
  - WhatsApp

---

# Números de teléfono de usuario {#user-phone-numbers}

> Este artículo abordará diferentes temas relacionados con los números de teléfono de tus usuarios o clientes.

Los números de teléfono se muestran en el perfil de usuario en formatos locales, pero no estarán en el formato que usas para importar el número (`(724) 123 4567`).

## Importar números de teléfono {#importing-phone-numbers}

Puedes importar números de teléfono [cargando un CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/#csv) o [a través de la API]({{site.baseurl}}/api/endpoints/user_data/#user-track-endpoint) para crear un usuario.

### Formato {#formatting}

Es importante importar los números no estadounidenses en formato [`E.164`](https://en.wikipedia.org/wiki/e.164), incluyendo el "+" y el código de país. Cualquier número de teléfono que no se proporcione en este formato se interpretará como un número de EE. UU.

Si un número de teléfono se convierte al formato E.164 pero no pasa la validación, Braze no podrá enviar mensajes de WhatsApp a este número. Cualquier usuario con números de teléfono que no se puedan formatear saldrá automáticamente de un paso en Canvas que incluya WhatsApp.

Todos los números de EE. UU. deben ser números de teléfono válidos de 10 dígitos con un código de área válido. Se pueden introducir sin el `+` y el código de país, ya que Braze asumirá y mapeará todos los números válidos de 10 dígitos como números de EE. UU.

Todos los números internacionales deben comenzar con un `+`, seguido de su código de país y luego el número de teléfono (por ejemplo, `+442071838750`).

![]({% image_buster /assets/img/sms/e164.png %}){: style="max-width:50%;border: 0;"}

Sin embargo, para garantizar la precisión en caso de que estés enviando a múltiples regiones con diferentes códigos de país o de área, se recomienda usar el formato `E.164`, incluso para números de teléfono con sede en EE. UU.

Puedes ver las diferencias entre el formato de número local y el formato universal `E.164` en la siguiente tabla:

| País | Local | Código de país | `E.164` |
|---|---|---|---|
| EE. UU. | `4155552671` | 1 | `+14155552671` |
| Reino Unido | `02071838750` | 44 | `+442071838750` |
| Brasil | `1155256325` | 55 | `+551155256325` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Formato" }

### Añadir usuarios a un grupo de suscripción de WhatsApp {#adding-users-to-whatsapp-a-subscription-group}

Para que un cliente reciba un mensaje de WhatsApp, debe tener un número de teléfono válido y estar suscrito a un grupo de suscripción. Para más información, consulta [Grupos de suscripción de WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups/).


### Múltiples usuarios con el mismo número de teléfono {#multiple-users-with-the-same-phone-number}

Si múltiples usuarios tienen el mismo número de teléfono dentro de un segmento de una sola campaña o paso en Canvas, Braze deduplicará el envío y enviará solo un mensaje a ese número de teléfono.