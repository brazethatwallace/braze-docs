---
nav_title: Registrar compras
article_title: Registrar compras para iOS
platform: iOS
page_order: 4
description: "Este artigo de referência mostra como rastrear compras e receitas no app e atribuir propriedades de compra em seu aplicativo iOS."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Registrar compras para iOS {#log-purchases-for-ios}

Registre as compras no app para poder rastrear sua receita ao longo do tempo e entre as fontes de receita, bem como segmentar seus usuários pelo valor do tempo de vida deles.

A Braze oferece suporte a compras em várias moedas. As compras informadas em uma moeda diferente do dólar americano serão mostradas no dashboard em dólares americanos com base na taxa de câmbio na data em que foram informadas.

Antes da implementação, não deixe de analisar exemplos das opções de segmentação oferecidas por eventos personalizados, atributos personalizados e eventos de compra em nossas [práticas recomendadas]({{site.baseurl}}/developer_guide/analytics), bem como nossas notas sobre [convenções de nomenclatura de eventos]({{site.baseurl}}/user_guide/data/activation/events/event_naming_conventions).

## Rastreamento de compras e receitas {#tracking-purchases-and-revenue}

Para usar esse recurso, adicione essa chamada de método após uma compra bem-sucedida em seu app:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance] logPurchase:@"your product ID"
inCurrency:@"USD"
atPrice:[[[NSDecimalNumber alloc] initWithString:@"0.99"] autorelease]];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.logPurchase("your product ID", inCurrency: "USD", atPrice: NSDecimalNumber(string: "0.99"))
```

{% endtab %}
{% endtabs %}

- Os símbolos de moeda compatíveis incluem: USD, CAD, EUR, GBP, JPY, AUD, CHF, NOK, MXN, NZD, CNY, RUB, TRY, INR, IDR, ILS, SAR, ZAR, AED, SEK, HKD, SPD, DKK, entre outros.
  - Qualquer outro símbolo de moeda fornecido resultará em um aviso registrado, sem nenhuma outra ação realizada pelo SDK.
- O identificador do produto pode ter no máximo 255 caracteres.
- Observe que, se o identificador do produto estiver vazio, a compra não será registrada na Braze.

### Adicionando propriedades {#properties-purchases}

Você pode adicionar metadados sobre compras passando um [vetor de propriedades de evento]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties#nested-objects) ou passando um `NSDictionary` preenchido com valores `NSNumber`, `NSString` ou `NSDate`.

Consulte a [documentação da classe iOS](http://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#aaca4b885a8f61ac9fad3936b091448cc) para mais detalhes.

### Adicionando quantidade {#adding-quantity}
Você pode adicionar uma quantidade às suas compras se os clientes fizerem a mesma compra várias vezes em um único checkout. Para isso, basta passar um `NSUInteger` para a quantidade.

* O valor de quantidade deve estar no intervalo de [0, 100] para que o SDK registre a compra.
* Os métodos sem entrada de quantidade terão um valor padrão de 1.
* Os métodos com entrada de quantidade não possuem valor padrão e **devem** receber um valor de quantidade para que o SDK registre a compra.

Consulte a [documentação da classe iOS](http://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#ab50403068be47c0acba9943583e259fa) para mais detalhes.

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance] logPurchase:@"your product ID"
inCurrency:@"USD"
atPrice:[[[NSDecimalNumber alloc] initWithString:@"0.99"] autorelease]
withProperties:@{@"key1":"value1"}];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.logPurchase("your product ID", inCurrency: "USD", atPrice: NSDecimalNumber(string: "0.99"), withProperties: ["key1":"value1"])
```

{% endtab %}
{% endtabs %}

{% alert tip %}
Se você passar um valor de 10 USD e uma quantidade de 3, isso será registrado no perfil do usuário como três compras de 10 dólares, totalizando 30 dólares.
{% endalert %}

### Registrar compras no nível do pedido {#log-purchases-at-the-order-level}
Se você deseja registrar compras no nível do pedido em vez do nível do produto, pode usar o nome do pedido ou a categoria do pedido como `product_id`. Consulte nossa [especificação do objeto de compra]({{site.baseurl}}/api/objects_filters/purchase_object#naming-conventions) para saber mais.

### Chaves reservadas {#reserved-keys}

As seguintes chaves são reservadas e não podem ser usadas como propriedades de compra:

- `time`
- `product_id`
- `quantity`
- `event_name`
- `price`
- `currency`

### REST API

Você também pode usar nossa REST API para registrar compras. Consulte a [documentação da API de usuário]({{site.baseurl}}/api/endpoints/user_data) para mais detalhes.