---
nav_title: Usar eventos recomendados de comercio electrónico
article_title: Cómo usar eventos recomendados de comercio electrónico
page_type: reference
alias: /ecommerce_events/
description: "Aprende a usar los eventos recomendados de comercio electrónico en Braze, incluyendo las características compatibles, métricas clave y mejores prácticas para segmentación, mensajería e informes."
---

# Cómo usar eventos de comercio electrónico {#how-to-use-ecommerce-events}

> Los [eventos recomendados]({{site.baseurl}}/recommended_events/) de comercio electrónico usan un esquema compartido a nivel de pedido, lo que permite a Braze construir características confiables sobre tus datos de comercio electrónico, incluyendo perfiles de usuario, segmentación, mensajería, informes y recomendaciones impulsadas por IA. Las secciones de este artículo cubren cómo usar cada capacidad en Braze.<br><br> Consulta [Esquemas de eventos]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/#event-schemas) para los requisitos de propiedades y tipos de datos, y [Validación de eventos y solución de problemas]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/#event-validation-and-troubleshooting) para saber qué sucede cuando un evento no pasa la validación.

Dado que los eventos de comercio electrónico siguen un esquema predecible, Braze puede construir características confiables sobre ellos, desde el seguimiento de ingresos y plantillas de Canvas prediseñadas hasta recomendaciones impulsadas por IA. Las siguientes secciones te ofrecen un resumen rápido de cada capacidad con enlaces a la documentación completa.

{% alert note %}
Los eventos de comercio electrónico de Braze y sus propiedades de eventos segmentables no cuentan como [puntos de datos]({{site.baseurl}}/user_guide/data/infrastructure/data_points/).
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
{: .reset-td-br-1 .reset-td-br-2 aria-label="Order activity metrics" }

### Carrito activo {#active-cart}

El módulo **Active cart** muestra el carrito más reciente en el perfil de usuario. Esta vista es especialmente útil mientras realizas pruebas. Puedes usarla para confirmar el contenido del carrito, validar recorridos basados en el carrito o verificar que los eventos `ecommerce.cart_updated` están actualizando el perfil como esperas.

**Active cart** incluye lo siguiente:

- **Cart ID** — Identificador del carrito que recibió por última vez un evento `ecommerce.cart_updated`.
- **Last updated** — Marca de tiempo de la actualización de carrito más reciente.
- **Total cart value** — Valor total de los artículos en el carrito actual.
- **View products** — Un enlace para abrir la lista de productos en el carrito (hasta 50 productos).

## Orquestación de comercio electrónico {#ecommerce-orchestration}

### Segmentación {#segmentation}

Braze ofrece tres formas de segmentar usuarios basándose en datos de comercio electrónico:

- **Filtros de comercio electrónico:** Usa la categoría **eCommerce** en el segmentador, que contiene filtros impulsados por eventos recomendados de comercio electrónico (como **Last Order Placed**, **Total Revenue** y **Average Order Value**). Para una lista completa de filtros disponibles, consulta [Filtros de segmento]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters/).
- **Filtros de eventos personalizados:** Dado que los eventos de comercio electrónico se comportan como eventos personalizados, todos los filtros de eventos personalizados existentes funcionan de inmediato. Por ejemplo, puedes filtrar por "Ha realizado el evento personalizado `ecommerce.order_placed` más de X veces" o "Realizó por primera vez el evento personalizado `ecommerce.order_placed`".
- **Extensiones de segmento:** Para segmentar por propiedades de eventos anidados, incluyendo el arreglo de productos anidados o las propiedades de los objetos de metadatos, usa [Extensiones de segmento]({{site.baseurl}}/user_guide/audience/segments/segment_extension/) con filtrado de propiedades de eventos anidados. Esto te permite crear audiencias como "usuarios que compraron el producto SKU-123 en los últimos 90 días" o combinar criterios entre diferentes propiedades del mismo pedido.

