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

Braze define a un "usuario activo" durante un periodo de tiempo determinado como cualquier usuario que haya registrado una sesión en una aplicación móvil o sitio web, se haya actualizado, haya recibido un mensaje o haya interactuado con un mensaje.

Si estableces ID de usuario para identificar a los usuarios cuando un nuevo usuario inicia sesión, se contará como un usuario activo independiente. Los usuarios que se actualicen a través de la API también se contabilizarán como usuarios activos en el periodo de tiempo en que se actualicen.

{% alert important %}
Tanto los usuarios inactivos como los usuarios latentes serán archivados a menos que el usuario sea excluido del archivado por las razones que se indican a continuación.
{% endalert %}

### Usuarios inactivos {#inactive-users}

Los "usuarios inactivos" son usuarios inaccesibles que probablemente han abandonado. Los usuarios inactivos son aquellos que cumplen todos estos criterios:

- No pueden recibir correo electrónico. Por ejemplo, no tienen dirección de correo electrónico o se han dado de baja de todas las listas de correo electrónico.
- No pueden recibir SMS. Por ejemplo, no tienen un número de teléfono válido o se han dado de baja de todos los grupos de suscripción a SMS.
- No pueden recibir push. Por ejemplo, han desinstalado la aplicación o han desactivado los permisos push.
- No pueden recibir un mensaje de WhatsApp. Por ejemplo, no tienen un número de teléfono válido o se han dado de baja de todos los grupos de suscripción de WhatsApp.
- No pueden recibir un mensaje de LINE. Por ejemplo, no tienen un ID de LINE o se han dado de baja de todos los grupos de suscripción de LINE.
- No han utilizado ninguna aplicación móvil ni visitado un sitio web en un espacio de trabajo en más de seis meses.
- No han recibido ningún mensaje de un espacio de trabajo en más de seis meses.
- No se han actualizado en más de seis meses.

En este caso, estos usuarios no pueden recibir mensajes y no están interactuando con tu marca. Estos usuarios han abandonado efectivamente.

### Usuarios latentes {#dormant-users}

Los "usuarios latentes" son usuarios que no han tenido actividad en los últimos doce meses y:

- No han utilizado ninguna aplicación móvil ni visitado un sitio web en un espacio de trabajo en más de 12 meses.
- No han recibido ningún mensaje de un espacio de trabajo en más de 12 meses.
- No se han actualizado en más de 12 meses.

## Usuarios del Grupo de control global {#global-control-group-users}

Los usuarios del Grupo de control global nunca serán archivados, aunque cumplan la definición de usuarios inactivos o latentes.

### Grupo de muestra de tratamiento {#treatment-sample-group}

Los usuarios del grupo de muestra de tratamiento en un Informe del Grupo de control global están excluidos del archivado.

## Usuarios de prueba {#test-users}

Los usuarios de prueba nunca se archivarán, aunque cumplan la definición de usuarios inactivos o latentes.

## Bloqueo de correo no deseado {#spam-blocking}

Braze bloquea a los usuarios individuales con más de 5 millones de sesiones ("usuarios ficticios") y ya no ingiere sus eventos de SDK, porque suelen ser el resultado de una integración incorrecta. Si descubres que esto le ha ocurrido a un usuario legítimo, presenta un ticket en el [soporte]({{site.baseurl}}/braze_support/) de Braze.

Para encontrar los usuarios ficticios de tu dashboard, realiza los siguientes pasos:

1. Crea un [segmento]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment/).
2. Selecciona el filtro `Session Count` y configúralo en `more than 5,000,000`.
3. Exporta el segmento mediante CSV.

Si es necesario, puedes eliminar a los usuarios a través del [punto de conexión `/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/).

## Personaliza tu política de archivado de usuarios {#customizing-your-user-archival-policy}

Braze proporciona características de orquestación de datos que te permiten personalizar tu política de archivado de usuarios. Crea una política de archivado de usuarios que te ofrezca lo mejor de ambos mundos con el componente [Actualización de usuario]({{site.baseurl}}/user_update/) de Canvas.

Esto te permite:

- Cumplir con el RGPD y las mejores prácticas de privacidad eliminando los perfiles de usuario que ya no sean valiosos.
- Conservar cualquier perfil de usuario para el que tengas una necesidad empresarial legítima.

### Pasos {#steps}

1. Dirígete a usuarios que cumplan los criterios de archivado de tu marca y que te gustaría conservar. Por ejemplo, podrías retener a los usuarios que:
    - Recibieron un mensaje por última vez hace más de 23 semanas o nunca han recibido un mensaje<br>Y<br>
    - Utilizaron tu aplicación por última vez hace más de 23 semanas o tuvieron cero sesiones en tu aplicación<br><br>
      ![Usuarios objetivo que recibieron cualquier mensaje por última vez hace más de 23 semanas, que nunca han recibido un mensaje de una campaña o paso en Canvas, que utilizaron estas aplicaciones por última vez hace más de 23 semanas y que han utilizado estas aplicaciones exactamente cero veces.][2]<br><br>
2. Establece que la reelegibilidad dure algo menos de 6 meses.<br><br>
      ![Controles de entrada con la reelegibilidad activada y la ventana de reelegibilidad fijada en 23 semanas.][3]<br><br>
3. Configura el paso Actualización de usuario para añadir un evento a cada perfil.<br><br>
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