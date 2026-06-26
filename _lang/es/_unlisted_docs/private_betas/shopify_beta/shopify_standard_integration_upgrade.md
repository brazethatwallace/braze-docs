---
nav_title: Actualizar Shopify
article_title: "Actualizar tu integración de Shopify"
description: "Aprende a actualizar tu integración de Shopify para Braze."
page_type: partner
search_tag: Partner
permalink: "/shopify_standard_upgrade/"
hidden: true
---

# Actualizar tu integración de Shopify (estándar) {#upgrading-your-shopify-integration-standard}

> Aprende a actualizar tu integración de Shopify utilizando la ruta estándar para Braze. Como parte de nuestro compromiso de ofrecerte la mejor experiencia posible, estamos requiriendo que todas las integraciones de Shopify se [actualicen]({{site.baseurl}}/shopify/) a la última versión antes del 28 de agosto de 2025. Esta actualización es esencial porque cambios significativos en la tecnología de Shopify afectarán el funcionamiento de nuestra integración.

## ¿Quién es elegible? {#whos-eligible}

Esta ruta de actualización está destinada a marcas con una tienda en línea de Shopify.

{% multi_lang_include shopify_alerts.md alert='breaking' %}

## Requisitos de actualización {#upgrade-requirements}

Antes de comenzar, revisa lo siguiente:

