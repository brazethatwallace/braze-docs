---
nav_title: Archivado de usuarios
article_title: Archivado de usuarios
permalink: /user_archival/
page_order: 0
page_type: reference
description: "Este artículo de referencia cubre las definiciones de archivado de usuarios, el bloqueo de correo no deseado y cómo personalizar tu política de archivado de usuarios."

---
# Archivado de usuarios {#user-archival}

> Cada semana, el domingo a las 5:30 am EST, Braze ejecuta un proceso para eliminar usuarios inactivos y usuarios latentes de los servicios de Braze. Ten en cuenta que Braze no archiva usuarios a menos que el número de usuarios en el espacio de trabajo alcance el umbral de 250.000.

Este proceso pretende ayudar a Braze a proporcionar estadísticas precisas sobre las audiencias alcanzables por las campañas. También sirve de acuerdo con dos conceptos clave del [RGPD][1]:

1. El principio de limitación del almacenamiento: los datos personales tratados y almacenados no deben conservarse más tiempo del necesario.
2. Tener un fin comercial legítimo para procesar datos personales.

Es decir, los datos personales procesados y almacenados no deben conservarse más tiempo del necesario, y los datos personales solo deben procesarse con fines comerciales legítimos. También se eliminará el estado de cancelación de suscripción de los usuarios archivados en cumplimiento del RGPD.

{% alert important %}
Los usuarios archivados serán eliminados permanentemente. <br><br>Puedes [personalizar tu política de archivado de usuarios](#customizing-your-user-archival-policy) utilizando Canvas. Los clientes tienen pleno control sobre si un usuario está inactivo o latente. Canvas ofrece la posibilidad de hacerlo automáticamente, lo que te permite desactivar eficazmente esta funcionalidad para algunos o todos tus usuarios inactivos o latentes.
{% endalert %}

## Definiciones de archivado de usuarios {#user-archival-definitions}

### Usuarios activos {#active-users}

Braze define un "usuario activo" para un período de tiempo determinado como cualquier usuario que ha registrado una sesión en una aplicación móvil o sitio web, ha sido actualizado, ha recibido un mensaje o ha interactuado con un mensaje.

Si configuras ID de usuario para identificar a los usuarios cuando un nuevo usuario inicia sesión, se contará como un usuario activo independiente. Los usuarios que se actualicen a través de la API también se contarán como usuarios activos en el período de tiempo en que se actualicen.

{% alert important %}
Tanto los usuarios inactivos como los usuarios inactivos prolongados se archivarán a menos que el usuario esté excluido del archivado por las razones que se indican a continuación.
{% endalert %}

### Usuarios inactivos {#inactive-users}

Los "usuarios inactivos" son usuarios a los que no se puede contactar y que probablemente han cancelado. Los usuarios inactivos son aquellos que cumplen todos estos criterios:

- No pueden recibir correo electrónico. Por ejemplo, no tienen una dirección de correo electrónico o han cancelado la suscripción de todas las listas de correo electrónico.
- No pueden recibir SMS. Por ejemplo, no tienen un número de teléfono válido o han cancelado la suscripción de todos los grupos de suscripción de SMS.
- No pueden recibir push. Por ejemplo, han desinstalado la aplicación o han desactivado los permisos de push.
- No pueden recibir un mensaje de WhatsApp. Por ejemplo, no tienen un número de teléfono válido o han cancelado la suscripción de todos los grupos de suscripción de WhatsApp.
- No pueden recibir un mensaje de LINE. Por ejemplo, no tienen un ID de LINE o han cancelado la suscripción de todos los grupos de suscripción de LINE.
- No han utilizado ninguna aplicación móvil ni han visitado un sitio web en un espacio de trabajo en más de seis meses.
- No han recibido ningún mensaje de un espacio de trabajo en más de seis meses.
- No han sido actualizados en más de seis meses.

En este caso, no se puede enviar mensajes a estos usuarios y no están interactuando con tu marca. Estos usuarios han cancelado de forma efectiva.

### Usuarios inactivos prolongados {#dormant-users}

Los "usuarios inactivos prolongados" son usuarios que no han tenido actividad en los últimos doce meses y:

- No han utilizado ninguna aplicación móvil ni han visitado un sitio web en un espacio de trabajo en más de 12 meses.
- No han recibido ningún mensaje de un espacio de trabajo en más de 12 meses.
- No han sido actualizados en más de 12 meses.

## Usuarios del grupo de control global {#global-control-group-users}

Los usuarios del grupo de control global nunca se archivarán, incluso si cumplen con la definición de usuarios inactivos.

### Grupo de muestra de tratamiento {#treatment-sample-group}

Los usuarios del grupo de muestra de tratamiento en un informe de grupo de control global están excluidos del archivado.

## Usuarios de prueba {#test-users}

Los usuarios de prueba nunca se archivarán, incluso si cumplen con la definición de usuarios inactivos.

## Bloqueo de correo no deseado {#spam-blocking}

Braze bloquea los perfiles de usuario individuales que crecen de forma anormalmente grande ("usuarios ficticios"), ya que suelen ser el resultado de una integración incorrecta. Un perfil se bloquea cuando supera cualquiera de los siguientes umbrales:

| Umbral | Descripción |
| --- | --- |
| Más de 5.000.000 de sesiones | Normalmente causado por reutilizar un único `external_id` en muchos usuarios. |
| Más de 20.000 nombres de eventos personalizados distintos | Normalmente causado por generar un nuevo nombre de evento para cada evento en lugar de reutilizar un conjunto fijo de nombres. |
| Más de 20.000 nombres de productos distintos en compras | Normalmente causado por generar un nuevo `product_id` para cada compra en lugar de reutilizar un conjunto fijo de ID de productos. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Umbrales de bloqueo de usuarios ficticios" }

Después de que un perfil es bloqueado, Braze deja de ingerir todos los datos entrantes para ese perfil, tanto de los SDK como de la REST API. Las solicitudes a [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) que hacen referencia a un identificador bloqueado devuelven el error `"provided external_id is blacklisted and disallowed"`. Este texto se toma literalmente de la respuesta de la API. Braze también notifica a tu director de cuentas de Braze para que pueda plantearte el problema de integración.

Si descubres que esto ha ocurrido con un usuario legítimo, abre un ticket con el [soporte]({{site.baseurl}}/braze_support) de Braze.

Para encontrar los usuarios ficticios de tu panel, sigue estos pasos:

1. Crea un [Segment]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment).
2. Selecciona el filtro `Session Count` y configúralo en `more than 5,000,000`.
3. Exporta el Segment a través de CSV.

