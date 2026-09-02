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

Braze te permite enviar cargas útiles de datos adicionales a través de Content Cards a los dispositivos de los usuarios mediante pares clave-valor. Estos pueden ayudarte a hacer seguimiento de métricas internas, actualizar el contenido de la aplicación y personalizar propiedades. [Añade pares clave-valor usando el panel]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card#step-4-configure-additional-settings-optional).

{% alert note %}
No recomendamos enviar valores JSON anidados como pares clave-valor. En su lugar, aplana el JSON antes de enviarlo.
{% endalert %}

{% tabs %}
{% tab web %}

Los pares clave-valor se almacenan en objetos <a href="https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html" target="_blank">`card`</a> como `extras`. Estos pueden utilizarse para enviar datos junto con una tarjeta para su posterior procesamiento por parte de la aplicación. Llama a `card.extras` para acceder a estos valores.

{% endtab %}
{% tab android %}

Los pares clave-valor se almacenan en objetos <a href="https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/#-2118252107%2FProperties%2F-1725759721" target="_blank">`card`</a> como `extras`. Estos pueden utilizarse para enviar datos junto con una tarjeta para su posterior procesamiento por parte de la aplicación. Llama a <a href="https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/extras.html" target="_blank">`card.extras`</a> para acceder a estos valores.

{% endtab %}
{% tab swift %}

Los pares clave-valor se almacenan en objetos <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard" target="_blank">`card`</a> como `extras`. Estos pueden utilizarse para enviar datos junto con una tarjeta para su posterior procesamiento por parte de la aplicación. Llama a <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/data-swift.struct/extras" target="_blank">`card.extras`</a> para acceder a estos valores.

{% endtab %}
{% endtabs %}

{% alert tip %}
Es importante que tus equipos de marketing y desarrollo coordinen qué pares clave-valor se utilizarán (por ejemplo, `feed_type = brand_homepage`), ya que cualquier par clave-valor que los especialistas en marketing introduzcan en el panel de Braze debe coincidir exactamente con los pares clave-valor que los desarrolladores integren en la lógica de la aplicación.
{% endalert %}

## Content Cards como contenido complementario {#content-cards-as-supplemental-content}

![Fuente con una lista híbrida que combina datos locales y Content Cards de Braze.]({% image_buster /assets/img/cc_implementation/supplementary.png %}){: style="float:right;max-width:25%;margin-left:15px;border:0;"}

Puedes integrar fácilmente Content Cards en una fuente existente, permitiendo que los datos de múltiples fuentes se carguen simultáneamente. Esto crea una experiencia cohesiva y armoniosa con Content Cards de Braze y el contenido existente de la fuente.

El ejemplo adjunto muestra una fuente con una lista híbrida de elementos que se rellenan utilizando datos locales y Content Cards impulsadas por Braze. De esta forma, las Content Cards pueden resultar indistinguibles del contenido existente.

### Pares clave-valor activados por API {#api-triggered-key-value-pairs}

Las [Campaigns activadas por API]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery) son una buena estrategia a emplear cuando los valores de una tarjeta dependen de factores externos para determinar qué contenido mostrar al usuario. Por ejemplo, para mostrar contenido complementario, configura pares clave-valor utilizando Liquid. Ten en cuenta que `class_type` debe conocerse en el momento de la configuración.

![Los pares clave-valor para el caso de uso de Content Cards complementarias. En este ejemplo, diferentes aspectos de la tarjeta como "tile_id", "tile_deeplink" y "tile_title" se configuran utilizando Liquid.]({% image_buster /assets/img/cc_implementation/supplementary_content.png %}){: style="max-width:60%;"}

## Content Cards como contenido interactivo {#content-cards-as-interactive-content}
![Una Content Card interactiva que muestra una promoción del 50 por ciento aparece en la esquina inferior izquierda de la pantalla. Al hacer clic, se aplicará una promoción al carrito.]({% image_buster /assets/img/cc_implementation/discount2.png %}){: style="border:0;"}{: style="float:right;max-width:45%;border:0;margin-left:15px;"}

