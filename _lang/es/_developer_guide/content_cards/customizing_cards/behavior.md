---
nav_title: Comportamiento
article_title: Personalizar el comportamiento de las Content Cards
page_order: 2
description: "Esta guía de implementación trata sobre cómo cambiar el comportamiento de las Content Cards, cómo añadir extras como pares clave-valor a tu carga útil, y recetas para personalizaciones comunes."
channel:
  - content cards
platform:
  - Android
  - FireOS
  - Swift
  - Web
---

# Personalizar el comportamiento de las Content Cards {#customize-the-behavior-of-content-cards}

> Esta guía de implementación trata sobre cómo cambiar el comportamiento de las Content Cards, cómo añadir extras como pares clave-valor a tu carga útil, y recetas para personalizaciones comunes. Para obtener la lista completa de tipos de tarjetas de contenido, consulta [Acerca de las Content Cards]({{site.baseurl}}/developer_guide/content_cards).

## Pares clave-valor {#key-value-pairs}

Braze te permite enviar cargas útiles de datos adicionales mediante Content Cards a los dispositivos de los usuarios utilizando pares clave-valor. Pueden ayudarte a realizar un seguimiento de las métricas internas, actualizar el contenido de la aplicación y personalizar las propiedades. [Añade pares clave-valor utilizando el dashboard]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create#step-4-configure-additional-settings-optional).

{% alert note %}
No recomendamos enviar valores JSON anidados como pares clave-valor. En su lugar, aplana el JSON antes de enviarlo.
{% endalert %}

{% tabs %}
{% tab web %}

Los pares clave-valor se almacenan en objetos <a href="https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html" target="_blank">`card`</a> como `extras`. Se pueden utilizar para enviar datos junto con una tarjeta para su posterior manipulación por la aplicación. Llama a `card.extras` para acceder a estos valores.

{% endtab %}
{% tab android %}

Los pares clave-valor se almacenan en objetos <a href="https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/#-2118252107%2FProperties%2F-1725759721" target="_blank">`card`</a> como `extras`. Se pueden utilizar para enviar datos junto con una tarjeta para su posterior manipulación por la aplicación. Llama a <a href="https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/extras.html" target="_blank">`card.extras`</a> para acceder a estos valores.

{% endtab %}
{% tab swift %}

Los pares clave-valor se almacenan en objetos <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard" target="_blank">`card`</a> como `extras`. Se pueden utilizar para enviar datos junto con una tarjeta para su posterior manipulación por la aplicación. Llama a <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/data-swift.struct/extras" target="_blank">`card.extras`</a> para acceder a estos valores.

{% endtab %}
{% endtabs %}

{% alert tip %}
Es importante que tus equipos de marketing y desarrolladores se coordinen sobre qué pares clave-valor se utilizarán (por ejemplo, `feed_type = brand_homepage`), ya que cualquier par clave-valor que los especialistas en marketing introduzcan en el dashboard de Braze debe coincidir exactamente con los pares clave-valor que los desarrolladores incorporen a la lógica de la aplicación.
{% endalert %}

## Content Cards como contenido complementario {#content-cards-as-supplemental-content}

![Fuente con una lista híbrida que combina datos locales y Content Cards de Braze.]({% image_buster /assets/img/cc_implementation/supplementary.png %}){: style="float:right;max-width:25%;margin-left:15px;border:0;"}

Puedes integrar fácilmente las Content Cards en una fuente existente, permitiendo que los datos de varias fuentes se carguen simultáneamente. Esto crea una experiencia cohesiva y armoniosa con las Content Cards de Braze y el contenido de la fuente existente.

El ejemplo de la derecha muestra una fuente con una lista híbrida de elementos que se rellenan mediante datos locales y Content Cards impulsadas por Braze. Con esto, las Content Cards pueden ser indistinguibles del contenido existente.

### Pares clave-valor desencadenados por la API {#api-triggered-key-value-pairs}

Las [Campaigns desencadenadas por API]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery) son una buena estrategia a emplear cuando los valores de una tarjeta dependen de factores externos para determinar qué contenido mostrar al usuario. Por ejemplo, para mostrar contenido complementario, establece pares clave-valor utilizando Liquid. Ten en cuenta que `class_type` debe conocerse en el momento de la configuración.

![Los pares clave-valor para el caso de uso de las Content Cards complementarias. En este ejemplo, diferentes aspectos de la tarjeta, como "tile_id", "tile_deeplink" y "tile_title", se configuran utilizando Liquid.]({% image_buster /assets/img/cc_implementation/supplementary_content.png %}){: style="max-width:60%;"}

