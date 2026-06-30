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

> Un evento de conversión es un tipo de métrica de éxito que rastrea si un destinatario de tu mensajería realiza una acción de alto valor en un período de tiempo determinado después de recibir tu interacción. Usa estos eventos para asegurarte de que estás recopilando información relevante y útil que luego puedes utilizar para obtener información sobre tu campaña o Canvas.

## Cómo funciona {#how-it-works}

Para una campaña personalizada de festividades dirigida a usuarios activos, un evento de conversión de **Iniciar una sesión** dentro de dos o tres días puede ser apropiado, ya que te permite tener una idea de la interacción de los usuarios al recibir tu mensaje. También puedes seleccionar eventos adicionales como **Realiza un pedido**, **Actualiza la aplicación** o cualquiera de tus eventos personalizados como eventos de conversión.

### ¿Cuándo comienza el seguimiento de conversiones? {#when-does-conversion-tracking-begin}

{% tabs %}
{% tab Campaign %}

El seguimiento de conversiones comienza cuando un usuario recibe la campaña o entra en el grupo de control de la campaña. Recibir un mensaje y la asignación a una variante generalmente ocurren al mismo tiempo. Para campañas de mensajes dentro de la aplicación, el seguimiento de conversiones comienza cuando Braze registra una impresión.

{% endtab %}
{% tab Canvas %}

El seguimiento de conversiones comienza cuando un usuario entra al Canvas. Para los pasos en Canvas, las conversiones se atribuyen mientras el usuario está activo en ese paso. Cuando el usuario avanza a otro paso, el seguimiento de conversiones se detiene para el paso anterior y comienza para el siguiente paso.

Mientras un usuario está en un paso de retraso u otro paso sin mensaje, las conversiones que ocurren durante esa espera aún se atribuyen al último paso de mensaje recibido hasta que el usuario recibe otro paso de mensaje. Después de que el usuario recibe el último paso de mensaje en su ruta, las conversiones aún pueden registrarse hasta el plazo de conversión (contado desde la entrada al Canvas), incluso si no hay más pasos de mensaje.

{% endtab %}
{% endtabs %}

