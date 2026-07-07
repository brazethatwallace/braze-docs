---
nav_title: Conectar varias tiendas
article_title: Soporte para múltiples tiendas en Shopify
alias: /shopify_connecting_multiple_stores/
page_order: 6
description: "Este artículo de referencia explica cómo conectar y configurar varias tiendas Shopify en un único espacio de trabajo."
---

# Conecta varias tiendas Shopify {#connect-multiple-shopify-stores}

> Conecta varios dominios de tiendas Shopify a un único espacio de trabajo para tener una visión holística de tus clientes en todos los mercados. Construye y lanza programas de automatización y recorridos en un único espacio de trabajo sin duplicar esfuerzos en las tiendas regionales.

{% alert important %}
Esta característica no es compatible con Shopify Markets ni Markets Pro. Si deseas solicitar soporte para estos, envía una [solicitud de producto]({{site.baseurl}}/user_guide/administer/personal/product_portal).
{% endalert %}

## Requisitos {#requirements}

| Requisito | Descripción |
| ----------- | ----------- |
| Configurar una tienda Shopify | Asegúrate de que ya has [configurado al menos una tienda de Shopify con Braze]({{site.baseurl}}/shopify_overview). |
| Dominios de tienda Shopify únicos para cada región | El soporte para múltiples tiendas está pensado para usarse con dominios de tienda Shopify únicos para diferentes escaparates regionales. <br><br>Si quieres conectar varias submarcas a Braze, te recomendamos crear espacios de trabajo separados para cada submarca. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos" }

## Conectar una tienda adicional {#connecting-an-additional-store}
Después de instalar la aplicación Braze en tu tienda Shopify e instalar tu primera tienda, selecciona **+ Connect New Store**.

![El botón "+ Connect New Store" en la página de integración de Shopify.]({% image_buster /assets/img/shopify/begin_setup_button.png %}){: style="max-width:80%;"}

Para tu tienda regional adicional de Shopify, selecciona **Begin setup**.

![La sección "Integration settings" con un botón para "Begin setup".]({% image_buster /assets/img/shopify/multiple_stores.png %}){: style="max-width:80%;"}

Como en la primera integración de tu tienda Shopify, puedes elegir entre una configuración estándar o personalizada.

![Sección "Enable the Braze SDKs" con opciones para implementar el SDK Web de Braze con la configuración estándar o personalizada.]({% image_buster /assets/img/shopify/standard_or_custom.png %}){: style="max-width:80%;"}

Elige la opción que mejor se adapte a tus necesidades:

{% multi_lang_include partners/shopify.md section='Integration Tabs' %}

Para ver la integración de cada tienda y configurar los ajustes avanzados, selecciona una tienda en el menú desplegable.

!["Integration settings" con un menú desplegable para seleccionar una tienda Shopify.]({% image_buster /assets/img/shopify/store_dropdown_menu.png %})

## Sincronización de usuarios entre tiendas {#syncing-users-across-stores}

### Alias de Shopify {#shopify-alias}

Cuando conectes varias tiendas, los usuarios de Shopify sincronizados que hayan iniciado sesión o realizado un pedido recibirán un nuevo alias con el formato: {% raw %}`shopify_customer_id_{{storename}}`{% endraw %}.

### ID externo de Braze {#braze-external-id}

Puedes elegir entre las siguientes opciones para tu ID externo de Braze:

| Opción | Descripción |
|------|-----------|
| ID de cliente de Shopify | Si utilizas el ID de cliente de Shopify como tu ID externo de Braze, cada tienda generará un ID de cliente único para cada usuario. Esto significa que si un usuario interactúa con varias tiendas, tendrá perfiles separados en Braze. |
| Correo electrónico, correo electrónico con hash o ID externo personalizado | Si utilizas los tipos de correo electrónico, correo electrónico con hash o ID externo personalizado, los perfiles de los usuarios que interactúan con varias tiendas se fusionarán en un único perfil consolidado cuando inicien sesión o realicen un pedido. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ID externo de Braze" }

### Campos fusionados {#merged-fields}

