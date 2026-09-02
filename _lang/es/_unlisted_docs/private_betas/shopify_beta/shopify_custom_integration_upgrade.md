---
nav_title: Actualizar Shopify (personalizado)
article_title: "Actualizar tu integración personalizada de Shopify"
description: "Aprende a actualizar tu integración personalizada de Shopify para Braze."
page_type: partner
search_tag: Partner
permalink: "/shopify_custom_upgrade/"
hidden: true
---

# Actualizar tu integración de Shopify (personalizada) {#upgrading-your-shopify-integration-custom}

> Aprende a actualizar tu integración de Shopify utilizando la ruta personalizada para Braze. Como parte de nuestro compromiso de ofrecerte la mejor experiencia posible, estamos requiriendo que todas las integraciones de Shopify se [actualicen]({{site.baseurl}}/shopify) a la última versión antes del 28 de agosto de 2025. Esta actualización es esencial porque cambios significativos en la tecnología de Shopify afectarán el funcionamiento de nuestra integración.

## ¿Quién es elegible? {#whos-eligible}

Esta ruta de actualización está pensada para marcas con una tienda headless de Shopify o una tienda Shopify Hydrogen.

{% multi_lang_include partners/shopify_alerts.md alert='breaking' %}

## Requisitos de actualización {#upgrade-requirements}

Antes de comenzar, revisa lo siguiente:

| Requisito             | Descripción |
|-----------------------|-------------|
| **Cambios críticos**  | Asegúrate de haber revisado todos los cambios importantes del conector legacy al nuevo conector en [Resumen de actualización de Shopify]({{site.baseurl}}/shopify_upgrade_overview#subscriber-collection). |
| **Prerrequisitos de actualización** | Asegúrate de haber completado todos los [prerrequisitos de actualización]({{site.baseurl}}/shopify_upgrade_overview#upgrade-prerequisites) necesarios con tus equipos de ingeniería y marketing. Para actualizar tu tienda headless de Shopify con Braze, necesitas completar dos pasos fundamentales:<br><br>- Inicializar y cargar el SDK Web de Braze para habilitar el seguimiento en el sitio<br>- Actualizar tu tienda existente a través de la experiencia de actualización dentro del producto |
| **Cambios incompatibles**  | Revisa y corrige todos los cambios incompatibles señalados en Braze. Para una guía completa, continúa a [Corrección de cambios incompatibles](#fixing-breaking-changes-fixing-breaking-changes). |
{: .reset-td-br-1 .reset-td-br-2  role="presentation"}

## Corregir cambios con ruptura {#fixing-breaking-changes}

En Braze, ve a **Integraciones de socios** > **Shopify** y selecciona **Iniciar actualización**.

![Panel con una opción para iniciar la actualización.]({% image_buster /assets/unlisted_docs/img/shopify/start_shopify_custom_upgrade.png %}){: style="max-width:35%;"}

Se señalarán todos los Canvas, Campaigns y Segments afectados que utilicen datos de Shopify.

![Un modal para revisar lo que se ve afectado por los cambios con ruptura.]({% image_buster /assets/unlisted_docs/img/shopify/review_breaking_changes.png %})

Para la mayoría de los eventos, recomendamos incluir los nuevos eventos y atributos de Shopify requeridos utilizando un operador "OR" para facilitar una actualización fluida de los mensajes activos. Para casos más específicos, consulta lo siguiente:

{% tabs local %}
{% tab Carrito abandonado %}
Para la mensajería de carrito abandonado, necesitarás usar las nuevas plantillas de Canvas de carrito abandonado que incluyen:

{% multi_lang_include partners/shopify/abandoned_cart_template_features.md %}
{% endtab %}

{% tab Pago abandonado %}
Para la mensajería de pago abandonado, necesitarás usar la nueva plantilla de Canvas de pago abandonado que incluye:

{% multi_lang_include partners/shopify/abandoned_checkout_template_features.md %}

Para una lista completa de las nuevas plantillas de Canvas de comercio electrónico y bloques HTML predefinidos para la personalización de productos disponibles a través de la integración, consulta [Crear los recorridos de usuario en Canvas]({{site.baseurl}}using_shopify_with_braze#create-your-canvas-user-journeys).

{% alert important %}
Si no tienes en cuenta los mensajes activos que utilizan eventos descontinuados en la integración de Shopify, los mensajes afectados ya no se enviarán a tus clientes.
{% endalert %}

Para obtener más información, revisa [Eventos de Shopify compatibles]({{site.baseurl}}/shopify_upgrade_overview#supported-shopify-events).
{% endtab %}

{% tab Listas de suscriptores %}
Si estás recopilando suscriptores de correo electrónico o SMS desde Shopify a través de la integración, confirma que tus mensajes activos incluyan las listas de suscriptores correspondientes para tu tienda Shopify.

Cuando la actualización esté completa, se crearán nuevos grupos de suscripción predeterminados para tu integración, los cuales necesitarás aprovechar como parte de tu mensajería activa. Para más información sobre los cambios, consulta [Recopilación de suscriptores]({{site.baseurl}}/shopify_upgrade_overview#subscriber-collection).
{% endtab %}
{% endtabs %}

## Actualización de Shopify {#upgrading-shopify}

{% alert important %}
Es esencial que [corrijas todos los cambios importantes](#fixing-breaking-changes) antes de iniciar la actualización.
{% endalert %}

### Paso 1: Inicializar y cargar el SDK Web de Braze para habilitar el seguimiento en el sitio {#step-1}

Si aún no lo has hecho, inicializa y carga el SDK Web de Braze para habilitar el seguimiento en el sitio. Para una guía completa, consulta [Configuración de integración personalizada de Shopify]({{site.baseurl}}/partners/ecommerce/shopify/shopify_custom_integration#step-1):
- Crear una aplicación web de Braze
- Añadir subdominio y variables de entorno
- Habilitar el seguimiento en el sitio
- Añadir un evento de inicio de sesión de cuenta de Shopify
- Añadir seguimiento para eventos de producto visto y actualización de carrito

### Paso 2: Iniciar la actualización {#step-2-start-the-upgrade}

En Braze, ve a **Partner Integrations** > **Shopify** y selecciona **Start upgrade**.

![Panel con una opción para iniciar la actualización.]({% image_buster /assets/unlisted_docs/img/shopify/start_shopify_custom_upgrade.png %}){: style="max-width:35%;"}

Acepta las directrices de actualización marcando la casilla y selecciona **Start the upgrade**.

![Modal para confirmar que comprendes que la actualización puede causar cambios importantes.]({% image_buster /assets/unlisted_docs/img/shopify/confirm_upgrade.png %}){: style="max-width:50%;"}

Verifica con tus desarrolladores que has completado el Paso 1 de la actualización de la ruta personalizada marcando la casilla y selecciona **Confirm**.

![Modal con una casilla para verificar que completaste los pasos del uno al cinco.]({% image_buster /assets/unlisted_docs/img/shopify/confirm_completed_steps.png %}){: style="max-width:50%;"}

{% alert important %}
Para que la integración funcione correctamente, asegúrate de completar el [Paso 1](#step-1) de la actualización personalizada. Si omites este paso, es posible que la integración no funcione correctamente.
{% endalert %}

### Paso 3: Reautorizar la aplicación de Braze {#step-3-reauthorize-the-braze-app}

Para reautorizar la aplicación de Braze, selecciona **Go to Shopify**.

![Panel con una opción para ir a Shopify.]({% image_buster /assets/unlisted_docs/img/shopify/custom_go_to_shopify.png %}){: style="max-width:35%"}

En el sitio de Shopify, sigue las indicaciones para reautorizar tu aplicación de Braze. Esto permite que Braze acceda a tus datos de Shopify.

{% alert important %}
El proceso de reautorización puede tardar unos minutos, pero se actualizará automáticamente en tu página de Shopify cuando se haya completado.
{% endalert %}

![Panel de actualización de Shopify con un icono giratorio junto a "Reauthorize the Braze app".]({% image_buster /assets/unlisted_docs/img/shopify/reauthorize_app_loading.png %}){: style="max-width:35%;"}

### Paso 4: Elegir un tipo de ID externo {#step-4-choose-an-external-id-type}

El tipo de ID externo que elijas se asignará a los nuevos perfiles de cliente de Shopify cuando se cree una cuenta de Shopify o se realice un pedido. También se usará para actualizar los perfiles de usuario existentes si ya tienen un alias de ID de cliente de Shopify pero no tienen un ID externo asignado en Braze.

Para elegir tu tipo de ID externo, vuelve a Braze y selecciona **Confirm external ID**.

![Panel de actualización de Shopify con un botón para confirmar el ID externo.]({% image_buster /assets/unlisted_docs/img/shopify/custom_confirm_external_id.png %}){: style="max-width:35%;"}

Elige el ID externo que te gustaría usar para la integración de Shopify de tu espacio de trabajo. Cuando hayas terminado, selecciona **Set external ID**.

![Modal con un menú desplegable para seleccionar el ID externo.]({% image_buster /assets/unlisted_docs/img/shopify/external_id_custom.png %}){: style="max-width:50%;"}

{% alert important %}
De forma predeterminada, Braze convierte automáticamente los correos electrónicos de Shopify a minúsculas antes de usarlos como ID externo. Si estás usando correo electrónico o correo electrónico con hash como tu ID externo, confirma que tus direcciones de correo electrónico también se conviertan a minúsculas antes de asignarlas como tu ID externo o antes de aplicarles hash desde otros orígenes de datos. Esto ayuda a prevenir discrepancias en los ID externos y evitar la creación de perfiles de usuario duplicados en Braze.
{% endalert %}

Si seleccionaste un tipo de ID externo personalizado, continúa con los pasos 4.1 a 4.3. De lo contrario, continúa con el paso 5.

#### Paso 4.1: Crear el metafield `braze.external_id` {#step-41-create-the-brazeexternal_id-metafield}

{% multi_lang_include partners/shopify/customer_metafield_definition_steps.md %}

Después de crear el metafield, llénalo para tus clientes. Recomendamos los siguientes enfoques:

- **Escuchar webhooks de creación de clientes:** Configura un webhook para escuchar los [eventos `customer/create`](https://help.shopify.com/en/manual/fulfillment/setup/notifications/webhooks). Esto te permite escribir el metafield cuando se crea un nuevo cliente.
- **Rellenar clientes existentes:** Usa la [Admin API](https://shopify.dev/docs/api/admin-graphql) o la [Customer API](https://shopify.dev/docs/api/admin-rest/2025-04/resources/customer) para rellenar el metafield de los clientes creados previamente.

#### Paso 4.2: Crear un endpoint para recuperar tu ID externo {#step-42-create-an-endpoint-to-retrieve-your-external-id}

Necesitas crear un endpoint público al que Braze pueda llamar para recuperar el ID externo. Esto es necesario para escenarios en los que Shopify no puede proporcionar el metafield `braze.external_id`.

##### Especificaciones del endpoint {#endpoint-specifications}

**Método:** `GET`

| Parámetros | Descripción |
| --- | --- |
| `shopify_customer_id` | El ID de cliente de Shopify. |
| `email_address` | La dirección de correo electrónico del usuario con sesión iniciada. |
| `shopify_storefront` | La tienda en línea para la solicitud. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

##### Ejemplo de endpoint {#example-endpoint}

```
GET
https://mystore.com/custom_id?shopify_customer_id=1234&email_address=bob@example.com&shopify_storefront=dev-store.myshopify.com
```

##### Respuesta esperada {#expected-response}

Braze espera un código de estado `200`. Cualquier otro código se considera un fallo.

{% raw %}
```json
{ "external_id": "my_external_id" }
```
{% endraw %}

{% alert important %}
Es importante validar que el `shopify_customer_id` y el `email_address` coincidan con los valores del cliente en Shopify. Puedes usar la [Admin API](https://shopify.dev/docs/api/admin-graphql) o la [Customer API](https://shopify.dev/docs/api/admin-rest/2025-04/resources/customer) para validar estos parámetros y recuperar el metafield `braze.external_id`.
{% endalert %}

#### Paso 4.3: Introducir tu ID externo {#step-43-input-your-external-id}

Repite el [Paso 4](#step-4-choose-an-external-id-type) e introduce la URL de tu endpoint después de seleccionar ID externo personalizado como tu tipo de ID externo de Braze.

##### Consideraciones {#considerations}

{% multi_lang_include partners/shopify/external_id_generation_notes.md %}

### Paso 5: Habilitar la inserción de la aplicación de Braze {#step-5-enable-the-braze-app-embed}

Para habilitar la inserción de la aplicación de Braze dentro del tema de tu tienda, vuelve a Braze y selecciona Go to Shopify.

![Panel de actualización de Shopify con un botón para habilitar la inserción de la aplicación de Braze.]({% image_buster /assets/unlisted_docs/img/shopify/custom_enable_app_embed.png %}){: style="max-width:35%;"}

En el sitio de Shopify, habilita la inserción de la aplicación de Braze y guarda tus cambios.

![Un ejemplo de inserción de aplicación.]({% image_buster /assets/unlisted_docs/img/shopify/app_embed.png %})

### Paso 6: Verificar la actualización {#step-6-verify-the-upgrade}

De vuelta en Braze, se te notificará cuando tu integración de Shopify haya terminado de instalarse.

![Página de integración de Shopify con un banner de éxito.]({% image_buster /assets/unlisted_docs/img/shopify/success_integration.png %})

Para verificar que tu nuevo conector de Shopify está en vivo, prueba lo siguiente:

{% multi_lang_include partners/shopify/upgrade_validation_checklist.md %}

Si tienes alguna pregunta, [contacta con soporte]({{site.baseurl}}/user_guide/administer/personal/braze_support).