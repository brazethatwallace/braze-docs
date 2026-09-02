---
nav_title: Usar eventos recomendados de comercio electrónico
article_title: Cómo usar eventos de comercio electrónico
page_type: reference
alias: /ecommerce_events/
description: "Aprende a usar los eventos recomendados de comercio electrónico en Braze, incluyendo las características compatibles, métricas clave y mejores prácticas para segmentación, mensajería e informes."
---

# Cómo usar eventos de comercio electrónico {#how-to-use-ecommerce-events}

> Los [eventos recomendados]({{site.baseurl}}/recommended_events) de comercio electrónico usan un esquema compartido a nivel de pedido, lo que permite a Braze construir características confiables sobre tus datos de comercio electrónico, incluyendo perfiles de usuario, segmentación, mensajería, informes y recomendaciones impulsadas por IA. Las secciones de este artículo cubren cómo usar cada capacidad en Braze.<br><br> Consulta [Esquemas de eventos]({{site.baseurl}}/user_guide/data/activation/events/recommended_events#event-schemas) para los requisitos de propiedades y tipos de datos, y [Validación de eventos y solución de problemas]({{site.baseurl}}/user_guide/data/activation/events/recommended_events#event-validation-and-troubleshooting) para saber qué sucede cuando un evento no pasa la validación.

Dado que los eventos de comercio electrónico siguen un esquema predecible, Braze puede construir características confiables sobre ellos, desde el seguimiento de ingresos y plantillas de Canvas prediseñadas hasta recomendaciones impulsadas por IA. Las siguientes secciones te ofrecen un resumen rápido de cada capacidad con enlaces a la documentación completa.

{% alert note %}
Los eventos de comercio electrónico de Braze y sus propiedades de eventos segmentables no cuentan como [puntos de datos]({{site.baseurl}}/user_guide/data/infrastructure/data_points).
{% endalert %}

<a id="transactions-tab" aria-hidden="true"></a>

## Pestaña Commerce {#commerce-tab}

La pestaña **Commerce** en cada perfil de usuario combina dos módulos: **Order activity** (métricas calculadas de ingresos y pedidos) y **Active cart** (el carrito más reciente de los eventos `ecommerce.cart_updated`).

### Actividad de pedidos {#order-activity}

El módulo **Order activity** muestra tres métricas calculadas que se actualizan en tiempo real a medida que se procesan los eventos. El modelo a nivel de pedido de estos cálculos separa claramente los precios de los productos del valor total del pedido.

{% alert note %}
Los eventos recomendados de comercio electrónico no se muestran dentro de la sección **Purchase history** de la pestaña **Commerce**. El historial de compras se llena con los eventos de compra heredados. Usa las métricas de la siguiente tabla para los ingresos y la actividad de pedidos de los eventos recomendados.
{% endalert %}

| Métrica | Fórmula |
| ----- | ----- |
| Ingresos totales | suma (`order_placed.total_value`) − suma (`order_refunded.total_value`) |
| Total de pedidos | conteo (distintos `order_placed`) − conteo (distintos `order_cancelled`) |
| Valor total de reembolsos | suma (`order_refunded.total_value`) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Métricas de actividad de pedidos" }

### Carrito activo {#active-cart}

El módulo **Active cart** muestra el carrito más reciente en el perfil de usuario. Esta vista es especialmente útil mientras realizas pruebas. Puedes usarla para confirmar el contenido del carrito, validar recorridos basados en el carrito o verificar que los eventos `ecommerce.cart_updated` están actualizando el perfil como esperas.

**Active cart** incluye lo siguiente:

- **Cart ID** — Identificador del carrito que recibió por última vez un evento `ecommerce.cart_updated`.
- **Last updated** — Marca de tiempo de la actualización de carrito más reciente.
- **Total cart value** — Valor total de los artículos en el carrito actual.
- **View products** — Un enlace para abrir la lista de productos en el carrito (hasta 50 productos).

## Orquestación de eCommerce {#ecommerce-orchestration}

### Segmentación {#segmentation}

Braze ofrece tres formas de segmentar usuarios basándose en datos de eCommerce:

- **Filtros de eCommerce:** Usa la categoría **eCommerce** en el segmentador, que contiene filtros basados en eventos recomendados de eCommerce (como **Last Order Placed**, **Total Revenue** y **Average Order Value**). Para una lista completa de filtros disponibles, consulta [Filtros de segmento]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters).
- **Filtros de eventos personalizados:** Dado que los eventos de eCommerce se comportan como eventos personalizados, todos los filtros de eventos personalizados existentes funcionan de inmediato. Por ejemplo, puedes filtrar por "Ha realizado el evento personalizado `ecommerce.order_placed` más de X veces" o "Primera vez que realizó el evento personalizado `ecommerce.order_placed`".
- **Extensiones de segmento:** Para segmentar con propiedades de eventos anidados, incluyendo el array de productos anidados o las propiedades de los objetos de metadatos, usa las [extensiones de segmento]({{site.baseurl}}/user_guide/audience/segments/segment_extension) con el filtrado de propiedades de eventos anidados. Esto te permite crear audiencias como "usuarios que compraron el producto SKU-123 en los últimos 90 días" o combinar criterios en diferentes propiedades del mismo pedido.

