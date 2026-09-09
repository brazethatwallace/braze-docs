---
nav_title: Stil
article_title: Den Stil der Content Cards anpassen
page_order: 1
description: "Dieser Artikel behandelt die Gestaltungsmöglichkeiten für Ihre Content Cards."
channel:
  - content cards
platform:
  - Android
  - FireOS
  - Swift
  - Web
---

# Den Stil der Content Cards anpassen {#customize-the-style-of-content-cards}

> Braze Content Cards werden mit einem Standard-Look-and-Feel geliefert. Dieser Artikel befasst sich mit den Styling-Optionen für Ihre Content Cards, damit Sie sie an Ihre Markenidentität anpassen können. Eine vollständige Liste der Content-Card-Typen finden Sie unter [Über Content Cards]({{site.baseurl}}/developer_guide/content_cards).

## Einen angepassten Stil erstellen {#creating-a-custom-style}

Die Standard-UI für Content Cards wird aus der UI-Schicht des Braze SDK importiert. Von dort aus können Sie bestimmte Aspekte des Card-Stylings, die Reihenfolge der angezeigten Karten und die Art und Weise, wie der Feed Ihren Nutzer:innen angezeigt wird, anpassen.

![Zwei Content Cards, eine mit der Standardschriftart und eckigen Ecken und eine mit abgerundeten Ecken und einer geschwungenen Schriftart]({% image_buster/assets/img/content_cards/content-card-customization-attributes.png %})

{% alert note %}
Content-Card-Eigenschaften wie `title`, `cardDescription`, `imageUrl` usw. können direkt über das [Dashboard]({{site.baseurl}}/user_guide/channels/content_cards/creative_details) bearbeitet werden, was die bevorzugte Methode ist, um diese Details zu ändern.
{% endalert %}


{% tabs %}
{% tab web %}

Die Standardstile von Braze sind in CSS innerhalb des Braze SDK definiert. Indem Sie ausgewählte Stile in Ihrer Anwendung überschreiben, können Sie unseren Standard-Feed mit Ihren eigenen Hintergrundbildern, Schriftfamilien, Stilen, Größen, Animationen und mehr anpassen. Das folgende Beispiel zeigt etwa eine Überschreibung, die Content Cards mit einer Breite von 800 px darstellt:

``` css
body .ab-feed {
  width: 800px;
}
```

Eine vollständige Liste der Eigenschaften, die Sie ändern können, finden Sie in den [SDK-Konfigurationsoptionen von Braze](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html).

{% endtab %}
{% tab android %}

