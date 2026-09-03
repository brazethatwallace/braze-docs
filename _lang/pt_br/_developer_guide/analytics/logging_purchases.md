---
nav_title: Registrar compras
article_title: Registrar compras através do SDK da Braze
page_order: 3.2
description: "Aprenda como registrar compras através do SDK da Braze."

---

# Registrar compras {#log-purchases}

> Aprenda como registrar compras no app através do SDK da Braze, para que você possa determinar sua receita ao longo do tempo e entre diferentes fontes. Isso permite que você segmente usuários [com base no valor do tempo de vida deles]({{site.baseurl}}/developer_guide/analytics#purchase-events-revenue-tracking) usando eventos personalizados, atributos personalizados e eventos de compra.

{% alert note %}
Para wrapper SDKs não listados, use o método nativo relevante do Android ou Swift.
{% endalert %}

Qualquer moeda diferente de USD reportada será exibida na Braze em USD com base na taxa de câmbio na data em que foi reportada. Para saber mais sobre conversão no dashboard, cache e atualização da taxa de câmbio, consulte [Conversão de moeda]({{site.baseurl}}/user_guide/data/activation/events/purchase_events#currency-conversion). Para evitar a conversão, registre as compras com `USD` como código de moeda.

## Registrar compras e receitas {#logging-purchases-and-revenue}

Para registrar compras e receitas, chame `logPurchase()` após uma compra bem-sucedida em seu app. Se o identificador do produto estiver vazio, a compra não será registrada na Braze.

{% tabs %}
{% tab web %}
Para uma implementação padrão do Web SDK, você pode usar o seguinte método:

```javascript
braze.logPurchase(product_id, price, "USD", quantity);
```

Se preferir usar o Google Tag Manager, você pode usar o tipo de tag **Purchase** para chamar o [método `logPurchase`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logpurchase). Use essa tag para rastrear compras na Braze, opcionalmente incluindo propriedades de compra. Para isso:

1. Os campos **Product ID** e **Price** são obrigatórios.
2. Use o botão **Add Row** para adicionar propriedades de compra.

![Uma caixa de diálogo mostrando as configurações da Braze Action Tag. As configurações incluídas são "tag type", "external ID", "price", "currency code", "quantity" e "purchase properties".]({% image_buster /assets/img/web-gtm/gtm-purchase.png %})
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
`productID` pode ter no máximo 255 caracteres. Além disso, se o identificador do produto estiver vazio, a compra não será registrada na Braze.
{% endalert %}

### Adição de propriedades {#adding-properties}

Você pode adicionar metadados sobre compras passando um dicionário preenchido com valores `Int`, `Double`, `String`, `Bool` ou `Date`.

{% tabs %}
{% tab web %}
Para uma implementação padrão do Web SDK, você pode usar o seguinte método:

```javascript
braze.logPurchase(product_id, price, "USD", quantity, {key: "value"});
```

Se seu site registra compras usando o item padrão de camada de dados do [evento de eCommerce](https://developers.google.com/analytics/devguides/collection/ga4/ecommerce?client_type=gtm) do Google Tag Manager, você pode usar o tipo de tag **E-commerce Purchase**. Esse tipo de ação registrará uma "purchase" separada na Braze para cada item enviado na lista de `items`.

Você também pode especificar nomes de propriedades adicionais que deseja incluir como propriedades de compra, informando suas chaves na lista de propriedades de compra. A Braze buscará dentro do `item` individual que está sendo registrado quaisquer propriedades de compra que você adicionar à lista.

Por exemplo, dado o seguinte payload de eCommerce:

```
items: [{
  item_name: "5 L WIV ECO SAE 5W/30",
  item_id: "10801463",
  price: 24.65,
  item_brand: "EUROLUB",
  quantity: 1
}]
```

Se você quiser que apenas `item_brand` e `item_name` sejam passados como propriedades de compra, basta adicionar esses dois campos à tabela de propriedades de compra. Se você não fornecer nenhuma propriedade, nenhuma propriedade de compra será enviada na chamada [`logPurchase`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logpurchase) para a Braze.
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

### Adição de quantidade {#adding-quantity}

Por padrão, `quantity` é definido como `1`. No entanto, você pode adicionar uma quantidade às suas compras se os clientes fizerem a mesma compra várias vezes em um único checkout. Para adicionar uma quantidade, passe um valor `Int` para `quantity`.

### Uso da REST API {#using-the-rest-api}

Você também pode usar nossa REST API para registrar compras. Para saber mais, consulte [Endpoints de dados de usuários]({{site.baseurl}}/api/endpoints/user_data).

## Registrar pedidos {#logging-orders}

Se quiser registrar compras no nível do pedido em vez do nível do produto, você pode usar o nome do pedido ou a categoria do pedido como o `product_id`. Consulte nossa [especificação do objeto de compra]({{site.baseurl}}/api/objects_filters/purchase_object#naming-conventions) para saber mais.

## Chaves reservadas {#reserved-keys}

As seguintes chaves são reservadas e não podem ser usadas como propriedades de compra:

- `time`
- `product_id`
- `quantity`
- `event_name`
- `price`
- `currency`

## Moedas compatíveis {#supported-currencies}

A Braze é compatível com os seguintes símbolos de moeda. Qualquer outro símbolo de moeda informado registra um aviso e a compra não é registrada na Braze.

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