Las Content Cards se pueden aprovechar para crear experiencias dinámicas e interactivas para tus usuarios. En el ejemplo que se muestra, aparece una ventana emergente de Content Card en el momento del pago para ofrecer a los usuarios promociones de último momento. Las tarjetas bien ubicadas como esta son una excelente forma de dar a los usuarios un "empujón" hacia acciones específicas.

Los pares clave-valor para este caso de uso incluyen un `discount_percentage` configurado como el monto de descuento deseado y `class_type` configurado como `coupon_code`. Estos pares clave-valor te permiten filtrar y mostrar Content Cards de un tipo específico en la pantalla de pago. Para obtener más información sobre el uso de pares clave-valor para administrar múltiples fuentes, consulta [Personalización de la fuente predeterminada de Content Cards]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/feed#implementing-multiple-feeds).
<br>
<br>

![Content Card interactiva que muestra una promoción en el momento del pago.]({% image_buster /assets/img/cc_implementation/discount.png %}){: style="max-width:80%;"}

## Señales de Content Cards {#content-card-badges}

![Una pantalla de inicio de iPhone que muestra una aplicación de ejemplo de Braze llamada Swifty con una señal roja que muestra el número 7]({% image_buster /assets/img/cc_implementation/ios-unread-badge.png %}){: style="max-width:35%;float:right;margin-left:15px;border:none;"}

Las señales son pequeños iconos ideales para captar la atención del usuario. Usar señales para alertar al usuario sobre nuevo contenido de Content Cards puede atraer a los usuarios de vuelta a tu aplicación y aumentar las sesiones.

### Mostrar el número de Content Cards no leídas como señal {#displaying-the-number-of-unread-content-cards-as-a-badge}

Puedes mostrar el número de Content Cards no leídas que tiene tu usuario como una señal en el icono de tu aplicación.

{% tabs %}
{% tab web %}

Puedes solicitar el número de tarjetas no leídas en cualquier momento llamando a:

```javascript
braze.getCachedContentCards().getUnviewedCardCount();
```

Luego puedes usar esta información para mostrar una señal que indique cuántas Content Cards no leídas hay. Consulta la <a href="https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.contentcards.html" target="_blank">documentación de referencia del SDK or kit de desarrollo de software</a> para más información.

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

Luego puedes usar esta información para mostrar una señal que indique cuántas Content Cards no leídas hay. Consulta la <a href="https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/get-content-card-unviewed-count.html" target="_blank">documentación de referencia del SDK or kit de desarrollo de software</a> para más información.


{% endtab %}
{% tab swift %}

El siguiente ejemplo usa `braze.contentCards` para solicitar y mostrar el número de Content Cards no leídas. Después de que la aplicación se cierra y la sesión del usuario termina, este código solicita un recuento de tarjetas, filtrando el número de tarjetas según la propiedad `viewed`.

Las aplicaciones que han adoptado el [ciclo de vida `UIScene`](https://developer.apple.com/documentation/technotes/tn3187-migrating-to-the-uikit-scene-based-life-cycle) (obligatorio para aplicaciones compiladas con [Xcode 27 y versiones posteriores](https://developer.apple.com/documentation/xcode-release-notes/xcode-27-release-notes)) deben implementar esto en `sceneDidEnterBackground(_:)` de `SceneDelegate.swift` en lugar de `applicationDidEnterBackground(_:)` de `AppDelegate.swift`.

{% subtabs %}
{% subtab Swift %}

```swift
func sceneDidEnterBackground(_ scene: UIScene)
```

Dentro de este método, implementa el siguiente código, que actualiza activamente el recuento de señales mientras el usuario visualiza las tarjetas durante una sesión determinada:

```swift
let unreadCards = AppDelegate.braze?.contentCards.cards.filter { $0.viewed == false }
UIApplication.shared.applicationIconBadgeNumber = unreadCards?.count ?? 0
```

{% endsubtab %}
{% subtab Objective-C %}

```objc
(void)sceneDidEnterBackground:(UIScene *)scene
```

Dentro de este método, implementa el siguiente código, que actualiza activamente el recuento de señales mientras el usuario visualiza las tarjetas durante una sesión determinada:

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