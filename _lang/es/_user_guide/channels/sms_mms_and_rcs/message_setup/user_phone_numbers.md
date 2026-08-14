---
nav_title: "Números de teléfono de usuario"
article_title: Números de teléfono de usuario de SMS
page_order: 3
description: "Este artículo de referencia cubre el formato de números de teléfono SMS, cómo importar números de teléfono, así como cómo añadir usuarios a grupos de suscripción SMS."
page_type: reference
alias: /user_phone_numbers/
channel:
  - SMS
  - MMS
  - RCS
---

# Números de teléfono de usuario {#user-phone-numbers}

> Este artículo abordará diferentes temas relacionados con los números de teléfono de tus usuarios o clientes. Si buscas información sobre tus propios números, consulta nuestro artículo sobre [números de teléfono de envío]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup).

## Formato recomendado {#recommended-format}

Recomendamos importar los números de teléfono en formato [`E.164`](https://en.wikipedia.org/wiki/e.164) para garantizar la precisión en caso de que envíes a múltiples regiones con diferentes códigos de país o área&#8212;incluso para números de teléfono con sede en EE. UU.

- **Números de EE. UU.:** Todos los números de EE. UU. deben ser números de teléfono válidos de 10 dígitos con un código de área válido. Si a algún número de teléfono de 10 dígitos le falta un `+` y el código de país, Braze lo asignará como número de EE. UU. Los números de teléfono de Puerto Rico aún requieren un `+` y el código de país, aunque utilicen un formato de 10 dígitos con códigos de área de estilo estadounidense.
- **Números internacionales:** Todos los números internacionales deben comenzar con un `+`, seguido de su código de país y luego el número de teléfono. Por ejemplo, `+442071838750`.

![Ejemplo de un número de teléfono internacional válido en formato e164.]({% image_buster /assets/img/sms/e164.png %}){: style="max-width:50%;border: 0;"}

Aquí tienes algunos ejemplos que muestran las diferencias entre el formato local y el formato `E.164`:

| País | Local | Código de país | `E.164` |
|---|---|---|---|
| EE. UU. | `4155552671` | 1 | `+14155552671` |
| Reino Unido | `2071838750` | 44 | `+442071838750` |
| Brasil | `1155256325` | 55 | `+551155256325` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Formato recomendado" }

## Importar números de teléfono {#import-phone-numbers}

Al importar números de teléfono, es importante que sigas el [formato recomendado](#recommended-format). Para importar números de teléfono, utiliza uno de los siguientes métodos:

- [Cargar un CSV a Braze]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#constructing-your-csv)
- [Usar el endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track)

{% alert important %}
Los números de teléfono de los usuarios aparecen en Braze como una cadena de dígitos. Si importas un número que contiene caracteres que no son dígitos (como `,`, `-` o `(`) distintos del {% raw %}`+`{% endraw %} inicial, los caracteres no numéricos se eliminan cuando se muestran en Braze. Por ejemplo, importar `+1 (724) 123-4567` aparece como `+17241234567`.
{% endalert %}

## Validación de números de teléfono {#phone-number-validation}

Braze utiliza la biblioteca [libphonenumber](https://github.com/google/libphonenumber) de Google para validar números de teléfono. Cuando se introducen nuevos prefijos de números móviles, el soporte se añade a medida que se actualiza la biblioteca de origen. Braze no mantiene una lista separada de prefijos válidos.

### Gestión de números de teléfono no válidos {#handling-invalid-phone-numbers}

Cuando un número de teléfono se considera no válido, Braze marcará el número de teléfono del usuario como no válido y no intentará enviar más comunicaciones a ese número de teléfono. Un número de teléfono no válido se marca en la **pestaña de interacción** del perfil de usuario.

![Ejemplo de mensaje de error para números de teléfono no válidos en Braze.]({% image_buster /assets/img/sms/invalid_banner.png %}){: style="max-width:50%;border: 0;"}

Un número de teléfono se considera no válido por las siguientes razones:

- **Error del proveedor**: se recibió un error permanente del proveedor de SMS y RCS. Esto indica que el número de teléfono proporcionado tiene un formato incorrecto o no puede recibir mensajes SMS o RCS de forma permanente.
- **Desactivado**: el número de teléfono ha sido desactivado porque un suscriptor móvil canceló su servicio y liberó su número de su operador (y eventualmente puede ser reciclado y asignado a un nuevo usuario). Un número de teléfono desactivado puede marcarse como no válido incluso si no has enviado ningún mensaje SMS o RCS a ese número de teléfono.

Estos números de teléfono no válidos se pueden gestionar utilizando [endpoints de SMS y RCS]({{site.baseurl}}/api/endpoints/sms).

{% alert note %}
Si varios perfiles de usuario tienen el mismo número de teléfono y ese número se marca como no válido, todos los perfiles de usuario existentes con ese número se mostrarán como no válidos. Los perfiles de usuario recién creados nunca se marcarán inicialmente como no válidos.
{% endalert %}

También puedes incluir o excluir cualquier usuario con números de teléfono no válidos al [crear un segmento]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment#step-4-add-filters-to-your-segment).

## Excluir envíos de SMS rechazados de la segmentación {#exclude-rejected-sms-sends-from-segmentation}

{% alert important %}
Los rechazos de SMS se cobran de tu asignación de SMS.
{% endalert %}

Para excluir de tus segmentos a los usuarios con envíos de SMS rechazados, utiliza [extensiones de segmento SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments) y haz lo siguiente:

1. Ve a **Audiencia** > **Extensiones de segmento**.
2. Selecciona **Crear nueva extensión** > **Actualización completa** o **Actualización incremental**.
3. Escribe una consulta SQL que identifique a los usuarios con rechazos de SMS. Por ejemplo, puedes consultar el evento `USERS_MESSAGES_SMS_REJECTION_SHARED` para encontrar usuarios que hayan recibido rechazos de SMS.
4. Guarda tu extensión de segmento.
5. Al crear tu segmento de SMS, añade un filtro para excluir a los usuarios en esta extensión de segmento.

## Añadir usuarios a grupos de suscripción de SMS y RCS {#add-users-to-sms-and-rcs-subscription-groups}

Para que un usuario reciba un mensaje SMS o RCS, debe tener un número de teléfono válido y estar suscrito a un grupo de suscripción. Los grupos de suscripción están vinculados al programa de SMS o RCS que estés ejecutando (asegúrate de cumplir con los [requisitos legales para SMS, MMS y RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations) y de haber registrado el consentimiento de cada cliente). Para más información, consulta [Grupos de suscripción de SMS y RCS]({{site.baseurl}}/sms_rcs_subscription_groups).

## Obtención y verificación de terceros {#third-party-sourcing-and-verification}

Braze depende de herramientas de terceros para obtener números no válidos. Braze no es responsable de interrupciones o información errónea de estos servicios. Por lo tanto, esta herramienta no debe utilizarse como tu único método de cumplimiento para verificar números no válidos.

## Captura de números de teléfono {#phone-number-capture}

Para capturar números de teléfono a través de mensajes dentro de la aplicación, consulta [Captura de números de teléfono]({{site.baseurl}}/phone_number_capture).