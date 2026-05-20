---
nav_title: スタイル
article_title: Content Cardsのスタイルをカスタマイズする
page_order: 1
description: "この記事では、Content Cardsのスタイルオプションについて説明します。"
channel:
  - content cards
platform:
  - Android
  - FireOS
  - Swift
  - Web
---

# Content Cardsのスタイルをカスタマイズする {#customize-the-style-of-content-cards}

> Braze Content Cardsには、デフォルトのルックアンドフィールが含まれています。この記事では、ブランドアイデンティティに合わせるためのContent Cardsのスタイルオプションについて説明します。コンテンツカードタイプの完全なリストについては、[Content Cardsについて]({{site.baseurl}}/developer_guide/content_cards/)を参照してください。

## カスタムスタイルの作成 {#creating-a-custom-style}

デフォルトのContent Cards UIは、Braze SDKのUIレイヤーからインポートされます。そこから、カードのスタイルの特定の部分、カードが表示される順序、フィードがユーザーに表示される方法を調整できます。

![2枚のコンテンツカード。1枚はデフォルトのフォントで角が四角いもの、もう1枚は角が丸くカーリーフォントのもの]({% image_buster/assets/img/content_cards/content-card-customization-attributes.png %})

{% alert note %}
Content Cardsのプロパティ（`title`、`cardDescription`、`imageUrl` など）は、[ダッシュボード]({{site.baseurl}}/user_guide/channels/content_cards/creative_details/)から直接編集できます。これは、詳細を変更するための推奨される方法です。
{% endalert %}


{% tabs %}
{% tab web %}

Brazeのデフォルトスタイルは、Braze SDK内のCSSで定義されています。アプリケーションで選択したスタイルをオーバーライドすることで、標準フィードを独自の背景画像、フォントファミリー、スタイル、サイズ、アニメーションなどでカスタマイズできます。例えば、以下のオーバーライドはContent Cardsを幅800ピクセルで表示させる例です。

``` css
body .ab-feed {
  width: 800px;
}
```

変更可能なプロパティの完全な一覧については、[BrazeのSDK設定オプション](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html)を参照してください。

{% endtab %}
{% tab android %}