{% alert important %}
Las extensiones de segmento para eventos recomendados de eCommerce son una característica de pago y en acceso anticipado. Si te interesa participar en el acceso anticipado, ponte en contacto con tu CSM or administrador de éxito de cliente or administrador de éxito de cliente. Confirma que tu plan incluye acceso antes de recomendar la segmentación por propiedades anidadas a tu equipo.
{% endalert %}

### Desencadenamiento {#triggering}

Puedes usar desencadenadores de eventos personalizados realizados con eventos de eCommerce en todo Braze, igual que con otros eventos personalizados. Para flujos de carrito abandonado, usa el desencadenador **Perform Cart Updated Event** para capturar correctamente las actualizaciones del carrito.

Además, Braze ofrece un desencadenador dedicado **Places Order**, que te permite iniciar recorridos o realizar acciones basadas en cualquier pedido realizado, o en pedidos que incluyan un producto específico. Puedes filtrar este desencadenador por nombre de producto, `product_id` o `variant_id` para dirigirte a escenarios de compra específicos. Para más información, consulta [Entrega basada en acciones]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery).

![Desencadenador Places Order con una opción seleccionada para realizar cualquier pedido.]({% image_buster /assets/img/recommended_events/places_order_trigger.png %})

### Personalización con Liquid {#liquid-personalization}

Los eventos de eCommerce son compatibles con la [personalización con Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid) del mismo modo que los eventos personalizados; puedes hacer referencia a las propiedades del evento directamente en tu mensajería. Para incorporar imágenes de productos, precios u otros datos de catálogo en tus mensajes, une tu catálogo con el evento usando `product_id` o `variant_id` como identificador de enlace. La etiqueta de Liquid {% raw %}`{% shopping_cart %}`{% endraw %} te permite recorrer el contenido actual del carrito de un usuario para recordatorios de carrito abandonado, avisos de pago o confirmaciones de pedido. Para ver ejemplos de código listos para usar, consulta [Ejemplos de eCommerce]({{site.baseurl}}/ecommerce_use_cases).

Como alternativa sin código, los [bloques de producto en arrastrar y soltar]({{site.baseurl}}/user_guide/messaging/design_and_edit/product_blocks) están disponibles en el programa de acceso anticipado.

### Plantillas de Canvas para eCommerce {#ecommerce-canvas-templates}

Braze ofrece plantillas de Canvas listas para usar, preconfiguradas con eventos recomendados de eCommerce como criterios de entrada, salida y conversión, para que puedas lanzar flujos de ciclo de vida sin configuración personalizada. Cada plantilla incluye diseños de correo electrónico de arrastrar y soltar y es compatible con bloques de producto de arrastrar y soltar (actualmente en acceso anticipado). Para ejemplos de uso detallados y ejemplos de Liquid, consulta [Ejemplos de eCommerce]({{site.baseurl}}/ecommerce_use_cases).

Estas plantillas cubren los flujos de ciclo de vida de eCommerce más comunes. Úsalas como punto de partida y luego personaliza los tiempos, canales y creativos para tu audiencia.

{% tabs %}
{% tab Navegación abandonada %}

Vuelve a captar a los usuarios que vieron un producto pero no lo añadieron al carrito.

Usa esta plantilla cuando quieras traer de vuelta a los navegantes para que consideren productos que vieron recientemente pero sobre los que no actuaron.

| Configuración | Valor |
| --- | --- |
| Evento de entrada | `ecommerce.product_viewed` |
| Eventos de salida | `ecommerce.product_viewed`, `ecommerce.cart_updated`, `ecommerce.checkout_started`, Placed Order |
| Evento de conversión | Placed Order |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Plantillas de Canvas para eCommerce" }

