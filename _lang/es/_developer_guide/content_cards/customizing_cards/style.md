---
nav_title: Estilo
article_title: Personalizar el estilo de Content Cards
page_order: 1
description: "Este artículo trata de las opciones de estilo para tus Content Cards."
channel:
  - content cards
platform:
  - Android
  - FireOS
  - Swift
  - Web
---

# Personalizar el estilo de Content Cards {#customize-the-style-of-content-cards}

> Las Content Cards de Braze tienen un aspecto predeterminado. Este artículo trata de las opciones de estilo de tus Content Cards para ayudarte a que coincidan con la identidad de tu marca. Para obtener la lista completa de tipos de tarjetas de contenido, consulta [Acerca de Content Cards]({{site.baseurl}}/developer_guide/content_cards).

## Crear un estilo personalizado {#creating-a-custom-style}

La interfaz de usuario predeterminada de Content Cards se importa desde la capa de interfaz del SDK de Braze. Desde ahí, puedes ajustar ciertos aspectos del estilo de la tarjeta, el orden en que se muestran las tarjetas y cómo se presenta la fuente a tus usuarios.

![Dos tarjetas de contenido, una con la fuente predeterminada y esquinas cuadradas, y otra con esquinas redondeadas y una fuente cursiva]({% image_buster/assets/img/content_cards/content-card-customization-attributes.png %})

{% alert note %}
Las propiedades de Content Cards como `title`, `cardDescription`, `imageUrl`, etc., se pueden editar directamente a través del [panel]({{site.baseurl}}/user_guide/channels/content_cards/creative_details), que es el método preferido para cambiar estos detalles.
{% endalert %}


{% tabs %}
{% tab web %}

Los estilos predeterminados de Braze se definen en CSS dentro del SDK de Braze. Al sobrescribir estilos seleccionados en tu aplicación, puedes personalizar nuestra fuente estándar con tus propias imágenes de fondo, familias de fuentes, estilos, tamaños, animaciones y más. Por ejemplo, la siguiente es una sobrescritura de ejemplo que hace que las Content Cards aparezcan con un ancho de 800 px:

``` css
body .ab-feed {
  width: 800px;
}
```

Para ver una lista completa de propiedades que puedes modificar, consulta las [opciones de configuración del SDK de Braze](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html).

{% endtab %}
{% tab android %}

