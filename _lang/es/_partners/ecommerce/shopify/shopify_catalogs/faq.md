---
nav_title: Preguntas frecuentes
article_title: Preguntas frecuentes sobre la sincronización de productos de Shopify
page_order: 0
page_type: FAQ
description: "Esta página ofrece respuestas a preguntas frecuentes sobre la sincronización de productos de Shopify con catálogos de Braze."
---

# Preguntas frecuentes {#frequently-asked-questions}

> Esta página ofrece respuestas a algunas preguntas frecuentes sobre la [sincronización de productos de Shopify]({{site.baseurl}}/shopify_catalogs/).

## Comportamiento del catálogo y la sincronización {#catalog-and-sync-behavior}

### ¿Puedo editar mi catálogo de Shopify directamente en Braze? {#can-i-edit-my-shopify-catalog-directly-in-braze}

No. El catálogo de Shopify es de solo lectura en Braze. Cualquier edición manual puede ser sobrescrita por la siguiente sincronización. Realiza todas las actualizaciones de productos directamente en Shopify.

### ¿Cómo elimino mi catálogo de Shopify? {#how-do-i-delete-my-shopify-catalog}

Para eliminar tu catálogo de Shopify, desactiva la sincronización desde la página del socio de Shopify. No elimines el catálogo directamente desde la página **Catalogs**. La desactivación elimina todo tu catálogo, incluidas todas las etiquetas, colecciones y datos de metafields sincronizados. Antes de desactivar, actualiza o pausa cualquier Campaign o Canvas que haga referencia a este catálogo, ya que podrían enviar mensajes con detalles de producto faltantes.

### ¿Qué ocurre si elimino un producto o campo de producto previamente sincronizado en Shopify? {#what-happens-if-i-delete-a-previously-synced-product-or-product-field-in-shopify}

Braze elimina automáticamente el producto o campo de tu catálogo de Shopify cuando detecta la eliminación. Sin embargo, cualquier Campaign, Canvas o Segment que haga referencia al producto o campo eliminado dejará de funcionar. Antes de eliminar productos o campos en Shopify, verifica que no se estén utilizando activamente en Braze.

### ¿Cómo cambio mi ID de catálogo (identificador de producto)? {#how-do-i-change-my-catalog-id-product-identifier}

Para cambiar tu ID de catálogo, primero desactiva la sincronización y confirma que ningún mensaje activo haga referencia a los datos de este catálogo. Luego vuelve a ejecutar la sincronización inicial y selecciona el identificador deseado.

### ¿Cambiar mis etiquetas, colecciones o metafields sincronizados afectará a las campañas activas? {#will-changing-my-synced-tags-collections-or-metafields-affect-active-campaigns}

Sí. Cambiar tus selecciones sincronizadas puede afectar a Campaigns, Canvas o [selecciones de catálogo]({{site.baseurl}}/catalog_selections/) activos que hagan referencia a ellos. Verifica que tu contenido activo esté actualizado antes de realizar cambios.

### ¿Cuánto tarda la sincronización inicial? {#how-long-does-the-initial-sync-take}

El tiempo de sincronización depende del número de productos y variantes en tu tienda. La sincronización inicial extrae productos en lotes, por lo que puede tardar un tiempo en que todas las etiquetas de producto, metafields y asociaciones de colecciones aparezcan. Monitoriza el estado de tu sincronización en la página del socio de Shopify.

## Configuración y límites {#configuration-and-limits}

### ¿Cuántas etiquetas, colecciones o metafields puedo sincronizar? {#how-many-tags-collections-or-metafields-can-i-sync}

Puedes sincronizar hasta 20 de cada uno por configuración:

- Hasta 20 etiquetas de producto
- Hasta 20 colecciones
- Hasta 20 metafields de producto

### ¿Qué pasa si un producto pertenece a más de 250 colecciones? {#what-if-a-product-belongs-to-more-than-250-collections}