{% endtab %}
{% tab Carrito abandonado %}

Recupera a los usuarios que añadieron artículos a su carrito pero no iniciaron el proceso de pago.

Usa esta plantilla cuando quieras recordar a los usuarios los artículos en su carrito y dirigirlos de vuelta para completar el pago.

| Configuración | Valor |
| --- | --- |
| Evento de entrada | `ecommerce.cart_updated` |
| Eventos de salida | `ecommerce.cart_updated`, `ecommerce.checkout_started`, Placed Order |
| Evento de conversión | Placed Order |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Plantillas de Canvas para eCommerce" }

{% alert tip %}
El evento `ecommerce.cart_updated` es compatible con el reemplazo completo del carrito (cada evento puede describir el carrito completo) o actualizaciones incrementales usando los valores `add` y `remove` para la propiedad opcional `action`. Elige un enfoque por carrito y evita mezclar actualizaciones de carrito de reemplazo e incrementales para el mismo `cart_id`. Usa la etiqueta de Liquid {% raw %}`{% shopping_cart %}`{% endraw %} en tu mensaje para mostrar dinámicamente el contenido actual del carrito en el momento del envío.
{% endalert %}

{% endtab %}
{% tab Pago abandonado %}

Recupera a los usuarios que iniciaron el proceso de pago pero no completaron la compra.

Usa esta plantilla cuando quieras recuperar compras en la etapa de mayor intención del embudo.

| Configuración | Valor |
| --- | --- |
| Evento de entrada | `ecommerce.checkout_started` |
| Evento de salida | Placed Order |
| Evento de conversión | Placed Order |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Plantillas de Canvas para eCommerce" }

{% endtab %}
{% tab Confirmación de pedido y cuestionario %}

Confirma una compra exitosa y hace seguimiento con un cuestionario de opinión para impulsar la recopilación de reseñas y la participación posterior a la compra.

Usa esta plantilla cuando quieras optimizar la comunicación posterior a la compra y recopilar comentarios de los clientes en un solo flujo de trabajo.

| Configuración | Valor |
| --- | --- |
| Evento de entrada | `ecommerce.order_placed` |
| Evento de conversión | Start Session o `ecommerce.product_viewed` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Plantillas de Canvas para eCommerce" }

{% endtab %}
{% endtabs %}

#### Personalizar plantillas {#customize-templates}

Estas plantillas están diseñadas como punto de partida. Las personalizaciones más comunes incluyen:
  - **Personalizar el correo electrónico:** Cada plantilla incluye un correo electrónico preconfigurado creado con el editor de arrastrar y soltar, totalmente editable para adaptarse a tu marca y contenido.
  - **Añadir canales:** Combina el correo electrónico con push, servicio de mensajes cortos o mensajes dentro de la aplicación para un refuerzo multicanal.
  - **Añadir retrasos y divisiones de decisiones:** Divide a los usuarios por comportamiento (por ejemplo, carrito de alto valor frente a carrito de bajo valor) o periodos de espera entre mensajes.
  - **Cambiar el creativo:** Reemplaza la plantilla de correo electrónico incluida con el estilo visual de tu marca.
  - **Usar bloques de producto:** Usa bloques de producto de arrastrar y soltar (en el programa de acceso anticipado) para representar dinámicamente el contenido de carritos abandonados o productos visitados sin escribir Liquid personalizado.

Para estrategias de ciclo de vida más avanzadas, incluyendo ejemplos de personalización con Liquid, consulta [Ejemplos de eCommerce]({{site.baseurl}}/ecommerce_use_cases).

## Informes de eCommerce {#ecommerce-reporting}

Los eventos recomendados de eCommerce potencian las mismas superficies de ingresos que los clientes ya utilizan hoy en día. Cuando tu integración está enviando eventos de eCommerce, los siguientes informes incluyen los ingresos de eCommerce automáticamente:

| Informe                                      | Qué muestra                             |
|---------------------------------------------|-------------------------------------------|
| Informe de ingresos                              | Ingresos totales, ingresos diarios promedio, compras diarias e ingresos por usuario a lo largo del tiempo en todas las fuentes para el rango de fechas y las aplicaciones seleccionadas.                                                                                     |
| Panel de ingresos de atribución de último toque     | Ingresos atribuidos a la última Campaign o Canvas con la que un usuario interactuó antes de realizar un pedido. Los eventos de contacto incluyen clics en correo electrónico, aperturas de push, clics en tarjetas de contenido, clics en mensajes dentro de la aplicación y clics en enlaces cortos de servicio de mensajes cortos o WhatsApp. |
| Análisis de Campaign y Canvas                | Ingresos totales atribuidos a una Campaign o Canvas específica dentro de la ventana de conversión primaria.                                                                                   |
| Informe de conversiones                          | Ingresos vinculados a eventos de conversión en Campaigns y Canvas.<br> **Nota:** Para contabilizar los ingresos de `ecommerce.order_placed`, la Campaign o Canvas debe usar el tipo de evento de conversión "Place Order" como su evento de conversión.                                                                                    |
| Información del segmento                            | Comparaciones de ingresos entre segmentos en el panel de información del segmento.                                                               |
| Generador de informes                              | Métricas de ingresos en informes personalizados creados en el generador de informes.                                                                                  |
| Dashboard Builder                           | Métricas de ingresos en paneles personalizados creados en Dashboard Builder.                                                                                  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Informes de eCommerce" }

Para los campos calculados no relacionados con el usuario (por ejemplo, los ingresos de una Campaign o Canvas), los ingresos se calculan de la misma manera en todos los informes: `price` multiplicado por `quantity` por producto en el pedido, sumados a través de los productos en cada evento `order_placed`.

{% alert note %}
Los cálculos de ingresos limitan las cantidades individuales de productos a 1000 unidades por pedido. Si falta el campo de cantidad para un producto, se establece de forma predeterminada en una unidad. El evento original `ecommerce.order_placed` conserva la cantidad completa que enviaste; solo el cálculo de ingresos aplica el límite.<br><br>
Si estás migrando de eventos de compra heredados a `ecommerce.order_placed`, coordina con tu equipo de cuenta de Braze antes de realizar cualquier cambio en la integración. Durante el periodo de transición, envía tanto los eventos de compra heredados como los eventos `ecommerce.order_placed` para confirmar que se están activando correctamente y para preparar tus Campaigns, Canvas y segmentos activos para migrar al nuevo evento. Tu equipo de cuenta puede ayudarte a planificar la transición para cambiar los informes de ingresos de los eventos de compra heredados a `ecommerce.order_placed`.
{% endalert %}

### BrazeAI<sup>TM</sup>

[Predictive Events]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events), [Predictive Churn]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn) y [recomendaciones de artículos]({{site.baseurl}}/user_guide/brazeai/item_recommendations) admiten eventos de eCommerce como eventos objetivo y señales, y tienen una opción dedicada "Order Placed". El esquema estandarizado hace que estos modelos sean más fiables porque los datos son consistentes en toda tu base de usuarios.

### Exportar datos {#export-data}

Braze ofrece varias formas de exportar datos de eventos de eCommerce para su uso en tu almacén de datos, herramientas de BI o sistemas posteriores. Los eventos recomendados de eCommerce se exportan a través de los mismos canales que el resto de tus datos de eventos.

| Ruta de exportación                         | Qué incluye                                                                                                                                                                                 |
|------------------------------------- |------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents)                            | Los eventos de eCommerce se transmiten como eventos personalizados; busca en el espacio de nombres `ecommerce.*` para encontrarlos. Los productos de cada pedido están disponibles como compras.                                                |
| [Snowflake Data Sharing]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/data_sharing)               | Los eventos de eCommerce se comparten como eventos personalizados; busca en el espacio de nombres `ecommerce.*` para encontrarlos. Los productos de cada pedido están disponibles en la tabla de compras.                                   |
| [Exportar datos de segmento a CSV]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/segment_data_to_csv)           | Exportación CSV de los miembros del segmento. Para incluir eventos de eCommerce, selecciónalos por nombre en el menú desplegable de eventos personalizados.                                                                                |
| [Exportar perfil de usuario por Segment (API)]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment#prerequisites) | Datos del perfil de usuario para los miembros del segmento, devueltos a través de la API. Los eventos de eCommerce se incluyen como eventos personalizados.                                                                                        |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Exportar datos" }

### ¿Cómo segmento usuarios por un producto específico? {#how-do-i-segment-users-by-a-specific-product}

El segmentador te permite filtrar por la cantidad de veces que un usuario realizó un evento de eCommerce. Para filtrar por propiedades específicas del producto (como `product_id` o `product_name`), usa las [extensiones de segmento]({{site.baseurl}}/user_guide/audience/segments/segment_extension), que admiten el filtrado de propiedades de eventos anidados. Por ejemplo, puedes encontrar a todos los usuarios que compraron el producto "SKU-123" en los últimos 90 días.