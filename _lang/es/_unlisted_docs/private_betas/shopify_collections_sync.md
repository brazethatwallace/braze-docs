---
nav_title: Sincronización de colecciones de Shopify
article_title: Sincronización de colecciones de Shopify
permalink: "/shopify_collections_sync/"
description: "Este artículo de referencia explica cómo configurar la sincronización de colecciones de Shopify, que te permite agrupar tus productos en colecciones para que los clientes puedan encontrarlos por categoría."
hidden: true
---

# Beta de sincronización de colecciones de Shopify {#shopify-collections-sync-beta}

> La sincronización de colecciones de Shopify te permite agrupar tus productos en colecciones para que los clientes puedan encontrarlos por categoría. Para una experiencia de compra más fluida, puedes incorporar artículos de las colecciones de tu tienda en tu mensajería de Braze.

{% alert important %}
La sincronización de colecciones de Shopify se encuentra actualmente en fase beta. Ponte en contacto con tu director de cuentas de Braze si deseas participar en la beta.
{% endalert %}

## Configuración de la sincronización de colecciones de Shopify {#setting-up-shopify-collections-sync}

Para sincronizar tus productos desde tu tienda Shopify con Braze, selecciona la casilla **Sync Shopify collections** en el paso **Sync products** de [integrar Shopify]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/setting_up_shopify#setting-up-shopify-in-braze).<br><br>![Paso 4 de la sincronización de productos de Shopify con la casilla "Sync Shopify collections" seleccionada.][1]

Una vez que tus productos se hayan sincronizado, puedes ver qué productos están asociados con tus colecciones consultando tu catálogo de Shopify. <br><br>![Fila de tabla del catálogo que muestra un producto en las colecciones "best-sellers" y "front page".][2]

Desde tu catálogo de Shopify, puedes ver tu colección de Shopify en la pestaña **Selections**. <br><br>![La pestaña Selections mostrando una lista de dos colecciones: "best-sellers" y "front page".][3]

### Funcionalidad beta {#beta-functionality}

- Braze admitirá hasta 30 colecciones.
- El orden de clasificación de tu colección no se mantiene ni se admite en este momento. Por ahora, el orden de clasificación se basa en lo siguiente:
    - Los elementos más recientes añadidos a tu colección.
    - El orden en que los elementos se actualizan durante las sincronizaciones continuas.
    - El orden que seleccionas en la pestaña de selección para tu colección de Shopify.

## Uso de las colecciones de Shopify {#using-shopify-collections}

Usa tus colecciones de Shopify para personalizar un mensaje para cada usuario en tu Campaign, de forma similar a como usarías una [selección de Braze]({{site.baseurl}}/user_guide/data/activation/catalogs/selections).

{% alert warning %}
Ten en cuenta el siguiente comportamiento en la versión beta: <br><br>Si actualizas la descripción de la colección de Shopify o la configuración de los filtros, interrumpirás la sincronización de tu colección de Shopify. Como resultado, tu colección de Shopify no funcionará como se espera.
{% endalert %}

### Paso 1: Configura el orden de clasificación de tu colección de Shopify {#step-1-configure-the-sort-order-of-your-shopify-collection}

1. Especifica el orden en que se devuelven los resultados de tu colección de Shopify seleccionando **Sort Order** en la pestaña de selección de tu colección de Shopify. Esto incluye una opción para aleatorizar el orden de clasificación.
2. Introduce el número máximo de resultados (hasta 50) en **Limit number**.
3. Selecciona **Update Selection**.

![La página Editar selección donde puedes seleccionar la configuración de los filtros, el tipo de ordenamiento y el límite de resultados.][4]

### Paso 2: Usa la colección en una Campaign {#step-2-use-the-collection-in-a-campaign}

1. Crea una Campaign, luego selecciona **+ Personalization** en el creador de mensajes.
2. Selecciona lo siguiente:<br>- **Catalog Items** como el **Personalization type**<br>- El nombre del catálogo<br>- El método de selección de elementos<br>- El nombre de la selección (el nombre de tu colección de Shopify) <br>- La información que deseas mostrar en tu mensaje

{: start="3"}
3. Copia y pega el fragmento de código Liquid donde quieras que aparezca la información en tu mensaje.

![La sección "Add Personalization" con campos para seleccionar tu catálogo, el método de selección de elementos y la información a mostrar.][5]{: style="max-width:30%;"}

#### Liquid en los resultados de la selección {#liquid-in-selection-results}

El uso de cualquier resultado en catálogos, como atributos personalizados y eventos personalizados, puede provocar que se devuelvan resultados diferentes para cada usuario en tu selección.

[1]: {% image_buster /assets/unlisted_docs/img/shopify/sync_products.png %}
[2]: {% image_buster /assets/unlisted_docs/img/shopify/view_catalog.png %}
[3]: {% image_buster /assets/unlisted_docs/img/shopify/selections_tab.png %}
[4]: {% image_buster /assets/unlisted_docs/img/shopify/edit_selection.png %}
[5]: {% image_buster /assets/unlisted_docs/img/shopify/add_personalization.png %}