---
nav_title: Feed padrão
article_title: Personalize o feed para Content Cards
page_order: 3
description: "Este artigo aborda as opções de personalização do feed de Content Cards."
channel:
  - content cards
platform:
  - Android
  - FireOS
  - Swift
  - Web
---

# Personalize o feed para Content Cards {#customize-the-feed-for-content-cards}

> Um feed de cartão de conteúdo é a sequência de Content Cards nos seus aplicativos móveis ou da web. Este artigo aborda a configuração de quando o feed é atualizado, a ordem dos cartões, o gerenciamento de vários feeds e as mensagens de erro de "feed vazio". Para a lista completa de tipos de cartões de conteúdo, consulte [Sobre Content Cards]({{site.baseurl}}/developer_guide/content_cards).

{% multi_lang_include developer_guide/_shared/about_session_lifecycle.md %}

## Atualização do feed {#refreshing-the-feed}

### Atualização automática {#automatic-refresh}

Por padrão, o feed de Content Cards é atualizado automaticamente quando:

- Uma nova sessão é iniciada
- O feed padrão de Content Cards é fechado e reaberto após mais de 60 segundos desde a última atualização.

{% alert tip %}
Para exibir Content Cards atualizados dinamicamente sem precisar atualizar manualmente, selecione **At first impression** durante a criação do cartão. Esses cartões serão atualizados quando estiverem disponíveis.
{% endalert %}

### Entrega em tempo real {#real-time-delivery}

A Braze também envia atualizações de Content Cards para o dispositivo assim que elas acontecem, por meio de uma conexão ativa que o SDK mantém durante a sessão. Os usuários não precisam iniciar uma nova sessão nem aguardar uma atualização para ver a mudança.

A entrega em tempo real abrange as seguintes atualizações:

- Um usuário se torna elegível para uma Campaign de Content Cards durante uma sessão.
- Um usuário avança para uma etapa de Content Cards em um Canvas.
- Um cartão é removido do feed de um usuário.
- Um cartão é enviado pela API, como com o endpoint [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages), [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns) ou [`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases).

A entrega em tempo real requer as seguintes versões mínimas do SDK:

{% sdk_min_versions swift:18.0.0 android:43.1.1 web:6.12.0 %}

Em versões anteriores do SDK, os cartões continuam chegando no início da sessão e durante a atualização.

### Atualização manual {#manual-refresh}

Para atualizar manualmente o feed em um momento específico:

{% tabs %}
{% tab web %}

Solicite uma atualização manual dos Content Cards da Braze pelo SDK Web a qualquer momento chamando [`requestContentCardsRefresh()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestcontentcardsrefresh).

Você também pode chamar [`getCachedContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#getcachedcontentcards) para obter todos os cartões disponíveis no momento a partir da última atualização de Content Cards.

```javascript
import * as braze from "@braze/web-sdk";

function refresh() {
  braze.requestContentCardsRefresh();
}
```

Para abrir links de Content Cards em uma nova aba do navegador em vez da mesma aba, defina `openCardsInNewTab: true` nas opções de inicialização do SDK Web. Para saber mais sobre as opções de inicialização, consulte o [guia do repositório do SDK Web]({{site.baseurl}}/developer_guide/sdk_repository_guides/web).

{% endtab %}
{% tab android %}

Solicite uma atualização manual dos Content Cards da Braze pelo SDK Android a qualquer momento chamando [`requestContentCardsRefresh`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/request-content-cards-refresh.html).

{% subtabs local %}
{% subtab Java %}

```java
Braze.getInstance(context).requestContentCardsRefresh();
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
Braze.getInstance(context).requestContentCardsRefresh()
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab swift %}

Solicite uma atualização manual dos Content Cards da Braze pelo SDK Swift a qualquer momento chamando o método [`requestRefresh`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/requestrefresh(_:)) na classe [`Braze.ContentCards`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class):

{% subtabs local %}
{% subtab Swift %}

Em Swift, os Content Cards podem ser atualizados com um completion handler opcional ou com um retorno assíncrono usando as APIs nativas de concorrência do Swift.

#### Completion handler {#completion-handler}

```swift
AppDelegate.braze?.contentCards.requestRefresh { result in
  // Implement completion handler
}
```

#### Async/Await

```swift
let contentCards = await AppDelegate.braze?.contentCards.requestRefresh()
```
{% endsubtab %}
{% subtab Objective-C %}