- **Cambios críticos:** Asegúrate de haber revisado todos los cambios importantes del conector heredado al nuevo conector en [Resumen de la actualización de Shopify]({{site.baseurl}}/shopify_upgrade_overview/#subscriber-collection).
- **Requisitos previos de actualización:** Asegúrate de haber completado todos los [requisitos previos de actualización]({{site.baseurl}}/shopify_upgrade_overview/#upgrade-prerequisites) necesarios con tus equipos de ingeniería y marketing.
- **Cambios con ruptura:** Revisa y corrige todos los cambios con ruptura señalados en Braze. Para un recorrido completo, continúa a [Corregir cambios con ruptura](#fixing-breaking-changes-fixing-breaking-changes).

## Corregir cambios con ruptura {#fixing-breaking-changes}

En Braze, ve a **Integraciones de socios** > **Shopify** y selecciona **Start upgrade**.

![Panel con una opción para iniciar la actualización.]({% image_buster /assets/unlisted_docs/img/shopify/start_shopify_upgrade.png %}){: style="max-width:35%;"}

Se señalarán todos los Canvas, Campaigns y Segments afectados que utilizan datos de Shopify.

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

Para una lista completa de las nuevas plantillas de Canvas de comercio electrónico y bloques HTML predefinidos para la personalización de productos disponibles a través de la integración, consulta [Crea los recorridos de usuario de tu Canvas]({{site.baseurl}}using_shopify_with_braze#create-your-canvas-user-journeys).

{% alert important %}
Si no tienes en cuenta los mensajes activos que utilizan eventos descontinuados en la integración de Shopify, los mensajes afectados ya no se enviarán a tus clientes.
{% endalert %}

Para obtener más información, revisa [Eventos de Shopify compatibles]({{site.baseurl}}/shopify_upgrade_overview/#supported-shopify-events).
{% endtab %}

{% tab Listas de suscriptores %}
Si estás recopilando suscriptores de correo electrónico o SMS de Shopify a través de la integración, confirma que tus mensajes activos incluyan las listas de suscriptores correspondientes para tu tienda de Shopify.

Cuando la actualización esté completa, se crearán nuevos grupos de suscripción predeterminados para tu integración, los cuales necesitarás aprovechar como parte de tu mensajería activa. Para más información sobre los cambios, consulta [Recopilación de suscriptores]({{site.baseurl}}/shopify_upgrade_overview/#subscriber-collection).
{% endtab %}
{% endtabs %}

## Actualizar Shopify {#upgrading-shopify}

{% alert important %}
Es esencial que [corrijas todos los cambios con ruptura](#fixing-breaking-changes) antes de iniciar tu actualización.
{% endalert %}

### Paso 1: Iniciar la actualización {#step-1-start-the-upgrade}

En Braze, ve a **Integraciones de socios** > **Shopify** y selecciona **Start upgrade**.

![Panel con una opción para iniciar la actualización.]({% image_buster /assets/unlisted_docs/img/shopify/start_shopify_upgrade.png %}){: style="max-width:35%;"}

Acepta los términos y condiciones marcando la casilla y luego selecciona **Start the upgrade**.

![Modal para confirmar que entiendes que la actualización puede causar cambios con ruptura.]({% image_buster /assets/unlisted_docs/img/shopify/confirm_upgrade.png %})

### Paso 2: Configurar los SDK de Braze {#step-2-set-up-the-braze-sdks}

La integración estándar añadirá automáticamente los SDK de Braze a tu sitio de Shopify. Si ya has integrado los SDK de Braze directamente o has utilizado una herramienta de terceros para esto, coordina con tus desarrolladores para eliminar la implementación anterior del SDK mientras realizas la actualización.

![Modal confirmando que la nueva integración implementará automáticamente el SDK de Braze y JavaScript en tu tienda.]({% image_buster /assets/unlisted_docs/img/shopify/confirm_integration.png %}){: style="max-width:70%;"}

### Paso 3: Reautorizar la aplicación de Braze {#step-3-reauthorize-the-braze-app}

Para reautorizar la aplicación de Braze, selecciona **Go to Shopify**.

![Panel de actualización de Shopify con un botón para ir a Shopify y reautorizar la aplicación de Braze.]({% image_buster /assets/unlisted_docs/img/shopify/reauthorize_braze_app.png %}){: style="max-width:35%;"}

En el sitio de Shopify, sigue las indicaciones para reautorizar tu aplicación de Braze. Esto permite que Braze acceda a tus datos de Shopify.

{% alert note %}
El proceso de reautorización puede tardar unos minutos, pero se actualizará automáticamente en tu página de Shopify cuando se complete.
{% endalert %}

![La página "Integration Settings" mostrando el estado de los eventos de Shopify.]({% image_buster /assets/unlisted_docs/img/shopify/reauthorization_status.png %})

### Paso 4: Elegir un tipo de ID externo {#step-4-choose-an-external-id-type}

El tipo de ID externo que elijas se asignará a los nuevos perfiles de clientes de Shopify cuando se cree una cuenta de Shopify o se realice un pedido. También se utilizará para actualizar los perfiles de usuario existentes si ya tienen un alias de ID de cliente de Shopify pero no tienen asignado un ID externo en Braze.

Para elegir tu tipo de ID externo, regresa a Braze y selecciona **Confirm external ID**.

![Panel de actualización de Shopify con un botón para confirmar el ID externo.]({% image_buster /assets/unlisted_docs/img/shopify/confirm_external_id.png %}){: style="max-width:35%;"}

Elige el ID externo que te gustaría usar para la integración de Shopify de tu espacio de trabajo. Cuando termines, selecciona **Set external ID**.

![Modal con un menú desplegable para seleccionar el ID externo.]({% image_buster /assets/unlisted_docs/img/shopify/external_id_field.png %}){: style="max-width:70%;"}

{% alert important %}
Usar una dirección de correo electrónico o una dirección de correo electrónico con hash como tu ID externo de Braze puede ayudar a simplificar la gestión de identidades en tus orígenes de datos. Sin embargo, es importante considerar los riesgos potenciales para la privacidad del usuario y la seguridad de los datos.<br><br>

- **Información predecible:** Las direcciones de correo electrónico son fácilmente predecibles, lo que las hace vulnerables a ataques.
- **Riesgo de explotación:** Si un usuario malintencionado altera su navegador web para enviar la dirección de correo electrónico de otra persona como su ID externo, podría acceder potencialmente a mensajes sensibles o información de la cuenta.
{% endalert %}

De forma predeterminada, Braze convierte automáticamente los correos electrónicos de Shopify a minúsculas antes de usarlos como ID externo. Si estás usando correo electrónico o correo electrónico con hash como tu ID externo, confirma que tus direcciones de correo electrónico también se conviertan a minúsculas antes de asignarlas como tu ID externo o antes de aplicarles hash desde otros orígenes de datos. Esto ayuda a prevenir discrepancias en los ID externos y evitar la creación de perfiles de usuario duplicados en Braze.

Si seleccionaste un tipo de ID externo personalizado, continúa con los pasos 4.1—4.3. De lo contrario, continúa al paso 5.

#### Paso 4.1: Crear el metacampo `braze.external_id` {#step-41-create-the-brazeexternal_id-metafield}

1. En tu panel de administración de Shopify, ve a **Settings** > **Metafields**.
2. Selecciona **Customers** > **Add definition**.
3. Para **Namespace and key**, ingresa `braze.external_id`.
4. Para **Type**, selecciona **ID Type**.

Después de crear el metacampo, rellénalo para tus clientes. Recomendamos los siguientes enfoques:

- **Escuchar webhooks de creación de clientes:** Configura un webhook para escuchar [eventos `customer/create`](https://help.shopify.com/en/manual/fulfillment/setup/notifications/webhooks). Esto te permite escribir el metacampo cuando se crea un nuevo cliente.
- **Rellenar clientes existentes:** Usa la [Admin API](https://shopify.dev/docs/api/admin-graphql) o la [Customer API](https://shopify.dev/docs/api/admin-rest/2025-04/resources/customer) para rellenar el metacampo de los clientes creados anteriormente.

#### Paso 4.2: Crear un punto de conexión para recuperar tu ID externo {#step-42-create-an-endpoint-to-retrieve-your-external-id}

Necesitas crear un punto de conexión público al que Braze pueda llamar para recuperar el ID externo. Esto es necesario para escenarios en los que Shopify no puede proporcionar el metacampo `braze.external_id`.

##### Especificaciones del punto de conexión {#endpoint-specifications}

**Método:** `GET`

| Parámetros | Descripción |
| --- | --- |
| `shopify_customer_id` | El ID de cliente de Shopify. |
| `email_address` | La dirección de correo electrónico del usuario que ha iniciado sesión. |
| `shopify_storefront` | La tienda para la solicitud. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

##### Ejemplo de punto de conexión {#example-endpoint}

```
GET
https://mystore.com/custom_id?shopify_customer_id=1234&email_address=bob@braze.com&shopify_storefront=dev-store.myshopify.com
```

##### Respuesta esperada {#expected-response}

Braze espera un código de estado `200`. Cualquier otro código se considera un fallo.

{% raw %}
```json
{
    "external_id": "my_external_id"
}
```
{% endraw %}

{% alert important %}
Es importante validar que el `shopify_customer_id` y el `email_address` coincidan con los valores del cliente en Shopify. Puedes usar la [Admin API](https://shopify.dev/docs/api/admin-graphql) o la [Customer API](https://shopify.dev/docs/api/admin-rest/2025-04/resources/customer) para validar estos parámetros y recuperar el metacampo `braze.external_id`.
{% endalert %}

#### Paso 4.3: Ingresar tu ID externo {#step-43-input-your-external-id}

Repite el [Paso 4](#step-4-choose-an-external-id-type) e ingresa la URL de tu punto de conexión después de seleccionar ID externo personalizado como tu tipo de ID externo de Braze.

##### Consideraciones {#considerations}

- Si tu ID externo no se genera cuando Braze envía una solicitud a tu punto de conexión, la integración usará de forma predeterminada el ID de cliente de Shopify cuando se llame a la función `changeUser`. Este paso es crucial para fusionar el perfil de usuario anónimo con el perfil de usuario identificado. Como resultado, puede haber un período temporal durante el cual existan diferentes tipos de ID externos dentro de tu espacio de trabajo.
- Cuando el ID externo esté disponible en el metacampo `braze.external_id`, la integración priorizará y asignará este ID externo.
    - Si el ID de cliente de Shopify se estableció previamente como el ID externo de Braze, será reemplazado por el valor del metacampo `braze.external_id`.

### Paso 5: Habilitar la inserción de la aplicación de Braze {#step-5-enable-the-braze-app-embed}

Para habilitar la inserción de la aplicación de Braze dentro del tema de tu tienda, regresa a Braze y selecciona **Go to Shopify**.

![Panel de actualización de Shopify con un botón para habilitar la inserción de la aplicación de Braze.]({% image_buster /assets/unlisted_docs/img/shopify/enable_app_embed.png %}){: style="max-width:35%;"}

En el sitio de Shopify, habilita la inserción de la aplicación de Braze y guarda tus cambios.

![Un ejemplo de inserción de aplicación.]({% image_buster /assets/unlisted_docs/img/shopify/app_embed.png %})

### Paso 6: Verificar la actualización {#step-6-verify-the-upgrade}

De vuelta en Braze, se te notificará cuando tu integración de Shopify haya terminado de instalarse.

![Página de integración de Shopify con un banner de éxito.]({% image_buster /assets/unlisted_docs/img/shopify/success_integration.png %})

Para verificar que tu nuevo conector de Shopify esté en vivo, prueba lo siguiente:

- **Canvas, Campaigns y Segments activos:** Confirma que estén funcionando correctamente.
- **Procesos de gestión de identidades:** Confirma que estos procesos estén funcionando como se espera.
- **Personalizaciones del SDK (opcional):** Si realizaste personalizaciones en tu integración de Braze y Shopify (como registrar eventos personalizados o atributos), verifica que estén funcionando correctamente después de la actualización.
- **Recopilación de suscriptores de correo electrónico o SMS (opcional):** Si habilitaste previamente la recopilación de suscriptores de correo electrónico o SMS, se crearán nuevos grupos de suscripción predeterminados para reflejar el estado más reciente de tus suscriptores durante la actualización. Los grupos de suscripción predeterminados tendrán el nombre de tu tienda de Shopify. Estos nuevos grupos de suscripción predeterminados estarán disponibles aproximadamente 5 horas después de la actualización, y necesitarás añadirlos a tus mensajes activos.

Si tienes alguna pregunta, [ponte en contacto con Soporte]({{site.baseurl}}/user_guide/administrative/access_braze/support/).