Standardmäßig entsprechen die Content Cards des Android- und FireOS-SDK den Standard-Android-UI-Richtlinien, um ein nahtloses Erlebnis zu bieten. Diese Standardstile finden Sie in der Datei [`res/values/styles.xml`](https://github.com/braze-inc/braze-android-sdk/blob/master/android-sdk-ui/src/main/res/values/styles.xml) in der Braze-SDK-Distribution:

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

Um das Styling Ihrer Content Cards anzupassen, überschreiben Sie diesen Standardstil. Um einen Stil zu überschreiben, kopieren Sie ihn vollständig in die Datei `styles.xml` in Ihrem Projekt und nehmen Sie Änderungen vor. Der gesamte Stil muss in Ihre lokale `styles.xml`-Datei kopiert werden, damit alle Attribute korrekt gesetzt werden.

{% subtabs local %}
{% subtab Korrekte Stil-Überschreibung %}

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
{% subtab Falsche Stil-Überschreibung %}

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

Standardmäßig entsprechen die Content Cards des Android- und FireOS-SDK den Standard-Android-UI-Richtlinien, um ein nahtloses Erlebnis zu bieten.

Sie können Styling auf zwei Arten anwenden. Die erste Möglichkeit ist, ein [`ContentCardListStyling`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards.styling/-content-card-list-styling/index.html) und [`ContentCardStyling`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards.styling/-content-card-styling/index.html) an [`ContentCardsList`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards/-content-cards-list.html) zu übergeben, wie im folgenden Beispiel:

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

Die zweite Möglichkeit ist, [`BrazeStyle`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose/-braze-style.html) zu verwenden, um ein globales Styling für Braze-Komponenten zu erstellen, wie im folgenden Beispiel:

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

Der Content-Cards-View-Controller ermöglicht es Ihnen, das Erscheinungsbild und Verhalten aller Zellen über das Struct [`BrazeContentCardUI.ViewController.Attributes`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct) anzupassen. Die Konfiguration von Content Cards über `Attributes` ist eine einfache Option, mit der Sie Ihre Content-Cards-UI mit minimalem Aufwand starten können.

{% alert important %}
Die Anpassung über `Attributes` ist nur in Swift verfügbar.
{% endalert %}

{% subtabs %}
{% subtab Swift %}

**`Attributes.default` ändern**

Passen Sie das Erscheinungsbild aller Instanzen des Braze-Content-Card-UI-View-Controllers an, indem Sie die statische Variable [`Attributes.defaults`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct/defaults) direkt ändern.

Um beispielsweise die Standard-Bildgröße und den Eckenradius für alle Zellen zu ändern:

```swift
BrazeContentCardUI.ViewController.Attributes.defaults.cellAttributes.cornerRadius = 20
BrazeContentCardUI.ViewController.Attributes.defaults.cellAttributes.classicImageSize = CGSize(width: 65, height: 65)
```

**Den View-Controller mit Attributes initialisieren**

Wenn Sie nur eine bestimmte Instanz des Braze-Content-Card-UI-View-Controllers ändern möchten, verwenden Sie den Initialisierer [`init(braze:attributes:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/init(braze:attributes:)/), um ein benutzerdefiniertes `Attributes`-Struct an den View-Controller zu übergeben.

Sie können beispielsweise die Bildgröße und den Eckenradius für eine bestimmte Instanz des View-Controllers ändern:

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.cellAttributes.cornerRadius = 20
attributes.cellAttributes.classicImageSize = CGSize(width: 65, height: 65)

let viewController = BrazeContentCardUI.ViewController(braze: AppDelegate.braze, attributes: attributes)
```

**Zellen durch Subclassing anpassen**

Alternativ können Sie benutzerdefinierte Schnittstellen erstellen, indem Sie für jeden gewünschten Kartentyp eigene Klassen registrieren. Um Ihre Subklasse anstelle der Standardzelle zu verwenden, ändern Sie die Eigenschaft [`cells`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct/cells) im `Attributes`-Struct. Beispiel:

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
// Register your own custom cell
attributes.cells[BrazeContentCardUI.ClassicImageCell.identifier] = CustomClassicImageCell.self

let viewController = BrazeContentCardUI.ViewController(braze: AppDelegate.braze, attributes: attributes)
```

**Content Cards programmatisch ändern**

Sie können Content Cards programmatisch ändern, indem Sie den [`transform`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct/transform)-Closure in Ihrem `Attributes`-Struct zuweisen. Das folgende Beispiel ändert den `title` und die `description` kompatibler Karten:

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

Ein vollständiges Beispiel finden Sie in der [Examples-Beispiel-App](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples/Swift).

{% endsubtab %}
{% subtab Objective-C %}

Die Anpassung von Content Cards über `Attributes` wird in Objective-C nicht unterstützt.

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Anpassungsbeispiele {#customization-examples}

### Benutzerdefinierte Schriftart {#custom-font}

Durch die Anpassung der in Ihren Content Cards verwendeten Schriftart können Sie Ihre Markenidentität wahren und eine visuell ansprechende Erfahrung für Ihre Nutzer:innen schaffen. Verwenden Sie diese Rezepte, um die Schriftart für alle Content Cards programmatisch festzulegen.

{% tabs %}
{% tab web %}

Wie bei jedem anderen Web-Element können Sie das Erscheinungsbild von Content Cards einfach über CSS anpassen. Verwenden Sie in Ihrer CSS-Datei oder in Inline-Styles die Eigenschaft `font-family` und geben Sie den gewünschten Schriftartnamen oder Font Stack an.

```css
/* CSS selector targeting the Content Card element */
.card-element {
  font-family: "Helvetica Neue", Arial, sans-serif;
}
```

{% endtab %}
{% tab android %}

Um die Standardschriftart programmatisch zu ändern, legen Sie einen Style für Karten fest und verwenden Sie das Attribut `fontFamily`, um Braze anzuweisen, Ihre benutzerdefinierte Schriftfamilie zu verwenden.

Um beispielsweise die Schriftart aller Titel für Bildkarten mit Beschriftung zu aktualisieren, überschreiben Sie den Style `Braze.ContentCards.CaptionedImage.Title` und referenzieren Sie Ihre benutzerdefinierte Schriftfamilie. Der Attributwert sollte auf eine Schriftfamilie in Ihrem Verzeichnis `res/font` verweisen.

Hier ist ein gekürztes Beispiel mit einer benutzerdefinierten Schriftfamilie, `my_custom_font_family`, die in der letzten Zeile referenziert wird:

```xml
  <style name="Braze.ContentCards.CaptionedImage.Title">
    <item name="android:layout_width">wrap_content</item>
    ...
    <item name="android:fontFamily">@font/my_custom_font_family</item>
    <item name="fontFamily">@font/my_custom_font_family</item>
  </style>
```

Das obige XML-Beispiel zeigt, wie Sie eine benutzerdefinierte Schriftfamilie in Ihren Karten-Styles referenzieren.
{% endtab %}
{% tab Jetpack Compose %}
Um die Standardschriftart programmatisch zu ändern, können Sie den [`titleTextStyle`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards.styling/-content-card-styling/index.html#715371549%2FProperties%2F-1725759721) von `ContentCardStyling` festlegen.

Sie können `titleTextStyle` auch für einen bestimmten Kartentyp festlegen, indem Sie ihn auf [`BrazeShortNewsContentCardStyling`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards.styling/-braze-short-news-content-card-styling/index.html) setzen und an den [`shortNewsContentCardStyle`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards.styling/-content-card-styling/index.html#8580250%2FProperties%2F-1725759721) von `ContentCardStyling` übergeben.

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

Passen Sie Ihre Schriftarten an, indem Sie die `Attributes` der Instanzeigenschaft [`cellAttributes`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct/cellattributes/) anpassen. Zum Beispiel:

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.cellAttributes.titleFont = .preferredFont(textStyle: .callout, weight: .bold)
attributes.cellAttributes.descriptionFont = .preferredFont(textStyle: .footnote, weight: .regular)
attributes.cellAttributes.domainFont = .preferredFont(textStyle: .footnote, weight: .medium)

let viewController = BrazeContentCardUI.ViewController.init(braze: braze, attributes: attributes)
```

{% endsubtab %}
{% subtab Objective-C %}

Die Anpassung von Schriftarten über `Attributes` wird in Objective-C nicht unterstützt.

Sehen Sie sich die [Beispiel-App](https://github.com/braze-inc/braze-swift-sdk/blob/main/Examples/ObjC/Sources/ContentCards-Custom-UI/CardsInfoViewController.m#L97) an, um ein Beispiel für die Erstellung einer eigenen UI mit benutzerdefinierten Schriftarten zu erhalten.

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Benutzerdefinierte Pin-Symbole {#custom-pinned-icons}

Beim Erstellen einer Content Card haben Marketer die Möglichkeit, die Karte anzupinnen. Eine gepinnte Karte wird oben im Feed der Nutzer:innen angezeigt und kann nicht geschlossen werden. Wenn Sie Ihre Karten-Styles anpassen, können Sie auch das Aussehen des Pin-Symbols ändern.

![Vergleich der Content-Card-Vorschau in Braze für Mobilgeräte und Web mit aktivierter Option „Diese Karte oben im Feed anpinnen“.]({% image_buster /assets/img/cc_pin_to_top.png %}){:style="border:none"}

{% tabs %}
{% tab web %}

Die Struktur des Pin-Symbols für Content Cards ist:

```css
<div class="ab-pinned-indicator">
  <i class="fa fa-star"></i>
</div>
```

Wenn Sie ein anderes FontAwesome-Symbol verwenden möchten, ersetzen Sie den Klassennamen des `i`-Elements durch den Klassennamen des gewünschten Symbols.

Wenn Sie das Symbol komplett austauschen möchten, entfernen Sie das `i`-Element und fügen Sie das benutzerdefinierte Symbol als Kindelement von `ab-pinned-indicator` hinzu. Es gibt mehrere Möglichkeiten, das Symbol zu ändern, eine einfache Methode ist die Verwendung von `replaceChildren()` auf dem `ab-pinned-indicator`-Element.

Zum Beispiel:

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

Um ein benutzerdefiniertes Pin-Symbol festzulegen, überschreiben Sie den Style `Braze.ContentCards.PinnedIcon`. Ihr benutzerdefiniertes Bild-Asset sollte im `android:src`-Element deklariert werden. Zum Beispiel:

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

Um das Standard-Pin-Symbol zu ändern, können Sie die [`pinnedResourceId`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards.styling/-content-card-styling/index.html#794044424%2FProperties%2F-1725759721) von `ContentCardStyling` festlegen. Zum Beispiel:

```kotlin
ContentCardStyling(
    pinnedResourceId = R.drawable.pushpin,
    pinnedImageAlignment = Alignment.TopCenter
)
```

Sie können auch ein Composable in [`pinnedComposable`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards.styling/-content-card-styling/index.html#1460938052%2FProperties%2F-1725759721) von `ContentCardStyling` angeben. Wenn `pinnedComposable` angegeben ist, überschreibt es den `pinnedResourceId`-Wert.

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

Passen Sie das Pin-Symbol an, indem Sie die Eigenschaften `pinIndicatorColor` und `pinIndicatorImage` der Instanzeigenschaft [`cellAttributes`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct/cellattributes/) ändern. Zum Beispiel:

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.cellAttributes.pinIndicatorColor = .red
attributes.cellAttributes.pinIndicatorImage = UIImage(named: "my-image")

let viewController = BrazeContentCardUI.ViewController.init(braze: braze, attributes: attributes)
```

Sie können auch Subclassing verwenden, um Ihre eigene benutzerdefinierte Version von `BrazeContentCardUI.Cell` zu erstellen, die den Pin-Indikator enthält. Zum Beispiel:

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.cells[BrazeContentCardUI.ClassicImageCell.identifier] = CustomClassicImageCell.self

let viewController = BrazeContentCardUI.ViewController(braze: AppDelegate.braze, attributes: attributes)
```

{% endsubtab %}
{% subtab Objective-C %}

Die Anpassung des Pin-Indikators über `Attributes` wird in Objective-C nicht unterstützt.

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Farbe des Ungelesen-Indikators ändern {#changing-the-unread-indicator-color}

Content Cards enthalten eine blaue Linie am unteren Rand der Karte, die anzeigt, ob die Karte bereits angesehen wurde oder nicht.

![Zwei Content Cards nebeneinander. Die erste Karte hat eine blaue Linie am unteren Rand, die anzeigt, dass sie noch nicht gesehen wurde. Die zweite Karte hat keine blaue Linie, was bedeutet, dass sie bereits gesehen wurde.]({% image_buster /assets/img/braze-content-cards-seen-unseen-behavior.png %})

{% tabs %}
{% tab web %}

Um die Farbe des Ungelesen-Indikators einer Karte zu ändern, fügen Sie benutzerdefiniertes CSS zu Ihrer Webseite hinzu. Um beispielsweise die Farbe des Indikators auf Grün zu setzen:

```css
.ab-unread-indicator { background-color: green; }
```

{% endtab %}
{% tab android %}

Ändern Sie die Farbe des Ungelesen-Indikators, indem Sie den Wert von `com_braze_content_cards_unread_bar_color` in Ihrer `colors.xml`-Datei anpassen:

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <!-- The color used to highlight unread Content Cards at their bottom edge -->
  <color name="com_braze_content_cards_unread_bar_color">#1676d0</color>
</resources>
```

{% endtab %}
{% tab Jetpack Compose %}

Um die Farbe des Ungelesen-Indikators zu ändern, passen Sie den Wert von [`unreadIndicatorColor`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards.styling/-content-card-styling/index.html#-1669590042%2FProperties%2F-1725759721) in `ContentCardStyling` an:

```kotlin
ContentCardStyling(
    unreadIndicatorColor = Color.Red
)
```

{% endtab %}
{% tab swift %}

{% subtabs %}
{% subtab Swift %}

Ändern Sie die Farbe des Ungelesen-Indikators, indem Sie der Tint-Color Ihrer `BrazeContentCardUI.ViewController`-Instanz einen Wert zuweisen:

```swift
let viewController = BrazeContentCardUI.ViewController(braze: AppDelegate.braze)
viewController.view.tintColor = .systemGreen
```

Wenn Sie jedoch nur den Ungesehen-Indikator ändern möchten, können Sie auf die Eigenschaft `unviewedIndicatorColor` Ihrer `BrazeContentCardUI.ViewController.Attributes`-Struktur zugreifen. Wenn Sie Braze-`UITableViewCell`-Implementierungen verwenden, greifen Sie auf die Eigenschaft zu, bevor die Zelle gezeichnet wird.

Um beispielsweise die Farbe des Ungesehen-Indikators auf Rot zu setzen:

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.cellAttributes.unviewedIndicatorColor = .red

let viewController = BrazeContentCardUI.ViewController(braze: AppDelegate.braze, attributes: attributes)
```

Ein vollständiges Beispiel finden Sie in der [Beispiel-App](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples/Swift).

{% endsubtab %}
{% subtab Objective-C %}

Ändern Sie die Farbe des Ungelesen-Indikators, indem Sie der Tint-Color Ihres `BRZContentCardUIViewController` einen Wert zuweisen:

```objc
BRZContentCardUIViewController *viewController = [[BRZContentCardUIViewController alloc] initWithBraze:AppDelegate.braze];
[viewController.view setTintColor:[UIColor systemGreenColor]];
```

Die Anpassung nur des Ungesehen-Indikators über `Attributes` wird in Objective-C nicht unterstützt.

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Dark Mode {#dark-mode}

Um je nach Dark oder Light Mode des Geräts unterschiedliche Bilder oder Styles anzuzeigen, verwenden Sie [Schlüssel-Wert-Paare]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/key_value_pairs) in Ihrer Content-Card-Nachricht. Fügen Sie beispielsweise ein Schlüssel-Wert-Paar wie `dark_mode_image` mit der URL Ihres Dark-Mode-Bild-Assets hinzu. Fügen Sie dann in Ihrer App benutzerdefinierte Logik hinzu, um den aktuellen Darstellungsmodus des Geräts zu prüfen und das entsprechende Bild anzuzeigen.

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

Dieses Muster funktioniert für alle darstellungsabhängigen Inhalte, einschließlich Text, Farben oder Layouts. Laden Sie Ihre Dark-Mode-Bild-Assets in die [Mediathek]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/image_specifications) hoch und referenzieren Sie sie dann in einem Schlüssel-Wert-Paar.

### Ungelesen-Indikator deaktivieren {#disabling-unread-indicator}

{% tabs %}
{% tab web %}

Blenden Sie den Ungelesen-Indikator aus, indem Sie den folgenden Style zu Ihrem `css` hinzufügen:

```css
.ab-unread-indicator { display: none; }
```

{% endtab %}

{% tab android %}

Blenden Sie den Ungelesen-Indikator aus, indem Sie [`setUnreadBarVisible`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.view/-content-card-view-holder/set-unread-bar-visible.html?query=fun%20setUnreadBarVisible(isVisible:%20Boolean)) auf `ContentCardViewHolder` auf `false` setzen.

{% endtab %}

{% tab Jetpack Compose %}
Das Deaktivieren des Ungelesen-Indikators wird in Jetpack Compose nicht unterstützt.
{% endtab %}
{% tab swift %}
{% subtabs %}
{% subtab Swift %}

Blenden Sie den Ungelesen-Indikator aus, indem Sie die Eigenschaft `attributes.cellAttributes.unviewedIndicatorColor` in Ihrer `Attributes`-Struktur auf `.clear` setzen.

{% endsubtab %}
{% subtab Objective-C %}

Die Anpassung nur des Ungesehen-Indikators über `Attributes` wird in Objective-C nicht unterstützt.

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}