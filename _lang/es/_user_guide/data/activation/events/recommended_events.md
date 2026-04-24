---
nav_title: Eventos recomendados
article_title: Eventos recomendados
alias: /recommended_events/
page_order: 2
page_type: reference
description: "Este artículo de referencia describe los eventos recomendados, que son recomendaciones proporcionadas por Braze para eventos de comercio electrónico."
---

# Eventos recomendados

> Los eventos recomendados se corresponden con los casos de uso de comercio electrónico más comunes. Al usar eventos recomendados, puedes desbloquear plantillas de Canvas prediseñadas, dashboards de informes que se corresponden con el ciclo de vida del cliente, y más.

Por ejemplo, puede que tengas un evento personalizado llamado "cart_updated" o "update_to_cart" para capturar cuándo un usuario ha añadido, eliminado o actualizado los productos en su carrito. Para los eventos recomendados, Braze proporcionará la plantilla del evento, que incluye un nombre definido y propiedades relevantes para este evento.

{% alert important %}
Los eventos recomendados se encuentran actualmente en acceso anticipado. Ponte en contacto con tu administrador del éxito del cliente de Braze si te interesa participar en este acceso anticipado. <br><br>Si estás utilizando el nuevo [conector de Shopify]({{site.baseurl}}/partners/ecommerce/shopify/multiple_stores/?tab=shopify%20connector), estos eventos recomendados estarán disponibles automáticamente a través de la integración.
{% endalert %}

## Cómo funciona

Braze aplica una validación especial a todos los eventos recomendados, y algunos eventos recomendados tienen acciones especiales de posprocesamiento. Para ciertos eventos recomendados de la industria, Braze puede admitir un tratamiento especial, como nuevos desencadenantes basados en acciones para campañas y Canvas.

Los eventos recomendados funcionan de manera similar a los [eventos personalizados]({{site.baseurl}}/user_guide/data/activation/events/custom_events/). Puedes exportar eventos recomendados desde Currents, incluirlos en la lista de bloqueo y usarlos en informes. También puedes enviar datos a Braze para el seguimiento de estos eventos usando el [SDK de Braze]({{site.baseurl}}/developer_guide/getting_started/sdk_overview) o el [punto de conexión `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track).

### Eventos recomendados de comercio electrónico

Los [eventos recomendados de comercio electrónico]({{site.baseurl}}/ecommerce_events/) se basan en los eventos recomendados. Estos eventos recomendados de comercio electrónico hacen seguimiento de las acciones realizadas por tus clientes, como ver un producto, actualizar su carrito o iniciar el proceso de pago.

- `ecommerce.product_viewed`
- `ecommerce.cart_updated`
- `ecommerce.checkout_started`
- `ecommerce.order_placed`
- `ecommerce.order_refunded`
- `ecommerce.order_cancelled`

#### Plantillas de Canvas de comercio electrónico

Consulta nuestros [casos de uso de comercio electrónico]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/ecommerce_use_cases/) dedicados para obtener más ideas sobre cómo usar las plantillas prediseñadas de Braze Canvas para implementar estrategias esenciales.

## Preguntas frecuentes

### ¿Los eventos recomendados son lo mismo que los eventos personalizados?

No. Braze definirá esquemas de datos específicos para los eventos recomendados. Esto incluirá propiedades del evento obligatorias y opcionales que pasarán por un proceso de validación en Braze. Los [eventos personalizados]({{site.baseurl}}/user_guide/data/activation/events/custom_events/) son acciones específicas realizadas por tus usuarios, o actualizaciones sobre ellos, en tu aplicación o sitio web que deseas rastrear. Puedes personalizar el nombre del evento y lo que rastrea.

### ¿Puedo personalizar el nombre de los eventos recomendados?

No. Los eventos recomendados tienen nombres y propiedades de eventos estandarizados. Estas estandarizaciones ayudan a crear consistencia en tus datos.

### ¿Puedo seguir usando eventos de compra para registrar compras?

Con el lanzamiento de los eventos recomendados de comercio electrónico, Braze dejará de dar soporte al evento de compra heredado en el futuro. Si actualmente estás usando el evento de compra, recibirás un aviso con antelación sobre los planes de descontinuación. Mientras tanto, puedes seguir usando los eventos de compra hasta la fecha oficial de descontinuación.