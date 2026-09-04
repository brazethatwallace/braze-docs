---
nav_title: Eventos de conversión
article_title: Eventos de conversión
page_order: 3
page_type: reference
description: "Este artículo de referencia define los eventos de conversión, cómo utilizarlos para definir tus métricas de éxito en Braze y cómo usar estos eventos para ver qué tan comprometidos están tus usuarios."
tool:
    - Campaigns
    - Canvas
---

# Eventos de conversión {#conversion-events}

> Un evento de conversión es un tipo de métrica de éxito que rastrea si un destinatario de tu mensajería realiza una acción de alto valor en un período de tiempo determinado después de recibir tu interacción. Usa estos eventos para asegurarte de que estás recopilando información relevante y útil que luego puedes utilizar para obtener información sobre tu Campaign o Canvas.

## Cómo funciona {#how-it-works}

Para una campaña festiva personalizada dirigida a usuarios activos, un evento de conversión de **Iniciar una sesión** dentro de dos o tres días puede ser apropiado porque te permite tener una noción de la participación del usuario a partir de la recepción de tu mensaje. También puedes seleccionar eventos adicionales como **Realizar pedido**, **Actualizar aplicación** o cualquiera de tus eventos personalizados como eventos de conversión.

### ¿Cuándo comienza el seguimiento de conversiones? {#when-does-conversion-tracking-begin}

{% tabs %}
{% tab Campaign %}

El seguimiento de conversiones comienza cuando un usuario recibe la Campaign o entra en el grupo de control de la Campaign. La recepción de un mensaje y la asignación a una variante generalmente ocurren al mismo tiempo. Para Campaigns de mensajes dentro de la aplicación, el seguimiento de conversiones comienza cuando Braze registra una impresión.

{% endtab %}
{% tab Canvas %}

El seguimiento de conversiones comienza cuando un usuario entra en el Canvas. Para los pasos en Canvas, las conversiones se atribuyen mientras el usuario está activo en ese paso. Cuando el usuario avanza a otro paso, el seguimiento de conversiones se detiene para el paso anterior y comienza para el siguiente.

Mientras un usuario se encuentra en un paso de Retraso u otro paso sin mensaje, las conversiones que ocurren durante esa espera aún se atribuyen al último paso de mensaje recibido hasta que el usuario recibe otro paso de mensaje. Después de que el usuario recibe el último paso de mensaje en su recorrido, las conversiones aún pueden registrarse hasta la fecha límite de conversión (contada desde la entrada al Canvas), incluso si no hay más pasos de mensaje.

{% endtab %}
{% endtabs %}

{% alert tip %}
Para más información sobre conversiones, consulta nuestro [curso de Braze Learning](https://learning.braze.com/campaign-setup-delivery-targeting-conversions) sobre la configuración de Campaigns.
{% endalert %}

### Reglas de seguimiento de conversiones {#conversion-tracking-rules}

Los eventos de conversión atribuyen las acciones de los usuarios a un punto de participación. En general, mientras una ventana de conversión está abierta, un usuario convierte como máximo una vez por evento de conversión para esa Campaign o Canvas. Si realiza la misma acción de conversión más de una vez antes de la fecha límite (por ejemplo, dos compras), Braze solo cuenta una conversión para ese evento. Las Campaigns multicanal pueden registrar una oportunidad de conversión separada para cada canal de mensajería, lo que puede producir tasas de conversión superiores al 100 % cuando comparas los recuentos de conversiones con los destinatarios únicos (como se describe en los siguientes puntos).

Ten en cuenta lo siguiente sobre cómo Braze gestiona las conversiones múltiples:

- **Campaigns de canal único:** Las conversiones ocurren por usuario, no por dispositivo. Dentro de un solo canal, un usuario convierte solo una vez por evento de conversión, incluso si un mensaje se envía a varios dispositivos. Por ejemplo, si una Campaign tiene un solo evento de conversión configurado como "Realiza cualquier compra" y un usuario realiza dos compras separadas dentro de la fecha límite de conversión, Braze solo cuenta una conversión. Sin embargo, cuando la [reelegibilidad]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility) está habilitada, los usuarios que reciben la Campaign varias veces pueden volver a convertir con cada envío. En Campaigns con reelegibilidad, el mecanismo de conversión es una vez por usuario por envío de Campaign, lo que puede resultar en recuentos de conversiones más altos cuando los usuarios reciben y convierten a partir de la misma Campaign varias veces.
- **Campaigns multicanal:** Para Campaigns multicanal, cada canal tiene su propia oportunidad de conversión. Un usuario puede convertir una vez por canal después de recibir un mensaje en ese canal. Esto significa que si un usuario recibe mensajes en varios canales (por ejemplo, tanto correo electrónico como push) y realiza la acción de conversión, Braze cuenta una conversión por cada canal, lo que puede resultar en tasas de conversión superiores al 100 %.
- **Pasos de mensaje en Canvas:** Braze atribuye las conversiones que ocurren dentro de la fecha límite de conversión al último paso de mensaje en Canvas que el usuario recibió. Después de que recibe el siguiente paso de mensaje, la atribución se traslada a ese paso. Braze mide esa ventana desde que el usuario entra en el Canvas, no desde cada mensaje individual. Las conversiones que ocurren durante los retrasos entre pasos de mensaje cuentan para la atribución del paso de mensaje anterior hasta que el usuario avance; las conversiones después del último paso de mensaje aún cuentan hasta la fecha límite de conversión del Canvas.
- **Retención de eventos históricos:** El seguimiento de conversiones en los paneles de Campaign y Canvas mide acciones históricas, no perfiles de usuario actuales. Cuando un usuario cumple una regla de conversión dentro de la ventana designada, Braze registra una conversión en los análisis y no la elimina, incluso si el perfil de ese usuario se elimina, fusiona o archiva posteriormente durante tareas rutinarias de higiene de datos o cumplimiento del RGPD. Los recuentos de Segments en vivo pueden ser naturalmente inferiores a los registros de eventos permanentes del panel porque los Segments dinámicos solo filtran perfiles activos que existen actualmente en la base de datos.
- Si un usuario realiza un evento de conversión dentro de las fechas límite de conversión de dos Campaigns o Canvas separados que recibió, la conversión se registra en ambos.
- Un usuario se cuenta como convertido si realizó el evento de conversión específico en la ventana, incluso si no abrió ni hizo clic en el mensaje.

