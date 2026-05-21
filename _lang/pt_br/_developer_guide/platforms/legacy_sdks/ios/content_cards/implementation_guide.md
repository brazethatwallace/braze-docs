---
nav_title: Implementação avançada (opcional)
article_title: Guia de implementação de Content Cards para iOS (opcional)
platform: iOS
page_order: 7
description: "Este guia de implementação avançada aborda considerações sobre o código de Content Cards do iOS, três casos de uso criados por nossa equipe, trechos de código que os acompanham e orientações sobre o registro de impressões, cliques e descartes."
channel:
  - content cards

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

<br>
{% alert important %}
Está procurando o guia básico de integração de Content Cards para desenvolvedores? Encontre [aqui]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/content_cards/integration/).
{% endalert %}

# Guia de implementação de Content Cards {#content-card-implementation-guide}

> Este guia de implementação opcional e avançado aborda considerações sobre o código de Content Cards, três casos de uso personalizados criados por nossa equipe, trechos de código que os acompanham e orientações sobre o registro de impressões, cliques e descartes. Visite nosso repositório de demonstrações da Braze [aqui](https://github.com/braze-inc/braze-growth-shares-ios-demo-app)! Este guia de implementação está centrado em uma implementação Swift, mas são fornecidos trechos em Objective-C para os interessados.

## Considerações sobre o código {#code-considerations}

### Content Cards como objetos personalizados {#content-cards-as-custom-objects}

Assim como um foguete que adiciona um propulsor, seus próprios objetos personalizados podem ser estendidos para funcionar como Content Cards. Superfícies de API limitadas como essa oferecem flexibilidade para trabalhar com diferentes back-ends de dados de forma intercambiável. Isso pode ser feito em conformidade com o protocolo `ContentCardable` e implementando o inicializador (como visto nos trechos de código a seguir) e, por meio do uso da struct `ContentCardData`, permite acessar os dados `ABKContentCard`. A carga útil `ABKContentCard` será usada para inicializar a struct `ContentCardData` e o próprio objeto personalizado, tudo a partir de um tipo `Dictionary` por meio do inicializador fornecido com o protocolo.

O inicializador também inclui um enum `ContentCardClassType`. Esse enum é usado para decidir qual objeto será inicializado. Por meio do uso de pares chave-valor no dashboard da Braze, você pode definir uma chave `class_type` explícita que será usada para determinar qual objeto inicializar. Esses pares chave-valor para Content Cards são exibidos na variável `extras` do `ABKContentCard`. Outro componente central do inicializador é o parâmetro de dicionário `metaData`. O `metaData` inclui tudo do `ABKContentCard` analisado em uma série de chaves e valores. Depois que os cartões relevantes forem analisados e convertidos em seus objetos personalizados, o app estará pronto para começar a trabalhar com eles como se tivessem sido instanciados a partir de JSON ou de qualquer outra fonte.

Depois de entender bem essas considerações de código, confira nossos [casos de uso](#sample-use-cases) para começar a implementar seus objetos personalizados.

{% tabs local %}
{% tab ContentCardable %}
{% subtabs global %}
{% subtab Swift %}
**Protocolo ContentCardable**<br>
Um objeto `ContentCardData` que representa os dados `ABKContentCard` junto com um enum `ContentCardClassType`. Um inicializador usado para instanciar objetos personalizados com metadados do `ABKContentCard`.
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
**Struct de dados do Content Card**<br>
`ContentCardData` representa os valores analisados de um `ABKContentCard`.

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
Um objeto `ContentCardData` que representa os dados `ABKContentCard` juntamente com um enum `ContentCardClassType`, um inicializador usado para instanciar objetos personalizados com metadados do `ABKContentCard`.
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
**Struct de dados do Content Card**<br>
`ContentCardData` representa os valores analisados de um `ABKContentCard`.

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
Os metadados de um `ABKContentCard` são usados para preencher as variáveis do seu objeto. Os pares chave-valor configurados no dashboard da Braze são representados no dicionário "extras".

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

**Identificação de tipos**<br>
O enum `ContentCardClassType` representa o valor `class_type` no dashboard da Braze. Esse valor também é usado como um identificador de filtro para exibir Content Cards em diferentes lugares.

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
Os metadados de um `ABKContentCard` são usados para preencher as variáveis do seu objeto. Os pares chave-valor configurados no dashboard da Braze são representados no dicionário "extras".


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

**Identificação de tipos**<br>
O enum `ContentCardClassType` representa o valor `class_type` no dashboard da Braze. Esse valor também é usado como um identificador de filtro para exibir Content Cards em diferentes lugares.

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
**Solicitação de Content Cards**<br>
Desde que o observador ainda esteja retido na memória, o retorno de chamada de notificação do SDK da Braze pode ser esperado.

```swift
func loadContentCards() {
  BrazeManager.shared.addObserverForContentCards(observer: self, selector: #selector(contentCardsUpdated))
  BrazeManager.shared.requestContentCardsRefresh()
}
```

**Manipulação do retorno de chamada do SDK de Content Cards**<br>
Encaminhe o retorno de chamada da notificação para o arquivo auxiliar para analisar os dados de carga útil do(s) seu(s) objeto(s) personalizado(s).
```swift
@objc func contentCardsUpdated(_ notification: Notification) {
  guard let contentCards = BrazeManager.shared.handleContentCardsUpdated(notification, for: [.yourValue]) as? [CustomObject],!contentCards.isEmpty else { return }

 // do something with your array of custom objects
}
```

**Trabalhando com Content Cards**<br>
O `class_type` é passado como um filtro para retornar apenas Content Cards que tenham um `class_type` correspondente.

```swift
func handleContentCardsUpdated(_ notification: Notification, for classTypes: [ContentCardClassType]) -> [ContentCardable] {
  guard let updateIsSuccessful = notification.userInfo?[ABKContentCardsProcessedIsSuccessfulKey] as? Bool, updateIsSuccessful, let cards = contentCards else { return [] }

  return convertContentCards(cards, for: classTypes)
}
```
{% endsubtab %}
{% subtab Objective-C %}
**Solicitação de Content Cards**<br>
Desde que o observador ainda esteja retido na memória, o retorno de chamada de notificação do SDK da Braze pode ser esperado.

```objc
- (void)loadContentCards {
  [[BrazeManager shared] addObserverForContentCards:self selector:@selector(contentCardsUpdated:)];
  [[BrazeManager shared] requestContentCardsRefresh];
}
```

**Manipulação do retorno de chamada do SDK de Content Cards**<br>
Encaminhe o retorno de chamada da notificação para o arquivo auxiliar para analisar os dados de carga útil do(s) seu(s) objeto(s) personalizado(s).
```objc
- (void)contentCardsUpdated:(NSNotification *)notification {
  NSArray *classTypes = @[@(ContentCardClassTypeYourValue)];
  NSArray *contentCards = [[BrazeManager shared] handleContentCardsUpdated:notification forClassTypes:classTypes];

  // do something with your array of custom objects
}
```

**Trabalhando com Content Cards**<br>
O `class_type` é passado como um filtro para retornar apenas Content Cards que tenham um `class_type` correspondente.

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
**Trabalhando com dados de carga útil**<br>
Percorre o array de Content Cards e analisa apenas os cartões com um `class_type` correspondente. A carga útil de um ABKContentCard é analisada em um `Dictionary`.

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

**Inicializando seus objetos personalizados a partir dos dados de carga útil do Content Card**<br>
O `class_type` é usado para determinar quais dos seus objetos personalizados serão inicializados a partir dos dados de carga útil.

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
**Trabalhando com dados de carga útil**<br>
Percorre o array de Content Cards e analisa apenas os cartões com um `class_type` correspondente. A carga útil de um ABKContentCard é analisada em um `Dictionary`.

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

**Inicializando seus objetos personalizados a partir dos dados de carga útil do Content Card**<br>
O `class_type` é usado para determinar quais dos seus objetos personalizados serão inicializados a partir dos dados de carga útil.

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

## Casos de uso {#sample-use-cases}

Fornecemos três casos de uso abaixo. Cada caso de uso oferece uma explicação detalhada, trechos de código relevantes e uma visão de como as variáveis do Content Card podem parecer e ser usadas no dashboard da Braze:
- [Content Cards como conteúdo suplementar](#content-cards-as-supplemental-content)
- [Content Cards em um centro de mensagens](#content-cards-in-a-message-center)
- [Content Cards interativos](#interactive-content-cards)

### Content Cards como conteúdo suplementar {#content-cards-as-supplemental-content}

![]({% image_buster /assets/img/cc_implementation/supplementary.png %}){: style="float:right;max-width:25%;margin-left:15px;border:0;"}

Você pode combinar perfeitamente Content Cards em um feed existente, permitindo que os dados de vários feeds sejam carregados simultaneamente. Isso cria uma experiência coesa e harmoniosa com Content Cards da Braze e o conteúdo de feed existente.

O exemplo à direita mostra uma `UICollectionView` com uma lista híbrida de itens que são preenchidos por meio de dados locais e Content Cards fornecidos pela Braze. Com isso, os Content Cards podem ser indistinguíveis do conteúdo existente.

#### Configuração do dashboard {#dashboard-configuration}

Esse Content Card é entregue por uma Campaign disparada por API com pares chave-valor disparados por API. Isso é ideal para Campaigns em que os valores do cartão dependem de fatores externos para determinar o conteúdo a ser exibido ao usuário. Note que `class_type` deve ser conhecido no momento da configuração.

![Os pares chave-valor para o caso de uso de Content Cards suplementares. Neste exemplo, diferentes aspectos do cartão, como "tile_id", "tile_deeplink" e "tile_title", são definidos usando Liquid.]({% image_buster /assets/img/cc_implementation/supplementary_content.png %}){: style="max-width:60%;"}

##### Pronto para registrar a análise de dados? {#ready-to-log-analytics}
Visite a [seção a seguir](#logging-impressions-clicks-and-dismissals) para entender melhor como deve ser o fluxo de dados.

### Content Cards em um centro de mensagens {#content-cards-in-a-message-center}
<br>
Content Cards podem ser usados em um formato de centro de mensagens em que cada mensagem é seu próprio cartão. Cada mensagem no centro de mensagens é preenchida por meio de uma carga útil de Content Card, e cada cartão contém pares chave-valor adicionais que potencializam a UI/UX ao clicar. No exemplo a seguir, uma mensagem direciona você para uma visualização personalizada arbitrária, enquanto outra abre uma webview que exibe HTML personalizado.

![]({% image_buster /assets/img/cc_implementation/message_center.png %}){: style="border:0;"}{: style="max-width:80%;border:0"}

#### Configuração do dashboard {#dashboard-configuration}

Para os seguintes tipos de mensagens, o par chave-valor `class_type` deve ser adicionado à configuração do seu dashboard. Os valores atribuídos aqui são arbitrários, mas devem ser distinguíveis entre os tipos de classe. Esses pares chave-valor são os identificadores-chave que o aplicativo examina ao decidir para onde ir quando o usuário clica em uma mensagem resumida da caixa de entrada.

{% tabs local %}
{% tab Arbitrary custom view message - full page %}

Os pares chave-valor para esse caso de uso incluem:

- `message_header` definido como `Full Page`
- `class_type` definido como `message_full_page`

![]({% image_buster /assets/img/cc_implementation/full_page.png %}){: style="max-width:60%;"}

{% endtab %}
{% tab Webview message - HTML %}

Os pares chave-valor para esse caso de uso incluem:

- `message_header` definido como `HTML`
- `class_type` definido como `message_webview`
- `message_title`

Essa mensagem também procura um par chave-valor HTML, mas se você estiver trabalhando com um domínio web, um par chave-valor de URL também é válido.

![]({% image_buster /assets/img/cc_implementation/html_webview.png %}){: style="max-width:60%;"}

{% endtab %}
{% endtabs %}

#### Explicação adicional {#further-explanation}

A lógica do centro de mensagens é orientada pelo `contentCardClassType`, que é fornecido pelos pares chave-valor da Braze. Usando o método `addContentCardToView`, você pode filtrar e identificar esses tipos de classe.

{% tabs %}
{% tab Swift %}
**Usando `class_type` para comportamento ao clicar**<br>
Quando uma mensagem é clicada, o `ContentCardClassType` determina como a próxima tela deve ser preenchida.
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
**Usando `class_type` para comportamento ao clicar**<br>
Quando uma mensagem é clicada, o `ContentCardClassType` determina como a próxima tela deve ser preenchida.
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

##### Pronto para registrar a análise de dados? {#ready-to-log-analytics}
Visite a [seção a seguir](#logging-impressions-clicks-and-dismissals) para entender melhor como deve ser o fluxo de dados.

![Um Content Card interativo mostrando uma promoção de 50% aparece no canto inferior esquerdo da tela. Depois de clicado, uma promoção será aplicada ao carrinho.]({% image_buster /assets/img/cc_implementation/discount2.png %}){: style="border:0;"}{: style="float:right;max-width:45%;border:0;margin-left:15px;"}

### Content Cards interativos {#interactive-content-cards}
<br>
Content Cards podem ser aproveitados para criar experiências dinâmicas e interativas para seus usuários. No exemplo à direita, temos um pop-up de Content Card que aparece no checkout, oferecendo aos usuários promoções de última hora.

Cartões bem posicionados como esse são uma ótima maneira de dar aos usuários um "empurrãozinho" em direção a ações específicas.
<br><br><br>
#### Configuração do dashboard {#dashboard-configuration}

A configuração do dashboard para Content Cards interativos é simples. Os pares chave-valor para esse caso de uso incluem `discount_percentage` definido como o valor do desconto desejado e `class_type` definido como `coupon_code`. Esses pares chave-valor são como os Content Cards específicos por tipo são filtrados e exibidos na tela de checkout.

![]({% image_buster /assets/img/cc_implementation/discount.png %}){: style="max-width:70%;"}

##### Pronto para registrar a análise de dados? {#ready-to-log-analytics}
Visite a [seção a seguir](#logging-impressions-clicks-and-dismissals) para entender melhor como deve ser o fluxo de dados.

## Personalização do modo escuro {#dark-mode-customization}

Por padrão, as visualizações de Content Cards responderão automaticamente às alterações do modo escuro no dispositivo com um conjunto de cores temáticas.

Esse comportamento pode ser substituído conforme detalhado em nosso [guia de estilo personalizado]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/content_cards/customization/custom_styling/#disabling-dark-mode).

## Registro de impressões, cliques e descartes {#logging-impressions-clicks-and-dismissals}

Depois de estender seus objetos personalizados para funcionarem como Content Cards, o registro de métricas valiosas como impressões, cliques e descartes é rápido. Isso pode ser feito usando um protocolo `ContentCardable` que faz referência e fornece dados a um arquivo auxiliar para ser registrado pelo SDK da Braze.

#### Componentes de implementação<br><br> {#implementation-components}

{% tabs %}
{% tab Swift %}
**Registrando análise de dados**<br>
Os métodos de registro podem ser chamados diretamente de objetos em conformidade com o protocolo `ContentCardable`.
```swift
customObject.logContentCardImpression()
customObject.logContentCardClicked()
customObject.logContentCardDismissed()
```

**Recuperando o `ABKContentCard`**<br>
O `idString` passado do seu objeto personalizado é usado para identificar o Content Card associado para registrar a análise de dados.

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
**Registrando análise de dados**<br>
Os métodos de registro podem ser chamados diretamente de objetos em conformidade com o protocolo `ContentCardable`.
```objc
[customObject logContentCardImpression];
[customObject logContentCardClicked];
[customObject logContentCardDismissed];
```

**Recuperando o `ABKContentCard`**<br>
O `idString` passado do seu objeto personalizado é usado para identificar o Content Card associado para registrar a análise de dados.

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
Para uma variante de controle de Content Card, um objeto personalizado ainda deve ser instanciado, e a lógica da interface do usuário deve definir a visualização correspondente do objeto como oculta. O objeto pode então registrar uma impressão para informar nossa análise de dados sobre quando um usuário teria visto o cartão de controle.
{% endalert %}

## Arquivos auxiliares {#helper-files}

{% details Arquivo auxiliar ContentCardKey %}
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