{% alert tip %}
Para más información sobre conversiones, consulta nuestro [curso de Braze Learning](https://learning.braze.com/campaign-setup-delivery-targeting-conversions) sobre configuración de campañas.
{% endalert %}

### Reglas de seguimiento de conversiones {#conversion-tracking-rules}

Los eventos de conversión atribuyen las acciones de los usuarios a un punto de interacción. En general, mientras una ventana de conversión está abierta, un usuario convierte como máximo una vez por evento de conversión para esa campaña o Canvas. Si realiza la misma acción de conversión más de una vez antes del plazo (por ejemplo, dos compras), Braze solo cuenta una conversión para ese evento. Las campañas multicanal pueden registrar una oportunidad de conversión separada para cada canal de mensajería, lo que puede producir tasas de conversión superiores al 100 % cuando comparas los recuentos de conversiones con los destinatarios únicos (ver más abajo).

Ten en cuenta lo siguiente sobre cómo Braze maneja múltiples conversiones:

- **Campañas de un solo canal**: Las conversiones ocurren por usuario, no por dispositivo. Dentro de un solo canal, un usuario convierte solo una vez por evento de conversión, incluso si un mensaje se envía a múltiples dispositivos. Por ejemplo, si una campaña tiene solo un evento de conversión configurado como "Realiza cualquier compra" y un usuario realiza dos compras separadas dentro del plazo de conversión, Braze cuenta solo una conversión.
- **Campañas multicanal**: Para campañas multicanal, cada canal tiene su propia oportunidad de conversión. Un usuario puede convertir una vez por canal después de recibir un mensaje en ese canal. Esto significa que si un usuario recibe mensajes en múltiples canales (por ejemplo, tanto correo electrónico como push) y realiza la acción de conversión, Braze cuenta una conversión por cada canal, lo que puede resultar en tasas de conversión superiores al 100 %.
- **Pasos de mensaje en Canvas**: Braze atribuye las conversiones que ocurren dentro del plazo de conversión al último paso de mensaje en Canvas que el usuario recibió. Después de que recibe el siguiente paso de mensaje, la atribución se mueve a ese paso. Braze mide esa ventana desde que el usuario entra al Canvas, no desde cada mensaje individual. Las conversiones que ocurren durante los retrasos entre pasos de mensaje cuentan para la atribución del paso de mensaje anterior hasta que el usuario avanza; las conversiones después del último paso de mensaje aún cuentan hasta el plazo de conversión del Canvas.
- Si un usuario realiza un evento de conversión dentro de los plazos de conversión de dos campañas o Canvas separados que recibió, la conversión se registra en ambos.
- Un usuario cuenta como convertido si realizó el evento de conversión específico dentro de la ventana, incluso si no abrió ni hizo clic en el mensaje.

### Evento de conversión primaria {#primary-conversion-event}

El evento de conversión primaria es el primer evento que agregas durante la creación de una campaña o Canvas. Este evento tiene la mayor influencia en tu interacción e informes. Braze usa tu evento de conversión primaria para:

- Calcular la variante de mensaje ganadora en campañas o Canvas [multivariantes]({{site.baseurl}}/user_guide/messaging/ab_testing#multivariate-and-ab-testing).
- Determinar la ventana en la que se calculan los ingresos para la campaña o Canvas.
- Ajustar las distribuciones de mensajes para campañas y Canvas usando [Intelligent Selection]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_selection).

El recuento del evento de conversión primaria es el número de eventos de conversión que ocurrieron. Para campañas multicanal, Braze cuenta las conversiones por canal (como se describe en [Reglas de seguimiento de conversiones](#conversion-tracking-rules)), lo que significa que el recuento de conversiones puede superar el número de usuarios únicos y resultar en tasas de conversión superiores al 100 %. Braze calcula la tasa del evento de conversión primaria dividiendo este recuento entre el número de destinatarios únicos. Braze considera a un usuario como destinatario cuando el mensaje se envía o se muestra, dependiendo del canal. Por ejemplo, en push o correo electrónico, un usuario se convierte en destinatario después de que Braze envía el mensaje. Para mensajes dentro de la aplicación o Content Cards, el usuario debe ver el mensaje para ser considerado destinatario.

{% alert note %}
Si cancelas mensajes usando la etiqueta Liquid `abort`, Braze cancela los mensajes solo para los usuarios que pasan por las variantes. Los mensajes para los usuarios en el grupo de control no se cancelan, lo que puede llevar a porcentajes de conversión sesgados entre variantes y grupos de control. Como solución alternativa, usa la [segmentación]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment) para dirigirte a tus usuarios en la entrada de la campaña y Canvas.
{% endalert %}

## Crear una campaña con seguimiento de conversiones {#creating-a-campaign-with-conversion-tracking}

### Paso 1: Configura tu campaña {#step-1-set-up-your-campaign}

[Crea una campaña]({{site.baseurl}}/user_guide/messaging/campaigns/creating_campaign) para el canal de mensajería que desees. Después de configurar los mensajes y la planificación de tu campaña, puedes agregar hasta cuatro eventos de conversión para el seguimiento.

Usa tantos eventos de conversión como sea necesario. Agregar un segundo o tercer evento de conversión enriquece significativamente tus informes. Por ejemplo, para una campaña dirigida a usuarios inactivos, agregar un evento de conversión secundario junto con el evento de conversión primaria **Inicia sesión** te ayuda a entender qué tan efectiva es tu campaña para traer a los usuarios de vuelta a tu aplicación.

### Paso 2: Agrega los eventos de conversión {#step-2-add-the-conversion-events}

Primero, selecciona el tipo general de evento que te gustaría usar:

| Tipo de evento de conversión | Descripción |
|-------------------------|----------------------------|
| **Inicia sesión** | Un usuario se cuenta como convertido cuando abre cualquiera de las aplicaciones que especifiques (por defecto, todas las aplicaciones en el espacio de trabajo). |
| **Realiza una compra** | Un usuario se cuenta como convertido cuando registra un [evento de compra]({{site.baseurl}}/api/objects_filters/purchase_object). Esto rastrea cualquier compra por defecto, o puedes especificar un producto en particular. |
| **Realiza un pedido** | Un usuario se cuenta como convertido cuando desencadena el [evento recomendado de comercio electrónico Pedido realizado]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events#ecommerce-recommended-events?tab=ecommerce.order_placed). Esto rastrea cualquier pedido por defecto, o puedes filtrar por un producto específico.<br><br>El evento "Realiza un pedido" se encuentra actualmente en acceso anticipado. Ponte en contacto con tu director de cuentas de Braze si estás interesado en participar en este acceso anticipado. |
| **Realiza un evento personalizado** | Un usuario se cuenta como convertido cuando realiza uno de tus eventos personalizados existentes (no hay valor predeterminado, debes especificar el evento). |
| **Actualiza la aplicación** | Un usuario se cuenta como convertido cuando actualiza la versión de la aplicación en cualquiera de las aplicaciones que especifiques (por defecto, todas las aplicaciones en el espacio de trabajo). Braze realiza una comparación numérica de mejor esfuerzo para determinar si el cambio fue una actualización. Las versiones no numéricas se cuentan como conversiones si la versión cambia. |
| **Abre el correo electrónico** | Un usuario se cuenta como convertido cuando abre el correo electrónico (solo para campañas de correo electrónico). |
| **Hace clic en el correo electrónico** | Un usuario se cuenta como convertido cuando hace clic en un enlace dentro del correo electrónico (solo para campañas de correo electrónico). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Paso 2: Agrega los eventos de conversión" }

{% alert important %}
**Las propiedades anidadas no son compatibles con los eventos de conversión**. No puedes usar propiedades anidadas en eventos de conversión. Por ejemplo, si `product_code` o `product_name` son propiedades anidadas dentro de un array `products` (como `products[].product_code`), no puedes usarlas para verificar si se ha realizado una compra de un producto específico en un evento de conversión.
{% endalert %}

Establece tu plazo de conversión. Esta es la cantidad máxima de tiempo que puede pasar antes de que Braze considere una conversión. Puedes establecer una ventana de hasta 30 días durante la cual Braze cuenta la conversión si el usuario realiza la acción especificada.

![El tipo de evento de conversión "Realiza una compra" como ejemplo para registrar conversiones de usuarios que realizan cualquier compra. Tiene un plazo de conversión de 12 horas.]({% image_buster /assets/img_archive/conversion_event_selection.png %})

Después de haber seleccionado tus eventos de conversión, continúa el proceso de creación de la campaña y comienza a enviarla.

### Paso 3: Consulta tus resultados {#step-3-view-your-results}

Ve a la página **Detalles** para ver los detalles de cada evento de conversión asociado con la campaña que creaste. Independientemente de los eventos de conversión que hayas seleccionado, también puedes ver los ingresos totales atribuidos a esta campaña específica, así como a variantes específicas, durante la ventana del evento de conversión primaria.

{% alert note %}
Si no seleccionas ningún evento de conversión durante la creación de la campaña, el tiempo predeterminado es de tres días.
{% endalert %}

Además, para mensajes multivariantes, puedes ver el número de conversiones y los porcentajes de conversión para tu grupo de control y cada variante.

![Cuatro eventos de conversión que rastrean conversiones basándose en cuándo se realizó una compra dentro de tres horas, se realizó una compra dentro de dos horas, se inició una sesión dentro de 30 minutos y se inició una sesión dentro de 25 minutos.]({% image_buster /assets/img_archive/conversion_event_details.png %})