```objc
[AppDelegate.braze.contentCards requestRefreshWithCompletion:^(NSArray<BRZContentCardRaw *> * contentCards, NSError * error) {
  // Implement completion handler
}];
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Sincronização completa vs. sincronização parcial {#full-sync-vs-partial-sync}

O SDK da Braze usa dois tipos de sincronização ao buscar Content Cards no servidor:

- **Sincronização completa:** Baixa todos os Content Cards para os quais o usuário é elegível. Sincronizações completas ocorrem automaticamente a cada 7 dias ou sempre que `changeUser()` é chamado.
- **Sincronização parcial:** Baixa apenas os novos Content Cards desde a última solicitação. Se o usuário não for elegível para nenhum cartão novo, a resposta retorna zero cartões. Sincronizações parciais ocorrem sempre que `requestContentCardsRefresh()` é chamado (a menos que 7 dias tenham se passado desde a última sincronização completa, caso em que uma sincronização completa é acionada).

Sincronizações parciais reduzem a carga do servidor e o consumo de bateria do dispositivo. Os Content Cards já recebidos são armazenados localmente no SDK, de modo que os usuários continuarão vendo seus cartões disponíveis mesmo quando uma sincronização parcial retorna zero cartões novos.

### Limite de frequência {#rate-limit}

A Braze usa um algoritmo de token bucket para aplicar os seguintes limites de frequência:
- Até 5 chamadas de atualização por dispositivo, compartilhadas entre usuários e chamadas a `openSession()`
- Após atingir o limite, uma nova chamada fica disponível a cada 180 segundos (3 minutos)
- O sistema mantém até cinco chamadas para você usar a qualquer momento
- `subscribeToContentCards()` ainda retornará cartões em cache mesmo quando o limite de frequência for atingido

{% alert important %}
O SDK da Braze também aplica limites de frequência para desempenho e confiabilidade. Tenha isso em mente ao executar testes automatizados ou realizar QA manual. Consulte [Limites de frequência do SDK da Braze]({{site.baseurl}}/developer_guide/sdk_integration/rate_limits) para saber mais.
{% endalert %}

## Personalizando a ordem de exibição dos cartões {#customizing-displayed-card-order}

Você pode alterar a ordem em que seus Content Cards são exibidos. Isso permite ajustar a experiência do usuário priorizando determinados tipos de conteúdo, como promoções com prazo limitado.

{% tabs %}
{% tab web %}

Personalize a ordem de exibição dos Content Cards no seu feed usando o parâmetro [`filterFunction`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showcontentcards) de `showContentCards():`. Por exemplo:

```javascript
braze.showContentCards(null, (cards) => {
  return sortBrazeCards(cards); // Where sortBrazeCards is your sorting function that returns the sorted card array
});
```

{% endtab %}
{% tab android %}
{% subtabs %}
{% subtab android view controller %}
O [`ContentCardsFragment`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html) depende de um [`IContentCardsUpdateHandler`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.handlers/-i-content-cards-update-handler/index.html) para lidar com qualquer classificação ou modificação dos Content Cards antes de serem exibidos no feed. Um update handler personalizado pode ser definido via [`setContentCardUpdateHandler`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/set-content-card-update-handler.html) no seu `ContentCardsFragment`.

A seguir está o `IContentCardsUpdateHandler` padrão, que pode ser usado como ponto de partida para personalização:

{% details Mostrar exemplo em Java %}
```java
public class DefaultContentCardsUpdateHandler implements IContentCardsUpdateHandler {

  // Interface that must be implemented and provided as a public CREATOR
  // field that generates instances of your Parcelable class from a Parcel.
  public static final Parcelable.Creator<DefaultContentCardsUpdateHandler> CREATOR = new Parcelable.Creator<DefaultContentCardsUpdateHandler>() {
    public DefaultContentCardsUpdateHandler createFromParcel(Parcel in) {
      return new DefaultContentCardsUpdateHandler();
    }

    public DefaultContentCardsUpdateHandler[] newArray(int size) {
      return new DefaultContentCardsUpdateHandler[size];
    }
  };

  @Override
  public List<Card> handleCardUpdate(ContentCardsUpdatedEvent event) {
    List<Card> sortedCards = event.getAllCards();
    // Sort by pinned, then by the 'updated' timestamp descending
    // Pinned before non-pinned
    Collections.sort(sortedCards, new Comparator<Card>() {
      @Override
      public int compare(Card cardA, Card cardB) {
        // A displays above B
        if (cardA.getIsPinned() && !cardB.getIsPinned()) {
          return -1;
        }

        // B displays above A
        if (!cardA.getIsPinned() && cardB.getIsPinned()) {
          return 1;
        }

        // At this point, both A & B are pinned or both A & B are non-pinned
        // A displays above B since A is newer
        if (cardA.getUpdated() > cardB.getUpdated()) {
          return -1;
        }

        // B displays above A since A is newer
        if (cardA.getUpdated() < cardB.getUpdated()) {
          return 1;
        }

        // At this point, every sortable field matches so keep the natural ordering
        return 0;
      }
    });

    return sortedCards;
  }

