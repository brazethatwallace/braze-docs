---
nav_title: Mensajes de producto
article_title: Mensajes de producto
page_order: 4
description: "Esta página explica cómo usar los mensajes de producto de WhatsApp para enviar mensajes interactivos de WhatsApp que muestren productos de tu catálogo de Meta."
page_type: reference
alias: "/whatsapp_product_messages/"
tool:
 - Campaigns
channel:
 - WhatsApp
---

# Mensajes de producto {#product-messages}

> Los mensajes de producto te permiten enviar mensajes interactivos de WhatsApp que muestran productos directamente desde tu catálogo de Meta.

Cuando envías un mensaje de producto de WhatsApp a un usuario, este sigue el siguiente recorrido del cliente:

1. El usuario recibe tu mensaje de producto o catálogo en WhatsApp.
2. El usuario añade productos a su carrito directamente desde WhatsApp.
3. El usuario toca **Place order** en WhatsApp.
4. Tu sitio web o aplicación recibe los datos del carrito desde Braze y genera un enlace de pago.
5. El usuario es dirigido a tu sitio web o aplicación para completar su compra.

Cuando los usuarios añaden artículos a su carrito a través de mensajes de catálogo, Braze recibe datos de webhook para acciones de seguimiento.

## Requisitos {#requirements}

| Requisito | Descripción |
| --- | --- |
| Cuenta de WhatsApp Business | Para usar los mensajes de producto de WhatsApp, debes tener una cuenta de WhatsApp Business conectada con Braze. |
| Catálogo de Meta | Necesitas configurar un catálogo de Meta en tu Commerce Manager. |
| Cumplimiento de términos | Cumplir con los [Términos y políticas de comercio de Meta](https://www.facebook.com/policies_center/commerce). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos" }

## Tipos de mensajes de producto {#product-message-types}

{% alert note %}
Mejora tu experiencia con mensajes de producto con el selector de productos integrado, al que se accede durante el paso 4 de [Configuración de mensajes de producto](#setting-up-product-messages).
{% endalert %}

{% tabs local %}
{% tab Mensajes de catálogo %}

Los mensajes de catálogo muestran todo tu catálogo de productos en un formato interactivo. Están disponibles como [mensajes de plantilla y de respuesta](#building-a-product-message).

Si habilitaste los permisos de catálogo para Braze durante la [configuración](#setting-up-product-messages), puedes seleccionar qué miniatura es visible para los usuarios.

{% alert note %}
No necesitas hacer selecciones de productos adicionales en Braze, ya que la conexión del catálogo es gestionada por Meta y, por lo tanto, se hereda en tu catálogo de productos.
{% endalert %}


{% endtab %}
{% tab Mensajes multiproducto %}

Los mensajes multiproducto destacan productos específicos de tu catálogo, con hasta 30 artículos destacados por mensaje. Están disponibles como [mensajes de plantilla y de respuesta](#building-a-product-message).

Puedes seleccionar los productos manualmente con IDs o, si habilitaste los permisos de catálogo durante la [configuración](#setting-up-product-messages), usar el selector desplegable de productos.

{% alert important %}
Existe un problema conocido de visualización de encabezados con las plantillas de mensajes multiproducto en Meta. Meta está al tanto del problema y trabajando en una solución.
{% endalert %}

{% endtab %}
{% tab Producto único %}

Los mensajes de producto único destacan un producto específico de tu catálogo de productos. Están disponibles como [mensajes de respuesta](#building-a-product-message).

Puedes seleccionar los productos manualmente con IDs o, si habilitaste los permisos de catálogo durante la [configuración](#setting-up-product-messages), usar el selector desplegable de productos.

{% endtab %}
{% endtabs %}

## Configuración de mensajes de producto {#setting-up-product-messages}

1. En el [Meta Commerce Manager](https://business.facebook.com/business/loginpage/?next=https%3A%2F%2Fbusiness.facebook.com%2Fcommerce_manager%2F#), sigue [las instrucciones de Meta](https://www.facebook.com/business/help/1275400645914358?id=725943027795860&ref=search_new_1) para crear tu catálogo de Meta. Asegúrate de estar en el mismo Meta Business Portfolio donde reside tu cuenta de WhatsApp Business conectada con Braze.
2. Sigue las instrucciones de Meta para [conectar tu catálogo de Meta](https://www.facebook.com/business/help/1953352334878186?id=2042840805783715) a tu cuenta de WhatsApp Business conectada con Braze asignando el permiso "Manage Catalog" en Meta Business Manager.

![Página de "Catalogs" de Meta con una flecha apuntando al botón "Assign partner" para el catálogo llamado "sweeney_catalog".]({% image_buster /assets/img/whatsapp/meta_catalog.png %}){: style="max-width:90%;"}

Asegúrate de usar el ID de Braze Business Manager, `332231937299182`, como ID de socio comercial.

![Ventana para compartir un catálogo con un socio que contiene campos para ingresar un ID de socio comercial y asignar el permiso "Manage catalog".]({% image_buster /assets/img/whatsapp/share_meta_catalog.png %}){: style="max-width:70%;"}

{: start="3"}
3. Selecciona la configuración de tu catálogo de Meta. Debes seleccionar **Show catalog icon in chat header** para enviar mensajes de catálogo.

![Página de configuración de WhatsApp Manager para el catálogo "Catalog_products".]({% image_buster /assets/img/whatsapp/meta_catalog_settings.png %}){: style="max-width:90%;"}

{: start="4"}
4. En Braze, completa el proceso de [registro integrado]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/embedded_signup) para proporcionar permisos. Asegúrate de seleccionar **todos** los catálogos para los que deseas proporcionar permisos. Esto desbloqueará el selector de productos integrado de Braze.

![Ventana con cinco catálogos seleccionados para proporcionar permisos.]({% image_buster /assets/img/whatsapp/select_catalogs.png %}){: style="max-width:50%;"}

{% alert tip %}
Para conocer las mejores prácticas al crear catálogos de Meta, consulta [Consejos para crear un catálogo de alta calidad en Commerce Manager](https://www.facebook.com/business/help/2086567618225367?id=725943027795860).
{% endalert %}

## Creación de un mensaje de producto {#building-a-product-message}

Puedes crear un mensaje de producto usando una plantilla de mensaje de WhatsApp o un mensaje de respuesta.

{% tabs local %}
{% tab Plantilla de mensaje de WhatsApp %}

1. En tu Meta Business Manager, ve a **Message Templates**.
2. Selecciona **Catalog** como formato y luego elige entre **Catalog message** (muestra el catálogo completo) y **Multi-product catalog message** (destaca artículos específicos).
3. En Braze, crea una Campaign de WhatsApp o un paso de mensaje en Canvas.
4. Selecciona el grupo de suscripción que coincida con donde enviaste la plantilla.
5. Selecciona **WhatsApp Template Message**.
6. Selecciona la plantilla que deseas usar.
    - Si seleccionas una plantilla multiproducto, proporciona el título de la sección y los IDs de contenido de los productos a destacar. Puedes copiar el Content ID directamente desde tu Meta Commerce Manager o, si habilitaste los permisos para el selector de productos integrado, seleccionar los artículos.

![Lista de artículos con campos para ingresar los títulos de sección y el ID de contenido.]({% image_buster /assets/img/whatsapp/multi_product_template.png %}){: style="max-width:60%;"}

![Lista de artículos con un desplegable de artículos para seleccionar.]({% image_buster /assets/img/whatsapp/content_id_items.png %}){: style="max-width:60%;"}

{: start="7"}
7. Continúa creando tu mensaje.

{% endtab %}
{% tab Mensaje de respuesta %}

1. En Braze, crea una Campaign de WhatsApp o un paso de mensaje en Canvas.
2. Selecciona un grupo de suscripción.
3. Selecciona **Response Message**.
4. Selecciona **Meta Product Messages**.

![Opciones para seleccionar un tipo de mensaje y diseño de mensaje de respuesta, con "Response Message" y "Meta Product Messages" resaltados.]({% image_buster /assets/img/whatsapp/response_message_layouts.png %}){: style="max-width:90%;"}

{: start="5"}
5. Selecciona el [tipo de mensaje](#product-message-types) que deseas usar.

![Selección de diseño de mensaje "Multi-product".]({% image_buster /assets/img/whatsapp/multi-product_message_layout.png %}){: style="max-width:90%;"}

{: start="6"}
6. Continúa creando tu mensaje.

![Ejemplo de mensaje de producto de Meta con información completada para los productos.]({% image_buster /assets/img/whatsapp/example_response_message.png %}){: style="max-width:90%;"}

{% endtab %}
{% endtabs %}

## Gestión de productos {#managing-products}

### Acceso a Commerce Manager {#accessing-commerce-manager}

En tu Meta Business Manager, ve a **Commerce Manager** y selecciona tu organización. Aquí puedes gestionar los activos de tu catálogo, como:
- Crear nuevos catálogos
- Añadir productos a catálogos existentes
- Actualizar información de productos
- Quitar artículos descontinuados

{% alert important %}
Si eliminas productos referenciados de tu catálogo, los mensajes asociados no se enviarán.
{% endalert %}

## Recepción de preguntas entrantes sobre productos {#receiving-inbound-product-questions}

Los usuarios pueden responder a tu mensaje de producto o catálogo con preguntas sobre productos. Estas llegan como mensajes entrantes, que luego pueden clasificarse con una [ruta de acción]({{site.baseurl}}/action_paths).

Además, Braze extrae el ID del producto y el ID del catálogo de estas preguntas, por lo que si deseas automatizar respuestas o enviar preguntas a otro equipo (como soporte al cliente), puedes incluir esos detalles. Por ejemplo, podrías personalizar respuestas con las propiedades de WhatsApp `inbound_product_id` o `inbound_catalog_id`.

![Ventana "Add Personalization" con un tipo de personalización de "WhatsApp Properties" y un atributo resaltado de "inbound_product_id".]({% image_buster /assets/img/whatsapp/inbound_product_questions.png %}){: style="max-width:60%;"}

## Pago: procesamiento de carritos y webhooks {#checkout-cart-processing-and-webhooks}

Cuando los usuarios interactúan con tus mensajes de producto de WhatsApp, pueden explorar productos y añadir artículos a su carrito. Sin embargo, actualmente no existe una funcionalidad de pago integrada para información de envío o procesamiento de pagos. En su lugar, te recomendamos crear un carrito dentro de tu propia aplicación o sitio web y dirigir a los usuarios a ese carrito usando un enlace personalizado.

### Consideraciones {#considerations}

- **Sin pago dentro de la aplicación:** los usuarios no pueden completar compras directamente dentro de WhatsApp. Todas las transacciones deben redirigirse a tu sitio web o aplicación.
- **Enlace personalizado requerido:** necesitas crear un enlace personalizado que dirija a los usuarios a su carrito en tu plataforma.
- **Configuración manual:** el proceso de configuración requiere la configuración manual de tu carrito y flujos de mensajería.

{% alert note %}
Actualmente no admitimos pagos que ocurran directamente en WhatsApp, y el soporte futuro será específico por país (actualmente, Meta lo ofrece solo para empresas con sede en India, Brasil y Singapur que trabajan directamente con usuarios en esos países).
{% endalert %}

### Configuración de desencadenadores de eventos de carrito {#setting-up-cart-event-triggers}

Cuando un cliente realiza un pedido en WhatsApp, Braze automáticamente:
1. Recibe el contenido del carrito desde WhatsApp (IDs de productos, cantidades y otros datos del pedido).
2. Crea un evento de comercio electrónico `ecommerce.cart_update` con todos los datos relevantes, incluyendo `source = whats_app`.
3. Desencadena una respuesta, permitiéndote configurar campañas automatizadas para responder al pedido.

El evento de comercio electrónico `ecommerce.cart_update` solo aparece listado en Braze después de que se haya enviado un evento, lo cual se puede hacer generando un mensaje de producto de prueba desde Braze y enviando un evento de carrito.
El evento de carrito incluye:

- **ID del carrito:** identificador único del carrito
- **Productos:** lista de artículos con IDs de productos, cantidades y precios
- **Valor total:** suma de todos los artículos
- **Moneda:** la moneda del carrito
- **Origen:** marcado como "whats_app"
- **Metadatos:** datos adicionales como el ID del catálogo y el texto del mensaje

Puedes encontrar información adicional sobre eventos de carrito de Braze en [Tipos de eventos de comercio electrónico recomendados]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events).

### Configuración de una respuesta desencadenada {#setting-up-a-triggered-response}

1. Crea un desencadenador de evento personalizado para `ecommerce.cart_updated`.
2. Añade un filtro de propiedad para `source = "whats_app"`.

![Paso de Canvas para un desencadenador de evento personalizado `ecommerce.cart_updated` con la propiedad básica de "source" igual a `whats_app`.]({% image_buster /assets/img/whatsapp/product_message_canvas_step.png %})

{: start="3"}
3. Configura acciones de seguimiento basadas en los datos del carrito.

### Implementaciones de pago recomendadas {#recommended-checkout-implementations}

{% tabs local %}
{% tab Enlaces de carrito basados en Liquid %}

Usa Liquid para crear URLs de carrito directamente en tu mensaje de respuesta. Esto es ideal si tienes IDs de productos consistentes entre WhatsApp y tu plataforma de comercio electrónico.

#### Ejemplo de Liquid {#example-liquid}

{% raw %}
```liquid
{% assign cart_link = "http://alejandro-test-new.myshopify.com/cart/" %}
{% for product in event_properties.products %}
 {% assign variant_id = product.product_id %}
 {% assign quantity = product.quantity %}
 {% if forloop.first %}
   {% assign cart_link = cart_link | append: variant_id | append: ":" | append: quantity %}
 {% else %}
   {% assign cart_link = cart_link | append: "," | append: variant_id | append: ":" | append: quantity %}
 {% endif %}
{% endfor %}
{{ cart_link }}
```
{% endraw %}

#### Configuración {#setup}

1. Crea una Campaign de mensaje de respuesta de WhatsApp con el desencadenador de un evento de comercio electrónico `ecommerce.cart_update`.
2. Crea un mensaje posterior con la URL del carrito.
3. Construye tu URL de carrito con Liquid. Si usas Shopify, puedes [crear un enlace permanente de carrito](https://shopify.dev/docs/apps/build/checkout/create-cart-permalinks) con el ejemplo de Liquid anterior.

![Diagrama que muestra el flujo de trabajo de la experiencia de pago para un carrito generado con Liquid: Meta envía un mensaje de pedido recibido a Braze, que desencadena un desencadenador basado en acciones y luego crea un mensaje con un enlace de carrito, que luego envía un mensaje de WhatsApp.]({% image_buster /assets/img/whatsapp/liquid_generated_cart_link_checkout.png %})

{% endtab %}
{% tab Contenido conectado %}

Realiza una llamada API a tu sistema de comercio electrónico para generar una URL de pago personalizada. Esto es ideal si necesitas generación dinámica de URLs de carrito o mapeado complejo de productos.

#### Configuración

1. Crea una Campaign de webhook o un paso en Canvas desencadenado por el evento de comercio electrónico [`ecommerce.cart_update`]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events?tab=ecommerce.cart_updated), que enviará los datos del carrito a tu sistema de comercio electrónico.
2. Crea una Campaign de WhatsApp o un paso de mensaje en Canvas desencadenado por el mismo evento de comercio electrónico para enviar un mensaje de respuesta de WhatsApp con la URL del carrito al usuario. Sigue las instrucciones en el mensaje de respuesta posterior para usar [contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content).

![Diagrama que muestra el flujo de trabajo de la experiencia de pago para una llamada de contenido conectado: Meta envía un mensaje de pedido recibido a Braze, que tiene llamadas de ida y vuelta con una plataforma de comercio electrónico, y luego envía un mensaje de WhatsApp.]({% image_buster /assets/img/whatsapp/connected_content_checkout.png %})

{% endtab %}
{% tab Webhooks y eventos personalizados %}

Usa webhooks para enviar datos del carrito a tu sistema y luego desencadena mensajes de seguimiento a través de eventos personalizados. Esto es ideal para integraciones complejas que requieren un procesamiento extenso del carrito o flujos de trabajo de varios pasos.

#### Configuración

Crea una Campaign de webhook o un paso en Canvas desencadenado por el evento de comercio electrónico `ecommerce.cart_update`, que enviará los datos del carrito a tu sistema de comercio electrónico. Tu API entonces:
1. Recibirá los datos del carrito
2. Creará un carrito en tu sistema
3. Generará la URL de pago
4. Enviará un evento `checkout_started` a Braze, desencadenando el envío de tu mensaje de WhatsApp con el enlace de pago

![Diagrama que muestra el flujo de trabajo de la experiencia de pago para webhooks y eventos personalizados: Meta envía un mensaje de pedido recibido a Braze, que tiene llamadas de ida y vuelta con una plataforma de comercio electrónico, y luego envía un mensaje de WhatsApp con la URL del carrito.]({% image_buster /assets/img/whatsapp/webhooks_custom_events_checkout.png %})

{% endtab %}
{% endtabs %}

## Pruebas y validación {#testing-and-validation}

### Requisitos de mensajes de prueba {#test-message-requirements}

La funcionalidad del carrito se mantiene entre mensajes de prueba, pero el procesamiento del resultado entrante no se mantiene.

### Vista previa del mensaje {#message-preview}

- Las imágenes y detalles de los productos se obtienen de tu catálogo de Meta.
- La vista previa interactiva muestra marcadores de posición hasta que la integración esté completa.

### Códigos de error {#error-codes}

- Si un ID de producto no existe en el catálogo, recibirás el error `product not found for product_retailer_id, fake-product-id, in catalog_id, 1903196950214359`.
- Si un catálogo está desconectado del WABA, recibirás el error `Check if catalog is linked to the WhatsApp Business Account and the catalog is enabled in the WhatsApp Commerce Settings`.