Shopify permite que los productos pertenezcan a más de 250 colecciones, pero Braze solo puede obtener las primeras 250 asociaciones de colecciones por producto. Si un producto pertenece a una colección seleccionada que queda fuera de las primeras 250 obtenidas, esa asociación no se reflejará en tu catálogo de Shopify. Si notas asociaciones de colecciones faltantes, ponte en contacto con tu administrador del éxito del cliente.

### ¿Por qué no veo todas mis colecciones en el modal de configuración? {#why-dont-i-see-all-my-collections-in-the-configuration-modal}

El modal de configuración muestra hasta 5000 de las colecciones actualizadas más recientemente. Si tu tienda supera este límite, es posible que las colecciones más antiguas no aparezcan. Las colecciones previamente seleccionadas que queden fuera de las 5000 principales seguirán mostrándose en tu selección.

### ¿Puedo filtrar por etiquetas y colecciones a la vez en una sola selección de catálogo? {#can-i-filter-by-both-tags-and-collections-in-a-single-catalog-selection}

No. Las selecciones de catálogo solo admiten un campo de array por filtro de selección. No puedes combinar etiquetas y colecciones en la misma selección. Si necesitas segmentar usuarios en función de criterios de etiquetas y colecciones, utiliza [extensiones de segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/) con consultas SQL en su lugar.

### ¿Cuáles son los límites de las selecciones de catálogo? {#what-are-the-catalog-selection-limits}

Las selecciones de catálogo están sujetas a los mismos límites que las selecciones de catálogo estándar. Para obtener detalles sobre los límites de elementos, restricciones de filtros y límites de almacenamiento por nivel, consulta [Selecciones de catálogo]({{site.baseurl}}/catalog_selections/).

## Metafields y solución de problemas {#metafields-and-troubleshooting}

### ¿Por qué algunos de mis tipos de metafield no aparecen? {#why-are-some-of-my-metafield-types-not-showing-up}

Solo los tipos de metafield compatibles aparecen en el modal de configuración. Los siguientes tipos no son compatibles actualmente: `dimension`, `json`, `link`, `money`, `rating`, `rich_text_field`, `volume` y `weight`. Para ver los tipos compatibles y la lista completa, consulta [Metafields de producto de Shopify]({{site.baseurl}}/shopify_catalogs/#shopify-product-metafields) en la página de sincronización de productos de Shopify.

### Recibí un error "Duplicate Metafield Column Name". ¿Qué hago? {#i-got-a-duplicate-metafield-column-name-error-what-do-i-do}

Dos o más de tus metafields seleccionados crearían el mismo nombre de columna en el catálogo. Deselecciona uno de los metafields en conflicto, o renombra la clave del metafield en Shopify para que cada uno se asigne a un nombre de columna único. Luego vuelve a guardar tu configuración.

### ¿Por qué mis etiquetas tardan más de lo esperado en cargarse? {#why-are-my-tags-taking-longer-than-expected-to-load}

Las etiquetas se obtienen directamente de Shopify cuando abres el modal de configuración. Si tu tienda tiene una gran cantidad de productos o etiquetas, esto puede tardar más en cargarse. Este es un comportamiento esperado y no afecta al rendimiento de la sincronización. Si la carga se agota de forma constante, intenta reducir el número total de etiquetas en tu tienda de Shopify o ponte en contacto con soporte.

## Almacenamiento {#storage}

### ¿Sincronizar datos de producto adicionales afectará a mi almacenamiento de catálogo? {#will-syncing-additional-product-data-affect-my-catalog-storage}

Sí. Sincronizar etiquetas, metafields y colecciones aumenta el uso de almacenamiento de tu catálogo. El nivel gratuito de catálogo tiene un límite de almacenamiento de 100 MB. Si tu sincronización supera tu límite, Braze deja de sincronizar y las actualizaciones de productos ya no se reflejarán. Ponte en contacto con tu director de cuentas para actualizar tu nivel si es necesario.