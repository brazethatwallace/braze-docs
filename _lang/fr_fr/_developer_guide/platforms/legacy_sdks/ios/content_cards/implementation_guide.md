---
nav_title: Mise en œuvre avancée (facultative)
article_title: Guide d'implémentation des Content Cards pour iOS (facultatif)
platform: iOS
page_order: 7
description: "Ce guide d'implémentation avancée couvre les considérations du code des Content Cards pour iOS, trois cas d'utilisation créés par notre équipe, les extraits de code l'accompagnant et les directives sur l'enregistrement des impressions, des clics et des rejets."
channel:
  - content cards

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

<br>
{% alert important %}
Vous recherchez le guide d'intégration de base du développeur des Content Cards ? Retrouvez-le dans le [guide d'intégration de base du développeur des Content Cards]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/content_cards/integration).
{% endalert %}

# Guide d'implémentation des Content Cards {#content-card-implementation-guide}

> Ce guide d'implémentation avancé et optionnel couvre les considérations du code des Content Cards, trois cas d'utilisation personnalisés créés par notre équipe, les extraits de code l'accompagnant et les directives sur l'enregistrement des impressions, des clics et des rejets. Visitez notre dépôt de démonstrations Braze sur [le dépôt de démonstrations Braze sur GitHub](https://github.com/braze-inc/braze-growth-shares-ios-demo-app) ! Notez que ce guide d'implémentation est centré autour d'une implémentation Swift, mais les extraits de code Objective-C sont fournis aux personnes intéressées.

## Considérations du code {#code-considerations}

### Les Content Cards comme objets personnalisés {#content-cards-as-custom-objects}

Tout comme l'ajout d'un booster à une fusée, vos propres objets personnalisés peuvent être étendus pour fonctionner comme des Content Cards. Les surfaces d'API limitées telles que celles-ci offrent la flexibilité de travailler avec différents backends de données de manière interchangeable. Cela peut être fait en respectant le protocole `ContentCardable` et en implémentant l'initialiseur (comme indiqué dans les extraits de code suivants) et, via l'utilisation de la structure `ContentCardData`, qui vous permet d'accéder aux données `ABKContentCard`. La charge utile `ABKContentCard` sera utilisée pour initialiser la structure `ContentCardData` et l'objet personnalisé lui-même, le tout depuis un type `Dictionary` via l'initialiseur fourni avec le protocole.

L'initialiseur comprend également un enum `ContentCardClassType`. Cet enum sert à décider quel objet initialiser. Grâce à l'utilisation de paires clé-valeur dans le tableau de bord de Braze, vous pouvez définir une clé `class_type` explicite qui sera utilisée pour déterminer l'objet à initialiser. Ces paires clé-valeur pour les Content Cards apparaissent dans la variable `extras` sur le `ABKContentCard`. Un autre composant essentiel de l'initialiseur est le paramètre du dictionnaire `metaData`. Les `metaData` incluent tout, du `ABKContentCard` analysé en une série de clés et de valeurs. Une fois les cartes concernées analysées et converties en vos objets personnalisés, l'application est prête à commencer à travailler avec elles comme si elles étaient instanciées à partir de JSON ou de toute autre source.

Une fois que vous aurez acquis une solide compréhension de ces considérations du code, consultez nos [cas d'utilisation](#sample-use-cases) pour commencer à mettre en œuvre vos objets personnalisés.

{% tabs local %}
{% tab ContentCardable %}
{% subtabs global %}
{% subtab Swift %}
**Protocole ContentCardable**<br>
Un objet `ContentCardData` représentant les données `ABKContentCard` avec un enum `ContentCardClassType`. Un initialiseur utilisé pour instancier des objets personnalisés avec les métadonnées `ABKContentCard`.
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
**Structure de données Content Card**<br>
`ContentCardData` représente les valeurs analysées d'un `ABKContentCard`.

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
**Protocole ContentCardable**<br>
Un objet `ContentCardData` représentant les données `ABKContentCard` avec un enum `ContentCardClassType`, un initialiseur utilisé pour instancier des objets personnalisés avec les métadonnées `ABKContentCard`.
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
**Structure de données Content Card**<br>
`ContentCardData` représente les valeurs analysées d'un `ABKContentCard`.

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
**Initialiseur d'objet personnalisé**<br>
Les métadonnées d'un `ABKContentCard` sont utilisées pour renseigner les variables de votre objet. Les paires clé-valeur définies dans le tableau de bord de Braze sont représentées dans le dictionnaire « extras ».

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

**Identifier les types**<br>
L'enum `ContentCardClassType` représente la valeur `class_type` dans le tableau de bord de Braze. Cette valeur est également utilisée comme identifiant de filtre pour afficher les Content Cards à différents endroits.

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
**Initialiseur d'objet personnalisé**<br>
Les métadonnées d'un `ABKContentCard` sont utilisées pour renseigner les variables de votre objet. Les paires clé-valeur définies dans le tableau de bord de Braze sont représentées dans le dictionnaire « extras ».


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

**Identifier les types**<br>
L'enum `ContentCardClassType` représente la valeur `class_type` dans le tableau de bord de Braze. Cette valeur est également utilisée comme identifiant de filtre pour afficher les Content Cards à différents endroits.

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
**Demander des Content Cards**<br>
Tant que l'observateur est toujours conservé en mémoire, le rappel de notification du SDK Braze peut être attendu.

```swift
func loadContentCards() {
  BrazeManager.shared.addObserverForContentCards(observer: self, selector: #selector(contentCardsUpdated))
  BrazeManager.shared.requestContentCardsRefresh()
}
```

**Gestion du rappel SDK des Content Cards**<br>
Transmettez le rappel de notification au fichier auxiliaire pour analyser les données de la charge utile de votre ou vos objets personnalisés.
```swift
@objc func contentCardsUpdated(_ notification: Notification) {
  guard let contentCards = BrazeManager.shared.handleContentCardsUpdated(notification, for: [.yourValue]) as? [CustomObject],!contentCards.isEmpty else { return }

 // do something with your array of custom objects
}
```

**Travailler avec les Content Cards**<br>
Le `class_type` est transmis comme filtre pour ne renvoyer que les Content Cards qui ont un `class_type` correspondant.

```swift
func handleContentCardsUpdated(_ notification: Notification, for classTypes: [ContentCardClassType]) -> [ContentCardable] {
  guard let updateIsSuccessful = notification.userInfo?[ABKContentCardsProcessedIsSuccessfulKey] as? Bool, updateIsSuccessful, let cards = contentCards else { return [] }

  return convertContentCards(cards, for: classTypes)
}
```
{% endsubtab %}
{% subtab Objective-C %}
**Demander des Content Cards**<br>
Tant que l'observateur est toujours conservé en mémoire, le rappel de notification du SDK Braze peut être attendu.

```objc
- (void)loadContentCards {
  [[BrazeManager shared] addObserverForContentCards:self selector:@selector(contentCardsUpdated:)];
  [[BrazeManager shared] requestContentCardsRefresh];
}
```

**Gestion du rappel SDK des Content Cards**<br>
Transmettez le rappel de notification au fichier auxiliaire pour analyser les données de la charge utile de votre ou vos objets personnalisés.
```objc
- (void)contentCardsUpdated:(NSNotification *)notification {
  NSArray *classTypes = @[@(ContentCardClassTypeYourValue)];
  NSArray *contentCards = [[BrazeManager shared] handleContentCardsUpdated:notification forClassTypes:classTypes];

  // do something with your array of custom objects
}
```

**Travailler avec les Content Cards**<br>
Le `class_type` est transmis comme filtre pour ne renvoyer que les Content Cards qui ont un `class_type` correspondant.

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
**Travailler avec les données de la charge utile**<br>
Parcourt le tableau de Content Cards et n'analyse que les cartes avec un `class_type` correspondant. La charge utile d'une ABKContentCard est analysée dans un `Dictionary`.

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

**Initialisation de vos objets personnalisés à partir des données de la charge utile des Content Cards**<br>
Le `class_type` est utilisé pour déterminer lequel de vos objets personnalisés sera initialisé à partir des données de la charge utile.

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
**Travailler avec les données de la charge utile**<br>
Parcourt le tableau de Content Cards et n'analyse que les cartes avec un `class_type` correspondant. La charge utile d'une ABKContentCard est analysée dans un `Dictionary`.

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

**Initialisation de vos objets personnalisés à partir des données de la charge utile des Content Cards**<br>
Le `class_type` est utilisé pour déterminer lequel de vos objets personnalisés sera initialisé à partir des données de la charge utile.

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

## Cas d'utilisation {#use-cases}

Vous trouverez ci-dessous trois cas d'utilisation. Chaque cas d'utilisation offre une explication détaillée, des extraits de code pertinents et un aperçu de la façon dont les variables des Content Cards peuvent être rassemblées et utilisées dans le tableau de bord de Braze :
- [Content Cards en tant que contenu supplémentaire](#content-cards-as-supplemental-content)
- [Content Cards dans un centre de messages](#content-cards-in-a-message-center)
- [Content Cards interactives](#interactive-content-cards)

### Content Cards en tant que contenu supplémentaire {#content-cards-as-supplemental-content}

![Flux avec une liste hybride combinant des données locales et des Content Cards Braze.]({% image_buster /assets/img/cc_implementation/supplementary.png %}){: style="float:right;max-width:25%;margin-left:15px;border:0;"}

Vous pouvez intégrer de façon fluide les Content Cards dans un flux existant, ce qui permet de charger simultanément les données de plusieurs flux. Cela crée une expérience cohésive et harmonieuse avec les Content Cards de Braze et le contenu du flux existant.

L'exemple à droite montre un `UICollectionView` avec une liste hybride d'éléments renseignés par les données locales et les Content Cards alimentées par Braze. Avec cette méthode, les Content Cards ne peuvent pas être différenciées du contenu existant.

#### Configuration du tableau de bord {#dashboard-configuration}

Cette Content Card est livrée par une Campaign déclenchée par API avec des paires clé-valeur déclenchées par API. Cette option est idéale pour les Campaigns où les valeurs de la carte dépendent de facteurs externes pour déterminer le contenu à afficher à l'utilisateur. Notez que `class_type` doit être connu au moment de la configuration.

![Les paires clé-valeur pour le cas d'utilisation des Content Cards supplémentaires. Dans cet exemple, différents aspects de la carte, tels que « tile_id », « tile_deeplink » et « tile_title », sont définis à l'aide de Liquid.]({% image_buster /assets/img/cc_implementation/supplementary_content.png %}){: style="max-width:60%;"}

##### Prêt à enregistrer les analyses ? {#ready-to-log-analytics}
Consultez la [section suivante](#logging-impressions-clicks-and-dismissals) pour mieux comprendre à quoi doit ressembler le flux de données.

### Content Cards dans un centre de messages {#content-cards-in-a-message-center}
<br>
Les Content Cards peuvent être utilisées dans un format de centre de messages dans lequel chaque message est sa propre carte. Chaque message du centre de messages est rempli via une charge utile de Content Card et chaque carte contient des paires clé-valeur supplémentaires qui alimentent l'interface ou l'expérience utilisateur lors du clic. Dans l'exemple suivant, un message vous dirige vers une vue personnalisée arbitraire, tandis qu'un autre ouvre une vue web qui affiche du HTML personnalisé.

![Centre de messages Content Card avec des cartes de messages individuelles.]({% image_buster /assets/img/cc_implementation/message_center.png %}){: style="border:0;"}{: style="max-width:80%;border:0"}

#### Configuration du tableau de bord

Pour les types de messages suivants, la paire clé-valeur `class_type` doit être ajoutée à la configuration de votre tableau de bord. Les valeurs assignées ici sont arbitraires, mais doivent pouvoir être distinguées entre types de classe. Ces paires clé-valeur sont les identifiants clés que l'application examine lorsqu'elle décide où aller lorsque l'utilisateur clique sur un message abrégé de la boîte de réception.

{% tabs local %}
{% tab Message de vue personnalisée arbitraire - pleine page %}

Les paires clé-valeur pour ce cas d'utilisation comprennent :

- `message_header` défini comme `Full Page`
- `class_type` défini comme `message_full_page`

![Exemple de message Content Card en pleine page.]({% image_buster /assets/img/cc_implementation/full_page.png %}){: style="max-width:60%;"}

{% endtab %}
{% tab Message webview - HTML %}

Les paires clé-valeur pour ce cas d'utilisation comprennent :

- `message_header` défini comme `HTML`
- `class_type` défini comme `message_webview`
- `message_title`

Ce message recherche également une paire clé-valeur HTML, mais si vous travaillez avec un domaine web, une paire clé-valeur URL est également valide.

![Content Card ouvrant une vue web HTML à partir d'une paire clé-valeur.]({% image_buster /assets/img/cc_implementation/html_webview.png %}){: style="max-width:60%;"}

{% endtab %}
{% endtabs %}

#### Explication supplémentaire {#further-explanation}

La logique du centre de messages est dirigée par le `contentCardClassType` qui est fourni par les paires clé-valeur de Braze. En utilisant la méthode `addContentCardToView`, vous pouvez à la fois filtrer et identifier ces types de classe.

{% tabs %}
{% tab Swift %}
**Utilisation de `class_type` pour le comportement au clic**<br>
Lorsqu'un message est cliqué, le `ContentCardClassType` gère la façon dont l'écran suivant doit être rempli.
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
**Utilisation de `class_type` pour le comportement au clic**<br>
Lorsqu'un message est cliqué, le `ContentCardClassType` gère la façon dont l'écran suivant doit être rempli.
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

##### Prêt à enregistrer les analyses ?
Consultez la [section suivante](#logging-impressions-clicks-and-dismissals) pour mieux comprendre à quoi doit ressembler le flux de données.

![Une Content Card interactive affichant une promotion de 50 % apparaît dans le coin en bas à gauche de l'écran. Après avoir cliqué, une promotion sera appliquée au panier.]({% image_buster /assets/img/cc_implementation/discount2.png %}){: style="border:0;"}{: style="float:right;max-width:45%;border:0;margin-left:15px;"}

### Content Cards interactives {#interactive-content-cards}
<br>
Les Content Cards peuvent être utilisées pour créer des expériences dynamiques et interactives pour vos utilisateurs. Dans l'exemple à droite, une fenêtre contextuelle de Content Card apparaît au moment du paiement, fournissant aux utilisateurs des promotions de dernière minute.

Des cartes bien placées comme celles-ci constituent un excellent moyen d'encourager les utilisateurs à entreprendre des actions spécifiques.
<br><br><br>
#### Configuration du tableau de bord

La configuration du tableau de bord pour les Content Cards interactives est simple. Les paires clé-valeur pour ce cas d'utilisation comprennent un `discount_percentage` défini comme montant de remise souhaité et un `class_type` défini comme `coupon_code`. Ces paires clé-valeur déterminent la façon dont les Content Cards spécifiques à un type sont filtrées et affichées sur l'écran de paiement.

![Content Card interactive affichant une promotion au moment du paiement.]({% image_buster /assets/img/cc_implementation/discount.png %}){: style="max-width:70%;"}

##### Prêt à enregistrer les analyses ?
Consultez la [section suivante](#logging-impressions-clicks-and-dismissals) pour mieux comprendre à quoi doit ressembler le flux de données.

## Personnalisation du mode sombre {#dark-mode-customization}

Par défaut, les vues des Content Cards s'adaptent automatiquement aux changements de mode sombre de l'appareil grâce à un ensemble de couleurs thématiques.

Ce comportement peut être modifié comme indiqué dans notre [guide des styles personnalisés]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/content_cards/customization/custom_styling#disabling-dark-mode).

## Enregistrer les impressions, les clics et les rejets {#logging-impressions-clicks-and-dismissals}

Après avoir étendu vos objets personnalisés pour qu'ils fonctionnent comme des Content Cards, l'enregistrement d'indicateurs précieux tels que les impressions, les clics et les rejets est rapide. Pour ce faire, vous pouvez utiliser un protocole `ContentCardable` qui référence et fournit des données à un fichier auxiliaire qui sera enregistré par le SDK Braze.

### Composants d'implémentation {#implementation-components}<br><br> {#implementation-components}

{% tabs %}
{% tab Swift %}
**Enregistrer les analyses**<br>
Les méthodes de journalisation peuvent être appelées directement à partir d'objets conformes au protocole `ContentCardable`.
```swift
customObject.logContentCardImpression()
customObject.logContentCardClicked()
customObject.logContentCardDismissed()
```

**Récupérer la `ABKContentCard`**<br>
Le `idString` transmis à partir de votre objet personnalisé est utilisé pour identifier la Content Card associée afin d'enregistrer les analyses.

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
**Enregistrer les analyses**<br>
Les méthodes de journalisation peuvent être appelées directement à partir d'objets conformes au protocole `ContentCardable`.
```objc
[customObject logContentCardImpression];
[customObject logContentCardClicked];
[customObject logContentCardDismissed];
```

**Récupérer la `ABKContentCard`**<br>
Le `idString` transmis à partir de votre objet personnalisé est utilisé pour identifier la Content Card associée afin d'enregistrer les analyses.

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
Pour une Content Card de variante de contrôle, un objet personnalisé doit toujours être instancié et la logique de l'interface graphique doit définir la vue correspondante de l'objet comme masquée. L'objet peut ensuite enregistrer une impression pour informer notre analytique du moment où l'utilisateur aurait vu la carte de contrôle.
{% endalert %}

## Fichiers d'aide {#helper-files}

{% details Fichier d'aide ContentCardKey %}
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