  // Parcelable interface method
  @Override
  public int describeContents() {
    return 0;
  }

  // Parcelable interface method
  @Override
  public void writeToParcel(Parcel dest, int flags) {
    // No state is kept in this class so the parcel is left unmodified
  }
}
```
{% enddetails %}

{% details Mostrar exemplo em Kotlin %}
```kotlin
class DefaultContentCardsUpdateHandler : IContentCardsUpdateHandler {
  override fun handleCardUpdate(event: ContentCardsUpdatedEvent): List<Card> {
    val sortedCards = event.allCards
    // Sort by pinned, then by the 'updated' timestamp descending
    // Pinned before non-pinned
    sortedCards.sortWith(Comparator sort@{ cardA: Card, cardB: Card ->
      // A displays above B
      if (cardA.isPinned && !cardB.isPinned) {
        return@sort -1
      }

      // B displays above A
      if (!cardA.isPinned && cardB.isPinned) {
        return@sort 1
      }

      // At this point, both A & B are pinned or both A & B are non-pinned
      // A displays above B since A is newer
      if (cardA.updated > cardB.updated) {
        return@sort -1
      }

      // B displays above A since A is newer
      if (cardA.updated < cardB.updated) {
        return@sort 1
      }
      0
    })
    return sortedCards
  }

  // Parcelable interface method
  override fun describeContents(): Int {
    return 0
  }

  // Parcelable interface method
  override fun writeToParcel(dest: Parcel, flags: Int) {
    // No state is kept in this class so the parcel is left unmodified
  }

  companion object {
    // Interface that must be implemented and provided as a public CREATOR
    // field that generates instances of your Parcelable class from a Parcel.
    val CREATOR: Parcelable.Creator<DefaultContentCardsUpdateHandler?> = object : Parcelable.Creator<DefaultContentCardsUpdateHandler?> {
      override fun createFromParcel(`in`: Parcel): DefaultContentCardsUpdateHandler? {
        return DefaultContentCardsUpdateHandler()
      }

      override fun newArray(size: Int): Array<DefaultContentCardsUpdateHandler?> {
        return arrayOfNulls(size)
      }
    }
  }
}
```
{% enddetails %}

{% alert tip %}
O código-fonte do `ContentCardsFragment` pode ser encontrado no [GitHub](https://github.com/braze-inc/braze-android-sdk/blob/master/android-sdk-ui/src/main/java/com/braze/ui/contentcards/ContentCardsFragment.kt).
{% endalert %}
{% endsubtab %}
{% subtab Jetpack Compose %}
Para filtrar e classificar Content Cards no Jetpack Compose, defina o parâmetro `cardUpdateHandler`. Por exemplo:

```kotlin
ContentCardsList(
    cardUpdateHandler = {
        it.sortedWith { cardA, cardB ->
            // A displays above B
            if (cardA.isPinned && !cardB.isPinned) {
                return@sortedWith -1
            }
            // B displays above A
            if (!cardA.isPinned && cardB.isPinned) {
                return@sortedWith 1
            }
            // At this point, both A & B are pinned or both A & B are non-pinned
            // A displays above B since A is newer
            if (cardA.updated > cardB.updated) {
                return@sortedWith -1
            }
            // B displays above A since A is newer
            if (cardA.updated < cardB.updated) {
                return@sortedWith 1
            }
            0
        }
    }
)
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab swift %}

{% subtabs %}
{% subtab Swift %}