De forma predeterminada, las Content Cards del SDK de Android y FireOS se ajustan a las directrices estándar de la interfaz de Android para proporcionar una experiencia uniforme. Puedes ver estos estilos predeterminados en el archivo [`res/values/styles.xml`](https://github.com/braze-inc/braze-android-sdk/blob/master/android-sdk-ui/src/main/res/values/styles.xml) en la distribución del SDK de Braze:

```xml
  <style name="Braze.ContentCards.CaptionedImage.Description">
    <item name="android:textColor">@color/com_braze_description</item>
    <item name="android:textSize">15.0sp</item>
    <item name="android:includeFontPadding">false</item>
    <item name="android:paddingBottom">8.0dp</item>
    <item name="android:layout_marginLeft">10.0dp</item>
    <item name="android:layout_marginRight">10.0dp</item>
    <item name="android:layout_marginTop">8.0dp</item>
    <item name="android:layout_width">match_parent</item>
    <item name="android:layout_below">@id/com_braze_content_cards_captioned_image_card_title_container</item>
  </style>
```

Para personalizar el estilo de tus Content Cards, sobrescribe este estilo predeterminado. Para sobrescribir un estilo, cópialo en su totalidad en el archivo `styles.xml` de tu proyecto y haz las modificaciones. El estilo completo debe copiarse a tu archivo `styles.xml` local para que todos los atributos se establezcan correctamente.

{% subtabs local %}
{% subtab Sobrescritura de estilo correcta %}

```xml
<style name="Braze.ContentCardsDisplay">
  <item name="android:background">@color/mint</item>
  <item name="android:cacheColorHint">@color/mint</item>
  <item name="android:divider">@android:color/transparent</item>
  <item name="android:dividerHeight">16.0dp</item>
  <item name="android:paddingLeft">12.5dp</item>
  <item name="android:paddingRight">5.0dp</item>
  <item name="android:scrollbarStyle">outsideInset</item>
</style>
```

{% endsubtab %}
{% subtab Sobrescritura de estilo incorrecta %}

```xml
<style name="Braze.ContentCardsDisplay">
  <item name="android:background">@color/mint</item>
  <item name="android:cacheColorHint">@color/mint</item>
</style>
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Jetpack Compose %}

De forma predeterminada, las Content Cards del SDK de Android y FireOS se ajustan a las directrices estándar de la interfaz de Android para proporcionar una experiencia uniforme.

Puedes aplicar estilos de una de estas dos maneras. La primera es pasar un [`ContentCardListStyling`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards.styling/-content-card-list-styling/index.html) y un [`ContentCardStyling`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards.styling/-content-card-styling/index.html) a [`ContentCardsList`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards/-content-cards-list.html), como en el siguiente ejemplo:

```kotlin
ContentCardsList(
    style = ContentCardListStyling(listBackgroundColor = Color.Red),
    cardStyle = ContentCardStyling(
        titleTextStyle = TextStyle(
            fontFamily = fontFamily,
            fontSize = 25.sp
        ),
        shadowRadius = 10.dp,
        shortNewsContentCardStyle = BrazeShortNewsContentCardStyling(
            shadowRadius = 15.dp
        )
    )
)
```

La segunda es usar [`BrazeStyle`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose/-braze-style.html) para crear un estilo global para los componentes de Braze, como en el siguiente ejemplo:

```kotlin
BrazeStyle(
    contentCardStyle = ContentCardStyling(
        textAnnouncementContentCardStyle = BrazeTextAnnouncementContentCardStyling(
            cardBackgroundColor = Color.Red,
            descriptionTextStyle = TextStyle(
                fontFamily = fontFamily,
                fontSize = 25.sp,
            )
        ),
        titleTextColor = Color.Magenta
    )
) {
    // Your app here, including any ContentCardsList() in it
}
```

{% endtab %}
{% tab swift %}

El controlador de vista de Content Cards te permite personalizar la apariencia y el comportamiento de todas las celdas a través de la estructura [`BrazeContentCardUI.ViewController.Attributes`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct). Configurar Content Cards usando `Attributes` es una opción sencilla que te permite lanzar tu interfaz de Content Cards con una configuración mínima.

{% alert important %}
La personalización a través de `Attributes` solo está disponible en Swift.
{% endalert %}

{% subtabs %}
{% subtab Swift %}

**Modificar `Attributes.default`**

Personaliza la apariencia de todas las instancias del controlador de vista de la interfaz de Content Cards de Braze modificando directamente la variable estática [`Attributes.defaults`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct/defaults).

Por ejemplo, para cambiar el tamaño de imagen predeterminado y el radio de esquina para todas las celdas:

```swift
BrazeContentCardUI.ViewController.Attributes.defaults.cellAttributes.cornerRadius = 20
BrazeContentCardUI.ViewController.Attributes.defaults.cellAttributes.classicImageSize = CGSize(width: 65, height: 65)
```

**Inicializar el controlador de vista con Attributes**

Si deseas modificar solo una instancia específica del controlador de vista de la interfaz de Content Cards de Braze, usa el inicializador [`init(braze:attributes:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/init(braze:attributes:)/) para pasar una estructura `Attributes` personalizada al controlador de vista.

Por ejemplo, puedes cambiar el tamaño de imagen y el radio de esquina para una instancia específica del controlador de vista:

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.cellAttributes.cornerRadius = 20
attributes.cellAttributes.classicImageSize = CGSize(width: 65, height: 65)

let viewController = BrazeContentCardUI.ViewController(braze: AppDelegate.braze, attributes: attributes)
```

**Personalizar celdas mediante subclases**

Como alternativa, puedes crear interfaces personalizadas registrando clases personalizadas para cada tipo de tarjeta deseado. Para usar tu subclase en lugar de la celda predeterminada, modifica la propiedad [`cells`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct/cells) en la estructura `Attributes`. Por ejemplo:

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
// Register your own custom cell
attributes.cells[BrazeContentCardUI.ClassicImageCell.identifier] = CustomClassicImageCell.self

let viewController = BrazeContentCardUI.ViewController(braze: AppDelegate.braze, attributes: attributes)
```

**Modificar Content Cards programáticamente**

Puedes cambiar las Content Cards programáticamente asignando el closure [`transform`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct/transform) en tu estructura `Attributes`. El siguiente ejemplo modifica el `title` y la `description` de las tarjetas compatibles:

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.transform = { cards in
  cards.map { card in
    var card = card
    if let title = card.title {
      card.title = "[modified] \(title)"
    }
    if let description = card.description {
      card.description = "[modified] \(description)"
    }
    return card
  }
}

let viewController = BrazeContentCardUI.ViewController(braze: AppDelegate.braze, attributes: attributes)
```

Consulta la [aplicación de ejemplo de Examples](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples/Swift) para ver un ejemplo completo.

{% endsubtab %}
{% subtab Objective-C %}

La personalización de Content Cards a través de `Attributes` no es compatible con Objective-C.

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Ejemplos de personalización {#customization-examples}

### Fuente personalizada {#custom-font}

Personalizar la fuente utilizada en tus Content Cards te permite mantener la identidad de tu marca y crear una experiencia visualmente atractiva para tus usuarios. Usa estas recetas para configurar la fuente de todas las Content Cards de forma programática.

{% tabs %}
{% tab web %}

Al igual que cualquier otro elemento web, puedes personalizar fácilmente la apariencia de las Content Cards mediante CSS. En tu archivo CSS o estilos en línea, usa la propiedad `font-family` y especifica el nombre de la fuente o la pila de fuentes deseada.

```css
/* CSS selector targeting the Content Card element */
.card-element {
  font-family: "Helvetica Neue", Arial, sans-serif;
}
```

{% endtab %}
{% tab android %}

Para cambiar la fuente predeterminada de forma programática, establece un estilo para las tarjetas y usa el atributo `fontFamily` para indicarle a Braze que utilice tu familia de fuentes personalizada.

Por ejemplo, para actualizar la fuente en todos los títulos de las tarjetas con imagen subtitulada, sobrescribe el estilo `Braze.ContentCards.CaptionedImage.Title` y haz referencia a tu familia de fuentes personalizada. El valor del atributo debe apuntar a una familia de fuentes en tu directorio `res/font`.

Este es un ejemplo resumido con una familia de fuentes personalizada, `my_custom_font_family`, referenciada en la última línea:

```xml
  <style name="Braze.ContentCards.CaptionedImage.Title">
    <item name="android:layout_width">wrap_content</item>
    ...
    <item name="android:fontFamily">@font/my_custom_font_family</item>
    <item name="fontFamily">@font/my_custom_font_family</item>
  </style>
```

El ejemplo XML anterior muestra cómo hacer referencia a una familia de fuentes personalizada en los estilos de tus tarjetas.
{% endtab %}
{% tab Jetpack Compose %}
Para cambiar la fuente predeterminada de forma programática, puedes establecer el [`titleTextStyle`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards.styling/-content-card-styling/index.html#715371549%2FProperties%2F-1725759721) de `ContentCardStyling`.

También puedes establecer `titleTextStyle` para un tipo de tarjeta específico configurándolo en [`BrazeShortNewsContentCardStyling`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards.styling/-braze-short-news-content-card-styling/index.html) y pasándolo al [`shortNewsContentCardStyle`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards.styling/-content-card-styling/index.html#8580250%2FProperties%2F-1725759721) de `ContentCardStyling`.

```kotlin
val fontFamily = FontFamily(
    Font(R.font.sailec_bold)
)

ContentCardStyling(
    titleTextStyle = TextStyle(
        fontFamily = fontFamily
    )
)
```
{% endtab %}
{% tab swift %}
{% subtabs %}
{% subtab Swift %}

Personaliza tus fuentes modificando los `Attributes` de la propiedad de instancia [`cellAttributes`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct/cellattributes/). Por ejemplo:

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.cellAttributes.titleFont = .preferredFont(textStyle: .callout, weight: .bold)
attributes.cellAttributes.descriptionFont = .preferredFont(textStyle: .footnote, weight: .regular)
attributes.cellAttributes.domainFont = .preferredFont(textStyle: .footnote, weight: .medium)

let viewController = BrazeContentCardUI.ViewController.init(braze: braze, attributes: attributes)
```

{% endsubtab %}
{% subtab Objective-C %}

La personalización de fuentes mediante `Attributes` no es compatible en Objective-C.

Consulta la [aplicación de ejemplo de Examples](https://github.com/braze-inc/braze-swift-sdk/blob/main/Examples/ObjC/Sources/ContentCards-Custom-UI/CardsInfoViewController.m#L97) para ver un ejemplo de cómo construir tu propia interfaz con fuentes personalizadas.

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Iconos de anclaje personalizados {#custom-pinned-icons}

Al crear una Content Card, los especialistas en marketing tienen la opción de anclar la tarjeta. Una tarjeta anclada se muestra en la parte superior de la fuente de un usuario, y el usuario no puede descartarla. Al personalizar los estilos de tus tarjetas, puedes cambiar la apariencia del icono de anclaje.

![Vista previa de Content Cards en Braze lado a lado para móvil y web con la opción "Anclar esta tarjeta en la parte superior de la fuente" seleccionada.]({% image_buster /assets/img/cc_pin_to_top.png %}){:style="border:none"}

{% tabs %}
{% tab web %}

La estructura del icono de anclaje de Content Cards es:

```css
<div class="ab-pinned-indicator">
  <i class="fa fa-star"></i>
</div>
```

Si quieres usar un icono de FontAwesome diferente, puedes reemplazar el nombre de clase del elemento `i` con el nombre de clase del icono deseado.

Si quieres cambiar el icono por completo, elimina el elemento `i` y agrega el icono personalizado como hijo de `ab-pinned-indicator`. Hay varias formas de cambiar el icono, pero un método sencillo es usar `replaceChildren()` en el elemento `ab-pinned-indicator`.

Por ejemplo:

```javascript
// Get the parent element
const pinnedIndicator = document.querySelector('.ab-pinned-indicator');

// Create a new custom icon element
const customIcon = document.createElement('span');
customIcon.classList.add('customIcon');

// Replace the existing icon with the custom icon
pinnedIndicator.replaceChildren(customIcon);
```

{% endtab %}
{% tab android %}

Para establecer un icono de anclaje personalizado, sobrescribe el estilo `Braze.ContentCards.PinnedIcon`. Tu activo de imagen personalizado debe declararse en el elemento `android:src`. Por ejemplo:

```xml
  <style name="Braze.ContentCards.PinnedIcon">
    <item name="android:src">@drawable/{my_custom_image_here}</item>

    <item name="android:layout_width">wrap_content</item>
    <item name="android:layout_height">wrap_content</item>
    <item name="android:layout_alignParentRight">true</item>
    <item name="android:layout_alignParentTop">true</item>
    <item name="android:contentDescription">@null</item>
    <item name="android:importantForAccessibility">no</item>
  </style>
```

{% endtab %}
{% tab Jetpack Compose %}

Para cambiar el icono de anclaje predeterminado, puedes establecer el [`pinnedResourceId`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards.styling/-content-card-styling/index.html#794044424%2FProperties%2F-1725759721) de `ContentCardStyling`. Por ejemplo:

```kotlin
ContentCardStyling(
    pinnedResourceId = R.drawable.pushpin,
    pinnedImageAlignment = Alignment.TopCenter
)
```

También puedes especificar un Composable en [`pinnedComposable`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards.styling/-content-card-styling/index.html#1460938052%2FProperties%2F-1725759721) de `ContentCardStyling`. Si se especifica `pinnedComposable`, este sobrescribe el valor de `pinnedResourceId`.

```kotlin
ContentCardStyling(
    pinnedComposable = {
        Box(Modifier.fillMaxWidth()) {
            Text(
                modifier = Modifier
                    .align(Alignment.Center)
                    .width(50.dp),
                text = "This message is not read. Please read it."
            )
        }
    }
)
```
{% endtab %}
{% tab swift %}
{% subtabs %}
{% subtab Swift %}

Personaliza el icono de anclaje modificando las propiedades `pinIndicatorColor` y `pinIndicatorImage` de la propiedad de instancia [`cellAttributes`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct/cellattributes/). Por ejemplo:

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.cellAttributes.pinIndicatorColor = .red
attributes.cellAttributes.pinIndicatorImage = UIImage(named: "my-image")

let viewController = BrazeContentCardUI.ViewController.init(braze: braze, attributes: attributes)
```

También puedes usar subclassing para crear tu propia versión personalizada de `BrazeContentCardUI.Cell`, que incluye el indicador de anclaje. Por ejemplo:

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.cells[BrazeContentCardUI.ClassicImageCell.identifier] = CustomClassicImageCell.self

let viewController = BrazeContentCardUI.ViewController(braze: AppDelegate.braze, attributes: attributes)
```

{% endsubtab %}
{% subtab Objective-C %}

La personalización del indicador de anclaje mediante `Attributes` no es compatible en Objective-C.

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Cambiar el color del indicador de no leído {#changing-the-unread-indicator-color}

Las Content Cards contienen una línea azul en la parte inferior de la tarjeta que indica si la tarjeta ha sido vista o no.

![Dos Content Cards mostradas lado a lado. La primera tarjeta tiene una línea azul en la parte inferior, indicando que no ha sido vista. La segunda tarjeta no tiene una línea azul, indicando que ya ha sido vista.]({% image_buster /assets/img/braze-content-cards-seen-unseen-behavior.png %})

{% tabs %}
{% tab web %}

Para cambiar el color del indicador de no leído de una tarjeta, agrega CSS personalizado a tu página web. Por ejemplo, para establecer el color del indicador de no visto en verde:

```css
.ab-unread-indicator { background-color: green; }
```

{% endtab %}
{% tab android %}

Cambia el color de la barra del indicador de no leído modificando el valor en `com_braze_content_cards_unread_bar_color` en tu archivo `colors.xml`:

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <!-- The color used to highlight unread Content Cards at their bottom edge -->
  <color name="com_braze_content_cards_unread_bar_color">#1676d0</color>
</resources>
```

{% endtab %}
{% tab Jetpack Compose %}

Para cambiar el color de la barra del indicador de no leído, modifica el valor de [`unreadIndicatorColor`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards.styling/-content-card-styling/index.html#-1669590042%2FProperties%2F-1725759721) en `ContentCardStyling`:

```kotlin
ContentCardStyling(
    unreadIndicatorColor = Color.Red
)
```

{% endtab %}
{% tab swift %}

{% subtabs %}
{% subtab Swift %}

Cambia el color de la barra del indicador de no leído asignando un valor al color de tinte de tu instancia de `BrazeContentCardUI.ViewController`:

```swift
let viewController = BrazeContentCardUI.ViewController(braze: AppDelegate.braze)
viewController.view.tintColor = .systemGreen
```

Sin embargo, si solo quieres modificar el indicador de no visto, puedes acceder a la propiedad `unviewedIndicatorColor` de tu estructura `BrazeContentCardUI.ViewController.Attributes`. Si usas las implementaciones `UITableViewCell` de Braze, accede a la propiedad antes de que la celda se dibuje.

Por ejemplo, para establecer el color del indicador de no visto en rojo:

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.cellAttributes.unviewedIndicatorColor = .red

let viewController = BrazeContentCardUI.ViewController(braze: AppDelegate.braze, attributes: attributes)
```

Consulta la [aplicación de ejemplo de Examples](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples/Swift) para ver un ejemplo completo.

{% endsubtab %}
{% subtab Objective-C %}

Cambia el color de la barra del indicador de no leído asignando un valor al color de tinte de tu `BRZContentCardUIViewController`:

```objc
BRZContentCardUIViewController *viewController = [[BRZContentCardUIViewController alloc] initWithBraze:AppDelegate.braze];
[viewController.view setTintColor:[UIColor systemGreenColor]];
```

La personalización del indicador de no visto exclusivamente mediante `Attributes` no es compatible en Objective-C.

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Modo oscuro {#dark-mode}

Para mostrar diferentes imágenes o estilos según el modo oscuro o claro del dispositivo, usa [pares clave-valor]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/key_value_pairs) en tu mensaje de Content Card. Por ejemplo, agrega un par clave-valor como `dark_mode_image` con la URL de tu activo de imagen en modo oscuro. Luego, en tu aplicación, agrega lógica personalizada para verificar el modo de apariencia actual del dispositivo y mostrar la imagen adecuada.

{% tabs %}
{% tab swift %}

```swift
if let darkImageUrl = card.extras["dark_mode_image"],
   view.traitCollection.userInterfaceStyle == .dark {
  // Use darkImageUrl for the image
}
```

{% endtab %}
{% tab android %}

```kotlin
val darkModeImage = card.extras["dark_mode_image"]
val isDarkMode = (resources.configuration.uiMode and Configuration.UI_MODE_NIGHT_MASK) == Configuration.UI_MODE_NIGHT_YES
if (isDarkMode && darkModeImage != null) {
    // Use darkModeImage for the image
}
```

{% endtab %}
{% tab web %}

```javascript
const darkModeImage = card.extras?.dark_mode_image;
const isDarkMode = window.matchMedia("(prefers-color-scheme: dark)").matches;
if (isDarkMode && darkModeImage) {
  // Use darkModeImage for the image
}
```

{% endtab %}
{% endtabs %}

Este patrón funciona para cualquier contenido que dependa de la apariencia, incluyendo texto, colores o diseños. Sube tus activos de imagen en modo oscuro a la [biblioteca de medios]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/image_specifications) y luego referéncialos en un par clave-valor.

### Desactivar el indicador de no leído {#disabling-unread-indicator}

{% tabs %}
{% tab web %}

Oculta la barra del indicador de no leído agregando el siguiente estilo a tu `css`:

```css
.ab-unread-indicator { display: none; }
```

{% endtab %}

{% tab android %}

Oculta la barra del indicador de no leído estableciendo [`setUnreadBarVisible`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.view/-content-card-view-holder/set-unread-bar-visible.html?query=fun%20setUnreadBarVisible(isVisible:%20Boolean)) en `ContentCardViewHolder` como `false`.

{% endtab %}

{% tab Jetpack Compose %}
No se admite desactivar el indicador de no leído en Jetpack Compose.
{% endtab %}
{% tab swift %}
{% subtabs %}
{% subtab Swift %}

Oculta la barra del indicador de no leído estableciendo la propiedad `attributes.cellAttributes.unviewedIndicatorColor` en tu estructura `Attributes` como `.clear`.

{% endsubtab %}
{% subtab Objective-C %}

La personalización del indicador de no visto exclusivamente mediante `Attributes` no es compatible en Objective-C.

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}