Cuando se sincroniza un perfil de usuario, se fusionan los siguientes campos. Para obtener todos los detalles sobre el comportamiento de fusión, consulta [Comportamiento de fusión]({{site.baseurl}}/api/endpoints/user_data/post_users_merge#merge-behavior).

- Información del dispositivo
- Recuento total de sesiones (combinado de ambos perfiles)
- Datos de eventos personalizados y compras
- Propiedades de eventos personalizados para la segmentación (por ejemplo, "X veces en Y días" donde X ≤ 50 e Y ≤ 30)
- Recuento de eventos (combinado de ambos perfiles)
- Fechas de los primeros y últimos eventos (Braze selecciona las fechas más antigua y más reciente)
- Datos de interacción de Campaign (campos de fecha más recientes)
- Resúmenes del flujo de trabajo (campos de fecha más recientes)
- Historial de mensajes e interacciones
- Grupos de suscripción

### Recopilar suscriptores (opcional) {#collecting-subscribers-optional}

Puedes elegir recopilar suscriptores directamente a través de Braze (en la configuración de tu conector de Shopify) o a través de alternativas de API y SDK que sincronizan los datos desde Shopify.

{% tabs local %}
{% tab Shopify connector %}
En el paso **Manage users** de la configuración de tu conector de Shopify, puedes utilizar Braze para recopilar las adhesiones voluntarias de suscriptores por correo electrónico y SMS y organizarlas en un grupo de suscripción dedicado:

1. Crea un grupo de suscripción único para cada tienda que conectes. Esto te ayuda a mantener datos precisos sobre la procedencia de los suscriptores.
2. Habilita la recopilación de suscriptores por correo electrónico y SMS.
{% endtab %}

{% tab Braze API or SDKs %}
Alternativamente, puedes sincronizar la información de adhesión voluntaria al marketing por correo electrónico y SMS directamente desde Shopify utilizando la API o los SDK de Braze.

| Opción | Recursos |
|------|---------|
| API | - [Puntos finales de grupos de suscripción]({{site.baseurl}}/api/endpoints/subscription_groups) para sustituir directamente lo que admite la integración<br>- [Punto de conexión `Users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track#set-subscription-groups) para configurar los datos del grupo de suscripción o el [estado global de suscripción al correo electrónico]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions#subscription-states)<br>- [Centro de preferencias de Braze]({{site.baseurl}}/user_guide/channels/email/subscriptions) para más opciones personalizadas de recopilación de adhesiones voluntarias de marketing |
| SDK | - [`NotificationSubscriptionTypes`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#notificationsubscriptiontypes)<br>- [`addToSubscriptionGroup`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addtosubscriptiongroup)<br>- [`removeFromSubscriptionGroup`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#removefromsubscriptiongroup)<br>- [`setEmailNotificationSubscriptionType`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemailnotificationsubscriptiontype) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Recopilar suscriptores (opcional)" }
{% endtab %}
{% endtabs %}

## Datos de Shopify {#shopify-data}

### Atributos sincronizados {#synced-attributes}

Cuando conectes más de una tienda, los siguientes atributos se sincronizarán con el estado más reciente del perfil de Shopify:
- Nombre
- Apellido
- Correo electrónico
- Género
- Fecha de nacimiento
- País
- Ciudad
- Última aplicación usada
- Idioma
- Zona horaria
- Etiquetas de Shopify
- Recuento de pedidos de Shopify
- Total gastado en Shopify

### Eventos compatibles {#supported-events}

#### Eventos recomendados de comercio electrónico {#ecommerce-recommended-events}

Cuando conectas varias tiendas, los eventos recomendados de comercio electrónico entrantes incluirán una propiedad de evento de origen. Esta propiedad identifica la URL del escaparate del que se originó el evento, lo que te permite utilizar esta información para la segmentación o para desencadenar casos de uso específicos.

![Un Canvas basado en acciones con un desencadenante para que entren los usuarios que realizan el evento personalizado `ecommerce.order_placed`.]({% image_buster /assets/img/shopify/ecommerce_order_placed.png %}){: style="max-width:80%;"}

Los eventos recomendados de comercio electrónico compatibles con la integración de Shopify son:

- `ecommerce.product_viewed`
- `ecommerce.cart_updated`
- `ecommerce.checkout_started`
- `ecommerce.order_placed`
- `ecommerce.order_cancelled`
- `ecommerce.order_refunded`

#### Eventos personalizados de Shopify {#shopify-custom-events}

Los eventos personalizados entrantes de Shopify incluyen una propiedad de evento llamada `shopify_storefront`. Esta propiedad indica de qué URL del escaparate procede el evento, lo que te permite aprovecharla para la segmentación o para desencadenar casos de uso.

![Un Canvas basado en acciones con un desencadenante para que entren los usuarios que realizan el evento personalizado `shopify_paid_order`.]({% image_buster /assets/img/shopify/shopify_paid_order.png %}){: style="max-width:80%;"}

Los eventos personalizados de Shopify compatibles incluyen:

- `shopify_fulfilled_order`
- `shopify_partially_fulfilled_order`
- `shopify_paid_order`
- `shopify_account_login`

Para obtener un resumen completo de todas las cargas útiles de eventos, consulta [Características de datos de Shopify]({{site.baseurl}}/shopify_data_features).

### Sincronización de productos de Shopify {#shopify-product-sync}

Cuando conectas y configuras cada tienda de Shopify en Braze, puedes habilitar opcionalmente la sincronización de productos de Shopify como parte de la integración.

Si activas la sincronización de productos para cada tienda, Braze incluye el nombre de tu tienda Shopify en el nombre del catálogo. Esto distingue los productos de diferentes tiendas.

![Catálogos de Shopify con el nombre de su tienda Shopify incluido en el nombre.]({% image_buster /assets/img/shopify/catalog_store_name.png %})