Personalize a ordem do feed de cartões modificando diretamente a variável estática [`Attributes.defaults`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct/defaults).

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.transform = { cards in
    cards.sorted {
        if $0.pinned && !$1.pinned {
            return true
        } else if !$0.pinned && $1.pinned {
            return false
        } else {
            return $0.createdAt > $1.createdAt
        }
    }
}
let viewController = BrazeContentCardUI.ViewController(braze: AppDelegate.braze, attributes: attributes)
```

{% endsubtab %}
{% subtab Objective-C %}

A personalização via `BrazeContentCardUI.ViewController.Attributes` não está disponível em Objective-C.

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Personalizando a mensagem de "feed vazio" {#customizing-empty-feed-message}

Quando um usuário não se qualifica para nenhum Content Cards, o SDK exibe uma mensagem de erro de "feed vazio" informando: "We have no updates. Please check again later." Você pode personalizar essa mensagem de erro de "feed vazio" de forma semelhante ao seguinte:

![Uma mensagem de erro de feed vazio que diz "This is a custom empty state message."]({% image_buster/assets/img/content_cards/content-card-customization-empty.png %})

{% tabs %}
{% tab web %}

O SDK para web não oferece suporte à substituição programática do texto de "feed vazio". Você pode optar por substituí-lo toda vez que o feed for exibido, mas isso não é recomendado porque o feed pode levar algum tempo para ser atualizado e o texto de feed vazio não será exibido imediatamente.

{% endtab %}
{% tab android %}
{% subtabs %}
{% subtab android view system %}

Se o [`ContentCardsFragment`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html) determinar que o usuário não se qualifica para nenhum Content Cards, ele exibe a mensagem de erro de feed vazio.

Um adaptador especial, o [`EmptyContentCardsAdapter`](https://github.com/braze-inc/braze-android-sdk/blob/master/android-sdk-ui/src/main/java/com/braze/ui/contentcards/adapters/EmptyContentCardsAdapter.kt), substitui o [`ContentCardAdapter`](https://github.com/braze-inc/braze-android-sdk/blob/master/android-sdk-ui/src/main/java/com/braze/ui/contentcards/adapters/ContentCardAdapter.kt) padrão para exibir essa mensagem de erro. Para definir a mensagem personalizada, sobrescreva o recurso de string `com_braze_feed_empty`.

O estilo usado para exibir essa mensagem pode ser encontrado em [`Braze.ContentCardsDisplay.Empty`](https://github.com/braze-inc/braze-android-sdk/blob/2e386dfa59a87bfc24ef7cb6ff5adf6b16f44d24/android-sdk-ui/src/main/res/values/styles.xml#L522-L530) e é reproduzido no seguinte snippet de código:

```xml
<style name="Braze.ContentCardsDisplay.Empty">
  <item name="android:lineSpacingExtra">1.5dp</item>
  <item name="android:text">@string/com_braze_feed_empty</item>
  <item name="android:textColor">@color/com_braze_content_card_empty_text_color</item>
  <item name="android:textSize">18.0sp</item>
  <item name="android:gravity">center</item>
  <item name="android:layout_height">match_parent</item>
  <item name="android:layout_width">match_parent</item>
</style>
```

Para saber mais sobre como personalizar os elementos de estilo dos Content Cards, consulte [Personalizando o estilo]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/style).
{% endsubtab %}
{% subtab Jetpack Compose %}
Para personalizar a mensagem de erro de "feed vazio" com o Jetpack Compose, você pode passar uma `emptyString` para [`ContentCardsList`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards/-content-cards-list.html). Você também pode passar [`emptyTextStyle`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards.styling/-content-card-list-styling/index.html#1193499348%2FProperties%2F-1725759721) para `ContentCardListStyling` para personalizar ainda mais essa mensagem.

```kotlin
ContentCardsList(
    emptyString = "No messages today",
    style = ContentCardListStyling(
        emptyTextStyle = TextStyle(...)
    )
)
```

Se você tiver um Composable que deseja exibir no lugar, pode passar `emptyComposable` para [`ContentCardsList`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards/-content-cards-list.html). Se `emptyComposable` for especificado, a `emptyString` não será usada.

```kotlin
ContentCardsList(
    emptyComposable = {
        Image(
            painter = painterResource(id = R.drawable.noMessages),
            contentDescription = "No messages"
        )
    }
)
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab swift %}
{% subtabs local %}
{% subtab Swift %}