## Content Cards como contenido interactivo {#content-cards-as-interactive-content}
![Una Content Card interactiva que muestra una promoción del 50 % aparece en la esquina inferior izquierda de la pantalla. Tras hacer clic, se aplicará una promoción al carrito.]({% image_buster /assets/img/cc_implementation/discount2.png %}){: style="border:0;"}{: style="float:right;max-width:45%;border:0;margin-left:15px;"}

Las Content Cards pueden aprovecharse para crear experiencias dinámicas e interactivas para tus usuarios. En el ejemplo de la derecha, tenemos una ventana emergente de una Content Card que aparece en el momento de la compra y que ofrece a los usuarios promociones de última hora. Las tarjetas bien colocadas como esta son una forma estupenda de dar a los usuarios un "empujoncito" hacia acciones específicas.

Los pares clave-valor para este caso de uso incluyen un `discount_percentage` configurado como el importe de descuento deseado y `class_type` configurado como `coupon_code`. Estos pares clave-valor te permiten filtrar y mostrar Content Cards de tipos específicos en la pantalla de pago. Para más información sobre el uso de pares clave-valor para gestionar varias fuentes, consulta [Personalizar la fuente predeterminada de Content Cards]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_feed#multiple-feeds).
<br>
<br>

![Content Card interactiva que muestra una promoción en el momento del pago.]({% image_buster /assets/img/cc_implementation/discount.png %}){: style="max-width:80%;"}

## Señales de Content Cards {#content-card-badges}

![Una pantalla de inicio de iPhone que muestra una aplicación de ejemplo de Braze llamada Swifty con una señal roja que muestra el número 7]({% image_buster /assets/img/cc_implementation/ios-unread-badge.png %}){: style="max-width:35%;float:right;margin-left:15px;border:none;"}

Las señales son pequeños iconos ideales para llamar la atención del usuario. Utilizar señales para alertar al usuario sobre nuevo contenido de Content Cards puede atraer a los usuarios de vuelta a tu aplicación y aumentar las sesiones.

### Mostrar el número de Content Cards no leídas como una señal {#displaying-the-number-of-unread-content-cards-as-a-badge}

Puedes mostrar el número de Content Cards no leídas que tiene tu usuario como una señal en el icono de tu aplicación.

{% tabs %}
{% tab web %}

Puedes solicitar el número de tarjetas no leídas en cualquier momento llamando a:

```javascript
braze.getCachedContentCards().getUnviewedCardCount();
```

Puedes utilizar esta información para mostrar una señal que indique cuántas Content Cards hay sin leer. Consulta <a href="https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.contentcards.html" target="_blank">la documentación de referencia del SDK</a> para obtener más información.

{% endtab %}
{% tab android %}

Puedes solicitar el número de tarjetas no leídas en cualquier momento llamando a:

{% subtabs %}
{% subtab Java %}

```java
Braze.getInstance(context).getContentCardUnviewedCount();
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
Braze.getInstance(context).contentCardUnviewedCount
```

{% endsubtab %}
{% endsubtabs %}

Puedes utilizar esta información para mostrar una señal que indique cuántas Content Cards hay sin leer. Consulta <a href="https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/get-content-card-unviewed-count.html" target="_blank">la documentación de referencia del SDK</a> para obtener más información.


{% endtab %}
{% tab swift %}

El siguiente ejemplo utiliza `braze.contentCards` para solicitar y mostrar el número de Content Cards no leídas. Una vez cerrada la aplicación y finalizada la sesión del usuario, este código solicita un recuento de tarjetas, filtrando el número de tarjetas en función de la propiedad `viewed`.

{% subtabs %}
{% subtab Swift %}

```swift
func applicationDidEnterBackground(_ application: UIApplication)
```

Dentro de este método, implementa el siguiente código, que actualiza activamente el recuento de señales mientras el usuario ve las tarjetas durante una sesión determinada:

```swift
let unreadCards = AppDelegate.braze?.contentCards.cards.filter { $0.viewed == false }
UIApplication.shared.applicationIconBadgeNumber = unreadCards?.count ?? 0
```

{% endsubtab %}
{% subtab Objective-C %}

```objc
(void)applicationDidEnterBackground:(UIApplication *)application
```

Dentro de este método, implementa el siguiente código, que actualiza activamente el recuento de señales mientras el usuario ve las tarjetas durante una sesión determinada:

```objc
NSInteger unreadCardCount = 0;
for (BRZContentCardRaw *card in AppDelegate.braze.contentCards.cards) {
  if (card.viewed == NO) {
    unreadCardCount += 1;
  }
}
[UIApplication sharedApplication].applicationIconBadgeNumber = unreadCardCount;
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}