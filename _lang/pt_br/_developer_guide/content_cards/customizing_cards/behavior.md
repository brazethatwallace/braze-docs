---
nav_title: Comportamento
article_title: Personalize o comportamento dos Content Cards
page_order: 2
description: "Este guia de implementação aborda a alteração do comportamento dos Content Cards, a adição de extras como pares de chave-valor à sua carga útil e receitas de personalizações comuns."
channel:
  - content cards
platform:
  - Android
  - FireOS
  - Swift
  - Web
---

# Personalize o comportamento dos Content Cards {#customize-the-behavior-of-content-cards}

> Este guia de implementação aborda a alteração do comportamento dos Content Cards, a adição de extras como pares de chave-valor à sua carga útil e receitas de personalizações comuns. Para a lista completa de tipos de cartões de conteúdo, consulte [Sobre os Content Cards]({{site.baseurl}}/developer_guide/content_cards).

## Pares chave-valor {#key-value-pairs}

A Braze permite enviar cargas úteis de dados extras por meio de Content Cards para os dispositivos dos usuários usando pares chave-valor. Esses pares podem ajudar você a rastrear métricas internas, atualizar o conteúdo do app e personalizar propriedades. [Adicione pares chave-valor usando o dashboard]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card#step-4-configure-additional-settings-optional).

{% alert note %}
Não recomendamos enviar valores JSON aninhados como pares chave-valor. Em vez disso, nivele o JSON antes de enviá-lo.
{% endalert %}

{% tabs %}
{% tab web %}

Os pares chave-valor são armazenados em objetos <a href="https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html" target="_blank">`card`</a> como `extras`. Eles podem ser usados para enviar dados junto com um cartão para processamento adicional pelo aplicativo. Chame `card.extras` para acessar esses valores.

{% endtab %}
{% tab android %}

Os pares chave-valor são armazenados em objetos <a href="https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/#-2118252107%2FProperties%2F-1725759721" target="_blank">`card`</a> como `extras`. Eles podem ser usados para enviar dados junto com um cartão para processamento adicional pelo aplicativo. Chame <a href="https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/extras.html" target="_blank">`card.extras`</a> para acessar esses valores.

{% endtab %}
{% tab swift %}

Os pares chave-valor são armazenados em objetos <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard" target="_blank">`card`</a> como `extras`. Eles podem ser usados para enviar dados junto com um cartão para processamento adicional pelo aplicativo. Chame <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/data-swift.struct/extras" target="_blank">`card.extras`</a> para acessar esses valores.

{% endtab %}
{% endtabs %}

{% alert tip %}
É importante que suas equipes de marketing e de desenvolvedores coordenem quais pares chave-valor serão usados (por exemplo, `feed_type = brand_homepage`), já que qualquer par chave-valor que os profissionais de marketing inserirem no dashboard da Braze deve corresponder exatamente aos pares chave-valor que os desenvolvedores incorporam na lógica do app.
{% endalert %}

## Content Cards como conteúdo complementar {#content-cards-as-supplemental-content}

![Feed com uma lista híbrida combinando dados locais e Content Cards da Braze.]({% image_buster /assets/img/cc_implementation/supplementary.png %}){: style="float:right;max-width:25%;margin-left:15px;border:0;"}

Você pode combinar Content Cards de forma integrada em um feed existente, permitindo que os dados de vários feeds sejam carregados simultaneamente. Isso cria uma experiência coesa e harmoniosa com Content Cards da Braze e o conteúdo existente do feed.

O exemplo ao lado mostra um feed com uma lista híbrida de itens preenchidos com dados locais e Content Cards da Braze. Dessa forma, os Content Cards podem se tornar indistinguíveis do conteúdo existente.

### Pares chave-valor disparados por API or interface de programação do aplicativo (API) {#api-triggered-key-value-pairs}

[Campaigns disparadas por API or interface de programação do aplicativo (API)]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery) são uma boa estratégia quando os valores de um cartão dependem de fatores externos para determinar qual conteúdo exibir ao usuário. Por exemplo, para exibir conteúdo complementar, defina pares chave-valor usando Liquid. Observe que `class_type` deve ser conhecido no momento da configuração.

![Os pares chave-valor para o caso de uso de Content Cards complementares. Neste exemplo, diferentes aspectos do cartão, como "tile_id", "tile_deeplink" e "tile_title", são definidos usando Liquid.]({% image_buster /assets/img/cc_implementation/supplementary_content.png %}){: style="max-width:60%;"}

