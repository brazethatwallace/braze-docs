---
nav_title: Sincronización de segmentos de Shopify
article_title: Sincronización de segmentos de Shopify
alias: /shopify_segments_sync/
page_order: 8
description: "Este artículo de referencia explica cómo sincronizar segmentos de Shopify en Braze como cohortes para una gestión y segmentación de audiencias unificada."
---

# Sincronización de segmentos de Shopify {#shopify-segments-sync}

> La sincronización de segmentos de Shopify extiende tu tienda Shopify a Braze, dando a tu equipo de marketing acceso directo a datos de usuario más completos que residen en Shopify, incluidas señales que no se capturan con la integración estándar de Braze con Shopify. Al sincronizar segmentos de Shopify como cohortes, alineas las definiciones de audiencia en ambas plataformas y ofreces experiencias de usuario consistentes y coordinadas, ya sea que un usuario sea segmentado en Shopify o interactúe a través de una campaña de Braze.

{% alert important %}
La sincronización de segmentos de Shopify se encuentra actualmente en fase beta. Para solicitar acceso, ponte en contacto con tu administrador del éxito del cliente.
{% endalert %}

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| --- | --- |
| Integración de Braze con Shopify | La aplicación de Braze para Shopify debe estar instalada en tu tienda Shopify y conectada a un espacio de trabajo de Braze. Para obtener instrucciones de configuración, consulta [Configuración de la integración estándar de Shopify]({{site.baseurl}}/partners/ecommerce/shopify/shopify_standard_integration/) o [Configuración de la integración personalizada de Shopify]({{site.baseurl}}/partners/ecommerce/shopify/shopify_custom_integration/). |
| Permiso de usuario de Shopify | El usuario de Shopify que inicie la sincronización de segmentos debe tener el permiso **Exportar** para exportar datos de clientes. Para más información sobre los permisos de Shopify, consulta la [documentación de permisos de tienda de Shopify](https://help.shopify.com/en/manual/your-account/users/roles/permissions/store-permissions#customers-permissions). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Cómo funciona {#how-it-works}

La sincronización de segmentos de Shopify funciona en dos fases.

1. Cuando sincronizas un segmento por primera vez, Braze rellena todos los miembros actuales y crea una cohorte correspondiente en Braze. El relleno se ejecuta de forma asíncrona y puede tardar unos momentos en completarse.
2. Durante la sincronización inicial, Braze rellena los miembros actuales y se suscribe a los webhooks de Shopify para que la membresía se mantenga sincronizada casi en tiempo real.

| Tema del webhook | Efecto en Braze |
| --- | --- |
| `customer.joined_segment` | El usuario se añade a la cohorte correspondiente de Braze. |
| `customer.left_segment` | El usuario se elimina de la cohorte correspondiente de Braze. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Tema del webhook" }

Si una sincronización falla, el modal de extensión de acción muestra un banner de error con una acción recomendada. Selecciona **Sync with Braze** para reintentar.

## Integración de importación de datos {#data-import-integration}

### Paso 1: Selecciona un segmento de Shopify para sincronizar {#step-1-select-a-shopify-segment-to-sync}

En Shopify, ve a **Customers** > **Segments** y selecciona el segmento que deseas sincronizar con Braze. Puedes sincronizar cualquier segmento creado con la segmentación nativa de Shopify, incluidos segmentos basados en historial de pedidos, compras de productos, etiquetas de clientes, gasto de por vida y metacampos.

![Panel de segmentos con una lista de segmentos de Shopify.]({% image_buster /assets/img/shopify/shopify_segments.png %})

### Paso 2: Inicia la sincronización {#step-2-initiate-the-sync}

1. En la página de detalle del segmento de Shopify, abre el desplegable **Use segment** y selecciona **Braze Segment Sync**.

![Página de detalle del segmento con un desplegable "Use segment" que tiene la opción "Braze Segment Sync".]({% image_buster /assets/img/shopify/braze_segment_sync.png %})

{: start="2"}
2. En el modal de extensión de acción de Braze que se abre, se muestra el nombre del segmento y el tamaño de la audiencia. Selecciona **Sync with Braze** para iniciar la importación.

![Modal con un botón para sincronizar con Braze.]({% image_buster /assets/img/shopify/sync_with_braze.png %}){:style="max-width:70%;"}

{: start="3"}
3. Selecciona **Done**.

![Modal que confirma que la sincronización está activa.]({% image_buster /assets/img/shopify/braze_sync_active.png %}){:style="max-width:70%;"}

### Paso 3: Crea un segmento de Braze con el filtro de membresía de cohorte {#step-3-create-a-braze-segment-with-the-cohort-membership-filter}

En Braze, ve a **Audience** > **Segments** y crea un nuevo segmento. En **Add Filter**, selecciona el filtro **Cohort Membership** y elige tu segmento de Shopify sincronizado en el desplegable. Después de guardar, puedes hacer referencia a este segmento de Braze al segmentar usuarios en una campaña o Canvas.

![Constructor de segmentos con el filtro "Shopify Cohorts".]({% image_buster /assets/img/shopify/segment_builder_cohort_import.png %})

## Coincidencia de usuarios {#user-matching}

Los usuarios sincronizados desde segmentos de Shopify se emparejan con perfiles de usuario de Braze utilizando el alias `shopify_customer_id` que se establece como parte de la integración de Braze con Shopify. Los usuarios sin un perfil de usuario de Braze coincidente se omiten durante la sincronización.

Para obtener más detalles sobre cómo la integración de Shopify identifica y asigna alias a los usuarios, consulta [Características de datos de Shopify]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features/).

## Limitaciones {#limitations}

- **Sincronización unidireccional.** La membresía de segmentos fluye solo de Shopify a Braze. Los cambios en la membresía de cohortes realizados directamente en Braze no se envían de vuelta a Shopify.
- **Sin creación de perfiles.** Solo los clientes de Shopify que ya tienen un perfil de usuario en Braze se añaden a la cohorte.
- **Las sincronizaciones no se pueden deshacer.** Una vez que un segmento de Shopify se sincroniza, no se puede deshacer.