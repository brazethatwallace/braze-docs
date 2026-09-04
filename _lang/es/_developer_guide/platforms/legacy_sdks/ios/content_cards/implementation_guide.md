---
nav_title: Implementación avanzada (opcional)
article_title: Guía de implementación de Content Cards para iOS (opcional)
platform: iOS
page_order: 7
description: "Esta guía de implementación avanzada abarca consideraciones sobre códigos de Content Cards de iOS, tres casos de uso creados por nuestro equipo, fragmentos de código que los acompañan y orientaciones sobre el registro de impresiones, clics y descartes."
channel:
  - content cards

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

<br>
{% alert important %}
¿Buscas la guía básica de integración del desarrollador de Content Cards? Encuéntrala en la [guía básica de integración del desarrollador de Content Cards]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/content_cards/integration).
{% endalert %}

# Guía de implementación de Content Cards {#content-card-implementation-guide}

> Esta guía de implementación opcional y avanzada abarca consideraciones sobre códigos de Content Cards, tres casos de uso personalizados creados por nuestro equipo, fragmentos de código que los acompañan y orientaciones sobre el registro de impresiones, clics y descartes. ¡Visita nuestro repositorio de demostraciones Braze en [GitHub](https://github.com/braze-inc/braze-growth-shares-ios-demo-app)! Ten en cuenta que esta guía de implementación se centra en una implementación Swift, pero se proporcionan fragmentos de código Objective-C para los interesados.

## Consideraciones sobre códigos {#code-considerations}

### Content Cards como objetos personalizados {#content-cards-as-custom-objects}

Al igual que un cohete que añade un propulsor, tus propios objetos personalizados se pueden ampliar para funcionar como Content Cards. Las superficies de API limitadas como esta proporcionan flexibilidad para trabajar con diferentes backends de datos de forma intercambiable. Esto se puede hacer conformando el protocolo `ContentCardable` e implementando el inicializador (como se muestra en los siguientes fragmentos de código) y, mediante el uso de la estructura `ContentCardData`, te permite acceder a los datos de `ABKContentCard`. La carga útil de `ABKContentCard` se utilizará para inicializar la estructura `ContentCardData` y el propio objeto personalizado, todo desde un tipo `Dictionary` a través del inicializador que proporciona el protocolo.

El inicializador también incluye una enumeración `ContentCardClassType`. Esta enumeración se utiliza para decidir qué objeto inicializar. Mediante el uso de pares clave-valor dentro del panel de Braze, puedes establecer una clave `class_type` explícita que se utilizará para determinar qué objeto inicializar. Estos pares clave-valor para Content Cards se reciben a través de la variable `extras` en `ABKContentCard`. Otro componente fundamental del inicializador es el parámetro de diccionario `metaData`. Los `metaData` incluyen todo lo del `ABKContentCard` descompuesto en una serie de claves y valores. Una vez que las tarjetas relevantes se analizan y se convierten en tus objetos personalizados, la aplicación está lista para comenzar a trabajar con ellos como si hubieran sido instanciados desde JSON o cualquier otra fuente.

Una vez que tengas una comprensión sólida de estas consideraciones sobre códigos, consulta nuestros [ejemplos](#sample-use-cases) para empezar a implementar tus objetos personalizados.

{% tabs local %}
{% tab ContentCardable %}
{% subtabs global %}
{% subtab Swift %}
**Protocolo ContentCardable**<br>
Un objeto `ContentCardData` que representa los datos de `ABKContentCard` junto con una enumeración `ContentCardClassType`. Un inicializador utilizado para instanciar objetos personalizados con metadatos de `ABKContentCard`.
```swift
protocol ContentCardable {
  var contentCardData: ContentCardData? { get }
  init?(metaData: [ContentCardKey: Any], classType contentCardClassType: ContentCardClassType)
}

extension ContentCardable {
  var isContentCard: Bool {
    return contentCardData != nil
  }

  func logContentCardClicked() {
    BrazeManager.shared.logContentCardClicked(idString: contentCardData?.contentCardId)
  }

  func logContentCardDismissed() {
    BrazeManager.shared.logContentCardDismissed(idString: contentCardData?.contentCardId)
  }

  func logContentCardImpression() {
    BrazeManager.shared.logContentCardImpression(idString: contentCardData?.contentCardId)
  }
}
```
**Estructura de datos de Content Card**<br>
`ContentCardData` representa los valores analizados de un `ABKContentCard`.

```swift
struct ContentCardData: Hashable {
  let contentCardId: String
  let contentCardClassType: ContentCardClassType
  let createdAt: Double
  let isDismissable: Bool
  ...
  // other Content Card properties such as expiresAt, pinned, etc.
}

extension ContentCardData: Equatable {
  static func ==(lhs: ContentCardData, rhs: ContentCardData) -> Bool {
    return lhs.contentCardId == rhs.contentCardId
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
**Protocolo ContentCardable**<br>
Un objeto `ContentCardData` que representa los datos de `ABKContentCard` junto con una enumeración `ContentCardClassType`, un inicializador utilizado para instanciar objetos personalizados con metadatos de `ABKContentCard`.
```objc
@protocol ContentCardable <NSObject>

@property (nonatomic, strong) ContentCardData *contentCardData;
- (instancetype __nullable)initWithMetaData:(NSDictionary *)metaData
                                  classType:(enum ContentCardClassType)classType;

- (BOOL)isContentCard;
- (void)logContentCardImpression;
- (void)logContentCardClicked;
- (void)logContentCardDismissed;

@end
```
**Estructura de datos de Content Card**<br>
`ContentCardData` representa los valores analizados de un `ABKContentCard`.

```objc
@interface ContentCardData : NSObject

+ (ContentCardClassType)contentCardClassTypeForString:(NSString *)rawValue;

- (instancetype)initWithIdString:(NSString *)idString
                       classType:(ContentCardClassType)classType
                       createdAt:(double)createdAt isDismissible:(BOOL)isDismissible;

@property (nonatomic, readonly) NSString *contentCardId;
@property (nonatomic) ContentCardClassType classType;
@property (nonatomic, readonly) double *createdAt;
@property (nonatomic, readonly) BOOL isDismissible;
...
// other Content Card properties such as expiresAt, pinned, etc.

@end
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Custom Objects %}
{% subtabs global %}
{% subtab Swift %}
**Inicializador de objeto personalizado**<br>
Los metadatos de un `ABKContentCard` se utilizan para rellenar las variables de tu objeto. Los pares clave-valor configurados en el panel de Braze se representan en el diccionario "extras".

```swift
extension CustomObject: ContentCardable {
  init?(metaData: [ContentCardKey: Any], classType contentCardClassType: ContentCardClassType) {
    guard let idString = metaData[.idString] as? String,
      let createdAt = metaData[.created] as? Double,
      let isDismissable = metaData[.dismissable] as? Bool,
      let extras = metaData[.extras] as? [AnyHashable: Any],
      else { return nil }

    let contentCardData = ContentCardData(contentCardId: idString, contentCardClassType: contentCardClassType, createdAt: createdAt, isDismissable: isDismissable)
    let customObjectProperty = extras["YOUR-CUSTOM-OBJECT-PROPERTY"] as? String

    self.init(contentCardData: contentCardData, property: customObjectProperty)
  }
}
```

**Identificación de tipos**<br>
La enumeración `ContentCardClassType` representa el valor de `class_type` en el panel de Braze. Este valor también se utiliza como identificador de filtro para mostrar Content Cards en diferentes lugares.

```swift
enum ContentCardClassType: Hashable {
  case yourValue
  case yourOtherValue
  ...
  case none

  init(rawType: String?) {
    switch rawType?.lowercased() {
    case "your_value": // these values much match the value set in the Braze dashboard
      self = .yourValue
    case "your_other_value": // these values much match the value set in the Braze dashboard
      self = .yourOtherValue
    ...
    default:
      self = .none
    }
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
**Inicializador de objeto personalizado**<br>
Los metadatos de un `ABKContentCard` se utilizan para rellenar las variables de tu objeto. Los pares clave-valor configurados en el panel de Braze se representan en el diccionario "extras".


```objc
- (id _Nullable)initWithMetaData:(nonnull NSDictionary *)metaData classType:(enum ContentCardClassType)classType {
  self = [super init];
  if (self) {
    if ([metaData objectForKey:ContentCardKeyIdString] && [metaData objectForKey:ContentCardKeyCreated] && [metaData objectForKey:ContentCardKeyDismissible] && [metaData objectForKey:ContentCardKeyExtras]) {
      NSDictionary  *extras = metaData[ContentCardKeyExtras];
      NSString *idString = metaData[ContentCardKeyIdString];
      double createdAt = [metaData[ContentCardKeyCreated] doubleValue];
      BOOL isDismissible = metaData[ContentCardKeyDismissible];

      if ([extras objectForKey: @"YOUR-CUSTOM-PROPERTY")
        _customObjectProperty = extras[@"YOUR-CUSTOM-OBJECT-PROPERTY"];

      self.contentCardData = [[ContentCardData alloc] initWithIdString:idString classType:classType createdAt:createdAt isDismissible:isDismissible];

      return self;
    }
  }
  return nil;
}
```

**Identificación de tipos**<br>
La enumeración `ContentCardClassType` representa el valor de `class_type` en el panel de Braze. Este valor también se utiliza como identificador de filtro para mostrar Content Cards en diferentes lugares.

```objc
typedef NS_ENUM(NSInteger, ContentCardClassType) {
  ContentCardClassTypeNone = 0,
  ContentCardClassTypeYourValue,
  ContentCardClassTypeYourOtherValue,
  ...
};

+ (NSArray *)contentCardClassTypeArray {
  return @[ @"", @"your_value", @"your_other_value" ];
}

+ (ContentCardClassType)contentCardClassTypeForString:(NSString*)rawValue {
  if ([[self contentCardClassTypeArray] indexOfObject:rawValue] == NSNotFound) {
    return ContentCardClassTypeNone;
  } else {
    NSInteger value = [[self contentCardClassTypeArray] indexOfObject:rawValue];
    return (ContentCardClassType) value;
  }
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Handling Content Cards %}
{% subtabs global %}
{% subtab Swift %}
**Solicitar Content Cards**<br>
Mientras el observador permanezca en memoria, se puede esperar la devolución de llamada de notificación del SDK de Braze.

```swift
func loadContentCards() {
  BrazeManager.shared.addObserverForContentCards(observer: self, selector: #selector(contentCardsUpdated))
  BrazeManager.shared.requestContentCardsRefresh()
}
```

**Gestión de la devolución de llamada del SDK de Content Cards**<br>
Reenvía la devolución de llamada de notificación al archivo auxiliar para analizar los datos de la carga útil de tus objetos personalizados.
```swift
@objc func contentCardsUpdated(_ notification: Notification) {
  guard let contentCards = BrazeManager.shared.handleContentCardsUpdated(notification, for: [.yourValue]) as? [CustomObject],!contentCards.isEmpty else { return }

 // do something with your array of custom objects
}
```

**Trabajar con Content Cards**<br>
El `class_type` se pasa como filtro para devolver solo las Content Cards que tengan un `class_type` coincidente.

```swift
func handleContentCardsUpdated(_ notification: Notification, for classTypes: [ContentCardClassType]) -> [ContentCardable] {
  guard let updateIsSuccessful = notification.userInfo?[ABKContentCardsProcessedIsSuccessfulKey] as? Bool, updateIsSuccessful, let cards = contentCards else { return [] }

  return convertContentCards(cards, for: classTypes)
}
```
{% endsubtab %}
{% subtab Objective-C %}
**Solicitar Content Cards**<br>
Mientras el observador permanezca en memoria, se puede esperar la devolución de llamada de notificación del SDK de Braze.

```objc
- (void)loadContentCards {
  [[BrazeManager shared] addObserverForContentCards:self selector:@selector(contentCardsUpdated:)];
  [[BrazeManager shared] requestContentCardsRefresh];
}
```

**Gestión de la devolución de llamada del SDK de Content Cards**<br>
Reenvía la devolución de llamada de notificación al archivo auxiliar para analizar los datos de la carga útil de tus objetos personalizados.
```objc
- (void)contentCardsUpdated:(NSNotification *)notification {
  NSArray *classTypes = @[@(ContentCardClassTypeYourValue)];
  NSArray *contentCards = [[BrazeManager shared] handleContentCardsUpdated:notification forClassTypes:classTypes];

  // do something with your array of custom objects
}
```

**Trabajar con Content Cards**<br>
El `class_type` se pasa como filtro para devolver solo las Content Cards que tengan un `class_type` coincidente.

```objc
- (NSArray *)handleContentCardsUpdated:(NSNotification *)notification forClassType:(ContentCardClassType)classType {
  BOOL updateIsSuccessful = [notification.userInfo[ABKContentCardsProcessedIsSuccessfulKey] boolValue];
  if (updateIsSuccessful) {
    return [self convertContentCards:self.contentCards forClassType:classType];
  } else {
    return @[];
  }
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Working with Payload Data %}
{% subtabs global %}
{% subtab Swift %}
**Trabajar con datos de carga útil**<br>
Recorre el array de Content Cards y solo analiza las tarjetas con un `class_type` coincidente. La carga útil de un ABKContentCard se analiza en un `Dictionary`.

```swift
func convertContentCards(_ cards: [ABKContentCard], for classTypes: [ContentCardClassType]) -> [ContentCardable] {
  var contentCardables: [ContentCardable] = []

  for card in cards {
    let classTypeString = card.extras?[ContentCardKey.classType.rawValue] as? String
    let classType = ContentCardClassType(rawType: classTypeString)
    guard classTypes.contains(classType) else { continue }

    var metaData: [ContentCardKey: Any] = [:]
    switch card {
    case let banner as ABKBannerContentCard:
      metaData[.image] = banner.image
    case let captioned as ABKCaptionedImageContentCard:
      metaData[.title] = captioned.title
      metaData[.cardDescription] = captioned.cardDescription
      metaData[.image] = captioned.image
    case let classic as ABKClassicContentCard:
      metaData[.title] = classic.title
      metaData[.cardDescription] = classic.cardDescription
    default:
      break
    }

    metaData[.idString] = card.idString
    metaData[.created] = card.created
    metaData[.dismissible] = card.dismissible
    metaData[.urlString] = card.urlString
    metaData[.extras] = card.extras
    ...
    // other Content Card properties such as expiresAt, pinned, etc.

    if let contentCardable = contentCardable(with: metaData, for: classType) {
      contentCardables.append(contentCardable)
    }
  }
  return contentCardables
}
```

**Inicializar tus objetos personalizados a partir de datos de carga útil de Content Card**<br>
El `class_type` se utiliza para determinar cuál de tus objetos personalizados se inicializará a partir de los datos de la carga útil.

```swift
func contentCardable(with metaData: [ContentCardKey: Any], for classType: ContentCardClassType) -> ContentCardable? {
  switch classType {
  case .yourValue:
    return CustomObject(metaData: metaData, classType: classType)
  case .yourOtherValue:
    return OtherCustomObject(metaData: metaData, classType: classType)
  ...
  default:
    return nil
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
**Trabajar con datos de carga útil**<br>
Recorre el array de Content Cards y solo analiza las tarjetas con un `class_type` coincidente. La carga útil de un ABKContentCard se analiza en un `Dictionary`.

```objc
- (NSArray *)convertContentCards:(NSArray<ABKContentCard*> *)cards forClassType:(ContentCardClassType)classType {
  NSMutableArray *contentCardables = [[NSMutableArray alloc] init];      for (ABKContentCard *card in cards) {
    NSString *classTypeString = [card.extras objectForKey:ContentCardKeyClassType];
    ContentCardClassType cardClassType = [ContentCardData contentCardClassTypeForString: classTypeString];
    if (cardClassType != classType) { continue; }

    NSMutableDictionary *metaData = [[NSMutableDictionary alloc] init];
    if ([card isKindOfClass:[ABKBannerContentCard class]]) {
      ABKBannerContentCard *banner = (ABKBannerContentCard *)card;
      metaData[ContentCardKeyImage] = banner.image;
    } else if ([card isKindOfClass:[ABKCaptionedImageContentCard class]]) {
      ABKCaptionedImageContentCard *captioned = (ABKCaptionedImageContentCard *)card;
      metaData[ContentCardKeyTitle] = captioned.title;
      metaData[ContentCardKeyCardDescription] = captioned.cardDescription;
      metaData[ContentCardKeyImage] = captioned.image;
    } else if ([card isKindOfClass:[ABKClassicContentCard class]]) {
      ABKClassicContentCard *classic = (ABKClassicContentCard *)card;
      metaData[ContentCardKeyCardDescription] = classic.title;
      metaData[ContentCardKeyImage] = classic.image;
    }

    metaData[ContentCardKeyIdString] = card.idString;
    metaData[ContentCardKeyCreated] = [NSNumber numberWithDouble:card.created];
    metaData[ContentCardKeyDismissible] = [NSNumber numberWithBool:card.dismissible];
    metaData[ContentCardKeyUrlString] = card.urlString;
    metaData[ContentCardKeyExtras] = card.extras;
    ...
    // other Content Card properties such as expiresAt, pinned, etc.

    id<ContentCardable> contentCardable = [self contentCardableWithMetaData:metaData forClassType:classType];
    if (contentCardable) {
      [contentCardables addObject:contentCardable];
    }
  }

  return contentCardables;
}
```

**Inicializar tus objetos personalizados a partir de datos de carga útil de Content Card**<br>
El `class_type` se utiliza para determinar cuál de tus objetos personalizados se inicializará a partir de los datos de la carga útil.

```obj-c
- (id<ContentCardable>)contentCardableWithMetaData:(NSDictionary *)metaData forClassType:(ContentCardClassType)classType {
  switch (classType) {
    case ContentCardClassTypeYourValue:
      return [[CustomObject alloc] initWithMetaData:metaData classType:classType];
    case ContentCardClassTypeYourOtherValue:
      return nil;
    ...
    default:
      return nil;
  }
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Ejemplos {#use-cases}

Hemos proporcionado tres ejemplos en la siguiente sección. Cada ejemplo ofrece una explicación detallada, fragmentos de código relevantes y una visión de cómo pueden verse y utilizarse las variables de Content Cards en el panel de Braze:
- [Content Cards como contenido suplementario](#content-cards-as-supplemental-content)
- [Content Cards en un centro de mensajes](#content-cards-in-a-message-center)
- [Content Cards interactivas](#interactive-content-cards)

### Content Cards como contenido suplementario {#content-cards-as-supplemental-content}

![Fuente con una lista híbrida que mezcla datos locales y Content Cards de Braze.]({% image_buster /assets/img/cc_implementation/supplementary.png %}){: style="float:right;max-width:25%;margin-left:15px;border:0;"}

Puedes combinar fácilmente Content Cards en una fuente existente, permitiendo que los datos de múltiples fuentes se carguen simultáneamente. Esto crea una experiencia cohesiva y armoniosa con Content Cards de Braze y el contenido existente de la fuente.

El ejemplo adjunto muestra un `UICollectionView` con una lista híbrida de elementos que se rellenan a través de datos locales y Content Cards proporcionadas por Braze. Con esto, las Content Cards pueden ser indistinguibles del contenido existente.

#### Configuración del panel {#dashboard-configuration}

Esta Content Card se entrega mediante una Campaign activada por API con pares clave-valor activados por API. Esto es ideal para Campaigns en las que los valores de la tarjeta dependen de factores externos para determinar qué contenido mostrar al usuario. Ten en cuenta que `class_type` debe conocerse en el momento de la configuración.

![Los pares clave-valor del ejemplo de Content Cards como contenido suplementario. En este ejemplo, diferentes aspectos de la tarjeta como "tile_id", "tile_deeplink" y "tile_title" se configuran usando Liquid.]({% image_buster /assets/img/cc_implementation/supplementary_content.png %}){: style="max-width:60%;"}

##### ¿Listo para registrar análisis? {#ready-to-log-analytics}
Visita la [siguiente sección](#logging-impressions-clicks-and-dismissals) para comprender mejor cómo debería verse el flujo de datos.

### Content Cards en un centro de mensajes {#content-cards-in-a-message-center}
<br>
Las Content Cards se pueden utilizar en formato de centro de mensajes, donde cada mensaje es su propia tarjeta. Cada mensaje del centro de mensajes se rellena a través de la carga útil de una Content Card, y cada tarjeta contiene pares clave-valor adicionales que controlan la UI/UX al hacer clic. En el siguiente ejemplo, un mensaje te dirige a una vista personalizada arbitraria, mientras que otro abre una vista web que muestra HTML personalizado.

![Centro de mensajes con Content Cards con tarjetas de mensajes individuales.]({% image_buster /assets/img/cc_implementation/message_center.png %}){: style="border:0;"}{: style="max-width:80%;border:0"}

#### Configuración del panel

Para los siguientes tipos de mensajes, el par clave-valor `class_type` debe añadirse a la configuración de tu panel. Los valores asignados aquí son arbitrarios, pero deben ser distinguibles entre los tipos de clase. Estos pares clave-valor son los identificadores clave que la aplicación utiliza para decidir a dónde ir cuando el usuario hace clic en un mensaje resumido del buzón de entrada.

{% tabs local %}
{% tab Vista personalizada arbitraria - página completa %}

Los pares clave-valor para este ejemplo incluyen:

- `message_header` establecido como `Full Page`
- `class_type` establecido como `message_full_page`

![Ejemplo de mensaje de Content Card a página completa.]({% image_buster /assets/img/cc_implementation/full_page.png %}){: style="max-width:60%;"}

{% endtab %}
{% tab Mensaje de vista web - HTML %}

Los pares clave-valor para este ejemplo incluyen:

- `message_header` establecido como `HTML`
- `class_type` establecido como `message_webview`
- `message_title`

Este mensaje también busca un par clave-valor HTML, pero si trabajas con un dominio web, un par clave-valor de URL también es válido.

![Content Card que abre una vista web HTML desde un par clave-valor.]({% image_buster /assets/img/cc_implementation/html_webview.png %}){: style="max-width:60%;"}

{% endtab %}
{% endtabs %}

#### Explicación adicional {#further-explanation}

La lógica del centro de mensajes se basa en el `contentCardClassType` que proporcionan los pares clave-valor de Braze. Usando el método `addContentCardToView`, puedes filtrar e identificar estos tipos de clase.

{% tabs %}
{% tab Swift %}
**Uso de `class_type` para el comportamiento al hacer clic**<br>
Cuando se hace clic en un mensaje, el `ContentCardClassType` determina cómo debe rellenarse la siguiente pantalla.
```swift
func addContentCardToView(with message: Message) {
    switch message.contentCardData?.contentCardClassType {
      case .message(.fullPage):
        loadContentCardFullPageView(with: message as! FullPageMessage)
      case .message(.webView):
        loadContentCardWebView(with: message as! WebViewMessage)
      default:
        break
    }
}
```
{% endtab %}
{% tab Objective-C %}
**Uso de `class_type` para el comportamiento al hacer clic**<br>
Cuando se hace clic en un mensaje, el `ContentCardClassType` determina cómo debe rellenarse la siguiente pantalla.
```objc
- (void)addContentCardToView:(Message *)message {
  switch (message.contentCardData.classType) {
    case ContentCardClassTypeMessageFullPage:
      [self loadContentCardFullPageView:(FullPageMessage *)message];
      break;
    case ContentCardClassTypeMessageWebview:
      [self loadContentCardWebView:(WebViewMessage *)message];
      break;
    default:
      break;
  }
}
```
{% endtab %}
{% endtabs %}

##### ¿Listo para registrar análisis?
Visita la [siguiente sección](#logging-impressions-clicks-and-dismissals) para comprender mejor cómo debería verse el flujo de datos.

![Una Content Card interactiva que muestra una promoción del 50 por ciento aparece en la esquina inferior izquierda de la pantalla. Tras hacer clic, se aplica una promoción al carrito.]({% image_buster /assets/img/cc_implementation/discount2.png %}){: style="border:0;"}{: style="float:right;max-width:45%;border:0;margin-left:15px;"}

### Content Cards interactivas {#interactive-content-cards}
<br>
Las Content Cards se pueden utilizar para crear experiencias dinámicas e interactivas para tus usuarios. En el ejemplo adjunto, aparece una ventana emergente de Content Card en el proceso de pago para ofrecer a los usuarios promociones de último momento.

Las tarjetas bien ubicadas como esta son una excelente forma de dar a los usuarios un "empujón" hacia acciones de usuario específicas.
<br><br><br>
#### Configuración del panel

La configuración del panel para las Content Cards interactivas es sencilla. Los pares clave-valor para este ejemplo incluyen un `discount_percentage` establecido como el monto de descuento deseado y `class_type` establecido como `coupon_code`. Estos pares clave-valor determinan cómo las Content Cards de tipo específico se filtran y muestran en la pantalla de pago.

![Content Card interactiva que muestra una promoción en el proceso de pago.]({% image_buster /assets/img/cc_implementation/discount.png %}){: style="max-width:70%;"}

##### ¿Listo para registrar análisis?
Visita la [siguiente sección](#logging-impressions-clicks-and-dismissals) para comprender mejor cómo debería verse el flujo de datos.

## Personalización del modo oscuro {#dark-mode-customization}

De forma predeterminada, las vistas de Content Cards responderán automáticamente a los cambios de modo oscuro en el dispositivo con un conjunto de colores temáticos.

Este comportamiento puede anularse como se detalla en nuestra [guía de estilo personalizado]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/content_cards/customization/custom_styling#disabling-dark-mode).

## Registro de impresiones, clics y descartados {#logging-impressions-clicks-and-dismissals}

Después de ampliar tus objetos personalizados para que funcionen como Content Cards, registrar métricas valiosas como impresiones, clics y descartados es rápido. Esto se puede hacer usando un protocolo `ContentCardable` que hace referencia y proporciona datos a un archivo auxiliar para que sean registrados por el SDK de Braze.

### Componentes de implementación<br><br> {#implementation-components}

{% tabs %}
{% tab Swift %}
**Registro de análisis**<br>
Los métodos de registro se pueden llamar directamente desde objetos que se ajustan al protocolo `ContentCardable`.
```swift
customObject.logContentCardImpression()
customObject.logContentCardClicked()
customObject.logContentCardDismissed()
```

**Recuperación de la `ABKContentCard`**<br>
El `idString` pasado desde tu objeto personalizado se utiliza para identificar la Content Card asociada y registrar análisis.

```swift
extension BrazeManager {
  func logContentCardImpression(idString: String?) {
    guard let contentCard = getContentCard(forString: idString) else { return }

    contentCard.logContentCardImpression()
  }

  private func getContentCard(forString idString: String?) -> ABKContentCard? {
    return contentCards?.first(where: { $0.idString == idString })
  }
}
```
{% endtab %}
{% tab Objective-C %}
**Registro de análisis**<br>
Los métodos de registro se pueden llamar directamente desde objetos que se ajustan al protocolo `ContentCardable`.
```objc
[customObject logContentCardImpression];
[customObject logContentCardClicked];
[customObject logContentCardDismissed];
```

**Recuperación de la `ABKContentCard`**<br>
El `idString` pasado desde tu objeto personalizado se utiliza para identificar la Content Card asociada y registrar análisis.

```objc
- (void)logContentCardImpression:(NSString *)idString {
  ABKContentCard *contentCard = [self getContentCard:idString];
  [contentCard logContentCardImpression];
}

- (ABKContentCard *)getContentCard:(NSString *)idString {
  NSPredicate *predicate = [NSPredicate predicateWithFormat:@"self.idString == %@", idString];
  NSArray *filteredArray = [self.contentCards filteredArrayUsingPredicate:predicate];

  return filteredArray.firstObject;
}
```
{% endtab %}
{% endtabs %}

{% alert important %}
Para una Content Card de variante de control, aún se debe instanciar un objeto personalizado, y la lógica de la interfaz de usuario debe configurar la vista correspondiente del objeto como oculta. El objeto puede entonces registrar una impresión para informar a nuestros análisis sobre cuándo un usuario habría visto la tarjeta de control.
{% endalert %}

## Archivos auxiliares {#helper-files}

{% details Archivo auxiliar ContentCardKey %}
{% tabs %}
{% tab Swift %}
```swift
enum ContentCardKey: String {
  case idString
  case created
  case classType = "class_type"
  case dismissible
  case extras
  ...
}
```
{% endtab %}
{% tab Objective-C %}
```objc
static NSString *const ContentCardKeyIdString = @"idString";
static NSString *const ContentCardKeyCreated = @"created";
static NSString *const ContentCardKeyClassType = @"class_type";
static NSString *const ContentCardKeyDismissible = @"dismissible";
static NSString *const ContentCardKeyExtras = @"extras";
...
```
{% endtab %}
{% endtabs %}
{% enddetails %}