## Content Cards como conteúdo interativo {#content-cards-as-interactive-content}
![Um Content Card interativo exibindo uma promoção de 50% aparece no canto inferior esquerdo da tela. Ao clicar, a promoção será aplicada ao carrinho.]({% image_buster /assets/img/cc_implementation/discount2.png %}){: style="border:0;"}{: style="float:right;max-width:45%;border:0;margin-left:15px;"}

Os Content Cards podem ser usados para criar experiências dinâmicas e interativas para seus usuários. No exemplo ao lado, um pop-up de Content Card aparece na finalização da compra para oferecer promoções de última hora aos usuários. Cartões bem posicionados como esse são uma ótima forma de dar um "empurrãozinho" para ações específicas do usuário.

Os pares chave-valor para esse caso de uso incluem `discount_percentage` definido como o valor de desconto desejado e `class_type` definido como `coupon_code`. Esses pares chave-valor permitem filtrar e exibir Content Cards de tipos específicos na tela de finalização de compra. Para saber mais sobre o uso de pares chave-valor para gerenciar múltiplos feeds, consulte [Personalização do feed padrão de Content Cards]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/feed#implementing-multiple-feeds).
<br>
<br>

![Content Card interativo exibindo uma promoção na finalização de compra.]({% image_buster /assets/img/cc_implementation/discount.png %}){: style="max-width:80%;"}

## Emblemas de Content Cards {#content-card-badges}

![Tela inicial de um iPhone mostrando um app de exemplo da Braze chamado Swifty com um emblema vermelho exibindo o número 7]({% image_buster /assets/img/cc_implementation/ios-unread-badge.png %}){: style="max-width:35%;float:right;margin-left:15px;border:none;"}

Emblemas são pequenos ícones ideais para chamar a atenção do usuário. Usar emblemas para alertar o usuário sobre novos conteúdos de Content Cards pode atraí-los de volta ao seu app e aumentar as sessões.

### Exibindo o número de Content Cards não lidos como um emblema {#displaying-the-number-of-unread-content-cards-as-a-badge}

Você pode exibir o número de Content Cards não lidos que seu usuário possui como um emblema no ícone do seu app.

{% tabs %}
{% tab web %}

Você pode solicitar o número de cartões não lidos a qualquer momento chamando:

```javascript
braze.getCachedContentCards().getUnviewedCardCount();
```

Em seguida, você pode usar essa informação para exibir um emblema indicando quantos Content Cards não lidos existem. Consulte a <a href="https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.contentcards.html" target="_blank">documentação de referência do SDK or kit de desenvolvimento de software</a> para saber mais.

{% endtab %}
{% tab android %}

Você pode solicitar o número de cartões não lidos a qualquer momento chamando:

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

Em seguida, você pode usar essa informação para exibir um emblema indicando quantos Content Cards não lidos existem. Consulte a <a href="https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/get-content-card-unviewed-count.html" target="_blank">documentação de referência do SDK or kit de desenvolvimento de software</a> para saber mais.


{% endtab %}
{% tab swift %}

O exemplo a seguir usa `braze.contentCards` para solicitar e exibir o número de Content Cards não lidos. Depois que o app é fechado e a sessão do usuário termina, este código solicita uma contagem de cartões, filtrando o número de cartões com base na propriedade `viewed`.

Apps que adotaram o [ciclo de vida `UIScene`](https://developer.apple.com/documentation/technotes/tn3187-migrating-to-the-uikit-scene-based-life-cycle) (obrigatório para apps compilados com o [Xcode 27 e versões posteriores](https://developer.apple.com/documentation/xcode-release-notes/xcode-27-release-notes)) devem implementar isso no `sceneDidEnterBackground(_:)` do `SceneDelegate.swift` em vez do `applicationDidEnterBackground(_:)` do `AppDelegate.swift`.

{% subtabs %}
{% subtab Swift %}

```swift
func sceneDidEnterBackground(_ scene: UIScene)
```

Dentro deste método, implemente o seguinte código, que atualiza ativamente a contagem do emblema enquanto o usuário visualiza cartões durante uma sessão:

```swift
let unreadCards = AppDelegate.braze?.contentCards.cards.filter { $0.viewed == false }
UIApplication.shared.applicationIconBadgeNumber = unreadCards?.count ?? 0
```

{% endsubtab %}
{% subtab Objective-C %}

```objc
(void)sceneDidEnterBackground:(UIScene *)scene
```

Dentro deste método, implemente o seguinte código, que atualiza ativamente a contagem do emblema enquanto o usuário visualiza cartões durante uma sessão:

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