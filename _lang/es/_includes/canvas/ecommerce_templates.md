{% tabs %}
{% tab Abandoned browse %}

### Navegación abandonada {#abandoned-browse}

Utiliza la plantilla **Navegación abandonada** para promover la interacción con los usuarios que han navegado por los productos, pero no los han añadido a su carrito ni han realizado un pedido.

![Plantilla de Canvas "Navegación abandonada" aplicada con "Reglas de entrada" expandidas.]({% image_buster /assets/img_archive/abandoned_browse.png %})

#### Configuración {#setup}

En la página de Canvas, selecciona **Use a Canvas Template** > **Braze templates** y, a continuación, aplica la plantilla **Abandoned browse**.

##### Configuración predeterminada {#default-settings}

Los siguientes ajustes están preconfigurados en tu Canvas:
- Conceptos básicos
    - Nombre del Canvas: **Abandoned browse**
    - Evento de conversión: `ecommerce.order placed`
        - Fecha límite de conversión: 3 días
- Horario de entrada
    - Basado en la acción cuando un usuario realiza el evento `ecommerce.product_viewed`
    - La hora de inicio es cuando creas la plantilla de Canvas<br><br>!["Opciones basadas en acciones" para el Canvas.]({% image_buster /assets/img/ecommerce/abandoned_browse_entry.png %})<br><br>
- Audiencia objetivo
    - Audiencia de entrada
        - El correo electrónico **no está en blanco**
        - También puedes modificar los criterios de audiencia de entrada para adaptarlos a las necesidades de tu empresa
    - Controles de entrada
        - Los usuarios son elegibles para volver a entrar en este Canvas una vez que se haya completado la duración total del Canvas
    - Criterios de salida
        - Realiza `ecommerce.cart_updated`, `ecommerce.checkout_started` o `ecommerce.order_placed`<br><br>![Controles de entrada y criterios de salida para el Canvas.]({% image_buster /assets/img/ecommerce/abandoned_browse_entry_exit.png %})<br><br>
- Ajustes de envío
    - Usuarios que están suscritos o que han dado su consentimiento
- Paso de retraso
    - 1 hora de retraso
