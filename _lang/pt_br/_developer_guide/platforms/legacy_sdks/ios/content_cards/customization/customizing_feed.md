---
nav_title: Personalizar feed
article_title: Personalizando o feed de Content Cards para iOS
platform: iOS
page_order: 2
description: "Este artigo aborda as opções de personalização do feed de Content Cards no seu aplicativo iOS."
channel:
  - content cards
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Personalizar o feed de Content Cards {#customize-the-content-cards-feed}

Você pode criar sua própria interface de Content Cards estendendo `ABKContentCardsTableViewController` para personalizar todos os elementos de UI e o comportamento dos Content Cards. As células dos cartões de conteúdo também podem ser subclassificadas e usadas programaticamente ou por meio de um storyboard personalizado que registra as novas classes. Confira o [app de exemplo](https://github.com/Appboy/appboy-ios-sdk/tree/master/Samples/ContentCards/BrazeContentCardsSampleApp) de Content Cards para um exemplo completo.

Também é importante considerar se você deve usar uma estratégia de subclasse em vez de um view controller completamente personalizado e [se inscrever para atualizações de dados]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/content_cards/integration). Por exemplo, se você subclassificar o `ABKContentCardsTableViewController`, pode usar o [método `populateContentCards`](#overriding-populated-content-cards) para filtrar e ordenar cartões (recomendado). No entanto, se você usar uma personalização completa do view controller, terá mais controle sobre o comportamento do cartão — como exibir em um carrossel ou adicionar elementos interativos — mas precisará contar com um observador para implementar a lógica de ordenação e filtragem. Você também deve implementar os respectivos métodos de análise de dados para registrar corretamente impressões, eventos de descarte e cliques.

## Personalizando a UI {#customizing-ui}

Os trechos de código a seguir mostram como estilizar e alterar os Content Cards para atender às suas necessidades de UI usando métodos fornecidos pelo SDK. Esses métodos permitem personalizar todos os aspectos da UI dos Content Cards, incluindo fontes personalizadas, componentes de cores personalizados, texto personalizado e mais.

Existem duas maneiras distintas de personalizar a UI dos Content Cards:
- Método dinâmico: atualizar a UI do cartão individualmente, cartão por cartão
- Método estático: atualizar a UI em todos os cartões

### UI dinâmica {#dynamic-ui}

O método `applyCard` do Content Card pode referenciar o objeto do cartão e passar pares chave-valor que serão usados para atualizar a UI:

{% tabs %}
{% tab Objective-C %}
```objc
- (void)applyCard:(ABKCaptionedImageContentCard *)captionedImageCard {
  [super applyCard:captionedImageCard];

  if ([card.extras objectForKey:ContentCardKeyBackgroundColorValue]) {
    NSString *backgroundColor = [card.extras objectForKey:ContentCardKeyBackgroundColor];
    if ([backgroundColor colorValue]) {
      self.rootView.backgroundColor = [backgroundColor colorValue];
    } else {
      self.rootView.backgroundColor = [UIColor lightGray];
    }
  } else {
    self.rootView.backgroundColor = [UIColor lightGray];
  }
}
```
{% endtab %}
{% tab Swift %}
```swift
override func apply(_ captionedImageCard: ABKCaptionedImageContentCard!) {
  super.apply(captionedImageCard)

  if let backgroundColor = card.extras?[ContentCardKey.backgroundColor.rawValue] as? String,
     let backgroundColorValue = backgroundColor.colorValue() {
    rootView.backgroundColor = backgroundColorValue
  } else {
    rootView.backgroundColor = .lightGray
  }
}
```
{% endtab %}
{% endtabs %}

### UI estática {#static-ui}

O método `setUpUI` pode atribuir valores aos componentes estáticos dos Content Cards em todos os cartões:

{% tabs %}
{% tab Objective-C %}
```objc
#import "CustomClassicContentCardCell.h"

@implementation CustomClassicContentCardCell

- (void)setUpUI {
  [super setUpUI];
  self.rootView.backgroundColor = [UIColor lightGrayColor];
  self.rootView.layer.borderColor = [UIColor purpleColor].CGColor;
  self.unviewedLineView.backgroundColor = [UIColor redColor];
  self.titleLabel.font = [UIFont italicSystemFontOfSize:20];
}
```
{% endtab %}
{% tab Swift %}
```swift
override func setUpUI() {
  super.setUpUI()

  rootView.backgroundColor = .lightGray
  rootView.layer.borderColor = UIColor.purple.cgColor
  unviewedLineViewColor = .red
  titleLabel.font = .italicSystemFont(ofSize: 20)
}
```
{% endtab %}
{% endtabs %}

## Fornecendo interfaces personalizadas {#providing-custom-interfaces}

Interfaces personalizadas podem ser fornecidas registrando classes personalizadas para cada tipo de cartão desejado.

![Um Content Card de banner. Um Content Card de banner mostra uma imagem à direita do banner com o texto "Thanks for downloading Braze Demo!".]({% image_buster /assets/img/interface1.png %}){: style="max-width:35%;margin-left:15px;"}
![Um Content Card de imagem legendada. Um Content Card legendado mostra uma imagem da Braze com a legenda sobreposta na parte inferior "Thanks for downloading Braze Demo!".]({% image_buster /assets/img/interface2.png %}){: style="max-width:25%;margin-left:15px;"}
![Um Content Card clássico. Um Content Card clássico mostra uma imagem no centro do cartão com as palavras "Thanks for downloading Braze Demo" abaixo.]({% image_buster /assets/img/interface3.png %}){: style="max-width:18%;margin-left:15px;"}

A Braze fornece três modelos de Content Cards (banner, imagem legendada e clássico). Como alternativa, se você quiser fornecer suas próprias interfaces personalizadas, consulte os seguintes trechos de código:

{% tabs %}
{% tab Objective-C %}
```objc
- (void)registerTableViewCellClasses {
  [super registerTableViewCellClasses];

  // Replace the default class registrations with custom classes for these two types of cards
  [self.tableView registerClass:[CustomCaptionedImageContentCardCell class] forCellReuseIdentifier:@"ABKCaptionedImageContentCardCell"];
  [self.tableView registerClass:[CustomClassicContentCardCell class] forCellReuseIdentifier:@"ABKClassicCardCell"];
}
```
{% endtab %}
{% tab Swift %}
```swift
override func registerTableViewCellClasses() {
  super.registerTableViewCellClasses()

  // Replace the default class registrations with custom classes
  tableView.register(CustomCaptionedImageContentCardCell.self, forCellReuseIdentifier: "ABKCaptionedImageContentCardCell")
  tableView.register(CustomBannerContentCardCell.self, forCellReuseIdentifier: "ABKBannerContentCardCell")
  tableView.register(CustomClassicImageContentCardCell.self, forCellReuseIdentifier: "ABKClassicImageCardCell")
  tableView.register(CustomClassicContentCardCell.self, forCellReuseIdentifier: "ABKClassicCardCell")
}
```
{% endtab %}
{% endtabs %}

## Substituindo Content Cards populados {#overriding-populated-content-cards}

Os Content Cards podem ser alterados programaticamente usando o método `populateContentCards`:

{% tabs %}
{% tab Objective-C %}
```objc
- (void)populateContentCards {
  NSMutableArray<ABKContentCard *> *cards = [NSMutableArray arrayWithArray:[Appboy.sharedInstance.contentCardsController getContentCards]];
  for (ABKContentCard *card in cards) {
    // Replaces the card description for all Classic Content Cards
    if ([card isKindOfClass:[ABKClassicContentCard class]]) {
      ((ABKClassicContentCard *)card).cardDescription = @"Custom Feed Override title [classic cards only]!";
    }
  }
  super.cards = cards;
}
```
{% endtab %}
{% tab Swift %}
```swift
override func populateContentCards() {
  guard let cards = Appboy.sharedInstance()?.contentCardsController.contentCards else { return }
  for card in cards {
    // Replaces the card description for all Classic Content Cards
    if let classicCard = card as? ABKClassicContentCard {
      classicCard.cardDescription = "Custom Feed Override title [classic cards only]!"
    }
  }
  super.cards = (cards as NSArray).mutableCopy() as? NSMutableArray
}
```
{% endtab %}
{% endtabs %}