{% alert important %}
Las Extensiones de segmento para eventos recomendados de comercio electrónico son una característica de pago y están en acceso anticipado. Si te interesa participar en el acceso anticipado, ponte en contacto con tu administrador del éxito del cliente. Confirma que tu plan incluye acceso antes de recomendar la segmentación por propiedades anidadas a tu equipo.
{% endalert %}

### Desencadenamiento {#triggering}

Puedes usar desencadenadores de eventos personalizados realizados con eventos de comercio electrónico en todo Braze, igual que con otros eventos personalizados. Para flujos de carrito abandonado, usa el desencadenador **Perform Cart Updated Event** para capturar correctamente las actualizaciones del carrito.

Además, Braze ofrece un desencadenador dedicado **Places Order**, que te permite iniciar recorridos o tomar acciones basadas en cualquier pedido realizado, o en pedidos que incluyan un producto específico. Puedes filtrar este desencadenador por nombre de producto, `product_id` o `variant_id` para dirigirte a escenarios de compra específicos. Para más información, consulta [Entrega basada en acciones]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/).

![Desencadenador Places Order con una opción seleccionada para realizar cualquier pedido.]({% image_buster /assets/img/recommended_events/places_order_trigger.png %})

### Personalización con Liquid {#liquid-personalization}

Los eventos de comercio electrónico admiten la [personalización con Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid/) de la misma forma que los eventos personalizados; puedes hacer referencia a las propiedades del evento directamente en tu mensajería. Para incluir imágenes de productos, precios u otros datos del catálogo en tus mensajes, vincula tu catálogo con el evento usando `product_id` o `variant_id` como identificador de enlace. La etiqueta de Liquid {% raw %}`{% shopping_cart %}`{% endraw %} te permite recorrer el contenido actual del carrito de un usuario para recordatorios de carrito abandonado, incentivos de pago o confirmaciones de pedido. Para ejemplos de código listos para usar, consulta [Casos de uso de comercio electrónico]({{site.baseurl}}/ecommerce_use_cases/).

Para una alternativa sin código, los [bloques de producto de arrastrar y soltar]({{site.baseurl}}/user_guide/messaging/design_and_edit/product_blocks/) están disponibles en el programa de acceso anticipado.

### Plantillas de Canvas de comercio electrónico {#ecommerce-canvas-templates}

Braze proporciona plantillas de Canvas listas para usar, preconfiguradas con eventos recomendados de comercio electrónico como criterios de entrada, salida y conversión, para que puedas lanzar flujos de ciclo de vida sin configuración personalizada. Cada plantilla incluye diseños de correo electrónico de arrastrar y soltar y admite bloques de producto de arrastrar y soltar (actualmente en acceso anticipado). Para casos de uso detallados y ejemplos de Liquid, consulta [Casos de uso de comercio electrónico]({{site.baseurl}}/ecommerce_use_cases/).

Estas plantillas cubren los flujos de ciclo de vida de comercio electrónico más comunes. Úsalas como punto de partida y luego personaliza los tiempos, canales y creatividades para tu audiencia.

{% tabs %}
{% tab Navegación abandonada %}

Vuelve a captar a los usuarios que vieron un producto pero no lo agregaron a su carrito.

Usa esta plantilla cuando quieras traer de vuelta a los navegadores para que consideren productos que vieron recientemente pero sobre los que no actuaron.

| Configuración | Valor |
| --- | --- |
| Evento de entrada | `ecommerce.product_viewed` |
| Eventos de salida | `ecommerce.product_viewed`, `ecommerce.cart_updated`, `ecommerce.checkout_started`, Placed Order |
| Evento de conversión | Placed Order |
{: .reset-td-br-1 .reset-td-br-2 aria-label="eCommerce Canvas templates" }

{% endtab %}
{% tab Carrito abandonado %}

Recupera a los usuarios que agregaron artículos a su carrito pero no iniciaron el pago.

Usa esta plantilla cuando quieras recordar a los usuarios sobre los artículos en su carrito e impulsarlos a completar el pago.

| Configuración | Valor |
| --- | --- |
| Evento de entrada | `ecommerce.cart_updated` |
| Eventos de salida | `ecommerce.cart_updated`, `ecommerce.checkout_started`, Placed Order |
| Evento de conversión | Placed Order |
{: .reset-td-br-1 .reset-td-br-2 aria-label="eCommerce Canvas templates" }

{% alert tip %}
El evento `ecommerce.cart_updated` admite el reemplazo completo del carrito (cada evento puede describir el carrito completo) o actualizaciones incrementales usando los valores `add` y `remove` para la propiedad opcional `action`. Elige un enfoque por carrito y evita mezclar actualizaciones de reemplazo e incrementales para el mismo `cart_id`. Usa la etiqueta de Liquid {% raw %}`{% shopping_cart %}`{% endraw %} en tu mensaje para mostrar dinámicamente el contenido actual del carrito en el momento del envío.
{% endalert %}

{% endtab %}
{% tab Pago abandonado %}

Recupera a los usuarios que iniciaron el pago pero no completaron la compra.

Usa esta plantilla cuando quieras recuperar compras en la etapa de mayor intención del embudo.

| Configuración | Valor |
| --- | --- |
| Evento de entrada | `ecommerce.checkout_started` |
| Evento de salida | Placed Order |
| Evento de conversión | Placed Order |
{: .reset-td-br-1 .reset-td-br-2 aria-label="eCommerce Canvas templates" }

{% endtab %}
{% tab Confirmación de pedido y encuesta %}

Confirma una compra exitosa y hace seguimiento con una encuesta de opinión para impulsar la recopilación de reseñas y la interacción posterior a la compra.

Usa esta plantilla cuando quieras optimizar la comunicación posterior a la compra y recopilar comentarios de los clientes en un solo flujo de trabajo.

| Configuración | Valor |
| --- | --- |
| Evento de entrada | `ecommerce.order_placed` |
| Evento de conversión | Start Session o `ecommerce.product_viewed` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="eCommerce Canvas templates" }

{% endtab %}
{% endtabs %}

#### Personalizar plantillas {#customize-templates}

Estas plantillas están diseñadas como punto de partida. Las personalizaciones comunes incluyen:
  - **Personalizar el correo electrónico:** Cada plantilla incluye un correo electrónico preconfigurado creado con el editor de arrastrar y soltar, totalmente editable para que coincida con tu marca y contenido.
  - **Agregar canales:** Combina el correo electrónico con push, SMS o mensajes dentro de la aplicación para un refuerzo multicanal.
  - **Agregar retrasos y divisiones de decisiones:** Segmenta a los usuarios por comportamiento (por ejemplo, carrito de alto valor frente a carrito de bajo valor) o períodos de espera entre mensajes.
  - **Cambiar la creatividad:** Reemplaza la plantilla de correo electrónico incluida con el estilo visual de tu marca.
  - **Usar bloques de producto:** Usa bloques de producto de arrastrar y soltar (en el programa de acceso anticipado) para renderizar dinámicamente el contenido del carrito abandonado o los productos navegados sin escribir Liquid personalizado.

Para estrategias de ciclo de vida más avanzadas, incluyendo ejemplos de personalización con Liquid, consulta [Casos de uso de comercio electrónico]({{site.baseurl}}/ecommerce_use_cases/).

## Informes de comercio electrónico {#ecommerce-reporting}

Los eventos recomendados de comercio electrónico alimentan las mismas superficies de ingresos que los clientes ya usan hoy. Cuando tu integración envía eventos de comercio electrónico, los siguientes informes incluyen los ingresos de comercio electrónico automáticamente:

| Informe | Qué muestra |
|---------------------------------------------|-------------------------------------------|
| Informe de ingresos | Ingresos totales, ingresos diarios promedio, compras diarias e ingresos por usuario a lo largo del tiempo en todas las fuentes para el rango de fechas y aplicaciones seleccionados. |
| Dashboard de ingresos de atribución de último toque | Ingresos atribuidos a la última campaña o Canvas con los que un usuario interactuó antes de realizar un pedido. Los eventos de toque incluyen clics en correo electrónico, aperturas de push, clics en tarjetas de contenido, clics en mensajes dentro de la aplicación y clics en enlaces cortos de SMS o WhatsApp. |
| Análisis de Campaign y Canvas | Ingresos totales atribuidos a una campaña o Canvas específicos dentro de la ventana de conversión primaria. |
| Informe de conversiones | Ingresos vinculados a eventos de conversión en campañas y Canvas.<br> **Nota:** Para contar los ingresos de `ecommerce.order_placed`, la campaña o Canvas debe usar el tipo de evento de conversión "Place Order" como su evento de conversión. |
| Información del segmento | Comparaciones de ingresos entre segmentos en el dashboard de información del segmento. |
| Generador de informes | Métricas de ingresos en informes personalizados creados en el Generador de informes. |
| Generador de dashboards | Métricas de ingresos en dashboards personalizados creados en el Generador de dashboards. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="eCommerce reporting" }

Para campos calculados que no son de usuario (por ejemplo, ingresos de una campaña o Canvas), los ingresos se calculan de la misma manera en todos los informes: `price` multiplicado por `quantity` por producto en el pedido, sumado entre los productos de cada evento `order_placed`.

{% alert note %}
Para evitar el doble conteo de ingresos, no envíes tanto compras heredadas como eventos recomendados de comercio electrónico para los mismos pedidos. Si planeas hacer la transición de compras heredadas a eventos recomendados, coordina el cambio con tu equipo de cuenta de Braze antes de realizar cualquier cambio en la integración.<br><br>
Los cálculos de ingresos limitan las cantidades individuales de productos a `1,000` unidades por pedido. Si falta un campo `quantity` para un producto, se establece por defecto en `1`. El evento `order_placed` original conserva la cantidad completa que enviaste; solo el cálculo de ingresos aplica el límite.
{% endalert %}

### BrazeAI<sup>TM</sup>

[Predictive Events]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/), [Predictive Churn]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/) y las [recomendaciones de elementos]({{site.baseurl}}/user_guide/brazeai/item_recommendations/) admiten eventos de comercio electrónico como eventos objetivo y señales, y tienen una opción dedicada "Order Placed". El esquema estandarizado hace que estos modelos sean más confiables porque los datos son consistentes en toda tu base de usuarios.

### Exportar datos {#export-data}

Braze ofrece varias formas de exportar datos de eventos de comercio electrónico para usarlos en tu almacén de datos, herramientas de BI o sistemas posteriores. Los eventos recomendados de comercio electrónico se exportan a través de los mismos canales que tus otros datos de eventos.

| Ruta de exportación | Qué incluye |
|------------------------------------- |------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/) | Los eventos de comercio electrónico se transmiten como eventos personalizados; busca el espacio de nombres `ecommerce.*` para encontrarlos. Los productos de cada pedido están disponibles como compras. |
| [Uso compartido de datos de Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/data_sharing/) | Los eventos de comercio electrónico se comparten como eventos personalizados; busca el espacio de nombres `ecommerce.*` para encontrarlos. Los productos de cada pedido están disponibles en la tabla de compras. |
| [Exportar datos de segmento a CSV]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/segment_data_to_csv/) | Exportación CSV de miembros del segmento. Para incluir eventos de comercio electrónico, selecciónalos por nombre en el menú desplegable de eventos personalizados. |
| [Exportar perfil de usuario por Segment (API)]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/#prerequisites) | Datos de perfil de usuario para miembros del segmento, devueltos a través de la API. Los eventos de comercio electrónico se incluyen como eventos personalizados. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Export data" }

### ¿Cómo segmento usuarios por un producto específico? {#how-do-i-segment-users-by-a-specific-product}

El segmentador te permite filtrar por el número de veces que un usuario realizó un evento de comercio electrónico. Para filtrar por propiedades específicas del producto (como `product_id` o `product_name`), usa [Extensiones de segmento]({{site.baseurl}}/user_guide/audience/segments/segment_extension/), que admiten el filtrado de propiedades de eventos anidados. Por ejemplo, puedes encontrar todos los usuarios que compraron el producto "SKU-123" en los últimos 90 días.