デフォルトでは、AndroidおよびFireOS SDKのContent Cardsは標準のAndroid UIガイドラインに準拠し、シームレスなエクスペリエンスを提供します。これらのデフォルトのスタイルは、Braze SDKディストリビューション内の[`res/values/styles.xml`](https://github.com/braze-inc/braze-android-sdk/blob/master/android-sdk-ui/src/main/res/values/styles.xml)ファイルで確認できます。

`````````xml
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

Content Cardsのスタイルをカスタマイズするには、このデフォルトのスタイルをオーバーライドします。スタイルをオーバーライドするには、スタイル全体をプロジェクトの`styles.xml`ファイルにコピーし、変更を加えます。すべての属性が正しく設定されるようにするには、スタイル全体をローカルの`styles.xml`にコピーする必要があります。

{% subtabs local %}
{% subtab Correct style override %}

`````````xml
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
{% subtab Incorrect style override %}

`````````xml
<style name="Braze.ContentCardsDisplay">
  <item name="android:background">@color/mint</item>
  <item name="android:cacheColorHint">@color/mint</item>
</style>
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Jetpack Compose %}

デフォルトでは、AndroidおよびFireOS SDKのContent Cardsは標準のAndroid UIガイドラインに準拠し、シームレスなエクスペリエンスを提供します。

2つの方法のいずれかでスタイルを適用できます。1つ目は、以下の例のように、[`ContentCardListStyling`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards.styling/-content-card-list-styling/index.html)および[`ContentCardStyling`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards.styling/-content-card-styling/index.html)を[`ContentCardsList`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards/-content-cards-list.html)に渡す方法です。

`````````kotlin
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

2つ目は、以下の例のように、[`BrazeStyle`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose/-braze-style.html)を使用してBrazeコンポーネントのグローバルスタイルを作成する方法です。

`````````kotlin
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

Content Cardsビューコントローラーを使用すると、[`BrazeContentCardUI.ViewController.Attributes`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct)構造体を介してすべてのセルの外観と動作をカスタマイズできます。`Attributes`を使用したContent Cardsの設定は簡単なオプションであり、最小限のセットアップでContent Cards UIを起動できます。

{% alert important %}
`Attributes`によるカスタマイズは、Swiftでのみ利用可能です。
{% endalert %}

{% subtabs %}
{% subtab Swift %}

**`Attributes.default`の変更**

静的[`Attributes.defaults`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct/defaults)変数を直接変更して、Braze Content Cards UIビューコントローラーのすべてのインスタンスのルックアンドフィールをカスタマイズします。

たとえば、すべてのセルのデフォルトの画像サイズと角の半径を変更するには、次のようにします。

`````````swift
BrazeContentCardUI.ViewController.Attributes.defaults.cellAttributes.cornerRadius = 20
BrazeContentCardUI.ViewController.Attributes.defaults.cellAttributes.classicImageSize = CGSize(width: 65, height: 65)
```

**Attributesを使用してビューコントローラーを初期化する**

Braze Content Cards UIビューコントローラーの特定のインスタンスのみを変更する場合は、[`init(braze:attributes:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/init(braze:attributes:)/)イニシャライザーを使用してカスタムの`Attributes`構造体をビューコントローラーに渡します。

たとえば、ビューコントローラーの特定のインスタンスの画像サイズと角の半径を変更できます。

`````````swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.cellAttributes.cornerRadius = 20
attributes.cellAttributes.classicImageSize = CGSize(width: 65, height: 65)

let viewController = BrazeContentCardUI.ViewController(braze: AppDelegate.braze, attributes: attributes)
```

**サブクラス化によるセルのカスタマイズ**

また、必要なカードタイプごとにカスタムクラスを登録して、カスタムインターフェイスを作成することもできます。デフォルトのセルの代わりにサブクラスを使用するには、`Attributes`構造体の[`cells`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct/cells)プロパティを変更します。以下に例を示します。

`````````swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
// Register your own custom cell
attributes.cells[BrazeContentCardUI.ClassicImageCell.identifier] = CustomClassicImageCell.self

let viewController = BrazeContentCardUI.ViewController(braze: AppDelegate.braze, attributes: attributes)
```

**プログラムによるContent Cardsの変更**

`Attributes`構造体に[`transform`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct/transform)クロージャを割り当てることで、プログラムでContent Cardsを変更できます。以下の例では、互換性のあるカードの`title`と`description`を変更しています。

`````````swift
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

完全な例については、[Examplesサンプルアプリ](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples/Swift)を確認してください。

{% endsubtab %}
{% subtab Objective-C %}

`Attributes`によるContent Cardsのカスタマイズは、Objective-Cではサポートされていません。

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## カスタマイズの例 {#customization-examples}

### カスタムフォント {#custom-font}

Content Cardsで使用されるフォントをカスタマイズすると、ブランドアイデンティティを維持し、ユーザーにとって視覚的に魅力的なエクスペリエンスを作成できます。以下のレシピを使用して、すべてのContent Cardsのフォントをプログラムで設定します。

{% tabs %}
{% tab web %}

他のWeb要素と同様に、CSSを使用してContent Cardsの外観を簡単にカスタマイズできます。CSSファイルまたはインラインスタイルで、`font-family`プロパティを使用して、希望のフォント名またはフォントスタックを指定します。

`````````css
/* CSS selector targeting the Content Card element */
.card-element {
  font-family: "Helvetica Neue", Arial, sans-serif;
}
```

{% endtab %}
{% tab android %}

デフォルトのフォントをプログラムで変更するには、カードのスタイルを設定し、`fontFamily`属性を使用して、カスタムフォントファミリーを使用するようにBrazeに指示します。

たとえば、キャプション付き画像カードのすべてのタイトルのフォントを更新するには、`Braze.ContentCards.CaptionedImage.Title`スタイルをオーバーライドし、カスタムフォントファミリーを参照します。属性値は、`res/font`ディレクトリのフォントファミリーを指す必要があります。

以下は、最後の行でカスタムフォントファミリー`my_custom_font_family`を参照している省略されたコード例です。

`````````xml
  <style name="Braze.ContentCards.CaptionedImage.Title">
    <item name="android:layout_width">wrap_content</item>
    ...
    <item name="android:fontFamily">@font/my_custom_font_family</item>
    <item name="fontFamily">@font/my_custom_font_family</item>
  </style>
```

Android SDKでのフォントのカスタマイズの詳細については、[フォントファミリーガイド]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/font_customization/#font-customization)を参照してください。
{% endtab %}
{% tab Jetpack Compose %}
デフォルトのフォントをプログラムで変更するには、`ContentCardStyling`の[`titleTextStyle`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards.styling/-content-card-styling/index.html#715371549%2FProperties%2F-1725759721)を設定します。

また、[`BrazeShortNewsContentCardStyling`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards.styling/-braze-short-news-content-card-styling/index.html)に設定し、`ContentCardStyling`の[`shortNewsContentCardStyle`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards.styling/-content-card-styling/index.html#8580250%2FProperties%2F-1725759721)に渡すことで、特定のカードタイプに`titleTextStyle`を設定することもできます。

`````````kotlin
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

[`cellAttributes`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct/cellattributes/)インスタンスプロパティの`Attributes`をカスタマイズして、フォントをカスタマイズします。以下に例を示します。

`````````swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.cellAttributes.titleFont = .preferredFont(textStyle: .callout, weight: .bold)
attributes.cellAttributes.descriptionFont = .preferredFont(textStyle: .footnote, weight: .regular)
attributes.cellAttributes.domainFont = .preferredFont(textStyle: .footnote, weight: .medium)

let viewController = BrazeContentCardUI.ViewController.init(braze: braze, attributes: attributes)
```

{% endsubtab %}
{% subtab Objective-C %}

`Attributes`によるフォントのカスタマイズは、Objective-Cではサポートされていません。

カスタムフォントを使用して独自のUIを構築する例については、[Examplesサンプルアプリ](https://github.com/braze-inc/braze-swift-sdk/blob/main/Examples/ObjC/Sources/ContentCards-Custom-UI/CardsInfoViewController.m#L97)を確認してください。

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### カスタムの固定アイコン {#custom-pinned-icons}

Content Cardsの作成時、マーケターはカードを固定するオプションを選択できます。固定されたカードはユーザーのフィードの上部に表示され、ユーザーはそれを閉じることができません。カードスタイルをカスタマイズする際に、固定アイコンの見た目を変更できます。

![Brazeのモバイルおよび Web向けContent Cardsプレビューを、「このカードをフィードの先頭にピン留めする」オプションを選択した状態で並べて表示]({% image_buster /assets/img/cc_pin_to_top.png %}){:style="border:none"}

{% tabs %}
{% tab web %}

Content Cardsの固定アイコンの構造は次のとおりです。

`````````css
<div class="ab-pinned-indicator">
  <i class="fa fa-star"></i>
</div>
```

別のFontAwesomeアイコンを使用したい場合は、`i`要素のクラス名を目的のアイコンのクラス名に置き換えます。

アイコンを完全に切り替えたい場合は、`i`要素を削除し、カスタムアイコンを`ab-pinned-indicator`の子要素として追加します。アイコンを変更する方法はいくつかありますが、簡単な方法の一つは、`ab-pinned-indicator`要素に`replaceChildren()`を使用することです。

以下に例を示します。

`````````javascript
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

カスタムの固定アイコンを設定するには、`Braze.ContentCards.PinnedIcon`スタイルをオーバーライドします。カスタム画像アセットは、`android:src`要素で宣言する必要があります。以下に例を示します。

`````````xml
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

デフォルトの固定アイコンを変更するには、`ContentCardStyling`の[`pinnedResourceId`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards.styling/-content-card-styling/index.html#794044424%2FProperties%2F-1725759721)を設定します。以下に例を示します。

`````````kotlin
ContentCardStyling(
    pinnedResourceId = R.drawable.pushpin,
    pinnedImageAlignment = Alignment.TopCenter
)
```

`ContentCardStyling`の[`pinnedComposable`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards.styling/-content-card-styling/index.html#1460938052%2FProperties%2F-1725759721)にComposableを指定することもできます。`pinnedComposable`が指定された場合、`pinnedResourceId`の値がオーバーライドされます。

`````````kotlin
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

固定アイコンをカスタマイズするには、[`cellAttributes`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct/cellattributes/)インスタンスプロパティの`pinIndicatorColor`と`pinIndicatorImage`のプロパティを変更します。以下に例を示します。

`````````swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.cellAttributes.pinIndicatorColor = .red
attributes.cellAttributes.pinIndicatorImage = UIImage(named: "my-image")

let viewController = BrazeContentCardUI.ViewController.init(braze: braze, attributes: attributes)
```

サブクラス化を使用して、ピンインジケーターを含む`BrazeContentCardUI.Cell`のカスタムバージョンを独自に作成することもできます。以下に例を示します。

`````````swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.cells[BrazeContentCardUI.ClassicImageCell.identifier] = CustomClassicImageCell.self

let viewController = BrazeContentCardUI.ViewController(braze: AppDelegate.braze, attributes: attributes)
```

{% endsubtab %}
{% subtab Objective-C %}

`Attributes`によるピンインジケーターのカスタマイズは、Objective-Cではサポートされていません。

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### 未読インジケーターの色の変更 {#changing-the-unread-indicator-color}

Content Cardsの下部には、カードが閲覧されたかどうかを示す青い線が表示されます。

![2枚のContent Cardsが並んで表示されている。最初のカードの下部には青い線があり、まだ閲覧されていないことを示している。2番目のカードには青い線がなく、すでに閲覧されたことを示している。]({% image_buster /assets/img/braze-content-cards-seen-unseen-behavior.png %})

{% tabs %}
{% tab web %}

カードの未読インジケーターの色を変更するには、WebページにカスタムCSSを追加します。たとえば、未閲覧インジケーターの色を緑に設定するには、次のようにします。

`````````css
.ab-unread-indicator { background-color: green; }
```

{% endtab %}
{% tab android %}

未読インジケーターバーの色を変更するには、`colors.xml`ファイルの`com_braze_content_cards_unread_bar_color`の値を変更します。

`````````xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <!-- The color used to highlight unread Content Cards at their bottom edge -->
  <color name="com_braze_content_cards_unread_bar_color">#1676d0</color>
</resources>
```

{% endtab %}
{% tab Jetpack Compose %}

未読インジケーターバーの色を変更するには、`ContentCardStyling`の[`unreadIndicatorColor`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards.styling/-content-card-styling/index.html#-1669590042%2FProperties%2F-1725759721)の値を変更します。

`````````kotlin
ContentCardStyling(
    unreadIndicatorColor = Color.Red
)
```

{% endtab %}
{% tab swift %}

{% subtabs %}
{% subtab Swift %}

未読インジケーターバーの色を変更するには、`BrazeContentCardUI.ViewController`インスタンスのティントカラーに値を割り当てます。

`````````swift
let viewController = BrazeContentCardUI.ViewController(braze: AppDelegate.braze)
viewController.view.tintColor = .systemGreen
```

ただし、未閲覧インジケーターのみを変更したい場合は、`BrazeContentCardUI.ViewController.Attributes`構造体の`unviewedIndicatorColor`プロパティにアクセスします。Brazeの`UITableViewCell`実装を使用する場合、セルが描画される前にプロパティにアクセスしてください。

たとえば、未閲覧インジケーターの色を赤に設定するには、次のようにします。

`````````swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.cellAttributes.unviewedIndicatorColor = .red

let viewController = BrazeContentCardUI.ViewController(braze: AppDelegate.braze, attributes: attributes)
```

完全な例については、[Examplesサンプルアプリ](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples/Swift)を確認してください。

{% endsubtab %}
{% subtab Objective-C %}

未読インジケーターバーの色を変更するには、`BRZContentCardUIViewController`のティントカラーに値を割り当てます。

`````````objc
BRZContentCardUIViewController *viewController = [[BRZContentCardUIViewController alloc] initWithBraze:AppDelegate.braze];
[viewController.view setTintColor:[UIColor systemGreenColor]];
```

`Attributes`による未閲覧インジケーターのみのカスタマイズは、Objective-Cではサポートされていません。

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### ダークモード {#dark-mode}

デバイスのダークモードまたはライトモードに基づいて異なる画像やスタイルを表示するには、Content Cardsメッセージで[キーと値のペア]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details/#key-value-pairs)を使用します。たとえば、`dark_mode_image`というキーと値のペアにダークモード画像アセットのURLを追加します。次に、アプリにカスタムロジックを追加して、デバイスの現在の外観モードを確認し、適切な画像を表示します。

{% tabs %}
{% tab swift %}

`````````swift
if let darkImageUrl = card.extras["dark_mode_image"],
   view.traitCollection.userInterfaceStyle == .dark {
  // Use darkImageUrl for the image
}
```

{% endtab %}
{% tab android %}

`````````kotlin
val darkModeImage = card.extras["dark_mode_image"]
val isDarkMode = (resources.configuration.uiMode and Configuration.UI_MODE_NIGHT_MASK) == Configuration.UI_MODE_NIGHT_YES
if (isDarkMode && darkModeImage != null) {
    // Use darkModeImage for the image
}
```

{% endtab %}
{% tab web %}

`````````javascript
const darkModeImage = card.extras?.dark_mode_image;
const isDarkMode = window.matchMedia("(prefers-color-scheme: dark)").matches;
if (isDarkMode && darkModeImage) {
  // Use darkModeImage for the image
}
```

{% endtab %}
{% endtabs %}

このパターンは、テキスト、色、レイアウトなど、外観に依存するあらゆるコンテンツに使用できます。ダークモードの画像アセットを[メディアライブラリ]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/image_specifications/)にアップロードし、キーと値のペアで参照します。

### 未読インジケーターを無効にする {#disabling-unread-indicator}

{% tabs %}
{% tab web %}

未読インジケーターバーを非表示にするには、`css`に次のスタイルを追加します。

`````````css
.ab-unread-indicator { display: none; }
```

{% endtab %}

{% tab android %}

未読インジケーターバーを非表示にするには、`ContentCardViewHolder`の[`setUnreadBarVisible`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.view/-content-card-view-holder/set-unread-bar-visible.html?query=fun%20setUnreadBarVisible(isVisible:%20Boolean))を`false`に設定します。

{% endtab %}

{% tab Jetpack Compose %}
未読インジケーターの無効化は、Jetpack Composeではサポートされていません。
{% endtab %}
{% tab swift %}
{% subtabs %}
{% subtab Swift %}

未読インジケーターバーを非表示にするには、`Attributes`構造体の`attributes.cellAttributes.unviewedIndicatorColor`プロパティを`.clear`に設定します。

{% endsubtab %}
{% subtab Objective-C %}

`Attributes`による未閲覧インジケーターのみのカスタマイズは、Objective-Cではサポートされていません。

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}