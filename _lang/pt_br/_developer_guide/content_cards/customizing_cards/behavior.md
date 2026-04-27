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

> Este guia de implementação aborda a alteração do comportamento dos Content Cards, a adição de extras como pares de chave-valor à sua carga útil e receitas de personalizações comuns. Para a lista completa de tipos de cartões de conteúdo, consulte [Sobre os Content Cards]({{site.baseurl}}/developer_guide/content_cards/).

## Pares de chave-valor {#key-value-pairs}

A Braze permite que você envie cargas úteis de dados extras por meio de Content Cards para os dispositivos dos usuários usando pares de chave-valor. Eles podem ajudar a rastrear métricas internas, atualizar o conteúdo do app e personalizar propriedades. [Adicione pares de chave-valor usando o dashboard]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/#step-4-configure-additional-settings-optional).

{% alert note %}
Não recomendamos o envio de valores JSON aninhados como pares de chave-valor. Em vez disso, achate o JSON antes de enviá-lo.
{% endalert %}

{% tabs %}
{% tab web %}

Os pares de chave-valor são armazenados em objetos <a href="https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html" target="_blank">`card`</a> como `extras`. Eles podem ser usados para enviar dados junto com um cartão para tratamento posterior pelo aplicativo. Chame `card.extras` para acessar esses valores.

{% endtab %}
{% tab android %}

Os pares de chave-valor são armazenados em objetos <a href="https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/#-2118252107%2FProperties%2F-1725759721" target="_blank">`card`</a> como `extras`. Eles podem ser usados para enviar dados junto com um cartão para tratamento posterior pelo aplicativo. Chame <a href="https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/extras.html" target="_blank">`card.extras`</a> para acessar esses valores.

{% endtab %}
{% tab swift %}

Os pares de chave-valor são armazenados em objetos <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard" target="_blank">`card`</a> como `extras`. Eles podem ser usados para enviar dados junto com um cartão para tratamento posterior pelo aplicativo. Chame <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/data-swift.struct/extras" target="_blank">`card.extras`</a> para acessar esses valores.

{% endtab %}
{% endtabs %}

{% alert tip %}
É importante que suas equipes de marketing e de desenvolvimento coordenem quais pares de chave-valor serão usados (por exemplo, `feed_type = brand_homepage`), pois todos os pares de chave-valor que os profissionais de marketing inserirem no dashboard da Braze devem corresponder exatamente aos pares de chave-valor que os desenvolvedores criam na lógica do app.
{% endalert %}

## Content Cards como conteúdo suplementar {#content-cards-as-supplemental-content}

![]({% image_buster /assets/img/cc_implementation/supplementary.png %}){: style="float:right;max-width:25%;margin-left:15px;border:0;"}

Você pode combinar perfeitamente os Content Cards em um feed existente, permitindo que os dados de vários feeds sejam carregados simultaneamente. Isso cria uma experiência coesa e harmoniosa com os Content Cards da Braze e o conteúdo de feed existente.

O exemplo à direita mostra um feed com uma lista híbrida de itens que são preenchidos por meio de dados locais e Content Cards fornecidos pela Braze. Com isso, os Content Cards podem ser indistinguíveis do conteúdo existente.

### Pares de chave-valor disparados por API {#api-triggered-key-value-pairs}

As [Campaigns disparadas por API]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery/) são uma boa estratégia a ser empregada quando os valores de um cartão dependem de fatores externos para determinar o conteúdo a ser exibido para o usuário. Por exemplo, para exibir conteúdo suplementar, defina pares de chave-valor usando Liquid. Note que o `class_type` deve ser conhecido no momento da configuração.

![Os pares de chave-valor para o caso de uso de Content Cards suplementares. Neste exemplo, diferentes aspectos do cartão, como "tile_id", "tile_deeplink" e "tile_title", são definidos usando Liquid.]({% image_buster /assets/img/cc_implementation/supplementary_content.png %}){: style="max-width:60%;"}

