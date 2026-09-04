---
nav_title: Registrar compras
article_title: Registrar compras a través del SDK de Braze
page_order: 3.2
description: "Aprende a registrar compras a través del SDK de Braze."

---

# Registrar compras {#log-purchases}

> Aprende a registrar las compras dentro de la aplicación a través del SDK de Braze, para que puedas determinar tus ingresos a lo largo del tiempo y de las distintas fuentes. Esto te permitirá segmentar a los usuarios [en función de su LTV]({{site.baseurl}}/developer_guide/analytics#purchase-events-revenue-tracking) utilizando eventos personalizados, atributos personalizados y eventos de compra.

{% alert note %}
Para los SDK envolventes que no aparecen en la lista, utiliza el método nativo de Android o Swift correspondiente.
{% endalert %}

Cualquier moneda distinta al USD que se notifique se mostrará en Braze en USD según la tasa de cambio vigente en la fecha en que se notificó. Para obtener información sobre la conversión en el panel, el almacenamiento en caché y la frecuencia de actualización de las tasas de cambio, consulta [Conversión de divisas]({{site.baseurl}}/user_guide/data/activation/events/purchase_events#currency-conversion). Para evitar la conversión, registra las compras con `USD` como código de moneda.

## Registrar compras e ingresos {#logging-purchases-and-revenue}

Para registrar compras e ingresos, llama a `logPurchase()` después de una compra con éxito en tu aplicación. Si el identificador del producto está vacío, la compra no se registrará en Braze.

{% tabs %}
{% tab web %}
Para una implementación estándar del SDK Web, puedes utilizar el siguiente método:

```javascript
braze.logPurchase(product_id, price, "USD", quantity);
```

Si prefieres utilizar Google Tag Administrador, puedes emplear el tipo de etiqueta **Purchase** para llamar al [método `logPurchase`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logpurchase). Usa esta etiqueta para hacer seguimiento de compras en Braze, incluyendo opcionalmente propiedades de la compra. Para hacerlo:

1. Los campos **Product ID** y **Price** son obligatorios.
2. Utiliza el botón **Add Row** para añadir propiedades de la compra.

![Un cuadro de diálogo que muestra los ajustes de configuración de la etiqueta de acción de Braze. Los ajustes incluyen "tag type", "external ID", "price", "currency code", "quantity" y "purchase properties".]({% image_buster /assets/img/web-gtm/gtm-purchase.png %})
{% endtab %}

{% tab android %}
{% subtabs %}
{% subtab java %}

```java
Braze.getInstance(context).logPurchase(
   String productId,
   String currencyCode,
   BigDecimal price,
   int quantity
);
```

{% endsubtab %}
{% subtab kotlin %}

```kotlin
Braze.getInstance(context).logPurchase(
  productId: String,
  currencyCode: String,
  price: BigDecimal,
  quantity: Int
)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab swift %}
{% subtabs %}
{% subtab swift %}

```swift
AppDelegate.braze?.logPurchase(productID: "product_id", currency: "USD", price: price)
```

{% endsubtab %}
{% subtab objective-c %}

```objc
[AppDelegate.braze logPurchase:"product_id"
                      currency:@"USD"
                         price:price];
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab cordova %}

```javascript
var properties = {};
properties["KEY"] = "VALUE";
BrazePlugin.logPurchase("PRODUCT_ID", 10, "USD", 5, properties);
```

{% endtab %}

{% tab flutter %}

```dart
braze.logPurchase(productId, currencyCode, price, quantity, properties: properties);
```

{% endtab %}

{% tab React Native %}

```javascript
Braze.logPurchase(productId, price, currencyCode, quantity, properties);
```

{% endtab %}

{% tab roku %}

```brightscript
m.Braze.logPurchase("product_id", "currency_code", Double price, Integer quantity)
```

{% endtab %}

{% tab unity %}

```csharp
AppboyBinding.LogPurchase("product_id", "currencyCode", price(decimal));
```

{% endtab %}
{% endtabs %}

{% alert warning %}
`productID` solo puede tener un máximo de 255 caracteres. Además, si el identificador del producto está vacío, la compra no se registrará en Braze.
{% endalert %}

### Añadir propiedades {#adding-properties}

Puedes añadir metadatos sobre las compras pasando un diccionario con valores de tipo `Int`, `Double`, `String`, `Bool` o `Date`.

{% tabs %}
{% tab web %}
Para una implementación estándar del SDK Web, puedes utilizar el siguiente método:

```javascript
braze.logPurchase(product_id, price, "USD", quantity, {key: "value"});
```

Si tu sitio registra compras utilizando el elemento de capa de datos de [evento de comercio electrónico](https://developers.google.com/analytics/devguides/collection/ga4/ecommerce?client_type=gtm) estándar en Google Tag Administrador, puedes emplear el tipo de etiqueta **E-commerce Purchase**. Este tipo de acción registrará una "compra" separada en Braze por cada elemento enviado en la lista de `items`.

También puedes especificar nombres de propiedades adicionales que deseas incluir como propiedades de la compra, indicando sus claves en la lista de propiedades de la compra. Ten en cuenta que Braze buscará dentro del `item` individual que se está registrando cualquier propiedad de la compra que hayas añadido a la lista.

Por ejemplo, dada la siguiente carga útil de comercio electrónico:

```
items: [{
  item_name: "5 L WIV ECO SAE 5W/30",
  item_id: "10801463",
  price: 24.65,
  item_brand: "EUROLUB",
  quantity: 1
}]
```

Si solo quieres que `item_brand` e `item_name` se pasen como propiedades de la compra, simplemente añade esos dos campos a la tabla de propiedades de la compra. Si no proporcionas ninguna propiedad, no se enviarán propiedades de la compra en la llamada a [`logPurchase`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logpurchase) a Braze.
{% endtab %}

{% tab android %}
{% subtabs %}
{% subtab java %}

```java
BrazeProperties purchaseProperties = new BrazeProperties();
purchaseProperties.addProperty("key", "value");
Braze.getInstance(context).logPurchase(..., purchaseProperties);
```

{% endsubtab %}
{% subtab kotlin %}

```kotlin
val purchaseProperties = BrazeProperties()
purchaseProperties.addProperty("key", "value")
Braze.getInstance(context).logPurchase(..., purchaseProperties)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab swift %}
{% subtabs %}
{% subtab swift %}

```swift
let purchaseProperties = ["key": "value"]
AppDelegate.braze?.logPurchase(productID: "product_id", currency: "USD", price: price, properties: purchaseProperties)
```

{% endsubtab %}
{% subtab objective-c %}

```objc
NSDictionary *purchaseProperties = @{@"key": @"value"};
[AppDelegate.braze logPurchase:@"product_id"
                      currency:@"USD"
                         price:price
                   properties:purchaseProperties];
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab cordova %}

```javascript
var properties = {};
properties["key"] = "value";
BrazePlugin.logPurchase("PRODUCT_ID", 10, "USD", 5, properties);
```

{% endtab %}

{% tab flutter %}

```dart
braze.logPurchase(productId, currencyCode, price, quantity, properties: {"key": "value"});
```

{% endtab %}

{% tab React Native %}

```javascript
Braze.logPurchase(productId, price, currencyCode, quantity, { key: "value" });
```

{% endtab %}

{% tab roku %}

```brightscript
m.Braze.logPurchase("product_id", "currency_code", Double price, Integer quantity, {"stringPropKey" : "stringPropValue", "intPropKey" : Integer intPropValue})
```

{% endtab %}

{% tab unity %}

```csharp
Dictionary<string, object> purchaseProperties = new Dictionary<string, object>
{
    { "key", "value" }
};
AppboyBinding.LogPurchase("product_id", "currencyCode", price(decimal), purchaseProperties);
```

{% endtab %}
{% endtabs %}

### Añadir cantidad {#adding-quantity}

De forma predeterminada, `quantity` se establece en `1`. Sin embargo, puedes añadir una cantidad a tus compras si los clientes realizan la misma compra varias veces en una sola transacción. Para añadir una cantidad, pasa un valor `Int` a `quantity`.

### Usar la REST API {#using-the-rest-api}

También puedes utilizar nuestra REST API para registrar compras. Para más información, consulta [Endpoints de datos de usuario]({{site.baseurl}}/api/endpoints/user_data).

## Registrar pedidos {#logging-orders}

Si quieres registrar compras a nivel de pedido en lugar de a nivel de producto, puedes utilizar el nombre del pedido o la categoría del pedido como `product_id`. Consulta nuestra [especificación del objeto de compra]({{site.baseurl}}/api/objects_filters/purchase_object#naming-conventions) para obtener más información.

## Claves reservadas {#reserved-keys}

Las siguientes claves están reservadas y no pueden utilizarse como propiedades de la compra:

- `time`
- `product_id`
- `quantity`
- `event_name`
- `price`
- `currency`

## Divisas compatibles {#supported-currencies}

Braze admite los siguientes símbolos de divisa. Cualquier otro símbolo de divisa que proporciones registrará una advertencia y la compra no se registrará en Braze.

- `AED`, `AFN`, `ALL`, `AMD`, `ANG`, `AOA`, `ARS`, `AUD`, `AWG`, `AZN`
- `BAM`, `BBD`, `BDT`, `BGN`, `BHD`, `BIF`, `BMD`, `BND`, `BOB`, `BRL`
- `BSD`, `BTC`, `BTN`, `BWP`, `BYR`, `BZD`
- `CAD`, `CDF`, `CHF`, `CLF`, `CLP`, `CNY`, `COP`, `CRC`, `CUC`, `CUP`, `CVE`, `CZK`
- `DJF`, `DKK`, `DOP`, `DZD`
- `EEK`, `EGP`, `ERN`, `ETB`, `EUR`
- `FJD`, `FKP`
- `GBP`, `GEL`, `GGP`, `GHS`, `GIP`, `GMD`, `GNF`, `GTQ`, `GYD`
- `HKD`, `HNL`, `HRK`, `HTG`, `HUF`
- `IDR`, `ILS`, `IMP`, `INR`, `IQD`, `IRR`, `ISK`
- `JEP`, `JMD`, `JOD`, `JPY`
- `KES`, `KGS`, `KHR`, `KMF`, `KPW`, `KRW`, `KWD`, `KYD`, `KZT`
- `LAK`, `LBP`, `LKR`, `LRD`, `LSL`, `LTL`, `LVL`, `LYD`
- `MAD`, `MDL`, `MGA`, `MKD`, `MMK`, `MNT`, `MOP`, `MRO`, `MTL`, `MUR`, `MVR`, `MWK`, `MXN`, `MYR`, `MZN`
- `NAD`, `NGN`, `NIO`, `NOK`, `NPR`, `NZD`
- `OMR`
- `PAB`, `PEN`, `PGK`, `PHP`, `PKR`, `PLN`, `PYG`
- `QAR`
- `RON`, `RSD`, `RUB`, `RWF`
- `SAR`, `SBD`, `SCR`, `SDG`, `SEK`, `SGD`, `SHP`, `SLL`, `SOS`, `SRD`, `STD`, `SVC`, `SYP`, `SZL`
- `THB`, `TJS`, `TMT`, `TND`, `TOP`, `TRY`, `TTD`, `TWD`, `TZS`
- `UAH`, `UGX`, `USD`, `UYU`, `UZS`
- `VEF`, `VND`, `VUV`
- `WST`
- `XAF`, `XAG`, `XAU`, `XCD`, `XDR`, `XOF`, `XPD`, `XPF`, `XPT`
- `YER`
- `ZAR`, `ZMK`, `ZMW`, `ZWL`