Personalize o estado vazio do controlador de visualização definindo os [`Attributes`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct/defaults) relacionados.

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.emptyStateMessage = "This is a custom empty state message"
attributes.emptyStateMessageFont = .preferredFont(forTextStyle: .title1)
attributes.emptyStateMessageColor = .secondaryLabel
```

{% endsubtab %}
{% subtab Objective-C %}

Altere o texto que aparece automaticamente em feeds vazios de Content Cards redefinindo as strings localizáveis de Content Cards no arquivo [`ContentCardsLocalizable.strings`](https://github.com/braze-inc/braze-swift-sdk/tree/main/Sources/BrazeUI/Resources/Localization/en.lproj) do seu app.

{% alert note %}
Se você quiser atualizar essa mensagem em diferentes idiomas, encontre o idioma correspondente na [estrutura da pasta Resources](https://github.com/braze-inc/braze-swift-sdk/tree/main/Sources/BrazeUI/Resources/Localization) com a string `ContentCardsLocalizable.strings`.
{% endalert %}

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Implementando múltiplos feeds {#implementing-multiple-feeds}

Os Content Cards podem ser filtrados no seu app para que apenas cartões específicos sejam exibidos, permitindo que você tenha múltiplos feeds de Content Cards para diferentes casos de uso. Por exemplo, você pode manter tanto um feed transacional quanto um feed de marketing. Para isso, crie diferentes categorias de Content Cards definindo pares de chave-valor no dashboard da Braze. Em seguida, crie feeds no seu app ou site que tratem esses tipos de Content Cards de forma diferente, filtrando alguns tipos e exibindo outros.

### Etapa 1: Definir pares de chave-valor nos cartões {#step-1-set-key-value-pairs-on-cards}

Ao criar uma Campaign de Content Cards, defina [dados de pares de chave-valor]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/behavior) em cada cartão. Você usará esse par de chave-valor para categorizar os cartões. Os pares de chave-valor são armazenados na propriedade `extras` no modelo de dados do cartão.

Neste exemplo, vamos definir um par de chave-valor com a chave `feed_type` que designará em qual feed de Content Cards o cartão deve ser exibido. O valor será o que seus feeds personalizados forem, como `home_screen` ou `marketing`.

### Etapa 2: Filtrar Content Cards {#step-2-filter-content-cards}

Depois que os pares de chave-valor forem atribuídos, crie um feed com lógica que exiba os cartões que você deseja e filtre cartões de outros tipos. Neste exemplo, vamos exibir apenas cartões com um par de chave-valor correspondente de `feed_type: "Transactional"`.

{% tabs %}
{% tab web %}

O exemplo a seguir mostrará o feed de Content Cards para cartões do tipo `Transactional`:

```javascript

/**
 * @param {String} feed_type - value of the "feed_type" KVP to filter
 */
function showCardsByFeedType(feed_type) {
  braze.showContentCards(null, function(cards) {
    return cards.filter((card) => card.extras["feed_type"] === feed_type);
  });
}
```

Em seguida, você pode configurar um botão de alternância para o seu feed personalizado:

```javascript
// show the "Transactional" feed when this button is clicked
document.getElementById("show-transactional-feed").onclick = function() {
  showCardsByFeedType("Transactional");
};
```

Para saber mais, consulte a [documentação de métodos do SDK](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showcontentcards).

{% endtab %}
{% tab android %}
{% subtabs %}
{% subtab android view system %}

Por padrão, o feed de Content Cards é exibido em um [`ContentCardsFragment`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html) e o [`IContentCardsUpdateHandler`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.handlers/-i-content-cards-update-handler/index.html) retorna uma lista de cartões para exibição após receber um [`ContentCardsUpdatedEvent`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.events/-content-cards-updated-event/index.html) do SDK da Braze. No entanto, ele apenas ordena os cartões e não lida com nenhuma filtragem diretamente.

#### Etapa 2.1: Criar um handler personalizado {#step-21-create-a-custom-handler}

Você pode filtrar Content Cards implementando um [`IContentCardsUpdateHandler`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.handlers/-i-content-cards-update-handler/index.html) personalizado, usando os pares de chave-valor definidos por [`Card.getExtras()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/extras.html) no dashboard, e então modificá-lo para remover da lista quaisquer cartões que não correspondam ao valor de `feed_type` que você definiu anteriormente.

{% details Mostrar exemplo em Java %}
```java
private IContentCardsUpdateHandler getUpdateHandlerForFeedType(final String desiredFeedType) {
  return new IContentCardsUpdateHandler() {
    @Override
    public List<Card> handleCardUpdate(ContentCardsUpdatedEvent event) {
      // Use the default card update handler for a first
      // pass at sorting the cards. This is not required
      // but is done for convenience.
      final List<Card> cards = new DefaultContentCardsUpdateHandler().handleCardUpdate(event);

      final Iterator<Card> cardIterator = cards.iterator();
      while (cardIterator.hasNext()) {
        final Card card = cardIterator.next();

        // Make sure the card has our custom KVP
        // from the dashboard with the key "feed_type"
        if (card.getExtras().containsKey("feed_type")) {
          final String feedType = card.getExtras().get("feed_type");
          if (!desiredFeedType.equals(feedType)) {
            // The card has a feed type, but it doesn't match
            // our desired feed type, remove it.
            cardIterator.remove();
          }
        } else {
          // The card doesn't have a feed
          // type at all, remove it
          cardIterator.remove();
        }
      }

      // At this point, all of the cards in this list have
      // a feed type that explicitly matches the value we put
      // in the dashboard.
      return cards;
    }
  };
}
```
{% enddetails %}