## Content Cards como conteúdo interativo {#content-cards-as-interactive-content}
![Um Content Card interativo mostrando uma promoção de 50% aparece no canto inferior esquerdo da tela. Depois de clicado, a promoção será aplicada ao carrinho.]({% image_buster /assets/img/cc_implementation/discount2.png %}){: style="border:0;"}{: style="float:right;max-width:45%;border:0;margin-left:15px;"}

Os Content Cards podem ser aproveitados para criar experiências dinâmicas e interativas para seus usuários. No exemplo à direita, temos um pop-up de Content Card que aparece no checkout, oferecendo aos usuários promoções de última hora. Cartões bem posicionados como esse são uma ótima maneira de dar aos usuários um "empurrãozinho" em direção a ações específicas.

Os pares de chave-valor para esse caso de uso incluem `discount_percentage` definido como o valor do desconto desejado e `class_type` definido como `coupon_code`. Esses pares de chave-valor permitem filtrar e exibir Content Cards específicos por tipo na tela de checkout. Para saber mais sobre o uso de pares de chave-valor para gerenciar vários feeds, consulte [Personalização do feed padrão de Content Cards]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_feed/#multiple-feeds).
<br>
<br>

![]({% image_buster /assets/img/cc_implementation/discount.png %}){: style="max-width:80%;"}

## Emblemas de Content Cards {#content-card-badges}

![Tela inicial de um iPhone mostrando um app de exemplo da Braze chamado Swifty com um emblema vermelho exibindo o número 7]({% image_buster /assets/img/cc_implementation/ios-unread-badge.png %}){: style="max-width:35%;float:right;margin-left:15px;border:none;"}

Os emblemas são ícones pequenos, ideais para chamar a atenção do usuário. O uso de emblemas para alertar o usuário sobre novos conteúdos de Content Cards pode atrair os usuários de volta ao seu app e aumentar as sessões.

### Exibir o número de Content Cards não lidos como um emblema {#displaying-the-number-of-unread-content-cards-as-a-badge}

Você pode exibir o número de Content Cards não lidos que seu usuário tem como um emblema no ícone do seu app.

{% tabs %}
{% tab web %}

Você pode solicitar o número de cartões não lidos a qualquer momento chamando:

```javascript
braze.getCachedContentCards().getUnviewedCardCount();
```

Em seguida, você pode usar essas informações para exibir um emblema que indica quantos Content Cards não lidos existem. Para saber mais, consulte a <a href="https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.contentcards.html" target="_blank">documentação de referência do SDK</a>.

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

Em seguida, você pode usar essas informações para exibir um emblema que indica quantos Content Cards não lidos existem. Para saber mais, consulte a <a href="https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/get-content-card-unviewed-count.html" target="_blank">documentação de referência do SDK</a>.


{% endtab %}
{% tab swift %}

O exemplo a seguir usa `braze.contentCards` para solicitar e exibir o número de Content Cards não lidos. Depois que o app é fechado e a sessão do usuário termina, esse código solicita uma contagem de cartões, filtrando o número de cartões com base na propriedade `viewed`.

{% subtabs %}
{% subtab Swift %}

```swift
func applicationDidEnterBackground(_ application: UIApplication)
```

Nesse método, implemente o seguinte código, que atualiza ativamente a contagem de emblemas enquanto o usuário visualiza os cartões durante uma determinada sessão:

```swift
let unreadCards = AppDelegate.braze?.contentCards.cards.filter { $0.viewed == false }
UIApplication.shared.applicationIconBadgeNumber = unreadCards?.count ?? 0
```

{% endsubtab %}
{% subtab Objective-C %}

```objc
(void)applicationDidEnterBackground:(UIApplication *)application
```

Nesse método, implemente o seguinte código, que atualiza ativamente a contagem de emblemas enquanto o usuário visualiza os cartões durante uma determinada sessão:

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