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
Shopify Markets está actualmente en beta. Para más información, contacta a tu CSM de Braze.
{% endalert %}

## Cómo funciona la integración {#how-the-integration-works}

Shopify Markets amplía tu integración existente de Shopify. Conecta tu tienda predeterminada a través de la ruta de integración [estándar]({{site.baseurl}}/partners/ecommerce/shopify/shopify_standard_integration) o [personalizada (SDK)]({{site.baseurl}}/partners/ecommerce/shopify/shopify_custom_integration), y luego selecciona los mercados que quieres que Braze sincronice a partir de los mercados configurados en tu tienda. Las integraciones existentes pueden agregar mercados sin interrumpir catálogos, grupos de suscripción ni eventos. Para obtener instrucciones paso a paso, consulta [Configuración de Shopify Markets](#shopify-markets-setup).

Shopify Markets ofrece estas capacidades:

- **Perfiles con reconocimiento de mercado:** La integración captura la configuración regional de Shopify de cada usuario junto con los atributos estándar de país e idioma de Braze, para que puedas segmentar y desencadenar por mercado sin necesidad de configuración personalizada.
- **Catálogos localizados:** Los datos de productos específicos por mercado se sincronizan diariamente, incluyendo precios y moneda, así como títulos, descripciones y URL de productos traducidos.
- **Personalización con reconocimiento de mercado:** Usa la etiqueta de Liquid {% raw %}`{% shopify_market %}`{% endraw %} para personalizar con productos del catálogo del mercado de cada usuario, incluyendo el contenido traducido de Shopify. También puedes hacer referencia a detalles del mercado, como la moneda de presentación, a partir de eventos de Shopify compatibles como `ecommerce.order_placed`.
- **Alternativa de tienda predeterminada:** Cuando un usuario no pertenece a uno de tus mercados conectados, Braze utiliza la configuración y los productos de tu tienda predeterminada, de modo que cada usuario recibe un mensaje completo y preciso.

Para ver ejemplos, consulta [Usar datos de usuario de Markets](#use-markets-user-data) y [Tutorial: Mostrar productos y precios por mercado](#tutorial-show-products-and-prices-per-market).

## Tipos de mercados de Shopify compatibles {#supported-shopify-market-types}

Puedes seleccionar hasta 25 [mercados activos de un solo país o de varios países](https://help.shopify.com/en/manual/markets/getting-started/market-types#country-or-region-markets). Cada país solo puede pertenecer a un mercado seleccionado.

Los mercados de subregiones, mercados de comercio minorista, mercados B2B y mercados de canal no son compatibles.

### Qué necesita cada mercado {#what-each-market-needs}

Cada mercado seleccionado necesita un catálogo de mercado con productos activos. Braze lee lo siguiente de ese catálogo:

| Datos | Descripción |
| --- | --- |
| Precios | Establecidos en el catálogo de mercado, en la divisa especificada para ese mercado. La configuración "Use local currencies" de Shopify no es compatible. |
| Traducciones | Traducciones adaptadas realizadas a través de la aplicación Shopify Translate & Adapt, como el título del producto y el título de la variante. Actualmente, Braze no es compatible con configuraciones de idioma específicas del mercado. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Qué necesita cada mercado" }

![Perfil de mercado de Shopify para un mercado de Australia.]({% image_buster /assets/img/shopify/shopify_markets_example.png %})

### Consideraciones {#considerations}

#### General

- **Una tienda conectada:** Solo puedes conectar una tienda Shopify habilitada para Markets a un espacio de trabajo de Braze a la vez.
- **Alcance de la configuración regional:** Las configuraciones regionales obtienen títulos y descripciones de productos traducidos según lo que configuraste con la aplicación Shopify Translate & Adapt, además de URLs específicas de la configuración regional. El precio, la divisa y otros campos compartidos del catálogo permanecen iguales en todas las configuraciones regionales dentro de un mercado. De forma predeterminada, Braze utiliza el [idioma predeterminado](https://help.shopify.com/en/manual/markets/languages) de cada mercado, la configuración regional principal que Shopify asigna a ese mercado. Si activas la compatibilidad ampliada con configuraciones regionales, Braze sincroniza las configuraciones regionales adicionales configuradas para ese mercado.

#### Catálogo de mercado {#market-catalog}

- **Nuevas vistas de mercado en tu catálogo original de Shopify:** Markets no crea catálogos separados. En su lugar, Braze los muestra como parte de tu catálogo original de Shopify. Los datos de Markets se añaden como nuevas filas de catálogo a tu catálogo de Shopify.
- **Selecciones de catálogo:** Hasta 30 selecciones de catálogo.
- **Frecuencia de actualización:** Los datos de productos del catálogo de mercado se actualizan una vez al día.
- **Precios de mercado y contenido localizado:** Las filas de mercado incluyen el precio del mercado y `compare_at_price`, incluyendo títulos de productos y variantes localizados, así como URLs de productos cuando las traducciones están configuradas a través de la aplicación Shopify Translate & Adapt.
- **Cantidad de inventario:** Las filas de mercado incluyen valores de inventario agregados. Actualmente, Braze no ofrece la capacidad de diferenciar el inventario entre ubicaciones.
- **Bajada de precio:** Compatible con catálogos de mercado. Un cambio de precio en un catálogo de mercado se activa según el precio de ese mercado en lugar del precio predeterminado de tu tienda. Dado que los datos de productos del catálogo de mercado se actualizan una vez al día, las bajadas de precio se detectan diariamente en lugar de cuando el precio cambia en Shopify.
- **Vuelta a estar en existencias:** [Vuelta a estar en existencias]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/back_in_stock_notifications) es compatible con productos en tu catálogo de tienda predeterminado. Las filas de mercado no desencadenan notificaciones de vuelta a estar en existencias. Esta función analiza el inventario total disponible para una variante de producto en todas las ubicaciones de Shopify, por lo que el inventario añadido en una ubicación de comercio minorista puede desencadenar una notificación.

## Configuración de Shopify Markets {#shopify-markets-setup}

### Si ya tienes una integración activa de Shopify {#if-you-already-have-an-active-shopify-integration}

Markets se añade a tu integración actual. No necesitas desconectarla ni reconstruir tu configuración.

- Tus grupos de suscripción se convierten en tus grupos de toda la tienda y siguen recibiendo cada adhesión voluntaria, incluidos los grupos adicionales que hayas asignado.
- Tus suscriptores existentes permanecen en los grupos en los que ya están. Si agregas grupos de país más tarde, Braze no añade a los suscriptores existentes a esos grupos.
- Tu catálogo sigue sincronizándose. Las filas de mercado se añaden a él en lugar de a un catálogo nuevo, y tus selecciones existentes siguen funcionando con tus filas predeterminadas.
- Tu tienda predeterminada aparece junto a tus mercados seleccionados, lo que te permite asignar grupos de suscripción y crear selecciones de catálogo de la misma manera.

Si tu tienda ya está conectada, comienza con el [Paso 2](#step-2-select-your-market-user-data) para obtener más información sobre cada configuración y cómo funciona.

### Paso 1: Conecta tu tienda habilitada con Shopify Markets {#step-1-connect-your-shopify-markets-enabled-store}

1. Conecta tu tienda utilizando la ruta de [integración estándar de Shopify]({{site.baseurl}}/partners/ecommerce/shopify/shopify_standard_integration) o la [integración personalizada de Shopify]({{site.baseurl}}/partners/ecommerce/shopify/shopify_custom_integration). Después de conectar tu tienda, configura Shopify Markets en el creador de configuración.
2. Completa el flujo de OAuth y confirma que Braze solicita los alcances de mercados en el OAuth:
   - `read_markets`
   - `read_publications`
   - `read_locales`
3. Después de que la autorización tenga éxito y se abra el creador de configuración, selecciona **Begin Setup**.
4. Activa los SDK de Braze.

### Paso 2: Selecciona los datos de usuario de tu mercado {#step-2-select-your-market-user-data}

1. En **Track Shopify Data**, selecciona **Sync Shopify Markets data**.
2. Selecciona **Select Markets** para elegir tu mercado y asegúrate de haber seleccionado el seguimiento de eventos de comportamiento y atributos de usuario.
   - (Opcional) Activa el relleno de datos históricos

#### Datos de usuario de mercados {#markets-user-data}

Para dar soporte a Shopify Markets, Braze sincroniza datos adicionales más allá de los [eventos y atributos estándar]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features#tracked-shopify-events) de la integración.

##### Atributos del perfil de usuario {#user-profile-attributes}

| Atributo | Tipo de datos | Descripción | Origen de datos |
| --- | --- | --- | --- |
| `shopify_locale` | Atributo personalizado | El idioma en el que el cliente navega tu tienda, como `en` o `fr-CA`. Cambia cuando cambian el idioma de la tienda. | Configuración regional del cliente en Shopify |
| `browser_language` | Atributo estándar | El idioma configurado en el navegador del cliente. | SDK de Braze |
| `country` | Atributo estándar | El país del cliente. | SDK de Braze |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Atributos del perfil de usuario"}

##### Propiedades de eventos de pedido {#order-event-properties}

| Propiedad | Descripción | Origen de datos |
| --- | --- | --- |
| `country` | Código de país de dos letras del cliente. | La `default_address` del cliente en Shopify, o la `shipping_address` del pedido si no se ha configurado una dirección predeterminada |
| `presentment_currency` | La moneda en la que pagó el cliente, que puede diferir de la moneda de tu tienda. | Moneda de presentación del pedido en Shopify |
| `market_handle` | Handle del mercado que coincide con el país del cliente. Vacío cuando ningún mercado configurado coincide. | Braze, a partir de tu configuración de mercado |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Propiedades de eventos de pedido"}

Estas propiedades se añaden a:

- Eventos recomendados de eCommerce: `ecommerce.order_placed`, `ecommerce.order_cancelled`, `ecommerce.order_refunded`
- Eventos personalizados: `shopify_paid_order`, `shopify_fulfilled_order`, `shopify_partially_fulfilled_order`

##### Cómo funcionan estas propiedades de eventos de mercado {#how-these-market-event-properties-work}

| Propiedad | Cómo funciona |
| --- | --- |
| `market_handle` | `market_handle` es el handle que le diste al mercado en Shopify, como `france`. El mismo handle funciona como prefijo para los ID de las filas de mercado en tu catálogo, como `france_46714756268231`. Está vacío cuando no has configurado mercados, o cuando el país del pedido no coincide con un mercado que hayas configurado, así que verifica si el valor está vacío antes de usarlo en Liquid o en un filtro de Segment. |
| `country` | `country` proviene de la dirección predeterminada del cliente y usa la `shipping_address` si la predeterminada no existe. Por ejemplo, un cliente en Francia que envía un pedido a Japón sigue llevando el mercado de Francia. |
| Propiedades del evento | Las propiedades del evento son una instantánea del momento en que ocurrió el evento y no cambian después. Si un cliente actualiza su dirección predeterminada más tarde, los nuevos eventos usan su nuevo país, mientras que los eventos anteriores conservan el país con el que se registraron. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Cómo funcionan las propiedades de eventos de mercado"}

##### Moneda {#currency}

Los eventos compatibles de carrito, pago y pedido de Shopify llevan dos conjuntos de valores:
- La moneda de tu tienda en los campos existentes de precio y total, sin cambios
- El objeto `presentment_currency` que contiene los montos que el cliente vio y pagó

Usa `presentment_currency` cuando le muestres al cliente lo que pagó, como una confirmación de pedido o un mensaje de carrito abandonado. Usa los valores de moneda de la tienda cuando compares ingresos entre mercados, ya que están en una moneda única.

##### Información localizada del producto {#localized-product-information}

Los eventos compatibles de Shopify llevan los títulos del producto y la variante en el idioma predeterminado de tu tienda. Braze no traduce las cargas útiles de los eventos.

Los títulos traducidos, las descripciones y las URL de los productos se encuentran en las filas de catálogo de tu mercado. Para mostrar información localizada del producto en un mensaje, busca el producto en tu catálogo usando el ID de producto o de variante del evento.

### Paso 3: Administra usuarios {#step-3-manage-users}

1. Selecciona tu tipo de `external_id` en el menú desplegable.
2. Activa las adhesiones voluntarias de correo electrónico y SMS desde Shopify, lo que permite a Braze sincronizar los estados de suscripción de correo electrónico y SMS desde Shopify. Tienes dos opciones:
   - **Usar la integración:** Braze sincroniza los estados de correo electrónico y SMS. Selecciona los grupos de suscripción con los que se sincronizan.
   - **Crea la tuya:** Para tener más control sobre la gestión de estados, crea una integración personalizada usando los endpoints de grupos de suscripción de Braze.
3. Selecciona los grupos de suscripción con los que se sincroniza el consentimiento de Shopify:
   - **Grupos de toda la tienda (obligatorio):** Selecciona al menos un grupo de correo electrónico y un grupo de SMS. Cada adhesión voluntaria que Braze recibe de Shopify se registra aquí.
   - **Grupos de país (opcional):** Asigna uno o más grupos a cualquier país en tus mercados sincronizados. Las adhesiones voluntarias también se registran aquí cuando Braze puede determinar el país del cliente.

#### Cómo funcionan las adhesiones voluntarias y los rechazos {#how-opt-ins-and-opt-outs-work}

En Shopify, cada cliente tiene un estado de consentimiento de correo electrónico y un estado de consentimiento de SMS. Cuando los clientes se adhieren, se suscriben a tu marca, no a un país ni a una lista.

Braze registra cada adhesión voluntaria en tus grupos de toda la tienda. Si configuras grupos de país y Braze puede determinar en qué país está el cliente, la adhesión voluntaria también se registra en los grupos de ese país.

Si no configuras grupos de país, las adhesiones voluntarias van solo a tus grupos de toda la tienda, lo cual coincide con cómo Shopify gestiona el consentimiento actualmente.

#### Cómo determina Braze el país {#how-braze-determines-country}

| Canal | Determinación del país |
| ------- | ---------------------------- |
| Correo electrónico | Usa primero la configuración regional de Shopify del cliente; si no está disponible, usa el atributo de país en su perfil de Braze. |
| SMS | Usa el país del número de teléfono, según lo determinado por los patrones de enrutamiento de país E.164. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Determinación de país por canal en Braze"}

Una configuración regional identifica un país solo cuando incluye una región, como `fr-FR`. Una configuración regional de `fr` por sí sola no lo hace.

Para SMS, el país proviene del número de teléfono. El comprador debe estar agregado a un grupo de suscripción que pueda enviar mensajes a ese número.

#### Qué sucede cuando alguien se adhiere {#what-happens-when-someone-opts-in}

| Estado del país | Grupos de toda la tienda | Grupos de país |
|------------------------------------------|-------------------|---------------------------------------|
| Determinado y configurado en tus mercados | Suscrito | Suscrito a los grupos de ese país |
| No se puede determinar | Suscrito | No suscrito |
| Determinado, pero no configurado en tus mercados | Suscrito | No suscrito |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Resultados de adhesión según el estado del país"}

La pertenencia a un grupo de suscripción se basa en los eventos de consentimiento de Shopify. Si el país o la configuración regional de un comprador cambia, su pertenencia al grupo no cambia. Braze la actualiza solo cuando Shopify envía un nuevo evento de consentimiento, por ejemplo si se recopila el consentimiento nuevamente del comprador en Shopify después de que el país o la configuración regional haya cambiado.

{% alert note %}
Los grupos de país controlan el consentimiento, no el idioma. Un país puede tener más de un idioma. Los clientes de habla inglesa y francesa en Canadá, `en-CA` y `fr-CA`, pertenecen al mismo grupo de país. Usa `shopify_locale` dentro de tus mensajes para especificar el idioma.
{% endalert %}

#### Qué sucede cuando alguien rechaza {#what-happens-when-someone-opts-out}

Un rechazo en Shopify elimina al usuario de todos los grupos de suscripción asignados a tu integración de Shopify. Esto es igual independientemente de si se dieron de baja a través de un sitio de mercado o a través de su página de cuenta de Shopify.

Los grupos de suscripción en tu espacio de trabajo que no están asignados a la integración no se ven afectados.

#### Adhesiones voluntarias desde países que no has configurado {#opt-ins-from-countries-you-havent-configured}

Si un cliente se adhiere desde un país que no forma parte de tus mercados configurados, ya sea porque nunca lo agregaste o porque eliminaste ese mercado, se suscribe a tus grupos de toda la tienda. No se le agrega a ningún grupo de país.

Configurar mercados no restringe a quién puedes enviar mensajes. Si no puedes enviar mensajes a un país por razones legales o regulatorias, excluye a esos usuarios con un filtro de Segment o dirígelos a un grupo de suscripción separado.

{% alert tip %}
Crea ese Segment como una lista de permitidos de los países a los que prestas servicio, no como una lista de bloqueo de los que no. Los usuarios cuyo país no se pudo determinar no tienen valor de país, por lo que una lista de bloqueo no los detectará.
{% endalert %}

Para SMS, los permisos de país de cada grupo de suscripción siguen controlando la entrega. Un usuario cuyo país no está permitido en el grupo no recibirá mensajes de este.

#### Los usuarios no se agregan a los grupos de país más tarde {#users-arent-added-to-country-groups-later}

Si Braze no puede determinar el país de un cliente cuando se adhiere, se le agrega únicamente a tus grupos de toda la tienda. Si su país se conoce más tarde, no se le agrega automáticamente a los grupos de ese país.

Cuando activas Markets en una tienda ya integrada, tus grupos de suscripción existentes se convierten en tus grupos de toda la tienda. Los suscriptores existentes permanecen suscritos a estos grupos y no se agregan automáticamente a los nuevos grupos de país.

Para agregarlos tú mismo, crea un Segment para esos usuarios y suscríbelos usando un paso [User Update]({{site.baseurl}}/user_update) de Canvas.

#### Conteo de suscriptores entre grupos {#counting-subscribers-across-groups}

Una adhesión voluntaria puede agregar a un usuario a más de un grupo de suscripción, por lo que sumar los totales de los grupos cuenta a la misma persona varias veces. Usa un Segment cuando necesites un conteo de suscriptores únicos.

#### Cómo funciona {#how-it-works}

1. Un cliente se suscribe a SMS en el pago o a través de un formulario.
2. Shopify envía la suscripción a Braze.
3. Braze establece al usuario como pendiente y envía tu texto de confirmación.
4. El cliente responde con tu palabra clave de confirmación y queda suscrito.
5. Si no responde antes de que termine la ventana de confirmación, permanece como pendiente.

Para obtener más información, consulta [Doble adhesión voluntaria]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/double_opt_in).

### Paso 4: Sincroniza productos {#step-4-sync-products}

1. Para sincronizar productos dentro de tu mercado, selecciona **Sync Shopify products and variants to Braze**.
2. Asigna el ID de catálogo de Braze y configura cualquier ajuste adicional.

Tu catálogo incluye una vista por mercado para los productos predeterminados de tu tienda. Para cada producto publicado en tu mercado, Braze agrega una fila de mercado a tu catálogo existente, además de los [campos de catálogo estándar de Shopify]({{site.baseurl}}/partners/ecommerce/shopify/shopify_catalogs#supported-shopify-catalog-data) que ya son compatibles. Puede tardar unos minutos en sincronizarse si activas Shopify Markets en una integración existente.

En las filas de mercado, estos campos tienen valores específicos del mercado:

| Campo | Descripción |
| --- | --- |
| `id` | Un ID compuesto con prefijo del handle de mercado, como `france_46714756268231`. Las filas predeterminadas mantienen sus ID de artículo originales. |
| `market_handle` | El handle que le diste al mercado en Shopify, como `france`. |
| `locale` | La configuración regional del mercado, que determina el idioma del contenido traducido. |
| `price` | Precio específico del mercado a partir de la fijación de precios contextual del mercado, después de aplicar cualquier ajuste de la lista de precios. |
| `compare_at_price` | Precio de comparación específico del mercado después de los ajustes. Braze devuelve `0` cuando no se resuelve ningún precio de comparación para ese mercado, incluso cuando la lista de precios del mercado está configurada para anular los precios de comparación. |
| `product_title` y `variant_title` | Títulos traducidos, cuando las traducciones están configuradas a través de la aplicación Shopify Translate & Adapt. |
| `product_url` | La URL del producto para ese mercado. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Campos de catálogo de filas de mercado"}

{% alert important %}
`inventory_quantity` no está incluido en las filas de mercado. Aparece solo en las filas predeterminadas, donde refleja el inventario total disponible para una variante de producto en todas las ubicaciones de Shopify.<br><br>Cuando uses `compare_at_price` en Liquid, verifica si es "0" antes de mostrarlo o calcular un descuento. Un mercado sin precio de comparación muestra un precio de cero o un descuento incorrecto.
{% endalert %}

### Paso 5: Activa canales {#step-5-activate-channels}

1. (Opcional) Selecciona si deseas habilitar la mensajería dentro del navegador.
2. Selecciona **Finish Setup**.

## Usar datos de usuario de Markets {#use-markets-user-data}

Después de que estos atributos y propiedades estén en los perfiles de usuario, puedes usarlos para segmentar usuarios por mercado y personalizar mensajes.

### Segmentar por mercado en la segmentación {#target-by-market-in-segmentation}

Filtra por país, idioma del navegador o `shopify_locale` en Segments y en los criterios de entrada de Campaign o Canvas. Por ejemplo, crea una audiencia de usuarios en un mercado específico, o divide un Canvas por configuración regional.

### Desencadenar y personalizar con Liquid {#trigger-and-personalize-with-liquid}

Haz referencia a los datos de mercado en tus mensajes con estas variables de Liquid.

#### Desde el perfil de usuario {#from-the-user-profile}

| Atributo | Liquid |
| --- | --- |
| El idioma del cliente | {% raw %}`{{custom_attribute.${shopify_locale}}}`{% endraw %} |
| El país del cliente | {% raw %}`{{${country}}}`{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Variables de Liquid del perfil de usuario de Markets"}

#### Desde eventos de pedido {#from-order-events}

| Propiedad del evento | Liquid |
| --- | --- |
| El país del pedido | {% raw %}`{{event_properties.${country}}}`{% endraw %} |
| El mercado del pedido | {% raw %}`{{event_properties.${market_handle}}}`{% endraw %} |
| La moneda en la que pagó el cliente | {% raw %}`{{event_properties.${metadata}.presentment_currency.code}}`{% endraw %} |
| El total del pedido en esa moneda | {% raw %}`{{event_properties.${metadata}.presentment_currency.<total_value>}}`{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Variables de Liquid de eventos de pedido de Markets"}

#### Mostrar precios en la moneda del cliente {#show-prices-in-the-customers-currency}

Siempre asocia un monto con su código de moneda. Un monto mostrado sin contexto es el error más común en la mensajería multimercado, porque "129.95" significa algo diferente en cada mercado.

Usa el total del pedido para mensajes a nivel de pedido, como una confirmación, y el precio del producto para contenido a nivel de producto, como un carrito o una recomendación.

{% raw %}
```liquid
Thanks for your order! Your total: {{event_properties.${metadata}.presentment_currency.code}}
{{event_properties.${metadata}.presentment_currency.<total field>}}
```
{% endraw %}

Como estas propiedades viajan con el evento, el mensaje se mantiene preciso para el mercado de cada cliente sin configuración adicional.

#### Verificar valores vacíos {#check-for-empty-values}

Dos valores no siempre estarán presentes, y ambos se muestran incorrectamente cuando faltan.

`market_handle` está vacío cuando el país del cliente no coincide con un mercado configurado. Verifica antes de ramificar con base en él:

{% raw %}
```liquid
{% if event_properties.${market_handle} != blank %}
  ...
{% endif %}
```
{% endraw %}

`compare_at_price` devuelve `0` cuando no se resuelve un precio de comparación para ese mercado. Verifica si es `0` antes de mostrarlo o calcular un descuento, o el cliente verá un precio tachado de cero.

#### Mostrar información de producto localizada {#show-localized-product-information}

Los nombres de productos en los eventos están en el idioma predeterminado de tu tienda. Para mostrar títulos, descripciones o URL de productos traducidos, busca el producto en tu catálogo usando el ID de producto o variante del evento. Para ver un ejemplo, consulta [Tutorial: Mostrar productos y precios por mercado](#tutorial-show-products-and-prices-per-market).

### Desencadenar mensajes desde la actividad de pedidos {#trigger-messages-from-order-activity}

Las propiedades de mercado se incluyen con los eventos compatibles de Shopify, por lo que una Campaign o un Canvas desencadenado por un pedido puede usarlas sin configuración adicional. Estos eventos incluyen `country`, `presentment_currency` y `market_handle`.

| Tipo de evento | Eventos |
| --- | --- |
| Eventos recomendados de eCommerce | `ecommerce.order_placed`, `ecommerce.order_cancelled`, `ecommerce.order_refunded` |
| Eventos personalizados | `shopify_paid_order`, `shopify_fulfilled_order`, `shopify_partially_fulfilled_order` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Eventos de pedido de Shopify Markets con propiedades de mercado"}

`presentment_currency` tiene la cobertura más amplia en comparación con los otros. Se incluye con los eventos compatibles de carrito, pago y pedido, por lo que un mensaje de carrito abandonado puede mostrar el monto que vio el cliente aunque los eventos de carrito no incluyan `country` ni `market_handle`. Para más detalles, consulta [Moneda](#currency).

## Informes de Markets {#markets-reporting}

Cuando Markets está habilitado, Braze desglosa los ingresos y el rendimiento de los mensajes por país.

### Ingresos por país {#revenue-by-country}

Tu informe de ingresos incluye un desglose por país junto con el desglose por aplicación, tanto para el tiempo de vida como para un intervalo de tiempo seleccionado.

Cada pedido se atribuye a un país, y sus ingresos completos se asignan a ese país. El país se selecciona primero del pedido y luego del perfil del comprador. Los pedidos en los que ninguno está disponible aparecen bajo **Desconocido**.

Los ingresos se muestran en USD, igual que el resto del informe de ingresos. Para ver lo que un comprador realmente pagó, usa `presentment_currency` en el evento del pedido.

### Rendimiento por país {#performance-by-country}

Los análisis de Campaign y Canvas incluyen una tabla de **Rendimiento por país** que muestra cómo se desempeñó un mensaje en cada país y una fila de total para cada país. La moneda y los ingresos totales se agregan a partir del `presentment_currency` del pedido.

| Columna | Qué muestra |
| --- | --- |
| País | Cada país al que llegó tu mensaje. |
| Moneda | La moneda para los ingresos de ese país, agregada por el `presentment_currency`. |
| Ingresos totales | Ingresos atribuidos a ese país. |
| Compras | Compras atribuidas a ese país. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Qué muestra cada columna de rendimiento por país"}

## Eliminar un mercado {#remove-a-market}

Eliminar un mercado impide que Braze sincronice nuevos datos para sus países. No elimina los datos que ya tienes.

### Grupos de suscripción {#subscription-groups}

Eliminar un mercado actualiza tu configuración de mercados. No elimina los grupos de suscripción de tu espacio de trabajo ni elimina a los usuarios que ya están suscritos a grupos de países.

#### Qué cambia en tu configuración {#what-changes-in-your-setup}

- Los países del mercado eliminado ya no aparecen en la interfaz de mercados.
- Braze elimina las asignaciones de grupos de suscripción de esos países de tu configuración de integración.

#### Qué permanece igual {#what-stays-the-same}

- Los grupos de suscripción de países permanecen en tu espacio de trabajo y siguen disponibles para la segmentación, pero Shopify ya no sincroniza las cancelaciones de suscripción con ellos. Los usuarios que cancelen su suscripción en Shopify pueden seguir apareciendo como suscritos en esos grupos de países a menos que actualices su estado de suscripción de otra manera, por ejemplo, a través de los [endpoints de grupos de suscripción]({{site.baseurl}}/api/endpoints/subscription_groups) o un flujo de trabajo de cancelación de suscripción en Braze.
- Los usuarios que ya están suscritos a los grupos de países de un mercado eliminado permanecen suscritos.

#### Sincronización de consentimiento futura {#future-consent-sync}

- Las nuevas adhesiones voluntarias de compradores en países eliminados se sincronizan solo con tus grupos de toda la tienda, de la misma manera que las [adhesiones voluntarias de países que no has configurado](#opt-ins-from-countries-you-havent-configured).
- Braze ya no sincroniza nuevas adhesiones voluntarias ni cancelaciones de suscripción con los grupos de países de los países eliminados.
- Los grupos de suscripción de toda la tienda continúan recibiendo actualizaciones de consentimiento.

### Datos de usuario {#user-data}

- Los atributos que ya están en el perfil de un usuario, incluidos `shopify_locale` y `country`, no cambian.
- El `market_handle` dentro de nuevos eventos de pedido ya no está disponible.
- Los filtros de Segment de Shopify Market para mercados eliminados ya no están disponibles.
- Las referencias de Liquid a un mercado eliminado ya no están disponibles.

### Catálogos {#catalogs}

- Las filas de mercado para ese mercado dejan de actualizarse y se eliminan de tu catálogo.
- Las selecciones de catálogo creadas a partir de esas filas de mercado dejan de devolver productos. Actualízalas o elimínalas antes de tu próximo envío.
- Tus filas predeterminadas, y cualquier selección creada a partir de ellas, no se ven afectadas.

## Tutorial: Mostrar productos y precios por mercado {#tutorial-show-products-and-prices-per-market}

Usa un catálogo con reconocimiento de mercados para crear un único mensaje que muestre a cada usuario los productos y precios de su propio mercado.

1. Crea una selección que utilice datos de mercados.
2. Haz referencia a la selección en un mensaje con Liquid.

Puedes usar un mercado fijo cuando un mensaje se dirige a un mercado específico.

### Paso 1: Crear una selección usando datos de mercados {#step-1-create-a-selection-using-markets-data}

Las [selecciones]({{site.baseurl}}/catalog_selections) son conjuntos de productos seleccionados a los que haces referencia en los mensajes. Para catálogos de Shopify con mercados sincronizados, la sección **Configuración de filtros** incluye un área de **Alcance de mercado** que delimita los datos de productos a un mercado o los personaliza por usuario.

1. Ve a tu catálogo de Shopify y abre la pestaña **Selecciones**.
2. Selecciona **Crear selección**, luego nombra la selección, agrega una descripción opcional y establece un límite de resultados.
3. En **Configuración de filtros**, en **Alcance de mercado**, selecciona cómo la selección resuelve productos específicos del mercado en el menú desplegable **Mercado**:
   - **Personalizado:** Cada destinatario ve productos y precios del mercado que coincide con el atributo `country` de su perfil.
   - **Un mercado sincronizado:** Selecciona un mercado por nombre para fijar la selección a los productos y precios de ese mercado. Usa esto cuando un mensaje se dirige a un solo mercado.
4. Termina cualquier criterio de filtro adicional y luego guarda la selección.
5. En **Vista previa para usuario**, selecciona un usuario para ver qué devuelve la selección para ese perfil. Las selecciones que usan **Personalizado** solo pueden previsualizarse después de seleccionar un usuario.

| Objetivo | Filtro |
| --- | --- |
| Un mercado específico | `market_handle` = `au` |
| Solo productos predeterminados | `market_handle` = `default` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Objetivos y filtros asociados"}

{% alert note %}
Si no especificas un mercado, Braze usa tus productos predeterminados.
{% endalert %}

### Paso 2: Agregar selecciones de catálogo con reconocimiento de mercado a los mensajes {#step-2-add-market-aware-catalog-selections-to-messages}

Para servir a cada usuario los productos de su propio mercado en un único mensaje, crea una selección con este filtro:

| Nombre de selección | Campo | Operador | Valor |
| --- | --- | --- | --- |
| `market_products` | `market_handle` | igual a | {% raw %}`{{shopify_market.handle}}`{% endraw %} |
| `default_products` | `market_handle` | igual a | `default` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Nombre de selección y filtros asociados"}

En el momento del envío, Braze sustituye {% raw %}`{{shopify_market.handle}}`{% endraw %} por el mercado de cada usuario, de modo que `market_products` le da a todos los productos correctos. `default_products` es la alternativa para usuarios sin un mercado coincidente.

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
- Sustituye `<your_catalog_name>` por tu catálogo y usa tus propios nombres de selección si difieren.
- La comprobación de {% raw %}`{{shopify_market.handle}}`{% endraw %} redirige a los usuarios sin un mercado coincidente a `default_products`, de modo que sigan recibiendo productos en lugar de un mensaje vacío.
- Cuando uses `compare_at_price` en Liquid, verifica si el valor es "0" antes de mostrarlo o calcular un descuento. Un mercado sin precio de comparación muestra un precio de cero o produce un descuento incorrecto.

Previsualiza como un usuario en tu mercado para confirmar que el mensaje muestra los productos, precios y títulos traducidos de ese mercado.