{% details Mostrar exemplo em Kotlin %}
```kotlin
private fun getUpdateHandlerForFeedType(desiredFeedType: String): IContentCardsUpdateHandler {
  return IContentCardsUpdateHandler { event ->
    // Use the default card update handler for a first
    // pass at sorting the cards. This is not required
    // but is done for convenience.
    val cards = DefaultContentCardsUpdateHandler().handleCardUpdate(event)

    val cardIterator = cards.iterator()
    while (cardIterator.hasNext()) {
      val card = cardIterator.next()

      // Make sure the card has our custom KVP
      // from the dashboard with the key "feed_type"
      if (card.extras.containsKey("feed_type")) {
        val feedType = card.extras["feed_type"]
        if (desiredFeedType != feedType) {
          // The card has a feed type, but it doesn't match
          // our desired feed type, remove it.
          cardIterator.remove()
        }
      } else {
        // The card doesn't have a feed
        // type at all, remove it
        cardIterator.remove()
      }
    }

    // At this point, all of the cards in this list have
    // a feed type that explicitly matches the value we put
    // in the dashboard.
    cards
  }
}
```
{% enddetails %}

#### Etapa 2.2: Adicionar a um fragment {#step-22-add-it-to-a-fragment}

Depois de criar um [`IContentCardsUpdateHandler`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.handlers/-i-content-cards-update-handler/index.html), crie um [`ContentCardsFragment`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html) que o utilize. Esse feed personalizado pode ser usado como qualquer outro `ContentCardsFragment`. Nas diferentes partes do seu app, exiba diferentes feeds de Content Cards com base na chave fornecida no dashboard. Cada feed `ContentCardsFragment` terá um conjunto único de cartões exibidos graças ao `IContentCardsUpdateHandler` personalizado em cada fragment.

{% details Mostrar exemplo em Java %}
```java
// We want a Content Cards feed that only shows "Transactional" cards.
ContentCardsFragment customContentCardsFragment = new ContentCardsFragment();
customContentCardsFragment.setContentCardUpdateHandler(getUpdateHandlerForFeedType("Transactional"));
```
{% enddetails %}

{% details Mostrar exemplo em Kotlin %}
```kotlin
// We want a Content Cards feed that only shows "Transactional" cards.
val customContentCardsFragment = ContentCardsFragment()
customContentCardsFragment.contentCardUpdateHandler = getUpdateHandlerForFeedType("Transactional")
```
{% enddetails %}
{% endsubtab %}

{% subtab Jetpack Compose %}
Para filtrar quais Content Cards são exibidos neste feed, use `cardUpdateHandler`. Por exemplo:

```kotlin
ContentCardsList(
     cardUpdateHandler = {
         it.filter { card ->
             card.extras["feed_type"] == "Transactional"
         }
     }
 )
 ```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab swift %}

The following example will show the Content Cards feed for `Transactional` type cards:

{% subtabs %}
{% subtab Swift %}

```swift
// Filter cards by the `Transactional` feed type based on your key-value pair.
let transactionalCards = cards.filter { $0.extras["feed_type"] as? String == "Transactional" }
```

Para ir além, os cartões apresentados no view controller podem ser filtrados definindo a propriedade `transform` na sua struct `Attributes` para exibir apenas os cartões filtrados pelos seus critérios.

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.transform = { cards in
  cards.filter { $0.extras["feed_type"] as? String == "Transactional" }
}

// Pass your attributes containing the transformed cards to the Content Card UI.
let viewController = BrazeContentCardUI.ViewController(braze: AppDelegate.braze, attributes: attributes)
```

{% endsubtab %}
{% subtab Objective-C %}

```objc
// Filter cards by the `Transactional` feed type based on your key-value pair.
NSMutableArray<BRZContentCardRaw *> *transactionalCards = [[NSMutableArray alloc] init];
for (BRZContentCardRaw *card in AppDelegate.braze.contentCards.cards) {
  if ([card.extras[@"feed_type"] isEqualToString:@"Transactional"]) {
    [transactionalCards addObject:card];
  }
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}