---
nav_title: Resumen de la actualización de Shopify
article_title: Resumen de la actualización de Shopify
description: "Este artículo de referencia describe cómo actualizar tu integración de Shopify a la última versión."
page_type: partner
search_tag: Partner
permalink: "/shopify_upgrade_overview/"
hidden: true
---

# Resumen de la actualización de Shopify {#shopify-upgrade-overview}

> Como parte de nuestro compromiso de ofrecerte la mejor experiencia posible, estamos requiriendo que todas las integraciones de Shopify se [actualicen]({{site.baseurl}}/shopify/) a la última versión antes del 28 de agosto de 2025. Esta actualización es esencial porque cambios significativos en la tecnología de Shopify afectarán el funcionamiento de nuestra integración.

## Fechas clave {#key-dates}

- **De finales de febrero a abril:** Recibirás notificaciones sobre cuándo tu grupo específico (cohorte) estará listo para la actualización. Mantente atento a esta información importante.
- **Fecha límite de actualización:** Todos los clientes deben completar la actualización antes del **28 de agosto de 2025**.

{% multi_lang_include shopify_alerts.md alert='breaking' %}

## ¿Qué cambia en la integración de Shopify? {#whats-changing-in-the-shopify-integration}

Como parte de los planes de Shopify para mejorar la extensibilidad del checkout, se avecinan cambios significativos en su integración con Braze. Esto es lo que necesitas saber:

- **Deprecación de Script Tags y `checkout.liquid`:** Shopify está eliminando gradualmente los Script Tags y `checkout.liquid`. Después de agosto de 2025, el SDK web de Braze ya no se cargará en las páginas de checkout a través de Script Tags a menos que migres a la última versión de la integración.
- **Mejoras generales en la integración:**
    - **Introducción de eventos recomendados:** Estamos añadiendo eventos de comercio electrónico recomendados a la integración, lo que simplifica los casos de uso comunes de comercio electrónico a través de plantillas prediseñadas en Braze.
    - **Gestión de identidades optimizada:** Estamos mejorando nuestro enfoque para gestionar las identidades de los usuarios, lo que mejorará el seguimiento y la atribución de datos de usuarios anónimos. Para más información sobre cómo se procesará la gestión de identidades, consulta [Sincronización de usuarios y datos](https://braze.com/docs/partners/ecommerce/shopify/shopify_overview/#user-and-data-syncing).
    - **Listas de suscriptores de correo electrónico y SMS:** Si actualmente estás recopilando suscriptores de correo electrónico y SMS, se crearán automáticamente grupos de suscripción predeterminados para cada canal como parte de la actualización. Cuando Braze sincronice las adhesiones voluntarias de correo electrónico y SMS, Braze ya no sobrescribirá el estado de suscripción global en el perfil de usuario y solo actualizará la adhesión voluntaria del grupo de suscripción.
    - Para conocer todos los detalles sobre los cambios de la versión actual a la nueva versión, consulta el [registro de cambios](#full-changelog).

{% alert important %}
Esta actualización es esencial para mantener la funcionalidad de tu integración entre Shopify y Braze. Te recomendamos colaborar estrechamente con tu equipo de desarrollo para evaluar el alcance y las implicaciones de estos cambios y facilitar una transición fluida.
{% endalert %}

## Requisitos de actualización {#upgrade-requirements}

Antes de iniciar el proceso de actualización en la página de integración de Shopify, completa los siguientes requisitos con tu equipo de ingeniería:

- **Verifica las personalizaciones del SDK:** Si has personalizado tu integración de Braze y Shopify (por ejemplo, registrando eventos personalizados o atributos), asegúrate de que estas personalizaciones funcionen correctamente después de la actualización. Si has creado tus propios eventos de navegador para acciones como "producto visto" o "carrito actualizado", coordina con tus desarrolladores para eliminarlos antes de la actualización, ya que duplicarán la funcionalidad proporcionada por el nuevo conector.

{% alert important %}
Si tienes una tienda en línea de Shopify y tus desarrolladores implementaron los SDK de Braze directamente en tu sitio de Shopify, o a través de Google Tag Manager o una plataforma de datos de los clientes, debes planificar dejar de usarlos a medida que actualices al nuevo conector de Shopify.
{% endalert %}

- **Revisa la gestión de identidades:** Si estás usando un ID externo de Braze, trabaja con tu equipo de desarrollo para asegurarte de que sea compatible con la nueva integración. Si configuras el ID externo dentro de la experiencia de tu tienda Shopify, haz que tus desarrolladores lo ajusten para evitar conflictos con el [nuevo proceso de gestión de identidades](https://braze.com/docs/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify_overview/#user-and-data-syncing).
- **Prepara las Campaigns, Canvas y Segments afectados:** Durante el proceso de actualización guiada, puedes ver y exportar cualquier Campaign, Canvas y Segment que dependa de datos de Shopify. Te recomendamos añadir los nuevos eventos y atributos de Shopify requeridos usando un operador "OR" para facilitar una actualización fluida de tus mensajes activos.
- **Crea recorridos de usuario de carrito abandonado y checkout abandonado:** El recorrido de usuario de carrito abandonado ahora debe usar el desencadenante "Performed Cart Updated" como parte de los criterios de entrada en tu Canvas. Además, necesitas usar la nueva etiqueta de Liquid del carrito de compras tanto para los recorridos de usuario de carrito abandonado como de checkout abandonado. Puedes usar nuestras nuevas [plantillas de Canvas]({{site.baseurl}}/using_shopify_with_braze/#create-your-canvas-user-journeys) para ayudarte a comenzar.

Completar estos pasos te ayudará a facilitar una actualización exitosa a la última versión de la integración de Shopify.

## Opciones de integración {#integration-options}

Braze ofrece dos opciones de integración para comerciantes de Shopify diseñadas para satisfacer las diversas necesidades de los negocios de comercio electrónico: **integración estándar** e **integración personalizada**.

{% tabs local %}
{% tab Estándar %}
La integración estándar está diseñada para tiendas en línea de Shopify, proporcionando un proceso de configuración fluido y sencillo. Esta opción te permite conectar rápidamente tu tienda Shopify a Braze, permitiéndote aprovechar potentes herramientas de interacción con los clientes sin necesidad de amplios conocimientos técnicos. Con esta opción de integración, puedes sincronizar datos de clientes, automatizar mensajes personalizados y mejorar tus esfuerzos de marketing a través de las funciones integrales de Braze.

Para actualizar tu integración de Shopify existente a través de la ruta de actualización estándar, consulta [Actualización de tu integración de Shopify (estándar)]({{site.baseurl}}/shopify_standard_upgrade/).
{% endtab %}

{% tab Personalizada %}
La integración personalizada ofrece una solución más flexible y componible si usas Shopify Hydrogen o tienes una tienda headless. Esta opción te permite implementar los SDK de Braze directamente en tu entorno de Shopify, habilitando una integración más profunda y funcionalidades a medida. Ya sea que busques crear experiencias de cliente únicas u optimizar flujos de trabajo específicos, la integración personalizada proporciona las herramientas necesarias para aprovechar al máximo las capacidades de Braze en una configuración headless.

Para actualizar tu integración de Shopify existente a través de la ruta de actualización personalizada, consulta [Actualización de tu integración de Shopify (personalizada)]({{site.baseurl}}/shopify_custom_upgrade/).
{% endtab %}
{% endtabs %}

## Registro de cambios {#changelog}

{% alert important %}
Esta integración utiliza Shopify como la fuente de verdad para los atributos y eventos compatibles. Como resultado, Shopify puede reemplazar valores preexistentes, como atributos estándar o personalizados, en un perfil de usuario cuando los datos se sincronizan.
{% endalert %}

### Integración estándar {#standard-integration}

| Versión anterior | Última versión |
| --- | --- |
| {::nomarkdown}<ul><li>Script Tag support</li><li>Braze Web SDK only</li><li>Shopify webhooks for events and products</li></ul>{:/} | {::nomarkdown}<ul><li>Web Pixel API support</li><li>New Braze app embed</li><li>Braze Web SDK & JavaScript SDK</li><li>Shopify webhooks for events and products</ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Integración estándar" }

### Identificadores de usuario compatibles con la integración {#user-identifiers-supported-by-the-integration}

| Identificadores de usuario | Versión anterior | Última versión |
| --- | --- | --- |
| ID de dispositivo de Braze |  {::nomarkdown}<ul><li>A randomly generated ID that is stored on the browser</li></ul>{:/} | {::nomarkdown} <ul><li>A randomly generated ID that is stored on the browser</li></ul>{:/}|
| Alias de Braze | {::nomarkdown}<ul><li>Shopify customer ID</li><li>Shopify email</li></ul>{:/} | {::nomarkdown}<ul><li>Shopify cart token</li><li>Shopify checkout token</li></ul>{:/}|
| ID externo de Braze | {::nomarkdown}<ul><li>N/A</li></ul>{:/}| {::nomarkdown}<ul><li>Shopify customer ID</li><li>Email</li><li>Hashed email (SHA-256, SHA-1, MD5)</li><li>Custom external ID</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Identificadores de usuario compatibles con la integración" }

Para más detalles sobre la sincronización de usuarios y la gestión de ID, consulta [Datos de usuario y sincronización](https://braze.com/docs/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify_overview/#user-and-data-syncing).

{% alert note %}
De forma predeterminada, Braze convierte automáticamente los correos electrónicos de Shopify a minúsculas antes de usarlos como ID externo. Si estás usando el correo electrónico o el correo electrónico con hash como tu ID externo, confirma que tus direcciones de correo electrónico también se conviertan a minúsculas antes de asignarlas como tu ID externo o antes de aplicarles hash desde otros orígenes de datos. Esto ayudará a prevenir discrepancias en los ID externos y evitará la creación de perfiles de usuario duplicados en Braze.
{% endalert %}

### Eventos de Shopify compatibles {#supported-shopify-events}

| Eventos o atributos | Versión anterior | Última versión |
| --- | --- | --- |
| Eventos |  {::nomarkdown}<ul><li><a href="https://www.braze.com/docs/partners/ecommerce/shopify_legacy/using_shopify/shopify_data_in_braze/?subtab=product%20viewed">shopify_product_viewed</a></li></ul>{:/} | {::nomarkdown}<ul><li>Replaced with <a href="https://www.braze.com/docs/partners/ecommerce/shopify/shopify_data_features/?subtab=product%20viewed">ecommerce.product_viewed</a></li><li>Added <a href="https://www.braze.com/docs/user_guide/engagement_tools/canvas/ideas_and_strategies/ecommerce_use_cases/#abandoned-browse">abandoned browse Canvas template</a></li></ul>{:/} |
| Eventos |  {::nomarkdown}<ul><li><a href="https://braze.com/docs/partners/ecommerce/shopify_legacy/using_shopify/shopify_data_in_braze/?tab=example%20payload">shopify_product_clicked</a></li></ul>{:/} | {::nomarkdown}<ul><li>Deprecated event</li></ul>{:/} |
| Eventos | {::nomarkdown}<ul><li><a href="https://braze.com/docs/partners/ecommerce/shopify_legacy/using_shopify/shopify_data_in_braze/?subtab=abandoned%20cart&tab=example%20payload">shopify_abandoned_cart</a></li><li><a href="https://www.braze.com/docs/partners/ecommerce/shopify_legacy/setting_up_shopify/#advanced-settings-optional">Abandoned cart timer setting</a></li></ul>{:/} | {::nomarkdown}<ul><li>Replaced with <a href="https://www.braze.com/docs/partners/ecommerce/shopify/shopify_data_features/?subtab=cart%20updated">ecommerce.cart_updated</a></li><li>Deprecated abandoned cart timer setting</li><li>Added <a href="https://www.braze.com/docs/user_guide/engagement_tools/canvas/ideas_and_strategies/ecommerce_use_cases/#abandoned-cart">abandoned cart Canvas template</a></li></ul>{:/} |
| Eventos | {::nomarkdown}<ul><li><a href="https://braze.com/docs/partners/ecommerce/shopify_legacy/using_shopify/shopify_data_in_braze/?subtab=abandoned%20checkout&tab=example%20payload">shopify_abandoned_checkout</a></li><li><a href="https://www.braze.com/docs/partners/ecommerce/shopify_legacy/setting_up_shopify/#advanced-settings-optional">Abandoned cart timer setting</a></li></ul>{:/}| {::nomarkdown}<ul><li>Replaced with <a href="https://www.braze.com/docs/partners/ecommerce/shopify/shopify_data_features/?subtab=checkout%20started">ecommerce.checkout_started</a></li><li>Deprecated abandoned checkout timer setting</li><li>Added <a href="https://www.braze.com/docs/user_guide/engagement_tools/canvas/ideas_and_strategies/ecommerce_use_cases/#abandoned-checkout">abandoned checkout Canvas template</a></li></ul>{:/}|
| Eventos | {::nomarkdown}<ul><li><a href="https://braze.com/docs/partners/ecommerce/shopify_legacy/using_shopify/shopify_data_in_braze/?subtab=created%20order&tab=example%20payload">shopify_created_order</a></li></ul>{:/} | {::nomarkdown}<ul><li>Replaced with <a href="https://www.braze.com/docs/partners/ecommerce/shopify/shopify_data_features/?subtab=order%20placed">ecommerce.order_placed</a></li><li>Added <a href="https://www.braze.com/docs/user_guide/engagement_tools/canvas/ideas_and_strategies/ecommerce_use_cases/#order-confirmation-and-feedback-survey">order confirmation & post-purchase survey Canvas template</a></li></ul>{:/}|
| Eventos | {::nomarkdown}<ul><li><a href="https://braze.com/unlisted_docs/using_shopify_with_braze/?tab=order%20confirmation">Braze purchase event</a></li></ul>{:/}| {::nomarkdown}<ul><li>Deprecated event. Use <a href="https://www.braze.com/docs/partners/ecommerce/shopify/shopify_data_features/?subtab=order%20placed">ecommerce.order_placed</a>.</li></ul>{:/}|
| Eventos | {::nomarkdown}<ul><li><a href="https://braze.com/docs/partners/ecommerce/shopify_legacy/using_shopify/shopify_data_in_braze/?subtab=paid%20order&tab=example%20payload">shopify_paid_order</a></li></ul>{:/}| {::nomarkdown}<ul><li>No changes</li></ul>{:/}|
| Eventos | {::nomarkdown}<ul><li><a href="https://braze.com/docs/partners/ecommerce/shopify_legacy/using_shopify/shopify_data_in_braze/?subtab=partially%20fulfilled%20order&tab=example%20payload">shopify_partially_fulfilled_order</a></li></ul>{:/}| {::nomarkdown}<ul><li>No changes</li></ul>{:/}|
| Eventos | {::nomarkdown}<ul><li><a href="https://braze.com/docs/partners/ecommerce/shopify_legacy/using_shopify/shopify_data_in_braze/?subtab=fulfilled%20order&tab=example%20payload">shopify_fulfilled_order</a></li></ul>{:/}| {::nomarkdown}<ul><li>No changes</li></ul>{:/}|
| Eventos | {::nomarkdown}<ul><li><a href="https://braze.com/docs/partners/ecommerce/shopify_legacy/using_shopify/shopify_data_in_braze/?subtab=cancelled%20order&tab=example%20payload">shopify_cancelled_order</a></li></ul>{:/}| {::nomarkdown}<ul><li>Replaced with <a href="https://www.braze.com/docs/partners/ecommerce/shopify/shopify_data_features/?subtab=order%20cancelled">ecommerce.order_cancelled</a></li></ul>{:/}|
| Eventos | {::nomarkdown}<ul><li><a href="https://braze.com/docs/partners/ecommerce/shopify_legacy/using_shopify/shopify_data_in_braze/?subtab=created%20refund&tab=example%20payload">shopify_created_refund</a></li></ul>{:/}| {::nomarkdown}<ul><li>Replaced with <a href="https://www.braze.com/docs/partners/ecommerce/shopify/shopify_data_features/?subtab=order%20refunded">ecommerce.order_refunded</a></li></ul>{:/}|
| Eventos| {::nomarkdown}<ul><li>No Shopify account login event</li></ul>{:/}| {::nomarkdown}<ul><li>Added <a href="https://www.braze.com/docs/partners/ecommerce/shopify/shopify_data_features/?subtab=account%20login#tracked-shopify-events">shopify_account_login</a></li></ul>{:/}|
| Atributos | {::nomarkdown}<ul><li>shopify_total_spent</li></ul>{:/}| {::nomarkdown}<ul><li>No changes</li></ul>{:/}|
| Atributos | {::nomarkdown}<ul><li>shopify_order_count</li></ul>{:/}| {::nomarkdown}<ul><li>No changes</li></ul>{:/}|
| Atributos | {::nomarkdown}<ul><li>shopify_last_order_id</li></ul>{:/}| {::nomarkdown}<ul><li>No changes</li></ul>{:/}|
| Atributos | {::nomarkdown}<ul><li>shopify_last_order_name</li></ul>{:/}| {::nomarkdown}<ul><li>No changes</li></ul>{:/}|
| Atributos | {::nomarkdown}<ul><li>shopify_zipcode</li></ul>{:/}| {::nomarkdown}<ul><li>No changes</li></ul>{:/}|
| Atributos | {::nomarkdown}<ul><li>shopify_province</li></ul>{:/}| {::nomarkdown}<ul><li>No changes</li></ul>{:/}|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Eventos de Shopify compatibles" }

### Recopilación de suscriptores {#subscriber-collection}

| Tipo de recopilación | Versión anterior | Última versión |
| --- | --- | --- |
| Recopilación de suscriptores de correo electrónico |  {::nomarkdown}<ul><li>Override for global email subscription state</li><li>Ability to assign one or more subscription groups</li><li>No default subscription group for the integration for the connected Shopify store</li></ul>{:/} | {::nomarkdown}<ul><li>Deprecated override functionality</li><li>A default subscription group will be created as part of the upgrade</li><li>Ability to assign additional subscription groups</li></ul>{:/} |
| Recopilación de suscriptores de SMS |  {::nomarkdown}<ul><li>Required to assign one or more subscription groups</li><li>No default subscription group for the integration for the connected Shopify store</li></ul>{:/} | {::nomarkdown}<ul><li>A default subscription group will be created as part of the upgrade</li><li>Ability to assign additional subscription groups</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Recopilación de suscriptores" }

{% alert note %}
Si actualmente estás recopilando suscriptores de correo electrónico o SMS, se creará un nuevo grupo de suscripción predeterminado después de que se complete la actualización. El grupo de suscripción predeterminado tendrá el nombre de tu tienda de Shopify. Este proceso puede tardar hasta 5 horas. <br><br>Una vez que los grupos de suscripción estén disponibles, asegúrate de incluirlos en tus Campaigns, Segments o Canvas activos para llegar eficazmente a tus compradores suscritos.
{% endalert %}

### Sincronización de productos {#product-sync}

| Tipo de sincronización | Versión anterior | Última versión |
| --- | --- | --- |
| Sincronización inicial de productos | {::nomarkdown}<ul><li>If product syncing is enabled, initial import of all products in your storefront</li><li>Ability to only import active products</li></ul>{:/} | {::nomarkdown}<ul><li>No&nbsp;changes</li></ul>{:/} |
| Sincronización de productos en tiempo real | {::nomarkdown}<ul><li>Real-time syncs when products are created, updated, or deleted from your store</li></ul>{:/} | {::nomarkdown}<ul><li>No&nbsp;changes</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Sincronización de productos" }

### Canales {#channels}

| Canal | Versión anterior | Última versión |
| --- | --- | --- |
| Mensajes dentro de la aplicación |  {::nomarkdown}<ul><li>Included within standard integrations for Shopify online stores</li></ul>{:/} | {::nomarkdown}<ul><li>No changes</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Canales" }