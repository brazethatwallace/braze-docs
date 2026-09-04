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

> Aprende a actualizar tu integración de Shopify utilizando la ruta estándar para Braze. Como parte de nuestro compromiso de ofrecerte la mejor experiencia posible, estamos requiriendo que todas las integraciones de Shopify se [actualicen]({{site.baseurl}}/shopify) a la última versión antes del 28 de agosto de 2025. Esta actualización es esencial porque cambios significativos en la tecnología de Shopify afectarán el funcionamiento de nuestra integración.

## ¿Quién es elegible? {#whos-eligible}

Esta ruta de actualización está destinada a marcas con una tienda en línea de Shopify.

{% multi_lang_include partners/shopify_alerts.md alert='breaking' %}

## Requisitos para la actualización {#upgrade-requirements}

Antes de empezar, revisa lo siguiente:

- **Cambios críticos:** Asegúrate de haber revisado todos los cambios importantes del conector heredado al nuevo conector en [Resumen de la actualización de Shopify]({{site.baseurl}}/shopify_upgrade_overview#subscriber-collection).
- **Requisitos previos de la actualización:** Asegúrate de haber completado todos los [requisitos previos de la actualización]({{site.baseurl}}/shopify_upgrade_overview#upgrade-prerequisites) necesarios con tus equipos de ingeniería y marketing.
- **Cambios con interrupciones:** Revisa y corrige todos los cambios con interrupciones señalados en Braze. Para una guía completa, continúa a [Corrección de cambios con interrupciones](#fixing-breaking-changes-fixing-breaking-changes).

## Corregir cambios con ruptura {#fixing-breaking-changes}

En Braze, ve a **Integraciones de socios** > **Shopify** y selecciona **Start upgrade**.

![Panel con una opción para iniciar la actualización.]({% image_buster /assets/unlisted_docs/img/shopify/start_shopify_upgrade.png %}){: style="max-width:35%;"}

Se señalarán todos los Canvas, Campaigns y Segments afectados que utilizan datos de Shopify.

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

Para una lista completa de las nuevas plantillas de Canvas de comercio electrónico y bloques HTML predefinidos para la personalización de productos disponibles a través de la integración, consulta [Crea los recorridos de usuario de tu Canvas]({{site.baseurl}}using_shopify_with_braze#create-your-canvas-user-journeys).

{% alert important %}
Si no tienes en cuenta los mensajes activos que utilizan eventos descontinuados en la integración de Shopify, los mensajes afectados ya no se enviarán a tus clientes.
{% endalert %}

Para obtener más información, revisa [Eventos de Shopify compatibles]({{site.baseurl}}/shopify_upgrade_overview#supported-shopify-events).
{% endtab %}

{% tab Listas de suscriptores %}
Si estás recopilando suscriptores de correo electrónico o SMS de Shopify a través de la integración, confirma que tus mensajes activos incluyan las listas de suscriptores correspondientes para tu tienda de Shopify.

Cuando la actualización esté completa, se crearán nuevos grupos de suscripción predeterminados para tu integración, los cuales necesitarás aprovechar como parte de tu mensajería activa. Para más información sobre los cambios, consulta [Recopilación de suscriptores]({{site.baseurl}}/shopify_upgrade_overview#subscriber-collection).
{% endtab %}
{% endtabs %}

## Actualización de Shopify {#upgrading-shopify}

{% alert important %}
Es fundamental que [corrijas todos los cambios disruptivos](#fixing-breaking-changes) antes de iniciar la actualización.
{% endalert %}

### Paso 1: Inicia la actualización {#step-1-start-the-upgrade}

En Braze, ve a **Integraciones de partners** > **Shopify** y selecciona **Iniciar actualización**.

![Panel con la opción de iniciar la actualización.]({% image_buster /assets/unlisted_docs/img/shopify/start_shopify_upgrade.png %}){: style="max-width:35%;"}

Acepta los términos y condiciones marcando la casilla y selecciona **Iniciar la actualización**.

![Modal para confirmar que comprendes que la actualización puede causar cambios disruptivos.]({% image_buster /assets/unlisted_docs/img/shopify/confirm_upgrade.png %})

### Paso 2: Configura los SDK de Braze {#step-2-set-up-the-braze-sdks}

La integración estándar añadirá automáticamente los SDK de Braze a tu sitio de Shopify. Si ya has integrado los SDK de Braze directamente o has utilizado una herramienta de terceros para esto, coordina con tus desarrolladores para eliminar la implementación anterior del SDK mientras actualizas.

![Modal que confirma que la nueva integración implementará automáticamente el SDK de Braze y JavaScript en tu tienda.]({% image_buster /assets/unlisted_docs/img/shopify/confirm_integration.png %}){: style="max-width:70%;"}

### Paso 3: Reautoriza la aplicación de Braze {#step-3-reauthorize-the-braze-app}

Para reautorizar la aplicación de Braze, selecciona **Ir a Shopify**.

![Panel de actualización de Shopify con un botón para ir a Shopify y reautorizar la aplicación de Braze.]({% image_buster /assets/unlisted_docs/img/shopify/reauthorize_braze_app.png %}){: style="max-width:35%;"}

En el sitio de Shopify, sigue las indicaciones para reautorizar tu aplicación de Braze. Esto permite que Braze acceda a tus datos de Shopify.

{% alert note %}
El proceso de reautorización puede tardar unos minutos, pero se actualizará automáticamente en tu página de Shopify cuando se complete.
{% endalert %}

![La página "Configuración de integración" mostrando el estado de los eventos de Shopify.]({% image_buster /assets/unlisted_docs/img/shopify/reauthorization_status.png %})

### Paso 4: Elige un tipo de ID externo {#step-4-choose-an-external-id-type}

El tipo de ID externo que elijas se asignará a los nuevos perfiles de clientes de Shopify cuando se cree una cuenta de Shopify o se realice un pedido. También se usará para actualizar los perfiles de usuario existentes si ya tienen un alias de ID de cliente de Shopify pero no tienen asignado un ID externo en Braze.

Para elegir tu tipo de ID externo, vuelve a Braze y selecciona **Confirmar ID externo**.

![Panel de actualización de Shopify con un botón para confirmar el ID externo.]({% image_buster /assets/unlisted_docs/img/shopify/confirm_external_id.png %}){: style="max-width:35%;"}

Elige el ID externo que deseas usar para la integración de Shopify de tu espacio de trabajo. Cuando hayas terminado, selecciona **Establecer ID externo**.

![Modal con un desplegable para seleccionar el ID externo.]({% image_buster /assets/unlisted_docs/img/shopify/external_id_field.png %}){: style="max-width:70%;"}

{% alert important %}
Usar una dirección de correo electrónico o una dirección de correo electrónico con hash como tu ID externo de Braze puede ayudar a simplificar la gestión de identidades en tus orígenes de datos. Sin embargo, es importante considerar los riesgos potenciales para la privacidad del usuario y la seguridad de los datos.<br><br>

- **Información predecible:** Las direcciones de correo electrónico son fáciles de adivinar, lo que las hace vulnerables a ataques.
- **Riesgo de explotación:** Si un usuario malintencionado altera su navegador web para enviar la dirección de correo electrónico de otra persona como su ID externo, podría acceder a mensajes sensibles o información de la cuenta.
{% endalert %}

De forma predeterminada, Braze convierte automáticamente los correos electrónicos de Shopify a minúsculas antes de usarlos como ID externo. Si estás usando el correo electrónico o el correo electrónico con hash como tu ID externo, confirma que tus direcciones de correo electrónico también se conviertan a minúsculas antes de asignarlas como tu ID externo o antes de aplicarles hash desde otros orígenes de datos. Esto ayuda a evitar discrepancias en los ID externos y a no crear perfiles de usuario duplicados en Braze.

Si seleccionaste un tipo de ID externo personalizado, continúa con los pasos 4.1 a 4.3. De lo contrario, continúa con el paso 5.

#### Paso 4.1: Crea el metacampo `braze.external_id` {#step-41-create-the-brazeexternal_id-metafield}

{% multi_lang_include partners/shopify/customer_metafield_definition_steps.md %}

Después de crear el metacampo, rellénalo para tus clientes. Recomendamos los siguientes enfoques:

- **Escuchar webhooks de creación de clientes:** Configura un webhook para escuchar los [eventos `customer/create`](https://help.shopify.com/en/manual/fulfillment/setup/notifications/webhooks). Esto te permite escribir el metacampo cuando se crea un nuevo cliente.
- **Rellenar clientes existentes:** Usa la [API de administración](https://shopify.dev/docs/api/admin-graphql) o la [API de clientes](https://shopify.dev/docs/api/admin-rest/2025-04/resources/customer) para rellenar el metacampo de los clientes creados anteriormente.

#### Paso 4.2: Crea un endpoint para recuperar tu ID externo {#step-42-create-an-endpoint-to-retrieve-your-external-id}

Necesitas crear un endpoint público al que Braze pueda llamar para recuperar el ID externo. Esto es necesario para escenarios en los que Shopify no puede proporcionar el metacampo `braze.external_id`.

##### Especificaciones del endpoint {#endpoint-specifications}

**Método:** `GET`

| Parámetros | Descripción |
| --- | --- |
| `shopify_customer_id` | El ID de cliente de Shopify. |
| `email_address` | La dirección de correo electrónico del usuario que ha iniciado sesión. |
| `shopify_storefront` | El escaparate de la solicitud. |
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
{
    "external_id": "my_external_id"
}
```
{% endraw %}

{% alert important %}
Es importante validar que `shopify_customer_id` y `email_address` coincidan con los valores del cliente en Shopify. Puedes usar la [API de administración](https://shopify.dev/docs/api/admin-graphql) o la [API de clientes](https://shopify.dev/docs/api/admin-rest/2025-04/resources/customer) para validar estos parámetros y recuperar el metacampo `braze.external_id`.
{% endalert %}

#### Paso 4.3: Introduce tu ID externo {#step-43-input-your-external-id}

Repite el [paso 4](#step-4-choose-an-external-id-type) e introduce la URL de tu endpoint después de seleccionar ID externo personalizado como tu tipo de ID externo de Braze.

##### Consideraciones {#considerations}

{% multi_lang_include partners/shopify/external_id_generation_notes.md %}

### Paso 5: Habilita la inserción de la aplicación de Braze {#step-5-enable-the-braze-app-embed}

Para habilitar la inserción de la aplicación de Braze dentro del tema de tu tienda, vuelve a Braze y selecciona **Ir a Shopify**.

![Panel de actualización de Shopify con un botón para habilitar la inserción de la aplicación de Braze.]({% image_buster /assets/unlisted_docs/img/shopify/enable_app_embed.png %}){: style="max-width:35%;"}

En el sitio de Shopify, habilita la inserción de la aplicación de Braze y guarda tus cambios.

![Ejemplo de inserción de una aplicación.]({% image_buster /assets/unlisted_docs/img/shopify/app_embed.png %})

### Paso 6: Verifica la actualización {#step-6-verify-the-upgrade}

De vuelta en Braze, recibirás una alerta cuando tu integración de Shopify haya terminado de instalarse.

![Página de integración de Shopify con un banner de éxito.]({% image_buster /assets/unlisted_docs/img/shopify/success_integration.png %})

Para verificar que tu nuevo conector de Shopify está en vivo, prueba lo siguiente:

{% multi_lang_include partners/shopify/upgrade_validation_checklist.md %}

Si tienes alguna pregunta, [contacta con soporte]({{site.baseurl}}/user_guide/administer/personal/braze_support).