El filtro **Session Count** solo encuentra usuarios ficticios basados en sesiones. No existe un filtro de segmentación para el número de nombres de eventos personalizados distintos o nombres de productos en un perfil, así que contacta con tu director de cuentas de Braze para identificar los perfiles bloqueados por esas razones.

Si es necesario, puedes eliminar los usuarios a través del [endpoint `/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete).

## Personalización de tu política de archivado de usuarios {#customizing-your-user-archival-policy}

Braze proporciona características de orquestación de datos que te permiten personalizar tu política de archivado de usuarios. Crea una política de archivado de usuarios que te ofrezca lo mejor de ambos mundos con el componente [Actualización de usuario]({{site.baseurl}}/user_update) de Canvas.

Esto te permite:

- Cumplir con el RGPD y las mejores prácticas de privacidad eliminando perfiles de usuario que ya no son valiosos.
- Conservar cualquier perfil de usuario para el que tengas una necesidad empresarial legítima.

### Pasos {#steps}

1. Segmenta a los usuarios que cumplan los criterios de archivado de tu marca y que desees conservar. Por ejemplo, podrías conservar a los usuarios que:
    - Recibieron un mensaje por última vez hace más de 23 semanas o nunca han recibido un mensaje<br>Y<br>
    - Usaron tu aplicación por última vez hace más de 23 semanas o tuvieron cero sesiones en tu aplicación<br><br>
      ![Segmentar usuarios que recibieron cualquier mensaje por última vez hace más de 23 semanas, nunca han recibido un mensaje de una Campaign o un paso en Canvas, usaron estas aplicaciones por última vez hace más de 23 semanas y han usado estas aplicaciones exactamente cero veces.][2]<br><br>
2. Configura la reelegibilidad para que sea un poco menos de 6 meses.<br><br>
      ![Controles de entrada con la reelegibilidad activada y la ventana de reelegibilidad configurada en 23 semanas.][3]<br><br>
3. Configura el paso de Actualización de usuario para añadir un evento a cada perfil.<br><br>
      ![Paso de Actualización de usuario que añade el evento "do_not_archive" al perfil del usuario.][4]
{% details Ejemplo de objeto de Actualización de usuario %}

{% raw %}
```json
{
    "events": [
        {
            "name": "do_not_archive",
            "time": "{{ 'now' | time_zone: 'UTC' | date: '%Y-%m-%dT%H:%M:%SZ' }}"
        }
    ]
}
```
{% endraw %}

{% enddetails %}

[1]: {{site.baseurl}}/dp-technical-assistance/#the-right-to-erasure
[2]: {% image_buster /assets/img_archive/user_archival_policy1.png %}
[3]: {% image_buster /assets/img_archive/user_archival_policy2.png %}
[4]: {% image_buster /assets/img_archive/user_archival_policy3.png %}