- Paso de mensaje
    - Revisa la plantilla de correo electrónico y el bloque HTML con un ejemplo de plantilla Liquid para añadir productos a tu mensaje en la plantilla prediseñada. Si utilizas tu propia plantilla de correo electrónico, también puedes consultar las [variables Liquid](#message-personalization), como se muestra en la siguiente sección.

#### Personalización de productos de navegación abandonada para correos electrónicos {#abandoned-browse-product-personalization-for-emails}

A continuación se muestra un ejemplo de cómo añadir un bloque de producto HTML a tu correo electrónico de navegación abandonada.

{% raw %}
```java
<table aria-label="Abandoned browse product personalization for emails" style="width:100%">
  <tr>
    <th><img src="{{context.${image_url}}}" width="200" height="200"><img></th>
    <th align="left">
      <ul style="list-style-type: none">
        <li>Item: {{context.${product_name}}}</li>
        <li>Price: ${{context.${price}}}</li>
      </ul>
    </th>
  </tr>
</table>
```
{% endraw %}

##### URL del producto {#product-url}

{% raw %}
```liquid
{{context.${product_url}}}
```
{% endraw %}

{% endtab %}
{% tab Abandoned cart %}

### Carrito abandonado {#abandoned-cart}

Utiliza la plantilla **Carrito abandonado** para cubrir posibles pérdidas de ventas de clientes que añadieron productos a su carrito pero no continuaron con el proceso de pago ni realizaron un pedido.

![Plantilla de Canvas "Carrito abandonado" aplicada con "Reglas de entrada" expandidas.]({% image_buster /assets/img_archive/abandoned_cart.png %})

#### Configuración

En la página de Canvas, selecciona **Use a Canvas Template** > **Braze templates** y, a continuación, aplica la plantilla **Abandoned cart**.

##### Configuración predeterminada

Los siguientes ajustes están preconfigurados en tu Canvas:
- Conceptos básicos
    - Nombre del Canvas: **Abandoned cart**
    - Evento de conversión: `ecommerce.order_placed`
        - Fecha límite de conversión: 3 días
- Horario de entrada
    - Desencadenador basado en acciones cuando un usuario desencadena el evento **Perform Cart Updated Event** (ubicado en el menú desplegable)
    - La hora de inicio es cuando creas la plantilla de Canvas<br><br>!["Opciones basadas en acciones" para el Canvas.]({% image_buster /assets/img/ecommerce/abandoned_cart_entry.png %})<br><br>
- Público objetivo
    - Audiencia de entrada
        - Ha utilizado estas aplicaciones **más de 0** veces
        - El correo electrónico **no está en blanco**
    - Controles de entrada
        - Los usuarios vuelven a ser elegibles inmediatamente para la entrada en Canvas
    - Criterios de salida
        - Realiza `ecommerce.cart_updated`, `ecommerce.checkout_started` o `ecommerce.order_placed`<br><br>![Controles de entrada y criterios de salida para el Canvas.]({% image_buster /assets/img/ecommerce/abandoned_cart_entry_exit.png %})<br><br>
- Ajustes de envío
    - Usuarios que están suscritos o que han dado su consentimiento
- Paso de retraso
     - 4 horas de retraso
- Paso de mensaje
    - Revisa la plantilla de correo electrónico y el bloque HTML con un ejemplo de plantilla Liquid para añadir productos a tu mensaje en la plantilla prediseñada. Si utilizas tu propia plantilla de correo electrónico, también puedes consultar las [variables Liquid](#message-personalization), como se muestra en la siguiente sección.

#### Cómo funciona la lógica de reentrada del carrito abandonado {#how-abandoned-cart-re-entry-logic-works}

Cuando un usuario inicia el proceso de pago, su carrito se marca como `checkout_started`. A partir de ese momento, cualquier actualización posterior del carrito con el mismo ID de carrito no permitirá al usuario volver a entrar en el recorrido de usuario del carrito abandonado.

1. Cuando un usuario añade un artículo a su carrito, entra en el Canvas.
2. Cada vez que añade o actualiza artículos, vuelve a entrar en el Canvas, lo que mantiene actualizados los datos de su carrito y la mensajería.
3. Cuando el usuario inicia el proceso de pago, su carrito se etiqueta como `checkout_started` y sale del Canvas.
4. Las futuras actualizaciones del carrito que utilicen el mismo ID de carrito no desencadenarán una nueva entrada, ya que este carrito ya ha pasado a la fase de pago.

Cuando los usuarios pasan al recorrido de usuario de pago, se les dirige al [Canvas de pago abandonado](#abandoned-checkout), diseñado para usuarios que se encuentran en una fase más avanzada del proceso de compra.

#### Personalización de productos del carrito abandonado para correos electrónicos {#abandoned-cart-checkout}

Los recorridos de usuario de carrito abandonado requieren una etiqueta de Liquid `shopping_cart` especial para la personalización de productos.

A continuación se muestra un ejemplo de cómo añadir un bloque HTML con tu etiqueta de Liquid `shopping_cart` para añadir productos a tu correo electrónico.

{% raw %}
```java
<table aria-label="Abandoned cart product personalization for emails #abandoned-cart-checkout" style="width:100%">
  {% shopping_cart {{context.${cart_id}}} %}
  {% for item in shopping_cart.products %}
  {% catalog_items <add_your_catalog_name> {{item.variant_id}} %}
  <tr>
    <th><img src="{{ items[0].variant_image_url }}" width="200" height="200"><img></th>
    <th align="left">
      <ul style="list-style-type: none">
        <li>Item: {{ item.product_name }}</li>
        <li>Price: ${{ item.price }}</li>
        <li>Quantity: ${{ item.quantity }}</li>
        <li>Variant ID: {{ item.variant_id }}</li>
        <li>Product URL:{{ item.product_url }}</li>
        <li>SKU: {{ item.metadata.sku }}</li>
      </ul>
    </th>
  </tr>
  {% endfor %}
</table>
```
{% endraw %}

{% alert note %}
Si utilizas Shopify, añade el nombre de tu catálogo para obtener la URL de la imagen de la variante.
{% endalert %}

##### URL del carrito HTML {#html-cart-url}

Si deseas redirigir a los usuarios a su carrito, puedes añadir una propiedad de evento anidada bajo el objeto de metadatos, como por ejemplo:

{% raw %}
```liquid
{{context.${metadata}.cart_url}}
```
{% endraw %}

Si utilizas Shopify, crea la URL de tu carrito utilizando esta plantilla Liquid:

{% raw %}
```liquid
{{context.${source}}}/checkouts/cn/{{context.${cart_id}}}
```
{% endraw %}

{% endtab %}
{% tab Abandoned checkout %}

### Pago abandonado {#abandoned-checkout}

Utiliza la plantilla **Pago abandonado** para dirigirte a los clientes que iniciaron el proceso de pago pero lo abandonaron antes de realizar el pedido.

![Plantilla de Canvas "Pago abandonado" aplicada con "Reglas de entrada" expandidas.]({% image_buster /assets/img_archive/abandoned_checkout.png %})

#### Configuración

En la página de Canvas, selecciona **Use a Canvas Template** > **Braze templates** y, a continuación, aplica la plantilla **Abandoned checkout**.

##### Configuración predeterminada

Los siguientes ajustes están preconfigurados en tu Canvas:

- Conceptos básicos
    - Nombre del Canvas: **Abandoned checkout**
    - Evento de conversión: `ecommerce.order_placed`
        - Fecha límite de conversión: 3 días
- Horario de entrada
    - Desencadenador basado en acciones cuando un usuario realiza el evento `ecommerce.checkout_started`
    - La hora de inicio es cuando creas la plantilla de Canvas<br><br>!["Opciones basadas en acciones" para el Canvas.]({% image_buster /assets/img/ecommerce/abandoned_checkout_entry.png %})
- Audiencia objetivo
    - Audiencia de entrada
        - Ha utilizado estas aplicaciones **más de 0** veces
        - El correo electrónico **no está en blanco**
    - Controles de entrada
        - Los usuarios vuelven a ser elegibles inmediatamente para la entrada en Canvas
        - Criterios de salida
            - Realiza los eventos `ecommerce.order_placed`<br><br>![Controles de entrada y criterios de salida para el Canvas.]({% image_buster /assets/img/ecommerce/abandoned_checkout_entry_exit.png %})<br><br>
- Ajustes de envío
    - Usuarios que están suscritos o que han dado su consentimiento
- Paso de retraso
    - 4 horas de retraso
- Paso de mensaje
    - Revisa la plantilla de correo electrónico y el bloque HTML con un ejemplo de plantilla Liquid para añadir productos a tu mensaje en la plantilla prediseñada. Si utilizas tu propia plantilla de correo electrónico, también puedes consultar las [variables Liquid](#message-personalization), como se muestra en la siguiente sección.

#### Personalización del pago abandonado para correos electrónicos {#abandoned-checkout-personalization-for-emails}

Los recorridos de usuario de pago abandonado requieren una etiqueta de Liquid `shopping_cart` especial para la personalización de productos.

A continuación se muestra un ejemplo de cómo añadir un bloque HTML con tu etiqueta de Liquid `shopping_cart` para añadir productos a tu correo electrónico.

{% raw %}
```java
<table aria-label="Abandoned checkout personalization for emails" style="width:100%">
  {% shopping_cart {{context.${cart_id}}} :abort_if_not_abandoned false %}
  {% for item in shopping_cart.products %}
  {% catalog_items <add_your_catalog_name> {{item.variant_id}} %}
  <tr>
    <th><img src="{{ items[0].variant_image_url }}" width="200" height="200"><img></th>
    <th align="left">
      <ul style="list-style-type: none">
        <li>Item: {{ item.product_name }}</li>
        <li>Price: ${{ item.price }}</li>
        <li>Quantity: ${{ item.quantity }}</li>
        <li>Variant ID: {{ item.variant_id }}</li>
        <li>Product URL:{{ item.product_url }}</li>
        <li>SKU: {{ item.metadata.sku }}</li>
      </ul>
    </th>
    {% endfor %}
</table>
```
{% endraw %}

##### `abort_if_not_abandoned` {#abort-if-not-abandoned}

El parámetro `abort_if_not_abandoned` es específico del caso de uso de pago abandonado y se utiliza únicamente con la etiqueta de Liquid `shopping_cart` en combinación con el evento `ecommerce.checkout_started`.

| Valor | Comportamiento |
| ----- | -------- |
| `true` (predeterminado) | El mensaje se cancela si el carrito no ha sido abandonado, es decir, si el usuario ya ha completado su pedido. |
| `false` | El mensaje se envía aunque el carrito no esté en estado de abandono, lo que permite que el correo electrónico incluya los detalles del carrito independientemente del estado actual del proceso de pago. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="abortifnotabandoned #abort-if-not-abandoned" }

Establece `abort_if_not_abandoned` en `false` cuando quieras enviar el recordatorio de pago independientemente de si el carrito todavía se considera abandonado en el momento del envío. Si omites el parámetro o lo estableces en `true`, Braze cancela el mensaje para los usuarios que ya han completado su compra.

##### URL de pago {#checkout-url}

{% raw %}
```liquid
{{context.${metadata}.checkout_url}}
```
{% endraw %}

{% endtab %}
{% tab Order confirmation and feedback survey %}

### Confirmación de pedido y cuestionario de satisfacción {#order-confirmation-and-feedback-survey}

Utiliza la plantilla **Order confirmation & feedback survey** para confirmar los pedidos realizados con éxito y mejorar la satisfacción del cliente.

![Plantilla de Canvas "Confirmación de pedido" aplicada con "Reglas de entrada" expandidas.]({% image_buster /assets/img_archive/order_confirmation_feedback.png %})

#### Configuración

En la página de Canvas, selecciona **Use a Canvas Template** > **Braze templates** y, a continuación, aplica la plantilla **Order confirmation & feedback survey**.

##### Configuración predeterminada

Los siguientes ajustes están preconfigurados en tu Canvas:

- Conceptos básicos
    - Nombre del Canvas: **Order confirmation with feedback survey**
    - Evento de conversión: `ecommerce.session_start`
        - Fecha límite de conversión: 10 días
- Horario de entrada
    - Desencadenador basado en acciones cuando un usuario realiza el evento `ecommerce.cart_updated`
    - La hora de inicio es cuando creas la plantilla de Canvas<br><br>!["Opciones basadas en acciones" para el Canvas.]({% image_buster /assets/img/ecommerce/feedback_entry.png %})<br><br>
- Audiencia objetivo
    - Audiencia de entrada
        - Ha utilizado estas aplicaciones **más de 0** veces
        - El correo electrónico **no está en blanco**
    - Controles de entrada
        - Los usuarios vuelven a ser elegibles inmediatamente para la entrada en Canvas
    - Criterios de salida
        - No aplicable<br><br>![Filtros adicionales y controles de entrada para el Canvas.]({% image_buster /assets/img/ecommerce/feedback_entry_exit.png %})<br><br>
- Ajustes de envío
    - Usuarios que están suscritos o que han dado su consentimiento
- Paso de mensaje
    - Revisa la plantilla de correo electrónico y el bloque HTML con un ejemplo de plantilla Liquid para añadir productos a tu mensaje en la plantilla prediseñada. Si utilizas tu propia plantilla de correo electrónico, también puedes consultar las [variables Liquid](#message-personalization), como se muestra en la siguiente sección.

#### Personalización de la confirmación de pedido para correos electrónicos {#order-confirmation-personalization-for-emails}

A continuación se muestra un ejemplo de cómo añadir un bloque de producto HTML a la confirmación de pedido una vez que se ha realizado el pedido.

{% raw %}
```json
<table aria-label="Order confirmation personalization for emails" style="width:100%">
  {% for item in {{context.${products}}} %}
  {% catalog_items <add_your_catalog_name> {{item.variant_id}} %}
  <tr>
    <th><img src="{{ items[0].variant_image_url }}" width="200" height="200" /></th>
    <th align="left">
      <ul style="list-style-type: none">
        <li>Item: {{item.product_name}}</li>
        <li>Price: {{item.price}}</li>
        <li>Quantity: {{item.quantity}}</li>
      </ul>
    </th>
  </tr>
  {% endfor %}
</table>
```
{% endraw %}

##### URL del estado del pedido {#order-status-url}

{% raw %}
```liquid
{{context.${metadata}.order_status_url}}
```
{% endraw %}

{% endtab %}
{% endtabs %}