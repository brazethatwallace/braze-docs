---
nav_title: Sincronización de segmentos de Shopify
article_title: Sincronización de segmentos de Shopify
alias: /shopify_segments_sync/
page_order: 8
description: "Este artículo de referencia explica cómo sincronizar segmentos de Shopify en Braze como cohortes para una gestión y segmentación de audiencias unificada."
---

# Sincronización de segmentos de Shopify {#shopify-segments-sync}

> La sincronización de segmentos de Shopify extiende tu tienda Shopify a Braze, dando a tu equipo de marketing acceso directo a datos de usuario más completos que residen en Shopify, incluidas señales que no se capturan con la integración estándar de Braze con Shopify. Al sincronizar segmentos de Shopify como cohortes, alineas las definiciones de audiencia en ambas plataformas y ofreces experiencias de usuario consistentes y coordinadas, ya sea que los segmentes en Shopify o los alcances a través de una Campaign de Braze.

{% alert important %}
La sincronización de segmentos de Shopify se encuentra actualmente en fase beta. Para solicitar acceso, ponte en contacto con tu CSM.
{% endalert %}

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| --- | --- |
| Integración de Braze con Shopify | La aplicación de Braze para Shopify debe estar instalada en tu tienda Shopify y conectada a un espacio de trabajo de Braze. Para instrucciones de configuración, consulta [Configuración de la integración estándar de Shopify]({{site.baseurl}}/partners/ecommerce/shopify/shopify_standard_integration) o [Configuración de la integración personalizada de Shopify]({{site.baseurl}}/partners/ecommerce/shopify/shopify_custom_integration). |
| Permiso de usuario de Shopify | El usuario de Shopify que inicie la sincronización de Segment debe tener el permiso **Exportar** para exportar datos de usuario. Para más información sobre los permisos de Shopify, consulta la [documentación de permisos de tienda de Shopify](https://help.shopify.com/en/manual/your-account/users/roles/permissions/store-permissions#customers-permissions). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Cómo funciona {#how-it-works}

La sincronización de segmentos de Shopify funciona en dos fases.

1. **Reposición inicial:** Cuando sincronizas un segmento por primera vez, Braze repone todos los miembros actuales y crea una cohorte correspondiente en Braze. La reposición se ejecuta de forma asíncrona y puede tardar unos momentos en completarse.
2. **Sincronización continua:** Después de la reposición inicial, Braze también se suscribe a los webhooks de Shopify para que la membresía se mantenga sincronizada prácticamente en tiempo real.

| Tema del webhook | Efecto en Braze |
| --- | --- |
| `customer.joined_segment` | El usuario se añade a la cohorte correspondiente de Braze. |
| `customer.left_segment` | El usuario se elimina de la cohorte correspondiente de Braze. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Tema del webhook" }

Si una sincronización falla, el modal de la extensión de acción muestra un banner de error que explica qué ocurrió y cómo proceder. Algunos errores ofrecen la acción **Retry sync**. Otros requieren un cambio de administrador o de configuración.

## Integración de importación de datos {#data-import-integration}

### Paso 1: Seleccionar un segmento de Shopify para sincronizar {#step-1-select-a-shopify-segment-to-sync}

En Shopify, ve a **Customers** > **Segments** y selecciona el segmento que quieras sincronizar con Braze. Puedes sincronizar cualquier segmento creado con la segmentación nativa de Shopify, incluidos los segmentos basados en el historial de pedidos, compras de productos, etiquetas de clientes, gasto total y metacampos.

![Panel de segmentos con una lista de segmentos de Shopify.]({% image_buster /assets/img/shopify/shopify_segments.png %})

### Paso 2: Iniciar la sincronización {#step-2-initiate-the-sync}

1. En la página de detalle del segmento de Shopify, abre el desplegable **Use segment** y selecciona **Braze Segment Sync**.

![Página de detalle del segmento con un desplegable "Use segment" que tiene la opción "Braze Segment Sync".]({% image_buster /assets/img/shopify/braze_segment_sync.png %})

{: start="2"}
2. Se abre el modal de la extensión de acción de Braze, que muestra el nombre del segmento y el tamaño de la audiencia. Selecciona **Sync with Braze** para comenzar la importación.

![Modal con un botón para sincronizar con Braze.]({% image_buster /assets/img/shopify/sync_with_braze.png %}){:style="max-width:70%;"}

{: start="3"}
3. El modal pasa a un estado de sincronización y muestra un banner de progreso mientras Braze importa los miembros.

![Modal que muestra la sincronización en curso.]({% image_buster /assets/img/shopify/sync_in_progress.png %}){:style="max-width:70%;"}

{: start="4"}
4. Selecciona **Close**. La sincronización continúa en segundo plano. Cerrar el modal no la detiene.

Para comprobar si la sincronización se ha completado, cierra y vuelve a abrir el modal. Cuando la sincronización finalice, el modal se abrirá con un banner de éxito.

![Modal que confirma que la sincronización está activa.]({% image_buster /assets/img/shopify/braze_sync_active.png %}){:style="max-width:70%;"}

### Paso 3: Crear un Segment de Braze con el filtro de pertenencia a cohorte {#step-3-create-a-braze-segment-with-the-cohort-membership-filter}

En Braze, ve a **Audience** > **Segments** y crea un nuevo segmento. En **Add Filter**, selecciona el filtro **Cohort Membership** y elige tu segmento de Shopify sincronizado en el desplegable. Después de guardar, puedes hacer referencia a este Segment de Braze al segmentar usuarios en una Campaign o Canvas.

![Constructor de segmentos con el filtro "Shopify Cohorts".]({% image_buster /assets/img/shopify/segment_builder_cohort_import.png %})

## Resincronización de un segmento {#re-syncing-a-segment}

Después de sincronizar un segmento, puedes actualizar la pertenencia a la cohorte en cualquier momento desde la misma extensión de acción.

1. En Shopify, abre el segmento sincronizado y selecciona **Use segment** > **Braze Segment Sync**.
2. En el modal, selecciona **Sync now**.
3. En el cuadro de diálogo de confirmación, selecciona **Sync now** para iniciar la resincronización.

La resincronización es aditiva: los usuarios que coinciden con el segmento actual de Shopify se agregan a la cohorte, pero los usuarios que ya no coinciden permanecen en la cohorte.

## Gestionar segmentos sincronizados en Braze {#managing-synced-segments-in-braze}

Puedes gestionar todos los segmentos sincronizados desde el panel de Braze. Ve a **Integraciones de partners** > **Partners tecnológicos**, selecciona tu integración de Shopify y abre la pestaña **Gestionar usuarios**.

### Estado de sincronización {#sync-status}

Cada segmento sincronizado tiene un estado de sincronización.

| Estado | Descripción |
| --- | --- |
| **Sincronizando** | Braze está importando los miembros del segmento. |
| **En cola** | El segmento está esperando un espacio de sincronización disponible. |
| **Activo** | El segmento está sincronizado y la membresía se actualiza casi en tiempo real. |
| **Pausado** | Las actualizaciones de membresía de este segmento están pausadas. |
| **Error** | El último intento de sincronización falló. Selecciona **Reintentar sincronización** para intentarlo de nuevo. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Estados de sincronización" }

### Sincronizar segmentos de forma masiva {#syncing-segments-in-bulk}

Para sincronizar segmentos adicionales, edita la integración, ve al paso **Gestionar usuarios** y selecciona **Editar segmentos** en la sección **Sincronizar segmentos**. En el modal de selección:

- Selecciona cualquier cantidad de segmentos. Se sincronizan 25 segmentos a la vez; el resto se pone en cola automáticamente.
- Los segmentos que ya se están sincronizando están bloqueados. Para eliminar un segmento, elimínalo en Shopify.

Guarda los cambios para iniciar las sincronizaciones.

### Pausar un solo segmento {#pausing-a-single-segment}

Para pausar la sincronización de un segmento, selecciona **Pausar sincronización** en su fila de la tabla de segmentos y confirma. Cuando la sincronización de un segmento está pausada:

- La cohorte y sus miembros permanecen en Braze y se pueden seguir utilizando para segmentación. Las Campaigns y los Canvas que usan la cohorte siguen enviando a los miembros actuales de la cohorte.
- Las actualizaciones de membresía se detienen.
- Renombrar el segmento en Shopify sigue actualizando el nombre visible de la cohorte.
- Eliminar el segmento en Shopify sigue finalizando el seguimiento.
- Las solicitudes de **Sincronizar ahora** desde la extensión de acción de Shopify se rechazan.

Para reanudar, selecciona **Reanudar sincronización** en la fila. Braze reanuda las actualizaciones de membresía y ejecuta una sincronización de recuperación. Los usuarios que abandonaron el segmento de Shopify mientras la sincronización estaba pausada permanecen en la cohorte de Braze.

### Pausar la sincronización de todos los segmentos {#pausing-all-segment-syncing}

Para pausar la sincronización de todos los segmentos a la vez, edita la integración, selecciona **Pausar sincronización** en la sección **Sincronizar segmentos** del paso **Gestionar usuarios** y guarda la configuración. Mientras la sincronización de todos los segmentos está pausada:

- La tabla de segmentos muestra solo los nombres de los segmentos, con un estado **Pausado** junto al encabezado.
- Las acciones a nivel de fila no están disponibles hasta que reanudes.
- Braze no actualiza los nombres de cohorte cuando se renombran en Shopify. Los nombres de cohorte se actualizan cuando reanudes.
- Las solicitudes de **Sincronizar ahora** desde la extensión de acción se rechazan. La extensión sigue mostrando el último estado conocido de cada segmento, y seleccionar **Sincronizar ahora** no inicia una sincronización.

Para reanudar, selecciona **Reanudar sincronización** en la misma sección y guarda. Braze vuelve a sincronizar automáticamente todos los segmentos seleccionados previamente con una sincronización de recuperación. No necesitas volver a seleccionarlos. Los segmentos que pausaste individualmente permanecen pausados hasta que los reanudes desde su fila en la tabla de segmentos.

## Actualizaciones de Segments en Shopify {#segment-updates-in-shopify}

### Renombrar un Segment {#renaming-a-segment}

Cuando renombras un Segment de Shopify, Braze actualiza automáticamente el nombre de visualización de la cohorte correspondiente. No es necesario volver a sincronizar. Braze también actualiza el nombre de la cohorte mientras la sincronización de un Segment está pausada individualmente. Mientras toda la sincronización de Segments está pausada, Braze actualiza los nombres de las cohortes cuando la reanudas.

### Cambiar los criterios de un Segment {#changing-segment-criteria}

Braze no actualiza automáticamente la pertenencia a la cohorte cuando cambias los criterios de un Segment de Shopify. Para incluir a los usuarios que ahora coinciden con los criterios, vuelve a sincronizar el Segment desde la extensión de acción. Los usuarios que ya no coinciden permanecen en la cohorte porque la resincronización no elimina miembros. Para más detalles, consulta [Resincronizar un Segment](#re-syncing-a-segment).

## Coincidencia de usuarios {#user-matching}

Los usuarios sincronizados desde Segments de Shopify se emparejan con perfiles de usuario de Braze utilizando el alias `shopify_customer_id` que se configura como parte de la integración de Braze con Shopify. Los usuarios que no tengan un perfil de usuario de Braze coincidente se omiten durante la sincronización.

Para más detalles sobre cómo la integración de Shopify identifica y asigna alias a los usuarios, consulta [Características de datos de Shopify]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features).

Braze empareja a los usuarios sincronizados con los perfiles de usuario de Braze existentes, independientemente de cómo se hayan creado esos perfiles, incluso a través del llenado histórico de Shopify, tu propia plataforma de datos (como Snowflake u otro almacén de datos) o importaciones directas por API. Si tu cohorte es más pequeña que tu Segment de Shopify, significa que algunos miembros del segmento aún no tienen un perfil de Braze coincidente. Para aumentar la cobertura de coincidencias, completa los perfiles de usuario de Braze a través de tu método preferido antes de sincronizar.

## Limitaciones {#limitations}

- **Sincronización unidireccional.** La pertenencia a Segments fluye solo de Shopify a Braze. Los cambios en la pertenencia a cohortes realizados directamente en Braze no se envían de vuelta a Shopify.
- **Sin creación de perfiles.** Solo los clientes de Shopify que ya tienen un perfil de usuario en Braze se añaden a la cohorte.
- **No hay forma de detener la sincronización desde Braze.** Para detener la sincronización de un Segment, elimínalo en Shopify. La cohorte y sus miembros permanecen en Braze y dejan de actualizarse.
- **La resincronización solo añade miembros.** Resincronizar un Segment añade usuarios que coinciden recientemente a la cohorte, pero no elimina usuarios que ya no están en el Segment de Shopify.