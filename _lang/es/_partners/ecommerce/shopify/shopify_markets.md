---
nav_title: Shopify Markets
article_title: Shopify Markets
description: "Este artículo de referencia cubre cómo configurar y usar la integración de Shopify Markets con Braze."
page_type: partner
search_tag: Partner
permalink: "/shopify_markets/"
hidden: true
---

# Shopify Markets

> Este artículo cubre la integración de Shopify Markets (actualmente en beta), incluyendo qué está dentro del alcance, cómo funciona y cómo usar los datos de tus mercados en tu mensajería. Braze está lanzando progresivamente funcionalidades adicionales de Markets a lo largo del período beta, escalando para soportar estructuras de mercado más complejas con el tiempo.

{% alert important %}
Shopify Markets está actualmente en beta. Para más información, contacta a tu administrador de éxito de cliente de Braze.
{% endalert %}

## Cómo funciona la integración {#how-the-integration-works}

Shopify Markets extiende tu integración existente de Shopify. Conecta tu tienda predeterminada a través de la ruta de integración [estándar]({{site.baseurl}}/partners/ecommerce/shopify/shopify_standard_integration) o [personalizada (SDK)]({{site.baseurl}}/partners/ecommerce/shopify/shopify_custom_integration), luego selecciona los mercados que quieres que Braze sincronice desde los mercados configurados de tu tienda. Las integraciones existentes pueden agregar mercados sin interrumpir catálogos, grupos de suscripción o eventos. Para instrucciones paso a paso, consulta [Configuración de Shopify Markets](#shopify-markets-setup).

Shopify Markets proporciona estas capacidades:

- **Perfiles con reconocimiento de mercado.** La integración captura la configuración regional de Shopify de cada usuario junto con los atributos estándar de país e idioma de Braze, para que puedas segmentar y desencadenar por mercado sin configuración personalizada.
- **Catálogos localizados.** Los datos de productos específicos del mercado se sincronizan diariamente: precios, moneda y disponibilidad por mercado, además de títulos, descripciones y URLs de productos traducidos.
- **Personalización con reconocimiento de mercado.** Usa la etiqueta de Liquid {% raw %}`{% shopify_market %}`{% endraw %} para personalizar con productos del catálogo del mercado de cada usuario, incluyendo el contenido traducido de Shopify. También puedes hacer referencia a detalles del mercado, como la moneda de presentación, desde eventos de Shopify compatibles como `ecommerce.order_placed`.
- **Alternativa de tienda predeterminada.** Cuando un usuario no pertenece a uno de tus mercados conectados, Braze usa la configuración y los productos de tu tienda predeterminada, para que cada usuario reciba un mensaje completo y preciso.

Para ejemplos, consulta [Usar datos de usuario de Markets](#use-markets-user-data) y [caso de uso de catálogo con reconocimiento de mercado](#tutorial-show-products-and-prices-per-market).

## Tipos de mercado de Shopify compatibles {#supported-shopify-market-types}

Durante esta fase de la beta, puedes seleccionar hasta 25 mercados de un solo país en Braze, sujeto a las siguientes reglas:

- Cada mercado seleccionado debe ser un [mercado de un solo país](https://help.shopify.com/en/manual/markets/getting-started/market-types#country-or-region-markets) activo. Los mercados B2B y de comercio minorista no son compatibles.
  - La configuración "Usar monedas locales" de Shopify no es compatible
- Un país solo puede pertenecer a un mercado seleccionado.
- Los mercados de múltiples países no son compatibles en esta fase de la beta.

Cada mercado seleccionado requiere un catálogo de mercado con productos activos para que Braze lo soporte:

- Precios específicos del mercado en productos, usando la moneda establecida en el catálogo del mercado
- Disponibilidad de productos por mercado
- Traducciones de productos realizadas a través de la aplicación Shopify Translate & Adapt (como el título del producto o el título de la variante)

![Perfil de mercado de Shopify para un mercado de Australia.]({% image_buster /assets/img/shopify/shopify_markets_example.png %})

### Consideraciones {#considerations}

#### General

- **Una tienda conectada:** Solo puedes conectar una tienda de Shopify habilitada para Markets a un espacio de trabajo de Braze a la vez.
- **Alcance de la configuración regional:** Las configuraciones regionales traen títulos y descripciones de productos traducidos basados en lo que configuraste usando la aplicación Shopify Translate & Adapt, y URLs específicas de la configuración regional. El precio, la moneda y otros campos compartidos del catálogo permanecen iguales entre configuraciones regionales dentro de un mercado. De forma predeterminada, Braze usa el [idioma predeterminado](https://help.shopify.com/en/manual/markets/languages) de cada mercado, la configuración regional principal que Shopify asigna a ese mercado. Si el soporte expandido de configuraciones regionales está activado para tu cuenta, Braze sincroniza configuraciones regionales adicionales configuradas para ese mercado.

#### Catálogo de mercado {#market-catalog}

- **Nuevas vistas de mercado en tu catálogo original de Shopify:** Markets no crea catálogos separados. En su lugar, se muestran como parte de tu catálogo original de Shopify. Los datos de Markets se agregan como nuevas filas de catálogo a tu catálogo de Shopify.
- **Selecciones de catálogo:** Hasta 30 selecciones de catálogo.
- **Tiempo de actualización:** Los datos de productos del catálogo de mercado se actualizan una vez al día.
- **Catálogos de mercado solo de precios:** Un catálogo de mercado solo de precios establece precios específicos del mercado sin publicar productos en un canal de ventas. El inventario y la disponibilidad de productos se sincronizan desde tu catálogo de tienda predeterminado, mientras que el precio refleja la lista de precios del catálogo de mercado o los precios contextuales.

### Características no compatibles {#unsupported-features}

Las siguientes no son compatibles en esta beta:

- Desencadenadores de bajada de precio y vuelta en stock para catálogos de mercado
- Doble adhesión voluntaria por correo electrónico y SMS para grupos de suscripción configurados por mercado
- Grupos de mercado anidados o flujos de trabajo de grupos de países más allá del modelo actual de selección de un solo país y múltiples países
- Seleccionar más de 25 mercados
- Exportación de catálogo para catálogos habilitados para mercados
- Paridad completa con la conversión de moneda local de Shopify, reglas de redondeo y comportamiento de precio más bajo de múltiples catálogos en navegación y pago

## Configuración de Shopify Markets {#shopify-markets-setup}

### Paso 1: Conecta tu tienda habilitada para Shopify Markets {#step-1-connect-your-shopify-markets-enabled-store}

1. Conecta tu tienda usando la ruta de [integración estándar de Shopify]({{site.baseurl}}/partners/ecommerce/shopify/shopify_standard_integration) o [integración personalizada de Shopify]({{site.baseurl}}/partners/ecommerce/shopify/shopify_custom_integration). Después de que tu tienda esté conectada, configura Shopify Markets en el creador de configuración.
2. Completa el flujo de OAuth y confirma que Braze solicita los alcances de mercados en el OAuth:
   - `read_markets`
   - `read_publications`
   - `read_locales`
3. Después de que la autorización sea exitosa y se abra el creador de configuración, selecciona **Begin Setup**.
4. Activa los SDK de Braze.

### Paso 2: Selecciona tu mercado y la configuración de datos {#step-2-select-your-market-and-data-settings}

1. En **Track Shopify Data**, selecciona **Sync Shopify Markets data**.
2. Selecciona **Select Markets** para elegir tu mercado, y asegúrate de haber elegido rastrear eventos de comportamiento y atributos de usuario.
   - (Opcional) Activa el relleno histórico

#### Datos de usuario de Markets {#markets-user-data}

Para soportar Shopify Markets, Braze sincroniza más datos que los [eventos y atributos estándar]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features#tracked-shopify-events) de la integración.

Braze escribe este contexto de mercado adicional en cada perfil de usuario:

| Tipo de datos | Valor | Origen de datos |
| --- | --- | --- |
| Atributo personalizado | `shopify_locale` | Shopify |
| Atributo estándar | idioma del navegador | SDK de Braze |
| Atributo estándar | país | SDK de Braze |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Tipo de datos del perfil de usuario"}

Braze también recopila las siguientes propiedades adicionales de eventos de pedido para soportar el contexto de mercados:

| Tipo de datos | Eventos afectados | Nuevas propiedades agregadas |
| --- | --- | --- |
| Eventos recomendados de eCommerce | `ecommerce.order_placed`<br>`ecommerce.order_cancelled`<br>`ecommerce.order_refunded` | `country`, `presentment_currency`, `market_handle` |
| Eventos personalizados | `shopify_paid_order`<br>`shopify_fulfilled_order`<br>`shopify_partially_fulfilled_order` | `country`, `presentment_currency`, `market_handle` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Tipo de datos de eventos de pedido"}

Cada propiedad se deriva de las siguientes fuentes:

| Propiedad | Origen de datos |
| --- | --- |
| `country` | `default_address` del cliente de Shopify; si no está disponible, Braze usa `shipping_address` |
| `presentment_currency` | Valor monetario de presentación de Shopify |
| `market_handle` | Mercado de Shopify configurado para el país del pedido; se establece solo cuando los mercados están configurados y el país coincide |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Orígenes de datos de propiedades de eventos de pedido"}

### Paso 3: Administrar usuarios {#step-3-manage-users}

1. Selecciona tu tipo de `external_id` del menú desplegable.
2. Activa las adhesiones voluntarias de correo electrónico y SMS desde Shopify, lo que permite a Braze sincronizar los estados de suscripción de correo electrónico y SMS desde Shopify. Tienes dos opciones:
  - **Usar la integración:** Braze sincroniza los estados de correo electrónico y SMS. Solo necesitas elegir los grupos de suscripción a los que se sincronizan.
  - **Construir la tuya propia:** Para más control sobre la gestión de estados, puedes construir una integración personalizada usando los endpoints de grupos de suscripción de Braze.
3. Crea grupos de suscripción predeterminados para cada país asociado con tus mercados sincronizados durante la configuración.
  - **Nueva integración de Shopify:** Asigna un grupo de suscripción predeterminado de correo electrónico y SMS por país.
  - **Integración existente de Shopify:** El grupo predeterminado actual de tu tienda deja de sincronizarse. Asigna nuevos grupos predeterminados de correo electrónico y SMS por país. Tu configuración anterior no se transfiere automáticamente.

#### Cómo funcionan las adhesiones voluntarias y las cancelaciones de suscripción {#how-opt-ins-and-unsubscribes-work}

Durante la configuración, configuras grupos de suscripción predeterminados de correo electrónico y SMS para cada país asociado con tus mercados sincronizados (hasta 25 países). Esto es obligatorio antes de que puedas guardar la configuración de tu país. También puedes asignar grupos de suscripción adicionales por país si deseas dirigir el consentimiento a más de una lista.

##### El consentimiento se aplica a todos los países configurados {#consent-applies-to-all-configured-countries}

Cuando el estado de consentimiento de un usuario cambia en Shopify, Braze aplica ese cambio en los grupos de suscripción predeterminados de cada país vinculados a tu tienda conectada, no solo al país específico del usuario:
  - Si un usuario se suscribe en Shopify, se suscribe al grupo de suscripción predeterminado de correo electrónico o SMS de cada país que hayas configurado.
  - Si un usuario cancela su suscripción en Shopify, se cancela su suscripción del grupo de suscripción predeterminado de correo electrónico o SMS de cada país que hayas configurado.

{% alert important %}
El consentimiento de Shopify es por tienda, no por país. En Shopify, el consentimiento se rastrea una vez para correo electrónico y una vez para SMS por registro de cliente, y no suscribe ni cancela la suscripción por país o por tipo de lista. Debido a esto, Braze no puede aplicar cambios de consentimiento a un solo país o a un solo grupo de suscripción. Un evento de suscripción o cancelación de suscripción en Shopify siempre se aplica a los grupos de suscripción predeterminados de todos tus países configurados a la vez. <br><br> Sin embargo, dentro de Braze, puedes tener un control más granular de las adhesiones voluntarias y cancelaciones a nivel de grupo de suscripción a medida que los usuarios interactúan con los canales de mensajería.
{% endalert %}

### Paso 4: Sincronizar productos {#step-4-sync-products}

1. Para sincronizar productos dentro de tu mercado, selecciona **Sync Shopify products and variants to Braze**.
2. Asigna el **catalog ID** de Braze y configura cualquier ajuste adicional.

Tu catálogo incluye una vista por mercado para los productos predeterminados de tu tienda. Para cada producto publicado en tu mercado, Braze agrega una fila de mercado a tu catálogo existente, además de los [campos estándar del catálogo de Shopify]({{site.baseurl}}/partners/ecommerce/shopify/shopify_catalogs#supported-shopify-catalog-data) ya compatibles. Puede tomar unos minutos para que estos se sincronicen si activas Shopify Markets en una integración existente.

En las filas de mercado, estos campos tienen valores específicos del mercado:

| Campo | Descripción |
| --- | --- |
| {% raw %}`market_handle`{% endraw %} | Identifica el mercado para la fila. Las filas del mercado predeterminado usan `default`; los mercados adicionales usan su identificador (por ejemplo, `au`). |
| {% raw %}`locale`{% endraw %} | Cuando el soporte expandido de configuraciones regionales está habilitado, identifica la configuración regional para la fila (por ejemplo, `fr`). |
| {% raw %}`price`{% endraw %} | Precio específico del mercado desde los precios contextuales del mercado. |
| {% raw %}`compare_at_price`{% endraw %} | Precio de comparación específico del mercado, o `0` cuando Shopify no tiene un precio de comparación para ese mercado. |
| {% raw %}`product_title`{% endraw %} | Título del producto traducido cuando existe una traducción de Shopify para la configuración regional de la fila. |
| {% raw %}`variant_title`{% endraw %} | Título de la variante traducido cuando existe una traducción de Shopify para la configuración regional de la fila. |
| {% raw %}`product_url`{% endraw %} | URL de la tienda para el mercado y la configuración regional cuando las URLs localizadas están habilitadas; de lo contrario, esta es la URL predeterminada del producto en `myshopify.com`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Campos del catálogo de filas de mercado"}

Las filas de mercado usan un `id` compuesto con prefijo del identificador del mercado, como `<market>_<variant_id>`. Cuando el soporte expandido de configuraciones regionales está habilitado, el ID también incluye la configuración regional (por ejemplo, `<market>_<locale>_<variant_id>`). Tus productos predeterminados mantienen sus IDs originales.

### Paso 5: Activar canales {#step-5-activate-channels}

1. (Opcional) Elige si deseas habilitar la **mensajería en el navegador**.
2. Selecciona **Finish Setup**.

## Usar datos de usuario de Markets {#use-markets-user-data}

Después de que estos atributos y propiedades estén en los perfiles de usuario, puedes usarlos para dirigirte a usuarios por mercado y personalizar mensajes.

### Dirigirse por mercado en la segmentación {#target-by-market-in-segmentation}

Filtra por país, idioma del navegador o `shopify_locale` en Segments y en los criterios de entrada de Campaign o Canvas. Como ejemplo, construye una audiencia de usuarios en un mercado específico, o divide un Canvas por configuración regional.

### Personalizar y desencadenar con Liquid {#personalize-and-trigger-with-liquid}

Haz referencia a los datos directamente en tus mensajes.

| Datos de usuario a referenciar | Liquid a usar |
| --- | --- |
| La configuración regional del usuario | {% raw %}`{{custom_attribute.${shopify_locale}}}`{% endraw %} |
| El país del usuario | {% raw %}`{{${country}}}`{% endraw %} |
| El país de un pedido (en un mensaje desencadenado) | {% raw %}`{{event_properties.${country}}}`{% endraw %} |
| El mercado de un pedido (en un mensaje desencadenado) | {% raw %}`{{event_properties.${market_handle}}}`{% endraw %} |
| La moneda de un pedido (en un mensaje desencadenado) | {% raw %}`{{event_properties.${presentment_currency}}}`{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Datos de usuario a referenciar con Liquid"}

### Desencadenar mensajes desde la actividad de pedidos {#trigger-messages-from-order-activity}

Las nuevas propiedades de pedido viajan con cada evento de pedido, por lo que puedes desencadenar un mensaje a partir de un pedido y personalizar lo que dice usando detalles con reconocimiento de mercado.

Una versión simple en el cuerpo del mensaje podría verse así:

{% raw %}
```liquid
Thanks for your order! Your total: {{event_properties.${presentment_currency}}} {{event_properties.${total_value}}}
```
{% endraw %}

Debido a que las propiedades están en el evento mismo, el mensaje se mantiene preciso para el mercado de cada usuario sin configuración adicional.

## Tutorial: Mostrar productos y precios por mercado {#tutorial-show-products-and-prices-per-market}

Usa un catálogo con reconocimiento de mercado para construir un solo mensaje que muestre a cada usuario los productos y precios de su propio mercado.

1. Crea una selección que use datos de mercados.
2. Haz referencia a la selección en un mensaje con Liquid.

Puedes usar un mercado fijo cuando un mensaje se dirige a un mercado específico.

### Paso 1: Crear una selección usando datos de mercados {#step-1-create-a-selection-using-markets-data}

Las [selecciones]({{site.baseurl}}/catalog_selections) son conjuntos de productos seleccionados que referencias en mensajes. Para catálogos de Shopify con mercados sincronizados, la sección **Filter settings** incluye un área de **Market scope** que limita los datos de productos a un mercado o los personaliza por usuario.

1. Ve a tu catálogo de Shopify y abre la pestaña **Selections**.
2. Selecciona **Create Selection**, luego nombra la selección, agrega una descripción opcional y establece un límite de resultados.
3. En **Filter settings**, bajo **Market scope**, usa el menú desplegable **Market** para elegir cómo la selección resuelve productos específicos del mercado:
   - **Personalized:** Cada destinatario ve productos y precios del mercado que coincide con el atributo `country` de su perfil.
   - **A synced market:** Selecciona un mercado por nombre para fijar la selección a los productos y precios de ese mercado. Usa esto cuando un mensaje se dirige a un solo mercado.
4. Termina cualquier criterio de filtro adicional, luego guarda la selección.
5. En **Preview for user**, selecciona un usuario para ver qué devuelve la selección para ese perfil. Las selecciones que usan **Personalized** solo pueden previsualizarse después de seleccionar un usuario.

| Objetivo | Filtro |
| --- | --- |
| Un mercado específico | `market_handle` = `au` |
| Solo productos predeterminados | `market_handle` = `default` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Objetivos y filtros asociados"}

{% alert note %}
Si no especificas un mercado, Braze usa tus productos predeterminados.
{% endalert %}

### Paso 2: Agregar selecciones de catálogo con reconocimiento de mercado a los mensajes {#step-2-add-market-aware-catalog-selections-to-messages}

Para servir a cada usuario los productos de su propio mercado en un solo mensaje, crea una selección con este filtro:

| Nombre de la selección | Campo | Operador | Valor |
| --- | --- | --- | --- |
| `market_products` | `market_handle` | equals | {% raw %}`{{shopify_market.handle}}`{% endraw %} |
| `default_products` | `market_handle` | equals | `default` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Nombre de la selección y filtros asociados"}

En el momento del envío, Braze reemplaza {% raw %}`{{shopify_market.handle}}`{% endraw %} con el mercado de cada usuario, por lo que `market_products` le da a todos los productos correctos. `default_products` es la alternativa para usuarios sin un mercado coincidente.

Haz referencia a tu selección en tu mensaje con la etiqueta {% raw %}`{% shopify_market %}`{% endraw %}:

{% raw %}
```liquid
{% shopify_market %}
{% if shopify_market.handle %}
  {% catalog_selection_items <your_catalog_name> <your_market-catalog_selection_name> %}
  {% for item in items %}
    {{ item.product_title }} — {{ item.price }}
  {% endfor %}
{% else %}
  {% catalog_selection_items <your_catalog_name> <your_default-catalog_selection_name> %}
  {% for item in items %}
    {{ item.product_title }} — {{ item.price }}
  {% endfor %}
{% endif %}
```
{% endraw %}

- Coloca {% raw %}`{% shopify_market %}`{% endraw %} antes de {% raw %}`{% catalog_selection_items %}`{% endraw %} para que el mercado del usuario se establezca antes de que se ejecute la selección.
- Reemplaza `<your_catalog_name>` con tu catálogo, y usa tus propios nombres de selección si difieren.
- La verificación de {% raw %}`{{shopify_market.handle}}`{% endraw %} dirige a los usuarios sin un mercado coincidente a `default_products`, para que aún reciban productos en lugar de un mensaje vacío.

Previsualiza como un usuario en tu mercado para confirmar que el mensaje muestra los productos, precios y títulos traducidos de ese mercado.