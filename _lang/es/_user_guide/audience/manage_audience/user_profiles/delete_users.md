---
nav_title: Eliminar usuarios
article_title: Eliminar usuarios
page_order: 6
toc_headers: h2
description: "Aprende a eliminar un usuario individual o un segmento de usuarios directamente a través del panel de Braze."
alias: /delete_users/
---

# Eliminar usuarios {#delete-users}

> Aprende a eliminar un usuario individual o un segmento de usuarios directamente a través del panel de Braze.

## Requisitos previos {#prerequisites}

Para eliminar usuarios, debes ser administrador o tener el permiso **Eliminar usuarios**. Para ver los registros de eliminación de usuarios, debes ser administrador o tener el permiso **Ver registros de eliminación de usuarios**. Los siguientes permisos controlan la eliminación de usuarios y los registros de eliminación:

| Permiso | Descripción |
|------------|-------------|
| Eliminar usuarios | Eliminar usuarios de forma permanente de manera individual o masiva. |
| Ver registros de eliminación de usuarios | Ver los registros de eliminación de usuarios. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Acerca de la eliminación de usuarios {#about-user-deletion}

La eliminación de usuarios te permite gestionar tu base de datos eliminando perfiles que ya no son necesarios, que se crearon por error o que deben eliminarse por cumplimiento normativo (como el RGPD o la CCPA).

| Consideración | Detalles |
|---------------|---------|
| Tamaño máximo | Puedes eliminar hasta 10 millones de perfiles de usuario cuando eliminas un Segment. |
| Período de espera | Todas las eliminaciones de Segments requieren un período de espera de 7 días más el tiempo que tarda en procesarse la eliminación. |
| Límites de trabajos | Solo se puede eliminar un Segment a la vez, lo que incluye el período de espera de 7 días. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Acerca de la eliminación de usuarios" }

## Eliminar usuarios {#deleting-users}

Puedes eliminar un [usuario individual](#delete-individual) o un [segmento de usuarios](#delete-segment) a través del panel de Braze:

### Eliminar un usuario individual {#delete-individual}

Para eliminar un usuario individual de Braze, ve a **Audiencia** > **Buscar usuarios** y, a continuación, busca y selecciona un usuario. Si estás eliminando un perfil de usuario duplicado, verifica que hayas seleccionado el correcto.

![La página "Buscar usuarios" en Braze.]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/search_user.png %}){: style="max-width:75%;"}

{% alert warning %}
Las eliminaciones de un solo usuario son permanentes: los perfiles no se pueden recuperar una vez eliminados.
{% endalert %}

En la página de su perfil, selecciona <i class="fa-solid fa-ellipsis-vertical" aria-label="Mostrar opciones"></i> **Mostrar opciones** > **Eliminar usuario**. Ten en cuenta que el usuario puede tardar unos minutos en eliminarse completamente en Braze.


### Eliminar un segmento {#delete-segment}

Si aún no lo has hecho, [crea un segmento]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment) que contenga los perfiles de usuario que deseas eliminar. Asegúrate de incluir todos los perfiles de usuario si estás eliminando usuarios duplicados.

En Braze, ve a **Audiencia** > **Gestionar audiencia** y, a continuación, selecciona la pestaña **Eliminar usuarios**.

![La pestaña "Eliminar usuarios" en la sección "Gestionar audiencia" del panel de Braze.]({% image_buster /assets/img/audience_management/deleting_users/delete_users_tab.png %}){: style="max-width:85%;"}

Selecciona **Eliminar usuarios**, elige el segmento que deseas eliminar y, a continuación, selecciona **Siguiente**.

![Una ventana emergente con un segmento seleccionado para su eliminación.]({% image_buster /assets/img/audience_management/deleting_users/choose_segment_to_delete.png %}){: style="max-width:75%;"}

Escribe **DELETE** para confirmar tu solicitud y, a continuación, selecciona **Eliminar usuarios**.

![La página de confirmación con "DELETE" escrito en el cuadro de confirmación.]({% image_buster /assets/img/audience_management/deleting_users/confirm_segment_delete.png %}){: style="max-width:75%;"}

Los usuarios de este segmento no se eliminarán de inmediato. En su lugar, se marcarán como pendientes de eliminación durante los próximos 7 días. Transcurrido ese tiempo, se eliminarán y te enviaremos un correo electrónico para informarte.

Durante el período de espera de 7 días, los usuarios pendientes de eliminación aún pueden recibir Campaigns y Canvas a menos que los excluyas explícitamente. Para evitar que los usuarios pendientes reciban mensajes, añade un filtro de segmento para excluir a los usuarios con el estado **Pending Deletion** de tus Campaigns y Canvas.

{% alert tip %}
Para garantizar que estos usuarios exactos se eliminen independientemente de los cambios en el segmento, se crea automáticamente un filtro de segmento llamado **Pending Deletion**. Puedes [usar este filtro]({{site.baseurl}}/user_guide/audience/segments/managing_segments#filters) para comprobar el estado de las eliminaciones pendientes.
{% endalert %}

## Confirmación de eliminaciones de segmentos {#confirming-segment-deletions}

Braze envía un correo electrónico de confirmación con el número de perfiles pendientes de eliminación.

Para continuar con la eliminación, inicia sesión en Braze y confirma la solicitud de eliminación.

Si no confirmas dentro del plazo indicado en el correo electrónico, la solicitud de eliminación caduca y no se procesa.

## Cancelar eliminaciones de segmentos {#cancel}

Tienes 7 días para cancelar las eliminaciones de segmentos pendientes. Para cancelar, ve a **Audience** > **Manage Audience** y luego selecciona la pestaña **Delete Users**.

![La pestaña "Delete Users" en la sección "Manage Audience" del panel de Braze.]({% image_buster /assets/img/audience_management/deleting_users/delete_users_tab.png %}){: style="max-width:85%;"}

Junto a una eliminación de segmento pendiente, selecciona <i class="fa-solid fa-eye"></i> **View details** para abrir los detalles del registro de eliminación.

![Una eliminación de segmento pendiente en la pestaña "Delete Users".]({% image_buster /assets/img/audience_management/deleting_users/pending_deletion.png %})

En los detalles del registro de eliminación, selecciona **Cancel deletion**.

![La ventana "Deletion Record Details" en la pestaña "Delete Users".]({% image_buster /assets/img/audience_management/deleting_users/deletion_record_details.png %}){: style="max-width:55%;"}

{% alert tip %}
Cuando la eliminación masiva de usuarios está en curso, puedes cancelarla en cualquier momento. Sin embargo, los usuarios que ya se hayan eliminado antes de la cancelación no se pueden restaurar.
{% endalert %}

## Verificar el estado de eliminación {#status}

Puedes verificar el estado de una eliminación usando [filtros de segmento](#segment-filters), la página de [gestionar audiencia](#manage-audience) o los [informes de eventos de seguridad](#security-event-report).

### Filtros de segmento {#segment-filters}

Cuando solicitas la eliminación de un segmento de usuarios, se crea automáticamente un [filtro de segmento]({{site.baseurl}}/user_guide/audience/segments/managing_segments#filters) llamado **Pending Deletion**. Puedes usarlo para:

- Ver el conjunto exacto de usuarios vinculados a una fecha de ejecución de eliminación específica.
- Excluir a esos usuarios de Campaigns para que no reciban mensajes antes de su eliminación.
- Exportar la lista si la necesitas para cumplimiento normativo o mantenimiento de registros.

### Gestionar audiencia {#manage-audience}

{% alert note %}
Para obtener la lista de usuarios exactos que se eliminarán, usa el [filtro de segmento **Pending Deletion**](#segment-filters) en su lugar.
{% endalert %}

Ve a **Audience** > **Manage Audience** y luego selecciona la pestaña **Delete Users**.

![La pestaña "Delete Users" en la sección "Manage Audience" del panel de Braze.]({% image_buster /assets/img/audience_management/deleting_users/delete_users_tab.png %}){: style="max-width:85%;"}

En esta página, puedes encontrar la siguiente información general para todas las eliminaciones actuales y pendientes:

| Campo | Descripción |
|-------|-------------|
| Fecha de solicitud | La fecha en que se realizó originalmente la solicitud. Úsala con el filtro **Pending Deletion** para obtener la lista de perfiles pendientes de eliminación. |
| Solicitante | El usuario que inició la solicitud de eliminación. |
| Nombre del segmento | El nombre del segmento utilizado para seleccionar los usuarios pendientes de eliminación. |
| Estado | Muestra si la solicitud de eliminación está pendiente, en curso o completada. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Gestionar audiencia" }

Para obtener más detalles sobre una solicitud específica, selecciona <i class="fa-solid fa-eye"></i> **View details** para mostrar los detalles del registro de eliminación. Aquí también puedes [cancelar eliminaciones de segmentos pendientes](#cancel).

![Una eliminación de segmento pendiente en la pestaña "Delete Users".]({% image_buster /assets/img/audience_management/deleting_users/pending_deletion.png %})

### Informe de eventos de seguridad {#security-event-report}

También puedes verificar el estado de eliminaciones anteriores descargando un informe de eventos de seguridad. Para más información, consulta [Configuración de seguridad]({{site.baseurl}}/user_guide/administer/global/admin_settings/security_settings#security-event-report).

## Preguntas frecuentes {#faq}

### ¿Puedo eliminar segmentos con más de 10 millones de usuarios? {#can-i-delete-segments-with-more-than-10-million-users}

No. No puedes eliminar segmentos con más de 10 millones de usuarios. Si necesitas ayuda para eliminar un segmento de este tamaño, ponte en contacto con [soporte de Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support).

### Solo puedo eliminar hasta 10 millones de usuarios a la vez. ¿Es un error? {#i-can-only-delete-up-to-10-million-users-at-a-time-is-this-a-bug}

No, esto no es un error. El número máximo de perfiles de usuario que se pueden eliminar en una sola ejecución de eliminación de segmento es de 10 millones.

### ¿La fusión automatizada de usuarios afecta la eliminación de usuarios? {#does-automated-user-merging-affect-user-deletion}

Si una fusión programada incluye perfiles de usuario pendientes de eliminación, Braze omite esos perfiles y no los fusiona. Para fusionar estos perfiles, primero debes quitarlos de la eliminación pendiente.

### ¿Qué sucede con los datos enviados a usuarios pendientes de eliminación? {#what-happens-to-data-sent-to-users-pending-deletion}

Los datos enviados desde sistemas externos o SDK se siguen aceptando, pero los usuarios se eliminarán según lo programado independientemente de la actividad.

### ¿Se desencadenan Canvas y Campaigns para usuarios pendientes de eliminación? {#do-canvases-and-campaigns-trigger-for-users-pending-deletion}

Sí. Sin embargo, puedes añadir un filtro de inclusión de segmento para excluir a todos los usuarios con el [filtro de segmento](#segment-filters) **Pending Deletion**.

### ¿Puedo recuperar perfiles de usuario eliminados? {#can-i-recover-deleted-user-profiles}

Las eliminaciones de usuarios individuales son permanentes.

Puedes [cancelar eliminaciones de segmentos](#cancel) dentro de los primeros 7 días. Sin embargo, los usuarios que ya se hayan eliminado antes de la cancelación no se pueden restaurar.

### ¿Puedo eliminar usuarios con la API en lugar del panel? {#can-i-delete-users-with-the-api-instead-of-the-dashboard}

Sí. Para lotes más pequeños, puedes usar el [endpoint `/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete), que acepta hasta 50 identificadores por solicitud y está sujeto al [límite de velocidad]({{site.baseurl}}/api/endpoints/user_data/post_user_delete#rate-limit) de ese endpoint. La eliminación basada en segmentos desde el panel es más adecuada para audiencias muy grandes, pero incluye el [período de espera de 7 días](#about-user-deletion).