### Evento de conversión primaria {#primary-conversion-event}

El evento de conversión primaria es el primer evento que agregas durante la creación de la Campaign o el Canvas. Este evento tiene la mayor influencia en tu participación e informes. Braze utiliza tu evento de conversión primaria para:

- Seleccionar la variante de mensaje con mejor rendimiento en [Campaigns multivariantes]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/variant_selection) o Canvas.
- Determinar la ventana en la que se calculan los ingresos para la Campaign o el Canvas.
- Ajustar las distribuciones de mensajes para Campaigns y Canvas utilizando [Optimizar con BrazeAI<sup>TM</sup>]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/variant_selection).

El recuento de eventos de conversión primaria es el número de eventos de conversión que ocurrieron. Para Campaigns multicanal, Braze cuenta las conversiones por canal (como se describe en [Reglas de seguimiento de conversiones](#conversion-tracking-rules)), lo que significa que el recuento de conversiones puede superar el número de usuarios únicos y dar lugar a tasas de conversión superiores al 100 %. Braze calcula la tasa de eventos de conversión primaria dividiendo este recuento entre el número de destinatarios únicos. Braze considera a un usuario como destinatario cuando el mensaje se envía o se muestra, dependiendo del canal. Por ejemplo, en push o correo electrónico, un usuario se convierte en destinatario después de que Braze envía el mensaje. Para mensajes dentro de la aplicación o Content Cards, el usuario debe ver el mensaje para ser considerado destinatario.

{% alert note %}
Si interrumpes mensajes utilizando la etiqueta Liquid `abort`, Braze interrumpe los mensajes solo para los usuarios que pasan por las variantes. Los mensajes para los usuarios en el grupo de control no se interrumpen, lo que puede llevar a porcentajes de conversión sesgados entre las variantes y los grupos de control. Como solución alternativa, utiliza la [segmentación]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment) para dirigirte a tus usuarios en la entrada de la Campaign y el Canvas.
{% endalert %}

## Creación de una Campaign con seguimiento de conversiones {#creating-a-campaign-with-conversion-tracking}

### Paso 1: Configura tu Campaign {#step-1-set-up-your-campaign}

[Crea una Campaign]({{site.baseurl}}/user_guide/messaging/campaigns/creating_campaign) para el canal de mensajería que desees. Después de configurar los mensajes y la programación de tu Campaign, puedes añadir hasta cuatro eventos de conversión para el seguimiento.

Utiliza tantos eventos de conversión como sea necesario. Añadir un segundo o tercer evento de conversión enriquece significativamente tus informes. Por ejemplo, para una Campaign dirigida a usuarios inactivos, añadir un evento de conversión secundario junto con el evento de conversión primaria **Starts Session** te ayuda a comprender la eficacia de tu Campaign para hacer que los usuarios vuelvan a tu aplicación.

### Paso 2: Añade los eventos de conversión {#step-2-add-the-conversion-events}

Primero, selecciona el tipo general de evento que te gustaría utilizar:

| Tipo de evento de conversión | Descripción |
|-------------------------|----------------------------|
| **Starts Session** | Un usuario se cuenta como convertido cuando abre cualquiera de las aplicaciones que especifiques (de forma predeterminada, todas las aplicaciones del espacio de trabajo). |
| **Makes Purchase** | Un usuario se cuenta como convertido cuando registra un [evento de compra]({{site.baseurl}}/api/objects_filters/purchase_object). Esto hace seguimiento de cualquier compra de forma predeterminada, o puedes especificar un producto en particular. |
| **Places Order** | Un usuario se cuenta como convertido cuando desencadena el [evento recomendado de eCommerce Order Placed]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events#ecommerce-recommended-events?tab=ecommerce.order_placed). Esto hace seguimiento de cualquier pedido de forma predeterminada, o puedes filtrar por un producto específico.<br><br>El evento "Places Order" se encuentra actualmente en acceso anticipado. Contacta a tu director de cuentas de Braze si te interesa participar en este acceso anticipado. |
| **Performs Custom Event** | Un usuario se cuenta como convertido cuando realiza uno de tus eventos personalizados existentes (no hay valor predeterminado, debes especificar el evento). |
| **Upgrade App** | Un usuario se cuenta como convertido cuando actualiza la versión de la aplicación en cualquiera de las aplicaciones que especifiques (de forma predeterminada, todas las aplicaciones del espacio de trabajo). Braze realiza una comparación numérica de mejor esfuerzo para determinar si el cambio fue una actualización. Las versiones no numéricas se cuentan como conversiones si la versión cambia. |
| **Opens email** | Un usuario se cuenta como convertido cuando abre el correo electrónico (solo para Campaigns de correo electrónico). |
| **Clicks email** | Un usuario se cuenta como convertido cuando hace clic en un enlace dentro del correo electrónico (solo para Campaigns de correo electrónico). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Paso 2: Añade los eventos de conversión" }

{% alert important %}
**Las propiedades anidadas no son compatibles con los eventos de conversión**. No puedes usar propiedades anidadas en eventos de conversión. Por ejemplo, si `product_code` o `product_name` son propiedades anidadas dentro de un array `products` (como `products[].product_code`), no puedes usarlas para verificar si se ha realizado la compra de un producto específico en un evento de conversión.
{% endalert %}

Establece tu plazo de conversión. Esta es la cantidad máxima de tiempo que puede pasar antes de que Braze considere una conversión. Puedes establecer una ventana de hasta 30 días durante la cual Braze contabiliza la conversión si el usuario realiza la acción especificada.

![El tipo de evento de conversión "Makes Purchase" como ejemplo para registrar conversiones de usuarios que realizan cualquier compra. Este tiene un plazo de conversión de 12 horas.]({% image_buster /assets/img_archive/conversion_event_selection.png %})

Después de haber seleccionado tus eventos de conversión, continúa el proceso de creación de la Campaign y comienza a enviarla.

### Paso 3: Consulta tus resultados {#step-3-view-your-results}

Ve a la página **Details** para ver los detalles de cada evento de conversión asociado con la Campaign que creaste. Independientemente de los eventos de conversión seleccionados, también puedes ver los ingresos totales atribuidos a esta Campaign específica, así como a variantes específicas, durante la ventana del evento de conversión primaria.

{% alert note %}
Si no seleccionas ningún evento de conversión durante la creación de la Campaign, el tiempo se establece de forma predeterminada en tres días.
{% endalert %}

Además, para mensajes multivariantes, puedes ver el número de conversiones y los porcentajes de conversión de tu grupo de control y de cada variante.

![Cuatro eventos de conversión que hacen seguimiento de conversiones en función de cuándo se realizó una compra en un plazo de tres horas, se realizó una compra en un plazo de dos horas, se inició una sesión en un plazo de 30 minutos y se inició una sesión en un plazo de 25 minutos.]({% image_buster /assets/img_archive/conversion_event_details.png %})

## Tasas de conversión del paso en Canvas frente a la variante {#canvas-step-versus-variant-conversion-rates}

Es habitual que el recuento total de conversiones de una variante en Canvas sea superior a la suma de los recuentos de conversiones de sus pasos individuales. Esto ocurre porque las conversiones se rastrean de forma diferente a nivel de variante y a nivel de paso:

- Las conversiones de variante se contabilizan en cuanto el usuario entra en la variante.
- Las conversiones de paso se contabilizan solo después de que el mensaje del paso se envíe al usuario.

Esto significa que cualquier usuario que entre en el Canvas y realice el evento de conversión antes de recibir un paso contará para el total de la variante, pero no para ningún paso.

Los siguientes escenarios también pueden provocar esta discrepancia:

- **El usuario abandona el Canvas antes de recibir ningún paso.** Si un usuario entra en el Canvas pero lo abandona (por ejemplo, debido a un filtro o a una discrepancia de audiencia) antes de que se envíe ningún mensaje, una conversión que realice seguirá contabilizándose a nivel de variante, pero no a nivel de paso.
- **El paso se dirige a un subconjunto de usuarios.** Si un paso está configurado para enviar solo a una plataforma específica (como móvil), los usuarios de otras plataformas (como Web) pueden seguir entrando en el Canvas y convertir. Dado que esos usuarios nunca reciben el mensaje del paso, la conversión no se contabiliza a nivel de paso, solo a nivel de variante.

Para más información sobre los análisis de Canvas, consulta [Medir y probar con análisis de Canvas]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics).