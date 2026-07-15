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

Esta ruta de actualización está destinada a marcas con una tienda Shopify headless o Shopify Hydrogen.

{% multi_lang_include partners/shopify_alerts.md alert='breaking' %}

## Requisitos de actualización {#upgrade-requirements}

Antes de comenzar, revisa lo siguiente:

| Requisito | Descripción |
|-----------------------|-------------|
| **Cambios críticos** | Asegúrate de haber revisado todos los cambios importantes del conector heredado al nuevo conector en [Resumen de la actualización de Shopify]({{site.baseurl}}/shopify_upgrade_overview#subscriber-collection). |
| **Requisitos previos de actualización** | Asegúrate de haber completado todos los [requisitos previos de actualización]({{site.baseurl}}/shopify_upgrade_overview#upgrade-prerequisites) necesarios con tus equipos de ingeniería y marketing. Para actualizar tu tienda Shopify headless con Braze, necesitas completar dos pasos críticos:<br><br>- Inicializar y cargar el SDK web de Braze para habilitar el seguimiento en el sitio<br>- Actualizar tu tienda existente a través de la experiencia de actualización dentro del producto |
| **Cambios con ruptura** | Revisa y corrige todos los cambios con ruptura señalados en Braze. Para un recorrido completo, continúa a [Corregir cambios con ruptura](#fixing-breaking-changes-fixing-breaking-changes). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Corregir cambios con ruptura {#fixing-breaking-changes}

En Braze, ve a **Integraciones de socios** > **Shopify** y selecciona **Iniciar actualización**.

![Panel con una opción para iniciar la actualización.]({% image_buster /assets/unlisted_docs/img/shopify/start_shopify_custom_upgrade.png %}){: style="max-width:35%;"}

Se señalarán todos los Canvas, Campaigns y Segments afectados que utilicen datos de Shopify.

![Un modal para revisar lo que se ve afectado por los cambios con ruptura.]({% image_buster /assets/unlisted_docs/img/shopify/review_breaking_changes.png %})

Para la mayoría de los eventos, recomendamos incluir los nuevos eventos y atributos de Shopify requeridos utilizando un operador "OR" para facilitar una actualización fluida de los mensajes activos. Para casos más específicos, consulta lo siguiente:

{% tabs local %}
{% tab Carrito abandonado %}
Para la mensajería de carrito abandonado, necesitarás usar las nuevas plantillas de Canvas de carrito abandonado que incluyen:

- Un nuevo desencadenador basado en la acción "Performed cart updated"
- Criterios de salida predefinidos para eliminar a los clientes que han avanzado en su proceso de compra
- Una nueva etiqueta de Liquid de carrito de compras para soportar la personalización de productos
{% endtab %}

{% tab Pago abandonado %}
Para la mensajería de pago abandonado, necesitarás usar la nueva plantilla de Canvas de pago abandonado que incluye:

- El evento ecommerce.checkout_started predefinido en tus criterios de entrada
- Criterios de salida predefinidos para eliminar a los clientes que han avanzado en su proceso de compra
- Una nueva etiqueta de Liquid de carrito de compras para soportar la personalización de productos

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

## Actualizar Shopify {#upgrading-shopify}

{% alert important %}
Es esencial que [corrijas todos los cambios con ruptura](#fixing-breaking-changes) antes de iniciar tu actualización.
{% endalert %}

### Paso 1: Inicializar y cargar el SDK web de Braze para habilitar el seguimiento en el sitio {#step-1}

Si aún no lo has hecho, inicializa y carga el SDK web de Braze para habilitar el seguimiento en el sitio. Para un recorrido completo, consulta [Configuración de la integración personalizada de Shopify]({{site.baseurl}}/partners/ecommerce/shopify/shopify_custom_integration#step-1):
- Crear una aplicación web de Braze
- Agregar subdominio y variables de entorno
- Habilitar el seguimiento en el sitio
- Agregar un evento de inicio de sesión de cuenta de Shopify
- Agregar seguimiento para eventos de producto visto y actualización de carrito

### Paso 2: Iniciar la actualización {#step-2-start-the-upgrade}

En Braze, ve a **Integraciones de socios** > **Shopify** y selecciona **Iniciar actualización**.

![Panel con una opción para iniciar la actualización.]({% image_buster /assets/unlisted_docs/img/shopify/start_shopify_custom_upgrade.png %}){: style="max-width:35%;"}

Acepta las directrices de actualización marcando la casilla y selecciona **Iniciar la actualización**.

![Modal para confirmar que entiendes que la actualización puede causar cambios con ruptura.]({% image_buster /assets/unlisted_docs/img/shopify/confirm_upgrade.png %}){: style="max-width:50%;"}

Verifica con tus desarrolladores que has completado el paso 1 de la ruta de actualización personalizada marcando la casilla y selecciona **Confirmar**.

![Modal con una casilla para verificar que completaste los pasos del uno al cinco.]({% image_buster /assets/unlisted_docs/img/shopify/confirm_completed_steps.png %}){: style="max-width:50%;"}

{% alert important %}
Para que la integración funcione correctamente, asegúrate de completar el [Paso 1](#step-1) de la actualización personalizada. Si omites este paso, la integración podría no funcionar correctamente.
{% endalert %}

### Paso 3: Reautorizar la aplicación de Braze {#step-3-reauthorize-the-braze-app}

Para reautorizar la aplicación de Braze, selecciona **Ir a Shopify**.

![Panel con una opción para ir a Shopify.]({% image_buster /assets/unlisted_docs/img/shopify/custom_go_to_shopify.png %}){: style="max-width:35%"}

En el sitio de Shopify, sigue las indicaciones para reautorizar tu aplicación de Braze. Esto permite que Braze acceda a tus datos de Shopify.

{% alert important %}
El proceso de reautorización puede tardar unos minutos, pero se actualizará automáticamente en tu página de Shopify cuando se complete.
{% endalert %}

![Panel de actualización de Shopify con un icono giratorio junto a "Reautorizar la aplicación de Braze".]({% image_buster /assets/unlisted_docs/img/shopify/reauthorize_app_loading.png %}){: style="max-width:35%;"}

### Paso 4: Elegir un tipo de ID externo {#step-4-choose-an-external-id-type}

El tipo de ID externo que elijas se asignará a los nuevos perfiles de clientes de Shopify cuando se cree una cuenta de Shopify o se realice un pedido. También se utilizará para actualizar los perfiles de usuario existentes si ya tienen un alias de ID de cliente de Shopify pero no tienen asignado un ID externo en Braze.

Para elegir tu tipo de ID externo, regresa a Braze y selecciona **Confirmar ID externo**.

![Panel de actualización de Shopify con un botón para confirmar el ID externo.]({% image_buster /assets/unlisted_docs/img/shopify/custom_confirm_external_id.png %}){: style="max-width:35%;"}

Elige el ID externo que deseas usar para la integración de Shopify de tu espacio de trabajo. Cuando termines, selecciona **Establecer ID externo**.

![Modal con un menú desplegable para seleccionar el ID externo.]({% image_buster /assets/unlisted_docs/img/shopify/external_id_custom.png %}){: style="max-width:50%;"}

{% alert important %}
De forma predeterminada, Braze convierte automáticamente los correos electrónicos de Shopify a minúsculas antes de usarlos como ID externo. Si estás usando correo electrónico o correo electrónico con hash como tu ID externo, confirma que tus direcciones de correo electrónico también se conviertan a minúsculas antes de asignarlas como tu ID externo o antes de aplicarles hash desde otros orígenes de datos. Esto ayuda a prevenir discrepancias en los ID externos y evitar la creación de perfiles de usuario duplicados en Braze.
{% endalert %}

Si seleccionaste un tipo de ID externo personalizado, continúa con los pasos 4.1 a 4.3. De lo contrario, continúa con el paso 5.

#### Paso 4.1: Crear el metacampo `braze.external_id` {#step-41-create-the-brazeexternal_id-metafield}

1. En tu panel de administración de Shopify, ve a **Configuración** > **Metacampos**.
2. Selecciona **Clientes** > **Agregar definición**.
3. En **Espacio de nombres y clave**, ingresa `braze.external_id`.
4. En **Tipo**, selecciona **Tipo de ID**.

Después de crear el metacampo, rellénalo para tus clientes. Recomendamos los siguientes enfoques:

- **Escuchar webhooks de creación de clientes:** Configura un webhook para escuchar [eventos `customer/create`](https://help.shopify.com/en/manual/fulfillment/setup/notifications/webhooks). Esto te permite escribir el metacampo cuando se crea un nuevo cliente.
- **Rellenar clientes existentes:** Usa la [API de administración](https://shopify.dev/docs/api/admin-graphql) o la [API de clientes](https://shopify.dev/docs/api/admin-rest/2025-04/resources/customer) para rellenar el metacampo de los clientes creados anteriormente.

#### Paso 4.2: Crear un punto de conexión para recuperar tu ID externo {#step-42-create-an-endpoint-to-retrieve-your-external-id}

Necesitas crear un punto de conexión público al que Braze pueda llamar para recuperar el ID externo. Esto es necesario para escenarios en los que Shopify no puede proporcionar el metacampo `braze.external_id`.

##### Especificaciones del punto de conexión {#endpoint-specifications}

**Método:** `GET`

| Parámetros | Descripción |
| --- | --- |
| `shopify_customer_id` | El ID de cliente de Shopify. |
| `email_address` | La dirección de correo electrónico del usuario que inició sesión. |
| `shopify_storefront` | La tienda para la solicitud. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

##### Ejemplo de punto de conexión {#example-endpoint}

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
Es importante validar que `shopify_customer_id` y `email_address` coincidan con los valores del cliente en Shopify. Puedes usar la [API de administración](https://shopify.dev/docs/api/admin-graphql) o la [API de clientes](https://shopify.dev/docs/api/admin-rest/2025-04/resources/customer) para validar estos parámetros y recuperar el metacampo `braze.external_id`.
{% endalert %}

#### Paso 4.3: Ingresar tu ID externo {#step-43-input-your-external-id}

Repite el [Paso 4](#step-4-choose-an-external-id-type) e ingresa la URL de tu punto de conexión después de seleccionar ID externo personalizado como tu tipo de ID externo de Braze.

##### Consideraciones {#considerations}

- Si tu ID externo no se genera cuando Braze envía una solicitud a tu punto de conexión, la integración usará de forma predeterminada el ID de cliente de Shopify cuando se llame a la función `changeUser`. Este paso es crucial para fusionar el perfil de usuario anónimo con el perfil de usuario identificado. Como resultado, puede haber un período temporal durante el cual existan diferentes tipos de ID externos dentro de tu espacio de trabajo.
- Cuando el ID externo esté disponible en el metacampo `braze.external_id`, la integración priorizará y asignará este ID externo.
    - Si el ID de cliente de Shopify se estableció previamente como el ID externo de Braze, se reemplazará con el valor del metacampo `braze.external_id`.

### Paso 5: Habilitar la inserción de la aplicación de Braze {#step-5-enable-the-braze-app-embed}

Para habilitar la inserción de la aplicación de Braze dentro del tema de tu tienda, regresa a Braze y selecciona **Ir a Shopify**.

![Panel de actualización de Shopify con un botón para habilitar la inserción de la aplicación de Braze.]({% image_buster /assets/unlisted_docs/img/shopify/custom_enable_app_embed.png %}){: style="max-width:35%;"}

En el sitio de Shopify, habilita la inserción de la aplicación de Braze y guarda tus cambios.

![Un ejemplo de inserción de aplicación.]({% image_buster /assets/unlisted_docs/img/shopify/app_embed.png %})

### Paso 6: Verificar la actualización {#step-6-verify-the-upgrade}

De vuelta en Braze, se te notificará cuando tu integración de Shopify haya terminado de instalarse.

![Página de integración de Shopify con un banner de éxito.]({% image_buster /assets/unlisted_docs/img/shopify/success_integration.png %})

Para verificar que tu nuevo conector de Shopify esté en vivo, prueba lo siguiente:

- **Canvas, Campaigns y Segments activos:** Confirma que estén funcionando correctamente.
- **Procesos de gestión de identidad:** Confirma que estos procesos estén funcionando como se espera.
- **Personalizaciones del SDK (opcional):** Si realizaste personalizaciones en tu integración de Braze y Shopify (como registrar eventos personalizados o atributos), verifica que estén funcionando correctamente después de la actualización.
- **Recopilación de suscriptores de correo electrónico o SMS (opcional):** Si habilitaste previamente la recopilación de suscriptores de correo electrónico o SMS, se crearán nuevos grupos de suscripción predeterminados para reflejar el estado más reciente de tus suscriptores durante la actualización. Los grupos de suscripción predeterminados tendrán el nombre de tu tienda de Shopify. Estos nuevos grupos de suscripción predeterminados estarán disponibles aproximadamente 5 horas después de la actualización, y necesitarás agregarlos a tus mensajes activos.

Si tienes alguna pregunta, [ponte en contacto con Soporte]({{site.baseurl}}/user_guide/administrative/access_braze/support).