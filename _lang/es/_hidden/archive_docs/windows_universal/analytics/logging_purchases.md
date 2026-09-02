---
nav_title: Registrar compras
article_title: Registrar compras para Windows Universal
platform: Windows Universal
page_order: 4
description: "En este artículo de referencia se explica cómo registrar compras en la plataforma Windows Universal."
hidden: true
---

# Registrar compras {#log-purchases}
{% multi_lang_include archive/windows_deprecation.md %}

Registra las compras dentro de la aplicación para que puedas hacer un seguimiento de tus ingresos a lo largo del tiempo y de las distintas fuentes de ingresos, así como segmentar a tus usuarios por su valor de duración del ciclo de vida.

Braze admite compras en varias divisas. Las compras que notifiques en una divisa distinta del USD se mostrarán en el panel en USD según la tasa de cambio en la fecha en que se notificaron.

Antes de la implementación, asegúrate de revisar ejemplos de las opciones de segmentación que ofrecen los eventos personalizados, los atributos personalizados y los eventos de compra en nuestro artículo de [buenas prácticas]({{site.baseurl}}/developer_guide/analytics#best-practices). También te recomendamos que te familiarices con nuestras [convenciones de denominación de eventos]({{site.baseurl}}/user_guide/data/activation/events/event_naming_conventions).

Para utilizar esta característica, añade esta llamada al método después de una compra con éxito en tu aplicación:

Las compras se registran utilizando `EventLogger`, que es una propiedad expuesta en IAppboy. Para obtener una referencia a `EventLogger`, llama a `Appboy.SharedInstance.EventLogger`.

```csharp
bool LogPurchase(string productId, string currencyCode, decimal price)
```

## Registrar compras a nivel de pedido {#log-purchases-at-the-order-level}
Si deseas registrar las compras a nivel de pedido en lugar de a nivel de producto, puedes usar el nombre del pedido o la categoría del pedido como `product_id`. Consulta nuestra [especificación del objeto de compra]({{site.baseurl}}/api/objects_filters/purchase_object#naming-conventions) para obtener más información.

## REST API

También puedes utilizar nuestra REST API para registrar compras. Consulta la documentación de [la API de usuarios]({{site.baseurl}}/api/endpoints/user_data) para más detalles.